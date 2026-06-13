# 每日股市熱門話題分析 - 2026-06-14

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜正向｜熱度 8｜市場確認 100.00｜同向 2/2
2. **散熱與液冷供應鏈**｜負向｜熱度 2｜市場確認 86.50｜同向 1/1
3. **AI 伺服器與資料中心**｜中性｜熱度 14｜市場確認 N/A｜同向 0/0
4. **關稅與供應鏈轉移**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0
5. **半導體與晶片供應鏈**｜中性｜熱度 5｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.82（樣本 3）
- 5日相關係數：0.98（樣本 3）
- 同向比例：3/3

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 100.00 | 2/2 | 0 | +11.54% | +21.39% |
| 散熱與液冷供應鏈 | 86.50 | 1/1 | 0 | +5.50% | +7.50% |
| AI 伺服器與資料中心 | N/A | 0/0 | 0 | N/A | N/A |
| 關稅與供應鏈轉移 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：SpaceX | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
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
| 2026-06-14 | 0.82 | 0.98 | +100.00% | 3 |

## 歷史回測摘要

- 回測日期：2026-06-14
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

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits；Why I'm Still Holding Every Micron Share (NASDAQ:MU) - Seeking Alpha；Top AI Memory Stocks in 2026: Which Stocks Are Worth Watching? - Moomoo

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.68 | N/A | N/A | 981.61 | 981.61 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.68 | +20.26% | +26.98% | 1,980.10 | 1,980.10 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.52 | +2.82% | +15.80% | 205.19 | 211.14 | -2.82% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.50 | N/A | N/A | 511.57 | 516.10 | -0.88% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.50 | N/A | N/A | 124.57 | 124.57 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、memory、Micron Technology」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally, surges, 52-week highs, hit 52-week highs, rockets。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk、SNDK」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：surges, rockets。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits](https://news.google.com/rss/articles/CBMi0AFBVV95cUxOWm5KdEIwSXpyY191UEhDa1V6NVpWa01UbmpJeWRIV0ttT080TmpDNEhISW5TWkQwUzBVYzBqSHJPWXRVNVJCampoWWRlYmhKVkhIeHBJLS0wLW5Ua09GQnRORXpFcW5qTEJkcnJGcW55aU5rOFVOLUFMbjRPZEpWT3A2ZllucnM0SU9JNEdrNUwyc3V2WHAtNFk3VHl4R1F6SkZRMFpleEE2Zl9MdW4tSEpMMnFGZ2hQZURWQ3B1WDlPR1BhRjJELVN5ODJWYVR3?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 12 Jun 2026 20:36:33 GMT
- [Why I'm Still Holding Every Micron Share (NASDAQ:MU) - Seeking Alpha](https://news.google.com/rss/articles/CBMihwFBVV95cUxOdzAwSXI4NllzenZjdWd2OWNIUEdrcmt4SHh4cUJ1X0hxUUMtS0FESEtJV290NkNJT2lSalRENERVOEQ4YUNhV0drd0llYmotdFE2cEdKSnlKalBDODQ0ckE5bTY5bmVFRnNVZzlQQlM0cXpFNmNlMGhnR2hmSEozNG5Hb3BXZW8?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 13 Jun 2026 13:00:21 GMT
- [Top AI Memory Stocks in 2026: Which Stocks Are Worth Watching? - Moomoo](https://news.google.com/rss/articles/CBMifEFVX3lxTE0xdDZURldJM2NCVHA3bnA2SjJDNXdqSVFWYnhIbk0xb3gzT3BTNmFZTi1ITXFyV1hTZ25QTktsQWZxUUFOcG9kQk1nTDBaMy1zbzZNTWc3U1Y1cVl0Z0swOUVoNlpMLVotNzBRYTBEOGpHSmQta1dkWVE4TWs?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 12 Jun 2026 08:37:00 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：非氟碳冷卻液革命！美超微 SMC PG25-A 高阻抗冷卻液如何改寫 AI 資料中心散熱賽局與台美股供應鏈｜股市話題 - sinotrade.com.tw；焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | -0.61 | -5.50% | -7.50% | 2,405.00 | 2,835.00 | -15.17% | 同向 | 61.06 | 39.52 | 15.87B TWD / 60.64% | 2026-06-01 |
| AMD 超微 | 新聞直接提及 | -0.50 | N/A | N/A | 511.57 | 516.10 | -0.88% | N/A | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 2 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：跌停。
- AMD：新聞直接提及「超微」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [非氟碳冷卻液革命！美超微 SMC PG25-A 高阻抗冷卻液如何改寫 AI 資料中心散熱賽局與台美股供應鏈｜股市話題 - sinotrade.com.tw](https://news.google.com/rss/articles/CBMi9ARBVV95cUxQR3BZMlpsamJ1al9KdHNmUENzbXJxSnAxZGh6MDFPazFnRGtPWWR3bDFCTTZ1MmJmZjYwMWFIaWhaWHlnZEJuQjhkN3B0WnhCYXlxOHRWcy1UeG9GN3VFUGZ1UEJIYWROMmc0LTg4YVI2YzZLYmRaS25pYjNEM0dhS21sWjQtMW9sSTFXMEd6bFNoNEJ0Rmg1WjBwNzJXNEtZT3FiNkNOY2Z6UzRVR19GSGthcFN4RDJ4OWZyMWxFbjYwX2NGV2ZOemxiNy0zeU1ZaVA3cVNsZEkyNF9lRG9MdTNkdTZBRm9jM0J6MFdyN0pTRjZHSVh0cmoyLV9PX240Y0xUaW1BV19oUE9yWjVXNjEtQy0tVW5CSXFOS1VtSUZVQjVSRWlOc2RzR3VTRERwbllHZVA0UGt5OC1kN0tGSlROZXc1SEdnWjhLeTh5Qk5pRkpPTzV6VFhPdWd1LVpqdHVGZTRBNW5FdXVBZjRiakcycUUtRlVpOHlTem9DZi05RTJTZmdEcnA0LW5KZDdNWTdKSG40eTZ2QmwzVmtPUzdReVpZeC11cTNONkFTNFJOMDdpN0JzdnAxV0JNenJxQ0RvdkdlUTF4bjFmOXNUa0U4SXg2eFNnNDZrYVQxdXA1Z3BuU1RlbFdXZlJDUDNFMnJmNzdRa3BvWkR6TlphUDlZUjR5TWNlUHVfSnhIcWRpelRoR1lWdHNDMGF5ZGZobkwxSFpFU3pOUGlhVkIxdktFeDh2OUJJaWFUc0g5NUg0SG1uZEhKT0VKNTVsb0k5QzBPLV9ieWEzSm9Qc1RCQ0cwOU1NYjVqelBsOENYRUY5S2hT?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 12 Jun 2026 05:14:01 GMT
- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 12 Jun 2026 21:09:24 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Why Intel, AMD, Arm, and Other Artificial Intelligence (AI) Stocks Popped Today - AOL.com；2 Popular AI Stocks to Sell Before They Drop 44% and 60%, According to Wall Street - The Motley Fool；當 AI 競爭轉向成本效率，哪些二線廠商將迎來轉機？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 124.57 | 124.57 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | N/A | N/A | 511.57 | 516.10 | -0.88% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +2.82% | +15.80% | 205.19 | 211.14 | -2.82% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +0.22% | -2.33% | 2,310.00 | 2,355.00 | -1.91% | 不適用 | 74.39 | 31.06 | 416.98B TWD / 30.09% | 2026-06-01 |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | -0.51% | -22.88% | 390.74 | 506.69 | -22.88% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -8.47% | +19.57% | 382.07 | 446.77 | -14.48% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | +3.69% | +2.25% | 590.00 | 611.00 | -3.44% | 不適用 | 10.86 | 54.78 | 63.03B TWD / 28.57% | 2026-06-01 |
| 2454 聯發科 | 產業/供應鏈推估 | 0.00 | -6.59% | -2.79% | 4,180.00 | 4,310.00 | -3.02% | 不適用 | 62.91 | 66.61 | 47.43B TWD / 4.99% | 2026-06-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Why Intel, AMD, Arm, and Other Artificial Intelligence (AI) Stocks Popped Today - AOL.com](https://news.google.com/rss/articles/CBMidkFVX3lxTE5EX1pfT3Zkc1RMMU9NTVo1b2dpV1ZFS1Q1ODBrVjVuZ2RLTlJ2Z1pfWEpDeHcyVFVqdkJlczlZM19GSThNc2kyczljM1dGS0xHRWdsNkVqcExqaGRfTmlBSGgtSDZRSjBkcFhLX2xRRHdmSmJmQ1E?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 13 Jun 2026 01:24:17 GMT
- [2 Popular AI Stocks to Sell Before They Drop 44% and 60%, According to Wall Street - The Motley Fool](https://news.google.com/rss/articles/CBMilgFBVV95cUxPVmpnZ0JPd1N1WVp1OGR5Sm9kVWV1UkR6U3dKTUxxNmpONUpxQkk5dFM3bUI1OHFqV2tjM0cxVDZqVlN6RU1HeWVVWDNoMHl2cWtsZEYzTE5hWDhDdkpZSWlNU2ZFTGJmSXQtaEJScEVSQ1ROUHFWQ01xaEJkNFUzcy0wcUVRUHdaVGd2WlZPVGlidHFnSmc?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 12 Jun 2026 10:12:00 GMT
- [當 AI 競爭轉向成本效率，哪些二線廠商將迎來轉機？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMijwFBVV95cUxPaEI4YUlHRC02NW9EWE9EamRuZmdRcFItc0dsc2ViNGpZakl2M0xvWXpiN2dzUDBYeWJEcTdpdFR6RHFFMkNfdzFFQ3BzVGEtaHlxc1FVeTFWYUFtNi1SRXVHUlZJSDdURG8zS2ZFQTNFb09xY3Qwa1ItdHpSbS1QOVVoaWJsSHNXQUZ5STl0RQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 13 Jun 2026 19:55:11 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：非氟碳冷卻液革命！美超微 SMC PG25-A 高阻抗冷卻液如何改寫 AI 資料中心散熱賽局與台美股供應鏈｜股市話題 - sinotrade.com.tw；屏東要變半導體重鎮？台積電攜7廠進駐供應鏈名單、布局全曝光- 日報 - 工商時報；台積電聯合七大供應鏈進駐屏科估創360億元年產值- 產業 - 工商時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | 0.00 | +0.22% | -2.33% | 2,310.00 | 2,355.00 | -1.91% | 不適用 | 74.39 | 31.06 | 416.98B TWD / 30.09% | 2026-06-01 |
| AMD 超微 | 新聞直接提及 | 0.00 | N/A | N/A | 511.57 | 516.10 | -0.88% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | -5.50% | -7.50% | 2,405.00 | 2,835.00 | -15.17% | 不適用 | 61.06 | 39.52 | 15.87B TWD / 60.64% | 2026-06-01 |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +10.20% | +25.41% | 291.13 | 312.06 | -6.71% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | -6.13% | -8.44% | 260.50 | 289.00 | -9.86% | 不適用 | 14.13 | 18.50 | 859.41B TWD / 39.57% | 2026-06-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 2 篇新聞命中。
- AMD：新聞直接提及「超微」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 3017：新聞直接提及「散熱」，共 1 篇新聞命中。

### 主要來源

- [非氟碳冷卻液革命！美超微 SMC PG25-A 高阻抗冷卻液如何改寫 AI 資料中心散熱賽局與台美股供應鏈｜股市話題 - sinotrade.com.tw](https://news.google.com/rss/articles/CBMi9ARBVV95cUxQR3BZMlpsamJ1al9KdHNmUENzbXJxSnAxZGh6MDFPazFnRGtPWWR3bDFCTTZ1MmJmZjYwMWFIaWhaWHlnZEJuQjhkN3B0WnhCYXlxOHRWcy1UeG9GN3VFUGZ1UEJIYWROMmc0LTg4YVI2YzZLYmRaS25pYjNEM0dhS21sWjQtMW9sSTFXMEd6bFNoNEJ0Rmg1WjBwNzJXNEtZT3FiNkNOY2Z6UzRVR19GSGthcFN4RDJ4OWZyMWxFbjYwX2NGV2ZOemxiNy0zeU1ZaVA3cVNsZEkyNF9lRG9MdTNkdTZBRm9jM0J6MFdyN0pTRjZHSVh0cmoyLV9PX240Y0xUaW1BV19oUE9yWjVXNjEtQy0tVW5CSXFOS1VtSUZVQjVSRWlOc2RzR3VTRERwbllHZVA0UGt5OC1kN0tGSlROZXc1SEdnWjhLeTh5Qk5pRkpPTzV6VFhPdWd1LVpqdHVGZTRBNW5FdXVBZjRiakcycUUtRlVpOHlTem9DZi05RTJTZmdEcnA0LW5KZDdNWTdKSG40eTZ2QmwzVmtPUzdReVpZeC11cTNONkFTNFJOMDdpN0JzdnAxV0JNenJxQ0RvdkdlUTF4bjFmOXNUa0U4SXg2eFNnNDZrYVQxdXA1Z3BuU1RlbFdXZlJDUDNFMnJmNzdRa3BvWkR6TlphUDlZUjR5TWNlUHVfSnhIcWRpelRoR1lWdHNDMGF5ZGZobkwxSFpFU3pOUGlhVkIxdktFeDh2OUJJaWFUc0g5NUg0SG1uZEhKT0VKNTVsb0k5QzBPLV9ieWEzSm9Qc1RCQ0cwOU1NYjVqelBsOENYRUY5S2hT?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 12 Jun 2026 05:14:01 GMT
- [屏東要變半導體重鎮？台積電攜7廠進駐供應鏈名單、布局全曝光- 日報 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1kLWMyVzM5ZE15VnctdE1xVC0zRGl6Q2FSWjRSQ2U5U1ItVmdLcUR1dFlCSE00Q25lbHNpckc3eXFkU3pxenQwSHozVXYwYjNrVXl5NVZqOFdpLXhELXpv?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 12 Jun 2026 19:00:00 GMT
- [台積電聯合七大供應鏈進駐屏科估創360億元年產值- 產業 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1lNXJ4MnpkT1lyYXVib0xsRmZMRWEyZzc2Tk1Lc1Q3TVp2WnowQ0ZuUWJOVDNRckJXRHBDSkFSMmpSY2gwQlU3MG51T1U5YnZoX0VVNjBMV2l6ZW0yMGVj?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 12 Jun 2026 07:11:00 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel Is Up 8% Today: Is It Outperforming Other Chip Stocks Like AMD and NVIDIA? - 24/7 Wall St.；總統見證動土 屏東半導體專區啟動 - 中央社 CNA；南華大學推動半導體學程赴美深化合作 攜手美國名校共育國際人才 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 124.57 | 124.57 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +2.82% | +15.80% | 205.19 | 211.14 | -2.82% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | N/A | N/A | 511.57 | 516.10 | -0.88% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +0.22% | -2.33% | 2,310.00 | 2,355.00 | -1.91% | 不適用 | 74.39 | 31.06 | 416.98B TWD / 30.09% | 2026-06-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +4.71% | +1.52% | 133.50 | 144.50 | -7.61% | 不適用 | 4.00 | 33.54 | 22.94B TWD / 17.78% | 2026-06-01 |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 981.61 | 981.61 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | +20.26% | +26.98% | 1,980.10 | 1,980.10 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -8.47% | +19.57% | 382.07 | 446.77 | -14.48% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Is Up 8% Today: Is It Outperforming Other Chip Stocks Like AMD and NVIDIA? - 24/7 Wall St.](https://news.google.com/rss/articles/CBMivgFBVV95cUxOMmZraGthM1NZSHdVbm1nSlVJYmlJdTJvemEtakZ1MjFwbzJoNmhMa3lBTVFBMlpnMHhtekwxQUh0R1BzMGZOTXcyc2l1NnhnbGZKMDJTc3lIMkNfRHBRYlVOZkxXaVVKaV9Xalg4S1p2bHBmZEszQWF5QVFJV0loLUJqeDgtU1QtWmc1aWhxMnNRUHR2X1dmTVF2dFk5UG5ZdkhELWV0U0JxU280SVA0ZTl5TGtGcnEwZFljLVBR?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 12 Jun 2026 17:36:17 GMT
- [總統見證動土 屏東半導體專區啟動 - 中央社 CNA](https://news.google.com/rss/articles/CBMiU0FVX3lxTFB1NDZoc2N1V09sSkxjUEtFZVFxNE9ZcXp1czRLc0FzTkNZUmdjMktGMHBpTnhQX2hLNWFoRU5jMVFzdHNTLWN4T0Vrd3Z4RE1WVWV3?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 12 Jun 2026 08:59:36 GMT
- [南華大學推動半導體學程赴美深化合作 攜手美國名校共育國際人才 - 中央社 CNA](https://news.google.com/rss/articles/CBMiVkFVX3lxTE5BTTZxX1R1cjhVb3dldklkVk9KNkJtckY0U2d5YTRYVHJpb2lRNV9HaVdoTkxtbkpVTzRnUmd1NTcxX0VwZDNYVk1wZjJtWUJhRHZmQWpB?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 12 Jun 2026 10:14:22 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：永豐金-豐原 對 昇貿(3305)個股 單一券商歷史明細 - justdata.moneydj.com；華南永昌-古亭 對 宏捷科(8086)個股 單一券商歷史明細 - justdata.moneydj.com；富邦-羅東 對 坤悅(5206)個股 單一券商歷史明細 - justdata.moneydj.com

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [永豐金-豐原 對 昇貿(3305)個股 單一券商歷史明細 - justdata.moneydj.com](https://news.google.com/rss/articles/CBMikgFBVV95cUxQanB0bHpNcVRNUjIxOTl1RENOUVNJTERXYk54NEJyMzNFVVNBWWl6blNELV9VZ25zQzMxU1REYk9uRE1uand5N2NUZnB5QmdnZTNMbE13MmFGN3hrdEM5cU5Tb1VCdDY0S0NDWFlSbFRKcm1uMTBCdDAySms5eVM2R2wtaE9kT1lvbENiRFZvbEZ2QQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 13 Jun 2026 12:47:43 GMT
- [華南永昌-古亭 對 宏捷科(8086)個股 單一券商歷史明細 - justdata.moneydj.com](https://news.google.com/rss/articles/CBMiggFBVV95cUxON1VXWG43YzNpY0pNajFUWGdVNGRaWTdmbDlKcW54NldUeWJScWVPWlRBZFZUQ1FpajREYlk0Y0M2V044M2hmWG9mZmEwQU1ZV3RZUllFUXFmUDJfNEZpNmhBVmJUMEdjSm5PS1p1NmduMmhuaEtrRGptcGF0YnRBNDBR?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 13 Jun 2026 08:51:59 GMT
- [富邦-羅東 對 坤悅(5206)個股 單一券商歷史明細 - justdata.moneydj.com](https://news.google.com/rss/articles/CBMihgFBVV95cUxQUnBWdUVqbUdLdGRmSlY0dnAtdlpsNGpXbkk5c0poTmFlTEgyMTVRb0JDbW9fSERzdU1WR19YZlplV191cy1SWHp2TXRTTk9LQThhSUk1bjVnWE1RRkFyOHI0b082bG8ySUVJRE5YVG1iYWtqelU2Tm5yb21HdTdDSlNpVHZZZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 13 Jun 2026 11:23:59 GMT

## 新興題材：SpaceX

摘要：新興題材：SpaceX 相關新聞集中在：Mag 7? MANGOS? SpaceX forces name rethink on Wall Street's tech-stock moniker - Reuters；Space stocks slump as blistering rally cools after SpaceX market debut - Reuters；Stocks rise as SpaceX makes market debut; oil slides on Gulf peace hopes - Reuters

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [Mag 7? MANGOS? SpaceX forces name rethink on Wall Street's tech-stock moniker - Reuters](https://news.google.com/rss/articles/CBMixgFBVV95cUxOVFh2RmJuX1poQlE4QVhNMG1kYjNaeUVhQmx3T2lEU002bTluMC1kbmhIUWR0eG5EYnRycEVvc2NWUGM5WFNDY3BwM3hhZzdzc2pzQW1pMHlsaHpkYVBteHZKSDAxajF5UVNXV0ZIdlpLcWFjSlM2ZFg3YlFscDRseHpMdURVOEJicWRtdVdGUXEtYVR0dklLbzN4bjV5XzBfeHl5VEVmaWN1OXFMUzVNQVdlRWlqNGNZUXRlS1dGQllFSTlrRUE?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 13 Jun 2026 10:23:46 GMT
- [Space stocks slump as blistering rally cools after SpaceX market debut - Reuters](https://news.google.com/rss/articles/CBMiwAFBVV95cUxQZ3V5alJuSTF4eVE5Y25rS0JDZGRVQmZubUQyclBTU3A5N3NBOUFoRWMxdXd2RWp4NXEtMGp3aHNnZy1kQlRzaHBMaWZFSjdSMHFqdWpaaUlXalVkOG1uZHV5WElCTFZyZ2FIQllrdlpHOWxxOG5oVTlQaWpuMWxwdC1NTDFZRU82UDdINlNsaWdmaHRzZzU1eVgyaFB0ZzhhSVRjc2d6QjEwTk8zVVo3bkNibG5ONHU3QUptb2hCMTM?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 12 Jun 2026 19:01:09 GMT
- [Stocks rise as SpaceX makes market debut; oil slides on Gulf peace hopes - Reuters](https://news.google.com/rss/articles/CBMigwFBVV95cUxPV1pjRmJPbG9FY2Q3ekpEY1dDQTI3aWU0MzdqR0tMbDdKNjdkWHNDRGk3TEdFbDVzeHBZODUyS20yNnpuWHR0N2xPRHFPWHN4QlA3QzNUM1BONlRJakJfdGpTOWYybHU2ZTBfM29JamNOc096OWgzd0FRa01GN1BWbzNraw?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 12 Jun 2026 00:40:00 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：產業評析最新專欄分析 - MoneyDJ；富邦金 115年5月營收304.08億 - MoneyDJ；台新新光金 115年4月營收172.21億、年增673.62% - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [產業評析最新專欄分析 - MoneyDJ](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPME5JN0JfdHVjRkExcExuOFZKMzJwNnV0V1p2U1dpcEJHSFZ1dTNSLTJtZFNRQU91Z0Z1Q0VsM2FKSWd0akJmZEZSRTBHSkUxTVNqN2pVaWJndmhXdTBKc1hoVnNqU29RTjJVV2lRZ0pIUDNBTTBCX05JaUUwc0hoWTFTNHRVVi1D?oc=5) - Google News source discovery | MoneyDJ Fri, 12 Jun 2026 22:22:55 GMT
- [富邦金 115年5月營收304.08億 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPa0x3YWNDZUs4V2wwS1ZUV080WFlWTlFVRDNyc3RrZkVQcWV3MlRocUpSZURmY1pWcUV3SFUyVzV2M3RHWXp2a0R5N3EtOVZDZVM3dkJMdlJtcldUVmR1cFVqOVF2VDRqc3k0ejcyZFluYldfUTNsNjk2SEx2VVhoSmptdGUwSm9ZcEFEbkRpU2pwQQ?oc=5) - Google News source discovery | MoneyDJ Fri, 12 Jun 2026 10:11:00 GMT
- [台新新光金 115年4月營收172.21億、年增673.62% - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxOdG95NUllVFpyNVVaMlhNYk9OZFBicEx6M2dYc2owZldLdXEtc1A1YURYQWg1OHRCM1NuMmh1TnQ5ZFJlSXp1bjd3SjNRNzh6VGVsSmdMQ2JoRnhoNkNORjNDZ2dyb2RjYzhQT0ZlbS1VVWZvdVYwRGlLTUF4eGhjTkMyZVVfRDRHQlpRcm5JQUNuUQ?oc=5) - Google News source discovery | MoneyDJ Fri, 12 Jun 2026 10:21:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
