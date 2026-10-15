# 每日股市熱門話題分析 - 2026-10-16

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **半導體與晶片供應鏈**｜負向｜熱度 7｜市場確認 75.89｜同向 7/8
2. **記憶體與 HBM 供應鏈**｜中性｜熱度 6｜市場確認 N/A｜同向 0/0
3. **散熱與液冷供應鏈**｜負向｜熱度 3｜市場確認 85.70｜同向 2/2
4. **關稅與供應鏈轉移**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
5. **先進封裝與 CoPoS**｜負向｜熱度 3｜市場確認 53.75｜同向 5/7

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.13（樣本 25）
- 5日相關係數：-0.25（樣本 18）
- 同向比例：16/25

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 半導體與晶片供應鏈 | 75.89 | 7/8 | 1 | +4.88% | +5.87% |
| 記憶體與 HBM 供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | 85.70 | 2/2 | 0 | +5.24% | +2.21% |
| 關稅與供應鏈轉移 | N/A | 0/0 | 0 | N/A | N/A |
| 先進封裝與 CoPoS | 53.75 | 5/7 | 2 | +1.25% | -5.44% |
| AI 伺服器與資料中心 | 9.14 | 2/8 | 6 | -2.79% | -3.03% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價呈負相關；應檢查正負向詞庫，並降低新聞直接提及但股價背離的權重。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-10-03 | -0.35 | 0.13 | +16.67% | 6 |
| 2026-10-04 | -0.12 | 0.70 | +80.00% | 20 |
| 2026-10-05 | -0.16 | 0.29 | +73.33% | 15 |
| 2026-10-06 | -0.72 | -0.75 | +37.50% | 8 |
| 2026-10-07 | 0.48 | 0.61 | +73.33% | 15 |
| 2026-10-08 | 0.13 | 0.40 | +58.33% | 12 |
| 2026-10-09 | -0.03 | 0.37 | +38.89% | 18 |
| 2026-10-10 | -0.28 | -0.96 | +57.14% | 7 |
| 2026-10-11 | 0.66 | -0.74 | +40.00% | 5 |
| 2026-10-12 | -0.08 | -0.07 | +41.67% | 12 |
| 2026-10-13 | -0.05 | -0.03 | +46.67% | 15 |
| 2026-10-14 | 0.08 | -0.29 | +57.14% | 14 |
| 2026-10-15 | -0.08 | 0.08 | +33.33% | 12 |
| 2026-10-16 | -0.13 | -0.25 | +64.00% | 25 |

## 歷史回測摘要

- 回測日期：2026-10-16
- 近5日 3日相關：0.05
- 近5日 5日相關：0.04
- 同向比例：+47.62%
- 權重狀態：未調整

- 方向準確度：+47.62%
- 信心排序準確度：0.05
- 診斷：低相關

調整原因：近 5 日信心分數與股價關係偏低，提高價格確認，降低寬題材推估。；關鍵詞×公司後續樣本有效 4 筆，未達 30 筆，不調整樣本權重

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

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Taiwan Semiconductor Falls 3% Despite Record Quarterly Profit; Intel Drops 4%, AMD Slides 3% - 24/7 Wall St.；台法學者探討台灣半導體產業核心地位釐清5大誤解| 國際 - 中央社 CNA；台灣AI紅利待擴散學者籲拓展半導體上下游布局| 產經 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.53 | -16.84% | N/A | 95.37 | 114.68 | -16.84% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | -0.50 | -3.94% | -5.61% | 2,440.00 | 2,490.00 | -2.01% | 同向 | 86.28 | 28.28 | 511.86B TWD / 54.65% | 2026-10-01 |
| AMD 超微 | 新聞直接提及 | -0.24 | +8.94% | N/A | 562.23 | 570.82 | -1.50% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2303 聯電 | 產業/供應鏈推估 | -0.05 | -8.25% | -10.10% | 133.50 | 164.50 | -18.84% | 同向 | 6.68 | 20.08 | 25.35B TWD / 27.22% | 2026-10-01 |
| NVDA 輝達 | 產業/供應鏈推估 | -0.04 | -1.61% | +8.57% | 217.23 | 228.38 | -4.88% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | -0.04 | -4.09% | N/A | 931.24 | 971.00 | -4.09% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | -0.04 | -6.22% | -13.34% | 1,394.83 | 2,335.00 | -40.26% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -7.02% | -8.85% | 344.33 | 446.77 | -22.93% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「Taiwan Semiconductor」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip, foundry。 方向判斷命中詞：falls。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Taiwan Semiconductor Falls 3% Despite Record Quarterly Profit; Intel Drops 4%, AMD Slides 3% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiywFBVV95cUxNcjYwVnBPdDQ1cFoxUGFiZ3RQeUQ2QktvUU1FUEU5dVJ0cFEtNmhzcXY5V1ZhLXlsQzlkZmlIVlBiYXZLMnJSM19kV1FIc2tBS3pqOXVfY3UxdWRoeE5hdHFMd0ZZek5SXzZjUzFOOFhoSE93SFp4cFFiTUVISE1FX1pGRklTOGw4SF9qbnVCMVZWVDZIUThZWnhWc0g2VnZaMEhGRW50YUlwQmE5QnVHOHBzRG9JSWNLR1JZSDhEZXpNVEpaMHloUXZhQQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 15 Oct 2026 13:08:00 GMT
- [台法學者探討台灣半導體產業核心地位釐清5大誤解| 國際 - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBMbkt4X0FqWGVPbDdQeDFLRFF0THhnS1VQY21RR2gxYk5NMlFSS0t2VWc3Z000RFZULVp3ZFRhUnB0WFpGZk13dUsyOEpJNWl4d29peEpWR0JhWDQ0VXhv?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 15 Oct 2026 10:07:00 GMT
- [台灣AI紅利待擴散學者籲拓展半導體上下游布局| 產經 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE5TaFRoNzBCTXhabG5jMzNONmVRZ1BySk5paW9va25RUHhwbTlIV2xEWUxpWS1DNVd4UzRRZ19MVFRXZ2REZUc2V0pXa0tKVW81RFhkbFowN2Y0S1hOdkE?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 15 Oct 2026 10:36:00 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：INTC, AMD, MU, NVDA: Chip Stocks Tumble Again, Stalling A Nascent Rebound - Stocktwits；Micron & SanDisk Stocks Look Oversold: Time to Buy the Dip? - TradingView；Micron & SanDisk Stocks Look Oversold: Time to Buy the Dip? - Zacks Investment Research

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | -4.09% | N/A | 931.24 | 971.00 | -4.09% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | -6.22% | -13.34% | 1,394.83 | 2,335.00 | -40.26% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | 0.00 | -1.61% | +8.57% | 217.23 | 228.38 | -4.88% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | +8.94% | N/A | 562.23 | 570.82 | -1.50% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | 0.00 | -16.84% | N/A | 95.37 | 114.68 | -16.84% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron、美光」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVDA、NVIDIA」，共 2 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [INTC, AMD, MU, NVDA: Chip Stocks Tumble Again, Stalling A Nascent Rebound - Stocktwits](https://news.google.com/rss/articles/CBMizAFBVV95cUxORHdiV3k3V2RtSVBoRTJaaW5PcTZhQzBTNlRUM2VqcjBpcTViNkREdS1uVGtnb1FYckxkREh4Z00zN2NBSnlNRGZ0SWhpNERydkZKTlJCejRLQ2xqejNxREhfS1ZzSm5CdjhrZzlZTnRiN1Z6M3VtSDU1d2trMG9jVFUwT3hadk93R2l0TlBBZkttekkyTDBHTW1Zc01YTmNzRVJ3Tm11dGcwNktNX04yU0pLUENBQl9sOUI4dVMydW02UUhxZDVXX2pZT0M?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 15 Oct 2026 08:14:12 GMT
- [Micron & SanDisk Stocks Look Oversold: Time to Buy the Dip? - TradingView](https://news.google.com/rss/articles/CBMisAFBVV95cUxPQml5T1RTb2I4Zm93N0NlTGlwaFl3a3FWM010QWlzdkVQaGZMcDVOOGZ3SzFFeEpCR1d1NUZETzZvRVFvQWg1RUJ0Z2E4UkNiRzlMOGl2b01idTVtV2tDS09PTFhwYU1zWVNuZHlDekZDeEFNVTk4dW8xYUNrMlRVRFRvT3ozTXdxX1RONnlYVzRfYkZuT05hZkN5Rk5pcWU3cnJtVzJvREI2RjEyZ3hYYw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 15 Oct 2026 18:13:00 GMT
- [Micron & SanDisk Stocks Look Oversold: Time to Buy the Dip? - Zacks Investment Research](https://news.google.com/rss/articles/CBMinAFBVV95cUxOQXU2NkdtVDB5dDhENk0tVzA5M2NNSUQ1c3pqYTZBWnY3Z2pMUU5NSFhLNFpRVUlfbGVJVUozVm5HNW1mWHdjU0xIVl9iNE9pcXBmR0tnV2VjbXBkNkhWemY0VDUwdTU4Z3dLXzZfU3hjTEEwVHZZMlN3eGwxM05pcjFFc2czZms2VkNpelJXVWdhQzJIUkVsNS1HSEE?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 15 Oct 2026 18:31:34 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報；台灣供應鏈直面AI的供電、散熱與連接挑戰 - TVBS新聞網；上半年賺贏去年整年！成立僅4年的散熱新創 如何打進緯創、輝達供應鏈？ - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | -0.59 | -8.86% | -12.98% | 3,085.00 | 3,435.00 | -10.19% | 同向 | 75.13 | 41.12 | 21.02B TWD / 44.92% | 2026-10-01 |
| NVDA 輝達 | 新聞直接提及 | -0.43 | -1.61% | +8.57% | 217.23 | 228.38 | -4.88% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 3 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：跌停。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 15 Oct 2026 09:50:04 GMT
- [台灣供應鏈直面AI的供電、散熱與連接挑戰 - TVBS新聞網](https://news.google.com/rss/articles/CBMiTkFVX3lxTFBpaXg5ek1CUGd2cF80N0wyM1FPaWpWeFdIckRvb0lLRlVRRUt6MlU4Sm1tTGIybWVMOEdEX1dVNHJvcjBHYWYxOVdiSXA0Zw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 15 Oct 2026 06:01:00 GMT
- [上半年賺贏去年整年！成立僅4年的散熱新創 如何打進緯創、輝達供應鏈？ - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBBSWZ1M1I3clhuSGFJakhid01CMHIwOGpTVzFIQ1ZadHM4bE90ZHBMMW1iNHNManRmbi1MLXdXSk1WVU81dHdhTzJBMEE2UjUxa1otUXpBbVVld9IBX0FVX3lxTE9Ud3llUEIwMmk4TzJISnZCRC1Uc1JxcXNkcTN1azdyZWNOWjh6VVRpcHY4Yy1ZNnB3QUtiMzZxYS0xNXZxTlFXbXdmYjU4QjY1alRJZms0MXhIOUZnUUpN?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 15 Oct 2026 12:37:27 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：台灣供應鏈直面AI的供電、散熱與連接挑戰 - TVBS新聞網；上半年賺贏去年整年！成立僅4年的散熱新創 如何打進緯創、輝達供應鏈？ - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | -8.86% | -12.98% | 3,085.00 | 3,435.00 | -10.19% | 不適用 | 75.13 | 41.12 | 21.02B TWD / 44.92% | 2026-10-01 |
| NVDA 輝達 | 新聞直接提及 | 0.00 | -1.61% | +8.57% | 217.23 | 228.38 | -4.88% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +9.59% | +22.65% | 342.00 | 342.96 | -0.28% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | -2.04% | -4.96% | 239.50 | 289.00 | -17.13% | 不適用 | 15.21 | 15.79 | 1158.63B TWD / 38.42% | 2026-10-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 2 篇新聞命中。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [台灣供應鏈直面AI的供電、散熱與連接挑戰 - TVBS新聞網](https://news.google.com/rss/articles/CBMiTkFVX3lxTFBpaXg5ek1CUGd2cF80N0wyM1FPaWpWeFdIckRvb0lLRlVRRUt6MlU4Sm1tTGIybWVMOEdEX1dVNHJvcjBHYWYxOVdiSXA0Zw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 15 Oct 2026 06:01:00 GMT
- [上半年賺贏去年整年！成立僅4年的散熱新創 如何打進緯創、輝達供應鏈？ - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBBSWZ1M1I3clhuSGFJakhid01CMHIwOGpTVzFIQ1ZadHM4bE90ZHBMMW1iNHNManRmbi1MLXdXSk1WVU81dHdhTzJBMEE2UjUxa1otUXpBbVVld9IBX0FVX3lxTE9Ud3llUEIwMmk4TzJISnZCRC1Uc1JxcXNkcTN1azdyZWNOWjh6VVRpcHY4Yy1ZNnB3QUtiMzZxYS0xNXZxTlFXbXdmYjU4QjY1alRJZms0MXhIOUZnUUpN?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 15 Oct 2026 12:37:27 GMT

## 先進封裝與 CoPoS

摘要：先進封裝與 CoPoS 相關新聞集中在：TSMC CEO Hints Company Could Back Up Customers If Intel’s Advanced Packaging Ramp-Up Falls Short - TradingView；台灣美光先進封裝與測試二廠啟用，深化 AI 時代高頻寬記憶體布局 - TechNews 科技新報；外資指英特爾晶圓代工與先進封裝獲重大突破，取得蘋果、輝達、微軟等廠商訂單 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | -0.52 | -3.94% | -5.61% | 2,440.00 | 2,490.00 | -2.01% | 同向 | 86.28 | 28.28 | 511.86B TWD / 54.65% | 2026-10-01 |
| INTC 英特爾 | 新聞直接提及 | -0.51 | -16.84% | N/A | 95.37 | 114.68 | -16.84% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | -0.43 | -1.61% | +8.57% | 217.23 | 228.38 | -4.88% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 新聞直接提及 | -0.43 | -4.09% | N/A | 931.24 | 971.00 | -4.09% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 新聞直接提及 | -0.21 | +19.81% | +9.64% | 539.44 | 539.44 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 新聞直接提及 | -0.21 | +9.59% | +22.65% | 342.00 | 342.96 | -0.28% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.12 | -11.68% | -8.06% | 673.00 | 747.00 | -9.91% | 同向 | 13.92 | 48.70 | 88.13B TWD / 45.52% | 2026-10-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「TSMC」，共 1 篇新聞命中。 同時符合主題標籤：advanced packaging, CoWoS, CoPoS, FOPLP。 方向判斷命中詞：falls。
- INTC：新聞直接提及「Intel、英特爾」，共 2 篇新聞命中。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [TSMC CEO Hints Company Could Back Up Customers If Intel’s Advanced Packaging Ramp-Up Falls Short - TradingView](https://news.google.com/rss/articles/CBMi7gFBVV95cUxOdEJaLXBOUkZxT1NDb184QWZyTEU5VnVfajZyelhpNzR1eDgwdFR4TE82N2I0N2Zrcm9VY09ORE1LWGNsdXpvOXJJT21LdXZHRkN2SFZ2VnVZUkdLcnN2cHdOX0xEQ0R0dEhmdTdGUG1HM3oycjZuZ2xTdUlNWXduU2Zuenp4WTlCS1Rhdy1TZHluVmVJLWtiWndZd0hGNFQ0ZUlIWmhBVzJjLWo3WXgxMGRpZWJxUWYzVUh3X2poOE5oVENqQjQyOWpnOE5RaERSMUhNX3RrRDJEVFdaeWZzSmFsZGxsTDlMTUJ5cGZn?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 15 Oct 2026 15:19:11 GMT
- [台灣美光先進封裝與測試二廠啟用，深化 AI 時代高頻寬記憶體布局 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiqAFBVV95cUxNMGtZM3NVT2dVVXBvbG11SEtNbDdwYVhkRVM3Wk9oc2p6ZEhjSVRYNlJvczVNUmxjNi1UazdNWk4tQ09Bb0ktMVdBZWF1cFNIZHJfQ2xLOTA5MjJJSUV4c1MyUGQ4SDZBQnRNTmVRSzFyemE5SUhhYVlsTG03LUx1WC16VlBwOER2ZUJsejJoemxSZ0VlVm9BQzBYOXFxdkk4YTB1am10cDU?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 15 Oct 2026 23:55:13 GMT
- [外資指英特爾晶圓代工與先進封裝獲重大突破，取得蘋果、輝達、微軟等廠商訂單 - TechNews 科技新報](https://news.google.com/rss/articles/CBMizgFBVV95cUxQZlNkdmNwRU1tUEtuNk1yRmZxRUp4aXg1ZmZrU0M3al81a1hFcnAta3BBMzJyQjBRTWxMZlZ0b2E2SXduTlltNGJGS0VUSEM3WjdSXzJ3alNSM0otZ09ycWhISGtRU000WWRtVF9BQTk4ZlZVeHQxWk1qb1dlSUVIUDBrcGYyWERFUWM1X2xrd3ljaVdzM1d4RTItcXo3TlNlc1hVbUU0Vl8yVXBUUHpVV0VScm1vNmJNOGpfVldVa0xCaXlSX2FGYzU0aldPdw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 15 Oct 2026 23:21:12 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel Stock And 2 AI Infrastructure Plays For Data Center Growth - Simply Wall Street；新加坡也受益 AI 熱潮，經濟成長率僅次台灣 - TechNews 科技新報；CNN, Axios and other publishers join Google's AI news program - Reuters

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.28 | -16.84% | N/A | 95.37 | 114.68 | -16.84% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.03 | -1.61% | +8.57% | 217.23 | 228.38 | -4.88% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.06 | +8.94% | N/A | 562.23 | 570.82 | -1.50% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.03 | -3.94% | -5.61% | 2,440.00 | 2,490.00 | -2.01% | 背離 | 86.28 | 28.28 | 511.86B TWD / 54.65% | 2026-10-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | +19.81% | +9.64% | 539.44 | 539.44 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -7.02% | -8.85% | 344.33 | 446.77 | -22.93% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.02 | -11.68% | -8.06% | 673.00 | 747.00 | -9.91% | 背離 | 13.92 | 48.70 | 88.13B TWD / 45.52% | 2026-10-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.02 | -9.95% | -13.86% | 4,165.00 | 4,920.00 | -15.35% | 背離 | 60.69 | 68.79 | 55.40B TWD / 1.97% | 2026-10-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：growth, 成長。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：growth, 成長。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：growth, 成長。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Stock And 2 AI Infrastructure Plays For Data Center Growth - Simply Wall Street](https://news.google.com/rss/articles/CBMizAFBVV95cUxOYWRVMDlUVkxGYnZuM2wzZEl1ZkJXQm5BTU5abmZrLTM5YUtEOEpLUFBUTzBobk9WU2twb0pCWDBxeEdESHlXSE9rbDhmQUxBWi1zZFphbUdDU2RCZHF0V3NqSWFUN0hPOW4wajdOMlRRa3FjbFUwcW0yVmYzbDFia3lCTG9BbnVWSHo1RWVmZlhYeHVtWDJnZGNxVWpXODlwSVJRamZFbE9ta0RYam1xV0lkUm9GOW5qT0VweDNheU9mdTZpekw3Yml5RFLSAdIBQVVfeXFMUHBoWnVtaWhQdTVLRE1laVJxTFlOYjlWd3lETmJBSzFkVlhBUGx0REJCX0ZzVE5RdDBId0NXRmhtanBubHFPYW5sZVFOVVREeXoxOWFlU0xtZFhxeC1UYjZwN0tvY0x5TEN0TkdkUlFpTnUyWjllVHBtTkxMLUJKOWpmZHBYTENEc1M4Z2dwNWtvWUFYREthMlJsSG5SbWpzQmg5YjdyRXpFbGJXSDZKWW00c2hGcE0xMURCZk5Oa0ZfZ1l2MWdvRjJ0NGcwdS1QbFhn?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 15 Oct 2026 16:08:04 GMT
- [新加坡也受益 AI 熱潮，經濟成長率僅次台灣 - TechNews 科技新報](https://news.google.com/rss/articles/CBMi5AFBVV95cUxORnZpYVM4Nm8tZ3ladkxIN0J3TTdRVXhGQTdYa2Jzb1d2cDh1a3RxRy02YXpGRXpPMnJDbHBVcmxBS0xKNXJPek9zZ2J0SHJGeVpJTU1KQTVXVFd0cm0tRjgtZzdpNDhRZWpkTFVod2hDRXBuQXlrOGZwRF80MmtJaDJGUEVLd21ZYkQ3Q1RFVlR4Tm9uMXREYmUtb3k1YVdlelRTemhGQ1hiRlZ1TDZvZTVzbkVXRGFtQW8yYlA0QVNYM3hiSGVEYVV4V29QenJHdUgxNXNFeGRXWDRIczJhMGhwSWQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 15 Oct 2026 17:28:17 GMT
- [CNN, Axios and other publishers join Google's AI news program - Reuters](https://news.google.com/rss/articles/CBMiqgFBVV95cUxOZnM2QWR6ZVFBcTRKb1MxbGgwXzBYMkt5aldWd2Q0UHRBbklWZTBYQVdEeFE4QnRDY09rR1hnX1BSam41NVRRS0d6dTdaSkU3c3NsbFMyYS1sN1pqRnA1dl94bXRxdk01WTJaNnFWVVJzRk5xUjdTRDBocnlzbkVxZWdNaUwxRExrU1RrVkd3ZXJpM3djTVFBSGZZRE0wRWVKaHpGRER4d2hXUQ?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 15 Oct 2026 19:31:47 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股狂瀉1,800點...月線失守後還會跌？分析師曝關鍵是「這個」 - 經濟日報；台股操作...盯六大指標 - 經濟日報；台股外資大提款 賣超3,025億 史上最多 | 市場焦點 | 證券 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股狂瀉1,800點...月線失守後還會跌？分析師曝關鍵是「這個」 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9tdHFyR0pQdU1aN2ZVODUzZXlEMnA0QXludHNCRG4ydkF3b3lLdUFxREgybk1NZVpWdklDdDhZRTRSVDFlamxHRkxzRnhHZkpRYmNyN2F6dXoyd9IBX0FVX3lxTE1nUE9sXzBveXR0SVVUSE1hME5fYk5hUWszcEtEdTVVR0JxdEtDOWNLN0lrZGdYb2htNDJEY1lWRDlZa1BxdGVKTFhXY3ZvZXFPVE5JTmt6cnFJUUhEOGVV?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 15 Oct 2026 04:17:49 GMT
- [台股操作...盯六大指標 - 經濟日報](https://news.google.com/rss/articles/CBMifEFVX3lxTE55OWZ1SUg2WWZOS1d5Vkc5ZmZXVG5SeVZ4YUxpcG93V3EzaHhJVTNuaEhFSDcwZjFIamRoLUlVdE5zallXQnpvV253Z25MQzBHdUFWenlKaXJJYVg3dkx2WUxqMDU0b0cxNDFvQ3R3OTlmeHd5Q3k0RWF6SELSAV9BVV95cUxNQmxhWmJhODNuRWQzdXlRZkdNMERiNzhwMW1GSWFBcHRNVnBoOE1oU1ZBcDV4U0hXS2lqbE91dTB5c0VOS0wtYVpSRV9QQnMxVWpCYWNtMmxxRl8wNktLZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 15 Oct 2026 19:09:17 GMT
- [台股外資大提款 賣超3,025億 史上最多 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9pUUg0TllFX3FuLUg0TTFzOTJfeGNxQ2pSSHVkU0xJMV9HeERqczRaaVB0QkhVODFkNnJVN2hXUUx6SkxSb0plbEhsWXQ2ODJXXzdFQTlXTzl2QQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 15 Oct 2026 19:24:11 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》外資賣超3025億 重挫1655點/失守47K - MoneyDJ；台股重挫 台幣重貶1.92角、爆70億美元天量 - MoneyDJ；312億元台股ETF股利今發放00919配發金額最多- 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》外資賣超3025億 重挫1655點/失守47K - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNNGZFcjY0UGg3WDN1YWRmVm9kSDNNOEo3eHYxNE4wV0NRRjFEUU9QbmJyZF9uRXpjSEp1TWtVTFhtd09raW9IMWZ3eGNYSUtNRm1jUmt3MU8zN052VlhVQV9tMjMxLVh0dGprOWRDY0xNZlZvT19HSnk3Q05UWW10R1ZaLUc2TGhNSk5EZFk1aHV2QQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 15 Oct 2026 07:46:00 GMT
- [台股重挫 台幣重貶1.92角、爆70億美元天量 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxOWFNycm1KV1I2R0lzSGI3V1JvZ0tpU1JjUmtzUFFTU01XeGdYelU1ZERPcG92VjdNdnc2N0pZdThkcXdHNy1weFptRlBGRFNoU1hQUC00eEVmOTFZcmozb0hPeFh0S1B4NldKekNUcUlPTGFuZ1Y5Rmlsa2hERC1OVnJYcUppRW9LYWZGVjItaEY?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 15 Oct 2026 09:32:00 GMT
- [312億元台股ETF股利今發放00919配發金額最多- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQM0xQeVh2TVFTZzNSSlByblFialEwUjBjeFZESVhzUG5idTR1dERnYXNCNW1YU0dLY3YwNm1tMTN4RlliRnE0ZlZXX0pQT2RjVkRHWFc1Nk1GTUtZd0ZHeGdkcndXOVQ3NW9uQTI1ODdaLUJ2UmVoTmZKdUhRbHB4dkZ3RUVjbUlPQ1R5bUx1Y2lGQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 15 Oct 2026 02:43:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
