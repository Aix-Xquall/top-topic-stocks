# 每日股市熱門話題分析 - 2026-06-11

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜中性｜熱度 4｜市場確認 N/A｜同向 0/0
2. **利率與成長股估值**｜負向｜熱度 2｜市場確認 N/A｜同向 0/0
3. **半導體與晶片供應鏈**｜中性｜熱度 5｜市場確認 N/A｜同向 0/0
4. **散熱與液冷供應鏈**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
5. **AI 伺服器與資料中心**｜正向｜熱度 11｜市場確認 0.00｜同向 1/6

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.05（樣本 7）
- 5日相關係數：-0.08（樣本 7）
- 同向比例：1/7

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 0.00 | 1/6 | 4 | -3.98% | -3.40% |
| 新興題材：5月營收 | 0.00 | 0/1 | 1 | -4.65% | -7.01% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：AI伺服器 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-05-29 | 0.14 | -0.04 | +71.43% | 7 |
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

## 歷史回測摘要

- 回測日期：2026-06-11
- 近5日 3日相關：0.11
- 近5日 5日相關：-0.26
- 同向比例：+31.58%
- 權重狀態：已調整

- 方向準確度：+31.58%
- 信心排序準確度：0.11
- 診斷：弱正相關

調整原因：近 5 日方向與信心排序皆偏弱，降低方向詞與供應鏈推估權重，並加重背離扣分。；關鍵詞×公司後續樣本有效 4 筆，未達 30 筆，不調整樣本權重

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

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：SanDisk (SNDK) Is Doing Something Unprecedented In The Al Sector! SNDK STOCK PODCAST ANALYSIS BUY Jobe Bellingham (gRMiCAoJ7a) - Mshale；Micron, SanDisk, and SK hynix Investors Should Fear One Thing: Elon Musk - 24/7 Wall St.；Sandisk: Market Has Completely Misread The AI NAND Supercycle (NASDAQ:SNDK) - Seeking Alpha

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| SNDK SanDisk | 新聞直接提及 | 0.00 | +5.38% | -10.28% | 1,643.23 | 1,831.50 | -10.28% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 891.88 | 971.00 | -8.15% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +0.43% | +13.11% | 200.42 | 211.14 | -5.08% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- SNDK：新聞直接提及「SNDK、SanDisk」，共 4 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- MU：新聞直接提及「Micron、NAND」，共 3 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [SanDisk (SNDK) Is Doing Something Unprecedented In The Al Sector! SNDK STOCK PODCAST ANALYSIS BUY Jobe Bellingham (gRMiCAoJ7a) - Mshale](https://news.google.com/rss/articles/CBMiW0FVX3lxTE82c25ZNkhMbnBFcHlYZktjT2gzRlFzREd4ZFlubTJYeG4zZFJ6NU1OdGxaX3BRYWM0bFdDWk5tMlNVS3BvWXRLZW1jUVp3SUdNYXlKam5zNEhNVm8?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 10 Jun 2026 20:36:40 GMT
- [Micron, SanDisk, and SK hynix Investors Should Fear One Thing: Elon Musk - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiswFBVV95cUxOc2x6LVR3cUZJQWNBTHFVU1FiVjBsSmFpODZJMjdrSDVKTDZ3VkNZbVNKclBvNkxzUjZwWW9FWUI4VEZpOUdaeFhwZWdHaTBqbThFYnd1Wm8yZUxxeFFkY3I5TGd6cWplM1FXLWJsRkpHb3lsRkcxaW1LcXh4OGVqdVQ1Nk9kR0JZdk5MZ2VBU1NGT2ZoSUFQUEhrVEhXTGwtM1BhU2NfWHZVMUg5SHlGa2ZVQQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 10 Jun 2026 14:17:15 GMT
- [Sandisk: Market Has Completely Misread The AI NAND Supercycle (NASDAQ:SNDK) - Seeking Alpha](https://news.google.com/rss/articles/CBMiowFBVV95cUxPUmRWQVNzbEZHb2FwTW9uOFZuc19NbUU1YU1KMmphN2p6Z2VMdll4YmtRWEZJNUdBOWREdUwwWGE4NlJWa0NON1NGMUQxVjZPVHFOMVV5VGw2dFVUWjl0bHVFbWJkdDM0V3RqRndPalBxUUNQc29mbXhOb3Q1U0RGN3ZCczJsR0tJUVZRLUFpZ2tINXpYU2JXb1BIenJCYTlSbDhn?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 09 Jun 2026 17:43:30 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：美5月CPI憂喜參半！年增4.2%創逾三年新高、核心通膨低於預期 - news.cnyes.com；〈美股早盤〉通膨利多不敵中東風險 主要指數開低 - news.cnyes.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +1.18% | -21.58% | 397.36 | 506.69 | -21.58% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [美5月CPI憂喜參半！年增4.2%創逾三年新高、核心通膨低於預期 - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTFA3LU9mWmJRZ2pRTXQ5dzcxN1F6LS1iYXNzZHJDOXc5U0dPUzFTdUNlOU4wZmtOVDZWS1l4V0wyYTB5YU96Y3diOUF4U2JQNU0?oc=5) - Google News source discovery | 鉅亨網 Wed, 10 Jun 2026 12:35:38 GMT
- [〈美股早盤〉通膨利多不敵中東風險 主要指數開低 - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTE9qQlpZd1o5NG5uZjVKai1sTGtwYk9KOWVtTGE0R3pDT1dHZGh5THdxN0FycDlBT2NKWEoyeV9kWFg1aEQ3MFg1a25rRTVYOG8?oc=5) - Google News source discovery | 鉅亨網 Wed, 10 Jun 2026 13:39:00 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Forget Intel Corporation: As June Volatility Rocks Chip Stocks, This Tech Monopoly Is The Smart Money Pivot - 24/7 Wall St.；臺大開辦半導體系列學分班 攜手頂尖師資進駐雲林 - 中央社 CNA；晶片 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 107.04 | 114.68 | -6.66% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -4.65% | -7.01% | 2,255.00 | 2,355.00 | -4.25% | 不適用 | 74.39 | 30.32 | 416.98B TWD / 30.09% | 2026-06-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | -9.89% | -9.20% | 118.50 | 144.50 | -17.99% | 不適用 | 4.00 | 29.77 | 22.94B TWD / 17.78% | 2026-06-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +0.43% | +13.11% | 200.42 | 211.14 | -5.08% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 452.40 | 516.10 | -12.34% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 891.88 | 971.00 | -8.15% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | +5.38% | -10.28% | 1,643.23 | 1,831.50 | -10.28% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -10.86% | +16.45% | 372.10 | 446.77 | -16.71% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 1 篇新聞出現相關標籤。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 1 篇新聞出現相關標籤。

### 主要來源

- [Forget Intel Corporation: As June Volatility Rocks Chip Stocks, This Tech Monopoly Is The Smart Money Pivot - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi4wFBVV95cUxPckRsQXZKVEJRWHd2RDJqT2FCTG5xWVBDb2FIOWZManlidmZrRUZXbjdRbm1jQ1hwQlNqOV9FTTd5UDZSREx5Vy1TWEw1cUhWSVNzeFZXTEFGam9wVUdOd3QwRDBwZFdtZlFiU3kzSTBXaC1EOTl0b3ZSeDJ2eWxHOUljMmxoZGllNjEwZTZVdm9lM0VTWDg5Qm83S3BNeGloaDNkYXlzVjBzVFhQLVRVdkRSY0I2S0tXS2w5V180alZOQ2lBcjhYcVNJcmJlUGk0WDJ6X2dEdjd5RUFmYUd0WkdwWQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 10 Jun 2026 15:53:57 GMT
- [臺大開辦半導體系列學分班 攜手頂尖師資進駐雲林 - 中央社 CNA](https://news.google.com/rss/articles/CBMiVkFVX3lxTE9kdFdwVzg3UGNiaHcxV1BOMU4yeVhzQ1pjal94ZndQU0NYTnI1Rzh6WkN2U00ya2xOQTk3VEdoT0QtZnpJUEFlM1R1VHVHRV9uWGlrcnFn?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 10 Jun 2026 02:07:27 GMT
- [晶片 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiakFVX3lxTE5FSXY3YUd6UlJlaFh0VC1oMnpVWENEd3VmaGFSZEtHbmJWT19BcWhDaUw5eWFoVWxjNmtFVWpocDExVW9fY3JsZVYzUGRLeHU2RmdMN3dEUjRHd1JuMTQwU3B0NUNIdV82T1E?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 10 Jun 2026 22:37:52 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：奇鋐、雙鴻 押價內外15% - 經濟日報；法人喊目標價3690元！「這散熱大廠」前5月營收暴增90％ 夯到訂單一路排到2029年 - FTNN 新聞網

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | -9.23% | -17.34% | 2,360.00 | 2,835.00 | -16.75% | 不適用 | 61.06 | 38.78 | 15.87B TWD / 60.64% | 2026-06-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐、散熱」，共 2 篇新聞命中。 同時符合主題標籤：thermal。

### 主要來源

- [奇鋐、雙鴻 押價內外15% - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBjZVg1MERzYnZaUXBwQmR0Ri10NW91dzdNdDdDemYtdkV2cF9RSGk0TlVzZkhHSFFqUGZxVEEybjZrZXdKQnJWZzUyTUh3dGFWeTlqUzlXb3NLZ9IBX0FVX3lxTE1tdy1yYWRXX3RER0pfMFNuNE5jeWJsVlN1MGlMQTM1ZmtRRURiYUc4NlJDU1dhQTJGcGFiTldCRXVpMXR6Tlg3UFpOWjYySEk2RUVGblJ2WlNXYTBqRVgw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 09 Jun 2026 09:00:00 GMT
- [法人喊目標價3690元！「這散熱大廠」前5月營收暴增90％ 夯到訂單一路排到2029年 - FTNN 新聞網](https://news.google.com/rss/articles/CBMiS0FVX3lxTE1yVmF5ZXFfWnA2RHdTQW9HeU11NExOWkRqbXc1akdZN05QREd4UVE0aWFhbHh3am1sdkFURmdObW9KemYwUWpPb0JwOA?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 09 Jun 2026 03:30:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：營收翻倍成長後，美超微如何維持 AI 市場領先地位？ - TechNews 科技新報；轉向金融市場募資，是否預示 AI 伺服器進入軍備競賽？ - TechNews 科技新報；AI 人工智慧 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AMD 超微 | 新聞直接提及 | +0.63 | N/A | N/A | 452.40 | 516.10 | -12.34% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 產業/供應鏈推估 | +0.08 | N/A | N/A | 107.04 | 114.68 | -6.66% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.04 | +0.43% | +13.11% | 200.42 | 211.14 | -5.08% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.03 | -4.65% | -7.01% | 2,255.00 | 2,355.00 | -4.25% | 背離 | 74.39 | 30.32 | 416.98B TWD / 30.09% | 2026-06-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | +1.18% | -21.58% | 397.36 | 506.69 | -21.58% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -10.86% | +16.45% | 372.10 | 446.77 | -16.71% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.02 | -6.59% | -12.78% | 539.00 | 611.00 | -11.78% | 背離 | 10.86 | 50.05 | 63.03B TWD / 28.57% | 2026-06-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.02 | -3.37% | -8.58% | 4,155.00 | 4,475.00 | -7.15% | 背離 | 62.91 | 66.22 | 47.43B TWD / 4.99% | 2026-06-01 |

關聯理由（前 3）：
- AMD：新聞直接提及「超微」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。 方向判斷命中詞：成長。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：成長。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：成長。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [營收翻倍成長後，美超微如何維持 AI 市場領先地位？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiYEFVX3lxTFBRMFVIQXk4YlJDZU1UTDRKRkh1WHVoUl9xWkF0a3lxZW9mb3NYbU9KNlRnNjNqR0p3cjVtcXllTVM3bGtpNEtCTTR3VzdTSUlOTU1kcUlvVlNQS1ZYZnZWMw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 10 Jun 2026 20:05:48 GMT
- [轉向金融市場募資，是否預示 AI 伺服器進入軍備競賽？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiYEFVX3lxTE1sLWJaNWZTeTMzV0pCQWZncVlSaG1EUzlyN05Rem1WTko2VDJFdDNxdnY1ZXpyMWFQdVR5aUgwVlBCMGJqdXV2LVJQNHI4UThDTVhISDZDOEZqZHlMRzhfVg?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 10 Jun 2026 20:03:49 GMT
- [AI 人工智慧 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiVEFVX3lxTE4zam9EYUpCX216QXItaXJlcVltZU1zTnFQaXVRZmNsMWZ2RDAydUd3NmxEZEcxZ1duQ0FBUENiS1lWazl3QW55cEtTNVVVdGc2MXRsVQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 10 Jun 2026 19:47:03 GMT

## 新興題材：5月營收

摘要：新興題材：5月營收 相關新聞集中在：5月營收創高照樣被砍！外資倒貨「這2檔晶圓代工」8.9萬張 連賣台積電6天捲走1862億元 - Yahoo股市；台積電明股價噴？5月營收史上最強 專家看好漲45元 - Yahoo股市

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | +0.29 | -4.65% | -7.01% | 2,255.00 | 2,355.00 | -4.25% | 背離 | 74.39 | 30.32 | 416.98B TWD / 30.09% | 2026-06-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 2 篇新聞命中。 方向判斷命中詞：創高。

### 主要來源

- [5月營收創高照樣被砍！外資倒貨「這2檔晶圓代工」8.9萬張 連賣台積電6天捲走1862億元 - Yahoo股市](https://news.google.com/rss/articles/CBMi4gJBVV95cUxQWWV3UnlfY2w3a2g0ZXZZcTVidzZfcnBDMkF3dFpSWUN5ZUVULW9ES25qbm43aDF6S1Z4TDBINFo4dFA5bm9INTE4VTRlcWxxUmFDWUs4MmJ0bWtKZVhabmtEd1NMS3gwdWhCb0lSZllWUXhWdlRSbUZ3RDdkbFluTWNYRFl5VHFUMzRUdE1zVXVWRE5neDJia3MydzJOdUNfNjBfdmQ4WWxvRG8wMGNGek90N3Z2NE1KRW9UdXhPY0F4d1llSWRfN3Vwb2xxOWNGWlNsTlhaa0EydnFaemNhTmFUVDBOdlJRS3EyZm1wSVNSMmVmZ0hOZ2M5LVZEWXlLRWxrTFJveGpBSkJ3UUtBZ3JpUklXRkE4MXd1Q1psLXhHM0dONXFKQXVuaENEcEk4bGY2eTMzQnNIcVZPdG5XVEVRbkdDUnZoMTZDbV9UY2QzUFRaUnJGOGY1bTBEUC1EOWc?oc=5) - Google News source discovery | Yahoo 奇摩股市 Wed, 10 Jun 2026 12:30:00 GMT
- [台積電明股價噴？5月營收史上最強 專家看好漲45元 - Yahoo股市](https://news.google.com/rss/articles/CBMi3AJBVV95cUxOR2Z3aHVfSWxwOGNxeF96VEtQV1A1djhldXVUNGgyQXRxb0h4cnViWHpoSkNrQUs2czZ0clpSUUFRdnlTd2FyWXhXSHdhR1BwR2ozalJjMmlPb3ZHbWR3cW5PN2ZxWUZKNXl0cl8wdlJ0UG1aVXZ2eUFjaWNYUkZNaTFmdUJDTWhaVWNPQXpDMEdIVk5lUDJNRGxHLTJwakZKYzhITG5FUWhjYzJRcUszZjlaVlJjeXNULTUtdjU4VGdiR3FMS0l5ckZ4VHJwU3dqbWhuVFQzaGVERWF6U1RFX2dKLWllaXZrWlJkR2RIRHBSaW96d1lOdXZQS0ZoTzd1WjhjRmtVdVJXU2p2T2ZXajNxU3BDTTNKV0d6bTlHWlpfSEVJSXpIT0lKUEd3NTc5QTk4OWh3Xy14cUlPX1VvVkJJTGl0VHB5czdmMUdiSnJEZFM3MlA5cXdnVDE?oc=5) - Google News source discovery | Yahoo 奇摩股市 Wed, 10 Jun 2026 07:47:01 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：大華銀：台股H2仍看樂觀，配置高息ETF應對震盪- 新聞 - MoneyDJ理財網；《台股盤後》開低走低、重摔1478點，失守月線- 新聞 - MoneyDJ理財網；20260610台股融資維持率 - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [大華銀：台股H2仍看樂觀，配置高息ETF應對震盪- 新聞 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikgFBVV95cUxOTklMTVhfOHZtMWVaeVh5TEt4T3RIQXJkZXdPNVkyT2RPMlJESFJXMzdBNmYyOXNudmpGTU1hWGFYYi1Nb2dESjZKQUJ6ZHJva2ZnQ1REOVpRUEkyb0s0VTM3dF9YREx3SDR6NDhybmZiUHFFeDFoWXJvU2dTRUFFZnhhTkltZ1J0VFRuQ0hCc2Z1UQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 10 Jun 2026 21:35:00 GMT
- [《台股盤後》開低走低、重摔1478點，失守月線- 新聞 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikgFBVV95cUxOY1ZfR09GZXlLODFqaXAyaHNtYUtrcERLZ09BYmJCUVRqN1hBZXh5V3hHQjZQNkF5a2gyRnNueFljZThvWG4yUkdoNG1hX0IyY0VaMENPLUZIbGZYaWxvSi1JeFo2MmFmcjhqeUlSc0RQSXhTaWJObmVEV1I0anZnZGNqRkVLYUJ3bUhmZVE0aV9BZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 10 Jun 2026 08:06:00 GMT
- [20260610台股融資維持率 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMisgFBVV95cUxPZTJvd1ctakRMaktSOTN6RFJ0dHNJa1NNM2lMVlMyUmNsV3hqbWROblctS1RJWTF6Y2hPdVBtY2Q1cFdBUy1VTVdoSGpmeGN5RjBFeVl0XzNvVThaXzI4LVRoVlV2NGNjYTBQR0lDbTVFeXlucDRkX0hEMXRHNTdiUG1CUnM5ZlRxbTlsSVFoMVh3c1lBTDlNNDlXZDJCS2JRZ3d0NzJDNmpiTGRKTTQxY3pn0gG3AUFVX3lxTE9sSWVOczhsUlV0dFBKNTE2MW9pVzNNRGR0b2dFZThsMGpKQ0paZDFUMVh3cjVZX3d4V1FSUXJCZS1YWVYyUExrSFlVdE5tc2FHWDlsd1pSTlRCRUtRNG9pbGRINGRRN0FMS2pSV2tiQmlkc1Z3ZXNNSVRnZ2pyTGFOR3hMNkNUNlJnNjcyNHBzb2ZYMVBmSDdMaUt3YWlZRFdxNXN4UDRUNHFrSUVZWUEtdW80dTBqSQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 10 Jun 2026 15:48:26 GMT

## 新興題材：AI伺服器

摘要：新興題材：AI伺服器 相關新聞集中在：台股快閃季線最佳買點 AI伺服器廠提前進入出貨旺季 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股快閃季線最佳買點 AI伺服器廠提前進入出貨旺季 - 經濟日報](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5FdUxnYmxlQjRFalo2b2JmRmNITktuNmdaZlBzTjZXU1c1Z01kMWxCMGZnMGE4Vnh0cENIbEhtSEdoVllvQUpwTzRHRWVDMk4yZ09ZNFIzUm5ydGvSAWBBVV95cUxPeHFlVVdXWU8xMUpUdDhCaG9oY203ZUM4ZFdHUXVnT040WHUyQldQZWd2a043Vmhhalp5OFNieE5NYmhSQzJnLWM4NmlUc1hWZUxPUk90ZEQtT0pPclltTTM?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 10 Jun 2026 16:29:23 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
