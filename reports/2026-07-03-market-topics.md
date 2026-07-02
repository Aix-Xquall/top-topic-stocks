# 每日股市熱門話題分析 - 2026-07-03

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜負向｜熱度 5｜市場確認 65.09｜同向 3/5
2. **利率與成長股估值**｜中性｜熱度 4｜市場確認 N/A｜同向 0/0
3. **半導體與晶片供應鏈**｜負向｜熱度 8｜市場確認 64.21｜同向 3/5
4. **AI 伺服器與資料中心**｜正向｜熱度 9｜市場確認 36.74｜同向 3/6
5. **消費電子與手機**｜負向｜熱度 2｜市場確認 14.31｜同向 1/2

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.21（樣本 18）
- 5日相關係數：0.08（樣本 18）
- 同向比例：10/18

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 65.09 | 3/5 | 1 | +7.70% | +3.38% |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | 64.21 | 3/5 | 1 | +7.40% | +0.25% |
| AI 伺服器與資料中心 | 36.74 | 3/6 | 2 | +0.58% | +3.77% |
| 消費電子與手機 | 14.31 | 1/2 | 1 | -6.89% | -12.88% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：B0478BDFF2C3 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-06-20 | 0.29 | 0.21 | +63.16% | 19 |
| 2026-06-21 | -0.01 | 0.32 | +55.56% | 18 |
| 2026-06-22 | -0.87 | -0.87 | +100.00% | 3 |
| 2026-06-23 | 0.38 | 0.01 | +62.50% | 8 |
| 2026-06-24 | -0.38 | -0.11 | +25.00% | 12 |
| 2026-06-25 | 0.10 | -0.21 | +20.00% | 5 |
| 2026-06-26 | 0.08 | 0.04 | +25.00% | 16 |
| 2026-06-27 | 0.12 | 0.29 | +57.89% | 19 |
| 2026-06-28 | 0.16 | 0.55 | +85.71% | 14 |
| 2026-06-29 | 0.49 | -0.25 | +38.46% | 13 |
| 2026-06-30 | 0.44 | -0.27 | +62.50% | 8 |
| 2026-07-01 | -0.08 | 0.25 | +30.77% | 13 |
| 2026-07-02 | 0.30 | 0.03 | +55.56% | 9 |
| 2026-07-03 | 0.21 | 0.08 | +55.56% | 18 |

## 歷史回測摘要

- 回測日期：2026-07-03
- 近5日 3日相關：-0.08
- 近5日 5日相關：0.18
- 同向比例：+46.15%
- 權重狀態：未調整

- 方向準確度：+46.15%
- 信心排序準確度：-0.08
- 診斷：低相關

調整原因：近 5 日有效樣本 13 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Zacks Investment Ideas feature highlights: JPMorgan, Sandisk, Micron Technology, Nvidia, Broadcom, AMD, Taiwan Semiconductor, Arista Networks, Meta Platforms and Microsoft - The Globe and Mail；Why Is SanDisk Stock Falling Wednesday? - SanDisk (NASDAQ:SNDK) - Benzinga；Memory chip stocks hit the brakes at highs: SanDisk and Micron plunge sharply - 富途牛牛

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | -0.65 | N/A | N/A | 975.56 | 1,032.28 | -5.49% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.65 | -14.89% | -25.27% | 1,745.00 | 2,335.00 | -25.27% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | -0.50 | -7.72% | +11.71% | 194.83 | 211.14 | -7.72% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.48 | N/A | N/A | 517.82 | 540.88 | -4.26% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 新聞直接提及 | -0.36 | -0.57% | -22.93% | 390.49 | 506.69 | -22.93% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | -0.48 | -19.32% | +16.46% | 360.45 | 446.77 | -19.32% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | -0.24 | +4.01% | +3.14% | 2,465.00 | 2,505.00 | -1.60% | 背離 | 74.39 | 33.14 | 416.98B TWD / 30.09% | 2026-06-01 |

關聯理由（前 3）：
- MU：新聞直接提及「Micron Technology、Micron」，共 3 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk、SNDK」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Zacks Investment Ideas feature highlights: JPMorgan, Sandisk, Micron Technology, Nvidia, Broadcom, AMD, Taiwan Semiconductor, Arista Networks, Meta Platforms and Microsoft - The Globe and Mail](https://news.google.com/rss/articles/CBMi5gJBVV95cUxQd3o5MUdua3lkZmZ6SXB3OUQxQVZGUmVRNjJiLUktM1NtRldCREE2ZUFvQzl6VFJDSlJiZmpuUjJMQjh3b1VBbUk2MUtia1g3VllzV2VKM1hRelkyak5SX3ZhNUgwUW9WNWZkVjM4YnFFak1YR05LQjBVR1oxN0RlRnFOM1NDNzB2bkZFdlpuNzlZWlNqSXdxRWdHLTlWRWNXSFUxR0NQTm9tMkM1ZTRwamViRWR0czR4MzRsWF9JME9ZdmdKaFd0Y0VBMTBObkNXb0xlLUNsQ0t6WkRGVUVWZ3Q5Y0hvSDRTalY4R1VSbDBUcEZUc2N1bXlEaHBwWGRkME5LeUVqTmQzdFlEZUhtdkRJNWVOUmFUR015LU9vdW9EWHE2X2IybVhtd1RpUGlkenh4YzRVMVdER2N5dFhMdnJHY2hTeEJUbEhkc2FDc2lhT29jeXJWbGpJdmVoWGVWWm5nZXdR?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 02 Jul 2026 14:24:00 GMT
- [Why Is SanDisk Stock Falling Wednesday? - SanDisk (NASDAQ:SNDK) - Benzinga](https://news.google.com/rss/articles/CBMioAFBVV95cUxPV0NKNWVHQ2l5YU9xbHR5ektHalFSUFB1VEJ5RmxZWnloeWFKOEx3anN5dWV3MXhvTzRLUnNndk5sQnVwZUY3ZGw2NnpvWmRHZ01qSXBFYk1vem5CZXNCRHBMVEFILXdzVTdGcjJKR2Zfbm5kQW4tcTBkMXRUWENfRXB3NUZzVlExUFBQam5mLVhIZXhrRDgwNldlYTlHb0Yt?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 01 Jul 2026 13:27:19 GMT
- [Memory chip stocks hit the brakes at highs: SanDisk and Micron plunge sharply - 富途牛牛](https://news.google.com/rss/articles/CBMimwFBVV95cUxPVFNpakNLMWViUlhoUmlpdjZqS2NwRkZYOHI0dWFyY2JKSEJ2N1N3VGlOVklSSWVhMU1uSUtGYTV1N1BSU3JSVkNEQjR5YVlSZjUzeEFRV1ItNkROaFJKdHV1c3ZWNXl0ZTBqZVVpOEVKRTVVQjY3N0pEWDY0MWRWM2hTOUc2MlY1andMQXEwUWphWEt2MktzTHJfRQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 01 Jul 2026 19:00:44 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：輝達終於出現勁敵？AI 晶片新創 Etched 估值達 50 億美元、10 億美元訂單入袋 - TechNews 科技新報；半導體「普漲黃金期」已過！大摩點名擁抱這幾檔龍頭、警惕4台廠估值泡沫 - Yahoo股市；半導體「普漲黃金期」已過！大摩點名擁抱這幾檔龍頭、警惕4台廠估值泡沫 - news.cnyes.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | 0.00 | -7.72% | +11.71% | 194.83 | 211.14 | -7.72% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | -0.57% | -22.93% | 390.49 | 506.69 | -22.93% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [輝達終於出現勁敵？AI 晶片新創 Etched 估值達 50 億美元、10 億美元訂單入袋 - TechNews 科技新報](https://news.google.com/rss/articles/CBMinwFBVV95cUxQSC1jLVBaV2F3WlQwS29ZMUJHVGtmVXBMNlh0UGVRWGNRNEtUU2QzeUx4X2RSczN0Q1BGSXVJdFpUOFVpMnphOWhUMEc5RjF6c1Z6S3VLRy1mTFhacjhEa0pGQjVKZzlJeW5jcW9tc1BsN3c2LXBVYUtBQnE3Y1pXNUtncVlGellNaDZMOXIxaXU5WDctWmV3MXplc1hMOXc?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 01 Jul 2026 02:43:46 GMT
- [半導體「普漲黃金期」已過！大摩點名擁抱這幾檔龍頭、警惕4台廠估值泡沫 - Yahoo股市](https://news.google.com/rss/articles/CBMivgNBVV95cUxPM0dfYmQ1VENCUFFEa09xTWJaNUNUQVJ3TlRMUVJBd0pDMDljV1Q1ZUVoM2pGbHZHNkdfQ0R0emJTV2FFaTR2TmN3eEJHUGZ6cXNHYm1hT1hnSjZLWGF5bUxxazJNMzdJVnd5aWQwMDBMTnpyV1FyN2U1SkI1eU54UW9vbkE1NmFleFFIRkJLVE5iUDZ0cmVvY192VFd4d0hLS2JidXlpa0ZwaVlEa0tLMGVyUXgtX2VqSm96MnBiVkRGeDJWTVVLdGdwaXMycnlBMUdqUThBcmpMVXQtYWZNcHR4dFF1OG5CZHlUckdiOWM0U1NUdTdDRWJZTEZxcjJodFRZSW9IZUppeV9MbEtjNTJDT0g0eGsxcnh1S3c2X3VrWTQ0ZG9JSVU1eVh2dlVKRk9lN0o0YUU5UURjSjhDZUR1ZWh5UExqdTNjWVIwUjg5UFQ0cmtpNjA3OUF2akFzemFFWVFLanVuSWN0Nm1kUk5xTkNMVVNsSFp2bW5CSDZkTXZ4M2NZU0NsNDRTcGE4dTlCV3hCTkxwTlhJa0hjdXIwcTV0Nnd5RV9FTjFETFA2SVBJU2lxT25FcVA1QQ?oc=5) - Google News source discovery | Yahoo 奇摩股市 Thu, 02 Jul 2026 08:33:07 GMT
- [半導體「普漲黃金期」已過！大摩點名擁抱這幾檔龍頭、警惕4台廠估值泡沫 - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTE85ZjlQcnZNNGlnUWZTd3lKVDJTd3hsenFQOHctamp2RkthNTdEdzRVN0Y3RGc4OVh0Sm5tLTYtcVRobHJIY0ZrOGtUN2tFcHM?oc=5) - Google News source discovery | 鉅亨網 Thu, 02 Jul 2026 08:33:07 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：AI 半導體鏈 野村唱旺 | 市場焦點 | 證券 - 經濟日報；Intel Sinks 6% Even as HSBC Sees 60% Upside, AMD Slides 5% as Chip Stocks Pull Back - 24/7 Wall St.；Intel (NASDAQ:INTC): What Comes Next for the Chip Giant? - Kalkine Media

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.65 | N/A | N/A | 120.35 | 127.02 | -5.25% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.54 | N/A | N/A | 517.82 | 540.88 | -4.26% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.03 | +4.01% | +3.14% | 2,465.00 | 2,505.00 | -1.60% | 背離 | 74.39 | 33.14 | 416.98B TWD / 30.09% | 2026-06-01 |
| 2303 聯電 | 產業/供應鏈推估 | -0.04 | +0.91% | -7.28% | 165.50 | 169.00 | -2.07% | 未明確 | 4.00 | 41.58 | 22.94B TWD / 17.78% | 2026-06-01 |
| NVDA 輝達 | 產業/供應鏈推估 | -0.04 | -7.72% | +11.71% | 194.83 | 211.14 | -7.72% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | -0.04 | N/A | N/A | 975.56 | 1,032.28 | -5.49% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | -0.04 | -14.89% | -25.27% | 1,745.00 | 2,335.00 | -25.27% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -19.32% | +16.46% | 360.45 | 446.77 | -19.32% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel、INTC」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 2 篇新聞出現相關標籤。

### 主要來源

- [AI 半導體鏈 野村唱旺 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBHQ29Vc0dqZ3Itc1BlQmFrQXRpOVN4RGdhWldhbFhCSUhhVXV5cG42WEtRZUVpeHI4Ql81aFVKWFpoSDhPb0VDQmFXRlFDbjVvVTlXM29yR2tPQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 01 Jul 2026 16:54:21 GMT
- [Intel Sinks 6% Even as HSBC Sees 60% Upside, AMD Slides 5% as Chip Stocks Pull Back - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiwAFBVV95cUxQQTN6SGtLUDNnbWRMZURoNHduUC11Zm5CelhGVTNBT1RJSjNIZndyWVZZTGJELWlrQlF4TkZGWF93WGVyWmg1Q1JfaUxqTlpDMnk2OUhjWGhsMzE3MlUxdHlGcnlSMDdXLXRDc3o4WGhCNjEtdk53TjVmcjBKWDVOSUd0UE5RT0Q5NW0zSDNYU0pzOWJUX1N1X0JyVkcyOUhNb0tsdHdLZUNlbElsRnhRZEN5M2FfeWlIbUFDci1sc0o?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 02 Jul 2026 18:16:19 GMT
- [Intel (NASDAQ:INTC): What Comes Next for the Chip Giant? - Kalkine Media](https://news.google.com/rss/articles/CBMingFBVV95cUxQTjZYRFMxeUJjWk10TmR2dDNyWDBMZUtyQVZyYmhlU1NzZUp5dkxvOS1QcWZZenJyaXZXNm45c0hVcGkzdVdqRFZyZkotaERBU2dzZEllX19FcTdGbTRPUE1OUEZuanZ4cGM3N2p0eGRiajBVc2ZCdTJoMU9RWndwaDhhM0NYUE9XVzI5REg5cWRTckw5WWdGWFdURE02QQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 02 Jul 2026 16:09:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：AI 半導體鏈 野村唱旺 | 市場焦點 | 證券 - 經濟日報；比爾·蓋茲預言十年內 AI 取代大部分工作，只有四種職業留下 - TechNews 科技新報；「矽電光熱」成 AI 發展主要瓶頸！法人點名台積電、穎崴等十檔受惠股 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.31 | -7.72% | +11.71% | 194.83 | 211.14 | -7.72% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | +0.60 | +4.01% | +3.14% | 2,465.00 | 2,505.00 | -1.60% | 同向 | 74.39 | 33.14 | 416.98B TWD / 30.09% | 2026-06-01 |
| MSFT 微軟 | 新聞直接提及 | +0.43 | -0.57% | -22.93% | 390.49 | 506.69 | -22.93% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 產業/供應鏈推估 | +0.08 | N/A | N/A | 120.35 | 127.02 | -5.25% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.06 | N/A | N/A | 517.82 | 540.88 | -4.26% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -19.32% | +16.46% | 360.45 | 446.77 | -19.32% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.04 | +15.95% | +13.42% | 727.00 | 727.00 | 0.00% | 同向 | 10.86 | 67.50 | 63.03B TWD / 28.57% | 2026-06-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.04 | +11.13% | +0.81% | 4,345.00 | 4,345.00 | 0.00% | 同向 | 62.91 | 69.24 | 47.43B TWD / 4.99% | 2026-06-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。 方向判斷命中詞：受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 同時符合主題標籤：AI, advanced packaging, CoWoS, AI server。 方向判斷命中詞：受惠。
- MSFT：新聞直接提及「Microsoft」，共 1 篇新聞命中。 同時符合主題標籤：AI, datacenter。 方向判斷命中詞：受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AI 半導體鏈 野村唱旺 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBHQ29Vc0dqZ3Itc1BlQmFrQXRpOVN4RGdhWldhbFhCSUhhVXV5cG42WEtRZUVpeHI4Ql81aFVKWFpoSDhPb0VDQmFXRlFDbjVvVTlXM29yR2tPQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 01 Jul 2026 16:54:21 GMT
- [比爾·蓋茲預言十年內 AI 取代大部分工作，只有四種職業留下 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiqAFBVV95cUxONS1wYm5VenVsNWp6RUYySzRfZVg1cW9Qcm9XSmdSNk5SVUViTDhLWlpJWUVHU192SkRjcnFSZ2JMQ2M1SGZtcXQ3TTd0MWU5WXF1b0NDRk9wajdXeDBaQ004V1lBZnkzeGVsVlZVVE9kQm13aFVPQzNqamxLeVhWSHhWU1k2eU5nTmNkSGw3dTExYkR0cnNQbE5oV19QNERhTG1JS1NRc1k?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 01 Jul 2026 23:14:29 GMT
- [「矽電光熱」成 AI 發展主要瓶頸！法人點名台積電、穎崴等十檔受惠股 - TechNews 科技新報](https://news.google.com/rss/articles/CBMif0FVX3lxTE8tYkgydnJUUVJOd1N6aXBIUlFJdDdacGhvQWtrNEdZOTlBWGJUT2IwVVRNTlJDaWNpMlIyRnZSc3RTSGt6MElsZC1HMVFGQV9WWG1vaHh2Q3NLLUtZQVk0SlN6WUFPZ1NwUEFTV1VOcHFJVGlLTTJkUHQzTVdsWk0?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 02 Jul 2026 02:56:04 GMT

## 消費電子與手機

摘要：消費電子與手機 相關新聞集中在：Meta's Pivot to Cloud Leasing Sparks Concerns of Computing Power Oversupply. Micron Falls Nearly 10%, Marvell Plunges 7%: Is the Logic Behind AI Hardware Stocks Shaken? - TradingKey；AI 手機對萬級大電量的需求與必要性？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | -0.48 | N/A | N/A | 975.56 | 1,032.28 | -5.49% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 產業/供應鏈推估 | -0.05 | +16.83% | +32.95% | 308.63 | 312.06 | -1.10% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | -0.08 | -3.04% | -7.18% | 239.00 | 289.00 | -17.30% | 同向 | 14.13 | 16.97 | 859.41B TWD / 39.57% | 2026-06-01 |
| 2454 聯發科 | 產業/供應鏈推估 | 0.00 | +11.13% | +0.81% | 4,345.00 | 4,345.00 | 0.00% | 不適用 | 62.91 | 69.24 | 47.43B TWD / 4.99% | 2026-06-01 |

關聯理由（前 3）：
- MU：新聞直接提及「Micron」，共 1 篇新聞命中。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AAPL：產業/供應鏈推估：公司標籤符合「消費電子與手機」關鍵字 hardware, consumer electronics, smartphone；其中 1 篇新聞出現相關標籤。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「消費電子與手機」關鍵字 hardware, consumer electronics；其中 1 篇新聞出現相關標籤。 方向判斷命中詞：falls。

### 主要來源

- [Meta's Pivot to Cloud Leasing Sparks Concerns of Computing Power Oversupply. Micron Falls Nearly 10%, Marvell Plunges 7%: Is the Logic Behind AI Hardware Stocks Shaken? - TradingKey](https://news.google.com/rss/articles/CBMi3gFBVV95cUxOZXZlRVg1M0Z2eXF2Q2Q5SEoyaF8wRHBLckYzeEJqaWhNNE1VOU5uTURkdFdZWmFyazhIWDIwQ09FS29jSzVxQi1yNHd5SUpycVFMaDFvMmxZT2paVDMwc09XYzQxOE1QVmpDR1kwWHgyeC0xS0lTckY3eDR3R2Z4X1p2a0dranJnNjhOR1lYaUdqeTcwQWNSVXUwSU1WSkZZWENOSEdhczFoVUhkN2xnLTFidkFiZFppNHoyZXVmU3k0N3pZVXE2VGYwc3g0X0F0UDVQVkk2T0hXMUlUQUE?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 01 Jul 2026 18:08:18 GMT
- [AI 手機對萬級大電量的需求與必要性？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMimwFBVV95cUxNT3NTc2h0RWRGZzZPZFh3OUFoOEpzdjFWdVhDZ295azVqaGdPM2hIZnBSak5Xbi1QLWhkZE1MSW5maUlkVmpIMWxuNHFqMEljckdCblJCWU44SnpPT3NfNXh4UUw4T05HZmtQU2NrbFNwVS1WUkNLMEozVnU0cG9qRnFPOTY2bTNLa3JvZ1FIejJEM1hlTUFrUUZWVQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 02 Jul 2026 21:12:26 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：比外資更大咖的金主來了！賣超890億元 台股僅跌274點 - 經濟日報；台股外資倒貨 內資撿便宜 法人預測後市震盪向上 | 市場焦點 | 證券 - 經濟日報；主動台股 ETF 強悍 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [比外資更大咖的金主來了！賣超890億元 台股僅跌274點 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1waFVPdlV3TktBenBsX2JJQkhXWHdVb084Q2Q3ZjNaa0w2eDR5VUhUQXl4X2I5cUNNd2RXVGFJS1JSdDZLWDY1WVlIMTVBa2FOa2Y3SnVBRDZmZ9IBX0FVX3lxTE1qU1R4eEY0LTR0UVQ4ODR3bG44M3FwNmdCRklmQmlhSVF4NVNJQ09jdTlnc1czN3NwWXZoS2g3OGo1aTJWM19sTWVYVmx1Y2pKZnAwMDdieEZRM3RURnM4?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 01 Jul 2026 09:00:00 GMT
- [台股外資倒貨 內資撿便宜 法人預測後市震盪向上 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMikAFBVV95cUxOeVVCNHZqY0xsdGY0eUhrU0JsR005bzBONFJYVEhqUy1QNk1hNHplbFhfRUpZdUFnR1RKenJ5a3NaTTlaMUo1aVdxVlBrZHRqcDYydkYzUURBcTlLMHQ0Mk16d0pmdG56M21nRWhnZXJ1eUJhcFlHdlJWa29WZ3RnVjkzdkduNVMzVk1EaFFPbjA?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 02 Jul 2026 17:20:34 GMT
- [主動台股 ETF 強悍 - 經濟日報](https://news.google.com/rss/articles/CBMifkFVX3lxTE1ZY3JRN3A5Vnk1RkdpNEk5d0ZrTnJYY0kta0VWZERSdUhpeFR5NmgxZ0NFRXhzdXgzR0dFdjhlWmZTcnNMSEtDR2NULTdCUHpMMGxjYmhIb295bjJoUS1pVDh0cHc4dnFDbFNNelQ0a1JaVjZEM3JaM0IyLW4yd9IBX0FVX3lxTE9wMTB3Qi1oaXM0ZWJneEprZHdTMC04RE56OGFiNExKMUdfQ2ZzQ1Y3Z2xZYXpsVXBHNjhWRldXeFJUaEFPdGg5emFqNFlqV2tTTm5zaVpPbUFiN0xjdERR?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 02 Jul 2026 17:55:48 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：台股延長交易時間？金管會：須先達成社會共識- 新聞 - MoneyDJ；【台股操盤人筆記】行情雨露均霑，核心權值股仍是首選 - MoneyDJ；《台股盤後》開低走高、收跌274點，10日線失而復得-新聞內容-基金 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股延長交易時間？金管會：須先達成社會共識- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQMTVqUmRtc2pKRG03Tm5LSHhUUnU3elhWMXhsSDkycXhlZW1YZ3M3ajBJWTVQcXZSS1N5NXF2TXAzXzBpTElEbHUyNVJNZnh1ZWhZOVZiRmRSUnVzVC1vVldqMkxVTWpxSkNBZmFWaDZxM2pHQ2lWZnN2QUFTWTllX0lGdlc2RGxsS1J3OGM1bndTQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 02 Jul 2026 21:03:00 GMT
- [【台股操盤人筆記】行情雨露均霑，核心權值股仍是首選 - MoneyDJ](https://news.google.com/rss/articles/CBMilwFBVV95cUxOM1hHRjFCUGI0N19uaVIzVzNVd09NVjZTNUJrSWh3ZHR1NC1VS1F2QUNGVkdVQkpKSnNibi11ZVNSZkhvU1p1NFU0X2toX2xCenpiX285SXVLSzRLN21oeFFHZUVSRlVLcXFmUzhscDVnR21IQmc5bHlsM1VXTVdsa3JJbjBCU2tCWXpjSVVXVWNRVXktWmpZ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 02 Jul 2026 08:51:00 GMT
- [《台股盤後》開低走高、收跌274點，10日線失而復得-新聞內容-基金 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxOUFlleHBoTDBpODBvRW5TNm16TzlzUDlpcjVZdUMzSG9fUEllNm1oM2tzMmdjNzlNb241LUtDQ3dmblgyd1ViV3JPVEphWlZIN2FzbF81aWxTOE00UFRUalg2eTZRNFYxNzNKbjVIWnhBaVRGYXA5eUtGckNuZWRHQlJEVkV3eS1EX1pneFV1Zmg?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 02 Jul 2026 07:45:00 GMT

## 新興題材：B0478BDFF2C3

摘要：新興題材：B0478BDFF2C3 相關新聞集中在：個股動態報導內容-D57A9166-A411-47A7-A4D4-B0478BDFF2C3 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-D57A9166-A411-47A7-A4D4-B0478BDFF2C3 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxPdkNWUjlxYU92S3drWjdCUFhHQWhlYzUxYlB1cXhlbkhEUWJtMjIxcGRQOVZoNjhZdmZwbXBzNDU4ZXkwU05zbkpVRlBpQ0NlRThMWUtMeGFGNWVfU1dObThnTUROTzZaZkJPbDNXSmMxYm96dm1GNHVVekhnNlhHd29iTDFSUnpFZ0VTR0hwRHF1WWNk?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 02 Jul 2026 12:15:40 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
