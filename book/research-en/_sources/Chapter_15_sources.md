# Chapter 15 source trail: The Role of Reddit and Social Platforms in AI Search

> This file is for tracing only and does not go into the main text. Paper numbers, forum item ids and consensus cluster numbers all come from internal evidence pack (not published).

## 1. Core principles

| Section | Conclusion | Basis |
|---|---|---|
| 15.1 | Social platforms belong to the third-party source ecosystem; accessibility is affected by crawling/licensing policy | Framework main thread; 2609.19244; c_p6xqznm (report of Reddit tightening AI crawler blocking in mid-August, see context) |
| 15.2 | Social citation shares: Search GPT 0.1%, AIO 8.5%, organic results 13.4%; domain overlap 24%/25%/68%; 11,000 NQ questions | 2603.16138 (B) |
| 15.2 | reddit.com/youtube.com appear in ChatGPT and Grok, completely absent from Claude search; 613 users, 171,264 conversations | 2609.19244 (B) |
| 15.2 | General-purpose LLMs: 18 of 4,932 citations (0.4%) point to Reddit | 2609.14575 (B) |
| 15.3 | AIO community/forum sources under-used −22.1pp; Wikipedia and long documents over-used; limitation of max-over-chunks measure | 2603.16138 (B) |
| 15.3 | 14–53% of answer claims supported by search results but not cited | 2609.19244 (B) |
| 15.4 | Reddit Answers: 30,000 answers; OR 2.88, 1.97; percentile 0.91 vs 0.45; formality OR 1.488, experiential tone OR 0.789; first person 3.3%→0.06%; moderator pinned/flagged OR 0.010/0.052; 41.8%, 89.6% | 2609.14575 (B) |
| 15.5 | 105,012 subreddits; comments +12.0%, users +12.4%; experience-based 2.3/2.8 times; Q2 55.6%/77.2%; after AI Mode 9.54→−0.17, 6.29→2.57 (59% decay) | 2605.16428 (A) |
| 15.6 | UGC 16.7–23.4%, Reddit share of UGC 53.7–70.7%; about 13 words: exposure 57–76%, citation 34–61%, mention 22–37%; mention 0 when not exposed; Co-STORM 100%; OmniThink 37.8%; 0.5–3.9% poisoning still 29.7–52.5%; perplexity AUROC<0.68; output similarity ineffective; blocking UGC; Gemini DR 623/5157 (12.1%), OpenAI DR 0.4% | 2605.24245 (D) |

## 2. How strong is the evidence

| Conclusion | Basis |
|---|---|
| Evidence grade for each row | 2605.16428 (A), 2603.16138 (B), 2609.14575 (B), 2609.19244 (B), 2605.24245 (D); effect of brand participation: p_1v45557 (R-B), p_1vhostn (R-A) |

## 3. Debates and counterexamples

| Section | Conclusion | Basis |
|---|---|---|
| Debate 1 | Commercial questions: Reddit 1.8%, Wikipedia <0.6%, about 90% to vendor documentation; 127,198 citations, about 16,400 questions, 5 engines, March–June 2026 | p_1uirn62 (R-B) |
| Debate 1 | About 74k citations: AI Mode 528, Gemini 258, ChatGPT 23, Claude 1, Perplexity 0/17,476; Google about 97% | p_1u0g32z (R-B); c_oqllndm (R-D) |
| Debate 1 | WordPress plugin, 8 weeks, 2 of top 8 sources were 2022/2023 threads; Perplexity most active | c_ohp458k (R-B) |
| Debate 1 | BOFU, 100 answers, Reddit <5% | c_odz0map (R-D) |
| Debate 1 | Reddit often in top three | c_owwgr5m (R-D) |
| Debate 1 | Consensus "Reddit is still the most-cited source" is contested | Cluster 197 (6 for / 2 against); Cluster 101 |
| Debate 2 | 3.8%→0.5%, about 86% drop | p_1vwuthp (R-B, main text quotes third-party data); c_p59syal, c_pa2f2hf (R-D context); Cluster 141 |
| Debate 2 | 1,564 API questions, 7/10 categories, 38 times (2.4%), 92% from reviews-and-opinions | p_1vwuthp (R-B) |
| Debate 2 | Only ChatGPT affected; citation attribution ≠ model behavior | c_p59syal (R-D) |
| Debate 2 | 46 questions 9→3, replaced by mid-sized vendor blogs; short-window swings have reversed | c_pa2f2hf (R-D) |
| Debate 2 | Rise in share of searches using the `site:` operator | c_pa2f2hf (R-D context) |
| Debate 3 | 4 questions, 96 checks, 0 citations; new questions from 8/26, 9 times in 6 days; sources about 9→6 | c_p6xqznm (R-A) |
| Debate 3 | "A vendor claims" Perplexity made a major turn within two weeks (unverified, not named) | p_1ucao4c (zone F, lead to check) |
| Debate 4 | 3-week thread with 40 upvotes beat 2-year-old blog post; deep comments cited | p_1v70w9y (R-D) |
| Debate 4 | 60% of citations from within six months | p_1sr8co7 (R-D) |
| Debate 4 | 96% stability, traceable back 7 years | c_p6sabv3 (R-D) |
| Debate 4 | "A vendor claims" 60–70% of cited threads are archived (unverified, not named) | p_1vwpfgm (zone F, lead to check) |
| Debate 5 | Consistent narrative, consistent messaging across the web | Cluster 80, Cluster 64; compare 2609.14575, 2603.16138 |

## 4. Cases

| Case | Basis |
|---|---|
| Case 1: 100 buyer questions, 8 weeks before and after | p_1v45557 (R-B) |
| Case 2: 4 weeks lurking, 90 days 8%→39% | p_1vhostn (R-A) |
| Case 3: 20 posts not cited by ChatGPT | p_1v1enkn (R-D) |
| Case 4: LinkedIn 1,310,455 URLs | p_1w7f08y (R-B) |
| Case 4: 350 non-brand questions, 20 of 22 URLs Pulse | c_p8jc3da (R-A) |
| Case 4: Brand page posts help little | Cluster 113 |
| Case 5: Distribution of 86 social citations | c_p5tpa76 (R-D) |
| Case 5: 40 questions, Gemini 22, ChatGPT ≤1 | c_paiwlt6 (R-D, title) |

## 5. Compliant participation vs manipulation

| Conclusion | Basis |
|---|---|
| Personal account + disclosure; brand accounts rejected | c_okj01yc (R-D) |
| Aged-account posting services, negative-thread removal services | c_ozu538y (R-D, context) |
| Self-admitted black hat | c_ozu538y (R-D) |
| Manufacturing "natural-looking" mentions | c_o8e4yqr (R-D, tool name not given) |
| Mechanism of planting short phrases | 2605.24245 (D) |
| Banned, appeals unanswered | c_o7yn8qt (R-D) |
| Citation sources cut off | c_p6xqznm (R-A), p_1vwuthp (R-B) |
| Moderator-flagged not selected; first person erased | 2609.14575 (B) |
| Cited a lot, used little | 2603.16138 (B) |
| Blocking UGC as an effective defense | 2605.24245 (D) |

## 6. What to do

| Practice | Basis |
|---|---|
| Measure first, then invest | 2603.16138, 2609.19244; p_1uirn62; c_ozu538y |
| Separate by engine | p_1u0g32z, c_paiwlt6, c_ogr9na2 |
| Separate by question type | c_p6xqznm, p_1vwuthp, p_1v45557 |
| Participate in threads already cited and still open | p_1vhostn; c_p9q3hkx |
| Formal, specific, answer in first two sentences | 2609.14575; p_1vhostn |
| Real identity and disclosure | c_okj01yc |
| LinkedIn personal long-form | p_1w7f08y, c_p8jc3da; Cluster 113 |
| Measure citations separately from traffic/leads | c_p9q3hkx; 2603.16138, 2609.19244 |
| Multi-week tracking | c_pa2f2hf, c_paiwlt6 |

## Content not used

- Remaining leads to check in zone F (p_1w6cimz, c_p4mdr3s, p_1u1xlwg, c_p8p6469, p_1vys3ea, p_1rlkbss): the authors have commercial relationships with the brands mentioned; not used as evidence or cases.
- Exaggerated or unverifiable R-D numbers (59.7% from c_ofdjej5, 90% from c_nz6xy8r, 129% from c_nr8hl1y, 75% from c_onrkuga, 450% from p_1sr8co7): not written into the main text as numbers; only the freshness claim from p_1sr8co7 is used as a contrasting lead.
- Contradiction between 2605.16428 and 2602.18455: the evidence pack has no details on 2602.18455; not written in.

## Supplement (new papers, 2026-10-11)

- New row in the evidence table, gap split into two layers, risk of citations persisting after deletion: B·2610.11932
- Qualification of "write formally": E·2609.18282 (Table 3: ρ 0.947 → −0.073)
