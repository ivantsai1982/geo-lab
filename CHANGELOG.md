# Changelog

All editions (research edition, plain-language editions in English, Traditional Chinese and Simplified Chinese) share one version number.

Versioning: **MAJOR.MINOR.PATCH**
- MAJOR: structural changes (chapters added or removed, principles rewritten)
- MINOR: new content (new papers, new experiments, new cases)
- PATCH: corrections (typos, numbers, added caveats)

Versions before 1.0.0 are the pre-release phase.

## [0.7.0] - 2026-10-20
### Changed
- Plain-language editions (all 17 chapters) rewritten prose-first so the book reads like a book rather than a list of bullet points: paragraphs instead of lists, far less bold, no label templates, fewer subheadings, tables kept only where they compare real data, no horizontal rules. No principle, number, case, caveat or evidence-strength wording was added or removed; every chapter was checked number by number against the previous version.
- English edition retranslated from the rewritten Traditional Chinese chapters. Chapter titles now use the form "Chapter N: Title", and the text uses no em dashes.
- Simplified Chinese edition reconverted from the rewritten Traditional Chinese chapters.
- Research edition: light formatting pass only (horizontal rules removed, label templates unbolded, at most two bold phrases per section). Evidence tables and wording unchanged.
- Contents pages, word counts and full-book files regenerated for all editions.
### Fixed
- Simplified Chinese conversion script now writes LF line endings on Windows.

## [0.6.0] - 2026-10-20
### Added
- Ch. 3: "AI did not read the latest version" split into two cases: reading a cached copy, and not opening the page at all
- Ch. 4: search behaviour of ChatGPT's fast and thinking modes; every page ChatGPT cites comes from its own search, and whether a page is retrieved matters far more than its features; AI engines read location through different channels (ChatGPT follows the declared city, Gemini follows the network's country)
- Ch. 5: the brand prior also acts on search queries, source selection and the answer; the share of citations going to a party's own websites varies by field
- Ch. 7: research evidence for "cited does not mean opened"
- Ch. 8: structural fields assessed separately (paragraphs and titles that match the question help; FAQ, structured data, summary boxes and page speed show no clear effect within the same website); rewriting without a specified target barely works
- Ch. 9: API vs. web interface compared at URL and domain level; thinking mode changes search behaviour
### Changed
- Ch. 4: "write the city into the sentence" limited to Gemini and Google AI Overviews; location debate updated
- Ch. 6: caveat on the advantage of recent dates in real-world settings
- Ch. 12: caveat on "asking in Chinese switches to Chinese sources" for ChatGPT
### Sources
- 5 new papers: 2610.15382, 2610.15033, 2610.24081, 2610.21731, 2610.21330

## [0.5.0] - 2026-10-11
### Added
- Ch. 11: whether posts on platforms that AI favours enter citations; disclosing interests is necessary but does not stop AI persuasion
- Ch. 9: real multi-turn conversation logs; the baseline is part of the definition; AI judges may measure the wrong thing
- Ch. 15: new evidence row; the "gap" split into two layers; deleting a post does not stop citations
- Ch. 13: whether descriptions are symmetric
### Changed
- Ch. 6 principle 6.4, Ch. 11 "verifiable facts", Ch. 4 (language vs. location, short prompts), Ch. 8 and Ch. 15 (caveats for the goal of AI citation)
### Sources
- 6 new papers: 2610.11932, 2607.22392, 2602.16136, 2603.23474, 2604.04263, 2609.18282

## [0.4.1] - 2026-10-07
### Added
- Ch. 5: "Where the prior comes from" (being written about a lot vs. being written about alongside the right things; two timelines)

## [0.4.0] - 2026-10-04
### Added
- Ch. 3–7: the author's own ChatGPT retrieval experiments (40 sessions via the API)
- Ch. 3: OpenAI's official documentation (third-party search providers, crawler roles, noindex, ARIA)
- Writing guide: new evidence label for the author's own small-scale tests

## [0.3.0] - 2026-10-03
### Added
- Ch. 4, 6, 7, 9, 10, 12, 14: a randomized field experiment on a major newspaper's on-site AI search; evidence-selection bias in deep research agents; conversational capture in multi-turn dialogue
### Sources
- 3 new papers: 2609.38946, 2609.39026, 2609.40069

## [0.2.1] - 2026-10-03
### Fixed
- Ch. 3: "ChatGPT relies on Google's index" was an unsupported remark; corrected and made consistent with Ch. 4
- Ch. 3: classification of OAI-SearchBot

## [0.2.0] - 2026-10-01
### Added
- Plain-language edition (Traditional Chinese), fully rewritten
- Simplified Chinese and English editions
- Website (English, Traditional Chinese, Simplified Chinese)

## [0.1.0] - 2026-09-30
### Added
- First draft of the research edition (Chapters 0–15, Appendix A)
