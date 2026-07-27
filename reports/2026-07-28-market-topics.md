# 每日股市熱門話題分析 - 2026-07-28

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜負向｜熱度 8｜市場確認 100.00｜同向 1/1
2. **利率與成長股估值**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
3. **新興題材：TradingKey**｜負向｜熱度 3｜市場確認 46.14｜同向 2/3
4. **新興題材：OpenAI**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
5. **AI 伺服器與資料中心**｜正向｜熱度 14｜市場確認 9.69｜同向 1/6

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.32（樣本 11）
- 5日相關係數：0.13（樣本 11）
- 同向比例：4/11

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 100.00 | 1/1 | 0 | +20.07% | +8.10% |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：TradingKey | 46.14 | 2/3 | 1 | -0.18% | -16.57% |
| 新興題材：OpenAI | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 9.69 | 1/6 | 4 | -0.66% | +10.26% |
| 半導體與晶片供應鏈 | 0.00 | 0/1 | 1 | -2.08% | +1.29% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-07-15 | 0.20 | -0.16 | +28.57% | 7 |
| 2026-07-16 | 0.20 | 0.02 | +33.33% | 12 |
| 2026-07-17 | 0.36 | 0.02 | +60.00% | 15 |
| 2026-07-18 | 0.18 | 0.08 | +53.85% | 13 |
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

## 歷史回測摘要

- 回測日期：2026-07-28
- 近5日 3日相關：0.13
- 近5日 5日相關：-0.18
- 同向比例：+26.67%
- 權重狀態：未調整

- 方向準確度：+26.67%
- 信心排序準確度：0.13
- 診斷：弱正相關

調整原因：近 5 日方向與信心排序皆偏弱，降低方向詞與供應鏈推估權重，並加重背離扣分。；關鍵詞×公司後續樣本有效 5 筆，未達 30 筆，不調整樣本權重

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

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：SanDisk Rises 8%, Western Digital Jumps 9%, Micron Adds 7% as Memory Rebound Accelerates - AOL.com；SanDisk Stock Price Forecast: Chinese Manufacturers May Rapidly Break DRAM and NAND Industry Barriers; Shares to Fall Below $1,100? - TradingKey；EXCLUSIVE: China Is Coming For SanDisk—But Not Yet For Micron’s Memory Crown (CORRECTED) - Benzinga

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | -0.48 | N/A | N/A | 900.20 | 971.00 | -7.29% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.48 | -20.07% | -8.10% | 1,278.23 | 2,335.00 | -45.26% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -6.93% | +12.68% | 196.51 | 211.14 | -6.93% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、DRAM」，共 4 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [SanDisk Rises 8%, Western Digital Jumps 9%, Micron Adds 7% as Memory Rebound Accelerates - AOL.com](https://news.google.com/rss/articles/CBMigAFBVV95cUxOUGJ5YUhSYS1tTXMtSXNpbTgzSXRpdFZOOVZmenJuakVrVlA1T0tuZ3NjdVVCd3dQbkhkMEV0N0szVzd6ZVM2TS0yWDlMYlF3bXhxRGtaUVdSX1I4ZFBWTUlZTDlrUy1EQ0hud09yVnJxS2JBd2FrcDV0X1IyVWotcQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 27 Jul 2026 02:55:25 GMT
- [SanDisk Stock Price Forecast: Chinese Manufacturers May Rapidly Break DRAM and NAND Industry Barriers; Shares to Fall Below $1,100? - TradingKey](https://news.google.com/rss/articles/CBMi7AFBVV95cUxPV1ZQNWM0X2k5aTNIZjVzLW9BY3VaVXg2UUtSLTlReFVxZnZiZ1FmMndxTUZRcmk4NUI5YTZYRWc5OTM3TW90aldTaHlnYU1wYU9FYjN1UzNoVkF0MWR0cmNHbVh1V2YtYjNINGF6SjF6S1NyRGtNYU03bWl3azhzalZCWFZDU2F4cS1ybXRxSUpHdGRyR1hLdVRPdS11T1B1ZnNJb2RQVUJsLWQ4akJteGpSVlEzSUtLcFdDQTFSNENFOG1QdFg0cnlHSEJJSXBmRVVLbWRWUTJ1SmNaYTRFSG9jRVJfOVY5V2J0RQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 27 Jul 2026 15:26:35 GMT
- [EXCLUSIVE: China Is Coming For SanDisk—But Not Yet For Micron’s Memory Crown (CORRECTED) - Benzinga](https://news.google.com/rss/articles/CBMiuAFBVV95cUxOWFBuSHlwMlBodXJ1RThQamtGVC14VU5ab1FoQlAyRDVNYlg0ZDlnM0Y4RVZNUUNnTm9SSXNYWm9RMmJoal9PeFBUZE5zaS1KR1lQc3daVGlWVW5ETGNZUUZtRG1TVmd1bkJtdzJ0X1ZUOWJOYW9NNUxVV1UyRXFRSFZzWmczQjdNWWtyVWs2cWN3VU5rRWp6d2FpM2xDbF9EdmtQSnpjeHYtSEdDN3BfeGgxM1d0Zi1h?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 27 Jul 2026 20:10:00 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：美股估值過熱？「巴菲特指標」飆破236% 外媒：投資人正在玩火 - Yahoo股市；越南控股公司公布2026年6月淨資產值下跌，估值差距持續 作者 Investing.com - Investing.com 香港 - 股市報價& 財經新聞

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | -0.93% | -23.21% | 389.10 | 506.69 | -23.21% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [美股估值過熱？「巴菲特指標」飆破236% 外媒：投資人正在玩火 - Yahoo股市](https://news.google.com/rss/articles/CBMi7AJBVV95cUxNMFdxU1VNQm9XQ04xenIxWVg1NTFtcDdtY1RpRGpnTUN6ZGpzU0l6SEp4VDR1SGJXVnhpQWNfZnAxLXNRUmZDelY4bC1zNlctazNYazl3M0gxTFJLVXJLRXdnNnphZEIyZ2QzcUFfLWYwM0l4UmZ1cTZOMlFhMmRTQjgyd0FiTDNHeHBXOHNyTXVMazF5RlZMTXFFUGFHWGJ3ejg0ajhwSHVRZW1KT2RWQjlWU08waUFiVktCaDBQS1UtTnNvdms5QjhpNDQyN2dtdHhma1JuTm1Zc2FOZGtiVS1QZ1NnTE5LdnVtdlc2Q1k3NXpzY1UxMXJHUTVJNTlQdHo1YTJsaFFaVnh6U0dtYm1xUzRNRGZSclhfS3AwaEFFQktCbTBnT3VxRzRHMkV4eFc4bXV2QWstWW40a0w3b0ZaMjdJVDhJcnpXLXdjME41R2pYc1QzVnRuSENCaDNkcXBHVVVKNnhyQ0Zy?oc=5) - Google News source discovery | Yahoo 奇摩股市 Mon, 27 Jul 2026 09:34:00 GMT
- [越南控股公司公布2026年6月淨資產值下跌，估值差距持續 作者 Investing.com - Investing.com 香港 - 股市報價& 財經新聞](https://news.google.com/rss/articles/CBMicEFVX3lxTFB0VHpCOTJNZFpTUkRtMHVsLXBOWnFHY3FKVzY5aDRMWFZ4ZkRSNWlKY3l6X1U3cjc1UjZHdDMwaXVBcWRDVWxybDVMNEF4TGhIVW1od3ZrUnBsVVMtbEs1ZWgtVko1NHk0THo1azBoZXI?oc=5) - Google News source discovery | Investing.com Calendar Mon, 27 Jul 2026 06:04:03 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Intel (INTC) Beat Q2 by 110% Then Fell 19% - Here Is Why and What Comes Next - TradingKey；SanDisk Stock Price Forecast: Chinese Manufacturers May Rapidly Break DRAM and NAND Industry Barriers; Shares to Fall Below $1,100? - TradingKey；US Market Close: Major Indexes Mixed as Apple Overtakes Nvidia; Nasdaq Composite Index Falls for Fourth Day as Chip Stocks Lead Declines While Software Shares Rise - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | -0.42 | -6.93% | +12.68% | 196.51 | 211.14 | -6.93% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | -0.42 | N/A | N/A | 91.67 | 114.68 | -20.06% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 新聞直接提及 | -0.42 | N/A | N/A | 900.20 | 971.00 | -7.29% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.42 | -20.07% | -8.10% | 1,278.23 | 2,335.00 | -45.26% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 新聞直接提及 | -0.21 | +27.53% | +45.13% | 336.91 | 336.91 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MU：新聞直接提及「DRAM」，共 1 篇新聞命中。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel (INTC) Beat Q2 by 110% Then Fell 19% - Here Is Why and What Comes Next - TradingKey](https://news.google.com/rss/articles/CBMirAFBVV95cUxOTUNMRzM5dmQtWnNkLVFRbmZsVk03c0RtZmpjNlFTY0kwd0JDc29DQlZsLVpJN2pUaVpuTTc2X09ERmxoQkJQOXlPSUMzV2tyTGpIWFJ4S3JVRjMwUmFTRjNaR1lzdS04ZXZPOGRoYjNuU0RvbmhKQmQtMHVNMVpKUzFDd3pnNTNJdTRaZ1h1UnQtcDkzVVRkQVF3Vy1ZR0FsX2Nub1NsMGpTX0tS?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 27 Jul 2026 15:06:35 GMT
- [SanDisk Stock Price Forecast: Chinese Manufacturers May Rapidly Break DRAM and NAND Industry Barriers; Shares to Fall Below $1,100? - TradingKey](https://news.google.com/rss/articles/CBMi7AFBVV95cUxPV1ZQNWM0X2k5aTNIZjVzLW9BY3VaVXg2UUtSLTlReFVxZnZiZ1FmMndxTUZRcmk4NUI5YTZYRWc5OTM3TW90aldTaHlnYU1wYU9FYjN1UzNoVkF0MWR0cmNHbVh1V2YtYjNINGF6SjF6S1NyRGtNYU03bWl3azhzalZCWFZDU2F4cS1ybXRxSUpHdGRyR1hLdVRPdS11T1B1ZnNJb2RQVUJsLWQ4akJteGpSVlEzSUtLcFdDQTFSNENFOG1QdFg0cnlHSEJJSXBmRVVLbWRWUTJ1SmNaYTRFSG9jRVJfOVY5V2J0RQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 27 Jul 2026 15:26:35 GMT
- [US Market Close: Major Indexes Mixed as Apple Overtakes Nvidia; Nasdaq Composite Index Falls for Fourth Day as Chip Stocks Lead Declines While Software Shares Rise - TradingKey](https://news.google.com/rss/articles/CBMi_AFBVV95cUxOSERoTU1XbldtTTdLMkJQMjNCTTluNldxZFNwR1hsRHJqbWlCSnBPb3RLRUM0MFA5Uy0zV2RKcGVvdXBNenhrYTU0V250ZnZEMDFHa05FV2NYdndlX0VhbEdES24wbGVfZ1hueWRBUHBrWF84MEprNzNrT1lYd2c3OEc1ZEFQWXRla0dvT0VPdUNadnpMcV9MMFRXWXBveG9SVlNFMVJkZVNlTmVLZDdXMHJ6WDBBT29IVHJ0NnNnYWRHT25qRjBPckpOczZPTGhhUUpZRlAtaUZmUFNRUVpVbUNsU3pXQlFocWVwNEdzd3M4ZlJ6Y2poMFV0VHI?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 27 Jul 2026 20:16:42 GMT

## 新興題材：OpenAI

摘要：新興題材：OpenAI 相關新聞集中在：AI Stocks Crash After NVIDIA Plans to Finance $250 Billion OpenAI Buildout Are Reported - 24/7 Wall St.；Nvidia and OpenAI in talks for up to $250 billion dollar backstop to fund AI infrastructure plans - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | 0.00 | -6.93% | +12.68% | 196.51 | 211.14 | -6.93% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 新聞直接提及 | 0.00 | -0.93% | -23.21% | 389.10 | 506.69 | -23.21% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MSFT：新聞直接提及「OpenAI」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AI Stocks Crash After NVIDIA Plans to Finance $250 Billion OpenAI Buildout Are Reported - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiygFBVV95cUxNNmFRbzY5MldBYzJxMGN5TEp1aXYwVlJGaHduMHE5bmFFYlVrZVJ6RVl6T1VadkNrQlhOWHAybGJ5NW9PVlVsc0l2TmpVQlFKRy1vbkZoTWtFQzE0bzBCZXhqTmc3NzNPUGFQOUluRHFaTzdjYXd6cUdQcFhhWWpEUWgyVU1HVDRZUkMyYmpDN2J3VzRyOHdDdzV1VGxJZDFRaldzUzNLS0VUR2dLWTIzNDNUaFEyOGxrbmpkVzc3WDFta3Nmc1VyREVR?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 27 Jul 2026 16:00:49 GMT
- [Nvidia and OpenAI in talks for up to $250 billion dollar backstop to fund AI infrastructure plans - CNBC](https://news.google.com/rss/articles/CBMipwFBVV95cUxOTXFNTG1IS2JkSThkaWkxX2N2UVIyM2RqTEhkQjAybnVVUmRXSER4SkxSRi1PZWtueEpSQldBd0xpbzdqZzUwSkpuUU9YTVJFUnBkUTJUbG9KeXlEajNkd2NxV1pzSTVRbV9PVEVxdTIzeFJkdFEwNDlDQjJNbzBpckp5Sk5nMEdZdHplbXNFalFDbE1pMGxSbG50N3F2aGtndWx1TEN5WdIBrAFBVV95cUxNeGlpWjRLQndUSmJ4VjdQTGFtSVFCOVZKMzUxTVBWSGhtdXQzeGR6Z2RTSWtpcVJDQ0V6QkVDUElzT2sxYkQzYzkwUmpaZDBLckhvYWdJZW1PWHgtLUhCN1hVWWE2MnNHVzNFNlBvZWFUQ2tuMDl2dzVSekVRTmtTREVnY0hvbW5XbWVaVDM2Rm11WU1LRnZrN2Q2bEdvQ204TVF2Q3ZlQjk0VXBo?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 27 Jul 2026 17:32:53 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel Stock And 2 AI Infrastructure Picks Retail Investors Are Researching - simplywall.st；4 High-Growth AI Infrastructure Stocks to Buy for Long-Term Gains - The Globe and Mail；AI 裝置能否挑戰蘋果硬體地位？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.54 | N/A | N/A | 91.67 | 114.68 | -20.06% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 新聞直接提及 | +0.42 | +27.53% | +45.13% | 336.91 | 336.91 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.03 | -6.93% | +12.68% | 196.51 | 211.14 | -6.93% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.06 | N/A | N/A | 494.95 | 521.95 | -5.17% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.03 | -2.08% | +1.29% | 2,350.00 | 2,410.00 | -2.49% | 背離 | 74.39 | 31.59 | 442.68B TWD / 67.87% | 2026-07-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.03 | -0.93% | -23.21% | 389.10 | 506.69 | -23.21% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -14.22% | +23.82% | 383.22 | 446.77 | -14.22% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.02 | -7.32% | +1.84% | 608.00 | 680.00 | -10.59% | 背離 | 10.86 | 56.45 | 65.78B TWD / 32.86% | 2026-07-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AAPL：新聞直接提及「蘋果」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Stock And 2 AI Infrastructure Picks Retail Investors Are Researching - simplywall.st](https://news.google.com/rss/articles/CBMiygFBVV95cUxOV3YwLUhjZk9CVEtncHY2X3JlenhJZk9GX1JObWo1SDJzNFQ3b3Nob1RDNE1qWEVFOFc1UVhFcmZUU2VmbjU5SW5DOTJ2eFZaZnZER2Y2dVM0SER4b2N6Qll0UWtXNWlkQ3FkZDU3aWJFSlltbF80SFlSb3pORm13SmlVZjRQLU1heUdsa3RtTWxwaVB6YzBCYXRDYWpLdTVnbUxpdUhYUTNkNmg0cVl1aHpVY1Uxa1NRTGtCWkExZS11S216TWtabURR?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 27 Jul 2026 03:33:34 GMT
- [4 High-Growth AI Infrastructure Stocks to Buy for Long-Term Gains - The Globe and Mail](https://news.google.com/rss/articles/CBMi4gFBVV95cUxQZzZ2bGZqVkZSajNXQ0N2YmNvcl9GLUZNVjNxbGxKQS1ZRzFKX0wxdVFva2R2Sjd4Vng3cTRsb2VuNXV0WUVfbHhYejhQRUZJMGRMb1JONmhYQmxHSk5rWHRfMjE5SzZUVk5SVG5FRmpsYzhBSzVoNEU5TmpHbTQwRVpiYW1lNmsyemtpN2U3dFAzcnNnTExtYlJvMHJyMnd3cHhNY0JzamtuU0JseTR2UWpKTHU4ZnV4UFZOeE5kWk9kYkFaa2FQVExaWWV6aEdDS0NZdWlvb21yTk5hSHNqY2Vn?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 27 Jul 2026 14:10:26 GMT
- [AI 裝置能否挑戰蘋果硬體地位？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE44aU9fNUdTRVNiRkN1NS1QMXg3MWtLenYxTEYtWHBFMERtWXBEY1hCWm1nUXhoS1Y5TE9KbUtibEZtdEppb2xMMGZmd1dQNmxvREVQQUkyeml4TkZGN1FsUU14aTduMjA?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 27 Jul 2026 20:45:21 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：台股連挫「涼了」？外資喊半導體遭超賣曝AI重返賽道時機11檔有信心- 日報 - 工商時報；黃仁勳：半導體短期不會衰退，這波成長「不一樣」非景氣循環 - TechNews 科技新報；晶片 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | +0.23 | -2.08% | +1.29% | 2,350.00 | 2,410.00 | -2.49% | 背離 | 74.39 | 31.59 | 442.68B TWD / 67.87% | 2026-07-01 |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 91.67 | 114.68 | -20.06% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | -9.35% | -3.08% | 126.00 | 164.50 | -23.40% | 不適用 | 4.00 | 31.66 | 23.12B TWD / 22.85% | 2026-07-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -6.93% | +12.68% | 196.51 | 211.14 | -6.93% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 494.95 | 521.95 | -5.17% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 900.20 | 971.00 | -7.29% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -20.07% | -8.10% | 1,278.23 | 2,335.00 | -45.26% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -14.22% | +23.82% | 383.22 | 446.77 | -14.22% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip, foundry。 方向判斷命中詞：擴大。
- INTC：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 CPU, server CPU, x86, foundry；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 0 篇新聞出現相關標籤。

### 主要來源

- [台股連挫「涼了」？外資喊半導體遭超賣曝AI重返賽道時機11檔有信心- 日報 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5Ua0x1UmhtdU56bnp5a21HN1JYQm41bWZmWnZIUGJOUjQ5YzF4ekk3azNUMV9SNWdZVWY4dmtGN0FwSWJwX21NanBmcHBQWkdzeXpWZUI3eXhCOXBTamtr?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 26 Jul 2026 19:00:00 GMT
- [黃仁勳：半導體短期不會衰退，這波成長「不一樣」非景氣循環 - TechNews 科技新報](https://news.google.com/rss/articles/CBMi7gFBVV95cUxNUXp3MFBubFhLQW9sZThFWG1uYTNJc0RsWld0cEFDU2xYOGxRU3QzeHdIaFBEa3FScDBobVZCVUFsYy1ncklQZTdHLXAzRHZBNnluTkVoSUZDRmNLMTRWbGdpUHhRblZ5Q1ZpT2ZVRU5CVXA3X0I0bTNzUjhONGU5bjIwakFneWJiOTNhUmxhUzdJS1laQ0JjdGVkVTZ4M3FQa3BrRjhScElDMXFfRlBhSUtwd0ZwN1piUHpVdXJQSmljOTh4QWc3YUdzTHpVU3ZWSGJzcV9IdFR4akpyM1d3YUgtanhSQ2U4ZmRYNFh3?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 27 Jul 2026 02:41:09 GMT
- [晶片 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiakFVX3lxTFAwcUxuVXpyRlZidFhjMld5YUZvaW9qd1RVSDIybGZRUkMwb0FTWG9qeURlSjBsRzREYzVhYndta1haNk1DNjh5S0xGNWJ3dHpjRTB1LTlwa2J3SGRKZC1YU2ZlLTVoQWtkd3c?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 27 Jul 2026 19:26:05 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股外資轉買 大盤震盪 投資人靜待聯準會 FOMC 利率決議 - 經濟日報；台股三資點火 聚焦權值股 匯市本周觀察三重點 - 經濟日報；台股 ETF 科技題材火 0052今年來績效逾六成 優於多數市值型商品 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股外資轉買 大盤震盪 投資人靜待聯準會 FOMC 利率決議 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1EaGhtanNwSmgtMlVBcU9jV2F2OGFHTEJ1VDJxSUZwS3RYZ0IzcVlVUUVjRENVbTRfRUdKbnlPaWctMFJ4Tzkwc3VRQkFiVV9fWWZra0dzWXRDZ9IBX0FVX3lxTFBPREJCRWZsRHpCWUdTNjB2YUJIRkRlLUo5aDhDMmdwSWpIaVVZMkZraGlXYWxFTURSX294VFBIaFU3cURRMUItZ0R2SzRZSWt4REQtM3lSR1VhdGc4QWJj?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 27 Jul 2026 04:00:00 GMT
- [台股三資點火 聚焦權值股 匯市本周觀察三重點 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5qTFZaWFdUM3V4a2NDXzJaOWtuUjlzZmdDaUNFTXRGejhJMVFRd1BqdGJvMlktT0NuWmExQXpqVDFPVU1xeHBhSG5ZcVRBRGxzaGV3M3JMNXRhQdIBX0FVX3lxTFBsQVE4OFRZVTNBM2c0YkRNVk95TnJiZkVsOGxwSFBNc0dtckZFSGtTWE1sMjgxZHQ2T25wcVkxV3ZjQXNiWGpNaW5lbXZ6UEJzdEo2ZmlEal95aEoxNXJ3?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 27 Jul 2026 18:14:10 GMT
- [台股 ETF 科技題材火 0052今年來績效逾六成 優於多數市值型商品 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBVT3N0ZWt6V0lUejBjdmZQVE9MR0xCNUhTMjJkSmpOSDg2eXJDMndyUjNaWVdScDhiX2w4eHVNUzB0cjZabU1aYXRXYUtzc3dpQkwxWWo5WURsd9IBX0FVX3lxTE5FX09fMHFzZHRzcWNNakNwYnNucFZoZS1ubkN3cl9UUU5OWi1lM2toZTNzYTlFQ1NXTXVGUVMyNzVxTVk3MjAwOUtNSU5kQk5JNTFyWklRaXBIRkNzcWNN?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 27 Jul 2026 15:57:49 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：個股動態報導內容-3C274A0F-24FC-4054-AD95-BB1CD8595DB2 - MoneyDJ；《台股盤後》小跌20點、日K翻紅，43K失而復得 - MoneyDJ；‧永豐期貨盤後分析 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-3C274A0F-24FC-4054-AD95-BB1CD8595DB2 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxQYkkwZ1FCVnpXblR5TTllelEwT1Y4RVBIUmhHOVJjNi1WR29FYVZ0dHlXYWlDa09kV2ppQ2ZVNTFnWFdqU2gtMlJaZnBYSENIbXZ3OV9jRktYRXdVQUJyOUZ1d2RhbFAyekFzcDBQaDF0WVdwelU3YmpUeGpHa2xLeFBtbC1xeXRPdHhGM20yRUJQY0lS?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 27 Jul 2026 19:02:32 GMT
- [《台股盤後》小跌20點、日K翻紅，43K失而復得 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPQ1hVazZKR1RlVEFqMEZfd1QtSVdWT1RWQTQteWRkNGVEWmxIZXhSSmtqcVdIMlpZT01hX0M2RkdEbmprakxvME8wVEhWRkVwSnN5MEdhRjFIVExzNWZyUGQ2RGRKeU5vdkxyUzZQaFA2SmNBRHF4eHdBZXFMeDAwU1A5YjkyTm1qZG5HOEVmc0h2Zw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 27 Jul 2026 07:35:00 GMT
- [‧永豐期貨盤後分析 - MoneyDJ](https://news.google.com/rss/articles/CBMijgFBVV95cUxPMHZnOUY2N1JoaVpuOEJQS0pKa2dReTA5Y1ZCTHpIeTI4eE56T3JOek9MWmFwbXMzNGRzcmdiNVNfUVBxeTFpOS1yeUQxdWdvWlZ5aFQwTGJTTzJLNUtjcGNZaXdSSzVSM2FzNGlPeS1Vb3FMcC1WRUFTOWUySXptaWsxeUJpaXd1UmRTdjln?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 27 Jul 2026 08:26:54 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
