# Chapter 6 — You Made the Shortlist, So Why Doesn't AI Pick You?

> Of the seven gates, this is the fourth: **does it pick you** (selection and ranking).
>
> Does it search → Can it get in the door → Can it find you → [Does it pick you] → Does it mention you → Does it actually use you → Do people come over
>
> The earlier chapters covered whether you can get onto the **shortlist**. This chapter covers what happens once you are on it: on what grounds AI picks you, where it places you, and who it finally recommends.

---

## First, imagine a scene

What follows is a hypothetical situation.

The owner of an online shop sells handmade coffee grinders. She opens an AI chat tool and types: "What are the best coffee grinder brands?"

The answer lists several well-known big brands. She is not among them.

She tries a different question: "If I only grind enough for one cup of pour-over a day, what kind of grinder should I use?"

This time, the AI mentions her shop, and even repeats the burr material and grind settings written on her page.

She changed nothing. The page is still the same page. Only the question changed.

This scene is made up. But later in this chapter you will see that a practitioner measured something very similar in the real world.

---

## Five questions this chapter answers

1. Once content is on the shortlist, which factors decide whether it gets chosen? Which factors have almost no effect?
2. How much does "being first in line" really matter? Why do different studies give such different answers?
3. In recommendation situations (choosing a hotel, a product, a service provider), what does AI weigh? Can you trust the reasons it states?
4. Why are "being mentioned", "being cited" and "being chosen as a recommendation" three different things?
5. What can you do based on this? What should you stop doing?

---

## The big idea of this chapter

**Being on the shortlist does not mean being picked.**

When AI picks sources, the first thing it looks at is: are you answering exactly "this" question? Next it looks at: have you written concrete facts such as prices, specifications and dates?

Whether the layout looks nice has little effect. Where you are placed in line also matters less than many people think, and the effect is very unstable.

One more thing needs to be clear up front: what AI says out loud about "why I recommend this" and how it actually picks are not the same thing.

Let's go through these one by one.

---

## 1. Filter first, then compare: relevance is the most reliable sieve

### How the librarian picks books

Let's go back to the book's very busy librarian.

You ask him a question. He carries back a stack of books from the shelves; that stack is the shortlist. But he will not read every one to the end.

He works in two steps:

1. **First, filter (gatekeeping).** Does the topic match this question? Is it placed near the front of the stack? Does it state the price or specifications clearly? Is the date fairly recent? If it fails any one of these, it is hard to get picked no matter how well the rest is written.
2. **Then, compare (pulling ahead).** Only after the first step does the comparison begin: who speaks with more certainty and backs it with evidence? Who makes comparisons? Are the ratings high, are there many reviews?

The final result is "chosen, cited, recommended".

### Why "relevance" comes first

AI's task at this step is to answer "this one" question.

However authoritative a piece of content is, if it answers the neighbouring question, similar but different, it is of no use for this question.

"Relevant" here does not mean the broad kind of relevance, as in "we are all in the same industry". It means "the exact sentence the user asked is the one your page happens to answer".

Broad category words and pretty marketing language are often eliminated at exactly this step.

### Evidence 1: a very large controlled experiment

In an experimental system where conditions could be controlled, researchers gave the AI only two sources at a time and had it pick one.

They tested 6 AI models, 18 possible factors and 1,440 scenarios, running about 252,000 trials in total. The results:

- **A topic mismatch** had a huge effect.
- **Position in the list** also had a huge effect (this shrinks outside the experiment; Section 2 covers it).
- **A more recent date** had a clear advantage over an old date. (However, on real ChatGPT, researchers found that predicting citation from how new a page is works about as well as guessing.)
- **Stating an explicit price** was likewise a strong factor.
- By contrast, **changing only the layout**, that is, turning dense paragraphs into a format with headings and bullet points, **had almost no effect**.

Overall, 11 of the 18 factors had a clear effect in 4 or more models; the other 7 had no consistent effect across models.

### Evidence 2: talking about a "quality score" without the question helps very little

Another study was done under test conditions with a given set of web pages.

Researchers compared two prediction methods to see which was better at guessing "which web page will be cited":

- Method A: look at "how relevant this page is to this particular question".
- Method B: ignore the question and just give the page content itself a "quality score".

Method A was far more accurate.

> **A closer look: what these two numbers mean**
>
> The researchers measured prediction accuracy with a "correlation coefficient". It ranges from 0 to 1. The closer to 1, the more the prediction matches the real result; close to 0 means it almost never guesses right.
>
> Method A (relevance to the question) was about 0.39. Method B (a quality score for the content alone) was only about 0.11.

In other words: **talking about "my content is high quality" apart from any specific question helps very little in predicting whether it will be cited.**

### Evidence 3: most non-citations are because it "didn't match"

Yet another study, in a controllable experimental system, set out specifically to diagnose "why something wasn't cited". Researchers analysed 949 comparison pairs and sorted the causes of failure into four categories:

- **62.2%: the content and the question did not match in meaning.**
- 27.1%: problems with content quality.
- 10.1%: problems of technical incompleteness.
- Only 0.6%: deliberately excluded by the system.

In addition, in the starting state before anything was changed, about 43% of on-topic pages were not cited. In other words, "being on topic" is not enough by itself; it has to match that particular question.

### A real observation: the same page, invisible for a broad question, first for a narrow one

What follows is a test a practitioner did on his own; no one has independently verified it.

He manually tested about 30 websites on ChatGPT, and also pulled Google's AI Overviews results through a search-results data interface.

He saw one very clear example. An enterprise client that makes industrial equipment **did not appear at all** for a broad question like "best laser marking machine brands in [a country]"; the answer listed only the big manufacturers.

But for a narrow question like "which type of marking machine should I use for metal marking?", this client **was listed first by ChatGPT, and cited**.

**Nothing on the page changed between the two.**

He also noticed something the cited clients had in common. The AI would repeat **concrete details** from their pages, for example the specific equipment models listed on a clinic's page. Pages written in category language were not cited.

The same practitioner also found that an article ranked first in Google's traditional search results was tested on 6 topics, and ChatGPT did not cite it even once (0/6).

What this observation means: **relevance is about one specific question; it is not a fixed property a page carries around. Concrete nouns match other people's questions more easily than pretty descriptions do.**

### Additional clues: the wording happens to match

The following are all observations from single practitioners and can only serve as circumstantial support for "relevance matters a lot".

- A practitioner saw that social platform content cited by AI used wording **exactly the same** as the user's question.
- A post on a professional networking platform with only 10 likes was also picked by AI, because its title **contained the exact sentence of the question**.
- Another practitioner found that, for the same need, when the question was reworded to a more specific angle, in 21 of 25 cases a niche site replaced a big site.

### How strong the evidence is for this point

This point counts as **fairly strong**. Three studies with different designs (a controllable large-scale experiment, a test with given web pages, and a search-then-answer process that can be repeated) all point the same way.

But you should know two limitations:

- In the "pick one of two sources" experiment, the sources were generated by AI, and the content the AI read was fixed in advance.
- The authors of the "relevance prediction" study themselves provide a content-scoring service.

---

## 2. Does being first in line really matter that much?

Many people believe: as long as you squeeze into first place on the list the AI reads, you win.

That claim is only partly right.

### In the lab, position matters a lot

When AI reads a long string of documents, its attention is not spread evenly.

Simulations and theoretical analysis show that, as a matter of mechanism, a "high at both ends, low in the middle" pattern can appear: information placed at the beginning and the end is used most, and information in the middle is easily overlooked.

In one experiment with fixed documents, researchers gave the AI a set of documents and had it answer questions based on several of them:

- In the worst case, the accuracy rate dropped by more than 20%.
- Under some settings, accuracy even fell **below the 56.1% it scored with no documents at all, answering from its own memory**. In other words, with key information in the wrong place, giving it documents was worse than giving it none.
- Increasing the retrieved documents to 20 or more brought only about another 1% to 1.5% improvement.
- Simply letting the AI read longer content at once did not improve how it used information in the middle either.

Another set of fixed-document experiments was even more striking: **moving a document to position 1 gave a bigger boost than any method of rewriting the content.** Across 54 scenarios, rewriting the content produced a statistically credible ranking improvement in only 3.

### In near-real conditions, the effect shrinks sharply

**Experiment 1: let AI shop on a person's behalf.**

Researchers built their own shopping environment and let an AI assistant that takes multiple steps on its own browse, compare and decide.

- On each shopping trip, the AI assistant looked at 1.63 to 5.83 options. Humans looked at 1.12 on average.
- The effect of position on "whether the AI opens an item to look at it" was only about 1/4 to 1/10 of its effect on humans.
- And the effect was not "the further forward, the better": the share of items viewed was lowest around positions 68 to 74, and then rose again.
- When the AI's "thinking level" was set to maximum, the effect of position on the final choice could no longer be seen statistically.

**Experiment 2: replay the same batch of records.**

In a controllable experimental system, researchers took a batch of already fixed records and replayed them, comparing the citation gap between "ranked 1st" and "ranked 5th":

- Looking directly at the raw observational data: a gap of **42.3 percentage points**.
- After controlling for other factors: only **7.9 percentage points**.
- Re-checked on a set of samples held back in advance and never used: the gap was **0**.

### Why does this happen?

Because in the raw data, sources placed near the front were often more relevant and more authoritative to begin with.

Position is tangled up with these strengths, so it looks as though "position matters a lot". Once the other conditions are held fixed, the effect of position alone is much smaller.

Also, AI assistants look at several options; the more carefully they think, the less they depend on "who appears first".

However, this conclusion has limits. All the evidence above is about AI picking from a list already laid out in front of it.

"Deep research" AI searches many rounds in a row on its own, and here ordering works through another path as well: documents placed first get read first, and what is read first in turn decides what to search for in the next round.

One experiment fixed a batch of candidate documents and only swapped the order of the documents supporting a view and those opposing it. As a result, the overall stance of the evidence the AI read shifted sharply; in about half of the cases, the direction of the evidence it read did not match the overall direction of all the documents. The evidence from this experiment is fairly weak: it did not use a real search engine, it used small models, and it measured which documents the AI read, not the report it finally wrote.

So a more accurate way to put it is: **position has little effect on "a single pick", but in multi-round searching it may be amplified by "what gets read first".**

### How strong the evidence is for this point

"Position matters a lot" comes mainly from simulations and fixed-document experiments. Under those conditions, the position effect is strong.

In AI assistant environments closer to reality and in controlled replays, it is much weaker and unstable. So the conclusion "position matters a lot" **depends heavily on how the experiment is designed**.

---

## 3. AI has its own set of scales

When it comes to "which one to recommend", AI does not neutrally compare every condition one by one.

It has its own set of weights: some conditions are amplified, others ignored.

### An experiment on picking hotels

The researchers published their experimental design and analysis method in advance, and only then began the experiment. The benefit: afterwards, they could not pick out only the results that favoured them to report.

They had 12 AI models choose among 3,024 sets of hotel options, with 61,459 calls in total. All these hotels were **fictional**. Each time only one condition was changed, to see how the probability of the hotel being chosen shifted:

| What was changed | Change in probability of being chosen |
|---|---|
| Rating raised from 3.9 to 4.7 | Up 31.65 percentage points |
| Price per night raised from US$129 to US$249 | Down 30.03 percentage points |
| Has an eco-certification | Up 11.61 percentage points (the researchers judged that AI **gives it too much weight**) |
| Large number of reviews | Up 8.31 percentage points |
| Belongs to a chain brand | Down 1.79 percentage points |
| Management replies to reviews | Up 0.11 percentage points (statistically zero) |
| Placed 1st in the list (compared with positions 2 to 5) | Up about 2 to 4 percentage points, roughly equal to being US$11.7 cheaper per night; but as high as about 26 percentage points for individual models |

This table shows: rating and price are the leading roles.

Some things you might assume must help, such as carefully replying to every review, weigh almost nothing on AI's scales.

### Authority labels get amplified too

Another experiment had AI recommend academic papers. This was also a fixed-document experiment.

The papers' titles and abstracts were **left completely unchanged**; only the "authority labels" were changed, for example which journal the paper was published in. The results:

- **39.2% of the recommendations flipped.**
- Among these flipped cases, 68.2% moved toward the more authoritative side.
- Different models differed greatly in how sensitive they were to authority labels, ranging from 17.4% to 49.2%.

### The reasons it gives are not its real reasons

This is the most counter-intuitive point in this chapter.

AI will earnestly tell you: "I recommend this one because it has good reviews and a reasonable price." But when researchers compared the reasons AI wrote out with the weights it actually relied on, they found the two **only partly agree**.

> **A closer look: how much is "partly agree"?**
>
> The researchers again used a correlation coefficient from 0 to 1. The correlation between the reasons AI wrote itself and its actual weights was between 0.59 and 0.85. There is a relationship, but it is far from a perfect match.

The clearest example is position. Position clearly affects its choice, yet in the reasons AI writes out, **position is mentioned less than 0.7% of the time**.

The researchers also tried directly telling the AI "don't be influenced by authority":

- With strongly worded instructions, the share of reasons in which AI **mentioned** authority fell by 24.0 percentage points.
- But the share of recommendations that **actually** flipped fell by only 12.9 percentage points.
- Gentler reminders were almost useless; on the most advanced group of models, they even backfired.

In other words, AI learned to "not mention it", but the degree to which it is "actually influenced" fell by only about half.

**So you cannot work backwards to its selection logic by asking AI "why did you recommend A?"** What it gives you is an account, not its decision record.

### Limitations to be honest about

In the two experiments above, the hotels were fictional, and the list of papers was fixed in advance.

Their design is rigorous, but they belong to simulation-type evidence, and the strength of evidence counts as **moderate**. They show "how AI may pick, as a matter of mechanism"; they **cannot be taken as equal to the weights in real AI search products**.

---

## 4. AI prefers text that "reads like AI wrote it"

In a controllable experimental system, researchers observed a kind of "stylistic preference".

The more "predictable" a text is for AI, that is, text where after reading the first half of a sentence it is easy to guess the second half, the more likely it is to be cited.

- For each increase of one statistical unit in a text's "predictability" (in research this is called one standard deviation), the probability of being cited rose from 47% to 56%.
- Traditional search rankings do not show this pattern.
- When researchers randomly shuffled the order of sources and had the AI search first and then answer based on what it found, this preference **still remained**.
- What's more, it is **a separate factor** from "whether the content is relevant to the question".

The researchers also tried having AI polish the source text first:

- General polishing increased the number of sources cited per question by about 1.07 on average.
- Polishing aimed at "being cited" increased it by about 2.11.

But this finding has so far **only been verified on a small number of AI engines**, and the strength of evidence is **moderate to weak**. It comes from a controllable experimental system plus observations of a single commercial engine. It is a new finding that needs further confirmation; do not treat it as a rule that applies to every platform.

Another simulation study is a reminder: this preference is not the same as "preferring text written by AI" as such. AI-generated documents that are well compiled and rewritten, on topic and more factually correct get picked far too often (only 67% of the candidate material but over 80% of the top 10); but AI-generated documents that alter names, product names and numbers are almost all blocked by the re-ranking system (exposure no more than 0.09%). For now it is impossible to separate whether what is preferred is "AI's style" or "more complete, more on topic, more correct".

---

## 5. Mentioned, cited, recommended: three different doors

Academic research mostly measures "whether it was cited" or "what position it had when cited".

But for recommendation-type questions, practitioners keep pointing to another door: **a brand appearing in the answer does not mean it is finally recommended.**

In shopping conversations, users often follow up round after round: within what budget? In what region? For what use? With each round of follow-up, the AI eliminates some options based on these conditions.

For now this point comes mainly from practitioners' own tests.

### It appeared, but was not chosen

The following are all practitioners' own test reports; no one has independently verified them. Each report uses different definitions and methods, so **the numbers cannot be compared with one another**. But they point in the same direction:

| What was tested | Scale | Result |
|---|---|---|
| Multi-round brand questions, across 4 AI models | 150+ brand questions | Brands appearing in the round-1 answers made up 78%; only 31% lasted to the final recommendation in round 4 |
| A survey of local businesses in one US city, across 4 AI assistants | 1,444 businesses | Only 241 had ever been named as a recommendation; 83% never appeared once |
| Leading brands across US product categories, asked with category questions that don't mention brand names | 2,475 brands | 86% of e-commerce brands were never mentioned; but when asked about the brand names directly, all 4 assistants knew these brands well |
| Multi-round shopping conversations, across 3 platforms | 12,000+ times | Of the brands that appeared early, 87% did not make it into the final recommendation |

The third row is especially worth remembering: **"AI knows you" and "AI thinks of you when someone describes a need" are two different things.**

One more reminder: if the multi-round tests in the table asked follow-up questions in a pre-written order, they cannot measure "how AI's answers change a real person's next question". A real person's next question may be led by the previous round's answer.

Selection and ranking is a gate of its own.

### Websites AI names on its own are chosen more often

When writing this book, we tested ChatGPT ourselves through the API (method in Chapter 4; the sample is very small and no one else has independently verified it): websites that AI named with `site:` in its search terms had a clearly higher chance of being cited in the same conversation. This was so in 18 of the 20 comparable conversations for the three types, and in 9 of the 10 for the swimming question. This is another signal besides "how similar the meaning is": before searching, AI has already decided where to look.

> **A closer look:** Comparing within each conversation and then combining, a named website's odds of being cited were about 3.6 times those of an unnamed website (about 2.7 times for the swimming question).

### Add one condition, and the recommendation changes

What follows is a controlled test by a practitioner, repeated several times. The author also notes that the sample is small.

For the same 5 healthy-snack shopping questions, he asked each one twice:

- Once with just the question.
- Once with a description of the buyer first: cutting fat, tracking nutrients, reads the ingredients list, doesn't care about price.

Each time he opened a brand-new incognito conversation. The results:

- In the 50 answers without a buyer description, the AI explicitly advised avoiding a certain brand only 2 times.
- With the buyer description added, this became 20 times.
- **The same brand was recommended in one conversation and advised against in another.**
- With the buyer description added, the AI's answers also became more decisive, no longer listing a long string of options.

This shows: the choice depends on the conditions carried in the question, and on AI's own set of scales. The same feature of the same brand may be treated as a strength under some conditions and as a weakness under others.

### A new product replaced in round one before it was seriously considered

What follows is a practitioner's own test; the sample is very small, and no one has independently verified it.

He placed a prebiotic cola newly launched by a large beverage company into 6 AI shopping conversations in total across ChatGPT, Gemini and Perplexity.

In 4 of the 6, the new product was replaced **in the first round** by a challenger brand. That challenger brand had established its position in this category earlier.

It reminds us: **picking often happens right at the start of the conversation.** Once AI leans toward a competitor early on, it is hard to reverse in later rounds.

A theoretical model explains why this kind of "first impression wins" might happen, but it assumes that both users and AI tend to reinforce earlier answers, and this has not yet been verified.

### How strong the evidence is for this point

For "appearing does not equal being chosen", the strength of evidence is currently **weak to moderate**: several sources point the same way, but none has been independently verified, and most involve recommendation and shopping questions.

---

## 6. Two real first-hand observations

The following two cases are both first-hand observations by single practitioners, with no controls; they can only serve as clues.

### The "competitor list" on your own site, used to recommend competitors

One company ranked well in traditional search, and its website was often a main source for AI answers, sometimes cited 4 times in a single conversation.

Yet the AI **never recommended this brand**.

The cause was a passage on the website that said, roughly: "We may not be right for everyone; here are 5 trustworthy competitors."

The AI found the most relevant source, namely the company's own website; then it extracted the passage that listed brand names and used it directly as the recommendation answer.

According to this practitioner, after the company put its own brand first in that list, it became the AI's top-recommended brand within a few days.

In terms of the librarian metaphor: he found your book, then recommended other people, following the recommendation list written in your book.

This observation relates to two principles: relevance decides which document is chosen; and who is written in the list inside that document, and who comes first, then decides whom the answer recommends.

### A small local shop that published its prices

A local business **published its prices** on its website and social media pages. This was the only clear difference between it and nearby competitors. There were 3 businesses in the same trade on the same block, and more than 20 within 5 km.

About 3 months later, in shopping-type questions about a certain product in that area, the shop was listed by AI as the top supplier almost every time. Some customers also reported that they had learned about the shop from Google's AI and ChatGPT.

In controllable experiments, an explicit price is a "gatekeeping" factor. This observation points the same way as the experiments, but it is a single case without controls, and **cannot prove that price was the cause**.

---

## 7. Two reminders about "how to measure"

### Reminder 1: asking once doesn't count

This is what the whole book calls **rolling the dice**.

In a controllable experimental system, under identical conditions, a yes-or-no decision like "whether to cite a certain source" flips about 15% of the time.

The researchers also calculated that about 45% of the observed differences in effect actually came from the randomness inherent in how AI generates text.

So drawing conclusions from a single run makes it easy to see effects that do not exist at all.

### Reminder 2: looking directly at raw data overestimates

The example covered earlier: the gap between 1st and 5th place was 42.3 percentage points in the raw observational data, and only 7.9 after controlling for other factors.

Statistics practitioners run themselves, of the type "such-and-such a factor is linked to being recommended", can suffer from the same problem: something seems to be caused by A, when it is really caused by B, which appears together with A.

---

## 8. Questions still under debate

### Debate 1: does layout and structure help at all?

There are three views:

**View 1: almost no help.**
- In the controllable "pick one of two" experiment, changing only the layout had a small and inconsistent effect.
- A practitioner tested 61 websites and did 540+ citation checks, and concluded that headings, bullet points and semantically appropriate page markup are only a "baseline". Almost every site already does them, so they don't set anyone apart.

**View 2: a little help, but it "redistributes" rather than "expands".**
- In a controllable AI assistant experiment, presenting content with headings, bullet points and tables increased the number of times the target source was cited by about 0.5; but the total number of citations across all sources did not increase.
- "Whether it gets cited" rose by 4.5 percentage points, but the statistical margin of error included zero, so **it is uncertain whether there is a real effect**.
- It looks more like redistributing credit among several similar sources.

**View 3: a clear effect.**
- A practitioner analysed 600 answer snippets and said pages with structured comparison tables were featured 2.4 times as often.
- This report also said that if the author's credentials are written within two paragraphs of the answer, the citation rate rises from about 12% to about 31%.

**How to make sense of it?** The three views are actually measuring different things.

- "Can it get into the answer" is decided mainly by relevance; structure plays a very small role.
- "Among similar sources, who gets more citations": structure may play a small role.
- That 2.4 times is an observed comparison and has not been independently verified. It may be mixed up with the factor "pages that make comparison tables are more relevant to begin with".

### Debate 2: is the position effect large or small?

- Fixed-document research: very large, even larger than all content rewriting.
- The hotel experiment: only 2 to 4 percentage points on average, but as high as about 26 percentage points for individual models.
- The shopping AI assistant: very weak, and not "the further forward, the better"; the more carefully the AI thinks, the smaller the effect.
- Controlled replay: close to zero on the held-back samples.

**How to make sense of it?** The position effect is real, but its size depends on which model it is, how carefully it is set to think, and how long the shortlist is. "Being first means winning" is not a stable rule.

For you, what you can control more is relevance and the conditions you provide, not position.

### Debate 3: does authority matter?

**On the research side:**
- Changing only authority labels such as the journal flipped nearly 40% of paper recommendations.
- Another controllable experiment also found that some pages, even after their content was fixed, still were not cited because they could not compete with others on domain authority.

**On the practitioner side:**
- Several test reports hold that traditional SEO metrics such as backlinks and domain authority have almost nothing to do with whether AI recommends you.
- A practitioner observed pages with very low domain authority beating sites with much higher authority.

**How to make sense of it?** The two sides do not mean the same thing by "authority".

- In the research, authority means labels AI can read, such as a journal name or an institution name, written right in the content it reads.
- The domain authority practitioners talk about is an external score calculated by SEO tools, which AI may not be able to see.

One possible interpretation: **authority labels AI can see have an effect; SEO scores AI cannot see have limited effect.** But this is just one interpretation, and it has not been directly verified.

### Debate 4: how fresh does content need to be?

- In the controllable "pick one of two" experiment, a more recent date is a gatekeeping-level factor.
- A practitioner's test report says some platforms place particular weight on freshness and recommends updating content once every 30 days.
- But this "30 days" is a rule of thumb from a single report, without controls, and **should not be treated as a threshold**.
- In addition, the paper for that "pick one of two" experiment describes the size of some effects inconsistently between its main text and its tables, so the specific numbers should be read cautiously.

### A counterexample: broad category questions are occupied by big brands

The "filter first, then compare" logic does not mean small websites have a chance on every question.

A practitioner's test report points out: broad category questions (for example "the best brands of a certain type of machine in [a country]") are almost always occupied by existing big brands.

In addition, the view that "small websites, because they focus on narrow topics, are actually more likely to be cited" is supported by several practitioners, but remains disputed in some discussions.

**Narrow questions have open spots; broad questions may not.**

---

## 9. What to do, what not to do, and what is already outdated

### Recommended practices (with strength of evidence)

**1. Write around specific questions, not around category words.**
List the questions users ask "with conditions attached", such as budget, region or use case, and make your pages match those questions directly.
Evidence: fairly strong. Controllable experiments, tests with given web pages, and repeatable processes: three types of evidence point the same way.

**2. Write concrete facts that AI can repeat directly.**
For example prices, specifications, model numbers, service areas, certification names, and dated figures.
Evidence: moderate. Controllable experiments show that explicit prices and specifications are strong factors; several practitioner test reports point the same way.

**3. Publish clear prices.**
Price is one of the gatekeeping factors. Options without a price find it hard to get into the comparison.
Evidence: moderate. Controllable experiments, plus a single practitioner's observation.

**4. Keep content genuinely updated, and mark the date.**
In controllable experiments, a more recent date has a large effect.
Evidence: moderate, only from controllable experiments. "Update every 30 days" is just a single rule of thumb.

**5. If your business depends on recommendations, work on your rating and number of reviews.**
In the hotel experiment, rating and number of reviews were the main positive conditions.
Evidence: moderate to weak, from simulations and fictional data.

**6. First diagnose "why you weren't chosen", then make targeted edits.**
In a controllable experimental system, small edits aimed at the cause of failure, changing only about 5% of the content, raised the citation rate from 56.6% to 79.5%.
Evidence: moderate, from a controllable experimental system.

**7. Track "mentioned", "cited" and "recommended" separately.**
Use real shopping-type questions, add one condition (budget, region, size), and record whether you drop out at each step.
Evidence: this is a methodological suggestion from practitioner test reports, not proof of effect.

**8. Repeat every test many times.**
Because in a single generation, the decision to "cite or not cite" flips about 15% of the time.
Evidence: from a controllable experimental system.

**9. Check the comparison and list-type passages on your own website.**
Passages like these may be extracted directly by AI and used to recommend others.
Evidence: observed by a practitioner; only a clue.

**10. If you decide the order of a list (for example, your own comparison page), reasonably place yourself near the front.**
Under fixed-document conditions, position has an effect; but in AI assistants and real systems, the effect is weak and unstable.
Evidence: weak, mainly from simulations.

### Don't do this

- **Don't change only the layout.** Headings, bullet points and consolidating information had almost no effect in controllable experiments. At most, structure redistributes citations among several similar sources; it won't take you from "not chosen" to "chosen".
- **Don't apply generic rewriting rules, and don't drastically compress your pages.** Controllable experiments found that generic rules hurt niche long-tail topics, and also hurt topics that were already performing well; drastically compressing pages didn't work well either.
- **Don't stuff keywords.** In one content-scoring study, keyword stuffing was judged a clear penalty; another practitioner test report found that keyword density has nothing to do with whether content gets featured.
- **Don't use vague wording, and don't let your content contradict itself.** In controllable experiments, both lowered the probability of being cited.
- **Don't treat the reasons AI itself gives as its real basis for decisions.** What it says and the weights it actually relies on only partly agree.
- **Don't count on certain signals that "look like they should help".** For example, in the hotel experiment, the effect of management replying to reviews was statistically zero.
- **Don't draw conclusions from a single query or a single platform.**

### Practices that are already outdated

**Practice 1: adding quotations, statistics and a references section to content to raise citations.**

These three tricks came from a classic 2023 study, and at the time the effect was clear.

Later, researchers retested them under test conditions with given web pages, on several current families of AI engines (including commercial models). **None** of the three tricks raised the share of citations any more.

Measured the way the original study measured, the effects of the three tricks went from +42.6, +32.8 and +27.7 back then to −0.33, −0.28 and −0.79.

In another set of fixed-document experiments, the "add statistics" rewrite **clearly lowered** citation ranking in 19 of 24 scenarios.

This does not mean content can't contain numbers. It means: **forcing in numbers and quotations in order to be cited no longer works.**

**Practice 2: treating SEO domain authority as the main indicator for AI recommendations.**

Several practitioner test reports hold that the link between the two is weak. But remember: authority labels AI can read still have an effect (see Debate 3 in Section 8).

---

## Wrapping up

Let's go back to the online shop owner selling coffee grinders from the beginning.

Her page didn't get worse, and it didn't get better. Only the question changed.

When AI, that very busy librarian, picks sources, the first thing it asks is not "who wrote it most beautifully", nor "who is first in line", but "who happens to be answering this question". Next it looks at whether you have clearly written the facts it can use directly, such as price, specifications, model numbers and dates.

And the reasons it tells you after it has picked are not necessarily its real reasons.

### Key points of this chapter

1. **Relevance is the first door.** It means matching a specific question, not broadly belonging to the same topic. A "content quality score" that ignores the question is weak at predicting citations.
2. **Gatekeeping factors come before the factors that pull you ahead.** A matching topic, an explicit price and a more recent date need to be in place first. Changing only the layout has almost no effect.
3. **The position effect depends on conditions.** It is strong in fixed-document experiments; it shrinks sharply in AI assistants and controlled replays. Looking directly at raw observational data overestimates it.
4. **AI has its own set of scales.** In the hotel experiment, rating and price were the leading roles; eco-certification was given too much weight, and management replies to reviews had almost no effect; authority labels could flip nearly 40% of paper recommendations. These come from simulations and controlled experiments, and only show what is "possible as a matter of mechanism".
5. **Don't trust AI's explanations of itself.** The reasons it gives and the weights it actually relies on only partly agree.
6. **The more "predictable" a text is for AI, the more likely it is to be cited.** This is a fairly new finding, and it has so far been verified only in a limited range.
7. **Mentioned, cited and recommended are three things.** Several practitioner test reports show that a large number of brands appear but are not recommended; the conditions carried in the question change how AI rates the same brand.
8. **The 2023 method of "add data, add quotations" no longer works.** Measure repeatedly and track stage by stage, instead of chasing a one-off trick.

---

### Remember in one sentence

**AI doesn't pick the one that's written best; it picks the one that happens to answer "this question" and states concrete facts clearly.**

### What you can do tomorrow

1. **List the questions customers ask "with conditions attached".** Add budget, region, use case and size. Check each one: does your page answer it directly?
2. **Replace category language with concrete facts.** Write prices, specifications, model numbers, service areas, certification names and dated figures, so AI can repeat them directly.
3. **If you can publish your prices, publish them.** Without a price, you may well be eliminated at the first sieve.
4. **Put dates on your content, and actually update it.** There's no need to be superstitious about the "30 days" figure, but outdated content loses out at the gatekeeping stage.
5. **If your business depends on recommendations, work on your rating and number of reviews.** But don't expect "replying to every review" to make AI pick you more.
6. **First find out "why you weren't chosen", then make small-scale edits.** Changing a small part aimed at the cause of failure works better than a sweeping overhaul.
7. **Record three things separately: whether you were mentioned, whether you were cited, whether you were recommended.** Use real shopping-type questions, add one condition, follow up for a few rounds, and see at which step you drop out.
8. **Ask every question many times.** Look at "how many times out of ten you appear", not your position in any single run.
9. **Go through the "comparison" and "recommended list" passages on your own website.** Make sure AI can't take them directly and use them to recommend others.
10. **If it's a comparison page where you decide the order, reasonably place yourself near the front.** But don't expect this trick to have a big effect.

### Stop doing this

1. **Stop thinking that changing the layout will get you picked.** Headings and bullet points are the basics, not the deciding factor.
2. **Stop applying generic rewriting rules, and stop drastically compressing your pages.**
3. **Stop stuffing keywords.**
4. **Stop using vague statements, and stop letting your content contradict itself.**
5. **Stop taking AI's own stated reasons for recommending at face value.**
6. **Stop counting on signals that "look like they should help"**, such as replying to reviews.
7. **Stop drawing conclusions from one query or one platform.**
8. **Stop forcing in statistics, quotations and references sections to "raise your citation rate".** That is a 2023 method; retested now, it no longer works, and it can even backfire.
9. **Stop treating SEO domain authority as the main indicator for AI recommendations.**

### What is still uncertain

1. **Does layout and structure help at all?** It may only redistribute citations among several similar sources; "comparison tables 2.4 times higher" and "author credentials raise the citation rate from 12% to 31%" are both observations that have not been independently verified.
2. **How big is the position effect?** People have measured everything from close to zero to about 26 percentage points, depending on the model, its thinking level and the length of the shortlist.
3. **Does authority really matter?** "Authority labels AI can see have an effect; SEO scores it can't see have limited effect" is just one interpretation, and has not been directly verified.
4. **How fresh does content need to be?** A more recent date matters, but "30 days" has no controls; the specific numbers in the related experiment are themselves inconsistent in places.
5. **Are small websites that focus on narrow topics really more likely to be cited?** Quite a few practitioners support this, but it is still disputed.
6. **Is AI's preference for text that "reads like AI wrote it" true of every platform?** So far it has been verified on only a few engines.
7. **Do the weights in the hotel and paper experiments equal the weights in real AI search products?** Not necessarily. They only show what is possible as a matter of mechanism.
8. **How large is the "appeared but not recommended" effect?** Several practitioner reports point the same way, but none has been independently verified, the definitions differ, and the numbers cannot be compared with one another.
