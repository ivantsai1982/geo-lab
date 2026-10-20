# Chapter 7: Citation and Absorption (Listed ≠ Used ≠ Used Correctly)

> In the main thread of this book, "Triggering → Accessibility → Retrieval → Selection/Ranking → **Citation → Absorption** → User behavior", this chapter covers the two stages most easily misread.
> Earlier chapters answered "how to enter the candidate set". This chapter answers: after you enter the candidate set, and even after you appear in the citation list, is your content actually used, and is it used correctly?

## 1. Questions this chapter answers

1. If a web page appears in the citation list of an AI answer, does that mean its content was used in the answer?
2. Why are some web pages cited heavily while their brand name hardly appears in the answers?
3. How many statements in AI answers are genuinely supported by their sources? What are the common types of distortion?
4. When users see citations, do they distinguish whether the citations actually support the answer?
5. When measuring GEO results, which layers should be looked at separately, and what is the denominator for each layer?

## 2. Core principles

### 2.1 Four layers: mention, citation, absorption, correct description

"Being seen by AI" is not one thing but at least four:

```
Retrieved (enters the candidate set)
   ↓
Listed (appears in the citation list: citation)
   ↓
Absorbed (content actually enters the body of the answer: absorption)
   ↓
Used correctly (the answer faithfully presents what the source meant: fidelity)
   ↓
Named (brand or site name appears in the answer text: mention)
```

These layers do not work as "if the layer above holds, the layer below automatically holds". Each layer loses some, and for different reasons:

| Layer | Question answered | Mainly decided by |
|---|---|---|
| Citation | Was the page listed as a source? | Retrieval and selection (see earlier chapters) |
| Absorption | Was the page's content written into the answer? | How the generation stage uses the context |
| Fidelity | Is what was written in correct? | The combination of model and search backend |
| Naming | Does the answer say your name? | Whether a claim needs to be attributed to a specific source |

There is one more gap that lies outside these four layers: **every single citation can be correct and the overall conclusion can still drift away from the available evidence.** Citation and fidelity only check whether the documents read were used correctly; whether the documents read represent all the available documents is a separate question. In an experiment with a fixed set of candidate documents (weaker evidence), which documents a deep research agent reads is influenced by ranking and early discoveries, forming a biased sample (see Chapter 6, Principle 6.2).

### 2.2 Principle 1: Breadth of citation and depth of absorption do not line up

On different platforms, "listing many sources" and "how much each source is used" are two different things.

A cross-platform static snapshot analysis shows (descriptive analysis, weaker evidence, possible in principle):

| Platform | Average citations per prompt | Average absorption per fetched page |
|---|---|---|
| ChatGPT | 6.88 | 0.271 |
| Google (AI Overview/Gemini) | 12.06 | 0.058 |
| Perplexity | 16.35 | 0.065 |

That is, on platforms that cite fewer sources, each source is used more deeply. The longer the citation list, the thinner a single source's weight in the answer may be.

Repeated tests on real AI search engines found the same gap on Chinese-language generative search platforms:

- Of the listed sources, 66% had content that entered the body of the answer;
- 30% were cited substantively;
- only 8% were cited in depth;
- 39.3% were "silent citations": listed as sources, but the answer did not use their content.

The same study also found that only 8.3% of brands appearing in the citation pool made it into the answer.

Another large-scale audit on real engines found that Google AI Overviews cites forum and Q&A community sources, but the actual use of these sources in answers is about 22 percentage points lower than their citation share. By contrast, encyclopedia sources were used slightly more than their citation share.

### 2.3 Principle 2: There is a great deal of "invisible use"

The direction can also be reversed: content is used but not credited.

Repeated tests on real AI search engines found that **14–53% of answer claims are supported by search results but carry no citation**. The same study also found that more than 15–20% of claims could not be grounded in the search results.

This means:

- Looking only at the citation list **underestimates** the real influence of some sources;
- and overestimates the influence of others (listed but not used, that is, the silent citations of the previous section);
- "Citation count" is not a reliable proxy for "influence".

### 2.4 Principle 3: Being used does not mean being used correctly

Even when a source really exists, is listed and its content is used, the answer can still distort it. The table below summarizes the main current measurements:

| Problem | Data | Type of evidence |
|---|---|---|
| Statements in Google AI Overviews not supported by sources | About 11% (98,020 statements; mainly omissions: omitted 7.0%, incorrect 2.7%, ambiguous 1.4%) | Repeated measurement on real engines |
| Citations that distort the source's meaning | 30.6% | Repeated measurement on real engines |
| Unsuitable sources (the source itself is not suitable to support the statement) | 27.1% | Repeated measurement on real engines |
| Answers containing at least one problematic citation | 71.3%–96.1% (depending on model) | Repeated measurement on real engines |
| Cited URLs that do not exist at all (hallucinated URLs) | 3.0%–13.3% | Controlled experimental system |
| More search calls, lower fact-check pass rate | One model fell from 78.6% at 2 calls to 16.7% at 150 calls | Controlled experimental system |

Key points:

1. **Distortion and unsuitability are two independent axes, and they trade off against each other.** In a measurement covering 761,495 citation pairs and 10 models, the model with the lowest distortion rate had a relatively high rate of unsuitable sources; the model with the highest distortion rate had the lowest unsuitability rate. No model was low on both.
2. **Both are decided mainly by the "provider (search backend)", not by model size.** The provider explained about 96% of the variance in source suitability and about 88% of the variance in faithfulness. Within the same provider, scaling up the model barely improved the distortion rate (difference under 0.8 percentage points). Reasoning models can lower the distortion rate (one model from 34.1% to 18.0%), but have almost no effect on source suitability (change under 2 percentage points).
3. High source quality does not mean faithful use. In longitudinal measurement of Google AI Overviews, the credibility scores of cited sources were higher than those of the first-page search results for the same query, but the correlation between source quality and statement faithfulness was only about 0.045, essentially unrelated.
4. A valid, relevant link does not mean the fact is supported. In controlled experimental systems, 12 of 14 models had link validity rates above 94%, and frontier models had citation relevance above 80%, yet fact-check pass rates were only 24%–77%.
5. Check first that the citation exists. In controlled experimental systems, 3–13% of cited URLs had no archived record at all and may never have existed. Deep research agents had a higher hallucination rate (10.7%) than ordinary search-augmented models (4.8%). Some models cited about 4.3 times as many sources, but their share of unresolvable URLs was about 2 times higher.

In addition, repeated tests on real AI search engines found that once search is connected, answers hedge less than the sources themselves: one system used about 40% fewer hedging expressions, and Google AI Overviews about 60% fewer. Where a source says "possibly" or "in some cases", the answer may state a definite conclusion.

### 2.5 Principle 4: Citations are a "persuasion signal"

Citations are not only source markers for machines; they also directly affect users.

- In a randomized survey experiment with fixed stimuli (4,927 people, 9 queries; simulation-level evidence, possible in principle), attaching reference links increased user trust (+0.091 on a 7-point scale) and willingness to share (+0.121). **Whether the links were valid or invalid and hallucinated made almost no difference to trust** (-0.021, not significant). Instead, flagging uncertainty lowered trust (-0.157).
- On real AI search engines, an analysis of large-scale crowdsourced preference data found (24,069 conversations, 12,652 preference votes) that user preference correlated positively with the number of citations. More important: **citations that support the argument (coefficient 0.29) and citations unrelated to the argument (coefficient 0.27) had almost the same effect on preference**; only citations that contradict the argument were not significant. This is correlation, not causation.

Implication: on the user side, citations work more like "looks well-founded" than "has been verified". This makes the distortion problem in Section 2.4 worse: an incorrect description with a citation attached is more likely to be believed.

### 2.6 Principle 5: AI rewrites testimony into generalized advice

Repeated tests on real AI search engines found (an audit of 30,000 answers from the built-in generative Q&A feature of a community platform):

- **The selection stage** favours comments that already have high scores, are top-level and are formal in tone: each 1 standard deviation increase in score percentile within the thread multiplied the odds of being selected by about 2.88; top-level comments had odds about 1.97 times higher; a formal tone about 1.49 times; an experiential tone was actually lower (about 0.79 times). Comments pinned or flagged by moderators were almost never selected.
- **The synthesis stage** erases first-person testimony: first-person singular expressions made up 3.3% of the sources, but only 0.06% of the answers.

"I used it for three months and the battery failed twice" gets rewritten as "some users report problems with battery durability". Personal experience is compressed into generalized advice, and the origin and context disappear together. This matters especially for brands that rely on genuine user word of mouth: your positive reviews may be handled the same way, and you cannot directly control what they are turned into.

### 2.7 Principle 6: Being cited and being named are two different things

Putting the above together, "being cited" and "being named" can be seen as two different mechanisms:

```
Citation: page matches the query → retrieved → listed as a source          (a retrieval problem)
Naming: a claim in the answer needs attribution → source or brand name stated    (an attribution and entity problem)
```

Practitioners' reports from their own tests and first-hand observations by several practitioners all point to the same phenomenon: a web page is used as a source, but the answer names and recommends someone else. No research yet specifically proves the causal mechanism of the two, but the data mentioned above, such as "silent citations", "only 8.3% of brands move from the citation pool into the answer" and "repeated appearance across sources predicts brand inclusion better than traditional SEO quality scores", are consistent with this division.

## 3. How strong is the evidence

| Conclusion | Type of evidence | Strength |
|---|---|---|
| There is a gap between citation and absorption (silent citations; forums cited but rarely used) | Repeated measurement / large-scale audit on real AI search engines | Moderate. Several independent studies point the same way; but the Chinese-platform study comes from an AI visibility vendor, and another is a single snapshot |
| Breadth of citation and depth of absorption diverge (cross-platform comparison) | Descriptive analysis of a static snapshot | Weak. Shows only what is possible in principle; confounders not controlled |
| Invisible use (14–53% of claims uncredited) | Field logs on real engines + controlled replay | Moderate. The range is very wide, and platforms differ greatly |
| About 11% of AIO statements unsupported by sources | 40-day longitudinal measurement on a real engine | Moderate to strong. Covers only Google AI Overviews and popular queries |
| Distortion 30.6%, unsuitability 27.1%, decided by the provider | Real engine APIs + checks against the actually crawled sources | Moderate to strong. Large sample (760,000 citation pairs), but via APIs rather than the user interface |
| Hallucinated URLs 3–13% | Controlled experimental system | Moderate. The authors call it a lower-bound estimate |
| More search calls, lower factual accuracy | Controlled experimental system | Weak. Ablation on only two models, with a model as judge |
| Citation links increase trust, valid or invalid makes no difference | Randomized survey experiment with fixed stimuli | User reactions are real, but the stimuli are fixed, not a real usage situation |
| User preference does not distinguish supporting from unrelated citations | Real engine + crowdsourced preferences | Moderate. Correlation; the unrelated-citation part has only about 800 conversations |
| Testimony generalized, first person deleted | Black-box audit of a real platform | Moderate. Studied only one platform's built-in Q&A |

Scope reminders:

- Most numbers come from English and from Google/ChatGPT/Perplexity-type platforms; there is only one large study of Chinese-language platforms.
- Studies define and calculate "absorption" and "faithfulness" differently, so **numbers cannot be compared directly across studies**; only the direction can be compared.
- One study itself points out that the conclusion that long documents are "overused" is partly an artefact of the measurement method: when the calculation switches to averages, the extent to which short sources are underestimated shrinks considerably.

## 4. Debates and counterexamples

### 4.1 "A citation signals trust" vs "a citation is just a retrieval result"

- **Practitioners widely believe**: when a model cites a source, it trusts that information; when a brand is only mentioned, that shows only that the brand is present. This is a view, not proof.
- **Research shows**: there are large gaps between citation and actual use (silent citations 39.3%), and there is also a great deal of uncredited use. On the user side, people do not even distinguish whether a citation supports the argument.
- Reading them side by side: a citation may reflect "this page matches the query", but does not necessarily reflect "the model adopted its claims". Neither view has direct causal evidence.

### 4.2 Can an FAQ / Q&A format increase absorption?

- A common practical recommendation is to rewrite content in FAQ or Q&A format.
- A descriptive snapshot analysis found that pages in Q&A format had slightly lower absorption (0.0947) than pages not in Q&A format (0.1005); pages containing code, numbers, definitions and comparisons were 41%–77% higher.
- This is correlational data without control for confounders and cannot prove that the FAQ format is harmful. All that can be said is: **there is no evidence that "FAQ formatting in itself increases absorption"**; content density and semantic fit may matter more.

### 4.3 Does more searching make answers better?

- Intuition says that more retrieval means more accurate answers.
- In controlled experimental systems, both models showed "the more search calls, the lower the fact-check pass rate": one fell from 78.6% to 16.7%, the other from 80.0% to 57.9%.
- Another study on real engines also found that one platform's more frequent searching had only mixed effects on answer quality.
- But both pieces of evidence are limited: the former has only two models, the latter is a descriptive observation. For now one can only say that "more retrieval does not necessarily bring more accurate citations".
- Another experiment with a fixed set of candidate documents (weaker evidence) looks at a different metric: the more rounds of reading, the better the documents the agent read represent all the available documents; the average error (stance scores range from −1 to 1) fell from 0.84 in round 1 to 0.41 in round 10, but did not disappear. So "more retrieval" may lower citation accuracy while improving the representativeness of the evidence; these are different metrics, and one cannot conclude that "less searching is better".

### 4.4 Are high-quality sources used more faithfully?

- The sources cited by Google AI Overviews are indeed more credible than first-page results.
- But source quality and faithfulness are almost uncorrelated (about 0.045).
- Faithfulness and suitability also trade off against each other. Optimizing to "make yourself an authoritative source" is not the same as "making sure you are described correctly".

### 4.5 Are deep research agents more reliable than ordinary search?

- Overall, deep research agents have a higher hallucinated-URL rate (10.7%) than search-augmented models (4.8%).
- But one particular deep research product had only 3.5%, below average.
- The difference depends more on the specific system than on the category "deep research".

## 5. Cases

> All the cases below are practitioners' field observations. Those labelled "practitioners report from their own tests" are not independently verified; those labelled "one practitioner observed" are only single leads.

### Case 1: Regular checks of the brand description trace errors to their source

- **What was done**: the marketing lead of a growing startup queried ChatGPT, Claude and Gemini once a month with a fixed prompt set, for example "what does a certain company do", "the best tools in a certain category", "us vs a certain competitor", recording how the models described the company, whom they placed alongside it, and which sources they relied on.
- **What was observed**: twice the models were found repeating outdated or incorrect information; tracing it back showed that the sources were, respectively, a stale directory page and an inaccurate third-party article.
- Evidence strength: practitioners report from their own tests (with a fixed process and repeated checks; not independently verified).
- Related principle: fidelity problems often lie not on your own site but in third-party sources that the AI adopts.

### Case 2: 15 positive reviews, 1 negative review, and the answer discusses only the negative one

- **Platform**: ChatGPT and Gemini.
- **Situation**: a client had accumulated about 15 positive reviews and 1 negative review on a community platform. When ChatGPT was asked about the company, the answer focused almost entirely on the negative review and warned users to "be careful"; Gemini mentioned the negative review but noted that most reviews were positive.
- How it was tested: tested on 5 different devices and IPs, ChatGPT's output was the same every time. After the problem was pointed out in the conversation, the model apologized and corrected itself; but when a new user asked again, it went back to the negative summary.
- Evidence strength: practitioners report from their own tests (repeated across devices; not independently verified).
- Related principle: absorption is not proportional. An answer may amplify a few sources out of proportion. Corrections in a conversation do not change the next answer. Practitioners widely believe that a brand will still be mentioned even when there is negative discussion, but the negative sentiment will be reflected in the description.

### Case 3: Cited, but never named

- **What was done**: a practitioner took 85 B2B software companies, asked 10 buyer-style questions for each, kept to the same engine, and recorded two things for each answer: whether the company was named, and whether the company's own domain was listed as a source.
- **What was observed**: 29.4% of companies were "cited" more often than they were "named". Of these, 9 were named 0 times in 10 answers, yet their own sites appeared in the citation lists. Across the 616 "absent answers" he classified, the types of questions that triggered absence varied with the company's existing visibility.
- His interpretation: the pages answered the question well, so they were pulled in as material; the recommendation lists went to brands with more social proof. He also acknowledges that whether being cited without being named has any effect cannot be attributed.
- Evidence strength: one practitioner observed (a single dataset; can serve only as a lead).
- Related principle: citation and naming are two separate stages.

### Case 4: About 700 pages cited, site name appears only 5 times

- **Situation**: for an English-language news site about three months after launch, about 700 pages were cited by AI, but the brand name was mentioned only 5 times, roughly once per 140 citations. Distribution of citations: ChatGPT 659, AI Overviews 32, AI Mode 22, Gemini 0.
- **His hypothesis**: citation belongs to retrieval (a page that matches the query gets pulled in); naming belongs to attribution (a source is named only when a claim needs a source behind it). Much breaking news is reported by other outlets at the same time, so there is no reason the site must be named.
- Next step planned: produce more original content (its own statistics, numbers no one else has), place the author's name next to the numbers, then compare how often such articles are named. Results have not yet been reported.
- Evidence strength: one practitioner observed (a single site; can serve only as a lead).

### Case 5: The page is used as a source, but competitors are recommended

- **Situation**: a small cycling tour operator's traffic was falling and it was not being recommended by AI. A practitioner set up about 17 prompts for it and monitored them for about two weeks.
- **What was observed**: the client's pages were consistently used as sources, but the answers never mentioned the client's name; instead they drew on the client's guide content and then named and recommended three or four competitors with prices. For one question, the AI used the client's page as the primary source and still recommended others.
- His diagnosis: the problem was not crawling but presentation. The client's brand name was not next to the key sentences, whereas the competitors placed brand, facts and numbers together.
- Evidence strength: one practitioner observed (a single client; can serve only as a lead).

### Case 6: An AI Overview uses your image but lists others

- **Situation**: a practitioner who builds websites for local engineering businesses found that an image from a site he built appeared in a Google AI Overview, but the answer mentioned neither the site nor the business; instead it listed 4 other sites.
- **Evidence strength**: practitioners report from their own tests (a single observation; not independently verified).
- Related principle: content being used and being attributed are separate; invisible use does not happen only with text.

### Case 7: Structured data is correct, but the answer still shows an old price

- **Situation**: a merchant that updates prices hourly had complete and valid product structured data (price, currency, stock), but Google AI Overviews kept showing last month's 99-dollar range instead of the current 79 dollars.
- **Evidence strength**: one practitioner observed (a single case). Several authors in the community share the view that AI Overviews prices depend on the snapshot from the last crawl, but this point remains disputed.
- Related principle: fidelity problems also include "timeliness distortion"; structured markup does not guarantee being read in real time.

### Case 8: Confusion between entities with the same name

- **Situation**: a practitioner pointed out that a site's content was all crammed into one large block of text, with entities mixed together; in addition, there were two apps with the same name on the market (one an e-commerce plugin, the other an image generation tool), and Gemini could not tell which one was meant.
- **Evidence strength**: practitioners report from their own tests (with screenshots; not independently verified). Practitioners widely believe that inconsistent brand narratives prevent models from correctly understanding, categorizing or mentioning a brand.
- Related principle: if absorbed content is attributed to the wrong entity, that is another form of incorrect use.

### Case 9: Cited does not necessarily mean opened

- **What was done**: the author's small-scale tests (method in Chapter 4).
- **What was observed**: the model rarely opened web pages on its own: 16 times in total across 30 sessions of the three question types, and 37 times across 10 sessions of the swimming question; most citations relied only on snippets in the search results. Taking the new site most cited on the swimming question as an example (Chapter 3, Case 8), its pages were cited 25 times (counted by session), and the model opened the page in only 10 of them: the main data page was opened 7 times out of 9 citations; other level pages with the same structure were opened only 3 times out of 10 citations; research articles 0 times out of 5 citations.
- Evidence strength: the author's small-scale tests, one site, 10 questions; weak evidence, suitable only as a case. The API does not show the text the model actually received, so how much the model really read cannot be determined from outside.
- Supporting research: repeated tests on real AI search engines found (using OpenAI native search via the API) that a lightweight model did not open a single web page in 53.6% of sessions; in controlled experimental systems, sessions that read only snippets gave outdated answers (6.4%) and unfaithful citations (6.4%) at higher rates than sessions that opened and cited pages (1.3%, 2.3%). Differences across models and search environments are large (under controlled conditions, the share of sessions with no page opened ranged from 2.6% to 76.0%).
- Related principle: being cited does not mean the full text was read. Implication for writing (an inference): every page needs a passage that can be understood on its own; pages with a uniform structure may let AI cite similar pages with confidence after reading one.

### Other leads (single observations, for reference only)

- One practitioner observed that when asked about the size of a certain community, the model cited an old number from a blog post about 18 months old, rather than the current number.
- One practitioner observed that contacting the sources used in AI answers one by one and asking them to correct incorrect or outdated information succeeded about 70% of the time; after also adding pages on topics the site itself had not covered, the AI's description of the brand slowly improved.
- One practitioner observed that among about 30 companies of similar revenue size, common LLMs missed products, gave vague descriptions, put them in the wrong category, and even attributed products to larger competitors.
- One practitioner reported that in two verticals, models in the decision turn used on average only about 23% of the known brand facts, falling back on general impressions of the category. The data are not public; can serve only as a lead.
- One practitioner reported screenshots showing that Google AI Overviews quotes a passage from a source verbatim and presents it separately from the surrounding answer.

## 6. What to do

### 6.1 Build layered measurement

| Practice | Evidence strength |
|---|---|
| Split results into four layers recorded separately: **mention** (whether the answer text names you), **citation** (whether you are in the source list), **absorption** (whether your content enters the answer), **correct description** (whether the content that enters the answer is faithful) | Several repeated measurements on real engines show large gaps between layers |
| State the denominator clearly for each layer: "all prompts", "prompts that triggered an AI answer", "answers that cite you", or "answers that name you" | Definitions vary widely across studies; this is a methodological requirement |
| Do not use citation counts to represent influence: check both silent citations (listed but not used) and invisible use (used but not listed) | Repeated measurement on real engines |
| Before counting citation share, verify that the cited URLs really exist and resolve | Controlled experimental system (3–13% hallucinated URLs) |
| Also track the share "cited but not named" as a separate metric | One practitioner observed; consistent with the layer gaps in the research |

### 6.2 Monitor and correct descriptions

| Practice | Evidence strength |
|---|---|
| Query several platforms regularly with a fixed prompt set (what the company does, category recommendations, comparison with competitors), recording the description, what you are placed alongside, and which sources are used | Practitioners report from their own tests |
| When you find an error, trace it to the specific source page; errors often lie in third-party directories and old articles, not on your own site | Practitioners report from their own tests; AIO research shows source quality does not guarantee faithfulness |
| Contact the source of the error and request a correction | One practitioner observed (a single lead) |
| Do not rely on correcting the model in a conversation; when the next user asks, the answer may not change | Practitioners report from their own tests |
| Watch for cases where a small amount of negative content is amplified, and check each platform separately | Practitioners report from their own tests; community consensus |

### 6.3 Increase the chance of being "absorbed correctly and named"

| Practice | Evidence strength |
|---|---|
| Include high-density information on the page, such as clear definitions, numbers and comparisons | Descriptive snapshot analysis, correlation only (possible in principle) |
| Put the brand name, facts and numbers in the same sentence or adjacent positions, so claims can be attributed | One practitioner observed (a lead, not verified) |
| Publish original data (numbers others do not have), and make the attribution clear | A hypothesis one practitioner observed; no results yet |
| Use clear paragraphs to avoid entities being confused within one large block of text; deal with distinguishing entities that share a name | Practitioners report from their own tests; community consensus |
| Keep brand information consistent across the web, and reduce outdated or contradictory third-party descriptions | Practitioners widely believe; the Chinese-platform study shows co-occurrence across multiple sources is associated with brand inclusion |
| State uncertainty carefully: answers may turn "possibly" into "certainly", so write key limiting conditions into the claim itself rather than in a separate paragraph | Repeated measurement on real engines shows hedging decreases after search grounding; the writing advice is an inference |

### 6.4 Do not do

- **Do not treat "being cited" as the finish line.** Being cited without being named may amount to supplying material for a competitor's recommendation.
- **Do not treat citation counts as a measure of credibility or results.** Models that cite more are not necessarily more accurate; users also do not distinguish whether a citation supports the argument.
- Do not assume that high-authority sources will be described correctly. Source quality and faithfulness are almost uncorrelated.
- Do not look at only one platform. Distortion and unsuitability are decided mainly by the provider, and platforms behave differently.
- Do not pile up large volumes of unstructured content. One practitioner reported that the brands with the highest visibility are not necessarily used at the decision point (a single lead).

### 6.5 Practices that are outdated or lack evidence

- **"Being listed among the citations counts as success"**: several studies show that citation, absorption and naming are clearly decoupled.
- **"FAQ formatting increases how much content is used"**: there is currently no evidence for this, and descriptive data even point slightly the other way.
- "Structured data lets AI read the latest prices or information in real time": a practitioner observation and community views suggest it does not; this remains disputed and cannot be relied on.
- "Making AI search more makes it more accurate": the opposite trend appeared in controlled experiments (limited evidence).

## 7. Key points

1. "Being seen by AI" has at least four layers: mention, citation, absorption, correct description. Each layer loses some; when measuring, record them separately and state the denominator clearly.
2. Being listed does not mean being used: on Chinese-language platforms about 39% of listed sources are silent citations; forum sources are cited in Google AI Overviews but actually used relatively little.
3. Being used does not necessarily mean being credited: 14–53% of answer claims are supported by search results but carry no citation. Citation counts are not a reliable proxy for influence.
4. Being used does not mean being used correctly: about 11% of AIO statements are unsupported by sources; about 30% of citations distort the original meaning and about 27% of sources are unsuitable; the two trade off against each other and are decided mainly by the search backend.
5. Citations are a persuasion signal: users trust answers more because they see citations, but do not distinguish whether the citations are valid or support the argument.
6. AI generalizes personal testimony: first-person experience is almost entirely erased during synthesis, and selection favours high-scoring, top-level, formal-toned content.
7. Being cited and being named are two mechanisms: practitioners have repeatedly observed "the page is used as a source, but someone else is recommended". Making claims attributable to you is a separate task.
8. The practical priority is to keep monitoring whether descriptions are correct and to trace incorrect third-party sources, not merely to chase citation counts.
