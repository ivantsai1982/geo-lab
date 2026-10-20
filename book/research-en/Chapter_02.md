# Chapter 2: Triggering: When Does AI Search?

The first gate of the AI search pipeline is not "ranking" but "whether to search at all".

```
Triggering → Accessibility → Retrieval → Selection/ranking → Citation → Absorption → User behavior
 ▲
This chapter
```

If a question does not trigger a web search, none of the later stages happen. The answer then comes only from what the model memorised during training. However well your page is written, it will not be read.

## Questions this chapter answers

1. When AI products answer questions, what share of the time do they actually search the web?
2. Who decides whether to search: the product, the model, or the way the user phrases the question?
3. Which query forms are more likely to trigger a search? Which almost never do?
4. If a user asks the AI to "list sources" in the prompt, does that make it search?
5. For practitioners, how can you tell whether your target queries are a "search battle" or a "memory battle"?

## 1. Core principles

### Principle 2.1: Whether to search is a separate decision stage

When AI answers a question, it can take one of two paths:

```
User question
   │
   ▼
[Triggering decision]──no search──▶ Answers from parametric knowledge only (what it memorised in training) ──▶ Usually no citations at all
   │
  search
   ▼
Query rewriting → Retrieve web pages → Filter → Generate the answer with citations
```

This decision is not fixed. Three things jointly determine it:

- **Product and platform settings**: some products search every time; others let the model decide.
- **The model's own tendency**: for the same question, different models differ greatly in their willingness to search.
- The form and topic of the query: questions, long queries and questions that need fresh information are more likely to trigger a search.

Researchers describe this structure, in which the product's outer instructions and the model itself jointly decide whether to search, as a joint decision between the harness and the model.

### Principle 2.2: Trigger rates vary enormously

Trigger rates cannot be summed up by a single "industry average". They change sharply with the product, the model and the query sample.

**Differences between conversational AI products:**

| Condition | Observed result |
|---|---|
| Same set of 1,000 prompts, GPT-5.3-chat | Only 14% invoked search |
| Same set of 1,000 prompts, Claude Sonnet 4.6 | 83% invoked search |
| ChatGPT in 45 days of repeated measurement | 57.8% of runs produced no citations at all |
| ChatGPT in another study | 75.8% of queries did not trigger search |

In the last study, the researchers further broke down the reasons for "no search": 69.4% were intent misjudgements (the model decided no search was needed) and 30.6% were safety refusals.

**Trigger rates of Google AI Overviews (hereafter AIO):**

| Query sample | Overall trigger rate | Questions | Non-questions |
|---|---|---|---|
| 55,393 popular searches | 13.7% | 64.7% | 9.5% |
| Public sample of real search logs | 51.5% | 89.9% | 51.9% |
| Real browsing records of 900 US adults | about 18% | n/a | n/a |

The three figures differ by nearly a factor of four. The main reason is the different samples: popular searches contain a high share of navigational and short-keyword queries, while real logs contain a high share of long queries and questions. So the question "what is the AIO trigger rate?" is meaningless in itself. The question to ask is "what is the trigger rate for my type of query?"

### Principle 2.3: Query form is the most stable trigger signal

One pattern holds across all studies: **questions and long queries are more likely to trigger AI answers.**

- In the sample of popular searches, questions triggered AIO nearly 7 times as often as non-questions (64.7% vs 9.5%).
- In the sample of real logs, interrogative sentences had a trigger rate of 89.9%.
- In real browsing records, long queries, queries starting with a question word, and queries containing both a noun and a verb were more likely to trigger.
- By intent: AI answers appeared for about 60% of questions, about 37% of statements and about 12% of navigational queries.

Navigational queries (for example, searching directly for a brand's official website) almost never trigger. The reason is intuitive: the user wants a URL, not an explanation.

### Principle 2.4: Platforms actively adjust triggering by topic and region

Triggering is not only the algorithm's "judgement" of a query. It is also platform "policy".

- AIO coverage expanded from 7 countries in 2024 to 229 countries in 2025.
- The AIO appearance rate for US queries rose from 42% to 67%.
- The AIO appearance rate for COVID-related queries went from 1% in 2024 to 66% in 2025 (this observation is based on only 74 queries).

The implication: visibility on a topic can change abruptly because of a single platform policy change, regardless of what you did.

### Principle 2.5: Prompt wording can change triggering, but mainly on the API

On the API, prompt wording has a very large effect on triggering; in consumer products, the effect is small.

| Condition | Without "List your sources" | With it |
|---|---|---|
| API (model decides whether to search) | Search invocation rate 12.1% | 88.4% |
| API citations per response | 0.60 | 7.05 |
| Consumer product (free, not logged in) | Average citations 16.6 | 19.9 |

In the consumer product, the composition of cited sources changed by no more than 2.1 percentage points.

This has two implications for practitioners:

1. When you use the API to monitor visibility, the way the prompt is written can seriously distort the results.
2. Most real users do not add instructions like this, so do not use "results with the instruction added" to estimate real exposure.

### Principle 2.6: More searching does not mean better answers

Triggering a search only means the answer "has a chance" to use web content. It does not mean the web content will be cited or used correctly.

- Studies found that 14–53% of claims in answers were supported by search results but carried no citation (invisible use).
- A further 15–20% or more of claims could not be matched to any search result.
- Models that search more often showed only mixed effects on answer quality, not across-the-board improvement.

So "triggering", the concern of this chapter, is a necessary condition for being seen, not a sufficient one. Later chapters deal with the stages after the search.

## 2. How strong is the evidence

| Conclusion | Type of evidence | Strength assessment |
|---|---|---|
| Trigger rates differ enormously between models (14% vs 83%) | Repeated tests on real AI search engines found; plus real conversation logs from 613 users and 171,264 conversations | Strong. But only specific model versions were compared; the figures will change after version updates |
| ChatGPT does not trigger search a large share of the time | Two independent studies with repeated measurement on real commercial engines | Strong. The two studies use different definitions ("zero citations" vs "search not triggered"), so the figures cannot be directly added or compared |
| Questions and long queries trigger AIO more easily | Three independent studies, with samples ranging from popular searches to real logs to real browsing records | Strong. The direction is consistent; this is the most reliable conclusion in this chapter |
| Platforms adjust triggering strategy by topic | Repeated tests on real AI search engines found, with crawls repeated across years | Medium. The COVID case has a sample of only 74 queries |
| Prompt wording changes API triggering | Repeated tests on real AI search engines, with API and product compared | Medium to strong. Tested only on mental health topics; other topics not verified |

Limits of applicability:

- Most of the data come from specific model versions in 2025–2026. Triggering strategy is a product decision and changes with version updates.
- Research on Google AIO focuses mainly on US or English-language queries.
- Most triggering research on conversational AI uses the API or donated conversation logs, which may differ from real use when logged in, with memory and personalisation.

## 3. Debates and counterexamples

### Debate 1: Do comparison and purchase questions trigger search or not?

This is the most obvious contradiction in this chapter. Tests by different practitioners reached opposite conclusions.

| View | Basis | Test conditions |
|---|---|---|
| **Yes, they trigger almost every time** | Practitioners' repeated, controlled tests found: across about 2,000 buyer-intent questions about software and developer tools, the share with at least one citation within a month was 95% for ChatGPT, 99% for AIO and 100% for Perplexity | Narrow question set: B2B software "best X", "X vs Y", "tools for doing Z" |
| **No, the more specific, the less search** | Practitioners report from their own tests: on ChatGPT, 76 of 80 "Brand A vs Brand B" questions involved no search at all; 106 of 120 situational questions such as "I have a certain condition, which mattress should I buy" involved no search; while about half of broad category questions such as "best camera backpack for hiking" triggered search | Consumer goods; API with the web search tool enabled, the model deciding by itself |

Each side has a basis, and for now neither can be declared correct. Possible explanations include:

- **Different categories**: software tools change quickly, so the model may judge that fresh information is needed; for brand comparisons of consumer goods, the model may consider its training knowledge sufficient.
- **Different question shapes**: "X vs Y" names two brands directly, so the model may think it already knows the answer; "best X" requires a list and needs more outside information.
- Different measurement methods: the former uses "whether there is a citation" as the indicator, the latter uses "whether search was invoked" as reported by the API.

The view put forward by the first practitioner deserves attention: the trigger rate is mainly a property of the question, not of the engine. A prompt mix that includes definitional and how-to questions will naturally lower an engine's "average trigger rate".

### Debate 2: Shopping-card triggering is not the same as search triggering

One practitioner reports that among more than 10,000 shopping queries, 93% of purchase-intent queries triggered ChatGPT's product carousel cards, compared with only 15% of comparison queries. One practitioner observed a similar pattern: carousels appeared for 93% of purchase-execution queries and only 2.8% of post-purchase queries.

These figures cannot be used to answer "does it search or not". The product carousel is a different answer format, and reportedly depends mainly on structured product feeds rather than web content. The practitioner who put forward these figures works in a related business, and the figures are not independently verified.

### Debate 3: Are research questions answered from training knowledge alone?

One practitioner observed: research questions are answered from training data without triggering search, so they have almost nothing to do with Google rankings; only purchase questions ("best X in a place", "top providers for doing Z") trigger search, and there the correlation with ranking is clearly higher.

This is consistent with the view in Debate 1 that "definitional and how-to questions are answered directly from the weights", but it is a single observation and can serve only as a lead.

### Debate 4: Can complex prompts make AI do "deep research"?

One practitioner observed: however the question is asked, complex prompts do not make the model start agentic deep search. On the surface this contradicts Principle 2.5 (wording can greatly change API triggering). A possible explanation: wording can change "whether to search" but not necessarily "how deeply to search". No research has tested this directly so far.

## 4. Cases

### Case 1: The same brand lives in two worlds, with search on and with search off

- **What was done**: a services company found that when people asked ChatGPT "who can do X", it was mentioned only about 6% of the time. It first audited its own website: all crawlers received normal responses and there were no technical problems, yet changing its pages brought no change at all.
- **Diagnostic method**: another practitioner suggested a "search on / search off" comparison test. This practitioner reports having scored about 180 companies this way; the companies named were usually not those with the cleanest websites, but those that often appeared in "X vs Y" articles written by others.
- What was observed: one practitioner who followed this approach was cited about 16% of the time with search on, and 0 with search off.
- Implication: this company's visibility comes entirely from real-time retrieval. At the level of training memory, it does not currently exist. So it makes sense that page changes had no effect: answers to this kind of question come from third-party comparison and roundup content, not from the company's own pages.

```
Search off → Mentioned?
   ├─ Yes → Already in training memory, a long-term asset
   └─ No → Search on → Mentioned?
              ├─ Yes → Relies on real-time retrieval; leverage lies in the third-party content that gets retrieved
              └─ No → Neither path reaches you; deal with accessibility and retrieval first (Chapters 3–4)
```

### Case 2: A local business performs completely differently across AI products

One practitioner observed: the same local business had 0% visibility when the model answered from internal knowledge only. After web search was turned on, some AI products began recommending it consistently, while others still did not mention it at all.

This shows that "AI visibility" is not a single number. You first need to understand each product's triggering behaviour before optimisation makes sense.

### Case 3: A brand-new entity can be cited only through real-time retrieval

One practitioner observed: a brand-new entity that appeared after the training cutoff dates of all models could be cited in AI answers. Server logs showed that training crawlers were blocked throughout the test period, while real-time fetchers obtained the content normally.

This is a clean control: training memory cannot be the source, so the citations can only come from retrieval at query time. For new brands and new products, triggering search is the only route to exposure.

### Case 4: Monitoring visibility through the API may measure something else

- **What was done**: a practitioner used the API to track weekly visibility across several AI products, about 285 answers per model per week, for four weeks.
- **What was observed**: when tool choice was set to "auto", the model answered most product-recommendation questions directly from its priors, with no search at all. The "web-connected" and "not connected" result sets almost merged into one, and had to be separated by forcing search.
- Another finding: week-to-week fluctuation was larger for web-connected results than for non-connected ones, estimated at about 3 times. But with only 4 weeks of data, the confidence interval for this ratio runs roughly from 1 to 11 times, so uncertainty is high. Within one week, visibility for the same set of questions rose from 0.226 to 0.285.
- A similar report from another group of practitioners: across collection from four engines, ChatGPT in auto mode gave zero citations on all pilot questions and answered in about 4 seconds; the other engines searched in real time and took 15 to 40 seconds. (This practitioner states that they provide AI visibility services, and their ChatGPT sample was only 18 of 280 questions, so it should not be relied on heavily.)

## 5. What to do

### Recommended practices

| Practice | Strength of evidence |
|---|---|
| **Classify target queries first**: group the queries you want to track by form (question / non-question, long / short) and intent (definition, how-to, category comparison, brand comparison, navigation), and record trigger rates for each group separately | Query form affects triggering: consistently supported by large-scale repeated tests. Grouping by intent: practitioners' repeated, controlled tests found |
| **Make questions and long queries your main targets**: these queries are the most likely to trigger AI answers, and are where GEO can have an effect | Repeated tests on real AI search engines found; three studies point in the same direction |
| **Run search on / off comparison tests**: ask the same question with web search turned on and turned off, to judge whether your absence is due to training memory or to real-time retrieval | Practitioners report from their own tests (scoring of about 180 companies), not independently verified |
| **Use "zero citations" to judge whether search happened**: in monitoring data, flag answers with no citations separately. One practitioner found that all 406 non-connected answers had zero citations | Practitioners report from their own tests |
| **Monitor each product separately**: do not assume all AI products behave the same. Practitioners report from their own tests that Gemini searched 493 times out of 500, Perplexity searched all 500 times, and almost all answers without search came from ChatGPT (343 of 406) | Repeated tests on real AI search engines found (differences between models); specific figures are from practitioners' own tests |
| **State the search setting when monitoring through the API**: record whether search was forced or automatic, and distinguish the two in reports | Practitioners report from their own tests; the difference between API and product is supported by research |
| **Factor platform policy changes into interpretation**: when visibility on a topic suddenly changes a lot, first check whether the AI answer trigger rate for that topic has changed | Repeated tests on real AI search engines across years found |
| **For queries that do not trigger search, accept that it is a long game**: the only way is to keep being mentioned in third-party sources and gradually enter the training data of future versions | Mechanistic inference; practitioners widely believe third-party comparison content is key, which is an opinion, not proof |

### Do not do

- **Do not judge an engine by a single "average trigger rate"**. Trigger rates vary mainly with the prompt mix.
- **Do not add words such as "list sources", "latest" or "2026" to monitoring prompts**, unless that is exactly the situation you want to test. Practitioners report from their own tests that such words sharply increase search frequency, and most real users do not ask questions this way.
- Do not treat results from the API's auto mode as "web-connected visibility". They may be mostly training knowledge, or a mix of the two in unknown proportions.
- Do not assume that changing your own pages can change results for queries that do not trigger search. These queries never read your pages.
- Do not treat the appearance rate of shopping carousels as the search trigger rate. They are different mechanisms.

### Already outdated

- **Equating "ranking first on Google" directly with "visible to AI"**: for queries that do not trigger search, ranking has almost nothing to do with AI answers; even when search is triggered, the overlap between the sources of AI answers and the search results page is low (see later chapters).
- **Tracking only navigational or brand-name queries**: these queries have the lowest rate of triggering AI answers.

## 6. Key points

1. "Whether to search" is the first gate of the AI search pipeline. Without a triggered search, web content has no chance to be read.
2. Trigger rates vary enormously: on the same set of prompts, one model searched only 14% of the time and another 83%; Google AIO trigger rates range from 13.7% to 51.5% depending on the sample.
3. The most consistent pattern: questions and long queries are more likely to trigger AI answers, and navigational queries are the least likely.
4. Platforms actively adjust triggering strategy by topic and region, and visibility can change abruptly because of platform policy.
5. Wording such as "list sources" can push the API search invocation rate from 12.1% to 88.4%, but has little effect in consumer products. Watch for this bias when monitoring.
6. Whether comparison and purchase questions trigger search is unsettled, as practitioners' tests contradict each other. The more reasonable view: the trigger rate is mainly a property of the question rather than of the engine.
7. A search on / off comparison test is a practical way to judge whether you are fighting a "memory battle" or a "retrieval battle".
8. Triggering search is a necessary condition for being seen, not a sufficient one. After the search come further gates: retrieval, selection, citation and absorption.
