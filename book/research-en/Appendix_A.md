# Appendix A: Major Disagreements Between Studies, and Between Research and Practice

## Questions this appendix answers

1. For which GEO practices have different studies reached opposite conclusions?
2. How strong is the evidence behind each of these opposing conclusions?
3. Why are they inconsistent: different engines, different times, different methods, or different things being measured?
4. Of the practices practitioners widely believe in, which are supported by research, which go further than the research, and which do practitioners themselves fail to agree on?
5. Where the evidence is inconsistent, what should be done in practice?

## How to read this appendix

Each disagreement is presented in the same format:

- **Question**: what the dispute is about.
- **Position one / Position two**: each side's claims and the strength of its evidence.
- Why they may be inconsistent: a comparison from four angles: engine, time, method and sample.
- What to do in practice: a safe approach under uncertainty.

Evidence-strength phrases match those used in the chapters:

| Phrase | Meaning | How far it can be pushed |
|---|---|---|
| Repeated tests on real AI search engines found | Commercial engines, repeated measurement | Fairly strong reference value for that engine at that point in time; mostly observational, not causation |
| When the pages are supplied to the engine | Sources supplied manually, real retrieval skipped | Speaks only to the "generation/citation" step |
| In controlled experimental systems | Reproducible retrieval-augmented generation (RAG) pipelines | Mechanism credible, but not a real engine |
| Simulations or theoretical analysis suggest that, in principle, … may | Fixed context, LLM simulation | Shows only that a mechanism is possible; must not be written up as a real-world conclusion |
| Practitioners widely believe | The view of most people in the community | An opinion, not proof |

Two points to keep in mind from the start:

- "Consensus" does not mean "correct". That most practitioners agree on something only shows it is the mainstream view in the trade.
- Research conclusions have a shelf life. The studies collected in this appendix range from late 2023 to October 2026. Engines went through several generations during that period.

## Part 1: Disagreements between studies

### A1: Does adding statistics, quotations and source citations to content help?

**Question**: the three GEO practices that were first spread widely were adding statistics (Statistics), adding quotations (Quotation) and citing sources (Cite Sources). Do they actually raise the chance of being cited by AI?

**Position one: they work.**

- In controlled experimental systems (a pipeline made of Google's top 5 results plus gpt-3.5-turbo), adding quotations, statistics and source citations raised Position-Adjusted Word Count (a measure of how much of the answer a source occupies and how early it appears) by about 30–40%, and a subjective impression metric by about 15–30%.
- In the same study, effects varied by domain; the combination of fluency plus statistics was more than 5.5% higher than any single strategy.
- Simulations or theoretical analysis suggest that, in principle, "page-level" evidence density may be what is at work: in a study that generated whole pages using 13 interpretable features, visibility on three models rose from 13.34%, 8.89% and 5.20% to 18.31%, 15.35% and 10.17% respectively; in the ablation analysis, statistics and source citations contributed most.

Position two: they do not work, and may even be harmful.

- Simulations or theoretical analysis suggest (fixed context, no real retriever, tested with gpt-4o-mini, claude-3-5-haiku, o3 and o4-mini): in only 3 of 54 scenarios was there a statistically significant improvement in citation rank, and none worked on question-answering tasks; "adding statistics" significantly lowered rank in 19 of 24 scenarios.
- When the pages are supplied to the engine (5 sources supplied manually, real retrieval skipped), a re-test covering 6 engine families plus commercial models (n=605) found that none of quotations, statistics or source citations moved citation share; replicated on three gpt-5.x engines (n=450), the results were likewise zero or nominally negative.
- The same re-test, measured with the original 2023 metric: quotations -0.33, statistics -0.28, source citations -0.79 percentage points, against the +42.6, +32.8 and +27.7 reported in 2023.
- It should be pointed out that the authors of this re-test themselves sell a content-scoring service.
- Repeated tests on real AI search engines found (three AI search engines, 56 artificially created data void topics, only one page published per topic, indexed naturally by search engines): on-page GEO writing (statistics, inline source citations, an opening summary, technical terminology and safety notes, added together) had no detectable effect on whether the page entered the answer (odds ratio 0.91), ruling out effects of twofold or more; the strongest factor was domain visibility, and new domains that were not indexed scored 0 on all three engines.
- Limitations: pages with and without GEO writing numbered 46 versus 10, so only large effects can be ruled out; the topics had no competing sources, and all content was fictional.

Why they may be inconsistent:

| Angle | Position one | Position two |
|---|---|---|
| Engine | gpt-3.5 in 2023 | New-generation models in 2025–2026 |
| Metric | Word-count visibility, subjective impression | Citation rank, citation share |
| Implementation | Whole-page rewriting, whole-page feature density | A statistics/quotation block appended to the page |
| System | Simplified RAG pipeline | Fixed context or manually supplied sources |

One further study falls between the two positions. When the pages are supplied to the engine (the researchers published product pages on a real website, then gave the URLs to three commercial AI search engines to read and rank), product pages that added statistics through a whole-page rewrite beat plain originals in average rank on all three AI search engines, but fell behind other whole-page rewriting methods; and none of the numbers in these 80 pages had any basis in the specifications, yet the engines did not rank them lower for it. This shows that "engines prefer numbers" and "the numbers are true" are two different things. Limitations: some of the researchers are authors of the best-performing method; reversing the URL order or rerunning changed the results.

The most reasonable reconciliation at present has three parts:

1. What works is genuine evidence density across the whole page, not an appended block. The same whole-page optimization study also found that 9 token-level GEO rewrites (including keyword stuffing) fell below the unrewritten baseline on all three engines.
2. Effects expire as engines are updated. The levers measured in 2023 can no longer be measured when re-tested on new-generation engines.
3. The closer the conditions are to the real world and the stronger the evidence, the weaker the evidence that writing techniques help. Under real retrieval conditions, on-page writing had no detectable effect, and whether the page is indexed and whether the domain is visible matter more; when the pages are supplied to the engine, adding statistics beat only plain originals, and AI search does not check numbers.

Practitioner view: Practitioners widely believe that "only content with views worth citing or useful information gets cited". This is consistent with the "genuine evidence density" reconciliation, but it is an opinion, not a measurement.

What to do in practice:

- Put real, verifiable data and sources where the argument genuinely needs them, rather than adding a "data summary" block at the end.
- Do not treat the 2023 improvement figures as today's expectations.
- Any claim of the form "adding element X raises results by X%" should be re-tested on the engines you care about with a fixed query set.
- First confirm that the page is indexed and that its domain can be found; then worry about the writing.
- Do not write unsupported numbers. AI search does not check them; invented numbers mislead readers and are a reputational risk for the writer.

### A2: Does structure (headings, Schema, lists) help?

**Question**: does making a page structured (title, meta, headings, Schema, lists, tables) raise the chance of being cited?

**Position one: it helps at the retrieval stage.**

- In controlled experimental systems (a corpus of 171,000 real web pages, BM25 retrieval, a reranking model, GPT-5-mini generation), changing only structural fields (title, meta, heading, schema) raised the top-20 hit rate at the retrieval stage from 0.58 to 0.71 (about +22%).
- But in the same experiment, the reranking stage still fell from 1.00 to 0.83 (about -17%). Structure helps with "being pulled out", but does not guarantee "being placed into the context".
- In controlled experimental systems (an agent pipeline plus counterfactual replay of frozen records), structured presentation (headings, lists, tables) increased the number of citations of the target source by about 0.50, but the total number of citations did not increase; the primary endpoint, "whether cited", was +4.5 percentage points, with a confidence interval crossing zero, so it is uncertain.

Position two: formatting has no effect.

- Simulations or theoretical analysis suggest (a two-source controlled test with 6 models, 18 factors and 252,000 trials) that the odds ratio for "structured vs dense text" lies between 0.79 and 1.68, with no consistent effect; changing only headings, lists or information aggregation had no clear effect.
- In the same study, what actually worked were gatekeeping factors: whether the topic is relevant, list position, whether the price is stated, and whether the timestamp is more recent.

Why they may be inconsistent:

- Different stages measured. The positive effects seen in Position one concentrate on retrieval and extraction; Position two measures directly at the step of "which of two documents already in the context gets cited", bypassing retrieval.
- Different things measured. "Citations being redistributed" and "the probability of being cited rising" are two different things. Structure may shift credit between equivalent sources, rather than give you one more chance of being selected.
- The evidence for both positions comes from experimental systems or simulations; there are no direct tests on real engines.

What to do in practice:

- Treat structure as a condition for entering the candidate pool and for ease of extraction, not as a citation lever.
- Put the core entities and key numbers into structural fields such as title and heading; in experimental systems, this was the change most favorable to retrieval.
- Do not expect "turning paragraphs into lists" to bring citation growth by itself.
- Prioritize the gatekeeping factors from Position two: topic alignment, stating prices and specifications, and keeping dates recent.

### A3: Are off-site mentions (a brand being mentioned on other websites) a strong signal?

**Question**: the more a brand is mentioned on third-party websites, the more easily it appears in AI answers?

**Position one: cross-source co-occurrence is a strong signal.**

- Repeated tests on real AI search engines found (4 Chinese-language generative search engines, 8 Web and App interfaces in total, 614 queries, 3 runs each, 160,860 citations in total): when a brand appeared in only 1 citation, the rate of entering the answer was 2.1%; when it appeared in 11 or more citations, the rate was 59.9%.
- In the same study, the composite traditional SEO quality score had an importance of only 4.52% in the prediction model.
- This is association, not an interventional experiment.

Position two: once site readability is controlled for, off-site mentions have no independent effect.

- Repeated tests on real AI search engines found (4 real agent frameworks, 1,056 companies, 37,927 agent journeys, matched on prominence and the model's prior knowledge): after controlling for how readable a site is to AI agents (AX), two metrics measuring off-site mentions and discoverability had no significant partial correlation with "whether the answer lands on the company's own content", "whether the company is recommended" or "cost"; AX itself had partial correlations of +0.62, +0.41 and -0.27 respectively.
- For highly readable sites, 78% of answers came from their own pages, against 58% for the comparison group; explicit recommendation rates were 20% vs 11%.
- It should be pointed out that this is a matched observational study using the authors' own scorer, and the authors themselves sell related services.

Why they may be inconsistent:

| Angle | Position one | Position two |
|---|---|---|
| Stage examined | Whether the brand **surfaces** in the answer | Whose content is used when the agent, having found the brand, **looks deeper** |
| Engine and market | Chinese-language search engines | Mainly English-language agent frameworks |
| Outcome metric | Whether it enters the answer | Whether the answer comes from the company's own pages; whether it is explicitly recommended |

The most reasonable reconciliation at present: the two may act at different stages. Off-site co-occurrence affects "whether you come to mind"; site readability affects "once you come to mind, whose content the answer is built from".

Practitioner view: Practitioners widely believe that off-site mentions are very important, for example "consistent mentions of a brand on external platforms such as community discussions and review sites matter more than your own site's ranking", "a core explanation that appears repeatedly across several platforms is more easily adopted than a single high-quality page", and "consistent descriptions of a brand across platforms are key to AI understanding and citing it". These views point in the same direction as Position one but go further: the research shows only association, and one study shows no independent effect at a certain stage once controls are applied. Claims such as "GEO is 70% distribution and 30% content" are rules of thumb with no research support.

What to do in practice:

- Do both, but be clear about which part each governs: genuine, consistent off-site mentions govern "coming to mind"; your own site being smoothly readable by agents governs "once you come to mind, the answer tells your version".
- Off-site mentions should aim for authenticity and consistency, not manipulated volume; multi-source co-occurrence may be useful precisely because it reflects genuine evidence from multiple sources.
- Do not treat off-site placement as a shortcut that can substitute for your own site's readability.

### A4: How much does ranking near the top (position) matter?

**Question**: how much does a document's position in the retrieval results or in the context affect whether it is cited or selected?

**Position one: in a fixed context, position has a large effect.**

- Simulations or theoretical analysis suggest that the gain from placing a document in position 1 in the context (retail domain +2.77) is far larger than that from any kind of GEO content rewrite.
- The same study also shows that as more and more people adopt the same rewriting method, each adopter's gain diminishes toward 0, a zero-sum competition.

Position two: in agents and controlled replays, position has a weak effect.

- Simulations or theoretical analysis suggest (a self-built hotel search environment, shopping agents on 8 models): agents examine 1.63–5.83 options per session (humans 1.12); the coefficient of position on "whether examined" is about 1/4 to 1/10 of that for humans, and it does not decrease monotonically, bottoming out at positions 68–74 and then rising again.
- In the same study, at the highest reasoning effort, position had no significant effect on the final choice; one hotel that was not fully dominated by other options on its attributes took 78.2% of all bookings.
- In controlled experimental systems, the gap in citation rate between position 1 and position 5 in observational data was 42.3 percentage points; after controlled replay it was only +7.9 percentage points; in the held-out sample it was 0.

Additional evidence for position one (real AI search, fixed candidate list):

- When the pages are supplied to the engine (three commercial AI search engines read 6 product-page URLs supplied by the researchers, with the content completely unchanged), merely reversing the URL order changed the first-place rate of the same rewrite on one AI search engine from 73.8% to 93.8%, and the first place changed for about a quarter of brands; on another AI search engine, the method that came first most often switched outright. This is still "choosing from a given list", but the subjects are real commercial AI search engines, not simulated agents.

Why they may be inconsistent:

- Method. In observational data, documents ranked near the top tend to be more relevant and better in their own right; once that is controlled for, the effect of position itself shrinks considerably.
- System type. A single generation from a fixed context behaves differently from an agent that examines and compares multiple times.
- Model and settings. The size of position bias changes with the model and the reasoning effort.

The most reasonable reconciliation at present: observational data overestimate the position effect; but in a fixed candidate list, even for real commercial AI search engines, order can still clearly change who comes first (when the pages are supplied to the engine, the gap can reach 20 percentage points).

What to do in practice:

- "Getting into the candidate pool" still matters; if you cannot get in, nothing else is possible.
- Once in the candidate pool, rather than chasing marginal rank, make sure your content is not fully dominated by competitors on visible attributes (ratings, price, specifications, topic fit).
- Do not judge optimization results by a single observational metric such as "what position am I in".

### A5: Does llms.txt help?

**Question**: does providing an llms.txt file in the website's root directory raise AI visibility?

**Position one: unrelated to outcomes.**

- Repeated tests on real AI search engines found (5 commercial engines with search, 5,460 answers) that 16.9% (177/1,047) of cited websites had llms.txt, and the correlation between technical markers such as llms.txt and answer accuracy was about -0.04, essentially none.
- Limitations: this study measured answer accuracy, not whether a given website can be cited; it is also observational data.

Position two: relevant as part of a "site readability package".

- Repeated tests on real AI search engines found (real agents, real company websites) that companies with higher site readability scores had more of their answers drawn from their own pages and a higher rate of explicit recommendation. The readability score includes: content that does not depend on JavaScript, structured data, llms.txt or a Markdown fallback version, and bot controls that do not block agents.
- Limitations: this is a package score that does not break out individual elements, so it cannot show that llms.txt works on its own.

Why they may be inconsistent: the two do not in fact conflict directly. One measures the association of llms.txt alone with accuracy; the other measures the association of a package that includes llms.txt with landing rate. There is currently no evidence that llms.txt works on its own.

Practitioner view: Practitioners widely believe that llms.txt does not help AI visibility or citation, and also widely believe that most models never look for this file at all. This broadly matches the research. Practitioners also widely believe that two other things are more substantive: AI crawlers are often blocked at the CDN or WAF (web application firewall) layer, by default or unintentionally, which makes allowing them in robots.txt useless; and most AI crawlers do not execute JavaScript, so client-side rendered content is invisible to them.

What to do in practice:

- llms.txt is low-cost and can be done, but do not make it a priority, and do not expect it to bring change on its own.
- First check the more basic parts of the readability package: whether core content is in the initial HTML, and whether the CDN/WAF is blocking AI crawlers.

## Part 2: Gaps between practitioner consensus and research

This part covers only two kinds of situation: views on which practitioners have clearly reached consensus, and views on which practitioners are clearly split. "Practitioners widely believe" below describes views in the trade, not proof.

### B1: "Clear, direct, answer-first content is more easily cited"

**Practitioners widely believe**: content that provides clear, direct answers and is structured is more easily extracted and cited by AI; the answer should be placed at the start of the page; AI prefers compact paragraphs that can stand alone as answers over long, comprehensive pages. This is one of the views with the most supporters across the whole practitioner community, with almost no one opposed.

What the research says:

- Partly supported: in controlled experimental systems, answer-first placement and topical consistency help at the reranking stage; optimizing only the body text while greatly expanding it causes documents to fall behind at retrieval and reranking.
- Partly not supported: simulations or theoretical analysis suggest that formatting itself (structured vs dense) has no consistent effect; in controlled experimental systems, structured presentation redistributed citation credit between equivalent sources but did not reliably raise the citation rate.

**Where the gap lies**: practitioners bundle "answer first" (a content matter) and "lists and tables" (a formatting matter) into one thing. Research shows the former has mechanistic support and the latter has limited effect. In addition, specific thresholds such as "the first 100 to 150 words" are practitioner experience; the research does not give this number.

What to do in practice: prioritize answer-first placement and topical focus at the content level; treat formatting changes as supporting work, not as the main lever.

### B2: "SEO is the foundation of GEO" and "good Google rankings do not guarantee AI visibility"

**Practitioners widely believe**: AEO (answer engine optimization)/GEO is an extension of SEO rather than a replacement, and a solid SEO foundation is the main route to AI visibility. But this view has a considerable number of opponents; it is not one-sided. At the same time, practitioners also widely believe that good Google rankings do not guarantee AI visibility, a point on which almost no one disagrees.

What the research says:

- Supporting the "foundation" side: simulations or theoretical analysis suggest that context position (equivalent to "being retrieved and ranked near the top", which traditional SEO determines) has a far larger effect than content rewriting; in controlled experimental systems, documents that optimize only their body text fall behind at the retrieval and reranking stages.
- Supporting the "no guarantee" side: repeated tests on real AI search engines found that the composite traditional SEO quality score has low importance in predicting whether a brand enters the answer; in another study with real agents, two metrics measuring traditional AEO performance had no independent effect after controlling for site readability.

**Where the gap lies**: the two practitioner views can in fact both hold. SEO governs "entering the candidate pool", while the subsequent reranking, extraction, generation and agent deep-dive each have different determining factors. Proportional claims such as "GEO is 90% SEO" have no research support.

What to do in practice: keep up SEO fundamentals, especially being crawlable, indexable and retrieved for relevant queries; but do not use Google rankings as a direct stand-in for AI visibility. Measure the two separately.

### B3: Schema markup

**Practitioners widely believe**: Schema markup on its own has limited effect, and is ineffective especially when added carelessly or incompletely. The stronger claim that "Schema does nothing at all for AI citation" also has supporters, but has not formed a stable consensus.

**What the research says**: in controlled experimental systems, schema changed together with title, meta and heading had a positive effect at the retrieval stage but did not help reranking. In the real-agent study, structured data was part of the site readability package and was not broken out separately. No study has yet tested the effect of Schema on citation in isolation.

Where the gap lies: the practitioners' "limited effect" is close in direction to the research's "effective only at the retrieval stage"; "no use at all" goes beyond the existing evidence.

What to do in practice: Schema should be complete, accurate and consistent with the page content; treat it as supporting information that helps systems understand the page, not as a citation switch.

### B4: Cited ≠ recommended (research and practice point the same way)

**Practitioners widely believe**: a citation by a generative engine does not mean the brand will be recommended or mentioned; being recommended matters more than being cited. This is one of the views with the most supporters and no opponents.

**What the research says**: repeated tests on real AI search engines found that of the listed sources, 66% made it into the body text, 30% were substantively cited, and only 8% were cited in depth; of the brands appearing in the citation pool, only 8.3% ultimately made it into the answer. The real-agent study also measured "explicit recommendation rate" separately from "the answer landing on the company's own content".

This item is not a disagreement but an example of practitioner experience running ahead and research quantifying it afterwards. It is listed here as a reminder: any performance figure that reports only "number of citations" should be questioned on whether it distinguishes citation, mention and recommendation.

### B5: Single measurements are unreliable (research and practice point the same way, but the thresholds are rules of thumb)

**Practitioners widely believe**: the outputs of generative AI are unstable, and results from a single run or a few runs are unreliable; a fixed, representative prompt set should be built, run repeatedly and tracked over time. One practitioner proposed "at least 10 repetitions, sustained over several weeks".

**What the research says**: in controlled experimental systems, the binary "cite or not" decision flips 15% of the time in a single generation, and 45% of the variance in effects comes from decoding itself. When the pages are supplied to the engine, published GEO levers expire as engines are updated. Repeated tests on real AI search engines found that the sources from the App and Web interfaces of the same platform overlap at the domain level by only 0.19–0.51 (Jaccard coefficient).

Where the gap lies: the direction is consistent. But "10 times" and "several weeks" are practitioner rules of thumb; the research does not derive these numbers.

What to do in practice: use a fixed query set, run it multiple times, and record results separately by engine and by interface; re-test after every engine update; do not judge whether a change worked from a single screenshot.

### B6: Issues on which practitioners are clearly split

On the following issues, practitioners include many supporters and many opponents, and the studies collected in this appendix did not measure them directly. Only the split itself is presented here.

| Issue | One side's view | The other side's view | Research status |
|---|---|---|---|
| Traffic from AI | Some practitioners believe ChatGPT brings websites significant traffic | Just as many practitioners disagree; there is also a widely held view that AI referral traffic is still small compared with organic search | Not directly measured by the studies collected in this appendix |
| Accuracy of tracking tools | Widely believed that most AI visibility tools are not reliable enough and lean toward vanity metrics | Also widely believed that tracking is feasible and there are several methods; the stronger claim that "tools cannot provide accurate data at all" has a considerable number of opponents | Research shows only that the outputs themselves are unstable (see B5) |
| Whether GEO is just old SEO | Quite a few practitioners believe it is just the practices of fifteen years ago under a new name | Quite a few also disagree | Research shows that different pipeline stages reward different features (see B2) |

**What to do in practice**:

- Answer questions about traffic and revenue with your own data. Practitioners widely believe that directly asking customers how they heard about you (forms, conversations) is the most effective way to attribute AI recommendations.
- When choosing a tracking tool or service, practitioners widely believe you should require the provider to show a verifiable measurement method and explain how it relates to business outcomes.
- Look at trends and relative changes in tracking figures, not the absolute value of a single score; do not compare numbers from different tools directly.

## Summary table

| Issue | Research position one | Research position two | Practitioner view | Safest current understanding |
|---|---|---|---|---|
| Statistics, quotations, sources | Effective (experimental systems, simulation) | Ineffective or harmful (simulation, pages supplied); no detectable effect under real retrieval (real engines) | Only content worth citing gets cited | Genuine whole-page evidence density may help; appended blocks do not; effects expire; being indexed and domain visibility matter more than writing; engines do not check numbers |
| Structure/Schema | Helps at the retrieval stage (experimental system) | Formatting has no effect (simulation) | Schema on its own has limited effect | Governs retrieval and extraction; not a citation lever |
| Off-site mentions | Co-occurrence is a strong signal (real engines, association) | No independent effect once readability is controlled (real agents, matched observation) | Very important | May act at different stages |
| Position | Very strong in a fixed context (simulation); can still change who comes first in a fixed candidate list (pages supplied) | Very weak in agents and controlled replay (simulation, experimental system) | (none) | Observational data overestimate the position effect; in a fixed candidate list, order can still change who comes first |
| llms.txt | Unrelated (real engines, association) | Part of a package (real agents) | No use | No evidence that it works on its own |
| Answer first | Helps reranking (experimental system) | Formatting itself is ineffective (simulation) | Very important | Content-level answer-first has a mechanism; formatting is secondary |
| SEO and GEO | Retrieval position has a large effect (simulation) | Traditional quality score has low predictive power (real engines, association) | SEO is the foundation, but rankings do not guarantee visibility | SEO governs entry into the pool; other factors decide afterwards |

## Common practices under uncertainty

1. **Think in stages.** Most "seemingly contradictory" conclusions measure different stages of the pipeline. First ask: "Does this conclusion govern retrieval, reranking, generation, or agent deep-dives?"
2. **Distinguish types of study.** Conclusions from simulations and fixed contexts show only what is mechanistically possible; do not treat them as laws of real engines.
3. Re-test for yourself. Once an engine updates, old conclusions may stop holding. Test any practice on your own query set and on the engines and interfaces you care about before scaling it up.
4. Avoid zero-sum and expired tactics. The gains from content-rewriting tricks that everyone uses get diluted; do not keep relying on practices that re-tests on new-generation engines have refuted.
5. Do first what neither side opposes. Content that can be crawled and rendered, answer-first placement, topical focus, real verifiable data, and genuine, consistent off-site mentions: none of these has been refuted by any of the studies or by practitioners.

## Key points

1. The early positive results for "adding statistics, quotations and sources" can no longer be measured when re-tested on new-generation engines with an appended-block implementation; what is more likely to work is genuine whole-page evidence density. Under real retrieval conditions, on-page writing had no detectable effect, and whether the page is indexed and whether the domain is visible matter more; AI search also does not check numbers.
2. Structure mainly helps retrieval and extraction; changing formatting alone did not reliably raise citation rates in multiple tests.
3. The evidence on off-site co-occurrence and site readability looks contradictory, but more likely reflects two different stages: "coming to mind" and "whose content is used once you come to mind".
4. Observational data clearly overestimate the position effect; after controlled replay, the effect of position shrinks considerably. But when the pages are supplied to the engine, real AI search facing a fixed candidate list can still have its first place clearly changed by order.
5. There is currently no evidence that llms.txt works on its own, and practitioner views broadly match the research.
6. The strongest practitioner consensus views (answer first, cited is not the same as recommended, single measurements are unreliable) mostly have partial research support, but the specific threshold numbers are rules of thumb, not research conclusions.
7. Traffic from AI and the accuracy of tracking tools are issues on which practitioners remain clearly split and that research has not directly measured; judge them with your own data.
