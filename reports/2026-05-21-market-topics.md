# 每日股市熱門話題分析 - 2026-05-21

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜中性｜熱度 6｜市場確認 N/A｜同向 0/0
2. **半導體與晶片供應鏈**｜正向｜熱度 9｜市場確認 58.00｜同向 2/5
3. **新興題材：OpenAI**｜中性｜熱度 5｜市場確認 N/A｜同向 0/0
4. **AI 伺服器與資料中心**｜正向｜熱度 8｜市場確認 55.28｜同向 3/6
5. **關稅與供應鏈轉移**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.28（樣本 11）
- 5日相關係數：0.52（樣本 11）
- 同向比例：5/11

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | 58.00 | 2/5 | 3 | +11.34% | +9.48% |
| 新興題材：OpenAI | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 55.28 | 3/6 | 3 | +6.76% | +11.71% |
| 關稅與供應鏈轉移 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：輝達Q1財報營收 | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。

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
| 2026-05-20 | 0.36 | 0.35 | +28.57% | 7 |
| 2026-05-21 | 0.28 | 0.52 | +45.45% | 11 |

## 歷史回測摘要

- 回測日期：2026-05-21
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

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Intel, AMD, Micron shares climb ahead of Nvidia earnings - Latest news from Azerbaijan；Micron Is Up 6% Today: Is It Outperforming Other Memory Stocks Like SanDisk and Western Digital? - 24/7 Wall St.；Micron (MU) and SanDisk (SNDK) – Why a Top Analyst Boosted Price Targets on These AI Stocks - TipRanks

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 731.99 | 731.99 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | -1.07% | -3.78% | 1,392.56 | 1,562.34 | -10.87% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +28.14% | +16.92% | 223.47 | 223.47 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | N/A | N/A | 447.58 | 447.58 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 118.96 | 118.96 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、MU、memory」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk、SNDK」，共 4 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel, AMD, Micron shares climb ahead of Nvidia earnings - Latest news from Azerbaijan](https://news.google.com/rss/articles/CBMiggFBVV95cUxQTzdHTzc3UjhqNUpoZkYyV3M0TzVLZk9QZDVWSWhKd3hVQng3TXN5MzdfRnJSSkx2QmlzWVZhZjZVVTF2aEJIWDEwRS1vX21KeHRLdkdlWmFxNmEzalNPMXlqc1YzZWZfV2dZbDktWXFyQ3plTFIxQnk4Z21STklFTmhB?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 20 May 2026 12:08:34 GMT
- [Micron Is Up 6% Today: Is It Outperforming Other Memory Stocks Like SanDisk and Western Digital? - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi0wFBVV95cUxNUlZhQy05U3k1YmxlSVJDNmNaemFpdDAtSE8xOF91U1oxUFMxRHNDZU9Leks4blNuM3ZTSmxPTkktbGdJaXBSNlVkWkdZN3VGaDJtcXA5TUVQYUUwMjJqeXJjTnptVmRuSmNVOFpQaHF3bU9EMldCVTJkLWhnMTZwUUw4TzJXRTJNeEllTjhxRFVfOFM5bDZIcEVrQVhUUzFab0MxNWVVeGF3NGFfc0NfQTlOWXd2bG01bUdsR05ZSDl2ejNRNnZPMkNpSXdlWjFyS3Vv?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 19 May 2026 18:17:14 GMT
- [Micron (MU) and SanDisk (SNDK) – Why a Top Analyst Boosted Price Targets on These AI Stocks - TipRanks](https://news.google.com/rss/articles/CBMitgFBVV95cUxPemJ3SDk4amFybllYNU9pckVlWnRRekFSNm9yTlQtZ21icEhQZGV4Ny05M3FMWEhpeHBESVN3cFZVaHpzd2lVY1ZMX3hKcFhfV1NFZ2lSemNhc0RJcTdneENWY0hHWk5PQWhSclgzQWY4LU8xa3U0aDg2WllmdnYxWVRsMHlTeFVrbDRWM2N1TUlpRlJRTlZGRzc2bGM4aWFQUWNfUGZ3V1hUQWp0OUhmdzBRZnJTdw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 19 May 2026 20:35:19 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：AMD Is Up 8% Today: Is It Outperforming Other Chip Stocks Like Intel and NVIDIA? - 24/7 Wall St.；Intel Tenstorrent Interest Puts AI Chip Ambitions And Risks In Focus - simplywall.st；韓商FADU攻AI市場與台灣半導體儲存生態系深化合作| 產經 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.76 | N/A | N/A | 118.96 | 118.96 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.74 | +28.14% | +16.92% | 223.47 | 223.47 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.65 | N/A | N/A | 447.58 | 447.58 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.04 | -3.53% | -1.58% | 2,185.00 | 2,205.00 | -0.91% | 背離 | 74.39 | 29.38 | 410.73B TWD / 17.50% | 2026-05-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.04 | -1.82% | +9.76% | 108.00 | 113.00 | -4.42% | 背離 | 4.00 | 27.14 | 22.66B TWD / 10.80% | 2026-05-01 |
| MU 美光 | 產業/供應鏈推估 | +0.06 | N/A | N/A | 731.99 | 731.99 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.03 | -1.07% | -3.78% | 1,392.56 | 1,562.34 | -10.87% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.06 | +34.97% | +26.10% | 417.76 | 417.76 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AMD Is Up 8% Today: Is It Outperforming Other Chip Stocks Like Intel and NVIDIA? - 24/7 Wall St.](https://news.google.com/rss/articles/CBMivgFBVV95cUxQdFJSTXhUdzZtT0hrbTRnbFM1Rmw1Ui1IYU1XSE9VYmpUZWpxY1RxblVpQTNjMTAtNExIdWFleDZSY0oweXoxWmlXeEtyOXItMm9MWm9JM0tkdDB5STEtMmw2T2psZVJrRU1HNkNoQ3pRdkE5WEx2aEVaWm1oSXlaYnBpMjdrV2liYWR5RmU0bmEtY1dMbjBXaXJxZ0V3TU5wcGI0ZXc3VzRyMjhqYnVVS3BkcWFaNE1PLVdUQndR?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 20 May 2026 16:08:26 GMT
- [Intel Tenstorrent Interest Puts AI Chip Ambitions And Risks In Focus - simplywall.st](https://news.google.com/rss/articles/CBMiyAFBVV95cUxQdE9EVmhLc3VKejNsRllIZnhJMWNVOERnUkxnOUtSWFM1WkxDQUtVckg1TDl4YjhVRXNCR25JUTV3UGhsbUZhRnBKZnNqY0lGbmQ3NUZpeElNb2RNM2xqU1ZMTFROOUE1cEJzMUlxZ3AxU0hQX3lJTFpIZzBhUE5fM3dFSDk3ak9aUTI2U1lBQ2hRcE9YWFlaYWM1NVZsdU16YzdVaXI3Y1JaOEU2WkIySXI4S3J1NE5tVEVtMVd4c0gtTDkxM3NXU9IBzgFBVV95cUxPcGpXWTB4MlZsaUxoLVdtWFJoYTM1VUN3TmRTNE9zVWR3TkloeGZxRWI3aE5Wcy0ycG9xZXUzOXhhRjRWMnhRVHRwWlMwRGhrQ01TR29BVHRNUEtPcWkzTWJJYkphbnF5QzhYMDhWQlNVTmYxeVBZalAyN3VCYlB0WXVOZGhEYVJyZ3BjVE4yX0dxeVpBUldGSzhsOE12R2tiSVlWWEstZV80bFBaZ280Z3RJdk4tQnEyQnhWODBpb21lVnZjUWM3R0JVNkR2UQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 20 May 2026 08:39:44 GMT
- [韓商FADU攻AI市場與台灣半導體儲存生態系深化合作| 產經 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE5Ca2g0Qk1LZXpGeGJKUWRQcWExUzJuYlhpMVdlb19KSjhtSm5IUjFCaWtBUl8xNUdGcEhHVVJCeTE2WHB0Ul9ZaTNWT2dXUTB2MjRIM0FoVnVUVkJSa1E?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 20 May 2026 12:28:00 GMT

## 新興題材：OpenAI

摘要：新興題材：OpenAI 相關新聞集中在：OpenAI 與 Google 聯手推雙層內容溯源，更容易辨識 AI 圖片 - TechNews 科技新報；OpenAI 從非營利轉營利的法律爭議，對未來 AI 新創的治理架構有何啟示？ - TechNews 科技新報；OpenAI 承諾投資新加坡逾 2 億美元深度合作，並設首座海外應用 AI 實驗室 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 新聞直接提及 | 0.00 | -14.42% | -8.54% | 421.06 | 506.69 | -16.90% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：新聞直接提及「OpenAI」，共 5 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [OpenAI 與 Google 聯手推雙層內容溯源，更容易辨識 AI 圖片 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiqwFBVV95cUxOM01rc3Q0aTJHTWM5U1ZzMmZCNkJBeDVsdl9PcEIwT1NFM1Q5bVVUbVJELWxsVldYOTVtN1phakEtWlpyYi1GdnViWkFCSVlEVFBVdlV0TG9mZjhDbHB0bEpHRVJRX0UtTEpUUTdJYUNyb1g4cW1YSTFMNjB0S29OZTAyODl1QkkwV0s0eVMwMEt5bmU1VUNKanpqUzQ2aDNMdFRsR08wWnlfams?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 20 May 2026 10:11:52 GMT
- [OpenAI 從非營利轉營利的法律爭議，對未來 AI 新創的治理架構有何啟示？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMieEFVX3lxTE5RWWlqVjg4dEY4Nzh4ZklsMUhmQ3pRc2dEQ1l3T1ZKUkRIUHFpcDNPSXpfUWJRcU4tRHYxVEV0UFFyMXE0ZzFYS251bkswY09TSGpKZ2ttU1NaN2pYQVhNM3Y4RThNWGVZZVdQQS0xaXk1WE8tQUpmYg?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 20 May 2026 12:49:32 GMT
- [OpenAI 承諾投資新加坡逾 2 億美元深度合作，並設首座海外應用 AI 實驗室 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiqAFBVV95cUxNUTBqZGdRb21xYkx6YXpucm5QY2tKLXJjS3h6NElTZ2FHZGhZVk44MWw1TzFCWVZCT0NHbUZrQm5fTkpXNWF4cWJKRFcyOEdjZjhkaWU3UGFIeFN4elZYMDZCU0VyM056cHJtdmw3RDdXTW1wTUNSLTJpYU5CdkxTSGRfVjBTcmlzRWM1UzFRWUV2Ql9TdUlqNWRRZkZXLVVYSnBscEZwR24?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 20 May 2026 08:52:10 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel Tenstorrent Interest Puts AI Chip Ambitions And Risks In Focus - simplywall.st；macOS 版 App 推出，如何與蘋果原生 AI 競爭？ - TechNews 科技新報；盤點日本隱形冠軍！除了味之素、TOTO，還有哪些日本老品牌默默賺 AI 財？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.72 | N/A | N/A | 118.96 | 118.96 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 新聞直接提及 | +0.56 | +8.39% | +50.49% | 302.25 | 302.25 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.10 | +28.14% | +16.92% | 223.47 | 223.47 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.09 | N/A | N/A | 447.58 | 447.58 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.04 | -3.53% | -1.58% | 2,185.00 | 2,205.00 | -0.91% | 背離 | 74.39 | 29.38 | 410.73B TWD / 17.50% | 2026-05-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | -14.42% | -8.54% | 421.06 | 506.69 | -16.90% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.07 | +34.97% | +26.10% | 417.76 | 417.76 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.04 | -12.98% | -13.14% | 476.00 | 478.00 | -0.42% | 背離 | 10.86 | 44.20 | 62.25B TWD / 19.22% | 2026-05-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：tight supply。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AAPL：新聞直接提及「蘋果」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：tight supply。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Tenstorrent Interest Puts AI Chip Ambitions And Risks In Focus - simplywall.st](https://news.google.com/rss/articles/CBMiyAFBVV95cUxQdE9EVmhLc3VKejNsRllIZnhJMWNVOERnUkxnOUtSWFM1WkxDQUtVckg1TDl4YjhVRXNCR25JUTV3UGhsbUZhRnBKZnNqY0lGbmQ3NUZpeElNb2RNM2xqU1ZMTFROOUE1cEJzMUlxZ3AxU0hQX3lJTFpIZzBhUE5fM3dFSDk3ak9aUTI2U1lBQ2hRcE9YWFlaYWM1NVZsdU16YzdVaXI3Y1JaOEU2WkIySXI4S3J1NE5tVEVtMVd4c0gtTDkxM3NXU9IBzgFBVV95cUxPcGpXWTB4MlZsaUxoLVdtWFJoYTM1VUN3TmRTNE9zVWR3TkloeGZxRWI3aE5Wcy0ycG9xZXUzOXhhRjRWMnhRVHRwWlMwRGhrQ01TR29BVHRNUEtPcWkzTWJJYkphbnF5QzhYMDhWQlNVTmYxeVBZalAyN3VCYlB0WXVOZGhEYVJyZ3BjVE4yX0dxeVpBUldGSzhsOE12R2tiSVlWWEstZV80bFBaZ280Z3RJdk4tQnEyQnhWODBpb21lVnZjUWM3R0JVNkR2UQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 20 May 2026 08:39:44 GMT
- [macOS 版 App 推出，如何與蘋果原生 AI 競爭？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMid0FVX3lxTE9RdDEwSGNFeWQtbFN4SHZzbi05STVIOVRVWU4xTWllLVg5Nm1SU2hjbmNrUE1SNUNUaEJLdDdxanFxUGV2UFR3QTEwb1UybWVhVTNJQkM1QUdZZ3BBZVRwMnc0N0pQQ0tnY0hlMEdPaERlbnM5NU40?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 20 May 2026 13:31:01 GMT
- [盤點日本隱形冠軍！除了味之素、TOTO，還有哪些日本老品牌默默賺 AI 財？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiggFBVV95cUxPZ1hMLVB1Y0syMDlERDlaS3hiWmVMTl93ZlYxM0VXNEY2NEZyU2xNR1lSeWl1dHdfaE50aElQOXk4eXZ6Y2pWS2M4V3ROMEFWRllzSnNJdElLVjBYX1hKNVh5VENKWGpYMUdZQm01VHBCR3JjdXA1enVyN1UzZ0lOZ2pn?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 20 May 2026 09:34:49 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：輝達豪擲 900 億美元布局 AI 生態系，欲以投資「固樁」客戶與供應鏈 - TechNews 科技新報；E.l.f. Beauty to walk back some tariff price increases amid high gas prices and consumer 'suffering' - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +28.14% | +16.92% | 223.47 | 223.47 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +8.39% | +50.49% | 302.25 | 302.25 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | -3.42% | -4.38% | 240.00 | 257.50 | -6.80% | 不適用 | 14.13 | 17.05 | 832.10B TWD / 29.74% | 2026-05-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 1 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 1 篇新聞出現相關標籤。

### 主要來源

- [輝達豪擲 900 億美元布局 AI 生態系，欲以投資「固樁」客戶與供應鏈 - TechNews 科技新報](https://news.google.com/rss/articles/CBMioAFBVV95cUxPejV1SU8tNnZCQzgyRm1iZExBSV9IQkR1eUpiYTlLVDFfWVpmWUxrWmZwcnJNbGhqbzVybmhKd1FyckFKejJiRXRUbUhGVmMyWTdQemlPaExPYnh3c1BLUXZocDBEUDFCdE5kclo3UGRlcE9hN3FjeXdKLVE5ckFaN2VoRVFMYmFCN0ZPcE4ySVc0dk9GM3dVYUptX2dxSVdv?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 20 May 2026 14:05:34 GMT
- [E.l.f. Beauty to walk back some tariff price increases amid high gas prices and consumer 'suffering' - CNBC](https://news.google.com/rss/articles/CBMid0FVX3lxTFBKNUF4aEJjTU5wTjNhbnd6ZEMyMklSOEwtQW9NNVl5UFhBQ1VHVDlZY2J6eEN2Yl9BZGxfbnZzUUZudzdOTHJUT1FCMnRLaDBPU3dQYXU2bHVWNG5ZSjFoTjI3SUtWejNucUtsOURHUmFpcVNUNWRB0gF8QVVfeXFMTzY3b0k0S1RpTG1SWWhUZl80bG5oOHdZdURQN2lZRjIwcHgyVWQ5QlRLdHpCMTVmNGtELW5uMXFBNjdJUW9ndHg2SU16X0oxTUdtRzB4NXMwN1B0SWQ0akx1UUhhSjR0UWk3NzRsWC1odGdTUHVlNG80dW5IQg?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 20 May 2026 20:05:24 GMT

## 新興題材：輝達Q1財報營收

摘要：新興題材：輝達Q1財報營收 相關新聞集中在：AI熱潮帶動 輝達Q1財報營收創新高 - 經濟日報；AI熱潮帶動　輝達Q1財報營收創新高 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +28.14% | +16.92% | 223.47 | 223.47 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AI熱潮帶動 輝達Q1財報營收創新高 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE16VUxiMy13YWFFZkxLODhvNGl5bTVwMjNWYnFvR2xqNmRNXzVFUVZJN3U5Si1qREVSUHhka0VQdEYzUU1KZ0JGT0xmTXRIYU0xYW5BaWRRRV9zZ9IBX0FVX3lxTE5rQjhpcGZ5MTU0WmNHZ1dLeHpNSjA3d2Y5LURJeGtEZ2pDWE9PVlVBMndRcFNPSEtIdmN0ZWJ3SEpCVEFmODhrWjA2Ul9jYXhxamVQeFVrd21wRnVpTHV3?oc=5) - Google News source discovery | 經濟日報 money Wed, 20 May 2026 21:54:15 GMT
- [AI熱潮帶動　輝達Q1財報營收創新高 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxPQlZNZFM0Um9CTF9HOTA5NmZHQk53Yk5hal9WQjFka0lZa0ZrS3hxbWtlSXJzZ1MzTWlXM3E0UUdyV3d6ZzRXemhWakJWSC1IbEdGZnI1ZFpqb1RGOW1hV1J5RDl5TzZaZkZIUzBFNERnQl9oWWg0bVA0Q2VjX3d6bNIBX0FVX3lxTE5rQjhpcGZ5MTU0WmNHZ1dLeHpNSjA3d2Y5LURJeGtEZ2pDWE9PVlVBMndRcFNPSEtIdmN0ZWJ3SEpCVEFmODhrWjA2Ul9jYXhxamVQeFVrd21wRnVpTHV3?oc=5) - Google News source discovery | 經濟日報 money Wed, 20 May 2026 21:54:15 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：換股秀登場 009816、00940等11檔台股 ETF 新成分股出爐 - 經濟日報；台股多空拉鋸 險守4萬關 成交量縮至1.02兆元 | 市場焦點 | 證券 - 經濟日報；台股上演40,000點保衛戰 「籌碼穩定」優勢股具領漲抗跌優勢 | 市場焦點 | 證券 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [換股秀登場 009816、00940等11檔台股 ETF 新成分股出爐 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9mU2YwTi1SSk9mcmM2Sm5uQjREbEVDVHRybHdiaTM4UjdoQ0FTcDhUZDZjNFl2Y016QnN4b3gxVEJnd2VMbURkejhUeVotV0VnY3Nobll1ZlpFQdIBX0FVX3lxTE5POXlSM25KQ1haaklzOXVVQmpBU3B1UEVVUUVnWHVXRGpvV3BYYWduSDVYUThuVHB6Wlhkc3UtZ3pyVWtvNWNJd2pYNzcyTUc0aU9oRUtYUVR0dEZRd00w?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 20 May 2026 03:00:00 GMT
- [台股多空拉鋸 險守4萬關 成交量縮至1.02兆元 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5aVmdXc1dLaHRKYVZFeWdEbjdzRmtSQmdZdVJtRGVzRFI4UkFIY29Bc0RyZjNFbkR5RGFRVzY0UmNvYVE1dXBFTHNCZUdkeHZnNVdZUHhQTnhSUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 20 May 2026 16:35:44 GMT
- [台股上演40,000點保衛戰 「籌碼穩定」優勢股具領漲抗跌優勢 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9Panp3RTNudnprU2QzakNhNzY0VUc3REw0cnJZeGdSZkF4RUplVlR6dTAyMUxRTEtKTkxoazd0bHBrcDBaYjF4UkRUUGxQMlZlMENPeDZrbXp2QQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 20 May 2026 14:22:22 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》下跌154點、連四黑K，險守4萬大關- 新聞 - MoneyDJ；法人專欄分析內容-台股 - MoneyDJ；法人盤勢分析內容-台股 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》下跌154點、連四黑K，險守4萬大關- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxOMmY5N2JiaEhiaXpKdmNVWk5UN3FQTm5lY3RsTU5WcFpFMk5GWDlmVmRYU0ptQnBzM0d3T0VkcVBoOHlWbk1nTXdWMko5SUxhMm1oRXNmaXBQQnMxZ2l4VlZLTXQ1cnVtV2RyWC1nVWxla2JmRlVPV2NwRzJ5ejU5UGJzSWdaWXJKWDR1bTZtcW9ZQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 20 May 2026 07:27:00 GMT
- [法人專欄分析內容-台股 - MoneyDJ](https://news.google.com/rss/articles/CBMijgFBVV95cUxQamp6TEZvemJmekhKM2txWmk3V1JqbGRrOXBKTUE1UW5ieFdSYmRCNUVic3QxLU5zd0JaelFwekhEY3EtQWF3aDltSFhIQm9rb2Q0aXQzVk5WaXpaVW40d05WRnNaTVk0YTdrV0FzRG1PTlFDSkl4MV9tU3ZUVXVSSk5MRFBKOTZNYk1ta0R3?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 20 May 2026 16:17:20 GMT
- [法人盤勢分析內容-台股 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxOUjRDYUFpWHNEM3FBdS1hWkx5ZDI4bFR5ZHpoaHFaR2pDdjYyTUVOS1g0Rk5Jc1hFVWtVQ0RhY3RfclR5LVNJRW5TSUpiMXVOdnBqeGZ6aVJtdmJaenVVMFhTZjJ1YzNBS1I3Z0lkZ1Z3Y3ByUjd2YUZReTNhak50YWtWN3JsQkdtSHB3c1BKamY?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 20 May 2026 00:32:13 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
