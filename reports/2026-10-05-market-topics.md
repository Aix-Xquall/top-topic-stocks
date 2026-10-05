# 每日股市熱門話題分析 - 2026-10-05

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **AI 伺服器與資料中心**｜正向｜熱度 13｜市場確認 70.99｜同向 6/8
2. **記憶體與 HBM 供應鏈**｜正向｜熱度 6｜市場確認 50.21｜同向 1/2
3. **散熱與液冷供應鏈**｜正向｜熱度 3｜市場確認 80.72｜同向 2/2
4. **新興題材：TradingKey**｜正向｜熱度 3｜市場確認 60.86｜同向 2/3
5. **半導體與晶片供應鏈**｜中性｜熱度 8｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.16（樣本 15）
- 5日相關係數：0.29（樣本 10）
- 同向比例：11/15

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| AI 伺服器與資料中心 | 70.99 | 6/8 | 1 | +6.16% | +2.41% |
| 記憶體與 HBM 供應鏈 | 50.21 | 1/2 | 0 | +5.07% | -3.25% |
| 散熱與液冷供應鏈 | 80.72 | 2/2 | 0 | +3.58% | +8.03% |
| 新興題材：TradingKey | 60.86 | 2/3 | 0 | +4.73% | -3.25% |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 先進封裝與 CoPoS | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：台股重量級法說 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價呈負相關；應檢查正負向詞庫，並降低新聞直接提及但股價背離的權重。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-09-22 | -0.00 | -0.01 | +88.24% | 17 |
| 2026-09-23 | 0.35 | 0.22 | +80.95% | 21 |
| 2026-09-24 | 0.05 | 0.42 | +90.00% | 10 |
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

## 歷史回測摘要

- 回測日期：2026-10-05
- 近5日 3日相關：0.03
- 近5日 5日相關：-0.14
- 同向比例：+54.17%
- 權重狀態：未調整

- 方向準確度：+54.17%
- 信心排序準確度：0.03
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

摘要：AI 伺服器與資料中心 相關新聞集中在：Not Intel. Not Nvidia. The $2.4 Trillion Chipmaker That Wall Street Calls the Ultimate AI "Picks-and-Shovels" Play - The Motley Fool；The AI Chip Revolution Wouldn’t Be Possible Without This Company - 24/7 Wall St.；250 萬人下載 Muse 暴紅背後：AI 代理人暴增，真贏家是資安 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.54 | +5.97% | +16.92% | 233.95 | 233.95 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.54 | +4.05% | N/A | 119.33 | 119.33 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.06 | +22.83% | N/A | 633.91 | 633.91 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.06 | +1.01% | 0.00% | 2,500.00 | 2,500.00 | 0.00% | 同向 | 86.28 | 28.98 | 514.81B TWD / 53.32% | 2026-09-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | +14.95% | +5.19% | 517.53 | 517.53 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -4.10% | -5.99% | 355.14 | 446.77 | -20.51% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.04 | +3.78% | +2.89% | 713.00 | 713.00 | 0.00% | 同向 | 13.92 | 51.59 | 82.25B TWD / 45.66% | 2026-09-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.03 | +0.81% | -4.53% | 4,950.00 | 4,950.00 | 0.00% | 未明確 | 60.69 | 81.75 | 64.18B TWD / 44.08% | 2026-09-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Not Intel. Not Nvidia. The $2.4 Trillion Chipmaker That Wall Street Calls the Ultimate AI "Picks-and-Shovels" Play - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxOWHphWDQ3ZDJDSTZXb090R00xMGg2b1YwcUtDUmF0bnh6T1R6RHc2aDB4OUR3LUZOM291MUVGMHBJbGRJSzJxbElfVkN2RlJseXo5dG16SXk4aUlNekw5Vl83WmhrQnZsVlExSEMxeGxIaTJpbHFoZW40bndjRTNEX2VfRTBTc1R6bGFXQjRtMXFXM2d1UmxSOQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 04 Oct 2026 09:00:00 GMT
- [The AI Chip Revolution Wouldn’t Be Possible Without This Company - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiqwFBVV95cUxQczRsRVU3dGhZN2JwdEJWOUtTMkZ4djRzVEh5cFVyeWk2OHN0X052RmRwYmJoUnAtVklaNTVJRkRJZzF2Rk9Zem5zbFV4aTdrREhWWnpNT05xN2VnZU1xenBjYlNNZjZFUWZZWmRtTTJmcGxPZUV3a0RzeW8xVkw3OUkxbnhUbTdHU1FSVHdHbmY5TjRYZ3B0SFNoU05yX3BhSGMyRWFRZW1HRUk?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 03 Oct 2026 15:30:00 GMT
- [250 萬人下載 Muse 暴紅背後：AI 代理人暴增，真贏家是資安 - TechNews 科技新報](https://news.google.com/rss/articles/CBMibkFVX3lxTE9lamZiV21EMU9oRGVBS3VmMU9pVVZ2dmxmZlJSQm1KWlhDUENyN1FUSVN2dnIwSmlUekhiandCVEhRQzhJNTdQV2VZQURxVmN4MGs3U25tV2U2OEhTWC1ieE93OEVVRlV2RUVzTVlR?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 05 Oct 2026 00:11:15 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Micron or Sandisk: If I Could Only Own One for the Next 5 Years, It Would Be This One - The Motley Fool；Micron vs. SanDisk: As AI Data Center Boom Continues to Heat Up, Which Memory Stock Is a Better Buy? - TradingKey；Sandisk (SNDK) Weekend Outlook: Can the S&P 500's Best Stock Extend Its 857% Rally? - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.57 | +10.70% | N/A | 1,074.89 | 1,074.89 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.43 | -0.56% | -3.25% | 1,719.99 | 2,335.00 | -26.34% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +5.97% | +16.92% | 233.95 | 233.95 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、美光」，共 4 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：大增。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk、SNDK」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Micron or Sandisk: If I Could Only Own One for the Next 5 Years, It Would Be This One - The Motley Fool](https://news.google.com/rss/articles/CBMilwFBVV95cUxPbmgzT0VqTE9aa1plT0RnRXpyclJjSEFCNGptcFlrcU41VTNadVp0SVlUeGZLSUVrZGozWEhxd2Q1bHZoN29IcE9sV25kd19MZTlUVEo1bHFfakpURmdmaG9KeXhKRXJVSDVYams0alpsdlJpMS13c3ItZ3NFUUkwQ3FFOEMwM2V3N1RSTFlrOEdFYmVDM0pF?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 04 Oct 2026 13:56:00 GMT
- [Micron vs. SanDisk: As AI Data Center Boom Continues to Heat Up, Which Memory Stock Is a Better Buy? - TradingKey](https://news.google.com/rss/articles/CBMiwgFBVV95cUxNb2l6VlJubm1teWI3RlFGWm9fZ0g0dDJFVWhtMUJaaHkySzF4NnQxMW5ScllzSGNlMFR2dUZPYUhFeUNVVndpNU82c2dRVTB2S1BoRTVwV1pIekRJWENUNFBYbDVQVjV5Yk9GYUhxdTNuVkNUVXNtREZ4ck5mN0laTlBUbDlUQkxhSjhNMTFNcE5TWjdVWkIwekZKTXI2d3ExUU1XZnFraF9ncWlnQnJfeDJxZzJnRGhUQXhrVFJzdzUwdw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 05 Oct 2026 00:05:52 GMT
- [Sandisk (SNDK) Weekend Outlook: Can the S&P 500's Best Stock Extend Its 857% Rally? - TradingKey](https://news.google.com/rss/articles/CBMi1AFBVV95cUxPUGktaU50QjhYb3FKOGNVdU1BRlRsYlRJWHRWbkVsTTJvQl9ScHFFMGV1T3JjTndZSm51NDc0a0dxVnJEbzNNXzBzaXNkT1dSUUdIWmhCRDVVRm5CdUVyREdsMXNYZUlXN1k5NkFsdmtON2Jzbm8tVVl4ckFjWHplSUxibmRZRHh0SFN4bUdoQzZuV0h6Tk9qTlJXVEhWczREUktmQkZiMHB3XzN3eG5lbDFfb3JxMFNMbDdkaVVSZUFMQ2dkQzJJUW1FM0VsQzVTVXA2SQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 04 Oct 2026 06:08:02 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：CDU認證落榜、Rubin Ultra規格傳變？法人卻反手上修這家散熱廠業績及目標價- 證券 - ctee.com.tw；〈財經週報-台股熱點〉從AI到外太空 散熱族群題材不斷 - 自由時報；輝達、Google、AWS齊助攻！這「散熱股」水冷板訂單滿手 今年估賺逾10個股本 - FTNN

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.57 | +1.18% | -0.86% | 3,440.00 | 3,440.00 | 0.00% | 同向 | 75.13 | 45.85 | 19.48B TWD / 54.34% | 2026-09-01 |
| NVDA 輝達 | 新聞直接提及 | +0.42 | +5.97% | +16.92% | 233.95 | 233.95 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 3 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：上修。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [CDU認證落榜、Rubin Ultra規格傳變？法人卻反手上修這家散熱廠業績及目標價- 證券 - ctee.com.tw](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5jQ2hwTUdkTm9wU1JrQ0RiUEhMOGVjZXlyM1RxVGVqM2pRazBhLU1CLUNiTHZZYjZNeW9takZzTFVOZ3R4TC1LTkM2M3NfSG9UUWZneHNGcUZ4R09KUkFF?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 04 Oct 2026 01:25:00 GMT
- [〈財經週報-台股熱點〉從AI到外太空 散熱族群題材不斷 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTE9rc0xOT3JaSGZPbV9uNjZUNmJLdkctMThER29ldnFaMXp1YlBQajNxaVBBcHlrVEFOOUNLZkxISUt1ZVFOMHF4WXBSd1Jtc0plYWh5bDRrdVk?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 04 Oct 2026 12:32:32 GMT
- [輝達、Google、AWS齊助攻！這「散熱股」水冷板訂單滿手 今年估賺逾10個股本 - FTNN](https://news.google.com/rss/articles/CBMiS0FVX3lxTE00UmNaTUJTZGttSkcyY0lOYTJ5TlpQT1FQMDloUXZSaHZTZXpESU1Ua0s3ckVWOHk5LWFWU2stc3dUc19WUWszYVlpZw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 04 Oct 2026 15:50:00 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Why Is Intel (INTC) Stock Volatile After Earnings? Revenue Beat Overshadowed by $11 Billion Loss - TradingKey；Micron vs. SanDisk: As AI Data Center Boom Continues to Heat Up, Which Memory Stock Is a Better Buy? - TradingKey；Sandisk (SNDK) Weekend Outlook: Can the S&P 500's Best Stock Extend Its 857% Rally? - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| SNDK SanDisk | 新聞直接提及 | +0.37 | -0.56% | -3.25% | 1,719.99 | 2,335.00 | -26.34% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.42 | +4.05% | N/A | 119.33 | 119.33 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 新聞直接提及 | +0.42 | +10.70% | N/A | 1,074.89 | 1,074.89 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- SNDK：新聞直接提及「SanDisk、SNDK」，共 2 篇新聞命中。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MU：新聞直接提及「Micron」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Why Is Intel (INTC) Stock Volatile After Earnings? Revenue Beat Overshadowed by $11 Billion Loss - TradingKey](https://news.google.com/rss/articles/CBMiyAFBVV95cUxPdGVhdUdOWHYwd0I2OHRLRjlFVE9KTkNud09aOHhCOTZGY2NDZVM4VjFnTTZKdkpKdlBORHo1OG5RWENLVFg4VUZoYVdVWVRpaWFCSWtxY2dHX280ZFFsaDlvSldKQm9NdTdWTjlueks4V3V3RUVJQ2pqYVFtNi0xVU9zY2V3MGdONjRFaHJqU1RRaVZZMm9GZndlNVRSaWpveDlMWG41WG5qUk52T0tRcGl1bklGZ2twMmQyQnJxdkM0YzU1d1J2Wg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 03 Oct 2026 11:52:09 GMT
- [Micron vs. SanDisk: As AI Data Center Boom Continues to Heat Up, Which Memory Stock Is a Better Buy? - TradingKey](https://news.google.com/rss/articles/CBMiwgFBVV95cUxNb2l6VlJubm1teWI3RlFGWm9fZ0g0dDJFVWhtMUJaaHkySzF4NnQxMW5ScllzSGNlMFR2dUZPYUhFeUNVVndpNU82c2dRVTB2S1BoRTVwV1pIekRJWENUNFBYbDVQVjV5Yk9GYUhxdTNuVkNUVXNtREZ4ck5mN0laTlBUbDlUQkxhSjhNMTFNcE5TWjdVWkIwekZKTXI2d3ExUU1XZnFraF9ncWlnQnJfeDJxZzJnRGhUQXhrVFJzdzUwdw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 05 Oct 2026 00:05:52 GMT
- [Sandisk (SNDK) Weekend Outlook: Can the S&P 500's Best Stock Extend Its 857% Rally? - TradingKey](https://news.google.com/rss/articles/CBMi1AFBVV95cUxPUGktaU50QjhYb3FKOGNVdU1BRlRsYlRJWHRWbkVsTTJvQl9ScHFFMGV1T3JjTndZSm51NDc0a0dxVnJEbzNNXzBzaXNkT1dSUUdIWmhCRDVVRm5CdUVyREdsMXNYZUlXN1k5NkFsdmtON2Jzbm8tVVl4ckFjWHplSUxibmRZRHh0SFN4bUdoQzZuV0h6Tk9qTlJXVEhWczREUktmQkZiMHB3XzN3eG5lbDFfb3JxMFNMbDdkaVVSZUFMQ2dkQzJJUW1FM0VsQzVTVXA2SQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 04 Oct 2026 06:08:02 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel, AMD Slide 4.2% as Nvidia Unveils N1X PC Chip [2026] - tech-insider.org；The AI Chip Revolution Wouldn’t Be Possible Without This Company - 24/7 Wall St.；造山者瑞士聖加侖巡演台灣半導體聚集德語四國觀眾| 國際 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | +4.05% | N/A | 119.33 | 119.33 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +5.97% | +16.92% | 233.95 | 233.95 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | +22.83% | N/A | 633.91 | 633.91 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +1.01% | 0.00% | 2,500.00 | 2,500.00 | 0.00% | 不適用 | 86.28 | 28.98 | 514.81B TWD / 53.32% | 2026-09-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +5.21% | +0.94% | 161.50 | 164.50 | -1.82% | 不適用 | 6.68 | 24.29 | 25.04B TWD / 30.71% | 2026-09-01 |
| MU 美光 | 產業/供應鏈推估 | 0.00 | +10.70% | N/A | 1,074.89 | 1,074.89 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -0.56% | -3.25% | 1,719.99 | 2,335.00 | -26.34% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -4.10% | -5.99% | 355.14 | 446.77 | -20.51% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel, AMD Slide 4.2% as Nvidia Unveils N1X PC Chip \[2026\] - tech-insider.org](https://news.google.com/rss/articles/CBMie0FVX3lxTE9sZFgwRmtNRC1GR0lrbTVablMyc29CU1dDUVJDMUR1YmFmOW8yN1NsNmRyeHRlZ1ZQcE9aUjlPcF96b1ljM0liSGF6ZW9ock9rLWk4QmNBZGFjamcxYnZNNkRoa0FXNUV4SDUzQXk1TV9nQ2NIZGlGZkVQUQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 04 Oct 2026 11:00:59 GMT
- [The AI Chip Revolution Wouldn’t Be Possible Without This Company - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiqwFBVV95cUxQczRsRVU3dGhZN2JwdEJWOUtTMkZ4djRzVEh5cFVyeWk2OHN0X052RmRwYmJoUnAtVklaNTVJRkRJZzF2Rk9Zem5zbFV4aTdrREhWWnpNT05xN2VnZU1xenBjYlNNZjZFUWZZWmRtTTJmcGxPZUV3a0RzeW8xVkw3OUkxbnhUbTdHU1FSVHdHbmY5TjRYZ3B0SFNoU05yX3BhSGMyRWFRZW1HRUk?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 03 Oct 2026 15:30:00 GMT
- [造山者瑞士聖加侖巡演台灣半導體聚集德語四國觀眾| 國際 - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBURlBLYUg4UDd2S0lkd25IMnRYYzhhWnVoeWh1MUJad3RZQnRBRTBYUVlnNzVoVElTSUdsMUU2Q0J0cGUtY1I2NnFYcHFRbDRxT1duTDJfM2JLUXM2b2xv?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 04 Oct 2026 14:36:00 GMT

## 先進封裝與 CoPoS

摘要：先進封裝與 CoPoS 相關新聞集中在：面板雙虎轉型法人聚焦先進封裝技術進展| 產經 - 中央社 CNA；面板雙虎不當病貓了！群創、友達華麗轉型先進封裝法人關注10月中旬一件事- 證券 - ctee.com.tw

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +1.01% | 0.00% | 2,500.00 | 2,500.00 | 0.00% | 不適用 | 86.28 | 28.98 | 514.81B TWD / 53.32% | 2026-09-01 |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | +3.78% | +2.89% | 713.00 | 713.00 | 0.00% | 不適用 | 13.92 | 51.59 | 82.25B TWD / 45.66% | 2026-09-01 |

關聯理由（前 3）：
- 2330：產業/供應鏈推估：公司標籤符合「先進封裝與 CoPoS」關鍵字 advanced packaging, CoWoS, CoPoS, FOPLP；其中 0 篇新聞出現相關標籤。
- 3711：產業/供應鏈推估：公司標籤符合「先進封裝與 CoPoS」關鍵字 advanced packaging, CoPoS, FOPLP, panel-level packaging；其中 0 篇新聞出現相關標籤。

### 主要來源

- [面板雙虎轉型法人聚焦先進封裝技術進展| 產經 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE9OQWd1SGpkdWhsY1A1TzBGekZPcWlQS2dKS2JCbk5PRDk0cW5iT29BaGxrbFU2TkdIWmEwSHN0Mm9NVUdEWHJhem4wTXJWOEYxU1pyZG1wU0NkNi1fUlE?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 04 Oct 2026 07:08:00 GMT
- [面板雙虎不當病貓了！群創、友達華麗轉型先進封裝法人關注10月中旬一件事- 證券 - ctee.com.tw](https://news.google.com/rss/articles/CBMiX0FVX3lxTFB6VHZnVXc1bVJjdnMtNy1DdENETUFGNmJTeDlTWFRYcXJfeVEwNXdIWEFlNjFuaGM2WXNVeFhKS21jWE1RNndrd1RjV1pYWkhUSVJfRml1MHVXeVUySkhJ?oc=5) - Google News source discovery | 工商時報 Sun, 04 Oct 2026 07:41:00 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台指期夜盤飆破4萬9！ 專家估：台股10月中可站上5萬 - MoneyDJ理財網；法人盤勢分析內容-台股 - MoneyDJ理財網；法人專欄分析內容-台股 - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台指期夜盤飆破4萬9！ 專家估：台股10月中可站上5萬 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikgFBVV95cUxNTmtTRjJTTXJmenEwN0kzN3pkel9hdkxkdjE0UEJqeWh2dmlKSHBObmY4U2xPWDdhMnV6azBTRmxrUFJGN1drVWYwOEdvQUxCYm9BTzBmRFA5U2RGbFlFVk9tS3k1cnRLd2I5Y0FyRHZ1c2VfeEtBUElSSzNFX3l0MmxTcTNjbmowQW9tWnppc0FNdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 03 Oct 2026 06:12:00 GMT
- [法人盤勢分析內容-台股 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMijgFBVV95cUxNZ0FrVnNudU1oM1RSbl9Za1dCaXcxZE05Tlh0UC1ORmV5N2NLNnJhZDdCZ2tGQzNkVEpuSTlnb0ZNa3haR2FHOFl4Z005TS1aUi1YSFF3Ni1LUExkY0pQYjJIOGlHN0xCT05nMC15cXAyb1JxTjcyWGlvX2kzTWdjR2IyX3VHQUNaT2lNeUNR?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 05 Oct 2026 00:15:42 GMT
- [法人專欄分析內容-台股 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilgFBVV95cUxOcVlaZHNzdVIzRmZ5cGpIZUVBRHBQVnJqZzJHV0ZaODB2bHFtMnozM1l0bEpxRTJYM3ZNRjN1VzEwS2FLRFlUOFl6RFFJd0xsSkZtUkMwYm1INnVmTFZMcjQ4b3QzdjZ0VVZCQWViYWR4QVpicThWdVdoU3dfOHBiMVA2cnd0aTA2bzdqaERoak5odGNOMUE?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 04 Oct 2026 16:11:42 GMT

## 新興題材：台股重量級法說

摘要：新興題材：台股重量級法說 相關新聞集中在：台股重量級法說會登場　法人：震盪盤堅 - 經濟日報；台股重量級法說會登場法人：震盪盤堅| 證券 - 中央社 CNA

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股重量級法說會登場　法人：震盪盤堅 - 經濟日報](https://news.google.com/rss/articles/CBMieEFVX3lxTE9NaWdOY2ZwVlF2V1hzeHktRk1INEhQWXpVcFhYQWxCNXpLX2Y5STRURUl2UTQ2ZlFld0J3aVF4am1XRTY0cDNiOFpwLXR4bjhIcXByZWl4WEd0R0VMbk53TUVIYV83UmpEemxiQUNsOTgyS3J2OW44eNIBX0FVX3lxTFByb3RKNzZjOEsxVFMwLWpzT0hEd3J5MlZUdm15NzQtdnAwbnNEanRWVFEzU1JlRmFYVUhSMGdrUmJUMkh1cTVOTlpDQTBYaENIZGlPREhrbERvQTBUSUU4?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 04 Oct 2026 02:00:45 GMT
- [台股重量級法說會登場法人：震盪盤堅| 證券 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTFA0ZGJGVnZaRTdoN2JfUV9VVGExMzN1YlNFZm9JaFdSc2h5d0duUFdXQ3MwMTl3RE9KWGp2R0gyRXZNb2tFYUdaa0Zub01laUVEeGtPc19uUEZ6cEhYcmc?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 04 Oct 2026 01:51:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
