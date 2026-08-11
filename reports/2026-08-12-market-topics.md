# 每日股市熱門話題分析 - 2026-08-12

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **AI 伺服器與資料中心**｜正向｜熱度 17｜市場確認 98.33｜同向 6/6
2. **綜合市場情緒**｜正向｜熱度 40｜市場確認 N/A｜同向 0/0
3. **記憶體與 HBM 供應鏈**｜正向｜熱度 7｜市場確認 49.53｜同向 1/2
4. **半導體與晶片供應鏈**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
5. **先進封裝與 CoPoS**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.52（樣本 8）
- 5日相關係數：-0.47（樣本 8）
- 同向比例：7/8

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| AI 伺服器與資料中心 | 98.33 | 6/6 | 0 | +9.44% | +3.81% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 記憶體與 HBM 供應鏈 | 49.53 | 1/2 | 0 | +4.84% | -0.99% |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 先進封裝與 CoPoS | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：D96FDB8063B2 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：加速半導體晶片 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
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
| 2026-08-12 | 0.52 | -0.47 | +87.50% | 8 |

## 歷史回測摘要

- 回測日期：2026-08-12
- 近5日 3日相關：0.35
- 近5日 5日相關：-0.21
- 同向比例：+28.57%
- 權重狀態：未調整

- 方向準確度：+28.57%
- 信心排序準確度：0.35
- 診斷：正相關

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

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel's huge rally is helping pay for its AI comeback: Chart of the Day - Yahoo! Finance Canada；Intel upsizes stock offering to $20 billion at $95 per share as AI demand accelerates - CNBC；AI 代理損害責任，法律歸屬如何界定？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.57 | N/A | N/A | 97.71 | 114.68 | -14.80% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 新聞直接提及 | +0.50 | +28.28% | -0.57% | 503.81 | 506.69 | -0.57% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.06 | +8.70% | +8.98% | 217.50 | 223.96 | -2.88% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.06 | N/A | N/A | 474.32 | 516.10 | -8.10% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.06 | +1.27% | +3.23% | 2,395.00 | 2,425.00 | -1.24% | 同向 | 74.39 | 32.20 | 467.58B TWD / 44.69% | 2026-08-01 |
| AVGO 博通 | 產業/供應鏈推估 | +0.04 | +10.15% | -0.32% | 416.08 | 446.77 | -6.87% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.04 | +5.71% | +7.52% | 629.00 | 680.00 | -7.50% | 同向 | 13.92 | 45.51 | 73.78B TWD / 43.15% | 2026-08-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.04 | +2.55% | +4.01% | 4,020.00 | 4,310.00 | -6.73% | 同向 | 60.69 | 66.39 | 48.47B TWD / 12.16% | 2026-08-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 2 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MSFT：新聞直接提及「微軟」，共 1 篇新聞命中。 同時符合主題標籤：AI, datacenter。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel's huge rally is helping pay for its AI comeback: Chart of the Day - Yahoo! Finance Canada](https://news.google.com/rss/articles/CBMiugFBVV95cUxPTnVyQktSZVBWR180U01yWmtRVGVoUk02dVl5ZE5JRFhhTW1DVUFrZDk3b1ZQUk95WndQeUwwaUtTYmxzdzhyWV9FdFlZeUh0ZHpEN3BhalpkU3JBQ3JzSDNkdEw1eDhUb09DTnVveGp1R0ZBeVdKT244ZXZFOGN3Zk5EaFJ5UEhVVG5xTjRadHRobmZlRnk3TFVCVzNhN2tqZ2VZdE02RGVrYUpMQXNTRV92UExNYlZKbUE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 11 Aug 2026 12:40:42 GMT
- [Intel upsizes stock offering to $20 billion at $95 per share as AI demand accelerates - CNBC](https://news.google.com/rss/articles/CBMic0FVX3lxTE9wLUxnRncxa2pNdGoxaFhBVnZzNU40Qks5MDFnSFJ5eHAzdWo0RGluXzctenFpbmREckVJQkFhTHJMREdNbnZaeDNtYnNDQnBxckd3bGZ2Qm1xbU9ZaW01bkQwNnRvdUFRUUVjYXpyT2JxSjjSAXhBVV95cUxOUFZTSFNOX3hPb2lHTzhMMXdESmV6anV2SlNObC1wZmNDM3RmUmtVdXdfMmpETzkxTmVROG5Idy00V1Q1UEt4b1VEaS1aZEdRRXBYNmZKbGotSU0yNkNPMDJZcHZsU29zMTdWekNHSUNWT2lBellmMlc?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 10 Aug 2026 12:49:52 GMT
- [AI 代理損害責任，法律歸屬如何界定？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiaEFVX3lxTE8xS19jZVp1eTViS1p0RmNWTXIzeEpzMS05OXFxR293a18xR2syWjAxSmNuLWl3eUhKTEI2bnBfR3psY0FENHhoeHFubFVZY1pwTlNveUUwODBzblJ0M0FyRnZodnluVkVO?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 11 Aug 2026 18:38:19 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股先殺多再軋空收復45K 外資動向、油價、處置股新制牽動後市 - 經濟日報；台股反彈的資金去哪了？ETF 約487億撤出 這幾檔反而被買爆 | 基金天地 | 理財 - 經濟日報；台股震盪逾500點收漲191點　多檔被動元件攻漲停 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.42 | N/A | N/A | 97.71 | 114.68 | -14.80% | N/A | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 方向判斷命中詞：raise。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [台股先殺多再軋空收復45K 外資動向、油價、處置股新制牽動後市 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE4tWm9ZaGFuQVVyYVpwRjAwZWI2U3djbWJyTmJtRTVVQlNvazZLSFdvbXZvQmlvb3dNcGl0QmFZLXJvSWo5QTVRajZuVXRwNlV1Q1lhXzFfV2ZJd9IBX0FVX3lxTE8zczM3bUxhbFNQRDV0NnhYWlpFLXhKV3RFcktPWjdSanFRbHRNRElyZEtWa08zOXZHYllxamNjRUxYOVplb0ctTUVWbHY5MXlOUDctOXo5bzdXcUlzZDFF?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 11 Aug 2026 17:14:25 GMT
- [台股反彈的資金去哪了？ETF 約487億撤出 這幾檔反而被買爆 | 基金天地 | 理財 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBUTmpvZXpTNzJ0SXNDbGJHYmNmbzVLTVF2bUUtOS1taUpGLXQya0VvR2pvOXFJWU5xaUw3a3pDeE1HSzNmQUJlNklmalI3VzJqZl9pd2lPcHdNZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 11 Aug 2026 15:05:34 GMT
- [台股震盪逾500點收漲191點　多檔被動元件攻漲停 - 經濟日報](https://news.google.com/rss/articles/CBMieEFVX3lxTE5qTmxoa1BPS2xHTFFGQ0Q2UGhsdzhCYlJ6ZFBvalBwMFVCaW1CSlJ2UFFvV2M4Yy1SaGQyV0l0dlRuUU44V1p5MnRnS25NV0xhRnFwWW9IakhJbDF3VENWQzY5aGE5VENMMWNDSF9GZnB4M3NGSlRzc9IBX0FVX3lxTFBzYkdnMlhDVnRfS1ZpdFpFSk1SUVJDWnBta1JsUkdRUk8tMWJsM2k0dU5EZDViU1dLNE1Gcnh2U1F2TFZIb2FKYnBIbC1FNkNBaGhGRG5VYlBkMlViVjRJ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 11 Aug 2026 06:21:47 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：台股開低走高 投資人搶買面板、正2、記憶體 零股成交第一0050 - 經濟日報；The Undeniable Reasons Why Micron Stock Is a Buy This August - 24/7 Wall St.；What Just Happened To AI Stocks? (Micron, AMD & Nvidia Explained) Francesco Gabbani (qUyiUiHK0V) - Mshale

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.48 | N/A | N/A | 868.52 | 971.00 | -10.55% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.32 | +0.99% | -10.97% | 1,271.05 | 2,335.00 | -45.57% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.37 | +8.70% | +8.98% | 217.50 | 223.96 | -2.88% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.36 | N/A | N/A | 474.32 | 516.10 | -8.10% | N/A | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、memory」，共 3 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：surge。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 1 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：surge。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [台股開低走高 投資人搶買面板、正2、記憶體 零股成交第一0050 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxQU29tTi1zcDNxTWNiNWFBaDBmTFNraTRkZy12RUdJalh2OFNaV2piWVVMOVZGN2hlV1BmYkQ3U1NmU05XU3hNS1FVWHlpQUZIUlE4T3hNREx1QVNYREtmckZ1b1c1SGtMOS1sMXVkZGZTOWx0NGhhOFRuOUVkZDA5QdIBX0FVX3lxTE1oTU5DVDYxbDVRTlNIbTlneGNfVXZOZlJqNVRxMWNqMmhZSFp5VjFXcVRBYnlXUmszQU9FNzdPUWJTMkVlRGNfZzEtT2dDaHRjOVlUUnBicFN3YTVVS3I0?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 10 Aug 2026 09:00:00 GMT
- [The Undeniable Reasons Why Micron Stock Is a Buy This August - 24/7 Wall St.](https://news.google.com/rss/articles/CBMipwFBVV95cUxNQXJqYkE3RUY2bUQ4ZlNSelFXMWpKWi1UaVhTdXhFTzlQbF9kbVRwelNVSkFFMDNBd1NQcjdpejRfTmNBSDZvUWVGTnVSOHV2X1dDYVhrTGpxeVpKY1BtMVVONUVSZjNPNjV6UVdMUGJmTm9VbkpGc1lfRlVRdHN5R1JIaGdvRnNxUFJQeFVWWWdCeURTdENkMUxWZjZuM0hBX1JLOFJPbw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 11 Aug 2026 14:00:19 GMT
- [What Just Happened To AI Stocks? (Micron, AMD & Nvidia Explained) Francesco Gabbani (qUyiUiHK0V) - Mshale](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5DVGktWnNERl9sc0xBaEJLVl9iSGtLUmFEa3FOdm9xV09aN3UwYmVZLVpSVHh6ZWNuNS05dE5EWl81SGV1Vk41bWVTdGtvOUZ4OVBCUm1tYzc2Zw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 10 Aug 2026 18:35:11 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：台股指數站上45K 半導體封測與高填息策略躍居雙主軸 - 經濟日報；大摩：市場關注 AI 資本支出回報率等六大議題 看好半導體四台廠 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3711 日月光投控 | 新聞直接提及 | 0.00 | +5.71% | +7.52% | 629.00 | 680.00 | -7.50% | 不適用 | 13.92 | 45.51 | 73.78B TWD / 43.15% | 2026-08-01 |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 97.71 | 114.68 | -14.80% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +1.27% | +3.23% | 2,395.00 | 2,425.00 | -1.24% | 不適用 | 74.39 | 32.20 | 467.58B TWD / 44.69% | 2026-08-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +1.23% | +3.80% | 123.00 | 164.50 | -25.23% | 不適用 | 6.68 | 18.50 | 23.84B TWD / 18.98% | 2026-08-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +8.70% | +8.98% | 217.50 | 223.96 | -2.88% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 474.32 | 516.10 | -8.10% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 868.52 | 971.00 | -10.55% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | +0.99% | -10.97% | 1,271.05 | 2,335.00 | -45.57% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3711：新聞直接提及「封測」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
- INTC：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 CPU, server CPU, x86, foundry；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 0 篇新聞出現相關標籤。

### 主要來源

- [台股指數站上45K 半導體封測與高填息策略躍居雙主軸 - 經濟日報](https://news.google.com/rss/articles/CBMieEFVX3lxTFAzT2ZYXzd3bW11SFlRUW92YkRiNllYcW44Ykg4ZjJDMlpKUVJEejhTQ1prdVlfSmpORS1uQjFCZ3lSSVpzeHJhelI3TUdfdTZJOWR0Q096OWx5aTF0OFRYSDdMT1pLcU85dXFfZ012alhzTFctSHJ2NtIBX0FVX3lxTE0teG9jSWtqTDlFZlFvc042OEtzRFVKTHZXUGI2enhQNzljalJYckd4MDhJcjFUamZaa0plOG01RmNxZl94OHRDZFA4VnR4RWVfS3J5Y0RpSWMzSVA5aXNB?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 10 Aug 2026 09:00:00 GMT
- [大摩：市場關注 AI 資本支出回報率等六大議題 看好半導體四台廠 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1PSEtrMTJCRGZOaVloTF9zOGEwX184VTFpWldFNHdmaVJTMHlNbFdWOE1UTTZnQkEwb0Z1Q3BKVmIza0Y2cTU5TG5GTHRPRnBZdFBpRXFMbkV2UdIBX0FVX3lxTE5iV2RNWHNQYXNiNUZ6UzNZQWQ4X0NmUlQxbl9kOWZiZFc4TlZuMGI1OGhuMkhFODBITGJsX1laUDA2ajZDR2JqYU53TjV1SU5MSWg0N1dic1h0dFZqU0Yw?oc=5) - Google News source discovery | 經濟日報 money Mon, 10 Aug 2026 09:00:00 GMT

## 先進封裝與 CoPoS

摘要：先進封裝與 CoPoS 相關新聞集中在：台積電 5.5 倍光罩良率最高 99%、2029 年拚 14 倍！何軍揭先進封裝新挑戰 - technews.tw

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | 0.00 | +1.27% | +3.23% | 2,395.00 | 2,425.00 | -1.24% | 不適用 | 74.39 | 32.20 | 467.58B TWD / 44.69% | 2026-08-01 |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | +5.71% | +7.52% | 629.00 | 680.00 | -7.50% | 不適用 | 13.92 | 45.51 | 73.78B TWD / 43.15% | 2026-08-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 同時符合主題標籤：advanced packaging, CoWoS, CoPoS, FOPLP。
- 3711：產業/供應鏈推估：公司標籤符合「先進封裝與 CoPoS」關鍵字 advanced packaging, CoPoS, FOPLP, panel-level packaging；其中 0 篇新聞出現相關標籤。

### 主要來源

- [台積電 5.5 倍光罩良率最高 99%、2029 年拚 14 倍！何軍揭先進封裝新挑戰 - technews.tw](https://news.google.com/rss/articles/CBMiaEFVX3lxTE5SdG1xVWJjZnVDeEphb25iV1gxSU5XLUtGbWFuU3B3aUUtb1JNSjdWVUR2T0Z6VVRxREpsOUx1V2ViTUJTZFNLWG1rSmtnN0ZhRXMwQTFQVnNkUWIybTBzekNhNFpwNENx?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 11 Aug 2026 06:32:40 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：個股動態報導內容-D5619C4B-0185-4420-AD8C-D96FDB8063B2 - MoneyDJ；《台股盤後》開低走高、收漲191點，站上45K - MoneyDJ；個股動態報導內容-6F16F42B-D52A-4855-BD37-FC9349D23F78 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-D5619C4B-0185-4420-AD8C-D96FDB8063B2 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxOYWttemtRejQ4Qnp4QzhEMkRsdDE4YmFuZnNJX1FIZXhvSVQ4QlVSMDMwRnd4SVUyNm9BV1hKSkRFazY4bWxHcE1fVExzOXFYbTlrMmxicFZBWG1SVGhObVYxWGhkd2cxdjJTZFIyWkJjRXF0bk9USXA2WGV2al9hYXpnT0ZLV1hRUFlWWEQ3dy1PWGE2?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 11 Aug 2026 19:30:49 GMT
- [《台股盤後》開低走高、收漲191點，站上45K - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPSjFseGppVy1FRVI5RDBXdFpOSkFISGNtbzVUS29XcFRmS3dQTUgtc25Va3ktRXRjeXREMzdhU0cwRVpLX0xQUE44QWNVYkNkcVdaLXA2Q0hpWGxvb2JoV2E4ZVkxZ3k0ZlEzX01ZX1plR3NlTHNhbER1UlB1OWJoY3cwcVBRcEtualNpMGZ4T3RyQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 11 Aug 2026 07:40:00 GMT
- [個股動態報導內容-6F16F42B-D52A-4855-BD37-FC9349D23F78 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxPZGNWNGVOdnRDU0ppeVBHOTZ5a0M0dTgtbk82SktsWm5xX0ZBbjFCTi13YW4yYnpHM3FuZDdFZWgxelplcFBGanBSSXhIREhJajFmYS1md0Ixa2FlRjRGN3RicDI3Ukd4bFBJdVN3ekJ4Y3BvTDdyX2xxSGRjb19wcnVVZGNwSkdQYUFLRUI4X0w0bnNp?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 11 Aug 2026 14:37:44 GMT

## 新興題材：D96FDB8063B2

摘要：新興題材：D96FDB8063B2 相關新聞集中在：個股動態報導內容-D5619C4B-0185-4420-AD8C-D96FDB8063B2 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-D5619C4B-0185-4420-AD8C-D96FDB8063B2 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxOYWttemtRejQ4Qnp4QzhEMkRsdDE4YmFuZnNJX1FIZXhvSVQ4QlVSMDMwRnd4SVUyNm9BV1hKSkRFazY4bWxHcE1fVExzOXFYbTlrMmxicFZBWG1SVGhObVYxWGhkd2cxdjJTZFIyWkJjRXF0bk9USXA2WGV2al9hYXpnT0ZLV1hRUFlWWEQ3dy1PWGE2?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 11 Aug 2026 19:30:49 GMT

## 新興題材：加速半導體晶片

摘要：新興題材：加速半導體晶片 相關新聞集中在：Discovered Materials完成900萬美元種子輪融資，加速半導體晶片新材料的應用 - cna.com.tw

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [Discovered Materials完成900萬美元種子輪融資，加速半導體晶片新材料的應用 - cna.com.tw](https://news.google.com/rss/articles/CBMiVkFVX3lxTE9HbnpGbG55LTBaSWd4TW1yLXFDcnFWdDBkN0F1ZWRtOGFCaENCUTdITklXVE05Y1c5ZDJwNklTSlV6WDIwTVN4clR3VS03V1RpZTFTTGdB?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 11 Aug 2026 09:44:50 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
