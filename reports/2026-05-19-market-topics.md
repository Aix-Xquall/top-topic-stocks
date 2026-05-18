# 每日股市熱門話題分析 - 2026-05-19

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **AI 伺服器與資料中心**｜正向｜熱度 13｜市場確認 76.67｜同向 2/3
2. **半導體與晶片供應鏈**｜正向｜熱度 9｜市場確認 76.67｜同向 2/3
3. **散熱與液冷供應鏈**｜正向｜熱度 2｜市場確認 100.00｜同向 1/1
4. **新興題材：TradingKey**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0
5. **先進封裝與 CoPoS**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.04（樣本 8）
- 5日相關係數：-0.01（樣本 8）
- 同向比例：5/8

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| AI 伺服器與資料中心 | 76.67 | 2/3 | 1 | +16.50% | +11.77% |
| 半導體與晶片供應鏈 | 76.67 | 2/3 | 1 | +18.51% | +9.82% |
| 散熱與液冷供應鏈 | 100.00 | 1/1 | 0 | +27.48% | +16.32% |
| 新興題材：TradingKey | N/A | 0/0 | 0 | N/A | N/A |
| 先進封裝與 CoPoS | N/A | 0/0 | 0 | N/A | N/A |
| 記憶體與 HBM 供應鏈 | 0.00 | 0/1 | 1 | -7.89% | -13.86% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-05-08 | 0.03 | 0.48 | +76.92% | 13 |
| 2026-05-09 | 0.10 | 0.55 | +33.33% | 9 |
| 2026-05-10 | 0.45 | 0.55 | +75.00% | 8 |
| 2026-05-11 | -0.03 | 0.47 | +85.71% | 14 |
| 2026-05-12 | 0.00 | 0.42 | +78.57% | 14 |
| 2026-05-13 | -0.08 | 0.07 | +58.33% | 12 |
| 2026-05-14 | -0.29 | -0.20 | +50.00% | 6 |
| 2026-05-15 | -0.17 | -0.08 | +58.33% | 12 |
| 2026-05-16 | -0.12 | -0.69 | +33.33% | 12 |
| 2026-05-17 | 0.09 | -0.34 | +40.00% | 15 |
| 2026-05-18 | -0.01 | -0.17 | +33.33% | 9 |
| 2026-05-19 | 0.04 | -0.01 | +62.50% | 8 |

## 歷史回測摘要

- 回測日期：2026-05-19
- 近5日 3日相關：0.38
- 近5日 5日相關：0.31
- 同向比例：+66.67%
- 權重狀態：未調整

- 方向準確度：+66.67%
- 信心排序準確度：0.38
- 診斷：正相關

調整原因：近 5 日有效樣本 6 筆，低於 15 筆門檻，暫不調整權重。

## 參考來源

| 類別 | 平台 | 用途 | 讀取方式 |
| --- | --- | --- | --- |
| 官方資料 | [公開資訊觀測站 MOPS](https://mops.twse.com.tw/) | 重大訊息、月營收、財報、法說、年報 | 事實驗證 / 基本面來源 |
| 官方資料 | [臺灣證券交易所 TWSE](https://www.twse.com.tw/) | 上市股價、法人、注意股、產業統計 | 價格與市場驗證 |
| 官方資料 | [櫃買中心 TPEx](https://www.tpex.org.tw/) | 上櫃、興櫃公告與交易資料 | 價格與市場驗證 |
| 官方資料 | [SEC EDGAR](https://www.sec.gov/edgar/search/) | 美股 10-K、10-Q、8-K、S-1 與公司申報 | 美股事實驗證 / 財報來源 |
| 財經新聞 | [Yahoo 奇摩股市](https://tw.stock.yahoo.com/news) | 台股、美股、個股新聞與熱門排行 | 題材熱度來源 |
| 財經新聞 | [鉅亨網](https://news.cnyes.com/news/cat/tw_stock_news) | 台股即時新聞、盤後整理、產業與法人動向 | 題材熱度來源 |
| 財經新聞 | [MoneyDJ](https://www.moneydj.com/kmdj/common/listnewarticles.aspx?a=X0200000&svc=NW) | 個股情報、產業新聞、供應鏈脈絡 | 題材熱度來源 |
| 財經新聞 | [經濟日報 money](https://money.udn.com/money/cate/5590) | 證券、產業與法人觀點 | 題材熱度來源 |
| 財經新聞 | [中央社財經](https://www.cna.com.tw/list/afe.aspx) | 公司公告、政策、產業新聞 | 高可信新聞來源 |
| 財經新聞 | [工商時報](https://www.ctee.com.tw/) | 台股、產業、法人與供應鏈新聞 | 題材熱度來源 |
| 科技產業 | [TechNews 科技新報](https://technews.tw/) | 半導體、AI、晶片、先進封裝與供應鏈 | 產業題材來源 |
| 國際財經 | [Reuters Markets](https://www.reuters.com/markets/) | 美股、國際市場、公司與總經事件 | 高可信新聞來源 |
| 國際財經 | [CNBC Markets](https://www.cnbc.com/markets/) | 美股、科技股、盤中市場題材 | 題材熱度來源 |
| 事件日曆 | [Nasdaq Earnings Calendar](https://www.nasdaq.com/market-activity/earnings) | 美股財報日程、股利、IPO、拆併股 | 事件校正來源 |
| 事件日曆 | [Investing.com Economic Calendar](https://www.investing.com/economic-calendar) | CPI、利率、PMI、GDP 等總經事件 | 總經事件校正 |

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Stock Market Today, May 18: Intel Slips After AI Bubble Risk Warning Offsets Early Gains - The Globe and Mail；The AI Chip Rally Is Masking a Dangerous Truth. Half the S&P 500 Is Being Left Behind - AOL.com；Intel Shares Edge Up as AI Chip Trade Runs Into Hurdles - TechStock²

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.76 | N/A | N/A | 108.17 | 108.77 | -0.55% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | +0.66 | +35.93% | +26.99% | 420.71 | 425.19 | -1.05% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.10 | +27.48% | +16.32% | 222.32 | 225.32 | -1.33% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.09 | N/A | N/A | 420.99 | 424.10 | -0.73% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.09 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | 30.12 | N/A TWD / N/A | N/A |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | -13.92% | -8.00% | 423.54 | 506.69 | -16.41% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.07 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | 47.35 | N/A TWD / N/A | N/A |
| 2454 聯發科 | 產業/供應鏈推估 | +0.07 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | 54.18 | N/A TWD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 4 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：risk, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AVGO：新聞直接提及「Broadcom」，共 1 篇新聞命中。 同時符合主題標籤：AI, datacenter。 方向判斷命中詞：risk, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：risk, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Stock Market Today, May 18: Intel Slips After AI Bubble Risk Warning Offsets Early Gains - The Globe and Mail](https://news.google.com/rss/articles/CBMigAJBVV95cUxORTF3ZU0wdlppdE5VclI2M2N2RG8xRnVnaGpYYTN3QnRqcHZxeU5IaWdtdV9oSHhDZHU2TGt6UENmd1BkejdQcUxiZlhEeU4ybVVud2JlclNQOGhGRUo0SDg3M3RPeDR0c1BjRWJ5aFAwNUtJOXJqNnp1UEs0YW9iRFlEWWdpcWJtMjNxcHk5NHV6eU1VY256Q0pQNENZN21vd0lXWVdnTmY0MGNnbENKVUNXRzJwVG9hX3ZTMkRaOTVNQ3FreHVJeTdHNFQ3Zm5JX0swNmxvWmNYaHY5RXRKV3JlWmsybTRQQzV6SVkzNm5Ra1A0Y2F2NGdmVXZENHN1?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 18 May 2026 21:36:54 GMT
- [The AI Chip Rally Is Masking a Dangerous Truth. Half the S&P 500 Is Being Left Behind - AOL.com](https://news.google.com/rss/articles/CBMigAFBVV95cUxNTlJwRnc3enVDUF9Ea245TnVReVFrcTlZVE8wYXF5VWV5aFZNU1R6Yl90NjVfc0Ftck40U3J3TnE4b1RVMTUwcW43Q1Rmb04xUUVWX2c5N1RfLVQ2MTRVbHJJbkM2LS1yQm5yNXo5cF9OWXF6dC0yX01qaHVUdVlzbw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 18 May 2026 17:42:24 GMT
- [Intel Shares Edge Up as AI Chip Trade Runs Into Hurdles - TechStock²](https://news.google.com/rss/articles/CBMilwFBVV95cUxOMUE0eG5QZlFmV1dob1lSeXlpYWdpQy1pVGZfZHZQZFZIX0dqNUFrb3NfQ2RkT1BsVjZYeHo3LWVZWUJMV3htajNzMVRadUM4M25udmZ5MlpNSUNLelAxem9RaEFmZlFBaS13UF9RYWJOOTFhbm9TaHFrYTV5ZS1pTTFsR2xTQnRYZ2YtM3U0NlJGbUgzQjdz?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 18 May 2026 14:45:52 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：The AI Chip Rally Is Masking a Dangerous Truth. Half the S&P 500 Is Being Left Behind - AOL.com；Intel Shares Edge Up as AI Chip Trade Runs Into Hurdles - TechStock²；Intel stock (US4581401001): earnings beat and AI foundry pivot keep momentum in focus - AD HOC NEWS

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.76 | N/A | N/A | 108.17 | 108.77 | -0.55% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.08 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | 30.12 | N/A TWD / N/A | N/A |
| 2303 聯電 | 產業/供應鏈推估 | +0.08 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | 27.89 | N/A TWD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.06 | +27.48% | +16.32% | 222.32 | 225.32 | -1.33% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.06 | N/A | N/A | 420.99 | 424.10 | -0.73% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | +0.06 | N/A | N/A | 681.54 | 724.66 | -5.95% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.03 | -7.89% | -13.86% | 1,333.01 | 1,562.34 | -14.68% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.06 | +35.93% | +26.99% | 420.71 | 425.19 | -1.05% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 3 篇新聞出現相關標籤。 方向判斷命中詞：rally。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 3 篇新聞出現相關標籤。 方向判斷命中詞：rally。

### 主要來源

- [The AI Chip Rally Is Masking a Dangerous Truth. Half the S&P 500 Is Being Left Behind - AOL.com](https://news.google.com/rss/articles/CBMigAFBVV95cUxNTlJwRnc3enVDUF9Ea245TnVReVFrcTlZVE8wYXF5VWV5aFZNU1R6Yl90NjVfc0Ftck40U3J3TnE4b1RVMTUwcW43Q1Rmb04xUUVWX2c5N1RfLVQ2MTRVbHJJbkM2LS1yQm5yNXo5cF9OWXF6dC0yX01qaHVUdVlzbw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 18 May 2026 17:42:24 GMT
- [Intel Shares Edge Up as AI Chip Trade Runs Into Hurdles - TechStock²](https://news.google.com/rss/articles/CBMilwFBVV95cUxOMUE0eG5QZlFmV1dob1lSeXlpYWdpQy1pVGZfZHZQZFZIX0dqNUFrb3NfQ2RkT1BsVjZYeHo3LWVZWUJMV3htajNzMVRadUM4M25udmZ5MlpNSUNLelAxem9RaEFmZlFBaS13UF9RYWJOOTFhbm9TaHFrYTV5ZS1pTTFsR2xTQnRYZ2YtM3U0NlJGbUgzQjdz?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 18 May 2026 14:45:52 GMT
- [Intel stock (US4581401001): earnings beat and AI foundry pivot keep momentum in focus - AD HOC NEWS](https://news.google.com/rss/articles/CBMiwAFBVV95cUxOY21xZGNXWFZkRDBDYnM4OXVFNGFGQUR4TjZYTmpmUkpxNVF3NzRxOGV2RWhWc1dIYmxBMkIxSDdvYk1wbkRlYWQ3OXRXUFk1SzhSNmRuRlpMTUhxSWJXTzNXendlMm9zRGktdVNoT0E4dXp0M0dHYnF4RnA1RmwtNWVZa2RlSVBsLW9wdDFvRG5LaDEwdi1tVGd4YTFKdHZqcXgydlNYanpzMjNZemctZmxVdEdIWE9yRTRocmlDUXo?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 18 May 2026 05:04:59 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：輝達拉貨太猛！台股「散熱一哥」EPS上看95元 最新目標價曝光 - Yahoo股市；邊緣 AI 散熱需求，如何開拓醫療與教育新商機？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.67 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | 39.60 | N/A TWD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.56 | +27.48% | +16.32% | 222.32 | 225.32 | -1.33% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 2 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：拉貨。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：拉貨。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [輝達拉貨太猛！台股「散熱一哥」EPS上看95元 最新目標價曝光 - Yahoo股市](https://news.google.com/rss/articles/CBMijwJBVV95cUxQSEhGQUNRbDhkZGVsT1Q4Xzl4RklFQ1RoeWxMM21SQl80TFdTRndiVWJKT3pKelZoRmpHTnNwQjlLX2lTbWJUdkxZZ1Q5akxzNjJoNUN2Sms1dFhvRXRROWNxc1NROW5OWUwxX3BvYWFQeDNKbWFPYWZ4MFlLNmJJbExlNW53b1ZiNlJZMm52VmVRMjBsM29vQjJ2UXdiRDhyWm1yck9GbUVDS1I3dWNKSENiMDdMaEEyX2JodW0zMEdpZzU0dGhoX3paNzBuSU5lQW9DaTdBblh2b2xjMmUyTDVDZlVmYk9qdURFOUx2UUEwSEIzWC05cU9vVkc4andHM3Q1c1B4REtJVF94LTgw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 17 May 2026 13:15:00 GMT
- [邊緣 AI 散熱需求，如何開拓醫療與教育新商機？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMic0FVX3lxTE1FSTZQR2Q5TDJiYzdHNVhRLVpYcEV6eU5STWdSSlQzT190bERIaHVVNlR6OE1RMlM4NzRPckw0NnkyMjFqcnJkQkRKelNGOWhnWjlpcTJiR0VBUVEza0ZXVUY4bllYNVZua2ExdlJBaExDV28?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 18 May 2026 15:59:16 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：SanDisk Soars 411% This Year Yet Wall Street Forecasts 9x PE. Why Are Memory Stocks Getting Cheaper as They Rise? When Will the Memory Cycle Peak? - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 681.54 | 724.66 | -5.95% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | -7.89% | -13.86% | 1,333.01 | 1,562.34 | -14.68% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「memory」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。

### 主要來源

- [SanDisk Soars 411% This Year Yet Wall Street Forecasts 9x PE. Why Are Memory Stocks Getting Cheaper as They Rise? When Will the Memory Cycle Peak? - TradingKey](https://news.google.com/rss/articles/CBMisgFBVV95cUxObzJfc3d4cmhVcWFHbmc4Q3ZCQkJ3RkpWZ2ZJUXlOeDRRb09HNVpTX1Vwbks5d1poQ3VwV09ORlRGVmZGQTNYQWZ5LW9Vc1FtZEVZSkxLRmhkQkRrdlNHMUZGNm96eDNid0FhRjVfc0FqbF9aYnhYNHUyVVFaREtqbk9YajVBbGRyc01ndzVzMm9UZDVFMFBtdXItU2l1TTYxd3N0eGpPZEY2U3BIVmdQNUNn?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 17 May 2026 09:32:10 GMT

## 先進封裝與 CoPoS

摘要：先進封裝與 CoPoS 相關新聞集中在：晶片尺寸逼近極限，玻璃基板如何助攻 AI 效能？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | 30.12 | N/A TWD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | 47.35 | N/A TWD / N/A | N/A |

關聯理由（前 3）：
- 2330：產業/供應鏈推估：公司標籤符合「先進封裝與 CoPoS」關鍵字 advanced packaging, CoWoS, CoPoS, FOPLP；其中 0 篇新聞出現相關標籤。
- 3711：產業/供應鏈推估：公司標籤符合「先進封裝與 CoPoS」關鍵字 advanced packaging, CoPoS, FOPLP, panel-level packaging；其中 0 篇新聞出現相關標籤。

### 主要來源

- [晶片尺寸逼近極限，玻璃基板如何助攻 AI 效能？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMipgFBVV95cUxOalE0dFh6RVdMSVlBVFJmLVdXLTJGU0p4ZENwaG9reFdMUFBENTRoc0NqeWtwN1ByTk5kRG03WFBfSFVFUy1jQTVIc0VMMU1TTGJES2dJS1hoeGN3VndqVzRRN2ZWd29hMmYzX0VfbTJtMHVMVzdLMjZOaE9PTnkyMnRBLTdyVGV2UjZEMndPS0NlWE9vNEtPMU1QRDFRQzROZ2tTZzRn?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 18 May 2026 15:55:21 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：5 Best AI Memory Stocks to Buy for 2026 | Investing - U.S. News Money；Micron (MU) vs Sandisk (SNDK): Pure-Play Memory Stocks Compared for 2026 - Gotrade；Micron or SanDisk: Billionaire Israel Englander Picks One AI Memory Stock Over the Other - TipRanks

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.76 | N/A | N/A | 681.54 | 724.66 | -5.95% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.38 | -7.89% | -13.86% | 1,333.01 | 1,562.34 | -14.68% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +27.48% | +16.32% | 222.32 | 225.32 | -1.33% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「memory、MU、Micron」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK、SanDisk」，共 4 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [5 Best AI Memory Stocks to Buy for 2026 | Investing - U.S. News Money](https://news.google.com/rss/articles/CBMiiwFBVV95cUxNME40RlVTSDItbE4xNjd5bkNfMGg4Ri0tQ3RlejZWNE9hcTBxQUp4QUJXTDMxVnl3ZEhmTlRmVVJ0RFR0MW5PYnk2ejZZcDFMV29FaHlOQ2dya0luS2RmSFZjczBIWXl3TE53MnlBWHpMNS15M21MUk5UZk1mVWh4WjBvMUMzZ3Fua1pF?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 18 May 2026 19:47:59 GMT
- [Micron (MU) vs Sandisk (SNDK): Pure-Play Memory Stocks Compared for 2026 - Gotrade](https://news.google.com/rss/articles/CBMifEFVX3lxTE5DYkJUcnRPQTBXeklZd09Nc19LSVZvUVItVURhZGJTMldaNEpua2hBSDV6SFI5bDI3ZjQzc3VObl9xc1JWS3BZLWU4MXdDdkd2QWllelJQR2ppOXJCT1ZQLXp0REZRQ0RtMnQ2NHVMNEZuMHY0c28wc25aQ2E?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 18 May 2026 11:50:28 GMT
- [Micron or SanDisk: Billionaire Israel Englander Picks One AI Memory Stock Over the Other - TipRanks](https://news.google.com/rss/articles/CBMisgFBVV95cUxPZnRQM3lQNWx5M2JxdE92TUpSdUhDOGpGYW40N1FRdkVUNlZ5VUk5RGJsa25vakZFUW1GLUtwWFphX2hSallEbWZ2anUxam5zcTZJSGlpdktoc2dwRjBHT3VfbkY5bkp0bjlGZVBScF9GT0l5TkJ2X1JCOWd2SzVsREF0a0tRSVluQnA2NDduUTFCZ1RBTDlPWVJQN2JXaXVIa25ONWRGTjFyOXhFZ0NsYnhB?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 18 May 2026 22:34:53 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股巨震 三大內資護盤 法人預期短線有望反彈 - 經濟日報；台股修正回檔 法人搶買哪些族群？這些受青睞 | 市場焦點 | 證券 - 經濟日報；外資賣超台股452億元連2賣　減碼台指期淨空單 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股巨震 三大內資護盤 法人預期短線有望反彈 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBiZ3RoTWl2cDNFQzFSSUtsakxaYVM4UlphdE9FdV9vMnc4d0U5T2R1QzFxMDNOcDhESVR6UmpoMFR2RW9mYzVJLWNFRDJBbElaclV3aTl5Nl94Z9IBX0FVX3lxTE5Md1dDRERicWt1bDJTazA2OHVBTWREOGtlX0xUdFprLVpRSzJEM0tkeTR4UEJzNXhMYU1uVm80T0lSOFhUSkpka2l4LWg5OHlMX2VTSEpOZGhvaXM3b0dj?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 18 May 2026 17:51:20 GMT
- [台股修正回檔 法人搶買哪些族群？這些受青睞 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFB2cGpXZklYSEdMVjNQTmk5d2VBLThwYVJGdi10Z3BlUXNqRGI3RVMydU1rdDdCRUpycjh6RXp4TDlGcUtiZnhnUDZNS1E2YTBMUU5fT1dlVVFvQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 17 May 2026 09:00:00 GMT
- [外資賣超台股452億元連2賣　減碼台指期淨空單 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5KQXo1UHdkNEhLZDJ1cjlKd08xdWJBOWt2TmFHQUUtbGdmTU1uUWVNcTdETm52ejFTcjZHY2h1Y3VLNmRXOEE3NkRVTzlUN1hQYzhCbTRHcjFid9IBX0FVX3lxTE00WThqOVAyYm1vcXFUTU9hYXYzVWtkOTNjNkRSd1lkTUtVaEo1dUd5bDg0NFNZQ3BUMW4tcmxnTGctc0RyemFETXc0dWRORnRBc093UllQTXBqa01KZ2Nr?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 18 May 2026 09:54:20 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》回測月線、收跌280點；下影線逾700點-新聞內容-基金 - MoneyDJ；台股焦點：單井(3490.TW) - 台股 - 新聞 - MoneyDJ；台股焦點：技嘉(2376.TW) - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》回測月線、收跌280點；下影線逾700點-新聞內容-基金 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxNZFhNd3N6MmtNSDlKV3Nhb2EwUEUzTlJpN1ZkOXg1SERQY1NHU1l5Xy1HNVJmNzZmN2tKTWJZZDJ4dkxVUUc2cUZNYXRWOVJMa3Ywa0tVcjcweG01dTVucGZqMHpsblhXck5CX0dNREgzRXJNMUgyaFBsQ0hSZmpoX2tDXzZqalhmelkzMGtyOHE?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 18 May 2026 07:48:00 GMT
- [台股焦點：單井(3490.TW) - 台股 - 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMiggFBVV95cUxNODRpWURlNmRNYmV6c2hfLVdWeGxoeU9Zby14VHBZX0k2UU9UcWlGVGxLcGNXM0hSTURuSjhpTEMxRGJ4XzZMRHd6WDg2Z3VTSlRnc2duZG1PemhmMmxYVGljc3RLWWlRM2lDTTNRYlBJdnN5bmowazlWX0k1R1lHSTdR?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 18 May 2026 01:14:00 GMT
- [台股焦點：技嘉(2376.TW) - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNcGZKTzV2U1k4QlBRc1ZlUHVzeDU5d0RoV3hYSUVZLUZocV9LdjRpM3Y2aWEyaHd5dWQ5dmRKbXV6NXZYdzJwQ1RGd3h5REd0N2JvOGhpSE1GUnIyR1RjbzY4SjBQUm1ydkFGVmJ2MHN5aXBEWFZyRno2V1czY3p6clVybmpQTXVtN29YbmNpajNYdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 18 May 2026 01:18:00 GMT

## 資料缺口與需人工確認

- FinMind 月營收抓取失敗：2303，原因：HTTP Error 402: Payment Required
- FinMind 月營收抓取失敗：2330，原因：HTTP Error 402: Payment Required
- FinMind 月營收抓取失敗：2454，原因：HTTP Error 402: Payment Required
- FinMind 月營收抓取失敗：3017，原因：HTTP Error 402: Payment Required
- FinMind 月營收抓取失敗：3711，原因：HTTP Error 402: Payment Required
- FinMind 綜合損益表抓取失敗：2303，原因：HTTP Error 402: Payment Required
- FinMind 綜合損益表抓取失敗：2330，原因：HTTP Error 402: Payment Required
- FinMind 綜合損益表抓取失敗：2454，原因：HTTP Error 402: Payment Required
- FinMind 綜合損益表抓取失敗：3017，原因：HTTP Error 402: Payment Required
- FinMind 綜合損益表抓取失敗：3711，原因：HTTP Error 402: Payment Required
- FinMind 股價抓取失敗：2303，原因：HTTP Error 402: Payment Required
- FinMind 股價抓取失敗：2330，原因：HTTP Error 402: Payment Required
- FinMind 股價抓取失敗：2454，原因：HTTP Error 402: Payment Required
- FinMind 股價抓取失敗：3017，原因：HTTP Error 402: Payment Required
- FinMind 股價抓取失敗：3711，原因：HTTP Error 402: Payment Required
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
