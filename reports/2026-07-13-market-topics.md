# 每日股市熱門話題分析 - 2026-07-13

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜正向｜熱度 5｜市場確認 62.51｜同向 1/2
2. **先進封裝與 CoPoS**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
3. **半導體與晶片供應鏈**｜正向｜熱度 9｜市場確認 14.01｜同向 1/5
4. **AI 伺服器與資料中心**｜正向｜熱度 8｜市場確認 0.00｜同向 0/6
5. **綜合市場情緒**｜負向｜熱度 24｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.39（樣本 13）
- 5日相關係數：-0.09（樣本 13）
- 同向比例：2/13

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 62.51 | 1/2 | 0 | +9.17% | +15.38% |
| 先進封裝與 CoPoS | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | 14.01 | 1/5 | 3 | +0.00% | +10.44% |
| AI 伺服器與資料中心 | 0.00 | 0/6 | 4 | -3.25% | +1.27% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：6月營收 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：押寶權王法說 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-06-30 | 0.44 | -0.27 | +62.50% | 8 |
| 2026-07-01 | -0.08 | 0.25 | +30.77% | 13 |
| 2026-07-02 | 0.30 | 0.03 | +55.56% | 9 |
| 2026-07-03 | 0.21 | 0.08 | +55.56% | 18 |
| 2026-07-04 | -0.22 | -0.36 | +22.22% | 18 |
| 2026-07-05 | -0.00 | 0.24 | +40.00% | 10 |
| 2026-07-06 | N/A | N/A | 0.00% | 2 |
| 2026-07-07 | N/A | N/A | 0.00% | 1 |
| 2026-07-08 | -0.05 | -0.05 | +71.43% | 14 |
| 2026-07-09 | -0.11 | -0.36 | +64.29% | 14 |
| 2026-07-10 | 0.55 | 0.05 | +77.78% | 9 |
| 2026-07-11 | 0.13 | -0.08 | +50.00% | 12 |
| 2026-07-12 | 0.27 | 0.13 | +16.67% | 12 |
| 2026-07-13 | 0.39 | -0.09 | +15.38% | 13 |

## 歷史回測摘要

- 回測日期：2026-07-13
- 近5日 3日相關：0.45
- 近5日 5日相關：0.32
- 同向比例：0.00%
- 權重狀態：未調整

- 方向準確度：0.00%
- 信心排序準確度：0.45
- 診斷：正相關

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

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Micron, Sandisk, Marvell stocks jump, leading chip sector gains - AOL.com；Micron, SanDisk, and Western Digital Sink 7% as Samsung Earnings Spark a Memory Selloff - AOL.com；SanDisk Rebounds 5%, Western Digital Gains 5%, Micron Climbs 3% as UBS, Citi, BofA Turn Bullish on Memory - AOL.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.50 | N/A | N/A | 979.30 | 979.30 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.50 | +18.43% | +9.79% | 1,915.92 | 2,335.00 | -17.95% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.02 | -0.09% | +20.96% | 210.96 | 211.14 | -0.09% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、memory」，共 4 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：shortage。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：shortage。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 1 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Micron, Sandisk, Marvell stocks jump, leading chip sector gains - AOL.com](https://news.google.com/rss/articles/CBMigwFBVV95cUxOWjlRdFlDUnBSUGgzZ2M5SmI3NERuSXZhWl9mRXFsVTJFMkVaTk1qMDcyT3ZpM0syWVpUTEpjYjBLMUNxWlNjb1RWRWhRYXZfRDNDSXhxUzZPcEFCTUFBajVxeDN2U1NWanp4VG9UQkpscW1nOFhWWU55U0xZWnNzdkp6UQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 12 Jul 2026 18:41:05 GMT
- [Micron, SanDisk, and Western Digital Sink 7% as Samsung Earnings Spark a Memory Selloff - AOL.com](https://news.google.com/rss/articles/CBMihgFBVV95cUxQOVpySXZranEwNXhHOHlIb3RpWV9BM0V4SjVSeTdXSEpNVU5WUEpFYTdFeEFXN29jNG5CQnYzc1lHUWpIQjRnYjF0SUhFb3JKLVpBZ0Q1Y1RQUnVDeDVQaHJiS2tsVHFNN3M1a1lqYUhBREtLV0VyWTZsWHIwb2FpMHZUcFF2dw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 11 Jul 2026 01:39:57 GMT
- [SanDisk Rebounds 5%, Western Digital Gains 5%, Micron Climbs 3% as UBS, Citi, BofA Turn Bullish on Memory - AOL.com](https://news.google.com/rss/articles/CBMigwFBVV95cUxPMzRlcDNNdG1uZ3dYS0h5czFPUFJ2Tmw1cnI2c2FiczhtR0kxSUUxSEFNWWFMNVVTcHpIS1NOM2dNamNOZ1hvU2hRSTBJMXk5LWtyMlJyN1ZnMWtIcWxRTjBXVUJpMHlnbVdIdmhNOGxVa0lRT3hRSmtWUW9fZE5xdDlXYw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 11 Jul 2026 05:03:15 GMT

## 先進封裝與 CoPoS

摘要：先進封裝與 CoPoS 相關新聞集中在：嘉義科學園區二期基地正式動土，台積電先進封裝擴產進入新里程 - TechNews 科技新報；TGV 玻璃載板技術如何助攻晶呈佈局先進封裝市場？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | 0.00 | -1.83% | -2.03% | 2,415.00 | 2,415.00 | 0.00% | 不適用 | 74.39 | N/A | 416.98B TWD / 30.09% | 2026-06-01 |
| 3037 欣興 | 新聞直接提及 | 0.00 | -4.58% | -10.62% | 875.00 | 1,070.00 | -18.22% | 不適用 | 7.06 | N/A | 14.90B TWD / 36.31% | 2026-07-01 |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | -0.29% | -6.88% | 677.00 | 680.00 | -0.44% | 不適用 | 10.86 | N/A | 65.78B TWD / 32.86% | 2026-07-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 同時符合主題標籤：advanced packaging, CoWoS, CoPoS, FOPLP。
- 3037：新聞直接提及「載板」，共 1 篇新聞命中。
- 3711：產業/供應鏈推估：公司標籤符合「先進封裝與 CoPoS」關鍵字 advanced packaging, CoPoS, FOPLP, panel-level packaging；其中 0 篇新聞出現相關標籤。

### 主要來源

- [嘉義科學園區二期基地正式動土，台積電先進封裝擴產進入新里程 - TechNews 科技新報](https://news.google.com/rss/articles/CBMi0AFBVV95cUxPYXZ1SUJfWVZpY04waWg0aTZKZGpKLW44cmhCaUpXRVNGZW1XRDZyMms5OTZ5eDZtVVRzNWFEaHFKci1nVl9VNkdXYmM0MTJvSEhxS05BcC05dmFZcmRJYWFEWTU2X1N1c2J4RThhSlVSQTU4cDFiYzBWWUtKMnFFc1F5bElRcEh1U2tVRkVoTHZRd0lQYU9HeElzeGV2ZTZSTzlBTWhONDJET0xnT0RydW55MlVTa1g5aExVZzE1QjVvdk94Y1MyWkpNMGQwVVFZ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 12 Jul 2026 07:11:51 GMT
- [TGV 玻璃載板技術如何助攻晶呈佈局先進封裝市場？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMifEFVX3lxTE5ZNENEVU1nN2JfdGlkNzJ0ZFFsVlcwRml0Rm96ajRZa1c4RTdQbF9aZ1N3LTdsQ090NzhhRjY5eXhteFJGYTZTLTNOc1VPa25FUGlKVnRDQTlVUnRXSk01LVVkdk5RNERYb0t0Z05WY1BrMnh1MTdWS2ozQkg?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 12 Jul 2026 16:42:33 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel (INTC) Raises Server Chip Prices As AI Demand Pushes Supply Limits - Yahoo Finance；川普屢點名台灣美學者：台美是半導體夥伴非競爭者| 政治 - 中央社 CNA；SK海力士登美股會長：不排除追加美國半導體投資| 產經 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.52 | N/A | N/A | 109.84 | 114.68 | -4.22% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.03 | -1.83% | -2.03% | 2,415.00 | 2,415.00 | 0.00% | 背離 | 74.39 | N/A | 416.98B TWD / 30.09% | 2026-06-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.03 | -6.02% | -5.74% | 156.00 | 164.50 | -5.17% | 背離 | 4.00 | N/A | 23.12B TWD / 22.85% | 2026-07-01 |
| NVDA 輝達 | 產業/供應鏈推估 | +0.03 | -0.09% | +20.96% | 210.96 | 211.14 | -0.09% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.04 | N/A | N/A | 557.89 | 557.89 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | +0.04 | N/A | N/A | 979.30 | 979.30 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.04 | +18.43% | +9.79% | 1,915.92 | 2,335.00 | -17.95% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -10.48% | +29.23% | 399.97 | 446.77 | -10.48% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 1 篇新聞出現相關標籤。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 1 篇新聞出現相關標籤。

### 主要來源

- [Intel (INTC) Raises Server Chip Prices As AI Demand Pushes Supply Limits - Yahoo Finance](https://news.google.com/rss/articles/CBMimAFBVV95cUxNWUhrbV9RZWlYZy14V1hNbk53bjNYZ3lNYk8wWnVJUmNHZUdCUnoybFlLSzZNMTVXTEFKeDlReGJqYm54QUY1VWQxSlZLeFRpdUs5dEJfZVRka2E1SllZcXRZVDY0aEtBMllmR1BDY1Jaa1g3UWQxeC0yRGh0R0xRWDZQcUtBdi04TXZEN3BaV0Q3dUZiQm8xRg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 12 Jul 2026 04:15:00 GMT
- [川普屢點名台灣美學者：台美是半導體夥伴非競爭者| 政治 - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTE0tVlZLZUw0OUx5U0tURGwzV1UtbDdmaXNwczF1WUI0SkQ4aDgtaGg2MHU3T2Vucno4SW5leVdQWWVqdHRIeDd0aGZ6MVZLc0lNNFJGYnBnYnVYemR5eWZJ?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 12 Jul 2026 00:39:00 GMT
- [SK海力士登美股會長：不排除追加美國半導體投資| 產經 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE5yVnhVdEt2Y2hXVTlJYWk1SGJUSzMwR3hIVUo5aDFBTGVBcW04SFZJbFUyS25GTXVycFMySkJESk5xS3ZtYmtWSE5mUEVZZXhRLUhaN3ZVcmw2ZFBuTXc?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 11 Jul 2026 04:05:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel (INTC) Raises Server Chip Prices As AI Demand Pushes Supply Limits - Yahoo Finance；Intel (INTC) Just Lost The Data Center Revenue Lead To AMD - simplywall.st；台積電如何與 AI 醫療聚落產生綜效？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.59 | N/A | N/A | 109.84 | 114.68 | -4.22% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.54 | N/A | N/A | 557.89 | 557.89 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | +0.27 | -1.83% | -2.03% | 2,415.00 | 2,415.00 | 0.00% | 背離 | 74.39 | N/A | 416.98B TWD / 30.09% | 2026-06-01 |
| NVDA 輝達 | 產業/供應鏈推估 | +0.04 | -0.09% | +20.96% | 210.96 | 211.14 | -0.09% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 產業/供應鏈推估 | +0.02 | -1.95% | -24.00% | 385.10 | 506.69 | -24.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -10.48% | +29.23% | 399.97 | 446.77 | -10.48% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.03 | -0.29% | -6.88% | 677.00 | 680.00 | -0.44% | 未明確 | 10.86 | N/A | 65.78B TWD / 32.86% | 2026-07-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.02 | -4.85% | -9.67% | 3,925.00 | 4,310.00 | -8.93% | 背離 | 62.91 | N/A | 58.01B TWD / 2.80% | 2026-07-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 2 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 同時符合主題標籤：AI, advanced packaging, CoWoS, AI server。

### 主要來源

- [Intel (INTC) Raises Server Chip Prices As AI Demand Pushes Supply Limits - Yahoo Finance](https://news.google.com/rss/articles/CBMimAFBVV95cUxNWUhrbV9RZWlYZy14V1hNbk53bjNYZ3lNYk8wWnVJUmNHZUdCUnoybFlLSzZNMTVXTEFKeDlReGJqYm54QUY1VWQxSlZLeFRpdUs5dEJfZVRka2E1SllZcXRZVDY0aEtBMllmR1BDY1Jaa1g3UWQxeC0yRGh0R0xRWDZQcUtBdi04TXZEN3BaV0Q3dUZiQm8xRg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 12 Jul 2026 04:15:00 GMT
- [Intel (INTC) Just Lost The Data Center Revenue Lead To AMD - simplywall.st](https://news.google.com/rss/articles/CBMixAFBVV95cUxNbl9FN2hnMmVEdFY2MEJOR0ozMndLYmRTc1FsQlo1MmYtQXlVUEZEckFaZEx2RnQ0QTJDMFFXUnpENV90SnZZYlJ4STc3RWFqek5oaXlXYUtMRWYtMG5RNmpUeDBNbjk4THJVbGI5amRaNi1ZQmRDQkZieEhlS1dkaUhKSVlmTm5ZdUlLbVBEWWFBZnhybjVzUDl3YzRQc2xZMTYxajE0UTBlYnlJZEVaM2hBa0VOZldmZHBfQnRIZzlTTS050gHKAUFVX3lxTE5hY1dsRWR0SWRxTUJTcGFncWlNQnJZV0xGdjRXYlpCSV9MMGpueFZ2dmh5RnJqT2l4bUs4QlZxUXJnS3p6SlV4amQzbklESWZOUHBJZmFEV3B1N2ZlNmMwS0pHRDlfejhsanhJbDVaNlpYUlhxN3Brb2RGWkM2NllNcXlJVjVlWFc1REd0NkI4RENGclpoQ0hRSkF3SDdZajFTZXk4U003VE9zalNIQWNJNzc5X3h3VW1LTlZlcmIzZUtZdGtUcjgtdmc?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 11 Jul 2026 17:43:48 GMT
- [台積電如何與 AI 醫療聚落產生綜效？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiUEFVX3lxTE1MMzU1NWhkaUd2RndYM0E0Q0d3RTBRLWFjbElvbER1ZlB6UlZnMWpZR0E0bklhN0k2WWxuQm40UElpc1NyYkdWTXhSbWk5VVZw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 12 Jul 2026 21:56:24 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：統一-士林 對 麗豐-KY(4137)個股 單一券商歷史明細 - justdata.moneydj.com；聯邦-台南 對 合富-KY(4745)個股 單一券商歷史明細 - justdata.moneydj.com；玉山-雙和 對 嘉澤(3533)個股 單一券商歷史明細 - justdata.moneydj.com

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [統一-士林 對 麗豐-KY(4137)個股 單一券商歷史明細 - justdata.moneydj.com](https://news.google.com/rss/articles/CBMikgFBVV95cUxPSENDUTkzdG8wSW10UDRHX1hCZk8xakxqcFFGTVlFU0Q0REJDTlZoUEtZUk1EWUpGMDVMV0tBS2otYnZhc2lqZFZJcHkwaV9hVDNSXy1jMDdOblRzc1l1MDl6UGJ5RjVZZnFtZG9TXzdjTjJzVnFqaFREN0N3dFpqX2hlb3J4ajVVWTQ5OEpCam54dw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 11 Jul 2026 21:14:42 GMT
- [聯邦-台南 對 合富-KY(4745)個股 單一券商歷史明細 - justdata.moneydj.com](https://news.google.com/rss/articles/CBMiggFBVV95cUxQREUwWi02eURHUldqU0kzZlBaRG80bE5hOTE1VnEwZ211eUxCZ2Nja3JodnQ2RnlSS2tKZXVXSDhsd0RaaHdYZ0ZQcWo3emVMMWVfZV94S3pHTDB3Uk1vRWY0aTFTQjRFVmQ3V3M4SU9ubmp3cWRmTkJ1OTN2Tlk5cHZ3?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 11 Jul 2026 22:30:43 GMT
- [玉山-雙和 對 嘉澤(3533)個股 單一券商歷史明細 - justdata.moneydj.com](https://news.google.com/rss/articles/CBMiggFBVV95cUxQYmRIWC00ci1ub2ZUVjJHOVlISF9YVjE3eU9XRjY0TDlEN1l2VTdTdnJyOVAwWVdUTC1NemJ2MFNCUGgtWUlEVjU0NEJGVkNjX0N5aGFaSG5aYWhwcFJwQ1dvMmtrSWVBNC1NSXQ1WVJXc2NFdWRHZ2hHN3pXYWpxVl9n?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 11 Jul 2026 19:43:01 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：產業評析-MANGOS科技新帝國－Meta、谷歌挺過三世代...芒果股誕生！ - MoneyDJ；恩德 115年6月營收2.75億、年增22.55% - MoneyDJ；法人專欄分析內容-台股 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [產業評析-MANGOS科技新帝國－Meta、谷歌挺過三世代...芒果股誕生！ - MoneyDJ](https://news.google.com/rss/articles/CBMilgFBVV95cUxQVFpZMnQzZ3AtZG9GYmdkeUdab1FOVjIyOFZHWUdFYU9wMVRXSkxYNTkzcUFjYXd5eXVtcHlQRlZobDd3aFN1M2h0WF9EdkwxVGxaeU5KcG5UTi00M3Q1ZDVzNFA4STZYTG1QcGh1LWUwWVR1OGo4LWFnTVIxS1lRMnNGWlpkdWxEVVk3SGMyZDdiOTVXbmc?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 12 Jul 2026 16:03:01 GMT
- [恩德 115年6月營收2.75億、年增22.55% - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPdThGOWFWaFo4TmhEYVdvZmJzeDU2VmdHN2tNNmJ4cFQtQ3NZNUVMbWxLb3dla3I3aVNDeUpZTGNnQm9TZWNhREZaUWNNRThBVGlWZENaR3BpbUtvU2ZrQ3dDVFZReHpfYUhpclN6MWRRdHZTc3J1RGd4VHMxT0JKVkpXa1VzSllhM2szQ2FQamR2QQ?oc=5) - Google News source discovery | MoneyDJ Sun, 12 Jul 2026 13:09:00 GMT
- [法人專欄分析內容-台股 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxNRW9LbXV5UlNaZTFJcVZlRmQ5VmlicjBhMEZKQUM2Zlg4RHdKblBTdXFaNDRtN3huamZrOXk0NWt5VE9pLTJxWkpXQzNzUGxGRHdIYmN4MVk0cVRSanVxdUVNQVkyT05FbEhoWDlfcUNwREZFUWJfaVhHeVJ6MS1QaUZLdlphSC1jbVVXSWZFVGI?oc=5) - Google News source discovery | MoneyDJ Sun, 12 Jul 2026 16:03:01 GMT

## 新興題材：6月營收

摘要：新興題材：6月營收 相關新聞集中在：台股跌千點照樣飛！這「AI顯卡廠」6月營收暴增544% 股價衝漲停、週線勁揚22% - Yahoo股市；6月營收飆增375%創新高！「板卡廠」AI PC、AI伺服器助攻 法人看旺下半年表現 - Yahoo股市

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股跌千點照樣飛！這「AI顯卡廠」6月營收暴增544% 股價衝漲停、週線勁揚22% - Yahoo股市](https://news.google.com/rss/articles/CBMi8AJBVV95cUxQd0lKQlU0b3lSTWRIVUx5akI1OFIwREpwSjU2TndUa20tOUhEbUg1Q2VBT1M2a0FIb2czZUZPMHdDenBJNzFPQmxFQzY4TUd4a2dqem9ScnBHN29ZeHMtbHlxRTM1SXN1V1Z2WHpwcndrWkJ5N1VoZkpNSlE5MC1nY3E5NXBhMzB3aVAxS1M1WkZSdjlUSTBvSDB2WGt2aWc2UExMLWxCU2R6eFJTdnJRdUo4MzhLWHZCbFh5UlFTdDg5T1ByOXF2UlVGeVhhRW80SE9lNG92Tkw1dldEWjJ2WXlFMWZralI2WE5LS25SUnZZbXZybVUzby0zLWkzUGRFT0pBQ2prSHNrN28tQjVHUFZueWg5LUtFOXZGRFJHNmFWZU9CWk5laHpMWW1zbTl4QW5ldzRLQlBpQWJYaVNmODJrR3E5MjJHOC1BdlZMRmFRWEt6RG1vbWZNak5na3FiZF9SczhtUW9nR1dhVThEbw?oc=5) - Google News source discovery | Yahoo 奇摩股市 Sun, 12 Jul 2026 15:30:00 GMT
- [6月營收飆增375%創新高！「板卡廠」AI PC、AI伺服器助攻 法人看旺下半年表現 - Yahoo股市](https://news.google.com/rss/articles/CBMi7wFBVV95cUxQaWYwY2oxbktXUDhwdXNmLURycEJrYWlER1dhczZuQmNwbnhucHBEVXF4Yi10QWw2OGlVd3ItdFhqMGhkRkVqb2Q3ODdKRTBmdUtZSEJOY0laSkIweGN6NGttZEtiOTJUcEtETzdSN1Q2U2l4TnVxUXZPR2l3NE5rNTJ2YWVSX3B6Um4wb2xXa1Jhb2thaVY3YzJBV2x4WHZ1TkhvRXgxTWJhd1lfSTI4UDZOWW5CZldDbmZsNFdMaU5jWjFsZGVYSkk1T3hZYlVBcUJFRUYyTGFORUNfZzBkVkduWFhDYUsxMm4waEt0Zw?oc=5) - Google News source discovery | Yahoo 奇摩股市 Sun, 12 Jul 2026 14:50:00 GMT

## 新興題材：押寶權王法說

摘要：新興題材：押寶權王法說 相關新聞集中在：台股補漲行情有影 押寶權王法說買盤可期 大盤短線挑戰48K | 市場焦點 | 證券 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股補漲行情有影 押寶權王法說買盤可期 大盤短線挑戰48K | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9LSmFyaWVJSVRCX25WdGFrNTlhSm1BWG5WX3ZTUFJCUURZdlYzUXE3czNsQU1fS28zNHdQcFN6R21sX1ctX1FUNHRjZjJrRURDY0kybEdfSjhmdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 11 Jul 2026 09:00:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
- TWSE PER/PBR 抓取失敗：<urlopen error [Errno 104] Connection reset by peer>
