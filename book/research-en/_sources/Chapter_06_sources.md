# Chapter 06 source mapping (not part of the main text)

Evidence packs: internal evidence pack (not published)

## Core principles

### Principle 6.1 Relevance as gatekeeper
- Two-source experiment (252,000 trials, 6 models, 18 factors, 1,440 scenarios; 11/18 significant, 7/18 no consistent effect; formatting OR 0.79–1.68; recent timestamp OR 14.4 to >10k): E·2605.25517 (SIGIR'26, industry authors, LLM-generated corpus)
- Query relevance Spearman 0.388 vs content score 0.114: C·2609.07559 (authors are a vendor)
- Citation failure diagnosis, 949 pairs: 62.2% / 27.1% / 10.1% / 0.6%; at baseline 43% of relevant pages not cited: D·2603.09296

### Principle 6.2 Position effect
- U shape, worst-case drop of more than 20%, below closed-book 56.1%, >20 documents only +1–1.5%, enlarging the window no improvement: E·2307.03172 (TACL)
- Position 1 gain larger than all rewrites, only 3 of 54 scenarios significant: E·2506.11097 (NeurIPS'25)
- Shopping agent: views 1.63–5.83 vs 1.12; coefficient about 1/4–1/10 of humans; lowest at ranks 68–74 then rising again; not significant at highest reasoning setting: E·2608.22697
- Controlled replay 42.3 → 7.9 → 0: D·2609.15164

### Principle 6.3 Signal weights and the say-do gap
- Hotel audit table (+31.65 / −30.03 / +11.61 / +8.31 / −1.79 / +0.11; position 2–4pp, $11.7, about 26pp; Spearman 0.59–0.85; position ≤0.7%; 61,459 calls, 12 models, 3,024 choice sets): E·2606.16344 (preregistered)
- Authority metadata flips 39.2%, 68.2% toward higher authority, sensitivity 17.4%–49.2%, authority mentions −24.0pp vs flips −12.9pp, mild prompt rebound in frontier models: E·2609.00248

### Principle 6.4 Preference for AI style
- Perplexity 1 SD: 47% → 56%; replicated in randomly ordered RAG; polishing +1.07 / +2.11: D·2509.14436

### Supplement: Appearing ≠ being selected
- See sources for "Case 2"

## How strong is the evidence
- Single generation 15% flips, 45% of variance from decoding: D·2609.15164
- Observational vs controlled position gap: D·2609.15164
- Conflict of interest of the scoring vendor: 2609.07559

## Debates and counterexamples
- Debate 1 (formatting): E·2605.25517; D·2609.15164 (+0.50 citation count, +4.5pp CI [−1.4,+10.4]); p_1tu2kr4 (R-B, structure and schema as baseline); p_1skbtgs (R-B, comparison tables 2.4 times, author credentials 12%→31%)
- Debate 2 (position): E·2307.03172, E·2506.11097, E·2606.16344, E·2608.22697, D·2609.15164
- Debate 3 (authority): E·2609.00248; D·2603.09296 (fixed disadvantage on domain authority); p_1s67wgj (R-B, backlinks/DA almost unrelated); c_om4e6sa (R-D, DR 7 page wins); cluster 48 (disputed)
- Debate 4 (freshness): E·2605.25517 (main text and Table 2 inconsistent); p_1s67wgj (R-B, platforms prefer freshness, 30-day updates)
- Counterexample (broad questions occupied by big brands): c_p4fwgc3 (R-B); cluster 39 (disputed, support 6 / oppose 0), cluster 125 (consensus support)

## Cases
- Case 1: c_p4fwgc3 (R-B); clinic equipment models also in c_p74oq5h (R-D)
- Case 2: p_1s67wgj (R-B, 78%→31%); c_p0p2h2l (R-B, 1,444 / 241 / 83%); p_1w22mjh (R-B, 2,475 brands, 86%); p_1tb2l0z (R-B, 12,000+ sequences, 87%)
- Case 3: p_1vf9fbz (R-A); p_1vf92lu (R-B, same experiment)
- Case 4: p_1t96o06 (R-B, replaced in the first turn in four of six journeys; its own proprietary scoring metric not used)
- Case 5: c_oem9kv6 (R-D, text spans the end of part1 and the start of part2)
- Case 6: c_ors4sak (R-D)
- Additional lead: c_p4kz64b (R-D), c_odns79x (R-D), c_o29p754 (R-D, 21/25)

## What to do
- Around specific questions: E·2605.25517, C·2609.07559, D·2603.09296; c_om9yzae (R-B), c_op3g2pe (R-B)
- Specific facts: E·2605.25517; c_p4fwgc3 (R-B); c_p3j8hy3 (R-D)
- Publish prices: E·2605.25517; c_ors4sak (R-D)
- Updates and dates: E·2605.25517; p_1s67wgj (R-B)
- Ratings and review counts: E·2606.16344
- Targeted changes after diagnosis (56.58%→79.52%, about 5% of content): D·2603.09296
- Stage-by-stage tracking: p_1w51clk (R-B)
- Repeated testing: D·2609.15164
- Check list passages: c_oem9kv6 (R-D)
- List order: E·2506.11097, E·2608.22697
- Do not change only formatting: E·2605.25517, D·2609.15164
- No generic rules / heavy compression: D·2603.09296
- Keyword stuffing: C·2609.07559 (score −13.0); p_1skbtgs (R-B)
- Vague wording, self-contradiction: E·2605.25517
- Do not trust self-reports: E·2606.16344, E·2609.00248
- Management replies ineffective: E·2606.16344
- Outdated (quotations/statistics/sources +42.6/+32.8/+27.7 → −0.33/−0.28/−0.79; n=605): C·2609.07559; Statistics lowered rank in 19/24: E·2506.11097
- Domain authority: p_1s67wgj (R-B), c_o3w8q9w (R-D), c_oeg8un1 (R-D)

## Not used
- All of Section F (leads with commercial relationships, to be checked): c_ojdeurh, p_1w4e6s2, c_okcrywp, p_1t2moid, p_1vfn1f1, p_1pj08s1, p_1pjvtf7, c_oiwj4iw, p_1uq3wru, p_1wiw1dy, c_ohfewjv, p_1w47emu
- p_1riwsqt, p_1ra6mqq (text deleted); c_p848bws (screenshot only); p_1wdncg6 (model self-report, usable only as a hypothesis); p_1sqohve (analysis of leaked source code, belongs to the retrieval stage); p_1vwrkwd (preferred sources feature, not evidence of the selection mechanism); c_onxvpkm (author admits causation not verified, numbers lack confidence intervals)
- Other R-D items not cited individually: p_1t48knc, p_1tbswhc, c_p0kzpse, p_1t634rv, c_oat64bt, c_p4fpysw, c_opao7r6, p_1ta44ii, c_p0m6so8, c_o9tgytu, c_p0y0v04, c_o6mqc1u, c_olpnt21, p_1t0fr4a, c_ot3ic0c, c_p6baeeu, p_1u7e7gq, c_ocx6djg, c_p79f8tn, c_p3nqs35, p_1swlnjw, c_og6un8n, c_ovyh4n3, c_p2590uh, c_olq4h5l

## Supplement (2026-10-03 new papers)

- Scope of Principle 6.2 (ranking amplified in multi-round search): E·2609.39026 (Table 3: ranking sensitivity 0.5849, direction error 0.4907)
- "Method caution" in How strong is the evidence, path-dependence mechanism in Case 4: E·2609.40069 (§3, §6)

## Supplement (2026-10-04 author's tests and official FAQ)

Experimental data: the authors' own experiment runs (raw data not published); handoff: internal notes (not published). Official: OpenAI Publishers and Developers FAQ (help.openai.com/en/articles/12627856, read 2026-10).

- Supplement paragraph "Sites the model names on its own initiative are selected more often": three question types 18/20, stratified odds ratio about 3.6; swimming 9/10, about 2.7 (author's tests; the authors' own experiment runs (raw data not published) and recalculation during review)

## Supplement (2026-10-11 new papers)

- Qualification of Principle 6.4: E·2602.16136 (Table 1a: SEO-style synthetic documents 67% of pool, top 10 80.95% / 79.98%; Table 1b: misleading exposure ≤0.09%)

## Supplement (2026-10-20 new papers)

- Recency in real environments: B·2610.15382 (AUC 0.482, 0.535)
