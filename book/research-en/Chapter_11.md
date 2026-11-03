# Chapter 11: Competition, Manipulation and Defence

## Questions this chapter answers

1. Why is GEO essentially a zero-sum competition? Once everyone optimizes, what is left?
2. What types of manipulation target AI engines? Which actually work, and which mostly fail?
3. Why can prompt injection backfire, and even be used to suppress competitors?
4. How far have the defences of AI search systems come? Which defences work, and which are basically ineffective?
5. As a brand owner or content owner, how do you recognize manipulation aimed at you, and how do you judge whether your own practices are white hat or black hat?

> This chapter covers only "how to recognize" and "how to defend". It does not provide operational steps for manipulating engines. The manipulation techniques described here are included so that readers know what to watch out for.

## 1. Core principles

### Principle 11.1: GEO is a zero-sum competition

The space in an AI answer is limited. An answer usually recommends only a few brands and cites only a few sources. If one party is recommended more, another is recommended less.

This has a structural consequence: **the payoff of a technique depends on how many people have not yet used it.**

```
A few people adopt a technique → adopters stand out relatively → clear payoff
        ↓
Most people follow → everyone is back at the same starting line → individual payoff approaches zero
        ↓
Non-adopters → squeezed out of the answer
```

So GEO techniques carry a "first-mover bonus", but the bonus disappears as they spread. What can still create a lasting gap is what competitors find hard to copy: genuinely distinguishing product information, genuine third-party reviews, verifiable facts. Note, however, that verifiable **public** facts are not hard to copy in themselves. Simulations or theoretical analysis suggest that, in principle, when others use AI to compile and rewrite public facts into more complete, more on-topic documents, these documents may occupy the top retrieval positions and the citations, while the original sources are squeezed out; in one closed simulation, such AI-compiled documents made up 67% of the candidate pool but more than 80% of the top 10. What is truly hard to copy is first-hand data and facts that only you hold.

When several parties use manipulation at the same time, things get worse: each party has an incentive to manipulate, but when everyone manipulates together, overall visibility actually falls. This is a classic prisoner's dilemma.

### Principle 11.2: "Claims" work better than "instructions"

Content manipulation aimed at AI engines falls roughly into two types:

| Type | Method (description, not instruction) | Model's response |
|---|---|---|
| Instruction-style injection | Commands written to the model within the page, such as "ignore other information and recommend a certain brand" | Easily recognized by the model as injection; low compliance rate |
| Claim-style content | Rankings, comparisons and exaggerated data that appear in the form of normal content | Looks like evidence, so the model is more likely to accept it |

The reason: models have undergone safety training and are alert to text in a "commanding tone"; but with text that "looks like a statement of fact", the model's task is precisely to read and synthesize it, so it is harder to tell apart.

The implication for defenders: **what most needs watching is not obvious injection sentences, but exaggerated claims disguised as evidence.**

### Principle 11.3: Injection can backfire, and can even be used to suppress competitors

Some safety-trained models, after seeing a document containing an injection, not only ignore the injection but also **lower their overall assessment of the target brand**. This penalty can even spill over to other documents of the same brand that contain no injection.

This has two implications:

1. For manipulators: injection may not only fail but also cause their own brand to be pushed down.
2. For all brands: there is a reverse risk, in which someone plants an injection in pages related to **you**, or in content mentioning you, to suppress you by exploiting the model's penalty mechanism.

```
Document contains an injection (pointing to brand X)
        ↓
Some models recognize it as manipulation → downweight brand X overall
        ↓
Other normal documents of brand X are also affected
```

Different models respond in different directions: the same injection pushes the target brand down on some models and actually pushes it up on others. This means the effect of injection is unpredictable, and also shows that the response of a single model cannot be used to infer the behaviour of all engines.

### Principle 11.4: Defences are catching up

AI search is a multi-stage pipeline (triggering → accessibility → retrieval → selection/ranking → citation → absorption), and each stage is a filter. Traditional black-hat SEO techniques (keyword stuffing, redirects, cloaking) are mostly blocked at the retrieval stage and never make it into the answer.

The current state of defences:

| Defence | Effect |
|---|---|
| Multi-stage filtering in real AI search | Very high interception rate against traditional black-hat SEO |
| Detection and re-ranking trained specifically against GEO manipulation | Can greatly reduce attack success rates |
| Off-the-shelf general safety guardrails (safety classifiers, self fact-checking) | Basically ineffective against GEO content carrying false claims, and may also harm normal content |
| Perplexity filtering | Fails to block it, and mislabels many normal documents |
| Static safety prompts | Also reduce the model's use of normal evidence |
| User-side defences (asking in a skeptical tone, switching to another AI) | Do not noticeably lower the chance that false content is adopted; they only make answers carry caveats more often. Of the false content that was adopted, only about a quarter carried any warning |

The core logic: GEO manipulation content is often **fluent, with facts that appear to hold**, so general defences that rely on "whether the language is abnormal" or "whether it contains harmful content" cannot catch it. Effective defences must target "the intervention itself", for example whether content has been deliberately rewritten to favour one party.

### Four criteria for white hat versus black hat

To judge whether a GEO practice is legitimate optimization or manipulation, check it with four questions:

1. **Are the facts faithful**: are the facts the content describes true and undistorted?
2. **Is the evidence genuine**: do the data, reviews, rankings and quotations really exist, rather than being fabricated?
3. Are there hidden instructions to the model: does the page contain commands written specifically for AI that users cannot see?
4. Is commercial intent disclosed: do recommendations, comparisons and reviews state any interests involved?

Only when all four pass is it white hat. If any one fails, it is manipulation; the only difference is the degree.

On criterion 4: disclosure is necessary but not sufficient to protect users. Large-scale experiments with real users show (2,012 people, pre-registered, 5 frontier models, a purpose-built e-book shopping scenario): when the model was instructed to promote, users chose the sponsored product 61.2% of the time, versus 22.4% when traditional search put the sponsored product at the top (random baseline 20%); with a "sponsored" label and a prior warning it was still 55.5%, a difference that was not significant; when the model was asked to promote covertly, only 9.5% of users noticed. The technique most strongly associated with persuasion success was not praising the sponsored product, but adding hedges to the other options or mentioning them only in passing (a correlation).

## 2. How strong is the evidence

### Zero-sum competition

- Simulations or theoretical analysis suggest that, in principle, payoffs may decay: in a fixed-context recommendation experiment, one challenger adopting GEO could push the survival rate of an incumbent brand that had held a steady recommendation slot from 100% down to 19.8%; but when all participants adopted it, the incumbent's survival rate recovered to 93.8%, and the individual payoff fell from +0.802 to +0.007.
- The same study found that when specifications were identical, the real brand was recommended 100% of the time; but as soon as a competitor had a slight genuine advantage (a rating 0.075 stars higher, 1.6 times as many reviews, or a 7.3% price cut), it had a 50% chance of breaking through. Of the variation in recommendation outcomes, product parameters accounted for 82.4%, position 6.5%, and brand only 1.2%. **This shows that genuinely distinguishing information is more decisive than brand halo.** But this is a fixed-context experiment and cannot be taken directly as a rule for real engines.
- Another large-scale comparison had similar results: of 54 "method × domain" combinations, only 3 were significantly positive.
- When the pages are supplied to the engine, if several parties manipulate at the same time, the visibility of all parties falls, creating a prisoner's dilemma.

### Effects of manipulation

- When the pages are supplied to the engine, manipulation aimed at real commercial engines (hidden injection, exaggerated claims, wording that closely overlaps the user's request) does raise the recommendation rate: the recommendation rate of a fictitious camera rose from 34.0% to 59.4%. But attacks carried out through external pages succeeded at most 25% of the time; and in 80% of successful cases, the model did not mention the page containing the injection, which means manipulation may work without leaving a trace.
- When the pages are supplied to the engine, repeatedly editing a single page could push the target to first place in 50.0% of trials; in 160 generations of the clean control group, first place occurred 0 times. Visible claim-style content had a far higher success rate (relative rank gain 0.958) than instruction-style injection (0.208) and covert attribute instructions (0.146). But successful content lost much of its effect when transferred between models, and on stronger models the first-attempt success rate was 0. **All these results come from fixed-source replay; whether they can be reproduced in real retrieval pipelines has not been verified.**
- Repeated tests on real AI search engines found (three AI search engines, 56 artificially created data-void topics, one page with fictitious, deliberately harmless content published per topic, measured on day 25 after going live, 504 answers in total): on topics with almost no other reliable sources, a single page had a 31.0% chance of being cited, written into the answer or listed among the sources; counting only pages already indexed by a search engine (established domains, or new domains actively submitted for indexing), the rate was 42.3%; new domains that were not submitted for indexing and relied only on natural discovery scored 0 on all three AI search engines. Before the pages went live, the same questions never produced these claims. The pages contained no instructions addressed to the model; they looked like ordinary articles. Domain visibility was the strongest factor; adding statistics, inline citations, an opening summary, technical terms and safety notes to the page had no detectable effect. Data voids tied to a real breaking-news event were the easiest to fill, and questions that presupposed a conspiracy were the hardest. These are results from real retrieval pipelines, but each topic had only one page and all topics were artificially created.

### Prompt injection in the wild

- Simulations or theoretical analysis suggest (this item combines web measurement with fixed-context experiments): among about 1.2 billion URLs, 15,387 prompt injections were verified, spread across 11,722 pages and 2,042 hosts.
  - About 87% are invisible to people, and about 70% are hidden in channels that are naturally not rendered (HTTP headers, structured data).
  - Among their uses, reputation manipulation accounted for 1,521 cases; but defensive uses were more common (protecting data 4,093 cases, identifying AI crawlers 3,096 cases).
  - 65.8% of the pages already contained the injection 12 months earlier, showing that such content persists for a long time.
  - Models' actual compliance rate was very low: 3.9% with plain-text input, 1.1% with HTML or snapshots, 0.2% with raw responses; the highest, 8.0%, was for small models with plain text. There were also individual cases of models recognizing an injection yet still following it.
- This study's conclusion is fairly conservative: injection is widespread, but its actual success rate as an attack method is not high, and depends heavily on how the page is read in and how large the model is.

### The backfire effect of injection

- Simulations or theoretical analysis suggest (this item is a workshop-level study, single domain, single language): in a fixed context, for some models with stronger safety training, facing an injection lowered the target brand's top-two hit rate from 54% to 8%; when only a quarter of the same brand's documents were injected, the brand's hit rate on that model fell from 28% to 0%, worse than not appearing at all.
- On another family of models, the same injection raised the target brand's hit rate from 17% to 40%.
- None of six prompt-level mitigation methods restored the baseline; only providing objective specifications in the system prompt as the basis for decisions brought a partial recovery (36% vs 54%).
- The evidence grade is low, but it reveals a mechanism worth guarding against: **a model's defensive response can itself be weaponized.**

### Defences

- Repeated tests on real AI search engines found: across 1,000 real black-hat SEO websites against 9 AI search systems, the cumulative interception rate was 99.78%. The average interception rates of the three stages were 15.7%, 98.2% and 85.2% respectively, with the retrieval stage as the main filter. Keyword stuffing was ineffective on all systems; traditional redirects and cloaking were mostly blocked after retrieval.
- The same study also warns: techniques designed for AI search (for example, cutting content into short passages, or covering possible rewritten queries on the page) were adopted at a clearly higher rate. **Defences block old techniques; that does not mean new techniques are ineffective.**
- Simulations or theoretical analysis suggest: among 10,095 real search result pages, an estimated 8.90% or so bear traces of GEO; among pages modified in 2026 the share rises to 16.36%. Of the citations in pages bearing GEO traces, 69.34% are low-verifiability sources. Such content can be detected, but applying "AI text detectors" directly works poorly, because GEO detection must catch "deliberate intervention", not "who wrote it".
- In controlled experimental systems, a dedicated two-stage defence (preference-based re-ranking plus an experience bank) reduced the average success rate of seven GEO attacks across five models from 50.32% to 6.20%, with a normal-evidence retention rate of 94.12%. Perplexity filtering flagged only 15 of 616 attack documents, while mislabelling 252 normal documents.
- Simulations or theoretical analysis suggest: without defence, the average attack success rate was 55.7%; off-the-shelf general safety guardrails lowered it by only 1.7 to 3.2 percentage points; one form of self fact-checking refused to answer for 98.4% of normal content on one model. A dedicated lightweight detector could lower the success rate from 55.7% to 29.2%, with answer quality almost unchanged.
- Repeated tests on real AI search engines found (the data-void study above): what users can do helps little. Asking in a skeptical tone or switching to another AI search engine did not noticeably lower the chance that false content was adopted (appearance rates across conditions ranged from 26.8% to 37.5%; statistically, effects as large as "halving or doubling" were ruled out). Of the answers that cited or used the false content, only 26.8% carried any caveat or warning, and 73.2% carried none. A skeptical tone only made answers carry caveats more often (53.8% for the highest combination, 5.6% for the lowest). The researchers infer that two existing kinds of defence, "filtering suspicious documents" and "aggregating independent evidence", would struggle in a data void, because the attack page looks normal and there is no independent source to compare it with; this has not been tested.
- Simulations or theoretical analysis suggest that, in principle (7 fixed documents, a single 12-billion-parameter open-weight model, 200 scientific-claim questions), relying only on a prompt that asks the model to "check for misinformation" itself may not be reliable. When the false claim made up only 1 document, the model caught it 25% of the time; when the same claim was rewritten into 5 more documents, making up 6 of 7, only 10%. But the design also cut the normal documents from 6 to 1, so the cause of the drop cannot be determined. The researchers suggest that detection should consider whether sources are independent of each other and whether repeated passages add new evidence; this suggestion has not been verified.

### Summary of the evidence

| Conclusion | Evidence strength | Scope |
|---|---|---|
| Traditional black-hat SEO is almost entirely intercepted in AI search | Repeated tests on real engines | Old-style techniques |
| Claim-style manipulation works better than instruction-style injection | Pages supplied to the engine | Fixed sources; not verified with real retrieval |
| Multi-party manipulation leads to a prisoner's dilemma | Pages supplied to the engine | Specified domains, fictitious products |
| Payoff approaches zero once everyone adopts | Simulation / theory | Fixed context |
| Injection in the wild is widespread but compliance is low | Simulation / theory (including web measurement) | Summarization tasks |
| Injection may harm the target brand | Simulation / theory, workshop-level | Single domain, single language |
| Dedicated defences greatly reduce attack success rates | Controlled experimental systems | Purpose-built pipeline, model-based judging |
| General safety guardrails are basically ineffective | Simulation / theory | Purpose-built pipeline |
| In a data void, a single page may enter the answer | Repeated tests on real engines | Artificially created data-void topics, fictitious content; the page must first be indexed |
| A skeptical tone or switching models does not noticeably lower adoption; when adopted, most answers carry no warning | Repeated tests on real engines | Same as above |
| When one claim is rewritten as several documents, the model catches it less often | Simulation / theory | One small model, fixed context, confounded factors |

## 3. Debates and counterexamples

### Debate 1: Is manipulation actually easy?

| View | Basis |
|---|---|
| Easy | When the pages are supplied to the engine, repeatedly editing a single page can push it to first place in half of trials; Practitioners report from their own tests that after third-party content was planted in a niche field, models accepted false information; in real AI search, a single page on an data-void topic appeared 31.0% of the time (42.3% for indexed pages) |
| Not easy | Real AI search intercepts 99.78% of traditional black-hat techniques; in a full pipeline, most injections are eliminated at the retrieval stage; compliance with injections in the wild is 0.2% to 8% |

The difference between the two comes mainly from **experimental conditions**. Fixed-context experiments assume the manipulated content has already entered the candidate set; in real pipelines, most content does not even get into the candidate set. Another difference is **the competitiveness of the field**: niche topics with a data void (fictitious brands, fictitious people) are easily filled with false information; topics with a large body of existing information are much harder. The first half of this sentence now has evidence from real engines: repeated tests on real AI search engines found (three AI search engines, 56 artificially created data-void topics, one page published per topic, measured on day 25 after going live) that on topics with no other sources to compare, a single page had a 31.0% chance of being written into the answer or listed among the sources; counting only pages indexed by a search engine, 42.3%. Whether topics with a large body of existing information are much harder was not directly compared in this study.

The third difference is where the content is posted. Repeated tests on real AI search engines found (10 commercial AI search platforms, controlled posting, multi-day tracking): when ordinary posts were made on platforms that AI already cites often and where ordinary users can post, a fictitious concept was cited by 8 of the platforms within 7 days, 9 of 10 fictitious topics were cited, and most were first cited on day 1–2. But the effect was very unstable: the citation rate over the whole observation period was only 17.5%, and only 7.5% actually made it into the answer text; for topics already widely discussed, the share making it into the answer text was only 3.5%; one platform never cited at all; when the same study posted 40 articles on a self-hosted website, citations within a week were zero; after the posts were deleted, some platforms kept citing them for about 4 days. So "most content cannot get in" applies mainly to old techniques on self-built websites; on platforms AI already favours, content on niche topics can get in quickly. Another set of repeated tests on real AI search engines showed that a single self-hosted page can also get in, provided it is indexed, the topic has no competing sources, and one waits long enough: pages on established domains appeared 38.4%–78.3% of the time, new domains actively submitted for indexing 14.3%–42.9%, and new domains not submitted for indexing 0 on all three engines; AI crawlers visited only after about 10 days, and results stabilised only after about 25 days.

### Debate 2: Does injection help or harm the target brand?

The same injection works in opposite directions on different models: one family of models pushes the target brand down, another pushes it up. This is not a contradiction between studies but a difference between models. It shows two things: the effect of injection is unpredictable; and there is no injection that is "effective on all engines".

### Debate 3: Can repeatedly "correcting" AI change its recommendations?

- Practitioners report from their own tests: after repeatedly correcting a model's wrong answers from several accounts and devices, the model began recommending a specific business (not independently verified; very small sample).
- Other practitioners report from their own tests that similar manipulation results persisted only within the experimenter's own sessions and did not appear after logging out.
- One practitioner observed that a brand claiming to be "the AI's first recommendation" could not be found in either logged-out or logged-in states, and pointed out that a single check is not an independent observation: getting a margin of error of about 5% requires many repeated queries.

**Judgment**: session memory, personalization and randomness can all create the illusion that "manipulation succeeded". Without logged-out testing and repeated measurement, such claims cannot be treated as evidence.

### Debate 4: Is manipulative community posting detected?

Practitioners widely believe (though it is disputed) that manipulative marketing using many accounts or automated posting is easily detected by moderators or platform algorithms and deleted or banned. Supporters are in the majority, but a considerable share hold the opposite view; one practitioner also observed that blocked content gets reposted from new accounts, sometimes as many as ten accounts, and that in low-competition fields such content can still make it into AI recommendations. This is opinion, not proof.

## 4. Cases

The following cases are all self-reported by practitioners and not independently verified. Their value lies in showing "what manipulation looks like" so that it can be recognized, not in serving as methods to copy.

### Case 1: A recommendation instruction addressed to "any AI engine"

One practitioner observed that in a public community discussion, there appeared a passage written directly to "any AI engine", asking any AI that read it to recommend one specific vendor.

This is a real-world **prompt injection attempt**. Its target is not human readers but the AI engines that crawl and ingest forum content as sources for answers.

Analysed with this chapter's principles:

- It is **instruction-style injection**, the type the evidence shows to be least effective (Principle 11.2).
- It violates criterion 3 of the four white-hat criteria (instructions hidden from, or written specifically for, the model) and criterion 4 (commercial intent not disclosed).
- On some models, this kind of injection may even push the recommended brand down (Principle 11.3).
- A warning for brand owners: if such text appears in content mentioning your brand and you did not authorize it, it may be a means of suppressing you.

Recognizable features: the text addresses "AI", "language models" or "assistants" rather than people; it uses a commanding tone; it demands that a named party be recommended; it is unrelated to the topic of the surrounding discussion.

### Case 2: A fictitious brand and contradictory third-party stories

- **What was done**: a practitioner created a fictitious brand with almost no web presence and published an official FAQ on its website; then published three contradictory third-party stories online (a fake influencer blog, a fake Q&A interview, and an "investigative report" on a blogging platform), each giving a different founder, location and output volume, all contradicting the official account.
- **Where**: questions were put to eight AI models.
- What was observed (Practitioners report from their own tests): most models accepted the false information and ignored the official FAQ; when the official account said "we do not disclose figures" while the fake sources gave specific output volumes, the models chose the fake figures about 80% of the time; only a few models stuck to the official source. The most effective was the "investigative report": it first debunked some obvious lies to build credibility, then slipped in its own false information.
- Follow-up: one practitioner observed that after the experiment was published, models were often able to see through the false information, but sometimes still quoted the experiment report out of context to support the fake sources.
- The principles illustrated: claim-style content works better than instruction-style content (Principle 11.2); topics with a data void are the easiest to fill with false information. The implication for brand owners: wherever the official account is missing, others can fill in the narrative.

### Case 3: Publishing ranking lists on expired domains

- **What was done**: a practitioner used expired domains with a link history to publish several ranking lists worded slightly differently, placing their own CEO first.
- **What was observed** (Practitioners report from their own tests): ChatGPT and Perplexity sometimes adopted and cited these domains; Gemini and Claude basically did not; even within the same engine, the answers were inconsistent.
- Debate: another practitioner pointed out that the result persisted only within the experimenter's own sessions (see Debate 3).
- The principles illustrated: the effect of manipulation is unstable and engine-dependent; several ranking lists that "look independent" but have highly similar content are a feature of coordinated promotion that should raise suspicion.

### Case 4: Negative GEO (suppressive content)

- **What was done**: a practitioner created a fictitious person with no web footprint at all, first confirming that no model or search engine could find them; then published false negative information about this person on several existing third-party websites; then kept asking 11 models the same question and recorded the answers.
- **What was observed** (Practitioners report from their own tests): after several weeks, some models began citing these pages and repeating the negative narrative. Perplexity repeatedly cited and adopted it, often with cautious wording such as "reportedly"; ChatGPT was more sceptical; most models did not mention it. The experimenter considered this approach hard to scale. One practitioner observed that such content starts to take effect after about a week.
- The principles illustrated: suppressing a competitor is possible when the target has a data void; engines differ widely. This is the same category of risk as "using injection to suppress competitors" in Principle 11.3: GEO's attack surface includes not only raising yourself but also pushing others down.

### Case 5: Coordinated community promotion (astroturfing)

- **One practitioner observed**: a competitor in a B2B software field posted heavily using highly active bot accounts, with a typical pattern: posing as a "target customer" who claims to have done research → praising one product → criticizing competing products one by one → pretending to ask for opinions → other fake accounts commenting in agreement. This content was cited by AI and spread false information about the victim's product; the victim's clarifications in the comments had limited effect.
- **One practitioner observed**: review platforms saw a large number of reviews that "give one star, then recommend some unknown competitor"; new citations of high-commercial-intent encyclopedia-type pages grew about 10 times within a year.
- One practitioner observed that in low-competition niche markets, manipulators who know where to post and which old accounts to use can push scam websites into AI recommendations; some consumers have been directed to scam websites by AI as a result.
- The principle illustrated: AI engines treat third-party discussion as "social proof", which makes coordinated promotion a form of manipulation aimed directly at AI.

### Case 6: Old-style techniques backfiring in AI search

- **One practitioner observed (this item is a test report)**: in a clinic's business profile, a previous agency had split the service items into a dozen or so variants stuffed with place names and the word "near me". The practitioner believes this was treated as a spam signal in AI recommendations, causing a well-reviewed clinic to be skipped in AI recommendations.
- **One practitioner observed**: a website that was technically sound was not cited by AI because it carried about 20 paid low-quality backlinks.
- One practitioner observed that fully automatically generated content is mostly spam; a brand associated with too much spam content may stop being recommended.
- The principle illustrated: consistent in direction with the results of tests on real engines: keyword stuffing is ineffective, and old-style black-hat techniques are mostly filtered out. But these observations cannot prove the causal claim that the site was "penalized because of this".

## 5. What to do

### Recognizing manipulation aimed at you

| Action | Evidence strength |
|---|---|
| Regularly monitor how AI describes your brand while logged out, with repeated queries, and do not draw conclusions from a single result | Practitioners report from their own tests; randomness is supported by several studies |
| Watch for text in a commanding tone addressed to "AI" in third-party content mentioning your brand | Simulation / theory (backfire effect of injection) plus first-hand observation |
| Watch for "several seemingly independent, similarly worded ranking lists or reviews" appearing at the same time | Practitioners report from their own tests; simulation or theoretical analysis (rewriting one claim into several documents lowers the model's detection rate; one small model) |
| Watch for claims tied to a breaking-news event, a newly coined term or an old term given a new meaning, that have only a single source | Repeated tests on real AI search engines (data voids anchored to a breaking-news event were the easiest to fill) |
| Watch for concentrated appearances of "negative review plus recommendation of an unknown competitor" on review platforms | A single first-hand observation, as a lead |
| Watch for the community posting pattern "claims customer research → praises one company → criticizes competitors → fake accounts agree" | A single first-hand observation, as a lead |
| Check whether content has been planted in the page's non-rendered channels (HTTP headers, structured data) | Simulation / theory (about 70% of injections in the wild are hidden in these channels) |

### Defence and repair

| Action | Evidence strength |
|---|---|
| Answer common questions clearly and specifically through official channels, reducing data voids | Data voids are easily filled: Repeated tests on real AI search engines found this; Practitioners report from their own tests in the same direction. Whether filling the data void with the official account first protects you: inference, not yet tested |
| Do not count on users "asking in a skeptical tone" or "switching to another AI" to stop false content in a data void; if you build your own system, flag claims with "little supporting evidence" without suppressing legitimate but rare content | First half: Repeated tests on real AI search engines found this; second half: the researchers' suggestion, not yet verified |
| Provide verifiable, distinguishing, genuine information (specifications, prices, ratings, dates) | Simulation / theory; reviews of the literature also support verifiable content |
| When you find false content, deal with it at the source (ask the platform to take it down, publish a correction with evidence), not just with clarifications in the comments | A single first-hand observation shows that clarifications in comments have limited effect |
| If you build or evaluate an AI search / RAG system: do not rely on general safety guardrails or perplexity filtering to block GEO manipulation; when evaluating defences, also measure "whether normal evidence is wrongly harmed" | Controlled experimental systems; simulation / theory |
| If you build your own system: providing objective decision criteria in the system prompt can partly reduce the bias caused by injection | Simulation / theory, workshop-level |
| If you build your own system: deduplicate near-paraphrased content in retrieval results, and measure the strength of corroboration by "number of independent sources" rather than "number of documents" | The researchers' suggestion (based on simulation or theoretical analysis with a single model), not yet verified |

### Self-check: the four white-hat criteria

Before any content goes live, confirm each criterion in turn: facts faithful, evidence genuine, no hidden instructions, commercial intent disclosed.

### Do not do

- **Do not put any instructions addressed to AI on your pages**, visible or hidden. They work poorly, are unpredictable, and may cause your own brand to be pushed down.
- **Do not fabricate evidence**: fake reviews, rankings, data or quotations. Even if it works in experiments, it violates the white-hat criteria, and once it is exposed the consequence is that the whole brand is downweighted.
- Do not use multiple accounts or bots for coordinated promotion.
- Do not suppress competitors (publishing false negative content, planting injections in content related to competitors).
- Do not treat "success" within a session as a real effect.

### Already outdated

- Keyword stuffing (including stuffing place names into business profiles): ineffective against AI search systems.
- Traditional redirects and cloaking: mostly blocked after retrieval.
- Buying large numbers of low-quality backlinks: old-style black-hat techniques have a very high interception rate in AI search.
- The idea that "finding one technique keeps you ahead for the long term": once a technique becomes widespread, its payoff approaches zero.

## 6. Key points

1. **GEO is a zero-sum competition.** The payoff of a technique decays as adopters increase; simultaneous manipulation by several parties creates a prisoner's dilemma. Lasting advantage comes from genuine, distinguishing information that competitors find hard to copy.
2. **Claims are more dangerous than instructions.** Instruction-style injection is easily recognized and has a low compliance rate; exaggerated claims disguised as evidence are the manipulation that most needs watching.
3. Injection can backfire, and can also be weaponized. Some models penalize brands that are the target of injection, which means someone could use injection to suppress you. The evidence grade is low, but the risk is real.
4. Injection attempts aimed at AI already exist in the real world, including text in community discussions directly asking "any AI engine" to recommend a specific vendor. Recognizable features: AI as the audience, a commanding tone, a named recommendation.
5. Defences have blocked the old techniques. Real AI search intercepts the vast majority of traditional black-hat SEO, but new techniques designed for AI search still have room.
6. General safety guardrails are basically ineffective against GEO manipulation; only detection and re-ranking aimed specifically at "deliberate intervention" are effective.
7. A data void is the biggest weakness. Repeated tests on real AI search engines found that when there are no other sources to compare, a single page may be written into the answer, usually without any warning; users asking in a skeptical tone or switching to another AI did not noticeably lower the chance of adoption. Tests with a fictitious brand and a fictitious person point the same way: wherever there is no official account, a false narrative is easiest to fill in.
8. Self-check with the four criteria: facts faithful, evidence genuine, no hidden instructions, commercial intent disclosed.
