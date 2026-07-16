# 每日股市熱門話題分析 - 2026-07-17

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜正向｜熱度 10｜市場確認 100.00｜同向 1/1
2. **新興題材：台積電法說**｜正向｜熱度 3｜市場確認 73.69｜同向 1/1
3. **新興題材：UnitedHealth**｜正向｜熱度 2｜市場確認 73.69｜同向 1/1
4. **半導體與晶片供應鏈**｜負向｜熱度 7｜市場確認 58.92｜同向 3/5
5. **AI 伺服器與資料中心**｜負向｜熱度 11｜市場確認 43.04｜同向 3/6

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.36（樣本 15）
- 5日相關係數：0.02（樣本 15）
- 同向比例：9/15

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 100.00 | 1/1 | 0 | +15.70% | +24.06% |
| 新興題材：台積電法說 | 73.69 | 1/1 | 0 | +1.23% | +0.20% |
| 新興題材：UnitedHealth | 73.69 | 1/1 | 0 | +1.23% | +0.20% |
| 半導體與晶片供應鏈 | 58.92 | 3/5 | 2 | +5.64% | -2.84% |
| AI 伺服器與資料中心 | 43.04 | 3/6 | 3 | +2.68% | -3.50% |
| 綜合市場情緒 | 0.00 | 0/1 | 1 | -1.23% | -0.20% |
| 新興題材：半下挫台股聚焦台積電法說 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-07-04 | -0.22 | -0.36 | +22.22% | 18 |
| 2026-07-05 | -0.00 | 0.24 | +40.00% | 10 |
| 2026-07-06 | N/A | N/A | 0.00% | 2 |
| 2026-07-07 | N/A | N/A | 0.00% | 1 |
| 2026-07-08 | -0.05 | -0.05 | +71.43% | 14 |
| 2026-07-09 | -0.11 | -0.36 | +64.29% | 14 |
| 2026-07-10 | 0.55 | 0.05 | +77.78% | 9 |
| 2026-07-11 | 0.13 | -0.08 | +50.00% | 12 |
| 2026-07-12 | 0.27 | 0.13 | +16.67% | 12 |
| 2026-07-13 | 0.39 | -0.09 | +15.38% | 13 |
| 2026-07-14 | 0.10 | -0.07 | +21.43% | 14 |
| 2026-07-15 | 0.20 | -0.16 | +28.57% | 7 |
| 2026-07-16 | 0.20 | 0.02 | +33.33% | 12 |
| 2026-07-17 | 0.36 | 0.02 | +60.00% | 15 |

## 歷史回測摘要

- 回測日期：2026-07-17
- 近5日 3日相關：-0.10
- 近5日 5日相關：-0.18
- 同向比例：+57.14%
- 權重狀態：未調整

- 方向準確度：+57.14%
- 信心排序準確度：-0.10
- 診斷：低相關

調整原因：近 5 日有效樣本 14 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits；If the AI Boom Is So Strong, Why Are Memory Stocks Crashing? - Yahoo Finance；SNDK vs. MU: Which AI Memory Stock is a Smarter Buy at Current Levels? - Zacks Investment Research

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.50 | N/A | N/A | 853.20 | 971.00 | -12.13% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.50 | -15.70% | -24.06% | 1,411.08 | 2,335.00 | -39.57% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.37 | N/A | N/A | 500.94 | 529.14 | -5.33% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.37 | N/A | N/A | 96.98 | 114.68 | -15.43% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -1.77% | +18.92% | 207.40 | 212.50 | -2.40% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、memory、Micron」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：fall, weak, rally, strong, 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK、SanDisk」，共 4 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：fall, weak, strong。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits](https://news.google.com/rss/articles/CBMi0AFBVV95cUxOWm5KdEIwSXpyY191UEhDa1V6NVpWa01UbmpJeWRIV0ttT080TmpDNEhISW5TWkQwUzBVYzBqSHJPWXRVNVJCampoWWRlYmhKVkhIeHBJLS0wLW5Ua09GQnRORXpFcW5qTEJkcnJGcW55aU5rOFVOLUFMbjRPZEpWT3A2ZllucnM0SU9JNEdrNUwyc3V2WHAtNFk3VHl4R1F6SkZRMFpleEE2Zl9MdW4tSEpMMnFGZ2hQZURWQ3B1WDlPR1BhRjJELVN5ODJWYVR3?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 15 Jul 2026 13:47:30 GMT
- [If the AI Boom Is So Strong, Why Are Memory Stocks Crashing? - Yahoo Finance](https://news.google.com/rss/articles/CBMilAFBVV95cUxOblY5TmhGN2UyNmdzN05YZUVjU1VDY0ZwSzhNdTg5QXdvR1lBd1hLbUFKMXdZVnlIZHBoVWFOTnFiZ3BYcm5ibDJkbHk2WWxIY3RaWnZZcE1QVEdJV2Iwa1V6a2RMRmJjTXR0dlp3ZU82UlF0MHhmNjFOOEtHUThUdm5ieGtjc1NaTUJqUTVYSTEtaFJQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 16 Jul 2026 15:14:17 GMT
- [SNDK vs. MU: Which AI Memory Stock is a Smarter Buy at Current Levels? - Zacks Investment Research](https://news.google.com/rss/articles/CBMirAFBVV95cUxQdmJOT2JiT3hSNkRGTkNycW5IUHlBVWRGalZvbmtUTlZMNHFLTE9zeW9nV2NoMm1kM0EyRmhzRmZEdWptbk0tVHNabG1vSDhvNy1oUlg2ZGl0Y3htOS0yTkxIVHhZdVdRVjdrcmlZa2tGZ0VTZVRyaHJndGdXMmZ1UFVSUVYxU29EWVdhM192T1BoeHluSDZjYVk3Q2VONEpHTVowbVNmczRudE9n?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 16 Jul 2026 13:22:02 GMT

## 新興題材：台積電法說

摘要：新興題材：台積電法說 相關新聞集中在：台積電法說會激勵股價收高30元 台股大盤拉長下影線跌6點、收45,624點 - 經濟日報；〈台積電法說〉Q3美元營收季增12%再攀峰 上調全年營收年增至逾4成 - news.cnyes.com；〈台積電法說〉Q2雙率再超標、EPS 27.25元同創高 上半年大賺近5個股本 - news.cnyes.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | +0.58 | +1.23% | +0.20% | 2,470.00 | 2,470.00 | 0.00% | 同向 | 74.39 | 33.21 | 442.68B TWD / 67.87% | 2026-07-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 3 篇新聞命中。 方向判斷命中詞：創高。

### 主要來源

- [台積電法說會激勵股價收高30元 台股大盤拉長下影線跌6點、收45,624點 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9VTV9PWnBiVXBNRFdiSC1xeWJIWFZwa01QcXVIRW81dWJTOVB0c3MwdXZ0bkJiTTk0X1Z2SW1RMWdzUE51Ml8tQXVWbWNrcHdkaFo0ZDU0ZDVMd9IBX0FVX3lxTE9NYzAxNUlwZ1Y5TGN4RTdvaWhZdmt4NUE4Umk3dVp4Q2FPbkhzTnJ0cFFMLXk3dW43bl9GeGc1MGZlQ3ZtZXpPNUxWSGhwR1NhamNNVkNyeDkyTmxEMGNz?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 15 Jul 2026 09:00:00 GMT
- [〈台積電法說〉Q3美元營收季增12%再攀峰 上調全年營收年增至逾4成 - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTE5jX0dmb2wyM3luNVEtVkNGbnRldEhUOW1yZ2xma3Z2aGpBdWJoeU1DSEY0dHg5dURrdlNERTVnQU14bGdkX2N5c3c1WGRVMFU?oc=5) - Google News source discovery | 鉅亨網 Thu, 16 Jul 2026 06:39:56 GMT
- [〈台積電法說〉Q2雙率再超標、EPS 27.25元同創高 上半年大賺近5個股本 - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTE5oSGpMa2tDQ2dPa2VCNjFmS2hLS0pnQ2VRc0pKYjZfY0E1SmdxRXZaX193NlBsaHZoZWZHVHZBempVUGRGQTY5cEV4VnlTbG8?oc=5) - Google News source discovery | 鉅亨網 Thu, 16 Jul 2026 05:53:19 GMT

## 新興題材：UnitedHealth

摘要：新興題材：UnitedHealth 相關新聞集中在：UnitedHealth regains earnings momentum, shares surge - Reuters；Stocks making the biggest moves midday: Manpower, Abbott, UnitedHealth, TSMC & more - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | +0.43 | +1.23% | +0.20% | 2,470.00 | 2,470.00 | 0.00% | 同向 | 74.39 | 33.21 | 442.68B TWD / 67.87% | 2026-07-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「TSMC」，共 1 篇新聞命中。

### 主要來源

- [UnitedHealth regains earnings momentum, shares surge - Reuters](https://news.google.com/rss/articles/CBMisgFBVV95cUxNcjdKdHAtZk5PZF92ZEdIRVBWa3lBbmZOeU9DaWkwZENUdjI2YThzMVUzQnpOSzhjZmpvWl96Xy1QZG1VM05ZeW5NNFdfZDRaQktUc3QxeGwzR2dHYTRCb001Q0pfT01FdVp3ZVJsTXctQ3FUZWlISl95UktmLVR0NTQ4UUtwMDdTdnlYU2hib3M4NzdwMVNTczV1T1NLZWVGbjRDWjE2djlZQXliNWlGak9n?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 16 Jul 2026 14:22:24 GMT
- [Stocks making the biggest moves midday: Manpower, Abbott, UnitedHealth, TSMC & more - CNBC](https://news.google.com/rss/articles/CBMinAFBVV95cUxPaUJKazRxOGhsbTJBaDB2ZkhVa2k1cDFIdTZtc1hnMWNNbjJRRzFRSmxyNkM1SFRMdVVDSlMyT1hrQW9BN09Qd3BPTXl3LXlmOEZyNmsxaFFETVB0eTVYRGsyNVd2bzlVeUpRcURIQjBBSC04aU1XQlB4TkNDMS1XR0hjeXRfbGpZNzczTG92NUZrYjZ5VktfOUNoeXY?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 16 Jul 2026 16:03:48 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：What Triggered the Recent Semiconductor Sell-Off - Kavout | AI；The Chip-Stock Slide Isn’t Over. The AI Trade Is Still Under Pressure. But ‘No One Is Short’ - Investopedia；臺師大團隊登《Nature》：首度量測二維半導體電子轉移長度 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | -0.26 | +1.23% | +0.20% | 2,470.00 | 2,470.00 | 0.00% | 背離 | 74.39 | 33.21 | 442.68B TWD / 67.87% | 2026-07-01 |
| INTC 英特爾 | 產業/供應鏈推估 | -0.08 | N/A | N/A | 96.98 | 114.68 | -15.43% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2303 聯電 | 產業/供應鏈推估 | -0.03 | +4.23% | -1.84% | 160.00 | 166.00 | -3.61% | 背離 | 4.00 | 40.20 | 23.12B TWD / 22.85% | 2026-07-01 |
| NVDA 輝達 | 產業/供應鏈推估 | -0.04 | -1.77% | +18.92% | 207.40 | 212.50 | -2.40% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | -0.04 | N/A | N/A | 500.94 | 529.14 | -5.33% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | -0.04 | N/A | N/A | 853.20 | 971.00 | -12.13% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | -0.04 | -15.70% | -24.06% | 1,411.08 | 2,335.00 | -39.57% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -16.19% | +20.98% | 374.45 | 446.77 | -16.19% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip, foundry。 方向判斷命中詞：lower, pressure。
- INTC：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 CPU, server CPU, x86, foundry；其中 3 篇新聞出現相關標籤。 方向判斷命中詞：lower, pressure。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 3 篇新聞出現相關標籤。 方向判斷命中詞：lower, pressure。

### 主要來源

- [What Triggered the Recent Semiconductor Sell-Off - Kavout | AI](https://news.google.com/rss/articles/CBMiiwFBVV95cUxQeV9hbWl4LXg0eW5ZWFVERlpaZGRsZzBkOEQzb0VuSmptQ2RsR3RUcldSTzhJcW1URGZsbnBjVUxmYlNpMHlESnlJdEVvZ1RaSWloQ0ZfODJXV012UF9qYjFfYVNDaG15cXpBNXYxYWpjaGNIY2hRa3hOdGhUSjdOcDhabENFWmFvV1M0?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 16 Jul 2026 16:37:41 GMT
- [The Chip-Stock Slide Isn’t Over. The AI Trade Is Still Under Pressure. But ‘No One Is Short’ - Investopedia](https://news.google.com/rss/articles/CBMirgFBVV95cUxOYnhlZUVNVnQwdnoxQWRwbkNwam5sWG4yTHdqWnhiOHRySlpzNlNFODlKNkkzOWJVeFlGcS05cVFuVkNJVFlNQlVHZzNHUjNibEtNeDVGTTRVb0Z0c2JKenVRUGc4MjlpNUxQSDNJMEpmSTdLeDdmLXRLNlBPeGZhek9DcTZoZkw1dVdsS2RsWFNEMXFWeEpMajRVQjFmOUZCSU5pNENjX2FjZlJIRUE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 16 Jul 2026 15:43:33 GMT
- [臺師大團隊登《Nature》：首度量測二維半導體電子轉移長度 - 中央社 CNA](https://news.google.com/rss/articles/CBMiVkFVX3lxTFBLaGFIZzgxRlJuTVFaQnVtbHROR2h3aWhjY3RuT01ZYjUtUkJDaFp3WnlGaHVlejIxS194N3UtT0dqbHJ2Y05IWVJjSGNQWGJxQnYtLXBn?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 16 Jul 2026 07:29:25 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：What Triggered the Recent Semiconductor Sell-Off - Kavout | AI；Marvell Drops 8% as AI Capex Slowdown Fears Weigh on Chips; Broadcom, AMD, and Intel Slide - 24/7 Wall St.；The Chip-Stock Slide Isn’t Over. The AI Trade Is Still Under Pressure. But ‘No One Is Short’ - Investopedia

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.59 | N/A | N/A | 96.98 | 114.68 | -15.43% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.54 | N/A | N/A | 500.94 | 529.14 | -5.33% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | -0.51 | -16.19% | +20.98% | 374.45 | 446.77 | -16.19% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | -0.06 | -1.77% | +18.92% | 207.40 | 212.50 | -2.40% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.03 | +1.23% | +0.20% | 2,470.00 | 2,470.00 | 0.00% | 背離 | 74.39 | 33.21 | 442.68B TWD / 67.87% | 2026-07-01 |
| MSFT 微軟 | 產業/供應鏈推估 | -0.02 | +2.13% | -20.84% | 401.10 | 506.69 | -20.84% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.02 | +1.79% | +9.12% | 682.00 | 683.00 | -0.15% | 背離 | 10.86 | 63.32 | 65.78B TWD / 32.86% | 2026-07-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.04 | -3.27% | -7.38% | 3,700.00 | 4,310.00 | -14.15% | 同向 | 62.91 | 58.96 | 58.01B TWD / 2.80% | 2026-07-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel、INTC」，共 2 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：falls, pressure, slowdown。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。 方向判斷命中詞：falls, pressure, slowdown。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AVGO：新聞直接提及「Broadcom」，共 1 篇新聞命中。 同時符合主題標籤：AI, datacenter。 方向判斷命中詞：falls, pressure, slowdown。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [What Triggered the Recent Semiconductor Sell-Off - Kavout | AI](https://news.google.com/rss/articles/CBMiiwFBVV95cUxQeV9hbWl4LXg0eW5ZWFVERlpaZGRsZzBkOEQzb0VuSmptQ2RsR3RUcldSTzhJcW1URGZsbnBjVUxmYlNpMHlESnlJdEVvZ1RaSWloQ0ZfODJXV012UF9qYjFfYVNDaG15cXpBNXYxYWpjaGNIY2hRa3hOdGhUSjdOcDhabENFWmFvV1M0?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 16 Jul 2026 16:37:41 GMT
- [Marvell Drops 8% as AI Capex Slowdown Fears Weigh on Chips; Broadcom, AMD, and Intel Slide - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiygFBVV95cUxPWXQ1azRhRXU2WGEtTjBNbG5ZMDIyN1JkdWhTdmhfWTJ4aENuUkpWREdOelZCTllxdUxNS2V1MzlaSUVwTmJRSy1VTWxyWF9kOWQyTXFzZ0tmSWgxTkZqTFdQXzI1cEJuelJzNl9xTzVIM05odjdmUmpDSGZrMlBLWHBGcFdLZ2ZPQ3RpOGczZVlRRHVyZlljRnJ5ZlhKc0ZqTjFSeTRzbVlVYTFpenlxc0VhQW1EUExyMnlqd2pMR3pLazc2MnRnN1RB?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 16 Jul 2026 16:12:07 GMT
- [The Chip-Stock Slide Isn’t Over. The AI Trade Is Still Under Pressure. But ‘No One Is Short’ - Investopedia](https://news.google.com/rss/articles/CBMirgFBVV95cUxOYnhlZUVNVnQwdnoxQWRwbkNwam5sWG4yTHdqWnhiOHRySlpzNlNFODlKNkkzOWJVeFlGcS05cVFuVkNJVFlNQlVHZzNHUjNibEtNeDVGTTRVb0Z0c2JKenVRUGc4MjlpNUxQSDNJMEpmSTdLeDdmLXRLNlBPeGZhek9DcTZoZkw1dVdsS2RsWFNEMXFWeEpMajRVQjFmOUZCSU5pNENjX2FjZlJIRUE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 16 Jul 2026 15:43:33 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：三大法人轉賣超431億元！台積電神救援 台股跌點從660點收斂至6點 - 經濟日報；台股基金 年輕世代搶買 - 經濟日報；台股外資連十賣 累計達4,534億 台指期盤後一度跌逾千點 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | -0.21 | +1.23% | +0.20% | 2,470.00 | 2,470.00 | 0.00% | 背離 | 74.39 | 33.21 | 442.68B TWD / 67.87% | 2026-07-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。

### 主要來源

- [三大法人轉賣超431億元！台積電神救援 台股跌點從660點收斂至6點 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9uRUNiektyb1o3TTU2X2otV01HNVhsdnFPaDNSQVFublJBelE5d093UE16cF9xaXptM2N3bnUzVTR3UG5Pb3BhZXJ1cHdJRGoxTERvTjIycTR6Z9IBX0FVX3lxTE1ZdGlmaXFPNWl2WE9RcnpzQVVqTXRYeXdIRjM5UldnWTlCbEl3RUlDWktKNldOcHBsdGx5RnpqNE9nSGdVbHpNaFJrdTZjaEFDUGNMVzg4U2tWa1BYeDE4?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 15 Jul 2026 09:00:00 GMT
- [台股基金 年輕世代搶買 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxOSE92R2lvbUFucXBMN2stbXEyR2JXUkltVm1kaHV6VFpyQlg3SktJV2VDMm14blh2UThhVDFrVWV2ZVVfbGdXMS1GSVNOSnJZeFRjYjlNdVI0TDNPbzBWbFlyamZ0S3VSclJfRGU2M21DMS1nYWxrLXRoRDNFQVZNSdIBX0FVX3lxTE5wclMxVFlCUGtjdmtxYTZpWnIzM19adFl4WjdSNTJwaDNLRTlJeDN5OTdtMTNVQXNoNXAyTXFJX0Y2bW1VaTlKWW12RzJuZzBhV1lHbTVQUFhieFRxcWNV?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 16 Jul 2026 18:32:47 GMT
- [台股外資連十賣 累計達4,534億 台指期盤後一度跌逾千點 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1GbC1Uc2x4MnlydE92MzN0aThOeXhBS21SZXpfNFUyMFAxMDJIYWtBNElCbEE4VWR2RkdCZnFPTWFhdFZZTWZVSUUtSlBEa0FXUHp3LWdsVEpEQdIBX0FVX3lxTFBkODF3bjkwQ1JlR29aejRDTzJEOGJ6SnpXVHVLVmQ2bDd5VWxxeUVRYy1tMU1hbEhheDJsangzQlJwQ2QxZlBVQ1JPbDFwUHptcTJ3UFZPU24yTE9sdXNJ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 16 Jul 2026 17:45:45 GMT

## 新興題材：半下挫台股聚焦台積電法說

摘要：新興題材：半下挫台股聚焦台積電法說 相關新聞集中在：美股3大指數上揚費半下挫台股聚焦台積電法說會| 證券 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | 0.00 | +1.23% | +0.20% | 2,470.00 | 2,470.00 | 0.00% | 不適用 | 74.39 | 33.21 | 442.68B TWD / 67.87% | 2026-07-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。

### 主要來源

- [美股3大指數上揚費半下挫台股聚焦台積電法說會| 證券 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE9zel9IaU5CZmUyeGFqeUZ0Y0xDUUZCc1NTMUJFZ3NRMTZCc2RFN2FlUkhCZzVVVzVDMkt1eUFyeXV5VzlONlpxRTNOOVlNaWFJTk9jNVh3SjE1RjVZNmc?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 16 Jul 2026 00:33:00 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：【台股操盤人筆記】戰事震盪反而創造布局機會 - MoneyDJ；‧永豐期貨盤後分析 - MoneyDJ；個股動態報導內容-01772A61-996A-43F0-ACB0-983392958BA7 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [【台股操盤人筆記】戰事震盪反而創造布局機會 - MoneyDJ](https://news.google.com/rss/articles/CBMilwFBVV95cUxOSUFhZzRhZTd6OWY2RVZnWkV5QzhJTkY2SVVnbWZoeGdHY0Z3b18wQTU3WXEtMWVucnVjak1sNWJRRm9SeXQ1bDlMcGVJcmlKb24wT3U2Y1lDYVJZYVZRYmVhbHlXS1JOZkFacE04cFYzV19nd2R6dGsxaVdOd0gzSGJralItVVFSWmdOT1dKbVBfNHRkWEMw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 16 Jul 2026 07:20:00 GMT
- [‧永豐期貨盤後分析 - MoneyDJ](https://news.google.com/rss/articles/CBMijgFBVV95cUxOU2dXNXhqOVE3Y2tnTTBHdXIzbndQcDNoRzNOUVgzVUtOcmk3MmtQVG4ybFRpWnFjUGM1b3RkSTdySlozX2dQU01JQXlFb2hiTHpqV00wM3R6ZkxBcEYxUE0zSGh3MW9raGREZE9HY3FaTURGRUs2U1V0SFZ2UUx3UzF2VFBIQ3F4WFphejhB?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 16 Jul 2026 08:12:22 GMT
- [個股動態報導內容-01772A61-996A-43F0-ACB0-983392958BA7 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxQYXRFdUI4Zml4d0JhSUVKTHJlckFVWTUwUTVpX2ZlTkRXQlpTSUlQS2p0aDRDcVdvYURMYjE0cG95dWpubEQwLXBYMWFpZEJ5bW5UU3J5RWg1SW1YZFRuMDd0ZVd2Vk94WHVrSEVkeHE0cHdUYXBSWHdOYUdIeTNNcmFHNG5JdFpfMElTdjBRWXRETjgz?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 16 Jul 2026 11:29:24 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
