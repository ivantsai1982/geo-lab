# Chapter 2: Triggering: Source map

> This file is for tracing only and is not part of the main text. Paper numbers are close-reading note ids; forum entries are evidence-pack entry ids.

## 1. Core principles

| Section | Conclusion | Source |
|---|---|---|
| Principle 2.1 | Search is jointly decided by the harness instructions and the model | Paper 2609.19244 (B) |
| Principle 2.2 | GPT-5.3-chat 14% / Claude Sonnet 4.6 83% (same set of 1,000 prompts) | Paper 2609.19244 (B) |
| Principle 2.2 | ChatGPT 57.8% of runs with zero citations (45 days of repeated measurement) | Paper 2604.07585 (B) |
| Principle 2.2 | ChatGPT 75.8% did not trigger search; 69.4% intent misjudgement, 30.6% safety refusal | Paper 2603.25500 (B, WWW 2026) |
| Principle 2.2 | AIO 55,393 popular searches 13.7%; questions 64.7%, non-questions 9.5% | Paper 2605.14021 (B) |
| Principle 2.2 | AIO real query logs (ORCAS) 51.5%; interrogatives 89.9%, non-interrogatives 51.9% | Paper 2604.27790 (B, SIGIR 2026) |
| Principle 2.2 | AIO browsing records of 900 people about 18% | Paper 2608.04831 (B, IC2S2 2026 extended abstract) |
| Principle 2.3 | Long queries, queries starting with a question word, and queries containing nouns and verbs trigger more easily | Paper 2608.04831 (B) |
| Principle 2.3 | Questions 60%, statements 37%, navigational 12% | Paper 2602.13415 (B) |
| Principle 2.4 | AIO 7 countries→229 countries; US 42%→67%; Covid 1%→66% (sample 74) | Paper 2602.13415 (B) |
| Principle 2.5 | API with List your sources: search invocation 12.1%→88.4%; citations per response 0.60→7.05; product-side citations 16.6→19.9, composition change ≤2.1 percentage points | Paper 2609.00319 (B) |
| Principle 2.6 | 14–53% of claims supported by search results but not cited; 15–20% or more of claims not grounded; more search only mixed effects | Paper 2609.19244 (B) |

## 2. How strong is the evidence

- 613 users, 171,264 conversations: Paper 2609.19244
- All other items: the papers matched in the table above.

## 3. Debates and counterexamples

| Debate | Content | Source |
|---|---|---|
| Debate 1 (triggers) | About 2,000 answers, B2B buyer-intent questions; citation appearance rate ChatGPT 95%, AIO 99%, Perplexity 100%; "trigger rate is a property of the question" | Forum c_p6b6y7n (R-A) |
| Debate 1 (does not trigger) | Brand comparisons 76/80 no search; situational questions 106/120 no search; broad categories about half searched | Forum c_p7ejcg6 (R-B) |
| Debate 2 | Purchase intent 93% carousel vs comparison 15% (author states a related business) | Forum c_olk9q6g (R-B) |
| Debate 2 | Purchase execution 93% vs post-purchase 2.8% | Forum c_ojuxkg5 (R-D) |
| Debate 2 | Carousels depend mainly on the structure of product feeds | Forum c_olk9q6g (R-B), c_ondhads (R-D) |
| Debate 3 | Research questions rely on training, purchase questions trigger search | Forum c_oklho47 (R-D) |
| Debate 4 | Complex prompts do not trigger deep research | Forum c_olswb4f (R-D) |

## 4. Cases

| Case | Source |
|---|---|
| Case 1: mentioned about 6%, website audit ineffective; search on/off test, scoring of about 180 companies | Forum c_p3dytm0 (R-B) |
| Case 1: search on about 16%, off 0 | Forum c_p3gcoyd, c_p3hk1kn (R-D) |
| Case 2: local business 0% from internal knowledge, differs by product with search on | Forum c_owgjjpn (R-D) |
| Case 3: new entity after training cutoff, training crawlers blocked, real-time fetchers normal | Forum c_oqegw5q (R-D) |
| Case 4: 285 answers per week, four weeks; auto mode mostly no search; 0.226→0.285 | Forum c_p0ld2a0 (R-B) |
| Case 4: fluctuation about 3 times, 95% interval about 1.0–11 | Forum c_p0kt0pd (R-D) |
| Case 4: ChatGPT auto mode zero citations, about 4 seconds vs 15–40 seconds; 18/280 (author states they provide related services) | Forum c_p4a5j8e (R-B) |

## 5. What to do

| Practice | Source |
|---|---|
| Classify queries, target questions and long queries | Paper 2605.14021, 2604.27790, 2608.04831, 2602.13415; Forum c_p6b6y7n |
| Search on / off comparison | Forum c_p3dytm0 |
| Zero citations indicate no search; all 406 non-connected answers had zero citations | Forum c_p0ld2a0, c_p7ejcg6 |
| Gemini 493/500, Perplexity 500/500, ChatGPT 343/406 | Forum c_p7ejcg6; also ChatGPT 334/500 without query expansion, see c_p8z81mr (R-B, not listed separately in the main text) |
| Words such as "latest" and "2026" push up search | Forum c_p7ejcg6 |
| API settings must be stated | Forum c_p0ld2a0, c_p4a5j8e; Paper 2609.00319 |
| Platform policy changes | Paper 2602.13415 |
| Third-party comparison content as long-term leverage (opinion) | Forum c_p3dytm0; consensus cluster 1 (freshness, not used directly in the main text) |
| Already outdated: low overlap between AI sources and the SERP | Paper 2604.27790 (Jaccard 0.11–0.18) |

## Not used

- Leads to check (commercial relationship) c_ohfc7t6, p_1w5ce7j, p_1vt0xke, c_ohorxep: not used.
- c_otx76a5 (R-D, author sells related services, timing claims lack support): not used.
- p_1sa5c83 (R-B, 29% AIO; contains click and traffic figures that cannot be verified): not used.
- c_o9pwqs3, p_1snhik2, c_okazce8, c_oinjiys, c_ouu1f6z: weakly related to this chapter's topic of triggering, left for later chapters.
