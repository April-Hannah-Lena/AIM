#!/usr/bin/env python3
"""Catalogue integrity tests on disposable copies; standard library only."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class CatalogueTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='aim-catalogue-test-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ('data', 'problems', 'research', 'scripts'):
            shutil.copytree(ROOT / name, self.root / name)
        for name in ('README.md', 'CONTRIBUTING.md', 'catalogue.json'):
            shutil.copy2(ROOT / name, self.root / name)

    def run_catalogue(self, mode='--write', expected=0, message=None):
        result = subprocess.run([sys.executable, 'scripts/catalogue.py', mode],
                                cwd=self.root, capture_output=True, text=True)
        self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
        if message:
            self.assertIn(message, result.stdout)

    def read_json(self, name):
        return json.loads((self.root / name).read_text())

    def write_json(self, name, value):
        (self.root / name).write_text(json.dumps(value, indent=2) + '\n')

    def change_row(self, edit):
        rows = self.read_json('data/spectral.json')
        edit(rows)
        self.write_json('data/spectral.json', rows)

    def change_page(self, edit):
        row = self.read_json('data/spectral.json')[0]
        path = self.root / row['file']
        path.write_text(edit(path.read_text()))

    def test_baseline_and_preservation(self):
        originals = {p.relative_to(self.root): p.read_bytes()
                     for p in (self.root / 'problems').glob('*.md')}
        self.run_catalogue()
        self.run_catalogue('--check')
        self.assertTrue(all((self.root / p).read_bytes() == text
                            for p, text in originals.items()))

    def test_duplicate_id(self):
        self.change_row(lambda rows: rows.append(dict(rows[0])))
        self.run_catalogue(expected=1, message='Duplicate ID')

    def test_duplicate_file(self):
        self.change_row(lambda rows: rows[1].update(file=rows[0]['file']))
        self.run_catalogue(expected=1, message='Duplicate file')

    def test_missing_metadata(self):
        self.change_row(lambda rows: rows[0].pop('status'))
        self.run_catalogue(expected=1, message='incomplete metadata')

    def test_missing_heading(self):
        self.change_page(lambda text: text.replace('## References', '## Reading'))
        self.run_catalogue(expected=1, message='missing References')

    def test_metadata_mismatch(self):
        self.change_row(lambda rows: rows[0].update(area='Incorrect area'))
        self.run_catalogue(expected=1, message='inconsistent Area')

    def test_unindexed_page(self):
        (self.root / 'problems/unindexed.md').write_text('# Unindexed\n')
        self.run_catalogue(expected=1, message='Unindexed problem file')

    def test_missing_page(self):
        row = self.read_json('data/spectral.json')[0]
        (self.root / row['file']).unlink()
        self.run_catalogue(expected=1, message='Missing problems/')

    def test_invalid_date(self):
        self.change_row(lambda rows: rows[0].update(last_checked='2026-02-30'))
        self.run_catalogue(expected=1, message='invalid ISO date')

    def test_future_date(self):
        self.change_row(lambda rows: rows[0].update(last_checked='9999-01-01'))
        self.run_catalogue(expected=1, message='status check is in the future')

    def test_broken_local_link(self):
        self.change_page(lambda text: text + '\n[Missing](../missing.md)\n')
        self.run_catalogue(expected=1, message='broken local link')

    def test_stale_output(self):
        self.run_catalogue()
        path = self.root / 'README.md'
        path.write_text(path.read_text() + 'Stale output\n')
        self.run_catalogue('--check', expected=1, message='README is stale')

    def test_noncontiguous_grouping_and_counts(self):
        manifest = self.read_json('catalogue.json')
        first_id = max(int(i) for batch in manifest['batches'] for i in batch['ids']) + 1
        ids = []
        for offset, stem in enumerate(('spectral', 'operators', 'spectral')):
            rows = self.read_json(f'data/{stem}.json')
            original = rows[0]
            row = dict(original)
            row['id'] = f'{first_id + offset:03d}'
            row['title'] = 'Temporary test ' + row['id']
            row['file'] = f"problems/{row['id']}-temporary-test.md"
            content = (self.root / original['file']).read_text()
            content = content.replace(original['id'], row['id'], 1)
            content = content.replace(original['title'], row['title'], 1)
            (self.root / row['file']).write_text(content)
            rows.append(row)
            self.write_json(f'data/{stem}.json', rows)
            ids.append(row['id'])
        manifest['batches'].append({'key': 'test', 'title': 'Temporary test', 'ids': ids})
        self.write_json('catalogue.json', manifest)
        self.run_catalogue()
        self.run_catalogue('--check')
        readme = (self.root / 'README.md').read_text()
        spectral = readme.split('## Spectral theory and spectral geometry\n')[1].split('\n## ')[0]
        operators = readme.split('## Operators, matrices and computation\n')[1].split('\n## ')[0]
        self.assertIn(f'| {ids[0]} |', spectral)
        self.assertIn(f'| {ids[2]} |', spectral)
        self.assertNotIn(f'| {ids[1]} |', spectral)
        self.assertIn(f'| {ids[1]} |', operators)
        self.assertIn(f'# AIM — {first_id + 2} Open Applied Problems', readme)

    def test_missing_batch_membership(self):
        manifest = self.read_json('catalogue.json')
        manifest['batches'][0]['ids'].pop()
        self.write_json('catalogue.json', manifest)
        self.run_catalogue(expected=1, message='batches must partition')

    def test_unregistered_metadata(self):
        self.write_json('data/unregistered.json', [])
        self.run_catalogue(expected=1, message='Unregistered metadata')

    def test_retired_id_cannot_be_reused(self):
        manifest = self.read_json('catalogue.json')
        manifest['retired'] = [{'id': '001', 'reason': 'Test only',
                                'record': 'research/METHODOLOGY.md'}]
        self.write_json('catalogue.json', manifest)
        self.run_catalogue(expected=1, message='Duplicate ID')

    def test_documented_retirement_preserves_id(self):
        manifest = self.read_json('catalogue.json')
        all_rows = [(group['key'], row) for group in manifest['groups']
                    for row in self.read_json(f"data/{group['key']}.json")]
        stem, row = max(all_rows, key=lambda pair: int(pair[1]['id']))
        rows = self.read_json(f'data/{stem}.json')
        self.write_json(f'data/{stem}.json', [r for r in rows if r['id'] != row['id']])
        old_path = self.root / row['file']
        record = f"research/retired-{row['id']}.md"
        old_path.rename(self.root / record)
        for path in self.root.rglob('*.md'):
            content = path.read_text().replace(row['file'], record)
            if path.parent == self.root / 'problems':
                content = content.replace(f']({old_path.name})', f'](../{record})')
            path.write_text(content)
        manifest['retired'] = [{'id': row['id'], 'reason': 'Test only', 'record': record}]
        self.write_json('catalogue.json', manifest)
        self.run_catalogue()
        self.run_catalogue('--check')


if __name__ == '__main__':
    unittest.main()
