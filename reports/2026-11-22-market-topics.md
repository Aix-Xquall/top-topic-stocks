# 每日股市熱門話題分析 - 2026-11-22

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **綜合市場情緒**｜負向｜熱度 39｜市場確認 100.00｜同向 1/1
2. **記憶體與 HBM 供應鏈**｜負向｜熱度 6｜市場確認 100.00｜同向 4/4
3. **半導體與晶片供應鏈**｜負向｜熱度 2｜市場確認 100.00｜同向 8/8
4. **新興題材：TrendForce**｜負向｜熱度 1｜市場確認 100.00｜同向 2/2
5. **關稅與供應鏈轉移**｜負向｜熱度 2｜市場確認 93.49｜同向 1/1

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.11（樣本 24）
- 5日相關係數：0.38（樣本 19）
- 同向比例：17/24

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 綜合市場情緒 | 100.00 | 1/1 | 0 | +12.76% | +18.69% |
| 記憶體與 HBM 供應鏈 | 100.00 | 4/4 | 0 | +25.30% | +28.13% |
| 半導體與晶片供應鏈 | 100.00 | 8/8 | 0 | +24.72% | +14.68% |
| 新興題材：TrendForce | 100.00 | 2/2 | 0 | +22.72% | +19.45% |
| 關稅與供應鏈轉移 | 93.49 | 1/1 | 0 | +7.83% | +14.89% |
| 散熱與液冷供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 0.00 | 1/8 | 7 | -19.56% | -13.07% |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價呈負相關；應檢查正負向詞庫，並降低新聞直接提及但股價背離的權重。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-11-09 | -0.56 | -0.62 | +60.00% | 10 |
| 2026-11-10 | -0.32 | 0.24 | +3.45% | 29 |
| 2026-11-11 | 0.34 | -0.26 | +46.67% | 15 |
| 2026-11-12 | -0.09 | 0.07 | +50.00% | 14 |
| 2026-11-13 | -0.56 | 0.42 | +54.17% | 24 |
| 2026-11-14 | -0.34 | 0.12 | +42.11% | 19 |
| 2026-11-15 | -0.02 | 0.62 | +50.00% | 20 |
| 2026-11-16 | -0.30 | -0.27 | +38.89% | 18 |
| 2026-11-17 | 0.44 | 0.39 | +80.00% | 15 |
| 2026-11-18 | 0.27 | -0.38 | +86.36% | 22 |
| 2026-11-19 | 0.20 | -0.23 | +69.57% | 23 |
| 2026-11-20 | -0.35 | -0.36 | +69.23% | 13 |
| 2026-11-21 | 0.04 | 0.04 | +65.00% | 20 |
| 2026-11-22 | -0.11 | 0.38 | +70.83% | 24 |

## 歷史回測摘要

- 回測日期：2026-11-22
- 近5日 3日相關：0.24
- 近5日 5日相關：0.35
- 同向比例：+90.91%
- 權重狀態：已調整

- 方向準確度：+90.91%
- 信心排序準確度：0.24
- 診斷：正相關

調整原因：近 5 日信心分數與後續報酬呈正相關，提高市場確認、歷史題材與直接提及權重。；關鍵詞×公司後續樣本有效 0 筆，未達 30 筆，不調整樣本權重

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

摘要：綜合市場情緒 相關新聞集中在：金管會出手禁平盤下放空！台股救市措施有用嗎？法人看反彈或回代工價 - 經濟日報；台股擂台／周冠軍「低調黑馬」陳奇琛 本周押聯發科、亞力 | 台股擂台 | 證券 - 經濟日報；台股跌跌不休 15檔法人、大戶抄底股 蓄力伺機突圍 | 市場焦點 | 證券 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2454 聯發科 | 新聞直接提及 | -0.48 | -12.76% | -18.69% | 3,350.00 | 4,920.00 | -31.91% | 同向 | 62.35 | 53.88 | 55.03B TWD / 5.77% | 2026-11-01 |

關聯理由（前 3）：
- 2454：新聞直接提及「聯發科」，共 1 篇新聞命中。

### 主要來源

- [金管會出手禁平盤下放空！台股救市措施有用嗎？法人看反彈或回代工價 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9FNmFlUDFZWnZBN2lIWjlRakU5d3pRcFdnaWMyOFZ6OVF2bDBKZmNxcHgxbFdSNVhTdFBUZnRrSU5UUWd5MEhWU1hKZ2xWMThLU3RXMWlZMElxQdIBX0FVX3lxTFBuc1p0VDUxM3FnYTFCaElMa2toeXNMbHdoZHhZX3hvVW5VSmRQS1ZwclpPLUlzV19zMjloZ0VlUmJTOUpGLThYWHVkb2ZJY19UbFB3azdCWm5zU3h6SVAw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 20 Nov 2026 20:00:00 GMT
- [台股擂台／周冠軍「低調黑馬」陳奇琛 本周押聯發科、亞力 | 台股擂台 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTE9QcUh4XzZFZThlYmJYN2lZMS1hX0s3bEFmZkdnaDhYUHRSc3VZeWk2Ui03Xy1yNlBSc3JzUFQzY2JramNfaHRXWDI1Vm9TNWVNSnZKQWJYdVpWMVpq?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 21 Nov 2026 16:04:44 GMT
- [台股跌跌不休 15檔法人、大戶抄底股 蓄力伺機突圍 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9HdWhFa2RWSFNINFVDTUFOUWRMTm9lN05sTFNzODVzUjVxY1hsck9lOVQwcDZkT0NJaGhuUk5PcUFxUVVVUndMcDZrRWVzazlaNVAzMUdzQXhDUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 21 Nov 2026 18:56:07 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Micron and SanDisk Stocks Crash 12%-14% as AI Selloff Spreads to Memory Chipmakers - Coinpaper；SanDisk Tumbles 8% as TrendForce Turns Bearish on 2027 NAND Prices; Micron Falls 5%, SK Hynix Slides 4% - 24/7 Wall St.；Why are Micron and SanDisk stocks plunging sharply in premarket today? - Invezz

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | -0.65 | -38.77% | N/A | 594.51 | 971.00 | -38.77% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.65 | -6.67% | -19.45% | 94.39 | 291.88 | -67.66% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | -0.58 | -45.03% | -37.47% | 125.53 | 228.38 | -45.03% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3017 奇鋐 | 新聞直接提及 | -0.48 | -10.73% | -27.47% | 2,205.00 | 3,435.00 | -35.81% | 同向 | 90.78 | 24.38 | 22.10B TWD / 34.35% | 2026-11-01 |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、美光」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：bearish, falls, 暴跌。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：bearish, falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「輝達」，共 2 篇新聞命中。 同時符合主題標籤：HBM。 方向判斷命中詞：暴跌。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Micron and SanDisk Stocks Crash 12%-14% as AI Selloff Spreads to Memory Chipmakers - Coinpaper](https://news.google.com/rss/articles/CBMirgFBVV95cUxNYV83ZXhRN1MzSExhN3JhZi1xNEpVUlplSHcwZS1rOW1BR19QU0U3SDIzUXltZDZaQ25ETElCaVdFSnJDckhqUU5FYmRPMTdtU1pJV214X2RBb29qNDlNanhtczBQamVQMGlIWFBkU2pUVWxrdm56OU1IRHdBdXBrdWt5V1pRaVpFMmc2Rl8wT2l2N1YxSHhLLXRGUUNaU0tOaXFPOWI3V0hHazFEaXc?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 20 Nov 2026 22:31:44 GMT
- [SanDisk Tumbles 8% as TrendForce Turns Bearish on 2027 NAND Prices; Micron Falls 5%, SK Hynix Slides 4% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi2gFBVV95cUxOVEl4eHlVV1BGWUVwei1KdWRVeUxhZzZhQmRMZWRXemQ4MDhmTTNJTi1abThheG5TQ0xUczJLUmlySnEtS21aX3poNXlRMDRRM0hGaFllOGNoNHFjWjI4MTRUX2ZUWHFQWkczbHNLV19TOUhkd3lBdkhaX3F5NWpORHN3S3JhcHo3T0JvWXpLR1J4ZWpYYXpjODJERVNIVHNaRlJsSUkybEg4U3lSS2dqZDlDdDdlbDdFVi1YVjdsRXRzRlBsUzVkdjZEeXRmemlNR1N5ZktHY0VwZw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 20 Nov 2026 14:09:00 GMT
- [Why are Micron and SanDisk stocks plunging sharply in premarket today? - Invezz](https://news.google.com/rss/articles/CBMilAFBVV95cUxOWTdhNzR2YVI4azd6bVR3bXdwWUxzLU1CeTBPNE9WeW9TVmhneVFuc1hydGhUQm9RQ2RQY0xWNVE0b3I3RFRzdVQ2aFJIOTRILXdrNFJScXIzRERKTnBQWVc4bDJ3QTRqV3M3M242aGZTb19pQkJyLTduNnNkMV9CQ2pkTXZNVElxWV9YY1JNRjZwSTVs?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 20 Nov 2026 12:45:29 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：A massive bearish trade just happened in the chip stocks - CNBC；做空AI交易開始獲利了結？ 《大賣空》貝瑞減半輝達、半導體ETF看跌期權 - 鉅亨網

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | -0.52 | -45.03% | -37.47% | 125.53 | 228.38 | -45.03% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 產業/供應鏈推估 | -0.07 | -55.28% | +26.43% | 51.28 | 114.68 | -55.28% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.04 | -7.83% | -14.89% | 2,000.00 | 2,480.00 | -19.35% | 同向 | 98.27 | 20.36 | 586.89B TWD / 59.71% | 2026-11-01 |
| 2303 聯電 | 產業/供應鏈推估 | -0.04 | -13.10% | -20.89% | 80.30 | 164.50 | -51.19% | 同向 | 6.80 | 11.86 | 25.20B TWD / 18.33% | 2026-11-01 |
| AMD 超微 | 產業/供應鏈推估 | -0.03 | -17.77% | N/A | 424.39 | 516.10 | -17.77% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | -0.03 | -38.77% | N/A | 594.51 | 971.00 | -38.77% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | -0.03 | -6.67% | -19.45% | 94.39 | 291.88 | -67.66% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.03 | -13.32% | -21.80% | 304.41 | 446.77 | -31.86% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：bearish。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 CPU, server CPU, x86, foundry；其中 1 篇新聞出現相關標籤。 方向判斷命中詞：bearish。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 1 篇新聞出現相關標籤。 方向判斷命中詞：bearish。

### 主要來源

- [A massive bearish trade just happened in the chip stocks - CNBC](https://news.google.com/rss/articles/CBMimAFBVV95cUxOVEN2YWJvcmsxZzRobzluR0xLTnBYczVRd1RmblBsU1dqM2hpaGZJY2Y0YWx4NDRMOVk5Rml5QTgtSGs3YmFtUFRsa0swYkp2dlk5b2N3LXlfdE9vX01tbzRxNy1VS3BSTkRYNl92bUpDaGlsUkw4TFhGMWtYNG1sOEhidjgzRXRvME82R2FicGxJeHB5aFYtVdIBngFBVV95cUxQZS1MQ3JIc1l0ay1LWl9DbUpiYy1BWXFLbXBkVGdlSVFsbV9Yd0sydFBVNUc1dUpYREtiSGp3cEwwckEwUWhJNEJPeG1QLTJJX0k5Nnd1ck9CV3kxWjFJYWJydnVFYUZkc19YOVc5bDBnSnp2THlEMlFFVG1kVTJFU29Cc1lxNzhtajNYSk5NTzEwZTJlZEtRZURfZGlxUQ?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 20 Nov 2026 19:32:59 GMT
- [做空AI交易開始獲利了結？ 《大賣空》貝瑞減半輝達、半導體ETF看跌期權 - 鉅亨網](https://news.google.com/rss/articles/CBMiT0FVX3lxTFBBcGZFUFFLNGNmcTdGREYxR3Qya3VDUmcxRjR0OUlIVEYwUThCR19NbzlUZFFfRVNWcDFLX1NHa3I1aXZLd1BKWTBLS1JmTEE?oc=5) - Google News source discovery | 鉅亨網 Sat, 21 Nov 2026 05:16:40 GMT

## 新興題材：TrendForce

摘要：新興題材：TrendForce 相關新聞集中在：SanDisk Tumbles 8% as TrendForce Turns Bearish on 2027 NAND Prices; Micron Falls 5%, SK Hynix Slides 4% - 24/7 Wall St.

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | -0.48 | -38.77% | N/A | 594.51 | 971.00 | -38.77% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.48 | -6.67% | -19.45% | 94.39 | 291.88 | -67.66% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron」，共 1 篇新聞命中。 方向判斷命中詞：bearish, falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 1 篇新聞命中。 方向判斷命中詞：bearish, falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。

### 主要來源

- [SanDisk Tumbles 8% as TrendForce Turns Bearish on 2027 NAND Prices; Micron Falls 5%, SK Hynix Slides 4% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi2gFBVV95cUxOVEl4eHlVV1BGWUVwei1KdWRVeUxhZzZhQmRMZWRXemQ4MDhmTTNJTi1abThheG5TQ0xUczJLUmlySnEtS21aX3poNXlRMDRRM0hGaFllOGNoNHFjWjI4MTRUX2ZUWHFQWkczbHNLV19TOUhkd3lBdkhaX3F5NWpORHN3S3JhcHo3T0JvWXpLR1J4ZWpYYXpjODJERVNIVHNaRlJsSUkybEg4U3lSS2dqZDlDdDdlbDdFVi1YVjdsRXRzRlBsUzVkdjZEeXRmemlNR1N5ZktHY0VwZw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 20 Nov 2026 14:09:00 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：愛豐通運布局捷克打造歐洲半導體供應鏈樞紐| 全球中央 - 中央社 CNA；台積電周線重挫15.8%！台股創36年最慘單周紀錄、美收緊AI晶片出口管制添壓 - 鉅亨網

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | -0.48 | -7.83% | -14.89% | 2,000.00 | 2,480.00 | -19.35% | 同向 | 98.27 | 20.36 | 586.89B TWD / 59.71% | 2026-11-01 |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +9.77% | +22.85% | 342.56 | 342.56 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | -4.11% | -12.86% | 210.00 | 289.00 | -27.34% | 不適用 | 16.57 | 12.70 | 1305.32B TWD / 45.73% | 2026-11-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 方向判斷命中詞：重挫。
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [愛豐通運布局捷克打造歐洲半導體供應鏈樞紐| 全球中央 - 中央社 CNA](https://news.google.com/rss/articles/CBMiZkFVX3lxTE90QzFlaFNOSmdSN2dOclQ4ZHFoa1JwRERnZ3drZC1ZRjc4eGhVYzNIY0VxdTdGbTdlSlVQVjZoeEFLWXQ0Mi03SkxZcmVGTzcxSURya0Ztb0hCcHE4TGIzNWxQS2NtUQ?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 21 Nov 2026 09:07:00 GMT
- [台積電周線重挫15.8%！台股創36年最慘單周紀錄、美收緊AI晶片出口管制添壓 - 鉅亨網](https://news.google.com/rss/articles/CBMiT0FVX3lxTE1CdGhhMmtpREk3aDJGQ25PVklyeDNyajBISkVQODBob3FnWFhXclVva0dackJaWE5xY2psdmpDOEJTNS1oN01mdXZySm1NOTA?oc=5) - Google News source discovery | 鉅亨網 Sat, 21 Nov 2026 10:12:26 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：散熱雙雄戰1》奇鋐、雙鴻同喊明年ASIC超車 輝達獨大局面生變？ - Yahoo新聞；【即時新聞】最新財報報喜！奇鋐Q3獲利創佳績，單季EPS高達29.32元 - CMoney投資網誌；台股一路殺、外資還在買誰？從記憶體、PCB到散熱15檔口袋名單出列- 日報 - 工商時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | -10.73% | -27.47% | 2,205.00 | 3,435.00 | -35.81% | 不適用 | 90.78 | 24.38 | 22.10B TWD / 34.35% | 2026-11-01 |
| NVDA 輝達 | 新聞直接提及 | 0.00 | -45.03% | -37.47% | 125.53 | 228.38 | -45.03% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐、散熱」，共 3 篇新聞命中。 同時符合主題標籤：thermal。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [散熱雙雄戰1》奇鋐、雙鴻同喊明年ASIC超車 輝達獨大局面生變？ - Yahoo新聞](https://news.google.com/rss/articles/CBMi8gJBVV95cUxNektmQm9BLVl0UTlIQ2M1bzNoM2dfX2pFNnVoa2xrOHFaZ0wtRVJoZDNjT0hMUi15b1d0NFVUb2Z0SXA0dE5OMFc5WnhiRk1mbkp6OXJFazJleVNRMWNWSzl0ZmpxUkM4VWdjV2FXZDVIRU9PZWZKZjR1V0V1R2hmT3QySjVua2U1R0w5S2NINVcyMG94dWdFN0lkV25NVXNWRjFHWlN3cGRDNEVpeDNpOXN2YjBPVkZCbzEzRXVoU285X01PeHo5V2Z5eW9paWVqRndfNkZVQUV5V1RIZTdUU1FTd29HRTBLVWY4SFpuSUFENVFVN1g5Sm0zTFY2R3l5NkpESFJYSURkQ2JmanktNUJDM21GcjBBRjZ2RlQ0VU9NSG1kNXFJOGVURkxMU3FuN01pWGFwamZNZGJVbzdtMHdPamtMZUVOTGlGTXhDc1BTVXl6SkVoZEVFZ0VyY3d5Z0h0bEVCUWc0ZGhidy1QRlFB?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 22 Nov 2026 00:14:39 GMT
- [【即時新聞】最新財報報喜！奇鋐Q3獲利創佳績，單季EPS高達29.32元 - CMoney投資網誌](https://news.google.com/rss/articles/CBMikAFBVV95cUxNQmt6Y3ZONkRBZDVUNy1jdTRtdE9tei0tT3BUYWViRXRhSFJ1QkYzVDRQMWhkNWRTdkg4SDFjVTRzQk1ucFF6U2VMOGtsbVdGcGlJajQ0NVhwQ2I5WjZUMFJnZXBvVEctc2NuT1R4Q2M0SDk5NHZUaU5NWUFHSENMUF9NMWM0RWtnbFhncTFCc3g?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 21 Nov 2026 15:38:13 GMT
- [台股一路殺、外資還在買誰？從記憶體、PCB到散熱15檔口袋名單出列- 日報 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1aZVQ4a1YtcGhuR0d1aHRtNmllRUY0UTgzOXp0Z1g0X1dzd1JfRlFBU1VjSW1RdXk3UUFhVElyQzExRnVKNmRSUWhxTDVjMWh1d21OVWlqbW9LamNsZVlr?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 20 Nov 2026 19:00:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：AMD Is Down 26% and Intel Is Down 42%. Which AI Stock Is Worth Buying on the Dip? - The Motley Fool；Nvidia vs. Intel: One AI Stock Is Worth the Drama, the Other Isn’t Worth the Wait, Says Investor - The Globe and Mail；Intel Stock And 2 AI Infrastructure Shares Backing Data Center Growth - Simply Wall St

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.33 | -55.28% | +26.43% | 51.28 | 114.68 | -55.28% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.31 | -45.03% | -37.47% | 125.53 | 228.38 | -45.03% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.30 | -17.77% | N/A | 424.39 | 516.10 | -17.77% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.03 | -7.83% | -14.89% | 2,000.00 | 2,480.00 | -19.35% | 背離 | 98.27 | 20.36 | 586.89B TWD / 59.71% | 2026-11-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | +7.61% | -1.52% | 484.52 | 507.29 | -4.49% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -13.32% | -21.80% | 304.41 | 446.77 | -31.86% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.02 | -12.12% | -23.58% | 457.00 | 703.00 | -34.99% | 背離 | 17.55 | 26.23 | 88.62B TWD / 47.13% | 2026-11-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.02 | -12.76% | -18.69% | 3,350.00 | 4,920.00 | -31.91% | 背離 | 62.35 | 53.88 | 55.03B TWD / 5.77% | 2026-11-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 3 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。 方向判斷命中詞：growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。 方向判斷命中詞：growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AMD Is Down 26% and Intel Is Down 42%. Which AI Stock Is Worth Buying on the Dip? - The Motley Fool](https://news.google.com/rss/articles/CBMiygFBVV95cUxNR1M0ek8zcGxGYUdSUDBrMEdkX2VkTk5PTkdONzNFRkVnc21TTnFRejZIWUhyNmxLc2tjSXFHTzlhNGw1MmJlREt6WUlTY3B6VlVrbU1lVWFubXVyUUNmYTdkSk16cUZUTzVib0tlSmowa1lyRXl2bkJFRWw1anZlQkRqUXk4ZS1sX1BTdWhLeHpfMndJQUZPMVl0SndSaHZSVGVuYkN3al9Lakk4RDNkQTJYUExhWm8tNWQtNk1iNmc3NWJ1VHlpR2h3?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 20 Nov 2026 20:30:02 GMT
- [Nvidia vs. Intel: One AI Stock Is Worth the Drama, the Other Isn’t Worth the Wait, Says Investor - The Globe and Mail](https://news.google.com/rss/articles/CBMiigJBVV95cUxNdUJxMFhWd2pVZTBYOUwwbXJNUjNETFBnNWFicVR0TzdrV0FKcV9LSXFDUWh0cjhUcFlKbVFEeVU4UmpUeDdxaGJQLU5LWnYxVXZ0QTVnLS1WUFhJTDlsS0JwWllrcjdlXzNVTUJ0VkVqbERYaEQ1dklOWDhOTV9iTDc3b2QxcFU0NkZ0N3BVWmRRUWE3eV8tWXIyaUdyd19PZUh4TmtROGtHOUtMQktlRW1scmdtYTNMU3RmOTJYOHNOTGFRV3F6ZU1rVVQxUXA2YVpEdnBMbDNneHZyUC1mbGRTUXlmeVQ4RG1NdUZpMzVsS1l0SjZnWjBnZ25VVnY2QmU2MDZpclF5UQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 20 Nov 2026 14:28:03 GMT
- [Intel Stock And 2 AI Infrastructure Shares Backing Data Center Growth - Simply Wall St](https://news.google.com/rss/articles/CBMiygFBVV95cUxQNTU2MldLVGdRQ3ExWW1WTzNwYTZyRnJYRzEwZHI0VmJTakJXNlZDa2NtSGw3eGNPUzgwNWlIejZhVVZRQTIwQm9UekQtQXFfVFFwQ0ZRTWlsa2NXUU5OMTFmODdXOUNYX3dhSHRjNXVjTVBTcm1VUldEcm52YjF6TVA2UXZYOTlPanNWZXNiVVZ2d2hUQ0diUUJjNVdhbXY1blZpMXhmMnUtVXhKRks3QzJsUkREV3REOThXemRrQlN3SnRUX2FGcHRR?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 20 Nov 2026 18:10:47 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：台股崩跌金管會出手！ 宣布週一「全面禁止平盤以下放空」等5措施 - MoneyDJ；《台股盤後》重摔2393點、險守36K；本週跌逾17% - MoneyDJ；主動式台股基金/ETF規模成長統一投信貢獻靚- 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股崩跌金管會出手！ 宣布週一「全面禁止平盤以下放空」等5措施 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPYWVJMGU3cXpjY3pWNEVhVGdRTWRyc2Y1Q3FuVzBjWWgyX082aGN2dFJBbXJmbGxqSUV3QlVmdFhiQW9wdmZMQnU3QjV6Z28tSkdLRWhFVFU2WEFBVW1FdXg4QmptYmp3Q3QzR0V3T2hGMFkzWDBBNlJ5aGQ0UmxKTEtmdmM3QTdaZGNpdmszWExpQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 21 Nov 2026 08:43:00 GMT
- [《台股盤後》重摔2393點、險守36K；本週跌逾17% - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxQZjBGai1Vd3NWUWo3OVpZSmVXRDRRYUx4amhCT1VwRDZuaVo4WmlFLURNM2JDRlduRllfa2JGcVNJem9Jemcza0lSUWJUem9SRmc4aVBPYWdXOWRsZGlya0NfQkhBalgyVkZZNjZfZFc0WWtCbWdXZ0I1WkRkR1lfa0Q1cldSRlB6bFJVTzBsMms?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 20 Nov 2026 08:15:00 GMT
- [主動式台股基金/ETF規模成長統一投信貢獻靚- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPYmVKX3VWQ1dkdDVLYy1WWFpGYTUzUGRHckpwaG1mQTdMWmE2eEk5TmVzd1d3WGdYNXF6dnl4T1RTN1Nzdm5jem5ZcW1xdGNhZVI0YWtKa0Fpd0tXTWlRR3FDeVBQNlA1Vi1rY09nRDNVaXJKdW82bVB3cDhLUElMYlpYZkpwNFczaWRXUDYyZEZ1QQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 20 Nov 2026 07:05:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
