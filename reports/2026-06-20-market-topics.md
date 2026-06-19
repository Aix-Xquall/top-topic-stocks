# 每日股市熱門話題分析 - 2026-06-20

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **新興題材：MoneyDJ**｜正向｜熱度 10｜市場確認 74.41｜同向 1/1
2. **記憶體與 HBM 供應鏈**｜正向｜熱度 8｜市場確認 67.93｜同向 3/4
3. **半導體與晶片供應鏈**｜正向｜熱度 6｜市場確認 63.24｜同向 4/5
4. **AI 伺服器與資料中心**｜正向｜熱度 11｜市場確認 37.15｜同向 3/6
5. **先進封裝與 CoPoS**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.29（樣本 19）
- 5日相關係數：0.21（樣本 19）
- 同向比例：12/19

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 新興題材：MoneyDJ | 74.41 | 1/1 | 0 | +1.47% | +7.11% |
| 記憶體與 HBM 供應鏈 | 67.93 | 3/4 | 1 | +5.14% | +23.04% |
| 半導體與晶片供應鏈 | 63.24 | 4/5 | 1 | +2.41% | +17.45% |
| AI 伺服器與資料中心 | 37.15 | 3/6 | 3 | +0.71% | +8.30% |
| 先進封裝與 CoPoS | N/A | 0/0 | 0 | N/A | N/A |
| 關稅與供應鏈轉移 | 36.59 | 1/2 | 0 | +0.53% | +4.95% |
| 散熱與液冷供應鏈 | 1.23 | 0/1 | 0 | +0.41% | -2.78% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
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
| 2026-06-18 | -0.41 | -0.41 | +42.86% | 7 |
| 2026-06-19 | 0.06 | -0.04 | +57.14% | 7 |
| 2026-06-20 | 0.29 | 0.21 | +63.16% | 19 |

## 歷史回測摘要

- 回測日期：2026-06-20
- 近5日 3日相關：0.16
- 近5日 5日相關：0.06
- 同向比例：+75.00%
- 權重狀態：未調整

- 方向準確度：+75.00%
- 信心排序準確度：0.16
- 診斷：弱正相關

調整原因：近 5 日有效樣本 8 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：新興題材：MoneyDJ 相關新聞集中在：首頁 ETF介紹 ETF全部持股 個股技術分析 - MoneyDJ；統一台股升級50主動式ETF基金五月份市場回顧與操作策略-報告內容-基金 - MoneyDJ；《台股盤後》電金權值領軍、收漲587點/創高；週K翻紅- 新聞 - MoneyDJ

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | +0.48 | +1.47% | +7.11% | 2,410.00 | 2,410.00 | 0.00% | 同向 | 74.39 | 32.40 | 416.98B TWD / 30.09% | 2026-06-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。

### 主要來源

- [首頁 ETF介紹 ETF全部持股 個股技術分析 - MoneyDJ](https://news.google.com/rss/articles/CBMidEFVX3lxTE5pNzJKMGc1Tmg4dnBNT3VIS1hoWU1OZVZmU21HSXhtc1M1MDdvNHotNHNxRGV3S1loLWszOFlvVG9lSVV3bkhSQU4zVVduTS1PTmdWNEthNGxTTHhyalY0RXMxUEtlLXJXN2hrMjRBeHUyODBz?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 18 Jun 2026 22:51:29 GMT
- [統一台股升級50主動式ETF基金五月份市場回顧與操作策略-報告內容-基金 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxQd0pfT2pBcERlNExOU2dmWXdaVXl3UVdtNmZnUXNMVUhZTU9XM3lEeHdNRzZhakpzQTBLRjNLYTNIUEszUm9qOHRNRkQzNkNveGF1bHRJc1U2d2VCdDhrQ1hnaWRzcHg0dnZEVDR5UmV6d3JaTW9oVHNLT2ZISkdHcmJlYjJsbExVUzB2WnhFTjA?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 18 Jun 2026 05:52:00 GMT
- [《台股盤後》電金權值領軍、收漲587點/創高；週K翻紅- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNakk5Smd5QVhaRGNNTXFvTzlKQzh6V3BaaHVSX1FReC1jUEFRd0NENGFXMTJBUFItYXV2ZkRHMGtmX2R2TXVRd0duNDF3dlc4cTVvRkdNWVRkclRJOFJXOUhEWmxvQlBMTEJtZTZaemlkVkQwYnk3aDF4RDFWRVdVSS1BMkxEZklFVmYzazRpN2tlZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 18 Jun 2026 07:57:00 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Analyst Warns Intel Valuation 'Doesn't Make Sense.' Suggests NVIDIA, AMD, Micron, and Broadcom as Alternatives. - 24/7 Wall St.；INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits；Micron Gets the Headlines, But Sandisk Could Offer More Upside - TradingView

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.65 | N/A | N/A | 1,133.99 | 1,133.99 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.65 | +3.65% | +16.12% | 2,184.75 | 2,184.75 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.56 | N/A | N/A | 537.37 | 537.37 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.56 | N/A | N/A | 133.99 | 133.99 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.50 | +5.57% | +18.91% | 210.69 | 211.14 | -0.21% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 新聞直接提及 | +0.48 | +12.81% | +28.38% | 298.01 | 312.06 | -4.50% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | +0.24 | -1.46% | +28.73% | 411.35 | 446.77 | -7.93% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、MU、memory」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 2 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Analyst Warns Intel Valuation 'Doesn't Make Sense.' Suggests NVIDIA, AMD, Micron, and Broadcom as Alternatives. - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi4AFBVV95cUxPNXJ3TlVIQWUzVkZzSnpYZlJGVUJtTE0xZEk3NDVLRmlPaU9zaVI3MlBzYmIxSWJQemVVTU9pZlhCS2daR3lLdXBGYWo2VVcxWGVvZXpKbkFYelRrTi12N1lLXzJwN0dJSFVSX0gwSXdiY1ZOQ2lIWUZsYnEzT0J4Q2U2c283MHdNYWlrSGduRjBqYkRRQ0ViY3cxVmttMWdTVHRuNVBVSTRidFdIa1lpQ2xZODRuR3pOU0VaLXlYSmM2OE5RVEZaN0JTWWNBNXlpQ1V0Ymg2MC1qUmJ4ZnVhSA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 19 Jun 2026 17:36:48 GMT
- [INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits](https://news.google.com/rss/articles/CBMi0AFBVV95cUxOWm5KdEIwSXpyY191UEhDa1V6NVpWa01UbmpJeWRIV0ttT080TmpDNEhISW5TWkQwUzBVYzBqSHJPWXRVNVJCampoWWRlYmhKVkhIeHBJLS0wLW5Ua09GQnRORXpFcW5qTEJkcnJGcW55aU5rOFVOLUFMbjRPZEpWT3A2ZllucnM0SU9JNEdrNUwyc3V2WHAtNFk3VHl4R1F6SkZRMFpleEE2Zl9MdW4tSEpMMnFGZ2hQZURWQ3B1WDlPR1BhRjJELVN5ODJWYVR3?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 19 Jun 2026 05:00:47 GMT
- [Micron Gets the Headlines, But Sandisk Could Offer More Upside - TradingView](https://news.google.com/rss/articles/CBMiuAFBVV95cUxNZkZyY2ducmdEak1tRkV3OU1aU1U5Y1paMDlOMG1KUDNlMGxnUl85MGtCTl9tM2k2RVBjanVKX3J2UlliRDFnLTJteTFxZXRTSVd3UldtelhQSml3SF92d21PTnV0RGgyUHF4VDN4NnJ0WTgtREptMjctNE9jLWpadFhsNlcwSVFnSXdSQU9uRlYxci1HdnRHQU1zRVNON1ZETFo0OUlCTUxEUm1tbzcxWFV5SENXdF9l?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 19 Jun 2026 19:00:00 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：台股狂飆587點創新高功率半導體掀漲停潮、國巨重返千金股- 證券 - 工商時報；Wall Street recovers from Fed slump, and the next step for Amazon's AI chip ambitions - CNBC；半導體原料戰開打！南韓挖到稀有「黑金」材料 不甩中國出口限制 - Yahoo股市

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | +0.07 | N/A | N/A | 133.99 | 133.99 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.04 | +1.47% | +7.11% | 2,410.00 | 2,410.00 | 0.00% | 同向 | 74.39 | 32.40 | 416.98B TWD / 30.09% | 2026-06-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.04 | +2.83% | +16.40% | 145.50 | 145.50 | 0.00% | 同向 | 4.00 | 36.56 | 22.94B TWD / 17.78% | 2026-06-01 |
| NVDA 輝達 | 產業/供應鏈推估 | +0.03 | +5.57% | +18.91% | 210.69 | 211.14 | -0.21% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.03 | N/A | N/A | 537.37 | 537.37 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | +0.03 | N/A | N/A | 1,133.99 | 1,133.99 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.03 | +3.65% | +16.12% | 2,184.75 | 2,184.75 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.01 | -1.46% | +28.73% | 411.35 | 446.77 | -7.93% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 CPU, server CPU, x86, foundry；其中 1 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 1 篇新聞出現相關標籤。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 1 篇新聞出現相關標籤。

### 主要來源

- [台股狂飆587點創新高功率半導體掀漲停潮、國巨重返千金股- 證券 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5PT3FiRUFhM0ZVM0p6WlVDbVRoNnRsY2VLTGZ0b2t3eUNON1JRdDZCbXNiay1QeFVLck9YNkJRWHdLaVZ0SzVkeVU3OGJrWklIanpwdDdDVy1HcF9TbUtr?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 18 Jun 2026 06:03:00 GMT
- [Wall Street recovers from Fed slump, and the next step for Amazon's AI chip ambitions - CNBC](https://news.google.com/rss/articles/CBMijAFBVV95cUxPdkgxdDVrZFJuR2ZMbU9sLVIxRzBFMzEtRF9zUXhCUjFReUdUSHFpTDdtQzUydTZIUmx4R2hkM29qczdaRTVUYXhiMlR5dmtQUm1IQUVjU0ZfMERwTUFWYk1ZZHB2NHhnR3pRajBOSHByd2tka0daSXBiQ2hEdlFDbDRuMEcwSkFJa3RjWg?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 18 Jun 2026 18:35:10 GMT
- [半導體原料戰開打！南韓挖到稀有「黑金」材料 不甩中國出口限制 - Yahoo股市](https://news.google.com/rss/articles/CBMimANBVV95cUxPdHl1UnJlX0Y3RDd0akZNMDAzM2t5a3AtVlduM0NQbXZfM0NJMXpCd2xZczdKbHRLWll6UEg4Y2tBWDNfdG5XSkQ1cDJlQ1ZJRVRxdXRicHZfTWczclpWZ3BSS0taZjdOel85bzFiT3FHM1ZjM3NvMW9PZE1wb0VwZTBoRmFMZ1BtT1Rweng3WkdKSUpXNzhLT0NyWlN4VGFidzd0bGppdXVpMEJJdVVwWG5tLV8xb3AtLUlaZ1JSeklPcnhxLVRCV1V3b3JLdk1zNjhCT2RDdzlZUlI2MTZnSG5VY085R1lEd1Z6T3ROYy14bE9MVEw5NVpzQlRGdWlMR2kyX1AwcWFGZXFmRmxxMy1DMGVJYzJ3VFU0cDRwT253dGRhcGU5QVpTbi05VG1iVEptdjdXZmJ4MXZ1X0pCRnd6SXlXWFFiY1p1RF9nRHdzbXE4VnZvVGRYVHBLZVdtX1BBLXRXUjh0R2JNX3lySkpDQl9oVUJvQUZRY19GSkVmSUhaQzBXY0EzNzRiSDU5LWtSN2h6aGo?oc=5) - Google News source discovery | Yahoo 奇摩股市 Fri, 19 Jun 2026 09:56:56 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：政府補助 50% 政策，能否加速中小型餐飲業 AI 應用的普及？ - cdn.technews.tw；Norway imposes near ban on AI in elementary school - Reuters；China tightens indium export checks as AI demand increases - Reuters

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | +0.08 | N/A | N/A | 133.99 | 133.99 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.06 | +5.57% | +18.91% | 210.69 | 211.14 | -0.21% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.06 | N/A | N/A | 537.37 | 537.37 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.06 | +1.47% | +7.11% | 2,410.00 | 2,410.00 | 0.00% | 同向 | 74.39 | 32.40 | 416.98B TWD / 30.09% | 2026-06-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.02 | -3.40% | -25.12% | 379.40 | 506.69 | -25.12% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -1.46% | +28.73% | 411.35 | 446.77 | -7.93% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.04 | +3.90% | +12.68% | 613.00 | 613.00 | 0.00% | 同向 | 10.86 | 56.92 | 63.03B TWD / 28.57% | 2026-06-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.02 | -1.79% | +7.47% | 4,390.00 | 4,390.00 | 0.00% | 背離 | 62.91 | 69.96 | 47.43B TWD / 4.99% | 2026-06-01 |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：benefit。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：benefit。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：benefit。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [政府補助 50% 政策，能否加速中小型餐飲業 AI 應用的普及？ - cdn.technews.tw](https://news.google.com/rss/articles/CBMifEFVX3lxTFB0VFA0WERWN1FDc1R1bW14YUYtTEEyYm5WeVFFdGU0Wm5GTnJWb1pjb3VTSkV2WFpxdUFTM0hSWEs2ZDdWRGdnMEVmQ0lxUjRNZkItcjdfLUg0ZWloSTZXS201aGI5dE1wa2VxQ3dlRmZ0UEdJazlIWHpfWkk?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 18 Jun 2026 08:11:16 GMT
- [Norway imposes near ban on AI in elementary school - Reuters](https://news.google.com/rss/articles/CBMilgFBVV95cUxNVkxUbENacTJvOWN5TXpEeWZGbmppRFVUVmthNUJHTlBlb09mdVdYeU10bzhFLXBIcl92VlpHU1UzQmV6WlhtS1V5ZHE1blNaODdQaWF1WU84Zm1aNHhuMkpEVHhEZVZSY0RMQjFJWTg5QmROeEtCUmtxTDNKSExGMUxDZkR6azVRc1RpQmliSzVuclBmT2c?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 19 Jun 2026 15:41:56 GMT
- [China tightens indium export checks as AI demand increases - Reuters](https://news.google.com/rss/articles/CBMipgFBVV95cUxNdkk1QUdvSW53RlVYM3prTVFxMmpkdlNfUUdrY3RsUDJtY09iSmxqV3ZlWTBjdHNjTkczZHhtVlJYNkVQZFEtOW1UWXM5Y2NRbmlibG9wNV9MS2ozeTZvYWQzX3ZsZGxBU1ZHeHNFUWFfNGlvTktaN2FYNk10T2dhSHVmeVctSXl3MEh3cGo3SmI3a0VrWWFNTjVzbzRLYUFQYjJsMUFB?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 19 Jun 2026 06:39:00 GMT

## 先進封裝與 CoPoS

摘要：先進封裝與 CoPoS 相關新聞集中在：群創領先投入面板級封裝受矚 友達握技術跨入光通訊 - Yahoo股市；台積電結合台日供應鏈發表玻璃基板封裝成果，給韓國對手強大威脅 - technews.tw

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | 0.00 | +1.47% | +7.11% | 2,410.00 | 2,410.00 | 0.00% | 不適用 | 74.39 | 32.40 | 416.98B TWD / 30.09% | 2026-06-01 |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | +3.90% | +12.68% | 613.00 | 613.00 | 0.00% | 不適用 | 10.86 | 56.92 | 63.03B TWD / 28.57% | 2026-06-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 同時符合主題標籤：advanced packaging, CoWoS, CoPoS, FOPLP。
- 3711：產業/供應鏈推估：公司標籤符合「先進封裝與 CoPoS」關鍵字 advanced packaging, CoPoS, FOPLP, panel-level packaging；其中 0 篇新聞出現相關標籤。

### 主要來源

- [群創領先投入面板級封裝受矚 友達握技術跨入光通訊 - Yahoo股市](https://news.google.com/rss/articles/CBMi8AJBVV95cUxQSmFEek44UkJaS2hibnVfNGlmcFJnc0tPRVE4dFFCSXRUcjlLaG1EcFdMTGtGS1YtOWI5WTF0VXU0X1NFTWxPZVh0R1F6VmFiZk1VSFhoOTdnWENQc1laWlhLb3p1Y3dPeWxBY0hXdTFidDBtSGtTdURiYnZSaWtocjQ4QjBsSTlKN3N4VVh4VDYwTlVrRXpVYXJ5eHRZamNKWXR5TWhOQzJrUVdURWdoWkc5YXlISlA5cXVjY0QwUVJJWUFJeGlPcmk2ZjBUc3VORlJBRktOaGxuTGx5WlVfbHllWkswbHVvMFg4bnctNW5HZkpYOFM0d2R2VzVjRHJ5UEhUQTRMR3VXS21fWXNfaWRRaG5nYjFSbWY2amVOOGFyRE9aSXhyb2MtbzZuZEEwdl9fXzRKemY1ZlEzYWE0Q053aE9PcUxzaVFHSlVCZ2piWXMwbkFleHYycXozTllrVTl3dWQyX3c0S1l0YjdESg?oc=5) - Google News source discovery | Yahoo 奇摩股市 Fri, 19 Jun 2026 07:10:06 GMT
- [台積電結合台日供應鏈發表玻璃基板封裝成果，給韓國對手強大威脅 - technews.tw](https://news.google.com/rss/articles/CBMi8gFBVV95cUxPVTZDVGxpOWJURVYweU5WS2lScjJIZURmdWxKYzQ2TjV1SGxPR0Fya0ZBdlVCa2RNRVdCcC1ZZ2JzeVVsSXFXUHlhUjJlcm1GWXFwWnQwWXMweEhWS3RyZndibm8waFBTajAtcnpWSms3UUlqdENSZS1jRGFRTkdMb1BuSGlRbUZnMGlXTGVPelV6cHMzVndkNUcyZWtoQl9uSFZEejRaV05oTENOcU10NUdPa1dFR1RRdlZOa2hHeFlSWjRJQUg4X2dwbkc1VWdBcGVuU2lnZngxUjhhSE1samFKUXNZaXk2a2NkVS11UUhvQQ?oc=5) - Google News source discovery | TechNews 科技新報 Thu, 18 Jun 2026 10:46:04 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：GB300出貨爆量、Rubin正式量產！「這檔」5月營收暴增172％！奇鋐、台光電、廣達…法人點名AI供應鏈13強1次看- 上市櫃 - 旺得富理財網；連噴5根仍未達目標價！「液冷關鍵廠」雙題材股價衝史高、EPS上修12.2元 打入AI巨頭供應鏈 - FTNN 新聞；即時部署解決方案將如何重塑資料中心供應鏈模式？ - cdn.technews.tw

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | +0.48 | +1.47% | +7.11% | 2,410.00 | 2,410.00 | 0.00% | 同向 | 74.39 | 32.40 | 416.98B TWD / 30.09% | 2026-06-01 |
| 3017 奇鋐 | 新聞直接提及 | +0.36 | -0.41% | +2.78% | 2,400.00 | 2,835.00 | -15.34% | 未明確 | 61.06 | 39.43 | 15.87B TWD / 60.64% | 2026-06-01 |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +12.81% | +28.38% | 298.01 | 312.06 | -4.50% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | +0.37% | +3.87% | 268.50 | 289.00 | -7.09% | 不適用 | 14.13 | 19.07 | 859.41B TWD / 39.57% | 2026-06-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。
- 3017：新聞直接提及「奇鋐」，共 1 篇新聞命中。
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [GB300出貨爆量、Rubin正式量產！「這檔」5月營收暴增172％！奇鋐、台光電、廣達…法人點名AI供應鏈13強1次看- 上市櫃 - 旺得富理財網](https://news.google.com/rss/articles/CBMiakFVX3lxTE9pOUxhbU4ybWl5TWR3TjhGTVJkU1Qta2RLV202amhVMnVSVkVfTFk4TlQ2QklzZVE4Nm9oLUp3ckRtdkRMQnBBQkF0MU9VR3g3VXZaNXc1SXJnc3RGQnB3aV9ZUU5QZjQzMHc?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 19 Jun 2026 02:06:10 GMT
- [連噴5根仍未達目標價！「液冷關鍵廠」雙題材股價衝史高、EPS上修12.2元 打入AI巨頭供應鏈 - FTNN 新聞](https://news.google.com/rss/articles/CBMiS0FVX3lxTE1haHk4NXN0eVJ2MFRONzR3bWZMNXBTdTBDTC10cVlabFZVUkFFUndSdnhRXzQxLXVWVFdQRlM2ZjNwRXFDZWdhV2JoUQ?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 18 Jun 2026 03:35:00 GMT
- [即時部署解決方案將如何重塑資料中心供應鏈模式？ - cdn.technews.tw](https://news.google.com/rss/articles/CBMiaEFVX3lxTE9ObmtYdDNTb18yZWw4dzNjVmJ4WE9tLTJidTc1LUw3bnVVR0N4VWxuN1dtcDFodFlXejBqLTZKMklEcTRELXhBNVhiRm1YakdVcWNXWHUwaWNmX3lhU2dKSGJPM01CZnZE?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 18 Jun 2026 16:31:50 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：GB300出貨爆量、Rubin正式量產！「這檔」5月營收暴增172％！奇鋐、台光電、廣達…法人點名AI供應鏈13強1次看- 上市櫃 - 旺得富理財網；焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報；連噴5根仍未達目標價！「液冷關鍵廠」雙題材股價衝史高、EPS上修12.2元 打入AI巨頭供應鏈 - FTNN 新聞

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | -0.43 | -0.41% | +2.78% | 2,400.00 | 2,835.00 | -15.34% | 未明確 | 61.06 | 39.43 | 15.87B TWD / 60.64% | 2026-06-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐、散熱」，共 2 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：跌停。

### 主要來源

- [GB300出貨爆量、Rubin正式量產！「這檔」5月營收暴增172％！奇鋐、台光電、廣達…法人點名AI供應鏈13強1次看- 上市櫃 - 旺得富理財網](https://news.google.com/rss/articles/CBMiakFVX3lxTE9pOUxhbU4ybWl5TWR3TjhGTVJkU1Qta2RLV202amhVMnVSVkVfTFk4TlQ2QklzZVE4Nm9oLUp3ckRtdkRMQnBBQkF0MU9VR3g3VXZaNXc1SXJnc3RGQnB3aV9ZUU5QZjQzMHc?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 19 Jun 2026 02:06:10 GMT
- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 19 Jun 2026 03:05:42 GMT
- [連噴5根仍未達目標價！「液冷關鍵廠」雙題材股價衝史高、EPS上修12.2元 打入AI巨頭供應鏈 - FTNN 新聞](https://news.google.com/rss/articles/CBMiS0FVX3lxTE1haHk4NXN0eVJ2MFRONzR3bWZMNXBTdTBDTC10cVlabFZVUkFFUndSdnhRXzQxLXVWVFdQRlM2ZjNwRXFDZWdhV2JoUQ?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 18 Jun 2026 03:35:00 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股多頭火種旺 操盤人近期反手買超這10檔 | 市場焦點 | 證券 - 經濟日報；台股熱帶動元大金市值向前衝至金控第四名 第三季將晉級兆元俱樂部 - 經濟日報；台股熱帶動元大金市值向前衝至金控第四名 第三季將晉級兆元俱樂部 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股多頭火種旺 操盤人近期反手買超這10檔 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1fYmxKRHoyVmx4Z2VxNlI3UW1ZMTByX1FvRWVkQVR0SUtmLXU2NXdSLUE4ZkZ3MFZ6TjJGQlM3Y3huWmlVNlZRV21aOEZVNkVzaVNXYlc2QzhEZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 19 Jun 2026 10:28:00 GMT
- [台股熱帶動元大金市值向前衝至金控第四名 第三季將晉級兆元俱樂部 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE0zR3V6QzdlNDdGRzl6M2hYU3IyUkdrOWdsMDdlRUFjNjBOang2LVR6N0lkQndfVnBIbHJjQ0xYakhuOHJ2NFBWdUdpUjl0dnVkOVB4Z0VIMHVpZ9IBX0FVX3lxTE92ek93amFmRXROMFNKY1Q2UUJsOHl3ZVhrQk83RWZ1Yks4akxiVTB3UEk5Rk85V1RDU0g3RTZmc1RkZGZnRVdMc1gyZXFCSXFhYjd2dWFmRlI1S1g2Vklr?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 19 Jun 2026 07:37:55 GMT
- [台股熱帶動元大金市值向前衝至金控第四名 第三季將晉級兆元俱樂部 - 經濟日報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE92ek93amFmRXROMFNKY1Q2UUJsOHl3ZVhrQk83RWZ1Yks4akxiVTB3UEk5Rk85V1RDU0g3RTZmc1RkZGZnRVdMc1gyZXFCSXFhYjd2dWFmRlI1S1g2Vklr0gFfQVVfeXFMT3Z6T3dqYWZFdE4wU0pjVDZRQmw4eXdlWGtCTzdFZnViSzhqTGJVMHdQSTlGTzlXVENTSDdFNmZzVGRkZmdFV0xzWDJlcUJJcWFiN3Z1YWZGUjVLWDZWSWs?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 19 Jun 2026 12:20:38 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
