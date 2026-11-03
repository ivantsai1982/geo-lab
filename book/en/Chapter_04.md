# Chapter 4: AI Doesn't Search for the Sentence You Typed

> This chapter covers the third of the seven gates: can it find you, which is retrieval. The previous chapter was about "can it get in the door", meaning whether AI's crawlers can read your web pages. This chapter covers the next step: AI has already decided to go online and look things up. In the batch of material it pulls back, are you there?

## Imagine

Imagine the owner of a software company that makes a "team shared inbox" tool. The tool lets several colleagues handle the same customer service mailbox together, without replying twice and without missing any emails. (The following is a fictional illustrative scenario.)

One day she asks AI: "What is the best shared inbox software?" Her product is in the answer, and she feels reassured. The next day she asks again, using a customer's exact words: "How can our team handle a shared mailbox together without disrupting everyone's usual email workflow?" This time she is not in the answer. She asks several times in a row, and the result is the same.

Her product hasn't changed, her website hasn't changed, and no new competitor has appeared. The only thing that changed is the way the question was asked.

This kind of thing is not imaginary. Later you will see that someone in the industry asked similar questions 10 times on each of four AIs, and really did see one tool go from "named every time" to "0 out of 10".

## The big idea of this chapter

**AI does not take the sentence the user typed and search for it directly. It first rewrites it into its own search queries, then pulls back material. For you to be pulled in, you have to match the queries it rewrote, and you have to be in the right language and the right market.**

This chapter unfolds along four principles. First, the sources cited by different AIs barely overlap. Second, AI rewrites questions, and rewriting makes sources even less stable. Third, wording and word choice decide whether you are on the shortlist. Fourth, the language of the question and the location act like a market gate. After the principles, we look at how reliable the evidence is, what is still disputed, and a set of real cases.

## 1. What this gate does

Back to the metaphor used throughout this book: AI is like a very busy librarian. When you ask him a question, he doesn't take your exact words straight to the shelves. He first thinks about what this person is really looking for, then rewrites the question into one or several queries and goes off to pull books for each. This act of rewriting a question and splitting it into several smaller questions to search separately is called query fan-out.

The whole process can be divided roughly into six steps:

1. The user asks a question.
2. AI rewrites the question into one or more search queries. This is query fan-out.
3. Each query is sent into its own search system, and a batch of web pages is pulled back.
4. The pages pulled back form the shortlist. This step is called retrieval.
5. AI selects and ranks from the shortlist. This is the topic of the next chapter.
6. AI writes the answer and cites some of the sources.

Retrieval decides who is eligible to compete. The later selection, citation and absorption all happen only inside the shortlist. If you are not on the list, no matter how well your content is written, you never get a chance to play. As mentioned at the start of this book, once content gets onto the shortlist, it really can change AI's answer. **But whether you get in is mainly not a question of writing quality.**

This gate can be broken down into four principles, and each one has a direct meaning for you. The first principle is that the sources cited by different AIs barely overlap, so there is no single, unified "AI leaderboard" in the world. The second principle is that AI rewrites questions and rewriting makes sources even less stable, so what you need to match is the sentence AI searches for, not the sentence the user typed. The third principle is that wording and word choice decide whether you are on the shortlist: what the category is called, who the buyer is, and your own coined terms all change the results. The fourth principle is that the language of the question and the location form a "market gate", and results measured in English cannot see the local market. Let's go through them one by one.

## 2. Principle one: there is no such thing as an "AI leaderboard"

The first question many business owners ask is: "Where do I rank in AI?" The question itself is the wrong question. The reason is that three layers of difference are stacked on top of each other. Each AI uses a different search system, which is like looking for books on different shelves. Each AI rewrites questions differently, which is like holding a different reading list. Each AI also has different preferences when selecting sources, which is like choosing books by different standards. Stack the three layers together, and the pages finally cited go almost entirely their own separate ways.

Researchers ran repeated tests on real AI search and measured this difference. Before looking at the numbers, here is one way of measuring it: researchers often use an "overlap score" between 0 and 1. If two sets of URLs are identical, the score is 1; if they have nothing in common, it is 0.

Start with different interfaces from the same company. Between Google's ordinary search results, Google's AI summary and Gemini, the sources had an overlap score of only 0.11 to 0.18, so most sources were different. Then look across different companies: for the same question, the URLs cited by ChatGPT, Copilot, Google and Perplexity had an average overlap score of only 0.0079, practically 0. In 84.9% of cases, any two of them did not share even a single URL. For the same four, when 10 questions were tested in full and only the top 5 URLs from each were considered, all 60 pairwise comparisons showed zero overlap.

If you look at only one AI, the sources you can see are also very limited. Taking all the URLs cited by the four together as the total, a single one accounted for only 11.4% to 42.6% of it, and 96.4% of the URLs appeared in only one of them.

The distance between AI and traditional search is just as large. How much do the websites AI cites overlap with Google's top 10? For GPT-4o it is 4.0%, for Gemini 11.1%, for Claude 12.6% and for Perplexity 15.2%. Seen from another angle, 37% of the websites AI cites never appeared in traditional search results, and 38% appear in both. Even Google's own AI summary cites websites of which 29.8% are not in the first page of Google results for the same query, and only 25.0% are in the top 5 of that first page. The same holds from the opposite direction: researchers on real AI search ran one large-scale check with 3,611 health questions (collected once), and only about 44% of the pages in Google's traditional top 5 were cited by the AI summary; looking only at short, one-question-one-answer exchanges, about 47%.

### A few easily overlooked details

The first detail is that AI gives out fewer places than traditional search. Each AI answer cites an average of 4.3 URLs, while a traditional search results page has an average of 10.3. With fewer places, competition is more concentrated.

The second detail is that ranking first in traditional search still gives an advantage. When pages cited by AI also appear in traditional search results, the one cited most often is the result ranked first in traditional search, accounting for 23.27% on Bing and 14.53% on Google. So the claim that "Search Engine Optimization (SEO) is no longer useful" is wrong. SEO is still useful; it just isn't enough.

The third detail is that the same AI changes every day too, but the gap between AIs is even larger. Ask the same AI again a day later, and 67.0% of the cited URLs will have been swapped out. Even so, the similarity of the same AI on two neighbouring days is still about 42 times the similarity of "different AIs on the same day". Each AI changes from day to day, and the gap between one AI and another is larger still.

The fourth detail is that industries differ a great deal. Compared with Google's top 5 websites, the overlap of AI citations is 15% for smartphones, 32% for laptops, 33% for electric vehicles, and only 0.1% to 20.6% for local services. On car-related questions, the overlap score of the websites cited by different AIs falls between 0.096 and 0.251. Health has its own lean too. In the health-question check above, compared with the traditional top 5 for the same question, the AI summary leaned more towards commercial health information websites, and large academic medical institutions and government health agencies had lower shares, though the gaps were all small. This check left out video and forum sources, so the comparison holds only among web pages that could be read.

Tests by people in the industry point in the same direction, though no one has independently verified them. Someone tested 1,000 questions, a mix of "information-seeking" and "intending to buy" questions, and found that the sources of ChatGPT, Google and Bing overlapped by only 19%. Another person reported that across a large number of identical questions, ChatGPT and Perplexity agreed on only 11% of sources, though this report left only its conclusion and the test method cannot be seen. Someone else compared 48 local markets across 8 cities and 6 industries, and found that of the businesses Google Maps listed for buyer questions, only 11.9% had been mentioned by any AI at all; in most markets, more than half of the businesses mentioned by AI were mentioned by only one AI.

Why does this happen? Someone in the industry observed that each AI is connected to a different search system. As for which search database ChatGPT actually uses when it goes online, there is no consensus in the industry, and the "Disputes" section later returns to this. What is certain is that when the search systems behind them differ, the shortlists they pull back naturally differ too.

So "ranking first in AI" is not something that can be measured. All you can say is: "On a particular AI, in a particular language, in a particular market, with a particular phrasing, my probability of being pulled onto the shortlist is roughly this much." This is also what the book's "rolling the dice" metaphor means. Ask the same question ten times, and the answers may differ. **Look at how many times out of ten you appear (the mention rate), not at what position you rank.**

> **A closer look: what do these scores mean?**
>
> The "overlap score" mentioned in this section is commonly measured in research with something called the Jaccard index, calculated as the intersection of two sets of URLs divided by their union. 0 means completely different, and 1 means completely the same. A score of 0.0079 means the URL lists of the two AIs have almost nothing in common.
>
> The next section brings in another score, called RBO in research. It looks not only at whether there is overlap but also at whether the ordering is similar, and the higher positions count for more. It also runs from 0 to 1, and the closer to 1, the more stable.

## 3. Principle two: AI rewrites your question, and rewrites it differently each time

The user types an ordinary sentence, and AI doesn't take it unchanged and search for it. It first rewrites it into one or more search queries, which is query fan-out. The rewriting is "generated" by AI and may be different every time, and the search results change along with the rewriting. For this reason, the sources of AI search are less stable than those of traditional search.

Researchers ran repeated tests on real AI search and measured this instability. With just a slight rewording of the question, the ranking stability of the sources in Google's AI summary (the RBO score mentioned above) is only 0.49; with the same rewording, traditional search results score 0.74. Even with no rewording at all, simply asking again on the same device, the AI summary's stability is only 0.69, against 0.86 for traditional search.

The same kind of research ran another experiment: the queries rewritten by AI were sent back into Google search. In 98.16% of cases, the "black-hat SEO" websites (websites that use cheating techniques to push up their rankings) that had originally ranked near the top could no longer be found; with only a small rewording, the success rate of this kind of attack fell below 10%. This has two layers of meaning for you. The bad news is that AI's rewriting layer keeps out most pages that were "optimized only for the user's original keyword". The good news is that the rewriting itself follows patterns, and whoever can predict how AI will rewrite holds the entrance to the shortlist.

In the same study, researchers covered in a page the query wording AI was likely to produce when rewriting. In all 5 AI systems tested, such pages were adopted at more than 2 times the rate of the control group. Note that what was measured here is "share of all adopted content", not a "success rate". The same study also found that **simply stuffing keywords had no effect on any of the systems tested.**

### What rewritten queries look like

Research has not systematically disclosed each AI's rewriting rules. The observations below come from people in the industry who intercepted network data and examined logs themselves, and no one has independently verified them.

Start with how many searches are run per conversation. In a small test of 30 questions, ChatGPT searched 1.1 times on average, Google's AI Mode 3.3 times, and the AI summary 3.4 times; Google's two figures were reconstructed by inference, not seen directly. The mode also makes a big difference. Researchers captured how the web version of ChatGPT actually operates (versions 5.2 to 5.5) and found that the fast mode (Instant) searched only 1 to 2 queries each time, mostly in a single round, while the thinking mode (5.4 Thinking) searched about 12 queries each time over an average of more than 3 rounds, with more than half of the later rounds using `site:` to target a specific website. The figure of 1.1 searches above is closer to the fast mode.

The query ChatGPT searches is usually one fairly long query packed with brand or product names, averaging 8.2 words, and about a third copy the user's original sentence directly. For pages cited per answer, ChatGPT averages 4.1, AI Mode 16.9 and the AI summary 13.3. Are the cited pages in the top 10 search results? Only 10% of the pages cited by AI Mode and the AI summary are in the top 10 for the main query; even counting all the smaller split-off queries, it is only 23% (AI Mode) and 28% (AI summary).

AI also automatically adds a year to queries. When the user asks "Best shoes for running", what ChatGPT actually searches is "best running shoes 2026", and most of the cited pages have "2026" in their title or content. In addition, someone in the industry intercepted Gemini's search activity and found that it often sends 3 to 5 short, fairly technical verification queries in the background, such as "[category] safety certification list 2026" or "pricing plans table". It also often adds the name of a community discussion site, or words such as "forum", to the end of a query, to find the consensus among community users. The most intriguing observation is this: the user mentioned no brand at all, yet the smaller queries ChatGPT split off already included the names of several well-known brands in that category.

All of these figures have a shelf life. In a test we ran ourselves while writing this book (October 2026, see below), GPT-5.6 Sol used through the API generated an average of 9.5 to 11.9 sets of search terms per conversation, far more than the 1.1 searches above. Because the model version is different, and the API differs from the web interface, this result cannot directly replace the earlier observation; it only shows that observations of this kind quickly go out of date as versions change.

Another large-scale study covered two markets, 90 days and 158,000 answers. It found that the pages ChatGPT cited all came from results it had searched itself; 97% of the pages it found were not in Google's top 50; and among pages on the same website, "whether it was found by ChatGPT's search" explained about 32% of the difference in citation, while the features of the page itself explained only about 2.8%. This is a correlational study using a small model, and the authors themselves run an AI monitoring platform.

### Before AI goes online, it already has a list in mind

Go back to the observation that "the user mentioned no brand, yet AI's search queries already contained brands". It means that before AI goes online, it already has a list in mind, and searching online is only a way to verify and add to that list. This is what this book calls the brand prior: the brand impressions AI already remembers before it looks anything up.

Someone in the industry observed that brands written into the query had a citation rate of 68.9%, while brands not written into the query had only 2.1%. However, only the title of this report remains and its content cannot be seen, so it can only be treated as a clue. This is consistent with the point made in Chapter 1: AI knows famous brands from memory, while it has to find unknown brands by going online. Researchers also found, in a controllable experimental system, that on average 16% of the brands or products listed in AI's rankings did not appear in any of the passages it had pulled back. Part of the list AI gives does not come from the material it found.

### What we measured ourselves

While writing this book, we ran our own tests on ChatGPT through the API (October 2026). We used GPT-5.6 Sol through OpenAI's API with web search turned on, and recorded the search terms AI generated, the URLs in the search results, and who was finally cited. There were 40 conversations in all: one swimming recruitment question, asked 2 times each in 5 English phrasings; and 3 categories, shopping, local services and health knowledge, with 5 questions each, every question asked once in each of 2 phrasings. The limitations need to be stated up front: English only, a single model, the API rather than the web interface, only one city for the local questions, a very small sample, and no independent verification by anyone else yet.

The first thing we saw was that almost every search term added words the user had not said: 94% for the swimming question, and 95% for the three categories (270 of 284). The added words fell roughly into five kinds. AI switched to insider terminology, for example replacing "how fast should a 12-year-old swim" with the official name of the sport's time standards. It anticipated what evidence was needed, for example "official" or "results". It anticipated the constraints behind the question, for example caps on admission places. It filled in concrete examples from memory, for example the names of well-known swimmers. And it anticipated a deeper question, for example long-term follow-up studies. As a result, a research article answering "what happened later to swimmers who were slow at age 12" was cited, even though the user had never asked about that.

Different types of question were also rewritten in different ways. Shopping questions had specific brand models written in, plus specification words such as price, weight and battery hours. Health questions had evidence-level words added, such as clinical guidelines, systematic reviews and randomized trials. Local service questions had verification words added, such as official, reviews, licence and address.

More directly, quite a few conversations already named a website in their first search term. In 7 of the 30 conversations for the three categories, and 6 of the 10 for the swimming question, the first search term used `site:` to target a specific website; shopping questions often targeted a product page on the brand's official website directly. This is direct evidence that "AI already has a list in mind before it goes online".

We also scored the pages AI had looked at using similarity in meaning. Scoring with the search terms AI generated separated the cited from the uncited better than scoring with the user's original sentence. Broken down by question type, the gap was clear only for shopping questions; local services and health questions pointed the same way, but the gap was not clear. We also ruled out the possibility that "AI first decided whom to cite and then wrote the product name into the search term": using only search terms without `site:`, or only the first search term, the result was the same. Meaning also mattered more than literal wording. Scoring by similarity in meaning separated the cited from the uncited moderately well; matching literal keywords alone, once the most-cited website was removed from the swimming question, was about as good as guessing. The exception was shopping questions, where exact terms such as model numbers made literal matching useful too.

> **A closer look:** "Separating" here is measured with an indicator called AUC, where 0.5 equals guessing and 1 means perfectly separated. Scoring by meaning gave 0.74 for the swimming question and 0.67 for the three categories; scoring shopping questions by keywords gave 0.71. AI's generated search terms scored 0.075 higher than the user's original sentence, with a 95% confidence range of 0.022 to 0.127, calculated by resampling conversations.

These results support the point of this section: what you need to match is the query AI rewrote. But they come from a small sample, one model, through the API, and they cannot represent the web version of ChatGPT, nor other platforms.

### Searching more does not mean searching wider

Intuitively, the more times AI searches, the more spread out its sources should be. The evidence does not support this intuition.

Researchers found in a controllable experimental system that so-called "deep research" AIs, meaning AIs that search many rounds in a row on their own and write long reports, tend after several rounds of searching to concentrate on a small number of pages of "user content that anyone can edit", such as community discussions and Q&A pages. In open-source deep research AIs, this kind of user content made up 16.7% to 23.4% of the URLs pulled back, and a single large community discussion site alone accounted for 53.7% to 70.7% of that user content. Looking at commercial deep research products, 12.1% of Gemini's citations were this kind of user content, against only 0.4% for the product from OpenAI (the developer of ChatGPT). One possible reason for the concentration is "whatever it reads first, it keeps searching in that direction", because what to search in the next round is decided by the content already read. One experiment with a fixed set of candidate documents (weaker evidence) found that when two searches differed only in the order of the documents, by round 4, 63.9% of the search terms were already different and 75.0% of the documents read were in a different order.

Tests by people in the industry (repeated tests with a control group) saw a similar phenomenon. From 8 August 2026, ChatGPT's search behaviour suddenly changed: the sources pulled back per answer rose from about 11.7 to 18.9, an increase of 61%, and distinct URLs rose by 69%, but distinct websites rose by only 9%; the number of pages taken from the same website in a single answer rose from 1.38 to 2.20. ChatGPT was reading deeper into the websites it already used, not discovering new ones. Websites that were not on the shortlist before 8 August were not pulled in just because AI searched more.

**What you need to match is the few sentences AI rewrote, and AI searching more will not automatically bring you onto the shortlist.**

## 4. Principle three: change the phrasing, and you may vanish from the list

Once AI has rewritten the query, it finds pages by similarity of meaning. This is called semantic matching. It doesn't count how many times a keyword appears; it compares whether what this page talks about resembles what this query is looking for. So the words on your page, what you call your own category, the task you describe and the kind of buyer you write for decide which queries can pull you in. Call the category something else, or ask the question as a different kind of buyer, and a different batch of pages gets pulled back.

The strength of the evidence for this principle needs to be made clear first. Research evidence is relatively thin, and it comes mainly from repeated tests by people in the industry. On the research side there are only two points of indirect support: first, rewriting queries changes sources substantially (the previous section); second, covering the rewritten query wording in a page helps it get adopted.

### Three sets of tests by people in the industry

The three sets of tests below were all done by people in the industry, with repeated tests and a control group.

The first set of tests asked about exactly this: "shared inbox software". The tester asked in two ways. One was the category-name phrasing, "best shared inbox software", and the other was what a real user would say, "How do we handle a shared mailbox together without disrupting our usual email flow?" Each phrasing was asked 10 times on each of four AIs. When asked by category name, the two main tools were named almost every time. With the descriptive phrasing, one of the tools went from "appearing every time" on ChatGPT to "0 out of 10". The tester also tracked two other tools as a control, and they were stable under every phrasing. What these two tools had in common was that their pages described the actual workflow in the buyer's own language, rather than just saying "we are a shared inbox software".

The second set of tests changed the buyer. A certain newsletter platform appeared only in phrasings where "the buyer is a creator". When the buyer was set as "a business" and the task was described only in plain language, it dropped to 0 out of 40. If all the phrasings are mixed together to calculate an average "visibility score", this difference is completely hidden. You would think you were doing quite well, when in fact, in front of a whole group of buyers, you don't exist at all.

The protagonist of the third set of tests was a brand-new author, meaning an entity that had not previously existed on the web. For 99 consecutive days, the tester tested three AIs each day with 16 fixed questions. In the 10 questions that "do not mention the author's name and only ask AI for recommendations", AI answered 6,729 times in total, and this author was named only 40 times, 25 of them from the same question. That question used the name of a niche genre the author had coined, a term that did not previously exist on the web. As for phrasings like "are there people similar to [famous author]", each question was asked about 700 times, and the author was named 0 times. When AI was asked directly by name "who is this author", from about day 49 onward the author was mentioned in a stable 72% of answers. This shows that AI could find this author, and the problem was not that "search engines hadn't indexed them". A self-coined term could be pulled in; "similar to whom" could not.

The tester has an interpretation of these results, but it is an opinion, not yet proof: other people's word of mouth (third-party comparison lists, reviews, discussion threads) decides whether you can get onto the recommendation list, while the language on your page describing concrete workflows decides whether you can stay on the list when the phrasing changes.

### Other clues

There are also some individual observations that can only be treated as clues. Someone in the industry observed that when the same marketing services firm was asked about using the niche term it was known for, it was named 19 times out of 25; when asked using the two broad category labels on its home page, it was named 0 times out of 25 both times. Calling the same category by a different name once made a brand's mention rate drop from about three quarters to zero. In the local business data of one city, about 42% of businesses changed whether they were recommended simply because the wording of the question was different.

The type of intent behind the question also matters. Phrasings like "what can replace [product]" cite comparison pages about 10 times as often as phrasings like "best [product]"; what makes the difference is the type of intent, and it has nothing to do with whether the question contains a brand name. Someone else reported that when no other explanatory source could be found, Google's AI Mode and AI summary cited social platform content whose wording almost exactly matched the question word for word.

Taking all this together, semantic matching and "keyword density" are two different things. **What decides whether you are on the shortlist is whether your page uses the set of phrases buyers say and AI rewrites, to describe the problem you really solve.**

## 5. Principle four: language and location are a "market gate"

Ask the same question in a different language, and the queries AI rewrites also turn into that language; once sent into the search system, what comes back is the web of that language. Changing the language is like changing to a different library: the shortlist is replaced wholesale, which is far from a minor adjustment. In addition, the user's network location when going online, meaning the country the internet service shows them to be in (technically called the "exit IP"), affects which country's user the search system treats you as.

### Five phenomena research has seen

Researchers ran repeated tests on real AI search and saw five phenomena.

First, changing the language replaces almost the entire set of websites. When GPT is asked in a different language, the overlap of the cited websites is close to 0; Claude is the most stable in this respect. Moreover, changing the wording within the same language has less effect on the cited websites than changing the language.

Second, local brands gain the most. Researchers collected 35,640 answers in 12 European languages from 3 AIs that go online. When the question was asked in the language of the brand's home country, the recommendation share of the local leading brands rose by 0.80, while global brands rose by only 0.15. The average content similarity between answers in different languages was 0.825 (1 means identical), slightly higher within the same language family than across families (0.844 against 0.820). The tone of the answers also changed with the language, and English answers were the most negative.

Third, the share of local sources changes by multiples. In Google's AI summaries on health topics, when the question was asked in English, the share of citations from each country's local sources varied widely: 48.2% for Australia, 33.7% for the United States, 2.3% for India and 0.2% for Nigeria. When the question was asked in the local native language instead, the share of citations from local sources rose 3.5 to 13.5 times, for example from 16.6% to 57.5% in Japan, and from 2.7% to 36.4% in South Korea.

Fourth, language decides "choose the local one", and location decides "which country's local one". This is a small-sample study, with 234 tests in total and each group repeated 6 times. When asked in English in Istanbul and Tallinn, local providers did not appear once in 12 tests; when asked in the local language, global providers appeared only once in 24. More telling still, a person in Berlin asking in Turkish got local German accounting software providers (5 of 6 times); a person in Tallinn asking in Russian got local Estonian providers (4 of 6 times). **The language of the question swaps the shortlist wholesale for "local-type" providers, while the location decides which country's local ones.** The study also had a control category, project management software, and this category showed no language effect. The researchers speculate that this may be because categories like accounting are affected by each country's regulations while project management is not, but this speculation has not been verified.

Fifth, different AIs read location in different ways. Researchers tested 31,200 answers on real AI search. ChatGPT looks at the location the app tells it, precise down to the city; it writes the place name into the search terms itself, and even when the search terms contain no place name, the search system still changes sources according to the location; it ignores which network you are actually connecting from. Gemini is the exact opposite: it ignores the location it is told and looks only at the country the network is in; even for questions unrelated to location, quite a few of its sources change, but it cannot distinguish down to the city level. The recommended businesses were very unstable: asking again in the same city gave only 32% the same; in a different city, only 8% remained.

Two additional points need to be remembered together with the above. Whether answers are stable depends mainly on which AI it is, and has little to do with which language is used: in the study's statistics, "which AI" explained about 0.319 of the differences, while "which language" explained only about 0.011. In addition, the language gate replaces the local layer, not all sources. In 11 of the 12 languages, the most-cited website was the same online encyclopedia.

### Observations from people in the industry in different markets

The following are tests by people in the industry, and no one has independently verified them.

In less widely spoken languages, new terms are easily misunderstood. Someone asked five AI search tools in Finnish: "Which is the best GEO agency in my area?" Only two of the tools understood it as a marketing service. The other three recommended, respectively, land surveying firms, agricultural earthworks contractors, and an outdoor game called geocaching. The reason is that in a language with relatively little web content, a short question doesn't give AI enough context to work out the meaning of a new term.

The city has to be written into the sentence; writing it into the settings is not enough. A logistics company serving about 8 cities in India tested 41 questions that buyers would ask and was named 0 times. With AI's location set to a particular city and general questions asked, it was still 0 out of 3. Once the city name was written directly into the question, Gemini named it all 3 times; Google's AI summary named it in two cities, and only in the cities for which it had a matching city page. Note that this observation holds only for Gemini and Google's AI summary. The research behind the fifth phenomenon above shows that ChatGPT does follow the city that is set.

Each market's local ecosystem is also different. Someone asked ChatGPT "GEO agency + city name" in 19 cities, and of 94 agencies, 97% had their official website cited. The share of citations going to "business profiles" (the business information pages on search engines) was 86% in India's large cities, only 18% elsewhere, and about 15% in other emerging markets. This is a feature of a single market, not a common pattern across all emerging markets.

Someone else in the industry observed that directly translating an English question list into other languages is not enough, because people who speak different languages ask buying questions in different ways to begin with. In addition, if you find that AI answers in the local language but cites English web pages, this shows that the local-language web has very little content on this topic. In that case, a decent local-language page may quickly be cited.

So results measured in English cannot represent the local market. **Language is a gate, and on the other side of the gate is a whole different shortlist.**

## 6. How reliable is this evidence

The sources and strength of the evidence for the four principles are not the same, and it is clearer to look at them separately.

The evidence for Principle one, "sources don't overlap", is the most solid. It comes from several repeated tests on real AI search, including peer-reviewed research, and large-sample tests by people in the industry point the same way. Its strength is that several independent teams, different AIs and different times all lead to the same conclusion. Its weakness is that some studies used very few questions, for example only 15, and some researchers themselves sell visibility measurement services, a conflict of interest.

Principle two, "rewriting makes sources unstable", likewise comes from repeated tests on real AI search, including peer-reviewed research; the finding that "deep research AIs concentrate on a few pages" was seen in a controllable experimental system. The ranking stability and "re-search" experiments directly measured the effect of rewriting, which is its strength. Its weakness is that what the rewritten queries look like in detail comes mainly from data intercepted by people in the industry, and Google's split-off smaller queries were inferred, not seen directly.

The evidence for Principle three, "wording decides the shortlist", is mainly tests by people in the industry, repeated and with a control group, with only indirect support on the research side. These tests had control groups, repetitions and long-term day-by-day records; but most tested only one category or one subject, and the mechanism behind them is only the testers' speculation.

Principle four, "language and the market gate", comes from three or more repeated tests on real AI search, covering 12 European languages as well as health topics in Asia and Africa. The effects are large, the direction is consistent, and different studies can reproduce them. The weakness is that "location decides which country" was tested on only one AI, 6 times per group, a very small sample; and the authors of two of the core studies also sell visibility measurement services.

When using this evidence, there are three more things to remember. **All of the above are observed phenomena; none of them proves causation.** They show how the shortlist changes, but no randomized experiment has proven that "changing a page's wording raises the probability of being pulled in, and traffic or sales rise along with it". Second, AI is updated very often. The sudden change in ChatGPT's search behaviour on 8 August shows that any specific figure (how many queries per search, how many pages cited) has a shelf life. Finally, the research finding that "covering rewritten query wording works" comes from websites the researchers set up themselves, and what it measured was "share of adopted content", not the success rate of real commercial websites.

## 7. What is still being debated

### Dispute one: can you see the queries AI splits off?

Accounts from people in the industry contradict each other. Some say ChatGPT lets you see its rewritten queries while Google's two interfaces (AI Mode and the AI summary) do not; others have seen ChatGPT's rewritten queries through the browser's developer tools. Yet another person's test says that Claude and Perplexity disclose the split-off queries, while ChatGPT and Gemini do not.

Someone else tried to get these queries through a third-party programming interface and got only 1 to 3, mostly small variations on the original keyword, and sometimes none at all; another person tried 6 times and got at most 3. The same person compared them and found that the "fan-out queries" produced by simulation tools were more useful, but those were "simulated" with prompts, not the queries AI actually sent.

Our view is that whether you can see them changes with the interface, the version and the time, and contradictory reports may each have been true at the moment they were tested. Simulated "fan-out queries" are only guesses and cannot be treated as observed data.

### Dispute two: whose search data does ChatGPT use?

The industry widely believes that when ChatGPT searches online, it uses search data from both Bing and Google. But this view is disputed; supporters outnumber opponents by a little over three to one, and that is not proof. OpenAI's official documentation confirms that ChatGPT search uses "third-party search providers" in addition to its own index, but does not say which ones. So whether it is Bing or Google has no answer yet. One industry study reported that 83% of the products in ChatGPT's shopping recommendation panel came from Google's shopping data through shopping-related fan-out queries. This can serve as supporting evidence, but it covers only the shopping scenario.

### Dispute three: does setting a location help?

One small-sample study says the location you connect from (the exit IP) decides which country's providers AI recommends. Tests by people in the industry say that with a location set and a general question asked, local businesses were still named 0 times, and it only helped to write the city name into the sentence. The two do not necessarily contradict each other. One possible explanation is that location works at the "country" level, while localisation at the "city" level needs the question itself to carry the place. But so far no study has tested these two things in the same experiment.

### Dispute four: are users' questions long or short?

There are only a few single-point observations from people in the industry on this. Someone cited two user surveys indicating that most questions are short, about two thirds within 15 words, close to traditional keyword search, but that more and more people add personal context such as budget and location. Someone saw in clients' website data that about 60% of questions were just search terms. Someone else believes that in the categories they know, questions run to about 20 words, and that questions have actually become shorter because AI remembers earlier context. Yet another person found that conversational queries as long as a whole paragraph have started appearing in Google Search Console.

These are all individual observations. For the "can it find you" gate, what matters more is the query after AI rewrites it; the length of the user's original sentence is secondary. Whether the original sentence is long or short, what is finally sent into the search system is the rewritten version. In addition, real conversation logs show that a sentence is often short because conditions such as budget and location were already stated in earlier rounds (see Chapter 9). Testing with an isolated short question may miss these conditions.

### Dispute five: is it other people's word of mouth that keeps you stable, or the wording on your page?

In the "shared inbox" wording test earlier, even the tester could not cleanly separate the two factors. What kept those tools appearing steadily may have been that their pages described workflows in the buyer's language, or it may have been the large number of third-party comparison lists on the web at work. The tester's provisional view is that "other people's word of mouth gets you in, and the wording on your page keeps you there", a hypothesis that has not yet been tested.

### Dispute six: is AI searching more a good thing or a bad thing?

For content owners, AI searching more means more entrances through which you might be pulled in. But in a controllable experimental system, repeated searching concentrated instead on a small number of user content pages "that anyone can edit", creating a weakness that is easy to attack. Adding about 13 words to one URL got it pulled into AI's reference material in 57% to 76% of tests; 34% to 61% cited it, and 22% to 37% mentioned the brand or product named by the attacker in the report. The researchers tried two common detection methods, one checking whether the text is "unnatural" and one checking whether outputs are similar, and neither could detect it.

At the same time, people in the industry observed that after August, ChatGPT sharply reduced its searching of large community discussion sites, and the share of such sites among its sources fell from about 4% to 0.02%. So the statement that "social platforms are sources AI will always pick up" may not hold at all for different AIs at different times. Someone in the industry cautioned that for the same question, only about 11% of the websites cited by one AI appear among another AI's citations, so a change in one AI cannot be applied to other AIs.

## 8. Real cases

The following cases all come from tests or second-hand accounts by people in the industry, not research papers. Each case states what it can prove and what it cannot.

### A different phrasing, a different buyer: from 10 times to 0

The tester in the first case asked about shared inbox tools on ChatGPT, Claude, Perplexity and Gemini in two phrasings, 10 times each: one was the category name, and one was a real user's descriptive phrasing; two tools were also tracked as a control. When asked by category name, the two main tools appeared almost every time. With the descriptive phrasing, the AIs' responses diverged: ChatGPT named one of them 9 times and the other 0 times; Claude was the reverse, 8 times against 5; Gemini named both, 10 times and 8 times respectively; Perplexity named one of them 5 times and the other 0 times, and simply switched to teaching the user how to set things up in their own email software. The two control tools were stable under every phrasing, at most slightly unstable on Perplexity. This case shows that whether you get pulled in depends on whether the phrasing matches the wording on your page (Principle three), and that each AI responds in a different direction (Principle one).

The second case is the new author's 99 days. This author only went live on 11 May. The tester registered the measurement method in advance, asked three AIs that go online 16 fixed questions every day, and scored more than 11,000 answers in total. For questions naming the author directly, the mention rate settled at 72% from about day 49 onward; in questions that did not name the author and asked AI for recommendations, 25 of the 40 mentions came from the one question that used the author's coined term; phrasings like "similar to [author]" got 0 out of about 700. This shows that a new brand or newcomer can be pulled in in the short term through their own coined terms (Principle three). But to be pulled in under "similar to [someone]" phrasings, other people need to mention you together with that famous person in the same piece of content, and this kind of third-party co-mention can't be produced within a few weeks.

### Location and language: one city name, one abbreviation

A logistics company serving about 8 cities first tested 41 buyer questions, then compared two approaches: "set the location + ask a general question", and "write the city name into the question". At first it was 0 out of 41; with the location set, it was still 0 out of 3; once the city name was written into the sentence, Gemini named it all 3 times, and Google's AI summary named it in two cities, and only where it had a city page. The location has to become part of the content of the question, and your website also has to have pages for the matching locations that can be matched (Principles four and three).

The other case happened in Finnish. Someone asked five AI search tools in Finnish, "Which is the best GEO agency in this area?", and three of them understood GEO as land surveying, earthworks, or the geocaching game. In a language with relatively little web content, a new term lacks enough context, and when AI rewrites a short question, it may pull in the wrong category altogether (Principle four). The tester's preliminary experience is that writing out the full name in the service description helps, but this has not been rigorously tested.

### ChatGPT reads deeper, but not wider

Someone in the industry used the same set of 961 questions to compare the sources pulled back in a total of 5,029 ChatGPT answers before and after 8 August. The sources pulled back per answer rose by 61%, but distinct websites rose by only 9%. Websites of government and official bodies increased sharply, while large community discussion sites and several media sites decreased sharply. The tester himself pointed out two caveats: his question mix leans toward health and finance and should not be treated as a general pattern; and he can only see that "it changed", not "why it changed". This case shows that searching more does not mean more diverse sources, and websites that were not originally on the shortlist will not be discovered just because AI searches more (Principle two).

### Aiming at the queries AI actually sends

A new website in a highly competitive category did not build pages for the sentences users would originally type, but for the fan-out queries ChatGPT split off; those fan-out queries already included the names of several well-known brands in that category. Within about a week, these pages were cited by ChatGPT for a very broad "best [type of tool]" question. The tester stressed that being cited is not the same as being recommended. Retrieval matches the rewritten queries (Principle two), but getting onto the shortlist is only the first step; whether AI picks you and recommends you is the subject of the next chapter.

So how do you capture the real fan-out queries? Someone in the industry who serves online shop clients asked the target question 5 times each on ChatGPT and Gemini, recorded every smaller query split off, and kept only those that appeared 3 or more times. One question for a kitchenware client yielded 14 smaller queries that appeared consistently. After that, he built one page for each query, using the wording of that query itself. In the month before this, his approach had been to write all kinds of synonymous sentences for users' phrasings and build pages for them; he made 9 pages, and all of them were wasted effort. What you need to match is the smaller queries AI really sends again and again, not synonymous sentences you imagined yourself (Principle two).

The evidence for the last case is weaker. Someone in the industry passed on a client case: this client gave up broad category terms and instead picked 5 to 6 phrasings from the buying stage, such as "best [product] for [use]" and "cheapest [product] that works well". They then first looked at which sources AI was already citing under these phrasings, picked out the ones they had a chance of competing with, and concentrated all their own content and their exposure on third-party websites on these few angles. The report says that within 90 days, this client went from almost invisible to appearing in 15% to 20% of relevant AI answers; the report also says the conversion rate of this traffic was about 4 times that of traditional search traffic. This is a second-hand account, not independently verified and without a control group, and the sales figures in particular should be treated with caution. This book's consistent judgment is that no research has yet proven that GEO reliably brings traffic or sales. The value of this case lies in showing an approach: **choose your battlefield by question type, and don't try to cover everything.**

## 9. Ideas that are already out of date

"I want to be number one in AI" is the first idea to let go of. The sources of different AIs barely overlap, and the same AI changes every day too, so there is no first place to fight over at all.

"If I rank first on Google, AI will cite me" is also out of date. Of the pages cited by Google's AI summary, only about one in ten are in the top 10 for the main query, and nearly 30% of the cited websites are not on the first page at all. For health questions, too, only about 44% of the pages in the traditional top 5 are cited by the AI summary. Ranking first still gives an advantage, but it is only one of the conditions.

"It's enough to optimize the keyword users will type" doesn't hold up either, because AI searches the rewritten query, and when rewriting it adds words, adds a year, and even adds brand names. "If AI searches more, sources will become more diverse" is not true either; research and industry data both show that searching more mainly means reading deeper into the websites already in use.

Last is "Do a good English version and just translate it." Changing the language means changing the whole shortlist, and people who speak different languages also ask questions in different ways.

## Key points of this chapter

Retrieval decides who is eligible to compete; pages that are not on the shortlist have no chance of being selected, cited or absorbed. There is also no such thing as "ranking first in AI": the URLs cited by different AIs barely overlap, the same AI swaps out a large majority of them the next day, and you can only look at "the probability of being pulled in" separately by AI, language, market and phrasing.

AI doesn't search for the sentence the user typed. It rewrites the question, possibly splitting it into several queries, adding a year, and even writing brand names in ahead of time; what you need to match is the rewritten query. Searching more also does not mean searching wider: repeated searching may concentrate on a few websites, or on a few user content pages that anyone can edit, and websites that are not on the shortlist will not be discovered just because AI searches more.

Change the phrasing, and a brand can go from "there every time" to "completely gone". The name of the category, the task described and the identity of the buyer all change the shortlist; brands that describe actual workflows in the buyer's language are more stable, which comes from tests by people in the industry, and the mechanism behind it has not been confirmed. The language of the question is a market gate: when the question is asked in the native language, the share of local brands and local sources rises sharply, and measuring in English cannot see the local market. The location needs to be written into the question itself: the place you connect from may decide "which country", but at the city level, the current evidence from people in the industry points to the question needing to contain the place, and your website also needing matching location pages.

Finally, being pulled in is not the same as getting traffic. The evidence in this chapter is all observed phenomena. After getting onto the shortlist, you still have to pass the two gates of selection and citation, and no research has yet proven that these reliably bring traffic or sales.

## Remember in one sentence

**AI doesn't search for the sentence the user typed, but for the few sentences it rewrote itself, searched in a particular language and in a particular market. Those few sentences are what you need to match.**

## What you can do tomorrow

1. Test and manage each AI separately, and don't use one "overall AI visibility score" to represent all AIs. Several repeated tests on real AI search all reach the same conclusion.
2. Test each language and each market separately, always test local brands in the local native language, and record for every measurement which language was used and which country or region you connected from. This comes from repeated tests on real AI search; the "location" part has only a small sample.
3. Ask the same question many times and look at the mention rate, not at a single screenshot. Researchers found on real AI search that for 4 out of 6 questions, the top recommendation changed when the question was asked again; even when asking again on the same device, the sources of Google's AI summary changed.
4. Cover in your pages the phrasings AI is likely to produce when rewriting, including qualifiers AI often adds automatically, such as the year. Researchers ran an experiment on real AI search using websites they built themselves, measuring "share of adopted content"; there are also test reports from people in the industry.
5. Capture the real fan-out queries: ask the same question several times on the same AI, keep only the smaller queries that recur, then use the original wording of that query to build a new page or add a section of content. This is a test report from people in the industry, and no one has independently verified it.
6. Describe the problems you actually solve and your workflows in the buyer's own language, rather than just saying "we are a [category] product". This comes from tests by people in the industry, repeated and with a control group.
7. Plan and test separately by phrasing type, including category-name, descriptive, comparison, "what can replace it", and "best / cheapest" phrasings, as well as phrasings from different buyer identities. This comes from tests by people in the industry, repeated and with a control group, though some parts are only single observations.
8. Build your own coined terms; a new brand can first be pulled in on the name of a niche genre it defines itself. This comes from tests by people in the industry, repeated and with a control group, but with only one subject.
9. If your business is tied to locations, build a dedicated page for each service location and test with "service + location" phrasings. This comes from tests by people in the industry, repeated and with a control group, but with only one company.
10. In language markets with fewer speakers, write out the full name of proper terms and add enough context, so that a new term isn't mistaken for an old one. This is a test report from people in the industry and has not yet been rigorously tested.
11. If a topic has very little content on the local-language web, give priority to building local-language pages. This is a phenomenon someone in the industry observed, and it can only be treated as a clue.

## Stop doing this

**Stop using measurement results in English to represent the local market.** Asking in English, you may not see your local competitors at all. In the same way, stop treating a single screenshot as evidence that "AI recommends me".

Stop stuffing keywords; in the AI search systems that have been tested, it had no effect at all on being pulled in. And stop building large numbers of pages for every synonymous sentence of users' phrasings; what you need to match is the smaller queries AI actually sends. Also stop treating the "fan-out queries" generated by simulation tools as observed data.

When testing local visibility, stop relying only on a VPN or AI's location setting; at the very least, also test the version that "writes the location directly into the question". Finally, stop applying a change in one AI to other AIs.

## What is still uncertain

**Can the queries AI splits off actually be seen?** Industry reports contradict each other, and the result may change with the interface, the version and the time. Simulated fan-out queries are only guesses.

**Whose search data does ChatGPT use when it goes online?** Most people in the industry believe it uses both Bing and Google, but this is disputed and unproven. OpenAI's official documentation only confirms that it uses "third-party search providers", without saying which ones. There is one piece of supporting evidence for the shopping scenario, but it is limited to shopping.

**Does a location setting actually help?** A small-sample study says "the location you connect from decides the country", and industry tests say "the city has to be written into the sentence". The two may each govern one level, but no study has tested them together yet. Another cross-country study on real search engines found that language decides results more than location does: for the same English queries across countries, the overlap of result websites was 0.58 to 0.80; switching to the local language, it was only 0.11 to 0.17. There is now research that has tested the two together, and the answer is that it depends on which AI (see Section 5).

**Are users' questions long or short?** All the claims are only individual observations. For this gate, though, the rewritten query matters more than the length of the original sentence.

**Is it other people's word of mouth or the wording on your page that keeps you appearing steadily?** At present the two can't be separated. "Other people's word of mouth gets you in, and the wording on your page keeps you there" is only a hypothesis waiting to be tested.

**Is AI searching more a good thing or a bad thing?** It brings more entrances, but it may also concentrate on a few editable pages, creating a weakness that is easy to attack; and different AIs at different times may behave in completely opposite ways.

**Why can wording make a brand disappear?** The phenomenon is supported by controlled tests, but the mechanism behind it is only the testers' speculation.

**Can changing a page's wording bring traffic or sales?** At present no randomized experiment has proven that "changing the wording leads to being pulled in more often, and traffic or sales rise along with it". The evidence in this chapter is all observed phenomena.

**Any specific figure in this chapter**, such as how many queries per search or how many pages are cited, may go out of date as AI is updated.
