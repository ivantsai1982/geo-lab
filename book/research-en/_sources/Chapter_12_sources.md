# Chapter 12 Source trail: Platform Differences and the Chinese-Language Ecosystem

> The identifiers below do not appear in the main text. Paper grades follow the evidence pack's labels; forum entry grades follow sections C/D of the evidence pack. Section F (leads with commercial relationships, pending verification) was not used at all.
> "Large forum and community sites" in the main text means reddit.com, which appears as a platform being cited, not as a source of evidence.

## 1. Core principles

### 12.1 Each platform is a different pipeline
- Framework main thread: main thread of 03_GEO教材框架_v1.md
- Overall judgment: 2609.19244 (B), 2609.18729 (B), 2604.27790 (B); cluster 154

### 12.2 Where the differences appear (table, row by row)
- Triggering 14% vs 83%: 2609.19244 (B)
- Blocking Google-Extended and zero citations in Gemini, fewer citations in AIO: 2604.27790 (B, correlation)
- URLs returned per query, ChatGPT 14.06 / DeepSeek 5.46: 2609.19244 (B, in vivo, 613 users, 171,264 conversations)
- Claude results without reddit.com / youtube.com: 2609.19244 (B)
- Own-asset bias: 2604.27790 (B), 2609.06798 (B); Baidu's own subdomains: 2609.24407 (B)
- First-person recommendations 79% / 7% / 2%: 2609.18729 (B)
- Citation counts 6.88 / 12.06 / 16.35 and influence 0.2713 / 0.0584 / 0.0646: 2604.25707 (E, secondary analysis of a static snapshot)

### 12.3 Platforms favor their own assets
- Google AIO cites YouTube most often for health queries (above CDC/WHO/Mayo): 2609.06798 (B)
- Jaccard 0.11–0.18 across three interfaces, AIO-SERP 0.18, own-asset bias: 2604.27790 (B)
- Baidu: 2609.24407 (B)

### 12.4 Levels of observation are not equivalent
- Interface vs API domain overlap 12.0% / 14.8%: 2609.18729 (B)
- Single run 2.65 → 3 runs 5.56 domains; product set Jaccard AIO 0.421 / Gemini 0.287 / ChatGPT 0.178: 2609.18729 (B)
- Slight rewording RBO AIO 0.49 / SERP 0.74; rerun on the same device 0.69 / 0.86: 2604.27790 (B)
- Model versions 3/10, and the smaller model always recommending the same company: c_okf8zbr (R-A)
- Model versions 8/10 vs raw API 0: c_okfasdi (R-A); see also p_1t65t5j (R-B)
- 14–53% supported but uncited, 15–20% or more not groundable: 2609.19244 (B)

### 12.5 The Chinese-language ecosystem
- Feature 1 (appearance rate, Gini, Top-1, Jaccard 0.008–0.034, cosine 0.701–0.813 on 331 shared queries; 500 translated queries, single run, Milan): 2609.24407 (B)
- Feature 2 (local citation share for English queries, native language raising it 3.5–13.5 times, Japan / South Korea, TCM return rate about 42%, Baidu about 1 citation on average): 2609.06798 (B)
- Feature 3 (614×8×3, 160,860 citations, source structure, 66/30/8, silent citations 39.3%, 8.3%, 2.1% vs 59.9%, quality score importance 4.52%, freshness 18/39 and 101/68 days, App/Web Jaccard 0.19–0.51, Qwen URL-level 0.014; author type: vendor): 2607.15771 (B)

## 2. How strong is the evidence
- Basis for each row as above; "low overlap" also draws on c_p8zzzcy, c_p9014sz, c_p90541x, p_1v98pfc (high-evidence entries in cluster 154)
- Practitioner corroboration that Claude has no forums/video: p_1uqxstc (R-B), p_1tjaru2 (R-B); c_ouhrag1 (R-D)
- Lack of controlled practitioner tests for the Chinese-language ecosystem: sections C/D of the evidence pack contain no entries on Chinese platforms (only p_1vbli31 includes DeepSeek, Kimi, GLM, Qwen; p_1rllrcj includes DeepSeek)

## 3. Debates and counterexamples
- Debate 1: p_1uqxstc (R-B, about 150,000 citations, publications and web pages 86–97%, AI Mode YouTube about 8%, ChatGPT forums about 5%, reference about 4%, Claude about 97%), p_1v98pfc (R-B, 14/16); opposing: c_p9ddw51 (R-A, 40 prompts, Gemini 22, AIO 20, ChatGPT ≤1), p_1tjaru2 (R-B, Gemini about 750, GPT-5 and Claude zero); also c_ozcuyui (R-A, grounded OpenAI 2,410 citations: Wikipedia 10.2%, reddit 4.6%, G2 4.1%, vendors' own sites 7.3% combined), figures not written directly into the main text
- Debate 2: 2604.25707 (E) vs p_1ux24pu (R-A, 70 prompts, 1,474 answers, 30 days; Gemini 15.08, OpenAI 9.62, AIO 5.34, Perplexity 5.04)
- Debate 3: 2609.18729 (B) vs c_owd32y9 (R-A, incognito reruns: Perplexity about 85%, ChatGPT about 2/3, Google unchanged in about 60% of cities)
- Debate 4: 2609.18729 (B, 5.4%, 76.7%), 2604.27790 (B), c_p8zzzcy (R-B, 11–14%, about 25%), c_p9014sz (R-B, 10.6–12.0%, AIO×Gemini 26.1%, AIO×Perplexity 20.7%, Gemini×Perplexity 16.8%), c_p90541x (R-B), c_p4l9mmv (R-B, 197 clinics, 39–48%), c_p9d333s (R-B, median 11%); pooled vs per-prompt: c_p21imml (R-D)
- Debate 5: cluster 121 (disputed, 5/0); c_oaxcuxl (R-B, Perplexity days vs ChatGPT weeks); p_1rllrcj (R-B, ChatGPT 2–4 weeks)
- Debate 6: cluster 154; p_1rllrcj (R-B, about 40% of ChatGPT's first-ranked brands invisible on DeepSeek); c_ov06pz1 (R-D, Google + Bing roughly cover it); for the view that pages are shared but source sets differ, see also c_p8zvfom (R-B)
- Debate 7: p_1rllrcj (R-B, 15 pages, two months); conflicts with: framework main thread, sentence 3

## 4. Cases
- Case 1: p_1whwdqn (R-B, 2026-09-16; 185,600 times, 400 pages/day, <100, about 1,500 clicks/day, 34 Asian markets, 7 of the top 12 queries, 61–85%)
- Case 2: c_ot4nobl (R-B, 2026-06-22; 0 → 6/10 prompts, 3/5 platforms, one month)
- Case 3: p_1w12ohu (R-B, 2026-08-28), p_1w1gaay (R-B, 2026-08-29; 11.9% / 26%, 376/206/134/92, 70%, 36/48, 14.4/14.1/9.7%); supplement c_p9d333s (R-B, 2026-09-12; 9,217 answers, 25/36, Perplexity source composition)
- Case 4: c_p9gwsyh (R-C, about 650 pages), c_p9q4a26 (R-D, 659 vs 0); corroboration c_on7yw9u (R-D, deindexed site), p_1we6og8 (R-D, 230 users)
- Case 5: p_1vbli31 (R-B, 2026-07-31; 29 brands, 19/29, 0.91 / about 18%, 6/10, Copilot zero overlap); c_p0uaudt (R-D, multi-model brands relying on verifiable third-party facts and financial media coverage; limitation of a single run)
- Case 6: c_okfasdi (R-A, 2026-05-07)

## 5. What to do
- Report by platform, no merged score: c_ozcuyui (R-A), p_1ty0b8t (R-B), c_pajewrb (R-D), cluster 154; research side 2609.18729 (B)
- Consumer interfaces, at least 3 runs: 2609.18729 (B)
- Logged out, incognito, new conversation: c_owd32y9 (R-A), p_1ui3yy4 (R-B), c_ot4nobl (R-B)
- Confirm whether it searched: p_1ui3yy4 (R-B), c_ougrb3w (R-B)
- Fixed prompt set rerun weekly, brand echo: c_p9ddw51 (R-A)
- Test on another platform first (25% vs 12.5%): c_p9o5xt3 (R-A)
- App/Web separately: 2607.15771 (B)
- Reachability classification, half to two thirds: c_p8zvfom (R-B), c_p8zzzcy (R-B, 17 of 38 pages owned by competitors)
- Google-Extended: 2604.27790 (B)
- Check the index when absent from Gemini: c_on7yw9u, p_1we6og8, c_p9q4a26 (all R-D), c_p9gwsyh (R-C), c_p8vlrtu (R-C)
- Multi-source co-occurrence: 2607.15771 (B), p_1vbli31 (R-B), c_p0uaudt (R-D)
- Native-language content: 2609.06798 (B)
- Pages by country: p_1whwdqn (R-B)
- Freshness: 2607.15771 (B)
- No one recommended for describe-the-problem queries: p_1w5f3hg (R-B), c_ougrb3w (R-B)
- Baidu's own subdomains: 2609.24407 (B)
- Traffic trade-offs: c_p9uxsz8 (R-C), c_p1m3g23 (R-D); "no research proves it reliably brings traffic": framework main thread, sentence 4
- Do not do / advice aimed at Google interfaces does not transfer: c_p9ddw51 (R-A)
- Already outdated / ranks well on Google but absent from AI: p_1u2s85l (R-B), c_p5190s9 (R-B); Chinese quality score: 2607.15771 (B)

## 6. Key points
- 1–2: 2609.19244, 2609.18729, 2604.27790; c_p8zzzcy, c_p9014sz; cluster 154
- 3: 2604.27790, 2609.06798, 2609.24407
- 4: 2609.18729, 2604.27790; c_okf8zbr, c_okfasdi
- 5: 2609.24407
- 6: 2609.06798
- 7: 2607.15771
- 8: p_1rllrcj; c_p8zvfom; cluster 121

## Not used (section F, commercial relationship)
c_o7d2ln4, p_1uw07cu, p_1ur1shm, c_p473dfa, p_1rpwsnu, p_1ugx6qf, p_1shg6vc, c_otn9wlf, c_p81y5bo, c_p87pomp, c_okktcs7, p_1rkkxtp, p_1uwjv28, p_1uey5qe, p_1vz4rk7, p_1vz6g03, p_1sfmw0b, p_1ugjgir, c_otlfa20, p_1uf59e8, p_1wsasr1, p_1wd6vc8, p_1wchegg, p_1vvjkx2, c_p9rxg5h

## Not used (sections C/D, other reasons)
- p_1w2tdfy (R-C, a question, includes a product name), c_ool0tbs (R-B, local map pack, belongs to the local SEO topic), c_p4czgif (R-C), c_pcq1lmz (R-C, feature launch), p_1waokeo (R-B, answer quality comparison, not source selection), p_1sic0m8 (R-C, no claim), c_ofx2d4y (R-B), c_o224gia (R-B), p_1tum8e3 (R-B), p_1ulhszj / p_1uli8s0 (R-B), c_p99rask (R-B), p_1u2s85l used only for "Already outdated", c_o224snn, c_onykpu2, p_1tv76qr, p_1tgmtpk, p_1wbdl54, c_p1vetsq, c_ovvvhd3, c_p9zqgae, p_1uip47u, p_1ue82jb, p_1t98rdv (R-D)

## Supplement (new papers, 2026-10-03)

- Qualification on the measurement advice to "open a new conversation": E·2609.40069 (§3)

## Supplement (new papers, 2026-10-20)

- Chinese questions searched in English: B·2610.15382
