# 每日股市熱門話題分析 - 2026-07-04

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **利率與成長股估值**｜正向｜熱度 2｜市場確認 N/A｜同向 0/0
2. **綜合市場情緒**｜正向｜熱度 36｜市場確認 0.00｜同向 0/1
3. **新興題材：TradingKey**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0
4. **AI 伺服器與資料中心**｜正向｜熱度 15｜市場確認 0.00｜同向 1/6
5. **半導體與晶片供應鏈**｜正向｜熱度 5｜市場確認 5.90｜同向 2/5

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.22（樣本 18）
- 5日相關係數：-0.36（樣本 18）
- 同向比例：4/18

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | 0.00 | 0/1 | 1 | -4.18% | -3.22% |
| 新興題材：TradingKey | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 0.00 | 1/6 | 3 | -4.51% | +4.29% |
| 半導體與晶片供應鏈 | 5.90 | 2/5 | 3 | -7.37% | +2.27% |
| 記憶體與 HBM 供應鏈 | 0.00 | 1/5 | 3 | -8.21% | -3.11% |
| 散熱與液冷供應鏈 | 0.00 | 0/1 | 1 | -9.31% | -22.39% |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價呈負相關；應檢查正負向詞庫，並降低新聞直接提及但股價背離的權重。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-06-21 | -0.01 | 0.32 | +55.56% | 18 |
| 2026-06-22 | -0.87 | -0.87 | +100.00% | 3 |
| 2026-06-23 | 0.38 | 0.01 | +62.50% | 8 |
| 2026-06-24 | -0.38 | -0.11 | +25.00% | 12 |
| 2026-06-25 | 0.10 | -0.21 | +20.00% | 5 |
| 2026-06-26 | 0.08 | 0.04 | +25.00% | 16 |
| 2026-06-27 | 0.12 | 0.29 | +57.89% | 19 |
| 2026-06-28 | 0.16 | 0.55 | +85.71% | 14 |
| 2026-06-29 | 0.49 | -0.25 | +38.46% | 13 |
| 2026-06-30 | 0.44 | -0.27 | +62.50% | 8 |
| 2026-07-01 | -0.08 | 0.25 | +30.77% | 13 |
| 2026-07-02 | 0.30 | 0.03 | +55.56% | 9 |
| 2026-07-03 | 0.21 | 0.08 | +55.56% | 18 |
| 2026-07-04 | -0.22 | -0.36 | +22.22% | 18 |

## 歷史回測摘要

- 回測日期：2026-07-04
- 近5日 3日相關：0.24
- 近5日 5日相關：-0.03
- 同向比例：+33.33%
- 權重狀態：未調整

- 方向準確度：+33.33%
- 信心排序準確度：0.24
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

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：野村投信：2026年下半年台股展望 AI驅動基本面續強 留意通膨與地緣政治變數 - MoneyDJ；AMD's Valuation is Stretched at 54.08X P/E: Buy, Sell or Hold the Stock? - TradingView

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AMD 超微 | 新聞直接提及 | +0.48 | N/A | N/A | 517.82 | 517.82 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | -0.57% | -22.93% | 390.49 | 506.69 | -22.93% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [野村投信：2026年下半年台股展望 AI驅動基本面續強 留意通膨與地緣政治變數 - MoneyDJ](https://news.google.com/rss/articles/CBMilwFBVV95cUxOM0dmRHpWRC1BblhEUy1OcWYya2dOZzhJYlhjRlN6QzJsb3NXUTBqbHNVSXRDeEhVSU1vMDh3ZkkxYU1yWGF1bGR0NlZ5NHJfXy1nUUNMZTJTcy1BcklkZzVpVWtpY2J1MXRRcXE4VmJHZU5oUERLaXItYnlZYlFYb25hcEl5aDZyQ2otMlZ1elJCcWF4aXhJ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 03 Jul 2026 08:36:00 GMT
- [AMD's Valuation is Stretched at 54.08X P/E: Buy, Sell or Hold the Stock? - TradingView](https://news.google.com/rss/articles/CBMiwwFBVV95cUxQZ0c4RV9wSng4RG01elFjb1BaNzFUTENxUC1ObUdiWkhwZFIyUjlTSmhRc3hNX0NjSzE3Xzc4a1g1Q1hEdTZUdDdfeEtRZWZEcm5vbFowd0cxRi0yaG1zV1k5OTdBeWVTNUJrYThWRGxOT1dkeG5xM29nWndVVXV3NDdZQ2hjLV92MXRKV3lzdzJNeWpMN3pPcFM4R28yZnN2cWlzRFNhZVZWNXJZd0NuQzdtc3p3X0RmbEo4eVc4S1VhTTA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 03 Jul 2026 16:50:00 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股下跌119點 三大法人逆勢買超473億元 - 經濟日報；台股外資狂砍 內資救援 力拱指數翻紅 - 經濟日報；台股黑翻紅46000點失而復得　單週上漲2208點 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2317 鴻海 | 新聞直接提及 | +0.24 | -4.18% | -3.22% | 240.50 | 289.00 | -16.78% | 背離 | 14.13 | 17.08 | 859.41B TWD / 39.57% | 2026-06-01 |

關聯理由（前 3）：
- 2317：新聞直接提及「鴻海」，共 1 篇新聞命中。

### 主要來源

- [台股下跌119點 三大法人逆勢買超473億元 - 經濟日報](https://news.google.com/rss/articles/CBMigwFBVV95cUxPVERqLUdRRk5Fa3RoRlFRcUJaWWhPMFhZbEFyYzJQTERMRVFRZDA3OGJBbGIzV2JFR0tIRm1lUHBOSFBFajIxdWl1eXJNZkZjOUZWZFhYa0JOdGhVN05TblhTVlNMQzZnUC1nd3BqQ2VvRGhFRTA5Y3laZ0pfWmN3RmEyd9IBX0FVX3lxTE1YUmVyRjIzRUh4OEhlV0NZaWtYRDBoOFdmdWhqTXpncmNJMUVPMjkxaW44c2xEV3RaSExyX21Yeno0UnlKVVVYWXhDLURNcXpTN19sT0Q5RWJCTkx1TjhV?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 02 Jul 2026 09:00:00 GMT
- [台股外資狂砍 內資救援 力拱指數翻紅 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5yblpBZURIeDloSUpLMVkwd1c2UmRkU2w1dGx6ei1qNENCZ3pFczZuY0NEcFdLSkg5ZTBkSDRUMjNyWmI5UWtzeHBGOXhucGxuWXRSaTdQTmdWQdIBX0FVX3lxTE1KeVlsdF9FVU9UYk42emRNdjlhMFZ4ZjZGLVBIQl9OWkhMcjZWOVEzTllBVTVfWHNpUFFUM3RyRTR0U19fV2JmMl9Pa1pNNm5IR0dkYVJGdlRVSEpsdWJZ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 03 Jul 2026 17:35:44 GMT
- [台股黑翻紅46000點失而復得　單週上漲2208點 - 經濟日報](https://news.google.com/rss/articles/CBMieEFVX3lxTE1oNndpanFYV2ZxZElheF9GNzZ4SGZCZlFDMGF2Vk9xdVctcDhHM2dlZzhGakl1cHJmamNaLW9rVmZfTWFZUk1adVU5aVJrZ1d4NjZtQUNScFlIcEQ1U0RkbVQ1THZ5dkNxU0Q5c2llamMxWDFHcUt3MtIBX0FVX3lxTE1zLWFMTXo3dkRNNXBVUlBaYUVpTnlwTnpqdW9HNmxONVk0eDFDNHZSSmpTRkxQb29vVTl0bEN1Z003a2EwMmRtNWN1b211ZEVOYmtyaDE2cGp5c2pYanZJ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 03 Jul 2026 06:31:13 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Micron Technology Inc Stock (MU) Moved Down by 4.27% on Jul 2: What Investors Need To Know - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 975.56 | 975.56 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Micron Technology Inc Stock (MU) Moved Down by 4.27% on Jul 2: What Investors Need To Know - TradingKey](https://news.google.com/rss/articles/CBMiiAFBVV95cUxObmpqaEhaUDhycDZhRmlaY3owMEFidVdJdmlCNnE0eERhcXZNODFxaTBidHJ1MzRSX1VUWkMzSnV4YkNYZk1zVE9kVlE1Z19Qclh0N1ZKTzBXampfejFOcWQyQk5GZmdKdEFPdi03TzFTUDNaM2E5R3Z6bHBxel9GVVdSeEJRYTlV?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 02 Jul 2026 15:15:24 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：台股收盤／漲36點收46780點 台積電收2445元跌0.81% | AI 人機協作 | 證券 - 經濟日報；AI Semiconductor Stocks Rally July 2026: NVDA AMD Investment Analysis - Intellectia AI；微型核反應爐首供 Blackwell！輝達攜手核能新創 Valar 布局 AI Factory - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.33 | -7.72% | +11.71% | 194.83 | 211.14 | -7.72% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.60 | N/A | N/A | 517.82 | 517.82 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | +0.60 | +1.45% | +4.49% | 2,445.00 | 2,465.00 | -0.81% | 同向 | 74.39 | 32.87 | 416.98B TWD / 30.09% | 2026-06-01 |
| MSFT 微軟 | 新聞直接提及 | +0.43 | -0.57% | -22.93% | 390.49 | 506.69 | -22.93% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 產業/供應鏈推估 | +0.08 | N/A | N/A | 120.35 | 120.35 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -19.32% | +16.46% | 360.45 | 446.77 | -19.32% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.03 | +0.29% | +7.91% | 682.00 | 727.00 | -6.19% | 未明確 | 10.86 | 63.32 | 63.03B TWD / 28.57% | 2026-06-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.02 | -1.18% | +8.12% | 4,195.00 | 4,345.00 | -3.45% | 背離 | 62.91 | 66.85 | 47.43B TWD / 4.99% | 2026-06-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVDA、輝達」，共 2 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。 方向判斷命中詞：衝擊, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。 方向判斷命中詞：衝擊, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 同時符合主題標籤：AI, advanced packaging, CoWoS, AI server。 方向判斷命中詞：衝擊, rally。

### 主要來源

- [台股收盤／漲36點收46780點 台積電收2445元跌0.81% | AI 人機協作 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1LZ1JCNkxpb2kxX1ROWENqcVp1R0N0S28xeDh4aDdma1ZobFBoX01UVmNweE16VEdWOFpRU2ZtRkdfdkNNVGRyYUNvci1tUUdrd3hOLVc2U3FDUVU?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 03 Jul 2026 00:00:00 GMT
- [AI Semiconductor Stocks Rally July 2026: NVDA AMD Investment Analysis - Intellectia AI](https://news.google.com/rss/articles/CBMidkFVX3lxTE4zcHVGTXhkajIwXzl0MkNoaHo1Q2ZjRFcyRl95QVZCQmNBR2RzUWFPSUVJNVZweGZUQ1lYQTNyM1pKZ2FqUGlOQTFPRXo4ZHVJUGEtTGFxQzB1MmduSnRzeUtTdjFwY2VUQmZaeC1IWUVZdVV1Nnc?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 03 Jul 2026 08:14:16 GMT
- [微型核反應爐首供 Blackwell！輝達攜手核能新創 Valar 布局 AI Factory - TechNews 科技新報](https://news.google.com/rss/articles/CBMidEFVX3lxTE94dlRLQzdhdXpkbURGejMzVGYzdmtLUDB2Y2NsMVR4eXBvYVNFVXZ3aXdmSkloSGZHbnZZYjZ0MEJLS3M4eDNHT3o3dk5tZlJWWXhfZkk0S210OHlnMGFQVzh0QmRFakVrNW50VEtsLThoODZL?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 02 Jul 2026 03:21:42 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：AI Semiconductor Stocks Rally July 2026: NVDA AMD Investment Analysis - Intellectia AI；金屬中心半導體檢測實驗室揭牌 攜手SEMI與日立先端強化S廊帶量能 - 中央社 CNA；美國半導體投資熱 德州科學園區吸引台灣企業布局 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.27 | -7.72% | +11.71% | 194.83 | 211.14 | -7.72% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.53 | N/A | N/A | 517.82 | 517.82 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 產業/供應鏈推估 | +0.07 | N/A | N/A | 120.35 | 120.35 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.04 | +1.45% | +4.49% | 2,445.00 | 2,465.00 | -0.81% | 同向 | 74.39 | 32.87 | 416.98B TWD / 30.09% | 2026-06-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.04 | +3.65% | +3.96% | 170.50 | 170.50 | 0.00% | 同向 | 4.00 | 42.84 | 22.94B TWD / 17.78% | 2026-06-01 |
| MU 美光 | 產業/供應鏈推估 | +0.03 | N/A | N/A | 975.56 | 975.56 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.01 | -14.89% | -25.27% | 1,745.00 | 2,335.00 | -25.27% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.01 | -19.32% | +16.46% | 360.45 | 446.77 | -19.32% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVDA」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 CPU, server CPU, x86, foundry；其中 1 篇新聞出現相關標籤。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AI Semiconductor Stocks Rally July 2026: NVDA AMD Investment Analysis - Intellectia AI](https://news.google.com/rss/articles/CBMidkFVX3lxTE4zcHVGTXhkajIwXzl0MkNoaHo1Q2ZjRFcyRl95QVZCQmNBR2RzUWFPSUVJNVZweGZUQ1lYQTNyM1pKZ2FqUGlOQTFPRXo4ZHVJUGEtTGFxQzB1MmduSnRzeUtTdjFwY2VUQmZaeC1IWUVZdVV1Nnc?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 03 Jul 2026 08:14:16 GMT
- [金屬中心半導體檢測實驗室揭牌 攜手SEMI與日立先端強化S廊帶量能 - 中央社 CNA](https://news.google.com/rss/articles/CBMiVkFVX3lxTE1IMDFKV0xaLTJ5V0YzTEljTUxRTXFFWTNTWFhubHdEbzZ1Y2RsMTFoVF9EMTN4emVoTTZmZkxVbFdValN2Wk84cE1UcXo4SGo2UXlrbDhR?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 03 Jul 2026 08:11:36 GMT
- [美國半導體投資熱 德州科學園區吸引台灣企業布局 - 中央社 CNA](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1GbmItcXptOHV0NjJFS2RoRjh1U0dVYnRPRlNUd3gyYko3clAwbTU3NU5WZXc4b2VFN3ZWVXJoUWJlLVI1Z1hlbTBSZUw5VUtmUmVKSjFYc3ZQQQ?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 03 Jul 2026 08:28:37 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：MU, INTC, SNDK: Chip Stocks Rally After-Hours On AMD’s Blowout Report - Stocktwits；US Memory Chip Giants Shed $340 Billion in Two Days as 'Big Short' Investor Targets Micron - finance.biggo.com；Zacks Investment Ideas feature highlights: JPMorgan, Sandisk, Micron Technology, Nvidia, Broadcom, AMD, Taiwan Semiconductor, Arista Networks, Meta Platforms and Microsoft - The Globe and Mail

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.65 | N/A | N/A | 975.56 | 975.56 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.33 | -14.89% | -25.27% | 1,745.00 | 2,335.00 | -25.27% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.56 | N/A | N/A | 517.82 | 517.82 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.25 | -7.72% | +11.71% | 194.83 | 211.14 | -7.72% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.48 | N/A | N/A | 120.35 | 120.35 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 新聞直接提及 | +0.36 | -0.57% | -22.93% | 390.49 | 506.69 | -22.93% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | +0.24 | -19.32% | +16.46% | 360.45 | 446.77 | -19.32% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | +0.48 | +1.45% | +4.49% | 2,445.00 | 2,465.00 | -0.81% | 同向 | 74.39 | 32.87 | 416.98B TWD / 30.09% | 2026-06-01 |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron、Micron Technology」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally, fuels。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK、SanDisk」，共 2 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：rally, fuels。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [MU, INTC, SNDK: Chip Stocks Rally After-Hours On AMD’s Blowout Report - Stocktwits](https://news.google.com/rss/articles/CBMiygFBVV95cUxPeVlYaXJjQjNtTkNRQUxQTHhaLUFMbE80Uy1MeDBpV0FPdkg2SHRLdkdfVUpXM1NrNWhZSVZQQ01sa0o4T1hKdzF1clBFRlRWUmMwWGxQTDNVVFBpOVhObUc2MXpBeXBOZ0p3R0w5NGRNOHB4X0ZIXzhlT0NMbmhzc1RtdmJRTWhlRUhKSHpyVnpaU0VGMlJyU2tDcmdkTG1hWVJJbmtTVDREbzFfWDB4bjhuTGswN3lmdkdHQzY1dzFOVU41VGlBNlZn?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 02 Jul 2026 13:08:27 GMT
- [US Memory Chip Giants Shed $340 Billion in Two Days as 'Big Short' Investor Targets Micron - finance.biggo.com](https://news.google.com/rss/articles/CBMidkFVX3lxTE93UE4yU21pTmxaYjhiU2d3S21YdEhwUk80SERKNmFZYUpmX0NaOEN4ZWUwYmkzLXhiTFMwZFRZTV93OUw0ZTlmdm9RMEpCdHlNb01GbU9Nb2xUX1BxRFhMWWxIUUdaVGpxalhJMGRJNy1jSG1yWHc?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 03 Jul 2026 06:15:00 GMT
- [Zacks Investment Ideas feature highlights: JPMorgan, Sandisk, Micron Technology, Nvidia, Broadcom, AMD, Taiwan Semiconductor, Arista Networks, Meta Platforms and Microsoft - The Globe and Mail](https://news.google.com/rss/articles/CBMi5gJBVV95cUxQd3o5MUdua3lkZmZ6SXB3OUQxQVZGUmVRNjJiLUktM1NtRldCREE2ZUFvQzl6VFJDSlJiZmpuUjJMQjh3b1VBbUk2MUtia1g3VllzV2VKM1hRelkyak5SX3ZhNUgwUW9WNWZkVjM4YnFFak1YR05LQjBVR1oxN0RlRnFOM1NDNzB2bkZFdlpuNzlZWlNqSXdxRWdHLTlWRWNXSFUxR0NQTm9tMkM1ZTRwamViRWR0czR4MzRsWF9JME9ZdmdKaFd0Y0VBMTBObkNXb0xlLUNsQ0t6WkRGVUVWZ3Q5Y0hvSDRTalY4R1VSbDBUcEZUc2N1bXlEaHBwWGRkME5LeUVqTmQzdFlEZUhtdkRJNWVOUmFUR015LU9vdW9EWHE2X2IybVhtd1RpUGlkenh4YzRVMVdER2N5dFhMdnJHY2hTeEJUbEhkc2FDc2lhT29jeXJWbGpJdmVoWGVWWm5nZXdR?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 02 Jul 2026 14:24:00 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | -0.25 | +9.31% | +22.39% | 2,760.00 | 2,835.00 | -2.65% | 背離 | 61.06 | 45.35 | 15.87B TWD / 60.64% | 2026-06-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 1 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：跌停。

### 主要來源

- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 02 Jul 2026 20:07:49 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：個股動態報導內容-5BFC87A9-0100-44FA-989E-1D077D56C21F - MoneyDJ；《台股盤後》收漲36點、5日/10日線失而復得；週K翻紅- 新聞 - MoneyDJ；個股動態報導內容-0ABA5E24-C285-41E9-A181-3764B51884D8 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-5BFC87A9-0100-44FA-989E-1D077D56C21F - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxQbDdfbXgzWHVZNVItOGhVV3NpTzY2ZnZuRHU4OFQtRWlBNThSVVNLNXZGNWY2MldVNUhDbVpFQ1hIeU9ZOGxuS3Y3RjhKeGVrbHN4N2hlR2Vnd0lWQnlERURHZnNfbW94ZXBuQ1dIMzh1eFM3QWM3MEhYdWpkZXRZSS14aXF3QTB6RmVvcE4xTE1yYWti?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 03 Jul 2026 19:06:44 GMT
- [《台股盤後》收漲36點、5日/10日線失而復得；週K翻紅- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxOb1dsMVRsVHlybXRuNG1oUVJQTjBWMmlsdkNUenlLaHUtYlQzbm15MGVlTjMwWHdyU0VnTFhrV3FtNERhektsbzBmVUxQaXNuYlZpNXQwMmJhLTY4bDRDQXFFNUpWVHZoV2dKVDFtZmhMRGg0Snl2ZXNnd0tnUzkyR3RJVldFQlVpZEhOTGZ6MlJ3Zw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 03 Jul 2026 08:21:00 GMT
- [個股動態報導內容-0ABA5E24-C285-41E9-A181-3764B51884D8 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxNdVVLWTJTOW4xQ1N1X3RKVHExNVBvcTFMSmdxSFVMSjMxNW1rYUZZSFluck9CaTdqRUd1WklGbG5UUS1IeDNuRXpHdkM1bXpYTHVTUmo1WFBqcjc1b2VCajI0MkVtWGVfTVdGRDFUSUJDRXFNcEl0UmJGeGc5WWVsTVdDVXUzYTRRNXlERnhHY2loUzVp?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 03 Jul 2026 12:12:08 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
