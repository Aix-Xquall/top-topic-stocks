# 每日股市熱門話題分析 - 2026-08-15

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜正向｜熱度 7｜市場確認 100.00｜同向 2/2
2. **散熱與液冷供應鏈**｜正向｜熱度 4｜市場確認 100.00｜同向 2/2
3. **AI 伺服器與資料中心**｜正向｜熱度 16｜市場確認 69.35｜同向 4/6
4. **半導體與晶片供應鏈**｜正向｜熱度 3｜市場確認 68.42｜同向 3/5
5. **新興題材：BofA**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.24（樣本 16）
- 5日相關係數：0.30（樣本 16）
- 同向比例：11/16

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 100.00 | 2/2 | 0 | +20.82% | +24.10% |
| 散熱與液冷供應鏈 | 100.00 | 2/2 | 0 | +14.87% | +14.49% |
| AI 伺服器與資料中心 | 69.35 | 4/6 | 1 | +7.56% | +3.17% |
| 半導體與晶片供應鏈 | 68.42 | 3/5 | 1 | +8.81% | +9.54% |
| 新興題材：BofA | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：AI散熱 | 0.00 | 0/1 | 1 | -17.21% | -16.16% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：7月上市櫃公司營收 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
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
| 2026-08-15 | 0.24 | 0.30 | +68.75% | 16 |

## 歷史回測摘要

- 回測日期：2026-08-15
- 近5日 3日相關：-0.10
- 近5日 5日相關：0.42
- 同向比例：+66.67%
- 權重狀態：未調整

- 方向準確度：+66.67%
- 信心排序準確度：-0.10
- 診斷：低相關

調整原因：近 5 日有效樣本 6 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits；Not Micron, Not Sandisk. This Artificial Intelligence (AI) Memory Stock Could Be the Next Nvidia. - The Motley Fool；Is Micron or Sandisk Better Poised For Upside Through The End of September? - 24/7 Wall St.

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.48 | N/A | N/A | 971.66 | 971.66 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.48 | +29.11% | +35.38% | 1,641.11 | 2,335.00 | -29.72% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.37 | +12.53% | +12.82% | 225.16 | 225.30 | -0.06% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.36 | N/A | N/A | 514.39 | 516.10 | -0.33% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.36 | N/A | N/A | 102.50 | 114.68 | -10.62% | N/A | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：boost, rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 5 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：boost。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits](https://news.google.com/rss/articles/CBMi0AFBVV95cUxOWm5KdEIwSXpyY191UEhDa1V6NVpWa01UbmpJeWRIV0ttT080TmpDNEhISW5TWkQwUzBVYzBqSHJPWXRVNVJCampoWWRlYmhKVkhIeHBJLS0wLW5Ua09GQnRORXpFcW5qTEJkcnJGcW55aU5rOFVOLUFMbjRPZEpWT3A2ZllucnM0SU9JNEdrNUwyc3V2WHAtNFk3VHl4R1F6SkZRMFpleEE2Zl9MdW4tSEpMMnFGZ2hQZURWQ3B1WDlPR1BhRjJELVN5ODJWYVR3?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 14 Aug 2026 07:29:39 GMT
- [Not Micron, Not Sandisk. This Artificial Intelligence (AI) Memory Stock Could Be the Next Nvidia. - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxNT1lqZTE3dmJEaW1sd0hsdGs2NWMzR2tycU1JLTlYVW9XUk1SM2ZoY0lGendPdmVTanNvNWpvRnIwTkxIdTVNRzg5TzZtMzA5ZUw0a25jZ1RYY1N6MFcxMUZ0UXVvYmM5M3ZZejNaYXJ0MVFuNDNib05FQVRXTkdpR3RjdVlWeWVTdjhUTURfdTFseXNLZTBTYg?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 14 Aug 2026 12:00:00 GMT
- [Is Micron or Sandisk Better Poised For Upside Through The End of September? - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiugFBVV95cUxOREJ5b1FjUmlGWWQ3cXB6ZnZOOFp0R3QwVGZGdHJ3aHdmdkJaN2FtN3BLdU9yRHlBa3JOQzdIa0QxQThVWFNSOHBHaEVLWHpsclFVdmNYREVFbzBQRUlwb0JhRUZleENiZnNlMEhObm9WQmxPOS1YSmhxVEZhSGZkOGpLcDBGd280RzM3TW5QNzlsMXV6WlpfNmtSOHJlS0FBRzQ1TTJsQnY1Q3hCdG5ibk5xUnFmTWwtcmc?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 14 Aug 2026 14:57:53 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：上半年EPS飆44元！「散熱大廠」Q2獲利翻倍創高 輝達Rubin、ASIC第四季放量業績季季漲 - ftnn.com.tw；焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報；〈焦點股〉奇鋐GPU及ASIC下半年同步放量 法說行情噴漲停新天價 - news.cnyes.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.57 | +17.21% | +16.16% | 3,235.00 | 3,235.00 | 0.00% | 同向 | 75.13 | 43.12 | 18.59B TWD / 57.39% | 2026-08-01 |
| NVDA 輝達 | 新聞直接提及 | +0.42 | +12.53% | +12.82% | 225.16 | 225.30 | -0.06% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱、奇鋐」，共 4 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：跌停, 放量, 創高, 噴漲, 漲停。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：放量, 創高。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [上半年EPS飆44元！「散熱大廠」Q2獲利翻倍創高 輝達Rubin、ASIC第四季放量業績季季漲 - ftnn.com.tw](https://news.google.com/rss/articles/CBMiS0FVX3lxTE5xbHJRczVrZi1maGhfN3UwaGVSa0hQYVdRVzFjTS1HbERzMTExdS0zb2xRNmpDS2RENTdkMFlJRkRpOVhQcklYSU5pVQ?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 13 Aug 2026 13:15:00 GMT
- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 13 Aug 2026 00:45:38 GMT
- [〈焦點股〉奇鋐GPU及ASIC下半年同步放量 法說行情噴漲停新天價 - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTE9xSm80RDg3RC12N0dzNGoyUlNKaU9Vc1ZIS3NkOERvU056Z2duYTRzcTN4VzB0ZXFMUzdoT2lsVHZpeUtfcGJiNGoySTV6M3M?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 13 Aug 2026 03:53:13 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：台股強彈高檔盤整 法人點名鎖定 AI 相關題材與落後補漲股區間操作 - 經濟日報；Intel stock holds at $100.95 amid mixed signals on foundry profits and AI growth potential. - Pluang；垂直 AI 投資如何強化企業門檻？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.54 | N/A | N/A | 102.50 | 114.68 | -10.62% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.06 | +12.53% | +12.82% | 225.16 | 225.30 | -0.06% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.06 | N/A | N/A | 514.39 | 516.10 | -0.33% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.04 | 0.00% | +1.05% | 2,395.00 | 2,435.00 | -1.64% | 未明確 | 86.28 | 27.76 | 467.58B TWD / 44.69% | 2026-08-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | +26.14% | -2.23% | 495.40 | 506.69 | -2.23% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.04 | +4.03% | -5.85% | 392.99 | 446.77 | -12.04% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.02 | -2.07% | +5.30% | 616.00 | 680.00 | -9.41% | 背離 | 13.92 | 44.57 | 73.78B TWD / 43.15% | 2026-08-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.04 | +4.73% | +7.95% | 4,210.00 | 4,310.00 | -2.32% | 同向 | 60.69 | 69.53 | 48.47B TWD / 12.16% | 2026-08-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [台股強彈高檔盤整 法人點名鎖定 AI 相關題材與落後補漲股區間操作 - 經濟日報](https://news.google.com/rss/articles/CBMid0FVX3lxTE1FTWNfa1NwOEpTRzFoeWViN1ltNEdFSlRubXlpb2VzcmpUUUNORWNRVWt4NjRZdUxDV3VNSWNNZ2hsNWNTOWduSmtkdHpXTWJBdjd4SkprM2dXWGJSczRILXNDSUZrSjljU0RrSmxwQ1dCYVBoVl9B0gFfQVVfeXFMTUFPUEpoMnZTNUlLa0Nua18zbTgxdmhmc043RUo1S2xTVzlzcXQ0Zl9zWjh0c1FDaFlsUlZWUThQcU5VMERybFhuN09wczk3T001b0Z2RW1kTjZ5RThodG8?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 14 Aug 2026 09:42:44 GMT
- [Intel stock holds at $100.95 amid mixed signals on foundry profits and AI growth potential. - Pluang](https://news.google.com/rss/articles/CBMif0FVX3lxTE1kbWltaDVmbmZ5M3NJWm1tYVV3N1pMY3JNaGhpbklQSXZZazM2S2xZeHhkV1RYVkl5S0F1Y1Vkak94eGxjamduMzFmTEUzeEVkOEVvTHoyblN4WmFoUTV5ZXBudlRIZW91WmdYWE5vaW9TaTREYnhPVFVnZ0lCVmM?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 13 Aug 2026 13:57:29 GMT
- [垂直 AI 投資如何強化企業門檻？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMicEFVX3lxTE5hc2RCUU9Rd3pSdTNBcHEzUUhyMkZCOU1pRHltbFZiX194aXhPNjl2dm9nemVVbEg4VWk2UWlnb29Uay1QQWtwemp2cFQwM0JTQ01DR3d4YVhsaWYzWHNuY0F4ZkhmWGM2bDF0RWcwZjg?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 14 Aug 2026 15:19:26 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：The Bull Market Is Almost Back for Chip Stocks - Investopedia；Intel stock holds at $100.95 amid mixed signals on foundry profits and AI growth potential. - Pluang；達興半導體動能靚；H2再增5項產品準備驗證- 新聞 - MoneyDJ理財網

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.52 | N/A | N/A | 102.50 | 114.68 | -10.62% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.03 | 0.00% | +1.05% | 2,395.00 | 2,435.00 | -1.64% | 未明確 | 86.28 | 27.76 | 467.58B TWD / 44.69% | 2026-08-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.02 | -1.63% | +4.31% | 121.00 | 164.50 | -26.44% | 背離 | 6.68 | 18.20 | 23.84B TWD / 18.98% | 2026-08-01 |
| NVDA 輝達 | 產業/供應鏈推估 | +0.03 | +12.53% | +12.82% | 225.16 | 225.30 | -0.06% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.03 | N/A | N/A | 514.39 | 516.10 | -0.33% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | +0.03 | N/A | N/A | 971.66 | 971.66 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.03 | +29.11% | +35.38% | 1,641.11 | 2,335.00 | -29.72% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.03 | +4.03% | -5.85% | 392.99 | 446.77 | -12.04% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 2 篇新聞出現相關標籤。 方向判斷命中詞：growth。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 2 篇新聞出現相關標籤。 方向判斷命中詞：growth。

### 主要來源

- [The Bull Market Is Almost Back for Chip Stocks - Investopedia](https://news.google.com/rss/articles/CBMijAFBVV95cUxNWm9VRXdUMHoyeEVoTDRXZjhhUjVXOUYyTDB0WXU4QXR2QXJGMk9ZQ0Vqb2dkMzlzTnhSLXhkb25OUmRZZlB0R0UxSmhkdDhPR29mMld1alhvVkJ0Y3pOclZ6cHQyMnBhVUNaRTd2V0cwVXgyMEV4c3JsT2RwTTJWMzlwdUFxZWJWRXJwSw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 13 Aug 2026 20:55:54 GMT
- [Intel stock holds at $100.95 amid mixed signals on foundry profits and AI growth potential. - Pluang](https://news.google.com/rss/articles/CBMif0FVX3lxTE1kbWltaDVmbmZ5M3NJWm1tYVV3N1pMY3JNaGhpbklQSXZZazM2S2xZeHhkV1RYVkl5S0F1Y1Vkak94eGxjamduMzFmTEUzeEVkOEVvTHoyblN4WmFoUTV5ZXBudlRIZW91WmdYWE5vaW9TaTREYnhPVFVnZ0lCVmM?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 13 Aug 2026 13:57:29 GMT
- [達興半導體動能靚；H2再增5項產品準備驗證- 新聞 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikgFBVV95cUxQNmFlVHN1ZlNyZFFJekJPbFBCV2c0ZGozSDQ3U3k4U2RrN01aaHJTd05sNWYydHhmcWRNYlRnbkd3UWFRNEtNdERkeU1CaDF4NTFJMTBmSmduUjJ2eW5JNWtqV1d6OGVYV0FOZm5Qa0pxS054TGtqdW95MzNvbXdZWW9vWUJhbC10WkdkR01uWFhIZw?oc=5) - Google News source discovery | MoneyDJ Fri, 14 Aug 2026 06:33:00 GMT

## 新興題材：BofA

摘要：新興題材：BofA 相關新聞集中在：Broadcom Sinks 6% as BofA Flags $370B in AI Debt, AMD Climbs 4% on Baird's $1,250 Call - 24/7 Wall St.

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AMD 超微 | 新聞直接提及 | 0.00 | N/A | N/A | 514.39 | 516.10 | -0.33% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | 0.00 | +4.03% | -5.85% | 392.99 | 446.77 | -12.04% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AVGO：新聞直接提及「Broadcom」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Broadcom Sinks 6% as BofA Flags $370B in AI Debt, AMD Climbs 4% on Baird's $1,250 Call - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiwAFBVV95cUxQdFk0NXo1bmRxMm4tQWkzRzE4alhISF81ZFpOM3JnWXB5c0oyaWpRS1phWU5MYUNhRXYyTTN0b3RPd3lLUlNnQnEzOUM1Y083U3l5RHNrck84LWU4bVZEREpacnRBT3VHWVFwZlcwOVFsX19ROXpTakQ1ek0tN3l0cHNEcGV2ay1hQ1VfQXRtZFJtM01DT1Z1VGc5V2JZcmtRRmNxNktrdE9vck05TkozandkM3JUQmZUYWVjVXhIOWg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 14 Aug 2026 18:07:38 GMT

## 新興題材：AI散熱

摘要：新興題材：AI散熱 相關新聞集中在：焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | -0.21 | +17.21% | +16.16% | 3,235.00 | 3,235.00 | 0.00% | 背離 | 75.13 | 43.12 | 18.59B TWD / 57.39% | 2026-08-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 1 篇新聞命中。 方向判斷命中詞：跌停。

### 主要來源

- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 13 Aug 2026 00:45:38 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：《台股盤後》收跌210點、5日線有守；周K連二紅- 新聞 - MoneyDJ理財網；MSCI季度調整：臺股於全球ACWI、新興及日本除外亞洲權重各上升0.05、0.25、0.28百分點 - MoneyDJ理財網；8檔台股ETF交投熱絡00685L登績效人氣王- 新聞 - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》收跌210點、5日線有守；周K連二紅- 新聞 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikgFBVV95cUxNLWVtUXdHV3JlczBLRWtXYmZCTjZEQ3JHaDN3YnFONEJIRFRmbFlBVEVHM2ZwVUQxWDNJX3pWWW5Ja2Jrc0twZENfQUxjMV8zdUk0NXlSa2RIenlQUXFjNmFubjlyUHlsa1ZrZHplR3Q1LXFrVjBNV3ZxOEF3cDBIYjhJckFfSjdVU3ZBSDlELUVKZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 14 Aug 2026 07:45:00 GMT
- [MSCI季度調整：臺股於全球ACWI、新興及日本除外亞洲權重各上升0.05、0.25、0.28百分點 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMieEFVX3lxTE9ua0hDWmpDaEV5VGhMSFgycHpNV0d0c3lCajJHRHl2UlF0R2N5X2lPb0JvUTdjSDYtVVl3ZTNlUTlsN1AtcHh3WVBsZlI1eXNGRXU2NE1lenNNZHVBVlFGa21oQk5Nanl4anlUY0ZiRlJZczhnZ2c0cw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 14 Aug 2026 00:01:00 GMT
- [8檔台股ETF交投熱絡00685L登績效人氣王- 新聞 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikgFBVV95cUxPbmVqVVk1bWRNWERsdHlxZEt6MzhnVHVUNXNla3VrSk5nQ3BrcVg2YnlzQ3V2SUM4TlpOQWpYTnhMX1BGLUdfSHdCWEp1dlFZbjFqS1h2bUE3ckFjbEJNN0VWTGhZOHBpN3RaTDNuRi14V1FodWhQd0k1Rjk0N3JDeHRpbDgteWNkTDNKVWVVLXRxZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 14 Aug 2026 02:36:00 GMT

## 新興題材：7月上市櫃公司營收

摘要：新興題材：7月上市櫃公司營收 相關新聞集中在：7月上市櫃公司營收亮眼 中信投信：台股第4季可望延續多頭行情 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [7月上市櫃公司營收亮眼 中信投信：台股第4季可望延續多頭行情 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE03cTRMQzh1WG9RWmsxVkVNdktaUUNfUEE1VUFUcTRabTVkRWdwZlNHYnNQNnhELWpmN0x6eUh0NWZoa0pyV0k5NGI3aExNdGw2SUJ1d09SNnA5Z9IBX0FVX3lxTFBUU2psRUVRQ0NOVXlEbXUtYjBzUEFrWEMtRFZSUF9kZUlQb2RsenVTQ2xnUE45akgwYVBnUDY0ckVmaGxzeWt4aDYtdF9FYWI5SnpaTUZxWGhJdDQwb1hv?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 14 Aug 2026 08:36:59 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
