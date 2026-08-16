# 每日股市熱門話題分析 - 2026-08-17

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜正向｜熱度 4｜市場確認 100.00｜同向 1/1
2. **半導體與晶片供應鏈**｜正向｜熱度 9｜市場確認 68.42｜同向 3/5
3. **利率與成長股估值**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0
4. **AI 伺服器與資料中心**｜正向｜熱度 7｜市場確認 69.35｜同向 4/6
5. **新興題材：TradingKey**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.49（樣本 12）
- 5日相關係數：0.60（樣本 12）
- 同向比例：8/12

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 100.00 | 1/1 | 0 | +29.11% | +35.38% |
| 半導體與晶片供應鏈 | 68.42 | 3/5 | 1 | +8.81% | +9.54% |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 69.35 | 4/6 | 1 | +7.56% | +3.17% |
| 新興題材：TradingKey | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
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
| 2026-08-16 | 0.37 | 0.51 | +70.00% | 10 |
| 2026-08-17 | 0.49 | 0.60 | +66.67% | 12 |

## 歷史回測摘要

- 回測日期：2026-08-17
- 近5日 3日相關：0.34
- 近5日 5日相關：0.18
- 同向比例：+30.00%
- 權重狀態：未調整

- 方向準確度：+30.00%
- 信心排序準確度：0.34
- 診斷：正相關

調整原因：近 5 日有效樣本 10 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits；Is Micron or Sandisk Better Poised For Upside Through The End of September? - aol.com；Social Media Went Negative on Memory Stocks like SanDisk & Micron Last Weekend. Then They Rallied. - 24/7 Wall St.

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.48 | N/A | N/A | 971.66 | 971.66 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.48 | +29.11% | +35.38% | 1,641.11 | 2,335.00 | -29.72% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.36 | N/A | N/A | 514.39 | 516.10 | -0.33% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.36 | N/A | N/A | 102.50 | 114.68 | -10.62% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +12.53% | +12.82% | 225.16 | 225.16 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron、美光」，共 4 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 2 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits](https://news.google.com/rss/articles/CBMi0AFBVV95cUxOWm5KdEIwSXpyY191UEhDa1V6NVpWa01UbmpJeWRIV0ttT080TmpDNEhISW5TWkQwUzBVYzBqSHJPWXRVNVJCampoWWRlYmhKVkhIeHBJLS0wLW5Ua09GQnRORXpFcW5qTEJkcnJGcW55aU5rOFVOLUFMbjRPZEpWT3A2ZllucnM0SU9JNEdrNUwyc3V2WHAtNFk3VHl4R1F6SkZRMFpleEE2Zl9MdW4tSEpMMnFGZ2hQZURWQ3B1WDlPR1BhRjJELVN5ODJWYVR3?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 15 Aug 2026 06:55:03 GMT
- [Is Micron or Sandisk Better Poised For Upside Through The End of September? - aol.com](https://news.google.com/rss/articles/CBMihgFBVV95cUxOdS1KR0lnaGRRYnU3dFRPMXk3dlEzeHFWMjVKbzlkQUs1V3AyQUFNUHdyQ2FTM3d4N2k4RVNwRnpFeGFhU002SC1BYzgyZ1k1Njl4SDQ0UEViZmJFMzd0ZElCZXNnbmkySTZuMmtFemtVeng0YmMzS2FQQ1RBa2ZiNHFoOUhyUQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 16 Aug 2026 13:21:41 GMT
- [Social Media Went Negative on Memory Stocks like SanDisk & Micron Last Weekend. Then They Rallied. - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi1AFBVV95cUxNb0NXR3BnT2g0TjRzZnJNeW9lVjFVZFRBVXNPaTFSTmJQMURZRFdSX1BKMHBXNFBYNEtVZ0F3Vl9nN1p4VWpOZmFiRkEybFdub1V1V3MyX2VBMUJoczNOb1Y3aXAyM2pCQ2pqZU5OaEFQTmJ0VnloWjJHeUk4WXNlRjNhb2tIUGZ1ODhXZnFoMW5SRHYxZ3g2MHo0Nm95cm1lZWpzM0VWSmJpUS1Nd3cyZzVBeHA1azRheG1sQ0s3TmVjeW1vaFpVcWlRa09CWVR5dlB1Vg?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 15 Aug 2026 14:43:38 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：S&P 500 Hits Record High in August 2026: How AI Chip Earnings Are Fueling the Historic Rally - Intellectia AI；美來台修讀STEM學位達百人續推半導體人才合作| 生活 - cna.com.tw；半導體 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | +0.08 | N/A | N/A | 102.50 | 114.68 | -10.62% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.04 | 0.00% | +1.05% | 2,395.00 | 2,425.00 | -1.24% | 未明確 | 86.28 | 27.76 | 467.58B TWD / 44.69% | 2026-08-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.03 | -1.63% | +4.31% | 121.00 | 164.50 | -26.44% | 背離 | 6.68 | 18.20 | 23.84B TWD / 18.98% | 2026-08-01 |
| NVDA 輝達 | 產業/供應鏈推估 | +0.04 | +12.53% | +12.82% | 225.16 | 225.16 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.04 | N/A | N/A | 514.39 | 516.10 | -0.33% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | +0.04 | N/A | N/A | 971.66 | 971.66 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.04 | +29.11% | +35.38% | 1,641.11 | 2,335.00 | -29.72% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.04 | +4.03% | -5.85% | 392.99 | 446.77 | -12.04% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 CPU, server CPU, x86, foundry；其中 1 篇新聞出現相關標籤。 方向判斷命中詞：rally, record high。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 1 篇新聞出現相關標籤。 方向判斷命中詞：rally, record high。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 1 篇新聞出現相關標籤。 方向判斷命中詞：rally, record high。

### 主要來源

- [S&P 500 Hits Record High in August 2026: How AI Chip Earnings Are Fueling the Historic Rally - Intellectia AI](https://news.google.com/rss/articles/CBMigwFBVV95cUxNWkZXTW9uZ2VJRFUwSG1EZ3p6dzYwWkVKWmRoNVZhbnBJcHoyeXpDOVdURm1NNVRSb0hyQ0FHQThmQ2tDdDBmOUVsVnpwMmlOVUhmV182LTBfbHlnQXJPM0lncjhWUGloOExzT0JTcnBqbkVXQXY2OW1Ub3ljdG43V2pFOA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 16 Aug 2026 00:16:43 GMT
- [美來台修讀STEM學位達百人續推半導體人才合作| 生活 - cna.com.tw](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBOT3NPWlhyU2dxZzhfbHE0d2tkRDh3YVdCakM4UkZ5blNzUWJfVzlycWlJS2pxVEs0d2FFM3k3aGMtVzJjaHFvazFxd3RFOHhQeklaNVhDQ1VYcUpURVNz?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 15 Aug 2026 05:31:00 GMT
- [半導體 - TechNews 科技新報](https://news.google.com/rss/articles/CBMicEFVX3lxTE9lMDllMEYyanFUV3pvM3dleXM2dlJjMkptRjk5cll4LWlDSnJnZ3lVRXZuYzc4UXJNOWYtLTJkU2N5M3VMZzRmUjByMjROTXhXUHJGRVQ0TkZnTkhMcXVPY0NZTDBpVm9OLVB0X2pnMnc?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 16 Aug 2026 20:32:56 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：法人看AI趨勢未變台股短線需留意通膨| 證券 - cna.com.tw；Inflation moderated as Intel and Nvidia fueled the AI trade in last week's market - CNBC；本週操盤筆記：Fed會議記錄、各國PMI初值、日GDP與通膨數據 - news.cnyes.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +12.53% | +12.82% | 225.16 | 225.16 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 102.50 | 114.68 | -10.62% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +26.14% | -2.23% | 495.40 | 506.69 | -2.23% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [法人看AI趨勢未變台股短線需留意通膨| 證券 - cna.com.tw](https://news.google.com/rss/articles/CBMiXkFVX3lxTE03LVV2T3JZS3lhM29lSGJzSzZxbVFvRVRPR1pjV0JSbVRwQlpaUnV5ZzZRRzZ6U0VJNFBjUk5fX2NXbWN4LUN0a3BDOFU0dWJfYVhSZjNPaDVpVUlRMnc?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 16 Aug 2026 02:01:00 GMT
- [Inflation moderated as Intel and Nvidia fueled the AI trade in last week's market - CNBC](https://news.google.com/rss/articles/CBMitwFBVV95cUxOTXozT0VsTTdYQzZiRVo0YnBqMXhqTjdOd1h4VkNBVXBBLV94dmdRLUFrQUZHYWJWWFhmU3hidWZrRDFhMV9rR0xkMHVvZ0MtVzFrLXBaMTMxOVFKUU1zTF9OQThHYWxqQkprRjBBR0FTSU1tOENFa2RyUGJLeXZWV3hRVmtyUW1PUTJKcmtsYjNTV1lNdDZ6S3ZObldnRldQeS03SFFvLWU3dXZGS2lHV1dQcnNuYVk?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 15 Aug 2026 14:22:54 GMT
- [本週操盤筆記：Fed會議記錄、各國PMI初值、日GDP與通膨數據 - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTE4yWTJHb0JndllneHZPck1IMkFKZDIyUHRkT1h3bkhzWVdGRFBhaTR1VjNNVEF0QktfOEpPOHBveV9UMU1GWVBZZTRwZkF3RkU?oc=5) - Google News source discovery | 鉅亨網 Sun, 16 Aug 2026 13:50:02 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Is Intel’s US$20 Billion AI-Focused Equity Raise Reshaping The Investment Case For Intel (INTC)? - simplywall.st；S&P 500 Hits Record High in August 2026: How AI Chip Earnings Are Fueling the Historic Rally - Intellectia AI；AI 如何重塑科技業性別分工與人才佈局？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.54 | N/A | N/A | 102.50 | 114.68 | -10.62% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.06 | +12.53% | +12.82% | 225.16 | 225.16 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.06 | N/A | N/A | 514.39 | 516.10 | -0.33% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.04 | 0.00% | +1.05% | 2,395.00 | 2,425.00 | -1.24% | 未明確 | 86.28 | 27.76 | 467.58B TWD / 44.69% | 2026-08-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | +26.14% | -2.23% | 495.40 | 506.69 | -2.23% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.04 | +4.03% | -5.85% | 392.99 | 446.77 | -12.04% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.02 | -2.07% | +5.30% | 616.00 | 680.00 | -9.41% | 背離 | 13.92 | 44.57 | 73.78B TWD / 43.15% | 2026-08-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.04 | +4.73% | +7.95% | 4,210.00 | 4,310.00 | -2.32% | 同向 | 60.69 | 69.53 | 48.47B TWD / 12.16% | 2026-08-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：恐, raise, rally, record high。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：恐, raise, rally, record high。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：恐, raise, rally, record high。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Is Intel’s US$20 Billion AI-Focused Equity Raise Reshaping The Investment Case For Intel (INTC)? - simplywall.st](https://news.google.com/rss/articles/CBMiygFBVV95cUxQS0I4U3kwOF9nek4zS1JsSGtleE05UmlUdklRMG5WX0h2Y2xuUE8yRVZZX0dpUXd2Z0l6dkpEUFgzX0l3TWU4UEVuNDZuRktRcVRMOFAwMHNXdXROeVozNDFvaDlCZmNVQWN6c0Nld3Q0ckR1NXNmd1A3SGlwbUdTZkVibnZROFp6TW1xakJwNklQMFJCY1Nod2lTbGFVdVdYSzNQMWFOWHV4VHkwTS1NdWl5ME1RN1NkV19GQ3dmMHVwaF9CNFpiNjBn0gHPAUFVX3lxTE1pS2Utc0tTbTRwSnoyajFrTHp4dXdoMzFfVWVZNXdxVHRNOFNLclQ3WHZaR1MtZ3F1cVpwUktxSHg5MG5GWmxfd2xrT3Y1WDdrQXRYd0tFTjB3U2Y3Mk1GcGVaVjZTMERqRTVSLVhrSDBxdmUzdkhWb0tlTEJIcjBPOThLWDdFYlg5N3lMSld4OTdDZ0ZEUXdqamlGWTZtWEtVQm5VTTEtV3o0aVVoTmVtanRhRks2eXFfLWstb3dLYkp0RlYzeFBPQmljQ09ZNA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 15 Aug 2026 18:30:35 GMT
- [S&P 500 Hits Record High in August 2026: How AI Chip Earnings Are Fueling the Historic Rally - Intellectia AI](https://news.google.com/rss/articles/CBMigwFBVV95cUxNWkZXTW9uZ2VJRFUwSG1EZ3p6dzYwWkVKWmRoNVZhbnBJcHoyeXpDOVdURm1NNVRSb0hyQ0FHQThmQ2tDdDBmOUVsVnpwMmlOVUhmV182LTBfbHlnQXJPM0lncjhWUGloOExzT0JTcnBqbkVXQXY2OW1Ub3ljdG43V2pFOA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 16 Aug 2026 00:16:43 GMT
- [AI 如何重塑科技業性別分工與人才佈局？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMitwFBVV95cUxOLXlpUHBxSjBhUHNLVTBkZ3plWW9uQzk5R19QR3hIcm9ubnhicFhwMGFaTVBqRURzQ0QwR1FMajlvcWZjdnBEa3lfZXlSYlpfTDhxRTQyRU9nZ0Zsa0tVN2tDbTBZb2czNHc4SWlXUy1pN2pHaDFicU5aUmZEN21nLUtZREg4QWR0ZTVqWjdsV2IyZmRlV1plS1AxdElfdmd4U1EtZE9PR0dXdFlRRjBVbm1XdHZZQ0U?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 16 Aug 2026 17:46:22 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Intel Price Forecast: Nvidia Picked Xeon 6, Invested $5B, Yet Analysts Still Trail INTC - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +12.53% | +12.82% | 225.16 | 225.16 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 102.50 | 114.68 | -10.62% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Price Forecast: Nvidia Picked Xeon 6, Invested $5B, Yet Analysts Still Trail INTC - TradingKey](https://news.google.com/rss/articles/CBMi6AFBVV95cUxPUTJ0M002eEJBWW5ocUl6ai1nTkJ1WjFMMktJRWtzekFRcktQd1d1MTFOd1RwbVFQWk9hU25UUC16RzBnbXBXdWZwcE5pS2ROeVN1YXhFZlNjVVctMWg4SWI1Y2FJazZTOTg2OVd0OWpmMGFKczk0ejdZX090Mkg2TU1Tc2Z4b2EwaUJ5MkxITm1NLWxic2JFdDVJRGZjdTBwbVNETDFURk1jMHBQN0ZQV3BhYVcyT2JDYWR2S1hLMERJNWc1bmVwODBxcUN1YUdxMlNQemdJbktvdzQxV0pmZXVIX1Zfam5N?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 16 Aug 2026 01:55:13 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：目標價直奔4005大關！「這散熱大廠」吃爆AI四大平台 明年EPS估衝160元 - 三立新聞；半導體、散熱、ASIC 長線向上 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | +17.21% | +16.16% | 3,235.00 | 3,235.00 | 0.00% | 不適用 | 75.13 | 43.12 | 18.59B TWD / 57.39% | 2026-08-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 2 篇新聞命中。 同時符合主題標籤：thermal。

### 主要來源

- [目標價直奔4005大關！「這散熱大廠」吃爆AI四大平台 明年EPS估衝160元 - 三立新聞](https://news.google.com/rss/articles/CBMiS0FVX3lxTE9vY0FuT3Y1OGJLUVhGSHhvOF9jMDVkdWd3amhtdmxvMEZkLWlxeW5ZLVlVMGhnT2hfZVVIeGl5eUlHTjJieG5jRDMxYw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 16 Aug 2026 17:02:18 GMT
- [半導體、散熱、ASIC 長線向上 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1GTjhTby1SVTh2bERhdlRRcTNLajBVRkxWTkN1T3ZKX19sbXVXUXIwVVNOQkp2WjJRZXcyeGRCenJ0UDJLM3VxT2ZhcUJxbWtpVXVTQ2pQQ2NyZ9IBX0FVX3lxTE9EdFRUc05paXVYdjlfR1JGa2pZYlFvUVdpaTd3YjlNZjNwb0V0QkhERTVNaWtiTmd2Y1Jnblgzc1ZacnE5SmtPXzhYcERKRFc3eThlNDVyaUlLZlZieDlN?oc=5) - Google News source discovery | 經濟日報 money Sun, 16 Aug 2026 17:00:09 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：產業評析-反彈滿足，好股盤整見真章 - MoneyDJ理財網；台股多頭重掌AI主旋律 - MoneyDJ理財網；查詢民國 (yy/mm/dd) 以前的相關新聞輸入日期 - 6480.moneydj.com

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [產業評析-反彈滿足，好股盤整見真章 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilgFBVV95cUxPNFFtbksyQUlIM0VUSDBBQmV2MHRrUlpJX2pIZVMwcGZ3bE9jZE82ZDNGQnQ0QkxRX2Q4cjZDaElBT1Z5RlRMNmRFcGxFa0FOTjR6bU1qQ3RaaFJRMGJnMGpKUHhJdldncDU5TVI3SkU3YmV0dnVqWHdnVkhKMWZNTEpKLTM3UWhqOTFVUF9pUGxtVE9welE?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 16 Aug 2026 16:29:39 GMT
- [台股多頭重掌AI主旋律 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMieEFVX3lxTE00aHY0bjNja2pvbE0xZV9qWGNOelZybDlwMnVaMFdhdGpKRW1vR3A2VTFMbE5jamRuaFlzclVabnBydElxYi16dzZHU21wb29abjBoWTRva0JwaXBPX0lwSW1WcDI0NnFlamsySm5BM0dQdWtXNlk1Qg?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 15 Aug 2026 01:10:00 GMT
- [查詢民國 (yy/mm/dd) 以前的相關新聞輸入日期 - 6480.moneydj.com](https://news.google.com/rss/articles/CBMiZEFVX3lxTE81cll2OGV6Tks4bHE4UmJUczJHc0ZuOGMwcm0tRWtTQTNYeFB1NkdVbHE3SkFYcEdJLXZra0lWSlFZY0V3MVZYbTFtazhrc1lVa0tQTDVxM1d5dHY2SUFlQ2dCNDU?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 15 Aug 2026 17:35:14 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：元大-大甲 對 遠百(2903)個股 單一券商歷史明細 - MoneyDJ；個股相關新聞-0537.HK - MoneyDJ；個股動態報導內容-9AC7A72A-8308-4653-A5EF-100E5A257997 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [元大-大甲 對 遠百(2903)個股 單一券商歷史明細 - MoneyDJ](https://news.google.com/rss/articles/CBMikwFBVV95cUxOUHB4b2pjMzB2YzU3dThrRmZpbnp3T3FLWi16bjZINDlGWjRTd0V0WUF6eUJGa2dReHJXb3c3a01CUl9sOGtXaHBmWG9fMlV2STl6N2ZJNHFFWUNmcmtlanRoUkJKNXFSTFdMb3E3OGtIbmxwbzluV0RYelcyeDF0ZFlvRFJZaWlFbkgtQjVxa3h4RHM?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 16 Aug 2026 01:02:21 GMT
- [個股相關新聞-0537.HK - MoneyDJ](https://news.google.com/rss/articles/CBMibkFVX3lxTE5GLUpjRW1XaW92bFpxcnh0NUNjZzVRMVhLaTNTN1Z1WDlzdVo1N1BHWnFXZXM3anZwdFlRclZtQjRxS2xtTmhqbk4yYUt2dmFKUnVHVlI3dVRyMzFCT3VBQWUwX0NqRW5GX21OaXl3?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 15 Aug 2026 21:46:59 GMT
- [個股動態報導內容-9AC7A72A-8308-4653-A5EF-100E5A257997 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxQQjM3TEE4RjhhWXBKSWxvOWYtUUxITTBzN3ZyeUZlYmdfZ3NNMEZnZzN4U3Z4R095LXRpYldCS3k2bU5DSUhVcklmSUhua1BrM2JjcVgxcVkwVUpUZHNIWWRxanEzYlVtZjYxWXBqTW5SR2JiMlNCdThZcmZzM3BpdXc0N21nTHBmaXRMMXl5dkptU3Z6?oc=5) - Google News source discovery | MoneyDJ Sat, 15 Aug 2026 07:15:28 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
