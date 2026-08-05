# 每日股市熱門話題分析 - 2026-08-06

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜正向｜熱度 14｜市場確認 100.00｜同向 1/1
2. **AI 伺服器與資料中心**｜中性｜熱度 10｜市場確認 88.33｜同向 5/6
3. **半導體與晶片供應鏈**｜負向｜熱度 8｜市場確認 0.00｜同向 0/5
4. **綜合市場情緒**｜正向｜熱度 41｜市場確認 N/A｜同向 0/0
5. **新興題材：SpaceX**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.07（樣本 12）
- 5日相關係數：0.33（樣本 12）
- 同向比例：6/12

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 100.00 | 1/1 | 0 | +11.17% | +32.94% |
| AI 伺服器與資料中心 | 88.33 | 5/6 | 0 | +10.49% | +10.23% |
| 半導體與晶片供應鏈 | 0.00 | 0/5 | 3 | -6.29% | -14.27% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：SpaceX | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：DeepMind | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：南亞科7月營收 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 相關性偏弱；應提高同向價格確認權重，降低泛 AI、泛半導體等寬標籤推估權重。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-07-24 | -0.16 | 0.43 | +50.00% | 6 |
| 2026-07-25 | 0.30 | -0.06 | +12.50% | 16 |
| 2026-07-26 | 0.38 | 0.06 | +23.53% | 17 |
| 2026-07-27 | 0.54 | 0.11 | +37.50% | 8 |
| 2026-07-28 | 0.32 | 0.13 | +36.36% | 11 |
| 2026-07-29 | 0.16 | -0.03 | +92.31% | 13 |
| 2026-07-30 | 0.25 | 0.92 | +66.67% | 6 |
| 2026-07-31 | 0.10 | -0.10 | +46.15% | 13 |
| 2026-08-01 | 0.38 | 0.25 | +54.55% | 11 |
| 2026-08-02 | 0.06 | -0.21 | +33.33% | 9 |
| 2026-08-03 | 0.35 | -0.49 | +60.00% | 5 |
| 2026-08-04 | 0.05 | -0.08 | +46.15% | 13 |
| 2026-08-05 | -0.39 | 0.44 | +64.29% | 14 |
| 2026-08-06 | 0.07 | 0.33 | +50.00% | 12 |

## 歷史回測摘要

- 回測日期：2026-08-06
- 近5日 3日相關：0.06
- 近5日 5日相關：-0.06
- 同向比例：+37.50%
- 權重狀態：未調整

- 方向準確度：+37.50%
- 信心排序準確度：0.06
- 診斷：低相關

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

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits；MU, INTC, SNDK: Chip Stocks Rally After-Hours On AMD’s Blowout Report - Stocktwits；Is SK Hynix Quietly Winning the AI Memory Supercycle Against Micron and Sandisk? - The Motley Fool

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.48 | N/A | N/A | 893.19 | 971.00 | -8.01% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.48 | +11.17% | +32.94% | 1,350.50 | 2,335.00 | -42.16% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.42 | N/A | N/A | 482.05 | 516.10 | -6.60% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.42 | N/A | N/A | 101.06 | 114.68 | -11.88% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +9.56% | +9.85% | 219.22 | 219.22 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK、SanDisk」，共 5 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits](https://news.google.com/rss/articles/CBMi0AFBVV95cUxOWm5KdEIwSXpyY191UEhDa1V6NVpWa01UbmpJeWRIV0ttT080TmpDNEhISW5TWkQwUzBVYzBqSHJPWXRVNVJCampoWWRlYmhKVkhIeHBJLS0wLW5Ua09GQnRORXpFcW5qTEJkcnJGcW55aU5rOFVOLUFMbjRPZEpWT3A2ZllucnM0SU9JNEdrNUwyc3V2WHAtNFk3VHl4R1F6SkZRMFpleEE2Zl9MdW4tSEpMMnFGZ2hQZURWQ3B1WDlPR1BhRjJELVN5ODJWYVR3?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 05 Aug 2026 17:27:41 GMT
- [MU, INTC, SNDK: Chip Stocks Rally After-Hours On AMD’s Blowout Report - Stocktwits](https://news.google.com/rss/articles/CBMiygFBVV95cUxPeVlYaXJjQjNtTkNRQUxQTHhaLUFMbE80Uy1MeDBpV0FPdkg2SHRLdkdfVUpXM1NrNWhZSVZQQ01sa0o4T1hKdzF1clBFRlRWUmMwWGxQTDNVVFBpOVhObUc2MXpBeXBOZ0p3R0w5NGRNOHB4X0ZIXzhlT0NMbmhzc1RtdmJRTWhlRUhKSHpyVnpaU0VGMlJyU2tDcmdkTG1hWVJJbmtTVDREbzFfWDB4bjhuTGswN3lmdkdHQzY1dzFOVU41VGlBNlZn?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 05 Aug 2026 15:33:16 GMT
- [Is SK Hynix Quietly Winning the AI Memory Supercycle Against Micron and Sandisk? - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxQQnNVVDBsYnRhQ3dWLVlnbjRaN1VNME91VEhRU2xmQ3FjMExXbTRIUjF0eWRFMEJvaWtHeGFpeC1JWmszd21BRjRObUJ1RGtONm9lbm5NMmstMEkzY1Rwdk1aeGl3TGZfQTY5eG1IZHdFRWJ3cnZWX0ZaSHV4UjVZTEtGMUgyb1FfMEM2NVA1Y2NyLVh0cHJfMQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 05 Aug 2026 05:00:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel and AMD Soar 13%, Taiwan Semiconductor Rallies 7% as AI-Chip Stocks Bounce Hard - AOL.com；AMD leads AI chip stocks higher ahead of Q2 results - Seeking Alpha；生成式 AI 犯罪對資安防護有何啟示？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AMD 超微 | 新聞直接提及 | +0.57 | N/A | N/A | 482.05 | 516.10 | -6.60% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.54 | N/A | N/A | 101.06 | 114.68 | -11.88% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | +0.40 | -0.82% | +9.32% | 2,405.00 | 2,425.00 | -0.82% | 未明確 | 74.39 | N/A | 442.68B TWD / 67.87% | 2026-07-01 |
| NVDA 輝達 | 產業/供應鏈推估 | +0.06 | +9.56% | +9.85% | 219.22 | 219.22 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | +24.12% | -3.80% | 487.46 | 506.69 | -3.80% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.04 | +10.73% | +0.20% | 418.28 | 446.77 | -6.38% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.04 | +6.85% | +18.84% | 593.00 | 680.00 | -12.79% | 同向 | 10.86 | N/A | 65.78B TWD / 32.86% | 2026-07-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.04 | +12.52% | +26.98% | 4,000.00 | 4,310.00 | -7.19% | 同向 | 60.69 | N/A | 58.01B TWD / 2.80% | 2026-07-01 |

關聯理由（前 3）：
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。 方向判斷命中詞：升級。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：升級。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「Taiwan Semiconductor」，共 1 篇新聞命中。 同時符合主題標籤：AI, advanced packaging, CoWoS, AI server。 方向判斷命中詞：升級。

### 主要來源

- [Intel and AMD Soar 13%, Taiwan Semiconductor Rallies 7% as AI-Chip Stocks Bounce Hard - AOL.com](https://news.google.com/rss/articles/CBMid0FVX3lxTE41by1UUVByc3A0NEtzcGdBNFFHUnZqVWcwVjdqRjN2SzFQSzlMYW1sYVhqSUJEMGw1TWd5NkdGeEZoUWhsZkw3YXRHUElLa3d3MTduMHYtRE50WE55WmxvTXNKMTFFYjhHX2Q2blVFd2VsNmd2RUpZ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 05 Aug 2026 11:16:37 GMT
- [AMD leads AI chip stocks higher ahead of Q2 results - Seeking Alpha](https://news.google.com/rss/articles/CBMikwFBVV95cUxOTjR4UWRHSXNHM0g3Q2dBUWkwMmZYNllicTZPNEdna2tHTUw4R0RHcWdtUjNESURsazBJV1RoMURlQXhkbDA3eTdKTmxEVTlIZkJTYnAxbU9RNWdINDFzbXdFVVloaTlXRlJJdmlHSVFITUw4SEdsNUwwNE0yNlJ3QVpYN0JKbFlydjZESVdrVU91ak0?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 04 Aug 2026 15:19:38 GMT
- [生成式 AI 犯罪對資安防護有何啟示？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMipwFBVV95cUxPSlJDM0xjdmFrTU9obnlkUmNKNkFlM2h3NmNzUEdxdnFaQWItQ1hpXzFIUHdZckRuaW4zcTh0RENKbFhJZ3l5eF9QeW5UcFZMdVY1aVBvTUsxWHBzTDBrNEVaRGhocEt2STlfa1NDSjU3UEtVZWwweXNTZVA2cnVwWTVmaUZnbGhjWUM5TmsyWlR3U0N4T2Flel84Q3hVOWJ6Y2FrWmstSQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 05 Aug 2026 13:53:14 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel Soars 10%, AMD Jumps 8%, Broadcom Rises 6% as Chip Stocks Ride a Risk-On Rally - 24/7 Wall St.；Intel and AMD Soar 13%, Taiwan Semiconductor Rallies 7% as AI-Chip Stocks Bounce Hard - AOL.com；AMD leads AI chip stocks higher ahead of Q2 results - Seeking Alpha

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AMD 超微 | 新聞直接提及 | -0.57 | N/A | N/A | 482.05 | 516.10 | -6.60% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | -0.57 | N/A | N/A | 101.06 | 114.68 | -11.88% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | -0.43 | -0.82% | +9.32% | 2,405.00 | 2,425.00 | -0.82% | 未明確 | 74.39 | N/A | 442.68B TWD / 67.87% | 2026-07-01 |
| AVGO 博通 | 新聞直接提及 | -0.24 | +10.73% | +0.20% | 418.28 | 446.77 | -6.38% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2303 聯電 | 產業/供應鏈推估 | -0.04 | +0.83% | +19.02% | 122.00 | 164.50 | -25.84% | 未明確 | 6.68 | N/A | 23.12B TWD / 22.85% | 2026-07-01 |
| NVDA 輝達 | 產業/供應鏈推估 | -0.02 | +9.56% | +9.85% | 219.22 | 219.22 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | -0.04 | N/A | N/A | 893.19 | 971.00 | -8.01% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | -0.02 | +11.17% | +32.94% | 1,350.50 | 2,335.00 | -42.16% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- AMD：新聞直接提及「AMD」，共 3 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：risk, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：risk, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「Taiwan Semiconductor、台積電」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip, foundry。 方向判斷命中詞：risk, rally。

### 主要來源

- [Intel Soars 10%, AMD Jumps 8%, Broadcom Rises 6% as Chip Stocks Ride a Risk-On Rally - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiwAFBVV95cUxPd0NBY05teWNwSG9tcDRjYWlHcjMwdDNBOHFDb3NWb0VOc0VOT2pCUkNPMTVxMFRETVJjWVFJWm5aMEpyTVJvT3RxSThlejBaOS0tckdWMjNyVjJ1bUJFZUozN0J1VWxpQk1oZy1LWHZJOHk4NEhQakVaa21NV1lKMzFwTXBZYTFsQWRiYzJ3eFZkRGdhREdpZU1QSjdJdGM4SmVHQXhfWWkxcTR4UmZxeU1vRHBWcVBZTEVrSTBIY2c?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 04 Aug 2026 16:36:11 GMT
- [Intel and AMD Soar 13%, Taiwan Semiconductor Rallies 7% as AI-Chip Stocks Bounce Hard - AOL.com](https://news.google.com/rss/articles/CBMid0FVX3lxTE41by1UUVByc3A0NEtzcGdBNFFHUnZqVWcwVjdqRjN2SzFQSzlMYW1sYVhqSUJEMGw1TWd5NkdGeEZoUWhsZkw3YXRHUElLa3d3MTduMHYtRE50WE55WmxvTXNKMTFFYjhHX2Q2blVFd2VsNmd2RUpZ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 05 Aug 2026 11:16:37 GMT
- [AMD leads AI chip stocks higher ahead of Q2 results - Seeking Alpha](https://news.google.com/rss/articles/CBMikwFBVV95cUxOTjR4UWRHSXNHM0g3Q2dBUWkwMmZYNllicTZPNEdna2tHTUw4R0RHcWdtUjNESURsazBJV1RoMURlQXhkbDA3eTdKTmxEVTlIZkJTYnAxbU9RNWdINDFzbXdFVVloaTlXRlJJdmlHSVFITUw4SEdsNUwwNE0yNlJ3QVpYN0JKbFlydjZESVdrVU91ak0?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 04 Aug 2026 15:19:38 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：《台股盤後》量增收漲1250點、站上44K，收復月/季線- 新聞 - moneydj.com；野村：台股修正非關基本面，跌深布局契機浮現- 新聞 - moneydj.com；金管會推台股融資資訊儀表板拚9月底前推出- 新聞 - moneydj.com

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》量增收漲1250點、站上44K，收復月/季線- 新聞 - moneydj.com](https://news.google.com/rss/articles/CBMikgFBVV95cUxNS093eWhuWjB5NmVfQUxURENPM0poU2FmSDhQYnlVSXlpZk85X1JLc0VVTGJYbE81SzI5YlBkV2NNMzktRThUa3dxRU53ajFsR2RHQzl6MHhPZE5lQXFCY3dhLXJJcHBxRlQxV0ZidjY0RXBhY2V2alQwc2JiYkc2NmVkR09WcjFPdkxkZlptcWhYZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 05 Aug 2026 08:09:00 GMT
- [野村：台股修正非關基本面，跌深布局契機浮現- 新聞 - moneydj.com](https://news.google.com/rss/articles/CBMikgFBVV95cUxOUGItTjh6V0RTR1EyWkFHUURDRVVIWllUOWdPM3QxdkRXS3ZOZElpMDdwM2I3NDlPYTRIdExyWFdUMy1IWWlxMmRhVTZ2R0dLdFRYaFl1QVRnN0Y2VEpCTG43ZE5Oa0ljYzZxdXEtOS1ZTWdEaWoxa19OS05uaHhWNm1TRXl4WGZFTzI3emw0bzlIQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 05 Aug 2026 02:24:00 GMT
- [金管會推台股融資資訊儀表板拚9月底前推出- 新聞 - moneydj.com](https://news.google.com/rss/articles/CBMieEFVX3lxTFA4Y1d4TTVJeGZxTDZQTU1MRUtBb1g5b1c0Yk5wYlNzVXp1MThkR2czNlp2b3JGTVJqQnhlQlhrRVRkWkVodWlDemY2b192bGxLVmtJMFpraDNNcTRrdG1zUFloMkVMaUpkTG9mZm1sVUVxU2djb1RJYw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 05 Aug 2026 00:48:00 GMT

## 新興題材：SpaceX

摘要：新興題材：SpaceX 相關新聞集中在：SpaceX slides as AI spending worries overshadow early returns - Reuters；SpaceX attracts retail buyers after post-earnings share slide - Reuters

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [SpaceX slides as AI spending worries overshadow early returns - Reuters](https://news.google.com/rss/articles/CBMiuAFBVV95cUxQZWU1MzhJUmZkZWYwa0ItM3ZsMHh3bnVZS3JiYllKRF83UWpmM0d6M2txVnY3eDdNVXdweUd0dFZDcmxZQWE0MlBTYlFzYTg0dFJWODl6Z0hfcWo0QXZwNkN6Z3pXZGJKMlY3SGZQcmZzWmhxbmxvNDdISHR6V29ST2hUVW1FUGUxR2ZOVVM5OUR0THhTcmJ6UXRhTld1WXFjNkdXYkM2REs2V1BnZC11VlR0WS1pUFU4?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 05 Aug 2026 22:05:29 GMT
- [SpaceX attracts retail buyers after post-earnings share slide - Reuters](https://news.google.com/rss/articles/CBMivAFBVV95cUxOa1NSdU9aQnBlR0J4a2tHWnRKMkhBUW5lLUlxd0U5SWNEMHNLRkVHV2N2a0pHdE50aGhYZ1lNSUQtWWdJMmtKNHhpaEc2dnlQNnJBd0JHRHBGRk0wUjEwdThnSm9MS2QxNzdoU0RCamlBQ0JZOVVXQk5XX2dxQzdxNDlFRG5EdzF0akNVRHNZRGY2UldUM1R1WnZwdGxCQ2Fwa1o4b2xQZ2FxdzJ3YWc0Sl9QM21mQ1Jnb2NFbQ?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 05 Aug 2026 16:30:58 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：個股動態報導內容-639C8209-68F2-4CEE-81CA-7CC6793CF848 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-639C8209-68F2-4CEE-81CA-7CC6793CF848 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxQdmhhdkhZQXR4ejJnbU1ocGJoZkJLX0M2Vy1pLW5kOE1heVJZcTdwWVBpNEtTbnVRYmZmeVRpVWdOTXFIa01BTzg4TFF6clFWTlRicDJSdkM4TDIwRGVSSmdTS3UyY1ZaWHozU0JvUkVNSGhlWkw5cklKbV9pTHlCdXU5NUdmaFkxUGlLMWFRYnNTRFJp?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 05 Aug 2026 11:42:00 GMT

## 新興題材：DeepMind

摘要：新興題材：DeepMind 相關新聞集中在：Google shakes up AI leadership as DeepMind chief shifts role - Reuters；Google's AI reshuffle: Chief scientist Jeff Dean exits and Demis Hassabis steps down as DeepMind CEO - CNBC

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [Google shakes up AI leadership as DeepMind chief shifts role - Reuters](https://news.google.com/rss/articles/CBMipAFBVV95cUxQaHV5Q1dFcHFPLTJhTmkyTG05amxnbm1QQkRGYnpCZ0tON1FJVnJ2d0pBQVZENUlJYm01cXBoWFhvVENnbklRLVZoNndsMVpiWGNhNnJ6cEt6VFdKUGdRQ0xPem5kaHo3Y24tTlFqWGFtZGZjS25UbFl5UUMxTWtsWkVRLWQzOTZWbTViWXJXbFdIYUU0STdDcTliOEJCUEFrR0x0cQ?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 05 Aug 2026 21:42:10 GMT
- [Google's AI reshuffle: Chief scientist Jeff Dean exits and Demis Hassabis steps down as DeepMind CEO - CNBC](https://news.google.com/rss/articles/CBMiogFBVV95cUxPVkhiNlh6LVJaNmJiWXYwZm11TFRwS3JVWWVVVkRHdzlWeGhkSk04WXhnQ1R2QjhJNmU5VXdsd3FJSG81cGVlQTlJUUdIYThaSnczYU1XbE84N09ucXRPVXBhbnlkamtWV3JhVUpUZ2NMMDE2RkJhWG1pdXlSRzljSTA0eXhRdHEybUpvOEZXcGJWQzJKWndPREFCZlBXNGZqVWfSAacBQVVfeXFMTmpLM184R3JUZkd3THZNMVEwalh2LURjVDFwMFlSSEt3eVMtV2VCVVhpTF9aSjhiT0twYVFaZi15TW9yXzFEMGpIdjIwMWZTaFJKVjZmeFB5dG43dUlhX0QwYUQzbzVvdnFnX0pfaU4yYzA4OFFZM205LVd5WDNMejBWbWdHVnA2MHVIYW5JZHdZZFQzZDdqWFZpazV2LUxpS0Z2UlFWRUU?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 05 Aug 2026 16:03:12 GMT

## 新興題材：南亞科7月營收

摘要：新興題材：南亞科7月營收 相關新聞集中在：南亞科7月營收月增近5成！網驚「記憶體現在是在印鈔票嗎」公司揭原因 - Yahoo股市；續創新高！南亞科7月營收年增逾7倍 網驚「記憶體現在是在印鈔票嗎」 - Yahoo股市

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [南亞科7月營收月增近5成！網驚「記憶體現在是在印鈔票嗎」公司揭原因 - Yahoo股市](https://news.google.com/rss/articles/CBMi0gNBVV95cUxOZEJMajdVNDlCRzZ0VC11MUpjWHpnanRoZ0U5X0hlU256YjVZTkxPNlFIMnZvd3BhTnZlbER4cjlNTVJXR1pRQVJNSEkycGUxMmd4aUpxbXpPdVZ6Y1YwZWNpRGFHNkk3X1lOSnFRLTRmNWhWbHN1M1dfZzFSR1lQNnBZZXI5RkVoS3QybG5jOE41cjZXRVR2ekhNcWtkWWhraWhSb2FtSTdUa0h4ZklQU3BrNE5VTXpPWUZ1a0M2TjlnMG82TTFXTEkwNWxfSUVqb1paSGFVRS1VNThuZTBETGx4R29zWk5wWmU3QXYyRG1tWTVlT01vZ0FZYVc5R2J1UW9EMW10R0RNTlhWZU1XUUp0UjEyOFduVVBlVU53X3pCX3dxUVpyLU1xN2YwNTQ2NVJhM1h1bHBFa1Z6SGg0dFNXMFNRbzNwOGFtVUVyckE3QmhRS3VsMGsxTnFvSkh6NDdITUJZdDBTNHN3RjBVS25SWjVlbERkYW1zaUpQeUxqT2cwNHZfNjdoTFJwVS1ISG5IOWhISTljdUdMV3pNVXQ5N2JKQ2UzdW5sdEZ4ZTJtRmJpYzVJR2NMZndEamdMMk1WVldyNzA2V2pSU3FOLUl3?oc=5) - Google News source discovery | Yahoo 奇摩股市 Wed, 05 Aug 2026 08:56:23 GMT
- [續創新高！南亞科7月營收年增逾7倍 網驚「記憶體現在是在印鈔票嗎」 - Yahoo股市](https://news.google.com/rss/articles/CBMixwNBVV95cUxObmk4SHhVcFRULWVNODBSTnNwai1zT3pXbFR1TnVXMTI3M3hEVGExZEMxVy1OeGhMRjBFWkJYVFB3dVZSclp5c3paNFJKV0I5Z0ViLUpNYnpsc1FUSlREdmhXdy1ITGxHWGhJeG0zbk5IWWRkTXRJS1lTQnFPei1VdjdhQnR3dmNqUGVzVm91LWV4cFliVUVoaGt6R0F4OV9UeTc0T3R0Nno2NGRJUkI5MmF3U0E1ZlFzcGZET2Q0Q0FwdHQ5RGRGMnpYQ3JCSmYyWUlaUkhLZmE1TVdacDcyVkI2cDJ1dDk5MGZueHdsMmV3OXpjZG1WZUxUaGN0dnBwLVR3aF96cUtDVXYya2lHRE9uMk01ejVPemxFdG9zWXlzWFVmNF85bm1iRHJMYWdGNXE3OUJZZU16amZsOXhmaVJrVVlfTjJWYUN5SVJDelhmTUVucGpNeHdUS1B5UGFZNWdSN0pBRHFxX29GN0dIWTR0dG1mRmg0X1cxTm5TZG9KUGZxV2VWSWdEaHJNdjhKNUVFYnZBVXQ3NldLTVV4bkRLWEt4ZjAtRTM2dmRRalhiY0dValBJWnVVdTBkUEcwZUtwWWMwbw?oc=5) - Google News source discovery | Yahoo 奇摩股市 Tue, 04 Aug 2026 09:00:14 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
- TWSE PER/PBR 抓取失敗：Expecting value: line 1 column 1 (char 0)
