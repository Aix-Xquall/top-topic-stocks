# 每日股市熱門話題分析 - 2026-07-29

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **AI 伺服器與資料中心**｜負向｜熱度 15｜市場確認 86.11｜同向 5/6
2. **記憶體與 HBM 供應鏈**｜負向｜熱度 14｜市場確認 100.00｜同向 1/1
3. **綜合市場情緒**｜負向｜熱度 40｜市場確認 N/A｜同向 0/0
4. **半導體與晶片供應鏈**｜負向｜熱度 7｜市場確認 100.00｜同向 5/5
5. **新興題材：TradingKey**｜負向｜熱度 2｜市場確認 100.00｜同向 1/1

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.16（樣本 13）
- 5日相關係數：-0.03（樣本 13）
- 同向比例：12/13

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| AI 伺服器與資料中心 | 86.11 | 5/6 | 0 | +9.26% | +2.31% |
| 記憶體與 HBM 供應鏈 | 100.00 | 1/1 | 0 | +31.93% | +31.04% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | 100.00 | 5/5 | 0 | +15.32% | +3.20% |
| 新興題材：TradingKey | 100.00 | 1/1 | 0 | +31.93% | +31.04% |
| 散熱與液冷供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：全球晶片 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-07-16 | 0.20 | 0.02 | +33.33% | 12 |
| 2026-07-17 | 0.36 | 0.02 | +60.00% | 15 |
| 2026-07-18 | 0.18 | 0.08 | +53.85% | 13 |
| 2026-07-19 | 0.37 | 0.09 | +12.50% | 16 |
| 2026-07-20 | -0.59 | 0.11 | +45.45% | 11 |
| 2026-07-21 | -0.12 | -0.03 | +12.50% | 8 |
| 2026-07-22 | -0.33 | -0.15 | +16.67% | 6 |
| 2026-07-23 | -0.01 | 0.01 | +41.67% | 12 |
| 2026-07-24 | -0.16 | 0.43 | +50.00% | 6 |
| 2026-07-25 | 0.30 | -0.06 | +12.50% | 16 |
| 2026-07-26 | 0.38 | 0.06 | +23.53% | 17 |
| 2026-07-27 | 0.54 | 0.11 | +37.50% | 8 |
| 2026-07-28 | 0.32 | 0.13 | +36.36% | 11 |
| 2026-07-29 | 0.16 | -0.03 | +92.31% | 13 |

## 歷史回測摘要

- 回測日期：2026-07-29
- 近5日 3日相關：-0.64
- 近5日 5日相關：-0.30
- 同向比例：+100.00%
- 權重狀態：未調整

- 方向準確度：+100.00%
- 信心排序準確度：-0.64
- 診斷：信心校準問題

調整原因：近 5 日有效樣本 13 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：AI 伺服器與資料中心 相關新聞集中在：AMD vs. Intel: Which Is the Better Artificial Intelligence Chip Stock to Own Until the End of 2027? - The Motley Fool；AMD Sinks 8%, Marvell Sinks 7%, Intel Fall 6% as AI Chip Trade Narrows to NVIDIA - 24/7 Wall St.；Intel Stock And 2 AI Infrastructure Picks Retail Investors Are Researching - simplywall.st

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.57 | N/A | N/A | 86.30 | 114.68 | -24.75% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | -0.57 | -6.69% | +12.96% | 197.01 | 211.14 | -6.69% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.57 | N/A | N/A | 454.62 | 516.10 | -11.91% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.06 | -5.20% | -5.39% | 2,280.00 | 2,410.00 | -5.39% | 同向 | 74.39 | 30.65 | 442.68B TWD / 67.87% | 2026-07-01 |
| MSFT 微軟 | 產業/供應鏈推估 | -0.03 | +0.16% | -22.37% | 393.35 | 506.69 | -22.37% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -14.74% | +23.07% | 380.91 | 446.77 | -14.74% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.04 | -14.64% | -12.48% | 554.00 | 680.00 | -18.53% | 同向 | 10.86 | 51.44 | 65.78B TWD / 32.86% | 2026-07-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.04 | -14.45% | -9.67% | 3,315.00 | 4,310.00 | -23.09% | 同向 | 62.91 | 52.83 | 58.01B TWD / 2.80% | 2026-07-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 3 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA、輝達」，共 2 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AMD vs. Intel: Which Is the Better Artificial Intelligence Chip Stock to Own Until the End of 2027? - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxOZmlRRXNPT0RKTDhibkh2X0o3ejZGY2FQak8tNzVNclhuQllGRzNzTUNxUnV4TFRkR1ZtVHBBcjVpaVZvQ1pLQlN0VFg4VTRkT2tPc1VydTBrR0tUZmN0STFJckhxa3dCRnU1ZmtOejJaYjVUVnBtZXptUTVRdmpRazI3U1NTZEpEcENSTGlRWGNjNGlGVGJ1WQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 28 Jul 2026 14:49:00 GMT
- [AMD Sinks 8%, Marvell Sinks 7%, Intel Fall 6% as AI Chip Trade Narrows to NVIDIA - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiuwFBVV95cUxOWUhyTWJxaWVIZm96VnByUUhnc1hxVS1fR3BQLVVpLVZKMWUySWQ4d0pnd1ZxWG45R3FzdzF5U0dKUERJTU5IZl8xOWp3eFA2c2laMm9JeWpQc05mNW4wek1raExUbGRCS0tYNVAtbzFLODBJS0VLSFBmQnJPUTlROUZBYUdjbDNIdHdDM3FkZEkyb1I3XzYyOXFwNUNHYUhQZmE2RENlLWRTcHJxSTdWLU9jRzBHUnVJZmVV?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 28 Jul 2026 15:28:43 GMT
- [Intel Stock And 2 AI Infrastructure Picks Retail Investors Are Researching - simplywall.st](https://news.google.com/rss/articles/CBMiygFBVV95cUxOV3YwLUhjZk9CVEtncHY2X3JlenhJZk9GX1JObWo1SDJzNFQ3b3Nob1RDNE1qWEVFOFc1UVhFcmZUU2VmbjU5SW5DOTJ2eFZaZnZER2Y2dVM0SER4b2N6Qll0UWtXNWlkQ3FkZDU3aWJFSlltbF80SFlSb3pORm13SmlVZjRQLU1heUdsa3RtTWxwaVB6YzBCYXRDYWpLdTVnbUxpdUhYUTNkNmg0cVl1aHpVY1Uxa1NRTGtCWkExZS11S216TWtabURR?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 27 Jul 2026 03:33:34 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：半導體、記憶體 台股重災區 台積、南亞科等合計市值一天少3兆 - 經濟日報；3 AI Chip and Memory Behemoths to Buy Ahead of August for Big Upside - TradingView；US Chip Stocks Slump Pre-Market: Micron Falls Over 5%, AMD and Intel Drop More Than 4% - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | -0.48 | N/A | N/A | 820.53 | 971.00 | -15.50% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.48 | -31.93% | -31.04% | 1,096.10 | 2,335.00 | -53.06% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.36 | N/A | N/A | 454.62 | 516.10 | -11.91% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | -0.36 | N/A | N/A | 86.30 | 114.68 | -24.75% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -6.69% | +12.96% | 197.01 | 211.14 | -6.69% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「memory、Micron」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [半導體、記憶體 台股重災區 台積、南亞科等合計市值一天少3兆 - 經濟日報](https://news.google.com/rss/articles/CBMieEFVX3lxTFBXS2xBUGtPMUxiSzNEZmZwWVhLUkh6MElvMmNPSG40SWZKUmpGc0xYLUE3TEhxYUdFS3ZiaUJ5SEtvN0p2dnV1ajR3N21UelBpNVdBZFJGYjBYOVlqeV9lMlhZdXU2a2ttY3h4TzkwT19hLWhMYnBjYtIBX0FVX3lxTE1YNzRHeUUwREhFeXg2QURMbm5qNkU4cUtMeGgxQmJmNTRLMlVCVVlSQzFWRnR5c2ltYWN0R09vQWRycjhiNE1IVjhCV2loT01Wc0xDemdhTGRXZ0NnbFJr?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 27 Jul 2026 09:00:00 GMT
- [3 AI Chip and Memory Behemoths to Buy Ahead of August for Big Upside - TradingView](https://news.google.com/rss/articles/CBMiwgFBVV95cUxPdUF5cWw1UmZRNTg0Vk5WdU4yVFVxRmFrYURzdDNrZElwekVaVnJlYzVOV25aRXlGeHZlNldUSmlwV1p0VFZqX1IwWmU0cUJWU0RBSFFKeDJONi1PRlhJR3UwUE1VVmI5OW9pemQ4NlB3b0VnSUoyUS01QVNOQ2tqYkVydEZKaWhRU01mUy03QkppWFIzd1hCQUFWd0ZjUWlKU0lkS0lHUW5Kc0ZIZDRnZm1FMTFZV1RzNnZabE5zV2gtQQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 28 Jul 2026 12:00:00 GMT
- [US Chip Stocks Slump Pre-Market: Micron Falls Over 5%, AMD and Intel Drop More Than 4% - TradingKey](https://news.google.com/rss/articles/CBMi3wFBVV95cUxNTG51Z2N1OGIyZllqMXpBYzAtVVJTci1xMzM5UGlDcjR5YXR5NFFGckI5bGU1MmVpbmZ4cXl2SFJadzEweHNvOUN1eUFwaEYzcTVZT21UbFVhNV83NDVsSVlTQnN0ZmQ5aDlvdUJpMUxnVnlNLXhJa1lwMlh2eGxPUkJGY2RNMzFTNUJvcWFnUlZ4cEE5QkJRb2VvQnY3YXlKM2JxSXh3WjVEVjdfb0s1bFNMRGVWV1NzbHczQUticEZXNEd6cC1TbG9pdUR4dTYtclkyWENHV1FhTmxKNUhz?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 28 Jul 2026 08:56:51 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股回檔爆槓桿危機！929檔「融資告急名單」熱門族群個股曝光 - 經濟日報；台股再殺2,030點 跌點寫史上第三大、季線有效跌破 - 經濟日報；台股 ETF 法人喊低接 大盤單日跌逾1,500點 30日後平均漲8.3% | 基金天地 | 理財 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.42 | N/A | N/A | 86.30 | 114.68 | -24.75% | N/A | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [台股回檔爆槓桿危機！929檔「融資告急名單」熱門族群個股曝光 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1pRXdBUkNhamxfaU5ianlPS2RfdklXYTZaTm1IZEc0NFRDaF93RE9BUnNJQzNVdjFDd0Z3ZmpHSnYzQ3ZPUlpJTThrTWdwYXV2bEtkOXZiUW01QdIBX0FVX3lxTE0wWE9rYzBmWlNETXVFYlMyNVZkeWZHYU81Rll5RlptbWVpTDdiaG40eG95ZUx2N2UwYVpxeHgyUkt5bXlpeGNpZ3FaWTRtc0tZd2taN3RuY1V2T2RLSURn?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 27 Jul 2026 09:00:00 GMT
- [台股再殺2,030點 跌點寫史上第三大、季線有效跌破 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBDWWhKTnZDWGZPUUR6alhsbzBwOHRfUXpzMkNtcHBnbjBzQ191NE16ZTVldUdDUmdIc1dnZ3loTERPY3ptUndxMlB6SVdMSWNLdy1ISkZPbnIzZ9IBX0FVX3lxTE9Ec1BkekNhRGtoRTdEaXhzemtZeUo0b2M0bVota3I3UVJiWnZta3ZCWXhHQzQ4SXgwQVFUUjVDSG9BZHh1RFFNSGtIcHN2WjU2cklDdFNCZldlRWVnano0?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 27 Jul 2026 09:00:00 GMT
- [台股 ETF 法人喊低接 大盤單日跌逾1,500點 30日後平均漲8.3% | 基金天地 | 理財 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBnUjFBZWxjam83cjZ1RHMzNWJnLUZaNURfdGNMc2hNdUY4UmRtcndXSlpZM1BDdzFSSUh1ZV90TnFiNmczVHE2eHVicVUxV1NRUkQ3aTN2RHFGUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 28 Jul 2026 15:53:03 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：AMD vs. Intel: Which Is the Better Artificial Intelligence Chip Stock to Own Until the End of 2027? - The Motley Fool；AMD Sinks 8%, Marvell Sinks 7%, Intel Fall 6% as AI Chip Trade Narrows to NVIDIA - 24/7 Wall St.；內鬼抓到了！涉嫌走私輝達高階 AI 晶片至中國，輝達經理羈押禁見 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.57 | N/A | N/A | 86.30 | 114.68 | -24.75% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | -0.56 | -6.69% | +12.96% | 197.01 | 211.14 | -6.69% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.56 | N/A | N/A | 454.62 | 516.10 | -11.91% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.05 | -5.20% | -5.39% | 2,280.00 | 2,410.00 | -5.39% | 同向 | 74.39 | 30.65 | 442.68B TWD / 67.87% | 2026-07-01 |
| 2303 聯電 | 產業/供應鏈推估 | -0.05 | -18.05% | -15.61% | 113.50 | 164.50 | -31.00% | 同向 | 4.00 | 28.52 | 23.12B TWD / 22.85% | 2026-07-01 |
| MU 美光 | 產業/供應鏈推估 | -0.04 | N/A | N/A | 820.53 | 971.00 | -15.50% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | -0.04 | -31.93% | -31.04% | 1,096.10 | 2,335.00 | -53.06% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -14.74% | +23.07% | 380.91 | 446.77 | -14.74% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA、輝達」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AMD vs. Intel: Which Is the Better Artificial Intelligence Chip Stock to Own Until the End of 2027? - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxOZmlRRXNPT0RKTDhibkh2X0o3ejZGY2FQak8tNzVNclhuQllGRzNzTUNxUnV4TFRkR1ZtVHBBcjVpaVZvQ1pLQlN0VFg4VTRkT2tPc1VydTBrR0tUZmN0STFJckhxa3dCRnU1ZmtOejJaYjVUVnBtZXptUTVRdmpRazI3U1NTZEpEcENSTGlRWGNjNGlGVGJ1WQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 28 Jul 2026 14:49:00 GMT
- [AMD Sinks 8%, Marvell Sinks 7%, Intel Fall 6% as AI Chip Trade Narrows to NVIDIA - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiuwFBVV95cUxOWUhyTWJxaWVIZm96VnByUUhnc1hxVS1fR3BQLVVpLVZKMWUySWQ4d0pnd1ZxWG45R3FzdzF5U0dKUERJTU5IZl8xOWp3eFA2c2laMm9JeWpQc05mNW4wek1raExUbGRCS0tYNVAtbzFLODBJS0VLSFBmQnJPUTlROUZBYUdjbDNIdHdDM3FkZEkyb1I3XzYyOXFwNUNHYUhQZmE2RENlLWRTcHJxSTdWLU9jRzBHUnVJZmVV?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 28 Jul 2026 15:28:43 GMT
- [內鬼抓到了！涉嫌走私輝達高階 AI 晶片至中國，輝達經理羈押禁見 - TechNews 科技新報](https://news.google.com/rss/articles/CBMibEFVX3lxTE03aG84VlhQNENYMFJ0TFlrT3Z4bE9RTlFSWVgzbUpsOERlaFp3ckN2RWZmX2VGa3NRZmxMWVdWbU5ZN2FWdUFNTEFnQk9RcGNLR21VZDRXSXRmWDRIZlAwYlU1bTZOdUJaODM0SQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 28 Jul 2026 08:53:21 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：US Chip Stocks Slump Pre-Market: Micron Falls Over 5%, AMD and Intel Drop More Than 4% - TradingKey；SanDisk Stock Price Forecast: Chinese Manufacturers May Rapidly Break DRAM and NAND Industry Barriers; Shares to Fall Below $1,100? - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | -0.49 | N/A | N/A | 820.53 | 971.00 | -15.50% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.42 | N/A | N/A | 454.62 | 516.10 | -11.91% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | -0.42 | N/A | N/A | 86.30 | 114.68 | -24.75% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.42 | -31.93% | -31.04% | 1,096.10 | 2,335.00 | -53.06% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、DRAM」，共 2 篇新聞命中。 方向判斷命中詞：fall, falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [US Chip Stocks Slump Pre-Market: Micron Falls Over 5%, AMD and Intel Drop More Than 4% - TradingKey](https://news.google.com/rss/articles/CBMi3wFBVV95cUxNTG51Z2N1OGIyZllqMXpBYzAtVVJTci1xMzM5UGlDcjR5YXR5NFFGckI5bGU1MmVpbmZ4cXl2SFJadzEweHNvOUN1eUFwaEYzcTVZT21UbFVhNV83NDVsSVlTQnN0ZmQ5aDlvdUJpMUxnVnlNLXhJa1lwMlh2eGxPUkJGY2RNMzFTNUJvcWFnUlZ4cEE5QkJRb2VvQnY3YXlKM2JxSXh3WjVEVjdfb0s1bFNMRGVWV1NzbHczQUticEZXNEd6cC1TbG9pdUR4dTYtclkyWENHV1FhTmxKNUhz?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 28 Jul 2026 08:56:51 GMT
- [SanDisk Stock Price Forecast: Chinese Manufacturers May Rapidly Break DRAM and NAND Industry Barriers; Shares to Fall Below $1,100? - TradingKey](https://news.google.com/rss/articles/CBMi7AFBVV95cUxPV1ZQNWM0X2k5aTNIZjVzLW9BY3VaVXg2UUtSLTlReFVxZnZiZ1FmMndxTUZRcmk4NUI5YTZYRWc5OTM3TW90aldTaHlnYU1wYU9FYjN1UzNoVkF0MWR0cmNHbVh1V2YtYjNINGF6SjF6S1NyRGtNYU03bWl3azhzalZCWFZDU2F4cS1ybXRxSUpHdGRyR1hLdVRPdS11T1B1ZnNJb2RQVUJsLWQ4akJteGpSVlEzSUtLcFdDQTFSNENFOG1QdFg0cnlHSEJJSXBmRVVLbWRWUTJ1SmNaYTRFSG9jRVJfOVY5V2J0RQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 27 Jul 2026 15:26:35 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：AI主流趨勢沒變！奇鋐、台燿獲看好 水冷產能暴增5倍、Q3營收續衝高 - Yahoo股市

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | -8.20% | -3.45% | 2,240.00 | 2,835.00 | -20.99% | 不適用 | 61.06 | 36.81 | 17.62B TWD / 66.11% | 2026-07-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐」，共 1 篇新聞命中。 同時符合主題標籤：thermal。

### 主要來源

- [AI主流趨勢沒變！奇鋐、台燿獲看好 水冷產能暴增5倍、Q3營收續衝高 - Yahoo股市](https://news.google.com/rss/articles/CBMikwNBVV95cUxQNTlLTU53RVE0T0N2ZXMxVGJCSlhKMktZal9jeEluYWtNVzlaeFhPM1o3S01Fc01sampMOGMwQUNfRS1vQk42am5PU2YxNWFJLUZoNi16WnFoMTB0Z1h5QXQ0M0pLc1l3dXduQlhSMExmek15endUNDFadi1YNjNEcW42ZWlJOTFPWENmSHRWN3hyV2w1TnNWUnZORHlWLWxPNjhva0xSMUdzQ2RuWjFQLTVPclpCTTJBYkc5YWxPUWNtUWZSYjVWaURJS2trcm15YzlvdGdyTndCM1BoOGZVM1ZFei1oeVdFQXI3LUpCQVR3MmJRdnlfS0VPaVBXVlJIVFhacnI1OWs4ZnpmeFJuWmd3WkdINDItVk9naW5fX2dtWGdRallJcmQtMF9lcHVoOGNEYkJDcVYwN29RdEZMQzl2VFYtME9hSnNMek1wNWsxYUszcWcxR1MtUXhHNjNhYlhFMWthdlpJWE0zMzZUWDBRcU9uTThYV3hLSUEzUW5mOVE0aTZfYU5xUHFUek1JQkRF?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 27 Jul 2026 03:02:26 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》重挫2030點/失守42K 創收盤第3大跌點- 新聞 - MoneyDJ；台股雪崩！收盤狂殺2030點「失守42K」 成史上收盤第3大跌點- 新聞 - MoneyDJ；個股動態報導內容-B1A922F2-91DA-4288-BCBD-53895DD4BB0B - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》重挫2030點/失守42K 創收盤第3大跌點- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQQzNNRGltaHpiZ0pteXkzT1h6R29Ib3JwbDBkdFBmQ3hZUVdoTUlDYU1LUXo4NGtDR0s2akJzSmk3MzMxeVQtZ1RDTS0zd1plOXBQQUpXVWxUdDNOQm1MUWxzcUx6TDNTV3E5Nlhyc01mNUxnMVo3VkxnLUhWNnZjNFNkNEtqS0ZYRng1VUZkMmcwZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 28 Jul 2026 07:36:00 GMT
- [台股雪崩！收盤狂殺2030點「失守42K」 成史上收盤第3大跌點- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPOXFMMG81Rmt3dlFXTjY4blF4YUk5TDNvOU00ZDk0eHVJN2d2eVk4UF9OLTZlbnAtQjFvRGpKVi1BaV9tUlVPTUJQWjI0ZU81eXNHczdLdC1hVE13YlZSNGE0YWs5WW1ZbDJjM3lJelYzYVJGUTN6VUpfUXRITG03VXBJM3luZFh4NnRGNTNZOUgzUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 28 Jul 2026 06:43:00 GMT
- [個股動態報導內容-B1A922F2-91DA-4288-BCBD-53895DD4BB0B - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxOXzZldU9xY2FfaTI1djRUT2d5d3c0WG5lRVliOHlMYnR2VVNBTDFXVkkyTlV6WW5VSi1sLVQwN255T0w5NXU4OVB6OWxPN0N3VFFpNm5GaVgzUGs1dDlYQWJNRERMd1pGUnViNVVpZDFtS1NnM3hyRlFLQnpPM1Zhdi1qOEVyWjhwdElWZ0U2dHM3dlM3?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 28 Jul 2026 11:00:25 GMT

## 新興題材：全球晶片

摘要：新興題材：全球晶片 相關新聞集中在：全球晶片股跳水 台股重挫2,030點 止跌緊盯三個訊號 - 經濟日報；〈美股盤後〉油價下滑 道瓊漲逾500點 全球晶片股慘遭血洗 費半狂瀉近5% - news.cnyes.com

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [全球晶片股跳水 台股重挫2,030點 止跌緊盯三個訊號 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5KVFF3a0dmT0swSEZEYTRrLVQza3BoclJXem1TVkJma3Fhd3NHUTBtZmh4QzlrVkluenQwTWMtUXhWZ29QdzNLOGlLTFQ4dEJxQncwdWdqTTgzd9IBX0FVX3lxTE5mMkhWNlE3M2NBbDdYeVVCQVRzVlFwRFhfNlFYZDJxMVFjMDEzU2pDa0hXQ25mbk15SlZGUzg1ekJnZlVXVzdySk1iSkJtNkxBRG0wZ2VQTHZpaVgtM0xV?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 28 Jul 2026 17:39:47 GMT
- [〈美股盤後〉油價下滑 道瓊漲逾500點 全球晶片股慘遭血洗 費半狂瀉近5% - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTE5yNkdaOFZhWVpZeEdRallIR3IzMWhJQ2NHR2U1OFFCUzU0SEpMaUMwTmZiSlh1QUFKOVVxQlBVZy1qdEZaMVJfMVMxekdxdjA?oc=5) - Google News source discovery | 鉅亨網 Tue, 28 Jul 2026 21:56:16 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
