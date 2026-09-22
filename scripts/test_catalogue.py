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
GENERATED = ('README.md', 'CATALOG.md', 'RESOLVED.md')


class CatalogueTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='aim-catalogue-test-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ('data', 'problems', 'research', 'scripts'):
            shutil.copytree(ROOT / name, self.root / name)
        for name in (*GENERATED, 'CONTRIBUTING.md', 'CITATION.cff', 'catalogue.json'):
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

    def active_entries(self):
        manifest = self.read_json('catalogue.json')
        return [row for group in manifest['groups']
                for row in self.read_json(f"data/{group['key']}.json")]

    def section(self, text, heading):
        return text.split(f'## {heading}\n', 1)[1].split('\n## ', 1)[0]

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

    def test_browsing_is_separate_from_readme(self):
        self.run_catalogue()
        readme = (self.root / 'README.md').read_text()
        catalogue = (self.root / 'CATALOG.md').read_text()
        resolved = (self.root / 'RESOLVED.md').read_text()
        manifest = self.read_json('catalogue.json')
        entries = self.active_entries()
        self.assertTrue(readme.startswith('# AIM — Open Applied Problems\n'))
        self.assertIn(f'**{len(entries)} open targets**', readme)
        self.assertIn('](CATALOG.md)', readme)
        self.assertIn('](RESOLVED.md)', readme)
        self.assertIn('](CITATION.cff)', readme)
        self.assertNotRegex(readme, r'(?m)^\| \d{3,} \|')
        self.assertNotIn('| Publication batch |', readme)
        self.assertIn('| Publication batch |', catalogue)
        for group in manifest['groups']:
            self.assertNotIn(f"## {group['title']}\n", readme)
            section = self.section(catalogue, group['title'])
            for row in self.read_json(f"data/{group['key']}.json"):
                self.assertIn(f"| {row['id']} |", section)
                self.assertIn(f"]({row['file']})", section)
        for row in manifest['retired']:
            self.assertNotIn(f"| {row['id']} |", catalogue)
            self.assertIn(f"| {row['id']} |", resolved)
            self.assertIn(f"]({row['record']})", resolved)
        claimed = self.section(resolved, 'Solution claimed')
        self.assertIn('| 077 |', claimed)
        self.assertNotIn('| 077 |', self.section(resolved, 'Solved'))

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

    def test_stale_outputs_are_detected_and_regenerated(self):
        self.run_catalogue()
        for name in GENERATED:
            with self.subTest(name=name):
                path = self.root / name
                original = path.read_text()
                path.write_text(original + 'Stale output\n')
                self.run_catalogue('--check', expected=1, message=f'{name} is stale')
                self.run_catalogue()
                self.assertEqual(path.read_text(), original)
                self.run_catalogue('--check')

    def test_missing_outputs_are_detected_and_regenerated(self):
        self.run_catalogue()
        originals = {name: (self.root / name).read_text() for name in GENERATED}
        for name in GENERATED:
            with self.subTest(name=name):
                (self.root / name).unlink()
                self.run_catalogue('--check', expected=1, message=f'{name} is missing')
                self.run_catalogue()
                self.assertEqual((self.root / name).read_text(), originals[name])
                self.run_catalogue('--check')
        for name in GENERATED:
            (self.root / name).unlink()
        self.run_catalogue('--check', expected=1, message='README.md is missing')
        self.run_catalogue()
        for name in GENERATED:
            self.assertEqual((self.root / name).read_text(), originals[name])
        self.run_catalogue('--check')

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
        catalogue = (self.root / 'CATALOG.md').read_text()
        spectral = self.section(catalogue, 'Spectral theory and spectral geometry')
        operators = self.section(catalogue, 'Operators, matrices and computation')
        self.assertIn(f'| {ids[0]} |', spectral)
        self.assertIn(f'| {ids[2]} |', spectral)
        self.assertNotIn(f'| {ids[1]} |', spectral)
        self.assertIn(f'| {ids[1]} |', operators)
        self.assertIn(f'**{len(self.active_entries())} open targets**', readme)
        self.assertNotRegex(readme, r'(?m)^\| \d{3,} \|')

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
        manifest['retired'].append({'id': '001', 'reason': 'Test only',
                                    'record': 'research/METHODOLOGY.md'})
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
        manifest['retired'].append({'id': row['id'], 'reason': 'Test only', 'record': record})
        self.write_json('catalogue.json', manifest)
        self.run_catalogue()
        self.run_catalogue('--check')
        resolved = (self.root / 'RESOLVED.md').read_text()
        self.assertIn(f"[Entry {row['id']}]({record})",
                      self.section(resolved, 'Other retained entries'))
        self.assertIn('| 077 |', self.section(resolved, 'Solution claimed'))
        self.assertIn(f'**{len(self.active_entries())} open targets**',
                      (self.root / 'README.md').read_text())

    def test_retained_status_sections(self):
        manifest = self.read_json('catalogue.json')
        first_id = max(int(i) for batch in manifest['batches'] for i in batch['ids']) + 1
        fixtures = []
        for offset, status in enumerate(('Solved', 'Solution claimed', 'Retired')):
            identifier = f'{first_id + offset:03d}'
            row = {'id': identifier, 'title': f'Temporary {status.lower()} target',
                   'status': status, 'reason': f'Temporary review for {identifier}',
                   'record': f'research/test-{identifier}.md'}
            (self.root / row['record']).write_text(f"# {row['title']}\n")
            manifest['retired'].append(row)
            fixtures.append(row)
        manifest['batches'].append({'key': 'retained-test', 'title': 'Retained test',
                                   'ids': [row['id'] for row in fixtures]})
        self.write_json('catalogue.json', manifest)
        self.run_catalogue()
        self.run_catalogue('--check')
        resolved = (self.root / 'RESOLVED.md').read_text()
        catalogue = (self.root / 'CATALOG.md').read_text()
        headings = ('Solved', 'Solution claimed', 'Other retained entries')
        for row, heading in zip(fixtures, headings):
            with self.subTest(status=row['status']):
                section = self.section(resolved, heading)
                self.assertIn(f"| {row['id']} |", section)
                self.assertIn(f"[{row['title']}]({row['record']})", section)
                self.assertIn(row['reason'], section)
                self.assertNotIn(f"| {row['id']} |", catalogue)
                for other_heading in headings:
                    if other_heading != heading:
                        self.assertNotIn(f"| {row['id']} |",
                                         self.section(resolved, other_heading))
        self.assertIn(f'**{len(self.active_entries())} open targets**',
                      (self.root / 'README.md').read_text())

    def test_invalid_optional_retirement_metadata(self):
        for field, values in (('title', ('', '   ', None, 123)),
                              ('status', ('', 'solved', 'Open', None, 123, [], {}))):
            for value in values:
                with self.subTest(field=field, value=value):
                    manifest = self.read_json('catalogue.json')
                    original = dict(manifest['retired'][0])
                    manifest['retired'][0][field] = value
                    self.write_json('catalogue.json', manifest)
                    self.run_catalogue(expected=1, message=f'invalid retired {field}')
                    manifest['retired'][0] = original
                    self.write_json('catalogue.json', manifest)


if __name__ == '__main__':
    unittest.main()
