# 每日股市熱門話題分析 - 2026-06-08

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **AI 伺服器與資料中心**｜中性｜熱度 8｜市場確認 N/A｜同向 0/0
2. **半導體與晶片供應鏈**｜負向｜熱度 4｜市場確認 55.00｜同向 3/5
3. **記憶體與 HBM 供應鏈**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
4. **散熱與液冷供應鏈**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0
5. **綜合市場情緒**｜負向｜熱度 42｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.36（樣本 5）
- 5日相關係數：-0.68（樣本 5）
- 同向比例：3/5

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| AI 伺服器與資料中心 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | 55.00 | 3/5 | 1 | +4.33% | -3.98% |
| 記憶體與 HBM 供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：投資人拋售晶片 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：台指期一度跌停 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
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
| 2026-06-05 | 0.31 | 0.93 | +50.00% | 6 |
| 2026-06-06 | 0.12 | 0.06 | +45.45% | 11 |
| 2026-06-07 | -0.32 | -0.20 | +45.45% | 11 |
| 2026-06-08 | 0.36 | -0.68 | +60.00% | 5 |

## 歷史回測摘要

- 回測日期：2026-06-08
- 近5日 3日相關：-0.05
- 近5日 5日相關：-0.17
- 同向比例：+33.33%
- 權重狀態：已調整

- 方向準確度：+33.33%
- 信心排序準確度：-0.05
- 診斷：低相關

調整原因：近 5 日信心分數與股價關係偏低，提高價格確認，降低寬題材推估。；關鍵詞×公司後續樣本有效 4 筆，未達 30 筆，不調整樣本權重

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

摘要：AI 伺服器與資料中心 相關新聞集中在：Broadcom Sinks 14% on Soft AI Chip Outlook Despite Earnings Beat, Dragging Down AMD and Intel - AOL.com；美政府入股 AI 公司有譜？川普正面回應，本週召開會議討論 - TechNews 科技新報；AI 股漲翻天還能買誰？Barron′s：輝達等五檔仍算便宜，就算退潮也是留到最後那批 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +2.77% | +15.75% | 205.10 | 211.14 | -2.86% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 99.17 | 114.68 | -13.52% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | N/A | N/A | 466.38 | 516.10 | -9.63% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | 0.00 | -7.59% | +20.71% | 385.73 | 446.77 | -13.66% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -0.63% | +0.42% | 2,365.00 | 2,365.00 | 0.00% | 不適用 | 74.39 | 31.80 | 410.73B TWD / 17.50% | 2026-05-01 |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +6.09% | -17.77% | 416.67 | 506.69 | -17.77% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | -2.20% | -5.56% | 577.00 | 611.00 | -5.56% | 不適用 | 10.86 | 53.57 | 62.25B TWD / 19.22% | 2026-05-01 |
| 2454 聯發科 | 產業/供應鏈推估 | 0.00 | -4.97% | -0.23% | 4,300.00 | 4,310.00 | -0.23% | 不適用 | 62.91 | 68.53 | 46.74B TWD / -4.14% | 2026-05-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Broadcom Sinks 14% on Soft AI Chip Outlook Despite Earnings Beat, Dragging Down AMD and Intel - AOL.com](https://news.google.com/rss/articles/CBMieEFVX3lxTE9kWlRUalB6cmJkd3ctZVQza1J5SXNTd1MtLVRWaEJYMUlvZE41TUtFbmd0ZXVyV0d3eTg3YmJtTHVxSENTRl9YZzRGY09Jc2pNczU1ZGRxZTNJYjd4d2IxdFgydWJwSzdQR2NQN2RmbE5pNUlYQUctbg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 07 Jun 2026 16:45:04 GMT
- [美政府入股 AI 公司有譜？川普正面回應，本週召開會議討論 - TechNews 科技新報](https://news.google.com/rss/articles/CBMinwFBVV95cUxQV1Y5MGlua1BocUtlVGNJMGxhZXNGdmFrZWRMeGJ5eWx3d0JxbWo1Vk5EQXhIcWljZEFPZnUxNU9lQy01U2hYQXBVemNleU1EM1VFaTNBV0FvV01RZ2p1cy1fLUtYVk1MU2l1aU5yQm5vNUVDdy1ZY0h6QllCaGhTckN1MWw5QnBfQW1Rek93dlRfa2JvaXZwanVxZWExSmc?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 07 Jun 2026 08:53:42 GMT
- [AI 股漲翻天還能買誰？Barron′s：輝達等五檔仍算便宜，就算退潮也是留到最後那批 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiqAFBVV95cUxQTVQwSVFidlVrcG5faGtIaTZFbE5WOW1fN0tLME82VXZybzhmNkpuQmRFaUctTFZidS1IX09GOWMxN29UTTZ1SUJHLWhJZm95MWZUa2RfalZrVGJYQ0hfaHIydmpGUHFhNHlscEdYazhISnF5aWU1T2FMSGl1TnJiTzRmS01kSktWVmk1YlhmU0ZsR19VMjlkX0tVcWt2VXdONDlmUEpQZjM?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 07 Jun 2026 02:11:37 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Broadcom Sinks 14% on Soft AI Chip Outlook Despite Earnings Beat, Dragging Down AMD and Intel - AOL.com；What Triggered the Recent Semiconductor Sell-Off - Kavout；Wall Street's 'fear gauge' punches back as the 'crash up' in chip stocks finally reverses - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.67 | N/A | N/A | 99.17 | 114.68 | -13.52% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.61 | N/A | N/A | 466.38 | 516.10 | -9.63% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | -0.61 | -7.59% | +20.71% | 385.73 | 446.77 | -13.66% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.04 | -0.63% | +0.42% | 2,365.00 | 2,365.00 | 0.00% | 未明確 | 74.39 | 31.80 | 410.73B TWD / 17.50% | 2026-05-01 |
| 2303 聯電 | 產業/供應鏈推估 | -0.05 | -7.07% | -9.00% | 131.50 | 144.50 | -9.00% | 同向 | 4.00 | 33.04 | 22.94B TWD / 17.78% | 2026-06-01 |
| NVDA 輝達 | 產業/供應鏈推估 | -0.02 | +2.77% | +15.75% | 205.10 | 211.14 | -2.86% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | -0.04 | N/A | N/A | 864.01 | 971.00 | -11.02% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | -0.04 | -9.15% | -8.00% | 1,559.32 | 1,831.50 | -14.86% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AVGO：新聞直接提及「Broadcom」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Broadcom Sinks 14% on Soft AI Chip Outlook Despite Earnings Beat, Dragging Down AMD and Intel - AOL.com](https://news.google.com/rss/articles/CBMieEFVX3lxTE9kWlRUalB6cmJkd3ctZVQza1J5SXNTd1MtLVRWaEJYMUlvZE41TUtFbmd0ZXVyV0d3eTg3YmJtTHVxSENTRl9YZzRGY09Jc2pNczU1ZGRxZTNJYjd4d2IxdFgydWJwSzdQR2NQN2RmbE5pNUlYQUctbg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 07 Jun 2026 16:45:04 GMT
- [What Triggered the Recent Semiconductor Sell-Off - Kavout](https://news.google.com/rss/articles/CBMiiwFBVV95cUxQeV9hbWl4LXg0eW5ZWFVERlpaZGRsZzBkOEQzb0VuSmptQ2RsR3RUcldSTzhJcW1URGZsbnBjVUxmYlNpMHlESnlJdEVvZ1RaSWloQ0ZfODJXV012UF9qYjFfYVNDaG15cXpBNXYxYWpjaGNIY2hRa3hOdGhUSjdOcDhabENFWmFvV1M0?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 06 Jun 2026 06:30:11 GMT
- [Wall Street's 'fear gauge' punches back as the 'crash up' in chip stocks finally reverses - CNBC](https://news.google.com/rss/articles/CBMivgFBVV95cUxQenFydEpMYUgwS3hiZTBTWjZuZ3dhS2YzNVAwa1RlM0lEbDFWYktubzBzN1BuM0lzZ0dhdXhIWUVZNE44cjNlVS05VHpFRVQxekI3WE84Z21kcG9jRDNvczl0bkFMNVFiQ2M3Tks1bXZhenNCM3JkaGo4R21sbHE5ZUF6c01oSzhQcmJWcGpJOEw1bkVFNW1oYmEyR0NjQUZwYTVaNlVqNXJHYWNvbXB2NUw2QTI2SWZpMnBkZFd30gHDAUFVX3lxTE42VTBsRDUyMnBoQWhkMWJRcERlQzFzeWY0aWhYUW1rVTQ2WmhVdjJ0WDlEWWtZSElfcU1iUTBOR1diVHhKRGlDd1B2MmVrWmtDREZWLUJvQ084anEtTUE5c0FqanJ0S1NUcFVPbDFLanlER2tDVU5Xel9iT01MQlVFTTZiUHNkRS1vbGZuaGQwNWVuX2xIYmpKcGhMYnRuMElQcWJCRS1lUzlaSnVjQUlYcGE5dWYzTUl5REF3N2hkR21uNA?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 06 Jun 2026 12:58:29 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Opinion: The Best Memory Stock to Buy Isn’t Named Micron or SanDisk - AOL.com；SanDisk (SNDK) Is Doing Something Unprecedented In The Al Sector! SNDK STOCK PODCAST ANALYSIS BUY Jobe Bellingham (gRMiCAoJ7a) - Mshale

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| SNDK SanDisk | 新聞直接提及 | 0.00 | -9.15% | -8.00% | 1,559.32 | 1,831.50 | -14.86% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 864.01 | 971.00 | -11.02% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +2.77% | +15.75% | 205.10 | 211.14 | -2.86% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- SNDK：新聞直接提及「SanDisk、SNDK」，共 2 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- MU：新聞直接提及「Micron」，共 1 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Opinion: The Best Memory Stock to Buy Isn’t Named Micron or SanDisk - AOL.com](https://news.google.com/rss/articles/CBMifkFVX3lxTE5DWkE5bWJ1czRLN1V0X1lnUzlQQUFLSENQcGd6ZlN6WGpYblZFNEJwdl9SUjBiS1hNUHpvMXNMNUhpazEzREdVa2owWmJuZkxrZGFhbFFVNWtGWTRiamZDZ2s5U0JJd2E5bzBQYU9rOHZHMHBKLVB2NENTc2QwQQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 06 Jun 2026 10:35:52 GMT
- [SanDisk (SNDK) Is Doing Something Unprecedented In The Al Sector! SNDK STOCK PODCAST ANALYSIS BUY Jobe Bellingham (gRMiCAoJ7a) - Mshale](https://news.google.com/rss/articles/CBMiW0FVX3lxTE82c25ZNkhMbnBFcHlYZktjT2gzRlFzREd4ZFlubTJYeG4zZFJ6NU1OdGxaX3BRYWM0bFdDWk5tMlNVS3BvWXRLZW1jUVp3SUdNYXlKam5zNEhNVm8?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 06 Jun 2026 17:27:45 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：〈財經週報-台股熱點〉從AI到外太空 散熱族群題材不斷 - 自由時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | -3.70% | -2.44% | 2,600.00 | 2,835.00 | -8.29% | 不適用 | 61.06 | 42.72 | 15.63B TWD / 71.62% | 2026-05-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 1 篇新聞命中。 同時符合主題標籤：thermal。

### 主要來源

- [〈財經週報-台股熱點〉從AI到外太空 散熱族群題材不斷 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTE9rc0xOT3JaSGZPbV9uNjZUNmJLdkctMThER29ldnFaMXp1YlBQajNxaVBBcHlrVEFOOUNLZkxISUt1ZVFOMHF4WXBSd1Jtc0plYWh5bDRrdVk?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 06 Jun 2026 02:07:21 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：產業評析-法人資金大挪移 金融股變飆股 富邦金破百 - MoneyDJ理財網；最新專欄分析 - MoneyDJ理財網；首頁 ETF介紹 ETF全部持股 個股技術分析 - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [產業評析-法人資金大挪移 金融股變飆股 富邦金破百 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMijgFBVV95cUxPOTBKcjBScDZiM2xTNXFrMGY1WDhYU1FqOHhhMi15bW0wTGpXR1o5RXNLUDVhLVpVbWphNGRmQV9XT0k5MkVxWFphQlFyb0hoQXhSNFBOdDdWZ0F0ZTBpMlRCTjNkUDFnQi1yNnJwQkN2cE5MN0Z0NGhZZ0xFR2V0YUFPT2xoLUZIam9OcWFR?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 07 Jun 2026 19:07:30 GMT
- [最新專欄分析 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMifkFVX3lxTE04Vk04X2I0YzhPYXc4eDdpRl9PcEdNcGFiNVhQZlU2eVgyYzE0TkNOcV90MkVYV3dVOGg1SUxQWF9SOGFESXRtMXg0LU1VVTZqUWtlV3Y5N2d4YlFEMzhPYm1nQkVxdHhKd2hRUzBrRmFfdVoyd1hiS24yVlRBZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 06 Jun 2026 13:53:54 GMT
- [首頁 ETF介紹 ETF全部持股 個股技術分析 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMiekFVX3lxTFBRYU1SR0RxTVk1ejBZOUN4YmlZVUVoaWVzOFNPTzFYSUI2Rl9weTBrZHRHd2twRlRRaWtMS2MtZkJHNlNZSXFySW9xcHRxX3V1eXFPSlN0SzVqOWF1NkMtdTcwZGVRTk1INGkzdkMwQVZYdzgxc3B6T1h3?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 06 Jun 2026 15:39:31 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：20260605台股融資維持率 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [20260605台股融資維持率 - MoneyDJ](https://news.google.com/rss/articles/CBMisgFBVV95cUxNdmN4SmhIdGV1VkptQVdhQkY2TmR0TzNEM3Z6R0xGMjdiRDdpYUo3MktYeUlGT1YzbUF6bldpVmlRWkI5SnA1Y0V4LTNOM2VmLTdzaGNJRmJQMlQ0dWNsY0xaRzY5ZUQ4R0hlWGFMV2M3Qm1aeUxNQjBrcHRrZi1kazZrVlU1cm4yRHlLdjBTZ3dCTGxUZ0xWeXM1cjNfOTF0ZDU1bmpmbS1hWjJNT1lQVzZn0gG3AUFVX3lxTFBCaWh4TzU0QlhLX2R3MV9qbkNiZXJfa25TX0p1M25SVnBtT1RXcmhIM24taFYxSDNZaXVmSk83ZkljNkZjdjg2cTd1ZnhseXVsY1Z1U3FxenJ1ZC1tdURNSEpFVlMzRjIxbWZJWkpnYXdTd3Q5dUdjLXRua0VUVEdzS0xHNzU3MUFFcTZaTDNGWms1T2w2Tkg1R0REYlV0NmJUbnpTd3JidjRQM2VLcGxVa2QtNFoyVQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 07 Jun 2026 07:13:57 GMT

## 新興題材：投資人拋售晶片

摘要：新興題材：投資人拋售晶片 相關新聞集中在：投資人拋售晶片股美半導體業者股價大跌| 產經 - 中央社 CNA

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [投資人拋售晶片股美半導體業者股價大跌| 產經 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE9qUmo1Slo4RVNkVkJrTG1xR1pORURnLVdUSzVDdjZNY3NSN3dHdlAySjF2WUFwcW8xVTVqbnVqVG90UEprN2lIY1FCMmZfU2Jmd2E1aFNTSVJBcXp0WGc?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 06 Jun 2026 00:15:00 GMT

## 新興題材：台指期一度跌停

摘要：新興題材：台指期一度跌停 相關新聞集中在：台指期一度跌停、台股周一恐跌數千點？四貸同堂挫著等？公股銀最新預測曝光- 證券 - 工商時報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台指期一度跌停、台股周一恐跌數千點？四貸同堂挫著等？公股銀最新預測曝光- 證券 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBoMEpHYTZLZnlEczdaR1RwXzIwX2UtYVBoQ01xQlhCdTYxQTY2cVh5OGVhanlad1dhTm1uZVExN01sSXJPaUs0dXlvY0hNZU1LQUpJckFuWUJoUUJKY0Zv?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 06 Jun 2026 06:30:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
