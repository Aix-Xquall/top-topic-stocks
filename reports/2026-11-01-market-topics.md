# 每日股市熱門話題分析 - 2026-11-01

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **綜合市場情緒**｜負向｜熱度 43｜市場確認 81.37｜同向 3/3
2. **記憶體與 HBM 供應鏈**｜負向｜熱度 5｜市場確認 100.00｜同向 3/3
3. **AI 伺服器與資料中心**｜負向｜熱度 16｜市場確認 70.49｜同向 6/8
4. **散熱與液冷供應鏈**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0
5. **新興題材：MarketWatch**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.47（樣本 14）
- 5日相關係數：-0.40（樣本 12）
- 同向比例：12/14

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 綜合市場情緒 | 81.37 | 3/3 | 0 | +3.79% | +6.80% |
| 記憶體與 HBM 供應鏈 | 100.00 | 3/3 | 0 | +21.11% | -27.55% |
| AI 伺服器與資料中心 | 70.49 | 6/8 | 2 | +6.00% | -6.71% |
| 散熱與液冷供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MarketWatch | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：OpenAI | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：B974 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-10-19 | 0.44 | 0.36 | +50.00% | 12 |
| 2026-10-20 | 0.09 | -0.81 | +69.23% | 13 |
| 2026-10-21 | -0.25 | 0.23 | +5.56% | 18 |
| 2026-10-22 | 0.02 | -0.21 | +38.89% | 18 |
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

## 歷史回測摘要

- 回測日期：2026-11-01
- 近5日 3日相關：0.14
- 近5日 5日相關：-0.17
- 同向比例：+52.63%
- 權重狀態：已調整

- 方向準確度：+52.63%
- 信心排序準確度：0.14
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

摘要：綜合市場情緒 相關新聞集中在：個股動態報導內容-02D16A59-9517-445F-82C9-7E2668667D1A - MoneyDJ理財網；個股動態報導內容-9023EB2B-A1A7-4A65-9B53-6438EDCA3C65 - MoneyDJ理財網；上市櫃公司獲利連年成長 台股明年發放上看5兆 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | -0.42 | -1.25% | -2.07% | 2,370.00 | 2,480.00 | -4.44% | 同向 | 86.28 | 27.47 | 511.86B TWD / 54.65% | 2026-10-01 |
| 2454 聯發科 | 新聞直接提及 | -0.42 | -1.14% | -5.43% | 3,915.00 | 4,920.00 | -20.43% | 同向 | 60.69 | 64.66 | 55.40B TWD / 1.97% | 2026-10-01 |
| 2303 聯電 | 新聞直接提及 | -0.42 | -8.98% | -12.89% | 111.50 | 164.50 | -32.22% | 同向 | 6.80 | 16.47 | 25.35B TWD / 27.22% | 2026-10-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。
- 2454：新聞直接提及「聯發科」，共 1 篇新聞命中。
- 2303：新聞直接提及「聯電」，共 1 篇新聞命中。

### 主要來源

- [個股動態報導內容-02D16A59-9517-445F-82C9-7E2668667D1A - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilAFBVV95cUxNNkNuTmY2MDM0V0hjWnZyeU16OWVOSkNwZzBZSkwxa3FiY3htYVZOQ0ZNQ3JVZVVpb3c4cUtFQWNDNUxHdUlUNUJmSmNiMDduNVRjSmFaa3ZqOTFtTkZlVjhuRXV4SUlLNDVra1pyUjZWd0VtRDIxQUwtUTFCazR2NEZiRjBySTZsUk1SLVgtVm4tdi1C?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 30 Oct 2026 11:44:48 GMT
- [個股動態報導內容-9023EB2B-A1A7-4A65-9B53-6438EDCA3C65 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikwFBVV95cUxNaXRiNjh0LXNKWkpqT0VTVTgtaHV2ZFlJWVF1ZkNVN1RqcU90T1paQjFrU1RrT2ZPN21xbXVGR0FqT2oyT182b3Y4Q2JvWlF6aGVmU3RrUlNFUHgxbWlYYjA2ai1WdmhoT3BVcTZsQ3drZjhXZ2hsSHd1a3VJRDdxRmJ5ei0xRTEwQ05DX01kZmVFS0E?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 30 Oct 2026 16:00:59 GMT
- [上市櫃公司獲利連年成長 台股明年發放上看5兆 - 經濟日報](https://news.google.com/rss/articles/CBMihAFBVV95cUxPbVQzQTR3VlFBRWpoZmZESTNQVTdwNFR2TkQzTFBJdUY0eGRNazZ1UHkyd2ZrR3VJbnczbEdOUE54Z2Q4VVVDdHRHQk1HS3VaMUhDTEZadXkwM2hTVTgwdld3aFFxZGcyNVNUYjJza2VmbzIwZDhOYnBvWWV5cUhvSUZrN1PSAV9BVV95cUxNeU9oRzRORUdhWTJqb3ZGZHJSaFBnYktfRExya203b0Y3b2J4aXY2dldzeVdWb1ZoUUdMUU1jcEJ3OGJlSnlaZTF2bC1tUEZCV3FiVVFVeGxLLUNVMkRQcw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 31 Oct 2026 18:38:40 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Sandisk Sinks 9% Despite Earnings Beat, Raised Guidance and 8-for-1 Split; Western Digital Tumbles 8%, Seagate Slides 7%, Micron Falls 6% - 24/7 Wall St.；Why are Micron, SK Hynix, and SanDisk stocks falling on Friday? - Invezz；批 PC 配大量 DRAM「相當糟糕」！Sam Altman：應優先配置 AI 資料中心 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | -0.57 | -8.88% | N/A | 884.74 | 971.00 | -8.88% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.56 | -11.80% | -7.04% | 1,150.89 | 2,335.00 | -50.71% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | -0.42 | -42.66% | +62.13% | 65.76 | 114.68 | -42.66% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -7.31% | +2.27% | 204.64 | 228.38 | -10.39% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、DRAM」，共 4 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 2 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- INTC：新聞直接提及「英特爾」，共 1 篇新聞命中。 方向判斷命中詞：暴跌。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Sandisk Sinks 9% Despite Earnings Beat, Raised Guidance and 8-for-1 Split; Western Digital Tumbles 8%, Seagate Slides 7%, Micron Falls 6% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMigwJBVV95cUxPRHRncUhXeEE4ajg0RnF2WVhka1ZpVFdYM1BhOGFjRlRaMndMQmh6VGVCekx0TTJzQmZKUVJ4d0JsSm02RjM4MjF3b2p2blY0ZlZ6R0dVbE5NWTVuOHBqTTctY0czUVdYbnZHanNTYXR2ODlwNkd2S1RKaENyejg5REpWQUdzOHRaTFcwUVYxLV8tUlRmcHVCNTlWNk5ld0Q1R1lHV1RpZ0xDLTRNQ2x3S3VkdEVZVXpieEc4TEg4UkFsdG1IZnVTeFMxV1c5Sk00U3ljeWN3aG56N1J4Y25ZUHRUQnUxS0dzZnc0NnVINlowNDcyMzhuNmFjaUM2ZDlDQzdR?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 30 Oct 2026 14:17:00 GMT
- [Why are Micron, SK Hynix, and SanDisk stocks falling on Friday? - Invezz](https://news.google.com/rss/articles/CBMinAFBVV95cUxQLTI3S1Zrcy00S3VBNURhWGpHWWhKLTdlWWYwNTF0aEFaUFVScldPbTVyQjRJZVZhTzl0Mm54MG5XNGl2emdzZVFkNTFvMlRoUGZxNVVnWm1iS1Z5ZTV2OFJhOG5GQWJueTlyMk40aVBVMHdNSWJucEJ1U1JiU1Q5ZEg5RE9aTjdqeGFWR292Y0VlU0xVSkxEeTV1RDY?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 30 Oct 2026 15:01:33 GMT
- [批 PC 配大量 DRAM「相當糟糕」！Sam Altman：應優先配置 AI 資料中心 - TechNews 科技新報](https://news.google.com/rss/articles/CBMieEFVX3lxTE1aM1Y5TUN3UGcwN1ZLdnFISnpqR2xmZEVPNEp6SW5OY19EQm8zelVLMktELU1UMmtpOWZOMzBRQlNYM1pmcXNLM084V1plSUFmdUtJZTNGR0hsMnRBWDB0LXpVU2VDR01hbHlCSGNtQW5aekRZQV96Tg?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 31 Oct 2026 01:25:34 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：AMD stock falls as Intel's earnings flag PC slump and server supply squeeze - Quartz；AI 提前 15 個月預警「癌王」胰臟癌，敏感度高達 73% 遠勝傳統判讀 - TechNews 科技新報；台達電 AI 訂單能見度高但出貨時點變動大，鄭平稱庫存增加屬階段性現象 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.55 | -42.66% | +62.13% | 65.76 | 114.68 | -42.66% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.53 | -2.19% | N/A | 504.80 | 516.10 | -2.19% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | -0.06 | -7.31% | +2.27% | 204.64 | 228.38 | -10.39% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.06 | -1.25% | -2.07% | 2,370.00 | 2,480.00 | -4.44% | 同向 | 86.28 | 27.47 | 511.86B TWD / 54.65% | 2026-10-01 |
| MSFT 微軟 | 產業/供應鏈推估 | -0.02 | +15.92% | +6.08% | 521.91 | 521.91 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -11.95% | -13.68% | 326.08 | 446.77 | -27.01% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.02 | +2.61% | -2.34% | 668.00 | 703.00 | -4.98% | 背離 | 13.92 | 48.34 | 88.13B TWD / 45.52% | 2026-10-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.04 | -1.14% | -5.43% | 3,915.00 | 4,920.00 | -20.43% | 同向 | 60.69 | 64.66 | 55.40B TWD / 1.97% | 2026-10-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 5 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AMD stock falls as Intel's earnings flag PC slump and server supply squeeze - Quartz](https://news.google.com/rss/articles/CBMieEFVX3lxTE03WGhQN1lFOU5lR1ZLNWFYdmRmZjNKTjBrNW9DX1FZbkpaVDczTXYwUG91VDBVYkwxNVJROXhmNFk2UG9ST1UxRFo3b1VfbUNpcUF2NVJ0WXJnbFo3eUQzUE85QVdqMEZwY1NBZ0xVWTkwRzhhb3I0TA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 30 Oct 2026 13:36:23 GMT
- [AI 提前 15 個月預警「癌王」胰臟癌，敏感度高達 73% 遠勝傳統判讀 - TechNews 科技新報](https://news.google.com/rss/articles/CBMid0FVX3lxTFB1d1l6YUtxSzFwbVpmRlVPRjBuYjd6RFRYRGVoMDUyX2hqLTJ1cWRqZ3N1bXNtXzFMV2V1cmNRZ05hUi1mOXlLZXNVLUR1MVZvam5wclZ1LUhZVm5oOG42dWNxeERuZU9UOE90UDlJSmdVR3l1T3ZR?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 30 Oct 2026 16:18:52 GMT
- [台達電 AI 訂單能見度高但出貨時點變動大，鄭平稱庫存增加屬階段性現象 - TechNews 科技新報](https://news.google.com/rss/articles/CBMitgFBVV95cUxOcm1mTlpnc3RkVXNEV0RyNmtwUnNCU0tKT2lNM0t1c2RGR2s5LUIwSmw1RWZxaDRZMmEzVklzNDBVallMdnd1UjJXaW9rSjQ4SHZ3M0NwY2hVTFlhRnVYMlJIdU1hS3kxN0VTV01SU3NodWhFX1BVZEZxcGNhNnRSeVptajdDT2duOTlrb2lWZld6RGlsd2VBcTdlNTc0WXBIanJzaUJHZERtTVJLWW9PQ0ZwRHdDUQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 31 Oct 2026 06:03:52 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：散熱股又有大消息？花旗喊買奇鋐、雙鴻 目標價齊升逾14% - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | -1.12% | -4.33% | 3,095.00 | 3,435.00 | -9.90% | 不適用 | 75.13 | 41.26 | 21.02B TWD / 44.92% | 2026-10-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐」，共 1 篇新聞命中。 同時符合主題標籤：thermal。

### 主要來源

- [散熱股又有大消息？花旗喊買奇鋐、雙鴻 目標價齊升逾14% - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE04UXU3RGRUUnBBVElIbVBGZWozMUxfTzNsbE50ejYzRE1pUTJBQ0FNWS03VjRSYlZrUWkzSXhuNHhFQl9teWs5YTJ4QUU4ck1MZ0NneEk3XzF3UdIBX0FVX3lxTE5tclh3dXNNWDhDMnNiYmMyRW1DRFJwZUt6ZlZXMmdEYlhoQU9VR1pSeTVrVUpVT2FWOE1idEkxdXRhYTYyYVpMcnRwaWQ4NGpmRUNTREJUQ2UwNU01N0pF?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 30 Oct 2026 09:00:00 GMT

## 新興題材：MarketWatch

摘要：新興題材：MarketWatch 相關新聞集中在：AMD’s stock slides after Intel earnings reveal two big issues - MarketWatch

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AMD 超微 | 新聞直接提及 | 0.00 | -2.19% | N/A | 504.80 | 516.10 | -2.19% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | 0.00 | -42.66% | +62.13% | 65.76 | 114.68 | -42.66% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AMD’s stock slides after Intel earnings reveal two big issues - MarketWatch](https://news.google.com/rss/articles/CBMipgFBVV95cUxQSG1ER3NBSmVWMHJlelZ0akVNa1FTVDFlM1J3b2ZMOWZXanV1cVdDblB6dDlHRmJYZDRVZ2JKWTRfRDIyTkZaNENTZVQ2MGFJUjk2X0ZfU2ZTVjZEcm02VlJZXzQyYmlVdHY2Mm5BaEVvUmN0Tm1rQUF2NWlIQTdLMFpWNVl3QUNvX05MRlg0cmw5d1JQWjAxeUtDeHpVandzY2tDZGxn?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 30 Oct 2026 20:28:00 GMT

## 新興題材：OpenAI

摘要：新興題材：OpenAI 相關新聞集中在：OpenAI slashes funding target by $10 billion amid tech rout, FT reports - Reuters；OpenAI pares fundraising goal, now seeking up to $20 billion in latest round - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 新聞直接提及 | 0.00 | +15.92% | +6.08% | 521.91 | 521.91 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：新聞直接提及「OpenAI」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [OpenAI slashes funding target by $10 billion amid tech rout, FT reports - Reuters](https://news.google.com/rss/articles/CBMinAFBVV95cUxNTWw3N0l5dm5KUi1FQmllTEpEeUdkY1k5TVlFNTlnWWFlbTgtdUJfZE9RMjZiQlJEVXU2VFo2blVaWk1MZzNYMm9OYmdrSngtSk02YnhKNDdVMVZkS3hIMHpWZ2dnRjJZWjBzQ0lFRU4ySFFUQzdTdnUzN3JETGtCYlo3Y3kxeGJseG5veVJMSVVCRDVPYzB3TXQyaFE?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 31 Oct 2026 00:17:00 GMT
- [OpenAI pares fundraising goal, now seeking up to $20 billion in latest round - CNBC](https://news.google.com/rss/articles/CBMiggFBVV95cUxOb2hwU1RZMjNaMVpkcW13aDRGb3M0UGlMb21CRTI4dDU5STc4eEJkZHNMc2VPQjVnYm80MEEzWm80RDFZdElReXNmbG1sS0xBYjNnNWNOZVJsSUhySmhIUTJfV0tEZjJncTFLSHJFbDVqU2FrdmlSVW1hNzdxZG8tbktn0gGHAUFVX3lxTFBEd2ZuVFNJR09vWjBBWUtDMF80c1luQkFnVWRkN2RWMG1DWmZJd3Z4clZwcjNIeEcwaExPcjc5MWt2MkZ1SW9KUHdZODhtV3NGanVTSVkzdFl0aTQtUmxZa1V6dHpDUkxacTNhTk1PWXFDbnVIR3NraVRJODh3MjFGdUhBNl9rTQ?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 31 Oct 2026 19:56:23 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：護盤？台股重挫1156點一度跌破半年線金管會、國安基金信心喊話- 新聞 - MoneyDJ；20261030台股融資維持率 - MoneyDJ；《台股盤後》收跌1156點、險守45K；周K連三黑/本月跌5.7%-新聞內容-基金 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [護盤？台股重挫1156點一度跌破半年線金管會、國安基金信心喊話- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNWmJsZXl1YnhxMkd3SlpwS3VuMFZVSmx2NHFITkdSMWpLWWRXZlFWaDI3YVpodXd3TWRPUml1aGxIOEotcERhNk15YU9FU3FieW9QcEVMR3JqZjRrVUo0QXphd2U0VXFvbFNFWlZoa2RTSlJleDQ0QnA5UTNpLS1wNFJRc0t2Z0N0dXNaQ2pKakc4UQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 31 Oct 2026 02:36:00 GMT
- [20261030台股融資維持率 - MoneyDJ](https://news.google.com/rss/articles/CBMisgFBVV95cUxOMnRaN19teXVpY2RWVUZhTmc5VC1DeHdlbXBRUzNFZ3p6dzctcWNKQ2tRRVBFdkNRREc0OWpFUWFxUWV0aGFzMzJzeVhwTVBIamxGSzdXQnE5NUxqWmVGWkF2UzZScERGNE8zNFU4eE5rNTVMX203bEcwWS1oZWdjSTNjaGE0enJ0SzRYMVBmNTNqUUhVUEQ3SUJac2Iwb0pFTTNRbU9fVWhyTXhoX0J3ckVB0gG3AUFVX3lxTE02dnFHNGtmNVNWWG9FWURMZGN5bEMyU0E1QnMwbUxJQWpoam54LUhlUzhnRjJiMDJmdndTaUMyT2NyU3ZOWGtVbGMwNko4TTlIRTd5T3hKZVM5aFhNMEFKZlpsMElFOEtzLXFWaG5KWGlhTjZaZ3pORGNJNmp3TW92ZWpiNVRXRExPV011Y1QtZmcyNkRId2NyTUtzQzVSeU1HUXNoNjRtVkFQNDVCbGZyYUlwTTgxSQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 30 Oct 2026 15:03:35 GMT
- [《台股盤後》收跌1156點、險守45K；周K連三黑/本月跌5.7%-新聞內容-基金 - MoneyDJ](https://news.google.com/rss/articles/CBMikwFBVV95cUxObkN2Wk5UZ1BoTGhTcE0wYzcxWWVfMDZyLVN3eFFjaXRiOEswNHcxVU5NdC1rTUU3bmVIQi1CUWVycEM2ZWVrdkkwNmpKdXFFRVZWeTNfVHdjY0FNbTVZaW14R184NDNZUGZYdTZHd3l3cnh0ODZoNWxWajdyRjBpVXl4Z2ctVTZlVU5WaVVybXhNdmc?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 30 Oct 2026 07:57:00 GMT

## 新興題材：B974

摘要：新興題材：B974 相關新聞集中在：個股動態報導內容-52418D41-0A3F-406F-B974-506F901D9D92 - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-52418D41-0A3F-406F-B974-506F901D9D92 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikwFBVV95cUxNOFlIVWNNTHlPZGVidl9BZ2ZyZ1lacmhXckJiVkpOWVRPOFdSemlMUkQzUjJfbUFHRDNXU1QtTnlYQXFzM3ZteThUcDR5ZHVOM0ZacmtqUEh2U1lIV21hdEhCU1JZVDJJQWJDLXdYNjhWYi1zeXZyVnVFRVZBYWJvS1BzSmF6OGdPSV8tSk5kTVQtY28?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 30 Oct 2026 18:27:51 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
