# 每日股市熱門話題分析 - 2026-05-13

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **半導體與晶片供應鏈**｜正向｜熱度 7｜市場確認 86.00｜同向 4/5
2. **AI 伺服器與資料中心**｜正向｜熱度 12｜市場確認 56.98｜同向 3/6
3. **利率與成長股估值**｜正向｜熱度 2｜市場確認 N/A｜同向 0/0
4. **散熱與液冷供應鏈**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0
5. **記憶體與 HBM 供應鏈**｜負向｜熱度 6｜市場確認 0.00｜同向 0/1

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.08（樣本 12）
- 5日相關係數：0.07（樣本 12）
- 同向比例：7/12

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 半導體與晶片供應鏈 | 86.00 | 4/5 | 1 | +15.27% | +14.26% |
| AI 伺服器與資料中心 | 56.98 | 3/6 | 3 | +7.33% | +7.00% |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 記憶體與 HBM 供應鏈 | 0.00 | 0/1 | 1 | -8.36% | -3.25% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：激內需餐飲股受惠4月營收 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 相關性偏弱；應提高同向價格確認權重，降低泛 AI、泛半導體等寬標籤推估權重。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-05-08 | 0.03 | 0.48 | +76.92% | 13 |
| 2026-05-09 | 0.10 | 0.55 | +33.33% | 9 |
| 2026-05-10 | 0.45 | 0.55 | +75.00% | 8 |
| 2026-05-11 | -0.03 | 0.47 | +85.71% | 14 |
| 2026-05-12 | 0.00 | 0.42 | +78.57% | 14 |
| 2026-05-13 | -0.08 | 0.07 | +58.33% | 12 |

## 歷史回測摘要

- 回測日期：2026-05-13
- 近5日 3日相關：-0.22
- 近5日 5日相關：-0.28
- 同向比例：+58.82%
- 權重狀態：已調整

- 方向準確度：+58.82%
- 信心排序準確度：-0.22
- 診斷：方向與信心皆需修正

主要錯誤來源（高信心但報酬不佳）：

- AI 伺服器與資料中心｜2330 台積電｜信心 0.82｜3日 -2.38%｜背離
- 半導體與晶片供應鏈｜2330 台積電｜信心 0.72｜3日 -2.38%｜背離
- 關稅與供應鏈轉移｜2317 鴻海｜信心 0.7｜3日 0.00%｜未明確

調整原因：近 5 日方向與信心排序皆偏弱，降低方向詞與供應鏈推估權重，並加重背離扣分。；關鍵詞×公司後續樣本有效 0 筆，未達 30 筆，不調整樣本權重

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

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel Crashes 10%, AMD Slides 5% as Chip Trade Cools After Parabolic Run - 24/7 Wall St.；Chip Stocks Are Bleeding Today. The 2018 and 2022 Selloffs Tell You Exactly What Comes Next - 24/7 Wall St.；美國半導體類股續強法人看台股維持強勢震盪盤堅| 證券 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.78 | N/A | N/A | 120.61 | 129.44 | -6.82% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.72 | N/A | N/A | 448.29 | 458.79 | -2.29% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.05 | -2.38% | +0.22% | 2,255.00 | 2,255.00 | 0.00% | 背離 | 66.26 | 34.04 | 410.73B TWD / 17.50% | 2026-05-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.10 | +8.29% | +25.75% | 104.50 | 104.50 | 0.00% | 同向 | 4.00 | 26.26 | 22.66B TWD / 10.80% | 2026-05-01 |
| NVDA 輝達 | 產業/供應鏈推估 | +0.08 | +26.59% | +15.51% | 220.78 | 220.78 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | +0.08 | N/A | N/A | 766.58 | 795.33 | -3.61% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.08 | +8.36% | +3.25% | 1,452.02 | 1,562.34 | -7.06% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.08 | +35.47% | +26.56% | 419.30 | 428.43 | -2.13% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 3 篇新聞出現相關標籤。 方向判斷命中詞：rally。

### 主要來源

- [Intel Crashes 10%, AMD Slides 5% as Chip Trade Cools After Parabolic Run - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiswFBVV95cUxPOFZwSTZJanBTdWc4MXcxLVdvNDFka2JYaDBYeks5SFI1SUp3OFRWQW5ORktWdVdLX2NDcFFONTY5S3FVemlvZ2J4RmNtcTNFUF94NW50ekg1ekRiVGJ6SzVPNlJXQW9semV2b2dMcW1DTTFnT2JEUEJUNWo2THJnX0JJZEpZVVRFdFNvNEdyS09Zd0RWWDdQSVNrNllTbS1seHVEWGFVcVFnUjdmLWdhamY0MA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 12 May 2026 17:58:33 GMT
- [Chip Stocks Are Bleeding Today. The 2018 and 2022 Selloffs Tell You Exactly What Comes Next - 24/7 Wall St.](https://news.google.com/rss/articles/CBMizwFBVV95cUxQQm5sY2xQYkRLVTdsampudE5vcWs0OUpETTVmWWlZUGl3cnJSRWQxQkpkU29JSVNZRHhJR2JDYk14SDB2WFBLemYzWHE3SWxBMFFjb3E5cEwzSVJTcTBNUEo2RWJtWkdJTDJKREpMTTRKeG5JYWRtb05QbnZwWnFaV3ZIT0NRUi1NeWVWdUpYSmZPR1pqQXo4UndDS3BhQ2paaXFjUk5BQkdBeUxQcnVuU3VDOS0tbk1rWFlyM3BKelhXbTNlTTk3aXdHMEFlNFE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 12 May 2026 20:28:45 GMT
- [美國半導體類股續強法人看台股維持強勢震盪盤堅| 證券 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE01S0w4ZHRtRHBpcTgwaS1NZmpsNzlCakZDV0dFbmdHOHVPOEgwTmlrTWlQdXlzcE9yRHQ4UDNIdF9OSUFIRjVBaU53Y1F4UlFjcmNHMFFjdHh4ZWRZZUE?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 12 May 2026 00:22:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：AI 伺服器出貨鴻海領先廣達、緯創，外資看好 2026 年產業鏈獲利全面釋放 - TechNews 科技新報；南山人壽公開 500 人數轉基地！業務員 AI 智能對練、三大機器人即戰力 - TechNews 科技新報；歐盟法規趨嚴， AI 視覺硬體紅利終結？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2317 鴻海 | 新聞直接提及 | +0.33 | -1.38% | +4.38% | 250.00 | 257.50 | -2.91% | 背離 | 13.60 | 18.44 | 832.10B TWD / 29.74% | 2026-05-01 |
| INTC 英特爾 | 產業/供應鏈推估 | +0.15 | N/A | N/A | 120.61 | 129.44 | -6.82% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.12 | +26.59% | +15.51% | 220.78 | 220.78 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.11 | N/A | N/A | 448.29 | 458.79 | -2.29% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.06 | -2.38% | +0.22% | 2,255.00 | 2,255.00 | 0.00% | 背離 | 66.26 | 34.04 | 410.73B TWD / 17.50% | 2026-05-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | -17.12% | -11.42% | 407.77 | 506.69 | -19.52% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.08 | +35.47% | +26.56% | 419.30 | 428.43 | -2.13% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.08 | +2.78% | +6.73% | 555.00 | 555.00 | 0.00% | 同向 | 10.86 | 51.53 | 62.25B TWD / 19.22% | 2026-05-01 |

關聯理由（前 3）：
- 2317：新聞直接提及「鴻海」，共 1 篇新聞命中。 同時符合主題標籤：AI server, server。
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AI 伺服器出貨鴻海領先廣達、緯創，外資看好 2026 年產業鏈獲利全面釋放 - TechNews 科技新報](https://news.google.com/rss/articles/CBMimwFBVV95cUxNcl9nc2FFM1ZHRFZfRjRlVDUwZ3JtLWhxQzA0bWRWakNWUEI2bWRqMXI1UE1SNUJOLU1ia194bHU4bVhmRGdiUUo1eTRKakV3bjlMMUVHTTZ5dnpRakMxMXlxYUxFMHNJbW5EMW02WFR1b29HcTBZdEpmVXB4MTNhNm11MmZzazc0R3Z4SFVHdU5SWjBESGMxU2h4WQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 12 May 2026 07:11:09 GMT
- [南山人壽公開 500 人數轉基地！業務員 AI 智能對練、三大機器人即戰力 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiZEFVX3lxTE5xMjVNckd2eFR5bFBYT1BiaVBYQ1otbkpaOXRYTlNzVjd2V0hVbmpIR1FfSWtFRFpUMlBWYzNjNk1hcndsWjZiREFYVUFWMFQtQlVsakNmMjRreV9rWFpJQ3Fubkc?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 12 May 2026 21:00:05 GMT
- [歐盟法規趨嚴， AI 視覺硬體紅利終結？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMilwFBVV95cUxObnhFQTd0ZWlJdm9tcFcwZUppdHBOT1ZLV2RhT0p5T3lRbGczX1dKdHFBTmlLOVFOZmZpRlJHN3FaUmgyVVpGWHBEU0dSeWxRNXBDRzFBeFpEUEtCXzlGOHp0ZURIbDZ6X2R4cTNONS14Rjd1Rkh0THhnZF9abDlRM0M2R3FPRUlRUy11ejVReFR2MXhfaHhB?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 12 May 2026 20:24:12 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：Intel Stock Pulls Back as AI Foundry Rally Meets Valuation and CPI Pressure - TechStock²；Markets raise chances for a Fed rate hike following hot inflation report - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.62 | N/A | N/A | 120.61 | 129.44 | -6.82% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | -17.12% | -11.42% | 407.77 | 506.69 | -19.52% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 方向判斷命中詞：pressure, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Stock Pulls Back as AI Foundry Rally Meets Valuation and CPI Pressure - TechStock²](https://news.google.com/rss/articles/CBMinAFBVV95cUxNU0YxelJIN2QwUkJOSEV3T1RpZHZHWXFNVlBBM2FjVjZPZmtINS1VSG5kdWU0VGNwVHZaSktKSzhGMHNENEN2MkNwYjItbmkxV0lHdDJxUlBhYWlUTXRmc3NwTFROSDdtbTRZMHpKbDgydEtZZE9xTFUxQm1GY0R5bE1fcEdHdXJCSDFZajg3WGZBd1NCbmZtOHZxY00?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 12 May 2026 14:36:32 GMT
- [Markets raise chances for a Fed rate hike following hot inflation report - CNBC](https://news.google.com/rss/articles/CBMirgFBVV95cUxOWm9qcWF5ZE1VRDl4cFhRRWhIM2hGZHc2QkZfVlhoU25BWXo0a3ZRcURJN2RtZXg0aEpBUW9wWXFVSGhFOUNGLWY5QVp1YklNR1dXWGVldlc5MmF0QUVZdlgtX0d6YVFiNmRKX1hWdnBJd20tZGR3bXJ4NWw2bzU1eVJtdFJpWDc2VjZPU1Q4OHd0R1NLdXdyWVNyVUl1Y3JVMFktYmFCdEUxZDRFbmfSAbMBQVVfeXFMT3pyT3lRUF9PZE1lMUlPb3dJeHJrSmpsWjQ4d0l1dXVwOGthYTIwTXpOV1JtSm1YUjEyTVZsRzdXb2xKZThJckNIUnVBamJjSnJtR3U5aUZackRYR2JyTlFBTFlRdUFweTQ2dUhhVjdtUlUwaUNKV3pIbHdfdHRfOVlLUm1nTUtfVzRyZzE3cTg3b05hOWdIenBENXpxaXl2UE04MzAtQW1SdHpBdjRwUUhvQ28?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 12 May 2026 17:33:45 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：散熱股大跌結束了嗎？健策亮燈、奇鋐守五日線 - 聯合新聞網

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | +4.35% | -6.84% | 2,520.00 | 2,835.00 | -11.11% | 不適用 | 49.17 | 51.51 | 15.63B TWD / 71.62% | 2026-05-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐」，共 1 篇新聞命中。 同時符合主題標籤：thermal。

### 主要來源

- [散熱股大跌結束了嗎？健策亮燈、奇鋐守五日線 - 聯合新聞網](https://news.google.com/rss/articles/CBMiUEFVX3lxTFBmNHdXUTNiMHpvZ3RLcnNzNjFhQmNFaThOdDM5Z1RVYVItWjdVWE9wUEpGMWx1SEtSbnRyeWJaaWxoTnZKVlYxaE1HVGhxem5G0gFWQVVfeXFMUGJiUUxEYjhhYlBqWDgwcHhYeTBic1dWUGEwMUFMV3IzUVV2NHEzRnJJOVpSS3dqSjlFTTEya0VXdHFHMVFNLUthcUM4aXVGY01JZFdoM0E?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 11 May 2026 04:06:05 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Buy, Sell, or Hold: SanDisk at $1,562 and Micron at $746 - 24/7 Wall St.；Why Sandisk, Micron stock are plunging upto 9% on Tuesday - TradingView；SanDisk and Micron Fall 9%, Western Digital Drops 8% as Memory Supercycle Trade Hits Pause Button - AOL.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | -0.84 | N/A | N/A | 766.58 | 795.33 | -3.61% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.42 | +8.36% | +3.25% | 1,452.02 | 1,562.34 | -7.06% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +26.59% | +15.51% | 220.78 | 220.78 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、memory」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk、SNDK」，共 5 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Buy, Sell, or Hold: SanDisk at $1,562 and Micron at $746 - 24/7 Wall St.](https://news.google.com/rss/articles/CBMimgFBVV95cUxQaFd2ODJsSVZWQVpBb09wYmpRN2FJU1JwdUloSDl3ZW96SlBGZ2s4eDFxQ01MRWZ6bkZhdWZqakZhaHBJQ1RXbWE1MU11OFNzSEcyZ3ZEUVNwRVh3V0RjdGl3YVZBbDlLbjcxMzJqOUxNdTh4MGViYWxsdFJaZ2tCcnZaVHByaVFTdnNzdGlQdTNkay10eHZDSlVB?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 12 May 2026 15:45:13 GMT
- [Why Sandisk, Micron stock are plunging upto 9% on Tuesday - TradingView](https://news.google.com/rss/articles/CBMisgFBVV95cUxQMF9FcmVaeWFWWFlHVm54elA0d0tOcEs4T2M0aGppZXJnOHVBWGh5UjNSOFZQOHNMcmVpOHFad3RXeWZZNDBualVXRTdSUHJEQi1VZVlmbm1OdzdINWNKd3MySC1PcWIxSmZMQ0pUVHBSaU1EQjB5alFIQS1nUkJRMmJjUS1rTzZGeFBMTDBJSDNDRkxzcWxsUmVfcTFfNC1XbzAtU09pX3Z2dGtKbFk4Q1Fn?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 12 May 2026 17:35:02 GMT
- [SanDisk and Micron Fall 9%, Western Digital Drops 8% as Memory Supercycle Trade Hits Pause Button - AOL.com](https://news.google.com/rss/articles/CBMifkFVX3lxTFB4QXMza2xaUU92ZmlCMHJ0OVQ3Vklzb2E4SFFpYnR5aUNHTUF6VjFQaFlVaFl1YjVUM2xlajdfQWZRVURsUk41MGVEMksxYzE2TmgtY2FGc0dIRXVQNFR0OUQ2SVBGS1RraGFETjVnZU15cWYydWtfbHM3b2Z1Zw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 12 May 2026 16:33:48 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股大散戶時代 三個劇變 - 經濟日報；台股基金18強績效翻倍 施羅德台灣樂活中小、元大新主流報酬率超越120% - 經濟日報；台股驚驚漲！這12檔法人連買強勢股 有望短線領漲 | 市場焦點 | 證券 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股大散戶時代 三個劇變 - 經濟日報](https://news.google.com/rss/articles/CBMieEFVX3lxTFByeE1DUEVrZEdXaDZVVGZRek1RWkpJSHZVTGN1NzhXQnR6V3BaMUIzanYtTmtEUGxJdW0yV1BQRXlyTnFjN3NLT1QtRHF5WHpKRTFkM1p0MkJaUVd6aktwOVpWQU1uRm43Tnd3ZUhhUzZwTXlPRzJqU9IBX0FVX3lxTE9VbG52eGtNVWpYNWsyOUdfdGJOUzZNWFpvWGo4ZjJqY2JMUVBPdndMYmc3eE81SU15d1k2a1ZQN2RRSjloWlRqOEdmUDZWc29QSF9peWQ5Wl9ZbHNFeUY4?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 12 May 2026 18:10:47 GMT
- [台股基金18強績效翻倍 施羅德台灣樂活中小、元大新主流報酬率超越120% - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1yTGlISGpyV2J5UEU5RmVQNndVYWVyT0d6OTVMdnk2LVhjczdHNFNwQmhZNmRWLUpzWHpfQk9uRExjUDZjSzNobVBiU1V0a2ota1ZvWnNHeHExQdIBX0FVX3lxTE1uME5meXdpYWhsYUR4WGU2MFRPaG5XT2JEbGlteXNqMFYxc24yUGNnZUF5cXNfTkU4eUFtenJqUTh6YXNwNTR6aTdaWERCNnU4ZXdQYWpUVXZuajdwa0J3?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 12 May 2026 16:20:36 GMT
- [台股驚驚漲！這12檔法人連買強勢股 有望短線領漲 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMidkFVX3lxTFBMcHpSaE9DNHB6VXREZ0pxbkZKUk9qUWVaRGJ2VkJZSkllOHhtTXpudFNGdVh0cUdyX1JmQlRrMW40VWZRczVIRjRfYV9CZVhoSTVJanlTbU5qUm5RU2JnT2JIaUNTbG5EZkkxZU1IMmZ0QzJyMHc?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 12 May 2026 12:51:45 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》闖關42K再失利/收漲108點 5日線失而復得-新聞內容-基金 - MoneyDJ；台股焦點：博盛半導體(7712.TW) - MoneyDJ；台股基本面支撐強勁！野村投信看好AI主軸，多頭延續 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》闖關42K再失利/收漲108點 5日線失而復得-新聞內容-基金 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxOdmZrbHRGQ3JETFhiTERZa3I1eFdQMDVwLXg1dUc2ZXZtdlNjbDEtR1JLYzVVMURRSER4cnBSX1FTWW5VZ2dYT2xtUk53V3d6cWhVa0dGYjZRVTNuaDhSbWRKTTRqemtMODJ3RTQzNWxjaHZPV282WEp6Ul9uMXFjaDVpbjdtS3RlNXh6Z1N5S2Y?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 12 May 2026 08:37:00 GMT
- [台股焦點：博盛半導體(7712.TW) - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPX3VldU5NOHFxbDRuaGFtVkMyODlSU0ZuUllQMXNmRmRFb3pSeklnT3BuQTBNaHNNdUFZb0gxRTBrd0N4ekxQSVB1UVRLNmhPX3A3NEpxMVRfY3VVTVFoVVlkcTU3amE3YmhyT1ZaTnpPRzhudlNyUUpkZjQ4SjlaZUFXRjRLUFRhX1ZTZzRpS2xvZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 12 May 2026 01:17:00 GMT
- [台股基本面支撐強勁！野村投信看好AI主軸，多頭延續 - MoneyDJ](https://news.google.com/rss/articles/CBMilwFBVV95cUxPdnk4N29vemp5dUVORTJJSkxGbXZ3SEFjT0ZsQ2MzcEVmTllvNjlpRXdjc2RnVDlKZGlrQTR2MDlnRW9lWmFyZFRsdUJzNW9vUE5YLVIzZkpxY0pTdlg1LTF3d20xaGtITjBxMUVTdVVuNnVMSjZES2lOeVBmTzB1YW9DUU5TOGloOUh6ZzREOGFyZXlfbUtV?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 12 May 2026 01:49:00 GMT

## 新興題材：激內需餐飲股受惠4月營收

摘要：新興題材：激內需餐飲股受惠4月營收 相關新聞集中在：台股飆漲刺激內需餐飲股受惠4月營收攀高| 證券 - 中央社 CNA

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股飆漲刺激內需餐飲股受惠4月營收攀高| 證券 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE5yYlo5ZVFzOVhyU19yU3JuQ1Z4UmhoZzJBbFpRZkhoN2pIR1VhTjd0NVBNNS0yRURFdXNoeGxHb1lEaFMwRkpHLTh4NU1YMzl3U2wzSGRjT3RRMXh0V0E?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 12 May 2026 03:10:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
