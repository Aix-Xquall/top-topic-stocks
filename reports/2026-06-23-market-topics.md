# 每日股市熱門話題分析 - 2026-06-23

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜正向｜熱度 12｜市場確認 100.00｜同向 1/1
2. **散熱與液冷供應鏈**｜正向｜熱度 3｜市場確認 76.33｜同向 1/1
3. **利率與成長股估值**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0
4. **半導體與晶片供應鏈**｜中性｜熱度 4｜市場確認 N/A｜同向 0/0
5. **AI 伺服器與資料中心**｜負向｜熱度 12｜市場確認 30.82｜同向 3/6

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.38（樣本 8）
- 5日相關係數：0.01（樣本 8）
- 同向比例：5/8

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 100.00 | 1/1 | 0 | +14.17% | +14.83% |
| 散熱與液冷供應鏈 | 76.33 | 1/1 | 0 | +2.11% | +0.62% |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 30.82 | 3/6 | 3 | -1.40% | -7.11% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：SpaceX | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
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
| 2026-06-21 | -0.01 | 0.32 | +55.56% | 18 |
| 2026-06-22 | -0.87 | -0.87 | +100.00% | 3 |
| 2026-06-23 | 0.38 | 0.01 | +62.50% | 8 |

## 歷史回測摘要

- 回測日期：2026-06-23
- 近5日 3日相關：0.06
- 近5日 5日相關：0.16
- 同向比例：+62.50%
- 權重狀態：未調整

- 方向準確度：+62.50%
- 信心排序準確度：0.06
- 診斷：低相關

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

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Micron Leads AI Trade Higher. Expectations Are Rising Ahead of the Memory Chipmaker's Earnings. - Investopedia；Why Sandisk Stock Soared Today - The Motley Fool；Micron Technology Inc Stock (MU) Opened Up by 5.24% on Jun 22: Facts Behind the Movement - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.65 | N/A | N/A | 1,211.38 | 1,211.38 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.65 | +14.17% | +14.83% | 2,273.73 | 2,273.73 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +4.55% | +17.75% | 208.65 | 211.14 | -1.18% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、MU」，共 4 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 2 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Micron Leads AI Trade Higher. Expectations Are Rising Ahead of the Memory Chipmaker's Earnings. - Investopedia](https://news.google.com/rss/articles/CBMizAFBVV95cUxNV0l4Zi1sQXRYTFlBWU9OMUdDdS1pUERqekhVQ19jZHhhVkJxTTMzdG4xN1VsUm5FdU9sTVpGYlVHSGlHTEFXSjBKNWVBVExHZUVyXzVGN0tXREF2YkhWaFlTWEpzWXhKbGpQaXc4aGJZOGJBbnBDWVNfa2d2cjBQb0k0dHBBVGF4VEVXTEZEdEFnbEcxVVp1Umg5YmxvMnphLUZJRGZXWEVLTy1KWE12SmhzRDJjOUJfUklMZW43SldzbDNkMElMS18yZno?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 22 Jun 2026 15:30:29 GMT
- [Why Sandisk Stock Soared Today - The Motley Fool](https://news.google.com/rss/articles/CBMifkFVX3lxTE0zbkZWam1IT3YxTE9PMHo1MGtqaXpOcVg4OEZvN3A5U0lySGZhM0hWYVRvaUJONkE4VW92NHU3SWRpWVNXSk9sR0JGbFZVUDYzdWdqS21zMUlVWDJBRVpwb2xnLV81TFZIYUlCSWd2UjBXYmp3TjBRVy0xRzcwdw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 22 Jun 2026 16:53:00 GMT
- [Micron Technology Inc Stock (MU) Opened Up by 5.24% on Jun 22: Facts Behind the Movement - TradingKey](https://news.google.com/rss/articles/CBMiiAFBVV95cUxNRXFCTDZ3WXVYVWFwZm94Q1MwaFRmN1JXZjBhc2hieXlLU2tpMktlVjJ4TWl3ZVR5TlZSeFFGb1JCQVF0RE1tVjhNUkhGWmFvQVNWajVPRG4wNm12SmlWMUlxNXJmYUM4WU01bXY0WXgxYThqZVhlM19pRl8yUWQ3andhSVR4TDJB?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 22 Jun 2026 13:48:02 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：〈觀察〉GPU及ASIC需求強勁 健策、奇鋐、雙鴻下半年營運看增 - news.cnyes.com；〈財經週報-台股熱點〉從AI到外太空 散熱族群題材不斷 - 自由時報；《DJ在線》液冷滲透率升，散熱廠從零件走向系統級 | MoneyDJ理財網 - LINE TODAY

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.65 | +2.11% | +0.62% | 2,420.00 | 2,835.00 | -14.64% | 同向 | 61.06 | 39.76 | 15.87B TWD / 60.64% | 2026-06-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐、散熱」，共 3 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：強勁。

### 主要來源

- [〈觀察〉GPU及ASIC需求強勁 健策、奇鋐、雙鴻下半年營運看增 - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTFA3WndjZlctLUxlZ3VPc3N1TGZIS0NnNmxSOEFObi02eXBIRnFfMmZDdHplbEtpRGsxYm9NV0lqN21kT2xuZHZRNFBodVppNGM?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 21 Jun 2026 01:10:02 GMT
- [〈財經週報-台股熱點〉從AI到外太空 散熱族群題材不斷 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTE9rc0xOT3JaSGZPbV9uNjZUNmJLdkctMThER29ldnFaMXp1YlBQajNxaVBBcHlrVEFOOUNLZkxISUt1ZVFOMHF4WXBSd1Jtc0plYWh5bDRrdVk?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 22 Jun 2026 07:52:34 GMT
- [《DJ在線》液冷滲透率升，散熱廠從零件走向系統級 | MoneyDJ理財網 - LINE TODAY](https://news.google.com/rss/articles/CBMiVkFVX3lxTE5RdFhwU093YUp2dExqeUhsOWZDdFhRSkpENjlwTF9nODdMMGsySWJhZzBETTRGQmpZMzlNVkt1U0dWb2x3aTd3dVNhRjRlMmRfMC1JbVVn?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 22 Jun 2026 04:39:30 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：As Anthropic Nears $1 Trillion Valuation, Tech Veterans Warn Against Repeating Intel's Biggest Mistake - 24/7 Wall St.；扛不住通膨與成本壓力，聯發科通知客戶調漲晶片價格 - TechNews 科技新報；花旗調查：經濟學家下調墨西哥2026年通膨預期 作者 Investing.com - Investing.com 香港 - 股市報價& 財經新聞

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 140.94 | 140.94 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2454 聯發科 | 新聞直接提及 | 0.00 | -2.08% | +6.82% | 4,465.00 | 4,465.00 | 0.00% | 不適用 | 62.91 | 71.16 | 47.43B TWD / 4.99% | 2026-06-01 |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | -6.47% | -27.50% | 367.34 | 506.69 | -27.50% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2454：新聞直接提及「聯發科」，共 1 篇新聞命中。
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [As Anthropic Nears $1 Trillion Valuation, Tech Veterans Warn Against Repeating Intel's Biggest Mistake - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi2wFBVV95cUxOXzRrNmVkNURtc0Ewb2R5SmhLZHpDMU5jU0c1d2NocGJlVWwwdVMzRHN0dWdManRCcnlxUXlvRnAtNDdiVnRucWJGU0Y1eHVZVHBWR05ONVZJUjZOZVAweDYwODZhc3o4UXNOZjZpWkxQM05BWHZiZWkzb0RMbkxoVENPMjFnOXBxV01wMzBlZWtWc01YWmg5MVY4OW9WOW1vUXJyYWxwbGlSQVN5ZlNTb0ZNTWF4Z2d3ZU9sZlJmYWVNVDBwMDVPRnBUMWVGNFFqdjh5VkZmN1ZuTGs?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 22 Jun 2026 19:25:44 GMT
- [扛不住通膨與成本壓力，聯發科通知客戶調漲晶片價格 - TechNews 科技新報](https://news.google.com/rss/articles/CBMingFBVV95cUxPWWRKa3RqZnduT0tka2ZrclFQYmxaUjZ5YnVQc3dLUUFzTHRsdkRfV0VmRDVzRnQ3R0IteERZdWNRVm5fR3YxaUI0VGlqWHZSLXJBb2lWcGwzdWp0MWxXOTNqRTJJc3BpaTBZTmR5YlFmR1hBazVIWjkxR3g4Sm1jemZrY2lOZ1dWRE9zdFA2bEw5cXZPTlg0dVppUGExdw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 22 Jun 2026 14:12:29 GMT
- [花旗調查：經濟學家下調墨西哥2026年通膨預期 作者 Investing.com - Investing.com 香港 - 股市報價& 財經新聞](https://news.google.com/rss/articles/CBMicEFVX3lxTE40enZEUDN6LTNSaEF3bklRVkRERXdJeDVYM0RkSHBEODNIb3dReDF3Q1Q0T3NXUUtlZ2lxUVhRWVFHNTRVcTRweDROX1k0OUtHb1FGamRXbGxNV0tETjFSamFHX2NwN0Nyd1hITWdmVEs?oc=5) - Google News source discovery | Investing.com Calendar Mon, 22 Jun 2026 18:24:51 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：AI、半導體投資熱日經收盤首破7.2萬點創新高| 證券 - 中央社 CNA；強茂三箭齊發攻功率半導體新藍海- 日報 - 工商時報；台股再登新高！ 權值股領軍 半導體ETF衝 - 工商時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 140.94 | 140.94 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +4.58% | +8.66% | 2,510.00 | 2,510.00 | 0.00% | 不適用 | 74.39 | 33.75 | 416.98B TWD / 30.09% | 2026-06-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +13.48% | +19.85% | 160.00 | 160.00 | 0.00% | 不適用 | 4.00 | 40.20 | 22.94B TWD / 17.78% | 2026-06-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +4.55% | +17.75% | 208.65 | 211.14 | -1.18% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 551.63 | 551.63 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 1,211.38 | 1,211.38 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | +14.17% | +14.83% | 2,273.73 | 2,273.73 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -6.06% | +22.71% | 392.13 | 446.77 | -12.23% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 CPU, server CPU, x86, foundry；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 0 篇新聞出現相關標籤。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 0 篇新聞出現相關標籤。

### 主要來源

- [AI、半導體投資熱日經收盤首破7.2萬點創新高| 證券 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE5DQTM1LW5Db0Y2ZlVFV0lqVi11OG1Fb1pPVHhBY1pzYnR6UG1BWkdGcWc4NVRybEpudjg2NlVpd3NKTkIyU1VjcGVoWHpSblN3enpHT3hZMzJadnFCbGc?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 22 Jun 2026 07:00:00 GMT
- [強茂三箭齊發攻功率半導體新藍海- 日報 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5nanl5S2ViV2pMMEFXT2xyTU1Wb1FSRVdJRW5TYnU2TWdFYjN1bERCZlhubm5neEczNERabDRVcVNYVGVoYWpmNy1FZHY0S1ZmMlRpTHdxMkpqb3Vlb0tz?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 21 Jun 2026 19:00:00 GMT
- [台股再登新高！ 權值股領軍 半導體ETF衝 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBuV09EZHFfX2RuekVZQnFQdE12d0F0cjh3Ym1IS0luMzFMNW96NnY0dzhLVzEtcjl4aERTbnpNZXdfbUVtWkYtR0liTFFSX1R1bm1ldnNoQ3U2OUlrQkxB?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 22 Jun 2026 19:00:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel vs Qualcomm: Which AI Stock Is The Better Buy - 24/7 Wall St.；Intel and Qualcomm show contrasting AI strategi... | Pluang – Crypto, Stocks, Gold & Funds - Pluang；Intel: Levitating On AI Hype (NASDAQ:INTC) - Seeking Alpha

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.65 | N/A | N/A | 140.94 | 140.94 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | -0.03 | +4.55% | +17.75% | 208.65 | 211.14 | -1.18% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | -0.06 | N/A | N/A | 551.63 | 551.63 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.03 | +4.58% | +8.66% | 2,510.00 | 2,510.00 | 0.00% | 背離 | 74.39 | 33.75 | 416.98B TWD / 30.09% | 2026-06-01 |
| MSFT 微軟 | 產業/供應鏈推估 | -0.04 | -6.47% | -27.50% | 367.34 | 506.69 | -27.50% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -6.06% | +22.71% | 392.13 | 446.77 | -12.23% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.02 | +13.85% | +14.24% | 674.00 | 674.00 | 0.00% | 背離 | 10.86 | 62.58 | 63.03B TWD / 28.57% | 2026-06-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.04 | -2.08% | +6.82% | 4,465.00 | 4,465.00 | 0.00% | 同向 | 62.91 | 71.16 | 47.43B TWD / 4.99% | 2026-06-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel、INTC」，共 3 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel vs Qualcomm: Which AI Stock Is The Better Buy - 24/7 Wall St.](https://news.google.com/rss/articles/CBMimgFBVV95cUxPODlwMnF0eHI1dVlqN2Rwa0NoT1RQRnVWTlJuVDlxV2RJV0lCdFNEc19FdHVyZVB4U3FDM2w0TGpDYXo5ZmlQRFp5Mjg3Zjc4aEMyS3FvNERqVFBYREtBVTdCWHZDa1NhVjVtQ1F0LVdLUzJKRElpOWY4dnp1R0RWaHFzQl9CcEN3MDU4cjVnNGFFYjRVRWNydXZn?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 22 Jun 2026 16:38:12 GMT
- [Intel and Qualcomm show contrasting AI strategi... | Pluang – Crypto, Stocks, Gold & Funds - Pluang](https://news.google.com/rss/articles/CBMihAFBVV95cUxOdW5tRmpKek1ranBscjVheFZVcE53WG9xQ0gxbzkwNGJuZ0tMSDNlckZOQVhlSFZZTVVBazhQQ1RvOC11eXFQbkdoYVRDTnhMaTFxY0p4VGZDTmo4ZEhUZWVabmNZanBROEx3TzNIb0cxSjFGaThEeUI5RzZ2bmNEVkhCT04?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 22 Jun 2026 18:57:20 GMT
- [Intel: Levitating On AI Hype (NASDAQ:INTC) - Seeking Alpha](https://news.google.com/rss/articles/CBMid0FVX3lxTE14MkVSZndTMGxGbmR6X2xlNnBZYktaRDl6VDdGdjk5c2Z1a212RmxndE5tN2FERUFjMEl4MjZ5YjFXMGprSzVvbElHOE4yX3pEck9PelJnajVCaV9OVnRybFhVYU52dVFvbEtJWVhJVVRxSkpkQVU4?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 22 Jun 2026 00:00:00 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股漲1276.31點 - 經濟日報；美伊展開和談　台股早盤上漲千點衝破47000大關 - 經濟日報；AI動能強　台股漲1276點收47741點續創新高 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股漲1276.31點 - 經濟日報](https://news.google.com/rss/articles/CBMiekFVX3lxTE5FSjlqa1NnUFZsem40dnpOeTZwOXUyTE1MRkJOREdyaEJGZmctd3YwcnhwMDN6dU1xMVhTaTZOblFoYVk5SW00eWRmX1ZjWmptZzJaYzY5amlscjlUVzgyMkdxNXE1YU9fcWlHZlFRV3JiZWRfaEpNWE9R0gFfQVVfeXFMTXhGUGd3OGJvRGNwcHV1RFhFZGhGOHpGNFdiOUVORER1MEptQzMtNlZsNmJRYWJ0bGY3Q2JCSnA5Nkx4VEhEdENELWZ3NVBVRnhyZTJpelZVQlhsMVV0Z0E?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 22 Jun 2026 06:21:41 GMT
- [美伊展開和談　台股早盤上漲千點衝破47000大關 - 經濟日報](https://news.google.com/rss/articles/CBMifkFVX3lxTE92ZXRCVGpaOUROXzVtUFRzYjYxR1lfWVBYeF9raFhBMENSZlg3MnlVTURoM1lXYTk2UFNtNlVjd3FqdS14OXotaGpnV2RyMWFiSllpcG1Ec3RndEEyTTlITVdRQm15cktHZ1FRaGtBdGZXeWdXZEl2OWtwbTVoQdIBX0FVX3lxTE5tWVBTSTcwNUttbng4SW9oY3pSWmdpekpMSUpBakFqNkQ5TlJOcWlVR3kyaHNoUnBfcjdhVEJvWFVFOTI4ZkhGcFU3WnZTRWtzZnRWdEZ2WHJIZ2pkOVdJ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 22 Jun 2026 01:31:10 GMT
- [AI動能強　台股漲1276點收47741點續創新高 - 經濟日報](https://news.google.com/rss/articles/CBMic0FVX3lxTE5HcWF6R01TbXZDZGJMZEdwcDZGTnFUeFNkRWZUS1BjYVN2YXJyVlBmZnFqV2g2ZVk0eXJYMWZaZmNUN3RYSkVuR0NOM2FJUEJ0cHlwa0JtQVFybElZeGFvVjY1NDlpWGFFTEZOaFRQUFJmaXPSAV9BVV95cUxOQUZNNnJubk10c3ZpTmxPaE5jOXo3dmpiek9wSW1ILWlubWZqYzBReHg1WXVoVWxKLV8xR2VCQ0dacXcteFlESTFYTE5HOC1DZVJORTRBeTVYSlFUb3NZZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 22 Jun 2026 06:12:30 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：個股動態報導內容-47B8A7D8-78B0-4CAF-A14C-B2DAD9DC9E82 - MoneyDJ；《台股盤後》大漲1276點、首收47K，日K連六紅- 新聞 - MoneyDJ；個股動態報導內容-B47AF358-EC30-490C-8FCB-F690494D5C5F - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-47B8A7D8-78B0-4CAF-A14C-B2DAD9DC9E82 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxOUThNeDRXRVRPNTdHLUp4eXR2UUItVDZndzMxX2FQOE9MaHFSQ2hqQXBLc3JkZ1VNYTNiYUVpM1hRNDY2aXpyVzNaR0dDbUFmNzRsZGZwQjFXS0laa1dheWNsb3hSa3JGUWtndlNUbk9lVHR0eWpZMjZlSHNTOGdXUDRNcVFFc1RjVHVmMThpTVp6VU5O?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 22 Jun 2026 09:11:43 GMT
- [《台股盤後》大漲1276點、首收47K，日K連六紅- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNQkdjZURudDU5Y1prWHdFT1A1aUFzWHFWWWpPS21OZEdvazZYUF9wZDZKdHY5bFhabGwybElSajduNUJRTUZrbENxXzFvYjdoZ2lWdXN4MnZLb011blhydmpHem9IT0xFV2tSUENwTXVtbFhSSl82Zm5qVFF1T2NZcnRzdndPTlZxeGNacWhvOGtGQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 22 Jun 2026 08:10:00 GMT
- [個股動態報導內容-B47AF358-EC30-490C-8FCB-F690494D5C5F - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxONGFfekdtckt1UXU1OVQ5cGVpSk0xdFNPRkNXbDY2SUZzcG1LTUl6MjAzb1pMSHBQdlZsMkdFc2FOQzFsRXNpeWpXek9ZT0ZRYUc0NVFqY1ktTDJVRXhEdUtrMzAzd0h3Qm5SY2xoVlhfWEhtX1FZWXBTWks4WEg4a0JyN2FBWDFQSEpibzRzVzRfcVQ4?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 22 Jun 2026 11:39:49 GMT

## 新興題材：SpaceX

摘要：新興題材：SpaceX 相關新聞集中在：AI startup Reflection signs computing power deal with SpaceX - Reuters；U.S. tech megacaps slide as SpaceX extends slump, AI expense concerns grow - Reuters；SpaceX signs computing power deal with open-source AI startup Reflection worth up to $6.3 billion - CNBC

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [AI startup Reflection signs computing power deal with SpaceX - Reuters](https://news.google.com/rss/articles/CBMiuwFBVV95cUxPdGsyX2NJeEJIdGgtSmVFV3M5OXhyX0tSclVLTlIwUm41SjNKS3RpYWM5QnZnZnNuaTRvcE5tZGZYbzJTSjJmYXBxMXFUUmh6cDlqRkZPYVB5MV9FMjQtUm9XWFg4cW1lX0Qza0Fkb3BUczhjS3hEWFpvTXhJSTVzUVFSdVB3d05jS0xBcWhZaDhONlRRV09kdDlVM3dhY1JWTzhjbW5XYTM0UXdVMUhLMzlYTnpzSmI1bVhJ?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 22 Jun 2026 18:51:43 GMT
- [U.S. tech megacaps slide as SpaceX extends slump, AI expense concerns grow - Reuters](https://news.google.com/rss/articles/CBMixgFBVV95cUxNTEZKNy1oOHpaZnFtM1B6Z0dsLV9aVi1VNEhNZWdibHZhZDhBUDJGb05MTGtsRG1od015d3kxd1A5bGNJaEN5MWdMVlFXR21wWV81M2pYOEtzQlZ2S2hySzZXLWlpWHNYM21leDlXWWFEM2RjdnhrQl92OUM3QWZNamI4c2ZRdUdobVhPMzc2bHZOcUVCUml2cTYzQXNLVHJKYkdickh0OVJ4bk1peXVlVVRzdW1PMWIzLVN2dGxWdm9RTFVjamc?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 22 Jun 2026 17:02:09 GMT
- [SpaceX signs computing power deal with open-source AI startup Reflection worth up to $6.3 billion - CNBC](https://news.google.com/rss/articles/CBMihAFBVV95cUxPSVg2LUhMRlRXMWJGbkUxTXY4VzRCbEJocGxrSVVaNV8yUFhtUC1oTjdNMGgtRU9vVldzbWY5WHBrdGhtXzJidkNsMlVFeDhTa1Bodkl6SHAzeXpZckRVdElpejRzajQyWjBWQzllZ0JNU2FCQlZtY0I3bVczbkxxS2lSemjSAYoBQVVfeXFMT09hVTBfNHBSOUxpVGFUZ0RWcEJXWU55UVZCWElXR3pNVlJhUTg4S0VBRWh4RkMwZHhjZlFsT3RHdEJzTlNtVEVHeDhTemh4YUFLT09xVXA3QTFjYkg3WlpiczRSQlg4d18xNDBXcjI1cDVDRm5YeEJuSWlPOG41QWVLRDI5TDdFbWh3?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 22 Jun 2026 15:00:01 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
