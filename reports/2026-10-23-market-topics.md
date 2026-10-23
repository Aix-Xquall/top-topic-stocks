# 每日股市熱門話題分析 - 2026-10-23

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **AI 伺服器與資料中心**｜負向｜熱度 21｜市場確認 74.89｜同向 7/8
2. **半導體與晶片供應鏈**｜負向｜熱度 5｜市場確認 82.01｜同向 7/8
3. **散熱與液冷供應鏈**｜負向｜熱度 2｜市場確認 85.81｜同向 1/1
4. **新興題材：OpenAI**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0
5. **記憶體與 HBM 供應鏈**｜中性｜熱度 3｜市場確認 0.00｜同向 0/1

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.35（樣本 19）
- 5日相關係數：0.29（樣本 14）
- 同向比例：15/19

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| AI 伺服器與資料中心 | 74.89 | 7/8 | 1 | +4.55% | +1.88% |
| 半導體與晶片供應鏈 | 82.01 | 7/8 | 1 | +6.92% | +3.68% |
| 散熱與液冷供應鏈 | 85.81 | 1/1 | 0 | +5.27% | -1.94% |
| 新興題材：OpenAI | N/A | 0/0 | 0 | N/A | N/A |
| 記憶體與 HBM 供應鏈 | 0.00 | 0/1 | 1 | -3.88% | +6.06% |
| 關稅與供應鏈轉移 | 0.00 | 0/1 | 1 | -3.88% | +6.06% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：震盪中聚焦供應鏈 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-10-10 | -0.28 | -0.96 | +57.14% | 7 |
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

## 歷史回測摘要

- 回測日期：2026-10-23
- 近5日 3日相關：N/A
- 近5日 5日相關：N/A
- 同向比例：0.00%
- 權重狀態：未調整

- 方向準確度：0.00%
- 信心排序準確度：N/A
- 診斷：樣本不足

調整原因：近 5 日有效樣本 3 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：AI 伺服器與資料中心 相關新聞集中在：Chip Stocks Fall as Supply Warning Deepens AI Selloff: Marvell and AMD Sink 8%, Intel Drops 7% - 24/7 Wall St.；Intel Needs More Than AI Momentum In Q3 - Seeking Alpha；Intel (INTC) Joins Musk's Terafab AI Chip Venture In High Profile Alliance - Simply Wall Street

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.57 | -25.45% | N/A | 85.49 | 114.68 | -25.45% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.53 | -1.58% | N/A | 507.93 | 552.72 | -8.10% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2454 聯發科 | 新聞直接提及 | -0.48 | -4.64% | -3.72% | 4,010.00 | 4,920.00 | -18.50% | 同向 | 60.69 | 66.23 | 55.40B TWD / 1.97% | 2026-10-01 |
| NVDA 輝達 | 產業/供應鏈推估 | -0.06 | -3.88% | +6.06% | 212.21 | 228.38 | -7.08% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.06 | -1.45% | -2.25% | 2,385.00 | 2,480.00 | -3.83% | 同向 | 86.28 | 27.65 | 511.86B TWD / 54.65% | 2026-10-01 |
| MSFT 微軟 | 產業/供應鏈推估 | -0.02 | +15.73% | +5.91% | 521.08 | 532.95 | -2.23% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -12.72% | -14.43% | 323.24 | 446.77 | -27.65% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.04 | -2.39% | -2.82% | 654.00 | 703.00 | -6.97% | 同向 | 13.92 | 47.32 | 88.13B TWD / 45.52% | 2026-10-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel、INTC」，共 3 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：fall, 強勁。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。 方向判斷命中詞：fall, 強勁。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2454：新聞直接提及「聯發科」，共 1 篇新聞命中。 同時符合主題標籤：AI。 方向判斷命中詞：fall, 強勁。

### 主要來源

- [Chip Stocks Fall as Supply Warning Deepens AI Selloff: Marvell and AMD Sink 8%, Intel Drops 7% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMizwFBVV95cUxPSHYtVnBnaXBZc3V3cXUySWxseXJNcVUxV0Vhb2R5SlFkMVF4aTRyemE3VDladG5fVVB4blJNb0YwR3BwTG85TUt4MG0xT2R4Q1dOMUFXcUNtSkFVejktNjVWVXlWRThLUVBoX1hHZGNQWnZPdjZCaXFqYzRFWm1IWXdoQzl0WjlpZ0hxclhpUWFZa01ERVFCMHRtTFdVUEtDRURXYW1lWnJxSlRVYmpiaEREaGphdmo3Rld6OUg4R1BaOUhXNGtadEZvOENFWlE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 22 Oct 2026 15:45:00 GMT
- [Intel Needs More Than AI Momentum In Q3 - Seeking Alpha](https://news.google.com/rss/articles/CBMihwFBVV95cUxPenROb1ZldU5vZ1VVTE15S2FqdWxvM0RKckkzMDB6S0tFTl92QUMtUEFxaEpVYVphZThVYl90NzVfMjEyZ19NS29CMFEzeWlRYjZHZ3RxeTBabGF0ZklwNXZrMG80elRiNlpXZF9sc3d6T2dnWEVvYno5WjRBRDgxaHV4ZlZfVGc?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 22 Oct 2026 03:24:52 GMT
- [Intel (INTC) Joins Musk's Terafab AI Chip Venture In High Profile Alliance - Simply Wall Street](https://news.google.com/rss/articles/CBMiygFBVV95cUxNYlBnVmlIdGZHNTQ2VFdwZk5lTlcwRlhVVjB2WFpUbjFMMGFaWW1CZ0tBcGJlbHpKUW9iMVhHRC14LWVCWC1pZDl2UHFVendRR0tRY01IRDZZdFhqNEhVeTI3VHFhM09pTW52eDVLdVVGT1lqaXdMM2EwUVFmZ0NKUWlFaEs0cDFsR0JWMGE0VVU0d04xeVIyN2FoX1ZEOUFzQUVVZWx0Q1lUYjNGWkVWUV9JM2k4ZlNuQTczNDhnNUM0T3BHWFF6N1hR0gHPAUFVX3lxTE9SejFUc19GVEN6VzFiX0Z6MEcxdGVxQTVvMUxMUXdNQnowZlU4RGhZc1ppbW5UVUhSQlNmQTZpSFlhY2hlcW1MN2pjdlJvYi03ajFIalk1a3FUZG9QZTJoeDVVRlFqWHZ5Qmc3emxYWDdITUlYejdPR1F2ZlVZYzR3OF9yRVhuYjZ5U1RRUGNlMWNHZWdPZzJYWFZMYW82Szhodmt6QXlaZzhQZU5oQ1VMYWRPT2xmbndWRG15Q2F4cjkzclRDLXBTSDFhazNnMA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 22 Oct 2026 06:17:57 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Chip Stocks Fall as Supply Warning Deepens AI Selloff: Marvell and AMD Sink 8%, Intel Drops 7% - 24/7 Wall St.；AMD, QCOM Targets Raised While INTC, COHR Face Cuts — Susquehanna Sees ‘Modest Upside’ For Chip Earnings - TradingView；Intel (INTC) Joins Musk's Terafab AI Chip Venture In High Profile Alliance - Simply Wall Street

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.57 | -25.45% | N/A | 85.49 | 114.68 | -25.45% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.57 | -1.58% | N/A | 507.93 | 552.72 | -8.10% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.05 | -1.45% | -2.25% | 2,385.00 | 2,480.00 | -3.83% | 同向 | 86.28 | 27.65 | 511.86B TWD / 54.65% | 2026-10-01 |
| 2303 聯電 | 產業/供應鏈推估 | -0.05 | -4.56% | -5.99% | 125.50 | 164.50 | -23.71% | 同向 | 6.68 | 18.87 | 25.35B TWD / 27.22% | 2026-10-01 |
| NVDA 輝達 | 產業/供應鏈推估 | -0.04 | -3.88% | +6.06% | 212.21 | 228.38 | -7.08% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | -0.04 | -11.79% | N/A | 856.49 | 971.00 | -11.79% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | -0.02 | +6.07% | -1.79% | 1,378.22 | 2,335.00 | -40.98% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -12.72% | -14.43% | 323.24 | 446.77 | -27.65% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel、INTC」，共 4 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 3 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 4 篇新聞出現相關標籤。 方向判斷命中詞：fall。

### 主要來源

- [Chip Stocks Fall as Supply Warning Deepens AI Selloff: Marvell and AMD Sink 8%, Intel Drops 7% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMizwFBVV95cUxPSHYtVnBnaXBZc3V3cXUySWxseXJNcVUxV0Vhb2R5SlFkMVF4aTRyemE3VDladG5fVVB4blJNb0YwR3BwTG85TUt4MG0xT2R4Q1dOMUFXcUNtSkFVejktNjVWVXlWRThLUVBoX1hHZGNQWnZPdjZCaXFqYzRFWm1IWXdoQzl0WjlpZ0hxclhpUWFZa01ERVFCMHRtTFdVUEtDRURXYW1lWnJxSlRVYmpiaEREaGphdmo3Rld6OUg4R1BaOUhXNGtadEZvOENFWlE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 22 Oct 2026 15:45:00 GMT
- [AMD, QCOM Targets Raised While INTC, COHR Face Cuts — Susquehanna Sees ‘Modest Upside’ For Chip Earnings - TradingView](https://news.google.com/rss/articles/CBMi7wFBVV95cUxPOERNdEdhT2hyV0MzdWFJSVMzN1lLU25zekdLOXZFLXBqVUhIb0VobzBTTV9PNDFTYzQ3TzJ0YjFDLUFNOHhrMVZiNzdBaW9NNmFLWGFsWXhPZDMyZ2d5eVp0NDJxZzlxdmJjQXdiYjRHZGxPcENEQkU4WThOMGl0RU1BcWJ0YkNoQ2laUkF0UnlNVGZiMjUzMFJEWFN4RUF0UXhfNTJEMGstdWl2SkpSaW1nakZQbDJndFJ3dHJta2xVNnBfRkN4c3phVVQ2anRkZE5uLVNFWjJIX2tEQW1mUEhOaFE3YkVjaWh2SGtQUQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 21 Oct 2026 14:30:29 GMT
- [Intel (INTC) Joins Musk's Terafab AI Chip Venture In High Profile Alliance - Simply Wall Street](https://news.google.com/rss/articles/CBMiygFBVV95cUxNYlBnVmlIdGZHNTQ2VFdwZk5lTlcwRlhVVjB2WFpUbjFMMGFaWW1CZ0tBcGJlbHpKUW9iMVhHRC14LWVCWC1pZDl2UHFVendRR0tRY01IRDZZdFhqNEhVeTI3VHFhM09pTW52eDVLdVVGT1lqaXdMM2EwUVFmZ0NKUWlFaEs0cDFsR0JWMGE0VVU0d04xeVIyN2FoX1ZEOUFzQUVVZWx0Q1lUYjNGWkVWUV9JM2k4ZlNuQTczNDhnNUM0T3BHWFF6N1hR0gHPAUFVX3lxTE9SejFUc19GVEN6VzFiX0Z6MEcxdGVxQTVvMUxMUXdNQnowZlU4RGhZc1ppbW5UVUhSQlNmQTZpSFlhY2hlcW1MN2pjdlJvYi03ajFIalk1a3FUZG9QZTJoeDVVRlFqWHZ5Qmc3emxYWDdITUlYejdPR1F2ZlVZYzR3OF9yRVhuYjZ5U1RRUGNlMWNHZWdPZzJYWFZMYW82Szhodmt6QXlaZzhQZU5oQ1VMYWRPT2xmbndWRG15Q2F4cjkzclRDLXBTSDFhazNnMA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 22 Oct 2026 06:17:57 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報；感測器廠宇田控制明登興櫃；拓半導體量測/液冷商機- 新聞 - MoneyDJ理財網

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | -0.43 | -5.27% | +1.94% | 3,145.00 | 3,435.00 | -8.44% | 同向 | 75.13 | 41.92 | 21.02B TWD / 44.92% | 2026-10-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 1 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：跌停。

### 主要來源

- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 22 Oct 2026 20:51:30 GMT
- [感測器廠宇田控制明登興櫃；拓半導體量測/液冷商機- 新聞 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikgFBVV95cUxQNm5kbEMybzJCVXVjdVdOeEhDUGFpRmVqOXNoRjA5NXFjR1BNUGFnUzhXazRTeXRpRWhxRDZBekRzX19WYkxFVkpUaWhxVXlOdmlMb2ZuNWlaVDlsMVZBOXByb2NpLUI5cUFoMGxuSVBjWjdKeGluRU1EOUFsU0E1VHFGYVJrWUZveTlJTjJlalBRdw?oc=5) - Google News source discovery | MoneyDJ Thu, 22 Oct 2026 08:45:00 GMT

## 新興題材：OpenAI

摘要：新興題材：OpenAI 相關新聞集中在：External evaluators find flaws in OpenAI's AI monitoring system in pilot review - Reuters；OpenAI's most powerful AI models disabled their own safety monitoring — and one lied about it - CNBC；OpenAI to bring AI models to Google's cloud, in further expansion beyond Microsoft - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 新聞直接提及 | 0.00 | +15.73% | +5.91% | 521.08 | 532.95 | -2.23% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：新聞直接提及「OpenAI、Microsoft」，共 3 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [External evaluators find flaws in OpenAI's AI monitoring system in pilot review - Reuters](https://news.google.com/rss/articles/CBMisgFBVV95cUxPa2JvMy1McnRUdXBvVGlqSDhtMERqUGQyczh4TzJpTGFLX21ncWdQMXZOLW9YNW01b3hvWm1iWnVEQmtfQWowX1JRdzgzZFBlZVk4d0pxbFFnX3p0andwR09xWU9Fb2gtQ2hBZXI0QmlKZU1OWGlLQW1RdEtJTlM1WUVIdk15U0xQYU00eVl5UThUX2M3N0ZZOFJKM3R1RVF5RUpoTTRFZ05EQmw5WG8tS2ZB?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 22 Oct 2026 18:14:36 GMT
- [OpenAI's most powerful AI models disabled their own safety monitoring — and one lied about it - CNBC](https://news.google.com/rss/articles/CBMie0FVX3lxTE82c0lqMFI4dFFfLWhRZ0VZbW9LeFpaVDVTM3kwR3BzWFlST3o4ZXFqcVJVVF9BT2JRM0dFcFN0YWNCcUJjOUVkUUFDZVFidUwyTFM0cHBPVHAtRXk3a2hCYVU4VFJqeDhBckpWNVJ1RjFlVEs5R1pHNXRhMNIBgAFBVV95cUxQbEVjZjZVOEZHSm1UelVuSmxTYnRPTDE3NFB2ZHJFTjBrUnBtejdCWTRVb0JWcXVmNW90R2R1RTBsZWx3Qkw3NXhwU3EzUHhQQ0hDbFg0emFvUkhTNlV0dWJCZm5FMzJQdHpzNTJrSm9ZenhtY1VUTng4UFVPOXp6SQ?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 21 Oct 2026 07:03:48 GMT
- [OpenAI to bring AI models to Google's cloud, in further expansion beyond Microsoft - CNBC](https://news.google.com/rss/articles/CBMiqAFBVV95cUxNNXhvUlpRaDlhdjFIa3BDYy12MFBILU1vZFNfa0ZKUlV6cERUd1lVUWtEbEFVcTAxRlVuaGJFTENlYUtyOFloTlhRZ1QwTW5zOUd2UXFwT1pjS0FhX2NfT0R4MUJpNVZ6Z3ItZ05WRklZN2tSX2NUdkhsckYyM1FHbjM4Mi1WeTNvdUI5MkR0LXphNWs5UHFUZGxENXE4NWliZkdQeXR5eW7SAa4BQVVfeXFMTUhXVUF3ZHRsOGJpRnlGR2dKT2FWdk5oaW5zTzVJN1E5aEt5eGM4Wmtyei00T2F4dFBMSm5CWGR1WjYzU3BpVWpKUjdNZkltS3VzdkYyMDNMZWtCbnQwZHUtMVV5dTdmZF9tcVpnVW52aGlqNGJzNlJvaDJyZXRMR19QN293Tzk2NnV0NXVwUmxBUUx6TTA2aDMzaUlTc20zWFg2UkhfdnhCUnpnMm9R?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 21 Oct 2026 12:00:02 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：SanDisk Sinks 8% as Memory Selloff Deepens Ahead of Earnings; Western Digital Drops 7%, Micron Falls 6% - 24/7 Wall St.；Micron Is Up 221% in 2026 and Seagate Is Up 155%: Take Profits, or Hold On for the Ride? - 24/7 Wall St.；Nvidia Just Triggered The Next Memory And MICRON (MU) Rally! Tigers Vs Mets (X96Ngzrxdp) - Unisba Media

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | -11.79% | N/A | 856.49 | 971.00 | -11.79% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | +6.07% | -1.79% | 1,378.22 | 2,335.00 | -40.98% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.21 | -3.88% | +6.06% | 212.21 | 228.38 | -7.08% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、MU」，共 3 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：falls, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 1 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：falls, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：HBM。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [SanDisk Sinks 8% as Memory Selloff Deepens Ahead of Earnings; Western Digital Drops 7%, Micron Falls 6% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi2gFBVV95cUxQSjV0eWxjVUNrNUN5VnExQ0x2RXU5NUlrMVBlLV9jZ25IX1ozYmVVcUNHY0Jld04yODNMTEtERWstbGJhNWdJb1FXcDZFOHhtRWtTWUFwclY4WDRxQmxrWVRybTRxYzVCXzh2TjlRNkRrYUYtbG9SaTV0aUhBU1VWYkdnc0tfenFnc2ZORXNoY3FEcGhHeFJld2pXUzI2MmRHZjVxZHhYYnBMdHN5RnhHZUN3cGJwaU9CMEpGcWdnY0xId3plZEhydDZLd0dUTk16ZG1GTmoyemNBQQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 22 Oct 2026 17:58:00 GMT
- [Micron Is Up 221% in 2026 and Seagate Is Up 155%: Take Profits, or Hold On for the Ride? - 24/7 Wall St.](https://news.google.com/rss/articles/CBMixgFBVV95cUxQeXRXNWlnOURzcll1dVFxNzdKeUJzajBxbmJjUWVHbVM0bEV1dTRWck5hTjdaaXZrdTdVVEdWOUFyTDhSV1pCUTljdFpvS3EwQmdGQmxGeFpuQ0xjRzFMcFhLZTY4ODJVcTVqa2NxZHpXSVBJTVN3N1REZjZvd3AzRjVuOXdnRFY3alNCT3Rud3ZRM0lHZXFrd0VKYU1xcWRtc05uY3Nwc1RtQUFVVzM4TThZSFoxQ0FZTGtiekJDc3g0THctYkE?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 21 Oct 2026 18:54:00 GMT
- [Nvidia Just Triggered The Next Memory And MICRON (MU) Rally! Tigers Vs Mets (X96Ngzrxdp) - Unisba Media](https://news.google.com/rss/articles/CBMiggFBVV95cUxQemx3Z2R2dEFrZkR3N0I5aEwxekdxQjR1UVI2bzVJNDY4ekRLVlJxbHNYMnMtSTFQNDg0LTl5aU5lZ2dqWE1QWVhvQVp3MzBnaXF5cTZxTDk3UlJFa0xtdFVTakhwVHB2b19icGtJajBSVkxoaWZSdDZZc2hjQ2RoenRR?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 22 Oct 2026 11:09:17 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：【台股操盤人筆記】雜音頻傳，震盪中聚焦供應鏈龍頭 - MoneyDJ理財網；整理包／黃仁勳概念股笑了！輝達季度財報超預期 完整台廠供應鏈名單、潛在受惠股一次看 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.21 | -3.88% | +6.06% | 212.21 | 228.38 | -7.08% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +11.59% | +24.88% | 348.22 | 348.22 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | +2.30% | +2.30% | 245.00 | 289.00 | -15.22% | 不適用 | 15.21 | 16.15 | 1158.63B TWD / 38.42% | 2026-10-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [【台股操盤人筆記】雜音頻傳，震盪中聚焦供應鏈龍頭 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilwFBVV95cUxNSVNXQ3dxWWw4a2FVbU9GN3ZCSWtDVGFrUTV1NkVmc3JweVk1ZTdpY2FBV1JST09ER2lkbVFQMHdLQkRoaWMtYjQ0R2FQWVpwUGstMTZWdjNPSWdUVm92TGpOaTFrX08zSWRIQkM2UjNURkY5c1ZWUVBFNUlkSDJFQ3J5czBIbHdXUUpXdHdnUFFtX08ySHdn?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 22 Oct 2026 03:14:00 GMT
- [整理包／黃仁勳概念股笑了！輝達季度財報超預期 完整台廠供應鏈名單、潛在受惠股一次看 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBQUlViSHpPeDVlY29yaHFNNE5NcVlUQnE3ZThTcXRGNHgxYTVPOVVTRDlaTDV6Zml5WEwxVHNSeGFDcnVHUHhRSW15SzNpU0dYVDU3dThWNEVCbkZI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 21 Oct 2026 09:00:00 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：基金-FundDJ基智網 - MoneyDJ理財網；《台股盤後》開高走低、收跌846點，失守季線- 新聞 - MoneyDJ理財網；台股翻黑下殺 台幣早盤震盪走貶7.8分 - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [基金-FundDJ基智網 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikAFBVV95cUxPaElfMU13bmFIQXg3Y3NuOTR0OHVEWnNQT2dkT2MwVmpDX0s0UlpkZmIzZnNuamExVTFMbldTWG5uZXo0QWNoZ3p6RWY2aXV1UzBtRjczMjN3XzVMWHZ6YTFVaUpKVmo2ZkhzR29WNFVXUUZQb1lMdVlHbE1zQkxoWUxnOWhIa2NZX0R2alJGU1U?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 22 Oct 2026 17:41:57 GMT
- [《台股盤後》開高走低、收跌846點，失守季線- 新聞 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikgFBVV95cUxNeHR2R2g5VE52cEhmSndCTzc2M1pNZWFEYnkxSW5GVzJmM0IzX1hiNmUtNEtYVWNpaFYzbnlfSFpuZllwM0g4eUQyQXVlTzNJREtOdjBqb3pNcXIzWkwwUmJCZmJBa3dLeXRmdTRuTVlPQ3BGV2pZY1l1NmZkQlFlNlZhMzZmbHNXWGhyZTJSdmdqQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 22 Oct 2026 08:10:00 GMT
- [台股翻黑下殺 台幣早盤震盪走貶7.8分 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikgFBVV95cUxQTFFSOERNVXUxbklsV3BuNDlsSUZIeVdHazV3bm9pbjFLMzRBeUpjOFplY3MxZW1Zbjc5akNMX3oycHU4SFRoZTFCRThqckNOMXcxU00yZWpWY0ZoT2VGUVo5TG04dGtJMndhTHdzRFZjdXVsMEsxdkRiRXVOQ0pmc3QzNnE4QkN6NUdKR0F3MG51QQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 22 Oct 2026 04:35:00 GMT

## 新興題材：震盪中聚焦供應鏈

摘要：新興題材：震盪中聚焦供應鏈 相關新聞集中在：【台股操盤人筆記】雜音頻傳，震盪中聚焦供應鏈龍頭 - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [【台股操盤人筆記】雜音頻傳，震盪中聚焦供應鏈龍頭 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilwFBVV95cUxNSVNXQ3dxWWw4a2FVbU9GN3ZCSWtDVGFrUTV1NkVmc3JweVk1ZTdpY2FBV1JST09ER2lkbVFQMHdLQkRoaWMtYjQ0R2FQWVpwUGstMTZWdjNPSWdUVm92TGpOaTFrX08zSWRIQkM2UjNURkY5c1ZWUVBFNUlkSDJFQ3J5czBIbHdXUUpXdHdnUFFtX08ySHdn?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 22 Oct 2026 03:14:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
