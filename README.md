# GEO Lab

**English** · [繁體中文](README.zh-Hant.md)

**A living textbook on Generative Engine Optimization (GEO), updated with new research and original experiments.**

How do AI search engines such as ChatGPT, Gemini and Perplexity decide which websites to find, read, cite and recommend? This repository answers that question as a textbook that keeps being updated:

- **Evidence-graded.** Built from 579 research papers and about 140,000 practitioner discussions. Every claim is labeled by the strength of its evidence: large-scale real-user experiments, repeated tests on real AI search engines, controlled lab systems, simulations, or practitioner reports.
- **Always current.** New papers are screened and added regularly. Every change gets a version number and an entry in the [changelog](CHANGELOG.md).
- **Original experiments.** We run our own tests on AI search engines; the findings are written into the textbook together with their method and limits.
- **Multilingual.** English, Traditional Chinese and Simplified Chinese.

Current version: [VERSION](VERSION) · Changelog: [CHANGELOG.md](CHANGELOG.md)

## What's inside

| Folder | Content |
|---|---|
| `book/en/` | Plain-language edition, English |
| `book/zh-hant/` | Plain-language edition, Traditional Chinese |
| `book/zh-hans/` | Plain-language edition, Simplified Chinese |
| `book/research-zh-hant/` | Research edition with evidence tables (Traditional Chinese) |
| `website/` | Static website for all three languages |
| `papers/` | Paper index and close-reading notes (no PDFs) |
| `framework/` | Textbook framework and data-review method |
| `scripts/` | Build, conversion and checking scripts |

## Read it

Open `website/index.html` in a browser, or serve it locally:

```bash
python -m http.server 8765 --directory website
```

Then visit http://localhost:8765 . On Windows you can also double-click `start-website.bat`.

## License

- **Textbook content, website, notes and framework documents:** [CC BY-NC-ND 4.0](LICENSE-CONTENT.txt). You may share them unmodified, with attribution, for non-commercial purposes. Modified versions, including translations, may not be distributed.
- **Code:** [MIT](LICENSE).

## How to cite

> ivantsai1982. *GEO Lab: A Living Textbook on Generative Engine Optimization*, version x.y.z. https://github.com/ivantsai1982/geo-lab

Please include the version number, because the content changes over time.
