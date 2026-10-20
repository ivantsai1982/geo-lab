# Chapter 4 — AI Doesn't Search for the Sentence You Typed

> The seven gates, on to gate three: **can it find you** (retrieval).
>
> The previous chapter was about "can it get through the door": whether AI crawlers can read your web pages. This chapter covers the next step: the AI has already decided to go online and look things up. In the batch of material it pulls back, are you there?

---

## Opening: the same product, two ways of asking, two results

Imagine (this is a fictional scenario):

The owner of a software company makes a "team shared inbox" tool. It lets several colleagues handle the same customer service mailbox together, without replying twice and without missing emails.

One day, she asks an AI: "What is the best shared inbox software?" Her product is in the answer. She feels reassured.

The next day, she asks again, using a customer's exact words: "How can our team handle a shared mailbox together without messing up everyone's usual email workflow?"

This time, she is not in the answer. She asks several times in a row. Still not there.

Her product has not changed, her website has not changed, and no new competitor has appeared. Only one thing changed: **the way the question was asked**.

This is not an imaginary phenomenon. Later you will see that someone in the industry asked a similar question 10 times on each of four AIs, and really did see one tool go from "named every time" to "0 out of 10".

The big idea of this chapter is just one sentence:

**AI does not take the sentence the user typed and search for it directly. It first rewrites it into its own search queries, then pulls back material. For you to be pulled in, you have to match the queries it rewrote, and you have to be in the right language and the right market.**

---

## 1. What this gate does

### The librarian does not copy your question word for word

Back to the metaphor used throughout this book: AI is like a very busy librarian.

You ask him a question, and he does not take your exact words straight to the shelves. He first thinks: "What is this person really looking for?" Then he rewrites the question into one or several queries and goes off to pull books for each.

This act of "rewriting one question and splitting it into several smaller questions to search separately" is called **query fan-out**.

The whole process is roughly like this:

1. The user asks a question.
2. The AI rewrites the question into one or more search queries (query fan-out).
3. Each query is sent into its own search system, and a batch of web pages is pulled back.
4. The pages pulled back are the **shortlist (candidate set)**. This step is called **retrieval**.
5. The AI selects and ranks from the shortlist (the topic of the next chapter).
6. The AI writes the answer and cites some of the sources.

### Retrieval decides "who is eligible to compete"

The later selection, citation and absorption all happen only inside the shortlist. If you are not on the list, no matter how well your content is written, you never get a chance to play.

As mentioned at the start of this book: once content gets onto the shortlist, it really can change the AI's answer. But **whether you get in is mainly not a question of writing quality**.

This gate can be broken down into four principles:

| Principle | In one sentence | What it means for you |
|---|---|---|
| First | Sources cited by different AIs barely overlap | There is no single, unified "AI leaderboard" in the world |
| Second | AI rewrites questions, and rewriting makes sources even less stable | What you need to match is the sentence the AI searches for, not the sentence the user typed |
| Third | Wording and word choice decide whether you are on the shortlist | What the category is called, who the buyer is, and your own coined terms all change the results |
| Fourth | The language of the question and the location are "market gates" | Results measured in English cannot see the local market |

Let's go through them one by one.

---

## 2. Principle one: there is no such thing as an "AI leaderboard"

### Why each AI pulls back different things

The first question many business owners ask is: "What's my ranking in AI?"

The question itself is the wrong question.

The reason is three layers of difference stacked on top of each other:

1. Each AI uses a different search system, which is like looking for books on different shelves.
2. Each AI rewrites questions differently, which is like holding a different reading list.
3. Each AI has different preferences for choosing sources, which is like picking books by different standards.

Stack the three layers together, and the pages finally cited go almost completely separate ways.

### How extreme are the numbers

Researchers tested real AI search repeatedly and got the following results.

First, a word on how this is measured. Researchers often use an "overlap score" between 0 and 1: two sets of URLs that are exactly the same score 1; two with no overlap at all score 0.

- **Sources of Google's regular search results, Google's AI Overviews, and Gemini**: the overlap score is only 0.11 to 0.18. In other words, most of the sources differ among the three.
- **URLs cited by ChatGPT, Copilot, Google and Perplexity for the same question**: the average overlap score is only 0.0079, practically 0. In 84.9% of cases, any two of them did not share even a single URL.
- **The same four, fully tested on 10 questions, looking only at each one's top 5 URLs**: 60 pairwise comparisons in total, and the overlap was 0 in every one.
- **How many sources you can see by looking at just one AI**: counting all URLs cited by the four together as the total, a single one accounts for only 11.4% to 42.6%. 96.4% of URLs appeared in only one of them.
- **How much the sites cited by AI overlap with Google's top 10 sites**: 4.0% for GPT-4o, 11.1% for Gemini, 12.6% for Claude, 15.2% for Perplexity.
- **How many of the sites cited by AI have appeared in traditional search**: 37% never appeared in traditional search results; 38% appear in both.
- **Sites cited by Google's AI Overviews**: 29.8% are not in the Google first-page results on the same page; only 25.0% are in the top 5 on the first page.

### A few easily overlooked details

**First, AI gives out fewer spots than traditional search.** AI cites an average of 4.3 URLs per answer; a traditional search results page has an average of 10.3. Fewer spots means more concentrated competition.

**Second, ranking first in traditional search still has an advantage.** When pages cited by AI also appear in traditional search results, the one cited most is the result ranked first in traditional search: 23.27% for Bing, 14.53% for Google. So the claim that "Search Engine Optimization (SEO) is useless now" is wrong. SEO is still useful, it just isn't enough.

**Third, the same AI changes every day, but the differences between AIs are even bigger.** Ask the same AI again a day later, and 67.0% of the cited URLs get swapped out. Even so, the similarity of the same AI on two consecutive days is still about 42 times the similarity of "different AIs on the same day". In other words: each AI changes every day on its own, and the gap between AIs is even bigger.

**Fourth, industries vary a lot.** Compared with Google's top 5 sites, the overlap of AI citations is: 15% for smartphones, 32% for laptops, 33% for electric vehicles, and only 0.1% to 20.6% for local services. For car-related questions, the overlap score of sites cited by different AIs is between 0.096 and 0.251.

### Tests by people in the industry point the same way

Someone in the industry tested this themselves and got numbers pointing the same way (but no one has independently verified it):

- On 1,000 questions (a mix of "looking for information" and "wanting to buy" questions), the sources of ChatGPT, Google and Bing overlapped by only 19%.
- Someone reported that on a large number of identical questions, ChatGPT and Perplexity agreed on only 11% of sources. Only the conclusion of this report remains; the testing method cannot be seen.
- Across 8 cities and 6 industries, 48 local markets in total, only 11.9% of the businesses Google Maps listed for buyer questions were mentioned by any AI at all. In most markets, more than half of the businesses mentioned by AI were mentioned by only one of the AIs.

### Why this happens

Someone in the industry has observed that each AI is connected to a different search system. As for which search database ChatGPT actually uses when it goes online, there is no consensus in the industry (the "Debates" section later covers this).

What is certain: with different search systems behind them, the shortlists they pull back are naturally different.

### Conclusion of this section

"Ranking first in AI" is not something that can be measured.

All you can say is: "On a particular AI, in a particular language, in a particular market, with a particular way of asking, the probability that I get pulled onto the shortlist is roughly this much."

This is also what the book's "rolling dice" metaphor means: ask the same question ten times and the answers may differ. Look at "how many times out of ten you appear" (**mention rate**), not "what rank you are".

> **A closer look: what do these scores mean?**
>
> The "overlap score" mentioned in this section is commonly measured in research with something called the Jaccard index: the intersection of two sets of URLs divided by their union. 0 means completely different, 1 means completely the same. 0.0079 means: the URL lists of the two AIs have almost nothing in common.
>
> The next section brings in another score (called RBO in research). It looks not only at whether there is overlap, but also at whether the ordering is similar, and the higher positions matter more. It also runs from 0 to 1; the closer to 1, the more stable.

---

## 3. Principle two: AI rewrites your question, and rewrites it differently each time

### How rewriting happens

The user types an ordinary sentence. The AI does not search it as is. It first rewrites it into one or more search queries. This is query fan-out.

The rewriting is "generated" by the AI, and may be different each time. The search results then change along with the rewriting. So the sources of AI search are less stable than those of traditional search.

### What the research says

Researchers tested real AI search repeatedly and found:

- **With just a slight rewording of the question**, the ranking stability of Google AI Overviews' sources (the RBO score mentioned above) is only 0.49; with the same rewording, traditional search results score 0.74.
- **Even with no rewording at all**, just asking again on the same device, the stability of AI Overviews is 0.69, and traditional search is 0.86.
- **Sending the AI's rewritten queries back into Google Search**: in 98.16% of cases, the "black-hat SEO" sites (sites that use cheating tactics to push up their rankings) that originally ranked near the top could not be found. With only a small rewording, the success rate of this kind of attack drops below 10%.

That last point means two things for you.

**The bad news:** the AI's rewriting layer keeps most pages that are "optimized only for the user's original keyword" outside the door.

**The good news:** rewriting itself follows patterns. Whoever can predict how the AI will rewrite holds the entrance to the shortlist.

In the same study, researchers covered in their pages the query wording the AI might rewrite to. As a result, across the 5 AI systems tested, the share of such pages being used reached more than 2 times that of the control group. Note: this is "how much of all the content used it accounts for", not a "success rate".

The same study also found: **simple keyword stuffing had no effect on any of the systems tested.**

### What the rewritten queries look like

Research has not systematically disclosed each AI's rewriting rules. The following was obtained by people in the industry who intercepted network data and looked at logs themselves; no one has independently verified it:

| Observation | Details |
|---|---|
| How many searches per conversation | In a small test of 30 questions, ChatGPT searched 1.1 times on average; Google's AI Mode 3.3 times on average, and AI Overviews 3.4 times on average. Google's two numbers were reconstructed by inference, not seen directly |
| Big differences between modes | Researchers captured how ChatGPT's web version actually works (versions 5.2 to 5.5): the fast mode (Instant) searches only 1 to 2 queries each time, mostly in a single round; the thinking mode (5.4 Thinking) searches about 12 queries each time over an average of more than 3 rounds, and in later rounds more than half use `site:` to target a website. The 1.1 times in the row above is closer to the fast mode |
| The sentences ChatGPT searches | Usually one fairly long query packed with brand or product names, averaging 8.2 words; about one third copy the user's original sentence directly |
| How many pages cited each time | ChatGPT 4.1 pages on average, AI Mode 16.9 pages on average, AI Overviews 13.3 pages on average |
| Whether cited pages are in the search top 10 | Of the pages cited by AI Mode and AI Overviews, only 10% are in the top 10 for the main query; even counting all the smaller split-off queries, it is only 23% (AI Mode) and 28% (AI Overviews) |
| Automatically adding the year | The user asks "Best shoes for running", and what ChatGPT actually searches is "best running shoes 2026". Most of the cited pages have "2026" in the title or content |
| Verification searches behind the scenes | Someone in the industry intercepted Gemini's search actions and found it often sends 3 to 5 short, fairly technical queries, such as "[category] safety certification list 2026" or "pricing plans table". It also often adds the name of a community discussion site, or words like "forum", at the end of the query, to look for consensus among internet users |
| Brands already written into the query | The user did not mention any brand at all, yet the smaller queries ChatGPT split off already had the names of several well-known brands in this category written in |

These numbers have a shelf life. In the test we ran ourselves while writing this book (October 2026, see below), GPT-5.6 Sol used through the API generated 9.5 to 11.9 sets of search terms per conversation on average, far more than the 1.1 times in the table above. The model version is different, and the API differs from the web interface, so this cannot directly replace the table; it only shows that observations like these go out of date quickly as versions change.

Another large-scale study (two markets, 90 days, 158,000 answers) found that every page ChatGPT cited came from its own search results; 97% of the pages it retrieved were not in Google's top 50; and among pages on the same website, "whether its search retrieved the page" explained about 32% of the differences in citation, while the page's own features explained only about 2.8%. (This is a correlational study, it used small models, and the authors run an AI monitoring platform.)

### The last item is worth stopping to think about

"The user did not mention a brand, but the AI's search query already contains brands." What does that mean?

It means **the AI already has a list in mind before it goes online**. Searching online is just to verify and add to this list. This is what this book calls the **brand prior**: the impression of a brand that the AI already remembers before it looks anything up.

Someone in the industry observed: brands written into the query had a citation rate of 68.9%; brands not written into the query had only 2.1%. However, only the title of this report remains and its content cannot be seen, so it can only be treated as a clue.

This is consistent with what Chapter 1 said: famous brands, AI knows from memory; brands without a name, AI has to find by going online. Researchers also found in a controllable experimental system: among the brands or products listed in an AI's ranking, on average 16% were not in any of the passages it had pulled back at all. In other words, part of the list the AI gives does not come from the material it searched.

### What we measured ourselves

When writing this book, we tested ChatGPT ourselves through the API (October 2026). The method: use GPT-5.6 Sol through OpenAI's API with web search turned on, and record the search terms AI generated, the web addresses in the search results, and whom it finally cited. 40 conversations in total: one swimming-recruitment question, asked in 5 English phrasings, 2 times each; plus 3 types (shopping, local services, health knowledge), 5 questions each, each question asked once in each of 2 phrasings.

The limits first: English only, only one model, through the API rather than the web interface, only one city for the local questions, a very small sample, and no independent verification by anyone else yet. What we saw:

- **Almost every search term added words the user never said.** 94% for the swimming question, 95% for the three types (270 of 284). The added words fall roughly into five kinds:
  - switching to insider wording: for example, turning "how fast does a 12-year-old need to swim" into the formal name of the sport's official time standards;
  - anticipating what evidence is needed: official, results sheets;
  - anticipating the constraints behind the question: for example, caps on recruiting places;
  - filling in concrete examples from memory: names of well-known swimmers;
  - anticipating a deeper question: for example, long-term follow-up research.

  As a result, a research article answering "what happens later to swimmers who were slow at 12" was cited, even though the user never asked about that.
- **Different types of question are rewritten in different ways.** Shopping questions get specific brand models written in, plus specification words such as price, weight and battery hours; health questions get words for levels of evidence (clinical guideline, systematic review, randomized trial); local-service questions get verification words (official, reviews, license, address).
- **The first search term already names a website.** In 7 of the 30 conversations for the three types, and 6 of the 10 for the swimming question, the very first search term used `site:` to specify a website; for shopping questions it often went straight to a specific product page on the brand's official site. This is direct evidence that "AI has a list in mind before it goes online".
- **The search terms AI generates explain who gets cited better than the user's original sentence does.** We scored the pages AI saw by similarity of meaning: scoring with AI's generated search terms separated cited from uncited pages better than scoring with the user's original sentence. By question type, only shopping showed a clear gap; local services and health went the same way, but the gap was not clear. We also ruled out the possibility that "AI first decided whom to cite and then wrote the product name into the search term": using only the search terms without `site:`, or only the first search term, gave the same result.
- **Meaning matters more than wording.** Scoring by similarity of meaning separated who got cited to a moderate degree; matching keywords by wording alone was about as good as guessing for the swimming question once the most-cited website was removed. The exception was shopping: for exact words such as model numbers, matching the wording also helped.

> **A closer look:** "Separating" here is measured with an indicator called AUC: 0.5 means guessing, 1 means perfectly separated. Scoring by meaning gave 0.74 for the swimming question and 0.67 for the three types; shopping with keywords gave 0.71. AI's generated search terms scored 0.075 higher than the user's original sentence, with a 95% range of 0.022 to 0.127 calculated by resampling conversations.

These results support this section's point: **what you need to match is the query AI rewrites.** But they come from one model and a small sample through the API, and cannot represent the web version of ChatGPT, or other platforms.

### Searching more does not mean searching wider

Intuitively, the more times AI searches, the more spread out the sources should be. The evidence does not support this intuition.

**What research found (in a controllable experimental system):** so-called "deep research" AIs (AIs that search many rounds in a row on their own and write long reports), after multiple rounds of searching, tend to concentrate on a small number of "user content that anyone can edit" pages, such as community discussions and Q&A pages.

- In open-source deep research AIs, this kind of user content accounts for 16.7% to 23.4% of the URLs pulled back.
- Of this, one large community discussion site alone accounts for 53.7% to 70.7% of this kind of user content.
- Looking at commercial deep research products: 12.1% of Gemini's citations are this kind of user content; for the product from OpenAI (the developer of ChatGPT), it is only 0.4%.
- One possible reason for this concentration is "whatever is read first, the search keeps going in that direction": what to search for in the next round is decided by the content already read. An experiment with a fixed set of candidate documents (weak evidence) found that when two searches differed only in the order of the documents, by round 4, 63.9% of the search terms were already different, and 75.0% of the sequences of documents read were different.

**Tests by people in the industry (repeated tests, with a control group):** starting from August 8, 2026, ChatGPT's search behavior suddenly changed:

- The sources pulled back per answer increased from about 11.7 to 18.9, 61% more.
- Distinct URLs went up by 69%.
- **But distinct websites went up by only 9%.**
- The number of pages grabbed from the same website within the same answer rose from 1.38 to 2.20.

In other words, ChatGPT is "reading deeper" within websites it already uses, not discovering new websites. **Websites that were not on the shortlist before August 8 did not get pulled in because the AI searched more.**

### Conclusion of this section

What you need to match is not the sentence the user typed, but the few sentences the AI rewrote.

And AI searching more will not automatically bring you onto the shortlist.

---

## 4. Principle three: say it a different way, and you may vanish from the list

### Why wording matters so much

After the AI has rewritten the query, it finds pages by "similar meaning". This is called semantic matching. It does not count how many times a keyword appears; it compares "whether what this page talks about looks like what this query is looking for".

So the words you use on your page, what you call your category, what task you describe, and which kind of buyer you are writing for, decide which queries can pull you in.

Call the category by a different name, or ask the question as a different buyer, and a different batch of pages gets pulled in.

### First, let's be clear about how strong the evidence is

The research evidence for this one is relatively thin; it comes mainly from repeated tests by people in the industry.

There are two points of indirect support from research: first, rewriting queries changes sources substantially (previous section); second, covering the rewritten query wording in a page helps it get used.

### Tests by people in the industry (repeated tests, with a control group)

**Example 1: the same tool, asked a different way, disappears.**

The tester asked about "shared inbox software" in two ways:

- One used the category name: "the best shared inbox software".
- The other used what a real user would say: "How can we handle a shared mailbox together without messing up our usual email workflow?"

Each way of asking was asked 10 times on each of four AIs.

When asked with the category name, the two main tools were named almost every time. After switching to the descriptive way of asking, one of the tools went from "appearing every time" to "0 out of 10" on ChatGPT.

The tester also tracked two other tools as a control. These two tools were very stable under all ways of asking. What they had in common: their pages used the buyer's own language to describe the actual workflow, rather than just saying "we are a shared inbox software".

**Example 2: change the buyer, and the results change.**

A certain newsletter platform appeared only in questions where "the buyer is a creator". When the buyer was set as "a business", and the task was simply described in plain language, it dropped to 0 out of 40.

If you mix all the ways of asking together and calculate one average "visibility score", this kind of difference is completely hidden. You would think you are "doing fine", but in front of a whole group of buyers, you simply do not exist.

**Example 3: a word you coined yourself can get you pulled in; "who is similar to whom" cannot.**

A brand-new author (an **entity** that had not existed on the internet before) tested three AIs every day for 99 days in a row, using 16 fixed questions.

- In the 10 questions that "do not mention the author's name, only ask AI for recommendations", the AI answered 6,729 times in total, and this author was named only 40 times.
- Of those 40 times, 25 came from the same question. That question used a niche genre name that the author had coined, a term that did not originally exist on the internet.
- With questions like "is there anyone similar to [famous author]", each question was asked about 700 times, and the author was named 0 times.
- Asking AI directly by name "who is this author", from about day 49 onwards, the author was mentioned steadily in 72% of answers. This shows the AI can find this author; the problem is not that "the search engine hasn't indexed it".

### The tester's interpretation (this is an opinion, not proof)

> What others say about you (third-party comparison lists, reviews, discussion threads) decides whether you can get onto the recommendation list; the language on your page describing concrete workflows decides whether you can stay on the list when the way of asking changes.

### Other clues (only individual observations, can only be treated as clues)

Someone in the industry observed the following:

- For the same marketing services company, asking with the niche term it is known for, it was named 19 times out of 25; asking with the two broad category labels on its homepage, it was 0 out of 25.
- Calling the same category by a different name dropped one brand's mention rate from about three quarters to zero.
- In the data on local businesses in a certain city, about 42% of businesses changed whether they were recommended purely because of differences in the wording of the question.
- Questions like "what can replace [product]" cited comparison-type pages about 10 times as often as questions like "the best [product]". The deciding factor is the type of intent behind the question, not whether the question contains a brand name.
- Someone reported: when no other explanatory sources could be found, Google's AI Mode and AI Overviews cited social platform content whose wording and question were almost word for word the same.

### Conclusion of this section

Semantic matching is not "keyword density".

What decides whether you are on the shortlist is whether your page uses the phrasing **buyers would say and AI would rewrite to** in order to describe the problem you actually solve.

---

## 5. Principle four: language and location are "market gates"

### Switching language is like switching to a different library

Ask the same question in a different language, and the queries the AI rewrites will also be in that language. Once sent into the search system, what gets pulled back is the web world of that language.

The shortlist is not fine-tuned; it is **swapped out wholesale**.

In addition, the user's network location when online (that is, the country the internet service shows, technically called the "exit IP") affects which country's user the search system takes you to be.

### What the research says

Researchers tested real AI search repeatedly and found:

**1. Switching language swaps out almost the entire set of websites.** When GPT is asked in a different language, the overlap of cited websites is close to 0. Claude is the most stable in this respect. Also, rewording within the same language affects the cited websites less than switching language does.

**2. Local brands benefit the most.** Researchers collected 35,640 answers across 12 European languages and 3 AIs that go online. When the question was asked in the language of the brand's home country:

- The recommendation share of leading local brands rose by 0.80.
- Global brands rose by only 0.15.
- The content similarity of answers in different languages averaged 0.825 (1 means completely the same). It was slightly higher within the same language family than between different language families (0.844 vs 0.820).
- The tone of the answers also changed with the language, with English answers being the most negative.

**3. The share of local sources changes by multiples.** In Google AI Overviews on health topics:

- When asked in English, the share of citations going to each country's local sources varied a lot: Australia 48.2%, the United States 33.7%, India 2.3%, Nigeria 0.2%.
- After switching to the local native language, the share of citations going to local sources rose by 3.5 to 13.5 times. For example, Japan rose from 16.6% to 57.5%, and South Korea from 2.7% to 36.4%.

**4. Language decides "choose local", location decides "which country's local".** This is a small-sample study: 234 tests in total, each group repeated 6 times.

- Asking in English in Istanbul and Tallinn, local vendors did not appear even once in 12 tests.
- Asking in the local language, global vendors appeared only 1 time out of 24.
- Even more telling: a person in Berlin asking in Turkish got **German** local accounting software vendors (5 out of 6 times); a person in Tallinn asking in Russian got **Estonian** local vendors (4 out of 6 times).

In other words: **the language of the question swaps the whole shortlist over to "local-type" vendors, and the location decides which country's local.**

**5. Different AIs read location in different ways.** Researchers tested 31,200 answers on real AI search:

- **ChatGPT** goes by the location the application tells it, down to the city. It writes the place name into its own search terms; even when the search terms contain no place name, the search system still changes sources by location. It **ignores** which network you are actually connecting from.
- **Gemini** is the opposite: it ignores the location it is told and goes only by the country of the network. Even for questions that have nothing to do with location, quite a few sources change; but it cannot tell cities apart.
- The businesses recommended are very unstable: asking again in the same city, only 32% were the same; in a different city, only 8%.

The study also had a comparison category: project management software. This category showed no language effect. The researchers speculate this may be because categories like accounting are affected by each country's regulations, while project management is not, but this speculation has not been verified.

### Two additions to remember together

- **Whether answers are stable depends mainly on which AI it is, not on which language is used.** In the study's statistics, "which AI" could explain about 0.319 of the variation, while "which language" explained only about 0.011.
- **The language gate swaps out the local layer, not all sources.** In 11 of the 12 languages, the most-cited website was the same online encyclopedia.

### Tests by people in the industry (no one has independently verified them)

**1. In smaller languages, new terms are easily misunderstood.** Someone asked five AI search tools in Finnish: "Which is the best GEO agency in my area?" Only two tools understood it as a marketing service. The other three recommended, respectively, a land surveying company, an agricultural earthworks contractor, and an outdoor game called "geocaching".

The reason: in a language with relatively little web content, a short question does not give enough context for the AI to tell what a new term means.

**2. Cities must be written into the sentence, not into the settings.** A logistics company providing services in about 8 cities in India:

- Tested with 41 questions buyers would ask, it was named 0 times.
- With the AI's location set to a certain city, and then asking generic questions, it was still 0 out of 3.
- With the city name written directly into the question, Gemini named it all 3 times; Google's AI Overviews named it in two cities, and only in the cities where it **had a dedicated city page**.

Note: this observation holds only for Gemini and Google AI Overviews. The study in point 5 above shows that ChatGPT follows the city that is set.

**3. Every market's local ecosystem is different.** Someone asked ChatGPT "GEO agency + city name" in 19 cities:

- Of 94 agencies, 97% had their official website cited.
- The share of citations going to "business profiles" (the business information pages on search engines) was 86% in India's big cities, only 18% elsewhere, and about 15% in other emerging markets.
- This is not a common pattern across all emerging markets, but a characteristic of a single market.

**4. Translating your list of questions is not enough.** Someone in the industry observed: translating an English list of questions directly into other languages is not enough, because people in different languages already ask buying questions in different ways.

Also, if you find that the AI, when answering in the local language, cites English web pages, this shows that the local-language web has very little content on this topic. In that case, one decent local-language page may quickly get cited.

### Conclusion of this section

Results measured in English cannot represent the local market.

Language is a gate, and on the other side of the gate is a whole other shortlist.

---

## 6. How reliable is this evidence

| Principle | Where the evidence comes from | Strengths | Weaknesses |
|---|---|---|---|
| 1: Sources don't overlap | Multiple repeated tests on real AI search, including peer-reviewed research; large-sample tests by people in the industry point the same way | Multiple independent teams, different AIs, different times, all conclusions point the same way | Some studies had very few questions (for example only 15 questions); some researchers themselves sell visibility measurement services, a conflict of interest |
| 2: Rewriting makes sources unstable | Repeated tests on real AI search (including peer-reviewed research); "deep research AIs concentrate on a few pages" was seen in a controllable experimental system | Ranking stability and "re-search" experiments directly measured the effect of rewriting | What the rewritten queries look like in detail comes mainly from data intercepted by people in the industry; Google's split-off smaller queries were inferred, not seen directly |
| 3: Wording decides the shortlist | Mainly tests by people in the industry (repeated, with a control group); research offers only indirect support | Control groups, repeated tests, long-term daily records | Most tested only one category or one subject; the mechanism behind it is the testers' speculation |
| 4: Language and market gates | Three or more repeated tests on real AI search, covering 12 European languages, plus health topics in Asia and Africa | Large effects, consistent direction, reproducible across different studies | "Location decides which country" was tested on only one AI, 6 times per group, a very small sample; the authors of the two core studies also sell visibility measurement services |

### Keep in mind when using this evidence

- **All of the above are "observed phenomena", not "proven causation".** They show how the shortlist changes, but no randomized experiment has proven: "change the page wording → higher probability of being pulled in → more traffic or sales".
- **AI is updated very frequently.** The sudden change in ChatGPT's search behavior on August 8 shows this: any specific number (how many queries per search, how many pages cited) has a shelf life.
- **The research finding that "covering rewritten query wording works" comes from websites the researchers set up themselves.** It measured "share of content used", not the success rate of real commercial websites.

---

## 7. Things still being debated

### Debate 1: Can you see the queries the AI splits off?

Claims from people in the industry contradict each other:

- Someone says: ChatGPT lets you see its rewritten queries, and Google's two interfaces (AI Mode and AI Overviews) do not. Someone else saw ChatGPT's rewritten queries through the browser's developer tools.
- Another person's test, however, says: Claude and Perplexity disclose the split-off queries, while ChatGPT and Gemini do not.
- Someone tried to get these queries through a third-party API and got only 1 to 3, mostly small variations of the original keyword, and sometimes not even one. Another person tried 6 times and got at most 3.
- The same person compared and found: the "fan-out queries" given by simulation tools were more useful, but those were "simulated" with prompts, not queries the AI actually sent.

**How to see it:** whether you can see them changes with the interface, version and time. Contradictory reports may each have been true at the time each was tested. Simulated "fan-out queries" are only guesses and cannot be treated as observed data.

### Debate 2: Whose search data does ChatGPT use?

The general view in the industry is that when ChatGPT searches online, it uses search data from both Bing and Google. But this is a disputed view: supporters outnumber opponents by a little over three to one. This is not proof.

OpenAI's official documentation confirms that besides its own index, ChatGPT search also uses "third-party search providers", but it does not say which ones. So "is it Bing or Google" still has no answer.

One industry study reported: 83% of the products in ChatGPT's shopping recommendation panel came from Google's shopping data, via shopping-type fan-out queries. This can serve as supporting evidence, but it covers only the shopping scenario.

### Debate 3: Does setting a location help?

- Research (small sample) says: the online location (exit IP) decides which country's vendors the AI recommends.
- Tests by people in the industry say: set the location and ask generic questions, and local businesses were still named 0 times; it only helps if the city name is written into the sentence.

These two do not necessarily contradict each other. A possible explanation: location works at the "country" level, while localization at the "city" level needs the question itself to carry the place. But so far no study has tested these two things in the same experiment.

### Debate 4: Are users' questions actually long or short?

Several one-off observations by people in the industry:

- Someone cited two user surveys: most questions are short, about two thirds within 15 words, close to traditional keyword searches; but more and more people add personal context such as budget and location.
- Someone saw in a client's website data: about 60% of questions were just search terms.
- Someone else believes that in the categories he knows, questions are about 20 words; and because AI remembers earlier context, questions have actually become shorter.
- Yet another person found that conversational queries as long as a whole paragraph have started appearing in Google Search Console.

**How to see it:** these are all individual observations. For the "can it find you" gate, what matters more is the query after the AI rewrites it, not the length of the user's original sentence. Whether the original is long or short, what finally goes into the search system is the rewritten version.

Also, real conversation records show that a sentence is often short because conditions such as budget and location were already stated in earlier rounds (see Chapter 9). Testing with an isolated short question may miss those conditions.

### Debate 5: Is it what others say about you that keeps you stable, or the language on your page?

In the earlier "shared inbox" wording test, even the tester could not cleanly separate the two factors:

- Was it that those tools' pages described workflows in buyer language that kept them appearing steadily?
- Or was it the large number of third-party comparison lists online at work?

The tester's tentative view is: "What others say about you gets you in; the language on your page keeps you there." This is a hypothesis that has not yet been tested.

### Debate 6: Is AI searching a few more times a good thing or a bad thing?

- **For content owners**: AI searching more times means more entrances through which you might be pulled in.
- **But in a controllable experimental system**: multiple searches instead concentrated on a small number of "anyone can edit" user content pages, creating a weak point that is easy to attack. Adding about 13 words to one URL was enough for 57% to 76% of tests to pull it into the AI's reference material, 34% to 61% to cite it, and 22% to 37% to mention the brand or product specified by the attacker in the report. The researchers tried two common detection methods (one checking whether the text is "unnatural", one checking whether outputs are similar), and neither detected it.
- **At the same time**, people in the industry observed: after August, ChatGPT sharply reduced its searches of large community discussion sites; these sites fell from about 4% of its sources to 0.02%.

In other words, the statement "social platforms are sources AI will definitely grab" may be completely untrue for different AIs and at different points in time.

Someone in the industry points out: for the same question, only about 11% of the websites cited by one AI appear in another AI's citations. So changes in one AI cannot be applied to the other AIs.

---

## 8. Real cases

The following cases all come from tests or second-hand accounts by people in the industry, not research papers. After each case, it is stated what it can and cannot prove.

### Case 1: the same tool, asked a different way, goes from 10 times to 0

**What was done:** On ChatGPT, Claude, Perplexity and Gemini, a shared inbox tool was asked about in two ways, 10 times each. One used the category name, the other a real user's descriptive way of asking. Two other tools were tracked as a control.

**What was seen:**

- Asked with the category name: the two main tools appeared almost every time.
- Asked the descriptive way:
  - ChatGPT named one of them 9 times and the other 0 times.
  - Claude was the reverse, 8 times vs 5 times.
  - Gemini named both, 10 times and 8 times respectively.
  - Perplexity named one of them 5 times and the other 0 times, and simply switched to teaching the user how to set things up in their own email software.
- The two control tools were very stable under all ways of asking, at most slightly unstable on Perplexity.

**What this shows:** whether you get pulled in depends on whether the way of asking matches the language on your page (principle three). And each AI reacts in a different direction (principle one).

### Case 2: a new author's 99 days

**What was done:** A brand-new author who only went live on May 11, having registered the measurement method in advance, asked three AIs that go online 16 fixed questions every day, scoring more than 11,000 answers in total.

**What was seen:**

- Questions naming the author directly: after about day 49, steady at 72%.
- In questions that did not name the author and asked AI for recommendations, of the 40 times the author was named, 25 came from the one question that used the author's coined term.
- Questions of the "similar to [author]" type: 0 out of about 700.

**What this shows:** a new brand or newcomer can get pulled in within a short time through "specialized terms you coined yourself" (principle three). But to get pulled in under "similar to [someone]" questions, you need others to mention you together with that famous person in the same piece of content. This kind of third-party joint mention cannot be produced within a few weeks.

### Case 3: add a city name, and go from 0 to 3

**What was done:** A logistics company providing services in about 8 cities first tested with 41 buyer questions, then compared two approaches: "set the location + ask generic questions" and "write the city name into the question".

**What was seen:** At first, 0 out of 41. After setting the location, still 0 out of 3. After writing the city name into the sentence, Gemini named it all 3 times; Google's AI Overviews named it in two cities, and only where it had a city page.

**What this shows:** the location must become part of the "content" of the question sentence, and your website must also have a page for that location that can be matched (principles four and three).

### Case 4: ChatGPT reads deeper, but not wider

**What was done:** Using the same set of 961 questions, the sources pulled back by a total of 5,029 ChatGPT answers before and after August 8 were compared.

**What was seen:** Sources pulled back per answer went up by 61%, but distinct websites went up by only 9%. Government and official agency websites increased sharply; large community discussion sites and several media websites decreased sharply.

The tester himself gave two warnings: first, his question set leaned towards health and finance and should not be treated as a general rule; second, he can only see "that it changed", not "why it changed".

**What this shows:** searching more does not mean more diverse sources. Websites that were not on the shortlist to begin with will not be discovered just because AI searches more (principle two).

### Case 5: building pages for the queries AI splits off, a new site gets cited within a week

**What was done:** A new website, in a very competitive category, built pages not for the sentences users would originally type, but for the fan-out queries ChatGPT split off. Those fan-out queries already had the names of several well-known brands in this category written in.

**What was seen:** Within about a week, these pages were cited by ChatGPT under a very broad "best [type of tool]" question.

The tester stressed in particular: **being cited is not the same as being recommended.**

**What this shows:** retrieval matches the rewritten queries (principle two). But getting onto the shortlist is only the first step; whether the AI picks you and recommends you is the subject of the next chapter.

### Case 6: how to capture the real fan-out queries

**What was done:** Someone in the industry who serves online store clients asked the target question 5 times each on ChatGPT and Gemini, noted every smaller query split off, and kept only those that appeared 3 or more times.

**What was seen:** One question for a kitchenware client produced 14 smaller queries that appeared consistently. After that, he made one page for each query, directly using the wording of that query itself.

In the first month before this, his approach had been to build pages by "writing all kinds of synonymous sentences for the user's way of asking". He made 9 pages, all wasted.

**What this shows:** what you need to match is the smaller queries the AI actually sends repeatedly, not synonymous sentences you imagined yourself (principle two).

### Case 7: "GEO" in Finnish

**What was done:** Five AI search tools were asked in Finnish: "Which is the best GEO agency in this area?"

**What was seen:** Of the five tools, three understood GEO as land surveying, earthworks, or the geocaching game.

**What this shows:** in a language with relatively little web content, a new term lacks enough context, and when the AI rewrites a short question it may pull in the wrong category entirely (principle four). The tester's preliminary experience is: writing out the full name in the service description helps, but this has not been rigorously tested.

### Case 8 (weaker evidence): targeting only a few "best/most" questions

**What was done:** Someone in the industry relayed a client case. This client gave up broad category terms and instead picked 5 to 6 buying-stage questions, such as "the best [product] for [use]" or "the cheapest [product] that works well". Then they first looked at which sources AI was already citing under these questions, picked the ones where they had a chance to compete, and concentrated all their own content and their exposure on third-party websites on these few angles.

**What was seen:** The report says that within 90 days, this client went from almost invisible to appearing in 15% to 20% of the relevant AI answers. The report also says the conversion rate of this traffic was about 4 times that of traditional search traffic.

**How to see it:** this is second-hand, not independently verified, and has no control group. The conversion figures in particular should be treated with caution. This book's consistent judgment is: so far no research has proven that GEO can reliably bring traffic or sales. The value of this case lies in showing an approach: **pick your battlefield by question type, rather than trying to cover everything.**

---

## 9. Ideas that are out of date

| Out-of-date idea | Why it is out of date |
|---|---|
| "I want to rank first in AI" | The sources of different AIs barely overlap, and the same AI changes every day too |
| "Rank first on Google, and you'll be cited by AI" | Only about 10% of the pages cited by Google AI Overviews are in the top 10 for the main query; nearly 30% of cited websites are not on the first page at all. Ranking first still has an advantage, but it is only one of the conditions |
| "Just optimize the keyword users would type" | AI searches rewritten queries, and when rewriting it adds words, adds the year, and even adds brand names |
| "If AI searches a few more times, sources will be more diverse" | Both research and industry data show that searching more mainly means reading deeper within websites already in use |
| "Get the English version right, then just translate it" | Switching language means switching to a whole different shortlist; and people in different languages also ask questions differently |

---

## Key points of this chapter

1. **Retrieval decides who is eligible to compete.** Pages not on the shortlist have no chance of being selected, cited or absorbed.
2. **There is no such thing as "ranking first in AI".** URLs cited by different AIs barely overlap, and the same AI swaps out a large part the next day. You can only look at the "probability of being pulled in" separately by AI, language, market and way of asking.
3. **AI does not search for the sentence the user typed.** AI rewrites the question, may split it into several, add the year, and even write in brand names in advance. What you need to match is the rewritten queries.
4. **Searching more does not mean searching wider.** Multiple searches may concentrate on a few websites, or a few user content pages that anyone can edit. Websites not on the shortlist will not be discovered just because AI searches more.
5. **Say it a different way, and a brand may go from "there every time" to "completely gone".** What the category is called, the task described, and who the buyer is all change the shortlist. Brands that describe actual workflows in buyer language are more stable (this is from tests by people in the industry; the mechanism behind it has not been confirmed).
6. **The language of the question is a market gate.** Ask in the native language, and the share of local brands and local sources rises sharply. Measure in English, and you cannot see the local market.
7. **The location must be written into the question itself.** The online location may decide "which country"; but at the city level, current evidence from people in the industry points to this: the question needs to contain the place, and your website also needs a page for that place.
8. **Being pulled in does not mean getting traffic.** The evidence in this chapter is all observed phenomena. After getting onto the shortlist, you still have to pass the two gates of selection and citation; and so far no research has proven that these can reliably bring traffic or sales.

---

## Remember in one sentence

**AI does not search for the sentence the user typed, but for the few sentences it rewrote itself, and it searches in one particular language, in one particular market. What you need to match is those few sentences.**

---

## What you can do tomorrow

1. **Test and manage each AI separately.** Do not use one "AI visibility total score" to represent all AIs. (Multiple repeated tests on real AI search reached consistent conclusions.)
2. **Test each language and each market separately.** Local brands must be tested in the local native language. For every measurement, record which language was used and which country or region you went online from. (Repeated tests on real AI search; the "location" part has only a small sample.)
3. **Ask the same question many times and look at the mention rate, not a single screenshot.** Researchers found on real AI search: in 4 out of 6 questions, the top recommendation changed when the question was asked again; even asking again on the same device, the sources of Google AI Overviews changed.
4. **Cover in your pages the ways of asking AI might rewrite to**, including qualifiers AI often adds automatically, such as the year. (Researchers ran experiments on real AI search using websites they built themselves, measuring "share of content used"; there are also test reports from people in the industry.)
5. **Capture the real fan-out queries.** Ask the same question several times on the same AI, keep only the smaller queries that appear repeatedly, then use the original wording of that query to make a new page, or add a section of content. (Test reports from people in the industry; no one has independently verified them.)
6. **Use the buyer's own language to describe the problem and workflow you actually solve.** Do not just say "we are a [category] product". (Tests by people in the industry, repeated, with a control group.)
7. **Plan and test separately by question type**: category-name, descriptive, comparison, "what can replace", "best/cheapest", and questions from different buyer identities. (Tests by people in the industry, repeated, with a control group; some are only single observations.)
8. **Build your own specialized terms.** A new brand can first get pulled in under a niche category name it defines itself. (Tests by people in the industry, repeated, with a control group, but only one subject.)
9. **For location-based businesses, make a dedicated page for each service location**, and test with "service + location" questions. (Tests by people in the industry, repeated, with a control group, but only one business.)
10. **In language markets with fewer users, write out the full name of specialized terms and add enough context**, so a new term is not mistaken for an old one. (Test reports from people in the industry, not yet rigorously tested.)
11. **If a topic has very little content on the local-language web, prioritize making local-language pages.** (Observed by someone in the industry; can only be treated as a clue.)

---

## Stop doing this

- **Stop using English measurement results to represent the local market.** Asking in English, you may completely fail to see your local competitors.
- **Stop treating a single screenshot as evidence that "AI recommends me".**
- **Stop keyword stuffing.** In the AI search systems tested, it had no effect at all on being pulled in.
- **Stop mass-producing pages for all kinds of synonyms of the user's way of asking.** What you need to match is the smaller queries AI actually sends.
- **Stop treating "fan-out queries" generated by simulation tools as observed data.**
- **Stop relying only on a VPN or the AI's location setting to test local visibility.** At the very least, also test the version with "the location written directly into the question".
- **Stop applying changes in one AI to the other AIs.**

---

## What is still uncertain

- **Can the queries AI splits off actually be seen?** Industry reports contradict each other, and it may change with interface, version and time. Simulated fan-out queries are only guesses.
- **Whose search data does ChatGPT use when it goes online?** Most people in the industry believe it uses both Bing and Google, but this is disputed and unproven. OpenAI officially confirms only that it uses "third-party search providers", without saying which ones. There is one piece of supporting evidence for shopping, but it is limited to shopping.
- **Does the location setting actually help?** A small-sample study says "the online location decides the country"; industry tests say "the city must be written into the sentence". The two may each govern one layer, but no study has yet tested them together. Another cross-country study on real search engines found that language decides the results more than location does: searching in English across countries, the overlap of result websites was 0.58 to 0.80; switching to the local language, it dropped to just 0.11 to 0.17. A study has now tested both together: the answer depends on which AI it is (see Section 5).
- **Are users' questions actually long or short?** All the claims are individual observations. But for this gate, the rewritten query matters more than the length of the original sentence.
- **Is what keeps you appearing steadily what others say about you, or the language on your page?** Currently they cannot be separated. "What others say about you gets you in; the language on your page keeps you there" is only a hypothesis waiting to be tested.
- **Is AI searching a few more times a good thing or a bad thing?** It brings more entrances, but may also concentrate on a few editable pages, forming a weak point that is easy to attack; and different AIs at different times may behave in completely opposite ways.
- **Why can wording make a brand disappear?** The phenomenon is supported by controlled tests, but the mechanism behind it is only the testers' speculation.
- **Can changing page wording bring traffic or sales?** So far no randomized experiment has proven "change wording → pulled in more often → more traffic or sales". The evidence in this chapter is only observed phenomena.
- **Any specific number in this chapter** (how many queries per search, how many pages cited) may go out of date because of AI updates.
