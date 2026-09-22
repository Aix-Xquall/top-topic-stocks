# 每日股市熱門話題分析 - 2026-09-23

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜正向｜熱度 10｜市場確認 100.00｜同向 2/2
2. **新興題材：MoneyDJ**｜正向｜熱度 11｜市場確認 100.00｜同向 1/1
3. **AI 伺服器與資料中心**｜中性｜熱度 16｜市場確認 89.95｜同向 7/8
4. **半導體與晶片供應鏈**｜正向｜熱度 3｜市場確認 89.83｜同向 7/8
5. **綜合市場情緒**｜負向｜熱度 39｜市場確認 0.00｜同向 0/2

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.35（樣本 21）
- 5日相關係數：0.22（樣本 15）
- 同向比例：17/21

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 100.00 | 2/2 | 0 | +14.89% | +23.26% |
| 新興題材：MoneyDJ | 100.00 | 1/1 | 0 | +15.11% | +16.93% |
| AI 伺服器與資料中心 | 89.95 | 7/8 | 1 | +9.57% | +4.72% |
| 半導體與晶片供應鏈 | 89.83 | 7/8 | 1 | +9.53% | +6.38% |
| 綜合市場情緒 | 0.00 | 0/2 | 2 | -8.28% | -10.04% |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：TradingKey | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：6年第2季全球半導體營收 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-09-10 | 0.28 | 0.86 | +75.00% | 4 |
| 2026-09-11 | -0.01 | -0.08 | +25.00% | 12 |
| 2026-09-12 | -0.39 | 0.04 | +25.00% | 20 |
| 2026-09-13 | -0.42 | -0.14 | +17.65% | 17 |
| 2026-09-14 | -0.31 | -0.54 | +33.33% | 15 |
| 2026-09-15 | -0.04 | -0.42 | +68.75% | 16 |
| 2026-09-16 | -0.19 | -0.46 | +55.56% | 9 |
| 2026-09-17 | 0.43 | -0.13 | +66.67% | 9 |
| 2026-09-18 | -0.15 | -0.07 | +35.71% | 14 |
| 2026-09-19 | 0.20 | 0.47 | +46.15% | 13 |
| 2026-09-20 | -0.04 | -0.25 | +30.77% | 13 |
| 2026-09-21 | -0.15 | -0.05 | +61.54% | 13 |
| 2026-09-22 | -0.00 | -0.01 | +88.24% | 17 |
| 2026-09-23 | 0.35 | 0.22 | +80.95% | 21 |

## 歷史回測摘要

- 回測日期：2026-09-23
- 近5日 3日相關：0.10
- 近5日 5日相關：-0.06
- 同向比例：+60.00%
- 權重狀態：已調整

- 方向準確度：+60.00%
- 信心排序準確度：0.10
- 診斷：低相關

調整原因：近 5 日信心分數與股價關係偏低，提高價格確認，降低寬題材推估。；關鍵詞×公司後續樣本有效 4 筆，未達 30 筆，不調整樣本權重

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

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Micron vs. SanDisk: Comparing Two Red-Hot AI Memory Stocks - Yahoo Finance；SNDK Stock 2026: SanDisk Price Forecast, Earnings & Outlook - Tycoonstory Media；SanDisk Jumps 6% as Rosenblatt Starts Coverage at Buy With $2,400 Target; Micron Rises 3%, Seagate Ticks Up - 24/7 Wall St.

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.57 | +12.89% | N/A | 1,096.16 | 1,096.16 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.57 | +16.89% | +23.26% | 1,887.04 | 2,335.00 | -19.18% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +14.01% | +8.40% | 228.87 | 228.87 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、MU」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk、SNDK」，共 5 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Micron vs. SanDisk: Comparing Two Red-Hot AI Memory Stocks - Yahoo Finance](https://news.google.com/rss/articles/CBMinAFBVV95cUxPT1JZU2ZaSmZPVzc1R01SN1c5b2otUjBEX19NcUNCTEdSZkVUTjNya0hHck5GdkN0NEVrSmJDdXdSMWFlZG5hbWI1SGFRcEkzclJqNmNSdFdtaVJKNThsUVRFNDZVOXg4NlVPRUtzRGZ2ejR6RmdJcVpRdVQ5STUxcV80UkZEbFpZTWo1bkNaMnVMajY5ekJKdmtYR1E?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 22 Sep 2026 20:57:00 GMT
- [SNDK Stock 2026: SanDisk Price Forecast, Earnings & Outlook - Tycoonstory Media](https://news.google.com/rss/articles/CBMiUEFVX3lxTE9JSUtaeU1GQ092eC03TllVZmpFWHVjQVBtZW9ZZTFKSVlWWDRpdjY0a2tPZ2xDdjY2Z0JiaWFjbjFOdGxyTmRnYmxqZkNQZWIz?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 21 Sep 2026 06:19:15 GMT
- [SanDisk Jumps 6% as Rosenblatt Starts Coverage at Buy With $2,400 Target; Micron Rises 3%, Seagate Ticks Up - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi3gFBVV95cUxQc3ZteU9CRElRRkd3MTVtdVZ3S2huNF9OV1JGb1R3S2xOZEtnR2RaTmc2cUJVdHhfOXJ5SWt6V2lZYUlmWTBqbkM4Ukp5cTQ2OElCVVVENU9xcDNWMFVxQ0llbjlJNW1RMHB0LXVpOEhwMTBRV2dzVlpuaDVLaE5mREJwR1RTcFNjamxLbV9RdEFnaWkwOEFZbW1fTjdiaUhKc0VBLW1QcG1qRUFzandsX0E0LVloamJYQ1dyVUlfS0lqZURDYU5FNkY4ZXRKMjBYN2hjRERSN1d5ak9zM3c?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 22 Sep 2026 16:04:00 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：台股加權指數衝48601點！創史高後拉回小漲81點照創收盤高- 新聞 - MoneyDJ；《台股盤後》飆新高後漲幅收斂、收漲81點，日K翻黑- 新聞 - MoneyDJ；股市Q4表現不俗 近5年台股平均漲幅居全球之冠 - MoneyDJ

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2454 聯發科 | 新聞直接提及 | +0.42 | +15.11% | +16.93% | 5,180.00 | 5,180.00 | 0.00% | 同向 | 60.69 | 85.55 | 64.18B TWD / 44.08% | 2026-09-01 |

關聯理由（前 3）：
- 2454：新聞直接提及「聯發科」，共 1 篇新聞命中。

### 主要來源

- [台股加權指數衝48601點！創史高後拉回小漲81點照創收盤高- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxOWVZBbXFyVk92YnVKSU5sU2JWdjcyOWRuTVJaUDBwNWZ6OEdQTFNHcGZMVHlEcUlBUlhIRUpHMktaaHpSa05tZVBSSUo1SHBqMmFxSUhlczBtUmViWGJVaTlWTzF1MGNuYk52d1I1Z1JXRDNVaDM3M0pIRm1LaENLTWt1WThSelk3ZFRCNk1nODJoUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 22 Sep 2026 09:11:00 GMT
- [《台股盤後》飆新高後漲幅收斂、收漲81點，日K翻黑- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPd2N1QUQxcndXQklNZnMtNWs1RjN2MUFrQ2Q3R3dqTHhrb3pGbWhJdGJrbkx1Q25IdHZzcjdXWkFYbTRnU204SWhlcTJUWk82Wl95WWZsRjZIalJ5SmQ5azFGVEpYQzFfOGdmT0ZobG5DVWZlZTI0YU9YWmFBb25aek5PYk5mekJ0dHppdWF4YU51dw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 22 Sep 2026 07:53:00 GMT
- [股市Q4表現不俗 近5年台股平均漲幅居全球之冠 - MoneyDJ](https://news.google.com/rss/articles/CBMiiwFBVV95cUxOTVVseTNGdHZrYVE0elBkYkRoZ3R2UTZtUUNrZWVoNjBBOEN0ekQ4bE5YaGNob1NhMjM1S0ptejExbm1vRmRneE1tbzAtTnZpS0ZwODlfUjZsTGk2a21MXzVCRFFISXZ5YndMenhTRWRHOTd2c096X0VURmpfaTRycmtkSnJSelZ3enFR?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 22 Sep 2026 03:07:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel and AMD shares surge as AI chip demand lifts sector - Yahoo Finance；縮短研發陣痛、提早揪出病灶，AI 助攻癌症醫療的三大關鍵 - TechNews 科技新報；AI 成為新使用介面！高通阿蒙揭 Agent 落地化「兩大關鍵」 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.54 | +8.00% | N/A | 123.86 | 123.86 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.53 | +20.86% | N/A | 623.77 | 623.77 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.06 | +14.01% | +8.40% | 228.87 | 228.87 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.06 | +1.44% | +3.14% | 2,460.00 | 2,460.00 | 0.00% | 同向 | 86.28 | 28.52 | 514.81B TWD / 53.32% | 2026-09-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | +10.61% | +1.22% | 498.00 | 507.29 | -1.83% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -6.36% | -18.41% | 364.54 | 446.77 | -18.41% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.04 | +12.87% | +17.06% | 693.00 | 693.00 | 0.00% | 同向 | 13.92 | 50.14 | 82.25B TWD / 45.66% | 2026-09-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.04 | +15.11% | +16.93% | 5,180.00 | 5,180.00 | 0.00% | 同向 | 60.69 | 85.55 | 64.18B TWD / 44.08% | 2026-09-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：surge。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。 方向判斷命中詞：surge。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：surge。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel and AMD shares surge as AI chip demand lifts sector - Yahoo Finance](https://news.google.com/rss/articles/CBMikwFBVV95cUxNMS0zMjgtRWc5UDZKcUdIRW9hYnFSOWcySGFTZFd6S3ZsSm1fa2RHN2sxeGRXS2RmZ1d3VUx4MnJNOVdWSWFPSWRjUk1penlhN2hWUGdqWWtHUFkxQ1E1YXlZYkowUUpqekc4dHFVMjdYZE1pTGZZWk5wVlpNcy1OZXFhd1NLUzFNVmdiNS1mQ0JiQ0U?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 21 Sep 2026 15:50:00 GMT
- [縮短研發陣痛、提早揪出病灶，AI 助攻癌症醫療的三大關鍵 - TechNews 科技新報](https://news.google.com/rss/articles/CBMigwFBVV95cUxOS3ZONkZMamhxZ2RTUXpUSVlFem1LMGRzNEVkNjNYQXNpUmtVenNEWFd6OHgtUUJSZGlZc2ppZlB3OFBoUHA1MmVUaW9GX3J1NGwzY2l6UTRNUEZITWpCSkdUNXMtSGY2OVdCTXh6dnNoSXN4bGRlWDFuYU1xTTBvTXBMQQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 22 Sep 2026 23:20:38 GMT
- [AI 成為新使用介面！高通阿蒙揭 Agent 落地化「兩大關鍵」 - TechNews 科技新報](https://news.google.com/rss/articles/CBMicEFVX3lxTE1sTEI1QThpNzltb1Awdk5SWERpZ3o2UHNIYjJuajFVSkJxWE5ZcW5xR0ptZlE4eUNoM3VVNmhrQ1ItQ2Z4emZBTVJoUlJaMkpvbUh6eXp2STVxVmVlOVFPV0VWWG1YM0VuZzNiM3JPWEk?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 22 Sep 2026 21:57:13 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel and AMD shares surge as AI chip demand lifts sector - Yahoo Finance；UVJC將於WESEMiBAY發表NovaJet，因應半導體產業尋求突破傳統微縮極限的新方向 - 中央社 CNA；正2、半導體台股ETF雙主流- 日報 - 工商時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.51 | +8.00% | N/A | 123.86 | 123.86 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.46 | +20.86% | N/A | 623.77 | 623.77 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.04 | +1.44% | +3.14% | 2,460.00 | 2,460.00 | 0.00% | 同向 | 86.28 | 28.52 | 514.81B TWD / 53.32% | 2026-09-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.04 | +8.47% | +15.52% | 160.00 | 164.50 | -2.74% | 同向 | 6.68 | 24.06 | 25.04B TWD / 30.71% | 2026-09-01 |
| NVDA 輝達 | 產業/供應鏈推估 | +0.03 | +14.01% | +8.40% | 228.87 | 228.87 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | +0.03 | +12.89% | N/A | 1,096.16 | 1,096.16 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.03 | +16.89% | +23.26% | 1,887.04 | 2,335.00 | -19.18% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.01 | -6.36% | -18.41% | 364.54 | 446.77 | -18.41% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：surge。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：surge。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 1 篇新聞出現相關標籤。 方向判斷命中詞：surge。

### 主要來源

- [Intel and AMD shares surge as AI chip demand lifts sector - Yahoo Finance](https://news.google.com/rss/articles/CBMikwFBVV95cUxNMS0zMjgtRWc5UDZKcUdIRW9hYnFSOWcySGFTZFd6S3ZsSm1fa2RHN2sxeGRXS2RmZ1d3VUx4MnJNOVdWSWFPSWRjUk1penlhN2hWUGdqWWtHUFkxQ1E1YXlZYkowUUpqekc4dHFVMjdYZE1pTGZZWk5wVlpNcy1OZXFhd1NLUzFNVmdiNS1mQ0JiQ0U?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 21 Sep 2026 15:50:00 GMT
- [UVJC將於WESEMiBAY發表NovaJet，因應半導體產業尋求突破傳統微縮極限的新方向 - 中央社 CNA](https://news.google.com/rss/articles/CBMiVkFVX3lxTFBBejg3NUhGYmJrMWhMS1FzRmNCbkE5cy0zc242Q1pmTkpEZXNKcW9ENjNwbFZCaGg2RzQzT0U3Z1RyM1hFMXYxS0Mza2tXa0hqUXc3aGdR?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 22 Sep 2026 09:43:22 GMT
- [正2、半導體台股ETF雙主流- 日報 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTFAxcUJXcEZQTTNHZ0llNDhDS1EweXBhMHZETFdVYzNSajJLTlZhZWFLM3Z0OWg5YzBHalREZENKYUZIc0hnUWpzbHRLaXZOaWkyWWh6dGgzSDkxajdxR0Y4?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 22 Sep 2026 19:00:00 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：個股動態報導內容-8420BC5C-5725-4758-8A50-57AC5673A220 - concords.moneydj.com；三大法人買超608億元！台股震盪801點創雙高 台積電翻黑、聯發科創天價 - 經濟日報；台股史上首檔逾2萬元神股誕生！外資目標價竟看到這裡 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | -0.21 | +1.44% | +3.14% | 2,460.00 | 2,460.00 | 0.00% | 背離 | 86.28 | 28.52 | 514.81B TWD / 53.32% | 2026-09-01 |
| 2454 聯發科 | 新聞直接提及 | -0.21 | +15.11% | +16.93% | 5,180.00 | 5,180.00 | 0.00% | 背離 | 60.69 | 85.55 | 64.18B TWD / 44.08% | 2026-09-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。
- 2454：新聞直接提及「聯發科」，共 1 篇新聞命中。

### 主要來源

- [個股動態報導內容-8420BC5C-5725-4758-8A50-57AC5673A220 - concords.moneydj.com](https://news.google.com/rss/articles/CBMilAFBVV95cUxPb2RDWjl6UU1UekxDcW9JR2lpOVhuRWhETWQ2eVZEalZ3ck9YNnlJWDVsOUhZNHphLXdQQXE0bW5WS3VZZWRLMXlaV0ZLRTBySHFuSXBTMy01c0RhWEtOSEpEODVUcndWaFNsNHRSdjV2LUdJWjk3dkFlX19iNXNOTjhRZnVVQWJ6dU42R3NZS04xVE9h?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 22 Sep 2026 10:26:13 GMT
- [三大法人買超608億元！台股震盪801點創雙高 台積電翻黑、聯發科創天價 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5sYzlMXzB2eHVjcWdPc2ZlMlBVV1IzMHpqY0twVC1OM3RBSDJZZWpMbE5YRjJ5T1IyX3VsMllQLWM3cm1rbXIxSHdldU5MbS13ZHpaTDB0b2hJd9IBX0FVX3lxTE9VZUxQeXEtUnFwZkJ5OHJ2MHRkMnc0VUdfRFV6UkMxdmRkVkd6NDBpa21ZZTZJT3gxelBqSVppRDdwekpkdjdEemt5VFFMb2pBMV9fUU9YR3B5RmdCd2Z3?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 21 Sep 2026 09:00:00 GMT
- [台股史上首檔逾2萬元神股誕生！外資目標價竟看到這裡 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBZSGNQUmFRcHI0MHdBLXVHZ0dCRm5Va3FpYVh2d2E2T1I4OTNPbzYyalF2dWxfOTlFZ3R6VlYxalhlVWhmZ1JhRVh0T21Jb1J4RlZ3d3NPWF9od9IBX0FVX3lxTFAyU1dmQlhNZWU0enRrRmlXMVRsa2otYmxDRFBLUTlQQVJ0RTQ0Uzd2TnItbUZlSlhoRGxHU1pYeUhYektNclF1Q3FPRFBSZ1cza2NtTXBhczVPR0V3SWVN?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 22 Sep 2026 00:00:00 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：Micron: Old Valuation Metrics No Longer Matter (NASDAQ:MU) - Seeking Alpha

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | +12.89% | N/A | 1,096.16 | 1,096.16 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +10.61% | +1.22% | 498.00 | 507.29 | -1.83% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Micron: Old Valuation Metrics No Longer Matter (NASDAQ:MU) - Seeking Alpha](https://news.google.com/rss/articles/CBMijwFBVV95cUxNSVhGZUdSc0U1Q21jdjlyMHMyMU42TnBWOGRMUnNmWXdWa1ZWcDZlVU9mZ3J0Yi1ma012a0ROblpaTmRWTzdvUms4em9TR3pja2ktY3JwTFhvUUdzMk9ydUptT3R6bDlUTkszOWpfV2VjSXNweExUcnpFZnQxQWhWYllkaTBtdVZGNEZGSFRSTQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 21 Sep 2026 16:19:16 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Intel Stock Forecast: INTC Breaks $116 as AI CPU Demand Revives the Turnaround - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | +8.00% | N/A | 123.86 | 123.86 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Stock Forecast: INTC Breaks $116 as AI CPU Demand Revives the Turnaround - TradingKey](https://news.google.com/rss/articles/CBMitAFBVV95cUxQVWlmWk1EZlJYOWNWbTMxNGw1aGozS2RYRERpOUtqWHJCYkFJWkFxZGo3cWNCenFxU25ObFA5NWExOXYydnlfdHE0WVVkc1RDZGtuT0NWZ2hTRGQ4RUhmNUZESlJVNkt3UGdsVkZsRVVMUXlHdnlHZFZtUVB0UGRaVUI4SlcwVWk1ZUIwbGliakRPamo0V2gzUTRWaHlTRkFnZmVVQlBLemlOdkJ3c1BPa2ctSVY?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 22 Sep 2026 10:09:34 GMT

## 新興題材：6年第2季全球半導體營收

摘要：新興題材：6年第2季全球半導體營收 相關新聞集中在：2026年第2季全球半導體營收激增31%，創下4,250億美元的歷史新高 - 中央社 CNA

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [2026年第2季全球半導體營收激增31%，創下4,250億美元的歷史新高 - 中央社 CNA](https://news.google.com/rss/articles/CBMiVkFVX3lxTFBqVXY2b3hxMWM2ZDJOODVvaGdaYUtEbFg2LVlqMklMM1k5YVdpZnhWa1B3aG52bW1wbmZTREVTRlRGRi1saVhWTEdIa19hTVlkNHJGT1d3?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 22 Sep 2026 10:02:10 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
