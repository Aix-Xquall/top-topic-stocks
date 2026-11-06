# 每日股市熱門話題分析 - 2026-11-06

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **綜合市場情緒**｜負向｜熱度 44｜市場確認 100.00｜同向 1/1
2. **記憶體與 HBM 供應鏈**｜負向｜熱度 5｜市場確認 100.00｜同向 3/3
3. **AI 伺服器與資料中心**｜中性｜熱度 19｜市場確認 N/A｜同向 0/0
4. **散熱與液冷供應鏈**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0
5. **新興題材：台積電跌停**｜負向｜熱度 2｜市場確認 81.58｜同向 1/1

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.18（樣本 5）
- 5日相關係數：0.77（樣本 4）
- 同向比例：5/5

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 綜合市場情緒 | 100.00 | 1/1 | 0 | +54.44% | -28.82% |
| 記憶體與 HBM 供應鏈 | 100.00 | 3/3 | 0 | +15.37% | +16.70% |
| AI 伺服器與資料中心 | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：台積電跌停 | 81.58 | 1/1 | 0 | +3.86% | +7.25% |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：一度超過500檔跌停 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-10-24 | 0.09 | -0.31 | +70.00% | 20 |
| 2026-10-25 | 0.41 | 0.78 | +64.29% | 14 |
| 2026-10-26 | 0.27 | -0.25 | +36.36% | 11 |
| 2026-10-27 | 0.07 | 0.31 | +50.00% | 18 |
| 2026-10-28 | -0.30 | 0.47 | +20.00% | 15 |
| 2026-10-29 | -0.05 | 0.04 | +42.86% | 14 |
| 2026-10-30 | -0.00 | -0.05 | +47.62% | 21 |
| 2026-10-31 | 0.50 | -0.68 | +80.00% | 15 |
| 2026-11-01 | 0.47 | -0.40 | +85.71% | 14 |
| 2026-11-02 | -0.15 | -0.06 | +27.78% | 18 |
| 2026-11-03 | -0.03 | 0.08 | +40.91% | 22 |
| 2026-11-04 | -0.21 | 0.35 | +15.79% | 19 |
| 2026-11-05 | 0.13 | -0.53 | +66.67% | 12 |
| 2026-11-06 | -0.18 | 0.77 | +100.00% | 5 |

## 歷史回測摘要

- 回測日期：2026-11-06
- 近5日 3日相關：0.26
- 近5日 5日相關：-0.07
- 同向比例：+56.67%
- 權重狀態：已調整

- 方向準確度：+56.67%
- 信心排序準確度：0.26
- 診斷：正相關

調整原因：近 5 日信心分數與後續報酬呈正相關，提高市場確認、歷史題材與直接提及權重。；關鍵詞×公司後續樣本有效 4 筆，未達 30 筆，不調整樣本權重

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

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股譜寫築底三部曲 法人：短線防斷頭賣壓 - 經濟日報；台股開盤跳崖崩跌 卓榮泰：已指示金管會 隨時穩定股市 - 經濟日報；台股跌破4萬點只是暫時的？ 楊金龍：希望是 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.43 | -54.44% | +28.82% | 52.25 | 114.68 | -54.44% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [台股譜寫築底三部曲 法人：短線防斷頭賣壓 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1acDlmMEVyV3U0ZXAySjgxS1R2Y2tSMkJ2b1AzbWs5TjBocFdVSFR5UEpVZ1RaUjlpcUd6bTFaRW9xSGNvQzJHT1RGM1FlbTRhSUl5WWxBYldCQdIBX0FVX3lxTFB4Ti1kMjhkR2JoNGhMRDZROWp3MDZQUVltT1JRZUd4YVN1eXdGcExCZ3REbUNGa0M5TGtNSVZXTllhWm5CcWxqaERiR3E0VmZRenNLWEd6Tk5abDEwQmJV?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 05 Nov 2026 18:39:04 GMT
- [台股開盤跳崖崩跌 卓榮泰：已指示金管會 隨時穩定股市 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE92OVdIYWlDMThrWHdNY2xFLTNsVG9QS3dTemdDWTMtcURYcndnOFhiM1czb0ozVjItcGNTay1ZbnRVX2dLMEdkQTBFRU1mbklNS2xZTUhVcjBoUdIBX0FVX3lxTE9LQWJhTW5uSm1fR0phemhXQjBGYkJJdUJDazlPSG1ZeTA2RHVKeDh3akxjZDNKcVhoc20yNEt1RVZfRFNxSF9SLXNKOEJVSzFSWEhYVEE5YURMdUlPd004?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 06 Nov 2026 01:28:29 GMT
- [台股跌破4萬點只是暫時的？ 楊金龍：希望是 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBkQXg1R2ZDRHdFckt2ZXlydmJpOUlnNjdFTEFoRV8yZzFHM3h6QkxuTTFfeThYQm5yczEyOTNLWVlvMlZseXA2SE9BSEVEaXhFdmZ4OFh0YnUwQdIBX0FVX3lxTE4wbjBoZmtWS2U0Wnh5dEFfZUkwbzZXRnZXSWFxNllZSzNTeGFoTUt6ZGZzR0JqOVZ0OVNZVEVjRVA1LWhWT1VSOEk1ZHVZem5aR1lhOUZMMk1rbVo5Rm1B?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 06 Nov 2026 01:34:29 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：SanDisk Slides 7%, Micron and Western Digital Fall 5% as Lawmaker's Call for AI Pause Extends Memory Rout - 24/7 Wall St.；SanDisk Retreats 9%, Micron and Western Digital Fall 7% as Election and Memory Price Worries Weigh - 24/7 Wall St.；Micron, SanDisk, SK Hynix plunge up to 20% as memory stocks selloff intensifies - TradingView

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | -0.59 | -32.40% | N/A | 656.39 | 971.00 | -32.40% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.59 | -9.86% | -26.15% | 1,037.40 | 2,335.00 | -55.57% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | -0.43 | -3.86% | -7.25% | 2,075.00 | 2,480.00 | -16.33% | 同向 | 86.28 | 25.96 | 511.86B TWD / 54.65% | 2026-10-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -20.48% | -9.54% | 181.60 | 228.38 | -20.48% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron」，共 4 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 4 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- 2330：新聞直接提及「TSMC」，共 1 篇新聞命中。

### 主要來源

- [SanDisk Slides 7%, Micron and Western Digital Fall 5% as Lawmaker's Call for AI Pause Extends Memory Rout - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi3gFBVV95cUxPVllxRm9UQlBHNkl1Q1l6TDFvV3lFVGVDcUtNdkZrMF9yTnR6UE1TTGh3SEpUM3VKX1l1YzRxUkh6aTRpem9tQlNHQmtXWEQ1cWVaM0k1djdYcVJadENkTjZnN2ZOYjNiZXE1MERib3FxSmRiSDFhOUNVYTlPWUd3czIxajh0SDVmZWR0bWZ0cVJtc0Z5OXQ1SVZzQXdhSF9MZTJvQzU0UF9XNWJRaHIwaFRaa3VSQnRqX2hKd09VYTJ5Q3pLcDdreDNqV0pPWkVGejNzTzJXbFA2ZFNhQUE?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 05 Nov 2026 13:47:00 GMT
- [SanDisk Retreats 9%, Micron and Western Digital Fall 7% as Election and Memory Price Worries Weigh - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi0wFBVV95cUxPYUlTdE9VUUNsNlB0a1M5S3RsVnZsODVyQUJ6NnBZZlBadkM4a0czWUI5Uk1MQlI2SkJlSzVCWjlrUUhGaFUwUllxbko5THNSVE1Nb1ROd0JXOWg0T3VOYi1GVGVXVE81T2pyaURBWHJ3czBGMlVKZU9NYTVMT05vMTlGNDhmWjBTUEFLNWNqRW9lNVo0NnZQdkJ4MnpacGUxVFY5R2JpYmVjS1FiRFdrdkxIQng1TGlmeElPNmhGRTBFNGEwUlluVFVIejRHVlFSNTJV?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 04 Nov 2026 16:02:00 GMT
- [Micron, SanDisk, SK Hynix plunge up to 20% as memory stocks selloff intensifies - TradingView](https://news.google.com/rss/articles/CBMizgFBVV95cUxQNjdEX3h1OG5EU3FoV19PQXBVNGZlUnh5MVcwMGE1QnJ0SGMxc181NG9PT2p0dzZsOFJGenlYLWtDZFV2ZUd1MnF3T3RjUmxWek5iZW5BYS1mNFBuTW1odDRyamJsdFJCQ0V0NDVqU28tRVhFWlRzMU9BaFNtWmFWTlhLekJPVjlvME5nODBGV256alJVX3ZHdEgwTzFHc2ZrZ0p1U2ZCZkxpQzU0blNsMTFnak9XMFZ2bXZ0SFNvcWxrLUVNcmstVG9ObDVFZw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 05 Nov 2026 16:26:11 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：AMD Tumbles 13%, NVIDIA Slides 7% as AI Regulation Fears Hit Chip Stocks; Intel Sinks 8% - 24/7 Wall St.；AMD’s AI Boom Puts It On Track To Outsell Intel For The First Time – Analysts See More Room To Grow - Yahoo Finance；Prediction: This Could Be the Best AI Stock You’re Not Talking About - Yahoo Finance

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | -54.44% | +28.82% | 52.25 | 114.68 | -54.44% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | -21.64% | N/A | 404.40 | 516.10 | -21.64% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | 0.00 | -20.48% | -9.54% | 181.60 | 228.38 | -20.48% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | 0.00 | -3.86% | -7.25% | 2,075.00 | 2,480.00 | -16.33% | 不適用 | 86.28 | 25.96 | 511.86B TWD / 54.65% | 2026-10-01 |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +19.03% | +8.93% | 535.93 | 555.80 | -3.58% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -16.99% | -25.11% | 291.53 | 446.77 | -34.75% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | -15.13% | -16.25% | 515.00 | 703.00 | -26.74% | 不適用 | 13.92 | 41.39 | 88.13B TWD / 45.52% | 2026-10-01 |
| 2454 聯發科 | 產業/供應鏈推估 | 0.00 | -12.85% | -14.46% | 3,165.00 | 4,920.00 | -35.67% | 不適用 | 60.69 | 57.14 | 55.40B TWD / 1.97% | 2026-10-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel、英特爾」，共 3 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AMD Tumbles 13%, NVIDIA Slides 7% as AI Regulation Fears Hit Chip Stocks; Intel Sinks 8% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMixgFBVV95cUxQZXpOcVdYWWIyd0ZyaldnY3QxMFJUUk14d3E0UmpWVzRwakhSOF9lOUE1azgtTmxRMm55V1JWZ24wZmhsNlVjWHBtZW1DNTJLMmFRNjd1YS0yaFJ1cUxQQVhkdU14V0Mzb1VjbFBreGpFS3FjYUdnXzd1NkVYUUlEY05uYWVJVEgxaGMzbDhzMU5rZWpmNkxqcjdBT0lLMy1kWVlhN1lhbjB2TDFEOGQ4SEJ3YXAxUnpuMi1kMy1RdkZzZVFicVE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 05 Nov 2026 15:46:00 GMT
- [AMD’s AI Boom Puts It On Track To Outsell Intel For The First Time – Analysts See More Room To Grow - Yahoo Finance](https://news.google.com/rss/articles/CBMikAFBVV95cUxQbENTZEtqblB0VE1MOUJWbmprcllrd0ZCNUtEcC0tdHFGUHVDaVBWNmpRM2NnUjVGajl1M3Bpd1N5ZF9KU0UyUDVQMFF2SjdTTWtZbWkzVGxPQ0xxSlNFMW12bEFMRnByT0QtNk9pWU1TcUlZQTVJSi1iQWhEVHN3amtRU1lQcVdZQjc1SDNmMjE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 04 Nov 2026 02:27:00 GMT
- [Prediction: This Could Be the Best AI Stock You’re Not Talking About - Yahoo Finance](https://news.google.com/rss/articles/CBMimwFBVV95cUxPMDh6OGtiZ3ltdVdDVS1QSEwwQmc0a3I2eERaT0FHQjlwTVQ4V0ZiODc0X2xsWUVfVXlBd2tuXzhYWWV0aS1pLTFINFB5M2ZDZ1lpbTN6YnRUSVFoTXFYSVhTZTBZZ2JHemIyLXRLbm4zNWlIN1otMXhQcHNFTU5jYllxMk4xc2lrc3p3SW4wb29TQnBSN2hEMGdaTQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 04 Nov 2026 16:03:56 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：散熱股又有大消息？花旗喊買奇鋐、雙鴻 目標價齊升逾14% - 經濟日報；輝達GB300大單帶旺業績！「散熱零組件廠」第四季EPS挑戰2股本 目標價喊上3100元 - FTNN 新聞網；馬斯克喊話SpaceX太空散熱更容易！AI運算衝上軌道！ - 蕃新聞

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | -16.18% | -17.39% | 2,310.00 | 3,435.00 | -32.75% | 不適用 | 75.13 | 34.19 | 21.02B TWD / 44.92% | 2026-10-01 |
| NVDA 輝達 | 新聞直接提及 | 0.00 | -20.48% | -9.54% | 181.60 | 228.38 | -20.48% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐、散熱」，共 3 篇新聞命中。 同時符合主題標籤：thermal。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [散熱股又有大消息？花旗喊買奇鋐、雙鴻 目標價齊升逾14% - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE04UXU3RGRUUnBBVElIbVBGZWozMUxfTzNsbE50ejYzRE1pUTJBQ0FNWS03VjRSYlZrUWkzSXhuNHhFQl9teWs5YTJ4QUU4ck1MZ0NneEk3XzF3UdIBX0FVX3lxTE5tclh3dXNNWDhDMnNiYmMyRW1DRFJwZUt6ZlZXMmdEYlhoQU9VR1pSeTVrVUpVT2FWOE1idEkxdXRhYTYyYVpMcnRwaWQ4NGpmRUNTREJUQ2UwNU01N0pF?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 04 Nov 2026 08:00:00 GMT
- [輝達GB300大單帶旺業績！「散熱零組件廠」第四季EPS挑戰2股本 目標價喊上3100元 - FTNN 新聞網](https://news.google.com/rss/articles/CBMiS0FVX3lxTFBiMFZwVnIycldIanVrSThXSk1sbzBQdzM4TWVUNkVKRTl1ZEdtMWxuUjJyYTJMVGFrNmpIWUlzNElPbjVEdnZ5aHQ2bw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 04 Nov 2026 15:40:00 GMT
- [馬斯克喊話SpaceX太空散熱更容易！AI運算衝上軌道！ - 蕃新聞](https://news.google.com/rss/articles/CBMiUkFVX3lxTE5HNmlvZnpYSTRnTU5pVDVzT1N4Ri1tOE1MT0lwcVF1X2d3bUh5QXZPTmo2T2ZlWE42VXhtUHZtU0owVmFUX1g1N0ZwNjlBajlGb3c?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 04 Nov 2026 00:00:00 GMT

## 新興題材：台積電跌停

摘要：新興題材：台積電跌停 相關新聞集中在：台積電跌停　台股早盤崩跌3737點創盤中最大跌點失守年線 - 經濟日報；台積電跌停台股早盤崩跌3737點創盤中最大跌點失守年線| 證券 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | -0.51 | -3.86% | -7.25% | 2,075.00 | 2,480.00 | -16.33% | 同向 | 86.28 | 25.96 | 511.86B TWD / 54.65% | 2026-10-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 2 篇新聞命中。 方向判斷命中詞：跌停。

### 主要來源

- [台積電跌停　台股早盤崩跌3737點創盤中最大跌點失守年線 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9lamw3TExKM0hNbDdpYm0teDFudHdMZWVKMVJaY1d6aktHTkVSYzd1U3R4S2JRNUktbEdQT3Q2aEk2Q2c4R3Zjck1NOEtGTGVJWmI2aW56Wks4Z9IBX0FVX3lxTE9pQ0I3VTRBNlNqQ2E1WWU4VDIyYU1DM1VBZGg5ZjZEcEoyenBGU0YxczV6LTZ5bnF4eE1TM25IWTNJdkE4RTVwakluaWlLRGtNX3B0TDlZbVNEVDJPbFNN?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 06 Nov 2026 01:21:58 GMT
- [台積電跌停台股早盤崩跌3737點創盤中最大跌點失守年線| 證券 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTFBOcHhBcTVOZjZKRVRDRVNnSFIyamloSkpSV2pDdW5FNFBuZEJkNjRWUmFldWNYR0hZTFZOM1YzWVdKbjBoUlg2QXlOekFkLUVhMjhGanI1cVRESWtWMkE?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 06 Nov 2026 01:13:00 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：AMD Tumbles 13%, NVIDIA Slides 7% as AI Regulation Fears Hit Chip Stocks; Intel Sinks 8% - 24/7 Wall St.；AI 晶片趨向大面積化，英特爾強調 EMIB 封裝技術將迎接龐大商機挑戰台積電 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | -54.44% | +28.82% | 52.25 | 114.68 | -54.44% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | 0.00 | -3.86% | -7.25% | 2,075.00 | 2,480.00 | -16.33% | 不適用 | 86.28 | 25.96 | 511.86B TWD / 54.65% | 2026-10-01 |
| NVDA 輝達 | 新聞直接提及 | 0.00 | -20.48% | -9.54% | 181.60 | 228.38 | -20.48% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | -21.64% | N/A | 404.40 | 516.10 | -21.64% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | -10.55% | -14.81% | 91.00 | 164.50 | -44.68% | 不適用 | 6.80 | 14.53 | 25.20B TWD / 18.33% | 2026-11-01 |
| MU 美光 | 產業/供應鏈推估 | 0.00 | -32.40% | N/A | 656.39 | 971.00 | -32.40% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -9.86% | -26.15% | 1,037.40 | 2,335.00 | -55.57% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -16.99% | -25.11% | 291.53 | 446.77 | -34.75% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel、英特爾」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip, foundry。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AMD Tumbles 13%, NVIDIA Slides 7% as AI Regulation Fears Hit Chip Stocks; Intel Sinks 8% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMixgFBVV95cUxQZXpOcVdYWWIyd0ZyaldnY3QxMFJUUk14d3E0UmpWVzRwakhSOF9lOUE1azgtTmxRMm55V1JWZ24wZmhsNlVjWHBtZW1DNTJLMmFRNjd1YS0yaFJ1cUxQQVhkdU14V0Mzb1VjbFBreGpFS3FjYUdnXzd1NkVYUUlEY05uYWVJVEgxaGMzbDhzMU5rZWpmNkxqcjdBT0lLMy1kWVlhN1lhbjB2TDFEOGQ4SEJ3YXAxUnpuMi1kMy1RdkZzZVFicVE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 05 Nov 2026 15:46:00 GMT
- [AI 晶片趨向大面積化，英特爾強調 EMIB 封裝技術將迎接龐大商機挑戰台積電 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiyAFBVV95cUxQVFNYdGpodllfQzJQT1ZrdHZCRmdBYjM5V0w3Mi1iVXZLQ1VvVWtJV2VENmJDcU1IaXlTVzBOR1BlQXpqYlhOLU43MjNra2hZNGNtZnVKTFBvem5LcDRwM0lwQm9PQ0h3MGxCbmtENHhGUUsxNWlwYzlKdlVPdW4tRERxY283UnFBM3RycXp4SW9qalU1S09nZEZfZFJpMWhMWU80ZDNnOTFCZXg0cmdPcmhhaG05bC05VnFzbVkwRjl1b3VpZi1HLQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 05 Nov 2026 23:06:52 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：國際股市影響，10月外資淨匯出/台股賣超寫同期高- 新聞 - MoneyDJ；國際股市震盪證交所：臺股展現相對穩健韌性- 新聞 - MoneyDJ；富邦投顧：台股融資仍待消化；Q4估40~50K震盪打底- 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [國際股市影響，10月外資淨匯出/台股賣超寫同期高- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQZGNiWTRWRmFjLVhBbXZiX09PUE9oRXZwV0ZfcW01R3N5THZIWWlzWW5oUk5lY1lxZ25LQ2ZBc1pQZE5MYXRVNGxYYXVsN1NyaU5vbHVUOER2OHZUSElfLU9aZmhCbnd1S0NvWnlROTl0dmNPR3JuczRzVUVSdUtob09ydXhfOUEzMTluVWJXY3gyZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 05 Nov 2026 21:16:00 GMT
- [國際股市震盪證交所：臺股展現相對穩健韌性- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQRG1sX0RZY2ZjZzE4WFJKNVJ4eExBSUdudkdzVFBSeEdyM0M1STdlTzFkV3JRVWZBbW1PUmFiRE9leFFGNUlXM3J0c2FiTTNEcHhOMmx3b2h5TTc4XzhXMHpOVUYyV29XaHhRcnhwSjlYTEp5MzNLcGM4cVR3ek9BbkxSZlo0ZkVtWHhRQTdUM09BUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 05 Nov 2026 09:07:00 GMT
- [富邦投顧：台股融資仍待消化；Q4估40~50K震盪打底- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPNWc4TjVrWVVoVXhIVWVUa1J6UzVZckFFMHFSWkwxcXNFb3ZoM2tYRHZHZFAwWnZuOUhBWWoxMnJiTlNncEh6U0tvdmFfR0ljMXFqOFFWak1nZmVoYmJIWXZMUlVrZlNYQmJ0YWNXWUZyMHRjNHM3YVVPbUlRS0JtenZLWDBpUnlyR0NXb2I0U1Jidw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 05 Nov 2026 11:51:00 GMT

## 新興題材：一度超過500檔跌停

摘要：新興題材：一度超過500檔跌停 相關新聞集中在：台股史詩級崩跌！開低暴殺3,737點摜破年線 一度超過500檔跌停 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股史詩級崩跌！開低暴殺3,737點摜破年線 一度超過500檔跌停 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9qbks0cThWXzNndkxpMHRtdTBpYldfR2J5VTNIN1JGaWw3My02a2pBSmxjUVpyYTlzM2RtNTlWdXNoLUc1VUh3LXlFb2xsNGZpOGwzQlpzWXhaZ9IBX0FVX3lxTE4tUnBGZHBkbzdBMkE2eE5RakF0QkJTZmlJOVR4X2xFNDloQlNMUTd0NVE4enV2X2NDaUNNai1Fd2pzV0RyUjNxRlh6N05JSExQS2VpRTRFYUFTMVFnX3ZZ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 05 Nov 2026 09:00:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
