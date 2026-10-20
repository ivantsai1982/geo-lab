# Chapter 15: Word of Mouth on Social Platforms: Can AI Really Hear It?

## Opening: one "I heard that"

Imagine this scenario (what follows is a hypothetical illustration, not a real case). The owner of an online shop that sells scheduling software hears a line at a sharing session: "AI loves citing Reddit most. If you want AI to recommend you, go and post on Reddit." He goes back and assigns a colleague to answer questions on Reddit full time. Three months later he opens ChatGPT and asks, "What scheduling software suits a small studio?" He is still not in the answer. He is puzzled. Doesn't everyone say AI loves Reddit most?

This chapter has only one big idea to teach. **How much social platforms matter in AI's eyes has no single answer. It depends on three things: which AI, which kind of question, and which period of time.** The owner's problem is not necessarily that Reddit is useless. The step he really missed was first checking whether the AI he cares about actually looks at Reddit for the kind of question he cares about.

This chapter answers five questions in turn. First, why do social platforms (Reddit above all) show up in the citations of AI answers, and on which AIs and which types of question are they cited? Second, does the claim "Reddit is the source AI cites most often" hold up, and what happened to the share of Reddit citations in 2026? Third, once community content is cited, how much of it does AI actually use, and what kind of comment gets picked? Fourth, can taking part in community discussions by the rules make a brand appear more often in AI answers, and how strong is the evidence? Finally, what risks come from tampering with community content, for example by faking comments, farming accounts, or stuffing a brand into discussion threads? This chapter treats Reddit as "the platform being studied", and uses LinkedIn as a point of comparison.

## 1. Communities are an especially lively part of "other people's word of mouth"

Let's go back to the book's metaphor. AI is like a very busy librarian with limited time, who flips through only a few books and particularly trusts claims that "lots of people say". The book keeps returning to one point of agreement: whether you can get onto AI's shortlist depends on four things. They are whether AI can read you (accessibility), whether the language and market match, whether there is enough of other people's word of mouth (third-party sources), and whether the content is relevant to the question.

Social platforms belong to other people's word of mouth, but they have three special features. Their content is real users' experiences, comparisons and recommendations, and for questions like "Which one is good?" or "Has anyone used this?" communities happen to hold a great many answers. They are also places where anyone can speak and anyone can edit. That is the reason AI is willing to use them, and it is also exactly the entry point where they are easiest to tamper with. In addition, whether AI can access community content depends on the crawling and licensing relationships between the platform and each AI company, and these relationships change. Because of these three points, "how much do social platforms matter in AI search" has no single answer. It is decided jointly by three things: which AI, which kind of question, and what time.

Seen through the book's seven gates, community content affects several gates along the way. At the gate "can it get in the door", what matters is whether the platform allows a given AI to crawl and use its content, and this changes with policy. At "can it find you", AIs differ enormously in whether they pull community pages onto the shortlist. At the gate "will it pick you", the question becomes which comment in a thread gets picked, and the tendency seen so far is a preference for high-scoring, top-level, formal-toned comments. Next comes "will it mention you", meaning whether you are listed as a source. Further on is "does it really use you": once listed as a source, how much of the content is actually used? Forum-type sources are often listed a lot and used little. Finally there is the seventh gate, "will people come over", meaning whether AI's answers in turn change how lively the community itself is. This point comes up in the section on how AI summaries feed back into communities.

## 2. Each AI flips through what is almost a different bookshelf

Researchers ran repeated tests on real AI search and found that when the same set of questions is given to different systems, the sources they pull back differ greatly. One study used 11,000 questions from a standard question-answering dataset (general knowledge questions), tested several systems at the same time, and looked at the share of all citations that went to social platforms:

| System | Social platforms' share of citations |
|---|---|
| ChatGPT with web search | 0.1% |
| Google's AI summaries (AI Overviews) | 8.5% |
| Google's ordinary search results | 13.4% |

The same study also compared the top 100 websites each system cited most often. ChatGPT with web search overlapped with Google AI Overviews by only 24%, and with Google's ordinary search results by only 25%. Between Google AI Overviews and Google's ordinary search results, the overlap was 68%. In terms of the librarian metaphor, **Google's AI Overviews largely look for books on Google's own shelves, while other AIs have a separate set of shelves.**

A second study used real conversation logs donated voluntarily by 613 users, 171,264 conversations in all, and the researchers then put these questions to each AI again as a comparison test. The result: reddit.com and youtube.com appeared in the search results of ChatGPT and Grok, but did not appear at all in Claude's search results. A third study checked the citations given by ordinary chat models (GPT-4o-mini and GPT-5): of 4,932 citations, only 18 pointed to Reddit, which is 0.4%.

The large records built up by people working in this field point in the same direction: Reddit citations are heavily concentrated in Google's own AI products. Later in this chapter, when we discuss the controversies, we will look at these numbers closely. Keep in mind, though, that these are all "snapshots" taken during the study period. Once platform policies change, the picture may look different.

## 3. Being listed is not the same as being used

The "sources" listed under an AI answer only show that it was mentioned, that is, cited. How much of that content the answer actually used is a separate matter, which is absorption. Researchers checked Google's AI Overviews on real AI search and found that for community and forum-type sources, the degree to which the content "was actually used" was 22.1 percentage points lower than the degree to which it "was listed as a source". Conversely, Wikipedia and longer documents were used more than they were listed. Put plainly, **Google's AI Overviews often hang forums in the sources column, but the content of the answer mainly comes from elsewhere.**

> **A closer look: why can't this number be copied as is?**
> When researchers measure "how much a source was used", they cut the source into many segments and calculate the similarity of "the segment most like the answer". This method partly amplifies the effect of length, because a long document has many segments and is more likely to happen to have one that closely resembles the answer. If you take the average across all segments instead, the extent to which short sources (such as forum comments) are underestimated shrinks greatly. So the direction "forums are used less than they are listed" is credible, but the precise size of 22.1 should not be copied as is.

The opposite case also exists. The real conversation log study mentioned earlier found that 14% to 53% of the statements in AI answers were in fact supported by search results without that source being listed. So some sources were used but not listed, and some were listed but not used. If you judge the influence of community content only by whether Reddit appears in the sources column, you can be wrong in either direction.

## 4. AI "follows the community's upvotes", and it also removes the "I"

Reddit has its own AI search feature too, called Reddit Answers. Researchers observed 30,000 answers it generated from the outside, to see which comments it picked from discussion threads. This kind of study can't see inside the system; it can only compare from the outside how "the picked" differ from "the not picked". They found five things.

The first is that it favours comments that are already prominent. The higher a comment's score ranks within its thread, the more likely it is to be picked. Each time the ranking moves up one step (statistically called "one standard deviation"), the chance of being picked becomes about 2.88 times what it was; the "chance" here is statistical odds, not a direct percentage. Top-level comments, meaning those replying directly to the original post rather than to someone else, had 1.97 times the odds of being picked compared with other comments. If you line up the comments in a thread by score from low to high on a scale of 0 to 1, the median of the picked comments falls at 0.91, close to the highest score; the median of the comments not picked is 0.45, roughly in the middle.

The second is that it favours a formal tone and is less fond of an experience-sharing tone. The more formal the tone, the higher the odds of being picked, with an odds ratio of 1.488; above 1 means more likely to be picked. The more the tone sounds like personal experience, the lower the odds of being picked, with an odds ratio of 0.789; below 1 means less likely to be picked.

The third is that it rewrites personal testimony into general advice. In the original comments, first-person singular words such as "I" made up about 3.3%, but in the AI-synthesised answers only 0.06% remained. The fourth is unexpected: comments pinned or flagged by moderators are almost never picked. The odds ratio for pinned comments was 0.010, and for moderator-flagged comments 0.052. Both numbers are far below 1, meaning the chance of being picked is very low.

The fifth is that when answers change, it is almost entirely because of "which comments were pulled back this time". When the same question was asked again, in 41.8% of cases the sources pulled back were exactly the same; and when the sources were the same, 89.6% of the answers were almost identical. This echoes the dice-rolling idea that runs through the book: the differences mainly happen at the shortlist step, while the answer-writing step is fairly stable.

To be honest, these are all observed correlations, not proof of cause and effect, and they apply only to Reddit's own AI search. But they reveal a mechanism. **At the picking step, AI does not separately assess which comment is of the best quality. It borrows the community's own signal of "who is loudest".** Comments that everyone has pushed to the top are more likely to be picked by AI; a sincere personal experience, even if it is picked, gets rewritten into advice without the "I".

## 5. AI summaries also change communities in return

This section holds the strongest evidence in the chapter, a large-scale experiment with real users. Researchers observed 105,012 Reddit discussion boards (Reddit calls them subreddits). What they did was a kind of "quasi-experiment": they had no way to assign groups randomly, but they found a natural comparison group. Discussion boards with general content could be cited by Google's AI Overviews, while boards with adult content could not. The researchers compared how the two groups changed before and after Google AI Overviews launched.

The result: daily comment counts on general discussion boards rose by 12.0%, and the number of people posting comments rose by 12.4%. Experience-sharing boards saw a bigger effect: compared with factual question-and-answer boards, the effect on comment counts was 2.3 times as large, and the effect on the number of commenters was 2.8 times as large. Small-to-medium boards showed the most obvious relative increase, with comment counts up 55.6% and commenters up 77.2%. "Small-to-medium" here means the second of four equal groups when all discussion boards are sorted by size from small to large, that is, the second-smallest group. So **after Google's AI Overviews launched, community activity on Reddit actually increased, and experience-sharing and small-to-medium communities benefited most.**

But the story has a second half. Google later launched its conversational "AI Mode", and after it launched, the extra advantage experience-sharing boards had gained shrank noticeably. The extra advantage in comment counts fell from 9.54 to -0.17, almost completely gone; the extra advantage in number of commenters fell from 6.29 to 2.57, a drop of 59%.

One plausible reading is that static AI summaries "send" people to look at discussions, while conversational AI "absorbs" the discussion into the conversation, so people no longer need to click through. For approaches that rely on communities to bring in visitors, this is a structural warning: on the same platform, a change in the form of the AI interface alone is enough to cancel out most of the traffic-sending effect. It also needs to be clear what this study measured. It looked only at two Google interfaces and measured only activity at the level of Reddit discussion boards; it did not measure brand exposure, and it did not measure traffic turning into business.

## 6. Pages anyone can write on are the easiest place to strike

Researchers ran tests in a controllable experimental system. This system is an open-source "deep research" AI that issues many searches on its own, reads many web pages, and then writes a research report. Their first finding was that however much it searches, it still ends up concentrated on a few pages. Even when AI splits a question into many smaller questions and searches them separately (query expansion), the results pulled back still converge on a handful of pages. Among them, community pages where anyone can post and edit made up 16.7% to 23.4% of the URLs pulled back; and among these community pages, Reddit made up 53.7% to 70.7%.

The next experiment is more unsettling. The researchers added only about 13 words to one community page that would be pulled back. As a result, the chance of this page being read by AI was 57% to 76%, the chance of it being cited was 34% to 61%, and the chance of the final report mentioning the brand the researchers had specified was 22% to 37%. If this page was not read by AI, the chance of the specified brand being mentioned was 0.

Once it was read, the effect was strong. In one of the AI systems, as long as this page was read, the citation rate was 100%. Another system picks passages using "semantic similarity" (technically, embedding vectors), and it resisted this attack best, but as long as it read this page, the chance of mentioning the specified brand was still 37.8%. Adding very few words also worked: even when the added text made up only 0.5% to 3.9% of the whole page, as long as the page was read, the chance of mentioning the specified brand was still 29.7% to 52.5%.

Existing defences did not work well. One method checks "how unnatural the text reads" (technically called perplexity) to try to pick out the added text, but its ability to tell them apart was weak. On a score where 0.5 means random guessing and 1 means perfect, it came in below 0.68, and its judgement pointed in the opposite direction from what was expected. Another method filters by comparing the similarity of output content, and it was ineffective. Not reading community pages at all can block this attack, at the cost of losing the genuinely valuable knowledge in communities.

The researchers also looked at commercial AI, but only observed citations and did no attack testing. In Gemini's deep research feature, 623 of 5,157 citations (12.1%) came from community pages anyone can write on; in ChatGPT's deep research feature it was only 0.4%.

This is evidence that only proves a mechanism. It proves that in a reproducible system, this kind of attack can be done and is hard to catch, but you can't directly infer the same success rate on commercial AI. Its real significance is this: **the very thing that makes community content attractive to people who want AI to see them is the reason it is so easy to abuse.**

## 7. How strong is the evidence?

Put the conclusions above side by side, and the strength of the evidence and the scope it applies to vary a great deal. The strongest is that Google AI Overviews increased activity on general Reddit discussion boards by about 12%, while the conversational AI Mode weakened the advantage of experience-sharing boards. This comes from a large-scale quasi-experiment with real users, and its strength is strong, but it covers only two Google interfaces and measures only activity at the level of Reddit discussion boards. It does not measure brand, and it does not measure traffic turning into business.

Several findings are of medium strength. Systems differ greatly in the share of citations going to communities (0.1%, 8.5%, 13.4%); this is a one-off snapshot taken on real AI search, using general knowledge questions rather than commercial ones. That forums are listed a lot but used little in Google AI Overviews comes from checks on real AI search; the direction is credible, but the size is affected by the calculation method. That Reddit's own AI search favours high-scoring, top-level, formal comments and removes the first person comes from observing a real platform from the outside; it applies only to Reddit's own AI search, and it is correlation, not causation. That Claude's search results contain no Reddit and that ordinary chat models cite Reddit only 0.4% of the time come from real conversation logs and checks on real AI; these are snapshots from the study period, and platform policies change.

One more finding is also of medium strength: posting ordinary articles on low-barrier platforms that AI already favours can get into the citations and answers of most commercial AI search. Researchers posted under controlled conditions on 10 real AI search platforms and tracked them over several days to get this result, but it is limited to fictional or obscure topics. On topics that already have a lot of discussion, only 3.5% got written into answers, and citations were not stable.

Two other findings need to be looked at separately. That adding about 13 words to a community page can sway a deep research report comes from a controllable experimental system; it only proves a mechanism, and the actual success rate on commercial AI is unknown. That brand participation on Reddit makes a brand appear more often in AI answers is currently supported only by before-and-after comparisons done by people in the industry themselves; the strength is weak, there are no randomised comparisons, and most authors themselves admit they cannot prove causation.

This brings out the biggest gap at present. **To date, no study has used random assignment or a quasi-experiment to prove that "brands taking part on social platforms" raises AI visibility, traffic or business.** Academic research cares about how AI handles community content; how brands make use of communities lies outside the questions it asks. That said, the layer "can posts get into AI citations" already has evidence from the controlled test mentioned above. What is still missing is whether real brands in highly competitive categories get recommended as a result, and gain traffic and business.

## 8. Controversies: what people say often contradicts itself

### Controversy 1: Is Reddit really the source AI cites most often?

Many people in the industry believe Reddit is still the source AI cites most. But "many people believe" does not mean "it is right". This view is itself disputed, and some people in the field openly disagree. The numbers the various sides put forward fall roughly into four positions.

The first position holds that Reddit's share of citations is very low. Someone in the industry tested this themselves (no one has independently verified it): from March to June 2026, they tested 5 AIs with about 16,400 commercial questions and collected 127,198 citations in total. Reddit made up only 1.8%, Wikipedia less than 0.6%, and roughly 90% of citations went to vendors' documentation, product pages, and all kinds of niche directory sites. The questions here carried purchase intent, and the unit counted was the website, not individual URLs.

The second position holds that Reddit citations appear almost only on Google's products. Another person in the industry tested this themselves: out of about 74,000 citations, those pointing to Reddit came from Google's AI Mode 528, Gemini 258, ChatGPT 23, Claude 1, and Perplexity 0, while Perplexity cited 17,476 sources in total during this period. Google's two products together made up about 97%. However, the brands this author tracked lean towards niche markets and business-to-business (B2B) markets, and he himself says the results should not be treated as a law.

The third position holds that Reddit is one of the main sources for all the major AIs, and that Perplexity is the most active. Someone in the industry tracked a client of a website plugin for 8 weeks and found that among the top 8 cited sources, 2 were Reddit threads from 2022 and 2023. This is only a single client in a single niche market. The fourth is the academic result mentioned earlier: only 0.4% of ordinary chat models' citations point to Reddit, and Claude's search results contain no Reddit at all. This too is a snapshot from the study period.

These contradictions don't necessarily cancel each other out, because they measure different things. The question types differ: some are commercial questions, some general knowledge questions, some review-and-opinion questions. The combinations of AIs tested differ, the points in time differ, and the counting methods differ too: some count websites, some count URLs, some count "how many answers mention it". Among them, "Perplexity cites Reddit most actively" and "Perplexity cites Reddit 0 times" directly conflict, and the two are only about two months apart. **This in itself shows that AI behaviour changes very fast, and no single snapshot can be used to infer what happens at other times.**

There are also two single observations. One person in the industry saw that in the answers to his 100 "questions asked just before placing an order", Reddit's citation rate was below 5%. Another person in the industry saw Reddit regularly make it into the top three cited sources in the reports he produced. Both are only single observations.

### Controversy 2: Is ChatGPT's "collapse" in Reddit citations real?

In August 2026 a widely repeated claim appeared: the share of ChatGPT search citations going to Reddit plunged by about 86% within a few days, from about 3.8% to about 0.5%. The industry generally accepts this claim, but both its scope and its cause are disputed.

The evidence that it "really is low" comes from a test done by one person in the industry. He used the developer interface behind ChatGPT (the API, with web search turned on) and ran 1,564 questions written in real conversational language. He had planned to test 10 categories of questions and completed only 7. Reddit was cited 38 times in all, 2.4%, and 92% of those came from "reviews and opinions" questions; every other category was very low. The author also admits that the developer interface is not exactly the same as the app ordinary people use.

Some observations also suggest this drop may have affected only ChatGPT. One person in the industry saw that over the same period, the share of Perplexity's citations going to Reddit on the websites he monitors showed no obvious change, and Google's AI Overviews were still citing Reddit heavily. Another person in the industry saw the same direction, but on a smaller scale. He tracks 46 business-to-business (B2B) questions every week, and Reddit's appearances fell from 9 in July to 3 at the last check in August, with mid-sized vendors' blogs and comparison pages taking its place. He also warns that a 4-day observation window is too short, and that fluctuations of a similar size have reversed within two weeks before.

As for the cause, two explanations are circulating. Over the same period, tracking data indicated that the share of ChatGPT searches using the "site:" command (which limits a search to one website) rose sharply, which looks like a change in how it looks for information. There were also reports that Reddit tightened its blocking of AI crawlers in mid-August. Neither explanation has been confirmed as the cause.

One more point is easy to overlook: citations disappearing does not mean influence disappearing. Someone in the industry pointed out that a change in "which sources get listed" does not mean AI's behaviour has changed. If ChatGPT still follows the consensus on Reddit when recommending brands, what changed may only be whether the source is listed. This matches the "used but not listed" case mentioned earlier in the section on being listed not being the same as being used. But there is currently no direct evidence that ChatGPT is still using Reddit content.

### Controversy 3: Did Perplexity "withdraw" from Reddit, or does it "pick sources by question"?

Someone in the industry tested this themselves repeatedly, with a control group. On a set of 4 fixed questions, from 20 August onwards, Perplexity did not cite Reddit in 96 consecutive checks. But on 26 August he added some questions containing brand names and some specific task-type questions, and within a single day Reddit citations reappeared: 9 times in 6 days, all from these new questions. Over the same period, the average number of sources Perplexity listed per answer fell from about 9 to about 6; however, the mix of questions changed during this period, so this number can only be taken as a hint.

On this basis the author judged that this was a contraction by question type, not a full withdrawal: broad popular category terms no longer cite Reddit, while questions with brand names and specific tasks accept Reddit again. This is only a small sample, with just a few more than 4 questions, in a single niche market. But it reminds us that when we hear "a certain AI no longer cites Reddit", we should first ask: on which questions?

In addition, one company claimed that Perplexity went from almost never citing Reddit to citing Reddit in most answers within two weeks. But this claim comes from a party with a commercial interest, and no one has independently verified it.

### Controversies 4 and 5: new versus old, and how much "consensus" really matters

The fourth controversy is whether new threads have the edge or old ones are cited just as much, and observations from different sides contradict each other. One person in the industry observed that a thread from 3 weeks earlier with 40 upvotes was cited first by Perplexity, while a 2-year-old blog post with more external links and almost identical content was ranked behind it. Another person in the industry claimed that 60% of citations come from threads less than six months old, but his claim was exaggerated in tone and the source of the data is unclear. Yet another person in the industry observed that when the same question was run many times, Reddit threads were stable as cited sources up to 96% of the time, and cited threads could be traced back as far as 7 years; the 8-week tracking mentioned earlier also found that threads from 2022 and 2023 were still cited. One more company claimed that 60% to 70% of the Reddit threads cited by AI were already archived and could no longer be commented on, but this claim comes from a party with a commercial interest, and no one has independently verified it. These are all single observations, and they don't agree with each other. All we can say at present is that both freshness and accumulated history may play a part, depending on which AI and which kind of question.

The fifth controversy is whether a community's "consensus view" really matters more than a single web page. Many people in the industry believe AI relies more on views that have been discussed over and over by many people in a community until they become consistent than on a single optimised web page. The industry also generally believes that keeping core messages consistent across the whole web is where Generative Engine Optimization (GEO) gets its results. But these are opinions, not proof.

Set against this view are two pieces of research evidence. In Reddit's own AI search, AI picks single high-scoring, top-level, formal comments, and rewrites personal experience away; we already saw this in the section on AI "following the community's upvotes". In Google's AI Overviews, forums are often listed as sources but rarely actually used. Neither point supports the simple picture that "a whole community's discussion is fully absorbed by AI".

## 9. What people who actually did it saw

The cases below all come from tests and observations by people working in this field. Unless otherwise stated, none of them has a control group, and none can prove that the results were caused by community participation.

### Two before-and-after comparisons: 8 weeks and 90 days

The first case is a direct approach. This person in the industry first recorded 100 questions that buyers ask on ChatGPT, Perplexity, Gemini and Google's AI products as a starting point, and then spent 8 consecutive weeks posting useful content and replies on Reddit. The numbers before and after the 8 weeks were as follows:

| Metric | At the start | After 8 weeks |
|---|---|---|
| Number of questions where the brand appeared | 4 | 17 |
| Number of times cited | 1 | 7 |
| Visits from Reddit | 6 | 94 |
| Sign-ups | 0 | 8 |

The key detail is that most of the growth came from specific questions, and broad terms like "what is the best tool" contributed very little. This person in the industry tested it themselves, no one has independently verified it, and the author himself states that this does not prove Reddit caused the growth. It is consistent with the earlier observation that Perplexity contracts "by question type": community content is more likely to be cited on specific, obscure, task-type questions.

The second case took the route of lurking first and taking part later, stretched out over 90 days. The author split the approach into four steps:

1. Lurk for 4 weeks first. Understand each discussion board's rules, and study which comments get upvoted and which get deleted. In the first month, do not mention the brand at all; just build up an account reputation score of about 200 to 500.
2. See which threads AI actually cites. Ask ChatGPT and Perplexity the target questions, note which Reddit threads they cite, and give priority to recommendation, comparison and experience threads.
3. Adjust the writing. Answer the question directly in the first two sentences, replace vague wording with specific numbers, and write about both the pros and the cons.
4. Track every week. Every Monday, use the same questions to check on ChatGPT, Perplexity and Google's AI Overviews whether the brand was mentioned, whether the tone was positive or negative, and which sources were cited.

Within 90 days, the brand's appearance rate in category-type AI answers rose from 8% to 39%. Visits from Reddit rose from about 22 a month to about 480 a month, with 37 new sign-ups a month attributable to Reddit. Content published in the first quarter was still being cited 5 months later. The author also observed that small communities with only 10 to 20 threads a day often worked better than large discussion boards.

This case was tested repeatedly by someone in the industry themselves, with a comparison, but all the numbers are self-reported. The author's premise is that "on many commercial questions, Reddit appears more often than brands' official websites and Wikipedia", which conflicts with the large-sample data in Controversy 1, so it should be treated with caution. Its writing approach (answering directly in the first two sentences, a formal tone, specific content) is consistent with the finding that Reddit's own AI search favours formal, explanation-like comments. "Small communities work better" also points in the same direction as the finding that small-to-medium discussion boards were most affected by Google AI Overviews, but the two measure different things and can't be used as proof of each other.

The third case is one that did not succeed. Someone in the industry wrote 20 pieces of content on Reddit for a start-up, and ChatGPT still did not cite the company. Set against Controversy 2, this is not surprising, because in the period the research covers, the share of ChatGPT's citations going to Reddit was already very low. The lesson: first confirm whether your target AI cites social platforms for your type of question, then decide whether to invest.

### LinkedIn: another social platform, with almost the opposite rules

LinkedIn is often put alongside Reddit as a "community source". But data from people in the industry show that the rules by which AI cites LinkedIn content are almost the opposite of the rules by which its feed recommends posts.

The first data set was tested by someone in the industry themselves, and no one has independently verified it. He analysed 1,310,455 LinkedIn URLs cited by ChatGPT, Perplexity, Google's AI Overviews, Google's AI Mode, Copilot and Gemini from January to June 2026. Likes and comments were almost unrelated to whether a post got cited: their correlations with citation counts were -0.06 and -0.04 respectively. This number lies between -1 and 1, and close to 0 means almost no relationship. Long articles were cited more often than short feed posts: LinkedIn's long articles made up 63% of cited URLs but received 72% of citations, with an average of 8.5 citations per long-article URL against 5.9 for short feed posts. On Copilot, 90% of LinkedIn citations were long articles.

In the same data set, content posted under a personal name was cited more often than content posted under a company name. Content posted by individuals made up 88% of cited URLs and 92% of citations, while company pages averaged 5.5 citations per URL. Plain text came out slightly ahead, averaging 6.48 citations per URL, against 5.91 for posts with images and 5.69 for posts with video. Citations were also very unevenly distributed: half of the cited URLs were cited exactly 2 times, the top URL was cited 4,685 times, and follower count made little difference. AIs differed a lot from one another: Perplexity alone accounted for 43% of LinkedIn citations, while Gemini cited LinkedIn only 38 times in five months.

The second data set was tested repeatedly by someone in the industry themselves, with a comparison. He used 350 questions without brand names and ran each 3 times over 4 days on ChatGPT, Perplexity and Google's AI Overviews, getting 4,581 answers and 39,236 retrieved items in all. Of the 22 LinkedIn URLs that were cited, 20 were long articles and none was a short feed post; of the 64 records in which LinkedIn was retrieved, 58 pointed to long articles. Of these 22 URLs, 19 were LinkedIn's localised Italian-language URLs.

However, LinkedIn made up only 0.16% of all the retrieved items in this set, and YouTube 1.13%. Ranked ahead of LinkedIn were the official websites of several large technology companies, and the official websites of EU and US standards bodies. In this data set, Google's AI Overviews cited LinkedIn more often than Perplexity did (6.1% against 3.4%), the exact opposite of the first data set's result. YouTube appeared 331 times in this data set, 314 of them from Google's AI Overviews. Many people in the industry also believe that posting on a LinkedIn company brand page does little for AI visibility.

LinkedIn shows that "popularity" signals on social platforms are not necessarily inherited by AI. Reddit's own AI search follows scores, but when outside AIs cite LinkedIn, the number of likes is almost irrelevant; what matters is the form of the content: long articles, plain text, and a personal name. **The rules of each platform and each AI have to be looked at separately.**

The last case concerns the relative weight of the various social platforms. In a small sample, one person in the industry saw 86 citations from social platforms: YouTube 38, Reddit 30, LinkedIn 9, software review sites 6, and Wikipedia, Quora and Facebook 1 each. Another person in the industry observed that with the same 40 questions and 7 AIs, Gemini cited Reddit on 22 of the questions, while ChatGPT did so on at most 1. These are all single observations. They can only remind us not to treat "social platforms" as a single whole, and not to average the numbers of the various AIs together.

## 10. Taking part properly versus tampering: what's the difference?

Taking part by the rules has roughly four features. They fit community rules, and they are compatible with the mechanisms described in this chapter. You answer real questions under your real identity, and you disclose your relationship with the brand. You share specific, verifiable experiences and numbers, and write about both the pros and the cons. You follow each discussion board's rules and accept moderation. You add new information to threads that AI already cites and that are still open for comments, without repeating promotion. Someone in the industry observed that in business-to-business (B2B) fields, only "personal accounts that disclose their identity" can be sustained over the long term. Accounts carrying a brand logo, even with helpful content, are easily rejected by niche communities, because once a community decides you are "here to grab something for yourself", it will downvote and report you.

Manipulation is a different matter, and this book does not recommend it. The most common form is using large numbers of farmed old accounts and high-reputation accounts to post brand recommendations in bulk. Someone in the industry observed that there really are people on the market offering this service: holding thousands of old accounts, charging monthly, posting threads and comments on clients' behalf, and even offering a service to "get rid of negative threads". Someone else in the industry admitted themselves that this is not allowed on the platform and is a rule-breaking practice. Other tactics include manufacturing brand mentions that "look natural"; stuffing short phrases into threads so that a specific brand comes along when AI pulls them back, which is exactly the method the researchers used earlier to prove the attack was feasible; and asking and answering your own questions and upvoting each other to push comment scores up.

Manipulation has several layers of cost. The most direct is banned accounts and deleted content. Someone in the industry observed that even without selling anything, just offering professional opinions, joining discussions often gets blocked, appeals go unanswered, and community rules are becoming more and more conservative. Next, the citation source may be cut off. The crawling and licensing relationships between platforms and AI companies change. Around mid-August, the shares of ChatGPT's and Perplexity's citations going to Reddit both fell sharply (see Controversies 2 and 3), and a strategy built on a single platform can stop working within a few days.

Then there is the problem of being picked and being understood. In Reddit's own AI search, comments pinned or flagged by moderators are almost never picked. Even when picked, first-person experience is rewritten into general advice and loses its original meaning; forum content is cited in Google AI Overviews but rarely actually used.

Some risks are inferences or concerns. Researchers have already pointed out that "not reading community pages" is an effective line of defence. If AI companies adjust in this direction, approaches that rely on manipulating community content will be hit first; this is an inference, and there is currently no evidence that it has happened. Once a community sees through manipulation, the negative discussion itself may also become a source AI cites and damage the brand's reputation; this is a concern in the industry, and there is currently no systematic evidence. Finally, deleting a post does not mean it stops being cited. Researchers found on real AI search that after an article was deleted, some platforms kept citing it for about 4 days. **If you post the wrong content, you can't count on deleting it to take it back right away.**

## 11. What to do, what not to do, and outdated approaches

### What you can do, and how strong the evidence is

The first thing is to measure first, then invest. For your core questions, record on each AI, one by one, which websites it cites, and confirm whether social platforms are among them. Don't rely on sweeping claims like "AI loves citing Reddit most". The basis for this is that researchers ran repeated tests on real AI search and found that the sources of different AIs differ enormously.

Next, plan separately for each AI. Unless your data show that other AIs respond too, treat community work as an approach that "mainly affects Google's AI products". The basis is checks on real AI search, plus tests by people in the industry themselves. In the same way, plan separately by question type. Community content is more likely to be cited on review-and-opinion, specific task-type, and brand-name questions, and less on broad category terms. This comes from observations that people in the industry tested repeatedly themselves with a comparison, plus tests by people in the industry themselves.

As for concrete action, you can take part in threads that are already cited and still open for comments, starting from the list of threads AI actually cites and judging whether you have anything specific to add. This comes from tests by people in the industry themselves; some people in the industry have also observed that some of the cited threads have already been removed or archived. When you write, write formally, specifically, and in a form that can be used directly: answer the question in the first two sentences, give specific numbers, and write about both the pros and the cons. The basis for this is outside observation of a real platform (only for Reddit's own AI search, and it is correlation, not causation), plus tests by people in the industry themselves. Note that writing this way is aimed at being picked by AI. A simulation study showed that what AI regards as a "popular answer", meaning one with more arguments, evidence and steps, is almost unrelated to the votes of real people; winning real people's votes in a Q&A community is a different goal.

Taking part under your real identity and disclosing your relationship with the brand is based on observations by people in the industry, and from the standpoint of playing by the rules, it is essential. On LinkedIn, give priority to long articles under a personal name and post fewer short updates from the brand page. The basis is tests by people in the industry themselves, plus data that people in the industry tested repeatedly with a comparison.

The way you measure also needs to change. Measure "being cited" separately from "bringing in visitors and potential customers", because people in the industry have observed that the two often don't move together, and research has also found that "being cited" and "being used" don't match. Finally, track continuously for several weeks and look at each AI separately rather than looking at a single result, because in tests by people in the industry, large short-term swings that later reversed happened again and again.

### What not to do, and ideas that are out of date

There are several things not to do. Don't farm accounts, buy comments, or post brand recommendations in bulk, and don't stuff threads with short brand phrases meant for AI to see. Don't promote in communities using only a brand account. When judging a community's influence, don't look only at "whether Reddit is in the sources column", because being cited is not the same as being used, and being used does not necessarily mean being cited; and don't average all the AIs' numbers into a single "AI visibility". On budget, don't bet everything on a single social platform, because a platform's crawling policy can change within a few days.

Three ideas are already out of date. The first is "Reddit is the source AI cites most often, so go all in on Reddit". At least for commercial questions in 2026, on ChatGPT and Claude, and on Perplexity during certain periods, this premise does not hold. The second is "posting on Reddit can influence every AI"; in reality, the sources of the various AIs are almost different worlds. The third is "chasing community popularity is the same as chasing AI visibility", but on LinkedIn, the number of likes is almost unrelated to whether AI cites a post.

## Key points of this chapter

The weight of social platforms in AI search depends on which AI, which kind of question, and what time. Google's AI Overviews and AI Mode use community sources heavily; other AIs rarely cited Reddit during the study periods, and Claude's search results contained no Reddit at all. "Reddit is the source AI cites most often" is a disputed claim; on commercial questions, large-sample data show that Reddit makes up only a very small share, and most citations go to vendors' documentation and product pages. Around August 2026, the shares of ChatGPT's and Perplexity's citations going to Reddit both fell sharply, but the scope, the cause, and whether it will last are all disputed, and Perplexity's change looks like a contraction by question type.

Being cited is not the same as being used. Forum-type sources are cited a lot but used little in Google AI Overviews; conversely, a great deal of content is used without being listed. At the picking step, AI inherits the community's signal of prominence, favouring high-scoring, top-level, formal comments, and rewriting first-person experience into general advice. A large-scale experiment with real users showed that Google's AI Overviews boosted community activity on Reddit, with experience-sharing and small-to-medium communities benefiting most, but the conversational AI Mode weakened this effect.

"Brand participation in communities raises AI visibility" is currently supported only by before-and-after comparisons from people in the industry, with no causal evidence, and the cases that worked are all concentrated on specific, obscure questions. Community pages anyone can write on are a single-point attack surface. Manipulation is mechanically possible and hard to detect, but it carries the risks of banned accounts, deleted posts, sources being cut off, and damaged reputation. Taking part by the rules, meaning real identity, a disclosed relationship and specific contributions, is the only approach that can last.

## Closing: back to that owner

Where the owner in the opening went wrong was not in going to Reddit, but in treating one "I heard that" as a map. Communities are a very important part of other people's word of mouth, but each librarian flips through different shelves, each kind of question calls for different books, and the shelves can be moved at any time. So measure first, then invest; look at each separately rather than averaging; and speak well under your real identity rather than tampering.

## Remember in one sentence

**How much community word of mouth matters in AI's eyes depends on which AI, which kind of question, and what time; measure clearly first, then take part properly under your real identity.**

## What you can do tomorrow

1. Measure first. List the core questions you care about most, ask each AI you care about one by one, note which websites they cite, and confirm whether social platforms are actually among them. Don't rely on claims like "AI loves Reddit most".
2. Plan separately for each AI. Unless your own data show that other AIs respond too, start by treating community work as an approach that "mainly affects Google's AI products".
3. Plan separately by question type. Give priority to review-and-opinion, specific task-type, and brand-name questions, and spend less effort on broad category terms.
4. Start from threads that AI already cites and that are still open for comments, think about whether you have specific new content to add, and keep in mind that some cited threads have already been removed or archived.
5. Write formally, specifically, and in a form that can be used directly: answer the question directly in the first two sentences, give specific numbers, and write about both the pros and the cons.
6. Take part under your real identity and disclose your relationship with the brand; in business-to-business fields, use a personal account that discloses your identity rather than relying only on a brand account.
7. On LinkedIn, give priority to long articles under a personal name and post fewer short updates from the brand page.
8. Record "being cited" separately from "bringing in visitors and potential customers".
9. Track continuously for several weeks and look at each AI separately. Don't be scared by a single result, and don't draw conclusions from one good result either.

## Stop doing this

**Stop believing "Reddit is the source AI cites most often, so go all in on Reddit".** At least for commercial questions in 2026, on ChatGPT and Claude, and on Perplexity during certain periods, this premise does not hold. Likewise, stop assuming that posting on Reddit can influence every AI, since the sources of the various AIs are almost different worlds; and stop treating community popularity as AI visibility, since on LinkedIn the number of likes is almost unrelated to whether AI cites a post.

Stop farming accounts, buying comments and posting brand recommendations in bulk, and stop stuffing threads with short brand phrases meant for AI to see. Promoting in communities using only a brand account is something to stop as well.

When measuring and allocating resources, stop looking only at whether Reddit is in the sources column, and stop averaging all the AIs' numbers into a single score. Finally, stop betting your whole budget on a single social platform.

## What is still uncertain

**Does brand participation in communities actually raise AI visibility, traffic or business?** No study using random assignment or a quasi-experiment has proven it so far. There are only before-and-after comparisons by people in the industry, and most authors themselves admit they cannot prove causation.

**Is Reddit really the source AI cites most often?** The numbers from different sides conflict, and the question types, AI combinations, timing and counting methods all differ. No single snapshot can be used to infer what happens at other times.

**How should ChatGPT's plunge in Reddit citations in August 2026 be read?** Whether the scope was ChatGPT alone or other AIs too, whether the cause was a change in how it looks for information or Reddit tightening its blocking, and whether it will last are all still unsettled. There is also no direct evidence on whether ChatGPT is still "using without listing" Reddit content.

**Has Perplexity withdrawn from Reddit entirely, or contracted only on certain questions?** For now there are only small-sample observations. The claim that it "went from almost never citing to citing in most answers within two weeks" comes from a party with a commercial interest and has not been independently verified.

**Do new threads have the edge, or do old ones do just as well?** The observations contradict each other, and claims like "60% are less than six months old" and "60% to 70% are archived" have unclear sources or have not been verified.

**Does a community's "consensus view" matter more than a single web page?** This is an industry opinion, and existing research does not support the simple picture that "a whole community's discussion is fully absorbed".

**When forums are "used little" in Google AI Overviews, how little is that exactly?** The precise size is affected by the calculation method; only the direction is credible.

**What is the actual success rate of tampering with community pages on commercial AI?** This is not yet known. Whether AI companies will start blocking community pages is also only an inference.

**Could negative discussions become a source AI cites and end up hurting the brand?** For now this is only a concern in the industry, with no systematic evidence.

**Which AI cites LinkedIn most often?** The two data sets give exactly opposite results.
