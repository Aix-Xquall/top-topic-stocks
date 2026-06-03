# 每日股市熱門話題分析 - 2026-06-04

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **AI 伺服器與資料中心**｜中性｜熱度 13｜市場確認 90.39｜同向 6/6
2. **記憶體與 HBM 供應鏈**｜中性｜熱度 4｜市場確認 N/A｜同向 0/0
3. **關稅與供應鏈轉移**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0
4. **散熱與液冷供應鏈**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
5. **半導體與晶片供應鏈**｜中性｜熱度 4｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.38（樣本 7）
- 5日相關係數：-0.30（樣本 7）
- 同向比例：6/7

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| AI 伺服器與資料中心 | 90.39 | 6/6 | 0 | +6.80% | +9.19% |
| 記憶體與 HBM 供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 關稅與供應鏈轉移 | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：CrowdStrike | 0.00 | 0/1 | 1 | -14.80% | -49.97% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
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
| 2026-06-01 | -0.92 | -0.72 | +16.67% | 6 |
| 2026-06-02 | 0.08 | 0.05 | +72.73% | 11 |
| 2026-06-03 | 0.48 | 0.62 | +90.91% | 11 |
| 2026-06-04 | -0.38 | -0.30 | +85.71% | 7 |

## 歷史回測摘要

- 回測日期：2026-06-04
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

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：NVIDIA vs. AMD: Which AI Chip Belongs in Your Retirement Portfolio? - 24/7 Wall St.；Intel Up 250% in 2026: Is the AI Comeback Real or a Short Squeeze? - Gotrade；AI Bubble or Not, the Stock Prices of These Dotcom Darlings Are Soaring Like It's 1999 - Investopedia

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.72 | +7.61% | +21.20% | 214.75 | 222.82 | -3.62% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.72 | N/A | N/A | 112.71 | 114.68 | -1.72% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.70 | N/A | N/A | 542.52 | 542.52 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.07 | +2.97% | +5.43% | 2,425.00 | 2,425.00 | 0.00% | 同向 | 74.39 | 32.60 | 410.73B TWD / 17.50% | 2026-05-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.05 | +8.81% | -15.66% | 427.34 | 506.69 | -15.66% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.05 | +14.80% | +49.97% | 479.23 | 481.57 | -0.49% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.05 | +1.15% | -3.74% | 618.00 | 618.00 | 0.00% | 同向 | 10.86 | 57.38 | 62.25B TWD / 19.22% | 2026-05-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.05 | +5.45% | -2.05% | 4,545.00 | 4,545.00 | 0.00% | 同向 | 62.91 | 72.43 | 46.74B TWD / -4.14% | 2026-05-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。 方向判斷命中詞：raise。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：raise。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。 方向判斷命中詞：raise。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [NVIDIA vs. AMD: Which AI Chip Belongs in Your Retirement Portfolio? - 24/7 Wall St.](https://news.google.com/rss/articles/CBMirAFBVV95cUxPNS1qZl9fUXFEcUdURWNRVTI2aVZqYkV1SXo4c2t6bjVmR01lNHhJYks3VC1kRWdGMm5pcHFYTGgyZFBtRjZmSF91eURIOHRBdVlMcGczc2c4MWQzYWRwNWFqVldOSm9IUUdjZ2hEdEFxQ3lHM1U4d29TY2JfRFc2a2pMaUFVYi1PZUZNU2EzNUVOREtLSmtUM0tQMFZkWmFzM3QzMHdlXzNxR0di?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 03 Jun 2026 13:00:13 GMT
- [Intel Up 250% in 2026: Is the AI Comeback Real or a Short Squeeze? - Gotrade](https://news.google.com/rss/articles/CBMickFVX3lxTE9FV0EyYTFDS1V2WXo0RE5leTQzbGJFYTV6ZzFacGQtZjRxanpTckhmRFRDUndTd3ViYVVGc3JfdnRuNllQZDVrU1E4Y0ljSzdDVTVObWswN2xQdlJOdV9BQjNkcXVxdmlLZGVfUFJkVzI3Zw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 02 Jun 2026 10:29:29 GMT
- [AI Bubble or Not, the Stock Prices of These Dotcom Darlings Are Soaring Like It's 1999 - Investopedia](https://news.google.com/rss/articles/CBMi0wFBVV95cUxPbm5waTRSdTJzV1hldE05RF96bERyY2lEdTBkbmtoM2JQRVltdHMxU3ZteGpaTmlZelhmenZZX1g0ZW1MZERPR3FQbVJiMm81VzdhOU5odXhyaDlUZlZzeDFWajk4ZDlHSWZqaEZQZlJaRWtpT1ZJZUVqb05jUnRic0lIc3hjN1BrNjlQTEl5SVNfY0ctR1ZWMFpXY0FlYmE5R21MSVJvcmFiYUdKQU9OQVYxYmJ2TmtTOVdaMWVUYURBbnl0d3dVNXhtTjhOMTV4NDRV?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 02 Jun 2026 19:43:43 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Prediction: This Artificial Intelligence (AI) Chip Stock Will Soar After Micron's Earnings - The Motley Fool；Move Over, Magnificent 7. Traders Are Flocking to SanDisk, Marvell, Micron, and the Parabolic 7 - 24/7 Wall St.；Micron, SanDisk Rule The AI Memory Boom — China's Big IPOs Could Crash The Party - Benzinga

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 1,079.57 | 1,079.57 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | +8.05% | +15.19% | 1,831.50 | 1,831.50 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +7.61% | +21.20% | 214.75 | 222.82 | -3.62% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron」，共 4 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Prediction: This Artificial Intelligence (AI) Chip Stock Will Soar After Micron's Earnings - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxORi12ZTlPcFI0ZE1UUnNHdElVQkppNVZaMWZEblRnbGQ5d25RdVFxXzhiTjR1d2hBVHUwNkUzaHhialh3REp0NU5DbnRYbWlIdFljZjM0VFFNalJJdUdfWjg5NnlvRm5ReWtzcDh3OHVSTEVVdG5sX0p2YjkyUmtQZm82c0hxcFNVZzdiRkVvcnlfell3aDNEWQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 03 Jun 2026 17:10:00 GMT
- [Move Over, Magnificent 7. Traders Are Flocking to SanDisk, Marvell, Micron, and the Parabolic 7 - 24/7 Wall St.](https://news.google.com/rss/articles/CBMizwFBVV95cUxNSml6S0UySTkwZlNlLTU5UHdVRzJxelVmYjU5TDl5bEVnZEs3S2V5YXRDREVtRDJvaDRLckxna0dNRWhyZHhWWFdXWkdWOGdnV2d0VHpkWlZqTEhjYV9sMFZnSjlmT2hPS2VlaXQtb3MtQUNhejBwYzl2RWg2T042RkxWWDNselhockxUMXNoazhmbEFxMmpJVDh4bWRhbXluVUNHVnAwNGF3aU5SQzdHNEZoTTRWZ2R4SGlleU9FYWM0SjBxakVvVl81b0lpbkk?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 03 Jun 2026 19:12:27 GMT
- [Micron, SanDisk Rule The AI Memory Boom — China's Big IPOs Could Crash The Party - Benzinga](https://news.google.com/rss/articles/CBMiyAFBVV95cUxPR3Bvb2lvZXF3T1p0QkhxZnB3OUptTzd5RlhPTEtieTY3Zktmclh4SG5DdWJoQUNfa0Q0ZDVaRWxNaTNrdHY0Q05FQlFyaUxzUVlqQ2JqVlRiaTRVWExoVFdzNE5HWEZCLVB3b2RPTlhNQUFKS3NELVAtSEpGYkdOSGE5bEIxT3FzaDB3akZHVkE1SktvM01NR19wUlN3bzZOSERwakg3MXhLdXlsSjhRd2tsWTNCaVVJVFkwQ3A3ai1VbHFieFk1MQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 03 Jun 2026 14:50:26 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：台化 AI 伺服器防火塑料打入供應鏈，其全球競爭優勢為何？ - TechNews 科技新報；電子級低碳氫氣碳足跡極低，如何助攻半導體供應鏈減碳？ - TechNews 科技新報；美國制裁如何加速中國半導體供應鏈自主化？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +17.44% | +33.65% | 310.26 | 315.20 | -1.57% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | +6.92% | +17.05% | 309.00 | 309.00 | 0.00% | 不適用 | 14.13 | 21.95 | 832.10B TWD / 29.74% | 2026-05-01 |

關聯理由（前 3）：
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [台化 AI 伺服器防火塑料打入供應鏈，其全球競爭優勢為何？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiUkFVX3lxTE9mUFl0SnVuTjlSSGFEWDZTMTlnUS1kM05OS2p5dTVXWmVLY1Bhemp2RlFNamJoaEx6UEkta0xIT20zV1JtS0Nua1dzU0N6LXhxcnc?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 03 Jun 2026 20:58:10 GMT
- [電子級低碳氫氣碳足跡極低，如何助攻半導體供應鏈減碳？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiUkFVX3lxTFBfY3NBY0taNkJlZTh3SWhySlgxRnlQTXUybjZPbThoekQtNXZSb0ZkSV9kM2ZUbW96aVhRNnNFRno4UE54SjFSQ25SLWdia0NkUVE?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 03 Jun 2026 20:58:09 GMT
- [美國制裁如何加速中國半導體供應鏈自主化？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMinwFBVV95cUxQZjRJRWNtdDFPUUVIa3loeDN4MFRIbk1GdlJjTjJlcEJjTHN2UWxvajFpSEpmLTdIS1J3Q0ZHRVpMWVhmdExqRVh6Vjg4RzdsaGNGWllNU1FMTUU5NF9iRkNIVlFTMm9YOTFQdjM3UTBYcjNRX0RlQTVGZi16STBLU0F2ODBzdnQtMU9TWkNWZ3AtZnVxazYyOERnTGJXdXM?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 03 Jun 2026 15:35:06 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：輝達一句話 炸出散熱產業三個真相！Rubin降規效應掀波瀾 節能可以不用散熱？ - 財訊；奇鋐：2026年下半年將大爆發 訂單看到2029年 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | +7.13% | +5.74% | 2,855.00 | 2,855.00 | 0.00% | 不適用 | 61.06 | 46.91 | 15.63B TWD / 71.62% | 2026-05-01 |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +7.61% | +21.20% | 214.75 | 222.82 | -3.62% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱、奇鋐」，共 2 篇新聞命中。 同時符合主題標籤：thermal。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [輝達一句話 炸出散熱產業三個真相！Rubin降規效應掀波瀾 節能可以不用散熱？ - 財訊](https://news.google.com/rss/articles/CBMie0FVX3lxTFB5NExyc2ZVT0s0NnNLb1JLNnpucDctak5fSTBUeElVSXkxQTc2Y2N0aDNXY0QyRDdxMXVtNm5oRkxsN21uMFZqX0RpeDRSN2liXzhaRTdIeG5Od2JINTVfNHRIM2N0dEhOX19BQXZfdV93b0hSOW9Nc1N5SQ?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 03 Jun 2026 09:00:00 GMT
- [奇鋐：2026年下半年將大爆發 訂單看到2029年 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1rQVZJMTVHbVJ1c2Q0MnFVVUY0TGZ3akVQVkp1SnBfZ3hsekFwU0VEajEzTnJBTUtTT2Z0bmc1OUFWdTBCSk5UbWlxWHpLS0ZaTWs1WnFmcElZZ9IBX0FVX3lxTE1lWHktNVZnUTRHODFlSWVBTkp5Wm1VeUtBMnljWnF2RUw3YW5hUDVKOXo1anhSNlpfN043RHIxSXBBMWFwRFpEbnlQOWF3d1Q5Yk1SV0JOaXNuY1d6UUQw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 02 Jun 2026 17:04:08 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：NVIDIA vs. AMD: Which AI Chip Belongs in Your Retirement Portfolio? - 24/7 Wall St.；Forget Intel: Buy This Ultra-Efficient, Cash-Generative Semiconductor Juggernaut Instead - 24/7 Wall St.；Broadcom stock plunges on weak software sales, unchanged AI chip forecast for the year - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AVGO 博通 | 新聞直接提及 | 0.00 | +14.80% | +49.97% | 479.23 | 481.57 | -0.49% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 112.71 | 114.68 | -1.72% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +7.61% | +21.20% | 214.75 | 222.82 | -3.62% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | N/A | N/A | 542.52 | 542.52 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +2.97% | +5.43% | 2,425.00 | 2,425.00 | 0.00% | 不適用 | 74.39 | 32.60 | 410.73B TWD / 17.50% | 2026-05-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | -9.69% | -9.06% | 130.50 | 144.50 | -9.69% | 不適用 | 4.00 | 32.79 | 22.66B TWD / 10.80% | 2026-05-01 |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 1,079.57 | 1,079.57 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | +8.05% | +15.19% | 1,831.50 | 1,831.50 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- AVGO：新聞直接提及「Broadcom」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：weak, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：weak, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：weak, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [NVIDIA vs. AMD: Which AI Chip Belongs in Your Retirement Portfolio? - 24/7 Wall St.](https://news.google.com/rss/articles/CBMirAFBVV95cUxPNS1qZl9fUXFEcUdURWNRVTI2aVZqYkV1SXo4c2t6bjVmR01lNHhJYks3VC1kRWdGMm5pcHFYTGgyZFBtRjZmSF91eURIOHRBdVlMcGczc2c4MWQzYWRwNWFqVldOSm9IUUdjZ2hEdEFxQ3lHM1U4d29TY2JfRFc2a2pMaUFVYi1PZUZNU2EzNUVOREtLSmtUM0tQMFZkWmFzM3QzMHdlXzNxR0di?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 03 Jun 2026 13:00:13 GMT
- [Forget Intel: Buy This Ultra-Efficient, Cash-Generative Semiconductor Juggernaut Instead - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiygFBVV95cUxOaVo3bW1xT3lvcHV0Z04zUENvc2V3WFZnbDVZcHoyaW5FZVdCQ1NsOFpkMXRzNmwxeWdhc083NFVpZHpmZ3BCbTloS2FXZVdjM29pTkNzazNXeFhjWWRuR1lBb0VHendJa0xRa1dsN0tWNmhDd1drUmtFSTBkVENxd056VzlNUGlJS2JyeWlyMjIzazVpOHNNZHFoM09jX1lsZXRpSG5sQlgxNU5zbktsak1Cc2lPb3ltOHhwczJMWWZETEtZMlFFNGFB?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 03 Jun 2026 15:20:10 GMT
- [Broadcom stock plunges on weak software sales, unchanged AI chip forecast for the year - CNBC](https://news.google.com/rss/articles/CBMif0FVX3lxTE9MUWNtalczVVl2UEVtVFhSUF9QVnZVd2ZuU01aaFZaTGZuOWpNWW1Wc1Y3Q050V1ZiRWs3MVE0R3ZUd196Sno4LUZkWUJadnRHaWI5VHpLVGRwQTBTZkJuY2JZelp1VWQyUTlpYVJrVTd2YkdSblQwNzV6dmk0aknSAYQBQVVfeXFMTTBfUHNDN2g0eG9Gc3VON0cwRFlFRUhLcDBMbmNZUXVPcTFVWFNwWTZibW51MkFuS1BON0xTTXVHbFd6N21LekpLZVF5NFBobnJTTnJxa0VhdGxzV3hDS3RYc2RIWHJlMG1LR2xXUlYtSGhsbGx1Y3JsTm8wbk5UUXhOZGJU?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 03 Jun 2026 20:20:29 GMT

## 新興題材：CrowdStrike

摘要：新興題材：CrowdStrike 相關新聞集中在：CrowdStrike narrowly beats estimates on AI tailwinds, but stock falls 10% - CNBC；Where Jim Cramer stands on CrowdStrike and Broadcom ahead of earnings - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AVGO 博通 | 新聞直接提及 | -0.28 | +14.80% | +49.97% | 479.23 | 481.57 | -0.49% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- AVGO：新聞直接提及「Broadcom」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [CrowdStrike narrowly beats estimates on AI tailwinds, but stock falls 10% - CNBC](https://news.google.com/rss/articles/CBMiekFVX3lxTE5mMmg0R2VTZFFEQXJXclJTQkQ1Zm04UV9PTFZuTnAwWlU0WGhTVGNEOGVLZE1RZ3FOaWw5SDU0clFtTFEtNDNibldlVHdtLUNEYm1YT0JuRGJxUjg2QUNKT1NfZG01dWxqaVAzLUNmSzZMYS1tclQyeE9n0gF_QVVfeXFMUFlxeTBqbXVLeUV2blJHdTdmbHUwRFRYbjd2ZFVHTThpbHVGeHBob3dRQm1qLWtMZ01MRTIzcU9ZTnlRc181Y19reTQyLVg4QndaUUMzbGZzSGxVcldZeEdhNTN4bDZsSHdXX0NINF9IWGpic0ZUbXN2QmhPUUlIOA?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 03 Jun 2026 20:47:57 GMT
- [Where Jim Cramer stands on CrowdStrike and Broadcom ahead of earnings - CNBC](https://news.google.com/rss/articles/CBMiqgFBVV95cUxNb1AxU3dyaHB6cWJvZzBvbzcxMWtkYl9BWVZRdjdaVGctYVVsRTk0ZWI2UFdRa2gwcGRhblpsUWdQUjFWeHdEXzlGbEZPNHdCWnFJbmM5ODlYUzlTanBaMFpwRXdXNVl0d1ZEdXl0bUdmbGY0aHBxUHBheDFNMFE1SFR1bC00RjZobHFXbVloWFNNT2ZfVEg5UVJ5QjR2VDkzTHVHQ3U3Z01LQQ?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 03 Jun 2026 16:25:01 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股連四天創高 漲了2,823點 - 經濟日報；台股電金發威攻上46K 大盤寫五紀錄 千金股重回52檔 - 經濟日報；台股基金十強 強勢上漲 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股連四天創高 漲了2,823點 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxOcXdtS1pXLVRHQjlNRFRQcUV1dHB3ZHhrZUN2SkZxTkY0SndWQlJVYXJUSFFhcGR4TVk1RWlFQmlJNGJzajcxR0JrMS0xUHdoU29nc2tMY2x0d00xWVBpWnhnaUt0ZzZFSTMzQzZ3M0JjMmhYam5heW1Fd3ZKUkpTb9IBX0FVX3lxTE1fU1lnV1A1V2tJV3RMc3RpbHBhc2FuTXV1OU1aS0hrZUFmZENnNi1fOF9keTVKaUwxZEcwUWZRNE5sQWY1cDBsZXFYYmwxenJFZWdBMmdTZUdtQ1doV1hn?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 03 Jun 2026 02:00:00 GMT
- [台股電金發威攻上46K 大盤寫五紀錄 千金股重回52檔 - 經濟日報](https://news.google.com/rss/articles/CBMikAFBVV95cUxOaVgtRG1oYlp5czR5WlBMM052ZTA4aXp6ejhtMFowTHpibkhuMFNsMEFWSTNzQ1JqT2lQb2UwRTJUNDdPNmFqMF9kUmJLejdhZ0JyNFVNZ09haE80eVR0dWVQLU5EREMxazVxMmVkMlVaU3pwa2tOWFZQSFF3TFRMSUFyRGc3Smp2SzhWVmdPRknSAV9BVV95cUxOVHItbHNOdHlDdW9hV0tqNUlsOEF1MzBQZXZTTTRpTWpsUzVOYmlMdWQxWFJ4ZXQzZ1ctNnNYLU14WjFjNURLYmFhSTFkdUQ1LVN2NlRtOHdyM2daa2p0TQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 02 Jun 2026 09:00:00 GMT
- [台股基金十強 強勢上漲 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxQaTJpMFowMHZtQ0w5ZF96Z0RRZTNlMzdyVkZ6RXZER0tyaTREeWlwWTFlNjV5R1o4RFZaQl93T2lUNk9KUW5WMVMybUllQ25XNnU3clBKTXBmVGx0WmpTZFdMTWo2aUhSZFptTUJOT2lESWtYem1FcGhRUTZkZTZuT9IBX0FVX3lxTE5MWW5FMlVta3M4cXoxMDVBWFhKcFF3bDdDN3hQNU5oMGFGRlhhRUw1ajJBaVR5SUZlNXRHc2FzdG1Fc0xhVjdlZFJXNVl3d2RON2diN1gtQlJQT3pJazdJ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 03 Jun 2026 16:48:15 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》上漲901點、首收46K，日K連四紅-新聞內容-基金 - MoneyDJ；《台股盤後》上漲901點、首收46K，日K連四紅- 新聞 - MoneyDJ；《金屬》需求擔憂影響 LME基本金屬全面下跌-台股 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》上漲901點、首收46K，日K連四紅-新聞內容-基金 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxPQlVOYUdMZ3FLQWlGRXN3SHJLOGxmank3MDk3emVwZW1vN1B4RTByVTd5eTdTZzFMNHkweGJkc2ZOb1JPUjU4dzdldzA1azUwVmF3eXlsa0RDMjJKM29jdzF4cy1mcnVpVm96ZXozU28wckctNWxhMnBiOHdHREgxMGJpVHpHeFhleGRRVmNBdHQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 03 Jun 2026 08:18:00 GMT
- [《台股盤後》上漲901點、首收46K，日K連四紅- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMilgFBVV95cUxOUlJnd1IzdmNNTjZCVEVCaktWclJVb3pvWERXUE9HX0VoQmNNRTdVbFhtSVJ6Rmo1RUpWaUJKb0g0NUxjcXRadFRyMXNSV2M4TjEyUkRMWlozUm9uVktqN3Q4OWNJdk5qSW9IN1VTTGEzNHd6OXJ3ZHBaaGpSTFN6X3BKTW9UWGZGaDdWUWxvOFE5UTgxNlE?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 03 Jun 2026 08:16:00 GMT
- [《金屬》需求擔憂影響 LME基本金屬全面下跌-台股 - MoneyDJ](https://news.google.com/rss/articles/CBMiigFBVV95cUxNWlhzc3ZaT2xGNGF2ZDh5b1JxeG5OYS1kajdyVWQ1ckxYaHBVMVQ2UkQ2SkgydXUyM19zVFhHQmZoeHEwOHd0elRHYkNKZ2pZcFpnZW9xNnBscW9LODZFWF9qYld6SEtNTjVvLS1KaTFaZkd3T2NpRV95WERnNVVGd2JGTmVvZnhYR1E?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 03 Jun 2026 22:17:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
