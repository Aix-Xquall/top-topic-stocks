# 每日股市熱門話題分析 - 2026-05-25

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **半導體與晶片供應鏈**｜正向｜熱度 6｜市場確認 100.00｜同向 1/1
2. **記憶體與 HBM 供應鏈**｜中性｜熱度 7｜市場確認 N/A｜同向 0/0
3. **散熱與液冷供應鏈**｜正向｜熱度 2｜市場確認 100.00｜同向 2/2
4. **新興題材：SpaceX**｜負向｜熱度 2｜市場確認 100.00｜同向 1/1
5. **關稅與供應鏈轉移**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.40（樣本 10）
- 5日相關係數：0.33（樣本 10）
- 同向比例：5/10

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 半導體與晶片供應鏈 | 100.00 | 1/1 | 0 | +23.47% | +12.66% |
| 記憶體與 HBM 供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | 100.00 | 2/2 | 0 | +14.98% | +8.16% |
| 新興題材：SpaceX | 100.00 | 1/1 | 0 | +14.93% | +9.08% |
| 關稅與供應鏈轉移 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 0.00 | 1/6 | 5 | -14.30% | -8.18% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：半導體關稅 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
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
| 2026-05-22 | 0.05 | -0.00 | +33.33% | 15 |
| 2026-05-23 | -0.00 | -0.05 | +84.62% | 13 |
| 2026-05-24 | -0.11 | 0.22 | +86.67% | 15 |
| 2026-05-25 | 0.40 | 0.33 | +50.00% | 10 |

## 歷史回測摘要

- 回測日期：2026-05-25
- 近5日 3日相關：-0.00
- 近5日 5日相關：0.02
- 同向比例：+45.00%
- 權重狀態：已調整

- 方向準確度：+45.00%
- 信心排序準確度：-0.00
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

摘要：半導體與晶片供應鏈 相關新聞集中在：中國聞泰提告安世半導體求償370億元| 兩岸 - 中央社 CNA；Nvidia says its forecast for $200 billion CPU market includes China - CNBC；Direxion每日二倍做多半導體5強ETF - 價格 - ETF - MoneyDJ理財網

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.60 | +23.47% | +12.66% | 215.33 | 215.33 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 產業/供應鏈推估 | +0.09 | N/A | N/A | 119.84 | 119.84 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +2.27% | -0.44% | 2,255.00 | 2,255.00 | 0.00% | 不適用 | 74.39 | 30.32 | 410.73B TWD / 17.50% | 2026-05-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +0.88% | +3.64% | 114.00 | 114.00 | 0.00% | 不適用 | 4.00 | 28.64 | 22.66B TWD / 10.80% | 2026-05-01 |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 467.51 | 467.51 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 751.00 | 751.00 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | +6.90% | +5.05% | 1,478.69 | 1,562.34 | -5.35% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | +33.81% | +25.00% | 414.14 | 417.43 | -0.79% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 CPU, server CPU, x86, foundry；其中 1 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 0 篇新聞出現相關標籤。

### 主要來源

- [中國聞泰提告安世半導體求償370億元| 兩岸 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE9IU0ZWbVVLdm9pYUdvNXNZbDUteVBzYkVMNTVvSUFHel9ZaWtmcHZOa0NCX05idXlnQjMzM3h6b0VRRHJERWVCUnhESndLQUc1U2I3enQtN1l0dmcwVVE?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 23 May 2026 05:00:00 GMT
- [Nvidia says its forecast for $200 billion CPU market includes China - CNBC](https://news.google.com/rss/articles/CBMimgFBVV95cUxOdXJ0YUZEVDhwbXVNTU5paDVicmdKVy1pTTloTFQ4T21TTF9ET2wwRmh4cTRPUHU3eGQ0QWVkTnJ5VUNSSXVXTFlwOFV3R0liaVQwdmdDN0ZNcVhvbndMSUVkdFRVcG9iNG9UR3dkOXlIanpMckpRUkgzbG1BaHdMWm50RGlOaG0wMVBCUzFPZFpYc0lsNmg1dlFn0gGfAUFVX3lxTE9oUlp6MGEyR1V4OXZfcHg2c0FvMUszRnJOWm1hSjlXSmcxSXUyaGNURFJxUG5seEdGVmtOTk44Tk5TXzE4cnphNjREZEs0RkVJbE1pV0txYWpScnF2eE12WTFseGo1SXNkRGtPNk9VUGx5UEk0b0JEc0hKMTJpaklwV0ctcDdsVC05RDNaalZINzM5WTB0dTk3Q3pzU2tiSQ?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 23 May 2026 12:03:16 GMT
- [Direxion每日二倍做多半導體5強ETF - 價格 - ETF - MoneyDJ理財網](https://news.google.com/rss/articles/CBMicEFVX3lxTE9VQV8zLVQwdU1pVjJkcjA3ZzkzTXdpSVpRVXZ2djkwMDJRbU04VnUzU1ExMklNc0twZHljdTl1RGxaN0Z3TDd3MFo2TEJOdUsyNFVUeElMVDFTbkQ2cTBIRDZ0VUZHN0I2WEpvS3hCbUs?oc=5) - Google News source discovery | MoneyDJ Sat, 23 May 2026 01:24:30 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Memory Chip Supercycle 2026: Why Micron and Sandisk Are the Hottest Bets Now - The Motley Fool；SA Asks: What's the best memory chip stock right now? (MU:NASDAQ) - Seeking Alpha；A Billionaire Investor Just Increased His Exposure to Memory Makers Sandisk and Micron. Should Investors Buy the Stocks? - The Motley Fool

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 751.00 | 751.00 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | +6.90% | +5.05% | 1,478.69 | 1,562.34 | -5.35% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +23.47% | +12.66% | 215.33 | 215.33 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、MU」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 4 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Memory Chip Supercycle 2026: Why Micron and Sandisk Are the Hottest Bets Now - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxQM0JMOHE1X2dfeFp2V055VUg3NDdBR3dsNWVhdVhrQms1Y2kzSnVtV1YtQzF4TDZYdUpIdG9mQkVaVWtITExjZDR6OFM0VmZoakNmR2J1TEpRQ3NmTW81QUF4aFZ3VVBHcjdIQ1UzUjA1MEE1SFZ3d3pHaHVJczk0ai1Mc3FLNFJXRVVaX2JnWEZHTlo4MUFSaA?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 23 May 2026 09:23:00 GMT
- [SA Asks: What's the best memory chip stock right now? (MU:NASDAQ) - Seeking Alpha](https://news.google.com/rss/articles/CBMikgFBVV95cUxNX21SMDFpcS1mRE1wUENtQnAteEtiaTk2Z0VsVHFGOWhPSlNMdE9kVEtyTHR2TkVPWDkyNi1ic3BkbmpHZS1EdUIybkRtSnJjcHdOUVhFWjh2dmFJcmc2b0otZnZBcE1YaHRDd08tMjdWZWZld0ljdmI2TWlXVzhuNG9BU0dtdVVFcEp3U1pvMTIzZw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 23 May 2026 15:00:42 GMT
- [A Billionaire Investor Just Increased His Exposure to Memory Makers Sandisk and Micron. Should Investors Buy the Stocks? - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxPUVBOYTlGSEl0VWFGX2hjU0I0ejFnMWJ6Q3c0N2I4NmZpYjQyZFN5RlpObGtXVjhqR2t5dllaTzlOR3Rya005dnIwN0tXYzhPZUFEQ1FDQkpDZUhENVVhaDM1TW5ybEZqaHdDTEptWFo2bEluSkFUdF9xb25rTkpFYXdZeGF4TjRST285SWxxNjJCcGd5QThzcQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 23 May 2026 12:45:00 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：輝達Vera Rubin點火！這「散熱大廠」液冷商機爆發 第二季EPS估達22.79元 - Yahoo股市；輝達新一代 AI 平台 Vera Rubin 報到 電源、散熱鏈含金量大增 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.67 | +6.49% | +3.67% | 2,545.00 | 2,835.00 | -10.23% | 同向 | 61.06 | 41.82 | 15.63B TWD / 71.62% | 2026-05-01 |
| NVDA 輝達 | 新聞直接提及 | +0.65 | +23.47% | +12.66% | 215.33 | 215.33 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 2 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：大增。
- NVDA：新聞直接提及「輝達」，共 2 篇新聞命中。 方向判斷命中詞：大增。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [輝達Vera Rubin點火！這「散熱大廠」液冷商機爆發 第二季EPS估達22.79元 - Yahoo股市](https://news.google.com/rss/articles/CBMioAJBVV95cUxOVTFFWUJsZVBsR1RQZVU5anZUNlBTVGpuNjV6MW91OGVHNnZ4cEZKdE9sZFc3VV9iby1UV01odmozVmQxaXBYdVR6bGJUTEtUdER1RjRwbHdHT3RVeGNvX05fcVJDLUNDR1UwUm1CRGZqdHllU3RBYU56SXMwSEwtb0NQTVZqb2xkbDR1TXBaaUgtc1lnbE5zYmNvQ3hJWHRMc3dOZ29RSHhBRmhJTC0tQnlkU0tyU01WcGZqSENYWlVlckFFU05zclNvNFk4RDY0NG9QakhiWmNzblVDV2tXLThvaTlWZXNlMFdTZzEyUk9jVS1FZVNZemxUUEhCY1d3MkEzdk5aaExBQ3ZuSzFTU1gwYU5WWWNSRFNadnc3VGo?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 24 May 2026 09:15:00 GMT
- [輝達新一代 AI 平台 Vera Rubin 報到 電源、散熱鏈含金量大增 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE16LXJSNWVzS1hIQXlmd3lNWmVwXzdTQmhpcjhMTVpIenhHU3I2Tk5QaXVBc0hyZVo2em83VE95OUl1UVlwMUZUN0ZzM1hjbnNLb252WlFXREVYd9IBX0FVX3lxTFBuaVRLMy1fQno0VWxmS2I4bmlxdWVsWXJPN3Z0YXZ6OE94R2hYMjVuT0FWaTktVWF4eVFsY2t6bjdQbzF0R0tOdkxESXFLNTVGQmROZXRGRHppdEh5S2xj?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 23 May 2026 09:00:00 GMT

## 新興題材：SpaceX

摘要：新興題材：SpaceX 相關新聞集中在：Exclusive: Grok falls flat in Washington, undercutting SpaceX's AI growth story - Reuters；美銀示警重演「超級泡沫」！SpaceX、OpenAI、Anthropic IPO恐將美股推向歷史極端 - news.cnyes.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 新聞直接提及 | -0.56 | -14.93% | -9.08% | 418.57 | 506.69 | -17.39% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：新聞直接提及「OpenAI」，共 1 篇新聞命中。 方向判斷命中詞：恐。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Exclusive: Grok falls flat in Washington, undercutting SpaceX's AI growth story - Reuters](https://news.google.com/rss/articles/CBMiqAFBVV95cUxNYkVBeG83TF9qcjAxRjBDQ3FLR25nNUxtLUFFMmI3S01nSm5obzhLS2FMTDA3MDZTeEpRdGg0TWlCOERydWI4RWlaZVJYRVM4YmN3TVEzRkFBbmtxa2NwWm9OT0xJVjJPQnl3NEZFZzRsOUdGUU13MGNLVFRqTXJZcW93dGk5SGZORExyNjJiX2s3V0tab3Zra21XbGdkaGFiUU9ydFZfaGg?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 23 May 2026 07:00:00 GMT
- [美銀示警重演「超級泡沫」！SpaceX、OpenAI、Anthropic IPO恐將美股推向歷史極端 - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTE5JaTlIMTd4Wm11ZktTbHU0QmVYSDBwS181ZEhBbGVlSWpDT0dWV0drcjV4TmozN0lVTFJiRVlFRHlDeXdvZV85UXJSYXdfeEU?oc=5) - Google News source discovery | 鉅亨網 Sat, 23 May 2026 08:10:05 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：美貿易代表：半導體關稅重要但近期不會加徵| 國際 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +10.75% | +53.76% | 308.82 | 308.82 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | +2.04% | +0.60% | 250.00 | 257.50 | -2.91% | 不適用 | 14.13 | 17.76 | 832.10B TWD / 29.74% | 2026-05-01 |

關聯理由（前 3）：
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [美貿易代表：半導體關稅重要但近期不會加徵| 國際 - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5CMVJjNWxnemNEVHFVWTJJdjZyRDdlU05SVFBYb3o4UEZWZUpVTnVVdldfaFlVVzFSbl85dHp2WEY2YmtDcEhBRUxmVEUwZF9WU1N3X0gwR2RoN210Zi1Z?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 23 May 2026 04:23:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel Has Soared 225% in 2026. Here's Where the AI Stock Could Be By the End of 2028 - The Motley Fool；Is Intel’s (INTC) Confidential AI Push Quietly Rewriting Its Core Investment Narrative? - Yahoo Finance UK；Google 訂閱制策略對 AI 創作市場的影響？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.76 | N/A | N/A | 119.84 | 119.84 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | -0.04 | +23.47% | +12.66% | 215.33 | 215.33 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | -0.07 | N/A | N/A | 467.51 | 467.51 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.04 | +2.27% | -0.44% | 2,255.00 | 2,255.00 | 0.00% | 背離 | 74.39 | 30.32 | 410.73B TWD / 17.50% | 2026-05-01 |
| MSFT 微軟 | 產業/供應鏈推估 | -0.05 | -14.93% | -9.08% | 418.57 | 506.69 | -17.39% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.03 | +33.81% | +25.00% | 414.14 | 417.43 | -0.79% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.03 | +18.86% | +2.56% | 561.00 | 561.00 | 0.00% | 背離 | 10.86 | 52.09 | 62.25B TWD / 19.22% | 2026-05-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.03 | +22.35% | +18.40% | 3,860.00 | 3,860.00 | 0.00% | 背離 | 62.91 | 61.51 | 46.74B TWD / -4.14% | 2026-05-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel、INTC」，共 2 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Has Soared 225% in 2026. Here's Where the AI Stock Could Be By the End of 2028 - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxQcUdJV19KVU1vOGRaZVFiWEc3MVFJRmxXSlJDMVVrN1VteHpWdjROYkd3T1lXZTV3cVZWVXlmYkJvOEVVMmczYTJTOEtWOGNucTFwYzhHWjVFMlRiSGJlZG8teTBiSmhWVkV3UTh1NzdGQ0lPYkdDMVpsZjhadVdTV0wyNEpsV0QxVFIxYTRDWmdLWnBacEZvNg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 23 May 2026 20:49:00 GMT
- [Is Intel’s (INTC) Confidential AI Push Quietly Rewriting Its Core Investment Narrative? - Yahoo Finance UK](https://news.google.com/rss/articles/CBMihwFBVV95cUxQUWViU3lKZVVmTU9Cb0tiOXBudWJUQVpkQXZnb0FBRmNpSWRnOWhNaDFfM29nQjd3cXRUdlEyZUpveW15c0tyWkZHQ0xWa2FiUVVRdkhidTdaTmNwd0dFeXdNTWV2ZUsydGxWNVJfTzV3aFlWNXhrS0ozb3dua1VsMXJMM3NQY0U?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 23 May 2026 15:11:55 GMT
- [Google 訂閱制策略對 AI 創作市場的影響？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMid0FVX3lxTE1Zb3JyTmNMbXNDSzhOYTRmWE5YSmZzQl9pMGc2RktHYUgxRzRhZWpDTTNBWGdfNTJOcWg3dldhRE5PWnZ3N0E2UVFXZ0NHQVdDTXVZbUFVSEpGOEM5NFVjUUNHLUNnOUdvcDVMYkp5cHBRUG9DVlpF?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 24 May 2026 21:19:24 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：投資觀點-台股年漲9成掀融資買股潮，借錢進場，必做4項財務體檢 - MoneyDJ理財網；進出明細表 - MoneyDJ理財網；理財行事曆 - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [投資觀點-台股年漲9成掀融資買股潮，借錢進場，必做4項財務體檢 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMijgFBVV95cUxNOHNXRTZqbnh1M1dfUHEwS2VSRGVzNXhDTzd4OFcwNV92Vkx2cDBpenRlTmM3X1AyTnUyMjlsU3BlTFQtZUg4c2M2REh5WUlYY05maDBNdWlUaUVtNWlDUzRnb010YnVaTXhvSWV4RDhHX2dmMVNjZE5pR0ZKdHE3SzJYNXhKTGNTX3hrdUFB?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 24 May 2026 16:10:25 GMT
- [進出明細表 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMijAFBVV95cUxPbWE0eDlrYmhNby15STNRRkRUWHFham1WV2dzcUdjaTJabzNUeFItTjJaRnJGeEcyV2xXYTFRcXktWmNtRTRwVi15NUdZNjg1TzhUMTE2bGR6Z3U4WFpaWnpjQWFHUWJRRWlyV3htZ0RSbTZBUmN1SjBhYVVGTTJ2Tkc3eUl2ejJJTnhfdQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 24 May 2026 10:44:59 GMT
- [理財行事曆 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMieEFVX3lxTE1SWTNwd0V2MWJiY2pNSFdMVW9fQmZxb045MUFoN2tKLTNLclJqUUQ1WmtKMnNsZ1RRXzNTUUUyWmxjejVlSFRRMV9BQ3lCX01pczFWTl9EaHJ2OUZpVTJuRjZjSzRCZVE4T25TdTVXNkY2cldnanU0Zw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 24 May 2026 07:04:59 GMT

## 新興題材：半導體關稅

摘要：新興題材：半導體關稅 相關新聞集中在：美貿易代表：半導體關稅重要但近期不會加徵| 國際 - 中央社 CNA

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [美貿易代表：半導體關稅重要但近期不會加徵| 國際 - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5CMVJjNWxnemNEVHFVWTJJdjZyRDdlU05SVFBYb3o4UEZWZUpVTnVVdldfaFlVVzFSbl85dHp2WEY2YmtDcEhBRUxmVEUwZF9WU1N3X0gwR2RoN210Zi1Z?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 23 May 2026 04:23:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
