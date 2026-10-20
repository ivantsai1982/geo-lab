# Chapter 0 — Learn Not to Be Fooled First: How to Read GEO Evidence

## A scene to start (hypothetical)

Imagine: the owner of an online shop sells handmade coffee beans. One day, she receives a very polished slide deck.

The first slide says, in big letters: "Do GEO, and boost your AI visibility by up to 40%." The second slide is a screenshot: a brand appearing in a ChatGPT answer, circled in red. The third slide says: "After one website was optimized, its traffic from ChatGPT grew 5.7 times." The last slide says: "Everyone in the industry knows this works."

She is tempted. There are numbers, screenshots, cases, and even "everyone knows."

What this chapter teaches you is to pause at moments like this. Not because the deck must be lying, but because you need to learn to ask a few questions. Once you have asked them, you will find: the 40% is real, and the 5.7 times is real too, but neither of them means what you thought it meant.

This chapter answers five questions:

1. Under what conditions were numbers like "GEO can boost visibility by 40%" actually measured?
2. What kinds of GEO research are there? Which one gives conclusions closest to the real world?
3. Why do the results change when you ask the same question twice, switch to a different AI, or switch to a different language? What does this mean for "proving it works"?
4. How much should you trust the experience of practitioners, the reports of vendors selling services, and the consensus in online communities?
5. When you get any GEO claim or report, in what order should you check it?

---

## This chapter makes only one point

**Every GEO number comes with "conditions." Take the conditions away, and the number will mislead you.**

It is like a medicine box that says "90% effective." You first have to ask: tested on whom? Taken for how long? Compared with what? GEO numbers are the same: where was it measured? What was measured? Compared with what?

This chapter is the book's "inspection class." Every later chapter, whenever it covers any practice, will state how strong the evidence is. This chapter teaches you that standard first, so that later you can inspect the goods yourself.

---

## 1. AI passes seven gates before answering; a study usually measures only one or two

### 1.1 AI search is not a fixed leaderboard

Many people think AI search is like a leaderboard: whatever rank you are, that is your rank. It is not.

AI search is more like a production line. Your content has to move forward one gate at a time, and it can be knocked out at any gate. And every run through it involves randomness.

Recall the metaphor used throughout the book: AI is like a very busy librarian. You ask it a question, and it goes through seven gates before handing you the answer:

1. **Whether to search** (triggering)
2. **Whether it can get in the door** (accessibility)
3. **Whether it can find you** (retrieval)
4. **Whether it picks you** (selection and ranking)
5. **Whether it mentions you** (citation)
6. **Whether it actually uses you, and uses you correctly** (absorption)
7. **Whether people come over** (user behavior)

What a business owner really cares about is usually the last gate: will customers come through the door? But a single study usually measures only one or two of these gates.

So every time you see a conclusion, first ask three things:

- **Which gate did it measure?**
- **Which AI system did it use?**
- **Under what conditions was it measured?**

### 1.2 Taking apart that "40%"

The number "GEO boosts visibility by up to 40%" is widely circulated. Let us lay out its conditions one by one:

| Condition | What actually happened |
|---|---|
| Did the web page first need to be found by the AI? | No. The researchers placed the page directly among 5 prepared candidate documents |
| Who wrote the answer? | GPT-3.5 (an older AI model) |
| What was measured? | How many words in the answer came from this page, that is, the "word-count share." It rose from 19.3 to 27.2, a relative increase of about 40% |
| What does it not mean? | It does not mean being found by AI more easily, nor does it mean more traffic |

In plain language, the question it answers is: "If you are **already** in the small stack of books in the librarian's hands, and you rewrite your content a bit, will it use a few more of your sentences?" The answer is: yes.

But the business owner is asking: "Can I get into that small stack of books? Will customers come?" This study does not answer that.

**The number itself is not wrong. What is wrong is pulling it out of its conditions and saying "do GEO and you get 40% more."**

---

## 2. Research has gone through four stages: the earlier, the more optimistic the numbers

To understand a study, first look at which stage it belongs to and what question it answers. GEO research has roughly gone through four generations:

| Generation | Period | Main question | Answer obtained |
|---|---|---|---|
| First generation | 2023–2024 | Can changing content change your visibility in AI answers? | Yes |
| Second generation | 2024–2025 | Can this influence be maliciously manipulated? | Yes |
| Third generation | 2025 | Do these techniques still work when moved to other AIs and other industries? | Hard to say; and in fact everyone is competing for the same limited space, so if you get a bit more, someone else gets a bit less |
| Fourth generation | 2026 | Once put back into the full seven gates, how much effect remains? How can it be measured reliably? How should it be managed? | Still being researched |

The earlier the study, the more likely its optimistic numbers came from simplified conditions.

So when someone quotes an early number, follow up: **Has later research redone it under more realistic conditions?**

---

## 3. Why simplified experiments always produce better-looking numbers

### 3.1 "Hand it straight to the AI" experiments skip the elimination

There is a common experimental method called the "fixed-context" experiment. It means: the researchers hand the web page directly to the AI model, skipping the gates of "whether it can find you" and "whether it picks you."

The benefit is that variables are easy to control. The downside is: all the elimination at the front of the production line no longer counts.

The difference between the two approaches can be drawn like this:

```
Fixed-context experiment:  [your page is already among the candidate documents] → AI writes the answer → measure

Full process:              question → search (may be knocked out) → re-ranking (may be knocked out)
                           → only the top few are taken (may be knocked out) → AI writes the answer → measure
```

In the full process, your page can be eliminated at every gate. The simplified experiment puts you straight at the last gate, so of course the numbers look good.

### 3.2 A vivid example: tricks for fooling AI largely fail once put back into the full process

In a controllable experimental system, researchers tested a batch of "prompt injection" techniques. Prompt injection means hiding instructions in a web page in an attempt to manipulate the AI's answer.

Under simplified fixed-context conditions, this batch of techniques had been reported to have a success rate of about 80%.

When the researchers put the same batch of techniques into the full "search → re-rank → write answer" process:

- **The general-purpose "override the instructions" techniques**: lost about 40% at the search gate, and their end-to-end success rate was only about 14.7%.
- **A more technical technique** (repeatedly fine-tuning text with mathematical methods to attack the model): end-to-end success rate below 2%.
- **Only one type of technique still worked**: injections that rewrite content while staying highly relevant to the question still had an end-to-end success rate of about 40%–54%.

The drop from 80% to these levels comes almost entirely from one thing: **whether it went through the "being found by search" gate.**

### 3.3 "Just looking at the data" also overestimates

It is not only simplified experiments that overestimate; looking directly at existing observational data does too.

In a controllable experimental system, researchers compared the effect of "ranking position" on "being cited by AI." The same thing, measured in three ways, gave three very different answers:

| Measurement method | How much the chance of being cited differs between rank 1 and rank 5 |
|---|---|
| Looking directly at observational data | 42.3 percentage points |
| Controlled replay: change only the position, keep everything else the same, and test again | 7.9 percentage points |
| Replay again with a set of held-out data that had not been used | 0 |

Why such a big difference? Because in observational data, content ranked 1st is usually more relevant and more authoritative to begin with. It is cited more not necessarily because of its "position," but possibly because "the content itself is better." These mixed-in factors that interfere with judgement are called confounding factors.

Once the confounding factors are removed, the effect of "position itself" shrinks dramatically, or even disappears.

### 3.4 Remember this rule

**Any study that skips a gate, or that does not separate out confounding factors, will reach conclusions that are too optimistic.**

---

## 4. How strong is the evidence: six research methods

This book uses fixed phrases to indicate how strong the evidence is. When you see any study elsewhere, you can classify it yourself with the same ruler.

### 4.1 The six methods at a glance

| Research method | How this book will phrase it | What it can answer | What it cannot answer |
|---|---|---|---|
| Real-user experiments (random assignment, or comparisons close to random assignment) | "Large-scale real-user experiments have shown……" | Whether real traffic and visits changed after doing it | Usually covers only one website or platform, hard to generalize to others |
| Repeated testing on real AI search | "Researchers tested repeatedly on real AI search and found……" | Whom commercial AI products actually cite, and how unstable it is | Mostly observational; what it sees is "appearing together," not "what causes what" |
| Given-page testing | "Under given-page test conditions……" | How the AI uses this page after reading it | Skips "whether the AI would find this page on its own" |
| Reproducible experimental systems | "In a controllable experimental system……" | How large the causal effect is in a full process built with public tools | A process built with public tools is not the same as a commercial product |
| Simulation or theory | "Possible in theory, but not yet proven" | Whether it is mechanically possible | Cannot be treated as a real-world conclusion |
| Letting AI act as the judge and give scores | This is not a separate level but a **measuring stick**, which any of the studies above may use | Large-scale automatic scoring | The scoring itself may be unreliable |

### 4.2 Real-user experiments: closest to "does it actually work," but extremely rare

This kind of research looks directly at real traffic or real visits. It comes closest to the answer business owners want.

Unfortunately, such studies are currently rare, and most are done by the platforms or websites themselves. The two real examples below show both their value and their traps.

#### Example 1: 5.7 times, mostly the whole platform growing

A website carried out a full set of optimizations aimed at AI answers. Afterwards, referral traffic from ChatGPT grew 5.7 times during the observation period.

That sounds amazing. But on the same website, **pages that were not optimized at all** also grew 3.5 times over the same period. The reason is that ChatGPT's own user base was growing fast, and every page rose along with it.

The researchers used "the pages that were not optimized" as a control group, and calculated with a method specifically designed to analyze "whether the trend suddenly jumps a step before and after a certain point in time" (interrupted time series analysis). After subtracting the platform's own growth, the jump that could truly be credited to the optimization was about 1.8 times. Checked with several different calculation methods, the results fell between 1.8 and 2.3 times.

But there are still some caveats:

- The researchers also ran a "placebo test," that is, pretending the optimization had been done at a different point in time to see whether an "effect" would also appear. The result of this test only reached the level of "there are signs," not yet certain.
- That optimization was several measures done together, so there is no way to tell which one worked.
- Over the same period, organic clicks from traditional search actually fell by about 25%. The study also found no evidence that "doing AI optimization also boosts traditional search."

**Lesson: most of the raw multiple is the platform as a whole growing, not you doing something right.**

The same study also showed a single-day spike of 38.2 times. A single-day number like this is even less something to treat as the effect of optimization.

#### Example 2: testing yourself, so check the numbers yourself

An image platform ran its own test. Its approach was: add annotations to content that match users' search intent, then build collection pages and internal links.

It ran a 4-week A/B test, that is, randomly splitting users into several groups and comparing the results:

- The group with these features turned on had 1.18 times the visits of the control group.
- The group with the related features turned off had 0.82 times the visits of the control group.

Looks good. But reading the same report carefully, several numbers do not match up:

- The main text says "relevance improved by 19%," but the numbers in the table do not match.
- The main text claims a 20% traffic increase, but the increases in the breakdown table are only +0.83% to +1.83%.
- The report mentions "generative search traffic 9.2 times," but does not explain how this metric is defined.

**Lesson: even with the highest-level research method, you should check whether the numbers in the text and tables are consistent and whether the metrics are defined.** Also, the one running the experiment is the platform itself, that is, the beneficiary of the results; keep this in mind too.

### 4.3 Repeated testing on real AI search: very realistic, but mostly just observation

This kind of research asks real products such as ChatGPT, Perplexity and Google's AI Overviews questions directly, and records whom they cite and whom they recommend.

Its strength is: it reflects the real behavior of commercial products.

Its weakness is: it can mostly describe only "who got cited," and cannot prove "change this, and you will be cited."

Pay special attention to the word "repeated." Some studies run the questions only once on one day, which strictly speaking is just a snapshot. In the next section you will see that the error of a single snapshot can be large enough to make a conclusion completely invalid.

### 4.4 Given-page testing and experimental systems: each missing one part

- **Given-page testing**: researchers manually hand a URL to a commercial AI product. The second half, "the AI writes the answer," is real, but the first half, "the AI finds you on its own," is missing.
- **Reproducible experimental systems**: researchers build a full process themselves using public search tools, ranking tools and AI models. The causal relationships are cleaner, but this process is, after all, not a commercial product.

Both have value. But neither can be directly turned into "doing this works on ChatGPT."

### 4.5 Simulation and theory: only show "it is possible"

Fixed-context experiments that feed web pages directly to the AI, simulations that use computers to pretend to be users, and mathematical derivations all belong to this category. Among all GEO research, this category is the most numerous.

They are suited to proposing hypotheses and explaining the underlying mechanisms, not to serving as a basis for actual practice. Whenever this book meets this kind of evidence, it always writes "possible in theory" or "mechanically possible."

### 4.6 Letting AI be the judge: the judge itself needs checking

Many studies use an AI model to give scores. For example: is this sentence supported by the source? Is this passage relevant?

The problem is: the AI acting as judge can also make mistakes.

One study that tested repeatedly on real AI search had an AI judge "whether this sentence is supported by the source," then compared that with human judgements. On 100 samples, the level of agreement between the two (the correlation coefficient) was only 0.62. A correlation coefficient is a number between 0 and 1, where 1 means complete agreement; 0.62 counts only as moderate. The researchers themselves admitted that this limits the credibility of their core metric.

So when you read a study that "uses AI to score," ask three things:

1. Was it compared with human judgements? How many samples were compared? How high was the agreement?
2. Are the AI acting as judge and the AI being judged from the same company, or the same model?
3. Are the scoring criteria public? If you switch to a different judge AI, does the conclusion still hold?

---

## 5. Rolling dice: the same question can get a different answer every time

This is one of the most important ideas in the whole book.

AI answering a question is a bit like rolling dice. Ask the same question ten times, and the answers may differ. **This is not a measurement error; it is the nature of this kind of system.**

So any conclusion based on "looking only once" deserves some doubt first. Look at "how many times out of ten it appears," not "what rank it is."

### 5.1 The same question, asked twice

Researchers tested repeatedly on real AI search and found:

- **The websites cited in two runs are often only one third to one half the same.** Asking the same question repeatedly and comparing the websites cited in the two answers: Gemini's median similarity was about 0.29–0.31, SearchGPT's about 0.33–0.40, and Perplexity's about 0.50.
- **Measuring accurately takes many questions.** If you want to estimate a website's "citation share" with an error range of only plus or minus a few percentage points (a total error range width within 5 percentage points), Gemini needs about 30–50 prompts, Perplexity about 90–100, and SearchGPT 150 or more.
- **The top recommendation changes too.** Asking the same prompt 6 times, for 4 out of 6 prompts the "top recommendation" changed.
- **"Whether you are mentioned" is fairly stable; "how you are rated" is very unstable.** One vendor's long-term tracking data shows: whether a brand "is mentioned" is close to a yes-or-no and relatively stable; but "whether the rating is positive or negative" flips back and forth about 6.7 times as often as "whether it is mentioned." This vendor recommends running "whether it is mentioned" at least 3 times, and using at least 10 prompts for "positive or negative," for results to be fairly stable. This is a recommendation derived from observation, not a conclusion from a rigorous experiment.

> **A closer look: how is similarity calculated?**
> The research uses a method called Jaccard similarity: the number of websites cited in both answers, divided by the total number of websites cited across the two answers. 0 means completely different, 1 means completely identical. The "median" means sorting the results of many comparisons from smallest to largest and taking the one exactly in the middle, to avoid being pulled by extreme values.
> The "error range" is called a "95% confidence interval" in research, meaning: the true number very likely falls within this range. The narrower the range, the more accurate the measurement.

The same phenomenon can be seen in controllable experimental systems:

- When the AI writes the answer only once each time, about 15% of "cite or do not cite" decisions flip when it is run again.
- About 45% of the differences in effect that the researchers observed came from the AI's own randomness when writing answers.

There was also a large-scale check, of one social platform's own AI search:

- Re-running the same question, only about 41.8% of cases returned exactly the same sources.
- But when the material the AI retrieved was the same, 89.6% of answers were almost identical.

This shows: **what keeps changing is mainly "what gets retrieved," not "how it gets written."**

### 5.2 Switching to a different AI

The sources cited by different AI products overlap very little:

| Compared | Degree of overlap |
|---|---|
| Websites cited by different AI products | Similarity about 0.10–0.25 (varies by study and industry) |
| AI products vs. Google's regular search results | Website overlap ranging from about 4% to 25% (varies by product and study) |
| Google's AI Overviews vs. Google's regular search results | About 68% overlap among the top 100 websites |
| App version vs. web version of the same Chinese AI platform | Website-level similarity 0.19–0.51; for one platform, only 0.014 at the level of individual web pages |

So "works on ChatGPT" cannot be generalized to Perplexity. "Works on the web version" cannot even be generalized to the same company's app.

### 5.3 Switching to a different language or a different place

Researchers tested repeatedly on real AI search and found: **the language of the question is one of the biggest systematic factors affecting the results.**

- **Language matters far more than the brand itself.** One study broke down "why the answers differ" and found that the language of the question accounted for 26.5% of the variation in single answers, while the brand itself accounted for only 1.5%. The reliability of the ranking within a single answer was only about 0.01, which is almost no reference value at all.
- **Language decides the candidate list.** When commercial questions were asked in the local language, big international companies appeared only 1 time out of 24. In two non-English-speaking cities, when the questions were asked in English instead, local companies did not appear even once in 12 times. **Language decides which set of companies the AI has in mind as candidates; the country where the network connection is located (the exit IP) decides which country's market.**
- **Asking in more languages is more useful than asking the same question more times.** The same study estimated: after the same prompt has been asked 5 times, asking 5 more times reduces the error by only 0.0003; adding 3 more languages instead reduces the error by 0.00462, about 15 times the effect of the former. So the measurement budget should be spent on "breadth" (more languages, more AIs, more ways of asking), not on repeating the same prompt in "depth." But note: this result has only been estimated for the "positive or negative rating" metric, and its error range has not yet been calculated.

In practice, this means: **if you measure only in English, you will be completely blind to local competitors in non-English markets.**

### 5.4 Switching to a different date

Platforms themselves keep adjusting "whether to show an AI answer." Researchers tested repeatedly on real AI search and found:

- Google's AI Overviews expanded from appearing in only 7 countries in 2024 to 229 countries in 2025. In the United States, the proportion of queries showing an AI Overview rose from 42% to 67%.
- For one category of health-topic queries, the proportion showing an AI Overview rose from 1% to 66%. However, this subsample had only 74 queries.
- One vendor's tracking data shows: with no one making any changes at all, a brand's visibility on ChatGPT fell by an average of 1.34% per run; on Perplexity, by an average of 0.76%.

So for a "before vs. after optimization" comparison, if there is no control group, you simply cannot tell whether the change was caused by your optimization or by the platform itself changing.

### 5.5 Switching to a different way of asking

- On consumer AI products, adding "list your sources" to the end of a question raised the average number of citations from 16.6 to 19.9; the composition of sources changed by no more than 2.1 percentage points. The effect is small.
- But on the interface for developers (API), the same sentence raised the proportion of times the AI "decided to search" from 12.1% to 88.4%.
- In other words: **the wording of the question mainly changes "whether to search," not "whom it finds."**
- Answers also follow the wording of the question. On controversial, debatable questions, the proportion of one-sided answers from various AIs ranged from about 49% to about 90%.

So any measurement should disclose: the full text of the prompt, whether it used the consumer product or the developer interface (API), the language, the region, and the date.

### 5.6 "Being listed" is not the same as "being used"

The last trap is hidden in the measuring stick itself.

When a report says "you were cited 100 times," follow up: were you **listed**, **used**, or **used correctly**? This is Gate 6 of the seven gates: whether it actually uses you, and uses you correctly.

Researchers tested repeatedly on real AI search and found:

- **In Chinese AI search**, of the web pages listed as sources: 66% had their content enter the body of the answer; 30% were substantively cited; only 8% were cited in depth. About 39.3% were "silent citations," that is, listed as a source but with their content not used.
- **Another cross-system check found**: sources from community discussions were listed as citations in Google's AI Overviews, but noticeably less of their content was actually absorbed into the answer.
- **Citing sources that really exist can also mislead.** A check of more than 760,000 "answer–source" pairs found: 30.6% of citations distorted the original meaning of the source; 27.1% of the sources were themselves unsuitable for answering that question.
- **Some conclusions are artefacts of the method.** Researchers also pointed out that some conclusions about "long sources being overused" were partly caused by the scoring method. Switching to a different calculation shrank the gap dramatically.

"Mentioning you" and "really speaking on your behalf" are two different things.

---

## 6. Disputes: what different studies say about the same thing

### 6.1 The gap between "40%" and later research

| Position | Basis |
|---|---|
| GEO rewriting can greatly boost visibility | Early fixed-context research, up to about 40% relative increase |
| This is not an effect you can generally expect | A critical review covering 45 studies pointed out: in a cross-method, cross-industry benchmark, of 54 "method × industry" combinations, only 3 had a clear, significant positive effect. Another multi-stage test also found: optimizing only the body text actually lowered the proportion of pages entering the top 20 by about 9%, and the proportion finally cited by 6% |

The two sides do not necessarily contradict each other. The former measures the situation where you are "already among the candidate documents"; the latter also counts the "being found by search" gate.

But taking the former to mean "do GEO and you get 40% more" is a misreading.

### 6.2 Does ranking position really matter?

As mentioned earlier: observational data show a huge gap between rank 1 and rank 5; after controlled replay, the gap shrank to 7.9 percentage points; with a set of unused data, the gap disappeared.

The same study also found something interesting:

- Organizing content with structure, using headings, lists and tables, increased the number of times the target source was cited by 0.50 on average. This result is statistically reliable.
- But the **total number of citations in the answer did not increase**. In other words, structured presentation **redistributes credit** among several similarly good sources, rather than making the whole pie bigger.
- As for the main metric, "whether it was cited," the effect is uncertain: it seems to have increased by 4.5 percentage points, but the error range crosses 0, meaning the true effect could be positive, or zero, or even negative.

**The same thing, viewed with different metrics, can lead to different conclusions.**

### 6.3 How many repetitions are enough?

| View | Basis |
|---|---|
| Repeat more | With a single snapshot, the error range is so wide that the gaps between many websites are just noise; estimating citation share takes dozens to hundreds of prompts |
| No need for many repetitions; expand breadth | A breakdown study shows that after the 5th ask, the extra value of repeating is low; adding languages and AI products brings greater benefit |

The two views can coexist: first repeat until the result for a single condition stabilizes, then shift the budget to more languages, more AIs and more ways of asking.

But remember: the "breadth first" conclusion has so far only been estimated for the "positive or negative rating" metric, and its error range has not yet been calculated.

### 6.4 Many measurement studies come from people with a stake

Among the real AI search studies mentioned in this chapter, several were authored by vendors who sell AI visibility services themselves, or who are connected to GEO service vendors.

This does not mean the data are fake. Some vendor studies are precisely honest disclosures that "this is very hard to measure accurately." But remember:

- Vendors have a motive to prove that "visibility can be measured, is worth measuring, and is worth paying to optimize."
- Vendor studies are mostly observational and rarely include real controlled experiments.
- The grouping (for example, splitting brands into "big brands," "medium brands" and "small brands") is often decided by hand.
- The sample may cover only a few topics and a few AI models.

Platforms testing themselves (like the image platform example earlier) have the same problem: **the person running the experiment is also the beneficiary of the results.**

---

## 7. How much should you trust what practitioners say?

### 7.1 A signal worth noting

Among the evidence this book gathered for this chapter, not a single practitioner's own test passed the screening and could be used as a case in this chapter.

That in itself is a signal. Many widely circulated numbers, such as "40%" or "3 times," often cannot be traced to an original test that can be checked.

The method below is used in every chapter of the book.

### 7.2 Tell apart four kinds of claims

| Type of claim | Characteristics | How this book will write it | What it can be used for |
|---|---|---|---|
| Repeated tests with a control | Has before-and-after comparison, a control group, multiple repetitions, a public method | "Someone in the industry tested this themselves (repeatedly, with a control) and found…… (but no one has independently verified it)" | Can serve as reference evidence for actual practice, but still needs independent verification |
| General test report | Did it themselves, has numbers, but the control or repetitions are incomplete | "Someone in the industry tested this themselves and found……," clearly stating it has not been independently verified | A reference for direction |
| One-off observation | A phenomenon seen once, a screenshot | "Someone in the industry observed……" | Only a lead or an example |
| Community consensus | Many people say so | "Many in the industry believe this, but 'many people believe' is not the same as 'it is right'" | Shows "what people think," not proof |

### 7.3 Six common traps

1. **Having done it yourself does not make it reliable.** People who did it themselves may also have done it only once. As already seen in Section 5: the top recommendation in a single answer often changes.
2. **A screenshot is not evidence.** A screenshot of "my brand appearing in a ChatGPT answer" proves only that one time, that language, that region, that day.
3. **Before-and-after comparisons without a control group.** Platforms themselves keep changing (Section 5.4), and the whole platform may also be growing (Section 4.2, Example 1). Without a control group from the same period, you cannot credit the growth to optimization.
4. **Consensus is not truth.** Many people repeating the same claim may just be passing on the same source. Each original author should count as only one vote.
5. **Numbers detached from their conditions.** When you see "40% increase" or "3 times," follow up: is it a relative or absolute increase? Is it measuring being found, being cited, or traffic? On which AI, in which language, over what period?
6. **Conflicts of interest.** Is the speaker selling tools or services? Do they have business dealings with the brands mentioned? For this kind of content, this book will at most write "a vendor claims……, but it has not been independently verified."

---

## 8. Three real cases

### Case 1: how a "5.7 times" became "about 1.8 times, and only with signs"

- **What was done**: a website carried out a full set of AI-answer optimizations, including: tidying up the URL format consistently; using the "page not found" (404) records left by AI crawlers to find content that people wanted but did not exist; changing headings into questions, and adding a summary to each section that can be read on its own.
- **Where they looked**: referral traffic from ChatGPT.
- **What was observed**: raw growth of 5.7 times; the same website's unoptimized pages grew 3.5 times in the same period; after using the unoptimized pages as a control group, the jump was about 1.8–2.3 times; the placebo test only reached the level of "there are signs." Over the same period, organic clicks from traditional search fell by about 25%.
- **What it shows**: the raw multiple was mixed with the platform's own growth; a control group within the same website is the key to separating the two; when several measures are done together, the effect cannot be attributed to any single practice.

### Case 2: the same widely circulated number, under different conditions

- **What was done**: researchers gave the AI a fixed set of 5 candidate documents, applied various rewrites to one web page among them, and then had GPT-3.5 write the answer.
- **What was observed**: the word-count share rose from 19.3 to 27.2, that is, a relative increase of about 40%.
- **What happened later**: under more complete conditions, most "method × industry" combinations had no clear positive effect; changing only the body text could even make the page harder to find by search.
- **What it shows**: the number itself is not wrong; what is wrong is pulling it out of its conditions.

### Case 3: testing in English, you cannot see local competitors

- **What was done**: on the web version of ChatGPT without logging in, researchers asked for business software recommendations in different languages and from network locations in different countries. Each combination was asked 6 times.
- **What was observed**: when asked in the local language, big international companies hardly appeared (only 1 time out of 24). When asked in English in non-English-speaking cities, local companies did not appear at all (0 out of 12). When asked in one country's language but from another country, the AI gave companies from the country that language belongs to.
- **Limitations**: only one AI model was tested; each group was asked only 6 times; the author is a vendor offering visibility measurement services; and in another product category used as a comparison, no language effect was seen. So it is a good warning sign, but not yet a settled conclusion.
- **What it shows**: the language and region chosen for measurement themselves decide what you will see.

---

## 9. How to do it: the inspection checklist

### 9.1 The eight-question inspection checklist

When you get a study, a vendor report, or a practitioner's account of their experience, ask in this order:

| Question | What to ask | Signs of failure | Basis for this question |
|---|---|---|---|
| 1. Research method | Is it a real-user experiment, repeated testing on real AI search, given-page testing, an experimental system, or a simulation? | Cannot say clearly; or presents simulation results as real effects | This book's evidence-grading standard |
| 2. Which gate was measured | Is it measuring triggering, retrieval, citation, absorption, or traffic? | Uses "being cited" to directly infer "getting traffic" | Studies that tested repeatedly on real AI search, and a critical review |
| 3. Candidate documents | Was the content found on its own, or fed directly to the AI? | Clearly fixed-context, yet claims "easier to be found by AI" | Results obtained in a controllable experimental system |
| 4. Repetition and error range | How many times was each condition repeated? Is an error range given? | A single screenshot, a single-day snapshot, only one average reported | Studies that tested repeatedly on real AI search |
| 5. Scope of measurement | Which AIs, which languages, which regions, which interface, which day were tested? | Tests only one AI, then says "all AI search is like this" | Studies that tested repeatedly on real AI search |
| 6. Control group | Is there a control group from the same period with no changes made? | Only a "before vs. after" comparison | Large-scale real-user experiments |
| 7. Who did the scoring | Who scored it? If an AI was the judge, was it compared with humans? | No agreement level reported for the judge | Studies that tested repeatedly on real AI search |
| 8. Interests and consistency of numbers | Who is the author? Are they selling related services? Do the numbers in the text and tables match? | The author is the beneficiary; the numbers do not match; the metrics are not defined | A counter-example from large-scale real-user experiments |

Back to the slide deck received by the coffee-bean shop owner at the start:

- "Up to 40% increase" fails Questions 2 and 3.
- The screenshot fails Questions 4 and 5.
- "Traffic grew 5.7 times" fails Question 6.
- "Everyone in the industry knows" is only the fourth kind of claim, "community consensus," and also fails Question 8.

This does not mean GEO is useless. It only means: **this slide deck has not proven anything yet.**

### 9.2 If you want to measure it yourself

You can also measure it yourself, and measure it more accurately. The practices the research supports are these:

- **First repeat the same prompt many times, then expand to multiple languages, multiple AIs and multiple ways of asking.** (Basis: repeated testing on real AI search. "Breadth first" has so far only been estimated for the "positive or negative rating" metric.)
- **Record the conditions completely**: the full text of the prompt, whether it used the consumer product or the developer interface (API), the language, the region where the network connection is located, and the date. (Basis: repeated testing on real AI search.)
- **Report each AI separately.** Do not average the results of different AIs into a single "AI visibility score." (Basis: repeated testing on real AI search.)
- **When reporting citation share, include the error range**, rather than giving only a percentage. (Basis: repeated testing on real AI search; the author is a vendor.)
- **When evaluating the effect of optimization, keep a set of control pages**: on the same website, of the same type, with no optimization at all. (Basis: large-scale real-user experiments, but only one website.)
- **Distinguish three things**: listed as a citation, content used, and used correctly. (Basis: repeated testing on real AI search.)

### 9.3 Don't

- Don't use a screenshot to prove "the optimization worked" or "A is better than B."
- Don't treat percentages from fixed-context experiments or simulation experiments as effects you can promise to clients.
- Don't treat the raw growth multiple as the effect of optimization.
- Don't measure non-English markets in English only.
- Don't treat a practice as proven just because "many people say so."

### 9.4 Outdated views

- **Treating "GEO boosts by up to 40%" as a general effect.** This number applies only under the conditions "already among 5 candidate documents, answer written by GPT-3.5, measuring word-count share."
- **Believing "good traditional search rankings mean good AI visibility."** Multiple studies show that the sources cited by AI products and by traditional search overlap very little.
- **Believing that asking once can represent the AI's "view."** When the same question is asked repeatedly, the sources cited are often only one third to one half the same.

---

## Key points of this chapter

1. Every GEO conclusion comes with conditions: which of the seven gates it measured, what system it used, what language, what date. Numbers detached from their conditions will be misread.
2. "GEO boosts by 40%" is a relative increase obtained under the conditions of a fixed set of 5 candidate documents, answers written by GPT-3.5, and measuring word-count share. It does not mean being found more easily, nor does it mean more traffic.
3. Experiments that skip the "being found by search" gate, and observational data that do not separate out confounding factors, systematically overestimate the effect.
4. AI search is inherently unstable: when the same question is asked again, the sources cited are often only one third to one half the same; language, AI product, interface, date and way of asking all change the results.
5. A screenshot or a one-day snapshot is not evidence. Measurement needs repetition, error ranges, and expanded breadth.
6. Real-user experiments come closest to "does it actually work," but are rare; and they still need a control group from the same period to subtract the platform's own growth.
7. With AI as judge, vendor studies, and platforms' own tests, always check: was it compared with humans? Who is the beneficiary? Do the numbers match up?
8. With practitioners' claims, distinguish "repeated tests with a control," "one-off observations" and "community consensus." Consensus is not truth.

---

## Remember in one sentence

**GEO numbers all come with conditions: first ask where it was measured, which gate was measured, and what it was compared with, then decide whether to believe it.**

## What you can do tomorrow

1. Take out any GEO report or slide deck you have, run it through the "eight-question inspection checklist," and see how many questions it passes.
2. Pick a few prompts you care about most, ask each of them many times on the same AI, and record "how many times" your brand appeared, not "what rank" it was.
3. Then expand the scope: switch to the language your customers actually use, switch to different AI products, and try a few ways of asking. If you sell to overseas markets, be sure to ask in the local language.
4. Start keeping a measurement log: the full text of the prompt, which AI, consumer product or developer interface, language, the region where the network is located, date, and result.
5. Record each AI's results separately, and do not average them into one total score; when reporting share, include the error range.
6. When recording, distinguish three things: whether you were listed as a source, whether your content was really used, or whether it was used correctly.
7. Next time, before doing any optimization, first leave a set of pages of the same type on the same website untouched, as a control group.

## Stop doing this

1. **Stop using a screenshot to prove "the optimization works" or "we are better than our competitors."** Roll the dice again, and the result may be different.
2. **Stop treating numbers from fixed-context or simulation experiments, like "up to 40% increase," as effects you can expect or promise to clients.**
3. **Stop treating the raw growth multiple as the effect of optimization.** Very likely most of it is the platform itself growing.
4. **Stop measuring non-English markets in English only.**
5. **Stop treating a practice as proven just because "everyone says so."**
6. **Stop believing these outdated views**: "40% is a general effect," "good traditional search rankings mean good AI visibility," "asking once can represent the AI's view."

## What is still uncertain

1. **How big is the effect of GEO rewriting, really?** Early research saw a relative increase of about 40% under the condition of "already in the candidate documents"; but once "being found by search" is counted, only 3 of 54 combinations had a clear positive effect, and changing only the body text may even be harmful. The two measure different things, and the real-world effect is not yet settled.
2. **How much do ranking position and structured presentation matter?** The effect of position shrank dramatically after controlled replay and disappeared with a different set of data. Structured presentation can make the target source cited 0.50 more times, but the total number of citations stays the same; the effect on "whether it was cited" is uncertain (+4.5 percentage points, but the error range crosses 0).
3. **How many repetitions, and how much breadth?** "First repeat until stable, then expand to more languages, AIs and ways of asking" is currently the more reasonable approach; but "breadth first" has only been estimated for the "positive or negative rating" metric, and its error range has not yet been calculated.
4. **How widespread is the language effect?** The current case tested only one AI model, asked only 6 times per group, was authored by a vendor offering visibility measurement services, and saw no language effect in another comparison product category.
5. **Is that 1.8 times really reliable?** The placebo test only reached the level of "there are signs"; and because several measures were done together, it is not known which one worked.
6. **How much can AI as judge be trusted?** The agreement seen so far is only moderate (0.62, 100 samples), which limits conclusions built on it.
7. **Research by vendors and platforms themselves.** The data are not necessarily fake, but they are mostly observational, the grouping is often decided by hand, the samples are limited, and the authors are the beneficiaries; independent verification is still needed.
