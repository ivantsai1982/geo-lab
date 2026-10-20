# Chapter 12 — Every AI Has Its Own Taste

## Opening: One question, three sets of answers

Imagine: the owner of an online shop selling handmade leather goods asks ChatGPT one morning, "Where can I get a durable wallet made to order?" Her shop is in the answer. She is delighted.

At noon, she asks Gemini the same question. She is not in the answer.

In the evening, she asks a friend to try again with another AI assistant. She has never heard of any of the shops it lists.

Same question, same day, same website. Why do three AIs give three sets of answers?

That is what this chapter is about. The big idea of this chapter fits in one sentence:

**There is no single, unified "AI search" in the world. Each AI platform is an independent librarian, with its own library, its own habits and its own taste. Being recommended by one tells you almost nothing about whether you will be recommended by another.**

This chapter answers five questions:

1. Why do we say there is no single, unified "AI search"? At which of the seven gates do the platforms differ?
2. What tendencies do ChatGPT, Gemini, Google's AI Overviews, Claude, Perplexity and Copilot each have when choosing sources? How reliable are these tendencies?
3. How are Chinese-language AI platforms (the AI Overviews on Baidu's search page, Doubao, DeepSeek, Tencent Yuanbao, Tongyi Qianwen) fundamentally different from English-language platforms?
4. How does the language you ask in change the sources AI cites?
5. When time and people are limited, which platforms should you track and optimize for first?

---

## 1. Every platform has its own seven gates

### The same process, but every platform has different standards

Throughout this book we have said: before AI answers a question, it passes through seven gates. Whether to search, whether it can get in the door, whether it can find you, whether it picks you, whether it mentions you, whether it actually uses you, and whether people come over.

This chapter adds one sentence: **every AI platform has its own set of seven gates, and the standard at almost every gate is different.**

We can draw a question's journey across different platforms as a road that keeps forking:

1. **First fork: whether to search.** Some platforms rarely go online to search and mainly answer from what the model itself remembers. Other platforms search most of the time.
2. **Second fork: which library to search.** The platforms that do search also use different "libraries". Some rely on Google's index, some on Bing's index, and some use their own real-time retrieval systems.
3. **Third fork: which kind of book it prefers.** Once the material is pulled back, each platform prefers different sources: some prefer the platform's own content, some often use forums, some often use videos, and some mainly use generally published web pages.
4. **Fourth fork: what tone it uses.** Finally, when writing the answer, some platforms say "I recommend…" in the first person, while others list items in a neutral tone. Platforms that do not search also reach this step.

Every fork makes the answer more different. At the end of the road, you get different answers, different sources and different brands.

So the same question, on the same day, with the same set of web pages, will get different answers on different platforms. **Being "visible" on one platform gives almost no information about whether you are visible on another.**

### Exactly which gates the differences come from

Below, we go through it gate by gate. Each point says how strong the evidence is.

**Gate one, "whether to search": the gap can be several times over.**

Researchers tested repeatedly on real AI search: they gave the same set of 1,000 questions to two models through the developer interface (API). GPT-5.3-chat went online to search for only 14% of the questions; Claude Sonnet 4.6 searched for 83%.

What does this mean? For the former, most of the time it answers from what it remembers. However well your website has been written recently, it may not have looked at it at all.

One honest caveat: this was measured by replaying questions through the developer interface under controlled conditions. When ordinary people use the website or mobile app, the proportion may be different.

**Gates two and three, "which library, and how much is pulled back": every platform is different.**

Google's products (Gemini and the AI Overviews on Google's search page) mainly rely on Google's own index.

Google has a crawler token called Google-Extended, which websites can use to tell Google "do not use my content for AI training". Researchers tested repeatedly on real AI search and found that websites that blocked this token were cited zero times in Gemini, and were also cited noticeably less in Google's AI Overviews.

However, this is a relationship of "appearing together" (correlation); it cannot yet prove that blocking is the cause (causation).

The amount of material pulled back each time also differs. According to real users' conversation data, ChatGPT pulls back an average of 14.06 URLs per query, while DeepSeek averages only 5.46. In other words, ChatGPT's shortlist is about 2.5 times as long as DeepSeek's.

**Gate four, "whether it picks you": preferred sources differ.**

Researchers found through repeated testing: a large forum community site and YouTube appear in ChatGPT's and Grok's search results, but did not appear at all in Claude's search results. This is an observation as of September 2026.

Platforms also prefer their own things. Google's platforms lean towards citing Google's own assets, such as YouTube. The AI Overviews on Baidu's search page mainly cite Baidu's own sub-sites. The next section covers this in more detail.

**The tone of the answer: the gap is very large.**

On product recommendation questions, researchers found through repeated testing on real AI search:

- 79% of ChatGPT's recommendations were delivered in the first person: "I recommend…".
- Gemini: only 7%.
- Google's AI Overviews: only 2%.

This finding applies only to "product recommendation" questions. Both count as being recommended, but being told "I recommend you" by an AI and being placed in a neutral list feel rather different to the reader.

**Gates five and six, "whether it mentions you, whether it actually uses you": a claim that is still uncertain.**

One analysis compared two numbers across three platforms.

The first number is "the average number of sources cited per question":

- ChatGPT: 6.88
- Google: 12.06
- Perplexity: 16.35

The second number is "on average, how much a fetched web page influences the answer's content" (the bigger the number, the deeper the influence):

- ChatGPT: 0.2713
- Google: 0.0584
- Perplexity: 0.0646

These two sets of numbers can be boiled down to one sentence: **ChatGPT cites less, but each cited source influences the answer more deeply.**

But this sentence needs a big discount. It comes only from one batch of data at a single point in time (researchers call it a "static snapshot"), it is someone else's after-the-fact reanalysis, and other possible influencing factors were not ruled out. It only counts as "description"; at most it suggests "the mechanism might work this way". It is not a law.

---

## 2. Platforms prefer their own things

### This is a structural problem, not a sign your content is bad

Every platform tends to prioritize its own content. This is caused by the platform's own structure and has nothing to do with the quality of your content.

Researchers found several examples on real AI search:

- **Health questions:** the source most often cited by Google's AI Overviews is YouTube. It ranks ahead of the websites of the US Centers for Disease Control and Prevention, the World Health Organization and well-known medical institutions.
- **Google's own three interfaces are very different from one another:** the sources used by Google's traditional search, Google's AI Overviews and Gemini overlap very little. Measured with an indicator called the "Jaccard coefficient", the overlap is only 0.11 to 0.18 (0.18 between AI Overviews and traditional search results). What's more, the two interfaces that write answers lean more towards Google's own assets.
- **Baidu:** the sources that appear most often in the AI Overviews on Baidu's search page are mainly Baidu's own sub-sites.

This "prefer your own" finding is supported by two studies, covering health questions and general questions. Whether it is equally severe in other industries is not yet known.

> **A closer look: What is the Jaccard coefficient?**
> It measures "how similar two lists are". Take the number of items that appear on both lists and divide it by the total number of items on the two lists combined. 0 means no items in common at all; 1 means exactly the same. 0.11 means that of the sources used on the two sides, only about 10% are shared.

### What this means for you

On Google's and Baidu's platforms, "the platform's own content formats" are an entry point in themselves.

But this **does not mean** every brand has to make videos, or open an account on the platform's sub-sites.

Its real use is this: when you analyze "why isn't my web page being cited", first subtract the spots already taken by the platform's own assets. Some spots were never meant for ordinary websites.

---

## 3. How you look determines what you see

There is another often-overlooked source of differences between platforms: **the way of observing itself.** Look at the same platform in different ways, and you see different things.

### The developer interface and the ordinary interface are not the same thing

AI platforms usually have two ways of being used: the website or app that ordinary people use (below called the "ordinary interface"), and the API that developers call from programs.

A large-scale check found that the websites returned by the ordinary interface and by the corresponding API overlap by only 12.0% (ChatGPT) and 14.8% (Gemini).

So **using API results to represent the answers ordinary users see is wrong.**

### Asking once and asking several times are not the same thing

This is what the book calls "rolling the dice".

On ChatGPT, asking only once shows you an average of just 2.65 websites. Ask the same question 3 times, and the cumulative number of websites seen rises to 5.56. Asking only once seriously underestimates the number of sources AI actually uses.

Lists of recommended products also differ each time. Researchers used the Jaccard coefficient to measure how similar the lists are when the same question is asked repeatedly:

- Google's AI Overviews: 0.421
- Gemini: 0.287
- ChatGPT: 0.178

The lower the number, the more different the list is each time. In other words, **ChatGPT's recommended products change the most from one time to the next.**

### Rephrase the question slightly, and the sources change

Researchers slightly rewrote questions and then looked at how much the order of sources changed. They used an indicator called "RBO": 1 means the order is exactly the same, and the lower it is, the more it changed:

- After slightly rewriting the question: Google's AI Overviews scored only 0.49, and traditional search results scored 0.74.
- Same question, rerun on the same device: Google's AI Overviews scored 0.69, and traditional search results scored 0.86.

The conclusion: **AI interfaces that write answers are less stable than the traditional row of blue links.**

### Different model versions, different results

Someone in the industry ran multiple controlled tests themselves and found two examples:

- For the same set of brand-related questions, a fintech company appeared 3 times out of 10 in a larger model. A smaller model, however the question was asked, recommended the same market leader every time.
- In another set of tests, the same company appeared 8 times out of 10 in a larger model; in the raw API without any system settings, it appeared 0 times.

These tests have small samples and only a single client, but they show one thing: different model versions under "the same platform" can also be two different worlds.

### "Being listed" does not equal "being used"

According to real users' conversation data:

- 14% to 53% of answer content is actually supported by search results, but the AI did not mark a citation.
- Another 15% to over 20% of answer content cannot be matched to any source at all.

So if you measure a source's influence only by "whether it was cited", you will both **undercount** (you were used but not credited) and **miscount** (you were credited but not actually used).

---

## 4. The Chinese-language ecosystem is not a translation of the English one

At this point, readers may think: Chinese-language AI platforms are probably just English-language platforms in another language.

They are not. Existing research points to three structural features of the Chinese-language ecosystem.

### Feature one: Baidu's AI Overviews are highly concentrated and prefer Baidu's own sub-sites

Researchers took 500 translated questions and asked each one once in Chinese and once in English on Baidu and on Google (collected only once). The results were:

| Indicator | Baidu (Chinese questions) | Google (Chinese questions) | Google (English questions) | Baidu (English questions) |
|---|---|---|---|---|
| Share of questions showing AI Overviews | 82.0% | 97.6% | 97.0% | 4.0% |
| Source concentration (Gini coefficient) | 0.895 | 0.500 | 0.462 | — |
| Share of citations taken by the top-ranked website | 27.1% | 6.6% | 5.5% | — |

How to read this table:

- Ask Baidu in Chinese, and 82.0% of questions show AI Overviews. Ask Baidu in English, and only 4.0% do.
- The closer the Gini coefficient is to 1, the more citations are concentrated in a few sources. Baidu in Chinese is 0.895, meaning a few websites (mainly Baidu's own sub-sites) take most of the citation spots.
- In Baidu's Chinese AI Overviews, the top-ranked website alone takes 27.1% of the citations. On Google, this number is only 5.5% to 6.6%.

> **A closer look: What is the Gini coefficient?**
> It was originally used to measure whether wealth is distributed evenly. 0 means everyone gets the same amount; 1 means everything is concentrated in one person's hands. Here, it measures whether the "citation spots" are spread evenly across many websites or concentrated in a few.

There is an even more interesting finding. The overlap (Jaccard coefficient) between the websites cited by Baidu and by Google is only 0.008 to 0.034; they have almost no sources in common.

But on the 331 questions where both sides had answers, researchers compared how close the "meaning" of the answers was (using a method called "semantic similarity", where 1 means the meaning is exactly the same). The median was between 0.701 and 0.813, which is fairly close.

In other words: **the two platforms' answers say roughly the same thing, yet the sources they cite are almost completely different.** For brands, the latter is what matters, because who gets cited decides who gets seen.

This study has clear limitations: data was collected only once, the questions were translated, and data was collected from only a single location (Milan, Italy).

### Feature two: the language you ask in matters more than where you are

Researchers studied where Google's AI Overviews cite sources from on health questions.

When questions were asked in English, the share of "local sources" cited varied greatly by country:

- Australia: 48.2%
- United States: 33.7%
- India: 2.3%
- Nigeria: 0.2%

After switching to the local native language, the share of local sources rose by 3.5 to 13.5 times. For example:

- Japan: from 16.6% to 57.5%
- South Korea: from 2.7% to 36.4%

This was observed repeatedly on real AI search, but only for health topics, and it is an observational study, not a controlled experiment.

What this means for Chinese-language content:

- Users who ask in Chinese face a citation pool made up mainly of Chinese-language sources. (But this needs a discount on ChatGPT: research found that the new ChatGPT fast mode searched only in English for about 70% of Chinese questions.)
- The upside: Chinese-language content does not have to compete for the same spots as authoritative English-language websites.
- The downside: the "authority" built up by English-language content does not automatically transfer to Chinese-language answers.

The same study also found: for questions about traditional Chinese medicine, Google's AI Overviews show an answer about 42% of the time; Baidu shows an answer more often, but attaches only about 1 citation on average.

### Feature three: on Chinese-language AI platforms, the gap between "cited" and "actually used" is large

One large-scale study covered four platforms: Doubao, DeepSeek, Tencent Yuanbao and Tongyi Qianwen. Websites and apps were counted separately, making 8 interfaces in total. Researchers asked 614 questions 3 times each on the 8 interfaces, collecting 160,860 citations in total.

The main findings are as follows.

**Where the sources come from:**

- Third-party sources make up about 69%.
- Brands' own official websites make up 12.9%.
- Government sources make up 4.5%.

**Being listed does not equal being used:**

- Of the listed sources, 66% had their content appear in the body of the answer.
- Only 30% were substantively cited.
- Only 8% were cited in depth.
- 39.3% were "silent citations": listed, but not used in the answer at all.

**It is hard for brands to get from the list into the answer:**

Of the brands appearing in the cited sources, only 8.3% ended up actually appearing in the answer.

**Being mentioned by many sources at once is the strongest signal:**

- When a brand appears in only 1 citation, the rate at which it gets into the answer is 2.1%.
- When a brand appears in 11 or more citations, the rate at which it gets into the answer is 59.9%.

**Traditional SEO scores are not the most important factor:**

Researchers took a commonly used third-party composite score for assessing how websites perform on Baidu, put it into a prediction model and looked at how important it was. Its importance came out at only 4.52%.

This shows it is not the main predictor. But note: this **cannot** prove that it is useless.

**Freshness:**

- For highly time-sensitive questions, the median publication age of cited web pages is 18 days; their "half-life" (the time it takes for the chance of being cited to drop by half) is 39 days.
- For questions with low time sensitivity, these two numbers are 101 days and 68 days.

**The app and website of the same platform are also very different:**

The websites used by the app and the website of the same platform overlap (Jaccard coefficient) by only 0.19 to 0.51. For Tongyi Qianwen, compared down to each individual URL, the overlap is only 0.014.

This point deserves its own emphasis: **in the Chinese-language ecosystem, the app and the website of the same brand should be treated as two platforms.**

**How credible this study is:**

The authors of this study come from a company that provides monitoring services, and the data was collected by their own monitoring system. All the findings are only relationships of "appearing together", not causation.

The design of the study (multiple interfaces, each question asked 3 times) is solid in itself. The more reasonable view is to treat it as the most complete descriptive data on Chinese currently available, not as proof of causation.

---

## 5. How reliable are these claims

Put the findings above side by side, and you can see that the strength of the evidence varies a lot:

| Conclusion | How strong the evidence is | Scope and limitations |
|---|---|---|
| The sources used by different platforms overlap very little | Several studies tested repeatedly on real AI search, with consistent results; multiple controlled tests by people in the industry also agree; widely believed in the industry | The most solid one. But the specific numbers vary a lot depending on the measurement method (see Section 6, Debate 4) |
| The gap in how often platforms search is huge (14% vs 83%) | Researchers tested repeatedly on real AI search | Controlled replay through the developer interface; the ordinary interface may differ |
| ChatGPT uses "I recommend" far more than Gemini and Google's AI Overviews | Researchers tested repeatedly on real AI search | Only for product recommendation questions |
| Claude's search results contain no large forum community sites and no YouTube | Researchers tested repeatedly on real AI search; test reports by people in the industry also agree | Observation as of September 2026 |
| Google's platforms prefer Google's own assets | Two studies tested repeatedly on real AI search | Health and general questions; other industries may not show it as clearly |
| Blocking Google-Extended is linked to zero citations in Gemini | Researchers tested repeatedly on real AI search | Correlation only, not causation |
| ChatGPT cites less but uses sources more deeply | Only at the level of simulation and theoretical analysis (after-the-fact analysis of a static snapshot) | Can only say "the mechanism might work this way" |
| Baidu's AI Overviews are highly concentrated | Researchers tested on real AI search | Collected only once, translated questions, collected from only one location (Milan) |
| Asking in your native language greatly increases local sources | Researchers observed repeatedly on real AI search | Health topics only; observational study |
| On Chinese-language platforms, being mentioned by many sources at once predicts whether a brand gets into the answer | Researchers tested repeatedly on real AI search | Correlation only; the authors are a monitoring service company |
| Different model versions differ greatly | Multiple controlled tests by people in the industry | Small sample, only a single client |

The overall judgement comes down to two sentences:

- **The evidence that "platforms are different from one another" is strong.** You can safely take it as a starting assumption when designing how you track.
- **The evidence on "what exactly each platform likes" is much weaker, and it changes quickly.** Treat these only as current observations, and attach the observation date when you use them.

The Chinese-language ecosystem has another obvious gap: almost all the current evidence comes from research, and there are hardly any controlled tests by people in the industry on Chinese-language platforms.

---

## 6. Questions still being argued over

### Debate 1: How much does ChatGPT really rely on forum communities?

Both sides have data.

**One side says: ChatGPT favors forum communities most.**

- Someone in the industry sorted about 150,000 citations by source type and found that ChatGPT leaned most towards forums and Q&A sites (about 5%), and reference and academic pages (about 4%).
- In another set of tests looking at only a single niche, 14 of the 16 community sources cited by ChatGPT came from the same large forum community site.

**The other side says: ChatGPT almost never cites forum communities.**

- Someone in the industry ran multiple controlled tests: asking a fixed set of 40 questions in the same week. That large forum community site was cited 22 times in Gemini and 20 times in Google's AI Overviews, but at most 1 time in ChatGPT.
- Another test spanning 10 industries, with questions related to South Africa: Gemini cited that forum about 750 times, while GPT-5 and Claude both cited it zero times.

Why is this happening? There are three possible explanations:

- The observations were made at different times (the former in July, the latter in September).
- Different things were tested (the API or the ordinary interface, and whether web access was turned on).
- Different industries.

For your own brand, the answer to this question can only be found by testing with your own prompt set. The relationship between platforms and forum communities is discussed specifically in Chapter 15.

One more thing to note: even if a website ranks very high among a platform's cited sources, its share of all citations may still be small. In the tests above, general publications and general web pages made up 86% to 97% on every platform. No platform was dominated by forums or videos.

### Debate 2: Which platform cites the most per answer?

Two sets of data reach almost opposite conclusions:

| Data source | ChatGPT | Google's platforms | Perplexity |
|---|---|---|---|
| A static snapshot study (average citations per question) | 6.88 | 12.06 | 16.35 |
| Tests by someone in the industry (70 questions, 30 days, 1,474 answers; average citations per answer) | 9.62 | Gemini 15.08; Google's AI Overviews 5.34 | 5.04 |

Perplexity is the highest in one set of data and the lowest in the other.

The difference may come from the collection method, the timing, the types of questions, and whether "Google" means AI Overviews or Gemini.

The lesson here is not who is right and who is wrong, but this: **"how many citations each answer has" is a product of the measurement method, and numbers from different studies cannot be compared with each other.**

### Debate 3: Which platform is the most stable?

- Research shows that, for how consistent recommended product lists are when a question is asked repeatedly, Google's AI Overviews are the highest (0.421) and ChatGPT the lowest (0.178).
- Someone in the industry ran multiple controlled tests: 45 emergency repair questions in 15 cities, rerun in incognito mode. About 85% of Perplexity's results stayed the same; about two-thirds of ChatGPT's repeated; for Google, about 60% of cities kept the same recommendations and 40% switched to someone else.

Both show that ChatGPT changes a lot, but they disagree about Google. Possible reasons: one measured product recommendations and the other measured local services; and the latter's Google results also included the effects of personalization.

### Debate 4: How much do platforms really overlap?

Different measurement methods give very different numbers:

| Measurement method | Degree of overlap |
|---|---|
| Research: average websites shared when ChatGPT and Gemini answer the same question | 5.4%; 76.7% of comparisons had no websites in common at all |
| Research: sources of Google's three interfaces (Jaccard coefficient) | 0.11 to 0.18 |
| Tests by someone in the industry (two independent samples cross-checking each other): pairwise overlap of cited websites | 10.6% to 14% between ChatGPT and the other three platforms; about 25% to 26% between Google's AI Overviews and Gemini |
| Tests by someone in the industry: 197 clinics in the same industry, three AI platforms, each question asked three times | 39% to 48% |
| Tests by someone in the industry: overlap in businesses named by Perplexity and Gemini in local recommendation lists (median) | 11% |

Someone in the industry pointed out: if you pool the cited sources for all questions before calculating overlap, the large number of obscure websites that appear only once will drag the number down; if you compare question by question, the overlap may be somewhat higher. So "11%" and "48%" do not necessarily contradict each other; they may just be calculated differently.

One point supported by both independent samples: **ChatGPT has the lowest overlap with other platforms; Google's two products are closest to each other.** Perplexity's position is inconsistent between the two sets of data.

### Debate 5: How quickly is new content reflected?

Many people in the industry believe Perplexity reflects new content faster than ChatGPT, on the grounds that Perplexity relies on real-time retrieval.

One test report by someone in the industry says Perplexity reflected updates within a few days, while ChatGPT took several weeks. Another test comparing multiple models says ChatGPT can reflect content changes in about 2 to 4 weeks.

But this view is still disputed. Its supporters have only their own one-sided observations, and no one has run a controlled test. "Many people believe it" does not equal "it is right".

### Debate 6: Should you build a separate version for each platform?

**The "do them separately" camp:** it is widely believed in the industry that because each platform cites different sources, you must track each platform separately. Someone in the industry found in tests that in about 40% of cases, the brand ranked first on ChatGPT was completely invisible on DeepSeek.

**The "one main version" camp:** someone in the industry observed that although the platforms' sources differ a lot, focusing on doing well in the two indexes of Google and Bing covers most cases more or less. Another person who ran tests pointed out that the way the web page itself is written can be shared across platforms; what really differs by platform is "which external sources decide who gets named".

The two camps can actually be combined:

**Do one version for the readability of the web page itself and a writing style that AI can easily extract from; look at the layout of external sources (where your third-party sources are) platform by platform.**

### Debate 7: Can summaries of "what each platform likes" be trusted?

One test report by someone in the industry drew a "preference profile" for each platform:

- ChatGPT values statistics and forum discussions.
- DeepSeek values freshness of content most.
- Gemini is the most balanced and is more influenced by structured data.

Be very careful with summaries like this, for three reasons:

- One of its points, "adding statistics has the biggest impact on ChatGPT", conflicts with the main thread of this book. The main thread of this book is: the 2023 techniques of "add data, add quotes" no longer work.
- The sample was only 15 web pages over two months, and no control group was made public.
- The sources each platform prefers can change within a few months.

Profiles like this can serve as "hypotheses" when you design your own tests, not as "conclusions".

---

## 7. Real cases

The following cases all come from tests or observations by people in the industry. Each case states its limitations.

### Case 1: After letting AI crawlers in, Copilot's citation curve turned (June to September 2026)

**What was done:** a website dedicated to answering "where can I watch a certain show in my country" covered 34 Asian markets. In June, the site owner had blocked AI crawlers because of bandwidth problems, then later lifted the block.

On the content side, the site owner did two things:

- Built "data-driven" comparison pages using real catalogue numbers, rather than writing opinions.
- Built separate pages for each country.

**On which platform:** Microsoft Copilot. The data came from the AI performance report in a search engine's official webmaster tools.

**What was observed:**

- Within 3 months, it was cited about 185,600 times in Copilot's answers.
- The number of pages cited per day rose from under 100 in June to about 400.
- Over the same period, clicks from traditional search rose from close to zero to about 1,500 a day.
- The site owner said the moment the block was lifted was exactly when the curve began to turn.
- Unexpectedly, the most-cited content was not the originally targeted markets, but comparisons of anime streaming platforms (7 of the top 12 most-cited questions).
- On another type of show-related question, the website's pages supplied 61% to 85% of the sources in the answers.

**The principle behind it:** "whether it can get in the door" is the first real hurdle; platforms go looking for sources that genuinely cover a given market (echoing the language and region points in Section 4).

**Limitations:** this is a test report by someone in the industry, covering only one website, and no one has independently verified it. Also, lifting the block and improving the content happened at the same time, so it is impossible to tell which one caused the change.

### Case 2: See which directory sites each platform cites, then build profiles there (about 1 month)

**What was done:** a service company designed 10 industry-related questions, plus a few questions asking directly about the brand. Each time, using an incognito browser and a new conversation for every question, they asked on ChatGPT, Copilot, Claude, Gemini and Perplexity, and recorded which sources each platform used and who the main competitors were.

Whenever they found that a source was an industry directory site, they went to that directory to create and complete their own profile, and asked clients to leave reviews.

**What was observed:** within one month, they went from not being cited at all to being cited on 3 of the 5 platforms and for 6 of the 10 questions.

The author also believes that Copilot and Perplexity rely more on traditional search rankings, so on these two platforms the only way forward was to improve traditional search rankings.

**The principle behind it:** the differences between platforms lie mainly in "which external sources they cite". So you need to read out the source list platform by platform, then fill the gaps.

**Limitations:** a test report by someone in the industry; no one has independently verified it. "Copilot and Perplexity rely more on traditional rankings" is the author's own judgement, with no control group.

### Case 3: 48 local markets, visibility on four AI platforms (August 2026, a single snapshot only)

**What was done:** 8 mid-sized US cities were chosen, multiplied by 6 business categories, for 48 markets in total.

First, they searched Google Maps for "category plus city" to get a list of businesses (about 97 per market, 4,657 in total). Then they asked ChatGPT, Claude, Gemini and Google's AI Overviews three questions like those a real buyer would ask, and looked at which businesses were named.

**What was observed:**

- Only 11.9% of businesses were named by at least one of the four platforms. With a looser way of matching names, it was 26%.
- Number of businesses named by each platform: Google's AI Overviews 376, ChatGPT 206, Gemini 134, Claude 92.
- Of the businesses named, 70% appeared on only one platform.
- In 36 of the 48 markets, no single business was named by all four platforms.
- The differences between categories were larger than the differences between cities. Share of businesses named: gyms 14.4%, coffee shops 14.1%, hair salons 9.7%.

**The principle behind it:** visibility on different platforms is four separate problems, not four measurements of the same problem.

**Limitations:** a test report by someone in the industry. Only the top 100 map results were taken, so businesses in large markets were underestimated. Matching names strictly versus loosely gave very different results, which the author also pointed out.

**Another related set of tests:** another person in the industry began recording daily from August and accumulated 9,217 answers. They added two points:

- Local recommendation lists are highly concentrated. In 25 of 36 local lists, the same business was listed on over 80% of days.
- For this type of question, Perplexity mainly cites the businesses' own web pages, plus a few directory sites and review sites.

### Case 4: The same news website, cited on hundreds of pages by ChatGPT and not a single page by Gemini (September 2026)

**What was observed:** tracking data for a news website showed about 650 to 659 of its pages cited by ChatGPT, and 0 pages cited by Gemini.

**The author's judgement:** Gemini's problem is not "whether it recognizes this brand", but that it did not pull these web pages back at all. This is a gap at the "whether it can find you" gate, not a problem of "whether it marks your name".

**Supporting evidence:**

- Someone in the industry observed: a large website removed from Google's index was heavily crawled every day by other platforms' crawlers, but Gemini knew nothing about it.
- Another developer observed: in the first month, his website got 230 users from ChatGPT, but Gemini never saw the website.

**The principle behind it:** whether Google's platforms can find you is tied to Google's index (see Section 1). So if you are absent from Gemini, check your status in Google's index first, before talking about content.

**Limitations:** a test report by someone in the industry plus a few first-hand observations; no one has independently verified it. It can only serve as a lead for troubleshooting.

### Case 5: One question, asked of 10 models, produced 29 brands (July 2026)

**What was done:** a Romanian marketing firm asked the same "recommend luxury jewellery brands" question in Romanian. The targets were 10 models: ChatGPT, Claude, Gemini, Copilot, Grok, Perplexity, DeepSeek, Kimi, GLM and Tongyi Qianwen.

The conditions: a clean conversation, no memory, and no brand names mentioned in the question. Each model was asked only once, with no regenerated answers.

**What was observed:**

- Across 50 recommendation slots from the 10 models, 29 different brands appeared.
- 19 of these brands appeared on only one model's list.
- Any two models shared only 0.91 brands on average (about 18%).
- Even the most frequently appearing brand appeared in only 6 models.
- Copilot's list had no overlap at all with the other 9 models. Its answer cited review counts. The author inferred that Copilot mainly relies on Bing's real-time index and review aggregation sites.
- The two brands that made it onto several models' lists had one thing in common: verifiable third-party facts that appeared repeatedly across different sources, and coverage by financial media.

**The principle behind it:** being mentioned together by many different sources is a strong signal for being chosen. This points in the same direction as the finding of the Chinese-language platform study (Section 4, Feature three).

**Limitations:** a test report by someone in the industry. Each model was asked only once, and it has not yet been tested how much each model varies when asked repeatedly. To judge whether "18%" is high or low, you first need that baseline.

### Case 6: The same brand in different model versions (May 2026)

**What was done:** someone in the industry tested questions like "the best project management tools for remote teams" in three places: a larger model, a smaller model, and the raw API without system settings.

**What was observed:**

- The same client appeared 8 times out of 10 in the larger model and 0 times in the raw API.
- The author believes what really made the difference was a 2023 article in a tech publication, together with discussions on two software review platforms from the same period. These older citations had an effect across more model versions, outweighing any recently published content.

**The principle behind it:** different model versions have different training data cut-off dates and different citation behavior (see Section 3). What a model "already remembers" (brand prior) depends on an older and broader presence online.

**Limitations:** multiple controlled tests by someone in the industry, but with only one client. "The old article made the difference" is the author's own inference, with no control group.

---

## 8. What to do

### First, get the measurement right

| Practice | Why | How strong the evidence is |
|---|---|---|
| **Report each platform separately; do not combine them into one "total AI visibility score"** | A total score averages away the very differences you want to see | Researchers tested repeatedly on real AI search; multiple controlled tests by people in the industry also agree |
| **Test in the ordinary interface, not only through the API** | The websites the two use overlap by only 12% to 15% | Researchers tested repeatedly on real AI search |
| **Ask each question at least 3 times** | Asking once seriously underestimates the number of sources (ChatGPT goes from 2.65 to 5.56) | Researchers tested repeatedly on real AI search |
| **Log out, use incognito mode, and start a new conversation for each question** | Otherwise your history will "feed" your brand back to you. Note: what this measures is the result of asking a single round, which is not the same as what users see when they keep asking follow-up questions in the same conversation | Multiple controlled tests by people in the industry |
| **Check whether the platform actually searched this time** | Someone in the industry found that one platform, while logged out, once did not go online to search, answered straight from memory, and misunderstood an abbreviation | Test report by someone in the industry |
| **Fix one prompt set, rerun it weekly by platform, and record the model version and date** | Platforms change; numbers without dates cannot be compared | Multiple controlled tests by people in the industry |
| **Handle "ask directly about the brand" questions separately** | When asked "Is X suitable for Y", the model repeats X back, whether or not it actually found X. This is an echo, not visibility | Multiple controlled tests by people in the industry |
| **Test on another platform first, then decide whether to change the web page** | Someone in the industry ran the same set of 16 questions daily; one entity was cited 25% of the time on one platform, but only 12.5% on Gemini. If the platform itself cites narrowly, changing the web page will not help | Multiple controlled tests by someone in the industry (only a single entity; the author themselves said it is just one data point) |
| **Track the app and website of Chinese-language platforms separately** | The sources the two use differ a lot | Researchers tested repeatedly on real AI search |

### Fill the gaps platform by platform

| Practice | Explanation | How strong the evidence is |
|---|---|---|
| **Read out, platform by platform, which sources your target questions cite, then sort them by "whether you can get on there"** | Split into: your own website, review platforms, communities, open platforms where anyone can post, and competitors' own websites. In tests by people in the industry, usually half to two-thirds of cited web pages are ones you can reach | Test report by someone in the industry |
| **Do not block Google-Extended** (if you care about Gemini and Google's AI Overviews) | Blocking it is linked to zero citations in Gemini | Researchers tested repeatedly on real AI search (correlation only) |
| **When you are absent from Gemini, check your Google index status first** | Whether Google's platforms can find you is tied to Google's index | Several first-hand observations by people in the industry, pointing the same way; can only serve as a troubleshooting lead |
| **Make yourself appear repeatedly across many third-party sources** | In both the Chinese-language platform study and the multi-model tests, this is strongly linked to "being chosen" | Researchers tested repeatedly on real AI search (correlation); test report by someone in the industry |
| **Write in the language of the market you are targeting; write Chinese content in Chinese** | Asking in the native language raises the share of local sources several times over | Researchers observed repeatedly on real AI search (observational) |
| **Build separate pages for each country or market, rather than one generic page** | See Case 1 | Test report by someone in the industry (only a single case) |
| **Keep highly time-sensitive topics updated** | On Chinese-language platforms, the median publication age of web pages cited for highly time-sensitive questions is only 18 days | Researchers tested repeatedly on real AI search (correlation) |
| **Publish content aimed at "describe the problem" type questions** | Several sets of tests found that when users describe a problem rather than naming a product category directly (for example, "how do I get clients to pay faster"), most platforms do not recommend any specific product | Test report by someone in the industry |
| **In Baidu's ecosystem, treat Baidu's own sub-sites as a structural given** | They take up a considerable share of the citation spots | Researchers tested repeatedly on real AI search; but there is no controlled evidence yet on exactly what to do |

### How to choose when time and people are limited

- Someone in the industry, based on observations of 100 to 150 website analytics accounts, believes ChatGPT and Gemini bring the most referral traffic. Another person in the industry observed that 98% of one client's AI traffic came from ChatGPT. These are all one-sided observations. And the main thread of this book points out: no research has yet proven that GEO reliably brings traffic.
- The more robust approach: first use your own prompt set to measure how absent you are on each platform, and why. Is the reason "it can't find you" (a retrieval gap), or "it found you but didn't pick you" (a selection gap)? Then, based on which platforms your audience actually uses, set the order in which you invest.
- If you target Chinese-speaking users, at least include the AI Overviews on Baidu's search page and the main Chinese-language AI platforms in your tracking. Do not rely only on conclusions drawn from English-language platforms.

### Do not

- Do not use a screenshot from one platform to infer how you perform on all platforms.
- Do not carry a success from one platform straight over to another. In particular, tests show that advice aimed at Google's interfaces does not carry over.
- Do not treat API results as the answers users see.
- Do not treat the result of asking once as the system's fixed output.
- Do not treat "listed as a citation" as "used in the answer". On Chinese-language platforms, 39.3% of citations are silent citations.
- Do not treat any "preference profile of each platform" as a stable rule.

### Outdated ideas

- **Treating "optimizing for AI search" as a single goal.** Platforms differ in whether they search, where they search, which sources they prefer and what tone they use. A vague overall goal cannot tell you what to do next.
- **Looking only at traditional search rankings to infer your visibility in AI.** Several sets of industry tests found that brands ranking well on Google were absent from AI answers. On Chinese-language platforms, the traditional quality score also has low predictive importance. Traditional rankings are still a prerequisite for "whether it can find you" on some platforms, but they cannot stand in for your visibility in AI.

---

## 9. Key points of this chapter

1. There is no single, unified "AI search" in the world. Platforms differ in whether they search, which library they search, which sources they prefer and what tone they use in answers. The same question gets different sources and different brands.
2. The sources used by different platforms overlap very little; this is the point with the strongest evidence in this chapter. ChatGPT has the lowest overlap with other platforms; Google's two products are closest to each other.
3. Platforms prefer their own assets: Google's platforms lean towards their own content such as YouTube, and the AI Overviews on Baidu's search page lean towards Baidu's own sub-sites.
4. The way you observe creates differences by itself: the ordinary interface versus the API, asking once versus asking several times, different model versions — each shows something different. So test in the ordinary interface, ask each question several times, and record the date and version.
5. Baidu's Chinese AI Overviews are highly concentrated (Gini coefficient 0.895, with the top-ranked website taking 27.1% of citations), and their sources barely overlap with Google's, even though the meaning of the answers on both sides is very close.
6. The language a question is asked in decides which sources AI cites more than where the person is. Asking in the native language raises the share of local sources several times over.
7. On Chinese-language AI platforms, being listed as a citation does not equal being used; only 8.3% of brands get from the cited sources into the answer; being mentioned by many sources at once is the most strongly linked signal. The app and website of the same platform should be looked at separately.
8. The evidence on "what exactly each platform likes" is weak and changes quickly; attach the observation date and use it only as a hypothesis. In practice: write the web page itself one way; look at the layout of external sources platform by platform.

---

## Remember in one sentence

**There is no one thing called "AI search", only one different librarian after another; write your web pages once, but check and fill in your third-party sources one platform at a time.**

## What you can do tomorrow

1. **List the AI platforms your audience actually uses.** If you have Chinese-speaking users, add the AI Overviews on Baidu's search page and the main Chinese-language AI platforms, and list the app and website separately.
2. **Prepare a fixed prompt set.** Include plenty of "describe the problem" type questions (for example, "how do I get clients to pay faster"), and put questions that ask directly about the brand in a separate group, not counted together with the others.
3. **Ask the right way.** Use the ordinary interface, not only the API; log out, turn on incognito mode, and start a new conversation for each question; ask each question at least 3 times; confirm that the AI actually searched online this time.
4. **Record results for each platform separately.** Do not calculate a total score. Record the date and model version every time, and rerun weekly by platform.
5. **Read out the list of sources each platform cites.** Sort them by "whether you can get on there": your own website, review platforms, communities, open posting platforms and competitors' websites. Start filling from the half to two-thirds you can reach, for example by building a profile on industry directories and asking clients to leave reviews.
6. **Work out why you are absent.** Is it "it can't find you", or "it found you but didn't pick you"? Before changing your web pages, test on another platform first; if the platform itself cites narrowly, changing your web pages will not help.
7. **If you are completely absent from Gemini,** first go to Google Search Console and check your status in Google's index. If you care about Gemini and Google's AI Overviews, do not block Google-Extended.
8. **Find ways to appear in many different third-party sources**, with verifiable facts and coverage.
9. **Write in the language of the market you are targeting; when needed, build separate pages for each country or market.**
10. **Update highly time-sensitive topics regularly.** On Chinese-language platforms, the median publication age of web pages cited for this type of question is only 18 days.
11. **If you target Baidu,** accept first that Baidu's own sub-sites will take some of the spots, and factor this into your analysis.
12. **When setting priorities,** first measure how absent you are on each platform and why, then decide where to start based on the platforms your audience actually uses.

## Stop doing this

- Stop using a screenshot from one platform to infer performance on all platforms.
- Stop carrying a successful approach from one platform (especially Google's interfaces) unchanged to another platform.
- Stop treating API results as the answers ordinary users see.
- Stop drawing conclusions after asking only once.
- Stop treating "listed as a citation" as "used in the answer".
- Stop believing that any "preference profile of each platform" is a stable rule.
- Stop treating "optimizing for AI search" as a single goal.
- Stop looking only at traditional search rankings to infer your visibility in AI.
- Stop combining all platforms into one "total AI visibility score".

## What is still uncertain

- **How much does ChatGPT really rely on forum communities?** Both sides have data, with opposite conclusions. It may depend on observation time, measurement method and industry. You can only test it with your own prompt set.
- **Which platform cites the most per answer?** Different data give opposite rankings. This number depends on the measurement method and cannot be compared across studies.
- **Which platform is the most stable?** There is broad agreement that ChatGPT changes a lot; on whether Google is stable, the two sets of data disagree.
- **How much do platforms really overlap?** Numbers range from 5.4% to 48%, depending on the calculation. The only consistent points are: ChatGPT has the lowest overlap with other platforms, and Google's two products are closest. Perplexity's position is still uncertain.
- **How quickly is new content reflected?** "Perplexity is faster than ChatGPT" is the view of many people in the industry, but there has been no controlled test.
- **Should you build a separate version for each platform?** The more reasonable compromise at present is "one way of writing web pages, with external sources looked at platform by platform", but both camps have observations supporting them.
- **The "preference profiles" of each platform** have small samples and no control group, and one of their points conflicts with the main thread of this book; they can only be used as hypotheses.
- **"ChatGPT cites less, but uses sources more deeply"** comes only from an after-the-fact analysis of one snapshot; we can only say the mechanism is possible.
- **Is blocking Google-Extended the cause of zero citations in Gemini?** For now we only know the two are linked, not whether it is causation.
- **In Baidu's ecosystem, what exactly should you do about Baidu's own sub-sites taking up spots?** There is no controlled evidence yet.
- **There is very little test evidence on Chinese-language platforms.** Almost all of it currently comes from research, the most complete of which comes from a monitoring service company and shows only correlation.
- **Do old media articles really influence models more than new content?** This is the author's own inference from a single case.
- **Can GEO reliably bring traffic?** No research has proven it yet.
