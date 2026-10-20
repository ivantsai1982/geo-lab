# Chapter 3 — Can AI Get Through Your Front Door?

> The second of the seven gates: **Can it get in the door** (accessibility).
> All later efforts rest on one precondition: AI's crawlers actually got your content.

---

## Imagine

Imagine a business owner who runs an online shop selling handmade furniture. Her website was built for her a few years ago, and it looks beautiful.

She has heard that many people now ask AI directly, "Where can I buy a sturdy solid-wood desk?", so she tries it herself. The answer lists four shops. She is not one of them. She tries a few other phrasings. Still not there.

She opens her website's settings file. It says "all crawlers welcome." She is puzzled: the door is clearly open, so why won't AI come in?

This chapter is about that door. It has several more layers than most people imagine. And when it breaks, it makes no sound at all.

(The above is a fictional illustrative scenario.)

---

## The big idea of this chapter

**If AI can't read you, you don't exist. And when it can't read you, it won't tell you. It will just quietly use someone else instead.**

So "Can it get in the door" has to be checked layer by layer:
- Which kind of crawler are you blocking?
- At which layer is it blocked?
- Once the crawler gets in, is there actually anything in the page it receives?

This chapter will answer five questions:

1. Does blocking or allowing AI crawlers change your chances of appearing in AI answers?
2. Why doesn't "robots.txt is fine" equal "AI can read it"? At which layers can blocking happen?
3. What does AI actually capture? Content assembled by JavaScript, the descriptive information in the page's "head", structured data: which of these really get read?
4. Which "catalogues" (indexes) does AI rely on behind the scenes? What's the difference between reading on the spot and a catalogue organised in advance?
5. Are llms.txt and Markdown versions for AI any use? When AI goes deep into your website to get things done for someone, what decides whether it can make use of your content?

---

## 1. If it can't be read, it doesn't exist

When AI search answers a question, it can only use the content it can get.

If it can't get it, you can't get onto the **shortlist**. The later selection, ranking and citation are all out of the question.

Think of AI as that very busy librarian. He is looking up material for a reader, walks up to your shelf, and finds the door locked, or the pages blank. He won't wait at the door, and he won't make up an introduction for you. He'll turn around and take a book from the shelf next door.

### Direct observations on Google products

Researchers ran repeated tests on real AI search and saw a very direct phenomenon.

Google has a dedicated identity marker called **Google-Extended**, used to separate crawling for "AI purposes". Websites that blocked Google-Extended:
- were cited by Gemini **zero** times;
- were also cited noticeably less often by the **AI summary** at the top of Google's search page.

Note: this is an observed correlation, not a randomised experiment. But the direction is clear.

### Failure is silent

What you most need to remember is "what failure looks like".

When an AI that goes online to get things done by itself (what this book calls an AI agent) can't read your website, it **won't make up content for you**. It will **leave you out**, and answer using content from third-party websites or competitors instead.

You won't see any error message. You'll just find that you're not in the answer.

---

## 2. "The AI crawler" isn't one crawler, but several

A **crawler** is a program that reads web pages automatically. The most common misunderstanding is treating all AI crawlers as the same thing, and thinking one switch can control them.

In fact, the same AI company usually sends out several crawlers with different identities, each handling one job. Each identity has its own name (technically called a user-agent, meaning the name the crawler gives when it visits).

### Taking the company behind ChatGPT as an example

This company has published its own division of labour. People in the industry summarise it as follows:

| Identity name | What it does | What happens if you block it |
|---|---|---|
| GPTBot | Collects data for training models | Your content won't be used for training; **does not affect real-time answers**. Official documentation: content obtained while users browse with ChatGPT Atlas, OpenAI's browser, also respects this block |
| OAI-SearchBot | Builds the index (catalogue) used by ChatGPT search | Official documentation: if you block it, your content will not appear in the summaries and snippets of ChatGPT search; if OpenAI learns your URL from a third-party search provider or from other web pages, ChatGPT Atlas may show only the link and title |
| ChatGPT-User | "On-the-spot reading" triggered by users in a conversation | When a user pastes your URL to AI, AI can't read it |
| OAI-AdsBot | Checks ad landing pages (added in 2026) | Related to ads |

### Other AI companies are similar

There's an easy-to-remember pattern: **identities with "User" in the name** (e.g. Claude-User, Perplexity-User) are usually for **on-the-spot reading** when answering questions.

Names like ClaudeBot and PerplexityBot are usually crawlers that build indexes or collect training data.

There's also a special case. Someone in the industry pointed out that the crawler named **meta-externalagent**, according to its official description, is responsible for **both** collecting training data and building the index used for Meta AI's answers. Blocking it means exiting both paths at once.

### Three types of crawler, three paths

You can divide them into three types:

1. **Those that collect training data** (e.g. GPTBot, ClaudeBot, and a public crawler called CCBot): content goes into the model's original "memory".
2. **Those that build indexes** (e.g. OAI-SearchBot, PerplexityBot): content goes into AI's own catalogue, ready to be looked up quickly when someone asks a question.
3. **Those that read on the spot** (e.g. ChatGPT-User, Claude-User): someone is asking a question right now, and within those few seconds AI comes to read your web page, used only for this one answer.

All three paths end up flowing into the same answer, but each goes through its own door.

### This division of labour leads to two direct conclusions

**First, blocking crawlers that collect training data won't make you disappear from real-time answers.**

Large-scale real user data (in the appendix of one study) shows:
- **79%** of domains blocked at least one AI crawler;
- the average referral traffic these blockers got from ChatGPT was **6.48**, versus **4.48** for those that didn't block. Blockers did not get less.

Note: this is only a correlation, and can't be read as "blocking actually brings traffic". It shows just one thing: **blocking training crawlers doesn't stop ChatGPT from sending people to you when it answers.**

**Second, allowing only training crawlers while blocking on-the-spot reading is the real loss.**

In the mode where AI goes online to answer, only about **7–10%** of the answer content comes from the model's original training memory; the rest is looked up on the spot.

In other words, whether AI has "learned" about you matters far less than whether it "can read" you right now.

---

## 3. The door has three layers, and robots.txt is only the outermost one

A website's root directory usually has a small file called **robots.txt**, used to tell crawlers "where you may come, and where please don't enter". Many people check accessibility by looking only at this one file.

The problem is that a request travelling from outside to your content has to pass through three layers:

```
Crawler's request
  → [Building security guard] Website acceleration and protection services (CDN), web application firewall (WAF), host's bot protection
  → [Sign at the door] robots.txt
  → [Are there words in the book] The content the server actually sends back
```

**The sign (robots.txt, the declaration layer).**
It says "Welcome" or "No entry". But it's only a courtesy notice; whether the other side follows the rules is up to them.

**The building security guard (CDN, WAF, host security settings, the enforcement layer).**
Before the request even reaches your website, it may be stopped based on the crawler's name or the reputation of its source address. The other side will receive "Forbidden" (technically the 403 status code) or a "prove you are human" challenge page.
This layer **is not written in robots.txt**. Browsing your own site in a browser, you can't see it at all either.

**Are there words in the book (the server's response content, the content layer).**
The guard lets it through and the request succeeds, but the page the other side receives may not contain the content you think it does. The next section goes into detail.

### The guard often shuts the door without you knowing

Many in the industry believe that AI crawlers are often blocked at the CDN or WAF layer, and often by default settings, or by settings switched on accidentally. Even if robots.txt says welcome, it doesn't help.

Clearly more people support this view than oppose it. But "many believe" does not equal "correct"; this is not proof.

A concrete example: one CDN service offers a "block AI crawlers" switch. Once switched on, it **inserts a block of rules it manages itself at the very top** of your own robots.txt, blocking GPTBot, ClaudeBot, Google-Extended and others, overriding your original settings.

Another person in the industry pointed out: from September 15, 2026, this CDN service changed its default so that it blocks "mixed-purpose" crawlers (that is, crawlers used for several purposes at once) on **pages with ads**. Websites without ad slots are not affected by this change.

---

## 4. AI reads the "server's raw response", not the page you see in your browser

When you open a web page in a browser, the browser runs a lot of programs (JavaScript) that "assemble" the prices, menus and collapsible Q&As piece by piece, and only then do you see the full page.

**Most AI crawlers don't do this assembly.** They only take the most raw HTML document the server sends out, convert it to plain text, and pass it to the model.

An analogy: you send the librarian a piece of furniture he has to assemble himself. You think he's receiving a desk; what he actually receives is a box of planks and a bag of screws. Anything on the web page that "only appears after assembly" doesn't exist for him.

### This is one of the strongest consensuses in the industry

"Most AI crawlers don't run JavaScript, and content generated by browser-side programs is invisible to them" is one of the claims with the strongest industry consensus on this topic. The ratio of supporters to opponents is about **23 to 1**.

Someone in the industry tested this themselves; details below (but no one has independently verified it):

- **Test 1:** Build a test page with more than 60 identifiers embedded in it, and have six AI platforms read it. **Three didn't run JavaScript at all**; the other three gave it only 0.5 to 3 seconds before leaving.
- **Test 2:** In the same test, of the 11 types of descriptive information in the page's head (`<head>`), **9 types had a read result of zero**. The page summary description (meta description), JSON-LD structured data, social sharing tags (OG tags) and schema markup were not read. The only thing read was the **page title (`<title>`)**. The tester's explanation: the step that converts the web page to plain text throws away the entire head section.
- **Test 3:** Among 50 websites, **34 (68%)** used browser-side programs such as a "tag manager" to insert JSON-LD structured data into the page after the fact. Result: for websites where the server output JSON-LD directly, **92%** of the structured data was picked up by at least two AI crawlers; for those relying only on browser-side insertion, **0%**.

### What you see isn't necessarily what it gets

**What you see in the browser's "developer tools" doesn't necessarily exist in the server's raw response.**

Developer tools usually show the result **after** the programs have run. Someone in the industry found that their own website's language-version tags (hreflang, used to tell machines "which other language versions this page has") numbered **0** in the raw response and **3** in the assembled page. Because the inspection tool showed the assembled version, this problem went unnoticed for months.

### Content that most often "only appears after assembly"

| Content | Why AI can't see it |
|---|---|
| Prices, plan figures | Filled into the page from a database by a browser-side program; the raw HTML only has the plan names |
| Text in carousel sections | Displayed in rotation by a program |
| Answers in FAQ collapsible sections | Loaded by a program only after a click |
| Headline text that rotates via animation | In the raw document the headline is only half a sentence; the rest is in the animation component |
| Structured data | Injected afterwards by a tag manager |
| Language-version tags | Generated by a front-end framework |

---

## 5. AI has several "catalogues" behind it, and they rarely overlap

The sources of AI answers come by roughly two paths:

1. **Indexes organised in advance**: built by the AI company itself, or borrowed from a search engine.
2. **On-the-spot reading when answering.**

### Same company, three interfaces, very different web pages seen

Researchers ran repeated tests on real AI search, comparing three interfaces from the same company: traditional search results, AI summaries, and Gemini.

The overlap of the sources they cited, measured with a standard "overlap ratio" (0 means completely different, 1 means completely identical), was only **0.11 to 0.18**.

In other words, even with the same company behind them, the sets of web pages that different AI interfaces get differ a lot.

### Being indexed by traditional search is itself part of AI accessibility

Someone in the industry has mentioned that when a site's content needs JavaScript to display, ChatGPT relies heavily on Google's index, but they offered no evidence. Which index ChatGPT actually uses is disputed (see Chapter 4). Separately, OpenAI's official documentation confirms that besides the index OAI-SearchBot builds itself, ChatGPT search also uses "third-party search providers", but it does not say which ones.

This means: **whether your web pages are indexed by traditional search engines is itself part of whether AI can read you.**

### "AI says it read it" doesn't necessarily mean it read the latest version

Someone in the industry made a pure-HTML test page and had four AIs read it:
- ChatGPT tried about 10 times and couldn't read it;
- Claude read it only the first time in a new conversation, and after that couldn't see updates to the page;
- Perplexity cited 14 unrelated pages;
- only Gemini read the full page, including the schema markup in it.

The tester judged that in most cases AI was reading a **cached version** (an old copy saved earlier). This is a single tester's observation and can only be treated as a clue.

Another situation: **AI doesn't open your page at all.** Researchers found on real AI search that a lightweight model did not open a single web page in 53.6% of conversations, answering only from the excerpts in the search results. Under lab conditions, answers based only on excerpts were more likely to be out of date, and their citations more likely not to match the original text (see Chapter 7).

### A new name, cited on day 6

"Newly emerging entities" illustrate the differences between indexes especially well. (An **entity** is "one thing" in AI's mind, such as a brand, a person or a product.)

Someone in the industry ran a repeated, controlled experiment:
- create a new entity with absolutely no footprint on the internet;
- for 23 consecutive days, have five AI systems that go online look it up every day;
- during this period, the CDN's default AI block returned "Forbidden" (403) to the training crawlers on **22** of the 23 days.

Even so, this entity was cited on **day 6**. What made it possible was the **knowledge graph** (the database AI and search engines use to record "who is who, and who is related to whom") plus **third-party sources** (mentions on third-party websites).

Server logs also showed that on the very same day, the two types of crawler that AI only uses when answering (OAI-SearchBot, which builds the index, and ChatGPT-User, which reads on the spot) were let through normally.

The gap between AI companies was also large: one used the entity's own domain as a basis about **119** times; another **0** times, taking data only from third-party social platforms.

---

## 6. When AI gets things done for people: getting in isn't enough, it also has to be usable

More and more often, AI doesn't just read one page and leave. Like an assistant, it **goes deep into your website**: checking prices, comparing specs, even completing tasks for people. This kind of AI that takes action itself is what the industry calls an AI agent.

At this point, the standard for accessibility rises from "can read the text" to "**can understand it and operate it**". The industry calls this **agent experience (AX)**.

### A large observation: readable websites are used more often to answer with their own content

Researchers ran repeated tests on real AI search: covering **1,056** businesses and **37,927** AI agent query sessions.

| | Websites readable by AI agents | Unreadable websites |
|---|---|---|
| Proportion of answer content coming from own pages | **78%** | 58% |
| Proportion explicitly recommended | **20%** | 11% |

When looking at these figures, you should know a few limitations:
- this study was done by **an organisation that provides related services**, using its own scoring tool;
- it is a **matched observational study**: websites similar in fame, AI's existing memory of the brand and other conditions were paired for comparison, but it is not a randomised experiment;
- "readability" is a **bundled score**, including: content not dependent on JavaScript, having structured data, having llms.txt or a Markdown fallback version, and bot protection that lets AI agents through. The study **did not separate out the effect of each item**.

The same study also found: after removing the factor of agent experience, "breadth of off-site mentions" (how widespread third-party sources are) had **no additional independent effect** on whether AI agents used your content or recommended you.

But this conclusion **applies only when an AI agent has already entered your website to look deeper**. It doesn't mean off-site mentions are unimportant at the "being discovered" step.

### E-commerce websites in the lab

Under lab conditions (a fully controllable experimental system), researchers modified a prototype e-commerce website, adding:
- JSON-LD structured data;
- markup that lets machines understand the purpose of buttons and fields (aria attributes);
- hints telling machines "what actions can be done here";
- fields marking the date of the data.

As a result, the task success rate of three browser AI agents under strict criteria rose from **49.3% to 89.3%**; the average number of steps needed fell from **9.31 to 6.49**.

But this is only **a single synthetic website**, and everything was changed as a bundle. The authors themselves call it a "proof of concept", and it's impossible to tell which item made the difference. It's not certain for the real world.

### Being found doesn't mean being usable

Under test conditions with given web pages, researchers looked at a "finding datasets" scenario.

After data providers published **machine-readable data descriptions**, the precision with which AI agents retrieved "data pages that can be used directly" was **46.4%**, versus **28.0%** for the control group.

But at the same time, AI agents taking this path answered only **40 questions**, while the control group answered **56**.

**Being found doesn't mean being usable.** This is the "last mile" problem in AI agent scenarios.

### An official tip: use accessibility labels to tell AI what a button is

OpenAI's official documentation says that the AI agent in its browser, ChatGPT Atlas, uses ARIA labels to understand the buttons, menus and forms on a web page. ARIA labels were originally accessibility markup for screen readers, telling users who cannot see the screen "what this element is and what it does". The official advice is to add clear roles, labels and states to these interactive elements.

---

## 7. A closer look: how strong is this evidence?

| Conclusion | Where the evidence comes from | Strength and limitations |
|---|---|---|
| Blocking Google-Extended is associated with zero Gemini citations and fewer AI summary citations | Repeated tests on real AI search | Medium to strong; correlation, not causation |
| Blocking training crawlers doesn't stop ChatGPT referrals | Large-scale real user data (study appendix) | Medium; correlation, the main study's causal design doesn't cover this point |
| Websites readable by AI agents are used more often to answer with their own content and recommended more often | Repeated tests with real AI agents | Medium; study by a service provider, matched observation, bundled score |
| Making websites machine-readable can raise the proportion of tasks AI agents complete | Controllable lab system | Weak to medium; only one synthetic website, not separated out |
| Most AI crawlers don't run JavaScript | Self-tests by people in the industry + very strong industry consensus | Medium; but most claims ultimately trace back to the same analysis from late 2024 (see next section) |
| Blocking often happens at the CDN/WAF layer | Industry consensus + samples by several people in the industry | Medium; proportions vary greatly between samples |
| Training crawlers and on-the-spot reading should be handled separately | Multiple sets of server logs from people in the industry + one repeated, controlled test | Medium |
| llms.txt is effective on its own | None | **No evidence at present** |

**Two things to remember in particular:**

1. Most accessibility research only proves that "not being readable puts you at a disadvantage"; it **does not prove that "being readable means being cited"**. Accessibility is a **necessary condition** (without it, it definitely won't work), not a **sufficient condition** (with it, it still may not work).
2. **The number of times crawlers come to fetch doesn't equal being cited.** The industry generally believes that fetch volume alone is not enough to measure your visibility in AI.

---

## 8. Six things still being debated

### Controversy 1: Is llms.txt any use at all?

**llms.txt** is a text file placed in a website's root directory; some people have proposed using it to tell AI "where the key points of my website are".

**The side that thinks it's useless:**

- Researchers ran repeated tests on real AI search: of the **1,047** source websites examined, **16.9%** had llms.txt. But this kind of technical markup had **no relationship** with answer accuracy (correlation coefficient about -0.04, practically zero).
- Several independent server logs point in the same direction. Someone in the industry tested this themselves:
  - A website launched a 38 KB llms.txt on August 31.
  - From September 2 to 16, this file was requested **299 times** in total: **240** were the website's own monitoring program, **59** were real requests, and **only 2 were AI crawlers** (both a crawler called Amazonbot).
  - During the same period, GPTBot fetched **920** times across the site, ClaudeBot **1,494** times and OAI-SearchBot **631** times, but each requested llms.txt **0** times.
- Another person in the industry examined **billions of lines** of client logs and tracked **more than 100** websites, and never saw AI tools request llms.txt.
- Most in the industry believe llms.txt doesn't help AI visibility or citations (**33** in support, **4** against); most large language models don't even look for this file.
- Someone in the industry observed: in citation data for **200** queries, **fewer than 3%** of the websites had llms.txt, and llms.txt pages themselves **were never cited**.
- Another person in the industry added llms.txt for a month and then removed it, and saw **no change at all** before and after.

**The side that thinks it's useful, or is holding off on a conclusion for now:**

- Google's official search documentation says special files like llms.txt are **not needed**. But Google's web page testing tool **has added an llms.txt check item**. Some in the industry read the latter as "it has an effect"; others point out that the testing tool can only confirm the file exists, and says nothing about whether any AI actually uses it.
- Someone in the industry observed: among **50** businesses, the **5** that had llms.txt were named by AI **77%** of the time, versus **49%** for those without. But the sample with llms.txt was only 5 businesses, and these websites had also made other changes to make them easy for machines to read.
- Some in the industry believe the value of llms.txt lies mainly in the fact that "the process of writing it forces you to sort out which pages matter"; or that it's useful for technical documentation websites for software development, because AI that helps people write code might read it.
- One company claims that in their logs, AI crawlers request llms.txt far more often than other pages. But this has not been independently verified, and it contradicts the results of the several independent logs above.

**This book's position:**
One study found it unrelated to accuracy; another study included it in a bundle without separating it out. **There is currently no evidence that llms.txt is effective on its own.**
It costs very little; if you want to put one up, you can, but don't treat it as the focus of your accessibility work.

### Controversy 2: Is it any use to prepare a separate Markdown version for AI?

Markdown is a very lean plain-text format. Some argue: make a separate Markdown version of every page, and AI will read it more easily.

- Someone in the industry tested this themselves: after deploying site-wide `.md` versions and llms.txt, training and indexing crawlers fetched **56** files **177** times. But **on-the-spot reading crawlers read almost only HTML**:
  - ChatGPT-User: read **1,936** HTML and **0** `.md`;
  - PerplexityBot: **306** HTML, **0** `.md`;
  - Claude-User: **38** HTML, **1** `.md`.
- Another person in the industry saw the same phenomenon in about three months of logs from two small blogs.
- Someone in the industry tested: Markdown mirror pages were crawled by Google within a few days, but ChatGPT and Perplexity **still cited the HTML version**, and the citation rate didn't change within **60 days**.
- Someone in the industry tested: serving Markdown to AI crawlers for **16** blog URLs, visits grew **52%** within **30 days**; but blog URLs that **did not** serve Markdown also grew **43%**. So it can't be determined that Markdown itself made the difference.
- Someone in the industry observed: in a grouped comparison test across **6** websites and **381** pages, pages that served Markdown got only about **1** extra bot visit (median) over three weeks.
- **A report from the opposing side:** Someone in the industry tested this themselves: after providing `.md` versions for **20** popular articles, Perplexity and ChatGPT search discovered and cited the Markdown versions faster, and AI's fetch rate **doubled**. But this report **had no control group**.

**Observations on cost:**

- Someone in the industry measured **300** websites: the median page needs **2,592 tokens** (a token is the unit AI uses to count amounts of text). About **half of this is not body text**, and about **one-fifth is navigation bars, headers and footers**.
- The **7** websites that provided Markdown versions had a median of **962 tokens**, which does save a lot.
- But of these 7 websites:
  - **6** were missing a technical header called `Vary: Accept`, so caching systems might send the wrong version to the wrong visitor;
  - **3** had Markdown versions that **lost the body text**.
- Another person in the industry pointed out: mainstream AI crawlers don't send the request header saying "I want Markdown" (`Accept: text/markdown`). So an approach that relies on this header to switch versions might never be triggered.

**Summing up:**
The more consistent observation at present is: **on-the-spot reading when answering users' questions reads HTML.**
Facts you want to influence the answer must be placed in **the HTML that humans see**. A Markdown version may save bandwidth and may be read by indexing crawlers, but there is no reliable evidence that it increases citations.

### Controversy 3: Does AI read JSON-LD structured data?

**Structured data** is information in a standard format written for machines to read (such as schema markup); the common way of writing it is called JSON-LD.

- **One side says it doesn't read it:** Someone in the industry tested this themselves: when AI converts a page to plain text, it throws away the entire head, and the read result for JSON-LD was zero. Another person in the industry reported that neither ChatGPT's nor Gemini's fetching uses schema data.
- **The other side says it does:** Someone in the industry tested this themselves: **92%** of JSON-LD output directly by the server was picked up by at least two AI crawlers. Someone in the industry observed that Gemini could read and repeat the schema in a page. And someone in the industry who analyses logs suggests: put JSON-LD in the same HTML that humans see, so that on-the-spot reading crawlers can also get machine-readable facts.

**The two sides don't entirely contradict each other.** "The crawler retrieved HTML containing JSON-LD" and "the model actually used the JSON-LD when answering" are two different things. Research on AI agent scenarios also included structured data in a bundle and didn't separate it out.

**Only one thing is certain: structured data inserted after the fact only by browser-side programs simply doesn't exist for crawlers that don't run JavaScript.**

### Controversy 4: Does "AI crawlers don't run JavaScript" still hold now?

This is industry consensus. But someone in the industry pointed out a few problems:
- almost every citation ultimately traces back to **the same analysis from December 2024**, about 20 months ago now;
- the party that published that analysis itself **sells "server-side page assembly" services**;
- server access logs can only record "what the other side requested", and **cannot record "whether the other side ran JavaScript"**.

Another person in the industry saw in their logs that OpenAI's training crawler made a small number of JavaScript-related requests; user-triggered on-the-spot reading did not.

**How to handle it:** Don't wait for this debate to reach a conclusion. Directly compare your **server's raw response** with the **assembled page**. As long as important content appears only in the latter, treat it as unreadable by AI.

### Controversy 5: Is robots.txt obeyed?

- Someone in the industry tested this themselves: in **48 days** of logs, GPTBot and Meta-WebIndexer **never checked** robots.txt.
- Another person in the industry tested: block a test page in robots.txt, then ask eight AI assistants to read it:
  - The assistants from ChatGPT, Claude and Meta **refused to read it** (Claude even explicitly reported "the website does not allow automated access");
  - Gemini, Grok and Manus **read it anyway**;
  - Copilot and Perplexity **did not try**.
  - The tester found that Google's documentation explains: user-triggered fetches are generally **not bound by robots.txt**.
  - This is only one domain, three rounds of testing, and involves only user-triggered fetches.

So **robots.txt can neither guarantee keeping crawlers out nor guarantee letting them in.**

### Controversy 6: Is accessibility really a common bottleneck?

Different samples give very different proportions. The following are all figures observed by people in the industry:

| What was observed | Sample | Result |
|---|---|---|
| Declared blocking in robots.txt | About 510,000 websites | 16.8% blocked large language model crawlers |
| Declared blocking in robots.txt | 300 small and medium businesses sampled from each of three industries | Law firms 1.8%, home services 5.4%, travel 3.0% |
| Blocked at the "guard layer" (requests with a named AI identity refused, ordinary requests passed) | 131 websites, mainly news, online software services (SaaS) and e-commerce | About 21% |
| Blocked at least one major large language model crawler, mostly at the CDN or host layer | About 3,000 websites, mainly business-to-business (B2B) online software services | 27% |
| Fetching small and medium business websites with an AI identity | About 17,000 French small and medium business websites | Accessibility was almost never the bottleneck |

These figures measure different layers and use different samples, so **they cannot be ranked against each other**.

What can be seen is:
- **Declared blocking in robots.txt is generally rare;**
- **Blocking at the "guard layer" is clearly more common on websites that use a CDN, B2B online software services and media websites.**

Someone in the industry also warns: if you test yourself from a data-centre network address, using an identity that "claims to be AI", getting a 200 (success) doesn't mean real crawlers can get it too, because CDNs check real crawlers' network address ranges. The reverse is also true.

**Another kind of counter-example: readable, but not cited.**

- Someone in the industry observed: a website of about **100,000 pages** was fetched about **430,000 times** by AI crawlers within **30 days**, but fetch volume had **no relationship** with whether it was cited. What actually got cited were pages that "state one fact per page, have stable URLs and are easiest to verify".
- Someone in the industry who has reviewed about **17,000** websites also believes: most websites aren't cited because their pages **have no answer that can be used directly**, not because of technical problems.

---

## 9. Real cases

### Case 1: Under "block AI by default", a new entity was cited on day 6

- **What was done:** Create a new entity with absolutely no footprint on the internet. Register the test plan in advance, and query five AI systems that go online every day. Each answer was rated "correct", "not found" or "hallucination" (made up by AI), for about **16,000** scoring points in total.
- **What was observed:**
  - The CDN's default AI block returned 403 (Forbidden) to the listed training crawlers on 22 of the 23 days; but on the same day, the on-the-spot reading crawlers were let through normally.
  - The entity was cited on **day 6**, thanks to the knowledge graph and third-party mentions.
  - Discussion volume on social platforms increased **23 times**, and citations **did not increase**.
  - What really had an effect was "structured identity": entries in public entity databases, stable identifiers, and a real website.
- **How long:** 23 days.
- **What this shows:** Training crawlers and on-the-spot reading have different jobs (Section 2); there is more than one path by which AI finds you (Section 5).
- **Limitations:** This is an experiment on a single entity; it can only illustrate the mechanism and doesn't represent a general rule.

### Case 2: A CDN switch quietly overrode the website's robots.txt

- **What happened:** A webmaster found that his website didn't appear in ChatGPT, Perplexity or AI summaries. But the robots.txt output by the website's code explicitly allowed all AI crawlers.
- **How it was discovered:** He used `curl` (a free command-line tool that can fetch a URL directly, like a crawler) to retrieve the robots.txt **actually live online**, and found an extra managed block at the very top **that he hadn't written**, blocking GPTBot, ClaudeBot, Google-Extended and others.
- **Cause:** The CDN's "block AI crawlers" switch inserts its own rules at the front of robots.txt.
- **What this shows:** The door has three layers (Section 3).
- **Limitations:** This is a report from a single person in the industry and has not been independently verified. But the checking method it reveals is universal: **look at the file actually served live, not just your own source code.**

### Case 3: A "block everything" rule left behind by an old plugin

- **Observation:** Someone in the industry who reviewed **50** local service websites (plumbing and electrical, air conditioning, dentists, lawyers) reported: one common problem was GPTBot and ClaudeBot being blocked by robots.txt. This wasn't intended by the owners; it was a "block everything" rule (`Disallow`) left behind by an **old SEO plugin**.
- **Another small-business sample:** Of the **10** websites flagged as "blocking AI crawlers":
  - **4** used a single rule to block **all** crawlers, including on-the-spot reading crawlers and even Google's search crawler (Googlebot). It looked as though "test environment" settings had been carried over to the live website;
  - **9** blocked meta-externalagent;
  - Several completely unrelated websites had **the same block list in exactly the same order**. That wasn't 10 people each making their own decision; it was **the same default**.
- **Result:** This reviewer reported that fixing just the blocking usually led to improvement in appearances in AI search within **2 to 4 weeks** at the earliest. This is a self-test result by someone in the industry and has not been independently verified.
- **What this shows:** The door has three layers (Section 3).

### Case 4: Prices existed only in the "assembled" page

- **Observation:** Someone in the industry scanned an online software service (SaaS) website:
  - the website's raw HTML was about **300 words**, and about **1,033 words** after assembly;
  - the pricing page's raw HTML was **194 words**, and **511 words** after assembly;
  - and the raw HTML contained **not a single price figure**, only plan names.
- **Consequence:** When AI assistants were asked about prices, they knew what plans there were, but couldn't say how much they cost.
- **Fix:** The website team found the cause: a "pre-assembly" program described the plans only in text, while prices were filled in from the database on the browser side. After the fix, fetching the pricing page with `curl` now returned the prices.
- **Unexpected finding:** The same check also found that the list of "pre-assembled" pages **was missing 7 pages**. This was only discovered after a search crawler found those pages.
- **What this shows:** AI reads the raw response (Section 4).
- **Limitations:** This is a first-hand observation of a single website and can only be treated as an example.

### Case 5: Building a separate parallel website for AI

- **What was done:** A little-known app brand found that ChatGPT, Claude and Perplexity were all citing it, but **with the wrong description**. So it built a `/ai/` parallel version of the whole site:
  - same content, but with distractions like the navigation bar, animations and "Buy now" call-to-action buttons removed;
  - every page rewritten as direct Q&A, with the answer placed within the first **75 to 120 words**;
  - every page pointing back to the original human-facing version with a marker (canonical);
  - placed in a separate sitemap;
  - made discoverable to AI through llms.txt, an "alternate version" link marker (`rel="alternate"`), and the way AI fetches directly when citing.
- **What was observed:** Self-test by someone in the industry (repeated, controlled): within **5 weeks**, the coverage of AI citations expanded by **12%**, and traffic referred from AI rose by **60%**. No new external links were added during this period.
- **Note:**
  - This was a bundle of changes; it's impossible to tell whether the content rewrite, readability, or the way AI discovered it made the difference;
  - and it's inconsistent with the observation in Controversy 2 that "on-the-spot reading crawlers only read HTML", so more repeated verification is needed.

### Case 6: Agent experience, and "being left out"

- **What was done:** Researchers ran **37,927** real AI agent query sessions on **1,056** business websites, comparing them in pairs matched by fame, AI's existing memory of the brand (**brand prior**) and other conditions.
- **What was observed:** For readable websites, **78%** of answers came from their own pages and **20%** were explicitly recommended; for unreadable websites, it was **58%** and **11%**. When a website was unreadable, AI agents substituted content from third parties or competitors, **rather than making things up**.
- **What this shows:** If it can't be read, it doesn't exist (Section 1); getting in isn't enough, it also has to be usable (Section 6).
- **Limitations:** Study by a service provider, bundled score; see Section 7 for details.

### Case 7: a well-known platform that blocks all AI crawlers was named by AI but cited 0 times

- **What was done:** When writing this book, we tested ChatGPT ourselves through the API (method in Chapter 4; the sample is very small and no one else has independently verified it). The same swimming-recruitment question was asked in 5 English phrasings, 2 times each, 10 times in total.
- **What was seen:** A well-known swimming data platform blocks GPTBot, OAI-SearchBot and other AI crawlers in its robots.txt. In 6 of the 10 runs, AI used `site:` to name this platform as a place to search, but it cited it **0 times**; the platform appeared only once in the search results. When not online, AI knew this platform well (see Chapter 5, Case 9). In other words, AI wanted to look it up but could not read it.
- **Limits:** Only one topic and one model, with no independent verification; there was also no comparison (we did not test what happens when the same platform allows the crawlers).
- **What it shows:** If AI can't read you, you don't exist (Section 1); which crawler you block changes the result (Section 2).

### Case 8: a new website less than four months old became the most-cited source through search alone

- **What was done:** The same 10 runs as Case 7.
- **What was seen:** A website that collects swimming-recruitment times, registered only in June 2026, was cited in **9** of the 10 runs, accounted for **44%** of all cited links, and was usually the first source cited. When not online, AI said 5 times out of 5 that it did not know the site, the same answer it gave for a made-up web address (see Chapter 5, Case 9). So it was cited entirely because search found it, not because of AI's memory.
- **What this website has:** robots.txt allows all crawlers; the data is written directly in the HTML; each "competition level × event" has its own page; page titles are almost the same as the search terms AI generated; the data source and update date are stated; pages link to one another. After reading one page, AI followed the pattern of the web addresses and used `site:` to search for other pages on the same site.
- **Limits:** Only one website and one topic; these features exist together, so it is impossible to tell which one is doing the work.
- **What it shows:** If AI can't read you, you don't exist (Section 1); important content should be in the original HTML (Section 4); it also echoes Chapter 4: "match the queries AI rewrites".

### Counter-example: mistaking "an indexing problem" for "AI being blocked"

After blocking AI crawlers for a few weeks, someone in the industry found that his indexing in Google kept dropping. He suspected the website firewall rules were causing collateral damage, so he switched off all the rules to troubleshoot.

Only later did he discover that the real cause was a **mistakenly submitted "temporary URL removal" request**, which caused an indexing freeze lasting **six months**.

The lesson: **verify accessibility problems layer by layer; don't jump straight from symptoms to a guess at the cause.**

---

## 10. What to do

### 1. First confirm the status of the three types of crawler, and decide separately

| What to do | Strength of evidence |
|---|---|
| Decide separately whether to allow the three types of identity: "collecting training data", "building indexes" and "reading on the spot". If you want to appear in AI answers, **at least allow the identities that build indexes and read on the spot** (e.g. OAI-SearchBot, ChatGPT-User, Claude-User, Perplexity-User) | Self-tests by people in the industry (repeated, controlled) + multiple sets of logs |
| If you care about Gemini and AI summaries, **don't block Google-Extended** | Repeated tests on real AI search (correlation) |
| After searching for GPTBot in robots.txt, **search again for OAI-SearchBot**. Writing only the former means making only half the decision | Self-test by someone in the industry: of 72 companies, 18 had written GPTBot, only 11 had written OAI-SearchBot, and 0 had written OAI-AdsBot |
| If you don't want a page to appear in ChatGPT, use a noindex tag rather than just blocking it in robots.txt; and the crawler must be able to read that page to see the tag | OpenAI official documentation |
| Have other web pages link to your important pages: OpenAI also discovers web addresses from other pages | OpenAI official documentation |

### 2. Check layer by layer; don't look only at robots.txt

1. **The sign (declaration layer):** Use `curl` to retrieve the robots.txt **actually live online**. Confirm there are no blocks inserted by a CDN or plugin, and no catch-all "block everything" rule (`Disallow: /`).
2. **The guard (enforcement layer):** Request the same page with each AI identity and with an ordinary browser identity at the same time, and compare the status codes and content sizes returned. If even the ordinary browser identity's request is refused, that's a general protection problem, not an AI-specific policy. Remember: this only tests "the response path"; it doesn't mean real crawlers will be treated the same way.
3. **On-the-spot test:** Paste your URL directly to an AI assistant such as ChatGPT and ask it "What services does this website offer?" A blocked website will fail outright; you can confirm in about ten seconds (someone in the industry tested this themselves).
4. **Are there words in the book (content layer):** Use `curl` or "view source" to get the server's raw response, and compare it with the assembled page. Prices, specs, FAQ answers, headlines and structured data that appear only in the assembled page all need to be changed.
   - Someone in the industry observed: 11 websites requested with an AI identity all returned 200 (success); but in **2** of 10 valid comparisons, the word count of the assembled page was **more than double** that of the raw response. The problem was in "assembly", not "blocking".

### 3. Make sure key content exists in the raw HTML

| What to do | Strength of evidence |
|---|---|
| Output key content and structured data using "assembled by the server before sending" (server-side rendering) or static HTML | Most in the industry believe this (very strong consensus) + self-tests by people in the industry |
| Use tag managers only for analytics tracking, not for outputting content AI needs to see | Self-tests by people in the industry |
| Confirm that text in carousels, collapsible sections and animations exists in full in the raw HTML | Observed by someone in the industry |
| For the list of "pre-assembled" pages, use a fixed process to make sure new pages are always added, to avoid more and more being missed | Observed by someone in the industry |
| Put facts you want to influence the answer (prices, specs, qualifications) in **the same HTML that humans see** | Self-tests by people in the industry (on-the-spot reading crawlers only read HTML) |

### 4. Look at your own server logs, but first confirm who the visitor is

- **Use server logs, not just analytics tools.** Website analytics tools usually filter out bots; analytics programs running in the browser also can't see crawlers that don't run JavaScript. Some hosting platforms keep request logs for only about **one hour**, so you need to store them long-term yourself.
- **Check the network address (IP).** The name a crawler gives is just a text field that can be filled in with anything.
  - Self-test by someone in the industry: over two months, **394** source addresses claiming to be ChatGPT were **all outside** the address ranges published by OpenAI; **79** of them were probing sensitive paths that store passwords and settings, such as `/.env` and `/.aws/credentials`.
  - Someone in the industry observed: of **14,771** verifiable visits, **5,577** were impostors; **38.3%** of the impostors were looking for passwords or configuration files.
  - How to check: compare against the address-range files published by each AI company. The "reverse domain name lookup" (reverse DNS) method works for Google's search crawler, but someone in the industry checked and found it **doesn't work** for GPTBot.
- **Look at on-the-spot reading crawlers, not total fetch volume.** A visit from an identity with "User" in its name means a real user asked a question a few seconds earlier and AI read this page for it. Someone in the industry observed that the ratio of fetches to subsequent real human visits is mostly **ten to one or more**.
- **Treat crawler logs as a "debugging tool":** use them to confirm whether pages were fetched, whether there are non-existent URLs hallucinated by AI, and whether any pages are too slow. As for your **visibility** results, measure them by tracking AI answers, not by logs.

### 5. Prepare machine-readable facts for AI agents

| What to do | Strength of evidence |
|---|---|
| Let AI agents get content without relying on JavaScript; provide structured data; have bot protection let AI agents through | Repeated tests on real AI search (bundled, not separated out) |
| On websites where AI agents need to take action, add machine-readable data, hint markup for "what actions can be done", and data-date fields | Under lab conditions (single website, not separated out) |
| For dataset-type content, publish standard machine-readable descriptions | Under test conditions with given web pages (limited to dataset scenarios) |
| Provide a simple "machine-readable facts" URL so AI cites the latest figures | Observed by someone in the industry |
| Whether e-commerce products can appear in AI shopping may depend on whether the product data feed is complete (product identifiers, variant attributes such as size and colour, policy data such as returns and exchanges), not just page content | Observed by someone in the industry; can only be treated as a clue |
| Following WAI-ARIA practice, add clear roles, labels and states to buttons, menus and forms | OpenAI official documentation (for the AI agent in ChatGPT Atlas) |

### 6. When crawlers come too aggressively, rate-limit rather than block

AI crawlers sometimes suddenly fetch in large volumes. Someone in the industry reported that GPTBot once reached **114 requests per minute** over **3 minutes**.

Someone in the industry observed: after setting a rate limit of "at most 60 per 60 seconds", returning "too many requests" (the 429 status code) when exceeded, the crawler slowed down after about **one week**.

**Rate-limiting is less likely than a full block to cause collateral damage to on-the-spot reading crawlers.**

---

## Key points of this chapter

1. **If it can't be read, it doesn't exist, and failure is silent.** When AI can't read you, it doesn't report an error; it replaces you with someone else's content.
2. **AI crawlers fall into three types, collecting training data, building indexes and reading on the spot, and you should decide on each separately.** Blocking training crawlers won't make you disappear from real-time answers; blocking indexing and on-the-spot reading is the real loss.
3. **The door has three layers:** the robots.txt sign, the CDN/WAF guard, and the content of the raw response. robots.txt being fine doesn't mean AI can get the content.
4. **AI reads the server's raw response.** Prices, FAQs and structured data that exist only after JavaScript assembly don't exist for most AI crawlers.
5. **AI has several catalogues behind it, and they rarely overlap.** Being indexed by traditional search engines is itself part of AI accessibility.
6. **AI agent scenarios require "usable", not just "findable".** Readable websites are used more often to answer with their own content and recommended more often, but the existing evidence is all bundled and not separated out.
7. **llms.txt and Markdown mirrors have not so far been proven to increase citations.** On-the-spot reading when answering questions reads HTML.
8. **Accessibility is a necessary condition, not a sufficient condition.** Fetch volume has no relationship with citations; once you can be read, whether you get picked depends on the factors covered in the following chapters.

---

## Remember in one sentence

**If AI can't read you, it will quietly use someone else instead; so confirm layer by layer: allow the right crawlers, remove the invisible guards, and write your important facts into the raw HTML.**

---

## What you can do tomorrow

1. **Open robots.txt and look at the three types of crawler separately.** Search for GPTBot, then search for OAI-SearchBot, ChatGPT-User, Claude-User, Perplexity-User, Google-Extended and meta-externalagent. If you want to appear in AI answers, at least allow the identities that build indexes and read on the spot; if you care about Gemini and AI summaries, don't block Google-Extended.
2. **Use `curl` to fetch the robots.txt "actually live online".** See whether there's a block quietly inserted at the top by a CDN or plugin, and whether there's a block-everything rule like `Disallow: /`.
3. **Check the "block AI crawlers" or "bot protection" settings of your CDN, web firewall and host.** Request the same page separately with an AI identity and an ordinary browser identity, and compare the results. Remember, this is only a response-path test.
4. **Paste your URL to an AI assistant** and ask "What services does this website offer?" In ten seconds you'll know whether it can read it.
5. **Compare the raw response with the assembled page.** Pay particular attention to prices, specs, FAQ answers, headlines, structured data and language-version tags. Anything that appears only after assembly should be changed to direct server output or static HTML.
6. **Use tag managers only for analytics tracking**; don't use them to output structured data or content AI needs to see.
7. **Confirm that text in carousels, collapsible sections and animations exists in full in the raw HTML.**
8. **If you use "pre-assembly", write "new pages must always be added to the list" into a fixed process.**
9. **Facts you want to influence the answer** (prices, specs, qualifications) must always be placed in the HTML that humans see.
10. **Start storing server logs long-term**, especially if your host keeps them for only one hour.
11. **Check crawlers' IPs** against the address ranges published by each AI company. Don't use reverse DNS to verify GPTBot.
12. **Focus on the number of on-the-spot reads by identities with "User" in the name**, not total fetch volume; treat logs as a debugging tool, for finding pages that weren't fetched, URLs hallucinated by AI, and pages that are too slow. Measure visibility by tracking AI answers.
13. **Prepare machine-readable facts for AI agents:** content that doesn't depend on JavaScript, structured data, and protection settings that let AI agents through; on websites where AI agents need to take action, add action hints and data-date fields; publish standard descriptions for dataset-type content; consider providing a simple machine-readable facts URL.
14. **If you run e-commerce**, check whether your product data feed is complete: product identifiers, variant attributes, policy data.
15. **When crawlers come too aggressively, rate-limit first** (e.g. 60 per 60 seconds, returning 429 when exceeded); don't go straight to a full block.
16. **When you find "I can't be seen in AI", check layer by layer**: the sign, the guard, the content, and traditional search indexing; don't jump straight from symptoms to conclusions.
17. **For pages you don't want to appear in ChatGPT, use noindex**, and make sure the crawler can read that page; for important pages you want found, have other web pages link to them.
18. **Add accessibility labels to buttons, menus and forms** (ARIA roles, labels and states), so AI agents know what each element does.

---

## Stop doing this

- **Stop** using block-everything rules like `Disallow: /`, or applying plugin or CDN default block lists directly without checking what's in them.
- **Stop** thinking that blocking GPTBot means exiting AI answers; and **stop** thinking that if robots.txt says allow, AI can read it.
- **Stop** relying only on browser-side JavaScript to insert content or structured data.
- **Stop** counting AI traffic directly by the names crawlers give, or reporting that number to clients. Numbers without IP checks will be inflated by impostor scanning programs.
- **Stop** showing AI and humans different content based on crawler names without handling cache headers; if you make a Markdown version, also confirm the body text hasn't been lost.
- **Stop** treating crawler fetch volume as a visibility metric.
- **Stop** inferring directly from "I can't be seen in AI" that "AI is being blocked". Verify layer by layer.

### Outdated ideas

- **"One robots.txt rule can control an entire AI company."** The company behind ChatGPT already runs four identities with different jobs, and other companies also split into training, indexing and on-the-spot reading.
- **"llms.txt is an AI ranking factor, or the solution for boosting visibility."** There is no evidence to support this; multiple logs show that major AI crawlers hardly ever request it.
- **"You can judge accessibility just by looking at robots.txt."** Blocking at the guard layer doesn't show up in robots.txt.
- **"If you can see it in the browser's developer tools, crawlers can see it."** Developer tools show the result after JavaScript has run.

---

## What is still uncertain

- **Is llms.txt any use at all?** One study found it unrelated to answer accuracy; multiple independent logs show that major AI crawlers hardly ever request it; the supporting evidence has very small samples, or is mixed with other changes, or has not been independently verified. There is currently no evidence that it is effective on its own. It costs little, so you can put one up, but it's not the focus.
- **Is a Markdown version any use?** Most observations show that on-the-spot reading reads only HTML, and no increase in citations has been seen; only a report without a control group says it works. A Markdown version may save bandwidth and may be read by indexing crawlers, but there is no reliable evidence that it increases citations.
- **Does AI read JSON-LD?** "The crawler got it" and "the model used it" are two different things, and there are claims on both sides at present. The only certainty: structured data inserted only on the browser side doesn't exist for crawlers that don't run JavaScript.
- **Is "AI crawlers don't run JavaScript" still true now?** The consensus is strong, but it mostly traces back to the same analysis from December 2024, whose publisher itself sells related services; logs also can't record whether the other side ran JavaScript. The way to handle it is to directly compare the raw response with the assembled page.
- **Is robots.txt obeyed?** Some AIs obey it, some don't, and some crawlers don't even read it; user-triggered fetches are generally not bound by it. The evidence comes from a small number of tests.
- **Is accessibility really a common bottleneck?** Proportions across samples range from "almost never a bottleneck" to about 27%, and they measure different layers, so they can't be compared directly. Blocking at the declaration layer is rare; blocking at the guard layer is more common on websites using CDNs, B2B online software services and media websites. Testing yourself with requests that "pretend to be AI" may not reflect how real crawlers are treated either.
- **Within agent experience, which item is most useful?** Existing research all involves bundled changes, without separating out each item's effect; the e-commerce experiment had only one synthetic website; the large observation was carried out by a service provider.
- **Does building a separate parallel website for AI (Case 5) work?** One case saw increases in citations and traffic, but it was a bundle of changes, and it's inconsistent with the observation that "on-the-spot reading reads only HTML", so more repeated verification is needed.
- **Why does AI often read an old version?** At present, only a single tester's observation shows that most AIs read a cached version; it can only be treated as a clue.
