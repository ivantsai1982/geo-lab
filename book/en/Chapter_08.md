# Chapter 8: Writing Tricks Have an Expiry Date Too

## A hypothetical story

Imagine that An is a marketer at a small software company. She read a piece on "secrets to getting AI to cite you". It advised putting in more statistics, quoting more experts and adding more reference sources, and claimed that doing this could raise your chances of being cited by AI by 30% to 40%.

An spent two weeks revising all twenty articles on the company website. At the bottom of every article she added a "data box", and she also put in a few expert quotes. A month later, she asked AI the same question, and her company still wasn't in the answer.

An wasn't lazy, and she didn't get any steps wrong. She had simply been handed a prescription that had already expired.

This chapter makes just one big point: **writing tricks expire; what doesn't expire is aiming at the question, staying true to the facts, and making the key points easy for both people and machines to extract.**

## Which gates this chapter deals with

Recall the book's seven gates. This chapter assumes two things first: your web page can already "get in the door", so accessibility is not a problem, and it has already been indexed by search engines. On that basis, the chapter asks only one question: for the same web page, does the way the content is written or revised change AI's chances of citing it, and how much it cites it? But let us be clear from the start: this precondition is not minor at all. In the tests closest to the real world, whether the page has been indexed and whether its website can be found matter more than how the content is written, as Debate 1 in Section 6 will discuss.

This question falls mainly on three gates. Gate four, "will it pick you", decides whom AI chooses from the shortlist and where it ranks them. Gate five, "will it mention you", decides whether your name or link appears in the answer. Gate six, "does it actually use you, and use you correctly", concerns how much of your content is written into the answer and whether it is paraphrased correctly. We will also look back at gate three, "can it find you", because revising content sometimes gets you eliminated at the retrieval gate, something many people never consider.

The chapter answers five questions in turn. First, why the 2023 fashion of "add statistics, add quotes, add reference sources" no longer works on today's AI. Second, if most tricks thought up by people have stopped working, what do machines find when left to search for the best way to write? Third, how much evidence there is for freshness, structure, structured data, Q&A format, short paragraphs, an authoritative tone and keyword stuffing, and which gate each one acts on. Fourth, what side effects content optimisation has, and when more optimisation makes things worse. Fifth, where research and industry tests contradict each other, and how to make sense of it.

## 1. Where that "expired prescription" came from

In 2023, researchers put together the first batch of writing methods for getting AI to cite you more. The three best known were adding quotes, adding statistics and adding reference sources. These tricks were measured under one specific condition. The experiment at the time assumed your web page was already on a candidate list of only a few pages; the AI model of the day wrote an answer from those few pages, and the researchers measured how much the share "how many words in the answer come from you" changed before and after rewriting.

The report at the time looked impressive. Later, researchers retested these three tricks on ten newer AI models, and the results were completely different:

| Trick | Effect reported in 2023 | Retested on new models |
|---|---|---|
| Add quotes | +42.6 | -0.33 |
| Add statistics | +32.8 | -0.28 |
| Add reference sources | +27.7 | -0.79 |

The unit in the table is "percentage points of citation share". Back then, each of the three tricks raised your weight in the answer by about 28 to 43 percentage points. On the ten new models, none of the three increased citations; the figures sat around zero, and were even slightly negative.

### Why they stopped working

The first reason is that AI itself keeps changing. Models are replaced generation after generation, and with each new generation, the way it judges "is this text worth citing" changes too. In the book's metaphor, the librarian has been replaced, and the writing the old librarian liked is not necessarily what the new one likes. So a method that worked on an old model is no guarantee of working on a new one.

The second reason is that when everyone uses it, it stops working. This is called the "crowding effect". Imagine an exam where the whole class has memorised the same set of predicted questions: those predictions are no longer anyone's advantage. The more websites adopt the same kind of rewriting, the less each adopter gains, until it approaches zero and becomes a zero-sum contest where your gain is someone else's loss. Simulation studies also found that once enough people adopt it, sticking stubbornly to a single trick can even perform worse than not optimising at all.

The third reason is that the experimental conditions back then were too lenient. In an experiment where the candidate list is fixed, your rewritten article only has to beat the other four on the list. The experimental process back then was short: you were already among 5 candidates, you rewrote, AI wrote the answer, and your share went up. Real AI search is a whole pipeline instead. It starts with the question, then fetches material (retrieval), then reranks, then AI writes the answer, and only at the end comes citation. The same rewritten article may fall behind at the fetching or reranking step, and never get as far as the step where AI writes the answer.

Another problem lies in what is used to do the scoring. Under test conditions with given web pages, researchers published the same set of rewritten product pages on a real website, then gave the URLs to three commercial AI search engines and asked them to open the pages, read them and rank them. At the same time, they gave the same text directly to five AI models to score. The rankings from the two approaches did not match well: within the same brand, the correlation coefficient ranged from 0.50 to −0.31, where a negative number means the opposite direction. One model's rankings ran in the opposite direction to all three AI search engines. Overall, "which rewrite is strongest" more or less held up, but at the level of individual brands, even the three AI search engines picked the same first place only about half to two-thirds of the time. So the effects measured by giving text directly to AI models cannot be taken as effects on real AI search.

The conclusion is that **any writing trick should be treated as "a hypothesis with an expiry date", not as a law.** If you want to keep using it, you have to measure it again on today's AI.

> **A closer look: how reliable is this retest?**
>
> Under test conditions with given web pages, researchers retested the three tricks on ten new models, and none of the three moved citations. Without statistical correction, the figure for "add reference sources" was nominally negative, meaning it looked slightly worse, but it cannot yet be said to be truly worse. They repeated the test on three models of the latest generation, and the result was again zero, or nominally slightly negative.
>
> Two limitations should be stated honestly here. First, the researchers who did this retest themselves provide a content-scoring service, so there is a conflict of interest. Second, their method "attached the quotes and statistics as a separate block" rather than working them into the body text.

### Other studies point in the same direction

Besides the retest above, there are several simulation studies. In a simulation study, researchers run experiments in a test environment they built themselves. It can show "this is how the mechanism might work", but that does not mean the real world is necessarily like this.

One of these studies paired various rewriting methods with different domains, 54 combinations in all. Only 3 of them produced a statistically credible improvement in citation ranking, and in question-answering tasks, none of them worked. Adding statistics more often backfired: in 19 of 24 scenarios it noticeably lowered the ranking instead. By comparison, placing a document in the first position of the material AI reads brought far greater benefit than any content-rewriting method, which shows that position matters more than rewriting.

Shopping recommendations look much the same. In an e-commerce reranking scenario, researchers tested 15 writing tricks designed by people. Only 4 slightly beat or tied "one simple prompt"; the other 11 all fell short, and the "storytelling" rewrite scored -4.36. As for small changes that only swap words and phrases, researchers tested 9 kinds, and on three AI engines all of them did worse than the original text with no rewriting at all.

Most of these studies were done in environments where the candidate material was fixed or controlled. Together they show that **tricks that attach something or only swap wording are unreliable.** But this does not mean "evidence and data are useless", a point the debates later in the chapter will discuss in detail.

### The closer to reality, the less the tricks show any effect

The retest above gave the candidate text directly to AI models. Two later studies moved the test conditions a step closer to the real world, and the three sets of results line up neatly.

The first was done under test conditions with given web pages. Researchers invented 80 brands, each with 6 product pages whose specifications were exactly the same and whose descriptions differed only in how they were written. They published these pages on a real website, then gave the URLs to three commercial AI search engines and asked them to open the pages, read them and rank them. Pages that added statistics through a whole-page rewrite had an average rank of 3.18, 3.31 and 3.83 on the three AI search engines, all better than the plain unrewritten originals (5.28, 5.84, 4.88); but the share that actually came first was only 10.0%, 11.3% and 5.0%, far behind the best-performing rewriting method. Even more striking, all 80 descriptions with added statistics contained numbers that the product specifications did not support at all, such as "18% better heat retention", and the AI search engines did not check them.

This study has several limitations that need to be stated honestly. The URLs were handed to AI directly by the researchers, so it was not tested whether AI could find these pages on its own. The originals used for comparison were plain text generated from a template, which is easy to beat in the first place. Some of the researchers are themselves authors of the best-performing method, so there is a conflict of interest. The results were not very stable either: rerunning the same conditions changed the first place for about 20% of brands, and merely reversing the order of the URLs, without changing a single word of content, made the best method's first-place share swing between 73.8% and 93.8%.

The second study is closer to reality. Researchers tested repeatedly on real AI search, choosing 56 topics with almost no other reliable content, which the industry calls "data voids". For each topic they published just one web page, let search engines index it on their own, and on day 25 after it went live asked three AI search engines. Whether the page used GEO writing, meaning statistics, sources cited in the text, an opening summary, technical terms and safety notes all added together, showed no effect at all on whether the page entered the answer: the odds ratio was 0.91, very close to 1, and the study ruled out an effect of "twofold or more". What really mattered was whether the website itself could be seen. New websites that had not been indexed appeared 0% of the time on all three AI search engines; pages on old websites appeared 38.4% to 78.3% of the time; and new websites that actively submitted themselves for indexing appeared 14.3% to 42.9% of the time.

This study has limitations too. Pages with and without GEO writing numbered 46 to 10, an uneven split, so only large effects can be ruled out, not smaller ones. The topics were all data voids with no competing sources, and the content was entirely fictional. And "whether the website can be seen" bundles together the website's age, its existing links and indexing, so it is impossible to tell which of them is doing the work.

Put the three kinds of evidence side by side and the picture is clear. When text is given directly to AI models, the effect of adding statistics has already become zero or slightly negative. When real AI search reads web pages supplied by researchers, adding statistics still beats a plain original, but the numbers are made up, and the results shift with order and with reruns. When real AI search has to find pages on its own, writing tricks show no effect. **The closer the conditions are to the real world and the stronger the evidence, the weaker the evidence that writing tricks help; whether your page has been indexed and whether your website can be found matter more than how you write.** In addition, AI search does not check numbers: made-up numbers are a real way of misleading readers, and a reputational risk for the writer.

## 2. What machines found when left to search for the best way to write

Since most tricks thought up by people had stopped working, researchers tried another approach: let AI try all kinds of rewrites itself and see which gets cited most. Several research groups arrived at the same direction. The writing that automatic optimisation finally converged on had only three features.

The first feature is staying true to the facts: no exaggeration, no invention, and no piling on emotion. The second is aiming at the question: responding directly to what the user is asking, in the user's own words, which the industry calls "query alignment". The third is clear structure: using bullet points and sections so that information is easy to extract.

One experiment shows this especially well. In an e-commerce scenario, researchers first had AI optimise a prompt whose goal was to manipulate product rankings. Then they added just one simple defensive rule to the system. As a result, the prompt that had been meant to manipulate the ranking shifted by itself towards a fact-stating style, and the share flagged as "manipulation" fell by 60 percentage points on average. **As long as AI has basic defences, the cost of manipulation outweighs the benefit, and honest, clear writing becomes the best solution.**

However, this conclusion comes from a simulation with a defensive rule added. Under test conditions with given web pages, three commercial AI search engines showed no such defence. The best performer was a method that adjusts appended text based on ranking feedback, and it had used the actual rankings of one of these AI search engines as feedback; some of the researchers are also authors of this method. Rewrites containing unsupported numbers were not ranked lower for it either, as Section 4 will discuss.

This matches the point made in Chapter 6 of this book. What AI prefers is not some writing gimmick, but content that matches the question, can be extracted and can be trusted.

### Preferences differ by domain, and matching the question comes first

The preferences machines work out change with the domain. Researchers had machines automatically work out "what kind of content AI engines like". When the model was switched, the rules they arrived at still overlapped fairly well, at about 79% to 84%. When the domain was switched, for example from e-commerce to general question answering, the overlap fell to only about 35% to 40%. So writing that works for others in another industry won't necessarily work in yours.

Another study shows that matching the question matters more than writing well. Researchers compared two ways of scoring. The first looked only at how well the content itself was written, regardless of what the user asked. The link between this "content quality score" and actually being cited was weak, with a correlation coefficient of about 0.11. The second measured whether the question and the source matched, and this score had a clearly stronger link with being cited, about 0.35 to 0.39. A correlation coefficient is a number between 0 and 1; the closer it is to 1, the more often two things occur together. To put it another way, the busy librarian is looking for a book that can answer this question, and the most beautifully written book is not on his priority list.

> **A closer look: automatic optimisation has its costs too**
>
> In an experimental system that researchers could control, using "engine preference rules" worked out automatically by machines to guide rewriting raised visibility from 20.18 to 43.76 on one engine, and the other two engines also improved noticeably. But on one of the engines, answer precision fell from 96.51 to 84.98, so the claim that "this kind of rewriting doesn't affect answer quality" does not fully hold. In a simulated e-commerce analysis, automatically optimised prompts improved 63 of 75 test cells, and the size of the improvement had nothing to do with the length of the product description.

## 3. Different content elements act on different gates

Many people think every content adjustment is a "get AI to cite me" button. In fact, each one does its work at a different gate. The "structural fields", meaning titles, page descriptions (meta), subheadings and structured data, together with short paragraphs and covering the words AI will use after it rewrites the question, act mainly on gate three: can it find you. Matching the topic and putting the answer first act mainly on the reranking at gate four. Freshness, topic alignment and clear statements backed by evidence act on gate five, deciding whether AI mentions you. Definitions, numbers, comparisons and steps relate to gate six, affecting how much of you the answer uses. Below we look at each one in turn, and at how strong the evidence for each is.

### Freshness, and content that can be used directly

Freshness is currently the item with the most consistent evidence, and two kinds of evidence point the same way. In controlled experiments, researchers ran about 252,000 simulated trials and found that for the same content, the version labelled with a newer date had 14.4 times the odds of being selected compared with the version labelled with an older date, and under some conditions more than 10,000 times. The "odds ratio" here is exactly this kind of "how many times" comparison.

Researchers also ran repeated tests on real AI search, on Chinese-language AI search engines, covering about 160,000 citations in all. For highly time-sensitive questions, the median age of cited web pages was 18 days, and the citation "half-life" was 39 days, meaning that after about 39 days, the chance of such pages being cited drops by half. For weakly time-sensitive questions, the median age was 101 days and the half-life was 68 days. So **freshness works, especially for time-sensitive questions, and the evidence is fairly strong.** But Debate 5 later will show a twist: the most frequently cited pages are not newly published articles.

Another finding concerns absorption. Web pages containing definitions, numbers, comparisons and steps were absorbed into AI answers 41% to 77% more. But this is a descriptive analysis researchers did of real AI answers. It only shows that the two things often occur together and does not rule out other possible causes, so the evidence is on the weak side. It points the same way as the experimental results for "raising evidence density across the whole page".

### Structure and structured data: they help you be understood, not help you be chosen

There are actually two kinds of "structure", and they need to be looked at separately. The first is structural fields, including titles, page descriptions, subheadings and structured data (such as schema markup). They help AI's retrieval systems find you. In an experimental system researchers could control, using about 171,000 real web pages, changing the structural fields raised the chance of being retrieved by about 22%, but at the next step, reranking, performance still fell. This evidence is of medium strength.

The second is body-text layout: adding lists, adding subheadings, organising information into a block. In controlled experiments, layout had almost no effect on who gets cited. Its odds ratio fell between 0.79 and 1.68, sometimes slightly below 1 and sometimes slightly above 1, with no consistent direction. Changing only the layout doesn't work.

The items within the structural fields also differ in effect. A large-scale study covering 158,000 answers compared different pages within the same website. It found that when paragraphs matched the user's question, citations were clearly higher: each additional standard deviation brought 15.5% more citations. When titles matched the question, citations were 14.1% higher, but this had no effect on ChatGPT. FAQs, structured data, summary boxes and page speed all looked effective when different websites were compared with each other (+7.5% to +20.9%), but within the same website none of them was noticeable (−5.3% to +6.9%), because these practices mostly appear on large websites that are already cited a lot. So the role of title wording is to match the question, and structured data cannot be treated as the reason AI cites you. This is a correlational study using small models, and the authors themselves run an AI monitoring platform.

Simulation studies also show that rewriting without specifying whom to highlight is almost useless. Of 36 settings, none was effective after correction, and roughly a quarter actually helped competitors. When a target was specified, half were effective after correction. Structural and argument-based rewrites worked best and switching to technical jargon worked worst, but the gain was only 0.5 to 1.5 percentage points.

More importantly, structured presentation only redistributes citations; it does not make the whole pie bigger. When several sources of similar content exist for the same fact, researchers used replay experiments asking "what would happen with a different way of presenting it" and found that structured presentation can get the target page a few more citations, about +0.50, but the total number of citations across all sources did not increase. The extra came from other comparable sources. As for the most important measure, "whether it gets cited at all", the credible range of the improvement crossed zero, which means it cannot be determined whether there was any improvement. This evidence is of medium strength.

On real AI search, an observational audit of business software (B2B SaaS) websites covering 1,702 citations found a correlation coefficient of 0.63 between structured data and being cited. But this is only a correlation, and the audit looked only at cited pages, with no uncited pages for comparison. Taken together, **structure acts on the two steps of "being found" and "being extracted"; it is not in itself a lever for getting AI to cite you.**

### Q&A format, short paragraphs, authoritative tone and keywords

Many people think that turning an article into questions and answers will do the job, but the data does not support it. Pages in Q&A format were absorbed 5.74% less than ordinary pages, and this is descriptive evidence. In experiments with self-built websites, the Q&A format also had no clear advantage. Together, the strength of this evidence is weak to medium. What really relates to absorption is whether the page contains content that can be used directly, such as definitions, numbers and comparisons.

Short paragraphs have preliminary evidence. Someone built 450 websites of their own to test on real AI search, and short paragraphs and sectioning performed best. But that figure represents "among the cases that succeeded in getting exposure, what proportion used short paragraphs", not "if you use short paragraphs, what is the probability of success", so how large the effect really is remains unknown for now.

An authoritative tone is not recommended. Rewriting in an "expert voice" gives unstable results and may make AI see you as less credible. This conclusion comes from a simulated analysis with AI acting as the scorer, so the evidence is on the weak side.

Keyword stuffing is the only item in this section with no controversy. Tests on real AI search, together with several simulation studies, agree: keyword stuffing doesn't work, and can even do harm.

Put side by side, these pieces of evidence vary greatly in strength. Freshness has two kinds of evidence, repeated testing on real AI search (Chinese-language engines, about 160,000 citations) and simulation experiments (252,000 trials), pointing the same way, so it belongs to the stronger group. Structural fields helping you get retrieved rests on a controllable experimental system (about 171,000 real web pages) and is of medium strength: the chance of being retrieved rose by 22%, but reranking still fell. The link between structure and being cited comes from an observational audit of 1,702 citations of business software websites on real AI search; it is only a correlation, and only cited pages were examined. Structured presentation merely redistributing citations comes from a controllable experimental system that included replay experiments; it is of medium strength, and the main measure is uncertain. The evidence for short paragraphs comes from 450 self-built websites on real AI search and counts only as preliminary; the figure is a share among successful exposures, not a success rate. The evidence for definitions, numbers and comparisons comes from a descriptive analysis of real AI answers and is on the weak side, because other causes were not ruled out. The Q&A format having no advantage comes from descriptive analysis plus self-built website experiments, weak to medium. An authoritative tone being harmful comes from a simulated analysis scored by AI, on the weak side. Keyword stuffing not working is the consistent conclusion of real AI search tests and several simulation studies.

## 4. Optimisation has side effects too

Content optimisation does not bring only benefits. The known side effects fall into four types.

The first type is that looking after one question hurts others. A web page usually has to respond to several related questions. If you adjust it for just one of them, 30.6% of the questions that were not the target get worse.

The second type is that being seen more also means being misreported more. Automatic rewriting aimed at raising visibility caused two scores to drop noticeably. One is faithfulness, meaning whether what AI paraphrases matches the original text, which fell from 8.29 to 4.90. The other is attribution accuracy, meaning whether AI credits a claim to the right source, which fell from 6.15 to 4.18. The page was seen more, but it was paraphrased correctly less.

The third type is falling behind at an earlier gate. In the full pipeline, changing only the body text lowered the chance of a page being retrieved by about 9%, and lowered the chance of it being kept during reranking by about 16%. Automatic rewriting that greatly expanded the content lowered the chance of being retrieved by about 36%, and rewrites that replaced the original wording with obscure or technical terms suffered the greatest loss.

Add it all up and the picture is clear. Changing only the body text may gain you a little at the step where AI writes the answer, but with 9% less retrieval and 16% less in reranking, the net effect is **a citation rate of -6%**. It is like a job seeker who, to shine more in the interview, makes their CV long and flashy, and then fails even the paper screening.

The fourth type is that made-up numbers are not stopped. Under test conditions with given web pages, one "add statistics" rewrite was allowed to use "hypothetical data", and as a result all 80 product descriptions contained numbers not supported by the specifications, such as "18% better heat retention"; other automatic rewriting methods also occasionally produced unsupported comparisons such as "30% energy saving". The three commercial AI search engines did not push them down the ranking for it, and the rewrites with added statistics still had a clearly better average rank than the unrewritten originals. Being seen and being reported correctly are two different things. Fake numbers written into a web page get passed on by AI: for readers they are a real way of being misled, and for the writer they are a reputational risk.

## 5. Don't celebrate yet: the measurement itself wobbles

Remember the book's "rolling dice" metaphor? Ask the same question ten times and the answers may differ. In a controllable experimental system, researchers found that about 15% of AI's single decisions on "whether to cite this page" flip when run again, and about 45% of the measured differences in effect actually came from the randomness of AI generating text.

Someone in the industry ran repeated, controlled tests and, before making any change, first measured how much the results wobble on their own. He tested with 387 questions, and after 3 days, 98% gave the same results. So he believes that changes smaller than about 3 to 4 percentage points should be treated as measurement noise, not as an effect.

The same wobble exists on real AI search. Under test conditions with given web pages, rerunning the same pages in the same order on ChatGPT changed the first place for about 20% of brands; merely reversing the order of the URLs, with the content completely unchanged, made the best-performing rewriting method's first-place share swing between 73.8% and 93.8%. Product names, a tiny price difference (±0.2%), and whether AI was given a brand overview page or individual product pages also changed the results. So when you measure, record these conditions and rotate them.

This means that **testing only once, seeing a change of a few percentage points, and declaring that some way of writing works, is unreliable.**

## 6. Seven questions still under debate

What research says and what industry tests say often contradict each other. Look closely, and most of the contradictions arise because the two sides are not talking about the same thing.

### Debate 1: Do statistics and evidence actually help?

The side that says they don't has two grounds. On new AI models, attaching a block of statistics does not increase citations. In simulation experiments, adding statistics often lowered the ranking, and credibility as scored by AI also fell from 8.352 to 7.613.

The side that says they do also has research support. In simulation experiments, rewriting the whole page to raise the density of statistics and reference sources increased visibility by 37% to 96%. When researchers removed each change one at a time for comparison, they found that statistics and reference sources contributed the most. In another simulation, adding statistics had an effect of +3.49, and among all the writing tricks, the "add evidence" kind of change was the strongest. The two sides actually rest on different grounds: the side that says they don't help tested attaching a block or only swapping wording, while the side that says they help tested raising evidence density when rewriting the whole page.

Another study, in which researchers tested repeatedly on real AI search, saw both sides. In real usage logs, pages with statistics, sources cited in the text and accurate wording were retrieved and cited more often: pages with statistics had an odds ratio of 2.11 for being retrieved and 1.17 for being cited; for sources cited in the text the figures were 1.34 and 1.22; for accurate wording, 2.26 and 1.71. Fluently written pages were actually retrieved and cited less often (0.67 and 0.58). But all of these are only correlations. When the researchers added these elements to pages directly in a controlled experiment, no effect could be seen, and which website a page was published on mattered far more than how it was written.

Industry tests offer two observations as well. Someone in the industry tested this themselves: he produced an original study auditing the AI visibility of more than two thousand training companies, and this study became the only page on his website that Perplexity listed as its first source. He therefore believes that original figures are currently the strongest "worth citing" signal, but no one has independently verified this. Another person in the industry looked at about 150 websites and found that the median share of paragraphs containing numbers, quotes or external links was only 23/100, so most websites' paragraphs actually contain very little evidence.

**"Pasting numbers in" and "the content already containing evidence not found anywhere else" are two different things.** The former has been shown to be unreliable. The latter is currently supported only by simulation experiments, industry reports and correlational evidence on real AI search; on real AI search there is not yet any causal evidence.

There is also a third case: writing numbers the specifications do not support into the body text. Under test conditions with given web pages, this kind of rewrite can beat a plain original, but it falls short of other whole-page rewriting methods, and it amounts to handing false information to AI to pass on. It is not evidence, and it should not appear in any recommended practice. For the three kinds of evidence side by side, see "The closer to reality, the less the tricks show any effect" in Section 1.

### Debate 2: Does structured data help?

The supporting side has several grounds. In a controllable experimental system, structural fields including structured data raised the chance of being retrieved by about 22%. In an observational audit, the correlation coefficient between structured data and being cited was 0.63, but that is only a correlation. Someone in the industry tested this themselves: comparing business software websites with similar traffic, websites with complete structured data were cited about twice as often as those without. Another person in the industry observed that after filling in the structured data for a product with several variants, AI went from picking up only the price of the default variant to correctly listing the price of each variant.

The sceptical side has tests too. Someone in the industry ran a randomised controlled test on 318 pages and found no statistically credible improvement from Markdown formatting; he also believes structured data is not the main lever. Someone in the industry tested this themselves: on the same test page, the price written in the structured data was 199.99 and the price visible on the page was 349.99, and both ChatGPT and Gemini showed the visible 349.99. Yet another person in the industry observed that one of their websites has no structured data at all and still receives about 55,000 citations a month from search engines' AI features. Many in the industry believe that structured data on its own has limited effect, and that adding it casually or incompletely does nothing, but "many people believe" does not mean "it is right".

A more reasonable reading is that the role of structured data is to help machines understand what you already have: it helps retrieval and helps AI tell which entity you are, but it is not responsible for getting AI to choose you. Someone in the industry summed it up in one sentence: **being understood is not the same as being chosen.** And when structured data conflicts with the content visible on the page, at least in the test above, AI trusted the visible content.

### Debate 3: Does the FAQ format help?

On the research side, the results lean negative. Q&A pages were absorbed 5.74% less than ordinary pages, which is descriptive evidence; in self-built website experiments, the Q&A format also had no clear advantage.

On the industry-testing side, there are success stories. Someone in the industry tested this themselves: they rewrote 8 comparison pages so that "under each second-level subheading, one question is fully answered within 300 characters", and added FAQ structured data. Within 6 weeks, on 12 target questions, ChatGPT's citations went from 0 to 4. Another industry test added FAQ structured data, a summary at the top of the page and a comparison table, and also posted on social media; afterwards, across 60 questions, appearances rose from 4 to 25.

There is one key counterexample. Someone in the industry tested this themselves: FAQ questions written to match keywords were completely ignored by AI, and only questions written in the sentences real people actually type got cited. Industry success stories almost always involve several changes made together, so the credit can't be assigned to the FAQ format alone. And the detail of "asking questions the way real people do" actually points to the **query alignment** discussed in Section 2, and has little to do with the format itself.

### Debate 4: Should the tone be confident or cautious?

Under laboratory conditions, an "authoritative-voice" rewrite lowered credibility as scored by AI from 8.352 to 7.332, and in the e-commerce scenario an authoritative voice was also on the list of ineffective tricks. But another controlled experiment found that clear statements backed by evidence help a page get cited, while vague wording, and content that contradicts itself, lowers the chance of being cited.

The industry side offers two observations too. Someone in the industry tested this themselves: they rewrote 8 articles into clearer, easy-to-quote assertive sentences, and within two months two topics that previously had no visibility at all began to be cited. But there was no control group this time, and the author themselves suspects it may have been coincidence. Another person in the industry ran repeated, controlled tests and found that after cutting back on hedging words such as "however", "although" and "even though", citations became more stable.

So **the problem lies in whether there are grounds, and has little to do with how confident the tone is.** Clear statements backed by evidence and an authoritative voice without grounds may have effects in exactly opposite directions.

### Debate 5: Newer is better, or older is steadier?

We have already seen the evidence for "new". Research shows newer dates have a strong advantage, and the citation half-life for time-sensitive questions is only 39 days. Someone in the industry tested this themselves: they deliberately stopped updating a page for two months, and ChatGPT stopped citing it entirely, citing instead a short post on a professional networking platform that was newer and answered more directly.

There is plenty of evidence for "old" as well. Someone in the industry tested this themselves: of 356 cited pages, the median age was 23 months, and only 35% had been created less than a year earlier, but the median "last updated" date was 5 months earlier. Another industry test found that about 43% of articles published more than two months earlier were cited, against only about 7% of new articles. Yet another person in the industry observed that when cited pages were first recorded as being cited, their median age was 203 days, and only 9% were less than a month old. There are counterexamples too: someone in the industry observed that after they updated a page that had been cited steadily, its citations dropped noticeably, recovered only partly after a few weeks, and did not return to their original level.

"Fresh" may be two different things. One is that someone has maintained the page recently, which favours pages that already exist. The other is that the page has just been published, and new pages often need time to build up. The most consistent pattern in the data is that **pages that have existed for some time and keep being updated are cited most often.** At the same time, updating carries its own risk: a major overhaul of a page may temporarily disrupt the citations it already has.

### Debate 6: Top summaries, long content, publishing in bulk

First, top summaries. In simulation studies, putting a summary before the content brought a small but credible benefit in two domains, retail and games; in a controllable experimental system, putting the answer first helped with reranking. But someone in the industry tested this themselves and found that adding a "key points summary" at the top of the page had no effect.

Next, length. In simulation studies, the benefit of optimisation had nothing to do with the length of the description; in a controllable experimental system, greatly expanding content lowered the chance of being retrieved by about 36%. Industry observations go both ways: someone in the industry observed that strong brands tend to publish long content of over 2,000 words, while someone else in the industry observed that after making their content more concise and more factual, they won a place in the AI summary.

Finally, publishing pages in bulk. Someone in the industry ran repeated, controlled tests: after publishing a large number of new pages on separate topics, the share of ChatGPT answers recommending the brand rose from 11.9% to 23.1% within six weeks, but over the same period Claude's recommendation share fell by 4.1 percentage points. Another person in the industry observed that publishing three articles a week for two months, adding structured data and submitting to various directory sites for listing made almost no difference to citations.

These three things can be understood this way. "Putting the answer first" and "adding a summary at the front" are two different things: the former changes how each section begins, while the latter just adds one more block of text. Length itself is not the key either; **whether each section can answer one question on its own** is. As for whether publishing a large number of pages helps, that depends on whether each page corresponds to a question that really exists and has not yet been answered well.

### Debate 7: Does good writing matter?

Someone in the industry tested this themselves: auditing 158 articles, the average quality score of cited articles was 60.4 and that of uncited ones was 62.5, so the ignored articles were actually slightly better written. Another person in the industry ran repeated, controlled tests and found that across 200 articles and 3 AI engines, the quality scores given by editors had almost nothing to do with being cited. Many in the industry believe that only content with a viewpoint worth citing or useful information gets cited.

"Quality" here mostly means writing style and editors' scores. What AI values is matching the question, being easy to extract, and offering information not found elsewhere; fine phrasing is not among them. This points the same way as the research result in Section 2 that "content quality scores that ignore the question have only a weak correlation with citation".

## 7. Six real cases

The following cases all come from first-hand reports by people in the industry, and no one has independently verified them. They are used to illustrate the points and cannot be taken as proof.

The first case is short. Someone in the industry deliberately stopped updating a page for two months, keeping the topic and keywords unchanged, and watched how ChatGPT responded. ChatGPT stopped citing the page entirely and cited instead a short post on a professional networking platform. The author of that short post had only 300 followers, but the post was newer and answered more directly. This shows that freshness is a strong factor at the "will it mention you" gate; but "answered more directly" was also at work, so the cause can't be put down to freshness alone.

### A B2B client, from 0 to 7/10 in 12 weeks

The second case is a business-to-business (B2B) client. At the start, 7 of 10 target questions already ranked on the first or second page of traditional search, but the client had zero citations in the AI summary. They worked on it over three months. In the first month they reviewed the content and restructured it so that each page opened with a direct answer to the question, and added FAQ structured data to 8 target pages. In the second month they worked on getting other websites to mention them, going from 2 to more than 12. In the third month they kept the content fresh and monitored continuously. The main platform tracked was Google's AI summary, and they also looked at Perplexity.

On day 18, the first AI summary citation appeared. By week 12, 7 of the 10 questions produced citations, while traditional search rankings did not change at all. FAQ questions written to match keywords were completely ignored, and only those written the way real people speak were used. The remaining 3 questions, held by big brands, never broke through. This case shows that putting the answer first helps with reranking, and that aiming at the question matters more than format. It also shows that revising content alone can't close a gap in third-party sources, which the chapter of this book on third-party sources discusses in detail.

### Four experiments by a website-building platform

The third case is four experiments run by a website-building platform. They rewrote their blog into articles that answer real users' questions, and within 3 weeks, share of voice on the tracked questions rose from 38% to 100%, with 70% of tracked questions improving. After adding a table of contents, clicks rose by 23% within 4 weeks and visits from AI rose by 60%. After rewriting titles as questions, visits from AI rose by 58% within 4 weeks. Adding a "key points summary" at the top of the page had no effect.

The three that worked all had to do with aiming at users' questions and helping AI quickly find the right section. The one that didn't work merely added a summary block without changing the structure of the sections themselves, which matches the conclusion of Debate 6.

### Measure the noise first, then look at the effect

The fourth case was handled more rigorously. This person in the industry tracked the same set of 134 questions every week. The strategy was to publish a large number of new pages on separate topics, 458 in all, rather than rewriting old pages that already ranked; these pages were all plain HTML and did not depend on JavaScript. The platforms tracked were ChatGPT, Claude and Google.

Before making any change, he measured the noise first: 98% of questions gave unchanged results after 3 days, so changes smaller than about 3 to 4 percentage points were all treated as noise. Over about six weeks, the share of ChatGPT answers actively recommending the brand rose from 11.9% to 23.1%, with 24 questions going up and 9 going down; over the same period, Claude fell by 4.1 percentage points. Google listed the website as a source in 36% of its answers, but the share of answers recommending the brand was 0%. Claude copied as many as 64 consecutive words from the website, with the URL attached, but the recommendation list it gave still came from competitors' official websites.

This case shows that "being cited" and "being recommended" are two different states; that the same content strategy may have opposite effects on different AIs, echoing Section 1; and that before evaluating an effect, you must first know how large the noise is, echoing Section 5.

### An audit of 158 articles, and a price conflict

The fifth case is a content audit. This person in the industry reviewed 158 pieces of published content, audited 78 of them in detail against 28 criteria, and tracked them on ChatGPT, Perplexity, Google's AI summary and Claude. Writing quality made almost no difference: cited pieces averaged 60.4 points and uncited ones 62.5. With the same author and the same material, publishing in industry media gave a citation rate of about 52%, while publishing on the company blog or a personal web page both gave 0%. Question-style second-level subheadings raised citations by +19%, tables or lists by +18%, and a sales tone came in at -26%. About 43% of articles published more than two months earlier were cited, against about 7% of new articles.

This audit shows that where you publish (in other words, third-party sources) has far more influence than how you write; that a sales tone violates "staying true to the facts" from Section 2; and that new content needs time to build up, which matches the observations in Debate 5.

The sixth case is a deliberately created conflict. On a test page, someone in the industry made the price marked in the structured data (199.99) differ from the price visible on the page (349.99), then had ChatGPT and Gemini read it. Both showed the visible 349.99. At least in this test, AI went by the visible text, and structured data cannot replace the body text, which echoes Debate 2.

## 8. Sorted into three baskets

### Recommended, in order of strength of evidence

Before the nine items below, there is one precondition: first confirm that your web page has been indexed by search engines and that its website can be found, and only then think about the writing. Researchers tested repeatedly on real AI search (on data void topics): new websites that had not been indexed scored 0 on all three AI search engines, and how the pages were written showed no effect.

The top priority is to first confirm that your content corresponds to real questions, and to write titles and questions in the words users actually use. In controllable experiments and simulations, whether the question and the content match is the strongest predictor, and industry tests support this too. Match the question first, then think about the writing.

The second is to keep updating pages that already exist, and to update time-sensitive topics more often. This rests on repeated testing on real AI search and simulation experiments, pointing the same way; the half-life for time-sensitive questions is about 39 days, which can serve as a reference for your review cycle.

The third is to write the core entities and key figures into the structural fields: titles, page descriptions, subheadings and structured data. The basis is a controllable experimental system. Remember that this acts on "being found" and is not a lever for getting AI to cite you.

The fourth is to make each section open with the answer, so that every section can answer one question on its own. Controllable experiments show that putting the answer first helps with reranking, and many in the industry believe this too. What needs to change is how each section starts; adding a summary at the top of the page does not count.

The fifth is to break content into short paragraphs. There is preliminary evidence from real AI search, but that figure is a share, not a success rate, and the size of the effect is not yet known.

The sixth is to include evidence not found anywhere else, such as original data, definitions, comparisons and steps. The basis is simulation experiments, descriptive correlations and industry tests. This evidence needs to be worked into the body text, with sources and dates; attaching a separate block is useless.

The seventh is to use clear statements backed by evidence and cut unnecessary hedging. The basis is controlled experiments, plus repeated, controlled industry tests. Clear is not the same as exaggerated; where you have no grounds, don't force it into an assertion.

The eighth is to have one page serve several related questions rather than tuning it for just one. The basis is simulated analysis: tuning for just one question makes 30.6% of the other questions worse.

The ninth is to measure the noise before evaluating any change, and to record each AI engine separately. The basis is controllable experiments (15% of decisions flip) and repeated, controlled industry tests. Don't treat changes smaller than 3 to 4 percentage points as an effect.

### Myths: useless or harmful

Keyword stuffing is the clearest one. All the relevant research shows it doesn't work or does harm, and on real AI search it had no effect on any system. Replacing your original wording with obscure or technical terms is the rewrite that causes the greatest loss in "being retrieved" across the full pipeline; greatly expanding content to be "more comprehensive" also makes a page fall behind at the retrieval step.

A sales, advertising, storytelling or emotionally exaggerated style points to negative effects, with research and industry reports in agreement. This point concerns "being cited by AI"; simulation studies show that in Q&A communities, emotional, expressive answers are actually more likely to win votes from real people, but that is a different goal. Adding only an authoritative voice without adding evidence may lower credibility.

Letting structured data disagree with the visible content is another myth. AI may go by the visible content, and the conflict only creates confusion. A major one-off overhaul of a page that was being cited steadily is risky as well: someone in the industry observed that citations dropped for several weeks as a result and never fully recovered, so changes should be made in small steps and be reversible. Finally, chasing visibility at the expense of accuracy doesn't pay either. Rewriting aimed at visibility lowers faithfulness: you get cited more, and also misreported more.

In the same way, don't write unsupported numbers on your web pages. Under test conditions with given web pages, AI search did not check numbers, and rewrites containing fake numbers were not ranked lower for it. These numbers get passed on to readers: for readers they are misleading, and for the writer they are a reputational risk.

### Already outdated

Treating the trio of "add statistics, add quotes, add reference sources" as standalone tricks is already outdated. The +27% to +43% reported in 2023 became zero or slightly negative when retested on new models; under real retrieval conditions, GEO writing on the page also showed no effect. The same goes for any "one trick for a 40% boost" list: rewrites that only swap wording did worse than no rewriting at all in several studies, and the more people adopt them, the closer the effect gets to zero.

Treating the FAQ format or structured data as the main way to get AI to cite you is outdated too. They help AI understand you and find you, but they do not in themselves decide whether AI chooses you. The idea of "optimise once, effective forever" should also be dropped. Once an AI engine updates, known methods may expire, so you have to measure again regularly.

## Back to An

If An could start over, what she should do is not add another data box. She should first work out what questions customers really ask AI and in what words, and then make every article, and every section, answer that question directly, honestly and clearly.

If the company has data not found anywhere else, it should go into the body text, with the source and date noted. After that, update regularly, but don't overhaul everything at once. And after making changes, don't look at the results only once. First find out how much the "rolling dice" wobble on their own, and then judge whether you have really made progress.

Tricks expire. Aiming at the question, staying true to the facts and being easy to extract do not.

## Key points of this chapter

Writing tricks have an expiry date. The 2023 tricks of adding statistics, adding quotes and adding reference sources no longer increase citations when retested on new models. The closer the conditions are to the real world and the stronger the evidence, the weaker the evidence that writing tricks help, and whether your page has been indexed and whether your website can be found matter more. When machines are left to search for the best way to write, they converge on staying true to the facts, aiming at the question and clear structure. This is currently the direction closest to a "universal best solution", though preferences differ by domain.

Match the question first, then think about the writing. Whether the question and the content match predicts citation better than content quality that ignores the question, and how well something is written has almost nothing to do with being cited. Freshness is the content factor with the most consistent evidence, but the pages cited most often are those that have existed for some time and keep being updated; newly published pages are actually not cited often.

Structure and structured data act on "being found" and "being extracted". Structured presentation only redistributes citations among comparable sources and is not in itself a lever for getting AI to cite you. The Q&A format, an authoritative tone and keyword stuffing, used on their own, are all ineffective or harmful; FAQ success stories mostly come from aiming at the question in the words real people use, and have little to do with the format itself.

Optimisation has side effects. Tuning for one question hurts others, chasing visibility lowers faithfulness, and changing only the body text can make a page fall behind at the retrieval step, and AI search does not check numbers either, so made-up numbers are not stopped. Finally, a single test can't be trusted: about 15% of citation decisions flip when run again; on real AI search, reversing the candidate order or running again also changes who comes first. Before evaluating any method, measure the noise first, and record each AI engine separately.

## Remember in one sentence

**Writing gimmicks have an expiry date; what AI ultimately prefers is content that aims at the question, stays true to the facts, and makes one thing clear per section.**

## What you can do tomorrow

1. Confirm you are indexed first. Check whether your web page has already been indexed by search engines and whether its website can be found, and only after confirming this start changing how you write.
2. Match the question first. List the questions customers really ask, in their own words, and compare them with your titles and subheadings; rewrite questions written to match keywords into sentences real people would type.
3. Make every section able to answer a question on its own. Pick a few of your most important articles and rewrite the first sentence of each section so that it answers the question directly, rather than just adding a summary at the top of the page.
4. Break up long paragraphs so that each paragraph covers only one thing.
5. Write your structural fields well. Put your core entities (brand, products) and key figures into the titles, page descriptions, subheadings and structured data, and check that the structured data matches the content visible on the page, especially prices, specifications and dates.
6. Include evidence not found anywhere else. If you have original data, clear definitions, comparisons or steps, work them into the body text and note the source and date. Every number must have grounds; don't make any up.
7. Say things clearly, with grounds. Delete unnecessary "however", "although" and "even though", but where you have no grounds, don't force it into an assertion.
8. Have one page serve several related questions. Before rewriting, list all the related questions the page should answer, and after rewriting, check them one by one to see whether any got worse.
9. Set an update cycle. Keep maintaining pages that already exist; for time-sensitive topics, you can use the half-life of about 39 days as a reference when scheduling reviews. Update in small steps, and keep the old version so you can roll back.
10. Measure the noise first, then evaluate. Before making changes, ask the same set of questions several times, note how much the results wobble on their own, and record each AI engine separately; afterwards, don't treat changes smaller than 3 to 4 percentage points as an effect.
11. Treat every method as a hypothesis. After AI engines update, measure again regularly on the current engines.

## Stop doing this

**Stop "pasting" a data box or expert quote at the bottom of an article and assuming AI will cite you more.** Likewise, stop believing "one trick for a 40% boost" lists, and stop assuming that the FAQ format or structured data can on its own get AI to choose you.

Stop stuffing keywords, and stop replacing your original wording with obscure or technical terms. Greatly expanding content to be "more comprehensive" will likewise make a page fall behind at the retrieval step.

Stop using a sales, advertising, storytelling or emotionally exaggerated style, and stop adding an authoritative voice without adding evidence. Both may look persuasive, but in AI's eyes they may make you seem less credible.

Stop letting structured data contradict the content visible on the page, and stop overhauling a page that was being cited steadily all in one go. Finally, stop sacrificing accuracy to be seen: being cited more while also being misreported more is not worth it. And stop writing unsupported numbers on your web pages: AI will not check them for you, but readers will be misled and your reputation will suffer.

## What is still uncertain

**Does original evidence have a causal effect on real AI search?** "Raising evidence density across the whole page" works in simulations, and industry reports also support original figures, but on real AI search there is not yet any causal evidence, only correlational evidence.

**Does the way a page is written have no effect at all under real retrieval conditions?** The tests closest to the real world so far show no effect, but they ruled out only large effects of twofold or more, and they tested data void topics with no competing sources. In tests with given web pages, adding statistics still beat a plain original, but the results shifted with order and with reruns.

**How much does structured data really do?** It can help with being retrieved, and it is correlated with being cited; but a randomised controlled test saw no effect from formatting, and there are websites with no structured data at all that are still cited heavily. What can be said for now is that being understood is not the same as being chosen. A related question is whether structured presentation can raise "whether it gets cited at all". It can take some citations from comparable sources, but the improvement in the main measure cannot be determined.

**Does the FAQ format itself deserve credit?** Industry success stories all involve several changes made together, so the credit cannot be assigned to the format alone.

**How confident should the tone be?** Clear statements backed by evidence seem to help, and an authoritative voice without grounds may do harm; but some industry reports had no control group, so the results may be coincidence.

**How should freshness be weighed against page age?** New dates have a strong advantage, but the pages cited most often are older ones that keep being updated, and updating itself may temporarily disrupt existing citations.

**For top summaries, length and publishing volume, there are currently opposing observations.** Top summaries brought a small benefit in some simulations but had no effect in industry tests; both long content and concise content have successful observations; and publishing in bulk worked on one AI while falling on another.

**How large is the effect of short paragraphs?** There is only preliminary evidence for now, and the size of the effect is unknown.

**Does automatic optimisation sacrifice answer quality?** While visibility rose sharply, answer precision fell, at least on one engine.

**Preferences change with domain and engine.** Automatically derived rules overlap by only about 35% to 40% across domains; what works today may not work on the next generation of engines.
