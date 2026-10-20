# Chapter 3: Accessibility: Source map

> The ids below do not appear in the main text. Papers are identified by arXiv-style numbers; forum entries by evidence-pack ids; consensus items by cluster numbers.
> Section F of the evidence pack (leads to check with commercial relationships) is excluded; its only use is the sentence in the main text "A vendor claims …, but this has not been independently verified", see Debate 1.

## 1. Questions this chapter answers
- Based on Chapter 3 of the framework (Principles 3.1, 3.2, debates, questions to verify).

## 2. Core principles

### Principle 3.1 If it can't be read, it doesn't exist
- Blocking Google-Extended → zero Gemini citations, fewer AIO citations: 2604.27790 (B, SIGIR'26, correlation)
- Failure takes the form of omission rather than fabrication, substituting third parties/competitors: 2609.34951 (B, vendor)

### Principle 3.2 Division of labour among crawlers
- OpenAI's four identities (GPTBot / OAI-SearchBot / ChatGPT-User / OAI-AdsBot): p_1w1m6ve (R-B); c_pa8lb5v (R-B, those with User are real-time fetching)
- meta-externalagent handles both training and indexing: c_p6twy0w (R-B)
- 79% of domains block at least one AI crawler; blockers' mean ChatGPT referral traffic 6.48 vs 4.48; blocking training crawlers does not stop ChatGPT referral traffic: 2607.07652 appendix OA.5 (correlational part of an A study)
- Only 7–10% of answers come from training knowledge: 2609.34951 §5.3

### Principle 3.3 Three layers of blocking
- Consensus on CDN/WAF-layer blocking: cluster 212 (38 for / 9 against), high-evidence entries p_1s04hc7, p_1srlq0o
- CDN "AI crawler" switch inserts managed robots rules: p_1srlq0o (R-C)
- From 2026-09-15, mixed-purpose crawlers blocked on pages with ads; websites without ads not affected: c_p8pfmj3 (R-B, including the context of the post body)
- Enforcement-layer blocking does not appear in robots.txt: c_p6txr1i (R-D), c_p3xw4nn (R-D)

### Principle 3.4 Raw response vs rendering
- Consensus that most AI crawlers do not execute JS: cluster 161 (23 / 1), cluster 143 (9 / 0)
- 6-platform test, 3 do not execute JS, 0.5–3 seconds; 9 of 11 metadata categories zero, only title; 62 elements: p_1s9l4be (R-B)
- 34 of 50 sites (68%) inject JSON-LD via GTM; server-side 92% vs GTM-only 0%: p_1sfl8mz (R-B)
- hreflang raw 0 / DOM 3; no-store: c_p766ck6 (R-B)
- Lost content types in the table: prices c_p079ku7, c_p07xea8 (R-D); carousels c_p5kftwi (R-C); FAQ accordions c_p071c75 (R-D); animated headlines c_oyuzbsl (R-D); structured data p_1sfl8mz; language tags c_p766ck6

### Principle 3.5 Indexes
- Jaccard 0.11–0.18 for sources across three interfaces: 2604.27790 Table 2
- ChatGPT relies on Google's index: c_o8qlajn (R-B)
- OAI-SearchBot builds the ChatGPT search index: p_1w1m6ve, c_pa8lb5v
- Four AIs reading a test page (ChatGPT failed about 10 times, Claude only the first time, Perplexity 14 unrelated pages, Gemini read everything including schema): c_oupsdwq, c_ouppe67, c_ow3q5jl (R-B, same author)
- New entity 23 days, cited on day 6, 403 on 22/23 days, real-time fetching let through the same day, 119x vs 0x: p_1tzk4z9 (R-A)

### Principle 3.6 Agent experience
- 1,056 companies, 37,927 journeys, 78% vs 58%, 20% vs 11%, composition of the bundled score, no independent effect of off-site mentions after controlling for AX (drill-down only): 2609.34951 (B, vendor, matched observation)
- 49.3% → 89.3%, steps 9.31 → 6.49, single synthetic website, not separated: 2607.12056 (D)
- 46.4% vs 28.0%, 40 questions vs 56 questions, last mile: 2605.28787 (C)

## 3. How strong is the evidence
- Combined from the above; "a single late-2024 analysis" per c_p766ck6.
- Crawl volume is not enough to measure visibility: cluster 118 (5 / 0)

## 4. Debates and counterexamples

### Debate 1 llms.txt
- 16.9% (177/1,047), unrelated to accuracy (-0.04): 2607.14197 (B)
- 38 KB file, 299 requests, 240 own monitoring, 59 real, only 2 AI (Amazonbot); GPTBot 920, ClaudeBot 1,494, OAI-SearchBot 631: p_1whtxtr (R-B)
- Billions of log lines with no requests: c_o8qlajn (R-B); 100+ websites with no requests: c_nr0ef7k (R-B)
- Consensus: cluster 192 (33 / 4), cluster 175 (8 / 0); see also clusters 190, 200, 210
- 200-query dataset, <3% with llms.txt, never cited: c_o8j5n94 (R-D); added for a month then removed, no change: c_onspspx (R-D)
- Google official documentation vs testing tool adding a check: c_p3jbukc (R-D post context), c_ossmame (R-D), c_on0gi9i (R-D, tool can only confirm existence)
- 50 companies n=5, 77% vs 49%: p_1u73adl (R-D)
- Value of sorting out pages: c_olf4qe8 (R-D); technical documentation websites: c_ohiqxgy (R-D), p_1whtxtr (coding agents)
- The "A vendor claims" sentence: c_on1eyea, p_1u362hg (section F, commercial relationship, not used as evidence)
- Framework conclusion: 2607.14197 and 2609.34951 → no evidence it is effective on its own

### Debate 2 Markdown
- Real-time fetching reads only HTML (ChatGPT-User 1,936/0, PerplexityBot 306/0, Claude-User 38/1; training and index 177 fetches of 56 files): p_1uvlwe8 (R-B)
- Two small blogs over three months: p_1wfcneh (R-B)
- Mirror crawled by Google within days, no change in citation rate over 60 days: c_os6hjba, c_oswaf69 (R-B)
- 16 URLs +52% vs +43%: p_1up6rkk (R-B)
- 381-page A/B about 1 visit: p_1rewp9q (R-D)
- 20 md articles, crawl rate doubled (other side): p_1r1uc4g (R-B)
- 2,592 / 962 tokens, 7 sites, 6 missing Vary, 3 lost body text: p_1w1q92b, p_1w1q637, c_p7ccdzw (R-D)
- Do not send Accept: text/markdown: c_p6sbt2h (R-D)

### Debate 3 JSON-LD
- Zero reads: p_1s9l4be; schema not used: c_o8xxexh (R-C)
- 92%: p_1sfl8mz; Gemini restates schema: c_ow3q5jl; put in the same HTML: p_1uvlwe8

### Debate 4 Source of the JS rendering consensus
- Single 2024-12 analysis, 20 months, publisher sells SSR: c_p766ck6 (R-B)
- Training crawler makes a small number of JS requests: c_obsvqvj (R-D)

### Debate 5 Compliance with robots.txt
- GPTBot and Meta-WebIndexer do not check: p_1s04hc7 (R-B)
- Eight-assistant test: p_1vsr4er (R-B)

### Debate 6 Whether accessibility is a bottleneck
- 513,554 sites 16.8%: p_1ucgsw1 (R-D)
- Law firms 1.8%, home services 5.4%, travel 3.0%: c_p3nxg7k (R-D)
- 131 sites about 21%: c_p3xvasd (R-D)
- About 3,000 sites 27%: p_1r05rxp, p_1r8b5b7 (R-D)
- About 17,000 French small businesses: c_p3jbukc, c_p3nqbiq, c_oz6ad0m (R-D)
- Tests with claimed identities are not equal to real crawlers: c_p3nqbiq, c_p1h6n8u (R-D)
- About 100,000 pages, about 430,000 fetches in 30 days, crawl volume unrelated to citation: c_p8pfmj3 (R-B)

## 5. Cases
- Case 1: p_1tzk4z9 (R-A)
- Case 2: p_1srlq0o (R-C)
- Case 3: p_1ryxiap (R-B, 50 local businesses, 2–4 weeks); c_p6twy0w, c_p6tydmw (small business sample of 10 sites, 4 catch-all, 9 blocking meta-externalagent, plugin default)
- Case 4: c_p079ku7, c_p07xea8, c_p0miode (R-D)
- Case 5: p_1u0a0z9 (R-A, /ai/ parallel version, 5 weeks, +12% / +60%)
- Case 6: 2609.34951
- Counterexample: c_osn2xae, c_osn4vv5 (R-D)

## 6. What to do
- Separate the three types of identities: p_1tzk4z9, p_1w1m6ve, c_pa8lb5v, c_p84c66f (R-B, 14 of the 19 sites refusing GPTBot allow answering identities)
- Google-Extended: 2604.27790
- 72 companies 18 / 11 / 0: p_1w1m6ve
- URL-pasting test: c_p6yixw8 (R-B)
- 11 sites, 2/10 comparisons differ by double: c_p1h6n8u (R-D)
- SSR / static HTML, GTM for tracking only: cluster 161, p_1sfl8mz
- Prerendering drift: c_p0miode
- Facts in HTML: p_1uvlwe8
- Server logs, GA cannot see: p_1s04hc7, p_1wfcneh (hosting platform about one hour of logs)
- 394 impersonating IPs, 79 probing sensitive paths: p_1ul7sbm (R-B)
- 14,771 verifiable, 5,577 impersonators, 38.3%: p_1waq94n (R-D)
- Reverse DNS does not work for GPTBot: c_p6qo4iu (R-D); impersonating scanners: c_pa5serc (R-D)
- Fetch-to-visit ratio above ten to one: c_pa8lb5v
- Logs as a debugging layer: c_p7s7sz6 (R-D), c_oz6ad0m
- Agent bundle: 2609.34951; 2607.12056; 2605.28787
- Facts endpoint: c_p04wxzg (R-D)
- Product feeds: c_okc8qtb (R-D)
- 114 per minute burst: p_1s04hc7; 429 rate limiting: c_nzydut6 (R-D)
- Do not do / Already outdated: combined from p_1w1m6ve, p_1ryxiap, c_p6txr1i, p_1ul7sbm, p_1w1q92b, cluster 118, cluster 192, cluster 212, c_p766ck6, c_osn4vv5

## 7. Key points
- Combined from all sections above.

## Supplement (2026-10-04 author's tests and official FAQ)

Experimental data: the authors' own experiment runs (raw data not published); handoff: internal notes (not published). Official: OpenAI Publishers and Developers FAQ (help.openai.com/en/articles/12627856, read 2026-10).

- Principle 3.2 crawler table (GPTBot / OAI-SearchBot official documentation), Principle 3.5 "third-party search providers", Principle 3.6 ARIA, What to do noindex / link discovery / ARIA: OpenAI official FAQ
- Case 7 (platform blocking AI crawlers: named in 6/10, 0 citations, appeared 1 time in search results), Case 8 (new website 9/10, 44%): author's tests (swimming, 10 sessions)
- The well-known swimming data platform's robots.txt blocks GPTBot and OAI-SearchBot, checked with curl on 2026-10-04.

## Supplement (2026-10-20 new paper)

- Principle 3.5 web page not opened: B·2610.21731 (Table 1: 53.6%)
