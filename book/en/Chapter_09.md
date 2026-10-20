# Chapter 9 — AI Is Rolling Dice: How to Measure Without Fooling Yourself

## The meeting sparked by one screenshot

Imagine this scene (purely hypothetical):

The owner of an online coffee bean shop asks AI one morning: "Recommend a few online coffee bean shops that are good for beginners." The second shop in the answer is his own. He is delighted and sends the screenshot to the whole team.

That afternoon, An, someone on the team, asks the same question. This time they are not in the answer. An asks again, and this time they appear, in fifth place. One more time, and they are gone again.

Which time is the "real" one?

The answer: **every one of them is real, but no single one means anything on its own.**

This chapter makes just one point:

> **AI answers questions as if it were rolling dice. What you should count is not "what place we rank," but "out of many rolls, how many times we appear."**

The earlier chapters covered the seven gates an AI goes through to answer a question: whether to search, whether it can get in the door, whether it can find you, whether it picks you, whether it mentions you, whether it actually uses you, and whether people come over. They also covered where you can push at each gate.

This chapter is about how to **see** the results of those gates. If the measurement method itself is unreliable, none of the earlier effort can be verified.

This chapter answers five questions:

1. Why does asking AI once and taking a screenshot prove almost nothing?
2. How many repetitions, and how much coverage, does a credible AI visibility number need?
3. Are the answers you see through the programming interface, the web version and the mobile app the same? Which one should you test?
4. Why should "mentioned," "cited" and "recommended" be counted separately?
5. How do you judge whether the numbers from a tracking tool or a GEO service provider can be trusted?

---

## 1. Every question is just one roll of the dice

### Old search was like a notice board; today's AI is like rolling dice

A traditional search results page stays roughly fixed over a short period. You search once, a colleague searches again, and you see about the same order. So "we rank number 3" is a meaningful sentence.

AI search is not like that. For the same question, every time you ask, it has to go through several steps that change:

- **Breaking down the question**: The AI splits your question into several smaller questions and searches them separately (this is called **query fan-out**). The smaller questions may be different each time.
- **Pulling in material**: The search index and live results are themselves always changing, so the **shortlist (candidate set)** it pulls back may be different each time.
- **Writing the answer**: When the AI writes the answer, there is some randomness built in.

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

So every answer you see is just one sample drawn from a large pile of "possible answers." Rolling a 6 once does not mean this die always rolls 6.

That is why the right unit for measuring AI visibility is not "rank," but: **on a fixed set of questions, after asking many times, the proportion of times you appear**. This proportion is called the **mention rate**. That fixed set of questions is called the **prompt set**.

### What researchers saw on real AI search

Researchers tested real AI search repeatedly and found:

- **About two-thirds of sources change every day.** Researchers measured 4 AI search engines every day for 45 consecutive days. They compared how much the cited sources overlapped between neighbouring days, and the overlap was only 0.34 to 0.42 (1 means exactly the same, 0 means completely different). In other words, about two-thirds of the sources change every day.
- **The same holds within a single day.** Asking the same question 10 times within one day, the overlap of sources was 0.32 to 0.43, about the same as across days. This means the change mostly comes from **the randomness of each individual question**, not from "today's web being different from yesterday's."
- **Some engines often list no sources at all.** For one of the engines, 57.8% of answers cited no sources at all.
- **Another study saw similar results.** Researchers ran the same query repeatedly on three engines and compared the overlap of cited domains (taking the median): about 0.29 to 0.31 for one engine, 0.33 to 0.40 for another, and even the most stable was only 0.50.
- **Even for frequently cited sites, the numbers are imprecise.** Even for domains that are cited very often, the "citation share" from a single test has a margin of error (the 95% confidence range) as wide as 3 to 7 percentage points. Many apparent "gaps" between domains actually fall within the noise.

### People in the industry, testing on their own, saw the same direction

Someone in the industry tested this themselves, with repeated tests and control groups (but no one has independently verified it), and the results point the same way as the research:

- Across 197 websites in the same industry and three engines, each question was run three times. 32% of citations appeared in only one of the three runs.
- When the same question was run twice within 24 hours, the brand recommended in first place was different 48.5% of the time.
- The same batch of 45 local-service questions, worded exactly the same, each time in a brand-new conversation, was run twice. For one of the engines, about a third of the recommended businesses changed.

### What does "appeared 4 times out of 10" actually mean?

Suppose you are a bit more careful and ask the same question 10 times, and your brand appears 4 times. You say: "Our mention rate is 40%."

It sounds scientific. But run the statistics, and with only 10 asks and 4 appearances, the true mention rate falls, with 95% confidence, somewhere between roughly 12% and 74%. That range is so wide it tells you almost nothing.

> **Any percentage that does not tell you "how many times it was asked" carries almost no information.**

A screenshot is even less. That is not evidence; it is one roll of the dice.

> **A closer look: What does "margin of error" mean?**
> In statistics it is called a "confidence interval." It means: based on how many times you asked and how many times you appeared, the range the true mention rate "very likely" falls within. The fewer times you ask, the wider the range. For 4 out of 10, the range is 12% to 74%; the only way to narrow it is to ask more, and ask more kinds of questions.

---

## 2. Rolling more times is not as good as rolling in different ways

### Asking more times is right, but it is not everything

"Run it a few more times" is right, but doing only that is not enough.

Researchers tested on real AI search, breaking down more than ten thousand answers about brands to find out where "the differences between answers" mainly came from:

- **Which language you ask in** is the biggest systematic source of difference, accounting for about 26.5% of the difference in individual answers. The brand itself accounts for only 1.5%.
- After asking the same question a 5th time, asking 5 more times barely reduces the error any further. But if instead you ask in 3 more languages, the error drops by about 15 times as much.
- Looking at just one answer, the reliability of telling "which brand is better" is only about 0.01, practically zero.
- **Brands are more stable than URLs.** Looking at "whether a brand is mentioned," the overlap between neighbouring days is about 0.45 to 0.59; looking at "which URLs are cited," it is only 0.34 to 0.42.

This study comes with caveats: the authors themselves provide visibility services; what it measured was the AI's sentiment toward brands (liking or disliking), not the mention rate; and its margins of error have not yet been calculated. So the evidence is weak, but the direction is worth considering:

> **Rather than rolling the same question a hundred times, use different dice and roll on different tables.**

Changing engines, languages, regions and phrasings gives you a clearer picture of the whole than asking the same sentence over and over.

### How many times should you ask? There is no fixed answer

There is no single fixed number for how many samples you need.

One study used 10 topics, 125 queries per topic, and 3 platforms. Their method was "collect while checking whether the ranking has settled; stop only once it stops changing" (this is called **sequential convergence**). The results:

- Most combinations settled after collecting 33 to 75 responses.
- But 3 combinations still had not settled after 125. All 3 came from the same engine.

What happens if you instead stop at a fixed threshold (for example, "stop once the correlation between two successive rankings reaches 0.95 or above")?

- All 30 combinations reached the threshold, but only 19 held it afterwards.
- Looking only at whether the ranking was stable, the agreement between the order at the stopping point and the final result was as low as 0.364 in the worst case.
- If you add one more condition, requiring "the signal to be clearly larger than the noise," the worst case was 0.717.

What this means: **stopping just because "the ranking seems to have stopped moving" can easily lead to conclusions drawn too early.**

### The fewer citations an engine gives, the more times you need to ask

Engines differ a lot in how many citations each answer carries: two engines give about 15 to 50 citations per answer, while another gives only about 4 to 6.

The fewer the citations, the less information each question gives you, and the more questions you need to collect. Another study estimated that to narrow the margin of error for citation share to 5 percentage points, the three engines would need roughly 30 to 50, 90 to 100, and more than 150 queries respectively.

### "Asking again" and "asking another way" are two different things

- **Asking the same question again** is to smooth out randomness.
- **Asking another way** is to check "if it is phrased differently, are you still there?"

Many in the industry believe you need to do both; doing only one can still mislead you.

---

## 3. Where you look decides what you see

For the sentence "I saw myself in AI," first ask one question: **where did you see it?**

The same AI actually has several "windows":

| Window | How it is usually accessed | Known differences |
|---|---|---|
| Web version (the one ordinary people open in a browser) | Checked manually, or captured automatically with a browser | Source overlap with the programming interface is only 12.0% to 14.8% |
| Mobile app | Checked manually | Domain overlap with the same platform's web version is only 0.19 to 0.51; one platform, at the URL level, only 0.014 |
| Programming interface (the access point for engineers, called an API in the industry), with search on | Called automatically by a program | Some programming interfaces do not return certain social platform sources that the web version shows (for example X) |
| Programming interface, without search | Called automatically by a program | What you measure is the AI's memory, not what it found by searching online |
| Your own logged-in account | Personal use | Affected by your past conversations and what it remembers about you |

The first three rows of the table are the results of researchers testing real AI search repeatedly.

Another study that captured how ChatGPT's web version actually works (versions 5.2 to 5.5) adds: the web addresses cited through the programming interface matched the web version only 13% to 15% of the time; at the domain level it was better, 28% to 41%. So comparisons should be made at two levels, "web address" and "domain". **The thinking mode also changes search behaviour**: the fast mode mostly searches only one round, while the thinking mode averages more than 3 rounds and about 12 queries; the web version may also quietly switch to another model partway through the same conversation. So when measuring, record which mode was used and how high the thinking strength was.

The differences between engines are also large: faced with the same query, two mainstream engines share on average only 5.4% of domains; in 76.7% of comparisons, the two had no domains in common at all.

Many tracking tools ask automatically through the programming interface. But ordinary users see the web version or the app. **What the two sides see may be two different worlds.**

### A few more differences that are easy to overlook

Someone in the industry tested this themselves (mostly repeated tests with control groups, but no one has independently verified them), adding several layers that are easy to overlook:

**1. Whether this answer looked things up and listed sources.**

- In about 2,600 runs, one engine gave no sources at all in 282 of 615 runs (46%); all 359 runs of another engine included sources.
- In another 10-day record of 2,209 answers, one engine showed sources in only 59% of answers.

So "not appearing in the answer" means different things on different engines. Being absent from an answer that lists a dozen or so sources means you really were not chosen. Being absent from an answer that lists no sources at all tells you almost nothing.

**2. Whether an AI answer was triggered this time.**

For the same query, in the same location, searched repeatedly a few minutes apart, **AI Overviews** appeared only about 7 times out of 10. Searching once and seeing "no AI Overview" is not enough to draw a conclusion.

**3. Location and language.**

- Same model, same question, only telling it which country the user is in: a certain brand went from "not mentioned" to "named" in 5 out of 6 cases.
- Asking the same batch of questions in two languages, the cited sources overlapped by only 22%.

**4. Programming interface versus product interface.**

For the same query, in the product interface there was about a 50% chance of citing the platform's own content; run 30 times through the programming interface, it did not happen once.

---

## 4. Scores are "defined" by the rules

### Same data, a different calculation, a 31-point difference

One theoretical analysis recalculated already-published aggregate data, together with made-up examples, to demonstrate one thing: with the same batch of data, just by adjusting "how much weight each type of question gets," a certain "adoption rate" could go from 39.7% to 70.5%, a difference of about 31 percentage points. Change the weights, and it may even flip which of two systems comes out higher.

This is not a new experiment; it can only show that it is "possible in theory." But it points to something very important:

> **A visibility score is not something that exists objectively. It is "defined" jointly by the questions, weights and scoring rules you choose.**

### A question no one has measured yet: follow-up questions

"Defining" also includes one more thing: **what you use as the unit of one measurement.** The common practice today is "one question, asked many times". But real people ask follow-up questions one after another.

One theoretical analysis raises the possibility of "conversational capture": within the same conversation, a source cited early is more likely to be cited again later. There are two reasons:

- On the AI side: the earlier conversation affects what gets searched for later.
- On the human side: the answer leads the person's next question toward that source.

If this is really so, a measurement that asks only one round captures only the direct effect, not the part that builds up over many rounds; the two ways of measuring might even rank different approaches in a different order.

But this is only a theoretical model, and the numbers in the paper were calculated from parameters the authors set themselves. The direction is also uncertain: if people tend to follow up with "is this true?", a one-round measurement would instead overestimate the effect.

A comparison you can run yourself: take the same set of multi-round questions, ask them once in a row within the same conversation and once with a new conversation for each round, and compare how many times you are cited. This is a suggestion in theory; no one has reported results yet.

That real people's needs are spread across several rounds, however, already has real data behind it. One study analysed 8,133 real English multi-round conversations (two datasets):

- in about half of the conversations, the last sentence left out conditions stated earlier (50.3% and 44.8% in the two datasets);
- only about a quarter of last sentences included all the conditions;
- once a conversation reached 5 rounds or more, about 70% of the conditions remained only in earlier rounds.

So repeating a single fixed question measures the answer to "that one sentence", not the user's real, complete need in the conversation. When comparing, you can use three conditions: the full conversation, only what the user said in each round, and only the last sentence. Whether a one-round measurement overestimates or underestimates your visibility is something no one has measured yet.

### Several situations people in the industry found in their own tests

"What you compare against" is also part of the definition. Before elections in Europe and the US, researchers audited the sources of real search engines and AI (the AI part had only about two hundred answers): for the same batch of ChatGPT answers, mentions of one type of party were 13.3 percentage points higher than an "even split" (clear), only 2.3 higher than media coverage (not clear), and 17.3 higher than the previous election result (clear). The same data, with a different baseline, turns the conclusion from "biased" into "not biased". Your brand's share of visibility is the same: be clear about what you are comparing it with, for example media coverage or market share.

Someone in the industry tested this themselves and reported several specific situations (mostly data from a single team; no one has independently verified them):

- **Type of question.** On a single engine, with each question run only once: for "which is the best X" questions, 41% named the company being tested; for comparison questions it was 20%; and for "what should I use for such-and-such" use-case questions, 40% named no vendor at all. If the mix of questions you track slowly shifts toward use-case questions, the mention rate will "fall," though nothing has actually changed.
- **Wording.** The same page gets cited for one precise query; add one word to the query and the list of sources changes completely. The same query, the same wording, within one day: cited in the early hours, gone by evening.
- **Putting the brand name in the question.** If the question already contains your brand name, the answer will almost certainly mention you. That number is meaningless.
- **Rotating the question set.** Generating a new batch of questions each time you test creates "completely fake declines." Afterwards these are often paired with a story that "the algorithm was updated."
- **Letting AI do the scoring.** When an AI model scores visibility, the score drifts by 10 to 15 points for the same input. AI scoring can also measure the wrong thing: in a simulation study, four AI judges predicting which answer in a Q&A community real people liked most got it right only 8.2% to 16.4% of the time, lower than the 25% of random guessing.

### A few single observations (clues only)

The following are single observations from individual people in the industry and can only be treated as clues:

- **Whether aliases count.** After also counting product aliases as "mentioned," with the same 20 questions and the same four engines, the score went from 77 to 94. The world did not change; only the counting rule did.
- **Removing samples where "the brand name is already in the question."** After removing them, the proportion of cited sources that were named in the answer fell from 10.9% to 8.9%; for "X versus Y" questions, it fell from 15.8% to 8.1%.
- **For some questions, AI does not name any brand at all.** Someone collected 60 questions buyers would ask, from real community discussions and "related questions." In one round 13, and in another round 23, of the questions got AI answers that named no brand at all. Tracking questions like these can never prove anything.
- **Testing only the hottest terms.** Testing only with the most fiercely competitive core terms gave a conclusion of "0 out of 10 questions"; after adding more specific, niche questions, the same site was cited.

---

## 5. "Mentioned," "cited" and "recommended" are three different things

### Three different kinds of "appearing"

"Appearing in an AI answer" has at least three meanings. This chapter separates them:

| Measure | Meaning | Why it matters |
|---|---|---|
| Mentioned | Your brand name appears in the text of the answer | Users will remember the name, but there may be no link |
| **Cited** | Your page appears in the answer's sources or links | May bring clicks, but the content of the answer may be recommending someone else |
| Recommended | The answer treats you as a suggested choice | Closest to a business result |

Researchers tested real AI search repeatedly: in a large-scale study of one Chinese AI search engine, only 8.3% of brands that appeared in the cited material actually made it into the answer; of the sources listed, only 66% had their content actually written into the body of the answer. The ones that were not used are **silent citations**.

### Numbers from people in the industry

Someone in the industry tested this themselves (but no one has independently verified it):

- Across 76 companies and about 1,140 questions, brands were mentioned in an average of 44% of answers, but recommended in only 10%.
- In about 26,400 answers about brands in competitive categories, brands appeared only about 16% of the time; of that, about 13% were cited, and about 3% were only named without a link. There were clear differences between engines. The median brand was about 13%; the average was pulled up by a few big brands.
- Someone observed (a single observation) a newly created author identity (a new **entity**), tracked every day for 99 consecutive days. The engines came to know him better and better, but the recommendation rate stayed at zero from start to finish.

"Being cited does not mean being recommended, nor does it mean being mentioned" — this is a view many in the industry agree on, and among all the evidence in this chapter, it has the most supporters. But remember: "many people believe" is not the same as "it is right."

### Before and after the answer, there are two more measures

Beyond these three measures, there are two more, one before the answer and one after:

```
Crawled (server logs) → Mentioned / cited / recommended (asking questions repeatedly) → Clicked (referral traffic) → Conversion (purchases, etc.)
     Leading indicator                   Intermediate indicator                        Outcome indicator
```

- **Leading indicator**: Whether AI **crawlers** have come to fetch your pages. You can see this in your website's server logs.
- **Intermediate indicator**: Whether the answer mentions, cites or recommends you.
- **Outcome indicator**: Whether people clicked through, and whether they bought.

Someone in the industry tested this themselves and found:

- Tracking tools almost all measure only the middle segment, yet are often sold as if they covered all three.
- Server logs can provide clues for the other two segments, and changes show up there earlier.
- In addition (repeated tests with control groups): when most AI assistants open a link for a user, they do not include the "where I came from" information (called the referrer in the industry). These visits get recorded as "direct traffic." So tools that only look at referral traffic will, by their very structure, underestimate the traffic AI brings.

---

## 6. How strong is this evidence?

| Conclusion | Where the evidence comes from | Strength | Scope and limits |
|---|---|---|---|
| About two-thirds of cited sources change every day, and the same happens with repeats on the same day | Real engines, measured every day for 45 days, plus 10 repeats on the same day | Strong | 4 engines; captured from the web interface |
| A single test has a margin of error 3 to 7 percentage points wide | Real engines, repeated measurements through the programming interface | Medium | Authors are a visibility service provider; only 3 topics |
| There is no universal fixed sample size; judge while collecting | Real engines, 30 "platform × topic" combinations | Medium | Authors are a service provider |
| Adding breadth (languages) reduces error more than more repetition, by about 15 times | Real engine programming interfaces, plus estimates from a statistical model | Medium to weak | Authors are a service provider; measured sentiment, not mention rate; margin of error not yet calculated |
| Sources from the programming interface and the web interface overlap by only 12% to 15% | Real engines, one-to-one comparison of the interface and the programming interface | Strong | Product recommendation questions |
| App and web version overlap 0.19 to 0.51 | Real engines, 8 interfaces | Medium | Chinese engines; authors are a service provider |
| Changing the weights can make scores differ by 31 percentage points | Theoretical analysis, recalculated from existing data | Weak | Only shows it is possible in theory |
| During follow-up questions, a source cited early may keep being cited | Theoretical model | Weak | Only shows it is possible in theory; neither direction nor size has been measured |
| Users' conditions are spread over several rounds, and the last sentence often leaves out earlier ones | Real conversation records (8,133 conversations) | Moderate (descriptive) | AI's answers were not tested; conditions were found with keyword rules |
| Mentioned, cited and recommended are separate | Many in the industry testing on their own, plus broad consensus | Medium | Teams define them differently; no one has independently verified it |
| The link between visibility and traffic or revenue | None | **No evidence** | No research so far proves that GEO visibility reliably brings traffic or conversions |

Two reminders:

1. **Conflicts of interest.** A sizeable share of the measurement research cited in this chapter comes from companies that provide AI visibility services; much of the industry data also comes from people who build tracking tools themselves. Their criticisms of measurement methods are often right, but their conclusions naturally lean toward "you need more, and more expensive, measurement."
2. **The biggest gap is in the last segment.** All the strong evidence so far is about "how to measure without fooling yourself"; not a single piece is about "how much business a measured rise in visibility will bring."

---

## 7. Seven questions still being debated

### Debate 1: How many times should each question be run?

What different sides say:

| Claim | Basis |
|---|---|
| At least 7 times a day (8 if you want to look at sources), viewed on a rolling 2 to 4 weeks | Real engines, 45 days of repeated testing |
| No fixed number; judge while collecting; engines with fewer citations need more | Study of 30 combinations on real engines |
| Beyond 5 repeats, extra runs add little value; move the budget to more languages, models and phrasings | Breakdown of differences on real engines (sentiment results only) |
| 3 times, counting it only if "it appears in 2 out of 3" | People in the industry testing on their own (repeated, with controls) |
| For the top positions, returns diminish after 5 to 10 runs; the long tail further down needs more | People in the industry testing on their own |
| 10 or more times, even 20 or more | People in the industry testing on their own, plus community consensus |

These claims do not really conflict. The research emphasises **the total sample size and how it is allocated**. When people in the industry say "3 times," it is usually on a limited budget, combined with many questions and looked at together over several weeks.

**The only thing that is truly wrong is "once."**

### Debate 2: Test the programming interface, or the product interface?

- **Reasons for testing the programming interface**: It can be automated; you can fix the model version; it is not disturbed by personal memory. Data from someone in the industry showed that checking with their own account gave results that "looked great"; logged out, in a clean conversation, the results were clearly worse. Another person in the industry used 20 clean accounts to retest someone else's claim of "cited within a week," and the brand did not appear at all.
- **Reasons for testing the product interface**: Research shows that sources from the programming interface and the product interface overlap by only 12% to 15%, and users see the product interface. Someone in the industry also reported: for the same query, the product interface had about a 50% chance of citing the platform's own content, while 30 runs through the programming interface did not do so once.
- **The compromise**: People in the industry generally advise that you **choose one window to observe, and keep it fixed**. Otherwise what your trend line measures is really "a change of window," not a change in visibility. If you use the programming interface, regularly check a small sample in the product interface too.

### Debate 3: Which engine is the most stable?

The industry's data are inconsistent with each other:

- Someone found that for one engine, about 90% of sources were the same one day apart.
- Another team found that with three models each rerun five times, the overlap was about 65%, 55% and 35% respectively.
- Someone said one engine had the highest share of "appeared only once out of three" (43%); others said the same engine was the most stable for brand mentions.
- On the research side, one of three engines had the highest median overlap (0.50).

There are only two points of rough agreement: engines really do differ in stability; and "whether sources are stable" and "whether brands are stable" are not the same thing. Across different question types, times and settings, the order of which is most stable changes. Do not treat any engine's stability as fixed.

### Debate 4: Are brands more stable, or are sources?

- **Research**: Brand-level mentions are more stable than URL-level ones.
- **Industry tests supporting this**: The same question on the same engine, run for 30 days in a row: sources changed often, but two brands were recommended 28 and 26 times out of 30 respectively.
- **Industry tests against this**: **How** a brand is described is less stable than citations. The same brand was the top recommendation in one round and only mentioned in passing in the next; citations, by contrast, overlapped by 40% to 80% across five runs. The instability was concentrated in positions 4 to 10, which is exactly where most brands fall.

A possible explanation: "whether you are mentioned" is fairly stable; "how you are described and what place you rank" is less stable. Reports should keep these two things separate.

### Debate 5: Can AI visibility actually be measured?

- **The sceptical side**: Many in the industry believe AI visibility cannot currently be measured reliably. Someone also got ten people to each open an incognito window and ask the same questions on five platforms; each person got different answers and citations.
- **The side that believes it can be measured**: Someone in the industry fixed 16 questions and tested once a day. Over 28 runs, the day-to-day fluctuation (standard deviation) was 2.8 percentage points. The citation rates of three engines were 27%, 9% and 0%, gaps far larger than that fluctuation, so the gaps are real. The other view is: repeated sampling is the standard method for measuring a random system anyway; the key is the number of repeats and the margin of error.

The two sides are actually saying the same thing: **a single snapshot measures nothing; the distribution from repeated sampling can be measured**. It is just limited by cost and precision.

### Debate 6: Can numbers from different tools be compared with each other?

- Someone in the industry observed that the same domain's AI citation count differed by about 8 times between two tools. He guessed that the two count different scopes: one counts every appearance in every rerun, while the other only samples its own database. Many in the industry believe raw numbers cannot be compared directly across tools.
- **A counterexample**: Someone in the industry used three commercial tracking tools to track the same 5 brands. The brand order given by the three tools was exactly the same, and the top 5 cited domains were also exactly the same. But the overlap of the top cited URLs was only 55% and 64% depending on the platform, and only 14% for one platform.

In other words: **the rough relative order may agree; down at the URL level, or in absolute numbers, the differences are large.**

### Debate 7: For local businesses, is it simply "either you're there or you're not"?

Someone in the industry believes that whether a local service provider appears in AI is basically a stable "yes or no," depending on whether the AI can recognise the shop as a clear entity; the run-to-run fluctuation that tools measure comes from measuring the wrong thing.

But the industry test mentioned earlier (repeated, with control groups) showed: the same batch of local queries, with unchanged wording, run twice, and one engine still changed about a third of the businesses it recommended; only the businesses that appeared most widely on other websites showed up every time.

The former is a single viewpoint; the latter has repeated measurement. For now, the latter has more support.

---

## 8. Seven real cases

### Case 1: A "visibility drop" that was actually an unpaid bill

- **What they did**: A team measured every week on 7 AI answer engines, using 40 fixed, unchanging buyer questions, and published the data.
- **What they saw**: One week, the total number of cited domains fell from 851 to 790. Broken down by engine, one engine had dropped from 225 to 73, while most of the other engines had actually risen. The reason: that engine's programming interface quota ran out partway through the measurement, and only 11 of the 40 questions were answered. The entire "drop" was a measurement tool failure.
- **Afterwards**: They built a "failure classification" (timeout, rate-limited, AI refused to answer, wrong question asked, answer not captured, and so on). Along the way they found two more things:
  - They had first written the classification code based on the error messages they imagined, and when they ran it on real errors, 38 of 69 (55%) were put into "other."
  - Another engine's field had been sending only truncated questions all along. All 80 rows of data published in the first two weeks were relabelled as "asked the wrong question."
  - Yet another engine dropped by 37 that week, and they admitted frankly: they could not tell whether it was because they had changed their code, or because the engine itself had changed.
- **The lesson**: Failures cannot be recorded as "not mentioned." Every number should come with its denominator (how many times it was asked) and how many times it failed.

### Case 2: A model update, and the whole dashboard moves together

- **What they did**: A tracking team fixed a set of questions and recorded the cited sources over a long period.
- **What they saw**: One engine had cited a large community forum 9 times within a week, then did not cite it once across 64 consecutive runs. All the brands on the dashboard moved at the same time, and no one had changed anything.
- **What they did about it**: They argue for setting about a quarter of the questions aside as a "no optimisation at all" control group. If these untouched questions move too, then the engine has changed; it is not your achievement, nor your fault.
- Someone else in the industry observed something similar: for a fixed set of 5 peer brands, the overall score rose from 0.226 to 0.285 within a week, while the measurement settings had not changed at all.
- **The lesson**: Before-and-after comparisons must have a control group; otherwise a model update will be mistaken for the effect of optimisation.

### Case 3: Server logs exposed "you're visible on a certain engine"

- **What they did**: Someone in the industry compared the AI crawler records in their website's server logs side by side with the results of asking questions repeatedly.
- **What they saw**:
  - One engine's search crawler went from fetching 548 times a day in mid-August to 189 times a day recently.
  - The visit records that represent "a real person clicking a link in a conversation" fell from 230 a day to 48.
  - The search crawlers of two other engines fetched zero times a day for a whole month.
- **Conclusion**: Any tool saying he was "visible on those two engines" was sampling something that could not be true. With zero crawler fetches, there cannot be any citation based on searching online. So "whether you are crawled" is the earliest leading indicator.

### Case 4: The dashboard says 45%, but the client cannot find themselves

- **What they did**: A project rewrote about 1,000 target keywords into about 20,000 natural-language questions, and used a tracking dashboard to measure the brand's coverage on a certain engine.
- **What they saw**: The dashboard showed brand coverage of 45%. But every time the client spot-checked it themselves, they could not see their own brand.
- **Possible causes**: The window differences covered in Section 3 (programming interface versus product interface, account status, location) could all cause this kind of gap. This case itself did not find the exact cause. But it shows that **"the tool's numbers" and "what buyers actually see" must be checked against each other regularly.**

### Case 5: Fix 16 questions and first measure how big the noise is

- **What they did**: Someone in the industry fixed 16 questions for their own website, did not change them from day one, and ran them once a day.
- **What they saw**: Over 28 runs, the day-to-day fluctuation (standard deviation) was 2.8 percentage points. On the same day, the citation rates of three engines were 27%, 9% and 0%, gaps far larger than the noise, which can be trusted. The difference between two model tiers of the same engine (17 versus 5) was close to the noise range, so he did not interpret it.
- **The lesson**: Only once you know what the noise looks like can you tell which changes are worth paying attention to.

### Case 6: A ten-day before-and-after test

- **What they did**: A small product did not appear for 7 out of 8 buyer questions. The team identified the questions where "AI named competitors but not us," and for those questions published two comparison articles and one page of technical documentation, and rewrote the project description.
- **What they saw**: Ten days later, the number of questions where they appeared rose from 1 to 5. Of the four engines, three corrected their earlier wrong classification of the product category.
- **How to read it**: This is data from someone in the industry who tested it themselves (repeated, with controls), and the author builds measurement tools. It demonstrates a complete loop: "find the questions where you are absent → make changes → measure again." But the sample was only 8 questions, and the author himself cautioned that each question should be run more than once before drawing conclusions.
- **Another review**: Someone in the industry reviewed 26 public "visibility improvement" cases. Of these, 19 defined a question set, and 16 used repeated measurement rather than a single screenshot. But **not one clearly isolated "which practice actually worked"**; most changed content, structured data, PR and third-party mentions all at once. Public cases are good for generating ideas, but not for estimating the effect of any single practice.

### Case 7: A search engine's official AI exposure report

- **What they did**: A chocolate database website started seeing a "generative AI performance" report in Google Search Console.
- **What they saw**: From mid-May, 9,093 generative AI impressions in total. Daily impressions grew from 30 to 40 to 200 to 280; 579 URLs appeared in all. Another person in the industry's website had 116,061 AI impressions in 53 days.
- **Limits**:
  - Many in the industry point out that this report lacks data on "what users asked" and "whether they clicked."
  - Someone in the industry observed that about two-thirds of the long-question impressions in their own report were actually other people running tracking probes by "asking while pretending to be a certain role." These impressions get zero clicks and will distort your judgement of real demand.
  - Bing Webmaster Tools also provides AI citation data. Someone in the industry reported that a new site only two months old had about 865 citations in seven days, but with large daily fluctuations.
- **The lesson**: Official reports are some of the few data that are "not obtained by sampling." But they only cover their own engine, and the items you can see are limited.

---

## 9. Do it yourself: a credible measurement process

Each of the 15 steps below is marked with where its evidence comes from.

**1. Measure a baseline first, then make changes.**
Before making changes, measure at least twice, ideally across two or more days. Otherwise you cannot tell whether a change came from what you did, or from the drift that happens every day anyway.
(Many in the industry believe this, and some people in the industry have tested it themselves.)

**2. Questions should come from what real buyers say.**
Look in sales calls, customer service records, customer reviews, and the query reports in search engines' webmaster tools. Do not put your own brand name in the questions.
(People in the industry have tested this themselves; community consensus.)

**3. Fix the question set and label its version.**
Add new questions by "adding a new column." Do not replace old questions or change their wording.
(People in the industry have tested this themselves.)

**4. Screen the questions first.**
Do one trial run first, and set aside questions that "never name any brand"; do not include them in the main score. Look at trends grouped by question type: "which is best," comparison, alternatives, and use-case.
(People in the industry have tested this themselves; there are also individual observations.)

**5. Ask each question several times, and include the sample size when reporting the mention rate.**
Research suggests at least 7 to 8 times per question per day. On a limited budget, at least 3 times, counting by a "2 out of 3" majority.
(Researchers testing real AI search repeatedly; people in the industry testing on their own, repeated, with controls.)

**6. Spend the budget on breadth.**
Multiple engines, multiple languages, multiple regions and multiple phrasings are more effective than running the same question dozens of times.
(Researchers testing on real AI search; but only sentiment was measured, and the authors are a service provider.)

**7. Report each engine, language and region separately.**
Do not blend them into a single average score.
(Researchers testing real AI search repeatedly; people in the industry testing on their own.)

**8. Fix one observation window, and record the settings.**
Write down: programming interface or product interface, whether search is on, model version, region, whether logged in. If you use the programming interface, regularly spot-check the product interface with a clean conversation.
(Researchers testing real AI search repeatedly; people in the industry testing on their own.)

**9. Record every run.**
Write down: whether there was an answer, whether it looked things up, the failure category, whether you were mentioned, which URLs were cited, whether you were recommended, and what position you were in. Failures and gaps do not count as "not mentioned."
(People in the industry testing on their own, repeated, with controls.)

**10. Fix the definition of "a hit."**
Should brand aliases and product names count? If the question already contains the brand name and the answer just repeats it, should it be removed? Once the definition is set, do not change it; if you change it, build a new baseline.
(Observations from individual people in the industry.)

**11. Set up a control group.**
Do no optimisation at all on about a quarter of the questions. Also track a group of peer brands you do not serve.
(People in the industry testing on their own, repeated, with controls; there are also individual observations.)

**12. Look at trends, not single weeks.**
Research suggests looking at a rolling window of 2 to 4 weeks; people in the industry mostly use 4 weeks or more. One person in the industry's rule of thumb: treat changes within 15% in a single week as noise at first, and only take them seriously if they repeat for two weeks in a row. This is just personal experience, not a law.
(Researchers testing real AI search repeatedly; people in the industry testing on their own.)

**13. To judge whether a change is real, ask three questions.**
- Are several platforms moving at the same time?
- Is the number of cited URLs moving with it?
- Does the timing line up with what you did?
(People in the industry testing on their own.)

**14. Record the cited URLs, not just "whether you appeared."**
The list of cited sources tells you which pages to go after for exposure. But it only shows "a connection," not "that these sources caused it."
(People in the industry testing on their own.)

**15. Fill in both ends.**
- Use server logs to see whether AI crawlers have come to fetch.
- Use official webmaster tools (such as Google Search Console and Bing Webmaster Tools) to see AI impressions.
- Split traffic into two buckets: "confirmed as from AI" and "inferred as possibly from AI."
(People in the industry testing on their own.)

### How much does it cost to do it yourself?

The following are reference figures from people in the industry testing on their own; prices will change:

- Building it yourself with a search programming interface that returns citations costs about half a US cent per query; one round of 100 queries costs about US$0.5.
- About 300 queries, 4 engines, run every day: programming interface costs of about US$30 a month.
- 600 runs a day on a single engine: about US$1.6.
- One person in the industry's own program crashed at about 50 queries, having spent about US$200.

Doing it yourself is not necessarily cheaper, but the advantage is that the method is entirely in your hands.

### The minimum viable version

If you just want to get started, one person in the industry's approach is:

- Fix 5 questions real customers would ask.
- On the same day each week, ask each engine once.
- Count only "how many of the 5 questions mention us."

The sample is small, but the advantage is that the client can sit alongside and reproduce it themselves. Even better is to ask each question 3 times.

---

## 10. How to evaluate tracking tools and GEO service providers

### One overall principle: does it dare to let you catch it being wrong?

Someone in the industry who also builds tools proposed a very useful overall principle:

> **Does this tool make claims that "you could catch it being wrong about"?**

If it only says "you appeared," you cannot verify whether it is right. But if it says "this answer cited your pricing page and a competitor's comparison page," you can open them and check for yourself.

### 12 questions to ask

| Question to ask | Why ask it | Where the evidence comes from |
|---|---|---|
| How many times is each question run? Does it report sample size and margin of error? | About a third of a single run is noise | Research, plus people in the industry testing on their own |
| Does it test the programming interface (with or without search), or the product interface? | The overlap between different windows is only 12% to 15% | Research |
| Who sets the question set? Can you set it yourself and keep it fixed? | Default question banks often lean toward other industries, and contain many questions "no one can win" | People in the industry testing on their own |
| Can you see the raw answers and the cited URLs? | Only numbers that can be checked are worth anything | People in the industry testing on their own (repeated, with controls) |
| Are engines reported separately? | Averaging them together confuses "really absent" with "the engine doesn't list sources anyway" | People in the industry testing on their own |
| How are failures, gaps and cases where it didn't look things up handled? What is the denominator? | Recording failures as zero creates fake declines | People in the industry testing on their own |
| Can it tell "a model update" from "your changes"? Is there a control group? | A model update makes the whole category move together | People in the industry testing on their own |
| Is the score calculated with fixed rules, or scored by an AI model? | When a model scores, the same input may drift by 10 to 15 points | People in the industry testing on their own |
| Does it really ask every engine it claims to cover? | Someone in the industry read the code of an open-source tracking tool: the documentation claimed to cover several engines, but the code had only one engine's interface and three fixed questions | People in the industry testing on their own |
| Where does the "question search volume" data come from? | Someone in the industry tested an interface that provides AI keyword data; it reported zero search volume for a batch of niche queries, but when asked manually, the platform answered every time. The source and representativeness of this kind of data cannot be verified | People in the industry testing on their own |
| How does traffic attribution handle visits that "carry no source information"? | Counting only referral traffic will, by structure, underestimate | People in the industry testing on their own (repeated, with controls) |
| Do its numbers match your business data? | The tool's charts should match what you hear in sales calls | People in the industry testing on their own (repeated, with controls) |

### Ask for a few more things when evaluating service providers

Many in the industry believe that when evaluating a GEO service provider, you should ask them to:

- explain their specific measurement method;
- show results that can be verified;
- explain how those results connect to business outcomes.

You can add two more:

- Before charging, can they first show you a baseline done to the standards above?
- Can changes and results be matched to the specific week they happened?

### Warning signs: if any one appears, press for answers

- Only a single "AI visibility score" that blends all engines together, or "you rank number X in AI."
- Percentages without sample sizes. Someone in the industry observed a report that printed "only 1 mention in total" as "1% share of voice"; it also gave inexplicable fields such as "100% purchase likelihood" from a sample of 15 questions over 14 days.
- Only screenshots; or only a list of questions, without the raw answers.
- Reporting long-term trends using a question set that keeps changing.
- Using a single before-and-after comparison to prove "our optimisation worked."
- The same domain's numbers differing several times over between tools, with no one able to explain how each one is calculated.

### Why tool numbers jump around

Someone in the industry tested this themselves: after trying several tools in a row, they found the numbers jumping wildly every week (60%, 35%, 50%). They manually asked the same question 10 times in a row, and got a different answer every time.

The problem is not that the tools have bugs, but that most tools run each question only once. Because running it ten times also makes the programming interface costs ten times higher.

---

## Key points of this chapter

1. **Visibility is a probability distribution, not a ranking.** On real AI search, about two-thirds of cited sources change every day, and the same happens with repeats within a day. A single snapshot has no value as evidence.
2. **When reporting the mention rate, always include the sample size and margin of error.** For 4 out of 10, the true range is roughly 12% to 74%.
3. **Spend the budget on breadth.** Multiple languages, engines and phrasings reduce error more than hammering the same question. There is no fixed answer for how many samples you need; engines with fewer citations need more.
4. **Different windows cannot substitute for each other.** Programming interface and product interface, app and web, logged in and logged out, different regions and languages: each sees something different. Choose one window, keep it fixed, and record the settings.
5. **Scores are defined.** The question set, weights, question types and the rules for "a hit" all change the numbers dramatically. Keep them fixed; if you change them, rebuild the baseline.
6. **Count mentioned, cited and recommended separately, then fill in crawling and traffic at both ends.** Being cited is not the same as being recommended; whether you are crawled is a leading indicator; traffic is structurally underestimated.
7. **Without a control group, you cannot tell your changes from model updates.** Keep a portion of questions unoptimised, plus a group of peer brands as a benchmark.
8. **When evaluating tools and service providers, trust only numbers that can be checked.** You must be able to see the raw answers, the cited URLs, the denominator, how failures are handled, and how many times it was run. No research so far proves that visibility reliably turns into traffic or revenue; anyone promising this needs to show their own data.

---

## Remember in one sentence

> **Every AI answer is one roll of the dice: don't look at what place you ranked on one roll; look at how many times you appeared after rolling many times on a fixed set of questions.**

---

## What you can do tomorrow

1. **Write down a set of questions real buyers would ask.** Look in sales calls, customer service records, reviews, and webmaster tools' query reports. Don't put your own brand name in the questions. Then fix this list and label its version; from then on, only add to it, never rewrite it.
2. **Do one trial run first, and screen out questions that "never name any brand"**, then group the rest by type: which is best, comparison, alternatives, use-case.
3. **Measure a baseline before making changes**, at least twice, across two or more days.
4. **Ask each question at least 3 times**, counting "2 out of 3"; if the budget allows, follow the research suggestion of 7 to 8 times per question per day. When reporting, always state "how many times asked, how many times appeared."
5. **Spend the budget on breadth**: multiple engines, multiple languages, multiple regions, multiple phrasings. Report each separately; don't blend them into one average score.
6. **Choose one observation window and write down the settings**: programming interface or product interface, whether search is on, model version, region, whether logged in. If you use the programming interface, regularly spot-check the product interface with a clean conversation.
7. **Record every run**: whether there was an answer, whether it looked things up, the failure category, whether you were mentioned, which URLs were cited, whether you were recommended, position. Failures don't count as "not mentioned."
8. **Write down the rules for "a hit"** (whether aliases count, whether to remove questions that already contain the brand name); once set, don't change them; if you do, rebuild the baseline.
9. **Keep about a quarter of the questions as a control group**, with no optimisation at all; also track a group of peer brands you don't serve.
10. **Look at results as trends over 2 to 4 weeks or more**, not single weeks. When you see a change, ask three questions: are several platforms moving together? Is the number of cited URLs moving with it? Does the timing line up with what you did?
11. **Record the cited URLs** as clues to "where to go after exposure," but don't treat them as proof of cause and effect.
12. **Open your server logs and see whether AI crawlers have come to fetch your site.** With zero crawler fetches, there cannot be any citation based on searching online.
13. **Open Google Search Console and Bing Webmaster Tools and look at AI impressions and citation data**, while remembering that they lack query and click information, and may be mixed with other people's tracking probes.
14. **Split traffic into two buckets**: "confirmed as from AI" and "inferred as possibly from AI."
15. **If your budget is very small, start with the minimum viable version**: 5 questions, the same day each week, asked once on each engine (ideally 3 times), counting only "how many of the 5 questions mention us."
16. **Take the 12 questions from Section 10 of this chapter to your tool or service provider**, and ask them to give you a baseline first and match results to specific weeks.
17. **Spot-check regularly yourself**, to confirm the tool's numbers match what buyers actually see and what you hear in sales calls.

---

## Stop doing this

**Don't:**

- Don't use one question and one screenshot to prove "we were recommended" or "we disappeared."
- Don't check your own visibility with your own logged-in account.
- Don't count results where "the brand name was already in the question" towards visibility.
- Don't change question wording, replace questions or change counting rules during tracking, while continuing to draw the same trend line.
- Don't record programming interface failures, rate limiting or missing answers as "not mentioned."
- Don't add up or directly compare raw citation counts from different engines: the number of citations per answer differs several times over between engines.
- Don't treat the list of cited sources as proof of cause and effect.

**Outdated practices:**

| Outdated practice | Why it is outdated |
|---|---|
| Treating AI answers as a search results page and tracking "what place we rank" | An answer is a distribution; the list and the order change almost every time |
| Running each question once a week and drawing it as a trend chart | The noise from a single run is bigger than the effect of most changes |
| Doing a one-off "AI visibility audit" | An audit is just a snapshot; models, competitors and cited sources change within weeks. Someone in the industry tested this themselves: a brand's visibility score stayed at the same value for 47 days in a row, while AI's purchase recommendations had long since shifted to a competitor |
| Measuring GEO by traffic alone | Being named but not clicked leaves no record at all; visits brought by AI are often recorded as direct traffic |

---

## What is still uncertain

- **Can visibility bring business?** So far there is **no evidence**. No research proves that GEO visibility reliably brings traffic or conversions. All the strong evidence is only about "how to measure without fooling yourself."
- **How many times should each question be run?** There is no consensus. People argue for anything from 3 times to 20 or more; research says to look at the total sample size and judge while collecting. The only thing known to be wrong is "once."
- **Is adding breadth 15 times more effective than more repetition?** The direction is credible, but the number comes from a service provider, measured sentiment rather than mention rate, and its margin of error has not yet been calculated.
- **Should you test the programming interface or the product interface?** Both sides have a point; the current compromise is to fix one window and spot-check with the other.
- **Which engine is the most stable?** The data from different sides contradict each other, and the order changes with question type, time and settings.
- **Are brands more stable, or are sources?** "Whether you are mentioned" may be more stable, and "how you are described and what place you rank" may be less stable, but there is no settled conclusion.
- **Can AI visibility really be measured accurately?** A single snapshot cannot; repeated sampling can, but with limited cost and precision.
- **Can numbers from different tools be compared?** The rough order may agree, but URLs and absolute numbers differ a lot; how each tool calculates is often not transparent.
- **Is it "yes or no" for local businesses?** Current evidence from repeated measurement shows there is still fluctuation, but only one side has done measurements.
- **Changing the weights to make scores differ by 31 percentage points** is only possible in theory, and has not yet been confirmed by a real experiment.
- **Conflicts of interest**: Much of the measurement research and industry data in this chapter comes from people who provide visibility services or build tracking tools. Their criticisms of methods are mostly reasonable, but their conclusions naturally lean toward "you need more, and more expensive, measurement."
- **Public "visibility improvement" cases**: so far, not one can clearly show which practice actually worked.
