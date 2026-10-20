# Chapter 2 — If AI Never Goes to Look, It Doesn't Matter How Well You Write

## Let's start with a scene

Imagine (this is a hypothetical scenario): a business owner runs an office cleaning company. Her website was rebuilt just last year.

The pages are clean, they load quickly, the service descriptions are crystal clear, and the FAQ is well organised too.

One day, she asks an AI: "Which office cleaning companies do you recommend?"

The answer lists four companies. She is not one of them.

She goes back and revises her website again, adding more explanation. A month later she asks again. She is still not in the answer.

The problem may have nothing to do with her website at all.

The problem may be this: **when the AI answered that question, it never went online to look.**

If the AI doesn't go and look, it won't read any web pages. However well your pages are written, they are like a book sitting on a shelf that nobody ever opens.

This chapter makes just one point:

> Before AI answers a question, it first decides "whether to go and look." This is the first of the seven gates. If this gate isn't passed, none of the later gates ever happen.

When people talk about AI visibility, the first thing they often ask is "What's my ranking?" But the first gate isn't ranking. It's "whether to look."

```
Whether to search → Can it get in the door → Can it find you → Does it pick you → Does it mention you → Does it really use you → Will people come
    ▲
This chapter
```

---

## Five questions this chapter will answer

1. When AI products answer questions, what proportion of the time do they actually go online to look?
2. Who decides whether to look: the product, the model, or the way the user asks?
3. Which ways of asking make AI more likely to look? Which almost never do?
4. If users ask for "list your sources" in the question, can that make AI go and look?
5. For people doing GEO, how can you tell whether your target questions are a "search battle" or a "memory battle"?

---

## 1. The first gate: will the librarian get up and go through the books?

The whole book uses the same metaphor: **AI is like a very busy librarian.**

You ask him a question, and he has two ways to handle it.

**Option one: answer directly from memory.** He has read a lot of books and remembers plenty, so he just answers. In this case, the answer usually comes with no sources at all.

**Option two: get up and go to the shelves to find material.** He first rewrites your question into a few phrasings suited for searching, then finds web pages, filters them, and finally writes an answer with sources attached. Only on this path does he have any chance of picking up the book you wrote.

As a diagram, it looks like this:

```
User asks a question
   │
   ▼
[Whether to search]──No──▶ Answer using only what was memorised in training ──▶ Usually no citations at all
   │
   Yes
   ▼
Rewrite the question → Find web pages → Filter → Write the answer and cite
```

All the effort you put into your web pages only matters on the second path.

So, before asking "How do I get AI to recommend me?", you need to ask a more basic question: **for the questions I care about, will AI actually go and look?**

---

## 2. Who decides whether to look?

This decision is not fixed. It is decided by three things together:

1. **The product and platform settings.** Some AI products look every time; some let the model decide for itself.
2. **The model's own habits.** For the same question, some models are very willing to look, while others avoid looking whenever they can. The difference is large.
3. **The form and topic of the question.** Questions phrased as questions, long questions and questions that need up-to-date information are more likely to make AI go and look.

Researchers describe this structure as "the product's outer settings" and "the model itself" deciding together: the product gives the model a set of instructions and tools from the outside, and under those instructions, the model then judges for itself whether to look.

In other words, whether to look is partly a rule set by the platform, partly the model's own judgement, and partly down to how the user asks.

---

## 3. The differences are bigger than you'd imagine

You might assume that different AIs look things up at roughly similar rates.

That is not the case at all. **The "trigger rate"**, meaning the proportion of the time AI decides to look, cannot be summed up with a single "industry average." It varies enormously depending on the product, the model and the questions used for testing.

### Between conversational AI products

Researchers ran repeated tests on real AI search, putting **the same set of 1,000 questions** to two models:

- GPT-5.3-chat: looked only **14%** of the time.
- Claude Sonnet 4.6: looked **83%** of the time.

Same questions: one mostly relies on memory, the other mostly goes through the books.

There are also two independent studies that measured ChatGPT repeatedly:

- The first study measured continuously for 45 days and found that **57.8%** of answers had no citations at all.
- The second study found that **75.8%** of questions did not make ChatGPT go and look, meaning about three-quarters.

The second study also broke down the reasons for "not looking":

- **69.4%** were cases where the model judged "this question doesn't need a search", which the researchers called intent misjudgement.
- **30.6%** were cases where the model refused to answer outright for safety reasons.

### Google's AI Overviews

The AI-written answer at the very top of the search results page is what this book calls the **AI summary**. It doesn't appear every time either. Three studies measured very different appearance rates:

| Questions used for testing | Overall appearance rate | Of which, questions | Of which, non-questions |
|---|---|---|---|
| 55,393 popular searches | 13.7% | 64.7% | 9.5% |
| Sample of public real search logs | 51.5% | 89.9% | 51.9% |
| Real browsing history of 900 US adults | About 18% | (not counted separately) | (not counted separately) |

The highest and lowest figures differ by nearly 4 times.

Why such a big difference? Mainly because the questions tested were different.

- Popular searches include many queries "looking directly for a particular website" and very short keywords, and AI summaries rarely appear for those.
- Real search logs typed in by ordinary people contain more long queries and questions, and AI summaries appear often for those.

So the question "What is the appearance rate of AI summaries?" is meaningless in itself.

What you should really ask is: **"What is the appearance rate for the type of questions I care about?"**

---

## 4. The most reliable pattern: questions and long queries are most likely to make AI step in

Of all the conclusions in this chapter, this one is the most solid. All the relevant studies point in the same direction:

**Questions and long queries are more likely to trigger AI answers.**

Specifically:

- In the popular-search sample, questions showed AI summaries **64.7%** of the time, while non-questions did so only **9.5%** of the time, a difference of nearly **7 times**.
- In the real search-log sample, the appearance rate for questions was as high as **89.9%**.
- In real people's browsing history, queries that were more likely to trigger had three features: they were longer, started with a question word (such as "how", "why", "where"), and contained both a noun and a verb.
- Split by user intent: about **60%** of questions got an AI answer, about **37%** of statements, and about **12%** of queries "looking directly for a particular website."

The least likely to trigger are these queries "looking directly for a particular website", which the industry calls **navigational queries**. For example, searching directly for a brand's official website.

The logic is intuitive: the user wants a web address, not an explanation. If someone searches "so-and-so brand official website", AI has no need to write an essay for them.

So if you only track your own brand name, you are looking at exactly the area where AI steps in the least.

---

## 5. When the platform changes its policy, your visibility changes with it

Whether to look is not just the algorithm's "judgement" about a question. It is also the platform's "policy."

Researchers repeatedly captured Google's AI summaries on real AI search across years and saw several changes:

- The number of countries covered by AI summaries expanded from **7** in 2024 to **229** in 2025.
- Among US queries, the appearance rate of AI summaries rose from **42%** to **67%**.
- For COVID-related queries, the appearance rate of AI summaries went from **1%** in 2024 to **66%** in 2025. However, this item looked at only **74** queries, a very small sample.

This reminds us of one thing: **the visibility of a topic can suddenly change dramatically because of a single platform adjustment, and this has nothing to do with anything you did.**

If one day you notice that exposure for a certain type of question has suddenly surged or dropped, don't rush to blame yourself. First check whether the platform has changed how it handles "whether to show an AI answer" for that type of question.

---

## 6. If you tell AI to "list your sources", will it go and look?

Many people monitoring AI visibility like to add the line "List your sources" at the end of their questions.

The effect of this line depends on where you ask.

First, let me explain a term. Besides the chat products that ordinary people use, AI companies also provide an interface that developers call from their programs, which the industry calls an **API**. A lot of monitoring work is done automatically through APIs.

Researchers ran a controlled test on real AI search:

| Scenario | Without "List your sources" | With it added |
|---|---|---|
| API (model decides for itself whether to look): proportion that looked | 12.1% | 88.4% |
| API: average number of sources cited per answer | 0.60 | 7.05 |
| Product used by ordinary people (free, not logged in): average number of sources cited per answer | 16.6 | 19.9 |

On the API, a single line took the proportion that looked from about one in eight to nearly 90%.

But on the product ordinary people use, adding the line or not made little difference. The mix of cited sources also changed by no more than **2.1 percentage points**.

This gives people doing GEO two reminders:

1. **If you use the API for visibility monitoring, the way you phrase questions can seriously distort the results.** What you measure may not be the real situation.
2. **Most real users don't add instructions like this.** So don't use "results after adding the instruction" to estimate what real people actually see.

---

## 7. Even if AI looks, that doesn't mean you've won

One last reminder.

If AI goes and looks, that only means your content has "a chance" of being used. It doesn't mean you'll definitely be cited, let alone that your content will be used correctly.

This is what research has seen:

- Research found that **14% to 53%** of the claims in answers were actually supported by retrieved material but had no source marked. In other words, AI used content from certain web pages but didn't mention them.
- Another **15% to over 20%** of claims could not be matched to any search result.
- Models that look more often did not give better-quality answers across the board; they were better in some respects and worse in others.

So "going to look" is a **necessary condition** for being seen, not a **sufficient condition**.

Once the librarian gets up, it still depends on whether he can reach your shelf, whether he picks up your book, whether he mentions you in the answer, and whether he gets it right. These are the gates the following chapters deal with.

---

## 8. How reliable is this evidence?

| Conclusion | Where the evidence comes from | Reliability |
|---|---|---|
| The proportion of looking varies hugely between models (14% vs 83%) | Researchers' repeated tests on real AI search; plus real conversation logs from 613 users, 171,264 conversations in total | Strong. But only specific model versions were compared; once versions update, the numbers will change |
| ChatGPT does not look a large proportion of the time | Two independent studies measured repeatedly on real commercial products | Strong. But the two studies define things differently: one looks at "no citations at all", the other at "did not look". The two numbers cannot be directly added or compared |
| Questions and long queries are more likely to trigger AI summaries | Three independent studies, with samples ranging from popular searches and real search logs to real people's browsing history | Strong. All three point the same way; this is the most reliable conclusion in this chapter |
| Platforms adjust by topic whether to show AI answers | Researchers' repeated captures on real AI search across years | Medium. The COVID example had only 74 queries |
| The wording of a question can change the proportion of looking on the API | Researchers' repeated tests on real AI search, comparing the API with the regular product | Medium to strong. But only tested on the topic of mental health; other topics have not been verified |

**When using these numbers, remember three limitations:**

1. Most of the data comes from specific model versions in 2025 to 2026. Whether to look is a decision made by the product side and will change as versions update.
2. The research on Google AI summaries focused mainly on US or English-language queries.
3. Most research on conversational AI used APIs or conversation logs volunteered by users. This may differ from real use, where users are logged in, the AI remembers who you are, and it personalises for you.

---

## 9. Where there is no settled conclusion yet

### Controversy 1: Do comparison and purchase questions actually trigger a search?

This is the most obvious contradiction in this chapter. People in the industry have tested it themselves, but reached exactly opposite conclusions.

**One side says: it looks almost every time.**

Someone in the industry ran multiple controlled tests themselves. He tested about **2,000** purchase questions about business software and developer tools, such as "the best X", "X vs Y" and "tools for doing Z". Over one month, the proportion with at least one citation was:

- ChatGPT: **95%**
- Google AI summaries: **99%**
- Perplexity: **100%**

Note that this is a very narrow question set, containing only business software.

**The other side says: the more specific the question, the less it looks.**

Another person in the industry also reported his own tests. He tested consumer products via the API with web search turned on, but let the model decide for itself whether to look. On ChatGPT:

- For questions like "Brand A vs Brand B", **76 out of 80** did not look at all.
- For questions with a personal situation, like "I have a certain physical condition; which mattress should I buy?", **106 out of 120** did not look.
- For broad category questions like "the best camera backpack for hiking", about **half** looked.

Both sides have their own grounds, and for now **we cannot force a judgement on who is right**. There are three possible explanations:

- **Different categories.** Software tools update quickly, so the model may judge that it needs fresh information; for brand comparisons of consumer products, the model may think what it remembers is enough.
- **Different question shapes.** "X vs Y" names two brands directly, so the model may think it already knows the answer; "the best X" requires listing a set of options, which needs more outside information.
- **Different measurement methods.** The first side looked at "whether a citation appeared"; the second side looked at "whether it looked", as reported by the API.

The first person in the industry offered a view worth remembering: **whether AI looks is mainly a characteristic of the "question", not of "which AI".**

If you test with a prompt set that mixes in lots of "What is X" (definition) and "How to do Y" (how-to) questions, a given AI's "average trigger rate" will naturally be pulled down. That doesn't necessarily mean this AI doesn't like to look; it means the questions you chose are ones it thinks don't need a search.

### Controversy 2: Product cards and "looking" are not the same thing

Someone in the industry reported: among more than 10,000 shopping-related questions, **93%** of purchase-intent questions made ChatGPT pop up a row of product cards, while only **15%** of comparison questions did.

Another person in the industry observed a similar pattern: **93%** of "about to place an order" questions showed product cards, while only **2.8%** of "after the purchase" questions did.

But these numbers cannot be used to answer "Will AI go and look?" Product cards are a different form of answer. According to the reports, they depend mainly on structured product data provided by merchants, not on web page content.

Moreover, the people who put forward these numbers work in related businesses themselves, and the numbers have not been independently verified.

### Controversy 3: Are research questions all answered from memory alone?

Someone in the industry observed: for research-oriented and knowledge-oriented questions, AI mostly answers from what it memorised in training and doesn't look, so your Google ranking is almost irrelevant. Only purchase questions, such as "the best X in a certain place" or "top suppliers for doing Z", make it look, and in those cases the link to search rankings is clearly higher.

This is consistent with the view in Controversy 1 that "definition and how-to questions are answered directly from memory." But this is only a single observation and can only be treated as a clue.

### Controversy 4: If you ask something very complex, can you make AI do "deep research"?

Someone in the industry observed: no matter how complex the question is, the model does not, because of that, start the kind of mode where it digs into material step by step, round after round, on its own.

On the surface, this contradicts Section 6's point that "wording can greatly change the proportion of looking on the API."

A possible explanation: wording can change "whether to look", but not necessarily "how deep to look." No research has directly tested this yet.

---

## 10. A few real observations

Most of the observations below come from people in the industry testing things themselves and have not been independently verified. Please treat them as clues.

### Observation 1: For the same company, search on and search off are two different worlds

**What happened:** A service company found that when people asked ChatGPT "Who can do X?", it was mentioned only about **6%** of the time.

It first checked its own website: all crawlers got normal responses, and there were no technical problems. But after revising the pages, nothing changed.

**How it was diagnosed:** Another person in the industry suggested a "search on / search off" comparison test: ask the same question once with web search turned on and once with web search turned off.

This person said he had used this method to score about **180** companies. The companies named by AI were usually not the ones with the cleanest websites, but those that **often appeared in "X vs Y" comparison articles written by others**.

**What was seen:** Someone in the industry followed this and found that with search on, the company was cited about **16%** of the time; with search off, it was **0**.

**What this means:** This company's visibility came entirely from AI looking things up in the moment. In what AI memorised during training, it currently does not exist.

So it makes sense that revising its own pages had no effect. The answers to this type of question come mainly from comparison and roundup articles written by third parties, in other words **third-party sources**, not from your own pages.

You can use this simple flow to assess your situation:

```
Ask once with search off → Are you mentioned?
   ├─ Yes → You are already in AI's memory; this is a long-term asset
   └─ No → Turn search on and ask again → Are you mentioned?
              ├─ Yes → You rely on AI looking things up in the moment;
              │        the key is the "third-party sources" it finds
              └─ No → You're not on either path;
                       first deal with "Can it get in the door" and "Can it find you" (Chapters 3 and 4)
```

### Observation 2: The same local business looks completely different on different AI products

Someone in the industry observed: the same local business had **0%** visibility when the model answered only from internal knowledge. After web search was turned on, some AI products started recommending it consistently, while others still didn't mention it at all.

This shows that "AI visibility" is not a single number. You first need to figure out whether and how each product looks things up before you can talk about optimisation.

### Observation 3: A brand-new name can only be seen through "looking in the moment"

Someone in the industry observed a very clean example: a brand-new entity, which appeared later than the training cut-off date of every model, could still be cited in AI answers.

Server logs showed that the crawlers responsible for collecting training data were kept out the whole time during the test period; the type that fetches web pages in real time at the moment of answering could read the content normally.

This is a clean comparison: AI's training memory could not possibly contain it, so the only way it could be cited was because AI looked it up at the moment of answering.

For new brands and new products, this matters a lot: **whether AI is willing to look is your only route to exposure.**

### Observation 4: When monitoring visibility via the API, you may be measuring something else

**What was done:** Someone in the industry used the API to track weekly visibility across several AI products. Each model collected about **285** answers per week, for **4 weeks**.

**What was seen:** When "whether to look" was set to "auto", leaving it to the model to decide, for most product-recommendation questions the model answered directly from its existing impressions and didn't look at all. As a result, the "web-connected group" and the "offline group" were almost identical; only by forcing the model to look could the two groups be told apart.

**Another finding:** The web-connected group's results fluctuated more from week to week than the offline group's, by an estimated **3 times** or so. But with only 4 weeks of data, the plausible range for this multiple is roughly from **1 to 11 times**, so the uncertainty is high. For the same set of questions, visibility rose from **0.226** to **0.285** within one week.

**A similar report from another person in the industry:** They collected answers on four AI products. ChatGPT in auto mode gave no citations at all for any of the pilot questions and finished answering in about **4 seconds**; the other products looked things up in real time and took **15 to 40 seconds**. However, this person works in AI visibility services himself, and his ChatGPT sample was only **18 out of 280 questions**, so it shouldn't be taken too seriously.

---

## 11. Which battle are you fighting?

Putting everything above together, you are actually facing two different battles:

**The memory battle:** AI doesn't look, and answers from what it memorised in training. However good your web pages are, it can't read them. In this case, the only way is to be mentioned over the long term in other people's articles, reviews and discussions, and slowly get into the memory of future versions of AI.

**The search battle:** AI does look. Only then do web pages and third-party sources start to have an effect, and only after that do the later gates come into play.

The same brand may be fighting different battles on different questions and different AI products. Sort that out first, then take action.

---

## Remember in one sentence

AI first has to decide "whether to go and look"; if it doesn't look, no one reads your web pages, however well written. And whether it looks depends mainly on what the question looks like, and also on which product and model it is.

## What you can do tomorrow

1. **Categorise the questions you care about.** Split them by form: question or non-question, long or short. Then split them by intent: asking for a definition, asking how to do something, category comparison, brand comparison, looking for an official website (navigational). Record separately for each type whether AI looks. (That the way a question is asked affects whether AI looks is consistently supported by large-scale repeated testing; grouping by intent is the approach used in multiple controlled tests by people in the industry.)
2. **Focus on questions and long queries.** These are the most likely to trigger AI answers and are the range where GEO can have an effect. (Researchers' repeated tests on real AI search; three studies point the same way.)
3. **Do a "search on / search off" comparison.** Ask the same question once with web search on and once with it off, to judge whether your absence is because you're not in AI's memory or because you weren't found. (Someone in the industry used this method to score about 180 companies, but no one has independently verified it.)
4. **Flag answers with "no citations at all" separately.** This is a simple signal for judging whether AI looked. Someone in the industry tested this themselves: among 406 offline answers, the number of citations was zero in every case.
5. **Monitor each AI product separately.** Don't assume they behave the same way. The differences between models are large; this is supported by researchers' repeated tests on real AI search. The specific numbers come from tests by people in the industry: Gemini looked 493 times out of 500; Perplexity looked all 500 times; answers that didn't look came almost entirely from ChatGPT (343 of 406 offline answers).
6. **When monitoring via the API, spell out the search settings.** Record whether it was "forced to look" or "auto", and keep the two separate in your reports. (This is a test report from people in the industry; that the API and the regular product differ is supported by research.)
7. **When interpreting data, factor in changes to platform policy.** When a topic's visibility suddenly changes dramatically, first check whether the proportion of AI answers appearing for that topic has changed. (Found by researchers' repeated tests on real AI search across years.)
8. **For questions AI doesn't look up, accept that it's a long-term battle.** For this type of question, the only way is to keep being mentioned in third-party sources and slowly get into the training data of future versions. (This is inferred from how the system works; many in the industry believe third-party comparison content is key, but "many believe" does not equal "proven".)

## Stop doing this

1. **Don't evaluate an AI product with a single "average trigger rate".** Whether it looks depends mainly on what questions you ask it.
2. **Don't add words like "list your sources", "latest" or "2026" to the questions you use for monitoring**, unless that's exactly the scenario you want to test. Someone in the industry tested this themselves: words like these greatly increase how often AI looks, but most real users don't ask this way.
3. **Don't treat results from the API's "auto" mode as "web-connected visibility".** It may mostly be what AI memorised in training, or a mix of the two in unknown proportions.
4. **Don't think that revising your own pages can change the answers to questions AI doesn't look up.** For this type of question, AI doesn't read your pages at all.
5. **Don't treat the appearance rate of product cards as the proportion of the time AI looks.** They are different mechanisms.

**Outdated ideas:**

- **"Ranking first on Google means AI can see me."** For questions AI doesn't look up, search rankings and AI answers are almost unrelated. Even when AI does look, the overlap between the sources cited in AI answers and the pages on the search results page is low (later chapters explain this in detail).
- **"I only need to track searches for my brand name and official website."** These navigational queries are exactly the type where AI answers appear least.

## What is still uncertain

1. **Do comparison and purchase questions actually trigger a search?** Test results from people in the industry contradict each other, and there is no settled conclusion yet. A more reasonable view is: whether AI looks is mainly a characteristic of the question, not of the AI product. But this is still a view, not a settled conclusion.
2. **Are the product-card numbers credible?** The people who put forward the numbers work in related businesses themselves, and the numbers have not been independently verified; besides, product cards and "looking" are two different things to begin with.
3. **Are research questions all answered from memory alone?** Currently supported by only a single observation; it can only be treated as a clue.
4. **Can complex phrasing make AI look deeper?** One observation says no. Wording can change "whether to look", but whether it can change "how deep to look" has not been directly tested by any research yet.
5. **Does the effect of "list your sources" hold for other topics?** So far it has only been tested on the topic of mental health.
6. **Will these numbers go out of date?** Very likely. Most come from specific model versions in 2025 to 2026; whether to look is a decision made by the product side and may change as soon as versions update. The research on Google AI summaries also focused mainly on US or English-language queries; other languages and markets remain uncertain.
7. **Is there a gap between research conditions and real use?** Most research on conversational AI used APIs or logs volunteered by users, which may differ from real use, where users are logged in and there is memory and personalisation.
8. **How large are the fluctuations in web-connected results, really?** The estimate is about 3 times, but with only 4 weeks of data, the plausible range is from 1 to 11 times, so it's hard to say.

## Chapter recap

1. "Whether to look" is the first of the seven gates. If AI doesn't look, web page content has no chance of being read.
2. The proportion of looking varies enormously: for the same set of questions, one model looked only 14% of the time, another 83%; the appearance rate of Google AI summaries ranges from 13.7% to 51.5%, depending on the questions tested.
3. The most consistent pattern: questions and long queries are the most likely to trigger AI answers, and navigational queries the least likely.
4. Platforms actively adjust their approach by topic and region, and visibility may suddenly change dramatically because of platform policy.
5. Wording like "list your sources" can push the proportion of looking on the API from 12.1% to 88.4%, but has little effect on the product ordinary people use. Watch out for this bias when monitoring.
6. Whether comparison and purchase questions trigger a search: test results from people in the industry contradict each other, and there is no settled conclusion yet. A more reasonable view is: this is mainly a characteristic of the question, not of the AI product.
7. The "search on / search off" comparison test is a practical way to judge whether you are fighting a "memory battle" or a "search battle".
8. AI looking is a necessary condition for being seen, not a sufficient condition. After it looks, there are still gates such as "Can it find you", "Does it pick you", "Does it mention you" and "Does it really use you".
