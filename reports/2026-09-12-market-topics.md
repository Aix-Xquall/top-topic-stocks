# 每日股市熱門話題分析 - 2026-09-12

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜中性｜熱度 5｜市場確認 N/A｜同向 0/0
2. **關稅與供應鏈轉移**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
3. **AI 伺服器與資料中心**｜正向｜熱度 14｜市場確認 16.19｜同向 2/8
4. **半導體與晶片供應鏈**｜正向｜熱度 6｜市場確認 12.27｜同向 2/8
5. **新興題材：ChartMill**｜正向｜熱度 1｜市場確認 21.84｜同向 1/3

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.39（樣本 20）
- 5日相關係數：0.04（樣本 13）
- 同向比例：5/20

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 關稅與供應鏈轉移 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 16.19 | 2/8 | 4 | -0.44% | -0.98% |
| 半導體與晶片供應鏈 | 12.27 | 2/8 | 4 | -1.75% | -0.49% |
| 新興題材：ChartMill | 21.84 | 1/3 | 1 | -0.50% | +3.39% |
| 新興題材：OpenAI | 0.00 | 0/1 | 1 | -10.08% | -0.74% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價呈負相關；應檢查正負向詞庫，並降低新聞直接提及但股價背離的權重。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-08-30 | -0.52 | -0.04 | +23.08% | 13 |
| 2026-08-31 | -0.41 | 0.29 | +40.00% | 10 |
| 2026-09-01 | N/A | N/A | +50.00% | 2 |
| 2026-09-02 | -0.29 | 0.24 | +75.00% | 12 |
| 2026-09-03 | 0.10 | -0.10 | +54.55% | 11 |
| 2026-09-04 | -0.08 | -0.08 | +28.57% | 7 |
| 2026-09-05 | 0.13 | 0.34 | +54.17% | 24 |
| 2026-09-06 | 0.19 | 0.43 | +50.00% | 24 |
| 2026-09-07 | -0.15 | -0.09 | +53.33% | 15 |
| 2026-09-08 | -0.07 | 0.18 | +57.89% | 19 |
| 2026-09-09 | -0.28 | -0.12 | +54.17% | 24 |
| 2026-09-10 | 0.28 | 0.86 | +75.00% | 4 |
| 2026-09-11 | -0.01 | -0.08 | +25.00% | 12 |
| 2026-09-12 | -0.39 | 0.04 | +25.00% | 20 |

## 歷史回測摘要

- 回測日期：2026-09-12
- 近5日 3日相關：-0.24
- 近5日 5日相關：0.29
- 同向比例：+42.86%
- 權重狀態：未調整

- 方向準確度：+42.86%
- 信心排序準確度：-0.24
- 診斷：方向與信心皆需修正

調整原因：近 5 日有效樣本 7 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Billionaire Stanley Druckenmiller Has Sold Micron, Broadcom, and Intel. Here's the Biggest AI Chip Designer Left in His Portfolio. - The Motley Fool；Micron Vs. Sandisk: Sandisk Built The Shield, But Micron Owns The Fortress (NASDAQ:MU) - Seeking Alpha；SK Hynix, Samsung Shares Dip In Korea After DeepSeek Debuts AI Tech That Uses Less Memory – Micron, SanDisk Hold Up - TradingView

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | +0.44% | N/A | 975.26 | 977.41 | -0.22% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | -6.02% | +5.04% | 1,633.35 | 2,335.00 | -30.05% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | 0.00 | -10.24% | N/A | 102.94 | 114.68 | -10.24% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | 0.00 | -7.01% | -18.98% | 361.99 | 446.77 | -18.98% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +8.74% | +3.39% | 218.29 | 220.78 | -1.13% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、MU」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk、SNDK」，共 4 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Billionaire Stanley Druckenmiller Has Sold Micron, Broadcom, and Intel. Here's the Biggest AI Chip Designer Left in His Portfolio. - The Motley Fool](https://news.google.com/rss/articles/CBMilwFBVV95cUxOS2JQeWtOUG9IamcxVUpOQjc5OHBtTGxucEFuTTlEOUl6cjhvVXhZazJZSDhGOGVJeTd4UE9RMFMxQTBRQWtUU0VxWXV2WXBjSGxfTC1zVk1WbXRMbXU1aUY3RlhINHVOMXBoUzRrcnNCNG1YVWhTcDFPampnM3ByclJJNXI3NVhtRUxMd1JVajZRVXF1aGpJ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 10 Sep 2026 13:26:00 GMT
- [Micron Vs. Sandisk: Sandisk Built The Shield, But Micron Owns The Fortress (NASDAQ:MU) - Seeking Alpha](https://news.google.com/rss/articles/CBMisgFBVV95cUxQQ0VCS2RVQTE2YXR0dFZMTDdZMXNMLXE5YUI2NVMwdlZILU9SMVphbUw5MldZNUtKdjJTTFB4SjllOTgyQzcxYUNQR3JOd0RheXQwVmEycEF0UWVvZ19TZXg3TzREcHFSalIyUlEtSmxtS3J6ZnRBYXVMWFhmeVRGZnVTcGJOQ1FxMzJIWjkwYXJ5MnI0YlB6Nk5UQkZnd0lONkxHQndiYmh6UWJhLVpVel9n?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 10 Sep 2026 06:52:40 GMT
- [SK Hynix, Samsung Shares Dip In Korea After DeepSeek Debuts AI Tech That Uses Less Memory – Micron, SanDisk Hold Up - TradingView](https://news.google.com/rss/articles/CBMiggJBVV95cUxQYzk4MzNIdGNsSUFGRnlaZU5JRlpFXzc5OWc0T3BLOXR2SUhkLUxRZlU3b214U25FbmlzXzBXS084RExNZnM4UGhqaEdISkZHTVFHUFhVdmpwTDdFeUpXNXRNeXUyRVFFZEptT2puaTNtczRmQzczZ3lSSDk0LUpFcXRQbFFjVkdJakpxUC16M001NHprbWFVV2NCbHlremhab0V6aTFtb2UweUYyczJ0Rzg3RUlVQnpsb3duc2NPMC1relgyOFlNckRtYktYRlFTTGFoMzNkdkZ1ZFkwN1Z6OGNhSXVWVG1mVFRUZ2dYd3FOa0hZV1BjX1U4TERNdnc2T1E?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 11 Sep 2026 07:18:11 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：原來川普將再課台灣半導體關稅是誤會一場？分析師如此解讀 - 經濟日報；CPO 技術如何重塑 AI 伺服器供應鏈競爭？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +6.48% | +19.16% | 332.27 | 332.27 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | -1.39% | -3.12% | 248.00 | 289.00 | -14.19% | 不適用 | 15.21 | 16.35 | 921.77B TWD / 51.98% | 2026-09-01 |

關聯理由（前 3）：
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [原來川普將再課台灣半導體關稅是誤會一場？分析師如此解讀 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFB2aUpySlhoYUl1Ym8tbFBKNnpmS2pYTTlJeFdzajhBUHRHdml3THUyNk00ck5ZQlVRcTRDejg5V1hVYko2bUw2aDAzMU5qOEdMN01iY0tFRXBoZ9IBX0FVX3lxTE9HOHRzSTdLM29lM2FDczFrSTlNMm1TNzV0cHBLVEpOOUg3WkNORnhtNUxjZ3F5RHNuMlVhdzRVTGMtSWpUN0RZRzhIbEp4QWpYODdMU2RqeVhDbUJDS1g0?oc=5) - Google News source discovery | 經濟日報 money Fri, 11 Sep 2026 08:51:06 GMT
- [CPO 技術如何重塑 AI 伺服器供應鏈競爭？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMidEFVX3lxTFBwMGJLOWFMazVlODRfa295VXFHcVpxQ3A2cnVuWnJBWml6dWIzd2gzcmhrRF9kZmV1bkYzdko1SWpEX0RJOS1vZllCYklQSUhwY1FrTjh1MUFQSENyLWlGMXk5T3NFRTJoNzBMTUpJRk9fRGZQ?oc=5) - Google News source discovery | TechNews 科技新報 Fri, 11 Sep 2026 12:18:08 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：《日股》AI/半導體權值股走弱 日經收跌1.93% - 工商時報；電力與營建資源能否支撐 AI 建設擴張？ - TechNews 科技新報；台灣如何從代工轉向 AIDC 布局，鞏固 AI 全球核心地位？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | +0.04 | -10.24% | N/A | 102.94 | 114.68 | -10.24% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.06 | +8.74% | +3.39% | 218.29 | 220.78 | -1.13% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.04 | +0.01% | N/A | 516.13 | 516.13 | 0.00% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.03 | -2.43% | 0.00% | 2,410.00 | 2,450.00 | -1.63% | 背離 | 86.28 | 27.94 | 514.81B TWD / 53.32% | 2026-09-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | +10.08% | +0.74% | 495.63 | 507.29 | -2.30% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -7.01% | -18.98% | 361.99 | 446.77 | -18.98% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.03 | 0.00% | +5.10% | 618.00 | 680.00 | -9.12% | 未明確 | 13.92 | 44.72 | 82.25B TWD / 45.66% | 2026-09-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.02 | -2.65% | +3.85% | 4,585.00 | 4,720.00 | -2.86% | 背離 | 60.69 | 75.72 | 64.18B TWD / 44.08% | 2026-09-01 |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [《日股》AI/半導體權值股走弱 日經收跌1.93% - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9LYWpqZ0pKSDJmaWZuWjdQTmxBbzFkNXE0MUhUMzVuX0VuNlVQWVVweW1BUmJPRkVQcktKYlNBNDdMX0RFLWhNQzNZeEJKRWZkRVF3Q194N0doWDBhb1RF?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 11 Sep 2026 08:19:00 GMT
- [電力與營建資源能否支撐 AI 建設擴張？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiVEFVX3lxTE5HWHZ1ZTBELWVKdWRjV3JhY3RJTzNfdHZOZWthYkZfU041UlBvclQzb2NMMXZxd1lCdXNRYmxvZHpoVlM5YXBFRzFxX2x6cDFURnN0cQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 11 Sep 2026 19:25:56 GMT
- [台灣如何從代工轉向 AIDC 布局，鞏固 AI 全球核心地位？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMibEFVX3lxTE9hSXZwM1RaenBqc25fRXJFYW9XX0ZUNmlGUUFnSEY5eEpjVjlobkJTSEJvdlVhb1AzMEplSWxoQVd2cTVYN0dzUU56ZXpiZGVIZjMwaFE4XzQtRWJlQm9Qd05POVVWMS0xX1ZiYQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 11 Sep 2026 16:36:42 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：台股外資狂砍 打46K 保衛戰 國家隊即刻救援 低接台積電、世芯等半導體股 - 經濟日報；Intel May Raise Chip Prices 10% and the Stock Took Off. Why Most Analysts Still Refuse to Buy. - 24/7 Wall St.；Intel (INTC) Advances High NA EUV For High Volume Foundry Production - simplywall.st

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.28 | -10.24% | N/A | 102.94 | 114.68 | -10.24% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | +0.25 | -2.43% | 0.00% | 2,410.00 | 2,450.00 | -1.63% | 背離 | 86.28 | 27.94 | 514.81B TWD / 53.32% | 2026-09-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.05 | +2.55% | +8.08% | 140.50 | 164.50 | -14.59% | 同向 | 6.68 | 21.13 | 25.04B TWD / 30.71% | 2026-09-01 |
| NVDA 輝達 | 產業/供應鏈推估 | +0.04 | +8.74% | +3.39% | 218.29 | 220.78 | -1.13% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.03 | +0.01% | N/A | 516.13 | 516.13 | 0.00% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | +0.03 | +0.44% | N/A | 975.26 | 977.41 | -0.22% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.02 | -6.02% | +5.04% | 1,633.35 | 2,335.00 | -30.05% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -7.01% | -18.98% | 361.99 | 446.77 | -18.98% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel、INTC」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：raise。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip, foundry。 方向判斷命中詞：raise。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 3 篇新聞出現相關標籤。 方向判斷命中詞：raise。

### 主要來源

- [台股外資狂砍 打46K 保衛戰 國家隊即刻救援 低接台積電、世芯等半導體股 - 經濟日報](https://news.google.com/rss/articles/CBMidkFVX3lxTE5PaTZ5MkZtTVBUS2xCS25UQnVFYU1GRC1JUmhPWERNLW5haktOSG10NmZ4N1FiTTZPWUpCYTFzdjMxcVlBY0d3WG5UT0QwWFZ3M0d0YW5CWEdqbk1jNnl2VUhhODA5aGw4bHd1aUpqalpMQ2FsZHfSAV9BVV95cUxOd3c0dTQ5T3NzUEdUMzlEdFVwUE9lZVRmWGMwR2MxRXlaMEItVWtiTWlqeDgzZkVoQktXRmFhYjM5VUxIek0yM2pBZ0ZMVF9VcERPcHo2WUhmdWY4NmJKQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 11 Sep 2026 17:02:33 GMT
- [Intel May Raise Chip Prices 10% and the Stock Took Off. Why Most Analysts Still Refuse to Buy. - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi0wFBVV95cUxOUUF0WWN1UVU4bGZ3bERLeVhobUpPX0JEVXpuaGdsRnFfSV9aeG9Vdzh2R2kzdXNLM3VfTlNmMWh6RmtQd1NRekRBaHA3eS1WZ1BKRERPUFU2T1owWk5OWW1kZU43ZTg4YkNIbEczQUVoel8yMmc4ajFiMXNVdC1lY2sxZlNoNkp1LXdMWlR0NFY2REl1c1h4MXp2M2NjV2hNX1dVcC1QdkhKekNPMDlfOFVra3ZPZDR6MDFJVG1qNDBQQ2VYMGI0UU5vQU9Kb21MMmRF?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 11 Sep 2026 12:51:00 GMT
- [Intel (INTC) Advances High NA EUV For High Volume Foundry Production - simplywall.st](https://news.google.com/rss/articles/CBMiygFBVV95cUxOaFp1MThlODdmZnFLQkRXckZZWUZiQTJkb1pWRHR3T1lTNVhBLVl4d1gzYzNDLTh3bEVrOVVhaU1TaTFJR1BiZUhYSEVUVnJJVUdqNVB2TUJIbTVLSFZsNXVlVUdYTHpLTDlDaEJkT3phMmNZNjBqeGVmMGE0cTRzamZ3ZDJhdlQwdmJ4NS1LMUdZOHhhb1ZnSFp4ekh5Qm1oUmY2UVJZYTdQdVA2S04wcEpGV0tqUEFqSFR0bmJQNlNVN2RsVkFNdXVR0gHPAUFVX3lxTE5FeGlRSlVqSG02QWRDejNVbkFLY1NmT0czSkZIRGVuRzlZeDFORHNlbmhGcnJrQlVVYWtHeUVWM2FGaTVzYzV3am1wU1Jnd0pKMVFwV2V6RUpwSzRKZDc4dXFZTjJSSXlDOFZPTzZleXpnUFR4RnBheTI5RG1jOVlWTU9BS0hvYjVKdE56ZHlWckpTVmlINmJ0SXZKVGtUV3NZNGlrR09peTZsVktCZ3pNRzQ2bU1wajA5a2pEblVXbDc2ZkJiNVU3ZktNanhrNA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 10 Sep 2026 19:20:50 GMT

## 新興題材：ChartMill

摘要：新興題材：ChartMill 相關新聞集中在：AI Chip Stocks Diverge Ahead of Nvidia Earnings as AMD and Intel Surge - ChartMill

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.42 | +8.74% | +3.39% | 218.29 | 220.78 | -1.13% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.32 | +0.01% | N/A | 516.13 | 516.13 | 0.00% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.21 | -10.24% | N/A | 102.94 | 114.68 | -10.24% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 方向判斷命中詞：surge。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 方向判斷命中詞：surge。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 方向判斷命中詞：surge。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AI Chip Stocks Diverge Ahead of Nvidia Earnings as AMD and Intel Surge - ChartMill](https://news.google.com/rss/articles/CBMivwFBVV95cUxPQnktTVVmYUFGMTZCZDVVLTdHdGRZZlpQOVpYejlxdmNWUk9nOUJMbHZ4aUZsQXdkV2dGZXJ0ZDkxX0J3UUlTaXhzS3JHLWh4cGJObTlGVGNwTXpLZU5DSHJLZEhfbjNYa0laYk13Q21McTdFYmJpbjVxR1ozM3FzVHNzZ1EtaUhTUjVpcVNmX0E2bDZmcG1KTWNhWVRVa0djSWljWm5laWpXWUlibHNkYTZsY0hMLVV6aGRvcXZmcw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 11 Sep 2026 12:36:03 GMT

## 新興題材：OpenAI

摘要：新興題材：OpenAI 相關新聞集中在：Altman tells staff OpenAI is open to slowing AI development, Bloomberg News reports - Reuters；Why fears of AI self-improvement are causing ‘existential’ concerns at Anthropic and OpenAI - CNBC；Trump dismisses AI extinction risks as more than a dozen OpenAI, Anthropic insiders call for a slowdown - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 新聞直接提及 | -0.28 | +10.08% | +0.74% | 495.63 | 507.29 | -2.30% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：新聞直接提及「OpenAI」，共 3 篇新聞命中。 方向判斷命中詞：slowdown。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Altman tells staff OpenAI is open to slowing AI development, Bloomberg News reports - Reuters](https://news.google.com/rss/articles/CBMiwgFBVV95cUxOM2FONXhOeTRKZVg5ZU5qa3JVQ2I4S1ZSX1V4YU1zelVDV19IczFXWWlGd1BfRjhfbVVNZ3R5ZW9VelJpT2k2TmVNUWk5UFdIcHJFMjdnMWVQbFdVMm53ckVfZEF5SnZqUjJvb0N3OXVKc19CNFd1Z2otY1Y4cmlBQ0VhaGZMbllrWHIyQUVLRU5JYTIzNm1jdTVTcmhQcHJmdWgzYzdwckp2c2NhcEttLUMycUh5OVA0NEVKZGZwRm04UQ?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 11 Sep 2026 02:33:00 GMT
- [Why fears of AI self-improvement are causing ‘existential’ concerns at Anthropic and OpenAI - CNBC](https://news.google.com/rss/articles/CBMigwFBVV95cUxNLXdFTmVGVWVBRlRkN0ktd3ZJTXBKTE1Da1RnTXB2bmpMTDhHeHR3Wjk1R1Z4el9ZOWxTVVYxTkNzTVk4dlBtTHpoZWNzUHkxZDVnSnZEMkNreERKZW9jekh5M1NhZU9oVGZPODRYMkhBQXpISVF2T1hBV1hfa1N0cjJBSdIBiAFBVV95cUxPR3VZZDNYM2x6VTVzeHM0aG16RmdBZ1JFQ00tc25OOFhjSTFHVmxoclVGanRob1Awb2ZzSXcxQ1o2cW9MS1BtUW45U2xhNG1DVEZUMlVGQjR1STZ0TFd6eDJoQ19fblVYZnRjVnNidHNkeF9Ka2xJbVNrWlJsN2ZIVUVUZ05NTURn?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 11 Sep 2026 11:00:01 GMT
- [Trump dismisses AI extinction risks as more than a dozen OpenAI, Anthropic insiders call for a slowdown - CNBC](https://news.google.com/rss/articles/CBMib0FVX3lxTFBFQmxROTdQNUMtdlp6WWt5NEJ4clJ3cXhXcmhCbWNSeHo3RWpkUzlsNVBqYldaVlFtYmtGdGl6ZklWczgyem0zbzcxWEM3R0Q5S2RwZElPNDdFYmtfbG9TeWFvc0tyVWt3U1FHd18wb9IBdEFVX3lxTE1ITHNmX3NhN1dBQ29pS3gzZ0JnX1dmQzNNUHdERWZuY3AwZXJmUXNDWVFaVFIxbF9GYkk3QWJKTkdabGdYX1F5Vkh6YU1OYVRaMUQ3aGMyVFVuM1VEOG1yTDFPS045d1NXd1o2VDcxMjhrUGF6?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 11 Sep 2026 10:58:24 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：誰成升息風暴重災戶？台股本周跌最慘10檔 新代、華星光意外入列 - 經濟日報；台股周線翻黑 誰還能逆勢狂飆？10檔周漲逾2成 這檔一周暴衝50% - 經濟日報；台股周線翻黑 誰還能逆勢狂飆？10檔周漲逾2成 這檔一周暴衝50% - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [誰成升息風暴重災戶？台股本周跌最慘10檔 新代、華星光意外入列 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1fUk53eDRFa1RQRXVCWjBIWE5SUFNZc2JpRG5pN2RVcXF5QUpEMThZVXY0SWxJWklWdndteFk3TzBCVVQ1NmtCTnBNRHQtMER2empKdm9LcjVsZ9IBX0FVX3lxTE9udzB2X1N1RVpLaUs3Sy05VTRNTi1OVHIxcjQtUVlSdExoSFhGaEV1X245UVlCNDZRMnZ1YkViUzZrRGtBOXR6N2lhUmExYXB1a3dpWXdWMTdaMy1iV3pv?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 11 Sep 2026 18:35:38 GMT
- [台股周線翻黑 誰還能逆勢狂飆？10檔周漲逾2成 這檔一周暴衝50% - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxNcmJGZTFqRjZ4eHZ3X0VqWFowTWxxVzRDYmgxTkhGY1F4dWluanNrQzZNbjVEd0ljWGdZSmR2ZFV6VmFoc2NNR1BycHRWTEFuNnNWT0U0UHVrdGRkcENkS3l1bGV5d3JEcVlhQWthZ09uLUpaZ2NER2Q4Qi1oX1cyUdIBX0FVX3lxTFBUQ1VfOGJ5cHBWbS11M1hOSDdFOVpJMHFzWk5MMXZKR1NULXBrZEIwRlJDbEg2aEdMdGdGb3dDWndpVU44dHJNa0h3QWxjSnBzemtJTVI2S1RzVjY0V1g0?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 10 Sep 2026 09:00:00 GMT
- [台股周線翻黑 誰還能逆勢狂飆？10檔周漲逾2成 這檔一周暴衝50% - 經濟日報](https://news.google.com/rss/articles/CBMie0FVX3lxTE0yOVVvVXFla0M1dTNaNzVEODdKUWRDQlpQdWFCWVoxUVNtUUxES2tHeF91S01zZHB2U1dCY3ZOQS0zT0NpMVc1dERER1N2SEdyMm1oUVpYNERUS3Z0OEpjLU55aWtucUk0T1VKc0xZdjdfenFUZjBLeWdQY9IBX0FVX3lxTE10dS1FVThIUElVMGRVY3RzQXladlZ4eEhGa0VSM1MwTGtvck9ZOXpEN2h0amVnQ3hnLVRjNGpYOWNuRmdlUFZ1R2F2ejh2WkhOSkFCWktpTGQ5NjROUmdv?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 11 Sep 2026 17:27:09 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》收跌755點、險守46K，周K翻黑- 新聞 - MoneyDJ；個股動態報導內容-17D84AC7-B1B6-4273-9F17-E2986C244F83 - MoneyDJ；台股產業結構轉變主動式市值型ETF助掌握核心動能- 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》收跌755點、險守46K，周K翻黑- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPQ0pSOWgyWXUwWVhNdmZPZDZMcEFJdXEyQWt2Z0tFRWJxZWV0VjdKa3pseXlZaExjWHRWLTlWYzgwaXB6ZzJ6cE5hSktWb3Z2Szc5Uk4yalFWQTByNzQ4c2MyNWJjWVFBUmZrWHhvcFFNWk1DOXhLQ2p1SGFrUmVnbVBfVktVQmctMGRIa250bnRWdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 11 Sep 2026 08:08:00 GMT
- [個股動態報導內容-17D84AC7-B1B6-4273-9F17-E2986C244F83 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxPMl9JemhJUHZWRXVlQ1h6ZVZacWN6dlJnaDR3Qm56azM2RXhNUnlibE54NVRlU21RU2wtcWVQTzNGa2loZTRyWFpZWEZvZXg3VVVVSXV4bm1MaEhOOVFnRUtOUjhzVy1TN2JaNTFtcWZ4bFZ1X0xPMENRY3NreHh0V1BSU0drcTVjQ2toSHFiS3ppU1h0?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 11 Sep 2026 16:51:23 GMT
- [台股產業結構轉變主動式市值型ETF助掌握核心動能- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNX25zamNQRFp2Q3BLVk5NdUR0WkVCdk5KajYyeWpKeWhvNkVYX2NwblNUR09iM3NrMUI2a1JEVms4SktUeGxfNUtVNVM5YndaNjZrc29rSDY4N2Z3TmpCMlY4MGMtYmFpMHY0Y214MURYWFd1NEFEcUZZX0l4bW9YbWFIR1k4di1GUG1rVHRoYk9IZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 11 Sep 2026 04:05:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
