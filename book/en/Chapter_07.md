# Chapter 7 — Being Listed Is Not the Same as Being Used

> This chapter covers the fifth and sixth of the seven gates: **does it mention you** (citation), and **does it actually use you, and use you correctly** (absorption).
> The earlier chapters covered "how to squeeze onto the shortlist". This chapter is about this: even if you already appear in the source list below an AI answer, the story isn't over.
> These two gates are the ones most easily misread along the whole path.

---

## Opening: you're in the source list, but not in the answer

Imagine (what follows is a hypothetical situation; the people and events are fictional):

The owner of a cycling tour company put a lot of effort into writing a very thorough guide to cycling routes. Routes, difficulty, supply points, things to watch out for: all written out clearly.

One day, he asks AI: "I want to join a cycling tour. Which companies do you recommend?"

The answer appears. In the source list below the answer, the first entry is his guide. He's delighted.

Then he looks up at the body of the answer. The AI used the routes he had compiled, and the cautions he had written. In the end, the AI recommended three companies, with prices attached.

He was not one of the three.

His guide became material for AI to write recommendations for his competitors.

This story is fictional, but the phenomenon behind it is not. Later in this chapter you will see that someone in the industry really ran into almost exactly the same thing.

This chapter makes only one big point:

**Being found, being listed as a source, having your content used, having it used correctly, and having your name said are several different things. Any one of them can get stuck.**

---

## Five questions this chapter answers

1. If a web page appears in an AI answer's source list, does that mean its content was used in the answer?
2. Why are some web pages cited heavily, yet their brand name hardly appears in the answer?
3. How many of the statements in AI answers are actually supported by the sources? What are the common kinds of "getting it twisted"?
4. When readers see a citation, do they tell whether it actually supports the answer?
5. When measuring GEO results, which layers should you look at separately? What is the denominator for each layer?

---

## 1. "Being seen by AI" is actually not one thing

We often say "AI cited me", as if that means success.

Let's go back to the book's very busy librarian. You ask him to look something up, and a stack of books piles up on his desk. Finally he writes you a summary, with a bibliography attached at the end.

Here's the question:

- If a book is in the bibliography, does that mean he really read it and used it?
- Did he copy the content he used correctly?
- Did he say in the summary "this is what such-and-such book says"?
- Conversely, might there be books he clearly used but didn't list in the bibliography?

AI answers are the same. "Being seen by AI" can be broken down into at least the following path, step by step:

```
Found (enters the shortlist)
   ↓
Listed (appears in the answer's source list, i.e. "citation")
   ↓
Absorbed (your content is actually written into the body of the answer)
   ↓
Used correctly (the answer faithfully presents what you meant)
   ↓
Named (the answer text says your brand or website name)
```

Between these layers, it is **not "pass one layer and the next passes automatically"**. At every layer someone drops out, and the reasons for dropping out differ:

| Layer | Question it answers | Mainly decided by |
|---|---|---|
| Citation | Is your web page listed as a source? | The process of finding and picking sources (covered in earlier chapters) |
| Absorption | Is your web page's content written into the answer? | How AI uses the sources in hand when writing the answer |
| Faithfulness (used correctly or not) | Is the content written in correct? | The combination of the AI model and the search system behind it |
| Naming | Does the answer say your name? | Whether a given sentence in the answer needs to explain "who said this" |

There is one more gap that is not in these four layers: **every single citation can be correct, and the overall conclusion can still be skewed.** These four layers only check whether "the material that was read" was used correctly; whether the material AI read can represent all the material that could be found is a separate question. An experiment with a fixed set of candidate documents (weak evidence) showed that which documents deep research AI reads is affected by their order and by what it read first (see Chapter 6).

This book calls the fifth gate "does it mention you". This chapter splits it further: **"being listed as a source" and "having your name said" are two things**, covered specifically later on.

---

## 2. Listed but not used: silent citation

First, the first kind of gap: you're in the source list, but the answer doesn't use your content at all.

### The more sources listed, the less each one is used?

One study compared data from several platforms at a single point in time. It calculated two things: how many sources are listed per question on average; and, for each web page fetched, how much of its content is used in the answer on average (the researchers call this the "degree of absorption"; the larger the number, the more is used).

| Platform | Average number of sources listed per question | Average degree of absorption per fetched web page |
|---|---|---|
| ChatGPT | 6.88 | 0.271 |
| Google (AI Overviews / Gemini) | 12.06 | 0.058 |
| Perplexity | 16.35 | 0.065 |

In other words, **platforms that list fewer sources actually use each source more deeply**. The longer the source list, the thinner the weight of a single source in the answer may be.

A reminder: this is only a description of data at one point in time, and does not rule out other possible influencing factors. The evidence is weak; all we can say is "possible in theory".

### The gap on Chinese-language AI search

Researchers ran repeated tests on real Chinese-language AI search platforms and saw the same gap. Among the sources listed:

- **66%** of sources had content that entered the body of the answer;
- **30%** were substantively cited;
- only **8%** were deeply cited;
- **39.3%** were "silent citations": listed in the source list, but the answer used none of their content.

The same study also found that of the brands appearing in citations, **only 8.3% actually made it into the answer in the end**.

### Forums are often listed but rarely used

Another study did a large-scale check on real AI search. It found that Google's AI Overviews list forum and Q&A community sites as sources; but the share of these sources actually used in the answer was **about 22 percentage points lower** than their share of the source list.

Encyclopedia-type sources were the opposite: the share actually used was slightly higher than their share of the source list.

### What this means

In plain terms: **the source list is more like "books I flipped through", not necessarily "views I adopted".**

---

## 3. Used but not listed: invisible use

The gap can also go the other way: your content is used, but not marked as a source.

Researchers ran repeated tests on real AI search and found:

- **14% to 53%** of the statements in answers actually had a basis in the search results, but no citation was marked.
- The same study also found that **15% to over 20%** of statements had no basis at all in the search results.

The range of 14% to 53% is wide, because platforms differ a lot. But the meaning is clear:

- Looking only at the source list **underestimates** the real influence of some sources, because they were used but not listed.
- Looking only at the source list also **overestimates** the influence of some sources, because they were listed but not used (that is, the silent citations of the previous section).
- So "how many times you were cited" is not a reliable indicator of "how much influence you have".

Invisible use doesn't only happen with text. Someone in the industry tested this themselves and found (but no one has independently verified it): on a website he built for a local engineering business, an image appeared in Google's AI Overviews. Yet the answer mentioned neither that website nor that business, and instead listed 4 other websites.

Content being used and who the content is credited to are two separate things.

---

## 4. Used, but not used correctly

Even if your content is listed and used, the answer may still get it twisted.

The table below summarises the main measurement results so far:

| Problem | Data | How it was measured |
|---|---|---|
| Statements in Google AI Overviews not supported by sources | About 11% (98,020 statements checked in total; of which "omitted" 7.0%, "wrong" 2.7%, "vague" 1.4%) | Repeated measurement on real AI search |
| Citations that distort the source's original meaning | 30.6% | Repeated measurement on real AI search |
| Inappropriate sources (the source itself is not suitable for supporting that statement) | 27.1% | Repeated measurement on real AI search |
| Answers containing at least one problematic citation | 71.3% to 96.1% (depending on the model) | Repeated measurement on real AI search |
| Cited URLs that don't exist at all (URLs made up by AI) | 3.0% to 13.3% | Under laboratory conditions |
| More searches, yet a lower pass rate on fact-checking | One model fell from 78.6% at 2 searches to 16.7% at 150 searches | Under laboratory conditions |

Note the first row: the most common problem is not "wrong" but "omitted". Premises and limiting conditions that were in the source are dropped from the answer.

### Five counter-intuitive things

**First, "getting it twisted" and "finding the wrong source" are two different things, and one rises as the other falls.**

One study checked about 761,000 (761,495) pairs of "answer statement and cited source", covering 10 models. The result: the model that twisted things least had a relatively high rate of wrong sources; the model that twisted things most had the lowest rate of wrong sources. **No model was good at both.**

**Second, what decides these two things is mainly the search system behind it, not the model size.**

The "search system" here means the service behind the AI that is responsible for looking things up online (the researchers call it the "provider").

- For whether sources are appropriate, about 96% of the difference can be explained by "which company's search system is used".
- For whether content is faithfully conveyed, about 88% of the difference can be explained the same way.
- Within the same search system, switching to a larger model barely changed the rate of twisting (a difference of less than 0.8 percentage points).
- Reasoning models that "think first before answering" clearly lowered the rate of twisting (one model fell from 34.1% to 18.0%), but had almost no effect on "whether sources are appropriate" (a change of less than 2 percentage points).

**Third, high-quality sources are not necessarily used faithfully.**

Researchers tracked Google's AI Overviews over a long period and found that the sources it cites do have higher credibility scores than the sites on the first page of results for the same search.

But the correlation between "source quality" and "whether statements are faithfully conveyed" is only about 0.045. This number is close to 0, meaning the two are almost unrelated.

**Fourth, a link that opens and relevant content do not mean the facts are supported.**

Under laboratory conditions, for 12 of 14 models, over 94% of links opened normally. For the most advanced models, over 80% of cited content was relevant to the question. But the share that actually passed fact-checking was only 24% to 77%.

**Fifth, first confirm that cited URLs actually exist.**

Under laboratory conditions, 3% to 13% of cited URLs had no archive record at all, and very likely never existed.

- Deep-research AI (AI tools that run many rounds of searches on their own and write long reports) made up URLs at a higher rate (10.7%) than ordinary AI that searches online (4.8%).
- Some models listed about 4.3 times as many citations, but the share of URLs that wouldn't open or couldn't be found was also about 2 times higher.

### AI turns "maybe" into "definitely"

Researchers ran repeated tests on real AI search and found: **once search is connected, answers contain less hedging language than the sources themselves.**

- In one system, hedging language fell by about 40%.
- In Google's AI Overviews, it fell by about 60%.

Where the source says "may" or "in some cases", the answer may state it as a definite conclusion.

---

## 5. With a citation, people just believe it

You might think: even if AI cites things messily, readers can just click through and see, right?

That's not how it actually works.

### Real link or fake link, trust is almost the same

One randomised survey experiment involved 4,927 people in total and used 9 questions. Each person saw a fixed screen prepared in advance by the researchers, not a situation of really using AI. So the readers' reactions were real, but the screens were designed.

Results (scored on a scale of 1 to 7):

- Attaching reference links to the answer raised readers' trust by 0.091 points and their willingness to share by 0.121 points.
- **Whether the links were valid, or invalid, or even made up by AI, made almost no difference to trust** (a difference of -0.021 points, which can be treated statistically as no difference).
- By contrast, flagging "this point is still uncertain" lowered trust by 0.157 points.

### Citations that support the claim and irrelevant citations have about the same effect

Another study, on real AI search, analysed 24,069 conversations and 12,652 user votes (users choosing which of two answers they preferred).

- Users preferred answers with more citations.
- More crucially: **citations that really support the claim (an influence of about 0.29) and citations unrelated to the claim (an influence of about 0.27) had almost the same effect on user preference.**
- Only citations that "contradict the claim" showed no clear effect.

This is correlation, not causation. And the data for the "irrelevant citations" part covers only about 800 conversations.

### What this means

For ordinary readers, a citation works more like "looks well-founded" than "has been checked".

This makes the problem in the previous section worse: **a twisted statement with a citation attached is actually more likely to be believed.** If it's your brand being twisted, the consequences are even more troublesome.

---

## 6. "I've used it for three months" becomes "some users report"

Many businesses rely on word of mouth from real customers. Here is a phenomenon you need to know about.

Researchers examined 30,000 answers from the built-in AI Q&A feature of a social platform and found two things.

### When picking: AI prefers comments that are "already popular and formal in tone"

- Within the same discussion thread, for every "standard deviation" increase in a comment's score ranking (think of it as "clearly a notch higher"), its chance of being chosen was about 2.88 times what it had been.
- Top-level comments (not replies to someone else) were about 1.97 times as likely to be chosen.
- Comments with a formal tone were about 1.49 times as likely to be chosen.
- Comments in a personal-experience-sharing tone were actually less likely to be chosen (about 0.79 times).
- Comments pinned or specially flagged by moderators were almost never chosen.

### When writing the answer: AI erases the "I"

In the sources, first-person "I" language made up about 3.3%. In the answers, only 0.06% remained; it almost entirely disappeared.

So "I've used it for three months and the battery broke twice" gets rewritten as "some users report problems with battery durability".

Who said it, and under what circumstances, disappear together. Personal experience is compressed into a generalised piece of advice.

This matters especially for brands that rely on good reviews: **your good reviews may be handled this way too, and you have no direct control over what they get turned into.**

---

## 7. Being cited and being named are two different things

Putting the above together, you can see "being cited" and "being named" as two different processes:

```
Cited: your web page matches the question → found → listed as a source        (this is a "finding sources" problem)
Named: a sentence in the answer needs to state where it came from → says the source or brand name    (this is a "who gets the credit" problem)
```

To use the librarian metaphor:

- **Being cited** is like the librarian "flipping through your book". If your web page happens to answer the question, it gets pulled in as a reference.
- **Being named** is like the librarian writing "according to such-and-such company" in the summary. Your name appears only when a sentence "must explain who said it".

To be honest: **no study so far has specifically proven the causal mechanism behind these two.**

But several pieces of data are consistent with this division of labour:

- the large number of silent citations;
- of the brands in citations, only 8.3% make it into the answer;
- the Chinese-language platform study mentioned earlier also found that a brand appearing repeatedly together across many different sources predicted whether it would be picked for the answer better than traditional Search Engine Optimization (SEO) quality scores did. This is also consistent with the book's point that "what others say about you" (third-party sources) matters a lot.

Reports from people in the industry who tested this themselves, and first-hand observations from several people in the industry, all point to the same phenomenon: **the web page is used as a source, yet the answer names and recommends someone else.**

Here are three examples. None has been independently verified; they can only serve as clues.

### Example 1: cited, yet never named once

- **What was done**: someone in the industry tested 85 enterprise software companies (companies that sell software to other businesses). For each, he asked 10 questions a buyer would ask, always using the same AI search. For each answer he recorded two things: whether it said the company's name; whether it listed the company's own website as a source.
- **What was seen**: for 29.4% of the companies, the number of times they were "listed as a source" was greater than the number of times they were "named". Of these, 9 were not named once in 10 answers, yet their own website appeared in the source list. After classifying 616 answers where "this company was absent", he found that which kinds of questions left a company absent varied with how visible the company already was.
- **His interpretation**: these web pages answered the questions well, so they were pulled in as material; but the recommendation list went to brands with more "social proof", that is, brands others review and discuss more. He also admits that he can't be sure whether being cited without being named has any effect.
- **Strength of evidence**: only a single set of data; it can only serve as a clue.

### Example 2: about 700 web pages cited, site name appears only 5 times

- **Situation**: an English-language news site that had been online for about three months had about 700 web pages cited by AI, but the site's name was mentioned only 5 times, roughly once per 140 citations.
- **Where the citations came from**: ChatGPT 659 times, Google AI Overviews 32 times, Google AI Mode 22 times, Gemini 0 times.
- **The site owner's guess**: being cited is about "finding sources"; any web page that matches the question gets pulled in. Being named is about "who gets the credit"; a name is given only when a sentence needs a source to back it up. The many breaking-news items he covers were being reported by other media at the same time, so AI had no reason it had to say his name.
- **His next step**: do more original content, such as his own statistics and numbers others don't have; put the author's name next to the numbers; then compare how often these articles get named. **The results have not been published yet.**
- **Strength of evidence**: only one website; it can only serve as a clue.

### Example 3: the web page is the primary source, but the recommendation goes to rivals

This is the real version of the fictional story at the start.

- **Situation**: a small cycling tour business saw its website traffic fall and was not being recommended by AI. Someone in the industry set up about 17 questions for it and monitored them for around two weeks.
- **What was seen**: this business's web pages kept being used as sources, but the answers never mentioned its name. The AI pulled content from its guide, and then named and recommended three or four competitors with prices attached. For one question, the AI used this business's page as the primary source and still recommended others.
- **His diagnosis**: the problem was not whether AI could read the web pages, but how they were written. This business's brand name was not next to the key sentences; the competitors put brand, facts and numbers together.
- **Strength of evidence**: only one client; it can only serve as a clue.

---

## 8. When you're described wrongly, the error often isn't on your site

The following examples of "AI getting a brand wrong" all come from the real experience of people in the industry, and likewise have not been independently verified.

### Example 4: the error came from someone else's old web page

- **What was done**: the marketing lead of a growing startup asked ChatGPT, Claude and Gemini a fixed set of questions once a month. The questions were like "What does this company do?", "Which is the best tool of this type?" and "How do we compare with a certain competitor?". He recorded how AI described the company, who it grouped with the company, and which sources it relied on.
- **What was seen**: twice, he found AI repeating outdated or wrong information. After tracing it, one case came from a very old directory page, and one came from a third-party article that had it wrong.
- **Strength of evidence**: someone in the industry tested this themselves, with a fixed process and repeated checks, but no one has independently verified it.
- **What this shows**: the problem of "getting it wrong" often isn't on your own website, but in the third-party sources AI adopts.

### Example 5: 15 good reviews, 1 bad review, and the answer only talks about the bad one

- **Platforms**: ChatGPT and Gemini.
- **Situation**: a company had accumulated about 15 good reviews and 1 negative review on a social platform. When ChatGPT was asked about this company, the answer talked almost only about that negative review, and even warned the user to "be careful". Gemini mentioned that negative review, but also explained that most reviews were positive.
- **How it was tested**: tested on 5 different devices and different network locations (IPs); ChatGPT's output was the same every time. After the problem was pointed out in the conversation, the AI would apologise and correct itself; but when a new user asked again, it went back to the negative account.
- **Strength of evidence**: someone in the industry tested this themselves, repeated on several devices, but no one has independently verified it.
- **What this shows**:
  - AI doesn't use information in proportion. A small number of sources can be disproportionately amplified.
  - Correcting AI in your conversation doesn't change the answer the next person sees.
  - Many in the industry believe: even when a brand has negative discussion, it still gets mentioned, but the negative sentiment is reflected in the description. But "many people believe" does not equal "is correct".

### Example 6: structured data is correct, but the answer still shows the old price

- **Situation**: a merchant that updates prices every hour had complete and valid product structured data (price, currency, stock) on its web pages. But Google's AI Overviews kept showing last month's US$99 price range rather than the current US$79.
- **Strength of evidence**: observed by someone in the industry; only this one example. Several authors in the community hold the same view, believing that AI Overviews prices depend on an old version from the last time the page was crawled. But this is still disputed.
- **What this shows**: "using it correctly" also includes "talking about the present". This is a kind of distortion in time. Structured data on a web page is no guarantee that it will be read in real time.

### Example 7: same name, confused

- **Situation**: someone in the industry pointed out that all the content of a certain website was crammed into one big block of text, with several entities (different products, companies, concepts) mixed together. And there happened to be two apps with the same name on the market: one a plug-in for online shops, one an image-generation tool. Gemini couldn't tell which one was meant.
- **Strength of evidence**: someone in the industry tested this themselves, with screenshots attached, but no one has independently verified it. Many in the industry believe that inconsistent descriptions of a brand across different places make AI unable to correctly understand, classify or mention the brand. But "many people believe" does not equal "is correct".
- **What this shows**: content was absorbed but credited to the wrong entity; this is also a kind of "not used correctly".

### Being cited doesn't always mean being opened

When writing this book, we tested ChatGPT ourselves through the API (method in Chapter 4; the sample is very small and no one else has independently verified it): AI rarely opened web pages itself. In the 30 conversations for the three types it opened pages only 16 times in total, and 37 times in the 10 conversations for the swimming question; most citations relied only on the excerpts in the search results.

Take the new website that was cited most for the swimming question (Chapter 3, Case 8): its pages were cited 25 times (counted by conversation), and only 10 times did AI actually open that page.

- Main data page: cited 9 times, opened 7 times;
- Other level pages with the same structure: cited 10 times, opened only 3 times;
- Research articles: cited 5 times, opened 0 times.

This is only one website and 10 questions; the evidence is very weak and can only serve as a case. Also, the API does not show which text AI actually received, so how much it really read cannot be determined from outside.

Research supports this too: researchers found on real AI search that a lightweight model did not open a single web page in 53.6% of conversations. Under lab conditions, answers based only on excerpts were out of date (6.4%) and had citations not matching the original (6.4%) more often than answers that opened the page and then cited it (1.3% and 2.3%). Models differ a lot: the share of not opening any page ranged from 2.6% to 76.0%.

It reminds us (this is an inference): **every page needs a passage that can be understood on its own**; pages with a uniform structure may let AI cite similar pages with confidence after reading one.

### Other scattered clues (all single observations, for reference only)

- Someone in the industry observed: when AI was asked how many members a certain community had, it cited an old number from a blog post from about 18 months earlier, rather than the current number.
- Someone in the industry observed: he contacted each of the sources AI answers used, one by one, asking them to correct wrong or outdated information, and succeeded about 70% of the time. He then added web pages on topics his own site hadn't covered, and AI's descriptions of the brand gradually improved.
- Someone in the industry observed: among about 30 companies of similar revenue size, it was common for AI to leave out products, describe them vaguely, put them in the wrong category, or even attribute products to a larger competitor.
- Someone in the industry reported: in two industries, in the round of answers where AI "helps someone decide", it used on average only about 23% of the known brand facts, and the rest of the time fell back on a general impression of the whole category. His data is not public; it can only serve as a clue.
- Someone in the industry reported: screenshots show that Google's AI Overviews sometimes quote a passage from a source word for word, presented separately from the surrounding answer.

---

## 9. How reliable is this evidence?

Below, the main conclusions of this chapter are sorted once more by strength of evidence:

| Conclusion | How it was measured | How reliable |
|---|---|---|
| There is a gap between citation and absorption (silent citation; forums listed but rarely used) | Repeated measurement on real AI search, and large-scale checks | Moderate. Several independent studies point the same way. But the Chinese-language platform study was done by a company that provides AI visibility services; another is data from a single point in time only |
| Across platforms, "how many sources are listed" and "how deeply each source is used" go in opposite directions | Description of data from a single point in time | Weak. Only possible in theory; other factors not ruled out |
| Invisible use (14% to 53% of statements used without attribution) | Usage records from real AI search, plus reruns under controlled conditions | Moderate. The range is wide, and platforms differ a lot |
| About 11% of AI Overviews statements have no source support | Continuous tracking of Google AI Overviews for 40 days | Moderate to strong. Covers only Google's AI Overviews and popular questions |
| Distortion 30.6%, inappropriate 27.1%, mainly decided by the search system | Questions put to real AI through a programming interface, then sources actually fetched and checked | Moderate to strong. The sample is very large (about 760,000 pairs), but it was through a programming interface, not the screen ordinary users see |
| 3% to 13% of cited URLs are made up | Laboratory conditions | Moderate. The researchers themselves say this is a conservative estimate; the real figure may be higher |
| The more searches, the less accurate the facts | Laboratory conditions | Weak. Only two models were tested, and an AI model was used as the grader |
| Citation links raise trust, and valid vs. invalid links make no difference | A randomised survey experiment using fixed screens | The readers' reactions were real, but the screens were fixed, not a real usage situation |
| Readers don't distinguish "citations that support the claim" from "irrelevant citations" | Real AI search, plus a large number of user votes | Moderate. Only correlation; the irrelevant-citation part covers only about 800 conversations |
| Personal testimony is generalised, and the first person is deleted | On a real platform, checking its output from the outside | Moderate. Only one platform's built-in Q&A feature was studied |

### Three things to remember when reading these numbers

1. **Most of the numbers come from English-language content, and from platforms such as Google, ChatGPT and Perplexity.** There is only one large study of a Chinese-language platform.
2. **Each study defines and calculates "absorption" and "faithfulness" differently.** The numbers cannot be compared directly across studies; you can only look at the direction.
3. **The method of calculation itself affects the conclusions.** One study pointed out itself that its original finding, "long articles are over-used", was partly caused by its calculation method. After switching to calculating with averages, the degree to which short sources were underestimated shrank sharply.

---

## 10. Some common claims: how much do we know now?

### Claim 1: "If AI cites you, it means it trusts you"

- **The common view in the industry**: AI citing a source means it trusts that information; a brand merely being mentioned only means the brand is "present". This is a view, not proof.
- **What research has seen**: there is a large gap between citation and actual use (silent citations make up 39.3%); there are also many cases of being used without attribution; and readers don't distinguish whether a citation supports the claim.
- **A safer understanding**: a citation may only mean "this web page matches the question", not necessarily "AI adopted its view". **Neither claim currently has direct causal evidence.**

### Claim 2: "Switch to an FAQ format and you'll be used more"

- A common suggestion is to rewrite content in an FAQ or question-and-answer format.
- One descriptive analysis of data from a single point in time found that pages in Q&A format had a slightly lower degree of absorption (0.0947) than non-Q&A pages (0.1005). Pages containing code, numbers, definitions and comparisons had a degree of absorption 41% to 77% higher.
- But this is only correlation, with other factors not ruled out, and it **cannot prove the FAQ format is harmful**. All that can be said is: **there is no evidence that "switching to FAQ in itself gets you used more"**. The information density of the content, and how closely it fits the question, may matter more.

### Claim 3: "The more AI searches, the better the answer"

- Intuitively, the more it looks up, the more accurate the answer should be.
- Under laboratory conditions, both models showed "the more searches, the lower the fact-checking pass rate". One fell from 78.6% to 16.7%, the other from 80.0% to 57.9%.
- Another study on real AI search also found that when one platform searched more often, the effect on answer quality was mixed.
- But both pieces of evidence are limited: the former tested only two models, and the latter is only a descriptive observation. For now, all that can be said is: **searching a few more times does not guarantee more accurate citations.**
- Another experiment with a fixed set of candidate documents (weak evidence) looked at something else: the more rounds of searching, the better the material AI read represented all the material that could be found. The average error (on a stance score from −1 to 1) fell from 0.84 in round 1 to 0.41 in round 10, but did not disappear. So "the more searching, the more accurate the citations" and "the more searching, the more complete the evidence" are two different things, and you cannot conclude that "less searching is better".

### Claim 4: "High-quality sources will be used more faithfully"

- The sources cited by Google's AI Overviews do have higher credibility than the sites on the first page of search results.
- But source quality and faithfulness are almost unrelated (a correlation of about 0.045).
- And "faithfulness" and "source appropriateness" trade off against each other.
- So, **working to "make yourself an authoritative source" is not the same as "getting yourself described correctly".**

### Claim 5: "Deep-research AI is more reliable than ordinary AI search"

- Overall, deep-research AI made up URLs at a higher rate (10.7%) than ordinary AI that searches online (4.8%).
- But one of the deep-research products was only 3.5%, below average.
- The difference depends mainly on which specific system it is, not on the category of "deep research".

---

## 11. So what should you do?

### Step 1: do the accounting properly, recording layer by layer

| Practice | How strong the evidence is |
|---|---|
| Split results into four layers and record them separately: **naming** (does the answer text say your name), **citation** (are you in the source list), **absorption** (did your content get into the answer), **correct description** (is the content in the answer faithful) | Researchers measured many times on real AI search and saw large gaps between the layers every time |
| For each layer, state the denominator clearly: is it "all the questions you asked", "questions that produced an AI answer", "answers that cited you", or "answers that named you"? | Definitions are generally inconsistent across studies; this is a basic methodological requirement |
| Don't let citation counts stand for influence. Check both silent citation (listed but not used) and invisible use (used but not listed) | Repeated measurement on real AI search |
| Before tallying your share of citations, first confirm that those cited URLs actually exist and open | Under laboratory conditions, 3% to 13% were made-up URLs |
| Track the share of "cited but not named" as a separate indicator | Observed by people in the industry; consistent with the gaps between layers seen in research |

### Step 2: regularly check how AI describes you, and trace errors to their source

| Practice | How strong the evidence is |
|---|---|
| Use a fixed set of questions and regularly ask several platforms (for example "What does this company do?", "Which company do you recommend for this kind of product?", "How does it compare with a certain competitor?"). Record how AI describes you, who it groups you with, and which sources it uses | Someone in the industry tested this themselves (no one has independently verified it) |
| When you find an error, trace it to the specific source page. Errors are often in third-party directories and old articles, not on your own website | Someone in the industry tested this themselves; research also shows that high source quality doesn't guarantee faithful use |
| Contact the source that has it wrong and ask them to correct it | Observed by someone in the industry (a single clue) |
| Don't rely on correcting AI in the conversation. When the next user asks, the answer may be completely unchanged | Someone in the industry tested this themselves (no one has independently verified it) |
| Watch for cases where a small amount of negative content is amplified, and check each platform separately | Someone in the industry tested this themselves; it is also widely believed in the industry |

### Step 3: make your content easier to absorb correctly and to be named

| Practice | How strong the evidence is |
|---|---|
| Put information-dense content such as clear definitions, numbers and comparisons on your pages | A description of data from a single point in time; only correlation (possible in theory) |
| Put your brand name, facts and numbers in the same sentence, or right next to each other, so that sentence can be "credited" to you | Observed by someone in the industry (a clue, not yet verified) |
| Publish original data (numbers others don't have), and state clearly who produced it | A hypothesis proposed by someone in the industry; no results yet |
| Use clear sections; don't let several entities get mixed together in one big block of text. If there are products or companies with the same name, make clear which one you are | Someone in the industry tested this themselves; it is also widely believed in the industry |
| Keep your brand information consistent everywhere online, and reduce outdated or contradictory third-party descriptions | Widely believed in the industry; the Chinese-language platform study also saw that "appearing together across multiple sources" is linked to a brand being picked |
| Write uncertainty carefully. AI may turn "maybe" into "definitely", so put key limiting conditions within the statement itself, not in a separate paragraph. For example, write "effective in such-and-such circumstances", not "Effective. But note…" | Research on real AI search saw less hedging language once search was connected; this way of writing is inferred from the research and has not been directly verified |

### Don't do this

- **Don't treat "being cited" as the finish line.** Being cited but not named may amount to supplying material for your competitors' recommendations.
- **Don't treat citation counts as an indicator of credibility or results.** Models that cite more are not necessarily more accurate; readers also don't distinguish whether a citation supports the claim.
- **Don't assume highly authoritative sources will be described correctly.** Source quality and faithfulness are almost unrelated.
- **Don't look at only one platform.** Twisting and wrong sources are mainly decided by the search system behind it, and platforms perform differently.
- **Don't pile up quantity with large amounts of disorganised content.** Someone in the industry reported that the brands with the highest visibility are not necessarily used when helping someone decide (a single clue).

### Practices that are outdated, or lack evidence

- **"Getting into the source list counts as success"**: several studies show that citation, absorption and naming are clearly decoupled.
- **"Switching to an FAQ format gets you used more"**: no evidence currently supports this; descriptive data even point slightly the other way.
- **"Structured data lets AI read the latest price or information in real time"**: observations from people in the industry and views in the community suggest not; this is still disputed and cannot be relied on.
- **"Letting AI search more times makes it more accurate"**: under laboratory conditions the opposite trend appeared (limited evidence).

---

## Key points of this chapter

1. "Being seen by AI" has at least four layers: naming, citation, absorption, correct description. At every layer someone drops out. When measuring, record them separately and state the denominator clearly.
2. Being listed is not the same as being used. On Chinese-language platforms, about 39% of listed sources are silent citations; forum-type sources are listed in Google AI Overviews but actually used relatively little.
3. Being used doesn't necessarily mean being attributed. 14% to 53% of answer statements used the search results without marking a citation. Citation counts are not a reliable indicator of influence.
4. Being used is not the same as being used correctly. About 11% of AI Overviews statements have no source support; about 30% of citations distort the original meaning, and about 27% of sources are inappropriate. These two trade off against each other and are mainly decided by the search system behind the AI.
5. A citation is a persuasion signal. Readers trust an answer more because they see a citation, but don't distinguish whether the citation is valid or supports the claim.
6. AI generalises personal testimony. First-person experience is almost entirely erased when the answer is written; when picking, AI prefers content that is high-scoring, top-level and formal in tone.
7. Being cited and being named are two different processes. People in the industry have repeatedly observed "the web page is used as a source, but someone else is recommended". Making a sentence creditable to you is a separate job.
8. In practice, the focus is on continually checking whether AI describes you correctly and tracing third-party sources that get it wrong, not just chasing citation counts.

---

## Remember in one sentence

**AI listing you, using you, using you correctly and saying your name are four different things; chase only the first, and you may be writing recommendations for your competitors.**

---

## What you can do tomorrow

1. **Prepare a fixed set of questions.** Pick 5 to 10 questions customers really ask, for example "What does such-and-such company do?", "Which company do you recommend for this kind of product?", "How does X compare with Y?". Use the same set every time from then on.
2. **Ask several platforms, and save the answers.** Record how AI describes you, who it groups you with, and which sources it uses. Redo this regularly, for example once a month.
3. **Record four boxes for each answer.** Does it name you, are you in the source list, was your content used, did it get it right. For each box, state clearly what the denominator is.
4. **Calculate one more number separately:** what share of the time you are "cited but not named".
5. **Open every cited URL.** Confirm it actually exists and opens before counting it in your statistics. At the same time, watch for "listed but not used" and "used but not listed".
6. **Trace errors to their source.** Open the sources and find which page caused the error. If it's someone else's website (for example an old directory or an article that got it wrong), try contacting them to correct it.
7. **Don't just correct AI in the conversation.** That won't change the answer the next person sees. What needs changing is the source.
8. **Check negative content separately on each platform.** Watch whether a few negative reviews are being amplified.
9. **Open your most important page and change how it's written.** Check whether your brand name is next to the key sentences; put brand, facts and numbers in the same sentence or right next to each other; add more definitions, numbers and comparisons.
10. **If you have original data, publish it.** Include numbers others don't have, and state clearly who produced them.
11. **Organise into sections, and distinguish same-name entities.** Don't cram several things into one big block. If there are products or companies with the same name, state clearly on your website "which one we are, and which one we are not".
12. **Keep your descriptions consistent everywhere.** Check your various introductions online; update the outdated ones and fix the contradictory ones.
13. **Write limiting conditions into the sentence.** Write "effective in such-and-such circumstances", not "effective" followed by a separate paragraph adding exceptions.

---

## Stop doing this

- **Stop treating "being cited" as the finish line.** Being listed as a source without being named may just mean you supplied material for your competitors' recommendations.
- **Stop using citation counts as an indicator of results or credibility.** More citations don't mean more accuracy, and readers don't distinguish whether a citation supports the claim.
- **Stop assuming authoritative sources will be described correctly.** Source quality and whether something is faithfully conveyed are almost unrelated.
- **Stop looking at only one platform.** Each platform has a different search system behind it, and performs differently.
- **Stop piling up quantity with large amounts of disorganised content.** High visibility doesn't equal being used when helping someone decide.
- **Stop believing "switching to FAQ gets you used more".** No evidence currently supports it, and the data even point slightly the other way.
- **Stop relying on structured data to let AI read the latest price in real time.** This is disputed and can't be relied on.
- **Stop assuming that letting AI search more times makes it more accurate.** The trend seen in the lab was the opposite (limited evidence).

---

## What is still uncertain

- **What does a citation actually mean?** Neither "a citation means AI trusts you" nor "a citation only means the page matches the question" has direct causal evidence.
- **What is the causal mechanism behind being cited and being named?** No study has specifically proven it so far. Existing data and industry observations merely point the same way.
- **When you're cited but not named, does it have any effect?** It can't be determined.
- **Does the FAQ format affect absorption at all?** Existing data are only correlation; you can't say it helps, and you can't say it's harmful.
- **Does "the more sources listed, the less each is used" hold?** There are only descriptive data from a single point in time; possible in theory, but not yet proven.
- **What is the relationship between the number of searches and accuracy?** Only two models were tested in the lab; real-world observations are mixed.
- **Do AI Overviews prices depend on an old version from the last crawl?** Still disputed.
- **Does putting the author's name next to original numbers get you named more often?** Someone is testing this; the results haven't been published yet.
- **When a brand has negative discussion, does it still get mentioned, just in a negative tone?** Many in the industry believe so, but it has not been proven.
- **How widely do these numbers apply?** Most come from English-language content and a few mainstream platforms; there is only one large study of a Chinese-language platform; studies define things differently, so the numbers cannot be compared directly with one another; the calculation method itself may also affect the conclusions.
