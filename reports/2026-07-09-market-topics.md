# 每日股市熱門話題分析 - 2026-07-09

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **AI 伺服器與資料中心**｜負向｜熱度 8｜市場確認 73.84｜同向 5/6
2. **半導體與晶片供應鏈**｜負向｜熱度 7｜市場確認 68.55｜同向 4/5
3. **記憶體與 HBM 供應鏈**｜正向｜熱度 9｜市場確認 0.00｜同向 0/1
4. **散熱與液冷供應鏈**｜中性｜熱度 7｜市場確認 0.00｜同向 0/2
5. **綜合市場情緒**｜正向｜熱度 38｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.11（樣本 14）
- 5日相關係數：-0.36（樣本 14）
- 同向比例：9/14

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| AI 伺服器與資料中心 | 73.84 | 5/6 | 0 | +5.17% | +0.38% |
| 半導體與晶片供應鏈 | 68.55 | 4/5 | 0 | +4.18% | -2.69% |
| 記憶體與 HBM 供應鏈 | 0.00 | 0/1 | 1 | -1.02% | -24.04% |
| 散熱與液冷供應鏈 | 0.00 | 0/2 | 1 | -7.47% | -6.43% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：6月營收 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：緯創6月營收 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價呈負相關；應檢查正負向詞庫，並降低新聞直接提及但股價背離的權重。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-06-26 | 0.08 | 0.04 | +25.00% | 16 |
| 2026-06-27 | 0.12 | 0.29 | +57.89% | 19 |
| 2026-06-28 | 0.16 | 0.55 | +85.71% | 14 |
| 2026-06-29 | 0.49 | -0.25 | +38.46% | 13 |
| 2026-06-30 | 0.44 | -0.27 | +62.50% | 8 |
| 2026-07-01 | -0.08 | 0.25 | +30.77% | 13 |
| 2026-07-02 | 0.30 | 0.03 | +55.56% | 9 |
| 2026-07-03 | 0.21 | 0.08 | +55.56% | 18 |
| 2026-07-04 | -0.22 | -0.36 | +22.22% | 18 |
| 2026-07-05 | -0.00 | 0.24 | +40.00% | 10 |
| 2026-07-06 | N/A | N/A | 0.00% | 2 |
| 2026-07-07 | N/A | N/A | 0.00% | 1 |
| 2026-07-08 | -0.05 | -0.05 | +71.43% | 14 |
| 2026-07-09 | -0.11 | -0.36 | +64.29% | 14 |

## 歷史回測摘要

- 回測日期：2026-07-09
- 近5日 3日相關：0.64
- 近5日 5日相關：0.48
- 同向比例：0.00%
- 權重狀態：未調整

- 方向準確度：0.00%
- 信心排序準確度：0.64
- 診斷：正相關

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

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Will INTC Stock Break Below $108 as AI Chip Selloff Tests Intel Foundry Bulls? - FXLeaders；Nasdaq futures fall after record Samsung profit fails to calm AI chip worries - KITCO；AI 女星出道近一年終有作品，首度主演長片 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.59 | N/A | N/A | 110.24 | 114.68 | -3.87% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | -0.06 | -3.32% | +17.04% | 204.12 | 211.14 | -3.32% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | -0.06 | N/A | N/A | 517.41 | 517.41 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.04 | +0.82% | -1.60% | 2,465.00 | 2,465.00 | 0.00% | 未明確 | 74.39 | N/A | 416.98B TWD / 30.09% | 2026-06-01 |
| MSFT 微軟 | 產業/供應鏈推估 | -0.04 | -2.39% | -24.34% | 383.34 | 506.69 | -24.34% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -13.00% | +25.58% | 388.69 | 446.77 | -13.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.04 | -8.36% | -11.10% | 625.00 | 680.00 | -8.09% | 同向 | 10.86 | N/A | 63.03B TWD / 28.57% | 2026-06-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.04 | -4.77% | -7.84% | 3,995.00 | 4,310.00 | -7.31% | 同向 | 62.91 | N/A | 47.43B TWD / 4.99% | 2026-06-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 5 篇新聞出現相關標籤。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 5 篇新聞出現相關標籤。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Will INTC Stock Break Below $108 as AI Chip Selloff Tests Intel Foundry Bulls? - FXLeaders](https://news.google.com/rss/articles/CBMiuwFBVV95cUxOT3FqbEVfOE9FZFQ4SVhUNGtmblNwNFNXV1FxdDdFYUlTN0QtZ3JySFAyYzVEQmcwXzJXaGhtdFVxeWlOUWIyRlZQWHJfUHpWWjFDQnk5VU0weXpBcVNOTmdBMEI2MjZWc01ZOTZpQUczQ2U1Z1Y5WlBMN2MzcUtISERyQWhfV3d6bnFOOUFUYnJUMWYzUXpLMWlXM1RVRkdlczJaVVdDTkhTMWtnbXZpcDJObHhOWi04QjdN?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 08 Jul 2026 05:25:19 GMT
- [Nasdaq futures fall after record Samsung profit fails to calm AI chip worries - KITCO](https://news.google.com/rss/articles/CBMiuAFBVV95cUxPdzZ4S3Jha3hEdzRzM3V0RHBiNWhsNW54LXo1aU9aTGhYWWlZX2VSMHNsNzJDTm1tSmQxNjlZSEJFUGlnWlV0Qmc1cFI3RzJpSmhBdkdBNUZNNkVVWDdhY2xRc25SVEhqZjFkTnhzaG51ZnZld3dzSDNGUG9EZy1SZ05hZklIV3g4SXZzRUZYanNTUWdVM0Fsb3BjSngxeDgxbXV2TTZRU1hTa0dtcmhjVW9BNDIwaUhJ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 07 Jul 2026 12:58:15 GMT
- [AI 女星出道近一年終有作品，首度主演長片 - TechNews 科技新報](https://news.google.com/rss/articles/CBMingFBVV95cUxPUks2ZUdiTUR0b3M4YldJa09jSkotczZUc2tpamtDX2dQczhTUG9sUk1kakhaOW80UlF4R0hubk0wMzRxZzd0Rmw4U0JDcnBLZjZDRkh3YzdkT2Y1SDhsTEZvZTVhZ1doMkh0S1pmcTlSblh5dDhzZkJhM0VsRFBiMTBBV3pNMjBQSV9BTkJlWHByTFpLX2M1dmJZY3dJUQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 07 Jul 2026 08:21:01 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel and Applied Materials Dive 10%, AMD Craters 8% as Samsung Earnings Trigger Chip Selloff - 24/7 Wall St.；Will INTC Stock Break Below $108 as AI Chip Selloff Tests Intel Foundry Bulls? - FXLeaders；Nasdaq futures fall after record Samsung profit fails to calm AI chip worries - KITCO

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.62 | N/A | N/A | 110.24 | 114.68 | -3.87% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.53 | N/A | N/A | 517.41 | 517.41 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.04 | +0.82% | -1.60% | 2,465.00 | 2,465.00 | 0.00% | 未明確 | 74.39 | N/A | 416.98B TWD / 30.09% | 2026-06-01 |
| 2303 聯電 | 產業/供應鏈推估 | -0.05 | -4.40% | -3.55% | 163.00 | 164.50 | -0.91% | 同向 | 4.00 | N/A | 23.12B TWD / 22.85% | 2026-07-01 |
| NVDA 輝達 | 產業/供應鏈推估 | -0.04 | -3.32% | +17.04% | 204.12 | 211.14 | -3.32% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | -0.04 | N/A | N/A | 948.80 | 971.00 | -2.29% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | -0.04 | -1.02% | -24.04% | 1,727.18 | 2,335.00 | -26.03% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -13.00% | +25.58% | 388.69 | 446.77 | -13.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel、INTC」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 3 篇新聞出現相關標籤。 方向判斷命中詞：fall。

### 主要來源

- [Intel and Applied Materials Dive 10%, AMD Craters 8% as Samsung Earnings Trigger Chip Selloff - 24/7 Wall St.](https://news.google.com/rss/articles/CBMizwFBVV95cUxOTXNNVnlfdi1fcEg1YVdVVGJvdmQ2amIteUpfeWlVdHIyZ1lUOWpYY2dxdzVuSDNiZW1OXzJEQlhDcHlCT1ZmWDRQSUhyc3I5aDRkZnVSZU5BWlVsY3N3ejczV1JEM0c1bmZ1a0hNc2JqQU5Ub3I1MTF0c2ZhRmxCdzdLUThoMWFxTVo2bnRGMlRySzM5T2o2MkhWcGlodnVpZTRrcGlDdEhIazlGQWIwU0libWxSZk5iem5TNUQ3ajRwWWpxaWs5VzJKcW1oMm8?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 07 Jul 2026 14:27:59 GMT
- [Will INTC Stock Break Below $108 as AI Chip Selloff Tests Intel Foundry Bulls? - FXLeaders](https://news.google.com/rss/articles/CBMiuwFBVV95cUxOT3FqbEVfOE9FZFQ4SVhUNGtmblNwNFNXV1FxdDdFYUlTN0QtZ3JySFAyYzVEQmcwXzJXaGhtdFVxeWlOUWIyRlZQWHJfUHpWWjFDQnk5VU0weXpBcVNOTmdBMEI2MjZWc01ZOTZpQUczQ2U1Z1Y5WlBMN2MzcUtISERyQWhfV3d6bnFOOUFUYnJUMWYzUXpLMWlXM1RVRkdlczJaVVdDTkhTMWtnbXZpcDJObHhOWi04QjdN?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 08 Jul 2026 05:25:19 GMT
- [Nasdaq futures fall after record Samsung profit fails to calm AI chip worries - KITCO](https://news.google.com/rss/articles/CBMiuAFBVV95cUxPdzZ4S3Jha3hEdzRzM3V0RHBiNWhsNW54LXo1aU9aTGhYWWlZX2VSMHNsNzJDTm1tSmQxNjlZSEJFUGlnWlV0Qmc1cFI3RzJpSmhBdkdBNUZNNkVVWDdhY2xRc25SVEhqZjFkTnhzaG51ZnZld3dzSDNGUG9EZy1SZ05hZklIV3g4SXZzRUZYanNTUWdVM0Fsb3BjSngxeDgxbXV2TTZRU1hTa0dtcmhjVW9BNDIwaUhJ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 07 Jul 2026 12:58:15 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：INTC, WDC, SNDK, AMD: Red-Hot AI Chip Stocks Lose Sheen In Samsung-Triggered Selloff - Yahoo Finance；INTC, WDC, SNDK, AMD: Red-Hot AI Chip Stocks Lose Sheen In Samsung-Triggered Selloff - TradingView；Memory Stock Sell-Off: Is This the Time to Buy Micron Technology and Sandisk Like There's No Tomorrow? - The Motley Fool

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| SNDK SanDisk | 新聞直接提及 | +0.31 | -1.02% | -24.04% | 1,727.18 | 2,335.00 | -26.03% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 新聞直接提及 | +0.62 | N/A | N/A | 948.80 | 971.00 | -2.29% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.53 | N/A | N/A | 517.41 | 517.41 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.53 | N/A | N/A | 110.24 | 114.68 | -3.87% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -3.32% | +17.04% | 204.12 | 211.14 | -3.32% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- SNDK：新聞直接提及「SNDK、SanDisk」，共 6 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：outperform。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- MU：新聞直接提及「Micron Technology、Micron、MU」，共 3 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [INTC, WDC, SNDK, AMD: Red-Hot AI Chip Stocks Lose Sheen In Samsung-Triggered Selloff - Yahoo Finance](https://news.google.com/rss/articles/CBMijwFBVV95cUxQd0ZHWDZOUDc2UWRpWmJQMGNjUXRLVHo3cl9YaDJDYXVHS1ZPZFVGNUJiWTZTal8xcEJfcjN4NjNrNmFTWUJRSDhPX1FPNEJnT0J5MVQyMEhBWVFrMW9mLVN1VTg4dkZ3MkpiQmRzaFN2WDNBLVVPM1prQ1c5dEhRSnBEaC1xb0NGRmVhbWswQQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 08 Jul 2026 02:40:00 GMT
- [INTC, WDC, SNDK, AMD: Red-Hot AI Chip Stocks Lose Sheen In Samsung-Triggered Selloff - TradingView](https://news.google.com/rss/articles/CBMi2AFBVV95cUxPbnh0RjlQR2ZhZkZOcGRZaUVvdGFnUVltVDVfVFJnN1lyQ3gxRkJBVHc2V0RhN2JCSWpPejQ5UjFBVHpDcHZxWFdkRzJQWkp1NXExei02VWJteW1mSDd5UzlDSGpzVzNUcVlGbG5tdlh0RTgxamNHQS0wMGNveVRqOVh1TDZ5WlhzTWlmejJycWRLR3lGVjhWd29OamFad0xuUU1NOHAtbG0xQjdBVTlSMjNmUTg5Ykp2RHJmb0J0TEoxOXhIcm5xc2I5cl92TXNtTEU2YV9mbWk?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 08 Jul 2026 02:40:00 GMT
- [Memory Stock Sell-Off: Is This the Time to Buy Micron Technology and Sandisk Like There's No Tomorrow? - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxQOWVlSTMzTlZIaU9Qd1d4WTBDdU9pX1VVSm8zbkZwMHJjODhzdEJwbU9zV0NVeWtZMkJmWDdHQnM2UUl1bmt3MmNCUi14a3lDTDQ3bkZjX3hOZ2pCUmdWYTFuN1gzbDJubFUxTmF2QmRXRjNVY0hxUWVhNzhWa01Ock1NU3AxNWwyRnJBdHEwSUFFWTllVFhLUA?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 08 Jul 2026 22:48:13 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：〈財經週報-台股熱點〉從AI到外太空 散熱族群題材不斷 - 自由時報；高通投資人日震撼登場：台廠奇鋐、廣達、台積電誰受惠？AI200／AI250／AI300 與 HBC 是什麼？｜產業熱話 - sinotrade.com.tw；散熱三雄6月營收僅雙鴻月減；上半年皆同期高 - 台視全球資訊網

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.31 | -15.76% | -11.26% | 2,325.00 | 2,835.00 | -17.99% | 背離 | 61.06 | N/A | 17.62B TWD / 66.11% | 2026-07-01 |
| 2330 台積電 | 新聞直接提及 | +0.34 | +0.82% | -1.60% | 2,465.00 | 2,465.00 | 0.00% | 未明確 | 74.39 | N/A | 416.98B TWD / 30.09% | 2026-06-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱、奇鋐」，共 5 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：受惠。
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 方向判斷命中詞：受惠。

### 主要來源

- [〈財經週報-台股熱點〉從AI到外太空 散熱族群題材不斷 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTE9rc0xOT3JaSGZPbV9uNjZUNmJLdkctMThER29ldnFaMXp1YlBQajNxaVBBcHlrVEFOOUNLZkxISUt1ZVFOMHF4WXBSd1Jtc0plYWh5bDRrdVk?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 07 Jul 2026 07:16:53 GMT
- [高通投資人日震撼登場：台廠奇鋐、廣達、台積電誰受惠？AI200／AI250／AI300 與 HBC 是什麼？｜產業熱話 - sinotrade.com.tw](https://news.google.com/rss/articles/CBMiiwRBVV95cUxOdUZybS1JWUptQTFaTkFqUGIxMVEtaHV3SzNPTWJ1QXVLNDI4ck9hVUVHYlNtMGZoZUVxa3lJaE1uOEViVVl6eUVIVWVJVXJUYTUtel9KQzd3NEliUmxxQ3ZhRGR0YnRRNC1WaS0yM0M5UVoxbUtSZENab05MUUNyYlZwZzVtX05ILWlGWlNuVUgteE5qOTRIQk9DRURYa09BV1lYdTBxLXZ6ZHZMX3gyRE1ieDMxZUpfNnl1X2w2TjYyQ1FHWjQ4X2taUy1qUkNuYnR6Qm5TYjlkemluaXBIVW1jQTN1VnQySzlfazY3d2xZd1F2b0RKeHBMU0NvTTFpTmxHbWJfNUh5U1lra19IRmM0VGlCOGQxTGxrNFhaZVRRRXZIeE8yS244SF9ORDFQcjJsV2Z0bXpfSmh6NUxaN0dvMjd0NnJENzBmbTY4VFQ1VVJ2Z0dsWVg2ay1yV2xBYU84Mi1lblptNGhZSjRyeExST29tWWtoZ3ZLcEdLTXZZVEQzcV9vWmVycW1OcnlNUlJVZlFNdU9wTnVEVjItVlVVc2Q4RVBCcnFMempuN2hfMGJ2YXJveFhFdG5ycF9vam5hcFp0ajc2c0xXMVFxeGRvSC1yTUxPNWlGOHlzMkVqajRWdzNQV2xwOWU5alBpdG5LWFppQWxQUUNLRGZSZGw2clM4TWZ2R2Jj?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 07 Jul 2026 12:48:15 GMT
- [散熱三雄6月營收僅雙鴻月減；上半年皆同期高 - 台視全球資訊網](https://news.google.com/rss/articles/CBMikgFBVV95cUxPRmxvNEpjZFpLMm5pZXh2TTN4VTA4eWJmanNXNDRPR094Nk9ZUUdLY3Y3VmNSeUtVdkJpc09TM0Y1UDM0ZkhiU05QYVJhMWtmdjIyT0ZBMDBsNi03NWZmRGJTSUlrckxLSGZNdll0eXdHdWYwcFdNTm5kcVIxTGl3U1N2Y3l0b1ZzVUZiRjVzWEJWUQ?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 08 Jul 2026 02:32:06 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：獨家／台股明年中三大改革！千金股不分整零1元一跳 零股撮合縮短至1秒 - 經濟日報；台股交易時間延長到三點半？ 彭金隆給答案了 - 經濟日報；台股高價股將迎來每檔「1元一跳」的全新時代 市場壓力測試...借鏡美股 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [獨家／台股明年中三大改革！千金股不分整零1元一跳 零股撮合縮短至1秒 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9Bb2lKZlZfR3ZOLUtzcmYxMEk3YlN1cUhUMGxRN0FnNG1zMlBIWnJLVFhEZ1dtb3NYV1M4c2NudklEOWFBRHUyOWlzZzdOWjl5VFdiM3FPLVp5QdIBX0FVX3lxTFBMNFgza0FPbzhja2Mwa3ZSYThBY1BycnUtdUFJMjI3Mjd3Y084ZTdqeDQ0R2tjbGNmaVZ6QzJnQ3B6Q3JDak42MnB0V2xEUEQ5TkVVc1k2N2dxRERTVmNF?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 08 Jul 2026 06:22:33 GMT
- [台股交易時間延長到三點半？ 彭金隆給答案了 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE8tVnZ4SWNOcjlQb0JYU0J5dkxlOE95b0pXTzVST1hBVlBKS1d5dndqZ1l5WXIxUHNHSmp5ejh3R1R2TGppVFU3Q2xXcktZVXhHbVJndkc1bF9LZ9IBX0FVX3lxTE4wcEk4TEZYdm44V1M3S29Gdy0yT3dMZFpPNGNqa05GRkwwWW1hUVg0TnR3QVN6VTg0V2ZxNVlVQUluRXY2OG1MaWRuQ3UtdlljSElaQ3dOVGkzVFNyNllR?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 08 Jul 2026 02:34:28 GMT
- [台股高價股將迎來每檔「1元一跳」的全新時代 市場壓力測試...借鏡美股 - 經濟日報](https://news.google.com/rss/articles/CBMidEFVX3lxTE1sSUh6VHZmSzNhd2MzRk43bUdPaTBsZ3RZbHg0aTBhWk1sbDVjUmp2bVJxNmF4dFJYOUU4MWxUc3BOemNvb0ZLcVhvTjc1UGtHaGloaUxKUGN4NnMyYjlzZExzeHdFdHNxSlctUFZQc3ZuUk9H0gFfQVVfeXFMUHVqQ3MxZGVUdU5OS2NLMWtGeDQ0QWhXMkFEdTR6cXBfbDMwM3lEQ19YM3lYSWdfNzh3SFZzQnhuVHdTVTJOSWxUR0dzbG1lQUhmMHZuNm4zRHpQOEt4bTg?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 08 Jul 2026 17:44:09 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》尾盤拉台積，收漲255點，月線沒站穩-新聞內容-基金 - MoneyDJ；國票證券：台股上方壓力仍相對沉重- 新聞 - MoneyDJ；統一證券：台股短線技術面陷入整理- 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》尾盤拉台積，收漲255點，月線沒站穩-新聞內容-基金 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxQaVlRT3lqNUMtWXNCS0tON0piaF9tYkNwQ3ZteUdJQ3lCc1MtTHZkS0x6d3ctMUUwemNxakJFcWZvbVBjNWpvT3oxamZNbTVRTV96VHNoSTNRWlJGeWlPMnBiMXE1TmhSeHpZTzhlMGh0Qm9mUjBEeDNoRlloZ2dBcTRReHM0ajg3SDlFUzJtVkk?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 08 Jul 2026 07:57:00 GMT
- [國票證券：台股上方壓力仍相對沉重- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQNW1yQXp4WThWRG9FbmdvcDYzNk5VSjhhM3g3cDlNcTFtcENzUlhlUVFteTYtdGEzTnZ0RXZYQUlGeGNXN3R1OEZ0a0NYZWp2a1VEQlVKb3lNVDdsSGJIN2ZYblNPY1J4MVl2WmNjSUpaeGE5bEU5UDJWNkZ0TmVRQXdYSVdwWnZ2ZF8xTmN4SmVkUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 08 Jul 2026 00:51:00 GMT
- [統一證券：台股短線技術面陷入整理- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPS1J6dm1aNVBUdW04dHhUbU1QQjBYT29GQWFMRWkwRWNPdzBkYTNFR2xlUHhuNG9zRFhnemtLaGFTcUVuQzU3aGstLUV2ZF95bkFRZFBRRFhmS2RSUHFHenJQcjBjT3hQT0p6QnAxTkt5Qk1HQ2doTWRjN1gyM3drQmotRVRqM1Y5TXl2N1E3WHUtQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 08 Jul 2026 00:51:00 GMT

## 新興題材：6月營收

摘要：新興題材：6月營收 相關新聞集中在：華邦電營收報喜！6月營收年增190% 最新目標價曝光 - Yahoo股市；國巨*6月營收續創單月新高 華新科寫逾5年最佳 - news.cnyes.com

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [華邦電營收報喜！6月營收年增190% 最新目標價曝光 - Yahoo股市](https://news.google.com/rss/articles/CBMixwJBVV95cUxPR21oSlVDMG5za1hrbmlWLXFtZnlUblY4bzhuOWJwTlJrQ01adVhub05nRDFoaEtBLXU2bVlqS1F0SGtrdEVzeFRiNV9KUVBxbUNQTElOcVF5bXpLV0ladExaM0ZFaUJjNE9SR3FzZE82RXV1MFV6Z01pcnA4V3dpSGZ2cGd6NnZ1cGp0dlZjblhMRE1MeWRCWlNLUmdYR0R4bU9BSUc1SXR3a1FySWJtWkZ3RVkwMlM4dlQtVWM2WTI4M0hVSTh2SzB4RDNpSnN3Yk9ENlY0ZXl6czVrekxZRjhRVE9ubVF3cVNTT1V3Vzd0blFqV2VyY3RSTzZWSHNPZkd4OEFMU2E0TVJVTC1EU25TT0xTYzdLTmtQZ3p6bElCQWZDV0hyXzZzdWh1LUJ4RnZjbno3cG8wakdPZjZ1N1VvZ2tXTEU?oc=5) - Google News source discovery | Yahoo 奇摩股市 Wed, 08 Jul 2026 11:00:00 GMT
- [國巨*6月營收續創單月新高 華新科寫逾5年最佳 - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTE9OTFM5WS1yRHJCQ2MxUF9qYXQ1NDJGOE9IYmhZZU4xS3cwQVVGeHk2S3VLQnpIMlpuQ0RxVWNvUzc1aXh2a0xpWm5RdDZINzg?oc=5) - Google News source discovery | 鉅亨網 Wed, 08 Jul 2026 10:38:30 GMT

## 新興題材：緯創6月營收

摘要：新興題材：緯創6月營收 相關新聞集中在：緯創6月營收寫歷史次高 第三季桌機螢幕買氣略回溫 - Yahoo股市；緯創6月營收3218億元年增5成 改寫歷史次高 - Yahoo股市

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [緯創6月營收寫歷史次高 第三季桌機螢幕買氣略回溫 - Yahoo股市](https://news.google.com/rss/articles/CBMi5gJBVV95cUxPcHdIQ1dlQVpxYzM1YUo0Y25OdDNFQm9qYmdBNzBZMzdpZXlFbFZkZ21RNkF4WjJqaGFlcUwwby1hbXNSLXJFck1tS1doYXQwTlpqZXdvSG9VTEN0Vk1fdjZRdGJHLWxpNjhvbTRQNGFMRnZUY1dOY3E2eGdSdUc2Szl1X0dWRFJxTjRuX1VSelZQbDBCZkF1UFYzVEhoemkxVjV2UEdsdlY4a09MV1NIaThQalJ0NHNGMjZWQ2NMSWtBWmFWN1B6d1dDMEVWRXEyRnp3Qk9LRmxaQzJPQlV3UHIxbFdYWV9id1FLenRBSzY0dzJkNmEwUjdLbE1UVTB4WDBVTUtqZGJQVVQ5SGhTUlpBTTJHcWNyeUNIZ1dpemdBX050a1YxWHZWU0lIMkJYUEFyZ28wRlFWSGVnQWtKZjRtdFQtTG5YWFdjaXhvQ3lvNEI2Ujdhc0N5Uy01NmxNTC1Ba1dR?oc=5) - Google News source discovery | Yahoo 奇摩股市 Wed, 08 Jul 2026 09:23:46 GMT
- [緯創6月營收3218億元年增5成 改寫歷史次高 - Yahoo股市](https://news.google.com/rss/articles/CBMipAJBVV95cUxOd1dLMXZNSGVHa1pzQ3BqSU1oUHdKQWN1M3doOXhtTWhQN09LUkNTRzdRbkV1TTV0VUtmZl9id1FlQVpwNWplemdVUXRxMUhlMnN2UDNnZk9KY05LRnBIR0lRR3BKd25iWVZuYUJ0Vm9zYi1mTTFISFFwUm9LNHhoV3VPXzFDVlQ4NjVqazR4THN5TnlHTjRJakFtNENpVFhKbFl1NXMtdHljQ1Z5c0FXN1hSNnVsTnR4VE43Z1BLV3c0aDRWWjE0M3VmMXdKUnVNQTY5d3V2aFBsQy1YSmZxUm85YVlycWlSWHNDR1o2ck5RejAzUGpNTnFzanZpNVVob2tWLXA2MEk5d0cyOHpnVlgtaUl5WGdhUTBjTjhIeVBGb3k2?oc=5) - Google News source discovery | Yahoo 奇摩股市 Wed, 08 Jul 2026 08:08:26 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
- TWSE PER/PBR 抓取失敗：Expecting value: line 1 column 1 (char 0)
