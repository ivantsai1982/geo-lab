# Chapter 6: You Made the Shortlist, So Why Doesn't AI Pick You?

> Of the seven gates, this is the fourth: does it pick you, which is selection and ranking.
>
> Does it search → Can it get in the door → Can it find you → [Does it pick you] → Does it mention you → Does it actually use you → Do people come over
>
> The earlier chapters covered whether you can get onto the shortlist. This chapter covers what happens once you are on it: on what grounds AI picks you, where it places you, and who it finally recommends.

## Imagine

What follows is a hypothetical situation. The owner of an online shop sells handmade coffee grinders. She opens an AI chat tool and types, "What are the best coffee grinder brands?" The answer lists several well-known big brands, and she is not among them.

She tries a different question: "If I only grind enough for one cup of pour-over a day, what kind of grinder should I use?" This time, AI mentions her shop, and even repeats the burr material and grind settings written on her page. She changed nothing. The page is still the same page. Only the question changed.

This scene is made up. But later in this chapter you will see that a practitioner measured something very similar in the real world.

## The big idea of this chapter

**Being on the shortlist does not mean being picked.**

When AI picks sources, the first thing it looks at is whether you happen to be answering "this exact" question. Next it looks at whether you have written concrete facts such as prices, specifications and dates. Whether the layout looks nice has little effect. Where you are placed in line also matters less than many people think, and the effect is very unstable. One more thing needs to be clear up front: what AI says out loud about "why I recommend this" and how it actually picks are not the same thing.

This chapter answers five questions. First, once content is on the shortlist, which factors decide whether it gets chosen, and which have almost no effect? Second, how much does "being first in line" really matter, and why do different studies give such different answers? Third, in recommendation situations, such as choosing a hotel, a product or a service provider, what conditions does AI weigh, and can you trust the reasons it states? Fourth, why are "being mentioned", "being cited" and "being chosen as a recommendation" three different things? Fifth, what can you do based on this, and what should you stop doing? We will go through them one by one.

## 1. Filter first, then compare: relevance is the most reliable sieve

Let's go back to the book's very busy librarian. You ask him a question, and he carries back a stack of books from the shelves. That stack is the shortlist. But he will not read every one to the end. He handles it in two steps.

The first step is filtering, or gatekeeping. He checks whether the topic matches this question, whether the book sits near the front of the stack, whether it states the price or specifications clearly, and whether the date is fairly recent. If it fails any one of these, it is hard to get picked no matter how well the rest is written. Only after passing the first step does it move on to the second step, where comparison begins and the gaps open up: who speaks with more certainty and backs it with evidence, who makes comparisons, whether the ratings are high, whether there are many reviews. Only the final result is "chosen, cited, recommended".

Across these two steps, "relevance" comes first. AI's task at this step is to answer "this one" question. However authoritative a piece of content is, if it answers the neighbouring question, similar but different, it is of no use for this one. Relevance here does not mean the broad kind, as in "we are all in the same industry". It means that the exact sentence the user asked is the one your page happens to answer. Broad category words and pretty marketing language are often eliminated at exactly this step.

### Three studies, one direction

The first piece of evidence comes from a very large controlled experiment. In an experimental system where conditions could be controlled, researchers gave AI only two sources at a time and had it pick one. They tested 6 AI models, 18 possible factors and 1,440 scenarios, running about 252,000 trials in total. The results showed that a topic mismatch had a huge effect. Position in the list also had a huge effect, although this shrinks outside the experiment, as Section 2 explains. A more recent date had a clear advantage over an old one, but on real ChatGPT, researchers found that predicting citation from how new a page is works about as well as guessing. Stating an explicit price was likewise a strong factor. By contrast, changing only the layout, that is, turning dense paragraphs into a format with headings and bullet points, had almost no effect. Overall, 11 of the 18 factors had a clear effect in 4 or more models, and the other 7 had no consistent effect across models.

The second study was done under test conditions with given web pages, and it shows that a "quality score" that ignores the question helps very little. Researchers compared two prediction methods to see which was better at guessing which web page would be cited. One method looked at how relevant the page was to this particular question. The other ignored the question and simply gave the page content a quality score of its own. The method based on relevance was far more accurate.

> **A closer look: what these two numbers mean**
>
> The researchers used a "correlation coefficient" to measure how accurate the predictions were. It ranges from 0 to 1. The closer it is to 1, the more closely the prediction matches the real outcome; close to 0 means it hardly ever guesses right. Looking at relevance to the question gave a figure of about 0.39. Looking only at the content's own quality score gave only about 0.11.

So **talking about "my content is high quality" without reference to a specific question does little to predict whether you will be cited.**

The third study, in a controllable experimental system, set out specifically to diagnose why content was not cited. Researchers analysed 949 contrasting pairs and sorted the causes of failure into four types. Of these, 62.2% were cases where the content and the question did not match in meaning, 27.1% were content quality problems, 10.1% were problems of technical incompleteness, and only 0.6% were deliberately excluded by the system. In addition, in the starting state before anything was changed, about 43% of topically relevant web pages were not cited. This shows that "being on topic" is not enough by itself. The content has to match that one specific question.

### The same page: invisible for a broad question, first for a narrow one

There are similar observations from the real world, but what follows is a test one practitioner ran himself, and no one has independently verified it. He manually tested about 30 websites on ChatGPT, and also pulled Google's AI summary results through a search results data interface. One example was very clear. An industrial equipment client did not appear at all for a broad question like "the best laser marking machine brands in [a certain country]", where the answer listed only the big manufacturers. Yet for a narrow question like "which type of marking machine should I use for metal marking", ChatGPT listed this client first and cited it. The page was not changed at all between the two.

He also noticed that the clients who were cited had something in common: AI would repeat the concrete details on their pages, such as the specific equipment models listed on a clinic's page, while pages written in category language were not cited. The same practitioner also found that an article ranking first in Google's traditional search results was tested on 6 topics, and ChatGPT did not cite it even once (0/6). These observations point to the same thing. Relevance is defined with respect to one specific question; it is not a fixed property a page carries around. Concrete nouns match other people's questions more easily than pretty descriptions do.

There are a few more clues, each a single practitioner's observation, which can only serve as side evidence that "relevance matters a lot". One practitioner saw that the social platform content cited by AI used exactly the same wording as the user's question. A post on a professional networking platform with only 10 likes was picked by AI because its title contained the exact sentence of the question. Another practitioner found that for the same need, when the question was reworded from a more specific angle, smaller niche websites replaced big websites in 21 of 25 cases.

Taken together, the evidence for this point is fairly strong. Three studies with different designs all point the same way: a controllable large-scale experiment, a test with given web pages, and a repeatable "search first, then answer" process. But there are two limitations to know about. In the "pick one of two sources" experiment, the sources were generated by AI, and the content AI read was fixed in advance. And the authors of the relevance prediction study themselves provide a content scoring service.

## 2. Does being first in line really matter that much?

Many people believe that if you can squeeze into first place on the list AI reads, you have won. This is only partly right.

In the laboratory, position does matter a great deal. When AI reads a long string of documents, its attention is not spread evenly. Simulations and theoretical analysis show that the mechanism can produce a "high at both ends, low in the middle" pattern: information at the beginning and the end is used most, and information in the middle tends to be overlooked. In one fixed-document experiment, researchers handed AI a set of documents and had it answer questions based on several of them. In the worst case, accuracy fell by more than 20%. Under some settings, accuracy was even lower than the 56.1% AI achieved with no documents at all, answering from its own memory alone. Put plainly, if the key information is in the wrong place, giving AI the documents is worse than giving it nothing. The same experiment also found that increasing the number of retrieved documents to more than 20 brought only about 1% to 1.5% more improvement, and simply letting AI read longer content at once did not improve how it used information in the middle.

Another fixed-document experiment produced an even more striking result: moving a document to position 1 brought a bigger improvement than any method of rewriting the content. Across 54 scenarios, rewriting the content produced a statistically credible ranking improvement in only 3.

### Closer to real conditions, the effect shrinks sharply

The first experiment had AI do the shopping for people. Researchers built their own shopping environment and let an AI assistant that carries out multiple steps on its own browse, compare and decide. Each time it shopped, the AI assistant looked at 1.63 to 5.83 options, while humans looked at only 1.12 on average. The effect of position on "whether AI clicks to take a look" was only about 1/4 to 1/10 of its effect on humans. And this effect was not "the further forward, the better". The share of options viewed was lowest at around positions 68 to 74, and then rose again after that. When AI's "level of thinking" was turned up to the maximum, the effect of position on the final choice could no longer be detected statistically.

The second experiment replayed the same batch of records. In a controllable experimental system, researchers took a batch of records that had already been fixed and replayed them, comparing how often sources in position 1 and position 5 were cited. Looking directly at the raw observational data, the gap was 42.3 percentage points. After controlling for other factors, only 7.9 percentage points remained. When it was checked again on a separate sample set aside in advance and not used before, the gap was 0.

Why does this happen? Because in the raw data, sources placed near the front were often more relevant and more authoritative to begin with. Position was tangled up with these strengths, so position looked very important. Once the other conditions are held fixed, the effect of position alone is much smaller. In addition, an AI assistant looks at several options, and the more carefully it thinks, the less it depends on who appears first.

This conclusion has limits on where it applies. All the evidence above concerns AI choosing from a list already laid out in front of it. "Deep research" style AI runs many rounds of searching on its own, and here ranking can work through another route: documents near the front are read first, and what is read first decides what to search for in the next round. One experiment fixed a set of candidate documents and only swapped the order of documents supporting a view and documents opposing it. As a result, the overall stance of the evidence AI read shifted sharply. In about half of the cases, the direction of the evidence it read did not match the overall direction of all the documents. The evidence from this experiment is fairly weak, because it did not use a real search engine, it used small models, and it measured which documents AI read, not the report it finally wrote. A more accurate statement is that **position has a small effect on "a single round of picking", but in multi-round searching it may be amplified by "what gets read first".**

As for the strength of the evidence, "position matters a lot" comes mainly from simulations and fixed-document experiments, and under those conditions the position effect is strong. In AI assistant environments closer to reality, and in controlled replays, it is much weaker and also unstable. So this conclusion depends heavily on how the experiment is designed.

## 3. AI has its own set of scales

When it comes to "which one to recommend", AI does not neutrally compare every condition one by one. It has its own set of weights. Some conditions get magnified and some get ignored.

The clearest example is a hotel-choosing experiment. The researchers published their experimental design and analysis methods before starting the experiment, so that afterwards they could not pick favourable results to report. They had 12 AI models choose from 3,024 sets of hotel options, making 61,459 calls in total. All the hotels were fictional. Each time, they changed only one condition and watched how the probability of the hotel being chosen changed:

| What was changed | Change in the probability of being chosen |
|---|---|
| Rating raised from 3.9 to 4.7 | Up 31.65 percentage points |
| Price per night raised from 129 US dollars to 249 US dollars | Down 30.03 percentage points |
| Has an environmental certification | Up 11.61 percentage points (the researchers consider that AI weighs this too heavily) |
| Many reviews | Up 8.31 percentage points |
| Belongs to a chain brand | Down 1.79 percentage points |
| Management replies to reviews | Up 0.11 percentage points (statistically equal to zero) |
| First on the list (compared with positions 2 to 5) | Up about 2 to 4 percentage points, roughly equal to being 11.7 US dollars cheaper per night; but as high as about 26 percentage points for individual models |

This table shows that rating and price are the main characters. Some things you might assume must help, such as carefully replying to every review, weigh almost nothing on AI's scales.

Authority labels also get magnified. Another experiment had AI recommend academic papers, again a fixed-document experiment. The titles and abstracts of the papers were left completely unchanged, and only the "authority labels" were altered, such as which journal a paper was published in. As a result, 39.2% of the recommendations flipped, and in 68.2% of these flipped cases the move was towards the more authoritative side. Different models differed greatly in how sensitive they were to authority labels, ranging from 17.4% to 49.2%.

### The reasons it gives are not its real reasons

This is the most counter-intuitive point in this chapter. AI will tell you very earnestly, "I recommend this one because it has good reviews and a reasonable price." But when researchers compared the reasons AI wrote with the weights it actually relied on, they found that the two matched only partly.

> **A closer look: how much "partly" is**
>
> The researchers again used a correlation coefficient from 0 to 1. The correlation between the reasons AI wrote itself and its actual weights was between 0.59 and 0.85. There is a relationship, but it is far from a perfect match.

The most obvious example is position. Position clearly affects its choices, yet fewer than 0.7% of the reasons AI wrote mentioned position.

Researchers also tried telling AI directly "not to be influenced by authority". With a strongly worded instruction, the share of AI's reasons that mentioned authority fell by 24.0 percentage points, but the share of recommendations that actually flipped fell by only 12.9 percentage points. A milder reminder had almost no effect, and on the most advanced group of models it even backfired. So AI learned to stop mentioning it, while the degree to which it was actually influenced fell by only about half. **So you cannot work out its selection logic by asking AI "why did you recommend A".** What it gives you is an account, not a record of its decisions.

The limitations need to be stated honestly here too. In the two experiments above, the hotels were fictional and the paper lists were fixed in advance. Their designs are rigorous, but they are simulation-type evidence, and the strength of evidence is moderate. They show how AI may pick at the level of mechanism. They cannot be taken as equal to the weights inside real AI search products.

## 4. AI prefers text that "reads like AI wrote it"

In a controllable experimental system, researchers observed a preference in style: the more "predictable" a text is for AI, meaning that after reading the first half of a sentence it is easy to guess the second half, the more likely it is to be cited. For every increase of one statistical standard unit in how predictable the text is (called one standard deviation in research), the probability of being cited rose from 47% to 56%. Traditional search rankings do not show this pattern. When researchers randomly shuffled the order of sources and had AI search first and then answer based on what it found, the preference was still there. And it is a separate factor from "whether the content is relevant to the question".

The researchers also tried having AI polish the source text first. General polishing increased the number of cited sources per question by about 1.07 on average. Polishing aimed specifically at "being cited" increased it by about 2.11. But this finding has so far been verified on only a few AI engines, and its strength of evidence is moderate to weak; it comes from a controllable experimental system plus observations of a single commercial engine. It is a new finding that needs further confirmation. Do not treat it as a rule that holds on every platform.

Another simulation study cautions that this preference does not equal a preference for "text written by AI" as such. AI-generated documents that are well organised and rewritten, on topic and more factually accurate get picked too often: they made up only 67% of the candidate sources but more than 80% of the top 10. But AI-generated documents that tampered with names of people, product names and numbers were almost all blocked by the re-ranking system, with exposure of no more than 0.09%. It is not yet possible to separate whether what gets preferred is AI's style, or content that is more complete, more on topic and more accurate.

## 5. Mentioned, cited, recommended: three different doors

Most academic research measures "whether it was cited" or "what position it held when cited". But for recommendation questions, practitioners keep pointing to another door: a brand appearing in the answer does not mean it is finally recommended. In shopping conversations, users often follow up round after round: what the budget limit is, which region, what situation it will be used in. With every round of follow-up, AI eliminates some options based on these conditions. For now, this comes mainly from practitioners' own tests.

The reports below are all practitioners' own test reports, and no one has independently verified them. Each report uses different definitions and methods, so the numbers cannot be compared with each other, but they point in the same direction:

| What was tested | Scale | Result |
|---|---|---|
| Multi-round brand questions, across 4 AI models | More than 150 brand questions | Brands appearing in round 1 answers made up 78%; only 31% lasted to the final recommendation in round 4 |
| A census of local businesses in one US city, across 4 AI assistants | 1,444 businesses | Only 241 were ever named as a recommendation; 83% never appeared even once |
| Leading brands across US product categories, asked with category questions that do not name the brand | 2,475 brands | 86% of e-commerce brands were never mentioned; but when asked about the brand by name, all 4 assistants knew these brands well |
| Multi-round purchase conversations, across 3 platforms | More than 12,000 | Of brands that appeared early, 87% did not make the final recommendation |

The third row is especially worth remembering. **"AI knows you" and "AI thinks of you when someone describes a need" are two different things.** One more caution: if the multi-round tests in the table asked their follow-up questions in a pre-written order, they cannot measure how AI's answer changes a real person's next question, and a real person's next question may well be steered by the previous answer. Selection and ranking is a gate of its own.

### Sites AI names itself, and the conditions inside the question

While writing this book, we tested ChatGPT ourselves through the API (method in Chapter 4; the sample is very small and no one else has independently verified it yet). Websites that AI named with `site:` in its search terms had a clearly higher chance of being cited in the same conversation. This was the case in 18 of the 20 comparable conversations across three question types, and in 9 of 10 for the swimming questions. This is a signal separate from "how similar the meaning is": before searching, AI has already decided where to look.

> **A closer look:** Comparing within each conversation and then pooling the results, the chance of a named website being cited was about 3.6 times that of a website not named (about 2.7 times for the swimming questions).

The conditions carried in the question also change the recommendation. One practitioner ran a controlled, repeated test, and he himself noted that the sample was small. He took the same 5 purchase questions about healthy snacks and asked each one twice: once with only the question, and once with a description of the buyer first, saying the person was cutting fat, tracked nutrients, read ingredient labels and did not care about price. Each time he opened a brand-new incognito conversation. In the 50 answers without a buyer description, AI explicitly advised avoiding a particular brand only 2 times. With the buyer description added, this became 20 times. The same brand was recommended in one conversation and advised against in another. With the buyer description added, AI's answers also became more decisive and no longer listed a long string of options. This shows that the choice depends on the conditions carried in the question and on AI's own set of scales. The same feature of the same brand may be treated as a strength under some conditions and as a weakness under others.

There is another practitioner's test, again with a very small sample and no independent verification. He placed a newly launched prebiotic cola from a large beverage company into AI shopping conversations on ChatGPT, Gemini and Perplexity, 6 conversations in total. In 4 of the 6, the new product was replaced in the very first round by a challenger brand, one that had established its position in this category earlier. This example reminds us that the picking often happens right at the start of a conversation. Once AI leans towards a competitor first, it is hard to turn things around in later rounds. A theoretical model explains why this kind of "first impression wins" might happen, but it assumes that both users and AI tend to reinforce earlier answers, and that assumption has not yet been verified.

As for the strength of evidence, "appearing does not mean being chosen" is currently weak to moderate. Several sources point the same way, but none has been independently verified, and most concern recommendation and purchase questions.

## 6. Two real first-hand observations

Both of the following are first-hand observations by a single practitioner, with no control group, and can only be treated as clues.

The first concerns a company. It ranked well in traditional search, and its website was often the main source for AI answers, sometimes cited 4 times in a single conversation, yet AI never recommended the brand. The cause was a passage on the website that said, roughly, "We may not be right for everyone; here are 5 trustworthy competitors." AI found the most relevant source, which was the company's own website, then pulled out the passage that listed brand names and used it directly as the recommendation answer. According to this practitioner, after the company put its own brand first on that list, within a few days it became AI's top recommended brand.

In terms of the librarian metaphor, he turned to your book and then, following the recommendation list written in your book, recommended someone else. This observation relates to two principles: relevance decides which document gets chosen, and then who is written on the list inside that document, and who comes first, decides who the answer recommends.

The second concerns a local business. It published its prices on its website and social media pages, which was the only clear difference between it and the competitors around it; there were 3 businesses in the same trade on the same block and more than 20 within 5 kilometres. About 3 months later, in purchase-type questions about a certain product in this area, AI listed this shop as the first-choice supplier almost every time, and some customers said they had heard about the shop from Google's AI and ChatGPT. In controllable experiments, an explicit price is a gatekeeping factor, and this observation points the same way as the experiments. But it is only one case with no control group, so **it cannot prove that the price was the cause.**

## 7. Two reminders about "how to measure"

The first reminder is that asking once does not count. This is what the book calls rolling the dice. In a controllable experimental system, under the same conditions, yes-or-no decisions such as "whether to cite a certain source" flipped about 15% of the time. The researchers also calculated that about 45% of the observed differences in effect actually came from the randomness inherent in how AI generates text. So drawing a conclusion from a single run makes it easy to see effects that do not exist at all.

The second reminder is that looking straight at raw data overestimates effects. As mentioned earlier, the gap between position 1 and position 5 was 42.3 percentage points in the raw observational data, and only 7.9 after controlling for other factors. Statistics that practitioners compile themselves, of the kind "such-and-such factor is linked to being recommended", can suffer from the same problem: what looks like the effect of A is actually the effect of B, which tends to show up together with A.

## 8. Questions still under debate

### Debate 1: Do layout and structure help at all?

There are three views on this. The first view is that they hardly help. In the controllable "pick one of two" experiment, changing only the layout had a small and inconsistent effect. One practitioner tested 61 websites and ran more than 540 citation checks, and concluded that headings, bullet points and semantically appropriate page markup are only a basic threshold that nearly every website already meets, so they do not set you apart.

The second view is that they help a little, but what they do is redistribute, not expand. In a controllable AI assistant experiment, presenting content with headings, bullet points and tables increased the number of citations for the target source by about 0.5, but the total number of citations across all sources did not increase. "Whether it gets cited" rose by 4.5 percentage points, but the statistical margin of error includes zero, so it is uncertain whether there is a real effect. It looks more like credit being redistributed among a few similar sources.

The third view is that they have a clear effect. One practitioner analysed 600 answer snippets and said that pages containing a structured comparison table were 2.4 times more likely to be featured prominently. The same report also said that if the author's credentials are written within two paragraphs of the answer, the citation rate rises from about 12% to about 31%.

The key to understanding these three views is that they actually measure different things. "Whether you can get into the answer" is decided mainly by relevance, and structure plays a very small part. "Who gets more citations among similar sources" is where structure may help a little. As for the 2.4 times figure, it is an observed comparison that has not been independently verified, and it may be mixed up with the factor that "pages that bother to make comparison tables were more relevant to begin with".

### Debate 2: Is the position effect large or small?

The position effects measured by different studies differ enormously. Fixed-document studies find it very large, even larger than all content rewriting. The hotel experiment measured an average of only 2 to 4 percentage points, but as high as about 26 percentage points for individual models. The shopping AI assistant experiment found it very weak, and not a case of "the further forward, the better"; the more carefully AI thinks, the smaller the effect. Controlled replays show that it is close to zero on held-out samples.

Taken together, the position effect is real, but its size depends on which model it is, how carefully it is set to think, and how long the shortlist is. "First place wins" is not a stable rule. What you can control more readily is relevance and the conditions you provide; position is hard to manage.

### Debate 3: Does authority matter?

The research side holds that authority has an effect. Changing only authority labels such as the journal flipped nearly 40% of paper recommendations. Another controllable experiment also found that some pages, even after their content was fixed, were still not cited because they could not compete with others on domain authority. On the practitioner side, several test reports hold that traditional SEO metrics such as backlinks and domain authority have almost nothing to do with whether AI recommends you; one practitioner observed pages with very low domain authority beating websites with much higher authority.

The two sides are not actually talking about the same "authority". Authority in the research means labels AI can read, such as the name of a journal or institution, written right into the content it reads. The domain authority practitioners talk about is an external score calculated by SEO tools, which AI may not be able to see. One possible interpretation is that **authority labels AI can see have an effect, while SEO scores AI cannot see have limited effect.** But this is only one interpretation, and it has not been directly verified.

### Debate 4: How fresh does content need to be? And a counter-example

In the controllable "pick one of two" experiment, a more recent date is a gatekeeping-level factor. One practitioner's test report says that some platforms place particular weight on freshness, and recommends updating content once every 30 days. But this "30 days" is a rule of thumb from a single report with no control group, and should not be treated as a threshold. In addition, in the paper on the "pick one of two" experiment, the main text and the tables do not describe some effect sizes consistently, so the specific numbers should be read cautiously.

Finally, there is a counter-example to keep in mind. The logic of "filter first, then compare" does not mean small websites have a chance on every question. One practitioner's test report points out that broad category questions, such as "the best brands of a certain kind of machine in a certain country", are almost all held by big brands that already exist. The view that "small websites, because they focus on narrow topics, are actually more likely to be cited" has the support of several practitioners, but it is still disputed in individual discussions. The safer statement is that narrow questions have open spots, while broad questions may not.

## 9. What to do, what not to do, and what is already outdated

### Recommended actions

The most important point is to write around specific questions, not around category words. First list the questions users will ask "with conditions attached", for example adding a budget, a region or a usage situation, then make your pages answer these questions directly. The evidence for this is fairly strong: three kinds of evidence, controllable experiments, tests with given web pages and repeatable processes, all point the same way.

Next, write concrete facts that AI can repeat directly, such as prices, specifications, model numbers, service areas, certification names and dated figures. The evidence is moderate: controllable experiments show that explicit prices and specifications are strong factors, and several practitioners' test reports point the same way. Publishing explicit prices deserves a separate mention, because price is one of the gatekeeping factors and options without a price have a hard time entering the comparison; the evidence for this is also moderate, coming from controllable experiments plus a single practitioner's observation. Also a gatekeeping factor is keeping content genuinely updated and dated. In controllable experiments, a more recent date had a large effect, but the evidence comes only from controllable experiments and is moderate in strength, and "update once every 30 days" is only a single rule of thumb.

If your business depends on recommendations, take good care of your rating and number of reviews. In the hotel experiment, rating and number of reviews were the main positive conditions, though the evidence is moderate to weak because it comes from simulations and fictional data.

Before changing your content, first diagnose "why it wasn't picked", then make targeted changes. In a controllable experimental system, making small changes aimed at the causes of failure, altering only about 5% of the content, raised the citation rate from 56.6% to 79.5%; the strength of evidence is moderate. When tracking results, record "being mentioned", "being cited" and "being recommended" separately: use real purchase-type questions, add one condition, such as budget, region or scale, and see whether you drop out at each step. This is a method suggestion from practitioners' test reports, not proof of an effect. Every test also needs to be repeated many times, because according to results from controllable experimental systems, about 15% of "cite or don't cite" decisions in a single generation flip.

The evidence for the last two points is weaker. One is to check the comparison and list-type passages on your own website, because AI may pull these passages out directly and use them to recommend others; this is something a practitioner observed, and it is only a clue. The other is that if you decide the order of a list, for example on your own comparison page, it is reasonable to put yourself near the front. Under fixed-document conditions position has an effect, but in AI assistants and real systems the effect is weak and unstable; the evidence for this point is weak and comes mainly from simulations.

### What not to do

Do not change only the layout. Headings, bullet points and gathering information together had almost no effect in controllable experiments; structure at most redistributes citations among a few similar sources, and will not take you from "not picked" to "picked". Also do not apply generic rewriting rules, or drastically compress your pages. Controllable experiments found that generic rules hurt niche long-tail topics and also hurt topics that were already performing well, and drastically compressing pages did not work well either.

Do not stuff keywords. In one content scoring study, keyword stuffing was judged a clear negative; another practitioner's test report holds that keyword density has nothing to do with whether content is featured prominently. In the same way, do not use vague wording, and do not let your content contradict itself. In controllable experiments, both of these lowered the chance of being cited.

Do not take the reasons AI gives as its real basis for decisions; what it says and the weights it actually relies on match only partly. Also do not count on signals that "look like they should help", such as management replying to reviews, whose effect in the hotel experiment was statistically equal to zero. Finally, do not draw conclusions from the results of a single query on a single platform.

### Outdated practices

The first outdated practice is adding quotations, statistics and reference source sections to content to raise citations. These three tricks come from a classic 2023 study, and at the time the effect was clear. Later, under test conditions with given web pages, researchers retested them on several current families of AI engines, including commercial models, and none of the three raised the share of citations any more. Measured the way the original study measured them, the effects of the three tricks went from +42.6, +32.8 and +27.7 back then to −0.33, −0.28 and −0.79. In another fixed-document experiment, rewrites that "added statistics" clearly lowered citation ranking in 19 of 24 scenarios. This does not mean your content cannot contain numbers. **Forcing in numbers and quotations in order to get cited is a method that no longer works.**

The second outdated practice is treating SEO domain authority as the main indicator for AI recommendations. Several practitioners' test reports hold that the link between the two is weak. But remember that authority labels AI can read still have an effect (see Debate 3 in Section 8).

## Wrapping up

Let's go back to the online shop owner who sells coffee grinders from the start of the chapter. Her page did not get worse, and it did not get better. Only the question changed.

When AI, that very busy librarian, picks sources, the first thing he asks is "who happens to be answering this question". Who writes most beautifully and who is first in line both come later. Next he looks at whether you have clearly written facts he can use directly, such as prices, specifications, model numbers and dates. And the reasons he gives you after picking are not necessarily his real reasons.

## Key points of this chapter

Relevance is the first door, and it means matching a specific question, not broadly belonging to the same topic; a content quality score that ignores the question is weak at predicting citation. Gatekeeping factors come before the factors that open up gaps: a matching topic, an explicit price and a more recent date need to be in place first, and changing only the layout has almost no effect.

The position effect depends on conditions. It is strong in fixed-document experiments, shrinks sharply in AI assistants and controlled replays, and looking straight at raw observational data overestimates it. AI also has its own set of scales: in the hotel experiment, rating and price were the main characters, environmental certification was weighed too heavily, and management replies to reviews were almost useless; authority labels could flip nearly 40% of paper recommendations. These come from simulations and controlled experiments and show only what is possible at the level of mechanism. AI's explanations of itself cannot be trusted; the reasons it gives and the weights it actually relies on match only partly. In addition, the more "predictable" a text is for AI, the more likely it is to be cited; this is a relatively new finding, and the scope of verification so far is limited.

Being mentioned, being cited and being recommended are three different things. Several practitioners' test reports show that large numbers of brands appear but are not recommended, and that the conditions carried in the question change how AI judges the same brand. Finally, the 2023 method of "adding data, adding quotations" no longer works. What you should do is measure repeatedly and track stage by stage; one-off tricks cannot be relied on.

## Remember in one sentence

**AI does not pick the best-written source. It picks the one that happens to answer "this question" and states its concrete facts clearly.**

## What you can do tomorrow

1. List the questions customers will ask "with conditions attached", adding budget, region, usage situation and scale, then check one by one whether your pages answer them directly.
2. Replace category language with concrete facts. Write down prices, specifications, model numbers, service areas, certification names and dated figures, so that AI can repeat them directly.
3. If you can publish your prices, do it, because without a price you are likely to be eliminated at the very first sieve.
4. Put dates on your content, and actually update it. There is no need to treat "30 days" as gospel, but outdated content loses out at the gatekeeping stage.
5. If your business depends on recommendations, work on your rating and number of reviews, but do not expect "replying to every review" to make AI pick you more often.
6. First find out "why it wasn't picked", then make small-scale changes. Changing a small part aimed at the cause of failure works better than a sweeping overhaul.
7. Record three things separately: whether you were mentioned, whether you were cited, whether you were recommended. Use real purchase-type questions, add one condition, follow up for a few rounds, and see at which step you drop out.
8. Ask every question many times and look at "how many times out of ten you appear", not at what position you held in any single run.
9. Go through the "comparison" and "recommendation list" passages on your own website, and make sure AI cannot simply take them and use them to recommend others.
10. On comparison pages where you decide the order, it is reasonable to put yourself near the front, but do not expect this trick to have a big effect.

## Stop doing this

**Stop thinking that changing the layout will get you picked.** Headings and bullet points are the basics, not what decides the outcome. In the same way, stop applying generic rewriting rules, and stop drastically compressing your pages; stop stuffing keywords, and stop using vague wording or letting your content contradict itself.

Stop taking the recommendation reasons AI gives at face value, and stop counting on signals that "look like they should help", such as replying to reviews. When judging results, stop drawing conclusions from one query on one platform.

**Stop forcing in statistics, quotations and reference source sections in order to "raise your citation rate".** That is a 2023 method. Retested now, it no longer works, and it can even backfire. And stop treating SEO domain authority as the main indicator for AI recommendations.

## What is still uncertain

**Do layout and structure help at all?** They may only redistribute citations among a few similar sources. "Comparison tables 2.4 times higher" and "author credentials raising the citation rate from 12% to 31%" are both observations that have not been independently verified.

**How big is the position effect?** People have measured anything from close to zero to about 26 percentage points, depending on the model, the level of thinking and the length of the shortlist.

**Does authority really matter?** "Authority labels AI can see have an effect, SEO scores it cannot see have limited effect" is only one interpretation and has not been directly verified.

**How fresh does content need to be?** A more recent date matters a lot, but "30 days" has no control group, and the specific numbers in the relevant experiment are themselves inconsistent in places.

**Are small websites that focus on narrow topics really more likely to be cited?** Quite a few practitioners support this, but it is still disputed.

**Does AI prefer text that "reads like AI wrote it" on every platform?** So far this has been verified on only a few engines.

**Do the weights in the hotel and paper experiments equal the weights in real AI search products?** Not necessarily. They show only what is possible at the level of mechanism.

**How large is the gap between "appearing" and "being recommended"?** Several practitioners' reports point the same way, but none has been independently verified, their definitions differ, and the numbers cannot be compared with each other.
