# 每日股市熱門話題分析 - 2026-10-14

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜負向｜熱度 15｜市場確認 50.16｜同向 4/6
2. **半導體與晶片供應鏈**｜中性｜熱度 8｜市場確認 N/A｜同向 0/0
3. **散熱與液冷供應鏈**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
4. **新興題材：NorthCrest**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0
5. **AI 伺服器與資料中心**｜負向｜熱度 17｜市場確認 28.00｜同向 4/8

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.08（樣本 14）
- 5日相關係數：-0.29（樣本 9）
- 同向比例：8/14

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 50.16 | 4/6 | 2 | +1.16% | +1.31% |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：NorthCrest | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 28.00 | 4/8 | 4 | -2.33% | -0.55% |
| 新興題材：MarketBeat | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 相關性偏弱；應提高同向價格確認權重，降低泛 AI、泛半導體等寬標籤推估權重。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-10-01 | 0.21 | -0.27 | +40.00% | 20 |
| 2026-10-02 | 0.51 | 0.37 | +72.73% | 11 |
| 2026-10-03 | -0.35 | 0.13 | +16.67% | 6 |
| 2026-10-04 | -0.12 | 0.70 | +80.00% | 20 |
| 2026-10-05 | -0.16 | 0.29 | +73.33% | 15 |
| 2026-10-06 | -0.72 | -0.75 | +37.50% | 8 |
| 2026-10-07 | 0.48 | 0.61 | +73.33% | 15 |
| 2026-10-08 | 0.13 | 0.40 | +58.33% | 12 |
| 2026-10-09 | -0.03 | 0.37 | +38.89% | 18 |
| 2026-10-10 | -0.28 | -0.96 | +57.14% | 7 |
| 2026-10-11 | 0.66 | -0.74 | +40.00% | 5 |
| 2026-10-12 | -0.08 | -0.07 | +41.67% | 12 |
| 2026-10-13 | -0.05 | -0.03 | +46.67% | 15 |
| 2026-10-14 | 0.08 | -0.29 | +57.14% | 14 |

## 歷史回測摘要

- 回測日期：2026-10-14
- 近5日 3日相關：0.01
- 近5日 5日相關：-0.03
- 同向比例：+50.00%
- 權重狀態：未調整

- 方向準確度：+50.00%
- 信心排序準確度：0.01
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

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Broadcom’s AI Durability Warning Triggers Sharp Drop In SK Hynix, Samsung In Korea; Nvidia's China AI Chip Share Falls As Huawei Closes In - Yahoo Finance；Nasdaq Futures Sink, Dow Rises Premarket As AI Chip Stocks Wobble Ahead Of Big Bank Earnings: MU, SNDK, NVTS, NVDA, SPCX, ASTS, UNH, V Stocks In Focus - TradingView；INTC, AMD, MU, NVDA: Chip Stocks Tumble Again, Stalling A Nascent Rebound - Stocktwits

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | -0.59 | -1.83% | N/A | 953.19 | 1,029.00 | -7.37% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | -0.29 | +3.51% | +14.21% | 228.52 | 229.28 | -0.33% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.58 | -12.12% | -12.72% | 1,487.33 | 2,335.00 | -36.30% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.21 | +17.33% | N/A | 605.53 | 608.10 | -0.42% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | -0.43 | -10.35% | N/A | 102.81 | 114.68 | -10.35% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | -0.43 | -3.52% | -5.41% | 357.31 | 446.77 | -20.02% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron、memory」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA、NVDA」，共 3 篇新聞命中。 同時符合主題標籤：HBM。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK、SanDisk」，共 2 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。

### 主要來源

- [Broadcom’s AI Durability Warning Triggers Sharp Drop In SK Hynix, Samsung In Korea; Nvidia's China AI Chip Share Falls As Huawei Closes In - Yahoo Finance](https://news.google.com/rss/articles/CBMipwFBVV95cUxQZ3dDT2F5Ym1KZWJLZ0NmX1g1Y25GdU1xZndZM2xzN2tLMmJmTFV2bWYyQlZ6RGNMYnJzOGdZTlJmY3B6TlI2X194bHFJSmtEUXU5TUcyUDZXNDI0anJwVXB2NVdfb2J0Tm1TMTZ5SHBjZUxKQzh0eHczaEk2NVp6eXBCQWk5MnhqRURIUEFBS3NmYVFtU19DVlFmWDFQRkFBODdEZzVmNA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 13 Oct 2026 07:21:09 GMT
- [Nasdaq Futures Sink, Dow Rises Premarket As AI Chip Stocks Wobble Ahead Of Big Bank Earnings: MU, SNDK, NVTS, NVDA, SPCX, ASTS, UNH, V Stocks In Focus - TradingView](https://news.google.com/rss/articles/CBMiqgJBVV95cUxPYzdXN2JsSWEyczhnMm9HUWdqU1UteEY0MW1FMU5yNnFaTjdHb0RkMlNVcUZwRHRrVUJPM1JLZUFDekdrZEtqRVZWcV8wN1laekgtUzZXbkRmVUVhbnRKUmV3bTloekwta2ZocE9INkpoLW4yTGFWTUNWbkpzekNWMU9meENhX0k2dkdzWnBfd01zOTZZSUtid2F4N3VhQWhiX3ltSHZiYTVFNHNhcHlpcUY1YjhkZGZad0p2NjJGZThCc1Bjb2FvVXRIZ3IzRGtJMHJNc01LQ01SOHpvZU9HQUd6c1FWVjJwdVdwYk1NWFV6azE0OXRCU09uRnBkYlA2bkpWZXFqUFhpV2FmTjlKMUc2SS1IUjVCQzBqRExBLVB5bThJRDZ5ajln?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 13 Oct 2026 08:37:30 GMT
- [INTC, AMD, MU, NVDA: Chip Stocks Tumble Again, Stalling A Nascent Rebound - Stocktwits](https://news.google.com/rss/articles/CBMizAFBVV95cUxORHdiV3k3V2RtSVBoRTJaaW5PcTZhQzBTNlRUM2VqcjBpcTViNkREdS1uVGtnb1FYckxkREh4Z00zN2NBSnlNRGZ0SWhpNERydkZKTlJCejRLQ2xqejNxREhfS1ZzSm5CdjhrZzlZTnRiN1Z6M3VtSDU1d2trMG9jVFUwT3hadk93R2l0TlBBZkttekkyTDBHTW1Zc01YTmNzRVJ3Tm11dGcwNktNX04yU0pLUENBQl9sOUI4dVMydW02UUhxZDVXX2pZT0M?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 13 Oct 2026 06:51:25 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：INTC, AMD, AVGO: Chip Stocks Jump Premarket After Nvidia's Blowout Report - Stocktwits；Semiconductor Equipment Stocks Slide as Investors Take Profits on a Huge Year: Applied Materials Sinks 7%, Lam Research and KLA Drop 4% - 24/7 Wall St.；Why Are Nvidia, AMD and Intel Stocks Falling Today? AI Chip Selloff Deepens - Stocks Down Under

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +3.51% | +14.21% | 228.52 | 229.28 | -0.33% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | 0.00 | -10.35% | N/A | 102.81 | 114.68 | -10.35% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | +17.33% | N/A | 605.53 | 608.10 | -0.42% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | 0.00 | -3.68% | -3.30% | 2,490.00 | 2,550.00 | -2.35% | 不適用 | 86.28 | 28.86 | 511.86B TWD / 54.65% | 2026-10-01 |
| AVGO 博通 | 新聞直接提及 | 0.00 | -3.52% | -5.41% | 357.31 | 446.77 | -20.02% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | -4.71% | -7.21% | 141.50 | 164.50 | -13.98% | 不適用 | 6.68 | 21.28 | 25.35B TWD / 27.22% | 2026-10-01 |
| MU 美光 | 產業/供應鏈推估 | 0.00 | -1.83% | N/A | 953.19 | 1,029.00 | -7.37% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -12.12% | -12.72% | 1,487.33 | 2,335.00 | -36.30% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA、輝達」，共 3 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「INTC、Intel」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [INTC, AMD, AVGO: Chip Stocks Jump Premarket After Nvidia's Blowout Report - Stocktwits](https://news.google.com/rss/articles/CBMizwFBVV95cUxPQUU4dTZXYndUX2YwZlZ6VmR6d3JoV2dDbE1XR1FKS0p2YTZScmlIclZkTUxxb0paRW00TEgwVlE1Qk5hT3BnM3J4eVZqVDBpZ3o1blFiYTQ5M2t3OTlJU3pud01kVlJYQzFVaF82a2xfWXRfM2R2MzBVRDczX0pnRkpPZ3dpam03QlhibkliRnQ3NWhJU25VM0d1bVlvSm02bjJaV2pjZlJwTUpVVnZCMHRxYjFFd2Q2RXRNOFl3ZkItc0llS0JKR2dVN1VORDg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 13 Oct 2026 13:07:31 GMT
- [Semiconductor Equipment Stocks Slide as Investors Take Profits on a Huge Year: Applied Materials Sinks 7%, Lam Research and KLA Drop 4% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMihgJBVV95cUxOUlZuWlJCaHNsNjJNLTZ2ZUVXcGdsQkhZZDFsb25WaEUyQTZRY2VfOGJxTGE4clJGUTF4Y0U5WHpCMFV4ajZQcGhZVHo3dVRJU0hrM0NIRFhkXzlfOThEa3lVaFN4Ui0zeGJoaWhLZ3hPSk80bU9RZ0o3ZlhyTWFVV0xvdmgtTkRJaWFsMkhnQkQyZXFVZDN5SGJRSXViMmZ2NHRkbjh2YmZYeGUtemVGWC0wbi1lU1VscGJsVllkN2JzX0JRRDVIRXIwMzRuT1V3TDU1MVIydHAwbnl2UmYwcjdLQjd5eWNtN24tZDVrR0gxM0k4alF3OGtneE5sRlppcTBxLVRR?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 13 Oct 2026 16:53:00 GMT
- [Why Are Nvidia, AMD and Intel Stocks Falling Today? AI Chip Selloff Deepens - Stocks Down Under](https://news.google.com/rss/articles/CBMiekFVX3lxTFBwQjkyMXh0YndVRlJhS3FBSll4dVB4akV2TWoyclpKWEE3RXEzODUwYWxtczdwdV9PUFFLUnVfenNtSWpZWnlGRUMzbGJiVHpaOVA0WEVmQ3RzSHFOalAzWENZWFVJeW1QMWtPRDh2YnRKNkdGYzFfN2hR?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 12 Oct 2026 17:13:51 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：9月營收1次評》奇鋐、雙鴻、健策、富世達...散熱4雄誰最不推？法人1原因選它- 上市櫃 - 旺得富理財網；2027 年液冷量產時程對 AI 投資布局的意義？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | -7.48% | -8.51% | 3,280.00 | 3,440.00 | -4.65% | 不適用 | 75.13 | 43.72 | 21.02B TWD / 44.92% | 2026-10-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐」，共 1 篇新聞命中。 同時符合主題標籤：thermal。

### 主要來源

- [9月營收1次評》奇鋐、雙鴻、健策、富世達...散熱4雄誰最不推？法人1原因選它- 上市櫃 - 旺得富理財網](https://news.google.com/rss/articles/CBMiakFVX3lxTFBNUXhvVGhJVGhfaXlvbVVaaVVWeUdwTVZYVjdUdTRhdFNETEhvdmxLbjBlVWQ2bTRJZ0dsRWp1RjBiS1d6NHc1dG1ndmd3SGRINmVaUEotR2R0MXptTEtoMTcwWGl2S21QR1E?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 13 Oct 2026 22:07:16 GMT
- [2027 年液冷量產時程對 AI 投資布局的意義？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMitwFBVV95cUxQVUZkV29jejJHMGZ1blNXNGJOTkhQcTI0bk1mUUtQODV1Z3RxODkwLThJZWMyYlFKVnJlcHZ1N0VsSTFKYlpPdXJ1MFJ4cEJwU3MwVHN3QktBZFZlMk1YY0VVS2Vla3dlQkQ3dWc2eThYMXdZWFN1c3h6WDNpR2FOWldsdVVMWWU1SktkNUxLTkFMbk5xNXVZTUJJdnQ3LXVndElrek1BNkZReDV6eUJfV2p3VFBvbjA?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 13 Oct 2026 23:43:16 GMT

## 新興題材：NorthCrest

摘要：新興題材：NorthCrest 相關新聞集中在：Intel Corporation $INTC Stock: NorthCrest Asset Manangement LLC Grows Stake - MarketBeat

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | -10.35% | N/A | 102.81 | 114.68 | -10.35% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Corporation $INTC Stock: NorthCrest Asset Manangement LLC Grows Stake - MarketBeat](https://news.google.com/rss/articles/CBMizwFBVV95cUxOT3VBbzNNQ3dkNENFeENMLTJJMlJrWFc1cnZJeEtDOVpfVXpWQmFyVWVKTk9GVnZBNnJDZFhJWms2RHhibmVWWGlaaFFEWUN4UnJoWHZJODRtMGVzdG1uSW9sRU03aV9XbEQ2MEVySldWOUstOHIyeS1ySE8xLW5oNzBhR1N3b2tPTGdJaFV1NFVTSWp0ZWRnaGtUeG1RZmhDc3JZWEszTm9IVlhtS01nckhMUzBhVjJLMEN6d2lqdjcyUjhfZTVkOEhHX19qQUE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 13 Oct 2026 11:37:48 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Why Are Nvidia, AMD and Intel Stocks Falling Today? AI Chip Selloff Deepens - Stocks Down Under；AI 發展失控恐出人命，學者警告：科技巨頭「自我監管」根本不夠 - TechNews 科技新報；AI 搶料下，衛星業者如何確保電力設備供應？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | -0.29 | +3.51% | +14.21% | 228.52 | 229.28 | -0.33% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | -0.56 | -10.35% | N/A | 102.81 | 114.68 | -10.35% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.27 | +17.33% | N/A | 605.53 | 608.10 | -0.42% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.06 | -3.68% | -3.30% | 2,490.00 | 2,550.00 | -2.35% | 同向 | 86.28 | 28.86 | 511.86B TWD / 54.65% | 2026-10-01 |
| MSFT 微軟 | 產業/供應鏈推估 | -0.02 | +20.70% | +10.46% | 543.45 | 543.45 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -3.52% | -5.41% | 357.31 | 446.77 | -20.02% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.02 | +1.09% | -0.27% | 740.00 | 744.00 | -0.54% | 背離 | 13.92 | 53.55 | 88.13B TWD / 45.52% | 2026-10-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.04 | -6.41% | -12.39% | 4,525.00 | 4,920.00 | -8.03% | 同向 | 60.69 | 74.73 | 55.40B TWD / 1.97% | 2026-10-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA、輝達」，共 2 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。 方向判斷命中詞：恐。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：恐。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。 方向判斷命中詞：恐。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Why Are Nvidia, AMD and Intel Stocks Falling Today? AI Chip Selloff Deepens - Stocks Down Under](https://news.google.com/rss/articles/CBMiekFVX3lxTFBwQjkyMXh0YndVRlJhS3FBSll4dVB4akV2TWoyclpKWEE3RXEzODUwYWxtczdwdV9PUFFLUnVfenNtSWpZWnlGRUMzbGJiVHpaOVA0WEVmQ3RzSHFOalAzWENZWFVJeW1QMWtPRDh2YnRKNkdGYzFfN2hR?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 12 Oct 2026 17:13:51 GMT
- [AI 發展失控恐出人命，學者警告：科技巨頭「自我監管」根本不夠 - TechNews 科技新報](https://news.google.com/rss/articles/CBMitgFBVV95cUxPemxmMnZSYlBzNE5kek9OZFBodDluRnNtemo1SE85cklNUnlkN0tzMm1qaTNPSWFHN2lZa19lTzFLaUpHMTdHT011bVp6a2RjRE01czE5aG85MDVscWkwTFhvcnRfeFJlZExheWhoZTE0NWJ6N1ZZS0Rsb2RqRk9YdDBZTWk4UzZHOFlHdGtWUFVHSzNMQkJuUHVsTHZyUXY5bTNHVVN6S184RVBzZ05Va1REWTY0Zw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 13 Oct 2026 23:24:13 GMT
- [AI 搶料下，衛星業者如何確保電力設備供應？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMic0FVX3lxTE4zMEJIMmI5TnBmYVdkekw2SmlHaVpMMVhCaTRSMmxMcnpoOFVidXNOcEpPbExFX1RBbThFOTlPTXhhYzJJX083eUkyTzhwczlkLW5jMm9IZm5LMkVDTndaTUdFRmNWUEVpVlR2MURtOExxZE0?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 13 Oct 2026 22:31:23 GMT

## 新興題材：MarketBeat

摘要：新興題材：MarketBeat 相關新聞集中在：Intel Corporation $INTC Stock: NorthCrest Asset Manangement LLC Grows Stake - MarketBeat

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | -10.35% | N/A | 102.81 | 114.68 | -10.35% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Corporation $INTC Stock: NorthCrest Asset Manangement LLC Grows Stake - MarketBeat](https://news.google.com/rss/articles/CBMizwFBVV95cUxOT3VBbzNNQ3dkNENFeENMLTJJMlJrWFc1cnZJeEtDOVpfVXpWQmFyVWVKTk9GVnZBNnJDZFhJWms2RHhibmVWWGlaaFFEWUN4UnJoWHZJODRtMGVzdG1uSW9sRU03aV9XbEQ2MEVySldWOUstOHIyeS1ySE8xLW5oNzBhR1N3b2tPTGdJaFV1NFVTSWp0ZWRnaGtUeG1RZmhDc3JZWEszTm9IVlhtS01nckhMUzBhVjJLMEN6d2lqdjcyUjhfZTVkOEhHX19qQUE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 13 Oct 2026 11:37:48 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台指期夜盤上揚　法人：台股可望回穩 - 經濟日報；台股多頭回歸 要看四要素 - 經濟日報；外資大撤退 股匯遇亂流 台股公股救援 單日買超412億元 寫次高紀錄 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台指期夜盤上揚　法人：台股可望回穩 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxQdFBDNGNrTjRwVm1qMHRzRjI2WWhvUDdhUmM1VW1McjJWaUlyUm5lWGhNdmtrZ0FERFR5bGxSdm9pdGY4WFRzM1QyVERVeHUwSm91bmhuSkhNQlZoT3J2UXBhZ2xRcFpBUjJOb1UzbG15Q2FnenVLRk00bldhbUdnV9IBX0FVX3lxTE9iR1ZTcUoxdkdtVlpUel8zbmRvUkRKRmJlRDRkM2VOZ1F1cm9DNUJiV3c1ejZ6Rk0zRXFYb2I2VHB5NW90ekVzcFZpSUJva3FZbC1UQ1FIcERVT194SEM0?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 14 Oct 2026 00:30:30 GMT
- [台股多頭回歸 要看四要素 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxPWW9ETGM1UXZidTlqVFJtaXJQVnc3QkFqZWtfOFRYWVhMaGJ4RFRqaTE4XzFETTdMVzVjUnItay0xcVVZMHVraHVPRTU2TmRSc1VkNmx0N2lyMHNTbzM5UDNrUF9NZnR0dmVoemtnVmFsdWR4TWpYN1FzcEo3ZnhVedIBX0FVX3lxTE9LMU9pSUJlQm9ZclJ5V0taek5US24zOU5FN29DZ3lUaTNDdDBvWnRwdThzNm96LXQ0cUlsMEFRN1o1bkFEOWl5SDhiMzlkQ0Vpd1FiR01BeUswOEE1RlRZ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 13 Oct 2026 18:56:00 GMT
- [外資大撤退 股匯遇亂流 台股公股救援 單日買超412億元 寫次高紀錄 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE16blZTa0FtcF9WcU5KVE42U2poMDJjZ01IT1IyQ1J2UXFfVFQzN2xvRGdFLVA0OUpVbU9ZRzFNNm8waFNpNTNuUm9pWkoya2RjZ2ZJS0hlQnlyZ9IBX0FVX3lxTE5EVkpyR0VkSHlLN0tGMHk1bXRINFpSX3J0MHIweHBFU0NKRzY4NXhra1B2Q1pqTWs3ZEJBUDJTWVB2Y1hhS3JSME1GSGhDbVRTTy12VlU3c0NuWWViZ0sw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 13 Oct 2026 17:44:51 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》量增收跌960點/退守48K 外資賣超1653億 - MoneyDJ；法人盤勢分析內容-台股-MoneyDJ理財網 - MoneyDJ；統一證券：台股技術面呈現漲多震檔整理格局- 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》量增收跌960點/退守48K 外資賣超1653億 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPTDB2clplSnd1Zm1GQ3NkZlVvUUJLcFNhU3ZobjlNRzQwcDNIVk15bElBUzY0R1VPVUVqaklObWt4clZBUnRPZHA0VGtqakJ3XzdhNGZteVJnMmdxajlxY3lKakRzT0M0dlNFN3Z2VHNtSThZQ0tKZG9ydEdFSHhOZDBpOU1YVjEyUEozZk1GMVNWUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 13 Oct 2026 08:16:00 GMT
- [法人盤勢分析內容-台股-MoneyDJ理財網 - MoneyDJ](https://news.google.com/rss/articles/CBMijgFBVV95cUxQUzBPWU1zZFhNcHJrVWJOZ2h5TjRuc3hpZFZEQk9odGpmamZVWUsybWNQYkI0S0tYOVRrd21OLWZnV1RIcThOVXpXdkVRWnlDa2FJZVFEQTZkNmx5SUtlUjlNdmR6ZEFkbzdkMUhNcFprbE9hMEVpM0hZRldPZDF3OFR2UDdMRC1Zenpocjh3?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 13 Oct 2026 23:57:08 GMT
- [統一證券：台股技術面呈現漲多震檔整理格局- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPYkJ6aFdDYWFXbEZWN2htYWtMQy1MdHlIcUI4bFJjTXlGXzZuQ3dIWXlhdlFXa2lwM3dFWjZzTF9GZHA5cVR1ZlpTblhyRnpvSVZxZmhiS0RmSXFEbXNObmU1QjFDRU1zdGRrRDRlVzZmc0pZcnlTX1pXeHYzUW1HaHgxSXhTb05RbVRpbGlNNFJfdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 13 Oct 2026 00:38:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
