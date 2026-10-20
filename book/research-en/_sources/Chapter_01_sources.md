# Chapter 1: Source trail

> Main text: `Chapter_01.md`. This file lists the basis for the conclusions in each subsection of the main text. The IDs below do not appear in the main text.
> Grades: papers A–E; forums R-A / R-B / R-C / R-D; consensus clusters are written as "cluster N".

## Questions this chapter answers
- Based on Chapter 1 of the framework `framework/03_geo-textbook-framework_v1.md` (Principles 1.1–1.4) and the book-wide backbone.

## 1. Core principles

### 1.1 Two sources of knowledge
- In web-connected agent mode, training knowledge makes up 7–10% of the answer: 2609.34951 (B, author type: vendor) §5.3
- Ranking shift of 2.30 places for popular entities vs 4.15 places for obscure entities; popular entities rely on priors, obscure ones on retrieval: 2601.16858 (B/E; the perturbation experiment uses a single model and fixed context)

### 1.2 The map of the book
- Seven pipeline stages, "random, multi-stage filtering pipeline": book-wide backbone of framework v1
- Chapter for each stage: chapter list of framework v1 (Chapters 0–15)
- Practical support for "random" (results drift across repeated runs): p_1qx8cp4 (R-A); cluster 49, cluster 112 (consensus)

### 1.3 Each stage values different things
- Retrieval/reranking/generation preference table; body-only changes -9% / -16% / -6%; structural fields +22%, reranking -17%; AutoGEO retrieval -36%, greatest losses when technical/rare words are rewritten; 5.8% of target documents dropped from 10th to 11th and were excluded; all strategies lowered citations in the Shopping domain: 2602.12187 SAGEO Arena (D, KDD 2026) Table 2, §5.1, Figure 4

### 1.4 The total effect is the combination of the effects at each stage
- Total effect is a composition of stages, downstream rewriting harms upstream retrieval: 2607.14035 (review, E) Sec.7.4; 2605.28017 (D)
- Retrieval survival 79.9%, IOA 59.3%, IOA end-to-end about 14.7%, gradient-based <2%, CORE-Reason/Review about 40–54% (the main text says "about 40–54%", based on one_line and the 53.5% / 46.7% / 40.2% in Table 4); reranker prefers later positions, generator prefers earlier positions: 2605.28017 (D) §5.2, Table 4, Fig 3
- "40%" is a relative gain in word share with five fixed documents (19.3→27.2): 2607.14035 Sec.4.1; framework v1, Chapter 0

### 1.5 Agents search in multiple rounds and open web pages to read them
- Source of the principle: framework v1, Principle 1.4
- Practical lead on the query fan-out phenomenon: c_p3bn8xj (R-D, used only as a lead; its figures are not in the main text)
- 1,056 businesses, 37,927 journeys; own pages 78% vs 58%; recommended 20% vs 11%; failure mode is omission rather than fabrication; bundled score not separated; own scorer: 2609.34951 (B, vendor) Fig7/Table7, Table 6

### 1.6 GEO and SEO
- SEO as the foundation and the way into the candidate set: c_p1s7y8p (R-D), c_p4ujmj0 (R-D) as background views; c_ozbduiw (R-B) "content-layer extension"
- Domain Jaccard: GPT-4o 4.0%, Gemini 11.1%, Claude 12.6%, Perplexity 15.2%; earned share Claude 65%, GPT-4o 57%, Google 41% earned / 34% social; median page age for car queries 148.0 vs 492.9 days: 2601.16858 (B, Section 2)
- AI Overviews two-month page overlap 18% vs organic 45%; URL Jaccard 0.11–0.18: 2607.14035 Sec.6.2, 8.1
- No research shows a stable, longitudinal, cross-platform causal effect on organic discoverability or conversion: 2607.14035 Abstract, Sec.10; framework v1, 4th sentence of the book-wide backbone

## 2. How strong is the evidence
- Summary of the above: 2609.34951 (B), 2601.16858 (B/E), 2602.12187 (D), 2605.28017 (D), 2607.14035 (review)

## 3. Debates and counterexamples

### Debate 1: does SEO automatically equal GEO
- View A:
  - About 70% overlap: c_p1s7y8p (R-D); 85% / 95% task overlap: c_p4ujmj0 (R-D)
  - Into AI answers through SEO alone, with no schema / llms.txt: c_ot1d32v (R-D), c_oozv6d1 (R-D)
  - Three or four months of SEO work, AI Overviews mentions 20–30 → more than 700, higher ranking means more likely to be cited: c_p0slw1m (R-D)
  - Title and first ~200 words changed, three months of GSC, ranking moved first, citation followed: p_1wgtvov (R-B)
- View B:
  - ~1,200 queries, 38–45% in the top three, ~30% from 6–20, ~20% from unranked sources: c_o99vs7k (R-B)
  - ~350,000 articles, 10,382 keywords, 52 categories, ~14% in the top 20: p_1tkvz8c (R-B)
  - 4 sites, 80 queries, top three 31%, beyond 10th place 12%: p_1uozkav (R-B)
  - ~40 prompts, ~500 citations, several weeks, Google ranking not a good proxy, source preferences differ by platform: p_1w45n7l (R-A). The figures from the large third-party dataset it cites (38%, 76%) are second-hand and come from a vendor; neither the figures nor the name appear in the main text
- Balanced "content-layer extension" statement: c_ozbduiw (R-B)
- One platform's AI draws on another search engine's index: c_opj2yuj (R-D); related claim c_okgkige (R-D)

### Debate 2: memory or search
- Practitioner view (most answers rely on training data): c_odj2j8h (R-B), c_odhd639 (R-D)
- Research: 2609.34951 (B) §5.3; 2601.16858 (B/E)
- Cited ten minutes after publication, due to real-time retrieval: c_o9q26qs (R-D)
- Triggering as the first gate: framework v1, Chapter 2

### Debate 3: off-site mentions vs own-site readability
- Consensus: cluster 29 (consistently repeated information), cluster 114 (consistent mentions on external platforms matter more than own-site ranking)
- Research: 2609.34951 (B) Table 6 (after controlling for AX, AEO proxy metrics have no significant partial correlation; limited to the drill-down scenario)
- Extended in Chapter 5: framework v1, Chapter 5

## 4. Cases
- Case 1 (audit of about 17,000 French SME websites): c_ozbduiw (R-B)
- Case 2 (Singapore chicken rice, AI Mode, 11 queries × 3 runs): p_1qx8cp4 (R-A)
- Case 3 (500+ local service businesses, 72%, ChatGPT / Siri): c_oz9ytqj (R-B)
- Case 4 (Google rank 30–40 but high impressions in the Bing AI section; after a community platform blocked crawlers in mid-August, its ChatGPT share plunged while AI Overviews and rankings barely changed): c_p755a31 (R-B)
- Case 5 (Gemini, client ranked 1–3, competitors ranked 6–20 were cited, readability changes had no effect): p_1wece9q (R-B)
- Case 6 (financial content ranked 3–5, cited about 20% of the time): c_oeccwaw (R-B)

## 5. What to do
- Triggering and separate planning for popular/obscure entities: 2609.34951, 2601.16858
- Accessibility: 2609.34951; c_p755a31 (R-B)
- Core entities and figures in structural fields: 2602.12187 works
- Answer first, consistent topic: 2602.12187 works; c_ozbduiw (R-B)
- Verifiable evidence in the body text (figures, prices, dates): 2602.12187; 2607.14035 works
- Consistent entity information: c_ozbduiw (R-B), c_oz9ytqj (R-B); cluster 57, cluster 123
- Stage-by-stage checks: 2602.12187, 2605.28017, 2607.14035
- Fixed prompt set, repeated runs, long-term tracking, rankings and citations recorded separately: cluster 2, cluster 15, cluster 49, cluster 52, cluster 75, cluster 76; c_p755a31 (R-B)
- Measuring by platform: 2601.16858 (B); p_1w45n7l (R-A)
- Do not optimise only the body text / do not expand heavily or rewrite technical terms: 2602.12187 fails
- Do not use ranking as a proxy: p_1uozkav, c_o99vs7k, p_1tkvz8c, p_1w45n7l; 2601.16858
- Cited ≠ recommended / business: cluster 58, cluster 65, cluster 122; 2607.14035 Sec.10
- Outdated "40%": 2607.14035 Sec.4.1; framework v1, Chapter 0, 3rd sentence of the book-wide backbone

## Key points
- Summarised from the sections above.

## Unused material
- Evidence pack section F (leads to check, with commercial relationships): p_1u1y9z2, p_1vwm9qt, c_ozc4bgp, c_p739sp7, c_o9y1yhy, p_1win2zi, c_o6bisw8, c_p74o480, p_1ukwmzl: none used as evidence or cases.
- Other R-D entries (such as c_o4fewj4, c_okmwfdq, c_o28d1pl, c_o5yfo6p) have unverified figures or are only weakly related to this chapter's backbone, and were not used.
