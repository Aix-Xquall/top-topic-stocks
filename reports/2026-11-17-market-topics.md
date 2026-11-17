# 每日股市熱門話題分析 - 2026-11-17

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜負向｜熱度 8｜市場確認 100.00｜同向 3/3
2. **新興題材：TradingKey**｜負向｜熱度 1｜市場確認 100.00｜同向 2/2
3. **AI 伺服器與資料中心**｜負向｜熱度 8｜市場確認 91.25｜同向 7/8
4. **新興題材：一顆晶片**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0
5. **半導體與晶片供應鏈**｜正向｜熱度 3｜市場確認 0.00｜同向 0/1

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.44（樣本 15）
- 5日相關係數：0.39（樣本 12）
- 同向比例：12/15

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 100.00 | 3/3 | 0 | +24.94% | +15.47% |
| 新興題材：TradingKey | 100.00 | 2/2 | 0 | +21.59% | +8.73% |
| AI 伺服器與資料中心 | 91.25 | 7/8 | 1 | +12.36% | -0.64% |
| 新興題材：一顆晶片 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | 0.00 | 0/1 | 1 | -7.52% | -0.89% |
| 關稅與供應鏈轉移 | 0.00 | 0/1 | 1 | -10.86% | -1.96% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-11-03 | -0.03 | 0.08 | +40.91% | 22 |
| 2026-11-04 | -0.21 | 0.35 | +15.79% | 19 |
| 2026-11-05 | 0.13 | -0.53 | +66.67% | 12 |
| 2026-11-06 | -0.18 | 0.77 | +100.00% | 5 |
| 2026-11-08 | -0.21 | 0.03 | +23.08% | 13 |
| 2026-11-09 | -0.56 | -0.62 | +60.00% | 10 |
| 2026-11-10 | -0.32 | 0.24 | +3.45% | 29 |
| 2026-11-11 | 0.34 | -0.26 | +46.67% | 15 |
| 2026-11-12 | -0.09 | 0.07 | +50.00% | 14 |
| 2026-11-13 | -0.56 | 0.42 | +54.17% | 24 |
| 2026-11-14 | -0.34 | 0.12 | +42.11% | 19 |
| 2026-11-15 | -0.02 | 0.62 | +50.00% | 20 |
| 2026-11-16 | -0.30 | -0.27 | +38.89% | 18 |
| 2026-11-17 | 0.44 | 0.39 | +80.00% | 15 |

## 歷史回測摘要

- 回測日期：2026-11-17
- 近5日 3日相關：0.42
- 近5日 5日相關：0.27
- 同向比例：+53.33%
- 權重狀態：已調整

- 方向準確度：+53.33%
- 信心排序準確度：0.42
- 診斷：正相關

調整原因：近 5 日信心分數與後續報酬呈正相關，提高市場確認、歷史題材與直接提及權重。；關鍵詞×公司後續樣本有效 0 筆，未達 30 筆，不調整樣本權重

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

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：‘I’m Not a SanDisk Fan. I’m a Micron Fan’: Jim Cramer Picks Sides. Why MU Stock Looks Safer Than SNDK Stock. - Barchart.com；SK Hynix Is Down 16% in a Month. What Will It Take to Get SKHY Stock Back to $150? - 24/7 Wall St.；US Memory Stocks Tumble Again Overnight as SanDisk, Micron Fall Over 4%, Western Digital Drops Over 3% - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | -0.59 | -25.95% | N/A | 719.02 | 971.00 | -25.95% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.59 | -17.24% | -8.73% | 809.11 | 2,335.00 | -65.35% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | -0.45 | -31.63% | -22.22% | 156.14 | 228.38 | -31.63% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK、SanDisk」，共 5 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [‘I’m Not a SanDisk Fan. I’m a Micron Fan’: Jim Cramer Picks Sides. Why MU Stock Looks Safer Than SNDK Stock. - Barchart.com](https://news.google.com/rss/articles/CBMi3AFBVV95cUxPemdiUWFhaEd2eHIwVlAwUWYwcUVpR1hibl9kVGJFMFhhX2lES0pJMnpnWlQxU0JsRUZ5Q1hMYzNvamotdTZ5aHVYZ0lFTThrbWlUNEV1dV9vWDZKQ2xLM1lYN0NGTVJkMXlPUXFJT0xVNHhEYXZ5RHhyT2VZSjJGbE1ocXFSek5VMEVEQzlhN25KNFJrY0pyZGZZX2ZtQV9NWURrcEM2UERLdVFGdVUwd2RfUllXeDVDU2hreE96RlVkV2lGc2c5VTVPaV92SWgyVm9WN0lkcjd6dEhI?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 16 Nov 2026 22:25:27 GMT
- [SK Hynix Is Down 16% in a Month. What Will It Take to Get SKHY Stock Back to $150? - 24/7 Wall St.](https://news.google.com/rss/articles/CBMivwFBVV95cUxOSl83eG1sQ3h1TzdRREptcHhkdmY5aXhnY3l1M1NkdXFtNlVTRmJ2Tjk5ZjB3TXBjb3phMl9lbmtPUGsyWTJlaFJBSDdvLS1GemhaMVRUU2x0OERJVkt2Vlh3STFLUXNObzRGVTFuczdvM0VCR2NzY01qYUZDUkNzQW92SG5nUl9KYzBxRlBXbk4zNU12c25iWmd2UDdqcWh4azZ2OGphd3VOVDNsMTJSdENEampNdmlXcWZqS1ZJZw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 16 Nov 2026 19:03:00 GMT
- [US Memory Stocks Tumble Again Overnight as SanDisk, Micron Fall Over 4%, Western Digital Drops Over 3% - TradingKey](https://news.google.com/rss/articles/CBMipwFBVV95cUxQUC1HOUEwbG9WdkFmalNKM2Z6Sk9zUno5N1dneFk3dHctWDluU0xXWGlweUN4cHQzU0k5dGJBVDZkS2lrTVpWWURLYm11RjBFV1VkSE1mVlhDQlYwN1ZoUVB1d0N4OTdoZU9TV19IRjAxMFg3TElmOTg4Wl83WC1tWmlhVDZpSEVRZVdnajFtU3ZIYWVwc0dMd2hFRUI5MWJuUExVMU5iMA?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 16 Nov 2026 09:08:31 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：US Memory Stocks Tumble Again Overnight as SanDisk, Micron Fall Over 4%, Western Digital Drops Over 3% - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | -0.44 | -25.95% | N/A | 719.02 | 971.00 | -25.95% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.44 | -17.24% | -8.73% | 809.11 | 2,335.00 | -65.35% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron」，共 1 篇新聞命中。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 1 篇新聞命中。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。

### 主要來源

- [US Memory Stocks Tumble Again Overnight as SanDisk, Micron Fall Over 4%, Western Digital Drops Over 3% - TradingKey](https://news.google.com/rss/articles/CBMipwFBVV95cUxQUC1HOUEwbG9WdkFmalNKM2Z6Sk9zUno5N1dneFk3dHctWDluU0xXWGlweUN4cHQzU0k5dGJBVDZkS2lrTVpWWURLYm11RjBFV1VkSE1mVlhDQlYwN1ZoUVB1d0N4OTdoZU9TV19IRjAxMFg3TElmOTg4Wl83WC1tWmlhVDZpSEVRZVdnajFtU3ZIYWVwc0dMd2hFRUI5MWJuUExVMU5iMA?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 16 Nov 2026 09:08:31 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：台股強震近1,750點！AI 高價股淪重災區 34千金僅「這4檔」逆勢走揚 | 市場焦點 | 證券 - 經濟日報；AI 踩煞車？調查機構下修支出預估、輝達承壓 - TechNews 科技新報；Google 示警：AI 代理已能「零人工」將修補程式轉為漏洞攻擊 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | -0.59 | -31.63% | -22.22% | 156.14 | 228.38 | -31.63% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 產業/供應鏈推估 | -0.08 | -51.63% | +36.76% | 55.47 | 114.68 | -51.63% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | -0.06 | -2.29% | N/A | 504.28 | 534.06 | -5.58% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.06 | -7.52% | -0.89% | 2,210.00 | 2,480.00 | -10.89% | 同向 | 98.27 | 22.54 | 586.89B TWD / 59.71% | 2026-11-01 |
| MSFT 微軟 | 產業/供應鏈推估 | -0.02 | +15.05% | +5.28% | 517.99 | 523.88 | -1.12% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -5.07% | -14.35% | 333.40 | 446.77 | -25.38% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.04 | -10.86% | -1.96% | 526.00 | 703.00 | -25.18% | 同向 | 17.55 | 31.57 | 88.62B TWD / 47.13% | 2026-11-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.04 | -4.89% | +1.88% | 3,885.00 | 4,920.00 | -21.04% | 同向 | 62.35 | 61.04 | 55.03B TWD / 5.77% | 2026-11-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 2 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。 方向判斷命中詞：下修, 升級。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：下修, 升級。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：下修, 升級。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [台股強震近1,750點！AI 高價股淪重災區 34千金僅「這4檔」逆勢走揚 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5SbFV2QjlUeHY5OUhONVdyelp4QmoyYjA4U3BsU2RILVNfWHV2MGNQUDNEaWRuaDZ1NmdsMDlnUmowamN5Q203TGc2dWJjbGdSbF9SX0ZXWTVZQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 17 Nov 2026 03:19:28 GMT
- [AI 踩煞車？調查機構下修支出預估、輝達承壓 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiuAFBVV95cUxOZzJKeXpwOFlpWkJrSmd1LVR1WENUQU5lMm43WmE3UnFTTHBJZlc0RDNxSlJ0TWNIS0VvdlJGZ1RDeEg4a0x0bzc2UVp6QXB6MG9lRTQySkxzVDl2djU4eFFVNkRBdFBaUmNqam1PbnJoaUh6U05vMTNnYjJIQUN0OU9kZlVyWlRiSmtRVHhROGp5WmxURk5vUGhpZndBWE5EMS15amZHUEhreFBNRmxJd3EzeDhOZHQx?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 17 Nov 2026 03:27:54 GMT
- [Google 示警：AI 代理已能「零人工」將修補程式轉為漏洞攻擊 - TechNews 科技新報](https://news.google.com/rss/articles/CBMinAFBVV95cUxNcnk1NXdManhJNFI4LXpYZlltNDF3NUVrYlREeUZENkZxQnVIaVcxQXRkQnNuOWJfLUhTbnhsYm1DclE3SFVVVWM2ZkxUUGZOeGpoQ0dORzRwV3gwYkppVnkwUFJzdXI1QTFqaHFqTmFjYXJpWUk3V3VQNmJjdTdSYkQ1TTl2ckl0M3AtdFp1c3NjWWQzNzc3T1dHOEY?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 17 Nov 2026 03:12:50 GMT

## 新興題材：一顆晶片

摘要：新興題材：一顆晶片 相關新聞集中在：一顆晶片運送托盤，揭開日月光的減碳神話！當 AI 算力飆升，封測龍頭如何用「供應鏈韌性」築起新護城河？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3711 日月光投控 | 新聞直接提及 | 0.00 | -10.86% | -1.96% | 526.00 | 703.00 | -25.18% | 不適用 | 17.55 | 31.57 | 88.62B TWD / 47.13% | 2026-11-01 |

關聯理由（前 3）：
- 3711：新聞直接提及「日月光」，共 1 篇新聞命中。

### 主要來源

- [一顆晶片運送托盤，揭開日月光的減碳神話！當 AI 算力飆升，封測龍頭如何用「供應鏈韌性」築起新護城河？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMirAFBVV95cUxOb3Y4WEdaazF1RmYyUEowMF8zUmlWbGRwLUFIYXlCXzV2U25yTUNQTjZqRk9NZ3JXRGp4MUdmdUlycl92MGo2cE5zNVFDbk5manE1NzdfWnpQM1NXUTRjZmJmakZLbmtsZ0VUdjZRU0JObnh1dTFXdEVPN2xKZzRlSXloZ18wOGktR00wTlhfZkVadE1POExmeUkxb01JYldIcVRXZzhhckc5aFZk?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 17 Nov 2026 01:31:22 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：美國升級對中國 AI 晶片管制，新加坡、泰國、馬來西亞、印尼與巴西列高風險國家 - TechNews 科技新報；台積電ADR大幅下跌，反映了市場對半導體產業前景的擔憂嗎？ - 鉅亨網；台積電ADR大幅下跌，與整體半導體產業趨勢相關嗎？ - 鉅亨網

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | +0.28 | -7.52% | -0.89% | 2,205.00 | 2,480.00 | -11.09% | 背離 | 98.27 | 22.54 | 586.89B TWD / 59.71% | 2026-11-01 |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | -51.63% | +36.76% | 55.47 | 114.68 | -51.63% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | -8.46% | -1.55% | 93.00 | 164.50 | -43.47% | 不適用 | 6.80 | 14.06 | 25.20B TWD / 18.33% | 2026-11-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -31.63% | -22.22% | 156.14 | 228.38 | -31.63% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | -2.29% | N/A | 504.28 | 534.06 | -5.58% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | -25.95% | N/A | 719.02 | 971.00 | -25.95% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -17.24% | -8.73% | 809.11 | 2,335.00 | -65.35% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -5.07% | -14.35% | 333.40 | 446.77 | -25.38% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip, foundry。
- INTC：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 CPU, server CPU, x86, foundry；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 0 篇新聞出現相關標籤。

### 主要來源

- [美國升級對中國 AI 晶片管制，新加坡、泰國、馬來西亞、印尼與巴西列高風險國家 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiiAFBVV95cUxQeGR0dEM4RmRpT1RUd0pUSkZUbDdQbVJUSjA1c05zSzJnYWJqVFVVVUNicjd4WjdsWTNZMTlpdHg5aWZmNVNXYnBmcldzTmQ2WGVOYjRYaXFtRGsxVG8wbWlpUS1fZk52THc5YTFySF9pTDRPWmQtWG9ndUI2VTVWM0tSd0VodTRj?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 17 Nov 2026 00:22:52 GMT
- [台積電ADR大幅下跌，反映了市場對半導體產業前景的擔憂嗎？ - 鉅亨網](https://news.google.com/rss/articles/CBMigwRBVV95cUxPbjZYcUl6amdFQ2haNkNkRW5yWEEzTTFEekJsU0pFbjhnc3lHQ2R1cGxkMmNlSE5mX2RrV3NmRUowaERGdm02ekJKQUV2X1JjcWdMTDNPT0JtS19tU2ZOM2MyaGFKQTlqZDhEeFpkWXpnbV90Yy1tOUVMc1F5RFNGQ21mZy1iWTJXV0NucU4xRThDbExZeFpPczhzRjRWd0pnLWdNVzlUMlJwOHZKMG1rNElWUzBTd0t0NW9rd3hELTAwTVFwSjJYUmxfeHpXdGdVNmx6SmkwcExLY0JDdkdrMm5aUXlZY0VjcGFTSHBFd1JkV2VIZ0FoZ24zc0x3bXJZb1drd0FZa0RCSmxlRXJzT0wtM1FMLTJRMThwZUhiajBCRDYweXBQSEM5MVFhSHBwa2NFWHZsWUYwNHZ0WWExbmJZOWNpTWNxMk1zbFYtajV6RDhqMUhVZS1jUF9TVVQxUXNiQ09jeVJmTlJPR2FxNXBuWmh2bFpiZU1EUHFNd1otRERPdkFTYVhrTl9XVmZTWWVOMDN4Q2M1ZW9wekJoWFYzYW5YMDFtRUVBb2dPVlJlUzhSLWJxTVhqOGNyTDFUSlZZbmZQenJqazFkejJRcnBqQlBydmlET1pJd1BIV3JVdzVGUmFoSG9qOV9uVWd4Z2ZJY0V6ZGhNZURqdS0wOFBXUQ?oc=5) - Google News source discovery | 鉅亨網 Mon, 16 Nov 2026 14:53:42 GMT
- [台積電ADR大幅下跌，與整體半導體產業趨勢相關嗎？ - 鉅亨網](https://news.google.com/rss/articles/CBMi0wNBVV95cUxOYjdETDg0cDVXaFNudnFrbTJneFNFUDBzLS16LXJVUVBFeE8taXBuQW9mVTR6Q3YtSGNaSUp0d3R4U3dhMGlzZVQ5TGtrVTVIQUJLYTRzbXp4TmU0dWI1b1QzLS1WY3FmTm9BR1EyWXltNjNJeTFKNFd0ZVVQclFicldQX2xmNHYyLWVKUXVhOWtFUVdhMThsdzJJLVh6MksyRUZUT2Rrby04TjQ1N0FTMzdWb0Y1TkVsdFk3WlFHMjMyQURDQlJhNWE0SzR4d1VtdURLQ2k0clo3cDRFOFBzTndDLS1PTFFUcW5VbGhZWnluRkUxSGQzcUhQams5RHRSMHU3M29XaVF0VHdXNWlqcnhRVVhEZm83TjZRSVFSQ1ZpbmI0WVlZejlPbUFuRzZNbHdpT0NWVlRFVGdRYXFYRGpHMzZZZVMySGxESGYydkY2VkJkY0RGOER2MklTS3JLaFFnUW5GUm41YlIxajNwcmJiTkpNa2xxX01tZ09BT0FZeHptTm9JajZMLXN2QVdNS0plUEhfU1dfWHBRbmVTcFRQUXB3Mi16SFZnR3N5TVZRRjM3UHppUTZraDN2SWQ3M2tvX3R3alJXR3JscDJBUDhpTQ?oc=5) - Google News source discovery | 鉅亨網 Mon, 16 Nov 2026 14:09:38 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：美擴大先進半導體出口管制新加坡：持續與美溝通、協助企業因應| 國際 - 中央社 CNA；一顆晶片運送托盤，揭開日月光的減碳神話！當 AI 算力飆升，封測龍頭如何用「供應鏈韌性」築起新護城河？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3711 日月光投控 | 新聞直接提及 | +0.22 | -10.86% | -1.96% | 525.00 | 703.00 | -25.32% | 背離 | 17.55 | 31.57 | 88.62B TWD / 47.13% | 2026-11-01 |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +13.05% | +26.51% | 352.78 | 356.27 | -0.98% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | -9.71% | -8.58% | 221.00 | 289.00 | -23.53% | 不適用 | 16.57 | 13.22 | 1305.32B TWD / 45.73% | 2026-11-01 |

關聯理由（前 3）：
- 3711：新聞直接提及「日月光」，共 1 篇新聞命中。
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [美擴大先進半導體出口管制新加坡：持續與美溝通、協助企業因應| 國際 - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTFB2ZkF3b2RfcVotVVlwV1JRVkh2RGkzM2M1eXczWC1RZkZ6bVVRNExlQ1JsbVhabFNCWXZKb2lYSlJfVE1qRnJlQkdEd09URm9XWGVaRUw4OHE4VkNObmx3?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 17 Nov 2026 03:41:00 GMT
- [一顆晶片運送托盤，揭開日月光的減碳神話！當 AI 算力飆升，封測龍頭如何用「供應鏈韌性」築起新護城河？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMirAFBVV95cUxOb3Y4WEdaazF1RmYyUEowMF8zUmlWbGRwLUFIYXlCXzV2U25yTUNQTjZqRk9NZ3JXRGp4MUdmdUlycl92MGo2cE5zNVFDbk5manE1NzdfWnpQM1NXUTRjZmJmakZLbmtsZ0VUdjZRU0JObnh1dTFXdEVPN2xKZzRlSXloZ18wOGktR00wTlhfZkVadE1POExmeUkxb01JYldIcVRXZzhhckc5aFZk?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 17 Nov 2026 01:31:22 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股崩跌失守42K、重挫1,900點！楊金龍：沒有國安基金跌勢恐更大 - 經濟日報；恐慌賣壓出籠！台股遭血洗 跌點史上第二大 專家：止跌盯四訊號 - 經濟日報；台股重挫2,635點 金管會、證交所：必要時出手救市 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股崩跌失守42K、重挫1,900點！楊金龍：沒有國安基金跌勢恐更大 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBfY1BIdVZJUXQydzFkd2l3Tm5vZGR4QnoyZ08tb1J5OUotTHE5RWZzUFpIVFg5bjQwZHU5c0lZQVhjQ044MmtTVVQwdUxVMlpUaHJFc05udnBGZ9IBX0FVX3lxTE1Sbmo0TzhVRlZWTlh2dGV3TnRGZ0d5S1piRnlBWDEtZTVlR0QxcXFYWUR0WFBJbnpLZGhJejlRU3F0U2Ryc3I1dm1ZUWdUUHRZRXUxbWJyMEtxeDBoaUxZ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 16 Nov 2026 03:55:00 GMT
- [恐慌賣壓出籠！台股遭血洗 跌點史上第二大 專家：止跌盯四訊號 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE4wX1ktMlcyUTk0OHQ3cVhYdm8zS0dILWhfZ200bk1TQWJaNENzbXEwclRxLXBRMm9RMmE0X3NsekZhczJ4cDhSTERpZHN4eWs1ei1rX3pYdzFJd9IBX0FVX3lxTE43ejVKcjI2MEVaZksxOWNSckRGazZKMVRTMnZYUHR4SEhBbHdZNkJnMGFXM3V5cmNNRzkzSGZFUlh5S19UVmpmRnRvR3dYVUJ1eG1yMVpFd2ltUXR5d09z?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 15 Nov 2026 08:00:00 GMT
- [台股重挫2,635點 金管會、證交所：必要時出手救市 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE94UnB5U283Tk56R2laQ0N3UHcwZmF4dTlBTVZQU0hWeFg2ajJtVElmMzNRZ2hYZEprOHdKUmVuWDQtNjk1cF9vRExEb09wM2oweUY5M2UtYVU3UdIBX0FVX3lxTE5Fd1NTZUlXTVB1VW93VHNTTlhRSlFSYmFmNVhfZjZLQ3JZXzVZSUU3UFctQXA4QzQ3MXU4NjJwWmhpalliTHhJeXFYVWM0dF9Ob1g5cUhDUkY0dmdYSG8w?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 16 Nov 2026 19:11:38 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：台股ETF受益人連五周創高高息/市值人氣旺- 新聞 - MoneyDJ；國安基金護盤+利多題材台新投信：台股Q1漲升可期- 新聞 - MoneyDJ；統一證券：台股整體技術面弱勢整理- 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股ETF受益人連五周創高高息/市值人氣旺- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQVXM2RmZBRXlmNHVpUmE5bmNUT1lxZzNwT0tiVXVTcEx1Y2tGdE51ZS02OGhfdWlJSUg5ZkVjb1loU18wOHVTd3R5a2RsQlo2NTZ3R2ZURkpBWm9sUTlsVkJYRnNKYUZ4ZXN6QTlTWFhTWnRHNTlxVmVIQ0haZDJ4Nm1Sa2xvdUIta0RDSmc0bkZHdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 17 Nov 2026 02:55:00 GMT
- [國安基金護盤+利多題材台新投信：台股Q1漲升可期- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPWEN3U1JlaG5vYm1sVS1tMl9CSk1fN2JDTFN0N3hmN3MyNzRveWJKZE15aUQtYXR3THhMT0ZPYXpJT000cHZFcU82eklVVGFBMGRrS1RVX2lKdzUzTy1pbkgtSS1MZ21hQXN6enYxVUk0cFdhanNSSWRNMkNfR2s1SW5qajBfM3JWcy13bmgtZmw5UQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 17 Nov 2026 03:02:00 GMT
- [統一證券：台股整體技術面弱勢整理- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQa3AyajhYWmt4c3pLYmxKVUJBX0pDT2JNcV90cE9TMmZjdW9aalkxRWdsTzRwblA1R1FtVXVJZmwtTm13R3daQ21uTW1RQnlPaGNxY1hHdmM3WElBSU9YWlJOYXdHSlBDM01haGFuNUtROWotZkhtdGtnVktXemp6XzFQLUEzYVNJRjB5aDBPTkZfQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 17 Nov 2026 01:01:00 GMT

## 資料缺口與需人工確認

- Google News 財經來源抓取失敗：site:ctee.com.tw 台股 OR 個股 OR 產業 OR 半導體 OR 法人，原因：HTTP Error 429: Too Many Requests
- Google News 財經來源抓取失敗：site:moneydj.com 台股 OR 個股 OR 產業 OR 半導體 OR 財報 OR 營收，原因：HTTP Error 429: Too Many Requests
- Google News 財經來源抓取失敗：site:tw.stock.yahoo.com 台股 OR 個股 OR 美股 OR 半導體 OR 財報 OR 營收，原因：HTTP Error 429: Too Many Requests
- RSS 抓取失敗：https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant，原因：HTTP Error 429: Too Many Requests
- RSS 抓取失敗：https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en，原因：HTTP Error 429: Too Many Requests
- RSS 抓取失敗：https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en，原因：HTTP Error 429: Too Many Requests
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
