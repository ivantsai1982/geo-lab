# Chapter 15: The Role of Reddit and Social Platforms in AI Search

> Where this chapter sits: the book's main thread is "triggering → accessibility → retrieval → selection/ranking → citation → absorption → user behavior". Social platforms affect several of these stages at once: whether they can be crawled (accessibility), whether they are retrieved (retrieval), which comments on the platform are picked (selection), whether content is actually used once cited (absorption), and whether AI summaries in turn change engagement within the communities themselves (user behavior). This chapter discusses Reddit as "the platform being studied" and uses LinkedIn as a point of comparison.

## Questions this chapter answers

1. Why do social platforms (especially Reddit) appear among the citations in AI answers? On which engines and for which question types are they cited?
2. Does the claim "Reddit is the source AI cites most" hold up? What happened to citation shares in 2026?
3. Once community content is cited, how much of it does AI actually use? What kind of comment gets cited?
4. Can compliant participation in community discussions raise a brand's mention rate in AI answers? How strong is the evidence?
5. What are the risks of manipulating community content (fake comments, cultivating accounts, planting brands in threads)?

## 1. Core principles

### Principle 15.1: Social platforms are part of the "third-party source ecosystem", but their weight varies by engine

The second consensus statement in the book's main thread is that whether you enter the candidate set depends on accessibility, language and market, the third-party source ecosystem, and relevance. Social platforms belong to the third-party source ecosystem. What makes them special:

- The content consists of real users' experiences, comparisons and recommendations, which map directly onto questions such as "which one works well" and "has anyone used this".
- The content is editable user-generated content (UGC) that anyone can post. This is both why it gets used and the entry point for manipulating it.
- Whether AI can use it depends on the crawling and licensing relationships between the platform and each AI vendor, and these relationships change.

So there is no single answer to "how important are social platforms in AI search". It is a function of three things: **engine × question type × time**.

```
Community content
  │
  ├─ Accessibility: does the platform allow this engine to crawl / use it? (changes with policy)
  │
  ├─ Retrieval: does this engine's retrieval put community pages into the candidate set? (varies enormously between engines)
  │
  ├─ Selection: which comment in the thread is picked? (skews toward high-scoring, top-level, formal-toned comments)
  │
  ├─ Citation: is it listed as a source?
  │
  └─ Absorption: once listed as a source, how much of the content is actually used? (forums are often "cited a lot, used little")
```

### Principle 15.2: The source pools of different engines are almost separate worlds

Repeated tests on real AI search engines found that the same set of questions draws very different sources on different systems. A cross-system audit using 11,000 questions from a standard question-answering dataset found:

| System | Share of citations going to social platforms |
|---|---|
| GPT with web search (Search GPT) | 0.1% |
| Google AI Overviews (AIO) | 8.5% |
| Google organic search results | 13.4% |

In the same study, Search GPT's top 100 domains overlapped with those of AIO and the organic results by only 24% and 25%; AIO and the organic results overlapped by 68%. That is, **Google's AI Overviews largely reuse Google Search's source pool, while other engines' source pools are a world of their own**.

Another study, based on real conversation logs donated by users (613 users, 171,264 conversations) plus controlled replays, found that reddit.com and youtube.com appear in ChatGPT's and Grok's search results but are completely absent from Claude's search results. In another audit of general-purpose large language models (GPT-4o-mini, GPT-5), only 18 of 4,932 citations (0.4%) pointed to Reddit.

Large-sample practitioner logs point the same way: Reddit citations are highly concentrated in Google's products (see Section 3).

### Principle 15.3: Being cited is not the same as being used

A citation only means "listed in the sources panel". How much content the answer actually absorbs is a separate matter.

An audit on real AI search engines found that in Google AIO, the degree to which content from community/forum sources is used is 22.1 percentage points lower than the degree to which it is cited; conversely, Wikipedia and longer documents are over-used. Put plainly, **AIO often lists forums as sources, but the answer's content mainly comes from elsewhere**.

This finding carries a measurement caveat: the study measures coverage by "taking the maximum similarity across passages", and this method partly amplifies length effects. With the mean instead, the extent to which short sources are under-used shrinks considerably. So the direction ("under-used") is credible, but the exact magnitude should not be taken at face value.

The opposite phenomenon also exists. The conversation-log study mentioned above found that 14–53% of claims in answers were in fact supported by search results but were not cited. That is, **some sources are used without being listed, and some are listed without being used**. Judging the influence of community content from the citation panel alone goes wrong in both directions.

### Principle 15.4: AI inherits the community's "visibility signals" and erases the first person

On the platform's own generative search (Reddit Answers), a black-box audit covering 30,000 answers found:

- **Selection favors comments that are already prominent**: each one-standard-deviation increase in a comment's score percentile within its thread multiplies the odds of being selected by 2.88; top-level comments have 1.97 times the odds of other comments. The median score percentile of selected comments is 0.91, against 0.45 for unselected ones.
- **A formal tone is favored and an experiential tone is disfavored**: the odds ratio for formality is 1.488; for experiential tone it is 0.789 (that is, less likely to be selected).
- Testimony is rewritten into generalized advice: first-person singular makes up 3.3% of the original comments but only 0.06% of the synthesized answers.
- Comments pinned or flagged by moderators are almost never selected: odds ratios of 0.010 and 0.052 respectively.
- Almost all variation in answers comes from retrieval: when the same question is re-run, 41.8% of the time exactly the same sources are retrieved; when the sources are the same, 89.6% of answers are nearly identical.

These are observational associations, not causation. But they illustrate a mechanism: AI's selection layer does not set up its own independent assessment of quality; it reuses the community's own "who is loudest" signal. A comment upvoted to the top by the community is more likely to be selected by AI; a sincere personal experience, even if selected, is rewritten into advice without the "I".

### Principle 15.5: AI summaries change the communities themselves

Large-scale experiments with real users show that after Google AI Overviews launched, community engagement on Reddit actually increased. This quasi-experiment used a sample of 105,012 subreddits, comparing general-content communities that AI Overviews can cite with adult-only (NSFW) communities that are not cited:

| Metric | Change |
|---|---|
| Daily comments in general communities | +12.0% |
| Commenting users in general communities | +12.4% |
| Effect in experience-based communities vs fact-based communities | 2.3 times for comments, 2.8 times for users |
| Relative increase in small and mid-sized communities (second quartile) | 55.6% for comments, 77.2% for users |

But after the conversational Google AI Mode launched, the premium for experience-based communities shrank markedly: the comment premium fell from 9.54 to -0.17, and the user premium from 6.29 to 2.57 (a 59% decay).

The mechanistic interpretation: **static summaries "direct" users toward discussions; conversational interfaces "absorb" the discussion into the conversation, so users no longer need to click through**. This is a structural warning for strategies that rely on community-driven traffic: on the same platform, a change in interface form alone is enough to cancel out most of the referral effect.

### Principle 15.6: Editable UGC pages are a single point of attack

In controlled experimental systems (open-source deep-research agent pipelines), researchers found:

- Even when deep-research agents issue many queries (query fan-out), retrieval results still converge on a small number of pages. UGC accounts for 16.7–23.4% of retrieved URLs, and Reddit accounts for 53.7–70.7% of the UGC.
- Appending about 13 words to a single retrieved UGC page: the probability that the agent sees the page (exposure) is 57–76%, that it is cited 34–61%, and that the report mentions the attacker's chosen entity 22–37%. When the page is not seen, the mention rate is 0.
- Once exposed, one of the agent systems had a 100% citation rate; another system, which selects passages using embedding vectors, was the most resistant, but its conditional mention rate was still 37.8%.
- Even when the poisoned text made up only 0.5–3.9% of the full text, the conditional mention rate was still 29.7–52.5%.
- Existing defenses work poorly: detecting poisoned text with perplexity gave an AUROC below 0.68, and in the wrong direction; filtering by output similarity was ineffective. Blocking UGC entirely stops the attack, but loses community knowledge.

On commercial systems, the researchers only observed citations: in Gemini's Deep Research, 623 of 5,157 citations (12.1%) were UGC; in OpenAI's Deep Research, only 0.4%.

This is grade D evidence: it proves that "the attack is feasible and hard to detect" in a reproducible pipeline, but one cannot directly infer the same success rate on commercial engines. Its significance is to show that **the very thing that makes community content attractive for GEO is what makes it easiest to abuse**.

## 2. How strong is the evidence

| Conclusion | Type of evidence | Strength and scope |
|---|---|---|
| AIO raised engagement in general Reddit communities by about 12%; AI Mode weakened the experience-based premium | Large-scale quasi-experiment with real users | Strong. Limited to two Google interfaces and community-level engagement on Reddit; does not measure brand or traffic conversion |
| Social citation shares differ widely between systems (0.1% / 8.5% / 13.4%) | Single-snapshot audit of real engines | Medium. General-knowledge questions, not commercial ones; single snapshot |
| AIO forums "cited a lot, used little" | Audit of real engines | Medium. Direction credible; magnitude affected by measurement method |
| Reddit Answers favors high-scoring, top-level, formal comments and erases the first person | Black-box audit of a real platform | Medium. Limited to Reddit's own search; observational associations |
| Reddit does not appear in Claude search; general-purpose LLMs cite Reddit only 0.4% of the time | Real-engine logs and audits | Medium. Snapshot from the study period; platform policies change |
| Appending about 13 words to a UGC page can manipulate deep-research reports | Controlled experimental system | Mechanistic evidence. Actual success rate on commercial engines unknown |
| Ordinary posts on low-barrier platforms that AI already favors can enter the citations and answers of most commercial AI search engines | Repeated tests on real AI search engines (10 platforms, controlled posting, multi-day tracking) | Medium. Limited to fictional or low-competition topics; for topics with extensive existing discussion, only 3.5% made it into answer text; citations unstable |
| Participating on Reddit can raise a brand's mention rate in AI answers | Practitioner before-and-after comparisons | Weak. No randomized controls; most authors admit they cannot prove causation |

**Gap**: no study has yet shown, through randomized or quasi-experimental methods, that "brand participation on social platforms" causes AI visibility, traffic or conversions to rise. Academic evidence concentrates on "how AI processes community content", not "how brands can use communities". That said, there is now interventional evidence at the layer of "whether posts can enter AI citations" (see the table above); what is still missing is recommendation rates, traffic and conversions for real brands in competitive categories.

## 3. Debates and counterexamples

### Debate 1: Is Reddit really the source AI cites most?

Practitioners widely believe that Reddit is still the source AI engines cite most, but this view is itself contested, and some practitioners explicitly disagree. The data on each side:

| Position | Basis | Conditions |
|---|---|---|
| Reddit's citation share is very low | Practitioners report from their own tests: across about 16,400 commercial questions, 5 engines and 127,198 citations, Reddit accounted for 1.8% and Wikipedia for under 0.6%; about 90% went to vendor documentation, product pages and long-tail category sites | Commercial-intent questions; domain-level counts; March–June 2026 |
| Reddit citations appear almost only in Google products | Practitioners report from their own tests: of about 74,000 citations, Reddit citations came from Google AI Mode 528, Gemini 258, ChatGPT 23, Claude 1, Perplexity 0 (Perplexity cited 17,476 sources in total); Google's two products accounted for about 97% | The brands the author tracks lean niche and B2B; the author admits this should not be treated as a law |
| Reddit is one of the main sources for the major engines, with Perplexity the most active | Practitioners report from their own tests: tracking a WordPress plugin client for 8 weeks, 2 of the top 8 cited sources were Reddit threads from 2022 and 2023 | Single client, single niche |
| Academic audits: general-purpose LLMs point to Reddit only 0.4% of the time; Reddit does not appear at all in Claude search | Real-engine audits and logs | Snapshots from the study period |

**How to make sense of these contradictions**: they do not necessarily refute one another; they measure different things. Question type (commercial vs general knowledge vs reviews and opinions), engine mix, timing and counting method (domain vs URL vs answer) all differ. Among them, "Perplexity cites Reddit most actively" and "Perplexity 0" directly conflict, and were only about two months apart, which in itself shows that engine behavior changes fast and no single snapshot can be extrapolated.

One practitioner observed that in answers to their 100 bottom-of-funnel (BOFU) purchase-decision questions, the Reddit citation rate was under 5%. Another practitioner observed that Reddit often made the top three cited sources in the reports they produced. Both are single observations.

### Debate 2: Is the "collapse" of ChatGPT's Reddit citations real?

In August 2026 a widely repeated claim appeared: ChatGPT search's citation share for Reddit plummeted by about 86% within a few days (from about 3.8% to about 0.5%). Practitioners widely accept this claim, but both its scope and its cause are disputed.

- **Supporting "it really is low"**: Practitioners report from their own tests that, using OpenAI's API (with web search on), they ran 1,564 real-language questions (10 categories planned, only 7 completed); Reddit was cited 38 times in total, 2.4%; 92% of those came from "reviews and opinions" questions, with other categories very low. The author also acknowledges that the API is not fully equivalent to the consumer app.
- **Only ChatGPT affected**: One practitioner observed that over the same period Perplexity's citation share on the sites they monitor showed no clear change, and Google AI Overviews still cited Reddit heavily.
- Same direction but smaller magnitude: One practitioner observed that across the 46 B2B questions they track weekly, Reddit appearances fell from 9 in July to 3 in the last check in August, replaced by mid-sized vendor blogs and comparison pages; the author also cautions that a four-day window is too short, and swings of similar size have reversed within two weeks.
- Possible causes: tracking data from the same period indicate that the share of ChatGPT searches using the `site:` operator rose sharply, which looks like a change in how sources are obtained; there were also reports that Reddit tightened its blocking of AI crawlers in mid-August. Neither has been confirmed as the cause.
- Citations disappearing does not mean influence disappearing: one practitioner pointed out that a change in citation attribution does not mean a change in model behavior. If ChatGPT's brand recommendations still follow the consensus on Reddit, what changed may only be "whether the source is listed". This is consistent with the "invisible use" in Principle 15.3, but there is currently no direct evidence that ChatGPT is still using Reddit content.

### Debate 3: Did Perplexity "withdraw" from Reddit, or "contract by question type"?

Practitioners' repeated, controlled tests found that on a set of 4 fixed questions, Perplexity did not cite Reddit in 96 consecutive checks from 20 August onward; but for brand-name queries and task-type questions newly added on 26 August, Reddit citations reappeared within a day (9 times in 6 days, all from the new questions). Over the same period, the number of sources per Perplexity answer fell from about 9 to about 6 (the question mix changed, so this can only be taken as a hint).

On this basis the author judges that **this is contraction by question type, not a full withdrawal**: the core head terms of the category no longer cite Reddit, while brand and task-type questions accept it again. This is only a small sample (4+ questions, a single niche), but it reminds us that conclusions such as "engine X no longer cites Reddit" must first ask "on which questions?"

A vendor claims that Perplexity once went from almost never citing Reddit to citing it in most answers within two weeks, but this claim comes from a party with a commercial interest and has not been independently verified.

### Debate 4: Does freshness matter, or are old threads cited just the same?

- One practitioner observed that a 3-week-old thread with 40 upvotes was prioritized by Perplexity over a 2-year-old blog post with many external links and nearly identical content.
- Another practitioner claimed that 60% of citations come from threads less than six months old (the claim is exaggerated in tone and the data source is unclear).
- But another practitioner observed that across multiple runs of the same question, Reddit threads were stable as cited sources up to 96% of the time, and cited threads could be traced back 7 years; the 8-week tracking mentioned above also found that threads from 2022 and 2023 were still cited.
- A vendor claims that 60–70% of the Reddit threads cited by AI are archived and can no longer be commented on, but this claim comes from a party with a commercial interest and has not been independently verified.

These are all single observations and they are inconsistent with one another. All that can be said for now is: **both freshness and accumulated history may play a role, depending on the engine and the question**.

### Debate 5: Does a community "consensus narrative" really matter more than a single page?

Practitioners widely believe that AI relies more on consistent narratives formed through repeated, multi-party discussion in communities than on a single optimized page; they also widely believe that consistent core messaging across the web is the source of GEO results. This is opinion, not proof.

The academic evidence on the other side: in Reddit Answers, AI picks **single** high-scoring, top-level, formal comments and rewrites away personal experience; in AIO, forums are cited but little used. Neither point supports the simple picture that "community narratives are absorbed whole".

## 4. Cases

The following cases come from practitioners' tests and observations. Unless stated otherwise, none had a control group, so none can prove causation.

### Case 1: 8 weeks of helpful replies, a before-and-after comparison on 100 purchase questions

- **What was done**: on ChatGPT, Perplexity, Gemini and Google's AI products, a baseline was first recorded for 100 questions buyers would ask; then helpful content and replies were posted on Reddit for 8 consecutive weeks.
- **What was observed**:

| Metric | Baseline | After 8 weeks |
|---|---|---|
| Questions in which the brand appeared | 4 | 17 |
| Citations | 1 | 7 |
| Visits from Reddit | 6 | 94 |
| Sign-ups | 0 | 8 |

- Key detail: most of the growth came from specific, question-style queries, not head terms such as "the best tool".
- Evidence strength: practitioners report from their own tests. The author states that "this does not prove Reddit caused the growth".
- Related principle: consistent with the "by question type" observation in Debate 3: community content is more easily cited on specific, long-tail, task-type questions.

### Case 2: Lurk first, then participate: changes in brand mention rate over 90 days

- **What was done**:
  1. Lurked for 4 weeks before posting, learning each subreddit's rules and studying which comments got upvoted and which got removed; zero brand mentions in the first month, building up about 200–500 comment karma.
  2. Asked the target questions in ChatGPT and Perplexity, recorded which Reddit threads they cited, and prioritized recommendation, comparison and experience threads.
  3. When writing, answered the question directly in the first two sentences, replaced vague statements with specific numbers, and covered both pros and cons.
  4. Every Monday, used the same questions in ChatGPT, Perplexity and Google AI Overviews to track whether the brand was mentioned, the sentiment, and the cited sources.
- **What was observed**: within 90 days the brand's mention rate in category-type AI answers rose from 8% to 39%; visits from Reddit rose from about 22 a month to about 480; 37 new sign-ups a month were attributed to Reddit; content published in the first quarter was still being cited 5 months later. The author also observed that small communities with 10–20 threads a day often performed better than large subreddits.
- Evidence strength: practitioners' repeated, controlled tests. But all the numbers are self-reported, and the author's premise that "Reddit appears more often than brand websites and Wikipedia on many commercial questions" conflicts with the large-sample data in Debate 1, so treat it with caution.
- Related principle: "answer directly in the first two sentences, formally and specifically" is consistent with the finding in Principle 15.4 that AI favors formal, directive comments; "small communities work well" points in the same direction as the finding in Principle 15.5 that small and mid-sized communities are most affected by AIO, but the two measure different things and cannot prove each other.

### Case 3: 20 posts written, still not cited

One practitioner observed that after writing 20 pieces of content on Reddit for a startup, ChatGPT still did not cite the startup. In light of Debate 2, this is not surprising: during the period the studies cover, ChatGPT's citation of Reddit was already very low. **First confirm whether the target engine cites social platforms for your question type, then decide whether to invest**.

### Case 4: LinkedIn: a comparison with another social platform

LinkedIn is often grouped with Reddit as a "community source". Practitioner data show that the rules by which it gets cited are almost the opposite of its feed algorithm:

- Practitioners report from their own tests: among 1,310,455 LinkedIn URLs cited by ChatGPT, Perplexity, Google AI Overviews, AI Mode, Copilot and Gemini from January to June 2026:
  - Likes and comments are almost unrelated to being cited (Pearson correlation coefficients of -0.06 and -0.04 respectively).
  - Pulse long-form articles made up 63% of cited URLs but 72% of citations; on average 8.5 citations per URL, against 5.9 for short feed posts; on Copilot, 90% were long-form.
  - Content under individuals' names made up 88% of cited URLs and 92% of citations; company pages averaged 5.5 per URL.
  - Text-only posts (6.48) were slightly higher than posts with images (5.91) and video (5.69).
  - Half of cited URLs were cited exactly twice; the top one was cited 4,685 times. Follower count had little effect.
  - Perplexity alone accounted for 43% of LinkedIn citations; Gemini cited LinkedIn only 38 times in five months.
- Practitioners' repeated, controlled tests found that across 350 non-brand questions (ChatGPT, Perplexity, Google AI Overviews, each run 3 times over 4 days, 4,581 answers and 39,236 retrievals in total), 20 of the 22 cited LinkedIn URLs were Pulse long-form articles and none were short feed posts; 58 of 64 retrievals pointed to Pulse; 19 of the 22 were on Italy's localized LinkedIn domain. However, LinkedIn accounted for only 0.16% of all retrievals (YouTube 1.13%), ranking behind microsoft.com, ibm.com, europa.eu and nist.gov. In this data set AI Overviews cited LinkedIn more often than Perplexity (6.1% vs 3.4%), the reverse of the previous result; and 314 of YouTube's 331 appearances came from AI Overviews.
- Practitioners widely believe that posts on LinkedIn company brand pages do little for AI visibility.

**Related principle**: the "popularity" signals on social platforms are not necessarily inherited by AI. Reddit Answers inherits the score signal (Principle 15.4), but when external engines cite LinkedIn, like counts are almost irrelevant; content form (long-form, text-only, under an individual's name) is what matters. **Each platform and each engine has to be looked at separately**.

### Case 5: The relative weight of different social platforms

One practitioner observed that in their small sample of 86 citations to social sources: YouTube 38, Reddit 30, LinkedIn 9, G2/Capterra 6, and Wikipedia, Quora and Facebook 1 each. Another practitioner observed that for the same 40 questions on 7 answer engines, Gemini cited Reddit in 22 of them, and ChatGPT in at most 1. These are all single observations and can only hint: **do not treat "social platforms" as a single whole, and do not average the numbers across engines**.

## 5. Compliant participation vs manipulation

### 5.1 What counts as compliant participation

The following practices are within community rules and are compatible with the mechanistic evidence in this chapter:

- Answer real questions under your real identity and disclose your relationship with the brand.
- Contribute specific, verifiable experience and data, covering both pros and cons.
- Follow each subreddit's rules and accept moderation.
- Add new information to threads that AI already cites and that are still open for discussion, rather than repeating promotion.

One practitioner observed that in B2B, only "personal accounts with identity disclosure" work over the long term; accounts carrying a brand logo, even with helpful content, are easily rejected in niche communities, because once a community decides you are "here to extract value", it downvotes and reports.

### 5.2 What counts as manipulation

The following practices are manipulation, and this textbook does not recommend them:

- Using large numbers of cultivated aged accounts or high-karma accounts to post brand recommendations in bulk. One practitioner observed that there are services on the market that use thousands of aged accounts to post threads and comments on your behalf for a monthly fee, and even offer to remove negative threads; another practitioner admitted that this is "not allowed" on the platform and is a black-hat practice.
- Manufacturing brand mentions that look "natural" (so-called organic-looking mentions).
- Planting short phrases in threads so that AI brings up a particular brand during retrieval: this is exactly the technique researchers used in Principle 15.6 to prove the attack is feasible.
- Staged question-and-answer exchanges and mutual upvoting to push up comment scores.

### 5.3 The risks of manipulation

| Risk | Basis |
|---|---|
| **Accounts banned, content removed** | One practitioner observed that even without selling anything, contributing only professional opinions, participation in discussions is often banned, and appeals go unanswered. Community rules are becoming more conservative. |
| **Citation sources cut off** | The crawling/licensing relationships between platforms and AI vendors change. Around mid-August, ChatGPT's and Perplexity's citations of Reddit both fell sharply (Debates 2 and 3). A strategy built on a single platform can stop working within days. |
| **Moderator flagging means not being selected** | In Reddit Answers, comments pinned or flagged by moderators are almost never selected. |
| **Rewritten by AI, original meaning lost** | Even when selected, first-person experience is flattened into generalized advice (Principle 15.4); forum content in AIO is cited but little used (Principle 15.3). |
| **Defenders are targeting UGC poisoning** | Researchers have already pointed out that blocking UGC is an effective line of defense. If AI vendors adjust in this direction, practices that rely on manipulating community content will be hit first. This is an inference; there is no evidence yet that it has happened. |
| **Brand reputation risk** | Once a community sees through it, the negative discussion itself may become a source that AI cites. This is a practitioner concern, with no systematic evidence yet. |
| **Deleting a post does not stop it being cited** | Repeated tests on real AI search engines found that after a post was deleted, some platforms kept citing it for about 4 days. If you post the wrong content, you cannot count on deletion to take it back immediately. |

## 6. What to do

### 6.1 What you can do

| Practice | Evidence strength |
|---|---|
| **Measure first, then invest**: for your core questions, record the cited domains engine by engine and confirm whether social platforms are among them. Do not rely on generalized claims such as "AI loves citing Reddit most" | Repeated tests on real AI search engines found that source pools differ enormously between engines |
| **Plan separately by engine**: treat community strategy as "mainly acting on Google's AI products", unless your data show that other engines respond too | Real-engine audits + practitioners report from their own tests |
| **Plan separately by question type**: community content is more likely to be cited on reviews-and-opinions, specific task-type and brand-name queries, and less on category head terms | Practitioners' repeated, controlled tests + practitioners report from their own tests |
| **Participate in threads that are already cited and still open**: start from the list of threads the engines actually cite, and judge whether you have specific content to add | Practitioners report from their own tests; one practitioner observed that some of the cited threads had been removed or archived |
| **Write formally, specifically, in a form that can be used directly**: answer the question in the first two sentences, give specific numbers, cover both pros and cons | Audit of a real platform (limited to Reddit Answers, observational associations) + practitioners' tests. Note that this is for being selected by AI: simulation research shows that what AI considers a "popular answer" (more arguments, evidence, steps) is almost unrelated to human votes, and winning human votes in Q&A communities is a different goal |
| **Participate under your real identity and disclose your relationship** | One practitioner observed this; necessary for compliance |
| **On LinkedIn, prefer long-form articles under an individual's name over short posts on a brand page** | Practitioners report from their own tests + practitioners' repeated, controlled tests |
| **Measure "being cited" separately from "bringing visits/leads"** | One practitioner observed that the two are often decoupled; academic research also found citation and use to be inconsistent |
| **Track over multiple weeks, broken down by engine; do not rely on single results** | In practitioners' tests, large short-term swings followed by reversals occurred repeatedly |

### 6.2 Do not do

- Do not cultivate accounts, buy comments, or post brand recommendations in bulk.
- Do not plant brand phrases prepared for AI in threads.
- Do not promote in communities using only a brand account.
- Do not judge community influence only by "whether Reddit is in the citation panel": being cited is not the same as being used, and being used does not necessarily mean being cited.
- Do not average the numbers across all engines into a single "AI visibility" figure.
- Do not bet the whole budget on a single social platform; a platform's crawling policy can change within days.

### 6.3 Already outdated

- **"Reddit is the source AI cites most, so go all in on Reddit"**: at least for commercial questions in 2026, on ChatGPT, Claude, and Perplexity during some periods, this premise does not hold.
- **"Posting on Reddit can influence all AI engines"**: the source pools of the various engines are almost separate worlds.
- "Chasing community popularity is the same as chasing AI visibility": on LinkedIn, like counts are almost unrelated to being cited by AI.

## Key points

1. The weight of social platforms in AI search depends on **engine × question type × time**. Google's AI Overviews and AI Mode draw heavily on community sources; other engines cited Reddit very little during the study period, and Reddit did not appear at all in Claude search.
2. "Reddit is the source AI cites most" is a contested claim. On commercial questions, large-sample data show that Reddit accounts for only a small share, with most citations going to vendor documentation and product pages.
3. Around August 2026, ChatGPT's and Perplexity's citations of Reddit both fell sharply, but the scope, cause and persistence are disputed; Perplexity's change looks like contraction by question type.
4. Being cited is not the same as being used: forum sources in AI Overviews are cited a lot and used little; conversely, a great deal of content is used without being listed.
5. AI's selection layer inherits the community's visibility signals: it favors high-scoring, top-level, formal comments and rewrites first-person experience into generalized advice.
6. Large-scale experiments with real users show that AI Overviews boosted engagement in Reddit communities, with experience-based and small and mid-sized communities benefiting most; but the conversational AI Mode weakened this effect.
7. The claim that brand participation in communities raises AI visibility is currently supported only by practitioners' before-and-after comparisons, with no causal evidence; the successful cases all concentrate on specific, long-tail questions.
8. Editable UGC pages are a single point of attack, and manipulation is mechanistically feasible and hard to detect; but manipulation carries the risks of banned accounts, removed posts, sources being cut off and reputational backlash. Compliant participation (real identity, disclosed relationships, specific contributions) is the only sustainable approach.
