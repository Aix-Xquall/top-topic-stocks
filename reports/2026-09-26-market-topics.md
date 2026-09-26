# 每日股市熱門話題分析 - 2026-09-26

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **AI 伺服器與資料中心**｜正向｜熱度 18｜市場確認 74.08｜同向 6/8
2. **記憶體與 HBM 供應鏈**｜中性｜熱度 4｜市場確認 51.08｜同向 1/2
3. **半導體與晶片供應鏈**｜中性｜熱度 4｜市場確認 N/A｜同向 0/0
4. **新興題材：MarketBeat**｜負向｜熱度 1｜市場確認 0.00｜同向 0/1
5. **綜合市場情緒**｜正向｜熱度 39｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.22（樣本 11）
- 5日相關係數：0.14（樣本 7）
- 同向比例：7/11

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| AI 伺服器與資料中心 | 74.08 | 6/8 | 1 | +7.19% | +3.97% |
| 記憶體與 HBM 供應鏈 | 51.08 | 1/2 | 0 | +5.36% | +8.62% |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MarketBeat | 0.00 | 0/1 | 1 | -7.25% | N/A |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：多元產能需求 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：B907 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-09-13 | -0.42 | -0.14 | +17.65% | 17 |
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

## 歷史回測摘要

- 回測日期：2026-09-26
- 近5日 3日相關：-0.07
- 近5日 5日相關：0.16
- 同向比例：+66.67%
- 權重狀態：未調整

- 方向準確度：+66.67%
- 信心排序準確度：-0.07
- 診斷：低相關

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

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Is Now the Time to Bet on Intel’s (INTC) Server CPU Comeback and AI Ambitions? - Yahoo Finance；AMD vs. Intel: Which Artificial Intelligence (AI) Chip Stock Has More Room to Run? - fool.com；What Is Intel (INTC) Doing In Edge AI And Brain Inspired Computing? - Yahoo Finance

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.57 | +7.25% | N/A | 123.00 | 127.39 | -3.45% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.53 | +22.19% | N/A | 630.63 | 630.63 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.06 | +12.11% | +6.60% | 225.07 | 225.07 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.04 | -0.20% | +2.06% | 2,475.00 | 2,475.00 | 0.00% | 未明確 | 86.28 | 28.69 | 514.81B TWD / 53.32% | 2026-09-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | +14.64% | +4.91% | 516.17 | 516.17 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -9.37% | -21.03% | 352.81 | 446.77 | -21.03% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.04 | +5.43% | +13.84% | 699.00 | 699.00 | 0.00% | 同向 | 13.92 | 50.58 | 82.25B TWD / 45.66% | 2026-09-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.04 | +5.49% | +17.44% | 5,285.00 | 5,285.00 | 0.00% | 同向 | 60.69 | 87.28 | 64.18B TWD / 44.08% | 2026-09-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC、Intel」，共 3 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Is Now the Time to Bet on Intel’s (INTC) Server CPU Comeback and AI Ambitions? - Yahoo Finance](https://news.google.com/rss/articles/CBMikAFBVV95cUxOaFNWZjBwYjcwUlVtaHotYTFvVUNkWVp1WFY2Z1NRaU1RcGF5T1hPZzV5cGppQTE4Q0k0cUs4VE9UaXluTVdkeWVrRFZWNU13aDkzdDJVd0FJRzU1Q09QWWgzQkNTZU9WR0VlNkdfMVFSSjJPTzI2akxLN3VXdG5iT3RCck0tNjVmbU14WkZIRlM?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 25 Sep 2026 22:11:24 GMT
- [AMD vs. Intel: Which Artificial Intelligence (AI) Chip Stock Has More Room to Run? - fool.com](https://news.google.com/rss/articles/CBMivAFBVV95cUxQc1ctM2dtTkJYeUpMTC1jZjY1VkxMMFNuU1ZCcGtDeDFMTEVOR3kwdFlodmN1RGpDMzRjYXpENTZya2RJSVNLYlFTOXY1Nk85OEltd01Idmhsc0dLd0pkUnVaTlA2b1BkMFN4eU0weUJXT2NYZnE5R1A2VnZfRlhrcUNDVWpuUjMzU3gzY2s2bWhJT2hPa3FsSUZ1T2lPR1lDLXItUXRXU3JiTFAzNmlCMi1POUhNTmhPdGRlNg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 24 Sep 2026 12:02:00 GMT
- [What Is Intel (INTC) Doing In Edge AI And Brain Inspired Computing? - Yahoo Finance](https://news.google.com/rss/articles/CBMikgFBVV95cUxOaG9CSEFBRFVVd1N4NnhXcVJvZGFmVFB0U1JESzlaN3JPdEdsWmV0LW5mbE8xUnhfZWprMDZGM0tjZmVNZWx1SmZzUnFNRnB5NUlpbzhjV0llZlNyMThyY0FJSi1oRXZuRFZVUlBXbjlBV2JmV0NpYTU2LWdoUzNYUlFSUXZQalByM2xmQmNyMmh0dw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 25 Sep 2026 21:07:01 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Micron vs. Sandisk: Which AI Memory Stock Is the Better Buy? - Insider Monkey；MU, SNDK Extend Slide For A Second Day As Memory Rally Fizzles: Micron Results Next Week To Test AI Demand - Yahoo Finance；Micron Technology Inc (MU) Stock Analysis & Forecast - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.57 | +11.46% | N/A | 1,082.28 | 1,082.28 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.43 | -0.74% | +8.62% | 1,753.62 | 2,335.00 | -24.90% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +12.11% | +6.60% | 225.07 | 225.07 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、MU」，共 3 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk、SNDK」，共 2 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Micron vs. Sandisk: Which AI Memory Stock Is the Better Buy? - Insider Monkey](https://news.google.com/rss/articles/CBMiowFBVV95cUxNaFRwNEtPQ0JoamRPSFN3aGswZHVpcEx1RW5FM3dVTVdZbndUMV9yUXBKeERZQ01OOW1xOUE0SFcyMmRoQUxndDh5TTlpQ1NDa1pMRldic0hHOG9NN3NUbzFzcFhyQ003ekZZdWx3LVZtREhaSW9HWmpnOV9hYU5ETWJoYk84by01NmRJYi1KNVlZZDNBeHBkWGlUOE40NmEzQVV30gGrAUFVX3lxTFAzZVE1OElDcHROcHU2NHRBREUyQ08zNm5RcEk0T0E0dDJDZWtTemlSb0dlVm9ZSmhnay1sc0NWeUNnNTA4QmJWSS1KWDZTQU5wZzQxR2h6Vk0yeWJnQXg1LXVlTnRNc2RJRUFYV0FfZk9Md2t4TFc2dkFseFpJTXI1eUY4RnQwRmRkbkwtcUR2YnVhU05HaU1wODRpc0ZNUjhnS1BxNHZpenN6bw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 24 Sep 2026 20:31:09 GMT
- [MU, SNDK Extend Slide For A Second Day As Memory Rally Fizzles: Micron Results Next Week To Test AI Demand - Yahoo Finance](https://news.google.com/rss/articles/CBMilwFBVV95cUxPWWNBemFPQ3NaMXowZFZCWGpHTF9EQkNiSDNOZXBiUEZlUDRlajZmbUxWS2NnZ3dwVTJKa0RhTnc3UGFENk9VRUF2UWVYcUIybjlLcUNTVEMtbWFXTENuZHdvVUVHTGlqTWl2YlMzNXpOdC16czBMeWI2UTQxYlRLbzJuMEE0TFVuNy1pUmFQeExsOW16MkZB?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 24 Sep 2026 08:19:31 GMT
- [Micron Technology Inc (MU) Stock Analysis & Forecast - TradingKey](https://news.google.com/rss/articles/CBMiY0FVX3lxTFB2cjlJNEFoZnN6al9fVWlOSktTV2tWRzJ1c0c2SklreGhaeHF5VlZlSjNNRE1SaXlnaUVsQ1FaMXFtZUlvM19kUzhHdURNU1VkNmNhLTNPSDNtXzBpSHNZS0xkNA?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 25 Sep 2026 21:41:14 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Is Now the Time to Bet on Intel’s (INTC) Server CPU Comeback and AI Ambitions? - Yahoo Finance；AMD vs. Intel: Which Artificial Intelligence (AI) Chip Stock Has More Room to Run? - fool.com；林佳龍籲優化台日雙邊對話平台功能聚焦半導體| 政治 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | +7.25% | N/A | 123.00 | 127.39 | -3.45% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | +22.19% | N/A | 630.63 | 630.63 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -0.20% | +2.06% | 2,475.00 | 2,475.00 | 0.00% | 不適用 | 86.28 | 28.69 | 514.81B TWD / 53.32% | 2026-09-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | -1.91% | +4.41% | 154.00 | 164.50 | -6.38% | 不適用 | 6.68 | 23.16 | 25.04B TWD / 30.71% | 2026-09-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +12.11% | +6.60% | 225.07 | 225.07 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | +11.46% | N/A | 1,082.28 | 1,082.28 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -0.74% | +8.62% | 1,753.62 | 2,335.00 | -24.90% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -9.37% | -21.03% | 352.81 | 446.77 | -21.03% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC、Intel」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 1 篇新聞出現相關標籤。

### 主要來源

- [Is Now the Time to Bet on Intel’s (INTC) Server CPU Comeback and AI Ambitions? - Yahoo Finance](https://news.google.com/rss/articles/CBMikAFBVV95cUxOaFNWZjBwYjcwUlVtaHotYTFvVUNkWVp1WFY2Z1NRaU1RcGF5T1hPZzV5cGppQTE4Q0k0cUs4VE9UaXluTVdkeWVrRFZWNU13aDkzdDJVd0FJRzU1Q09QWWgzQkNTZU9WR0VlNkdfMVFSSjJPTzI2akxLN3VXdG5iT3RCck0tNjVmbU14WkZIRlM?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 25 Sep 2026 22:11:24 GMT
- [AMD vs. Intel: Which Artificial Intelligence (AI) Chip Stock Has More Room to Run? - fool.com](https://news.google.com/rss/articles/CBMivAFBVV95cUxQc1ctM2dtTkJYeUpMTC1jZjY1VkxMMFNuU1ZCcGtDeDFMTEVOR3kwdFlodmN1RGpDMzRjYXpENTZya2RJSVNLYlFTOXY1Nk85OEltd01Idmhsc0dLd0pkUnVaTlA2b1BkMFN4eU0weUJXT2NYZnE5R1A2VnZfRlhrcUNDVWpuUjMzU3gzY2s2bWhJT2hPa3FsSUZ1T2lPR1lDLXItUXRXU3JiTFAzNmlCMi1POUhNTmhPdGRlNg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 24 Sep 2026 12:02:00 GMT
- [林佳龍籲優化台日雙邊對話平台功能聚焦半導體| 政治 - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9IeHRfWnVqeHh4Q0pRMEJudEpRUHJNZnlYTTQ3ak8yMzhtSXVQTnRHa2F1Rm5TR2ptSmZfX3prd3FLeGRiLXJ1X21vUV9oM0NKSGZZNFNrSFhpd0xNU2xF?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 25 Sep 2026 02:41:00 GMT

## 新興題材：MarketBeat

摘要：新興題材：MarketBeat 相關新聞集中在：Intel (NASDAQ:INTC) Stock Falls 3.4% - Here's Why - MarketBeat

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.21 | +7.25% | N/A | 123.00 | 127.39 | -3.45% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel (NASDAQ:INTC) Stock Falls 3.4% - Here's Why - MarketBeat](https://news.google.com/rss/articles/CBMipAFBVV95cUxQajdwcE1NSlZ1S21YZkhYTVM3b2tTZWpsUV9xSElkc3pPYmVGUG9hanN4TUc0ZXA3QXhlUWNrR2NfcDFZbURvLXZ6N0puQk1FajJzanlQellXQ0p2dWxLSUpSMm84LUJnQk9PNzdzRHRkUW9DZzVCRGpmN3lOaEJvdTV4VTdyb0NDZDcxWHI1Vi16UEJjMFc1Mk4xbFJnNlNlN2t5Mg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 25 Sep 2026 21:22:34 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台新-五權西 對 北基(8927)個股 單一券商歷史明細 - justdata.moneydj.com；臺銀 對 逸昌(3567)個股 單一券商歷史明細 - justdata.moneydj.com；台股萬元俱樂部 四檔呼聲高 有望更上層樓 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台新-五權西 對 北基(8927)個股 單一券商歷史明細 - justdata.moneydj.com](https://news.google.com/rss/articles/CBMilgFBVV95cUxOdklOdEpJVXlFN3ExQU9rcnhwZW53QmE3dGhEYVBQRjBMd0RCVFphWEtKZjhBTmlORXlLLWZuSDlaam1XQmJfRWstZFdhWHpOZzRQc2hJaG1kY3dYdmRnQ1VrTWotS0NtbjMxVVZOLTlib1YwY1VpaHpMZ0VkaEpXQktfNUNjY2V6VUs5TXNkZUlYVVF6bmc?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 25 Sep 2026 03:12:57 GMT
- [臺銀 對 逸昌(3567)個股 單一券商歷史明細 - justdata.moneydj.com](https://news.google.com/rss/articles/CBMiggFBVV95cUxPS2dXWTZKVzVoUFF6ZWxuMkR6VmVuVU5IZmtMWm5Vcnc0RGx4dFQ3dThONk44NUxwTFplbTI1dGdXSG51RENoNEhzYnYzdnNpbHR1RHl2eXJPVld3ank1OFNWZm9qSGNEZWpUVEtpYUxVMi1pY2dTSnJEaTRUdTZGb3FB?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 25 Sep 2026 03:40:40 GMT
- [台股萬元俱樂部 四檔呼聲高 有望更上層樓 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9PZkw1VFJxVDE2dUhBZnFXcUFuOHNwOUt0SEZYNWdyeTlNdGkya1UyaHpHcHptN3R1OEtweTB3RkNyUnhhM2JuZW8wRXNCYk11RDdqTHllZjZlZ9IBX0FVX3lxTE40WGpEcXlFUVhKVnFxdU9UTkVKX0ZvQ194ZXNuR256dHl1bDdmQ2o1WF96SXVLd2VWcjJJdU9VaEF6WGNfZmVXQUhnWHJ1ajNDUjE4VGh3elp4a2VaT2M4?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 25 Sep 2026 17:42:59 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：基金-FundDJ基智網 - MoneyDJ；個股動態報導內容-003B546E-D8DB-4A9A-8AFB-6BFAFC12F567 - MoneyDJ；個股動態報導內容-97BDD1F9-5A72-497F-B907-B1E52E9ED790 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [基金-FundDJ基智網 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxOSGRxbUtWT2xybEd6VWNBTDN5UEVvM0xtWUU3TkFqRWJyUkQtQWpha3F4WmlJWFo4SHF3b09Dek5ONDVIYVdWb1c1N2xrN25Cb2FjRWRoeUdzajE4UDEyejdJQVVyTkpQUXh2UnhvQ2c3LVBGeFp1aGxNU2MzWEdZNnYzbkpYYks5aDFQSWhhNko?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 25 Sep 2026 08:33:40 GMT
- [個股動態報導內容-003B546E-D8DB-4A9A-8AFB-6BFAFC12F567 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxNb1BvT2MwVlhVdzlER2FEY0R2QnU1RE05NTRZWFg1WjRWdmNZVVV2dXpMdWdDUkg4bUNhWldfSG5mSWhzYVVRRnIxdS1XaDdlLUdFUXBHeXhqQXNIS1FVRm9vZC0tTGtjUG1pei1DZzF4S0Y1RkF1TDhGQkQxVXZVSmZ6RFc2c2FDWXhqZzBWM1FPY2VN?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 24 Sep 2026 10:56:35 GMT
- [個股動態報導內容-97BDD1F9-5A72-497F-B907-B1E52E9ED790 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxOUDlPNmc0ZGZ1NXN2UmtBdHQyR3J4blNPU3o2ZkwwdmZZMzVJZVRNekVzQjI1TS1nN1pvZ3BrSFBBbEkySS1vSjB5Tm1zekFELUFJaEZ1YUVYQk1fejdsOWttbG9yVk9UNUZHMEJNR1ZhS1hSVExabXNtbnVNVGZWMjVsMGIyVVhWTzAwVGpoSmNxdEZp?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 24 Sep 2026 10:56:34 GMT

## 新興題材：多元產能需求

摘要：新興題材：多元產能需求 相關新聞集中在：多元產能需求驅動台灣半導體廠擴大新加坡布局| 產經 - 中央社 CNA；多元產能需求驅動，台灣半導體廠擴大新加坡布局 - TechNews 科技新報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [多元產能需求驅動台灣半導體廠擴大新加坡布局| 產經 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTFBpV0pKMFlkUmQyRGZwOVloMy0yS1ZpczFyaXlBUkVmNWJyUTNsRFo0bHRsYUFucHkxNDBJM0JiVXo0TTFFcWdfb0ZlN1BwOFlSNVRyc0phZlhGZHZMRWc?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 25 Sep 2026 03:41:00 GMT
- [多元產能需求驅動，台灣半導體廠擴大新加坡布局 - TechNews 科技新報](https://news.google.com/rss/articles/CBMipwFBVV95cUxOck44SnY3bzktQWxJUW15OXpCc1U1cllib2FQYnlqQUJIdWs4MTQ0cHZmVTVybVk2eEFnYzFDQUxqamEwb1JVb043QllyZmk5TUxEOHVoUWpWLUtqa3ZVNnhFSnRJc1dNUzB0WE9wdWJUeUNrbDA1eHkwSEtfQ3hXWmtpaEJpLUt6WWF2XzFlbVhPb3ZkYzVkQnFmYWd2dWR4VFBFbFVkVQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 25 Sep 2026 04:12:52 GMT

## 新興題材：B907

摘要：新興題材：B907 相關新聞集中在：個股動態報導內容-97BDD1F9-5A72-497F-B907-B1E52E9ED790 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-97BDD1F9-5A72-497F-B907-B1E52E9ED790 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxOUDlPNmc0ZGZ1NXN2UmtBdHQyR3J4blNPU3o2ZkwwdmZZMzVJZVRNekVzQjI1TS1nN1pvZ3BrSFBBbEkySS1vSjB5Tm1zekFELUFJaEZ1YUVYQk1fejdsOWttbG9yVk9UNUZHMEJNR1ZhS1hSVExabXNtbnVNVGZWMjVsMGIyVVhWTzAwVGpoSmNxdEZp?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 24 Sep 2026 10:56:34 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
