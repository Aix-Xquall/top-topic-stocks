# 每日股市熱門話題分析 - 2026-08-02

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜正向｜熱度 3｜市場確認 100.00｜同向 1/1
2. **半導體與晶片供應鏈**｜中性｜熱度 4｜市場確認 N/A｜同向 0/0
3. **新興題材：OpenAI**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
4. **散熱與液冷供應鏈**｜正向｜熱度 3｜市場確認 41.24｜同向 1/2
5. **AI 伺服器與資料中心**｜負向｜熱度 18｜市場確認 0.00｜同向 1/6

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.06（樣本 9）
- 5日相關係數：-0.21（樣本 9）
- 同向比例：3/9

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 100.00 | 1/1 | 0 | +10.83% | -15.43% |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：OpenAI | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | 41.24 | 1/2 | 0 | +2.08% | +5.39% |
| AI 伺服器與資料中心 | 0.00 | 1/6 | 3 | -4.33% | -2.56% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：A9B8290B8FFD | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-07-20 | -0.59 | 0.11 | +45.45% | 11 |
| 2026-07-21 | -0.12 | -0.03 | +12.50% | 8 |
| 2026-07-22 | -0.33 | -0.15 | +16.67% | 6 |
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

## 歷史回測摘要

- 回測日期：2026-08-02
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

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：MU, INTC, SNDK: Chip Stocks Rally After-Hours On AMD’s Blowout Report - Stocktwits；SanDisk Is Down 45% in a Month. Should Memory Investors Switch to Micron or SK Hynix Now? - Yahoo Finance；Prediction: Micron and Sandisk Stocks Will Both Plummet After July 30 - AOL.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.48 | N/A | N/A | 823.03 | 971.00 | -15.24% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.48 | +10.83% | -15.43% | 1,214.83 | 2,335.00 | -47.97% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.36 | N/A | N/A | 476.15 | 516.10 | -7.74% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.36 | N/A | N/A | 90.20 | 114.68 | -21.35% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +0.59% | +13.30% | 200.75 | 211.14 | -4.92% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron」，共 3 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK、SanDisk」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [MU, INTC, SNDK: Chip Stocks Rally After-Hours On AMD’s Blowout Report - Stocktwits](https://news.google.com/rss/articles/CBMiygFBVV95cUxPeVlYaXJjQjNtTkNRQUxQTHhaLUFMbE80Uy1MeDBpV0FPdkg2SHRLdkdfVUpXM1NrNWhZSVZQQ01sa0o4T1hKdzF1clBFRlRWUmMwWGxQTDNVVFBpOVhObUc2MXpBeXBOZ0p3R0w5NGRNOHB4X0ZIXzhlT0NMbmhzc1RtdmJRTWhlRUhKSHpyVnpaU0VGMlJyU2tDcmdkTG1hWVJJbmtTVDREbzFfWDB4bjhuTGswN3lmdkdHQzY1dzFOVU41VGlBNlZn?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 31 Jul 2026 00:45:00 GMT
- [SanDisk Is Down 45% in a Month. Should Memory Investors Switch to Micron or SK Hynix Now? - Yahoo Finance](https://news.google.com/rss/articles/CBMimAFBVV95cUxNcERka09icWV3QWRzQTI5RllWRmJPZ3dzVk8xcGNiVUdJRTFEYXdRaEFENlhfbHdrT0pSQWFPUWtlakZCNWZxVzlxUnplOUFNQmJpYmU3eDZOX1MtdzNqci1tOWdyNEZFTUpXZ3FXU2tjRXVWQ1dhNDJES3hMV0hiOVNJc0xSN2RJQ3B4R01uVy0ySzRXUUZpSQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 31 Jul 2026 18:36:06 GMT
- [Prediction: Micron and Sandisk Stocks Will Both Plummet After July 30 - AOL.com](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPd3FPNU9EQ0NyQW5nSmVVTDQtbnhHNjd5MmhXaDk3eE5LRUFYR0tNRkNUNDBGZ3A0NnFlRHdXSFF0TnJoa3VxbUVxM3hEMDZyaVpRZl95ek1sYW93QmktdGFiWHloODVTY1Q5ZnpSZEswUVpiMXA0S2ROSmtMaDdGRkExY2xqWXE5?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 31 Jul 2026 09:28:48 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel (INTC) Faces AI Supply Bottlenecks As Omdia Sees 94.1% Chip Revenue Jump - simplywall.st；SEMICON West長期移師鳳凰城延續半導體生態動能| 產經 - 中央社 CNA；5 分鐘無縫轉移，如何強化半導體韌性？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 90.20 | 114.68 | -21.35% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +6.36% | +3.19% | 2,425.00 | 2,425.00 | 0.00% | 不適用 | 74.39 | 32.60 | 442.68B TWD / 67.87% | 2026-07-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +6.61% | -5.47% | 121.00 | 164.50 | -26.44% | 不適用 | 6.68 | 18.20 | 23.12B TWD / 22.85% | 2026-07-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +0.59% | +13.30% | 200.75 | 211.14 | -4.92% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 476.15 | 516.10 | -7.74% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 823.03 | 971.00 | -15.24% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | +10.83% | -15.43% | 1,214.83 | 2,335.00 | -47.97% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -6.74% | +21.82% | 389.28 | 446.77 | -12.87% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 1 篇新聞出現相關標籤。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 1 篇新聞出現相關標籤。

### 主要來源

- [Intel (INTC) Faces AI Supply Bottlenecks As Omdia Sees 94.1% Chip Revenue Jump - simplywall.st](https://news.google.com/rss/articles/CBMiygFBVV95cUxPV2tYNU9MaW0xTGROOW5vNHNOaUt0dm9hRmxWSF9XcGNPNEJRMC1HaFpOWFp6cjl5dllxYUhqeWNnc0ZCaTJWejRwdl8ySzFOd3FnbUxZUDZLMlZNR2VXYmFyZE5QR01Oa3Q3WjlTZk9pRnUyM2FBb1JFRE5uREw0TmJTSWJVUWlmdHhjRXdrQXhBdHB1NnItOVJ0OERXTHdwSEFHMHNZT3ZxM0xkck1qSkZsSEZmckpNajJSQTdKZExhYmcwMXpmbE1B0gHPAUFVX3lxTFBpSHBmLXMwTUFOcVBwREg5bGRGd3Bod3BEOU1KSTJiTnN3Mm83T3cxbnZtYWtLbGFQc3dxcGxqMUZyLTVfV2J6MGxEejhrSGdjd1NVRVRtX0Q2WUdHMkhlYk10R3paeXgyclBMUnp6SHNHUXlmc3ZfdHBZSVNNLVlVc1pYX214cGdYRVlDWmtuaTRLNndyWXpTZTBmcFVkd1hMdURPNjBqcW1TUm5zcHczQ1JKeVZRWWUwOThUekdEMTlRYlZMSkR3M1hDS2ZTYw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 31 Jul 2026 12:25:39 GMT
- [SEMICON West長期移師鳳凰城延續半導體生態動能| 產經 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1iVGZUZnlWUWx0dWdlSXBxb1E4c2ZELXg1UGphMlZKNUd0QW95WnR6eVVkbHFTQlZSUm9qbkwxTDVGTC1sTW5NdVFNaW9MdG1oc3BqRlp5OG93MEE5MVE?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 01 Aug 2026 03:51:00 GMT
- [5 分鐘無縫轉移，如何強化半導體韌性？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiW0FVX3lxTE90QVg3ZnI4UlRsUDhkeVY0OGp3Tzdzb0hIdGM0WHlHRm8wZzlvaG9oUGVuT2I4LWE0cWZISVVOVEk4R0NmcndLOWZvYThNcTZqdEJKNlc3UGNfbDQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 01 Aug 2026 17:08:22 GMT

## 新興題材：OpenAI

摘要：新興題材：OpenAI 相關新聞集中在：EXCLUSIVE: OpenAI finds evidence other AI agents escaped containment as it widens hacking probe - Reuters；OpenAI's Hugging Face hack confirmed months of AI cyber warnings: 'Pandora's box is open' - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 新聞直接提及 | 0.00 | +18.33% | -8.28% | 464.72 | 506.69 | -8.28% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：新聞直接提及「OpenAI」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [EXCLUSIVE: OpenAI finds evidence other AI agents escaped containment as it widens hacking probe - Reuters](https://news.google.com/rss/articles/CBMivAFBVV95cUxQYTc2SUhrNmVER0NvNW9nZHBwbklFMlA0eTNSRFZETXpfSWpVYU1wOUhaMDRLUnRVSEhtRzByeEktX2FEX1ZzaThNMnpZMW9JdVZDZkVRTEQ4UjdlakFPVXZTUjZaM2JOUkhpN1BxeEU4bWJuSjNkUldBNXRVWDkyYWVXVUlKM0VEZU5wZklfX2FJRkQ0bmVybTIyY0xpbHd6aGtIVmZ3YU5ocGdsdFlNeXdOQlBXOUsyZnZtZA?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 31 Jul 2026 20:16:00 GMT
- [OpenAI's Hugging Face hack confirmed months of AI cyber warnings: 'Pandora's box is open' - CNBC](https://news.google.com/rss/articles/CBMigwFBVV95cUxNcmdXeDhvOWhnMk1CdEVPQ1l3SExjSl9Yd1dNWlpVS3U0WU9ta2EwM1U4REJyanh0QXVOZUdiXzVNYWJfazdzOG91VEFYS0o2eXBXNnQ4WVNjWEZ2T0xCaXpDaUkwX1VXamh2by1seFhGSE1McW1INDl5MnVBakdia3czNNIBiAFBVV95cUxPckY3OG1rcGJyWTBzdC16bGloeExwRmVVcmI3b19YQXZnSE44T0k1bzRuc0x0cXZ6SDRxQUZHQmdGeHZ3a0h0SS1pWl9NSlFZcHZubzY0eU50cldpT1QwOHNHaTlSNm1MV2d6N0tSQ2VjZWY1eWVXck93dUF3Z0VYRXBnbHI5dkdn?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 01 Aug 2026 12:00:01 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：5月EPS攻8.03元！「液冷散熱大廠」股價漲停鎖死 輝達Rubin、Google TPU放量業績走強 - Yahoo股市；焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報；800G、1.6T與CPO也導入液冷　它受惠Blackwell放量，法人目標價最高喊3,610元 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.51 | +3.57% | -2.52% | 2,320.00 | 2,835.00 | -18.17% | 同向 | 61.06 | 38.12 | 17.62B TWD / 66.11% | 2026-07-01 |
| NVDA 輝達 | 新聞直接提及 | +0.32 | +0.59% | +13.30% | 200.75 | 211.14 | -4.92% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 2 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：跌停, 放量, 漲停。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：放量, 漲停。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [5月EPS攻8.03元！「液冷散熱大廠」股價漲停鎖死 輝達Rubin、Google TPU放量業績走強 - Yahoo股市](https://news.google.com/rss/articles/CBMivAJBVV95cUxPUC0zRGZSdUIxZnN6WGRrU0JXc3B1ODdIaDhwaF91T3AwZUp6SG9adVBHbFRpaHRfQk43ZE1MM192bFctV3pydGZxOFYzcGxucm5CMGVXRE52YmU5Sm5lVGlkS1hrOWpMMVc1M3NkcHlmRVNtYTFRckl4WUdneXNtNXRKTjlWcHRGZ2dvMVFvZzZpc2FvcllSQU9hVE9RbGpoTXhNcGloR2xmY0NINWlXS1Z4aXB3SmJVMGlLdzF4MV8ydUNoeHVxS3NweFN6OE42b2syNjRDY25HemNGek9ISTVoVlJMeGItdVVzQ3VsbU50UnRLQlF5RHR6N0FGNUdCbjA3MDVRcXRlUi1Qb0p1M1pYc2M1SEJVU21VLXZTS3ZNQ3VyNDJucHV3eElJZnBMbUJVdjNxd3hhdzhW?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 01 Aug 2026 09:30:00 GMT
- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 31 Jul 2026 14:03:07 GMT
- [800G、1.6T與CPO也導入液冷　它受惠Blackwell放量，法人目標價最高喊3,610元 - 經濟日報](https://news.google.com/rss/articles/CBMikAFBVV95cUxNX2tpNjZPOENOcl83dWx4MFBWTXNVV2dfaWF5clM4ZnMxb2ZZRTJCN19QMWFtY3hSYXNPS2ZBLXdESk5TYUlRWlIxS0Y0eTVVUXlPUW1xV2JlSnhuVXJGNUpFRzJkbmVoS0p6dFFyMVdUTjBYam8wekRwNzF3azUxVHlEWC1FMmVwbzZBVGNmNGHSAV9BVV95cUxPdEppYXRNaFJUa2dma3QzcFZUcXZWV0pEWEVQdDFlaElSWjBDNlZxTjZpQUI1YUFGb2sxOVAxNmVlVTR3Rkwxd2RqX1F3LWwwSGIzV0RtTFRVWko0RDVCaw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 31 Jul 2026 15:15:16 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel (INTC) Faces AI Supply Bottlenecks As Omdia Sees 94.1% Chip Revenue Jump - simplywall.st；語音 AI 的「自然插話」機制，對使用者信任感有何影響？ - TechNews 科技新報；超低延遲推論技術的突破，將催生哪些新型態的 AI 商業應用？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.54 | N/A | N/A | 90.20 | 114.68 | -21.35% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | -0.04 | +0.59% | +13.30% | 200.75 | 211.14 | -4.92% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | -0.06 | N/A | N/A | 476.15 | 516.10 | -7.74% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.03 | +6.36% | +3.19% | 2,425.00 | 2,425.00 | 0.00% | 背離 | 74.39 | 32.60 | 442.68B TWD / 67.87% | 2026-07-01 |
| MSFT 微軟 | 產業/供應鏈推估 | -0.02 | +18.33% | -8.28% | 464.72 | 506.69 | -8.28% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -6.74% | +21.82% | 389.28 | 446.77 | -12.87% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.03 | +0.18% | -9.46% | 555.00 | 680.00 | -18.38% | 未明確 | 10.86 | 51.53 | 65.78B TWD / 32.86% | 2026-07-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.02 | +7.24% | -5.20% | 3,555.00 | 4,310.00 | -17.52% | 背離 | 60.69 | 58.71 | 58.01B TWD / 2.80% | 2026-07-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel (INTC) Faces AI Supply Bottlenecks As Omdia Sees 94.1% Chip Revenue Jump - simplywall.st](https://news.google.com/rss/articles/CBMiygFBVV95cUxPV2tYNU9MaW0xTGROOW5vNHNOaUt0dm9hRmxWSF9XcGNPNEJRMC1HaFpOWFp6cjl5dllxYUhqeWNnc0ZCaTJWejRwdl8ySzFOd3FnbUxZUDZLMlZNR2VXYmFyZE5QR01Oa3Q3WjlTZk9pRnUyM2FBb1JFRE5uREw0TmJTSWJVUWlmdHhjRXdrQXhBdHB1NnItOVJ0OERXTHdwSEFHMHNZT3ZxM0xkck1qSkZsSEZmckpNajJSQTdKZExhYmcwMXpmbE1B0gHPAUFVX3lxTFBpSHBmLXMwTUFOcVBwREg5bGRGd3Bod3BEOU1KSTJiTnN3Mm83T3cxbnZtYWtLbGFQc3dxcGxqMUZyLTVfV2J6MGxEejhrSGdjd1NVRVRtX0Q2WUdHMkhlYk10R3paeXgyclBMUnp6SHNHUXlmc3ZfdHBZSVNNLVlVc1pYX214cGdYRVlDWmtuaTRLNndyWXpTZTBmcFVkd1hMdURPNjBqcW1TUm5zcHczQ1JKeVZRWWUwOThUekdEMTlRYlZMSkR3M1hDS2ZTYw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 31 Jul 2026 12:25:39 GMT
- [語音 AI 的「自然插話」機制，對使用者信任感有何影響？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiZEFVX3lxTFAwR0hCVmU2OVVKekk0RE5RSmg1NTFRUkdGVG0zQ0tiSHNpNHVmajNyUWhWdVp5VFRMVUhqU3I3aVoxdlMwbnBwNVR0dVAxWmx6NzhTT2JfRElmNDlVVjVoTXRodC0?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 01 Aug 2026 21:32:04 GMT
- [超低延遲推論技術的突破，將催生哪些新型態的 AI 商業應用？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMimwFBVV95cUxOdnVtOVpGbVR6T1Ewb0hMcDNvNWdPRE40TWF2Q1lEbzhrei02cGFSM1Z0aC1YLTVFd2lRUFVRQ2JaZVVDdzhPRW1rSGhvNXJ6Rmo3Xzc3bEYzV0NUMVdXTm9pajdKaDlfUmd3TlNSMXh1N2ltOGxQbHMyVk12SVNVUUFiOEhtUndiZTk4Z1c0SFd0YjdCQ01TSlFjaw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 01 Aug 2026 21:01:46 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：群益金鼎-台北 對 台光電(2383)個股 單一券商歷史明細 - justdata.moneydj.com；富邦-虎尾 對 健喬(4114)個股 單一券商歷史明細 - justdata.moneydj.com；兆豐-竹北 對 鑫聯大投控(3709)個股 單一券商歷史明細 - justdata.moneydj.com

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [群益金鼎-台北 對 台光電(2383)個股 單一券商歷史明細 - justdata.moneydj.com](https://news.google.com/rss/articles/CBMikgFBVV95cUxObFRJaFAyWTFMS3F2SUtYMjlfYnRZT2RqNFdJaWdNbFR0ZjhLUjJKNVJfbW56Q244eTNUakI0ZC1BRUlMSmV5V2lmRjM4Y3llQmxsNTNBaWRGN1g1NVpuX1VadHVnWGplcVc1UHNPOG0xRzZycXRZUnFPMFd6bm4xaGpUWlQzT2pFQUJRWm1CUXhWUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 01 Aug 2026 06:24:50 GMT
- [富邦-虎尾 對 健喬(4114)個股 單一券商歷史明細 - justdata.moneydj.com](https://news.google.com/rss/articles/CBMiggFBVV95cUxQSFVLZjZRclZMSm05TTB0Y1hLZlZvT01DcTFwdTVfNnJiM1d1WVRhRUx4QXBiX1VQdHZCVDNiNUJKX1JQOXo3VUEtS0FfU0ZLNTdTVXZFN2VYM0hOUVpzcU04MWxfSUFmYVdXalE1LVNuclNnQmFxUklVZFpmcFdFT0pB?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 01 Aug 2026 07:56:56 GMT
- [兆豐-竹北 對 鑫聯大投控(3709)個股 單一券商歷史明細 - justdata.moneydj.com](https://news.google.com/rss/articles/CBMiggFBVV95cUxPc0Q2WUxiWlhsZ2NyUm84NWE2dnotUVo3bUltSkNYcDZSRFUyZUNySzQ4d2ZkR1ZBMjF3bjdnZUlLeU9iNU5TclF3aFFlaE1jblhhQUhweXVqRldUUmRLek5DWXRvLTZQRGdHTXFHcWFxalVWdUNJcGNPdk1Kd3h5akNR?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 01 Aug 2026 05:05:31 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：法人盤勢分析內容-台股 - MoneyDJ；AES-KY營收略優市場預期，Q2 EPS首挑戰11元 - MoneyDJ；毅嘉 115年7月營收11.67億、年增24.02% - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [法人盤勢分析內容-台股 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxOTl9CQ0ZVVFJ2WnlmUnBnTmMzbzJ1eEk1NEozOG1zR3hHdldFLTNiX0ItSkNwWmJ0QjZNWWxUdm9OZUVNaWh6ajJFdHNadzlvUGFsUHhUUTNSSmlBMXJtdVFZb1huVG1uMmZBdk9FdjRrOUxYdERXX0NxWXdxanZQeTdORUpUQmxpVjBvMEJtWWo?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 31 Jul 2026 00:40:01 GMT
- [AES-KY營收略優市場預期，Q2 EPS首挑戰11元 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNdzFBUV9lSUw5cGE5NWo5XzZEbFJWaWsyWDB0MjJLYXR5TmxiV3dNeWpjM2w1S1cxdENQZTlpVnpycFJpOFhhYVNHaGMzS213UndqSXNrOERXeG9TWjQwRnd3NmtNMGFQVEY4RVJpSWZBNGF3WFFnSW1jNUp4OHk1Z0FfRkVrcE1VTTY1V215d2lndw?oc=5) - Google News source discovery | MoneyDJ Fri, 31 Jul 2026 03:50:00 GMT
- [毅嘉 115年7月營收11.67億、年增24.02% - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQSjB2Ykl5UGtPdWJ0Q1YyRkwyRkRFaDBEYXBENUdNV09zNHlyNG1ZejVsRnd3OWFncG9WQUtIQTVlc1ZHc2k3N2psU1ZabnBLX2FFcENJbl9TcHROTjV3eFJCblkyRVV5dTJMXzc2enFLVGJlM044NHRIUHFydXphMXF2LVloaUZtWXJGZzJQbkdtdw?oc=5) - Google News source discovery | MoneyDJ Sat, 01 Aug 2026 10:28:00 GMT

## 新興題材：A9B8290B8FFD

摘要：新興題材：A9B8290B8FFD 相關新聞集中在：個股動態報導內容-0EB7BEA0-1777-497E-82C9-A9B8290B8FFD - justdata.moneydj.com

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-0EB7BEA0-1777-497E-82C9-A9B8290B8FFD - justdata.moneydj.com](https://news.google.com/rss/articles/CBMilAFBVV95cUxPaXRCZk1FTnBnZmNlQkgwLXU3LW11eUVGbTJJV2k4WWk5WFFWQ0dIYldLU3RYYm5INm84c3VUZk9ncG1BbHE4Yl9JR1RoOUVWdlNucFJldkk1Q2JBcGFRWlp4WGo5clV4S1h6YWsxZmZVT2owYXhya2o1QUtGd002dlp0eHNTSTlGTWwwT3ZEVGgzY2Vm?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 01 Aug 2026 06:18:41 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
