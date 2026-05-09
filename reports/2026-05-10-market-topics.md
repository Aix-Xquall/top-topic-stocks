# 每日股市熱門話題分析 - 2026-05-10

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **AI 伺服器與資料中心**｜正向｜熱度 14｜市場確認 76.67｜同向 4/6
2. **記憶體與 HBM 供應鏈**｜正向｜熱度 11｜市場確認 89.31｜同向 2/2
3. **半導體與晶片供應鏈**｜正向｜熱度 6｜市場確認 100.00｜同向 5/5
4. **散熱與液冷供應鏈**｜負向｜熱度 2｜市場確認 98.83｜同向 1/1
5. **先進封裝與 CoPoS**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.31（樣本 14）
- 5日相關係數：0.49（樣本 14）
- 同向比例：12/14

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| AI 伺服器與資料中心 | 76.67 | 4/6 | 1 | +10.46% | +14.47% |
| 記憶體與 HBM 供應鏈 | 89.31 | 2/2 | 0 | +6.43% | +19.44% |
| 半導體與晶片供應鏈 | 100.00 | 5/5 | 0 | +10.26% | +23.12% |
| 散熱與液冷供應鏈 | 98.83 | 1/1 | 0 | +9.61% | +13.76% |
| 先進封裝與 CoPoS | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：AI伺服器 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：B729 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-05-08 | 0.03 | 0.48 | +76.92% | 13 |
| 2026-05-09 | 0.10 | 0.55 | +33.33% | 9 |
| 2026-05-10 | 0.31 | 0.49 | +85.71% | 14 |

## 歷史回測摘要

- 回測日期：2026-05-10
- 近5日 3日相關：0.15
- 近5日 5日相關：-0.00
- 同向比例：+38.46%
- 權重狀態：未調整

- 方向準確度：+38.46%
- 信心排序準確度：0.15
- 診斷：弱正相關

調整原因：近 5 日有效樣本 13 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：AI 伺服器與資料中心 相關新聞集中在：股海自由行／AI 題材績優股 長線還有戲 | 證券達人 | 證券 - 經濟日報；台股 ETF AI 熱潮催動漲勢 群益半導體收益單周勁揚逾16% - 經濟日報；ARM vs. INTC: Which AI-Era Semiconductor Stock Will Reward Patient Investors? - 24/7 Wall St.

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.88 | N/A | N/A | 124.92 | 124.92 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.88 | N/A | N/A | 455.19 | 455.19 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.84 | +23.39% | +12.59% | 215.20 | 215.20 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.17 | +1.78% | +7.26% | 2,290.00 | 2,290.00 | 0.00% | 同向 | 66.26 | 34.57 | 410.73B TWD / 17.50% | 2026-05-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.06 | -15.63% | -9.83% | 415.12 | 506.69 | -18.07% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.12 | +38.93% | +29.79% | 430.00 | 430.00 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.09 | -0.77% | +7.95% | 516.00 | 516.00 | 0.00% | 未明確 | 9.37 | 55.54 | 62.25B TWD / 19.22% | 2026-05-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.12 | +15.06% | +39.08% | 3,630.00 | 3,630.00 | 0.00% | 同向 | 66.17 | 55.02 | 46.74B TWD / -4.14% | 2026-05-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC、Intel」，共 2 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：growth, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。 方向判斷命中詞：growth, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。 方向判斷命中詞：growth, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [股海自由行／AI 題材績優股 長線還有戲 | 證券達人 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBxdV82UlZ1Ymw3YU5IMk1Zd1kwdFV2bjhmS2JiMFk3dU9UdFZRVFR2Y1VlbGdzV3ZEa2tOR2xZOUdOWVdMbmd2YXhadDFqcm1wUEQ3YUZyRjFZdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 09 May 2026 18:53:25 GMT
- [台股 ETF AI 熱潮催動漲勢 群益半導體收益單周勁揚逾16% - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9iOWM5TGdmUjlxOXZxTUQxR3A4MkZuTGUxcHVFWUhQWG50Qi1nMXN6NVdWWkRDd0lBa01YZnUwMnBqSUJUaE1mSmFQMHFyNzQySVQxN0t1ZF82d9IBX0FVX3lxTE5PY1RjYVJPU1kzTnoxUmNQOW1TcFVqTHBTMW9uZFhoVThoRkNmdlhKWFNzLUFNNEh3VDJHWEYySU50d1BfZURPSFZ3SzZ5WGNVTE5yR1V2amlIOVF4S1M0?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 09 May 2026 15:42:48 GMT
- [ARM vs. INTC: Which AI-Era Semiconductor Stock Will Reward Patient Investors? - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiugFBVV95cUxOUFp0eFZTZFhYcUlrSmoxSVp1V284VXVhdjhuOFhWdmN6YUVHdFBqVnNHOG4xS0tUcVAzN2ZzZ0Vjd2tZdDV2RFF3bUlxR2F2NjlnWHp5eWFyMG03S0ptSjFmZ2pua0JWMjhYLXJiRldxZTcwNzIxYms5Ql9fd1pFOVZCSkNLeHZweElIOEFvWm9DbjBrY0EtX2RPblQ4azJUN0EyNnNkLVdsZm5SNGloa1BSQ0NKOGFoZlE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 09 May 2026 13:00:24 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：INTC, AMD, MU stocks hit 52-week highs today: What's triggering the rally? - MSN；Micron Has The Better Scarcity, Sandisk Has The Hotter Trade (NASDAQ:SNDK) - Seeking Alpha；Micron Rockets 11%, SanDisk Rallies 11%, Western Digital Up 3% on AI Memory Supercycle Bull Case - 24/7 Wall St.

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.88 | N/A | N/A | 746.81 | 746.81 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.88 | +11.09% | +31.62% | 1,562.34 | 1,562.34 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.65 | N/A | N/A | 455.19 | 455.19 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.65 | N/A | N/A | 124.92 | 124.92 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | +0.65 | +1.78% | +7.26% | 2,290.00 | 2,290.00 | 0.00% | 同向 | 66.26 | 34.57 | 410.73B TWD / 17.50% | 2026-05-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +23.39% | +12.59% | 215.20 | 215.20 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron、NAND」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs, rockets。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK、SanDisk、NAND」，共 5 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：rally, rockets。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [INTC, AMD, MU stocks hit 52-week highs today: What's triggering the rally? - MSN](https://news.google.com/rss/articles/CBMi-wJBVV95cUxQR0laZmpxNWE2U2w3VzdWRHBjOGN5MHllVFJRdnNiZFQtcExfOTRYX29XNWNoVGJPLXN5RmNkZVpuUXZwTHc4eWlpdWNPQlQwZHBDblI2cUNuVWRqMUhTd1JHTTRGb3VGT2MyakphaWctNEtjZ2JzZ0IyczdRNnZpVEoyMWFQTUtiemdBaGVHcXJzdG80TGpLY1pwZm1mYkpTWkxRVndJLTk1Rk5zZGxvZHY1N3Q3cWQ3dTNXd3ZjT3djVE1JZWpxWmJtRmFFQ0MtaFphZGRDdGxZSVQtUWV0MFh1Sm5DNXk0YTZ6S1hGSXpqRFVESUNEVEtIaFlOeGNBTFRrNW5QSEpSSU55LVUtcmhRRE9ZN1YyUUlzQ3J3c1dHSlI1R1doSExNc2NmUmhwY2x0eDNfaWJXVDhkeVFoN01NVGlLRElXNm9EUjVUU3lzYlplRW9CWHpOd2xNWFVHVVZHVnRvdEZUOHZXTFJGNENmWF9xUnRMbnNB?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 08 May 2026 05:20:46 GMT
- [Micron Has The Better Scarcity, Sandisk Has The Hotter Trade (NASDAQ:SNDK) - Seeking Alpha](https://news.google.com/rss/articles/CBMiogFBVV95cUxPd0ZFd1h0S2xPWDdWWFBOcnR1cmFWU3JqTllFQ1h2aGVQajA3dG9MeTJ4WU1xZHhqVWtXNi1wZlVWOUhGRm1LUURfUGV3dXZWX0RHbEZzWXBpMmowMWpVd1RyeXQxR0VkSjlZaUpYcUx4NVBCUkh1bDN4dFdUdlJjem9sTlRYcGpiOFpQSnNKMGZoUjVQY1IwdnlZbnozM1ItRXc?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 09 May 2026 10:51:53 GMT
- [Micron Rockets 11%, SanDisk Rallies 11%, Western Digital Up 3% on AI Memory Supercycle Bull Case - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi0AFBVV95cUxNdVdEUVVPNy1QXzdMaF9veS1EWk54NC1FM2VPR2hicTJ1T1pabS1CMTJaN3hMcEJabnFZVVFleHNBNERIQXFtVHZfTnBNbDE1djdNbWlTSXJjb3VmTmU0b0RwdUVjYkwtZ2kzeFUyS0pTQUxYdTJndVRVQ1hLYzg0cmJDUU8wUXBGekxncW9ma3JieG16Nlp6R1luUFJGUm5CVUF2SEQ0VkVkejZGak5zcGd0RkdkdVZHZEVRSHBkU2NRU2szdmV6UlRORFJBeXNZ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 08 May 2026 15:49:24 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：台股 ETF AI 熱潮催動漲勢 群益半導體收益單周勁揚逾16% - 經濟日報；ARM vs. INTC: Which AI-Era Semiconductor Stock Will Reward Patient Investors? - 24/7 Wall St.；How High Is Donald Trump’s 10% INTC Stake After the Apple-Intel Chip-Making Deal? - Coinpaper

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.88 | N/A | N/A | 124.92 | 124.92 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 新聞直接提及 | +0.65 | +5.19% | +46.04% | 293.32 | 293.32 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.14 | +1.78% | +7.26% | 2,290.00 | 2,290.00 | 0.00% | 同向 | 66.26 | 34.57 | 410.73B TWD / 17.50% | 2026-05-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.14 | +9.87% | +18.11% | 91.30 | 91.30 | 0.00% | 同向 | 4.00 | 22.94 | 22.66B TWD / 10.80% | 2026-05-01 |
| NVDA 輝達 | 產業/供應鏈推估 | +0.11 | +23.39% | +12.59% | 215.20 | 215.20 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.11 | N/A | N/A | 455.19 | 455.19 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | +0.11 | N/A | N/A | 746.81 | 746.81 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.11 | +11.09% | +31.62% | 1,562.34 | 1,562.34 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AAPL：新聞直接提及「Apple」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 2 篇新聞出現相關標籤。

### 主要來源

- [台股 ETF AI 熱潮催動漲勢 群益半導體收益單周勁揚逾16% - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9iOWM5TGdmUjlxOXZxTUQxR3A4MkZuTGUxcHVFWUhQWG50Qi1nMXN6NVdWWkRDd0lBa01YZnUwMnBqSUJUaE1mSmFQMHFyNzQySVQxN0t1ZF82d9IBX0FVX3lxTE5PY1RjYVJPU1kzTnoxUmNQOW1TcFVqTHBTMW9uZFhoVThoRkNmdlhKWFNzLUFNNEh3VDJHWEYySU50d1BfZURPSFZ3SzZ5WGNVTE5yR1V2amlIOVF4S1M0?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 09 May 2026 15:42:48 GMT
- [ARM vs. INTC: Which AI-Era Semiconductor Stock Will Reward Patient Investors? - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiugFBVV95cUxOUFp0eFZTZFhYcUlrSmoxSVp1V284VXVhdjhuOFhWdmN6YUVHdFBqVnNHOG4xS0tUcVAzN2ZzZ0Vjd2tZdDV2RFF3bUlxR2F2NjlnWHp5eWFyMG03S0ptSjFmZ2pua0JWMjhYLXJiRldxZTcwNzIxYms5Ql9fd1pFOVZCSkNLeHZweElIOEFvWm9DbjBrY0EtX2RPblQ4azJUN0EyNnNkLVdsZm5SNGloa1BSQ0NKOGFoZlE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 09 May 2026 13:00:24 GMT
- [How High Is Donald Trump’s 10% INTC Stake After the Apple-Intel Chip-Making Deal? - Coinpaper](https://news.google.com/rss/articles/CBMiqwFBVV95cUxPZkszQjl5OEtwZ1BfUXgyb2VVZEo5UGYxU3VGa0tmTTl5S0l2Rzd4S3BBQlJ2Rk9sQXVIZGMzOVZWY3RwSDU2QWlGZWg4ajVxMk9mRGJGR25vUF9BZ1k1OFVOV3lkUmlaNk9PdnRjbWFqRnhFVXdEY1FGVWFyNGZIdG5rY2tYUTFzdEU2TE1KUExXWjJnaGI5emJ4NEx4MWpfaVBmTzRmU1NBcDQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 09 May 2026 12:12:39 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：散熱三雄遭血洗！Rubin設計變更傳言衝擊，市場不需要散熱了嗎? - CMoney投資網誌；健策(3653)股價7天崩30％怎麼了？散熱股末日到了？台股老手解析：奇鋐(3017)、雙鴻(3324)回檔該逃命還是抄底？ - 今周刊

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | -0.79 | -9.61% | -13.76% | 2,445.00 | 2,835.00 | -13.76% | 同向 | 49.17 | 49.98 | 15.63B TWD / 71.62% | 2026-05-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱、3017」，共 2 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：衝擊。

### 主要來源

- [散熱三雄遭血洗！Rubin設計變更傳言衝擊，市場不需要散熱了嗎? - CMoney投資網誌](https://news.google.com/rss/articles/CBMifkFVX3lxTE9RalFwM2o4STVKZU5iV2wwdlRfMmxwTjF1OXJCd1RGa2pEeDRQcFg1SjIzVUdwWEptUHlrZEs4RlU1MVpPR2wtWUZRVkdXaEZGMVNibl8tUW9CZEV0WnJqamtLODNVazZLSUU5WkJXelNHb2wxMllvT2YwRHZGUQ?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 08 May 2026 08:26:50 GMT
- [健策(3653)股價7天崩30％怎麼了？散熱股末日到了？台股老手解析：奇鋐(3017)、雙鴻(3324)回檔該逃命還是抄底？ - 今周刊](https://news.google.com/rss/articles/CBMigAFBVV95cUxNbFNPMWROSEF2eDFwRV9od2hVclhMaDZBbE1YQm40UWhHblF1d25Lc2RyYlVWRlRrTURWYnU2NHRfTWFXLURWT0dGMHpibE56WmFTRi13ZEg0RThqZEg4R3F3LXdLa3EtbFhTdVdhelNmMEx6Rk1sLUw5TlZBSWNGVA?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 08 May 2026 06:50:00 GMT

## 先進封裝與 CoPoS

摘要：先進封裝與 CoPoS 相關新聞集中在：日月光攜手楠梓電擴廠打造先進封裝產能新據點- 產業 - 工商時報；產品線都漲價，這檔半導體今年營收季季高，擁FCBGA+FOPLP，從280元拉回到222被低估了嗎？ - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3711 日月光投控 | 新聞直接提及 | 0.00 | -0.77% | +7.95% | 516.00 | 516.00 | 0.00% | 不適用 | 9.37 | 55.54 | 62.25B TWD / 19.22% | 2026-05-01 |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +1.78% | +7.26% | 2,290.00 | 2,290.00 | 0.00% | 不適用 | 66.26 | 34.57 | 410.73B TWD / 17.50% | 2026-05-01 |

關聯理由（前 3）：
- 3711：新聞直接提及「日月光、FOPLP」，共 2 篇新聞命中。 同時符合主題標籤：advanced packaging, CoPoS, FOPLP, panel-level packaging。
- 2330：產業/供應鏈推估：公司標籤符合「先進封裝與 CoPoS」關鍵字 advanced packaging, CoWoS, CoPoS, FOPLP；其中 1 篇新聞出現相關標籤。

### 主要來源

- [日月光攜手楠梓電擴廠打造先進封裝產能新據點- 產業 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9MMWxVY0Fyek5VdlFVSXF3QUMydm5nU1NpeDd3aHdxV1RFc240WlpMRFJiLXJ6Yi10bUNHcEF6ZWJZaGVYOWZURFJkcWUyMlp2Q3JFUjZwTjYydWNkY1Q4?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 08 May 2026 06:59:00 GMT
- [產品線都漲價，這檔半導體今年營收季季高，擁FCBGA+FOPLP，從280元拉回到222被低估了嗎？ - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9rN0JOZUZmSE9iUk80VVlUYktiMkZOOXNuQmlzb21HVVptUEdJYnk4NWdXSlE5M0FxUGt0Z3RMdHRWWlFoT2xkbW9UTjd0UHJKSGtDSHhFZndmd9IBX0FVX3lxTE1iWWJ3MWdBZHROQkEtekhkc0hydEluMS1fU0hYN0VTc2hJX2E5VG1oNFBWM0FIN1RucEpYbk5mT09hVGNNOEVOODJqWWMzOGlMQ3hvbDFfRFpDMW1oMW5n?oc=5) - Google News source discovery | 經濟日報 money Fri, 08 May 2026 15:35:33 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：美股指數期貨最新報價 16:38-台股 - MoneyDJ理財網；5/8三大法人選擇權契約交易表-台股 - MoneyDJ理財網；‧永豐期貨盤後分析 - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [美股指數期貨最新報價 16:38-台股 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilgFBVV95cUxNeDdaeHhNWjdYcnZJWXpfNV9MeDBDbHpablQ1elBqaDd1cFJfRGpuLWZ1aHBUSVk5QkFZWHVvbEtPRFJabl9TekJYb08zeENXMlFxam04aW5hZlh1S2QwNXBTcHVrSUd4WjhzaUFWbVBZUGhJMEVtYkoyRkZTbzVRSWVvNmFQLU1yLWxYbWp5R2xPdWhMRmc?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 08 May 2026 08:52:57 GMT
- [5/8三大法人選擇權契約交易表-台股 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilgFBVV95cUxNY19HU3p2czBRVXNHeHFHQ3lBbUlaZExxc1kwZ3NDNWR1ci01QlpvLXhRY1J5T0o5SHhucUMwQnBVanp5c0ZkMDNmbGhuYkl6anYwNFY0RHpYbHdCTFFuZUo2OGYxMUdfWGUzUHdyNXYxNGNWc19ZUlNNd1pTQVNBajFOZVA4XzJRb2JFWlcyMUJQV1lJb1E?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 08 May 2026 07:51:48 GMT
- [‧永豐期貨盤後分析 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikAFBVV95cUxPaVk0Ym5HamYtOHZxVlRzZ05DcGN3dVJlNmE1MUJtVWhQanc4Vm1Kd3RLNFkzSHlpY0ZKUlduUmZVQ3FxZmN5ejk0R3VWdUZEWjVMUkVpRGdhZFYyYlVIaUllb1c5SGxaZ2ZFQ2ZpeHY0cDh3aWxZYkx6MktyRFhFOUU4M0xrR2NXU2VCVmZha2c?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 08 May 2026 15:56:15 GMT

## 新興題材：AI伺服器

摘要：新興題材：AI伺服器 相關新聞集中在：同業股價表現-電子-AI伺服器-台股 - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [同業股價表現-電子-AI伺服器-台股 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMiaEFVX3lxTE5kXzVkeWE2S3ZyWnFmaGFUcy1TUHoybTE4eWd4S2JxTDJ2OWxmc24wUUd3SWhqSXFVUDVYT0QzSzVMVjVpd3Q0U0E3UHdUUWxKX3haYkxFTjhMUnpvRDhHaGpTWmlqUDBZ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 09 May 2026 10:30:36 GMT

## 新興題材：B729

摘要：新興題材：B729 相關新聞集中在：個股動態報導內容-A5484CA0-4338-4C8D-B729-3A6C27904444 - pscnetsecrwd.moneydj.com

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-A5484CA0-4338-4C8D-B729-3A6C27904444 - pscnetsecrwd.moneydj.com](https://news.google.com/rss/articles/CBMimgFBVV95cUxOTUlUeTRkU0xtU3lQLUt1M3JWTWxVdDNkU0F6S2liNTZuT1dNOG4xNVg5bVlwQWxXcWVTNUtydGhWSUxLWFp0WU0zVDcwdHhqV0liMGhWUVphaHhKUVc2LVloOGRuRGVOTE1tMWlRMWhPZHBGUS0xMW0wRm9pYUlRTU9FbHpubENhTzM1VDdUd2VPcm80WFZmdUpR?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 09 May 2026 20:18:18 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
