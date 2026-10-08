# 每日股市熱門話題分析 - 2026-10-08

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜正向｜熱度 11｜市場確認 56.53｜同向 2/4
2. **AI 伺服器與資料中心**｜中性｜熱度 14｜市場確認 N/A｜同向 0/0
3. **利率與成長股估值**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0
4. **關稅與供應鏈轉移**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0
5. **半導體與晶片供應鏈**｜正向｜熱度 3｜市場確認 62.23｜同向 5/8

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.13（樣本 12）
- 5日相關係數：0.40（樣本 6）
- 同向比例：7/12

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 56.53 | 2/4 | 2 | +7.18% | -4.01% |
| AI 伺服器與資料中心 | N/A | 0/0 | 0 | N/A | N/A |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 關稅與供應鏈轉移 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | 62.23 | 5/8 | 3 | +6.16% | +4.54% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：BigGo | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：B7810D00 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-09-25 | -0.31 | 0.15 | +30.77% | 13 |
| 2026-09-26 | 0.22 | 0.14 | +63.64% | 11 |
| 2026-09-27 | 0.11 | -0.14 | +57.14% | 14 |
| 2026-09-28 | 0.05 | -0.53 | +63.64% | 11 |
| 2026-09-29 | 0.31 | -0.78 | +16.67% | 6 |
| 2026-09-30 | 0.05 | 0.04 | +33.33% | 18 |
| 2026-10-01 | 0.21 | -0.27 | +40.00% | 20 |
| 2026-10-02 | 0.51 | 0.37 | +72.73% | 11 |
| 2026-10-03 | -0.35 | 0.13 | +16.67% | 6 |
| 2026-10-04 | -0.12 | 0.70 | +80.00% | 20 |
| 2026-10-05 | -0.16 | 0.29 | +73.33% | 15 |
| 2026-10-06 | -0.72 | -0.75 | +37.50% | 8 |
| 2026-10-07 | 0.48 | 0.61 | +73.33% | 15 |
| 2026-10-08 | 0.13 | 0.40 | +58.33% | 12 |

## 歷史回測摘要

- 回測日期：2026-10-08
- 近5日 3日相關：0.23
- 近5日 5日相關：0.31
- 同向比例：+50.00%
- 權重狀態：未調整

- 方向準確度：+50.00%
- 信心排序準確度：0.23
- 診斷：正相關

調整原因：近 5 日有效樣本 12 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：INTC, AMD, MU, SNDK, SOXX: Chips, Memory Stocks Slip Premarket After Sharp October Rally - Yahoo Finance；Memory Trade: Cyclical or Durable Growth? - TradingView；Sandisk Is Up 613% in 2026 and Micron Isn't Far Behind. Which AI Memory Stock Has More Room to Run? - The Motley Fool

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.57 | +12.05% | N/A | 1,088.00 | 1,088.00 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.28 | -7.12% | -4.01% | 1,660.46 | 2,335.00 | -28.89% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.42 | +25.14% | N/A | 645.86 | 649.42 | -0.55% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.21 | -1.36% | N/A | 113.12 | 114.68 | -1.36% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +7.56% | +18.68% | 237.47 | 239.24 | -0.74% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、memory、Micron」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：risk, growth, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK、SanDisk、NAND」，共 5 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：risk, growth, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [INTC, AMD, MU, SNDK, SOXX: Chips, Memory Stocks Slip Premarket After Sharp October Rally - Yahoo Finance](https://news.google.com/rss/articles/CBMijwFBVV95cUxQWTlvdUh6RThyWDMySW9PNkR5djBpM0hiRkV1THlPZkdENEdlSW9tcTdYN0FfazcyM0JSTWduaVBXWTN1SEN3NlVLenFIRFZpS3Etc1BaWFZhcm00RGhabFVWei1HdG1rX3EtQTl1M29Vdnpqamk3U3R6REQ4Rk9YcV9LVkswYnhyaHlCUWFDMA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 06 Oct 2026 09:12:51 GMT
- [Memory Trade: Cyclical or Durable Growth? - TradingView](https://news.google.com/rss/articles/CBMimwFBVV95cUxNOEdQZWVvQnFiVzNHM0JnSDNjQXhsaTFyd3RUV0NiNmdKUE56MmxmWXI1M3gyTTU2V2Jfb2EyN3M0cFlBdm5Jb3NMVDJLR29MYmpleTMzWnFFLXlzWlJBYmlaZ3FTNnF3V1hUR1BmQmVncWFGVVRfVDJacVg3bldMc1dKY3dzYmpZMjFkQkNwMGxtRXkyOWZRMjZEOA?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 07 Oct 2026 20:05:00 GMT
- [Sandisk Is Up 613% in 2026 and Micron Isn't Far Behind. Which AI Memory Stock Has More Room to Run? - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxPbktRQm9WOXZlQmN1d3dITVNQYk5FbUh6RERNdlNaUzRNUmVpbTlpMHltM3FHNU04WVo4dlJ5NmJqTnVnYzNVVFlvdVZFeUZSUmE0ODNpMW5vSnptdUUxbWg1eDgzSklFblBYbDdTRzdsVzR5X0tmbWk1bnpHZTNkNDBfWlpHZWQzbjhrVmF6djR5dnBjbGd3VA?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 07 Oct 2026 10:15:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：AI Token經濟狂燒聯發科面臨兩難- 產業 - 工商時報；AI 搶電再推核能熱潮！Google 簽 20 年長約、核能股齊漲 - TechNews 科技新報；年底大選逼近，當政治人物開始用 AI「借你的嘴說話」 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2454 聯發科 | 新聞直接提及 | 0.00 | -2.32% | -1.73% | 4,800.00 | 4,920.00 | -2.44% | 不適用 | 60.69 | 79.85 | 64.18B TWD / 44.08% | 2026-09-01 |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | -1.36% | N/A | 113.12 | 114.68 | -1.36% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +7.56% | +18.68% | 237.47 | 239.24 | -0.74% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | +25.14% | N/A | 645.86 | 649.42 | -0.55% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +3.40% | +4.23% | 2,555.00 | 2,585.00 | -1.16% | 不適用 | 86.28 | 29.96 | 514.81B TWD / 53.32% | 2026-09-01 |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +17.66% | +7.67% | 529.76 | 529.76 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | +1.67% | -0.33% | 376.51 | 446.77 | -15.73% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | +2.66% | +4.13% | 717.00 | 744.00 | -3.63% | 不適用 | 13.92 | 52.97 | 82.25B TWD / 45.66% | 2026-09-01 |

關聯理由（前 3）：
- 2454：新聞直接提及「聯發科」，共 1 篇新聞命中。 同時符合主題標籤：AI。 方向判斷命中詞：恐, 擴大。
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：恐, 擴大。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：恐, 擴大。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AI Token經濟狂燒聯發科面臨兩難- 產業 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTFB2ZkxnWFc3UGUySE9BR3U3Q25aMmNlMjhFRkQzYUdfUXphcGZwQlhqaHJJNFE0OHVhZVRpeW1scXVCdWZSMkNUaFlRb05pNVlyYnFnNTlySDZtR1NoYm5R?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 06 Oct 2026 13:17:00 GMT
- [AI 搶電再推核能熱潮！Google 簽 20 年長約、核能股齊漲 - TechNews 科技新報](https://news.google.com/rss/articles/CBMisAFBVV95cUxOWGh0WW02YlFueWpEOVJWelU5dkNDR2ZUMlhQU2N4b1lwMmFZdW1PYU9yR2UwX1lBQjRiOWg2ZERmZ2k0UkhmcDNUOEVGWkNvaUVua1dua1dTRUxqTDhfbVFFTFJTMGZyTjlEMGMzM2NYZlRrdmJQaTdmS1c5QXdDOHNLdWFZNFI3WXBxSDM1T2cxbHhxQ2ZZQ1dqOXU0RHV6dmMyLVlDaS1Bd0ttVl9YXw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 07 Oct 2026 01:41:02 GMT
- [年底大選逼近，當政治人物開始用 AI「借你的嘴說話」 - TechNews 科技新報](https://news.google.com/rss/articles/CBMijwFBVV95cUxOWXZUVENFd3paT2YzQUdzRGdhUGR2Qmk5LTVtd01VNHd3VWl4QkQwSXU3RUpCZUUtakFrM3BmRVVCa0RENHU1TDlFMEhkZEZxR1Jwa0FhRnpjNTBTN1E1S0dXM2RDUXd4RWx0TGZPWjhzdlFtaTNFOW5aS0ZzNlE1dHZLNnlUYXhTM0ktUEgyUQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 07 Oct 2026 23:31:11 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：AMD’s Valuation Is Really Starting To Ruffle Feathers on Wall Street - 24/7 Wall St.；台股愈接近5萬點愈不能亂買！分析師點名6檔低本益比股台積電合理區間曝光- 證券 - 工商時報；〈美股盤後〉四大指數收低 標普終止連四紅 殖利率攀升再掀通膨疑慮 - 鉅亨網

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AMD 超微 | 新聞直接提及 | 0.00 | +25.14% | N/A | 645.86 | 649.42 | -0.55% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | 0.00 | +3.40% | +4.23% | 2,555.00 | 2,585.00 | -1.16% | 不適用 | 86.28 | 29.96 | 514.81B TWD / 53.32% | 2026-09-01 |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +17.66% | +7.67% | 529.76 | 529.76 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AMD’s Valuation Is Really Starting To Ruffle Feathers on Wall Street - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi3wFBVV95cUxPNEg2Z2V5dXpFci1adm1icGc1T0tBOFJnREYtMVRGNTNMSzJWaklvbUNISm4zSWF2YmVITl8wbzN0YV85WEdORVpac29Obmx5NHVSZUllQno0MGJuSDNjS0tTRjhzS1NQQ0pwNlVvYU95OW9RbVZ1Uld0ejJnYUFIclZmamwxVk85TXB1RUkyZnJ2S0JJRXVkRXZ0OFBkMHVMaUQyQWVSWjJLYlpuOVNuRHdncGxfYW1xU2Q3NnFZczBtTlAwTEwtSk1Fa1d1ejhIUzdLd21xY0ZuOF85b1VF?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 07 Oct 2026 12:45:00 GMT
- [台股愈接近5萬點愈不能亂買！分析師點名6檔低本益比股台積電合理區間曝光- 證券 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1QUkpRbWFFTW1CYXlJRU9SbGFGaHRrcHlwRzJkZmJKMnhOYnZlcC1QRXZ6QWlycE5EVExCT2NqZThsQURWWU5XS3ZQZEhWRFprcTNVQjFqTjAxVFhNdVJR?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 06 Oct 2026 07:00:00 GMT
- [〈美股盤後〉四大指數收低 標普終止連四紅 殖利率攀升再掀通膨疑慮 - 鉅亨網](https://news.google.com/rss/articles/CBMiT0FVX3lxTFBrcFYxcXFjUXd4azBGOUhtcjVBTUNWWi10ZUx3SEtLdmtnb0J6QWN5SjA4RXUxdmFaX3JRckQxckFsRk9WWV9kOWNER181UVE?oc=5) - Google News source discovery | 鉅亨網 Wed, 07 Oct 2026 21:50:00 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：康普攜手國際大廠打入先進製程半導體供應鏈- 產業 - 工商時報；台股憑完整 AI 供應鏈穩坐今年全球投資熱點，狠甩韓股幾條街 - TechNews 科技新報；Levi Strauss hikes profit guidance after tariff refunds, but its sales outlook is less optimistic - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +7.89% | +20.74% | 336.67 | 336.67 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | +0.40% | +0.20% | 250.00 | 289.00 | -13.49% | 不適用 | 15.21 | 16.61 | 1158.63B TWD / 38.42% | 2026-10-01 |

關聯理由（前 3）：
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 1 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 1 篇新聞出現相關標籤。

### 主要來源

- [康普攜手國際大廠打入先進製程半導體供應鏈- 產業 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBSZGRQNVBfRHFSYVlPWEdlT3RFNWVKVFFWaEtZRGFQN1JvRjNyYlhvMW5tMDZkQ011R0dIU01wVHJVcW11YlpQUFRZWFdkRVNDeTlZTVoxb3VtcTQ4UnFn?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 06 Oct 2026 07:53:00 GMT
- [台股憑完整 AI 供應鏈穩坐今年全球投資熱點，狠甩韓股幾條街 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiogFBVV95cUxOZV9JVjZQY1hyRDFUc050M0g2SlhPVnFOa19oYTdXS3VITTFMLW1lSWxHYlczU3hHY0NvVGlqemRkZHRFUC1YUWEwSVNabWhPOVprYlFBblBvbkVfWDNBZVhrd1ppX0dXU0d2aDA3aGEzTnozR2pwX1ZLVHFWRnNvT0M5Z1N6N1UtQjh1bGV1S0tZQVdJWHdKUXVRNFNjVmhxSmc?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 08 Oct 2026 00:11:28 GMT
- [Levi Strauss hikes profit guidance after tariff refunds, but its sales outlook is less optimistic - CNBC](https://news.google.com/rss/articles/CBMie0FVX3lxTE5NVGt5THJuMXkwR0Nsc1kyTnowRVJxaTJDRE9HTHVrZnNaWFNDWWxua2I0LW5ONElGN2JYWEJCZHB4S2UyODU2V1hLU1l1d2h3V2FERngxUHltU21CR044aVdleDVXQXo1a3lZUlctYUFoakRrbEI1d1Jwd9IBgAFBVV95cUxQYmh0c3dNWkNsMUNOVmVuZ0dYMGNvTTVuR0xLeUd1VzN2NDFwWU9scHl1b3pVdGI5OFFETnJDbHRPQ1Nxel9jRGh6QXh2SklwMW9CR283NWxTWTRKQmI1blFSSFh5cGVBS24zT1NiNU1taENPM20zcG5jOEN5S2VocQ?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 07 Oct 2026 20:13:01 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：昇恒昌桃園機場辦晶圓展回顧台灣半導體發展史展產業能量| 生活 - 中央社 CNA；大馬拚半導體產業升級累計培訓逾2萬名高科技人才| 國際 - 中央社 CNA；Microsoft to sell $2,599 Surface Laptop Ultra containing Nvidia AI chip - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.46 | +7.56% | +18.68% | 237.47 | 239.24 | -0.74% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 新聞直接提及 | +0.42 | +17.66% | +7.67% | 529.76 | 529.76 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 產業/供應鏈推估 | +0.04 | -1.36% | N/A | 113.12 | 114.68 | -1.36% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.04 | +3.40% | +4.23% | 2,555.00 | 2,585.00 | -1.16% | 同向 | 86.28 | 29.96 | 514.81B TWD / 53.32% | 2026-09-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.02 | -8.05% | -3.88% | 148.50 | 164.50 | -9.73% | 背離 | 6.68 | 22.33 | 25.35B TWD / 27.22% | 2026-10-01 |
| AMD 超微 | 產業/供應鏈推估 | +0.03 | +25.14% | N/A | 645.86 | 649.42 | -0.55% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | +0.03 | +12.05% | N/A | 1,088.00 | 1,088.00 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.01 | -7.12% | -4.01% | 1,660.46 | 2,335.00 | -28.89% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MSFT：新聞直接提及「Microsoft」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 CPU, server CPU, x86, foundry；其中 1 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [昇恒昌桃園機場辦晶圓展回顧台灣半導體發展史展產業能量| 生活 - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9lQ2VKMThnRWF0RTNGcl84MHRac21uTGYzeHpQMkRDN3FFU1Y0YmNaeDV4RElYNE9vcHM3Vko0aFpsNVFJQ2s4VnRuekF2ZU5PUXBLaUc3bEpBZS1EYV9v?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 07 Oct 2026 11:06:00 GMT
- [大馬拚半導體產業升級累計培訓逾2萬名高科技人才| 國際 - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1xUkJteWpFenNWa2IyM29Sbm10bjZwbTYyaFNyaERLZEFtaGF2ZWpQUk1lbHdJbGRrWE1UeWJ4NXk3V0RxTFkteWdOQzVYYXY1UlhCUndHZ2I5XzFYWUdR?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 07 Oct 2026 08:33:00 GMT
- [Microsoft to sell $2,599 Surface Laptop Ultra containing Nvidia AI chip - CNBC](https://news.google.com/rss/articles/CBMiogFBVV95cUxPb3RwVEx5UDFWcFpvRFBFR2hFR3pUUjRuOVE2MUNQVElscTdfNlZZZzNOQzZIRndNcUNKZzFCOVVRbXh2MklhT1NfaHlTTXdIS3Rma29DU3ZRMWtHQWlGdExBYm9oR1M3Wk1kU09LYWNNVDNTNFFBazhNWnQ3X0NOT0FhNXRWTVlHdDloek9GX1dvSFRucjB4U3kxTEpPTkhMNHfSAacBQVVfeXFMUGtjTngzVGppRjdrNnB2OElDaXhfWXRRWnRKTFFXZm04Rkx6U28tZ1loNjJMYms1VnRLZzY2d2hubmVLdGU0WWtlaHBCNGlfcXQ0VzNJVFhFS0NRMzdJdXJwc2Y3Z1RHMlNpLXJPTUEyTTFRVUt1UWJfc3dtdXFyaGpSMlY4bnpLSWdXLTBRaERvN1BPamJhdUd5c1ZpRlFXS21fSEZYZTg?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 07 Oct 2026 18:30:52 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：國票證券：台股多方結構相當堅挺- 新聞 - MoneyDJ理財網；《台股盤後》收跌16點、日K翻黑，5日線有守- 新聞 - MoneyDJ理財網；個股動態報導內容-28F937D6-1C53-4755-BBA1-66D5F2914C8E - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [國票證券：台股多方結構相當堅挺- 新聞 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikgFBVV95cUxOdmxvbTFWOTBURE1FZHVvUW83M0ZwSWpZTXd0VVRLVmI2TnlQVGo3OWdVaHZjUlgyMVEyX3dETmJUNkY3UmN5OHgzMDJfUldxNnJVZ0czanAwSDRLR1lZM2lxNUFRbDJVUlJidzZDeHVLR3Z5OE1aZm1qR0xLNkxkR1FvTU5ISEFvY1VaMDd6ekhuUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 08 Oct 2026 00:48:00 GMT
- [《台股盤後》收跌16點、日K翻黑，5日線有守- 新聞 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikgFBVV95cUxOSkxBdVdaaTVQWURULTF5SlFqcUk2amN5VllRMmlrWkdGVVVibTlFTDYwNmVXVEpteGJrREhmODlqbWFZeDJBOGNueW9GcEpCX1JzOTlXUmNhTTZZMm1Jc0xhRmFYTzRFOFZFRHFnbERuV2Fvb0Fjb0FYUmxKZDlHVXMwRTI2UjZsUmY1TExfZVNsZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 07 Oct 2026 07:50:00 GMT
- [個股動態報導內容-28F937D6-1C53-4755-BBA1-66D5F2914C8E - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilAFBVV95cUxQNVZkREZsZFZORVNEaUVlOVNIWVJVNUlUZWRhWUpSVVNHUTdPYVpfNFR0VmNQWEtxU3RzNkFQWVc1dUJ3bzd1M1Y0eU9RZFhKamtKVFJWSE16cXRrQzhVLUI5eVVqV2Z4LTNiZUw3SE9SZWE5em53M1ozaEhjX1RqZVBlb2twVVEtcW12VGQ3d2RrX25C?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 07 Oct 2026 18:18:38 GMT

## 新興題材：BigGo

摘要：新興題材：BigGo 相關新聞集中在：Chip Stocks Pause as Rising Yields and Oil Prices Weigh on AI Rally - BigGo Finance

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [Chip Stocks Pause as Rising Yields and Oil Prices Weigh on AI Rally - BigGo Finance](https://news.google.com/rss/articles/CBMidkFVX3lxTE9tbnNuLURQdVNPZExuSFh5al9HTWl6YU5XN0g0SG9FQXNJWGRPclVQRHVsSThwTVBESjlwWkpBVGVSOFE5bEhEakhMRlpJV3JRQVJtdGo1TEFMLXY3c19uOFR5TlRSU2FxNEktei1xa1NJaGd6d2c?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 07 Oct 2026 18:36:00 GMT

## 新興題材：B7810D00

摘要：新興題材：B7810D00 相關新聞集中在：個股動態報導內容-B7810D00-961F-46FF-B4FD-487E5585798B - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-B7810D00-961F-46FF-B4FD-487E5585798B - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilAFBVV95cUxPYXg4SjQtendzdE1WeERhaHVxaVNmRUpPcmN0VE1aUW1JWWl5S2JibFA3UGpjVzZwYjdxOUtra2VhREdOTzNUWkl1c0FlNTktXzl6OHU5M1huV3lZbm9Ycm1LeWlkU0RESTJDWFg4NldPV3ZEZEpqRWFKd19YbE1MdzFzTTAyWU5EdzF4bVV3ZmJKQjRu?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 07 Oct 2026 12:20:59 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
