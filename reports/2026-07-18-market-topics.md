# 每日股市熱門話題分析 - 2026-07-18

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **綜合市場情緒**｜負向｜熱度 37｜市場確認 86.11｜同向 1/1
2. **半導體與晶片供應鏈**｜負向｜熱度 9｜市場確認 100.00｜同向 5/5
3. **記憶體與 HBM 供應鏈**｜正向｜熱度 6｜市場確認 100.00｜同向 1/1
4. **新興題材：TradingKey**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0
5. **散熱與液冷供應鏈**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.18（樣本 13）
- 5日相關係數：0.08（樣本 13）
- 同向比例：7/13

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 綜合市場情緒 | 86.11 | 1/1 | 0 | +5.37% | +5.18% |
| 半導體與晶片供應鏈 | 100.00 | 5/5 | 0 | +10.78% | +1.21% |
| 記憶體與 HBM 供應鏈 | 100.00 | 1/1 | 0 | +22.93% | +29.29% |
| 新興題材：TradingKey | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 0.00 | 0/6 | 5 | -6.36% | -2.47% |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：SpaceX | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-07-05 | -0.00 | 0.24 | +40.00% | 10 |
| 2026-07-06 | N/A | N/A | 0.00% | 2 |
| 2026-07-07 | N/A | N/A | 0.00% | 1 |
| 2026-07-08 | -0.05 | -0.05 | +71.43% | 14 |
| 2026-07-09 | -0.11 | -0.36 | +64.29% | 14 |
| 2026-07-10 | 0.55 | 0.05 | +77.78% | 9 |
| 2026-07-11 | 0.13 | -0.08 | +50.00% | 12 |
| 2026-07-12 | 0.27 | 0.13 | +16.67% | 12 |
| 2026-07-13 | 0.39 | -0.09 | +15.38% | 13 |
| 2026-07-14 | 0.10 | -0.07 | +21.43% | 14 |
| 2026-07-15 | 0.20 | -0.16 | +28.57% | 7 |
| 2026-07-16 | 0.20 | 0.02 | +33.33% | 12 |
| 2026-07-17 | 0.36 | 0.02 | +60.00% | 15 |
| 2026-07-18 | 0.18 | 0.08 | +53.85% | 13 |

## 歷史回測摘要

- 回測日期：2026-07-18
- 近5日 3日相關：-0.07
- 近5日 5日相關：-0.00
- 同向比例：+59.09%
- 權重狀態：已調整

- 方向準確度：+59.09%
- 信心排序準確度：-0.07
- 診斷：低相關

調整原因：近 5 日信心分數與股價關係偏低，提高價格確認，降低寬題材推估。；關鍵詞×公司後續樣本有效 5 筆，未達 30 筆，不調整樣本權重

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

摘要：綜合市場情緒 相關新聞集中在：台股重挫為史上最大單日跌點 金管會回應了 - 經濟日報；外資狂砍1,890億元、三大法人爆賣2,617億元！台股殺出史上最大跌點 | 市場焦點 | 證券 - 經濟日報；台股收盤下跌2,953點寫最大跌點紀錄 台積電收低180元跌幅逾7% - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | -0.43 | -5.37% | -5.18% | 2,290.00 | 2,470.00 | -7.29% | 同向 | 74.39 | 30.79 | 442.68B TWD / 67.87% | 2026-07-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。

### 主要來源

- [台股重挫為史上最大單日跌點 金管會回應了 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBTTmt5a1MxTnlWc2hrb1ZMSTY5Q0c1WVZla2lkc2hWSzZDempCZkY1YmdmU2J6SVpKY1ktM1hLY0tOOHRxSl9jVURWLW5la3BtS3RXRW9oV3Znd9IBX0FVX3lxTE54SFE0LW80NENpN05WZmpnWVM5N1NFMjI1NldFZGRBV2ozTWtsSzVzUmtCUkVmVXc4dXFpNEVldm1xMEtSbExYVzZCMkpGZjJUdGZwbktJVUl2cmNfTHFR?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 17 Jul 2026 11:43:33 GMT
- [外資狂砍1,890億元、三大法人爆賣2,617億元！台股殺出史上最大跌點 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9TOGNsNGZna0dmeGhmNlNUN3FSaDUzZnJPVEdibTl5UC1tRkdzNDE1QXhJZ2pHQ09pU3FuOE5yS01NMUxKTF9iQXpsajJBZUY1eWdqOXZjTDZwZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 16 Jul 2026 09:00:00 GMT
- [台股收盤下跌2,953點寫最大跌點紀錄 台積電收低180元跌幅逾7% - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE85X1F0SUFsLWxZeE51d0NNOTVta1dMblpYR2lpbGxaQmVNb3RWUWxBMVJXbEE0XzNHWGZUZnFKSVBiYlZMN3daQnl5ZThlUmo0VnE2SlFwSE00QdIBX0FVX3lxTE1NWmdXN09ycm9jU3Z1bDBaajVGUU5HWmd1bWFvVXlMOHdxY1RQVHdwdHRSS1RtX3llY290SXlpWkc0ZzdOQ1YtYTZfVmpKSElnaEJQZEpNT3p1S0RfNnZF?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 16 Jul 2026 15:00:00 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：AMD Falls 5%, Intel Drops 4%, NVIDIA Slides 3% Before Recovering as Rotation Hits Semiconductor Stocks - 24/7 Wall St.；Intel (INTC) Stock May Trade At A Discount Following AI Chip Expansion - simplywall.st；The Chip-Stock Slide Isn’t Over. The AI Trade Is Still Under Pressure. But ‘No One Is Short’ - Investopedia

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.59 | N/A | N/A | 95.04 | 114.68 | -17.13% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | -0.51 | -3.95% | +16.29% | 202.81 | 211.14 | -3.95% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.51 | N/A | N/A | 495.76 | 516.10 | -3.94% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.06 | -5.37% | -5.18% | 2,290.00 | 2,470.00 | -7.29% | 同向 | 74.39 | 30.79 | 442.68B TWD / 67.87% | 2026-07-01 |
| 2303 聯電 | 產業/供應鏈推估 | -0.06 | -4.64% | -7.69% | 144.00 | 164.50 | -12.46% | 同向 | 4.00 | 36.18 | 23.12B TWD / 22.85% | 2026-07-01 |
| MU 美光 | 產業/供應鏈推估 | -0.04 | N/A | N/A | 848.95 | 971.00 | -12.57% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | -0.04 | -22.93% | -29.29% | 1,354.82 | 2,335.00 | -41.98% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -17.00% | +19.81% | 370.83 | 446.77 | -17.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel、INTC」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：falls, lower, pressure, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：falls, lower, pressure, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：falls, lower, pressure, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AMD Falls 5%, Intel Drops 4%, NVIDIA Slides 3% Before Recovering as Rotation Hits Semiconductor Stocks - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi2AFBVV95cUxNaEpYSjV2VTgtXzZFdWNKQTVydW5saUZpOTlsWUQ0VkJoX2pKVno1UTg5N0hibGxwYWlKZnQyS3N1QmZpTUlhS1dpQmYzOVBySmg5Um1OeGFPNm9uUDJjNm1jdXowOUhOV2I2bU1DdUpqQnd3bWtlcnJPT3g2Z2JIX0RuS0lNdWlPYnRlVTNDOWdkOEF2T0d5RUpvcTFGclR2cUhYYkQzQUl6dldmcWJQUmVRdGNlSG1qVHJweWJtMTJuc3VfUURhb08tNVlwSkowVnd6YmdaekI?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 17 Jul 2026 14:30:21 GMT
- [Intel (INTC) Stock May Trade At A Discount Following AI Chip Expansion - simplywall.st](https://news.google.com/rss/articles/CBMiygFBVV95cUxPMmFVdHlRNU9abUwxbXloZmU0NDNVSjNVdnA1OURsaVdqcFN4anBxV0NoSzlZYUpKUkYweEFXZWhsSEpyNmxZYXlzenRhcUhKZGZETnRLc2YxcldUNnJfMjBoR3BwX0Z6azRQSEF4TWFmWUY5aHZ1VXNFSTkyZUp6emFwN3pDNHIzQU0wX3dVUjR5MXhuZGFTX2VkSlpRM20tSXA2WWRhVk92ZHJlWFpxZWUzOW40T0FjS19yN013VVhDQWRZMWJrTVFB0gHPAUFVX3lxTE15T3JXX25NRVBRQ0dMSmFMX2RST3c3UVRDYVh4M0U4c3FTZnRQRVA1VEU1R3hmTDd5UmhmX0ttWUx1bTZrMzdPcVpVeFpkYlh4X3hpRkNZSURIMkV3YUQwN0E1d1ZlQkUxaWNoU0ZYMXBKbVVpRnVFSWJPcWdiQzBlVzRFWmFFaGxzWjNfamt4WDVZdFI2aV85Z3U0U3ljZ2hnOVBuQnE2WDk4REtCVE1wWGtZbkFMaHdxR1NhV3JRUzJELTl2NlNxMXJpRTA3cw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 17 Jul 2026 01:04:32 GMT
- [The Chip-Stock Slide Isn’t Over. The AI Trade Is Still Under Pressure. But ‘No One Is Short’ - Investopedia](https://news.google.com/rss/articles/CBMirgFBVV95cUxOYnhlZUVNVnQwdnoxQWRwbkNwam5sWG4yTHdqWnhiOHRySlpzNlNFODlKNkkzOWJVeFlGcS05cVFuVkNJVFlNQlVHZzNHUjNibEtNeDVGTTRVb0Z0c2JKenVRUGc4MjlpNUxQSDNJMEpmSTdLeDdmLXRLNlBPeGZhek9DcTZoZkw1dVdsS2RsWFNEMXFWeEpMajRVQjFmOUZCSU5pNENjX2FjZlJIRUE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 16 Jul 2026 15:43:33 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits；MU, SNDK, INTC, AMD, Other Chip Stocks Extend Slide – Retail Traders Still Buying The Memory Theme - TradingView；4 Top-Ranked Memory Stocks to Buy as AI Infrastructure Expands Globally - The Globe and Mail

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.50 | N/A | N/A | 848.95 | 971.00 | -12.57% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.50 | -22.93% | -29.29% | 1,354.82 | 2,335.00 | -41.98% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.43 | N/A | N/A | 495.76 | 516.10 | -3.94% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.43 | N/A | N/A | 95.04 | 114.68 | -17.13% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -3.95% | +16.29% | 202.81 | 211.14 | -3.95% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、memory、Micron」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：fall, weak, rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK、SanDisk」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：fall, weak。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits](https://news.google.com/rss/articles/CBMi0AFBVV95cUxOWm5KdEIwSXpyY191UEhDa1V6NVpWa01UbmpJeWRIV0ttT080TmpDNEhISW5TWkQwUzBVYzBqSHJPWXRVNVJCampoWWRlYmhKVkhIeHBJLS0wLW5Ua09GQnRORXpFcW5qTEJkcnJGcW55aU5rOFVOLUFMbjRPZEpWT3A2ZllucnM0SU9JNEdrNUwyc3V2WHAtNFk3VHl4R1F6SkZRMFpleEE2Zl9MdW4tSEpMMnFGZ2hQZURWQ3B1WDlPR1BhRjJELVN5ODJWYVR3?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 17 Jul 2026 10:50:47 GMT
- [MU, SNDK, INTC, AMD, Other Chip Stocks Extend Slide – Retail Traders Still Buying The Memory Theme - TradingView](https://news.google.com/rss/articles/CBMi6AFBVV95cUxNYkd0T1BNRmxjc0VoS05wSmJFSTI4cmVTMHprR2xJUDRVd1gwMFpjTmpxWVRXdTBzbExvX3NlZkVIZUItcFNpYmtsbWRDLXlkZEdVeWZJTHp4Q0FZcUx5c0pjTzBDcnh6Y2tqejdCQ2lHcV8xZHF1SmFsRlZWVFdwb3F1SjF1TU1yTEtOZVQwSHRJNUZ6VTBTeE1HTzl5emh3RzA1MWhPSlVWZXRYRFNHNUlQYXRHeE5zLVZ6QVBFeEVBejI3NmRvaWRueEl4cVpRLXZyZ1BNc2FKOHd4WG16SWNibm5hMEZv?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 17 Jul 2026 08:56:27 GMT
- [4 Top-Ranked Memory Stocks to Buy as AI Infrastructure Expands Globally - The Globe and Mail](https://news.google.com/rss/articles/CBMi6wFBVV95cUxORVRvckgtVkt3U0ZKWmpNQW1kVldiSXhhNUJTSUZnaEx1Z01GUmhnaDJrcXcwYXlwMmtKSFBGaFM3amkxUVhaMjlEX0EyNWNLVVRkQ1h3bkkwd3RoQ2xkV0dJc1o3RVltZEZldmVLNVlLM3RSTUVydkliNGxid0luU2VGVnoxY1FpNkhkb2tCLWFaSkhwandsR0J2NVY1SVNpbmo0Sk05OTJvb0lNVk53VXJBamxSY0dETGZ0Qll1a0U3TDhyTFFoU1dRNUdmbm5wU3JMTkZ3V0lXcWVJdGtScTBNYmREMEo0aTJJ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 17 Jul 2026 16:23:09 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Intel Stock Price Prediction: Can INTC Hold $94 Before Q2 Earnings? - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 95.04 | 114.68 | -17.13% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Stock Price Prediction: Can INTC Hold $94 Before Q2 Earnings? - TradingKey](https://news.google.com/rss/articles/CBMi2AFBVV95cUxQeU5CSjJkdHc5OV8zbHA1Z25mVzZTNjE3R25SWHp4ajU5anZ5OTdVVEVOaGx3NXBybHVNREtGZUxabmFKbUExc1MxdkhLUmlLOEgtck13QkFfdlpMRzRUeHFsTnpMc1A3RWU3OFVJRk5nSnktRmlLVFVFcWRLSEQ1bF9kdXh6MGxRdHFoLWptQi1XdXVoeXFKbF9jbS14U3cxVzY0bmdnWFNoRTExWVdlTS1POHVtTzFyOEFOZjZFNnJXYjdQSV9zd1kxYnNXeWpDMEFkYkYzNng?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 17 Jul 2026 02:05:28 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：【即時新聞】奇鋐(3017)單月EPS飆8元！小心這「3檔概念股」遭大戶倒貨！ - CMoney投資網誌

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | +3.77% | -6.38% | 2,200.00 | 2,835.00 | -22.40% | 不適用 | 61.06 | 36.15 | 17.62B TWD / 66.11% | 2026-07-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「3017」，共 1 篇新聞命中。 同時符合主題標籤：thermal。

### 主要來源

- [【即時新聞】奇鋐(3017)單月EPS飆8元！小心這「3檔概念股」遭大戶倒貨！ - CMoney投資網誌](https://news.google.com/rss/articles/CBMikAFBVV95cUxPZFEtcGlKamVTMUIwTzl6WV9pZkVCNElwc184emxrSFRSVGJZdHZpc09oaUpuN0Q5c25LMWtiQ1Mtb1paLXNXREZhMHNqSm9WQWdCaWFSMW9PT2V6dG5VSzQ5QURLdC1wM3VRRUswNWdtbG10ZE5rZ05MbDQ0cXk5ZTVxX2RJd1E4UVJpdEtOWTE?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 17 Jul 2026 03:37:25 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel (INTC) Stock May Trade At A Discount Following AI Chip Expansion - simplywall.st；The Chip-Stock Slide Isn’t Over. The AI Trade Is Still Under Pressure. But ‘No One Is Short’ - Investopedia；圖靈假設一開始就錯了？電腦科學家直言：AI 永遠無法掌握人類的「隱性知識」 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.56 | N/A | N/A | 95.04 | 114.68 | -17.13% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.03 | -3.95% | +16.29% | 202.81 | 211.14 | -3.95% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.06 | N/A | N/A | 495.76 | 516.10 | -3.94% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.03 | -5.37% | -5.18% | 2,290.00 | 2,470.00 | -7.29% | 背離 | 74.39 | 30.79 | 442.68B TWD / 67.87% | 2026-07-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.03 | +0.27% | -22.28% | 393.82 | 506.69 | -22.28% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -17.00% | +19.81% | 370.83 | 446.77 | -17.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.02 | -4.21% | -9.31% | 614.00 | 682.00 | -9.97% | 背離 | 10.86 | 57.01 | 65.78B TWD / 32.86% | 2026-07-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.02 | -7.92% | -14.14% | 3,370.00 | 4,310.00 | -21.81% | 背離 | 62.91 | 53.71 | 58.01B TWD / 2.80% | 2026-07-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：pressure, 擴大。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：pressure, 擴大。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：pressure, 擴大。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel (INTC) Stock May Trade At A Discount Following AI Chip Expansion - simplywall.st](https://news.google.com/rss/articles/CBMiygFBVV95cUxPMmFVdHlRNU9abUwxbXloZmU0NDNVSjNVdnA1OURsaVdqcFN4anBxV0NoSzlZYUpKUkYweEFXZWhsSEpyNmxZYXlzenRhcUhKZGZETnRLc2YxcldUNnJfMjBoR3BwX0Z6azRQSEF4TWFmWUY5aHZ1VXNFSTkyZUp6emFwN3pDNHIzQU0wX3dVUjR5MXhuZGFTX2VkSlpRM20tSXA2WWRhVk92ZHJlWFpxZWUzOW40T0FjS19yN013VVhDQWRZMWJrTVFB0gHPAUFVX3lxTE15T3JXX25NRVBRQ0dMSmFMX2RST3c3UVRDYVh4M0U4c3FTZnRQRVA1VEU1R3hmTDd5UmhmX0ttWUx1bTZrMzdPcVpVeFpkYlh4X3hpRkNZSURIMkV3YUQwN0E1d1ZlQkUxaWNoU0ZYMXBKbVVpRnVFSWJPcWdiQzBlVzRFWmFFaGxzWjNfamt4WDVZdFI2aV85Z3U0U3ljZ2hnOVBuQnE2WDk4REtCVE1wWGtZbkFMaHdxR1NhV3JRUzJELTl2NlNxMXJpRTA3cw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 17 Jul 2026 01:04:32 GMT
- [The Chip-Stock Slide Isn’t Over. The AI Trade Is Still Under Pressure. But ‘No One Is Short’ - Investopedia](https://news.google.com/rss/articles/CBMirgFBVV95cUxOYnhlZUVNVnQwdnoxQWRwbkNwam5sWG4yTHdqWnhiOHRySlpzNlNFODlKNkkzOWJVeFlGcS05cVFuVkNJVFlNQlVHZzNHUjNibEtNeDVGTTRVb0Z0c2JKenVRUGc4MjlpNUxQSDNJMEpmSTdLeDdmLXRLNlBPeGZhek9DcTZoZkw1dVdsS2RsWFNEMXFWeEpMajRVQjFmOUZCSU5pNENjX2FjZlJIRUE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 16 Jul 2026 15:43:33 GMT
- [圖靈假設一開始就錯了？電腦科學家直言：AI 永遠無法掌握人類的「隱性知識」 - TechNews 科技新報](https://news.google.com/rss/articles/CBMijwFBVV95cUxPR2pkTVJ0TThTcEpMMnFiS1NaUkJqVlhHWnBDVnMwNFhTU1YzbC1QMjV1RlBiLWhTRzlULXhxcjB5R1lmQjJHYkhBTGtVeGp3Y1lhaEpQeEV5TW5SVjVvTzNSYndNMEFrTEp0QUdBY1FScmVYVUtYSHdsT3ZyczUtSTZGcFk3V1gxTm5pQ3BQdw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 16 Jul 2026 23:55:30 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》崩跌2953點創史上最大跌點/失守季線 周K連2黑 - MoneyDJ；台股崩跌2953點創史上最慘專家揭反彈時間點- 新聞 - MoneyDJ；台股崩跌 台幣爆天量收貶3.9分 創逾一年新低-新聞內容-基金 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》崩跌2953點創史上最大跌點/失守季線 周K連2黑 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNWGhBUlNkUGlxWDdwMEtlUTRRSFUyNk53TlJ3QU1iak5Vd2hPcXNCY01DNU1JM0pjVTVjTE1ZNzZGemF2NjZLTl9WLU10N0NYMFZRVkphUU1OQ1M5UzBaTGdtNFF5T2FpWUZIYU5NMXE0VHlFM2FYaE1UcmhESXZIRmc4d2VPMUhpYVZOR3dFMkxSQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 17 Jul 2026 07:51:00 GMT
- [台股崩跌2953點創史上最慘專家揭反彈時間點- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNbEcyeHA1dDlRU1RBdF91UFk0b2xBUE1xLUFpWG9pSEtBMW5Za3FPbDFrSDZ2NDk3VGZMMHM0dXZlYVk3M2FLUmg0WkR0VU1tckFHbkV0QjZIVWJRa2FCWGRhaVMwdnlNaHA0SFJhc0VCY0oxZWI2dHZvRTk4NVI2YzJWdnBqZTAzY1hnWlEtbDU3dw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 17 Jul 2026 14:02:00 GMT
- [台股崩跌 台幣爆天量收貶3.9分 創逾一年新低-新聞內容-基金 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxQWXo4bUJMMGRmNWFPa3ZtcEtQMHh1aEdXLW5sVG1NRU1QVjBNVFp0TXNFc2lsNGNNbWdDVnNGWWZlUW9LZ1IzTHlqWjV0MmZYNGNKZmREUVNIT0JITmZydlF0SGpra25aZEw5dzBHUTBwNldpVFVObGtKdkhkbm4tVGdXTUU4LXFOX2VhY2hmSkQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 17 Jul 2026 10:04:00 GMT

## 新興題材：SpaceX

摘要：新興題材：SpaceX 相關新聞集中在：Stocks making the biggest moves premarket: Netflix, SpaceX, Alphabet and more - CNBC；Stocks making the biggest moves midday: Travelers, SpaceX, Alphabet, Netflix, Synopsys & more - CNBC

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [Stocks making the biggest moves premarket: Netflix, SpaceX, Alphabet and more - CNBC](https://news.google.com/rss/articles/CBMipgFBVV95cUxPZEI4Nm84SzVFd1FPNmFJbFgwYVdIY0plUTJfSDUtMWJCWE5KVWR5LTJSTmZzUk02QlNHT3d4ZFpQRUlPbTU3Nk5URE4zdFZqLXZLUURTVFI1RzQ3aDZsOXlXTnZtaTFoMUZvdG01SmUzTjVPQUdFVU1UVGoxRTYwM0lTNHJTaHFSOHYwSzdmdFN4UUhqdE9QUXZPS0RKaEM5aExEOWNn?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 17 Jul 2026 11:41:10 GMT
- [Stocks making the biggest moves midday: Travelers, SpaceX, Alphabet, Netflix, Synopsys & more - CNBC](https://news.google.com/rss/articles/CBMiogFBVV95cUxNWnp2RVZDcTE4dDV6U1FQNEhoQ3pmZC10Y2E3NkxrUVlNdUp3bmxPaVhnbUpjb1k5WWRTVEFyak1LY0Jpb3RfcUEzQkFjUmN4M0I2UEltYkw4Ykg2VmktLTZTXzlfQ1h1WVhNVUFBNTRNazFVWlQwZXpJb1lrOXAwSmNfcU1PVEpHb0tjUUlSdnRjendDTHVzaXlvVkZ4dk9zMmc?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 17 Jul 2026 16:21:55 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
