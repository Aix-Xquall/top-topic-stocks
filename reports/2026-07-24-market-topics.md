# 每日股市熱門話題分析 - 2026-07-24

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜中性｜熱度 6｜市場確認 N/A｜同向 0/0
2. **AI 伺服器與資料中心**｜中性｜熱度 17｜市場確認 41.13｜同向 3/6
3. **關稅與供應鏈轉移**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
4. **半導體與晶片供應鏈**｜中性｜熱度 5｜市場確認 N/A｜同向 0/0
5. **散熱與液冷供應鏈**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.16（樣本 6）
- 5日相關係數：0.43（樣本 6）
- 同向比例：3/6

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 41.13 | 3/6 | 3 | +2.04% | +3.18% |
| 關稅與供應鏈轉移 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：OpenAI | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
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
| 2026-07-24 | -0.16 | 0.43 | +50.00% | 6 |

## 歷史回測摘要

- 回測日期：2026-07-24
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

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Why Micron, Sandisk, and SK Hynix Are Surging—And How to Play It - Benzinga；Micron and Sandisk Are the Biggest Dark Horses as Chip Stocks Roar in 2026 - NAI500；Prediction: Micron and Sandisk Stocks Will Both Plummet After July 30 - Yahoo Finance

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 990.21 | 990.21 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | +15.77% | +14.12% | 1,610.33 | 2,335.00 | -31.04% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | 0.00 | -1.13% | +19.70% | 208.76 | 212.06 | -1.56% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 5 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Why Micron, Sandisk, and SK Hynix Are Surging—And How to Play It - Benzinga](https://news.google.com/rss/articles/CBMi1AFBVV95cUxPNVlvZjVOWGMyQjBSSFZYMEJqaGxVUkduQzRWemp2TDR2MHk3WmlHbHJKeUl5elJFR3VORDhDbGNibXFBZE9GY3ZacW1pMUVCYWtGcUItckhYVG9QTk5jNGNiM2dGam1KX3F1SVRQQkoxWUxrTUJYd2dCRlA2OTRoSFhFWlhfd3FGODZrVDhSMWZfS2tidE5mV1M1MVdxdkZKVUdtVlVHelBnX2laTkFLeU9wYk1OdkxXUUlYTjcwNmQzVUM5aUdiV0RQZ3dEMGdTZWJGcA?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 23 Jul 2026 09:40:22 GMT
- [Micron and Sandisk Are the Biggest Dark Horses as Chip Stocks Roar in 2026 - NAI500](https://news.google.com/rss/articles/CBMiqwFBVV95cUxQb1NHb0RPTlNYOFJHZzFsSHhONkZ0TjEwbV81ZGplTWhYV2RWSGUzZU5HWkZPRGtCYlJkVDJTWTE4MVh4UmVCdFdfeGI4LXhucEhvUGc1eVVfQlllRm9YVDB6MkJhRTV3MmlyZWNHUXE0cmZVTEVkS3k0eXNpbXZZdFBjSFEtQ0JpX1pTZ3ptQ2I3aXZmOVI5MjZpOW81ZVJyWGhQOVBzSkNiYUk?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 23 Jul 2026 13:11:38 GMT
- [Prediction: Micron and Sandisk Stocks Will Both Plummet After July 30 - Yahoo Finance](https://news.google.com/rss/articles/CBMipAFBVV95cUxPbEt3dnpOTG1aSGNob1Q2UnktdGtZRGstX085V2lIVnRWNjZvc1pWaUd0eEYtV1pBSkZOYWg1X25FVDUtMWdKaFNfX2xieDNITmQtazRfYjBMUGN6dXNtVnI5N3hLUzFjVzkydzhiVUVwSEpoMlZjcDdkWnJUaWcyWklxckp4ZmkzcVVvRWdNYXlhM0dlSUdDNGhtQVpUajNUN2dSVg?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 22 Jul 2026 11:05:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel's stock jumps 11% as chipmaker rides AI boom to fastest revenue growth in almost 15 years - CNBC；Intel forecast crushes estimates as AI boom boosts chip demand; shares jump - Reuters；Intel Stock Jumps as Earnings Blow Past Expectations Amid Booming AI Demand - Investopedia

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.59 | N/A | N/A | 100.23 | 114.68 | -12.60% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.28 | -1.13% | +19.70% | 208.76 | 212.06 | -1.56% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.54 | N/A | N/A | 539.69 | 552.33 | -2.29% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.06 | +3.66% | -2.63% | 2,405.00 | 2,410.00 | -0.21% | 同向 | 74.39 | 32.33 | 442.68B TWD / 67.87% | 2026-07-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.02 | -2.84% | -24.69% | 381.58 | 506.69 | -24.69% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -12.15% | +26.80% | 392.47 | 446.77 | -12.15% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.04 | +8.71% | -4.84% | 649.00 | 680.00 | -4.56% | 同向 | 10.86 | 60.26 | 65.78B TWD / 32.86% | 2026-07-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.04 | +16.02% | +4.73% | 3,875.00 | 4,310.00 | -10.09% | 同向 | 62.91 | 61.75 | 58.01B TWD / 2.80% | 2026-07-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 5 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。 方向判斷命中詞：growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。 方向判斷命中詞：growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel's stock jumps 11% as chipmaker rides AI boom to fastest revenue growth in almost 15 years - CNBC](https://news.google.com/rss/articles/CBMie0FVX3lxTE5OTVp5cW4xMmFTWkxNc1dUYkx0bFFYTGZhWURkWFNwT1NIcUxPUjVmb1dTU2hWcFBHd2dGVTA4alZFbDhDY0NScWJ4OVh0ZzVKRENFSW9CVkh4UTc0VGR3dEg4X1ZwSFhmZDhoLTNTRTdZY09XQWJuYlI4TQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 23 Jul 2026 20:03:07 GMT
- [Intel forecast crushes estimates as AI boom boosts chip demand; shares jump - Reuters](https://news.google.com/rss/articles/CBMivgFBVV95cUxNY1JRa3lMd0xIRC1RRGxjWWFMTmZqYmtPMnV1ZXlURS1KX0dQOFRRMXNhbDMwV0NieEhCYkc0QjNlVGlCSnE3OGYwZ1lUR1ZuTndhR2RBNVBxNnFnN043Z2NZM1BiemNBSUNvT3RRc1hSM0o5WjB0MTNkampodGcwSVFndUJwLWdaRXRHZHFKbzdNZFNNT245SHczYjdTX2NBVC0xNS1HcHc0Y1V6ZTFmQzMwcG1FR1NIUHVldlZn?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 23 Jul 2026 21:05:40 GMT
- [Intel Stock Jumps as Earnings Blow Past Expectations Amid Booming AI Demand - Investopedia](https://news.google.com/rss/articles/CBMiugFBVV95cUxPWndUSWpUTkFDbXBDS2UyR09oQkNNOV9ZOW9qZTBiVXVGZlZNTlhXNXpoQTZzeWwtZHo1Z2hsZVljTzZ3eXJheGNEeG5Ca3lQbXZDdDZmeXJ5MnBlTTl0Mmdaa1lCM0xxalNjcXBnUl9mdzdjLWtGS3pmYnZMc3dKVW1YRFZlQm1EcVlQVVk2aDJWNENYTThwRFhHQl90LVIxN0k4Wkg0RHY5ckRhbXNfNGtNenAtRjNvOHc?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 23 Jul 2026 21:54:32 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：無人載具拚產業國防齊強化 半導體傳產打入供應鏈 - 中央社 CNA；賴清德提三核心戰略推動離岸發電發展、產業供應鏈及人才培育- 要聞 - 工商時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +21.76% | +38.56% | 321.66 | 325.89 | -1.30% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | +9.81% | +6.19% | 257.50 | 289.00 | -10.90% | 不適用 | 14.13 | 18.29 | 821.76B TWD / 52.11% | 2026-07-01 |

關聯理由（前 3）：
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [無人載具拚產業國防齊強化 半導體傳產打入供應鏈 - 中央社 CNA](https://news.google.com/rss/articles/CBMiU0FVX3lxTE5VSEZLSzkxZkJoYVQyYWphczVGc2lyWUpJV0czRXFzR2QyVnRrVDgxVnhBUDIzVW94UGx2MWZ3NUp2clFrdExzQjBMc0ZfZWUyQUVN?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 23 Jul 2026 09:49:55 GMT
- [賴清德提三核心戰略推動離岸發電發展、產業供應鏈及人才培育- 要聞 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTFByZ2ZXMTdTdUlJY0dIc0lKMU54RnJrZzkzYUlyVjJqQ1J0TXpZS0NubldNbVc4NGZuU2JPNFVJTVNCRWd5a3JWbGVUcEs1SjBEMGNJRFExVW5HOFpnT3Jv?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 23 Jul 2026 08:41:00 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel forecast crushes estimates as AI boom boosts chip demand; shares jump - Reuters；Nvidia vs. Intel: Which is the Better AI Chip Stock to Own for the Next 3 Years? - The Motley Fool；AI淨零／ 台鎔科技看好半導體廢液處理 上市首日收漲近2成 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 100.23 | 114.68 | -12.60% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | 0.00 | -1.13% | +19.70% | 208.76 | 212.06 | -1.56% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +3.66% | -2.63% | 2,405.00 | 2,410.00 | -0.21% | 不適用 | 74.39 | 32.33 | 442.68B TWD / 67.87% | 2026-07-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +6.54% | -13.44% | 138.50 | 164.50 | -15.81% | 不適用 | 4.00 | 34.80 | 23.12B TWD / 22.85% | 2026-07-01 |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 539.69 | 552.33 | -2.29% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 990.21 | 990.21 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | +15.77% | +14.12% | 1,610.33 | 2,335.00 | -31.04% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -12.15% | +26.80% | 392.47 | 446.77 | -12.15% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 2 篇新聞出現相關標籤。

### 主要來源

- [Intel forecast crushes estimates as AI boom boosts chip demand; shares jump - Reuters](https://news.google.com/rss/articles/CBMivgFBVV95cUxNY1JRa3lMd0xIRC1RRGxjWWFMTmZqYmtPMnV1ZXlURS1KX0dQOFRRMXNhbDMwV0NieEhCYkc0QjNlVGlCSnE3OGYwZ1lUR1ZuTndhR2RBNVBxNnFnN043Z2NZM1BiemNBSUNvT3RRc1hSM0o5WjB0MTNkampodGcwSVFndUJwLWdaRXRHZHFKbzdNZFNNT245SHczYjdTX2NBVC0xNS1HcHc0Y1V6ZTFmQzMwcG1FR1NIUHVldlZn?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 23 Jul 2026 21:05:40 GMT
- [Nvidia vs. Intel: Which is the Better AI Chip Stock to Own for the Next 3 Years? - The Motley Fool](https://news.google.com/rss/articles/CBMilwFBVV95cUxQOFVKRTRYbWdrV09HQ2gzLVhCZ1pUWHVOWS1rWndJM2hqaDl6TXdWN1g0TUQxSHpOYUdYLXZ0Q01hOWpud2VLVUh1bkZFeXFBZ3ZTMTV2ZGxJd0JWZi1aVExDdkRrczREcXZKWGtYZEdWbXYycXR0Wnh6dUhoZmt6VV8yalFEd2xZcFpXNjN1eWd5V0wxbUtn?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 23 Jul 2026 13:46:00 GMT
- [AI淨零／ 台鎔科技看好半導體廢液處理 上市首日收漲近2成 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTFBjdmFRblpTVnd2cVNIV3luZjk4b3hRbWtXWlJfTkxiZWR0LW93UHVlTXM2NlgtbWprMjQ2MnNGMTU1TkVhV2tfUVJsWnl4ZzZ0OXlTakZqRGtDWEp0RVE?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 23 Jul 2026 07:58:00 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：《價值型投資最新產業研究報告》雙鴻（3324）、奇鋐（3017）AI伺服器升級，液冷散熱需求持續放大| 台股 - 鉅亨號；焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | +14.29% | +9.66% | 2,440.00 | 2,835.00 | -13.93% | 不適用 | 61.06 | 40.09 | 17.62B TWD / 66.11% | 2026-07-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「3017、散熱」，共 2 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：跌停, 升級。

### 主要來源

- [《價值型投資最新產業研究報告》雙鴻（3324）、奇鋐（3017）AI伺服器升級，液冷散熱需求持續放大| 台股 - 鉅亨號](https://news.google.com/rss/articles/CBMiSEFVX3lxTE0wTlp4U2djVXZjY3BZdFNpQ2VZaDkwa3JFZEtmXzN4eTRWZnVicU9GdDZpN19LN09ac3FaUDNQV05oUW95TnpDXw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 22 Jul 2026 03:33:55 GMT
- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 23 Jul 2026 04:51:35 GMT

## 新興題材：OpenAI

摘要：新興題材：OpenAI 相關新聞集中在：White House monitors OpenAI's 'rogue' AI incident, lawmakers propose 'kill switch' - Reuters；OpenAI's Hugging Face hack triggers 'AI Kill Switch' bill in Congress - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 新聞直接提及 | 0.00 | -2.84% | -24.69% | 381.58 | 506.69 | -24.69% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：新聞直接提及「OpenAI」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [White House monitors OpenAI's 'rogue' AI incident, lawmakers propose 'kill switch' - Reuters](https://news.google.com/rss/articles/CBMipAFBVV95cUxNRnhrdU9BTTRoNGhtSV9RbmlUT21SMkxiRHZuTU9vdnN2NjZodU1iVjEyMWdVQmQ1OGVKalFXOHRuUFBWNzZaejdwc3hLRE05TzBOcmpNeF83SmlVU0MwNThMZk9aZDBYSFhhNjRMNWxuNndFbHhCdnFnMnhEQTVBVE5QYzkxUllpOEw4U1pBSjFjeHljaXVVcXdOWGF0TUU1cnl3Wg?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 23 Jul 2026 21:44:05 GMT
- [OpenAI's Hugging Face hack triggers 'AI Kill Switch' bill in Congress - CNBC](https://news.google.com/rss/articles/CBMikgFBVV95cUxQWVhNdF9vVVNEUk5pRXdrZkFZNkU2WXA4MDJqSEVUOVhZaFYzZ0dKTUxvWTN5Z21CTzlNYVZXTF9ieTdLQkVWODQtTE51RTFpYzk2TjdoX1QwbUVtVmo3TktjX2pRZURaSVVQdVYyYTJQZk5raHRVOHMwNzMzLUF5dzZSamdxa3kwN3BZTVFSWGJpUdIBlwFBVV95cUxNX1dIYVZvcmZINEoxVjVJdnJOYUtoRGQwMGcteFV5a1NKU2huSkdYaE1DNFdQTjc2NmluNWg1Smd2UGRSbnpUQUpfeVdBOHJSVUs1SFRhc1JUaUZ6RVN0ckdwdDh6eTdJUnBOdU56V0Y5WUVIMWRCUHk3ZlF2c2x6ZmNlbWNGRTJoWWkzQ1pKakY5SHhrbmE0?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 23 Jul 2026 19:51:08 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股跌602.39點 - 經濟日報；證券劃撥餘額增速雖放緩 央行：台股三指標 熱度不減 - 經濟日報；台股又大跌了！不過這個族群逆勢揚 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股跌602.39點 - 經濟日報](https://news.google.com/rss/articles/CBMif0FVX3lxTE5WQmJqdmRwSE56bmJIc09UM3FMenFqYlo2WXB4bThzZXk2UmtHWkFTN1NOa3RpNl80NmJmdXZtUUoxTTZlUGNYSVNzSTdMOUlmNEdSeWxOUElvbmJUcnh6UkZ2WS1xR1ptdUpYaXJLZmZIald0cW84YzV2d3hCRk3SAV9BVV95cUxNcGV2QnJvVkZiYUd6NGVHMHVEdjNZWG5PWnBHUXkzRFk3MkdBd0dsLXQ0QVd1eEF0d0dXdkRwM0NVX3FNNmtOTmE4T3RaOU45OFdMeUZ3UFlEbEs1RjBxdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 23 Jul 2026 20:41:54 GMT
- [證券劃撥餘額增速雖放緩 央行：台股三指標 熱度不減 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1GNHlLOVMwYkh2Tkp3VE9MdzNYSnVGUnBIRlU2c1ZBNlVxVFVUd0JndUZubjhHa1VSb04zcWlrUVpqZ0xrYmR3NGNISjhzc1o3dWNwb3paalpFd9IBX0FVX3lxTE1neE5JYTQ3NE9rX2tPUnRTbmhwU3ZyU1ZraUg4UHowSl83VzZ4OGJIMWxfWmxST1JiVnk2Q1ZJeU9MNGNfZEVDRlMxa1lsdVNReXpIUjFPQWg5cktFNm04?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 23 Jul 2026 17:44:14 GMT
- [台股又大跌了！不過這個族群逆勢揚 - 經濟日報](https://news.google.com/rss/articles/CBMif0FVX3lxTFBmNmlibi1nVnFRd0p6RUdLUlZCbTdSOVZYXzVpQkxEUHdEajB6ajlETldOQkF1X3lnbVYzQXhBNFFqaDBoR2poeDEtdmVUSll5enBlV2NSQ2l3cm01RlBTb21LU1pJaEJFaEVmNG5vcTBNWVB2YVZtVDZ2V0RZazTSAV9BVV95cUxPZTlnN2RZeVN4cjIyMmVERTJodGlzZEVmUFBVVGQyaXpuUklUdmZzSm1Fd1AtVTE2b09IMDZpdUE0a0E2WlRST2Q0eFdKc2pjc25uR19iLTdEZVpKTm04QQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 22 Jul 2026 09:00:00 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：【台股操盤人筆記】籌碼最壞時刻漸過，企業獲利支撐台股反彈 - MoneyDJ；個股動態報導內容-22025B28-6909-4A2D-A76D-C01D57815877 - MoneyDJ；《台股盤後》台積拉尾盤、小漲25點；45K得而復失- 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [【台股操盤人筆記】籌碼最壞時刻漸過，企業獲利支撐台股反彈 - MoneyDJ](https://news.google.com/rss/articles/CBMilwFBVV95cUxPMFp3WHFJTXduWVYwQTZMeHZ4eTNKRlBGaG8yNWJ5c0VWTFZRMVpHOGRxZHFoY2dheVNJN0t5b3V6d01JcHRsNTJOMktOdHlOTXo3LVN1bXZUNWpDaFBuWmJkLXFaUTl0Q1k2V2hqRVRROTFydGNlLS1FLVJoeGR1dEk1dl80MzdPMHRHSHlOUm0zT3RkNWFB?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 23 Jul 2026 02:48:00 GMT
- [個股動態報導內容-22025B28-6909-4A2D-A76D-C01D57815877 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxPRHVxYzhicFBiME9VV19OeW9EcExrZEVHRTYtMWx4aWdOOE82ZFhkN2ZuQ2RFd01la3JsdW9hYmtMUllPckgyeGRNLXFETjV6cFh3eHFWelRQVVYwdXNwZFQ5cVd0U2Q1cE1fQTJJSFhmblY1T2d5aVdwbnRkU2tiMEl3Y0psWTl5dFg0Ylh0Y3hnd0xP?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 23 Jul 2026 11:14:12 GMT
- [《台股盤後》台積拉尾盤、小漲25點；45K得而復失- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQd2hubEdhWWVtNUVzWnQ1Q0FncXBuT0NWbTU0UkFnZ191Q3VhZ2NLNDc0MGlaVThPcDRxWldMU1h0Z0lYWFNtV2M5dnk1ei13ZkNjamMyUEdabERFNC1Mc0VrRHEyWlIxSnVVR1VrZ1VnZi10aUI2TUx5alAtWkhVelRsZkY4R3VkUTRRbTF1STdZUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 23 Jul 2026 07:48:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
