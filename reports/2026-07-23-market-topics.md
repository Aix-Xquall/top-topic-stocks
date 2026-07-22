# 每日股市熱門話題分析 - 2026-07-23

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜中性｜熱度 6｜市場確認 N/A｜同向 0/0
2. **AI 伺服器與資料中心**｜正向｜熱度 12｜市場確認 42.27｜同向 3/6
3. **新興題材：OpenAI**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
4. **半導體與晶片供應鏈**｜負向｜熱度 9｜市場確認 22.82｜同向 2/5
5. **散熱與液冷供應鏈**｜負向｜熱度 2｜市場確認 0.00｜同向 0/1

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.01（樣本 12）
- 5日相關係數：0.01（樣本 12）
- 同向比例：5/12

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 42.27 | 3/6 | 1 | +2.42% | +4.03% |
| 新興題材：OpenAI | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | 22.82 | 2/5 | 2 | -1.73% | -6.18% |
| 散熱與液冷供應鏈 | 0.00 | 0/1 | 1 | -2.95% | -4.62% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：BBFD1AB41629 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 相關性偏弱；應提高同向價格確認權重，降低泛 AI、泛半導體等寬標籤推估權重。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-07-10 | 0.55 | 0.05 | +77.78% | 9 |
| 2026-07-11 | 0.13 | -0.08 | +50.00% | 12 |
| 2026-07-12 | 0.27 | 0.13 | +16.67% | 12 |
| 2026-07-13 | 0.39 | -0.09 | +15.38% | 13 |
| 2026-07-14 | 0.10 | -0.07 | +21.43% | 14 |
| 2026-07-15 | 0.20 | -0.16 | +28.57% | 7 |
| 2026-07-16 | 0.20 | 0.02 | +33.33% | 12 |
| 2026-07-17 | 0.36 | 0.02 | +60.00% | 15 |
| 2026-07-18 | 0.18 | 0.08 | +53.85% | 13 |
| 2026-07-19 | 0.37 | 0.09 | +12.50% | 16 |
| 2026-07-20 | -0.59 | 0.11 | +45.45% | 11 |
| 2026-07-21 | -0.12 | -0.03 | +12.50% | 8 |
| 2026-07-22 | -0.33 | -0.15 | +16.67% | 6 |
| 2026-07-23 | -0.01 | 0.01 | +41.67% | 12 |

## 歷史回測摘要

- 回測日期：2026-07-23
- 近5日 3日相關：0.15
- 近5日 5日相關：0.50
- 同向比例：+66.67%
- 權重狀態：未調整

- 方向準確度：+66.67%
- 信心排序準確度：0.15
- 診斷：弱正相關

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

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：The Ultimate Bull Run for NVIDIA, Micron, and SanDisk May Be Closer Than Investors Think - 24/7 Wall St.；Prediction: Micron and Sandisk Stocks Will Both Plummet After July 30 - The Motley Fool；Micron vs SanDisk: Which Memory Play Wins the AI Boom? - AOL.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 959.48 | 971.00 | -1.19% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | +18.04% | -0.97% | 1,599.27 | 2,335.00 | -31.51% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +0.44% | +21.59% | 212.06 | 212.06 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、美光」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 5 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [The Ultimate Bull Run for NVIDIA, Micron, and SanDisk May Be Closer Than Investors Think - 24/7 Wall St.](https://news.google.com/rss/articles/CBMisgFBVV95cUxQM0hqdXJpZlhJbV9GdkZydDFyZXFxUHNTMURVVG5SdDExRWttcExUblczQVQzTFZ2RHNXZFFrSzN6dnVKUkdzSnRvOEZjeFVEZHNyelprMzZsV3p4OHZ2a3pfVXktWGdPaWEwRE9Sdy1SV21mSXFUNW85ZVhrM3k5UE1CckxtQ1M3eUoxbDE0LU1MT3dPUmpfcEpwQUlXSnZ1em5XNTA1MjlSb1llSEwtNnFn?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 22 Jul 2026 21:53:48 GMT
- [Prediction: Micron and Sandisk Stocks Will Both Plummet After July 30 - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxQVExqSDR4VnhUaU9QY3pOVEdXcnFQQmFpU0dIZ1drZEVIUndETHJJMEp0RGI4MUEzNUF4Z21kUk4zMjRUbjdHTjVZSWhFOVBmY3k2Vk1fcV9GRHFvdnFla0M2eFFrYWw3OEMtTTd0NTJYOFRMLUNGcWp3eDlONFRjRjhoU09rV1FUQ2JiNVBFV0ZDQzBGcko2YQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 22 Jul 2026 11:45:00 GMT
- [Micron vs SanDisk: Which Memory Play Wins the AI Boom? - AOL.com](https://news.google.com/rss/articles/CBMifkFVX3lxTE42Ym9lRnV1VFA1VjZuOHVZQ0IxcTF4eWs4ZFVGQmlJSEZYSHBldnY3bm5haDZ4MlFyMEFzT1QtZGpFU1ZKT1FwV2t3b0JuU2NNLS04UUJmNzRwZnpXbmVXVlZHRERBZEp3MThEZzN0TUY1UHVKYWFuWTJuSDFBdw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 22 Jul 2026 10:49:49 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel Earnings Test AI-Fueled Rally - TradingView；Intel Launches Fresh Layoffs in Data Center and AI Unit Ahead of Earnings as Lip-Bu Tan Pushes Turnaround Strategy - Benzinga；Is Intel (INTC) Still Cheap Following AI Partnerships And Earnings Optimism? - Yahoo Finance

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.59 | N/A | N/A | 102.62 | 114.68 | -10.52% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.04 | +0.44% | +21.59% | 212.06 | 212.06 | 0.00% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.06 | N/A | N/A | 552.33 | 552.33 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.06 | +4.80% | -1.64% | 2,400.00 | 2,410.00 | -0.41% | 同向 | 74.39 | 32.27 | 442.68B TWD / 67.87% | 2026-07-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.03 | -0.61% | -22.96% | 390.34 | 506.69 | -22.96% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -11.18% | +28.21% | 396.81 | 446.77 | -11.18% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.04 | +6.84% | -3.95% | 656.00 | 680.00 | -3.53% | 同向 | 10.86 | 60.91 | 65.78B TWD / 32.86% | 2026-07-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.04 | +14.24% | +2.94% | 3,850.00 | 4,310.00 | -10.67% | 同向 | 62.91 | 61.35 | 58.01B TWD / 2.80% | 2026-07-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel、INTC」，共 3 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Earnings Test AI-Fueled Rally - TradingView](https://news.google.com/rss/articles/CBMimwFBVV95cUxOU2tJV1Rzd2lTSUowUWZjMV9vMHh4SC1hUDkzM3ZseGFQN1R5dElRM1owbWpMRkwxQ3kyZE02VUhhdTNtRU11c3FTSzJMUFduRFpZQ0NnV096Vnpaa21iM0FVWEstY21VZ2dsT0h1TXU0SzNXLTR6SzFDOXNLeVl2SGk5UmphQnJIdlp1ci1qNGpxNnkwaXYxVm9SWQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 22 Jul 2026 18:05:11 GMT
- [Intel Launches Fresh Layoffs in Data Center and AI Unit Ahead of Earnings as Lip-Bu Tan Pushes Turnaround Strategy - Benzinga](https://news.google.com/rss/articles/CBMimwFBVV95cUxQVUNLYWFWSUpFY3NkOVRadzZIeUFjUWhKRjZxbXFCOHJUc1p4TWw1ZnYwb1gzWmJJdG5vTU1raVBUOE1UTTgzcV8xbk9zY2M4bUdkU2hFUUV0cGlzc3F5aGpVdkZJUm5YcENZYW5raTJuREJUOWtUZHFLRVgzUDFDQ3YyV2RrTHl2Mmo5WFNNSXI3LUJsbmVLcnpzVQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 21 Jul 2026 03:33:06 GMT
- [Is Intel (INTC) Still Cheap Following AI Partnerships And Earnings Optimism? - Yahoo Finance](https://news.google.com/rss/articles/CBMingFBVV95cUxPZEdHMkZGX05CeTFEeDY5Ukludl9qbDVPUFlrbUxtSUt6X2d3cnJpZnJHR2NsUVJlRGZIX3lsZ0VScVVHX0g2aTM0Qk5hclNSQ3BfWkllYUFTalBlSEdncGNFQTRqNjE2Y21JQkkxXzZFSndCa2c0WmFkV1oyVmFCaWlWZERNdTh3NDY4dHNkOFVBczF1WllmTDQzT1JXdw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 21 Jul 2026 14:08:11 GMT

## 新興題材：OpenAI

摘要：新興題材：OpenAI 相關新聞集中在：Chinese AI's role in stopping rogue OpenAI agent shows cost of US guardrails - Reuters；OpenAI cyber models broke out of training environment to hack Hugging Face - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 新聞直接提及 | 0.00 | -0.61% | -22.96% | 390.34 | 506.69 | -22.96% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：新聞直接提及「OpenAI」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Chinese AI's role in stopping rogue OpenAI agent shows cost of US guardrails - Reuters](https://news.google.com/rss/articles/CBMivwFBVV95cUxPTXZsaW1pWGxhWHBQMmZlWWRaSGtkVUNOQnIwby1wY19YSVBTSmhCaU9ORFE1UTI1Q1hpZU43WUhyZ1Y0cXRjZklIYmlpQU5Xa19tcGxpNzNmcV9BUG1WUVNtbDhfZDhDd0RHU1hIRWt1ZWRHbTZ3S1dKa0NuZlRUQmE4UWEyRmtUMnl6NTc4Y0xraGFFUllSWGNFSTZ6WDBHYmliYzh1NVhxOUZIenE0dFdNOVZYdEhQemQxSjVxWQ?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 22 Jul 2026 18:13:26 GMT
- [OpenAI cyber models broke out of training environment to hack Hugging Face - CNBC](https://news.google.com/rss/articles/CBMigAFBVV95cUxQS0Fzbkw4bWcyTTlMV1YzMlRzZmVzTDFJUkIxUVJxWFVlZjJVcjBHQ1RSaTZXOVZRclhkRkplY1ZDWFM1UVc0WEQ5Z0daUnFhZUpCa2xTMVJOaHVrZXNJbHNZWkMzNU9TSVMwc2JtcExHam9DTGdONHJFbkJaTzhFNtIBhgFBVV95cUxPdVNpQk40cDBmZWliMlZqX1drbFJNVkEwRUE2X19rT0l1WVFjcm5uQkxBaVhXSEk0M3Rvdk5aRWR2bWFqMkJmTmsxNEg1QUIyNHlzWVpQR2dlVGtCeUxGc2EwU3NhbTM1S05vMmtNNTRoWlNsdENUdVBBS0RjV0tlLW5NV1gzZw?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 22 Jul 2026 15:54:04 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel to report Q2 earnings as chip stocks bounce off recent losses - Yahoo Finance；Chip Stocks Are Rebounding - Should Investors Buy Intel (INTC) Before Q2 Earnings? - Zacks Investment Research；Gradiant支援德國德累斯頓具有里程碑意義之半導體製造擴建專案 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.59 | N/A | N/A | 102.62 | 114.68 | -10.52% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.03 | +4.80% | -1.64% | 2,400.00 | 2,410.00 | -0.41% | 背離 | 74.39 | 32.27 | 442.68B TWD / 67.87% | 2026-07-01 |
| 2303 聯電 | 產業/供應鏈推估 | -0.05 | -3.47% | -16.27% | 139.00 | 164.50 | -15.50% | 同向 | 4.00 | 34.92 | 23.12B TWD / 22.85% | 2026-07-01 |
| NVDA 輝達 | 產業/供應鏈推估 | -0.03 | +0.44% | +21.59% | 212.06 | 212.06 | 0.00% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | -0.04 | N/A | N/A | 552.33 | 552.33 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | -0.04 | N/A | N/A | 959.48 | 971.00 | -1.19% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | -0.02 | +18.04% | -0.97% | 1,599.27 | 2,335.00 | -31.51% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -11.18% | +28.21% | 396.81 | 446.77 | -11.18% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel、INTC」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 2 篇新聞出現相關標籤。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 2 篇新聞出現相關標籤。

### 主要來源

- [Intel to report Q2 earnings as chip stocks bounce off recent losses - Yahoo Finance](https://news.google.com/rss/articles/CBMiywFBVV95cUxNM29URHJTaXNyb1cxUW9scGY1TExLdklFdTFtMWFzNHI4d0VaY29hMDhQUmIydDRVeFF5T1FDNFJ4d2RFY01DOFNodDMxTlAyQXd4NXV6aW5BOHBrTEp0T0NVTVQ4VHJSakdaOWwzRjZCQXhlbVhCRWQ2TmNHeXBGRDdqYk0zUHNVYWtWYlN1UGdGU0NPLTJMZkl0V0FiNzNtTFZNcGlpWFFGUXljbVJGNS03X24wMHpId21lRXo0RE9md3pNeXNFRnpkOA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 22 Jul 2026 12:15:38 GMT
- [Chip Stocks Are Rebounding - Should Investors Buy Intel (INTC) Before Q2 Earnings? - Zacks Investment Research](https://news.google.com/rss/articles/CBMivAFBVV95cUxOOTEySGFhUW52MnF3eEwzS2NjLXp3VGxKMHp2YmtrTkYtbVJra1NHdHNreFlJbHNlZTVrSjU4elRzSEd4YXdQV2FoRTg0U00zOWdMUzJ0cmhXRlJJX2VjVmhLYlFrWFJQUTdKMDVjcFV3MmVxV0stQUdYbENKcjF5Y0UxbGJsUEUtZGN6YWgxMXo2X0JjbUZBSjhIWTVfQ0JySEhrNGNHbjY3X2gxZFNTVG1SWW9naUk2WFZ2Qw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 21 Jul 2026 18:31:26 GMT
- [Gradiant支援德國德累斯頓具有里程碑意義之半導體製造擴建專案 - 中央社 CNA](https://news.google.com/rss/articles/CBMiVkFVX3lxTE5yVFREQS05OGJTWFoxbjFOeDloZW9OajV1T1JMbVdFNWkwSzNZaWxjVzFoV0F4Q1cxdmxWZ3hpdmhQTTZuaTFLRU1Fc2lrYURIdXhkU3pR?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 22 Jul 2026 08:37:41 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：〈財經週報-台股熱點〉從AI到外太空 散熱族群題材不斷 - 自由時報；台股創高「散熱三雄」卻殺到跌停?阮慕驊揭市場利空鬼故事： 老套路又上演 - msn.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | -0.26 | +2.95% | +4.62% | 2,265.00 | 2,835.00 | -20.11% | 背離 | 61.06 | 37.22 | 17.62B TWD / 66.11% | 2026-07-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 2 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：利空, 跌停, 創高。

### 主要來源

- [〈財經週報-台股熱點〉從AI到外太空 散熱族群題材不斷 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTE9rc0xOT3JaSGZPbV9uNjZUNmJLdkctMThER29ldnFaMXp1YlBQajNxaVBBcHlrVEFOOUNLZkxISUt1ZVFOMHF4WXBSd1Jtc0plYWh5bDRrdVk?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 21 Jul 2026 16:32:34 GMT
- [台股創高「散熱三雄」卻殺到跌停?阮慕驊揭市場利空鬼故事： 老套路又上演 - msn.com](https://news.google.com/rss/articles/CBMiywNBVV95cUxOVWQ2cl9CQWdVTEtlWWZYRlVaMXYxSWRqRy0zU3VPcVhHZmxCVWEtUGRxNnk1aGhYcGtxcmo2ZUR2RlVzaEN0ak1XU1pkNUNJcS0tR0V5QmZNZlljaUpNeUVhdE1OSUZwYWU2bjEybGNwYnU3bHoycWlLcDlKMVdxZXNwaTZuaExTVENhdGRYdVFNanpmZ2QwUWlOTGw1R04wSkludG1XbnVZa1B0aWVKd2JRTGdTUE1OMTg0NmE2eHNZY3U3V1lIWmU5UVk0dEdrZ05ma3lHWjhUUktoX2lmcFhZNDJidUZTTWZHOVlqa1VvQXctMl83dkpsS0RHREtPYmNkd3AxNl96dHFRaGJwNWVYcHVrX3E2aXdwZmRMcGJaZjNjZmhYS1hNNi1mNkZVTFJBaGRZVEsySkZ6LTFTTi1jUFEyNHRLVE4yaFYwV3NNTG9ZT25HZDhldm9fSzJpYnlra3NwX1BUSnNxQjN4b3VrMC1icXRBWl9vTG9WZDc2dW5HMG9wX2hfVVFxN2VuWEVPbDN1dW9tS09tSUh3VEx3Vk1jN1dBclc2NVNvZEEzb1FpNUJFYVZqemsyV0gxLW92dF85Uk9zNms?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 21 Jul 2026 02:19:10 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股反彈能走多遠？ 法人曝關鍵 建議要先避開這兩個類型 - 經濟日報；台股外資回頭 點火AI股 法人：指數大漲小回 朝月線45,360邁進 - 經濟日報；台股基金 穩居雙冠王 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股反彈能走多遠？ 法人曝關鍵 建議要先避開這兩個類型 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFA1NlQ1ZFhuVGMzMzgtQi1Uc0pDR3E2RF9vdmZRTUxqNEpBNE0yckpoUTZhUExEcTRHMVJEZTVwWFM4SVFjM3N0dXhMRmVUWGJUdDVFTm5LVFpmZ9IBX0FVX3lxTFA5cnZnN195ZWk0Ynp3QVBIRXhhRWpPamExbS1qMWN2UVNwUnJwUmFVbTFoSXh4dGMxc0l4VGR3SVJwMTU2ZmhsaDdJamJGQTRfWko4WFVmQk40WV9zVTNF?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 22 Jul 2026 07:24:44 GMT
- [台股外資回頭 點火AI股 法人：指數大漲小回 朝月線45,360邁進 - 經濟日報](https://news.google.com/rss/articles/CBMic0FVX3lxTE1nS1ZlaFhUT0RQYzhPLVNUV1lGblRnUGdXNUMyU0FQZDN4dmNlbC05LUhPWi1kSGRlYjlLQ0k5aWg1Wl9XbHBxc3NIbXU1cFJaR2VwZTk4Sl9zMGxObzR4UzdxVnRsTVJfMGFDZ19OWXpIU3PSAV9BVV95cUxPZ21UVG55aUZ1dGtnQlpiWHpmbXNHLUZxazlIanRoRGJWaGp6dHhaOHJuZmJ5RUtLdndvdW1fekxtRE81ckhHZkU0MjRmSi1WT0ZRQU03MWNpNHp1WmZHZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 22 Jul 2026 17:26:54 GMT
- [台股基金 穩居雙冠王 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBYWFJUby14aUJvZVM3WmVRcmZQRV81Y09rb2tkNFdYY0RhamFhaC1LSEhuNElVcWtLR3Zud3h5RjhGV0otNXBKVnUycEc1SEhGU1RpQVpvRE95Z9IBX0FVX3lxTE9Bblg2UnM1RS1aaVBOMEUtd2ZvelIzU2tva3JoY2gtNXp2djl5a0NnRnpiZWZqUTU2akstV1hNVURqRXFIU1hsQXVLSlVxMkVTeDZYRW1kTE52dGtxZThz?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 22 Jul 2026 17:07:34 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》收漲592點、日K連二紅，險守10日線- 新聞 - MoneyDJ；產業評析-台股觀風向鏈 - MoneyDJ；個股動態報導內容-C5A50B08-D4BE-4002-A550-BBFD1AB41629 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》收漲592點、日K連二紅，險守10日線- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxOZE12NWV6MlhUa1VYLTVSakFmVVd4dl9rNG1tZWU2R21SUi1CNURnVlh2TmotUDVhaERSRmZ6ZVdkd2V1T0VvT0RPSC13alhGdGFKNnRtMzFqMjAzdWNPVlktLXRZNU1MenlRS01kOFR3WE9oeXAyb28tTXBfZVQzTktxVjdmdzFVRnJuNENxZ0pCUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 22 Jul 2026 08:20:00 GMT
- [產業評析-台股觀風向鏈 - MoneyDJ](https://news.google.com/rss/articles/CBMilgFBVV95cUxNQW9xVUk0TlJBQTRKY2pobFRwM1k4QTJ0eDVpckZyM0pkNDJfd056VkFidUlvZW90VEVlWEt0TXRaMW1XQkpqRFFzNGpUSHB5ZWpicExkblcxM0hqT1E5aGIteUtMcEhXMXJWcXdBMnN5QnVMcWo0RG41WTAtOVBvajMtMVQyYVYzS2lfSkM5Y1dtQkJuVFE?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 22 Jul 2026 16:06:41 GMT
- [個股動態報導內容-C5A50B08-D4BE-4002-A550-BBFD1AB41629 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxNNXowUW9vMmF1MTZONWRYaDg0UWxlVjluSVV5VkhYZnJERkpTUFF4ZV9JZ1FYU01SMklNYkljQnVwNGlYNS03RnMtZU95dmJJRDVlNXUzVHBUWTNFVWVPMkJUOUdxY0wwS0RyU2VjS1BXVWFLclYtMG8yZ2otaVRqM1dOVzJOUTkzdXhSMzZjY1VYYjhK?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 22 Jul 2026 07:52:21 GMT

## 新興題材：BBFD1AB41629

摘要：新興題材：BBFD1AB41629 相關新聞集中在：個股動態報導內容-C5A50B08-D4BE-4002-A550-BBFD1AB41629 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-C5A50B08-D4BE-4002-A550-BBFD1AB41629 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxNNXowUW9vMmF1MTZONWRYaDg0UWxlVjluSVV5VkhYZnJERkpTUFF4ZV9JZ1FYU01SMklNYkljQnVwNGlYNS03RnMtZU95dmJJRDVlNXUzVHBUWTNFVWVPMkJUOUdxY0wwS0RyU2VjS1BXVWFLclYtMG8yZ2otaVRqM1dOVzJOUTkzdXhSMzZjY1VYYjhK?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 22 Jul 2026 07:52:21 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
