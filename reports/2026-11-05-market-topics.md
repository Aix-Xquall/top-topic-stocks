# 每日股市熱門話題分析 - 2026-11-05

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **綜合市場情緒**｜負向｜熱度 45｜市場確認 83.92｜同向 1/1
2. **AI 伺服器與資料中心**｜負向｜熱度 14｜市場確認 86.23｜同向 7/8
3. **記憶體與 HBM 供應鏈**｜中性｜熱度 5｜市場確認 N/A｜同向 0/0
4. **散熱與液冷供應鏈**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
5. **消費電子與手機**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.13（樣本 12）
- 5日相關係數：-0.53（樣本 10）
- 同向比例：8/12

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 綜合市場情緒 | 83.92 | 1/1 | 0 | +4.64% | +6.80% |
| AI 伺服器與資料中心 | 86.23 | 7/8 | 1 | +8.33% | -1.58% |
| 記憶體與 HBM 供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 消費電子與手機 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：BigGo | 0.00 | 0/2 | 2 | -16.70% | -13.67% |
| 關稅與供應鏈轉移 | 0.00 | 0/1 | 1 | -12.37% | -0.31% |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-10-23 | 0.35 | 0.29 | +78.95% | 19 |
| 2026-10-24 | 0.09 | -0.31 | +70.00% | 20 |
| 2026-10-25 | 0.41 | 0.78 | +64.29% | 14 |
| 2026-10-26 | 0.27 | -0.25 | +36.36% | 11 |
| 2026-10-27 | 0.07 | 0.31 | +50.00% | 18 |
| 2026-10-28 | -0.30 | 0.47 | +20.00% | 15 |
| 2026-10-29 | -0.05 | 0.04 | +42.86% | 14 |
| 2026-10-30 | -0.00 | -0.05 | +47.62% | 21 |
| 2026-10-31 | 0.50 | -0.68 | +80.00% | 15 |
| 2026-11-01 | 0.47 | -0.40 | +85.71% | 14 |
| 2026-11-02 | -0.15 | -0.06 | +27.78% | 18 |
| 2026-11-03 | -0.03 | 0.08 | +40.91% | 22 |
| 2026-11-04 | -0.21 | 0.35 | +15.79% | 19 |
| 2026-11-05 | 0.13 | -0.53 | +66.67% | 12 |

## 歷史回測摘要

- 回測日期：2026-11-05
- 近5日 3日相關：0.18
- 近5日 5日相關：0.27
- 同向比例：+57.89%
- 權重狀態：未調整

- 方向準確度：+57.89%
- 信心排序準確度：0.18
- 診斷：弱正相關

調整原因：近 5 日方向與信心排序皆偏弱，降低方向詞與供應鏈推估權重，並加重背離扣分。；關鍵詞×公司後續樣本有效 4 筆，未達 30 筆，不調整樣本權重

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

摘要：綜合市場情緒 相關新聞集中在：外資狂砍1,499億元！三大法人賣超1,597億元 台股「V」型強震1,885點 - 經濟日報；台股收跌358點 兆元成交量拉出千點下影線 台積電收低35元 - 經濟日報；台股震盪走低跌逾千點 跌破42000點關卡 | 產業熱點 | 產業 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | -0.42 | -4.64% | -6.80% | 2,265.00 | 2,480.00 | -8.67% | 同向 | 86.28 | 26.20 | 511.86B TWD / 54.65% | 2026-10-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。

### 主要來源

- [外資狂砍1,499億元！三大法人賣超1,597億元 台股「V」型強震1,885點 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBfZXl5WXJSMkpId1pZNjRhNXNzM3pUdVB3UktxejA2aVBPSXVNcjlROXNTWGNhVmJrcDVfTnpTVkxPMzVWY1F0NGV3WlFkTnNGbksyWld0S2dGd9IBX0FVX3lxTE1HNy0xZU5mLTNxR1ZLbW1yLVVGRjVKYmZVQUFqZjZkbFFXWWVfWlJCSE91djlQalV0SW9vcHNEX1IzanlWWDJ2YkpHNjVZWDNRclhGakFiUGQydjhqWEpr?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 04 Nov 2026 08:00:00 GMT
- [台股收跌358點 兆元成交量拉出千點下影線 台積電收低35元 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBNSXhuSEFCT0ZXNDhhV3Jub1M5YUpmY29od2pUTnRGLUVxdE5leFJJLVp1TmpvanlhTzhNMklkZ2xUM0ZpNWM3RGlyWFA1a29NRy1KNnJEQi1XQdIBX0FVX3lxTE53d3E4SW1MeXdLRjVUMkNrR0tNRHB2YUxiMkdVdDhQUS10b0hzX2F2LWp2MHFWckhMa1VqSW1vLTF4Uy0zWTJ1VlZGd1VqSzROS0NLUVZUTGhIMGhrakRV?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 04 Nov 2026 08:00:00 GMT
- [台股震盪走低跌逾千點 跌破42000點關卡 | 產業熱點 | 產業 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9OME04MlU2RjJXdXQtekNybkhYTmdFZmE1U3htcmVMQXcxY2N5ZUttcUY5ZHlpOUVVbFJMNS1iUFVLR0hNem5vcVF6Y3pKTlloVVR2YjdaNm9iZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 05 Nov 2026 01:36:49 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：AMD’s AI Boom Puts It On Track To Outsell Intel For The First Time – Analysts See More Room To Grow - Yahoo Finance；Prediction: This Could Be the Best AI Stock You’re Not Talking About - 24/7 Wall St.；民主黨重返多數對 AI 與資料中心發展非全然負面，一文全面了解原因 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.54 | -49.19% | +43.66% | 58.27 | 114.68 | -49.19% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.53 | -5.29% | N/A | 488.78 | 516.10 | -5.29% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | -0.06 | -12.37% | -0.31% | 200.13 | 228.38 | -12.37% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.06 | -4.64% | -6.80% | 2,265.00 | 2,480.00 | -8.67% | 同向 | 86.28 | 26.20 | 511.86B TWD / 54.65% | 2026-10-01 |
| MSFT 微軟 | 產業/供應鏈推估 | -0.02 | +23.45% | +12.97% | 555.80 | 555.80 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -7.32% | -16.39% | 325.48 | 446.77 | -27.15% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.04 | -6.14% | -9.78% | 582.00 | 703.00 | -17.21% | 同向 | 13.92 | 45.37 | 88.13B TWD / 45.52% | 2026-10-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.04 | -5.11% | -12.28% | 3,580.00 | 4,920.00 | -27.24% | 同向 | 60.69 | 61.35 | 55.40B TWD / 1.97% | 2026-10-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：衝擊。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。 方向判斷命中詞：衝擊。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：衝擊。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AMD’s AI Boom Puts It On Track To Outsell Intel For The First Time – Analysts See More Room To Grow - Yahoo Finance](https://news.google.com/rss/articles/CBMikAFBVV95cUxQbENTZEtqblB0VE1MOUJWbmprcllrd0ZCNUtEcC0tdHFGUHVDaVBWNmpRM2NnUjVGajl1M3Bpd1N5ZF9KU0UyUDVQMFF2SjdTTWtZbWkzVGxPQ0xxSlNFMW12bEFMRnByT0QtNk9pWU1TcUlZQTVJSi1iQWhEVHN3amtRU1lQcVdZQjc1SDNmMjE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 04 Nov 2026 02:27:00 GMT
- [Prediction: This Could Be the Best AI Stock You’re Not Talking About - 24/7 Wall St.](https://news.google.com/rss/articles/CBMirwFBVV95cUxQWVByUzh1QzIzOHdFb2tRN3ZoWGRLcy1aTWoyQUZxd0dtRWZBaTR6R2VHNm9Va19KdXpkYW1zc1MxRXFQQVJqMU5JdDlibEs4NmNNdmlmU19WeUhWMjJscUpPWE40UEo5Q2U4TXVZeTVENWM5bUtXa3JPejBwRTB6WU9RNy1JYmdwLXRIcUV3UER0YmVqSHZ6WGExVXROMUFXWmVEa0toUkVscHdmM3BV?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 04 Nov 2026 16:03:00 GMT
- [民主黨重返多數對 AI 與資料中心發展非全然負面，一文全面了解原因 - TechNews 科技新報](https://news.google.com/rss/articles/CBMi5AFBVV95cUxOUGVDenlEM3UtZWgtdmljUmsweklybWo0U0x2RG9BcElPOEdIX0JwTEtOekZxdkUtZE8tWG11eUZHMVVpWnYtcmNpWUNua3YyMTRueDJvWUhkQTg5QzJVTEVrT0FLdUtLV2xMdnBZdmtrb3ZNOHZkbnlkV0x3Vm1WX1lGbUxaSlR6ZWxITnN2azNwQ0tXbVFoRVRrdDAwWDJmbEdGNy10aVpyNkgyV28tU1UtYzBFeFUtT1BNbTJnaDV2c0NnUG9ZYkFJNDZUS3Fid1NPQUNEQTRvU21vMU9kQmdSd3k?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 04 Nov 2026 22:15:00 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：US Pre-Market: Memory Chip Stocks Rally Broadly, SanDisk and Micron Each Up More Than 3% - BigGo Finance；SanDisk Retreats 9%, Micron and Western Digital Fall 7% as Election and Memory Price Worries Weigh - 24/7 Wall St.；Why Micron, Sandisk, and SK Hynix Stocks Suddenly Reversed Course Overnight — and What It Means for Investors - TipRanks

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | -18.10% | N/A | 795.23 | 971.00 | -18.10% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | -15.30% | -13.67% | 1,126.52 | 2,335.00 | -51.76% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -12.37% | -0.31% | 200.13 | 228.38 | -12.37% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、memory」，共 4 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：fall, weak, rally, shortage。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：fall, weak, rally, shortage。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [US Pre-Market: Memory Chip Stocks Rally Broadly, SanDisk and Micron Each Up More Than 3% - BigGo Finance](https://news.google.com/rss/articles/CBMidkFVX3lxTFBKU0ZYTXNYWDFJNmZaOWlhREVZRHVwdE1fM2UtVl9tWjNrWWhwVDdjRFVMczRZWkg2VWVKVTdaMjlwZjRqZm55eVh0VEZHaDhjYVhraXlXdFRnbGNKaU9jSW1UWVU0b0l1ODhlVlNUNXUyVVduZlE?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 03 Nov 2026 12:06:00 GMT
- [SanDisk Retreats 9%, Micron and Western Digital Fall 7% as Election and Memory Price Worries Weigh - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi0wFBVV95cUxPYUlTdE9VUUNsNlB0a1M5S3RsVnZsODVyQUJ6NnBZZlBadkM4a0czWUI5Uk1MQlI2SkJlSzVCWjlrUUhGaFUwUllxbko5THNSVE1Nb1ROd0JXOWg0T3VOYi1GVGVXVE81T2pyaURBWHJ3czBGMlVKZU9NYTVMT05vMTlGNDhmWjBTUEFLNWNqRW9lNVo0NnZQdkJ4MnpacGUxVFY5R2JpYmVjS1FiRFdrdkxIQng1TGlmeElPNmhGRTBFNGEwUlluVFVIejRHVlFSNTJV?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 04 Nov 2026 16:02:00 GMT
- [Why Micron, Sandisk, and SK Hynix Stocks Suddenly Reversed Course Overnight — and What It Means for Investors - TipRanks](https://news.google.com/rss/articles/CBMi0AFBVV95cUxOV1htcVRWUHJ3VlFiVVRCZ19paWgzYnpyYnJOZDRPaXltRExheTFVbS1ndi1kWlJ2clBFRndNamEzSEVZeFJVQnNDQ0ZzM2YydjFFT3BWSWhfVnVlbjBmdTE4OXhPaUFVeVZRTllRNDc2bFd1bXVRdmtHazJVQ2RUUmhyb0NKU0tmR0Jqc1VWLUtKdDVlTko0dm85NkxCbnpzQjU1Qy1RaWsxT05GMmVaWE1qOEIyNll0eGpENEg1OFdBeFhJaEtqVDNjMkVuejFU?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 04 Nov 2026 02:56:19 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：輝達GB300大單帶旺業績！「散熱零組件廠」第四季EPS挑戰2股本 目標價喊上3100元 - FTNN 新聞網；馬斯克喊話SpaceX太空散熱更容易！AI運算衝上軌道！ - 蕃新聞

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | -8.89% | -12.29% | 2,640.00 | 3,435.00 | -23.14% | 不適用 | 75.13 | 37.59 | 21.02B TWD / 44.92% | 2026-10-01 |
| NVDA 輝達 | 新聞直接提及 | 0.00 | -12.37% | -0.31% | 200.13 | 228.38 | -12.37% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 2 篇新聞命中。 同時符合主題標籤：thermal。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [輝達GB300大單帶旺業績！「散熱零組件廠」第四季EPS挑戰2股本 目標價喊上3100元 - FTNN 新聞網](https://news.google.com/rss/articles/CBMiS0FVX3lxTFBiMFZwVnIycldIanVrSThXSk1sbzBQdzM4TWVUNkVKRTl1ZEdtMWxuUjJyYTJMVGFrNmpIWUlzNElPbjVEdnZ5aHQ2bw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 04 Nov 2026 15:40:00 GMT
- [馬斯克喊話SpaceX太空散熱更容易！AI運算衝上軌道！ - 蕃新聞](https://news.google.com/rss/articles/CBMiUkFVX3lxTE5HNmlvZnpYSTRnTU5pVDVzT1N4Ri1tOE1MT0lwcVF1X2d3bUh5QXZPTmo2T2ZlWE42VXhtUHZtU0owVmFUX1g1N0ZwNjlBajlGb3c?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 04 Nov 2026 00:00:00 GMT

## 消費電子與手機

摘要：消費電子與手機 相關新聞集中在：高通手機晶片營收遜、蘋果訂單流失 盤後摔 - TechNews 科技新報；Qualcomm stock drops 7% on weak earnings forecast as memory shortage weighs on smartphone sales - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AAPL 蘋果 | 新聞直接提及 | 0.00 | +12.00% | +25.34% | 349.51 | 349.51 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2454 聯發科 | 新聞直接提及 | 0.00 | -5.11% | -12.28% | 3,580.00 | 4,920.00 | -27.24% | 不適用 | 60.69 | 61.35 | 55.40B TWD / 1.97% | 2026-10-01 |
| MU 美光 | 新聞直接提及 | 0.00 | -18.10% | N/A | 795.23 | 971.00 | -18.10% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | -2.24% | -4.57% | 238.00 | 289.00 | -17.65% | 不適用 | 15.21 | 15.82 | 1158.63B TWD / 38.42% | 2026-10-01 |

關聯理由（前 3）：
- AAPL：新聞直接提及「蘋果」，共 1 篇新聞命中。 同時符合主題標籤：hardware, consumer electronics, smartphone。 方向判斷命中詞：weak, shortage。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2454：新聞直接提及「手機晶片」，共 1 篇新聞命中。 同時符合主題標籤：smartphone。 方向判斷命中詞：weak, shortage。
- MU：新聞直接提及「memory」，共 1 篇新聞命中。 方向判斷命中詞：weak, shortage。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [高通手機晶片營收遜、蘋果訂單流失 盤後摔 - TechNews 科技新報](https://news.google.com/rss/articles/CBMingFBVV95cUxOV08tSTFPdUNRZEZabmZBUks4TFNWTktHbmZSa0RhS2dLSE1BNTVFTWlhaWY3aU1DZGF3RG1MZlpRbDJJalcxSzd1R25XeUEwOUt1eHVzVVpneDlIVUJ0UFA2QWV0d2tMZElhREhmdGZuVThNMC0xT3NJN3JFS05YX1NiUkgyb0RpVHE4STZXUUtpUkstX0Z5bzdIWWJHdw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 05 Nov 2026 01:09:59 GMT
- [Qualcomm stock drops 7% on weak earnings forecast as memory shortage weighs on smartphone sales - CNBC](https://news.google.com/rss/articles/CBMif0FVX3lxTE9KdnBhYm1hakZ1aldQNm80ZGNKSmUtY1JqWHVZem5QZE1DVE00UmZfeldSNWJ6b0FOekhBQzlPbWJPRC0zclJQMGVxaWFiOGtSWWxGSVUzVXl3RU9lLWJNN3kxR19iZEpQV2NjM2F4aTFiWkg4bzhoRF9mQzJjZzDSAYQBQVVfeXFMT19QY1RERExyM2ZhYTBmU1hLNXJhWlo2UEJmMGEyR0lIVzVfQWFGcWRLMmtaSk5lM2N6N3N6NUh4TW9HN3FtUENWdWtleTFFVzVWN01EODExQUlXMXdXcTlnckEwcXA3S2tZSVFVM2lqNGtrR285NXVzLXYyaWRycXF1TnV1?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 04 Nov 2026 21:06:06 GMT

## 新興題材：BigGo

摘要：新興題材：BigGo 相關新聞集中在：US Pre-Market: Memory Chip Stocks Rally Broadly, SanDisk and Micron Each Up More Than 3% - BigGo Finance

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.21 | -18.10% | N/A | 795.23 | 971.00 | -18.10% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.21 | -15.30% | -13.67% | 1,126.52 | 2,335.00 | -51.76% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron」，共 1 篇新聞命中。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 1 篇新聞命中。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。

### 主要來源

- [US Pre-Market: Memory Chip Stocks Rally Broadly, SanDisk and Micron Each Up More Than 3% - BigGo Finance](https://news.google.com/rss/articles/CBMidkFVX3lxTFBKU0ZYTXNYWDFJNmZaOWlhREVZRHVwdE1fM2UtVl9tWjNrWWhwVDdjRFVMczRZWkg2VWVKVTdaMjlwZjRqZm55eVh0VEZHaDhjYVhraXlXdFRnbGNKaU9jSW1UWVU0b0l1ODhlVlNUNXUyVVduZlE?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 03 Nov 2026 12:06:00 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：整理包／黃仁勳概念股笑了！輝達季度財報超預期 完整台廠供應鏈名單、潛在受惠股一次看 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.21 | -12.37% | -0.31% | 200.13 | 228.38 | -12.37% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +12.00% | +25.34% | 349.51 | 349.51 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | -2.24% | -4.57% | 238.00 | 289.00 | -17.65% | 不適用 | 15.21 | 15.82 | 1158.63B TWD / 38.42% | 2026-10-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [整理包／黃仁勳概念股笑了！輝達季度財報超預期 完整台廠供應鏈名單、潛在受惠股一次看 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBQUlViSHpPeDVlY29yaHFNNE5NcVlUQnE3ZThTcXRGNHgxYTVPOVVTRDlaTDV6Zml5WEwxVHNSeGFDcnVHUHhRSW15SzNpU0dYVDU3dThWNEVCbkZI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 03 Nov 2026 08:00:00 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：國票證券：台股有機會醞釀反彈行情- 新聞 - MoneyDJ；統一證券：台股技術面進入超賣區，短期醞釀反彈空間- 新聞 - MoneyDJ；《台股盤後》盤中V轉、收跌358點，42K失而復得 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [國票證券：台股有機會醞釀反彈行情- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxOMnE2cHY5cVRxMUprTWw5VlEtelpGMEEzakVTOHF4LTE0UjdQTlVDQllNMU9WYm5sRDNzMmhRXzRfa19PSEJma29XOUU1NTMtTkVFaGRMT082aEdOQkVxMHlCUnlYb3FuM1g1M1hwdFQ5VUREeXNWdUltOVhtclBaWnY2SjJkUnpNYURYeEFBNXAyZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 05 Nov 2026 00:39:00 GMT
- [統一證券：台股技術面進入超賣區，短期醞釀反彈空間- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNYVFCckZ0TW9EZEZIR2JiaHo5SHpuUUR4aTJiQS0yZ2dPVHpxcldWanN6b1RDdVJGcENCaEJ3U3g0ZXBVMTdWMWR4MEM0d3lUQ0d2bC1hSC11WnVNMkw1SkFycUg0RFhpMDI1a1kzenBXYWppaTVtYkV4bFRLdmgtZlRJRzl3VmtBaDNLcmlWWkJvUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 05 Nov 2026 00:39:00 GMT
- [《台股盤後》盤中V轉、收跌358點，42K失而復得 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNN1hkVjVlLXdKNEpOMjJXM0xyUHk4MnQ3dF9Ub0JrSjBUYzNNVWsyRXRWb0wyWEkyV0VrbXdsaVJDc0FSOUVuZUQ5b1dwUVA5d1BIcWdnQXY3c29aaFhraU1yc2dqRk9ERUtWaXkxN2ZQQUJxRXRaejNBb0t6TEhUazQwcF90SXB2Ui05TjBMaEZ2UQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 04 Nov 2026 07:46:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
