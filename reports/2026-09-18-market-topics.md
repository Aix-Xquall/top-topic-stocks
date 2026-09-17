# 每日股市熱門話題分析 - 2026-09-18

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **利率與成長股估值**｜負向｜熱度 2｜市場確認 85.39｜同向 1/1
2. **記憶體與 HBM 供應鏈**｜正向｜熱度 9｜市場確認 41.62｜同向 2/4
3. **新興題材：TradingKey**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0
4. **半導體與晶片供應鏈**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
5. **AI 伺服器與資料中心**｜負向｜熱度 17｜市場確認 3.60｜同向 2/8

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.15（樣本 14）
- 5日相關係數：-0.07（樣本 8）
- 同向比例：5/14

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 利率與成長股估值 | 85.39 | 1/1 | 0 | +5.13% | N/A |
| 記憶體與 HBM 供應鏈 | 41.62 | 2/4 | 1 | +2.21% | -0.37% |
| 新興題材：TradingKey | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 3.60 | 2/8 | 6 | -4.63% | +2.23% |
| 新興題材：StocksToTrade | 0.00 | 0/1 | 1 | -5.13% | N/A |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價呈負相關；應檢查正負向詞庫，並降低新聞直接提及但股價背離的權重。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-09-05 | 0.13 | 0.34 | +54.17% | 24 |
| 2026-09-06 | 0.19 | 0.43 | +50.00% | 24 |
| 2026-09-07 | -0.15 | -0.09 | +53.33% | 15 |
| 2026-09-08 | -0.07 | 0.18 | +57.89% | 19 |
| 2026-09-09 | -0.28 | -0.12 | +54.17% | 24 |
| 2026-09-10 | 0.28 | 0.86 | +75.00% | 4 |
| 2026-09-11 | -0.01 | -0.08 | +25.00% | 12 |
| 2026-09-12 | -0.39 | 0.04 | +25.00% | 20 |
| 2026-09-13 | -0.42 | -0.14 | +17.65% | 17 |
| 2026-09-14 | -0.31 | -0.54 | +33.33% | 15 |
| 2026-09-15 | -0.04 | -0.42 | +68.75% | 16 |
| 2026-09-16 | -0.19 | -0.46 | +55.56% | 9 |
| 2026-09-17 | 0.43 | -0.13 | +66.67% | 9 |
| 2026-09-18 | -0.15 | -0.07 | +35.71% | 14 |

## 歷史回測摘要

- 回測日期：2026-09-18
- 近5日 3日相關：0.13
- 近5日 5日相關：0.19
- 同向比例：+57.14%
- 權重狀態：未調整

- 方向準確度：+57.14%
- 信心排序準確度：0.13
- 診斷：弱正相關

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

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：升息利空變利多？通膨疑慮降溫、美股4大指數全面反彈 英特爾大漲近8% - Yahoo股市；〈美股早盤〉油價回落緩解通膨疑慮 主要指數開高迎接Fed決策 - Yahoo股市

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.42 | -5.13% | N/A | 108.80 | 114.68 | -5.13% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +10.55% | +1.17% | 497.75 | 507.29 | -1.88% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「英特爾」，共 1 篇新聞命中。 方向判斷命中詞：利空。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [升息利空變利多？通膨疑慮降溫、美股4大指數全面反彈 英特爾大漲近8% - Yahoo股市](https://news.google.com/rss/articles/CBMisgNBVV95cUxNbVFmcXJHWi1DNnl4elNQbDhKXzE0cXo2X0I5cnVEX0VHc3hlTm52UWVmWnZpT2tHTmVNQ2FYdWt2TUVzQ05FNUdGdS1ROFdPdXQwUUVfUnllUkNacXYtVXFLdmZIeUxnVmtBQ2RqYm01MUcxbUFxSUlDUnpLUnBuUXAyT0I3bWVhOEJCWWlBc0t2V2NGcmQ0RGJueHp6enJmSWlaOE1TNFNIeS1Da1pSRm1TVFZic1VFb0drMUtmQ2ppVVFjenQ4UjFfU3B6bjBIVnpVYTNjUGZWbjNUaVdCT210ZjN2S0lsZjQxVnEtcnU1RENUbURxdWFaWE5zMGl0WnlxbmtCM0RHMXNUd3B3aV91TTg1UVdsR09ycHVTb3BCc19DXzRfRDFoWXVReTA0bUhGc1N0UVJUcERZSVdWb3dZMjJqYkVKUUZWY1NHUzNTazNaVnBwcGx6ZFlqakhQZlRnWWsydmR2V3Y3alpQYm9LUFdoM2tyV2ZPMExlbTJkdTJLa0V2OFBtWnRETVg1X09TMHp4U21RUWsxZy0yanNqNEY2TDRpOVFyR1RTal9xUQ?oc=5) - Google News source discovery | Yahoo 奇摩股市 Thu, 17 Sep 2026 14:05:00 GMT
- [〈美股早盤〉油價回落緩解通膨疑慮 主要指數開高迎接Fed決策 - Yahoo股市](https://news.google.com/rss/articles/CBMiggNBVV95cUxNdVZ3Sm42ZWJNWHNrTFg2NEM1d2tkemZjVjl3OXdUM3BBdkZwSEU1bFBmRTFsSVNaRS1aMTltZTh2bWstM0MwUGdhMVhiejJCOFNodnNMMGd5RXdkT3BvaWVoZzVhdkxXb3haNzBVQ2NnVlItS05TbDBnTnJDU3NOaUFmcHY2VTNIMmhqNEw0UWJyV2NyUWhBcWZ2VzhwR3lUY2lBZ2F4SXAwc1h4ME1lYy0zSnhYRlpyWmtTVkNUeHhEOUlCMXY1Q3Z1UWc4Um5UNXUwNVNISThPYkoxM3FzMy1mTm04eW10ZExnSS1kXzBEd19rc2ZmQzlra2EycURjUjZPZTBJcDVfQ2ZDOXlFazU2cUYtSUZoOXFYYkRVRExKemlOZEtNSVpJblFVRUxMckN3S0hSMmNhcHJ2cUpOb056a1h4Z0NBbHZsWlBmdTh6T1ZWV0ttem9FRzVfdDlEd1VlMXdPb0NVRXVoRFh3LWZOeDhEMUE5ZXdEUGNVbnM2QQ?oc=5) - Google News source discovery | Yahoo 奇摩股市 Wed, 16 Sep 2026 13:42:31 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Intel Stock Jumps 4% on SK Hynix Rumor, But Here’s Why the Real Win Is Years Away - 24/7 Wall St.；What Could Intel (INTC) Gain From a US Memory Chip Push? - simplywall.st；SK Hynix Stock Rises as Intel Ohio Talks Reignite Memory Trade - TradingView

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.43 | +0.67% | N/A | 977.50 | 977.50 | 0.00% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.57 | +4.02% | -4.62% | 1,614.39 | 2,335.00 | -30.86% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.28 | -5.13% | N/A | 108.80 | 114.68 | -5.13% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.43 | +9.26% | +3.88% | 219.34 | 220.78 | -0.65% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「memory、Micron、MU」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：strong, shortage。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：strong, shortage。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel、INTC」，共 3 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Stock Jumps 4% on SK Hynix Rumor, But Here’s Why the Real Win Is Years Away - 24/7 Wall St.](https://news.google.com/rss/articles/CBMivwFBVV95cUxOZ2duanBTWEwtaEJVM0M2TG1OYV9zS2laNjYtekxwSDRPUGNnajVQOHR2Sk9ydEZ1M3dkcHZWTDNPcDhqS3h6ejFKdUVPem43a3A1NVc3WktLRy1CeVhiT0hxTllhSzV5U3ZSQmpDWUlmRUEyYXBQT21uS1NVY0NnMzg1bkowVW9Mb21ZOUxKb3FfM3J3ZlQwSjJZbTkwNGtCN3ZfdUxmRjhjU09TdlRWdUJZX1daQVNYYVBsOWlJdw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 17 Sep 2026 16:03:00 GMT
- [What Could Intel (INTC) Gain From a US Memory Chip Push? - simplywall.st](https://news.google.com/rss/articles/CBMiwAFBVV95cUxPcnVoYjNOdUduSXVUMnEwXzRELVM3bV9VY1UzcUZSMGdRMWVGc2k2OUFJWnozM3d6cmRleDVXQmhBN1lTaDBKMEJ2b0JCQzlLUlRkWllMdVRhcG1KTUFFY2gzdWl0SlpGNmVCdmNicWJVNDN6V2pFWmR1TE5saEJUend3Zkl4cVI3Q2JNUDZBeWctRm9YdEN5VmE0WjBfNEJyYUNJcVdDYTF3NWVvZ0NRelA2NkxwdG1nTDAwQktCVW_SAcYBQVVfeXFMUEYwNlV2cmt3cklJNkNoYk9NbzdBT2F6RlllNTBXaEJwUmp4MDlLOEpNLVBWOVFtcE5sVURRbTRYNkh3YzZaYjFUMW1zTE4yUTNBOGpQdEZJZEw2T3J3QWhuRUNJUFg2QlBGNDVyTVgwVEVsaGpnQ1lNaHBXZDdGcWxrU2VLUUhRc2YyT2EwV0Q3WXVOdFdYQ3hPb1JWVlowb2JqZHpKcXdhYl9GQTJha1IyaGpnY3JtR0M3UTd3Rkd6M1o4SDRB?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 17 Sep 2026 02:33:57 GMT
- [SK Hynix Stock Rises as Intel Ohio Talks Reignite Memory Trade - TradingView](https://news.google.com/rss/articles/CBMivgFBVV95cUxQa083S3VEUkxpU2tJM0tmMkJ1bWtUSWxxcndkN2JiUXVNeTVkc0RmaVdSVTktNmZRdDh6N194Tm1ranRtMGdmd01ZejNuenEtQWwzRHg5QXFiM29fUjhaOTk0dVpTYm5sMUtRekFaRjJKMnZoQ0dHa3VkZUpwOEN3NWVjTkNDMW9YVzdnZGRXWE9kQl82MFI4Q2M2T19FLUR2em5mMnRoTzF1VUtZM2N1bTJPTENxOFJrUlp5cEN3?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 17 Sep 2026 13:01:17 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Broadcom Inc Stock (AVGO) Moved Up by 3.17% on Sep 17: A Full Analysis - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AVGO 博通 | 新聞直接提及 | 0.00 | -10.78% | -22.26% | 347.30 | 446.77 | -22.26% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- AVGO：新聞直接提及「AVGO」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Broadcom Inc Stock (AVGO) Moved Up by 3.17% on Sep 17: A Full Analysis - TradingKey](https://news.google.com/rss/articles/CBMiiwFBVV95cUxPaUZIX1FTb2c4VXZOOHpkeXFIY2o3VkhSNXh3MUhZSDlWeG5Qbmh5YjN6Z1dneW1xZFdGSHNvdkJoTTZnbGVGcjc0TGR3Y2lVR0E2RTZVSzA0OEZTVkxGempRRUVHSVROc0hxNjREUG0wWE1NaGhuNklrSEcwamFNaHhySVFnalplREhj?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 17 Sep 2026 15:15:28 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel Stock Could Nearly Double to $200 in 2 Years, Analyst Says — Potential Apple, Tesla, and AI Chip De - Benzinga；日本對美投資添半導體廠格羅方德操刀、規模上看3兆日圓| 產經 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | -5.13% | N/A | 108.80 | 114.68 | -5.13% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 新聞直接提及 | 0.00 | +7.99% | +20.85% | 337.00 | 337.00 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| TSLA 特斯拉 | 新聞直接提及 | 0.00 | +17.67% | -15.97% | 366.20 | 456.56 | -19.79% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +1.89% | -1.02% | 2,425.00 | 2,425.00 | 0.00% | 不適用 | 86.28 | 28.11 | 514.81B TWD / 53.32% | 2026-09-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +3.51% | +3.51% | 147.50 | 164.50 | -10.33% | 不適用 | 6.68 | 22.18 | 25.04B TWD / 30.71% | 2026-09-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +9.26% | +3.88% | 219.34 | 220.78 | -0.65% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | +5.62% | N/A | 545.09 | 545.09 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | +0.67% | N/A | 977.50 | 977.50 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AAPL：新聞直接提及「Apple」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- TSLA：新聞直接提及「Tesla」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Stock Could Nearly Double to $200 in 2 Years, Analyst Says — Potential Apple, Tesla, and AI Chip De - Benzinga](https://news.google.com/rss/articles/CBMijAJBVV95cUxOc3pIU2NBYVY5TUp0LWpSR25xd3I3R2NDRXZtazBMeGZvQkxyLTFlS3hqS0xVQXNNNnBqb2ppcmJYNnF2NTFPd1NXQ2Y4cjlGMkRGRi1VZXdQZFh3UXd1UTNMWjdNVXpMRXNYR2t4d1JlMmNxTUpkREZEYlNTYnd4RjRYRXg5WXFHOG9sUGFJUS1ENnBfTHk4RmJlaW5uLWFFbnFTVzU0Q2YzS0xzd2hUazNrSkRMSi10akVNOVNBektsdGFVM1E1cm91bkYzYlE2bWI5TjN3NUVDb203bHc2c1F6SHVsYXZTUDVDSUFHdlkxbWtpMnQ5VTg5cjdZOTdpWWVnbEV1Ml8taEo1?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 17 Sep 2026 12:25:57 GMT
- [日本對美投資添半導體廠格羅方德操刀、規模上看3兆日圓| 產經 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE0tdnZYOXQtQzNRV2FXaWNqV05XSXlQYzhvZkhwYUJRYi1UVlUwbldMX0pEVUlKUDE1Rm9XUHNPVlhaTlc5dV9RT0lINHAyZmUyTmZzcXdmQ1l2WDJyWXc?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 17 Sep 2026 10:10:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel Stock Could Nearly Double to $200 in 2 Years, Analyst Says — Potential Apple, Tesla, and AI Chip De - Benzinga；NPU 支援多種精度運算，對開發者建構 AI 應用生態有何助益？ - TechNews 科技新報；頂尖專家頻繁流動，Meta 該如何維持 Muse 等 AI 產品的後續研發？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.54 | -5.13% | N/A | 108.80 | 114.68 | -5.13% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 新聞直接提及 | -0.21 | +7.99% | +20.85% | 337.00 | 337.00 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| TSLA 特斯拉 | 新聞直接提及 | -0.21 | +17.67% | -15.97% | 366.20 | 456.56 | -19.79% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | -0.03 | +9.26% | +3.88% | 219.34 | 220.78 | -0.65% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | -0.03 | +5.62% | N/A | 545.09 | 545.09 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.03 | +1.89% | -1.02% | 2,425.00 | 2,425.00 | 0.00% | 背離 | 86.28 | 28.11 | 514.81B TWD / 53.32% | 2026-09-01 |
| MSFT 微軟 | 產業/供應鏈推估 | -0.02 | +10.55% | +1.17% | 497.75 | 507.29 | -1.88% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -10.78% | -22.26% | 347.30 | 446.77 | -22.26% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AAPL：新聞直接提及「Apple」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- TSLA：新聞直接提及「Tesla」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Stock Could Nearly Double to $200 in 2 Years, Analyst Says — Potential Apple, Tesla, and AI Chip De - Benzinga](https://news.google.com/rss/articles/CBMijAJBVV95cUxOc3pIU2NBYVY5TUp0LWpSR25xd3I3R2NDRXZtazBMeGZvQkxyLTFlS3hqS0xVQXNNNnBqb2ppcmJYNnF2NTFPd1NXQ2Y4cjlGMkRGRi1VZXdQZFh3UXd1UTNMWjdNVXpMRXNYR2t4d1JlMmNxTUpkREZEYlNTYnd4RjRYRXg5WXFHOG9sUGFJUS1ENnBfTHk4RmJlaW5uLWFFbnFTVzU0Q2YzS0xzd2hUazNrSkRMSi10akVNOVNBektsdGFVM1E1cm91bkYzYlE2bWI5TjN3NUVDb203bHc2c1F6SHVsYXZTUDVDSUFHdlkxbWtpMnQ5VTg5cjdZOTdpWWVnbEV1Ml8taEo1?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 17 Sep 2026 12:25:57 GMT
- [NPU 支援多種精度運算，對開發者建構 AI 應用生態有何助益？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMie0FVX3lxTE90RXMtbGxWVHBGSGJmVzd0c2hQZkRWNXhkc01ka1NUY25tRUlkNWJEaDdKVk9pbktfVG1MeDBtYThqZjQzdEtST2Vod2tOOXFUczZzclIwajd0MkZwendjRHVQZ1M1bGYzalJlVnBRZ2pGOHN6QWpUOTA3Yw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 17 Sep 2026 20:44:54 GMT
- [頂尖專家頻繁流動，Meta 該如何維持 Muse 等 AI 產品的後續研發？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMihgFBVV95cUxPVmF2WVhaeXVBRkpYMEtWc0JBczdYN1E5NVRGLVRId2oybGk4ZFNRWXRMZzAwSGZMSTctV3JudjR3dkJUOHFQLUZhZ2E1RUhyTE8wd1I4TmIteURabkF4M3FCNmkwVXh4Y2Z4c09ic3plUWNnaGwxRDJ3c0wxWEU3dlB5MkVGQQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 17 Sep 2026 20:11:27 GMT

## 新興題材：StocksToTrade

摘要：新興題材：StocksToTrade 相關新聞集中在：Intel Stock Jumps As Analysts Boost Targets And AI Bets Grow - StocksToTrade

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.21 | -5.13% | N/A | 108.80 | 114.68 | -5.13% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 方向判斷命中詞：boost。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Stock Jumps As Analysts Boost Targets And AI Bets Grow - StocksToTrade](https://news.google.com/rss/articles/CBMifEFVX3lxTE5BTzA3THlwdHJ4NGI4WFdkZmVIeGdib2FaN1NmU0NsNXFNLVZOYWg1NWdpOV9JckIyOTMzU2xZSGNwVjZzVlZNS3pIdlBrcEVnWlR5Wmp6RUVwU0ZJYkpkX2xSZ0dxeEZIVXBEalZUNVNtTmZNTGZnZldBbHc?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 17 Sep 2026 19:04:00 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股外資歸隊 拚戰新高 法人看好中秋連假後量能回升 - 經濟日報；台股回測季線支撐 操作低接不追高 法人連買強勢股具領漲抗跌優勢 | 市場焦點 | 證券 - 經濟日報；法人買超股 短打悍將 | 市場焦點 | 證券 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股外資歸隊 拚戰新高 法人看好中秋連假後量能回升 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE01Ty1YZEdFclZJMjVxQjFfcElHem4wUlcxb0JHa1JFV2gtYjEzbFNnSnFLaFg3aGdnLUstcG9QcE51bVJXR0VLd3pLN1luVGFfbElXSWkyaVhIQdIBX0FVX3lxTE1ka3JQWXlXM3BlTHlZTWMyelVWRjRnZUJzall1bDRxWWZwQmlxcmRiVlcxYVZIZHFmOUt3NjJBajdmc2VvcWxCMUhHSmRGd01LR0ZEd1A1X2RhY05EbWhj?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 17 Sep 2026 17:25:53 GMT
- [台股回測季線支撐 操作低接不追高 法人連買強勢股具領漲抗跌優勢 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1SYXhqNDdMN05uNERHYmRPX3ZwdlhWeTR4VFQzM1g5dzJWWjNUV2RpRzU2akppampyRW9fVXdpbGdaTTBpLVhnYmpyRHhMQlc5S2xhbTJqNk0tdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 17 Sep 2026 13:03:27 GMT
- [法人買超股 短打悍將 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBWV0VZUk53Qk0yYkxfbEU4QXkwS1AzbVhhbzJyOE5mWm1qb3g0SXpmVFprZ19qLTNGT3YyM2E5bnR2N0lYM0hSSW9aclR4Z3didEROTnIyaXVmUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 17 Sep 2026 15:10:02 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》量增收漲439點、重返46K，收復月線- 新聞 - MoneyDJ；台股破月線進場報酬優 主動市值ETF有助卡位 - MoneyDJ；個股動態報導內容-EB1E4013-7BA8-460E-9BEB-9B21D8EAB85E - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》量增收漲439點、重返46K，收復月線- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPX2twcXVNN1pRWVNwLWlKaW81NG0tTml5TFVkZG9xOFRDRFpsUGs3Nkt3Qk5GWUpnT1dsajRBUzRNM1dPdHdvWkFrQW0xeXFnZkVJZnNGcjlPRWhUMlFoQkRnZkNudGxKaHEyX24xSzlpbnZLNUpUVEJocm9Sc04xT0o4Vml0ZjFjOGZDMnpIWG9Rdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 17 Sep 2026 07:57:00 GMT
- [台股破月線進場報酬優 主動市值ETF有助卡位 - MoneyDJ](https://news.google.com/rss/articles/CBMiiwFBVV95cUxPNDJtdjQzYWJ3Z252MzlEMy0zZzA4ZkpEZnQyRHJMbXItd3NoUlR0dHFndnFjNG5tMDhfRmFmZENzNVpPZ3ZueURKWGVVMUVvR1pqTkVFUF80VjZYa1R6eEgyNlFydDM3UHVvNWZ0TjJ0WFdmNFlSd1U2U1dFVGd4TjRtb2RWajAxM1Zv?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 16 Sep 2026 02:44:00 GMT
- [個股動態報導內容-EB1E4013-7BA8-460E-9BEB-9B21D8EAB85E - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxQaEotczZXOVRVa3RoNTVrSVhkTmdFcnVYUWVYclNLeDFCUk4teng2NFhqZG9JcWM4RU1Ia2oteEx3YjRuY2RuV052ODBqSFVIQmdhX245T2EtZjUwN0taVTljM2dMQV9iSlVHUnIydWlXcVUzU0ZhUnhYcEFVR1UzZmhmZktqZllvRTAxdV9zUmVoVENJ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 17 Sep 2026 05:23:45 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
