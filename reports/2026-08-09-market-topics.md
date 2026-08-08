# 每日股市熱門話題分析 - 2026-08-09

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **AI 伺服器與資料中心**｜正向｜熱度 14｜市場確認 88.33｜同向 5/6
2. **新興題材：TradingKey**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
3. **利率與成長股估值**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
4. **半導體與晶片供應鏈**｜中性｜熱度 4｜市場確認 N/A｜同向 0/0
5. **記憶體與 HBM 供應鏈**｜正向｜熱度 7｜市場確認 0.00｜同向 0/1

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.39（樣本 7）
- 5日相關係數：0.46（樣本 7）
- 同向比例：5/7

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| AI 伺服器與資料中心 | 88.33 | 5/6 | 0 | +12.21% | +8.58% |
| 新興題材：TradingKey | N/A | 0/0 | 0 | N/A | N/A |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 記憶體與 HBM 供應鏈 | 0.00 | 0/1 | 1 | -15.09% | -0.22% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：群聯7月營收 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-07-27 | 0.54 | 0.11 | +37.50% | 8 |
| 2026-07-28 | 0.32 | 0.13 | +36.36% | 11 |
| 2026-07-29 | 0.16 | -0.03 | +92.31% | 13 |
| 2026-07-30 | 0.25 | 0.92 | +66.67% | 6 |
| 2026-07-31 | 0.10 | -0.10 | +46.15% | 13 |
| 2026-08-01 | 0.38 | 0.25 | +54.55% | 11 |
| 2026-08-02 | 0.06 | -0.21 | +33.33% | 9 |
| 2026-08-03 | 0.35 | -0.49 | +60.00% | 5 |
| 2026-08-04 | 0.05 | -0.08 | +46.15% | 13 |
| 2026-08-05 | -0.39 | 0.44 | +64.29% | 14 |
| 2026-08-06 | 0.07 | 0.33 | +50.00% | 12 |
| 2026-08-07 | -0.22 | -0.17 | +50.00% | 8 |
| 2026-08-08 | 0.72 | 0.45 | +62.50% | 16 |
| 2026-08-09 | -0.39 | 0.46 | +71.43% | 7 |

## 歷史回測摘要

- 回測日期：2026-08-09
- 近5日 3日相關：0.48
- 近5日 5日相關：0.04
- 同向比例：+25.00%
- 權重狀態：未調整

- 方向準確度：+25.00%
- 信心排序準確度：0.48
- 診斷：正相關

調整原因：近 5 日有效樣本 12 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：AI 伺服器與資料中心 相關新聞集中在：Chip Stocks Find Buyers After Earnings Shock Shakes Out AI Trade - Benzinga；AI 翻譯如何加速漫畫全球同步發行效率？ - TechNews 科技新報；五大資料中心簽長約，對 AI 產業影響？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AAPL 蘋果 | 新聞直接提及 | +0.42 | +18.60% | +34.97% | 313.33 | 313.33 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 產業/供應鏈推估 | +0.08 | N/A | N/A | 101.65 | 114.68 | -11.36% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.06 | +11.93% | +12.22% | 223.96 | 223.96 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.06 | N/A | N/A | 483.36 | 516.10 | -6.34% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.06 | +2.16% | -2.27% | 2,370.00 | 2,425.00 | -2.27% | 同向 | 74.39 | 31.86 | 442.68B TWD / 67.87% | 2026-07-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | +27.31% | -1.32% | 499.99 | 506.69 | -1.32% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.04 | +13.24% | +2.47% | 427.76 | 446.77 | -4.25% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.03 | 0.00% | +5.41% | 585.00 | 680.00 | -13.97% | 未明確 | 10.86 | 54.32 | 65.78B TWD / 32.86% | 2026-07-01 |

關聯理由（前 3）：
- AAPL：新聞直接提及「Apple」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Chip Stocks Find Buyers After Earnings Shock Shakes Out AI Trade - Benzinga](https://news.google.com/rss/articles/CBMiuAFBVV95cUxPS1FTWlZCYm5qU3NkcC1zM21JUmZ4XzdXbl9KYVd3bFM1Zm0yeGRSN1o3TXFoMS1IbjJpNzY4Y2Jrd01fT2hyemhEaThnZUJya05WbkVHR0hnNkY4OGhNcnFoREJJRUxkZ2JHRzNmRnAydnFHR3gydnNxbzhTRmM4c19Nc2s4TGpITFdVb05ZR1k1RlFWR0Y4OTFRc2FHbmtkUXFES1U5VndBbUJBdll4dlV6c3JBMWtJ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 07 Aug 2026 14:26:14 GMT
- [AI 翻譯如何加速漫畫全球同步發行效率？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMib0FVX3lxTE1kMFMyVUwzUmQwR0lIdkJiUTV0RjU5bmxxaGJxclo3dzlnNlZGekdjeGk0ZzNYNEFpa2VHbGtvRHRWNUVfendXSWFMLURtd2NCaTc1SnVZTDdlZ3Q0Qk9XMUFTWWlOYldiSkZzTW1ZQQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 08 Aug 2026 17:17:34 GMT
- [五大資料中心簽長約，對 AI 產業影響？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMi3gFBVV95cUxPSGFLdFJCTFVseGl0OHJrUm1Bd251cldtTXVSSmtyRjVpbXVPX1N5RnlvSFFXSDdHdXBFcmhoWEJ2bThuaEpXbmEyRlhzQ3JVU19aVmgyeGxaZnIzQUg0ZEprZU1zV2F1LWstbGY4b2JaYXYycVgxdkxmQmQ2SVBSSFdLS29XY3libWVLako5UTdvb0VUdW5Ka0FfR3hTLXluMEJjZUZybDNvbXNoX3JIelV2anBLdzRzRU1JNFdqRDV1SWlFb2NncEIxbi16Y3VEX25RVWNsejFDT0F0eHc?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 08 Aug 2026 12:43:52 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Intel Smashes Q1 2026 Earnings and Breaks Its 2000 All-Time High - Is INTC Still Buyable at $82? - TradingKey；Memory Giant SK Hynix Nears US Listing: Some Key Information You Need to Know - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 101.65 | 114.68 | -11.36% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 877.57 | 971.00 | -9.62% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MU：新聞直接提及「memory」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Smashes Q1 2026 Earnings and Breaks Its 2000 All-Time High - Is INTC Still Buyable at $82? - TradingKey](https://news.google.com/rss/articles/CBMiuwFBVV95cUxOSkdkV2l0bEpsUDdzR0txTUdqdzMxWGdiTk56dzE0bWg3bEIzNXZVdVAwNnJzSnhJTnEzNmZUaC1wdEhKc01tNmt2bG4yRk05QklHVEx4Q1JVWTNRQ0RmU0N3UnctdDZmazVrMFNxUlhYZFpwMUxzWWx0N1NkSW9oSDVHQmx4Z0xhOXB4SlpKem1lOC1tX1NHcjJEa3lnb0t0Y0tPYmlaTWpBMDIxSU41cm9iOXdEeU8tS29z?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 08 Aug 2026 04:25:39 GMT
- [Memory Giant SK Hynix Nears US Listing: Some Key Information You Need to Know - TradingKey](https://news.google.com/rss/articles/CBMisgFBVV95cUxNY3h5Smd3UUktRzdfMXRISlplRm1CNG52TkJPSjRNSG43RGsxZHJENXlnaXFscVJNeXRORDFyenkyQ3pXZmM0SDU5VzEtX1gycFpwMHZ2d0RWeldvSzRUZGE4VUZfMGNzUDJkTkZUb0hHSkUtV2ZXeHdJTW56ZnJUUXJkMlZPYndOQ3piNlQ5RVY2UnpUWEZyM1l6NTFVODB5VURSbnFIYlU1bmdTTmJ5QVB3?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 08 Aug 2026 05:36:18 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：Wall St Week Ahead: Inflation data to test record-setting US stocks, Fed rate views - Reuters；台股關禁閉規定鬆綁、緯創法說、7月CPI連三月衝破通膨警戒線 本周大事回顧 - news.cnyes.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +27.31% | -1.32% | 499.99 | 506.69 | -1.32% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Wall St Week Ahead: Inflation data to test record-setting US stocks, Fed rate views - Reuters](https://news.google.com/rss/articles/CBMiwAFBVV95cUxNT2tydC12dWhpUnJJXzhSQXpxNFR2S2VQamVXcTAwMms4YWNSZnVwSnJEeEtMMi1WZW1EQkc2dzJwSEt0V0hBc3N1VUxHODRfZkhodk5teVg0NHBGS2xBNHVTczA2U1NvTE4xR1Y0dlVDVE5mOWpqbnIzczZiZ1drb3d5V3VWX0xOLUgwakItMF9jTXZzR3hhNWZjRXlnaklZcFg4MDZzOGtZd2RaZkhsT1laaXpST3NUR2JtVFlCNEo?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 07 Aug 2026 10:02:00 GMT
- [台股關禁閉規定鬆綁、緯創法說、7月CPI連三月衝破通膨警戒線 本周大事回顧 - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTFBiaklTdUtoOEdjX09vdjlWbUFXSUVsQWZpRF9BYWRPM1gtOXdDUTRQYXo1MEdRQTROcUgzYnJ3YzdkQ0FERmphMUczWGRSMDQ?oc=5) - Google News source discovery | 鉅亨網 Sat, 08 Aug 2026 01:46:51 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Chip Stocks Find Buyers After Earnings Shock Shakes Out AI Trade - Benzinga；What Does Intel (INTC) Gain From Its Texas Chip Facility Joint Venture? - Yahoo Finance UK；因應半導體展台灣高鐵推彩繪列車| 生活 - cna.com.tw

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 101.65 | 114.68 | -11.36% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +2.16% | -2.27% | 2,370.00 | 2,425.00 | -2.27% | 不適用 | 74.39 | 31.86 | 442.68B TWD / 67.87% | 2026-07-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | -2.11% | -4.13% | 116.00 | 164.50 | -29.48% | 不適用 | 6.68 | 17.44 | 23.84B TWD / 18.98% | 2026-08-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +11.93% | +12.22% | 223.96 | 223.96 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 483.36 | 516.10 | -6.34% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 877.57 | 971.00 | -9.62% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -15.09% | -0.22% | 1,212.21 | 2,335.00 | -48.09% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | +13.24% | +2.47% | 427.76 | 446.77 | -4.25% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 2 篇新聞出現相關標籤。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 2 篇新聞出現相關標籤。

### 主要來源

- [Chip Stocks Find Buyers After Earnings Shock Shakes Out AI Trade - Benzinga](https://news.google.com/rss/articles/CBMiuAFBVV95cUxPS1FTWlZCYm5qU3NkcC1zM21JUmZ4XzdXbl9KYVd3bFM1Zm0yeGRSN1o3TXFoMS1IbjJpNzY4Y2Jrd01fT2hyemhEaThnZUJya05WbkVHR0hnNkY4OGhNcnFoREJJRUxkZ2JHRzNmRnAydnFHR3gydnNxbzhTRmM4c19Nc2s4TGpITFdVb05ZR1k1RlFWR0Y4OTFRc2FHbmtkUXFES1U5VndBbUJBdll4dlV6c3JBMWtJ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 07 Aug 2026 14:26:14 GMT
- [What Does Intel (INTC) Gain From Its Texas Chip Facility Joint Venture? - Yahoo Finance UK](https://news.google.com/rss/articles/CBMigAFBVV95cUxPV21pM2pUN2pfYUpPdlNRMEZPbXM1SG81Y3ZFWlF0X1FPcFgwa0Z1QnRHRmNsMVpiN0lyalVrRlpMYklPWUJtVU4tWnVuX0otSFJKcEN4elJ1RDc1TVV6c3NzeTVYM3ZsM3p0UHlrb2I2YXNqMmY4WUZDV1VzcWRGRg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 08 Aug 2026 02:11:00 GMT
- [因應半導體展台灣高鐵推彩繪列車| 生活 - cna.com.tw](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1MVTdMbzBYSXJLMVN2aWZiem5nVzllSzAtNTJfNTlhSW1lRHBsQnR3TmxzV09SekVFclhERTJhRmNCb0RfUE1UY1U0NGh3UGp0LWRoZTFPSmJlUHdZVVBV?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 07 Aug 2026 07:54:00 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：MU, INTC, SNDK: Chip Stocks Rally After-Hours On AMD’s Blowout Report - Stocktwits；Micron vs. Sandisk: Which Is the Better AI Memory Stock to Own for the Next 3 Years? - finance.yahoo.com；Micron vs. Sandisk: Which AI Memory Stock Has the Edge for the Next 3 Years? - finance.biggo.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.48 | N/A | N/A | 877.57 | 971.00 | -9.62% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.24 | -15.09% | -0.22% | 1,212.21 | 2,335.00 | -48.09% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.36 | N/A | N/A | 483.36 | 516.10 | -6.34% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.36 | N/A | N/A | 101.65 | 114.68 | -11.36% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +11.93% | +12.22% | 223.96 | 223.96 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron、memory」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK、SanDisk」，共 4 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [MU, INTC, SNDK: Chip Stocks Rally After-Hours On AMD’s Blowout Report - Stocktwits](https://news.google.com/rss/articles/CBMiygFBVV95cUxPeVlYaXJjQjNtTkNRQUxQTHhaLUFMbE80Uy1MeDBpV0FPdkg2SHRLdkdfVUpXM1NrNWhZSVZQQ01sa0o4T1hKdzF1clBFRlRWUmMwWGxQTDNVVFBpOVhObUc2MXpBeXBOZ0p3R0w5NGRNOHB4X0ZIXzhlT0NMbmhzc1RtdmJRTWhlRUhKSHpyVnpaU0VGMlJyU2tDcmdkTG1hWVJJbmtTVDREbzFfWDB4bjhuTGswN3lmdkdHQzY1dzFOVU41VGlBNlZn?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 07 Aug 2026 02:47:27 GMT
- [Micron vs. Sandisk: Which Is the Better AI Memory Stock to Own for the Next 3 Years? - finance.yahoo.com](https://news.google.com/rss/articles/CBMilwFBVV95cUxPRjB5bW1rVlFkZ0Mtbml0N3hDdTVLc0lOMm1LbVZGZWo3WXB6V3lFcm12aXNadDRQLWVjM1pqZnBwS1IxQTJPOW01TG15SU1kdldUaHhBQ1VmSzZhbkZNVlVpNm1XQWRzMXFwdlBaVUdLNkp2Nl9oaDhQRGU1TWFtZ1BpRmpuZEx6eHYxVHJvNl9zbFd0VGhN?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 08 Aug 2026 10:03:00 GMT
- [Micron vs. Sandisk: Which AI Memory Stock Has the Edge for the Next 3 Years? - finance.biggo.com](https://news.google.com/rss/articles/CBMidkFVX3lxTE9tS0k0Q3AyQ2xDU0I5SW42cFZFZlhPYzgyeUFYNWRzdkZPa29ZTW5adXBVMVVnWTczMFlobFBBN2RrV05UcTBEempqWUtSZjBRNUVJdGE2akh6OXdBNzJ6bUw2T3hPa2pzc0QxTWlnWEMwRlVDbHc?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 08 Aug 2026 18:09:00 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：凱基-長庚 對 泰鼎-KY(4927)個股 單一券商歷史明細 - justdata.moneydj.com；台新-五權西 對 台肥(1722)個股 單一券商歷史明細 - justdata.moneydj.com；8月台股 ETF 配息一次看 00878、00929、00891等配息飆新高 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [凱基-長庚 對 泰鼎-KY(4927)個股 單一券商歷史明細 - justdata.moneydj.com](https://news.google.com/rss/articles/CBMiiwFBVV95cUxQcldhaEloanVTYUNSMjBPU3lxdGtMbElsYUY1UmxYckh2Mm5aTWxUZFZLeGlqREtCbUpfV0NEMVFZTWZiTE8wbG1aUlJuMjVabG1VN0F0NXdTWWJyd0lKVjQ1ck1NNjVEa2FVSG9OLTVxZE0zTF8teWpIYzVxSzM1ZmdSUTRManhVNGRz?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 08 Aug 2026 02:59:26 GMT
- [台新-五權西 對 台肥(1722)個股 單一券商歷史明細 - justdata.moneydj.com](https://news.google.com/rss/articles/CBMilgFBVV95cUxQaW5LS1ExaUxKeC14dUx2SmxWNGZyZ3AyZ0pmT3dPbmRhQU8tOTNnVkIxSERQTzZwZ2taaWxPUU4yTk1kbEVsQ2pHbVBCZTB5ZkROVFV4ekFqSlZQSTRYYWxLRVpIaXF2UHRqVEFxRzNxbVdSY29zR3Z1WVBxNXMwa0FsV1dGdzdMUExXZU44aHdJNE9HZlE?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 07 Aug 2026 21:03:59 GMT
- [8月台股 ETF 配息一次看 00878、00929、00891等配息飆新高 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1uaUFsaXgyRUh3aUI1OWVDQV81WEpVMjg0dFUtQmFOdkpidnNXdDY5SHhpM1p2RTM3OWl5QjQ2d21hdHEwWl9saGg3QTZETF80WjBabWZWcm1DQdIBX0FVX3lxTE9TcnRVa0psdHE1dHlNQTZyN0xyRTEzZGMzRHRyblp4Qk1Hb0dwTDhEYTNod3AtZ1Ytb3lKdERwLUNwRHNzeGdyLUtWSU8tTWpOc1JybHdPbW1qWXhuLTRN?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 07 Aug 2026 09:00:00 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：個股動態報導內容-D126FC45-5DB0-4191-92F6-62544C7D65DC - MoneyDJ；個股動態報導內容-371CD490-6AE4-4D9E-B4E8-3A9D5B90F162 - MoneyDJ；個股動態報導內容-4E4B89DD-BEDD-4E5B-A642-6F5B871AC261 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-D126FC45-5DB0-4191-92F6-62544C7D65DC - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxORF94amxFY3VzdlI2dWkyMUxkWWtIWmJ4OWR6Z0NrZmFkRU1tck03Z1AyMjdoYlhtakJtdkVybWlXZXIxU0RZTV9ZWDF5N0wyNFRDTkhDZ1ZCNGUtaXdhVjVPc2txTGk2SVRPcktJUEhCSUpNZFViSV9WU1VjdG1IcmlyazBsWmJJem9LRjZZMFVtaUhi?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 08 Aug 2026 17:06:23 GMT
- [個股動態報導內容-371CD490-6AE4-4D9E-B4E8-3A9D5B90F162 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxOLUdEX0Frc3dkZHhxM3B6Nzd4Z0tSMlFtMjhuTGxMYjkwOHF3RGNQUFhSRi1kdkFPZXVOaHBxYVo3UTlRZkZwTXdiM0dDX0l5YWJtd3ZTTXNnNU84cUVHWUVBajBFM012VjVLeVJtWkpYVmV1aEV2Sk93ZDZuSkFsc19rZHg3eTByN050dzduWThnTDFM?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 07 Aug 2026 20:47:29 GMT
- [個股動態報導內容-4E4B89DD-BEDD-4E5B-A642-6F5B871AC261 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxQam5nQ003bmxlMUdrdVptdWtDNDJuMXRUSWdYSTBVci03bzZCNi12bWhfRXZlZFZZU2RwV1BiUjNWMWRTRWRHd0ExLVRSX0hxUndYT21IMnJPNjlyNXJUYnltZDlPaF9DM1FkOExDV2YxM08yMDBDUmRwRmROcWNXR3NZX3pqUklNdGg1NzZYZ3lSR2xP?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 07 Aug 2026 15:33:54 GMT

## 新興題材：群聯7月營收

摘要：新興題材：群聯7月營收 相關新聞集中在：《半導體》群聯7月營收再寫新高 Boot Drive出貨飆45倍 - 工商時報；群聯7月營收創高，AI伺服器SSD出貨年增45倍 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《半導體》群聯7月營收再寫新高 Boot Drive出貨飆45倍 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE56Zm5pU1NnMGhmQVlXMV8wb29YbTdRX25aWk9VYmdydXlod2VJTURTRldsclp1NEEtdHFzMWtkU18xM0E5NzROMkY4VlZXODZDbi1XQ21tRzBDRklYZ040?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 07 Aug 2026 07:23:00 GMT
- [群聯7月營收創高，AI伺服器SSD出貨年增45倍 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQcmJaQXFwb1VCZHR0TEhDTVh4NzY5Zm5zMlg5SzhtQkFuREttdFh3WnEtZnRtdEdRZ2tWUGdidmtzRkVLaFg4bTJkWFc2ampXQ2FXd2VkSUt1Q1I1SmxBRUl0S3hRU3RtMlA4MGRTZFFSZDBxeDByQ0taSnZUM3djUWFQOUVmVE5INEZwaUlVNXBHQQ?oc=5) - Google News source discovery | MoneyDJ Fri, 07 Aug 2026 06:57:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
