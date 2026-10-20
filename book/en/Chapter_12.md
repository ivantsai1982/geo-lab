# Chapter 12: Every AI Has Its Own Taste

## Opening: One question, three sets of answers

Imagine the owner of an online shop selling handmade leather goods. One morning she asks ChatGPT, "Where can I get a durable wallet made to order?" Her shop is in the answer, and she is delighted. At noon she asks Gemini the same question, and her shop is not in the answer. In the evening she asks a friend to try once more with another AI assistant. This time she has never heard of any of the shops on the list.

Same question, same day, same website, yet three AIs gave three sets of answers. That is what this chapter is about, and the idea behind it fits in one sentence:

**There is no single, unified "AI search" in the world. Each AI platform is an independent librarian, with its own library, its own habits and its own taste. Being recommended by one tells you almost nothing about whether you will be recommended by another.**

This chapter answers five questions in turn. First, why do we say there is no single, unified "AI search", and at which of the seven gates do the platforms differ? Second, what tendencies do ChatGPT, Gemini, Google's AI Overviews, Claude, Perplexity and Copilot each have when choosing sources, and how reliable are these tendencies? Third, how are Chinese-language AI platforms (the AI Overviews on Baidu's search page, Doubao, DeepSeek, Tencent Yuanbao, Tongyi Qianwen) fundamentally different from English-language platforms? Fourth, how does the language you ask in change the sources AI cites? Finally, when time and people are limited, which platforms should you track and optimise for first?

## 1. Every platform has its own seven gates

Throughout this book we have said that before AI answers a question, it passes through seven gates: whether to search, whether it can get in the door, whether it can find you, whether it picks you, whether it mentions you, whether it actually uses you, and whether people come over. This chapter adds one sentence: **every AI platform has its own set of seven gates, and the standard at almost every gate is different.**

We can picture a question's journey across different platforms as a road that forks several times. The first fork is whether to search. Some platforms rarely go online and mainly answer from what the model itself remembers; others search most of the time. The second fork is which library to search. The platforms that do search use different "libraries": some rely on Google's index, some on Bing's index, and some on their own real-time retrieval systems. The third fork is which kind of book it prefers. Once the material is pulled back, some platforms prefer their own content, some often use forums, some often use videos, and some mainly use generally published web pages. The fourth fork is what tone it uses. When writing the answer, some platforms say "I recommend…" in the first person, while others list items in a neutral tone. Platforms that do not search also reach this step in the end.

Every fork makes the answer more different, and by the end of the road you have different answers, different sources and different brands. So the same question, on the same day, with the same set of web pages, gets different results on different platforms. Being "visible" on one platform gives almost no information about whether you are visible on another.

### Exactly which gates the differences come from

Below we go through it gate by gate, saying how strong each piece of evidence is.

Start with gate one, "whether to search", where the gap can be several times over. Researchers ran repeated tests on real AI search, giving the same set of 1,000 questions to two models through the developer interface (API). GPT-5.3-chat went online to search for only 14% of the questions, while Claude Sonnet 4.6 searched for 83%. For the former, most of the time it is answering from what it remembers, so however well your website has been written recently, it may not have looked at it at all. One honest caveat: this was measured by replaying questions through the developer interface under controlled conditions. When ordinary people use the website or mobile app, the proportion may be different.

Gates two and three are about which library is searched and how much is pulled back, and here too every platform is different. Google's products, meaning Gemini and the AI Overviews on Google's search page, mainly rely on Google's own index. Google has a crawler token called Google-Extended, which websites can use to tell Google "do not use my content for AI training". Researchers ran repeated tests on real AI search and found that websites that blocked this token were cited zero times in Gemini, and were also cited noticeably less in Google's AI Overviews. However, this is a relationship of "appearing together" (correlation); it cannot yet prove that blocking is the cause (causation).

The amount of material pulled back each time also differs. According to real users' conversation data, ChatGPT pulls back an average of 14.06 URLs per query, while DeepSeek averages only 5.46, so ChatGPT's shortlist is about 2.5 times as long as DeepSeek's.

At gate four, "whether it picks you", the platforms prefer different sources. Researchers found through repeated testing that a large forum community site and YouTube appear in ChatGPT's and Grok's search results but did not appear at all in Claude's search results. This is an observation as of September 2026. Platforms also prefer their own things: Google's platforms lean towards citing Google's own assets, such as YouTube, and the AI Overviews on Baidu's search page mainly cite Baidu's own sub-sites. The next section covers this in more detail.

The tone of the answer also differs enormously. Researchers ran repeated tests on real AI search with product recommendation questions and found that 79% of ChatGPT's recommendations were delivered in the first person ("I recommend…"), against only 7% for Gemini and only 2% for Google's AI Overviews. This finding applies only to questions that ask for product recommendations. Even when you are recommended either way, readers feel differently about being told "I recommend this to you" by AI and being placed in a neutral list.

Last come gates five and six, "whether it mentions you" and "whether it actually uses you", where there is only one claim, and it is still uncertain. One analysis compared two figures across three platforms. The first is the average number of sources cited per question. The second is how much influence a single retrieved web page has on the answer's content on average; the larger the number, the deeper the influence:

| Platform | Average sources cited per question | Average influence of a single web page on the answer |
|---|---|---|
| ChatGPT | 6.88 | 0.2713 |
| Google | 12.06 | 0.0584 |
| Perplexity | 16.35 | 0.0646 |

These two sets of figures can be boiled down to one sentence: ChatGPT cites fewer sources, but each cited source has a deeper influence on the answer. That sentence needs a heavy discount, though. It comes from a single batch of data at one point in time, which the researchers call a "static snapshot"; it is the result of someone else reanalysing the data afterwards; and other possible influences were not ruled out. So it counts only as a description. At most it says "this is possibly how the mechanism works", and it cannot be treated as a law.

## 2. Platforms prefer their own things

Every platform tends to use its own content first. This comes from the structure of the platform itself and has nothing to do with the quality of your content.

Researchers found several examples on real AI search. On health questions, the source most often cited by Google's AI Overviews was YouTube, ahead of the websites of the US Centers for Disease Control and Prevention, the World Health Organization and well-known medical institutions. Google's own three interfaces also differ a great deal from one another: the sources used by traditional search, the AI Overviews and Gemini overlap very little. Measured with an indicator called the "Jaccard coefficient", the overlap is only 0.11 to 0.18, with 0.18 between the AI Overviews and the traditional search results. And the two interfaces that write answers lean more towards Google's own assets. Baidu shows the same pattern: the sources that appear most often in the AI Overviews on its search page are mainly Baidu's own sub-sites.

This "preference for its own things" finding is supported by two studies, covering health questions and general questions. Whether it is equally strong in other industries is not yet known.

> **A closer look: What is the Jaccard coefficient?**
> It measures "how alike two lists are". You take the number of items that appear on both lists and divide it by the total number of items on the two lists combined. 0 means they have nothing in common, and 1 means they are identical. 0.11 means that of the sources used on both sides, only about one in ten is shared.

What does this mean for you? On Google's and Baidu's platforms, "the platform's own content formats" are themselves a way in. That does not mean every brand must start making videos or open an account on the platform's sub-sites. Its real use is in analysis. When you are wondering "why aren't my web pages being cited?", first subtract the positions already taken by the platform's own assets, because some positions were never meant for ordinary websites in the first place.

## 3. How you look determines what you see

There is another, often overlooked, source of differences between platforms: the way of observing itself. Look at the same platform in different ways and you see different things.

AI platforms are usually used in two ways. One is the website or app that ordinary people use (called "the ordinary interface" below); the other is the API that developers call from programs. A large-scale check found that the websites returned by the ordinary interface and the corresponding API overlapped by only 12.0% (ChatGPT) and 14.8% (Gemini). **So using API results to stand for the answers ordinary users see is wrong.**

Asking once and asking several times also show you different things. This is what this book calls "rolling the dice". Ask ChatGPT once and you see on average only 2.65 websites; repeat the same question 3 times and the cumulative number of websites rises to 5.56. Asking only once seriously underestimates how many sources AI actually uses. Product recommendation lists also change from one ask to the next. Researchers used the Jaccard coefficient to measure how alike the lists were when the same question was repeated: 0.421 for Google's AI Overviews, 0.287 for Gemini and 0.178 for ChatGPT. The lower the number, the more the list changes each time, which means ChatGPT's product recommendations vary the most.

Phrase the question slightly differently and the sources change with it. Researchers rewrote questions slightly and then looked at how much the order of sources changed, using an indicator called "RBO", where 1 means the order is exactly the same and lower numbers mean more change. After slight rewording, Google's AI Overviews scored only 0.49, against 0.74 for traditional search results; with the question unchanged and rerun on the same device, Google's AI Overviews scored 0.69 and traditional search results 0.86. This shows that AI interfaces that write answers are less stable than the traditional row of blue links.

### Different versions, different listing and use

Different model versions also give different results. Someone in the industry ran repeated tests of their own with a control group and saw two examples. In the first, using the same set of brand-related questions, a fintech company appeared 3 times out of 10 in a larger model, while a smaller model recommended the same market leader every time, however it was asked. In another set of tests, the same company appeared 8 times out of 10 in the larger model and 0 times in the raw API with no system settings. These tests had a small sample and only a single client, but they show that different model versions under "the same platform" can also be two different worlds.

Finally, "being listed" does not equal "being used". According to real users' conversation data, 14% to 53% of answer content was in fact supported by search results that AI did not mark as citations, and another 15% to 20% or more of answer content could not be matched to any source at all. So if you measure a source's influence only by "was it cited or not", you will both undercount and miscount: cases where you were used but not credited are missed, and cases where you were credited but not actually used are counted when they should not be.

## 4. The Chinese-language ecosystem is not a translation of the English one

At this point, readers might assume that Chinese-language AI platforms are roughly English-language platforms in another language. That is not the case. Existing research points to three structural features of the Chinese-language ecosystem.

### Baidu's AI Overviews are highly concentrated

The first feature is that Baidu's AI Overviews are highly concentrated and prefer Baidu's own sub-sites. Researchers took 500 translated questions and asked each one once in Chinese and once in English on both Baidu and Google (collected only once). The results:

| Indicator | Baidu (Chinese questions) | Google (Chinese questions) | Google (English questions) | Baidu (English questions) |
|---|---|---|---|---|
| Share of questions with an AI Overview | 82.0% | 97.6% | 97.0% | 4.0% |
| Source concentration (Gini coefficient) | 0.895 | 0.500 | 0.462 | n/a |
| Share of citations taken by the top-ranked website | 27.1% | 6.6% | 5.5% | n/a |

Ask Baidu in Chinese and 82.0% of questions get an AI Overview; ask Baidu in English and only 4.0% do. The closer the Gini coefficient is to 1, the more citations are concentrated in a few sources. Baidu in Chinese scores 0.895, which means a handful of websites (mainly Baidu's own sub-sites) take most of the citation positions. In Baidu's Chinese AI Overviews, the top-ranked website alone accounts for 27.1% of citations; on Google, the figure is only 5.5% to 6.6%.

> **A closer look: What is the Gini coefficient?**
> It was originally used to measure whether wealth is evenly distributed. 0 means everyone gets the same amount, and 1 means everything is concentrated in one person's hands. Here, it measures whether "citation positions" are spread evenly across many websites or concentrated in a few.

The same study had an even more interesting finding. The websites cited by Baidu and Google overlap (Jaccard coefficient) by only 0.008 to 0.034, so they share almost no sources. But on the 331 questions where both sides gave answers, the researchers compared how close the "meaning" of the answers was, using a method called "semantic similarity", where 1 means the meaning is identical. The median was between 0.701 and 0.813, which is quite close. **The two platforms' answers say much the same thing, yet the sources they cite are almost entirely different.** For brands, the second part is what matters, because who gets cited decides who gets seen. The study has clear limitations: data was collected only once, the questions were translated, and data was collected from a single location (Milan, Italy).

### The language you ask in matters more than where you are

The second feature concerns the language of the question. Researchers studied which sources Google's AI Overviews cited for health questions. When questions were asked in English, the share of each country's "local sources" varied widely: 48.2% in Australia, 33.7% in the United States, 2.3% in India and only 0.2% in Nigeria. When questions were asked in the local language instead, the share of local sources rose by 3.5 to 13.5 times. Japan, for example, went from 16.6% to 57.5%, and South Korea from 2.7% to 36.4%. This was observed repeatedly on real AI search, but only for health topics, and it is an observational study, not an experiment that controls variables.

For Chinese-language content, this means users who ask in Chinese face a citation pool made up mainly of Chinese-language sources. On ChatGPT this needs a discount, though, because research found that for Chinese questions, the fast mode of the new version of ChatGPT searches only in English about 70% of the time. This cuts both ways. The upside is that Chinese-language content does not have to compete with authoritative English-language websites for the same positions; the downside is that the "authority" built up by English-language content does not automatically carry over into Chinese-language answers.

The same study also found that for questions about traditional Chinese medicine, Google's AI Overviews appeared about 42% of the time; Baidu showed answers more often, but attached only about 1 citation on average.

### The gap between "cited" and "actually used"

The third feature is that on Chinese-language AI platforms, the gap between "cited" and "actually used" is large. One large-scale study covered four platforms, Doubao, DeepSeek, Tencent Yuanbao and Tongyi Qianwen, counting the web version and the app separately for a total of 8 interfaces. The researchers asked 614 questions 3 times each on all 8 interfaces, collecting 160,860 citations in total.

Looking at the make-up of the sources, third-party sources (what other people say about you) accounted for about 69%, brands' own official websites for 12.9% and government sources for 4.5%. Being listed as a source does not mean being used, either. Of the sources listed, 66% had their content appear in the body of the answer, but only 30% were substantively cited, only 8% were cited in depth, and 39.3% were "silent citations", meaning they were listed but the answer did not use them at all. It is also hard for brands to get from the list into the answer: of the brands that appeared in the cited sources, only 8.3% actually ended up in the answer.

In this study, the strongest signal was being mentioned by many sources at once. When a brand appeared in only 1 citation, its rate of getting into the answer was 2.1%; when it appeared in 11 or more citations, the rate was 59.9%. By comparison, traditional SEO scores were not the most important factor. The researchers put a third-party composite score commonly used to assess websites' performance on Baidu into the prediction model to see how important it was, and its importance was only 4.52%. This shows it is not the main predictor, but note that it does not prove the score is useless.

Freshness also plays a part. For time-sensitive questions, the cited web pages had a median publication age of 18 days, with a "half-life" (the time it takes for the chance of being cited to fall by half) of 39 days; for questions that are not time-sensitive, the two figures were 101 days and 68 days.

The app and web version of the same platform also differ a great deal. The websites they use overlap (Jaccard coefficient) by only 0.19 to 0.51; for Tongyi Qianwen, comparing down to each individual URL, the overlap is only 0.014. This deserves to be stressed on its own: in the Chinese-language ecosystem, the app and web version of the same brand should be treated as two platforms.

Finally, a word on how credible this study is. The authors come from a company that sells monitoring services, and the data was collected by their own monitoring system. All the findings are relationships of "appearing together", not causation. The study's design itself is solid, though: it covers several interfaces and asks each question 3 times. The more reasonable view is to treat it as the most complete descriptive data on the Chinese-language ecosystem available so far, rather than as proof of cause.

## 5. How reliable are these claims

Put the findings above side by side and you can see that the strength of the evidence varies a great deal.

The most solid point is that the sources used by different platforms overlap very little. Several studies ran repeated tests on real AI search and agree; repeated, controlled tests by people in the industry agree too; and it is widely believed in the industry. The specific overlap figures, however, vary a great deal depending on how they are measured, as the later discussion of the dispute over platform overlap explains.

Several conclusions come from researchers' repeated tests on real AI search, but each has its own scope. The huge gap in "whether to search" (14% against 83%) was measured by controlled replay through the developer interface, and the ordinary interface may differ. ChatGPT's much higher share of "I recommend" compared with Gemini and Google's AI Overviews applies only to product recommendation questions. The absence of large forum community sites and YouTube from Claude's search results is also consistent with test reports from people in the industry, but it is an observation as of September 2026. Google's platforms preferring their own assets is supported by two studies covering health questions and general questions, and may not be as pronounced in other industries. Blocking Google-Extended is associated with zero citations in Gemini, but this is only correlation, not causation.

The high concentration of Baidu's AI Overviews likewise comes from researchers' tests on real AI search, but data was collected only once, with translated questions, from a single location (Milan). That asking in the local language greatly raises the share of local sources was observed repeatedly by researchers on real AI search, but only for health topics, and it is an observational study. On Chinese-language platforms, being mentioned by many sources at once predicts whether a brand gets into the answer; this also comes from researchers' repeated tests, but it is only correlation, and the authors are a monitoring service company.

Two more claims rest on weaker evidence. "ChatGPT cites less but uses its sources more deeply" goes no further than simulation and theoretical analysis; it is an after-the-fact analysis of a static snapshot and can only say "possible in terms of mechanism". The large differences between model versions come from repeated, controlled tests by people in the industry, but with a small sample and only a single client.

The overall judgement can be boiled down to two sentences. **The evidence that "platforms differ from one another" is very strong, and you can safely treat it as the premise for designing how you track; the evidence for "what each platform specifically likes" is much weaker, and it changes quickly.** The latter can only be treated as a current observation, and when you use it you should attach the date it was observed. The Chinese-language ecosystem also has an obvious gap: almost all the current evidence comes from research, and there are hardly any controlled tests by people in the industry on Chinese-language platforms.

## 6. Questions still being argued over

### Forum communities and citation counts

The first dispute is how much ChatGPT really relies on forum communities, and both sides have data. One side says ChatGPT favours forum communities most. Someone in the industry classified about 150,000 citations by source type and found that ChatGPT leaned most towards forums and Q&A sites (about 5%) and towards reference and academic pages (about 4%). In another set of tests looking at a single niche, 14 of the 16 community sources ChatGPT cited came from the same large forum community site.

The other side says ChatGPT hardly cites forum communities at all. Someone in the industry ran repeated, controlled tests, asking a fixed set of 40 questions in the same week: that large forum community site was cited 22 times by Gemini, 20 times by Google's AI Overviews, and at most once by ChatGPT. Another set of tests across 10 industries, using questions related to South Africa, found Gemini citing that forum about 750 times, while GPT-5 and Claude both cited it zero times.

Why did the two sides reach opposite results? There are three possible explanations: the observations were made at different times (the former in July, the latter in September); different things were tested, for example API versus the ordinary interface, and whether web access was switched on; and the industries were different. For your own brand, the answer to this question can only be found with your own prompt set. Chapter 15 is devoted to the relationship between platforms and forum communities. One more thing to note: even if a website ranks high among a platform's cited sources, its share of all citations may still be small. In the tests above, generally published material and ordinary web pages accounted for 86% to 97% on every platform, and no platform relied mainly on forums or videos.

The second dispute is which platform cites the most per answer, and two sets of data reach almost opposite conclusions:

| Data source | ChatGPT | Google's platforms | Perplexity |
|---|---|---|---|
| A static snapshot study (average citations per question) | 6.88 | 12.06 | 16.35 |
| Tests by someone in the industry (70 questions, 30 days, 1,474 answers; average citations per answer) | 9.62 | Gemini 15.08; Google's AI Overviews 5.34 | 5.04 |

Perplexity has the most in one set of data and the fewest in the other. The difference may come from how the data was collected, the timing, the type of question, and whether "Google" means the AI Overviews or Gemini. The lesson here is not about who is right. **"How many citations each answer has" is a product of the measurement method, and figures from different studies cannot be compared with one another.**

### Stability and overlap

The third dispute is which platform is the most stable. Research shows that, for the consistency of product recommendation lists when a question is repeated, Google's AI Overviews score highest (0.421) and ChatGPT lowest (0.178). On the other hand, someone in the industry ran repeated, controlled tests, rerunning 45 emergency repair questions across 15 cities in incognito mode. About 85% of Perplexity's results stayed the same, about two-thirds of ChatGPT's repeated, and Google kept the same recommendations in about 60% of cities while switching to someone else in 40%. Both sides show that ChatGPT varies a lot, but they disagree about Google. A possible reason is that one measured product recommendations and the other local services, and the latter's Google results also included the effects of personalisation.

The fourth dispute is how much platforms really overlap, and different measurement methods give very different figures. One study looked at the websites ChatGPT and Gemini share on average when answering the same question: only 5.4%, and 76.7% of the comparisons had no website in common at all. Another study measured the sources of Google's three interfaces and found a Jaccard coefficient of 0.11 to 0.18. Tests by people in the industry used two independent samples to check each other and calculated the pairwise overlap of cited websites: 10.6% to 14% between ChatGPT and the other three platforms, and about 25% to 26% between Google's AI Overviews and Gemini. Another set of industry tests looked at 197 clinics in the same industry, asking each question three times on three AI platforms, and found an overlap of 39% to 48%. Yet another set of industry tests looked at local recommendation lists and found a median overlap of 11% between the businesses named by Perplexity and by Gemini.

Someone in the industry pointed out that if you pool the cited sources of all the questions before calculating overlap, the large number of obscure websites that appear only once pull the figure down; if you compare question by question, the overlap may be somewhat higher. So "11%" and "48%" do not necessarily contradict each other; they may simply be calculated differently. One point both independent samples support is that ChatGPT has the lowest overlap with the other platforms, and Google's two products are closest to each other; Perplexity's position is inconsistent across the two sets of data.

### Speed of updates, separate versions, and preference profiles

The fifth dispute is how quickly new content is reflected. Many people in the industry believe Perplexity reflects new content faster than ChatGPT, on the grounds that Perplexity relies on real-time retrieval. One test report from someone in the industry said Perplexity reflected updates within a few days, while ChatGPT took several weeks; another test comparing several models said ChatGPT reflects content changes in about 2 to 4 weeks. But this view is still disputed. Its supporters offer only their own one-sided observations, none has run a controlled test, and "many people believe" does not mean "it is right".

The sixth dispute is whether to build a separate version for each platform. The "do them separately" camp argues that it is widely believed in the industry that each platform cites different sources, so you must track each platform separately; someone in the industry found in tests that in about 40% of cases, the brand ranked first on ChatGPT was nowhere to be seen on DeepSeek. In the "one main version" camp, someone in the industry observed that although the platforms' sources differ a great deal, concentrating on doing well in the two indexes of Google and Bing roughly covers most situations; another tester pointed out that the way the web pages themselves are written works across platforms, and what really differs by platform is "which external sources decide who gets named". The two camps can in fact be read together: **the readability of the web pages themselves and writing that AI can easily extract from need only one version; the layout of external sources (where other people talk about you) should be looked at platform by platform.**

The seventh dispute is whether summaries of "what each platform likes" can be trusted. A test report from someone in the industry drew "preference profiles" for each platform, saying ChatGPT values statistics and forum discussions, DeepSeek cares most about whether content is fresh, and Gemini is the most balanced and more influenced by structured data. Summaries like this call for great care. The claim that "adding statistics has the biggest effect on ChatGPT" conflicts with this book's main line, which is that the 2023 technique of "add data, add quotations" no longer works. The report's sample was also only 15 web pages over two months, and it published no control group. On top of that, the sources each platform prefers can change within a few months. So profiles like these can serve as hypotheses when you design your own tests, not as conclusions.

## 7. Real cases

The cases below all come from tests or observations by people in the industry, and each one states its limitations.

### After letting crawlers in, and after filling in the directories

The first case ran from June to September 2026. A website dedicated to answering "where can I watch a given drama in my country" covered 34 Asian markets. In June, the site owner had blocked AI crawlers because of bandwidth problems, and later lifted the block. On the content side, he built "data-driven" comparison pages using real catalogue counts, wrote no opinion pieces, and built separate pages for each country. The website's performance on Microsoft Copilot could be seen in the AI performance report in the search engine's official webmaster tools. Within 3 months it was cited about 185,600 times in Copilot's answers, and the number of pages cited per day grew from under 100 in June to about 400. Over the same period, clicks from traditional search also grew from almost zero to about 1,500 a day. The site owner said the moment the block was lifted was exactly when the curve began to turn.

Some of the results were unexpected. The most cited content was not the market the site had originally focused on, but comparisons of anime streaming platforms, which accounted for 7 of the 12 most cited questions. On another type of drama-related question, the site's pages supplied 61% to 85% of the sources in the answers. This case shows that "whether it can get in the door" is the first real threshold, and also that platforms go looking for sources that genuinely cover a given market, echoing the earlier discussion of language and region. But it is a test report by someone in the industry themselves, covering only one website, and no one has independently verified it; and lifting the block and improving the content happened at the same time, so it is impossible to tell which one caused the change.

The second case took about 1 month. A service company designed 10 industry-related questions, plus a few questions that asked about the brand directly. Each time they used an incognito browser and opened a new conversation for every question, asking on ChatGPT, Copilot, Claude, Gemini and Perplexity in turn, and recorded which sources each platform used and who the main competitors were. Whenever a source turned out to be an industry directory site, they created and completed their own profile on that directory and asked clients to leave reviews. Within a month, the company went from not being cited at all to being cited on 3 of the 5 platforms and for 6 of the 10 questions. The author also believes that Copilot and Perplexity rely more on traditional search rankings, so on those two platforms the only route is to improve traditional search rankings.

This case shows that the differences between platforms lie mainly in "which external sources they cite", so you need to read out the source list platform by platform and then fill in the gaps. It too is a test report by someone in the industry, and no one has independently verified it; "Copilot and Perplexity rely more on traditional rankings" is the author's own judgement, with no control group.

### Local businesses and news websites

The third case is a snapshot taken in August 2026. Someone in the industry chose 8 mid-sized US cities and 6 business categories, giving 48 markets in all. He first searched Google Maps for "category plus city" to get a list of businesses, about 97 per market and 4,657 in total. He then asked ChatGPT, Claude, Gemini and Google's AI Overviews three questions of the kind real buyers would ask, to see which businesses were named.

Only 11.9% of the businesses were named by at least one of the four platforms; with looser name matching, the figure was 26%. The number of businesses each platform named also varied a lot: Google's AI Overviews named 376, ChatGPT 206, Gemini 134 and Claude 92. Of the businesses that were named, 70% appeared on only one platform; in 36 of the 48 markets, not a single business was named by all four platforms. The differences between categories were larger than the differences between cities: the share of businesses named was 14.4% for gyms, 14.1% for coffee shops and 9.7% for hair salons. This shows that visibility on different platforms is four separate problems, not four measurements of the same problem. This is a test report by someone in the industry. Only the top 100 map results were taken, so businesses in large markets are undercounted; and strict and loose name matching gave very different results, as the author pointed out.

Another person in the industry, recording daily from August and accumulating 9,217 answers, added two points. First, local recommendation lists are highly concentrated: in 25 of 36 local lists, the same business was listed on more than 80% of days. Second, for questions of this kind, Perplexity mainly cites businesses' own web pages, plus a few directory sites and review sites.

The fourth case took place in September 2026. A news website's tracking data showed that about 650 to 659 of its pages were cited by ChatGPT, but 0 pages by Gemini. The author concluded that Gemini's problem was not whether it recognised the brand, but that it had never pulled these web pages back at all. This is a gap at the "whether it can find you" gate and has nothing to do with "whether your name is marked". There are two further pieces of circumstantial evidence. Someone in the industry observed that a large website removed from Google's index was heavily crawled every day by other platforms' crawlers, yet Gemini knew nothing about it. Another developer observed that his website got 230 users from ChatGPT in its first month, but Gemini never saw the site.

This echoes what was said at the start of the chapter: whether Google's platforms can find you is tied to Google's index. So if you are absent from Gemini, check your status in Google's index first, before talking about content. This evidence consists of test reports by people in the industry plus a few first-hand observations, none independently verified, and it can only serve as clues for troubleshooting.

### Many models, many versions

The fifth case took place in July 2026. A Romanian marketing firm asked the same question, "recommend luxury jewellery brands", in Romanian, of 10 models: ChatGPT, Claude, Gemini, Copilot, Grok, Perplexity, DeepSeek, Kimi, GLM and Tongyi Qianwen. The conditions were a clean conversation, no memory, and no brand names in the question; each model was asked only once, with no request to regenerate the answer.

Across the 10 models there were 50 recommendation slots in total, filled by 29 different brands, 19 of which appeared on only one model's list. Any two models shared on average only 0.91 brands, about 18%; even the most frequently named brand appeared in only 6 models. Copilot's list had no overlap at all with those of the other 9 models; its answer cited review counts, and the author inferred that Copilot relies mainly on Bing's real-time index and review aggregation sites. The two brands that made it onto several models' lists had something in common: verifiable third-party facts that appeared again and again across different sources, and coverage in financial media. This shows that being mentioned together by many different sources is a strong signal for being chosen, pointing the same way as the Chinese-language platform study described earlier. This is a test report by someone in the industry. Each model was asked only once, and no one has yet tested how much each model varies when the same question is repeated; that baseline is needed before anyone can tell whether "18%" is high or low.

The sixth case took place in May 2026. Someone in the industry tested questions such as "the best project management tool for remote teams" in three places: a larger model, a smaller model, and the raw API with no system settings. The same client appeared 8 times out of 10 in the larger model and 0 times in the raw API. The author believes that what really made the difference was a 2023 article in a tech publication and discussions from the same period on two software review platforms. These older citations had an effect across more model versions, outweighing any content published recently.

This fits with what was said earlier about ways of observing: different model versions have different training data cut-off dates, and their citation behaviour differs too. What a model already remembers (its brand prior) depends on an older, broader presence on the web. These are repeated, controlled tests by someone in the industry, but with only one client; "the old article made the difference" is the author's own inference, with no control group.

## 8. What to do

### First, get the measurement right

The first thing is to report each platform separately rather than combining them into a single "AI visibility score", because a total score averages away exactly the differences you want to see. This is supported by researchers' repeated tests on real AI search, and repeated, controlled tests by people in the industry agree. Measure with the ordinary interface, not just the API, because the websites the two use overlap by only 12% to 15%. Ask each question at least 3 times, because asking only once seriously underestimates the number of sources: on ChatGPT it goes from 2.65 to 5.56. Both points are supported by researchers' repeated tests on real AI search.

The measuring environment must also be clean. Log out, use incognito mode and open a new conversation for each question; otherwise your history will "feed" your brand back to you. Note that what you measure this way is the result of a single round of asking, which is not the same as what users see when they keep asking follow-up questions in the same conversation. This comes from repeated, controlled tests by people in the industry. You should also confirm whether the platform actually searched this time. One test report from someone in the industry found that a platform, while logged out, once did not go online at all, answered straight from memory, and misread an abbreviation.

Next, fix a prompt set, rerun it every week platform by platform, and record the model version and date, because platforms change and figures without dates cannot be compared. Questions that "ask about the brand directly" should be handled separately. When you ask "Is X suitable for Y?", the model repeats X back to you whether or not it actually found anything about X. That is an echo, not visibility. Both points come from repeated, controlled tests by people in the industry.

There is another step that is easy to overlook: test on another platform before deciding whether to change your web pages. Someone in the industry ran the same set of 16 questions daily and found that an entity was cited 25% of the time on one platform but only 12.5% on Gemini. If the platform itself cites from a narrow range, changing your web pages will not help. This too comes from repeated, controlled tests by someone in the industry, but with only a single entity, and the author says it is just one data point. Finally, track the app and web version of Chinese-language platforms separately, because researchers' repeated tests on real AI search found that the two use very different sources.

### Fill the gaps platform by platform

Once you have measured, read out, platform by platform, which sources your target questions cite, then sort them by "can you get onto it": your own website, review platforms, communities, open platforms where anyone can post, and competitors' own websites. Test reports from people in the industry show that between half and two-thirds of the cited web pages are usually within your reach.

If you care about Gemini and Google's AI Overviews, do not block Google-Extended, because researchers' repeated tests on real AI search found that blocking it is associated with zero citations in Gemini, though this is only correlation. When you are absent from Gemini, check your status in Google's index first, because whether Google's platforms can find you is tied to Google's index. This comes from several first-hand observations by people in the industry that point the same way, but it can only serve as a clue for troubleshooting.

**Make sure you appear again and again across multiple third-party sources.** In both the Chinese-language platform study and the multi-model tests, this was strongly associated with "being chosen"; the former is researchers' repeated testing on real AI search (correlation), the latter a test report by someone in the industry. Language and market must also match. Write in the language of the market you are targeting, and write Chinese content in Chinese, because researchers observed repeatedly on real AI search that when questions are asked in the local language, the share of local sources rises several times over (observational). Build separate pages for each country or market rather than a single generic page; the basis for this is the streaming website case above, which is a test report by someone in the industry and a single case.

Keep time-sensitive topics up to date. Researchers' repeated tests on real AI search found that on Chinese-language platforms, the web pages cited for time-sensitive questions had a median publication age of only 18 days (correlation). You can also publish content aimed at questions that "describe a problem". Several sets of test reports from people in the industry found that when users describe a problem rather than naming a product category directly (for example, "how can I get clients to pay faster?"), most platforms do not recommend any specific product. In Baidu's ecosystem, treat Baidu's own sub-sites as a structural given, because they take up a substantial share of citation positions. This is supported by researchers' repeated tests on real AI search, but there is not yet controlled evidence on exactly how to respond.

### Choosing with limited resources, and practices to drop

When time and people are limited, how should you choose? Someone in the industry, based on observations from 100 to 150 website analytics accounts, believes ChatGPT and Gemini bring the most referral traffic; another person in the industry observed that 98% of one client's AI traffic came from ChatGPT. These are all one-sided observations, and this book's main line points out that no research has yet shown GEO reliably brings traffic.

A sounder approach is to use your own prompt set to measure how absent you are on each platform, and why. The reason may be "it can't find you", a retrieval gap, or "it found you but didn't pick you", a selection gap. Once that is clear, set the order of your investment according to which platforms your audience actually uses. If you serve Chinese-speaking users, at least include the AI Overviews on Baidu's search page and the main Chinese-language AI platforms in your tracking, rather than relying only on conclusions drawn from English-language platforms.

There are a few things not to do. Do not use a screenshot from one platform to infer your performance on all platforms, and do not carry a success on one platform straight over to another; advice aimed at Google's interfaces in particular has been shown in tests not to transfer. Do not treat API results as the answers users see, and do not treat the result of a single ask as the system's fixed output. Do not treat "listed as a citation" as "used in the answer"; on Chinese-language platforms, 39.3% of citations are silent citations. And do not treat any "platform preference profile" as a stable rule.

Two ideas are also outdated. The first is treating "optimising for AI search" as a single goal. Platforms differ in whether they search, where they search, which sources they prefer and what tone they use, and one vague overall goal cannot tell you what to do next. The second is inferring your visibility in AI only from traditional search rankings. Several sets of industry tests found that brands ranking well on Google were absent from AI answers, and on Chinese-language platforms, traditional quality scores also had low importance for prediction. Traditional rankings are still the precondition for some platforms to find you, but they cannot stand for your visibility in AI.

## 9. Key points of this chapter

There is no single, unified "AI search" in the world. Platforms differ in whether they search, which library they search, which sources they prefer and what tone they use to write answers, so the same question gets different sources and different brands. The sources different platforms use overlap very little, and this is the best-supported point in the chapter; ChatGPT has the lowest overlap with the other platforms, and Google's two products are closest to each other. Platforms also prefer their own assets: Google's platforms lean towards their own content such as YouTube, and the AI Overviews on Baidu's search page lean towards Baidu's own sub-sites.

The way of observing itself creates differences. The ordinary interface and the API, asking once and asking several times, and different model versions all show different things, so test with the ordinary interface, ask each question several times, and record the date and version.

The Chinese-language ecosystem follows its own rules. Baidu's Chinese AI Overviews are highly concentrated (Gini coefficient 0.895, with the top-ranked website taking 27.1% of citations) and share almost no sources with Google, even though the meaning of the two sides' answers is very close. The language a question is asked in decides which sources AI cites more than where the person is; when questions are asked in the local language, the share of local sources rises several times over. On Chinese-language AI platforms, being listed as a citation does not mean being used: only 8.3% of brands get from the cited sources into the answer, and being mentioned by many sources at once is the most strongly associated signal. The app and web version of the same platform should be looked at separately.

Finally, the evidence for "what each platform specifically likes" is weak and changes quickly, so it can only be used as a hypothesis, with the observation date attached. In practice, write your web pages one way for all platforms, and look at the layout of external sources platform by platform.

## Remember in one sentence

**There is no one thing called "AI search", only a series of different librarians; write your web pages once, but check and fill in what other people say about you one platform at a time.**

## What you can do tomorrow

1. List the AI platforms your audience actually uses. If you have Chinese-speaking users, add the AI Overviews on Baidu's search page and the main Chinese-language AI platforms, and list the app and web version separately.
2. Prepare a fixed prompt set. Include several questions that "describe a problem" (for example, "how can I get clients to pay faster?"), and put questions that ask about the brand directly in a separate group rather than counting them together with the others.
3. Ask the right way: use the ordinary interface, not just the API; log out, open incognito mode, and start a new conversation for each question; ask each question at least 3 times; and confirm that AI actually went online to search this time.
4. Record results for each platform separately, and do not calculate a total score. Record the date and model version every time, and rerun each platform once a week.
5. Read out the source list each platform cites, and sort it by "can you get onto it" into your own website, review platforms, communities, open posting platforms, and competitors' websites. Start filling in from the half to two-thirds that are within your reach, for example by building a profile on industry directories and asking clients to leave reviews.
6. Work out why you are absent: is it "it can't find you", or "it found you but didn't pick you"? Before changing your web pages, test on another platform; if the platform itself cites from a narrow range, changing your web pages will not help.
7. If you are completely absent from Gemini, check your status in Google's index in Google Search Console first. If you care about Gemini and Google's AI Overviews, do not block Google-Extended.
8. Find ways to appear in many different third-party sources, with content that consists of verifiable facts and reporting.
9. Write in the language of the market you are targeting; where needed, build separate pages for each country or market.
10. Update time-sensitive topics regularly. On Chinese-language platforms, the web pages cited for questions like these have a median publication age of only 18 days.
11. If you are targeting Baidu, accept first that Baidu's own sub-sites will take up some of the positions, and build that into your analysis.
12. When setting priorities, first measure how absent you are on each platform and why, then decide where to start according to the platforms your audience actually uses.

## Stop doing this

**Stop using the results of one platform to represent all of them.** A screenshot from one platform cannot tell you how you perform on all platforms, and a successful practice on one platform (especially Google's interfaces) cannot be carried unchanged to another. Likewise, stop combining all platforms into a single "AI visibility score".

Stop drawing conclusions from unreliable measurements. API results are not the answers ordinary users see, the result of a single ask is not the system's fixed output, and "listed as a citation" is even further from "used in the answer".

Stop believing that any "platform preference profile" is a stable rule. Their samples are small, and they change quickly.

Stop treating "optimising for AI search" as a single goal, and stop inferring your visibility in AI only from traditional search rankings.

## What is still uncertain

How much ChatGPT really relies on forum communities: both sides have data and reach opposite conclusions, possibly because of the timing of the observations, the measurement methods or the industries, and you can only find out with your own prompt set. Which platform cites the most per answer: different data sets also rank them in opposite orders, and because the figure depends on the measurement method, it cannot be compared across studies.

Which platform is the most stable: so far the only point of rough agreement is that "ChatGPT varies a lot", and the two sets of data disagree about whether Google is stable. How much platforms really overlap: figures range from 5.4% to 48%, depending on how they are calculated; the only consistent points are that ChatGPT has the lowest overlap with the other platforms and Google's two products are closest to each other, while Perplexity's position is still uncertain.

How quickly new content is reflected is also unsettled. "Perplexity is faster than ChatGPT" is the view of many people in the industry, but there are no controlled tests. On whether to build a separate version for each platform, the more reasonable compromise at present is "one way of writing web pages, with external sources looked at platform by platform", but each camp has observations to support it.

Several claims about platform preferences rest on thin evidence. The "preference profiles" for each platform have small samples and no control group, and one of their claims conflicts with this book's main line, so they can only be treated as hypotheses. "ChatGPT cites less but uses its sources more deeply" comes only from an after-the-fact analysis of one snapshot and can only be called possible in terms of mechanism. Whether blocking Google-Extended causes zero citations in Gemini is unknown; so far we only know the two are associated, not whether one causes the other.

The Chinese-language ecosystem raises more questions still. In Baidu's ecosystem, there is not yet controlled evidence on exactly what to do about Baidu's own sub-sites taking up positions. Test evidence on Chinese-language platforms is also scarce: almost all of it currently comes from research, the most complete study comes from a monitoring service company, and it shows only correlation.

Two bigger question marks remain. Whether older media coverage really has more influence on models than new content is so far only the author's own inference in a single case. And no research has yet shown whether GEO can reliably bring traffic.
