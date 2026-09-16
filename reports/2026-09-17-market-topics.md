# 每日股市熱門話題分析 - 2026-09-17

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **新興題材：MoneyDJ**｜負向｜熱度 11｜市場確認 74.92｜同向 1/1
2. **記憶體與 HBM 供應鏈**｜中性｜熱度 7｜市場確認 N/A｜同向 0/0
3. **AI 伺服器與資料中心**｜中性｜熱度 15｜市場確認 49.18｜同向 5/8
4. **散熱與液冷供應鏈**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0
5. **半導體與晶片供應鏈**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.43（樣本 9）
- 5日相關係數：-0.13（樣本 7）
- 同向比例：6/9

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 新興題材：MoneyDJ | 74.92 | 1/1 | 0 | +1.64% | +3.22% |
| 記憶體與 HBM 供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 49.18 | 5/8 | 2 | +1.81% | +5.67% |
| 散熱與液冷供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：StocksToTrade | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：OpenAI | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
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
| 2026-09-17 | 0.43 | -0.13 | +66.67% | 9 |

## 歷史回測摘要

- 回測日期：2026-09-17
- 近5日 3日相關：0.05
- 近5日 5日相關：0.58
- 同向比例：+33.33%
- 權重狀態：未調整

- 方向準確度：+33.33%
- 信心排序準確度：0.05
- 診斷：低相關

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

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》收漲337點、日K翻紅，46K得而復失- 新聞 - MoneyDJ；台股破月線進場報酬優 主動市值ETF有助卡位 - 台股 - 新聞 - MoneyDJ；台股反彈 台幣早盤翻紅走升5.8分 - MoneyDJ

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3037 欣興 | 新聞直接提及 | -0.42 | -1.64% | -3.22% | 961.00 | 1,070.00 | -10.19% | 同向 | 15.49 | 63.98 | 17.75B TWD / 56.26% | 2026-09-01 |

關聯理由（前 3）：
- 3037：新聞直接提及「ABF」，共 1 篇新聞命中。 方向判斷命中詞：衝擊。

### 主要來源

- [《台股盤後》收漲337點、日K翻紅，46K得而復失- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQQUFyZWM2TWlWbkxGNW1OMmt6aU1tRDRYbU0zaWVZMXg0WW01cmxOWXNjdnR4bjF4eE1ZbVV4U19DWEtCbnQwcVJzTVNFRWJob2R3SEF5Ym9TQjhoQ2E0RjFNazNEbDRZR3c2N0V5TVNfQ2hOWnVYdlZ4Q191LXFCR2dJWDB1WDlXRXdISU1tSEdQUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 16 Sep 2026 08:04:00 GMT
- [台股破月線進場報酬優 主動市值ETF有助卡位 - 台股 - 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMiggFBVV95cUxQY2FsU1ZlR1dBT0VYejFmRWtrTlY5Qy1zRDUzTGxqRW1zZVpPTkxBOC10VzViZ3J4a2MwSjAyNzdybzIycWtwY24xcG5yMXpKRnZJaVl1OWxZTXI4NGJQRWNqa0JRTGcwX2pKM0JubTgycExYd0dpX0RHRFNuaDNkdElB?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 16 Sep 2026 02:44:00 GMT
- [台股反彈 台幣早盤翻紅走升5.8分 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxOOWQxTmN2UV9GcF81cnlQSGtwUkJDSzNJV3JQZU1XMGdkbU03bU5neXZjUjY2VHNEY3BWM1R6OFNJa0t2TEM2dUNhdnlURW1Kd1FBSU16TXJBNTV5SEg5c3p1WHhjWHEyMHBHMjFZaElLS2RoQzBkaktUYkptcVhVbFZGaHhkVEswa19LVEt5MTREUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 16 Sep 2026 04:52:00 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Intel Stock Investors Should Pay Attention to This Potential SK Hynix Deal - The Motley Fool；Intel Stock Investors Should Pay Attention to This Potential SK Hynix Deal - The Globe and Mail；Intel Rises 4%, SK Hynix Climbs 3% on Reports of Talks to Make Memory Chips at Ohio Campus; Micron Holds Flat - 24/7 Wall St.

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | -4.58% | N/A | 926.55 | 971.00 | -4.58% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | 0.00 | -11.89% | N/A | 101.05 | 114.68 | -11.89% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | -6.94% | -13.84% | 1,519.97 | 2,335.00 | -34.90% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +6.55% | +1.31% | 213.90 | 220.78 | -3.12% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | -0.70% | N/A | 512.50 | 516.10 | -0.70% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、MU、memory」，共 4 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel、INTC」，共 4 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK」，共 1 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。

### 主要來源

- [Intel Stock Investors Should Pay Attention to This Potential SK Hynix Deal - The Motley Fool](https://news.google.com/rss/articles/CBMiuAFBVV95cUxQbXRKX24yY1N4emV2eWJOOWpNWnlaSG9XcjVEbG9McFhYNTQwU0otWWlldEN6N0Fua2docEswc3dSNGpKZ0RyaTBRbDk2QzJIeWNBUnkwNmtiZ0VMYXBpR2E2TzZMNlRSTVdCOWZWejl4b2FYY0ZJRGpTQUVRY1dRTkNsQ0t6Y292TDB1VlhpTlFPcHhsOU1XNk00N0M4V05hQ3RhZm5RdGg5X0RrdnB6bllTeE5hdC0z?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 16 Sep 2026 16:06:00 GMT
- [Intel Stock Investors Should Pay Attention to This Potential SK Hynix Deal - The Globe and Mail](https://news.google.com/rss/articles/CBMi8wFBVV95cUxOQjZ5YUtOWUlxMGxVT1h6d2V4MDNDQktRWVl0LUxmMGZ6UkVUeTNQRjByM2NGY1NuajBBQ2hicXV6dFFOczl4bTQzallpeVdCZkRtTHZSQVR2TTJyNU5UenpJakFVdTB4MmNDOXhQQUNJR0l4dDctamdHYktHOXM2MzFUSC1TX1o0ZnQ2RXZGSkJEM0VTaGkyMG1SZjB3MXNIbk9iaEpkZ2FheHVFR1hJdkVxa0ZGTVZxMGlRSnFwWFpsWkctYmh2NjJ0Qk9CTEJnZEgxRERFUldCU05GcDQ5RlV2bHZ3MXhFdXhpZGU3S2lGM2s?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 16 Sep 2026 15:33:56 GMT
- [Intel Rises 4%, SK Hynix Climbs 3% on Reports of Talks to Make Memory Chips at Ohio Campus; Micron Holds Flat - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi6gFBVV95cUxQNHNndVNsMGRvaTdjQUhEMUhwMGxCa0J6VWpjSmFSLThlVXRRRkVhY254NXlZdkpOR0VPSnJKR01SNmZOSGFRSE1ONTgxWk9nLWRZT0VDZEMxRjFGTWxncm1ETFhnNkZJYmxjT28yazhmeDZpUFZOaERlYnRJSmMwQmMzVFBjcElXTHExbFllV0k0d3RWOG9pRks3UmVZUlNtSFFYaVZ4SzVGTHJTay1HUW9JYWMtMkdCYm1fNGlkWnVZYnFXdW5pR01mcGdlR18takFxQk9udVhIdW1NVXYzQjZnT1NWWi1SM2c?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 16 Sep 2026 12:39:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Did AI Slowdown Calls Just Shift Intel's (INTC) Investment Narrative? - simplywall.st；AI 出事別只查技術漏洞：真正的風險起點，藏在更早的人類決策裡 - TechNews 科技新報；康舒 AI 營收占比目標 3 成，100kW Power Shelf 啟動驗證 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.54 | -11.89% | N/A | 101.05 | 114.68 | -11.89% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | -0.03 | +6.55% | +1.31% | 213.90 | 220.78 | -3.12% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | -0.04 | -0.70% | N/A | 512.50 | 516.10 | -0.70% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.06 | -1.24% | -3.45% | 2,380.00 | 2,425.00 | -1.86% | 同向 | 86.28 | 27.59 | 514.81B TWD / 53.32% | 2026-09-01 |
| MSFT 微軟 | 產業/供應鏈推估 | -0.02 | +8.90% | -0.35% | 490.30 | 507.29 | -3.35% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -12.79% | -24.01% | 339.51 | 446.77 | -24.01% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.04 | -2.10% | -5.47% | 605.00 | 680.00 | -11.03% | 同向 | 13.92 | 43.78 | 82.25B TWD / 45.66% | 2026-09-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.04 | -1.20% | -2.05% | 4,530.00 | 4,530.00 | 0.00% | 同向 | 60.69 | 74.81 | 64.18B TWD / 44.08% | 2026-09-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：slowdown。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：slowdown。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：slowdown。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Did AI Slowdown Calls Just Shift Intel's (INTC) Investment Narrative? - simplywall.st](https://news.google.com/rss/articles/CBMiygFBVV95cUxNakJZbUFyUjVHQjJ6WnBieFdVdHNkWGJKYjJzc0c1aVlQYjRpRVREOXRIdm1GeVRpLTczX3FYbEVuNWpRNUNuZDVSc3pIb050SXB5ZlJDSEFQVlFLSk5GVWxOaGl3dkRwdGV4ejFYU0g3b0t0NlZnaEswVUdYNVhZYUM5SjJKbFluZ0E0MmVWcG1rU1NuZnB3c1pHU0Z4SDhqYlgxNk5IcmM4eUtqVnJvam1NbTBKeVctSUdRUzJfeFRlUkFKNHlPSU930gHPAUFVX3lxTFA2TGgyeTJvSm9waExBN0tBMXVtbEE0aVdGcUpFeHpxYnJKaHFjV3k4b2F6YWhZcHNNSldTZXZxTl9QWlVwaWxxXzFSRjVJcThXRWdrZU1KZ2VMX2xwZEx2cllKR1dLWno3STlOemw5SnJWZ1NwZ0w3YU5WRUtSejdSbXVNbmx6NENLbHB3eG9ZUXNKNkk2cHZub3pFbkRvNmFYLW9TZHN1REszR3d0MXNQcExQckJia2R0UmhZRFZOekIzTXpmS2NSTmYtaUtaOA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 15 Sep 2026 17:45:54 GMT
- [AI 出事別只查技術漏洞：真正的風險起點，藏在更早的人類決策裡 - TechNews 科技新報](https://news.google.com/rss/articles/CBMimAFBVV95cUxNdFBMN2FxeXg1M1YzN3UwdnVidDlOSDRTcE5DTU9xVFF1TWZVVzdyVk5PQUtZYVJLdGNZLXljLTdidV9OZ1pXajdPR09jODZqRE1NUDhJYmVHbnFHVUJDNXBRbkZsY2hwNnZHaFh5Z0xtbG9OSTN1QUNYdWRuYzJjX2VUVldUblJMS1M4dTdjVWIybnFPQlg0OQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 16 Sep 2026 23:21:07 GMT
- [康舒 AI 營收占比目標 3 成，100kW Power Shelf 啟動驗證 - TechNews 科技新報](https://news.google.com/rss/articles/CBMimwFBVV95cUxOVnRSRy1ONnpqODRNNS1jTEtGUy1xVVhJdUk1VTJQMGk3M0UzM3ItdnhGWW82cmpaMDVPUFJWUFdBVUhCTExweGdYVGlnN3NhVzZJVmpaeVdoWHRRYi1rMnZUdk56T1dmU0NtSnpjQkI5TVNLMDJWTEJhd2dJNERKaTdpeTRoUHdfUVUyZU1JaXNsaXlmQ3JUemVTYw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 16 Sep 2026 02:26:26 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：AI散熱族群概念股有哪些？奇鋐、雙鴻、台達電上中下游供應鏈全指南 - pocket.tw；散熱需求強 奇鋐、雙鴻H2營運旺 - 中時新聞網；奇鋐上看4600元？ 外資最新報告出爐了 - 東森新聞

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | -5.79% | -6.07% | 3,175.00 | 3,425.00 | -7.30% | 不適用 | 75.13 | 42.32 | 19.48B TWD / 54.34% | 2026-09-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐」，共 3 篇新聞命中。 同時符合主題標籤：thermal。

### 主要來源

- [AI散熱族群概念股有哪些？奇鋐、雙鴻、台達電上中下游供應鏈全指南 - pocket.tw](https://news.google.com/rss/articles/CBMiY0FVX3lxTFA0eWNaMWZkZ2lkdmdXeTRRLVJZMGVfRUx6LUhpZ2lKTUlIQTVNSDFpLW5ucUROWVJMVm1MbTR6T0owZVB1dWpJb1BQVGhFQnBwYkxkM1FCME9ld0xSX3BIZ0hVTQ?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 16 Sep 2026 06:54:36 GMT
- [散熱需求強 奇鋐、雙鴻H2營運旺 - 中時新聞網](https://news.google.com/rss/articles/CBMia0FVX3lxTFBxWkFTTE5sX0ExREtUSWZkSTVaa184c05NNnN6ZnU2SXN4SDJRc0JnTVpoc3ZpQlpkb3FCUFcyVUR2eUREdkRoMl83cUpidDFUMzJGYzRFWEg4NklwQ0tEYnR2OTZaZ1p5c1J3?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 15 Sep 2026 20:10:00 GMT
- [奇鋐上看4600元？ 外資最新報告出爐了 - 東森新聞](https://news.google.com/rss/articles/CBMiV0FVX3lxTFBJbi1BRWFSZkxTS0plSW5YbjQwRkRIV3JnaVV1dzhnMWltWld0SGZOaWI4LUtkdF95WjJyZThZdzhON0gtT0pmQmdTZklUeG5XVXI2V2xRaw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 16 Sep 2026 05:00:00 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：量子感測如何驅動半導體失效分析的革命？ - TechNews 科技新報；美股收盤／Fed 升息還沒完！道瓊跌631點 晶片股逆勢反彈 - 經濟日報；科技半導體 ETF 績優 今年來00913漲逾106%奪冠 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | -11.89% | N/A | 101.05 | 114.68 | -11.89% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -1.24% | -3.45% | 2,380.00 | 2,425.00 | -1.86% | 不適用 | 86.28 | 27.59 | 514.81B TWD / 53.32% | 2026-09-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +1.07% | +0.35% | 142.00 | 164.50 | -13.68% | 不適用 | 6.68 | 21.35 | 25.04B TWD / 30.71% | 2026-09-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +6.55% | +1.31% | 213.90 | 220.78 | -3.12% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | -0.70% | N/A | 512.50 | 516.10 | -0.70% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | -4.58% | N/A | 926.55 | 971.00 | -4.58% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -6.94% | -13.84% | 1,519.97 | 2,335.00 | -34.90% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -12.79% | -24.01% | 339.51 | 446.77 | -24.01% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 CPU, server CPU, x86, foundry；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 0 篇新聞出現相關標籤。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 0 篇新聞出現相關標籤。

### 主要來源

- [量子感測如何驅動半導體失效分析的革命？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMid0FVX3lxTE1fWmZoTnlNbVhUSHRvWFd2Rks2ZVVxNW4zb3A3MGhndGY4ejhKLTBQckI4WmgwSTJuLUltTHlsZzF2Z3VFcWo3bVJEYld4RkVzSm5fVmlFM1JDM3ZSeGtEU3MzSlVVdldaeXUwQ0l2TFFkWV82RmQ0?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 16 Sep 2026 21:51:28 GMT
- [美股收盤／Fed 升息還沒完！道瓊跌631點 晶片股逆勢反彈 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTE9xc1pOdERNakFpemtrekZGMGFnbnhzcktGOGRVZmpnNUtaY0p4NEgweUNEUkN1MURfUUcxdHVyUkNCd1UtSzI2ck1tM0dqcDRucllnRFFKVVF2R2tP0gFiQVVfeXFMTW1iWEIyRTR2WkVrejNJNmNsam5VS1JkZ1JBQ2RkTVJ2YWhKYklUNlBHb2lSZ1k3RnpBZy13NDFYOHNjTkxSWkQtUDg0R1h6S2t3OUdVQS01Ym15ekdtN01YUWc?oc=5) - Google News source discovery | 經濟日報 money Wed, 16 Sep 2026 23:00:32 GMT
- [科技半導體 ETF 績優 今年來00913漲逾106%奪冠 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE90b3lKWkQ1Nk9iUi00dWRvZ1JoUEk1UEdpTVlWaVE1UUpXcjZrYUtaem1VZEhEeWdHZHl2dHc5d3pEMlp5SWpLa0lCYTlVMTVFWmwzMm1ySmRwZ9IBX0FVX3lxTE1qVTd5UFEwbmh5VlptdGJHWnJ5aHVEYTl0cFJ3ZlY1V3c2VmxtZ0h0anJ4YVVYTm9pdmxOREJOdUZmOGUtSElydHB5V2RDRUUwVmZCX04zckJRRlpxNk5R?oc=5) - Google News source discovery | 經濟日報 money Wed, 16 Sep 2026 15:20:06 GMT

## 新興題材：StocksToTrade

摘要：新興題材：StocksToTrade 相關新聞集中在：Intel Stock Jumps As AI Turnaround And Price Hikes Stoke Momentum - StocksToTrade

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | -11.89% | N/A | 101.05 | 114.68 | -11.89% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Stock Jumps As AI Turnaround And Price Hikes Stoke Momentum - StocksToTrade](https://news.google.com/rss/articles/CBMiekFVX3lxTFA1emhqdEJNYzFlLTgweks0SGVOVU1yeGgzbVl1V1ZqYlM1d2ROUV8yTXRSQVBXdTl0bnVNalZPZXFPNzQ1MFYyek1SdjNpdHhDOW9xMkp6TUNLTDdmN2h2OFZBX00wQ3k3UG5IeUFsU2pUM1JqT3JPU293?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 16 Sep 2026 11:48:00 GMT

## 新興題材：OpenAI

摘要：新興題材：OpenAI 相關新聞集中在：OpenAI tests advertiser-sponsored agents, expands AI tools for ChatGPT ads - Reuters；EXCLUSIVE: OpenAI's rogue agents probed Hugging Face for weaknesses two months before major hack - Reuters；Anthropic, OpenAI proposed new 'neutral' AI watchdogs. Why you should worry about the idea - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 新聞直接提及 | 0.00 | +8.90% | -0.35% | 490.30 | 507.29 | -3.35% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：新聞直接提及「OpenAI」，共 3 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [OpenAI tests advertiser-sponsored agents, expands AI tools for ChatGPT ads - Reuters](https://news.google.com/rss/articles/CBMixwFBVV95cUxPdzBSSTlvNXJRRXplQlhuWUlTV2NDS3pKOHdpV3Q5YnRRZ21XT3RrT0ExVkhmbFlkaWZMM3R1LUJybTVvMm1GOEluTS16ODZRVUl6VVlkbE5OaXFQY3Y5NWw1RVh3cGZ0VVdveDVIVFhNWVhsNDZ0aXVhQzEyeWlpOVVyLVpCMTNiSkhQVVp2R2ExWXlJUVhRamtEV3ZtVkJTR2lvM0R3RW0tVW5vQmhuTm9uMUtyYWlEdWdwNUNQaTIxdkxZeTZB?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 16 Sep 2026 14:20:27 GMT
- [EXCLUSIVE: OpenAI's rogue agents probed Hugging Face for weaknesses two months before major hack - Reuters](https://news.google.com/rss/articles/CBMizgFBVV95cUxQS2RNOFJnNVFtSUxoYTBUczVlemRjdHUtYndvcEc0MEF5QTRiRWxSOTFXU1ZqLUFKSjU1QXN2Tnh1TEhWQ195M0dUSTM3WEN3eTVxUlRja2liZmNyYXlrZGpOY2FTMUVzMmxZWkxISHZ1RFVTNUhGdUl6R3o3Y284b0l1VXZyVU9CMlIwLXVRTzVwUG8zSG1lOG4yTFJTQm9mLUFKQWREU08zVFI0VDY3NGNJNEtfQTcwdUtSa0Y5aS1OdUZQZ2czWi1nWFVhdw?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 16 Sep 2026 22:25:54 GMT
- [Anthropic, OpenAI proposed new 'neutral' AI watchdogs. Why you should worry about the idea - CNBC](https://news.google.com/rss/articles/CBMifkFVX3lxTE82dGJtZmlDaGJtODJPSXBoY2xRRTFMdEtQMEFYMkpyMzJoUEdzRnc3bXg4b2F3cC1lRUJGRlMzQ0QxbEVfSU1DVktIUm4yMzBLVEhwQjJhd0V4bWZxdnVVallHSTJBOHNfaEUtLThSYmI2eFpUbmtiLWZRXzR5d9IBgwFBVV95cUxPUFRFd2huX0ZQQk9EWGowajZHZ05OcWU4ZGhOMm95SGxnOEttR2ZTV05sN2UtS2ZOVzBnZFphdE5lYmI4LWdrcVluc3drWE9ZTzJjQmIwemEtODNiZDdiTldJM2FqdXF1dVQxVDhGYmZELW9yWjJmdEZ4Qjc2VWk1YV8wOA?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 16 Sep 2026 14:15:01 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股三轉機醞釀新攻勢 法人解讀有機會上演利空出盡行情 - 經濟日報；台股相對強勢卻別急著追！出口創高、AI續旺 操作先等趨勢表態 - 經濟日報；00934、00904等三檔台股 ETF 換股名單出爐 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股三轉機醞釀新攻勢 法人解讀有機會上演利空出盡行情 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE0xMk5yTWtYcHoxVW1CcGctblJUeVhmV0hwOVI3QnNZRldlM2hmSFR3M19UMThySVd1Q2g2MEs0enZNNzExQTlISTRCX2JZal9yU0ljd1ZPbW1ZUdIBX0FVX3lxTE5fd0dVaXVXU2UwdXJrbmRoUDVVRWljNThVSFdwcmxHQlRWd3RJSDZTR1k0bFFJNnVpLV9FdGl3M1c0akRlWEpRUExEN2d6eVhadVhEUDB6LTA2VUd6Skhn?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 16 Sep 2026 17:46:42 GMT
- [台股相對強勢卻別急著追！出口創高、AI續旺 操作先等趨勢表態 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTE5XckYtREJ5VFZlc0JkUmFIVTgyYnJFQXFHWDFJVEY1aTZwdnl6WTBzRGh0M005ZW5lXzZnWlM3U3ZmbW9hNWNHQU5VYWVHR3I0b1lkRnJQNlVrZEpI0gFgQVVfeXFMUDgtUHQ4d2NaYjQtZFJpbVBHSzh6aF9yY3JYdGJVazZIWGo5OGU0UmZlb0FDX3dha2w3cXVnQ2w2MG9aZ1FaMjlWanZrQS1lV1RQQTduOC1pRzhDT0RvLURI?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 16 Sep 2026 14:07:41 GMT
- [00934、00904等三檔台股 ETF 換股名單出爐 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE51VnFmUnQ2eHJQN2VEYXJIamlsX0VHQVJhRDFMcTZwMkVuekx4U2t1TERnQTc1eXhKUUloa053YWR2dUpVNVpvcUxYNnpHYzNsWEVZQVpBWjVaQdIBX0FVX3lxTE5LOVMzcDVyeWdGNVBTZG5wdkg0dWpsbDNTZjI0OHVTRThUMWNBOEgxbC1qUHpOeDNyZ1RrRmpmNFhpZUs0R0dBcC1YSzBBX2NzVVhQaHJxQWZxUENWQWxz?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 16 Sep 2026 09:18:17 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
