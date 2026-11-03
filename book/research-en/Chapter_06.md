# Chapter 6: Selection and Ranking (Relevance, Position, Attribute Weights)

> In the pipeline used throughout this book, this chapter covers the fourth stage:
>
> ```
> Triggering → Accessibility → Retrieval → [Selection/Ranking] → Citation → Absorption → User behavior
> ```
>
> Earlier chapters discussed whether content can enter the candidate set. This chapter asks: once you are in the candidate set, on what basis does the model pick you, where does it place you, and whom does it finally recommend?

## Questions this chapter answers

1. Once content enters the candidate set, which factors decide whether it is selected? Which factors have almost no effect?
2. How much does "being in first position" really matter? Why do different studies give such different answers?
3. In recommendation settings (choosing a hotel, a product, a service provider), which attributes does the model weigh? Can the reasons it gives be trusted?
4. Why are "being mentioned", "being cited" and "being selected as a recommendation" three different things?
5. What can practitioners do on this basis, and what should they stop doing?

## Core principles

### Principle 6.1: Relevance is the most stable gatekeeping factor

The selection stage is not "whoever writes best gets picked". It is closer to a two-stage screen that filters first and compares second:

```
Candidate documents
  │
  ├─ Gatekeeping: Does the topic match the query? Is the position near the top? Is there a clear price/specification? Is the timestamp recent?
  │        (Fail any one of these and it is hard to be selected, however well the rest is written)
  │
  └─ Differentiation: confident statements backed by evidence, comparisons, ratings and review counts, and similar attributes
           (Only after passing the gate do these start to create a gap)
  │
  ▼
Selected / Cited / Recommended
```

**Why does relevance come first?** At this stage the model's task is to answer "this one" question. However authoritative a piece of content is, if it answers a neighbouring but different question, it is of no use.

- In a controlled two-source experiment (6 models, 18 factors, 1,440 scenarios, 252,000 trials), topic mismatch and list position had very large effects; the advantage of a recent timestamp over an old one was also clear; an explicit price was likewise a strong factor. By contrast, **changing only the formatting (structured layout vs dense paragraphs) had almost no effect**. Of the 18 factors, 11 were significant in 4 or more models, and the other 7 had no consistent effect.
- In real environments, however, recency matters much less: repeated tests on real AI search engines found (ChatGPT web version) that using a page's publication recency to predict whether it is cited gives an AUC of only 0.48–0.54, close to guessing.
- When the pages are supplied to the engine, "relevance between query and source" predicts citation (correlation coefficient about 0.39) far better than a score that ignores the query and rates only the content itself (about 0.11). A "content quality score" detached from the query does little to predict citation.
- In controlled experimental systems, diagnosing why citations failed: of 949 comparison pairs, 62.2% were "semantic misalignment", 27.1% content quality, 10.1% technical completeness, and only 0.6% systematic exclusion. At baseline, about 43% of topically relevant pages were not cited.

What this means in practice: "relevant" does not mean belonging to the same broad topic, but matching the user's specific question. Broad category words and marketing language often drop out at this step.

### Principle 6.2: Position effects are strong in fixed contexts but much weaker in real systems and agents

**Mechanism**: when a model reads a long list of documents, its attention is not evenly distributed.

- Simulations or theoretical analysis suggest that, in principle, a U shape may appear: information placed at the beginning and end is used most, and information in the middle is easily ignored. In multi-document question answering with a fixed context, accuracy can drop by more than 20% in the worst case, and in some settings falls below the 56.1% achieved with no documents at all (closed book). In addition, retrieving more than 20 documents brings only about 1–1.5% further improvement, and simply enlarging the context window did not improve use of information in the middle.
- Another set of fixed-context experiments found that moving a document to position 1 in the context gave a larger gain than any content rewriting method. Across 54 scenarios, content rewriting produced a statistically significant ranking gain in only 3.

**But in settings closer to reality, the position effect shrinks sharply:**

- In a purpose-built shopping agent environment, agents viewed 1.63–5.83 options per session, while humans viewed only 1.12. The effect of position on "whether an option is viewed" was only about 1/4 to 1/10 of that for humans, and it was not monotonic: the view rate was lowest around ranks 68–74 and then rose again. At the highest reasoning setting, position no longer had a significant effect on the final choice.
- In controlled experimental systems, a counterfactual replay of the same frozen records: in the observational data, the citation gap between rank 1 and rank 5 was 42.3 percentage points; after controlling for other factors it was only 7.9; on the held-out sample it was 0.

Why does this happen? In observational data, sources ranked near the top are often more relevant and more authoritative to begin with. Position is entangled with these attributes, so it looks as if "position matters a lot". Once the other conditions are held fixed, the pure position effect is much smaller. Agents look at more options, and the more thoroughly they reason, the less they depend on "who appears first".

There is, however, a counterexample that must stand alongside this. When the pages are supplied to the engine, researchers gave the 6 product page URLs of the same brand to commercial AI search engines to read and rank, in two opposite orders, with the page content completely unchanged (the brands and products were fictional, and only one query pattern, "best [category]", was used). On ChatGPT, the share of first places won by the same rewriting method went from 73.8% to 93.8%, and the first place changed for about a quarter of brands; on Grok it was 37.5% versus 50.0%; on Gemini, the method winning the most first places switched outright. On all three engines that method won first place more often when it was at the top of the list, but the size of the effect differed a great deal. This is still "choosing from a supplied list", but the subjects are real commercial AI search engines, not simulated agents. Some of the researchers are authors of the best-performing rewriting method, and this conflict of interest should be considered when interpreting the result.

This conclusion has limits, however. All the evidence above concerns "choosing from a list that has already been presented". In deep research agents that search autonomously over multiple rounds, ranking also works through another path: documents ranked near the top are read first, and what is read first decides what is searched in the next round. In an experiment with a fixed set of candidate documents (weaker evidence, possible in principle), simply swapping the ranking of supporting and opposing documents shifted the overall direction of the evidence the agent read substantially, and in about half of cases it disagreed with the overall direction of all available documents. This experiment did not use a real search engine, used small open-source models, and measured the average stance of documents the agent read, not the text of the final report. So the more accurate statement is: position has a small effect on "a single choice", but in multi-round search it may be amplified through path dependence.

### Principle 6.3: Models have their own "signal weighting function", and the reasons they give do not match what they actually rely on

In recommendation settings, the model does not compare all attributes neutrally. It has its own set of weights: some attributes are amplified, others ignored.

**A preregistered hotel-choice audit** (12 models, 3,024 choice sets, 61,459 calls in total; the hotels were synthetic data):

| Attribute change | Change in probability of being selected |
|---|---|
| Rating 3.9 → 4.7 | +31.65 percentage points |
| Price $129 → $249 | −30.03 percentage points |
| Has an environmental certification | +11.61 percentage points (overweighted) |
| High review count | +8.31 percentage points |
| Belongs to a chain brand | −1.79 percentage points |
| Management replies to reviews | +0.11 percentage points (statistically equivalent to zero) |
| Position 1 in the list (vs positions 2–5) | About +2–4 percentage points, roughly equal to being $11.7 cheaper per night; up to about 26 percentage points for individual models |

**Authority signals are also amplified.** In a fixed-context experiment on academic paper recommendation, with titles and abstracts left completely unchanged and only authority metadata altered (for example the journal of publication), 39.2% of recommendations flipped; among the cases that changed, 68.2% moved toward the higher-authority side. Sensitivity across models ranged from 17.4% to 49.2%.

The say-do gap. The reasons a model writes down only partly match the weights it actually relies on (correlation coefficient 0.59–0.85). Position clearly has an effect, yet it is mentioned in less than 0.7% of the stated reasons. In the paper recommendation experiment, a strong debiasing instruction cut the share of responses that "mention authority" by 24.0 percentage points, but cut recommendation flips by only 12.9 percentage points; a mild debiasing prompt was almost useless and even produced a rebound in frontier models.

What this means in practice: you cannot reverse-engineer a model's selection logic by asking the AI "why did you recommend A". The reason it gives is an account, not a record of its decision.

> Note: both experiments above use fixed contexts and synthetic or controlled data. They show what "may happen in principle" and cannot be equated directly with the weights in real search products.

### Principle 6.4: AI prefers "AI-style" text

In controlled experimental systems, researchers observed a kind of "stylistic affinity":

- Text with lower perplexity, that is, more "predictable" to the model, is more likely to be cited. For each 1 standard deviation decrease in perplexity, the probability of being cited rose from 47% to 56%. Traditional search rankings show no such effect.
- In a RAG setting with sources in random order, this preference persisted, and it is a separate factor from semantic relevance.
- After sources were polished with an LLM, the number of cited sources per query increased by about 1.07 (generic polishing) to 2.11 (polishing aimed at being cited).

This evidence has so far been verified only on a few engines. It is a new finding that needs further confirmation and should not be extrapolated to all platforms. Another simulation study cautions that this preference is not the same as preferring "AI-written text" as such: AI-generated documents that compile and rewrite, stay on topic and are more factually correct were over-selected (67% of the candidate pool, but more than 80% of the top 10), while AI-generated documents that tampered with entities and numbers were almost completely excluded by the reranker (exposure no more than 0.09%). At present, "AI style" cannot be separated from "more complete, more on topic, more correct".

### Supplement: Appearing, being cited and being selected are three different gates

Most academic research measures "whether something is cited" or "citation rank". But for recommendation queries, practitioners repeatedly point to another gate: **a brand appearing in the answer does not mean it is finally recommended**. In multi-turn purchase conversations, the model gradually eliminates options in later turns according to conditions such as budget, region and use case. At present this comes mainly from practitioners' own tests, and this chapter describes it in detail in the "Cases" section.

**Sites the model names on its own initiative are selected more often.** In the author's small-scale tests (method in Chapter 4), sites that the model named with `site:` in its search terms had a clearly higher chance of being cited in the same session: this held in 18 of the 20 comparable sessions across three question types, with a session-stratified odds ratio of about 3.6; in 9 of 10 sessions on the swimming question (odds ratio about 2.7). This is a signal independent of semantic similarity: the model decides where to look before it searches. Single model, small sample, not independently verified.

## How strong is the evidence

| Principle | Main type of evidence | Strength assessment | Scope and limitations |
|---|---|---|---|
| 6.1 Relevance as gatekeeper | In controlled experimental systems (large-scale trials) + when the pages are supplied to the engine + reproducible RAG pipeline | Fairly strong: three different designs point the same way | The two-source experiment's corpus was LLM-generated with a fixed context; the authors of the relevance prediction study themselves provide a content scoring service |
| 6.2 Position effect | Mainly simulation / fixed context; agent environments and controlled replay as counter-evidence; a test on real AI search engines when the pages are supplied to the engine as a counterexample | Strong in fixed contexts, weak and unstable in real systems; but when real AI search engines read a fixed list, order can still change the first place | The conclusion "position matters a lot" depends heavily on the experimental setup; the counterexample is a single study, the URLs were supplied by the researchers, and some of the researchers are authors of the best-performing method |
| 6.3 Signal weights and the say-do gap | Simulations or theoretical analysis (preregistered randomized audit, fixed-context recommendation) | Moderate: rigorous design, but grade E | Synthetic hotels, fixed candidate papers; does not represent the real weights of commercial engines |
| 6.4 Preference for AI style | Controlled experimental systems + observation of a single commercial engine | Moderate to weak | Verified only on a few engines |
| Appearing ≠ being selected | Practitioners report from their own tests | Weak to moderate: several sources point the same way, but not independently verified | Mostly recommendation and purchase queries |

Two methodological cautions:

1. **A single generation is unreliable.** In controlled experimental systems, about 15% of binary decisions on "whether to cite a given source" flip under the same conditions, and about 45% of the variance in effects comes from decoding randomness. Draw conclusions from a single run and you can easily see false effects. When the pages are supplied to the engine, re-running ChatGPT once on the same pages in the same order also changed the first place for about one in five brands.
2. **Observational data overestimates.** The position gap shrinking from 42.3 percentage points in observational data to 7.9 under control is an example. Practitioners' correlation statistics may be confounded in the same way.

## Debates and counterexamples

### Debate 1: Do formatting and structure actually help?

| Position | Basis |
|---|---|
| Almost no help | In the controlled two-source experiment, changing only the formatting had small and inconsistent effects. Practitioners report from their own tests (61 sites, more than 540 citation checks) that headings, lists and semantic HTML are only a "baseline", which almost every site meets, so they do not differentiate. |
| Some help, but for "allocation" rather than "expansion" | In a controlled agent experiment, structured presentation (headings, lists, tables) increased citations of the target source by about 0.5, but total citations did not increase; the gain in "whether cited" was 4.5 percentage points, with a confidence interval spanning zero, so it is uncertain. It looks more like redistributing credit among several equivalent sources. |
| Clear effect | Practitioners report from their own tests (analysis of 600 answer snippets) that pages with structured comparison tables were featured 2.4 times as often; when author credentials appeared within two paragraphs of the answer, the citation rate rose from about 12% to about 31%. |

**How to read this**: the three measure different things. "Whether something enters the answer" is decided mainly by relevance, and structure plays a very small role; for "who gets more citations among similar sources", structure may help a little. The practitioners' 2.4 times figure is an observational comparison, not independently verified, and may be confounded by "pages with comparison tables were more relevant to begin with".

### Debate 2: Is the position effect large or small?

- Fixed-context studies: very large, even larger than any content rewriting.
- Hotel audit: only 2–4 percentage points on average, but up to about 26 percentage points for individual models.
- Shopping agent: very weak and non-monotonic; the stronger the reasoning, the smaller it is.
- Controlled replay: close to zero on the held-out sample.
- Real AI search engines reading a supplied list: when the pages are supplied to the engine, merely reversing the order of 6 URLs changed the share of first places won by the same method on ChatGPT by 20 percentage points (73.8% versus 93.8%); on Gemini the gap was much smaller (23.8% versus 28.8%).

**How to read this**: the position effect is real, but its size depends on the model, the reasoning configuration and the number of candidates. "Rank first and win" is not a stable rule. For practitioners, relevance and attributes are more controllable than position.

### Debate 3: Does authority matter?

- The research side: changing only authority metadata such as the journal flipped nearly 40% of paper recommendations; another controlled experiment also found that some pages, even after their content was fixed, still could not be cited because of competition on domain authority.
- The practitioner side: several practitioners report from their own tests that traditional metrics such as backlinks and domain authority are almost unrelated to AI recommendation rates; one practitioner observed a page with very low domain authority beating sites with far higher authority.

**How to read this**: the two sides do not mean the same thing by "authority". In the research, authority is an authority label that appears in the context and that the model can read (journal name, institution name). The domain authority practitioners refer to is an external metric calculated by SEO tools, which the model may not see. A possible interpretation: **authority signals the model can see have an effect; SEO metrics it cannot see have limited effect**. But this is only an interpretation and has not been directly verified.

### Debate 4: How important is freshness?

- In the controlled two-source experiment, a more recent timestamp is a gatekeeping-level factor.
- Practitioners report from their own tests that some platforms put particular weight on freshness, and recommend updating content within 30 days.
- This "30 days" is a rule of thumb from a single report, without a control, and should not be treated as a threshold. In addition, the main text and the tables of the two-source experiment paper do not agree on the size of some effects, so the specific numbers should be treated conservatively.

### Counterexample: big brands occupy the positions for broad category terms

The gatekeeping logic does not mean small sites have a chance in every query. Practitioners report from their own tests that broad category questions (such as "the best brand of a certain type of machine in a certain country") are almost entirely occupied by established big brands; the community view that "small sites are cited more easily because they focus on narrow topics" is supported by several practitioners, but remains disputed in some discussions. **Narrow questions have open slots; broad questions may not.**

## Cases

### Case 1: The same page, invisible for broad questions and first for narrow ones

- **What was done**: a practitioner manually tested about 30 websites on ChatGPT, and pulled Google AI Overviews results through a search results API.
- **What was observed**: a B2B industrial equipment client did not appear at all for broad questions such as "the best laser marking machine brands in a certain country", where the answer listed only the big manufacturers; but for narrow questions such as "which kind of marking machine should be used for metal marking", ChatGPT listed it first and cited it. The page did not change at all between the two.
- The cited clients had one thing in common: the model would restate specific details from their pages, such as the specific equipment models listed on a clinic's page. Pages written in category language were not cited.
- The same practitioner also found that an article ranked first in Google's organic results was not cited by ChatGPT on any of six topics (0/6).
- Evidence strength: practitioners report from their own tests, not independently verified.
- Related principle: 6.1. Relevance is specific to a query, not a fixed property of a page; specific nouns match queries more easily than polished narrative.

### Case 2: Appeared, but was not selected

Several practitioners report from their own tests the same phenomenon:

| Observation | Scale | Result |
|---|---|---|
| Multi-turn brand queries across 4 AI models | More than 150 brand queries | 78% of brands appeared in the first-turn answer; only 31% lasted to the final recommendation in turn 4 |
| Census of local businesses in a US city, across 4 AI assistants | 1,444 businesses | Only 241 were ever recommended by name; 83% never appeared once |
| Category-leading brands in the US, with category questions that did not name the brand | 2,475 brands | 86% of e-commerce brands were never mentioned; yet when asked directly by brand name, all four assistants knew these brands well |
| Multi-turn purchase sequences across 3 platforms | More than 12,000 | Of the brands that appeared early, 87% did not make it into the final recommendation |

- **Evidence strength**: practitioners report from their own tests, not independently verified; definitions and methods differ across reports, so the numbers cannot be compared with each other.
- **Method caution**: if multi-turn tests follow a pre-written script of follow-up questions, they cannot measure how the answer changes a real person's next question.
- Related principle: the selection stage is a separate gate. "The model knows you" and "the model thinks of you when someone else describes a need" are two different things.

### Case 3: Describe the buyer, and the recommendation changes

- **What was done**: a practitioner asked each of the same five healthy-snack purchase questions twice: once with the question alone, and once after first describing the buyer (cutting fat, tracking nutrients, reads ingredient labels, does not care about price). Each time used a fresh incognito session.
- **What was observed**: in the 50 answers without a persona, only 2 explicitly advised avoiding a particular brand; with the buyer persona added, this became 20. The same brand was recommended in one conversation and advised against in another. The answers also became more decisive and stopped listing large numbers of options.
- Evidence strength: practitioners' repeated, controlled tests found this; the author also states that the sample is small.
- Related principle: 6.3. Selection depends on the conditions in the query and the model's attribute weights; the same brand's attributes can be judged as strengths or weaknesses under different conditions.

### Case 4: A new product replaced in the first turn before it was seriously considered

- **What was done**: a practitioner tested a newly launched prebiotic cola from a large beverage company in six AI purchase journeys on ChatGPT, Gemini and Perplexity.
- **What was observed**: in four of the six, the new product was replaced in the first turn by challenger brands that had established the category earlier.
- Evidence strength: practitioners report from their own tests, very small sample, not independently verified.
- Related principle: selection happens early in the conversation. Once the model forms a preference for a competitor, later turns find it hard to reverse. A theoretical model offers a mechanism for this path dependence (weaker evidence), but it assumes that both users and engines tend to reinforce earlier answers, and this premise has not been verified.

### Case 5: The "competitor list" on your own site used to recommend competitors

- **What was done**: one practitioner observed a client that ranked well in traditional search and whose site was often a main source for AI answers, sometimes cited 4 times in a single conversation, yet its brand was never recommended. The reason was a passage on the site: "We may not be right for everyone; here are 5 trustworthy competitors."
- **What was observed**: the AI found the most relevant document (the client's own site), extracted the passage that listed entities, and used it directly to generate recommendations. According to this practitioner, after the client's own brand was placed at the top of the list, it became the first recommendation within a few days.
- Evidence strength: one practitioner observed (a single first-hand observation); can serve only as a lead.
- Related principle: 6.1 and 6.2. Relevance decided which document was selected; the entity list and its order inside the document then decided whom the answer recommended.

### Case 6: A local business that publishes its prices

- **What was done**: a local business published its prices on its website and social media pages; this was its only clear difference from nearby competitors (3 on the same block, more than 20 within 5 km).
- **What was observed**: after about three months, the shop was listed by AI as the top supplier almost every time for purchase-intent queries about a certain product in the area; customers reported that they had learned of the shop from Google AI and ChatGPT.
- Evidence strength: one practitioner observed (a single first-hand observation), without a control.
- Related principle: 6.1. In controlled experiments, an explicit price is a gatekeeping factor; this observation points the same way but cannot prove causation.

### Additional lead: "exact alignment" of query wording

One practitioner observed that social platform content cited by AI used wording identical to the prompt; a post on a professional social network with only 10 likes, but whose title contained the exact query, was also selected. Another practitioner observed that when the query was changed to a niche angle within the same intent, small niche sites replaced big sites in 21 of 25 cases. These are all single observations and can serve only as indirect support for the relevance principle.

## What to do

### Recommended practices

| Practice | Explanation | Evidence strength |
|---|---|---|
| Write around specific questions, not category words | List the questions users ask with conditions attached (budget, region, use case), and make the page match those questions directly | Fairly strong (controlled experiments, pages supplied to the engine, and reproducible pipelines: three types of evidence agree) |
| Write specific facts the model can restate directly | Prices, specifications, model numbers, service area, certification names, dated figures. When the pages are supplied to the engine, even a ±0.2% price difference changes the mean rank of some rewriting methods, although it does not change who comes first | Moderate (controlled experiments show explicit prices and specifications are strong factors; several practitioners report from their own tests in the same direction) |
| Publish clear prices | Price is one of the gatekeeping factors; options without a price have difficulty entering the comparison | Moderate (controlled experiment + a single practitioner observation) |
| Keep content genuinely updated, and show dates | A more recent timestamp had a large effect in controlled experiments | Moderate (controlled experiments only; "update every 30 days" is only a single rule of thumb) |
| In recommendation-driven businesses, build ratings and review counts | Ratings and review counts were the main positive attributes in the hotel audit | Moderate to weak (simulation / synthetic data) |
| First diagnose "why it was not selected", then make targeted changes | In controlled experiments, small changes aimed at the cause of failure (changing only about 5% of the content) raised the citation rate from 56.6% to 79.5% | Moderate (controlled experimental system) |
| Track "mentioned / cited / recommended" separately | Use real purchase prompts, add one condition (budget, region, size), and record at which step you drop out | Practitioners report from their own tests (a method recommendation, not proof of effect) |
| Repeat each test several times | About 15% of citation decisions from a single generation flip | Controlled experimental system |
| Check comparison and list passages on your own site | Such passages may be extracted directly to recommend others | One practitioner observed (a lead) |
| If you control the order of a list (such as your own comparison page), reasonably place yourself near the top | Position has an effect in fixed contexts; but in agents and real systems the effect is weak and unstable | Weak (mainly simulation; there is also a test on real AI search engines when the pages are supplied to the engine, showing that the order of a URL list can change the first place, but it tested the order of URLs given to the engine, not the arrangement within a page) |

### Do not do

- **Do not change only the formatting.** Headings, lists and information aggregation had almost no effect in controlled experiments; at most, structure redistributes citations among equivalent sources, and it will not take you from nothing to being selected.
- **Do not apply generic rewriting rules, or heavily compress pages.** Controlled experiments found that generic rules hurt long-tail topics and topics that were already performing well; heavily compressing pages also worked poorly.
- Do not stuff keywords. In one content scoring study, keyword stuffing was scored clearly negative; separately, practitioners report from their own tests that keyword density is unrelated to whether content is featured.
- Do not use vague wording or self-contradictory content. Both reduced the probability of being cited in controlled experiments.
- Do not treat the reasons a model states as the basis of its decisions. Stated reasons only partly match the actual weights.
- Do not count on signals that "look as if they should help". For example, in the hotel audit, the effect of management replies to reviews was statistically equivalent to zero.
- Do not draw conclusions from a single query on a single platform.

### Already outdated

- **Adding quotations, statistics and citation blocks to increase citation.** When the pages are supplied to the engine, researchers retested these three classic 2023 methods on several modern engine families (including commercial models), and none increased citation share; measured on the original metric, the effects went from +42.6, +32.8 and +27.7 at the time to −0.33, −0.28 and −0.79. In another set of fixed-context experiments, "add statistics" rewriting significantly lowered citation rank in 19 of 24 scenarios.
- **Treating SEO domain authority as the main indicator for AI recommendation.** Several practitioners report from their own tests that the link is weak; but note that authority labels the model can see still have an effect (see Debate 3).

## Key points

1. **Relevance is the first gate.** It means matching the specific query, not belonging to the same broad topic. A content quality score that ignores the query predicts citation poorly.
2. **Gatekeeping factors come before differentiating factors.** Topical relevance, a clear price and a recent timestamp must be in place first; changing only the formatting has almost no effect.
3. The position effect depends on the setup. It is strong in fixed contexts and shrinks sharply in agents and controlled replay. Observational data overestimates it. But when the pages are supplied to the engine, order can still noticeably change the first place when real AI search engines read a fixed list (a single study, and some of the researchers are authors of the best-performing method).
4. Models have their own attribute weights. Rating and price dominate hotel choice; environmental certification is overweighted, and management replies are almost ineffective; authority labels can flip nearly 40% of paper recommendations. These come from simulations and controlled experiments, and show only what may happen in principle.
5. Do not trust the model's own account. The reasons it gives only partly match the weights it actually relies on.
6. Text that is "predictable" to the model is more likely to be cited. This is a newer finding, so far verified only to a limited extent.
7. Appearing, being cited and being recommended are three things. Several practitioners report from their own tests that many brands appear but are not recommended; conditions in the query change how the model evaluates the same brand.
8. The 2023 practice of "adding data and quotations" no longer works. Measure repeatedly and track stage by stage, rather than chasing one-off tricks.
