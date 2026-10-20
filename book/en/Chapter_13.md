# Chapter 13 — AI Knows You, So Why Doesn't It Recommend You?

> This is a case chapter. The earlier chapters explained the principles; this chapter covers things that really happened.
>
> Every story ends with a "What this shows" section, telling you which of the seven gates it got stuck at, and which chapter to go back to.
>
> Chapters used: Chapter 1 (AI's two sources of knowledge: memory and searching online), Chapter 2 (whether to search), Chapter 3 (whether it can get in the door), Chapter 4 (whether it can find you, including language and market), Chapter 5 (other people's word of mouth and the brand prior), Chapter 6 (whether it picks you), Chapter 7 (whether it mentions you, whether it actually uses you), Chapter 9 (rolling the dice and measurement), Chapter 10 (whether people come over), Chapter 11 (manipulation), Chapter 12 (every AI has different tastes). The role of community discussions as a source will be covered specifically in Chapter 15.

---

## First, imagine a scene

Imagine (this is a hypothetical scenario): An runs an online shop selling coffee beans. She has been doing it for many years, has lots of reviews, and is fairly well known among her peers.

One day she opens an AI assistant and asks: "Do you know An's Coffee?"

The AI answers fluently: what year it started, which origins it focuses on, what kind of taste it suits. It explains it more clearly than her new staff do.

She is very pleased, and then tries a different question: "Recommend a few online coffee bean shops that are good for beginners."

The answer lists five shops. She is not one of them.

She asks a few more times, in a few different ways. Still not there.

An cannot understand it: "But you clearly know me."

This chapter deals with exactly this problem: "It clearly knows you, but doesn't recommend you." This chapter tries to answer five questions:

1. When AI clearly "knows" a brand, why doesn't it recommend it in questions like "recommend an X"?
2. When a brand cannot get onto the recommendation list, which gate is it usually stuck at? How do you find out?
3. How much do third-party recommendation lists, review sites, business directories and community discussions affect recommendations? How hard is the evidence?
4. Does your official website still matter? In what situations does it matter?
5. How should you measure a brand's visibility so that you don't fool yourself?

---

## The big idea of this chapter: a recommendation is a multi-round knockout

When a user asks "What is the best X?", the AI does not go and look up a ready-made brand ranking.

It follows the path described in Chapter 1: a filtering process with random elements, split into several stages. It is very much like that **very busy librarian**: first deciding whether to search, then going to the shelves to pull a batch of material (the **shortlist**), picking a few pieces to read, and only then speaking up with a recommendation.

If your brand is knocked out at any gate, you will not be in the final answer. Applied to brand recommendations, the path roughly goes like this:

1. **What the question looks like**: Which category word was used? What situation was described? What kind of buyer did the person say they were?
2. **Whether to search** (triggering): the AI decides whether to search online or answer directly from memory.
3. **Whether it can find you** (retrieval): the material the AI pulls back is limited by category, language and market.
4. **Whose content is on the shortlist**: mainly third-party content written by others.
5. **Whether it can get in the door** (accessibility): the AI may walk into your official website to take a closer look, and at that point whether your website is readable matters a lot.
6. **Whether it picks you** (selection): the AI may name you and recommend you, or it may advise people not to choose you.
7. **Whether people come over** (user behavior): users click through, search for your brand name, or call you directly.

### Being recommended is not just a "yes" or "no" state

A brand can appear in an AI answer in at least five ways:

| State | In plain words | Common misunderstanding |
|---|---|---|
| Known | Ask about your name directly, and the AI can describe you correctly | Thinking "AI knows me" equals "AI will recommend me" |
| Cited | Your official website appears in the answer's source list | Thinking being listed as a source means being recommended |
| Named | The body of the answer mentions your name | It may just be listing you in passing, or even using you as a bad example |
| Recommended | The AI clearly advises choosing you | This is the state your business actually needs |
| Advised against | The AI clearly advises not choosing you | Most tracking reports don't record this at all |

These five states are often separate. You can be known but not named, and cited but not recommended. Most of the stories in this chapter are about how they come apart, and why.

There is also a harder-to-notice situation: you are listed, but compared with the other options, you are described more briefly and with more reservations. A large-scale experiment with real users found that in AI conversations, adding reservations to the other options or mentioning them in a single line was most strongly related to users switching to the promoted product (see Chapter 11). So besides recording which state you are in, also compare whether AI describes you and others on equal terms.

### First, lay out the four core principles

These four principles come from Chapters 5, 6 and 3. This chapter tests them against real cases.

1. **Real conditions that create a difference decide recommendations.** Ratings, price, reviews, specifications: these facts that make you different from others are what the AI uses to choose (Chapters 5 and 6).
2. **The brand prior only matters when "everyone looks the same".** The brand prior is the impression of a brand the AI remembers before it looks anything up. The advantage big brands get from this is most obvious when there is no difference between the candidates (Chapter 5).
3. **Other people's word of mouth is the evidence AI uses to judge.** The AI's answers about a brand are built mainly on what others say about you, not on what you say about yourself (Chapter 5).
4. **AI will walk into your official website to look.** Whether your website can be understood by AI decides whose content is used in the answer (Chapter 3).

---

## First, let's be clear: how hard is this evidence?

This chapter has a lot of stories, but the strength of the evidence varies a lot. Let's make this clear first:

| Conclusion | Where the evidence comes from | Strength and limits |
|---|---|---|
| When AI answers questions about brands, most of the sources it cites are other people's websites | Researchers tested repeatedly on real AI search, and the results of several large citation analyses agree | This describes a phenomenon; it does not prove cause and effect. The authors of several of the studies are themselves companies selling visibility services |
| "Knowing" is not the same as "recommending" | Researchers tested repeatedly on real AI search; in addition, many people in the industry have tested this themselves | The direction is consistent, but the specific numbers vary a lot with the sample |
| The more different sources mention the same brand, the more likely it is to be selected into the answer | Researchers tested repeatedly on real AI search (Chinese-language AI search) | Only a relationship of "appearing together"; the authors are a service provider |
| Whether your official website is easy for AI to read affects recommendations | Researchers tested repeatedly on real AI search (comparing matched pairs of similar businesses) | The authors used a scoring method they designed themselves; it is a bundled total score, without looking at each item separately |
| Working to get into third-party recommendation lists can increase recommendations | Only reports from people in the industry who tested it themselves | **No study has done an experiment that "deliberately changes one thing and sees whether the result changes"**; most cases have no control group, and did several things at the same time |
| Visibility must be measured many times, in multiple languages, and across multiple AI platforms together | Researchers tested repeatedly on real AI search, plus several industry tests with control groups | **This is the strongest evidence in this chapter** |
| Doing GEO can bring business results | One quasi-experiment using real user traffic (only one website); everything else is what people in the industry say themselves | The effect is much smaller than the raw numbers, and can only count as "there are signs" |

**The one thing you most need to remember from this chapter:** "Get third parties to write about you, and your recommendations will go up" is a very common view in the industry, and quite a few cases support it. But so far, it has only observational and before-and-after evidence; **it has not been verified by controlled experiments**. Many people in the industry believe it, but "many people believe it" does not mean "it is true".

> **A closer look: a few ways of describing evidence that this chapter uses often**
>
> - "Researchers tested repeatedly on real AI search and found...": systematic studies with larger samples.
> - "Someone in the industry tested this themselves, repeated many times, with a control group...": more careful practical tests, but no one has independently verified them.
> - "Someone in the industry tested this themselves...": practical reports, usually without a control group, and no one has independently verified them.
> - "Someone in the industry observed...": personal observation, the weakest kind.
> - "Before-and-after comparison": only compares before doing something and after doing it, with no control group from the same period that "did nothing". This kind of comparison makes it very easy to mistake outside changes for your own achievement.

---

## Story group 1: AI knows you, but doesn't think of you

This group corresponds to Chapter 2 (whether to search), Chapter 5 (knowing is not recommending), and Chapter 1 (AI has two sources of knowledge: what it memorised during training, and what it finds online).

### Story 1: The "discovery gap" for new products

Researchers tested a batch of newly launched products repeatedly on real AI search.

When asked directly by product name, the AI recognised almost all of them: the recognition rate on one AI platform was 99.4%, and on another it was 94.3%.

But when switched to "find me an X" questions that ask only about the category, without mentioning the brand name, the share of answers these products appeared in dropped to just 3.32% and 8.29%. That is a gap of 30 times and 11 times.

The researchers also found two things:

- The overall GEO score of these products' official websites had almost no relationship with visibility (a correlation coefficient of about -0.1, close to zero, meaning "no visible relationship").
- On AI platforms that search online, visibility rose together with "how many other websites link to you" and "how many times you are mentioned in communities". This is only a relationship of appearing together; it does not mean cause and effect.

What to discount: the study only tested through the developer interface (API), not the chat screen that ordinary consumers use.

**What this shows:** A brand existing in the AI's memory does not mean it will be "thought of" in category questions. This is stuck at gate 3, "whether it can find you" (Chapter 4), and the root cause is what Chapter 5 described: "knowing is not recommending".

### Story 2: Even category leaders were not named

Someone in the industry tested this themselves: they checked 2,475 US brands. These brands were all category leaders, selected by number of reviews.

In category questions without a brand name, 86% of the e-commerce brands **did not appear even once** across four AI assistants.

Yet when asked directly by brand name, all four AI assistants could state these brands' founding year, product lines and positioning.

Another person in the industry also tested this (repeated many times, with a control group), using questions like "find me an executive coach":

- The best-known coach in the industry appeared only 1 time in 6 queries.
- Another coach with a huge audience also appeared only 1 time.
- But when asked directly who this coach is, two AI platforms both gave a detailed and accurate introduction.

Yet another person in the industry tested (repeated many times, with a control group) 20 Indian startups. These companies had all raised their first formal round of venture capital (Series A) or a later round.

- 17 were completely absent from category questions.
- When asked directly by brand name, most of them were answered normally.
- The 3 that appeared had things in common: community discussions, clearly structured comparison pages, and structured data markup for reviews.

What to discount: these are all observations; they did not prove that "doing something" can change the result.

**What this shows:** Fame, funding and number of reviews do not automatically turn into recommendations. AI recommends "brands that have evidence supporting them in the context of this question". This is stuck at gate 3, "whether it can find you", and gate 4, "whether it picks you" (Chapters 4, 5 and 6).

### Story 3: The closer a question is to a purchase, the less ChatGPT searches online

Someone in the industry tested this themselves: through the developer interface, they turned on the search tool and let the AI decide for itself whether to search online. The results:

- Comparison questions like "which is better, brand A or brand B": ChatGPT did **not** search online in 76 out of 80 times.
- Situation questions like "I have a certain condition, which one should I buy": it did not search online in 106 out of 120 times.
- Broad category questions: it searched online about half the time.
- Gemini searched 493 times out of 500. Perplexity searched all 500 times.
- Answers that did not search online cited zero sources.

What to discount: this was a developer interface test. The author believes the products that ordinary consumers use make the same decision, but this has not been directly verified.

**What this shows:** This is stuck at gate 1, "whether to search" (Chapter 2). The most crucial comparison questions may be answered entirely from the AI's memory. At that point, no matter how good your official website is, it cannot be used. What decides the result is how much presence your brand has in the material the AI read during training.

### Story 4: Many buyers' questions don't name any brand at all

Three observations all point to the same thing:

- Someone in the industry tested this themselves: they compiled 300 buyer questions about field service software. For questions describing a problem, like "how can I stop losing work orders", most AI platforms only gave general advice and did not recommend any product.
- Someone in the industry tested this themselves: in Romania, they asked 18 book-buying questions in Romanian, running two rounds. 58% of the answers did not recommend any bookshop or publisher; the market leader appeared in only about one fifth of the answers.
- Someone in the industry observed: out of 60 real buyer questions collected from forums and the "related questions" on search pages, 13 in one round and 23 in another round did not name any brand.

**What this shows:** Before you start tracking a question, first confirm that the question "names brands". For a question that never names any brand, no matter how long you track it, you will not prove anything. This relates to measurement, covered in Chapter 9: if you measure the wrong thing, however good the numbers look, they are useless.

---

## Story group 2: Ask a different way, and you disappear

This group corresponds to Chapter 4 (whether it can find you: how AI rewrites questions, how language and market limit the scope), and Chapter 6 (AI first looks at "is it relevant", before anything else).

### Story 5: From "there every time" to "not there even once"

Someone in the industry tested this themselves (repeated many times, with a control group), on team email tools of the "shared inbox" type.

First, asking with the broad category word, the two main brands were named almost every time on four AI platforms.

Then they switched to the wording real users would use: not saying the category name, but describing the workflow they wanted. Each platform was asked 10 times:

| AI platform | Brand A | Brand B |
|---|---|---|
| ChatGPT | 9 out of 10 times | 0 out of 10 times |
| Claude | 5 out of 10 times | 8 out of 10 times |
| Gemini | 10 out of 10 times | 8 out of 10 times |
| Perplexity | 0 out of 10 times | 5 out of 10 times |

The same company, the same website; only the way of asking changed.

The two other control brands tracked at the same time had roughly stable results, only loosening somewhat on Perplexity.

The author's guess is: a brand's "footprint" outside its official website (how others mention you) decides whether you can get onto the shortlist; whether your official website uses the buyer's language to describe "what it actually helps people get done" decides whether you can stay on the list when the question changes. The author also says he could not cleanly separate these two factors.

Another person in the industry also tested (repeated many times, with a control group) a newsletter platform. It appeared only in questions like "a creator wants to start a newsletter and make money".

When the buyer was changed to a business and the same thing was described in plain language, its appearances dropped to 0 out of 40 times.

What it "owns" is not a keyword, but a certain type of buyer.

**What this shows:** This is stuck at gate 3, "whether it can find you" (Chapter 4). When AI pulls material, it looks at the meaning and intent of the question, not at the brand itself. Which kind of question and which kind of buyer your brand is tied to decides where you can be seen.

### Story 6: Put into the wrong category by AI

Someone in the industry tested this themselves (repeated many times, with a control group): a CSV file import tool appeared only 1 time in 8 purchase conversations.

And when it did appear, it was described as a data moving and transformation tool (called an ETL tool in the industry), which it actually is not.

Worse, two AI models simply switched to describing a competitor, with wording clearly taken from the competitor's own marketing copy.

What the team did: they found the specific questions where AI named the competitor but not themselves, and for those questions they published two comparison articles and one page of technical documentation, and rewrote the documentation of their code project.

10 days later, appearances rose to 5 out of 8 times. Of the four AI platforms, three no longer put it in the wrong category.

What to discount: the author himself builds measurement tools, and he himself also stated that the results should be discounted; the sample was only 8 questions.

Similar things have also happened:

- Someone in the industry observed: an agency searched using the name of its best-known niche service, and was named 19 out of 25 times; searching with the two broad category labels written on its homepage, both gave 0 out of 25 times.
- Someone in the industry observed: calling the same category by a different name can make the share of times a brand is mentioned drop from about three quarters to zero.
- Someone in the industry observed: when testing three Australian law firms, AI put them into categories much narrower than expected, for example "employment law firm", rather than "lawyer".

**What this shows:** Being put in the wrong category happens at the "understanding" stage before "pulling material", that is, how the AI sees you as an **entity**. If AI puts you in the wrong category, you will be compared with the wrong rivals, or never get onto the shortlist at all. This is stuck at gate 3, "whether it can find you" (Chapter 4).

### Story 7: Broad questions are filled up by big brands; niche questions still have room

Someone in the industry tested this themselves: a business-to-business client was completely invisible in broad questions like "best laser marking machine brands in India".

But in niche questions like "which type of printer should I use for metal marking", it ranked first and was cited. The pages had not been changed at all.

The clients that were cited had one thing in common: the AI would repeat specific details from their pages, such as specific equipment models. Pages that were written only in category language, without specific details, did not get cited.

**What this shows:** Broad questions and niche questions are actually two different contests. This relates to gate 3, "whether it can find you" (Chapter 4), and gate 4, "whether it picks you" (Chapter 6): specific facts give AI something it can use.

### Story 8: Write the city into the question, rather than only setting the location

Someone in the industry tested this themselves (repeated many times, with a control group): a logistics company provides services in about 8 cities in India.

Searching with 41 buyer questions, it was not named even once.

- Setting the AI's location to Bhopal, then asking general questions: 0 out of 3 times.
- Writing "in Bhopal" directly into the question sentence: Gemini named it 3 out of 3 times.
- Google's AI Overviews also named it in two cities, Bhopal and Coimbatore.

The author points out: it was only named in places where the company had a corresponding city page.

What to discount: the author works on visibility tools, which he has disclosed himself.

**What this shows:** The location setting mainly affects ranking. But a place name written into the question sentence changes "what this question is asking", and so changes which material the AI pulls back. This is stuck at gate 3, "whether it can find you" (Chapter 4).

### Story 9: Language and market are a door

Researchers tested repeatedly on real AI search and found:

- Across 12 European languages, switching to the language of the brand's own country to ask raised the recommendation share of local leading brands by 0.80, while global brands rose by only 0.15.
- When asking in the local language, global suppliers appeared only 1 time in 24.
- Asking in English in Istanbul and Tallinn, local suppliers appeared 0 times in 12.
- Asking in Turkish, but from a Berlin network address, gave German suppliers (5 out of 6 times).
- In other words: the language used to ask decides who is on the shortlist; the country the connection is from decides which country's market it is. This part tested only one model, and the sample was small.
- AI's tone of liking or disliking a brand also changes with language: the same batch of brands got the most negative assessments in English.

Someone in the industry tested this themselves (repeated many times, with a control group): the same model, the same question, only telling the AI where the user was, and a brand went from completely absent to being named 5 out of 6 times.

Someone else in the industry tested this themselves: they asked 10 AI models the same "recommend jewellery brands" question in Romanian.

- They got 29 different brands in total.
- 19 of these were mentioned by only one model.
- Between any two models, the recommendations overlapped by only about 18% on average.
- One model had no overlap at all with the other nine.

**What this shows:** This is stuck at gate 3, "whether it can find you" (the language and market gate described in Chapter 4), and also echoes Chapter 12, "every AI has its own tastes". Testing a local market only in English will systematically underestimate local brands.

---

## Story group 3: AI listens to other people's word of mouth

This group corresponds to Chapter 5: AI's answers are built mainly on third-party sources, and it gives great weight to "many sources say so".

### Story 10: Official websites make up only a small share of citations

Several groups counted whom AI cited when answering questions about brands. The results were as follows:

| Finding | Strength of evidence |
|---|---|
| Out of 167,551 citations in total, across 128 brands and 13 languages, third-party websites made up 85.7%, and brands' own websites only 14.3%. 80% of citations were concentrated on about 18.2% of domains. In 11 of the 12 languages, Wikipedia was the most cited website. | Researchers tested repeatedly on real AI search (the authors are a service provider) |
| Out of 149,912 citations in total, across 102 brands, brands' own websites made up only 2.9%, and pages of other businesses in the same field made up 75.2%. Recommendation-list pages made up 21.0% of all citations, and 35.7% of "content-type" citations. | Researchers tested repeatedly on real AI search (a service provider's actual operating records; observational) |
| In "ranking" questions, AI strongly favoured third-party media: in AI answers for the US car category, third-party media made up 81.9%, and community sources 0. In Google search results for the same kind of question, these two figures were 45.1% and 15.4% respectively. | Researchers tested repeatedly on real AI search |
| In answers that searched online, out of 2,410 citations, the websites of all the tracked vendors combined made up only 7.3%, and each vendor on its own was under 1%. | Someone in the industry tested this themselves (repeated many times, with a control group); the author clearly states this is only a distribution, with no evidence of cause and effect |
| In 510 Turkish hotel questions, 98% of Google AI Mode's answers cited at least one booking platform; the largest booking platform appeared in 74% of answers; hotels' own official websites were almost never cited. | Someone in the industry tested this themselves |
| Out of 1,783 citations in total, across 180 sneaker recommendation answers, the top ones were video platforms, review sites and fashion media. The official website of the most recommended brand was cited only 2 times. Perplexity cited brands' official websites zero times. | Someone in the industry tested this themselves |

**What this shows:** AI's "view" of a brand is mainly pieced together from other people's pages. A brand being recommended most often does not mean its official website is the basis for it. This corresponds to the source material behind gate 4, "whether it picks you", and gate 5, "whether it mentions you" (Chapter 5).

### Story 11: The more places mention you, the easier it is to be written into the answer

Researchers tested repeatedly on Chinese-language AI search and found:

- Of the brands that appeared in the material AI cited, only 8.3% were actually written into the body of the answer.
- If a brand appeared in only 1 cited source, the share selected into the answer was 2.1%.
- If it appeared in 11 or more sources, this share was 59.9%.
- In the model predicting "who will be selected", the importance of traditional SEO quality scores was only 4.52%.
- Of the sources listed, 66% had content that actually made it into the body of the answer, 30% were substantively cited, and 8% were cited in depth. Chapters 7 and 12 explain more.

What to discount: this is a relationship of "appearing together", not an experiment in which someone deliberately changed something. It shows that "brands mentioned in many places are selected more often", but it does not prove that "posting in many places will get you selected".

**What this shows:** This is what the librarian looks like when it "especially trusts what many people say". It happens at gate 4, "whether it picks you", and gate 6, "whether it actually uses you" (Chapters 5 and 7).

### Story 12: Squeezing into the recommendation lists AI is already citing (before-and-after comparison)

The cases below all use the same playbook: first find the pages AI repeatedly cites when answering the target questions, then find ways to get your own brand onto those pages.

**Case 1: a cannabis consumer brand.** The team contacted every website that had appeared in the target questions, trying to get added to existing articles; where they couldn't get added, they wrote guest articles. For a question about sleep products, they did 5 recommendation lists and 2 product roundups. Within about a week, ChatGPT ranked this brand in 2nd place.

What to discount: this is a report from someone in the industry who tested it themselves; the author was responsible only for off-site links, and this client's website already had strong SEO to begin with.

**Case 2: a new energy drink brand.** The team found that Google's AI Overviews repeatedly cited 3 to 4 "best X drinks" review blogs, so they worked to get included in them. Within a few days, the brand appeared alongside big brands in AI Overviews and on the first page of search results. This is a report from someone in the industry who tested it themselves.

**Case 3: 12 client pages.** The team first did everything that could be done on the website itself: structured data, heading levels, making it clear to AI "which entity this is", and internal links on the site. Two weeks later, they tracked with 15 prompts, in a logged-out state.

There was no change at all within two weeks. In the third week, a roundup article comparing this client with four competitors was published. Within a few days, two pages that had not been visible before started being cited.

What to discount: this is a report from someone in the industry who tested it themselves; the author himself says the sample was small, and there was no way to separate which cause it was.

**Case 4: a warehouse management software company** (specialising in the small field of third-party logistics). Every month they recorded 40 recommendation-type questions: ChatGPT named them only 2 to 4 times, while a competitor on the second page of Google search was named about 18 times.

What did the competitor have? Two recommendation lists on logistics blogs, a category page on a review platform, and a three-year-old positive community post.

This company did two things: unified the contradictory company descriptions on three platforms, and published one comparison page every day. By August, it had become about 9 out of 40 times.

What to discount: someone in the industry tested this themselves (repeated many times, with a control group); the two things were done at the same time, so their separate effects cannot be separated.

The same company also added a few observations (a report from someone in the industry who tested it themselves):

- Citations came mainly from review platforms, other people's recommendation lists and one community discussion thread.
- The official website was cited only when someone asked about "price" and "what software it integrates with", and almost never when asked "which one should I choose".
- 200 posts on a professional social network in a year brought zero citations.
- Spending 6,000 US dollars to upgrade their profile on a review platform made no difference.
- Instead, it was the membership directory of an industry association that got cited by Perplexity.

**Case 5: service provider directories.** The team recorded the directory websites each AI cited when answering industry questions, then created and filled out profiles on these directories, and asked clients to leave reviews. Within a month, they went from zero citations to being cited in 3 of 5 AIs and 6 of 10 prompts. This is a report from someone in the industry who tested it themselves.

What to discount (this applies to this whole group):

1. **All of these are before-and-after comparisons, with no control group from the same period.** The quasi-experiment in Chapter 10 shows: if you don't subtract the growth of the AI platforms themselves, the raw multiples will seriously overestimate the effect.
2. **Borrowed exposure is not stable.** Someone in the industry observed: if your appearance depends on other people's recommendation lists, the day they update their page, you may disappear. Citations of your own documentation or pricing page are more stable.
3. **Paying for a spot on a recommendation list, or trading guest articles for links**, may break the rules on some platforms, and also falls into the grey area discussed in Chapter 11.

**What this shows:** AI's answers are pieced together from "pages that are already on the shortlist". Squeezing onto those pages is the same as squeezing directly onto the shortlist. This corresponds to gate 3, "whether it can find you" (Chapters 4 and 5). But remember: so far this playbook is supported only by industry cases, with no controlled experiments.

### Story 13: Consistent descriptions matter more than a large quantity (this part is mostly opinion)

- Someone in the industry tested this themselves: a company used a fixed set of questions every month to check how each AI described it. Twice it found wrong information, traced respectively to an outdated directory profile and a third-party article that had got things wrong.
- Someone in the industry tested this themselves: tracking three competitors' descriptions for six weeks in a row, two of them clearly changed. One went from "analytics tool" to "AI visibility platform"; the other gained a line of criticism, "limited integration capabilities". Neither change came from content the competitors published themselves; they were traced to comparison discussions in small niche communities, and a few forum comments with a lot of engagement.
- Someone in the industry tested this themselves: brands whose product information was consistent and complete across different retail channels had clearly higher citation rates. But the author admits that cause and effect have not been verified, and there was no control group from the same period.
- Someone in the industry observed: changing the official website's "About us" page and all third-party profiles to exactly the same description was the single change with the largest effect, and about three months later it started being cited consistently.

**What this shows:** AI's impression of you is pieced together from many places. If each piece of the puzzle says something different, the AI may put it together wrong. This relates to "many sources say so" in Chapter 5, and also to gate 6, "whether it uses it correctly" (Chapter 7).

### Story 14: Mass-distributing press releases doesn't work

Someone in the industry tested this themselves (repeated many times, with a control group): on 4 AI platforms, they compared AI startups that had already raised funding with long-established big companies.

- The startups' citation rate was 6% to 13%; the big companies' was 32% to 62%.
- Sending out press releases and getting financial websites to republish them didn't help; on Perplexity it even had a slightly negative effect.
- Only the startups making vector databases reached 34%. The author thinks the reason is: this kind of product has been written about by tech blogs for years, and has already made it into the material AI read during training.

Later, this report was questioned, and the author corrected two points:

1. Each round was actually 5,400 trials, not the 46,122 queries stated in the headline.
2. A more accurate way to put it would be: "AI cites entities that are well represented in its training data and that have authoritative sources that can be found by search; startups lack both", rather than "big companies have the advantage".

This correction is itself a lesson in measurement (Story group 7 later will come back to this).

**What this shows:** What decides citations is not how many press releases you send out, but whether you are in the AI's memory (the brand prior from Chapter 1, Chapter 5), and whether there are credible sources online that can be found by search (gate 3, "whether it can find you", Chapter 4).

---

## Story group 4: When your official website has the final say

This group corresponds to Chapter 3 (whether it can get in the door), and Chapter 1 (AI really does open web pages and read them).

### Story 15: Once AI walks into your website, how readable it is decides whose content the answer uses

Researchers tested repeatedly on real AI search: they had AI that goes into websites and reads them by itself browse the websites of 1,056 businesses, running 37,927 visits in total.

- For websites friendly to this kind of AI, 78% of the answer's content came from the business's own pages; for unfriendly websites it was 58%.
- Friendly websites were clearly recommended 20% of the time; unfriendly ones 11%.
- After controlling for the factor of "how readable the website is", the two measures representing "how much you are mentioned off-site" had **no** clear independent effect on "how much of the business's own page content the answer used", "whether it was recommended" or "how much it cost the AI".
- When the website could not be read, the AI switched to third-party or competitor content. The way it failed was **by leaving you out**, not by making things up.
- The knowledge the AI memorised during training made up only 7% to 10% of the final answer.

What to discount: the authors are a service provider using their own scoring method; it is an observational study of matched comparisons. "How readable" is a bundled total score, including: content visible without relying on JavaScript, having structured data, having a plain-text (Markdown) backup version for machines to read, and crawler settings not blocking this kind of AI. This total score did not look at the effect of each item separately.

**What this shows:** This is gate 2, "whether it can get in the door" (Chapter 3). When AI arrives at your door and the door won't open, it turns around and asks your neighbours and rivals.

### Story 16: When the official website is pulled, the brand is almost always mentioned

Someone in the industry tested this themselves (repeated many times, with a control group): in shopping recommendation answers for several brands,

- When the brand's official website was pulled by the AI, the brand was mentioned 89% of the time.
- When the official website was not pulled, only 24%.

Another finding: of 165 citations of one brand's own website, 116 came from blog articles and only 3 from product pages; a single roundup article on its own was cited 37 times.

The author also mentions: when the same questions were rerun, about a quarter of the results changed.

**What this shows:** The same visibility score can hide completely different problems: it may never have been pulled at all, it may have been pulled but not recommended, the AI may have understood only part of your product line, or the question itself may rarely name brands. This involves gate 3, "whether it can find you" (Chapter 4), and measurement in Chapter 9.

### Story 17: Building a clean version just for AI

Someone in the industry tested this themselves (repeated many times, with a control group): a small, not very well-known app was originally cited by several AIs, but the descriptions were wrong; even the most basic way the product works was described wrongly.

The founder made a "parallel version" of the website:

- Removed distractions like menus, animations and cookie consent banners.
- Wrote every page as a direct question and answer, with the answer placed within the first 75 to 120 words of the page.
- Used a technical tag on every page to tell search engines "the official version is the original page" (called canonical in the industry), to avoid being treated as duplicate content.
- Also provided a sitemap, and then used an llms.txt file and a "there is an alternative version here" tag (rel="alternate") so that AI could find this version.

Within 5 weeks, the coverage of AI citations expanded by 12%, and traffic from AI rose by 60%. No new off-site links were added during this period.

What to discount: the author is the product's founder, which he has disclosed; several methods were done together, so it's impossible to tell which one worked; so far, **there is no evidence that llms.txt works on its own** (Chapter 3).

**What this shows:** This is gate 2, "whether it can get in the door" (Chapter 3), and gate 6, "whether it uses it correctly" (Chapter 7): make it easy for AI to read, and it is more likely to describe you correctly.

### Story 18: The website itself was all done right, and it still didn't help

Someone in the industry tested this themselves: a company was named about 6% of the time in ChatGPT questions like "who can do X".

The website check came back clean, and all crawlers could read it normally (the server always responded "200", meaning "the door is open as normal"). But after making the fixes on the website, nothing changed.

Someone suggested using a comparison to work out where the problem is:

- It doesn't appear even with **the online search function turned off**: what's missing is the AI's memory from training.
- It only appears with **the online search function turned on**: it relies on real-time search, and here the lever is those roundup articles.

The person who made the suggestion said he had scored about 180 companies: the ones that got named were companies that often appeared in "X vs Y" type articles, not the companies with the cleanest websites.

Another person in the industry also tested this: a company ranked on the first page of Google search, but ChatGPT did not name it even once for the same question; a competitor ranked lower than it was named three times instead.

**What this shows:** The door being open (gate 2, Chapter 3) does not mean you will appear on the shelf. The problem may be at gate 1, "whether to search" (Chapter 2), or at gate 3, "whether it can find you" (Chapters 4 and 5).

### Story 19: What your official website controls is "how AI describes you"

Someone in the industry tested this themselves: a GEO agency with only a business profile and a homepage was still named by ChatGPT.

The author searched in 19 cities and recorded 94 agencies:

- 97% of the agencies' official websites were cited.
- Business profiles being cited was a phenomenon specific to India: 86% in major Indian cities, 18% in other regions.
- **For agencies without a dedicated service page, ChatGPT was guessing what they did 66% of the time; for those with a dedicated page, the guessing was zero.**

What to discount: only one question and one model were used; the author's own agency was also in the sample.

**What this shows:** A profile can get you named, but only a dedicated page can control how AI talks about you. This is gate 6, "whether it uses it correctly" (Chapter 7).

---

## Story group 5: Cited, but someone else got recommended

This group corresponds to Chapter 6 (whether it picks you) and Chapter 7 (being listed does not mean being used, let alone being used correctly).

### Story 20: Being cited and being recommended are two different things

Someone in the industry tested this themselves (repeated many times, with a control group): for the same client, they ran 134 fixed questions every week.

- Within six weeks, the share of times ChatGPT proactively recommended this client rose from 11.9% to 23.1%, an increase of 11.2 percentage points. Of these, 24 questions improved and 9 questions got worse. Over the same period, Claude actually fell by 4.1 percentage points.
- Google listed this client's website as a source in 36% of answers, but recommended the brand 0% of the time. Specifically: out of 538 answers, cited 194 times, recommended 0 times.
- Claude copied up to 64 consecutive words from the client's article word for word, with the web address attached; but the recommendation list was compiled from competitors' official websites. **It takes the description from you, and the list from others.**
- Before doing anything, they first measured the "noise floor": 387 questions were rerun 3 days later, and 98% of the results were the same. So they treated any change below 3 to 4 percentage points as error from the measurement itself.
- What they did was publish 458 separate topic pages (plain HTML, not relying on JavaScript), rather than rewriting pages that already had rankings. Of one batch of 110, about 50% to 55% were indexed by Google within 5 days, but AI citations appeared several weeks later than indexing.

Other data pointing the same way:

- Someone in the industry tested this themselves: across 76 companies and about 1,140 prompts, brands were mentioned in 44% of answers on average, but recommended in only 10%.
- Someone in the industry tested this themselves: in about 26,400 answers about brands, the brand appeared in only about 16%; citations with a link made up about 13%, and mentions of just the name, without a link, about 3%. ChatGPT had the lowest share of citations with a link (under 10%), but the highest share of "mentioning only the name, without giving a link".
- Someone in the industry observed: of 85 enterprise software companies, 29.4% were cited more times than they were named; for 9 of them, the official website appeared in the citation list, yet they were not named in any answer.

**What this shows:** This is the separation of gate 5, "whether it mentions you", from gate 4, "whether it picks you" (Chapters 6 and 7). Being listed as a source may just mean supplying material for someone else's recommendation.

### Story 21: Your sentences, under someone else's name

Someone in the industry observed: a travel guide page written by a small cycling tour operator was used by AI as a main source.

But the answer named and recommended three or four competitors with prices attached. One of the recommendation sentences was taken almost word for word from this operator's own page.

The reason was the way it was written: on this operator's page, the brand name was not next to the key sentences; the competitors put the brand name, facts and numbers in the same sentence.

Another person in the industry also observed: a company's official website had a passage that roughly said, "We may not be right for everyone; here are 5 trustworthy competitors." Perplexity used this list directly to produce recommendations. This company's official website was cited as many as 4 times, but its own brand was not in the recommendations.

**What this shows:** This is gate 6, "whether it actually uses you, whether it uses it correctly" (Chapter 7). AI extracts "passages that list a string of brands", and "sentences where the brand and facts sit right next to each other". If the brand name is too far from the facts, the facts may end up attached to someone else's name.

### Story 22: Specific facts get cited; vague copy gets skipped

- Someone in the industry tested this themselves: when searching for "AI search optimisation services" in Perth, every agency that got named had its information taken from its own service page. Those whose pages stated real prices were cited; those that only said "feel free to contact us" were skipped.
- Someone in the industry tested this themselves: a clinic in London that ranked first on Google search had zero citations on three AI platforms. A competitor with average rankings was recommended about 70% of the time. The difference: the competitor had named doctor profiles, a dedicated page for every service, and real third-party mentions.
- Someone in the industry observed: clinics that listed specific equipment models on their pages were quoted word for word by AI.

**What this shows:** This is gate 4, "whether it picks you", and gate 6, "whether it actually uses you" (Chapters 6 and 7). AI needs specific facts it can use; vague adjectives don't help.

### Story 23: As soon as buyers describe themselves, AI starts "advising against"

Someone in the industry tested this themselves (repeated many times, with a control group): they asked five purchase questions about healthy snacks, opening a brand-new incognito window every time.

- When only the question was asked, 2 out of 50 answers clearly told people to avoid a certain brand.
- After adding a description of the buyer (cutting fat, tracking nutrients, reading ingredient lists, not caring about price), it became 20.
- The same brand was recommended in one conversation and advised against in another.

Researchers tested repeatedly on real AI search and also found: in product recommendations, 79% of ChatGPT's answers recommended in the first person (for example, "If I could only buy one, I would..."); for Gemini it was 7%, and for Google's AI Overviews 2%.

**What this shows:** This is gate 4, "whether it picks you" (Chapter 6). Once there are specific criteria for judging, the AI screens by the product's conditions, brands can be ranked against one another, and the brand prior falls back to being secondary. This is what "real conditions that create a difference decide recommendations" looks like in practice. In practice: besides tracking "being recommended", also track "being advised against".

### Story 24: The challenger won first in the AI's memory

Someone in the industry tested this themselves: a large beverage company launched a new prebiotic cola. In 6 simulated AI shopping processes, 4 times it was replaced in the first round by a challenger brand.

The author's interpretation is: during the period when the AI was trained, the challenger brand had already taken over the relevant material online; the big brand that arrived late, however famous, couldn't catch up. Buying ad placements inside the AI platform afterwards also couldn't change the preference the AI had already formed.

What to discount: a sample of 6 times is very small; the author used his own scoring method; "ads can't rescue it" is only an inference and was not actually tested.

**What this shows:** This relates to gate 1, "whether to search" (Chapter 2), and the brand prior in Chapter 5: when AI answers from memory, whoever got a firm footing first in the material it read has the advantage.

---

## Story group 6: Local businesses, a different set of rules

This group corresponds to Chapter 4 (differences between AIs), Chapter 5 (other people's word of mouth) and Chapter 3 (how readable your official website is). The situation for local businesses is clearly different from national brands, and is worth looking at separately.

### Story 25: Ranking well on the map, but invisible in AI

- **Someone in the industry tested this themselves:** across 8 US cities and 6 categories, 48 markets in total, they took the roughly 97 businesses returned by map search in each market.
  - Only 11.9% were named by at least one of four AI systems.
  - Of 4,657 businesses, Google's AI Overviews named 376, ChatGPT 206, Gemini 134, and Claude 92.
  - Of the businesses that were named, 70% appeared in only one system. In 36 of the 48 markets, not a single business was named by all four systems at once.
  - The differences between categories were larger than the differences between cities: gyms 14.4%, coffee shops 14.1%, hair salons 9.7%.
  - This was counted using "exact name match"; with a looser matching standard, the share was 26%.
- **Someone in the industry tested this themselves (repeated many times, with a control group):** in 15 cities, they searched 45 times using 3 "emergency plumbing and electrical repair" questions, then reran them in incognito windows.
  - Google switched who it recommended in about 40% of cities; for ChatGPT, about two thirds of the names were repeated; for Perplexity, about 85% stayed the same.
  - One national chain brand took about half of the answers under all conditions.
  - The consistent winners were chains that inherited national fame, or local shops that happened to have built up reviews on platforms AI reads.
- **Someone in the industry tested this themselves:** across 48 combinations of city and niche industry, recording daily, 9,217 answers in total.
  - In 25 of 36 local lists, the same business appeared on more than 80% of days.
  - For businesses named by Perplexity and Gemini for the same question, the median overlap was only 11%.
  - What Perplexity cited was mainly the businesses' own pages, plus a few directory websites.
- **Someone in the industry tested this themselves:** 197 clinics in the same industry, 3 AI platforms, each question run 3 times.
  - The citation overlap between different platforms was only 39% to 48%.
  - The factor most related to being cited was "whether it has its own website"; next was structured data specific to this industry, rather than generic markup automatically generated by plugins.
- **Someone in the industry tested this themselves:** 20 logged-out tests were done in Perth.
  - Broad questions like "best X in Perth" are basically a contest of reviews: AI reads the businesses on the map with the most reviews and the longest time in operation.
  - For questions about niche services, AI takes the answer directly from the businesses' service pages.
- **Someone in the industry tested this themselves:** checking more than 400 local businesses, 72% ranked fairly well on the map but did not appear in AI answers. The author says that a business's structured data, FAQ structured data, and whether the name, address and phone number are consistent everywhere predict appearing better than map ranking does; but the author has not published his method.
- **Someone in the industry tested this themselves:** of 1,444 businesses in Charleston, only 241 had ever been named and recommended by AI; 83% had never appeared.
- **Someone in the industry tested this themselves:** of 33 local service businesses, 76% had zero citations on all AI platforms; 67% had inconsistent name, address and phone number. It was also observed that on the day of the review, the AI Overviews for most home service categories in one city were systematically turned off and not shown.

**What this shows:** In local questions, map ranking and being named by AI are two different sets of signals. Unlike national brands, **local businesses' official websites and service pages carry clearly more weight in AI citations**. Directory websites, review platforms, and whether the name, address and phone number are consistent are also often mentioned. This involves gate 2, "whether it can get in the door" (Chapter 3), gate 3, "whether it can find you" (Chapter 4), and "every AI has different tastes" from Chapter 12.

**Don't do this:** Someone in the industry tested this themselves and found that stuffing the service items in a business profile with city names and the word "near me" (for example, a dozen or so variations of "city name + service") may be treated as a spam signal. This is only one reviewer's observation, but it points in the same direction as Chapter 11's analysis of manipulation tactics.

---

## Story group 7: Measure it wrong, and it's all for nothing

This group corresponds to Chapter 9: visibility is a distribution, not a ranking. Remember **rolling the dice**: ask the same question ten times, and the answers may be different.

### Story 26: What you see on your own account is not what others see

Someone in the industry tested this themselves: someone claimed that within a week his new website was being cited by ChatGPT in highly competitive category questions.

Another person in the industry tested it with 20 clean accounts, through connection addresses on ordinary home networks, and the brand did not appear at all. What appeared was ChatGPT's set of default statements about "new companies". The original author had been misled by his own conversation history.

Still, the original author's observation itself is valuable: when ChatGPT answers broad category questions, it splits the question into several smaller questions and searches them separately (**query fan-out**), and these smaller questions already contain the names of a few well-known brands. In other words, the shortlist is already partly decided before the search even begins (Chapter 4). The original author also admits: being cited is not the same as being recommended.

Another example (a report from someone in the industry who tested it themselves): the tracking report showed the brand's coverage was 45%, but when the client spot-checked it themselves, they could not see their own brand at all.

**What this shows:** Your conversation history and location will make you see results that others don't see (Chapter 9).

### Story 27: A single result is a roll of the dice

| Finding | Strength of evidence |
|---|---|
| Testing daily on four AI platforms for 45 days in a row, plus repeating 10 times on the same day: between two consecutive days, the overlap of cited sources was only 0.336 to 0.423 (1 means exactly the same, 0 means completely different); repeating on the same day, the differences were about the same as the next day. 57.8% of ChatGPT's answers had no citations at all. It is recommended to run each question at least 7 times a day (at least 8 times if you want to look at cited sources), and to look at it over a rolling window of 2 to 4 weeks. | Researchers tested repeatedly on real AI search |
| Asking the same question 6 times in a row: for 4 of the 6 questions, the first recommendation changed. | Researchers tested repeatedly on real AI search (small sample) |
| Whether a brand is mentioned is close to a "yes or no" matter: 63.2% of test combinations never mentioned it, and only 6.8% flipped back and forth. But the AI's tone of liking or disliking a brand flipped 6.7 times as often as "whether it was mentioned". To make "whether it is mentioned" stable, you need at least 3 runs; to make the tone of liking or disliking stable, you need at least 10 questions. | Researchers tested repeatedly on real AI search (the authors are a service provider) |
| Run 10 times, appear 4 times, and it looks like "40%". But statistically, the true share probably falls somewhere between 12% and 74%. | Someone in the industry tested this themselves |
| The same buyer question, run 10 times on the same AI platform, swung between scores of 50% and 80%; Gemini recommended this brand exactly 5 out of 10 times. | Someone in the industry tested this themselves (the author himself sells visibility tools) |

**What this shows:** A single screenshot proves nothing. What you need to look at is the **mention rate**, that is, "how many times out of ten it appears", and you need to know how large the error of that number itself is (Chapter 9).

### Story 28: Widening the range is more useful than repeating over and over

Researchers tested repeatedly on real AI search, breaking down "why one brand answer comes out differently":

- The language used to ask explained 26.5% of the difference.
- The brand itself explained only 1.5%.
- After running the same question 5 times, running it 5 more times barely reduced the error any further.
- Adding 3 more languages instead was about 15 times as effective as "running it 5 more times" (this result was calculated using the "tone of liking or disliking" measure).

**What this shows:** Rather than asking the same sentence a hundred times, change the language, change the AI platform, change the way of asking. Chapter 9 explains more.

### Story 29: Different AIs, different versions, different interfaces all need to be looked at separately

- Researchers tested repeatedly on real AI search: the chat screen used by ordinary consumers and the developer interface overlapped in cited domains by only 12.0% (ChatGPT) and 14.8% (Gemini). When ChatGPT and Gemini answered the same question, they shared only 5.4% of domains on average.
- Someone in the industry tested this themselves (repeated many times, with a control group): the same client appeared 8 out of 10 times in one model version; in the developer interface without system settings, it was zero. Another fintech client was cited 3 out of 10 times in a larger model; the smaller model recommended the same large payment company no matter how it was asked.
- Someone in the industry tested this themselves: in the same week, for the same "alternatives to a well-known project management software" question, the same brand ranked first on ChatGPT and Claude, but only fourth on Gemini.
- Someone in the industry tested this themselves: in data from the last 30 days, the overlap of cited domains between any two of Gemini, Perplexity and Google's AI Overviews was about 25%; between ChatGPT and them it was only 11% to 14%.
- Someone in the industry tested this themselves (repeated many times, with a control group): across 40 fixed buyer questions, community forum sources made up 7% in Gemini and Google's AI Overviews, 9% in Google's AI Mode, 1% in Perplexity, and almost zero in ChatGPT and Claude (Chapter 15).

**What this shows:** Every AI has its own tastes (Chapter 12). Measuring them all mixed together is the same as measuring nothing (Chapter 9).

### Story 30: Counting rules can create fake changes

- Someone in the industry observed: counting only the company name, the score was 77. After product names were also counted as the company's aliases, with the same 20 questions and the same 4 AI platforms, the score the next day became 94. The world didn't change; the counting method did.
- Someone in the industry observed: if the question itself contains a brand name (for example, "X vs Y" or "alternatives to X"), the AI may just be repeating the name from the question. After removing this kind of "echo", the overall naming rate fell from 10.9% to 8.9%; for "X vs Y" type questions, it fell from 15.8% to 8.1%.
- Someone in the industry tested this themselves: of 10 companies in one tracking database, the names of 2 were read by AI as ordinary words. When a brand name is the same as an ordinary word or another entity, "not appearing" may just mean the AI thought you were talking about something else. You can only see this by reading the raw answers.
- Someone in the industry tested this themselves: a car brand's visibility score stayed at 84 for 47 days in a row; but in purchase recommendation answers, the results had long since shifted to a competitor. The score did not reflect that the citations supporting it were slowly draining away.

**What this shows:** Before you start recording, first define clearly "what counts as a hit", and don't change it casually afterwards (Chapter 9).

### Story 31: One blended score wipes out what you need to see

Someone in the industry tested this themselves (repeated many times, with a control group): within the same set of questions, one AI model favoured identity verification vendor A, another favoured vendor B, and the AI platforms that search online favoured vendor C.

If you blend them into one "total AI visibility score", you average away the very differences you really need to see.

You also need to tell two kinds of numbers apart: "how often it is mentioned" answers "who appeared"; "rank-weighted share" answers "who is at the top". The two are asking different questions.

**What this shows:** Look at each AI platform separately, and be clear about what question the number you are looking at answers (Chapters 9 and 12).

---

## Story group 8: Did business really get better?

This group corresponds to gate 7, "whether people come over" (Chapter 10).

### Story 32: Subtract the platform's own growth, and the effect is much smaller

There was one large-scale experiment using real user traffic (but covering only one website):

- Referral traffic from ChatGPT grew 5.7 times month on month.
- But pages on the same website that had received no treatment at all also grew 3.5 times over the same period.
- After using these untreated pages as a control group, the traffic level of the pages that had been given GEO treatment jumped by about 1.82 times. The statistically reasonable range was 1.31 to 2.54 times (95% confidence interval); checked with several different methods, the results fell between 1.8 and 2.3 times.
- The researchers also did a "placebo test": taking a point in time when nothing was done and pretending something had been done, to see whether an effect would also appear. The result was not clean enough (statistical value p=0.16), so overall it can only count as "there are signs", not as certain.
- The study did not find the effect of "doing GEO boosts ordinary search traffic, forming a virtuous cycle".

**What this shows:** When brands see "AI traffic has multiplied several times", most of it may just be the AI platforms themselves growing. Without a control group from the same period, there is no way to tell what GEO actually did (Chapter 10).

### Story 33: What AI brings is often not clicks

- Someone in the industry tested this themselves: server logs showed that one of ChatGPT's fetching programs (which appears only when a real person asks a question and ChatGPT fetches the web page on the spot) visited the website about 14 times a day, but the website's analytics tool recorded only about 1 click. The rest of the users, after seeing the recommendation, searched for the brand name directly, and so were recorded as "direct traffic".
- Someone in the industry observed: AI answers about local businesses often give the business name, address and phone number directly. Users call directly, with no click and no referral record. He suggests preparing a dedicated phone number, placed only on the business profile and on listings meant for AI to read; and adding the question "May I ask how you found us?"
- Someone in the industry tested this themselves: an agency asked clients verbally on the first call how they had heard of them, and found that about 30% of deals came from AI search. The author thinks this may only be the minimum, because the agency's sales cycle is short and clients still remember where they first saw it.

**What this shows:** Something that looks like **zero-click** does not mean AI brought no customers. The customers just came by a different route (Chapter 10).

### Story 34: Citations went up, but sales didn't necessarily follow

Someone in the industry tested this themselves: a small business-facing online subscription software company did these things: put the answer at the very top of pages, added FAQ and product structured data, put up llms.txt, made comparison pages, and cleaned up AI's description of the company as an entity.

AI citations did go up. But visitors coming from AI left faster than visitors coming from ordinary search, and there were almost no sales.

Other people in the industry reported the opposite results:

- Someone in the industry tested this themselves (repeated many times, with a control group): potential customers who came in after being named by AI converted at 8% to 9%; ordinary search was about 1%.
- Someone in the industry tested this themselves: focusing on 5 to 6 "best X" type purchase questions, within 90 days the mention rate in related AI answers reached 15% to 20%, and the conversion rate was about 4 times that of ordinary search traffic.

What to discount: these sales figures are all self-reported, with no control group. And a high conversion rate may just be because these users were already close to making a decision (Chapter 10).

**What this shows:** After gate 7, "whether people come over", there is also "whether they buy once they've come". Both need to be measured with a control group (Chapter 10).

---

## Story group 9: Some people try to cheat

This group corresponds to Chapter 11 (zero-sum competition, manipulation and defence).

- **Under test conditions with given web pages:** researchers added hidden **prompt injection** and exaggerated claims to pages, and the share of times a fictional camera was recommended rose from 34.0% to 59.4% (the real brand's was 57.9%). But if several parties do this at the same time, everyone's visibility falls together, becoming a situation where no one is willing to stop and everyone ends up harmed together (called the "prisoner's dilemma" in the industry).
- **Someone in the industry tested this themselves:** someone claimed to have used multiple accounts and devices to repeatedly "correct" ChatGPT's answers; after 5 real users did this, ChatGPT started recommending their business. This claim has no control group, and cannot rule out the effects of personalisation and random fluctuation (see Story group 7); it should not be treated as a method.
- **Someone in the industry observed:** in a small field with very little competition, 4 community posts made a new website the second recommendation of two AIs. There were also users who were recommended to scam websites because AI cited positive reviews in communities.
- **Someone in the industry observed:** a competitor used highly reputable automated accounts to post in large volumes on community forums, pretending to be neutral buyers making comparisons, while running down other products. AI cited this content and spread wrong information about the targeted brand. The targeted brand clarifying in the comments had limited effect.

**What this shows:** Chapter 5 said that "many sources say so" is both the strongest signal and the biggest attack surface. These cases are what that attack surface actually looks like. Authoritative-sounding copy and faked evidence really do work in experiments, but that is manipulation; and when the whole industry does it, the benefit tends towards zero (Chapter 11).

---

## Five things still being argued about

### Debate 1: Does being mentioned off-site actually help?

| Position | Basis |
|---|---|
| Being mentioned off-site decides whether you can be recommended | On Chinese-language AI search, being mentioned together by more sources better predicts being selected (Story 11); new products' visibility rises together with "how many websites link to you" and "how many times you are mentioned in communities" (Story 1); many industry before-and-after cases (Story 12) |
| After controlling for how readable the website is, being mentioned off-site has no independent effect | Results of matched comparisons where AI browsed business websites in depth (Story 15) |

A possible explanation (Chapter 5): these two things act at different stages. Being mentioned off-site decides whether you can "surface" on the shortlist; when AI walks into the website to look more closely, how readable the website is decides whose content is used.

Someone in the industry used the same framework to describe their own observation: your off-site footprint gets you onto the list, and the language on your official website describing the job you do keeps you on the list when the question changes (Story 5).

The conditions of the two studies were different; **at present it is impossible to judge who is right and who is wrong**.

### Debate 2: Do structured data and llms.txt help?

| View | Basis |
|---|---|
| They help | Someone in the industry tested this themselves: among online subscription software websites of the same traffic level, those with complete structured data were cited about twice as often as those without; after changing 8 comparison pages to short question-and-answer headings and adding FAQ structured data, citations for 12 target questions went from 0 to 4 within 6 weeks; among local businesses, industry-specific structured data was related to visibility (Story 25) |
| They are basic hygiene, not a lever | Someone in the industry tested this themselves (repeated many times, with a control group): llms.txt was never linked to any change; structured data won't get you named, but when you are already named, it helps you be described correctly; wrong structured data is worse than none |
| Almost no measurable effect | Someone in the industry observed: FAQ structured data and llms.txt had no measurable effect; optimising the website itself is the smallest lever |

Chapter 3 has already pointed out: **at present there is no evidence that llms.txt works on its own.** In this chapter's cases, every one that reported it working did it together with other changes.

### Debate 3: Does Google ranking still matter?

- Many people in the industry report: "Number one on Google, but invisible in AI".
- But someone in the industry also tested this themselves and believes that citations in Google's AI Overviews and Gemini are highly related to traditional rankings: ranking high doesn't guarantee being cited, but not being in the search results at all almost certainly means being filtered out. Another person in the industry tested this themselves (repeated many times, with a control group) and found that citations in Google's AI Mode clearly overlapped with the first page of search results, but the order of recommendations and the descriptions were different.
- Researchers tested repeatedly on real AI search: the overlap between domains cited by AI platforms and by Google search is very low; for example, for the smartphone category, the top 5 overlapped by only 15%.

A more reasonable reading: for AI platforms that rely on Google's index, ranking is more like an "entry threshold"; for ChatGPT's comparison questions (which often don't search online), ranking is almost irrelevant. It needs to be judged separately for each AI platform.

### Debate 4: Does fame actually matter?

- Researchers tested repeatedly on real AI search (a service provider's actual operating data): on the first run, in questions without brand names, visibility showed three clear tiers: big brands 72.9%, mid-sized brands 43.6%, small brands 11.4%.
- But the cases of the famous coaches, the category leaders and the funded startups (Story 2) all show: fame does not turn directly into recommendations.

The way to reconcile this: this tier difference does not reflect "fame" itself, but how "densely a brand appears" in AI's training data and in sources that can be found by search (this is the corrected conclusion from Story 14).

Big brands usually have both, so they have the advantage in broad questions. But in niche questions and specific buyer situations, this "density of appearance" has to be counted per "question", not per "brand".

Someone in the industry observed: big spirits brands won only in broad questions; in more specific questions like "which one should I use to mix a particular cocktail", the leaders were brands with more distinctive brand stories.

### Debate 5: How soon can you see results?

| Reported time | Situation | Strength of evidence |
|---|---|---|
| A few days | Squeezing into review blogs that AI is already citing | Someone in the industry tested this themselves |
| About a week | After doing 5 recommendation lists plus 2 roundups, ChatGPT ranked the brand 2nd | Someone in the industry tested this themselves |
| 10 days | Publishing comparison articles plus technical documentation, went from 1 to 5 out of 8 questions | Someone in the industry tested this themselves (repeated many times, with a control group) |
| About 2 weeks for Perplexity, close to 2 months for ChatGPT | Running 20 buyer questions every week, and working to get exposure on the sources that kept appearing | Someone in the industry tested this themselves |
| AI citations came several weeks later than indexing | Publishing large numbers of separate topic pages | Someone in the industry tested this themselves (repeated many times, with a control group) |
| About 3 months | Unifying descriptions, plus squeezing into existing comparison articles | Someone in the industry observed |

At the same time, several observations point out that older content is still having an effect:

- Someone in the industry tested this themselves (repeated many times, with a control group): tech media coverage and review discussion threads from three years ago had an effect in more AI model versions than recently published content.
- But researchers testing on Chinese-language AI search found: for highly time-sensitive questions, the median age of cited pages was only 18 days.

A more reasonable reading: AI platforms that rely on real-time search (especially Perplexity) respond quickly; questions that rely on AI's memory (such as ChatGPT's comparison questions) respond slowly, and have to wait until the content makes it into the AI's training data.

---

## How to do it: first find out which gate you're stuck at

### Diagnostic process

1. **Write down a list of questions.** Write down 10 to 30 questions that real buyers would ask, covering category, alternatives, usage situations, cities and buyer identity. This is your **prompt set**.
2. **Delete the questions that don't name brands.** A question that never names any brand is meaningless to track (Story 4).
3. **Set a baseline.** Run each question at least 3 times on each AI platform. Use clean conversations, the target language and the target region.
4. **Record things separately.** Record separately: whether you were named, whether you were recommended, whether you were advised against, whether your official website was cited, and which third-party pages were cited.
5. **Work out which gate you're stuck at:**
   - Doesn't appear even with online search turned off → what's missing is the AI's memory (slow to show results).
   - Only appears with online search turned on, or you aren't in the material AI cites at all → what's missing is other people's word of mouth (medium speed to show results).
   - Your official website is cited, but you aren't named → the problem is in how it's written and "whether it actually uses you" (quick to show results).
   - Put in the wrong category → the problem is in how your category and positioning are described.
6. **Deal with the gate you're stuck at, then retest with the same set of questions.** Before retesting, first measure the "noise floor": do nothing, rerun a few days later, and see how much the results change on their own (Story 20).

### List of methods (with strength of evidence)

| Method | Strength of evidence |
|---|---|
| Measure separately by AI platform, language, market and model version; don't use a blended total score | Researchers tested repeatedly on real AI search, and several studies agree |
| Run each question many times and report the mention rate and how stable it is, rather than a single screenshot; prioritise widening the range of languages, AI platforms and ways of asking | Researchers tested repeatedly on real AI search |
| Ask in the target market's language, and write the city into the question sentence, to test local visibility | Researchers tested repeatedly on real AI search; in addition, someone in the industry tested this themselves (repeated many times, with a control group) |
| First fix "what counts as a hit" (aliases, other entities with the same name, the "echo" of a brand name already in the question), then start long-term recording | Someone in the industry observed; methodologically, it is common sense |
| Find the third-party pages that AI repeatedly cites when answering the target questions (recommendation lists, review sites, directories, industry listings), and work to be genuinely included | Someone in the industry tested this themselves (multiple cases, no control group); no study has verified it |
| Unify the company description on your official website's "About us" and in all third-party profiles: what you do, and who it's for | Reports and observations from people in the industry who tested it themselves; in principle, consistent with "many sources say so" in Chapter 5 |
| Build a dedicated page for each core buyer question and each service; put the brand name, specific facts, prices and numbers near each other in the same sentence | Someone in the industry tested this themselves; consistent with the principles in Chapters 6 and 7 on relevance and "whether it actually uses you" |
| Use the buyer's language to describe what the product actually helps people get done, rather than only claiming to belong to a certain category | Someone in the industry tested this themselves (repeated many times, with a control group), a single case |
| Make sure your official website can be understood by AI that comes in to read: content that doesn't rely on JavaScript, structured data provided, crawler settings not blocking | Researchers tested repeatedly on real AI search (a bundled total score, not broken down) |
| Local businesses: keep name, address and phone number consistent across directories; build city pages and service pages; work on review platforms | Someone in the industry tested this themselves; several independent samples point the same way |
| Choose niche questions, specific situations and particular buyers where big brands don't have the advantage as your way in | Reports and observations from people in the industry who tested it themselves, pointing the same way |
| Use a control group from the same period (untreated pages on the same website) to assess business effects; local businesses should use a dedicated phone number and ask "how did you find us" | A large-scale real-user experiment shows a control group is necessary (only one website) |

---

## Remember in one sentence

**AI knowing you does not mean it will recommend you; a recommendation is a multi-round knockout, so first find out which gate you're stuck at, then confirm it with measurement that is repeated many times, split by platform and split by language.**

---

## What you can do tomorrow

1. **Write down 10 to 30 questions that real buyers would ask**, covering category, alternatives, situations, cities and buyer identity; delete the questions that never name any brand.
2. **Test with clean conversations**: don't use your own account and conversation history; run each question at least 3 times on each AI platform; use the target market's language, and write the city directly into the question sentence.
3. **Record the five states separately**: known, cited, named, recommended, advised against. Especially, don't forget "advised against".
4. **Measure the noise floor first**: change nothing, rerun a few days later, and see how much the results change on their own. Don't take any change smaller than that seriously.
5. **First settle "what counts as a hit"**: do aliases count? Does it count when your name is already in the question? When a brand name clashes with an ordinary word or another entity, go and read the raw answers.
6. **Ask once with "online search off" and once with "online search on"**, to work out whether what you're missing is the AI's memory or other people's word of mouth.
7. **List the third-party pages AI repeatedly cites** (recommendation lists, review sites, directories, industry listings), and work to be genuinely included. Remember: this kind of borrowed exposure may disappear as soon as the other side changes its page.
8. **Unify your description on your official website and all third-party profiles**: what you do and who it's for, saying the same thing everywhere. Regularly check how AI describes you, and when you find an error, trace it to the source (for example, an outdated directory profile) and fix it.
9. **Make a dedicated page for each core buyer question and each service**: state real prices, specific models and specific numbers, and put the brand name in the same sentence as these facts.
10. **Use the buyer's language to describe what you actually help people get done**; don't just write "we are a leader in such-and-such category".
11. **Confirm that your official website is readable by AI**: important content doesn't rely on JavaScript, there is structured data, and crawler settings don't block AI.
12. **Local businesses**: keep name, address and phone number consistent across directories; make city pages and service pages; work on review platforms; prepare a dedicated phone number used only for AI and the business profile, and when dealing with customers, ask "May I ask how you found us?"
13. **Pick battlegrounds where big brands don't have the advantage**: niche questions, specific situations, particular buyers.
14. **When assessing business effects, always have a control group from the same period**, for example untouched pages on the same website.

---

## Stop doing this

- **Stop judging visibility with your own account and a single screenshot.** Your conversation history and location will make you see results that others don't see.
- **Stop treating being cited as being recommended.** Your official website being cited may mean it is supplying descriptions for your competitors.
- **Stop looking only at one blended total visibility score.** It covers up differences between AI platforms, differences between buyers, and the fact that recommendations have already shifted.
- **Don't list "trustworthy competitors" on your official website**, unless you can accept AI taking it directly to use as a recommendation list.
- **Don't fake evidence, flood the internet with posts, or hide instructions in your pages.** It works in experiments, but that is manipulation; when several parties do it at the same time, everyone is harmed together (Chapter 11), and it also invites action from platforms and risks to your reputation.
- **Don't stuff your business profile with place names and words like "near me".**
- **Don't count on mass-distributing press releases, posting in large volumes on professional social networks, or paying to upgrade your review platform profile.** Current tests by people in the industry show no visible effect from these.

### Ideas that are already out of date

- "If I rank well on Google, AI will naturally recommend me." For some AI platforms, ranking is only an entry threshold; for ChatGPT's comparison questions, it is almost irrelevant.
- "Track questions that contain my brand name, and look at my mention rate." When your name is in the question, you will almost certainly appear, so this number is meaningless.
- "Monitor a global brand only in English, from only one location." This systematically hides local competitors from you.
- "Do one check, and you can relax for a long time." Recommendation lists change every week, and citations also slowly drain away.

---

## What is still uncertain

- **"Get third parties to write about you, and your recommendations will go up" has not yet been confirmed by controlled experiments.** At present there is only observational and before-and-after evidence; most cases have no control group, and did several things at the same time.
- **Whether being mentioned off-site actually has an independent effect**: the two types of studies reach different conclusions, under different conditions. One possible explanation is that the two act at different stages, but at present it is impossible to judge who is right and who is wrong.
- **Whether structured data and llms.txt help**: views in the industry are split into three camps. The only thing that is fairly clear is: there is not yet any evidence that llms.txt works on its own; the cases that reported it working all did it together with other changes.
- **Whether Google ranking still matters** needs to be looked at separately for each AI platform; at present there is no single answer.
- **Whether fame matters**: big brands do have the advantage in broad questions, but the more likely explanation is "density of appearance" rather than "fame" itself. This is a reconciling reading, not a settled conclusion.
- **How soon results appear**: people report anything from a few days to a few months, all in the industry's own reports; whether old content or new content is more useful, different observations point in different directions.
- **Whether buying ads on AI platforms can change the preferences AI has already formed**: "it can't be rescued" is only an inference; no one has actually tested it.
- **ChatGPT rarely searches online for comparison questions**: this was measured through the developer interface; whether the products ordinary consumers use behave the same has not been directly verified.
- **The business effects of GEO**: the only study with a control group covers just one website, and its results can only count as "there are signs"; the conversion rates reported in the industry range from high to low, none of them with a control group, and high conversion rates may just be because these users were already close to making a decision.

---

## Key points of this chapter

1. **Brand recommendation is a multi-round knockout.** Known, cited, named, recommended and advised against are five different states, and they come apart from each other. First find out which gate the brand is stuck at.
2. **"Knowing" is not the same as "recommending".** Ask the name directly, and the recognition rate can be close to 100%; ask only about the category, and the discovery rate is only in single digits. Fame, funding and number of reviews do not automatically turn into recommendations.
3. **What the question looks like decides the shortlist.** The category word, the way of asking, the buyer's identity, a city written into the sentence, and the language of the question can all swap out the entire recommendation list. For comparison questions closest to a purchase, ChatGPT often does not search online.
4. **AI's answers about brands are built mainly on other people's word of mouth.** Your own website makes up only a small share of citations; being mentioned together by more sources is strongly related to being selected into the answer. "Squeezing into the recommendation lists AI is already citing will increase recommendations" is supported by many industry cases, but has not yet been verified by controlled experiments.
5. **The role of your official website lies in "being understood" and "controlling the description".** When AI walks into the website, how readable it is decides whose content the answer uses; without a dedicated page, AI will guess your positioning; the brand name needs to sit together with specific facts, or the facts may end up attached to a competitor's name. For local businesses, the official website carries clearly more weight.
6. **Measurement is the part of this chapter with the strongest evidence.** You must run things many times, split by AI platform, by language and by version, fix "what counts as a hit", and measure the noise floor first; a single screenshot and a blended total score will both mislead you.
7. **Business effects must have a control group.** After subtracting the growth of the AI platforms themselves, the effect is much smaller than the raw multiples; the value AI brings often shows up as "searching the brand name" and "calling directly", which is hard to credit to AI.
8. **"Many sources say so" is both the strongest signal and the biggest attack surface.** Flooding with posts, faking evidence and hidden instructions may work in the short term, but that is manipulation; and when the whole industry does it, the benefit tends towards zero.
