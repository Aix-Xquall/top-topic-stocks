# 每日股市熱門話題分析 - 2026-10-25

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **新興題材：BigGo**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0
2. **AI 伺服器與資料中心**｜負向｜熱度 11｜市場確認 65.10｜同向 6/8
3. **記憶體與 HBM 供應鏈**｜中性｜熱度 5｜市場確認 N/A｜同向 0/0
4. **新興題材：TradingKey**｜負向｜熱度 1｜市場確認 65.00｜同向 1/2
5. **新興題材：CapEx**｜負向｜熱度 1｜市場確認 65.00｜同向 1/2

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.41（樣本 14）
- 5日相關係數：0.78（樣本 10）
- 同向比例：9/14

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 新興題材：BigGo | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 65.10 | 6/8 | 1 | +4.20% | +1.93% |
| 記憶體與 HBM 供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：TradingKey | 65.00 | 1/2 | 1 | +11.51% | +11.50% |
| 新興題材：CapEx | 65.00 | 1/2 | 1 | +11.51% | +11.50% |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 關稅與供應鏈轉移 | 45.47 | 1/2 | 1 | +3.49% | +15.06% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-10-12 | -0.08 | -0.07 | +41.67% | 12 |
| 2026-10-13 | -0.05 | -0.03 | +46.67% | 15 |
| 2026-10-14 | 0.08 | -0.29 | +57.14% | 14 |
| 2026-10-15 | -0.08 | 0.08 | +33.33% | 12 |
| 2026-10-16 | -0.13 | -0.25 | +64.00% | 25 |
| 2026-10-17 | -0.10 | 0.49 | +26.32% | 19 |
| 2026-10-18 | -0.12 | 0.33 | +21.74% | 23 |
| 2026-10-19 | 0.44 | 0.36 | +50.00% | 12 |
| 2026-10-20 | 0.09 | -0.81 | +69.23% | 13 |
| 2026-10-21 | -0.25 | 0.23 | +5.56% | 18 |
| 2026-10-22 | 0.02 | -0.21 | +38.89% | 18 |
| 2026-10-23 | 0.35 | 0.29 | +78.95% | 19 |
| 2026-10-24 | 0.09 | -0.31 | +70.00% | 20 |
| 2026-10-25 | 0.41 | 0.78 | +64.29% | 14 |

## 歷史回測摘要

- 回測日期：2026-10-25
- 近5日 3日相關：0.58
- 近5日 5日相關：-0.45
- 同向比例：+75.00%
- 權重狀態：未調整

- 方向準確度：+75.00%
- 信心排序準確度：0.58
- 診斷：正相關

調整原因：近 5 日有效樣本 8 筆，低於 15 筆門檻，暫不調整權重。

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

## 新興題材：BigGo

摘要：新興題材：BigGo 相關新聞集中在：Micron and Sandisk Both Tripled in 2026, but Wall Street Sees More Room in Micron - BigGo Finance

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | -9.62% | N/A | 877.55 | 971.00 | -9.62% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | -9.33% | -4.72% | 1,238.03 | 2,335.00 | -46.98% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。

### 主要來源

- [Micron and Sandisk Both Tripled in 2026, but Wall Street Sees More Room in Micron - BigGo Finance](https://news.google.com/rss/articles/CBMidkFVX3lxTE9kUnYwLW8yd2xYXy1qdlFfWmUySVpLSGFZR3Rhb3hTZllNVGxwMzRaWjBQQWZma0ttTEc3NE9yYzVLX3E0bzE2dWk4a00tRVR1WHVUMXQxYnZSdTgtOThmb3hlYW5nNmFjNXlWbFpYTGtyTmpHbmc?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 23 Oct 2026 18:15:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：AI資料中心支出續增，現金流壓力會先壓到誰？-柏宇 KD 獲利模式 - CMoney投資網誌；營收兩千萬美元授權門檻如何影響 AI 商業化？ - TechNews 科技新報；中國 AI 模型接連出海對全球開源生態的衝擊？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | -0.08 | -24.17% | N/A | 86.96 | 114.68 | -24.17% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | -0.06 | -4.45% | +5.43% | 210.96 | 228.38 | -7.63% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | -0.04 | +0.13% | N/A | 516.79 | 516.79 | 0.00% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.06 | -1.45% | -2.25% | 2,385.00 | 2,480.00 | -3.83% | 同向 | 86.28 | 27.65 | 511.86B TWD / 54.65% | 2026-10-01 |
| MSFT 微軟 | 產業/供應鏈推估 | -0.02 | +16.50% | +6.61% | 524.51 | 524.51 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -13.14% | -14.84% | 321.68 | 446.77 | -28.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.04 | -2.39% | -2.82% | 654.00 | 703.00 | -6.97% | 同向 | 13.92 | 47.32 | 88.13B TWD / 45.52% | 2026-10-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.04 | -4.64% | -3.72% | 4,010.00 | 4,920.00 | -18.50% | 同向 | 60.69 | 66.23 | 55.40B TWD / 1.97% | 2026-10-01 |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 5 篇新聞出現相關標籤。 方向判斷命中詞：衝擊。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 5 篇新聞出現相關標籤。 方向判斷命中詞：衝擊。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 5 篇新聞出現相關標籤。 方向判斷命中詞：衝擊。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AI資料中心支出續增，現金流壓力會先壓到誰？-柏宇 KD 獲利模式 - CMoney投資網誌](https://news.google.com/rss/articles/CBMigAFBVV95cUxQWEJwQXdEbDF4c1J3VFdwdlN6SDdudFVjV0VVREYwV3QxWlZ0eTY5VmNNbDBMZEZsc1Z4UkhNUGk2Y2t5SlR2ZHA4TGpJdDc5X2ZrbTdyNHlBQ0FPRkJjV3Vqbzc4ZW1kdlJpVnM1RXJ4ZG1IOS1Ydk1rZzhtMkR1QQ?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 23 Oct 2026 05:27:12 GMT
- [營收兩千萬美元授權門檻如何影響 AI 商業化？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiZEFVX3lxTE15RFFuZENZYnpQOEljOFZQNzk0ZkhoWmNMVmdtaHRCNEFxM254dUlRVTRfTDhteVcwbVI3MEtObmlmSGVNNGVtVXA2VnpyNWttWXhkdExEM0YyYXZJa0JlYmJvdVI?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 24 Oct 2026 21:03:49 GMT
- [中國 AI 模型接連出海對全球開源生態的衝擊？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiZEFVX3lxTFBCQmc0cjVsQzlJcGpLNmVFTjdDMDRGdmtJVU5yWkNZVFNSSEgyaW1CU3dWWjJTSmZUZGpVUjVCS2RRZXl0Nk9NUG5Va3hHWHp5SmxaSVo1U0FhZmEyNDFNWFM0NG4?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 24 Oct 2026 21:02:20 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Micron vs. Sandisk: Which Is the Better AI Memory Stock to Own for the Next 3 Years - Yahoo Finance；Micron vs. Sandisk: Which Is the Better AI Memory Stock to Own for the Next 3 Years - The Motley Fool；Better Memory Stock: Micron vs. Sandisk - Yahoo Finance

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | -9.62% | N/A | 877.55 | 971.00 | -9.62% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | -9.33% | -4.72% | 1,238.03 | 2,335.00 | -46.98% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -4.45% | +5.43% | 210.96 | 228.38 | -7.63% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 5 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Micron vs. Sandisk: Which Is the Better AI Memory Stock to Own for the Next 3 Years - Yahoo Finance](https://news.google.com/rss/articles/CBMilwFBVV95cUxNYVBRaFNhTkpyeEZmQWtnZWE3UFNEQzM3d3lndzhpWTFadU9JbGhYTWRCMzhaZ0toeUF0S3NiTUdCaDBzazhuNDFyVmxXOG9ZWldXc0JpUHdiaTFjSXpCTHlWcmp0c2pUaDN5RjlvUWZUeGJDTzhyZmZJQ2xXemo3QlJFZXVIWUlKaFpoRFByMF9OQ2lTNC1B?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 24 Oct 2026 13:22:00 GMT
- [Micron vs. Sandisk: Which Is the Better AI Memory Stock to Own for the Next 3 Years - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxPUjZqMUtTU1d6MnMzTVF6Z181YmxqSGF5YTFkdUQzaWRQaDJXSUpkWVZ1TGFuaWxyOWRCOWJUdkNjSzdja05jR0hjcFg2TkhoVHdULTFnLWJLaXAwem1HVXhDbXRFRFU0RnRqNjBOZDlQLTVWcVVHOURfMjFvOHNlVW1FZmJMSDRZeVREYWtibUp3RTlFZ2xEZA?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 24 Oct 2026 14:02:00 GMT
- [Better Memory Stock: Micron vs. Sandisk - Yahoo Finance](https://news.google.com/rss/articles/CBMimgFBVV95cUxNSjgxYWpWQUVNSTJOb1dRdEpxemFxXzVrcXozZXVjWFRDZWZvSC1KeWdpX2xJVFFfZURseXpBR1M2aUsyLThuVmw2R0pFVGlwaG5QeFNEVmg3ZlI2NXR6VV9Denl5N1BTYVZLRTdON2d5RlFFUzlGY1FQb3RldTNFbk92TXA2aXQ4WkdFTEc0S1RSMVlLM3ZLNURR?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 23 Oct 2026 09:04:00 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Why Did Intel Stock Plunge 8%? Tesla CapEx Cut Sparks AI Chip Demand Concerns - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.42 | -24.17% | N/A | 86.96 | 114.68 | -24.17% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| TSLA 特斯拉 | 新聞直接提及 | -0.21 | +1.16% | -11.50% | 372.22 | 456.56 | -18.47% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 方向判斷命中詞：cut。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- TSLA：新聞直接提及「Tesla」，共 1 篇新聞命中。 方向判斷命中詞：cut。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Why Did Intel Stock Plunge 8%? Tesla CapEx Cut Sparks AI Chip Demand Concerns - TradingKey](https://news.google.com/rss/articles/CBMi0gFBVV95cUxQWHVWUUlxd0JKSTZEZkRRTmdHRDdqUWJWcHJEanRxS0Nqdm9sWG96OUVWYVFobHFwNG9xZjA4WVFKUFNNN2tDY0wzOUdQY29sdG1rVXNDRnRVS29DSjR3YnZSZzJlV1BTT3dsSFhGNTlObFJDY3BkYTMzOGFlRS1HWXRKd3U3N0c1Mk9rZFBZWWI2czRMLXZISmIwUWd5YzdXVUl4MGEwbWhkTmI4eHY5RkFXLVRoVkhVc1JQaFRUellIQ0phSUlxWXJyMnFrbm4zVHc?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 23 Oct 2026 06:52:49 GMT

## 新興題材：CapEx

摘要：新興題材：CapEx 相關新聞集中在：Why Did Intel Stock Plunge 8%? Tesla CapEx Cut Sparks AI Chip Demand Concerns - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.42 | -24.17% | N/A | 86.96 | 114.68 | -24.17% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| TSLA 特斯拉 | 新聞直接提及 | -0.21 | +1.16% | -11.50% | 372.22 | 456.56 | -18.47% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 方向判斷命中詞：cut。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- TSLA：新聞直接提及「Tesla」，共 1 篇新聞命中。 方向判斷命中詞：cut。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Why Did Intel Stock Plunge 8%? Tesla CapEx Cut Sparks AI Chip Demand Concerns - TradingKey](https://news.google.com/rss/articles/CBMi0gFBVV95cUxQWHVWUUlxd0JKSTZEZkRRTmdHRDdqUWJWcHJEanRxS0Nqdm9sWG96OUVWYVFobHFwNG9xZjA4WVFKUFNNN2tDY0wzOUdQY29sdG1rVXNDRnRVS29DSjR3YnZSZzJlV1BTT3dsSFhGNTlObFJDY3BkYTMzOGFlRS1HWXRKd3U3N0c1Mk9rZFBZWWI2czRMLXZISmIwUWd5YzdXVUl4MGEwbWhkTmI4eHY5RkFXLVRoVkhVc1JQaFRUellIQ0phSUlxWXJyMnFrbm4zVHc?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 23 Oct 2026 06:52:49 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：菲律賓力拚發展半導體產業周民淦：台灣可助攻| 國際 - 中央社 CNA；林佳龍接見英駐台代表盼深化半導體量子科技等合作| 政治 - 中央社 CNA；功率半導體補助如何強化美國能源科技競爭力？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | -24.17% | N/A | 86.96 | 114.68 | -24.17% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -1.45% | -2.25% | 2,385.00 | 2,480.00 | -3.83% | 不適用 | 86.28 | 27.65 | 511.86B TWD / 54.65% | 2026-10-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | -4.56% | -5.99% | 125.50 | 164.50 | -23.71% | 不適用 | 6.68 | 18.87 | 25.35B TWD / 27.22% | 2026-10-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -4.45% | +5.43% | 210.96 | 228.38 | -7.63% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | +0.13% | N/A | 516.79 | 516.79 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | -9.62% | N/A | 877.55 | 971.00 | -9.62% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -9.33% | -4.72% | 1,238.03 | 2,335.00 | -46.98% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -13.14% | -14.84% | 321.68 | 446.77 | -28.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 CPU, server CPU, x86, foundry；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 0 篇新聞出現相關標籤。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 0 篇新聞出現相關標籤。

### 主要來源

- [菲律賓力拚發展半導體產業周民淦：台灣可助攻| 國際 - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9jWkl5VVIyTmdCZkU1TGRQOC1RczBjd0FXNGdoSW1JSlpfbmNOY3llTVlPWVNvYXFjVWZPM3p0SjhpMXg3eWtEMDlaSnpXVV9PdnlzQ1lOYTJKRXlvckxj?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 24 Oct 2026 12:10:00 GMT
- [林佳龍接見英駐台代表盼深化半導體量子科技等合作| 政治 - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBOM2QxNjE2Z2VfUG4zcXFrZ29JdXJoOF93ZUJDcG9BOG9xN1U4SkZQOExENU9CcjRPSk5sdU5WM3ZISlpHZkxZNVY5bzRkcndxTEt4NWRoRWpiUFlnclVN?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 23 Oct 2026 04:42:00 GMT
- [功率半導體補助如何強化美國能源科技競爭力？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiyAFBVV95cUxPN0d5NVBkdEpCSlozdGs1U0RFNXg2SWxrRkZsNjc1Z2o5dUxaSXZEMFNUSmtMSmMyTG9CSGxPT19qS202ZGRlVmNWaEY3WXczYlFzNkxMNTFCc0pxUmhzdUdKblJmcnk0SHd4MUVLLXk5UHNEc0g3Y053aXlMRV9HZWtMVUt0QTFTV1ZrRnBqSXFPWUh3eElLRUs4S3VLZnd0ZkYtdENnMWJUb0tOM0hOQklPWkszLW1xQ0M2ZUdrdDI0U0Q1MzVZaA?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 24 Oct 2026 13:03:32 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：整理包／黃仁勳概念股笑了！輝達季度財報超預期 完整台廠供應鏈名單、潛在受惠股一次看 - 經濟日報；蘋果研發 6G 晶片對高通供應鏈的長期影響？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AAPL 蘋果 | 新聞直接提及 | +0.45 | +11.43% | +24.70% | 347.73 | 347.73 | -0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.21 | -4.45% | +5.43% | 210.96 | 228.38 | -7.63% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | +2.30% | +2.30% | 245.00 | 289.00 | -15.22% | 不適用 | 15.21 | 16.15 | 1158.63B TWD / 38.42% | 2026-10-01 |

關聯理由（前 3）：
- AAPL：新聞直接提及「蘋果」，共 1 篇新聞命中。 同時符合主題標籤：tariff, supply chain。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [整理包／黃仁勳概念股笑了！輝達季度財報超預期 完整台廠供應鏈名單、潛在受惠股一次看 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBQUlViSHpPeDVlY29yaHFNNE5NcVlUQnE3ZThTcXRGNHgxYTVPOVVTRDlaTDV6Zml5WEwxVHNSeGFDcnVHUHhRSW15SzNpU0dYVDU3dThWNEVCbkZI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 23 Oct 2026 09:00:00 GMT
- [蘋果研發 6G 晶片對高通供應鏈的長期影響？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiuAFBVV95cUxONEtWdDkzX2thVS03ZUlBYnZhVTVISUxDRFRvRzJfVmV1NUdGYTNWVUtOY3AxQk4xTWgyMmlhem54RG1BY3ZFbkR0a1VwZzNJa01IaHZvaXc5OWJFV0NKWm1Nd3hJc1F5YVFHc1FKWkJSS2p0bDB0Unh1MDE5WHFGQWlZUjdtenVXNm9mbExwak1jXzRrMF9ESTVNUFlmTkRqOER4R3ZTYXVELW1ubzhzNTJDTkhSZHM4?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 24 Oct 2026 22:00:03 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：個股動態報導內容-82A5A219-765B-4154-BF8F-210BB2829DF9 - MoneyDJ理財網；個股動態報導內容-F1107D08-018C-4ADE-9F29-F3768B6DA8BC - MoneyDJ理財網；同業股價表現-電子-化學氣相沈積設備-台股 - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-82A5A219-765B-4154-BF8F-210BB2829DF9 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilAFBVV95cUxNb1pvMUc1clVKUENLaFNvS0VRSEJLSTRhWTZ6YXJLQjh4bmhsWWxCenJUNGtXWFNySmFQWm5COEJpWUtWZFlud054bW10YXJPT2VJblVQRkZMZ2FFRF9NSTNYZzFRQ213MFd2Wmg4SGcwbEo5M0JhdVNGN3l1TVBHTGdORDJRY0J3aWlBd1ZiTDlMUXFQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 23 Oct 2026 08:24:29 GMT
- [個股動態報導內容-F1107D08-018C-4ADE-9F29-F3768B6DA8BC - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilAFBVV95cUxNaWpwT05pSGI3MEFIT04wVm9jWEpmRE9mUm5XalhxblpYdV9EY094amdJaDgwS2JEalBJYnpjbkpMUHhNSFZMTHpPVGRGNHNaRU5XenFJaUpIZHBPUnlyMm1kRnFuTFllQW02T29RRE45dnN2a3NFSmY1ZDRpT3NMX2RuN2pEd1gtdlZESkU3V0g0UXBD?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 23 Oct 2026 08:07:19 GMT
- [同業股價表現-電子-化學氣相沈積設備-台股 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMiaEFVX3lxTFBXSzlCQzBsQkVoMVN1dXlSYmZ6V3FFOTYwWklrY1ppWC0wajNfakFzekZOXzVRc3BITURJa2VDdE9KODVGaDhZcTVtUXNzMUx4U0I1YmEtVF9mNE80RnlpX1liVzN2VkZQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 23 Oct 2026 15:25:56 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
