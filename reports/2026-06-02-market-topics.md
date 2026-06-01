# 每日股市熱門話題分析 - 2026-06-02

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜正向｜熱度 10｜市場確認 100.00｜同向 2/2
2. **AI 伺服器與資料中心**｜正向｜熱度 19｜市場確認 65.00｜同向 3/6
3. **關稅與供應鏈轉移**｜正向｜熱度 4｜市場確認 100.00｜同向 3/3
4. **半導體與晶片供應鏈**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
5. **新興題材：MarketBeat**｜正向｜熱度 1｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.08（樣本 11）
- 5日相關係數：0.05（樣本 11）
- 同向比例：8/11

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 100.00 | 2/2 | 0 | +19.72% | +18.25% |
| AI 伺服器與資料中心 | 65.00 | 3/6 | 3 | +10.84% | +10.49% |
| 關稅與供應鏈轉移 | 100.00 | 3/3 | 0 | +11.40% | +9.17% |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MarketBeat | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：TradingKey | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 相關性偏弱；應提高同向價格確認權重，降低泛 AI、泛半導體等寬標籤推估權重。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
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
| 2026-06-01 | -0.92 | -0.72 | +16.67% | 6 |
| 2026-06-02 | 0.08 | 0.05 | +72.73% | 11 |

## 歷史回測摘要

- 回測日期：2026-06-02
- 近5日 3日相關：0.38
- 近5日 5日相關：0.21
- 同向比例：+50.00%
- 權重狀態：未調整

- 方向準確度：+50.00%
- 信心排序準確度：0.38
- 診斷：正相關

調整原因：近 5 日有效樣本 6 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Micron Rises 7%, Western Digital Climbs and SanDisk Climb 4% as Memory Stocks Extend Parabolic Run - 24/7 Wall St.；2 AI Memory Stocks Outperforming NVIDIA With Big Upside Ahead - TradingView；AI's Memory Shortage Runs Into 2028 — Goldman Stays Bullish On SanDisk, Samsung, SK Hynix - Benzinga

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.76 | N/A | N/A | 1,035.50 | 1,035.50 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.76 | +10.79% | +19.12% | 1,761.43 | 1,761.43 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.59 | +28.65% | +17.39% | 224.36 | 224.36 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、memory、Micron Technology」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：increase, record highs, shortage。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk、SNDK」，共 4 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：record highs, shortage。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：HBM。 方向判斷命中詞：increase, shortage。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Micron Rises 7%, Western Digital Climbs and SanDisk Climb 4% as Memory Stocks Extend Parabolic Run - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi1gFBVV95cUxQWGk4MzVNdHRfU1JvRTc2Q2phVmRCd2Q3c0h6cVlzZ3dsczdkdzlHcGRGdXE5ZjVsY3AxMFMzUVFRMF9weG16OExPaHN2cVZHRFJiRlhaTUxLVGdvRy1Sb3VkNVF4SkxIMExoSEQ1My16Q25jZ2Jwa3o1X1BhWlNSMnppNF9nclQ0QjNRbVNTNW1rS016VDFjTXh6cVlIaUZkUXM0dThsNmE4OG13M3RjUjJ5cWhGVGo4NnI5LS1rQTg1VWxycDc0NW1PLUpfcjFmY0dyWWdR?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 01 Jun 2026 18:38:38 GMT
- [2 AI Memory Stocks Outperforming NVIDIA With Big Upside Ahead - TradingView](https://news.google.com/rss/articles/CBMiuAFBVV95cUxOa3dycEFBNVJNa2RBZ3ZYd1RCQ3JyMHZIXzgwNk9DVVRjS05JQ3BnZFVBQ0J5eFNteEs0RUw2enJuWGEtanBaNDR4ODZPQ2NoYlFDaDIyY3NpTndRUkdqR3ROdTFlVFBTaERpUU1hb3QtTWJYZk43VmtOYU9nWFFHR2tTS0syV1pjbmpQdWRRT1RvdnhxT3N3dWVieFdNN3JFa3pZWjFfeHUwYTgyRElMdDZhcEJRS0FT?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 01 Jun 2026 19:00:00 GMT
- [AI's Memory Shortage Runs Into 2028 — Goldman Stays Bullish On SanDisk, Samsung, SK Hynix - Benzinga](https://news.google.com/rss/articles/CBMiuAFBVV95cUxQRmoxcHpGcFZDbTZxM3cxNjFWRHVWUjQzSFh0Zy1fMnJ1eE9GRXhxUXpjT3RFMXJ1cUp0VkVjTHg3cGJ3cXZuQTZUZTJpVkR6TXhjczJaRjk2Z1FzSDhKVTdRZ3ZtZ19LdUNCRmYwVUJaM1lHUXdxZ1g2ZTZ6SWlFV21ZTkRhSGhscmhXRVNjQVRBRXRON2V0UE1DTDNFSzM5WUNnNDNxRWJ5aERha3dSaWt5UV8yekFq?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 01 Jun 2026 14:15:57 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Here's What Nvidia CEO Jensen Huang Said That's Causing Big Moves in The AI Trade Today - Investopedia；ARM Holdings Rockets 18%, Microsoft, Dell Rise on RTX Spark AI PC Launch - 24/7 Wall St.；AI 競爭從性能轉向語境理解，對台廠有何機會？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.72 | +28.65% | +17.39% | 224.36 | 224.36 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 新聞直接提及 | +0.33 | -6.40% | +0.03% | 460.52 | 506.69 | -9.11% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 產業/供應鏈推估 | +0.10 | N/A | N/A | 109.33 | 114.68 | -4.67% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.07 | N/A | N/A | 510.13 | 516.10 | -1.16% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.07 | +2.39% | +1.95% | 2,355.00 | 2,355.00 | 0.00% | 同向 | 74.39 | 31.66 | 410.73B TWD / 17.50% | 2026-05-01 |
| AVGO 博通 | 產業/供應鏈推估 | +0.05 | +48.61% | +38.84% | 459.97 | 459.97 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.03 | -6.39% | -2.59% | 601.00 | 611.00 | -1.64% | 背離 | 10.86 | 55.80 | 62.25B TWD / 19.22% | 2026-05-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.03 | -1.83% | +7.30% | 4,555.00 | 4,555.00 | 0.00% | 背離 | 62.91 | 72.59 | 46.74B TWD / -4.14% | 2026-05-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。 方向判斷命中詞：rockets。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MSFT：新聞直接提及「Microsoft」，共 1 篇新聞命中。 同時符合主題標籤：AI, datacenter。 方向判斷命中詞：rockets。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：rockets。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Here's What Nvidia CEO Jensen Huang Said That's Causing Big Moves in The AI Trade Today - Investopedia](https://news.google.com/rss/articles/CBMixgFBVV95cUxOdWFXY09DRktvdUQzRGVwTXg3bUFsODRsOG90UTVSUlBpQU12Nk9qWTl4czFkZTZMeGFoNXcwM3hqd0JabUl2ZjB4VjBTX2dfVkljODdNVUNZWllLcGVDMEFmSWRzaDdPaUFiSm1yTEswVzVSRjZJa1FuRGNubUpHdGFLWjN0azlpX296QkpLc2RSV2JSQ0dZdXRkajBkNGNXOGw4blN3RWRSdmladDU2Nld2TThrZkR2Q0pjVzV1di11UjZ5Vnc?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 01 Jun 2026 13:49:39 GMT
- [ARM Holdings Rockets 18%, Microsoft, Dell Rise on RTX Spark AI PC Launch - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiswFBVV95cUxPRUNoQnhKX19XdURNUjZYak9qaHM2X19HbGF1NV9UV2pvUTE4RUNQR3dLbmJmZk91TUg5SEVoZGhIWHVoeEVqM3hVeFRRNHotaEFrcU9jWE9kb29EWktjX29xREdVbkZ1cXZZakd5LTB2SDF4dW04LXhOS05KS3BOd3JXRWRXTm1RMjdnTGRhSFY3VEFBcDFWZUxyalJYel9DclJ3US1HTFdybUxJcDFRdm9nWQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 01 Jun 2026 16:31:09 GMT
- [AI 競爭從性能轉向語境理解，對台廠有何機會？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiiwFBVV95cUxQMm9HaEd2dC1na2RnRFUwcWVCbkU0UVRydHFFOTlSNU5OdXlaSFd0a1FWSE5TSzdxMm9QeFlJSW9FN3RmU1RYMTNZQlJuRFIzY1ZFaHJxQ3ZQanRXb2ZMeUZRRVUyRE4zTVRLTjBFVmZubXFWai1lUDY2MUF4VzBqVDJMblFaVWkzNTNB?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 01 Jun 2026 18:30:26 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：熱／黃仁勳的Vera Rubin放量　供應鏈14強 - 鏡週刊Mirror Media；輝達GTC效應發威，散熱與背板供應鏈齊揚-財經焦點情報站 - CMoney投資網誌；台股45K一躍而過AI放大絕這檔打入機器人供應鏈連4日漲停- 證券 - 工商時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.56 | +28.65% | +17.39% | 224.36 | 224.36 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | +0.56 | +2.39% | +1.95% | 2,355.00 | 2,355.00 | 0.00% | 同向 | 74.39 | 31.66 | 410.73B TWD / 17.50% | 2026-05-01 |
| 3017 奇鋐 | 新聞直接提及 | +0.56 | +3.15% | +8.16% | 2,785.00 | 2,835.00 | -1.76% | 同向 | 61.06 | 45.76 | 15.63B TWD / 71.62% | 2026-05-01 |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +9.85% | +52.51% | 306.31 | 312.06 | -1.84% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | +11.17% | +12.45% | 293.50 | 293.50 | 0.00% | 不適用 | 14.13 | 20.85 | 832.10B TWD / 29.74% | 2026-05-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。
- 3017：新聞直接提及「散熱」，共 1 篇新聞命中。

### 主要來源

- [熱／黃仁勳的Vera Rubin放量　供應鏈14強 - 鏡週刊Mirror Media](https://news.google.com/rss/articles/CBMiYkFVX3lxTE1iM01PTnRPWF83QXJ6MEJqckxMWUJDOUtvR1N4bWFkdlo0S2N6RG83YkUydHd1UE04ZVFjOF90aW1scTJFUmdPQ0RMdnV5NU43QjFxV25zOWN0cHFydVlhdWpR0gFiQVVfeXFMTWIzTU9OdE9YXzdBcnowQmpyTExZQkM5S29HU3htYWR2WjRLY3pEbzdiRTJ0d3VQTThlUWM4X3RpbWxxMkVSZ09DREx2dXk1TjdCMXFXbnM5Y3RwcXJ1WWF1alE?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 01 Jun 2026 18:00:00 GMT
- [輝達GTC效應發威，散熱與背板供應鏈齊揚-財經焦點情報站 - CMoney投資網誌](https://news.google.com/rss/articles/CBMiggFBVV95cUxQZktUTUYzLWdLUnJPVF9UODRobVdLSE5nMWhoRDdmQ1hmTFBQdENpNHRCNU1yS3BnYkROVU5FbmR1ODBxNHZQTkZGY3B3dXZ6eUhaZERNZWg4elk2eHlPLTdKWjVuWGlrTlQzSVlaTWRJQUdEbTFleWdEMDQ4Z0g5b3Vn?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 01 Jun 2026 04:45:07 GMT
- [台股45K一躍而過AI放大絕這檔打入機器人供應鏈連4日漲停- 證券 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE43dFVHeS1xc0xOS1p3Sk14TEcwU3VNeUxIcWdQX1ZkcnVkdXZBM2VhUjZ0VWh4NUJyRzZ5ZTZESzBvaFFFVWwzSjh0eVEtRlIzUy1XenhKTGl1QXpxX1E0?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 01 Jun 2026 06:11:00 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：COMPUTEX 6月2號開展，全面引爆 AI概念股強漲，輝達Rubin800V架構將帶動導線架與功率半導體?【研究觀點】 - sinotrade.com.tw；半導體海內外大擴產 廠務工程五雄滿手單 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +28.65% | +17.39% | 224.36 | 224.36 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 109.33 | 114.68 | -4.67% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +2.39% | +1.95% | 2,355.00 | 2,355.00 | 0.00% | 不適用 | 74.39 | 31.66 | 410.73B TWD / 17.50% | 2026-05-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +1.74% | +16.80% | 146.00 | 146.00 | 0.00% | 不適用 | 4.00 | 36.68 | 22.66B TWD / 10.80% | 2026-05-01 |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 510.13 | 516.10 | -1.16% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 1,035.50 | 1,035.50 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | +10.79% | +19.12% | 1,761.43 | 1,761.43 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | +48.61% | +38.84% | 459.97 | 459.97 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 CPU, server CPU, x86, foundry；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 0 篇新聞出現相關標籤。

### 主要來源

- [COMPUTEX 6月2號開展，全面引爆 AI概念股強漲，輝達Rubin800V架構將帶動導線架與功率半導體?【研究觀點】 - sinotrade.com.tw](https://news.google.com/rss/articles/CBMirARBVV95cUxQYVNIbkZONWdtVDF6eGV5YjlqemtTajhNVjBYdDlqT213WmV0MkJ2QkdWWXJGSU1sbHZYSVR2WW1fOVZvV0E1ck1yMHZRYWo5Ym5ubFFQalV4RkVnb2J1RmRXRW8zeThyQjBxbktweUtSUklYSklLckticUNEcnZwWi1kdm5OV3hkbk84aGtrUTNWVE5XNnUzUmJyaVNUT3JnR0h5TFZySGYxSERkZHNRUE4yOU1tSXFBOWtfWFVRajVGU1hXWExNYnJNWjY4aVAtWXBJWWJJdXNaS1h6UDV0dUZmZWFjc1NxR2tqbmgtVk1CcGtSaS0tM19VVmk5LW5xU0F3TUlwRnY0M0xqTWxlVXFHb2Y0dVNvQXgzNDJ5MFVzMDM5WU1MMEp6MVd0Tk9RTHJQMHRJVkV2bDZZZ0QwQ0tsenJveGJuRG5VTzRad2VlWVNhRm9JTTd3VElFcmJrU05RdDZqeDlmS3Bzd2hnTUQ3a3lYRV9ScThTT3hIZUwzOHcxUlRpQkRPVFUxYkdjYnhGZjFudXdPTFJzWGZRb0hLU0dHMnZQdnhVUnpLa0xOWlZsX3Q5S0lnRXd6R0loR0NtREpxVmVCNTdqRjZQaTRGSndFSl9QVDNWUGEtc01INlo5d0NKa25uejR1SFByR0FReVphcUhDYzhubGliQXVGSWh3aDFVVmtiTmhyUG82WW10ejNUVnVhc3J3NjgxdUROMFVFSGZLejc4?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 01 Jun 2026 02:26:28 GMT
- [半導體海內外大擴產 廠務工程五雄滿手單 - 經濟日報](https://news.google.com/rss/articles/CBMiW0FVX3lxTE45NHkyRzZpVUUtWldpampiTTZUZDVtZzRibmRYSGM3YUJYcXVKWklIbng2dGw3SXd2aDdxUmRoWWFjeTlUMkF4NGVqYlgxMWxOZ085TExtdjRGUGPSAWBBVV95cUxQX3pQOHQyZGVJcktEanNRWjJyY19hclVTc1RGYjJfTkF0RTFxMmZBRDk3MExHay1tZ1FaNGdkdGgyR1hZQUY2eXMwSXdEck1TMklBVGF6c2lVenVCQzEwSlk?oc=5) - Google News source discovery | 經濟日報 money Mon, 01 Jun 2026 01:00:00 GMT

## 新興題材：MarketBeat

摘要：新興題材：MarketBeat 相關新聞集中在：Mizuho Forecasts Strong Price Appreciation for Intel (NASDAQ:INTC) Stock - MarketBeat

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.56 | N/A | N/A | 109.33 | 114.68 | -4.67% | N/A | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。 方向判斷命中詞：strong。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Mizuho Forecasts Strong Price Appreciation for Intel (NASDAQ:INTC) Stock - MarketBeat](https://news.google.com/rss/articles/CBMiwAFBVV95cUxNdFo0TXNId3RQTWtxekxVQzZZTGR5bnI0a3JORjBSMXdINVlsM0dtOEthRTY0RXlZV3lNM0dPMVNDaVQwRThOakY0Rk05OHlNMGJCQVl1MjJxX2F3UUY1b3ZwTExzVlk5S05UM3QxZXc0U251WjJlM3liME5TTGRtR0pWYWllR3RNUjloRk0tU2o1YzVkaVlfa1lMenB1a3NLYmU0N2lWWHQ5Uk5YWXBRTTVGM0VmM3VSaURXSTBjVFQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 01 Jun 2026 12:15:33 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股6月開門紅寫五亮點 法人：不預設高點 行情偏多看待 - 經濟日報；證券開戶數創高 老中青齊發 - 經濟日報；國票金控旗下國票證券遭檢調搜索 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股6月開門紅寫五亮點 法人：不預設高點 行情偏多看待 - 經濟日報](https://news.google.com/rss/articles/CBMikAFBVV95cUxQWXQtdTNZdlpYQWw3WVpWMU12OHl3Zi1hclVBUUxRS0tXY1FtWHk2TXF5THpQWmJlQm5RUHRTbDBFWTJ0eklYYjEwOGp6c2NXRThoZWVGbVNsY004QzlCZEQwQzNUejBWRExHQ2F2a3gwM19mY082djN2U21lNmliRDBldkZ5a0ltSjFzbFFraWfSAV9BVV95cUxQcm1XUXo4Qi1EREFIamFfRGlPcTdzeXVLd2JDZzhSZkYyZjNUYXNreVRkaGlxN3dDd0tmNzFmNWZZQUpQQUtQMmViS2doYnFoRXFGQkxiaWVOSGhRVERsOA?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 01 Jun 2026 17:56:16 GMT
- [證券開戶數創高 老中青齊發 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxPYzQwSVR2TlZoUUEtWDU1MHphWW4tOEJTc3I2U01UNzhpcDNOMmc1WHpGc2dzOHJqdDNKMDRYQ0ZTWVNQS1ppNVRLNjJMM1UyQVFtMGlrWUZ5SXpwdjl6dm8wY00zQWZPUWxFakgtRU1neFFoanVBMEF5UWpWVUxHRtIBX0FVX3lxTE9sMy1uckg4UDhUMkFJM0FMNEZPZklfT2hFZFlPSmtPbHc4WDBVQV9WWl84Y3EtRmFHWW1nbjRDY0NpZHYzWUp4aGdYRHhuTEVPbV9iVGJpX29acll0aXJR?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 01 Jun 2026 16:43:03 GMT
- [國票金控旗下國票證券遭檢調搜索 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9XSHRuUnk5aXpQN2U5MUFlaW95amswM1hZTHNZQWV4dDk5cmNnMG1FSUxVS3B0YW9Nd3pYWEFUaTJMMHdMVHctU0o3SHNzWUotZ21pb1FTX0djZ9IBX0FVX3lxTE16U2NxSldSanZTaDlRMDJvTnV2MkZEVVdFMWdJUmtQUS1oeE80b0Rad200SklCWjNzV0JCSUlseUZnVUh2a09KckZhMTRxb1hOczcza1pNUFNBVy1UYXdz?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 01 Jun 2026 11:34:39 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》量縮收漲604點、日K連二紅，首收45K - MoneyDJ；00981A除息日6/16；台股仍有機會震盪向上- 新聞 - MoneyDJ；柏瑞投信：透過GIANT投資術，掌握台股AI產業升級投資契機 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》量縮收漲604點、日K連二紅，首收45K - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxONy1TUTNacjd2UDZPeHF6SEtRQzFUd1ZvLXkyVmZ6a0U5OXlxWWFsN2x6UVRqVmxYTExqRXlMVFhYaDBNaE1FTVQ2RXBSRlRNUGxMZFhTR0o2aGZPQjNyVnpnUGhqNmVUWjJfQjA4bDZtR1hQUlhoTlIyRmpRbDNGQVpqWkJfSTRhR2VqUEZKWWhQZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 01 Jun 2026 07:36:00 GMT
- [00981A除息日6/16；台股仍有機會震盪向上- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPbTNRYUhxdFM0Y1ZGRTVQMUplWFdEMzc3WTIwZ2lTOGlDWlBGWG9TVnNFb1prNFJMUXFiNHRqYmpLNE44ZE54b3Nic0Z2aFpSVU1kME1GT3dQbGh2MDNUYWdlNzZ3cmFKVHFFdEkzRFYxS2RWY0k4ZHktYk1QVU82NFhrdDBnVXIxN3VBUXNXZnZUdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 01 Jun 2026 08:42:00 GMT
- [柏瑞投信：透過GIANT投資術，掌握台股AI產業升級投資契機 - MoneyDJ](https://news.google.com/rss/articles/CBMilwFBVV95cUxNU003bGpTejN0OE42eUVvY0I4WWVmUFNybVEyY0lrREs2TEJVdEZXOWpOUzJ6M0FiU3h5bmV3THhQMWt6dGxkNGlaZEpBR2J0dVNhbE5aYmhhQll3dFVBTy12aW95ekFEWFZwR2w4Z2VscW5tT25sNFkwRVl5TERzeTV1X3RLQWdvbjUtMmZoN1dFb0VuZS1J?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 01 Jun 2026 07:57:00 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：SK Hynix 1,000% Annual Gain Not Enough? Top Wall Street Funds Increase Stakes, Will HBM Chip Supply Shortage Escalate Further? - TradingKey

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [SK Hynix 1,000% Annual Gain Not Enough? Top Wall Street Funds Increase Stakes, Will HBM Chip Supply Shortage Escalate Further? - TradingKey](https://news.google.com/rss/articles/CBMiswFBVV95cUxNeVFoMlVkLVZfWERVemV6Qm1Ga1hGazNMb19RNk5YODdKdWZLZlVhTnE2alVMcjlDekJCdnZCcTVVUnVCQUJDU1lpUndibS13RGs0U1ZmSDhWTXp5REU1WkhkdHBMaVI3bWVDRmU0TEV3aVdzM0dBRTJRUnpaYlJwVTNhYlJTY2JCeUJuR182LVhSYnJ6c3pzU1hiMTFjZW11X0piZ1ZSRnEyYW42X1Bac2RHTQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 01 Jun 2026 13:05:45 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
