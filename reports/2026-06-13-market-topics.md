# 每日股市熱門話題分析 - 2026-06-13

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **綜合市場情緒**｜負向｜熱度 49｜市場確認 90.73｜同向 1/1
2. **記憶體與 HBM 供應鏈**｜正向｜熱度 8｜市場確認 100.00｜同向 2/2
3. **散熱與液冷供應鏈**｜負向｜熱度 2｜市場確認 86.50｜同向 1/1
4. **AI 伺服器與資料中心**｜中性｜熱度 10｜市場確認 N/A｜同向 0/0
5. **半導體與晶片供應鏈**｜中性｜熱度 7｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.87（樣本 4）
- 5日相關係數：0.98（樣本 4）
- 同向比例：4/4

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 綜合市場情緒 | 90.73 | 1/1 | 0 | +6.91% | +3.32% |
| 記憶體與 HBM 供應鏈 | 100.00 | 2/2 | 0 | +11.54% | +21.39% |
| 散熱與液冷供應鏈 | 86.50 | 1/1 | 0 | +5.50% | +7.50% |
| AI 伺服器與資料中心 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：SpaceX | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：今年營收 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-05-30 | 0.16 | -0.06 | +71.43% | 7 |
| 2026-05-31 | 0.96 | 0.09 | +100.00% | 3 |
| 2026-06-01 | -0.92 | -0.72 | +16.67% | 6 |
| 2026-06-02 | 0.08 | 0.05 | +72.73% | 11 |
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

## 歷史回測摘要

- 回測日期：2026-06-13
- 近5日 3日相關：-0.38
- 近5日 5日相關：-0.21
- 同向比例：+33.33%
- 權重狀態：未調整

- 方向準確度：+33.33%
- 信心排序準確度：-0.38
- 診斷：方向與信心皆需修正

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

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台新 對 台光電(2383)個股 單一券商歷史明細 - justdata.moneydj.com；玉山-大里 對 翔耀(2438)個股 單一券商歷史明細 - justdata.moneydj.com；永豐金-信義 對 台塑化(6505)個股 單一券商歷史明細 - justdata.moneydj.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3037 欣興 | 新聞直接提及 | -0.50 | -6.91% | -3.32% | 902.00 | 1,055.00 | -14.50% | 同向 | 7.06 | N/A | 14.06B TWD / 32.37% | 2026-06-01 |

關聯理由（前 3）：
- 3037：新聞直接提及「欣興」，共 1 篇新聞命中。

### 主要來源

- [台新 對 台光電(2383)個股 單一券商歷史明細 - justdata.moneydj.com](https://news.google.com/rss/articles/CBMilgFBVV95cUxNVFVmMFozUll4eDZaZTBzMVdJN2ZDQXRqNXVXaHBzckt3bTlXQWtxYUhzSWVDemstLVViMW5xMWoyWkJ5ckJ2dlliRkdMVW8zUDNuUXhDUExKVjkyTXFadXJ1MXhXVlIyT2d5cjJ3dDRNdkdmcU1wdThTN1VWRER0S0JRMmtYejBMRHRPelB1Z2ZfWkJXTGc?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 12 Jun 2026 17:45:37 GMT
- [玉山-大里 對 翔耀(2438)個股 單一券商歷史明細 - justdata.moneydj.com](https://news.google.com/rss/articles/CBMikgFBVV95cUxPV2VWTnFpbGtMS3JPbkwwNlA2R2oxSWZ4X3NXV0NoUktnd1BxODZ2LVZHRnFPdzZGbFM5WmdxVVFqZkVBUVozWDFORWRoVmxjODZTWmN4TUxSNW9RX09XWHh0UzF6UWt0M0JaSm9lQmxqREpwMnNPdnR4dFNQbk5WSWRnOGlGWmlueURLeFdOMkswdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 12 Jun 2026 12:28:18 GMT
- [永豐金-信義 對 台塑化(6505)個股 單一券商歷史明細 - justdata.moneydj.com](https://news.google.com/rss/articles/CBMikgFBVV95cUxOV1JKZlhRVWxUeE1SVVRBM0VGNHlqYzhacnlwZlF0UWo2dHNyVE5SQ2RNaVFDRzBmbWZuV1J4b1E2aU9ncDk1YWlJWjd0MmJKaTJFVkh3VHA5dV85Q0NoTWRUOEtNWnBGOVYzVDhkRjZCdEh3RUdDcTh2cUtxTEg3eFVSc1hfeWowVDlVSEtaVENZQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 12 Jun 2026 06:12:28 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits；Top AI Memory Stocks in 2026: Which Stocks Are Worth Watching? - Moomoo；The Zacks Analyst Blog Highlights Micron Technology, Marvell Technology, NVIDIA and Sandisk - Yahoo Finance Singapore

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.68 | N/A | N/A | 981.61 | 995.87 | -1.43% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.68 | +20.26% | +26.98% | 1,980.10 | 1,980.10 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.52 | +2.82% | +15.80% | 205.19 | 211.14 | -2.82% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.50 | N/A | N/A | 511.57 | 516.10 | -0.88% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.50 | N/A | N/A | 124.57 | 124.57 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、memory、Micron Technology」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 2 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits](https://news.google.com/rss/articles/CBMi0AFBVV95cUxOWm5KdEIwSXpyY191UEhDa1V6NVpWa01UbmpJeWRIV0ttT080TmpDNEhISW5TWkQwUzBVYzBqSHJPWXRVNVJCampoWWRlYmhKVkhIeHBJLS0wLW5Ua09GQnRORXpFcW5qTEJkcnJGcW55aU5rOFVOLUFMbjRPZEpWT3A2ZllucnM0SU9JNEdrNUwyc3V2WHAtNFk3VHl4R1F6SkZRMFpleEE2Zl9MdW4tSEpMMnFGZ2hQZURWQ3B1WDlPR1BhRjJELVN5ODJWYVR3?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 11 Jun 2026 17:36:22 GMT
- [Top AI Memory Stocks in 2026: Which Stocks Are Worth Watching? - Moomoo](https://news.google.com/rss/articles/CBMifEFVX3lxTE0xdDZURldJM2NCVHA3bnA2SjJDNXdqSVFWYnhIbk0xb3gzT3BTNmFZTi1ITXFyV1hTZ25QTktsQWZxUUFOcG9kQk1nTDBaMy1zbzZNTWc3U1Y1cVl0Z0swOUVoNlpMLVotNzBRYTBEOGpHSmQta1dkWVE4TWs?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 12 Jun 2026 08:37:00 GMT
- [The Zacks Analyst Blog Highlights Micron Technology, Marvell Technology, NVIDIA and Sandisk - Yahoo Finance Singapore](https://news.google.com/rss/articles/CBMijgFBVV95cUxOc0NSTmsxYUt1ZEVGSVVwRFJIcVFFamRRdWdqY0h0dFFmRjlvdEJuNFZ1LUFMY05rZUdIZDJTWlRIYnFINHpfMkVEb2s1bnRVVERJdnBQYWxGclJUNGljd2ZLRlFyV1A3MnhTMmxkVHFNRE1nWXl5dFZaSUVibURwa3EtZENaTngxd0gwWWV3?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 12 Jun 2026 14:38:00 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：奇鋐、雙鴻 押價內外15% - 經濟日報；焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | -0.61 | -5.50% | -7.50% | 2,405.00 | 2,835.00 | -15.17% | 同向 | 61.06 | N/A | 15.87B TWD / 60.64% | 2026-06-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐、散熱」，共 2 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：跌停。

### 主要來源

- [奇鋐、雙鴻 押價內外15% - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBjZVg1MERzYnZaUXBwQmR0Ri10NW91dzdNdDdDemYtdkV2cF9RSGk0TlVzZkhHSFFqUGZxVEEybjZrZXdKQnJWZzUyTUh3dGFWeTlqUzlXb3NLZ9IBX0FVX3lxTE1tdy1yYWRXX3RER0pfMFNuNE5jeWJsVlN1MGlMQTM1ZmtRRURiYUc4NlJDU1dhQTJGcGFiTldCRXVpMXR6Tlg3UFpOWjYySEk2RUVGblJ2WlNXYTBqRVgw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 11 Jun 2026 09:00:00 GMT
- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 12 Jun 2026 06:12:01 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：2 Popular AI Stocks to Sell Before They Drop 44% and 60%, According to Wall Street - The Motley Fool；精湛轉型 AI 視覺，對提升檢測毛利與技術門檻有何影響？ - TechNews 科技新報；AI 導入如何解決 AOI 過殺痛點，並優化客戶製程損耗成本？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 124.57 | 124.57 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +2.82% | +15.80% | 205.19 | 211.14 | -2.82% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 511.57 | 516.10 | -0.88% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +0.22% | -2.33% | 2,310.00 | 2,355.00 | -1.91% | 不適用 | 74.39 | N/A | 416.98B TWD / 30.09% | 2026-06-01 |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | -0.51% | -22.88% | 390.74 | 506.69 | -22.88% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -8.47% | +19.57% | 382.07 | 446.77 | -14.48% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | +3.69% | +2.25% | 590.00 | 611.00 | -3.44% | 不適用 | 10.86 | N/A | 63.03B TWD / 28.57% | 2026-06-01 |
| 2454 聯發科 | 產業/供應鏈推估 | 0.00 | -6.59% | -2.79% | 4,180.00 | 4,310.00 | -3.02% | 不適用 | 62.91 | N/A | 47.43B TWD / 4.99% | 2026-06-01 |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [2 Popular AI Stocks to Sell Before They Drop 44% and 60%, According to Wall Street - The Motley Fool](https://news.google.com/rss/articles/CBMilgFBVV95cUxPVmpnZ0JPd1N1WVp1OGR5Sm9kVWV1UkR6U3dKTUxxNmpONUpxQkk5dFM3bUI1OHFqV2tjM0cxVDZqVlN6RU1HeWVVWDNoMHl2cWtsZEYzTE5hWDhDdkpZSWlNU2ZFTGJmSXQtaEJScEVSQ1ROUHFWQ01xaEJkNFUzcy0wcUVRUHdaVGd2WlZPVGlidHFnSmc?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 12 Jun 2026 10:12:00 GMT
- [精湛轉型 AI 視覺，對提升檢測毛利與技術門檻有何影響？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMib0FVX3lxTFBTUkZhNk1ySnRWa056MEt2aHRrWFdGRmxIdFphbDAzam1UdDQ2UTdtTl9FaDBYMzh4WF9WSzMtandTT01Dek80SVVfNUVmTGtjY2dwa1VUSU9tUlpoekstXzc2ZDI2THFJeXFPS29KQQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 12 Jun 2026 20:33:41 GMT
- [AI 導入如何解決 AOI 過殺痛點，並優化客戶製程損耗成本？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMib0FVX3lxTE9ucmVBY3NpcUVDcTJkNS1FclJxVW1ldHhfOThHUGtoSzRlYl9XSDM0TTNGNkhrQ0lFbV9fdERlN0ZKbjhfdnRGdnZJZk4wbFE5OEFTejhONUZqTkpSQ0ZlR0F3ZjRZNVNsUDhtbVVJcw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 12 Jun 2026 20:33:44 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel Is Up 8% Today: Is It Outperforming Other Chip Stocks Like AMD and NVIDIA? - 24/7 Wall St.；Intel Is Up 8% Today: Is It Outperforming Other Chip Stocks Like AMD and NVIDIA? - AOL.com；總統見證動土 屏東半導體專區啟動 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 124.57 | 124.57 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +2.82% | +15.80% | 205.19 | 211.14 | -2.82% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | N/A | N/A | 511.57 | 516.10 | -0.88% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | 0.00 | +0.22% | -2.33% | 2,310.00 | 2,355.00 | -1.91% | 不適用 | 74.39 | N/A | 416.98B TWD / 30.09% | 2026-06-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +4.71% | +1.52% | 133.50 | 144.50 | -7.61% | 不適用 | 4.00 | N/A | 22.94B TWD / 17.78% | 2026-06-01 |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 981.61 | 995.87 | -1.43% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | +20.26% | +26.98% | 1,980.10 | 1,980.10 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -8.47% | +19.57% | 382.07 | 446.77 | -14.48% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Is Up 8% Today: Is It Outperforming Other Chip Stocks Like AMD and NVIDIA? - 24/7 Wall St.](https://news.google.com/rss/articles/CBMivgFBVV95cUxOMmZraGthM1NZSHdVbm1nSlVJYmlJdTJvemEtakZ1MjFwbzJoNmhMa3lBTVFBMlpnMHhtekwxQUh0R1BzMGZOTXcyc2l1NnhnbGZKMDJTc3lIMkNfRHBRYlVOZkxXaVVKaV9Xalg4S1p2bHBmZEszQWF5QVFJV0loLUJqeDgtU1QtWmc1aWhxMnNRUHR2X1dmTVF2dFk5UG5ZdkhELWV0U0JxU280SVA0ZTl5TGtGcnEwZFljLVBR?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 12 Jun 2026 17:36:17 GMT
- [Intel Is Up 8% Today: Is It Outperforming Other Chip Stocks Like AMD and NVIDIA? - AOL.com](https://news.google.com/rss/articles/CBMigwFBVV95cUxNYm5xODREWVFsUV9hd2RHbXI1SWZjSnNlU3lQcmY3Tkd5ZS0taUg0QV9JNlYyQTJjU0x4TFkxSU42aWcyN0FkVEVtbnZxRi0tdGVwSmV5aHVEbkZxR0pZRFNpamhUc1Nhay1hM3FaY3QxMnVPaGc4VHoyVkV1cVVTLTg3SQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 12 Jun 2026 17:55:34 GMT
- [總統見證動土 屏東半導體專區啟動 - 中央社 CNA](https://news.google.com/rss/articles/CBMiU0FVX3lxTFB1NDZoc2N1V09sSkxjUEtFZVFxNE9ZcXp1czRLc0FzTkNZUmdjMktGMHBpTnhQX2hLNWFoRU5jMVFzdHNTLWN4T0Vrd3Z4RE1WVWV3?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 12 Jun 2026 08:59:36 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》收漲1019點、收復月線；週K翻黑- 新聞 - MoneyDJ；統一證券：台股短線高檔震盪格局- 新聞 - MoneyDJ；國票證券：台股有望重返月線之上- 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》收漲1019點、收復月線；週K翻黑- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNS0w0MHYtSTBpZlpPakJvTkQwMUVPZ0RmczBiRzN6dVRGRWJYSTQ1TGY3R0R1aUZwVmlleFlBTlpQSFdZSC1iODduMWZ2MHlUdEE4YVR3R3QzYlBRa3FLSWpoYk9wVFROWnBmN21HWWZBdTg4REs4cFNlRjVXZmJQVmp1MlljRmFqYlV0bUZhMnZqdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 12 Jun 2026 07:59:00 GMT
- [統一證券：台股短線高檔震盪格局- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQUVVITUI5VUdtaEpja1U4bHVrem9pMEJRNGNWall6RzlXcDNxYnFoZEdSb2EzdHVYbzdnNnJtWkNEb3gxQXEzNm9rc0pBeEZxUm54RHgzd2RPNExmM1R5Z08tOGZtb2REc2JEOXdjcmRBbmFBY2t4aDJDOXFZUTFlNkxfazRJem5JMTFoZHNJZzNJQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 12 Jun 2026 00:45:00 GMT
- [國票證券：台股有望重返月線之上- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNQ1RDSGJQb0tvOC1TY1oxblQxUFdITklsd21fTmx3TmZEZVFmWUwzMlJjVE1RbU03Sl80X0duWlRLejJLRVp3dlMtXzNPMk9BNE5UZTR1VXBid29LSXlNamxiWXBGMXh2WGdwcUQ4SUlRTzFhVi1na0ZNcWFLR29fbTY0aXRTYmtYZDk4UmdiWUpJUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 12 Jun 2026 00:45:00 GMT

## 新興題材：SpaceX

摘要：新興題材：SpaceX 相關新聞集中在：Space stocks slump as blistering rally cools after SpaceX market debut - Reuters；Stocks rise as SpaceX makes market debut; oil slides on Gulf peace hopes - Reuters；SpaceX just went public. This analyst thinks these related stocks are worth buying - CNBC

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [Space stocks slump as blistering rally cools after SpaceX market debut - Reuters](https://news.google.com/rss/articles/CBMiwAFBVV95cUxQZ3V5alJuSTF4eVE5Y25rS0JDZGRVQmZubUQyclBTU3A5N3NBOUFoRWMxdXd2RWp4NXEtMGp3aHNnZy1kQlRzaHBMaWZFSjdSMHFqdWpaaUlXalVkOG1uZHV5WElCTFZyZ2FIQllrdlpHOWxxOG5oVTlQaWpuMWxwdC1NTDFZRU82UDdINlNsaWdmaHRzZzU1eVgyaFB0ZzhhSVRjc2d6QjEwTk8zVVo3bkNibG5ONHU3QUptb2hCMTM?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 12 Jun 2026 19:01:09 GMT
- [Stocks rise as SpaceX makes market debut; oil slides on Gulf peace hopes - Reuters](https://news.google.com/rss/articles/CBMigwFBVV95cUxPV1pjRmJPbG9FY2Q3ekpEY1dDQTI3aWU0MzdqR0tMbDdKNjdkWHNDRGk3TEdFbDVzeHBZODUyS20yNnpuWHR0N2xPRHFPWHN4QlA3QzNUM1BONlRJakJfdGpTOWYybHU2ZTBfM29JamNOc096OWgzd0FRa01GN1BWbzNraw?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 12 Jun 2026 00:40:00 GMT
- [SpaceX just went public. This analyst thinks these related stocks are worth buying - CNBC](https://news.google.com/rss/articles/CBMiugFBVV95cUxNQTN5TXNXaERyTWYwTFJMc1I5MklMWlBpTXlpbUxaZVM5OGlNRG93b1RpYTIwWnFhbklHaE5hZFNEaXBvc1ZyMkwzUlBfQlZNdkdlX1VtSWdHUTVJVnNjQXVSa0J1ODVCNmR4NHVSWkZyNXp3aTRNSjA1TXFhWXcwR0VwUWRCS3pyYnh6cGRVWTZ1a0JYMkpqX2I2WWt3dFhPakRRbXBPNHRIaXFDRmNydjlHVXdFUjl3LUE?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 12 Jun 2026 16:30:44 GMT

## 新興題材：今年營收

摘要：新興題材：今年營收 相關新聞集中在：Vera Rubin放量，它訂單能見度到2029年，今年營收年增60%，明年拚再成長33% - 經濟日報；漢唐在手訂單近1,940億，今年營收有望創新高- 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [Vera Rubin放量，它訂單能見度到2029年，今年營收年增60%，明年拚再成長33% - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5TYzdIS0tQWWRyeGJ4Y1lYUHB4cEh0X0RYZlJXQXRybXJCX2pJU1VuRS1ycnJoQ015RmUzMFJjU1F0ZmE5aF83TjJ4LTB2Ry1jUno5QlNmaGhIUdIBX0FVX3lxTE1UdXA0TlBLMHkwX0N1UWNWOTIwSEhCOVdla2R4VFZMNVNseF9fX2xPNTdaV3dIM1Z2OUlmZ1VZNkhfdFZ0eGpxYWdmN1ZCLUtBWmxPSHZjMklvdHJzWWdN?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 12 Jun 2026 16:10:31 GMT
- [漢唐在手訂單近1,940億，今年營收有望創新高- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQcFdqbk45VUhhMDBXTzFMVXNScmJxTXVaNEpGa2dNeE9lb0lZRGloN3hpZndqcEFDZUJJOGRPTHNWYkVaMTlzeENlbzJXR2JqRmlIcUFiUDFRak5US0RmZzhCSGdlZU5KUWQ5QmlJVk53TzNGUVdTNEx1NURIZEJuZGQzVkktczFyaVhINU81dXlWdw?oc=5) - Google News source discovery | MoneyDJ Thu, 11 Jun 2026 08:58:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
- TWSE PER/PBR 抓取失敗：Expecting value: line 1 column 1 (char 0)
