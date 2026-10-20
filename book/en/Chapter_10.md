# Chapter 10 — AI Named You. Now What?

> The last of the seven gates: **will people come over** (user behavior).
>
> The earlier chapters were all about "how to get into AI's answers". This chapter asks a more practical question: once you are in, will readers click through to your website? Will they buy?
>
> The conclusion first: this is the chapter with the strongest evidence in the whole book. And the strongest evidence does not bring good news.

---

## Imagine: a Monday morning

Imagine that An runs a small software company that sells a project management tool for businesses.

Over the past six months, An followed all kinds of GEO advice and reworked the website. Subheadings became questions, the first two or three sentences of each section gave the answer directly, FAQs were added, and there were several pages of "us versus such-and-such product" comparisons.

The results looked good. When An asked AI, the company name often showed up in the answers. The number of mentions grew month after month.

But this Monday, An opened the website dashboard and froze.

AI brought very few visitors. The ones who came left faster than people from ordinary search, and almost no one placed an order.

An's first thought was: "Did I do something wrong?"

What this chapter wants to say is: most likely An did nothing wrong. This is simply how AI search works.

---

## The five questions this chapter answers

1. After AI search arrived, do websites get more clicks or fewer? How many fewer?
2. Which websites does the remaining traffic flow to? Which kinds of content get hurt, and which actually benefit?
3. After doing GEO, how much of the traffic growth comes from optimization, and how much is just the AI platform itself growing?
4. If "being cited by AI" brings no clicks, what is its commercial value?
5. With incomplete tracking tools, how do you measure the business effect of GEO without fooling yourself?

---

## 1. The librarian read the books for you

Remember the metaphor used throughout the book? AI is like a very busy librarian.

A traditional search engine is more like the library's card catalogue. You ask a question, it hands you a stack of cards and tells you: "The answer is in these books. Go look for yourself." You have to walk to the shelf and take the book down. Websites get their clicks from this act of "walking over". Websites trade content for clicks. This is the business model of traditional search: **sending traffic**.

The AI librarian is different. It reads several books, organizes them, and tells you the answer directly. This is the business model of generative engines: **answering**.

Once the question is solved, the reader rarely has a reason to walk to the shelf and flip through that book.

The big idea of this chapter can be written as a chain of cause and effect:

```
The more complete the answer → the less the reader needs to click → the fewer clicks the source website gets
          → being cited ≠ being clicked
```

Please note: this is not because your ranking dropped. You may still be in the same position, and your content may even be written into the answer, yet the clicks still drain away.

So many websites see a strange pattern: **the number of times they are seen (impressions) stays flat or even rises, but the share of people who click through (click-through rate) falls.**

There is, however, a precondition to this chain of cause and effect: **the answer is provided by someone else's platform.**

If the answer is provided by the website itself, things are different. A major US newspaper ran a large-scale randomized experiment in the search function on its own website, with about 38,000 readers taking part over 38 days. Half of the readers saw an extra AI answer above the search results, with the newspaper's own articles attached as sources. The results:

- After each search, the share of people clicking ordinary search results fell by 20.8 percentage points; the articles opened per search fell by about 19%.
- But readers searched about 29% more often, so counted per reader, the articles opened actually rose by about 5%.
- The share of people who left right after searching did not differ between the two groups.

The reason: readers' follow-up questions stayed on the same website. In other words, **whoever's platform the follow-up questions stay on gets the traffic that follows.**

Note: this is only one newspaper, and it only looks at how engaged readers were. It cannot be extended to general search such as Google, nor can it be used to prove that "AI search increases clicks overall".

---

## 2. How strong is the evidence? This time, really strong

In many earlier chapters, we could often only say "seen under lab conditions" or "someone in the industry tested this themselves".

This chapter is different. Several large-scale experiments with real users, using different methods and different data sources, reached conclusions pointing the same way. This is where the evidence in the whole book is hardest.

### The first set of numbers: 5.2% versus 31.1%

Researchers tracked the real browsing records of a large number of US households on desktop computers (this is called "clickstream" data).

- In ChatGPT conversations, only **5.2%** of conversations led to a click on an external website.
- With Google search, this share was **31.1%**.
- Among households that use ChatGPT often, **74.4%** had never clicked any external link. That is roughly three quarters.

The same data also showed: after more people could use ChatGPT's search feature (ChatGPT Search), traditional search queries fell by **9.4%**; after 20 weeks, the drop reached **17.0%**.

These conclusions are backed by large-scale real-user data, and the research method is close to an experiment.

> **A closer look: what are a "quasi-experiment" and "difference-in-differences"?**
> A true experiment randomly splits people into groups. But often that is not possible, so researchers use changes that happen naturally in the real world (for example, some people get a new feature first and others later), and compare two layers of difference: "before versus after the change" and "the group with the change versus the group without it". This is called "difference-in-differences". This kind of study is not as clean as a randomized experiment, but it is far more reliable than simple observation. The 9.4% and 17.0% above used an advanced version of it (stacked difference-in-differences), which means stacking together several batches of people who got the feature at different times and comparing them.

### The second set of numbers: 18.8 percentage points fewer

There was a randomized experiment with a **publicly pre-registered research plan**, run on real Google search. Researchers randomly split users into groups, and one group was forced to use Google's conversational AI search (AI Mode).

- In this group, the share of clicks to external websites fell by **18.8 percentage points**.
- The researchers estimated that the true drop most likely lies between 15.3 and 22.2 percentage points (this is called the "95% confidence interval", meaning that if the study were repeated many times, the true value would fall within this range in 95% of cases).

And it was not only fewer clicks. The same experiment found that users forced to use AI Mode:

- made **0.92** fewer searches (search "sessions") per day;
- had trust drop by **0.34** (scored on a 1-to-7 scale);
- had satisfaction drop by **0.73 standard deviations** (a standard deviation is a unit measuring "how much people's scores usually differ");
- switched to other search engines at a rate **11.2 percentage points** higher.

The same experiment also ran the opposite test: one group was asked to **turn off** AI Overviews (the AI Overviews at the top of Google search results). This group's click-through rate rose by **8.8 percentage points**. However, only about **51%** of the people assigned to this group actually did it (this is called the "compliance rate").

> **A closer look: why does "publicly pre-registered" matter?**
> Before seeing the results, the researchers publicly write down what they will measure and how they will analyze it. That way, they cannot afterwards pick the numbers that suit them to report. This is currently one of the most widely accepted trustworthy research practices.

### The third set of numbers: about 1%

Another study recorded the real browsing of **900** US adults, covering **91,121** views of search results pages.

- About **18%** of Google searches showed AI Overviews.
- When AI Overviews appeared, the share of clicks on traditional search results fell from **15%** to **8%**.
- Only about **1%** of people clicked a source cited inside AI Overviews.
- When AI Overviews appeared, **26%** of browsing ended on that page; without AI Overviews, it was **16%**. In other words, AI Overviews make people end their browsing sooner.

This study is observational data from a real search engine, not an experiment. It can only show that "two things happen together"; it cannot prove "which causes which".

Also, in the newspaper experiment mentioned earlier, the share of people who left right after searching was about 21% in both groups, with no difference. But the two settings differ: one is Google, the other is the search on the newspaper's own website, so they cannot be compared directly.

### The fourth set of numbers: Wikipedia lost about 5%

Wikipedia is one of the sources AI Overviews cite most often. In theory, being cited so much should bring benefits.

Researchers compared about **500,000 pairs** of articles to see what changed after AI Overviews went live by default:

- Traffic to English Wikipedia from external search fell by **5.45%** relative to the German version, and by **4.82%** relative to the French version.
- The researchers also ran a "placebo test" and it passed. That means: they deliberately redid the analysis at times or on subjects where there should be no effect, confirmed that no false effect appeared there, and showed the result was not a fluke.
- By the researchers' estimate, this amounts to **about 100 million fewer visits per month** from search.

From this, the researchers inferred: **being cited often does not make up for the clicks absorbed by the answer.**

These studies also have limits, and we should be honest about them:

- The clickstream data comes only from desktop computers in the US and does not include phones.
- The randomized experiment ran for only **7 days**, and participants skewed young and highly educated.
- The Wikipedia study also had a comparison of the English version against the Japanese version, showing a drop of **16.53%**, but the observation period was too short, so it can only serve as side evidence that "points the same way".
- The study of the 900 people's browsing records is observational; it can only show correlation, not prove causation.

But the overall direction is consistent. **AI search keeps most demand inside the platform**, and this is the conclusion this book is most confident about.

### What have people in the industry seen?

Beyond academic research, people in the industry have also measured data from many websites themselves. These were all measured by them; no one has independently verified them. But on the point that "AI brings very little traffic", their accounts are highly consistent:

| Report context | AI sources as a share of all traffic |
|---|---|
| Multiple client websites | Clearly identifiable AI sources are usually under 5% of total visits, even when the site is cited heavily |
| Two websites selling to business customers | 2% to 4% of visits |
| Multiple content websites | Traffic from ChatGPT is under 2% of organic search traffic |
| One client website | ChatGPT brought 251 new users, 0.35% of total traffic |
| Multiple client accounts | A low single-digit percentage of the total |

The gap between "being cited" and "being clicked" is even more startling:

- 6 informational pages were cited by Google's AI over 15 days, generating **9,600 impressions** but only **6 clicks**.
- A website dedicated to answering "which streaming platform can I watch this film or show on" became the **most-cited source** in its small niche within 12 weeks of launch (**65%** of all page citations), and was cited **more than 10,000 times** in 30 days, but traffic from AI was **under 1% of total visits**. The author's conclusion: citations behave like brand advertising, not a channel that brings in new customers.
- A website with **fewer than 50** traditional search visitors a day was cited by AI assistants about **200 times** a day, but ChatGPT brought only **3 to 5** visits a day.

Many in the industry believe this: referral traffic from AI tools is still negligible compared with traditional search. This is an opinion, not proof; but "many people believe" points the same way as the research above.

---

## 3. Who are the visitors that remain?

Clicks do not fall evenly. Two questions decide how badly a website gets hurt.

**First, can your content be fully replaced by a paragraph of answer?**
Definitions, facts, simple calculations: the answer itself can deliver these. Clicks on this kind of content are the easiest to disappear.

**Second, what does the reader click out for?**
If the reader wants to use a tool, check original data, see other people's firsthand experience, or complete a transaction, they still have a reason to leave the answer page.

So the little traffic AI sends out leans towards **reference, academic, developer, tool, subscription and non-profit** websites, and away from websites that **make money from advertising**.

Large-scale real-user data supports this:

- After more people used ChatGPT's search feature, search traffic fell for every category of website: academic **−32.8%**, reference **−26.5%**, developer **−15.1%**, news **−13.4%**.
- Among clicks sent out by ChatGPT, the share going to ad-revenue websites was **27.6 percentage points** lower than Google's. (This is a descriptive comparison showing "what the distribution looks like", not a causal inference.)

There is an easy point of confusion here, so please pay special attention:

Reference and academic websites take a higher **share** of "the traffic AI sends out". But the **total traffic** they get from traditional search is falling too. Both things are true at once: **the share they get is bigger, but the total to be shared is shrinking.**

### "What real people say" used to be a shelter

One very large study looked at **105,012** discussion boards in a large online community forum. This too is large-scale real-user data.

After AI Overviews launched, these boards actually became busier:

- daily comments rose by **12.0%**;
- the number of users commenting rose by **12.4%**;
- boards for sharing **experience** grew **2.3 times** (comments) and **2.8 times** (users) as much as boards answering **facts**;
- **small and medium** boards had the largest relative growth.

The reason is not hard to understand: AI Overviews are short, and after reading them, people still want to know "what do people who actually used it say".

**But this benefit did not last.** The same study found that when the interface became the conversational AI Mode, where you can keep asking follow-up questions, the extra benefit for experience-based boards shrank sharply: the gain in users decayed by about **59%**, and the gain in comments **almost entirely disappeared**.

The reason: readers can keep asking in the conversation, "So what is it like in actual use?" Even the reason to click out, "wanting to see real people's experience", was absorbed by the platform.

```
Static AI Overviews: short answer → reader still wants "what real people say" → experience-based content benefits
Conversational AI Mode: follow-ups can be done inside the platform → even the reason to click experience-based content is absorbed
```

### Does being cited help or not? Two studies that seem to contradict each other

| Study | Conclusion |
|---|---|
| Wikipedia study | Cited often by AI Overviews, search traffic still fell about 5% |
| Large community forum study | After AI Overviews launched, community engagement rose about 12% |

One says traffic fell after being cited; the other says it rose. How do we explain this?

The answer is **different content types**. Wikipedia is fact-based content, and the answer can fully replace it. A forum is experience-based content; after the answer gives a summary, readers still want to see real people's experiences. This is exactly where the "two questions" in this section come from.

But don't forget: the same forum study also found that under AI Mode, this benefit shrank sharply. So **"experience-based content is safer" is only a temporary conclusion, and it depends on what the interface looks like.**

---

## 4. Can GEO actually bring in business? Honestly: the evidence is not there

This is the question many people most want answered. This book's answer is: **there is currently no reliable evidence.**

### An easy trap to fall into

The whole market of "traffic from AI" is growing fast. Your website's traffic from AI platforms multiplying several times over may simply be because "more people use AI search", not because you optimized.

As a formula:

```
The growth you see = the platform's overall growth + the effect of your optimization + random fluctuation
```

If you don't keep a set of "untouched pages" for comparison, you simply cannot separate out the middle term.

### The only study that seriously separated them

So far, only one study has done this separation. It was a "natural experiment" a website ran based on its own server logs: some pages were optimized, the others were left alone.

- For the optimized pages, monthly traffic from ChatGPT grew to **5.7 times**. That sounds amazing.
- But **pages that were not touched at all also grew to 3.5 times in the same period.**
- After subtracting that, the effect the optimization really brought was about **1.82 times**. The researchers estimated that the true value most likely lies between **1.31 and 2.54 times**; recalculated with several different analysis methods, the result was between **1.8 and 2.3 times**.

This roughly 1.8-times effect comes with many caveats:

- The researchers ran a check: pretend the "date optimization started" was moved to a different time, and see whether an effect also appears. This check was not convincing enough (statistically p=0.16, while the usual requirement is below 0.05). So this result only counts as "some signs", and cannot be called solid.
- Only **one website**.
- The author comes from industry.
- Several practices **went live at the same time**, so it is impossible to tell which one worked.

The things this website did at the same time were:

1. tidying up URLs (keeping only one standard URL for the same content);
2. using URLs that AI crawlers requested but that did not exist on the site (requests that got "page not found" errors) to work out what readers really wanted;
3. changing titles into questions;
4. adding a summary to each page that can be read on its own.

This combination matches growth of about 1.8 to 2.3 times, but it cannot say which item was doing the work.

The study had two more results worth noting:

- On a single day, there was a spike of **38.2 times**. But this kind of raw multiple **cannot** be taken as the effect of optimization.
- **GEO was not seen to lift traditional search along with it.** In the same period, the site's organic clicks from Google actually fell by about **25%**, and not because Google removed the pages from its index. The so-called virtuous circle of "do GEO well and traditional search will improve too" (often called the "flywheel effect") did not appear here.

### Another study: nice numbers, but many problems

A large image platform ran its own A/B test (splitting users into two groups, one using the new approach and one kept as it was, and comparing the results):

- In a 4-week experiment, the group using the new feature had **1.18 times** the visits of the control group; the group where the feature was **removed** had **0.82 times**.

But the problems are:

- the authors are the platform itself;
- the paper mentions "generative search traffic grew 9.2 times", but does not explain how this metric is defined;
- the paper claims a **20%** traffic increase, but the figures in its own tables are only **+0.83% to +1.83%**, and the two do not match.

### So the conclusion is

**No study so far has proven that GEO reliably brings traffic or sales.** Of the two existing studies, one is not statistically convincing enough, and the other was done by the platform itself, with unclear metrics.

The practical meaning behind this is: **the value of "being cited" is leaning more and more towards brand exposure, not clicks.** When measuring GEO, you must look at three things together: **impressions, visits, revenue**. And you must accept that part of it cannot be measured accurately.

---

## 5. Are visitors from AI more likely to buy?

This is the question the industry discusses most, and disagrees on most. Everything below is from industry people's own reports; no one has independently verified them.

### The "yes" side

- Someone in the industry tested this repeatedly themselves, with comparisons: ChatGPT brought only single-digit visits a day, but the conversion rate was about **8 times** that of organic search traffic. In his words: "This is a channel for sales, not a channel for traffic."
- On one client website, the "engagement rate" (the share of visits that actually did something on the page) of visitors referred by ChatGPT was **48.57%**, higher than Google paid search (39.71%), Google organic search (34.71%), Bing organic search (33.92%) and visitors who typed the URL directly (20.73%).
- Visitors referred by ChatGPT and Perplexity had a lower rate of leaving after one page (bounce rate) and viewed more pages per visit.
- The conversion rate of visitors from AI sources was about **2 times** the site-wide average; but because the base number of people is very small, this means little.
- For one client with a "dedicated AI source category", **97%** of 450 AI visits came from ChatGPT, and the sales quality was better than ordinary organic search traffic.
- Other people in the industry have also reported various multiples such as **3 times, 7 times, 16 times**, but each is only a single observation and can only serve as a lead.

Their reasoning is "**they have already been filtered**": in the AI conversation, readers have already compared and narrowed down their options, so when they click through, they already have a clear goal in mind.

### The "not so good" or "not necessarily" side

- An online software service company selling to businesses spent 6 months on a full set of optimizations for AI answers (answer first, structured data for FAQs and products, publishing an llms.txt file [a site description file written specifically for AI], comparison pages). Citations went up, but visitors referred by AI **bounced faster than those from organic search, and almost never converted**.
- Someone in the industry tested **8,520** shopping queries and found that traffic from AI converted **86%** worse than affiliate links (links that "recommend products and earn a commission"). He put this down to product data not meeting the requirements of AI agents (AI programs that compare prices and place orders for people automatically): missing Global Trade Item Numbers (GTIN), outdated stock information, no returns and exchange policy page, and incomplete data for different variants (for example size, colour). This one has not been independently verified either.
- Some in the industry believe most claims that "AI traffic converts well" overstate AI's contribution to sales by **2 to 5 times**, because source tracking itself is inaccurate.
- One author originally claimed that high engagement on his site came from AI citations; later, when he checked the sources, he found this traffic had not come from AI at all. He corrected himself: it is still too early to say it was brought by AI citations.

Their reasoning is "**it depends on the question**": if the growth in citations comes from informational questions, the reader has already finished the task at the answer, so naturally they won't buy when they click through.

Someone in the industry tested this repeatedly, with comparisons, and found:

- in questions like "what are the alternatives to X", comparison pages (pages whose URLs often contain /vs, /alternatives, /compare) made up **34% to 43%** of citations;
- in questions like "what is the best X", comparison pages made up only **2.8%**;
- informational questions mostly cited documentation pages.

### Both sides are stuck on the same problem

**Too few people, and sources that cannot be fully tracked.** With single-digit visitors a day, one or two extra sales can flip the ratio dramatically.

The industry view is this: the claim that "traffic referred by AI converts better" is supported by 6 authors, with no one publicly opposing it. But it is still marked "disputed", because there is no high-quality evidence directly supporting it. "Many people believe" does not equal "it is true".

### This book's position: no conclusion

"Converts better" appears in several industry reports, but all of them use self-selected samples, very small numbers of people, and incomplete source tracking.

It may be true; or it may just be an illusion created by "only the few people who most want to buy click through" (this is called "selection bias"). These two explanations cannot be told apart at present.

---

## 6. AI traffic can also vanish overnight

Traffic from AI is not only small, but also **unstable**.

### Is it growing or shrinking?

- On the question of whether "ChatGPT brings significant traffic to websites", industry opinion is completely split, with 5 authors on each side.
- Someone in the industry reported: a travel website's referral traffic from ChatGPT fell by about **50%** within **11 days** (5 July to 16 July); however, the remaining traffic converted better.
- Someone in the industry reported: a website's human visits from ChatGPT peaked at **1 to 3** a day from 7 May to 15 May, and **dropped to zero from 16 May**. But over the same period, the number of times ChatGPT's crawlers read the site (including ChatGPT-User, which reads in real time on the user's behalf, and GPTBot, which collects data) stayed at about **30 to 50** a day, with no drop at all. The format of the source URLs did not change either.

The reporter's interpretation: the content is still being read, it just no longer appears in answers as a "clickable link". **Being read does not equal being shown.**

He inferred that it was not that the website did something wrong, but that the platform changed "which questions get citation cards attached", or that the topics that used to bring traffic were no longer within the range AI answers on its own initiative.

This shows: the platform only has to adjust its rules a little, and a website's AI traffic can drop to zero overnight, with nothing to do with what the website itself did.

### Can blocking AI crawlers protect your traffic?

The appendix of a large-scale clickstream study looked at this in passing:

- about **79%** of websites blocked at least one AI crawler;
- websites that blocked had a **higher** average referral from ChatGPT (6.48) than those that did not block (4.48).

The researchers' interpretation: blocking crawlers that "collect data to **train** AI" does not stop ChatGPT from sending people over "**when answering questions**".

But this is only two things appearing together (correlation), not causation. It may also be that large websites already have large traffic and also happen to be more likely to block.

### The research conclusions contradict the platform's claims

That publicly pre-registered randomized experiment found that AI Mode reduced the number of searches per day. This points in the opposite direction from Google's official claim that "AI increases queries and brings higher-quality clicks".

The difference between the two: the experiment used forced group assignment and third-party measurement; the platform's data did not publish its methods. On methodological transparency, the experiment's evidence is more trustworthy.

---

## 7. Stories from a few real websites

The following are all firsthand reports from industry people themselves; no one has independently verified them. They are used to illustrate what the principles look like on real websites, not as proof.

### Story one: ranking unchanged, revenue down by nearly half

- **Website:** an independent French product review website that keeps running on commissions from recommending products.
- **Event:** Google's AI Overviews launched in France (22 July).
- **Approach:** compare two comparable weeks before and after the launch.
- **Results seen:**
  - Google search clicks fell **25%**, while impressions were almost unchanged (**+0.1%**).
  - For a query ranked first, the click-through rate dropped from **54.5%** to **16.7%** within a week.
  - Revenue fell by nearly **47%**, about twice the drop in traffic. The number of items sold also fell, showing that not only did fewer people come, but those who came were also less likely to buy.
- **What this shows:** the ranking did not change, impressions did not change, and the clicks were absorbed by the answer. Informational queries in the review category are the easiest to replace with an answer.

### Story two: the same page, two years later

- **Website:** the website of a small law firm.
- **Approach:** compare the same informational page, in the same ranking position, over two years.
- **Results seen:** two years ago, about 4,000 to 5,000 impressions brought about **800** clicks a month. Now, 1,200 impressions bring only **90** clicks. What still supports the business is people who search the firm's name directly and people referred by past clients, not informational queries.
- **Strength of evidence:** this is a single firsthand observation and can only serve as an example.
- **What this shows:** informational traffic drained away; traffic from people who know your name and actually need something done stayed.

### Story three: first in citations, traffic close to zero

- **Website:** a new website, 12 weeks old, dedicated to answering "which streaming platform can I watch a given film or show on" for Asian markets.
- **Strategy:** from day one, optimize for AI answers rather than compete for traditional search rankings.
- **Results seen:**
  - In a set of queries in its small niche, it became the most-cited source, with **65%** of all page citations, ahead of large aggregator websites.
  - It was cited by Copilot **more than 10,000 times** in 30 days.
  - The direct referral traffic these citations brought was **under 1% of total visits**.
- **What the author thought worked best:** making pages for very specific small questions targeted at particular countries; writing content in a comparison format; question-style headings followed immediately by a short 2-to-3-sentence answer; dated, up-to-date data.
- **What this shows:** GEO can be very successful at the "being cited" step, but citations do not automatically turn into clicks. This website's answer happens to be a short fact ("where a given title can be watched in a given country"), and the answer itself can deliver it.

### Story four: citations rising, sales at zero

- **Website:** a small project management software company for businesses (the real-life model for An's scene at the start of this chapter).
- **What was done over 6 months:** core documentation and comparison pages were rewritten with question-style subheadings, answering directly in the first 2 to 3 sentences; structured data for FAQs and products was added site-wide; llms.txt was published; several "A vs. B" and "alternatives to a product" comparison pages were created; mentions of the brand in ChatGPT, Perplexity and Gemini were tracked manually.
- **Results seen:** citations went up, but visitors referred by AI bounced faster than those from organic search, and almost never converted.
- **One explanation (someone in the industry tested this repeatedly, with comparisons):** first split citations by "type of question". If the growth in citations comes from informational questions, readers were already satisfied at the answer, and this is not a conversion problem that can be fixed by changing pages. Only citations from questions where people are "ready to buy" (buyer questions) have a chance of turning into business.
- **What this shows:** **being mentioned many times does not equal being mentioned in the right questions.**

### Story five: AI is still reading, but people have stopped coming

- **Results seen (industry people's own report):** a website's human visits from ChatGPT dropped to zero after mid-May; but ChatGPT crawler reads stayed steady, and the format of the referral source URLs did not change either.
- **Inference:** it was not that the website did something wrong, but that the platform changed which questions get citation cards attached, or the topics that brought traffic were no longer within the range AI answers on its own initiative.
- **What this shows:** the rise and fall of AI traffic may come entirely from the platform's side.

### Story six: the invisible phone call

- **Results seen (observed by someone in the industry, a single observation):** when someone asks AI questions like "best dentist nearby", AI often gives the clinic's name, address and phone number directly. The patient calls directly, clicks no link, leaves no source, and the website dashboard has no record at all.
- **What this shows:** if you measure GEO only by website traffic, you will conclude "no effect at all". In reality, it may be bringing in calls you cannot track. The value of GEO may lie where website analytics tools cannot see.

---

## 8. How to measure without fooling yourself?

### First accept: a big chunk cannot be measured

AI's influence can be drawn as four paths:

```
Someone sees you in an AI answer
   │
   ├─ No click, but remembers your name → later searches your name or types the URL directly
   │                          → recorded as "direct traffic" or "brand search"
   ├─ Clicks, but the platform passes no source information (or it opens in an in-app browser)
   │                          → recorded as "direct traffic"
   ├─ Clicks, and the source information is kept → recorded as an AI referral (the only confirmable part)
   └─ Calls directly, walks into the shop directly → never appears in website data at all
```

The common view in the industry is: because source information is missing, analytics tools wrongly count a large amount of traffic that was actually referred by AI under other categories.

### Eight ways to measure

**1. Always set up a control group.**
Within the same website, leave a batch of pages unoptimized as a control. Compare the growth gap between the two batches. Without a control, the platform's own growth will be mistaken for the effect of optimization. The earlier example, "raw growth of 5.7 times, while the untouched pages also grew 3.5 times", is the best reminder. This point is supported by research data.

**2. Report "confirmed" and "inferred" AI traffic separately.**
- **Confirmed:** visits with AI source information; or AI programs in the server logs that fetch pages in real time on the user's behalf (for example ChatGPT-User, Perplexity-User, Claude-User).
- **Inferred:** visits within "direct traffic" that land straight on a deep documentation page or comparison page.
- When reporting externally, the honest number is the "confirmed" one. The "inferred" part is used to estimate how big the gap is. In one report, the inferred amount was about **2 to 3 times** the confirmed amount.
- This is a practice someone in the industry tested repeatedly, with comparisons (not independently verified).

**3. Split direct traffic by "first page on entry".**
Visitors brought by AI often land straight on a deep documentation page or comparison page. Direct visitors who type the URL by hand almost never enter this way. This too is a practice someone in the industry tested repeatedly, with comparisons.

**4. Ask customers directly: "How did you hear about us?"**
- Ask on the form or in the first call. Use an **open text field**, not a drop-down menu.
- One report showed that about **40% to 50%** of people fill it in.
- Another report showed that **15%** of potential customers said they found the company through AI, while the source-tracking parameters in the URLs showed only **3%**.
- Asking in person is more accurate than a form. However, customers usually cannot remember the exact wording they used when asking AI.
- The industry almost unanimously supports this practice (12 authors in favour, none against).

**5. Cross-check "the source customers report themselves" against "a fixed set of test questions".**
Every month, ask AI the same set of "ready to buy" questions (a prompt set), and record whether you appear and which page is cited. Then compare these changes with changes in the sources customers report themselves. This is a practice observed by someone in the industry and can only serve as a lead.

**6. Local businesses can set up a dedicated phone number.**
This number is placed only on the business profile page and in the business directories AI reads, plus the question "May I ask where you heard about us?" This too is a practice observed by someone in the industry and can only serve as a lead.

**7. Keep an eye on how often your brand name is searched.**
Quite a few in the industry treat it as an early signal of "exposure without clicks". But this point is still marked "disputed": 6 authors support it and none oppose it, yet there is no high-quality evidence; there are also reports that although brand searches rose slightly, the rise was too small to draw a conclusion.

**8. Look for the traces AI Overviews leave in Google Search Console.**
If some pages show "impressions rising, click-through rate falling, average ranking roughly unchanged", this is usually AI Overviews absorbing your clicks. Note: clicks from AI Overviews **cannot be distinguished** from ordinary organic search clicks in analytics tools. This is industry people's own report.

---

## 9. How should the goals change?

Since "being cited" less and less equals "getting clicks", the goals must be adjusted.

**1. Change the goal of GEO from "grabbing clicks" to "being named" plus "catching the people who really want to buy".**
The value of being cited leans more and more towards brand exposure (large-scale real-user data supports the loss of clicks). In addition, someone in the industry observed: AI conversations shorten the customer's "discover and compare" stage, but the sales process after that does not get any shorter.

**2. Prioritize citations in "buyer" questions.**
For questions like "alternatives to X" and "A versus B", AI is more likely to cite comparison pages. Readers brought by informational questions end their journey at the answer. (Someone in the industry tested this repeatedly, with comparisons.)

**3. Catch readers the moment they arrive.**
Visitors referred by AI are often already halfway through making a decision. The first page they see should provide proof, case studies, clear pricing information, and one clear next step. (Observed by someone in the industry; can only serve as a lead.)

**4. Honestly assess how much your business depends on clicks.**
Websites that rely on ads or referral commissions and mainly offer informational content are hit hardest. Reference, tool, developer and subscription websites are better at keeping clicks. (Supported by large-scale real-user data.)

**5. Make more content that answers cannot replace.**
Original viewpoints, firsthand experience, tools, things that can only be done on your website. That experience-based content benefits is supported by large-scale research; in addition, someone in the industry observed that articles with a distinctive argument get far more reader time and engagement than generic explainers.

**6. Don't treat the benefit of experience-based content as a long-term guarantee.**
Experience-based content benefited in the AI Overviews stage, but after the move to AI Mode, this benefit shrank sharply. (Supported by large-scale real-user data.)

**7. If you run an online shop, check that your product data is complete.**
Missing Global Trade Item Numbers (GTIN), outdated stock information, no policy pages such as returns and exchanges, and incomplete data for different variants may make AI agents skip your products entirely. This is a test report from industry people themselves, not independently verified. The industry also widely believes this (15 in favour, 1 against), but that is opinion, not proof.

---

## 10. Practices that are already outdated

**1. Treating total website traffic as the only success metric for SEO or GEO.**
In an environment where answers absorb clicks, "impressions up, clicks down" is normal. Looking only at traffic will lead you to the wrong judgement.

**2. Counting AI traffic only by "source information" (referrer, the piece of information the browser gives the website about "where the visitor came from").**
Most of AI's influence carries no source information. Counting this way will systematically underestimate, and can only serve as a lower bound of "at least this much".

**3. Treating the new "AI category" in analytics tools as the complete answer.**
Someone in the industry observed that in 2026, mainstream website analytics tools added a dedicated traffic category for "AI assistants". But it only captures visits that carry source information: visits from some AI platforms are still classed as ordinary referral traffic; clicks from AI Overviews are still counted as organic search; and past data is not backfilled. In addition, different observers report launch dates and platform coverage that do not agree with each other.

---

## Key points of this chapter

1. **AI search keeps most demand inside the platform.** Only 5.2% of ChatGPT conversations click out to an external website, versus 31.1% for Google search; in a randomized experiment, forcing people to use AI Mode cut the external click-through rate by 18.8 percentage points. This is the conclusion with the strongest evidence in the whole book.
2. **Being cited does not equal being clicked.** Only about 1% of people click a source cited in AI Overviews; Wikipedia, cited heavily, still saw search traffic fall about 5%.
3. **The remaining traffic is selective.** It leans towards reference, academic, developer, tool and subscription websites, and away from ad-supported websites. Experience-based content benefited in the AI Overviews stage, but the benefit shrank sharply under AI Mode.
4. **The return on investment of GEO lacks reliable evidence.** In the only quasi-experimental study, raw growth of 5.7 times shrank to only about 1.8 times after subtracting the platform's own growth, and statistically it is only "some signs".
5. **Evaluating AI traffic always needs a control group.** Otherwise the platform's own growth will be mistaken for the effect of optimization.
6. **"AI traffic is small but may convert better" is a common industry claim, but it has not been proven.** Too few people, self-selected samples and gaps in source tracking can all create the illusion of "converting better"; there are also reports showing that AI visitors almost never convert.
7. **Report sources in layers.** Separate confirmed, inferred and customer-reported AI sources, and accept that part of the value (brand memory, phone calls) can never be measured.
8. **The value of GEO is leaning more and more towards brand exposure.** The goal should shift from "grabbing clicks" to "being named in buyer questions", and the landing pages should catch visitors AI has already filtered.

---

## Remember in one sentence

**Being named by AI is more and more like running a brand ad, not bringing in customers; don't measure it only by clicks, and don't fool yourself with numbers that have no control group.**

---

## What you can do tomorrow

1. **Open Google Search Console** and find the pages with "impressions flat or rising, click-through rate falling, average ranking roughly unchanged". Those are most likely clicks absorbed by AI Overviews.
2. **Add an open question to your enquiry form or first call:** "How did you hear about us?" Use a text field, not a drop-down menu. If you can ask in person, ask in person.
3. **Before your next website change, leave a batch of pages untouched** as a control group.
4. **Report AI traffic in three layers:** confirmed (with AI source information, or with programs that fetch on the user's behalf, such as ChatGPT-User, Perplexity-User, Claude-User, in the server logs), inferred (direct traffic that lands straight on deep documentation pages or comparison pages), and customer-reported. Externally, use only "confirmed" as the official number.
5. **Split direct traffic by "first page on entry"**, and see how many people land straight on deep pages.
6. **Prepare a fixed set of "ready to buy" questions**, ask AI every month, record whether you appear and which page is cited, then compare this with the sources customers report themselves.
7. **Split the questions where AI cites you into two types:** "pure knowledge" and "ready to buy". Put your effort into the latter, especially questions like "alternatives to X" and "A versus B", and the matching comparison pages.
8. **Check which page AI visitors land on most often**, and make sure that page has proof, case studies, clear pricing information, and a clear next step.
9. **If you are a local business**, set up a dedicated phone number placed only on your business profile page and in the directories AI reads, and when answering, ask "May I ask where you heard about us?"
10. **Keep an eye on how often your brand name is searched**, as a reference signal of "exposure without clicks" (but don't treat it as conclusive).
11. **Honestly assess how much your business depends on clicks**; if you rely mainly on ads or commissions and mostly offer informational content, be mentally prepared.
12. **Make more content that answers cannot replace**: original viewpoints, firsthand experience, tools, things that can only be done on your site.
13. **If you run an online shop**, check that every product has a Global Trade Item Number (GTIN), that stock is up to date, that a returns and exchange policy page exists, and that data for every variant is complete.
14. **When measuring GEO, look at three things together**: impressions, visits, revenue.

---

## Stop doing this

1. **Don't use "AI traffic multiplied several times" to prove GEO works.** Most of it may just be more people using AI. A single-day spike counts even less.
2. **Don't treat the "citation share score" of AI visibility tools as a performance metric.** A test report from industry people themselves points out that such scores sample a batch of simulated questions and then extrapolate to the whole of real queries that no one can actually see, so their precision has no basis. They can be a rough directional reference, not an assessment metric.
3. **Don't equate "how many times you were cited" directly with commercial value.** The example of being cited 10,000 times with traffic under 1% shows the two can be completely disconnected.
4. **Don't assume that doing GEO well will make traditional search better too.** The only quasi-experimental study did not see this virtuous circle.
5. **Don't assume that blocking AI training crawlers will protect or increase traffic from AI.** There is only correlational data so far, and it points the opposite way from intuition.
6. **Don't claim "conversion rate several times higher" when the numbers are too small.** With only single-digit visits a day, one or two sales can make the ratio swing wildly.
7. **Stop treating total website traffic as the only success metric**, don't count AI traffic only by source information, and even less treat the new AI category in analytics tools as the complete answer.
8. **Don't treat the benefit experience-based content currently gets as a long-term guarantee.**

---

## What is still uncertain

1. **Are visitors from AI really more likely to buy?** Several industry reports say "yes", and there are also reports saying "they almost never buy". It may really be "already filtered", or it may just be an illusion created by "only the few who most want to buy click through". These cannot be told apart at present.
2. **How much traffic or business can GEO actually bring?** In the only study that seriously separated the effects, the effect was about 1.8 times, but statistically it only counts as "some signs", and it covers only one website with several practices mixed together. The other study was done by the platform itself, with unclear metrics.
3. **What is the relationship between blocking AI crawlers and AI referrals?** So far we only see the correlation that "sites that block actually get more referrals", which may just be because large sites are more likely to block.
4. **Is AI traffic overall growing or shrinking?** Industry opinion is split half and half; an individual site's AI traffic can drop to zero overnight because of platform adjustments.
5. **Can brand search volume serve as a metric of "exposure without clicks"?** Many people think so, but there is no high-quality evidence, and the changes observed are too small.
6. **How long will the benefit of experience-based content last?** It existed in the AI Overviews stage and shrank sharply under AI Mode; it depends on how the interface changes.
7. **Is incomplete product data the main reason AI traffic converts poorly?** There are only unverified industry tests and industry opinion.
8. **The scope of the research:** the clickstream data covers only US desktop computers; the randomized experiment lasted only 7 days, with participants skewing young and highly educated; some results (such as the Wikipedia English-versus-Japanese comparison) had too short an observation period and can only serve as a directional reference.
9. **The platform's claims contradict the research conclusions.** The platform says AI brings more queries and higher-quality clicks, but has not published its methods; the experimental evidence with more transparent methods currently points the opposite way.
10. **Which platforms does the new AI category in analytics tools cover, and when did it launch?** Reports from different observers do not agree.
