# 每日股市熱門話題分析 - 2026-10-24

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **半導體與晶片供應鏈**｜負向｜熱度 11｜市場確認 85.74｜同向 7/8
2. **AI 伺服器與資料中心**｜負向｜熱度 18｜市場確認 65.10｜同向 6/8
3. **新興題材：BigGo**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
4. **散熱與液冷供應鏈**｜負向｜熱度 1｜市場確認 85.81｜同向 1/1
5. **記憶體與 HBM 供應鏈**｜正向｜熱度 9｜市場確認 0.00｜同向 0/2

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.09（樣本 20）
- 5日相關係數：-0.31（樣本 13）
- 同向比例：14/20

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 半導體與晶片供應鏈 | 85.74 | 7/8 | 0 | +8.16% | +5.45% |
| AI 伺服器與資料中心 | 65.10 | 6/8 | 1 | +4.20% | +1.93% |
| 新興題材：BigGo | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | 85.81 | 1/1 | 0 | +5.27% | -1.94% |
| 記憶體與 HBM 供應鏈 | 0.00 | 0/2 | 2 | -8.83% | -9.60% |
| 新興題材：TradingKey | 0.00 | 0/1 | 1 | -9.62% | N/A |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 相關性偏弱；應提高同向價格確認權重，降低泛 AI、泛半導體等寬標籤推估權重。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-10-11 | 0.66 | -0.74 | +40.00% | 5 |
| 2026-10-12 | -0.08 | -0.07 | +41.67% | 12 |
| 2026-10-13 | -0.05 | -0.03 | +46.67% | 15 |
| 2026-10-14 | 0.08 | -0.29 | +57.14% | 14 |
| 2026-10-15 | -0.08 | 0.08 | +33.33% | 12 |
| 2026-10-16 | -0.13 | -0.25 | +64.00% | 25 |
| 2026-10-17 | -0.10 | 0.49 | +26.32% | 19 |
| 2026-10-18 | -0.12 | 0.33 | +21.74% | 23 |
| 2026-10-19 | 0.44 | 0.36 | +50.00% | 12 |
| 2026-10-20 | 0.09 | -0.81 | +69.23% | 13 |
| 2026-10-21 | -0.25 | 0.23 | +5.56% | 18 |
| 2026-10-22 | 0.02 | -0.21 | +38.89% | 18 |
| 2026-10-23 | 0.35 | 0.29 | +78.95% | 19 |
| 2026-10-24 | 0.09 | -0.31 | +70.00% | 20 |

## 歷史回測摘要

- 回測日期：2026-10-24
- 近5日 3日相關：0.00
- 近5日 5日相關：-0.32
- 同向比例：+66.67%
- 權重狀態：未調整

- 方向準確度：+66.67%
- 信心排序準確度：0.00
- 診斷：低相關

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

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Chip Stocks Fall as Supply Warning Deepens AI Selloff: Marvell and AMD Sink 8%, Intel Drops 7% - 24/7 Wall St.；Intel (INTC) Joins Musk's Terafab AI Chip Venture In High Profile Alliance - Simply Wall Street；The Foundry Disconnect: Intel Nails the Transistor, But TSMC Holds the Keys to Yield and Scale. - 24/7 Wall St.

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.57 | -24.17% | N/A | 86.96 | 114.68 | -24.17% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | -0.50 | -1.45% | -2.25% | 2,385.00 | 2,480.00 | -3.83% | 同向 | 86.28 | 27.65 | 511.86B TWD / 54.65% | 2026-10-01 |
| AMD 超微 | 新聞直接提及 | -0.35 | +0.13% | N/A | 516.79 | 516.79 | 0.00% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| 2303 聯電 | 產業/供應鏈推估 | -0.05 | -4.56% | -5.99% | 125.50 | 164.50 | -23.71% | 同向 | 6.68 | 18.87 | 25.35B TWD / 27.22% | 2026-10-01 |
| NVDA 輝達 | 產業/供應鏈推估 | -0.04 | -4.45% | +5.43% | 210.96 | 228.38 | -7.63% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | -0.04 | -9.62% | N/A | 877.55 | 971.00 | -9.62% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | -0.04 | -8.04% | -9.60% | 1,260.93 | 2,335.00 | -46.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -13.14% | -14.84% | 321.68 | 446.77 | -28.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel、INTC」，共 3 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「TSMC」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip, foundry。 方向判斷命中詞：fall。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Chip Stocks Fall as Supply Warning Deepens AI Selloff: Marvell and AMD Sink 8%, Intel Drops 7% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMizwFBVV95cUxPSHYtVnBnaXBZc3V3cXUySWxseXJNcVUxV0Vhb2R5SlFkMVF4aTRyemE3VDladG5fVVB4blJNb0YwR3BwTG85TUt4MG0xT2R4Q1dOMUFXcUNtSkFVejktNjVWVXlWRThLUVBoX1hHZGNQWnZPdjZCaXFqYzRFWm1IWXdoQzl0WjlpZ0hxclhpUWFZa01ERVFCMHRtTFdVUEtDRURXYW1lWnJxSlRVYmpiaEREaGphdmo3Rld6OUg4R1BaOUhXNGtadEZvOENFWlE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 22 Oct 2026 15:45:00 GMT
- [Intel (INTC) Joins Musk's Terafab AI Chip Venture In High Profile Alliance - Simply Wall Street](https://news.google.com/rss/articles/CBMiygFBVV95cUxNYlBnVmlIdGZHNTQ2VFdwZk5lTlcwRlhVVjB2WFpUbjFMMGFaWW1CZ0tBcGJlbHpKUW9iMVhHRC14LWVCWC1pZDl2UHFVendRR0tRY01IRDZZdFhqNEhVeTI3VHFhM09pTW52eDVLdVVGT1lqaXdMM2EwUVFmZ0NKUWlFaEs0cDFsR0JWMGE0VVU0d04xeVIyN2FoX1ZEOUFzQUVVZWx0Q1lUYjNGWkVWUV9JM2k4ZlNuQTczNDhnNUM0T3BHWFF6N1hR0gHPAUFVX3lxTE9SejFUc19GVEN6VzFiX0Z6MEcxdGVxQTVvMUxMUXdNQnowZlU4RGhZc1ppbW5UVUhSQlNmQTZpSFlhY2hlcW1MN2pjdlJvYi03ajFIalk1a3FUZG9QZTJoeDVVRlFqWHZ5Qmc3emxYWDdITUlYejdPR1F2ZlVZYzR3OF9yRVhuYjZ5U1RRUGNlMWNHZWdPZzJYWFZMYW82Szhodmt6QXlaZzhQZU5oQ1VMYWRPT2xmbndWRG15Q2F4cjkzclRDLXBTSDFhazNnMA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 22 Oct 2026 06:17:57 GMT
- [The Foundry Disconnect: Intel Nails the Transistor, But TSMC Holds the Keys to Yield and Scale. - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi0gFBVV95cUxPN2xnaHFFeDhMQjM5N0dRbjI4cnJERnpKMlhNSkRlMFVXVkloQzVCOTBnRHdlOVhpdm1qc3pzU0M2U0IyRHJRWU1La1JoSDM3R29LaFBEM1ROaWNyOFVTb3RreThfODNSaXZEZlBpeUZQYVR1M0xuLXZ4Rng1SERmV1NsZU1Mbms4V0RyMzY2NXlqbmZaZXZMa2dEWFFTOTNVRlVYRGc3cUR3Sy0ycloxWTJwUF9OWUFuOWxRMHRWS2JTaGtfeUNlQ3IyT2ljUVhCcHc?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 23 Oct 2026 11:15:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Chip Stocks Fall as Supply Warning Deepens AI Selloff: Marvell and AMD Sink 8%, Intel Drops 7% - 24/7 Wall St.；Intel (INTC) Joins Musk's Terafab AI Chip Venture In High Profile Alliance - Simply Wall Street；AI資料中心支出續增，現金流壓力會先壓到誰？-柏宇 KD 獲利模式 - CMoney投資網誌

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.57 | -24.17% | N/A | 86.96 | 114.68 | -24.17% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.40 | +0.13% | N/A | 516.79 | 516.79 | 0.00% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | -0.06 | -4.45% | +5.43% | 210.96 | 228.38 | -7.63% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.06 | -1.45% | -2.25% | 2,385.00 | 2,480.00 | -3.83% | 同向 | 86.28 | 27.65 | 511.86B TWD / 54.65% | 2026-10-01 |
| MSFT 微軟 | 產業/供應鏈推估 | -0.02 | +16.50% | +6.61% | 524.51 | 524.51 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -13.14% | -14.84% | 321.68 | 446.77 | -28.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.04 | -2.39% | -2.82% | 654.00 | 703.00 | -6.97% | 同向 | 13.92 | 47.32 | 88.13B TWD / 45.52% | 2026-10-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.04 | -4.64% | -3.72% | 4,010.00 | 4,920.00 | -18.50% | 同向 | 60.69 | 66.23 | 55.40B TWD / 1.97% | 2026-10-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel、INTC」，共 2 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 5 篇新聞出現相關標籤。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Chip Stocks Fall as Supply Warning Deepens AI Selloff: Marvell and AMD Sink 8%, Intel Drops 7% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMizwFBVV95cUxPSHYtVnBnaXBZc3V3cXUySWxseXJNcVUxV0Vhb2R5SlFkMVF4aTRyemE3VDladG5fVVB4blJNb0YwR3BwTG85TUt4MG0xT2R4Q1dOMUFXcUNtSkFVejktNjVWVXlWRThLUVBoX1hHZGNQWnZPdjZCaXFqYzRFWm1IWXdoQzl0WjlpZ0hxclhpUWFZa01ERVFCMHRtTFdVUEtDRURXYW1lWnJxSlRVYmpiaEREaGphdmo3Rld6OUg4R1BaOUhXNGtadEZvOENFWlE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 22 Oct 2026 15:45:00 GMT
- [Intel (INTC) Joins Musk's Terafab AI Chip Venture In High Profile Alliance - Simply Wall Street](https://news.google.com/rss/articles/CBMiygFBVV95cUxNYlBnVmlIdGZHNTQ2VFdwZk5lTlcwRlhVVjB2WFpUbjFMMGFaWW1CZ0tBcGJlbHpKUW9iMVhHRC14LWVCWC1pZDl2UHFVendRR0tRY01IRDZZdFhqNEhVeTI3VHFhM09pTW52eDVLdVVGT1lqaXdMM2EwUVFmZ0NKUWlFaEs0cDFsR0JWMGE0VVU0d04xeVIyN2FoX1ZEOUFzQUVVZWx0Q1lUYjNGWkVWUV9JM2k4ZlNuQTczNDhnNUM0T3BHWFF6N1hR0gHPAUFVX3lxTE9SejFUc19GVEN6VzFiX0Z6MEcxdGVxQTVvMUxMUXdNQnowZlU4RGhZc1ppbW5UVUhSQlNmQTZpSFlhY2hlcW1MN2pjdlJvYi03ajFIalk1a3FUZG9QZTJoeDVVRlFqWHZ5Qmc3emxYWDdITUlYejdPR1F2ZlVZYzR3OF9yRVhuYjZ5U1RRUGNlMWNHZWdPZzJYWFZMYW82Szhodmt6QXlaZzhQZU5oQ1VMYWRPT2xmbndWRG15Q2F4cjkzclRDLXBTSDFhazNnMA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 22 Oct 2026 06:17:57 GMT
- [AI資料中心支出續增，現金流壓力會先壓到誰？-柏宇 KD 獲利模式 - CMoney投資網誌](https://news.google.com/rss/articles/CBMigAFBVV95cUxQWEJwQXdEbDF4c1J3VFdwdlN6SDdudFVjV0VVREYwV3QxWlZ0eTY5VmNNbDBMZEZsc1Z4UkhNUGk2Y2t5SlR2ZHA4TGpJdDc5X2ZrbTdyNHlBQ0FPRkJjV3Vqbzc4ZW1kdlJpVnM1RXJ4ZG1IOS1Ydk1rZzhtMkR1QQ?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 23 Oct 2026 05:27:12 GMT

## 新興題材：BigGo

摘要：新興題材：BigGo 相關新聞集中在：Micron and Sandisk Both Tripled in 2026, but Wall Street Sees More Room in Micron - BigGo Finance；SK Hynix vs. Micron: Wall Street Sees Roughly Equal Upside in the Memory Duopoly - BigGo Finance

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | -9.62% | N/A | 877.55 | 971.00 | -9.62% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | -8.04% | -9.60% | 1,260.93 | 2,335.00 | -46.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。

### 主要來源

- [Micron and Sandisk Both Tripled in 2026, but Wall Street Sees More Room in Micron - BigGo Finance](https://news.google.com/rss/articles/CBMidkFVX3lxTE9kUnYwLW8yd2xYXy1qdlFfWmUySVpLSGFZR3Rhb3hTZllNVGxwMzRaWjBQQWZma0ttTEc3NE9yYzVLX3E0bzE2dWk4a00tRVR1WHVUMXQxYnZSdTgtOThmb3hlYW5nNmFjNXlWbFpYTGtyTmpHbmc?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 23 Oct 2026 18:15:00 GMT
- [SK Hynix vs. Micron: Wall Street Sees Roughly Equal Upside in the Memory Duopoly - BigGo Finance](https://news.google.com/rss/articles/CBMidkFVX3lxTE5FY05ScDhlMnBYb1cxM29mbjNpUC1IQU5pc3VsMFNQT2dOS0hhblB6ZzdrY1FoMFlyeDVVVHpGbTAyRGRGQUhlcjV5ZnZlZUt4WjFEWEUyMG9KTHJtVlJtWnpUUF90MXlPTFpRN3FLdEw1a2hiaWc?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 23 Oct 2026 18:15:00 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | -0.43 | -5.27% | +1.94% | 3,145.00 | 3,435.00 | -8.44% | 同向 | 75.13 | 41.92 | 21.02B TWD / 44.92% | 2026-10-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 1 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：跌停。

### 主要來源

- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 22 Oct 2026 20:51:30 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Better Memory Stock: Micron vs. Sandisk - Yahoo Finance；Micron and Sandisk Both Tripled in 2026, but Wall Street Sees More Room in Micron - BigGo Finance；SK Hynix Jumps 4% After Scrapping Solidigm’s U.S. IPO; Micron and SanDisk Edge Higher - 24/7 Wall St.

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.28 | -9.62% | N/A | 877.55 | 971.00 | -9.62% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.28 | -8.04% | -9.60% | 1,260.93 | 2,335.00 | -46.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -4.45% | +5.43% | 210.96 | 228.38 | -7.63% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、memory」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally, surges。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 4 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：rally, surges。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Better Memory Stock: Micron vs. Sandisk - Yahoo Finance](https://news.google.com/rss/articles/CBMimgFBVV95cUxNSjgxYWpWQUVNSTJOb1dRdEpxemFxXzVrcXozZXVjWFRDZWZvSC1KeWdpX2xJVFFfZURseXpBR1M2aUsyLThuVmw2R0pFVGlwaG5QeFNEVmg3ZlI2NXR6VV9Denl5N1BTYVZLRTdON2d5RlFFUzlGY1FQb3RldTNFbk92TXA2aXQ4WkdFTEc0S1RSMVlLM3ZLNURR?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 23 Oct 2026 09:04:00 GMT
- [Micron and Sandisk Both Tripled in 2026, but Wall Street Sees More Room in Micron - BigGo Finance](https://news.google.com/rss/articles/CBMidkFVX3lxTE9kUnYwLW8yd2xYXy1qdlFfWmUySVpLSGFZR3Rhb3hTZllNVGxwMzRaWjBQQWZma0ttTEc3NE9yYzVLX3E0bzE2dWk4a00tRVR1WHVUMXQxYnZSdTgtOThmb3hlYW5nNmFjNXlWbFpYTGtyTmpHbmc?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 23 Oct 2026 18:15:00 GMT
- [SK Hynix Jumps 4% After Scrapping Solidigm’s U.S. IPO; Micron and SanDisk Edge Higher - 24/7 Wall St.](https://news.google.com/rss/articles/CBMixAFBVV95cUxPMllOMGRCWTM3ZHdxbDF0azJnZExNa2ZfM3A2WHFGSEZaZHY5WXFoV3NUUmE5WWdvV1lTRTRBcWh5LU9fX2RkYlRzVmlaZUxKOGhMZy1ScDVNajFjcVRTTk5FTHV3RzgtRmFJTXY5Y1Y1MDhibnFpUm55WnFwN3M3ZVhlcG1WS3ZBSUt6b0NrUk1ZR0xkY3RDVGRwajhlbDVFNXM4ZGhnZ3piaDY4VjFrOXZtVDBqc1Vvc0l3Qll1NlhyUXBs?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 23 Oct 2026 13:25:00 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Memory Stocks Rally Pre-Market as SK Hynix Surges Over 6%: Can the Stock Break Through the $145 Resistance Level? - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.21 | -9.62% | N/A | 877.55 | 971.00 | -9.62% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「memory」，共 1 篇新聞命中。 方向判斷命中詞：rally, surges。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Memory Stocks Rally Pre-Market as SK Hynix Surges Over 6%: Can the Stock Break Through the $145 Resistance Level? - TradingKey](https://news.google.com/rss/articles/CBMi0AFBVV95cUxOemgtOHhMRWY2ZGZMODRaZl94M2ttNEpISG90VU96NGNWcmVjTFdZTEx6cXlwMmpwd1FwTXJQTlJYTnhhc2t2ZzJhU1czRTFsY3pqVmtJYklVanlqaEY2eXV6Ul8walBlQjIxMjVaeXIta0hWelNvNE5jNHJMS2VtSmlGZlRJcnJFekRZUmg4MXI3NFpoLUNaRGJwdWMwZV9NamR3d1lBeHNKbG9vbTBhQ29JYmF2dkh6c1ZXV0g3YkpUOWNlTmhMMFh4ZUJCeEc4?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 23 Oct 2026 15:18:04 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：個股動態報導內容-82A5A219-765B-4154-BF8F-210BB2829DF9 - MoneyDJ理財網；個股動態報導內容-F1107D08-018C-4ADE-9F29-F3768B6DA8BC - MoneyDJ理財網；基金-FundDJ基智網 - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-82A5A219-765B-4154-BF8F-210BB2829DF9 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilAFBVV95cUxNb1pvMUc1clVKUENLaFNvS0VRSEJLSTRhWTZ6YXJLQjh4bmhsWWxCenJUNGtXWFNySmFQWm5COEJpWUtWZFlud054bW10YXJPT2VJblVQRkZMZ2FFRF9NSTNYZzFRQ213MFd2Wmg4SGcwbEo5M0JhdVNGN3l1TVBHTGdORDJRY0J3aWlBd1ZiTDlMUXFQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 23 Oct 2026 08:24:29 GMT
- [個股動態報導內容-F1107D08-018C-4ADE-9F29-F3768B6DA8BC - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilAFBVV95cUxNaWpwT05pSGI3MEFIT04wVm9jWEpmRE9mUm5XalhxblpYdV9EY094amdJaDgwS2JEalBJYnpjbkpMUHhNSFZMTHpPVGRGNHNaRU5XenFJaUpIZHBPUnlyMm1kRnFuTFllQW02T29RRE45dnN2a3NFSmY1ZDRpT3NMX2RuN2pEd1gtdlZESkU3V0g0UXBD?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 23 Oct 2026 08:07:19 GMT
- [基金-FundDJ基智網 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikAFBVV95cUxPaElfMU13bmFIQXg3Y3NuOTR0OHVEWnNQT2dkT2MwVmpDX0s0UlpkZmIzZnNuamExVTFMbldTWG5uZXo0QWNoZ3p6RWY2aXV1UzBtRjczMjN3XzVMWHZ6YTFVaUpKVmo2ZkhzR29WNFVXUUZQb1lMdVlHbE1zQkxoWUxnOWhIa2NZX0R2alJGU1U?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 22 Oct 2026 17:41:57 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：台股翻黑下殺 台幣早盤震盪走貶7.8分 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股翻黑下殺 台幣早盤震盪走貶7.8分 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQTFFSOERNVXUxbklsV3BuNDlsSUZIeVdHazV3bm9pbjFLMzRBeUpjOFplY3MxZW1Zbjc5akNMX3oycHU4SFRoZTFCRThqckNOMXcxU00yZWpWY0ZoT2VGUVo5TG04dGtJMndhTHdzRFZjdXVsMEsxdkRiRXVOQ0pmc3QzNnE4QkN6NUdKR0F3MG51QQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 22 Oct 2026 04:35:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
