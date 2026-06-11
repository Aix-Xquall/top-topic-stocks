# 每日股市熱門話題分析 - 2026-06-12

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜中性｜熱度 7｜市場確認 N/A｜同向 0/0
2. **AI 伺服器與資料中心**｜中性｜熱度 11｜市場確認 N/A｜同向 0/0
3. **半導體與晶片供應鏈**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0
4. **先進封裝與 CoPoS**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
5. **新興題材：OpenAI**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：N/A（樣本 0）
- 5日相關係數：N/A（樣本 0）
- 同向比例：0/0

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 先進封裝與 CoPoS | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：OpenAI | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：BofA | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：5年來台指期首度觸及跌停 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-05-29 | 0.14 | -0.04 | +71.43% | 7 |
| 2026-05-30 | 0.16 | -0.06 | +71.43% | 7 |
| 2026-05-31 | 0.96 | 0.09 | +100.00% | 3 |
| 2026-06-01 | -0.92 | -0.72 | +16.67% | 6 |
| 2026-06-02 | 0.08 | 0.05 | +72.73% | 11 |
| 2026-06-03 | 0.48 | 0.62 | +90.91% | 11 |
| 2026-06-04 | -0.38 | -0.30 | +85.71% | 7 |
| 2026-06-05 | 0.31 | 0.93 | +50.00% | 6 |
| 2026-06-06 | 0.12 | 0.06 | +45.45% | 11 |
| 2026-06-07 | -0.32 | -0.20 | +45.45% | 11 |
| 2026-06-08 | 0.36 | -0.68 | +60.00% | 5 |
| 2026-06-09 | 0.07 | 0.19 | +25.00% | 8 |
| 2026-06-10 | 0.17 | 0.15 | +53.85% | 13 |
| 2026-06-11 | -0.05 | -0.08 | +14.29% | 7 |

## 歷史回測摘要

- 回測日期：2026-06-12
- 近5日 3日相關：-0.25
- 近5日 5日相關：-0.32
- 同向比例：+33.33%
- 權重狀態：未調整

- 方向準確度：+33.33%
- 信心排序準確度：-0.25
- 診斷：方向與信心皆需修正

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

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Beyond Micron: 2 AI Stocks That Could Deliver Explosive Returns - TradingView；Move Over, Magnificent 7. Traders Are Flocking to SanDisk, Marvell, Micron, and the Parabolic 7 - AOL.com；SanDisk (SNDK) Is Doing Something Unprecedented In The Al Sector! SNDK STOCK PODCAST ANALYSIS BUY Jobe Bellingham (gRMiCAoJ7a) - Mshale

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 995.87 | 995.87 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | +14.59% | +6.92% | 1,881.51 | 1,881.51 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 116.96 | 116.96 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +2.66% | +15.62% | 204.87 | 211.14 | -2.97% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、MU」，共 4 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk、SNDK」，共 4 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Beyond Micron: 2 AI Stocks That Could Deliver Explosive Returns - TradingView](https://news.google.com/rss/articles/CBMiugFBVV95cUxObkFwUWVEVE9iZUxvbmZBZUpXSVFIYkJBYktIQkR4YURnRW5qVHpidVpweUR1TzkwVDh0VmxyaFloa1VYRGNhTmFTRmRCaE5xWGQ1b0I4Zm5KdTBwQXV5bjdTcVYyMHFxNE9FRWUxZWJVZDRYOHVpOG12WUpEMHExcUNsQkZJd2xuNldvLWRTWUdNZGlGbzhPZUtUaS00TkRJTmFyQTV2WHp6dFNyaE9naERpdGp5a0FzSmc?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 11 Jun 2026 19:00:00 GMT
- [Move Over, Magnificent 7. Traders Are Flocking to SanDisk, Marvell, Micron, and the Parabolic 7 - AOL.com](https://news.google.com/rss/articles/CBMigAFBVV95cUxNZVE3dk5LajR1STJYQVdFN3diMWFSMkpVQ2xEZ29acVBDZFJ2RGkwalMwZmxSOW1mRWo4OE54TDNyNzVJWGJrRXNJc2VjaTREdU5aVWN6eWlpZ0NIU1B6dmpOX0ZEcEoxdlk4VTc4TzRrS0pQb3JQN09IaG5LbHo0Tg?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 11 Jun 2026 18:51:15 GMT
- [SanDisk (SNDK) Is Doing Something Unprecedented In The Al Sector! SNDK STOCK PODCAST ANALYSIS BUY Jobe Bellingham (gRMiCAoJ7a) - Mshale](https://news.google.com/rss/articles/CBMiW0FVX3lxTE82c25ZNkhMbnBFcHlYZktjT2gzRlFzREd4ZFlubTJYeG4zZFJ6NU1OdGxaX3BRYWM0bFdDWk5tMlNVS3BvWXRLZW1jUVp3SUdNYXlKam5zNEhNVm8?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 10 Jun 2026 20:36:40 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel Jumps 8%, AMD Rises 4% on Bank of America’s $170 Billion Server-CPU Call - 24/7 Wall St.；台灣 PCB 業人才缺口達 61%，如何透過產學合作解決 AI 規模化困境？ - TechNews 科技新報；AI 安全責任歸屬應如何界定以避免法律爭議？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +2.66% | +15.62% | 204.87 | 211.14 | -2.97% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 116.96 | 116.96 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | N/A | N/A | 488.45 | 516.10 | -5.36% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -1.96% | -5.66% | 2,250.00 | 2,355.00 | -4.46% | 不適用 | 74.39 | 30.25 | 416.98B TWD / 30.09% | 2026-06-01 |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | -0.61% | -22.96% | 390.34 | 506.69 | -22.96% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -7.63% | +20.66% | 385.57 | 446.77 | -13.70% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | +0.74% | -8.26% | 544.00 | 611.00 | -10.97% | 不適用 | 10.86 | 50.51 | 63.03B TWD / 28.57% | 2026-06-01 |
| 2454 聯發科 | 產業/供應鏈推估 | 0.00 | +0.37% | -7.79% | 4,085.00 | 4,310.00 | -5.22% | 不適用 | 62.91 | 65.10 | 47.43B TWD / 4.99% | 2026-06-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Jumps 8%, AMD Rises 4% on Bank of America’s $170 Billion Server-CPU Call - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiuAFBVV95cUxPMXpqbktndWpWVjBrekV0SS1LU3RBaTZkOUZ6Y0VTN1VLOFVRYzhodnBvWVlDWFFULURYekN5a01teFB0eEpYNGZWby02TUg4TjBRcmNNRDRtbENRX0otY0pJMC1IcGF6Skg3TllEZF9rT29UYXlnVHZkWkZsdGcyWE1uTFlkVEhKZktNSlRqUUo3S080bVltTVpFQUZEd1A5c0RpUV9iZkxKZkV5NmU5S3hQWXJwbzJX?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 11 Jun 2026 14:18:37 GMT
- [台灣 PCB 業人才缺口達 61%，如何透過產學合作解決 AI 規模化困境？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiiAFBVV95cUxOcnl5bklkdW9VRk1zbGNhTi1qN1BWVU04TUQ4SFhaTGJfWnUtY0wyZm5Sa2FBOWgxaGxQNmJPckN3QXptaVphSU9uZmk4SEdNSUlhc19Mcll1VkNubGtpN3VCZlJOZG0xUEVOcEgwYlQ5RERuNFprWHgwLW1iaHNEWTB6S3BMTmVf?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 11 Jun 2026 22:24:15 GMT
- [AI 安全責任歸屬應如何界定以避免法律爭議？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMisgFBVV95cUxOajN1YlVlckJ4QW5HdVpPUmNzUlFKS21RRFEtSkNKX05zb3hJOUpmZzRvZmdzejhHaHlVbFFVbFZTMEc2bVVhTVdSbjJKUWZvOEcyYlF1OE5QRVUwWHZzRWl3Q1VPeE1jNnI4amVMVjcyMGJQRHFpZFk4aTdGeGFlRFZGbDUxUjlvcEVKbnZPTUhnc19aS21hcnBVSGpUeFpsOXZ3ZHUxR1JsRkQwWkh0aXlR?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 11 Jun 2026 19:34:32 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel Jumps 8%, AMD Rises 4% on Bank of America’s $170 Billion Server-CPU Call - 24/7 Wall St.；大葉大學解鎖半導體隱藏關卡AI神隊友助力| 樂活情報 - 中央社 CNA；Oracle shares tumble on earnings. But there's a silver lining for our AI chip and power stocks - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 116.96 | 116.96 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | N/A | N/A | 488.45 | 516.10 | -5.36% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -1.96% | -5.66% | 2,250.00 | 2,355.00 | -4.46% | 不適用 | 74.39 | 30.25 | 416.98B TWD / 30.09% | 2026-06-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +3.31% | 0.00% | 125.00 | 144.50 | -13.49% | 不適用 | 4.00 | 31.41 | 22.94B TWD / 17.78% | 2026-06-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +2.66% | +15.62% | 204.87 | 211.14 | -2.97% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 995.87 | 995.87 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | +14.59% | +6.92% | 1,881.51 | 1,881.51 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -7.63% | +20.66% | 385.57 | 446.77 | -13.70% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 1 篇新聞出現相關標籤。

### 主要來源

- [Intel Jumps 8%, AMD Rises 4% on Bank of America’s $170 Billion Server-CPU Call - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiuAFBVV95cUxPMXpqbktndWpWVjBrekV0SS1LU3RBaTZkOUZ6Y0VTN1VLOFVRYzhodnBvWVlDWFFULURYekN5a01teFB0eEpYNGZWby02TUg4TjBRcmNNRDRtbENRX0otY0pJMC1IcGF6Skg3TllEZF9rT29UYXlnVHZkWkZsdGcyWE1uTFlkVEhKZktNSlRqUUo3S080bVltTVpFQUZEd1A5c0RpUV9iZkxKZkV5NmU5S3hQWXJwbzJX?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 11 Jun 2026 14:18:37 GMT
- [大葉大學解鎖半導體隱藏關卡AI神隊友助力| 樂活情報 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTFBwSzFHbHhRbUFKN01ZczRNenUyUDhtRTdINEpjRW5DdnAwS24zLS1CaXh1OF9xX2wtNjZCeENHdEpCSXhsblNHS0ZzZDdBTEV5cnZtQjBhb2pVd08tZmc?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 11 Jun 2026 11:23:00 GMT
- [Oracle shares tumble on earnings. But there's a silver lining for our AI chip and power stocks - CNBC](https://news.google.com/rss/articles/CBMiyAFBVV95cUxOTUotWWtENVFySVlLTzhoZllPMG0yclliQk5jenpGTnNQTVZDMWIwRUVRQ0lUMEFMM1R4aFJZQlBsbTh3OXZmSzlJUWhhaWJnSFpQdG9pNXU4SDJ4MnhBWUY5Wnp6d0JHMzRLcUVTM2lRanQtTlZJM2M5cTdjYklxMkUtWjRrYjRGOFRiTkFtN29hT0RiMGtnMmlGX0dLQjJnSF9QVzNET1Z1c3RycjR3YTB2QmVPYm5nbURlM3paQkUteHlQLVlnWA?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 11 Jun 2026 16:51:27 GMT

## 先進封裝與 CoPoS

摘要：先進封裝與 CoPoS 相關新聞集中在：供應鏈已提供產品與耗材，台積電 CoPoS 先進封裝進入核心測試階段 - TechNews 科技新報；是晶圓代工，還是先進封裝？Google 下單英特爾 300 萬顆晶片消息引爭議 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | 0.00 | -1.96% | -5.66% | 2,250.00 | 2,355.00 | -4.46% | 不適用 | 74.39 | 30.25 | 416.98B TWD / 30.09% | 2026-06-01 |
| 3711 日月光投控 | 新聞直接提及 | 0.00 | +0.74% | -8.26% | 544.00 | 611.00 | -10.97% | 不適用 | 10.86 | 50.51 | 63.03B TWD / 28.57% | 2026-06-01 |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 116.96 | 116.96 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 同時符合主題標籤：advanced packaging, CoWoS, CoPoS, FOPLP。
- 3711：新聞直接提及「CoPoS」，共 1 篇新聞命中。 同時符合主題標籤：advanced packaging, CoPoS, FOPLP, panel-level packaging。
- INTC：新聞直接提及「英特爾」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [供應鏈已提供產品與耗材，台積電 CoPoS 先進封裝進入核心測試階段 - TechNews 科技新報](https://news.google.com/rss/articles/CBMikgFBVV95cUxOQWc3b296RThvUnF0bFdhcDRlTTFRd1lDdF9FMENYQnozdEU0LWp4ajFNMFU1WmwtdnJhdERHN3hBajM2dkl2UmF2WjZMUzBNWTR4dUJzLWZIVUVWMWp5V0Vva3AtNHBHd3NyVUExN0dMV2lFS0RhQzVHU0o2LS1PMERRV1V2dWNPMkMwOG1qTUpKdw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 10 Jun 2026 01:01:59 GMT
- [是晶圓代工，還是先進封裝？Google 下單英特爾 300 萬顆晶片消息引爭議 - TechNews 科技新報](https://news.google.com/rss/articles/CBMilwFBVV95cUxNbEhOMnpmU2QzdWRsOXlaMzdNTnMxQmpLYjVYb09mQ005M0xxU1NobmFwVUZTQkpZdGFqckNMNElReDU1ZnRsdVFZZXgxMUNMYUZPZmFhVXdSWThGWXFILV9pVTNVamtFWDRWV2lZTGkwMnVYRHNxc3ljNi0yMGJLSHRLT0FzVFZPTmZuMjZGWUtCdjJoQjc4?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 10 Jun 2026 03:47:02 GMT

## 新興題材：OpenAI

摘要：新興題材：OpenAI 相關新聞集中在：Anthropic v. OpenAI: Behind the bitter battle for the future of AI - Reuters；OpenAI to acquire Ona to support its AI coding assistant, Codex - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 新聞直接提及 | 0.00 | -0.61% | -22.96% | 390.34 | 506.69 | -22.96% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：新聞直接提及「OpenAI」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Anthropic v. OpenAI: Behind the bitter battle for the future of AI - Reuters](https://news.google.com/rss/articles/CBMiqAFBVV95cUxNUk5nUHlsdmNnT25PcUpTYUFLYS1FSHl3bmdpRE0wN0NfSzBSd3FRdkVtT1VPSE55bmJnczN3aGFmRUlyTmhPVlRJYlhHOElpZGl2X0hpMW1iZU0yMVJOZHhjaVU3RXVWa19xUTJTY2c4T2JUNmhRXzRVMUdsdXgtTVFhRG9yd1FQSU03SVN2ZjhnQ0I3RWdPZEh4aEVVSDc3RTdndzV2VWY?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 11 Jun 2026 17:18:17 GMT
- [OpenAI to acquire Ona to support its AI coding assistant, Codex - CNBC](https://news.google.com/rss/articles/CBMidEFVX3lxTE55b0NuQ2NnRUxsRnl1MlBBX2pFNUIzSll5WEVHN3V0TzRIT01RQ0dEbDlGLWVaWXdaaHRybmJjb25URHB6cDl1bmlOcTA4dGg2c2xqSjhHaVZSMXFKSTRvR0hacWNkeFN0aWNzVVl6Z0V2d0Np0gF6QVVfeXFMTXBKWlVVckZnRFlrcE42SWlkTnROWTBwSnpRRjZHTnU3WktnbkQwZ1VIekNXVmVINE8yR3VWNzh1cVFxdGRtNnNETG1WZF84elJLTUNrc2ZFNWN1dXlpcUN6LTV2dFFHdVZJZXltQ0stRTZwOXBzdEl2cFE?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 11 Jun 2026 16:26:10 GMT

## 新興題材：BofA

摘要：新興題材：BofA 相關新聞集中在：AMD, ARM, INTC, NVDA Get A Fresh AI Tailwind - BofA Sees Agentic AI Expanding Server CPU Market To $170B - TradingView

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +2.66% | +15.62% | 204.87 | 211.14 | -2.97% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | N/A | N/A | 488.45 | 516.10 | -5.36% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 116.96 | 116.96 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVDA」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AMD, ARM, INTC, NVDA Get A Fresh AI Tailwind - BofA Sees Agentic AI Expanding Server CPU Market To $170B - TradingView](https://news.google.com/rss/articles/CBMi8AFBVV95cUxNQUs4cEJDckJoQzBmNmNPX3JwYzhCeXhVTmZvdVlpZVVra3JBeld6WHVBeUk3WmVrRWJxeXFIR0hCeWNuUlByQThTZEVONHJwc2ZEeTg3ajNJNjcyY1A5U2hESWVTa1Q5R1lENFNSaXdCR2V6SG1WZTQ1bTdqb2NXdDFoV040aFhvWHBQOE91TEZra0QxSVpadi1BNkI5RzBqbC1STzVzeWJMUU5nc25RWGN5ODlycVlSWE1Nb0UxZVhfc2NGNnYyamNNTVFwQ2ZKalVlT05tN29WRDF5M0hodmpaaVBxRjZCVkhfZ0t1M28?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 11 Jun 2026 12:32:32 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：《台股盤後》盤中V轉、收跌76點，險守43K-新聞內容-基金 - MoneyDJ理財網；台股強勁漲勢助5月證交稅首破700億大關- 新聞 - MoneyDJ理財網；【台股操盤人筆記】在籌碼雜亂中回歸初心 - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》盤中V轉、收跌76點，險守43K-新聞內容-基金 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMimAFBVV95cUxNTUFTMzBlYW1ocUFIb1pUQnViRlNLbnBJRnU3NkZCQ28wYTVaRmlzLVhDVHVVbVNLNFBVWWdOdE5qVVJlMWNBTzdId1QyUVFJTV9zU2FUaEFuOTZDRjFRLTdLR1RQUmZ2c3M0UElNVEljbjdtMENxa2ppOVpOZ1VqVXZZWnA4bHhtQWI3Y2x3MndhZTVrRXpFTQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 11 Jun 2026 08:11:00 GMT
- [台股強勁漲勢助5月證交稅首破700億大關- 新聞 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikgFBVV95cUxQek9jeGh3bHhrXzFiZkx1cVZiUTk2Qnh1dWNQVklHVnVLR2p2alBKSDE4anZVWXdYUnhUMVVFVG45YmdWR1VVZXVDV3dMOFktc2dPVU9BdGlKTGttdzRZeGh5dWdKTk5WaTlqYzRVeDVJUnVYTEp4eG1mTlUyQ1dPY0dqUmpQV012dDk2ZlpMOEhPQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 11 Jun 2026 09:18:00 GMT
- [【台股操盤人筆記】在籌碼雜亂中回歸初心 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilwFBVV95cUxOWkgzSWFvaVBSeG9pQ3R5TU5kX3lHdE5UU3pZUDhIdXI2bE5EVGJaR2dMYW42RHN0T3h4UG5nRW1uWEdpMnlGdVlCX0dMN0hHQ1lPY3d3NUdTTHJyM2Rwd2JGdGwweE5Jd2dUbDVWbFR5VVZzdDlZUm9Kek1uNlR1QlhWRVJZa1N0aTVoWUFQaW5uUVU4OWdF?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 11 Jun 2026 01:47:00 GMT

## 新興題材：5年來台指期首度觸及跌停

摘要：新興題材：5年來台指期首度觸及跌停 相關新聞集中在：5年來台指期首度觸及跌停，現在台股還能抱波段嗎？ | 個人理財 | 理財 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [5年來台指期首度觸及跌停，現在台股還能抱波段嗎？ | 個人理財 | 理財 - 經濟日報](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBBRHhkUjh2UF92Z2VGbGVoNFAzSXJ0OU5GQnNzRE56Z3ZxUVYxNlg1ZXNSS2JBTEpvTkJ5UjV5MFZwa3ZteVNad1RUYW1LclExckpkcTJWUVNFeTg?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 11 Jun 2026 12:24:44 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
