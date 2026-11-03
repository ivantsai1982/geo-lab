# Chapter 11: Source trail (not part of the main text)

Evidence pack: internal evidence pack (not published) (this one only)

## 1. Core principles
- Principle 11.1 Zero-sum competition: 2606.17443 (E, +0.802→+0.007); C-SEO Bench results as relayed by the review 2607.14035 (E); prisoner's dilemma 2406.18382 (C)
- Principle 11.2 Claims vs instructions: 2607.21951 (C, NRG 0.958 vs 0.208); 2604.27202 (E)
- Principle 11.3 Backfire effect of injection and suppression risk: 2606.09204 (E, workshop); model differences in opposite directions in Table 2 and Table 8 of the same paper
- Principle 11.4 Defences: 2603.25500 (B, WWW'26); 2608.16824 (E); 2609.02964 (D); 2609.02316 (E)
- Four white-hat/black-hat criteria: review 2607.14035

## 2. How strong is the evidence
- Zero-sum competition: 2606.17443 (§2.1, §2.3, §2.4, §4); only 3 of 54 combinations significantly positive: 2607.14035 Sec.7.3; prisoner's dilemma: 2406.18382
- Effects of manipulation: 2406.18382 (34.0%→59.4%, external pages at most 25%, 80% do not mention the injected page); 2607.21951 (50.0%, control 0/160, NRG 0.958/0.208/0.146, cross-model transfer, Sonnet first iteration 0)
- Injection in the wild: 2604.27202 (15,387 / 11,722 / 2,042; 87%, 70%; 1,521 / 4,093 / 3,096; 65.8%; 3.9% / 1.1% / 0.2% / 8.0%; 6 cases of following after recognizing)
- Backfire effect of injection: 2606.09204 (54%→8%; 28%→0%; 17%→40%; 36% vs 54%)
- Defences: 2603.25500 (99.78%, 15.7/98.2/85.2%, keyword stuffing ineffective, passage splitting and rewritten queries); 2608.16824 (10,095, 8.90%, 16.36%, 69.34%, AI text detectors fail); 2609.02964 (50.32%→6.20%, BER 94.12%, PPL 15/616 and 252 mislabelled); 2609.02316 (55.7%, 1.7–3.2pp, 98.4% refusals, 55.7→29.2)

## 3. Debates and counterexamples
- Debate 1: 2607.21951, p_1pn5y6c vs 2603.25500, 2604.27202; for injections eliminated at retrieval in a full pipeline, see framework Chapter 0 (2605.28017, not in this pack; used only as background, no numbers written)
- Debate 2: 2606.09204
- Debate 3: c_p2064qv (R-B); c_notwkaq (R-C); c_p5i3wmy (R-D, 400 queries for about 5% error)
- Debate 4: cluster 86 (disputed, 9 in support / 4 against); c_opdxc24 (R-D); c_p066yoe (R-D)

## 4. Cases
- Case 1 (recommendation instruction addressed to "any AI engine"): a real observation specified in this chapter's task brief, with no corresponding item in the evidence pack; worded as a first-hand observation (grade R-D), with no numbers, platforms or company names written. Analysis based on 2607.21951, 2606.09204, 2607.14035
- Case 2: p_1pn5y6c (R-B); follow-up c_nueeb9w (R-D)
- Case 3: p_1oua669 (R-C); rebuttal c_notwkaq (R-C)
- Case 4: p_1rfhbge (R-B); takes effect in about a week c_o7n5aqq (R-D, cost figures not used)
- Case 5: p_1v1dfps (R-D); c_oa6iq3b (R-D); c_p066yoe (R-D)
- Case 6: p_1vnj4zg (R-C); c_p3mxsgx (R-D); c_ojmka24 (R-D); compare 2603.25500
- Not used: p_1upli7n (R-D, body deleted, title only, no verifiable content); c_p7of3nw (R-D, not directly related to this chapter)

## 5. What to do
- Logged-out, repeated-query monitoring: c_p5i3wmy, c_notwkaq
- Recognizing injection text: 2606.09204, Case 1
- Similar ranking lists: p_1oua669
- Anomalies on review platforms: c_oa6iq3b
- Coordinated posting pattern: p_1v1dfps
- Non-rendered channels: 2604.27202
- Reducing data voids: p_1pn5y6c, p_1rfhbge
- Verifiable information: 2606.17443, 2607.14035
- Limited effect of clarifications in comments: p_1v1dfps
- Defences for self-built systems: 2609.02316, 2609.02964; objective criteria in the system prompt: 2606.09204
- Outdated practices: 2603.25500, p_1vnj4zg, c_p3mxsgx, 2606.17443

## 6. Key points
- 1: 2606.17443, 2406.18382
- 2: 2607.21951, 2604.27202
- 3: 2606.09204
- 4: observation specified in the task brief
- 5: 2603.25500
- 6: 2609.02316, 2609.02964, 2608.16824
- 7: p_1pn5y6c, p_1rfhbge
- 8: 2607.14035

## Supplement (new papers, 2026-10-11)

- Third difference in Debate 1 (posting platform): B·2610.11932 (§V-B Table III, Table VI, §V-C, §V-D)
- Qualification of "verifiable facts": E·2602.16136
- White-hat criterion 4: A (with reservations)·2604.04263 (61.2% / 22.4%, 55.5%, 9.5%)

## Supplement (new papers, 2026-11-03)

- Principle 11.4 defence table, "user-side defences" row: B·2610.30365 (Table III, Table V, Table VI, Appendix H)
- New item in "Effects of manipulation" (56 data voids, 504 answers, 31.0% / 42.3%, low visibility 0, pre-launch baseline 0, GEO factors odds ratio 0.91, breaking news odds ratio 3.58, conspiracy premise 0.29): B·2610.30365 (abstract, §III, §IV, Table IV, Table V, Appendix E)
- New defence item one (26.8%–37.5%, equivalence tests, 26.8% / 73.2% without warnings, 53.8% / 5.6%, failure of existing RAG defences is the authors' inference): B·2610.30365 (§IV Takeaway 5, Table III, Table VI, §VI)
- New defence item two (25% → 10%, normal documents 6 → 1, authors' suggestion): E·2610.41012 (Table 1, Table 2, Sections 5–6)
- Three new rows in the evidence summary: B·2610.30365; E·2610.41012
- Debate 1 table "Easy" row, addition after the competitiveness sentence, addition to the third difference (38.4%–78.3%, 14.3%–42.9%, 0; AI crawlers on day 10, stable on day 25): B·2610.30365 (Table IV, §III-D, §V)
- Recognition table: similar ranking lists row adds E·2610.41012; breaking news and newly coined terms row B·2610.30365 (Table V)
- Defence and repair table: evidence strength of the "reduce data voids" row, user-side and "little supporting evidence" flag row B·2610.30365 (§IV-A, §VII); near-paraphrase deduplication row E·2610.41012 (Section 5)
- Key point 7: B·2610.30365; p_1pn5y6c, p_1rfhbge
