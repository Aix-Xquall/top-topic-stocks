# 每日股市熱門話題分析 - 2026-11-07

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **AI 伺服器與資料中心**｜中性｜熱度 14｜市場確認 N/A｜同向 0/0
2. **記憶體與 HBM 供應鏈**｜中性｜熱度 6｜市場確認 N/A｜同向 0/0
3. **半導體與晶片供應鏈**｜中性｜熱度 5｜市場確認 N/A｜同向 0/0
4. **新興題材：TradingKey**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0
5. **新興題材：OpenAI**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：N/A（樣本 0）
- 5日相關係數：N/A（樣本 0）
- 同向比例：0/0

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| AI 伺服器與資料中心 | N/A | 0/0 | 0 | N/A | N/A |
| 記憶體與 HBM 供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：TradingKey | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：OpenAI | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：一度超過500檔跌停 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-10-24 | 0.09 | -0.31 | +70.00% | 20 |
| 2026-10-25 | 0.41 | 0.78 | +64.29% | 14 |
| 2026-10-26 | 0.27 | -0.25 | +36.36% | 11 |
| 2026-10-27 | 0.07 | 0.31 | +50.00% | 18 |
| 2026-10-28 | -0.30 | 0.47 | +20.00% | 15 |
| 2026-10-29 | -0.05 | 0.04 | +42.86% | 14 |
| 2026-10-30 | -0.00 | -0.05 | +47.62% | 21 |
| 2026-10-31 | 0.50 | -0.68 | +80.00% | 15 |
| 2026-11-01 | 0.47 | -0.40 | +85.71% | 14 |
| 2026-11-02 | -0.15 | -0.06 | +27.78% | 18 |
| 2026-11-03 | -0.03 | 0.08 | +40.91% | 22 |
| 2026-11-04 | -0.21 | 0.35 | +15.79% | 19 |
| 2026-11-05 | 0.13 | -0.53 | +66.67% | 12 |
| 2026-11-06 | -0.18 | 0.77 | +100.00% | 5 |

## 歷史回測摘要

- 回測日期：2026-11-07
- 近5日 3日相關：0.36
- 近5日 5日相關：-0.37
- 同向比例：+84.21%
- 權重狀態：已調整

- 方向準確度：+84.21%
- 信心排序準確度：0.36
- 診斷：正相關

調整原因：近 5 日信心分數與後續報酬呈正相關，提高市場確認、歷史題材與直接提及權重。；關鍵詞×公司後續樣本有效 4 筆，未達 30 筆，不調整樣本權重

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

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel: Floundering Without Visible AI Story (NASDAQ:INTC) - Seeking Alpha；AMD Tumbles 13%, NVIDIA Slides 7% as AI Regulation Fears Hit Chip Stocks; Intel Sinks 8% - 24/7 Wall St.；強攻 AI 與企業級市場，潘健成：群聯擺脫依賴低價庫存邁入 AI 營運收割期 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | -50.92% | +38.76% | 56.28 | 114.68 | -50.92% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | 0.00 | -18.28% | -7.03% | 186.64 | 228.38 | -18.28% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | -12.99% | N/A | 449.04 | 516.10 | -12.99% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -6.97% | -9.92% | 2,135.00 | 2,480.00 | -13.91% | 不適用 | 86.28 | 24.75 | 511.86B TWD / 54.65% | 2026-10-01 |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +17.85% | +7.85% | 530.61 | 535.93 | -0.99% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -16.37% | -24.56% | 293.69 | 446.77 | -34.26% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | -14.45% | -21.11% | 527.00 | 703.00 | -25.04% | 不適用 | 13.92 | 38.13 | 88.13B TWD / 45.52% | 2026-10-01 |
| 2454 聯發科 | 產業/供應鏈推估 | 0.00 | -7.76% | -13.41% | 3,390.00 | 4,920.00 | -31.10% | 不適用 | 60.69 | 55.99 | 55.40B TWD / 1.97% | 2026-10-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC、Intel」，共 2 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel: Floundering Without Visible AI Story (NASDAQ:INTC) - Seeking Alpha](https://news.google.com/rss/articles/CBMiiwFBVV95cUxPQ0xlMzNnV0I0VUJSbURfVU9nT3Vhd2p1a2pOZmV5V2FNeGs2N0huWHFkekhOb2tFU1BobThEYWFNQ1o1QzJYOXdmd094c0c0elFoSVo4TnZaZHFzMnpabXZLaENhSVZvdkNld3JwdVRoaDFIYWtKRDItLUZSUWlxUzYyWjdBQ1diUzZB?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 05 Nov 2026 10:07:47 GMT
- [AMD Tumbles 13%, NVIDIA Slides 7% as AI Regulation Fears Hit Chip Stocks; Intel Sinks 8% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMixgFBVV95cUxQZXpOcVdYWWIyd0ZyaldnY3QxMFJUUk14d3E0UmpWVzRwakhSOF9lOUE1azgtTmxRMm55V1JWZ24wZmhsNlVjWHBtZW1DNTJLMmFRNjd1YS0yaFJ1cUxQQVhkdU14V0Mzb1VjbFBreGpFS3FjYUdnXzd1NkVYUUlEY05uYWVJVEgxaGMzbDhzMU5rZWpmNkxqcjdBT0lLMy1kWVlhN1lhbjB2TDFEOGQ4SEJ3YXAxUnpuMi1kMy1RdkZzZVFicVE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 05 Nov 2026 15:46:00 GMT
- [強攻 AI 與企業級市場，潘健成：群聯擺脫依賴低價庫存邁入 AI 營運收割期 - TechNews 科技新報](https://news.google.com/rss/articles/CBMi9wFBVV95cUxPWnl1UVVNUV9KSUd0b0VsRDhDdGhrY3BrYlk3ZEQ5T2lwY0ZKMTZwVTRQamVhX1V0VndnUWM2UmtSTzBNMVlJYzhfOV93enA1WTc2Q2h2M1dscU5qc3NzWTd4SHh5TXkxSnpWcDRjNXJnUHRZUVlMbjZ4Z1FyS3BCZkZmd2hmaHlZcElkY09MdEZCNm84anN5WTI0NjhmVl94THl2SFg2ZV8zXzVSOEhhY3U1RDdzQTRUbW4yaFQ0TFRYRkZYWF9DeTBfam96amY4c0ZkUDFSS2U0ZTFFX3JHeXNIb3dFZDBJYzNVR2diSTBjc1lNVk4w?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 06 Nov 2026 12:53:10 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：SanDisk Surges 10%, Micron and Western Digital Jump 8% as Memory and Storage Stocks Rebound From AI Sell-Off - 24/7 Wall St.；SanDisk Slides 7%, Micron and Western Digital Fall 5% as Lawmaker's Call for AI Pause Extends Memory Rout - 24/7 Wall St.；Micron Technology Inc (MU) Stock Analysis & Forecast - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | -28.94% | N/A | 690.00 | 971.00 | -28.94% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | -24.99% | -39.37% | 806.43 | 2,335.00 | -65.46% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | 0.00 | -6.97% | -9.92% | 2,135.00 | 2,480.00 | -13.91% | 不適用 | 86.28 | 24.75 | 511.86B TWD / 54.65% | 2026-10-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -18.28% | -7.03% | 186.64 | 228.38 | -18.28% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、MU、memory」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：fall, surges。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 2 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：fall, surges。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- 2330：新聞直接提及「TSMC」，共 1 篇新聞命中。

### 主要來源

- [SanDisk Surges 10%, Micron and Western Digital Jump 8% as Memory and Storage Stocks Rebound From AI Sell-Off - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi4wFBVV95cUxPZS1YbHc4X3E2bTJFVVlNa2MxelRtN28wVVNqR0wzRXBUMXJaQTJTN3E5WTh2M3BHZllVb01pc18tOWhjbGowQlpwVmZCMWtNV3dxdDJrZE41akxCdkpNY1c4aGtpdE5MekswV21LRjV6UjNockY3Qk5hVUQ0NWVFTlB5WVUyOEplZjlCdVlQTUdZTWdJTVhZQ3VmQl92YmtzeGkwQ1JJYks0UzNUdXI4R2ZVNE1aTXV1Mm5jWTMtdjJmVmNwYkp6RGFQbUdTM1UyZW5wbzRaRmc0WEN5eW1vRXpacw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 06 Nov 2026 14:08:00 GMT
- [SanDisk Slides 7%, Micron and Western Digital Fall 5% as Lawmaker's Call for AI Pause Extends Memory Rout - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi3gFBVV95cUxPVllxRm9UQlBHNkl1Q1l6TDFvV3lFVGVDcUtNdkZrMF9yTnR6UE1TTGh3SEpUM3VKX1l1YzRxUkh6aTRpem9tQlNHQmtXWEQ1cWVaM0k1djdYcVJadENkTjZnN2ZOYjNiZXE1MERib3FxSmRiSDFhOUNVYTlPWUd3czIxajh0SDVmZWR0bWZ0cVJtc0Z5OXQ1SVZzQXdhSF9MZTJvQzU0UF9XNWJRaHIwaFRaa3VSQnRqX2hKd09VYTJ5Q3pLcDdreDNqV0pPWkVGejNzTzJXbFA2ZFNhQUE?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 05 Nov 2026 13:47:00 GMT
- [Micron Technology Inc (MU) Stock Analysis & Forecast - TradingKey](https://news.google.com/rss/articles/CBMiY0FVX3lxTFB2cjlJNEFoZnN6al9fVWlOSktTV2tWRzJ1c0c2SklreGhaeHF5VlZlSjNNRE1SaXlnaUVsQ1FaMXFtZUlvM19kUzhHdURNU1VkNmNhLTNPSDNtXzBpSHNZS0xkNA?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 05 Nov 2026 00:14:52 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：AMD Jumps 8%, Intel and NVIDIA Climb 5% as Chip Stocks Rebound From Worst Sell-Off Since 2020 - 24/7 Wall St.；AMD Tumbles 13%, NVIDIA Slides 7% as AI Regulation Fears Hit Chip Stocks; Intel Sinks 8% - 24/7 Wall St.；〈美股盤後〉晶片股反彈！費半勁揚逾4.2% 台積電ADR升超6% 那指標普周線四連黑 - Yahoo股市

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | -50.92% | +38.76% | 56.28 | 114.68 | -50.92% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | 0.00 | -6.97% | -9.92% | 2,135.00 | 2,480.00 | -13.91% | 不適用 | 86.28 | 24.75 | 511.86B TWD / 54.65% | 2026-10-01 |
| NVDA 輝達 | 新聞直接提及 | 0.00 | -18.28% | -7.03% | 186.64 | 228.38 | -18.28% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | -12.99% | N/A | 449.04 | 516.10 | -12.99% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | -10.68% | -17.49% | 92.00 | 164.50 | -44.07% | 不適用 | 6.80 | 13.59 | 25.20B TWD / 18.33% | 2026-11-01 |
| MU 美光 | 產業/供應鏈推估 | 0.00 | -28.94% | N/A | 690.00 | 971.00 | -28.94% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -24.99% | -39.37% | 806.43 | 2,335.00 | -65.46% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -16.37% | -24.56% | 293.69 | 446.77 | -34.26% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「台積電」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip, foundry。
- NVDA：新聞直接提及「NVIDIA」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AMD Jumps 8%, Intel and NVIDIA Climb 5% as Chip Stocks Rebound From Worst Sell-Off Since 2020 - 24/7 Wall St.](https://news.google.com/rss/articles/CBMizwFBVV95cUxPa01iWmYtRkh1S3plOXhjRGlOVGg1RzZfUS1yRzA3REs1MTFmb0NYQWJRYmNWSlRVYjlnV1hnMm5IT0d6YXFrUDRhWG94UG81TEJ0OVAwSzJ3TzRha3hESW5hSS1hXzA0cm9VV0ZVV1NoZFdSTGdDc3lTaG1wOEV2YkdUYjFkclpkbk1sQmkzYXBHNHBIUkdXb2NEMkkwcWNya2t5WkdXZWtFN2ZBWDFiZlkwd3VXd0ozcExtZ29kZGQzOWl3YWg1YmM0dkVZSTQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 06 Nov 2026 14:05:00 GMT
- [AMD Tumbles 13%, NVIDIA Slides 7% as AI Regulation Fears Hit Chip Stocks; Intel Sinks 8% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMixgFBVV95cUxQZXpOcVdYWWIyd0ZyaldnY3QxMFJUUk14d3E0UmpWVzRwakhSOF9lOUE1azgtTmxRMm55V1JWZ24wZmhsNlVjWHBtZW1DNTJLMmFRNjd1YS0yaFJ1cUxQQVhkdU14V0Mzb1VjbFBreGpFS3FjYUdnXzd1NkVYUUlEY05uYWVJVEgxaGMzbDhzMU5rZWpmNkxqcjdBT0lLMy1kWVlhN1lhbjB2TDFEOGQ4SEJ3YXAxUnpuMi1kMy1RdkZzZVFicVE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 05 Nov 2026 15:46:00 GMT
- [〈美股盤後〉晶片股反彈！費半勁揚逾4.2% 台積電ADR升超6% 那指標普周線四連黑 - Yahoo股市](https://news.google.com/rss/articles/CBMizAJBVV95cUxOOXF4Y0pkbERadVRfU3ZjWU42WGJGTDlZa01vWmhXZEJhY0wzNVFEbjl0bkZOcWthMnAwazYzZE5zWGdSZTcyN0hXa0thVlFzd1ZjZjN4YVRBYmNBem9WbmtIRm44dElLaEx5b0VnaEVET0xXUTRiSl9BWVNMYzFUNDNMbXRqdU5NSm81eDVvSFFBOW1oOGF0YnpxX3NhQTBqWXc1R29lR0hjRDgzZl9Sam1IMGg3bHRGczBLVG9tY29BUWY5MnNrYk1RU3NqTDFJRV9RdXN1Q3BpeUVsUTQxYUdFRWxleWtjaVVmTy1HeUJWSGNvWHB0VXRHZTdKTHlLMk1idXpMSG5xdWRKNmppQ1h4WVRqa0kxMndyWHk0YzNsakRDSkhVdE1vandvOVlNbm1PWkZXcUJKb0xjRzVYY0FHdExlaEFzU2MtWQ?oc=5) - Google News source discovery | Yahoo 奇摩股市 Fri, 06 Nov 2026 21:52:24 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Micron Technology Inc (MU) Stock Analysis & Forecast - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | -28.94% | N/A | 690.00 | 971.00 | -28.94% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Micron Technology Inc (MU) Stock Analysis & Forecast - TradingKey](https://news.google.com/rss/articles/CBMiY0FVX3lxTFB2cjlJNEFoZnN6al9fVWlOSktTV2tWRzJ1c0c2SklreGhaeHF5VlZlSjNNRE1SaXlnaUVsQ1FaMXFtZUlvM19kUzhHdURNU1VkNmNhLTNPSDNtXzBpSHNZS0xkNA?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 05 Nov 2026 00:14:52 GMT

## 新興題材：OpenAI

摘要：新興題材：OpenAI 相關新聞集中在：OpenAI, Arm and Qualcomm executives react to post-midterm AI sell-off - CNBC；OpenAI investing in AI data centers despite election results, CFO says - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 新聞直接提及 | 0.00 | +17.85% | +7.85% | 530.61 | 535.93 | -0.99% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：新聞直接提及「OpenAI」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [OpenAI, Arm and Qualcomm executives react to post-midterm AI sell-off - CNBC](https://news.google.com/rss/articles/CBMijAFBVV95cUxQdE1TbUF3dUNNZjVhZlhtOEhPOVRVbkYwV25tWXZzY1Q0LTdfV3pKOTg4bkpBZ3QwaFhlUS1LRjJHczMzelRQRFlFQWtwQlhxaDV3NHVHX2FsVzJ1eXVxR0VBLVBUUllyek1OLXZUNk5wZGxzM1Y2bnA1MGJEanV1MFFqS2ZjUl8wY25kaQ?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 06 Nov 2026 18:27:19 GMT
- [OpenAI investing in AI data centers despite election results, CFO says - CNBC](https://news.google.com/rss/articles/CBMidEFVX3lxTE54bWpvVi13alRsTVY0VGFfT0dUS3JtMG4yYVZtNDhkN2lIUndZeFVvVEdwZExsNjNPeXR1aEVVZzNSZjlBS1lSdUdoeUg4RmpWc3VqcDREUzA0RGlxZ2kzaC1KYVNzX3pxTlBLSGJtUlA0LUVq?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 06 Nov 2026 16:22:49 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：國安基金出手了！台股盤中狂瀉3,737點 第10度進場護盤救市 - 經濟日報；台股狂殺逾3千點 國安基金：崩跌影響很多人、不排除召開臨時會 - 經濟日報；台股寫史上盤中最大、收盤第四大跌點！三大法人賣超卻收斂至1,140億元 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [國安基金出手了！台股盤中狂瀉3,737點 第10度進場護盤救市 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE02VnpuMXdSbm8yUTJxTFBPM3hDWlp6SWdKVHc1cGZYMm9kMl8yblVETTJoNVFrU3pkWVN2VmVvcmQzTlpjWVVVN0Z6MVlaTjdkaTRITlN3Z3B6d9IBX0FVX3lxTE53aElVRTE2dF8zSkY2TWFNbGxmOEVTVzZhWlVnLUpwYk1YMktveFp2SnktcFdpQVkyRmo4Y2NFd0FWQWRGWU84SUx1Y1lDeVhyRldiLXVDTjdYVzBLZFNZ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 06 Nov 2026 09:55:14 GMT
- [台股狂殺逾3千點 國安基金：崩跌影響很多人、不排除召開臨時會 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9QTmwtNTZ5ckFReU1uc01menAtZFBwek9DdUFacy11RE1rRXVyZWhOdF9fZWU3WVpWTkVyUHF4TkhkNnNld2RBUDBKZXlUSW5FU3kwUzlmQy1LUdIBX0FVX3lxTE1UVTJaSEtzd3NhMmxRZHNNNnlPX04yWjFfZUhOc0FvZzY0eUhSdF9JajNRX2h5LVZSOGZLc3U5cWpFTmRTLXpub2lzd2hKLWR0cWF2SGhMOTRJODA4TEY4?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 06 Nov 2026 02:10:41 GMT
- [台股寫史上盤中最大、收盤第四大跌點！三大法人賣超卻收斂至1,140億元 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE8xdVd1UmFnZlF6YVZSaGt4dHpXaWZBWG15Tkt1OHBDbjRUSF9vMHl6WHFXazZ5Znh2U045clJrSWN0VWFJaUl0TzJGQ2NrUGxfTlk2c2x5UXJEQdIBX0FVX3lxTFBDTE52QnN1RC0xVUhidnpvLWczV01Ea0RHY3BXSF8tSXdDV01JMngtR05xTFZpUWNiQmdjRTB6OEZaVGpsbkhRS0V0aDlzVW1wQ2Y0R3RKQUlUSUJEamQw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 05 Nov 2026 23:00:00 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》重挫1873點、年線失而復得；週K連四黑- 新聞 - MoneyDJ；台股崩跌賴總統籲勿恐慌/適時推政策助市場穩定- 新聞 - MoneyDJ；國際股市影響，10月外資淨匯出/台股賣超寫同期高- 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》重挫1873點、年線失而復得；週K連四黑- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxOR2VIYW1GU0hwQ21wZkV4NzN6TzhRQ2pQaDNyNVNLLVNZLTdjVHdBMmNtT3BhMUlVLUFJU3JrMmp1ZHRkaEVlTDBrYXpTeGhFRVBMeW5ERmd0eGRqNUFiOU1MRkF2ckRITEVSMDFjUkJQUjB4elZ3Q0hCQWo4NDV5Q2o1dTkwTGpWMUFnRnR2LVRrQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 06 Nov 2026 08:09:00 GMT
- [台股崩跌賴總統籲勿恐慌/適時推政策助市場穩定- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQR2tpZFcwOGNCamVxUWpCaG5maEMyWC1EQTM5MHVPOGc3em9vcFZweDl5U04ta0huNzltZVBVdC14bGtPWDV1YjV4aFJfZXktQ0tmalB4VkduWXVvdUxpbVowQVJvT3o0ZUtOc193NnJpVy12RVVJSGE1RmhBNTRKT0lEQjQ1Y2REOWgxWkZHYUQzUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 06 Nov 2026 04:34:00 GMT
- [國際股市影響，10月外資淨匯出/台股賣超寫同期高- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQZGNiWTRWRmFjLVhBbXZiX09PUE9oRXZwV0ZfcW01R3N5THZIWWlzWW5oUk5lY1lxZ25LQ2ZBc1pQZE5MYXRVNGxYYXVsN1NyaU5vbHVUOER2OHZUSElfLU9aZmhCbnd1S0NvWnlROTl0dmNPR3JuczRzVUVSdUtob09ydXhfOUEzMTluVWJXY3gyZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 05 Nov 2026 21:16:00 GMT

## 新興題材：一度超過500檔跌停

摘要：新興題材：一度超過500檔跌停 相關新聞集中在：台股史詩級崩跌！開低暴殺3,737點摜破年線 一度超過500檔跌停 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股史詩級崩跌！開低暴殺3,737點摜破年線 一度超過500檔跌停 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9qbks0cThWXzNndkxpMHRtdTBpYldfR2J5VTNIN1JGaWw3My02a2pBSmxjUVpyYTlzM2RtNTlWdXNoLUc1VUh3LXlFb2xsNGZpOGwzQlpzWXhaZ9IBX0FVX3lxTE4tUnBGZHBkbzdBMkE2eE5RakF0QkJTZmlJOVR4X2xFNDloQlNMUTd0NVE4enV2X2NDaUNNai1Fd2pzV0RyUjNxRlh6N05JSExQS2VpRTRFYUFTMVFnX3ZZ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 05 Nov 2026 08:00:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
