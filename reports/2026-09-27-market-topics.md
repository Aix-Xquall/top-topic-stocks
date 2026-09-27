# 每日股市熱門話題分析 - 2026-09-27

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **AI 伺服器與資料中心**｜正向｜熱度 14｜市場確認 74.08｜同向 6/8
2. **半導體與晶片供應鏈**｜正向｜熱度 5｜市場確認 100.00｜同向 2/2
3. **新興題材：TradingKey**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0
4. **利率與成長股估值**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
5. **關稅與供應鏈轉移**｜負向｜熱度 2｜市場確認 0.00｜同向 0/2

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.11（樣本 14）
- 5日相關係數：-0.14（樣本 9）
- 同向比例：8/14

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| AI 伺服器與資料中心 | 74.08 | 6/8 | 1 | +7.19% | +3.97% |
| 半導體與晶片供應鏈 | 100.00 | 2/2 | 0 | +14.72% | N/A |
| 新興題材：TradingKey | N/A | 0/0 | 0 | N/A | N/A |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 關稅與供應鏈轉移 | 0.00 | 0/2 | 1 | -4.75% | -11.15% |
| 記憶體與 HBM 供應鏈 | 0.00 | 0/2 | 2 | -11.79% | -6.60% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-09-14 | -0.31 | -0.54 | +33.33% | 15 |
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

## 歷史回測摘要

- 回測日期：2026-09-27
- 近5日 3日相關：0.08
- 近5日 5日相關：0.47
- 同向比例：+60.00%
- 權重狀態：已調整

- 方向準確度：+60.00%
- 信心排序準確度：0.08
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

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel (INTC) Aligns Open Edge Platform With a Standardized Edge AI Ecosystem - simplywall.st；AMD, INTC Stocks Extend Rally As Meta's Muse Fuels Bets On An AI-Agent CPU Boom - Yahoo Finance；Intel Stock Soars 220%, Optimistic Outlook Ahead - Intellectia AI

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.57 | +7.25% | N/A | 123.00 | 127.39 | -3.45% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.53 | +22.19% | N/A | 630.63 | 630.63 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | +0.40 | -0.20% | +2.06% | 2,475.00 | 2,475.00 | 0.00% | 未明確 | 86.28 | 28.69 | 514.81B TWD / 53.32% | 2026-09-01 |
| NVDA 輝達 | 產業/供應鏈推估 | +0.06 | +12.11% | +6.60% | 225.07 | 225.07 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | +14.64% | +4.91% | 516.17 | 516.17 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -9.37% | -21.03% | 352.81 | 446.77 | -21.03% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.04 | +5.43% | +13.84% | 699.00 | 699.00 | 0.00% | 同向 | 13.92 | 50.58 | 82.25B TWD / 45.66% | 2026-09-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.04 | +5.49% | +17.44% | 5,285.00 | 5,285.00 | 0.00% | 同向 | 60.69 | 87.28 | 64.18B TWD / 44.08% | 2026-09-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC、Intel」，共 3 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：rally, fuels。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。 方向判斷命中詞：rally, fuels。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 同時符合主題標籤：AI, advanced packaging, CoWoS, AI server。 方向判斷命中詞：rally, fuels。

### 主要來源

- [Intel (INTC) Aligns Open Edge Platform With a Standardized Edge AI Ecosystem - simplywall.st](https://news.google.com/rss/articles/CBMiygFBVV95cUxNTVdUMHkxaGdneWpjaG1zbFdQZDFoelpMc2JOREVnLUttZ3U0VkZzQkhzQWJjOXdianJCYmVfS3lwcV9MQmxVSWIxbmNwYWo2UHRIdVhfbHItQTdsc2w1YWh3SHpKbkRBUlV6dlRIMjRNTzJoZEpJUWRRMzcyS0JvWVlLNy1PNUkyRmlmNzVObktwaHFpZXBDRThSM0JxX1pCa0h2cUJkeWVxU3Z0NGVvX1pmZEprSm55NzJsYWJNM3Z3UW5YZUhrRzdn0gHPAUFVX3lxTE9reW1CdXZ3Q21sUmhOaVFFVkVlZmI0TzJKNmdCTllWVnRrbTRTc3U5TVhxZUQ1ZnZWa293Q2Jvb0c1R0pNNXZ6eldtQWNXRlJFVXlsWndiVmtQdGsyWEpqQUVfajgtd0UyZm1FcjZOdjhhaUxETmlFelZ1UHk2Y0lDZTItUjJYa242OWVWYkNnQlVIODhnVVp4b0Fha1lPejdReGdHa0sxRlVTb0pwWVkybnNmMTJubTJmZ3FWY2NIcUN3cDlHQWFjenlZdzFyZw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 26 Sep 2026 20:47:30 GMT
- [AMD, INTC Stocks Extend Rally As Meta's Muse Fuels Bets On An AI-Agent CPU Boom - Yahoo Finance](https://news.google.com/rss/articles/CBMimAFBVV95cUxQX05pQ3M1R3JXUzZ2NFR5Q1A0RmVSWW9xN0RSVW5JN1E5bDRPeEVDeDV1RXVXTVNzUzBtd25iLWVQV09XU2QzNlZRb3NMb25lX0VrMzRNYVR4aEg3eE9mN29TczI0SThScERQWENnVi1YZkZXS1ZlRkl1b1J5UEJqcXlqLVNDTjJkT3M4N04wX1pES2hSWEVGNw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 25 Sep 2026 03:30:00 GMT
- [Intel Stock Soars 220%, Optimistic Outlook Ahead - Intellectia AI](https://news.google.com/rss/articles/CBMihwFBVV95cUxQTWJQYXZZY0hySEExZGtlQ1dlcDE0LXozOEVGdkxGeXplUEQyRmlwWjA1cnFLa0xQZDVEX1pIaTJzRHZ1aHZuOWpudE10bGp4ZFp4Y0V4TTlVaGo5cUQ1dGVLVHBZZFZqZFNDUXhOd0lZMHVfVUlMbjV6dkMxWWNKTkU3NXFCNVU?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 26 Sep 2026 11:16:12 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：AMD, INTC Stocks Extend Rally As Meta's Muse Fuels Bets On An AI-Agent CPU Boom - Yahoo Finance；林佳龍籲優化台日雙邊對話平台功能聚焦半導體| 政治 - 中央社 CNA；台股ETF績效靚半導體最猛- 日報 - 工商時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.51 | +7.25% | N/A | 123.00 | 127.39 | -3.45% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.45 | +22.19% | N/A | 630.63 | 630.63 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -0.20% | +2.06% | 2,475.00 | 2,475.00 | 0.00% | 不適用 | 86.28 | 28.69 | 514.81B TWD / 53.32% | 2026-09-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | -1.91% | +4.41% | 154.00 | 164.50 | -6.38% | 不適用 | 6.68 | 23.16 | 25.04B TWD / 30.71% | 2026-09-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +12.11% | +6.60% | 225.07 | 225.07 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | +11.46% | N/A | 1,082.28 | 1,082.28 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -5.79% | -0.78% | 1,777.80 | 2,335.00 | -23.86% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -9.37% | -21.03% | 352.81 | 446.77 | -21.03% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：rally, fuels。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：rally, fuels。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 0 篇新聞出現相關標籤。

### 主要來源

- [AMD, INTC Stocks Extend Rally As Meta's Muse Fuels Bets On An AI-Agent CPU Boom - Yahoo Finance](https://news.google.com/rss/articles/CBMimAFBVV95cUxQX05pQ3M1R3JXUzZ2NFR5Q1A0RmVSWW9xN0RSVW5JN1E5bDRPeEVDeDV1RXVXTVNzUzBtd25iLWVQV09XU2QzNlZRb3NMb25lX0VrMzRNYVR4aEg3eE9mN29TczI0SThScERQWENnVi1YZkZXS1ZlRkl1b1J5UEJqcXlqLVNDTjJkT3M4N04wX1pES2hSWEVGNw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 25 Sep 2026 03:30:00 GMT
- [林佳龍籲優化台日雙邊對話平台功能聚焦半導體| 政治 - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9IeHRfWnVqeHh4Q0pRMEJudEpRUHJNZnlYTTQ3ak8yMzhtSXVQTnRHa2F1Rm5TR2ptSmZfX3prd3FLeGRiLXJ1X21vUV9oM0NKSGZZNFNrSFhpd0xNU2xF?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 25 Sep 2026 02:41:00 GMT
- [台股ETF績效靚半導體最猛- 日報 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1aV2kwVzBfc1hCVjhxTnNfOGp0clVFVzQ5MWdkMGotZU5NTUMtOWQ5aDIwQUt2OGdUVlNWSm1EbUQtLU1kalFCV1FXNWpUSWpQNDNxWHlFYThrVDFvc2FN?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 26 Sep 2026 19:00:00 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Micron Technology Inc (MU) Stock Analysis & Forecast - TradingKey；SanDisk Corporation (SNDK) Stock Analysis & Forecast - TradingKey；SK hynix American Depositary Shares (SKHY) Stock Analysis & Forecast - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | +11.46% | N/A | 1,082.28 | 1,082.28 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | -5.79% | -0.78% | 1,777.80 | 2,335.00 | -23.86% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。

### 主要來源

- [Micron Technology Inc (MU) Stock Analysis & Forecast - TradingKey](https://news.google.com/rss/articles/CBMiY0FVX3lxTFB2cjlJNEFoZnN6al9fVWlOSktTV2tWRzJ1c0c2SklreGhaeHF5VlZlSjNNRE1SaXlnaUVsQ1FaMXFtZUlvM19kUzhHdURNU1VkNmNhLTNPSDNtXzBpSHNZS0xkNA?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 26 Sep 2026 21:23:33 GMT
- [SanDisk Corporation (SNDK) Stock Analysis & Forecast - TradingKey](https://news.google.com/rss/articles/CBMiZkFVX3lxTE9XMjJrRXVpaHc5VnJuZzRiY0pCS2lFLWx2bmZWNWJ1cE9oT3ZsN3lScEtrY2JGaGtPNWFXN2QzVkMyVmNRR3ZBcGxDczM2RmtDUGxCTXRaeHBZUXdScGo4SnVKbTdIZw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 26 Sep 2026 04:51:38 GMT
- [SK hynix American Depositary Shares (SKHY) Stock Analysis & Forecast - TradingKey](https://news.google.com/rss/articles/CBMiZkFVX3lxTE5uVVhEamUxT1BrU29xU295S3FVWG40SVY3ejMzY2k1R0ZSSUVGLUN3eEVhUVNSbW0zYWhBM0ZCVGE1NzB4QTVySUxEVHE5R3BLUUF0dFlZUGpGQzU2eU1fMTdkLWluQQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 25 Sep 2026 21:35:45 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：美股收漲！費半周線連四紅 本周緊盯通膨、就業 考驗這波漲勢動能 - 經濟日報；傳SK海力士美國子公司考慮IPO 估值上看1500億美元| 國際 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +14.64% | +4.91% | 516.17 | 516.17 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [美股收漲！費半周線連四紅 本周緊盯通膨、就業 考驗這波漲勢動能 - 經濟日報](https://news.google.com/rss/articles/CBMiYkFVX3lxTFB2OFQ3cXI2cnU5bGZheWVwMTFTbnM3aXk2UGtpYUNod3d2T2FFX2E3R3Vmdk9aTlVNeElKbXFSTGg3RG1ZU1dITEVKTFc0ZnRMQnNvMTVZSlFfNTlKV2lXSEJ30gFiQVVfeXFMUHY4VDdxcjZydTlsZmF5ZXAxMVNuczdpeTZQa2lhQ2h3d3ZPYUVfYTdHdWZ2T1pOVU14SUptcVJMaDdEbVlTV0hMRUpMVzRmdExCc28xNVlKUV81OUpXaVdIQnc?oc=5) - Google News source discovery | 經濟日報 money Sat, 26 Sep 2026 19:41:52 GMT
- [傳SK海力士美國子公司考慮IPO 估值上看1500億美元| 國際 - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5HdEJJSFh3cmFlS2gyOS0taUFYZzZubkRKVHJQUnU5QldsSWZDb0tfc25xZTg0RFVyMWtodm1pX3hGMzdPTVV0VEo1cWNZQlYtOWlFMW5XLWVmWTBkaDhB?oc=5) - Google News source discovery | 中央社財經 Sat, 26 Sep 2026 06:46:00 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：China, US agree to AI dialogue, tariff cuts on $30 billion in goods during Xi visit - reuters.com；China, U.S. agree to $30 billion tariff cut, AI dialogue during Xi visit, Beijing says - CNBC

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

- [China, US agree to AI dialogue, tariff cuts on $30 billion in goods during Xi visit - reuters.com](https://news.google.com/rss/articles/CBMisgFBVV95cUxNT2FRVWRwSDZuWUZPYTRXcmNuNTFDR0hrQkVUZnpSdV9RdGhpUjV5R0hwN2V6MUNUS2hiTHpENFhwUFVDODBIeDhBSm5SdUJOeU1qSUhjekl2RzBDd0VBYi0tdmNDblQwV1RMTF9QMGFHdlFRcDRmalE3dWlhX0l6aUJjSGtsVjlsZXNnbmZWY3JzMEtwY3hxNEZHT3JjWXJEQlVRSFpSM0haSUROOUFRaWJB?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 26 Sep 2026 19:59:32 GMT
- [China, U.S. agree to $30 billion tariff cut, AI dialogue during Xi visit, Beijing says - CNBC](https://news.google.com/rss/articles/CBMid0FVX3lxTE0xSmZMbFZYV2FMZWJqSU9PdTI4QVNrT1lKS1FkSC1BdE54ZnpzN2RMZTFTNG11TW5sZWVSeGJZblBfVi0ybkctU0VRbnllOVBISU9iOTZEbTdlam1tQXNVazNULXlIRjN2WnVsRkF6czdCWDJSMHBz0gF8QVVfeXFMT3NpeHlJU3phd3RTbTFfNUlvdDJPd2R3QXRhQnhhQ29yZnJuX0M0Q3ZKQWhSNmZyanpMQ2ZUc1RPY0VadTRNRnYtNVpra3hwUjdBTmlxMkF3RFBnampNT3BaSVpaY3V0bnprMFBMNno4WUFiQVprY3Nud1JPWQ?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 26 Sep 2026 10:58:02 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Micron Technology Inc (MU) Stock Analysis & Forecast - TradingKey；SanDisk Corporation (SNDK) Stock Analysis & Forecast - TradingKey；SK hynix American Depositary Shares (SKHY) Stock Analysis & Forecast - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | -0.28 | +11.46% | N/A | 1,082.28 | 1,082.28 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | -5.79% | -0.78% | 1,777.80 | 2,335.00 | -23.86% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | -0.21 | +12.11% | +6.60% | 225.07 | 225.07 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、美光」，共 3 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：恐。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK」，共 1 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 同時符合主題標籤：HBM。 方向判斷命中詞：恐。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Micron Technology Inc (MU) Stock Analysis & Forecast - TradingKey](https://news.google.com/rss/articles/CBMiY0FVX3lxTFB2cjlJNEFoZnN6al9fVWlOSktTV2tWRzJ1c0c2SklreGhaeHF5VlZlSjNNRE1SaXlnaUVsQ1FaMXFtZUlvM19kUzhHdURNU1VkNmNhLTNPSDNtXzBpSHNZS0xkNA?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 26 Sep 2026 21:23:33 GMT
- [SanDisk Corporation (SNDK) Stock Analysis & Forecast - TradingKey](https://news.google.com/rss/articles/CBMiZkFVX3lxTE9XMjJrRXVpaHc5VnJuZzRiY0pCS2lFLWx2bmZWNWJ1cE9oT3ZsN3lScEtrY2JGaGtPNWFXN2QzVkMyVmNRR3ZBcGxDczM2RmtDUGxCTXRaeHBZUXdScGo4SnVKbTdIZw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 26 Sep 2026 04:51:38 GMT
- [SK hynix American Depositary Shares (SKHY) Stock Analysis & Forecast - TradingKey](https://news.google.com/rss/articles/CBMiZkFVX3lxTE5uVVhEamUxT1BrU29xU295S3FVWG40SVY3ejMzY2k1R0ZSSUVGLUN3eEVhUVNSbW0zYWhBM0ZCVGE1NzB4QTVySUxEVHE5R3BLUUF0dFlZUGpGQzU2eU1fMTdkLWluQQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 25 Sep 2026 21:35:45 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：臺銀 對 逸昌(3567)個股 單一券商歷史明細 - justdata.moneydj.com；台股擂台／周冠軍「股市獲利王」何文高 本周青睞智原、嘉晶 - 經濟日報；台股擂台／挑戰者「Q女王」劉良梅 本周押環球晶、合晶 | 台股擂台 | 證券 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [臺銀 對 逸昌(3567)個股 單一券商歷史明細 - justdata.moneydj.com](https://news.google.com/rss/articles/CBMiggFBVV95cUxPS2dXWTZKVzVoUFF6ZWxuMkR6VmVuVU5IZmtMWm5Vcnc0RGx4dFQ3dThONk44NUxwTFplbTI1dGdXSG51RENoNEhzYnYzdnNpbHR1RHl2eXJPVld3ank1OFNWZm9qSGNEZWpUVEtpYUxVMi1pY2dTSnJEaTRUdTZGb3FB?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 25 Sep 2026 03:40:40 GMT
- [台股擂台／周冠軍「股市獲利王」何文高 本周青睞智原、嘉晶 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTE5tQXhaWmJIZTJuZ3E0d2t4UDhfbUpmYmRvUjI2SllYbFhSZko1TTREb1Nhb2xGcURvT196enROMTRWNk5QM3N0ZllMY3VTeGJHN01kalBuTWhBZktq?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 26 Sep 2026 18:33:23 GMT
- [台股擂台／挑戰者「Q女王」劉良梅 本周押環球晶、合晶 | 台股擂台 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTE1HMGU4WEpiTl9KWjRvQ3FBZktIZ0NYTF9aRlF1VXlvMG5jQzJMcjhaZlZfaGVjZnhjY2xVVXVLa2pFbHNZTW5Icnh2Nmc2WFJ3RmJJNUpoZlg3Qnlm?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 26 Sep 2026 18:30:50 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：台股季線轉升有望增強助漲力道- 新聞 - MoneyDJ；個股動態報導內容-DFAF2B3E-D906-4CB6-8294-989A857F2717 - MoneyDJ；謝金河：賣鏟子勝過買鏟子！台股基本面愈來愈紮實 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股季線轉升有望增強助漲力道- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMieEFVX3lxTE9QYS1HUnBZejd2WjB4VktzTjhoM05INFRZWk5BNUU1LVRsU1JnRVZHeV85SGxFb242ckJER2daQWR2bUZKb21iTnJTQ1JSTGkwVzEyRF9ySmYwblB4eXdyMHBVZy15aWp3RktKMUl5ZmljUmQwS1Y0Uw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 26 Sep 2026 01:40:00 GMT
- [個股動態報導內容-DFAF2B3E-D906-4CB6-8294-989A857F2717 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxPd09zcHJRTkVXUGoxdUVKVlRvSnBEUTczeFZIbHZqTjhCUmNuLXBjRmpaNExQTXNvcDZFRm1ja2RyWndUYmZzN29MS000cnJ5cU0wNUV2WmpveTE0aHBMbUF6QzBKR3FWT2U1ZVB2d3FIakw3MWE5UTQyVG1veGpORGJCblRXTmxMNUhmc3FRdzhMQXpu?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 25 Sep 2026 09:19:34 GMT
- [謝金河：賣鏟子勝過買鏟子！台股基本面愈來愈紮實 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxOSGRxbUtWT2xybEd6VWNBTDN5UEVvM0xtWUU3TkFqRWJyUkQtQWpha3F4WmlJWFo4SHF3b09Dek5ONDVIYVdWb1c1N2xrN25Cb2FjRWRoeUdzajE4UDEyejdJQVVyTkpQUXh2UnhvQ2c3LVBGeFp1aGxNU2MzWEdZNnYzbkpYYks5aDFQSWhhNko?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 25 Sep 2026 08:33:40 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
