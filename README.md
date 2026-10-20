<div align="center">
  <img src="docs/banner.svg" width="860" alt="GEO Lab: a living textbook on Generative Engine Optimization" />
  <h1>GEO Lab</h1>
  <p><strong>English</strong> · <a href="README.zh-Hant.md">繁體中文</a> · <a href="README.zh-Hans.md">简体中文</a></p>
  <p><strong>A living textbook on Generative Engine Optimization (GEO), updated with new research and original experiments.</strong></p>
  <p>How AI search finds, reads, cites and recommends websites · Evidence-graded · Always updated</p>
  <p>
    <img src="https://img.shields.io/badge/version-0.6.0-0f172a?style=flat-square" alt="version 0.6.0" />
    <a href="LICENSE-CONTENT.txt"><img src="https://img.shields.io/badge/content-CC%20BY--NC--ND%204.0-e8a181?style=flat-square" alt="content license CC BY-NC-ND 4.0" /></a>
    <a href="LICENSE"><img src="https://img.shields.io/badge/code-MIT-e8a181?style=flat-square" alt="code license MIT" /></a>
    <img src="https://img.shields.io/badge/languages-EN%20%7C%20%E7%B9%81%E4%B8%AD%20%7C%20%E7%AE%80%E4%B8%AD-1e3a5f?style=flat-square" alt="languages: English, Traditional Chinese, Simplified Chinese" />
    <img src="https://img.shields.io/badge/papers-579-1e3a5f?style=flat-square" alt="579 papers" />
    <img src="https://img.shields.io/badge/updated-2026--10--20-1e3a5f?style=flat-square" alt="last updated 2026-10-20" />
  </p>
  <p>
    <a href="#why-this-book">Why this book</a> ·
    <a href="#whats-inside">What's inside</a> ·
    <a href="#read-it">Read it</a> ·
    <a href="#how-it-is-built">How it is built</a> ·
    <a href="#how-evidence-is-graded">Evidence grades</a> ·
    <a href="CHANGELOG.md">Changelog</a> ·
    <a href="#about-the-author">Author</a> ·
    <a href="#license">License</a>
  </p>
</div>

## Why this book

AI search engines such as ChatGPT, Gemini and Perplexity now answer questions directly and name a handful of sources. Which websites make that list, and why? Most advice on this topic is either personal experience or marketing. This book separates **what research has shown** from **what practitioners believe**, and keeps both up to date as the engines change.

<table>
  <tr>
    <td width="33%"><strong>Evidence-graded</strong><br /><br />Built from 579 research papers and about 140,000 practitioner discussions. Every claim states how strong its evidence is, from randomized experiments with real users down to single observations.</td>
    <td width="33%"><strong>Always updated</strong><br /><br />New papers are screened regularly. Every change gets a version number and a <a href="CHANGELOG.md">changelog</a> entry, and claims are dated because AI search changes fast.</td>
    <td width="33%"><strong>Original experiments</strong><br /><br />We test AI search engines ourselves, across models and over time. Findings go into the book together with their method and limits.</td>
  </tr>
  <tr>
    <td><strong>Seven gates</strong><br /><br />The book follows an answer through seven stages: whether AI searches at all, whether it can reach your page, recall, selection, citation, faithful use, and what happens to traffic.</td>
    <td><strong>Two editions</strong><br /><br />A plain-language edition for everyone, and a research edition with evidence tables and source tracing.</td>
    <td><strong>Three languages</strong><br /><br />English, Traditional Chinese and Simplified Chinese, kept in sync with every release.</td>
  </tr>
</table>

## What's inside

| Folder | Content |
|---|---|
| [`book/en/`](book/en/) | Plain-language edition, English |
| [`book/zh-hant/`](book/zh-hant/) | Plain-language edition, Traditional Chinese |
| [`book/zh-hans/`](book/zh-hans/) | Plain-language edition, Simplified Chinese |
| [`book/research-zh-hant/`](book/research-zh-hant/) | Research edition with evidence tables (Traditional Chinese) |
| [`website/`](website/) | Static website for all three languages |
| [`papers/`](papers/) | Paper index and close-reading notes (no PDFs) |
| [`framework/`](framework/) | Textbook framework and data-review method |
| [`scripts/`](scripts/) | Build, conversion and checking scripts |

## Read it

- **On GitHub:** start with [`book/en/00_Contents.md`](book/en/00_Contents.md).
- **As a website:** open `website/index.html` in a browser, or serve it locally:

```bash
python -m http.server 8765 --directory website
```

Then visit http://localhost:8765 . On Windows you can also double-click `start-website.bat`.

## How it is built

1. **Research papers.** Papers on generative search, retrieval and AI citation are collected from arXiv, screened, and read in full. Each one gets a structured note and an evidence grade.
2. **Practitioner discussions.** About 140,000 posts and comments from GEO and SEO communities are classified by several language models, with agreement checked statistically. Soft advertising and duplicated posts are filtered out, and recurring claims are tested for real consensus.
3. **Original experiments.** We query AI search engines through their APIs, record what they search, which pages they see and which they cite, and compare models over time.
4. **Writing and checking.** Every number in the plain-language editions must exist in the research edition; translations are checked for structure and numbers.

## How evidence is graded

| Grade | Study design |
|---|---|
| A | Randomized field experiments or strong quasi-experiments with real users |
| B | Real commercial AI search engines, measured repeatedly |
| C | Commercial systems with manually supplied pages |
| D | Reproducible retrieval-and-generation pipelines |
| E | Fixed contexts, simulations or theory |

Practitioner reports are labeled separately and never presented as proof.

## About the author

<table>
  <tr>
    <td width="180" valign="top"><img src="docs/author.jpg" width="160" alt="Portrait of the author" /></td>
    <td valign="top">
      <strong>ivantsai1982</strong><br /><br />
      I first went online in 1999 and have worked in the internet industry since 2003. I began studying search engine optimization in 2005 and have since written several books on SEO and published research papers. Since 2007 I have worked on the front line of SEO, combining hands-on practice with research.<br /><br />
      In 2022, as AI began answering questions directly, I turned to generative engine optimization, and I have been studying it ever since. More than twenty years of SEO have taught me one thing above all: search keeps changing, and most advice cannot keep up. GEO Lab is my attempt to build a textbook that does: every claim tied to evidence, every change versioned, every update open.
    </td>
  </tr>
</table>

## License

- **Textbook content, website, notes and framework documents:** [CC BY-NC-ND 4.0](LICENSE-CONTENT.txt). You may share them unmodified, with attribution, for non-commercial purposes. Modified versions, including translations, may not be distributed.
- **Code:** [MIT](LICENSE).

## How to cite

> ivantsai1982. *GEO Lab: A Living Textbook on Generative Engine Optimization*, version 0.6.0. https://github.com/ivantsai1982/geo-lab

Please include the version number, because the content changes over time.
