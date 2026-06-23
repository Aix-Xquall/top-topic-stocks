# 每日股市熱門話題分析 - 2026-06-24

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **新興題材：SpaceX**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
2. **利率與成長股估值**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
3. **散熱與液冷供應鏈**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
4. **AI 伺服器與資料中心**｜負向｜熱度 8｜市場確認 21.40｜同向 2/6
5. **半導體與晶片供應鏈**｜負向｜熱度 8｜市場確認 3.57｜同向 1/5

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.38（樣本 12）
- 5日相關係數：-0.11（樣本 12）
- 同向比例：3/12

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 新興題材：SpaceX | N/A | 0/0 | 0 | N/A | N/A |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 21.40 | 2/6 | 3 | -0.64% | -4.03% |
| 半導體與晶片供應鏈 | 3.57 | 1/5 | 2 | -3.48% | -10.00% |
| 記憶體與 HBM 供應鏈 | 0.00 | 0/1 | 0 | -0.25% | +6.84% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價呈負相關；應檢查正負向詞庫，並降低新聞直接提及但股價背離的權重。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
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
| 2026-06-21 | -0.01 | 0.32 | +55.56% | 18 |
| 2026-06-22 | -0.87 | -0.87 | +100.00% | 3 |
| 2026-06-23 | 0.38 | 0.01 | +62.50% | 8 |
| 2026-06-24 | -0.38 | -0.11 | +25.00% | 12 |

## 歷史回測摘要

- 回測日期：2026-06-24
- 近5日 3日相關：0.20
- 近5日 5日相關：0.29
- 同向比例：+75.00%
- 權重狀態：未調整

- 方向準確度：+75.00%
- 信心排序準確度：0.20
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

## 新興題材：SpaceX

摘要：新興題材：SpaceX 相關新聞集中在：SpaceX launches $25 billion notes offering for debt repayment, AI expansion - Reuters；Stocks making the biggest moves midday: Micron Technology, SpaceX, IBM, Flex & more - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 1,051.77 | 1,211.38 | -13.18% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron Technology」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [SpaceX launches $25 billion notes offering for debt repayment, AI expansion - Reuters](https://news.google.com/rss/articles/CBMirgFBVV95cUxPNG9acmpUMFN5LVBLMW1nbUw0X1NmVGNaTzBKcllhUldUTno5ZEpXdk55Q00tbXhCNWJNOUluYzJiWHhUbzNBdWZKeUJlaExVd0x6YVY5MFRCRGN1Y0JIM1VDVHNGTTJWNFk2MUw3N3Nsay1wZlBQNktWSjRXUmN6ZnpiQmJhSVltUzZxSHFMVGZ6OGlVa3R2eEdycXdvV09QQ3RLUXJObXp6UW5MOVE?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 23 Jun 2026 22:40:47 GMT
- [Stocks making the biggest moves midday: Micron Technology, SpaceX, IBM, Flex & more - CNBC](https://news.google.com/rss/articles/CBMilwFBVV95cUxNdnBUWlRFamwxQUFpanJ2SHhjTlNXa2hNLUwyR25PQ2JtVk5xOXlEb2F4UFlOYVBFMTBpajBIM3RDdXpySGVSdnNnV01MTW1HOEFpVEJ4ZWJRa080eC11ZnhWbkNaM0FlY3JOaEhqVjVTSHJFX1JNQ3pPTXNSamlJREZVYWxKYURwQjlVZU5DZzljcnpCUFM0?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 23 Jun 2026 16:32:12 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：扛不住通膨與成本壓力，聯發科通知客戶調漲晶片價格 - TechNews 科技新報；投資人看淡市場前景 兩大指標示警美股估值過高 - Yahoo股市

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2454 聯發科 | 新聞直接提及 | 0.00 | +1.68% | +1.45% | 4,535.00 | 4,535.00 | 0.00% | 不適用 | 62.91 | 72.27 | 47.43B TWD / 4.99% | 2026-06-01 |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | -4.79% | -26.20% | 373.94 | 506.69 | -26.20% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 2454：新聞直接提及「聯發科」，共 1 篇新聞命中。
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [扛不住通膨與成本壓力，聯發科通知客戶調漲晶片價格 - TechNews 科技新報](https://news.google.com/rss/articles/CBMingFBVV95cUxPWWRKa3RqZnduT0tka2ZrclFQYmxaUjZ5YnVQc3dLUUFzTHRsdkRfV0VmRDVzRnQ3R0IteERZdWNRVm5fR3YxaUI0VGlqWHZSLXJBb2lWcGwzdWp0MWxXOTNqRTJJc3BpaTBZTmR5YlFmR1hBazVIWjkxR3g4Sm1jemZrY2lOZ1dWRE9zdFA2bEw5cXZPTlg0dVppUGExdw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 22 Jun 2026 14:12:29 GMT
- [投資人看淡市場前景 兩大指標示警美股估值過高 - Yahoo股市](https://news.google.com/rss/articles/CBMi2AJBVV95cUxPQVBLTHJvVmNlTTVfcGtTc204aldKQmRmTURpSk5YZjE5eGhsek5MNEctNGlhQi1XQzByNEpzZnVSeDV5ZGcycVR0d1B4VUZhbkZnVFp6UzQ2REpCNjE2MzBQSzVrbmNfVVh4cjZDUHVqalpUVnIxS1FsUkY5U04tYVJyRFcyVkV6X0YtbGg1RkFOZjRIaERkWHpjSGZuSFF1dFB4VkczdHB5Xy16SWpuSHdGQ1B5elVjRTJROWFhOXEyN09PYVpvbFducTYyS3MwX214QXRkMjFDYklDRGVoeGwyYkl2c0NYMVJDTzR1d18wSGtSWGoyRVpraTVGOEYyVWwzQlJuQ2ZqczR0RnBSVGdScHpHbHNybEtvUWVZb1lMSnNGdllYMVRYWHBGa2hLRHpjVGZzT1VJYUFULU42QnpOOGNwclRiS2hFS0hEWE41Zlh3cVZUUA?oc=5) - Google News source discovery | Yahoo 奇摩股市 Tue, 23 Jun 2026 20:59:25 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：〈財經週報-台股熱點〉從AI到外太空 散熱族群題材不斷 - 自由時報；《DJ在線》液冷滲透率升，散熱廠從零件走向系統級- 新聞 - MoneyDJ

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | +2.54% | +0.62% | 2,425.00 | 2,835.00 | -14.46% | 不適用 | 61.06 | 39.85 | 15.87B TWD / 60.64% | 2026-06-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 2 篇新聞命中。 同時符合主題標籤：thermal。

### 主要來源

- [〈財經週報-台股熱點〉從AI到外太空 散熱族群題材不斷 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTE9rc0xOT3JaSGZPbV9uNjZUNmJLdkctMThER29ldnFaMXp1YlBQajNxaVBBcHlrVEFOOUNLZkxISUt1ZVFOMHF4WXBSd1Jtc0plYWh5bDRrdVk?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 22 Jun 2026 07:52:34 GMT
- [《DJ在線》液冷滲透率升，散熱廠從零件走向系統級- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNb3dhWmYyRExOd09VcmEtdVRLQlpqTzUwYmpiQTNDdVNWZnZOV1h0SDN6NXY4QXFSQzhtd0NBZ3E5d3NKaXRJZmN6WnhQWUZTRjZNVWpyMUZ5M3E5ZzhRT045NVU0OHVaRi1EeTNZYnhaREUxck9ZY055clJRZnhibjNSYVVjTXN4WTZXRG5OaEtrUQ?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 22 Jun 2026 03:22:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Wall Street Lunch: AI Chip Stocks Sink As Investors Take Profits, Analysts Stay Bullish - Seeking Alpha；AI 結合真人監控，如何顛覆傳統安防市場？ - TechNews 科技新報；頂尖人才爭奪戰白熱化，對 AI 產業的投資佈局有何啟示？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | -0.08 | N/A | N/A | 132.28 | 140.94 | -6.14% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | -0.04 | +0.24% | +12.90% | 200.04 | 211.14 | -5.26% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | -0.06 | N/A | N/A | 519.85 | 551.63 | -5.76% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.03 | +4.40% | +4.84% | 2,490.00 | 2,510.00 | -0.80% | 背離 | 74.39 | 33.48 | 416.98B TWD / 30.09% | 2026-06-01 |
| MSFT 微軟 | 產業/供應鏈推估 | -0.04 | -4.79% | -26.20% | 373.94 | 506.69 | -26.20% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -8.93% | +18.96% | 380.15 | 446.77 | -14.91% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.02 | +11.26% | +12.20% | 662.00 | 674.00 | -1.78% | 背離 | 10.86 | 61.47 | 63.03B TWD / 28.57% | 2026-06-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.02 | +1.68% | +1.45% | 4,535.00 | 4,535.00 | 0.00% | 背離 | 62.91 | 72.27 | 47.43B TWD / 4.99% | 2026-06-01 |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：lower。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：lower。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：lower。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Wall Street Lunch: AI Chip Stocks Sink As Investors Take Profits, Analysts Stay Bullish - Seeking Alpha](https://news.google.com/rss/articles/CBMixAFBVV95cUxPZjFYVVppY1JGUXAyOVpNMmFEOHZsWWdVcHNpMGlaMi15cURfTkYzV1ZMYWNXdm5oQW1LeWxzaXhmclpLWEdFbEloMHZSeFVLUHFnSHFkN3RFQ05KMlBXZjRYOF9PaEtqUDVCbjlHOUVLTFhkS0VEYVZWWWJzLTJZLURBWkhfUXNvVnlNUXFPeWRqdDR4VTA1V0tZV0o4eDZrMEV5ZmhXTi1sRVdidFZzSmd2RDYxbDBUUVBBQk9FbWNyRlIx?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 23 Jun 2026 16:24:29 GMT
- [AI 結合真人監控，如何顛覆傳統安防市場？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMibkFVX3lxTE5xZ3JaQ3laM0t3bU1FZ2Ffd21pMGYzelJ2Yi1pTnlMOEFZSmpCZmwySzRjMWVNRmxLdzhDdXRqeUdyVTBPV0c1cHVNdGc2dXdUV0htckU2ZEE3UXVwbWoxYjUwSlI1UEZEb3hpeVBB?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 23 Jun 2026 15:34:14 GMT
- [頂尖人才爭奪戰白熱化，對 AI 產業的投資佈局有何啟示？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMixgFBVV95cUxNQWxTaUdGUnBYd2hHYzBpQjlDcERkMkZTNks2YW1va3UtZUZlcU9UdTYtdjFqRHp3YUF0Z09vZ1FjSnAwbEE0OVdYd1J3Q3FaYV9PeVFJVExGVHdtNjM0ZnlMNWs4RjQ4dF84WEdabVZHTEJhLWVWZW5tcUMxUFdjbnVvY1hmbDRlVUlYcEdsRWp2MVJBamozNW54ZmZ5UzlmOE10MHNCMVRIYUhCZFowUGdGdEdkV0RDaHNIQjRGSllQVGlMSGc?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 23 Jun 2026 10:47:42 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：AMD and Intel Drop 5%, NVIDIA Slips 3% Amid Korean-Led Chip Selloff Bulls Say Is "Healthy" - 24/7 Wall St.；Wall Street Lunch: AI Chip Stocks Sink As Investors Take Profits, Analysts Stay Bullish - Seeking Alpha；Intel (INTC) And UMC Team Up On 12nm And 3nm Chip Development - simplywall.st

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.65 | N/A | N/A | 132.28 | 140.94 | -6.14% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2303 聯電 | 新聞直接提及 | -0.29 | +21.43% | +20.14% | 170.00 | 170.00 | 0.00% | 背離 | 4.00 | 42.71 | 22.94B TWD / 17.78% | 2026-06-01 |
| NVDA 輝達 | 新聞直接提及 | -0.43 | +0.24% | +12.90% | 200.04 | 211.14 | -5.26% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.57 | N/A | N/A | 519.85 | 551.63 | -5.76% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.03 | +4.40% | +4.84% | 2,490.00 | 2,510.00 | -0.80% | 背離 | 74.39 | 33.48 | 416.98B TWD / 30.09% | 2026-06-01 |
| MU 美光 | 產業/供應鏈推估 | -0.04 | N/A | N/A | 1,051.77 | 1,211.38 | -13.18% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | -0.03 | +0.25% | -6.84% | 1,963.60 | 2,273.73 | -13.64% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -8.93% | +18.96% | 380.15 | 446.77 | -14.91% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel、INTC」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2303：新聞直接提及「UMC」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, foundry, chip。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AMD and Intel Drop 5%, NVIDIA Slips 3% Amid Korean-Led Chip Selloff Bulls Say Is "Healthy" - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiyAFBVV95cUxQTDFLYWd5N0tVem80V1M2aGN2dTZMOS02OVpuV1ZrR1VSYnUwR3R1NlBtQWNjUWp1WE5hampyMWlUZ0k0WXR6MHJ3Nk1Jb1dTRGRwY2JsTFUxVEl0Xy1sOFlpOFlpV21lcWJTcWFWeHVfVVpZRzdESndzTVhHVXBFbEZxRnprQlF0TnVqaFZDaVIzSmN2Tkg5LTlRajZDM1JSSE0wMHVtLWZXcVEyYnVJcktHQTRzbHpUbF9yM1RVRUM4eGpIRnplSg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 23 Jun 2026 17:23:22 GMT
- [Wall Street Lunch: AI Chip Stocks Sink As Investors Take Profits, Analysts Stay Bullish - Seeking Alpha](https://news.google.com/rss/articles/CBMixAFBVV95cUxPZjFYVVppY1JGUXAyOVpNMmFEOHZsWWdVcHNpMGlaMi15cURfTkYzV1ZMYWNXdm5oQW1LeWxzaXhmclpLWEdFbEloMHZSeFVLUHFnSHFkN3RFQ05KMlBXZjRYOF9PaEtqUDVCbjlHOUVLTFhkS0VEYVZWWWJzLTJZLURBWkhfUXNvVnlNUXFPeWRqdDR4VTA1V0tZV0o4eDZrMEV5ZmhXTi1sRVdidFZzSmd2RDYxbDBUUVBBQk9FbWNyRlIx?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 23 Jun 2026 16:24:29 GMT
- [Intel (INTC) And UMC Team Up On 12nm And 3nm Chip Development - simplywall.st](https://news.google.com/rss/articles/CBMiyAFBVV95cUxQOUJmRXNuVjF6OEIyNDlneTlqa1R5QUxmZGhSV0xRbVlkRG40RE53VzBIcVFzcV9vMk1oZllhTFdmY3RsWWFUZm9RSXdZMGlPTVh5ek9BS3JFWGNtVEhOZ3JnSXdZYzkyYUY2MDRQU0RTWFlmazY2cFItMl9BbjYtckpDcnotRUxnZm9sa2w1V2s2OS1UdnVObm45M0pfLXp4azZ6QjBEa2hmYW1ZUjZlOGtsYncxZnQyVDFzNk9FdVJnVk9nVUpBQdIBzgFBVV95cUxObEtFbTVrSm4ycFI5a3NpYk5JeVl1Z3hSRUFCOUh3V3RUUzRGbzhPMndhM0xoOTR4cTBwUEJCazE4VUdWWXdkLS1rdjBZMEZETEJhSG1oMzdvcDFycVB3NkU3d2tXbFlLbmkzYUwxZnBUSGwySjRaN1dDLTRqUTFBLU04WEg2Uk9JM2lxYXNSbkl1YmptX21KamZkY3h1SzlGeWoyZXNWTzl5MXRPbjJiVklBSzlhMHhERHhiTGxxbmRIQWIzRFZRVGJPb1Fpdw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 23 Jun 2026 13:44:18 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：台股創高後震盪翻黑收跌640點 記憶體股賣壓沉重 - 經濟日報；Micron Leads AI Trade Higher. Expectations Are Rising Ahead of the Memory Chipmaker's Earnings. - Investopedia；Buy, Sell, or Hold: SanDisk at $2,184 and Micron at $1,134 - 24/7 Wall St.

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | -0.65 | N/A | N/A | 1,051.77 | 1,211.38 | -13.18% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.49 | +0.25% | -6.84% | 1,963.60 | 2,273.73 | -13.64% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +0.24% | +12.90% | 200.04 | 211.14 | -5.26% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron」，共 3 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：lower。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [台股創高後震盪翻黑收跌640點 記憶體股賣壓沉重 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBzNTQtdGhXbjJDdlA0eFNMVGJrdVQ1bGMzdWllWDVMRWU4OFctVTdTNnVwUDkwZjdMZDFEUTJtUGdSdjlqTFhzZ0V4d1BCZ2ZHSmZDNV90S1hWd9IBX0FVX3lxTE9OcFlhek9zcFVqc3A2LVotNVQ3d2c4M18ydWFLdTA5NV94N0piSUI1S2RGNDdRSWczVnJPV2lualk0d0RNVHZqcnhlaVBOVDNHODdvQVI1RFdUTFdlamcw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 23 Jun 2026 06:54:29 GMT
- [Micron Leads AI Trade Higher. Expectations Are Rising Ahead of the Memory Chipmaker's Earnings. - Investopedia](https://news.google.com/rss/articles/CBMizAFBVV95cUxNV0l4Zi1sQXRYTFlBWU9OMUdDdS1pUERqekhVQ19jZHhhVkJxTTMzdG4xN1VsUm5FdU9sTVpGYlVHSGlHTEFXSjBKNWVBVExHZUVyXzVGN0tXREF2YkhWaFlTWEpzWXhKbGpQaXc4aGJZOGJBbnBDWVNfa2d2cjBQb0k0dHBBVGF4VEVXTEZEdEFnbEcxVVp1Umg5YmxvMnphLUZJRGZXWEVLTy1KWE12SmhzRDJjOUJfUklMZW43SldzbDNkMElMS18yZno?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 22 Jun 2026 15:30:29 GMT
- [Buy, Sell, or Hold: SanDisk at $2,184 and Micron at $1,134 - 24/7 Wall St.](https://news.google.com/rss/articles/CBMimwFBVV95cUxPc29Vb3Z6b2hibTRvYmJqQ1NXUUZfNW9Pam5mejVWZEpMMzJJdGUyMXBzRjdzdVcyZFN1aXJ6UWhDcmhZTGlmZnRCMnltYXpMVjVIUTNtMjBlVUdPbDIwUFI5eS05LVFLX3NpR1NMLWRxeUlZUFBPQnNKX2RFdVc1clBncEI4VE1SdHEyTjFlZW5NdW8zLXRkX2tMQQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 23 Jun 2026 14:27:42 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：個股動態報導內容-FCAA7E36-A9B3-4610-8FBB-507372F75F42 - 5850web.moneydj.com；光寶科、康舒 認購熱 | 權證特區 | 證券 - 經濟日報；台股狂震千餘點 專家：基本面護持 換手再攻 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-FCAA7E36-A9B3-4610-8FBB-507372F75F42 - 5850web.moneydj.com](https://news.google.com/rss/articles/CBMikgFBVV95cUxPWXUxLW9YOGtVSEJfRlJvV2dQcHVrZ2VSOGpJbzFxRENOWXBESXVUbl9DN3RXeFh0Vm43VW94MTI3NGZLUW9aNjZhb2xJZ0xrR3JoM0t3eXRwQjYySUlnNU9uMTFUVjZHOWJ3LXk4b09hWnNWd0szOVJuOWwyTUg1c282eFBjUmV4NnJFRFZqa3BPdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 23 Jun 2026 19:30:33 GMT
- [光寶科、康舒 認購熱 | 權證特區 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1pVFNkNV9uUzJrTG9NRDQzNDFXYXUtWnl5VUFPUU1ZeVM2TkpraFJmNmlwR1ZYbE5mMzBVaVZhZElsbkVUM3FYQ3JWS1UydkN3em40SXlnNXRRUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 22 Jun 2026 17:22:38 GMT
- [台股狂震千餘點 專家：基本面護持 換手再攻 - 經濟日報](https://news.google.com/rss/articles/CBMif0FVX3lxTFA1VDNidUFUOEV1VjYxZ2tiZ29xdVJwNFBuOTFqLUNtYUlxcDAzY2lKbXZseDJnM1o2RUVLcHBlcTdoTlp5eF9odUZuQVlINmU2Mld5d0gwS2I5cEJBdUk0MEM0Qm4wYTRwejhTdHhFS2tNLTdDRUNqRmYtTWNLTVXSAV9BVV95cUxQeWltNXdIdjBla09HODFjQVlHWEVjN2xad1VpeFJVZ1FDVXdHbXVaSHFDLTlYM2FreFdTZUFKN0dyVUZ1SU9QMDRKSG4yNVpBaTZDZHVraExxMHhUZUFVMA?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 23 Jun 2026 17:17:14 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》收跌640點、日K翻黑，5日線有守- 新聞 - MoneyDJ；台股ETF受益人周減近9萬，風向見轉進高息- 新聞 - MoneyDJ；個股動態報導內容-2717E2CE-2C44-4124-AE28-1086DCE59BF1 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》收跌640點、日K翻黑，5日線有守- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxOdW9zMURZczlHLS0xalJpMFZ4ZkRoRm1EbDlEbXY1NWpLYXZUR0tUNC1odDF0VUhwOWVpNmIzcVFheEpvcTBKU0UyeHExVlpqcUFZcnVrb2ZOM2REYXFZdEVLV1RyS1pybHRKUkhEQ28zM0trVllsUlhLTENjeUZ6UzlrWDlYQlgyZXBNWUlPVElXZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 23 Jun 2026 08:05:00 GMT
- [台股ETF受益人周減近9萬，風向見轉進高息- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxONkxNYXg4ZlZPUS1IWFJvQjNIZjBfRERCWFdSYVJGeHQwYllzbjZGTHU0MnF3TWpDZ3AtaU9rWmNSbUFXMFRCQ2NFUXVha3F6alJHdVBuRWMxcnNCeVJvdEtMTHdPWDFGQ2pMMmprcHZEaGdnUFd1eUJuaUt5RGRFdl9ja195RFNLaUk2dTY3Q0l3QQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 23 Jun 2026 05:50:00 GMT
- [個股動態報導內容-2717E2CE-2C44-4124-AE28-1086DCE59BF1 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxPMzE5NDdjdV9uZGVpZGFJMzRiSEhTR0w4UWJnZzVZZi11ZlI3TkhTMXBpSzk4RWI0dC1IWlE1NTVnZE8xVjFILUZvbDhjTWhIRGxaNi0yMzZoN1l6cW15SEtJM0NlRjJhMmJjQV9WZXEzbmRnSlNUWGFDZnBMWlk3RWFiSkdhN1J6SFB0Vk9nVkN4bVNu?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 23 Jun 2026 11:36:57 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
