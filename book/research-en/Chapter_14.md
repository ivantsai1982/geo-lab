# Chapter 14: Content Websites: After the Traffic Is Intercepted, What Content Still Gets Cited and Clicked

> This is a case chapter. The earlier chapters covered the principles behind each stage of the pipeline; this chapter applies those principles to websites that "live on content", such as publishers, blogs, tool sites and affiliate review sites, and looks at what has actually happened to them in the face of AI answers.
>
> Principles applied: Chapter 2 (triggering), Chapter 3 (accessibility), Chapter 4 (retrieval and query rewriting), Chapter 6 (relevance), Chapter 7 (citation and absorption), Chapter 8 (content-level practices), Chapter 9 (measurement), Chapter 10 (traffic and commercial value).

## 1. Questions this chapter answers

1. Since AI answers appeared, how much traffic have content websites actually lost? What kind of traffic is it?
2. Why does being cited by AI often fail to bring clicks, or even a mention by name?
3. What kind of content still gets cited, and still gets clicked, in the era of AI answers?
4. After which changes did content websites observe more citations? Which changes did nothing, or even backfired?
5. How can you tell whether "AI traffic growth" means you did something right, or that the platform itself is growing?

## 2. Core principles

### Principle 14.1: AI answers keep most information needs inside the platform; content websites get a "selective residue"

The bargain of traditional search was this: the search engine takes your content for its index and gives you clicks in exchange. AI answers break this bargain. Users get what they want on the answer page and have no need to click out (see Principle 10.1 in Chapter 10).

For content websites, this mechanism has three consequences:

```
AI answer appears
  → Informational queries are "answered on the spot"
  → Clicks on traditional results fall (ranking unchanged, clicks lost)
  → The remaining clicks concentrate on what the answer cannot provide (transactions, brands, in-depth tools, subscription content)
```

- **Unchanged rankings with falling clicks** is the most typical signal. Impressions may hold steady or even rise, but the click-through rate collapses.
- **Residual traffic is selective.** The clicks AI sends out lean towards reference, academic, developer, tool, subscription and non-profit websites, and away from ad-dependent websites (Principle 10.2 in Chapter 10).
- Informational websites that depend on advertising and affiliate commissions are hit most directly, because their business model rests on the chain "information query → click → ad impression or referral sale", and AI answers cut exactly the middle of that chain.

### Principle 14.2: Cited ≠ clicked ≠ named ≠ absorbed

The easiest mistake for a content website is to treat "being cited" as the finish line. In fact there are at least four different events here, each determined by a different mechanism (Chapter 7):

| Event | Determined by | Meaning for a content website |
|---|---|---|
| Retrieved and listed as a source (citation) | Retrieval and relevance: whether the page matches the rewritten sub-queries (Chapters 4 and 6) | A necessary condition, but it produces no revenue by itself |
| The answer's content actually comes from your page (absorption) | Whether the page provides the specific facts, definitions, numbers and comparisons the answer needs | Determines your actual contribution to the answer |
| The answer text names your website (naming) | Attribution: the model usually names a source only "when a claim needs backing" | The source of brand exposure |
| The user clicks through (click) | Whether the answer has already met the need; whether you offer something the answer cannot | The source of traffic and revenue |

The four events narrow one after another. A website can be cited more than a thousand times, be named a single-digit number of times, and get clicks amounting to less than one percent of its total traffic.

### Principle 14.3: Content that gets cited is "readable, separable, fresh and irreplaceable"

Drawing on the earlier chapters, a content website must pass four gates at once to get into AI answers:

1. **Readable (Chapter 3)**: AI crawlers are not blocked, and the page can be fetched at its canonical URL. Blocking the crawlers means leaving this channel.
2. **Separable (Chapters 6 and 8)**: answers are taken by "passage", not by "whole page". If the first two or three sentences of each subsection can answer that subsection's question on their own, the content is easier to extract than a long article that only makes sense once read in full.
3. Fresh (Chapter 8): on time-sensitive topics (comparisons, prices, availability), newer pages are chosen more often; pages that are no longer updated may be replaced.
4. Irreplaceable (Chapters 5 and 7): if AI can piece your content together from ten other sources, it has no reason to cite you in particular. Exclusive data, first-hand testing, details of a specific market and the views of named experts are what an answer needs to "borrow".

### Principle 14.4: Search ranking and AI citation are two related but different systems

An AI answer rewrites one question into several sub-queries (query fan-out, Principle 4.2 in Chapter 4), and then picks passages from the results of each sub-query. Therefore:

- A high ranking for the main page does not mean it matches the sub-queries the model actually sends.
- A page that ranks very low, or not even in the first few pages, can still be cited because it happens to be the cleanest answer to one sub-query.
- Ranking still matters (pages ranked very far down are noticeably less likely to be cited), but it is only one of the entry conditions.

## 3. How strong is the evidence

### Traffic interception: the strongest evidence in this book

**Large-scale experiments with real users show**:

- In US desktop clickstream data, only 5.2% of ChatGPT conversations produced an external click, against 31.1% for Google queries; 74.4% of active ChatGPT households had never clicked an external link. After ChatGPT Search use expanded, traditional search queries fell by 9.4%, reaching 17.0% after 20 weeks.
- In the same study, the drop in search referrals varied by type of website: academic -32.8%, reference -26.5%, developer -15.1%, news -13.4%. Among the clicks ChatGPT sends out, the share going to ad-supported websites is 27.6 percentage points lower than for Google.
- In a pre-registered randomised field experiment, forcing the use of AI Mode reduced the external click-through rate by 18.8 percentage points; turning off AI Overviews (AIO) raised the click-through rate by 8.8 percentage points (compliance rate about 51%). AI Mode also lowered users' trust and satisfaction. The sample was about 1,100 people, the treatment period 7 days, skewed towards younger and more highly educated participants.
- In a quasi-experiment on Wikipedia, after AIO launched by default in the US, external search traffic to the English edition fell by 5.45% relative to the German edition and by 4.82% relative to the French edition. The authors infer that even for sources AIO cites frequently, citation is not enough to offset the loss of traffic.

**Repeated measurements and observations on real AI search engines found**:

- Browsing logs from 900 US adults show that about 18% of Google searches displayed AIO; when AIO appeared, 8% of visits clicked a search result, against 15% without AIO; clicks on sources cited inside AIO accounted for only about 1% of page visits with AIO; when AIO appeared, 26% of browsing sessions ended right there, against 16% without. This is an observational study, not a causal one.
- Users of answer engines hovered over only about 2 sources on average and clicked about 1; for traditional Google users the figures were 11.81 and 3.80 (a 2024 study).
- The rate at which AIO appeared on US queries rose from 42% to 67%; 60% of question-form queries showed an AI answer. AIO cited fewer long-tail domains.
- A cross-interface panel study published by an AI visibility vendor shows that 34.1% of AI assistant sessions had no external web step, against 19.5% of search sessions. The authors state explicitly that they draw no causal conclusions.

Scope: these studies cover overall traffic, not individual websites. They can show that "interception is real and sizeable", but they cannot tell you how much a particular website will lose. That depends on how many of your queries are informational and how many trigger an AI answer (Chapter 2).

### Cited vs absorbed

**Simulations or theoretical analysis suggest that, in principle,** (secondary analysis of a static snapshot, correlational only):

- The average number of citations per prompt is 6.88 for ChatGPT, 12.06 for Google and 16.35 for Perplexity; but the average influence of each fetched page on the answer is 0.2713, 0.0584 and 0.0646 respectively. The more sources listed, the less each source is used.
- Pages containing code, numbers, definitions or comparisons have 41%–77% higher influence; pages that simply adopt a Q&A format are slightly lower (0.0947 vs 0.1005).
- The absorption of news media sources (0.0726) is lower than that of encyclopaedic sources (0.2144).

**Repeated tests on real AI search engines found**: of 366,000 citations, news accounted for only 9.0%, and these were highly concentrated in a few large outlets. For news websites, "being cited" is itself a scarce resource.

Simulations or theoretical analysis suggest that, in principle, attaching citation links to an AI answer may raise users' trust in the answer, even when the links are invalid. This means the value of a citation to the platform (more trust) and its value to the cited website (clicks) are two different things.

### Causal attribution of AI traffic

Only two studies can currently answer directly whether "GEO brings traffic to content websites", and both are weak:

- **A single-site natural experiment** (authors from industry): total ChatGPT referral traffic grew 5.7 times, but untreated pages grew 3.5 times over the same period. With untreated pages on the same domain as the control, the level of treated pages jumped about 1.82 times (95% confidence interval 1.31–2.54), with robustness checks falling between 1.8 and 2.3 times; but the placebo test gave p=0.16, so this counts only as suggestive evidence. The treatment was a bundle of measures: URL canonicalisation, mining demand from AI crawlers' 404 logs, question-form headings, and summaries that stand on their own. The study found no flywheel effect of AEO driving organic search; over the same period Google organic clicks fell by about 25%.
- **A platform self-test** (authors from the platform): adding annotations to images in the form of "queries users would search", and building collection pages and internal links, produced 1.18 times the sessions of the control group in a 4-week A/B test; but the traffic metric definitions and statistical disclosure are insufficient, and some numbers in the paper are inconsistent with each other.

The conclusion of a review study is that no research so far shows a stable, longitudinal, cross-platform causal effect of GEO on organic discoverability or conversion (Chapter 0, Principle 10.3 in Chapter 10).

### Practitioner evidence

Many of the cases in this chapter come from data on practitioners' own websites. Their value is that they are concrete and close to practice; their limitation is that the samples are usually a single site, with no control, unable to rule out seasonal and platform changes. Each case below states its evidence strength.

## 4. Debates and counterexamples

### Debate 1: Is AI traffic "small but high quality", or just "small"?

| Observations on one side | Observations on the other side |
|---|---|
| Practitioners report from their own tests: traffic from AI answers is less than 2% of organic traffic, but has a lower bounce rate, longer dwell time and higher intent. | Practitioners report from their own tests: one author at first believed his high engagement came from AI citations, then checked the sources and corrected himself: at current traffic levels, the referral traffic was not coming from AI; some AI traffic is recorded as "direct", so attribution itself is murky. |
| Practitioners report from their own tests: a new domain went from 0 to 93 citations in 90 days, and reported a conversion rate of about 4.8% for AI referral traffic against about 0.9% for organic search. | Practitioners report from their own tests: one website cited more than 10,000 times a month by AI assistants got referral traffic of less than one percent of total sessions; another affiliate website was cited about 8,000 times in 50 days and received only 1–2 AI-sourced visits a day. |

**The basis on each side**: the conversion figures on the "high quality" side mostly come from single sites with very small denominators, and conversion rates fluctuate wildly with small samples; the figures on the "small" side also come from single sites, but their direction is consistent with the large-scale studies (Section 3). Both can be true at once: the few visitors AI brings may indeed have stronger intent, but the total is not enough to replace the search traffic that has been intercepted. For websites that depend on advertising or affiliate commissions, the latter is what decides the matter.

### Debate 2: Does updating content raise or hurt citations?

- Practitioners report from their own tests: after deliberately leaving a page un-updated for two months, ChatGPT stopped citing it completely and cited a newer, more direct short community post instead.
- One practitioner observed that after updating a page that had been cited steadily (adding subsections, refreshing data), citations dropped markedly, recovered only partly after several weeks, and did not return to the original level.
- One practitioner observed that merely moving the answer block further down turned a page with the same content from a top-three citation into an invisible one.
- Practitioners report from their own tests: an audit of 158 articles found that about 43% of articles published more than two months earlier were cited, against about 7% of newer ones.

**How to read this**: "freshness" and "structural stability" are two different variables. Updating the date and refreshing data may help on time-sensitive topics; but if an update buries the answer that sat at the top and could be extracted directly inside a new passage, it breaks the extraction path ("separable" in Principle 14.3). As for "older articles having a higher citation rate", this more likely reflects that pages need time to be indexed and to accumulate external signals, rather than "old is better than new". These are all single-site observations and cannot be compared directly with each other.

### Debate 3: Are "versions for machines", such as Markdown mirrors and llms.txt, any use?

- Practitioners report from their own tests: after providing raw Markdown versions of popular articles, the AI crawl rate doubled, and Perplexity and others cited them faster. (This report reads like promotion and has not been independently verified.)
- One practitioner observed that in an A/B test on 381 pages across six websites, pages offering Markdown gained only about 1 additional bot visit (median) over three weeks.
- Practitioners report from their own tests: serving Markdown to AI crawlers for 16 blog URLs increased sessions by 52%; but untreated blog pages grew 43% over the same period, so the gain cannot be attributed to Markdown.
- Practitioners report from their own tests: after deploying Markdown mirrors, Google fetched them within days; but ChatGPT and Perplexity still cited the HTML versions, and the citation rate did not change within 60 days. Another set of server logs showed that the ChatGPT user-agent that fetches pages in real time never fetched the Markdown copies; the Markdown was read only by indexing crawlers.

**Direction of the conclusion**: controlled tests found no clear effect; the reports claiming large effects lack controls. For content websites, what actually gets cited is still the page at the canonical URL, so **the page itself must carry all the content**. This is consistent with Principle 3.1 in Chapter 3, "if it can't be read, it doesn't exist": what matters is whether crawlers can read the canonical page, not whether you open a separate copy.

### Debate 4: How closely are ranking and citation related?

- Practitioners' repeated, controlled tests found that an AI tools directory website analysed about 196,000 of its own AI citations, and some of the cited pages ranked 80th in traditional search or did not rank at all.
- Practitioners report from their own tests: in manual checks of 80 queries across 4 websites, only 31% of pages ranking in Google's top three were cited by AIO; beyond 10th place, the citation rate fell to 12%.
- Practitioners report from their own tests: in an analysis of about 350,000 B2B SaaS articles, only about 14% of AI-cited URLs appeared in Google's top 20.
- An observation in the opposite direction: one practitioner observed that an article was cited ten minutes after publication, because it reached first place on Google as soon as it went live and was retrieved in real time.

**How to read this**: the two accounts do not contradict each other. Ranking is one of the "admission tickets" to retrieval (far down the ranking, the chance drops noticeably), but once inside, which page is chosen depends on whether its passage answers the sub-query most directly. In addition, different AI products rely on different search indexes behind the scenes (Chapters 4 and 12), so matching Google rankings against citations in all AI products may itself be a mismatch.

## 5. Cases

The cases are grouped by the principle they illustrate. Each case follows the order "situation → principle → what was done / what was observed → what worked and what did not → caveats".

### Case group A: Interception: ranking unchanged, clicks gone (Principle 14.1)

**A1. French affiliate review site: one week before vs one week after AIO launched**

- **Situation**: an independent French affiliate review website (product reviews, testing).
- Observation: comparing the corresponding weeks before and after AIO launched in France (22 July), Google search clicks fell 25% while impressions were essentially flat (+0.1%). For one query ranked first, the click-through rate fell from 54.5% to 16.7% within a week. Revenue fell nearly 47%, about twice the drop in traffic. Sales also fell, which shows that not only were there fewer visitors, but the visitors who remained converted worse.
- Principle: unchanged impressions with collapsing clicks is exactly the signature of "answered on the spot". Revenue falling more than traffic shows that AI answers ate precisely the most valuable part of the affiliate site's clicks.
- Evidence strength: practitioners report from their own tests. Only two weeks, before and after, no control, but the direction is consistent with the large-scale studies.
- Caveat: informational and review-type queries are hit first; the author also warns that the impact will at least be concentrated on this type of query.

A2. Small law firm website: two years of change on the same informational page

- Observation: one practitioner observed that a typical informational page received about 800 clicks and 4,000–5,000 impressions a month two years ago; now, at the same ranking, it gets 1,200 impressions and 90 clicks, because AI Overviews answer the question before the user scrolls. What still supports the traffic is brand search and direct referrals from existing clients.
- Principle: residual traffic concentrates where AI answers cannot reach: brand intent and transactional intent.

A3. A travel guide website and authors who make a living from content

- Observation: one practitioner observed that a website with about 2,000 Portugal travel guides, with rankings largely unchanged, saw traffic fall 40% from the previous year and 70% from its 2024 peak. The website monetises through display ads. Another practitioner observed that authors who make a living from content have seen traffic and income fall by about 80%.
- Principle: ad-dependent informational websites are exactly the type that the large-scale studies found AI clicks "moving away from".
- A reflection worth noting: the travel guide author points out that small, real-time details such as changed bus routes, attractions closed for repairs, and tips for getting a ride at the airport used to come from small websites like his. If these websites stop updating because their traffic dries up, AI answers will also have fewer sources of fresh information. This is an ecosystem-level concern, and no study has quantified it yet.

A4. The split between informational and transactional

- Observation: one practitioner observed that informational queries have shifted heavily to AI answers, with blog traffic down 40% year on year, while transactional queries have barely changed. The author's advice is not to measure the two with one total figure, or you will wrongly conclude that "SEO is dead".
- Another observation: one practitioner observed that a client website's impressions on informational keywords rose while its click-through rate fell by about 25%, even though the website was cited directly by AI summaries.
- Principle: splitting traffic by query intent is the first step in judging the extent of interception (Chapter 2: the triggering rate depends on the form of the query).

### Case group B: Cited, but no clicks and no naming (Principle 14.2)

**B1. Asian streaming availability website: over 10,000 citations, less than one percent of traffic**

- **Situation**: a 12-week-old website that answers "where can I watch a given title in a given Asian country". From the start it did not compete with large aggregators for traditional rankings, but optimised for AI answers.
- Observation: it became the number-one cited source in its niche query set, accounting for 65% of all page citations, ahead of the large streaming platforms' own domains and the aggregators; within 30 days Copilot cited it more than 10,000 times, and citations from ChatGPT and Gemini were also growing. But all these citations together brought direct referral traffic of less than one percent of the website's sessions: the assistants used its data to answer the question, and users had no need to visit.
- What the author judged to work (in order of impact): country-specific long-tail pages ("where to watch X in Pakistan"); comparison-format content ("service A vs service B"); question-form headings followed by a 2–3 sentence answer; dated availability pages ("as of August 2026").
- Principle: this is an extreme example of "absorbed deeply, clicked rarely". What the answer needs is exactly one fact (where to watch it), and once the answer states the fact, there is no reason to click.
- Evidence strength: practitioners report from their own tests, single site.
- The author's own conclusion: the citations are accumulating, but they behave like brand advertising rather than a source of traffic.

B2. News website: about 700 pages cited, website name mentioned only 5 times

- Situation: an English-language news website, with 84% of traffic from the US, and a domain about three months old.
- Observation: about 700 pages were cited by AI, but the brand name was mentioned only 5 times, about one naming per 140 citations. Citations were distributed as ChatGPT 659, AI Overviews 32, AI Mode 22, Gemini 0.
- An explanation offered by participants in the discussion: citation is a retrieval mechanism, so a page that ranks and matches the query gets pulled in; naming is an attribution mechanism, so the model mostly names a source when a claim needs backing. This website publishes a large volume of quickly rewritten news, and other outlets report the same story within the same hour, so nothing in its content "needs" its name.
- Direction for the next test: do more original work (its own statistics, numbers nobody else has), put the author's name next to the numbers, and then compare the naming rate of these articles.
- Another open question: Gemini's citation count is zero, while ChatGPT's is in the hundreds. Participants judged this to be a retrieval gap rather than a naming problem: Gemini did not pull these pages into its candidate set at all.
- Principle: cited ≠ named; homogeneous news lacks "irreplaceable" claims (Principle 14.3). Each engine has a different set of sources (Principle 4.1 in Chapter 4).
- Evidence strength: the main case is "one practitioner observed"; the retrieval-gap judgement is "practitioners report from their own tests".

B3. More single-site data on "many citations, few clicks"

| Website type | Observation | Evidence strength |
|---|---|---|
| 6 informational pages | 9,600 impressions from Google AI citations in 15 days, bringing only 6 clicks | Practitioners report from their own tests |
| A website | 39,000 citations, 300 clicks, 0 from Copilot | One practitioner observed |
| News website | Hundreds of ChatGPT real-time fetch requests in one day, but only 8 of 2,270 visitors over 4 days came from AI | One practitioner observed |
| Website with very low organic traffic | Bing AI cites it about 200 times a day; ChatGPT brings 3–5 sessions a day | Practitioners report from their own tests |
| A website | 116,061 impressions in the AI section of GSC over 53 days; Bing reports about 338 citations a day | Practitioners report from their own tests |

Caveat: the definition of "citation count" varies enormously between tools (see Case group G), so these numbers show only orders of magnitude and cannot be compared with each other.

### Case group C: What content still gets cited (Principle 14.3, "irreplaceable")

**C1. Streaming guide website: data-based comparison pages + country pages + allowing crawlers, 185,600 Copilot citations in three months**

- **Situation**: a free streaming discovery platform that answers "where can I watch this title in my country" for 34 Asian markets.
- Observation (based on the new AI performance report in Bing Webmaster Tools): cited 185,600 times in Copilot answers over three months; the number of pages cited each day rose from fewer than 100 in June to about 400; over the same period, Bing search clicks rose from almost zero to about 1,500 a day.
- The surprise: the website was originally built for Indian streaming, but what AI used it for most was comparing anime platforms (7 of the top 12 queries), followed by Pakistani dramas. For these queries, its pages supplied 61%–85% of the answer content.
- Three things the author believes made the difference:
  1. Comparison pages built on data rather than opinion: "which platform has more X" is answered with real catalogue counts.
  2. Separate pages per country: a US-centred guide is wrong for Jakarta or Karachi.
  3. Allowing AI crawlers: in June the author had blocked AI crawlers because of bandwidth issues, and the moment of unblocking was exactly the turning point of the curve.
- Principle: Chapter 3 (accessibility) + Principle 4.3 in Chapter 4 (the market gate: AI seems able to judge whether a source genuinely covers a given market) + irreplaceable data.
- Evidence strength: practitioners report from their own tests, single site, three measures bundled, so their separate effects cannot be isolated.
- Caveat: this may be the same kind of website as B1; high citation and low clicks can coexist. In this case Bing clicks also grew, which shows that outside "fact lookup" queries, some users still click through.

C2. Original research becomes the only page listed as the top source

- Observation: practitioners report from their own tests that a publisher released an original study (auditing the AI visibility of 2,141 French training organisations, average score 40.7/100), and it became the only page on that website that Perplexity listed as the first source, ranking ahead of much larger domains on related queries. The author also observed that French-language answers seem less dominated by large authoritative domains than English-language answers.
- Principle: original numbers are what an answer "needs to borrow" (Principle 14.3); competitive density differs across language markets (Principle 4.3 in Chapter 4, Chapter 12).
- Caveat: a single page in the French market; this cannot be generalised to "original research always ranks first".

C3. Definition-type content takes most AIO impressions

- Observation: practitioners report from their own tests that after Google Search Console launched its generative AI performance report in June, data from the first 35 days for a group of B2B domains showed: glossary / definition pages accounted for 55% of AIO impressions, blog / tutorial / explainer pages for 32%, and product / category pages for only 10%. The best-performing single URL type was glossary entries on financial concepts with a cost per click close to zero, whose AIO impressions exceeded those of all product pages combined. The AIO flag in keyword tools captured only 27% of actual impressions; the missing part was mainly in mid- and long-tail definition queries.
- Corroboration: one practitioner observed, testing 5 engines weekly with 168 fixed queries, that definition pages were cited far more often than other content; a client's "what is…" page of about 200 words, with no backlinks, was cited consistently by ChatGPT and Perplexity, while large cornerstone articles were ignored.
- Principle: a definition is the content unit most easily "separated" and "absorbed" (Chapter 7: pages containing definitions, numbers and comparisons have higher absorption).
- Caveat: "impressions" are not clicks. Definition queries are also exactly the ones most easily answered on the spot; what these pages gain is mostly impressions and brand exposure, not traffic.

C4. Large programmatic website: crawl volume unrelated to citation

- Observation: practitioners report from their own tests that a programmatic directory website of about 100,000 pages, without ads, was crawled about 430,000 times by AI crawlers in 30 days. But crawl volume said nothing at all about whether pages were cited: the cited pages were those easiest to re-verify, one fact per page with stable URLs.
- Corroboration: one practitioner observed that over 58 days, 12 of 13 known AI crawlers visited their test website, but which pages got cited followed a completely different logic.
- Principle: accessibility is a necessary condition, not a sufficient one (Chapter 3 → Chapter 6).

C5. A SaaS not yet launched: 13 blog posts, 5,300 Copilot citations

- Observation: practitioners report from their own tests that a website whose product was still in development, with only a landing page and 13 blog posts documenting its own research process, and no GEO-specific work at all (no llms.txt, no AI-specific schema), showed in the Bing report more than 5,300 citations by Copilot and its partners, growing month on month. The author wrote about "questions I could not find good answers to myself, so I documented them".
- Principle: covering specific, unanswered questions matters more than brand size (Principle 5.3 in Chapter 5: the brand prior only comes into play when the information cannot be told apart).
- Caveat: the author provided no click data; the citation count comes from a single engine's report.

C6. Experience and named views: content that "cannot be summarised away"

- One practitioner observed that on immigration law websites, traffic to definition pages and pricing pages fell sharply, while content in which named lawyers published distinctive views performed better. The author's judgement: evergreen content that AI Overviews can summarise completely no longer has a moat.
- One practitioner observed that an original article making specific claims about the AI economy had an average engagement time of 6 minutes 15 seconds, while generic explainers on the same site had under 2 minutes. (The same author later corrected this: these high-engagement visitors did not come from AI citations; see Debate 1. This case illustrates the relationship between content type and engagement, not AI traffic.)
- One practitioner observed that an in-depth list article that personally tested every platform, with real screenshots, brought in 50% of the website's traffic.
- Principle: Principle 10.2 in Chapter 10 notes that experience-based content benefits relatively in the AI answer environment; Principle 7.5 in Chapter 7 warns that during synthesis AI rewrites first-person testimony into generalised advice. Experience has value in itself, but there is no guarantee it appears under your name.

### Case group D: Structure and extractability (Principle 14.3, "separable")

**D1. A citation audit of 158 articles**

- **Observation**: practitioners report from their own tests (the audit was carried out by an outside vendor; the author published the prompt set and scan IDs). Of 158 publications, 78 were audited against 28 criteria, tracking ChatGPT, Perplexity, Google AI Overviews and Claude:
  - Writing quality was almost irrelevant: cited articles had an average quality score of 60.4, uncited ones 62.5.
  - The publishing platform was a multiplier: with the same author and the same material, about 52% were cited on industry publishing platforms, and 0% on both the company blog and the personal homepage.
  - Articles with question-form H2s were cited 19% more; tables / checklists 18% more.
  - Any promotional tone reduced citations by 26%.
  - Formats such as short content, narrow vertical headings and single-company case studies got zero citations.
- Principle: the difference between publishing platforms corresponds to the third-party source ecosystem in Chapter 5; promotional tone being filtered out relates to the discussion of "claim-style content" in Chapter 11.
- Caveat: this is a correlational audit, not a controlled experiment; the quality scoring method was not disclosed.

D2. B2B client: AIO citations for 7 of 10 queries in 12 weeks

- Situation: the client already ranked on the first or second page for 7 of its 10 target queries, but had zero AIO citations. The operator's judgement: this was not a ranking problem but a structure and trust problem.
- What was done: in month 1, a content audit and structural rewrite (openings that answer directly, FAQ schema added to 8 target pages), with the first AIO citation appearing on day 18; in month 2, off-site mentions, with third-party mentions rising from 2 (both directory listings) to more than 12; in month 3, freshness maintenance and monitoring.
- Result: after 12 weeks, 7 of the 10 queries produced citations; brand search volume in GSC rose 28%; organic rankings did not change at all.
- What did not work: FAQ questions optimised for keywords were completely ignored; only the phrasings real people actually type, even somewhat awkward ones, worked. Generic community comments gave no signal; only answers based on real experience helped.
- The 3 queries that failed: occupied by big brands, impossible to break into.
- Evidence strength: practitioners report from their own tests, single client, several measures bundled.
- Caveat: this case illustrates both Principle 14.4 (ranking present, citation absent) and Chapter 5 (third-party mentions).

D3. A blog rewrite experiment at a SaaS platform

- Observation: practitioners report from their own tests that after writing the blog in the form of real user questions, share of voice rose from 38% to 100% within 3 weeks, and 70% of tracked questions improved; after adding a table of contents, clicks rose 23% and AI visits 60% over 4 weeks; after changing titles into questions, AI visits rose 58% over 4 weeks.
- What did not work: adding a "key takeaways" block at the top of the page.
- Caveat: the time windows of the changes overlap, and there is no control group; share of voice depends on the query set chosen (Principle 9.4 in Chapter 9).

D4. From long articles to standalone answer blocks

- One practitioner observed that some articles ranking 6th–9th with good impressions had never been cited by AIO, and what they had in common was being written as flowing long-form prose; rewriting the first two or three sentences under each H2 into an answer that could stand alone for that subheading made the difference.
- One practitioner observed that a "what is the difference between X and Y" FAQ of only two short paragraphs, with no backlinks, was cited by AIO, while a 3,000-word optimised guide on the same topic was not.
- Practitioners report from their own tests: a client website ranked in Google's top three but was not cited by ChatGPT; instead, sites with lower authority but concise bulleted summaries were cited.
- One practitioner observed that changing FAQs from paragraph form to "one-sentence definition + list of key points" increased citations 3.2-fold within 6 weeks.
- Principle: answers are extracted passage by passage (Principle 14.3).
- Tension with the research: static snapshot analysis shows that simply adopting a Q&A format has no positive correlation with absorption (Section 3). A reasonable reading is that what works is not the "format" itself, but "giving a specific, self-contained answer at the start". Wrapping passages without substance in a Q&A format will not help.

D5. Starting from real phrasings

- Practitioners report from their own tests: tracking ChatGPT's high-traffic questions in their own niche and writing articles that answer those questions directly led to hundreds of ChatGPT mentions in a short time.
- One practitioner observed that finding real customers' questions on forums and writing the most direct answers led, three months later, to appearances in Perplexity long-tail queries, although these articles did not rank well on Google.
- One practitioner observed that sorting the expanded sub-queries supplied by an AI tracking tool by frequency, and writing content for them one by one, got some articles cited.
- Practitioners report from their own tests: taking the questions behind their pages that ranked high on Google and asking a model that browses the web, only 2 of 8 questions cited their own site, even though some pages ranked 2nd.
- Principle: what has to match is the sub-queries the model actually sends, not your keyword list (Principle 14.4, Principle 4.2 in Chapter 4).

### Case group E: Freshness and the risk of updating (Principle 14.3, "fresh")

**E1. Replaced after two months without updates**

- Practitioners report from their own tests: after deliberately leaving a page un-updated for two months (topic and keywords unchanged), ChatGPT stopped citing it completely and instead cited a short community post whose author had only 300 followers, but which was more recently updated and answered more directly.
- Practitioners report from their own tests: finance content ranking 3rd–5th on Google was cited by AI only about 20% of the time; content older than 6 months seemed to be noticeably downweighted.

**E2. Comparison content has a short visibility window**

- One practitioner observed that a "platform A vs platform B" article was cited in AI answers continuously for about 6 weeks and then suddenly disappeared. The author speculates that comparison content stops being cited as soon as it becomes even slightly outdated.

E3. Updating actually lost citations

- See Debate 2. One practitioner observed that after a "content refresh" buried the Q&A block under new passages, AI citations fell 40%; the advice is to change one section at a time and wait a week before changing the next.

E4. Large domains pushed out of the answer by an update

- Practitioners report from their own tests: one author observed that Perplexity cited her new articles within two hours; 24 hours after she updated content, domains with far higher authority than her own sites disappeared from the answer completely.

Principle and caveats: real-time retrieval engines such as Perplexity react very quickly to new content; but "fast in" also means "fast out". Freshness matters most for time-sensitive topics such as comparisons, prices and availability. All of these are single-site observations, and it cannot be determined whether "freshness" itself is the cause, or whether the update also made the answer more direct.

### Case group F: Accessibility: to block or not to block (Chapter 3)

- **The turning point of allowing crawlers**: in C1, the moment the streaming guide website unblocked AI crawlers was exactly the turning point of the citation curve (practitioners report from their own tests).
- **Accidental blocking**: one practitioner observed that by allowing only Googlebot in robots.txt, they had accidentally blocked GPTBot and ClaudeBot, making their pages invisible to AI crawlers; another of their best-performing articles lost its citations 4 months later.
- A counterexample of platform-level blocking: practitioners report from their own tests that after a large community platform blocked crawlers at the domain level in mid-August, its share of ChatGPT citations plunged within days, while its share in Google AI Overviews barely changed, and its rankings did not change either. Same content, same rankings, and one channel disappeared (see Chapter 15 for details).
- Related evidence from a large-scale study: 79% of domains blocked at least one AI crawler; blockers' average ChatGPT referrals were actually slightly higher (6.48 vs 4.48). This is a correlation, not causation; the researchers' interpretation is that blocking training crawlers does not stop ChatGPT's referrals at answer time.
- Principle: distinguish "crawlers for training" from "crawlers for real-time retrieval" (Chapter 3). Blocking decisions should target specific crawlers rather than apply one blanket rule.
- A content website's dilemma: one practitioner observed that a content website operator, averaging 15,000 generative AI feature impressions a day and believing most of them were zero-click, was considering turning off Google's newly launched generative AI usage controls. This is a real business trade-off: opting out protects the content from being "used for free", but also gives up impressions and brand exposure. There is currently no evidence on which side pays off better.

### Case group G: Measurement and attribution (Chapters 9 and 10)

**G1. A single-site natural experiment: how much is left after subtracting platform growth**

- See Section 3. Of the raw 5.7-fold growth, a large part was the platform itself growing (untreated pages also grew 3.5 times); the single-day spike of 38.2 times can even less be taken as a causal effect.
- **Lesson**: claims of "AI traffic grew X times" without a same-domain control group are almost always overestimates.

G2. Sensitivity to wording: one extra word, a different set of sources

- Practitioners report from their own tests: one of their own pages was cited for a certain exact query, and disappeared completely when one word was added to the same query. With the same query and the same wording, it was cited at 3:00 and not cited at 18:00 on the same day. The advice is to freeze about 10 real buyer phrasings, run them regularly, and watch the change in citation share across the whole set; a single answer is noise.
- Practitioners report from their own tests: the same prompt gives different answers in the API and the web version, with different retrieval and citations, so one interface should be fixed for tracking.
- Practitioners' repeated, controlled tests found that the same query was cited about 50% of the time in the ChatGPT app, but 0 times out of 30 through the API; repeating the same prompt about 10 times produced about 5 citations; searchers in different countries saw completely different sets of sources.

G3. An 8-fold difference between tools

- One practitioner observed that a YMYL website with about 790,000 organic visits a month showed about 512,000 and 62,000 citations in two AI visibility tools, a difference of about 8 times. The author speculates that the former counted every appearance each time a query was rerun, while the latter sampled its own index, so the two counted different populations.
- Practitioners report from their own tests: mention counts for the same website were also inconsistent across tools.

G4. The platforms' own reports

- Practitioners report from their own tests: the AI reports in Google Search Console and Bing Webmaster Tools provide first-hand data that was not available before (for example, a chocolate database website had a cumulative 9,093 generative AI impressions across 579 URLs, with daily impressions rising from 30–40 to 200–280).
- But note: "impressions" in the Bing report are not "citations", and the granularity is coarse; one practitioner observed that a page ranked 94th in GSC was cited 64 times on Bing last month. Using Google rankings to explain citations in all AI products may be a mismatch.

G5. Monitoring can see changes earlier than traffic

- Practitioners report from their own tests: using the API with a scheduler to query topic variants daily and parse the citations once detected a rise in a client blog's visibility 3 weeks earlier than the website analytics tool.
- Caveat: this does not conflict with G2's "the API and the app give different results": what is monitored is the trend, not the absolute value; but the trend is also valid only for the one interface you use consistently.

G6. A self-correcting case

- Practitioners report from their own tests: one author first claimed that the high-engagement visitors of a new website came from AI citations, then checked source-level data and publicly corrected himself: at current traffic levels, the referral traffic was not coming from AI, and there were no referral sources from ChatGPT or Perplexity yet; some AI traffic is recorded as direct, which makes attribution for small websites very murky.
- Lesson: check the source first, then draw conclusions.

## 6. What to do

### Diagnose first: what situation is your website in?

```
1. Split traffic by query intent (informational / transactional / brand)
   → Find informational queries with flat impressions and falling clicks: this is the interception zone
2. Check accessibility: robots.txt, CDN and firewall settings; list each AI crawler that is allowed or blocked
3. Check platform reports: the GSC generative AI report and the Bing AI report; see which URL types get AI impressions
4. Build a fixed query set: use real user wording, freeze it, rerun it regularly
5. Control group: for any change, keep untreated pages on the same domain for comparison
```

### Practical measures

| Measure | Evidence strength | Notes |
|---|---|---|
| Accept that informational clicks will fall, and measure traffic separately by intent | Large-scale experiments with real users | Interception is the conclusion with the strongest evidence in this book (Chapter 10) |
| Confirm that AI real-time retrieval crawlers can fetch the page at its canonical URL | Practitioners report from their own tests (several cases point the same way); consistent with the principles in Chapter 3 | Distinguish training crawlers from retrieval crawlers; do not apply one blanket rule |
| Have the first two or three sentences of each subsection answer that section's question on their own | Practitioners report from their own tests (several single-site cases); the most robust correlation in controlled experiments | What works is "the specific answer comes first", not the Q&A format itself |
| Provide what an answer needs to borrow: original numbers, first-hand testing, details of a specific market, views of named experts | Practitioners report from their own tests; static analysis shows that pages containing numbers, definitions and comparisons have higher absorption (correlational) | Content that others can piece together gives no reason to be cited |
| Design questions and headings with real users' wording | Practitioners report from their own tests | There are quite a few cases where questions rewritten according to keyword tools were ignored |
| Maintain update dates and data for definition, comparison and availability content | Practitioners report from their own tests | Time-sensitive topics are the most sensitive to freshness |
| When updating, keep the existing answer position, and change one thing at a time | One practitioner observed | Avoid breaking passages that are already being extracted |
| One topic per page, stable URLs, so pages are easy to re-verify | Practitioners report from their own tests | Especially important for programmatic websites |
| Take part on third-party platforms (industry publishing platforms, communities) with real experience | Practitioners report from their own tests | See Chapters 5 and 15; generic comments do not work |
| When measuring, look at "the trend of citation share on a fixed query set", not single results | Practitioners' repeated, controlled tests | See Chapter 9 |
| Use a same-domain control group when evaluating AI traffic | Large-scale experiments with real users (quasi-experimental, suggestive) | Otherwise platform growth will be mistaken for an optimisation effect |
| Treat "citations" as a brand exposure metric, and measure "clicks and revenue" separately | Large-scale studies + several single-site cases point the same way | Do not use citation counts to prove traffic value |

### Adjustments at the business-model level (strategic judgement, not empirical conclusions)

The following are directions inferred from the evidence, not validated prescriptions:

- **Ad-dependent informational websites**: informational clicks are the most heavily intercepted part. One direction to consider is adding what AI answers cannot provide: interactive tools, continuously updated databases, subscription content, communities. Large-scale studies show that AI's residual clicks lean towards tool, reference and subscription websites.
- **Affiliate review sites**: "best X" queries are an area AI covers heavily, and third-party comparison pages are cited most for these queries. In-depth reviews with first-hand testing and original evidence stand a better chance than restated specifications. But even when cited, conversion may fall (Case A1).
- News websites: homogeneous breaking news is hard to get named. Original investigations, exclusive data and named authors are more likely to earn naming.
- Providing your own AI answers: large-scale experiments with real users show that after a major newspaper added cited AI answers to its on-site search, readers searched more and stayed longer on the site, each reader opened slightly more articles, and reading spread to less popular topics. This route keeps follow-up questions on your own website. But this is only engagement data from a single publisher, with no revenue or subscription data (see Principle 10.1 in Chapter 10).
- Tool and database websites: the easiest to get cited, and also the easiest to be "used up and left" (Cases B1, C1). Citations can be treated as brand building, and the operations that can be completed on the page (filtering, comparing, alerts) can be made more useful than the answer.

### Do not do

- **Do not treat "number of citations" as proof of traffic or revenue.** There are many cases of tens of thousands of citations with less than one percent of clicks.
- **Do not look only at the raw growth multiple of AI traffic.** The platforms themselves are growing fast; multiples without a control group are almost always overestimates.
- Do not draw conclusions from a single query or the results of a single interface. One word of difference in wording, a few hours of difference in time, or the gap between the API and the app can all produce completely different results.
- Do not block all AI crawlers with one blanket rule to save bandwidth, unless you have already decided to leave this channel.
- Do not publish rankings on your own website that put yourself first. One practitioner observed that such self-serving lists are being downweighted, and may even end up giving competitors exposure.
- Do not use a promotional tone in content. An audit shows that promotional wording is associated with fewer citations.
- Do not change the structure of a large number of pages in a single redesign. Extraction paths that are already cited may break, and you will not be able to tell which change made the difference.

### Already outdated or unproven practices

- **"Adding data and quotations raises visibility by 40%"**: this number holds only on the condition that the page is already among a fixed set of 5 candidate documents (Chapter 0); it does not mean the page can be retrieved, still less that traffic will increase.
- **Making long articles even longer ("skyscraper" content)**: several single-site observations show no additional benefit beyond a certain length; practitioners' repeated, controlled tests found that on Perplexity returns level off above 1,800 words (the sample was only 14 articles, and the author also warns that the sample is small).
- Providing separate Markdown versions for AI crawlers and publishing llms.txt: controlled tests found no clear effect (Debate 3). It is cheap and can be done, but do not expect it to change citations.
- Adding a "key takeaways" block at the top of the page: ineffective in at least one experiment.
- Relying only on FAQ schema or structured data: practitioners report from their own tests that structured data helps but is not the key factor; another single-site observation reported a positive result but lacked a control; in static analysis, a plain Q&A format had no positive correlation with absorption.

## 7. Key points

1. **Interception is real, and it is the conclusion with the strongest evidence in this book.** Only 5.2% of ChatGPT conversations produce an external click (31.1% for Google); when AIO appears, the click-through rate on traditional results roughly halves; clicks on the cited sources themselves account for only about 1%. Informational, ad-dependent websites are hit most directly.
2. **Unchanged rankings, flat impressions and falling clicks are the typical signature of AI interception.** Traffic needs to be split by query intent; transactional and brand queries are affected much less.
3. Being cited, absorbed, named and clicked are four different things. Tens of thousands of citations with less than one percent of clicks is common on fact-lookup websites. Citation is closer to brand exposure than to a source of traffic.
4. The content that still gets cited is readable, separable, fresh and irreplaceable. Original numbers, details of specific markets, definitions, data-based comparisons and first-hand testing are cited more often than generic explainers.
5. Ranking and citation are two related but different systems. Ranking is one of the entry conditions, but what gets chosen is the passage that answers the sub-query most directly; pages that rank very low can also be cited.
6. Accessibility is a switch. Cases in both directions, unblocking becoming the turning point of the citation curve and citation share plunging after a platform blocked crawlers, show the same thing: if it can't be read, it doesn't exist.
7. Measurement needs controls, fixed queries, a fixed interface and a focus on trends. Platform growth, sensitivity to wording, differences between the API and the app, and differences in how tools count can all badly distort uncontrolled numbers.
8. No research so far proves that GEO reliably brings traffic or revenue to content websites. The only quasi-experiment shows a net effect of about 1.8–2.3 times, and it is only suggestive evidence. Treating GEO as brand building and defence fits the current evidence better than treating it as an engine of traffic growth.
