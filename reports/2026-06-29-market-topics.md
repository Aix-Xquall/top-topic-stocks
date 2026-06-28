# 每日股市熱門話題分析 - 2026-06-29

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜正向｜熱度 3｜市場確認 89.41｜同向 1/1
2. **半導體與晶片供應鏈**｜負向｜熱度 7｜市場確認 67.50｜同向 4/5
3. **綜合市場情緒**｜正向｜熱度 25｜市場確認 0.00｜同向 0/1
4. **AI 伺服器與資料中心**｜正向｜熱度 16｜市場確認 0.00｜同向 0/6
5. **新興題材：MoneyDJ**｜中性｜熱度 8｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.49（樣本 13）
- 5日相關係數：-0.25（樣本 13）
- 同向比例：5/13

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 89.41 | 1/1 | 0 | +6.47% | -4.30% |
| 半導體與晶片供應鏈 | 67.50 | 4/5 | 1 | +3.83% | -5.68% |
| 綜合市場情緒 | 0.00 | 0/1 | 0 | -0.50% | -5.66% |
| AI 伺服器與資料中心 | 0.00 | 0/6 | 6 | -7.68% | -2.49% |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：F4365DBB4477 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：B818D25D | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：FinanceAsia | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-06-16 | 0.39 | 0.50 | +76.92% | 13 |
| 2026-06-17 | 0.17 | 0.47 | +62.50% | 8 |
| 2026-06-18 | -0.41 | -0.41 | +42.86% | 7 |
| 2026-06-19 | 0.06 | -0.04 | +57.14% | 7 |
| 2026-06-20 | 0.29 | 0.21 | +63.16% | 19 |
| 2026-06-21 | -0.01 | 0.32 | +55.56% | 18 |
| 2026-06-22 | -0.87 | -0.87 | +100.00% | 3 |
| 2026-06-23 | 0.38 | 0.01 | +62.50% | 8 |
| 2026-06-24 | -0.38 | -0.11 | +25.00% | 12 |
| 2026-06-25 | 0.10 | -0.21 | +20.00% | 5 |
| 2026-06-26 | 0.08 | 0.04 | +25.00% | 16 |
| 2026-06-27 | 0.12 | 0.29 | +57.89% | 19 |
| 2026-06-28 | 0.16 | 0.55 | +85.71% | 14 |
| 2026-06-29 | 0.49 | -0.25 | +38.46% | 13 |

## 歷史回測摘要

- 回測日期：2026-06-29
- 近5日 3日相關：0.50
- 近5日 5日相關：0.27
- 同向比例：+66.67%
- 權重狀態：未調整

- 方向準確度：+66.67%
- 信心排序準確度：0.50
- 診斷：正相關

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

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：MU, INTC, SNDK: Chip Stocks Rally After-Hours On AMD’s Blowout Report - Stocktwits；AMD Just Acquired MEXT to Crack the Memory Optimization Problem. Should Micron and Sandisk Investors Be Nervous? - The Motley Fool；Are SanDisk and Micron too expensive? Here's how you can invest in the artificial intelligence (AI) memory supercycle for just $50. - MSN

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.65 | N/A | N/A | 1,132.33 | 1,132.33 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.65 | +6.47% | -4.30% | 2,090.71 | 2,335.00 | -10.46% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.56 | N/A | N/A | 521.58 | 521.58 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.48 | N/A | N/A | 128.32 | 128.32 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -3.53% | +8.66% | 192.53 | 211.14 | -8.81% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron」，共 3 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK、SanDisk」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [MU, INTC, SNDK: Chip Stocks Rally After-Hours On AMD’s Blowout Report - Stocktwits](https://news.google.com/rss/articles/CBMiygFBVV95cUxPeVlYaXJjQjNtTkNRQUxQTHhaLUFMbE80Uy1MeDBpV0FPdkg2SHRLdkdfVUpXM1NrNWhZSVZQQ01sa0o4T1hKdzF1clBFRlRWUmMwWGxQTDNVVFBpOVhObUc2MXpBeXBOZ0p3R0w5NGRNOHB4X0ZIXzhlT0NMbmhzc1RtdmJRTWhlRUhKSHpyVnpaU0VGMlJyU2tDcmdkTG1hWVJJbmtTVDREbzFfWDB4bjhuTGswN3lmdkdHQzY1dzFOVU41VGlBNlZn?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 28 Jun 2026 01:42:13 GMT
- [AMD Just Acquired MEXT to Crack the Memory Optimization Problem. Should Micron and Sandisk Investors Be Nervous? - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxQSERvb1NPVTh6cmt3UW5NU0taUEpSODd3SEhlR3d5ejVDeDI5aFNYdTVEV04td2MzaUZzSlU0NndxOTVlSFZ3UW81MnRwWW4xdlliUXpKMUg1LTVQSG1ucFNUNUR1SlFYajFTNFh3Z29KemRWXzBIdDdWU3hEcTg5ZzN1RXM2V3hxNV90VDlic1p2UTRPbk5TYQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 28 Jun 2026 19:00:00 GMT
- [Are SanDisk and Micron too expensive? Here's how you can invest in the artificial intelligence (AI) memory supercycle for just $50. - MSN](https://news.google.com/rss/articles/CBMi4gNBVV95cUxOZEl1UHc1OXNnNVVucWtGNWQydEdzS3FyV2R6cGFxR25vM09wbzlKLWxRcGJ0NEVuQWhjWXlCUWx2TW5jTXJJWEJGUnpwZTh4MG1DelROM003NWEtMDJjd2NkOUhsYTJNelpqSXlGbGZBaUFJZTZFR0Z5TXhGMzlXeG1PeTBRdGRHVVMyYmQ4MUR6djFtT3RUYWFpQy1tOU15ZzdGYlh0MHpKWHRvNWNGdkJvZXZDOWx0UENEMkZ1dFBPQkFnTTBCeEI4cjZuV0t5bFYwSE1EWlJaXzhqX3lBb2RlcEh0Y04xOGM4LVBJN2oxcGgzcS0zcmVmd2wyNWNDR1RkbldsSEJndGZkdzJKV09BUWo5dm1VWW5IWDNfY21Mb0RjXzc2ZUYzcnVxN3VvUFUwYjhhU0daZm9vOXpPQlZhS2RZaXk5WklPNTdQNzI3SWh0QzlyaU9iV2NIejdoQU9TMXozazkyMDBvZi0zc1lDQkFaaWFEaGM4Njl0YUhXRHV5S2dvTjk2STJNQlJCcDZuVVBCenNwbmRfb2E5a2RHQUJPRTg5emwzR3FmMGZERHFrYnE0d0pIUnctTS1IdEFwc1RtaVJ5UlNJbFZxbEQwem5Hb2NhVkdMd00xSnRnUQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 27 Jun 2026 15:11:57 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：3 Beaten-Down AI Chip Stocks to Consider Buying in the Sell-Off - The Motley Fool；台灣半導體攬才吸睛馬來西亞掀赴台就業熱潮| 產經 - 中央社 CNA；台股功率半導體恐遭波及！安森美狂瀉23％ 專家點名這5檔下周小心- 證券 - 工商時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | -0.08 | N/A | N/A | 128.32 | 128.32 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.05 | -6.02% | -2.90% | 2,340.00 | 2,355.00 | -0.64% | 同向 | 74.39 | N/A | 416.98B TWD / 30.09% | 2026-06-01 |
| 2303 聯電 | 產業/供應鏈推估 | -0.05 | -3.53% | +12.71% | 164.00 | 164.00 | 0.00% | 同向 | 4.00 | N/A | 22.94B TWD / 17.78% | 2026-06-01 |
| NVDA 輝達 | 產業/供應鏈推估 | -0.04 | -3.53% | +8.66% | 192.53 | 211.14 | -8.81% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | -0.04 | N/A | N/A | 521.58 | 521.58 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | -0.04 | N/A | N/A | 1,132.33 | 1,132.33 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | -0.02 | +6.47% | -4.30% | 2,090.71 | 2,335.00 | -10.46% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -12.56% | +14.23% | 365.02 | 446.77 | -18.30% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 CPU, server CPU, x86, foundry；其中 1 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 1 篇新聞出現相關標籤。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 1 篇新聞出現相關標籤。

### 主要來源

- [3 Beaten-Down AI Chip Stocks to Consider Buying in the Sell-Off - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxPbVlaNEY4MGx5TTFDV3RCQ0l1VENTQldlT1NZdGF1dC14WkJHZ3J2WlVWbkdCRTJQeldDNG91TWItS0RyQUF5bzBNSTJqWDltUmctMkF3NTNvcnFHaDdLTXA3WFdKd2UtWENBLTZyWl9CX0RWNHVScUZqUGRGNTEzcWZMTFBmU004ZjVKZVgxSDFkbFJKMUZBLQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 27 Jun 2026 04:30:00 GMT
- [台灣半導體攬才吸睛馬來西亞掀赴台就業熱潮| 產經 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTFBrSG4zeTJSQ2lETjVQYjRfeWRDWEZFazcwWnB6R0YwZ3dzWjNzenVZbkczX3VwVVhSbDVTOFdZemtzY05WU19reHRJbmw5NGFNQzFlbnFIc3hEME93Mmc?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 27 Jun 2026 09:15:00 GMT
- [台股功率半導體恐遭波及！安森美狂瀉23％ 專家點名這5檔下周小心- 證券 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5aRDdzUFdaU2pYOGVNTUhDb1cwUjFoUjV3UTdYV0xtLVlPOXJmZm54eTU5dXdDTmg4ekc0SGlrR0IxQkN2LW02NkN4RjlEWlZNRmRsM0pzeXB1LTB6RURJ?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 28 Jun 2026 03:37:00 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股短線交易熱 當沖比攀高 - 經濟日報；台股上週大跌1893點　法人：系統性回調非基本面反轉 - 經濟日報；大盤大跌千點 台股正二商品布局時點到 掌握後市上漲契機 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.48 | N/A | N/A | 128.32 | 128.32 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| TSLA 特斯拉 | 新聞直接提及 | +0.36 | -0.50% | -5.66% | 379.71 | 456.56 | -16.83% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- TSLA：新聞直接提及「Tesla」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [台股短線交易熱 當沖比攀高 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxQWnNndmt4bnhLb09lNzd2Y21XcTJSRG5rSVl2aHI3aXZnamZ2dmZWNDhmR1h3VXRWVFVQSkNWeTB6RURnaXZIaXZhd3BRV1k2bHlneEpwVk5VbjVaWE5wNkMzSkdPZ05YZU9XVVlKWTdadi1UaExXV0FxdkMtX3lKOdIBX0FVX3lxTE1OMUZMUm5ZN3hpWmgydmdUSUZPTEUydVYtdW5HZmFwek5XR2JxMUVLaDdpWE9HS0Y1TFNpNWE0UkRSakFMVTdFQ2VzendIUVBPcDlwZDJTR1FOQmZpRkFZ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 28 Jun 2026 19:24:12 GMT
- [台股上週大跌1893點　法人：系統性回調非基本面反轉 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5GdFY0M3NNLUw1aF91a2F2T000NUxsbFV2NE9MTGl6V1BSOWJ2ajV3QVhiQ0JWTXBldklRWVA5ajNIaDY5ZkdxRmRoSzJ3Y29hYzZOTV9NVEdsd9IBX0FVX3lxTFBYdEZ2SE9WckVNbTdmSGNSQjZDRDVwV0F5cmltM2JTRjFjVE1kTEVnZXViWUxkU19tUDVtZjhQbTB1M3RBd1hIRUpKUDFHU2RpSzBuMmNUVUM5TTRYQnVz?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 28 Jun 2026 02:12:30 GMT
- [大盤大跌千點 台股正二商品布局時點到 掌握後市上漲契機 - 經濟日報](https://news.google.com/rss/articles/CBMid0FVX3lxTE14cFd5ejVoX2hEaFoxSWtoVnFwVVlySzI0bS1MaktyQ3hQUkF2WXBXN3BOLTNFNTNGdTU1ZWtzaTl4SjFNZW5lM1FhSnJseHhHc285RTZQZzlMVHhMX0s1X0VyVGd0bnpYYVZ5NnM5dk41SF91cFJr0gFfQVVfeXFMTWYzNGYySkpKRWRWUEVPd1U3T08yUjhXYnVMWE5DRHpWcU05R3FZNGE3RDU4RGdPQUJMdnBGSi10VWVjUm9sQmU3bE0yaXdCbkk2UmlERmItbTdyblNVazA?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 28 Jun 2026 18:08:30 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：台股連跌引發回檔疑慮 法人：AI 基本面未變 技術性修正非趨勢反轉 | 市場焦點 | 證券 - 經濟日報；3 Beaten-Down AI Chip Stocks to Consider Buying in the Sell-Off - The Motley Fool；Arm Holdings Is Up 111% Over the Past Year. Here’s Whether the AI Rally Still Has Room to Run - TIKR.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | +0.08 | N/A | N/A | 128.32 | 128.32 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.03 | -3.53% | +8.66% | 192.53 | 211.14 | -8.81% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.06 | N/A | N/A | 521.58 | 521.58 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.03 | -6.02% | -2.90% | 2,340.00 | 2,355.00 | -0.64% | 背離 | 74.39 | N/A | 416.98B TWD / 30.09% | 2026-06-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.02 | -5.03% | -26.39% | 372.97 | 506.69 | -26.39% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -12.56% | +14.23% | 365.02 | 446.77 | -18.30% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.02 | -4.53% | +3.10% | 632.00 | 632.00 | 0.00% | 背離 | 10.86 | N/A | 63.03B TWD / 28.57% | 2026-06-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.02 | -14.44% | -11.62% | 3,880.00 | 4,310.00 | -9.98% | 背離 | 62.91 | N/A | 47.43B TWD / 4.99% | 2026-06-01 |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [台股連跌引發回檔疑慮 法人：AI 基本面未變 技術性修正非趨勢反轉 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMifEFVX3lxTE9MS3lFZEhXbEFNeTR5RGxUZ3ZHOUhMTU5vdENqbjNSUXFOb1k2U1hzcklEd0ZoSGhidUxhNmg3T3lxb1B6LTJzc2t5SDhHenJFN2tYUDNFbHVSWTBuY2FiQ2tRVzBYdUJrVXhFcFV3ZXNYSl9PRGl2WVV4a1A?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 28 Jun 2026 16:25:25 GMT
- [3 Beaten-Down AI Chip Stocks to Consider Buying in the Sell-Off - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxPbVlaNEY4MGx5TTFDV3RCQ0l1VENTQldlT1NZdGF1dC14WkJHZ3J2WlVWbkdCRTJQeldDNG91TWItS0RyQUF5bzBNSTJqWDltUmctMkF3NTNvcnFHaDdLTXA3WFdKd2UtWENBLTZyWl9CX0RWNHVScUZqUGRGNTEzcWZMTFBmU004ZjVKZVgxSDFkbFJKMUZBLQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 27 Jun 2026 04:30:00 GMT
- [Arm Holdings Is Up 111% Over the Past Year. Here’s Whether the AI Rally Still Has Room to Run - TIKR.com](https://news.google.com/rss/articles/CBMitwFBVV95cUxPb0x1OWU3N1JlcWQtdWFTeFI3Q0JEOHVFaHdIRVB5X2I2RmhYNjFJSnlIc0xxQzFZSG5jZDIxMkcyNzg2TGlmQWFBWC1QWS1sejdDZk92a3VqRkhLSElyYWdCNHVIZ3Q3NDcwTEFHdWc1YUNWeU0ya2hMZmMyRGtiMjFPVWE5cEdSQ21BRnFGYTBqRnlHZzBiWHViVzljNXc5VGdwaTdHb0ZFblZxTjAyZklHb0RkQnc?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 27 Jun 2026 11:14:40 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：個股動態報導內容-3725BCA4-95D1-44D7-938C-7D7D0401B94D - MoneyDJ；個股動態報導內容-1DA5EB61-3E0E-47A1-8CCB-F4365DBB4477 - MoneyDJ；個股動態報導內容-3318E5ED-6998-4398-9E8C-728FFC909AB4 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-3725BCA4-95D1-44D7-938C-7D7D0401B94D - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxNT3U1UElUTDFHeGowN0JiczQxTm9NUlpyWlJQV1I2VmVzcDlUc0RRd3IzV3R0QkhlUW4xWVN6TG1CdlhZRnZUWFY3NXhfdWxUcHhzNG1wSDJlZ1RzeXZOQTY3N3lsZG9FV2xYMXZnNGd6RWJYa3lJbFZhZHI1SmRlRU03RXZKTHJ3ck5zNk1NSXB3M1Nl?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 28 Jun 2026 20:26:28 GMT
- [個股動態報導內容-1DA5EB61-3E0E-47A1-8CCB-F4365DBB4477 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxQWnIyODNyUVJUME1ZUzFzTkVzbTgwdTJmSVJxQXVHeEpUcWxfbndGOUZQZmdaVEtTbGk5RWl2aWVtUk1weUtlNXJRNUFxZ3l4NExPc1VhVjB6dmVyekJpWWRpNW5STms0QWhDZU9PT0FUQ3VaR29rN0s3X2RvQ0c3ZUE0MVhBNDV3LWRzYWkxWFRZVGNC?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 28 Jun 2026 20:26:28 GMT
- [個股動態報導內容-3318E5ED-6998-4398-9E8C-728FFC909AB4 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxOUl9pZ0RaSS1oS3JYNnNsT0UzWFdNS3ZDZVJlb3k4U2FNNVo0UEtHVVUyeFhlNlRqN3ZIOGt3ejJBd2M4RC1vMGIxV2Q4VjhRTGlBd3Y5Ny10c1FXS2pENWtCbjBGTWdiN3hDYnJHUWZyRnRMTUtPUEdfdkx0QjJrQm1ISWRhblM4OUZkT0doRS1FYlVj?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 28 Jun 2026 18:40:00 GMT

## 新興題材：F4365DBB4477

摘要：新興題材：F4365DBB4477 相關新聞集中在：個股動態報導內容-1DA5EB61-3E0E-47A1-8CCB-F4365DBB4477 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-1DA5EB61-3E0E-47A1-8CCB-F4365DBB4477 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxQWnIyODNyUVJUME1ZUzFzTkVzbTgwdTJmSVJxQXVHeEpUcWxfbndGOUZQZmdaVEtTbGk5RWl2aWVtUk1weUtlNXJRNUFxZ3l4NExPc1VhVjB6dmVyekJpWWRpNW5STms0QWhDZU9PT0FUQ3VaR29rN0s3X2RvQ0c3ZUE0MVhBNDV3LWRzYWkxWFRZVGNC?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 28 Jun 2026 20:26:28 GMT

## 新興題材：B818D25D

摘要：新興題材：B818D25D 相關新聞集中在：個股動態報導內容-B818D25D-571B-4D59-AB3E-B2FE4370C586 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-B818D25D-571B-4D59-AB3E-B2FE4370C586 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxOMnlCUklHNXZSMVNjOWtpbUFFb2lwZ1lyV2MxSmZXRWctVDFhanlteEdYMVZmY29IN0EzLWtUOV92OU1NWTVja0xGWFA2azdESl9IS1VOaEJuVFNkZGRrckkxMGZPUmZFZEh2WUNaYUdfZV9na0ZpSUJkX3BWU21KUzBkd29qYTNYQ2p1bG1KVkZVdWVn?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 28 Jun 2026 01:14:04 GMT

## 新興題材：FinanceAsia

摘要：新興題材：FinanceAsia 相關新聞集中在：永豐金證券榮獲 FinanceAsia 2026大獎 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [永豐金證券榮獲 FinanceAsia 2026大獎 - 經濟日報](https://news.google.com/rss/articles/CBMieEFVX3lxTFBsWEZLNFpxSkZxZy1ZOThNTmVZRHR3VW9XTnFrTnNHSVNrbVB2ZFRVcS1MQ3lPbW5rYWFlenpjM0xkZzhLRHFudzZUdFdzbkVMSm9pdW12QTEtQlNjbnlZSmt5SkExZzdlay1nMXlCMWg4TkV1Nkt4R9IBX0FVX3lxTE92LThnRUxNWG0xdTBvWG42MndkbllzNkxJdW9aM3VaUUthTVF6eFY3cThScE1JX3JZRU9tWTRFcXJlNHlvTi1KSWlneWRLckMwU0dRLThheXlnMmR0NmFn?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 28 Jun 2026 06:51:32 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
- TWSE PER/PBR 抓取失敗：Expecting value: line 1 column 1 (char 0)
