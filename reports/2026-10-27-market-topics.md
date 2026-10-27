# 每日股市熱門話題分析 - 2026-10-27

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜負向｜熱度 7｜市場確認 99.66｜同向 4/4
2. **散熱與液冷供應鏈**｜負向｜熱度 1｜市場確認 85.81｜同向 1/1
3. **新興題材：AI散熱**｜負向｜熱度 1｜市場確認 85.81｜同向 1/1
4. **AI 伺服器與資料中心**｜正向｜熱度 21｜市場確認 9.38｜同向 2/8
5. **半導體與晶片供應鏈**｜正向｜熱度 5｜市場確認 2.99｜同向 1/3

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.07（樣本 18）
- 5日相關係數：0.31（樣本 12）
- 同向比例：9/18

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 99.66 | 4/4 | 0 | +9.88% | -1.61% |
| 散熱與液冷供應鏈 | 85.81 | 1/1 | 0 | +5.27% | -1.94% |
| 新興題材：AI散熱 | 85.81 | 1/1 | 0 | +5.27% | -1.94% |
| AI 伺服器與資料中心 | 9.38 | 2/8 | 6 | -2.71% | -0.91% |
| 半導體與晶片供應鏈 | 2.99 | 1/3 | 2 | -6.78% | +7.95% |
| 新興題材：輝達VR伺服器 | 0.00 | 0/1 | 1 | -2.17% | +7.95% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 相關性偏弱；應提高同向價格確認權重，降低泛 AI、泛半導體等寬標籤推估權重。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-10-14 | 0.08 | -0.29 | +57.14% | 14 |
| 2026-10-15 | -0.08 | 0.08 | +33.33% | 12 |
| 2026-10-16 | -0.13 | -0.25 | +64.00% | 25 |
| 2026-10-17 | -0.10 | 0.49 | +26.32% | 19 |
| 2026-10-18 | -0.12 | 0.33 | +21.74% | 23 |
| 2026-10-19 | 0.44 | 0.36 | +50.00% | 12 |
| 2026-10-20 | 0.09 | -0.81 | +69.23% | 13 |
| 2026-10-21 | -0.25 | 0.23 | +5.56% | 18 |
| 2026-10-22 | 0.02 | -0.21 | +38.89% | 18 |
| 2026-10-23 | 0.35 | 0.29 | +78.95% | 19 |
| 2026-10-24 | 0.09 | -0.31 | +70.00% | 20 |
| 2026-10-25 | 0.41 | 0.78 | +64.29% | 14 |
| 2026-10-26 | 0.27 | -0.25 | +36.36% | 11 |
| 2026-10-27 | 0.07 | 0.31 | +50.00% | 18 |

## 歷史回測摘要

- 回測日期：2026-10-27
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

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Chip Stocks Find Support Before Key Reports From Intel, Sandisk - Investor's Business Daily；Here's What $1,000 Spread Across These 4 Memory and Storage Stocks Could Be Worth by 2030 - Yahoo Finance；Here's What $1,000 Spread Across These 4 Memory and Storage Stocks Could Be Worth by 2030 - AOL.co.uk

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | -0.57 | -6.93% | N/A | 903.70 | 971.00 | -6.93% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.57 | -9.33% | -4.72% | 1,238.03 | 2,335.00 | -46.98% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | -0.43 | -2.17% | +7.95% | 216.00 | 228.38 | -5.42% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | -0.42 | -21.11% | N/A | 90.47 | 114.68 | -21.11% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「memory、Micron」，共 3 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 2 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Chip Stocks Find Support Before Key Reports From Intel, Sandisk - Investor's Business Daily](https://news.google.com/rss/articles/CBMimgFBVV95cUxQWEw1a2xadXdxUEZzckxXYWYyb1pxSm9YWXJDV1QyWHdDcEJrMTlQMVk4NlI2X0ZPMGhDUndGd1RFNlFqeHhSQjVTc0JCMUt3dnBuU3o4RVlQYXVBSjRNUWFHYkxlY01VUnR1Q3Fzc1JzTzVHXzAyd2NyS0dIeG9jWFZWdTlXdFM2cnlEeXZET0NPdVd2X2tSRzlR?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 26 Oct 2026 21:50:00 GMT
- [Here's What $1,000 Spread Across These 4 Memory and Storage Stocks Could Be Worth by 2030 - Yahoo Finance](https://news.google.com/rss/articles/CBMilAFBVV95cUxQNk41Q2k2NEdCRnV4eU5hX1ZtM003M3cxZ0NycWF6UzlYdVhZbHJlTU96bW9XY2xxYVRmTGZNYlpJT1U2NzdZbUlpZHFWZG52aXlZUUdQZXhyZFNJWWN2bkhtRVZzVG1Xbi1jRzhHTHRRVlU0dDFRU0l3eTNLTFdENzEtOHptUHBzVXlrNl9tM091ZW13?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 26 Oct 2026 10:20:00 GMT
- [Here's What $1,000 Spread Across These 4 Memory and Storage Stocks Could Be Worth by 2030 - AOL.co.uk](https://news.google.com/rss/articles/CBMie0FVX3lxTFBrajFCWmtjLUR4bjM1Y1g5d0ZhanZYb1d4aUtJbHRBNFdjWmhaTTNheHAtY3NjXy1aakVrakJqRlRQQ09oWUtwRmt1TExoVHdaSHRiTzFzd1Z5SGl2bWhNblRKNjVtMzhZUVJkUGZUQldjZW9ON1BzRWctUQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 26 Oct 2026 10:20:00 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | -0.43 | -5.27% | +1.94% | 3,145.00 | 3,435.00 | -8.44% | 同向 | 75.13 | 41.92 | 21.02B TWD / 44.92% | 2026-10-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 1 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：跌停。

### 主要來源

- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 25 Oct 2026 12:32:30 GMT

## 新興題材：AI散熱

摘要：新興題材：AI散熱 相關新聞集中在：焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | -0.42 | -5.27% | +1.94% | 3,145.00 | 3,435.00 | -8.44% | 同向 | 75.13 | 41.92 | 21.02B TWD / 44.92% | 2026-10-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 1 篇新聞命中。 方向判斷命中詞：跌停。

### 主要來源

- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 25 Oct 2026 12:32:30 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel Rises 5% as New Street Upgrade Cites Server CPU Shortage; AMD and NVIDIA Gain 3% - 24/7 Wall St.；Intel: Agentic AI Is Making CPUs A New Bottleneck (NASDAQ:INTC) - Seeking Alpha；Intel (INTC) Unveils Crescent Island GPU D Series For Agentic AI - Yahoo Finance

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.28 | -21.11% | N/A | 90.47 | 114.68 | -21.11% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.27 | -2.17% | +7.95% | 216.00 | 228.38 | -5.42% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.53 | +2.94% | N/A | 531.28 | 531.28 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.03 | -1.45% | -2.25% | 2,385.00 | 2,480.00 | -3.83% | 背離 | 86.28 | 27.65 | 511.86B TWD / 54.65% | 2026-10-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | +18.29% | +8.25% | 532.60 | 532.60 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -11.12% | -12.86% | 329.17 | 446.77 | -26.32% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.02 | -2.39% | -2.82% | 654.00 | 703.00 | -6.97% | 背離 | 13.92 | 47.32 | 88.13B TWD / 45.52% | 2026-10-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.02 | -4.64% | -3.72% | 4,010.00 | 4,920.00 | -18.50% | 背離 | 60.69 | 66.23 | 55.40B TWD / 1.97% | 2026-10-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel、INTC」，共 3 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：shortage, upgrade。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。 方向判斷命中詞：shortage, upgrade。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。 方向判斷命中詞：shortage, upgrade。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Rises 5% as New Street Upgrade Cites Server CPU Shortage; AMD and NVIDIA Gain 3% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMixgFBVV95cUxNTWpBX0ZyOWZISEViUlRGWExyVWc0WXFYNFNaMm1YTGg1dnZzYlhLaGs1Zm9Ob01TZlhWOVQxVm11NVh3RmltV2hab040ODlWTWthc01oVnp6YTVqM2Y2TEx4SllpcVNVVjNpd1FUYlBlYmhMZ2E3THdYeWpzOFctYXNBY2Flamw0STlONXBrajNHM1huMjRkQ1ZBNDY1dkd5VXRjT0FzbWdQcXN2MnJrVnVDdzdsaEpySXREZWQ5MVZUSmFteEE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 26 Oct 2026 18:50:00 GMT
- [Intel: Agentic AI Is Making CPUs A New Bottleneck (NASDAQ:INTC) - Seeking Alpha](https://news.google.com/rss/articles/CBMijwFBVV95cUxPckJrNDZtMnl3ZmFVTnp2UUEwSG5YNGVkWFhRQncxazBYWlF2S0ZLQmVqQ0lvZC1sNHktTTk2SldMT2xqZ3hITFUxa0x0b01hblN1WWc0XzlJOUkwRHItelozdGNDbm1ReXJhX3dCMDZBdGpmMkdrck0zT0tHS1RLRXdGY1pFalR1V2FuM1BTVQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 26 Oct 2026 18:05:42 GMT
- [Intel (INTC) Unveils Crescent Island GPU D Series For Agentic AI - Yahoo Finance](https://news.google.com/rss/articles/CBMinwFBVV95cUxPZGNLUTY5a09NcUxUeEFyNXZfekRlQTdXbGVnOUpFTDJNRTdnZ3h0a1ZhYk9jZXUzT3JaaDV0ZnRuNWI0UHhReUV6Y0VEd2xtRC10U1phQ2hCVFF1VWdqcTZ5eVBiMEV3STNlel9jODRDdVpYYWlES0g2LXNvQUNlajRTZkQ5OHp0c0FCdGRxaTB6eXBzUjc2c0F3XzE1UWc?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 26 Oct 2026 10:09:02 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel Rises 5% as New Street Upgrade Cites Server CPU Shortage; AMD and NVIDIA Gain 3% - 24/7 Wall St.；立陶宛雷射技術札實 攜手台灣攻半導體 - 中央社 CNA；要開天窗？越南首座半導體廠明年試產難未敲定ASML設備採購- 國際 - 工商時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.26 | -21.11% | N/A | 90.47 | 114.68 | -21.11% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.23 | -2.17% | +7.95% | 216.00 | 228.38 | -5.42% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.45 | +2.94% | N/A | 531.28 | 531.28 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -1.45% | -2.25% | 2,385.00 | 2,480.00 | -3.83% | 不適用 | 86.28 | 27.65 | 511.86B TWD / 54.65% | 2026-10-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | -4.56% | -5.99% | 125.50 | 164.50 | -23.71% | 不適用 | 6.68 | 18.87 | 25.35B TWD / 27.22% | 2026-10-01 |
| MU 美光 | 產業/供應鏈推估 | 0.00 | -6.93% | N/A | 903.70 | 971.00 | -6.93% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -9.33% | -4.72% | 1,238.03 | 2,335.00 | -46.98% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -11.12% | -12.86% | 329.17 | 446.77 | -26.32% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：shortage, upgrade。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：shortage, upgrade。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：shortage, upgrade。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Rises 5% as New Street Upgrade Cites Server CPU Shortage; AMD and NVIDIA Gain 3% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMixgFBVV95cUxNTWpBX0ZyOWZISEViUlRGWExyVWc0WXFYNFNaMm1YTGg1dnZzYlhLaGs1Zm9Ob01TZlhWOVQxVm11NVh3RmltV2hab040ODlWTWthc01oVnp6YTVqM2Y2TEx4SllpcVNVVjNpd1FUYlBlYmhMZ2E3THdYeWpzOFctYXNBY2Flamw0STlONXBrajNHM1huMjRkQ1ZBNDY1dkd5VXRjT0FzbWdQcXN2MnJrVnVDdzdsaEpySXREZWQ5MVZUSmFteEE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 26 Oct 2026 18:50:00 GMT
- [立陶宛雷射技術札實 攜手台灣攻半導體 - 中央社 CNA](https://news.google.com/rss/articles/CBMiU0FVX3lxTE5Id29IdlM0aVVHMzh1MDI4U2RNT0pndGp5aXN6a1hrNjBsNGJjTlREY0hndEo4ck9mNHJPWFRVdVlndXc1TTc1dEJ2S2R6S3lsakJv?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 25 Oct 2026 09:49:55 GMT
- [要開天窗？越南首座半導體廠明年試產難未敲定ASML設備採購- 國際 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1PN3M4TGJxV1lXQWlMUERWSUJlemxzcmVjYnR4VWszMWNITHctSjdwRXZINVVmcE9zSktVWTJOS3N5LTh3YjFpSWlkdFdESGZ0V3JwRTBRdXBVRVhaNjlV?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 26 Oct 2026 10:59:00 GMT

## 新興題材：輝達VR伺服器

摘要：新興題材：輝達VR伺服器 相關新聞集中在：輝達VR伺服器啟動出貨 法人點名6大受惠產業 - 自由財經；輝達VR伺服器啟動出貨 法人點名6大受惠產業 - 自由時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.24 | -2.17% | +7.95% | 216.00 | 228.38 | -5.42% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 2 篇新聞命中。 方向判斷命中詞：受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [輝達VR伺服器啟動出貨 法人點名6大受惠產業 - 自由財經](https://news.google.com/rss/articles/CBMiZEFVX3lxTFBYWThKS0F4UG1fZEhRWExid0ZjSGwyaFpUaUk3YTNzUWlmbGhvTzVvYXMxdnlkSDJ3WVNNajJadXpVUWJFa1M1cGtRczc2S1hjdVN1QmJILVhCUWhDeGpjNXMyS2HSAWRBVV95cUxQWFk4SktBeFBtX2RIUVhMYndGY0hsMmhaVGlJN2Ezc1FpZmxob081b2FzMXZ5ZEgyd1lTTWoyWnV6VVFiRWtTNXBrUXM3NktYY3VTdUJiSC1YQlFoQ3hqYzVzMkth?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 26 Oct 2026 04:53:45 GMT
- [輝達VR伺服器啟動出貨 法人點名6大受惠產業 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFB2dnBmWldoZXcwQW8zb29KamtLbmJmbU50ODlkUFNVNkt1ZFNkamJDT1JhQVFNamNRVDNMaDVDSEZPZkgyWjE4QWVpdzFtRldLUWJfVW1wbVg?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 26 Oct 2026 08:56:40 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股五利多強抗四利空 法人：短線拚重返 47K - 經濟日報；台股震盪格局 法人四策略教戰 投資人逢回可中長線布局 | 市場焦點 | 證券 - 經濟日報；專家看後市 六大關鍵牽動台股 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股五利多強抗四利空 法人：短線拚重返 47K - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE82ZjRKNlEzVFhWTXJ1VE0wUzREMGluNXA0WG1wQ2xoWVdFWHRZNklnSXVMRWRBay1iZWR1RHJUd3pPNWpDWVQ3dGJUUGFTeXFxdjZEVE0yc0M0QdIBX0FVX3lxTE9kelROdjZwUU54WWpCbjVYcjN3Nm4ycjNBTy1zNmhoTW9qMjN4SDBxYUNnQzdzWXRQSXMtdGxLaFh5UVlPLWVjaEV6T2EtSXFXQ0M1U1NBS0JuX0tGeXVB?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 26 Oct 2026 17:36:45 GMT
- [台股震盪格局 法人四策略教戰 投資人逢回可中長線布局 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9Rc3RQUjA4TkVVWWU2b3Q0LXplS0N5NGRRYlZtQXU0XzlYN3czUHZNcVlEOHJXb1VEQjZKNGNQUWwwdUVMN0xzY0F2cUxsN2oyN21XZkhWZ3Vndw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 25 Oct 2026 09:00:00 GMT
- [專家看後市 六大關鍵牽動台股 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxPQnVGTkVaWkthZ1ltVWVhR0RIWTM2ckR2Q05xY0czaDZQX3B4WktXUGE4VkhlYTk3eFVXUm9zS0NKbVJzNGJKRDN2VV9FY2doYkFubTFrZ1Qyd1RMdF9LcWN5bzdpWmtlWDRfRmU4MmFZUXQ4REpGMjVfY0w3bV93b9IBX0FVX3lxTE9CemhLY0hHY3lTSHpfbHU4RUVkY2hfcWhwOXlzRW4zOWd3OUEzQ2R4anFMNXMzNnNJSG5EUVB6MWt1bjR5ZjFQNmdhNDZfWTB4YTV5aC05bmFXTklsR1NN?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 26 Oct 2026 15:46:01 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：法人盤勢分析內容-台股 - MoneyDJ；敦吉 拚連六年賺半個股本(經濟日報，無內文) - 台股 - 新聞 - MoneyDJ；永豐金-埔里 對 太極(4934)個股 單一券商歷史明細 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [法人盤勢分析內容-台股 - MoneyDJ](https://news.google.com/rss/articles/CBMijgFBVV95cUxQQ0dDc0hFbkxDbl9HX2RxNl80MVNwRDhuakkwMDBxU1J4NC1VSEZ6bXN1MnZnajNRR202UHVtRnZOUjJhV0dObWR0NHVTa1pzc2dJekRRZmxxbWswU2N4Rk9YekRaV2NUQ01rVklQU3h6VkN0Yl9lMkdneGw4NGtKWTJSejh1eUljbGV1UzVB?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 27 Oct 2026 00:43:13 GMT
- [敦吉 拚連六年賺半個股本(經濟日報，無內文) - 台股 - 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMimwFBVV95cUxPUmRDQ0hiaEFLSk85Rk8zSy1WTUxFRDZoUFJ2SWwzeXJCbzhMeXlFZGhvbGl0enNWbWhETVVLLU9ITmZQYWg0Wk5Jc2xVeUdick9XQklYZnphMjgyVzE4ZnJwOHR5czhqdjZiWFRlUTI2cllac3ZVeFVzSTY5SE9fN1d5NlU1T1FGWjR5blZNY1RocTV4UTA1VnBJTQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 27 Oct 2026 00:02:00 GMT
- [永豐金-埔里 對 太極(4934)個股 單一券商歷史明細 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPRDA5dE0ybWk0Y0RmSDNCYk5Sa3VvT2p5TDB0Y0hTdHo2SnZPYlNobDJYeFRxYzlYLVZnTTVhcFozVk5ya043TDNMdEJoOVFBWXE5NEtUWTctNEF2MllfR3lTcGNoYURSamk5LW9RTlB1SmE5SXd0QTVlNENXZXpUVkd2OHMwdHllNVhXZGVubElwdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 26 Oct 2026 08:40:06 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
