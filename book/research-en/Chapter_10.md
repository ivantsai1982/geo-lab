# Chapter 10: Traffic and Commercial Value

> The book's main thread: triggering → accessibility → retrieval → selection/ranking → citation → absorption → **user behavior**
>
> The earlier chapters discussed "how to get into the answer". This chapter deals with the last segment of the pipeline: once you are in the answer, will users click through, and will they buy? This is the chapter with the strongest evidence in the book, and the conclusions drawn from the strongest evidence are not optimistic.

## 1. Questions this chapter answers

1. Since AI search appeared, have the clicks websites receive gone up or down? By how much have they fallen?
2. Where does the remaining traffic go? Which kinds of content are hurt, and which actually benefit?
3. After doing GEO, how much of the traffic growth comes from optimization, and how much is simply the platform itself growing?
4. If "being cited by AI" brings no clicks, what is its commercial value?
5. With incomplete attribution tools, how can you measure the commercial effect of GEO without fooling yourself?

## 2. Core principles

### Principle 10.1: AI search keeps most demand inside the platform

The business model of traditional search engines is "sending traffic": the user asks, the engine returns a list of links, and the user clicks out. Websites trade content for clicks.

The model of generative engines is "answering": the engine reads and integrates content from several sources and gives the answer directly. The user's question is resolved inside the platform, and the reasons to click out shrink sharply.

The causal chain is simple:

```
The more complete the answer → the less the user needs to click → the fewer clicks the source website receives
          → being cited ≠ being clicked
```

This is not caused by "falling rankings". A website may still hold its original position, or even be cited directly in the answer, yet still lose clicks. This is why many websites see "impressions flat or rising, click-through rate falling".

**But this causal chain has a precondition: the answer is provided by a third-party platform.** Large-scale experiments with real users show that the situation differs when the website itself provides the answer. A large newspaper ran a randomized field experiment in its on-site search (about 38,000 readers, 38 days): the treatment group saw an AI answer with citations above the regular search results. As a result, the share of searches followed by a click on a regular result fell by 20.8 percentage points, and article opens per search fell by about 19%; but readers' number of searches rose by about 29%, article opens per reader actually rose by about 5%, and the share of sessions ending after a search did not change. The reason is that follow-up questions stayed on the same website. **Whoever's platform the follow-up questions stay on gets the subsequent traffic.** This study covers only one publisher and measures only engagement. It cannot be extended to general search engines, nor used to support the claim that "AI search increases clicks overall".

### Principle 10.2: The remaining traffic is selective

Clicks do not fall evenly. Two factors determine how much a website is hurt:

- **Whether the content can be fully replaced by the answer.** Definitions, facts and simple calculations can be delivered by the answer itself, so their clicks disappear most easily.
- **What users click out for.** When they want to use a tool, check original data, read other people's first-hand experience or complete a transaction, users still have a reason to leave the answer page.

So the outbound traffic AI sends leans toward reference, academic, developer, tool, subscription and non-profit websites, and away from ad-supported websites. Experience-based and discussion content even benefits at the static summary stage (Google AI Overviews); but when the interface becomes conversational (AI Mode), this benefit decays sharply.

```
Static summary (AI Overviews): short answer → users still want to see "what real people say" → experience-based content benefits
Conversational (AI Mode)     : follow-ups can be completed inside the platform → even the reasons to click experience-based content are absorbed
```

### Principle 10.3: There is no reliable evidence on the return on investment of GEO

The whole "pie" of AI referral traffic is growing fast. A website's traffic from AI platforms may multiply several times simply because more people use AI search, not because of optimization.

```
Observed growth = overall platform growth + optimization effect + noise
```

Without a control group, the middle term cannot be separated out. The only study so far that has done this separation shows that after subtracting platform growth, the net effect of optimization is far smaller than the raw figure, and is only "suggestive" statistically.

The practical implication of this principle: **the value of "being cited" leans more and more toward brand exposure rather than clicks.** When measuring GEO, you must look at three things at once (exposure, site visits and revenue) and accept that part of it cannot be measured accurately.

## 3. How strong is the evidence

### 3.1 Click loss: several large-scale experiments with real users agree

This section is where the book's evidence is hardest. Several studies used different methods and different data sources, and point in the same direction.

| Finding | Study design | Evidence strength |
|---|---|---|
| Only 5.2% of ChatGPT conversations produce an outbound click; for Google queries it is 31.1%. 74.4% of active ChatGPT households never clicked an external link | US desktop clickstream, quasi-experiment | Large-scale experiments with real users |
| After access to ChatGPT Search was widened, traditional search queries fell by 9.4%; after 20 weeks, by 17.0% | Same as above, stacked difference-in-differences | Large-scale experiments with real users |
| Forcing the use of AI Mode reduced the outbound click-through rate by 18.8 percentage points (95% confidence interval −22.2 to −15.3) | Pre-registered randomized field experiment, real Google search | Large-scale experiments with real users |
| Turning off AI Overviews raised the click-through rate by 8.8 percentage points | Same as above (compliance rate only about 51%) | Large-scale experiments with real users |
| After AI Overviews went live by default, external search traffic to English Wikipedia fell by 5.45% relative to the German edition and by 4.82% relative to the French edition | About 500,000 article pairs, difference-in-differences, placebo test passed | Large-scale experiments with real users |
| About 18% of Google searches show AI Overviews; when they appear, the share of clicks on traditional results drops from 15% to 8%; only about 1% click a source cited in the AI Overview | Browsing logs from 900 US adults, 91,121 search page views | Observational data on real engines (not an experiment) |

Some details worth remembering:

- **Forcing AI Mode not only reduces clicks but also makes users less satisfied.** In the same randomized experiment, AI Mode reduced daily search sessions by 0.92, lowered trust by 0.34 (7-point scale), lowered satisfaction by 0.73 standard deviations, and raised the share of users switching to another search engine by 11.2 percentage points.
- **Wikipedia is a source heavily cited by AI Overviews, and its traffic still fell.** The researchers infer from this that being cited frequently is not enough to offset the loss of clicks. By the researchers' estimate, this amounts to about 100 million fewer search visits per month.
- AI Overviews make users end their browsing sooner. When an AI Overview appears, 26% of sessions end there; without one, 16%. These are observational data on Google; in the newspaper's on-site search randomized experiment mentioned in Principle 10.1, the share of sessions ending after a search was about 21% in both groups, with no difference. The two settings differ and cannot be compared directly.

Scope and limitations:
- The clickstream data come from US desktop users and exclude mobile.
- The treatment period of the randomized experiment was only 7 days, and the sample skews young and highly educated.
- The English-versus-Japanese comparison in the Wikipedia study (−16.53%) has a short window and can serve only as directional support.
- The browsing-log study is observational. It shows only correlation and cannot prove causation.

### 3.2 Selectivity of traffic: supported by real-user experiments, but moderated by content type

| Finding | Evidence strength |
|---|---|
| After ChatGPT Search use was widened, search referral traffic fell: academic −32.8%, reference −26.5%, developer −15.1%, news −13.4% | Large-scale experiments with real users |
| Among ChatGPT's outbound clicks, the share going to ad-supported websites is 27.6 percentage points lower than for Google | Large-scale experiments with real users (descriptive comparison) |
| Across 105,012 communities on a large community forum, after AI Overviews went live, daily comments rose by 12.0% and commenting users by 12.4% | Large-scale experiments with real users |
| The increase for experience-based communities was 2.3 times (comments) and 2.8 times (users) that of fact-based communities | Same as above |
| Small and medium-sized communities saw the largest relative increase | Same as above |
| After the move to AI Mode, the extra gain for experience-based communities decayed sharply: by about 59% on the user side, and almost entirely on the comment side | Same as above |

Note the directions of the first and second rows: reference and academic websites take a larger share of "the traffic AI sends out", but the traffic they get from traditional search is falling too. Both are true at once: AI's residual referral traffic leans toward them, but the total is still shrinking.

### 3.3 The return on investment of GEO: only weak evidence

| Study | Finding | Limitations |
|---|---|---|
| Log-based natural experiment on a single website | Monthly traffic from ChatGPT grew 5.7 times, but pages on the same site that received no optimization also grew 3.5 times over the same period. After subtraction, the level effect of optimization is about 1.82 times (95% confidence interval 1.31–2.54), with robustness checks between 1.8 and 2.3 times | Placebo time-permutation test p=0.16, so only suggestive evidence; only one website; the authors come from industry; several measures were implemented as a bundle and cannot be separated |
| Self-run A/B test by a large image platform | In a 4-week experiment, sessions were 1.18 times the control group (the group with the feature removed was at 0.82 times) | The authors are the platform; the metric "generative search traffic 9.2 times" is undefined; the 20% traffic increase claimed in the text does not match the +0.83% to +1.83% figures in its own tables |

The first study has two further results worth noting:
- A single-day peak of 38.2 times appeared, but raw multiples of this kind cannot be treated as a causal effect.
- **No "flywheel" effect of GEO lifting traditional search was found.** Over the same period, the site's Google organic clicks fell by about 25%, and this was not because it was removed from the index.

The measures implemented as a bundle in that study included: URL canonicalization, mining user needs from AI crawlers' 404 requests, switching to question-style titles, and adding a standalone summary to each page. This combination is consistent with the growth of about 1.8–2.3 times, but cannot show which measure had the effect.

Conclusion: no study so far proves that GEO reliably brings traffic or conversions. Of the two existing studies, one is not statistically significant enough, and the other was run by the platform itself with unclear metrics.

### 3.4 Practitioner data: consistent in direction, scattered in numbers

Practitioners' test data agree closely on "the volume is small" and differ widely on "how much higher the conversion rate is".

**Share of traffic (Practitioners report from their own tests, not independently verified):**

| Reporting context | Share from AI sources |
|---|---|
| Several client websites | Named AI sources are usually under 5% of total sessions, even when the site is heavily cited |
| Two B2B websites | 2%–4% of sessions |
| Several content websites | ChatGPT referral traffic is under 2% of organic traffic |
| One client website | ChatGPT brought 251 new users, 0.35% of total traffic |
| Several client accounts | A low single-digit percentage of the total |

**The gap between being cited and being clicked (Practitioners report from their own tests):**
- 6 informational pages cited by Google AI produced 9,600 impressions in 15 days and brought only 6 clicks.
- A streaming-platform lookup website became the number-one cited source in its niche within 12 weeks (65% of all page citations) and was cited more than 10,000 times in 30 days, but traffic from AI was under 1% of total sessions. The author's conclusion: citations behave like brand advertising, not like a customer acquisition channel.
- A website with fewer than 50 traditional search visitors a day was cited about 200 times a day by AI assistants, while ChatGPT brought only 3–5 sessions a day.

Practitioners widely believe (community consensus, an opinion and not a proof) that referral traffic from AI tools is still negligible compared with traditional search.

## 4. Debates and counterexamples

### 4.1 Is the conversion rate of AI traffic really high?

This is the question practitioners discuss most and disagree on most.

The side supporting "high conversion rate":

| Report | Evidence strength |
|---|---|
| ChatGPT brings only single-digit sessions a day, but the conversion rate is about 8 times that of organic traffic; "this is a closing channel, not a traffic channel" | Practitioners' repeated, controlled tests |
| On one client website, the engagement rate of ChatGPT referral traffic was 48.57%, higher than Google paid search (39.71%), Google organic search (34.71%), Bing organic search (33.92%) and direct traffic (20.73%) | Practitioners report from their own tests |
| Referral traffic from ChatGPT and Perplexity has a lower bounce rate and more pages viewed per session | Practitioners report from their own tests |
| The conversion rate of AI-sourced traffic is about 2 times the site-wide average, but because the base is small, this means little | Practitioners report from their own tests |
| For clients with a dedicated AI channel, 97% of 450 AI sessions came from ChatGPT, and conversion quality was better than ordinary organic traffic | Practitioners report from their own tests |

Other practitioners have observed multiples ranging from 3 times and 7 times to 16 times. These are all single observations and can serve only as leads.

**The side supporting "not that good" or "not necessarily":**

| Report | Evidence strength |
|---|---|
| A B2B SaaS company did 6 months of AEO (answer up front, FAQ and product structured markup, llms.txt, comparison pages). Citations rose, but AI-referred visitors bounced faster than organic search visitors and almost never converted | Practitioners report from their own tests |
| A test on 8,520 shopping queries showed AI traffic converting 86% worse than affiliate links; the cause was attributed to product data not meeting AI agents' requirements (missing GTIN, outdated inventory, missing returns-policy page, incomplete variant data) | Practitioners report from their own tests (not independently verified) |
| Most claims that "AI traffic converts well" overestimate its conversion contribution by 2–5 times, because attribution itself is inaccurate | Practitioners report from their own tests |
| An author originally claimed that high engagement on their website came from LLM citations, then corrected this after checking the sources: the traffic did not come from LLMs, and "the claim about LLM citations was premature" | Practitioners report from their own tests |

The reasoning on each side:
- The supporting side's logic is "pre-screening": users have already compared options and narrowed their choices in the AI conversation, so they arrive with clearer intent.
- The opposing side's logic is "it depends on the query": if citation growth comes from informational questions, users complete their task at the answer, so naturally they do not convert after arriving. Practitioners' repeated, controlled tests found that for "alternatives to X" prompts, comparison pages (/vs, /alternatives, /compare) account for 34%–43% of citations, for "best X" prompts only 2.8%, and informational prompts mostly cite documentation pages.
- Both sides are troubled by the same problem: the denominator is too small and attribution is incomplete.

The state of community consensus: "AI referral traffic converts better" is supported by 6 authors and opposed by none, yet it is labelled "disputed" because no high-evidence item supports it directly.

This book's position: no conclusion. "High conversion rate" appears in several practitioner reports, but all of them are self-selected samples with small bases and incomplete attribution. It may be a real phenomenon, or it may be selection bias caused by "only the few with the strongest intent click out". The two explanations cannot currently be told apart.

### 4.2 Does being cited do any good at all?

The studies seem to contradict each other on this point:

| Study | Conclusion |
|---|---|
| Wikipedia study | Frequently cited by AI Overviews, yet search traffic still fell by about 5% |
| Large community forum study | After AI Overviews went live, community engagement rose by about 12% |

The resolution: the content types differ. Wikipedia is fact-based content that the answer can replace completely. A forum is experience-based content: after the answer gives a summary, users still want to read "real people's experiences". This is the origin of Principle 10.2. But the same forum study also found that under AI Mode this benefit decays sharply, so "experience-based content is safe" is only a temporary, interface-dependent conclusion.

### 4.3 Research findings contradict what the platform says

The pre-registered randomized experiment found that AI Mode reduces daily search sessions. This runs in the opposite direction to Google's official claim that "AI increases query volume and high-quality clicks". The difference between the two: the experiment used forced assignment and third-party measurement; the platform's data have no published methodology. On methodological transparency, the experimental evidence is more credible.

### 4.4 Can blocking AI crawlers protect traffic?

The appendix of the large-scale clickstream study shows that 79% of domains blocked at least one AI crawler, and the average referral traffic blockers received from ChatGPT (6.48) was actually higher than for non-blockers (4.48). The researchers' interpretation: blocking AI **training** crawlers does not stop ChatGPT from sending traffic **when it answers**. But this is correlation, not causation: large websites may both tend to block and already have high traffic.

### 4.5 Is AI traffic growing or shrinking?

- Community views on "ChatGPT brings websites significant traffic" are split evenly, with 5 authors on each side.
- Practitioners report from their own tests that ChatGPT referral traffic to a travel website fell by about 50% within 11 days (5–16 July), but the remaining traffic converted better.
- Practitioners report from their own tests that a website's human visits from ChatGPT peaked at 1–3 a day from 7 to 15 May and dropped to zero from 16 May; but over the same period ChatGPT's crawl volume (ChatGPT-User plus GPTBot) stayed at about 30–50 a day without falling. The reporter's interpretation: the content was still being read, just no longer presented in clickable form, so "being indexed is not the same as being shown".

This shows that AI referral traffic is not only small but also **unstable**: when the platform changes which questions trigger citation cards, a website's referral traffic can drop to zero overnight, regardless of what the website itself did.

## 5. Cases

The following cases are all first-hand reports from practitioners and are not independently verified. They illustrate how the principles play out on real websites; they are not proofs.

### Case 1: A French affiliate review website, before and after AI Overviews went live

- Website type: independent affiliate marketing website publishing product reviews.
- Platform: Google search, with AI Overviews launched in France (22 July).
- Method: compare two matched weeks before and after the launch.
- Observations:
  - Google search clicks fell by 25%, with impressions almost unchanged (+0.1%).
  - For one query ranked first, the click-through rate fell from 54.5% to 16.7% within a week.
  - Revenue fell by nearly 47%, about twice the drop in traffic; the number of sales also fell, showing that not only were there fewer visits, but conversion also got worse.
- Related principle: 10.1. Rankings unchanged, impressions unchanged, clicks absorbed by the answer. Informational review queries are the easiest to replace.

### Case 2: A small law-practice website, the same page compared over two years

- Method: compare the performance of the same informational page, at the same ranking position, two years apart.
- Observations: two years ago, about 4,000–5,000 impressions brought about 800 clicks a month; now 1,200 impressions bring only 90 clicks. What still supports the business is brand search and referrals from existing clients, not informational queries.
- Evidence strength: One practitioner observed (a single first-hand observation); usable only as an example.
- Related principles: 10.1 and 10.2. Informational traffic is lost; traffic with brand and transactional intent remains.

### Case 3: A streaming-platform lookup website, first in citations, near zero in traffic

- Website type: a new site, live for 12 weeks, specializing in lookups of film and TV streaming availability in Asian markets.
- Strategy: optimize for AI answers from day one, instead of competing for traditional rankings.
- Observations:
  - Became the number-one cited source in the query set of its niche, with 65% of all page citations, ahead of large aggregator websites.
  - Cited by Copilot more than 10,000 times in 30 days.
  - The direct referral traffic from these citations was under 1% of total sessions.
- What the author says worked best: country-specific long-tail pages; content in comparison format; question-style headings paired with 2–3-sentence short answers; time-sensitive data with dates marked.
- Related principle: 10.3. GEO can succeed very well at the "being cited" step, but citations do not automatically turn into clicks. This website's answer happened to be a short fact ("where to watch X in a given country"), which the answer itself can deliver.

### Case 4: B2B SaaS, citations rising, conversions at zero

- Website type: a small B2B SaaS (project management tool).
- Method (6 months): rewrote core documentation and comparison pages with question-style subheadings, answering directly in the first 2–3 sentences; added FAQ and product structured markup site-wide; published llms.txt; created several new "vs." and "alternatives" comparison pages; manually tracked brand mentions in ChatGPT, Perplexity and Gemini.
- Observations: citations rose, but visitors referred by AI bounced faster than organic search visitors and almost never converted.
- **One explanation (Practitioners' repeated, controlled tests):** first split citations by prompt type. If citation growth comes from informational prompts, users are already satisfied at the answer, and this is not a conversion problem a page can fix; only citations from "buyer-type" prompts have a chance to convert.
- Related principles: 10.2 and 10.3. The volume of "being cited" is not the same as "being cited for the right questions".

### Case 5: Crawl volume stable, clicks at zero

- Observation (Practitioners report from their own tests): a website's human visits from ChatGPT dropped to zero after mid-May, while ChatGPT's crawl volume stayed steady; the URL format of the referral source did not change either.
- Inference: the website did nothing wrong. Rather, the platform changed which queries trigger citation cards, or the topics that brought traffic moved out of the active answer set.
- Related principles: 10.1 and 4.5. Fluctuations in AI referral traffic may come entirely from the platform side.

### Case 6: Local businesses, conversions without clicks

- **Observation (One practitioner observed, a single first-hand observation):** when AI assistants answer questions like "the best dentist near me", they often give the business name, address and phone number directly. The user calls directly: no click, no referral source, no record of any kind in analytics tools.
- Implication: measuring GEO by website traffic alone leads to the conclusion that "it has no effect at all", while in fact it may be bringing in calls that cannot be attributed.
- Related principle: 10.3. The value of GEO may lie where website analytics tools cannot see.

## 6. What to do

### 6.1 Measurement: first solve the "cannot measure accurately" problem

Attribution of AI traffic has three structural gaps:

```
Exposure in an AI answer
   │
   ├─ User does not click, simply remembers the brand → later searches the brand name / types the URL → recorded as "direct" or "brand search"
   ├─ User clicks, but the platform does not pass referrer information (or opens it in an in-app browser) → recorded as "direct"
   ├─ User clicks, referrer information is preserved → recorded as AI referral (the only confirmable part)
   └─ User calls directly / visits the store → never enters website data at all
```

Practitioners widely believe (community consensus) that analytics tools, lacking referrer information, wrongly assign a large amount of AI referral traffic to other channels.

| Action | Explanation | Evidence strength |
|---|---|---|
| **Use a control group to assess the effect of optimization** | Keep a set of unoptimized pages on the same website as a control and compare the difference in growth. Without a control, platform growth will be mistaken for an optimization effect | Large-scale experiments with real users (raw growth 5.7 times, control group also grew 3.5 times) |
| **Report "confirmed" and "inferred" AI traffic separately** | Confirmed: there is AI referrer information, or server logs show agents fetching on a user's behalf (such as ChatGPT-User, Perplexity-User, Claude-User). Inferred: visits within direct traffic that land directly on deep documentation or comparison pages. The honest number is the confirmed one; the inferred part is used to estimate how large the gap is (about 2–3 times the confirmed volume in one report) | Practitioners' repeated, controlled tests |
| **Split direct traffic by landing page** | AI visitors often land directly on deep documentation or comparison pages, whereas direct visitors who type the URL by hand almost never do | Practitioners' repeated, controlled tests |
| **Ask "how did you hear about us" directly in forms or the first call** | Use an open text field, not a drop-down menu. One report shows a completion rate of about 40%–50%; another shows that 15% of leads said they found the business through AI, while source-tracking parameters showed only 3%. Asking verbally is more precise than a form, but customers mostly cannot recall the exact wording they used when asking AI | Practitioners report from their own tests; community consensus (12 authors in support, 0 against) |
| **Cross-check self-reported sources against a fixed prompt panel** | Each month, test with the same set of purchase-intent prompts, recording whether you appear and which page is cited; then compare with changes in self-reported sources | One practitioner observed (a lead) |
| **Set up a dedicated phone number for local businesses** | A phone number used only on the business profile page and in directories that AI reads, plus a question about the source | One practitioner observed (a lead) |
| **Track changes in brand search volume** | As a leading indicator of "exposure without clicks" | Practitioners widely believe (disputed in the community: 6 in support, 0 against, but no high-evidence item; one report says brand search rose slightly, but too slightly to draw a conclusion) |
| **Look for the signature of AI Overviews in Search Console** | Impressions rising, click-through rate falling, average position roughly unchanged. Clicks from AI Overviews cannot be distinguished from ordinary organic search clicks in analytics tools | Practitioners report from their own tests |

### 6.2 Strategy: accept "citation ≠ click" and redefine the goal

| Action | Explanation | Evidence strength |
|---|---|---|
| **Shift the goal of GEO from "getting clicks" to "being named" plus "catching high-intent visitors"** | The value of being cited leans more and more toward brand exposure. AI conversations compress the discovery and comparison stages but do not shorten the subsequent sales cycle | Large-scale experiments with real users (click loss); One practitioner observed (sales cycle) |
| **Prioritize citations for "buyer-type" questions** | Prompts such as "alternatives to X" and "A vs. B" are more likely to cite comparison pages; visitors from informational prompts stop at the answer | Practitioners' repeated, controlled tests |
| **Make landing pages build on the trust AI has already established** | Visitors referred by AI are often already midway through a decision. Landing pages should offer proof, case studies, clear pricing signals and one clear path to action | One practitioner observed (a lead) |
| **Assess how much the business model depends on clicks** | Websites that rely on advertising or affiliate commissions and are mainly informational content are hit hardest; reference, tool, developer and subscription websites retain clicks better | Large-scale experiments with real users |
| **Value content that answers cannot replace** | Original viewpoints, first-hand experience, tools, and tasks that can only be completed on the site. One practitioner observed that articles making a distinctive argument hold engagement time far longer than generic explainers | Large-scale experiments with real users (experience-based content benefits); Practitioners report from their own tests |
| **Do not treat the benefit to experience-based content as a long-term guarantee** | Experience-based content benefits at the AI Overviews stage, but the gain decays sharply once AI Mode arrives | Large-scale experiments with real users |
| **E-commerce sites should check whether product data are complete** | Missing GTIN, outdated inventory, missing policy pages and incomplete variant data may cause AI agents to skip a product outright | Practitioners report from their own tests (not independently verified); community consensus (15 in support, 1 against; an opinion) |

### 6.3 Do not do

- **Do not use raw growth multiples to prove that GEO works.** "AI traffic grew 5 times" may be mostly platform growth. A single-day spike is even less acceptable as an effect.
- **Do not use the "citation share score" of AI visibility tools as a performance metric.** Practitioners report from their own tests that such scores are sampled with synthetic prompts and then extrapolated to a population of real queries that no one can observe, so their precision has no basis. They can serve as a rough directional reference, not as a KPI.
- Do not equate "number of citations" directly with commercial value. The example of being cited 10,000 times and bringing under 1% of traffic shows that the two can be completely decoupled.
- Do not assume GEO will lift traditional search. The only quasi-experimental study found no such flywheel effect.
- Do not assume that blocking AI training crawlers will preserve or increase AI referral traffic. There are only correlational data on the two so far, and the direction runs against intuition.
- Do not claim conversion-rate multiples when the denominator is too small. With single-digit sessions a day, one or two sales can make the conversion rate swing widely.

### 6.4 Already outdated

- **Using total website traffic as the only success metric for SEO/GEO.** In an environment where clicks are absorbed by answers, rising impressions with falling clicks is normal, and looking at traffic alone leads to misjudgment.
- **Counting AI traffic only from referrer information.** Most AI influence carries no referrer information, so such counts systematically underestimate and can only serve as a lower bound.
- Treating the AI channel newly added to analytics tools as the complete answer. One practitioner observed that in 2026 mainstream analytics tools added a dedicated channel for AI assistants, but it captures only visits that carry referrer information; some platforms still fall under ordinary referral traffic, clicks from AI Overviews are still counted as organic search, and historical data are not backfilled. Different observers report inconsistent launch dates and platform coverage.

## 7. Key points

1. **AI search keeps most demand inside the platform.** Only 5.2% of ChatGPT conversations produce an outbound click, against 31.1% of Google queries; in a randomized experiment, forcing AI Mode reduced the outbound click-through rate by 18.8 percentage points. This is the conclusion with the strongest evidence in the book.
2. **Being cited is not the same as being clicked.** The click-through rate on sources cited in AI Overviews is only about 1%; Wikipedia, heavily cited, still saw its search traffic fall by about 5%.
3. The remaining traffic is selective. It leans toward reference, academic, developer, tool and subscription websites and away from ad-supported websites; experience-based content benefits at the AI Overviews stage, but the gain decays sharply under AI Mode.
4. There is no reliable evidence on the return on investment of GEO. In the only quasi-experimental study, raw growth of 5.7 times shrank to about 1.8 times after subtracting platform growth, and is only suggestive statistically.
5. Assessing AI traffic requires a control group. Otherwise the platform's own growth will be mistaken for an optimization effect.
6. That AI traffic is "small in volume, possibly higher in conversion" is a common practitioner report, but it is unproven. Small denominators, self-selected samples and attribution gaps can all create the illusion of "high conversion"; there are also reports of AI visitors almost never converting.
7. Report attribution in layers. Separate confirmed, inferred and self-reported AI sources, and accept that part of the value (brand memory, phone calls) can never be measured.
8. The value of GEO leans more and more toward brand exposure. The goal should shift from "getting clicks" to "being named in buyer-type questions", with landing pages that catch visitors already pre-screened by AI.
