# Chapter 07 Citation and Absorption: Source trail

> Evidence pack: internal evidence pack (not published) (this one only). The identifiers below do not appear in the main text.

## 2. Core principles

### 2.1 Four layers
- Framework structure: framework v1, Chapter 7 "Implications for practice" (layers: mention, citation, absorption, correct description)

### 2.2 Breadth of citation and depth of absorption
- Platform citation counts 6.88/12.06/16.35 and absorption 0.271/0.058/0.065: 2604.25707 (E, secondary analysis of a static snapshot)
- Chinese-language platforms 66%/30%/8%, silent citations 39.3%, brand inclusion 8.3%: 2607.15771 (B, author type: vendor)
- AIO forum sources underused −22.1pp, encyclopedias overused: 2603.16138 (B, single snapshot)

### 2.3 Invisible use
- 14–53% of claims uncredited, more than 15–20% of claims cannot be grounded: 2609.19244 (B)

### 2.4 Fidelity
- AIO 11.0% of statements unsupported (Omitted 7.0 / Incorrect 2.7 / Ambiguous 1.4), source quality vs faithfulness r≈0.045, AIO source credibility higher than first page: 2605.14021 (B)
- FFR 30.6%, SFR 27.1%, 761,495 citation pairs, 10 models, the two axes trade off, provider explains 96%/88%, scaling models difference <0.8pp, reasoning model 34.1%→18.0%, SFR change <2pp, answer level 71.3–96.1%: 2605.28565 (B)
- Hallucinated URLs 3.0–13.3%, deep research agents 10.7% vs 4.8%, 4.3 times more citations with 2 times higher unresolvable rate: 2604.03173 (D)
- 12/14 models link validity >94%, relevance >80%, Fact Check 24–77%, 78.6%→16.7%: 2605.06635 (D, author type: industry)
- Hedging reduced 40%/60% after search: 2603.16138 (B)
- Long health questions: AIO cited statements grounded 47.1% (HallOumi), 56.7% after correction (95% CI 45.3–68.6), uncited factual statements 20.8%; AIO-cited pages lower than traditional top 5 on 4 of 6 quality indicators (|dz| ≤ 0.19), lean towards commercial health publishers; grounding vs clinical score ρ = .01, source quality ρ = −.05 / .10: 2610.39339 (B, weak end: single 3-day snapshot, US English, questions adapted from HealthBench)

### 2.5 Citations as a persuasion signal
- 4,927 people, 9 queries, trust +0.091, sharing +0.121, valid/invalid difference -0.021 not significant, uncertainty highlighting -0.157: 2504.06435 (E)
- 24,069 conversations, 12,652 votes, supporting β=0.29, unrelated β=0.27, contradicting not significant, about 800 conversations: 2506.05334 (B, ICLR 2026)
- Answer side: uncited vs cited AIO clinical scores 40.4% vs 39.2% (p = .649), grounding vs accuracy ρ = .01, physician rubrics 38.2%, pre-specified harmful claims 22.2%, high-risk questions uncited 17.6%; authors cannot separate parametric knowledge from citations attached after the fact: 2610.39339 (B, weak end)

### 2.6 Generalization of testimony
- 30,000 answers, score OR 2.88, top-level OR 1.97, formal OR 1.488, experiential OR 0.789, moderator-pinned almost never selected, first person 3.3%→0.06%: 2609.14575 (B; the object of study is Reddit Answers, described in the main text as "the built-in generative Q&A feature of a community platform")

### 2.7 Being cited and being named
- Research data: 2607.15771 (8.3%, multi-source co-occurrence more important than 5118-Baidu quality score)
- Practitioner observations: c_p9q3qgh, c_p139rq7, p_1v7kppa, p_1uy6iwb (all R-D)

## 3. How strong is the evidence
- Each row corresponds to the papers listed above; vendor authors: 2607.15771; single snapshot: 2603.16138; note on measurement artefact (max-over-chunks): 2603.16138 limitations
- Unrelated-citation sample about 800 conversations: 2506.05334 §3.2

## 4. Debates and counterexamples
- 4.1 A citation signals trust: consensus cluster 31 (support 8 / oppose 0); compare 2607.15771, 2609.19244, 2506.05334
- 4.2 FAQ format: 2604.25707 (Q&A 0.0947 vs 0.1005; with code/numbers/definitions/comparisons 41–77% higher)
- 4.3 More searching: 2605.06635 (78.6%→16.7%; 80.0%→57.9%); 2609.19244 (Claude mixed effects)
- 4.4 Source quality and faithfulness: 2605.14021; 2605.28565; opposite direction in health (AIO-cited pages slightly lower quality, lean towards commercial health publishers) and agreement (quality and grounding do not predict accuracy): 2610.39339 (B, weak end)
- 4.5 Deep research agents: 2604.03173 (10.7% vs 4.8%; openai-deepresearch 3.5%)

## 5. Cases
- Case 1 regular checks of brand description: c_p0uc82c (R-B)
- Case 2 15 positive, 1 negative review: p_1vko1uf (R-B); consensus cluster 126 (support 16 / oppose 1)
- Case 3 85 B2B companies cited but not named: p_1v7kppa, c_p0bf0p5, c_p0beyd8, c_p0beziz, c_p0xxfgh, c_p0bf1km (all R-D, same author's dataset)
- Case 4 news site 700 citations, 5 namings: p_1wesnrr, c_p9q3qgh (R-D)
- Case 5 cycling tour operator: p_1uy6iwb (R-D)
- Case 6 AIO uses image without attribution: p_1s43bvb (R-C)
- Case 7 schema price not updated: p_1ugnymf (R-D); consensus cluster 4 (disputed, support 5 / oppose 0)
- Case 8 confusion between same-name entities: c_ovko1sx (R-C); consensus cluster 57 (support 7 / oppose 0)
- Other leads: p_1td0xjo (old blog number), c_p0vqdmr (contacting sources about 70% success), c_oe4asts (about 30 companies described incorrectly), p_1u3xu06 (23% of facts deployed, data not public), c_p8wyu74 (R-C, screenshot of verbatim quote block)

## 6. What to do
- 6.1 Layered measurement: framework v1, Chapter 7 implications; 2607.15771; 2609.19244; 2604.03173; p_1v7kppa
- 6.2 Monitoring and correction: c_p0uc82c; p_1vko1uf; c_p0vqdmr; 2605.14021; consensus cluster 126
- 6.3 Increasing correct absorption and naming: 2604.25707; p_1uy6iwb; c_p9q3qgh; c_ovko1sx; consensus cluster 57; 2607.15771 (multi-source co-occurrence); 2603.16138 (hedging)
- 6.4 Do not do: p_1v7kppa, c_p139rq7; 2604.03173; 2506.05334; 2605.14021; 2605.28565; p_1u3xu06
- 6.5 Outdated: 2607.15771, 2603.16138, 2604.25707, p_1ugnymf + consensus cluster 4, 2605.06635

## Content not used
- Section F (with commercial relationships), none used: p_1sghzxj, c_p5sn3g0, p_1u7s61q, p_1t9xa8c, p_1w37gg9, p_1rq1oby
- c_ob61v6y: the third-party tool vendor numbers it cites are secondhand; not used
- c_p4a5i5f: the author states they sell in this field; their numbers not used
- c_oom70j0, c_owca9k0, c_p8c5arn, p_1tkvrch, consensus clusters 182, 189: weakly related to this chapter's topic or only the title remains; not used
- 2607.15771's freshness half-life and App/Web overlap data: belong to other chapters' topics; not used

## Supplement (2026-10-03 new papers)

- 2.1 "Correct citations ≠ representative evidence": E·2609.39026 (§1)
- 4.3 The more read, the better the representativeness: E·2609.39026 (Table 10: MAE 0.8424→0.4108)

## Supplement (2026-10-04 author's tests and official FAQ)

Experimental data: the authors' own experiment runs (raw data not published); handoff: internal notes (not published). Official: OpenAI Publishers and Developers FAQ (help.openai.com/en/articles/12627856, read 2026-10).

- Case 9 "Cited does not necessarily mean opened": open_page actions 16 for the three question types, 37 for swimming (recalculated from raw/); new site opened in 10 of 25 citations (main data page 9/7, other level pages 10/3, research articles 5/0): author's tests

## Supplement (2026-10-20 new papers)

- Supporting research for Case 9: B/D·2610.21731 (Table 1, Table 2)
