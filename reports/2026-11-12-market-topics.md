# 每日股市熱門話題分析 - 2026-11-12

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **AI 伺服器與資料中心**｜中性｜熱度 15｜市場確認 N/A｜同向 0/0
2. **綜合市場情緒**｜負向｜熱度 36｜市場確認 17.38｜同向 1/3
3. **新興題材：10月營收**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0
4. **關稅與供應鏈轉移**｜正向｜熱度 3｜市場確認 62.14｜同向 2/3
5. **半導體與晶片供應鏈**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.09（樣本 14）
- 5日相關係數：0.07（樣本 11）
- 同向比例：7/14

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| AI 伺服器與資料中心 | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | 17.38 | 1/3 | 2 | -1.98% | +0.03% |
| 新興題材：10月營收 | N/A | 0/0 | 0 | N/A | N/A |
| 關稅與供應鏈轉移 | 62.14 | 2/3 | 1 | +5.16% | -1.61% |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 記憶體與 HBM 供應鏈 | 35.95 | 1/2 | 1 | +0.32% | -5.76% |
| 新興題材：CoreWeave | 10.26 | 3/6 | 3 | -8.25% | +10.21% |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 相關性偏弱；應提高同向價格確認權重，降低泛 AI、泛半導體等寬標籤推估權重。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-10-29 | -0.05 | 0.04 | +42.86% | 14 |
| 2026-10-30 | -0.00 | -0.05 | +47.62% | 21 |
| 2026-10-31 | 0.50 | -0.68 | +80.00% | 15 |
| 2026-11-01 | 0.47 | -0.40 | +85.71% | 14 |
| 2026-11-02 | -0.15 | -0.06 | +27.78% | 18 |
| 2026-11-03 | -0.03 | 0.08 | +40.91% | 22 |
| 2026-11-04 | -0.21 | 0.35 | +15.79% | 19 |
| 2026-11-05 | 0.13 | -0.53 | +66.67% | 12 |
| 2026-11-06 | -0.18 | 0.77 | +100.00% | 5 |
| 2026-11-08 | -0.21 | 0.03 | +23.08% | 13 |
| 2026-11-09 | -0.56 | -0.62 | +60.00% | 10 |
| 2026-11-10 | -0.32 | 0.24 | +3.45% | 29 |
| 2026-11-11 | 0.34 | -0.26 | +46.67% | 15 |
| 2026-11-12 | -0.09 | 0.07 | +50.00% | 14 |

## 歷史回測摘要

- 回測日期：2026-11-12
- 近5日 3日相關：-0.01
- 近5日 5日相關：0.07
- 同向比例：+57.14%
- 權重狀態：未調整

- 方向準確度：+57.14%
- 信心排序準確度：-0.01
- 診斷：低相關

調整原因：近 5 日信心分數與股價關係偏低，提高價格確認，降低寬題材推估。；關鍵詞×公司後續樣本有效 1 筆，未達 30 筆，不調整樣本權重

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

摘要：AI 伺服器與資料中心 相關新聞集中在：AMD vs. Intel: Which Is the Better Artificial Intelligence (AI) Chip Stock to Buy Right Now? - The Motley Fool；Prediction: This Could Be the Biggest AI Stock You’re Not Talking About - 24/7 Wall St.；「AI 界央行」輝達股價止跌回升，美股聚焦黃仁勳案發展 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | 0.00 | -23.93% | -13.46% | 173.73 | 228.38 | -23.93% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | 0.00 | -45.50% | +54.09% | 62.50 | 114.68 | -45.50% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | +7.13% | N/A | 552.90 | 552.90 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +12.18% | +5.97% | 2,385.00 | 2,480.00 | -3.83% | 不適用 | 86.28 | 27.76 | 586.89B TWD / 59.71% | 2026-11-01 |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +15.74% | +5.92% | 521.12 | 521.13 | -0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -1.70% | -11.32% | 345.22 | 446.77 | -22.73% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | +17.08% | -1.59% | 621.00 | 703.00 | -11.66% | 不適用 | 17.55 | 35.42 | 88.62B TWD / 47.13% | 2026-11-01 |
| 2454 聯發科 | 產業/供應鏈推估 | 0.00 | +17.70% | +7.40% | 4,050.00 | 4,920.00 | -17.68% | 不適用 | 60.69 | 65.90 | 55.03B TWD / 5.77% | 2026-11-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AMD vs. Intel: Which Is the Better Artificial Intelligence (AI) Chip Stock to Buy Right Now? - The Motley Fool](https://news.google.com/rss/articles/CBMiygFBVV95cUxNal81S2Q0LVVWX3p5UkFSeTFmRjZCUUNjaVA4eTVqVmFDYUpJT3g1NHE1MDhqUWFRcjJXUzZDa0Vkd2pLUDJqVXRfYVNORWt6SS1rT2FxUmcxSzBYQW1pS2VyUGhPV0toYnNHbWdNME5mUWNJOUtlVzZNTFVsMzZYQmg0RmJucl9sWHBVRVdEVlV2Q3dtclBzX1ZuMTIxNzlkYlB6Qkg3eGxndEFBMDJsQnJNdFdtSG5RSGNQMDJwbld3UEhUU2RlM09R?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 10 Nov 2026 13:52:00 GMT
- [Prediction: This Could Be the Biggest AI Stock You’re Not Talking About - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiswFBVV95cUxQaVNDUzd2SzYyYjBINVo5Z0RfQ2dXX0liR1FOWmNJaktEQjZfWHRBQm0yUDFoc2lmR0ZQZkRhZHVnSXJaYW5SNkVhc0I1cXg5TXZlWGQwQjZsMUFCbWc4SHY3Wm1kUEd0blVIaGpJalFtTDVfeGs4STN0UzRsWjEtLUtTS2pUcTBKOUJqSHpWVG5GUXB4Nll5WGU2UDdvQXJKcXdKanR5bFZkNXdkMm51YlRDdw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 11 Nov 2026 16:03:00 GMT
- [「AI 界央行」輝達股價止跌回升，美股聚焦黃仁勳案發展 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiqAFBVV95cUxOMmhjU0NLbG9Gb0UwYjRLVk1GQWQ2YWFybm9EZVVKQkI1cXJGY0dZY1dUT0ZIR2FWVF94blVONndwNDZNeGg1cTNNMkN0X1Y3d0FUR0lHX3JJNUJkSUtQay12a3dYbDNDVndOZU5pTDZST2FiSlEtVnJyTTVrVjJMOXBMTDM4XzltdGlMN0hmeTJjZmcyY0s0dzF2RHlWY2VXWlJKNmRoXy0?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 12 Nov 2026 01:13:52 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股 V 型反彈 挑戰單周最大漲點 指數年底前上看48,200點 - 經濟日報；台股早盤震盪逾500點　台積電跌40元 - 經濟日報；黃仁勳人事傳聞衝擊輝達盤後重挫！台股震盪回測44K 聯發科領軍抗空 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | -0.42 | -23.93% | -13.46% | 173.73 | 228.38 | -23.93% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | -0.21 | +12.18% | +5.97% | 2,385.00 | 2,480.00 | -3.83% | 背離 | 86.28 | 27.76 | 586.89B TWD / 59.71% | 2026-11-01 |
| 2454 聯發科 | 新聞直接提及 | -0.21 | +17.70% | +7.40% | 4,050.00 | 4,920.00 | -17.68% | 背離 | 60.69 | 65.90 | 55.03B TWD / 5.77% | 2026-11-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：重挫, 衝擊。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。
- 2454：新聞直接提及「聯發科」，共 1 篇新聞命中。 方向判斷命中詞：重挫, 衝擊。

### 主要來源

- [台股 V 型反彈 挑戰單周最大漲點 指數年底前上看48,200點 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBORVY1QlQ2cWtvcDRFX1N0d2IxMVZQQ3UxaXV2TGdBSFJUX0lHOXM5eGVOY0QxdUQ5bmNxTTM4MlV6Y0hMdy1LUmdzOFB5X1JmNEt6SDFqdlRmUdIBX0FVX3lxTE0zbEYxUFk3R3BYYWxJdldoWWlNWE9yMTB4S1M5dmVxUWs5cXUweTllMFB4SG8yZXZzV1FEVGROYmxOOWtnRTVCdTR6OFNaeGtvYUtBRXo4Q2J4WGd5clVr?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 11 Nov 2026 17:15:44 GMT
- [台股早盤震盪逾500點　台積電跌40元 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBwcU5Mb0cxZERoTHB6bzZkRnVlV1M0MU05dGRyWUpBNjRRVld3Wkc3VVZlSlpRS1N6U0gxVWhfTHo1cUgzb0laYVF2dFRzZTY5T3dJZkZHaXQ0UdIBX0FVX3lxTE80Q1VpbEZmS09LX1BNczBMYUJ6cE5TSkk5UnFJYXVpZEEyX0ZtZnljNmEzNHJoYjNjUnlQUEZleldUMWZVd0dkazM0SHVOazFuM3RoQzYxWWVlNy1PZUxR?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 12 Nov 2026 01:30:43 GMT
- [黃仁勳人事傳聞衝擊輝達盤後重挫！台股震盪回測44K 聯發科領軍抗空 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5aYU1RdEgxWnR2QjlSYUF0M21NRmIzcVJrYVhQakxoU0tUbFlCLXJuOFVHaGZKVVRXZTNBRExJdnNsS21pb3ZRU2VYU2dlV3JFQThxb1RWM0ROZ9IBX0FVX3lxTE5ENEoyYktmTWpZbnhJUm9fRWl2QXRUUXNWQ3RIV0JEYWtWMG9acGdzcTlqVFRNOWdibF9aNTA1eWVvZENfWTBobVdMS2xLNkNwZl82NjBkalNrZGJpOVc0?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 11 Nov 2026 08:00:00 GMT

## 新興題材：10月營收

摘要：新興題材：10月營收 相關新聞集中在：指數重返44K 10月營收後選股21檔 - 三立新聞網SETN.com；豪配9元現金股利！台積電領漲3.5% 功率半導體「這檔」10月營收連2月寫新高大漲6%、健策漲8.72%最夯 - Yahoo股市；亞洲藏壽司前三季EPS 3.61元；10月營收創同期高- 新聞 - MoneyDJ

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | 0.00 | +12.18% | +5.97% | 2,385.00 | 2,480.00 | -3.83% | 不適用 | 86.28 | 27.76 | 586.89B TWD / 59.71% | 2026-11-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。

### 主要來源

- [指數重返44K 10月營收後選股21檔 - 三立新聞網SETN.com](https://news.google.com/rss/articles/CBMiS0FVX3lxTE1LdjRnZnhBRW1ZckwxT0lhdU41QzZ3R1pDc1BuTXVycU9seE9LckdKeFN4MW1kQ3AtWGRoWHJBZ2lhZDRfUlgweUlyTQ?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 11 Nov 2026 19:02:54 GMT
- [豪配9元現金股利！台積電領漲3.5% 功率半導體「這檔」10月營收連2月寫新高大漲6%、健策漲8.72%最夯 - Yahoo股市](https://news.google.com/rss/articles/CBMiyAJBVV95cUxPemx2NHRVeE03NE93OC1vUVJfQUd0YmU1dWVQVnVRUndQWFRFN0ZQamFxeGtoT1pDbmVKTER2SmFVcXY5V1lUaGo0eE1sMFlDQkFpRUFKd3hCcGNZUU1yYlZ6Q1Jkb2hMZFItRUoxRnFWUElWeURGTVRQdnBYcDhoajl3WDltaWhGNy1RMURKM2h4VDZyb2dTSjZvQlNRLUxsTEx2X2dVeTZHdmtQM2VCX1hydTNiYmNfcnpmZGVBTjYwVVh2bVNXSHBvSXd5a01VbVpkTk5WU3dqa0NvSV9sNGJDNl90M1AzYUVvX0RpakdDYmxSMG1sLWRBSFhrdFZJYVplNlIxWDByTTFobjRWV0pRcTctOFBoc042VDFHcXA1NDZQbTNSMnkzbWpJQmVPWE5HMElLVERXUFltVlF4ZnpqSFBHTDY2?oc=5) - Google News source discovery | Yahoo 奇摩股市 Wed, 11 Nov 2026 03:56:42 GMT
- [亞洲藏壽司前三季EPS 3.61元；10月營收創同期高- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxOeVJTWmQwc1RzVTNVUnVPRkJobzFmVkJ4X0xUeENsTzV5V055UDQyU01hNEZfcUp2S014b2FETk1lblBKZGZzTFQ4YWRZYjNrOTFveHRUV3dFR1RFTVhBcXg3Q2dpX1M2SUVOd1pLaUhNRExBRFdMVjM5VHJrVmpjOXJpV0hEVzZpSndvbzRtRXFuQQ?oc=5) - Google News source discovery | MoneyDJ Tue, 10 Nov 2026 09:22:00 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：整理包／黃仁勳概念股笑了！輝達季度財報超預期 完整台廠供應鏈名單、潛在受惠股一次看 - 經濟日報；SpaceX 太空算力 2028 年上看 5GW！外資點名鴻海、奇鋐、台光電供應鏈 - 鏈新聞 ABMedia；黃仁勳爭議牽動東南亞晶片供應鏈監管，泰專家：資料中心受考驗 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2317 鴻海 | 新聞直接提及 | +0.45 | +7.80% | +0.83% | 243.50 | 289.00 | -15.74% | 同向 | 15.21 | 15.95 | 1305.32B TWD / 45.73% | 2026-11-01 |
| NVDA 輝達 | 新聞直接提及 | +0.21 | -23.93% | -13.46% | 173.73 | 228.38 | -23.93% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3017 奇鋐 | 新聞直接提及 | +0.42 | +31.60% | +7.80% | 3,000.00 | 3,435.00 | -12.66% | 同向 | 90.78 | 33.61 | 22.10B TWD / 34.35% | 2026-11-01 |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +13.96% | +27.53% | 355.63 | 355.63 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 2317：新聞直接提及「鴻海」，共 1 篇新聞命中。 同時符合主題標籤：supply chain, tariff。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 3017：新聞直接提及「奇鋐」，共 1 篇新聞命中。

### 主要來源

- [整理包／黃仁勳概念股笑了！輝達季度財報超預期 完整台廠供應鏈名單、潛在受惠股一次看 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBQUlViSHpPeDVlY29yaHFNNE5NcVlUQnE3ZThTcXRGNHgxYTVPOVVTRDlaTDV6Zml5WEwxVHNSeGFDcnVHUHhRSW15SzNpU0dYVDU3dThWNEVCbkZI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 10 Nov 2026 08:00:00 GMT
- [SpaceX 太空算力 2028 年上看 5GW！外資點名鴻海、奇鋐、台光電供應鏈 - 鏈新聞 ABMedia](https://news.google.com/rss/articles/CBMiakFVX3lxTE9yUi1TMm0xWmlMZVR6VkE5cml3VzEzZGZzWEJvN1dKcWctQzRURFBmcGZWbkFTeFYzaEVqcHpzODY2MjJPSDhmYllSdjVjVVBHTXhVMVJLRlo1LU91YTEtN1dMcnc3NnhxMlE?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 10 Nov 2026 03:32:14 GMT
- [黃仁勳爭議牽動東南亞晶片供應鏈監管，泰專家：資料中心受考驗 - TechNews 科技新報](https://news.google.com/rss/articles/CBMi6wFBVV95cUxPVHlQaDEtSXFrUG8zeXZacHI3U1pwanlCMUs3bDRUa1Nobm5JbU5UeFRmMUZBLWhCMlRwMmxqOU1hUnZLTXhldmV6VXlWQk1ueTFjSTFZdVRmaUIxWGtndzFlb0hWakoxODRCUlRJMk5JM3hUNXhRc0NnQ1h1R0JvbXBkNjFQN1RESFFiM0lMWlB0SkpXR3N0aE1GdFBHaTgxMWE4UEttMThxN2lxZjZsUWNhZG1DMHlucGVfSVl6OWJHNTNDN2NTQ1h2VkN0M1AtRFptZGF0dTBiV3pOemJsX3lnUHhGS2JDZVhB?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 12 Nov 2026 00:38:44 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：AMD vs. Intel: Which Is the Better Artificial Intelligence (AI) Chip Stock to Buy Right Now? - The Motley Fool；INTC vs. TSM: Which Semiconductor Stock Has More Upside Now? - TradingView

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | -45.50% | +54.09% | 62.50 | 114.68 | -45.50% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | +7.13% | N/A | 552.90 | 552.90 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +12.18% | +5.97% | 2,385.00 | 2,480.00 | -3.83% | 不適用 | 86.28 | 27.76 | 586.89B TWD / 59.71% | 2026-11-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +13.04% | -1.42% | 105.00 | 164.50 | -36.17% | 不適用 | 6.80 | 15.36 | 25.20B TWD / 18.33% | 2026-11-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -23.93% | -13.46% | 173.73 | 228.38 | -23.93% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | -16.45% | N/A | 811.30 | 971.00 | -16.45% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | +17.08% | -5.76% | 977.69 | 2,335.00 | -58.13% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -1.70% | -11.32% | 345.22 | 446.77 | -22.73% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel、INTC」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 2 篇新聞出現相關標籤。

### 主要來源

- [AMD vs. Intel: Which Is the Better Artificial Intelligence (AI) Chip Stock to Buy Right Now? - The Motley Fool](https://news.google.com/rss/articles/CBMiygFBVV95cUxNal81S2Q0LVVWX3p5UkFSeTFmRjZCUUNjaVA4eTVqVmFDYUpJT3g1NHE1MDhqUWFRcjJXUzZDa0Vkd2pLUDJqVXRfYVNORWt6SS1rT2FxUmcxSzBYQW1pS2VyUGhPV0toYnNHbWdNME5mUWNJOUtlVzZNTFVsMzZYQmg0RmJucl9sWHBVRVdEVlV2Q3dtclBzX1ZuMTIxNzlkYlB6Qkg3eGxndEFBMDJsQnJNdFdtSG5RSGNQMDJwbld3UEhUU2RlM09R?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 10 Nov 2026 13:52:00 GMT
- [INTC vs. TSM: Which Semiconductor Stock Has More Upside Now? - TradingView](https://news.google.com/rss/articles/CBMiswFBVV95cUxOdmtzX3pXc0FBdzV5V25UekxfMVdSTUxuamZZRzVKZnA3WEJkN0JaZ01lTGhONm1XaU1oNzAyeDJ6dDlXbUN5NzFQR0FGeUlsMkpwaVNHa2dsSHBna2hFU0JURU5oLTRCMDhCeGxsRDVIRkRYazR1SEVrNDR2MUg5cHRBZE1jWDlHZFFSSThHYmlCMl94M1ZnSzhjcks4YnI4bXZvcU42WWlnUzRzajExdkpLUQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 10 Nov 2026 16:54:01 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Jim Cramer Says Micron Isn’t Going Away. Here’s Why He Picks It Over Sandisk - Yahoo Finance；Jim Cramer Says Micron Isn’t Going Away. Here’s Why He Picks It Over Sandisk - 24/7 Wall St.；Micron Stock Surges After CoreWeave's AI Earnings Surprise - Yahoo Finance

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.28 | -16.45% | N/A | 811.30 | 971.00 | -16.45% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.57 | +17.08% | -5.76% | 977.69 | 2,335.00 | -58.13% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | 0.00 | -23.93% | -13.46% | 173.73 | 228.38 | -23.93% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | 0.00 | -1.70% | -11.32% | 345.22 | 446.77 | -22.73% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、美光」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：surges。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 5 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：surges。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Jim Cramer Says Micron Isn’t Going Away. Here’s Why He Picks It Over Sandisk - Yahoo Finance](https://news.google.com/rss/articles/CBMilgFBVV95cUxPMnF5U3Z2R1JKTzUxTmdQUjVqOHE2eC1QZlEzZEZCbVZxSW5vejdvMHp6WEVvYVN3anRqQ0hqYk5Md3dpczR6QVN4dzNQZXFQTVlGZmh5VkhpS2hJamhDQmVwcWVlRkkzSng1VEZLRWNMYWZTRDRWdTN3VFBpWFBUaHUweGFadFUwM21JSjZLM0g4aFBIeGc?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 11 Nov 2026 22:07:24 GMT
- [Jim Cramer Says Micron Isn’t Going Away. Here’s Why He Picks It Over Sandisk - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiuAFBVV95cUxPTUpQYlZUVFVLYmg4eDYyYS1PdkVqekk3YW44TWlrMHc5WXpjUjlKcGNKaGNMd0F6LTRrekQzN0FpbzFVdy1pNm8zRmU5WV9zUFZhM3RiUmtIRk9NTjlRMnVKdDYwb0RLeDBxODRSV2o1TlU2WjUzR1hHd1d3eFZHUkFiYnlUZHdRRXFnU1JTSFZxcTVhMmxWRUM4dk1MNjhHQU1ZUVpZNC1sQ0F6andudjhIejFDcTVz?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 11 Nov 2026 22:07:00 GMT
- [Micron Stock Surges After CoreWeave's AI Earnings Surprise - Yahoo Finance](https://news.google.com/rss/articles/CBMinwFBVV95cUxQekdVRXpLajdRZVA3aWlYNklNWlhVRTJnOElDTDFHUGI3UVg3UTZkUnp4SnBKTkMyV2tvck9nWVpVR0lVMGpCNHpQQjM1Zjd5TFhVNDdySjN2WFhhbTRQVzlmVWJTUm9UbVQ3ZWR6bC1VQnpxQTBNazVKUlRNZGpmUHIxeGRHWnQxekNoSFM5MVdRUHhkdGNTZ0NCOEJVeHc?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 11 Nov 2026 16:01:54 GMT

## 新興題材：CoreWeave

摘要：新興題材：CoreWeave 相關新聞集中在：Marvell and Intel Rally 7% as CoreWeave's Results Reignite the AI Chip Trade; Taiwan Semiconductor Climbs 4% - 24/7 Wall St.；AMD Rises 4% as CoreWeave’s Raised Outlook Revives the AI Chip Trade - TIKR.com；Micron Stock Surges After CoreWeave's AI Earnings Surprise - Yahoo Finance

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.25 | -16.45% | N/A | 811.30 | 971.00 | -16.45% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.21 | -23.93% | -13.46% | 173.73 | 228.38 | -23.93% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.42 | +7.13% | N/A | 552.90 | 552.90 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.21 | -45.50% | +54.09% | 62.50 | 114.68 | -45.50% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.42 | +17.08% | -5.76% | 977.69 | 2,335.00 | -58.13% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | +0.42 | +12.18% | +5.97% | 2,385.00 | 2,480.00 | -3.83% | 同向 | 86.28 | 27.76 | 586.89B TWD / 59.71% | 2026-11-01 |

關聯理由（前 3）：
- MU：新聞直接提及「Micron」，共 2 篇新聞命中。 方向判斷命中詞：surges。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Marvell and Intel Rally 7% as CoreWeave's Results Reignite the AI Chip Trade; Taiwan Semiconductor Climbs 4% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi4gFBVV95cUxOams4aFViZ0MzZnZKUXdOUEUtcVJ0QzNQTXpLSjExRjctOVdOZnhGZDU2WVlQWFJxMUZYNjFabC0tU1NMekFxT21VdjktUkNFZDZ4WmRFMi11MHY3MllzWXRPV3FhbjZ6dkxDV2RFMEY4XzVfZzdUTVlFcy01WU5PelljOElGb0dmekt0ZmZsbzU1NWJnTVczU0loYVpfNkJYQWUyZ1Y0MnBXaXlqTDN2MFZBME5xZFdVcE1iMGxWbVo3bnY4TkxTVnBMYUNON2FBT1J4YlVQQmg2NnRyZ2pmbU1R?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 11 Nov 2026 14:48:00 GMT
- [AMD Rises 4% as CoreWeave’s Raised Outlook Revives the AI Chip Trade - TIKR.com](https://news.google.com/rss/articles/CBMimAFBVV95cUxNeDVmVlZZWjlVc3djZlFiZ091NmVVR3F1UDlYV3h3N0p6LTdnSFJoZGNFT0RKcEhkMVhURkVzRUVJN2xXTDNRb2hoRVFILUd4RjZQb2pxME15OFpPU1pPdzV5dkl0TF9iZHZIeHRqVTJNUlpCOG1yVzJob1dxbkdKZWxBSmVOOUtHWTJPSVZZVVlUOUtWeFRiNg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 11 Nov 2026 15:10:14 GMT
- [Micron Stock Surges After CoreWeave's AI Earnings Surprise - Yahoo Finance](https://news.google.com/rss/articles/CBMinwFBVV95cUxQekdVRXpLajdRZVA3aWlYNklNWlhVRTJnOElDTDFHUGI3UVg3UTZkUnp4SnBKTkMyV2tvck9nWVpVR0lVMGpCNHpQQjM1Zjd5TFhVNDdySjN2WFhhbTRQVzlmVWJTUm9UbVQ3ZWR6bC1VQnpxQTBNazVKUlRNZGpmUHIxeGRHWnQxekNoSFM5MVdRUHhkdGNTZ0NCOEJVeHc?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 11 Nov 2026 16:01:54 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：國票證券：台股仍可能以震盪方式消化賣壓- 新聞 - MoneyDJ；統一證券：台股高檔震盪，切忌追高- 新聞 - MoneyDJ；受保護的內容: 20261111台股短線信用交易觀察 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [國票證券：台股仍可能以震盪方式消化賣壓- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQQ0V0dExHcW1melRhQVZCUmdRaEJUYUtOWGJvbS04Rnd2aGZKUl9XMFZGS01KMGs4Z3BCOFBtVjZmN2pxVTNRZWhpRDU5MDVCNl9GcHF1NEtNN0VzWmZDYUdsMTQ4cFJib0F4aDNGTW42UmJFTUoyTGpmaHMyLWFnOE45cWRkVVJaQWYzOEtSWWFhQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 12 Nov 2026 00:47:00 GMT
- [統一證券：台股高檔震盪，切忌追高- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNUDFYRnhPY3ZYQTQ4Z1gxZ2J3cTE4YmY2YkhveTNOTUNmYldUQ0drS2E1ckdVbllZZ3RrMjBDRlpxNG11dGtXVk16cDJfY1FhWlVWSzNqem55d0FEajJIQkNXTVJQalpaNEsxbGhJcXZBY1kwd3Q0Z29HUmtiaUpEUVVIdkxJVkpUS21LWG5ad08yUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 12 Nov 2026 00:47:00 GMT
- [受保護的內容: 20261111台股短線信用交易觀察 - MoneyDJ](https://news.google.com/rss/articles/CBMi1gFBVV95cUxNWHNKUEp5R0Q4S0NCY3F2QW41OVdKdzR3WGUyandKcXRuV3pWSEw3UlFtWkcyRlRYUUdlWlkwU3o0RGNJd0o1Y2dkNkgzZzRwVFZOd3FYUUdCbDhoVzdPSUsydUxoY2ZBdEpaN29xU1QyWWJ0VTIyVVQ2UXRzdVBOOG1IM1Fnc1FPN2F4VXlZN2VtWUNwOXN0R014ZG5NaVA5dFM0Z2NwdGNpdm5uYUhUUXM2SVI2aEhxMnJkRWJrc1FUYkFHeWpxT3A4LWtmNzE4QzlwWUJB?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 11 Nov 2026 18:56:07 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
