# Chapter 08: Source trail (not part of the main text)

Main text: `Chapter_08.md`
Evidence packs: internal evidence pack (not published)

## 8.1 Core principles

### Principle 1: Techniques have a shelf life
- Retest of the three techniques (-0.33/-0.28/-0.79 vs 2023 +42.6/+32.8/+27.7; ten modern models): 2609.07559 [C, authors are a vendor]
- 2023 experimental setup (5 candidates, word-count share): framework Chapter 0, survey 2607.14035
- Crowding / zero-sum: 2506.11097 [E] §6.4; at high adoption a single strategy falls below the unoptimized baseline: 2608.27631 [E] Fig.2
- Rewrites fall behind at retrieval / reranking in the pipeline: 2602.12187 [D]

### Principle 2: Direction automated optimization converges on
- Converges on faithful to the facts, aligned with intent, structured: 2511.20867 [E]; 2510.11438 [D]
- Defensive clause lowers manipulation-flag rate by 60 percentage points: 2511.20867 §6.2
- Preference rules overlap 79–84% across LLMs, 35–40% across domains: 2510.11438
- Query-independent content score vs citation Spearman 0.114; cross-encoder 0.388, full model 0.348: 2609.07559 §8–9
- Consistent with Principle 6.1: framework Principle 8.2

### Principle 3: Stage at which each element acts
- Freshness OR 14.4 to >10k: 2605.25517 [E]; Chinese-language engines median 18 days / half-life 39 days, 101 days / 68 days: 2607.15771 [B, vendor]
- Definitions / numbers / comparisons 41–77% higher; Q&A -5.74%: 2604.25707 [E]
- Structural fields help retrieval: 2602.12187 [D]; layout OR 0.79–1.68: 2605.25517; structured presentation +0.50 citations, total citations do not rise, primary endpoint CI crosses zero: 2609.15164 [D]; r=0.63: 2509.10762 [B, correlational]
- Q&A no clear advantage, short paragraphs strongest: 2603.25500 [B]
- Authoritative tone lowers credibility: 2509.05607 [E]
- Keyword stuffing ineffective: 2603.25500, 2510.11438, 2604.19113, 2609.07559

### Principle 4: Side effects
- Negative-gain rate on non-target queries 30.6%: 2601.13938 [E] Table 4
- Faithfulness 8.29→4.90, attribution accuracy 6.15→4.18: 2608.27631 [E] Table 3
- Body text only: retrieval -9%, reranking -16%, citation -6%; AutoGEO retrieval -36%; obscure terms lose the most: 2602.12187 Table 2

## 8.2 How strong is the evidence
- Ten-model retest, gpt-5.x replication, appended-block implementation, vendor interest: 2609.07559
- Only 3 of 54 combinations effective; statistics lowered rank in 19/24; first position in context +2.77, far larger than rewriting: 2506.11097 [E, NeurIPS'25]
- In e-commerce most hand-written techniques do worse than a simple prompt, storytelling -4.36; 63 of 75 cells improved; gain unrelated to length: 2511.20867
  - Note: the framework says "13 of 15 do worse than a simple prompt", the notes say "only 4 slightly better"; the two disagree, so the main text was rewritten as "most do worse"
- 9 word-level techniques below baseline: 2604.19113 [E]
- AutoGEO 20.18→43.76; Claude precision 96.51→84.98: 2510.11438 [D]
- 171,000-page corpus: 2602.12187; 1,702 citations: 2509.10762; 450 self-built websites, 65.22% is a share: 2603.25500; 252,000 trials: 2605.25517; about 160,000 citations: 2607.15771
- 15% flips, 45% of variance from decoding: 2609.15164
- Noise floor 98% / 3–4pp: c_p0lu7u5 [R-A]

## 8.3 Debates and counterexamples
- Debate 1 (statistics / evidence): 2609.07559, 2506.11097, 2509.05607 (Trust 8.352→7.613) vs 2604.19113 (+37/+73/+96%, in ablation statistics and cite sources contribute most), 2601.13938 (evidence type strongest; Statistics +3.49 see contradicts column); practitioners: c_oz6botw [R-B], p_1w5qqlq [R-D]
- Debate 2 (Schema): 2602.12187, 2509.10762 vs c_owript2 [R-B, 318-page RCT], c_o3aqism [R-B, 349.99 vs 199.99]; c_o8aifbp [R-B, about 2×]; c_oru48yh [R-D, zero schema, 55,000 citations]; c_o3b4mfd [R-D, multi-variant prices]; p_1v1eve0 [R-D, readable is not the same as chosen]; consensus clusters 89, 147, 150, 137
- Debate 3 (FAQ): 2604.25707, 2603.25500 vs c_oeeqzcr [R-B], p_1td86ak [R-B], c_oeqjlr4 [R-B]; counterexample p_1w79x6u [R-B]; consensus cluster 34
- Debate 4 (authoritative tone): 2509.05607, 2511.20867 vs 2605.25517 (confident statements backed by evidence help, vagueness and self-contradiction hurt); p_1sqtbsw [R-B]; c_o0wrrkb [R-A]; c_o0wxldp [R-D]
- Debate 5 (freshness): 2605.25517, 2607.15771, c_okorz1k [R-B] vs p_1wowxci [R-B], p_1wc7ius [R-B], p_1vzc8ze [R-D, 203 days]; counterexample p_1sxlfgw [R-D]; see also c_o0wsfas [R-D], c_nz585rn [R-C], c_nz585rn/c_nx8s1gb (not used in the main text)
- Debate 6 (summary / length / number of pages): 2506.11097 (LLM Guidance summary placed first), 2602.12187 (answer first, heavy expansion -36%), p_1ofa5qx [R-B, Key Insights no effect], 2511.20867 (rho≈0), p_1tibfpn [R-D], p_1s4ljhs [R-D], c_p0lu7u5 [R-A], p_1wr588m [R-D]; consensus clusters 71, 78, 167, 168, 177, 191, 234, 235
- Debate 7 (quality): p_1wc7ius [R-B], c_p0lu7u5 [R-A]; consensus cluster 68; 2609.07559 (content scores weakly correlated)

## 8.4 Cases
- Case 1: c_okorz1k [R-B]
- Case 2: p_1w79x6u [R-B]
- Case 3: p_1ofa5qx [R-B] (website-building platform, not named in the main text)
- Case 4: c_p0lu7u5 [R-A]
- Case 5: p_1wc7ius [R-B] (the client commissioning the audit and the service name are not given)
- Case 6: c_o3aqism [R-B]

## 8.5 What to do
- Query alignment: 2609.07559, 2511.20867, p_1w79x6u, c_oeqjlr4
- Continuous updating: 2607.15771, 2605.25517, p_1wowxci
- Structural fields: 2602.12187
- Answer first: 2602.12187; consensus clusters 167, 168, 177, 191
- Short paragraphs: 2603.25500
- Original evidence worked into the body text: 2604.19113, 2604.25707, c_oz6botw
- Clear statements: 2605.25517, c_o0wrrkb
- Serving several queries: 2601.13938
- Noise floor: 2609.15164, c_p0lu7u5
- Do not do: 2603.25500, 2602.12187, 2511.20867, p_1wc7ius (sales tone -26%), 2509.05607, c_o3aqism, p_1sxlfgw, 2608.27631
- Already outdated: 2609.07559, 2506.11097, 2604.19113, 2609.07559 (strategies have a shelf life)

## Not used
- Evidence pack section F (commercial relationships), none used: p_1rwzpld, c_p5mukd8, p_1up8mlv, c_p5hegbz, c_of6wrha, p_1vhnnf8, c_oj3a1bz, c_p97wm07, p_1u037e3, c_p1z1uo5, p_1rij0b4, p_1s2vydl, p_1vwhnfy, c_omckckf

## Additions (new papers, 2026-10-11)

- Do not use an emotional style (goal-specific): E·2609.18282 (§5.1)

## Additions (new papers, 2026-10-20)

- Structural fields considered item by item: B·2610.15033 (Table 2, §4.2)
- Rewrites that do not specify a target: E·2610.21330 (§6.2, A.4)

## Additions (new papers, 2026-11-03)

- Chapter precondition note (under real retrieval, indexing and domain visibility matter more than writing): B·2610.30365 (§IV, Table IV, Table V)
- Principle 1 "the evaluation method itself can also change the conclusion" (scores from text given directly to models vs AI search rankings after reading pages, within-brand ρ 0.50 to −0.31; three AI search engines agree on first place 48.8%–66.3%): C·2611.01126 (Table 1, Table 3, Fig. 4)
- Principle 2 limitation of the defensive-clause conclusion (best-performing method optimizes an appended suffix with ranking feedback and used ChatGPT's actual rankings as feedback; some authors are authors of that method): C·2611.01126 (§1, §4.1, Table 1)
- Principle 4 item 4, AI search does not check numbers (statistics addition 80/80 with numbers unsupported by specs, e.g. "18% better heat retention", "30% energy saving"; average rank still better than originals): C·2611.01126 (§4.2 RQ4, Table 1, Table 6)
- 8.2 statistics addition when pages are supplied (average rank 3.18/3.31/3.83 vs 5.28/5.84/4.88; Top-1 10.0%/11.3%/5.0%) and limitations (URLs supplied manually, template originals, author conflict of interest, rerun changes about 20% of first places, reversed order 73.8% vs 93.8%): C·2611.01126 (Tables 1–3)
- 8.2 on-page GEO writing has no detectable effect under real retrieval (OR 0.91, p=0.711, equivalence test rules out twofold effects; visibility low 0, high 38.4%–78.3%, medium 14.3%–42.9%; 46/10; day-25 snapshot): B·2610.30365 (§III-B, §III-D, §IV, Table IV, Table V, Appendix H, §V)
- 8.2 measurement problem (reruns, reversed order, identity labels in product names, ±0.2% price, brand page vs product pages): C·2611.01126 (Tables 1–3)
- 8.3 Debate 1: correlations in real logs (statistics 2.11/1.17, inline citations 1.34/1.22, terminology 2.26/1.71, fluent prose 0.67/0.58) and no effect in the intervention: B·2610.30365 (§III-A Table II, §IV); third case (unsupported numbers): C·2611.01126; side-by-side table of three kinds of evidence: C·2609.07559, C·2611.01126, B·2610.30365
- 8.5 Recommended "confirm indexing first": B·2610.30365; Do not do "unsupported numbers": C·2611.01126; Already outdated addition: B·2610.30365
- Key points 1, 7, 8 additions: B·2610.30365, C·2611.01126
