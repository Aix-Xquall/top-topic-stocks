# 每日股市熱門話題分析 - 2026-11-25

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜負向｜熱度 5｜市場確認 100.00｜同向 5/5
2. **AI 伺服器與資料中心**｜負向｜熱度 11｜市場確認 65.00｜同向 4/8
3. **關稅與供應鏈轉移**｜負向｜熱度 7｜市場確認 39.11｜同向 1/3
4. **半導體與晶片供應鏈**｜正向｜熱度 5｜市場確認 0.00｜同向 2/8
5. **散熱與液冷供應鏈**｜正向｜熱度 2｜市場確認 5.00｜同向 1/2

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.25（樣本 26）
- 5日相關係數：0.11（樣本 21）
- 同向比例：13/26

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 100.00 | 5/5 | 0 | +29.18% | +2.31% |
| AI 伺服器與資料中心 | 65.00 | 4/8 | 4 | +10.99% | -0.12% |
| 關稅與供應鏈轉移 | 39.11 | 1/3 | 2 | +5.26% | -2.60% |
| 半導體與晶片供應鏈 | 0.00 | 2/8 | 6 | -17.99% | -3.62% |
| 散熱與液冷供應鏈 | 5.00 | 1/2 | 1 | -12.81% | -8.67% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：SpaceX | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-11-12 | -0.09 | 0.07 | +50.00% | 14 |
| 2026-11-13 | -0.56 | 0.42 | +54.17% | 24 |
| 2026-11-14 | -0.34 | 0.12 | +42.11% | 19 |
| 2026-11-15 | -0.02 | 0.62 | +50.00% | 20 |
| 2026-11-16 | -0.30 | -0.27 | +38.89% | 18 |
| 2026-11-17 | 0.44 | 0.39 | +80.00% | 15 |
| 2026-11-18 | 0.27 | -0.38 | +86.36% | 22 |
| 2026-11-19 | 0.20 | -0.23 | +69.57% | 23 |
| 2026-11-20 | -0.35 | -0.36 | +69.23% | 13 |
| 2026-11-21 | 0.04 | 0.04 | +65.00% | 20 |
| 2026-11-22 | -0.11 | 0.38 | +70.83% | 24 |
| 2026-11-23 | 0.26 | -0.36 | 0.00% | 6 |
| 2026-11-24 | -0.41 | 0.30 | +3.70% | 27 |
| 2026-11-25 | 0.25 | 0.11 | +50.00% | 26 |

## 歷史回測摘要

- 回測日期：2026-11-25
- 近5日 3日相關：-0.00
- 近5日 5日相關：0.43
- 同向比例：+70.59%
- 權重狀態：未調整

- 方向準確度：+70.59%
- 信心排序準確度：-0.00
- 診斷：信心校準問題

調整原因：近 5 日方向判斷多數同向，但信心分數與後續報酬呈負相關；判定為信心校準問題，優先降低高信心膨脹、寬題材推估與背離容忍。；關鍵詞×公司後續樣本有效 0 筆，未達 30 筆，不調整樣本權重

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

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：AI Stocks Crash as AMD Drops 10%, Micron Falls 8% and Intel Slides 5% - Coinpaper；Micron vs. Sandisk: Which AI Memory Stock Is the Better Buy? - Yahoo Finance；Micron Falls 7% as NVIDIA Pullback Partially Reverses Monday's AI Chip Rally; SanDisk and SK Hynix Drop 6% - 24/7 Wall St.

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | -0.65 | -35.14% | N/A | 629.79 | 971.00 | -35.14% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.65 | -6.67% | -19.45% | 94.39 | 291.88 | -67.66% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | -0.49 | -31.96% | -22.60% | 155.38 | 228.38 | -31.96% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.48 | -19.92% | N/A | 413.27 | 516.10 | -19.92% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | -0.48 | -52.21% | +35.11% | 54.80 | 114.68 | -52.21% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、MU」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：downgrade, falls, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：falls, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：HBM。 方向判斷命中詞：falls, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AI Stocks Crash as AMD Drops 10%, Micron Falls 8% and Intel Slides 5% - Coinpaper](https://news.google.com/rss/articles/CBMimAFBVV95cUxOdjE4dUpFVTlXR1FQbjlQWGQ4bGVucTFfMGFlSVJZdF8wdGRHVS1wdFlUbkU1Y0RaWk9Da1V4bW9UbG92Vk5NbGFIUVB1dkNTcGVhSlVtMW9yeWRnN0VhUnY4bTYwMnJIZlJOMUhYdmFkN3hKdjh2Q2l3cElqRkxCOUZJRjc0ZDY2YjJZeDQwejBTUzJTcTNDZg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 24 Nov 2026 15:44:14 GMT
- [Micron vs. Sandisk: Which AI Memory Stock Is the Better Buy? - Yahoo Finance](https://news.google.com/rss/articles/CBMilwFBVV95cUxQb3FMcEw4VGdDR2wxVTZlOXJuVU53MWlvQkw1Z3hqSnpqNWFINnBvaUhYQ1pUY3J3ellQSm9leF96SHFjaTBXYUZFLVJSTHAxdzR2VmRyM1hCUjR6SE1zZmQxc0U1dndyQTBCSmpWYTh6eXlDaDFnSkxqZllFRm5odHJIa1FGand5NEpHQzV2MDlSb2MzbVlz?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 24 Nov 2026 20:25:02 GMT
- [Micron Falls 7% as NVIDIA Pullback Partially Reverses Monday's AI Chip Rally; SanDisk and SK Hynix Drop 6% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi3wFBVV95cUxNMEhYd2YzdW9RLU5fRm1YYllkNjlZVlU0d3BKcXM1UzNXZkduWmZWMWlsTTR5WFVKX2RxdnNFSXd6RElyenpGYVBuanUza240SU9KM1lYQlo1dmdsNkNQeU1PVTNCbkhtRzF4XzFyc2xlcjh0OUd6aGNFelAyU3Y4a0FnRHl4S19nMGRYRklRSUtGeklHWXVkOEFITUhFUy13Q1ZzdnBCSXpMb19Vdmx1RFVPRjcxdDE4T2xaOGVlMjdaaW1tRDh4ODRHLVpxNzFxTG1IR09PZWhvakptRXlv?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 24 Nov 2026 14:07:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel And 2 More AI Stocks To Watch - Yahoo Finance；AI 伺服器賣翻 戴爾 Q3 超旺、營收翻倍創新高 - TechNews 科技新報；AI 亂寫判決，法官竟然被換掉了！ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | -0.62 | -31.96% | -22.60% | 155.38 | 228.38 | -31.96% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | -0.62 | -52.21% | +35.11% | 54.80 | 114.68 | -52.21% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | -0.06 | -19.92% | N/A | 413.27 | 516.10 | -19.92% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.03 | +6.19% | +2.76% | 2,160.00 | 2,480.00 | -12.90% | 背離 | 98.27 | 22.70 | 586.89B TWD / 59.71% | 2026-11-01 |
| MSFT 微軟 | 產業/供應鏈推估 | -0.02 | +10.19% | +0.84% | 496.13 | 507.29 | -2.20% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -14.27% | -22.66% | 301.08 | 446.77 | -32.61% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.02 | +5.16% | +1.92% | 501.00 | 703.00 | -28.73% | 背離 | 17.55 | 30.42 | 88.62B TWD / 47.13% | 2026-11-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.02 | +8.87% | +5.47% | 3,645.00 | 4,920.00 | -25.91% | 背離 | 62.35 | 65.14 | 55.03B TWD / 5.77% | 2026-11-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。 方向判斷命中詞：衝擊。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：衝擊。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：衝擊。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel And 2 More AI Stocks To Watch - Yahoo Finance](https://news.google.com/rss/articles/CBMijwFBVV95cUxOOHg2LVdXZVFmY3J5T3ZQckNSM3BTRzdGdWNIVnpHVkRoZlFLU2F6aXIzeHFtRVJJM3RnWFZKRWJoX29iZGFET19LZzB3TUhSc1RLejl6Sk5JcG1HdFR6TzVKY3hTWk9rRzNMbFdUb1VRaVJwOGpLRW1ZYkJwWnlCVnhOeWsxZFVNZ1Q1bkZLZw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 24 Nov 2026 22:19:18 GMT
- [AI 伺服器賣翻 戴爾 Q3 超旺、營收翻倍創新高 - TechNews 科技新報](https://news.google.com/rss/articles/CBMihwFBVV95cUxOdXdQYnBGX2pyUkl3Q043bUFieUxwcDZTX1hyVVpVaUl4UmthTmtTTmN3VHcwVWVsYWZBTXMtNXpkcDZZdktFSHQ5aFdqV1k5T1docC1wVHVyRW5NMU9yZVQxOC1aOUg5cFQ0R3UtcE9IbXJfWEszb25oZnRLZTVncnFCbllhZ0U?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 25 Nov 2026 02:50:59 GMT
- [AI 亂寫判決，法官竟然被換掉了！ - TechNews 科技新報](https://news.google.com/rss/articles/CBMioAFBVV95cUxOamhRQk5MSWo5cUtIcXhZNHBzQW5ORTQ1dEFmVS1fSDNmaWpTbUxyT3F1VXMxdko3UDB5VlFxWDVCaEQ4YVYyMjZicElBQ1Q0UHBJbXhjUjg2U0xOdG81OWMzZmRQaTNqQ1N5bmY0TzNwdUwwUUV6V3JyY0c3MC11SWlhRVZOQUxIUUdrakJKQkNqSFVhTkd0c2xJcV9NMUtB?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 25 Nov 2026 00:05:33 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：台股反彈一天就熄火？關稅變數再起法人揭盤勢警訊 - 經濟日報；爭奪 GW 級電力配額！AI 大廠共址發電與全球重電供應鏈戰略重估 - TechNews 科技新報；Stocks retreat as AI rebound stumbles, tariff threats loom - Reuters

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | -0.48 | -31.96% | -22.60% | 155.38 | 228.38 | -31.96% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 產業/供應鏈推估 | -0.04 | +13.46% | +26.98% | 354.07 | 354.07 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | -0.04 | +2.72% | +3.42% | 207.50 | 289.00 | -28.20% | 背離 | 16.57 | 13.70 | 1305.32B TWD / 45.73% | 2026-11-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：恐。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 1 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 1 篇新聞出現相關標籤。

### 主要來源

- [台股反彈一天就熄火？關稅變數再起法人揭盤勢警訊 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9yeEtOYWlsN1ZrY05mYjUyV3pDQ3pjdTMyWU5hSlFTd3dzTzRJUlVXRDZlM1pfLTRhSDFpNW5BOFdzZXItZTdjQnZZcFlQTlU3UXFQbFRkamJwd9IBX0FVX3lxTE10SC1iVmlwbk80eUpmOHVtUG9hTkJJYmp6SEtMMzI4ZjVLQTlkUWcxSHNIVHZGZndPNnlvd2F2QmJGa3oyXzRCT1ppNnFBR1o1M1M1aFkzWDdGVy1mbk9F?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 25 Nov 2026 04:20:39 GMT
- [爭奪 GW 級電力配額！AI 大廠共址發電與全球重電供應鏈戰略重估 - TechNews 科技新報](https://news.google.com/rss/articles/CBMisgFBVV95cUxOMU0zOFRHb3lKTXIwUnpOa3daa2EzWGJkSFdEMi1ndDQ4WTJkUFoycVpZUU9HQ1VQbDBreTFMRzNVdV9ub3lnVzNkaHB6LVVRSnZmOE96LUw2bnZfdmplTVBkQUpoSFdnWFktVHl1U0p1dXNmQkdVNlBYd2xxc0NLOF9MZlVOM3U4bmd5VjlGN2dIdG1xZzQtTG5NUUtfUXlVaFRyUzJtSm0wc3Ewam0xTnp3?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 24 Nov 2026 23:01:26 GMT
- [Stocks retreat as AI rebound stumbles, tariff threats loom - Reuters](https://news.google.com/rss/articles/CBMigwFBVV95cUxNRFVsTjFROGtER0loSkZOcnF2NDRLUWFmcjBHZ01ybE51N19idjFFMXI1dnFqZ21JYS1HVVpicTJ1V1RfVU4zd3pkVEZMWHdqMUJWRENOQWJ2VjFqT1Y3WS0xYTV3bzd2RnRraFhtOVpzVE9yYThzdV9tdWxJbUpjNzFraw?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 25 Nov 2026 01:50:00 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Why Is Intel Stock Down Today? Shares Fall 8.1% to $54.83 as Chip Rally Cools After 16.3% Jump - Around Prague；Intel: Geopolitics And Foundry Improvements Offer Potent One-Two Punch (Rating Upgrade) - Seeking Alpha；《基金》愈跌愈買！半導體ETF人氣旺- 理財 - 工商時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.33 | -52.21% | +35.11% | 54.80 | 114.68 | -52.21% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.05 | +6.19% | +2.76% | 2,160.00 | 2,480.00 | -12.90% | 同向 | 98.27 | 22.70 | 586.89B TWD / 59.71% | 2026-11-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.05 | +10.09% | +5.09% | 87.40 | 164.50 | -46.87% | 同向 | 6.80 | 14.34 | 25.20B TWD / 18.33% | 2026-11-01 |
| NVDA 輝達 | 產業/供應鏈推估 | +0.02 | -31.96% | -22.60% | 155.38 | 228.38 | -31.96% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.02 | -19.92% | N/A | 413.27 | 516.10 | -19.92% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | +0.02 | -35.14% | N/A | 629.79 | 971.00 | -35.14% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.02 | -6.67% | -19.45% | 94.39 | 291.88 | -67.66% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -14.27% | -22.66% | 301.08 | 446.77 | -32.61% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：fall, rally, upgrade。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 3 篇新聞出現相關標籤。 方向判斷命中詞：fall, rally, upgrade。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 3 篇新聞出現相關標籤。 方向判斷命中詞：fall, rally, upgrade。

### 主要來源

- [Why Is Intel Stock Down Today? Shares Fall 8.1% to $54.83 as Chip Rally Cools After 16.3% Jump - Around Prague](https://news.google.com/rss/articles/CBMirgFBVV95cUxNQ1hzRkw4OWJpcE9GMHBjSFp0WV9KdlFKWC1ZY01nSmgxbkRrM2N2eGRBTVFBM21BNTRQNVdmcUljT0Y0dDNNc20zcDJjYTFPUExuQkItZ251ZENpQ3JIVDl4YmxYLS1INUREY2JFLTZVMnBEQlptYU5JWjJFTjd5S1lMbmFaWHQxeUF3UDFRSkE4QnQzbWxWMjh2X21fQ2lkOVg5WmpURDdzMmdWWHc?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 24 Nov 2026 17:11:07 GMT
- [Intel: Geopolitics And Foundry Improvements Offer Potent One-Two Punch (Rating Upgrade) - Seeking Alpha](https://news.google.com/rss/articles/CBMirwFBVV95cUxQNlJlVmxWYllZX3lZS1dZTTRnZFVWanVWWkhNWXlLb0Vrajg2S2ZIZEo1emVTTWpjc3BwTVd0c3RGeDRLU3BLcVFfVFBKZWliLTZlMHc4ZGxJQjVqTVBhUV9IdVhXellLU0NhTXRMSVFLSUZ6WVJ1V09oSzN1bXpCOGs4bWZRVUVZM2x1Nmp2YVhVSnE3Qmx4V1plcTNhdmoyS2Y1VjZsV1dDMXdqcFNF?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 24 Nov 2026 15:05:21 GMT
- [《基金》愈跌愈買！半導體ETF人氣旺- 理財 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9iSG1yeTI5VHdidXYtRmFOeEpQUGJSTXhPTXozM0g4SWdsc0VEVnlkd1llaDVaU0FXSk53OHFaQkk3b2VkNm9RVGNiXzhNNEw2RUY4LW9GdUh0Ymh4dkJF?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 25 Nov 2026 01:48:00 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：累計EPS大賺73元！「散熱大廠」第三季獲利翻倍成長 輝達Vera Rubin量產帶飛 - Yahoo股市；【即時新聞】今日法人看好奇鋐液冷散熱出貨放量，第三季毛利率衝33.9%創新高！ - CMoney投資網誌

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.58 | +6.34% | +5.26% | 2,615.00 | 3,435.00 | -23.87% | 同向 | 90.78 | 28.74 | 22.10B TWD / 34.35% | 2026-11-01 |
| NVDA 輝達 | 新聞直接提及 | +0.24 | -31.96% | -22.60% | 155.38 | 228.38 | -31.96% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱、奇鋐」，共 2 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：成長, 放量。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：成長。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [累計EPS大賺73元！「散熱大廠」第三季獲利翻倍成長 輝達Vera Rubin量產帶飛 - Yahoo股市](https://news.google.com/rss/articles/CBMikwNBVV95cUxQa0NTWENQd1d3UDNCYndMaTVlaVh0WFNnZk9GelVHWXVNSmdKWlhtYzU5dlZtVzVJOGs3NG40ZVZfQ2xQeDVKVU1FZDRmd0h6MWNTc3VTekRveEVaanZnZXM1d0tleXNGT3lTRmFHMXNHZmdpOThBekF3eUtWZHUtSHFIX2FLcWh2c0RsUW5QUGtWbVRlQ1FRaGFNbFZ6UzJnY0dlMDZMcWNJQUZMbGZYdXd4QmFMUkUxU3lYako0M0JSLXdTVVA3NzQzVE45ZmVvbHhFRFNrRzJqRW5ud0pHZTVTdmRIcWQwdDc2VXZ0LS1MZVRvODU1bjlFTjZuU09SWHg1MURnQXRrOHRac25nR1lXcVVfT0tJSFJYUVY2VTM2eU5wQXRCVXBVTk1IWVh6T1dOTVRKTlE3elJYaEx3MFFQQTVRWWd0aDRqODBfSEpTSnktZF9TN3Etbld5djR2UEdyMmtjWWNpeXRtMFBKX2Nlbl8xZjlYcWpfR0JRRnZfaERlUllZWWMzREdXWTNORjBJ?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 23 Nov 2026 03:32:59 GMT
- [【即時新聞】今日法人看好奇鋐液冷散熱出貨放量，第三季毛利率衝33.9%創新高！ - CMoney投資網誌](https://news.google.com/rss/articles/CBMikAFBVV95cUxPTjBpR19sU1BvM2RpUTJQN1NPS250eldvZ3VDVUpsdjdmT1FScmtqa2xpaXJqYk5BR2dvd3BMWUlFbWQtS1RwTDIwdzUxS01Ua2pWOEVES1JIWDhCNmJWTXNNN2s0V1RERmVXWXo0b2V3SHAzRW9JWTV5ODRBeHNhcElyUkZCV21NaENlMjNPb1U?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 23 Nov 2026 22:08:15 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：三大法人逆勢大賣1,230億元！台股暴漲3,310點創紀錄 自營商大砍810億元 - 經濟日報；台股盤中一度暴跌逾3,400點後強拉千點 20大權值股誰在撐？ - 經濟日報；黃仁勳利多退燒！台股一度重挫2,061點 台光電、台達電領軍守5日線 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [三大法人逆勢大賣1,230億元！台股暴漲3,310點創紀錄 自營商大砍810億元 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5ybXcyVzBzQlJKTVpLQkxwQnZDOTNTd0s4TUJGSGtVUXptYWNvTkdXaV9YM044enhzd1hqT25vM3J1a1BQT2VmSWc3WlBvaVpfRmlXbjNGbVRMZ9IBX0FVX3lxTE9QcGlZMkZYZno1c1U2cnJWRU5VYmNkVUlqNkFsWXJPX3JTUXVnMXR3UHlDS3RjNk1TczlMMHdrWHYwUlY5OGhXRU9kWUZNcUlPb3lXSUlOWGh1X29BeWZz?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 23 Nov 2026 08:00:00 GMT
- [台股盤中一度暴跌逾3,400點後強拉千點 20大權值股誰在撐？ - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1VcENOUkVRX2hQczB5UG5NemRoTWZ5SUg5cTBROHBzb1FKaE80R2JnU0RZTlhCcXVjYzJiWF9SdWRObTlwRFk1djlWeDU3NVlaR3RWN3AxeWZwd9IBX0FVX3lxTE9BR0RYUjJUdm1yeUhlZFQ5NUVFakF6Y0NHeHdOSHkwRzJFQTk2SUNGQWJNNmFqZ2RTWjJyRXY3R2VxQ1lvdW9jdzN3eF8wNV82azhfSEo5SUM3QmY0S1R3?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 24 Nov 2026 08:00:00 GMT
- [黃仁勳利多退燒！台股一度重挫2,061點 台光電、台達電領軍守5日線 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1VaVZMQ0RZUnBsTm9NcTg3aDU3RFR5d2N4OW9mOEZ6Ry1IZ1FpTFFFTHZXYUNQUmhROHRoTURqQTA5OWhtanNvaEFIbEN6TDdiR0F3NENBa3gzZ9IBX0FVX3lxTE9VYzhrYl8wQ0FMdlNRY2tabUhfSzlnNzhXYTdLRXhKUWJQdVl3QW1DQVJMaEN4YzVnTGoxbDh6UTJvZXVOMV9wemtXNFQwZm1rUUhpLU00ZUNrNlUzT1ZN?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 24 Nov 2026 08:00:00 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：國票證券：台股留意能否於五日均線附近出現止穩 - 報告 - 新聞 - MoneyDJ；統一證券：台股估震盪築底- 新聞 - MoneyDJ；「主動施羅德AI台股」11/26起上市買賣，並得辦理融資融券- 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [國票證券：台股留意能否於五日均線附近出現止穩 - 報告 - 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMihwFBVV95cUxNR1lpNURiZmVtcE0zbjBpa1d3TkN2dUlrcjlSaEpCWWQtbUc0TjBtZ1cwX0JlOHhvMjE2dFFmQjRHMGdGYzFXcHpEZFFGVGdOQ0lMdzhXcFpmcFZ6TF91dmp5WEQ3OEF1UlJtckk3V1FkUG5jdFJaeEJoQVF6bFZwRGlONkFPQ3M?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 25 Nov 2026 00:37:00 GMT
- [統一證券：台股估震盪築底- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNX3dqWXl6TER4aU9wNHJJUGFubDBkWld5VzczbWVIQk01dElxaklBUjcwWE5mRzNOZ015T25NOVhibUtURW5QbndMMV9sTEpWYTdxOXJnZUZnTlp2REVyUXhGelB1NmljTXFyR082Uk9HWkZIdTEwU0FidnNxNzM4bkRSY0xjSlBueHZlSlBZRVRUUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 25 Nov 2026 00:37:00 GMT
- [「主動施羅德AI台股」11/26起上市買賣，並得辦理融資融券- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNMVp4c1ZDZVJTSDRmMDdYZzVTRXVja1NRdWk5Z09fR2Fzakl2bVh3eWt3TURySXFLLUkxbm5YWDI3TVlZZ1VTWUhUTjVUdlpnajk5TVlVNk5zcGtUa0V5cV8xZ3J2c3JPSDF1VXF5UExrNF92Nk1NZlBERjBuQnc1N3pvb3JPTzRiNWtiVDUwZG1sdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 25 Nov 2026 00:17:00 GMT

## 新興題材：SpaceX

摘要：新興題材：SpaceX 相關新聞集中在：馬斯克坦言 AI「競爭失利」：SpaceX 轉當算力房東，Anthropic 每月租金 31 億美元 - TechNews 科技新報；SpaceX sued by Oregon and Virginia over AI deepfake porn, Grok safety claims - CNBC

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [馬斯克坦言 AI「競爭失利」：SpaceX 轉當算力房東，Anthropic 每月租金 31 億美元 - TechNews 科技新報](https://news.google.com/rss/articles/CBMimwFBVV95cUxQRmk3QUdfdVZFRlBGa09ZY0hNdzVLdnB1YnFrcnpsTEFmbFVSWlRlV1B5ZEVmbUI2TEdZbnBmUllxOW1HQWt0eDlrNC1DNmxfSk5zVHZETlpyTWlNY2NUa2VGeVlYbGI0LWQtUWFPX0JnVkVYb20zSjFDOUVKWWNaWl92aGdBUzd5dklPbUZUU3dJLXlCV2NsclBnMA?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 25 Nov 2026 01:59:51 GMT
- [SpaceX sued by Oregon and Virginia over AI deepfake porn, Grok safety claims - CNBC](https://news.google.com/rss/articles/CBMiigFBVV95cUxQbHNWNVZoWUNJLXJxQl9wTkZnTFdZNkVTZXllR2pxSlFMeWxnS0xENDRnUXZBSENCV3lybG1tSXFfWF9xdWJiMHVxYlhWSXVkMU9lTFlFR200Qkg2eVpOR2NzRE55RXhudHRnb1QzTEZIdXFQUWl2bDRVMDVxT2FqbkNnTXJVS1J5bGfSAY8BQVVfeXFMTzdXQVNETlE0OGxPY0FSejh4THJESzBWQ0ZnV1NXRWtwUEE5T0hpbGs2SmpYMXVTdThMa1BqR2xQTTN2ZWZQb1JkZ0RfOC1KZm0yRldLX19pWWZpZUpBVGxpTXRyWF9KTW1hSUdHcENaVDlQN0QtcFdnSTJyMEl3ejNGNHRYc093blFaakhHS0k?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 23 Nov 2026 12:40:37 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
