# Chapter 9: Source trail (not part of the main text)

Evidence pack: internal evidence pack (not published)
Paper grades follow Framework v1; forum item grades follow the labels in the evidence pack. Section F (leads with commercial ties, pending checks) was not used at all.

## 1. Core principles

### Principle 9.1: Each question asked is only one sample
- Adjacent-day source Jaccard 0.336–0.423, 10 same-day repetitions 0.321–0.434, ChatGPT zero citations in 57.8% of runs: paper 2604.07585 (B)
- Median Jaccard of cited domains 0.29–0.31 / 0.33–0.40 / 0.50; 95% CI 3–7 pp wide: paper 2603.08924 (B, vendor)
- Query rewriting differs each time (description of mechanism): c_p9bfzus (R-A)
- 197 sites, three engines, 3 runs per question, 32% of citations appeared only once: c_p4l9w6p (R-A)
- Top-recommended brand differed 48.5% between two runs within 24 hours: c_p5y5vd9 (R-A)
- 45 local queries run twice, about one-third of businesses swapped; another engine 85% unchanged: c_owip8i4 (R-A), c_owip5ah (R-B)
- Interval of 12%–74% for 4/10: p_1t54uc3 (R-B); checked by the author with the Clopper-Pearson exact interval (about 12.2%–73.8%)

### Principle 9.2: Breadth > depth
- Language 26.5%, brand 1.5%; after the 5th run, adding 5 runs vs adding 3 languages about 15 times; single-answer reliability about 0.01: paper 2607.13304 (B, vendor, sentiment outcomes, CI not computed)
- Brand Jaccard 0.453–0.589, higher than sources: paper 2604.07585 (B)
- Sequential convergence n*=33–75; 3 combinations did not converge; fixed ρ≥0.95 held in only 19/30; agreement as low as 0.364, 0.717 with SNR added; differences in citations per answer: paper 2607.10341 (B, vendor)
- Queries needed to narrow the CI to 5 pp 30–50 / 90–100 / ≥150: paper 2603.08924 (B)
- Re-running and rephrasing serve different purposes: c_omyltsh (R-B opinion), c_owomcek (R-D)

### Principle 9.3: Observation layers
- Interface and API domain overlap 12.0% / 14.8%; two engines share 5.4%, 76.7% with no common domain: paper 2609.18729 (B)
- App/Web domain Jaccard 0.19–0.51; one platform 0.014 at URL level: paper 2607.15771 (B, vendor, Chinese-language engines)
- Some APIs do not return X sources: paper 2601.01750 (B)
- 46% (282/615) without sources vs 0/359: c_p8zw5hc (R-A)
- 10 days, 2,209 answers, 59% showed sources: p_1wf7zgp (R-A)
- AI Overviews triggered about 7/10: c_p8j7mnw (R-B)
- Location prompt turned brand from absent to named in 5/6: c_p8hps6a (R-A); same account c_p8hp2af (R-D)
- Sources overlap 22% across two languages: p_1uf6f2l (R-A)
- Interface about 50% vs API 0/30: c_p9bfzus (R-A), c_pa60zva (R-A)

### Principle 9.4: Scores are defined by prompts and counting rules
- Weights make activation rate 39.66% vs 70.54%, ranking can reverse: paper 2609.06811 (E)
- Question type 41% / 20% / 40% naming no one: c_p49lliv (R-B; single engine, single run)
- One extra word replaces the whole set of sources; same day present at 03:00, absent at 18:00: c_oyhqdtr (R-B), c_oyj1sx1 (R-B)
- Brand name in the question almost always appears: c_p8hps6a (R-A)
- Rotating prompt set creates fake declines; LLM scoring drifts 10–15 points: c_p8j8t8h (R-B)
- Aliases make 77→94: c_pa5v8gt (R-D)
- Echo removal 10.9%→8.9%, X vs Y 15.8%→8.1%: c_p97a18o, c_p9innwu (R-D)
- 13 / 23 of 60 questions named no brand: c_p9qbeh1 (R-D); same direction p_1wf7zgp (R-A)
- Testing only core terms gave 0/10: c_paj49pj (R-D)

### Principle 9.5: Mention / citation / recommendation
- 8.3% of brands in the citation pool entered the answer; 66% of listed sources entered the body: paper 2607.15771 (B)
- 44% mentioned vs 10% recommended: c_oxazh5x (R-B)
- About 26,400 answers, 16% appeared, 13% cited, 3% named only, median 13%: p_1uy3rsv (R-B)
- Zero recommendations over 99 days: c_p6yjdrf (R-D)
- Consensus "citation does not mean recommendation or mention": Cluster 58 (71/0, highest support); Cluster 65
- Crawling / indexing / outcome three-way split: c_pa3b16q (R-B); chain: c_p7csywz (R-D); zero crawling = leading indicator: c_oscfa6e (R-B)
- No referrer goes into direct traffic, two-bucket attribution: c_p7k7iw5 (R-A); c_opopl9w (R-B)

## 2. How strong is the evidence
- Each row corresponds to the papers above; the "vendor" author type is taken from the Section B notes of the evidence pack
- No research shows a link between visibility and traffic/revenue: Framework v1, main thread, sentence 4
- Practitioner data come mostly from tool developers: self-disclosures in c_p7k7iw5, c_p8zw5hc, c_p8j8t8h, c_ov0fnba, etc.

## 3. Debates and counterexamples
- Debate 1: 2604.07585, 2607.10341, 2607.13304; c_p4l9w6p (R-A), c_olkqryg (R-B), p_1t54wef (R-B), c_okf2knn (R-B); Cluster 75, Cluster 49
- Debate 2: c_p47vwwq (R-B, own account inflated), c_p52dqed (R-B, 20 clean accounts); 2609.18729; c_p9bfzus (R-A); c_oyhqdtr (R-B, fix one observation surface); c_oy40n7a (R-B)
- Debate 3: c_p900tjl (R-B, 90/67/52/34), c_on4tfk7 (R-A, 65/55/35), c_p4l9w6p (R-A, 43%), c_p2t56lb (R-C, ChatGPT most stable), 2603.08924 (B); Cluster 103
- Debate 4: 2604.07585; c_pcsavm8 (R-B, 28/30, 26/30); c_olkqryg (R-B, description less stable, 40–80%, positions 4–10)
- Debate 5: Cluster 135 (28/3), Cluster 111 (disputed), c_okj78ql (R-B, ten people incognito); c_p3t2q98 (R-A, SD 2.8); c_on8z8b2 (R-B)
- Debate 6: p_1wfbo4v, p_1wfbsda (R-D, 8 times); Cluster 14; c_p8yh3uc (R-B, three tools same ordering, URL overlap 55/64/14%)
- Debate 7: c_ow2tdz7 (R-D) vs c_owip8i4 (R-A)

## 4. Cases
- Case 1: c_p9rxbmq (R-A, 851→790, 225→73, 11/40); c_pbeckcq (R-B, 55% other, 80 rows wrong-question); c_pa6edv0 (R-B, -37 cannot be attributed)
- Case 2: c_p7k7iw5 (R-A, 9→0/64, one-quarter control); c_p0shdwu (R-D, 0.226→0.285)
- Case 3: c_pa3b16q (R-B); c_oscfa6e (R-B)
- Case 4: p_1r9wejb (R-B)
- Case 5: c_p3t2q98 (R-A)
- Case 6: c_ov0fnba (R-A, 1/8→5/8, 10 days); p_1vh3q0w (R-B, 26 cases)
- Case 7: p_1vkjfki (R-B); c_p7jfa9u (R-B, 116,061 impressions/53 days); Cluster 227, Cluster 224; c_p45yz0o (R-D, probe contamination); p_1tj7u6g (R-B, 865 citations/7 days)

## 5. What to do
- 5.1 #1 Baseline: Cluster 2 (14/0), c_oflf8qe (R-B), c_p8hps6a (R-A), c_owq21nr (R-D, cross-day baseline)
- #2 Prompt sources: c_pa2hom0 (R-B), c_oe1mwti (R-B), c_oyj1sx1 (R-B), Cluster 15
- #3 Freezing and versioning: c_p8j8t8h (R-B), c_oyhqdtr (R-B), c_p4nkl9u (R-B)
- #4 Screening and grouping questions: c_p9qbeh1 (R-D), p_1wf7zgp (R-A), c_p49lliv (R-B)
- #5 Repetition: 2604.07585; c_p4l9w6p (R-A)
- #6 Breadth: 2607.13304
- #7 Separate reporting: 2609.18729; p_1u11m66 (R-A); c_p3t2q98 (R-A)
- #8 Observation surface: 2609.18729, 2607.15771; c_oyhqdtr (R-B); c_p0zqs2k (R-D, web search on/off 0.402 vs 0.256); c_p5wfn23 (R-D)
- #9 Recorded fields and failures: c_p8zw5hc (R-A), c_p9rxbmq (R-A), c_pbeckcq (R-B), c_p8j7xxd (R-D)
- #10 Hit definition: c_pa5v8gt, c_p97a18o (R-D)
- #11 Control group: c_p7k7iw5 (R-A); c_p0shdwu (R-D); c_p1h6jsz (R-D)
- #12 Trend window: 2604.07585; c_opou11e (R-B, 4 weeks or more); p_1qx8tu2 (R-B, 15% rule of thumb); c_oxodby3 (R-B)
- #13 Three questions: c_opou11e (R-B)
- #14 Recording cited URLs, correlation not attribution: c_p6wquwi (R-B), c_p47vwwq (R-B), c_p7k7iw5 (R-A)
- #15 Logs, webmaster tools, two buckets of traffic: c_pa3b16q (R-B), c_oscfa6e (R-B), c_p7k7iw5 (R-A), Cluster 120
- Cost: c_oyhqdtr (R-B), c_oscfa6e (R-B), c_oxpmg2o (R-B), c_p7j9o3r (R-B)
- Minimum viable version: c_p9w8jv9 (R-B); c_p9w8zco (R-D, 3 times per question)
- 5.2 General principle and falsifiability: c_p7k7iw5 (R-A)
- Evaluation table: c_p4l9w6p, 2609.18729, c_oe1mwti, c_p7k7iw5, p_1wf7zgp, c_p9rxbmq, c_p8j8t8h, c_pa3b16q (open-source tracker code), p_1rl529g (prompt search volume), c_p0zqs2k (R-D question list), c_o5vnc8o (R-D API vs UI)
- Vendors: Cluster 88, Cluster 228, Cluster 124, Cluster 91 (disputed)
- Warning signs: p_1vfgzvk (R-D, 1 mention→1%, 15 prompts 14 days); p_1t54uc3 (R-B, 60/35/50%, economic reasons for single runs); p_1wfbo4v (R-D)
- 5.3 Do not do: c_p47vwwq, c_p52dqed, c_p8hps6a, c_p8j8t8h, c_p9rxbmq, 2607.10341 (differences in citations per answer), c_p6wquwi
- 5.4 Outdated: c_otbfntu (R-B), p_1ushz6a (R-B), c_oy1jz5k (R-D), c_oeei7ho (R-B, 47 days at 84 points), c_opopl9w (R-B), c_p7k7iw5 (R-A)

## Not used (Section F, commercial ties)
p_1wfdk6f, c_omx0mnj, c_p5r4kg0, c_p7k54g3, c_p83uh8h, p_1p8n67i, c_ok50ytm, c_p9w9rlg, p_1uxhq4n, p_1u3qa3c, p_1udfe1h, p_1vuhqf2, p_1rvvicx, p_1w3r50o, c_pacicqi, p_1v9kq94, c_p0adsgb, c_p9rxz04, p_1vy1esp, p_1r1ratd, c_p32zo5w, c_owxx3ie, c_ou2zfqf, c_ofuih1z

## Supplement (new papers, 2026-10-03)

- Principle 9.4 unit of evaluation (conversation capture) and new row in the evidence table: E·2609.40069 (§2, §5.3, §6, §10; numbers determined by parameters the authors chose, not cited in the main text)

## Supplement (new papers, 2026-10-11)

- 9.4 Baseline: B (LLM part weak)·2603.23474 (ChatGPT +13.3 / +2.3 / +17.3)
- 9.4 Real multi-turn logs and new row in the evidence table: A (descriptive)·2607.22392 (Table 3: 50.3% / 44.8%, 26.1% / 26.2%; §6.4: 72.2% / 71.0%)
- Model scoring measures the wrong thing: E·2609.18282 (Table 2: Top-1 0.082–0.164, random 0.25)

## Supplement (new papers, 2026-10-20)

- API vs web version, reasoning mode: B·2610.15382 (Table 4, §5.2)

## Supplement (new papers, 2026-11-03)

- Principle 9.1 deep research mode (10 repetitions; entity median Jaccard about 0.12; cited URLs about 0.01; entity-citation pairs 0.0073; each report about 5,000 words, about 79 URLs), Principle 9.2 addition on brands being more stable than URLs, 9.2 long tail not saturated (Figure 3; "size of the candidate space" is the authors' hypothesis, the implication for brands is the book's inference), new row in the 9.3 observation-layer table, new row in the Debate 1 table, supporting side of Debate 4, new row in the evidence table, 5.1 #8: B (weak)·2610.26421 (Sections 3 and 4, Figures 2 and 3)
- Principle 9.4 refetch checking (drift 21.9% vs 5.8%, about 3.8 times; dead 11.8% vs 16.0%), Principle 9.5 a 200 in logs is not the main content (about one fifth of static 200s lack main content), Case 3 note, new row in the evidence table, 5.1 #15, 5.3 Do not do, Key point 6: D·2611.00884 (Tables 1 and 6, Sections 5 and 7)
