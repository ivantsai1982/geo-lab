# Chapter 7: Being Listed Is Not the Same as Being Used

> This chapter covers the fifth and sixth of the seven gates: does it mention you (citation), and does it actually use you, and use you correctly (absorption). The earlier chapters were about how to squeeze onto the shortlist. This chapter is about something else: even once you appear in the source list below an AI answer, the story isn't over. These two gates are the ones most easily misread along the whole path.

## Opening: you're in the source list, but not in the answer

Imagine the owner of a cycling tour company. He put a lot of effort into writing a very thorough guide to cycling routes, with the routes, the difficulty, the supply points and the things to watch out for all written out clearly. One day he asks AI: "I want to join a cycling tour. Which companies do you recommend?" The answer appears, and the first entry in the source list below it is his guide. He is delighted.

Then he looks up at the body of the answer. The AI used the routes he had compiled and the cautions he had written, and in the end it recommended three companies, with prices attached. He was not one of the three. The guide he worked so hard on had become material for AI to write recommendations for his competitors.

The above is a hypothetical scenario, and the people and events are fictional, but the phenomenon behind it is real. Later in this chapter you will see that someone in the industry really ran into almost exactly the same thing.

This chapter makes only one big point: **being found, being listed as a source, having your content used, having it used correctly, and having your name said are several different things, and any one of them can get stuck.**

## Five questions this chapter answers

This chapter answers five questions in turn. First, if a web page appears in the source list of an AI answer, does that mean its content was used in the answer? Second, why are some web pages cited heavily while their brand name hardly appears in the answer? Third, how many of the statements in AI answers are actually supported by the sources, and what are the common kinds of "getting it twisted"? Fourth, when readers see a citation, do they tell whether it actually supports the answer? Fifth, when measuring the results of GEO, which layers should you look at separately, and what is the denominator for each layer?

## 1. "Being seen by AI" is actually not one thing

We often say "AI cited me", as if that means success. Let's go back to the book's very busy librarian. You ask him to look something up, a stack of books piles up on his desk, and finally he writes you a summary with a bibliography attached at the end. That bibliography actually hides several things that need to be checked separately. A book being in the bibliography doesn't mean he really read it and used it. The content he used may not have been copied correctly. Even if it was copied correctly, he may not write in the summary "this is what such-and-such book says". And the other way round, there may be books he clearly used but didn't list in the bibliography.

AI answers are the same. "Being seen by AI" can be broken down into at least the following path, step by step:

```
Found (enters the shortlist)
   ↓
Listed (appears in the answer's source list, that is, "citation")
   ↓
Absorbed (your content is actually written into the body of the answer)
   ↓
Used correctly (the answer faithfully presents what you meant)
   ↓
Named (the answer text says your brand or website name)
```

These layers don't pass along automatically. Getting through one layer doesn't mean you get through the next. At every layer someone drops out, and the reasons for dropping out differ. The citation layer answers "is your web page listed as a source?", and it is mainly decided by the process of finding and picking sources, which the earlier chapters covered. The absorption layer answers "is your web page's content written into the answer?", and it depends on how AI uses the material in hand when writing the answer. The faithfulness layer, "was it used correctly", answers whether the content written in is right, and it is decided by the combination of the AI model and the search system behind it. The naming layer answers whether the answer says your name, and the key is whether a given sentence in the answer needs to explain "who said this".

There is one more gap that is not in these four layers: every single citation can be correct and the overall conclusion can still be skewed. These four layers only check whether "the material that was read" was used correctly. Whether the material AI read can represent all the material that could be found is a separate question. An experiment with a fixed set of candidate documents (weaker evidence) showed that which documents deep research AI reads is affected by their order and by what it read first (see Chapter 6).

This book calls the fifth gate "does it mention you". This chapter splits it further, because "being listed as a source" and "having your name said" are two things, which are covered specifically later on.

## 2. Listed but not used: silent citation

Start with the first kind of gap: you are in the source list, but the answer doesn't use your content at all.

One study compared data from several platforms at a single point in time and calculated two things. One was how many sources are listed per question on average. The other was how much of each fetched web page's content is used in the answer on average, which the researchers call the "degree of absorption"; the larger the number, the more is used.

| Platform | Average number of sources listed per question | Average degree of absorption per fetched web page |
|---|---|---|
| ChatGPT | 6.88 | 0.271 |
| Google (AI Overviews / Gemini) | 12.06 | 0.058 |
| Perplexity | 16.35 | 0.065 |

From this table, platforms that list fewer sources actually use each source more deeply. The longer the source list, the thinner the weight of a single source in the answer may be. But this is only a description of data at one point in time and does not rule out other possible influencing factors. The evidence is weak, and all we can say is that it is possible in theory.

Researchers ran repeated tests on real Chinese-language AI search platforms and saw the same gap. Among the sources listed, 66% had content that entered the body of the answer, 30% were substantively cited, and only 8% were deeply cited. Another 39.3% were "silent citations": listed in the source list, while the answer used none of their content. The same study also found that of the brands appearing in citations, only 8.3% actually made it into the answer in the end.

Another study did a large-scale check on real AI search. It found that Google's AI Overviews list forum and Q&A community sites as sources, but the share of these sources actually used in the answer was about 22 percentage points lower than their share of the source list. Encyclopedia-type sources were the opposite: the share actually used was slightly higher than their share of the source list.

In plain terms, **the source list is more like "books I flipped through", not necessarily "views I adopted".**

## 3. Used but not listed: invisible use

The gap can also go the other way: your content is used, but not marked as a source. Researchers ran repeated tests on real AI search and found that 14% to 53% of the statements in answers actually had a basis in the search results, yet no citation was marked. The same study also found that 15% to over 20% of statements had no basis at all in the search results.

The range of 14% to 53% is wide because platforms differ a lot, but the meaning is clear. Looking only at the source list underestimates the real influence of some sources, because they were used but not listed. At the same time it overestimates the influence of others, because they were listed but not used, which is the silent citation of the previous section. So "how many times you were cited" is not a reliable indicator of "how much influence you have".

Invisible use doesn't only happen with text. Someone in the industry tested this themselves (no one has independently verified it). On a website he built for a local engineering business, an image appeared in Google's AI Overviews, yet the answer mentioned neither that website nor that business, and instead listed 4 other websites. **Content being used and who the content is credited to are two separate things.**

## 4. Used, but not used correctly

Even if your content is listed and used, the answer may still get it twisted. The main measurement results so far fall into two groups, by how they were measured.

The first group comes from repeated measurement on real AI search. In Google's AI Overviews, statements not supported by sources make up about 11%. The study checked 98,020 statements in total; "omitted" made up 7.0%, "wrong" 2.7% and "vague" 1.4%. Another set of measurements found that citations distorting the source's original meaning made up 30.6%. Inappropriate sources, where the source itself is not suitable for supporting that statement, made up 27.1%. Answers containing at least one problematic citation made up 71.3% to 96.1%, depending on the model.

"About 11%" cannot be treated as a general figure for all questions. Researchers on real AI search ran one large-scale check with 3,611 long, chat-like health questions (collected once). Among the statements that could be scored against their sources, an automatic judging tool found only about 47% supported by the attached sources; after correcting with the results of human checking, the estimate was about 57%, with a likely range of roughly 45% to 69%. A further about 21% of statements were factual statements with no source attached at all. This check used different tools, question types and ways of splitting statements from the "about 11%" study, so the two numbers cannot be compared directly.

The second group was seen under laboratory conditions. Cited URLs that don't exist at all, made up by AI, accounted for 3.0% to 13.3%. Also, as the number of searches rose, the pass rate on fact-checking fell: one model went from 78.6% at 2 searches to 16.7% at 150 searches.

Looking back at the breakdown in the first group, the most common problem is "omitted", far more common than "wrong". Premises and limiting conditions that were in the source get dropped from the answer.

### Five counter-intuitive things

The first counter-intuitive thing is that "getting it twisted" and "finding the wrong source" are two different problems, and one rises as the other falls. One study checked about 761,000 (761,495) pairs of "answer statement and cited source", covering 10 models. The model that twisted things least had a relatively high rate of wrong sources, and the model that twisted things most had the lowest rate of wrong sources. No model was good at both.

The second is that what decides these two things is mainly the search system behind the AI, and model size has very little effect. The "search system" here means the service behind the AI that is responsible for looking things up online, which the researchers call the "provider". For whether sources are appropriate, about 96% of the difference can be explained by "which company's search system is used". For whether content is faithfully conveyed, about 88% of the difference can be explained the same way. Within the same search system, switching to a larger model barely changed the rate of twisting, with a difference of less than 0.8 percentage points. Reasoning models that "think first before answering" clearly lowered the rate of twisting, with one model falling from 34.1% to 18.0%, but they had almost no effect on "whether sources are appropriate", with a change of less than 2 percentage points.

The third is that high-quality sources are not necessarily used faithfully. Researchers tracked Google's AI Overviews over a long period and found that the sources it cites do have higher credibility scores than the sites on the first page of results for the same search. But the correlation between "source quality" and "whether statements are faithfully conveyed" is only about 0.045. This number is close to 0, meaning the two are almost unrelated. That study, however, looked at general questions. The health-question check above found the opposite direction: compared with the traditional top 5 search results for the same question, pages cited by AI Overviews scored slightly lower on 4 of 6 credibility indicators and leaned more towards commercial health information websites, though the gaps were all small. The second half agreed: for health questions, neither source quality nor whether statements had source support could meaningfully predict whether the answer was right by doctors' standards. For now the two results stand side by side. The difference may come from the domain (general questions versus health questions), or from the level measured (whole websites versus single pages).

The fourth is that a link that opens and relevant content do not mean the facts are supported. Under laboratory conditions, for 12 of 14 models, over 94% of links opened normally, and for the most advanced models, over 80% of cited content was relevant to the question. Yet the share that actually passed fact-checking was only 24% to 77%.

The fifth follows from the fourth: first confirm that cited URLs actually exist. Under laboratory conditions, 3% to 13% of cited URLs had no archive record at all and very likely never existed. Deep research AI, meaning AI tools that run many rounds of searches on their own and write long reports, made up URLs at a higher rate (10.7%) than ordinary AI that searches online (4.8%). Some models listed about 4.3 times as many citations, but the share of URLs that wouldn't open or couldn't be found was also about 2 times higher.

Beyond these five, there is one more way of getting things twisted that businesses should watch out for: AI turns "maybe" into "definitely". Researchers ran repeated tests on real AI search and found that once search is connected, answers contain less hedging language than the sources themselves. In one system, hedging language fell by about 40%, and in Google's AI Overviews it fell by about 60%. Where the source says "may" or "in some cases", the answer may state it as a definite conclusion.

## 5. With a citation, people just believe it

You might think that even if AI cites things messily, readers can just click through and see. That isn't how it actually works.

One randomised survey experiment involved 4,927 people in total and used 9 questions. Each person saw a fixed screen prepared in advance by the researchers, not a situation of really using AI, so the readers' reactions were real but the screens were designed. The study used scores from 1 to 7. Attaching reference links to the answer raised readers' trust by 0.091 points and their willingness to share by 0.121 points. Whether the links were valid, or invalid, or even made up by AI, made almost no difference to trust: the gap was -0.021 points, which can be treated statistically as no difference. By contrast, flagging "this point is still uncertain" lowered trust by 0.157 points.

Another study, on real AI search, analysed 24,069 conversations and 12,652 user votes, in which users chose which of two answers they preferred. Users preferred answers with more citations. More important, citations that really support the claim (an influence of about 0.29) and citations unrelated to the claim (an influence of about 0.27) had almost the same effect on user preference. Only citations that contradict the claim showed no clear effect. This is correlation, not causation, and the data for the "irrelevant citations" part covers only about 800 conversations.

For ordinary readers, a citation works more like "looks well-founded" than "has been checked". This makes the problem in the previous section worse: **a twisted statement with a citation attached is actually more likely to be believed.** If it's your brand being twisted, the consequences are even more troublesome.

Looking at the answers themselves, the direction is the same. In that health-question check, researchers had an AI grading tool score each AI Overview against grading standards written by doctors; the grading tool had been checked against doctors' own grading beforehand. AI Overviews with no sources at all scored almost the same as those with sources (about 40.4% versus 39.2%, not a significant difference), and whether statements had source support was also unrelated to whether the answer was accurate. **For health questions, whether an answer carries citations has nothing to do with whether it is correct.** Overall, these AI Overviews scored only about 38.2% on the doctors' grading standards, losing points mainly by leaving out things that should have been said. On questions where doctors had specified a harmful or wrong claim in advance, 22.2% of AI Overviews stated at least one of them. High-risk questions more often got no sources at all (about 17.6%), yet were still answered. This is correlation, not causation. The researchers themselves cannot tell the reason apart: the answers may come mainly from the AI's own knowledge, or the citations may have been attached after the answer was written.

## 6. "I've used it for three months" becomes "some users report"

Many businesses rely on word of mouth from real customers, so here is a phenomenon you need to know about. Researchers examined 30,000 answers from the built-in AI Q&A feature of a social platform and found that AI changes what word of mouth originally looked like at two stages: picking comments and writing the answer.

At the picking stage, AI prefers comments that are already popular and formal in tone. Within the same discussion thread, for every "standard deviation" increase in a comment's score ranking (think of it as "clearly a notch higher"), its chance of being chosen was about 2.88 times what it had been. Top-level comments that are not replies to someone else were about 1.97 times as likely to be chosen, and comments with a formal tone about 1.49 times. Comments in a personal-experience-sharing tone were actually less likely to be chosen, at about 0.79 times. Comments pinned or specially flagged by moderators were almost never chosen.

At the stage of writing the answer, AI erases the "I". In the sources, first-person "I" language made up about 3.3%. In the answers only 0.06% remained; it almost entirely disappeared. So "I've used it for three months and the battery broke twice" gets rewritten as "some users report problems with battery durability". Who said it, and under what circumstances, disappear together, and personal experience is compressed into a generalised piece of advice.

This matters especially for brands that rely on good reviews. **Your good reviews may be handled this way too, and you have no direct control over what they get turned into.**

## 7. Being cited and being named are two different things

Putting the above together, you can see "being cited" and "being named" as two different processes. The path to being cited is: your web page matches the question, it is found, and then it is listed as a source. This is a "finding sources" problem. The path to being named is: a sentence in the answer needs to state where it came from, so the source or brand name is said. This is a "who gets the credit" problem.

To use the librarian metaphor, being cited is like the librarian "flipping through your book". If your web page happens to answer the question, it gets pulled in as a reference. Being named is like the librarian writing "according to such-and-such company" in the summary. The name appears only when a sentence must explain who said it.

To be honest, **no study so far has specifically proven the causal mechanism behind these two.** Several pieces of data are consistent with this division of labour, though. We saw the large number of silent citations earlier. Of the brands in citations, only 8.3% make it into the answer. The Chinese-language platform study mentioned earlier also found that a brand appearing repeatedly together across many different sources predicted whether it would be picked for the answer better than traditional Search Engine Optimization (SEO) quality scores did. This last point is also consistent with the book's repeated point that "what others say about you" matters a lot.

Reports from people in the industry who tested this themselves, and first-hand observations from several people in the industry, all point to the same phenomenon: the web page is used as a source, yet the answer names and recommends someone else. None of the three examples below has been independently verified, and they can only serve as clues.

### Three examples of being cited without being named

The first example comes from one person in the industry's test of 85 enterprise software companies, all of which sell software to other businesses. For each company he prepared 10 questions a buyer would ask, always used the same AI search, and recorded two things for each answer: whether it said the company's name, and whether it listed the company's own website as a source. For 29.4% of the companies, the number of times they were "listed as a source" was greater than the number of times they were "named". Of these, 9 were not named once in 10 answers, yet their own website appeared in the source list. After classifying 616 answers where "this company was absent", he found that which kinds of questions left a company absent varied with how visible the company already was. His interpretation is that these web pages answered the questions well, so they were pulled in as material, but the recommendation list went to brands with more "social proof", that is, brands that others review and discuss more. He also admits that he can't be sure whether being cited without being named has any effect. This is only a single set of data and can only serve as a clue.

The second example is an English-language news website that had been live for about three months. About 700 of its web pages were cited by AI, yet the site's name was mentioned only 5 times, roughly once every 140 citations. Of these citations, ChatGPT accounted for 659, Google AI Overviews 32, Google AI Mode 22 and Gemini 0. The site owner suspects that being cited is a matter of "finding sources": any web page that matches the question gets pulled in. Being named is a matter of "who gets the credit": a name is given only when a sentence needs a source to back it up. Much of the breaking news he reports is also being reported by other media at the same time, so AI has no reason it must say his name. His next step is to produce more original content, such as statistics he calculates himself and numbers no one else has, put the author's name next to the numbers, and then compare how often these articles are named. The results have not been published yet. This is only one website, and again it can only serve as a clue.

The third example is the real version of the fictional story at the start of the chapter. A small cycling tour company's website traffic was falling, and AI did not recommend it either. Someone in the industry set up about 17 questions for it and monitored them for around two weeks. They found that the company's web pages were consistently used as a source, yet the answers never mentioned its name. AI took the content of its guides and then named and recommended three or four competitors, with prices attached. In one question, AI used this company's web page as the primary source and still recommended others. This person's diagnosis was that the problem lay in how the web pages were written and had nothing to do with whether AI could read them: the company's brand name was not next to the key sentences, while its competitors put the brand, the facts and the numbers together. This is only one client and can only serve as a clue.

## 8. When you're described wrongly, the error often isn't on your site

The following examples of "AI getting a brand wrong" all come from the practical experience of people in the industry, and none has been independently verified either.

The first example is the head of marketing at a growing startup. Once a month he asks ChatGPT, Claude and Gemini a fixed set of questions, such as "what does this company do", "which tool of this kind is best" and "how do we compare with a certain competitor", and then records how AI describes the company, whom it puts alongside the company, and which sources it relies on. Twice he found AI repeating outdated or incorrect information. When he traced it, one case came from a very old directory page and the other from a third-party article that had got things wrong. This is a result someone in the industry tested themselves, with a fixed process and repeated checks, but no one has independently verified it. It shows that the problem of "getting it wrong" often lies not on your own website but in the third-party sources AI draws on.

The second example happened on ChatGPT and Gemini. A company had built up about 15 good reviews and 1 bad review on a social platform. When ChatGPT was asked about the company, the answer talked almost only about the bad review and warned the user to "be careful". Gemini mentioned the bad review but also explained that most reviews were positive. The tester tried this on 5 different devices from different network locations (IPs), and ChatGPT's output was the same every time. When the problem was pointed out in the conversation, AI apologised and corrected itself, but when a new user asked again, it went back to the negative account. This too is a result someone in the industry tested themselves and repeated across several devices, and no one has independently verified it. The example shows that AI does not use material in proportion: a few sources may be magnified out of proportion, and correcting AI in a conversation does not change the answer the next person sees. Many in the industry believe that a brand with negative discussion around it will still be mentioned, with the negative sentiment reflected in how it is described, but "many people believe" does not mean "it is right".

The third example is about price. A merchant updates prices every hour, and the product structured data on its web pages (price, currency, stock) is complete and valid, yet Google's AI Overviews kept showing last month's price band of 99 US dollars, not the current 79 US dollars. This was observed by one person in the industry, and it is the only example. Several authors in the community share the view that the prices in AI Overviews rely on an old version from the last time the web page was crawled, but this point is still disputed. It shows that "used correctly" also includes "talking about the present", which is a kind of distortion in time: structured data on a web page is no guarantee of being read in real time.

The fourth example is confusion caused by a shared name. Someone in the industry pointed out that all of one website's content was crammed into one large block of text, with several entities, that is, different products, companies and concepts, mixed together. On top of that, there happened to be two apps on the market with the same name: one a plugin for online shops, the other an image generation tool. As a result, Gemini couldn't tell which one was meant. This person tested it themselves and attached screenshots, but no one has independently verified it. Many in the industry believe that inconsistent descriptions of a brand across different places prevent AI from correctly understanding, classifying or mentioning that brand, but "many people believe" does not mean "it is right". This example shows that content being absorbed but credited to the wrong entity is also a way of "not being used correctly".

### Being cited doesn't always mean being opened

While writing this book, we ran our own tests on ChatGPT through the API (the method is in Chapter 4; the sample is very small, and no one else has independently verified it yet). We found that AI rarely opens web pages on its own. Across 30 conversations on three types of question, it opened pages only 16 times in total. In 10 conversations on the swimming question, it opened pages 37 times in total. Most citations were based only on the excerpts in the search results.

Take the new website cited most often on the swimming question (Chapter 3, Case 8). Its pages were cited 25 times (counted by conversation), and only 10 times did AI actually open the page. Looking more closely, the main data page was cited 9 times and opened 7 times; the other level pages with the same structure were cited 10 times and opened only 3 times; the research articles were cited 5 times and opened 0 times. This is only one website and 10 questions, so the evidence is very weak and it can only be treated as a case. Also, the API does not show which text AI actually received, so how much it really read can't be determined from the outside.

Research supports this phenomenon too. Researchers found on real AI search that a lightweight model did not open a single web page in 53.6% of its conversations. Under laboratory conditions, answers based only on excerpts had higher rates of being out of date (6.4%) and of citations not matching the original text (6.4%) than answers that opened the web page before citing (1.3% and 2.3%). Models differed greatly, with the share of conversations that opened no web page ranging from 2.6% to 76.0%.

From this we can infer (this is only an inference): **every page should have a passage that makes sense on its own when taken out.** Also, pages with a uniform structure may let AI, after reading one page, feel safe citing other pages of the same kind.

### Other scattered clues

There are a few more scattered clues, all single observations, for reference only. One person in the industry observed that when AI was asked how many members a certain community had, it cited an old figure from a blog post about 18 months old instead of the current figure. Another person in the industry contacted, one by one, the sources that AI answers drew on and asked them to correct wrong or outdated information, and succeeded about 70% of the time. He then added web pages on topics his own website hadn't covered, and AI's description of the brand gradually improved.

Someone in the industry also observed that, among about 30 companies with similar revenue, common AIs would miss products, give vague descriptions, put them in the wrong category, and even credit products to larger competitors. Another person in the industry reported that in two sectors, in the round of answering where AI "helps someone make a decision", it used on average only about 23% of the known brand facts, and the rest of the time fell back on a general impression of the whole category. His data is not public and can only serve as a clue. Yet another person in the industry showed with screenshots that Google's AI Overviews sometimes quote a passage from a source word for word, set apart from the surrounding answer.

## 9. How reliable is this evidence?

If you sort this chapter's main conclusions by strength of evidence, you will find that their reliability varies quite a lot.

The gap between citation and absorption, including silent citation and forums being listed but rarely used, comes from repeated measurement and large-scale checks on real AI search, and its reliability is moderate. Several independent studies point in the same direction, but the Chinese-language platform study was carried out by a company that provides AI visibility services, and another study used data from only a single point in time. The opposite directions of "how many sources each platform lists" and "how deeply each source is used" are only a description of data from a single point in time. The evidence is weak, all we can say is that it is possible in theory, and other factors have not been ruled out. Invisible use, that is, the 14% to 53% of statements used without being marked, comes from usage records on real AI search plus reruns under controlled conditions. Its reliability is moderate, but the range is wide and platforms differ a lot.

About 11% of AI Overviews statements lacking source support comes from 40 days of continuous tracking on Google's AI Overviews. Its reliability is moderate to strong, but it covers only Google's AI Overviews and popular questions. About 43% to 53% of cited statements lacking source support in long health questions, and neither citations nor source support predicting whether the answer is accurate, come from one large-scale check by researchers on real AI search (3,611 questions, 3 days), using an automatic judging tool and an AI grading tool, both spot-checked by humans or doctors. Its reliability is moderate; it covers only US English and long questions adapted from a conversational evaluation dataset, and there was no repeated measurement. Distortion at 30.6% and inappropriate sources at 27.1%, mainly decided by the search system, were obtained by putting questions to real AI through a programming interface and then actually fetching the sources to check them. Their reliability is also moderate to strong. The sample is very large, about 760,000 pairs, but it used a programming interface, which differs from the screen ordinary users see. The 3% to 13% of cited URLs being made up comes from laboratory conditions, and its reliability is moderate. The researchers themselves say this is a conservative estimate and the real figure may be higher. "The more searches, the less accurate the facts" also comes from laboratory conditions, and the evidence is weak, because only two models were tested and AI models were used as the graders.

The three conclusions about readers vary in strength. "Citation links raise trust, and whether the links are valid makes no difference" comes from a randomised survey experiment using fixed screens. The readers' reactions were real, but the screens were fixed, not a real usage situation. "Readers don't distinguish citations that support the claim from irrelevant ones" comes from real AI search plus a large number of user votes. Its reliability is moderate, but it is only a correlation, and the irrelevant-citation part covers only about 800 conversations. "Personal testimony gets generalised and the first person gets deleted" was obtained by examining a real platform's output from the outside. Its reliability is moderate, and only one platform's built-in Q&A feature was studied.

When reading these numbers, keep three more things in mind. First, most of the numbers come from English-language content and from platforms such as Google, ChatGPT and Perplexity; there is only one large study of Chinese-language platforms. Second, each study defines and calculates "absorption" and "faithfulness" differently, so the numbers can't be compared directly across studies; only their direction can be compared. Finally, the calculation method itself affects the conclusions. One study pointed out itself that its original finding that "long articles are over-used" was partly produced by the calculation method; after switching to calculating with averages, the degree to which short sources were underestimated shrank considerably.

## 10. Some common claims: how much do we know now?

The first common claim is "if AI cites you, it means it trusts you". The common view in the industry is that when AI cites a source, it trusts that information, while a brand that is only mentioned is merely "present". This is a view, not proof. What research has seen is a large gap between citation and actual use (silent citations make up 39.3%), many cases of content being used without being marked, and readers who don't distinguish whether a citation supports the claim. A safer understanding is that a citation may only mean "this web page matches the question", not necessarily "AI adopted what it says". Neither view currently has direct causal evidence.

The second claim is "switch to an FAQ format and you'll be used more", which is very common advice. A descriptive analysis of data from a single point in time found that the degree of absorption of Q&A-format web pages (0.0947) was slightly lower than that of non-Q&A pages (0.1005), while web pages containing code, numbers, definitions or comparisons had degrees of absorption 41% to 77% higher. But this is only correlation, other factors were not ruled out, and it can't prove that the FAQ format is harmful. All we can say is that there is no evidence that "switching to FAQ" by itself gets you used more. The information density of the content, and how closely it fits the question, may matter more.

The third claim is "the more AI searches, the better the answer". Intuitively, the more you look up, the more accurate the answer should be. Yet under laboratory conditions, both models showed that "the more searches, the lower the fact-checking pass rate": one fell from 78.6% to 16.7%, and the other from 80.0% to 57.9%. Another study, on real AI search, also found that one platform searching more often had only a mixed effect on answer quality. Both pieces of evidence are limited: the first tested only two models, and the second is only a descriptive observation. So for now we can only say that searching more doesn't guarantee more accurate citations. Another experiment with a fixed set of candidate documents (weaker evidence) looked at something else: the more rounds of searching, the better the material AI had read represented all the material that could be found. The average error (on a stance score ranging from −1 to 1) fell from 0.84 in round 1 to 0.41 in round 10, but did not disappear. So "more searching, more accurate citations" and "more searching, more complete evidence" are two different things, and neither lets you conclude that "fewer searches are better".

The fourth claim is "high-quality sources will be used more faithfully". In long-term tracking of general questions, the sources cited by Google's AI Overviews do have higher credibility than the sites on the first page of search results; but in one large-scale check of health questions the direction was reversed: pages cited by AI Overviews had slightly lower credibility, leaned more towards commercial health information websites, and gave lower shares to academic medical institutions and government sources. For now the two results stand side by side without forced reconciliation. For general questions, source quality and faithfulness are almost unrelated (a correlation of about 0.045); for health questions, source quality also barely predicts whether the answer is accurate. And "faithfulness" and "appropriate sources" also trade off against each other. **Working to become an authoritative source is not the same as making sure you are described correctly.**

The fifth claim is "deep research AI is more reliable than ordinary AI search". Overall, deep research AI made up URLs at a higher rate (10.7%) than ordinary AI that searches online (4.8%), but one deep research product had a rate of only 3.5%, below the average. The difference depends mainly on which specific system it is, and has little to do with the "deep research" category.

## 11. So what should you do?

### Step 1: do the accounting properly, recording layer by layer

The first thing is to split results into four layers and record them separately. At the naming layer, check whether the answer text says your name. At the citation layer, check whether you are in the source list. At the absorption layer, check whether your content made it into the answer. At the correct-description layer, check whether the content that made it into the answer is faithful. Researchers measured this many times on real AI search and saw large gaps between the layers every time, which is the reason for separating them.

Every layer needs a clearly stated denominator: is it "all the questions you asked", "the questions that produced an AI answer", "the answers that cited you" or "the answers that named you"? Definitions are generally inconsistent across studies, so stating the denominator clearly is a basic methodological requirement.

Next, don't use citation counts to stand for influence. Check for both silent citation (listed but not used) and invisible use (used but not listed); both gaps were measured repeatedly on real AI search. Before counting your share of citations, confirm that the cited URLs really exist and open, because under laboratory conditions 3% to 13% were made-up URLs. Finally, track the share of "cited but not named" as a separate indicator. This is something people in the industry have observed, and it is consistent with the gaps between layers that research has seen.

### Step 2: regularly check how AI describes you, and trace errors to their source

Use a fixed set of questions and regularly ask several platforms, for example "what does this company do", "which company do you recommend for this kind of product" and "how does it compare with a certain competitor". Record how AI describes you, whom it puts alongside you, and which sources it uses. This practice comes from tests people in the industry ran themselves, and no one has independently verified it.

When you find something wrong, trace it to the specific source web page. Errors often lie in third-party directories and old articles, not on your own website; someone in the industry tested this themselves, and research also shows that high-quality sources are no guarantee of being used faithfully. Once you find the source, contact it and ask for a correction. This is a single clue observed by someone in the industry.

Don't rely on correcting AI in a conversation, because when the next user asks, the answer may not have changed at all. This too is a result someone in the industry tested themselves, and no one has independently verified it. Also watch for a small amount of negative content being magnified, and check each platform separately. Someone in the industry tested this themselves, and it is also a common view in the industry.

### Step 3: make your content easier to absorb correctly and to be named

Put information-dense content on your web pages, such as clear definitions, numbers and comparisons. The basis for this is a description of data from a single point in time; it is only a correlation and possible in theory. Put the brand name, the facts and the numbers in the same sentence, or right next to each other, so that the sentence can be "credited" to you. This is a clue observed by people in the industry and has not been verified yet. Publish original data, meaning numbers no one else has, and state clearly who produced it. For now this is a hypothesis put forward by people in the industry, and there are no results yet.

Divide your content into clear sections, and don't let several entities get mixed together in one large block of text. If there are products or companies with the same name, make clear which one you are. Someone in the industry tested this themselves, and it is also a common view in the industry. Keep your brand information consistent across the web, and reduce outdated or contradictory third-party descriptions. This is a common view in the industry, and the Chinese-language platform study also saw that "appearing together across many sources" is linked to a brand being chosen.

Finally, be careful when writing about uncertainty. AI may turn "maybe" into "definitely", so write the key limiting conditions into the statement itself rather than in a separate paragraph. For example, write "effective under such-and-such conditions", not "Effective. But note that…". Research on real AI search saw that hedging language decreases once search is connected; this way of writing is inferred from that research and has not been directly verified.

### What not to do, and practices that are outdated

**Don't treat "being cited" as the finish line.** Being cited without being named may amount to supplying material for your competitors' recommendations. Also, don't use citation counts as an indicator of credibility or results, because models that cite more are not necessarily more accurate, and readers don't distinguish whether a citation supports the claim. Don't assume that high-authority sources will be described correctly; source quality and faithfulness are almost unrelated.

In the same way, don't look at only one platform. Twisting and wrong sources are mainly decided by the search system behind the AI, and platforms perform differently. Don't pile up large amounts of disorganised content for the sake of quantity either. Someone in the industry reported that the most visible brands are not necessarily used when AI helps people make decisions (a single clue).

Several practices are outdated or lack evidence. "Getting into the source list counts as success" is outdated; several studies show that citation, absorption and naming are clearly decoupled. "Switching to an FAQ format gets you used more" currently has no supporting evidence, and descriptive data even points slightly the other way. "Structured data lets AI read the latest prices or information in real time": an observation by someone in the industry and views in the community say it doesn't, the point is still disputed, and it can't be relied on. "Making AI search a few more times makes it more accurate": the opposite trend appeared under laboratory conditions, although the evidence is limited.

## Key points of this chapter

"Being seen by AI" has at least four layers: naming, citation, absorption and correct description. At every layer someone drops out, so record them separately when measuring and state the denominator clearly. Being listed is not the same as being used. On Chinese-language platforms, about 39% of listed sources are silent citations, and forum-type sources are listed in Google's AI Overviews but actually used less. Being used doesn't necessarily mean being marked either: 14% to 53% of statements in answers used the search results without a marked citation, so citation counts are not a reliable indicator of influence.

Being used is not the same as being used correctly. About 11% of AI Overviews statements lack source support (in one check of long health questions the share was much higher, about 43% to 53%), about 30% of citations distort the original meaning, and about 27% of sources are inappropriate. These two trade off against each other and are mainly decided by the search system behind the AI. A citation is itself a persuasion signal: readers trust an answer more because they see a citation, without telling whether the citation is valid or supports the claim. For health questions, whether an answer carries citations is also unrelated to whether it is correct. AI also generalises personal testimony: first-person experience is almost entirely erased when the answer is written, and at the picking stage AI prefers content that is high-scoring, top-level and formal in tone.

Being cited and being named are two different processes. People in the industry have observed many times that "the web page is used as a source, but someone else is recommended". Making a sentence creditable to you is a separate piece of work. In practice, the key is to keep checking whether AI describes you correctly and to trace the third-party sources of errors, rather than chasing citation counts alone.

## Remember in one sentence

**AI listing you, using you, using you correctly and saying your name are four different things; if you chase only the first, you may be writing recommendations for your competitors.**

## What you can do tomorrow

1. Prepare a fixed set of questions. Pick 5 to 10 questions customers really ask, such as "what does such-and-such company do", "which company do you recommend for this kind of product" and "how does such-and-such compare with such-and-such", and use the same set every time from then on.
2. Ask several platforms this set of questions and save the answers. Record how AI describes you, whom it puts alongside you and which sources it uses, and repeat this regularly, for example once a month.
3. Record four boxes for each answer: whether it named you, whether you are in the source list, whether your content was used, and whether it was described correctly. State clearly what the denominator is for each box.
4. Calculate one more number: the share of times you were "cited but not named".
5. Open every cited URL and confirm that it really exists and opens before counting it, and at the same time watch for "listed but not used" and "used but not listed".
6. When you find something described wrongly, open its source and trace which page caused it. If it is someone else's website (such as an old directory or an article that got things wrong), try contacting them for a correction.
7. Don't just correct AI in the conversation, because that doesn't change the answer the next person sees. What needs changing is the source.
8. Check for negative content on each platform separately, and watch whether a few bad reviews are being magnified.
9. Open your most important page and rework how it is written: check whether your brand name is next to the key sentences, put the brand, the facts and the numbers in the same sentence or right next to each other, and add more definitions, numbers and comparisons.
10. If you have original data, publish it, with numbers no one else has, and state clearly who produced it.
11. Organise your content into sections, and don't cram several things into one large block. If there are products or companies with the same name, state clearly on your website "which one we are, and which one we are not".
12. Check the various introductions of you around the web so that they all say the same thing, updating outdated ones and fixing contradictory ones.
13. Write limiting conditions into the sentence: write "effective under such-and-such conditions", not "effective" followed by a separate paragraph adding the exceptions.

## Stop doing this

**Stop treating "being cited" as the finish line.** Being listed as a source without being named may just mean you supplied material for your competitors' recommendations. Also stop using citation counts as an indicator of results or credibility, because more citations don't mean more accuracy, and readers don't distinguish whether a citation supports the claim.

Stop assuming that authoritative sources will be described correctly; source quality has almost nothing to do with whether something is faithfully conveyed. And stop looking at only one platform: the search systems behind each platform differ, and so does their performance.

Stop piling up large amounts of disorganised content for the sake of quantity; high visibility doesn't mean being used when AI helps people make decisions. Stop believing that "switching to FAQ gets you used more". There is currently no evidence for it, and the data even points slightly the other way.

Stop relying on structured data to let AI read your latest prices in real time; this point is disputed and can't be relied on. Finally, stop assuming that making AI search a few more times makes it more accurate. The trend seen in the laboratory was the opposite, although the evidence is limited.

## What is still uncertain

**What does a citation actually mean?** Neither "a citation means AI trusts you" nor "a citation only means the web page matches the question" has direct causal evidence.

**What is the causal mechanism behind being cited and being named?** No study has specifically proven it so far; the existing data and industry observations only point in the same direction. Whether being cited without being named has any effect also can't be determined for now.

**Does the FAQ format actually affect absorption?** The existing data is only correlation, so we can't say it helps, and we can't say it harms. In the same way, whether "the more sources listed, the less each source is used" holds rests only on descriptive data from a single point in time. It is possible in theory, but not yet proven.

**Are the sources cited by AI Overviews more or less credible than search results?** Long-term tracking of general questions says more credible; one large-scale check of health questions says slightly less. The difference may come from the domain, or from whether whole websites or single pages are measured. There is no settled answer yet.

**What is the relationship between the number of searches and accuracy?** Only two models were tested in the laboratory, and real-world observations are mixed.

**Do the prices in AI Overviews rely on an old version from the last crawl?** This point is still disputed.

**Will putting the author's name next to original numbers get you named more often?** Someone is testing this, and the results have not been published yet.

**When a brand has negative discussion around it, is it still mentioned, just in a more negative tone?** Many in the industry believe so, but it has not been proven.

**How widely do these numbers apply?** Most of them come from English-language content and a few mainstream platforms, and there is only one large study of Chinese-language platforms. Studies define things differently, so the numbers can't be compared with each other directly, and the calculation method itself may also affect the conclusions.
