# 每日股市熱門話題分析 - 2026-08-24

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **AI 伺服器與資料中心**｜中性｜熱度 10｜市場確認 N/A｜同向 0/0
2. **記憶體與 HBM 供應鏈**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0
3. **新興題材：TradingKey**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0
4. **新興題材：NextG**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0
5. **半導體與晶片供應鏈**｜負向｜熱度 8｜市場確認 40.69｜同向 3/5

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.94（樣本 5）
- 5日相關係數：-0.77（樣本 5）
- 同向比例：3/5

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| AI 伺服器與資料中心 | N/A | 0/0 | 0 | N/A | N/A |
| 記憶體與 HBM 供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：TradingKey | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：NextG | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | 40.69 | 3/5 | 2 | -0.44% | +1.99% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：ic挖角Google晶片 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-08-10 | -0.09 | 0.74 | +71.43% | 7 |
| 2026-08-11 | 0.57 | -0.18 | +54.55% | 11 |
| 2026-08-12 | 0.52 | -0.47 | +87.50% | 8 |
| 2026-08-13 | 0.72 | 0.24 | +100.00% | 7 |
| 2026-08-14 | 0.34 | 0.57 | +92.86% | 14 |
| 2026-08-15 | 0.24 | 0.30 | +68.75% | 16 |
| 2026-08-16 | 0.37 | 0.51 | +70.00% | 10 |
| 2026-08-17 | 0.49 | 0.60 | +66.67% | 12 |
| 2026-08-18 | 0.29 | 0.36 | +80.00% | 10 |
| 2026-08-19 | -0.23 | -0.33 | +30.00% | 10 |
| 2026-08-20 | -0.72 | 0.06 | +50.00% | 8 |
| 2026-08-21 | -0.48 | -0.45 | +61.54% | 13 |
| 2026-08-22 | N/A | N/A | +50.00% | 2 |
| 2026-08-24 | -0.94 | -0.77 | +60.00% | 5 |

## 歷史回測摘要

- 回測日期：2026-08-24
- 近5日 3日相關：N/A
- 近5日 5日相關：N/A
- 同向比例：N/A
- 權重狀態：未調整

- 方向準確度：N/A
- 信心排序準確度：N/A
- 診斷：樣本不足

調整原因：近 5 日有效樣本 0 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：AI 伺服器與資料中心 相關新聞集中在：This Stock Could Be a Major AI Winner Through 2027. What’s It Worth? - AOL.ca；千億美元信用擔保，如何改變 AI 融資模式？ - TechNews 科技新報；學生負責下令，AI 負責讀大學：AI 代理「幫上課」成高等教育危機 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 90.07 | 114.68 | -21.46% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +7.31% | +7.59% | 214.72 | 214.72 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 473.25 | 516.10 | -8.30% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +1.26% | +0.63% | 2,410.00 | 2,425.00 | -0.62% | 不適用 | 86.28 | 27.94 | 467.58B TWD / 44.69% | 2026-08-01 |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +23.04% | -4.63% | 483.24 | 506.69 | -4.63% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -2.46% | -11.73% | 368.45 | 446.77 | -17.53% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | -2.00% | -4.71% | 587.00 | 680.00 | -13.68% | 不適用 | 13.92 | 42.47 | 73.78B TWD / 43.15% | 2026-08-01 |
| 2454 聯發科 | 產業/供應鏈推估 | 0.00 | -2.45% | -9.98% | 3,790.00 | 4,310.00 | -12.06% | 不適用 | 60.69 | 62.59 | 48.47B TWD / 12.16% | 2026-08-01 |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [This Stock Could Be a Major AI Winner Through 2027. What’s It Worth? - AOL.ca](https://news.google.com/rss/articles/CBMiekFVX3lxTE5qV3pOb2xBTXJFMVpaWmFQZE9kRFhWd0tWS3M1M3JaSExhakYyeUttSUt2YTJRczR1ZEhqWGdFZU4wTkJONWZLd1djcGs0S1VsQ2dKLWo2MjlDNDhVV1lyYkRFR1M1QS1mUms3SEFZSklHVkdRcXlNb1pB?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 22 Aug 2026 00:08:10 GMT
- [千億美元信用擔保，如何改變 AI 融資模式？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiakFVX3lxTE1oZ2xmMGt2U3JNOEZ6YVdQVjQ4TjE5YzhjZUg2UnFFeWpYeEJUVlZUM1hORVVaSlpQT1B0QnBLMFhwdGlyN1R4U3cyUEJTQ05jb1diLU5WUlNDMWVCLVRwd28xTjFtelhtUFE?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 23 Aug 2026 16:50:11 GMT
- [學生負責下令，AI 負責讀大學：AI 代理「幫上課」成高等教育危機 - TechNews 科技新報](https://news.google.com/rss/articles/CBMimwFBVV95cUxONVhEUGpwLTIyRzh6Y1IxeWs5YUg1RU1teWFDZGFfUzl3T2ZYT1FUNmNRTlRCNE5hbWhqUVc5QWh2bFpDZmhUczZFeFJwRE4yTTFTQlVGZ3RaaWc2NzZZSjhsdi03cWFCLTkwbC1rZnJ3dmZvZWc5eGJJLTk3cEdUY2lRWmJVQWdUWVcxeGM5Q0g2T1o2QWpia0xoZw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 22 Aug 2026 23:36:49 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：AI Money Moves Put These Five Stocks In Spotlight Last Week: NVDA, INTC, ORCL, AMD, SNDK - Stocktwits；Micron vs. Sandisk: Which AI Memory Stock Should You Own? - The Motley Fool；These AI Stocks Could Crash But The Opportunity Is Huge (Micron Sandisk AMD Nvidia SK Hynix SMH ETF) Restaurant (4r1PXOJbkl) - Mshale

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| SNDK SanDisk | 新聞直接提及 | 0.00 | -1.83% | -2.74% | 1,596.08 | 2,335.00 | -31.65% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 966.78 | 971.00 | -0.43% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +7.31% | +7.59% | 214.72 | 214.72 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | N/A | N/A | 473.25 | 516.10 | -8.30% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 90.07 | 114.68 | -21.46% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- SNDK：新聞直接提及「SNDK、SanDisk」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- MU：新聞直接提及「Micron」，共 2 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVDA、NVIDIA」，共 2 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AI Money Moves Put These Five Stocks In Spotlight Last Week: NVDA, INTC, ORCL, AMD, SNDK - Stocktwits](https://news.google.com/rss/articles/CBMi4AFBVV95cUxNd2pVcHZnd2ZRY2JnQldxNE5YdUNFSzNEUGdoVzI3S0ZhcWZ5UVp1elNzV3ZvTnMyb1BNbmRrU1FlejdPcldpRngtbS1LSWx5b3VITWlfZU83eGdsbGNLWlRZaV9rR29KbjFQRE1ENFRnS1Z0Rm5GT1pBTzZ1VjJyckhVejNRZHNaSWU3NTI4eGFpbWw4RDdhaktXU1JMNmc3VUt0enBwSmotRGEwU00wcUpLVUhVaTNkcmZFUjBtLXdiR0IwSTNVdUw5MXpJS2xWeEJZYmZ5SU1uYVE0R3pzQg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 23 Aug 2026 09:35:12 GMT
- [Micron vs. Sandisk: Which AI Memory Stock Should You Own? - The Motley Fool](https://news.google.com/rss/articles/CBMijwFBVV95cUxOelBsaHdNZlp3QzE2VHpVVmhTUWlrSDJWY244ckdsbkZXR21GaTJGcXFydE1nSm9HRGRSTUVoeGp4cThkUWl4NEthWF9IZ0tWbnNVS0JpTU4zc29sOUJFSWxaZ1BUOGtId2k1eEdfRlM1aW9aandKckNiZTVPX3NtaGFvbmdiTUFiVloxdTJoYw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 23 Aug 2026 09:55:00 GMT
- [These AI Stocks Could Crash But The Opportunity Is Huge (Micron Sandisk AMD Nvidia SK Hynix SMH ETF) Restaurant (4r1PXOJbkl) - Mshale](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBjRy11bHV3MlZQb25NMFU2MkcxN01BLTlyRlFLQ0FxUnkwZy1BRFlVZFdTUUF2aGRkeHpUMVZ6RGg4MDl5MklKLUhYTUJTVC1ZQkhSSndlVWU4ZkU?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 22 Aug 2026 06:29:13 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Intel Price Forecast: Nvidia Picked Xeon 6, Invested $5B, Yet Analysts Still Trail INTC - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +7.31% | +7.59% | 214.72 | 214.72 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 90.07 | 114.68 | -21.46% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Price Forecast: Nvidia Picked Xeon 6, Invested $5B, Yet Analysts Still Trail INTC - TradingKey](https://news.google.com/rss/articles/CBMi6AFBVV95cUxPUTJ0M002eEJBWW5ocUl6ai1nTkJ1WjFMMktJRWtzekFRcktQd1d1MTFOd1RwbVFQWk9hU25UUC16RzBnbXBXdWZwcE5pS2ROeVN1YXhFZlNjVVctMWg4SWI1Y2FJazZTOTg2OVd0OWpmMGFKczk0ejdZX090Mkg2TU1Tc2Z4b2EwaUJ5MkxITm1NLWxic2JFdDVJRGZjdTBwbVNETDFURk1jMHBQN0ZQV3BhYVcyT2JDYWR2S1hLMERJNWc1bmVwODBxcUN1YUdxMlNQemdJbktvdzQxV0pmZXVIX1Zfam5N?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 23 Aug 2026 01:54:19 GMT

## 新興題材：NextG

摘要：新興題材：NextG 相關新聞集中在：Intel (INTC) Pushes Into NextG Testing With Large Scale Open Source 5G Trials - simplywall.st

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 90.07 | 114.68 | -21.46% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel (INTC) Pushes Into NextG Testing With Large Scale Open Source 5G Trials - simplywall.st](https://news.google.com/rss/articles/CBMiygFBVV95cUxOako1M2NOc3VhUXVETG4tUG45X1phZFVsbVlOS1YySWgtZWVYVTMtUl9KU2ZVN0VxWUxJYXY5WG16bGp3Qlh6ZU9Qa3RZVG95N05Hd3ZYV2JsTG8zdnRVSmtqT1A4MU9TcTB1WlhFd1J3TklsaUxOdkRjb1IzUDVzaUcxa3U2cnAtQTFGUVk2bjhmZ1V2QzRoNEdlRDJUWkF5S3RMbmh4Z0dCdy1vWFZuaUFwLVdPb2JSd0UzODVRcUtCLTZ1MDJHMnpn0gHPAUFVX3lxTFBiWUhIY3NQMmt1RGVYUXV6U0xYX0U1RjZfVDBfMUhFMnE4TTVaMzAyNWc3d2RmLUZ3TDREWV9vR01QRTFNSGl2MWRaQmlWaExoSWZyZVB1V2VjaUVnSDVmUGQ1TEx2cE9keDl6ZXVNRTRtUUM1TlV4S0hoeS1lYXBpd2s4ZzNuY0tfLS1rMDR0VjFjU19mU2k1M1dWVlByMnN1bWRhUWNPelFLNmEzTDRISGRsQm53anI4aVFQZC02ZGNNSjVzb1hHdmRiS1NjQQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 22 Aug 2026 00:44:19 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel and AMD Fall 4%, NVIDIA Unchanged as Chip Selloff Defies Bond Yield Relief - AOL.com；國際半導體展9/2登場逾1300家參展、AI產業鏈齊聚| 產經 - cna.com.tw；韓國效法台灣打造半導體聚落專家：短期不具隱憂| 產經 - cna.com.tw

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.51 | N/A | N/A | 90.07 | 114.68 | -21.46% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | -0.23 | +7.31% | +7.59% | 214.72 | 214.72 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.46 | N/A | N/A | 473.25 | 516.10 | -8.30% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.03 | +1.26% | +0.63% | 2,410.00 | 2,425.00 | -0.62% | 背離 | 86.28 | 27.94 | 467.58B TWD / 44.69% | 2026-08-01 |
| 2303 聯電 | 產業/供應鏈推估 | -0.05 | -2.10% | -3.72% | 116.50 | 164.50 | -29.18% | 同向 | 6.68 | 17.52 | 23.84B TWD / 18.98% | 2026-08-01 |
| MU 美光 | 產業/供應鏈推估 | -0.04 | N/A | N/A | 966.78 | 971.00 | -0.43% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | -0.04 | -1.83% | -2.74% | 1,596.08 | 2,335.00 | -31.65% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -2.46% | -11.73% | 368.45 | 446.77 | -17.53% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel and AMD Fall 4%, NVIDIA Unchanged as Chip Selloff Defies Bond Yield Relief - AOL.com](https://news.google.com/rss/articles/CBMidkFVX3lxTE5WTENHR3kwSGFJTU5nRVFNeXZTcmFFVzhlU2EyYUgyNVZuaUgtVzAzNkhfZ1VsTzFwbFhYX3VQcklhU19jU1FMcndjeHdGN1FNcWQtaUcwVTRsSUltNk9vYjRiRWVpd3lkd05pdXk3X3d1blRBWVE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 22 Aug 2026 23:42:25 GMT
- [國際半導體展9/2登場逾1300家參展、AI產業鏈齊聚| 產經 - cna.com.tw](https://news.google.com/rss/articles/CBMiXkFVX3lxTE9vendlOFUzM2hlaU83NHBWeHBCeTlNNEFLWlV0dUlHeF9HdUdHNlhnTDRRTmpPU1FhaXVRTElQRG9mOVZYTWxFZG1mYWNJN3VhN1I5ckVsNnZiLVg0Q2c?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 23 Aug 2026 04:16:00 GMT
- [韓國效法台灣打造半導體聚落專家：短期不具隱憂| 產經 - cna.com.tw](https://news.google.com/rss/articles/CBMiXkFVX3lxTE02eUtTTU1uYUN5WXlPdHBiNk80QjdtS21rYzdSeC1tRTVsTG1QTmtwRWNrbFcyQjBkQ1BqYTBwMXJJdDlIWjhnSkxWeVl4VGtIOW9FcWJYWFlvOTdRUGc?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 23 Aug 2026 02:42:00 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：宏遠-桃園 對 大眾控(3701)個股 單一券商歷史明細 - justdata.moneydj.com；國泰-松江 對 尖點(8021)個股 單一券商歷史明細 - justdata.moneydj.com；永豐金-三重 對 山隆(2616)個股 單一券商歷史明細 - justdata.moneydj.com

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [宏遠-桃園 對 大眾控(3701)個股 單一券商歷史明細 - justdata.moneydj.com](https://news.google.com/rss/articles/CBMiggFBVV95cUxOdFY4OEx5UkhMZy1KQzZncWxTcWZxejVXYkI3MnNLaFdEZTZsTjVUUHV1N3BwOVlNd3FjblB1X1FmZnFadlhQTlBrSjdBcG10bzA3M1pReXkxd1U1LV85bUlRTTdSYkVfam94cTBMb3Vyd2oxU3pKS29jcUxxYUtSdTd3?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 23 Aug 2026 11:51:42 GMT
- [國泰-松江 對 尖點(8021)個股 單一券商歷史明細 - justdata.moneydj.com](https://news.google.com/rss/articles/CBMihgFBVV95cUxPYWpDci1pdmhUTTU1OUNGVF9vWjZqZ0J6YmtFVUpoS0NPaFNXbGpCLXpPOTcwU2lPMUVYX1RPbkVMRUM4elhyYmc4S3FZUlJKQXlERGlSUDBjZ1N1N3RIYXZYbWZydGNiRUYxQ2dQMzFMTVJicjBnNUE3UEFLUFZOYmlscVp6QQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 23 Aug 2026 11:12:24 GMT
- [永豐金-三重 對 山隆(2616)個股 單一券商歷史明細 - justdata.moneydj.com](https://news.google.com/rss/articles/CBMikgFBVV95cUxOUHJGSzBiSjdQcngzcm5jR2R6a25GdXZIcm1EeVRRZzBBTnVrWGVxYmd0U1BDVnNNQjQtV1VtMm0yYUpkOHBZODZjZFV5VFRlS2xGenE2SVBETG9RYkN6Z3lXblRrTVdVc012XzNyS1NuV2Faam9JVS1sR3VqeXA2WUFTVXFCOGhqQlpLdFQ4ampCUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 23 Aug 2026 04:05:26 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：法人專欄分析內容-台股 - MoneyDJ；個股動態報導內容-A46B9F91-1834-46A1-929F-A90002C00586 - MoneyDJ；個股動態報導內容-911A9688-9FD0-4D87-A6D1-DE042C217F0D - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [法人專欄分析內容-台股 - MoneyDJ](https://news.google.com/rss/articles/CBMilgFBVV95cUxPaVMtX2otc0wybGpfOFFWTmJORGF6cXBvd1h4Z0tHSnNBU1lPUmNEaS16Zk9FeVB1LTU0LW1rZ2ZfOG5HdHFMdU5uRm5SaTZLVEI0RTBLNFNkNEtxMGtkU2g5VFNaSVl6dmcyM2FxUlJOTHh0ZVVDNXRwLVEzaF9pT185YUNVM3VEd3lFMS14SzVLaVRCd3c?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 23 Aug 2026 16:06:47 GMT
- [個股動態報導內容-A46B9F91-1834-46A1-929F-A90002C00586 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxPZlJiX0VJam9KcVRNRmFUN2dhbTgybW5pSW1IMmxxQlU3elZBTzVKZXlFaVFxWHh0a3dOUjhhZU5HYnhrZXhvbzVZemppYndPVmpjSXVCT05JdGJMRWdoLWJTdVdsM3VXTFBVQUhySVpCTDFXRm9aSTd0TmNSa1RBQnpVd2s5VXE5Y1k0VENSRFNlSnNk?oc=5) - Google News source discovery | MoneyDJ Sat, 22 Aug 2026 23:52:38 GMT
- [個股動態報導內容-911A9688-9FD0-4D87-A6D1-DE042C217F0D - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxPS3JYT2txTExnWXoxZXFIamtOeWJva3J1blN2eUlJX244MkRiS1BCU09wLUlJaUNYdGJCRFdaenIwWVRkRjFmODZFUHNjY2JacE0tUVotSWhWMW4tQTRlMUpqcHhjbXh5aWZldkJfVENzWDUwZnBFR0U5aGk5ekNsWkFoUVJTT3ZKWGw2eFFUaDJFeUE4?oc=5) - Google News source discovery | MoneyDJ Sun, 23 Aug 2026 01:43:00 GMT

## 新興題材：ic挖角Google晶片

摘要：新興題材：ic挖角Google晶片 相關新聞集中在：Anthropic挖角Google晶片大將布局自研半導體| 國際 - cna.com.tw

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [Anthropic挖角Google晶片大將布局自研半導體| 國際 - cna.com.tw](https://news.google.com/rss/articles/CBMiX0FVX3lxTE0wQ2JfOFNUYkpaaDNtR0JFd2hDRkRjajVabDVhMUo4X0o4aS1ZdkdqcWVoNXc3S0lqZzBnTDZsNERWanVBR3lOc2xBTjUyTURBdDZnVUlvcENXVTFRVDRB?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 22 Aug 2026 06:53:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
