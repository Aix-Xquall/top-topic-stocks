# 每日股市熱門話題分析 - 2026-07-08

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜負向｜熱度 8｜市場確認 100.00｜同向 1/1
2. **AI 伺服器與資料中心**｜負向｜熱度 11｜市場確認 80.05｜同向 5/6
3. **半導體與晶片供應鏈**｜負向｜熱度 11｜市場確認 66.13｜同向 4/5
4. **新興題材：TradingKey**｜負向｜熱度 2｜市場確認 N/A｜同向 0/0
5. **利率與成長股估值**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.05（樣本 14）
- 5日相關係數：-0.05（樣本 14）
- 同向比例：10/14

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 100.00 | 1/1 | 0 | +20.40% | +21.10% |
| AI 伺服器與資料中心 | 80.05 | 5/6 | 0 | +7.24% | -0.23% |
| 半導體與晶片供應鏈 | 66.13 | 4/5 | 1 | +3.38% | -4.22% |
| 新興題材：TradingKey | N/A | 0/0 | 0 | N/A | N/A |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | 0.00 | 0/2 | 2 | -5.79% | -0.86% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 相關性偏弱；應提高同向價格確認權重，降低泛 AI、泛半導體等寬標籤推估權重。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-06-25 | 0.10 | -0.21 | +20.00% | 5 |
| 2026-06-26 | 0.08 | 0.04 | +25.00% | 16 |
| 2026-06-27 | 0.12 | 0.29 | +57.89% | 19 |
| 2026-06-28 | 0.16 | 0.55 | +85.71% | 14 |
| 2026-06-29 | 0.49 | -0.25 | +38.46% | 13 |
| 2026-06-30 | 0.44 | -0.27 | +62.50% | 8 |
| 2026-07-01 | -0.08 | 0.25 | +30.77% | 13 |
| 2026-07-02 | 0.30 | 0.03 | +55.56% | 9 |
| 2026-07-03 | 0.21 | 0.08 | +55.56% | 18 |
| 2026-07-04 | -0.22 | -0.36 | +22.22% | 18 |
| 2026-07-05 | -0.00 | 0.24 | +40.00% | 10 |
| 2026-07-06 | N/A | N/A | 0.00% | 2 |
| 2026-07-07 | N/A | N/A | 0.00% | 1 |
| 2026-07-08 | -0.05 | -0.05 | +71.43% | 14 |

## 歷史回測摘要

- 回測日期：2026-07-08
- 近5日 3日相關：0.14
- 近5日 5日相關：-0.05
- 同向比例：0.00%
- 權重狀態：未調整

- 方向準確度：0.00%
- 信心排序準確度：0.14
- 診斷：弱正相關

調整原因：近 5 日有效樣本 8 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：AI memory, chip stocks fall despite Samsung's Q2 profit surge as worries around AI boom loom - Seeking Alpha；Philadelphia Semiconductor Index Falls Over 6% as Chip and Memory Stock Selloff Intensifies. Micron Drops Below $900, While Samsung’s Mixed Earnings Spread Panic. - TradingKey；The AI Trade Is Off to a Hot Start This Week as Chip, Memory Stocks Surge - Investopedia

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | -0.62 | N/A | N/A | 938.38 | 975.56 | -3.81% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.62 | -20.40% | -21.10% | 1,617.70 | 2,335.00 | -30.72% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -6.73% | +12.92% | 196.93 | 211.14 | -6.73% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「memory、Micron」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：fall, falls, surge。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 2 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：fall, falls, surge。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AI memory, chip stocks fall despite Samsung's Q2 profit surge as worries around AI boom loom - Seeking Alpha](https://news.google.com/rss/articles/CBMixwFBVV95cUxNRTl5bEIyMmNmMEwzZU9BSnlPellVU0xoMDhiRkdEWS1hMDNZRll0VlJ4SzdzdGFRWkpqem5weXhaNTE1aWplVXltdzJsZUZRTjVHdV9xY1U3U0U5bEFPUFFmSkR5czVmRDVjX01NOHBPTWRubzY0UmlMRjM5NUcwVFd6SjhBdWxaSENMUE9GcG1BOXFlbFZabkNSdjNVOThrUnpUNWNvYjhrTXFFZlZGaEpNSlJ4MzJoRndQUHdjU3NGZmY5ZGk0?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 07 Jul 2026 18:00:00 GMT
- [Philadelphia Semiconductor Index Falls Over 6% as Chip and Memory Stock Selloff Intensifies. Micron Drops Below $900, While Samsung’s Mixed Earnings Spread Panic. - TradingKey](https://news.google.com/rss/articles/CBMizgFBVV95cUxOR25WakszRFRZNWprT0dfS2FYbDlFYzVVQnlpVmxpXzV2d0RCWkl4czgwQm1QeEhMM2lrSE4yX21BX3lreVRqd1p5X1VtZVRjWE0xN09TazBvNkwxaGduc21FV0lUMnZKU1lPdHVsaVc5YzItNFJxZTF6cjVWX09xRGUzMnJSUEVXNnJiUnJ6MGRPUkNzSGs0UU8xclV0UTdaT0U4Y3ljRmRRaW9HVUNaOGNBQ3pqWU44RVJPQ1cydHpVRERpeFFxM0ZEUnBJdw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 07 Jul 2026 18:42:02 GMT
- [The AI Trade Is Off to a Hot Start This Week as Chip, Memory Stocks Surge - Investopedia](https://news.google.com/rss/articles/CBMivgFBVV95cUxNeFJRSWNtNWJMT1NiMlA5R2tEc0VZUXpxdW1IdGdKVmdKOUZSOFI2X0N6RVRpNjJQRTFFQ3RwYkNUd0ZmYWQydTJOTkMzSzYxS0l3bWVwM0RjbERuR3o4X1A5Zmo3cFFub1BndF9BZklLekljSmw5OURoaXFHQ2pkNDJ2RFd2bUpjdW1nT0RVWWVQSUZ5dzg5SEdnbWQyUkdsSDM0QVY1elZBWjBmY3NPcDNRaURoa24zenRqOF93?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 06 Jul 2026 17:23:03 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：五檔台股 ETF 犀利市場聚焦 投資半導體及 AI 績效最佳 | 基金天地 | 理財 - 經濟日報；五檔台股 ETF 犀利市場聚焦 投資半導體及 AI 績效最佳 | 基金天地 | 理財 - 經濟日報；Intel Stock Tumbles as Samsung's Record Profit Sparks Fresh AI Fears - TradingView

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.59 | N/A | N/A | 110.39 | 120.35 | -8.28% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | -0.06 | -6.73% | +12.92% | 196.93 | 211.14 | -6.73% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | -0.06 | N/A | N/A | 516.11 | 517.82 | -0.33% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.06 | -1.01% | +1.24% | 2,440.00 | 2,445.00 | -0.20% | 同向 | 74.39 | 32.80 | 416.98B TWD / 30.09% | 2026-06-01 |
| MSFT 微軟 | 產業/供應鏈推估 | -0.03 | -0.99% | -23.26% | 388.84 | 506.69 | -23.26% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -17.01% | +19.80% | 370.78 | 446.77 | -17.01% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.04 | -10.45% | -4.26% | 651.00 | 682.00 | -4.55% | 同向 | 10.86 | 60.45 | 63.03B TWD / 28.57% | 2026-06-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.04 | -7.25% | -5.06% | 4,030.00 | 4,310.00 | -6.50% | 同向 | 62.91 | 64.22 | 47.43B TWD / 4.99% | 2026-06-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [五檔台股 ETF 犀利市場聚焦 投資半導體及 AI 績效最佳 | 基金天地 | 理財 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFA5MnNsZzl2RmZuMHJyanZWbTVVTzN3SS1UWTU3QklwcXhxMzFwZ2RrRGZLb2d4bU92dkNMWG91Vk00UGJIc0dEd2xVcV83eVFoVmYtU1R0MU5mdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 07 Jul 2026 16:19:36 GMT
- [五檔台股 ETF 犀利市場聚焦 投資半導體及 AI 績效最佳 | 基金天地 | 理財 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxOZ2xHYjFyU3l3cERzVlNyRDVkNmVsZnBYVnYySGxsR3UxcU9Cb3E1anhFaXdVZFUyMGxEcGJGZmR0MUhnS2I5SnBmazZ3OUtUSWwtN3dJaUNLNF92T19MeG9MdWlETldkc2QwUndyM09RYmJVSXZ0TnJfaWI5aVE4cQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 07 Jul 2026 16:19:36 GMT
- [Intel Stock Tumbles as Samsung's Record Profit Sparks Fresh AI Fears - TradingView](https://news.google.com/rss/articles/CBMixwFBVV95cUxNRTI0RllDc2pnaEM0MW13M092SndlM3ItcjRzSHZEamE0Z0ZTcmFnc0dpTml1MXlRLWJHQzJZa2R1c1U2SEJOa3FCSDJWeWt2b0w3RE1WeTcyZmR4Ri05dG5hNHltZWU4c3ZHelRaWkxRMFA0djJpek9aY1dJbmxPNG9KZTVDVFJLb0Y4S1otZzVQaF9KUWhqX2ZKOHRBZ0pPbjRlUDYzUlIyRGFfSkExNnRTMEY3ZXRwVkNoV0RRbHNSVEhoR0JZ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 07 Jul 2026 15:54:21 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：五檔台股 ETF 犀利市場聚焦 投資半導體及 AI 績效最佳 | 基金天地 | 理財 - 經濟日報；五檔台股 ETF 犀利市場聚焦 投資半導體及 AI 績效最佳 | 基金天地 | 理財 - 經濟日報；Intel and Applied Materials Dive 10%, AMD Craters 8% as Samsung Earnings Trigger Chip Selloff - Yahoo Finance

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.62 | N/A | N/A | 110.39 | 120.35 | -8.28% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.53 | N/A | N/A | 516.11 | 517.82 | -0.33% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 新聞直接提及 | -0.23 | +17.59% | +33.82% | 310.66 | 312.06 | -0.45% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.05 | -1.01% | +1.24% | 2,440.00 | 2,445.00 | -0.20% | 同向 | 74.39 | 32.80 | 416.98B TWD / 30.09% | 2026-06-01 |
| 2303 聯電 | 產業/供應鏈推估 | -0.05 | -6.34% | -5.78% | 155.00 | 170.50 | -9.09% | 同向 | 4.00 | 38.94 | 23.12B TWD / 22.85% | 2026-07-01 |
| NVDA 輝達 | 產業/供應鏈推估 | -0.04 | -6.73% | +12.92% | 196.93 | 211.14 | -6.73% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | -0.04 | N/A | N/A | 938.38 | 975.56 | -3.81% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | -0.04 | -20.40% | -21.10% | 1,617.70 | 2,335.00 | -30.72% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AAPL：新聞直接提及「Apple」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [五檔台股 ETF 犀利市場聚焦 投資半導體及 AI 績效最佳 | 基金天地 | 理財 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFA5MnNsZzl2RmZuMHJyanZWbTVVTzN3SS1UWTU3QklwcXhxMzFwZ2RrRGZLb2d4bU92dkNMWG91Vk00UGJIc0dEd2xVcV83eVFoVmYtU1R0MU5mdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 07 Jul 2026 16:19:36 GMT
- [五檔台股 ETF 犀利市場聚焦 投資半導體及 AI 績效最佳 | 基金天地 | 理財 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxOZ2xHYjFyU3l3cERzVlNyRDVkNmVsZnBYVnYySGxsR3UxcU9Cb3E1anhFaXdVZFUyMGxEcGJGZmR0MUhnS2I5SnBmazZ3OUtUSWwtN3dJaUNLNF92T19MeG9MdWlETldkc2QwUndyM09RYmJVSXZ0TnJfaWI5aVE4cQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 07 Jul 2026 16:19:36 GMT
- [Intel and Applied Materials Dive 10%, AMD Craters 8% as Samsung Earnings Trigger Chip Selloff - Yahoo Finance](https://news.google.com/rss/articles/CBMinAFBVV95cUxQejl6d3BwV3J5VzZYMjY5QTJZb0s5Vk5nUWlCZkw1bkNxZnZOS3FQTlZoRUJ0a2JTOHdfTS02ZzFyekhBaU50UWdOQVFQd3h5clhhbmdiYlhlZVJ6MS1yenpxeHRqb3dVS0VRUkEtM3NhWDZsTkgyLTd4UUN6ZXlEdmM1QlFEanZ4ZGxLRU43c2ZHMGFJa3B4dUVEWE4?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 07 Jul 2026 14:27:59 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Philadelphia Semiconductor Index Falls Over 6% as Chip and Memory Stock Selloff Intensifies. Micron Drops Below $900, While Samsung’s Mixed Earnings Spread Panic. - TradingKey；Applied Materials Inc Stock (AMAT) Moved Down by 9.51% on Jul 7: Facts Behind the Movement - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | -0.45 | N/A | N/A | 938.38 | 975.56 | -3.81% | N/A | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron」，共 1 篇新聞命中。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Philadelphia Semiconductor Index Falls Over 6% as Chip and Memory Stock Selloff Intensifies. Micron Drops Below $900, While Samsung’s Mixed Earnings Spread Panic. - TradingKey](https://news.google.com/rss/articles/CBMizgFBVV95cUxOR25WakszRFRZNWprT0dfS2FYbDlFYzVVQnlpVmxpXzV2d0RCWkl4czgwQm1QeEhMM2lrSE4yX21BX3lreVRqd1p5X1VtZVRjWE0xN09TazBvNkwxaGduc21FV0lUMnZKU1lPdHVsaVc5YzItNFJxZTF6cjVWX09xRGUzMnJSUEVXNnJiUnJ6MGRPUkNzSGs0UU8xclV0UTdaT0U4Y3ljRmRRaW9HVUNaOGNBQ3pqWU44RVJPQ1cydHpVRERpeFFxM0ZEUnBJdw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 07 Jul 2026 18:42:02 GMT
- [Applied Materials Inc Stock (AMAT) Moved Down by 9.51% on Jul 7: Facts Behind the Movement - TradingKey](https://news.google.com/rss/articles/CBMiiwFBVV95cUxNSzk0b3hKSVZvcUgzQXItOF9wcTFxbDBOWkpETElVcE5EalNmejNtRlQ4T2p6VkhPWExpbmd2c0tqS3g0Vjk3TkozdlY3R2JnMllXV2dmOFZjRXRjVmVnZmVWMEJ5VW1wRW90cnlkLVU4UVBqLVV4WXd3aU4tS01QcXBxNHdjWDI2Zjdj?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 07 Jul 2026 14:15:22 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：路博邁投信：台股估值合理、未過熱，續聚焦AI - MoneyDJ；〈美股早盤〉AI估值疑慮升溫、DeepSeek傳自研晶片 主要指數漲跌互現 - news.cnyes.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | -0.99% | -23.26% | 388.84 | 506.69 | -23.26% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [路博邁投信：台股估值合理、未過熱，續聚焦AI - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxObDRNOVIySzFTRlduYzc1VEpyeDFhOVdGT19qNDVKTV9xSHlKT255SXgxSkdyYzZEUUJMREhQMkNUM1dvaTZlRTZfQzBWWW5sRml3V1RXbkc0clM4WFpoOFNWdTZwVkxvOWluUHJlaWtFOEJ5aXk2QmZKeWt0d29tUXhRaTVHYTlSa25CRnlRaWI2Zw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 07 Jul 2026 05:22:00 GMT
- [〈美股早盤〉AI估值疑慮升溫、DeepSeek傳自研晶片 主要指數漲跌互現 - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTE5OWEFRQlEtaDVaSWRXS04wTXhUbkx6bzRnbXRQY3pEalJ4WEJYbEVWeHVsUUdXNzZ4Yk5fUHZfMHBqUklqMHpUd2hqQ3l4Tzg?oc=5) - Google News source discovery | 鉅亨網 Tue, 07 Jul 2026 13:40:26 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：〈財經週報-台股熱點〉從AI到外太空 散熱族群題材不斷 - 自由時報；高通投資人日震撼登場：台廠奇鋐、廣達、台積電誰受惠？AI200／AI250／AI300 與 HBC 是什麼？｜產業熱話 - sinotrade.com.tw；AI液冷深度：108塊冷板、CDU與Rubin無風扇機櫃，誰能守住60-70億美元冷板價值池 - 鉅亨號

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.31 | -10.58% | -2.97% | 2,450.00 | 2,835.00 | -13.58% | 背離 | 61.06 | 40.26 | 17.62B TWD / 66.11% | 2026-07-01 |
| 2330 台積電 | 新聞直接提及 | +0.23 | -1.01% | +1.24% | 2,440.00 | 2,445.00 | -0.20% | 背離 | 74.39 | 32.80 | 416.98B TWD / 30.09% | 2026-06-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱、奇鋐」，共 3 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：受惠。
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 方向判斷命中詞：受惠。

### 主要來源

- [〈財經週報-台股熱點〉從AI到外太空 散熱族群題材不斷 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTE9rc0xOT3JaSGZPbV9uNjZUNmJLdkctMThER29ldnFaMXp1YlBQajNxaVBBcHlrVEFOOUNLZkxISUt1ZVFOMHF4WXBSd1Jtc0plYWh5bDRrdVk?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 07 Jul 2026 07:16:53 GMT
- [高通投資人日震撼登場：台廠奇鋐、廣達、台積電誰受惠？AI200／AI250／AI300 與 HBC 是什麼？｜產業熱話 - sinotrade.com.tw](https://news.google.com/rss/articles/CBMiiwRBVV95cUxOdUZybS1JWUptQTFaTkFqUGIxMVEtaHV3SzNPTWJ1QXVLNDI4ck9hVUVHYlNtMGZoZUVxa3lJaE1uOEViVVl6eUVIVWVJVXJUYTUtel9KQzd3NEliUmxxQ3ZhRGR0YnRRNC1WaS0yM0M5UVoxbUtSZENab05MUUNyYlZwZzVtX05ILWlGWlNuVUgteE5qOTRIQk9DRURYa09BV1lYdTBxLXZ6ZHZMX3gyRE1ieDMxZUpfNnl1X2w2TjYyQ1FHWjQ4X2taUy1qUkNuYnR6Qm5TYjlkemluaXBIVW1jQTN1VnQySzlfazY3d2xZd1F2b0RKeHBMU0NvTTFpTmxHbWJfNUh5U1lra19IRmM0VGlCOGQxTGxrNFhaZVRRRXZIeE8yS244SF9ORDFQcjJsV2Z0bXpfSmh6NUxaN0dvMjd0NnJENzBmbTY4VFQ1VVJ2Z0dsWVg2ay1yV2xBYU84Mi1lblptNGhZSjRyeExST29tWWtoZ3ZLcEdLTXZZVEQzcV9vWmVycW1OcnlNUlJVZlFNdU9wTnVEVjItVlVVc2Q4RVBCcnFMempuN2hfMGJ2YXJveFhFdG5ycF9vam5hcFp0ajc2c0xXMVFxeGRvSC1yTUxPNWlGOHlzMkVqajRWdzNQV2xwOWU5alBpdG5LWFppQWxQUUNLRGZSZGw2clM4TWZ2R2Jj?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 07 Jul 2026 12:48:15 GMT
- [AI液冷深度：108塊冷板、CDU與Rubin無風扇機櫃，誰能守住60-70億美元冷板價值池 - 鉅亨號](https://news.google.com/rss/articles/CBMiSEFVX3lxTE1EZzVmX2YtVFN6R0RkQXJTLXg1Q2l5OEQ4MkszUk9FMXUtYmp2LWdvRnlnQWNQNlBlV1AyZnYwWVI2bzlzam5keQ?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 07 Jul 2026 08:03:43 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：外資、主力大戶等瘋狂倒貨 台股失守46K 指數震盪1,535點 - 經濟日報；台股 ETF 人氣強強滾 近一周11檔人數成長 主動型、高息型最受青睞 | 基金天地 | 理財 - 經濟日報；台股「豬羊變色」！寫史上第八大收盤跌點、第五大震盪紀錄 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [外資、主力大戶等瘋狂倒貨 台股失守46K 指數震盪1,535點 - 經濟日報](https://news.google.com/rss/articles/CBMikAFBVV95cUxPbGF4dlRQanNqYllCQTRtaTN3eTR1Z2c2c01fZGZmMXFqdV9HVEpfRWxlMjNiR0o0Nm9MSlpIdjBOYWp3T3VkbVNsakFRTERoYkc5QmF0Vkh0TlJVa0EtSklaaTFEbkxjcVVBQ1FrNWhsaEJDd3F2QUFvV1RBVW90RGpCY0JVNkNXQVlpRjRkYljSAV9BVV95cUxOemJkSjdtam01aDJmRTNrZHR5YUdncFBvM0Y5TUtNM2lMaTdOczZLT2xzNU1KczEwMkp1cXU0MmhUbnhzaXZYSG1hWHJKd2hwaXpVZjhKNU05Y1IzQXRkYw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 07 Jul 2026 17:44:30 GMT
- [台股 ETF 人氣強強滾 近一周11檔人數成長 主動型、高息型最受青睞 | 基金天地 | 理財 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1KZWhTc2JNSTlPOTlHd3VyWHFxWW9RRUpFd1JEWW5VSkJHUjE4R0d1UFh0dThQYVFWd2J2OWlxd0VadTlnQVJuSHJBWFdKQ0F3anFYNkVuNnhBQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 07 Jul 2026 16:20:37 GMT
- [台股「豬羊變色」！寫史上第八大收盤跌點、第五大震盪紀錄 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1HZ0xJTVNHWkhUcW1hU1RXRGFsQUZiOFZ0VmFlRTJIcHpxVzllakxJMWNobEtIZkp4QXdJY1BxTjE5Q2tndzcxLUs0S01mOGJQcXBIZUFaM1oxUdIBX0FVX3lxTE53cm5LWEZRQnNwR1NtVlQ3b0ttLUdsSDJmOGFiSWttZlhNWmxzd3hRLTIwM2UxRXFqUzZhWnJkb0JYOTNKMXNudHhpMTByWlQ4UERxYUxUSmh0TGEtZmpN?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 06 Jul 2026 09:00:00 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》破月線挫跌1077點，三大法人賣超946億-新聞內容-基金 - MoneyDJ；個股動態報導內容-CF139535-3F3E-496C-B3EF-F02B83E3C6AA - MoneyDJ；個股動態報導內容-7116DC4F-D6B5-4564-B2C0-0AEF29F0CDFB - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》破月線挫跌1077點，三大法人賣超946億-新聞內容-基金 - MoneyDJ](https://news.google.com/rss/articles/CBMikwFBVV95cUxOdEExQW5oand4RXZTZjFhOE1iSng5bk9UOFotU2M3RGhXRnQ2X3daWU5SSjBWMXhkSXM1Qm9LMnNBUGMxTFlBN2R5STZuamh0SHFtZGMxNnM5M3hsTV9IUmRnb0FfRjJGMmpKcjNyRk1sV0Y4bGNwX0M0ZkdQVFlURmVqMEE4MmpVUFVnRm95V05udDg?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 07 Jul 2026 07:50:00 GMT
- [個股動態報導內容-CF139535-3F3E-496C-B3EF-F02B83E3C6AA - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxPbHZ1ZmRodVZMWXlEdnNWVV9OOWJrLWEwXzFHVFhqSFh2RktHbFM4UzNaeTBDNzZEeGtBaEI3Z3o4c3BIZlFpWkpUYWJQZktzSFk3bTVYU21JajA0MklEXzd2NzNzaVNnVmp6RDY1QVFrZnFXZ0IxVkxNbGNUaEQzYVBLOWJvOGY4WmFhbmoyVkdpTzZY?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 07 Jul 2026 12:00:16 GMT
- [個股動態報導內容-7116DC4F-D6B5-4564-B2C0-0AEF29F0CDFB - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxOVjU2RmxaNmVVcVQ2MS0wWmJYZzNRV0doajVzY3I3a1VFNmRmeTZJelYtNjZwMkpWaGNkVjE1Z21VTDBhTTN1QWRFcWVWSE1UdVp6MEN4Q2pYSTZEMTA1My1YNFRqZjBJZFBqb1oyXy1pNV9wVE1NOFhvZlcyRkotRDZLRVBLSTJqSkQzd0p1R1N3ck5t?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 07 Jul 2026 12:00:16 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
