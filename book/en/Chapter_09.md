# Chapter 9: AI Is Rolling Dice, and How to Measure Without Fooling Yourself

## The meeting sparked by one screenshot

Imagine this scene (purely hypothetical). The owner of an online coffee bean shop asks AI one morning: "Recommend a few online coffee bean shops that are good for beginners." The second shop in the answer is his own. He is delighted and sends the screenshot to the whole team.

That afternoon An, someone on the team, asks the same question, and this time they are not in the answer. An asks again, and this time they appear, in fifth place. One more try, and they are gone again. So which time is the "real" one?

In fact every one of them is real, but no single one means anything on its own. This chapter makes just one point: **AI answers questions as if it were rolling dice. What you should count is how many times you appear after many rolls. What place you rank in any single roll means very little.**

The earlier chapters covered the seven gates an AI goes through to answer a question: whether to search, whether it can get in the door, whether it can find you, whether it picks you, whether it mentions you, whether it actually uses you, and whether people come over. They also covered where you can push at each gate. This chapter is about how to see the results of those gates. If the measurement method itself is unreliable, none of the earlier effort can be verified.

This chapter answers five questions in turn. First, why does asking AI once and taking a screenshot prove almost nothing? Second, how many repetitions, and how much coverage, does a credible AI visibility number need? Third, are the answers you see through the programming interface, the web version and the mobile app the same, and which one should you test? Fourth, why should "mentioned", "cited" and "recommended" be counted separately? Fifth, how do you judge whether the numbers from a tracking tool or a GEO service provider can be trusted?

## 1. Every question is just one roll of the dice

A traditional search results page stays roughly fixed over a short period. You search once, a colleague searches again, and you see about the same order, so "we rank number 3" is a meaningful sentence. Search used to be more like a notice board. Today's AI is more like a die.

For the same question, every time AI answers, it has to go through several steps that change. First it splits your question into several smaller questions and searches them separately. This is called query fan-out, and the smaller questions may be different each time. Next it pulls in material, but the search index and live results are themselves always changing, so the shortlist it pulls back may be different each time. Finally it writes the answer, and the writing itself has some randomness built in.

```
The same question
   │
   ├─► Break down the question (may be split differently each time)
   ├─► Pull in material (index and live results are changing)
   ├─► Write the answer (randomness built in)
   ▼
One answer = one draw from "all possible answers"

Ask N times ──► N answers ──► mention rate (e.g. appeared 7 times out of 20) + margin of error
```

So every answer you see is just one sample drawn from a large pile of "possible answers". Rolling a 6 once does not mean this die always rolls 6. That is why the right unit for measuring AI visibility is a proportion: on a fixed set of questions, after asking many times, the share of times you appear. This proportion is called the mention rate, and the fixed set of questions is called the prompt set.

### The variation seen in research and industry tests

Researchers who tested real AI search repeatedly saw a great deal of variation. They measured 4 AI search engines every day for 45 consecutive days and compared how much the cited sources overlapped from one day to the next. The overlap was only 0.34 to 0.42 (1 means identical, 0 means completely different). Put plainly, about two-thirds of the sources changed every day. When the same question was asked 10 times within one day, the overlap of sources was 0.32 to 0.43, about the same as across days. This shows that the variation comes mainly from the randomness of each individual question, and not from "today's web being different from yesterday's". The same study also found that some engines often list no sources at all: for one engine, 57.8% of answers cited no source whatsoever.

Another study saw similar results. Researchers ran the same query repeatedly on three engines and compared the overlap of cited domains (taking the median). One engine was about 0.29 to 0.31, another 0.33 to 0.40, and even the most stable was only 0.50. The numbers are imprecise even for frequently cited sites. Even for a very frequently cited domain, the "citation share" from a single test had a margin of error (the range you can be 95% sure of) as wide as 3 to 7 percentage points. Many of the apparent "gaps" between domains actually fall within the noise.

People in the industry testing on their own saw the same direction. Someone in the industry ran repeated tests with control groups (but no one has independently verified them): across 197 websites in the same industry and three engines, with each question run three times, 32% of citations appeared only once in the three runs. When the same question was run twice within 24 hours, the brand recommended in first place was different 48.5% of the time. When the same batch of 45 local-service questions, with exactly the same wording and a brand-new conversation each time, was run twice, one engine replaced about a third of the businesses it recommended.

### What does "appeared 4 times out of 10" actually mean?

Suppose you are a bit more careful. You ask the same question 10 times, your brand appears 4 times, and you say: "Our mention rate is 40%." That sounds scientific. But work it out with statistics, and with only 10 questions and 4 appearances, you can be 95% sure that the true mention rate falls somewhere between about 12% and 74%. That range is so wide it tells you almost nothing.

**Any percentage that doesn't tell you "how many times it was asked" carries almost no information.** A screenshot is even less. It doesn't count as evidence. It is just one roll of the dice.

> **A closer look: what does "margin of error" mean?**
> In statistics this is called a "confidence interval". It means: given how many times you asked and how many times you appeared, the range in which the true mention rate "very likely" falls. The fewer times you ask, the wider the range. For 4 out of 10, the range is 12% to 74%. The only way to narrow it is to ask more, and to ask more different kinds of questions.

## 2. Rolling more times is not as good as rolling in different ways

"Run it a few more times" is right, but doing only that is not enough. Researchers tested real AI search and broke down more than 10,000 answers about brands to find out where the differences between answers mainly came from. They found that the language of the question was the largest systematic source of difference, accounting for about 26.5% of the variation in individual answers, while the brand itself accounted for only 1.5%. After the same question had been repeated 5 times, asking it 5 more times barely reduced the error, whereas asking in 3 more languages reduced the error by about 15 times as much. Looking at just one answer, the reliability for telling "which brand is better" was only about 0.01, practically zero. The study also found that brands are more stable than URLs: for "whether a given brand is mentioned", the overlap between consecutive days was about 0.45 to 0.59, while for "which URLs are cited" it was only 0.34 to 0.42.

A few caveats come with this study. The authors themselves provide visibility services. What it measured was AI's sentiment toward brands (favourable or unfavourable), not mention rate. And its margin of error has not yet been calculated. So the evidence is fairly weak, but the direction is worth considering: **rather than rolling the same die a hundred times on one question, roll different dice on different tables.** Switching engines, languages, regions and phrasings shows you the whole picture better than asking the same sentence over and over.

### How many times should you ask? There is no fixed answer

There is no single fixed number for how large a sample you need. One study used 10 topics, 125 queries per topic and 3 platforms. Its method was to collect while watching whether the rankings had settled, and to stop only once they stopped changing. This approach is called sequential convergence. Most combinations settled after 33 to 75 responses, but 3 combinations had still not settled after 125, and all 3 of them came from the same engine.

If you instead stop at a fixed threshold, for example "stop when the correlation between two successive rankings reaches 0.95 or above", the results become much less reliable. 30 combinations reached the threshold, but only 19 held it afterwards. Judging only by whether the ranking was stable, the agreement between the order at the stopping point and the final result was as low as 0.364 in the worst case. Adding one more condition, that "the signal must be clearly larger than the noise", raised the worst case to 0.717. This shows that stopping just because "the ranking seems to have stopped moving" can easily lead to a premature conclusion.

The fewer citations an engine gives, the more times you need to ask. The number of citations per answer varies a lot between engines: two engines give about 15 to 50 citations per answer, while another gives only about 4 to 6. The fewer the citations, the less information each question yields, and the more questions you need to collect. Another study estimated that to narrow the margin of error on citation share to 5 percentage points, the three engines would need roughly 30 to 50, 90 to 100, and more than 150 queries respectively.

Finally, keep two things apart: "asking again" and "asking another way". Asking the same question again smooths out randomness. Asking it another way tests whether you are still there once the wording changes. Many people in the industry believe you need to do both, and that doing only one will still mislead you.

## 3. Where you look decides what you see

When you hear "I saw myself in AI", the first thing to ask is: where did you see it? The same AI actually has several "windows", and researchers testing real AI search repeatedly found large gaps between some of them. The web version that ordinary people open in a browser can be checked by hand or captured automatically with a browser, and its sources overlap with those of the programming interface by only 12.0% to 14.8%. The mobile app is usually checked by hand, and its domain overlap with the web version of the same platform is only 0.19 to 0.51; for one platform, at the URL level, it is only 0.014. The programming interface is the access point for engineers, which the industry calls an API, and it has to be called automatically by a program. With search turned on, some programming interfaces do not return certain social platform sources (such as X) that the web version would show.

The problems with two other windows are more fundamental. If the programming interface has search turned off, what you measure is AI's memory, not what it found by going online. Your own logged-in account is influenced by your past conversations and by what it remembers about you.

Another study, which captured how the ChatGPT web version actually works (versions 5.2 to 5.5), added more detail. The URLs cited through the programming interface matched those of the web version only 13% to 15% of the time. At the domain level it was better, at 28% to 41%. So comparisons need to separate two levels, "URL" and "domain". The study also found that thinking mode changes search behaviour: fast mode mostly searches only one round, while thinking mode averages just over 3 rounds and about 12 queries. The web version may also quietly switch to a different model partway through a conversation. So when measuring, record which mode you used and how high the thinking effort was.

The differences between engines are also large. Faced with the same query, two mainstream engines shared on average only 5.4% of their domains, and in 76.7% of comparisons the two sides had no domain in common at all. Many tracking tools ask automatically through the programming interface, while ordinary users see the web version or the app. **What the two sides see may be two different worlds.**

### A few more layers that are easy to overlook

People in the industry who tested this themselves (mostly repeated tests with control groups, but no one has independently verified them) added several layers that are easy to overlook.

The most basic layer is whether the answer went to look things up at all, and whether it listed sources. In about 2,600 runs, one engine gave no sources at all in 282 of 615 runs (46%), while another engine included sources in all 359 of its runs. In another record covering 10 days and 2,209 answers, one engine showed sources in only 59% of its answers. So "not appearing in the answer" means different things on different engines. Being absent from an answer that lists a dozen or more sources means you really weren't chosen. Being absent from an answer that lists no sources at all tells you almost nothing.

One layer further back is whether an AI answer was triggered at all. When the same query was searched repeatedly from the same location a few minutes apart, an AI summary appeared in only about 7 out of 10 searches. If you search only once and see "no AI summary", you cannot draw a conclusion.

Location and language also change the results. With the same model and the same question, simply telling it which country the user was in moved one brand from "not mentioned" to "named" in 5 out of 6 cases. When the same batch of questions was asked in two languages, the cited sources overlapped by only 22%. There is a gap of this kind between the programming interface and the product interface too: for the same query, the product interface cited a platform's own content about 50% of the time, but 30 runs through the programming interface produced not a single such citation.

## 4. Scores are "defined" by the rules

One theoretical analysis recalculated already-published aggregate data and combined it with fictional examples to demonstrate one thing: with the same data, simply adjusting "how much weight each type of question carries" can move a certain "adoption rate" from 39.7% to 70.5%, a difference of about 31 percentage points. Changing the weights could even reverse the ranking of two systems. This is not a new experiment, and it can only show what is "possible in theory". But it points to something very important: **a visibility score is not something that exists objectively. It is "defined" jointly by the questions you choose, the weights and the scoring rules.**

### Follow-up questions: a question no one has measured yet

"Definition" also includes what you count as one unit of measurement. The common practice today is "one question, asked many times", but real people ask follow-up questions. One theoretical analysis proposed the possibility of "conversation capture": within one conversation, sources cited early on become more likely to be cited again later. The reasons come from both ends. On the AI's side, the earlier conversation affects what it searches for later. On the human side, the answer steers the person's next question toward that source. If this is true, single-round measurement captures only the direct effect and misses the part that builds up over several rounds, and the two ways of measuring might even rank different approaches in a different order.

However, this is only a theoretical model, and the numbers in the paper were calculated from parameters the authors set themselves. The direction is uncertain too: if people tend to follow up with "Is this true?", single-round measurement would actually overestimate the effect. There is a comparison you can run yourself: take the same set of multi-round questions, ask them once in a row within a single conversation and once with a new conversation for every round, and then compare how many times you are cited. This is a theoretical suggestion, and no one has reported results yet.

That "real people's needs are spread across several rounds" does, however, already have real data behind it. One study analysed 8,133 real multi-round English conversations (in two datasets). In about half of the conversations, the last message left out conditions stated earlier: 50.3% and 44.8% in the two datasets respectively. Only about a quarter of last messages contained all the conditions. Once a conversation reached 5 rounds or more, about 70% of the conditions remained only in earlier rounds. So asking one fixed question repeatedly measures only the answer to "this one sentence", which is not the same as the user's real, complete need within a conversation. Comparisons can be split into three cases: the full conversation, only what the user said in each round, and only the last message. As for whether single-round measurement overestimates or underestimates your visibility, no one has tested that yet.

### Baselines, phrasings and counting rules

"What you use as the baseline for comparison" is also part of the definition. Before elections in Europe and the United States, researchers audited the sources of real search engines and AI, and the AI part contained only about two hundred answers. For the same set of ChatGPT answers, mentions of one type of political party were 13.3 percentage points higher compared with "equal distribution" (significant), only 2.3 higher compared with media coverage volume (not significant), and 17.3 higher compared with the previous election result (significant). With the same data, switching the baseline turns the conclusion from "biased" into "not biased". The same goes for your brand's share of visibility: you need to state clearly what you are comparing it with, for example media share of voice or market share.

People in the industry who tested this themselves reported several specific situations (mostly data from a single team, and no one has independently verified them). The type of phrasing has a big effect. On a single engine, with each question run only once, "which is the best X" questions named the tested company 41% of the time and comparison questions 20% of the time, while for use-case questions of the form "what should I use for such-and-such", 40% named no vendor at all. If the mix of questions you track gradually drifts toward use-case questions, your mention rate will "fall" even though nothing has actually changed. Wording is just as sensitive. The same page might be cited for one precise query, yet add one word to the query and the whole list of sources changes. For the same query with the same wording, within a single day, a page might be cited in the early hours and gone by evening.

The same reports also pointed out several common traps. If your brand name is already in the question, the answer will almost certainly mention you, and that number is meaningless. Generating a fresh batch of questions each time you test, that is, rotating the question set, creates entirely fake declines, which are often explained afterwards with a story about "an algorithm update". Letting an AI model score your visibility is also a problem: with the same input, the score drifts by 10 to 15 points. And AI scoring may even measure the wrong thing. In one simulation study, four AI judges predicted which answer in a Q&A community real people liked most, and they got it right only 8.2% to 16.4% of the time, lower than the 25% from random guessing.

There are also several single observations from individual people in the industry, which can only be treated as clues. One person started counting the product's alternative names as "mentioned", and with the same 20 questions and the same four engines, the score went from 77 to 94. The world hadn't changed. Only the counting rule had. One person removed the samples where "the brand name is already in the question", and the share of answers in which cited sources were named fell from 10.9% to 8.9%, while for "compare X and Y" questions it fell from 15.8% to 8.1%. One person collected 60 questions buyers would ask, from real community discussions and "related questions", and found that in one round 13 of them, and in another round 23 of them, got AI answers that named no brand at all; tracking questions like these can never prove anything. And one person tested only with the most competitive core keywords and concluded "0 out of 10", but after adding more specific questions, the same website was cited.

## 5. "Mentioned", "cited" and "recommended" are three different things

"Appearing in an AI answer" has at least three meanings, and this chapter counts them separately. Being mentioned means your brand name appears in the text of the answer. Users will remember the name, but there may not be a link. Being cited means your page appears among the answer's sources or links. This may bring clicks, but the content of the answer may be recommending someone else. Being recommended means the answer treats you as a suggested choice, which is the closest to a business outcome.

The gaps between these three showed up clearly when researchers tested real AI search repeatedly. In a large-scale study of one Chinese-language AI search engine, only 8.3% of the brands that appeared in the cited material actually made it into the answer, and only 66% of the listed sources had their content actually written into the body of the answer. The ones that weren't used are silent citations.

Numbers from people in the industry point to the same thing. Someone in the industry tested this themselves (but no one has independently verified it): across 76 companies and about 1,140 questions, brands were mentioned in 44% of answers on average, but recommended in only 10%. In another set of about 26,400 answers about brands in competitive categories, a brand appeared in only about 16% of them, of which about 13% were cited and about 3% were only named without a link, with clear differences between engines. The median brand was at about 13%, and the average was pulled up by a few big brands. Someone else observed (a single observation) a newly created author identity, that is, a new entity, tracked every day for 99 days in a row. The engines got to know him better and better, but his recommendation rate stayed at zero from start to finish.

"Being cited doesn't mean being recommended, or even being mentioned" is a view that many people in the industry agree with, and of all the evidence in this chapter, it has the most supporters. But remember that "many people believe" does not mean "it is right".

### Before and after the answer, there are two more measures

Besides these three measures, there are two more, one before the answer and one after it.

```
Crawled (server logs) → Mentioned / cited / recommended (asking questions repeatedly) → Clicked (referral traffic) → Converted (purchase, etc.)
     Leading indicator                   Intermediate indicator                        Outcome indicator
```

The leading indicator is whether AI's crawlers came to fetch your pages, which you can see in your website's server logs. The intermediate indicator is whether the answer mentions, cites or recommends you. The outcome indicator is whether people clicked through and whether they bought.

Someone in the industry tested this themselves and found that tracking tools almost all measure only the middle stage, yet are often sold as covering all three. Server logs, meanwhile, offer clues about the other two stages, and changes show up in them earlier. In another repeated test with a control group, they also found that most AI assistants, when opening a link for a user, do not attach the information saying "where I came from" (which the industry calls the referrer), so these visits are recorded as "direct traffic". So **tools that look only at referral traffic will, by their very structure, always underestimate the traffic AI brings.**

## 6. How strong is this evidence?

Putting this chapter's conclusions side by side, the sources and strength of the evidence vary a great deal.

The two strongest both come from systematic measurement on real engines. "About two-thirds of cited sources change every day, and the same holds for repeats within one day" rests on 45 days of daily measurement on real engines plus 10 repeats within one day, and its strength is strong; its scope is 4 engines, with data captured from the web interfaces. "The programming interface and the web interface overlap in sources by only 12% to 15%" rests on a one-to-one comparison of the interface and the programming interface on real engines, and its strength is also strong, but it covers only product recommendation questions.

Several findings are of medium strength. "A single test has a margin of error 3 to 7 percentage points wide" comes from repeated measurement through programming interfaces on real engines; the authors are a visibility service provider, and there were only 3 topics. "There is no universal fixed sample size; you should judge while collecting" comes from 30 "platform × topic" combinations on real engines, and the authors are again a service provider. "The app and the web version overlap by 0.19 to 0.51" comes from 8 interfaces on real engines, involves only Chinese-language engines, and the authors are also a service provider. "Users' conditions are spread across several rounds, and the last message often leaves out earlier conditions" comes from 8,133 real conversation records; its strength is medium and it is descriptive evidence; it did not test AI's answers, and the conditions were identified with keyword rules. "Mentioned, cited and recommended are separate" comes from many industry parties testing on their own plus broad consensus; its strength is medium, but each team defines the terms differently, and no one has independently verified it.

"Adding breadth (languages) reduces error more than adding repetitions, by about 15 times" comes from programming interfaces on real engines plus estimates from a statistical model, and its strength is medium to weak, because the authors are a service provider, it measured sentiment rather than mention rate, and the margin of error has not yet been calculated. The two theoretical conclusions are both weak. "Changing the weights can make scores differ by 31 percentage points" is a theoretical analysis that recalculated existing data, and only shows what is possible in theory. "With follow-up questions, sources cited early may keep being cited" comes from a theoretical model, and likewise only shows what is possible in theory; neither its direction nor its size has been measured. As for the relationship between visibility and traffic or revenue, **there is currently no evidence**: no study has shown that GEO visibility reliably brings traffic or conversions.

Two more reminders. The first is conflict of interest. A considerable share of the measurement studies cited in this chapter come from companies that provide AI visibility services, and much of the industry data also comes from people who build tracking tools themselves. Their criticism of measurement methods is often correct, but their conclusions naturally lean toward "you need more, and more expensive, measurement". The second is that the biggest gap is in the final stage. All the strong evidence today is about "how to measure without fooling yourself". None of it says "how much business a rise in measured visibility will bring".

## 7. Seven questions still being debated

### How many runs, and which window to test

The first debate is how many times to run each question, and the views differ a lot. One study, based on 45 days of repeated testing on real engines, recommends at least 7 runs per day, or 8 if you want to look at sources, viewed on a rolling 2 to 4 week basis. Another study, based on 30 combinations on real engines, holds that there is no fixed number, that you should judge while collecting, and that engines with fewer citations need more. The variance breakdown done on real engines (looking only at sentiment results) holds that beyond 5 repetitions, extra runs add little value, and the budget should go to more languages, models and phrasings instead. Views from people in the industry are even more scattered. One person who tested this themselves (repeatedly, with a control) argues for 3 runs, counting a hit only when it "appears in 2 out of 3". Another who tested it themselves found that for the top positions, returns diminish after 5 to 10 runs, while the long tail further down needs more. Still others, based on their own tests plus community consensus, argue for 10 or more runs, or even 20 or more.

These views don't really conflict. The research stresses total sample size and how it is allocated. When people in the industry say "3 runs", they usually mean on a limited budget, combined with many questions and accumulated over several weeks. **The only thing that is truly wrong is "1 run".**

The second debate is whether to test the programming interface or the product interface. Those who favour the programming interface argue that it can be automated, can be pinned to a fixed model version, and isn't disturbed by personal memory. Data from one person in the industry shows that searching with their own account gave results that "looked great", while searching in a clean conversation after logging out was clearly worse. Another person in the industry used 20 clean accounts to retest someone else's claim of "cited within a week", and the brand did not appear at all. Those who favour the product interface point out that research shows the programming interface and the product interface overlap in sources by only 12% to 15%, and that users see the product interface. One person in the industry also reported that for the same query, the product interface cited the platform's own content about 50% of the time, but 30 runs through the programming interface produced not a single such citation.

The compromise, widely recommended in the industry, is to choose one window to observe through and keep it fixed. Otherwise what your trend line measures is really "a change of window", not a change in visibility. If you use the programming interface, regularly check a small sample through the product interface as well.

### Which is more stable

The third debate is which engine is the most stable, and the industry data contradicts itself. One person measured an engine whose sources were about 90% the same one day apart; another team re-ran three models five times each and found overlaps of about 65%, 55% and 35%. One person said a certain engine had the highest share of "appearing only once in three runs" (43%), while someone else said the same engine was the most stable for brand mentions. On the research side, one of three engines had the highest median overlap (0.50).

Only two points are broadly agreed: engines really do differ in stability, and "whether sources are stable" and "whether brands are stable" are two separate things. Under different question types, times and settings, the ranking of which engine is most stable changes. So don't treat any engine's stability as fixed.

The fourth debate is related to the previous one: are brands more stable, or are sources? Research found that mentions at the brand level are more stable than at the URL level. One industry test supports this: the same question was run on the same engine for 30 days in a row, and the sources changed often, but two brands were recommended in 28 and 26 of the 30 runs respectively. Another industry test came away with the opposite impression, finding that how a brand is described is less stable than the citations. The same brand was the top recommendation in one round and only mentioned in passing in the next, while the citations actually overlapped by 40% to 80% across five runs. The instability was concentrated in positions 4 to 10, which is exactly where most brands fall.

One possible explanation is that "whether you are mentioned" is fairly stable, while "how you are described and what place you rank" is less stable. Reports should keep these two things separate.

### Can it be measured accurately, and can the numbers be compared?

The fifth debate is the most fundamental: can AI visibility be measured at all? On the sceptical side, many people in the industry believe that AI visibility cannot currently be measured reliably. One person had ten people each open a private window and ask the same questions on five platforms, and every person got different answers and citations. On the side that thinks it can be measured, one person in the industry fixed 16 questions and tested once a day. Over 28 runs, the daily fluctuation (standard deviation) was 2.8 percentage points, while the citation rates of three engines were 27%, 9% and 0%, gaps far larger than that fluctuation, so the gaps are real. This side's view is that repeated sampling is the standard way to measure a random system, and that the key lies in the number of repetitions and the margin of error. The two sides are really saying the same thing: **a single snapshot measures nothing; the distribution you get from repeated sampling can be measured**, though cost and precision are limited.

The sixth debate is whether numbers from different tools can be compared with each other. One person in the industry observed that the same domain's AI citation count differed by about 8 times between two tools. He guessed that the two count different scopes: one counts every appearance in every re-run, while the other only samples its own database. Many people in the industry believe raw numbers cannot be compared directly across tools. But there are counterexamples. One person in the industry used three commercial tracking tools to track the same 5 brands, and the three tools gave exactly the same brand ranking and exactly the same top 5 cited domains. However, the overlap of the top cited URLs was only 55% and 64% depending on the platform, and only 14% on one platform. So a rough relative ranking may agree, but at the URL level, or when you look at absolute numbers, the differences are large.

The seventh debate is whether local businesses are simply "either you're there or you're not". One person in the industry holds that whether a local service business appears in AI is basically a stable "yes or no", depending on whether AI can recognise the shop as a clear entity, and that the run-to-run fluctuations tools measure come from measuring the wrong thing. But the industry test mentioned earlier (repeated, with control groups) showed that when the same batch of local queries, with unchanged wording, was run twice, one engine still replaced about a third of the businesses it recommended; only the businesses that appeared most widely on other websites showed up every time. The former is a single viewpoint, the latter has repeated measurements, and for now the latter is better supported.

## 8. Seven real cases

### When the number drops, you may not have dropped

The first case comes from a team that publishes its data. Every week they measured 40 fixed buyer questions on 7 AI answer engines. One week, the total number of cited domains fell from 851 to 790, which looked like a drop in visibility. But broken down by engine, one engine had fallen from 225 to 73, while most of the others had actually risen. It turned out that engine's programming interface quota had run out partway through the measurement, and only 11 of the 40 questions were answered. The whole "drop" was caused by a failure in the measuring tool.

Afterwards, they built a "failure taxonomy" covering timeouts, rate limiting, AI refusals, wrong questions asked, answers not captured, and so on. Two more problems came up while building it. They had first written the classification code based on error messages they imagined, and when they ran it on real errors, 38 of 69 (55%) were filed under "other". They also discovered that another engine's field had been sending only truncated questions all along, so they relabelled all 80 rows of data published in the first two weeks as "wrong question asked". Yet another engine dropped by 37 that week, and they openly admitted they couldn't tell whether it was because they had changed their own code or because the engine itself had changed. This case shows that **failures must not be recorded as "not mentioned", and every number needs its denominator (how many times it was asked) and how many runs failed.**

The second case is about model updates. A tracking team kept a fixed set of questions and recorded the cited sources over a long period. One engine had cited a certain large community forum 9 times within a week, and then not once in the next 64 consecutive runs. Every brand on the dashboard moved at the same time, and nobody had changed anything. So they argue for setting aside about a quarter of the questions as a control group that gets "no optimisation at all". If these untouched questions move too, then the engine has changed, and it is neither to your credit nor your fault. Another person in the industry observed something similar: for a fixed set of 5 peer brands, the overall score rose from 0.226 to 0.285 within one week, with the measurement settings completely unchanged. Before-and-after comparisons must have a control group, otherwise model updates will be mistaken for the effect of optimisation.

### When tool numbers don't match reality

In the third case, a person in the industry compared the AI crawler records in his website's server logs with the results of asking questions repeatedly. He saw that one engine's search crawler had gone from fetching 548 times a day in mid-August to 189 times a day recently, and that the visits representing "a real person opening a link during a conversation" had fallen from 230 a day to 48. The search crawlers of two other engines had fetched zero times every day for a whole month. His conclusion was that any tool saying he was "visible on those two engines" was sampling something that could not possibly be true. With zero crawler fetches, there can be no citations based on online search, so "whether you are crawled" is the earliest leading indicator.

The fourth case is a project. The team turned about 1,000 target keywords into about 20,000 natural-language questions and used a tracking dashboard to measure the brand's coverage on one engine. The dashboard showed 45% brand coverage, but every time the client spot-checked, they couldn't see their own brand. The window differences mentioned earlier under "where you look", including programming interface versus product interface, account status and location, could all cause this kind of gap. This case itself never found the exact cause, but it shows that "the tool's numbers" and "what buyers actually see" must be checked against each other regularly.

### Measure the noise first, then look at changes

The fifth case is the person in the industry mentioned earlier in the debates. He fixed 16 questions for his own website, never changed them from the first day, and ran them once a day. Over 28 runs, the daily fluctuation (standard deviation) was 2.8 percentage points. On the same day, the citation rates of three engines were 27%, 9% and 0%, gaps far larger than the noise, so they can be trusted. The difference between two model tiers of the same engine (17 versus 5) was close to the noise range, so he didn't interpret it. Only once you know what the noise looks like can you tell which changes are worth paying attention to.

The sixth case is a ten-day before-and-after test. A small product did not appear in 7 of 8 buyer questions. The team identified the questions where "AI named competitors but not us", published two comparison articles and one page of technical documentation aimed at those questions, and rewrote the project description. Ten days later, the number of questions where it appeared had risen from 1 to 5, and three of the four engines had corrected their earlier misclassification of the product's category. This is data from someone in the industry testing on their own (repeated, with a control), and the author builds measurement tools. It demonstrates a complete cycle: find the questions where you are absent, make changes, and measure again. But the sample is only 8 questions, and the author himself cautions that each question should be run more than once before drawing conclusions.

Related to this case is a compilation. One person in the industry compiled 26 public "visibility improvement" cases. 19 of them defined a question set, and 16 used repeated measurement rather than a single screenshot. Yet not one clearly isolated "which practice actually worked"; most changed content, structured data, PR and third-party mentions all at once. Public cases are good for generating ideas, but not for estimating the effect of any single practice.

### A search engine's official AI exposure report

The seventh case comes from a chocolate database website. It began seeing a "generative AI performance" report in Google Search Console: from mid-May, a cumulative 9,093 generative AI impressions, with daily impressions growing from 30 to 40 to 200 to 280, and 579 URLs appearing in total. Another person in the industry had 116,061 AI impressions on their website over 53 days.

This report has its limits too. Many people in the industry point out that it lacks data on "what users asked" and "whether they clicked". One person in the industry observed that about two-thirds of the long-question impressions in their own report were actually other people running tracking probes by "asking questions while pretending to be a certain persona". These impressions get zero clicks and will distort your judgement of real demand. Bing Webmaster Tools also provides AI citation data, and one person in the industry reported that a new website only two months old had about 865 citations within seven days, though with large daily fluctuations. Official reports are among the few data sources that "don't come from sampling", but they cover only the provider's own engine, and the items you can see are limited.

## 9. Do it yourself: a credible measurement process

Each of the 15 steps below states in brackets where its evidence comes from.

1. Measure a baseline first, then make changes. Measure at least twice before making changes, ideally across two or more days; otherwise you can't tell whether a change came from what you did or from the drift that happens every day anyway. (Many people in the industry believe this, and people in the industry have tested it themselves.)
2. Questions should come from what real buyers say: find them in sales calls, customer service records, customer reviews and the query reports in search engine webmaster tools, and don't put your own brand name in the questions. (People in the industry tested this themselves; community consensus.)
3. Fix the question set and label it with a version. Add new questions as "a new column"; don't replace old questions or change their wording. (People in the industry tested this themselves.)
4. Screen the questions first. Do a trial run, move questions that "never name any brand" to one side, and leave them out of the main score. Then look at trends by grouping questions by phrasing type: "which is the best" questions, comparison questions, alternatives questions and use-case questions. (People in the industry tested this themselves; there are also individual observations.)
5. Ask each question many times, and include the sample size when reporting the mention rate. Research recommends at least 7 to 8 runs per question per day; on a limited budget, at least 3, counted by a "2 out of 3" majority rule. (Researchers tested real AI search repeatedly; people in the industry tested this themselves, repeatedly, with controls.)
6. Spend the budget on breadth. Multiple engines, multiple languages, multiple regions and multiple phrasings work better than running the same question dozens of times. (Researchers tested real AI search; but only sentiment was measured, and the authors are a service provider.)
7. Report each engine, language and region separately; don't blend them into one average score. (Researchers tested real AI search repeatedly; people in the industry tested this themselves.)
8. Fix one observation window and record the settings: programming interface or product interface, whether search is turned on, the model version, the region, and whether you are logged in. If you use the programming interface, regularly spot-check through the product interface in a clean conversation. (Researchers tested real AI search repeatedly; people in the industry tested this themselves.)
9. Record every run, including whether there was an answer, whether it went to look things up, the failure category, whether you were mentioned, which URLs were cited, whether you were recommended, and in what position. Failures and gaps do not count as "not mentioned". (People in the industry tested this themselves, repeatedly, with controls.)
10. Fix the definition of "a hit". Whether brand aliases and product names count, and whether to exclude cases where the brand name was already in the question and the answer merely repeats it: once these are decided, don't change them; if you do change them, rebuild the baseline. (Observations from individual people in the industry.)
11. Set up a control group. Leave about a quarter of the questions without any optimisation, and also track a group of peer brands you are not working for. (People in the industry tested this themselves, repeatedly, with controls; there are also individual observations.)
12. Look at trends, not single weeks. Research recommends viewing on a rolling 2 to 4 week window, and people in the industry mostly use 4 weeks or more. One person in the industry has a rule of thumb: treat a single-week change within 15% as noise at first, and take it seriously only if it repeats for two weeks in a row; this is just personal experience, not a law. (Researchers tested real AI search repeatedly; people in the industry tested this themselves.)
13. To judge whether a change is real, first ask three questions: are several platforms moving at the same time, did the number of cited URLs move with it, and does the timing line up with what you did? (People in the industry tested this themselves.)
14. Record the cited URLs, not just "whether you appeared". The list of cited sources tells you which pages to go after for exposure, but it only shows "an association", not that "these sources caused it". (People in the industry tested this themselves.)
15. Fill in both ends. Use server logs to see whether AI crawlers come to fetch your pages; use official webmaster tools (such as Google Search Console and Bing Webmaster Tools) to see AI impressions; and split traffic into two buckets, "confirmed from AI" and "inferred as possibly from AI". (People in the industry tested this themselves.)

### Costs, and the minimum viable version

For what it costs to do this yourself, you can refer to figures from people in the industry who tested it themselves, but prices change. Building it yourself with a search programming interface that returns citations costs about half a US cent per query, so one round of 100 queries is about US$0.5. About 300 queries, 4 engines, run daily, costs about US$30 a month in programming interface fees. 600 runs a day on a single engine costs about US$1.6. There is also a person in the industry whose self-written program crashed at about 50 queries and cost about US$200. Doing it yourself isn't necessarily cheaper, but the advantage is that the method is entirely in your hands.

If you just want to get started, one approach from a person in the industry is to fix 5 questions real customers would ask, ask each one once on each engine on the same day every week, and count only "how many of the 5 questions mention us". The sample is small, but the advantage is that the client can sit beside you and reproduce it themselves. A better approach is to ask each question 3 times.

## 10. How to evaluate tracking tools and GEO service providers

One person in the industry, who builds tools himself, proposed a very useful overall principle: **does this tool make claims that "you could catch it being wrong about"?** If it only says "you appeared", you have no way of checking whether it is right. But if it says "this answer cited your pricing page and a competitor's comparison page", you can open them and check for yourself.

Following this principle, you can ask a tool or service provider the 12 questions below. Each one is followed by why to ask it and where the evidence comes from.

1. How many times is each question run? Are the sample size and margin of error reported? About a third of a single run is noise. (Research, plus people in the industry testing on their own.)
2. Does it test the programming interface (with search on or off) or the product interface? The overlap between windows is only 12% to 15%. (Research.)
3. Who sets the question set? Can you set it yourself and keep it fixed? Default question banks often lean toward other industries, and contain many questions "nobody can win". (People in the industry testing on their own.)
4. Can you see the raw answers and the cited URLs? Only numbers you can check have value. (People in the industry testing on their own, repeatedly, with controls.)
5. Is each engine reported separately? Averaging them together confuses "really absent" with "this engine doesn't list sources anyway". (People in the industry testing on their own.)
6. How are failures, gaps and cases where it didn't look anything up handled? What is the denominator? Recording failures as zero creates fake declines. (People in the industry testing on their own.)
7. Can it tell "a model update" apart from "your changes"? Is there a control group? A model update makes the whole category move together. (People in the industry testing on their own.)
8. Is the score calculated with fixed rules, or scored by an AI model? With model scoring, the same input can drift by 10 to 15 points. (People in the industry testing on their own.)
9. Does it really query every engine it claims to cover? One person in the industry read the code of an open-source tracking tool: the documentation claimed it covered multiple engines, but the code contained the interface for only one engine and three fixed questions. (People in the industry testing on their own.)
10. Where does its "question search volume" data come from? One person in the industry tested an interface that provides AI keyword data: it reported zero search volume for a batch of niche queries, yet when asked by hand, the platform answered every time. The source and representativeness of this kind of data cannot be verified. (People in the industry testing on their own.)
11. How does traffic attribution handle visits that "carry no source information"? Counting only referral traffic will, by its structure, underestimate. (People in the industry testing on their own, repeatedly, with controls.)
12. Do its numbers line up with your business data? The tool's charts should match what you hear on sales calls. (People in the industry testing on their own, repeatedly, with controls.)

When evaluating a GEO service provider, many people in the industry believe you should ask them to explain their specific measurement method, show results that can be verified, and explain how those results relate to business outcomes. You can add two more: before charging you, can they first show you a baseline built to the standards above, and can they map changes and results to a specific week?

There are some warning signs, and if any one of them appears, press for answers. The first is a single "AI visibility score" that blends all engines together, or claims like "you rank number X in AI". The second is percentages with no sample size. One person in the industry observed a report that printed "only 1 mention in total" as "1% share of voice", and that also gave unexplainable fields such as "100% purchase likelihood" from a sample of 15 questions over 14 days. Other warning signs include giving only screenshots, or listing only the questions without the raw answers; reporting long-term trends with a question set that keeps changing; using a single before-and-after comparison to prove "our optimisation worked"; and the same domain's numbers differing several times over between tools without anyone being able to explain how each one was calculated.

Why do tool numbers jump around? One person in the industry tested several tools in a row and found that the numbers jumped sharply every week (60%, 35%, 50%). He asked the same question by hand 10 times in a row, and the answer was different every time. The problem was not a bug in the tools. It was that most tools run each question only once, because running it ten times would also make the programming interface costs ten times higher.

## Key points of this chapter

Visibility is a probability distribution, not a ranking. On real AI search, about two-thirds of cited sources change every day, and the same holds for repeats within one day, so a single snapshot has no value as evidence. When reporting a mention rate, always include the sample size and margin of error: for 4 out of 10, the true range is about 12% to 74%.

Spend the budget on breadth. More languages, more engines and more phrasings reduce error better than running the same question over and over. There is no fixed answer for how large a sample you need, and engines with fewer citations need more. Different windows can't stand in for one another either: the programming interface and the product interface, the app and the web, logged in and logged out, different regions and languages all see different things, so choose one window, keep it fixed and record the settings.

Scores are defined. The question set, the weights, the phrasing types and the rules for "a hit" can all change the numbers dramatically, so fix them, and if you change them, rebuild the baseline. Count mentioned, cited and recommended separately, then add the two ends, crawling and traffic: being cited is not the same as being recommended, whether you are crawled is the leading indicator, and traffic is structurally underestimated. Without a control group you can't tell your changes apart from model updates, so keep some questions unoptimised, plus a group of peer brands, as a benchmark.

When evaluating tools and service providers, trust only numbers that can be checked: you need to be able to see the raw answers, the cited URLs, the denominator, how failures are handled and how many runs were done. No study so far has shown that visibility reliably turns into traffic or revenue; anyone who promises this needs to show their own data.

## Remember in one sentence

**Every AI answer is one roll of the dice: don't look at what place you rank in one roll; look at how many times you appear after many rolls on a fixed set of questions.**

## What you can do tomorrow

1. Write down a set of questions real buyers would ask, finding them in sales calls, customer service records, reviews and the query reports in webmaster tools, and don't put your own brand name in the questions. Then fix this list and label it with a version; from now on, only add to it, never rewrite it.
2. Do a trial run first, screen out questions that "never name any brand", then group the rest by type: which is the best, comparison, alternatives, use case.
3. Measure a baseline before making changes, at least twice, and across two or more days.
4. Ask each question at least 3 times and count by "2 out of 3"; if the budget allows, follow the research recommendation of 7 to 8 runs per question per day. In reports, always state "how many times it was asked and how many times you appeared".
5. Spend the budget on breadth, covering multiple engines, languages, regions and phrasings, and report each separately; don't blend them into one average score.
6. Choose one observation window and write down the settings, including programming interface or product interface, whether search is on, the model version, the region, and whether you are logged in. If you use the programming interface, regularly spot-check through the product interface in a clean conversation.
7. For every run, record whether there was an answer, whether it went to look things up, the failure category, whether you were mentioned, which URLs were cited, whether you were recommended, and the position. Failures do not count as "not mentioned".
8. Write down the rules for "a hit", for example whether aliases count and whether to exclude questions that already contain the brand name; once decided, don't change them, and if you do, rebuild the baseline.
9. Keep about a quarter of the questions as a control group with no optimisation, and also track a group of peer brands you are not working for.
10. Look at results as trends over 2 to 4 weeks or more, not single weeks. When you see a change, ask three questions: are several platforms moving together, did the number of cited URLs move with it, and does the timing line up with what you did?
11. Record the cited URLs and treat them as clues to "where to go after exposure", but not as proof of cause and effect.
12. Open your server logs and see whether AI crawlers are coming to fetch your website. With zero crawler fetches, there can be no citations based on online search.
13. Open Google Search Console and Bing Webmaster Tools to look at AI impressions and citation data, remembering that they lack query and click information and may include other people's tracking probes.
14. Split traffic into two buckets: "confirmed from AI" and "inferred as possibly from AI".
15. If your budget is very small, start with the minimum viable version: 5 questions, the same day every week, asked once on each engine (ideally 3 times), counting only "how many of the 5 questions mention us".
16. Take the 12 questions listed in this chapter for evaluating tools and ask them of your tool or service provider, and ask them to give you a baseline first and to map results to specific weeks.
17. Spot-check regularly yourself to confirm that the tool's numbers match what buyers actually see and what you hear on sales calls.

## Stop doing this

**Stop using one question and one screenshot to prove you "got recommended" or "disappeared".** Likewise, don't check your own visibility with your own logged-in account, and don't count results where "the brand name was already in the question" towards visibility.

Changing the wording of questions, replacing questions or changing the counting rules during tracking while continuing to draw the same trend line also needs to stop. Don't record programming interface failures, rate limiting or missing answers as "not mentioned".

Don't add up or directly compare raw citation counts from different engines, because the number of citations per answer differs several times over between engines. And don't treat the list of cited sources as proof of cause and effect.

### Practices that are already out of date

Treating AI answers as a search results page and tracking "what place you rank" is out of date. An answer is a distribution, and the list and its order change almost every time. Running each question once a week and plotting it as a trend chart is also out of date, because the noise from a single run is larger than the effect of most changes.

A one-off "AI visibility audit" is not enough either. An audit is just a snapshot, and models, competitors and cited sources change within a few weeks. Someone in the industry tested this themselves: a brand's visibility score held at the same value for 47 days in a row, while AI's purchase recommendations had long since shifted to a competitor.

Measuring GEO by traffic alone is also an out-of-date practice. Being named without being clicked leaves no record at all, and visits that AI brings are often recorded as direct traffic.

## What is still uncertain

**Can visibility bring in business?** There is currently no evidence. No study has shown that GEO visibility reliably brings traffic or conversions; all the strong evidence is only about "how to measure without fooling yourself".

**How many times should each question be run?** There is no consensus. Some argue for 3, others for 20 or more; research says to look at total sample size and judge while collecting. The only thing certainly wrong is "1".

**Is adding breadth really 15 times more effective than adding repetitions?** The direction is credible, but the number comes from a service provider, it measured sentiment rather than mention rate, and the margin of error has not yet been calculated.

**Should you test the programming interface or the product interface?** Both sides have a point; the current compromise is to fix one window and spot-check with the other.

**Which engine is the most stable?** The data from different parties contradicts itself, and the ranking changes with question type, time and settings.

**Are brands more stable, or are sources?** "Whether you are mentioned" may be more stable, while "how you are described and what place you rank" may be less stable, but there is no firm conclusion yet.

**Can AI visibility actually be measured accurately?** A single snapshot can't measure it accurately; repeated sampling can measure it, but cost and precision are limited.

**Can numbers from different tools be compared?** A rough ranking may agree, but URLs and absolute numbers differ greatly, and how each tool calculates is often not transparent.

**For local businesses, is it simply "there or not there"?** Current evidence from repeated measurement shows there is still fluctuation, but only one party has done the measuring.

**Is it true that changing the weights makes scores differ by 31 percentage points?** This is only possible in theory, and no real experiment has confirmed it yet.

**How should conflicts of interest be viewed?** Much of the measurement research and industry data in this chapter comes from people who provide visibility services or build tracking tools. Their criticism of methods is mostly reasonable, but their conclusions naturally lean toward "you need more, and more expensive, measurement".

**Can public "visibility improvement" cases be trusted?** So far, not one of them clearly shows which practice actually worked.
