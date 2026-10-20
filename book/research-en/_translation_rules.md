# English translation rules: research edition

Source: the Traditional Chinese research edition in `book/research-zh-hant/`. Title: **GEO Lab: Research Edition. A Textbook on Generative Engine Optimization**. Readers are practitioners and researchers who want the evidence behind each claim.

1. **Translate only.** Do not add, remove, summarise, reorder, soften or strengthen anything. Every sentence, list item, table row, heading, example and caveat appears in the translation, in the same order.
2. **Keep the Markdown structure identical**: same heading levels, bold, lists, tables, block quotes, code blocks and mermaid diagrams (translate the text inside them). The source has no horizontal rules; do not add any.
3. **Numbers**: keep every number unchanged. Convert Chinese units only in form: 「約 3.1 萬」→ "about 31,000"; 「3 成」→ "30%". Paper numbers such as 2606.25787 and grade letters such as [B] stay exactly as written.
4. **Terminology**: use the English column of `book/zh-hant/_術語表.md` consistently. Keep product, platform and crawler names exactly (ChatGPT, GPTBot, Google AI Overviews, Perplexity…). 搜索/搜尋 → "search".
5. **Evidence-strength phrases** have fixed renderings. Use these exactly, every time:

| Source phrase | English |
|---|---|
| 大規模真實用戶實驗顯示 | Large-scale experiments with real users show |
| 在真實 AI 搜索引擎上重複測試發現 | Repeated tests on real AI search engines found |
| 在給定網頁的條件下 | When the pages are supplied to the engine |
| 在可控的實驗系統中 | In controlled experimental systems |
| 模擬／理論分析表明，機制上可能 | Simulations or theoretical analysis suggest that, in principle, … may |
| 從業者實測（多次、有對照）發現 | Practitioners' repeated, controlled tests found |
| 從業者實測報告 | Practitioners report from their own tests |
| 未經獨立驗證 | not independently verified |
| 從業者普遍認為 | Practitioners widely believe |
| 有從業者觀察到 | One practitioner observed |
| 有業者宣稱……，但未經獨立驗證 | A vendor claims …, but this has not been independently verified |
| 證據有限 | limited evidence |
| 服務商 (as a tag in source lists) | vendor |

   Grades: A, B, C, D, E for papers and R-A to R-D for practitioner reports stay as letters.

6. **Recurring section names**: 本章要回答的問題 → "Questions this chapter answers"; 核心原理 → "Core principles"; 原理 5.1 → "Principle 5.1"; 證據有多強 → "How strong is the evidence"; 爭議與反例 → "Debates and counterexamples"; 案例 → "Cases"; 怎麼做 → "What to do"; 不要做 → "Do not do"; 已經過時 → "Already outdated"; 本章要點 → "Key points"; 開放問題 → "Open questions"; 來源追溯 → "Source trail".
7. Chapter heading format: `# Chapter N: Title`. Appendix: `# Appendix A: Title`. Cross-references 「第 N 章」→ "Chapter N", 「5.3 節」→ "Section 5.3". File references such as `教材/第05章_來源生態.md` become the English file name given in your task.
8. **Never use em dashes.** Use commas, colons, parentheses or separate sentences. En dashes are fine for number ranges (24.8%–44.3%).
9. Clear, precise international English, as in a good academic textbook for practitioners. Avoid filler and AI phrasing ("It's worth noting", "Notably", "Crucially", "delve", "landscape", "In other words").
