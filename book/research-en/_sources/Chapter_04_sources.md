# Chapter 4: Source trail (not part of the main text)

Evidence packs: internal evidence pack (not published)

## 1. Core principles

### 1.1 What retrieval does
- Framework main line (the candidate set can change the answer; entering the candidate set depends on accessibility, language and market, the third-party ecosystem, and relevance): `framework/03_geo-textbook-framework_v1.md`

### 1.2 Principle 4.1 Source sets do not overlap
- Google/AIO/Gemini Jaccard 0.11–0.18: B·2604.27790 (SIGIR 2026)
- Four-engine exact URL Jaccard 0.0079, 84.9% with no shared URL, top-5 all 0 across 60 pairs, single engine 11.4–42.6%, 96.4% in only one engine, turnover 67.0%, 42 times: B·2609.22655 (vendor authors, 15 prompts)
- Domain overlap with Google top 10 4.0/11.1/12.6/15.2%: B·2601.16858
- 37% LLM only, 38% shared, 4.3 vs 10.3 URLs, Bing 23.27% / Google 14.53%: B·2512.09483
- AIO 29.8% not on first page, 25.0% in top 5: B·2605.14021
- Health questions: 44.4% of traditional top 5 pages cited by AIO (short single-turn 46.7%); AIO leans towards commercial health publishers, lower shares for academic medical systems and government sources (|dz| ≤ 0.27); video and Reddit/Quora excluded: B·2610.39339 (weak end: single 3-day snapshot, US English, page level)
- Category overlap 15%/32%/33%, local 0.1–20.6%, cars Jaccard 0.096–0.251: B·2509.08919 (mixed authors, with vendor ties)
- 19% overlap (1,000 prompts): c_ocl52a2 (R-B)
- ChatGPT and Perplexity 11%: p_1vh1n52 (R-B, removed from the main text)
- 48 markets 11.9%: p_1w11zyc (R-B)
- Native search provider of each model: c_p3oeoi8 (R-D)
- ChatGPT index debate: cluster 204

### 1.3 Principle 4.2 Query rewriting
- RBO 0.49 vs 0.74; same-device rerun 0.69 vs 0.86: B·2604.27790
- 98.16% fail to find black-hat sites, minor rewriting attack success rate <10%, rewritten-query coverage 2 times (share), keyword stuffing ineffective: B·2603.25500 (WWW 2026)
- Searches per conversation 1.1/3.3/3.4, 8.2 words, 4.1/16.9/13.3 pages, 10%/23%/28%: p_1vro0sz (R-B)
- 2026 added automatically: p_1u1zqqy (R-C)
- Gemini 3–5 background queries, forum words appended: p_1rw1ff8, p_1rw3i86 (R-B), c_oazdfy1 (R-C)
- Sub-queries with brand names built in: p_1vuhge5 (R-B)
- 68.9% vs 2.1%: p_1vrmfhh (R-D, only the title survives)
- 16% of entities not in retrieved snippets: 2601.16858
- Deep research convergence UGC 16.7–23.4%, 53.7–70.7%, Gemini DR 12.1%, OpenAI DR 0.4%: D·2605.24245
- 8 August sources 11.7→18.9, URLs +69%, domains +9%, 1.38→2.20: p_1vypj0x (R-A)

### 1.4 Principle 4.3 Wording and vocabulary
- Covering rewritten query terms: B·2603.25500
- Shared inbox phrasing flip: p_1urshcf (R-A); off-site footprint / on-page wording interpretation: c_ox5vpyk (R-B)
- Buyer identity 0/40: c_oxuj2o8 (R-A)
- Own vocabulary 99 days: p_1vsr0ge (R-A)
- Niche term 19/25 vs 0/25: c_p4fpfp6 (R-D)
- Category name three quarters to zero: c_p1nlbyx (R-D)
- 42% of businesses flipped: c_p0ov566 (R-D)
- Alternatives phrasing 10 times: c_p76n7oo (R-D)
- Social post wording identical to prompt: c_p4l297a (R-B)

### 1.5 Principle 4.4 Language and market gate
- GPT domain overlap near 0 when changing language, Claude most stable, rewording affects less than language: B·2509.08919
- +0.80 vs +0.15, 35,640 answers, cosine 0.825, 0.844/0.820, sentiment, stability 0.319/0.011, online encyclopedia 11/12: B·2606.23165 (vendor authors)
- Local citations 48.2/33.7/2.3/0.2%, 3.5–13.5 times, Japan 16.6→57.5, South Korea 2.7→36.4: B·2609.06798
- 234 runs, 0/12, 1/24, Turkish 5/6, Russian 4/6, negative control: B·2608.30052 (vendor authors, small sample)
- Finnish GEO ambiguity: p_1vj3aiz (R-B)
- City written into the sentence 0/41→3/3: p_1wcihtt (R-A)
- 19 cities, 97%, 86%/18%/15%: p_1uwddxt (R-B)
- Translating prompts is not enough, local pages cited quickly where local content is thin: c_p9in2ox (R-D)

## 2. How strong is the evidence
- author_type and evidence grade of each study above; top recommendation instability: 2608.30052

## 3. Debates and counterexamples
- 3.1 Visibility of fan-out queries: p_1vro0sz, p_1u1zqqy, c_or8zks0 (R-C), p_1v07cu5 (R-B), c_oyduz7t (R-D)
- 3.2 Index: cluster 204 (contested, 14 for / 4 against); shopping carousel 83%: p_1rltajy (R-B)
- 3.3 Location settings: 2608.30052 vs p_1wcihtt
- 3.4 Prompt length: p_1u2lkrf, c_oqzhbzk, c_or0f8h5, c_pamb2i6 (all R-D); c_okimikn (R-D, not in the main text)
- 3.5 Off-site footprint vs on-page wording: c_ox5vpyk
- 3.6 More queries and UGC: 2605.24245 (13 words, 57–76/34–61/22–37%, detection ineffective); p_1vypj0x; c_p5k6xi1 (R-D, about 11%)

## 4. Cases
- Case 1: p_1urshcf, c_ox5vpyk
- Case 2: p_1vsr0ge
- Case 3: p_1wcihtt
- Case 4: p_1vypj0x
- Case 5: p_1vuhge5
- Case 6: c_pa2gmwo (R-B; the third-party service named in the original is not written in)
- Case 7: p_1vj3aiz
- Case 8: c_o8iewk8 (R-B, relayed client case)

## 5. What to do
- 1: 2609.22655, 2604.27790, 2509.08919
- 2: 2606.23165, 2608.30052, 2609.06798
- 3: 2608.30052, 2604.27790
- 4: 2603.25500, p_1u1zqqy
- 5: c_pa2gmwo, c_om4xa7d (R-D, not written in separately)
- 6: p_1urshcf, c_ox5vpyk
- 7: p_1urshcf, c_oxuj2o8, c_p76n7oo, c_olbruth (R-D, not written in separately)
- 8: p_1vsr0ge
- 9: p_1wcihtt
- 10: p_1vj3aiz
- 11: c_p9in2ox
- Do not do / outdated: 2603.25500 (keyword stuffing), 2608.30052 (single screenshot), c_pa2gmwo (pages for paraphrases), p_1v07cu5 (simulated fan-out queries), p_1wcihtt (location settings), c_p5k6xi1 (cross-engine extrapolation), p_1vro0sz and 2605.14021 (Google ranking), p_1vypj0x and 2605.24245 (more queries)

## Not used (zone F, commercial relationship)
- c_om4x38k, p_1u6f5tr, p_1v6nxs7, p_1sqplmt: not used as evidence or cases. c_p0beg9i (R-D) is the same data as p_1v6nxs7 and was likewise not used.
- Others not used: c_o4kjfly (no claim), p_1tts0wu (R-D, weakly related to retrieval), c_p4a5g64 (R-D, duplicates data already used in the main text)

## Addendum (new papers, 2026-10-03)

- 4.x Query fan-out does not mean more diverse sources (path dependence addendum): E·2609.39026 (Appendix D: round 4, 63.9% of queries different, 75.0% of document sequences different)

## Addendum (author's tests and official FAQ, 2026-10-04)

Experiment data: the authors' own experiment runs (raw data not published); handoff: internal notes (not published). Official: OpenAI Publishers and Developers FAQ (help.openai.com/en/articles/12627856, read 2026-10).

- 1.3 "The author's own test": 94% (swimming 112/119), 95% (270/284), five types of new words, three category patterns, first search term site: (7/30, 6/10), AUC difference +0.075 (CI +0.022 to +0.127; shopping significant), vector AUC 0.74 / 0.67, shopping keyword 0.71; 9.5 (284/30) to 11.9 (119/10) sets of search terms per session
- Debate 3.2 third-party search providers: OpenAI official FAQ

## Addendum (new papers, 2026-10-11)

- 3.3 Language over location: B·2603.23474 (Table A29: English across countries Jaccard 0.58–0.80, local language 0.11–0.17)
- 3.4 Short prompts and multi-turn conditions: A (descriptive logs)·2607.22392

## Addendum (new papers, 2026-10-20)

- Mode differences in number of searches: B·2610.15382 (Table 3)
- Retrieval dominance: B·2610.15033 (§6.4: 32% vs 2.8%; 97% not in Google top 50)
- Principle 4.4 / Debate 3.3 location channels: B·2610.24081 (same city 32%, different city 8%)
