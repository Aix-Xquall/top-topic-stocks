# 每日股市熱門話題分析 - 2026-08-01

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **綜合市場情緒**｜正向｜熱度 41｜市場確認 89.08｜同向 1/1
2. **記憶體與 HBM 供應鏈**｜正向｜熱度 7｜市場確認 100.00｜同向 2/2
3. **新興題材：TradingKey**｜正向｜熱度 1｜市場確認 100.00｜同向 1/1
4. **半導體與晶片供應鏈**｜中性｜熱度 6｜市場確認 N/A｜同向 0/0
5. **新興題材：MarketBeat**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.38（樣本 11）
- 5日相關係數：0.25（樣本 11）
- 同向比例：6/11

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 綜合市場情緒 | 89.08 | 1/1 | 0 | +6.36% | +3.19% |
| 記憶體與 HBM 供應鏈 | 100.00 | 2/2 | 0 | +13.88% | +8.82% |
| 新興題材：TradingKey | 100.00 | 1/1 | 0 | +16.93% | +33.07% |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MarketBeat | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 16.17 | 2/6 | 3 | -2.39% | -3.52% |
| 散熱與液冷供應鏈 | 0.00 | 0/1 | 1 | -3.57% | +2.52% |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-07-19 | 0.37 | 0.09 | +12.50% | 16 |
| 2026-07-20 | -0.59 | 0.11 | +45.45% | 11 |
| 2026-07-21 | -0.12 | -0.03 | +12.50% | 8 |
| 2026-07-22 | -0.33 | -0.15 | +16.67% | 6 |
| 2026-07-23 | -0.01 | 0.01 | +41.67% | 12 |
| 2026-07-24 | -0.16 | 0.43 | +50.00% | 6 |
| 2026-07-25 | 0.30 | -0.06 | +12.50% | 16 |
| 2026-07-26 | 0.38 | 0.06 | +23.53% | 17 |
| 2026-07-27 | 0.54 | 0.11 | +37.50% | 8 |
| 2026-07-28 | 0.32 | 0.13 | +36.36% | 11 |
| 2026-07-29 | 0.16 | -0.03 | +92.31% | 13 |
| 2026-07-30 | 0.25 | 0.92 | +66.67% | 6 |
| 2026-07-31 | 0.10 | -0.10 | +46.15% | 13 |
| 2026-08-01 | 0.38 | 0.25 | +54.55% | 11 |

## 歷史回測摘要

- 回測日期：2026-08-01
- 近5日 3日相關：N/A
- 近5日 5日相關：N/A
- 同向比例：N/A
- 權重狀態：未調整

- 方向準確度：N/A
- 信心排序準確度：N/A
- 診斷：樣本不足

調整原因：近 5 日有效樣本 0 筆，低於 15 筆門檻，暫不調整權重。

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

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：自營商還在賣！三大法人終止連3賣、回補847億元 台股飆史上最大漲點 - 經濟日報；台股單日衝破四大關卡！台積電攻漲停 大盤終場飆3,186點寫歷史神蹟 - 經濟日報；台股融資減肥 醞釀反彈 台指期夜盤一度勁揚千點 市場氣氛好轉 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | +0.42 | +6.36% | +3.19% | 2,205.00 | 2,410.00 | -8.51% | 同向 | 74.39 | 32.60 | 442.68B TWD / 67.87% | 2026-07-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 方向判斷命中詞：漲停。

### 主要來源

- [自營商還在賣！三大法人終止連3賣、回補847億元 台股飆史上最大漲點 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1uOWE4Q0J0SnRLSnVVTkRlR1ZyNEV1b1dJa0VjVG1LU3VpQ2s4T1BFZkJvX1BjTVA3YXVEYWd4MHZDOXRxRnlGT3A0MlUtUjNGaWdCWU5HRmtJUdIBX0FVX3lxTE9Ib0tCcGJKQmxBaTNDdFlrWUV5R3RMa2J6NWtKcHg2OUlSaTBKcE9rbWdDMEFscFhJUGgzaE9rU0doTXJ2SXdVeVlib21tdVVXNnRyajRwNlRmWEY1UHkw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 30 Jul 2026 09:00:00 GMT
- [台股單日衝破四大關卡！台積電攻漲停 大盤終場飆3,186點寫歷史神蹟 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9BbnYtYlJIQUJSeUZJVm9wYkdZdVY0RXRVTUprcExQV2w1M3JLcHZ1TjltSlBiamRhWWtlV0d3STRyUExqZXJuYUZDZzVFN0laSnNUS1NZcU5Kd9IBX0FVX3lxTE9mTTVycUVRSVVpVVVSaTdoOFk2LVN2eFQ0SkF3STB3aFhjRS0wWWhJTzNvX24xckt4blJzZVg4RXE4QUpjM2ItRjgzN1RaX0RLenZKV2xsRk5SaV9td2pz?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 30 Jul 2026 09:00:00 GMT
- [台股融資減肥 醞釀反彈 台指期夜盤一度勁揚千點 市場氣氛好轉 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1jMi1wOFpLU1ZlTE1XWHpkS1c5SjdxSG0tU3NlZThqcEMxMEtFeFdyUHJXYmdOLXNTcTl6aUdwQi1mdVplaFMydlZzZU5PYUZEc3Q3ZDczZjIwZ9IBX0FVX3lxTFA0NVM2NlpsY014ZUxDTGhBYmV1NVB0SXc0TEl2WTRpNlBicWlzaW9DempjSUFaUEVzZ3dvMlAwd1phMGZuZlQ2Y3NGdWM3UmY4MUpEbUZaQzF6cWctazk4?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 30 Jul 2026 17:24:19 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：【US Pre-Market】Three Major Indices Rise as Amazon Gains Over 12%, Chip Stocks Including Micron, Intel and AMD Rally as Apple Slumps - TradingKey；SanDisk Is Down 45% in a Month. Should Memory Investors Switch to Micron or SK Hynix Now? - 24/7 Wall St.；Prediction: Micron and Sandisk Stocks Will Both Plummet After July 30 - AOL.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.48 | N/A | N/A | 823.03 | 971.00 | -15.24% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.48 | +10.83% | -15.43% | 1,214.83 | 2,335.00 | -47.97% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.36 | N/A | N/A | 476.15 | 516.10 | -7.74% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.36 | N/A | N/A | 90.20 | 114.68 | -21.35% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 新聞直接提及 | +0.36 | +16.93% | +33.07% | 308.91 | 333.43 | -7.35% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -4.92% | +15.11% | 200.75 | 211.14 | -4.92% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 5 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [【US Pre-Market】Three Major Indices Rise as Amazon Gains Over 12%, Chip Stocks Including Micron, Intel and AMD Rally as Apple Slumps - TradingKey](https://news.google.com/rss/articles/CBMi3gFBVV95cUxNWS04RGZ6aV8xYlFjRzRmYUdYTURyakV0QWg0U0t6S0V2U21RbHNrZktIcF9FRkFENXZRVWR2Ul9yeGJVSEprVjVBcXg5TFJIekpVU2VGREtzU1ZRSk1SUzhtNXRqbjluQVlndWlva3c3R0M5NFF3Wjh1OTcxX0xRRlAyQWVqWjM5TTFkdXdVNGoxNGZCWE5DNWd3d19ieDNUT09WanhuRGxsY3ZoMGljdy1iZmFRbFBfWmhMOVYxajdzVjIxc1N5aVFHQzUtQ1RZODhJWG52djEzQV83ZkE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 31 Jul 2026 12:05:00 GMT
- [SanDisk Is Down 45% in a Month. Should Memory Investors Switch to Micron or SK Hynix Now? - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiygFBVV95cUxOdkJEbzNjLVdmZWM0dzRPdElVRlg5NmZ3QklCOFZ6Q0pxbmcwM2ltM1MtbGZCUWgwbEFhTUNkclRZQi1GMUstNUcxN3NBeWpYNUFqOWRxWlo2UDU5OUNlTl96Wl9tWmZCVDJDRzdSYnhtaEhnZjBPUUdhWHZ3amdxY1FEeHpTdS1URmV3cjRYN0Q4QjAwYXRJUjQ0RERxN2FaSFZCNWVmaFltNDZLZFRieHVlSTdzYlE5WDdMX2k0ZGRlaVNIaVZpR0Vn?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 31 Jul 2026 18:36:06 GMT
- [Prediction: Micron and Sandisk Stocks Will Both Plummet After July 30 - AOL.com](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPd3FPNU9EQ0NyQW5nSmVVTDQtbnhHNjd5MmhXaDk3eE5LRUFYR0tNRkNUNDBGZ3A0NnFlRHdXSFF0TnJoa3VxbUVxM3hEMDZyaVpRZl95ek1sYW93QmktdGFiWHloODVTY1Q5ZnpSZEswUVpiMXA0S2ROSmtMaDdGRkExY2xqWXE5?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 31 Jul 2026 09:28:48 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：【US Pre-Market】Three Major Indices Rise as Amazon Gains Over 12%, Chip Stocks Including Micron, Intel and AMD Rally as Apple Slumps - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AMD 超微 | 新聞直接提及 | +0.42 | N/A | N/A | 476.15 | 516.10 | -7.74% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.42 | N/A | N/A | 90.20 | 114.68 | -21.35% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 新聞直接提及 | +0.42 | N/A | N/A | 823.03 | 971.00 | -15.24% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 新聞直接提及 | +0.42 | +16.93% | +33.07% | 308.91 | 333.43 | -7.35% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MU：新聞直接提及「Micron」，共 1 篇新聞命中。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [【US Pre-Market】Three Major Indices Rise as Amazon Gains Over 12%, Chip Stocks Including Micron, Intel and AMD Rally as Apple Slumps - TradingKey](https://news.google.com/rss/articles/CBMi3gFBVV95cUxNWS04RGZ6aV8xYlFjRzRmYUdYTURyakV0QWg0U0t6S0V2U21RbHNrZktIcF9FRkFENXZRVWR2Ul9yeGJVSEprVjVBcXg5TFJIekpVU2VGREtzU1ZRSk1SUzhtNXRqbjluQVlndWlva3c3R0M5NFF3Wjh1OTcxX0xRRlAyQWVqWjM5TTFkdXdVNGoxNGZCWE5DNWd3d19ieDNUT09WanhuRGxsY3ZoMGljdy1iZmFRbFBfWmhMOVYxajdzVjIxc1N5aVFHQzUtQ1RZODhJWG52djEzQV83ZkE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 31 Jul 2026 12:05:00 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel (INTC) Faces AI Supply Bottlenecks As Omdia Sees 94.1% Chip Revenue Jump - simplywall.st；Intel and AMD Soar 13%, Taiwan Semiconductor Rallies 7% as AI-Chip Stocks Bounce Hard - 24/7 Wall St.；Intel and AMD Soar 13%, Taiwan Semiconductor Rallies 7% as AI-Chip Stocks Bounce Hard - AOL.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 90.20 | 114.68 | -21.35% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | 0.00 | +6.36% | +3.19% | 2,205.00 | 2,410.00 | -8.51% | 不適用 | 74.39 | 32.60 | 442.68B TWD / 67.87% | 2026-07-01 |
| AMD 超微 | 新聞直接提及 | 0.00 | N/A | N/A | 476.15 | 516.10 | -7.74% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +6.61% | -5.47% | 110.00 | 164.50 | -33.13% | 不適用 | 6.68 | 18.20 | 23.12B TWD / 22.85% | 2026-07-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -4.92% | +15.11% | 200.75 | 211.14 | -4.92% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 823.03 | 971.00 | -15.24% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | +10.83% | -15.43% | 1,214.83 | 2,335.00 | -47.97% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -12.87% | +25.77% | 389.28 | 446.77 | -12.87% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC、Intel」，共 3 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「Taiwan Semiconductor」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip, foundry。
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel (INTC) Faces AI Supply Bottlenecks As Omdia Sees 94.1% Chip Revenue Jump - simplywall.st](https://news.google.com/rss/articles/CBMiygFBVV95cUxPV2tYNU9MaW0xTGROOW5vNHNOaUt0dm9hRmxWSF9XcGNPNEJRMC1HaFpOWFp6cjl5dllxYUhqeWNnc0ZCaTJWejRwdl8ySzFOd3FnbUxZUDZLMlZNR2VXYmFyZE5QR01Oa3Q3WjlTZk9pRnUyM2FBb1JFRE5uREw0TmJTSWJVUWlmdHhjRXdrQXhBdHB1NnItOVJ0OERXTHdwSEFHMHNZT3ZxM0xkck1qSkZsSEZmckpNajJSQTdKZExhYmcwMXpmbE1B0gHPAUFVX3lxTFBpSHBmLXMwTUFOcVBwREg5bGRGd3Bod3BEOU1KSTJiTnN3Mm83T3cxbnZtYWtLbGFQc3dxcGxqMUZyLTVfV2J6MGxEejhrSGdjd1NVRVRtX0Q2WUdHMkhlYk10R3paeXgyclBMUnp6SHNHUXlmc3ZfdHBZSVNNLVlVc1pYX214cGdYRVlDWmtuaTRLNndyWXpTZTBmcFVkd1hMdURPNjBqcW1TUm5zcHczQ1JKeVZRWWUwOThUekdEMTlRYlZMSkR3M1hDS2ZTYw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 31 Jul 2026 12:25:39 GMT
- [Intel and AMD Soar 13%, Taiwan Semiconductor Rallies 7% as AI-Chip Stocks Bounce Hard - 24/7 Wall St.](https://news.google.com/rss/articles/CBMixAFBVV95cUxPWjNkUlFwLW5GRm5rekkxNDVwNWRqbWdWMkMxbldhRTBGSnNfczRSUHNPNTU2aHdXdEE5OWJqeHNFM09tU1NQRzB6aV9jWVVfYzJCM1pkLUVVZWtzaEhWMXBMckl1eHJDeVNBbTFzZXIwbjNUR0JFaXBRTGl5S0hMa1F4QmpMWmNVTlBDdC0yYjRQMW43cWtKNzFBZ0xyRmhvX21ER0ZFdGpDakt5Rkw2VEp5R24xSDZCVGtWZURMOGxxSWZ5?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 30 Jul 2026 15:51:09 GMT
- [Intel and AMD Soar 13%, Taiwan Semiconductor Rallies 7% as AI-Chip Stocks Bounce Hard - AOL.com](https://news.google.com/rss/articles/CBMid0FVX3lxTE41by1UUVByc3A0NEtzcGdBNFFHUnZqVWcwVjdqRjN2SzFQSzlMYW1sYVhqSUJEMGw1TWd5NkdGeEZoUWhsZkw3YXRHUElLa3d3MTduMHYtRE50WE55WmxvTXNKMTFFYjhHX2Q2blVFd2VsNmd2RUpZ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 30 Jul 2026 16:06:56 GMT

## 新興題材：MarketBeat

摘要：新興題材：MarketBeat 相關新聞集中在：Vestor Capital LLC Makes New Investment in Intel Corporation $INTC - MarketBeat

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 90.20 | 114.68 | -21.35% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Vestor Capital LLC Makes New Investment in Intel Corporation $INTC - MarketBeat](https://news.google.com/rss/articles/CBMixAFBVV95cUxNVnRqa2gxYkp6STY1LXFvM1dfWm5nbndGajVzbGRibGxpYXNsVW80WXlxN2ZzNHVMYkpPTXBwVXVHMTRqQmhIenZKQ1IwVnFYS3hBalJhNmx6UEtkdDZlYy1SZGxYamFESjZ3WThlZG1fLXRzZUNLanUxNGdwckNZTmJiTm5iMzlSYUFvN01yMF9ZNGlnRlBnTVJXcXdzS2gzN0RISm55S1JVZTM1OEEtU2Q3ZjJFa2RFaDRMdk5mREZSdUhI?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 31 Jul 2026 10:36:49 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel (INTC) Faces AI Supply Bottlenecks As Omdia Sees 94.1% Chip Revenue Jump - simplywall.st；Intel and AMD Soar 13%, Taiwan Semiconductor Rallies 7% as AI-Chip Stocks Bounce Hard - 24/7 Wall St.；Intel Stock Jumps As AI-Fueled Earnings Crush Wall Street - timothysykes.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.57 | N/A | N/A | 90.20 | 114.68 | -21.35% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.57 | N/A | N/A | 476.15 | 516.10 | -7.74% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | -0.28 | +6.36% | +3.19% | 2,205.00 | 2,410.00 | -8.51% | 背離 | 74.39 | 32.60 | 442.68B TWD / 67.87% | 2026-07-01 |
| NVDA 輝達 | 產業/供應鏈推估 | -0.06 | -4.92% | +15.11% | 200.75 | 211.14 | -4.92% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 產業/供應鏈推估 | -0.02 | +18.33% | -8.28% | 464.72 | 506.69 | -8.28% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -12.87% | +25.77% | 389.28 | 446.77 | -12.87% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.03 | +0.18% | -9.46% | 505.00 | 680.00 | -25.74% | 未明確 | 10.86 | 51.53 | 65.78B TWD / 32.86% | 2026-07-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.02 | +7.24% | -5.20% | 3,235.00 | 4,310.00 | -24.94% | 背離 | 62.91 | 58.71 | 58.01B TWD / 2.80% | 2026-07-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC、Intel」，共 5 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：miss。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。 方向判斷命中詞：miss。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「Taiwan Semiconductor」，共 2 篇新聞命中。 同時符合主題標籤：AI, advanced packaging, CoWoS, AI server。 方向判斷命中詞：miss。

### 主要來源

- [Intel (INTC) Faces AI Supply Bottlenecks As Omdia Sees 94.1% Chip Revenue Jump - simplywall.st](https://news.google.com/rss/articles/CBMiygFBVV95cUxPV2tYNU9MaW0xTGROOW5vNHNOaUt0dm9hRmxWSF9XcGNPNEJRMC1HaFpOWFp6cjl5dllxYUhqeWNnc0ZCaTJWejRwdl8ySzFOd3FnbUxZUDZLMlZNR2VXYmFyZE5QR01Oa3Q3WjlTZk9pRnUyM2FBb1JFRE5uREw0TmJTSWJVUWlmdHhjRXdrQXhBdHB1NnItOVJ0OERXTHdwSEFHMHNZT3ZxM0xkck1qSkZsSEZmckpNajJSQTdKZExhYmcwMXpmbE1B0gHPAUFVX3lxTFBpSHBmLXMwTUFOcVBwREg5bGRGd3Bod3BEOU1KSTJiTnN3Mm83T3cxbnZtYWtLbGFQc3dxcGxqMUZyLTVfV2J6MGxEejhrSGdjd1NVRVRtX0Q2WUdHMkhlYk10R3paeXgyclBMUnp6SHNHUXlmc3ZfdHBZSVNNLVlVc1pYX214cGdYRVlDWmtuaTRLNndyWXpTZTBmcFVkd1hMdURPNjBqcW1TUm5zcHczQ1JKeVZRWWUwOThUekdEMTlRYlZMSkR3M1hDS2ZTYw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 31 Jul 2026 12:25:39 GMT
- [Intel and AMD Soar 13%, Taiwan Semiconductor Rallies 7% as AI-Chip Stocks Bounce Hard - 24/7 Wall St.](https://news.google.com/rss/articles/CBMixAFBVV95cUxPWjNkUlFwLW5GRm5rekkxNDVwNWRqbWdWMkMxbldhRTBGSnNfczRSUHNPNTU2aHdXdEE5OWJqeHNFM09tU1NQRzB6aV9jWVVfYzJCM1pkLUVVZWtzaEhWMXBMckl1eHJDeVNBbTFzZXIwbjNUR0JFaXBRTGl5S0hMa1F4QmpMWmNVTlBDdC0yYjRQMW43cWtKNzFBZ0xyRmhvX21ER0ZFdGpDakt5Rkw2VEp5R24xSDZCVGtWZURMOGxxSWZ5?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 30 Jul 2026 15:51:09 GMT
- [Intel Stock Jumps As AI-Fueled Earnings Crush Wall Street - timothysykes.com](https://news.google.com/rss/articles/CBMifkFVX3lxTE5yU2JmTFF3RV9zS0E5em5mVnJPUl9laVdSWnhTSGZIUmFua09HTEdxV1ZBbnluQmhOWlY0b0JjSzl2OWJoU0doeFV0bWtxVnRoX0lSVUdNS1gtT0lBQVA2RFhuN1JCMEhwdnktMHdvQ2NLTDkzRUE2bVBVNGVTZw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 31 Jul 2026 11:49:00 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報；800G、1.6T與CPO也導入液冷　它受惠Blackwell放量，法人目標價最高喊3,610元 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | -0.21 | +3.57% | -2.52% | 2,110.00 | 2,835.00 | -25.57% | 背離 | 61.06 | 38.12 | 17.62B TWD / 66.11% | 2026-07-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 1 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：跌停。

### 主要來源

- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 31 Jul 2026 14:03:07 GMT
- [800G、1.6T與CPO也導入液冷　它受惠Blackwell放量，法人目標價最高喊3,610元 - 經濟日報](https://news.google.com/rss/articles/CBMikAFBVV95cUxNX2tpNjZPOENOcl83dWx4MFBWTXNVV2dfaWF5clM4ZnMxb2ZZRTJCN19QMWFtY3hSYXNPS2ZBLXdESk5TYUlRWlIxS0Y0eTVVUXlPUW1xV2JlSnhuVXJGNUpFRzJkbmVoS0p6dFFyMVdUTjBYam8wekRwNzF3azUxVHlEWC1FMmVwbzZBVGNmNGHSAV9BVV95cUxPdEppYXRNaFJUa2dma3QzcFZUcXZWV0pEWEVQdDFlaElSWjBDNlZxTjZpQUI1YUFGb2sxOVAxNmVlVTR3Rkwxd2RqX1F3LWwwSGIzV0RtTFRVWko0RDVCaw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 31 Jul 2026 15:15:16 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》量縮飆漲3186點、收復43K；月K翻黑- 新聞 - MoneyDJ；台股暴力反彈 台幣早盤震盪微升0.4分 - MoneyDJ；個股動態報導內容-F9A09230-CD30-4D06-BA07-58E48D298A0D - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》量縮飆漲3186點、收復43K；月K翻黑- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPSllPeFhyM3hXRGtkVkpuQkFHaDhCa1JhcERqWURYcEFLMWRzcVpDekZKbU9JLVVucC00YVlLS2dPUVRvYzk0dkFlb3NzenNpWkxPRnFzam1MRnRUVEF0ZTFVamFuQlpxZGlsbzFPTFZsRml4S3pHN194NkdORnZtSmd5N3FxbldEMDQweUZJclR4Zw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 31 Jul 2026 07:45:00 GMT
- [台股暴力反彈 台幣早盤震盪微升0.4分 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQankzS083aWtXQU9rNlcwbFJFOUhxcGxueGg4UHhTZlVwSWpKYk54M1ZMbTJoNFVmc2ZkT3B5MVBKcGxHWDlXR0lhaUV1V2FUVjM4YUxuSlNjY3dzaWV6ZWR3bUFqUmpJbEg5NUt2azBXMk1mVzU0QkthYkNfdUxiSEJJc2tDYml2TmdpcmtFd3Rndw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 31 Jul 2026 04:56:00 GMT
- [個股動態報導內容-F9A09230-CD30-4D06-BA07-58E48D298A0D - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxNN21UZXZScUhOaDc4bGY0RFZ0N1NMdVQ2SzBHWWU1WjdpOGVtemxtVGhhZjhlVUxYVHQzdGhySVJqcVJrb1I0YjdtOWNsenZ3bFBUWkpoc2w5cGhOcUhXaXgxQldVNFJrR1hDR3hJTF9IUzVOQ1djbXVBU19ubElxbm9GWEdIVGx2ZUJLYVIzamQxLWJ1?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 31 Jul 2026 12:02:23 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
