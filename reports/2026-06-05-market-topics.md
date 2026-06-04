# 每日股市熱門話題分析 - 2026-06-05

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **AI 伺服器與資料中心**｜正向｜熱度 18｜市場確認 43.05｜同向 3/6
2. **記憶體與 HBM 供應鏈**｜中性｜熱度 6｜市場確認 N/A｜同向 0/0
3. **半導體與晶片供應鏈**｜中性｜熱度 8｜市場確認 N/A｜同向 0/0
4. **散熱與液冷供應鏈**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0
5. **新興題材：TradingKey**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.31（樣本 6）
- 5日相關係數：0.93（樣本 6）
- 同向比例：3/6

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| AI 伺服器與資料中心 | 43.05 | 3/6 | 2 | +2.69% | +6.32% |
| 記憶體與 HBM 供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：TradingKey | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：StocksToTrade | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-05-23 | -0.00 | -0.05 | +84.62% | 13 |
| 2026-05-24 | -0.11 | 0.22 | +86.67% | 15 |
| 2026-05-25 | 0.40 | 0.33 | +50.00% | 10 |
| 2026-05-26 | -0.23 | -0.31 | +92.31% | 13 |
| 2026-05-27 | -0.07 | -0.07 | +87.50% | 8 |
| 2026-05-28 | 0.14 | -0.07 | +88.89% | 9 |
| 2026-05-29 | 0.14 | -0.04 | +71.43% | 7 |
| 2026-05-30 | 0.16 | -0.06 | +71.43% | 7 |
| 2026-05-31 | 0.96 | 0.09 | +100.00% | 3 |
| 2026-06-01 | -0.92 | -0.72 | +16.67% | 6 |
| 2026-06-02 | 0.08 | 0.05 | +72.73% | 11 |
| 2026-06-03 | 0.48 | 0.62 | +90.91% | 11 |
| 2026-06-04 | -0.38 | -0.30 | +85.71% | 7 |
| 2026-06-05 | 0.31 | 0.93 | +50.00% | 6 |

## 歷史回測摘要

- 回測日期：2026-06-05
- 近5日 3日相關：0.19
- 近5日 5日相關：0.70
- 同向比例：+45.45%
- 權重狀態：未調整

- 方向準確度：+45.45%
- 信心排序準確度：0.19
- 診斷：弱正相關

調整原因：近 5 日有效樣本 11 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：AI 伺服器與資料中心 相關新聞集中在：Broadcom Sinks 14% on Soft AI Chip Outlook Despite Earnings Beat, Dragging Down AMD and Intel - 24/7 Wall St.；What To Watch In NVDA, AMD, AVGO & Other AI Chips After INTC Rally Coco Gauff (C4Djc3gy5z) - Mshale；Broadcom Stock Tumbles After AI Chip Forecast Disappoints - Gotrade

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AVGO 博通 | 新聞直接提及 | +0.57 | +0.35% | +31.09% | 418.91 | 479.23 | -12.59% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.76 | N/A | N/A | 111.78 | 114.68 | -2.53% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.76 | N/A | N/A | 523.20 | 542.52 | -3.56% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.72 | +9.57% | +23.40% | 218.66 | 218.66 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.07 | +1.27% | +3.92% | 2,385.00 | 2,425.00 | -1.65% | 同向 | 74.39 | 32.07 | 410.73B TWD / 17.50% | 2026-05-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.05 | +8.99% | -15.52% | 428.05 | 506.69 | -15.52% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.03 | -1.33% | -5.42% | 593.00 | 618.00 | -4.05% | 背離 | 10.86 | 55.06 | 62.25B TWD / 19.22% | 2026-05-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.03 | -2.74% | +0.45% | 4,430.00 | 4,545.00 | -2.53% | 背離 | 62.91 | 70.60 | 46.74B TWD / -4.14% | 2026-05-01 |

關聯理由（前 3）：
- AVGO：新聞直接提及「Broadcom、AVGO」，共 3 篇新聞命中。 同時符合主題標籤：AI, datacenter。 方向判斷命中詞：boost, growth, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel、INTC」，共 2 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：boost, growth, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。 方向判斷命中詞：boost, growth, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Broadcom Sinks 14% on Soft AI Chip Outlook Despite Earnings Beat, Dragging Down AMD and Intel - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi0AFBVV95cUxPdmRfWUZwQWcxUXprS1BlRjFpUTJ0QVVpTF95d19SY1BpRWxCNXBwcEVJMVpaSHVqX0JtVmdIajN1SzZZd1FIdnNETWVQWUViX01oY1hicEhUd0VDZExVVzA2cDRqcm5yaWkwX2ZOTHhfUkNfaWtFZENHbDd5Zm5TRjltY0NzVUllcXItaG84MF83c2twaHVFbGE1a3R2NnpROXJnQWdGZ2dJZTBfRkxXNEdwb1EyNkxrM0pzZFBfa2JNcVBGckRzM01UVlJkTmpX?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 04 Jun 2026 13:24:25 GMT
- [What To Watch In NVDA, AMD, AVGO & Other AI Chips After INTC Rally Coco Gauff (C4Djc3gy5z) - Mshale](https://news.google.com/rss/articles/CBMiYEFVX3lxTE1sZ290c3FXbk5XQVR3dUk2eE9ndjVNWklJbERLYjNIc3d3YmZlRm1DZVZzN2pOT0hVajM5bEFqV2hKeW05SjdqWXJqYnBHOXFNMVUyTWxWYTN5ZTVoYnVjQg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 04 Jun 2026 18:46:27 GMT
- [Broadcom Stock Tumbles After AI Chip Forecast Disappoints - Gotrade](https://news.google.com/rss/articles/CBMikAFBVV95cUxNQ1otdFFpWTdlXzFkazZCSjZUdmhrRzR1ZXRDTTZ5Y1ZzRmRCUTd1cXlqR0FKZjg3Yk9GOFpjZ3owc3dxSkc3OHVZRzV2Q2lqODhuQlRtLXNlbU9ZdFJrdHRLTnhpX1JBVm9kTUk4X2JqYi1NWU1tNkZoc3dEYXg5Mm5tX2FXdXc1MDZfZDVwRTk?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 04 Jun 2026 03:15:43 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Micron Drops 7% as Broadcom’s Disappointing AI Outlook Triggers a Semiconductor Selloff - Yahoo Finance；Opinion: The Best Memory Stock to Buy Isn’t Named Micron or SanDisk - AOL.com；Prediction: This Artificial Intelligence (AI) Chip Stock Will Soar After Micron's Earnings - The Motley Fool

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 996.00 | 1,079.57 | -7.74% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | -0.10% | +7.19% | 1,759.68 | 1,831.50 | -3.92% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | 0.00 | +0.35% | +31.09% | 418.91 | 479.23 | -12.59% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | 0.00 | +1.27% | +3.92% | 2,385.00 | 2,425.00 | -1.65% | 不適用 | 74.39 | 32.07 | 410.73B TWD / 17.50% | 2026-05-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +9.57% | +23.40% | 218.66 | 218.66 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、MU」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk、SNDK」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- AVGO：新聞直接提及「Broadcom」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Micron Drops 7% as Broadcom’s Disappointing AI Outlook Triggers a Semiconductor Selloff - Yahoo Finance](https://news.google.com/rss/articles/CBMipAFBVV95cUxQLTh2SkxLVW03ZHR5NDEyZXExR3RZOEZ4cUJseVJJYVpCRE5uWXItMzdhWE5HUTRJLWVTMmhKRzl2TnpwaHh4eno1UWNfdEJvR2xhNm81QjZlRVhCV0JZSzZjSU5WRlVjOHA0dWN4LXJrZE03Rlp2N1pMLXR6aTZONUZTbHhkQVAxbVZkcDh0LVI0U1lWY2J6dzhLcHBVMENIX0ZaeA?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 04 Jun 2026 15:15:44 GMT
- [Opinion: The Best Memory Stock to Buy Isn’t Named Micron or SanDisk - AOL.com](https://news.google.com/rss/articles/CBMifkFVX3lxTE9JR0xtQ25IWW9iUktGeHlhdDV0VUg5VkRjYjhTMjFOZGhxOWdJNjdySDhoWFZVbXJPbWZ6Ymo5ekJpZUJhN2tEam9BQXBIZXp2VUp0UkZUYzhUTzY0QnpETkJJbEtJZXgwUWlHb1NsazAwTTBkTjBPTUJJd1hWZw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 04 Jun 2026 14:41:11 GMT
- [Prediction: This Artificial Intelligence (AI) Chip Stock Will Soar After Micron's Earnings - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxORi12ZTlPcFI0ZE1UUnNHdElVQkppNVZaMWZEblRnbGQ5d25RdVFxXzhiTjR1d2hBVHUwNkUzaHhialh3REp0NU5DbnRYbWlIdFljZjM0VFFNalJJdUdfWjg5NnlvRm5ReWtzcDh3OHVSTEVVdG5sX0p2YjkyUmtQZm82c0hxcFNVZzdiRkVvcnlfell3aDNEWQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 03 Jun 2026 17:10:00 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Broadcom Sinks 14% on Soft AI Chip Outlook Despite Earnings Beat, Dragging Down AMD and Intel - 24/7 Wall St.；Broadcom's Stock Sinks Despite Solid Earnings. Other Chip Stocks Are Sliding Too. - Investopedia；Broadcom Stock Tumbles After AI Chip Forecast Disappoints - Gotrade

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AVGO 博通 | 新聞直接提及 | 0.00 | +0.35% | +31.09% | 418.91 | 479.23 | -12.59% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 111.78 | 114.68 | -2.53% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +9.57% | +23.40% | 218.66 | 218.66 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | N/A | N/A | 523.20 | 542.52 | -3.56% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +1.27% | +3.92% | 2,385.00 | 2,425.00 | -1.65% | 不適用 | 74.39 | 32.07 | 410.73B TWD / 17.50% | 2026-05-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | -14.38% | -11.97% | 125.00 | 144.50 | -13.49% | 不適用 | 4.00 | 31.41 | 22.66B TWD / 10.80% | 2026-05-01 |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 996.00 | 1,079.57 | -7.74% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -0.10% | +7.19% | 1,759.68 | 1,831.50 | -3.92% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- AVGO：新聞直接提及「Broadcom」，共 3 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Broadcom Sinks 14% on Soft AI Chip Outlook Despite Earnings Beat, Dragging Down AMD and Intel - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi0AFBVV95cUxPdmRfWUZwQWcxUXprS1BlRjFpUTJ0QVVpTF95d19SY1BpRWxCNXBwcEVJMVpaSHVqX0JtVmdIajN1SzZZd1FIdnNETWVQWUViX01oY1hicEhUd0VDZExVVzA2cDRqcm5yaWkwX2ZOTHhfUkNfaWtFZENHbDd5Zm5TRjltY0NzVUllcXItaG84MF83c2twaHVFbGE1a3R2NnpROXJnQWdGZ2dJZTBfRkxXNEdwb1EyNkxrM0pzZFBfa2JNcVBGckRzM01UVlJkTmpX?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 04 Jun 2026 13:24:25 GMT
- [Broadcom's Stock Sinks Despite Solid Earnings. Other Chip Stocks Are Sliding Too. - Investopedia](https://news.google.com/rss/articles/CBMisgFBVV95cUxOaEphSDRQOFVSdktVSjVmS1doUWt0TjRnVUg1WXBoR2l2ZUgwTXlVZGw5dzRVU2FXQm82VnY1ZHVCU09Da24xSDlvR3NTcF90cmtDZ1hrLVJGOXZCcWdsak1VV3Rwc2pBOGZKSGQyRXJ1a2kzYmZDbENDWFVYMUE1QWRqeFRjY0JQbm5LVlVDUkdDUnZpWGNxTGxKUEliT2tBRHdYLXpSVXI2UEVoNG5CcHdR?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 04 Jun 2026 14:57:38 GMT
- [Broadcom Stock Tumbles After AI Chip Forecast Disappoints - Gotrade](https://news.google.com/rss/articles/CBMikAFBVV95cUxNQ1otdFFpWTdlXzFkazZCSjZUdmhrRzR1ZXRDTTZ5Y1ZzRmRCUTd1cXlqR0FKZjg3Yk9GOFpjZ3owc3dxSkc3OHVZRzV2Q2lqODhuQlRtLXNlbU9ZdFJrdHRLTnhpX1JBVm9kTUk4X2JqYi1NWU1tNkZoc3dEYXg5Mm5tX2FXdXc1MDZfZDVwRTk?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 04 Jun 2026 03:15:43 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：輝達一句話 炸出散熱產業三個真相！Rubin降規效應掀波瀾 節能可以不用散熱？ - 財訊

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | -2.69% | +5.04% | 2,710.00 | 2,855.00 | -5.08% | 不適用 | 61.06 | 44.53 | 15.63B TWD / 71.62% | 2026-05-01 |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +9.57% | +23.40% | 218.66 | 218.66 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 1 篇新聞命中。 同時符合主題標籤：thermal。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [輝達一句話 炸出散熱產業三個真相！Rubin降規效應掀波瀾 節能可以不用散熱？ - 財訊](https://news.google.com/rss/articles/CBMie0FVX3lxTFB5NExyc2ZVT0s0NnNLb1JLNnpucDctak5fSTBUeElVSXkxQTc2Y2N0aDNXY0QyRDdxMXVtNm5oRkxsN21uMFZqX0RpeDRSN2liXzhaRTdIeG5Od2JINTVfNHRIM2N0dEhOX19BQXZfdV93b0hSOW9Nc1N5SQ?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 03 Jun 2026 09:00:00 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Intel Corp Stock (INTC) Opened Down by 3.98% on Jun 4: What Signal Does It Send? - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 111.78 | 114.68 | -2.53% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Corp Stock (INTC) Opened Down by 3.98% on Jun 4: What Signal Does It Send? - TradingKey](https://news.google.com/rss/articles/CBMiiwFBVV95cUxOQU5zeVVFcWxwWW1hbFgzTmxJTUFJeFRiX29TaHlxWFNPS2JrTmlIZTR0endsZVpGa28yTHJrc2lBdXNja3Y0RlUwbWtaS0RXQ2xNUUhYSVVrTFdKT3FOT1N0NElXcHBBcWRLTS1LQlBJb1owdHQ1Qzg5SExsVmQ0UWFLSkxHQTI1UFVZ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 04 Jun 2026 13:47:21 GMT

## 新興題材：StocksToTrade

摘要：新興題材：StocksToTrade 相關新聞集中在：Intel Stock Powers Higher As AI Strategy And Price Targets Align - StocksToTrade

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 111.78 | 114.68 | -2.53% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Stock Powers Higher As AI Strategy And Price Targets Align - StocksToTrade](https://news.google.com/rss/articles/CBMiekFVX3lxTE5xVWVBb0tfekRrZDJNM3NUNC14TG9ScFI0c3ZFOGhpQ0phak1EWVlMVFdZbnFLWHZKaTFlWTJlOWdsdXU4bDhTcWdNbFlYN3pQdnRrNTNZYXhLbjROUU9NeEpUTTVkYjAxMFVPNHZBN21rMjFuS3FMNXJB?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 03 Jun 2026 14:03:00 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股兆元宴 熱度不減 連25天日均量逾1兆元 - 經濟日報；台股平衡基金 穩穩賺 - 經濟日報；力成、建準 認購硬挺 | 權證特區 | 證券 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股兆元宴 熱度不減 連25天日均量逾1兆元 - 經濟日報](https://news.google.com/rss/articles/CBMifEFVX3lxTE5pMXVBOGdlX1UyMDhmTlR6N203cTNGNUVIRWhFQ0VHTElPamwyUzdZdUdiNEIwbFd3VE5KUTg5RURhTGRZcGowMmJQb2F2a2pIWVFZYlpyRGVSYmFHQVpEWmxXU0MyWURkSThPTTdTSzFyWjA2QzF4WGY1Tl_SAV9BVV95cUxNcC1FU2NXZlpwbG1PclFxQ3ZocTF5LVlUUGJjTGNtMzNoS3NlX0N4ZkFfZGlzV0RiaXNGcFd6TG5Kalg5WVUtUmxnd2Q2MjRvaEhBTHBhRWdweGZwWGx4SQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 04 Jun 2026 16:48:36 GMT
- [台股平衡基金 穩穩賺 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxQX0J3X0sxWkdsUDJtc3UzTG9wRllnZ1h2ang4UWI2QnJHVmJCM05XeXY5OEUyaVhGUUtEMGo2V05GOHRwZmZKSS1YWlNXNGljNWRtcGlDWDI3LXhBX3UzWWlVVVdHNkk1dzRYSHpkUG1qRzNJQ3paSmNMZG94eHd3eNIBX0FVX3lxTFB2bTRYbENySzRWZWpMVWh4WG5lcFVXSW5ENVA0VVRDY0tOU0tYTmo0RXdtempVc0VwMUwtWDJlc3QtRmpkXzBhWGE1UElINFhLQlpuTVRZMnJnbDk3X09v?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 04 Jun 2026 17:36:05 GMT
- [力成、建準 認購硬挺 | 權證特區 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE13Ykg1eGV3cERVX3YyUHpKWnlMTlZ4NFlzcVFFQTdzR3ZBVHc5LTRlZFQ1R3liWWtKd3RUZ01BUjc5YzYtdjdnd01iNGpzVkRfV0RUZnQ1cGlTZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 04 Jun 2026 16:53:41 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》收跌781點、失守46K，惟5日線有守- 新聞 - MoneyDJ；基金-FundDJ基智網 - MoneyDJ；《金屬》LME基本金屬多數下跌 期銅上漲0.6%-台股 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》收跌781點、失守46K，惟5日線有守- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQZFYybzZoeTJmWmtzUVdvMGEtSHB6Q3kzNC1GM3BmY1ZMeVZuejgwbVdoNzN0bU1XdDg5eDJ2X1lqWEFMVHBWWk02ZXZGZ1dHbVJ2QmROaDBaMkV1WGg4ZlVaUTAtY1RtLUx4NENGQWo2TjBKSy1Lb25KVmR1MTBJdDRISXhfTkN2WV8zRGVCd3FIUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 04 Jun 2026 07:48:00 GMT
- [基金-FundDJ基智網 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxPbWI2U3BQcVZoRFhhMmluX3d1WEhSbUppekYybXBqSnBxY3NjVUg2LXg5MDVXV3FDcDcwdFZPdFVicU43TnlIdmpPVVBrd3JqWG5fb0RoTUxJWVd3Undpci03alBOdHhLVURnc21FbjNINTI4MWZDZEljcW80dHlWc3Qzb0tVTlNzUDVJaXEwZjQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 04 Jun 2026 19:07:26 GMT
- [《金屬》LME基本金屬多數下跌 期銅上漲0.6%-台股 - MoneyDJ](https://news.google.com/rss/articles/CBMiigFBVV95cUxOZFd0ZTFJZ2tsVjg5cW50SmR4N3pPdU1ic2xTVFJiREU3OVVHcjlzc0dJb1J6R05Tcmg5Q2dQcm02YUhTbTJkRW9PbWVtdjhrYzB4OGFURkZHQUNrTjAzWndnNHNmRlhoNzNZalo0eE50anRMeGtGSkhneExMcHRWOVBlaUg1R1oxYmc?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 04 Jun 2026 22:14:25 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
