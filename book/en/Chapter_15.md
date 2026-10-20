# Chapter 15 — Word of Mouth on Social Platforms: Can AI Really Hear It?

## Opening: one "I heard that…"

Imagine this scene (what follows is a hypothetical illustration, not a real case).

The owner of an online store that sells scheduling software hears someone say at a sharing session: "AI loves citing Reddit most of all. If you want AI to recommend you, go and post on Reddit."

As soon as he gets back, he assigns a colleague to answer questions on Reddit full time. Three months later, he opens ChatGPT and asks: "What scheduling software is good for small studios?" He is still not in the answer.

He is confused: didn't they say AI loves Reddit most?

There is only one big lesson in this chapter:

**How important social platforms are in the eyes of AI has no single answer. It depends on three things: which AI, which kind of question, and which period of time.**

This owner's problem is not necessarily that Reddit is useless. His problem is this: he never checked first whether the AI he cares about actually looks at Reddit for the kind of questions he cares about.

This chapter answers five questions in order:

1. Why do social platforms (especially Reddit) appear among the citations in AI answers? On which AIs, and for which types of question, are they cited?
2. Does the claim "Reddit is the source AI cites most often" hold up? In 2026, what happened to the share of citations going to Reddit?
3. Once community content is cited, how much of it does AI actually use? What kind of comment gets picked?
4. Can taking part in community discussions by the rules make a brand appear more often in AI answers? How strong is the evidence?
5. What are the risks of tampering with community content (fake comments, farmed accounts, stuffing brands into threads)?

This chapter treats Reddit as "the platform being studied", and uses LinkedIn as a point of comparison.

---

## 1. Communities are an especially lively part of "other people's word of mouth"

First, back to the book's metaphor: AI is like a very busy librarian. It has limited time, only flips through a few books, and especially trusts claims that "lots of people say".

The book keeps returning to one consensus: whether you get onto AI's **shortlist** depends on four things — whether AI can read you (accessibility), whether the language and market match, whether there is enough **word of mouth from others** (third-party sources), and whether the content is relevant to the question.

Social platforms belong to "other people's word of mouth". They have three special features:

- **The content is real users' experiences, comparisons and recommendations.** For questions like "Which one is good?" or "Has anyone used this?", communities happen to hold a huge number of answers.
- **Anyone can post, and anyone can edit.** This is why AI is willing to use them, and it is also exactly the entry point most easily tampered with.
- **Whether AI can access them depends on the crawling and licensing relationships between the platform and each AI company.** These relationships change.

So "how important are social platforms in AI search" has no single answer. It is decided by three things together: "**which AI × which kind of question × what time**".

Seen through the book's seven gates, community content affects several gates along the way:

```
Community content
  │
  ├─ Can it get in the door (accessibility): does the platform allow this AI to crawl and access it? (changes with policy)
  │
  ├─ Can you be found (retrieval): does this AI pull community pages into its shortlist? (differs hugely between AIs)
  │
  ├─ Are you picked (selection and ranking): which comment in the thread gets picked? (leans towards high-scoring, top-level, formal tone)
  │
  ├─ Are you mentioned (citation): is it listed as a source?
  │
  └─ Are you really used (absorption): once listed as a source, how much of the content is actually used? (forums are often "listed a lot, used little")
```

Finally there is the seventh gate, "will people come over" (user behavior): whether AI answers in turn change how lively the communities themselves are. Section 5 of this chapter covers this.

---

## 2. Each AI flips through what is almost a different bookshelf

Researchers ran repeated tests on real AI search and found: give the same set of questions to different systems, and the sources they pull back differ enormously.

One study took 11,000 questions from a standard question-answering dataset (general-knowledge questions) and tested several systems at once, looking at what share of all citations went to social platforms:

| System | Share of citations going to social platforms |
|---|---|
| ChatGPT with web search | 0.1% |
| Google's AI summary (AI Overviews) | 8.5% |
| Google's ordinary search results | 13.4% |

The same study also compared the top 100 websites each system cited most often:

- ChatGPT with web search overlapped only 24% with Google AI Overviews, and only 25% with Google's ordinary search results.
- Google AI Overviews and Google's ordinary search results overlapped 68%.

In terms of the librarian metaphor: **Google's AI Overviews mostly look for books on Google's own bookshelf; other AIs have a bookshelf of their own.**

A second study used real conversation logs voluntarily donated by 613 users, 171,264 conversations in total, and the researchers then put the questions to each AI again for comparison testing. They found: reddit.com and youtube.com appeared in ChatGPT's and Grok's search results, but did not appear at all in Claude's search results.

A third study examined the citations given by ordinary chat models (GPT-4o-mini and GPT-5): of 4,932 citations, only 18 pointed to Reddit, which is 0.4%.

The large body of records accumulated by people working in this field also points in the same direction: **Reddit citations are highly concentrated in Google's own AI products** (section 8 looks at these numbers closely).

Remember, these are all "snapshots" taken during the study periods. Once platform policy changes, the picture may look different.

---

## 3. Being listed is not the same as being used

The "sources" listed under an AI answer only show that it was **mentioned** (citation). How much of that content the answer actually used is another matter (absorption).

Researchers examined Google's AI Overviews on real AI search and found: for community and forum sources, the degree to which the content "was actually used" was 22.1 percentage points lower than the degree to which it "was listed as a source". The other way round, Wikipedia and longer documents were used more than they were listed.

In plain words: **Google's AI Overviews often hang forums in the source list, but the content of the answer mainly comes from elsewhere.**

> **A closer look: why can't this number be copied as is?**
> When researchers measured "how much a source was used", they cut the source into many segments and took the similarity of "the segment most like the answer". This method partly amplifies the effect of length: long documents have many segments, so they are more likely to happen to have one segment that closely resembles the answer. If you instead take the average across all segments, the degree to which short sources (such as forum comments) are underestimated shrinks a lot.
> So the **direction**, "forums are used less than they are listed", is credible, but the **precise size** of 22.1 should not be copied as is.

The opposite situation also exists. The real-conversation-log study mentioned earlier found: 14% to 53% of the statements in AI answers were in fact supported by search results, yet the source was not listed.

So the conclusion is: **some sources are used but not listed, and some are listed but not used.** If you judge the influence of community content only by whether Reddit is in the source list, you can be wrong in both directions.

---

## 4. AI "follows the community's upvotes", and it also removes the "I"

Reddit has its own AI search feature too (Reddit Answers). Researchers observed 30,000 answers it generated from the outside, looking at which comments it picked from threads. This kind of study cannot see inside the system; it can only compare from the outside how "the picked" differ from "the not picked". It found five things.

**First, it favours comments that were already prominent.**

- The higher a comment's score ranks within its thread, the more likely it is to be picked. Each time the ranking moves up one step (statistically called "one standard deviation"), the chance of being picked becomes about 2.88 times what it was (the "chance" here is statistical odds, not a direct percentage).
- Top-level comments (replying directly to the original post, not to someone else's comment) had 1.97 times the odds of being picked compared with other comments.
- Arrange the comments in a thread by score from lowest to highest, on a scale from 0 to 1: picked comments had a median of 0.91, close to the top score; comments not picked had a median of 0.45, roughly in the middle.

**Second, it favours a formal tone, and is less keen on a tone of sharing experience.**

- The more formal the tone, the higher the odds of being picked (odds ratio 1.488; above 1 means more likely to be picked).
- The more the tone sounds like personal experience, the lower the odds of being picked (odds ratio 0.789; below 1 means less likely to be picked).

**Third, it rewrites personal testimony as general advice.** In the original comments, first-person singular words such as "I" made up about 3.3%; in the answers AI synthesised, only 0.06% remained.

**Fourth, comments pinned or flagged by moderators are almost never picked.** The odds ratio for pinned comments was 0.010, and for moderator-flagged comments 0.052. Both numbers are far below 1, meaning the chance of being picked is very low.

**Fifth, answers change almost entirely because of "which comments were pulled back this time".** When the same question was asked again, in 41.8% of cases exactly the same sources were pulled back; and when the sources were the same, 89.6% of the answers were almost identical. This echoes the **dice-rolling** idea from throughout the book: the differences mainly happen at the shortlist step, not at the answer-writing step.

To be honest: these are all observed **correlations**, not proven **causation**, and they apply only to Reddit's own AI search.

But they reveal a mechanism: **AI's selection step does not separately judge which comment is of the best quality; instead it reuses the community's own signal of "who is loudest".** Comments pushed to the top by everyone are more likely to be picked by AI; a sincere personal experience, even if picked, gets rewritten into a piece of advice with no "I".

---

## 5. AI summaries also change communities in return

This section has the strongest evidence in the chapter: **a large-scale experiment with real users.**

Researchers observed 105,012 Reddit discussion boards (Reddit calls them subreddits). What they did was a kind of "quasi-experiment": they had no way to assign groups randomly, but they found a natural comparison group —

- Discussion boards with general content: could be cited by Google's AI Overviews.
- Discussion boards with adult-only content: are not cited by Google's AI Overviews.

Comparing how the two groups changed before and after Google AI Overviews launched, the results were:

| Measure | Change |
|---|---|
| Daily comments on general discussion boards | Up 12.0% |
| Number of people commenting on general discussion boards | Up 12.4% |
| Effect on experience-sharing boards compared with factual Q&A boards | 2.3 times the effect on comments, 2.8 times the effect on commenters |
| Relative increase for small-to-medium discussion boards | Comments up 55.6%, commenters up 77.2% |

"Small-to-medium discussion boards" in the table means: divide all discussion boards evenly into four groups by size from smallest to largest, and take the second group (the second smallest).

In other words, **after Google's AI Overviews launched, community activity on Reddit actually increased, and experience-sharing and small-to-medium communities benefited most.**

But the story has a second half. Google later launched its conversational "AI Mode". After it launched, the extra advantage experience-sharing boards had gained shrank noticeably:

- The extra advantage in comments fell from 9.54 to -0.17, almost completely gone.
- The extra advantage in commenters fell from 6.29 to 2.57, shrinking by 59%.

One reading that makes sense is:

- **Static AI summaries** "bring" people over to look at discussions.
- **Conversational AI** "absorbs" the discussion into the conversation, so people no longer need to click through.

For approaches that rely on communities to bring visitors, this is a structural warning sign: **on the same platform, a change in the form of the AI interface alone is enough to cancel most of the traffic-driving effect.**

It also needs to be clear what this study measured: it only looked at two Google interfaces, and only measured activity at the level of Reddit discussion boards; **it did not measure brand exposure, nor how traffic turns into business**.

---

## 6. Pages anyone can write on are the easiest place to strike

Researchers ran tests in a controllable experimental system. This system is an open-source "deep research" AI — it issues many searches on its own, reads many web pages, and then writes a research report. They found:

**1. However much it searches, it still ends up concentrated on a few pages.** Even when AI splits a question into many smaller questions and searches them separately (query fan-out), the results pulled back still converge on a small number of pages. Among them, community pages where anyone can post and edit made up 16.7% to 23.4% of the URLs pulled back; and among those community pages, Reddit made up 53.7% to 70.7%.

**2. Changing just one page by adding about 13 words may be enough to sway the report.** On **one** community page that would be pulled back, the researchers added about 13 words, and the results were:

- Probability this page was read by AI: 57% to 76%.
- Probability this page was cited: 34% to 61%.
- Probability the final report mentioned the brand the researchers specified: 22% to 37%.
- If this page was not read by AI, the probability of mentioning the specified brand was 0.

**3. Once it is read, the effect is strong.** In one of the AI systems, as long as this page was read, the citation rate was 100%. Another system picks segments by "semantic similarity" (technically called embedding vectors); it resisted this attack best, but as long as it read this page, the probability of mentioning the specified brand was still 37.8%.

**4. Even very few added words work.** Even when the added text made up only 0.5% to 3.9% of the whole page, as long as the page was read, the probability of mentioning the specified brand was still 29.7% to 52.5%.

**5. Existing defences do not work well.**

- One method checks "how unnatural the text reads" (technically called perplexity) to try to pick out the added text. Its ability to detect it was weak: on a score where 0.5 means random guessing and 1 means perfect, it came in below 0.68, and its judgement pointed in the opposite direction from what was expected.
- Another method filters by comparing the similarity of output content; it did not work.
- Not reading community pages at all can block this attack, but it also loses the genuinely valuable knowledge in communities.

The researchers also looked at commercial AI, but only observed citations and did no attack testing: in Gemini's deep research feature, 623 of 5,157 citations (12.1%) came from community pages anyone can write on; in ChatGPT's deep research feature it was only 0.4%.

This is **evidence that only proves a mechanism**: it proves that in a reproducible system, "this attack can be done, and it is hard to catch". But it **cannot be used to directly infer** the same success rate on commercial AI.

Its real meaning is: **the reason community content is attractive to people who want to be seen by AI is exactly the reason it is so easily abused.**

---

## 7. How strong is the evidence? One summary table

| Conclusion | Type of evidence | Strength and scope |
|---|---|---|
| Google AI Overviews increased activity on general Reddit discussion boards by about 12%; the conversational AI Mode weakened the advantage of experience-sharing boards | Large-scale quasi-experiment with real users | Strong. Only covers two Google interfaces and only measures activity at Reddit discussion-board level; does not measure brand or traffic turning into business |
| The share of citations going to communities differs a lot between systems (0.1%, 8.5%, 13.4%) | One-off snapshot on real AI search | Moderate. General-knowledge questions, not commercial questions; only one snapshot taken |
| Forums in Google AI Overviews are "listed a lot, used little" | Examination on real AI search | Moderate. The direction is credible; the size is affected by the calculation method |
| Reddit's own AI search favours high-scoring, top-level, formal comments and removes the first person | External observation of a real platform | Moderate. Only covers Reddit's own AI search; correlation, not causation |
| Claude's search results contain no Reddit; ordinary chat models cite Reddit only 0.4% of the time | Real conversation logs and examination of real AI | Moderate. Snapshots from the study period; platform policies change |
| Adding about 13 words to a community page can sway a deep research report | Controllable experimental system | Only proves a mechanism. Actual success rate on commercial AI unknown |
| Ordinary posts on low-barrier platforms that AI already favours can get into the citations and answers of most commercial AI search | Researchers posted under control on 10 real AI search platforms and tracked for several days | Moderate. Limited to fictional or niche topics; for topics already discussed a lot, only 3.5% made it into the answer; citations are unstable |
| Brands taking part on Reddit can make the brand appear more often in AI answers | Before-and-after comparisons done by people working in the field | Weak. No randomised control; most authors themselves admit they cannot prove causation |

**The biggest gap right now:** to date, no study has used random assignment or a quasi-experiment to prove that "brands taking part on social platforms" raises AI **visibility**, traffic or business. Academic research cares about "how AI handles community content", not "how brands make use of communities". That said, the layer "can posts get into AI citations" now has evidence from controlled tests (see the table above); what is still missing is whether real brands in competitive categories get recommended, and gain traffic and business, as a result.

---

## 8. Controversies: what people say often contradicts itself

### Controversy 1: Is Reddit really the source AI cites most often?

Many people in the industry believe Reddit is still the source AI cites most. But "many people believe" does not mean "it is right". This view is itself disputed, and some people working in the field explicitly disagree. The numbers from each side are as follows:

**Position 1: Reddit's share of citations is very low.** Someone in the industry tested this themselves (no one has independently verified it): from March to June 2026, using about 16,400 commercial questions, they tested 5 AIs and collected 127,198 citations in total. Reddit made up only 1.8%, and Wikipedia less than 0.6%. About 90% of citations went to vendors' documentation, product pages, and all kinds of niche directory sites. The questions here had purchase intent, and the unit counted was the website (not the individual URL).

**Position 2: Reddit citations appear almost only on Google's products.** Another person in the industry tested this themselves: out of about 74,000 citations, those pointing to Reddit came from Google's AI Mode 528, Gemini 258, ChatGPT 23, Claude 1, and Perplexity 0 (and Perplexity cited 17,476 sources in total during this period). Google's two products together made up about 97%. However, the brands this author tracked lean towards niche markets and business-to-business (B2B) markets, and he himself says the results should not be treated as a law.

**Position 3: Reddit is one of the main sources for all the major AIs, and Perplexity is the most active.** Someone in the industry tracked a client of a website plugin for 8 weeks and found that, among the top 8 cited sources, 2 were Reddit threads from 2022 and 2023. This is just a single client in a single niche market.

**Position 4: Results from academic research.** As mentioned earlier: only 0.4% of ordinary chat models' citations pointed to Reddit; Claude's search results contained no Reddit at all. These are snapshots from the study period.

**How to make sense of these contradictions?** They do not necessarily cancel each other out; they measure different things:

- Different question types: commercial questions, general-knowledge questions, review-and-opinion questions.
- Different combinations of AIs tested.
- Different points in time.
- Different ways of counting: some count websites, some count URLs, some count "how many answers mention it".

Among these, "Perplexity cites Reddit most actively" and "Perplexity cited Reddit 0 times" directly conflict, and the two are only about two months apart. This fact alone shows: **AI behaviour changes very fast, and no single snapshot can be used to infer another time.**

There are also two single observations: someone in the industry saw that in the answers to his 100 "questions asked just before placing an order", Reddit's citation rate was below 5%; someone else in the industry saw Reddit frequently entering the top three cited sources in the reports he produced. Both are only single observations.

### Controversy 2: Is ChatGPT's "collapse" in Reddit citations real?

In August 2026, a widely repeated claim appeared: the share of ChatGPT search citations going to Reddit plunged by about 86% within a few days, from about 3.8% to about 0.5%. The industry generally accepts this claim, but its scope and causes are disputed.

- **Supporting "it really is low":** Someone in the industry tested this themselves, using the developer interface behind ChatGPT (the API, with web search turned on), running 1,564 questions written in real conversational language. He had planned to test 10 categories of question but only completed 7. Reddit was cited 38 times in total, 2.4%; 92% of these came from "review and opinion" questions, and all other categories were very low. The author also admits that the developer interface is not exactly the same as the App ordinary people use.
- **It may only affect ChatGPT:** Someone in the industry observed that during the same period, the share of Perplexity's citations going to Reddit on the sites he monitored did not change noticeably; Google's AI Overviews also still cited Reddit heavily.
- **Same direction, but smaller size:** Someone in the industry tracks 46 business-to-business (B2B) questions every week. Reddit's appearances fell from 9 in July to 3 at the last check in August; mid-sized vendors' blogs and comparison pages took its place. The author also warns: a 4-day observation window is too short, and fluctuations of a similar size have reversed within two weeks before.
- **Possible causes:** During the same period, tracking data indicated that the share of ChatGPT's use of the "site:" command (searching only within a particular website) rose sharply, which looks like a change in how it finds information. There were also reports that Reddit tightened its blocking of AI crawlers in mid-August. **Neither claim has been proven to be the cause.**
- **Citations disappearing does not mean influence disappearing:** Someone in the industry points out that a change in "which sources are listed" does not mean AI's behaviour has changed. If ChatGPT still follows the consensus on Reddit when recommending brands, what changed may only be "whether the source is listed". This is consistent with "used but not listed" from section 3. But **there is currently no direct evidence** that ChatGPT is still using Reddit's content.

### Controversy 3: Did Perplexity "withdraw" from Reddit, or does it "pick sources by question"?

Someone in the industry tested this repeatedly themselves, with a control group:

- On a set of 4 fixed questions, from 20 August, Perplexity did not cite Reddit in 96 consecutive checks.
- But on 26 August he added some questions containing brand names and some specific, task-type questions. Within one day, Reddit citations reappeared: 9 times in 6 days, all from these new questions.
- In the same period, the average number of sources Perplexity listed per answer fell from about 9 to about 6. However, the question mix changed during this period, so this number can only be taken as a hint.

From this the author concluded: **this is contraction by question type, not a full withdrawal.** Popular broad category terms no longer cite Reddit, while questions with brand names and specific tasks accept Reddit again.

This is only a small sample (a little more than 4 questions, a single niche market). But it reminds us: when you hear "a certain AI no longer cites Reddit", first ask: **on which questions?**

In addition, one company claims that within two weeks Perplexity went from barely citing Reddit to citing Reddit in most answers. But this claim comes from a party with a commercial interest, and no one has independently verified it.

### Controversy 4: Do new threads have the edge, or are old ones cited just as much?

Observations from different sides contradict each other:

- Someone in the industry observed: a thread from 3 weeks earlier with 40 upvotes was cited first by Perplexity, while a blog post from 2 years earlier with more external links and almost the same content ranked behind it.
- Someone else in the industry claimed: 60% of citations come from threads less than half a year old. But his claim was exaggerated in tone, and the source of the data is unclear.
- Another person in the industry observed: when the same question was run many times, Reddit threads were as stable as 96% as cited sources, and the cited threads could be traced back 7 years. The 8-week tracking mentioned earlier also found that threads from 2022 and 2023 were still being cited.
- One more company claimed: of the Reddit threads cited by AI, 60% to 70% are already archived and can no longer be commented on. But this claim comes from a party with a commercial interest, and no one has independently verified it.

These are all single observations, and they do not agree with one another. For now, all that can be said is: **both freshness and accumulated history may play a role, depending on which AI and which kind of question.**

### Controversy 5: Does a community's "consensus view" really matter more than a single web page?

Many people in the industry believe: AI relies more on views that many people in a community have discussed repeatedly until they agree than on a single, separately optimised web page. The industry also generally believes: keeping your core message consistent across the whole web is where **Generative Engine Optimization (GEO)** gets its results. But these are opinions, not proof.

Set against this view are two pieces of research evidence:

- In Reddit's own AI search, AI picks a **single** high-scoring, top-level, formal comment, and rewrites personal experience out (section 4).
- In Google's AI Overviews, forums are often listed as sources but rarely actually used (section 3).

Neither point supports the simple picture that "the whole community discussion is fully absorbed by AI".

---

## 9. What people who actually did it saw

The following cases all come from tests and observations by people working in the field. Unless stated otherwise, none had a control group, and **none can prove that community participation caused the results**.

### Case 1: 8 weeks of careful replies, a before-and-after comparison on 100 purchase questions

**What was done:** First, on ChatGPT, Perplexity, Gemini and Google's AI products, 100 questions buyers would ask were recorded as a baseline. Then, for 8 weeks in a row, useful content and replies were posted on Reddit.

**What was observed:**

| Measure | At the start | After 8 weeks |
|---|---|---|
| Number of questions where the brand appeared | 4 | 17 |
| Number of times cited | 1 | 7 |
| Visits from Reddit | 6 | 94 |
| Sign-ups | 0 | 8 |

**Key detail:** Most of the growth came from specific questions, not broad terms like "what is the best tool".

**Strength of evidence:** Someone in the industry tested this themselves; no one has independently verified it. The author himself states: this does not prove Reddit caused the growth.

**The corresponding principle:** This is consistent with the "by question type" observation in Controversy 3 — community content is more easily cited on specific, niche, task-type questions.

### Case 2: Lurk first, then take part — change in brand mention rate over 90 days

**What was done:**

1. **Lurk for 4 weeks first.** Understand each discussion board's rules, and study which comments get upvoted and which get deleted. In the first month, do not mention the brand at all; just build up an account reputation score of about 200 to 500.
2. **See which threads AI actually cites.** Ask the target questions in ChatGPT and Perplexity, note which Reddit threads they cite, and give priority to recommendation, comparison and experience threads.
3. **How to write:** Answer the question directly in the first two sentences; replace vague statements with specific numbers; write both the pros and the cons.
4. **Track weekly.** Every Monday, use the same questions to check on ChatGPT, Perplexity and Google's AI Overviews: whether the brand was mentioned, whether the tone was positive or negative, and which sources were cited.

**What was observed:**

- Within 90 days, the brand's **mention rate** in category-type AI answers rose from 8% to 39%.
- Visits from Reddit rose from about 22 a month to about 480 a month.
- 37 new sign-ups a month that could be credited to Reddit.
- Content published in the first quarter was still being cited 5 months later.
- The author also observed: small communities with only 10 to 20 threads a day often worked better than large discussion boards.

**Strength of evidence:** Someone in the industry tested this repeatedly themselves, with a control. But all the numbers are self-reported. And the author's premise is that "on many commercial questions, Reddit appears more often than brands' official websites and Wikipedia", which conflicts with the large-sample data in Controversy 1, so it should be viewed with caution.

**The corresponding principle:**

- The writing approach "answer directly in the first two sentences, formal tone, specific content" is consistent with the finding in section 4 that "AI favours formal, explanatory comments".
- "Small communities work better" points in the same direction as the finding in section 5 that "small-to-medium discussion boards were most affected by Google AI Overviews". But the two measure different things and cannot be used as proof of each other.

### Case 3: Wrote 20 posts, still not cited

Someone in the industry observed: he wrote 20 pieces of content on Reddit for a start-up, and ChatGPT still did not cite that company.

Compared with Controversy 2, this is not surprising: in the period the research shows, the share of ChatGPT's citations going to Reddit was already very low.

The lesson is: **first confirm whether your target AI cites social platforms for your type of question, then decide whether to invest.**

### Case 4: LinkedIn — another social platform, with almost the opposite rules

LinkedIn is often lumped together with Reddit as a "community source". But data from people in the industry show that the rules for AI citing LinkedIn content are almost the opposite of the rules its news feed uses for recommendations.

**First data set (someone in the industry tested this themselves; no one has independently verified it):** An analysis of 1,310,455 LinkedIn URLs cited by ChatGPT, Perplexity, Google's AI Overviews, Google's AI Mode, Copilot and Gemini from January to June 2026.

- **Likes and comments have almost nothing to do with whether something is cited.** Their correlation with the number of citations was -0.06 and -0.04 respectively (this number runs between -1 and 1; close to 0 means almost no relationship).
- **Long articles are cited more often than short posts.** LinkedIn long-form articles made up 63% of cited URLs but received 72% of citations. Long articles were cited 8.5 times per URL on average; short feed posts 5.9 times. On Copilot, 90% of LinkedIn citations were long articles.
- **Content under a personal name is cited more often than content under a company name.** Content posted under a personal name made up 88% of cited URLs and 92% of citations. Company pages were cited 5.5 times per URL on average.
- **Plain text does slightly better.** Plain-text content was cited 6.48 times per URL on average, content with images 5.91 times, and content with video 5.69 times.
- **The distribution is very uneven.** Half of the cited URLs were cited exactly 2 times; the top URL was cited 4,685 times. Follower count made little difference.
- **AIs differ a lot.** Perplexity alone accounted for 43% of LinkedIn citations; Gemini cited LinkedIn only 38 times in five months.

**Second data set (someone in the industry tested this repeatedly themselves, with a control):** Using 350 questions without brand names, run 3 times each on ChatGPT, Perplexity and Google's AI Overviews over 4 days, giving 4,581 answers and 39,236 retrieved items in total.

- Of the 22 LinkedIn URLs cited, 20 were long-form articles, and none was a short feed post.
- Of the 64 records in which LinkedIn was retrieved, 58 pointed to long-form articles.
- Of these 22 URLs, 19 were LinkedIn's localised Italian-language URLs.
- However, LinkedIn made up only 0.16% of all retrieved items (YouTube made up 1.13%). Ranked ahead of LinkedIn were the official websites of several large technology companies and the official websites of EU and US standards bodies.
- In this data set, Google's AI Overviews cited LinkedIn more often than Perplexity did (6.1% vs 3.4%), exactly the opposite of the first data set's result.
- YouTube appeared 331 times in this data set, 314 of them from Google's AI Overviews.

**Industry view:** Many people believe that posting on a LinkedIn company brand page does little for AI visibility.

**The corresponding principle:** "Popularity" signals on a social platform are not necessarily inherited by AI. Reddit's own AI search follows the scores (section 4); but when outside AIs cite LinkedIn, like counts hardly matter — **content format** (long-form, plain text, personal name) is what matters. **The rules for each platform and each AI have to be looked at separately.**

### Case 5: The relative weight of different social platforms

Someone in the industry, in a small sample, saw 86 citations from social platforms: YouTube 38, Reddit 30, LinkedIn 9, software review sites 6, and Wikipedia, Quora and Facebook 1 each.

Another person in the industry observed: with the same 40 questions and 7 AIs, Gemini cited Reddit in 22 of the questions, while ChatGPT did so in at most 1.

These are all single observations, and can only suggest: **do not treat "social platforms" as one whole, and do not average the numbers across different AIs.**

---

## 10. Taking part properly versus tampering: what's the difference?

### What taking part by the rules looks like

The following approaches comply with community rules and are also compatible with the mechanisms described in this chapter:

- Answer real questions under your real identity, and state your relationship to the brand.
- Share specific, verifiable experiences and numbers, and write both the pros and the cons.
- Follow each discussion board's rules and accept moderation.
- In threads that AI already cites and that are still open for comments, add new information rather than repeating promotion.

Someone in the industry observed: in business-to-business (B2B) fields, only "personal accounts that disclose their identity" can be sustained over the long term. Accounts carrying a brand logo, even with helpful content, are easily rejected by niche communities. Because once a community decides you are "here to grab something for yourself", it will downvote and report you.

### What manipulation looks like (this book does not recommend it)

- **Using large numbers of farmed old accounts and high-reputation accounts to post brand recommendations in bulk.** Someone in the industry observed that there really are people on the market offering this service: holding thousands of old accounts, charging monthly, posting threads and comments on clients' behalf, and even offering a service to "get rid of negative threads". Someone else in the industry admitted themselves that this is not allowed on the platform and is a rule-breaking practice.
- **Manufacturing brand mentions that "look natural".**
- **Stuffing short phrases into threads so that a particular brand comes up when AI retrieves them.** This is exactly the technique the researchers in section 6 used to prove the attack was feasible.
- **Asking and answering your own questions, and upvoting each other**, to push comment scores up.

### The cost of manipulation

| Risk | Basis |
|---|---|
| **Accounts banned, content deleted** | Someone in the industry observed: even without selling, just offering expert opinions, taking part in discussions often gets you blocked, and appeals get no response. Community rules are becoming more and more conservative. |
| **Citation sources cut off** | The crawling and licensing relationships between platforms and AI companies change. Around mid-August, the share of ChatGPT's and Perplexity's citations going to Reddit both fell sharply (Controversies 2 and 3). A strategy built on a single platform may stop working within days. |
| **Flagged by moderators, and so not picked** | In Reddit's own AI search, comments pinned or flagged by moderators are almost never picked (section 4). |
| **Rewritten by AI, losing the original meaning** | Even if picked, first-person experience gets rewritten into general advice (section 4); forum content is cited in Google AI Overviews but rarely actually used (section 3). |
| **Defenders are targeting the pollution of community pages** | Researchers have already pointed out that "not reading community pages" is an effective line of defence. If AI companies adjust in this direction, approaches that rely on manipulating community content will be the first to be affected. This is an inference; there is currently no evidence it has happened. |
| **Damage to brand reputation** | Once a community sees through it, the negative discussion itself may also become a source AI cites. This is a concern in the industry; there is currently no systematic evidence. |
| **Deleting a post doesn't stop it being cited** | Researchers found on real AI search that after a post was deleted, one platform kept citing it for about 4 more days. If you post something wrong, don't count on deleting it to take it back right away. |

---

## 11. What to do, what not to do, and outdated approaches

### What you can do, and how strong the evidence is

| Approach | Strength of evidence |
|---|---|
| **Measure first, then invest.** For your core questions, record on each AI one by one which websites it cites, and confirm whether social platforms are among them. Do not rely on vague claims like "AI loves citing Reddit most". | Researchers ran repeated tests on real AI search and found that sources differ hugely between AIs. |
| **Plan separately for each AI.** Unless your data show other AIs responding too, treat community work as an approach that "mainly affects Google's AI products". | Examination of real AI search, plus tests by people in the industry themselves. |
| **Plan separately for each question type.** Community content is more likely to be cited on review-and-opinion, specific task-type and brand-name questions, and less on broad category terms. | Someone in the industry tested this repeatedly themselves with a control, plus tests by people in the industry themselves. |
| **Take part in threads that are already cited and still open for comments.** Start from the list of threads AI actually cites, and judge whether you have specific content to add. | Tests by people in the industry themselves. Someone in the industry also observed that some cited threads have already been removed or archived. |
| **Write formally, specifically, and in a form that can be used directly.** Answer the question in the first two sentences, give specific numbers, write both pros and cons. (Note: this is for being picked by AI. Simulation research shows that AI's idea of a "popular answer", one with more arguments, evidence and steps, has almost nothing to do with real people's votes; winning real people's votes in a Q&A community is a different goal.) | External observation of a real platform (only Reddit's own AI search; correlation, not causation), plus tests by people in the industry themselves. |
| **Take part under your real identity, and state your relationship to the brand.** | Observations by people in the industry; from the point of view of following the rules, this is essential. |
| **On LinkedIn, prefer writing long-form articles under a personal name rather than posting short updates from a brand page.** | Tests by people in the industry themselves, plus someone in the industry testing repeatedly with a control. |
| **Measure "being cited" and "bringing visitors and potential customers" separately.** | People in the industry observed that the two often do not move together; research also found that "being cited" and "being used" do not match. |
| **Track for several weeks in a row, look at each AI separately, and do not look at just one result.** | In tests by people in the industry, large short-term swings that later reversed happened many times. |

### Don't do this

- Don't farm accounts, buy comments, or post brand recommendations in bulk.
- Don't stuff brand phrases meant for AI into threads.
- Don't promote in communities only with a brand account.
- Don't judge a community's influence only by "whether Reddit is in the source list". Being cited is not the same as being used, and being used does not always mean being cited.
- Don't average all AIs' numbers into a single "AI visibility".
- Don't bet your whole budget on a single social platform. A platform's crawling policy may change within days.

### Outdated approaches

- **"Reddit is the source AI cites most often, so go all in on Reddit."** At least for commercial questions in 2026, on ChatGPT and Claude, and on Perplexity during certain periods, this premise does not hold.
- **"Posting on Reddit lets you influence every AI."** Each AI's sources are almost a different world.
- **"Chasing community popularity equals chasing AI visibility."** On LinkedIn, like counts have almost nothing to do with whether something is cited by AI.

---

## Key points of this chapter

1. The weight of social platforms in AI search depends on "**which AI × which kind of question × what time**". Google's AI Overviews and AI Mode use community sources heavily; other AIs rarely cited Reddit during the study periods, and Claude's search results contained no Reddit at all.
2. "Reddit is the source AI cites most often" is a disputed claim. On commercial questions, large-sample data show Reddit makes up only a very small share, with most citations going to vendors' documentation and product pages.
3. Around August 2026, the share of ChatGPT's and Perplexity's citations going to Reddit both fell sharply. But the scope, the causes, and whether it will last are all disputed. Perplexity's change looks like "contraction by question type".
4. Being cited is not the same as being used: forum sources in Google AI Overviews are cited a lot and used little; the other way round, a great deal of content is used but not listed.
5. AI's selection step inherits the community's prominence signals: it favours high-scoring, top-level, formal comments, and rewrites first-person experience into general advice.
6. A large-scale experiment with real users showed that Google's AI Overviews boosted community activity on Reddit, with experience-sharing and small-to-medium communities benefiting most; but the conversational AI Mode weakened this effect.
7. "Brands taking part in communities can raise AI visibility" is currently supported only by before-and-after comparisons from people in the industry, with no causal evidence; the cases that worked are all concentrated on specific, niche questions.
8. Community pages anyone can write on are a single-point attack surface: manipulation is mechanically possible and hard to detect. But manipulation carries the risks of banned accounts, deleted posts, sources being cut off and damaged reputation. Taking part by the rules (real identity, disclosed relationship, specific contributions) is the only approach that can last.

---

## Closing: back to that owner

Where the owner from the opening went wrong was not going to Reddit, but treating one "I heard that…" as a map.

Communities are a very important part of **other people's word of mouth**. But each librarian flips through a different bookshelf, each kind of question calls for different books, and the bookshelves may be moved at any time.

Measure first, then invest; look at things separately, don't average; speak honestly under your real identity, and don't tamper.

---

### Remember in one sentence

How much community word of mouth matters in AI's eyes depends on which AI, which kind of question, and what time; measure clearly first, then take part properly under your real identity.

### What you can do tomorrow

1. **Measure first.** List the core questions you care about most, ask each AI you care about one by one, note which websites they cite, and confirm whether social platforms are actually among them. Do not rely on claims like "AI loves Reddit most".
2. **Plan separately for each AI.** Unless your own data show other AIs responding too, start by treating community work as an approach that "mainly affects Google's AI products".
3. **Plan separately for each question type.** Aim first at review-and-opinion, specific task-type and brand-name questions, rather than broad category terms.
4. **Start from threads AI already cites and that are still open for comments.** Think about whether you have specific new content to add. Note that some cited threads have already been removed or archived.
5. **Write formally, specifically, and in a form that can be used directly.** Answer the question directly in the first two sentences, give specific numbers, write both pros and cons.
6. **Take part under your real identity, and state your relationship to the brand.** In business-to-business fields, use personal accounts that disclose your identity; don't rely only on brand accounts.
7. **On LinkedIn, prefer writing long-form articles under a personal name**, rather than posting short updates from a brand page.
8. **Record "being cited" and "bringing visitors and potential customers" separately.**
9. **Track for several weeks in a row, looking at each AI separately.** Don't be scared by a single result, and don't jump to conclusions because of one good result.

### Stop doing this

1. **Stop believing "Reddit is the source AI cites most often, so go all in on Reddit".** At least for commercial questions in 2026, on ChatGPT and Claude, and on Perplexity during certain periods, this premise does not hold.
2. **Stop thinking "posting on Reddit lets you influence every AI".** Each AI's sources are almost a different world.
3. **Stop treating community popularity as AI visibility.** On LinkedIn, like counts have almost nothing to do with whether something is cited by AI.
4. **Stop farming accounts, buying comments and posting brand recommendations in bulk, and stop stuffing brand phrases meant for AI into threads.**
5. **Stop promoting in communities only with a brand account.**
6. **Stop looking only at whether Reddit is in the source list, and stop averaging all AIs' numbers into one score.**
7. **Stop betting your whole budget on a single social platform.**

### What is still uncertain

1. **Does brand participation in communities actually raise AI visibility, traffic or business?** No study using random assignment or a quasi-experiment has proven it so far; there are only before-and-after comparisons by people in the industry, and most authors themselves admit they cannot prove causation.
2. **Is Reddit really the source AI cites most often?** The numbers from different sides conflict; question types, AI combinations, timing and counting methods all differ, and no single snapshot can be used to infer another time.
3. **The plunge in ChatGPT's Reddit citations in August 2026**: its scope (only ChatGPT, or other AIs too), its cause (a change in how it finds information, or Reddit tightening its blocking), and whether it will last are all still unsettled. There is also no direct evidence on whether ChatGPT is still "using but not listing" Reddit's content.
4. **Has Perplexity fully withdrawn from Reddit, or only contracted on certain questions?** There are currently only small-sample observations; the claim that it "went from barely citing to citing in most answers within two weeks" comes from a party with a commercial interest and has not been independently verified.
5. **Do new threads have the edge, or are old ones just as good?** Observations contradict each other; claims like "60% come from the last half year" and "60% to 70% are already archived" have unclear sources or have not been verified.
6. **Does a community's "consensus view" matter more than a single web page?** This is an industry view; existing research does not support the simple picture that "the whole community discussion is fully absorbed".
7. **The precise size of how "little forums are used" in Google AI Overviews** is affected by the calculation method; only the direction is credible.
8. **The actual success rate of tampering with community pages on commercial AI** is still unknown; whether AI companies will start blocking community pages is also only an inference.
9. **Whether negative discussions will become sources AI cites and in turn hurt brands** is currently only a concern in the industry, with no systematic evidence.
10. **On LinkedIn, which AI cites it most often**: the two data sets give exactly opposite results.
