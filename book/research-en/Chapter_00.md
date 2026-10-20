# Chapter 0: How to Read GEO Evidence

## Questions this chapter answers

1. Under what conditions were figures such as "GEO can raise visibility by 40%" actually measured?
2. What kinds of design does GEO research use? Which one produces conclusions closest to the real world?
3. Why do results change when you ask the same question twice, switch engines or switch languages? What does this mean for "proving it works"?
4. How far should you trust practitioners' experience, vendors' reports and community consensus?
5. When you are handed any GEO claim or report, in what order should you check it?

## 1. Core principles

### 1.1 Every GEO conclusion comes with "conditions"

AI search is not a fixed ranking table. It is a random, multi-stage filtering pipeline:

```
Triggering → Accessibility → Retrieval → Selection/ranking → Citation → Absorption → User behavior
```

A study usually measures only one or two of these stages. So every conclusion carries an implicit question: **which stage of the pipeline was measured, with what system, and under what conditions?**

The most typical example is the widely circulated "GEO raises visibility by up to 40%". The conditions behind this figure are:

| Condition | What actually happened |
|---|---|
| Did the page first have to be found by search? | No. The page was already placed among 5 candidate documents |
| Who generated the answer | GPT-3.5 |
| What was measured | The share of words in the answer belonging to that page (relative increase, 19.3 → 27.2) |
| What it does not mean | It does not mean the page is easier to retrieve, and it does not mean more traffic |

So it answers only one question: "once a page is already in the candidate set, can rewriting make the answer use it a little more?" It does not answer what readers really care about: "will I be found, and will it bring business?"

### 1.2 Four generations of research

To understand a study, first look at which generation it belongs to and which question it is answering:

| Generation | Period | Main question |
|---|---|---|
| First generation | 2023–2024 | Can content change visibility in AI answers? (Showed that it "can") |
| Second generation | 2024–2025 | Can this influence be manipulated maliciously? (Showed that it "can") |
| Third generation | 2025 | Do the techniques generalise to other engines and other domains? (Found it "hard", and found zero-sum competition) |
| Fourth generation | 2026 | How much of the effect remains once placed back in the full pipeline? How can it be measured reliably? How should it be governed? |

The earlier the study, the more likely its figures are optimistic numbers obtained under simplified conditions. When citing an early figure, ask whether later research has repeated it under more realistic conditions.

### 1.3 Simplified conditions systematically overestimate effects

A "fixed context" experiment feeds the page directly to the model, skipping retrieval and ranking. This makes variables easy to control, but it misses the elimination that happens in the early stages of the pipeline.

```
Fixed-context experiment:   [Your page is already in the candidate set] → Generation → Measurement
Full pipeline:              Query → Retrieval (may be eliminated) → Reranking (may be eliminated) → Truncation (may be eliminated) → Generation → Measurement
```

In controlled experimental systems, when prompt injection attacks were placed in a full "retrieval → reranking → generation" pipeline:

- generic instruction-override injections lost about 40% at the retrieval stage, with an end-to-end success rate of about 14.7%;
- gradient-based attacks had an end-to-end success rate below 2%;
- only rewriting-style injections that stayed highly relevant to the query still had an end-to-end success rate of about 40%–54%.

The same set of attacks had been reported at about 80% success under fixed context. The gap comes almost entirely from "whether the attack had to pass the retrieval gate".

Observational data also overestimates. In controlled experimental systems, one study compared the effect of ranking position on citation:

| Measurement method | Citation-rate gap between rank 1 and rank 5 |
|---|---|
| Reading observational data directly | 42.3 percentage points |
| Controlled replay (only position changed, everything else held constant) | 7.9 percentage points |
| Replay on held-out samples | 0 |

In observational data, higher-ranked content is already more relevant and more authoritative. Once these confounding factors are removed, the effect of "position itself" shrinks sharply.

**Principle: any study that skips a stage, or does not control for confounding factors, reaches conclusions that lean optimistic.**

## 2. How strong is the evidence: six research designs

Throughout the book, fixed phrases mark the strength of evidence. Readers can use the same standard to classify any study they see in other material.

### 2.1 Overview of the six designs

| Design | Phrase used in this book | What it can answer | What it cannot answer |
|---|---|---|---|
| Real-user experiments (randomised or quasi-experimental) | "Large-scale experiments with real users show …" | Whether real traffic and sessions changed after an intervention | Usually covers only one site or platform, so it is hard to generalise |
| Repeated tests on real engines | "Repeated tests on real AI search engines found …" | Whom commercial engines actually cite, and how unstable this is | Mostly observational, showing correlation rather than causation |
| Tests with supplied pages | "When the pages are supplied to the engine …" | How the engine uses a page once it has read it | Skips "whether the engine would find this page on its own" |
| Reproducible experimental pipelines | "In controlled experimental systems …" | How large the causal effect is in a complete but open-source pipeline | An open-source pipeline is not a commercial engine |
| Simulation / theory | "Simulations or theoretical analysis suggest that, in principle, … may" | Whether something is possible in principle | Cannot be written up as a real-world conclusion |
| Large models as judges (LLM-as-judge) | Not a separate grade but a **measurement tool**, which can appear in any of the designs above | Large-scale automatic scoring | The scores themselves may be unreliable |

### 2.2 Real-user experiments: closest to "does it work", but very rare

These studies look directly at real traffic or sessions. There are very few so far, and most are run by platforms or websites themselves. Two examples show their value and their traps:

**Example 1: using a same-domain control group to remove the "platform tailwind".** A website carried out a set of optimisations aimed at AI answer engines. Referral traffic from ChatGPT grew 5.7 times in raw terms over the observation period. But the **pages on the same site that were not optimised** also grew 3.5 times over the same period: this was growth in the platform's own user base. Using the untreated pages as a control and running an interrupted time series analysis, the level jump attributed to the optimisation was about 1.8 times (robustness checks ranged from 1.8 to 2.3 times). The placebo test reached only a "suggestive" level. In addition, the optimisations were bundled together, so it is impossible to tell which one worked; over the same period, organic clicks from traditional search actually fell by about 25%, and there was no evidence of "AI optimisation lifting traditional search".

Lesson: most of the raw multiple is the whole market rising, not something you did right. In the same study, a single-day spike reached 38.2 times; a figure like that is even less usable as a causal effect.

Example 2: check the numbers in self-run tests yourself. An image platform tested on itself adding annotations aligned with users' search intent to its content, and building collection pages and internal links. In a 4-week A/B test, the enabled group had 1.18 times the sessions of the control group, and the group with the related features switched off had 0.82 times. But other figures in the same report were inconsistent: the text claimed relevance was 19% higher, but the table figures did not match; it claimed a 20% traffic increase, but the breakdown table showed increases of only +0.83% to +1.83%; "generative search traffic 9.2 times" did not define the metric.

Lesson: even with the highest grade of design, check whether the figures in the text match the tables and whether the metrics are defined. That the authors are the platform itself is also a factor to consider.

### 2.3 Repeated tests on real engines: realistic, but mostly observational

These studies put questions to real products such as ChatGPT, Perplexity and Google AI Overviews, and record citations and recommendations. Their strength is that they reflect the real behaviour of commercial engines; their weakness is that most can only describe "who gets cited" and cannot prove "change this and you will be cited".

Pay attention to the word "repeated". Some studies run their queries only once, on a single date, which strictly speaking is just a snapshot. As the next section shows, the error of a snapshot can be large enough to invalidate the conclusion.

### 2.4 Tests with supplied pages and reproducible pipelines: each lacks one stage

- Tests with supplied pages: the URL is handed to a commercial engine by hand. The generation side is real; what is missing is the stage where "the engine finds it on its own".
- Reproducible pipelines: a complete pipeline is built from open-source retrievers, rerankers and generation models. Causal inference is clean, but the pipeline is not a commercial engine.

Both have value, but neither can be directly stated as "doing this works on ChatGPT".

### 2.5 Simulation and theory: they only show what is "possible"

Fixed context, simulated users and mathematical derivations all belong here. This is the largest category in the total body of research. These studies are suited to proposing hypotheses and explaining mechanisms, not to serving as a basis for practice. Whenever this book meets this kind of evidence, it writes "in principle, … may".

### 2.6 Large models as judges: the judge itself must be tested

Many studies use a large model to score answers: is this statement supported by the source? Is this content relevant? The problem is that the judge model itself makes mistakes.

In one audit based on repeated tests on real AI search engines, researchers used a large model to judge "whether a statement is supported by the source" and then compared it with human judgement: on 100 samples, the correlation coefficient between the two was only 0.62. The researchers themselves acknowledged that this limits the credibility of the core metric.

When reading a study that uses large-model scoring, ask three things:

1. Was it compared with human annotation? On how many samples? How high was the agreement?
2. Are the judge model and the model being judged from the same company, or even the same model?
3. Are the scoring criteria public? Does the conclusion still hold with a different judge model?

## 3. Why results change: instability is the norm, not the exception

A generative engine may answer differently every time. This is not a measurement error but a property of the system itself. Any conclusion based on a single result must be discounted first.

### 3.1 Asking the same question twice

Repeated tests on real AI search engines found:

- When the same query is run repeatedly, the median Jaccard similarity of the cited domain sets (the intersection of two results divided by their union) is about 0.29–0.31 for Gemini, about 0.33–0.40 for SearchGPT and about 0.50 for Perplexity. That is, the domains cited in two answers are often only one-third to one-half the same.
- To estimate a domain's "citation share" with a 95% confidence interval no wider than 5 percentage points, Gemini needs about 30–50 queries, Perplexity about 90–100, and SearchGPT more than 150.
- When the same prompt was repeated 6 times, the "top recommendation" changed for 4 of the 6 prompts.
- One vendor's production tracking data showed that whether a brand "is mentioned or not" is close to binary and fairly stable, but the flip rate of "sentiment" is about 6.7 times the flip rate of mentions. The study recommends running mentions at least 3 times, and using at least 10 prompts for sentiment, before results become stable (an observational recommendation).

The same phenomenon appears in controlled experimental systems: in single generations, about 15% of binary "cite or not" decisions flip, and about 45% of the effect variance comes from the randomness of decoding.

A large-scale audit of one social platform's own generative search found that on re-query, only about 41.8% retrieved exactly the same sources; when the retrieval results were the same, 89.6% of answers were nearly identical. **The variation comes almost entirely from retrieval, not from generation.**

### 3.2 Switching engines

The sources cited by different engines overlap very little:

| Comparison | Degree of overlap |
|---|---|
| Source domains across different AI engines | Jaccard about 0.10–0.25 (varies by study and domain) |
| AI engines vs Google organic results | Domain overlap ranges from about 4% to 25% (varies by engine and study) |
| Google AI Overviews vs Google organic results | About 68% overlap in the top 100 domains |
| App vs web version of the same Chinese-language platform | Domain-level Jaccard 0.19–0.51; URL-level only 0.014 on one platform |

So "it works on ChatGPT" cannot be extended to Perplexity; "it works on the web version" cannot even be extended to the same company's app.

### 3.3 Switching language or region

Repeated tests on real AI search engines found that query language is one of the largest sources of systematic variation:

- In one variance decomposition study, query language accounted for 26.5% of the variance in single answers, while the brand itself accounted for only 1.5%. The ranking reliability of a single answer was only about 0.01.
- When commercial questions were asked in the local language, global vendors appeared only 1 time out of 24; when asked in English in two non-English-speaking cities, local vendors appeared 0 times out of 12. Language determines which set of candidate vendors appears, and the exit IP determines which country's market.
- The same variance study estimated that adding 5 more repetitions after the first 5 reduces error variance by only 0.0003; adding 3 more languages instead reduces it by 0.00462, about 15 times as much. The measurement budget should go to **breadth** (languages, models, rephrasings), not to **depth** of repetition of the same prompt. (This result is limited to the sentiment metric, and confidence intervals have not yet been calculated.)

Measurements made in English cannot see the local competitors in non-English markets.

### 3.4 Switching dates

Platforms actively adjust "whether to show an AI answer". Repeated tests on real AI search engines found:

- Google AI Overviews expanded from 7 countries in 2024 to 229 countries in 2025; the appearance rate for US queries rose from 42% to 67%.
- The appearance rate for one category of health-topic queries rose from 1% to 66% (this subsample has only 74 queries).
- In one vendor's tracking data, with no intervention at all, visibility on ChatGPT fell by an average of 1.34% per run, and on Perplexity by 0.76%.

A "before vs after optimisation" comparison without a control group cannot tell whether a change came from your optimisation or from the platform itself changing.

### 3.5 Switching the wording

- In consumer products, adding "list your sources" after a question raised the average number of citations from 16.6 to 19.9, and the source composition changed by no more than 2.1 percentage points: a very small effect.
- But on the API side, the same wording raised the share of cases where the model called search from 12.1% to 88.4%. Prompt wording mainly changes "whether to search", not "whom it finds".
- Answers also follow the wording of the question: on debate-type questions, the share of one-sided answers ranged from about 49% to about 90% across engines.

So every measurement should disclose the full prompt text, the interface (product or API), the language, the region and the date.

### 3.6 "Cited" does not mean "used"

The metric itself also needs checking. Repeated tests on real AI search engines found:

- In Chinese-language generative engines, of the listed sources only 66% had content that made it into the body of the answer, 30% were substantively cited and 8% were deeply cited; about 39.3% were "silent citations".
- Another cross-system audit found that community discussion sources were listed as citations in AI Overviews, but noticeably less of their content was actually absorbed.
- Citing a source that really exists can also mislead: in a check of more than 760,000 citation pairs, 30.6% of the citations distorted the source content, and 27.1% of the sources were themselves unsuitable for answering the question.
- Researchers also point out that some conclusions that "long sources are overused" are partly produced by the scoring method: with a different calculation, the gap shrinks sharply.

When a report says "cited so many times", ask: was the source listed, used, or used correctly?

## 4. Debates and counterexamples

### 4.1 The gap between "40%" and later research

| Position | Basis |
|---|---|
| GEO rewriting can raise visibility substantially | Early fixed-context research, up to about 40% relative increase |
| This is not a general promise | A critical review of 45 studies points out: in one cross-method, cross-domain benchmark, only 3 of 54 method–domain combinations were significantly positive; in another multi-stage test, optimising only the body text actually lowered the top-20 appearance rate by about 9% and final citations by 6% |

The two are not necessarily contradictory: the former measures "already in the candidate set", while the latter also counts retrieval. But reading the former as "doing GEO gets you 40% more" is a misreading.

### 4.2 Does position matter?

Observational data shows a huge gap between rank 1 and rank 5; after controlled replay the gap shrinks to 7.9 percentage points, and it disappears on held-out samples. The same study also found that structured presentation (headings, lists, tables) increased the number of citations of the target source by 0.50 (statistically significant), but the total number of citations did not increase: it **redistributes** credit among equivalent sources rather than enlarging the total. And on the main metric, "whether cited", the effect is uncertain (+4.5 percentage points, with a confidence interval that crosses 0).

The same thing, viewed through different metrics, can lead to different conclusions.

### 4.3 How many repetitions are enough?

| View | Basis |
|---|---|
| Repeat more | The intervals of a single snapshot are so wide that many domain differences amount to noise; share estimates need tens to hundreds of queries |
| Do not repeat too much; widen breadth | Variance decomposition shows that repetitions after the 5th have very low marginal value, while adding languages and models pays off more |

The two can coexist: first repeat enough to stabilise single points, then shift the budget to breadth across languages, engines and wordings. But the latter has only been estimated for the sentiment metric, and has no confidence intervals yet.

### 4.4 Much measurement research comes from interested parties

Among the real-engine studies cited in this chapter, several were written by AI visibility vendors or by authors connected with GEO vendors. This does not mean the data is fake; some vendor studies are precisely the ones exposing the instability of measurement. But note:

- vendors have a motive to show that "visibility can be measured, is worth measuring and is worth optimising";
- vendor studies are mostly observational and lack intervention experiments;
- grouping methods (for example, tiers of brand awareness) are often defined by hand;
- samples may cover only a few topics and a few models.

Platforms' self-run tests (such as Example 2 in 2.2) have the same problem: the people running the experiment also benefit from the result.

## 5. How to read practitioners' claims

In this chapter's evidence base, no practitioner test passed screening for use as a case. This is itself a signal: many widely circulated figures (for example, "40%" or "3 times") cannot be traced back to an original test that can be checked. Below is a method for reading practitioners' claims, which every chapter of the book uses.

### 5.1 Distinguish four kinds of claim

| Type of claim | Features | How this book writes it | What it can be used for |
|---|---|---|---|
| Repeated, controlled tests | Before-and-after comparison, a control group, multiple repetitions, published method | "Practitioners' repeated, controlled tests found …" | Can serve as practical evidence, but still awaits independent verification |
| Ordinary test reports | Done by the person, with figures, but incomplete controls or repetition | "Practitioners report from their own tests …", stating that this is not independently verified | Indicates a direction |
| A single first-hand observation | A phenomenon seen once, a screenshot | "One practitioner observed …" | Only a lead or an example |
| Community consensus | Many people say so | "Practitioners widely believe …" | Shows "what people think", not proof |

### 5.2 Common traps

1. **First-hand ≠ reliable.** Someone who did it personally may still have done it only once. Section 3 of this chapter shows that the top recommendation in a single answer often changes.
2. **A single screenshot is not evidence.** A screenshot of "my brand appeared in a ChatGPT answer" proves only that one time, that language, that region, that day.
3. Before-and-after comparisons without a control. Platforms are changing themselves (3.4), and the whole market is rising (Example 1 in 2.2). Without a control group over the same period, growth cannot be credited to optimisation.
4. Consensus ≠ truth. Many people repeating the same claim may simply be relaying the same source. Each author should count as only one vote.
5. Numbers detached from conditions. For "40% increase" or "3 times", ask: relative or absolute? Was it measured on retrieval, citation or traffic? On which engine, in which language, over which period?
6. Conflicts of interest. Does the speaker sell tools or services, or have a commercial relationship with the brands mentioned? For such content, this book at most writes "A vendor claims …, but this has not been independently verified".

## 6. Cases

### Case 1: how a "5.7 times" became "about 1.8 times, and only suggestive"

- **What was done**: a website carried out a set of AI answer engine optimisations, including URL normalisation, mining demand from the 404 logs of AI crawlers, and switching to question-style headings with standalone summaries.
- **Platform**: ChatGPT referral traffic.
- What was observed: raw growth of 5.7 times; untreated pages on the same site grew 3.5 times over the same period; with the untreated pages as a control, the level effect was about 1.8–2.3 times; the placebo test was only suggestive. Organic clicks from traditional search fell by about 25% over the same period.
- Principle illustrated: the raw multiple mixes in platform growth; a same-domain control group is the key to separating the two; when several measures are bundled, no single practice can be credited.

### Case 2: the same widely circulated figure under different conditions

- **What was done**: with 5 candidate documents fixed, researchers applied various rewrites to web pages and had GPT-3.5 generate answers.
- **What was observed**: word share rose from 19.3 to 27.2, a relative increase of about 40%.
- Follow-up: under more complete conditions, most method–domain combinations showed no significant positive effect; changing only the body text may even harm retrieval.
- Principle illustrated: the number itself is not wrong; what is wrong is stripping it from its conditions.

### Case 3: testing in English cannot see local competitors

- **What was done**: on the ChatGPT web interface while logged out, researchers asked for business software recommendations in different languages and from different exit IPs, repeating each combination 6 times.
- **What was observed**: when asked in the local language, global vendors almost never appeared (1 time out of 24); when asked in English in non-English-speaking cities, local vendors did not appear at all (0 times out of 12). Asking in one country's language from another country returned vendors from the country matching that language.
- Limitations: a single model, only 6 runs per combination, and the authors are a visibility measurement vendor; in one control category there was no language effect.
- Principle illustrated: the measurement settings (language, region) themselves determine what you see.

## 7. What to do: a checklist for evaluating any GEO claim

### 7.1 Eight-step checklist

When you are handed a study, a vendor report or a practitioner's claim, ask in this order:

| Step | Question to ask | Warning sign | Basis for this step |
|---|---|---|---|
| 1. Research design | Is it a real-user experiment, repeated tests on real engines, supplied pages, an experimental pipeline, or a simulation? | Cannot say clearly, or presents simulation results as real effects | This book's grading standard |
| 2. Pipeline stage | Does it measure triggering, retrieval, citation, absorption or traffic? | Infers "traffic" from "cited" | Repeated tests on real engines; critical review |
| 3. Candidate set | Was the content found on its own, or fed directly to the model? | Fixed context, yet claims "easier for AI to find" | In controlled experimental systems |
| 4. Repetition and intervals | How many times was each condition repeated? Are there confidence intervals? | A single screenshot, a single-day snapshot, only averages reported | Repeated tests on real engines |
| 5. Measurement scope | Which engines, languages, regions, interfaces and dates? | Tests one engine and calls it "AI search" | Repeated tests on real engines |
| 6. Control group | Is there an untreated control over the same period? | Only a before-and-after comparison | Large-scale experiments with real users |
| 7. Scoring method | Who did the scoring? Was the large-model judge compared with humans? | Judge agreement not reported | Repeated tests on real engines |
| 8. Interests and consistency | Who are the authors? Do they sell related services? Do the figures in the text match the tables? | Authors are beneficiaries, figures do not match, metrics undefined | Counterexample in a large-scale experiment with real users |

### 7.2 When you run measurements yourself

- **Do**: repeat the same prompt several times at least, then widen to multiple languages, engines and wordings. (Repeated tests on real engines; "breadth first" has so far only been estimated for the sentiment metric)
- **Do**: record the full prompt text, interface (product / API), language, exit region and date. (Repeated tests on real engines)
- Do: report each engine separately; do not average results from different engines into a single "AI visibility". (Repeated tests on real engines)
- Do: when reporting citation share, attach an interval rather than a single percentage. (Repeated tests on real engines; authors are a vendor)
- Do: when evaluating the effect of optimisation, keep a batch of pages from the same site and of the same type unoptimised as a control. (Large-scale experiments with real users; a single website)
- Do: distinguish "listed as a citation", "content used" and "used correctly". (Repeated tests on real engines)

### 7.3 Do not do

- Do not use a screenshot to prove that "the optimisation worked" or that "A beats B".
- Do not treat percentages from fixed-context or simulation experiments as effects you can promise to clients.
- Do not treat a raw growth multiple as the effect of optimisation.
- Do not measure non-English markets in English only.
- Do not treat a practice as proven because "many people say so".

### 7.4 Already outdated readings

- Treating "GEO raises visibility by up to 40%" as a general effect: this figure applies only under the conditions "already among 5 candidate documents, generated by GPT-3.5, measuring word share".
- Believing that "good traditional search rankings mean good AI visibility": several studies show that the sources of AI engines and traditional search results overlap very little.
- Believing that one query can represent an engine's "view": when the same question is asked repeatedly, the cited sources are often only one-third to one-half the same.

## Key points

1. Every GEO conclusion comes with conditions: which stage of the pipeline was measured, in what system, in what language and on what date. Figures detached from their conditions get misread.
2. "GEO raises visibility by 40%" is a relative increase in word share with 5 fixed candidate documents and GPT-3.5. It does not mean easier to find, and it does not mean more traffic.
3. Experiments that skip retrieval, and observational data without control for confounding, both systematically overestimate effects.
4. Generative engines are inherently unstable: when the same question is asked again, the cited sources often overlap by only one-third to one-half; language, engine, interface, date and wording all change the results.
5. Single screenshots and single-day snapshots are not evidence; measurements need repetition, intervals and wider breadth.
6. Real-user experiments come closest to "does it work", but they are rare, and they still need a same-period control group to subtract platform growth.
7. Large-model judges, vendor studies and platforms' self-run tests all need checking: were they compared with humans? Who benefits? Are the figures consistent throughout?
8. Distinguish among practitioners' claims: "repeated, controlled tests", "single observations" and "community consensus"; consensus is not truth.
