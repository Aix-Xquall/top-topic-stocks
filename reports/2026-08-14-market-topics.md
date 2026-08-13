# 每日股市熱門話題分析 - 2026-08-14

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜正向｜熱度 11｜市場確認 100.00｜同向 1/1
2. **AI 伺服器與資料中心**｜正向｜熱度 12｜市場確認 87.38｜同向 5/6
3. **半導體與晶片供應鏈**｜正向｜熱度 7｜市場確認 100.00｜同向 5/5
4. **散熱與液冷供應鏈**｜正向｜熱度 5｜市場確認 100.00｜同向 2/2
5. **新興題材：TradingKey**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.34（樣本 14）
- 5日相關係數：0.57（樣本 14）
- 同向比例：13/14

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 100.00 | 1/1 | 0 | +23.44% | +21.42% |
| AI 伺服器與資料中心 | 87.38 | 5/6 | 0 | +9.68% | +4.50% |
| 半導體與晶片供應鏈 | 100.00 | 5/5 | 0 | +10.04% | +7.97% |
| 散熱與液冷供應鏈 | 100.00 | 2/2 | 0 | +14.16% | +10.87% |
| 新興題材：TradingKey | N/A | 0/0 | 0 | N/A | N/A |
| 關稅與供應鏈轉移 | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：AI需求帶領台灣供應鏈 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-08-01 | 0.38 | 0.25 | +54.55% | 11 |
| 2026-08-02 | 0.06 | -0.21 | +33.33% | 9 |
| 2026-08-03 | 0.35 | -0.49 | +60.00% | 5 |
| 2026-08-04 | 0.05 | -0.08 | +46.15% | 13 |
| 2026-08-05 | -0.39 | 0.44 | +64.29% | 14 |
| 2026-08-06 | 0.07 | 0.33 | +50.00% | 12 |
| 2026-08-07 | -0.22 | -0.17 | +50.00% | 8 |
| 2026-08-08 | 0.72 | 0.45 | +62.50% | 16 |
| 2026-08-09 | -0.39 | 0.46 | +71.43% | 7 |
| 2026-08-10 | -0.09 | 0.74 | +71.43% | 7 |
| 2026-08-11 | 0.57 | -0.18 | +54.55% | 11 |
| 2026-08-12 | 0.52 | -0.47 | +87.50% | 8 |
| 2026-08-13 | 0.72 | 0.24 | +100.00% | 7 |
| 2026-08-14 | 0.34 | 0.57 | +92.86% | 14 |

## 歷史回測摘要

- 回測日期：2026-08-14
- 近5日 3日相關：N/A
- 近5日 5日相關：N/A
- 同向比例：N/A
- 權重狀態：未調整

- 方向準確度：N/A
- 信心排序準確度：N/A
- 診斷：樣本不足

調整原因：近 5 日有效樣本 0 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：MSCI 季調出爐！台股在全球標準指數「6進6出」 記憶體3檔入列 - 經濟日報；Can Micron's AI Memory Focus Help It Outpace SK Hynix and Sandisk? - The Globe and Mail；Memory Stocks Stay Strong With Sandisk, SK Hynix, and Western Digital Leading the Storage Stack - 24/7 Wall St.

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.48 | N/A | N/A | 949.83 | 971.00 | -2.18% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.48 | +23.44% | +21.42% | 1,528.11 | 2,335.00 | -34.56% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +12.60% | +12.89% | 225.30 | 225.30 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、memory、MU」，共 4 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally, strong。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 4 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：rally, strong。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [MSCI 季調出爐！台股在全球標準指數「6進6出」 記憶體3檔入列 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBpNk9GOFpTeUFoUTNCV2k1OFg1djNkZTRDUTJ1Q3BpU1FvbU12UW1wVkh6SHdsTTJ6MHZ6eW1mcG9HVG8xZTFNZ096ZXhwZDE2a0NBMnNVS2NSd9IBX0FVX3lxTE1uVVpFMkZ1d2FzVFFxdl9ZZlUzNzRwTVo1dXZ6QTRkcXRWMWktZDJ2OUtiU1V6M2MwNWZ2aUFjZFZLb2dkMEFpcHpTQ1lLZ0t4UjlRbWNncEQ5RmoteXRv?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 12 Aug 2026 09:00:00 GMT
- [Can Micron's AI Memory Focus Help It Outpace SK Hynix and Sandisk? - The Globe and Mail](https://news.google.com/rss/articles/CBMi4AFBVV95cUxOVFN2YnNZamxqZlNYSEZZckFzNU0zNFdHXzFFV0k3NG4wam1VUXlJclRySzBYOTZ4Ykk2WTZfRjFOYTVHNGE2clVGNHgzYzdhS0htcDNOVlN2bUVIWEI3OFcxZE5LZ0xrbmhiTXNBNG16VUZfbWNvTG5tcjNxVWJKcG1jSUVlWG94bHdBRENoTk9zWjFsbnpqc1lXNUwtY1RzNWhSTTBMek9XVDh1QnYwa3RVal9YS2JvRjVnVlZDOHhWejY4WXhZclZWVVdTdWZOaXpNTndlWHpRdzFIdF9nTQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 13 Aug 2026 15:46:44 GMT
- [Memory Stocks Stay Strong With Sandisk, SK Hynix, and Western Digital Leading the Storage Stack - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi0wFBVV95cUxOWS14RVc3RjlBZjljcGVqRE9yaFBlSnZIMUZhNHRPOXJVc3FHMEtWbmZTY0hfaW9DdkNQbWM4OEN0em8zMHFYZ0V0aGg4NVR5aElneE5OT2VUU21mLWRuSmh1S2xhU1V1UVMxYzg0bjNBb095WjFVZ1k3UVVWS0NrbnUyOVUtR0Vmc2E2SUhKVlVpNDd2RHJGYlJ1ZDEtOUZoNDc2S3ZUODhIZTBuQmNlb2xRbGhiSnoxNm9WTlNVaks5UVFHZEJCN0drNnlqeDZvSDln?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 13 Aug 2026 19:11:49 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：AMD, Intel, and NVIDIA All Rally Wednesday After Series of Blockbuster AI Earnings Reports - Yahoo Finance；Intel stock holds at $100.95 amid mixed signals on foundry profits and AI growth potential. - Pluang；AI Chip Stocks August 2026: Nvidia vs AMD Investment Analysis - intellectia.ai

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.57 | +12.60% | +12.89% | 225.30 | 225.30 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.57 | N/A | N/A | 104.56 | 114.68 | -8.82% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.57 | N/A | N/A | 483.01 | 516.10 | -6.41% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.06 | +2.31% | +2.96% | 2,435.00 | 2,435.00 | 0.00% | 同向 | 74.39 | 32.74 | 467.58B TWD / 44.69% | 2026-08-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | +26.52% | -1.94% | 496.88 | 506.69 | -1.94% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.04 | +10.61% | +0.09% | 417.82 | 446.77 | -6.48% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.03 | -0.63% | +5.21% | 626.00 | 680.00 | -7.94% | 未明確 | 13.92 | 45.30 | 73.78B TWD / 43.15% | 2026-08-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.04 | +6.69% | +7.78% | 4,225.00 | 4,310.00 | -1.97% | 同向 | 60.69 | 69.78 | 48.47B TWD / 12.16% | 2026-08-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 2 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。 方向判斷命中詞：growth, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 2 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：growth, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。 方向判斷命中詞：growth, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AMD, Intel, and NVIDIA All Rally Wednesday After Series of Blockbuster AI Earnings Reports - Yahoo Finance](https://news.google.com/rss/articles/CBMinAFBVV95cUxOZmFXZU54TWRFd1lrUzdXdGN1VkhlUFhwUnZzeldWVnpUY3pmUFJWeWItU0JZZFNCZ1M3b2Jqa3BGRUJlVy1WUFVmbTE0MUNZaVhPSHNnaEs3M2tjRlBjSjlYb2xjOXZVS1YwWFloc3JGMGdfcnRTUTBsQUJncUpseWI1YzNLY2NFRVZyNnZaQ3YyOGt1WkF0ZGJXWnA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 12 Aug 2026 22:21:27 GMT
- [Intel stock holds at $100.95 amid mixed signals on foundry profits and AI growth potential. - Pluang](https://news.google.com/rss/articles/CBMif0FVX3lxTE1kbWltaDVmbmZ5M3NJWm1tYVV3N1pMY3JNaGhpbklQSXZZazM2S2xZeHhkV1RYVkl5S0F1Y1Vkak94eGxjamduMzFmTEUzeEVkOEVvTHoyblN4WmFoUTV5ZXBudlRIZW91WmdYWE5vaW9TaTREYnhPVFVnZ0lCVmM?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 13 Aug 2026 13:57:29 GMT
- [AI Chip Stocks August 2026: Nvidia vs AMD Investment Analysis - intellectia.ai](https://news.google.com/rss/articles/CBMiZEFVX3lxTE9hNjg3V1lHY296SVZIMmVNRDE2X3FDQXdNS1dabXhFcFR5X3hNQWhiVm9KSkM0QjN0dW9USmZkaGwzOUp0RnBEYjV2T3l0TnB5SG81QXpNeE9RR1VIenBKSHNEN0g?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 13 Aug 2026 00:10:51 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel stock holds at $100.95 amid mixed signals on foundry profits and AI growth potential. - Pluang；AI Chip Stocks August 2026: Nvidia vs AMD Investment Analysis - intellectia.ai；漢測上半年獲利增近3.9倍 AI半導體擴產帶動晶圓測試| 證券 - cna.com.tw

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.52 | N/A | N/A | 104.56 | 114.68 | -8.82% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.46 | +12.60% | +12.89% | 225.30 | 225.30 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.46 | N/A | N/A | 483.01 | 516.10 | -6.41% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.05 | +2.31% | +2.96% | 2,435.00 | 2,435.00 | 0.00% | 同向 | 74.39 | 32.74 | 467.58B TWD / 44.69% | 2026-08-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.05 | +1.22% | +2.47% | 124.50 | 164.50 | -24.32% | 同向 | 6.68 | 18.72 | 23.84B TWD / 18.98% | 2026-08-01 |
| MU 美光 | 產業/供應鏈推估 | +0.04 | N/A | N/A | 949.83 | 971.00 | -2.18% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.04 | +23.44% | +21.42% | 1,528.11 | 2,335.00 | -34.56% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.04 | +10.61% | +0.09% | 417.82 | 446.77 | -6.48% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel stock holds at $100.95 amid mixed signals on foundry profits and AI growth potential. - Pluang](https://news.google.com/rss/articles/CBMif0FVX3lxTE1kbWltaDVmbmZ5M3NJWm1tYVV3N1pMY3JNaGhpbklQSXZZazM2S2xZeHhkV1RYVkl5S0F1Y1Vkak94eGxjamduMzFmTEUzeEVkOEVvTHoyblN4WmFoUTV5ZXBudlRIZW91WmdYWE5vaW9TaTREYnhPVFVnZ0lCVmM?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 13 Aug 2026 13:57:29 GMT
- [AI Chip Stocks August 2026: Nvidia vs AMD Investment Analysis - intellectia.ai](https://news.google.com/rss/articles/CBMiZEFVX3lxTE9hNjg3V1lHY296SVZIMmVNRDE2X3FDQXdNS1dabXhFcFR5X3hNQWhiVm9KSkM0QjN0dW9USmZkaGwzOUp0RnBEYjV2T3l0TnB5SG81QXpNeE9RR1VIenBKSHNEN0g?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 13 Aug 2026 00:10:51 GMT
- [漢測上半年獲利增近3.9倍 AI半導體擴產帶動晶圓測試| 證券 - cna.com.tw](https://news.google.com/rss/articles/CBMiXkFVX3lxTE9ZTVZkZkNGMklFczZjV0F5RTdSYlpCODZTRWdLYVZ0THQ2aTdJWTFjZUY0QkRpenBhTURMaVdKNDJGbE9FaWV4bXFLRlg5bE1KblhnMlh4SG5pLWlycUE?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 13 Aug 2026 09:59:00 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：上半年EPS飆44元！「散熱大廠」Q2獲利翻倍創高 輝達Rubin、ASIC第四季放量業績季季漲 - FTNN 新聞網；焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報；AI伺服器液冷滲透率攀升 奇鋐估2027年達5成 - digitimes.com.tw

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.57 | +15.73% | +8.84% | 3,200.00 | 3,200.00 | 0.00% | 同向 | 75.13 | 42.66 | 18.59B TWD / 57.39% | 2026-08-01 |
| NVDA 輝達 | 新聞直接提及 | +0.42 | +12.60% | +12.89% | 225.30 | 225.30 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱、奇鋐」，共 5 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：跌停, 放量, 創高, 噴漲, 漲停。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：放量, 創高。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [上半年EPS飆44元！「散熱大廠」Q2獲利翻倍創高 輝達Rubin、ASIC第四季放量業績季季漲 - FTNN 新聞網](https://news.google.com/rss/articles/CBMiS0FVX3lxTE5xbHJRczVrZi1maGhfN3UwaGVSa0hQYVdRVzFjTS1HbERzMTExdS0zb2xRNmpDS2RENTdkMFlJRkRpOVhQcklYSU5pVQ?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 13 Aug 2026 13:15:00 GMT
- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 13 Aug 2026 00:45:38 GMT
- [AI伺服器液冷滲透率攀升 奇鋐估2027年達5成 - digitimes.com.tw](https://news.google.com/rss/articles/CBMijgFBVV95cUxNSzItSE9aUE5nUkhZNEs5MkJKWjFoQVV0UGk4ZTNlUVE4WlE1R1MyMDVpUFNEUVh5ZjNuZHBjTUJ5TW42UzZReFk2WUZuc3liTFE3NDgtcUhKcGdKNGtOaTl6TENUZTdKQ19pRndzZXdQeFpNRG9Lc3owQzRxa3htOS1BZGFQSEFiMEpkZ3Bn?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 12 Aug 2026 18:36:00 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Micron Technology Inc Stock (MU) Moved Up by 3.09% on Aug 13: What Signal Does It Send? - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 949.83 | 971.00 | -2.18% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Micron Technology Inc Stock (MU) Moved Up by 3.09% on Aug 13: What Signal Does It Send? - TradingKey](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPNDdGcVAzMngxTTFtVXBITEJaeWdxR1hzNFpJbWRJdS10d0wxWHBadnRMQ21ram9sWE9JSHRoaHJ3NDExQVE3NElLWUVSSHZ4VmdGaDBLYThWbDFyek1oekVfMV9YX3NGNEJ4eUdvbWlOemUxZHdWNUFvUzRqTjlhbnlIU2trN2c5?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 13 Aug 2026 14:15:20 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：【台股操盤人筆記】油價震盪往下，AI需求帶領台灣供應鏈獲利向上 - MoneyDJ理財網；台股兆元權值股增至21檔 AI 供應鏈改寫市值版圖 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +15.55% | +31.50% | 305.26 | 312.06 | -2.18% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | -0.95% | -0.95% | 262.00 | 289.00 | -9.34% | 不適用 | 14.13 | 18.61 | 946.51B TWD / 54.19% | 2026-08-01 |

關聯理由（前 3）：
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [【台股操盤人筆記】油價震盪往下，AI需求帶領台灣供應鏈獲利向上 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilwFBVV95cUxOWXpOY3htb0xsTzZ2NzEtdFdNc3YwQVVNSGx2dTdVVkFHNkNyU0hyZlItTFJVSGZ3ZEtXOTRiT0FrSWN4RS04bTdqRXM5ZXNVd21pNjlPV3g2MmJQcC1sNmpZZzNoUDMyX2F1Z0xEa21INEF1WGhmZ3dkQzFGR1NXZEZwdDUxVTN3V01lNmFIUU5XZ2NZbjhB?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 13 Aug 2026 03:41:00 GMT
- [台股兆元權值股增至21檔 AI 供應鏈改寫市值版圖 - 經濟日報](https://news.google.com/rss/articles/CBMifEFVX3lxTE1fRHVsYmwwMkNkcTU5OW5QUVd4T1p6cmd3RlU5blFuQUNsQWdQbTB1SFBPMWtGd2lWaXNDbEZISXI5RnZuVnBqNkZ3cTBELW9kQzJNUDVZanh1MWdoWEU2c1lPWThLZm9Famd2YzlWMlAzbS1CSEU0d0VNcFHSAV9BVV95cUxNRVhBQnB0UEFTOWxPa242Ymo1dXZFSHFiejQ5WU1PSUdUS2lfS0FrZXJjb05jSnFEQVVfWFJKM1NXa3BTNVg0al9lckRHdXktcEpSbFFIX2t5ZzZWRVU1RQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 12 Aug 2026 17:11:09 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：《台股盤後》電子權值股領軍 收漲503點/重返46K - MoneyDJ理財網；第一金台股趨勢優選主動式ETF基金七月份經理人評論 - MoneyDJ理財網；國票證券：台股短線有望延續震盪偏多格局- 新聞 - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》電子權值股領軍 收漲503點/重返46K - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikgFBVV95cUxQSjQ5UDdzVlR2ajhtWUpJbkZlYnpmRDRObjdLaDNFMm1FSGVTb1JSMFZUYTRUbzd2QTJxYjJaTWtVbXoxVUc0ZjdjLXdvbmNQM0o0eEVwckNSYTJyX1N6bTdUSWZBa21pWGpMT0ZOc3BfSXBQVm40NFZXZlJzcms3bTQzTFhlZFA1ZXRaYWswdFlzUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 13 Aug 2026 07:45:00 GMT
- [第一金台股趨勢優選主動式ETF基金七月份經理人評論 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilwFBVV95cUxQbk5WMkZOVzhlMDdpYU1HX3BOdDBVNTlNanM3UjN6bmdNMWt0aURRWDV6QlVhQnl2TWtvU3VFQzlpUi13RUFWSHhlTExpdE1oUWJhX1RYLUdJX3htd3BYYnE5anlQM3N4cUVIRmUwb0NvSkNTeGZDLTk5ZGdlWW10bmlLMVM1Z0NBTm1NZWFQOC03Qm85bWM4?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 13 Aug 2026 06:00:00 GMT
- [國票證券：台股短線有望延續震盪偏多格局- 新聞 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikgFBVV95cUxOMHBLS3MyMkIzTGZTS0tNbFhITFBmYUNqQkwtZXVsZUFsYURrd1JlV0xJYklvR0FPTTQ2LXFabml3NkxzZEx1Z1B0V1hodkZfSmd6NUV5TmZEeGFEdEw4aHYwbE9RYmdVc0t2Mnd4OVRwQmJIZm1pQ3loUUdUU29OMzZYZHdJbzk4aWNaZ0ZpNU1GZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 13 Aug 2026 00:51:00 GMT

## 新興題材：AI需求帶領台灣供應鏈

摘要：新興題材：AI需求帶領台灣供應鏈 相關新聞集中在：【台股操盤人筆記】油價震盪往下，AI需求帶領台灣供應鏈獲利向上 - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [【台股操盤人筆記】油價震盪往下，AI需求帶領台灣供應鏈獲利向上 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilwFBVV95cUxOWXpOY3htb0xsTzZ2NzEtdFdNc3YwQVVNSGx2dTdVVkFHNkNyU0hyZlItTFJVSGZ3ZEtXOTRiT0FrSWN4RS04bTdqRXM5ZXNVd21pNjlPV3g2MmJQcC1sNmpZZzNoUDMyX2F1Z0xEa21INEF1WGhmZ3dkQzFGR1NXZEZwdDUxVTN3V01lNmFIUU5XZ2NZbjhB?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 13 Aug 2026 03:41:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
