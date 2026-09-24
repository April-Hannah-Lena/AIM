#!/usr/bin/env node
// Render the exact TeX recovered from GFM, rather than regex-extracted source.
const fs = require('fs');
let mathjax, TeX, SVG, liteAdaptor, RegisterHTMLHandler;
try {
  ({mathjax} = require('mathjax-full/js/mathjax.js'));
  ({TeX} = require('mathjax-full/js/input/tex.js'));
  ({SVG} = require('mathjax-full/js/output/svg.js'));
  ({liteAdaptor} = require('mathjax-full/js/adaptors/liteAdaptor.js'));
  ({RegisterHTMLHandler} = require('mathjax-full/js/handlers/html.js'));
  require('mathjax-full/js/input/tex/ams/AmsConfiguration.js');
  require('mathjax-full/js/input/tex/boldsymbol/BoldsymbolConfiguration.js');
} catch (error) {
  console.error('Install mathjax-full@3.2.2 and set NODE_PATH; see CONTRIBUTING.md for math QA setup.');
  process.exit(1);
}
const adaptor = liteAdaptor();
RegisterHTMLHandler(adaptor);
const document = mathjax.document('', {
  // Do not enable noerrors/noundefined: those can hide compilation failures.
  InputJax: new TeX({packages: ['base', 'ams', 'boldsymbol']}),
  OutputJax: new SVG({fontCache: 'none'}),
});

function render(tex, display) {
  const svg = adaptor.outerHTML(document.convert(tex, {display}));
  if (svg.includes('data-mjx-error=') || svg.includes('data-mml-node="merror"')) {
    throw new Error(svg.match(/data-mjx-error="([^"]*)"/)?.[1] || 'MathJax error node');
  }
}

// Check that parser failures are detected even when MathJax returns an error SVG.
for (const invalid of [
  String.raw`\left{x\right}`,
  String.raw`\begin{aligned}x&=1\tag{1}\end{aligned}`,
  String.raw`\AIMUnknownCommand{x}`,
]) {
  let caught = false;
  try { render(invalid, true); } catch { caught = true; }
  if (!caught) throw new Error('MathJax failure detection self-test failed');
}
render(String.raw`\left\{x\right\}`, true);
render(String.raw`\begin{aligned}x&=1\end{aligned}\tag{1}`, true);

const equations = JSON.parse(fs.readFileSync(0, 'utf8'));
const failures = [];
for (const [index, equation] of equations.entries()) {
  try { render(equation.tex, equation.display); }
  catch (error) { failures.push(`${equation.file}:${equation.line}: ${error.message}`); }
  if ((index + 1) % 2000 === 0) console.log(`MathJax rendered ${index + 1}/${equations.length} equations.`);
}
if (failures.length) {
  console.error(failures.join('\n'));
  process.exit(1);
}
console.log(`MathJax rendered all ${equations.length} equations without errors.`);
