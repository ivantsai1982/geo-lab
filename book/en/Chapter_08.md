# Chapter 8 — Writing Tricks Have an Expiry Date Too

## A hypothetical story

Imagine that An is a marketer at a small software company.

She read a piece on "secrets to getting AI to cite you": put more statistics in your articles, quote more experts, and add more reference sources. Supposedly, doing this could raise your chances of being cited by AI by 30% to 40%.

An spent two weeks revising all twenty articles on the company website. At the bottom of every article she added a "data box", plus a few expert quotes.

A month later, she asked the AI the same question. Her company still wasn't in the answer.

An wasn't lazy, and she didn't get any steps wrong. She was simply handed a prescription that had already expired.

This chapter makes just one big point: **Writing tricks expire. What doesn't expire is "aim at the question, stay true to the facts, and make the key points easy for both people and machines to extract."**

---

## Which gates this chapter deals with

Recall the book's seven gates. This chapter assumes two things up front: your web page can already "get through the door" (there is no problem with crawl access), and it has already been indexed by search engines.

This chapter asks only one question: **For the same web page, does how you write and revise the content change AI's chances of citing it, and how much of it gets cited?**

This mainly concerns three gates:

- Gate 4, "Will it pick you?" (selection and ranking)
- Gate 5, "Will it mention you?" (citation)
- Gate 6, "Did it really use you, and use you correctly?" (absorption)

We will also look back at Gate 3, "Can it find you?" (retrieval). Because changing your content can sometimes get you eliminated at this very gate — something many people don't expect.

This chapter answers five questions:

1. Why does the 2023 fad of "add statistics, add quotes, add cited sources" no longer work on today's AI?
2. If most tricks dreamed up by people have stopped working, what do machines end up finding when they search for the best way to write on their own?
3. Freshness, structure, structured data, Q&A format, short paragraphs, an authoritative tone, keyword stuffing: how much evidence is there for each? Which gate does each one act on?
4. What side effects does optimising content have? When does more optimisation make things worse?
5. Where do research and industry tests contradict each other? How should we make sense of that?

---

## 1. Where that "expired prescription" came from

### The three tricks of the time

In 2023, researchers first put together a set of writing methods for getting AI to cite you more. The three most famous were: add quotes, add statistics, and add cited sources.

These tricks were measured under a specific set of conditions:

- Your web page was **already** on a candidate list of just a few pages;
- An AI model of that time wrote the answer based on those few pages;
- What was measured was your "share of the words in the answer that came from you", and how much it changed before and after rewriting.

The reports at the time looked great. Later, researchers retested these three tricks on ten newer AI models, and the results were completely different:

| Trick | Effect reported in 2023 | Retested on new models |
|---|---|---|
| Add quotes | +42.6 | -0.33 |
| Add statistics | +32.8 | -0.28 |
| Add cited sources | +27.7 | -0.79 |

The unit in the table is "percentage points of citation share". Put simply: back then, each of the three tricks increased your weight in the answer by about 28 to 43 percentage points; retested on ten new models, none of the three increased citations, and the numbers dropped to around zero, or even slightly negative.

### Why they stopped working: three reasons

**First, AI itself keeps changing.** Models are replaced generation after generation. With each new generation, the way it judges "is this passage worth citing?" changes too. In the book's metaphor, the librarian has been replaced. The writing the old librarian liked is not necessarily what the new librarian likes. Something that worked on an old model doesn't mean it still works on a new one.

**Second, when everyone uses it, it stops working.** This is called the "crowding effect". Imagine an exam where the whole class has memorised the same set of predicted questions: those predictions are no longer anyone's advantage. The more websites adopt the same kind of rewriting, the less each adopter gains, until it approaches zero and becomes a zero-sum contest where your gain is someone else's loss. Simulation studies also found that once enough people adopt it, sticking stubbornly to a single trick can even perform **worse than not optimising at all**.

**Third, the experimental conditions back then were too lenient.** In experiments where "the candidate list is already fixed", your rewritten article only needs to beat the other four articles on the list. But real AI search is a whole pipeline:

- The experiment back then: you're already among 5 candidates → rewrite → AI writes the answer → your share rises
- The real pipeline: question → fetch material (retrieval) → re-ranking → AI writes the answer → citation

In the real pipeline, the same rewritten article may fall behind at the "fetch material" or "re-ranking" step, and never even reach the step where AI writes the answer.

### Conclusion of this section

**Any writing trick should be seen as "a hypothesis with an expiry date", not a law.** If you want to keep using it, you have to measure it again on today's AI.

> **A closer look: how reliable is this retest?**
>
> - Under test conditions where "the web pages are given", researchers retested these three tricks on ten new models, and none of the three moved citations. Without statistical correction, the number for "add cited sources" was nominally negative (meaning: it looks slightly worse, but we can't yet be sure it really is worse).
> - They then repeated it with three latest-generation models, and the result was again zero, or nominally slightly negative.
> - But two limitations must be stated honestly. First, the researchers who ran this retest themselves provide a content-scoring service, so there is a conflict of interest. Second, their method was to "append" the quotes and statistics "as a separate block", rather than blending them into the body text.

### Other studies point in the same direction

Besides the retest above, there are several simulation studies. A simulation study means: researchers run experiments in a test environment they built themselves. It can show that "the mechanism might work like this", but that doesn't mean the real world necessarily works that way.

- **54 combinations, only 3 worked.** Researchers paired various rewriting methods with different domains, 54 combinations in total. Only 3 produced a statistically credible improvement in citation ranking. In Q&A-type tasks, not a single one worked.
- **Adding statistics often backfires.** In 19 of 24 scenarios, adding statistics actually lowered rankings noticeably.
- **Position matters more than rewriting.** By comparison, putting a document in the first position of the material the AI reads brought far greater benefit than any content-rewriting method.
- **Shopping recommendation scenario.** In an e-commerce re-ranking scenario, researchers tested 15 human-designed writing tricks. Only 4 slightly beat or tied "one simple prompt"; the other 11 all fell short. The "storytelling" rewrite had an effect of -4.36.
- **Small word-level changes.** 9 rewriting tricks that only swap words and phrases **all** performed below the unrewritten original on three AI engines.

Most of these studies were done in environments where "the candidate material is fixed" or otherwise controlled. What they show together is: **tricks that are bolted on, or that only swap words, are unreliable.** This **does not mean** "evidence and data are useless". We'll discuss this in detail later in "Debate 1".

---

## 2. What machines found when left to search for the best way to write

### Three features it converged on

Since most human-invented tricks have stopped working, researchers tried a different approach: let AI try all kinds of rewrites itself and see which gets cited most.

Several research groups arrived at the same direction. The writing that automatic optimisation ultimately converged on had just three features:

- **True to the facts**: no exaggeration, no fabrication, no piling on emotion.
- **Aimed at the question**: respond directly to what the user is asking, in the user's own words. The industry calls this "query alignment".
- **Clearly structured**: points and paragraphs, so the information is easy to extract.

### One defensive rule makes manipulation pointless

One experiment is especially worth mentioning. In an e-commerce scenario, researchers first had AI optimise a prompt with the aim of "manipulating" product rankings. Then they added just one simple defensive clause to the system.

As a result, the prompt that had been used to manipulate rankings turned, on its own, towards a style of stating facts. The share flagged as "manipulation" dropped by an average of 60 percentage points.

In other words: **as long as the AI has basic defences, manipulation costs more than it gains. Honest, clear writing turns out to be the best solution.**

This is consistent with the point made in Chapter 6 of this book: what AI prefers is not some writing gimmick, but content that **matches the question, can be extracted, and can be trusted**.

### Two details to watch out for

**Preferences vary by domain.** Researchers had machines automatically summarise "what kind of content AI engines like". When the model was switched, the rules they came up with still overlapped fairly highly, about 79% to 84%. But when the domain was switched (for example, from e-commerce to general Q&A), the overlap fell to only about 35% to 40%. So writing that works for others in a different industry won't necessarily work in yours.

**Match the question first, then worry about how well it's written.** Another study compared two ways of scoring:

- One looks only at how well the content itself is written, regardless of what the user asked. This "content quality score" had only a weak relationship with actually being cited, a correlation coefficient of about 0.11.
- The other measures "whether the question and the source match". This score had a clearly stronger relationship with being cited, about 0.35 to 0.39.

(A correlation coefficient is a number between 0 and 1; the closer it is to 1, the more often the two things occur together.)

To put it another way: a busy librarian is looking for "a book that can answer this question", not "the book with the most beautiful prose".

> **A closer look: automatic optimisation isn't free either**
>
> - In an experimental system the researchers could control, using machine-summarised "engine preference rules" to guide rewriting raised visibility on one engine from 20.18 to 43.76; the other two engines also improved noticeably.
> - But on one of the engines, answer precision fell from 96.51 to 84.98. So the claim that "this kind of rewriting doesn't affect answer quality" doesn't fully hold.
> - In a simulated e-commerce analysis, automatically optimised prompts improved 63 of 75 test cells; and the size of the improvement had nothing to do with the length of the product description.

---

## 3. Different content elements act on different gates

### A common misunderstanding

Many people think every content tweak is a "make AI cite me" button. It isn't. Each works at a different gate:

| Content element | Which gate it mainly acts on |
|---|---|
| "Structural fields" such as the title, page description (meta), subheadings and structured data; short paragraphs; covering the words AI will use after rewriting the question | Gate 3: Can it find you? (retrieval) |
| The topic matches, the answer comes first | Gate 4: Will it pick you? (re-ranking) |
| Freshness, topical alignment, clear statements backed by evidence | Gate 5: Will it mention you? (citation) |
| Definitions, numbers, comparisons, steps | Related to Gate 6: How much of you the answer uses (absorption) |

Below, we look at them one by one, and how strong the evidence is for each.

### Freshness: effective, especially for time-sensitive questions

This is currently the item with the most consistent evidence. Two kinds of evidence point the same way:

- **Controlled experiments** (about 252,000 simulated trials): for the same content, the version labelled with a newer date had 14.4 times the odds of being selected compared with the version labelled with an older date, and under some conditions more than 10,000 times. (The "odds ratio" is exactly this kind of "how many times" comparison.)
- **Repeated testing on real AI search** (a Chinese-language AI search engine, about 160,000 citations):
  - For "highly time-sensitive" questions, the median age of cited web pages was 18 days; the citation "half-life" was 39 days, meaning that after about 39 days, the chance of such pages being cited drops by half.
  - For "weakly time-sensitive" questions, the median age was 101 days and the half-life was 68 days.

Conclusion: **Freshness works, especially for time-sensitive questions. The evidence is fairly strong.** But in "Debate 5" later we'll see a twist: the most-cited pages are not newly published articles.

### Definitions, numbers, comparisons, steps

Web pages containing these elements were absorbed into AI answers 41% to 77% more.

But note that this is a descriptive analysis researchers did on real AI answers. It only shows that "the two things often occur together", and doesn't rule out other possible causes. **The evidence is on the weak side.** Still, it points in the same direction as experimental results on "raising the evidence density of the whole page".

### Structure and structured data: they help you be understood, not help you be chosen

There are actually two kinds of "structure", and they need to be looked at separately.

**The first is structural fields**: the title, page description, subheadings and structured data (such as schema markup). They help AI's retrieval system find you. In an experimental system the researchers could control (about 171,000 real web pages), changing structural fields raised the chance of "being fetched" by about 22%. But at the following re-ranking step, performance still declined. **The evidence is moderate.**

**The second is body-text layout**: adding lists, adding subheadings, organising information into a block. In controlled experiments, layout had almost no effect on "who gets cited". Its odds ratio fell between 0.79 and 1.68 — sometimes slightly below 1, sometimes slightly above 1 — with no consistent direction. **Changing only the layout doesn't work.**

**The items within structural fields don't work the same way either.** A large-scale study (158,000 answers) compared different pages within the same website and found:

- **paragraphs that match the user's question** were cited clearly more (15.5% more per standard deviation);
- **titles that match the question** got 14.1% more, but had no effect on ChatGPT;
- **FAQ, structured data, summary boxes and page speed** all looked effective when comparing different websites (+7.5% to +20.9%), but none was clear when comparing within the same website (−5.3% to +6.9%). The reason is that these practices mostly appear on big websites that were already cited often.

So **the value of title wording lies in "matching the question"; structured data cannot be treated as a reason AI cites you**. This is a correlational study, it used small models, and the authors run an AI monitoring platform.

Also, simulation research shows: **rewriting without specifying whom to highlight barely works**. Of 36 settings, none was effective after correction, and about a quarter actually helped competitors; when a target was specified, half were effective after correction. Structural and argument-based rewrites worked best and switching to technical terms worked worst, but the gain was only 0.5 to 1.5 percentage points.

**Structured presentation only "redistributes"; it doesn't "grow the pie".** When the same fact has several sources of comparable content, researchers used replay experiments — "what would happen if it were presented differently?" — and found:

- Structured presentation can give the target page a few more citations, about +0.50;
- But the total number of citations across all sources did not increase — the extra ones were taken from other equivalent sources;
- As for the most important measure, "will it be cited at all?", the credible range of the improvement crossed zero; that is, **it's impossible to say whether there was any improvement at all**.

**The correlation between structure and being cited.** On real AI search, an observational audit of enterprise software (B2B SaaS) websites covering 1,702 citations found a correlation coefficient of 0.63 between structured data and being cited. But this is only a correlation, and it audited only pages that were cited, with no uncited pages for comparison.

Conclusion: **Structure acts on the two steps of "being found" and "being extracted"; in itself, it is not a lever for getting AI to cite you.**

### Q&A format: doesn't work on its own

Many people think it's enough to rewrite an article as a series of questions and answers. The data show:

- Q&A-format web pages are absorbed **5.74% less** than ordinary web pages (descriptive evidence).
- In self-built website experiments, the Q&A format had no clear advantage.

**The evidence is weak to moderate.** What really relates to absorption is whether the page has content that can be used directly: definitions, numbers, comparisons.

### Short paragraphs: there is preliminary evidence

On real AI search, someone built 450 websites themselves to test this, and short paragraphs and splitting into paragraphs performed best.

But this is **preliminary evidence**. That number represents "what share of successful exposures used short paragraphs", not "if you use short paragraphs, what your chance of success is". How big the effect really is remains unknown.

### Authoritative tone: not recommended

Rewriting in an "expert voice" has unstable effects, and may make AI see you as **less credible**. This conclusion comes from simulation analysis, with AI acting as the scorer; **the evidence is on the weak side**.

### Keyword stuffing: doesn't work

This one is not in dispute. Tests on real AI search, plus multiple simulation studies, agree: **keyword stuffing doesn't work, and can even be harmful.**

### Evidence strength at a glance

| Element | Where the evidence comes from | Strength |
|---|---|---|
| Freshness | Repeated testing on real AI search (Chinese-language engine, about 160,000 citations) + simulation experiments (252,000 trials) | Fairly strong; both kinds of evidence agree |
| Structural fields help with being fetched | Controllable experimental system (about 171,000 real web pages) | Moderate; chance of being fetched +22%, but re-ranking still declines |
| Structure correlates with being cited | Observational audit on real AI search (enterprise software websites, 1,702 citations) | Correlation only; looked only at cited pages |
| Structured presentation only redistributes citations | Controllable experimental system, including replay experiments | Moderate; main measure uncertain |
| Short paragraphs | Real AI search, 450 self-built websites | Preliminary; the number is "share among successful exposures", not a success rate |
| Definitions, numbers, comparisons | Descriptive analysis of real AI answers | Weak; other causes not ruled out |
| Q&A format has no advantage | Descriptive analysis + self-built website experiments | Weak to moderate |
| Authoritative tone is harmful | Simulation analysis, scored by AI | Weak |
| Keyword stuffing doesn't work | Real AI search tests + multiple simulation studies | Consistent across studies |

---

## 4. Optimisation has side effects too

Content optimisation doesn't bring only benefits. There are three known kinds of side effect.

**First, looking after one question hurts others.** A web page usually has to respond to several related questions. If you tune it for just one of them, 30.6% of the non-target questions get worse.

**Second, being seen more also means being misreported more.** Automatic rewriting aimed at "raising visibility" causes two scores to fall noticeably:

- Faithfulness (whether what AI paraphrases matches the original) fell from 8.29 to 4.90;
- Attribution accuracy (whether AI credits a claim to the correct source) fell from 6.15 to 4.18.

The page gets "seen" more, but it gets paraphrased correctly less.

**Third, falling behind at the earlier gates.** In the full pipeline:

- Changing only the body text lowered the chance of a page being fetched by about 9%, and the chance of it being kept during re-ranking by about 16%;
- Automatic rewriting that heavily expands the content lowered the chance of being fetched by about 36%;
- Rewrites that replace the original wording with obscure or technical terms caused the biggest losses.

Adding it all up:

- Change only the body text → at the step where AI writes the answer, perhaps you gain a little;
- But being fetched -9%, re-ranking -16%;
- Net effect: citation rate **-6%**.

It's like a job applicant who, wanting to shine at the interview, makes their CV long and flashy, and then doesn't even get through the paper screening.

---

## 5. Don't celebrate yet: the measurement itself wobbles

Remember the book's "rolling dice" metaphor? Ask the same question ten times, and the answers may differ.

- Researchers found in a controllable experimental system: when AI's single decision "should I cite this page?" is rerun, about 15% flip. Of the measured differences in effect, about 45% actually came from randomness in how AI generates text.
- Someone in the industry ran repeated, controlled tests: before making any change, first measure how much the results wobble on their own. He tested with 387 questions, and 3 days later 98% gave the same result. He therefore considers that changes smaller than about 3 to 4 percentage points should be treated as measurement noise, not as an effect.

This means: **testing just once, seeing a change of a few percentage points, and declaring that some way of writing works, is unreliable.**

---

## 6. Seven questions still under debate

Research and industry tests often contradict each other. But look closely, and most of the contradictions are really the two sides talking about different things.

### Debate 1: Do statistics and evidence actually help?

**The "no use" side:**

- On new AI models, appending a statistics block doesn't increase citations.
- In simulation experiments, adding statistics often lowered rankings; credibility as scored by AI also fell from 8.352 to 7.613.

**The "useful" side:**

- In simulation experiments, rewriting the whole page to raise the density of statistics and cited sources increased visibility by 37% to 96%. Researchers removed each change one at a time for comparison and found that "statistics" and "cited sources" contributed the most.
- In another simulation, adding statistics had an effect of +3.49; among all writing tricks, the "add evidence" type of change was the strongest.

**The two sides rest on different grounds:** the "no use" side tested "appending a block" or "only swapping words"; the "useful" side tested "raising evidence density when rewriting the whole page".

**On the industry-test side:**

- Someone in the industry tested this themselves: he produced an original study auditing the AI visibility of more than two thousand training companies. That study became the only page on his website listed by Perplexity as the first source. He believes original numbers are currently the strongest "worth citing" signal. (But no one has independently verified it.)
- Another person in the industry observed about 150 websites and found that the median share of paragraphs containing numbers, quotes or external links was only 23/100. In other words, on most websites, the paragraphs actually contain very little evidence.

**How to make sense of it: "pasting numbers on" and "the content genuinely containing evidence found nowhere else" are two different things.** The former has already been shown to be unreliable. The latter is currently supported only by simulation experiments and industry reports; on real AI search there is **no causal evidence yet**.

### Debate 2: Does structured data help?

**The supporting side:**

- In a controllable experimental system, structural fields (including structured data) raised the chance of being fetched by about 22%.
- In an observational audit, the correlation coefficient between structured data and being cited was 0.63 (correlation only).
- Someone in the industry tested this themselves: comparing enterprise software websites with similar traffic, sites with complete structured data were cited about twice as often as those without.
- Someone in the industry observed: after filling in complete structured data for a product with multiple variants, AI went from picking up only the default variant's price to correctly listing the price of every variant.

**The sceptical side:**

- Someone in the industry ran a randomised controlled test on 318 pages and found that Markdown formatting produced no statistically credible improvement. He also believes structured data is not the main lever.
- Someone in the industry tested this themselves: on the same test page, the price written in the structured data was 199.99, while the price visible on the page was 349.99. ChatGPT and Gemini both displayed the visible 349.99.
- Someone in the industry observed: one of their own websites has no structured data at all, yet still gets about 55,000 citations a month from search engines' AI features.
- Many people in the industry believe: structured data on its own has limited effect, and adding it casually or incompletely does nothing. (But "many people believe" doesn't mean "it's correct".)

**How to make sense of it:** Structured data works more like "helping machines understand what you already have" and "helping retrieval, and helping AI tell which entity you are", rather than "getting AI to choose you". Someone in the industry summed it up in one line: **Being readable is not the same as being chosen.** And when structured data conflicts with the content visible on the page, at least in the test above, AI trusted the visible content.

### Debate 3: Does the FAQ format help?

**On the research side:**

- Q&A pages are absorbed slightly less than ordinary pages, by 5.74% (descriptive evidence).
- In self-built website experiments, the Q&A format had no clear advantage.

**On the industry-test side:**

- Someone in the industry tested this themselves: they rewrote 8 comparison pages so that "under each second-level subheading, one question is fully answered within 300 characters", and added FAQ structured data. Within 6 weeks, across 12 target questions, ChatGPT citations went from 0 to 4.
- Another industry test: they added FAQ structured data, a summary at the top of the page and a comparison table, and posted on social media. Afterwards, across 60 questions, appearances rose from 4 to 25.

**A key counterexample:** Someone in the industry tested this themselves: FAQ questions written to follow keywords were **completely ignored** by AI; only questions written as "sentences real people actually type" were cited.

**How to make sense of it:** Industry success stories almost always involve "several changes made together", so the credit can't be assigned to the FAQ format alone. And the detail of "asking questions the way real people do" actually points to the **query alignment** discussed in Section 2, not to the format itself.

### Debate 4: Should the tone be confident or cautious?

- **Seen under lab conditions**: rewriting in an "authoritative voice" lowered credibility as scored by AI from 8.352 to 7.332. In the e-commerce scenario, the authoritative voice was also on the list of "tricks that don't work".
- **But another controlled experiment found**: "clear statements backed by evidence" favour being cited, while vague wording, and content that contradicts itself, lower the chance of being cited.
- **Someone in the industry tested this themselves**: they rewrote 8 articles into clearer assertive sentences that are easy to quote. Within two months, two topics that previously had no visibility at all started being cited. But there was no control group this time, and the author himself suspects it may have been a coincidence.
- **Another person in the industry ran repeated, controlled tests**: after cutting back on hedging words such as "however", "although" and "even though", citations became more stable.

**How to make sense of it: the issue isn't whether you sound confident, but whether you have grounds.** Clear statements backed by evidence and an authoritative voice with no grounds may have effects in exactly opposite directions.

### Debate 5: Newer is better, or older is steadier?

**Supporting "new":**

- Research shows newer dates have a strong advantage; the citation half-life for time-sensitive questions is only 39 days.
- Someone in the industry tested this themselves: they deliberately stopped updating a page for two months, and ChatGPT stopped citing it entirely, citing instead a short post on a professional networking platform that was newer and answered more directly.

**Supporting "old":**

- Someone in the industry tested this themselves: 356 cited pages had a median age of 23 months, and only 35% had been created less than a year earlier; but the median "last update" was 5 months earlier.
- Another industry test: about 43% of articles published more than two months earlier were cited; for new articles, only about 7%.
- Someone in the industry observed: when cited pages were first recorded as being cited, their median age was 203 days, and only 9% were less than a month old.

**Counterexample:** Someone in the industry observed that after updating a page that had been cited steadily, citations dropped noticeably. They only partly recovered weeks later, and never returned to the original level.

**How to make sense of it: "fresh" may mean two different things.** One is "someone has maintained this page recently", which helps pages that already exist; the other is "this page has just been published", and new pages often need time to build up. The most consistent pattern in the data is: **pages that have existed for a while and keep being updated are cited most often.** At the same time, updating itself carries risk: overhauling a page may temporarily disrupt the citations it already has.

### Debate 6: Top summaries, long content, publishing in bulk

**Top summaries:**

- In simulation studies, putting a summary at the front of the content had a small but credible benefit in two domains, retail and gaming.
- In a controllable experimental system, "putting the answer first" helped re-ranking.
- But someone in the industry tested this themselves: adding a "key points summary" at the top of the page had no effect.

**Length:**

- In simulation studies, the benefit of optimisation had nothing to do with the length of the description.
- In a controllable experimental system, heavy expansion lowered the chance of being fetched by about 36%.
- Someone in the industry observed that strong brands tend to publish long content of 2,000 words or more; someone else in the industry observed that making content more concise and more factual won a spot in AI Overviews.

**Publishing lots of pages:**

- Someone in the industry ran repeated, controlled tests: after publishing a large number of new pages on separate topics, within six weeks the share of ChatGPT recommending the brand rose from 11.9% to 23.1%; but over the same period, Claude's recommendation share fell by 4.1 percentage points.
- Another person in the industry observed: publishing three articles a week for two months, adding structured data and submitting to various directory websites for listing produced almost no change in citations.

**How to make sense of it:**

- "Putting the answer first" and "adding a summary at the front" are not the same thing. The former changes how each paragraph begins; the latter just adds one more paragraph of text.
- Length itself isn't the key. **Whether each paragraph can answer a question on its own** is the key.
- Whether publishing lots of pages helps depends on whether each page corresponds to a question that really exists and hasn't yet been answered well.

### Debate 7: Does good writing matter?

- Someone in the industry tested this themselves: auditing 158 articles, the average quality score of cited articles was 60.4, and of uncited ones 62.5. The ignored articles were actually slightly better written.
- Another person in the industry ran repeated, controlled tests: across 200 articles and 3 AI engines, the quality scores given by editors had almost nothing to do with being cited.
- Many people in the industry believe: only content with a viewpoint worth citing or useful information gets cited.

**How to make sense of it:** "Quality" here mostly means prose and editorial scores. What AI values is **being on-topic, being easy to extract, and providing information found nowhere else**, not fine phrasing. This points in the same direction as the research finding in Section 2 that "a content quality score that ignores the question has only a weak correlation with citation".

---

## 7. Six real cases

The following cases all come from first-hand reports by people in the industry, and no one has independently verified them. They are used to illustrate points, not as proof.

### Case 1: Two months without updates, replaced by a short post

- **What was done**: a page was deliberately left without updates for two months, with the topic and keywords unchanged.
- **Platform**: ChatGPT.
- **What was observed**: ChatGPT stopped citing this page entirely and instead cited a short post on a professional networking platform. The author of that short post had only 300 followers, but the post was newer and answered more directly.
- **What this shows**: freshness is a strong factor at the "Will it mention you?" gate. But "answering more directly" was also at work, so the cause can't be put down to freshness alone.

### Case 2: A business-to-business (B2B) client, from 0 to 7/10 in 12 weeks

- **Starting point**: of 10 target questions, 7 already ranked on the first or second page of traditional search, but had zero citations in AI Overviews.
- **What was done**:
  - Month one: review the content and restructure it so that each page opens by answering the question directly; add FAQ structured data to 8 target pages.
  - Month two: work on getting other websites to mention them, going from 2 to more than 12.
  - Month three: maintain content freshness and keep monitoring.
- **Platform**: Google's AI Overviews (plus Perplexity).
- **What was observed**:
  - The first AI Overviews citation appeared on day 18.
  - At 12 weeks, 7 of the 10 questions produced citations.
  - Traditional search rankings didn't change at all.
  - FAQ questions written to follow keywords were completely ignored; only questions written the way real people talk were used.
  - The remaining 3 questions, dominated by big brands, were never cracked.
- **What this shows**: putting the answer first helps re-ranking; aiming at the question matters more than format; and changing content alone can't close a gap in third-party sources (the chapter of this book on third-party sources discusses this in detail).

### Case 3: Four experiments by a website-building platform

- Rewrote the blog into articles that "answer real users' questions": within 3 weeks, share of voice on the tracked questions rose from 38% to 100%; 70% of tracked questions improved.
- Added a table of contents: within 4 weeks, clicks rose 23%, and visits from AI rose 60%.
- Changed titles into questions: within 4 weeks, visits from AI rose 58%.
- Added a "key points summary" at the top of the page: **no effect.**
- **What this shows**: the three things that worked all relate to "aiming at users' questions" and "letting AI quickly find the right passage". The one that didn't work just added a summary; the structure of the paragraphs themselves didn't change (see Debate 6).

### Case 4: Measure the noise first, then look at the effect

- **What was done**: tracked the same set of 134 questions every week. The strategy was to publish a large number of new pages on separate topics (458 articles), rather than rewriting old pages that already ranked. These pages were all plain HTML, not dependent on JavaScript.
- **Platforms**: ChatGPT, Claude, Google.
- **What was observed**:
  - Within about six weeks, the share of ChatGPT proactively recommending this brand rose from 11.9% to 23.1% (24 questions up, 9 down). Over the same period, Claude fell by 4.1 percentage points.
  - Google listed this website as a source in 36% of answers, but its share of recommending this brand was 0%.
  - Claude copied up to 64 consecutive words from this website, with the URL attached; but the recommendation list it gave still came from competitors' official websites.
  - Before making any change, he measured the noise first: 98% of questions gave unchanged results 3 days later. Changes smaller than about 3 to 4 percentage points were all treated as noise.
- **What this shows**: "being cited" and "being recommended" are two different states; the same content strategy can have opposite effects on different AIs (Section 1); before assessing an effect, you must first know how big the noise is (Section 5).

### Case 5: An audit of 158 articles

- **What was done**: reviewed 158 published pieces of content, audited 78 of them in detail against 28 criteria, and tracked them on ChatGPT, Perplexity, Google's AI Overviews and Claude.
- **What was observed**:
  - Writing quality was almost irrelevant: cited articles averaged 60.4 points, uncited ones 62.5.
  - The same author with the same material: published in industry media, the citation rate was about 52%; published on the company blog and on a personal web page, both were 0%.
  - Second-level subheadings phrased as questions: citations +19%; tables or lists: +18%; a sales tone: -26%.
  - About 43% of articles published more than two months earlier were cited, versus about 7% of new articles.
- **What this shows**: where it's published (third-party sources) matters far more than how it's written; a sales tone violates Section 2's "true to the facts"; new content needs time to build up (Debate 5).

### Case 6: Structured data at odds with visible content

- **What was done**: on a test page, the price marked up in the structured data (199.99) was made inconsistent with the price visible on the page (349.99).
- **Platforms**: ChatGPT, Gemini.
- **What was observed**: both displayed the visible 349.99.
- **What this shows**: at least in this test, AI took the visible text as authoritative. Structured data cannot replace body text (Debate 2).

---

## 8. Sorted into three baskets

### Recommended (ordered by strength of evidence)

| Practice | How strong the evidence is | Reminder |
|---|---|---|
| 1. First make sure the content corresponds to real questions, and write titles and questions in the words users actually use | In controllable experiments and simulations, "whether the question and content match" is the strongest predictor; industry tests also support it | Match the question first, then think about the writing |
| 2. Keep updating pages that already exist; update time-sensitive topics more often | Repeated testing on real AI search + simulation experiments, pointing the same way | The half-life for time-sensitive questions is about 39 days, which can serve as a reference for your review cycle |
| 3. Put your core entities and key numbers into the structural fields: title, page description, subheadings, structured data | Controllable experimental system | Acts on "being found"; not a lever for getting AI to cite you |
| 4. Give the answer at the very start of each section, so every paragraph can answer a question on its own | Controlled experiments (answer first helps re-ranking); many in the industry think so | It's about changing where paragraphs start, not adding a summary at the top of the page |
| 5. Break content into short paragraphs | Preliminary evidence on real AI search | The number is a share, not a success rate; size of effect unknown |
| 6. Include evidence found nowhere else: original data, definitions, comparisons, steps | Simulation experiments + descriptive correlation + industry tests | Blend it into the body text with source and date, not as a separate appended block |
| 7. Use clear statements backed by evidence, and cut unnecessary hedging | Controlled experiments; repeated, controlled industry tests | Clear is not the same as exaggerated; where you have no grounds, don't force it into an assertion |
| 8. Have one page look after several related questions, rather than tuning for just one | Simulation analysis | Tuning for just one question makes 30.6% of other questions worse |
| 9. Before assessing any change, measure the noise first, and record each AI engine separately | Controllable experiments (15% flip); repeated, controlled industry tests | Don't treat changes smaller than 3 to 4 percentage points as an effect |

### Myths: useless or harmful

- **Keyword stuffing.** All relevant research shows it doesn't work or is harmful; on real AI search, it has no effect on any system.
- **Replacing the original wording with obscure or technical terms.** In the full pipeline, this is the rewrite that causes the biggest loss in "being fetched".
- **Heavily expanding content to be "more comprehensive".** It makes the page fall behind at the "being fetched" step.
- **A sales, advertising, storytelling or emotionally exaggerated style.** Research and industry reports agree: they all point to negative effects. (This applies to the goal of "being cited by AI". Simulation research shows that in Q&A communities, answers with emotion and expressiveness actually get more votes from real people; these are two different goals.)
- **Adding only an authoritative voice, without evidence.** It may lower credibility.
- **Letting structured data and visible content disagree.** AI may go by the visible content; the conflict only causes confusion.
- **Overhauling a page that was being cited steadily all at once.** Someone in the industry observed citations dropping for several weeks as a result, and never fully recovering. Changes should be made in small steps and be reversible.
- **Chasing visibility alone at the expense of accuracy.** Rewriting aimed at visibility lowers faithfulness: you get cited more, and misreported more.

### Already outdated

- **Treating the "add statistics, add quotes, add cited sources" trio as standalone tricks.** The +27% to +43% reported in 2023 became zero or slightly negative when retested on new models.
- **Any "one trick boosts you 40%" list of tricks.** Rewrites that only swap words performed below no rewriting at all in several studies; and the more people adopt them, the closer the effect gets to zero.
- **Treating the FAQ format or structured data as the main means of "getting AI to cite you".** They help AI understand you and find you, but on their own they don't decide whether AI chooses you.
- **The idea of "optimise once, effective forever".** As soon as an AI engine updates, known practices may expire; you must remeasure regularly.

---

## Back to An

If An could start again, what she should do is not add another data box.

She should first work out: what questions do customers really ask AI? In what words? Then make every article, and every paragraph, answer that question directly, honestly and clearly.

If the company has data found nowhere else, write it into the body text, with its source and date. After that, update regularly, but don't do a big overhaul all at once.

Finally, after making changes, don't look at the result just once. First find out how much the "dice roll" itself wobbles, then judge whether you've actually improved.

Tricks expire. Aiming at the question, staying true to the facts and being easy to extract don't.

---

## Key points of this chapter

1. **Writing tricks have an expiry date.** The 2023 tricks of adding statistics, adding quotes and adding cited sources, retested on new models, no longer increase citations.
2. **Left to search for the best way to write on their own, machines end up converging on "true to the facts, aimed at the question, clearly structured".** This is currently the direction closest to a "universal best solution", and preferences also vary by domain.
3. **Match the question first, then think about the writing.** Whether the question and the content match predicts citation better than "content quality that ignores the question"; how well something is written has almost nothing to do with being cited.
4. **Freshness is the content factor with the most consistent evidence.** But the most-cited pages are those that "have existed for a while and keep being updated", not newly published ones.
5. **Structure and structured data act on "being found" and "being extracted".** Structured presentation only redistributes citations among equivalent sources; in itself it is not a lever for getting AI to cite you.
6. **Q&A format, an authoritative tone and keyword stuffing, used on their own, are all ineffective or harmful.** FAQ success stories mostly come from "aiming at the question in the words real people use", not from the format itself.
7. **Optimisation has side effects.** Tuning for one question hurts others; chasing visibility lowers faithfulness; changing only the body text may make a page fall behind at the "being fetched" step.
8. **Testing once can't be trusted.** About 15% of citation decisions flip when rerun. Before assessing any practice, measure the noise first, and record each AI engine separately.

---

## Remember in one sentence

Writing gimmicks have an expiry date; what AI ultimately prefers is content that aims at the question, stays true to the facts, and makes one thing clear per paragraph.

## What you can do tomorrow

1. **Match the question first.** List the questions customers really ask, in their own words, and compare them with your titles and subheadings; rewrite questions written to follow keywords as sentences real people would type.
2. **Make every paragraph able to answer a question on its own.** Pick a few of your most important articles and change the first sentence of each section so it answers the question directly. Don't just add a summary at the top of the page.
3. **Cut into short paragraphs.** Split long paragraphs up, one thing per paragraph.
4. **Get the structural fields right.** Put your core entities (brand, products) and key numbers into your title, page description, subheadings and structured data; and check that the structured data matches the content visible on the page, especially prices, specifications and dates.
5. **Include evidence found nowhere else.** If you have original data, clear definitions, comparisons or steps, blend them into the body text, with the source and date.
6. **Say things clearly, with grounds.** Delete unnecessary "however", "although" and "even though"; but where you have no grounds, don't force it into an assertion.
7. **Have one page look after several related questions.** Before rewriting, list all the related questions this page should answer; after rewriting, check each one to see whether any got worse.
8. **Set an update cycle.** Keep maintaining pages that already exist; for time-sensitive topics, you can use the half-life of about 39 days as a reference when scheduling reviews. Update in small steps, and keep the old version so you can roll back.
9. **Measure the noise first, then assess.** Before making changes, ask the same set of questions several times, note how much the results wobble on their own, and record each AI engine separately. After that, don't treat changes smaller than 3 to 4 percentage points as an effect.
10. **Treat every practice as a hypothesis.** After AI engines update, remeasure regularly on the current engines.

## Stop doing this

1. Stop "pasting" a data box or expert quote at the bottom of an article and assuming AI will cite you more.
2. Stop keyword stuffing.
3. Stop replacing your original wording with obscure or technical terms.
4. Stop heavily expanding content to be "more comprehensive".
5. Stop using a sales, advertising, storytelling or emotionally exaggerated style.
6. Stop adding only an authoritative voice without adding evidence.
7. Stop letting structured data contradict the content visible on the page.
8. Stop overhauling, in one go, a page that was being cited steadily.
9. Stop sacrificing accuracy to be seen: getting cited more and misreported more is not worth it.
10. Stop believing "one trick boosts you 40%" lists, and stop assuming the FAQ format or structured data on its own can make AI choose you.

## What is still uncertain

1. **Does original evidence have a causal effect on real AI search?** "Raising the evidence density of the whole page" works in simulations, and industry reports also support original numbers, but there is no causal evidence yet on real AI search.
2. **How much does structured data really do?** It can help with being fetched, and it correlates with being cited; but a randomised controlled test saw no effect from formatting, and there are websites with no structured data at all that are still cited heavily. What we can say for now is: being readable is not the same as being chosen.
3. **Can structured presentation raise "will it be cited at all?"** It can take some citations from equivalent sources, but whether the main measure improves can't be determined.
4. **Does the FAQ format itself deserve any credit?** Industry success stories all involve several changes made together, so the credit can't be assigned to the format alone.
5. **How confident should the tone be?** Clear statements backed by evidence seem to help, and an authoritative voice with no grounds may hurt; but some industry reports had no control group, so it may have been coincidence.
6. **How do you balance freshness against page age?** Newer dates have a strong advantage, but the most-cited pages are older ones that keep being updated; and updating itself may temporarily disrupt existing citations.
7. **Top summaries, length, publishing volume.** Top summaries showed a small benefit in some simulations, but had no effect in industry tests; both long and concise content have observed successes; publishing in bulk worked on one AI and actually declined on another.
8. **How big is the effect of short paragraphs?** There is only preliminary evidence; the size of the effect is unknown.
9. **Does automatic optimisation sacrifice answer quality?** While visibility rose sharply, answer precision fell on at least one engine.
10. **Preferences change with domain and engine.** Automatically summarised rules overlap only about 35% to 40% across domains; what works today may not work on the next generation of engines.
