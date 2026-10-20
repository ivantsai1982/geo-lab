# Chapter 16 — Conclusion: Questions That Are Still Open

Imagine this scene.

The owner of an online coffee-bean shop reads an article that says: "Adding statistics, quotations and sources to your content can clearly raise your chances of being cited by AI." He spends a weekend adding a "data summary" block to the bottom of every page.

A few days later, he reads another article: "The latest re-test found that adding statistics doesn't help, and sometimes makes things worse."

He doesn't know which one to believe. Both articles say they have evidence.

This chapter is about exactly this situation. In the previous fifteen chapters, we tried to stick to principles that hold up fairly well. In this chapter we want to tell you honestly: on some questions, one study's conclusion is the opposite of another's; on some questions, what people in this industry believe goes further than what research has proven; and on some questions, people in the industry are split among themselves. As of today, none of these questions is settled.

This chapter makes only one big point:

**Conclusions that seem to contradict each other have usually measured different things, at different gates, under different conditions, at different times. First work out which stage it measured and under what conditions, and you can make a sound decision.**

---

## Five questions this chapter answers

1. Which GEO practices have different studies reached opposite conclusions about?
2. How strong is the evidence behind each of these opposite conclusions?
3. Why don't they agree? Is it a different AI, a different time, a different test method, or a different thing being measured?
4. Of the practices that people in this industry widely believe in, which are backed by research? Which go further than the research? And on which do they themselves have no consensus yet?
5. When the evidence doesn't agree, what should you actually do?

For every question, we follow the same order: **the two claims → why they differ → what you should do now.**

---

## First, learn to read "how strong the evidence is"

Things that are all called "research" differ a lot in strength. From start to finish, this book uses the same set of phrases to describe how strong the evidence is, and this chapter does too:

| What this book says | How the research was done | How far it can be generalized |
|---|---|---|
| Researchers tested repeatedly on real AI search and found… | On a real, commercially running AI search, they asked repeatedly and recorded repeatedly | Very useful for that one AI at that one point in time; but it can usually only show that "two things occur together", not prove "which causes which" |
| Under test conditions with given web pages… | Researchers hand several web pages directly to the AI, skipping the step where the AI goes online to find information itself | Can only explain the step of "how the AI writes and cites once it has the information" |
| Seen under lab conditions…; the real world may differ | Researchers build a simplified AI search system of their own, which can be rerun and where every condition can be controlled | The mechanism is credible, but it is not real AI search |
| Possible in theory, but not yet proven | Simulated tests or theoretical calculation: a fixed set of information is handed to the AI, or the AI is made to simulate a scenario | Can only show "possible in principle"; cannot be treated as a real-world conclusion |
| Many in the industry believe | The view held by most people in this industry | A view, not proof |

Before we begin, there are two things to remember.

**First, "consensus" does not mean "correct".** When most people in this industry agree on something, it only means that is the mainstream view within the industry.

**Second, research conclusions have an expiry date.** The research this book draws on ranges from late 2023 at the earliest to September 2026 at the latest. During this period, AI search has gone through several generations. A result measured in one year may no longer be measurable after the AI moves on a generation.

There is also a tool you already know well: **the seven gates**. To answer a question, AI passes through seven gates: "whether to search, whether it can get in the door, whether it can find you, whether it picks you, whether it mentions you, whether it actually uses you, and whether people come over." Many of the "contradictions" in this chapter are really one study measuring the third gate and another study measuring the fifth. Neither side is wrong; they are just standing at different doors.

---

## Part One: Disagreements between studies

### Disagreement 1: Does adding statistics, quotations and source citations to your content help?

The three GEO practices that first spread widely were: adding statistics, adding quotations (quoting what someone said), and stating your sources. The question is: can these three things actually make AI cite you more often?

**Claim 1: They help.**

- Under lab conditions, researchers tested with a simplified system: "take the top 5 search engine results, then hand them to a 2023-generation AI model to write the answer." After adding quotations, statistics and source citations, one metric rose by about 30% to 40%. This metric measures how many words of your content appear in the answer and how near the front they are placed. Another set of metrics based on subjective scoring rose by about 15% to 30%. The real world may differ.
- The same study also found that the effect varies by field. Combining two practices, "making the writing more fluent" and "adding statistics", scored more than 5.5% higher than using a single practice alone.
- Another simulation study used 13 explainable features to rewrite content across the whole page. On three AI models, visibility rose from 13.34%, 8.89% and 5.20% to 18.31%, 15.35% and 10.17% respectively. The researchers then removed each feature one at a time to see how much the effect dropped without it, and found that the biggest contributors were precisely statistics and source citations. This shows that it is possible in theory that "the evidence density of the whole page" is what's at work, but this is not yet proven.

**Claim 2: They don't help, and can even hurt.**

- A simulation study handed a fixed set of information to the AI, with no real online search step at all, and tested 4 newer AI models. Out of 54 scenarios, only 3 showed a statistically reliable improvement in citation ranking; for question-answering tasks, none worked. Even more notably, "adding statistics" made citation ranking **clearly worse** in 19 out of 24 scenarios. This too can only show what is possible in theory.
- Under test conditions with given web pages, another re-test handed 5 sources directly to the AI, skipping the real search step. It covered 6 AI model families plus commercial models, 605 runs in total. The result: none of the three practices (quotations, statistics, source citations) changed the share of citations. The researchers then redid it on 3 newer-generation AIs (450 runs), and the result was again zero, or only a nominal negative.
- This re-test also checked itself using the same metric as the original 2023 study. The results: quotations -0.33, statistics -0.28, source citations -0.79 percentage points. Compare the figures reported by the original 2023 study: +42.6, +32.8, +27.7. In other words, the large gains measured back then almost completely disappeared this time.
- One thing must be made clear: the researchers who did this re-test themselves provide a content-scoring service. This doesn't mean the results are necessarily wrong, but readers should know about this conflict of interest.

**Why do they differ?**

| Angle of comparison | Claim 1 | Claim 2 |
|---|---|---|
| Which generation of AI was tested | 2023-generation models | New-generation models from 2025 to 2026 |
| What was measured | How many words in the answer, subjective impression | Citation ranking, share of citations |
| How the content was changed | Whole-page rewrite, raising the feature density of the whole page | Adding a separate block of statistics or quotations to the page |
| What system was used | A simplified AI search system | A fixed set of information, or manually given sources |

At present, the more reasonable explanation has two points:

1. **What works is the real evidence density of the whole page, not a separately added block.** The same whole-page-rewrite study also found that 9 "word-by-word" GEO rewriting methods (including stuffing keywords throughout the text) performed worse than making no changes at all, on all three AIs.
2. **The effect expires as AI is updated.** The clear effect measured in 2023 can no longer be measured when re-tested on new-generation AI.

**How people in the industry see it:** Many in the industry believe that "only content with genuinely citable points, or useful information, gets cited." This is in line with the "real evidence density of the whole page" explanation. But it is a view, not a measurement.

**What you should do now:**

- Put real, verifiable data and sources where your argument genuinely needs them. Don't add a separate "data summary" block at the end of the article.
- Don't treat the size of the gains measured in 2023 as the effect you can expect today.
- Any claim of "add this element and you'll gain X percent" should be re-tested on the AI you care about, using a fixed set of questions.

---

### Disagreement 2: Does giving content structure (headings, structured data, lists) help?

The question is: if you organize your page into a structured form, for example by writing good page titles, page descriptions and section subheadings, adding structured data, and switching to lists and tables, can that make AI cite you more often?

**Claim 1: It helps at the "whether it can find you" gate.**

- Under lab conditions, researchers built a system using about 171,000 real web pages: first retrieve information using a traditional keyword-matching method, then re-rank it with another model, and finally hand it to a small new-generation AI model to write the answer. Changing only the structural fields (page title, page description, section subheadings, structured data) raised the share of pages reaching the top 20 in the "finding information" stage from 0.58 to 0.71, an increase of about 22%.
- But in the same experiment, at the "re-ranking" step, performance actually fell from 1.00 to 0.83, a drop of about 17%. In other words: structure helps with "being pulled out", but doesn't guarantee "being placed in the small batch of information the AI finally refers to". In terms of the seven gates, it helped the third gate (whether it can find you) but not the fourth gate (whether it picks you).
- Another lab study used an AI system that looks up information step by step on its own, froze the search records from that time, then changed conditions and replayed them to see whether the results would differ. Structured presentation (headings, lists, tables) increased the number of times the target source was cited by about 0.50, but **the total number of citations across all sources did not increase**. The main metric the study wanted to look at was "whether it was cited"; the result was a 4.5-percentage-point increase, but statistically the possibility that "it is actually zero" could not be ruled out, so it is uncertain.

**Claim 2: Formatting has no effect.**

- A simulation study used 6 AI models and 18 factors, and ran about 252,000 tests. Each test gave the AI only two sources and looked at which one it cited. It found that, compared with "one big block of dense text", "structured" was sometimes better and sometimes worse; there was no consistent effect. Changing only the headings, changing only to lists, or only grouping information together had no clear effect. This can only show the theoretical picture.
- In the same study, what actually made a difference were a few "gatekeeping factors": whether the topic is relevant, where it sits in the list, whether a price is stated, and whether the date is more recent.

> **A closer look: What does "no consistent effect" mean?**
> Researchers used a number called the "odds ratio" to see "how many times more likely a structured source is to be chosen than dense text". If this number equals 1, there is no difference; greater than 1 means structure is better; less than 1 means structure is worse. In this study, the numbers calculated for different models and scenarios ranged from 0.79 to 1.68. Some were greater than 1, some less than 1, so it has no consistent direction.

**Why do they differ?**

- **Different gates were measured.** The benefits seen in Claim 1 are concentrated in two stages: "finding the information" and "extracting content from the page". Claim 2 directly tests "with both documents already placed in front of the AI, which one does the AI cite", skipping the finding-information stage entirely.
- **Different things were measured.** "Citations being redistributed among several sources" and "your chance of being cited actually going up" are two different things. Structure may simply let several similar sources take credit away from each other, rather than giving you one more chance of being chosen.
- **The evidence on both sides comes from lab systems or simulations.** So far no one has tested this directly on real AI search.

**What you should do now:**

- Treat "being structured" as a condition for **getting onto the shortlist and making it easy for AI to extract content**, not as a switch that makes AI cite you.
- Put your core entities (brand, product names) and key numbers in structural fields such as page titles and section subheadings. Under lab conditions, this is the change most favorable to "being found".
- Don't expect "turning paragraphs into lists" by itself to make you cited more often.
- Prioritize the gatekeeping factors from Claim 2: aim the topic at the question, state price and specifications, keep the date recent.

---

### Disagreement 3: Is your brand being mentioned on other websites (third-party sources) a strong signal?

The question is: the more your brand is mentioned on third-party websites, the more likely it is to appear in AI's answers?

**Claim 1: Appearing together across many sources is a strong signal.**

- Researchers tested repeatedly on real AI search and found this pattern. They tested 4 Chinese-language AI search engines, 8 interfaces in total across web and mobile app versions, asked 614 questions, each 3 times, and collected about 161,000 citations. The result: when a brand appeared in only 1 citation, the rate of it entering the answer was 2.1%; when a brand appeared in 11 or more citations, the rate was 59.9%.
- In the same study, the researchers built a prediction model to see which factors best predict whether a brand enters the answer. The composite quality score from traditional SEO had an importance of only 4.52% in this model.
- Note: this is a **correlation**, "two things occurring together", not an experiment in which researchers actively changed conditions. It cannot prove that "being mentioned more" "causes" entry into the answer.

**Claim 2: Once the factor "how easy the website is for AI to read" is taken out, third-party sources have no additional effect.**

- Researchers tested repeatedly on real AI search. This time they tested 4 real, running AI assistants — the kind that go online to look things up, compare and make recommendations on someone's behalf. The study covered 1,056 businesses and about 38,000 lookup sessions, and compared businesses in matched pairs with similar fame and similar levels of prior recognition by the AI.
- The result: once the factor "how easy the website is for AI to read" was taken out, two metrics measuring "third-party sources" and "how easy it is to be discovered" had no clear additional effect on any of these three things: whether the answer came from the business's own website, whether the business was recommended, and how much it cost the AI to look things up. Conversely, "how easy the website is for AI to read" itself was associated with these three things at +0.62, +0.41 and -0.27 respectively (positive means they rise together, negative means they fall together; the last is negative, meaning the easier to read, the lower the AI's cost).
- For websites that were easy to read, 78% of the AI's answers came from the business's own pages; the comparison group was 58%. The share explicitly recommended was 20% versus 11%.
- It must be made clear: this is a matched observational study, not an experiment. The scoring tool was built by the researchers themselves, and the researchers themselves also provide related services.

**Why do they differ?**

| Angle of comparison | Claim 1 | Claim 2 |
|---|---|---|
| Which stage is looked at | Whether the brand can **appear** in the answer | After the AI has already found the brand, whose content it uses when it **looks deeper** |
| Which AIs and which market were tested | Chinese-language AI search engines | Mainly English-language AI assistants |
| The outcome measured | Whether it entered the answer | Whether the answer came from its own website, whether it was explicitly recommended |

At present, the more reasonable explanation is: the two may act at different stages. **Third-party sources affect "whether AI thinks of you"; how easy your website is for AI to read affects "once AI thinks of you, whose content the answer is written from".**

**How people in the industry see it:** Many in the industry believe third-party sources are extremely important. Common claims include: "a brand being consistently mentioned on external platforms such as social discussions and review sites matters more than your own website's ranking", "the same core explanation repeated across several platforms is more likely to be adopted by AI than a single good page", and "consistent descriptions of the brand across platforms are key to AI understanding and citing the brand".

These views point in the same direction as Claim 1, but go further. The research has shown only a correlation; and one study shows that at one stage, once other factors are taken out, third-party sources have no additional effect. As for claims like "GEO is 70% distribution and 30% content", they are only rule-of-thumb ratios with no research behind them. Many in the industry believe this, but "many people believe it" does not mean "it is right".

**What you should do now:**

- Do both, but be clear about which stage each is responsible for: real, consistent mentions on external websites are responsible for making AI "think of you"; your own website being smoothly readable by AI is responsible for making sure that "once AI thinks of you, it tells your version".
- With third-party sources, aim for authenticity and consistency; don't manipulate the numbers. The reason appearing together across many sources may help is that it reflects real evidence from many parties.
- Don't treat "building a presence on external websites" as a shortcut that lets you ignore whether your own website is easy to read.

---

### Disagreement 4: How much does being near the top (position) matter?

The question is: how much does a document's position — in the search results, or in the batch of information placed in front of the AI — affect whether it gets cited or chosen?

**Claim 1: When the AI has a fixed set of information in hand, position has a big effect.**

- A simulation study showed that putting a document in position 1 of that set of information brought a benefit (+2.77 in the retail field) far greater than any GEO content rewrite. This can only show what is possible in theory.
- The same study also showed: as more and more people adopt the same rewriting method, each adopter gets less and less benefit, eventually approaching zero. It's like everyone fighting over the same pie: if one person takes more, others get less.

**Claim 2: When the AI looks at several options on its own, or in a strictly controlled replay, position has only a weak effect.**

- A simulation study built its own hotel search environment and had 8 AI models play shopping assistants booking rooms for people. These AI assistants looked at 1.63 to 5.83 options each time, while humans looked at only 1.12 on average. Position's effect on "whether it clicks in to look" was only a quarter to a tenth of that for humans. And this effect didn't simply get smaller the lower the ranking: it was lowest at around positions 68 to 74, then rose again.
- In the same study, when the AI was set to its most careful-thinking mode, position had no clear effect on which hotel was finally chosen. One hotel, which was not fully outdone on every condition by any other hotel, took 78.2% of all bookings.
- Under lab conditions, the researchers first looked at the raw observational data: the difference in citation rate between sources ranked 1st and 5th was 42.3 percentage points. But after strictly controlling other conditions and replaying, the gap shrank to only 7.9 percentage points. In another batch of samples held back for checking, the gap was 0.

**Why do they differ?**

- **Different test methods.** In the raw observational data, documents ranked near the top are often more relevant and of better quality in the first place. Once that influence is controlled for, the effect of "position itself" shrinks sharply.
- **Different types of AI system.** An AI that looks at a fixed set of information once and writes an answer behaves differently from an AI assistant that looks at several options and compares them.
- **Different models and settings.** How large the bias caused by position is changes with the model and with the level of thinking effort.

At present, the more reasonable explanation is: **raw observational data overestimates the effect of position.**

**What you should do now:**

- "Getting onto the shortlist" is still very important. If you can't get on, nothing else matters.
- Once you're on the shortlist, rather than fighting over one or two ranking places, make sure you aren't fully outdone by competitors on the visible conditions (ratings, price, specifications, how well you fit the question).
- Don't judge whether your optimization worked by the single number "what position am I in".

---

### Disagreement 5: Does llms.txt help?

llms.txt is a text file placed in the top-level directory of a website, intended to tell AI "what important content this website has". The question is: can providing this file raise your visibility in AI answers?

**Claim 1: It has no relationship to the outcome.**

- Researchers tested repeatedly on real AI search, covering 5 commercial AIs that search online and 5,460 answers. Among the websites cited, 16.9% had an llms.txt (177 out of 1,047 websites). And the correlation between technical markers like llms.txt and answer accuracy was about -0.04, essentially no relationship at all.
- Limitations: this study measured "whether the answer was correct", not "whether a given website would be cited". It is also observational data, not an experiment.

**Claim 2: As part of the whole package of conditions for "how easy the website is for AI to read", it is related.**

- Researchers tested repeatedly on real AI search, using real AI assistants to look up real business websites. Businesses whose websites scored higher on AI readability had more of the answer drawn from their own pages, and a higher share of explicit recommendations. This readability score includes several items: content readable without relying on JavaScript, structured data, an llms.txt or plain-text fallback version, and website crawler rules that don't block AI assistants.
- Limitations: this is a score combining a whole package of conditions, without breaking each item out separately. So it cannot say whether llms.txt on its own is effective.

**Why do they differ?** In fact, the two don't directly conflict. One measured the relationship between "llms.txt on its own" and "answer accuracy"; the other measured the relationship between "a whole package of conditions including llms.txt" and "whether the answer uses your own content". **There is currently no evidence that llms.txt on its own is effective.**

**How people in the industry see it:** Many in the industry believe llms.txt doesn't help with AI visibility or citation, and also believe that most AI models don't even look for this file. This broadly agrees with the research.

Many in the industry also believe that two other things are more concrete:

- AI crawlers are often blocked by default, or unintentionally, at the layer of the website's front-end protection and acceleration services (such as a content delivery network, CDN, or a web application firewall, WAF). In that case, even if the website's robots.txt allows the crawler in, it makes no difference.
- Most AI crawlers don't execute JavaScript. If your content only shows up after the browser runs JavaScript, these crawlers can't see it.

These two points are likewise industry views, not research proof.

**What you should do now:**

- llms.txt costs very little to do, so you can do it. But don't make it a priority, and don't expect it to bring change on its own.
- First check the more basic parts of that whole package of conditions: is your core content already there in the source code when the page first loads (the initial HTML)? Are your website's front-end protection and acceleration services blocking AI crawlers?

---

## Part Two: Gaps between what people in this industry believe and what research has proven

This part covers only two kinds of situation: views on which people in this industry have clearly formed a consensus, and views on which they are clearly split. Where we write "many in the industry believe" below, it describes views within the industry, not proof.

### Gap 1: "Clear, direct content that puts the answer first is more likely to be cited"

**What people in this industry say:** Many in the industry believe that content that gives clear, direct answers and is well structured is more likely to be extracted and cited by AI; that the answer should be placed at the start of the page; and that AI prefers concise passages that can be taken out on their own as an answer, rather than long pages that try to cover everything. This is one of the views with the most supporters in the whole industry, with almost no one opposing it.

**What research says:**

- **Partly supported.** Seen under lab conditions: putting the answer first and keeping the topic consistent helps at the "whether it picks you" (selection and ranking) gate. Conversely, changing only the body text while greatly lengthening the content makes a document fall behind in both the "finding information" and "re-ranking" stages.
- **Partly not supported.** Simulation studies show that formatting itself (structured versus dense text) has no consistent effect. Under lab conditions, structured presentation merely redistributed citation credit among several similar sources, and did not reliably raise the chance of being cited.

**Where the gap is:** People in this industry treat "putting the answer first" (a content matter) and "switching to lists and tables" (a formatting matter) as the same thing. Research shows the former has support at the level of mechanism, while the latter has limited effect. In addition, specific thresholds such as "the answer should be within the first 100 to 150 words" are industry experience; research has not produced this number.

**What you should do now:** Prioritize "answer first" and "topic focus" at the content level. Treat formatting changes as a support, not as your main method.

---

### Gap 2: "SEO is the foundation of GEO" and "a good Google ranking doesn't guarantee AI can see you"

**What people in this industry say:** There are two views in the industry.

- The first view: GEO (and other similar names) is an extension of SEO, not a replacement; a solid SEO foundation is the main route to AI visibility. But quite a few people oppose this view; it is not one-sided.
- The second view: a good Google ranking doesn't guarantee you'll be seen in AI answers. Almost no one opposes this.

**What research says:**

- **Supporting "SEO is the foundation":** Simulation studies show that a document's position in the batch of information in front of the AI (equivalent to what traditional SEO determines: "whether it's found and how near the top it ranks") has a far greater effect than content rewriting. It was also seen under lab conditions that documents where only the body text was changed fall behind in the "finding information" and "re-ranking" stages.
- **Supporting "ranking doesn't guarantee visibility":** Researchers tested repeatedly on real AI search and found that traditional SEO's composite quality score had very low importance in predicting whether a brand would enter the answer. In another study using real AI assistants, two metrics measuring traditional "answer-style search performance" had no additional effect once "how easy the website is for AI to read" was taken out.

**Where the gap is:** These two views can in fact both hold at the same time. SEO is responsible for "getting onto the shortlist"; after that, re-ranking, content extraction, writing the answer and the AI assistant's deeper look each have different deciding factors. As for ratio claims like "GEO is 90% SEO", there is no research behind them.

**What you should do now:** Keep the basics of SEO, especially: your pages can be crawled and indexed, and can be found for relevant questions. But don't let Google ranking stand directly for AI visibility; measure the two separately.

---

### Gap 3: Structured data (schema markup)

**What people in this industry say:** Many in the industry believe structured data on its own has limited effect; especially when it is added carelessly or incompletely, it has no effect. There is also a stronger claim: "structured data does nothing at all for AI citation." This claim also has supporters, but has not formed a stable consensus.

**What research says:** Seen under lab conditions: when structured data is changed together with page titles, page descriptions and section subheadings, it has a positive effect at the "finding information" stage, but doesn't help with "re-ranking". In the study using real AI assistants, structured data was part of the whole package of conditions for "how easy the website is for AI to read" and was not broken out separately. **No study so far has tested the effect of structured data on citation on its own.**

**Where the gap is:** The industry's "limited effect" is close in direction to research's "effective only at the finding-information stage". But the claim "completely useless" goes beyond what the existing evidence can support.

**What you should do now:** Structured data should be complete, accurate and consistent with the page content. Treat it as supporting information that helps systems understand your page, not as a switch that makes AI cite you.

---

### Gap 4: Being cited is not the same as being recommended (on this one, research and industry agree in direction)

**What people in this industry say:** Many in the industry believe that AI citing your web page doesn't mean it will recommend or mention your brand; being recommended matters more than being cited. This is one of the views with the most supporters and no opponents.

**What research says:** Researchers tested repeatedly on real AI search and found: of the sources AI lists, 66% had content that made it into the body of the answer, 30% were substantively cited, and only 8% were cited in depth. Of the brands that appeared in the cited sources, only 8.3% actually ended up in the answer. In addition, the study using real AI assistants also measured "the share explicitly recommended" separately from "whether the answer came from its own website".

**This one is not a disagreement.** It is an example of industry experience leading the way and research then confirming it with numbers. It is here to remind you: whenever a performance figure reports only "number of citations", ask one more question — does it count "being cited", "being mentioned" and "being recommended" separately?

---

### Gap 5: Testing only once is unreliable (research and industry agree in direction, but the threshold numbers are experience)

**What people in this industry say:** Many in the industry believe that AI output is unstable, and that results from running only once, or only a few times, are unreliable. You should build a fixed, representative prompt set, run it repeatedly, and track it over the long term. Some have proposed "repeat at least 10 times, and keep it up for several weeks".

**What research says:**

- Seen under lab conditions: when only one answer is generated for the same question, the yes/no judgment of "whether a given source is cited" flips 15% of the time on the next run. 45% of the ups and downs of the effect in the experiment came from the randomness inherent in each time the AI generates text. This is what this book calls "rolling the dice".
- Under test conditions with given web pages: GEO practices that have already been published become ineffective as AI is updated (see Disagreement 1).
- Researchers tested repeatedly on real AI search and found: the overlap between the source websites cited by the mobile app version and the web version of the same platform was only 0.19 to 0.51. What this number means: put together all the websites cited by the two interfaces, and those cited by both make up only about 20% to 50%.

**Where the gap is:** The direction agrees. But "10 times" and "several weeks" are industry rules of thumb; research has not derived these numbers.

**What you should do now:** Use a fixed prompt set; ask each question many times; record separately by AI and by interface (app or web); re-measure after every AI update; don't use a single screenshot to judge whether a change worked. Remember: look at "how many times out of ten it appears" (mention rate), not "what position it ranks".

---

### Gap 6: Three things on which people in this industry are themselves split

On the following three things, there are plenty of people in the industry both for and against, and the research this book draws on has not measured them directly. Here we only present the split itself, without concluding for either side.

| Issue | One side's view | The other side's view | State of the research |
|---|---|---|---|
| Traffic from AI | Some believe ChatGPT has brought websites noticeable traffic | About as many people disagree; many also believe traffic from AI recommendations is still small compared with ordinary search | Not directly measured by the research this book draws on |
| Whether tracking tools are accurate | Many believe most AI visibility tracking tools are not reliable enough and lean towards numbers that look good but have no real meaning | At the same time, many believe tracking is feasible and there are several methods; the stronger claim that "tools cannot provide accurate data at all" is opposed by quite a few people | Research only shows that AI output itself is unstable (see Gap 5) |
| Whether GEO is just old SEO | Quite a few people believe GEO is just a fifteen-year-old practice under a new name | Quite a few people also disagree | Research shows that the different stages of AI answering value different things (see Gap 2) |

**What you should do now:**

- Answer questions about traffic and revenue with your own data. Many in the industry believe that directly asking customers "how did you hear about us?" (in a form, or in conversation) is the most effective way to judge whether AI recommendations have brought you customers.
- If you are choosing a tracking tool or service, many in the industry believe you should ask the provider to show a verifiable way of measuring, and to explain how those numbers relate to your business results.
- With tracking numbers, look at trends and relative changes, not the absolute value of any single score. Don't directly compare numbers calculated by different tools.

---

## All the disagreements in one table

| Issue | Research claim 1 | Research claim 2 | Industry view | Current safer understanding |
|---|---|---|---|---|
| Statistics, quotations, sources | Helpful (lab systems, simulation) | Unhelpful or harmful (simulation, given web pages) | Only content worth citing gets cited | Real evidence density of the whole page may help; separately added blocks don't; the effect expires |
| Structure / structured data | Helps at the "finding information" stage (lab system) | Formatting has no effect (simulation) | Structured data on its own has limited effect | It governs being found and being extracted, not a switch that makes AI cite you |
| Third-party sources | Appearing together across many sources is a strong signal (real AI search, correlation) | No additional effect once website readability is taken out (real AI assistants, matched observation) | Extremely important | The two may act at different stages |
| Position | Big effect with fixed information (simulation) | Weak effect with AI assistants and strictly controlled replays (simulation, lab system) | (No clear view) | Raw observational data overestimates the effect of position |
| llms.txt | No relationship (real AI search, correlation) | Part of a package of conditions (real AI assistants) | Unhelpful | No evidence that it works on its own |
| Answer first | Helps re-ranking (lab system) | Formatting itself has no effect (simulation) | Extremely important | Putting the answer first in content has mechanism support; formatting is secondary |
| SEO and GEO | Position has a big effect (simulation) | Traditional quality scores have low predictive power (real AI search, correlation) | SEO is the foundation, but ranking doesn't guarantee visibility | SEO gets you onto the shortlist; after that, other factors decide |

---

## Five common practices when things are uncertain

1. **Think gate by gate.** Most conclusions that "look contradictory" measure different gates among the seven. When you see a conclusion, first ask: does it govern "whether it can find you", "whether it picks you", "whether it mentions you", or the stage where an AI assistant takes a deeper look?
2. **Distinguish types of research.** Conclusions from simulated tests and from "given a fixed set of information" can only show what is possible in principle. Don't treat them as laws of real AI search.
3. **Re-test for yourself.** As soon as AI is updated, old conclusions may stop holding. Test any practice first on your own prompt set, on the AIs and interfaces you care about, before scaling it up.
4. **Avoid tricks that "everyone is using" or that "have expired".** The benefit of content-rewriting techniques everyone is using gets shared out among everyone. Don't keep using practices that re-tests on new-generation AI have already refuted as your main method.
5. **First do what neither side opposes.** Content that can be crawled and displayed correctly; answers placed first; a focused topic; real, verifiable data; real, consistent mentions on external websites. None of these has been refuted by any of the studies or the industry views.

---

## Remember in one sentence

**When you see two opposite GEO conclusions, first ask which gate it measured, under what conditions, and in what year; then first do what neither side opposes, and use your own data to verify the rest.**

---

## What you can do tomorrow

- Open the most important pages on your website and make sure data and sources are placed where the argument genuinely needs them, not in a separate "data summary" block tacked onto the end of the article.
- Check your page titles and section subheadings and make sure they contain your core entities (brand, product names) and key numbers.
- Check your pages against the gatekeeping factors: is the topic aimed at the reader's question? Are price and specifications clearly stated? Is the date recent?
- Make sure your core content is already in the source code when the page first loads, and can be seen without running JavaScript.
- Ask your technical staff or website provider to confirm whether your website's front-end protection and acceleration services (CDN, WAF) are blocking AI crawlers.
- If you want to create an llms.txt, you can, but put it after the items above.
- Make sure your structured data is complete, accurate and consistent with the page content.
- At the start of each page, directly write the answer to the question the page is meant to answer, and keep the whole page centered on one topic.
- On external websites, seek real mentions with consistent descriptions, rather than chasing numbers.
- Build a fixed prompt set, ask each question many times, and record separately by AI and by interface (app, web); re-test after every AI update.
- Record Google ranking and AI visibility separately; don't let one stand for the other.
- When recording results, count "being cited", "being mentioned" and "being recommended" separately.
- In your enquiry form or customer-service chats, add a question: "How did you hear about us?"
- If you are choosing a tracking tool or service, ask the provider to show a verifiable way of measuring and to explain how the numbers relate to your business results; when tracking, look at trends and relative changes, and don't compare numbers from different tools with each other.
- Whenever you see a claim of "add this element and gain X percent", first re-test it on the AI you care about with a fixed prompt set, then decide whether to adopt it across the board.

---

## Stop doing this

- Stop adding a separate "data summary" or "quotation block" at the end of articles in the hope that AI will cite you more often.
- Stop treating the size of the gains measured in 2023 as the effect you can expect today.
- Stop rewriting articles word by word, or stuffing keywords throughout the text. In tests, this kind of rewriting performed worse than making no changes at all.
- Stop thinking that "turning paragraphs into lists" by itself will get you cited more often.
- Stop treating a presence on external websites as a shortcut that lets you ignore whether your own website is easy to read; and don't manipulate the number of mentions.
- Stop judging whether optimization worked only by "what position am I in".
- Stop making llms.txt a priority, or expecting it to bring change on its own.
- Stop adding structured data carelessly or only halfway, and then treating it as a citation switch.
- Stop greatly lengthening content just to change the body text.
- Stop letting Google ranking stand directly for AI visibility.
- Stop using a single screenshot to judge whether a change worked.
- Stop trusting performance figures that report only "number of citations" without distinguishing citations, mentions and recommendations.
- Stop comparing scores from different tools with each other, and stop looking only at the absolute value of a single score.
- Stop using rewriting techniques everyone is using, or practices already refuted by re-tests on new-generation AI, as your main method.

---

## What is still uncertain

- Adding statistics, quotations and sources: the positive results from 2023 can no longer be measured in re-tests on new-generation AI and with the "separately added block" approach. What is more likely to work is the real evidence density of the whole page, but this has not yet been proven on real AI search.
- Structured content: it mainly helps with "being found" and "being extracted"; changing only the formatting did not consistently raise the chance of being cited in multiple tests. And the evidence on both sides comes from lab systems or simulations; no one has yet tested it directly on real AI search.
- Structured data: no study so far has tested its effect on citation on its own.
- Third-party sources and how easy your website is for AI to read: the evidence on the two appears to conflict; more likely, they act at two different stages — "whether AI thinks of you" and "once it thinks of you, whose content it uses". But this is the current reasonable explanation, not a proven conclusion; and both studies are observational, and the researchers of one of them themselves provide related services.
- Position: raw observational data clearly overestimates the effect of position; after strict controls, the effect of position shrinks sharply. But how large the bias caused by position is still changes with the model and settings.
- llms.txt: there is currently no evidence that it works on its own. Industry views broadly agree with the research.
- The industry's strongest points of consensus (answer first, being cited isn't being recommended, testing only once is unreliable) are mostly partly supported by research; but specific thresholds such as "the first 100 to 150 words", "at least 10 times" and "for several weeks" are experience, not research conclusions. Ratios like "GEO is 70% distribution" and "GEO is 90% SEO" also have no research behind them.
- How much traffic AI brings, whether tracking tools are accurate, and whether GEO is just old SEO: on these three things the industry is still clearly split, and there is no research measuring them directly. You should judge using your own data.

---

## A final word: how to keep learning while AI search keeps changing

This is where this book ends. But AI search won't stop here.

To be honest, some of the content in this book will go out of date after a while. This chapter has already shown you one example: the clear effect measured in 2023 could no longer be measured once AI moved on a generation. The conclusions written today will face the same fate.

So, more worth taking away than any single technique is a way of looking at things:

- **When you see a new claim, ask three questions.** Which of the seven gates did it measure? Was it tested on real AI search, or under lab, simulation or given-web-page conditions? In what year, and on which generation of AI, was it tested?
- **Distinguish "proof" from "opinion".** "Many people believe this" is a lead worth considering, but it is not the answer.
- **Pay attention to who is speaking.** If the person putting forward a conclusion is selling related services themselves, that doesn't mean they are necessarily wrong, but you should take a second look.
- **Test it yourself.** Use a fixed set of questions, on the AIs you care about, ask several times, and keep records over the long term. Your own data will always be the evidence closest to your business.
- **Get the basics right first.** Let AI get in the door, find you and understand you; tell the truth and give real data; let others mention you sincerely. None of these has been refuted by any of the research or industry views. They are also the least likely to go out of date.

AI is like that very busy librarian. It will get new shelves, new ways of searching, even a new librarian. But one thing probably won't change: it is always looking for content that is real, clear, and that many people are willing to vouch for.

Turn yourself into that kind of content, then keep watching, keep testing, keep correcting. These are the last words this book wants to leave with you.
