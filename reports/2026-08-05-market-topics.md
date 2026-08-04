# 每日股市熱門話題分析 - 2026-08-05

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **AI 伺服器與資料中心**｜正向｜熱度 15｜市場確認 76.66｜同向 4/6
2. **記憶體與 HBM 供應鏈**｜正向｜熱度 11｜市場確認 100.00｜同向 1/1
3. **新興題材：SpaceX**｜正向｜熱度 3｜市場確認 100.00｜同向 1/1
4. **半導體與晶片供應鏈**｜正向｜熱度 9｜市場確認 53.08｜同向 3/5
5. **關稅與供應鏈轉移**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.39（樣本 14）
- 5日相關係數：0.44（樣本 14）
- 同向比例：9/14

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| AI 伺服器與資料中心 | 76.66 | 4/6 | 1 | +10.00% | +12.97% |
| 記憶體與 HBM 供應鏈 | 100.00 | 1/1 | 0 | +11.54% | +30.25% |
| 新興題材：SpaceX | 100.00 | 1/1 | 0 | +11.54% | +30.25% |
| 半導體與晶片供應鏈 | 53.08 | 3/5 | 1 | +3.69% | +18.61% |
| 關稅與供應鏈轉移 | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | 0.00 | 0/1 | 1 | -23.22% | -16.07% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價呈負相關；應檢查正負向詞庫，並降低新聞直接提及但股價背離的權重。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-07-23 | -0.01 | 0.01 | +41.67% | 12 |
| 2026-07-24 | -0.16 | 0.43 | +50.00% | 6 |
| 2026-07-25 | 0.30 | -0.06 | +12.50% | 16 |
| 2026-07-26 | 0.38 | 0.06 | +23.53% | 17 |
| 2026-07-27 | 0.54 | 0.11 | +37.50% | 8 |
| 2026-07-28 | 0.32 | 0.13 | +36.36% | 11 |
| 2026-07-29 | 0.16 | -0.03 | +92.31% | 13 |
| 2026-07-30 | 0.25 | 0.92 | +66.67% | 6 |
| 2026-07-31 | 0.10 | -0.10 | +46.15% | 13 |
| 2026-08-01 | 0.38 | 0.25 | +54.55% | 11 |
| 2026-08-02 | 0.06 | -0.21 | +33.33% | 9 |
| 2026-08-03 | 0.35 | -0.49 | +60.00% | 5 |
| 2026-08-04 | 0.05 | -0.08 | +46.15% | 13 |
| 2026-08-05 | -0.39 | 0.44 | +64.29% | 14 |

## 歷史回測摘要

- 回測日期：2026-08-05
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

摘要：AI 伺服器與資料中心 相關新聞集中在：AMD leads AI chip stocks higher ahead of Q2 results - Seeking Alpha；Intel, AMD Lead Powerful Chip Stocks Rally on AI Optimism - TradingView；Marvell Stock Surges 10%: Next-Gen AI Storage Unveiled Ahead of Q2 Earnings - Marvell Technology (NASDAQ - Benzinga

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AMD 超微 | 新聞直接提及 | +0.57 | N/A | N/A | 518.58 | 518.58 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.54 | N/A | N/A | 100.86 | 114.68 | -12.05% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.04 | +0.38% | +21.53% | 211.94 | 211.94 | 0.00% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.06 | +5.22% | +1.75% | 2,320.00 | 2,425.00 | -4.33% | 同向 | 74.39 | 31.19 | 442.68B TWD / 67.87% | 2026-07-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | +25.48% | -2.74% | 492.81 | 506.69 | -2.74% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -6.40% | +35.10% | 418.16 | 446.77 | -6.40% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.04 | +15.84% | +5.60% | 585.00 | 680.00 | -13.97% | 同向 | 10.86 | 54.32 | 65.78B TWD / 32.86% | 2026-07-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.04 | +19.47% | +16.59% | 3,865.00 | 4,310.00 | -10.32% | 同向 | 60.69 | 63.83 | 58.01B TWD / 2.80% | 2026-07-01 |

關聯理由（前 3）：
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。 方向判斷命中詞：rally, surges。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：rally, surges。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：rally, surges。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AMD leads AI chip stocks higher ahead of Q2 results - Seeking Alpha](https://news.google.com/rss/articles/CBMikwFBVV95cUxOTjR4UWRHSXNHM0g3Q2dBUWkwMmZYNllicTZPNEdna2tHTUw4R0RHcWdtUjNESURsazBJV1RoMURlQXhkbDA3eTdKTmxEVTlIZkJTYnAxbU9RNWdINDFzbXdFVVloaTlXRlJJdmlHSVFITUw4SEdsNUwwNE0yNlJ3QVpYN0JKbFlydjZESVdrVU91ak0?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 04 Aug 2026 15:19:38 GMT
- [Intel, AMD Lead Powerful Chip Stocks Rally on AI Optimism - TradingView](https://news.google.com/rss/articles/CBMitwFBVV95cUxPcVltYWlSdHFQLUVFVXNBYUZFMEw4eGJZaFMzY0s3bTlyd1BKb0ZITGtNUlZqMzhvaXFVN3FXMnVPbDI1d0F4YnRLUzBqQUZrUmtndjRjZFc4NUt5MkUybm4tRVUzdzdIZkx4WENiOGdwbGhGYjludFZLVDJCN0ZhSjY0dTVGajZLUlhQMVl1YUs1c2ZaVVVhcmhBWkxCSFVKZVdfUjhzNE42WDh1VDI0cHRhdXlyX2M?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 04 Aug 2026 20:27:13 GMT
- [Marvell Stock Surges 10%: Next-Gen AI Storage Unveiled Ahead of Q2 Earnings - Marvell Technology (NASDAQ - Benzinga](https://news.google.com/rss/articles/CBMixAFBVV95cUxNUzRjY2J0Ujh1Wkh3cUp5cks1NzhuVXg2dk5oY3NtLXQ2bTRTU05IcTQ2QUV6UHdSdlZqTU1PTDBJdE0ya1hkMVREVW52NE5PVDl0cndsNUhsUDJFSThKaWY1ZERQa3Y2d1BYbEowcUdrbDg5R1JTN1BuVkJlanptTGwxOThycWt5dlZmbVdvbVBqZTFQUV85TlJoVTViRC1vaG5EZUhpSVZmVEIwOGtZMWszUDV6RHdvdmN0R1h1WXBpZWs3?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 04 Aug 2026 15:50:08 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：MU, INTC, SNDK: Chip Stocks Rally After-Hours On AMD’s Blowout Report - Stocktwits；Sandisk Jumps 8%, Micron Gains 6%, SK Hynix Climbs 4% as Wall Street Hikes Price Targets on AI Memory Boom - 24/7 Wall St.；SanDisk Is Down 45% in a Month. Should Memory Investors Switch to Micron or SK Hynix Now? - AOL.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.48 | N/A | N/A | 892.67 | 971.00 | -8.07% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.48 | +11.54% | +30.25% | 1,427.62 | 2,335.00 | -38.86% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.36 | N/A | N/A | 518.58 | 518.58 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.36 | N/A | N/A | 100.86 | 114.68 | -12.05% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +0.38% | +21.53% | 211.94 | 211.94 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron、memory」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK、SanDisk」，共 6 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [MU, INTC, SNDK: Chip Stocks Rally After-Hours On AMD’s Blowout Report - Stocktwits](https://news.google.com/rss/articles/CBMiygFBVV95cUxPeVlYaXJjQjNtTkNRQUxQTHhaLUFMbE80Uy1MeDBpV0FPdkg2SHRLdkdfVUpXM1NrNWhZSVZQQ01sa0o4T1hKdzF1clBFRlRWUmMwWGxQTDNVVFBpOVhObUc2MXpBeXBOZ0p3R0w5NGRNOHB4X0ZIXzhlT0NMbmhzc1RtdmJRTWhlRUhKSHpyVnpaU0VGMlJyU2tDcmdkTG1hWVJJbmtTVDREbzFfWDB4bjhuTGswN3lmdkdHQzY1dzFOVU41VGlBNlZn?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 04 Aug 2026 00:53:59 GMT
- [Sandisk Jumps 8%, Micron Gains 6%, SK Hynix Climbs 4% as Wall Street Hikes Price Targets on AI Memory Boom - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi3gFBVV95cUxNX3RkZTFpYXNYODl4ajlmaVY1TkRXS01UWU5BMUpMU0RSakdZbUR3RGhKSVlMOHppTGNTenltNEQyR2pFOV83cEhVY0JYc1c5eFpCUGJHQUZpSUdDTmx6SzQ4SnJDRVBYNVAycUFnSFZtbkxXblp6SEt2T05QX0FOUWRuT0RRWmp6ZkdjREhNanNVX2tqbzNkYjVrcW5FN19aNHo4R19xQU02LVhTdTJPa1RfMnF4TFV3SUJuX19mVWxOenJMS2tMdTlISm1oc21TQ05IV0gtUmpJTUNrNmc?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 04 Aug 2026 17:36:33 GMT
- [SanDisk Is Down 45% in a Month. Should Memory Investors Switch to Micron or SK Hynix Now? - AOL.com](https://news.google.com/rss/articles/CBMifEFVX3lxTFBXcVYzU2hVa2JURGN0eDlIMzhQVHJkd2VWWklJTlFQT1JQZS1aSG9QSE1ZZHUwdHFRWnFRczR2TTFpU1EyUWtZeU1Uem1ydmw5TmhVVEJfYjk5WnBDcGJrRWVtckxzakJDWjNPNWZNaXRuak9nNjhoejNlMWc?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 04 Aug 2026 14:18:49 GMT

## 新興題材：SpaceX

摘要：新興題材：SpaceX 相關新聞集中在：SpaceX quarterly revenue surges in debut results as satellite, AI businesses surge - Reuters；Stocks making the biggest moves after the bell: SpaceX, AMD, Pinterest, Arista Networks, Wynn Resorts & more - CNBC；Stocks making the biggest moves midday: Palantir, Amazon, SpaceX, Sandisk, Snap & more - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AMD 超微 | 新聞直接提及 | +0.42 | N/A | N/A | 518.58 | 518.58 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.42 | +11.54% | +30.25% | 1,427.62 | 2,335.00 | -38.86% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。

### 主要來源

- [SpaceX quarterly revenue surges in debut results as satellite, AI businesses surge - Reuters](https://news.google.com/rss/articles/CBMiywFBVV95cUxNRkFZQkJoRmRlajg5SzYxaU5EQVZ3U2RYbUtyZHRfcndUVmpYb3lwWm5DNmtVMFY3bFZoLVEyaVJ0b0dmRWYxZ05vSXhRaWFLVXVlVG9MSmV2Qjg4OEFTNU4xLU5ST2NOMDh5b3NOM1J4cGgzQmFIRjBEOUNlZXhaQ1JoV0VPeS1ZWW9XX1ZSUnZJQ19kNHN6cnYwWHFoN25saEltTjZNQWhlclNieEJCQ1VWUGtDRC1xcjNEUmxjMG9KYVJLaGNHU2RJaw?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 04 Aug 2026 21:22:28 GMT
- [Stocks making the biggest moves after the bell: SpaceX, AMD, Pinterest, Arista Networks, Wynn Resorts & more - CNBC](https://news.google.com/rss/articles/CBMiqwFBVV95cUxPUFB4VVZSMjVhUkR1ZUV5V0FEU3ZNaV9XS1U2cGMzdkxyRThMbTFIaWRIMGJxSl9rVU9OSnZMSEF1bWpoNXFlcFpqWXlKbUhtRlNqSHdnNTFVREdNWG80aUN0eVVQYTBUNm5EdXdYME5nRnN6THV0b0FCN1ZWalM4c1FyYmh5X2U4MHA5OHBkWDdHcEVPdTVkVkRJY1R6azBCSGo4d2JKQ3IwV0E?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 04 Aug 2026 20:53:14 GMT
- [Stocks making the biggest moves midday: Palantir, Amazon, SpaceX, Sandisk, Snap & more - CNBC](https://news.google.com/rss/articles/CBMiogFBVV95cUxNMkEydnA2SDNxU25xUXdXRkowbElia3dGRF95dDMyQTNkMzYyWmJOOVlyc3k1NzRpUEVZVjF2cTZlWm1mNWJCbGNFeFdkQ1RLa0pxU2dWRkhnakVHTXNUcjlfM21NcXFEZmN4UWpJWkhHNVFnWjBPbGdiNEw5MDlmVjgySFlCNDM1NUNQWHdkQ25jOTkyWUFFSkljZ212WGdvTWc?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 04 Aug 2026 16:59:49 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel Soars 10%, AMD Jumps 8%, Broadcom Rises 6% as Chip Stocks Ride a Risk-On Rally - 24/7 Wall St.；AMD leads AI chip stocks higher ahead of Q2 results - Seeking Alpha；AMD to report Q2 earnings as chip stocks continue to waver - Yahoo Finance

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AMD 超微 | 新聞直接提及 | +0.57 | N/A | N/A | 518.58 | 518.58 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.57 | N/A | N/A | 100.86 | 114.68 | -12.05% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | +0.25 | -6.40% | +35.10% | 418.16 | 446.77 | -6.40% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.06 | +5.22% | +1.75% | 2,320.00 | 2,425.00 | -4.33% | 同向 | 74.39 | 31.19 | 442.68B TWD / 67.87% | 2026-07-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.06 | +7.73% | +4.41% | 118.50 | 164.50 | -27.96% | 同向 | 6.68 | 17.82 | 23.12B TWD / 22.85% | 2026-07-01 |
| NVDA 輝達 | 產業/供應鏈推估 | +0.03 | +0.38% | +21.53% | 211.94 | 211.94 | 0.00% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | +0.04 | N/A | N/A | 892.67 | 971.00 | -8.07% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.04 | +11.54% | +30.25% | 1,427.62 | 2,335.00 | -38.86% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- AMD：新聞直接提及「AMD」，共 4 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：risk, rally, strong。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel、INTC」，共 3 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：risk, rally, strong。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AVGO：新聞直接提及「Broadcom」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：risk, rally, strong。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Soars 10%, AMD Jumps 8%, Broadcom Rises 6% as Chip Stocks Ride a Risk-On Rally - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiwAFBVV95cUxPd0NBY05teWNwSG9tcDRjYWlHcjMwdDNBOHFDb3NWb0VOc0VOT2pCUkNPMTVxMFRETVJjWVFJWm5aMEpyTVJvT3RxSThlejBaOS0tckdWMjNyVjJ1bUJFZUozN0J1VWxpQk1oZy1LWHZJOHk4NEhQakVaa21NV1lKMzFwTXBZYTFsQWRiYzJ3eFZkRGdhREdpZU1QSjdJdGM4SmVHQXhfWWkxcTR4UmZxeU1vRHBWcVBZTEVrSTBIY2c?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 04 Aug 2026 16:36:11 GMT
- [AMD leads AI chip stocks higher ahead of Q2 results - Seeking Alpha](https://news.google.com/rss/articles/CBMikwFBVV95cUxOTjR4UWRHSXNHM0g3Q2dBUWkwMmZYNllicTZPNEdna2tHTUw4R0RHcWdtUjNESURsazBJV1RoMURlQXhkbDA3eTdKTmxEVTlIZkJTYnAxbU9RNWdINDFzbXdFVVloaTlXRlJJdmlHSVFITUw4SEdsNUwwNE0yNlJ3QVpYN0JKbFlydjZESVdrVU91ak0?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 04 Aug 2026 15:19:38 GMT
- [AMD to report Q2 earnings as chip stocks continue to waver - Yahoo Finance](https://news.google.com/rss/articles/CBMiugFBVV95cUxQWXBhRk5HYUtYR2NZamZqZVZiU1BBd0tVeUpWTW81eXdndkdKdV9mMTYyVjdQc1FKNmhURm9NdXJwOGtqMmZRYTZpTmdTazlLbkhQNHV0bDFxWkx5azhfamxhck55UVllbUl3VjBzNkNoc2FaOHdWZ0Vwel83N0dfV0hSZFdWUkFoQ3NKUzFWN3RqeUlJSVkxNEhVdWRVenkzbGxHdlk4MTlOVUhjSEUyN2lhQWxPemZsdmc?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 04 Aug 2026 12:42:58 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：切入四大CSP水冷供應鏈！法人看「這檔」全年EPS上看94.8元 GB平台、ASIC訂單齊發 - FTNN 新聞網；九大雲端業者資本支出近9000億美元 AI供應鏈迎商機 - 蕃新聞

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +17.11% | +33.27% | 309.38 | 312.06 | -0.86% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | +8.93% | +5.04% | 250.00 | 289.00 | -13.49% | 不適用 | 14.13 | 17.76 | 821.76B TWD / 52.11% | 2026-07-01 |

關聯理由（前 3）：
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [切入四大CSP水冷供應鏈！法人看「這檔」全年EPS上看94.8元 GB平台、ASIC訂單齊發 - FTNN 新聞網](https://news.google.com/rss/articles/CBMiS0FVX3lxTE5fa2U5clpzcXJJdnJpWWpLNk44WU1felhZNmdIRG41UDkwdlZ0RkNrWDF4OGxpM0NmZFdPUDlULTZmRC1nUlBLSWNmYw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 03 Aug 2026 13:45:00 GMT
- [九大雲端業者資本支出近9000億美元 AI供應鏈迎商機 - 蕃新聞](https://news.google.com/rss/articles/CBMiUkFVX3lxTFBWZ0lQNVpoeEpubm1YVWdSMG5Hamluc0N2TE9iRDV6anJRQnZzMDJpeVJfMmY2UVc5TlNrWWlURlUyYVlRZ3RBWE1UNHdaSktDdEE?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 04 Aug 2026 11:07:00 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：焦點股》健策：AI散熱賣壓沉重 再探跌停 - stock.ltn.com.tw；切入四大CSP水冷供應鏈！法人看「這檔」全年EPS上看94.8元 GB平台、ASIC訂單齊發 - FTNN 新聞網

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | -0.21 | +23.22% | +16.07% | 2,600.00 | 2,835.00 | -8.29% | 背離 | 61.06 | 42.72 | 17.62B TWD / 66.11% | 2026-07-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 1 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：跌停。

### 主要來源

- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - stock.ltn.com.tw](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 03 Aug 2026 19:56:20 GMT
- [切入四大CSP水冷供應鏈！法人看「這檔」全年EPS上看94.8元 GB平台、ASIC訂單齊發 - FTNN 新聞網](https://news.google.com/rss/articles/CBMiS0FVX3lxTE5fa2U5clpzcXJJdnJpWWpLNk44WU1felhZNmdIRG41UDkwdlZ0RkNrWDF4OGxpM0NmZFdPUDlULTZmRC1nUlBLSWNmYw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 03 Aug 2026 13:45:00 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：8月台股 ETF 配息一次看 00878、00929、00891等配息飆新高 - 經濟日報；台股多空戰情境推演 突破月季線反壓機率高 蓄勢攻45.5K - 經濟日報；台股鬆綁關禁閉 改革才剛開始 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [8月台股 ETF 配息一次看 00878、00929、00891等配息飆新高 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1uaUFsaXgyRUh3aUI1OWVDQV81WEpVMjg0dFUtQmFOdkpidnNXdDY5SHhpM1p2RTM3OWl5QjQ2d21hdHEwWl9saGg3QTZETF80WjBabWZWcm1DQdIBX0FVX3lxTE9TcnRVa0psdHE1dHlNQTZyN0xyRTEzZGMzRHRyblp4Qk1Hb0dwTDhEYTNod3AtZ1Ytb3lKdERwLUNwRHNzeGdyLUtWSU8tTWpOc1JybHdPbW1qWXhuLTRN?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 03 Aug 2026 09:00:00 GMT
- [台股多空戰情境推演 突破月季線反壓機率高 蓄勢攻45.5K - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1IRjFJVW13WlcxUkh3NXNBbVdhT3Fya2lKSU9hcEEwXzBNNUtyekVOaExfZzhaRXBFRDYxOC0tSHpjbE9VRzJIRlJKekhzUG9PSUtJdkRnWndsQdIBX0FVX3lxTE1QOFlBbXlKNjNDZkRCNUdUcjNXdlBBZE5DTTc3U2pHSUkwcGhOYzROU0pnellzcFd1TkJ4MjliQ1pLZVFIVGxab0ktQWYtdTNUa2kyc0JxanA5T3NxOWtj?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 03 Aug 2026 09:00:00 GMT
- [台股鬆綁關禁閉 改革才剛開始 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1KQ0w4dGxmM19EejYtTGVzZk4wdTRCSER2M1FJOWpQWXU2WGotNGpIVjRUaDJ5S09CcC05OHlKUmptUExMR1d1V0JHREdqdEg0Uk1VaHoxWlpXZ9IBX0FVX3lxTE1mOFJWN1J1SkNRSC1Rd2VMWG5wczYxTWpGa0xTclJBMWhBUG9mWTVwSnRvZTJ4ajdIYnphNVNQYXhBS05aOWFFelJUeGYzd3VzR19GYVlyMkpkN3RDa1Fr?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 04 Aug 2026 17:27:07 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《強勢台股特報》全新,華榮,景碩,光寶科等20檔 - MoneyDJ；《台股盤後》震盪小跌25點，月線得而復失- 新聞 - MoneyDJ；個股動態報導內容-9DD2EEE2-BBA0-4765-BCF7-C7396DA26A84 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《強勢台股特報》全新,華榮,景碩,光寶科等20檔 - MoneyDJ](https://news.google.com/rss/articles/CBMieEFVX3lxTE5tcEZZT3dPb0hMeV8zTmhVdUJiWWhEMzQ0Qjg3dTl6MW4xM3kyUzBUaHlWUkxXS20zel9Jc21tRi1NMlBEX2FPY0ZUNU5OeTBVWWRmYUZiNVk5UUZ6WVJtV1l0WDd6a3ItUEZCalBWUlAyRGhDZTBNMA?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 04 Aug 2026 01:10:00 GMT
- [《台股盤後》震盪小跌25點，月線得而復失- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxOTlIyOXJiOFdGOVlxaFdKS3FPLTQxMUNqWGtaM3lSY3ZvVkFpZ0paTlFkWUFiaDRhd1JQV0otOE9mN0VWSGQtalFtT0NveUkzZTV0TFdCVWVKNF81R2NxakFnbDY2Rk9Sc1BtSTVBazRtYTZ1NnpPU3dWZi1pU25qNjZYZkVURHVYbmF5Z2M4Ui1EQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 04 Aug 2026 07:42:00 GMT
- [個股動態報導內容-9DD2EEE2-BBA0-4765-BCF7-C7396DA26A84 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxPQmVaQ291S3Q4a3pfaWstdUdXME1rNTdMSDlnSVpRd1dsY1ZpUGNOcDBSYnhkSTlib1ZtZnNKVmhZcUZORVAzM3BNMnkyOTN4cjlHR3pFdmpMOXo1dVVwUTFtUGI4cUY0UUtJTWk3WUd3ZnpjSEZ4bTk1bU50bFV3OWFIXzhKdTlWQnZ1RmlLcmdCWXgz?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 04 Aug 2026 10:40:19 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
