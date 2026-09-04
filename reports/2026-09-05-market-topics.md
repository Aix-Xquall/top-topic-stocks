# 每日股市熱門話題分析 - 2026-09-05

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **綜合市場情緒**｜正向｜熱度 36｜市場確認 100.00｜同向 1/1
2. **記憶體與 HBM 供應鏈**｜正向｜熱度 6｜市場確認 47.24｜同向 3/5
3. **關稅與供應鏈轉移**｜中性｜熱度 5｜市場確認 N/A｜同向 0/0
4. **AI 伺服器與資料中心**｜中性｜熱度 14｜市場確認 47.04｜同向 5/8
5. **散熱與液冷供應鏈**｜中性｜熱度 5｜市場確認 45.92｜同向 1/2

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.13（樣本 24）
- 5日相關係數：0.34（樣本 15）
- 同向比例：13/24

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 綜合市場情緒 | 100.00 | 1/1 | 0 | +14.75% | +9.10% |
| 記憶體與 HBM 供應鏈 | 47.24 | 3/5 | 2 | +1.75% | +13.13% |
| 關稅與供應鏈轉移 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 47.04 | 5/8 | 3 | +1.10% | +0.69% |
| 散熱與液冷供應鏈 | 45.92 | 1/2 | 1 | +3.64% | +9.10% |
| 新興題材：OpenAI | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | 25.34 | 3/8 | 5 | -0.30% | +1.19% |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-08-22 | N/A | N/A | +50.00% | 2 |
| 2026-08-24 | -0.94 | -0.77 | +60.00% | 5 |
| 2026-08-25 | 0.01 | -0.58 | +35.71% | 14 |
| 2026-08-26 | 0.08 | 0.22 | +50.00% | 16 |
| 2026-08-27 | 0.38 | 0.11 | +54.55% | 11 |
| 2026-08-28 | 0.14 | 0.12 | +56.25% | 16 |
| 2026-08-29 | -0.10 | -0.01 | +40.00% | 10 |
| 2026-08-30 | -0.52 | -0.04 | +23.08% | 13 |
| 2026-08-31 | -0.41 | 0.29 | +40.00% | 10 |
| 2026-09-01 | N/A | N/A | +50.00% | 2 |
| 2026-09-02 | -0.29 | 0.24 | +75.00% | 12 |
| 2026-09-03 | 0.10 | -0.10 | +54.55% | 11 |
| 2026-09-04 | -0.08 | -0.08 | +28.57% | 7 |
| 2026-09-05 | 0.13 | 0.34 | +54.17% | 24 |

## 歷史回測摘要

- 回測日期：2026-09-05
- 近5日 3日相關：0.11
- 近5日 5日相關：0.12
- 同向比例：+75.00%
- 權重狀態：未調整

- 方向準確度：+75.00%
- 信心排序準確度：0.11
- 診斷：弱正相關

調整原因：近 5 日有效樣本 12 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：綜合市場情緒 相關新聞集中在：郭哲榮：台股二次崩盤 正式開始？ - 經濟日報；熱錢回補 台股蓄勢攻47K - 經濟日報；股海自由行／矽光子、輝達 VR 鏈 乘機押寶 | 證券達人 | 證券 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.42 | +14.75% | +9.10% | 230.36 | 230.36 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [郭哲榮：台股二次崩盤 正式開始？ - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5aNnhnNnQ2cUVsdGdTYUpYZmJHSXFUbTRjQlJVbzY5MElGZ2pmUnl2UlZyOHhVRnQ4aEVxZUFjYzlHVXYyZjhaQlY2QXNpZDFWYmNOYmxmRmhnQdIBX0FVX3lxTE9Ka3pRMHk4Uk13bVUyZDhQU3djZ25JOHI3SDVsRUdlRmhOdmxqQXpNSUcwZTlpMWg4YnptVHRDVXk1WDRhU3BQVmM3QzFDX05rUEttc05mYnRGRWZMaGpV?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 03 Sep 2026 10:24:23 GMT
- [熱錢回補 台股蓄勢攻47K - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxNNVRMal9nZS1BMDVWS1FEOERSdTdPUEdtS3B3dW9qdFVXSUFxdkVsc1M0Z3EzMml1TXNlaUFCUkU1a2ZzYzdtQXB1S01oZ2hsa1ZBU1NNc0tYbElsY0phZ2xLVGpLMWlaM2J4RGRqMkdsTEJmRGY2TmtOZm9YWGw4RtIBX0FVX3lxTFA0bXVrSVNRU3hjLW83dmROemFmLVZ2aHhuQWpfV01FbUIxeXB2QkJabDA3REFLcG5pTzdVc2hSRm16YWdGSXl4d1VFNjFmeE5zUkZhNDJxd0huUkhpb000?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 04 Sep 2026 16:50:13 GMT
- [股海自由行／矽光子、輝達 VR 鏈 乘機押寶 | 證券達人 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5kOFBCVE9QaVFDTGhtcTZaUHFEVUVleHNTR1VuU0p1ZS1HNDc1SW5tcjk1YUlwQkg2V2Uyd2xKSmNMNGRnM1pXcmlLZ0lXNjBlMzZXVFhlYXdJQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 04 Sep 2026 16:42:16 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Semiconductor Stocks EXPLODE! 🚨 Intel, Nvidia, AMD & Micron - Buy Now Or Bubble? Chicago Bulls (bldwmj4jtu) - Mshale；Micron (MU), SanDisk (SNDK), and SK Hynix (SKHY) Stocks Soar as Memory Trade Rebounds - TipRanks；Micron stock rises 2%, SanDisk gains 3%: why memory stocks are moving again - invezz.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.57 | +4.70% | N/A | 1,016.59 | 1,016.59 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.57 | +13.22% | +17.17% | 1,740.00 | 2,335.00 | -25.48% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.43 | +14.75% | +9.10% | 230.36 | 230.36 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.21 | -7.47% | N/A | 477.57 | 516.10 | -7.47% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.21 | -16.46% | N/A | 95.80 | 114.68 | -16.46% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、MU」，共 3 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK、SanDisk」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Semiconductor Stocks EXPLODE! 🚨 Intel, Nvidia, AMD & Micron - Buy Now Or Bubble? Chicago Bulls (bldwmj4jtu) - Mshale](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9Pb0N3cGRsYVBEUzNPTjhoSFpaczlFbENZanFuM1MxbGYtSTR5VHRsNENNeHk1TWkzYWFvNGphNVFPOXZZRVdsVjMwYkotWGJyNDZSZjRXQnVzSUk?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 04 Sep 2026 20:34:40 GMT
- [Micron (MU), SanDisk (SNDK), and SK Hynix (SKHY) Stocks Soar as Memory Trade Rebounds - TipRanks](https://news.google.com/rss/articles/CBMiqwFBVV95cUxQd2tJcjZnVl9mc1ZKMndCVjktNFpXRHlsQVVfa1dMX0JqS2lyS2JyU1JhR1ZRWVpBTTc1STB3aFZsb3lVaTVJX1h2NG9CVVpzZjd1QjN5dzlZZEo0WFZWeGhMQXQxMW9qWjc3bS1uOW5vVW5vT01mR1VraGxxald6MmlTNFpOVFZ4WXZjSks1bW80U0lfVzNNeGRTbktRaXIxNms5V1NIQ2tlMHc?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 04 Sep 2026 22:07:29 GMT
- [Micron stock rises 2%, SanDisk gains 3%: why memory stocks are moving again - invezz.com](https://news.google.com/rss/articles/CBMiqwFBVV95cUxOZG04VERhNC15SkJCTHlCdTk5aVBNNHVLYVltMWxaUUxhSnJtNUZTakRwLWs5a1A4a3laVEdJTHNPNXVVdmJsRjJIbllubk5aSmtrN21NQVgzbXg1b0hKOTlVZHBnZjB4dG1NTzFFT3hfcmlXMUhNSlpUWms0N3RNajhvUnczdjdmMDhlTHpQSGFwOXRXM1FOaWpxQXUwV1Y1dVlEdjNnSXp4cmc?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 04 Sep 2026 11:16:47 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：晶片關稅震撼彈！美國半導體新關稅確定了盧特尼克證實：台灣下周宣布加碼投資- 國際 - 工商時報；半導體設備也要資安認證！ 數發部、SEMI首推E187認證標章盼為供應鏈創標準- 產業 - 工商時報；西方如何精準封堵俄國軍工的半導體供應鏈？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3711 日月光投控 | 新聞直接提及 | 0.00 | -3.61% | -5.31% | 588.00 | 680.00 | -13.53% | 不適用 | 13.92 | 42.55 | 73.78B TWD / 43.15% | 2026-08-01 |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +2.53% | +14.75% | 319.97 | 328.21 | -2.51% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | 0.00% | +1.19% | 256.00 | 289.00 | -11.42% | 不適用 | 15.21 | 16.88 | 946.51B TWD / 54.19% | 2026-08-01 |

關聯理由（前 3）：
- 3711：新聞直接提及「封測」，共 1 篇新聞命中。
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [晶片關稅震撼彈！美國半導體新關稅確定了盧特尼克證實：台灣下周宣布加碼投資- 國際 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1Ra1hDejBlVGowYWRhcldyOGlsREdndWYxRkJtWFItY21oREN4c0o4b1RxSUFKbkJ2RHA1RHpRejJRUjV2bng5U2xwcEhLakU4NGtzSjY3a2pXamV2bDNV?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 03 Sep 2026 01:15:00 GMT
- [半導體設備也要資安認證！ 數發部、SEMI首推E187認證標章盼為供應鏈創標準- 產業 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1TSWxCeFdNNWlPWDBUMkg3V0lwX0lISmM3RDJnM0x1OFlwd045dmdpVC0tZ0hNa0FISmJwNU9RekNaVW9lUFdvZEt2VG44T25uMnVESGRaVTUtbmhhQU9F?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 04 Sep 2026 13:13:00 GMT
- [西方如何精準封堵俄國軍工的半導體供應鏈？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMi1AFBVV95cUxOZXNCZXdDZzAyWFhnVWlMS2xMZWdQVFlZcUJwWW9KZzFIbkdES1lrbHNzcS0tMHUxLWFVVjY2UFpzaXZCbzNxQ0ZUYXNIX0FmdkRRd2Z5bVh5MVpxU0N4d3V2YTMyeEFxOEpLNXJFeEo2SXd1clp5Q1ptRWxQZTQ4R1JzZHZPa09fTlJXczgyMGlzMVEyWFlYdTFhb2JXaDNENkN6MVBPeUU3OVExZmtpTDJ5MTVtdC1WaTRCUFBBMmthQV85ZDRFSjN1ZkljVUF3ZkhfRA?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 04 Sep 2026 15:23:36 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Nvidia Hugging Face Deal Puts Intel Stock And AI Infrastructure Plays In Focus - simplywall.st；設施受阻，是否削弱美國 AI 競爭力？ - TechNews 科技新報；AI 輔助基礎設施數位化對都市更新的價值？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | -0.28 | +14.75% | +9.10% | 230.36 | 230.36 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | -0.54 | -16.46% | N/A | 95.80 | 114.68 | -16.46% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | -0.06 | -7.47% | N/A | 477.57 | 516.10 | -7.47% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.06 | -1.23% | -0.41% | 2,410.00 | 2,425.00 | -0.62% | 同向 | 86.28 | 27.94 | 467.58B TWD / 44.69% | 2026-08-01 |
| MSFT 微軟 | 產業/供應鏈推估 | -0.02 | +10.99% | +1.56% | 499.70 | 510.12 | -2.04% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -8.06% | -19.89% | 357.89 | 446.77 | -19.89% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.04 | -3.61% | -5.31% | 588.00 | 680.00 | -13.53% | 同向 | 13.92 | 42.55 | 73.78B TWD / 43.15% | 2026-08-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.02 | +2.32% | +10.79% | 4,415.00 | 4,415.00 | 0.00% | 背離 | 60.69 | 72.91 | 48.47B TWD / 12.16% | 2026-08-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA、輝達」，共 2 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。 方向判斷命中詞：衝擊。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：衝擊。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：衝擊。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Nvidia Hugging Face Deal Puts Intel Stock And AI Infrastructure Plays In Focus - simplywall.st](https://news.google.com/rss/articles/CBMiygFBVV95cUxNT2ZBMHU4LWR3VnFJdEY5dEtxVVN2ZTZ0YkpLeWlJYUo2b01NQ1hPRmhmTjRwcDBDTThMaV9Ua2RFYk1YZmhLTVplNmtLWG9ocjN1TmtncWtrVldiRGlCWGxRM2ZVNWxvendCTTJMUTA0eHhHRGhkR3AtcTR1OTk1X1Y0cmQ1YnJybmR6NXh6U3hSMkdkSjdPYmJKcVhoMEdvUzNscWhOZkdmdXp6a25FRFVxbXRrZGhMMEJIcUZpenU4ZGYzSy15bzhR0gHPAUFVX3lxTE1qeTdlRzRaYk94anVOT2k3RFFRWW5xcTZxME04T2syT193X3RYSzFEYVFMWGhYUm42LUJGdUJsT2Etc291V2NlR202TURtTUQ1U0JZZG50OTZvVVVHSnNsSU13RjBaLTh6aFZLTzFTZFJfdkZjbV9tdE9fTUxUdmo3cnpMSnJCSldwbkZnUHdtZ3BSRHNocS1YUnV4Y1k4YURWd2dBTFRwOWstRWdQSnRwZC00NFg5eG84RURmQ053SWZlejkwOWl5M3lmUWFaMA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 03 Sep 2026 20:20:35 GMT
- [設施受阻，是否削弱美國 AI 競爭力？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMie0FVX3lxTE96WmFweG5BelAxVkswYlZEc2RyUkVDNnZyNTAtLVVEZ19sTVJib205YmwxRGl4VEFWT1RhRUJmNFlIR2FRaGI2c2F2SHRVZVVNa1lUSURDZ1p0bmROaGN6U2RPSUo2eGJyMGNieUlUUXpwZkM4cXB0V0pQaw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 04 Sep 2026 19:30:26 GMT
- [AI 輔助基礎設施數位化對都市更新的價值？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiakFVX3lxTE90Ylk2eGQ4dUxRcUJuVmQzcTZMRnRKZDdXNzZGMFBYWVJ0N0hRV2IxT3ZIRDJQMVliSnRzRC1ISm9nV1pscG1fQXdKbDNXOGk3WG9MZnB3d3VVYXFBVHI5dzQwNl9jYWdDUmc?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 04 Sep 2026 14:56:47 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：雙鴻(3324)大利多！Vera Rubin水冷板重返輝達推薦名單，2026年營收拚增70% - 鉅亨網；輝達、超微水冷需求預期！這「散熱大廠」第四季EPS估達32元 大咖法人上修目標價至4500元 - FTNN 新聞；健策AI散熱獲利爆發期| 雜誌 - UDN

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | +4.69% | +6.25% | 3,570.00 | 3,570.00 | 0.00% | 不適用 | 75.13 | 47.59 | 18.59B TWD / 57.39% | 2026-08-01 |
| NVDA 輝達 | 新聞直接提及 | +0.49 | +14.75% | +9.10% | 230.36 | 230.36 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.21 | -7.47% | N/A | 477.57 | 516.10 | -7.47% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱、奇鋐」，共 4 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：重挫, 上修。
- NVDA：新聞直接提及「輝達」，共 2 篇新聞命中。 方向判斷命中詞：上修。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「超微」，共 1 篇新聞命中。 方向判斷命中詞：上修。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [雙鴻(3324)大利多！Vera Rubin水冷板重返輝達推薦名單，2026年營收拚增70% - 鉅亨網](https://news.google.com/rss/articles/CBMiS0FVX3lxTE1EOElpbWM5THBYd3RYemZfX0hHdXEwRUJMTnJROVBUV252cGw1dFZHTUVqel9wWHY4ajVKZDhZakdhZ1hCRVJsRUU4Yw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 04 Sep 2026 06:30:04 GMT
- [輝達、超微水冷需求預期！這「散熱大廠」第四季EPS估達32元 大咖法人上修目標價至4500元 - FTNN 新聞](https://news.google.com/rss/articles/CBMiS0FVX3lxTFBOaVQ2RmoyNFZDZUpyZDVJdEdEUnNWbGVvbGNlczNqZXhqa0FuNHB0cElMcTlfUEVjdDZMMUVBMkRrTXlrRllRb3lHVQ?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 04 Sep 2026 15:15:00 GMT
- [健策AI散熱獲利爆發期| 雜誌 - UDN](https://news.google.com/rss/articles/CBMiUEFVX3lxTFBwQzVHVzJyWGsteHhkWl8tc0ZhT2lVaXZKOEpOUEN6Q2tTRVNFNndFQmVNcVI2YWZyYmtrVklpTVB5UU1mR1RQZU94UEhpNzJF?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 03 Sep 2026 07:26:50 GMT

## 新興題材：OpenAI

摘要：新興題材：OpenAI 相關新聞集中在：EXCLUSIVE: OpenAI agents hijacked German website in previously undisclosed AI breakout this spring - Reuters；OpenAI launches new Astra model amid growing scrutiny over agents' safety - Reuters；OpenAI agents hijacked German website in previously undisclosed AI breakout this spring: Reuters - cnbc.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 新聞直接提及 | 0.00 | +10.99% | +1.56% | 499.70 | 510.12 | -2.04% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：新聞直接提及「OpenAI」，共 3 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [EXCLUSIVE: OpenAI agents hijacked German website in previously undisclosed AI breakout this spring - Reuters](https://news.google.com/rss/articles/CBMixAFBVV95cUxQb0lsYkxySy1tYUVZRnlHQmN5Q1loNW14dl9oYWZ4UFpWX0N6TGNMdUdTSFRHMDBsMzMwazV2RkFkM01jTGFvbHpJUTk4ZVNzVGZJc3FtaWlHMGViMEp2ZHFUcEZuNmF3MUd3UjF3eEc4ZC04MDEwWmp3RlYzSmFPZTNLTVlpTURsdENEdE1FMlNzRjc1TzFQd2tSSUNoQmtxRF9DQUVIR0Ftams3Zm5KUFZ1dHhrZEtKUFlSQUFyeVozSmxk?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 04 Sep 2026 22:46:02 GMT
- [OpenAI launches new Astra model amid growing scrutiny over agents' safety - Reuters](https://news.google.com/rss/articles/CBMiwwFBVV95cUxQbEhVLUYyaUZ3dDB0UGpFemVFREl1RkE0Q2FldS0zQmNQVVNudlNULXg3RXlVdjBId2lKSUJSdGllakNFNzJTMUstb2R1Nm1NQ2R6UEQxZkw1dzRoRG5NLWE0WlJWVGw3Y3VWUkQ3WHNOd1h3YndNZ0FNQ2NmX0JHZnBjakRjemhjWEtvN1RnbUdRdWtSUGpWTkRnTG1ncmQ3Mk5fTmEycGgxemROWDBMNzZaYnlyUVpsYXVLNnNpMHJVV2s?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 03 Sep 2026 18:03:00 GMT
- [OpenAI agents hijacked German website in previously undisclosed AI breakout this spring: Reuters - cnbc.com](https://news.google.com/rss/articles/CBMimAFBVV95cUxQVlE2VzdwcC1mMkpIQm5UY2VvbG44V096UlR0Q196SVNfR3M2WFlaNlJIRWFlY3BPNXRnNHlNb0tTenc1UUgzeWpTanRmRUROZ1lLR1otbUQ4UjVTbWxqeU9yTXZrR1dGTlNJQTE3cE9VRURBOUlXNlJPZktlZk00S1dodXVtdDdZOXlVeXRvZ1ZNWXprQXB1ONIBngFBVV95cUxPd2lDVHNvUU5GWENpUF9Vc1FVcWllVklIMTUyZVF0bXdvem5TYUtxdmJKYzBCUkd1bE5UeUd0YUlSVTZyRzJyTHQwY1NGclhnaDdUWXRoRTlqQmtjelZRNVgtYWZhV2dvOWRRUk1rTFk1SW9sc3lDOFZKWXBwZFNaYVJWakJXNndmUllyb2lZZ0lidGVnNllRdVhqTlo3Zw?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 04 Sep 2026 12:47:12 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel Climbs 4%, AMD Rises 3%, NVIDIA Ticks Up as Chip Stocks Shrug Off Rising Rate Hike Odds - 24/7 Wall St.；Baya Systems選擇AdoreSys為合作夥伴，擴大半導體IP在中國及亞太市場的觸及範圍 - 中央社 CNA；印度半導體2.0 啟動台灣城- 日報 - 工商時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.55 | +14.75% | +9.10% | 230.36 | 230.36 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.26 | -16.46% | N/A | 95.80 | 114.68 | -16.46% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.23 | -7.47% | N/A | 477.57 | 516.10 | -7.47% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.03 | -1.23% | -0.41% | 2,410.00 | 2,425.00 | -0.62% | 背離 | 86.28 | 27.94 | 467.58B TWD / 44.69% | 2026-08-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.03 | -1.89% | 0.00% | 130.00 | 164.50 | -20.97% | 背離 | 6.68 | 19.55 | 25.04B TWD / 30.71% | 2026-09-01 |
| MU 美光 | 產業/供應鏈推估 | +0.04 | +4.70% | N/A | 1,016.59 | 1,016.59 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.04 | +13.22% | +17.17% | 1,740.00 | 2,335.00 | -25.48% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -8.06% | -19.89% | 357.89 | 446.77 | -19.89% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Climbs 4%, AMD Rises 3%, NVIDIA Ticks Up as Chip Stocks Shrug Off Rising Rate Hike Odds - 24/7 Wall St.](https://news.google.com/rss/articles/CBMizAFBVV95cUxORTRMSEJfSFJyWWwtYWNTMDNLNW1qTzVXY2I5N0V6SEp5SzYwakxoVUNBMFlBaHVwRmd6akJUTHhxcVMyZ2MwTkI0SEpHVFZaVDF4MjQyNkdyeFhCUGNhTHBhWHd5YVlOanNGQzNDY1Q3d3gwVEROVXlpYnhYVElKQk9rX25oSzVDREgzZEdKSGFyVnNJdnhKUWVFX2lUeWdCREg5Y1NxOVdTQjJSSU91OE9GZlNnN0lCRElrdW5hOWlXcllmTHRwY0tSRjk?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 04 Sep 2026 15:12:00 GMT
- [Baya Systems選擇AdoreSys為合作夥伴，擴大半導體IP在中國及亞太市場的觸及範圍 - 中央社 CNA](https://news.google.com/rss/articles/CBMiVkFVX3lxTFBwOHFDOXItMVhHeTVtRFQ0czEweWVudlRGZ1FXTVNzTDl5cWpzdFpFQWZGX0wxOFM2MzFTb0hJZ0ZZMWZwcW80M0kzdG5hcFFQUUtMQlVn?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 04 Sep 2026 07:54:06 GMT
- [印度半導體2.0 啟動台灣城- 日報 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1ybjYyMU9kSHQwMHdIckQ2LWJxLVNaZjJzREdhNHE1bVEyX0xtQlVsZHQwakFqeGFESlNsQk94aXgtZl9NWU5YOTBuNHYzSjNuYVJmVmt6MHNtSFVjRi13?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 04 Sep 2026 19:00:00 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》量縮收漲693點/重返5日線；週K連二紅- 新聞 - MoneyDJ；國票證券：台股短線多方力道降溫- 新聞 - MoneyDJ；美股指數期貨最新報價 16:37-台股 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》量縮收漲693點/重返5日線；週K連二紅- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQWTdwbDNkblFUS3V1YmNGREpGNjc1OHlhSGV2amhUMkdvZjE0cUoxaklzekhmaUhUZmdkNVpOX0huZVlUSUNjSmZkOUd0cUpfTms1ZEU1akJweHhPU3QyVWdGTTlTRm9LVDdBanpjLWhDUF9CNENBU2gxdzdfLW5OR1NPenhhZzdseVM3VjlrbXdZZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 04 Sep 2026 07:59:00 GMT
- [國票證券：台股短線多方力道降溫- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQRFZYZVp4WUFjMlgzMjN2ZERFS0RhS21zaHFaT0FaTDYwdG5XT0Q3RTZBTUhYb1MyUlc1M0FzbWtkYTBjbUdHMldtc29FbjNGNGZCa1QwaFdnMk1WTmdfMFl3bHVydmVYTEp3amJjQ2lycWZhV1k0WEdkVDNWVmhuUE1fWWhrQlVYc2hTakNJMVpnUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 04 Sep 2026 00:42:00 GMT
- [美股指數期貨最新報價 16:37-台股 - MoneyDJ](https://news.google.com/rss/articles/CBMiigFBVV95cUxNN285VXJDYWUzOUd3ZktfWmk0VHJ4WHlYWGcza3NqREJmcVFETG9DclBWN2dkZEJTRy1LM0V6T1NtT2dQbEVZXzNNR3J0NUpxUTFjTWI3YmdubXN2TVQxN3Q5MlNhVzV3dHJqRkJiVFJFQmRqaU9jN0lCOVR0NkxabFUzRlk0Y3I0MGc?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 04 Sep 2026 08:48:15 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
