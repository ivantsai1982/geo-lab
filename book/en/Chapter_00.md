# Chapter 0: Learn Not to Be Fooled First: How to Read GEO Evidence

## A scene to start (hypothetical)

Imagine the owner of an online shop that sells handmade coffee beans. One day she receives a very polished slide deck. The first slide says, in big letters: "Do GEO, and boost your AI visibility by up to 40%." The second slide is a screenshot of a brand appearing in a ChatGPT answer, circled in red. The third slide says: "After one website was optimised, its traffic from ChatGPT grew 5.7 times." The last slide has only one sentence: "Everyone in the industry knows this definitely works." There are numbers, a screenshot, a case, and even "everyone knows". She is tempted.

What this chapter teaches you is to pause at moments like this. The deck is not necessarily lying, but you need to learn to ask a few questions. Once you have asked them, you will find that the 40% is real, and the 5.7 times is real too. Neither of them, though, is about what you thought it was about.

This chapter answers five questions in turn. First, under what conditions were numbers like "GEO can boost visibility by 40%" actually measured? Second, what approaches does GEO research take, and which one gives conclusions closest to the real world? Third, why do the results change when you ask the same question twice, switch to a different AI or switch to a different language, and what does this mean for "proving it works"? Fourth, how far should you trust the experience of people in the industry, the reports of vendors selling services, and the consensus in online communities? Fifth, when you get any GEO claim or report, in what order should you check it?

## The big idea of this chapter

**Every GEO number comes with "conditions". Take the conditions away, and the number will mislead people.**

It works the same way as "90% effective" printed on a medicine box. You first need to know who it was tested on, how long they took it and what it was compared with before you know whether that 90% means anything for you. GEO numbers are the same: first work out where it was measured, what was measured and what it was compared with.

This chapter is the book's "inspection class". Every later chapter, whenever it covers any practice, will state how strong the evidence is. This chapter hands you that standard first, so that later you can inspect the goods yourself.

## 1. AI passes seven gates before answering, and a study usually measures only one or two

Many people think AI search is like a leaderboard: whatever rank you hold, that is your rank. In reality it is more like a production line. Your content has to move forward one gate at a time, it can be knocked out at any gate, and every run through it involves randomness.

Recall the metaphor used throughout the book: AI is like a very busy librarian. You ask it a question, and it goes through seven gates before handing you the answer. First it decides whether to search (triggering). Then come whether it can get in the door (accessibility), whether it can find you (retrieval), whether it picks you (selection and ranking), whether it mentions you (citation), and whether it actually uses you and uses you correctly (absorption). Only at the end comes whether people come over (user behavior). What a business owner really cares about is usually the last gate, that is, whether customers will come through the door. But a single study usually measures only one or two of these gates.

So every time you see a conclusion, first ask three things: which gate did it measure, which AI system did it use, and under what conditions was it measured?

The number "GEO boosts visibility by up to 40%" is widely circulated, which makes it good for practice. Let us lay out its conditions one by one. In that study, the web page did not first need to be found by AI; the researchers placed it directly among 5 prepared candidate documents. The answer was written by GPT-3.5, an older AI model. What was measured was how many words in the answer came from this page, the "word-count share", which rose from 19.3 to 27.2, a relative increase of about 40%. This number does not mean the page becomes easier for AI to find, and it does not mean more traffic either.

In plain language, the question it answers is this: if you are already in the small stack of books in the librarian's hands and you rewrite your content a little, will the librarian use a few more of your sentences? The answer is yes. But the business owner wants to know something else, namely whether she can get into that small stack of books and whether customers will come, and this study does not answer that.

**The number itself is not wrong. What is wrong is pulling it out of its conditions and saying "do GEO and you get 40% more".**

## 2. Research has gone through four stages: the earlier, the more optimistic the numbers

To understand a study, first look at which stage it belongs to and what question it is answering. GEO research has gone through roughly four generations.

The first generation appeared in 2023–2024 and asked whether changing content could change your visibility in AI answers. The answer was yes. The second generation, in 2024–2025, asked whether this influence could be maliciously manipulated, and the answer was again yes. The third generation, in 2025, asked whether these techniques still worked when moved to other AIs and other industries. This time the answer was that it is hard, and researchers found that everyone is in fact competing for the same limited space: if you get a bit more, someone else gets a bit less. In the fourth generation, in 2026, the questions became: once everything is put back into the full seven gates, how much effect remains, how can it be measured reliably, and how should it be managed? These questions are still being researched.

The order itself reveals something. The earlier the study, the more likely it produced optimistic numbers under simplified conditions. So when someone quotes an early number, follow up with one question: **has later research redone it under more realistic conditions?**

## 3. Why simplified experiments always produce better-looking numbers

There is a common experimental method called the "fixed-context" experiment. Researchers hand the web page straight to the AI model, skipping gates such as "can it find you" and "does it pick you". This makes variables easy to control, but the price is that none of the elimination at the front of the production line counts any more. The difference between the two approaches can be drawn like this:

```
Fixed-context experiment:  [Your page is already among the candidates] → AI writes the answer → Measure

Full process:              Question → Search (may be knocked out) → Re-ranking (may be knocked out)
                           → Only the top few kept (may be knocked out) → AI writes the answer → Measure
```

In the full process, your page can be eliminated at every gate. A simplified experiment puts you straight at the final gate, so of course the numbers look good.

Tricks for fooling AI are a vivid example. In a controllable experimental system, researchers tested a batch of "prompt injection" techniques, which hide instructions in a web page in an attempt to manipulate AI's answers. Under simplified fixed-context conditions, these techniques had been reported to succeed about 80% of the time. When the researchers put the same batch of techniques into the full "search → re-ranking → write the answer" process, most of them stopped working. The general-purpose "override the instructions" technique lost about 40% at the search gate alone, and its end-to-end success rate was left at only about 14.7%. A more technical technique, which attacks the model by repeatedly fine-tuning the text with mathematical methods, had an end-to-end success rate below 2%. Only one type of technique still worked: injections that rewrite the content while staying highly relevant to the question, which still had an end-to-end success rate of about 40%–54%.

The drop from 80% to these levels comes almost entirely from one thing: whether the content had to pass the "being found by search" gate.

Overestimation does not happen only in simplified experiments. Looking directly at existing observational data overestimates too. In a controllable experimental system, researchers compared the effect of "ranking position" on "being cited by AI". The same thing was measured in three ways, giving three very different answers:

| Measurement method | Difference in chance of being cited between rank 1 and rank 5 |
|---|---|
| Looking directly at observational data | 42.3 percentage points |
| Controlled replay: change only the position, keep everything else the same, measure again | 7.9 percentage points |
| Replay with a separate batch of data set aside in advance and never used before | 0 |

The gap is this large because, in the observational data, the content ranked first was already more relevant and more authoritative. It may be cited more often not because of its position but because the content itself is better. Factors like these, which are mixed in and distort your judgement, are called confounding factors. Once the confounding factors are removed, the effect of "position itself" shrinks sharply, and even disappears.

These two examples add up to one rule: **any study that skips a gate, or that does not separate out confounding factors, reaches conclusions that lean optimistic.**

## 4. How strong is the evidence: six research methods

This book uses fixed phrases to mark how strong the evidence is. When you see any study elsewhere, you can sort it yourself with the same ruler. The ruler has six research methods in total.

Closest to the truth are real-user experiments, meaning comparisons with random or near-random assignment into groups. When this book meets such a study, it will say "large-scale real-user experiments have shown…". This kind of study can answer whether real traffic and visits changed after something was done, but it usually covers only one website or platform and is hard to generalise to anyone else. Next comes repeated testing on real AI search, which this book writes as "researchers ran repeated tests on real AI search and found…". It can show whom commercial AI products actually cite and how unstable that is, but it is mostly observation: what it sees is "appearing together", not "what causes what".

The third method is given-page testing, which this book writes as "under test conditions with given web pages…". It can answer how AI uses a page after reading it, but it skips "will AI find this page by itself". The fourth is a reproducible experimental system, which this book writes as "in a controllable experimental system…". It can show how big a causal effect is in a complete process built with public tools, but a process built with public tools is not the same as a commercial product. The fifth is simulation or theory, which this book writes as "possible in theory, but not yet proven". It can only show whether something is possible in terms of mechanism, and cannot be taken as a real-world conclusion.

The sixth is letting AI act as the judge and give scores. Strictly speaking, it is not an independent level; it is more like a measuring stick that any of the methods above may use. Its advantage is that scoring can be automated at scale. The problem is that the scoring itself may be unreliable.

### Real-user experiments: closest to "does it actually work", but very few

These studies look directly at real traffic or real visits, so they come closest to the answer a business owner wants. Unfortunately there are very few of them so far, and most are run by the platforms or websites themselves. The two real examples below show, respectively, their value and their pitfalls.

In the first example, a website carried out a full set of optimisations aimed at AI answers, and afterwards its referral traffic from ChatGPT grew 5.7 times during the observation period. That sounds astonishing, but pages on the same website that had not been optimised at all also grew 3.5 times over the same period, because ChatGPT's own user base was growing fast and every page rose with it. The researchers used the unoptimised pages as a control group and calculated with a method designed specifically to analyse whether a trend suddenly jumps a step before and after a certain point in time. This method is called interrupted time series analysis. After removing the platform's own growth, the jump that can truly be credited to the optimisation was about 1.8 times; checked with several other calculation methods, the result fell between 1.8 and 2.3 times.

This 1.8 times comes with several reservations. The researchers ran a "placebo test", pretending the optimisation had happened at other points in time to see whether they would also "see an effect", and the result reached only the level of "there are signs", not yet certainty. The optimisation consisted of several measures done together, so there is no way to tell which one worked. Over the same period, organic clicks from traditional search actually fell by about 25%, and the study shows no evidence that "doing AI optimisation also lifts traditional search". The same study also recorded a single-day spike of 38.2 times, and a single-day figure like that is even less usable as an optimisation effect. The lesson of this example is that **most of the raw multiple is the whole platform growing, not you doing something right.**

The second example is a test an image platform ran on itself. It added annotations to its content that matched users' search intent, then built collection pages and internal links, and ran a 4-week A/B test, which means randomly splitting users into several groups and comparing them. The group with these features switched on had 1.18 times the visits of the control group; the group with the related features switched off had 0.82 times the visits of the control group. That looks good, but a careful reading of the same report reveals several numbers that don't match. The main text says "relevance improved by 19%", yet the figures in the table don't match it. The main text claims a 20% increase in traffic, while the breakdown table shows increases of only +0.83% to +1.83%. The report also mentions "9.2 times generative search traffic" without explaining how this metric is defined.

So even with the highest-level research method, you still need to check whether the numbers in the main text and the tables agree and whether the metrics are defined. Keep in mind too that the one running the experiment was the platform itself, that is, the party that benefits from the results.

### The other methods each have a gap

Studies that run repeated tests on real AI search put questions directly to real products such as ChatGPT, Perplexity and Google's AI Overviews, and record whom they cite and whom they recommend. Their strength is that they reflect the real behaviour of commercial products. Their weakness is that most of them can only describe "who was cited" and cannot prove that "change this, and you will be cited". Pay special attention to the word "repeated". Some studies run their questions only once on a single day, which strictly speaking is just a snapshot, and as you will see in the next section, the error in a single snapshot can be large enough to overturn the conclusion completely.

Given-page testing and reproducible experimental systems each miss one part. In given-page testing, researchers hand URLs to commercial AI products by hand. The second half, "AI writes the answer", is real, but the first half, "AI finds you by itself", is missing. In a reproducible experimental system, researchers use public search tools, ranking tools and AI models to build a complete process themselves. The causal relationships are cleaner, but this process is still not a commercial product. Both have value, and neither can be presented directly as "doing this works on ChatGPT".

Simulation and theory can only show that something is "possible". Fixed-context experiments that feed web pages straight to AI, simulations where computers pretend to be users, and mathematical derivations all belong here, and of all GEO research, this category is the largest. These studies are good for proposing hypotheses and explaining the mechanisms behind things, but not as a basis for practical action, so whenever this book meets such evidence it always writes "possible in theory" or "possible in terms of mechanism".

Last comes letting AI be the judge. Many studies use an AI model to give scores, for example to judge whether a sentence is supported by its source or whether a piece of content is relevant. The problem is that the AI acting as judge also makes mistakes. One study that ran repeated tests on real AI search had AI judge "whether this sentence is supported by the source" and then compared that with human judgements. On 100 samples, the agreement between the two (the correlation coefficient) was only 0.62. A correlation coefficient is a number between 0 and 1, where 1 means complete agreement; 0.62 counts as only moderate. The researchers themselves acknowledged that this limited the credibility of their core metric.

So when you read a study that "uses AI to score", first check whether it was compared with human judgements, how many samples were compared and how high the agreement was. Then check whether the judging AI and the AI being judged come from the same company or are the same model. Finally, check whether the scoring criteria are public, and whether the conclusion still holds when a different judging AI is used.

## 5. Rolling dice: the same question can get a different answer every time

This is one of the most important ideas in the whole book. AI answering a question is a bit like rolling dice: ask the same question ten times and the answers may differ. **This is a property of these systems themselves, not a measurement error.** So any conclusion based on "looking just once" deserves some doubt first. Look at "how many times out of ten it appears", not at "what rank it holds".

### The same question, asked twice

Researchers ran repeated tests on real AI search and found that when the same question is asked again, the websites cited in the two answers often overlap by only a third to a half. Comparing the websites cited in two answers, the median similarity was about 0.29–0.31 for Gemini, about 0.33–0.40 for SearchGPT and about 0.50 for Perplexity. This also means that measuring accurately takes a lot of questions. To estimate a website's "citation share" with an error range of only plus or minus a few percentage points (a total error range width within 5 percentage points), Gemini needs about 30–50 questions, Perplexity about 90–100, and SearchGPT 150 or more.

Even the top recommendation changes. When the same question was asked 6 times, the "top recommendation" changed for 4 out of 6 questions. Different metrics also differ in stability. One vendor's long-term tracking data shows that whether a brand "is mentioned or not" is close to a yes-or-no matter and relatively stable, but whether "the assessment is positive or negative" flips back and forth about 6.7 times as often as "is mentioned or not". This vendor recommends running "is mentioned or not" at least 3 times and using at least 10 questions for "positive or negative" before the results become reasonably stable. This is a recommendation drawn from observation, not the conclusion of a strict experiment.

> **A closer look: how is similarity calculated?**
> The research uses a calculation called Jaccard similarity: take the number of websites cited in both answers and divide it by the total number of websites cited across the two answers. 0 means completely different, 1 means identical. The "median" means lining up the results of many comparisons from smallest to largest and taking the one in the middle, so that extreme values don't pull the figure off.
> In research, the "error range" is called the "95% confidence interval". It means there is a high degree of confidence that the true number falls within this range. The narrower the range, the more accurate the measurement.

The same thing shows up in controllable experimental systems. When AI writes the answer only once each time, about 15% of the "cite or don't cite" decisions flip when it is run again, and about 45% of the differences in effect the researchers observed came from the randomness of AI writing the answer itself. There was also a large-scale check whose subject was a social platform's own AI search. When the same question was looked up again, only about 41.8% of cases got back exactly the same sources; but when the material AI retrieved was the same, 89.6% of the answers were almost identical. So what keeps changing is mainly "what gets found", while "how it gets written" is in fact quite stable.

### Switching to a different AI or a different language

Different AI products cite sources that overlap very little. The table below puts several comparisons together:

| What is compared | Degree of overlap |
|---|---|
| Websites cited by different AI products | Similarity about 0.10–0.25 (varies by study and industry) |
| AI products vs Google's regular search results | Website overlap ranging from about 4% to 25% (varies by product and study) |
| Google's AI Overviews vs Google's regular search results | About 68% overlap among the top 100 websites |
| The app version and the web version of the same Chinese AI platform | Website-level similarity 0.19–0.51; for one platform, only 0.014 at the level of individual pages |

So "it works on ChatGPT" cannot be extended to Perplexity, and "it works on the web version" cannot even be extended to the same company's app.

Language has an even bigger effect. Researchers ran repeated tests on real AI search and found that **the language the question is asked in is one of the largest systematic factors affecting the results.** One study broke down "why answers differ" and found that the language of the question accounted for 26.5% of the variation in single answers, while the brand itself accounted for only 1.5%. The reliability of the ranking within a single answer was only about 0.01, which means it has almost no reference value.

Language also decides the candidate list. When commercial questions were asked in the local language, major international companies appeared only 1 time out of 24. When the questions were asked in English in two non-English-speaking cities, local companies did not appear once in 12 tries. Language, then, decides which batch of companies AI has in mind as candidates, and the country the internet connection comes from (the exit IP) decides which country's market. In practice, this means that if you measure only in English, you will completely miss the local competitors in non-English markets.

The same study also estimated that asking in more languages is more useful than asking the same question more times. After the same question has been asked 5 times, asking it 5 more times reduces the error by only 0.0003; adding 3 more languages instead reduces the error by 0.00462, about 15 times the effect. So a measurement budget should be spent on "breadth", meaning more languages, more AIs and more ways of asking, rather than on repeating the same question in "depth". Note that this result has been estimated only for the "positive or negative assessment" metric, and its error range has not yet been calculated.

### Switching to a different date or a different way of asking

The platforms themselves keep adjusting "whether to give an AI answer". Researchers ran repeated tests on real AI search and found that Google's AI Overviews expanded from appearing in only 7 countries in 2024 to 229 countries in 2025; in the United States, the share of queries that showed AI Overviews rose from 42% to 67%. For one category of health-related queries, the share showing AI Overviews rose from 1% to 66%, though this subsample contained only 74 queries. One vendor's tracking data also shows that, with no one changing anything at all, a brand's visibility on ChatGPT fell by an average of 1.34% per run, and on Perplexity by an average of 0.76%. This means that if a "before vs after optimisation" comparison has no control group, you simply cannot tell whether a change was caused by your optimisation or by the platform itself changing.

The way a question is asked also changes the results, though not in the place most people expect. On AI products used by ordinary consumers, adding "list your sources" at the end of a question raised the average number of citations from 16.6 to 19.9, while the make-up of the sources changed by no more than 2.1 percentage points, a very small effect. But on the interface for developers (the API), the same sentence raised the share of cases in which AI "decides to search" from 12.1% to 88.4%. So the wording of a question mainly changes "whether to look it up", and has very little effect on "whom it finds". Answers also follow the wording of the question: on controversial, debatable questions, the share of one-sided answers from the various AIs ranged from about 49% to about 90%. Any measurement should therefore publish the full text of the questions, whether it used a consumer product or the developer interface (API), and the language, region and date.

### "Being listed" is not the same as "being used"

The last trap is hidden in the measuring stick itself. When a report says "you were cited 100 times", you need to ask whether you were listed, used, or used correctly. This is gate 6 of the seven gates: whether it actually uses you, and uses you correctly.

Researchers ran repeated tests on real AI search and found that, in Chinese AI search, content from 66% of the web pages listed as sources made it into the body of the answer, 30% were substantively cited, and only 8% were cited in depth. About 39.3% were "silent citations", meaning they were listed as sources but their content was not used. Another cross-system check found that community discussion sources were listed as citations in Google's AI Overviews, but noticeably little of their content was actually absorbed into the answers.

Citing sources that really exist can also mislead. A check of more than 760,000 "answer–source" pairs found that 30.6% of citations distorted the original meaning of the source, and in 27.1% of cases the source itself was not suitable for answering that question. The researchers also pointed out that some conclusions are in fact artefacts of the calculation method. For example, part of the conclusion that "long sources are overused" comes from the scoring method, and with a different way of calculating, the gap narrows sharply. **"Mentioning you" and "really speaking up for you" are two different things.**

## 6. Disputes: what different studies say about the same thing

The first dispute is the gap between "40%" and later research. One side believes GEO rewriting can greatly boost visibility, based on early fixed-context studies showing a relative increase of up to about 40%. The other side believes this is not an effect anyone can generally expect. A critical review that pulled together 45 studies points out that in a cross-method, cross-industry benchmark, only 3 of 54 "method × industry" combinations showed a clear, significant positive effect. Another multi-stage test also found that optimising only the body text actually reduced the share of pages entering the top 20 by about 9%, and reduced the share that were finally cited by 6%.

The two sides are not necessarily in contradiction. The former measures the situation where you are "already among the candidates", while the latter also counts the "being found by search" gate. But taking the former to mean "do GEO and you get 40% more" is a misreading.

The second dispute is whether ranking position really matters. As mentioned earlier, observational data shows a huge gap between rank 1 and rank 5; after controlled replay, the gap shrank to 7.9 percentage points; and with a batch of never-used data, the gap disappeared. The same study also found something interesting. Organising content with structure, using headings, lists and tables, increased the number of times the target source was cited by an average of 0.50, and this result is statistically reliable. But the total number of citations in the answer did not increase, so what structured presentation does is redistribute credit among several sources of similar quality; the pie as a whole does not get bigger. As for the most important metric, "whether it was cited or not", the effect is uncertain: it appears to rise by 4.5 percentage points, but the error range crosses 0, so the true effect could be positive, zero or even negative. **The same thing, viewed through different metrics, can lead to different conclusions.**

The third dispute is how many times you need to repeat a question. The side that favours more repetition points out that with only a single snapshot, the error range is so wide that the gaps between many websites are just noise, and estimating citation share takes from dozens to over a hundred questions. The side that says repetition need not be extensive and that breadth should be expanded relies on decomposition studies: after the 5th repetition, further repeats add little value, while adding languages and AI products brings greater benefit. The two views can coexist. First repeat until the results for a single condition stabilise, then shift the budget towards more languages, more AIs and more ways of asking. But remember that the "breadth first" conclusion has so far been estimated only for the "positive or negative assessment" metric, and its error range has not yet been calculated.

Finally there is a problem fewer people mention: many measurement studies come from people with a stake in the outcome. Among the real AI search studies mentioned in this chapter, several were written by vendors who sell AI visibility services themselves, or by people connected to GEO service providers. This does not mean the data is fake; some vendors' studies are precisely an honest disclosure that "this is hard to measure accurately". But keep in mind that vendors have a motive to prove that visibility "can be measured, is worth measuring and is worth paying to optimise", and vendor studies are mostly observational, rarely true controlled experiments. Groupings, such as sorting brands into "large brands", "mid-sized brands" and "small brands", are often decided by hand; samples may also cover only a few topics and a few AI models. Platforms testing themselves, like the image platform example earlier, have the same problem, because the people running the experiment are also the ones who benefit from the results.

## 7. How much should you trust what people in the industry say?

Among the evidence this book gathered for this chapter, not a single hands-on test by people in the industry passed the screening and could serve as a case in this chapter. That in itself is a signal. **Many widely circulated numbers, such as "40%" and "3 times", often cannot be traced back to an original test that can be checked.** The method below will be used in every chapter of the book.

First, distinguish four kinds of claims. The weightiest is a repeated, controlled hands-on test, marked by before-and-after comparisons, a control group, many repetitions and published methods. This book will write it as "someone in the industry tested this themselves (repeatedly, with controls) and found… (but no one has independently verified it)". It can serve as reference evidence for practical action, but still needs independent verification. Next is an ordinary hands-on test report: someone did it themselves and has numbers, but the controls or repetitions are incomplete. This book will write it as "someone in the industry tested this themselves and found…", state clearly that it has not been independently verified, and use it only as a reference for direction.

The third kind is a one-off observation, such as a phenomenon seen once or a screenshot. This book writes it as "someone in the industry observed…", and it can serve only as a clue or an example. The fourth kind is community consensus, that is, what many people say. This book will write "many people in the industry believe this, but 'many people believe' does not mean 'it is right'". It shows what people think, and cannot be taken as proof.

Once you have sorted the claims, you also need to avoid six common traps. The first trap is believing that having done it yourself makes it reliable. People who did it themselves may also have done it only once, and as Section 5 showed, the top recommendation in a single answer often changes. The second trap is treating a screenshot as evidence. A screenshot of "my brand appearing in a ChatGPT answer" proves only that one time, that language, that region and that day. The third trap is a before-and-after comparison without a control group. The platforms themselves keep changing (see the part of Section 5 on dates), and the whole platform may also be growing (see the first example in Section 4). Without a control group from the same period, growth cannot be credited to optimisation.

The fourth trap is treating consensus as truth. Many people repeating the same claim may simply be passing on the same source, and each original author should count as only one vote. The fifth trap is letting numbers drift away from their conditions. When you see "a 40% increase" or "3 times", ask whether it is a relative or an absolute increase, whether it measures being found by search, being cited or traffic, and in which AI, which language and which period it was measured. The sixth trap is conflict of interest. First find out whether the person speaking sells tools or services, and whether they have business dealings with the brands mentioned. For content like this, this book will at most write "a vendor claims…, but it has not been independently verified".

## 8. Three real cases

### How a "5.7 times" became "about 1.8 times, and only with signs"

A website carried out a full set of AI answer optimisations. It tidied its URL formats into a single consistent scheme, went through the "page not found" (404) records left by AI crawlers to find content people wanted that did not exist, rewrote headings as questions, and added a summary to each section that could be read on its own. The study looked at referral traffic from ChatGPT. The raw growth was 5.7 times, but pages on the same website that had not been optimised also grew 3.5 times over the same period. With the unoptimised pages as a control group, the jump was about 1.8–2.3 times, and the placebo test reached only the level of "there are signs". Over the same period, organic clicks from traditional search fell by about 25%.

This case shows that the raw multiple had the platform's own growth mixed into it, and that a control group within the same website is the key to separating the two. When several measures are done together, the effect cannot be credited to any single practice either.

### The same widely circulated number under different conditions

Researchers gave AI a fixed set of 5 candidate documents, rewrote the web pages among them in various ways, and then had GPT-3.5 write the answers. The word-count share rose from 19.3 to 27.2, a relative increase of about 40%. Later, under more complete conditions, most "method × industry" combinations showed no clear positive effect, and changing only the body text could even make a page less likely to be found by search. The number itself is not wrong; what is wrong is pulling it out of its conditions.

### Testing in English, you cannot see local competitors

Researchers used the logged-out web version of ChatGPT to ask for business software recommendations in different languages and from internet locations in different countries, repeating each combination 6 times. When asked in the local language, major international companies hardly appeared at all: only 1 time out of 24. When asked in English in non-English-speaking cities, local companies did not appear at all: 0 times out of 12. When asked in one country's language but from another country, AI gave companies from the country that language belongs to.

The limitations of this study are also obvious. It tested only one AI model, asked only 6 times per combination, its author is a vendor that provides visibility measurement services, and in another product category used as a comparison, no language effect was seen. So it is a good warning sign, but not yet a settled conclusion. The point it makes is that the language and region you choose when measuring decide in themselves what you will see.

## 9. How to do it: the inspection checklist

When you get a study, a vendor report, or someone in the industry sharing their experience, ask the eight questions below in order. Each one states what to ask, what counts as a failing signal, and what the question is based on.

1. Research method: ask whether it is a real-user experiment, repeated testing on real AI search, given-page testing, an experimental system, or a simulation. Being unable to say clearly, or presenting simulation results as real effects, is a failing signal. This question is based on the book's standard for grading evidence.
2. Which gate it measures: ask whether it measures triggering, retrieval, citation, absorption or traffic. Inferring "there is traffic" directly from "being cited" is a failing signal. This is based on studies that ran repeated tests on real AI search, and on the critical review.
3. Candidate documents: ask whether the content was found on its own or fed straight to AI. Claiming "easier for AI to find" when the setup was clearly fixed-context is a failing signal. This is based on results obtained in a controllable experimental system.
4. Repetitions and error range: ask how many times each condition was repeated and whether an error range is given. A single screenshot, a one-day snapshot, or reporting only one average are all failing signals. This is based on studies that ran repeated tests on real AI search.
5. Scope of measurement: ask which AIs, which languages, which regions, which interface and which day it tested. Testing only one AI and then saying "AI search is all like this" is a failing signal. This is based on studies that ran repeated tests on real AI search.
6. Control group: ask whether there is a control group from the same period with no changes made. Having only a "before vs after" comparison is a failing signal. This is based on large-scale real-user experiments.
7. Who did the scoring: ask who gave the scores and, if AI acted as judge, whether it was compared with humans. Not reporting the judge's level of agreement is a failing signal. This is based on studies that ran repeated tests on real AI search.
8. Interests and consistency of numbers: ask who the authors are, whether they sell related services, and whether the numbers in the main text and the tables agree. The author being the beneficiary, numbers that don't match, and undefined metrics are all failing signals. This is based on the counterexample in the large-scale real-user experiments.

Go back to the deck received by the coffee bean shop owner at the start of this chapter. "Up to 40%" fails questions 2 and 3, the screenshot fails questions 4 and 5, and "traffic grew 5.7 times" fails question 6. "Everyone in the industry knows" is only the fourth kind of claim, "community consensus", and it fails question 8 as well. This does not mean GEO is useless. **It only means this deck has not proven anything yet.**

### If you want to measure it yourself

You can measure it yourself too, and you can measure it fairly accurately. The research supports the six practices below, each listed with what it is based on.

1. Repeat the same question many times first, then expand to more languages, more AIs and more ways of asking. This is based on repeated testing on real AI search, though "breadth first" has so far been estimated only for the "positive or negative assessment" metric.
2. Record the conditions in full, including the complete text of the question, whether you used a consumer product or the developer interface (API), the language, the region of the internet connection, and the date. This is based on repeated testing on real AI search.
3. Report each AI separately, and don't average different AIs' results into a single "AI visibility score". This is based on repeated testing on real AI search.
4. When reporting citation share, include the error range rather than giving just one percentage. This is based on repeated testing on real AI search, though the authors are vendors.
5. When evaluating the effect of an optimisation, keep a batch of control pages, that is, pages on the same website, of the same type, with no optimisation done. This is based on a large-scale real-user experiment, though it covered only one website.
6. Distinguish three things: being listed as a citation, having your content used, and having it used correctly. This is based on repeated testing on real AI search.

### Things not to do, and views that are out of date

There are a few things you had better stop doing. Don't use a screenshot to prove "the optimisation worked" or "A is better than B", and don't treat percentages from fixed-context or simulation experiments as effects you can promise to clients. Don't treat raw growth multiples as the effect of optimisation. When measuring non-English markets, don't use only English. And a practice does not count as proven just because "many people say so".

In addition, three views are out of date. The first is treating "GEO boosts visibility by up to 40%" as a general effect, when in fact this number applies only under the condition of "already among 5 candidate documents, with GPT-3.5 writing the answer, measuring word-count share". The second is believing that good traditional search rankings mean good AI visibility, yet several studies show that the sources cited by AI products and by traditional search overlap very little. The third is believing that asking once can represent AI's "view", when in reality, if the same question is asked again, the sources cited often overlap by only a third to a half.

## Key points of this chapter

Every GEO conclusion comes with conditions: which of the seven gates it measures, what system it uses, what language and what date. Numbers stripped of their conditions get misread. "GEO boosts visibility by 40%" is a relative increase obtained under the conditions of a fixed set of 5 candidate documents, GPT-3.5 writing the answer, and measuring word-count share; it does not mean being found more easily, nor does it mean more traffic. Experiments that skip the "being found by search" gate, and observational data that does not separate out confounding factors, both systematically overestimate effects.

AI search is unstable by nature. When the same question is asked again, the sources cited often overlap by only a third to a half; language, AI product, interface, date and wording all change the results. So a screenshot or a one-day snapshot is not evidence; measurement needs repetition, needs an error range and needs to expand in breadth.

Real-user experiments come closest to "does it actually work", but there are very few of them, and they still need a control group from the same period to subtract the platform's own growth. With AI as judge, vendor studies and platforms' own tests, check whether there was comparison with humans, who benefits, and whether the numbers agree throughout. As for what people in the industry say, distinguish "repeated, controlled hands-on tests", "one-off observations" and "community consensus"; consensus is not the same as truth.

## Remember in one sentence

**GEO numbers all come with conditions: first ask where they were measured, which gate was measured and what they were compared with, then decide whether to believe them.**

## What you can do tomorrow

1. Take out any GEO report or slide deck you have and run it through the "eight-question inspection checklist" to see how many questions it passes.
2. Pick a few of the questions you care about most, ask each one many times on the same AI, and record "how many times" your brand appeared, not "what rank" it held.
3. Then widen the scope: switch to the languages your customers actually use, try different AI products and try several ways of asking. If you serve overseas markets, be sure to ask in the local language.
4. Start a measurement log, writing down the complete text of the question, which AI you used, whether it was a consumer product or the developer interface, the language, the region of the internet connection, the date and the result.
5. Record each AI's results separately and don't average them into one overall score; when reporting share, include the error range.
6. When recording, distinguish three things: whether you were listed as a source, whether your content was really used, or whether it was used correctly.
7. Before you do any optimisation next time, first leave a batch of pages of the same type on the same website untouched, as a control group.

## Stop doing this

**Stop using a screenshot to prove "the optimisation works" or "we are better than our competitors".** Roll the dice again and the result may well be different.

Stop treating numbers from fixed-context or simulation experiments, such as "up to 40%", as effects you can expect or promise to clients. Likewise, stop treating raw growth multiples as the effect of optimisation; much of that is very likely the platform's own growth.

Stop measuring non-English markets in English only, and stop treating a practice as proven just because "everyone says so".

Finally, stop believing these out-of-date views: "40% is a general effect", "good traditional search rankings mean good AI visibility", and "asking once can represent AI's view".

## What is still uncertain

**How big is the effect of GEO rewriting, really?** Early studies saw a relative increase of about 40% under the condition of "already among the candidate documents"; but once "being found by search" is counted, only 3 of 54 combinations showed a clear positive effect, and changing only the body text may even do harm. The two measure different things, and the real-world effect is not yet settled.

**How much do ranking position and structured presentation matter?** The effect of position shrank sharply after controlled replay and disappeared with a different batch of data. Structured presentation can increase the citations of the target source by 0.50, but the total number of citations stays the same; the effect on "whether it was cited or not" is uncertain, appearing to be +4.5 percentage points, but with an error range that crosses 0.

**How many repetitions, and how much breadth?** "Repeat until stable first, then expand to more languages, AIs and ways of asking" is currently the more reasonable approach; but "breadth first" has been estimated only for the "positive or negative assessment" metric, and its error range has not yet been calculated.

**How widespread is the language effect?** The current case tested only one AI model, asked only 6 times per combination, was written by a vendor that provides visibility measurement services, and saw no language effect in another product category used for comparison.

**Is that 1.8 times reliable after all?** The placebo test reached only the level of "there are signs"; and because several measures were done together, it is not known which one worked.

**How far can AI as judge be trusted?** The agreement seen so far is only moderate (0.62, on 100 samples), which limits conclusions built on it.

**How far can the studies of vendors and platforms themselves be trusted?** The data is not necessarily fake, but it is mostly observational, groupings are often decided by hand, samples are limited, and the authors are the beneficiaries, so independent verification is still needed.
