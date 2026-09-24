# 每日股市熱門話題分析 - 2026-09-24

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **新興題材：MoneyDJ**｜正向｜熱度 12｜市場確認 100.00｜同向 1/1
2. **AI 伺服器與資料中心**｜正向｜熱度 12｜市場確認 84.14｜同向 7/8
3. **記憶體與 HBM 供應鏈**｜中性｜熱度 7｜市場確認 N/A｜同向 0/0
4. **散熱與液冷供應鏈**｜正向｜熱度 2｜市場確認 73.51｜同向 1/1
5. **新興題材：TradingKey**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.05（樣本 10）
- 5日相關係數：0.42（樣本 8）
- 同向比例：9/10

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 新興題材：MoneyDJ | 100.00 | 1/1 | 0 | +18.25% | +20.71% |
| AI 伺服器與資料中心 | 84.14 | 7/8 | 1 | +7.63% | +3.68% |
| 記憶體與 HBM 供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | 73.51 | 1/1 | 0 | +1.17% | +9.29% |
| 新興題材：TradingKey | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：OpenAI | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 相關性偏弱；應提高同向價格確認權重，降低泛 AI、泛半導體等寬標籤推估權重。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
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
| 2026-09-24 | 0.05 | 0.42 | +90.00% | 10 |

## 歷史回測摘要

- 回測日期：2026-09-24
- 近5日 3日相關：-0.25
- 近5日 5日相關：-0.13
- 同向比例：+12.50%
- 權重狀態：未調整

- 方向準確度：+12.50%
- 信心排序準確度：-0.25
- 診斷：方向與信心皆需修正

調整原因：近 5 日有效樣本 8 筆，低於 15 筆門檻，暫不調整權重。

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

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：基金-FundDJ基智網 - MoneyDJ；《台股盤後》量縮收漲357點、首登48K，日K翻紅- 新聞 - MoneyDJ；台股首檔聚焦中小股本主動ETF 台新00416A將開募- 新聞 - MoneyDJ

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3037 欣興 | 新聞直接提及 | +0.42 | +18.25% | +20.71% | 1,160.00 | 1,160.00 | 0.00% | 同向 | 15.49 | 77.23 | 17.75B TWD / 56.26% | 2026-09-01 |

關聯理由（前 3）：
- 3037：新聞直接提及「載板」，共 1 篇新聞命中。

### 主要來源

- [基金-FundDJ基智網 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxPZlZhWXZqbGs0QVIxS3lDNFBVTmRfQ1JQZnVhaGZoaHJUY2l5ZlRQQkNfOHpmOEk1OTdDcFk0d292eWk3N29JeHQ5MEN1enVNX1JZZFlZZXdfNldGTTZRRkJkdy04NExFd3VzTzlzbEFIREZCbGNoZS1taDBVQXhSNDBkRmo3S0QtTnZZcG5WOC0?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 23 Sep 2026 18:07:08 GMT
- [《台股盤後》量縮收漲357點、首登48K，日K翻紅- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQZFFkbE41ODUyTHZJdmprd3Roa2ZTWFlaMlMwWDV3ekVLckxKelpKaDVaNENkXzRlck1pNGZNRlRpSXF4RjBOOEtKMVE1ekUyNGRWRzgzajlDR2ZGaGoyeTk2amFSUHh0U3ZYVlppeGlFaV9MZ1V1NHZ6NHlDSk9MQjZfTkhtWkFxQVJBTVV5bllUUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 23 Sep 2026 07:53:00 GMT
- [台股首檔聚焦中小股本主動ETF 台新00416A將開募- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxOdzI5bGR2SUx4SlhsVk9NVi1qNGlVbzVzZGlWX1JwRExzZ2ZPSHZWalQ5dEtjUG1DOTdDU05URURQZ0VteWJGQXhEeHZhLXBRczVRMzdnbWc3aXdHNWFZSDBrdW9XSmt5VUhTdm56OXhUa1lVcjlXX3VNNVRIMWpWeUh2TXd5MmFPMkxfbWUzRXVPdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 23 Sep 2026 10:25:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel: Beware The Muse AI-Driven FOMO Rally (NASDAQ:INTC) - Seeking Alpha；ASML vs. Intel: Which AI Chip Stock Is a Better Buy in 2026? - The Motley Fool；從雲端算力到邊緣實體智能，剖析 AI 晶片架構與光通訊技術新趨勢 - technews.tw

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.57 | +6.91% | N/A | 122.60 | 123.86 | -1.02% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.06 | +12.33% | +6.81% | 225.51 | 228.87 | -1.47% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.06 | +19.09% | N/A | 614.61 | 623.77 | -1.47% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.06 | +1.63% | +5.04% | 2,500.00 | 2,500.00 | 0.00% | 同向 | 86.28 | 28.98 | 514.81B TWD / 53.32% | 2026-09-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | +11.18% | +1.74% | 500.59 | 507.29 | -1.32% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -8.81% | -20.54% | 354.99 | 446.77 | -20.54% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.04 | +8.62% | +14.55% | 693.00 | 693.00 | 0.00% | 同向 | 13.92 | 50.14 | 82.25B TWD / 45.66% | 2026-09-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.04 | +10.08% | +14.46% | 5,185.00 | 5,185.00 | 0.00% | 同向 | 60.69 | 85.63 | 64.18B TWD / 44.08% | 2026-09-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC、Intel」，共 2 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel: Beware The Muse AI-Driven FOMO Rally (NASDAQ:INTC) - Seeking Alpha](https://news.google.com/rss/articles/CBMiiwFBVV95cUxQSmo4Z0VXeENYMGJtdUFNR1pQQ19nTE1JV1ZuY05uN1dMX2JFeFMzNlhmUFZ5VWtaemI3SUFmNDRQYURXOEhmVzhLbFAxN0JkLXdaV0F4cGJ1WTdjYXlKVmxTV1lNNHdRcmRleWN2QjJWNG51c0JWb2s2dU9nVVFKNzc2TnNndUNnLVlV?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 23 Sep 2026 18:45:24 GMT
- [ASML vs. Intel: Which AI Chip Stock Is a Better Buy in 2026? - The Motley Fool](https://news.google.com/rss/articles/CBMinAFBVV95cUxNZmJlSXBIOEc4cGpIbFNWLVlYMFNER3EtcHJGa2lSd3owTUJoQ182Y29MbzVmNlJFbkI5QXU2d2ZobV85RE1naE1yd2pxZ1A0cDJySTc1RE5HaEdFZ2pHUmgtV0xaN1Y1TGpLVVRNVjZRNmFKMzBlVHVCclJPV2NtM3Aya04zdE1JM3gtaTgyeUJIelNVbEVJWnVoTkE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 23 Sep 2026 00:35:00 GMT
- [從雲端算力到邊緣實體智能，剖析 AI 晶片架構與光通訊技術新趨勢 - technews.tw](https://news.google.com/rss/articles/CBMiswFBVV95cUxOcG1QZGxfdDhHdmRVa1VhQ0NwajRfSExlM081T2FIbllSSVRwYUFWbWY5RHh5Yks4NDU5ekNYd1gwdkgwZWpRWGRYb0tYR3Jzcmt2S2h0YXVOa1BlWkdGa1dyUmZVVE0tMy1Zd2Q3bndFdDd2bXpJR1EtSWFnemI1T29TNV9IMU9hX21uQlVQc0FLZkpfSEcxdDBkalpTT3RvQWgydzBpYzRzV1ctLUVjNm1Ebw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 24 Sep 2026 00:03:51 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：AI Is Supercharging Memory Stocks. Are Earnings Lying? - Micron Technology (NASDAQ:MU), SanDisk (NASDAQ:S - benzinga.com；Micron vs. SanDisk: 2 AI Memory Winners, But Only 1 Is Built for the Long Term - barchart.com；This AI Memory Stock Is Up More Than 650% in 2026. Micron Investors Should Pay Attention - Insider Monkey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | +10.39% | N/A | 1,071.88 | 1,096.16 | -2.22% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | +16.89% | +23.26% | 1,887.04 | 2,335.00 | -19.18% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +12.33% | +6.81% | 225.51 | 228.87 | -1.47% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 5 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AI Is Supercharging Memory Stocks. Are Earnings Lying? - Micron Technology (NASDAQ:MU), SanDisk (NASDAQ:S - benzinga.com](https://news.google.com/rss/articles/CBMijgFBVV95cUxOS1JKQnpjUDQtX19oM2VoMnFWb2hPTll1RG12N2d6bHM4bnFBNkxkWW94UGJrLVNrZFZUS2djcFZuYmFKeDJSUHVQWVBpYlBpSy1jT2dxam1ZS0lVQkJFUU9wZU9tU3Y3Z1VkOUJUOU4zS2RfMW9oMS1JQlBwaUQzZDZoRWl5NkZDcFAwQ3F3?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 23 Sep 2026 18:10:35 GMT
- [Micron vs. SanDisk: 2 AI Memory Winners, But Only 1 Is Built for the Long Term - barchart.com](https://news.google.com/rss/articles/CBMiuwFBVV95cUxOSnF2TFZJME9Dc1hVcE9sa0dBWGF5enc4d1lVeTVCUzFfVGFUOTgtcGdiLTdpcDBXNEktbDI1cnNkaGxfcjkxRlR1UzVncHdkcE9QZjdzSE1meFpTLXRGaVVEOHo5SGo2RXlZc0pGTTAwc0h0b2MzVTJ0S2tYSEhiTGllZ09qUGxkMF9HdzQ4V2w3UmlYVXQ3MVAwbVhqNFRmYTEyWnptX2NUYnkwZjR0XzNncmd3UTFCZW1B?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 23 Sep 2026 11:30:02 GMT
- [This AI Memory Stock Is Up More Than 650% in 2026. Micron Investors Should Pay Attention - Insider Monkey](https://news.google.com/rss/articles/CBMi0gFBVV95cUxOd3k5VWk5Q01fMlNHRy1pLW1xTUtGSEpkeXh0UC1xQ2FGOVdrSXJaMk9RQlVyWTJ5MkQwLXpfMVVMTlh4akt5azZrV2dSV3NBRmFLWVpPc1NCVG9FY0RtUEJHSzZtS2piMURSRmc0OUNtYnlfTmNDdGVYWDNIT2NHOVZDRUM2SUtsSzlMUDVvWmw4cWpCUFNEeENGaGV1emphb0NYc2MyZk5iZjhTMEtTcDcwcm5xRXhtU1AyQWtqT2FVQjlFaUs4dncxaWptY29MOEHSAdIBQVVfeXFMTnd5OVVpOUNNXzJTR0ctaS1tcU1LRkhKZHl4dFAtcUNhRjlXa0lyWjJPUUJVclkyeTJEMC16XzFVTE5YeGpLeWs2a1dnUldzQUZhS1laT3NTQlRvRWNEbVBCR0s2bUtqYjFEUkZnNDlDbWJ5X05jQ3RlWFgzSE9jRzlWQ0VDNklLbEs5TFA1b1psOHFqQlBTRHhDRmhldXpqYW9DWHNjMmZOYmY4UzBLU3A3MHJucUV4bVNQMkFrak9hVUI5RWlLOHZ3MWlqbWNvTDhB?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 23 Sep 2026 11:03:30 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：熱門股／散熱強攻！健策漲停飆天價、富世達同創高 奇鋐漲近6% - 非凡新聞台；〈焦點股〉健策獲日系外資上修EPS預估 漲停飆天價6410元超車大立光 - news.cnyes.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.43 | +1.17% | +9.29% | 3,470.00 | 3,470.00 | 0.00% | 同向 | 75.13 | 46.25 | 19.48B TWD / 54.34% | 2026-09-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐」，共 1 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：創高, 漲停。

### 主要來源

- [熱門股／散熱強攻！健策漲停飆天價、富世達同創高 奇鋐漲近6% - 非凡新聞台](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBwdlhaS2Z5TC1XVVRHSXBZMUNnVGY0ejdRVzZZR0FXVzJPRU54Wl9mT1R4NmR1R3FJV1k4d1Q5a3VpWkw2QnZWcUVMZExUUmtCS3dhaHhDeHEtZDFjRmdn?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 23 Sep 2026 12:03:36 GMT
- [〈焦點股〉健策獲日系外資上修EPS預估 漲停飆天價6410元超車大立光 - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTE15alJDZGZINHUwdjBqQXZnM2UtMEhlV1QxbzQtamx4VDdxTUloaVZpQmQ4cGo0aVp1VnBaNjctUS04SlR1TXBucF9yNTNJdDA?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 23 Sep 2026 04:50:22 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Intel Stock Price Forecast: INTC Nears $125, Can AI Server Demand Push Shares to $140? - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | +6.91% | N/A | 122.60 | 123.86 | -1.02% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Stock Price Forecast: INTC Nears $125, Can AI Server Demand Push Shares to $140? - TradingKey](https://news.google.com/rss/articles/CBMiyAFBVV95cUxQZGMwenNzeUZwcFVzcllxeXl1empBT1FleElvd2pOOTdQUlhMX0lrLUJlTG40SFFvazVLOC1tSnNOZ1EyRTFIa1dzT3BGdkVMTTNlNU9vYnpFVTVlQVhGbHkwM3M4U3RQYlk3YnJfSnVqZzZDanBiV0hSb3dDNGUxMkVBNWdfOUpPYjZqenBvX3FqSTRpc3ZYeDZzaUFCV0l3Y21pNnV5Zlc3ZE0zYUFia1M5dzJneEJnZ2h2V1k1WWFPX3p5WDdyWg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 23 Sep 2026 09:03:09 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：ASML vs. Intel: Which AI Chip Stock Is a Better Buy in 2026? - The Motley Fool；INTC, AMD, AVGO: Chip Stocks Jump Premarket After Nvidia's Blowout Report - Stocktwits；從雲端算力到邊緣實體智能，剖析 AI 晶片架構與光通訊技術新趨勢 - technews.tw

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | +6.91% | N/A | 122.60 | 123.86 | -1.02% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +12.33% | +6.81% | 225.51 | 228.87 | -1.47% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | +19.09% | N/A | 614.61 | 623.77 | -1.47% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | 0.00 | -8.81% | -20.54% | 354.99 | 446.77 | -20.54% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +1.63% | +5.04% | 2,500.00 | 2,500.00 | 0.00% | 不適用 | 86.28 | 28.98 | 514.81B TWD / 53.32% | 2026-09-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +2.56% | +12.68% | 160.00 | 164.50 | -2.74% | 不適用 | 6.68 | 24.06 | 25.04B TWD / 30.71% | 2026-09-01 |
| MU 美光 | 產業/供應鏈推估 | 0.00 | +10.39% | N/A | 1,071.88 | 1,096.16 | -2.22% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | +16.89% | +23.26% | 1,887.04 | 2,335.00 | -19.18% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel、INTC」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [ASML vs. Intel: Which AI Chip Stock Is a Better Buy in 2026? - The Motley Fool](https://news.google.com/rss/articles/CBMinAFBVV95cUxNZmJlSXBIOEc4cGpIbFNWLVlYMFNER3EtcHJGa2lSd3owTUJoQ182Y29MbzVmNlJFbkI5QXU2d2ZobV85RE1naE1yd2pxZ1A0cDJySTc1RE5HaEdFZ2pHUmgtV0xaN1Y1TGpLVVRNVjZRNmFKMzBlVHVCclJPV2NtM3Aya04zdE1JM3gtaTgyeUJIelNVbEVJWnVoTkE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 23 Sep 2026 00:35:00 GMT
- [INTC, AMD, AVGO: Chip Stocks Jump Premarket After Nvidia's Blowout Report - Stocktwits](https://news.google.com/rss/articles/CBMizwFBVV95cUxPQUU4dTZXYndUX2YwZlZ6VmR6d3JoV2dDbE1XR1FKS0p2YTZScmlIclZkTUxxb0paRW00TEgwVlE1Qk5hT3BnM3J4eVZqVDBpZ3o1blFiYTQ5M2t3OTlJU3pud01kVlJYQzFVaF82a2xfWXRfM2R2MzBVRDczX0pnRkpPZ3dpam03QlhibkliRnQ3NWhJU25VM0d1bVlvSm02bjJaV2pjZlJwTUpVVnZCMHRxYjFFd2Q2RXRNOFl3ZkItc0llS0JKR2dVN1VORDg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 22 Sep 2026 09:08:11 GMT
- [從雲端算力到邊緣實體智能，剖析 AI 晶片架構與光通訊技術新趨勢 - technews.tw](https://news.google.com/rss/articles/CBMiswFBVV95cUxOcG1QZGxfdDhHdmRVa1VhQ0NwajRfSExlM081T2FIbllSSVRwYUFWbWY5RHh5Yks4NDU5ekNYd1gwdkgwZWpRWGRYb0tYR3Jzcmt2S2h0YXVOa1BlWkdGa1dyUmZVVE0tMy1Zd2Q3bndFdDd2bXpJR1EtSWFnemI1T29TNV9IMU9hX21uQlVQc0FLZkpfSEcxdDBkalpTT3RvQWgydzBpYzRzV1ctLUVjNm1Ebw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 24 Sep 2026 00:03:51 GMT

## 新興題材：OpenAI

摘要：新興題材：OpenAI 相關新聞集中在：Australia says OpenAI agent breached government health data portal - Reuters；OpenAI and Anthropic CEOs push for AI cooperation at UN after Trump rebuffs 'globalist scheme' to control it - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 新聞直接提及 | 0.00 | +11.18% | +1.74% | 500.59 | 507.29 | -1.32% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：新聞直接提及「OpenAI」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Australia says OpenAI agent breached government health data portal - Reuters](https://news.google.com/rss/articles/CBMixwFBVV95cUxOLWZud0ZEMW9uYlUwVlpoRlBIbW82Tjc4Rjl3WW5jcWxVR25wSmZCTXlOdHkwR2VrQzdzZkUwX3lNMXBGUkZMZU1sYS13dzRRb1RMRzFOVjc5RmJIbXFfNy1ob1VZY1ItYS0tQW9XVHNLc3p3UEJwNy1QRWVSYVFjQnh0ellEX2JSZkpSdXlMYVI4UkV2VE05enVnZFJuV3BaS1pVczF5VE9vaTdZOGZyU2tjTk9oVVE5RVBjTnVWNGNUZzVEZDM0?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 23 Sep 2026 22:34:30 GMT
- [OpenAI and Anthropic CEOs push for AI cooperation at UN after Trump rebuffs 'globalist scheme' to control it - CNBC](https://news.google.com/rss/articles/CBMicEFVX3lxTFBnYmxuWFJ2T3UxeFlEbFlOY3VvVjFzaHQ2U2Z2MHlPZ0Q5c01zQ19aQmlGNE1hcnBUQWk3WTlXSmk4cUI0ZFp3TTVndkNDa3Q1RFFWdjdjV1lZWDJVZkpmaldLdEowRXpkSEZid2piVUXSAXZBVV95cUxNMHZEbDdqaUUwYy1xbTYxQ1dSWTJBZGhRRS1BOThUWTVKQnpBSnl3aTktbkN3Vmx2WGR1clRVZExIdDF0TU5meWo2T0wzek1HZTNQZnQ1SjNhTm9PZTJOTkMxUkxiWVdjRnZ5R21ZR3dLTmZyeGRR?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 23 Sep 2026 19:53:12 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股商品總規模衝破8兆 - 經濟日報；台股科技基金紅不讓 前十強近一周報酬率逾8% 全數超越大盤 - 經濟日報；台股「高彈力」ETF 搶鏡 7月底大盤反彈以來 績效十強勝出 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股商品總規模衝破8兆 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE0xLXVnZThPSnlWcG5rdnFTb1BURmVpQUJJVlU4dTdjME4tVzBHT21FTjZfbzZsZ2hVTEE3S2xyb0ZuTl9rMTFiZ08zM2sxRXE3eW8tVGZZdGRmQdIBX0FVX3lxTE1obHZoM1NEUVRSWXFhaElhckk5Wnh5VlZuYUVSTGZhVl9JVEdTYzd0MmQ5eVVWVGRMYTZWWUNtZWJtbXRrUUxtWUJreWhYTkJuOVF5U3RxdVdmNFc2VndB?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 23 Sep 2026 17:28:47 GMT
- [台股科技基金紅不讓 前十強近一周報酬率逾8% 全數超越大盤 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBVM2ZZUWI4b2ZRUUstMy1VZDNwcWlxVVBjSGN1QVNrazhRZWRDQUNlS3FiRU5zRGlEVjBwNVNmcDRiekFkOWhSMmVfNEFCWW5Id05uQ1ZsSk0zd9IBX0FVX3lxTE9MT05Kb2xMYnVmU1pOTzk1OHRpOWkyMHBhb0g0dHZpbzg0NnhBTzJwLVM4V0Utam9fWi1uZGIzOC1uZEtqMV93U3czbV9SYmRhLUc1UGZ0MEZtOXRHUHh3?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 23 Sep 2026 17:33:04 GMT
- [台股「高彈力」ETF 搶鏡 7月底大盤反彈以來 績效十強勝出 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBCYTFfZ3NNdzAzMWdnTmdBeFltTk01eU9uOWpFLThLM041dEhOWkx3S2k2OUtXQ090SDVwRlpxUDNLQ0pITnZnTkRHN3dTcVhsanRGM2JrZC1CZ9IBX0FVX3lxTE91RWN5M1M4ZTNoc1ZYR0ZLWG1nVHNRODdqOXpaeHFUcXF5dU41VU84QTh6bDlWVnZ2Y1NQX1JkbF9SbFg5VHc4X3ZnN3NQUjAwbExnY24xbV80UDFHa20w?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 23 Sep 2026 17:32:12 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
