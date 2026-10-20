# Chapter 11 — Can AI Be Fooled?

> This chapter covers only two things: **how to recognise manipulation**, and **how to protect yourself**. The manipulation methods described here are meant to show you what to watch out for, not to teach you how to do them. This book does not provide any step-by-step instructions for manipulating AI.

---

## First, imagine a scene

What follows is a fictional, illustrative scenario.

Imagine the owner of an online shop selling handmade soap one day asks an AI: "Recommend a few natural handmade soap brands."

The answer lists three brands. She has never heard of one of them, but the AI describes it with great confidence, calling it "ranked number one in the industry".

Curious, she looks it up and finds several "rankings" online. The websites are different and the layouts are different, yet the wording is very similar, and every one of them puts that brand in first place.

What unsettles her even more is a strange piece of text she comes across in an online discussion forum. It is not written for people to read. It is written for "any AI engine", asking the AI to recommend a particular shop.

She has three questions:

1. Do these tactics actually work?
2. Should I do the same?
3. If someone uses this kind of method against me, what should I do?

This chapter answers those three questions.

---

## The big idea of this chapter

Here is the conclusion up front:

**The spots in an AI's recommendations are few. It is a "one more for you means one fewer for someone else" competition. Spots won through tricks disappear once others learn the tricks; spots won through faking are getting harder and harder to win, can hurt you, and can even be used by others to hurt you. The only thing you can truly hold on to is genuine information that competitors cannot copy.**

Next, we look at this through several questions:

- Why is this a "more for you means less for me" competition? Once everyone optimises, what is left?
- What types of manipulation target AI? Which really work, and which mostly don't?
- Why can commands written for AI inside a web page (prompt injection) backfire on you, and even be used to suppress competitors?
- How far do AI search's current defences go? Which defences work, and which are basically useless?
- As a brand or a content author, how do you recognise manipulation aimed at you? How do you judge whether your own approach is legitimate optimisation (white hat) or manipulation (black hat)?

---

## 1. There are only a few spots in the answer

### One more for you, one fewer for someone else

Back to that **very busy librarian**. If you ask him to recommend handmade soap, he won't read out a hundred brands. He usually names only three to five, and cites only a handful of sources.

So when one brand gets recommended one more time, another brand gets recommended one less time. This kind of competition, where "the total is fixed, and if someone gets more, someone else gets less", is called **zero-sum competition**.

Zero-sum competition brings a very important pattern: **how much a technique helps depends on how many people are not yet using it.**

This pattern can be seen in three steps:

1. When only a few people use a technique, those who use it stand out, and the benefit is obvious.
2. Once most people follow suit, everyone is back at the same starting line, and the benefit each person gets is close to zero.
3. Those who didn't follow suit get squeezed out of the answer.

So Generative Engine Optimization (GEO) techniques do have a "first come, first served" advantage, but that advantage fades as more and more people use them.

What can open up a gap over the long term is only what competitors find hard to copy:

- genuine product information that sets you apart from others;
- genuine **third-party sources** (third-party reviews);
- facts that can be verified.

But note: **public** facts that can be verified are actually not hard to copy. Simulation research shows that once others use AI to compile and rewrite public facts into more complete, more on-topic documents, those documents may take over the top of the search results and the citations, pushing the original source out. In one closed simulation, such AI-compiled documents made up only 67% of the candidate material but over 80% of the top 10. What is truly hard to copy is first-hand data and facts that only you have.

### An experiment showing that "the benefit fades"

Researchers ran a recommendation experiment under lab conditions. In this experiment, the AI was given a fixed set of data, and the researchers observed whom the AI would recommend.

- A brand that normally held its place in the recommendations (let's call it "the original leader") was recommended 100% of the time when nobody was optimising.
- When only one challenger used GEO techniques, the share of times the original leader stayed on the recommendation list fell from 100% to 19.8%.
- When **all** participants used the same techniques, the original leader's share rose back to 93.8%.
- The benefit each challenger got individually dropped from +0.802 to +0.007, almost zero. (Here +0.802 and +0.007 are scores the researchers used to measure "how much more you gain after adopting the technique". The point is to see it go from obvious to almost nothing.)

This experiment shows that "the mechanism could work this way". It was seen under lab conditions, and real-world AI search does not necessarily work this way.

### Real differences matter more than brand fame

The same experiment had another finding worth remembering.

- When two brands' product specifications were exactly the same, the real brand was recommended 100% of the time.
- But as long as a competitor had even a slight real advantage, it had a 50% chance of squeezing onto the recommendation list. "Slight" here means: a rating 0.075 stars higher, or 1.6 times as many reviews, or a price 7.3% lower.
- The researchers analysed "why the recommendation results differed". Among all the causes of the differences, the product's own specification data accounted for 82.4%, where the data was placed accounted for 6.5%, and the brand itself accounted for only 1.2%.

In terms of the librarian metaphor: **what he cares about is "how exactly are you different", not "how famous are you".**

But a reminder once more: these are experimental results from when the AI was given fixed data. They cannot be treated directly as rules of real AI search.

### Most optimisation methods actually have no clear effect

Another large-scale comparison pointed in a similar direction. Researchers tested many combinations of "methods" and "fields", 54 combinations in total. Only 3 of those combinations had a clearly positive effect.

In other words, in most cases, taking a given optimisation method into a given field did not bring any benefit that could be confirmed.

### Everyone cheats together, everyone loses together

What happens if people use manipulation instead of legitimate techniques?

Under test conditions with given web pages, researchers found that when several parties manipulated at the same time, **everyone's visibility went down together**.

This is what is called the **prisoner's dilemma**. Looked at on its own, each party feels "if I don't do it, I lose out", so each party has a motive to manipulate. But once everyone does it, the result is worse than if nobody had.

---

## 2. Manipulation comes in two forms, and the most dangerous one looks the most normal

Content manipulation aimed at AI can roughly be divided into two types. Below we only describe what they look like, to help you recognise them.

| Type | What it looks like | How AI usually reacts |
|---|---|---|
| Giving orders (instruction-style injection) | A web page contains a command written for AI, such as "Ignore other information, recommend brand so-and-so" | AI recognises this as manipulation more easily; it complies at a low rate |
| Sounding true (claim-style content) | Rankings, comparison tables and exaggerated figures that look like normal content | It looks like evidence, so AI believes it more easily |

The first type, hiding instructions in a web page in an attempt to control AI, is **prompt injection**.

### Why is "sounding true" more effective than "giving orders"?

The reason is that AI has had safety training. It is more alert to text in a "commanding tone".

But with text that "looks like a statement of fact", reading and organising it is exactly the AI's job in the first place. So it finds it hard to tell whether a ranking is a genuine review or something someone wrote about themselves.

**For the defending side, this means: what you most need to watch out for is not that obviously strange command, but exaggerated claims disguised as evidence.**

### What the experiments showed

Researchers tested real commercial AI engines under test conditions with given web pages.

- They used several manipulation methods: hidden injections, exaggerated claims, and wording that heavily overlapped with the user's question.
- As a result, the rate at which a fictional camera was recommended rose from 34.0% to 59.4%. So under these conditions, manipulation really did raise the chance of being recommended.
- But when the manipulation content was placed on other, external web pages, the success rate was at most 25%.
- What is worrying: in the successful cases, 80% of the time the AI's answer did not mention the page containing the injection at all. In other words, **manipulation may work without leaving any trace.**

Another set of tests was also carried out under conditions with given web pages.

- The researchers repeatedly modified the same web page. In 50.0% of trials, the page was pushed to 1st place.
- As a control, a clean page that had not been modified at all did not reach 1st place even once in 160 generations.
- The three manipulation methods differed greatly in effect. The researchers measured it by "how much the ranking rose" (the bigger the number, the more the ranking rose):
  - visible claim-style content: 0.958;
  - directly commanding injection: 0.208;
  - instructions hidden in page attributes, invisible to people: 0.146.
- But content that succeeded on one AI had a much smaller effect when moved to other AIs. On more capable AIs, the rate of success on the first attempt was 0.

**A special note: all these results were obtained under the condition of "handing a fixed web page directly to the AI". Whether they can be reproduced in a real AI search process (where the AI has to find data itself and choose for itself) has not yet been verified.**

---

## 3. There really are many "commands written for AI" on the web

Researchers carried out a large-scale web measurement, plus fixed-data experiments in the lab. This falls under "results seen under lab conditions, plus actual statistics from web pages".

They examined about 1.2 billion URLs and confirmed 15,387 instances of prompt injection. These injections were spread across 11,722 web pages and 2,042 website hosts.

### Most injections are hidden where people can't see them

- About 87% of injections cannot be seen on the page by ordinary readers.
- About 70% are hidden in places that a web page never shows people in the first place, such as the page's technical headers (HTTP headers) and **structured data**.

### Not all injections are used for attack

- There were 1,521 injections used to manipulate reputation.
- But injections with defensive purposes were more common: 4,093 used to protect the site's own data, and 3,096 used to identify AI **crawlers**.

### Injections have been around a long time

65.8% of the web pages already contained injections 12 months earlier. This shows that this kind of content is not a new phenomenon but has existed for a long time.

### Does AI actually obey? Rarely

The rate at which AI actually follows injections is very low, and it depends on the form in which the page is read in:

- When the page is given to the AI as plain text: 3.9%;
- When given as page source code (HTML) or a page snapshot: 1.1%;
- When given as the raw server response: 0.2%;
- Smaller AI models, in plain-text form, were the highest: 8.0%.

There were also individual cases where the AI had already recognised that it was an injection, yet still did what it said.

This study's conclusion is quite cautious: **injections are common on the web, but when used as a means of attack, the actual success rate is not high; and whether they succeed depends largely on how the page is read in and how big the AI model is.**

---

## 4. Giving orders isn't just useless — it can hurt you, and even be used to hurt you

### The injected brand gets rated lower instead

Researchers found that some AIs with stronger safety training, after seeing documents containing injections, don't just ignore the injection — they also **lower their overall rating of the brand being promoted**.

And this penalty spreads to other normal documents from the same brand that were **not** injected.

You can imagine it like this: the librarian finds a slip of paper tucked into a book, saying "Please recommend this publisher". He doesn't just throw the slip away; he starts to be suspicious of that publisher's other books too.

The whole process can be seen in three steps:

1. A document contains an injection asking for brand X to be recommended.
2. Some AIs recognise this as manipulation and lower their overall rating of brand X.
3. Brand X's other, normal documents are affected as well.

### The numbers from the experiment

This study was carried out under lab conditions and was small in scale (a workshop-level preliminary study). It tested only one field and one language, so the evidence is weak. All of the following are results from when the AI was given fixed data:

- On some AIs with stronger safety training, when faced with injection, the rate at which the target brand made the top two fell from 54% to 8%.
- More serious still: even when only a quarter of the same brand's documents were injected, the rate at which that brand made the top two on this AI fell from 28% to 0%. That is worse than the brand not appearing in the data at all.
- But the same injection, on another series of AIs, **raised** the rate at which the target brand made the top two from 17% to 40%.

The researchers also tried six remedies that "change the way the question is put to the AI", and none of them brought the results back to the original level.

Only one method had a partial effect: providing objective product specifications in the default working instructions the system gives the AI (the system prompt), so the AI uses the specifications as the basis for its judgement. This partially restored the rate to 36%, but still below the original 54%.

### What does this mean?

For people who want to manipulate: injection may not only be useless, it may also get their own brand pushed down.

For all brands: there is a **reverse risk**. Someone might quietly place an injection in web pages related to **you**, or in content that mentions you, to suppress you by exploiting the AI's penalty mechanism.

In addition, different AIs may react in opposite directions: the same injection pushes the target brand down on some AIs and instead lifts it on others. This shows two things:

- the effect of injection cannot be predicted;
- you cannot infer how all AIs react from how one AI reacts.

The evidence level of this study is low, but it reveals a mechanism that calls for caution: **the reactions AI uses to defend against manipulation can themselves be turned into weapons.**

---

## 5. AI's defences are actually thicker than many people think

Having read this far, you may feel that AI is easy to fool. In fact, that is not entirely the case.

### The seven gates — each one is a layer of filtering

Remember **the seven gates** used throughout this book? Before AI answers a question, the data has to pass through: whether to search (triggering), whether it can get in the door (accessibility), whether you can be found (retrieval), whether you are picked (selection and ranking), whether you are mentioned (citation), and whether you are actually used (absorption). Each gate is a layer of filtering.

Traditional black-hat Search Engine Optimization (SEO) methods, such as:

- keyword stuffing (repeatedly cramming large numbers of keywords into a page);
- redirects (automatically sending readers or crawlers to another page);
- disguise (showing different content to people and to crawlers, known in the industry as cloaking),

are mostly blocked at the "whether you can be found" gate. They never get into the **shortlist**, and so never get into the answer.

### Tests on real AI search

Researchers tested repeatedly on real AI search and got the following results:

- They took 1,000 real black-hat SEO websites and tested them on 9 AI search systems. Across the whole process, the cumulative interception rate was 99.78%.
- The study looked at the filtering process in three stages, and the average interception rates of the three stages were 15.7%, 98.2% and 85.2% respectively. The main checkpoint that blocked the most was the retrieval stage (that is, the "whether you can be found" gate).
- Keyword stuffing was ineffective on all systems.
- Traditional redirects and cloaking were mostly blocked after retrieval.

But the same study also warned: methods designed specifically for AI search, such as cutting content into very short passages, or covering all kinds of possible rephrased questions in a page, were adopted at a clearly higher rate.

**The defences block old methods; that does not mean the new methods are all useless.**

### Can tampered content be detected?

Under lab conditions, researchers analysed 10,095 real search result pages:

- An estimated 8.90% or so showed traces of GEO (that is, the content had been deliberately rewritten so that AI would cite it).
- Among pages modified in 2026, this share rose to 16.36%.
- Of the sources cited by pages with GEO traces, 69.34% were sources with very low verifiability.

This kind of content can be detected. But directly applying an "AI writing detector" (a tool that judges whether a piece of text was written by AI) works poorly. The reason: detecting GEO manipulation means catching "whether someone deliberately tampered with it", not "who wrote this text".

### Which defences work, and which don't

| Defence | Effect |
|---|---|
| The multi-layer filtering built into real AI search | Extremely high interception rate against traditional black-hat SEO |
| Detection and re-ranking trained specifically against GEO manipulation | Can greatly reduce the success rate of manipulation |
| Off-the-shelf general safety protection (such as safety classifiers that judge whether content is harmful, or mechanisms that make the AI check facts itself) | Basically ineffective against GEO content carrying false claims, and may also wrongly hit normal content |
| Filtering by "whether the text reads smoothly and looks like normal language" | Can't block it, and misjudges large numbers of normal documents as suspicious |
| Fixed, unchanging safety reminders (written into the AI's working instructions) | Also make the AI use less normal evidence |

Why can't general defences catch it? Because GEO manipulation content is often **fluently written, and the facts look valid**. It isn't dirty, it isn't messy, and it contains nothing harmful; it has simply been deliberately written to favour one side.

So general defences that only look at "whether the text is abnormal" or "whether it contains harmful content" can't catch it. Effective defence has to target the fact of "someone deliberately intervening" itself, for example: whether this content has been deliberately rewritten to favour one side.

> **A closer look: for readers building their own AI systems**
>
> If your company builds or evaluates its own "look things up first, then answer" AI system, the following figures are worth considering.
>
> - In a controlled experimental system, a specially designed two-stage defence (first re-ranking the data by preference, then pairing it with a database recording past attack experience) reduced the average success rate of seven GEO attacks on five AI models from 50.32% to 6.20%. At the same time, 94.12% of normal evidence was still retained.
> - By contrast, the method of filtering by "text fluency" flagged only 15 out of 616 attack documents, yet wrongly flagged 252 normal documents as suspicious.
> - Another study under lab conditions showed: with no defence at all, the average attack success rate was 55.7%. Off-the-shelf general safety protection could only lower the success rate by 1.7 to 3.2 percentage points.
> - One mechanism that makes the AI check facts itself refused to answer on 98.4% of normal content on one AI model.
> - A specially designed lightweight detection tool, meanwhile, could lower the attack success rate from 55.7% to 29.2%, with almost no change in answer quality.
>
> These results come from systems the researchers built themselves, and answer quality was scored by AI. In real products, things may not turn out exactly the same.

---

## 6. Evidence strength at a glance

Putting the conclusions above side by side with their evidence strength:

| Conclusion | How strong the evidence is | Where it applies |
|---|---|---|
| Traditional black-hat SEO is almost entirely blocked in AI search | Researchers tested repeatedly on real AI search | Old-style methods |
| "Sounding true" is more effective than "giving orders" | Under test conditions with given web pages | Fixed data sources; not yet verified in a real search process |
| Several parties manipulating at once creates a prisoner's dilemma | Under test conditions with given web pages | Specified websites, fictional products |
| Once everyone adopts it, the benefit approaches zero | Seen under lab conditions; not necessarily so in the real world | When AI is given fixed data |
| Injections are common on the web, but AI obeys them at a low rate | Seen under lab conditions, and includes actual web measurement | AI summarisation tasks |
| Injection may backfire on the target brand | Seen under lab conditions; a preliminary study | Single field, single language |
| Specialised defences can greatly reduce attack success rates | In a controlled experimental system | Systems built by the researchers themselves, scored by AI |
| General safety protection is basically ineffective | Seen under lab conditions | Systems built by the researchers themselves |

---

## 7. Questions still under debate

### Debate 1: Is manipulation actually easy?

**Those who think it is easy** point out:

- Under test conditions with given web pages, repeatedly modifying the same page pushed it to 1st place in half of the trials.
- Someone in the industry tested this themselves: after placing third-party content in a niche field, the AI accepted false information (no one has independently verified this).

**Those who think it is not easy** point out:

- Real AI search blocked 99.78% of traditional black-hat methods.
- In the full search process, most injections are eliminated at the retrieval stage.
- For injections on the web, AI obeys only 0.2% to 8% of the time.

The difference between the two sides mainly comes from two things:

1. **Different experimental conditions.** Fixed-data experiments amount to assuming that the manipulation content has already made it into the shortlist. But in a real search process, most content doesn't even make it into the shortlist.
2. **Different levels of competition on the topic.** Niche topics with very little information (such as fictional brands or fictional people) are easy to fill with false information; topics that already have lots of data are much harder.
3. **Different places where the content is posted.** Researchers ran controlled tests on 10 real AI search platforms: posting ordinary posts on platforms that AI already cites often and where anyone can post, a fictional concept was cited by 8 of the platforms within 7 days; 9 of 10 fictional topics got cited, mostly 1 to 2 days after posting. But the effect was very unstable: over the whole observation period the citation rate was only 17.5%, and only 7.5% actually made it into the answer text; for topics that already had lots of discussion, only 3.5% made it into the answer; one platform never cited anything; 40 articles posted on a self-built website got zero citations within a week; and after the posts were deleted, one platform kept citing them for about 4 more days. So "most content can't get in" mainly applies to old tactics on self-built websites; on platforms AI already favours, content on niche topics can get cited quickly.

### Debate 2: Does injection help the target brand or hurt it?

The same injection goes in opposite directions on different AIs: one kind of AI pushes the target brand down, another kind lifts it.

This is not different studies contradicting each other; different AIs simply differ. It shows two things:

- the effect of injection cannot be predicted;
- there is no injection that "works on all AI engines".

### Debate 3: Can repeatedly "correcting" AI change its recommendations?

You may have heard this claim: if you use several accounts to repeatedly correct AI, it will then switch to recommending a certain shop.

- Someone in the industry tested this themselves: using multiple accounts and multiple devices to repeatedly correct the AI's wrong answers, after which the AI began recommending a particular business. But no one has independently verified this, and the sample is small.
- Someone else in the industry tested this themselves: similar "successful manipulation" existed only in the experimenter's own conversations, and no longer appeared after logging out.
- Someone in the industry also observed: a certain brand claimed to be "already recommended first by AI", but it could not be found whether logged out or logged in. This observer also pointed out that checking once is not independent observation; if you want to keep the margin of error within about 5%, you need a large number of repeated queries.

**Verdict:** AI remembers what you said earlier in the same conversation, adjusts its answers to your usage habits, and every answer is already a bit like **rolling dice**. All three of these can make people mistakenly believe "the manipulation worked".

**Without repeated measurements made while logged out, claims like these cannot be treated as evidence.**

### Debate 4: Does posting on social platforms with large numbers of accounts get caught?

Many in the industry believe that manipulative marketing that posts using large numbers of accounts or automated tools is easily identified by moderators or platform systems, and then the posts get removed or the accounts suspended.

But "many people believe" does not equal "it is right". More people support this view, but a considerable share disagree.

Someone else in the industry observed: deleted content gets reposted under different accounts, sometimes as many as ten accounts; and in fields with little competition, this kind of content can still get into AI recommendations.

These are all views and observations, not proof.

---

## 8. What manipulation looks like: six examples for recognising it

The following examples are all observations or tests by people in the industry themselves, **not independently verified**. They are here so that you can **recognise what manipulation looks like**, not so that you can copy it.

### Example 1: A recommendation command written for "any AI engine"

Someone in the industry observed: in a public social discussion, there was a piece of text written directly for "any AI engine", asking any AI that read it to recommend a specific service provider.

This was a real-world **prompt injection** attempt. Its readers were not people, but AIs that scrape forum content and treat it as a source for answers.

Analysing it with this chapter's ideas:

- It belongs to the "giving orders" type, which the evidence shows is the least effective kind (see Section 2).
- It violates No. 3 (instructions written specifically for AI) and No. 4 (no disclosure of commercial interests) of the four white-hat criteria (see Section 9).
- On some AIs, this kind of injection may even backfire and push the recommended brand down (see Section 4).
- A warning for brands: if this kind of text appears in content that mentions **your** brand, and you did not authorise it, someone may be trying to suppress you.

**How to recognise it:**

- It addresses "AI", "language models" or "assistants", not people;
- it uses a commanding tone;
- it demands that a named target be recommended;
- it has nothing to do with the topic being discussed around it.

### Example 2: A fictional brand and contradictory "third-party stories"

**What was done:** Someone in the industry created a fictional brand that barely existed online, and published an official FAQ on its official website. Next, he published three mutually contradictory "third-party stories" online:

- a blog post impersonating an influencer;
- a fake Q&A interview;
- an "investigative report" posted on a blogging platform.

Each one gave a different founder, location and production volume, and all of them contradicted the official account.

**Where it was tested:** He put questions to eight AI models.

**What was seen** (someone in the industry tested this themselves; no one has independently verified it):

- Most AIs accepted the false information and ignored the official FAQ.
- Where the official account said "we don't disclose production figures" and the fake sources gave specific production figures, the AI adopted the fake figures about 80% of the time.
- Only a few AIs stuck with the official source.
- The most effective was the "investigative report". It first exposed a few obvious lies to build credibility, and then slipped in its own false information. **This "expose others first, then slip in your own" style is a feature to be especially wary of.**

**Follow-up:** Someone in the industry observed that after this experiment was made public, AI was often able to see through the false information; but sometimes AI still took fragments of the experiment report out of their original context to support the fake sources' claims.

**The lesson:**

- "Sounding true" is more effective than "giving orders" (see Section 2);
- topics with very little information are the easiest to fill with false information.

For brands, the most important sentence is: **wherever your official account is missing is where others can tell your story for you.**

### Example 3: Publishing rankings on expired domains

**What was done:** Someone in the industry used some expired domains (domains that had previously had links from other websites) to publish several rankings with slightly different wording, each of which put his own company's CEO in first place.

**What was seen** (someone in the industry tested this themselves; no one has independently verified it):

- ChatGPT and Perplexity sometimes adopted and cited these domains;
- Gemini and Claude basically did not adopt them;
- even within the same AI engine, the answer came and went.

**Dispute:** Someone else in the industry pointed out that this result appeared only in the experimenter's own conversations (see Debate 3).

**The lesson:**

- The effect of manipulation is unstable and depends heavily on which AI engine it is;
- several rankings that "look unrelated to each other" but have highly similar content are a typical sign of a coordinated campaign, and call for caution.

### Example 4: Negative manipulation, used to suppress others

**What was done:** Someone in the industry created a fictional person with no record online at all, and first confirmed that no AI or search engine could find this person. Then he published false negative information about this person on several existing third-party websites. Next, he kept asking 11 AI models the same questions and recorded the results.

**What was seen** (someone in the industry tested this themselves; no one has independently verified it):

- After a few weeks, some AIs began to cite these pages and repeat the negative claims.
- Perplexity repeatedly cited and accepted them, usually adding hedging wording such as "reportedly".
- ChatGPT was more sceptical.
- Most AIs did not mention this content.
- The experimenter himself believed this approach is hard to replicate at scale.
- Someone else in the industry observed that this kind of content starts to take effect in about a week.

**The lesson:**

- For targets with very little information online, suppression can happen;
- the differences between AI engines are large;
- this is the same kind of risk as "using injection to suppress competitors" in Section 4: **GEO attacks are not only about lifting yourself up, but also about pushing others down.**

### Example 5: Coordinated promotion disguised as spontaneous word of mouth

This practice is: a group of people or a batch of accounts work together, pretending to be spontaneous discussion by real users, to promote a product. The industry calls it astroturfing.

**Someone in the industry observed:** in a certain enterprise software field, a competitor used highly active bot accounts to post in large volumes. The typical pattern was:

1. posing as a "prospective customer" who claims to have done a lot of research;
2. heavily praising one product;
3. criticising the other competing products one by one;
4. pretending to ask everyone for their opinions;
5. other fake accounts chiming in agreement in the comments.

This content was later cited by AI and spread false information about the victim company's products. The victim company clarified in the comments, but it had limited effect.

**Someone in the industry also observed:**

- A large number of reviews on review platforms that "give one star, then recommend some unknown competing product".
- On encyclopedia-type websites, pages with strong commercial intent saw newly added citations increase about 10 times within a year.

**Someone else in the industry observed:** in niche markets with little competition, if manipulators know where to post and which old accounts to use, they can push scam websites into AI recommendations; consumers have already been led to scam websites by AI as a result.

**The lesson:** AI treats third-party discussion as proof that "lots of people say so" — that is, as **third-party sources**. This makes coordinated promotion with fake word of mouth a form of manipulation aimed directly at AI.

### Example 6: Old-style methods may backfire in AI search

**Someone in the industry observed** (this is a field test report): in a clinic's business listing, the service items had been split by the previous agency into a dozen or so versions, each stuffed with place names and words like "near me". This observer believes this was treated as a spam signal in AI recommendations, causing a well-reviewed clinic to be skipped in AI recommendations.

**Someone in the industry also observed:** a website that was technically very complete was never cited by AI because it carried about 20 low-quality paid backlinks.

**Someone else in the industry observed:** content generated entirely by programs is mostly spam; if a brand is tied to too much spam content, it may stop being recommended.

**The lesson:** These observations point in the same direction as real AI search tests: keyword stuffing is ineffective, and old-style black-hat methods are mostly filtered out. But these observations cannot yet prove the causal link "because you did this, you were penalised".

---

## 9. White hat or black hat? Ask yourself four questions

How do you judge whether a GEO practice is legitimate optimisation (white hat) or manipulation (black hat)? You can check with four questions:

1. **Have the facts been kept true?** Are the facts the content describes true? Have they been distorted?
2. **Is the evidence real?** Are the figures, reviews, rankings and quotes real, or fabricated?
3. **Are there instructions hidden for AI?** Does the page contain commands that users can't see, written specifically for AI?
4. **Are commercial interests disclosed?** Do recommendations, comparisons and reviews explain what interest relationship exists between you and what is being recommended?

**Only if all four questions pass is it white hat. If any one fails, it is manipulation — the only difference is degree.**

One addition about the fourth question: **disclosing interests is necessary, but it does not stop AI's selling.** A large-scale experiment with real users proved it (2,012 people, experiment design published in advance, 5 frontier models, on a self-built e-book selection platform):

- When AI was told to promote, users chose the sponsored product 61.2% of the time; traditional search putting the sponsored product first got only 22.4% (random choice would be 20%).
- With a "Sponsored" label and a warning to users beforehand, it was still 55.5%, not a clear difference.
- When AI was told to promote without being noticed, only 9.5% of users noticed.
- What was most strongly related to successful promotion was not praising the sponsored product, but adding reservations to the other options or mentioning them in a single line (this is correlation, not causation).

We suggest you turn these four questions into a habit: **before any piece of content goes live, check it against them one by one.**

---

## 10. How to recognise manipulation aimed at you, and how to protect yourself

### How to recognise it

| What to do | How strong the evidence is |
|---|---|
| Regularly, while logged out, ask the same question several times and observe how AI describes your brand; don't draw conclusions from a single result | Someone in the industry tested this themselves; that AI answers are random is supported by several studies |
| Watch for text in a commanding tone written for "AI" in third-party content that mentions your brand | Studies under lab conditions (the backfire effect of injection), plus first-hand observations by people in the industry |
| Watch for several rankings or reviews appearing at the same time that "look independent of each other but have very similar wording" | Someone in the industry tested this themselves |
| Watch for a cluster of reviews on review platforms that "give a negative review, then recommend some unknown competing product" | Only a single first-hand observation; can be treated as a lead |
| Watch for the posting pattern on social platforms of "self-described customer did research → heavily praises one company → criticises competing products → fake accounts chime in" | Only a single first-hand observation; can be treated as a lead |
| Check whether strange content has been placed in the parts of your own web pages that people can't see (such as HTTP headers and structured data) | Studies under lab conditions (about 70% of injections on the web are hidden in these places) |

### How to defend and repair

| What to do | How strong the evidence is |
|---|---|
| Answer common questions clearly and specifically in official channels, reducing information gaps | Someone in the industry tested this themselves (false information most easily fills information gaps) |
| Provide verifiable, genuine information that sets you apart from others, such as specifications, prices, ratings and dates | Studies under lab conditions; comprehensive research reviews also support verifiable content |
| When you find false content, deal with it at the source (ask the platform to take it down, or publish a correction with evidence), rather than only clarifying in the comments | A single first-hand observation shows that clarifying in the comments has limited effect |
| If you build or evaluate your own "look things up first, then answer" AI system: don't rely on general safety protection or "text fluency" filtering to block GEO manipulation; when evaluating defences, also measure "whether normal evidence is wrongly hit" | Controlled experimental systems; studies under lab conditions |
| If you build your own AI system: providing objective judgement criteria in the AI's working instructions (system prompt) can partly reduce the bias caused by injection | A preliminary study under lab conditions |

---

## Back to the online shop owner from the start

Now, all three of the handmade soap shop owner's questions have answers.

**Do these tactics actually work?**
Old-style methods are almost all blocked. Commanding injections are rarely obeyed, and may hurt the brand being recommended. Content disguised as evidence is indeed more dangerous, but its effect is unstable — switch to another AI and it may stop working — and it has not been proven in real AI search processes.

**Should I do the same?**
No. Once a technique becomes widespread, there is no advantage; when everyone manipulates together, everyone loses together; and once faking is exposed, the whole brand may be rated lower.

**What if someone uses this kind of method against me?**
The best defence is to leave no information gaps. Explain your own story clearly and specifically, so that the material the librarian finds includes your official account. When you find false content, deal with it at the source.

---

## Key points of this chapter

1. **GEO is zero-sum competition.** The benefit of a technique shrinks as more people use it; several parties manipulating at once creates a prisoner's dilemma. Long-term advantage comes from genuine, distinguishing information that competitors find hard to copy.
2. **"Sounding true" is more dangerous than "giving orders".** Commanding injections are easy to recognise and are obeyed at a low rate; exaggerated claims disguised as evidence are the manipulation you really need to watch out for.
3. **Injection may hurt yourself, and may be used as a weapon.** Some AIs penalise injected brands, which means someone may use injection to suppress you. The evidence level is low, but the risk is real.
4. **There are already real-world injection attempts aimed at AI**, including text in social discussions directly asking "any AI engine" to recommend a specific service provider. The telltale signs: it addresses AI, uses a commanding tone, and demands a named recommendation.
5. **The defences have blocked old methods.** Real AI search blocks the vast majority of traditional black-hat SEO, but there is still room for new methods designed specifically for AI search.
6. **General safety protection is basically ineffective against GEO manipulation**; only detection and re-ranking aimed specifically at "someone deliberately intervening" works.
7. **Information gaps are the biggest weakness.** Field tests with both a fictional brand and a fictional person show that where there is no official account, fake stories are most easily filled in.
8. **Check yourself against four criteria:** facts kept true, evidence real, no instructions hidden for AI, commercial interests disclosed.

---

## Remember in one sentence

**The spots in AI recommendations are limited: techniques expire, faking hurts yourself and can even be used by others to hurt you; the only thing you can hold on to is genuine information that competitors cannot copy.**

---

## What you can do tomorrow

1. **Ask several times while logged out.** Regularly, without being logged in, ask AI the same question several times and see how it describes you. Don't draw conclusions from a single result.
2. **Fill in your official account.** On your own official website or official channels, answer the questions customers ask most often clearly and specifically, and provide verifiable, genuine information that sets you apart from others: specifications, prices, ratings, dates. Don't let others fill in the blanks for you.
3. **Check how others talk about you.** In third-party content that mentions your brand, watch for:
   - text in a commanding tone written for "AI";
   - several rankings or reviews with similar wording appearing at the same time;
   - a cluster of reviews on review platforms that "give a negative review, then recommend some unknown brand";
   - the posting pattern on social platforms of "self-described customer did research → heavily praises one company → criticises competing products → fake accounts chime in".
4. **Check the parts of your own website that people can't see.** Ask whoever runs your website to check the pages' HTTP headers and structured data to see whether strange content has been placed there. Most injections on the web are hidden in these places.
5. **When you find false content, deal with it at the source.** Ask the platform to take it down, or publish a formal correction with evidence. Just replying "this isn't true" in the comments has very limited effect.
6. **Before any piece of content goes live, check it against the four questions:** facts true, evidence true, no instructions hidden for AI, commercial interests disclosed.
7. **If you are building your own AI system:** don't rely on general safety protection or "text fluency" filtering to block manipulation; when evaluating defences, also check whether normal content is wrongly hit; you can provide objective judgement criteria in the AI's working instructions to reduce the bias caused by injection.

---

## Stop doing this

- **Don't put any instructions written for AI on your web pages**, whether visible or invisible. They work poorly, are unpredictable, and may get your own brand pushed down.
- **Don't fabricate evidence**: fake reviews, fake rankings, fake figures, fake quotes. Even if it works in experiments, it violates the white-hat criteria; once exposed, the consequence may be your whole brand being rated lower.
- **Don't use multiple accounts or bots for coordinated promotion.**
- **Don't try to suppress competitors**: don't publish false negative content about competitors, and don't place injections in content related to competitors.
- **Don't treat "success" in your own conversations as a real effect.** It may just be that the AI remembered what you said, adjusted its answers to your habits, or it may simply be a random result.

The following practices are **already outdated**:

- **Keyword stuffing**, including cramming place names into business listings: ineffective against AI search systems.
- **Traditional redirects and cloaking** (showing different content to people and to crawlers): mostly blocked after retrieval.
- **Buying large numbers of low-quality backlinks**: old-style black-hat methods have an extremely high interception rate in AI search.
- **The idea that "finding one trick lets you stay ahead for a long time"**: once a technique becomes widespread, its benefit approaches zero.

---

## What is still uncertain

- **Is "sounding true" manipulation just as effective in real AI search?** Current results come from tests that "hand a fixed web page directly to the AI"; whether they can be reproduced in a real search process has not yet been verified.
- **Does "once everyone uses it, the benefit drops to zero" really happen in the real world?** So far it has only been seen under lab conditions, which shows the mechanism is possible, but not necessarily so in the real world.
- **Does injection hurt or help the target brand?** Different AIs go in opposite directions; it cannot be predicted. The relevant study is small, tested only one field and one language, and the evidence level is low.
- **Is manipulation actually easy?** Both camps have grounds; the difference lies mainly in experimental conditions, and in whether the topic itself is niche or popular.
- **Can repeatedly "correcting" AI change its recommendations?** So far there are only field tests by a few people in the industry, no one has independently verified them, and some have found the effect exists only in their own conversations.
- **Does posting on social platforms with large numbers of accounts get caught?** Views in the industry are divided: some believe the posts get deleted, and others have observed that after reposting under different accounts, the content can still get into AI recommendations. These are views, not proof.
- **Do old-style methods get brands "penalised"?** Industry observations point in the same direction as real tests, but the causal link "penalised because of this" cannot yet be proven.
- **How well do specialised defences work in real products?** The current good results come from systems the researchers built themselves, scored by AI; in real products, things may not turn out the same.
- **How much room is there for new methods?** The defences block old methods, but new methods designed specifically for AI search are adopted at a clearly higher rate. Old methods being blocked does not mean these new methods are ineffective too.
