# Chapter 10: AI Named You. Now What?

> This chapter covers the last of the seven gates: will people come over, which is user behavior. The earlier chapters were all about "how to get into AI's answers". This chapter asks a more practical question: once you are in, will readers click through to your website, and will they buy? The conclusion first: this is the chapter with the strongest evidence in the whole book, and the strongest evidence does not bring good news.

## Imagine: a Monday morning

Imagine that An runs a small software company that sells a project management tool for businesses. Over the past six months, An followed all kinds of GEO advice and reworked the website. Subheadings became questions, the first two or three sentences of each section gave the answer directly, FAQs were added, and there were several pages of "us versus such-and-such product" comparisons.

The results looked good. When An asked AI, the company name often showed up in the answers, and the number of mentions grew month after month. But this Monday, An opened the website dashboard and froze. AI brought very few visitors, the ones who came left faster than people from ordinary search, and almost no one placed an order.

An's first thought was that something had been done wrong. What this chapter wants to say is that most likely An did nothing wrong. This is simply how AI search works.

## The five questions this chapter answers

This chapter answers five questions in turn. First, after AI search arrived, do websites get more clicks or fewer, and how many fewer? Second, which websites does the remaining traffic flow to, which kinds of content get hurt, and which actually benefit? Third, after doing GEO, how much of the traffic growth comes from optimization, and how much is just the AI platform itself growing? Fourth, if "being cited by AI" brings no clicks, what is its commercial value? Fifth, with incomplete tracking tools, how do you measure the business effect of GEO without fooling yourself?

## 1. The librarian read the books for you

Remember the metaphor used throughout the book? AI is like a very busy librarian. A traditional search engine is more like the library's card catalogue. You ask a question, it hands you a stack of cards and tells you the answer is in these books, so go and look for yourself. You have to walk to the shelf and take the book down, and websites get their clicks from this act of "walking over". Websites trade content for clicks. This is the business model of traditional search, and it can be called sending traffic.

The AI librarian works differently. It reads several books, organizes them, and tells you the answer directly. This is the business model of generative engines, and it can be called answering. Once the question is solved, the reader rarely has a reason to walk to the shelf and flip through that book.

The big idea of this chapter can therefore be written as a chain of cause and effect. The more complete the answer, the less the reader needs to click, and the fewer clicks the source website gets, so being cited does not equal being clicked. This has nothing to do with your ranking dropping. You may still be in the same position, and your content may even be written into the answer, yet the clicks still drain away. So many websites see a strange pattern: **the number of times they are seen (impressions) stays flat or even rises, but the share of people who click through (click-through rate) falls.**

This chain of cause and effect has a precondition, though: the answer is provided by someone else's platform. If the answer is provided by the website itself, things are different. A major US newspaper ran a large-scale randomized experiment in the search function on its own website, with about 38,000 readers taking part over 38 days. Half of the readers saw an extra AI answer above the search results, with the newspaper's own articles attached as sources. As a result, the share of searches followed by a click on ordinary search results fell by 20.8 percentage points, and the articles opened per search fell by about 19%. But readers searched about 29% more often, so counted per reader, the articles opened actually rose by about 5%. The share of people who left right after searching did not differ between the two groups.

The reason is that readers' follow-up questions stayed on the same website. Whoever's platform the follow-up questions stay on gets the traffic that follows. Keep in mind that this is only one newspaper, and it only looks at how engaged readers were. It cannot be extended to general search such as Google, nor can it be used to prove that "AI search increases clicks overall".

## 2. How strong is the evidence? This time, really strong

In many earlier chapters, we could often only say "seen under laboratory conditions" or "someone in the industry tested this themselves". This chapter is different. Several large-scale experiments with real users, using different methods and different data sources, reached conclusions pointing the same way. This is where the evidence in the whole book is hardest.

### From clickstream to randomized experiments

The first set of numbers is 5.2% versus 31.1%. Researchers tracked the real browsing records of a large number of US households on desktop computers, a kind of data called "clickstream". In ChatGPT conversations, only 5.2% of conversations led to a click on an external website; with Google search, this share was 31.1%. Among households that use ChatGPT often, 74.4% had never clicked any external link, which is roughly three quarters. The same data also showed that after more people could use ChatGPT's search feature (ChatGPT Search), traditional search queries fell by 9.4%, and after 20 weeks the drop reached 17.0%. These conclusions are backed by large-scale real-user data, and the research method is close to an experiment.

> **A closer look: what are a "quasi-experiment" and "difference-in-differences"?**
> A true experiment randomly splits people into groups. Often that is not possible, so researchers use changes that happen naturally in the real world, for example some people getting a new feature first and others later, and compare two layers of difference: "before versus after the change" and "the group with the change versus the group without it". This is called "difference-in-differences". This kind of study is not as clean as a randomized experiment, but it is far more reliable than simple observation. The 9.4% and 17.0% above used an advanced version of it called stacked difference-in-differences, which means stacking together several batches of people who got the feature at different times and comparing them.

The second set of numbers is 18.8 percentage points fewer. A randomized experiment with a publicly pre-registered research plan was run on real Google search. Researchers randomly split users into groups, and one group was forced to use Google's conversational AI search (AI Mode). In this group, the share of clicks to external websites fell by 18.8 percentage points. The researchers estimated that the true drop most likely lies between 15.3 and 22.2 percentage points. This range is called the "95% confidence interval", meaning that if the study were repeated many times, the true value would fall within this range in 95% of cases.

Clicks were not the only thing affected. The same experiment found that users forced to use AI Mode made 0.92 fewer searches (search "sessions") per day. On a scale of 1 to 7, their trust dropped by 0.34. Their satisfaction dropped by 0.73 standard deviations, a standard deviation being a unit that measures "how much people's scores usually differ". And the share who switched to other search engines rose by 11.2 percentage points. The experiment also ran the opposite test, asking one group to turn off the AI Overviews at the top of Google search results, and this group's click-through rate rose by 8.8 percentage points. However, only about 51% of the people assigned to this group actually did it, a share called the "compliance rate".

> **A closer look: why does "publicly pre-registered" matter?**
> Before seeing the results, the researchers publicly write down what they will measure and how they will analyze it. That way, they cannot afterwards pick the numbers that suit them to report. This is currently one of the research practices most widely accepted as trustworthy.

### About 1%, and the 5% Wikipedia lost

The third set of numbers is about 1%. Another study recorded the real browsing of 900 US adults, covering 91,121 views of search results pages. About 18% of Google searches showed AI Overviews. When AI Overviews appeared, the share of clicks on traditional search results fell from 15% to 8%, and only about 1% of people clicked a source cited inside AI Overviews. When AI Overviews appeared, 26% of browsing ended on that page, against 16% without them, so AI Overviews make people end their browsing sooner. This study is observational data from a real search engine, not an experiment. It can only show that two things happen together; it cannot prove which causes which. In the newspaper experiment mentioned earlier, the share of people who left right after searching was about 21% in both groups, with no difference. But the two settings differ, one being Google and the other the search on the newspaper's own website, so they cannot be compared directly.

The fourth set of numbers is the roughly 5% Wikipedia lost. Wikipedia is one of the sources AI Overviews cite most often, so in theory, being cited this much should bring benefits. Researchers compared about 500,000 pairs of articles to see what changed after AI Overviews went live by default. Traffic to English Wikipedia from external search fell by 5.45% relative to the German version, and by 4.82% relative to the French version. The researchers also ran a "placebo test" and it passed: they deliberately redid the analysis at times or on subjects where there should be no effect, confirmed that no false effect appeared there, and so showed the result was not a fluke. By the researchers' estimate, this amounts to about 100 million fewer visits per month from search. From this, they inferred that being cited often does not make up for the clicks absorbed by the answer.

These studies also have limits, and we should be honest about them. The clickstream data comes only from desktop computers in the US and does not include phones. The randomized experiment ran for only 7 days, and its participants skewed young and highly educated. The Wikipedia study also had a comparison of the English version against the Japanese version, showing a drop of 16.53%, but the observation period was too short, so it can only serve as side evidence that "points the same way". The study of the 900 people's browsing records is observational; it can only show correlation, not prove causation. Even so, the overall direction is consistent. **AI search keeps most demand inside the platform, and this is the conclusion this book is most confident about.**

### What have people in the industry seen?

Beyond academic research, people in the industry have also measured data from many websites themselves. These were all their own measurements and no one has independently verified them, but on the point that "AI brings very little traffic", their accounts are highly consistent. One person looked at several client websites and found that clearly identifiable AI sources were usually under 5% of total visits, even when the site was cited heavily. Another looked at two websites selling to business customers, where AI sources made up 2% to 4% of visits. Another looked at several content websites, where traffic from ChatGPT was under 2% of organic search traffic. On one client website, ChatGPT brought 251 new users, 0.35% of total traffic. And another person looked at several client accounts, where AI sources made up a low single-digit percentage of the total.

The gap between "being cited" and "being clicked" is even more startling. 6 informational pages were cited by Google's AI over 15 days, generating 9,600 impressions but only 6 clicks. A website dedicated to answering "which streaming platform can I watch this film or show on" became the most-cited source in its small niche within 12 weeks of launch, with 65% of all page citations, and was cited more than 10,000 times in 30 days, yet traffic from AI was under 1% of total visits. The author's conclusion was that citations behave like brand advertising, not like a channel that brings in new customers. Another website had fewer than 50 traditional search visitors a day and was cited by AI assistants about 200 times a day, but ChatGPT brought only 3 to 5 visits a day.

Many in the industry believe that referral traffic from AI tools is still negligible compared with traditional search. This is an opinion, not proof, and "many people believe" does not mean "it is right"; but this opinion points the same way as the research above.

## 3. Who are the visitors that remain?

Clicks do not fall evenly. How badly a website gets hurt depends on two questions. The first question is whether your content can be fully replaced by a paragraph of answer. Definitions, facts and simple calculations can be delivered by the answer itself, and clicks on this kind of content are the easiest to disappear. The second question is what the reader clicks out for. If readers want to use a tool, check original data, read about other people's firsthand experience, or complete a transaction, they still have a reason to leave the answer page.

So the little traffic AI sends out leans towards reference, academic, developer, tool, subscription and non-profit websites, and away from websites that make money from advertising. Large-scale real-user data supports this. After more people used ChatGPT's search feature, search traffic fell for every category of website: academic −32.8%, reference −26.5%, developer −15.1%, news −13.4%. Among clicks sent out by ChatGPT, the share going to ad-revenue websites was 27.6 percentage points lower than Google's. This is a descriptive comparison showing "what the distribution looks like", not a causal inference.

There is an easy point of confusion here. Reference and academic websites take a higher share of "the traffic AI sends out", but the total traffic they get from traditional search is falling too. **Both things are true at once: the share they get is bigger, but the total to be shared is shrinking.**

### "What real people say" used to be a shelter

One very large study looked at 105,012 discussion boards in a large online community forum, and this too is large-scale real-user data. After AI Overviews launched, these boards actually became busier. Daily comments rose by 12.0%, and the number of users commenting rose by 12.4%. Boards for sharing experience grew 2.3 times (comments) and 2.8 times (users) as much as boards for answering facts, and small and medium boards had the largest relative growth. The reason is not hard to understand: AI Overviews are short, and after reading them, people still want to know what those who have actually used something have to say.

But this benefit did not last. The same study found that when the interface became the conversational AI Mode, where you can keep asking follow-up questions, the extra benefit for experience-based boards shrank sharply: the gain in users decayed by about 59%, and the gain in comments almost entirely disappeared. The reason is that readers can keep asking in the conversation, "So what is it like in actual use?", and so even the wish to see real people's experience, a reason to click out, was absorbed by the platform. Static AI Overviews give short answers and readers still want to hear from real people, so experience-based content benefits. Under conversational AI Mode, follow-up questions can be finished inside the platform, and the reason to click on experience-based content gets absorbed as well.

Put the two studies side by side and at first glance they seem to contradict each other. The Wikipedia study says that despite being cited often by AI Overviews, search traffic still fell about 5%; the large community forum study says that after AI Overviews launched, community engagement rose about 12%. One says traffic fell after being cited, the other says it rose. The explanation lies in the different types of content. Wikipedia is fact-based content, and the answer can fully replace it. A forum is experience-based content, and after the answer gives a summary, readers still want to see real people's experiences. This is where the two questions at the start of this section come from. But don't forget that the same forum study also found that under AI Mode, this benefit shrank sharply. So "experience-based content is safer" is only a temporary conclusion, and it depends on what the interface looks like.

## 4. Can GEO actually bring in business? Honestly: the evidence is not there

This is the question many people most want answered. This book's answer is that **there is currently no reliable evidence.**

First, an easy trap to fall into. The whole market of "traffic from AI" is growing fast. Your website's traffic from AI platforms multiplying several times over may simply be because more people use AI search, with nothing to do with your optimization. As a formula:

```
The growth you see = the platform's overall growth + the effect of your optimization + random fluctuation
```

If you don't keep a set of "untouched pages" for comparison, you simply cannot separate out the middle term.

### The only study that seriously separated them

So far, only one study has done this separation. It was a "natural experiment" a website ran based on its own server logs: some pages were optimized, and the other pages were left alone. For the optimized pages, monthly traffic from ChatGPT grew to 5.7 times, which sounds amazing. But pages that were not touched at all also grew to 3.5 times in the same period. After subtracting that, the effect the optimization really brought was about 1.82 times. The researchers estimated that the true value most likely lies between 1.31 and 2.54 times; recalculated with several different analysis methods, the result was between 1.8 and 2.3 times.

This effect of around 1.8 times comes with many caveats. The researchers ran a check, pretending the "date optimization started" had been moved to a different time to see whether an effect also appeared there, and this check was not convincing enough (statistically p=0.16, while the usual requirement is below 0.05). So the result only counts as "some signs" and cannot be called solid. In addition, the study covers only one website, the author comes from industry, and several practices went live at the same time, so it is impossible to tell which one worked.

This website did four things at the same time. It tidied up its URLs, keeping only one standard URL for the same content. It used URLs that AI crawlers requested but that did not exist on the site (requests that got "page not found" errors) to work out what readers really wanted. It changed its titles into questions. And it added to each page a summary that can be read on its own. This combination matches growth of about 1.8 to 2.3 times, but it cannot say which item was doing the work.

The study had two more results worth noting. One is that on a single day there was a spike of 38.2 times, but this kind of raw multiple cannot be taken as the effect of optimization. The other is that GEO was not seen to lift traditional search along with it. In the same period, the site's organic clicks from Google actually fell by about 25%, and not because Google removed the pages from its index. The virtuous circle often called the "flywheel effect", meaning "do GEO well and traditional search will improve too", did not appear here.

### Another study, and the current conclusion

A large image platform ran its own A/B test, splitting users into two groups, one using the new approach and one kept as it was, and comparing the results. In a 4-week experiment, the group using the new feature had 1.18 times the visits of the control group, while the group where the feature was removed had 0.82 times. The numbers look good, but there are many problems. The authors are the platform itself. The paper mentions "generative search traffic grew 9.2 times" but does not explain how this metric is defined. And the paper claims a 20% traffic increase, while the figures in its own tables are only +0.83% to +1.83%, so the two do not match.

So the conclusion is that no study so far has proven that GEO reliably brings traffic or sales. Of the two existing studies, one is not statistically convincing enough, and the other was done by the platform itself, with unclear metrics. The practical meaning behind this is that **the value of "being cited" leans more and more towards brand exposure, and clicks carry less and less weight.** When measuring GEO, you must look at three things together: impressions, visits and revenue. And you must accept that part of it cannot be measured accurately.

## 5. Are visitors from AI more likely to buy?

This is the question the industry discusses most, and disagrees on most. Everything in this section comes from industry people's own reports, and no one has independently verified them.

The "yes" side has quite a few examples. Someone in the industry tested this repeatedly themselves, with comparisons, and found that ChatGPT brought only single-digit visits a day, but the conversion rate was about 8 times that of organic search traffic. In his words, this is a channel for sales, not a channel for traffic. On another client website, the "engagement rate" (the share of visits that actually did something on the page) of visitors referred by ChatGPT was 48.57%, higher than Google paid search (39.71%), Google organic search (34.71%), Bing organic search (33.92%) and visitors who typed the URL directly (20.73%). There are also reports that visitors referred by ChatGPT and Perplexity had a lower rate of leaving after one page (bounce rate) and viewed more pages per visit. Other reports say the conversion rate of visitors from AI sources was about 2 times the site-wide average, but because the base number of people is very small, this means little. For one client with a "dedicated AI source category", 97% of 450 AI visits came from ChatGPT, and the sales quality was better than ordinary organic search traffic. Other people in the industry have also reported various multiples such as 3 times, 7 times and 16 times, but each is only a single observation and can only serve as a lead. The reasoning on this side is that "they have already been filtered": in the AI conversation, readers have already compared and narrowed down their options, so when they click through, they already have a clear goal in mind.

### The "not so good" or "not necessarily" side

The other side has its own examples. An online software service company selling to businesses spent 6 months on a full set of optimizations for AI answers, including putting the answer first, adding structured data for FAQs and products, publishing an llms.txt file (a site description file written specifically for AI), and making comparison pages. Citations went up, but visitors referred by AI bounced faster than those from organic search, and almost never converted.

Someone in the industry tested 8,520 shopping queries and found that traffic from AI converted 86% worse than affiliate links, the links that "recommend products and earn a commission". He put this down to product data not meeting the requirements of AI agents. AI agents are AI programs that compare prices and place orders for people automatically, and these products were missing Global Trade Item Numbers (GTIN), had outdated stock information, had no returns and exchange policy page, and had incomplete data for different variants (for example size and colour). This one has not been independently verified either. Some in the industry also believe that most claims that "AI traffic converts well" overstate AI's contribution to sales by 2 to 5 times, because source tracking itself is inaccurate. And one author originally claimed that the high engagement on his site came from AI citations, but later, when he checked the sources, he found this traffic had not come from AI at all. He corrected himself, saying it is still too early to say it was brought by AI citations.

The reasoning on this side is that "it depends on the question". If the growth in citations comes from informational questions, the reader has already finished the task at the answer, so naturally they won't buy when they click through. Someone in the industry tested this repeatedly, with comparisons, and found that in questions like "what are the alternatives to X", comparison pages (pages whose URLs often contain /vs, /alternatives or /compare) made up 34% to 43% of citations; in questions like "what is the best X", comparison pages made up only 2.8%; and informational questions mostly cited documentation pages.

### Both sides are stuck on the same problem

The difficulty both sides share is that there are too few people and the sources cannot be fully tracked. With single-digit visitors a day, one or two extra sales can flip the ratio dramatically. The industry view is that the claim "traffic referred by AI converts better" is supported by 6 authors with no one publicly opposing it, yet it is still marked "disputed", because there is no high-quality evidence directly supporting it. "Many people believe" does not mean "it is right".

This book's position is to draw no conclusion. "Converts better" appears in several industry reports, but all of them use self-selected samples, very small numbers of people and incomplete source tracking. It may be true, or it may just be an illusion created by the fact that only the few people who most want to buy click through, which is called "selection bias". **At present, these two explanations cannot be told apart.**

## 6. AI traffic can also vanish overnight

Traffic from AI is not only small but also unstable. Whether it is growing or shrinking, the industry cannot say clearly. On the question of whether "ChatGPT brings significant traffic to websites", industry opinion is completely split, with 5 authors on each side. Someone in the industry reported that a travel website's referral traffic from ChatGPT fell by about 50% within 11 days (5 July to 16 July), although the remaining traffic converted better.

Another industry report is even more extreme. A website's human visits from ChatGPT peaked at 1 to 3 a day from 7 May to 15 May, and dropped to zero from 16 May. But over the same period, the number of times ChatGPT's crawlers read the site, including ChatGPT-User, which reads in real time on the user's behalf, and GPTBot, which collects data, stayed at about 30 to 50 a day with no drop at all, and the format of the source URLs did not change either. The reporter's interpretation is that the content is still being read, it just no longer appears in answers as a "clickable link". Being read does not equal being shown. He inferred that the problem was not the website itself, but that the platform had changed "which questions get citation cards attached", or that the topics that used to bring traffic were no longer within the range AI answers on its own initiative. **The platform only has to adjust its rules a little, and a website's AI traffic can drop to zero overnight, with nothing to do with what the website itself did.**

### Can blocking AI crawlers protect your traffic?

The appendix of a large-scale clickstream study looked at this in passing. About 79% of websites blocked at least one AI crawler, and the websites that blocked actually had a higher average referral from ChatGPT (6.48) than those that did not block (4.48). The researchers' interpretation is that blocking crawlers that "collect data to train AI" does not stop ChatGPT from sending people over "when answering questions". But this is only two things appearing together, which is correlation, not causation. It may also be that large websites already have large traffic and also happen to be more likely to block.

In addition, the research conclusions run opposite to the platform's claims. The publicly pre-registered randomized experiment found that AI Mode reduced the number of searches per day, which points in the opposite direction from Google's official claim that "AI increases queries and brings higher-quality clicks". The difference between the two is that the experiment used forced group assignment and third-party measurement, while the platform's data did not come with published methods. On methodological transparency, the experiment's evidence is more trustworthy.

## 7. Stories from a few real websites

The following are all firsthand reports from industry people themselves, and no one has independently verified them. They are used to illustrate what the principles look like on real websites, not as proof.

### Ranking unchanged, clicks absorbed by the answer

The first story comes from an independent French product review website that keeps running on commissions from recommending products. Google's AI Overviews launched in France on 22 July, and the site's owner compared two comparable weeks before and after the launch. Clicks from Google search fell 25%, while impressions were almost unchanged (+0.1%). For a query ranked first, the click-through rate dropped from 54.5% to 16.7% within a week. Revenue fell by nearly 47%, about twice the drop in traffic, and the number of items sold also fell, showing that not only did fewer people come, but those who came were also less likely to buy. The ranking did not change, impressions did not change, and the clicks were absorbed by the answer; informational queries in the review category are the easiest to replace with an answer.

The second story comes from the website of a small law firm. The owner compared the same informational page, in the same ranking position, over two years. Two years ago, the page had about 4,000 to 5,000 impressions and brought about 800 clicks a month; now, 1,200 impressions bring only 90 clicks. What still supports the business is people who search the firm's name directly and people referred by past clients; informational queries can no longer carry it. This is a single firsthand observation and can only serve as an example. What it shows is that informational traffic drained away, while traffic from people who know your name and actually need something done stayed.

### Cited a lot, but the business didn't come

The third story is about a new website, 12 weeks old, dedicated to answering "which streaming platform can I watch a given film or show on" for Asian markets. From day one it optimized for AI answers and did not compete for traditional search rankings. As a result, in a set of queries in its small niche, it became the most-cited source, with 65% of all page citations, ahead of large aggregator websites, and in 30 days it was cited by Copilot more than 10,000 times. But the direct referral traffic these citations brought was under 1% of total visits. The author thought four practices worked best: making pages for very specific small questions targeted at particular countries; writing content in a comparison format; using question-style headings followed immediately by a short answer of 2 to 3 sentences; and providing dated, up-to-date data. This example shows that GEO can be very successful at the "being cited" step, but citations do not automatically turn into clicks. This website's answer happens to be a short fact, namely where a given title can be watched in a given country, and the answer itself can deliver it.

The fourth story is about a small company making project management software for businesses, the real-life model for An's scene at the start of this chapter. Over 6 months, the company rewrote its core documentation and comparison pages with question-style subheadings, answering directly in the first 2 to 3 sentences; added structured data for FAQs and products site-wide; published llms.txt; created several "A vs. B" and "alternatives to a product" comparison pages; and tracked mentions of the brand in ChatGPT, Perplexity and Gemini by hand. Citations went up, but visitors referred by AI bounced faster than those from organic search, and almost never converted. Someone in the industry, who tested this repeatedly with comparisons, offers one explanation: first split citations by "type of question". If the growth in citations comes from informational questions, readers were already satisfied at the answer, and this is not a conversion problem that changing pages can fix. Only citations from questions where people are ready to buy (buyer questions) have a chance of turning into business. **Being mentioned many times does not equal being mentioned in the right questions.**

### The part you cannot measure

The fifth story was mentioned earlier. A website's human visits from ChatGPT dropped to zero after mid-May, but reads by ChatGPT's crawlers stayed steady, and the format of the referral source URLs did not change either. The reporter inferred that the problem was not the website, but that the platform had changed which questions get citation cards attached, or that the topics that brought traffic were no longer within the range AI answers on its own initiative. The rise and fall of AI traffic may come entirely from the platform's side.

The sixth story is about the invisible phone call, a single observation reported by someone in the industry. When someone asks AI questions like "best dentist nearby", AI often gives the clinic's name, address and phone number directly. The patient calls directly, clicks no link and leaves no source, and the website dashboard has no record at all. If you measure GEO only by website traffic, you will conclude it has "no effect at all", when in reality it may be bringing in calls you cannot track. The value of GEO may lie where website analytics tools cannot see.

## 8. How to measure without fooling yourself?

First, accept that a big chunk of AI's influence cannot be measured. After someone sees you in an AI answer, they will take roughly one of four paths:

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

Of the four paths, only the third can be confirmed. The common view in the industry is that because source information is missing, analytics tools wrongly count a large amount of traffic that was actually referred by AI under other categories. The eight ways of measuring below are designed with this in mind.

### Control groups and layered reporting

The first method, and the most important, is to **always set up a control group.** Within the same website, leave a batch of pages unoptimized as a control, and compare the growth gap between the two batches. Without a control, the platform's own growth will be mistaken for the effect of optimization. The earlier example, "raw growth of 5.7 times, while the untouched pages also grew 3.5 times", is the best reminder. This point is supported by research data.

The second method is to report "confirmed" and "inferred" AI traffic separately. Confirmed AI traffic means visits that carry AI source information, or AI programs in the server logs that fetch pages in real time on the user's behalf, such as ChatGPT-User, Perplexity-User and Claude-User. Inferred AI traffic means visits within "direct traffic" that land straight on a deep documentation page or comparison page. When reporting externally, the honest number is the "confirmed" one, and the "inferred" part is used to estimate how big the gap is. In one report, the inferred amount was about 2 to 3 times the confirmed amount. This is a practice someone in the industry tested repeatedly, with comparisons, and it has not been independently verified.

The third method is to split direct traffic by "first page on entry". Visitors brought by AI often land straight on a deep documentation page or comparison page, while direct visitors who type the URL by hand almost never enter this way. This too is a practice someone in the industry tested repeatedly, with comparisons.

### Ask customers, set up a phone line, watch brand searches

The fourth method is the simplest: ask customers directly, "How did you hear about us?" Ask on the form or in the first call, and use an open text field, not a drop-down menu. One report showed that about 40% to 50% of people fill it in. Another report showed that 15% of potential customers said they found the company through AI, while the source-tracking parameters in the URLs showed only 3%. Asking in person is more accurate than a form, though customers usually cannot remember the exact wording they used when asking AI. The industry almost unanimously supports this practice, with 12 authors in favour and none against.

The fifth method is to cross-check the sources customers report themselves against a fixed set of test questions. Every month, ask AI the same set of "ready to buy" questions (a prompt set), record whether you appear and which page is cited, and then compare these changes with changes in the sources customers report themselves. This is a practice observed by someone in the industry and can only serve as a lead. The sixth method suits local businesses: set up a dedicated phone number placed only on your business profile page and in the business directories AI reads, and when answering, add the question "May I ask where you heard about us?" This too is a practice observed by someone in the industry and can only serve as a lead.

The seventh method is to keep an eye on how often your brand name is searched. Quite a few in the industry treat it as an early signal of "exposure without clicks", but this point is still marked "disputed": 6 authors support it and none oppose it, yet there is no high-quality evidence, and there are also reports that although brand searches rose slightly, the rise was too small to draw a conclusion.

The eighth method is to look for the traces AI Overviews leave in Google Search Console. If some pages show "impressions rising, click-through rate falling, average ranking roughly unchanged", this is usually AI Overviews absorbing your clicks. Keep in mind that clicks from AI Overviews cannot be distinguished from ordinary organic search clicks in analytics tools. This is industry people's own report.

## 9. How should the goals change?

Since "being cited" less and less equals "getting clicks", the goals must be adjusted. The most fundamental step is to change the goal of GEO from "grabbing clicks" to "being named", plus "catching the people who really want to buy". The value of being cited leans more and more towards brand exposure, and the loss of clicks is supported by large-scale real-user data. In addition, someone in the industry observed that AI conversations shorten the customer's "discover and compare" stage, but the sales process after that does not get any shorter.

Next, prioritize citations in "buyer" questions. For questions like "alternatives to X" and "A versus B", AI is more likely to cite comparison pages, while readers brought by informational questions end their journey at the answer. This is the result of someone in the industry testing repeatedly, with comparisons. At the same time, catch readers the moment they arrive. Visitors referred by AI are often already halfway through making a decision, and the first page they see should provide proof, case studies, clear pricing information and one clear next step. This is a practice observed by someone in the industry and can only serve as a lead.

You also need to assess honestly how much your business depends on clicks. Websites that rely on ads or referral commissions and mainly offer informational content are hit hardest, while reference, tool, developer and subscription websites are better at keeping clicks; this is supported by large-scale real-user data. So make more content that answers cannot replace, such as original viewpoints, firsthand experience, tools, and things that can only be done on your website. That experience-based content benefits is supported by large-scale research; in addition, someone in the industry observed that articles making a distinctive argument get far more reader time and engagement than generic explainers. However, **don't treat the benefit of experience-based content as a long-term guarantee.** Experience-based content benefited in the AI Overviews stage, but after the move to AI Mode this benefit shrank sharply, which is also supported by large-scale real-user data.

Finally, if you run an online shop, check that your product data is complete. Missing Global Trade Item Numbers (GTIN), outdated stock information, no policy pages such as returns and exchanges, and incomplete data for different variants may make AI agents skip your products entirely. This is a test report from industry people themselves, not independently verified. The industry also widely believes this, with 15 in favour and 1 against, but that is opinion, not proof.

## 10. Practices that are already outdated

The first outdated practice is treating total website traffic as the only success metric for SEO or GEO. In an environment where answers absorb clicks, "impressions up, clicks down" is normal, and looking only at traffic will lead you to the wrong judgement.

The second outdated practice is counting AI traffic only by "source information". Source information (the referrer) is the piece of information the browser gives the website about "where the visitor came from", and most of AI's influence carries no source information. Counting this way will systematically underestimate, and can only serve as a lower bound of "at least this much".

The third outdated practice is treating the new "AI category" in analytics tools as the complete answer. Someone in the industry observed that in 2026, mainstream website analytics tools added a dedicated traffic category for "AI assistants", but it only captures visits that carry source information. Visits from some AI platforms are still classed as ordinary referral traffic, clicks from AI Overviews are still counted as organic search, and past data is not backfilled. In addition, different observers report launch dates and platform coverage that do not agree with each other.

## Key points of this chapter

AI search keeps most demand inside the platform. Only 5.2% of ChatGPT conversations click out to an external website, versus 31.1% for Google search, and in a randomized experiment, forcing people to use AI Mode cut the external click-through rate by 18.8 percentage points. This is the conclusion with the strongest evidence in the whole book. Being cited does not equal being clicked either: only about 1% of people click a source cited in AI Overviews, and Wikipedia, though cited heavily, still saw search traffic fall about 5%.

The remaining traffic is selective. It leans towards reference, academic, developer, tool and subscription websites, and away from ad-supported websites. Experience-based content benefited in the AI Overviews stage, but the benefit shrank sharply under AI Mode.

The return on investment of GEO lacks reliable evidence. In the only quasi-experimental study, raw growth of 5.7 times shrank to only about 1.8 times after subtracting the platform's own growth, and statistically it is only "some signs". This also shows that evaluating AI traffic always needs a control group, or else the platform's own growth will be mistaken for the effect of optimization. "AI traffic is small but may convert better" is a common industry claim, but it has not been proven. Too few people, self-selected samples and gaps in source tracking can all create the illusion of "converting better", and there are also reports showing that AI visitors almost never convert.

Report sources in layers, separating confirmed, inferred and customer-reported AI sources, and accept that part of the value (brand memory, phone calls) can never be measured. Taken as a whole, the value of GEO leans more and more towards brand exposure. The goal should shift from "grabbing clicks" to "being named in buyer questions", and the landing pages should catch visitors AI has already filtered.

## Remember in one sentence

**Being named by AI is more and more like running a brand ad and less and less like bringing in customers; don't measure it only by clicks, and don't fool yourself with numbers that have no control group.**

## What you can do tomorrow

1. Open Google Search Console and find the pages with "impressions flat or rising, click-through rate falling, average ranking roughly unchanged". Those are most likely clicks absorbed by AI Overviews.
2. Add an open question to your enquiry form or first call, "How did you hear about us?", using a text field rather than a drop-down menu; if you can ask in person, ask in person.
3. Before your next website change, leave a batch of pages untouched as a control group.
4. Report AI traffic in three layers: confirmed (with AI source information, or with programs that fetch on the user's behalf, such as ChatGPT-User, Perplexity-User and Claude-User, in the server logs), inferred (direct traffic that lands straight on deep documentation pages or comparison pages), and customer-reported. Externally, use only "confirmed" as the official number.
5. Split direct traffic by "first page on entry", and see how many people land straight on deep pages.
6. Prepare a fixed set of "ready to buy" questions, ask AI every month, record whether you appear and which page is cited, and then compare this with the sources customers report themselves.
7. Split the questions where AI cites you into two types, "pure knowledge" and "ready to buy", and put your effort into the latter, especially questions like "alternatives to X" and "A versus B" and the matching comparison pages.
8. Check which page AI visitors land on most often, and make sure that page has proof, case studies, clear pricing information and a clear next step.
9. If you are a local business, set up a dedicated phone number placed only on your business profile page and in the directories AI reads, and when answering, ask "May I ask where you heard about us?"
10. Keep an eye on how often your brand name is searched, as a reference signal of "exposure without clicks", but don't treat it as conclusive.
11. Honestly assess how much your business depends on clicks; if you rely mainly on ads or commissions and mostly offer informational content, be mentally prepared.
12. Make more content that answers cannot replace, such as original viewpoints, firsthand experience, tools, and things that can only be done on your site.
13. If you run an online shop, check that every product has a Global Trade Item Number (GTIN), that stock is up to date, that a returns and exchange policy page exists, and that data for every variant is complete.
14. When measuring GEO, look at three things together: impressions, visits and revenue.

## Stop doing this

**Don't use "AI traffic multiplied several times" to prove GEO works.** Most of it may just be more people using AI, and a single-day spike counts even less. In the same way, don't claim a "conversion rate several times higher" when the numbers are too small; with only single-digit visits a day, one or two sales can make the ratio swing wildly.

Don't treat the "citation share score" of AI visibility tools as a performance metric. A test report from industry people themselves points out that such scores sample a batch of simulated questions and then extrapolate to the whole of real queries that no one can actually see, so their precision has no basis. They can be a rough directional reference, not an assessment metric. And don't equate "how many times you were cited" directly with commercial value; the example of being cited 10,000 times with traffic under 1% shows the two can be completely disconnected.

Don't assume that doing GEO well will make traditional search better too; the only quasi-experimental study did not see this virtuous circle. And don't assume that blocking AI training crawlers will protect or increase traffic from AI; there is only correlational data so far, and it points the opposite way from intuition.

Stop treating total website traffic as the only success metric, don't count AI traffic only by source information, and even less treat the new AI category in analytics tools as the complete answer. Finally, don't treat the benefit experience-based content currently gets as a long-term guarantee.

## What is still uncertain

**Are visitors from AI really more likely to buy?** Several industry reports say "yes", and there are also reports saying "they almost never buy". It may really be that they were "already filtered", or it may just be an illusion created by "only the few who most want to buy click through". These cannot be told apart at present.

**How much traffic or business can GEO actually bring?** In the only study that seriously separated the effects, the effect was about 1.8 times, but statistically it only counts as "some signs", and it covers only one website with several practices mixed together. The other study was done by the platform itself, with unclear metrics.

**What is the relationship between blocking AI crawlers and AI referrals?** So far we only see the correlation that "sites that block actually get more referrals", which may just be because large sites are more likely to block.

**Is AI traffic overall growing or shrinking?** Industry opinion is split half and half, and an individual site's AI traffic can drop to zero overnight because of platform adjustments.

**Can brand search volume serve as a metric of "exposure without clicks"?** Many people think so, but there is no high-quality evidence, and the changes observed are too small.

**How long will the benefit of experience-based content last?** It existed in the AI Overviews stage and shrank sharply under AI Mode; it depends on how the interface changes.

**Is incomplete product data the main reason AI traffic converts poorly?** So far there are only unverified industry tests and industry opinion.

**How wide is the scope of the research?** The clickstream data covers only US desktop computers; the randomized experiment lasted only 7 days, with participants skewing young and highly educated; and some results, such as the Wikipedia English-versus-Japanese comparison, had too short an observation period and can only serve as a directional reference.

**Why do the platform's claims contradict the research conclusions?** The platform says AI brings more queries and higher-quality clicks, but has not published its methods; the experimental evidence with more transparent methods currently points the opposite way.

**Which platforms does the new AI category in analytics tools cover, and when did it launch?** Reports from different observers do not agree.
