# 每日股市熱門話題分析 - 2026-07-21

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **散熱與液冷供應鏈**｜負向｜熱度 2｜市場確認 74.17｜同向 1/1
2. **AI 伺服器與資料中心**｜中性｜熱度 15｜市場確認 N/A｜同向 0/0
3. **新興題材：R1YP3IyRnV**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0
4. **半導體與晶片供應鏈**｜正向｜熱度 11｜市場確認 0.00｜同向 0/5
5. **記憶體與 HBM 供應鏈**｜正向｜熱度 3｜市場確認 0.00｜同向 0/2

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.12（樣本 8）
- 5日相關係數：-0.03（樣本 8）
- 同向比例：1/8

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 散熱與液冷供應鏈 | 74.17 | 1/1 | 0 | +1.39% | +4.04% |
| AI 伺服器與資料中心 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：R1YP3IyRnV | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | 0.00 | 0/5 | 5 | -11.91% | +0.32% |
| 記憶體與 HBM 供應鏈 | 0.00 | 0/2 | 2 | -8.79% | -0.17% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：將二度漲價 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-07-08 | -0.05 | -0.05 | +71.43% | 14 |
| 2026-07-09 | -0.11 | -0.36 | +64.29% | 14 |
| 2026-07-10 | 0.55 | 0.05 | +77.78% | 9 |
| 2026-07-11 | 0.13 | -0.08 | +50.00% | 12 |
| 2026-07-12 | 0.27 | 0.13 | +16.67% | 12 |
| 2026-07-13 | 0.39 | -0.09 | +15.38% | 13 |
| 2026-07-14 | 0.10 | -0.07 | +21.43% | 14 |
| 2026-07-15 | 0.20 | -0.16 | +28.57% | 7 |
| 2026-07-16 | 0.20 | 0.02 | +33.33% | 12 |
| 2026-07-17 | 0.36 | 0.02 | +60.00% | 15 |
| 2026-07-18 | 0.18 | 0.08 | +53.85% | 13 |
| 2026-07-19 | 0.37 | 0.09 | +12.50% | 16 |
| 2026-07-20 | -0.59 | 0.11 | +45.45% | 11 |
| 2026-07-21 | -0.12 | -0.03 | +12.50% | 8 |

## 歷史回測摘要

- 回測日期：2026-07-21
- 近5日 3日相關：0.70
- 近5日 5日相關：0.52
- 同向比例：+16.67%
- 權重狀態：未調整

- 方向準確度：+16.67%
- 信心排序準確度：0.70
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

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報；無懼逆風 奇鋐、雙鴻權證搶鏡 - 中時新聞網

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | -0.52 | -1.39% | -4.04% | 2,135.00 | 2,835.00 | -24.69% | 同向 | 61.06 | 35.08 | 17.62B TWD / 66.11% | 2026-07-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱、奇鋐」，共 2 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：跌停。

### 主要來源

- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 19 Jul 2026 08:36:46 GMT
- [無懼逆風 奇鋐、雙鴻權證搶鏡 - 中時新聞網](https://news.google.com/rss/articles/CBMia0FVX3lxTFAtNE5HWUdzS3lmc3puT05QWmdEaUIxZ1RvVmFQVTVLWkdEdk92UFJaUUIzV2VLd1RWX2UtY21ZMzVlNmdrUm1mX0tkci00Skp5NnRVc19wTktnelB5SlJuRFEzNHpwVElGTkpj?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 19 Jul 2026 20:10:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel Stock Jumps Ahead of Earnings as Google AI Deal Expands - TradingView；Intel Earnings Preview: Can AI CPU Momentum Survive the Margin Test? - Moomoo；2027 年量產計畫對 AI 產業鏈影響 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 97.06 | 114.68 | -15.36% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -3.72% | +16.56% | 203.28 | 211.14 | -3.72% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 503.57 | 516.10 | -2.43% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -4.92% | -4.92% | 2,320.00 | 2,410.00 | -3.73% | 不適用 | 74.39 | 31.19 | 442.68B TWD / 67.87% | 2026-07-01 |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +2.43% | -20.60% | 402.29 | 506.69 | -20.60% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -15.36% | +22.18% | 378.16 | 446.77 | -15.36% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | -12.59% | -10.90% | 597.00 | 680.00 | -12.21% | 不適用 | 10.86 | 55.43 | 65.78B TWD / 32.86% | 2026-07-01 |
| 2454 聯發科 | 產業/供應鏈推估 | 0.00 | -10.70% | -12.68% | 3,340.00 | 4,310.00 | -22.51% | 不適用 | 62.91 | 53.23 | 58.01B TWD / 2.80% | 2026-07-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 2 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Stock Jumps Ahead of Earnings as Google AI Deal Expands - TradingView](https://news.google.com/rss/articles/CBMivgFBVV95cUxQTXJLeXJyMmE1YWg4Q2FVbXZiWm9tYjFUWmZBNDlwX0hVOXpxVi1FXzNfYlNCd083Vl8ySmluanRlYmVyLVpDazJNZmhzTnRfVDVva0pxMUZGQmRuRy1iYXFScW56a2RVS0N0NmxpeDQ1US1ySDR0RXJubmthMGl0WndycGdfRVQzbXZ2eVQzQTdSQmowRkhpQTNMM0NHYzU2NlliMUdGbEdiTUlHdWRUMTZHbjc4Q19jZS1uVml3?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 20 Jul 2026 16:30:11 GMT
- [Intel Earnings Preview: Can AI CPU Momentum Survive the Margin Test? - Moomoo](https://news.google.com/rss/articles/CBMitgFBVV95cUxQbDdFenFHVjh3TTh1aXRNODdoVWJaYUEtNW8zaU5vb0ZENGNuWUc1OGFQS2RSTVJ4bk81V201OHJ4SW9ad3BoT2Z4b2MxTEdmWnNMbTQxdEVXTDZfSXVHclhWRzVGaGJ3ZTlCbUgyTldXcWlvOUo2VkV4bWEzbDFuSnVUOWtkcU9TVEFDVzRaaXVZYnFsQXpvcmdZbERJai1qTFdzWS11Z00yN1VyQjYtdWtoNUhuQQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 20 Jul 2026 02:32:39 GMT
- [2027 年量產計畫對 AI 產業鏈影響 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiY0FVX3lxTFBSV3AteklGVE9iNm1IeW5KYXNadkY2eHhBS2s2U0ZvSy0wQzBmVnJpb3JBOVg4azBRTnhaY0pYNkZJblY4cy02MEZKZ0xIUmgxQTA1Slk0WnFSR2VKSThMaEQzUQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 20 Jul 2026 18:22:34 GMT

## 新興題材：R1YP3IyRnV

摘要：新興題材：R1YP3IyRnV 相關新聞集中在：What Just Happened To AI Stocks? (Micron, AMD & Nvidia Explained) Tampa Bay Rays (R1YP3IyRnV) - Mshale

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | 0.00 | -3.72% | +16.56% | 203.28 | 211.14 | -3.72% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | N/A | N/A | 503.57 | 516.10 | -2.43% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 865.46 | 971.00 | -10.87% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MU：新聞直接提及「Micron」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [What Just Happened To AI Stocks? (Micron, AMD & Nvidia Explained) Tampa Bay Rays (R1YP3IyRnV) - Mshale](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9EbHNjRlRhMTc5ejJqQTNtdlRRM1ZwV0JaR25fLW1uTWtONVR6N3pqM0NDcWJwZHdUVUpEdmpWN3VfRFRHcGF0QnhSTXk4NUVCSmE0ZkRQaEdNc1E?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 20 Jul 2026 20:26:07 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Why Intel Vs. Taiwan Semiconductor Isn’t a Real Competition Through The End of 2026 - 24/7 Wall St.；Chip stocks rebound ahead of key earnings, but risks from earnings and geopolitical tensions remain. - Pluang；Intel Earnings Preview: Can AI CPU Momentum Survive the Margin Test? - Moomoo

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.59 | N/A | N/A | 97.06 | 114.68 | -15.36% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | +0.27 | -4.92% | -4.92% | 2,320.00 | 2,410.00 | -3.73% | 背離 | 74.39 | 31.19 | 442.68B TWD / 67.87% | 2026-07-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.03 | -21.69% | -15.31% | 130.00 | 164.50 | -20.97% | 背離 | 4.00 | 32.66 | 23.12B TWD / 22.85% | 2026-07-01 |
| NVDA 輝達 | 產業/供應鏈推估 | +0.02 | -3.72% | +16.56% | 203.28 | 211.14 | -3.72% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.04 | N/A | N/A | 503.57 | 516.10 | -2.43% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | +0.04 | N/A | N/A | 865.46 | 971.00 | -10.87% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.02 | -13.87% | -16.91% | 1,390.95 | 2,335.00 | -40.43% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -15.36% | +22.18% | 378.16 | 446.77 | -15.36% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「Taiwan Semiconductor」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip, foundry。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 4 篇新聞出現相關標籤。

### 主要來源

- [Why Intel Vs. Taiwan Semiconductor Isn’t a Real Competition Through The End of 2026 - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiwwFBVV95cUxNd29XTzNJSmRYX01EZnh4VUxBaG1Ya3RFaWF2bEFVR0gyMkRPblp1U2p1ZkN6TnJiTFV1TG1fbjA3RGt4VzJLY2NoSUNyM2tVQ3J0VmtNYVFDekpYMndOQU5YNTRGTDczdU5JY09MRXR1Nm43b2ltbklFOXhvV0FPaDJqTTJNSFJhczhYLU0xQzlZRVpuWlBiTTNKQ2c0anVZaUxpdGhnMTZ5RXpmX1hLNEpyLUJWT091VF9qY2d0dTluOE0?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 20 Jul 2026 15:33:53 GMT
- [Chip stocks rebound ahead of key earnings, but risks from earnings and geopolitical tensions remain. - Pluang](https://news.google.com/rss/articles/CBMigwFBVV95cUxPY1gtWGQyTXZLZmVEa2VTaGRtSWU3ZWlZcWJTRTQ3VXp0Yk5EeHo4TzU0bnFObkUyWEtHVWx0aUFWZ08zU01JQk5DZEVCMXY3eXRRdW5CbnBqMEY2YTRFZ1lUYzRUN1ZiOHF1Q2lVbm14dmJVTlRRc2xHU0lVRlUtaFgyVQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 20 Jul 2026 17:41:56 GMT
- [Intel Earnings Preview: Can AI CPU Momentum Survive the Margin Test? - Moomoo](https://news.google.com/rss/articles/CBMitgFBVV95cUxQbDdFenFHVjh3TTh1aXRNODdoVWJaYUEtNW8zaU5vb0ZENGNuWUc1OGFQS2RSTVJ4bk81V201OHJ4SW9ad3BoT2Z4b2MxTEdmWnNMbTQxdEVXTDZfSXVHclhWRzVGaGJ3ZTlCbUgyTldXcWlvOUo2VkV4bWEzbDFuSnVUOWtkcU9TVEFDVzRaaXVZYnFsQXpvcmdZbERJai1qTFdzWS11Z00yN1VyQjYtdWtoNUhuQQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 20 Jul 2026 02:32:39 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：What Just Happened To AI Stocks? (Micron, AMD & Nvidia Explained) Tampa Bay Rays (R1YP3IyRnV) - Mshale；Micron stock up 3%, SanDisk gains 2.5%: what woke the memory trade? - Invezz；Micron Has Strong Q3 Earnings and Rising Guidance. Is It a Buy? - 24/7 Wall St.

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.50 | N/A | N/A | 865.46 | 971.00 | -10.87% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.21 | -13.87% | -16.91% | 1,390.95 | 2,335.00 | -40.43% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.19 | -3.72% | +16.56% | 203.28 | 211.14 | -3.72% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.37 | N/A | N/A | 503.57 | 516.10 | -2.43% | N/A | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron」，共 3 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：strong。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 1 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [What Just Happened To AI Stocks? (Micron, AMD & Nvidia Explained) Tampa Bay Rays (R1YP3IyRnV) - Mshale](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9EbHNjRlRhMTc5ejJqQTNtdlRRM1ZwV0JaR25fLW1uTWtONVR6N3pqM0NDcWJwZHdUVUpEdmpWN3VfRFRHcGF0QnhSTXk4NUVCSmE0ZkRQaEdNc1E?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 20 Jul 2026 20:26:07 GMT
- [Micron stock up 3%, SanDisk gains 2.5%: what woke the memory trade? - Invezz](https://news.google.com/rss/articles/CBMinwFBVV95cUxOV3otdFpxVllCV3h6WW9QdU95X3U2Smx5WUYzNXVia01uUzZ5NUMycFE1akxHdG5PSzZxX3p5ZXZGZVhjeElNOWlNMkJlZHBIVTdGaUJfVWUxX3JORkRQNW9VRWVOUjVYZVVHbnE4UGVmVFhHZkRVTHVaQ3VuTWF1MzY3UlhOaHlVN1pJMzVDLXRRTEJFQ1V6QmNhcUNnV1U?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 20 Jul 2026 10:12:29 GMT
- [Micron Has Strong Q3 Earnings and Rising Guidance. Is It a Buy? - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiwgFBVV95cUxNRElYbENRSXhjYnFvTm0tV3BIN0ltWEQtYkZvaGhOWnRYRU1hcEhQSDVDSFdRYzhqZ1p5WDNHc2dKZnRIQVVkcGlSbmpGWEl4dUtUVENfTC1BaGl3dlJQUWNjTnVfeTNnM19LcWR2ZkNUVUdDU01JUm5Ddk9kRnZZcl84NWFXMU5XM0RKQzFWNE5tWDkydF9hampQRGlBT3JyT1JGX055d3NvQVlUeHBrY0oydFZZcGJ2TjNIaWdmMkxidw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 19 Jul 2026 16:00:50 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：投信砸146億元撐盤、外資賣壓驟減！台股震盪逾1,100點收跌221點 - 經濟日報；台股戒備三情境推演 樂觀情況收復43,525點季線關卡 - 經濟日報；綠色證券宣導 回響熱烈 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [投信砸146億元撐盤、外資賣壓驟減！台股震盪逾1,100點收跌221點 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBhMVoxbklyS3lFYUdBYmFiT01qTXhaZjJ5a3ZUUDNueE9sT0tIbnFBZkJhRmc1T1QyNEhNRFdZUkNWZWZheUtGcTdtWFJyUEdqQ2JISWRZWm9zQdIBX0FVX3lxTE9MX3NQQWE3V0JmdWtPYVFITE1vTVNSVUJ0c3pGeUhHNDN6VE5jdWdudmdHMzIzdUo5NHBZVlpDTEJrWnBzQVB2QWFkSFp5WkdiTF80VnhWSFItcERVbTlR?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 19 Jul 2026 09:00:00 GMT
- [台股戒備三情境推演 樂觀情況收復43,525點季線關卡 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBDdm1BbVNIN1FfNHRyY1NtYU02QXFrRjczYXMtc1VtUnMxOFpZM3pMMXdLZ01ndWJXM3hZcXE3azZoWE9IbW9CalRsUzltaV9XTDV2ZVhzSDJIZ9IBX0FVX3lxTE9BZ29kTGdVUlNYZXF4aUtwQ2t0RWczQ1VYMXV3V0FvUXQ0Z1FENFBSR08wWlVha1U3N0xiSjBjLXhpUlJGenNxU2k3RU9DX1NNM3lqa3ZoT09ocHRkenBR?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 19 Jul 2026 17:21:56 GMT
- [綠色證券宣導 回響熱烈 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxPMkhWa2xCeV94WlJ5bzFfTFpJQjlfVHFkNjlBVmNtc1RQcnhCWXpzbVdsMUFBaHRtcldiMGNnNjhZTEdubkVXTFQ0Y3lVclBQM05vU1FWWjA2ZDh5SlZIc2VHT0ZnNXljbjF2VWpnWGt0Y3RCNnhFSTVjcVAxaFF2ctIBX0FVX3lxTE83STIxOTdENUFCU1VCVmZwdlZlNVpxUm1GczMtMUp1ZWJfeVZJVTdLd0pRTnhpXzZ5R1J0dmNTTGJXdzBUcldLUGZ6a1R0Vy1MeVl4b3VWaElEcUt0b0lV?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 20 Jul 2026 16:53:41 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》投信買超146億難撐盤 震盪收跌221點 - MoneyDJ；台股單日跌逾1500點後1個月皆正報酬布局ETF正逢時- 新聞 - MoneyDJ；統一投信：台股續擁AI紅利，震盪逢低分批布局- 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》投信買超146億難撐盤 震盪收跌221點 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPbW41ZWVCSzE2Yk9WUDFGTDRPcFREc1U3dUVpVUlWYXRsX3FHbGo3cFVqMWZhOVR3MWgxWmNTUlk5ZzZlZ2VLZERXUTYxX0FiTFJWZFhzS3NkZlZTSk9zODRTMzg2ZXp3M0xqS2hnVThrelM4eHhNNDVYZ0pWN0wybnhwQU9MWnFDai1RcGI2ZVo5QQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 20 Jul 2026 07:53:00 GMT
- [台股單日跌逾1500點後1個月皆正報酬布局ETF正逢時- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxOYnpyM1hjcGxaM3hRQUhvMi0tOWt0U3NDcXlIV0J3LTQwQkVZaUNkU2IxY0xQOW1LeWxHSngyM1VpZGVuaWdia1dGUWxFVjRXc0VDSDhpaHJHT1VaNnptbDlSbll3MWRUUzRfYU9hbGFud3BEemxvZ2NPbUVTQm5qWnpHVFdCcU1fbXFuRWxzZXVfUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 20 Jul 2026 05:09:00 GMT
- [統一投信：台股續擁AI紅利，震盪逢低分批布局- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPVm51VFYyZ3RDSlZPN0d2NlVyU214U1ZSTlhNdTFVYlJCNHJfUjNadDYwMG1UN29FOG9SclNaUUFCdE90UDQ2UUw5SnNDYlRtU1h4MXdjbVZOZUROb3hFUUdfX3J1TTg5c3NZY182XzBxUnJoampGYVdoUkpqUWY5Z2hBbXRTQmFlTUFmbjRBaTVkUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 20 Jul 2026 07:00:00 GMT

## 新興題材：將二度漲價

摘要：新興題材：將二度漲價 相關新聞集中在：高盛：CCL 將二度漲價 | 市場焦點 | 證券 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [高盛：CCL 將二度漲價 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMidkFVX3lxTE9zTXJYMjBRUnRVN1NmVDB0SkF1WXgyandBX3kwb3J0dzZ0WmdDcHJja0ZHRHB6NzJwS2tqZE9uUE0ydHdLNjIxMmUzbjlNRUdFUkxuZEhCb0JqcmZJSC11WjBmQnZGeXBxVlRYV19EOVFQUl8yR0E?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 20 Jul 2026 17:25:09 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
