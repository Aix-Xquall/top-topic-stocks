# 每日股市熱門話題分析 - 2026-09-16

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **新興題材：MoneyDJ**｜中性｜熱度 11｜市場確認 N/A｜同向 0/0
2. **AI 伺服器與資料中心**｜負向｜熱度 17｜市場確認 51.15｜同向 5/8
3. **散熱與液冷供應鏈**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
4. **記憶體與 HBM 供應鏈**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
5. **新興題材：OpenAI**｜中性｜熱度 5｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.19（樣本 9）
- 5日相關係數：-0.46（樣本 6）
- 同向比例：5/9

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 51.15 | 5/8 | 3 | +2.47% | +1.89% |
| 散熱與液冷供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 記憶體與 HBM 供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：OpenAI | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MarketBeat | 0.00 | 0/1 | 1 | -15.29% | N/A |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-09-03 | 0.10 | -0.10 | +54.55% | 11 |
| 2026-09-04 | -0.08 | -0.08 | +28.57% | 7 |
| 2026-09-05 | 0.13 | 0.34 | +54.17% | 24 |
| 2026-09-06 | 0.19 | 0.43 | +50.00% | 24 |
| 2026-09-07 | -0.15 | -0.09 | +53.33% | 15 |
| 2026-09-08 | -0.07 | 0.18 | +57.89% | 19 |
| 2026-09-09 | -0.28 | -0.12 | +54.17% | 24 |
| 2026-09-10 | 0.28 | 0.86 | +75.00% | 4 |
| 2026-09-11 | -0.01 | -0.08 | +25.00% | 12 |
| 2026-09-12 | -0.39 | 0.04 | +25.00% | 20 |
| 2026-09-13 | -0.42 | -0.14 | +17.65% | 17 |
| 2026-09-14 | -0.31 | -0.54 | +33.33% | 15 |
| 2026-09-15 | -0.04 | -0.42 | +68.75% | 16 |
| 2026-09-16 | -0.19 | -0.46 | +55.56% | 9 |

## 歷史回測摘要

- 回測日期：2026-09-16
- 近5日 3日相關：-0.15
- 近5日 5日相關：-0.15
- 同向比例：+37.50%
- 權重狀態：未調整

- 方向準確度：+37.50%
- 信心排序準確度：-0.15
- 診斷：方向與信心皆需修正

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

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》量縮僅六千億、跌351點，日K連四黑-新聞內容-基金 - MoneyDJ；費半挫近6%、台積電ADR跌3.52% 台股估震盪- 新聞 - MoneyDJ；紅海航線遭威脅 沙國石油供應面臨雙重瓶頸-台股 - MoneyDJ

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | 0.00 | -2.65% | -3.44% | 2,385.00 | 2,425.00 | -1.65% | 不適用 | 86.28 | 27.65 | 514.81B TWD / 53.32% | 2026-09-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。

### 主要來源

- [《台股盤後》量縮僅六千億、跌351點，日K連四黑-新聞內容-基金 - MoneyDJ](https://news.google.com/rss/articles/CBMikwFBVV95cUxQUDY0MWVYWW9uRDQ5c2NxNzFoVFNGVEZjZGY2TXZ0RzlEeWwwbVZiQ2U3V1pReFdLSVVacEJzaXRpb0duN3RybGVlejA5U2JXbTZTQ3lwN2xvYU1pSy1qV0tFdm10ejZPOVdjRTFmOFNtRHpKbG56aG5QRHhDQS1oWEhKbE05b3I4NFBESHJTbWhFeXM?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 15 Sep 2026 08:02:00 GMT
- [費半挫近6%、台積電ADR跌3.52% 台股估震盪- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNZk90UG9DUE53Rzl6U2lUVUU4SlJaRHJ4cVJRcWxhM0VyMUlfaDVrS0hBUXU0MVYxLUgtVUZNV1cyaXc4QjdRQ0RpeU9WZndqVEJBVzg3SE5tUXdSTDRmTEdBQ2N4T3BrSl8yWTMtNjRNbzVYb1VTbGFnUTV5bnJaMFhSX2hCY2lZSmZrQVEyejFrUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 15 Sep 2026 01:41:00 GMT
- [紅海航線遭威脅 沙國石油供應面臨雙重瓶頸-台股 - MoneyDJ](https://news.google.com/rss/articles/CBMiigFBVV95cUxNenFMUlp1TnBJRm1QREtrMGRnWHhxakc2X3o5TzJpSUlFdTFUVzJuSlNfZC1XWWIyRW43RTZIb3RITTVnLWhGbkRHLXFwTTFFZ3JJOE1welp4WVB0STBsWTNYS1p1OWR0NVlxV3prU0s1cTBWTW5QMENTc0tjTERiNlZxaVhlbm54blE?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 15 Sep 2026 23:15:47 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Prediction: AMD Could Be Closing the Gap in the AI Chip Race - 24/7 Wall St.；Did AI Slowdown Calls Just Shift Intel's (INTC) Investment Narrative? - simplywall.st；讓 AI 對話不再尷尬，蘋果前研究員創辦 Nuance 打造更自然、無延遲的影音 AI 模型 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.54 | -15.29% | N/A | 97.14 | 114.68 | -15.29% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.53 | -2.31% | N/A | 504.20 | 516.13 | -2.31% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | -0.53 | -2.65% | -3.44% | 2,385.00 | 2,425.00 | -1.65% | 同向 | 86.28 | 27.65 | 514.81B TWD / 53.32% | 2026-09-01 |
| AAPL 蘋果 | 新聞直接提及 | -0.21 | +6.18% | +18.82% | 331.34 | 332.27 | -0.28% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | -0.03 | +5.69% | +0.49% | 212.17 | 220.78 | -3.90% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 產業/供應鏈推估 | -0.02 | +10.41% | +1.04% | 497.12 | 507.29 | -2.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -12.85% | -24.06% | 339.27 | 446.77 | -24.06% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.04 | -8.92% | -4.21% | 592.00 | 680.00 | -12.94% | 同向 | 13.92 | 42.84 | 82.25B TWD / 45.66% | 2026-09-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：slowdown。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。 方向判斷命中詞：slowdown。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 同時符合主題標籤：AI, advanced packaging, CoWoS, AI server。 方向判斷命中詞：slowdown。

### 主要來源

- [Prediction: AMD Could Be Closing the Gap in the AI Chip Race - 24/7 Wall St.](https://news.google.com/rss/articles/CBMipgFBVV95cUxPeFZYaUd5UEhkTGpXSlo5eWpwZVc5WTl2ZVBnMG1zb1d1TWoxanFrcUVIV2tlSDg3bXd0ZGpxLVE3czdLZFJ4emJFb1Z1U3J0YzFKYTBkVmV6TExaMnZUempnNkRiaTd6SWg1MUJmNUlMZlMxOWJVN08tWlg2TVlISk1SRzFWVEFFRDB2Ty1jWWtTZlFlbUxPXy04NFd4aGtwQ0Z3MFp3?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 15 Sep 2026 17:00:00 GMT
- [Did AI Slowdown Calls Just Shift Intel's (INTC) Investment Narrative? - simplywall.st](https://news.google.com/rss/articles/CBMiygFBVV95cUxNakJZbUFyUjVHQjJ6WnBieFdVdHNkWGJKYjJzc0c1aVlQYjRpRVREOXRIdm1GeVRpLTczX3FYbEVuNWpRNUNuZDVSc3pIb050SXB5ZlJDSEFQVlFLSk5GVWxOaGl3dkRwdGV4ejFYU0g3b0t0NlZnaEswVUdYNVhZYUM5SjJKbFluZ0E0MmVWcG1rU1NuZnB3c1pHU0Z4SDhqYlgxNk5IcmM4eUtqVnJvam1NbTBKeVctSUdRUzJfeFRlUkFKNHlPSU930gHPAUFVX3lxTFA2TGgyeTJvSm9waExBN0tBMXVtbEE0aVdGcUpFeHpxYnJKaHFjV3k4b2F6YWhZcHNNSldTZXZxTl9QWlVwaWxxXzFSRjVJcThXRWdrZU1KZ2VMX2xwZEx2cllKR1dLWno3STlOemw5SnJWZ1NwZ0w3YU5WRUtSejdSbXVNbmx6NENLbHB3eG9ZUXNKNkk2cHZub3pFbkRvNmFYLW9TZHN1REszR3d0MXNQcExQckJia2R0UmhZRFZOekIzTXpmS2NSTmYtaUtaOA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 15 Sep 2026 17:45:54 GMT
- [讓 AI 對話不再尷尬，蘋果前研究員創辦 Nuance 打造更自然、無延遲的影音 AI 模型 - TechNews 科技新報](https://news.google.com/rss/articles/CBMingFBVV95cUxORWJLdVF0NzJXSTA1UVp1QzhNRkRRU1kwdVdLd0pGSVdXdEtlY043R3I5WERIaXk1U0QtWjRQRXF0cXptWHIyNU5iU2x5aHgxWVpHWTJsSnBLd2JCSG1KNmtmcDR2NjZpaE5TdzlhakNhRG5rNEFtWlFneHZjeWFING1zVTBrNWFWdWNEU2hnXzNEQnlIM3ZqVDhGbnc4UQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 15 Sep 2026 23:40:49 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：輝達Rubin+ASIC專案雙引擎點火！ 「散熱大廠」8月營收改寫新高 iPhone新機助攻營運、目標價衝4005元 - Yahoo股市；散熱需求強 奇鋐、雙鴻H2營運旺 - 中時新聞網

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | -9.97% | -5.18% | 3,115.00 | 3,425.00 | -9.05% | 不適用 | 75.13 | 41.52 | 19.48B TWD / 54.34% | 2026-09-01 |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +5.69% | +0.49% | 212.17 | 220.78 | -3.90% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱、奇鋐」，共 2 篇新聞命中。 同時符合主題標籤：thermal。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [輝達Rubin+ASIC專案雙引擎點火！ 「散熱大廠」8月營收改寫新高 iPhone新機助攻營運、目標價衝4005元 - Yahoo股市](https://news.google.com/rss/articles/CBMirgNBVV95cUxOTm90OWt5d0VncXowR29nZXJZaUV2dmdnSURfSGlxZmZzRGlwTDFYUHlfMHpqbFRETjJwWUNGOF9BYXp4SktPNzhxRXZ1bVRVa2pkeUZJTllNNUxKT3pRN0F4MmFNU0lObzhLYklocjF2QjE5dHAzMm8tamMxWDdQaTBibF9KUVFFOWM2TnV6MU9oUXpRd3hDWWM2NmN1Wm9qSEcyYlFXR01wanZZZmttUGtLTXhFV3hXUVM5Q0VFdmtuRnFjTG02a05LeUJ6ZGlDb0pDTFU4elJlQ1FnSVpFNGZ2X3BvdzA3dUV4eGNGQmx0Vmp2UElZMm8tX1VIQnN2WUstc2lUUXIwMk1iV0liLTNkN3JzaXZqX2dnWHNMTkw4ZGE5Tzd3RXU3UmpqaUU5N1J0M2Q3TVVYVHpKbVlJVlA2MTMzOEwyNEdEQnpWNFl0WGJlYkY2RUtBYVQ0bzE1aDlyRHNBUi1DWlN2VHlrMkdQZGZXd096amhDMHdlQkxxOThHanN0T3dFMThCOFAteC0zTGIyVldkdnUwWGk4ZmVER0s3cndhaW82b29B?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 14 Sep 2026 09:00:00 GMT
- [散熱需求強 奇鋐、雙鴻H2營運旺 - 中時新聞網](https://news.google.com/rss/articles/CBMia0FVX3lxTFBxWkFTTE5sX0ExREtUSWZkSTVaa184c05NNnN6ZnU2SXN4SDJRc0JnTVpoc3ZpQlpkb3FCUFcyVUR2eUREdkRoMl83cUpidDFUMzJGYzRFWEg4NklwQ0tEYnR2OTZaZ1p5c1J3?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 15 Sep 2026 20:10:00 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Chip Stocks Tumble as AI Pacing Call Reaches Beyond Memory: Intel Drops 7%, AMD Sinks 6%, NVIDIA Pulls Back - Yahoo Finance；Memory Stocks Lead AI Selloff as Anthropic and OpenAI Chiefs Urge Slower Development: Micron and SanDisk Sink 6%, SK Hynix Drops 7% - 24/7 Wall St.

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | -4.47% | N/A | 927.60 | 975.26 | -4.89% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | -9.55% | -11.92% | 1,530.90 | 2,335.00 | -34.44% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +5.69% | +0.49% | 212.17 | 220.78 | -3.90% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | -2.31% | N/A | 504.20 | 516.13 | -2.31% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | 0.00 | -15.29% | N/A | 97.14 | 114.68 | -15.29% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 新聞直接提及 | 0.00 | +10.41% | +1.04% | 497.12 | 507.29 | -2.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「memory、Micron」，共 2 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 1 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Chip Stocks Tumble as AI Pacing Call Reaches Beyond Memory: Intel Drops 7%, AMD Sinks 6%, NVIDIA Pulls Back - Yahoo Finance](https://news.google.com/rss/articles/CBMimAFBVV95cUxOMGN6c3J6elM5ZkVXVTBHYTl6TGFmeTNYbHI5TDJfMXEtTjd5aUFLUTl2UW9mYXFyeW05NWVpNGhzUlBybnA0YjVRMC1haXJjaVU3azBkME5qX2VXbEpraEVlY0xCSmNpakJ5QTg0Q0tVeWNMZ21GMndPNElqMXJqdzl1T1hlVkVnY3gxaDZkQzc0b0Q0MHNCYQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 14 Sep 2026 13:23:34 GMT
- [Memory Stocks Lead AI Selloff as Anthropic and OpenAI Chiefs Urge Slower Development: Micron and SanDisk Sink 6%, SK Hynix Drops 7% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMigAJBVV95cUxQWWdzS2syakFOajVaTVJORW1nX2lrOGUzeXFNd1RkOEwxeVB3LWs1bF9NUEpTUjZVODZ2VWZZbFlQQ2diNDZDRS1LTURZbEhlSTZSM3RBZW4wVDZjVm9QMVFyc2NxbjQ0WVY3bENQNHhXQWJFZGNEMFlJTnQxWTFDZFpYenNpMXpJNDE4Z3VWSlNSY1IyV2ktSDRnbzFVY1ZFbDhwWFhMUGVrSXdxSlpMVVJQdjUxdDQ0dmdJTjcxMDNKbVVjZWlBdi03Wlp6SjJHTTNHcHBucjFUX2RzUFdmaXZMajVEbHJkSi1RNGZNUVlQQk1pQ0ZMZkQyaVFTYTln?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 14 Sep 2026 13:18:00 GMT

## 新興題材：OpenAI

摘要：新興題材：OpenAI 相關新聞集中在：Memory Stocks Lead AI Selloff as Anthropic and OpenAI Chiefs Urge Slower Development: Micron and SanDisk Sink 6%, SK Hynix Drops 7% - 24/7 Wall St.；OpenAI is working with Anthropic, Google on AI safety, Bloomberg News reports - Reuters；Nvidia's Huang diverges with CEOs of Anthropic, OpenAI on AI safety at Dreamforce - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 新聞直接提及 | 0.00 | +10.41% | +1.04% | 497.12 | 507.29 | -2.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +5.69% | +0.49% | 212.17 | 220.78 | -3.90% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 新聞直接提及 | 0.00 | -4.47% | N/A | 927.60 | 975.26 | -4.89% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | -9.55% | -11.92% | 1,530.90 | 2,335.00 | -34.44% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：新聞直接提及「OpenAI」，共 5 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MU：新聞直接提及「Micron」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Memory Stocks Lead AI Selloff as Anthropic and OpenAI Chiefs Urge Slower Development: Micron and SanDisk Sink 6%, SK Hynix Drops 7% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMigAJBVV95cUxQWWdzS2syakFOajVaTVJORW1nX2lrOGUzeXFNd1RkOEwxeVB3LWs1bF9NUEpTUjZVODZ2VWZZbFlQQ2diNDZDRS1LTURZbEhlSTZSM3RBZW4wVDZjVm9QMVFyc2NxbjQ0WVY3bENQNHhXQWJFZGNEMFlJTnQxWTFDZFpYenNpMXpJNDE4Z3VWSlNSY1IyV2ktSDRnbzFVY1ZFbDhwWFhMUGVrSXdxSlpMVVJQdjUxdDQ0dmdJTjcxMDNKbVVjZWlBdi03Wlp6SjJHTTNHcHBucjFUX2RzUFdmaXZMajVEbHJkSi1RNGZNUVlQQk1pQ0ZMZkQyaVFTYTln?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 14 Sep 2026 13:18:00 GMT
- [OpenAI is working with Anthropic, Google on AI safety, Bloomberg News reports - Reuters](https://news.google.com/rss/articles/CBMiuwFBVV95cUxPaENkNHlJX1lkYlJtRzRtZ0NEaFpfbkxub0F1VkVUVHBvVTdMaHV1NjRDMnY5N09TTnIzRzFQZmFYcnY3ZkplMmxGQ1Y2OFRXT1kyTkNlWnZ0SjFsWHdHMWl6RklJeTFmMjVfYVN0ZTlidzhmR090TVdzRFRQd1ZmSFB2dXIyM1BLYVJDNlZMYy1PYnpTdTR0bHBYR2JwYWpMczAzSm5jU0JqYkJwb2V1SmhmMVJxSzRILXBZ?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 15 Sep 2026 14:53:18 GMT
- [Nvidia's Huang diverges with CEOs of Anthropic, OpenAI on AI safety at Dreamforce - CNBC](https://news.google.com/rss/articles/CBMingFBVV95cUxNamhBSWgtcmZwTVRVOXlnbGZMN2R1bDFlMWEtV21wUXFmUGVoWW5vQWNVbU55OEE0T0lWMUFlMXFZVGdvNmN0TElFUGNkQUlwQ01hU09aUEZIZlBjd0lMbGJMOVJHbmhOSTNRaHU0cXBnNmRVQ2lTb21odDUzOGlRQ1phSTRDUDVucThHQjNncjI1Q1pMOVV0WlotdDVpUdIBowFBVV95cUxNQW5ST21vbGJyUWYzcHVFZFJOZUgzTEJ3TWFkS3Y4Nm9fQ2w3c3puMnJqaFBpbl9CVG5Gd1RSZUVGQmJqLVZaN0dBZ0dOWEZNb3IxMDBtaGhWNGllb29aZERqeGxibHhnakZJRDgxeF9oa1NDSGV2YzYwa3plQ0dhZU43aHJNb1MyUlZRRm1hb1BZRVpZRVF4LUd1OWNQXzJpZFpr?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 15 Sep 2026 20:00:16 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Prediction: AMD Could Be Closing the Gap in the AI Chip Race - 24/7 Wall St.；看好 CPU 需求！富士通最快明年出口 2 奈米 AI 晶片，交由台積電代工 - TechNews 科技新報；聯發科發表首款 2 奈米旗艦 5G Agentic AI 天璣 9600 Pro 晶片，AI 性能提升 51% - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | 0.00 | -2.65% | -3.44% | 2,385.00 | 2,425.00 | -1.65% | 不適用 | 86.28 | 27.65 | 514.81B TWD / 53.32% | 2026-09-01 |
| AMD 超微 | 新聞直接提及 | 0.00 | -2.31% | N/A | 504.20 | 516.13 | -2.31% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2454 聯發科 | 新聞直接提及 | 0.00 | -6.14% | -5.94% | 4,430.00 | 4,585.00 | -3.38% | 不適用 | 60.69 | 73.16 | 64.18B TWD / 44.08% | 2026-09-01 |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | -15.29% | N/A | 97.14 | 114.68 | -15.29% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | -2.81% | +1.09% | 138.50 | 164.50 | -15.81% | 不適用 | 6.68 | 20.83 | 25.04B TWD / 30.71% | 2026-09-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +5.69% | +0.49% | 212.17 | 220.78 | -3.90% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | -4.47% | N/A | 927.60 | 975.26 | -4.89% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -9.55% | -11.92% | 1,530.90 | 2,335.00 | -34.44% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip, foundry。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2454：新聞直接提及「聯發科」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。

### 主要來源

- [Prediction: AMD Could Be Closing the Gap in the AI Chip Race - 24/7 Wall St.](https://news.google.com/rss/articles/CBMipgFBVV95cUxPeFZYaUd5UEhkTGpXSlo5eWpwZVc5WTl2ZVBnMG1zb1d1TWoxanFrcUVIV2tlSDg3bXd0ZGpxLVE3czdLZFJ4emJFb1Z1U3J0YzFKYTBkVmV6TExaMnZUempnNkRiaTd6SWg1MUJmNUlMZlMxOWJVN08tWlg2TVlISk1SRzFWVEFFRDB2Ty1jWWtTZlFlbUxPXy04NFd4aGtwQ0Z3MFp3?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 15 Sep 2026 17:00:00 GMT
- [看好 CPU 需求！富士通最快明年出口 2 奈米 AI 晶片，交由台積電代工 - TechNews 科技新報](https://news.google.com/rss/articles/CBMingFBVV95cUxPY0Q4VENIRkRkcG9DdzdtSzM2VkF4N0FUT2tCYXNheWVqN0QwUE5Tbm9LS2pnRFcwbWQtUlZDMUE3YW1fT0p1Tk5OZ2JudFE0YUh5c29nbmpkd1kwS2dBZGxhYW81Smp2QnZic3ZobHpqc0dIbUF3MlBRaVFOdlktemVtSjhBeElsZkM0Tm9WM1UxMVgyN0lBaG0yVnBUQQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 14 Sep 2026 07:08:54 GMT
- [聯發科發表首款 2 奈米旗艦 5G Agentic AI 天璣 9600 Pro 晶片，AI 性能提升 51% - TechNews 科技新報](https://news.google.com/rss/articles/CBMiqwFBVV95cUxNUFlvdUxqdURDcnJFWnNpeDZZb2czN1pCb2N5SWIzZ2JYRnVFZW5KUC1VMzE2NTg0MkdiM3Bmd2tyekdwVUE1bi1oeExJeXQ5cmkwODEtTjVTMnN4ZklTWGY3S3dURmxHUW5mNF9NZ09fZ1ZLY1RFWVpXVHBtUW5wZzAtU0Z6X19MczZubHpnY3dieVN4Qkl2UGpuY25OYlYtTUx0bVdfTy1JWHc?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 15 Sep 2026 07:36:26 GMT

## 新興題材：MarketBeat

摘要：新興題材：MarketBeat 相關新聞集中在：Tigress Financial Forecasts Strong Price Appreciation for Intel (NASDAQ:INTC) Stock - MarketBeat

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.21 | -15.29% | N/A | 97.14 | 114.68 | -15.29% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。 方向判斷命中詞：strong。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Tigress Financial Forecasts Strong Price Appreciation for Intel (NASDAQ:INTC) Stock - MarketBeat](https://news.google.com/rss/articles/CBMi2wFBVV95cUxNZ0lFM21nazl1SWVTa0NWTTBjRUpBQ05lR1FfdURNMkRaWFZwYk1xMEVYQS1ZLU5vZWdON2xjbE94YTRMeV9KOEoyYXBmbnBOTE1OenhSY0trRjFzV2MxclRFQk1ZdzZJbnZ0S3oyTVd1ZU9ZXzAtVHliTXpEWm1iX21maklHNjRsRm5GY3FBUHAyYVZ2NXZ5THpXTGFzV2w0ZE91a0ROQkxVMnQwc09ST2l2czZPb1I3RDhKMzF2OXBjZVlZdi0zUEhvQm9UQkZ6alBkY1RWd2RlMzQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 15 Sep 2026 20:27:38 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股外資狂賣 四個交易日提款2,272億 公股行庫連四買 - 經濟日報；台股儀表板 守護市場 - 經濟日報；11檔台股商品 量價齊揚 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股外資狂賣 四個交易日提款2,272億 公股行庫連四買 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE85aG8tT2dwa1BLWVhVdjNpaEw3SnN0U2Y4QWpWYmtuOTByQ0EzdGxNOERxUVdjS0NuVWxxaXJlOTZ4a00wQ25jMzJ5R3lQTnNmaF9XbmtBY0JDQdIBX0FVX3lxTE5CYVNFQVB6YTd2OURLR0FqbERIeV9zSy1QRnN4RVkwWFdHZVRjOWZnQ1hQY0RlOWQ0dklZbFlqN3BUTU9malF1YlhMa0tSY3RzR1RaeEp1N3cxbTNVNEZB?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 15 Sep 2026 17:47:01 GMT
- [台股儀表板 守護市場 - 經濟日報](https://news.google.com/rss/articles/CBMifEFVX3lxTE9QYUNObjN4LTJIZmE1cl9HME04aGpHNFdLa2RyR054TWxYSlJmZ3FCUlJZa3ZtallsQU5BOVQ2OWdCc0IybTAzYV9TQTJJR3FnRHduN0o0SUphVDVXeDBCS1pybEpIZ3g3T1E2NDFlN3hvN2pic0pyS1BFNHfSAV9BVV95cUxOQU14MExLTFFwTUN6MUhrN0dXQTdvMkx5akhRZWFXR1N6a25uS0xKMVpaTTVKOWdsNE91REhIMVp4Z0F3cXJVcnFfT0hyZnE0elp6cnBxWHNhRlFiVG1VVQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 15 Sep 2026 15:57:00 GMT
- [11檔台股商品 量價齊揚 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE8tazMybzhYU3pEdFJEWXRSWkktaHA3V0xINXpibVJudHoxWk1QRWRuZlBVSlBRWnZtWnpIbktMdDVRekFBQjFhYXUzM1o2elI1OWc5YXpOWDYwd9IBX0FVX3lxTE5KSlBpcnNYMTBGRHhfVU9fRkxvYks3YXR2Q3daSFA3UmZWVEp5MU9PNWZnSHl6OWp0ZlJBLTM0cjBDMVBVMDdDbkNrUjB2RHlnaUJ2aVRrMnVoS3N4UE00?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 15 Sep 2026 17:00:37 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
