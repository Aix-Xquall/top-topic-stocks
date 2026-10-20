# 每日股市熱門話題分析 - 2026-10-20

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **半導體與晶片供應鏈**｜負向｜熱度 7｜市場確認 82.32｜同向 7/8
2. **AI 伺服器與資料中心**｜中性｜熱度 17｜市場確認 N/A｜同向 0/0
3. **散熱與液冷供應鏈**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0
4. **新興題材：TradingKey**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
5. **記憶體與 HBM 供應鏈**｜正向｜熱度 11｜市場確認 38.63｜同向 2/4

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.09（樣本 13）
- 5日相關係數：-0.81（樣本 7）
- 同向比例：9/13

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 半導體與晶片供應鏈 | 82.32 | 7/8 | 1 | +7.02% | +7.03% |
| AI 伺服器與資料中心 | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：TradingKey | N/A | 0/0 | 0 | N/A | N/A |
| 記憶體與 HBM 供應鏈 | 38.63 | 2/4 | 2 | +1.21% | -17.86% |
| 新興題材：AI散熱 | 0.00 | 0/1 | 0 | -0.15% | +1.92% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 相關性偏弱；應提高同向價格確認權重，降低泛 AI、泛半導體等寬標籤推估權重。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-10-07 | 0.48 | 0.61 | +73.33% | 15 |
| 2026-10-08 | 0.13 | 0.40 | +58.33% | 12 |
| 2026-10-09 | -0.03 | 0.37 | +38.89% | 18 |
| 2026-10-10 | -0.28 | -0.96 | +57.14% | 7 |
| 2026-10-11 | 0.66 | -0.74 | +40.00% | 5 |
| 2026-10-12 | -0.08 | -0.07 | +41.67% | 12 |
| 2026-10-13 | -0.05 | -0.03 | +46.67% | 15 |
| 2026-10-14 | 0.08 | -0.29 | +57.14% | 14 |
| 2026-10-15 | -0.08 | 0.08 | +33.33% | 12 |
| 2026-10-16 | -0.13 | -0.25 | +64.00% | 25 |
| 2026-10-17 | -0.10 | 0.49 | +26.32% | 19 |
| 2026-10-18 | -0.12 | 0.33 | +21.74% | 23 |
| 2026-10-19 | 0.44 | 0.36 | +50.00% | 12 |
| 2026-10-20 | 0.09 | -0.81 | +69.23% | 13 |

## 歷史回測摘要

- 回測日期：2026-10-20
- 近5日 3日相關：0.30
- 近5日 5日相關：0.47
- 同向比例：+40.00%
- 權重狀態：未調整

- 方向準確度：+40.00%
- 信心排序準確度：0.30
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

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel, AMD and Nvidia Lead Chip Stocks Rebound After Brutal Selloff - TradingView；AMD vs. Intel: Which Chip Stock Is a Better Investment Option? - TOP1markets；高盛建議對沖台灣半導體 AI族群股價恐再跌15％ - 工商時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.57 | -19.75% | N/A | 92.03 | 114.68 | -19.75% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.28 | +4.25% | N/A | 538.05 | 538.05 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | -0.49 | -1.67% | +8.50% | 217.09 | 228.38 | -4.94% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.05 | -2.81% | -4.72% | 2,420.00 | 2,480.00 | -2.42% | 同向 | 86.28 | 28.05 | 511.86B TWD / 54.65% | 2026-10-01 |
| 2303 聯電 | 產業/供應鏈推估 | -0.05 | -7.39% | -9.62% | 131.50 | 164.50 | -20.06% | 同向 | 6.68 | 19.77 | 25.35B TWD / 27.22% | 2026-10-01 |
| MU 美光 | 產業/供應鏈推估 | -0.04 | -6.81% | N/A | 904.90 | 971.00 | -6.81% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | -0.04 | -12.35% | -17.86% | 1,299.30 | 2,335.00 | -44.36% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -9.65% | -11.43% | 334.59 | 446.77 | -25.11% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel, AMD and Nvidia Lead Chip Stocks Rebound After Brutal Selloff - TradingView](https://news.google.com/rss/articles/CBMixAFBVV95cUxNMW1QWXlTMjF3ZGpwYUpBYk96YVJfSHJ4RUhDR01KM0ZxVUV4X056ZFpjNUFRVUdoRWIzR1JVaUZudjVrRFNiLURlUmM1YnhEQW9qdGlhZkFnMGJYdm9LcFkxaC1VUE11OGNuSWdyS0djTkw0UWloMXpGLWgtSUdMbkFWX0xoTXJVY0Zhd2laU0lnVnVoTzBGUlEzOVNSSlRRYjNxVXhDNVBiaDZCd281ZWlyajJUWmZVTFBQNnAtTTh4MU1s?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 19 Oct 2026 19:49:07 GMT
- [AMD vs. Intel: Which Chip Stock Is a Better Investment Option? - TOP1markets](https://news.google.com/rss/articles/CBMie0FVX3lxTE5DWmNWWlh0V1ltcmZJcjRpbDZWU0J3ZXl4bE9zRGNOYkFveGJPNlYxVFRVWWtaN3NLTG5ReGpRYUxSWThpcmc3UHlmVVY4NjJvSEV0QXNUZ1hEZ1RMS3FaRHhmRWJVazJLbFZIVHZ3X2huY0JwanFwYmV1Yw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 19 Oct 2026 07:50:11 GMT
- [高盛建議對沖台灣半導體 AI族群股價恐再跌15％ - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9PbHE4NXJyX3U5aDVOR2l6Y0I2dHZQbjA0WHFJVWY2bzU2VnpaeVNqcTg2TFJ5NktGQjNLbzZlb1djbDk1NXdjdFhGbVJzd2hWd3U0UnlZVVpDQ0pUa0Vj?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 19 Oct 2026 14:16:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：10月20日盤前／台股回測季線築底 市場關注 AI 投資變現能力 - 經濟日報；軟硬體整合治理，能否化解各國 AI 監管疑慮？ - TechNews 科技新報；成果導向計價模式如何影響醫療 AI 普及？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | -19.75% | N/A | 92.03 | 114.68 | -19.75% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -1.67% | +8.50% | 217.09 | 228.38 | -4.94% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | +4.25% | N/A | 538.05 | 538.05 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -2.81% | -4.72% | 2,420.00 | 2,480.00 | -2.42% | 不適用 | 86.28 | 28.05 | 511.86B TWD / 54.65% | 2026-10-01 |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +18.50% | +8.44% | 533.52 | 533.52 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -9.65% | -11.43% | 334.59 | 446.77 | -25.11% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | -10.31% | -12.07% | 670.00 | 703.00 | -4.69% | 不適用 | 13.92 | 48.48 | 88.13B TWD / 45.52% | 2026-10-01 |
| 2454 聯發科 | 產業/供應鏈推估 | 0.00 | -6.03% | -9.08% | 4,205.00 | 4,920.00 | -14.53% | 不適用 | 60.69 | 69.45 | 55.40B TWD / 1.97% | 2026-10-01 |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [10月20日盤前／台股回測季線築底 市場關注 AI 投資變現能力 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE45T1FJNTZUd09TalhfYXhTdUtrOWlGUTFRb3lCTnpVWnpDVmVuR2lKQ2ExVzNHT0otYzN2UlRGYWtCeFhHMUUxM0RuLWpGaFFvRDBWN2lKYUVOUdIBX0FVX3lxTE13R011Q0d2b0UzWlYwUHhsWHZ6ekpoNTVCLUU4aFNLQXAySlRpd3hDT3ItMncwOE1zT0pzdW9kOTJzellWY0pfRHhZNTFVNUctVGlCSjJsRUN0a01UVVRJ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 20 Oct 2026 00:21:31 GMT
- [軟硬體整合治理，能否化解各國 AI 監管疑慮？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMihgFBVV95cUxNa011N2hVUF9ZbU5uelRQeEFLcXNoNjJwWU85SU1zeGJ6SXlLOWtzYkR3WFc3NVNEek9uOUtfZko1d2xzQlB3aXEtYWliNTlxV1YyT21wdDlxTkRIazZldG1veEtFSGJxVHRWSGFJNWlaenhMbFBKU0RFVDJ2VmFhdl9aS25zUQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 19 Oct 2026 22:50:07 GMT
- [成果導向計價模式如何影響醫療 AI 普及？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiggFBVV95cUxNb1VmTWVpVmlBM2gtSjNOWnpxRmtlOUNnc2xGTUEtMUhxc0NwYm9GRDluSDRMTkE2THlDeHFJT0xDdHh5eEhPczlGY01ad3ROa25ZdG1IZWhhSFBBdWIyUUo5bGZ1cmhfSUlLQVFOQ0x3YXNCbG1JY3JkTVAwUGFoR3Zn?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 19 Oct 2026 22:45:40 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報；散熱股又有大消息？花旗喊買奇鋐、雙鴻 目標價齊升逾14% - 經濟日報；偉詮電Q3營收創高，伺服器散熱續看增- 新聞 - MoneyDJ

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | +0.15% | -1.92% | 3,320.00 | 3,435.00 | -3.35% | 不適用 | 75.13 | 44.25 | 21.02B TWD / 44.92% | 2026-10-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱、奇鋐」，共 3 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：跌停, 創高。

### 主要來源

- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 19 Oct 2026 06:50:28 GMT
- [散熱股又有大消息？花旗喊買奇鋐、雙鴻 目標價齊升逾14% - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE04UXU3RGRUUnBBVElIbVBGZWozMUxfTzNsbE50ejYzRE1pUTJBQ0FNWS03VjRSYlZrUWkzSXhuNHhFQl9teWs5YTJ4QUU4ck1MZ0NneEk3XzF3UdIBX0FVX3lxTE5tclh3dXNNWDhDMnNiYmMyRW1DRFJwZUt6ZlZXMmdEYlhoQU9VR1pSeTVrVUpVT2FWOE1idEkxdXRhYTYyYVpMcnRwaWQ4NGpmRUNTREJUQ2UwNU01N0pF?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 18 Oct 2026 09:00:00 GMT
- [偉詮電Q3營收創高，伺服器散熱續看增- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPRnN1Y3FRZVBhdnRYQ2tQRXBqYjRBbVRoaWRBcm5scGJ4UllYSGlScTJEdld4emhYaFFldGxoQlNidjlFOEliT0pNUUhsWEw0cmxIdW5HRWxCRlFYekF2SjBscEk2dk9wdmtubEdObm9BNGVyQVZTOG1LclFpa0pnRVZ2cmxXSXlyY0RWRWpfNGlHZw?oc=5) - Google News source discovery | MoneyDJ Mon, 19 Oct 2026 04:39:00 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：US Storage Stocks Rebound Pre-Market as Micron, SanDisk, Western Digital, and Seagate Gain - TradingKey；Micron vs. SanDisk: As Storage Sector Drops Broadly, Which Is the Better Long-Term Investment? - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | -6.81% | N/A | 904.90 | 971.00 | -6.81% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | -12.35% | -17.86% | 1,299.30 | 2,335.00 | -44.36% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。

### 主要來源

- [US Storage Stocks Rebound Pre-Market as Micron, SanDisk, Western Digital, and Seagate Gain - TradingKey](https://news.google.com/rss/articles/CBMiwwFBVV95cUxNNU9zTjJJV1BkaE1ZZS1FWDF5QUdoYXdETTQtN21LVGEtQWkzVGNMamRzN3VCMmsyeFhjU1J2VWYyVW9IbEdZSGx3SjhnZ3FuNTJNRGVfTVo3MHE5b1ZHeDhDY1dhcS1qRDZ6OVI2UzdIZVVDRWJLUEk1V01LRG5ZWnR0R2QwNmI2UUZ0Q0ZHajNmSmI3ZUl5ZmkwOWE3RGU3LWcxa25SQlB4MEpHSXpNNnNwWC1BMzgwVG56SUJua1pqeGc?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 19 Oct 2026 09:28:50 GMT
- [Micron vs. SanDisk: As Storage Sector Drops Broadly, Which Is the Better Long-Term Investment? - TradingKey](https://news.google.com/rss/articles/CBMirwFBVV95cUxPRExCekw1bi01clVWX000RDFNOGpNOEVTVm13SDE3NDdBTUFUOURwS09tYkhtcE9fQTNiTUk4bDd2WmtWRnhlZkQ0NlJWWnV3UklmSGcwVnhSTjNOTmV6ci1FTW42Y1hjMVhoZXFfVUpGWHVOYU1tVGVlUFk2ZUR1SXhNRVV4a3Nia3JrbjFBWUZxdlptVUR3VjN5V2x5ZGFiVi1lTTJJQUFuX2l1LWsw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 18 Oct 2026 02:08:15 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：INTC, AMD, MU, SNDK: US Chip Stocks Rebound After Worst Week Since March - Stocktwits；Micron, Intel lead chip recovery, adding nearly $250B as most of Wall Street falls: Chart of the Day - Yahoo Finance；Memory Stocks Rally as Tech Selloff Unwinds: Micron Climbs 4%, Sandisk Jumps 7%, SK Hynix Rises 5% - 24/7 Wall St.

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.28 | -6.81% | N/A | 904.90 | 971.00 | -6.81% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.28 | -12.35% | -17.86% | 1,299.30 | 2,335.00 | -44.36% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | -0.49 | -19.75% | N/A | 92.03 | 114.68 | -19.75% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.42 | +4.25% | N/A | 538.05 | 538.05 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -1.67% | +8.50% | 217.09 | 228.38 | -4.94% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：falls, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK、SanDisk」，共 5 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- INTC：新聞直接提及「INTC、Intel」，共 2 篇新聞命中。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [INTC, AMD, MU, SNDK: US Chip Stocks Rebound After Worst Week Since March - Stocktwits](https://news.google.com/rss/articles/CBMizAFBVV95cUxNM2ZLdF9kOWJhRmFyWWIxWXVWVmxPaXdQR3lSbGJMXzhoMHNfbVB2a2VDVlNBSkwtTGRTZVZ4X19wWUp1bmZNdmFFN2UyUmYxSkprYVpDVmhsMF9mTnhWQms0U2ROQ0owR3BmNmIxRjFYWk5JRHFIYjF2WlpwakpnZTU0eGpqcTNncW14dzNTUEVXMDNPU2VDV2tqTkJsbkFkTUlXdG1QUWQxNXhLbU5EQUZLVFVraEF1akZtUVFiWElwQmZWcGVraklveng?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 19 Oct 2026 04:56:18 GMT
- [Micron, Intel lead chip recovery, adding nearly $250B as most of Wall Street falls: Chart of the Day - Yahoo Finance](https://news.google.com/rss/articles/CBMi6AFBVV95cUxNT0Z3eDRfMlBlWFBxNzA0U2V4Tzc3OURubzBkWGNVb3prRFp1MVlZNjhZZUExWHhTbFJoRV9FUnprSEVsYTdsZ0w4YU5uSy1qMnp3cDZNckJrSWZwMTVZN0tLUVFSTjc2T3Z0bFR0THdRbkxidElYX0drR0tKVFVhSUdYX1NGQTJXV1FHX3ZDZ2NvaXludE9BVUxwa2J3N2tsRGE0WXlhYTRDb0oxNkFPZHpLeUozNkQ1cTViR1daNUtJWW13cThLbUJRRjlOSEtwanl2TmdLMVFrellyMGplVEFnUV9hd1lw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 19 Oct 2026 14:43:02 GMT
- [Memory Stocks Rally as Tech Selloff Unwinds: Micron Climbs 4%, Sandisk Jumps 7%, SK Hynix Rises 5% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi0gFBVV95cUxQN19kYkI0VTV6ZVd3XzN2WnZTYTJFZmxnZExfYUU1eXJ1azRBYTV2eXd1NkVzWXNqaVplSVM3M0V6blJRaWJaYWdYUGY2Y2hYanRxT3FBNlgtdDFFelJ6UWlqV3MzUlcwYjdFYlE3Z2owNTN1dFlXaVVpeDdodEFHUXdVak5XQ21RR04zWWFCajZqTERScVZ2MTNHdEZBMFBoM0MyZE1PQTAtMkFwdmhIeXBoR1VUa3JpTVdfTWFkSFgxSmYzV0VEWGhIVHh5OWFQckE?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 19 Oct 2026 14:59:00 GMT

## 新興題材：AI散熱

摘要：新興題材：AI散熱 相關新聞集中在：焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | -0.32 | +0.15% | -1.92% | 3,320.00 | 3,435.00 | -3.35% | 未明確 | 75.13 | 44.25 | 21.02B TWD / 44.92% | 2026-10-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 1 篇新聞命中。 方向判斷命中詞：跌停。

### 主要來源

- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 19 Oct 2026 06:50:28 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：00881等七檔台股商品換股名單一次看 10月20日起生效 - 經濟日報；國家隊救援 台股拚反彈 法人研判探底危機已過 - 經濟日報；誰是台股的璞玉？近400檔一次看 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [00881等七檔台股商品換股名單一次看 10月20日起生效 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1HRVpFQVAweVUwLU5RYW1RdnprZnVQUU4tRjkyRzVTazZCOV9SeHhtNWdjZUNycVJqWkhFdEJQSWZUcmhFWDA5S3FBRkpLc240VmprclVoSnFXd9IBX0FVX3lxTFA4bmFpZ2hvV1I4VHdaZnAtbDI2VHJ4TVZzOVd5bmlRS3Z3RXJjdks2Qk1RU3ZZR0JzdkI3b3E3UUJRWlNma3hoU3E4b2RpR29hMlR6dHFxZG8wS3pKV3g4?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 19 Oct 2026 06:00:00 GMT
- [國家隊救援 台股拚反彈 法人研判探底危機已過 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5RMVFuZGJkRm5wNkczMEF4Tkt5aVcxVlQ2ZTBCQlZZSDFCV3h4NExHQUdtSHpoUEJFSzQxTWFELUZYS0JETkdFZ2hXU2lXbE94bjNQeWhVc0VEd9IBX0FVX3lxTE5lZjJtNnRhRDh0QTUzRTg4Y2E5UlVuUGdHUkV5WmliVi1pdkFTRGlHSDBWRk41S2xMSm16N3dNTUI5N2lpSmZicm5tZk85LTJpcjZDYU85NG0wM3FqeVN3?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 19 Oct 2026 18:22:15 GMT
- [誰是台股的璞玉？近400檔一次看 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBkOV9ObDJMN25BckRjcXhpZ1FzcjRGX0hsMHY1UThGYjNwQkNkTkEyWWJESENmRXJ0aTNMXzJFYXRwTWZScE1mNjRBeER6RjVYR2RFbnY5UDhDUdIBX0FVX3lxTE9BRXhWdEJpZERjTHl3LXZUellpX0tqdXVOdmZ1S2J5VFlyeG9mZTlLNVFUUF9PemRwc0RZQlREand6eHlLUGlHMm11QnRieVhpTTFTS3JUSUdVeDNRYU1V?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 19 Oct 2026 09:31:05 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》量縮收跌289點，守住季線- 新聞 - MoneyDJ；台股祭限空令？彭金隆：尊重市場機制- 新聞 - MoneyDJ；個股動態報導內容-B02A1CE0-5D07-4044-9DCE-5E59B0A650F0 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》量縮收跌289點，守住季線- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxOczRjNHVtbk9kR2V2VXdlZXBvV193RnNucTNHWlZhVGJsb3RUOGR2M3dsUXVoNDZISkRSVkk0Tll0VWx6emFhbTZpZ1NDYU1wZHM1dE5PRllZNTNuWDlCVFJJSW5mT3F0Vk4taE9PY0poOGloZDFzaGktNUhIWmNVeVlwMHFHZ0ItVEZuVW1HS0U5dw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 19 Oct 2026 07:39:00 GMT
- [台股祭限空令？彭金隆：尊重市場機制- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQV2hYN3FqQXIza1hCdnhpemtyS05rNGFtQ0YxOFpDcUhmeHA3dkV4QnNaZ3JsTVN3ZjYybW9Cei1KZkFYaFZtMEVweXItV1BjTlRkMmNrMVhtOXc4eVk4MUR6NWFWSmtGNnZHdThtbW0tSG5QOEdyNklEamJXM0U5bmF0T3JHUW9XNXlhaWNKelhiQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 19 Oct 2026 05:06:00 GMT
- [個股動態報導內容-B02A1CE0-5D07-4044-9DCE-5E59B0A650F0 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxQallNX09OWDQ0eVRSQ0ZzZlZMRl9EbzZsMXQ2MHNISE42bV9aUDk0YlRnTjBWclBvV1hwQ0hyaF8xaGpUXzEzdG5YOFZGWEZyelJYdEdYbEhtMzI2djZhczlYNmpVZTVHZU1VZ24xQVg4dGw1UmZQZHh1WTlad25yYzM2cVRiLXdiMzZ4YkNDQklUb19K?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 19 Oct 2026 12:04:34 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
