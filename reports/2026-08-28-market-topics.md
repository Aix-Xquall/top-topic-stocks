# 每日股市熱門話題分析 - 2026-08-28

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **AI 伺服器與資料中心**｜正向｜熱度 11｜市場確認 81.95｜同向 5/6
2. **散熱與液冷供應鏈**｜中性｜熱度 3｜市場確認 100.00｜同向 1/1
3. **記憶體與 HBM 供應鏈**｜正向｜熱度 7｜市場確認 55.09｜同向 1/2
4. **關稅與供應鏈轉移**｜負向｜熱度 3｜市場確認 N/A｜同向 0/0
5. **綜合市場情緒**｜負向｜熱度 44｜市場確認 0.00｜同向 0/2

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.14（樣本 16）
- 5日相關係數：0.12（樣本 16）
- 同向比例：9/16

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| AI 伺服器與資料中心 | 81.95 | 5/6 | 1 | +7.87% | +1.90% |
| 散熱與液冷供應鏈 | 100.00 | 1/1 | 0 | +13.94% | +14.24% |
| 記憶體與 HBM 供應鏈 | 55.09 | 1/2 | 0 | +6.70% | +3.50% |
| 關稅與供應鏈轉移 | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | 0.00 | 0/2 | 2 | -7.71% | -7.86% |
| 消費電子與手機 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | 33.50 | 2/5 | 2 | +1.83% | +0.02% |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-08-14 | 0.34 | 0.57 | +92.86% | 14 |
| 2026-08-15 | 0.24 | 0.30 | +68.75% | 16 |
| 2026-08-16 | 0.37 | 0.51 | +70.00% | 10 |
| 2026-08-17 | 0.49 | 0.60 | +66.67% | 12 |
| 2026-08-18 | 0.29 | 0.36 | +80.00% | 10 |
| 2026-08-19 | -0.23 | -0.33 | +30.00% | 10 |
| 2026-08-20 | -0.72 | 0.06 | +50.00% | 8 |
| 2026-08-21 | -0.48 | -0.45 | +61.54% | 13 |
| 2026-08-22 | N/A | N/A | +50.00% | 2 |
| 2026-08-24 | -0.94 | -0.77 | +60.00% | 5 |
| 2026-08-25 | 0.01 | -0.58 | +35.71% | 14 |
| 2026-08-26 | 0.08 | 0.22 | +50.00% | 16 |
| 2026-08-27 | 0.38 | 0.11 | +54.55% | 11 |
| 2026-08-28 | 0.14 | 0.12 | +56.25% | 16 |

## 歷史回測摘要

- 回測日期：2026-08-28
- 近5日 3日相關：0.06
- 近5日 5日相關：0.12
- 同向比例：+33.33%
- 權重狀態：已調整

- 方向準確度：+33.33%
- 信心排序準確度：0.06
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

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel Stock Rises 4.4% as Nvidia Forecast Revives AI-Chip Demand - TechStock²；AMD and INTC Are 2 AI Semiconductor Behemoths Ahead of NVDA in 2026 - The Globe and Mail；AI 寫程式比人快，驗證卻沒跟上：程式審查淪為形式化 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.57 | +13.94% | +14.24% | 227.98 | 227.98 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.57 | N/A | N/A | 92.09 | 114.68 | -19.70% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.53 | N/A | N/A | 476.67 | 516.10 | -7.64% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.06 | +1.47% | +1.47% | 2,420.00 | 2,425.00 | -0.21% | 同向 | 86.28 | 27.94 | 467.58B TWD / 44.69% | 2026-08-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | +28.60% | -0.32% | 505.06 | 506.69 | -0.32% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -1.64% | -10.99% | 371.54 | 446.77 | -16.84% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.04 | +2.20% | +2.54% | 621.00 | 680.00 | -8.68% | 同向 | 13.92 | 43.78 | 73.78B TWD / 43.15% | 2026-08-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.04 | +2.66% | +4.46% | 3,985.00 | 4,310.00 | -7.54% | 同向 | 60.69 | 63.83 | 48.47B TWD / 12.16% | 2026-08-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA、NVDA」，共 3 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。 方向判斷命中詞：upgrade。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel、INTC」，共 2 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：upgrade。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。 方向判斷命中詞：upgrade。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Stock Rises 4.4% as Nvidia Forecast Revives AI-Chip Demand - TechStock²](https://news.google.com/rss/articles/CBMijAFBVV95cUxNSDZXWFlocl9hUUNzM3B5dkI4R19iWDZPMloxRnlmSVdiWEEzc25SaWpoOHlsYktTQzRXS2FGd01mNlR4ZGFZZTJ0VWhJZjZfSVhxbDZXZVlON2ZFU1Z4VElkZTBDbEczT0dQc2I2OHlfMjhxa0IzOXAwUldVRFdlUXRJYkRFOW9vcmhXMg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 28 Aug 2026 05:17:05 GMT
- [AMD and INTC Are 2 AI Semiconductor Behemoths Ahead of NVDA in 2026 - The Globe and Mail](https://news.google.com/rss/articles/CBMi5wFBVV95cUxNWUtadkxRWGFmYU5IVjU2dldyQm9IdmVWYWNVZlUxN3RlN2RkR1RwaFI1bXBmMHBvOWVpVU50QXlseVpfVG1XNkJVVTN4Zjh1NVlLN1RaZm5GYU1iN0pwQTRRTkFFTTdoanljUFhzZXYtN2E3OElaamhQMWtfR2ROOFBxQWtpZTNEX0EwN05sVVBqVERmNzBnclhEMkFJSXZISDk1TXBiVDl5LVlUUGVQRlpKSmZtZzIyaS1vLU50UmZPMzc2RkZMcmZJZmozdkhEbmRxY2FqSXJpdklIVl9SRnppdkswRG8?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 27 Aug 2026 12:51:02 GMT
- [AI 寫程式比人快，驗證卻沒跟上：程式審查淪為形式化 - TechNews 科技新報](https://news.google.com/rss/articles/CBMioAFBVV95cUxNVnRzbVJmRVhnSXRMZXNITkxGMUhKdjFJZ25saHJDcDhfWVNMWmVMNWpjN1ZNSnNtSzVFTm5tbzk4WDVodFFRSG1fVnZhRFI0MjFIMmFXam5OMXcyblNkcUR6N1pIVEYzdzJUdkhlU0NBOFJyQWlOVno2cFJGUGhNbGhzYk5EcUpMcmZkTTNROElISEVpVEkzUUIxdFFId2hG?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 28 Aug 2026 00:38:18 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報；本季營收續創新高可期 法人調高奇鋐獲利預估值及目標價 - UDN；【即時新聞】最新！奇鋐受惠輝達水冷加單，Q3營收估季增15% - CMoney投資網誌

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | +16.99% | +11.89% | 3,360.00 | 3,360.00 | 0.00% | 不適用 | 75.13 | 44.52 | 18.59B TWD / 57.39% | 2026-08-01 |
| NVDA 輝達 | 新聞直接提及 | +0.42 | +13.94% | +14.24% | 227.98 | 227.98 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱、奇鋐」，共 3 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：跌停, 受惠。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 27 Aug 2026 01:04:04 GMT
- [本季營收續創新高可期 法人調高奇鋐獲利預估值及目標價 - UDN](https://news.google.com/rss/articles/CBMiUEFVX3lxTE50anhTcU9Wa2ZCZFdMNzlnVUxZanlWZU5zbFJkZkt6dFF4NXpSWWZLNDh6NjBYVXR0cDFteWZwSjdrWDdYTVgwTE1ZYzN5NzBf0gFWQVVfeXFMTXBKbkQwT3ExSG5lRFBRSHBSQXVYUFF4a1NiQUFWQTdmX1laOFMxR0FTSEFzYWNuMDJnTy1YRklJRlpKUHlEcTkxdWpKbkdCWVdNaFpqcEE?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 28 Aug 2026 05:32:28 GMT
- [【即時新聞】最新！奇鋐受惠輝達水冷加單，Q3營收估季增15% - CMoney投資網誌](https://news.google.com/rss/articles/CBMikAFBVV95cUxNenhIWFhSb2ZPX1hYMVZ1UDVlSlIxRW9CSlFPR3FOeTViSjFwLXFHc3ZIUzRNaFdlaW1ISjk1WGFOX3c2TWItZzBuU2J2WE0xSklXVVZnY3IybzM3SklrTzZ1am04bnd0Yzd2Wi1tYklTLWc4M29iWE5NZHhvZm5pemdOVDUtYlRQMndnSnh6X0U?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 27 Aug 2026 22:46:39 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits；Micron vs. Sandisk: Which AI Memory Stock Should You Own? - AOL.com；The Memory Selloff - An Institutional Audit Electric Bicycle (UlmltETmgV) - Mshale

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.48 | N/A | N/A | 935.39 | 971.00 | -3.67% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.36 | -0.55% | -7.23% | 1,484.95 | 2,335.00 | -36.40% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.43 | +13.94% | +14.24% | 227.98 | 227.98 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.36 | N/A | N/A | 476.67 | 516.10 | -7.64% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.36 | N/A | N/A | 92.09 | 114.68 | -19.70% | N/A | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron、memory」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk、SNDK」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 2 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits](https://news.google.com/rss/articles/CBMi0AFBVV95cUxOWm5KdEIwSXpyY191UEhDa1V6NVpWa01UbmpJeWRIV0ttT080TmpDNEhISW5TWkQwUzBVYzBqSHJPWXRVNVJCampoWWRlYmhKVkhIeHBJLS0wLW5Ua09GQnRORXpFcW5qTEJkcnJGcW55aU5rOFVOLUFMbjRPZEpWT3A2ZllucnM0SU9JNEdrNUwyc3V2WHAtNFk3VHl4R1F6SkZRMFpleEE2Zl9MdW4tSEpMMnFGZ2hQZURWQ3B1WDlPR1BhRjJELVN5ODJWYVR3?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 27 Aug 2026 04:20:37 GMT
- [Micron vs. Sandisk: Which AI Memory Stock Should You Own? - AOL.com](https://news.google.com/rss/articles/CBMie0FVX3lxTE5hYXF1Q2x6NF9kQmEyWGdmX2l5dEpoelpqMDB2SUMtdWhaM0dMandUaFhqN0h6cTBVU1JqMV90eUJWNnJzY2JvYTFFQzJ4cTV6UElIWFJsM20tSkxkbzN5S05qTXd5cHZSTk9zV29IYmNnSDVlSHZiWHdqYw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 26 Aug 2026 06:16:28 GMT
- [The Memory Selloff - An Institutional Audit Electric Bicycle (UlmltETmgV) - Mshale](https://news.google.com/rss/articles/CBMiYEFVX3lxTE4tSG1kVkktVzNmOXlVTm9MR3FhVEVkaTJydTMwR0s0NkQxTk1yejgwRkhTWnNlOXQteTdLTThwRVpFNHRYQ1VWWFlMUjRhMkRhLXAtTFBFSGtiVXFseWJZOQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 26 Aug 2026 03:58:43 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：SpaceX太空AI衛星提前升空！Starmind是什麼？華通、昇達科等低軌衛星供應鏈迎利多？｜股市話題 - sinotrade.com.tw；新一波半導體關稅又來，AI 伺服器、筆電與遊戲機恐納入 - TechNews 科技新報；外媒：台灣成新加坡最大貿易夥伴，AI 供應鏈成關鍵 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +19.08% | +35.51% | 314.58 | 314.58 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | +3.49% | +2.23% | 253.00 | 289.00 | -12.46% | 不適用 | 15.21 | 16.61 | 946.51B TWD / 54.19% | 2026-08-01 |

關聯理由（前 3）：
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [SpaceX太空AI衛星提前升空！Starmind是什麼？華通、昇達科等低軌衛星供應鏈迎利多？｜股市話題 - sinotrade.com.tw](https://news.google.com/rss/articles/CBMijARBVV95cUxOYnhJenBVR25ObllXRUhIU3F5c2x5Zl9ZNXdhWGgzbHdIamZFSkhWLWFSMFRpQlR5Z0lyb1Q2d3MtbmF2cGtRdEUya1RrbXlDMWRHUTVkVXN2TGpzaXpxLUtRUElzdnZKTWNTUzlnS2F4blRLNnZMNFJWcjhLWWR0SFRxOXRMakFIajhvWERNMzd3MGhFN1JQd01KR0hFell1TnUtX0pQMUtoaDBMVzdVUHAzdGdQTlRFRHdSUjhtV1BVOVZLZVc4VEFES2FRZTlnTkl4cHlOd0Frb2NUdHhUOEZ0amRuNHZkY2ZCZ3hPY0F2VkRVSmg0MVZ5OEpmS0ZiXzVsMDUzOUFOanFiS2ExbXM2clYyV0FMSXU0eFlQVEJzdmlqVzlCYVlHbGhCdGtCSTJmOENjdnJ5elBZRGVfTEthbUIza1VYMFVGbUJiUmFvSTdYeFl0eUIyY09iUURyeXdHLUVCbnF0Z2V5OENzM2FOd0N3Yk4ySGgxSV9EcEI5Wm1DX1BrM2RrMkZvMGNHMFZqSFdXWGJDbWpHb29oT2xudnRqMUxDcGl0cnNBVzk2MF91OWEwUXpIZzZhb3pGcWVWN3VoY2twZG1NWkNTcWptb3VRVFJNT1ZHWUc2eDZrblhQdFNTVlVIcUNWaEJQa2l4MWtCYlRSRkF3aksyMkk4eXhBbWpHMms4Zw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 26 Aug 2026 03:47:14 GMT
- [新一波半導體關稅又來，AI 伺服器、筆電與遊戲機恐納入 - TechNews 科技新報](https://news.google.com/rss/articles/CBMipwFBVV95cUxPbUszN0k0YU9TS3FjTjgtazlZMVA4a3JnX0RFdk04dzhibzUwNUx5U3Zmamxac01TdDBZaFpTSEpqaDd5a1h1RWJxSjFLbWFNakpBSkRELV9LSmhSWlQ3eWViaFc0ZWc4XzhqY0p3dWQ0UjhHaXk4emw2OFpUWm1UaGpWLWNwZEQ5SDFMaGdSYllmdjZEd3BnNWdKa1QzYld3MEEzeGRabw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 28 Aug 2026 00:39:38 GMT
- [外媒：台灣成新加坡最大貿易夥伴，AI 供應鏈成關鍵 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiigFBVV95cUxPZzlHWmpVOW5YVUVISHF4UFViNHI3cWFVbDl4TXhIS3lzSjJldVpkYUJzWmNmZnk3dEZsSW52WjlQY2cxT2o0c19MYUVMM3ZYeXdlRTMyUi1yaFVLejliSXhvYW9VLTZSMFhvWmY2b3B4X0dTZ1FwX1p1MHlBcTF1UnZiYUZnMExYUkE?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 28 Aug 2026 00:48:18 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股要衝了！分析師曝兩個跡象出現 優先搶的族群有這些 - 經濟日報；被動元件帶頭衝！台股收漲356點成交量破兆 單周揚1,107點、漲幅2.4% | 市場焦點 | 證券 - 經濟日報；主動台股 ETF 8月績效前十強輾壓大盤表現 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | -0.21 | +13.94% | +14.24% | 227.98 | 227.98 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | -0.21 | +1.47% | +1.47% | 2,420.00 | 2,425.00 | -0.21% | 背離 | 86.28 | 27.94 | 467.58B TWD / 44.69% | 2026-08-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。

### 主要來源

- [台股要衝了！分析師曝兩個跡象出現 優先搶的族群有這些 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1Xd1lNbUtIUnB1MVVaZ2dZVVBvVmUwUDZ0RkdqSnBRZGhuNXJ2RFpNSS0tZ0taQVJqSS12XzR3RHU5djNVSUNIaDFKMXhNRXVKbEJ0NS1hbjZhQdIBX0FVX3lxTE96bTlPbFN1UUV4NG0wS3VJWHAzRnBQTkwwSlF5b2dlZVI1Rl83b2tJM0M4U2NENTFQTmVFazFXYkFtejNjTGxmdUdLcV9ndndSZ2wwODl4SmlBOVlFc0Zv?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 27 Aug 2026 09:00:00 GMT
- [被動元件帶頭衝！台股收漲356點成交量破兆 單周揚1,107點、漲幅2.4% | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1udWVjYml0RkZvQlR6Q3NxMy10QjMxWU1DWWRWeEhmLTlDdU1kdk0xTmFuZ1laRzhGWThndjRwWXN1OFdqZFVKempyNEJDRTQwWVBrbDI3aE8ydw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 27 Aug 2026 09:00:00 GMT
- [主動台股 ETF 8月績效前十強輾壓大盤表現 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1xdEpqdUx1dmw1ZHJGNFN3b2RYV1lIb3czb0xHSVZkcHVadGhLdTl6aEk0NVJQNWUzeFNUTExsTHRkbjAzemJYaGwxZGtEaXY0b0RjWU1felNEQdIBX0FVX3lxTFBoTXlGWnUwU3ZLWC1NYmdfT0ZTNkk4bk1kRmpzV3NXWTcwMk91V1ZzMEpLbzlfNnd6UXRBVkM0ZWVTZGI2QnFMUlRvX29JSURQU24wYWtmQjRxcFlva2ZB?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 28 Aug 2026 02:22:26 GMT

## 消費電子與手機

摘要：消費電子與手機 相關新聞集中在：折疊 iPhone 尬 AI 伺服器！大立光、緯穎衝破7,000元 台股第三千金爭霸 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AAPL 蘋果 | 新聞直接提及 | 0.00 | +19.08% | +35.51% | 314.58 | 314.58 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 6669 緯穎 | 新聞直接提及 | 0.00 | +8.17% | +7.75% | 7,200.00 | 7,200.00 | 0.00% | 不適用 | 313.51 | 21.85 | 117.69B TWD / 39.23% | 2026-08-01 |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | +3.49% | +2.23% | 253.00 | 289.00 | -12.46% | 不適用 | 15.21 | 16.61 | 946.51B TWD / 54.19% | 2026-08-01 |
| 2454 聯發科 | 產業/供應鏈推估 | 0.00 | +2.66% | +4.46% | 3,985.00 | 4,310.00 | -7.54% | 不適用 | 60.69 | 63.83 | 48.47B TWD / 12.16% | 2026-08-01 |

關聯理由（前 3）：
- AAPL：新聞直接提及「iPhone」，共 1 篇新聞命中。 同時符合主題標籤：hardware, consumer electronics, smartphone。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 6669：新聞直接提及「緯穎」，共 1 篇新聞命中。
- 2317：產業/供應鏈推估：公司標籤符合「消費電子與手機」關鍵字 hardware, consumer electronics；其中 0 篇新聞出現相關標籤。

### 主要來源

- [折疊 iPhone 尬 AI 伺服器！大立光、緯穎衝破7,000元 台股第三千金爭霸 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBpMnZRZW1RQjAyYnkyU0V1TDBGb0FPSXAtd01KQmRLNHJOUXd5WVN5bnUxRTZWcFBjZW94bG9kd0s3TTlKYlR1VkhUczZyb1pIUUpzNF92OFpBd9IBX0FVX3lxTE5xX2ZTLUNmWFl5Q0ZUR0trQ01DbEZSZVJrRTVlX2ZkS2Y3ZEJYaEJPelZaTDhIcXUtc18yNWtsQ1Z0T01qVml5VVlDbHd4R0dzVm5GOXdZd1dtYWNnY0Q4?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 27 Aug 2026 09:00:00 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：INTC, AMD, AVGO: Chip Stocks Jump Premarket After Nvidia's Blowout Report - Yahoo Finance；Intel Stock Rises 4.4% as Nvidia Forecast Revives AI-Chip Demand - TechStock²；AMD and INTC Are 2 AI Semiconductor Behemoths Ahead of NVDA in 2026 - The Globe and Mail

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.57 | N/A | N/A | 92.09 | 114.68 | -19.70% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.57 | +13.94% | +14.24% | 227.98 | 227.98 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.56 | N/A | N/A | 476.67 | 516.10 | -7.64% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | +0.24 | -1.64% | -10.99% | 371.54 | 446.77 | -16.84% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.05 | +1.47% | +1.47% | 2,420.00 | 2,425.00 | -0.21% | 同向 | 86.28 | 27.94 | 467.58B TWD / 44.69% | 2026-08-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.03 | -4.05% | +2.60% | 130.00 | 164.50 | -20.97% | 背離 | 6.68 | 17.82 | 23.84B TWD / 18.98% | 2026-08-01 |
| MU 美光 | 產業/供應鏈推估 | +0.04 | N/A | N/A | 935.39 | 971.00 | -3.67% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.03 | -0.55% | -7.23% | 1,484.95 | 2,335.00 | -36.40% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC、Intel」，共 3 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA、NVDA」，共 3 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [INTC, AMD, AVGO: Chip Stocks Jump Premarket After Nvidia's Blowout Report - Yahoo Finance](https://news.google.com/rss/articles/CBMilAFBVV95cUxNX1Rwa211UlZEMjFBUjVwTDJpSG0tc2xVNnFuUVM2Z3FqdHh6V3F3dnBpQ2tvMUhGS3ctYWRQWlJoZUExQlREOTk2dGhNQktyR3VPX2RLNGZocm5JUW9NTUxoREVVemFTdURMWlhnOHNIemgxT2dVT3lDem4wX3hpbmlRNFdVVHUwcUdnX0tXSGZWN2pl?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 27 Aug 2026 09:43:17 GMT
- [Intel Stock Rises 4.4% as Nvidia Forecast Revives AI-Chip Demand - TechStock²](https://news.google.com/rss/articles/CBMijAFBVV95cUxNSDZXWFlocl9hUUNzM3B5dkI4R19iWDZPMloxRnlmSVdiWEEzc25SaWpoOHlsYktTQzRXS2FGd01mNlR4ZGFZZTJ0VWhJZjZfSVhxbDZXZVlON2ZFU1Z4VElkZTBDbEczT0dQc2I2OHlfMjhxa0IzOXAwUldVRFdlUXRJYkRFOW9vcmhXMg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 28 Aug 2026 05:17:05 GMT
- [AMD and INTC Are 2 AI Semiconductor Behemoths Ahead of NVDA in 2026 - The Globe and Mail](https://news.google.com/rss/articles/CBMi5wFBVV95cUxNWUtadkxRWGFmYU5IVjU2dldyQm9IdmVWYWNVZlUxN3RlN2RkR1RwaFI1bXBmMHBvOWVpVU50QXlseVpfVG1XNkJVVTN4Zjh1NVlLN1RaZm5GYU1iN0pwQTRRTkFFTTdoanljUFhzZXYtN2E3OElaamhQMWtfR2ROOFBxQWtpZTNEX0EwN05sVVBqVERmNzBnclhEMkFJSXZISDk1TXBiVDl5LVlUUGVQRlpKSmZtZzIyaS1vLU50UmZPMzc2RkZMcmZJZmozdkhEbmRxY2FqSXJpdklIVl9SRnppdkswRG8?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 27 Aug 2026 12:51:02 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：統一證券：台股震盪盤堅，仍有利於多方- 新聞 - MoneyDJ；國票證券：台股短線高檔格局有望延續- 新聞 - MoneyDJ；【台股操盤人筆記】把握榮景上漲機會，但也為循環轉折做準備-報告內容-基金 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [統一證券：台股震盪盤堅，仍有利於多方- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxOTTEzTFJjcEpnTHVIWkRGZl9tcVk3Wm9FbmhJZl92MWcxZl95VHFyZnRhRm5mdmZaQVBvYkt6SzltajZUMVZHOXBtQU1sdF9SdjV6SkZxaHF6UmVCclhKdGg2Z0dhRVlfdzBXbFRLN0ZtR2VUUVd1XzRsTlhWdlhPWVdUajJQdFN0ZUVLSllEVnNhZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 28 Aug 2026 00:41:00 GMT
- [國票證券：台股短線高檔格局有望延續- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPM3hzVVpXMm9zUk1sOW55WVczaC0xWkw5SlhaT1Vqdk9qMXBkQVpZdlk3RnAybXIxUmFYTUI5N2NGd1o1cF9sZHkzV25ncDZXUVFHQTZwTXhoblVhLTl4WGVCcHFFUDdKdWJqNzlldTZweEFEX3V4ZDZfejFZOUQydDMxQlhha3lQZGNzN3c1S0s3QQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 28 Aug 2026 00:41:00 GMT
- [【台股操盤人筆記】把握榮景上漲機會，但也為循環轉折做準備-報告內容-基金 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxPekh6N3dnaEg1TEJfNnRHSWRsOTMySmhsMXpMYy15ZmhaZ2trXzdLX0p1eENxNWFUOHBQQnJib3ZGcTM5WllJZ2hUNGNSRm1wQlZmMXpSUENjOVZLUjNCNXlleDUybXdfNW5rMk9ZQ0R2ZktMZ0hpaC00Y0I4T0ZRNWdvQ24zSmpLWlZOSGdjcXc?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 27 Aug 2026 08:17:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
