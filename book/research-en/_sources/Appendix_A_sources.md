# Appendix A source mapping (not part of the main text)

Evidence pack: internal evidence pack (not published) (Section A disagreement table, Section B paper notes; Sections C/D/E/F are empty)
Consensus report: the consensus report (not published) (issue number = issue cluster in the report; for/against = number of authors)

## Part 1: Disagreements between studies

### A1 Statistics, quotations, source citations
- Position one: 2311.09735 (D; PAWC +30–40%, subjective +15–30%, domain differences, Fluency+Statistics +5.5%); 2604.19113 FeatGEO (E; 18.31/15.35/10.17% vs 13.34/8.89/5.20%; Statistics and Cite Sources contribute most in ablation; 9 token-level heuristics below baseline)
- Position two: 2506.11097 (E; 3 of 54 scenarios significant; Statistics significantly lowers rank in 19/24); 2609.07559 (C, vendor authors; n=605 no effect; gpt-5.x n=450; -0.33/-0.28/-0.79 vs +42.6/+32.8/+27.7)
- Reconciliation: evidence pack Section A disagreement table, row 1
- Practitioner view: consensus supports, issue 7 "only content with views worth citing or useful information gets cited by generative engines" 32/0

### A2 Structure/Schema
- Position one: 2602.12187 (D; H@20 0.58→0.71 +22%; reranking 1.00→0.83 -17%); 2609.15164 (D; target citations +0.50, total citations not increased; whether cited +4.5pp CI [−1.4,+10.4])
- Position two: 2605.25517 (E; 252,000 trials, 6 models, 18 factors; Structured vs Dense OR 0.79–1.68; gatekeeping factors)
- Reconciliation: evidence pack Section A disagreement table, row 2

### A3 Off-site mentions
- Position one: 2607.15771 (B, vendor authors; 614 queries × 8 interfaces × 3 runs; 160,860 citations; 1 citation 2.1% / ≥11 citations 59.9%; SEO quality score importance 4.52%)
- Position two: 2609.34951 (B, vendor authors, matched observation; 1,056 companies, 37,927 journeys; AX partial correlations +0.62/+0.41/-0.27; 78% vs 58%; 20% vs 11%)
- Reconciliation: evidence pack Section A disagreement table, row 3
- Practitioner view: issue 4, consensus supports: "AI-driven discovery places more weight on consistent mentions of a brand on … external platforms" 13/1; "a core explanation that appears repeatedly across … several platforms is more easily adopted by AI than a single high-quality page" 8/0; "consistent descriptions of a brand across platforms and content on the web …" 7/0; "GEO is about 70% distribution and 30% content …" 11/0; issue 12 "AI models rely more on … consistent narratives in … social platforms" 7/0

### A4 Position
- Position one: 2506.11097 (E; position-1 gain Retail +2.77; crowding is zero-sum)
- Position two: 2608.22697 (E; examined 1.63–5.83 vs 1.12; coefficient about 1/4–1/10 of humans; lowest at positions 68–74; not significant at highest reasoning effort; 78.2%); 2609.15164 (D; observational 42.3 points, controlled +7.9pp, held-out 0.0pp)
- Reconciliation: evidence pack Section A disagreement table, row 4

### A5 llms.txt
- Position one: 2607.14197 (B; 5,460 answers; 16.9% (177/1,047); correlation with accuracy -0.04)
- Position two: 2609.34951 (B; AX package includes llms.txt / Markdown fallback, not broken out)
- Reconciliation: evidence pack Section A disagreement table, row 5
- Practitioner view: issue 2, consensus supports: "llms.txt does not help AI visibility or citation" 33/4; "most LLMs never look for llms.txt at all" 8/0; "AI crawlers are often … blocked at the CDN or WAF layer" 38/9; "most AI crawlers do not execute JavaScript" 23/1

## Part 2: Gaps between practitioner consensus and research

### B1 Answer first
- Consensus: issue 7 "content that provides clear, direct answers and is structured is more easily extracted and cited by AI" 45/0; "LLMs prefer clearly structured, direct answers … especially at the start of the page" 29/0; "AI prefers … compact paragraphs" 18/0; "put the direct answer at the top of the page (for example in the first 100 to 150 words)" 18/0
- Research: 2602.12187 (answer first helps reranking; body-only / AutoGEO falls behind); 2605.25517 (formatting ineffective); 2609.15164 (redistribution)

### B2 SEO and GEO
- Consensus: issue 13 "AEO is an evolution or extension of SEO …" 64/27; "a solid SEO foundation is … the main route" 51/8; "good Google rankings do not guarantee AI visibility" 10/0; "GEO is 90% SEO" 16/4
- Research: 2506.11097 (position gain); 2602.12187 (body-only changes fall behind at retrieval/reranking); 2607.15771 (SEO quality score 4.52%); 2609.34951 (AEO proxy metrics have no effect after controlling for AX)

### B3 Schema
- Consensus: issue 7 "Schema markup on its own has limited effect …" 7/0 (consensus supports); "Schema markup does nothing to improve AI citation" 6/0 (listed as contested in the report)
- Research: 2602.12187 (structural fields include schema, retrieval +22%, reranking -17%); 2609.34951 (structured data is part of the AX package)

### B4 Cited ≠ recommended
- Consensus: issue 8 "a citation by a generative engine does not mean the brand will be recommended or mentioned" 71/0; "being recommended matters more than being cited" 16/0
- Research: 2607.15771 (66%/30%/8%; 8.3%); 2609.34951 (recommendation rate measured separately)

### B5 Single measurements are unreliable
- Consensus: issue 8 "because generative AI recommendations are inconsistent, single measurements are unreliable …" 18/0; "tracking GEO trends requires running a fixed prompt set repeatedly at least 10 times and sustaining it over several weeks" 20/0; "a fixed, representative set of buyer-intent prompts should be built …" 8/0
- Research: 2609.15164 (15% flips, 45% of variance from decoding); 2609.07559 (levers expire as engines update); 2607.15771 (App/Web Jaccard 0.19–0.51)

### B6 Splits among practitioners
- Traffic: issue 9 "ChatGPT brings websites significant traffic" 5/5 (contested); "referral traffic from AI tools … is still negligible" 11/0 (consensus supports)
- Tracking tools: issue 8 "most current AI visibility tracking tools are not reliable enough …" 51/0; "AI visibility tracking is feasible …" 8/0; "the AI search tracking tools on the market cannot provide accurate data" 22/10 (contested); "differences in citation counts between two tools … raw numbers should not be compared directly" 6/0 (contested)
- Old SEO: issue 13 "so-called generative engine optimization … is essentially just the old search engine optimization practices of fifteen years ago" 13/7 (contested)
- Practical advice: issue 9 "directly asking customers … is the most effective way to attribute …" 12/0; issue 14 "when choosing a GEO agency, require it to show specific measurement methods and data for AI visibility …" 8/0; "when evaluating an AI SEO agency, require verifiable results" 25/0

## Summary table and common practices
- Synthesizes the sections above; "zero-sum" based on 2506.11097 §6.4; "expired" based on 2609.07559.
