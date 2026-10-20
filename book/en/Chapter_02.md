# Chapter 2: If AI Never Goes to Look, It Doesn't Matter How Well You Write

> This chapter covers the first of the seven gates: whether to search, which is triggering. Before AI answers, it first has to decide whether to go online and look things up or to answer directly from memory. If this gate isn't passed, none of the later gates ever happen.

## Let's start with a scene

Imagine (this is a hypothetical scenario) a business owner who runs an office cleaning company. Her website was rebuilt just last year. The pages are clean, they load quickly, the service descriptions are perfectly clear, and the FAQ is well organised too. One day she asks an AI, "Which office cleaning companies do you recommend?" The answer lists four companies, and hers is not among them.

She goes back and revises her website again, adding more explanation. A month later she asks again, and she is still not in the answer. The problem may have nothing to do with her website. It may lie in something else she cannot see: **when the AI answered that question, it never went online to look.**

If AI doesn't go and look, it won't read any web pages. However well your pages are written, they are like a book sitting on a shelf that nobody ever opens. This chapter makes just one point: before AI answers a question, it first decides "whether to go and look". This is the first of the seven gates. If this gate isn't passed, none of the later gates ever happen.

When people talk about AI visibility, the first thing they often ask is "What's my ranking?" But the first gate has nothing to do with ranking. What it asks is "whether to look". Lay the seven gates out in a line, and this chapter covers the very first box:

```
Whether to search → Can it get in the door → Can it find you → Does it pick you → Does it mention you → Does it really use you → Will people come
    ▲
This chapter
```

This chapter answers five questions in turn. First, when AI products answer questions, what proportion of the time do they actually go online to look? Second, who decides whether to look: the product, the model, or the way the user asks? Third, which ways of asking make AI more likely to look, and which almost never do? Fourth, if users ask for "list your sources" in the question, can that make AI go and look? Fifth, how can people doing GEO tell whether their target questions are a "search battle" or a "memory battle"?

## 1. The first gate: will the librarian get up and go through the books?

The whole book uses the same metaphor: AI is like a very busy librarian. You ask him a question, and he has two ways to handle it.

The first is to answer directly from memory. He has read a lot of books and remembers plenty, so he just answers. In this case, the answer usually comes with no sources at all. The second is to get up and go to the shelves to find material. He first rewrites your question into a few phrasings suited for searching, then finds web pages, filters them, and finally writes an answer with sources attached. Only on this path does he have any chance of picking up the book you wrote.

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

All the effort you put into your web pages only matters on the second path. So before asking "How do I get AI to recommend me?", you need to ask a more basic question: **for the questions I care about, will AI actually go and look?**

## 2. Who decides whether to look?

This decision is not fixed. Three things decide it together. The outermost layer is the product and platform settings: some AI products look every time, while others let the model decide for itself. Next come the model's own habits. For the same question, some models are very willing to look, while others avoid looking whenever they can, and the difference is large. Last comes the form and topic of the question. Questions phrased as questions, long questions and questions that need up-to-date information are more likely to make AI go and look.

Researchers describe this structure as "the product's outer settings" and "the model itself" deciding together. The product gives the model a set of instructions and tools from the outside, and under those instructions the model then judges for itself whether to look. So whether to look is partly a rule set by the platform, partly the model's own judgement, and partly down to how the user asks.

## 3. The differences are bigger than you'd imagine

You might assume that different AIs look things up at roughly similar rates. That is not the case at all. This book calls the proportion of the time AI decides to look the "trigger rate". It cannot be summed up with a single "industry average", and it varies enormously with the product, the model and the questions used for testing.

Start with conversational AI products. Researchers ran repeated tests on real AI search, putting the same set of 1,000 questions to two models. GPT-5.3-chat looked only 14% of the time, while Claude Sonnet 4.6 looked 83% of the time. With the same questions, one mostly relies on memory and the other mostly goes through the books.

There are also two independent studies that measured ChatGPT repeatedly. The first measured continuously for 45 days and found that 57.8% of answers had no citations at all. The second found that 75.8% of questions, about three-quarters, did not make ChatGPT go and look. The second study also broke down the reasons for "not looking": 69.4% were cases where the model judged "this question doesn't need a search", which the researchers called intent misjudgement; the other 30.6% were cases where the model refused to answer outright for safety reasons.

### Google's AI summary

The AI-written answer at the very top of the search results page is what this book calls the AI summary. It doesn't appear every time either. Three studies measured very different appearance rates:

| Questions used for testing | Overall appearance rate | Of which, questions | Of which, non-questions |
|---|---|---|---|
| 55,393 popular searches | 13.7% | 64.7% | 9.5% |
| Sample of public real search logs | 51.5% | 89.9% | 51.9% |
| Real browsing records of 900 US adults | About 18% | (not counted separately) | (not counted separately) |

The highest and lowest figures differ by nearly 4 times. The main reason for such a gap is that the questions tested were different. Popular searches include many queries that "go straight to a particular website" and very short keywords, and the AI summary rarely appears for them. The searches ordinary people actually type contain more long queries and questions, and the AI summary often appears for them.

So the question "What is the appearance rate of the AI summary?" is meaningless in itself. **The question to ask is: "What is the appearance rate for the kind of questions I care about?"**

## 4. The most reliable pattern: questions and long queries are most likely to make AI step in

Of all the conclusions in this chapter, this one is the most solid, and every relevant study points the same way: **questions and long queries are more likely to trigger an AI answer.**

In the popular-search sample, the AI summary appeared for 64.7% of questions and only 9.5% of non-questions, a gap of nearly 7 times. In the sample of real search logs, the appearance rate for questions was as high as 89.9%. In real people's browsing records, queries that triggered more easily shared three features: they were longer, they began with a question word (such as "how", "why" or "where"), and the sentence contained both a noun and a verb. Grouped by user intent, about 60% of questions brought up an AI answer, about 37% of statements did, and about 12% of queries that "go straight to a particular website" did.

The least likely to trigger are exactly these queries that "go straight to a particular website", which the industry calls navigational queries, for example searching directly for a brand's official site. The reason is intuitive: the user wants a web address, not a paragraph of explanation. If someone searches for "Brand X official site", AI has no need to write them an article. This also means that if you track only your own brand name, you are looking at precisely the area where AI steps in least.

## 5. When the platform changes its policy, your visibility changes with it

Whether to look is not only an algorithm's "judgement" about a question. It is also the platform's "policy". Researchers repeatedly captured Google's AI summary on real AI search across years and saw several changes. The countries covered by the AI summary grew from 7 in 2024 to 229 in 2025. Among US queries, the appearance rate of the AI summary rose from 42% to 67%. For COVID-related queries, the appearance rate of the AI summary went from 1% in 2024 to 66% in 2025, though this item looked at only 74 queries, so the sample is very small.

This is a reminder that **the visibility of a topic can change dramatically and suddenly because of a single platform adjustment, and that has nothing to do with anything you did.** If one day you find that exposure for a type of question has suddenly jumped or dropped, don't rush to blame yourself. First check whether the platform has changed how it decides "whether to give an AI answer" for that type of question.

## 6. If you tell AI to "list your sources", will it go and look?

When monitoring AI visibility, many people like to add "List your sources" at the end of the question. Whether this one sentence has any effect depends on where you ask.

First, a word of explanation. Besides the chat products ordinary people use, AI companies also provide an interface that developers call from their programs, which the industry calls an API. A lot of monitoring work is done automatically through APIs. Researchers ran a controlled test on real AI search, with these results:

| Situation | Without "List your sources" | With it added |
|---|---|---|
| API (the model decides for itself whether to look): proportion that looked | 12.1% | 88.4% |
| API: average number of sources cited per answer | 0.60 | 7.05 |
| Product for ordinary people (free, not logged in): average number of sources cited per answer | 16.6 | 19.9 |

On the API, one sentence moved the proportion that looked from about one in eight to nearly 90%. But on the product ordinary people use, adding the sentence or not made little difference, and the mix of cited sources changed by no more than 2.1 percentage points.

This gives people doing GEO two warnings. **If you use an API for visibility monitoring, the way you word the question can badly distort the results**, and what you measure may not be the real situation. On the other hand, most real users don't add such instructions, so don't use "results with the instruction added" to estimate what real people actually see.

## 7. Even if AI looks, that doesn't mean you've won

One last reminder. AI looking only means your content "has a chance" of being used. It doesn't mean you will certainly be cited, still less that your content will be used correctly.

Here is what the research found. Between 14% and 53% of the claims in answers were in fact supported by the retrieved material but carried no source label; AI used content from certain web pages without mentioning them. Another 15% to more than 20% of claims had no matching search result at all. Models that looked more often did not give better answers across the board either. They were better in some places and worse in others.

So **"going to look" is a necessary condition for being seen, not a sufficient one.** Once the librarian gets up, it still depends on whether he reaches your shelf, picks up your book, mentions you in the answer, and gets it right. These are the gates the later chapters deal with.

## 8. How reliable is this evidence?

Put the conclusions of the previous sections side by side, and their sources of evidence and degrees of reliability are not the same.

"Different models look at extremely different rates (14% against 83%)" comes from repeated tests by researchers on real AI search, and is further supported by real conversation logs from 613 users covering 171,264 conversations. The evidence for this one is strong, but it compared only specific model versions, and the numbers will change once the versions are updated. "ChatGPT doesn't look a large proportion of the time" comes from repeated measurements by two independent studies on a real commercial product, and the evidence is also strong. However, the two studies define things differently: one looks at "no citations at all", the other at "did not look", so the two numbers cannot be directly added or compared.

"Questions and long queries are more likely to trigger the AI summary" is supported by three independent studies, with samples ranging from popular searches and real search logs to real people's browsing records. All three point the same way, the evidence is strong, and it is the most reliable conclusion in this chapter. "Platforms adjust by topic whether to give an AI answer" comes from researchers repeatedly capturing results on real AI search across years; its reliability is moderate, because the COVID example covered only 74 queries. "The wording of a question can change the proportion that looks on the API" comes from repeated tests by researchers on real AI search, with the API compared against an ordinary product; its reliability is moderate to strong, but it was tested only on the topic of mental health, and other topics have not been verified.

When using these numbers, also keep three limitations in mind. First, most of the data comes from specific model versions from 2025 to 2026, and whether to look is a decision made by the product side, which changes as versions are updated. Second, the research on Google's AI summary is mainly based on US or English-language queries. Third, most research on conversational AI used the API or conversation logs that users volunteered. This may differ from real use, where users are logged in, AI remembers who you are, and it personalises for you.

## 9. Where there is no settled conclusion yet

### Controversy 1: Do comparison and purchase questions actually trigger a search?

This is the most obvious contradiction in this chapter. People in the industry have tested it themselves, but their conclusions are exactly opposite.

One camp says AI looks almost every time. Someone in the industry ran several controlled tests of their own, using about 2,000 purchase questions about business software and developer tools, such as "best X", "X vs Y" and "tools for doing Z". Over one month, the proportion with at least one citation was 95% for ChatGPT, 99% for Google's AI summary and 100% for Perplexity. Note that this is a very narrow question set, containing only business software.

The other camp says the more specific the question, the less AI looks. Another person in the industry also reported their own tests. They tested consumer goods, turning on web search through the API but letting the model decide for itself whether to look. On ChatGPT, for questions like "Brand A vs Brand B", 76 out of 80 did not look at all; for questions with a personal situation, like "I have a certain physical condition, which mattress should I buy?", 106 out of 120 did not look; for broad category questions like "best camera backpack for hiking", about half looked.

Both sides have their own grounds, and for now no one can force a verdict on who is right. There are three possible explanations. The first is that the categories differ: software tools change quickly, so the model may judge that it needs fresh information, while for brand comparisons of consumer goods the model may think what it remembers is enough. The second is that the shape of the question differs: "X vs Y" names two brands directly, so the model may think it already knows the answer, while "best X" calls for a list and needs outside information more. The third is that the measurement differs: the first camp looked at "whether a citation appeared", the second at whether the API reported that it "looked".

The first person in the industry offered a view worth remembering: **whether AI looks is mainly a property of "the question", not of "which AI".** If you test with a prompt set that mixes in many "What is X" (definition) and "How do I do Y" (how-to) questions, a given AI's "average trigger rate" will naturally be pulled down. That doesn't necessarily mean this AI dislikes looking. It may simply be that the questions you picked are ones it thinks don't need a search.

### The other three controversies: product cards, research questions, and how deep to look

The second controversy concerns product cards. Someone in the industry reported that among more than 10,000 shopping-related questions, 93% of purchase-intent questions made ChatGPT show a row of product cards, against only 15% of comparison questions. Another person in the industry observed a similar pattern: 93% of "ready to order" questions showed product cards, against only 2.8% of "after purchase" questions. But these figures cannot be used to answer "whether AI looks". Product cards are a different form of answer, and reportedly depend mainly on structured product data supplied by merchants, with little connection to web page content. Moreover, the people who put forward these figures work in a related business themselves, and the figures have not been independently verified.

The third controversy is whether research questions rely on memory alone. Someone in the industry observed that for research-oriented and knowledge-oriented questions, AI mostly answers from what it memorised in training and doesn't look, so your Google ranking is almost irrelevant. Only purchase questions, such as "best X in a certain place" or "top suppliers for doing Z", trigger a search, and only then is the link with search rankings clearly higher. This is consistent with the view in Controversy 1 that "definition and how-to questions are answered directly from memory", but it is only a single observation and can only be treated as a clue.

The fourth controversy is whether asking something very complex can make AI do "deep research". Someone in the industry observed that however complex the question, the model will not switch into the mode where it researches step by step, round after round, on its own. On the surface this contradicts Section 6's finding that "wording can greatly change the proportion that looks on the API". One possible explanation is that wording can change "whether to look" but not necessarily "how deep to look". No research has yet tested this directly.

## 10. A few real observations

Most of the observations below come from people in the industry testing things themselves and have not been independently verified. Please treat them as clues.

### For the same company, search on and search off are two different worlds

A service company found that when people asked ChatGPT "Who can do X?", it was mentioned only about 6% of the time. It first checked its own website: every crawler got a normal response, and there was no technical problem. Yet after it revised its pages, nothing changed.

Another person in the industry suggested a "search on / search off" comparison test: ask the same question once with web search turned on and once with it turned off. This person said they had used this method to score about 180 companies, and the companies AI named were usually not the ones with the cleanest websites, but the ones that often appeared in "X vs Y" comparison articles written by others. Someone in the industry tried it and found that with search on, the company was cited about 16% of the time; with search off, 0.

This means the company's visibility came entirely from AI looking in the moment; in what AI memorised in training, the company currently does not exist. So it makes sense that revising its own pages had no effect. The answers to this kind of question come mainly from comparison and roundup articles written by third parties, that is, **third-party sources**, and the company's own pages are not the main factor.

You can use this simple flow to work out where you stand:

```
Ask once with search off → Are you mentioned?
   ├─ Yes → You are already in AI's memory; this is a long-term asset
   └─ No → Ask again with search on → Are you mentioned?
              ├─ Yes → You depend on AI looking in the moment;
              │        the key is the third-party sources it finds
              └─ No → You're on neither path;
                       deal with "Can it get in the door" and "Can it find you" first (Chapters 3 and 4)
```

### Local businesses and brand-new names

Someone in the industry observed that the same local business had 0% visibility when the model answered only from its internal knowledge. Once web search was turned on, some AI products began recommending it consistently, while others still did not mention it at all. This shows that "AI visibility" is not a single number. You first need to work out whether each product looks and how it looks, and only then can you talk about optimisation.

Another person in the industry observed a very clean example. A brand-new entity, which appeared later than the training cutoff dates of all the models, could still be cited in AI answers. Server logs showed that crawlers collecting training data were kept out for the whole test period, while the kind that fetches web pages in real time at the moment of answering could read the content normally. AI's training memory could not possibly contain this entity, so it could only have been cited because AI looked at the moment of answering. For new brands and new products this matters a great deal: **whether AI is willing to look is your only route to exposure.**

### When monitoring visibility via the API, you may be measuring something else

One person in the industry used the API for weekly visibility tracking on several AI products, collecting about 285 answers per model per week for 4 weeks. They found that when "whether to look" was set to "auto" and left to the model, for most product recommendation questions the model answered directly from its existing impressions and did not look at all. As a result, the "web-connected group" and the "offline group" were almost identical; only when the model was forced to look did the two groups separate.

They also found that the web-connected group's results fluctuated more from week to week than the offline group's, by an estimated factor of about 3. But with only 4 weeks of data, the plausible range for this factor runs from about 1 to 11 times, so the uncertainty is high. For the same set of questions, visibility rose from 0.226 to 0.285 within a single week.

Another group in the industry reported something similar. They collected answers on four AI products. ChatGPT in auto mode gave no citations at all for any pilot question and finished answering in about 4 seconds; the other products looked in real time and took 15 to 40 seconds. However, this person in the industry provides AI visibility services themselves, and their ChatGPT sample was only 18 of 280 questions, so it should not be taken too seriously.

## 11. Which battle are you fighting?

Pulling everything together, you are really facing two different battles.

The first is the memory battle. AI doesn't look and answers from what it memorised in training, so however good your web pages are, it can't read them. Here the only way is to be mentioned in other people's articles, reviews and discussions over the long term, and slowly enter the memory of future AI versions. The second is the search battle. AI looks, and only then do your web pages and third-party sources start to play a role, followed by the later gates.

The same brand may be fighting different battles on different questions and different AI products. **Tell them apart first, then act.**

## Chapter recap

"Whether to search" is the first of the seven gates. If AI doesn't look, your web content has no chance of being read. And the proportion of looking varies enormously: for the same set of questions, one model looked only 14% of the time and another 83%; the appearance rate of Google's AI summary ranges from 13.7% to 51.5% depending on the questions tested.

The most consistent pattern is that questions and long queries are the most likely to trigger AI answers, and navigational queries the least likely. Platforms also actively adjust their approach by topic and region, and visibility can change dramatically and suddenly because of platform policy. Wording such as "list your sources" can push the proportion that looks on the API from 12.1% to 88.4%, but has little effect on the product ordinary people use, so watch out for this bias when monitoring.

Whether comparison and purchase questions trigger a search is unsettled, since industry tests contradict each other; the more reasonable view is that this is mainly a property of the question, not of the AI product. The "search on / search off" comparison test is a practical way to tell whether you are fighting the "memory battle" or the "search battle". Finally, AI looking is a necessary condition for being seen, not a sufficient one. After it looks, there are still the gates of "Can it find you", "Does it pick you", "Does it mention you" and "Does it really use you".

## Remember in one sentence

AI first has to decide "whether to go and look"; if it doesn't, nobody reads your web pages, however well written they are. And whether it looks depends mainly on what the question looks like, and also on which product and model it is.

## What you can do tomorrow

1. Sort the questions you care about. First divide them by form into questions or non-questions, long or short, then by intent into definition, how-to, category comparison, brand comparison and finding an official site (navigational), and record separately for each group whether AI looks. That the way of asking affects whether AI looks is consistently supported by large-scale repeated tests; grouping by intent is a method from repeated, controlled tests by people in the industry.
2. Focus on questions and long queries. These are the most likely to trigger AI answers, and they are where GEO can have an effect; researchers ran repeated tests on real AI search, and three studies point the same way.
3. Run a "search on / search off" comparison. Ask the same question once with web search on and once with it off, to work out whether you are absent because you aren't in AI's memory or because you weren't found. Someone in the industry has used this method to score about 180 companies, but no one has independently verified it.
4. Flag answers with "no citations at all" separately; this is a simple signal for whether AI looked. Someone in the industry tested this themselves: in 406 offline answers, the citation count was zero in every case.
5. Monitor each AI product separately, and don't assume they behave the same. Different models differ greatly, which is supported by repeated tests by researchers on real AI search. The specific figures come from tests by people in the industry: Gemini looked 493 times out of 500, Perplexity looked all 500 times, and almost all answers that didn't look came from ChatGPT (343 of 406 offline answers).
6. When monitoring via the API, state the search settings clearly, record whether it was "forced to look" or "auto", and keep the two separate in your reports. This is from test reports by people in the industry; the difference between the API and ordinary products is supported by research.
7. When interpreting data, take platform policy changes into account. When the visibility of a topic changes suddenly, first check whether the proportion of AI answers for that topic has changed; researchers found this through repeated tests on real AI search across years.
8. For questions where AI doesn't look, accept that this is a long-term battle. For these questions the only way is to keep being mentioned in third-party sources and slowly enter the training data of future versions. This is inferred from how the system works; many in the industry believe third-party comparison content is key, but "many people believe" does not mean "it has been proven".

## Stop doing this

**Don't judge an AI product by a single "average trigger rate".** Whether it looks depends mainly on which questions you ask it.

Don't add words such as "list your sources", "latest" or "2026" to your monitoring questions, unless that is exactly the situation you want to test. Someone in the industry tested this themselves: such words greatly increase how often AI looks, but real users mostly don't ask that way. Likewise, don't treat results from the API's "auto" mode as "web-connected visibility". They may be mostly what AI memorised in training, or a mix of the two in unknown proportions.

Don't assume that revising your own pages can change the answers to questions where AI doesn't look; for those questions, AI never reads your pages. And don't treat the appearance rate of product cards as the proportion of times AI looks; the two are different mechanisms.

### Outdated ideas

Some people think "ranking first on Google means AI can see me". For questions where AI doesn't look, search rankings and AI answers are almost unrelated; and even when AI looks, the sources cited in AI answers overlap very little with the pages on the search results page, as later chapters explain in detail.

Others think "it's enough to track searches for the brand name and the official site". These navigational queries are precisely the type least likely to bring up an AI answer.

## What is still uncertain

**Do comparison and purchase questions actually trigger a search?** Industry tests contradict each other, and there is no settled conclusion. The more reasonable view is that whether AI looks is mainly a property of the question rather than of the AI product, but this is still a view, not a settled conclusion.

**Can the product card figures be trusted?** The people who put them forward work in a related business and the figures have not been independently verified; besides, product cards and "looking" are two different things to begin with.

**Do research questions rely on memory alone?** Only a single observation supports this so far, so it can only be treated as a clue. As for whether complex wording can make AI look deeper, one observation says it cannot. Wording can change "whether to look", but whether it can change "how deep to look" has not yet been tested directly by any research.

**Does the effect of "list your sources" hold for other topics?** So far it has been tested only on the topic of mental health.

**Will these numbers go out of date?** Very likely. Most of them come from specific model versions from 2025 to 2026, and whether to look is a decision made by the product side, which may change as soon as a version is updated. Research on Google's AI summary is also mainly based on US or English-language queries, and other languages and markets remain uncertain.

**Is there a gap between research conditions and real use?** Most research on conversational AI uses the API or logs that users volunteered, which may differ from real use with logins, memory and personalisation.

**How large is the fluctuation in web-connected results?** The estimate is about 3 times, but with only 4 weeks of data, the plausible range runs from 1 to 11 times, so it is still hard to say.
