# 每日股市熱門話題分析 - 2026-09-28

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜正向｜熱度 8｜市場確認 84.33｜同向 4/5
2. **新興題材：TradingKey**｜正向｜熱度 5｜市場確認 71.27｜同向 3/4
3. **AI 伺服器與資料中心**｜中性｜熱度 11｜市場確認 N/A｜同向 0/0
4. **半導體與晶片供應鏈**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0
5. **新興題材：OpenAI**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.05（樣本 11）
- 5日相關係數：-0.53（樣本 6）
- 同向比例：7/11

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 84.33 | 4/5 | 1 | +9.44% | +2.91% |
| 新興題材：TradingKey | 71.27 | 3/4 | 1 | +6.26% | +2.91% |
| AI 伺服器與資料中心 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：OpenAI | N/A | 0/0 | 0 | N/A | N/A |
| 關稅與供應鏈轉移 | 0.00 | 0/2 | 1 | -4.75% | -11.15% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 相關性偏弱；應提高同向價格確認權重，降低泛 AI、泛半導體等寬標籤推估權重。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-09-15 | -0.04 | -0.42 | +68.75% | 16 |
| 2026-09-16 | -0.19 | -0.46 | +55.56% | 9 |
| 2026-09-17 | 0.43 | -0.13 | +66.67% | 9 |
| 2026-09-18 | -0.15 | -0.07 | +35.71% | 14 |
| 2026-09-19 | 0.20 | 0.47 | +46.15% | 13 |
| 2026-09-20 | -0.04 | -0.25 | +30.77% | 13 |
| 2026-09-21 | -0.15 | -0.05 | +61.54% | 13 |
| 2026-09-22 | -0.00 | -0.01 | +88.24% | 17 |
| 2026-09-23 | 0.35 | 0.22 | +80.95% | 21 |
| 2026-09-24 | 0.05 | 0.42 | +90.00% | 10 |
| 2026-09-25 | -0.31 | 0.15 | +30.77% | 13 |
| 2026-09-26 | 0.22 | 0.14 | +63.64% | 11 |
| 2026-09-27 | 0.11 | -0.14 | +57.14% | 14 |
| 2026-09-28 | 0.05 | -0.53 | +63.64% | 11 |

## 歷史回測摘要

- 回測日期：2026-09-28
- 近5日 3日相關：0.11
- 近5日 5日相關：0.24
- 同向比例：+47.37%
- 權重狀態：未調整

- 方向準確度：+47.37%
- 信心排序準確度：0.11
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

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：INTC, AMD, MU, NVDA: Chip Stocks Tumble Again, Stalling A Nascent Rebound - Stocktwits；Micron Technology Inc (MU) Stock Analysis & Forecast - TradingKey；SanDisk Corporation (SNDK) Stock Analysis & Forecast - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.57 | +11.46% | N/A | 1,082.28 | 1,082.28 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.28 | -5.79% | -0.78% | 1,777.80 | 2,335.00 | -23.86% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.43 | +12.11% | +6.60% | 225.07 | 225.07 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.42 | +22.19% | N/A | 630.63 | 630.63 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.42 | +7.25% | N/A | 123.00 | 127.39 | -3.45% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、美光」，共 4 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK」，共 2 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVDA」，共 1 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [INTC, AMD, MU, NVDA: Chip Stocks Tumble Again, Stalling A Nascent Rebound - Stocktwits](https://news.google.com/rss/articles/CBMizAFBVV95cUxORHdiV3k3V2RtSVBoRTJaaW5PcTZhQzBTNlRUM2VqcjBpcTViNkREdS1uVGtnb1FYckxkREh4Z00zN2NBSnlNRGZ0SWhpNERydkZKTlJCejRLQ2xqejNxREhfS1ZzSm5CdjhrZzlZTnRiN1Z6M3VtSDU1d2trMG9jVFUwT3hadk93R2l0TlBBZkttekkyTDBHTW1Zc01YTmNzRVJ3Tm11dGcwNktNX04yU0pLUENBQl9sOUI4dVMydW02UUhxZDVXX2pZT0M?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 26 Sep 2026 22:33:07 GMT
- [Micron Technology Inc (MU) Stock Analysis & Forecast - TradingKey](https://news.google.com/rss/articles/CBMiY0FVX3lxTFB2cjlJNEFoZnN6al9fVWlOSktTV2tWRzJ1c0c2SklreGhaeHF5VlZlSjNNRE1SaXlnaUVsQ1FaMXFtZUlvM19kUzhHdURNU1VkNmNhLTNPSDNtXzBpSHNZS0xkNA?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 27 Sep 2026 06:02:59 GMT
- [SanDisk Corporation (SNDK) Stock Analysis & Forecast - TradingKey](https://news.google.com/rss/articles/CBMiZkFVX3lxTE9XMjJrRXVpaHc5VnJuZzRiY0pCS2lFLWx2bmZWNWJ1cE9oT3ZsN3lScEtrY2JGaGtPNWFXN2QzVkMyVmNRR3ZBcGxDczM2RmtDUGxCTXRaeHBZUXdScGo4SnVKbTdIZw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 26 Sep 2026 04:51:38 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Intel Price Forecast: Nvidia Picked Xeon 6, Invested $5B, Yet Analysts Still Trail INTC - TradingKey；Micron Technology Inc (MU) Stock Analysis & Forecast - TradingKey；SanDisk Corporation (SNDK) Stock Analysis & Forecast - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.49 | +11.46% | N/A | 1,082.28 | 1,082.28 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.24 | -5.79% | -0.78% | 1,777.80 | 2,335.00 | -23.86% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.42 | +12.11% | +6.60% | 225.07 | 225.07 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.42 | +7.25% | N/A | 123.00 | 127.39 | -3.45% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK」，共 2 篇新聞命中。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Price Forecast: Nvidia Picked Xeon 6, Invested $5B, Yet Analysts Still Trail INTC - TradingKey](https://news.google.com/rss/articles/CBMi6AFBVV95cUxPUTJ0M002eEJBWW5ocUl6ai1nTkJ1WjFMMktJRWtzekFRcktQd1d1MTFOd1RwbVFQWk9hU25UUC16RzBnbXBXdWZwcE5pS2ROeVN1YXhFZlNjVVctMWg4SWI1Y2FJazZTOTg2OVd0OWpmMGFKczk0ejdZX090Mkg2TU1Tc2Z4b2EwaUJ5MkxITm1NLWxic2JFdDVJRGZjdTBwbVNETDFURk1jMHBQN0ZQV3BhYVcyT2JDYWR2S1hLMERJNWc1bmVwODBxcUN1YUdxMlNQemdJbktvdzQxV0pmZXVIX1Zfam5N?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 27 Sep 2026 06:09:36 GMT
- [Micron Technology Inc (MU) Stock Analysis & Forecast - TradingKey](https://news.google.com/rss/articles/CBMiY0FVX3lxTFB2cjlJNEFoZnN6al9fVWlOSktTV2tWRzJ1c0c2SklreGhaeHF5VlZlSjNNRE1SaXlnaUVsQ1FaMXFtZUlvM19kUzhHdURNU1VkNmNhLTNPSDNtXzBpSHNZS0xkNA?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 27 Sep 2026 06:02:59 GMT
- [SanDisk Corporation (SNDK) Stock Analysis & Forecast - TradingKey](https://news.google.com/rss/articles/CBMiZkFVX3lxTE9XMjJrRXVpaHc5VnJuZzRiY0pCS2lFLWx2bmZWNWJ1cE9oT3ZsN3lScEtrY2JGaGtPNWFXN2QzVkMyVmNRR3ZBcGxDczM2RmtDUGxCTXRaeHBZUXdScGo4SnVKbTdIZw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 26 Sep 2026 04:51:38 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel (INTC) Aligns Open Edge Platform With a Standardized Edge AI Ecosystem - simplywall.st；Goldman Sachs Says a $7.6 Trillion AI Spending Boom Is Coming. Skip the GPUs, Follow the Money Here - 24/7 Wall St.；本地化 AI 影像模型興起，雲端運算服務商如何因應？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | +7.25% | N/A | 123.00 | 127.39 | -3.45% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +12.11% | +6.60% | 225.07 | 225.07 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | +22.19% | N/A | 630.63 | 630.63 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -0.20% | +2.06% | 2,475.00 | 2,475.00 | 0.00% | 不適用 | 86.28 | 28.69 | 514.81B TWD / 53.32% | 2026-09-01 |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +14.64% | +4.91% | 516.17 | 516.17 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -9.37% | -21.03% | 352.81 | 446.77 | -21.03% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | +5.43% | +13.84% | 699.00 | 699.00 | 0.00% | 不適用 | 13.92 | 50.58 | 82.25B TWD / 45.66% | 2026-09-01 |
| 2454 聯發科 | 產業/供應鏈推估 | 0.00 | +5.49% | +17.44% | 5,285.00 | 5,285.00 | 0.00% | 不適用 | 60.69 | 87.28 | 64.18B TWD / 44.08% | 2026-09-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel (INTC) Aligns Open Edge Platform With a Standardized Edge AI Ecosystem - simplywall.st](https://news.google.com/rss/articles/CBMiygFBVV95cUxNTVdUMHkxaGdneWpjaG1zbFdQZDFoelpMc2JOREVnLUttZ3U0VkZzQkhzQWJjOXdianJCYmVfS3lwcV9MQmxVSWIxbmNwYWo2UHRIdVhfbHItQTdsc2w1YWh3SHpKbkRBUlV6dlRIMjRNTzJoZEpJUWRRMzcyS0JvWVlLNy1PNUkyRmlmNzVObktwaHFpZXBDRThSM0JxX1pCa0h2cUJkeWVxU3Z0NGVvX1pmZEprSm55NzJsYWJNM3Z3UW5YZUhrRzdn0gHPAUFVX3lxTE9reW1CdXZ3Q21sUmhOaVFFVkVlZmI0TzJKNmdCTllWVnRrbTRTc3U5TVhxZUQ1ZnZWa293Q2Jvb0c1R0pNNXZ6eldtQWNXRlJFVXlsWndiVmtQdGsyWEpqQUVfajgtd0UyZm1FcjZOdjhhaUxETmlFelZ1UHk2Y0lDZTItUjJYa242OWVWYkNnQlVIODhnVVp4b0Fha1lPejdReGdHa0sxRlVTb0pwWVkybnNmMTJubTJmZ3FWY2NIcUN3cDlHQWFjenlZdzFyZw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 26 Sep 2026 20:47:30 GMT
- [Goldman Sachs Says a $7.6 Trillion AI Spending Boom Is Coming. Skip the GPUs, Follow the Money Here - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi1wFBVV95cUxOZGJmdGxFdXplcWpzNTk1UHlMeE84U0JxeEJNaVZfYVZqNHExUW1qX3dpMGhsY2VlVUdWOXdfdEwtWm9uWko3XzZka2JZQ3VobTJ1RVR1cXZWYm41V3k3YmZWQ3pZVnlmbWFWQlUzY0NtNUVmY2d5OEE5QnY5UWttQ2lQMDdmZ2xGdDhmUXF5ZV9zRUtHeTE1WEJWTDJjY0QxbjdvVEhGaXlJUEZaNmhDVmQ3UnhWTkpDaXZoa2hCa1JJYUtHRnNJRjdYWGhEbkRDX0YzVGJjQQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 26 Sep 2026 11:19:00 GMT
- [本地化 AI 影像模型興起，雲端運算服務商如何因應？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiakFVX3lxTE5NcXNoYXBUc2JTQ1VBdEJtcDNVeUp5MG8waDZfM3NyVV9ES2RXZTRmZDNqM2hvS2kyaXliTGhxUGRLQ1N6cVFpOHV6MEFKcXRaRjJZYU91TVVDTW5VQWVPeWxLRFdpSEQyeWc?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 27 Sep 2026 20:51:48 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：A14 製程對 AI 晶片競爭有何影響？ - TechNews 科技新報；川普組AI部隊！台灣半導體迎大單 這3檔3年績效逾300% - Yahoo股市；漲太兇反遭當沖割！「這檔半導體設備股」單周飆23%後翻黑 6千張沖成韭菜王 - Yahoo股市

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | +7.25% | N/A | 123.00 | 127.39 | -3.45% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -0.20% | +2.06% | 2,475.00 | 2,475.00 | 0.00% | 不適用 | 86.28 | 28.69 | 514.81B TWD / 53.32% | 2026-09-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | -1.91% | +4.41% | 154.00 | 164.50 | -6.38% | 不適用 | 6.68 | 23.16 | 25.04B TWD / 30.71% | 2026-09-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +12.11% | +6.60% | 225.07 | 225.07 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | +22.19% | N/A | 630.63 | 630.63 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | +11.46% | N/A | 1,082.28 | 1,082.28 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -5.79% | -0.78% | 1,777.80 | 2,335.00 | -23.86% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -9.37% | -21.03% | 352.81 | 446.77 | -21.03% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 CPU, server CPU, x86, foundry；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 0 篇新聞出現相關標籤。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 0 篇新聞出現相關標籤。

### 主要來源

- [A14 製程對 AI 晶片競爭有何影響？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMioAFBVV95cUxQS2YtRW14bkdiQ1pHcVVYMEd2UW1yMHZZWjRtNVBXNXl1U0RmaHhfVnI2MTZSWkhQTzNQRHJhb1IzVXAzay1RS0EwNV9icUw4TEwwcFZFMngtU284dUIzeDM2Tm1fWVFCaGJmYzRucmc4aE1QQXhldkE1NGVrazF4Qzdaek9lSTZBMzRsWm8zVWQ3cllXY3FIZXZBMDE2UlV3?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 27 Sep 2026 14:59:30 GMT
- [川普組AI部隊！台灣半導體迎大單 這3檔3年績效逾300% - Yahoo股市](https://news.google.com/rss/articles/CBMiywJBVV95cUxQYm5NUkl4WkJrQ2gyejNEUE9xcFNIdjU0Vmg5clB5QjhKejJHQmw5SE56Z083Zk5BRDE0R3cySlFNMU9lRTMzTkNSVUhHT3J2Ty1ad3NydmcxNkFDNEptSUp1OVNUZUIwQ0JhUGY2clZqSTBUQW5IWnlEQ21vMExjekFucGdvZ0JkT3o3eWR6U19mOFBNaFlvVGd2MU1KN3pQTS12NzZhNDZQRExSSUJJYzhKcWU3WnJfVm13RTl6Z2x5TTk5eXNJWGhONDh5UFBQNEx6eUU5TmVRRE85eTM1dE5FMTlKOXQ2SjRJSnJJa2hacndsT0tqeXhKQ2xDT3NmQlV4ZjVodFdaRjVJcFotLWxGTDlBdV8wTVlLeWVaT2FGZmdUenNqQmtxcW9OaGZsWGREdkhjYU9WQjFGcW5jM29uRXowR0JZb2tr?oc=5) - Google News source discovery | Yahoo 奇摩股市 Sun, 27 Sep 2026 20:30:00 GMT
- [漲太兇反遭當沖割！「這檔半導體設備股」單周飆23%後翻黑 6千張沖成韭菜王 - Yahoo股市](https://news.google.com/rss/articles/CBMiwANBVV95cUxNRWRIbk1mb21janhaaGFvY3RYNFg0TWpJZ0Fqd1ZTMWFhcDZ1cV9IZnhPa0wwWVhFZm1YWXJoWG16dkFRRUpkcTExNWxUSU5OeTJQaWs3ZzdOT2xBcWcxRXlHMHNScTJfRFpPX2I2dE5oVmhRRDZKLVFabm9HU3RuLXdJQXNwZnlHN3ZDa1UwX01CRXNxZ1Q3TDlmc2xkYVFFNmFQZXZGdjl4S1dfaEdmMXNvbXFWVFNWOFpCUEgwaFRPLVlTa2tnZ09USWQ3ZHE3QW1BczVaSGFHV2VRN3lnTmNLczY1UUl2ZTVUSk80amREUEUxem9jSUZPSldqV2lfcDBuVlFPUXJHN25WNFJYTE5xcTItWEVYemlqcXpWYWNXM19xRXNKTWpyMjBwNkhUYnRiMEtEenNZcVBXRVd3eWs5eFVjeXBwbVo4ek1OamgtcG9sMkU4Q3lSR1hDM1BXVEp0QnMyOU5CRnZ2U1NuUGo5UmRwckxmYlJHWktsMWVDcVdCZEFrOGdMamVpXzRlMncyZVZXNFR4R0VlVjh6aDZrbzZneUZYakNQWjNneWpFcTBHWTc2NGpkeUM5VUxJ?oc=5) - Google News source discovery | Yahoo 奇摩股市 Sun, 27 Sep 2026 13:00:00 GMT

## 新興題材：OpenAI

摘要：新興題材：OpenAI 相關新聞集中在：OpenAI, Anthropic CEOs called to appear at Australian AI probe - Reuters；EXCLUSIVE: OpenAI works to understand full scope of agent activity as user data leak emerges - Reuters

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 新聞直接提及 | 0.00 | +14.64% | +4.91% | 516.17 | 516.17 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：新聞直接提及「OpenAI」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [OpenAI, Anthropic CEOs called to appear at Australian AI probe - Reuters](https://news.google.com/rss/articles/CBMirAFBVV95cUxPMkgwZG5VR01rUjNsZkNPUkw1TFNEYTY1TGtCa010MUlRVzE2Vy1qaTBMNnJiYXliYlY1MkJONXpValJTRTdQLVNjazhJbGc1RDNVMDdTNU9WZXd3elhRVVBZNEFZLTBER2VfVkdxUW13YXprcnJKc1NjcmFwS0FYRlZYTWtZZWNQQ0pJV3JjVWFkUDZHZDNOT01FSVJOaDZLUU1wa1BFdDZpU2hZ?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 27 Sep 2026 04:27:00 GMT
- [EXCLUSIVE: OpenAI works to understand full scope of agent activity as user data leak emerges - Reuters](https://news.google.com/rss/articles/CBMitAFBVV95cUxQZUEtbWlTaWtWX0dYU2dvc0dCT3c4TW8wQS1nOWFVUWp4NU1nNFVxZXMybmhIWTlLVWlUalRVVk5JUVNrdVRfQVVRTlVtNWtwTndFTWlpOEZ1WW9OZi1peUNJNFZMRHdVWXQ1VkhNNkxkS1dVNjFNWGtPenNtYjJyVkdnZzF1ZXNzUWsxbjlPbm5EcDNTVkdaYkN6ckdlTkRrTmJqWUFQOXUtVTJTWGVTYnZlUzM?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 26 Sep 2026 01:49:56 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：China, US agree to AI dialogue, tariff cuts on $30 billion in goods during Xi visit - Reuters；China, U.S. agree to $30 billion tariff cut, AI dialogue during Xi visit, Beijing says - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AAPL 蘋果 | 產業/供應鏈推估 | -0.04 | +9.30% | +22.31% | 341.07 | 341.07 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | -0.06 | +0.20% | 0.00% | 250.50 | 289.00 | -13.32% | 未明確 | 15.21 | 16.51 | 921.77B TWD / 51.98% | 2026-09-01 |

關聯理由（前 3）：
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 2 篇新聞出現相關標籤。 方向判斷命中詞：cut。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 2 篇新聞出現相關標籤。 方向判斷命中詞：cut。

### 主要來源

- [China, US agree to AI dialogue, tariff cuts on $30 billion in goods during Xi visit - Reuters](https://news.google.com/rss/articles/CBMisgFBVV95cUxNT2FRVWRwSDZuWUZPYTRXcmNuNTFDR0hrQkVUZnpSdV9RdGhpUjV5R0hwN2V6MUNUS2hiTHpENFhwUFVDODBIeDhBSm5SdUJOeU1qSUhjekl2RzBDd0VBYi0tdmNDblQwV1RMTF9QMGFHdlFRcDRmalE3dWlhX0l6aUJjSGtsVjlsZXNnbmZWY3JzMEtwY3hxNEZHT3JjWXJEQlVRSFpSM0haSUROOUFRaWJB?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 26 Sep 2026 19:59:32 GMT
- [China, U.S. agree to $30 billion tariff cut, AI dialogue during Xi visit, Beijing says - CNBC](https://news.google.com/rss/articles/CBMid0FVX3lxTE0xSmZMbFZYV2FMZWJqSU9PdTI4QVNrT1lKS1FkSC1BdE54ZnpzN2RMZTFTNG11TW5sZWVSeGJZblBfVi0ybkctU0VRbnllOVBISU9iOTZEbTdlam1tQXNVazNULXlIRjN2WnVsRkF6czdCWDJSMHBz0gF8QVVfeXFMT3NpeHlJU3phd3RTbTFfNUlvdDJPd2R3QXRhQnhhQ29yZnJuX0M0Q3ZKQWhSNmZyanpMQ2ZUc1RPY0VadTRNRnYtNVpra3hwUjdBTmlxMkF3RFBnampNT3BaSVpaY3V0bnprMFBMNno4WUFiQVprY3Nud1JPWQ?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 26 Sep 2026 10:58:02 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：個股動態報導內容-C9F44766-304A-4A2B-BED8-D4047E035CF5 - concords.moneydj.com；台股季底作帳最後衝刺 投信鎖碼股預料成本周領漲焦點 | 市場焦點 | 證券 - 經濟日報；台股 RWA 代幣境外搶商機 鏈上投資可為股市帶進更多資金活水 | 金融脈動 | 金融 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-C9F44766-304A-4A2B-BED8-D4047E035CF5 - concords.moneydj.com](https://news.google.com/rss/articles/CBMilAFBVV95cUxQRHhEb3B1QnM0SU0xTkhwMGZNSzFoZEgtdXdtc1JYZWFsZmFlczByZHBRbGJpNWVrY1k0Y0JnTm5XcTFSM2hlaG01T0RJTmladlpCVVU1UzR0ZF9GQjAwb2hsRDFoTUZMMDVZSFVYTVZRb19nOWJXVmJoSzNlM1JqczlKTnZ1Y2xjUFlKQ05ZT1JGWERw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 26 Sep 2026 23:42:13 GMT
- [台股季底作帳最後衝刺 投信鎖碼股預料成本周領漲焦點 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE16cU96ZVBDUXM3TGVEMGU0UXpka0xmcVFoek9DRFZ0MEpuTW95TGpycmRiLTRvUXlrSmtqUHl4bGtUekQ0VXhvVVplRkF3Q1NneE96MlJGLXREUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 26 Sep 2026 09:00:00 GMT
- [台股 RWA 代幣境外搶商機 鏈上投資可為股市帶進更多資金活水 | 金融脈動 | 金融 - 經濟日報](https://news.google.com/rss/articles/CBMidEFVX3lxTE9oc0lRYlk4YWIzTHNFV3c4UWhESTRxLVdnXzBqVEFGN1ZpdUpuX2xkSzQxOEltYXp1dzhYMEFNV1JDYS1Eb2RiU25renJSV3B3aXRzYXFwSHJ5Mk9xY1RHUkIwTGZFUmMxMnk3ZjFyeEhDUG9L?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 27 Sep 2026 16:59:23 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：台股季線轉升有望增強助漲力道- 新聞 - MoneyDJ；台灣境外基金-安聯亞洲半導體主動式ETF基金風險報酬 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股季線轉升有望增強助漲力道- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMieEFVX3lxTE9QYS1HUnBZejd2WjB4VktzTjhoM05INFRZWk5BNUU1LVRsU1JnRVZHeV85SGxFb242ckJER2daQWR2bUZKb21iTnJTQ1JSTGkwVzEyRF9ySmYwblB4eXdyMHBVZy15aWp3RktKMUl5ZmljUmQwS1Y0Uw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 26 Sep 2026 01:40:00 GMT
- [台灣境外基金-安聯亞洲半導體主動式ETF基金風險報酬 - MoneyDJ](https://news.google.com/rss/articles/CBMifkFVX3lxTE5xRTk5Sm9FTnNWV01xSC1ySG9IVUVMSjdac0tCR3lBbkhTN0JBSk1lck1NcS1EQmk0QjNIdDZHd3NyYWlxdWNhRXRvQnF0SUt4UnJhRWJZTGpmTjVZdEtPSWd6RENvYlozUkdQdDlTaGZMTnI5MENvd051d1hkdw?oc=5) - Google News source discovery | MoneyDJ Sun, 27 Sep 2026 15:20:49 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
