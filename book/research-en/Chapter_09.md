# Chapter 9: Measurement: Visibility Is a Distribution, Not a Ranking

> Where this chapter sits: the main thread of the book is "triggering → accessibility → retrieval → selection/ranking → citation → absorption → user behavior". The earlier chapters discuss how to influence this pipeline; this chapter discusses how to **see** it. If the measurement itself is unreliable, none of the optimization in the earlier chapters can be verified.

## Questions this chapter answers

1. Why does asking AI once and taking one screenshot prove almost nothing?
2. How many repetitions, and how broad a coverage, does a credible AI visibility number need?
3. Are the answers seen through the API, the web version and the app the same? Which one should you measure?
4. Why should "mentioned", "cited" and "recommended" be counted separately?
5. How do you judge whether the numbers from a tracking tool or a GEO vendor can be trusted?

## 1. Core principles

### Principle 9.1: Each question asked is only one sample drawn from a distribution

A traditional search results page stays roughly fixed over a short period. You search once, a colleague searches again, and you see roughly the same ranking. So "position 3" is a meaningful description.

AI search does not work this way. For the same question, every time it is asked it passes through several stages that vary:

```
The same question
   │
   ├─► Query rewriting (query fan-out; the sub-queries split off may differ each time)
   ├─► Retrieval (the index and real-time results are changing)
   ├─► Generation (model sampling is itself random)
   ▼
One answer = one draw from a distribution

Repeat N times ──► N answers ──► mention rate (e.g. 7/20) + uncertainty interval
```

So the correct unit of visibility is not a "ranking" but **the mention rate over a fixed set of questions after many repetitions**.

Repeated tests on real AI search engines found:
- In daily measurements of 4 AI search engines over 45 consecutive days, the overlap of cited sources between adjacent days (Jaccard) was only 0.34–0.42. Put simply, about two-thirds of the sources change every day.
- Repeating 10 times within the same day gave a source overlap of 0.32–0.43, about the same as across days. This means the variation comes mainly from **the randomness of each individual query**, not from "today's web being different from yesterday's".
- On one of the engines, 57.8% of runs cited no sources at all.
- Another study ran the same query repeatedly on three engines. The median overlap of the sets of cited domains was about 0.29–0.31 for one engine and 0.33–0.40 for another, and even the most stable was only 0.50.
- Even for frequently cited domains, the share obtained from a single measurement has a 95% confidence interval 3–7 percentage points wide. Many of the "gaps" between domains actually fall within the noise.

Practitioners' repeated, controlled tests found results in the same direction:
- Across 197 websites in one vertical and three engines, with each prompt run three times, 32% of citations appeared in only one of the three runs.
- When the same prompt was run twice within 24 hours, the top-recommended brand differed 48.5% of the time.
- For the same set of 45 local-service queries, run twice with identical wording in fresh sessions, about one-third of the recommended businesses on one engine were swapped out.

A simple statistical example shows why a "single number" is dangerous. If a brand appears 4 times in 10 runs, you would say its mention rate is 40%. But using the exact binomial interval, the 95% interval for the true mention rate is roughly 12%–74%. A percentage without a sample size carries almost no information.

### Principle 9.2: Widening the "breadth" of measurement is more effective than adding "depth"

"Run it a few more times" is correct, but it is not the whole story.

Repeated tests on real AI search engines found:
- When the variance of more than 10,000 brand answers is broken down, **the query language** is the largest systematic source of variation, accounting for about 26.5% of the variance of a single answer; the brand itself accounts for only 1.5%.
- After the 5th repetition of the same prompt, adding 5 more repetitions barely reduces the error; adding 3 more languages instead reduces the error by about 15 times as much.
- The reliability of a single answer for distinguishing between brands is only about 0.01.
- Mentions at the brand level are more stable than at the URL level: the adjacent-day overlap for brands is about 0.45–0.59, higher than the 0.34–0.42 for sources.

There is no fixed answer to how large a sample you need:
- One study used 10 topics × 125 queries × 3 platforms and a sequential convergence method, based on "the ranking reaching a plateau", to decide when collection could stop. Most combinations stabilized at 33–75 responses, but 3 combinations (all on the same engine) never converged within 125.
- If you stop using only a fixed threshold (for example a rank correlation coefficient ≥ 0.95), all 30 combinations reach it, but only 19 hold it. Looking only at ranking stability, the agreement between the ordering and the final result can be as low as 0.364; adding a signal-to-noise condition raises the worst case to 0.717.
- The number of citations per answer varies widely across engines: two engines give about 15–50 per answer, another only about 4–6. The sparser the citations, the more queries you need to collect. Another study estimated that narrowing the interval of a share to 5 percentage points requires about 30–50, 90–100, and 150 or more queries for the respective engines.

**Re-running and rephrasing are two different things.** Re-running the same prompt smooths out randomness; asking in a different way tests "are you still there if the question is phrased differently". Practitioners widely believe both are needed, and that leaving out either one will still mislead you.

### Principle 9.3: Different observation layers give results that cannot substitute for each other

Before saying "I see myself in AI", first ask: at which layer?

| Observation layer | Common way to obtain | Known differences |
|---|---|---|
| Consumer interface (web version) | Manual or browser capture | Source overlap with the API is only 12.0–14.8% |
| Consumer interface (app) | Manual | Domain overlap with the same platform's web version is only 0.19–0.51; on one platform only 0.014 at URL level |
| API (search enabled) | Programmatic calls | Some APIs do not return certain social platform sources shown in the interface (for example X) |
| API (search not enabled) | Programmatic calls | Measures the model's memory, not retrieval results |
| Logged-in account | Personal use | Affected by conversation history and memory |

The first three rows above are results of repeated tests on real AI search engines. The differences between engines are also large: two mainstream engines share on average only 5.4% of domains for the same query, and 76.7% of comparisons have no domain in common at all.

Another study that captured the internal execution of the ChatGPT web version (versions 5.2–5.5) adds that the URLs cited by the API match those of the web version (F1) only 13%–15% of the time, while precision at the domain level is 28%–41%, so comparisons should be made at two levels, URL and domain. **Reasoning mode also changes search behavior**: Instant mode mostly searches only one round, while Thinking mode averages 3.2 rounds and about 12 queries; the web version may also switch to another model partway through a session. When measuring, record the mode and the reasoning effort.

Practitioners' tests (mostly repeated and controlled) add several layers that are easy to overlook:
- **Whether sources were used**: across about 2,600 runs, one engine gave no sources at all in 282 of 615 runs (46%), while another engine gave sources in all 359. In another 10-day record of 2,209 answers, one engine showed sources in only 59% of answers. So "not appearing in the answer" means different things on different engines: being absent from an answer that lists a dozen or more sources means you really were not chosen; being absent from an answer that lists no sources at all tells you almost nothing.
- Whether it was triggered: when the same query was repeated in the same location a few minutes apart, AI Overviews appeared in only about 7 out of 10 times. Seeing "no AI Overview" from a single query does not support a conclusion.
- Location and language: with the same model and the same question, merely telling it the user's country turned a brand from absent to named in 5 out of 6 cases. When the same set of questions was asked in two languages, the cited sources overlapped by only 22%.
- API and interface: the same query cited the product itself about 50% of the time in the product interface, but not once in 30 runs through the API.

### Principle 9.4: A visibility score is "defined" by the prompts you choose and the counting rules

Simulations or theoretical analysis suggest that, in principle, the following may happen: the activation rate of the same sub-corpus can change from 39.7% to 70.5%, a difference of about 31 percentage points, simply by adjusting the weights of different query types; changing the weights may even reverse the ranking of two systems. This was demonstrated by recomputing published aggregate data and with invented examples, not by a new experiment, but it points to one thing: **the score does not exist objectively; it is defined jointly by the prompt set, the weights and the scoring rules.**

The unit of evaluation is also a definition. Current measurements usually take "one question, repeated many times" as the unit, but real users ask follow-up questions in sequence. Simulations or theoretical analysis suggest that, in principle, "conversation capture" may occur: within the same conversation, sources cited early are more likely to be cited again later, first because the conversation history affects later retrieval, and second because the answer steers the user's next question toward that source. If so, single-turn measurement captures only the direct effect and misses the part that accumulates over several turns, and the two units might even rank different methods in different orders. But this is only a theoretical model, and the numbers are determined by parameters the authors chose themselves; the direction is also unknown: if users tend to follow up with "is this true?", single-turn measurement would instead overestimate the effect. A comparison you can run yourself: take the same set of multi-turn questions and run them under two conditions, "asked in sequence in the same conversation" and "a new conversation for each turn", then compare how many times the target source is cited (a theoretical suggestion, with no test results yet).

That user needs are spread across several turns already has evidence from real logs. Descriptive analysis of large-scale real user logs (8,133 real English multi-turn conversations, two corpora) shows: in about half of conversations, the last message leaves out conditions stated earlier (50.3%, 44.8%); only about a quarter of last messages contain all the conditions; in conversations of 5 or more turns, about 70% of conditions remain only in earlier turns. So replaying one fixed prompt measures the answer to "this one sentence", not the user's complete request within a conversation; comparisons can be split into three conditions: the full conversation, only the user's messages from each turn, and only the last message. Whether single-turn measurement overestimates or underestimates visibility has not yet been tested.

The baseline is also part of the definition. Repeated tests on real AI search engines found (a source audit before elections in Europe and North America; the large-model part had only about two hundred answers): for the same set of ChatGPT answers, mentions of a certain type of party were 13.3 percentage points higher relative to an "even distribution" (significant), only 2.3 higher relative to the volume of media coverage (not significant), and 17.3 higher relative to the previous election result (significant). With the same data, changing the baseline turns the conclusion from "biased" into "not biased". The same is true of GEO visibility share: you have to state clearly what it is compared against, for example media share of voice or market share.

Practitioners report from their own tests several specific situations (mostly data from single teams, not independently verified):
- **Question type**: on a single engine with each question run once, 41% of "best X" questions named the company being tested, 20% of comparison questions did, and 40% of use-case questions named no vendor at all. If the mix of tracked questions shifts toward use-case questions, the mention rate will "drop" even though nothing has actually changed.
- Wording: the same page is cited for one exact query; add one word to the query and the whole list of sources is replaced. With the same query and the same wording, it was cited in the early morning of one day and not by the evening.
- Putting the brand name in the question: if you put your own brand name in the question, it will almost certainly appear, and this number is meaningless.
- Rotating the prompt set: regenerating the question set each time creates "completely fake declines", which are then afterwards paired with stories about algorithm updates.
- Scoring with a model: when an LLM is asked to score visibility, the same input drifts by 10–15 points. Model scoring may also measure the wrong thing: in a simulation study, four LLM judges predicting which answer in a Q&A community would be most popular with real people were right only 8.2%–16.4% of the time, below the 25% of random guessing.

One practitioner observed (single observations, offered only as leads):
- After counting product aliases as mentions, the score for the same set of 20 questions on the same four engines went from 77 to 94. The world did not change; only the counting rule did.
- After removing samples in which "the question already contains the brand name", the share of cited sources named in the answer fell from 10.9% to 8.9%; for "X vs Y" questions it fell from 15.8% to 8.1%.
- Of 60 buyer questions collected from real communities and from "related questions", in one round 13 and in another round 23 got AI answers that named no brand at all. Tracking such questions can never prove anything.
- Testing only with the most competitive core terms produced the conclusion "0 out of 10 questions"; after adding more specific questions, the same website was cited.

### Principle 9.5: Mention, citation and recommendation are three different quantities

"Appearing in an AI answer" has at least three meanings:

| Quantity | Definition | Why it matters |
|---|---|---|
| Mention | The brand name appears in the text of the answer | Users will remember the name, but there may be no link |
| Citation | Your page appears among the sources or links | May bring clicks, but the answer may be recommending someone else |
| Recommendation | The answer treats you as a suggested choice | Closest to a business outcome |

Repeated tests on real AI search engines found: in a large-scale study of a Chinese-language generative engine, only 8.3% of the brands that appeared in the citation pool finally made it into the answer; of the sources listed, only 66% had their content actually make it into the body of the answer.

Practitioners report from their own tests:
- Across 76 companies and about 1,140 prompts, brands were mentioned in an average of 44% of answers but recommended in only 10%.
- In about 26,400 answers about brands in competitive categories, brands appeared only about 16% of the time; of this, about 13% were cited and about 3% were only named without a link. The differences between engines were clear; the median brand was about 13%, with the average pulled up by a few large brands.
- One practitioner observed that a newly created author entity was tracked daily for 99 consecutive days; the engines got to know him better and better, but the recommendation rate was zero from start to finish.

Practitioners widely believe that "being cited does not mean being recommended or mentioned"; this is the consensus with the most supporters in this chapter's evidence pack.

Beyond these three quantities, there are two more, one before the answer and one after it:

```
Crawled (crawler logs) → Cited / mentioned / recommended (prompt sampling) → Clicked (referral traffic) → Conversion
     Leading indicator               Intermediate indicator                     Outcome indicator
```

Practitioners report from their own tests that tracking tools almost all measure only the middle segment, yet are often sold as covering all three. Server logs can provide leads on the other two segments, and changes show up there earlier. In addition, practitioners' repeated, controlled tests found that most AI assistants open links without passing on source information (the referrer), so visits are recorded as "direct traffic", and tools that look only at referral traffic structurally underestimate it.

## 2. How strong is the evidence

| Conclusion | Type of evidence | Strength | Scope and limitations |
|---|---|---|---|
| About two-thirds of cited sources change every day, and the same holds for repetitions within a day | Real engines, 45 days of daily measurement + 10 repetitions within the same day | Strong (B) | 4 engines, web interface capture |
| A single measurement has an interval 3–7 percentage points wide | Repeated measurement through real engine APIs | Medium (B) | Authors are a visibility vendor; only 3 topics |
| There is no universal fixed sample size; it should be decided sequentially | Real engines, 30 platform × topic combinations | Medium (B) | Authors are a vendor |
| Breadth (languages) reduces error more than repetition, by about 15 times | Real engine APIs + statistical model estimates | Medium to weak (B) | Authors are a vendor; the outcome variable is sentiment; confidence intervals not yet computed |
| API and interface sources overlap only 12–15% | Real engines, paired interface and API | Strong (B) | Product recommendation queries |
| App and web overlap 0.19–0.51 | Real engines, 8 interfaces | Medium (B) | Chinese-language engines; authors are a vendor |
| Changing weights can make scores differ by 31 percentage points | Theoretical analysis, recomputation of existing data | Weak (E) | Only shows what is possible in principle |
| In multi-turn conversations, sources cited early may keep being cited (conversation capture) | Theoretical model | Weak (E) | Only shows what is possible in principle; direction and size not tested |
| User conditions are spread across several turns, and the last message often leaves out earlier conditions | Real conversation logs (8,133 conversations) | Medium (descriptive) | Model answers not tested; conditions detected by keyword rules |
| Mention, citation and recommendation are separate | Practitioner tests from many sources + broad consensus | Medium | Definitions vary between teams; not independently verified |
| Relationship between visibility and traffic or revenue | None | **No evidence** | No research currently shows that GEO visibility reliably brings traffic or conversions |

Two reminders:

1. **Conflicts of interest.** A considerable share of the measurement studies cited in this chapter come from AI visibility vendors, and much of the practitioner data also comes from people who build tracking tools themselves. Their methodological criticisms are often correct, but their conclusions naturally lean toward "you need more, and more expensive, measurement".
2. **The biggest gap is in the last segment.** All the strong evidence at present says "how to measure without fooling yourself"; none of it says "how much business a measured rise in visibility will bring".

## 3. Debates and counterexamples

### Debate 1: How many times should each prompt be run?

| Position | Basis |
|---|---|
| At least 7 times a day (8 for sources), on a rolling 2–4 weeks | 45-day repeated test on real engines |
| No fixed number; decide by sequential convergence; sparse engines need more | Study of 30 combinations on real engines |
| Beyond 5 repetitions the marginal value is very low; the budget should go to languages, models and rephrasings instead | Variance decomposition on real engines (sentiment outcomes only) |
| 3 times, counted by a "2 out of 3" majority vote | Practitioners' repeated, controlled tests |
| Diminishing returns after 5–10 times for top positions; the long tail needs more | Practitioners report from their own tests |
| 10 or more, or even 20 or more | Practitioners report from their own tests; community consensus |

These positions do not fully conflict: the research emphasizes **the total sample size and how it is allocated**, while the practitioners' "3 times" is usually used under budget constraints, together with many questions accumulated over several weeks. The only thing truly wrong is "once".

### Debate 2: Measure the API or the product interface?

- For the API: it can be automated, the model version can be fixed, and there is no contamination from personal memory. One practitioner's data show that checking with their own account gave results that "looked great", but after logging out the results were clearly worse in a clean session; another practitioner retested, in 20 clean accounts, someone else's claim of "cited within a week", and the brand did not appear at all.
- For the interface: research shows that API and interface sources overlap only 12–15%, and what users see is the interface. One practitioner reported that the same query was about 50% in the interface and 0/30 through the API.
- The compromise: practitioners widely recommend **choosing one observation surface and keeping it fixed**, otherwise the trend line measures "a change of observation surface" rather than visibility; if you use the API, spot-check with small samples in the interface.

### Debate 3: Which engine is the most stable?

Practitioner data are inconsistent with each other: one person found that an engine's sources were about 90% the same a day apart, while another team found that re-running three models five times gave overlaps of about 65%, 55% and 35%; one person said a certain engine had the highest share of "appearing only once in three runs" (43%), while another said the same engine was the most stable for brand mentions. On the research side, one of three engines had the highest median overlap (0.50).

Only two points are broadly agreed: the engines really do differ in stability, and "stable sources" and "stable brands" are not the same thing. The ordering changes with query type, time and settings, so the stability of any one engine should not be treated as a fixed value.

### Debate 4: Are brands more stable, or sources?

- Research: mentions at the brand level are more stable than at the URL level.
- Practitioners report from their own tests (supporting): running the same prompt on the same engine for 30 consecutive days, the sources changed often, but two brands were recommended in 28/30 and 26/30 runs respectively.
- Practitioners report from their own tests (opposing): a brand's **description** is less stable than its citations. The same brand was the top recommendation in one round and only mentioned in passing in the next; citations, by contrast, overlapped 40–80% across five runs. The instability is concentrated in positions 4–10, which is where most brands fall.

A possible explanation: "whether you are mentioned" is fairly stable, while "how you are described and in what position" is less stable. Reports should keep these separate.

### Debate 5: Can AI visibility be measured at all?

- The skeptical side: practitioners widely believe that AI visibility cannot currently be measured reliably, a view with a fairly large number of supporters; in another case, ten people each opened an incognito window and ran the same questions on five platforms, and each person got different answers and citations.
- The measurable side: one practitioner measured 16 frozen questions once a day, and the standard deviation over 28 runs was 2.8 percentage points; the citation rates of three engines were 27%, 9% and 0%, gaps far larger than the noise, so these gaps are real. The other side argues that sampling is the standard method for measuring a random system anyway, and the key is repetition and intervals.

The two sides are actually saying the same thing: **a single snapshot cannot be measured, but the distribution from repeated sampling can**, only with limited cost and precision.

### Debate 6: Can numbers from different tools be compared?

- One practitioner observed that the same domain's AI citation counts in two tools differed by about 8 times, presumably because the two count different populations (one counts every appearance in every re-run, the other samples only its own index). Practitioners widely believe raw numbers cannot be compared directly across tools.
- Counterexample: one practitioner tracked the same 5 brands with three commercial tracking tools; the brand ordering was exactly the same and the top 5 cited domains overlapped completely, but the overlap of the top cited URLs was only 55% or 64% depending on the platform, and only 14% on one platform.

In short: **the coarse relative ordering may agree, while the fine-grained URLs and absolute values differ greatly.**

### Debate 7: Is it simply "present or absent" for local businesses?

One practitioner believes that whether a local service business appears in AI is basically a stable binary outcome, determined by entity recognition signals, and that the run-to-run fluctuation in tools comes from measuring the wrong thing. But the practitioners' repeated, controlled tests described earlier show that when the same set of local queries was run twice with unchanged wording, about one-third of the recommended businesses on one engine were still swapped out; only the businesses with the widest off-site footprint appeared every time. The former is a single opinion, while the latter has repeated measurements; at present the latter is better supported.

## 4. Cases

### Case 1: A "visibility decline" that was really an unpaid bill

- **What was done**: a team measured weekly on 7 AI answer engines using 40 frozen buyer questions, and published the data.
- **What was observed**: one week the total number of cited domains fell from 851 to 790. Broken down by engine, one engine had dropped from 225 to 73, while most of the other engines rose. The cause was that this engine's API quota ran out in the middle of the measurement, and only 11 of the 40 questions were answered. The whole "decline" was an instrument failure.
- Follow-up: they built a failure taxonomy (timeouts, rate limiting, refusals, wrong question, no answer parsed, and so on) and found two things: they had first written the classifier using imagined error messages, and when run on real errors, 38 of 69 (55%) fell into "other"; and one engine's field had been sending only truncated questions all along, so all 80 rows published over the first two weeks were relabeled as "asked the wrong question". Another engine fell by 37 that week, and they admitted they could not tell whether this was due to their own code changes or to changes in the engine.
- Principles: 9.1, 9.4. Failures must not be recorded as "not mentioned"; every number must carry its denominator and its number of failures.

### Case 2: A model update moves the whole panel at once

- **What was done**: a tracking team fixed a set of prompts and recorded the cited sources over a long period.
- **What was observed**: one engine had cited a large community forum 9 times in one week, and then not once in 64 consecutive runs. All brands on the panel moved at the same time, and nobody had changed anything.
- Approach: they recommend setting about a quarter of the prompts as a "not optimized" control group. If these prompts that nobody has touched move as well, the engine has changed, and it is neither your achievement nor your fault. One practitioner observed something similar: a fixed set of 5 peer brands rose as a whole from 0.226 to 0.285 within one week, with the measurement settings completely unchanged.
- Principle: 9.1. Before-and-after comparisons must have a control, otherwise a model update will be taken for the effect of optimization.

### Case 3: Logs exposed "visible on a certain engine"

- **What was done**: a practitioner compared the AI crawler records in the server logs with the results of prompt sampling.
- **What was observed**: one engine's search crawler fell from 548 fetches a day in mid-August to 189 a day recently; the user-agent that represents real people opening links during conversations fell from 230 a day to 48. The search crawlers of two other engines were at zero every day for a whole month.
- Conclusion: any tool that said he was "visible on those two engines" was sampling something that could not possibly be true. With zero crawling there can be no retrieval-based citation, so crawling is the earliest leading indicator.
- Principle: 9.5.

### Case 4: The dashboard says 45%, but the client cannot find it themselves

- **What was done**: a project rewrote about 1,000 target keywords into about 20,000 natural-language prompts and used a tracking dashboard to measure the brand's coverage on a certain engine.
- **What was observed**: the dashboard showed 45% brand coverage, but whenever the client spot-checked it themselves, they could not see the brand.
- Possible causes: the differences between observation layers described in Principle 9.3 (API versus interface, account state, location) could all produce such a gap. This case did not itself find the exact cause, but it shows that "the tool's numbers" and "what buyers see" must be reconciled regularly.

### Case 5: Fix 16 questions and first measure the noise floor

- **What was done**: a practitioner froze 16 questions for his own website, left them unchanged from the first day, and ran them once a day.
- **What was observed**: the day-to-day standard deviation over 28 runs was 2.8 percentage points. On the same day, the citation rates of three engines were 27%, 9% and 0%, gaps far larger than the noise, which can be trusted. The difference between two model tiers of the same engine (17 versus 5) was close to the noise band, and he did not interpret it.
- Principles: 9.1, 9.2. Only once you know what the noise looks like do you know which changes are worth looking at.

### Case 6: A ten-day before-and-after test

- **What was done**: a small product was absent from 7 of 8 buyer questions. For the questions where AI named competitors but not the product, the team published two comparison articles and one page of technical documentation, and rewrote the project description.
- **What was observed**: after ten days, the number of questions it appeared in rose from 1 to 5, and three of four engines corrected their misclassification of the product's category.
- Interpretation: these are data from practitioners' repeated, controlled tests, and the author builds measurement tools. It shows the closed loop of "target the questions where you are absent → change → retest", but the sample has only 8 questions, and the author himself cautions that each question should be run more than once before drawing conclusions. Another practitioner compiled 26 public "visibility improvement" cases: 19 defined a prompt set and 16 used repeated measurement rather than a single screenshot, but not one clearly isolated a single effective factor; most changed content, structured data, PR and third-party mentions at the same time. Public cases are suitable for generating hypotheses, not for estimating the effect of a single practice.

### Case 7: The search engine's official AI impressions report

- **What was done**: a chocolate database website started seeing the generative AI performance report in Google Search Console.
- **What was observed**: from mid-May, there were 9,093 cumulative generative AI impressions; daily impressions grew from 30–40 to 200–280, and 579 URLs appeared in total. Another practitioner's website had 116,061 AI impressions in 53 days.
- Limitations: practitioners widely point out that this report lacks query and click data. One practitioner observed that about two-thirds of the long-question impressions in their own report were actually other people running tracking probes with "persona prompts", with zero clicks, which contaminates judgments about demand. Bing Webmaster Tools also provides AI citation data; one practitioner reported about 865 citations in seven days for a two-month-old new site, but with large daily fluctuations.
- Principle: 9.5. Official reports are among the few "non-sampled" data, but they cover only the provider's own engine, and their definitions are limited.

## 5. What to do

### 5.1 Build a credible measurement process

| # | Practice | Strength of evidence |
|---|---|---|
| 1 | **Build a baseline first, then make changes.** Before changing anything, measure at least twice, ideally spanning two or more days; otherwise you cannot separate the effect of a change from day-to-day drift. | Practitioners widely believe (broad consensus) + practitioners' tests |
| 2 | **Take the prompt set from real buyer language**: sales calls, customer service records, reviews, query reports from webmaster tools. Do not put your own brand name in the questions. | Practitioners report from their own tests; community consensus |
| 3 | **Freeze and version the prompt set.** Add new questions as new columns; do not replace old questions or change their wording. | Practitioners report from their own tests |
| 4 | **Screen the questions first**: do a trial round, move questions that "never name any brand" aside and leave them out of the main score; group trends by question type (best, comparison, alternatives, use case). | Practitioners report from their own tests; one practitioner observed |
| 5 | **Repeat each question many times, and report the mention rate and the sample size**. Research recommends at least 7–8 times per question per day; on a limited budget, at least 3 times with majority-vote counting. | Repeated tests on real AI search engines found; practitioners' repeated, controlled tests |
| 6 | **Allocate the budget to breadth**: multiple engines, languages, regions and phrasings are more effective than running the same prompt dozens of times. | Repeated tests on real AI search engines found (sentiment outcomes only; authors are a vendor) |
| 7 | **Report each engine, language and region separately**; do not blend them into one average score. | Repeated tests on real AI search engines found; practitioners' tests |
| 8 | **Fix one observation surface and record the settings**: API or interface, whether search is enabled, model version, region, whether logged in. When using the API, regularly spot-check with the product interface in a clean session. | Repeated tests on real AI search engines found; practitioners' tests |
| 9 | **Record for every run**: whether there was an answer, whether sources were used, failure category, mention, cited URLs, whether recommended, position. Failures and missing data do not count as "not mentioned". | Practitioners' repeated, controlled tests |
| 10 | **Fix the definition of a "hit"**: whether brand aliases and product names count; whether echoes from questions that already contain the brand name are removed. Once the definition is set, do not change it; if you do, rebuild the baseline. | One practitioner observed |
| 11 | **Set up a control group**: leave about a quarter of the prompts without any optimization; also track a set of peer brands you are not working for. | Practitioners' repeated, controlled tests; one practitioner observed |
| 12 | **Look at trends, not single weeks**: research recommends a 2–4 week rolling window; practitioners mostly use 4 weeks or more. One practitioner's rule of thumb is to treat single-week changes within 15% as noise at first, and to take them seriously only if they recur for two consecutive weeks; this is only personal experience, not a law. | Repeated tests on real AI search engines found; practitioners report from their own tests |
| 13 | **To judge whether a change is real, ask three questions**: did several platforms move at the same time? Did the number of cited URLs move with it? Does the timing match something you did? | Practitioners report from their own tests |
| 14 | **Record cited URLs, not just "whether you appeared"**. The list of cited sources tells you which pages to pursue exposure on, but it is only correlation, not attribution. | Practitioners report from their own tests |
| 15 | **Fill in both ends**: use server logs to see whether AI crawlers are fetching; use the official webmaster tools to see AI impressions; split traffic into two buckets, "confirmed as from AI" and "inferred as possibly from AI". | Practitioners report from their own tests |

**Cost reference** (practitioners report from their own tests; prices change): building your own with a search API that returns citations costs about half a US cent per query, about 0.5 US dollars for a round of 100; running about 300 queries × 4 engines every day costs about 30 US dollars a month in API fees; 600 runs a day on a single engine cost about 1.6 US dollars. One practitioner's self-built script also crashed at about 50 queries, after spending about 200 US dollars. Building your own is not necessarily cheaper, but it gives you full control over the method.

**Minimum viable version**: one practitioner's approach is to fix 5 questions that real customers ask, ask each once per engine on the same day every week, and count only "how many of the 5 questions mention us". The sample is small, but the advantage is that the client can sit alongside and reproduce it themselves. A better approach is to ask each question 3 times.

### 5.2 How to evaluate tracking tools and GEO vendors

One practitioner who also builds tools proposed a useful general principle: **does this tool make claims that "you could catch being wrong"?** Saying only "you appeared" cannot be falsified; saying "the answer cited your pricing page and a competitor's comparison page" is something you can open and check.

| Question to ask | Why | Evidence |
|---|---|---|
| How many times is each prompt run? Are sample size and intervals reported? | About one-third of a single run is noise | Research + practitioners' tests |
| Is it measuring the API (with or without search) or the product interface? | Overlap between observation layers is only 12–15% | Research |
| Who set the prompt set? Can it be customized and frozen? | Default question banks are often skewed toward other industries and contain many questions "nobody can win" | Practitioners report from their own tests |
| Can you see the raw answers and cited URLs? | Only numbers that can be checked have value | Practitioners' repeated, controlled tests |
| Is each engine reported separately? | A blended average mixes "genuinely absent" with "the engine listed no sources" | Practitioners' tests |
| How are failures, missing data and answers without sources handled? What is the denominator? | Recording failures as zero creates fake declines | Practitioners' tests |
| Can it distinguish model updates from your changes? Is there a control group? | Model updates make a whole category move together | Practitioners' tests |
| Is the score a deterministic rule, or scored by a model? | Model scoring can drift by 10–15 points on the same input | Practitioners report from their own tests |
| Are all the engines it claims to cover actually queried? | One practitioner read the code of an open-source tracker whose documentation claimed coverage of several engines, but the code had only one engine's API and three fixed questions | Practitioners report from their own tests |
| Where does "prompt search volume" come from? | One practitioner tested an AI keyword data API, which reported zero search volume for a batch of niche queries, yet the platform answered every time they were queried manually; the source and representativeness of such data cannot be verified | Practitioners report from their own tests |
| How does traffic attribution handle visits without source information? | Counting only referral traffic structurally underestimates | Practitioners' repeated, controlled tests |
| Do its numbers match your business data? | The tool's charts should agree with what you hear in sales calls | Practitioners' repeated, controlled tests |

When evaluating vendors, practitioners widely believe you should ask them **to explain the specific measurement method, show verifiable results, and explain the link to business outcomes**. Two more conditions can be added: whether, before charging, they can show you a baseline done to the standards in the table above; and whether changes and results can be matched to specific weeks.

Warning signs (if any one appears, ask further):
- Only a single blended cross-engine "AI visibility score" or "ranked No. X in AI".
- Percentages without sample sizes. One practitioner observed a report that printed "1 mention in total" as "1% share of voice", and also gave unexplainable fields such as "100% purchase likelihood" from a sample of 15 prompts over 14 days.
- Only screenshots, or only a list of prompts without the raw answers.
- Long-term trends reported from a rotating question set.
- A single before-and-after comparison used to prove "our optimization works".
- The same domain's numbers differ several times over between tools, yet nobody can explain how each one counts.

Practitioners report from their own tests that, after testing several tools in a row, the numbers jumped sharply from week to week (60%, 35%, 50%), and when they manually ran the same prompt 10 times in a row, the answer was different each time. The problem is not that the tools have bugs, but that most tools run each prompt only once, because running it ten times also makes the API cost ten times higher.

### 5.3 Do not do

- Do not use one question and one screenshot to prove "we were recommended" or "we disappeared".
- Do not use a logged-in personal account to check your own visibility.
- Do not count results from questions that contain your brand name toward visibility.
- Do not change question wording, replace questions or change counting rules during tracking while continuing to draw the same trend line.
- Do not record API failures, rate limiting or missing answers as "not mentioned".
- Do not add up or compare raw citation counts directly across engines: the number of citations per answer differs several times over between engines.
- Do not treat the list of cited sources as causal attribution.

### 5.4 Already outdated

| Outdated practice | Why it is outdated |
|---|---|
| Treating AI answers as a search results page and tracking "what position" | The answer is a distribution; the list and its order change almost every time |
| Running each prompt once a week and drawing a trend chart | The noise of a single run is larger than the effect of most changes |
| A one-off "AI visibility audit" | An audit is only a snapshot; models, competitors and cited sources change within weeks. Practitioners report from their own tests that one brand's visibility score held the same value for 47 days while purchase recommendations had already shifted to a competitor |
| Measuring GEO by traffic alone | Being named without a click leaves no record; AI visits are often recorded as direct traffic |

## Key points

1. **Visibility is a probability distribution, not a ranking.** On real AI search engines, about two-thirds of cited sources change every day, and the same holds for repetitions within a single day. A single snapshot has no value as evidence.
2. **Report the mention rate, always with the sample size and interval.** The true interval for 4 out of 10 is roughly 12%–74%.
3. Spend the budget on breadth. Multiple languages, engines and phrasings reduce error more than running the same prompt over and over; there is no fixed answer to how large a sample you need, and sparse engines need more.
4. Observation layers cannot substitute for each other. API and interface, app and web, logged in and logged out, different regions and languages: each shows something different. Choose one observation surface, fix it and record it.
5. Scores are defined. The prompt set, weights, question types and hit rules can all change the numbers dramatically; freeze them, and if you change them, rebuild the baseline.
6. Count mentions, citations and recommendations separately, then fill in the two ends of crawling and traffic. Being cited is not the same as being recommended; crawling is a leading indicator, and traffic is structurally underestimated.
7. Without a control group, you cannot tell your changes apart from model updates. Keep unoptimized prompts and peer brands as a benchmark.
8. When evaluating tools and vendors, trust only numbers that can be checked. You need to be able to see the raw answers, cited URLs, denominators, handling of failures and number of runs. No research currently shows that visibility reliably converts into traffic or revenue, and anyone who promises this needs to show their own data.
