# 每日股市熱門話題分析 - 2026-08-22

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜正向｜熱度 10｜市場確認 43.22｜同向 1/2
2. **AI 伺服器與資料中心**｜中性｜熱度 9｜市場確認 N/A｜同向 0/0
3. **半導體與晶片供應鏈**｜中性｜熱度 6｜市場確認 N/A｜同向 0/0
4. **新興題材：航運記憶體**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0
5. **散熱與液冷供應鏈**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：N/A（樣本 2）
- 5日相關係數：N/A（樣本 2）
- 同向比例：1/2

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 43.22 | 1/2 | 1 | +2.74% | +2.42% |
| AI 伺服器與資料中心 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：航運記憶體 | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 先進封裝與 CoPoS | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-08-09 | -0.39 | 0.46 | +71.43% | 7 |
| 2026-08-10 | -0.09 | 0.74 | +71.43% | 7 |
| 2026-08-11 | 0.57 | -0.18 | +54.55% | 11 |
| 2026-08-12 | 0.52 | -0.47 | +87.50% | 8 |
| 2026-08-13 | 0.72 | 0.24 | +100.00% | 7 |
| 2026-08-14 | 0.34 | 0.57 | +92.86% | 14 |
| 2026-08-15 | 0.24 | 0.30 | +68.75% | 16 |
| 2026-08-16 | 0.37 | 0.51 | +70.00% | 10 |
| 2026-08-17 | 0.49 | 0.60 | +66.67% | 12 |
| 2026-08-18 | 0.29 | 0.36 | +80.00% | 10 |
| 2026-08-19 | -0.23 | -0.33 | +30.00% | 10 |
| 2026-08-20 | -0.72 | 0.06 | +50.00% | 8 |
| 2026-08-21 | -0.48 | -0.45 | +61.54% | 13 |
| 2026-08-22 | N/A | N/A | +50.00% | 2 |

## 歷史回測摘要

- 回測日期：2026-08-22
- 近5日 3日相關：0.22
- 近5日 5日相關：-0.17
- 同向比例：+71.43%
- 權重狀態：未調整

- 方向準確度：+71.43%
- 信心排序準確度：0.22
- 診斷：正相關

調整原因：近 5 日有效樣本 7 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：MU, INTC, SNDK: Chip Stocks Rally After-Hours On AMD’s Blowout Report - Stocktwits；INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits；WSJ Report Sends Memory Stocks Down. SanDisk Down 9%, Micron Down 7%, Western Digital Down 5% - AOL.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.48 | N/A | N/A | 966.78 | 974.33 | -0.77% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.24 | -1.83% | -2.74% | 1,596.08 | 2,335.00 | -31.65% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.42 | N/A | N/A | 473.25 | 516.10 | -8.30% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.42 | N/A | N/A | 90.07 | 114.68 | -21.46% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.37 | +7.31% | +7.59% | 214.72 | 216.85 | -0.98% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK、SanDisk」，共 4 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [MU, INTC, SNDK: Chip Stocks Rally After-Hours On AMD’s Blowout Report - Stocktwits](https://news.google.com/rss/articles/CBMiygFBVV95cUxPeVlYaXJjQjNtTkNRQUxQTHhaLUFMbE80Uy1MeDBpV0FPdkg2SHRLdkdfVUpXM1NrNWhZSVZQQ01sa0o4T1hKdzF1clBFRlRWUmMwWGxQTDNVVFBpOVhObUc2MXpBeXBOZ0p3R0w5NGRNOHB4X0ZIXzhlT0NMbmhzc1RtdmJRTWhlRUhKSHpyVnpaU0VGMlJyU2tDcmdkTG1hWVJJbmtTVDREbzFfWDB4bjhuTGswN3lmdkdHQzY1dzFOVU41VGlBNlZn?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 21 Aug 2026 01:08:22 GMT
- [INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits](https://news.google.com/rss/articles/CBMi0AFBVV95cUxOWm5KdEIwSXpyY191UEhDa1V6NVpWa01UbmpJeWRIV0ttT080TmpDNEhISW5TWkQwUzBVYzBqSHJPWXRVNVJCampoWWRlYmhKVkhIeHBJLS0wLW5Ua09GQnRORXpFcW5qTEJkcnJGcW55aU5rOFVOLUFMbjRPZEpWT3A2ZllucnM0SU9JNEdrNUwyc3V2WHAtNFk3VHl4R1F6SkZRMFpleEE2Zl9MdW4tSEpMMnFGZ2hQZURWQ3B1WDlPR1BhRjJELVN5ODJWYVR3?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 20 Aug 2026 13:31:57 GMT
- [WSJ Report Sends Memory Stocks Down. SanDisk Down 9%, Micron Down 7%, Western Digital Down 5% - AOL.com](https://news.google.com/rss/articles/CBMif0FVX3lxTFB5NDdMby01OWUyWFhOYXI2WkV0eW9ZTFFybVQxb0dkZ0FzcU5WWDlHcnhjY2xpMDVSUWRJNVRBcEhHemV1TXlyVGY4ZURYSnpNMzV5czJhLW9xOHlUTkFrdmNFb29IWnc0WC1SczNCMU1PRlhVdkI3ZW92aWdmaFU?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 20 Aug 2026 23:34:24 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：前 Google 首席科學家 Jeff Dean 談 AI 研究：廣泛閱讀論文，發現新連結 - TechNews 科技新報；模組化設計如何降低 AI 開發門檻？ - TechNews 科技新報；US corporate AI debt surge tests investor limits as fatigue emerges - Reuters

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +7.31% | +7.59% | 214.72 | 216.85 | -0.98% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 90.07 | 114.68 | -21.46% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 473.25 | 516.10 | -8.30% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +1.26% | +0.63% | 2,410.00 | 2,425.00 | -0.62% | 不適用 | 86.28 | 27.94 | 467.58B TWD / 44.69% | 2026-08-01 |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +23.04% | -4.63% | 483.24 | 506.69 | -4.63% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -2.46% | -11.73% | 368.45 | 446.77 | -17.53% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | -2.00% | -4.71% | 587.00 | 680.00 | -13.68% | 不適用 | 13.92 | 42.47 | 73.78B TWD / 43.15% | 2026-08-01 |
| 2454 聯發科 | 產業/供應鏈推估 | 0.00 | -2.45% | -9.98% | 3,790.00 | 4,310.00 | -12.06% | 不適用 | 60.69 | 62.59 | 48.47B TWD / 12.16% | 2026-08-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。 方向判斷命中詞：risk, surge。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：risk, surge。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：risk, surge。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [前 Google 首席科學家 Jeff Dean 談 AI 研究：廣泛閱讀論文，發現新連結 - TechNews 科技新報](https://news.google.com/rss/articles/CBMihwFBVV95cUxNcEhaSElndUNhWVFaT1BxNXNGUThYUjhPZDNOaDZ2eW5ZeEJVVHd5YjhRaS1ZeVp4eWZpQ0doaVp6U2Z5R0taYU9mMl91SWpBRF9ScENZQkQzaXNGSDFhVFU3TlpmQlBWODVDWWFsSHBRUDNjVmtiMlNpenJWOHdtSjliZG5rTlU?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 21 Aug 2026 08:32:28 GMT
- [模組化設計如何降低 AI 開發門檻？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMimwFBVV95cUxNczdNMzNocFlzT2hYZDhxLUh2YXYxNE5sUHdvN01yYlU3YndGMEhGOEtIUjB0RXJ3SGN6dWNBQnZmcHBQUHBMZDBxeVBQWnZUeFFHMUx0cVJSYk05c2FuTkdtSlIxa2dvQnRUbU5RSHo2NldDNnk4dEhnUTIxdkZEY3NBeThYcXEwbFMzNjFDUWJRM3J3Vm9zQUIwQQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 21 Aug 2026 12:38:03 GMT
- [US corporate AI debt surge tests investor limits as fatigue emerges - Reuters](https://news.google.com/rss/articles/CBMivAFBVV95cUxNR0I5VXZyeVp4RlV6cnhVdXFwZ2RNZUU0Q1czQ2c0WkpZUUJuRV9PNEg0VHkzLVlnSUdZMWVOalJzNkNXdlNtamlGSzRLbVRXb0VkVzl3dm5Uc3hPV21Cb3BIdTNyOWZQSDRGQ1ZvV2xUVUZ6eExfeGpRM0hQck8wSDlzR3ViRDJHS25NaGxwNHdVYWN5cHRUcWJvb0hybjRtclNxMFFGT18tMmc2SEw5RFNYb3ZrSWZpS0VYTw?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 21 Aug 2026 15:07:42 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：半導體展助攻矽光子族群開趴- 日報 - 工商時報；SEMI半導體材料聯盟成軍- 日報 - 工商時報；半導體材料邁向新紀元！徐秀蘭：台灣隱形冠軍要走向世界定義材料新標準 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 90.07 | 114.68 | -21.46% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +1.26% | +0.63% | 2,410.00 | 2,425.00 | -0.62% | 不適用 | 86.28 | 27.94 | 467.58B TWD / 44.69% | 2026-08-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | -2.10% | -3.72% | 116.50 | 164.50 | -29.18% | 不適用 | 6.68 | 17.52 | 23.84B TWD / 18.98% | 2026-08-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +7.31% | +7.59% | 214.72 | 216.85 | -0.98% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 473.25 | 516.10 | -8.30% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 966.78 | 974.33 | -0.77% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -1.83% | -2.74% | 1,596.08 | 2,335.00 | -31.65% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -2.46% | -11.73% | 368.45 | 446.77 | -17.53% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 CPU, server CPU, x86, foundry；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 0 篇新聞出現相關標籤。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 0 篇新聞出現相關標籤。

### 主要來源

- [半導體展助攻矽光子族群開趴- 日報 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9Edm9RNnJ5bkNHdUg0cjRTR3hBdmxaMUpJZTdYVHRRLXpQd2wwNEpURVJaSFlSSTRhVno0b2Jmb0kyclFOSkZZbk54OW9JaHFzd3RjWmppOTY3aktnb3Jn?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 20 Aug 2026 19:00:00 GMT
- [SEMI半導體材料聯盟成軍- 日報 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBwMnBpVEdlM2RfRXFDaXgxZkowVjFlei1ObkRvczU5SkVCTVV1ZWNCRDU5ZWwyMkJuRmpES3k5aVFIUGhNb18xLTZoa1NySHl2MmNCZ3B1V1NCemxpM1VZ?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 21 Aug 2026 19:00:00 GMT
- [半導體材料邁向新紀元！徐秀蘭：台灣隱形冠軍要走向世界定義材料新標準 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiwwFBVV95cUxQSldoOVZ2YzFuNGFoa0EtSGRPaVZhMDhZR2ZSWFRHWlBUSFJFN21xQkRnX0hKNHR6OVR4aEJXaWQ1Q2lueEZCdUpRbFZTSmZuT0dnZzNZNmZFV1NBRDZ6MWRtcXJkekdMNVRIYkZRUGFHczhfMDQyQkhqX2lIYUxoTmpLcGVFZm5kZ3RyS1AxcmJDaGsta0wwekRubG40OXFWVEh5ZElOc0RxZER4cnZtVDNiRDlOWllGdGEwR0x2SWdsUzQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 21 Aug 2026 09:12:26 GMT

## 新興題材：航運記憶體

摘要：新興題材：航運記憶體 相關新聞集中在：台股太狂了！V轉上漲290點台積電與聯發科領軍、航運記憶體噴出- 證券 - 工商時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | 0.00 | +1.26% | +0.63% | 2,410.00 | 2,425.00 | -0.62% | 不適用 | 86.28 | 27.94 | 467.58B TWD / 44.69% | 2026-08-01 |
| 2454 聯發科 | 新聞直接提及 | 0.00 | -2.45% | -9.98% | 3,790.00 | 4,310.00 | -12.06% | 不適用 | 60.69 | 62.59 | 48.47B TWD / 12.16% | 2026-08-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。
- 2454：新聞直接提及「聯發科」，共 1 篇新聞命中。

### 主要來源

- [台股太狂了！V轉上漲290點台積電與聯發科領軍、航運記憶體噴出- 證券 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBlVjNvZzViQXVHcmNObVc1SFFJVV9tMnB6SUFGTXVBdXJjWENGdVk0SXZMOERTUEpOTzBzeGdDaEZqakN6LTFmc2RDM25kTjBoMkpuaGVmMnBudF9aOU9z?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 21 Aug 2026 06:17:00 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：股海自由行／散熱、電源供應器 利多撐腰 | 證券達人 | 證券 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | -5.60% | -11.44% | 2,865.00 | 2,985.00 | -4.02% | 不適用 | 75.13 | 38.19 | 18.59B TWD / 57.39% | 2026-08-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 1 篇新聞命中。 同時符合主題標籤：thermal。

### 主要來源

- [股海自由行／散熱、電源供應器 利多撐腰 | 證券達人 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiW0FVX3lxTE94R0hfTWczYzc1NDloT25JdHh0QmJfTFIyU1ZBeWxHbUxkVWlPWktpOHFkVUJkTkQ4Z3hKOHdnalo5QllfNWtud3lGM3Bmb0NvbG5BYld3RTNERVk?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 21 Aug 2026 16:30:42 GMT

## 先進封裝與 CoPoS

摘要：先進封裝與 CoPoS 相關新聞集中在：晶片走向系統、先進封裝成關鍵戰場！Rapidus：晶圓代工、基板、OSAT 廠競爭加劇 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +1.26% | +0.63% | 2,410.00 | 2,425.00 | -0.62% | 不適用 | 86.28 | 27.94 | 467.58B TWD / 44.69% | 2026-08-01 |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | -2.00% | -4.71% | 587.00 | 680.00 | -13.68% | 不適用 | 13.92 | 42.47 | 73.78B TWD / 43.15% | 2026-08-01 |

關聯理由（前 3）：
- 2330：產業/供應鏈推估：公司標籤符合「先進封裝與 CoPoS」關鍵字 advanced packaging, CoWoS, CoPoS, FOPLP；其中 0 篇新聞出現相關標籤。
- 3711：產業/供應鏈推估：公司標籤符合「先進封裝與 CoPoS」關鍵字 advanced packaging, CoPoS, FOPLP, panel-level packaging；其中 0 篇新聞出現相關標籤。

### 主要來源

- [晶片走向系統、先進封裝成關鍵戰場！Rapidus：晶圓代工、基板、OSAT 廠競爭加劇 - TechNews 科技新報](https://news.google.com/rss/articles/CBMibEFVX3lxTFBxNmdoMlNsNWswN2xGc21wdU1pQ2JDdVV2NDNCYkZkLVJ3NHZNM25uZTNyY0RuQzdxSU1JM3JLVlZ4bERUb2YyeEtoMVlZbFQ2akhzTmFFTkpZSVZzQjJDMFhhZFhCUnBpX1lDRw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 21 Aug 2026 01:18:52 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：投信由買轉賣 台股資金風向變了！砍電子、抱金融 誰成了避風港？ - 經濟日報；台股周線翻黑 誰在逆勢吸金？3飆股狂噴60% 「三大水手」接棒成新主流 - 經濟日報；電金拉抬 台股演反彈秀 專家建議緊盯美長債對市場影響 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [投信由買轉賣 台股資金風向變了！砍電子、抱金融 誰成了避風港？ - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFB2QkVYMkdYbVVBTS1Vck54Q3FTNDJKSXdsLU90cjBXVUtuV2tnMUozcUhMX1ZIMmhnVWxyTk9YQ3pvdURXV08zVy0yTUhaNG1SVDBhUWdzaHFDUdIBX0FVX3lxTE1fY2dPSmxRdzhxLTRUbUFrY2c5U3RTYjdCb2RqTFg1b0hoNVBhQk1nSHNyci1RYlhvdUhneDJ6SEIxTFUyQUIydV9XTUsxRmlObWd4ajJCMnlEbEpWdnQw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 21 Aug 2026 19:27:57 GMT
- [台股周線翻黑 誰在逆勢吸金？3飆股狂噴60% 「三大水手」接棒成新主流 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE43OHdpQjJTeW50Vk1KbW5GaUd3MEprTTdERUdyelNTSWdwVXJuTE5xRGI3UVZhc3BYbExKN3REUFBPVm9PR3ZuR3VFOVYzNmdmX2JqNWY1aWE4d9IBX0FVX3lxTE41WUtFeXczS3dKNm1WZVdIZ1huamN4UndqM0JhS2c1djBqQzl3VFgxbDN1RXBaUUhTNWswMHZkUHI0b1h4dU51dXc5dWVIWDlVQXJHamhIVzJZZ2hJU3RV?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 20 Aug 2026 09:00:00 GMT
- [電金拉抬 台股演反彈秀 專家建議緊盯美長債對市場影響 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxORS1uNXpubGZEbjZEdjNLVE5ReWVRZFhrSm9WbTAtMk96RzFvMnlMOExXdHl3dGFUZHVtclBWbjV1WktuaU42b1lJLXZKTUp2YlNjX1RsY2ZyeV9veWVDU1hwWU9KTWhCbmxNSWo1YTd6R1k4VEJ6OHJqWmFvSXJaUdIBX0FVX3lxTFBUdUM5XzBQQU5vTHljajF6TXgtMHNoQVpFdi15Z3hnZzhSVlFpUFFPUDdDX2xWdUlJTktmMUh3TWpOMEJVcTd1LU5JY0h0anItc2RWRG5ibVNZSGtmazRZ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 21 Aug 2026 16:56:34 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》量縮收漲290點、重返5日線；週K翻黑- 新聞 - MoneyDJ；統一證券：台股將於月線至季線區間震盪- 新聞 - MoneyDJ；《台股盤後》量縮收漲290點、重返5日線；週K翻黑-新聞內容-基金 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》量縮收漲290點、重返5日線；週K翻黑- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNclBoOHdITkhRSWVaMkFpMlZUUXBoNzJ3THFkLWEyYUlTejVnbzlOZkZSYkRYTlRKaWdHNnZXY0JpMHF6REQ1a3NMSWhNWmRmMDRKY3pLSVdJYndUZVp0OEFzdGxKQ28yQmtsdVRHc0t3OThfbElwUXI0c0l6bVc0MnhhVHBKWEZrRTZ1X1UyVWR3QQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 21 Aug 2026 08:14:00 GMT
- [統一證券：台股將於月線至季線區間震盪- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPVWdOVExVRVQ3WF9JT0tnaHMtU21WZmhPZU5GaFRfdmVkZzRXM1daMXZxNHp3cTFSSWRCUXJkRjJlWGpxUlFtVUQxQ0lBTGhrMUltdDlZY2ZDaWRTMjY1eThEOFdxVFg3QjN5b2hJMU1hS2Y0RUoxTm5xYXpONDRfQUN0TXJ3SEdNZy16LXBFREFNQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 21 Aug 2026 00:43:00 GMT
- [《台股盤後》量縮收漲290點、重返5日線；週K翻黑-新聞內容-基金 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxOU2w1eDY5bmRKSHpLUlBhSGp0bjFNeHNydmxEU21uNDk5endsZ2dPUUJxSzAyaHo3c1dzdGJGeVEzZ0x6cWNod3JPWlljWFA3OFczSEZfMUZ3ZVlnVXdSeEFZekpHdElQWTVLRFJuamdWNEpiTTRwNGZPSEtSc3lJeFhlVHhmdTloN2dKWmtVZW0?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 21 Aug 2026 08:17:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://m.cnyes.com/news/cat/tw_stock_news?type=rss，原因：HTTP Error 502: Bad Gateway
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
