# GEO Lab

[English](README.md) · **繁體中文**

**一本持續更新的生成式引擎優化（GEO）教材：不斷納入新研究與原創實驗。**

AI 搜尋（ChatGPT、Gemini、Perplexity 等）怎麼決定要找到、讀取、引用、推薦哪些網站？這個倉庫用一本持續更新的教材來回答：

- **證據分級**：整理自 579 篇研究論文與約 14 萬則從業者討論，每一個結論都標明證據強弱。
- **永遠是新的**：定期篩選新論文納入教材；每次修改都有版本號與[更新記錄](CHANGELOG.md)。
- **原創實驗**：我們自己在 AI 搜尋上做實驗，結果連同方法與限制寫進教材。
- **多語言**：English、繁體中文、简体中文。

## 內容

| 資料夾 | 內容 |
|---|---|
| `book/en/` | 通俗版（英文） |
| `book/zh-hant/` | 通俗版（繁體中文） |
| `book/zh-hans/` | 通俗版（簡體中文） |
| `book/research-zh-hant/` | 研究版，含證據表（繁體中文） |
| `website/` | 三種語言的網站 |
| `papers/` | 論文索引與精讀筆記（不含 PDF） |
| `framework/` | 教材框架與數據審查方法 |
| `scripts/` | 建站、轉換與檢查腳本 |

## 閱讀

用瀏覽器打開 `website/index.html`，或在本機啟動：

```bash
python -m http.server 8765 --directory website
```

然後打開 http://localhost:8765 。Windows 上也可以直接雙擊 `start-website.bat`。

## 授權

- **教材內容、網站、筆記與框架文件**：[CC BY-NC-ND 4.0](LICENSE-CONTENT.txt)。可在非商業用途下原樣分享，並須註明出處；不得散布改編版本（包括翻譯）。
- **代碼**：[MIT](LICENSE)。

## 引用方式

> ivantsai1982. *GEO Lab: A Living Textbook on Generative Engine Optimization*, version x.y.z. https://github.com/ivantsai1982/geo-lab

引用時請註明版本號，因為內容會持續更新。
