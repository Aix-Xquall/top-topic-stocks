# 每日股市熱門話題分析 - 2026-06-17

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **新興題材：MoneyDJ**｜正向｜熱度 11｜市場確認 90.01｜同向 1/1
2. **AI 伺服器與資料中心**｜正向｜熱度 13｜市場確認 57.46｜同向 4/6
3. **記憶體與 HBM 供應鏈**｜中性｜熱度 6｜市場確認 N/A｜同向 0/0
4. **半導體與晶片供應鏈**｜中性｜熱度 6｜市場確認 N/A｜同向 0/0
5. **新興題材：TradingKey**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.17（樣本 8）
- 5日相關係數：0.47（樣本 8）
- 同向比例：5/8

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 新興題材：MoneyDJ | 90.01 | 1/1 | 0 | +6.67% | +4.12% |
| AI 伺服器與資料中心 | 57.46 | 4/6 | 1 | +3.60% | +3.79% |
| 記憶體與 HBM 供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：TradingKey | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | 0.00 | 0/1 | 1 | -1.50% | +6.88% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：SpaceX | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-06-03 | 0.48 | 0.62 | +90.91% | 11 |
| 2026-06-04 | -0.38 | -0.30 | +85.71% | 7 |
| 2026-06-05 | 0.31 | 0.93 | +50.00% | 6 |
| 2026-06-06 | 0.12 | 0.06 | +45.45% | 11 |
| 2026-06-07 | -0.32 | -0.20 | +45.45% | 11 |
| 2026-06-08 | 0.36 | -0.68 | +60.00% | 5 |
| 2026-06-09 | 0.07 | 0.19 | +25.00% | 8 |
| 2026-06-10 | 0.17 | 0.15 | +53.85% | 13 |
| 2026-06-11 | -0.05 | -0.08 | +14.29% | 7 |
| 2026-06-13 | 0.87 | 0.98 | +100.00% | 4 |
| 2026-06-14 | 0.82 | 0.98 | +100.00% | 3 |
| 2026-06-15 | 0.87 | 0.56 | +42.86% | 7 |
| 2026-06-16 | 0.39 | 0.50 | +76.92% | 13 |
| 2026-06-17 | 0.17 | 0.47 | +62.50% | 8 |

## 歷史回測摘要

- 回測日期：2026-06-17
- 近5日 3日相關：0.12
- 近5日 5日相關：0.44
- 同向比例：+66.67%
- 權重狀態：未調整

- 方向準確度：+66.67%
- 信心排序準確度：0.12
- 診斷：弱正相關

調整原因：近 5 日有效樣本 6 筆，低於 15 筆門檻，暫不調整權重。

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

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：基金-FundDJ基智網 - MoneyDJ；台股ETF受益人破1700萬主動式/高息人氣相對旺- 新聞 - MoneyDJ；統一證券：台股明日逢台指期結算，影響短期波動- 新聞 - MoneyDJ

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | +0.50 | +6.67% | +4.12% | 2,400.00 | 2,400.00 | 0.00% | 同向 | 74.39 | 32.27 | 416.98B TWD / 30.09% | 2026-06-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。

### 主要來源

- [基金-FundDJ基智網 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxQVDFsbE84Y3Y2cUUwUUNDSl82aG1iQjZZblVfRU5Yd0hwbUVEYzFyTDRhY3kyRGIyNE5JUjhGTFpzUDA1ckpaMnd3clZHYVJJMDgxeVZrV3g0QXVEMmU3RVpxWVpRXy1pb0N1YmFZSUJTbVNOZ1R3TEVZSFlESDVLd3dGaFYtRjVZRkl0MmY4eGw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 16 Jun 2026 19:13:43 GMT
- [台股ETF受益人破1700萬主動式/高息人氣相對旺- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQSUQ4b0h1UW9RRzRXR1lrMWFWM3JYbHpEQlEzSk9lWHMzOWNBOVd6MWJEdDcyT3c4N2VXX0ljdThUUHZyLUJYLUJDb2ExU1duWVhlT21MSTdUMDRQUE5VWWoxSEh3cDRlR0ppOU04aDlfdVJSZ2FNME9lVEx4cm13a1dHWVh6aXJVeXFPZ3lZR3MwQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 16 Jun 2026 02:51:00 GMT
- [統一證券：台股明日逢台指期結算，影響短期波動- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNbUNzVVlvWE91NzRDWFFSYUxqS0NmUzE5RDZFVUlxLVNncVhNZWpQX0dZbnZ2RDVTZThXMFBZd2tjeUtQQm0zNWk4ZFhCcThnVzBwZWtiX3NJa1JhOTVFYlJ4V2c3cWxDTFlJZ0thcllOeTlzU0QyaDRIeEtDTGJESTNCczJwRDJvYWgxT2dJUW1Sdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 16 Jun 2026 00:40:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel (INTC) Expands Panther Lake Into Industrial AI Through Kontron Partnership - simplywall.st；Is Intel Stock's AI-Fueled Rally Outpacing Its Turnaround? - Trefis；Focus on 5 AI Behemoths Carving a Niche in the Server CPU Chip Market - Yahoo Finance

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.68 | N/A | N/A | 117.05 | 127.86 | -8.45% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.65 | +3.93% | +17.06% | 207.41 | 212.45 | -2.37% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.06 | N/A | N/A | 507.29 | 547.26 | -7.30% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.06 | +6.67% | +4.12% | 2,400.00 | 2,400.00 | 0.00% | 同向 | 74.39 | 32.27 | 416.98B TWD / 30.09% | 2026-06-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.03 | +0.28% | -22.27% | 393.83 | 506.69 | -22.27% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -9.75% | +17.89% | 376.71 | 446.77 | -15.68% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.04 | +8.82% | +4.04% | 592.00 | 611.00 | -3.11% | 同向 | 10.86 | 54.97 | 63.03B TWD / 28.57% | 2026-06-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.04 | +11.63% | +1.90% | 4,560.00 | 4,560.00 | 0.00% | 同向 | 62.91 | 72.67 | 47.43B TWD / 4.99% | 2026-06-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC、Intel」，共 3 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：rally, 上修, 成長。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。 方向判斷命中詞：rally, 上修, 成長。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：rally, 上修, 成長。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel (INTC) Expands Panther Lake Into Industrial AI Through Kontron Partnership - simplywall.st](https://news.google.com/rss/articles/CBMiygFBVV95cUxQUTlxa2NkZ0J2MHVNUEMzbXV1Wldyc09pal9jZHpndnd5Z1JmMERBNzhra0JSb0xDY2liZ1dFdFVkZVp4ZTM5Uzk0Q2FsbW9XWDlwWUhtZ2hGdlI2V0pXNTZvSFdsMUNMeUhxMExBbVJqV2JXbUlxS29heUhfWE95VXJjS2VhdWFhTlFrc2x2NHNIS1IycnFvR2RnUWEwR1gtLVllNXdqYkFsdHdWLWVDSFJFMXhJSm56dlExbWU4YUtveGR6b2dQbzdn0gHPAUFVX3lxTE9WSmluQ1lYX3lreWU0SW1UU3ZXQ2dFdm1jOXhJMF95bFJvU1lsSG9ldmpUZ3lkT0llRDk1U0hMSVY0MXoybkg1RmZUQzBSdkVsd3RUMGk2aVpXRXR4SVFiY25vQ1FTMEdHcWlmc2s1SlVmWFB3ME5xOGNoblhOR3lnc2ZtMG9Od19CbHgtUXJtbF9CVklmZDMzdGNuUVFNaHNKUXpIZ3ViR0F2MkQ0UXFnMkFtN0lmSjFKS0NLVjllcm9xTTQ5T29wV0E2MF8wYw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 16 Jun 2026 13:36:36 GMT
- [Is Intel Stock's AI-Fueled Rally Outpacing Its Turnaround? - Trefis](https://news.google.com/rss/articles/CBMixwFBVV95cUxQdklCZElMcTdjbjZXa1Vubmo3Tld1LXNmTXhaRjBZSlZabEphblg1ZEJYTkpKVnFTVnhoclp0Y1MxQWpmRmlzMjByLUdqdmFYQ1JRZHpqOGNvbWI1Q3NpMkNoQWVGQm9JOHBOTlgxaGFfU0IyWElsSmNucDI4TjRLVnQ5aGVsaU11Z3Ryb1VhMG5sV2s2d2x4bWR0UFpydFZiVi1Tc3B2eHM3Y3RweDdNaDhSYTNLV3FXcWlMUGQ2YzlJUEpZRFdz?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 16 Jun 2026 06:14:25 GMT
- [Focus on 5 AI Behemoths Carving a Niche in the Server CPU Chip Market - Yahoo Finance](https://news.google.com/rss/articles/CBMilwFBVV95cUxPc1REQkdmOWg0MmpBZHRJbmlTcXJHSHQ3cWw1dTFkS3lwbmJhdlItRGkzRmgyQ241YzFQUXBYMHAzdjI3RE1ITWtoZzAzczVFelIyY0VFTUJLZ3l4ZzlILWNpajkteDkzLUVtME13ZDdwakNyN2hONDI4a2RjbkEyOWNWVWo1cmpXbGlCRXpIX3Fsa3FPWXdR?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 16 Jun 2026 12:52:00 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：The Zacks Analyst Blog Highlights SanDisk, Micron, Seagate Technology and Western Digital - The Globe and Mail；Sandisk: The Supercycle Won't Last As Long As Investors Hope (NASDAQ:SNDK) - Seeking Alpha；Up 770% YTD, How High Can Micron Go? - 24/7 Wall St.

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 1,020.76 | 1,087.99 | -6.18% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | +5.85% | +20.95% | 1,991.55 | 2,107.86 | -5.52% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +3.93% | +17.06% | 207.41 | 212.45 | -2.37% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、MU、DRAM」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk、SNDK」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [The Zacks Analyst Blog Highlights SanDisk, Micron, Seagate Technology and Western Digital - The Globe and Mail](https://news.google.com/rss/articles/CBMi_wFBVV95cUxOTE14MXNsR0MzYlF0TzZDdU9kMzZhSWN4djUxRHpFbWI2QWhDTnhTRFJZNFd6S3FQYkZ1dEFpVEg0VjVNRHFFV3ljTVZlRjlyUlBSLUJSejI4cnZOdGxyYU1wOFNJVzc0TmItcVRjWXpFVlF0LW8yNnRxLVdZV1V6eE9JNF9hQ0RrUGU1YlVIdEQ1SmVRS0puNGU3ZnJQcWZ2S3RFR2R4YXQ0WkQ1WllrQVRMcU9NdDBnbzFrbGlsTnlhY1VvWDNlLUpGek95LUpaSnYtckU4NXQtZzZHZjVINVNUOUxnazZvTk1BUWVfWWdTdGpNVGVOM3BJakVjckk?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 16 Jun 2026 09:42:00 GMT
- [Sandisk: The Supercycle Won't Last As Long As Investors Hope (NASDAQ:SNDK) - Seeking Alpha](https://news.google.com/rss/articles/CBMioAFBVV95cUxOZFZJbTVaR2psZHVzOVpBZHlYVVR3d0RRc1UtZngtSFRYNDJpeVNFWG9OVlhKSWZwMFczUmlpODFnbTZudmN1dlRIZ2Ezd2ZibkxSTW5VTURTdjdaQlIzREtWclR2WWNqQlVpYTFjX2ozYy1IMGx5Nmp2amdtZ1hzN2dYSFk5RlM4bTBPdlN5dmF2dTltVmZLZXQ4c1IxeDg5?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 15 Jun 2026 21:49:34 GMT
- [Up 770% YTD, How High Can Micron Go? - 24/7 Wall St.](https://news.google.com/rss/articles/CBMigwFBVV95cUxPZm0tMmZDdHY4LTNJdlNxZDRoV2NjcjgwMVFnSlpBN2xOUnBhRUE3ZzZiaGVIWnBwdEJKV1czaTZZcjFiSG4ycjdWQ2k5T0pJQ1AwZGZwVlNnX1dRNkZwQlFTVjNJU2ZzbnpxSmhMS2lPMk83RDBNVXFXTGtFWFNGY1dZOA?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 16 Jun 2026 13:37:20 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel Is Up 8% Today: Is It Outperforming Other Chip Stocks Like AMD and NVIDIA? - AOL.com；Focus on 5 AI Behemoths Carving a Niche in the Server CPU Chip Market - Yahoo Finance；專家：AI半導體撐台股衝5萬點留意槓桿風險| 證券 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 117.05 | 127.86 | -8.45% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +3.93% | +17.06% | 207.41 | 212.45 | -2.37% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | N/A | N/A | 507.29 | 547.26 | -7.30% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +6.67% | +4.12% | 2,400.00 | 2,400.00 | 0.00% | 不適用 | 74.39 | 32.27 | 416.98B TWD / 30.09% | 2026-06-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +12.80% | +10.59% | 141.00 | 144.50 | -2.42% | 不適用 | 4.00 | 35.43 | 22.94B TWD / 17.78% | 2026-06-01 |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 1,020.76 | 1,087.99 | -6.18% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | +5.85% | +20.95% | 1,991.55 | 2,107.86 | -5.52% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -9.75% | +17.89% | 376.71 | 446.77 | -15.68% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Is Up 8% Today: Is It Outperforming Other Chip Stocks Like AMD and NVIDIA? - AOL.com](https://news.google.com/rss/articles/CBMigwFBVV95cUxNYTduRHZxQVdPejFHSHlEYnhrVDVScUhGeFAwaElROFBOVGR6SjFRWFFramJYSWcwa1lveTVfYjJKU29zM0VhbGsxX0s0ZENIR1l0Z0dULVRMMHY4VlZJam4tVzFqeTFUbXFsQVFoVnZhVDlrZGJhQnZ6b2NuN0hKeXR4SQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 16 Jun 2026 18:29:36 GMT
- [Focus on 5 AI Behemoths Carving a Niche in the Server CPU Chip Market - Yahoo Finance](https://news.google.com/rss/articles/CBMilwFBVV95cUxPc1REQkdmOWg0MmpBZHRJbmlTcXJHSHQ3cWw1dTFkS3lwbmJhdlItRGkzRmgyQ241YzFQUXBYMHAzdjI3RE1ITWtoZzAzczVFelIyY0VFTUJLZ3l4ZzlILWNpajkteDkzLUVtME13ZDdwakNyN2hONDI4a2RjbkEyOWNWVWo1cmpXbGlCRXpIX3Fsa3FPWXdR?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 16 Jun 2026 12:52:00 GMT
- [專家：AI半導體撐台股衝5萬點留意槓桿風險| 證券 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTFB0TkpEX1JEX3dBRGFwWHZkVWRwOXFnV1B2NWJKNmVFTEVfVm9ySVNLT056cGNTUjhONnFzN21pRkFZcFNDTUdteXJjTHp4QW9WdWhuOTg4OTd0a2hFYVE?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 16 Jun 2026 11:56:00 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Intel Corp Stock (INTC) Moved Down by 6.39% on Jun 16: What Signal Does It Send? - TradingKey；Micron Technology Inc Stock (MU) Moved Up by 8.00% on Jun 15: What Investors Need To Know - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 117.05 | 127.86 | -8.45% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 1,020.76 | 1,087.99 | -6.18% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MU：新聞直接提及「MU」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Corp Stock (INTC) Moved Down by 6.39% on Jun 16: What Signal Does It Send? - TradingKey](https://news.google.com/rss/articles/CBMiiwFBVV95cUxQLVFRdWkzdmY5ZDlQT1B2ZzBVT2VHLTZCbzFLMUZJeTJFM0lYY2pyLXdSaldFMFpkRW1ZYkdnZnhNR1d1WVpYNWxUOUE5TFJlYjJFWlBjdUZGOUtLSmNrNXVJYWJxcUZrbDlQY1JMNFNwaVJIcDlpb3FfY0x0Q2xJNXJpWndFMEZCOWY4?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 16 Jun 2026 15:15:25 GMT
- [Micron Technology Inc Stock (MU) Moved Up by 8.00% on Jun 15: What Investors Need To Know - TradingKey](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPMk5JMklrcXVXeFdYSUVkSFFzbzQ1Z1J4T0UyZGJiclBCTGtDX0NsYnJHaUNlbjhBMkdqRjlXYTJkbkQxTVZabGdTSVJuTWNISEpkZ0FLTElsMVpQVl94dTJobGJyV2V5aWxQT0tnenBpc1JRT0YwdmRObWFKZWszSlFWU0dSN3BC?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 15 Jun 2026 14:15:31 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報；奇鋐、雙鴻 押逾三個月 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | -0.30 | +1.50% | -6.88% | 2,370.00 | 2,835.00 | -16.40% | 背離 | 61.06 | 38.94 | 15.87B TWD / 60.64% | 2026-06-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱、奇鋐」，共 2 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：跌停。

### 主要來源

- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 15 Jun 2026 06:05:19 GMT
- [奇鋐、雙鴻 押逾三個月 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBGeE5QY2doS3lPdTJQby1UeHhSekd5NVdMQm1JTTdHVmliRnB1dURCZ3o5SDM5ay12SDI4dUw0TGx0ZkFtZzVudUhhbHBramtRMFFVTUJEUWt2Z9IBX0FVX3lxTE5xeVZZWjc4elhPOWFUMWhyYWFiR0J6b0tyN3B0bkxHVzJtNmM1YzhvZTU0OTRkT0d0QndkOW5hUXlLN1JnZXNUQkhfZm1NME9yR1lFc1kxWFBxdGNLQXdV?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 15 Jun 2026 09:00:00 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：5月瘋台股 上市櫃市場日均值1.53兆元創新高、十大熱賣 ETF 推波助瀾 | 市場焦點 | 證券 - 經濟日報；有懼「高」症的台股投資人看過來！這檔鋼鐵股已獲長投買盤盯上 - 經濟日報；台股下跌而定期定額不減反增 豐存股用戶創新高 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [5月瘋台股 上市櫃市場日均值1.53兆元創新高、十大熱賣 ETF 推波助瀾 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxPTGNTcE16ZmtCSUMtSHBnZHA1YVBvTmxBODlGZWVqcVptVFJ4cDRnd3RaU2J0N1h0R3QwRXc1TmROV25zLTQyLXJnMVZ0T2VlaXdxNmJhVnFFTDd4OUc2RUZLNWkzc1hISGtlZHMySzRaWEJCNTZtbHgwVkJHM3ROZg?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 16 Jun 2026 14:21:36 GMT
- [有懼「高」症的台股投資人看過來！這檔鋼鐵股已獲長投買盤盯上 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE53Q3JlY1RVeGFyTmstdmszM3FUWGRuSzV5bWpqT0JQaUZKak1rU2tJbFltZTRaUHYwRHd6RHZGNGdoazdfNGZ0Z2ROd3JfM0M1aXFoWU9LNFEyZ9IBX0FVX3lxTE9yZVN6RUlybkZaUmdBM3FUcG9LbXJzUFRaamVqTGdIWG1PVDZXYmZiTElnMDRaak5JT0otY25NLXh6UGMxNF9PSjJSVFdRM2dzaGpVX1VqWmJnNXRobkpR?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 16 Jun 2026 08:10:47 GMT
- [台股下跌而定期定額不減反增 豐存股用戶創新高 - 經濟日報](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9pU3Z0ZEZ4QndqWWoySDZxNC15ZlktdENXcXY3bFV0eVZQN25VbE1hNk9yNEF4X0RNYXZFRGxYMEc5QUp1cjBGOXctR1RDWnR5WS1Nb202Rm83ZU3SAV9BVV95cUxQV0Q2Q0ZPTHdDb203M2tuMTFCel9HU0V1QTBPMXd6ZDNrLWlZRGE1bG5QazZwZ3oxQnNKajJXNVVhaC1ISU50RWFtdnVPa0pjTUp6SnliN0RHRWhMQTd5VQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 16 Jun 2026 09:54:06 GMT

## 新興題材：SpaceX

摘要：新興題材：SpaceX 相關新聞集中在：SpaceX 以 600 億美元收購 Cursor，加碼 AI 編碼與訓練布局 - TechNews 科技新報；SpaceX locks in $60 billion Cursor deal to close gap with rivals in AI coding race - Reuters；SpaceX's blistering start still faces key tests that will determine the stock's true value - CNBC

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [SpaceX 以 600 億美元收購 Cursor，加碼 AI 編碼與訓練布局 - TechNews 科技新報](https://news.google.com/rss/articles/CBMimAFBVV95cUxPVXN3V2VZRDRROXpjM3ZfMkViYXBrcEhTZjlha1EwVU85OC1HWUlxdkVFdV9RcGFQVUdKTTdydVpZWmdMZ01XajBSZDVHcFZfQzRHVzI5VWtMQ3NZN3BubzQ2bFNON3M4VE01djVqMTY1R202YnlaeG5Ec2Yzcl9MVEZyQjEtNXAwUWJKS0xnVVFZbGNmZGFqSQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 16 Jun 2026 13:29:41 GMT
- [SpaceX locks in $60 billion Cursor deal to close gap with rivals in AI coding race - Reuters](https://news.google.com/rss/articles/CBMikAFBVV95cUxPRmxuTnhpZnhfWk9xMXRkVFVNeXBjXzZSRmZRakJpR0RzZnBxOWFfMk40NW1yaXBvTlBQY2FhbG1wY0w4d0wyRFhIOUhjSlF5VW5Fc3pwZ2xRaERESmhmWGp0UE4yT1l2d0M2N2R2UTlLRGFYSkczc2wxcWxCSU1TMzhleHJMR2pKSjcydDRGMHE?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 16 Jun 2026 14:52:06 GMT
- [SpaceX's blistering start still faces key tests that will determine the stock's true value - CNBC](https://news.google.com/rss/articles/CBMiwwFBVV95cUxNVWdreE9zOVdMdjVfS3RtTnY4VVRObzE5dDZhNC1Ec0xSM21KQTY1QUd0QTN5Z25iX2o2YU5ScXFKZmh0UkJ5aDNrUDZVQWJDRDZfbUNCY3JFWDFJdU84WU03V05sblo0S0hvWWdpQ3pZakhGWWtvVW1McWY0RkJOYU5FcEdwb1prMjJNZTZhYTFrYTJqY1VGejE0RFhDWXRpQWRsU2MzcUw4MFRaM2hJTjJIcnRCZ3dxRElIeWdQd2ZWQkU?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 16 Jun 2026 20:24:47 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
