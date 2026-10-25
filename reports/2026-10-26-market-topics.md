# 每日股市熱門話題分析 - 2026-10-26

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **新興題材：TradingKey**｜負向｜熱度 1｜市場確認 100.00｜同向 1/1
2. **散熱與液冷供應鏈**｜負向｜熱度 1｜市場確認 85.81｜同向 1/1
3. **記憶體與 HBM 供應鏈**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0
4. **半導體與晶片供應鏈**｜中性｜熱度 4｜市場確認 N/A｜同向 0/0
5. **新興題材：台股重量級法說**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.27（樣本 11）
- 5日相關係數：-0.25（樣本 8）
- 同向比例：4/11

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 新興題材：TradingKey | 100.00 | 1/1 | 0 | +24.17% | N/A |
| 散熱與液冷供應鏈 | 85.81 | 1/1 | 0 | +5.27% | -1.94% |
| 記憶體與 HBM 供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：台股重量級法說 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：AI散熱 | 85.81 | 1/1 | 0 | +5.27% | -1.94% |
| AI 伺服器與資料中心 | 0.00 | 1/8 | 6 | -4.20% | -1.93% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
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
| 2026-10-25 | 0.41 | 0.78 | +64.29% | 14 |
| 2026-10-26 | 0.27 | -0.25 | +36.36% | 11 |

## 歷史回測摘要

- 回測日期：2026-10-26
- 近5日 3日相關：-0.03
- 近5日 5日相關：-0.00
- 同向比例：+77.78%
- 權重狀態：未調整

- 方向準確度：+77.78%
- 信心排序準確度：-0.03
- 診斷：信心校準問題

調整原因：近 5 日有效樣本 9 筆，低於 15 筆門檻，暫不調整權重。

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

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Intel Stock Forecast: INTC Falls 8% Toward $81.64 Support Ahead of the October 29 Margin Test - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.42 | -24.17% | N/A | 86.96 | 114.68 | -24.17% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Stock Forecast: INTC Falls 8% Toward $81.64 Support Ahead of the October 29 Margin Test - TradingKey](https://news.google.com/rss/articles/CBMi7AFBVV95cUxOcHhkazFsaUFxQ20tM0RqMkNoazNEYVRsWmhETkxSNXVDdW5BTWhfNEUxTUxnaW55dUY1UDMxZmJVUVZjemlrV2V5cGdWMHZaWGR1Y1A4X2V0Z1RlUDItYko5VGFZRVFkdU8zLUxFY0RMUXhIRlphdkwzZjlVVElLY0JhUk5tVjEyWWZnNElrV0VXLWktbmp2Tk5TRDhZbFh3TzVKRGN0NHNQOHpoXzBDckFMb1NjRnZTdGVjS1U3UHdHc2xPVGxuZEwtMjhKSS1YbzUyclRpUFdrRUhtWFNHOUZJSFVjSlU5c1puaw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 25 Oct 2026 13:03:20 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | -0.43 | -5.27% | +1.94% | 3,145.00 | 3,435.00 | -8.44% | 同向 | 75.13 | 41.92 | 21.02B TWD / 44.92% | 2026-10-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 1 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：跌停。

### 主要來源

- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 25 Oct 2026 12:32:30 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Micron vs. Sandisk: Which Is the Better AI Memory Stock to Own for the Next 3 Years - The Motley Fool；Micron vs. Sandisk: Which Is the Better AI Memory Stock to Own for the Next 3 Years - Yahoo Finance；Micron Technology and Sandisk Prospects Analysis - Intellectia AI

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | -9.62% | N/A | 877.55 | 971.00 | -9.62% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | -9.33% | -4.72% | 1,238.03 | 2,335.00 | -46.98% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -4.45% | +5.43% | 210.96 | 228.38 | -7.63% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、Micron Technology」，共 3 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Micron vs. Sandisk: Which Is the Better AI Memory Stock to Own for the Next 3 Years - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxPUjZqMUtTU1d6MnMzTVF6Z181YmxqSGF5YTFkdUQzaWRQaDJXSUpkWVZ1TGFuaWxyOWRCOWJUdkNjSzdja05jR0hjcFg2TkhoVHdULTFnLWJLaXAwem1HVXhDbXRFRFU0RnRqNjBOZDlQLTVWcVVHOURfMjFvOHNlVW1FZmJMSDRZeVREYWtibUp3RTlFZ2xEZA?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 24 Oct 2026 14:02:00 GMT
- [Micron vs. Sandisk: Which Is the Better AI Memory Stock to Own for the Next 3 Years - Yahoo Finance](https://news.google.com/rss/articles/CBMilwFBVV95cUxNYVBRaFNhTkpyeEZmQWtnZWE3UFNEQzM3d3lndzhpWTFadU9JbGhYTWRCMzhaZ0toeUF0S3NiTUdCaDBzazhuNDFyVmxXOG9ZWldXc0JpUHdiaTFjSXpCTHlWcmp0c2pUaDN5RjlvUWZUeGJDTzhyZmZJQ2xXemo3QlJFZXVIWUlKaFpoRFByMF9OQ2lTNC1B?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 24 Oct 2026 13:22:00 GMT
- [Micron Technology and Sandisk Prospects Analysis - Intellectia AI](https://news.google.com/rss/articles/CBMiigFBVV95cUxOT3o3ZHQ5QnlGOFhEbGt4bEIzN1BqYzd1QTAxY2hxVlY3UHBVaGFBRlVXVGdpVTZwWUxsOGZ6N1NJbFdLVHUzZV83dkdhM0xLX1RjTjRSei1FY2VPVTV4TzdlUDU0eEVtSDlMX3FGZm8xX3o1WWRCekdSNlcyVkdYd0N4UUxGbEZoRlE?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 24 Oct 2026 21:38:43 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：立陶宛雷射技術札實 攜手台灣攻半導體 - 中央社 CNA；菲律賓力拚發展半導體產業周民淦：台灣可助攻| 國際 - 中央社 CNA；異質運算趨勢下，CPU 在 AI 架構的角色如何轉變？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | -24.17% | N/A | 86.96 | 114.68 | -24.17% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -1.45% | -2.25% | 2,385.00 | 2,480.00 | -3.83% | 不適用 | 86.28 | 27.65 | 511.86B TWD / 54.65% | 2026-10-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | -4.56% | -5.99% | 125.50 | 164.50 | -23.71% | 不適用 | 6.68 | 18.87 | 25.35B TWD / 27.22% | 2026-10-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -4.45% | +5.43% | 210.96 | 228.38 | -7.63% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | +0.13% | N/A | 516.79 | 516.79 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | -9.62% | N/A | 877.55 | 971.00 | -9.62% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -9.33% | -4.72% | 1,238.03 | 2,335.00 | -46.98% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -13.14% | -14.84% | 321.68 | 446.77 | -28.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 CPU, server CPU, x86, foundry；其中 1 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 0 篇新聞出現相關標籤。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 0 篇新聞出現相關標籤。

### 主要來源

- [立陶宛雷射技術札實 攜手台灣攻半導體 - 中央社 CNA](https://news.google.com/rss/articles/CBMiU0FVX3lxTE5Id29IdlM0aVVHMzh1MDI4U2RNT0pndGp5aXN6a1hrNjBsNGJjTlREY0hndEo4ck9mNHJPWFRVdVlndXc1TTc1dEJ2S2R6S3lsakJv?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 25 Oct 2026 09:49:55 GMT
- [菲律賓力拚發展半導體產業周民淦：台灣可助攻| 國際 - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9jWkl5VVIyTmdCZkU1TGRQOC1RczBjd0FXNGdoSW1JSlpfbmNOY3llTVlPWVNvYXFjVWZPM3p0SjhpMXg3eWtEMDlaSnpXVV9PdnlzQ1lOYTJKRXlvckxj?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 24 Oct 2026 12:10:00 GMT
- [異質運算趨勢下，CPU 在 AI 架構的角色如何轉變？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiakFVX3lxTE1qb3lIeGxWdEVDSkhwUFRudENhelE0dmtxYkFpc3lkQjRETWdmcFVqYWM0REtDWXh6X1o2QmhqTDczdlF4ZDVveTliT3V6S2tPY2RDejlTVlZ0Z3VWeWlPWWF2ZnAxdTJYMmc?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 25 Oct 2026 21:36:25 GMT

## 新興題材：台股重量級法說

摘要：新興題材：台股重量級法說 相關新聞集中在：台股重量級法說會登場！聯發科、台達電、聯電上陣 AI 需求能變獲利？ - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2454 聯發科 | 新聞直接提及 | 0.00 | -4.64% | -3.72% | 4,010.00 | 4,920.00 | -18.50% | 不適用 | 60.69 | 66.23 | 55.40B TWD / 1.97% | 2026-10-01 |
| 2303 聯電 | 新聞直接提及 | 0.00 | -4.56% | -5.99% | 125.50 | 164.50 | -23.71% | 不適用 | 6.68 | 18.87 | 25.35B TWD / 27.22% | 2026-10-01 |

關聯理由（前 3）：
- 2454：新聞直接提及「聯發科」，共 1 篇新聞命中。
- 2303：新聞直接提及「聯電」，共 1 篇新聞命中。

### 主要來源

- [台股重量級法說會登場！聯發科、台達電、聯電上陣 AI 需求能變獲利？ - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxPa0M1V0tlcEQ2TGJfanRtUHRRV0VlT19MVGh4WjU0alV6ZGVnNHhUdncxSkdCdGU1YlptSW84ZGg3ZzRfZkltXzJ6Q19mcTczbU40U25fcTJ4WmJxT3RKQXBiWXo2V1lEZjNUeG1wdUVnV3RWYVBaY0cxMVJIX3VmZdIBX0FVX3lxTE1jczljZnBXdjNXb2NXbGhLUVA1TDltZERkcWh2SFhYcV9xam5OVG5SZ1NzSXhGYWRrelNveUliOGRCUXpPWE1yZ3RtLVhxOFJiNWZGazBRSEtzci1iaHFn?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 24 Oct 2026 09:00:00 GMT

## 新興題材：AI散熱

摘要：新興題材：AI散熱 相關新聞集中在：焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | -0.42 | -5.27% | +1.94% | 3,145.00 | 3,435.00 | -8.44% | 同向 | 75.13 | 41.92 | 21.02B TWD / 44.92% | 2026-10-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 1 篇新聞命中。 方向判斷命中詞：跌停。

### 主要來源

- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 25 Oct 2026 12:32:30 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Top 3 AI Stocks With Revenue Growth Over 14% To Watch - Simply Wall Street；異質運算趨勢下，CPU 在 AI 架構的角色如何轉變？ - TechNews 科技新報；AI 如何加速漏洞轉化為攻擊程式的過程？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | +0.04 | -24.17% | N/A | 86.96 | 114.68 | -24.17% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.03 | -4.45% | +5.43% | 210.96 | 228.38 | -7.63% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.04 | +0.13% | N/A | 516.79 | 516.79 | 0.00% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.03 | -1.45% | -2.25% | 2,385.00 | 2,480.00 | -3.83% | 背離 | 86.28 | 27.65 | 511.86B TWD / 54.65% | 2026-10-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | +16.50% | +6.61% | 524.51 | 524.51 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -13.14% | -14.84% | 321.68 | 446.77 | -28.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.02 | -2.39% | -2.82% | 654.00 | 703.00 | -6.97% | 背離 | 13.92 | 47.32 | 88.13B TWD / 45.52% | 2026-10-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.02 | -4.64% | -3.72% | 4,010.00 | 4,920.00 | -18.50% | 背離 | 60.69 | 66.23 | 55.40B TWD / 1.97% | 2026-10-01 |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Top 3 AI Stocks With Revenue Growth Over 14% To Watch - Simply Wall Street](https://news.google.com/rss/articles/CBMizAFBVV95cUxPdlhmWXNYT0N1ZkJNSlFXSHBRZFdMbGNWRHRvMm95emstaGRQdEdrdEJOTGpkR0dQUTIzSXViN010QXNDX3ZCbWtENk9ucTAtTkZ1YkQzQWNvZGQtMm1nTENzYzUzX0YtSE5GUVVQZjlZOVVHSnNlU3RUYmhwRU9QOEk2Y2tmc1hRZWV1TDg4MHEwMm14SENTWU42dUFscENZb283bzJicjJoQWpNcEZvTG5UbVRRRTJkaFVrQlBZaTFVc21zRkU3a1h6SGnSAdIBQVVfeXFMUEU0b042OU9wTW12bzFuaEVSNXVwdm5FT2p4d3djX19uQmpvRDVjT3BabFN5UWltR0JPR1BnQ05NMGhIeC1QYzdVc3Z6cFpkMHBpbEpIQ3kxZ3NRdk9ud2k0d0YtSUtvWlFFQmQ0LXhQc3lSXzFZOHFMQXh6SGNrNDRwZmVwbk1GUkNPMmNUWVhiYjRQX0JPNDNrSTVYZDZnSFBHUm1yV1o5MnhxUnJGZlFnQUpIUW9yUl9aTnFHWlFOYWFwZDFxOU1kS1dZZFRoZVNR?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 25 Oct 2026 17:43:34 GMT
- [異質運算趨勢下，CPU 在 AI 架構的角色如何轉變？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiakFVX3lxTE1qb3lIeGxWdEVDSkhwUFRudENhelE0dmtxYkFpc3lkQjRETWdmcFVqYWM0REtDWXh6X1o2QmhqTDczdlF4ZDVveTliT3V6S2tPY2RDejlTVlZ0Z3VWeWlPWWF2ZnAxdTJYMmc?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 25 Oct 2026 21:36:25 GMT
- [AI 如何加速漏洞轉化為攻擊程式的過程？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiaEFVX3lxTE4zdnBKT0Y2d0FQU2VrUzRDaXNiT2xZaTE0WjZYVU1wMlNRTHJsUmRHREdyeFJPc3NmNkdud3VRa3hoMXdGaVhWWjUtbTRGbGZ1M3BXZTZkS0ZYY3Z4T2RESDFzdDVFVGl6?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 25 Oct 2026 18:18:32 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：個股動態報導內容-D063E264-E966-40A9-AE74-5D2FDC6F5EFF - MoneyDJ理財網；玉山-信義 對 鈊象(3293)個股 單一券商歷史明細 - MoneyDJ理財網；9月台股基金定期定額扣款回落 統一奔騰、統一黑馬逆勢成長受青睞 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-D063E264-E966-40A9-AE74-5D2FDC6F5EFF - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilAFBVV95cUxPT0hsZWpQMDJvV0dVdW52N0tjUGJaYm5OT0xDbHVqWEFQWm5rSjdQSkZWbUh1VGpGSnZOWGlTMDd1cTc5dG5zeVVaZ2NhUWpMMWtCYWJ3WjNTNjVDUzNSVG5LQ1NnNFJPR1FadjNWbHpvMkFXUDBCcVVYNlpVU3U4SVdKS3F0UWZRb2FHTWZLYW10M0Vs?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 24 Oct 2026 15:57:52 GMT
- [玉山-信義 對 鈊象(3293)個股 單一券商歷史明細 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikwFBVV95cUxOZG92dXJIT2xoV1ZnYThucmg5RWlySjBmQ2ZwUGdHYkdRaEtwa2EwZGFZdUF6cmktTlJiQ3V0SHpDQjd2TjVEVldEZy03Qmo4TUVDMGNOMl80dlN0YzFvT2tTMmw4ODdCQ0ZGaW1YVU52Q3hoUUZ1UC01anFrUFJvNEktalFWVGwxVEFKS2ZiOHoxN0U?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 24 Oct 2026 09:40:04 GMT
- [9月台股基金定期定額扣款回落 統一奔騰、統一黑馬逆勢成長受青睞 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1QamFFVzNQZS1sSWtyOFNIWXB2ZEo3WjE2QWRDUVFYUzFPZHJRMDlkYk40WHhsWkxnQjJYUExxX0hiQktHZV9lSDNvd2ZaQVpMTjlsOFZDekhLQdIBX0FVX3lxTFB2WENCY3o0aUlkMThzQTlDVUpPcVF4cmloSzcyZUliaXY4STNfTGttaFFueGRVenZzU1phUTJabnlDcVN5M3FCc1JHNVc0NE83SWhJMDRIQUVjNVJybE5V?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 25 Oct 2026 11:31:35 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
