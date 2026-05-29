# 每日股市熱門話題分析 - 2026-05-30

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **AI 伺服器與資料中心**｜正向｜熱度 13｜市場確認 76.67｜同向 4/6
2. **記憶體與 HBM 供應鏈**｜正向｜熱度 7｜市場確認 89.89｜同向 1/1
3. **關稅與供應鏈轉移**｜中性｜熱度 7｜市場確認 N/A｜同向 0/0
4. **半導體與晶片供應鏈**｜中性｜熱度 9｜市場確認 N/A｜同向 0/0
5. **新興題材：SpaceX**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.16（樣本 7）
- 5日相關係數：-0.06（樣本 7）
- 同向比例：5/7

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| AI 伺服器與資料中心 | 76.67 | 4/6 | 1 | +10.29% | +11.35% |
| 記憶體與 HBM 供應鏈 | 89.89 | 1/1 | 0 | +6.63% | +9.90% |
| 關稅與供應鏈轉移 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：SpaceX | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：GuruFocus | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-05-17 | 0.09 | -0.34 | +40.00% | 15 |
| 2026-05-18 | -0.01 | -0.17 | +33.33% | 9 |
| 2026-05-19 | 0.04 | -0.01 | +62.50% | 8 |
| 2026-05-20 | 0.36 | 0.35 | +28.57% | 7 |
| 2026-05-21 | 0.28 | 0.52 | +45.45% | 11 |
| 2026-05-22 | 0.05 | -0.00 | +33.33% | 15 |
| 2026-05-23 | -0.00 | -0.05 | +84.62% | 13 |
| 2026-05-24 | -0.11 | 0.22 | +86.67% | 15 |
| 2026-05-25 | 0.40 | 0.33 | +50.00% | 10 |
| 2026-05-26 | -0.23 | -0.31 | +92.31% | 13 |
| 2026-05-27 | -0.07 | -0.07 | +87.50% | 8 |
| 2026-05-28 | 0.14 | -0.07 | +88.89% | 9 |
| 2026-05-29 | 0.14 | -0.04 | +71.43% | 7 |
| 2026-05-30 | 0.16 | -0.06 | +71.43% | 7 |

## 歷史回測摘要

- 回測日期：2026-05-30
- 近5日 3日相關：-0.22
- 近5日 5日相關：-0.19
- 同向比例：+57.14%
- 權重狀態：未調整

- 方向準確度：+57.14%
- 信心排序準確度：-0.22
- 診斷：方向與信心皆需修正

調整原因：近 5 日有效樣本 7 筆，低於 15 筆門檻，暫不調整權重。

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

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：This Sleeping Semiconductor Giant Will Be the Biggest Winner of the AI Inference Era (Hint: It's Not Intel) - The Globe and Mail；AMD Sinks 6% Despite a Holding Pattern in Intel and NVIDIA: The Selective AI Chip Trade Is Here - AOL.com；台灣企業如何從 AI 製造轉向全面導入 AI？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.76 | +21.07% | +10.47% | 211.14 | 214.25 | -1.45% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.76 | N/A | N/A | 114.68 | 120.89 | -5.14% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.70 | N/A | N/A | 516.10 | 518.09 | -0.38% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.07 | +3.74% | +4.43% | 2,355.00 | 2,355.00 | 0.00% | 同向 | 74.39 | 31.66 | 410.73B TWD / 17.50% | 2026-05-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.03 | -8.49% | -2.20% | 450.24 | 506.69 | -11.14% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.05 | +44.35% | +34.85% | 446.77 | 446.77 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.04 | 0.00% | +8.91% | 611.00 | 627.00 | -2.55% | 未明確 | 10.86 | 56.73 | 62.25B TWD / 19.22% | 2026-05-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.05 | +1.06% | +11.66% | 4,310.00 | 4,410.00 | -2.27% | 同向 | 62.91 | 68.69 | 46.74B TWD / -4.14% | 2026-05-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA、輝達」，共 2 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 2 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [This Sleeping Semiconductor Giant Will Be the Biggest Winner of the AI Inference Era (Hint: It's Not Intel) - The Globe and Mail](https://news.google.com/rss/articles/CBMimwJBVV95cUxQWXp6THNRQ3lsc0VnS3MxWkNYbFBPSXdTU045X00waC1sV3ZMclpBYl9oTU9XOGZiSDBkaVFlZU9DSlZVaHphaXdYcHdBYTFDakltZy1Dc1lndHF1bzlCbGpjcEZzcTF0TmFtMnMyb3lSWkdwWjN3S0lzeDhmYkZWZ3BJUEl4aEtSNVF6ek4xNTRxU1dtb0V2TUNiYmt6SExqcnRDcTRXaUlXM0ZHQTdqZHJZM2Fjd0E4OEhsYmRRNnVIQzRvOGQzVGlIeTRyUkhtUjA5S20tdnRHRk1waG1tRHpIOTdCNkhZODdBb3hyVkNzVVRUdlpPbTk5VkVDNzQ0UmFyQlRQMlZKSHpWbUlmakI1b0ZPVE0tTXFr?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 29 May 2026 17:50:40 GMT
- [AMD Sinks 6% Despite a Holding Pattern in Intel and NVIDIA: The Selective AI Chip Trade Is Here - AOL.com](https://news.google.com/rss/articles/CBMie0FVX3lxTE1xSnZBaXpvbGhaTG9FSFkwVDhYRGRTQ2RRY0NBUmk2d2lYdXU3TEh4OF9rOVBIUU9MRDFfZUUtMzFPNGRHVmJicEJ0ZnZYelBqTWlRcU9pYkFsdWR2bHhaSXpLU3Y0VzFEYndITk42WnBwclFlQ0Jya25Sbw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 28 May 2026 20:53:48 GMT
- [台灣企業如何從 AI 製造轉向全面導入 AI？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiqwFBVV95cUxNek56dHNPeEU5WXlvcy01dnpuSFB2dnZTZ0dVYUFEZVdUSW5UeTQ1UldYWEhjR0hsQ2ZYY19vUU94NFI2dW1LS1ZZeG1CU05FWGgwUERsMmZuQXlhaEFZU0dnQS1BaC1xSlE2dTg3YVF3ZmRIT2kyalpmWkZJdHNfZ1oxbmN0X2d5Um9rUVktQWxZWDk5Q3hRZG9fM2RJZGdWQ29NWjhvVjVRS2s?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 29 May 2026 21:58:47 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Micron Joined The $1 Trillion Club With Its Blistering Rally This Week. Here's How Much Traders See It Moving Next Week - Investopedia；Micron, Sandisk in focus as Susquehanna ups price targets (MU:NASDAQ) - Seeking Alpha；This AI Memory ETF Raised $1 Billion in One Day. Here Are 3 Stocks in Its Holdings You Should Consider Buying - AOL.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.76 | N/A | N/A | 971.00 | 971.00 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.76 | +6.63% | +9.90% | 1,694.98 | 1,694.98 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +21.07% | +10.47% | 211.14 | 214.25 | -1.45% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、MU、memory」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 4 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Micron Joined The $1 Trillion Club With Its Blistering Rally This Week. Here's How Much Traders See It Moving Next Week - Investopedia](https://news.google.com/rss/articles/CBMi8gFBVV95cUxPeE1nd3p1Z3NORi10bXpuUU51ZG5RbTI1NjBoRkZZRE5KdU5OTXVZdXp0QUpQSkpMc3pWYW1JLWdmZ0xYXy0wcHV2b3ZmbVBwUzlVclZyaFUtZHZPczBUTFdXbnZxS2tJQmJ5UHhQTzZ2aUktcnNHbkVnZUR0VTRJSEZLVUplU3RHNlF5cVVMUGVNS3hqU0RsaDZVNU5ma3RZYXVIdnRnQVJibnpmeTBzeVptVnoxRkd2WFRuNUpzb09QQ3BkVzkxYXR5SF9VS0tWUldOR1luRkZYTVFWWkFkVGhhZm1GYWxmcEtDckpQenlSZw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 29 May 2026 20:17:17 GMT
- [Micron, Sandisk in focus as Susquehanna ups price targets (MU:NASDAQ) - Seeking Alpha](https://news.google.com/rss/articles/CBMimgFBVV95cUxPUWk5VE1CTm9PQUY4R1pzaVNZTXpSQVlJU1o1T184OE52VXZHRlhFT09yRW1wWU41YVFGYzFLNXNpeGs1eHJPOFA3S0xGOE9EVVVOWmFfYm1ZR0lBTTN5T3hTZTYxNkpmSzBaSlEyeEpZRF9jS1YtYUhzS0ItSVU4eU5xdi1qNjdGaGNSV21aajV6QkRROHVqQ3Jn?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 29 May 2026 12:55:13 GMT
- [This AI Memory ETF Raised $1 Billion in One Day. Here Are 3 Stocks in Its Holdings You Should Consider Buying - AOL.com](https://news.google.com/rss/articles/CBMidEFVX3lxTE1uUzVkSVBvWnJMZU5iNGI0dExsdWRxb2ZkNmwzcDNTcHp2a2I5V2M2bFM5QWQ2T05wTENuRUQ5aUhJcW9kcjhxOE1MWkVIWVlXcjdMT0RsWmNUdFUzZkhQNjIwbmZpM1VMQ0swZFVkRFNhRDN4?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 29 May 2026 21:37:38 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：美公告對台非半導體232關稅優惠 落實投資MOU - 中央社 CNA；美國正式公告我非半導體232關稅優惠回溯自5／1起生效- 要聞 - 工商時報；賣的是整條 AI 供應鏈！證交所攜緯穎登彭博揭台股估值溢價密碼 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 6669 緯穎 | 新聞直接提及 | 0.00 | +3.12% | -1.45% | 5,445.00 | 5,525.00 | -1.45% | 不適用 | 298.31 | 18.25 | 82.73B TWD / 29.67% | 2026-05-01 |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +11.91% | +55.37% | 312.06 | 312.51 | -0.14% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | +11.58% | +15.60% | 289.00 | 289.00 | 0.00% | 不適用 | 14.13 | 20.53 | 832.10B TWD / 29.74% | 2026-05-01 |

關聯理由（前 3）：
- 6669：新聞直接提及「緯穎」，共 2 篇新聞命中。
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [美公告對台非半導體232關稅優惠 落實投資MOU - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5zMzZsX1lfUG9VVUxUWnphX1lvT2M5S09lXzdzaDdkdy1pTkJtWks1SUU1OTV1QUp5SmdrRWxza0UwUkxyR09ROUtKZGNTT3BOdEFFVk5GeTAzTEhYdzlJ?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 28 May 2026 23:20:00 GMT
- [美國正式公告我非半導體232關稅優惠回溯自5／1起生效- 要聞 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5qTjczN1ZGdWpFSEpRQ3had3I0TG5kSWo2NXN0WEpSQ3hOTTFJdzhjeDhQLXQwZ1RCNUNINTlLYjRqVjB1eDNmZjctdllaOHpZUFhyZks5eTY4MWdRTmJZ?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 28 May 2026 12:26:00 GMT
- [賣的是整條 AI 供應鏈！證交所攜緯穎登彭博揭台股估值溢價密碼 - TechNews 科技新報](https://news.google.com/rss/articles/CBMia0FVX3lxTE00ZEVuelhNTmVqaU1FV2d2NV9NZ2MxRm1xR2dieGszMEdmVHh6dTVpdUlxVzNBRTRWMHBkRkFybk5OSGNpTHRjVHVUWmFmNTJkZEdQb1FLMnY5ejg5ZVVEVUR6Mm1sUkJEX0hV?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 29 May 2026 08:14:14 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：This Sleeping Semiconductor Giant Will Be the Biggest Winner of the AI Inference Era (Hint: It's Not Intel) - The Globe and Mail；AMD Sinks 6% Despite a Holding Pattern in Intel and NVIDIA: The Selective AI Chip Trade Is Here - AOL.com；談華為半導體新突破 黃仁勳：台積電和台灣領先10年 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 114.68 | 120.89 | -5.14% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | 0.00 | +3.74% | +4.43% | 2,355.00 | 2,355.00 | 0.00% | 不適用 | 74.39 | 31.66 | 410.73B TWD / 17.50% | 2026-05-01 |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +21.07% | +10.47% | 211.14 | 214.25 | -1.45% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | N/A | N/A | 516.10 | 518.09 | -0.38% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +10.73% | +26.75% | 144.50 | 144.50 | 0.00% | 不適用 | 4.00 | 36.31 | 22.66B TWD / 10.80% | 2026-05-01 |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 971.00 | 971.00 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | +6.63% | +9.90% | 1,694.98 | 1,694.98 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | +44.35% | +34.85% | 446.77 | 446.77 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「台積電、TSMC」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip, foundry。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [This Sleeping Semiconductor Giant Will Be the Biggest Winner of the AI Inference Era (Hint: It's Not Intel) - The Globe and Mail](https://news.google.com/rss/articles/CBMimwJBVV95cUxQWXp6THNRQ3lsc0VnS3MxWkNYbFBPSXdTU045X00waC1sV3ZMclpBYl9oTU9XOGZiSDBkaVFlZU9DSlZVaHphaXdYcHdBYTFDakltZy1Dc1lndHF1bzlCbGpjcEZzcTF0TmFtMnMyb3lSWkdwWjN3S0lzeDhmYkZWZ3BJUEl4aEtSNVF6ek4xNTRxU1dtb0V2TUNiYmt6SExqcnRDcTRXaUlXM0ZHQTdqZHJZM2Fjd0E4OEhsYmRRNnVIQzRvOGQzVGlIeTRyUkhtUjA5S20tdnRHRk1waG1tRHpIOTdCNkhZODdBb3hyVkNzVVRUdlpPbTk5VkVDNzQ0UmFyQlRQMlZKSHpWbUlmakI1b0ZPVE0tTXFr?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 29 May 2026 17:50:40 GMT
- [AMD Sinks 6% Despite a Holding Pattern in Intel and NVIDIA: The Selective AI Chip Trade Is Here - AOL.com](https://news.google.com/rss/articles/CBMie0FVX3lxTE1xSnZBaXpvbGhaTG9FSFkwVDhYRGRTQ2RRY0NBUmk2d2lYdXU3TEh4OF9rOVBIUU9MRDFfZUUtMzFPNGRHVmJicEJ0ZnZYelBqTWlRcU9pYkFsdWR2bHhaSXpLU3Y0VzFEYndITk42WnBwclFlQ0Jya25Sbw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 28 May 2026 20:53:48 GMT
- [談華為半導體新突破 黃仁勳：台積電和台灣領先10年 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1MV2dMNFJNY21rdzZJcTI4V2hzUEcxRkJBRXNnMFExS1dpNFJ6aXFJVmtzZjFPSEZuVVdnNk9ZNGJTNmo2cEduQWhycFRNUHN3cnYxaEV3UnpFWi1Vd2c?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 28 May 2026 14:24:00 GMT

## 新興題材：SpaceX

摘要：新興題材：SpaceX 相關新聞集中在：SpaceX Interest In Intel Puts AI Foundry Plans Under A New Lens - simplywall.st

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 114.68 | 120.89 | -5.14% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [SpaceX Interest In Intel Puts AI Foundry Plans Under A New Lens - simplywall.st](https://news.google.com/rss/articles/CBMiygFBVV95cUxQUTFVTmN2N21YRU5SYkpNWVkzdTllYUM5dHRtdWlpUklkNF9NelFtMVYtN0RERVF6UGxSYW92TV9TVE5sU1IzbnM2LXU4ajlTeGxidlJhOU9hVEJyc1lvZW9BY29NdUEyQWM0aVh0X2p4bGhrUHBrSXUzTUVvTXRvUzhwWEpDZGhpZnVLbVdldk5TdFNKOF90MU95cVlici1UeGc4azlNZl9TMF9jdEFhUFNuSWpBSkxmZFFRV3llVkxXYlEwdk9VZk5R0gHPAUFVX3lxTE9GcGZLekY3TXJXSDdRVExmVWlGWXdjdnJQcnVaU2FGTm1ZWVVjZVpxdUZoNGg3VkNDbVpNRGZReDAtU1RwZE9NX2cxdm1jYjcwWnlfTmVOWWkyMThJNzRKbUsydno4czB0akt3Z0NkUkh0RW0yc0J0aDFmYTltVkxVM0ZPa2psZ09ia0FZMUlDdElVWm5Mb2JpdmlXb3plY2ZTeDRuYUwwLXpiQUxvLV9CSDJpTEJhUi1KYmJtU2RDLWFubHhtVGstT0hkSkRkZw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 28 May 2026 19:18:31 GMT

## 新興題材：GuruFocus

摘要：新興題材：GuruFocus 相關新聞集中在：Nvidia's Next AI Wave Sparks Big Calls on Micron, Dell, Arm Stoc - GuruFocus

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +21.07% | +10.47% | 211.14 | 214.25 | -1.45% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 971.00 | 971.00 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MU：新聞直接提及「Micron」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Nvidia's Next AI Wave Sparks Big Calls on Micron, Dell, Arm Stoc - GuruFocus](https://news.google.com/rss/articles/CBMitAFBVV95cUxOUEcxeWpyUHdvSk1WQkdBQ3NTV1JQZjVhSkw4OTlzdzBOeWFjUFdHblRsc1o2ZVc5azVYWjVpaThFSG1lUnpkSTJyYXk1MTNnbXYzaTd5Mzl3OGhMclNtNG9OQWowVVpHU29CVi1KVUJEMEZBV01rNkxtZmU2RFFXZy1MYmxNalhXZDJCTmlvUC1RekxTSzRJZ2pqWmJjeXNQNzdMVXlHTnhLLURKVGNNZDJtRHA?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 28 May 2026 21:04:17 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股基金績效 衝出新榮景 | 基金天地 | 理財 - 經濟日報；10檔外資鎖碼股 盤面聚焦 | 市場焦點 | 證券 - 經濟日報；台股5月大漲5,806點 法人：下周可望續戰新高 但短線行情可能出現波動 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股基金績效 衝出新榮景 | 基金天地 | 理財 - 經濟日報](https://news.google.com/rss/articles/CBMifEFVX3lxTFBDdVRVY29abnJPX0F1Q2VMTUhIcmYtdWxyTFQyakZHSmJKa1AyXzhZNGdWZ0hkd0xrdFlxQzhYLXAweFR4d0dJLWwwZFg0ZTdfS3hSN0NPVHZnTkdOcFg1RHRlMWw1Wk40Y19wODZsYjhuNExzUmFqWk1DcWE?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 29 May 2026 17:44:10 GMT
- [10檔外資鎖碼股 盤面聚焦 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiekFVX3lxTE1PaFdsSUZtdE8wbENfOVUxSE1Cd0h0WEFXWTV3ZGEtRGJjekdWN2hLLWktdGhDSF9HNF9tMEpXeWFWOVI0YWNFQkhwTlpaRVNJN3VPQkJSQk85eWFod29mZ1laVmZiZDB0TW9LX2hxajNVdndVaWZvaHN3?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 29 May 2026 16:13:23 GMT
- [台股5月大漲5,806點 法人：下周可望續戰新高 但短線行情可能出現波動 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1vb18tR1RXUWdZTThURmVYZno2azZ3bWlDTExOQy1HUUtWSTc3OHBKOENEU3VmcURDcTVMSms5UzlMNHF6dk1BR3cxMTBUelFJVU5PVXc2c09IUdIBX0FVX3lxTFA5MGpjMlR3RU9yQTcxUnlxTHVBYWtQSlRzMkdKdUpHY1hzRzhoaldDMEhtbzdxdVdCVHhCWkZjNG5ONi14RFJtRklOSmxaY1dEMVVOd1NvNnB4U1N2Z3pV?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 29 May 2026 10:05:24 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》天量飆漲1096點、寫新高；月K連二紅-新聞內容-基金 - MoneyDJ；統一證券：台股盤勢仍有利於多方- 新聞 - MoneyDJ；台股焦點：應廣(6716.TW) - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》天量飆漲1096點、寫新高；月K連二紅-新聞內容-基金 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxPdEg5d1RYUVFTc29VX1dfZkl4dXBkTzhXYmtnYmthNmZTLUptemNPeERKRzIxY3Y3Nk9fNVJJdFp4RjZtLXIzaGNCZ2dTd0xZaUpSbGg4S21VeG5Yd1JDSzBrN3ZCanJwZ1RBdnh2bkUyLW95b1R0U1EteFNCUUpidS1veGJtbkl1cGF5TW5ZTEw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 29 May 2026 08:26:00 GMT
- [統一證券：台股盤勢仍有利於多方- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNbndPdURrbGI3cHd5amVEa29TeXo4a0FMUHJERlUxR3dObDV3ZkJxWG5RNWVhRFBmeW9jSkNfQWR1R0cxTW01UmE3Nm5RTUo0enljemI4d1p3QU44QVhaOHE0T1F2TlpEX3p1WXc1eDFpT3pfcklmN1F3VVNMTEJCOXBPX2N0a0RhT2lFbTVCTUFIUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 29 May 2026 00:47:00 GMT
- [台股焦點：應廣(6716.TW) - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNa1NsdndZWFJ0X0NDdUFXNFdBbDdzaG9OMWdBeGRzS2UtbTNnbXVWY0ZBR3lhREhKb0FiRlo2RUZqYmUyQTZzM0x6bG11OEdOWlVhVWVzU25KekNsUFFkYVRRQmFYX1dhYTRBOVBhQTc0cExfa3BVYTlxdk12MS1xdnhXeDNsZ2VBT2ZoUEk2TlU5dw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 29 May 2026 01:16:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
