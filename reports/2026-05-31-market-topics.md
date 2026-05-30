# 每日股市熱門話題分析 - 2026-05-31

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **綜合市場情緒**｜中性｜熱度 42｜市場確認 N/A｜同向 0/0
2. **記憶體與 HBM 供應鏈**｜正向｜熱度 5｜市場確認 89.89｜同向 1/1
3. **AI 伺服器與資料中心**｜中性｜熱度 14｜市場確認 N/A｜同向 0/0
4. **關稅與供應鏈轉移**｜正向｜熱度 3｜市場確認 79.36｜同向 1/1
5. **散熱與液冷供應鏈**｜負向｜熱度 2｜市場確認 76.60｜同向 1/1

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.96（樣本 3）
- 5日相關係數：0.09（樣本 3）
- 同向比例：3/3

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 記憶體與 HBM 供應鏈 | 89.89 | 1/1 | 0 | +6.63% | +9.90% |
| AI 伺服器與資料中心 | N/A | 0/0 | 0 | N/A | N/A |
| 關稅與供應鏈轉移 | 79.36 | 1/1 | 0 | +3.12% | -1.45% |
| 散熱與液冷供應鏈 | 76.60 | 1/1 | 0 | +2.20% | -4.72% |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
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
| 2026-05-31 | 0.96 | 0.09 | +100.00% | 3 |

## 歷史回測摘要

- 回測日期：2026-05-31
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

摘要：綜合市場情緒 相關新聞集中在：個股動態報導內容-5B2E0EFC-79DB-4F19-982E-1C9C8626BD88 - MoneyDJ理財網；元大-大甲 對 精金(3049)個股 單一券商歷史明細 - justdata.moneydj.com；永豐金-南投 對 佳和(1449)個股 單一券商歷史明細 - kgieworld.moneydj.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2303 聯電 | 新聞直接提及 | 0.00 | +10.73% | +26.75% | 144.50 | 144.50 | 0.00% | 不適用 | 4.00 | 36.31 | 22.66B TWD / 10.80% | 2026-05-01 |

關聯理由（前 3）：
- 2303：新聞直接提及「聯電」，共 1 篇新聞命中。

### 主要來源

- [個股動態報導內容-5B2E0EFC-79DB-4F19-982E-1C9C8626BD88 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilAFBVV95cUxON25kSnc2UHhTNlZFczYzZC1hYVhfek9OSzYtU0tVNGZ5WFlZTGxXUFhqb2NUZFNKTDNFTF90S2FpXzJqZzBWbXMwTGNFSXpJVkJhUVo3YVY0QUpRYzAxWWp2eVZkcDYxSlZacmhDMXJibGE3YlQ5aENKME56OGU5NmFSSXpGeHlPeDQ5aGpJejY1eGJM?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 30 May 2026 00:28:35 GMT
- [元大-大甲 對 精金(3049)個股 單一券商歷史明細 - justdata.moneydj.com](https://news.google.com/rss/articles/CBMikgFBVV95cUxObEIzNTl5Q3NJZ05qM1NXRC1ZR2c4b0FHaGVYNmtCY0xIeHgtTWt3Z0Njd0hhWTNxRTdqNEl0amVRd0FMS0ctQVZWMFhSOExiOExLb2trS29xZmJhSnR0OWx0YldJN3dIZ203R05Xb0xKVExUZ3h2RTFMS3pqSFJwTHFKbnRDZFpoQnZEVUdoSUdqdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 30 May 2026 13:53:01 GMT
- [永豐金-南投 對 佳和(1449)個股 單一券商歷史明細 - kgieworld.moneydj.com](https://news.google.com/rss/articles/CBMilAFBVV95cUxNdkt3OG1taFA2cEhzT2R4TmZLRFlJN1NHckRVR1lhdmlWamVNTzNrRXlwRTM1bFpfVVI3c0F0ai1hRkVhU25UWTNDb3lVWDlPelFBdXJXZk9vQzR2b0I5TVk2dWQ0SFdyeTBNSlU4NncwSE9KRDdqYm0wTV91UTl4MFdQWXdPYmtmTTVMbjQ2V1BPeklM?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 29 May 2026 21:22:01 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Micron Joined The $1 Trillion Club With Its Blistering Rally This Week. Here's How Much Traders See It Moving Next Week - Investopedia；Not Just Micron: Memory Melt-Up Pulls SanDisk Up 8%, Western Digital Up 10% - AOL.com；Micron, Sandisk in focus as Susquehanna ups price targets (MU:NASDAQ) - Seeking Alpha

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.76 | N/A | N/A | 971.00 | 971.00 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.76 | +6.63% | +9.90% | 1,694.98 | 1,694.98 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +21.07% | +10.47% | 211.14 | 211.14 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、MU」，共 4 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Micron Joined The $1 Trillion Club With Its Blistering Rally This Week. Here's How Much Traders See It Moving Next Week - Investopedia](https://news.google.com/rss/articles/CBMi8gFBVV95cUxPeE1nd3p1Z3NORi10bXpuUU51ZG5RbTI1NjBoRkZZRE5KdU5OTXVZdXp0QUpQSkpMc3pWYW1JLWdmZ0xYXy0wcHV2b3ZmbVBwUzlVclZyaFUtZHZPczBUTFdXbnZxS2tJQmJ5UHhQTzZ2aUktcnNHbkVnZUR0VTRJSEZLVUplU3RHNlF5cVVMUGVNS3hqU0RsaDZVNU5ma3RZYXVIdnRnQVJibnpmeTBzeVptVnoxRkd2WFRuNUpzb09QQ3BkVzkxYXR5SF9VS0tWUldOR1luRkZYTVFWWkFkVGhhZm1GYWxmcEtDckpQenlSZw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 29 May 2026 20:17:17 GMT
- [Not Just Micron: Memory Melt-Up Pulls SanDisk Up 8%, Western Digital Up 10% - AOL.com](https://news.google.com/rss/articles/CBMie0FVX3lxTE5FeHdrVTdzRy1BdXYyS3ltaHFPWGotNzlPaG9hOTBNZTdDUkZtS0ZTem16cjhhcHZ1N1Z0V1lNR0VkRlU5RmEzYXJEZjFhaGJDdlNSbHhRNlIybWFCYjJwQUU5MG9oNm00R2lTaFJ4WVNNM29QYXg3bThJNA?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 30 May 2026 21:22:26 GMT
- [Micron, Sandisk in focus as Susquehanna ups price targets (MU:NASDAQ) - Seeking Alpha](https://news.google.com/rss/articles/CBMimgFBVV95cUxPUWk5VE1CTm9PQUY4R1pzaVNZTXpSQVlJU1o1T184OE52VXZHRlhFT09yRW1wWU41YVFGYzFLNXNpeGs1eHJPOFA3S0xGOE9EVVVOWmFfYm1ZR0lBTTN5T3hTZTYxNkpmSzBaSlEyeEpZRF9jS1YtYUhzS0ItSVU4eU5xdi1qNjdGaGNSV21aajV6QkRROHVqQ3Jn?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 29 May 2026 12:55:13 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Jim Cramer Says Dell's Blowout Quarter Could Mark A Turning Point For AI Stocks Like Nvidia And Intel: 'I Wonder If...' - Benzinga；AI 科技如何重塑傳統補教業競爭力？ - TechNews 科技新報；AI 診斷系統如何提升補教業教學效率？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +21.07% | +10.47% | 211.14 | 211.14 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 114.68 | 114.68 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 516.10 | 516.10 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +3.74% | +4.43% | 2,355.00 | 2,355.00 | 0.00% | 不適用 | 74.39 | 31.66 | 410.73B TWD / 17.50% | 2026-05-01 |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | -8.49% | -2.20% | 450.24 | 506.69 | -11.14% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | +44.35% | +34.85% | 446.77 | 446.77 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | 0.00% | +8.91% | 611.00 | 611.00 | 0.00% | 不適用 | 10.86 | 56.73 | 62.25B TWD / 19.22% | 2026-05-01 |
| 2454 聯發科 | 產業/供應鏈推估 | 0.00 | +1.06% | +11.66% | 4,310.00 | 4,310.00 | 0.00% | 不適用 | 62.91 | 68.69 | 46.74B TWD / -4.14% | 2026-05-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Jim Cramer Says Dell's Blowout Quarter Could Mark A Turning Point For AI Stocks Like Nvidia And Intel: 'I Wonder If...' - Benzinga](https://news.google.com/rss/articles/CBMi-AFBVV95cUxORUtmXzBQRDhFWF9mYW9NVTJfSVRyTUhJSTFxVEF3Tkh3cU13UW4wVDlKRW15UGRYd0pxNUE3Tnp0dXppRHFMdllUOW1oNk4wdk44NEt5SUE2ZFQ1ZmJoN1B2Z1hVUjRTNEVoekVlZXNiR3FoWmhzY25yN3dNb3BFZVRXYVlqSmRXUjBnQ3hLa2NTMkJVb0haV2lWVTh3U3RyZzBmVjBjRWVTaU8wczVya2ZiQjJHSUxZcDdVX2ljWHgwMl9YZUc4a3VsX3lTTkVoT08tNTBTLXhMV2RxNlcyWTM0TUJYSTBJcjlINml4RWROckUtaUoxXw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 30 May 2026 03:58:00 GMT
- [AI 科技如何重塑傳統補教業競爭力？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMid0FVX3lxTE9fQ09TZDRIa1VfWGw5NHNNZFVzUHE3N2RMWm9ZdzFiTGJqeDIxLTh3VmtpTkJvMFdvb0lDVWVBSDBrUFZLYk9nWjlSazdoMy1TenBONFA0N05Pak81TzdPdkw1Ry1kRm52UG80Um4tVjRWTEpFUzZV?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 30 May 2026 20:07:58 GMT
- [AI 診斷系統如何提升補教業教學效率？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMid0FVX3lxTFBKWmRRWlFVNFU4TTJNRk9yU3g1NFFQS0ZZLXRzY1dyZjlyWGItZFZTVmxuRFl6eGtEWVRtZzdqXzFvMUZLcFVDd0p3TVlxMGlmNGw2d3NZeVVpUDFRRVpRVFBBM3dvWjhzbk5EQnZaVjNreS0wUnlF?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 30 May 2026 19:33:07 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：日本製造鏈升級，對 AI 供應鏈意義？ - TechNews 科技新報；證交所與緯穎接受彭博專訪 聚焦 COMPUTEX 2026 展現台灣 AI 強韌供應鏈與生態圈 - TWSE 臺灣證券交易所；AI供應鏈再拉警報！南韓半導體設備業爆「史上最嚴重」非記憶體晶片缺貨危機 - news.cnyes.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 6669 緯穎 | 新聞直接提及 | +0.56 | +3.12% | -1.45% | 5,445.00 | 5,525.00 | -1.45% | 同向 | 298.31 | 18.25 | 82.73B TWD / 29.67% | 2026-05-01 |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +11.91% | +55.37% | 312.06 | 312.06 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | +11.58% | +15.60% | 289.00 | 289.00 | 0.00% | 不適用 | 14.13 | 20.53 | 832.10B TWD / 29.74% | 2026-05-01 |

關聯理由（前 3）：
- 6669：新聞直接提及「緯穎」，共 1 篇新聞命中。
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [日本製造鏈升級，對 AI 供應鏈意義？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiqgFBVV95cUxPUXRWbXRRaU9qb1BnaEZtbkUtMkJOVXZEeEVuaHN0T0x1YmNrQWw1TFltcy1CVXp3ZlZYcDRHUzZXSmRWdGJSdEU4YVY0QnpCUE50aThEUXctRVd1a2RmcTViaDdkYVFqZFVKczBuWi13VHBUWURTYXgtNEliNnlzQnZ5dnI5Wjg2QnFqeFZYbFo3TzZJQWhIX0RGQkhncmNCZkplVmZTd04xZw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 30 May 2026 19:01:06 GMT
- [證交所與緯穎接受彭博專訪 聚焦 COMPUTEX 2026 展現台灣 AI 強韌供應鏈與生態圈 - TWSE 臺灣證券交易所](https://news.google.com/rss/articles/CBMinwFBVV95cUxPQzRIVjJiZkl4VzBtblhhak5zUUd6Z1VsVlhBT3IxVDUtX18zZ3VXTVNkYTl6eVRvQzV2eUdnbFJ6TnlJbDRfQWxWT1N3a3U1STdYWUxIN0QtZFBQLUJpN01IYzZDS1FOTG5DWk40VDBXQXU4WnRwbnlyMDRpN3RxRHFqTzZFcG10c1hQR0FOM0J3MWRDMVJJRTlnMkFtd28?oc=5) - Google News source discovery | TWSE Fri, 29 May 2026 09:10:37 GMT
- [AI供應鏈再拉警報！南韓半導體設備業爆「史上最嚴重」非記憶體晶片缺貨危機 - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTE1zdHgydV9RdEpMN2xDaXZDdlJwTUxCSHM2Snlod2JidmRQUUtPQUgtX1JhVDFQVEl1ZHJHY1o3T1RqTGlQeDJUSjN2bnBuNzQ?oc=5) - Google News source discovery | 鉅亨網 Sat, 30 May 2026 14:00:06 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報；European defense stocks are cooling off after the military spending boom. Here's what's next - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | -0.58 | -2.20% | +4.72% | 2,665.00 | 2,835.00 | -6.00% | 同向 | 61.06 | 43.79 | 15.63B TWD / 71.62% | 2026-05-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 1 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：跌停。

### 主要來源

- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 29 May 2026 07:00:44 GMT
- [European defense stocks are cooling off after the military spending boom. Here's what's next - CNBC](https://news.google.com/rss/articles/CBMikAFBVV95cUxOZGJUTEtNRkZ5aGFtSENCdkJaR3FXWElGZnBZc0ZGSHZDMXlycmVTbW5RMkt5T2pFZjU1WGRvWjdpQ3IxcEV3bS1QQ3Z1dF9WaXdLNy1jUk5nM09CWHFlM3RfT29lelB0Vlk5YWE0eERydTVKYVFDd2xYck1JTUZVUi1JSmhWN0hOWUpNblRyTjfSAZYBQVVfeXFMTkVwb3lRa1prOXJGTjZkS2hqa1EzaHBlNG1IclRFa3QtZ3VYaUpzbG11eUlHSGloVnRqVmE2VlNGQUpVeENMZUUyTkJjTU9VbHBQVWRhc2RCUW5KdFMycUdiV29Tem9UNnU1RnlJM1FvdjA1MS1Kb1BxVURweUUzcnhBNV9xNzA3RUJJeXhTNGdzMGdIVW1R?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 30 May 2026 06:01:49 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：最新專欄分析 - MoneyDJ；京元電新增女性獨董；今年營收有望明顯躍升- 新聞 - MoneyDJ；光耀公告調整本公司114年度個體財報第67頁部分資訊- 新聞 - MoneyDJ

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2454 聯發科 | 新聞直接提及 | 0.00 | +1.06% | +11.66% | 4,310.00 | 4,310.00 | 0.00% | 不適用 | 62.91 | 68.69 | 46.74B TWD / -4.14% | 2026-05-01 |

關聯理由（前 3）：
- 2454：新聞直接提及「聯發科」，共 1 篇新聞命中。

### 主要來源

- [最新專欄分析 - MoneyDJ](https://news.google.com/rss/articles/CBMif0FVX3lxTE1jY2lmV2JPRWZ2U19BbGtwcEVWalROLUFpX0xHb2Y2VDdBdzQ2dGZnS3UwZExnbWFrUlRjeWZxTTRMNW1KUVJRaFI0cHVhWExBM1BzS3hDMGJtSWFkcGJsclZPV01sc0JaMkdvZVVuUWNSSTBOcElhTUM0QVVTNnc?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 30 May 2026 07:01:51 GMT
- [京元電新增女性獨董；今年營收有望明顯躍升- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPeFpSdC1XRjM1NTgyVF9qZGdoMS1jckxVSVJjUFJxeGg4R2dqcnJIRXpOOWVuRFY2YW1KR0ZpTUdqbVFtLXRZNHNuVzFPRTZSWkpfRmdnUDAyLS01WFFDcjNRblAwU0x0NEppN05GalpHUUF6SFJ3ZlI0UXRQUV9LMlZ6bURZckRra2Z0SzIzODEzUQ?oc=5) - Google News source discovery | MoneyDJ Fri, 29 May 2026 04:25:00 GMT
- [光耀公告調整本公司114年度個體財報第67頁部分資訊- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNQXlENzQ1c0dGWEtxUHowMkQzcFA2ZmRKYVNlU2k2TFVRUXlrZTgwUXRaQ3ViVHU5ZENXNlhwcUJaVVRiNzFZVTBadUsyRWN3LVpxR2dqRHBqMDNacXNoelp2LW5WNmtVbFBIYTlZc2dEbVBoUTlWZGR6VzdfSUFpTzBzc09vSGk1bzFhWkNBUDZYUQ?oc=5) - Google News source discovery | MoneyDJ Sat, 30 May 2026 09:16:00 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：童子賢：股市過熱要看本益比台股還沒有過熱| 產經 - 中央社 CNA；這家「七巨頭」之一本益比僅19倍！分析師：可能是十年一遇買點 - news.cnyes.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | -8.49% | -2.20% | 450.24 | 506.69 | -11.14% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [童子賢：股市過熱要看本益比台股還沒有過熱| 產經 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE5GaVctQXJBYjFNdmx1dXo5RVNDb2hoaDA3ZW1ZUE1XeHlpVXBqcWdiZVI5ZjRUbjE0ZlNvRE1aUVlVQ1NZRjgwM2kzN2tpY1lSQklGMnNSdXEyRDZUemc?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 30 May 2026 02:14:00 GMT
- [這家「七巨頭」之一本益比僅19倍！分析師：可能是十年一遇買點 - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTE9YTHV2WTBXSC0tWDFVZ2hTaXJPZlBPVW1vcXRmLVZvdzIzemVrdENtT28zZlFUekhXbFdkLWdkLVItVlB6dXBrSmRJRXNkeXc?oc=5) - Google News source discovery | 鉅亨網 Sat, 30 May 2026 08:00:03 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：AMD Is Up 5% Today: Is It Outperforming Other Chip Stocks Like Intel and NVIDIA? - AOL.com；台積電先進製程命脈！這水廠掌全台半導體45％再生水逆轉虧損大賺內幕- 產業 - 工商時報；證交所攜手台經院與資策會推出半導體、電腦及周邊設備、電子通路、綠能環保及生技醫療產業之洞察報告 - TWSE 臺灣證券交易所

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 114.68 | 114.68 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | 0.00 | +3.74% | +4.43% | 2,355.00 | 2,355.00 | 0.00% | 不適用 | 74.39 | 31.66 | 410.73B TWD / 17.50% | 2026-05-01 |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +21.07% | +10.47% | 211.14 | 211.14 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | N/A | N/A | 516.10 | 516.10 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +10.73% | +26.75% | 144.50 | 144.50 | 0.00% | 不適用 | 4.00 | 36.31 | 22.66B TWD / 10.80% | 2026-05-01 |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 971.00 | 971.00 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | +6.63% | +9.90% | 1,694.98 | 1,694.98 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | +44.35% | +34.85% | 446.77 | 446.77 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip, foundry。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AMD Is Up 5% Today: Is It Outperforming Other Chip Stocks Like Intel and NVIDIA? - AOL.com](https://news.google.com/rss/articles/CBMigAFBVV95cUxPUFk0Q0ZneEk5ZlR5eXlxdWEza0NXdVNVX0J4c3dfVFhwR19lUVVZVzlCTm1VZzdnRFI2el9XSlVWdXhvZUdrblNhSEM1dl9LSkhaUWJGdzZIcFFfenY1dGR4S2RTaHhLRFpCNm1uTWV4bTc5TGVBVDdiMVJCRE42OQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 30 May 2026 14:20:43 GMT
- [台積電先進製程命脈！這水廠掌全台半導體45％再生水逆轉虧損大賺內幕- 產業 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE12Q3ZVTVBKdG9FVUNlRFpEWlU0dUd2RHdPUGpuVzhLVVBRb25yYUszWnNSMmhqcng0eHJYV1hscmgyNUhXZWdQTDlXTW9jZnFkYXd5LXlZaUVZeGE1VENV?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 29 May 2026 23:24:00 GMT
- [證交所攜手台經院與資策會推出半導體、電腦及周邊設備、電子通路、綠能環保及生技醫療產業之洞察報告 - TWSE 臺灣證券交易所](https://news.google.com/rss/articles/CBMinwFBVV95cUxQRy10VUFEQVV1dTNiUXROQVdHV0pDZmNSWFpEOHRDWDF6ZkduX1V3MVFuZ2dYUTVyX216dTN4NTU4Q3lDcUVuWU9DX3JRek9XMW5sTzNuNWFWNjhLLTFnQUMyMW5rVWREUnZmQ3F3NmY1NFRoenM2bFd1djNrc0c3blhVV3BfQUV1Z0s1MkszTDByb05zenZJUzFmOUFaNVk?oc=5) - Google News source discovery | TWSE Fri, 29 May 2026 09:10:41 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
