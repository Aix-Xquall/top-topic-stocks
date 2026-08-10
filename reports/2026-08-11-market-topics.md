# 每日股市熱門話題分析 - 2026-08-11

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **AI 伺服器與資料中心**｜正向｜熱度 15｜市場確認 73.47｜同向 4/6
2. **記憶體與 HBM 供應鏈**｜中性｜熱度 8｜市場確認 N/A｜同向 0/0
3. **新興題材：台積電7月營收**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0
4. **散熱與液冷供應鏈**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
5. **半導體與晶片供應鏈**｜正向｜熱度 5｜市場確認 45.41｜同向 2/5

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.57（樣本 11）
- 5日相關係數：-0.18（樣本 11）
- 同向比例：6/11

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| AI 伺服器與資料中心 | 73.47 | 4/6 | 2 | +8.93% | +2.51% |
| 記憶體與 HBM 供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：台積電7月營收 | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | 45.41 | 2/5 | 2 | +5.80% | +1.93% |
| 新興題材：OpenAI | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
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
| 2026-08-10 | -0.09 | 0.74 | +71.43% | 7 |
| 2026-08-11 | 0.57 | -0.18 | +54.55% | 11 |

## 歷史回測摘要

- 回測日期：2026-08-11
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

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel plans $15 billion stock offering as AI demand accelerates - CNBC；Intel raises $15 billion in stock offering for AI chip growth - Yahoo Finance；Intel (INTC) Unveils $15 Billion Stock Offering As AI Buildout Accelerates - simplywall.st

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.57 | N/A | N/A | 97.52 | 114.68 | -14.96% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.06 | +8.73% | +9.01% | 217.55 | 223.96 | -2.86% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.06 | N/A | N/A | 469.56 | 516.10 | -9.02% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.03 | -1.04% | +0.42% | 2,380.00 | 2,425.00 | -1.86% | 背離 | 74.39 | 32.00 | 467.58B TWD / 44.69% | 2026-08-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | +28.85% | -0.12% | 506.06 | 506.69 | -0.12% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.04 | +11.82% | +1.19% | 422.40 | 446.77 | -5.45% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.04 | +6.24% | +3.28% | 630.00 | 680.00 | -7.35% | 同向 | 13.92 | 45.59 | 73.78B TWD / 43.15% | 2026-08-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.02 | -1.00% | +1.28% | 3,960.00 | 4,310.00 | -8.12% | 背離 | 60.69 | 65.40 | 48.47B TWD / 12.16% | 2026-08-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel、INTC」，共 3 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel plans $15 billion stock offering as AI demand accelerates - CNBC](https://news.google.com/rss/articles/CBMic0FVX3lxTE9wLUxnRncxa2pNdGoxaFhBVnZzNU40Qks5MDFnSFJ5eHAzdWo0RGluXzctenFpbmREckVJQkFhTHJMREdNbnZaeDNtYnNDQnBxckd3bGZ2Qm1xbU9ZaW01bkQwNnRvdUFRUUVjYXpyT2JxSjjSAXhBVV95cUxOUFZTSFNOX3hPb2lHTzhMMXdESmV6anV2SlNObC1wZmNDM3RmUmtVdXdfMmpETzkxTmVROG5Idy00V1Q1UEt4b1VEaS1aZEdRRXBYNmZKbGotSU0yNkNPMDJZcHZsU29zMTdWekNHSUNWT2lBellmMlc?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 10 Aug 2026 12:49:52 GMT
- [Intel raises $15 billion in stock offering for AI chip growth - Yahoo Finance](https://news.google.com/rss/articles/CBMimAFBVV95cUxPVjR0TU1GZk1GS1FqZVBCN3NKSHU2NGtDM0tuLXBEX1hrZ2ludDZlSEtiQlJZWWJZeGc4Mzg2QjRUMUJHUlZHNUwtWWE5RkVfcm9hMmg5QVExUHpGX0ZueDJObjUxdDlvUkFIRTFhQWVaRTZlYm5lYXdBSkk0Y2xIOE5RRHJuR1ptNlBZc1JGTlZPVU9XbUpJdg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 10 Aug 2026 12:45:34 GMT
- [Intel (INTC) Unveils $15 Billion Stock Offering As AI Buildout Accelerates - simplywall.st](https://news.google.com/rss/articles/CBMiyAFBVV95cUxNeHo1SHlBVUJlaGFMMnotV0dHM0V1ZjV6RThNck5yX0YtZlFyaHhyQzBKX2VtbnRaQndRODJlNmJlUGNrYmlqRE9ad0F1XzRnMmZ0RExubDVKUDIxRzRHcklYWTROemdEYTZqZ0dPdlo3bXd1U1VwMmlQZmpGZ1dYMHlVQlJJQVFseWQ4ZEFISEJ6YUx4VHRFV0p0ejJHb3laYWd5R1B4eW9sRGZRNnBUbjZidFJJOUVNZVM2WEppazFicm1SY2xEctIBzgFBVV95cUxQeldCM0xuVnFqbXo2UUdSLTh3OTVVXzcwRDlGZkY2dEdqWUtHT0dNZUZRdHFLYWdFVXUtako1NmhTWTRWSjZhSkxrNXFVdFNqcXRTaEdDTzJoSlNxZFQtSHNZQ2N1NzBZTFJwUFpRRnNfZVFDNnlSOGVIdnRqN2J6MTZOQ0ppRld6ODdhOGU1T0RwMzNDajZPaXR4ZTNvYjdmNHFEZURpTmNUUl9keWlTaTctbjBOQjhrelpURVdpSFUxSlp5Q2lvdVA4Z2NCUQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 10 Aug 2026 19:44:03 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Why Micron is Decisively Better Positioned Than Intel Now - 24/7 Wall St.；Opinion: The Best AI Memory Stock to Buy Isn't Micron or Sandisk -- It's This Korean Giant - Yahoo Finance；Micron vs. Sandisk: Which AI Memory Stock Has the Edge for the Next 3 Years? - finance.biggo.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 861.00 | 971.00 | -11.33% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | -8.34% | -3.89% | 1,237.92 | 2,335.00 | -46.98% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +8.73% | +9.01% | 217.55 | 223.96 | -2.86% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | N/A | N/A | 469.56 | 516.10 | -9.02% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 97.52 | 114.68 | -14.96% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、memory」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Why Micron is Decisively Better Positioned Than Intel Now - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiowFBVV95cUxPaUh5RS1MYm9ja3ZHZkdobnI4SkhyazFiS0lxQUFVbUVaMkp2cGRieWlicW1hTl9uVERSWndDSFV1VUhPVmxvSjJvSVFLeXdUeVJiUzkwV0s4RUxZY19KTFZHcC11TTJRMXoxLVBCZW1ham5FTms3NzF2dnN3OV9xcHhrNnNGNjgzOVdFLWIyVkNaYUQydGI4dXVhcjBzSU9yVUFB?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 10 Aug 2026 15:53:40 GMT
- [Opinion: The Best AI Memory Stock to Buy Isn't Micron or Sandisk -- It's This Korean Giant - Yahoo Finance](https://news.google.com/rss/articles/CBMilwFBVV95cUxOR0UzM3VpQ1ZOOHJxRkFscVEyR1FMVGsydHNWaE5XZHlSbmJramNNM1czckRRS1F6TGtEYkRlcHBvMk5nV2FmaXlkZktBNmJUSGNNYThsSFBhSmdacGZBaFBSMlh3TXBuNy1xYWhzMzJzcGhXT1FvR2k5NVA2UzdiYlRqUnpfbVpCMUk1LUpUay1NdWJCSnJF?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 09 Aug 2026 17:43:00 GMT
- [Micron vs. Sandisk: Which AI Memory Stock Has the Edge for the Next 3 Years? - finance.biggo.com](https://news.google.com/rss/articles/CBMidkFVX3lxTE9tS0k0Q3AyQ2xDU0I5SW42cFZFZlhPYzgyeUFYNWRzdkZPa29ZTW5adXBVMVVnWTczMFlobFBBN2RrV05UcTBEempqWUtSZjBRNUVJdGE2akh6OXdBNzJ6bUw2T3hPa2pzc0QxTWlnWEMwRlVDbHc?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 09 Aug 2026 00:01:23 GMT

## 新興題材：台積電7月營收

摘要：新興題材：台積電7月營收 相關新聞集中在：台積電7月營收超乎預期！破4675億元「史上最高」 - Yahoo股市；台積電7月營收創佳績！破4675億元、年增44.7% 股民卻吵翻：沒考120分 - Yahoo股市；台積電7月營收4676億元 年增44%續創單月新高 - news.cnyes.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | 0.00 | -1.04% | +0.42% | 2,380.00 | 2,425.00 | -1.86% | 不適用 | 74.39 | 32.00 | 467.58B TWD / 44.69% | 2026-08-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 3 篇新聞命中。

### 主要來源

- [台積電7月營收超乎預期！破4675億元「史上最高」 - Yahoo股市](https://news.google.com/rss/articles/CBMi0gJBVV95cUxOcDNwS09tU2xQUC1BVWl0RlQ1YXBfZUdwcFpSamV3Y3lsVFRwbWF4cTdnc1RHSHd6Yl9WSm1ad1JpOTM0ZlBkSU9vVTMzQVlHRmFIMWJaVVFObGtWRXlJTjZsSFpPZ2sxTlU1OFk5NE9oSVdGcUMwdUJxYXpsRjcxdUx3MHAzQVc2YnNROWlvbTRRQ2ZkOTVVVGZ5QllCallueWNnX1NpQlVnZWRLNEZrQkV5RHlYUHc3X0NjTlFlTlNCclBIOXYwMzFOSElzc0lOc1FxS2RnLVVYbl96Q1V6b1pQeE56ZUhVQnVQTksyWVU1ODZUQ3c3Sl80RFVEMkt0UzkybGFMeVFpUHByakMtQkloLXpqMnJhMjVadmxXUFYybktRQUFZTjBZRTRSTEJFZGFVTzlQZzNDX3dRZXJZdDRmUGtvTmJiWHFkelNNd0tqZw?oc=5) - Google News source discovery | Yahoo 奇摩股市 Mon, 10 Aug 2026 05:32:02 GMT
- [台積電7月營收創佳績！破4675億元、年增44.7% 股民卻吵翻：沒考120分 - Yahoo股市](https://news.google.com/rss/articles/CBMizwJBVV95cUxNaVFFLXkzSVF2bXR1VmJmSVZ3VjFwZTloUUVrQndrMVhlT1MtQVRFTkxzSWJSR2RMOXdBUWpxcEQzVFpVeTlaS01VWXRRSUhCTGM4ajFKMzhHaWF2QjQ5aFBnc2RBYU5Ya2QzUGhUY2JSSXlYcVB0MENNa0dUYlFhdUtsczh6eVJzOFBZU0dYYTBtZy1MaWFDRHN6bERFQlRKRTI5cHJLNDN3ZDkzbWFhMTV6SkZYVm9HVy1IbVpvLU90eWJOdmVIQ1JNeGp0MU5lQm51WndZQmR2c3NkdW8tUVYtbExtUVhuOGhoc05FSl9mZGU0VWEtcGMyMDhmbWt6MEJVWDRWcUw3WjUtTDZ4RlNZSGJHcVAyQ0czb1JEV2JpWDBqNTYxeThkOGl0b1p5SmUzbWhSMXhsdWxSLXJfT1JqQ0RBZnM2c3dIMDlJYw?oc=5) - Google News source discovery | Yahoo 奇摩股市 Mon, 10 Aug 2026 11:45:00 GMT
- [台積電7月營收4676億元 年增44%續創單月新高 - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTFB2ZkJNaEpReHNtd3hyYVlYZlo4NC1NaUdYN2ZyRUd4TTcwSnRTckoyckZLekVpOUZMNVE4OUlSX0x6SUxGRFJadndEZ1M1Rms?oc=5) - Google News source discovery | 鉅亨網 Mon, 10 Aug 2026 05:48:34 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：公告7月財報後 散熱王者它目標價飆升 - 三立新聞；公告7月財報後　散熱王者它目標價飆升 - 鏡週刊Mirror Media

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | +1.28% | +8.43% | 2,765.00 | 2,835.00 | -2.47% | 不適用 | 61.06 | 45.43 | 18.59B TWD / 57.39% | 2026-08-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 2 篇新聞命中。 同時符合主題標籤：thermal。

### 主要來源

- [公告7月財報後 散熱王者它目標價飆升 - 三立新聞](https://news.google.com/rss/articles/CBMiS0FVX3lxTE9Za2FHRGd5RGVrYnZfaVJHYjAyRXgzeDVuS2YtQUh2TXlhQUFSOC1wcjRPelQ4Z1ZNV0t3aDhHVXRwRWg2SDB5cnBvSQ?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 09 Aug 2026 09:06:26 GMT
- [公告7月財報後　散熱王者它目標價飆升 - 鏡週刊Mirror Media](https://news.google.com/rss/articles/CBMiYkFVX3lxTE1iVFk4cVVkVnN2bnpETm9rckVsMUVjaGVGNy1NZF9ub2pBOC1saGZJS3dpaXQzcklnTzRWWWlLaElLUGs3NTVkb2lsUi1EdVIyM1FsV1NaS25WQ09CbTgyUmR30gFiQVVfeXFMTWJUWThxVWRWc3ZuekROb2tyRWwxRWNoZUY3LU1kX25vakE4LWxoZklLd2lpdDNySWdPNFZZaUtoSUtQazc1NWRvaWxSLUR1UjIzUWxXU1pLblZDT0JtODJSZHc?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 09 Aug 2026 09:00:00 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel raises $15 billion in stock offering for AI chip growth - Yahoo Finance；韓國將啟動5兆韓元半導體基金扶植具潛力企業| 國際 - cna.com.tw；面對半導體擴廠潮，鋒魁如何佈局海外市場？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.52 | N/A | N/A | 97.52 | 114.68 | -14.96% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 新聞直接提及 | +0.42 | +28.85% | -0.12% | 506.06 | 506.69 | -0.12% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.03 | -1.04% | +0.42% | 2,380.00 | 2,425.00 | -1.86% | 背離 | 74.39 | 32.00 | 467.58B TWD / 44.69% | 2026-08-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.04 | +0.82% | +4.24% | 123.00 | 164.50 | -25.23% | 未明確 | 6.68 | 18.50 | 23.84B TWD / 18.98% | 2026-08-01 |
| NVDA 輝達 | 產業/供應鏈推估 | +0.04 | +8.73% | +9.01% | 217.55 | 223.96 | -2.86% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.04 | N/A | N/A | 469.56 | 516.10 | -9.02% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | +0.04 | N/A | N/A | 861.00 | 971.00 | -11.33% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.02 | -8.34% | -3.89% | 1,237.92 | 2,335.00 | -46.98% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MSFT：新聞直接提及「Microsoft」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 2 篇新聞出現相關標籤。 方向判斷命中詞：growth。

### 主要來源

- [Intel raises $15 billion in stock offering for AI chip growth - Yahoo Finance](https://news.google.com/rss/articles/CBMimAFBVV95cUxPVjR0TU1GZk1GS1FqZVBCN3NKSHU2NGtDM0tuLXBEX1hrZ2ludDZlSEtiQlJZWWJZeGc4Mzg2QjRUMUJHUlZHNUwtWWE5RkVfcm9hMmg5QVExUHpGX0ZueDJObjUxdDlvUkFIRTFhQWVaRTZlYm5lYXdBSkk0Y2xIOE5RRHJuR1ptNlBZc1JGTlZPVU9XbUpJdg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 10 Aug 2026 12:45:34 GMT
- [韓國將啟動5兆韓元半導體基金扶植具潛力企業| 國際 - cna.com.tw](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9sbjR5RjF6cDlLNF9NV1EwUXNGbEx3Y1F5aEpONEhKT0lxZGM0Z24tc2MtMnVqY3VoYWF4ZlRUQVhNcGJCNnNxRlpCbU5OVGtlRU9GS2hHZnVXcmFsZm1v?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 10 Aug 2026 13:49:00 GMT
- [面對半導體擴廠潮，鋒魁如何佈局海外市場？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiqwFBVV95cUxOQkY2SXBSd0RyV2ZYOUR1UW9wZHRKc1dQQ0ZReUplS3Z4UXpwdjJLUENtNnlaQm9IRXplcTJMbFlkM0JIY21ubFlQb3k1aWpocHNZZUZYQjc5RkhMNFVhZFZEamMxYkJfZXZIWnlBMUJBT0lJQ3FUbl85S3dTcFhyRXNHbzZTd3kzMTg1SlZMaUNYYTZDa3NJYWxlX1hoWjBnVG5Kdm11R3l4M1U?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 10 Aug 2026 13:39:18 GMT

## 新興題材：OpenAI

摘要：新興題材：OpenAI 相關新聞集中在：US House Democrats press Anthropic, OpenAI about rogue AI agents - Reuters；OpenAI expands Daybreak cybersecurity initiative as AI agent threats evolve - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 新聞直接提及 | 0.00 | +28.85% | -0.12% | 506.06 | 506.69 | -0.12% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：新聞直接提及「OpenAI」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [US House Democrats press Anthropic, OpenAI about rogue AI agents - Reuters](https://news.google.com/rss/articles/CBMitwFBVV95cUxQMDRJNHZDWC05T1Jvbm9qcjJvSTZXSHZfV1pabmhRWFU0MWZ5TVhhOV8zaFFvbzRmdnk1MXhkeXNmbDhMY2NKaDNGaFM3SVBUTHc1cklXYzJFU3F4dm8xcENxWHk1OVJnUnc5ZG9KMWZDUFRHUWlIcTZUSmYzNTBwZV9GSGJuUFMxSVhNQkRWemEwdEhpMjVUYVpFeWYxOGFXeUwxTDFoYkdkT2V4Q0ZxdTNva2Nha1E?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 10 Aug 2026 19:48:45 GMT
- [OpenAI expands Daybreak cybersecurity initiative as AI agent threats evolve - CNBC](https://news.google.com/rss/articles/CBMidkFVX3lxTE1QOGwxSHNLd2VfQzc4ZC1aaGgyMGFzQjV3b3ZWR0NQUmpXUmVHalRlSERRTFlQUEZQMDQ0azJlYnJEZGlObk9sR2xXUG9oRkpWTXFMaUhWWXRCLWZ1MTB0b1JRQ2NNcGNHWDVmbWI4UlNlZ2toRXfSAXtBVV95cUxObk1PT3kwQWxxemdBSmh6RGVKODJMb2VNWWtOM0hsc193Y2ZOTF9NNnhyZExNWDE4SzNQR0JzMW5mNnl5RVZTd0R1dU5pcDFOMUFCNWVqd1h1YWRZTmJGcUpuVUU3b1dSUHg3TW82dy1wWnF6bjYtd3dNcmM?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 10 Aug 2026 18:40:32 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》收漲702點、日K翻紅，45K得而復失- 新聞 - MoneyDJ；台股ETF規模7.5兆創高！受益人達1854萬 3類型最吸金- 新聞 - MoneyDJ；台股強漲，台幣早盤升值6.3分 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》收漲702點、日K翻紅，45K得而復失- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxOVGF4dUZHMC1Sam44Sjl5eWdoRFBrUkxQNmZodmVzbjdYbUpQTDFqYmFaM0VkNk44Z2JHZ21ORDFSeFY2OThNNDh3eFc2aTdIakQzUHBPNmJwNTgzMmdaeVdJM1dDQ2g3WHgxRGZidjI0STN5YVNqU3l0bF9Za3Mwa0RUZGZ3R3Z3di0xVTM4d3VJZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 10 Aug 2026 08:07:00 GMT
- [台股ETF規模7.5兆創高！受益人達1854萬 3類型最吸金- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPNFBLMlRjMktodjN6NFl2WEYtUDJJLUIyMTZMZU9kNUZqN0dwZEdEXzJRclR3YkhieS1LWDRPTFJPSU5mMktiTjdnbmRKLU5ZRFlQMW50anJZQnNtX2tFU0k5X01kLXNWN1lEZXpCTTE2T25RZnk5SXhwYlF6T3dWakhWRmxiU1ZfazBSMVRPeGZzdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 10 Aug 2026 08:45:00 GMT
- [台股強漲，台幣早盤升值6.3分 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxORHVSVnVZdDd0dmJyM2hmRkdOMlduczRCMzdmbEJzTEZlNW9XTXRZcVRUYmE4a0JwTmZFaFdhcUphbWQyUEI5a1RBR1VZVFVRNnFHZEFYY25reC1WdkpiMFZxM0RqYnZ1QW9meFB0ejVjazR0cnJ4VU1TS3RpQ012ME5vN2lkSGxicnVXZmNsSFdPQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 10 Aug 2026 04:54:00 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股有望繼續上攻？三大法人齊心協力加倉、買超731億元 - 經濟日報；處置股新制上路、財報點火、三大法人同買 台股本周挑戰46,500點 - 經濟日報；就市論勢／高含積量台股 ETF 分批買 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股有望繼續上攻？三大法人齊心協力加倉、買超731億元 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9TMHhnOXlObWtFdTNCZkNQdnFFbXljZUNhSkVFUnFRTVlOTUNZbEUzeS1yeGExQkRfbUhQUGVxUDhkLUt2ZzUwTXRhU2I2ekNwemVpNm9tdllpUdIBX0FVX3lxTE5YYl9VeXUyZW5UMTVqd2NWWTJ6R3I3S0h3NkFFOVRTOXVLVC00VVd4YzlBQjYwUjYwNWhuMzZsUnJkM0VHY0prWnRwYjZMZzE0MlE3dkpIazZYZW5wWGQw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 09 Aug 2026 09:00:00 GMT
- [處置股新制上路、財報點火、三大法人同買 台股本周挑戰46,500點 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBZbUl0OVBjMWFsSzhrVW85TkNCRElZdXZqNjJSd2Qwd29CcjYtbmhIWmx6UENhSThEeDN0cHVyV0FCSzhmOXZVYVhHUzBJVGRIclZ6STZYYi1JQdIBX0FVX3lxTE5hYl9UMUJuc0V3eXJZbFk4NC1YRTFJRkZjckwyMHNpZFJsLXpVODk2VGRQOF9tb1R4MmVBaUJOQ1o3YWZvb2VaekxCa3hmNHRQc2lYNlhzLWFuMnFyNnRn?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 10 Aug 2026 04:00:00 GMT
- [就市論勢／高含積量台股 ETF 分批買 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1jVHE0QTJsY2NJZTd6azFqZTJhVnpDdmxwZzZ5Qi01Yi1Eek5ULUdlLVd6Y280bUN5R2ttVVE4aHJjQ0Y4ZTNtNEYyNEpKbWVQcUdaVmdSSk42UdIBX0FVX3lxTFBWNGVJbE56OTJvdVFRd2RaX05jT3EyRjhuNGVUaDBJMERTODVxejNUR1NjQnY1OTFKcllqTG5VYldqam5CMk11RVdjUHhsMzgyc3BmUHVuN1lGOG8xanlr?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 10 Aug 2026 05:00:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
