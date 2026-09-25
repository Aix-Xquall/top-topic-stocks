# 每日股市熱門話題分析 - 2026-09-25

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜正向｜熱度 6｜市場確認 88.99｜同向 2/2
2. **散熱與液冷供應鏈**｜正向｜熱度 3｜市場確認 82.30｜同向 1/1
3. **新興題材：TradingKey**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
4. **綜合市場情緒**｜負向｜熱度 43｜市場確認 0.60｜同向 0/1
5. **半導體與晶片供應鏈**｜中性｜熱度 4｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.31（樣本 13）
- 5日相關係數：0.15（樣本 10）
- 同向比例：4/13

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 88.99 | 2/2 | 0 | +6.33% | +19.51% |
| 散熱與液冷供應鏈 | 82.30 | 1/1 | 0 | +4.10% | +11.62% |
| 新興題材：TradingKey | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | 0.60 | 0/1 | 0 | +0.20% | -2.06% |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 消費電子與手機 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 0.00 | 1/8 | 6 | -7.29% | -3.73% |
| 新興題材：MoneyDJ | 0.00 | 0/1 | 0 | -0.20% | +2.06% |

### 方法調整建議

- 方向信心與股價呈負相關；應檢查正負向詞庫，並降低新聞直接提及但股價背離的權重。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-09-12 | -0.39 | 0.04 | +25.00% | 20 |
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

## 歷史回測摘要

- 回測日期：2026-09-25
- 近5日 3日相關：-0.32
- 近5日 5日相關：-0.39
- 同向比例：+10.00%
- 權重狀態：未調整

- 方向準確度：+10.00%
- 信心排序準確度：-0.32
- 診斷：方向與信心皆需修正

調整原因：近 5 日有效樣本 10 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Micron vs. Sandisk: Which AI Memory Stock Is the Better Buy? - insidermonkey.com；MU, SNDK Extend Slide For A Second Day As Memory Rally Fizzles: Micron Results Next Week To Test AI Demand - TradingView；AI Is Supercharging Memory Stocks. Are Earnings Lying? - Micron Technology (NASDAQ:MU), SanDisk (NASDAQ:S - Benzinga

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| SNDK SanDisk | 新聞直接提及 | +0.57 | +1.38% | +19.51% | 1,816.57 | 2,335.00 | -22.20% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 新聞直接提及 | +0.57 | +11.28% | N/A | 1,080.53 | 1,080.53 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +11.87% | +6.37% | 224.58 | 225.51 | -0.41% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- SNDK：新聞直接提及「SanDisk、SNDK」，共 5 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- MU：新聞直接提及「Micron、MU」，共 4 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Micron vs. Sandisk: Which AI Memory Stock Is the Better Buy? - insidermonkey.com](https://news.google.com/rss/articles/CBMiowFBVV95cUxNaFRwNEtPQ0JoamRPSFN3aGswZHVpcEx1RW5FM3dVTVdZbndUMV9yUXBKeERZQ01OOW1xOUE0SFcyMmRoQUxndDh5TTlpQ1NDa1pMRldic0hHOG9NN3NUbzFzcFhyQ003ekZZdWx3LVZtREhaSW9HWmpnOV9hYU5ETWJoYk84by01NmRJYi1KNVlZZDNBeHBkWGlUOE40NmEzQVV30gGrAUFVX3lxTFAzZVE1OElDcHROcHU2NHRBREUyQ08zNm5RcEk0T0E0dDJDZWtTemlSb0dlVm9ZSmhnay1sc0NWeUNnNTA4QmJWSS1KWDZTQU5wZzQxR2h6Vk0yeWJnQXg1LXVlTnRNc2RJRUFYV0FfZk9Md2t4TFc2dkFseFpJTXI1eUY4RnQwRmRkbkwtcUR2YnVhU05HaU1wODRpc0ZNUjhnS1BxNHZpenN6bw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 24 Sep 2026 20:31:09 GMT
- [MU, SNDK Extend Slide For A Second Day As Memory Rally Fizzles: Micron Results Next Week To Test AI Demand - TradingView](https://news.google.com/rss/articles/CBMi-AFBVV95cUxOXzNLRnFVRHNLU0M4VFhpX2g2R1pfbE1oRXR4TzJSS2llVlF4a3lhLW81ZHFJaEFJM0tjVU5oYWNFaW5fd3ZDOTBSVG1WMERyb2wzUzdTcGhIVXluajludzM4WlZfMXVzTkl4QlBQNjRMZGZwTG5IV1d0SjNMdnhaZTZmUGYzaDhwMExWcGRlV2t5ZHktUEdhQ1RxVUxGY0ZPZ2VUc3ZHMjdESFBFSGREQ0pUWlRkSUdrTjFCeXZjQ0tsdFFRZEFid180ZXpxdkNLcjNlck1wWVAxQmpmRmwtcWVicHNWZ3FlMWhpcVZjSXRMRGFleGNWdQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 24 Sep 2026 08:19:31 GMT
- [AI Is Supercharging Memory Stocks. Are Earnings Lying? - Micron Technology (NASDAQ:MU), SanDisk (NASDAQ:S - Benzinga](https://news.google.com/rss/articles/CBMijgFBVV95cUxOS1JKQnpjUDQtX19oM2VoMnFWb2hPTll1RG12N2d6bHM4bnFBNkxkWW94UGJrLVNrZFZUS2djcFZuYmFKeDJSUHVQWVBpYlBpSy1jT2dxam1ZS0lVQkJFUU9wZU9tU3Y3Z1VkOUJUOU4zS2RfMW9oMS1JQlBwaUQzZDZoRWl5NkZDcFAwQ3F3?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 23 Sep 2026 18:10:35 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：〈焦點股〉健策獲日系外資上修EPS預估 漲停飆天價6410元超車大立光 - 鉅亨網；熱門股／散熱強攻！健策漲停飆天價、富世達同創高 奇鋐漲近6% - 非凡新聞台；《熱門族群》獨霸AI晶片散熱 健策飆天價、奇鋐同樂 - 富聯網

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.51 | +4.10% | +11.62% | 3,555.00 | 3,555.00 | 0.00% | 同向 | 75.13 | 47.39 | 19.48B TWD / 54.34% | 2026-09-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐」，共 2 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：創高, 漲停。

### 主要來源

- [〈焦點股〉健策獲日系外資上修EPS預估 漲停飆天價6410元超車大立光 - 鉅亨網](https://news.google.com/rss/articles/CBMiS0FVX3lxTFBkem1xSlRqZmRFeTBkdnBaNk03aUxhRFN1aXdqVmNBQVlyNU1jWlNySENfQm9hRTZoSENWY1R0ckhEbVQwNTQ0a0d3WQ?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 23 Sep 2026 04:50:22 GMT
- [熱門股／散熱強攻！健策漲停飆天價、富世達同創高 奇鋐漲近6% - 非凡新聞台](https://news.google.com/rss/articles/CBMif0FVX3lxTE9sLXJGM0lKUUk2MzFRX2VKNEhXLU80WUVCc2tKdGhodEgyN2d3Y3ZKcEM4cF9FdkZYYzJaMmUxYmVLSHlBa2pWMXVJbm8taGZOeXlURGJWcGZRM0JoWG5LcFotR3FhaFVKWElzNGstREJONWY4alJSay1rV1R5REU?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 23 Sep 2026 04:29:58 GMT
- [《熱門族群》獨霸AI晶片散熱 健策飆天價、奇鋐同樂 - 富聯網](https://news.google.com/rss/articles/CBMijwFBVV95cUxQNTdVSDNnSkpUa2JpdW9UZlJkTk1UMUpNOU1VS0dHcXpKRklQblpIMzl2QUcwS3FwLThNbkt4Nkpsd1RTR1NnSS1tZFBIcWxJbUROMjQydjZFdldkRnpKNm5VaTZuR2NKQThnSGJWYmZTVFI3akdMdEcyZUhJZHhaNlkzR1I5b3huVzR2YjNtdw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 23 Sep 2026 02:27:00 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Intel Stock Price Forecast: INTC Nears $125, Can AI Server Demand Push Shares to $140? - TradingKey；SanDisk Corporation (SNDK) Stock Analysis & Forecast - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | +11.08% | N/A | 127.39 | 127.39 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | +1.38% | +19.51% | 1,816.57 | 2,335.00 | -22.20% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。

### 主要來源

- [Intel Stock Price Forecast: INTC Nears $125, Can AI Server Demand Push Shares to $140? - TradingKey](https://news.google.com/rss/articles/CBMiyAFBVV95cUxQZGMwenNzeUZwcFVzcllxeXl1empBT1FleElvd2pOOTdQUlhMX0lrLUJlTG40SFFvazVLOC1tSnNOZ1EyRTFIa1dzT3BGdkVMTTNlNU9vYnpFVTVlQVhGbHkwM3M4U3RQYlk3YnJfSnVqZzZDanBiV0hSb3dDNGUxMkVBNWdfOUpPYjZqenBvX3FqSTRpc3ZYeDZzaUFCV0l3Y21pNnV5Zlc3ZE0zYUFia1M5dzJneEJnZ2h2V1k1WWFPX3p5WDdyWg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 23 Sep 2026 09:03:09 GMT
- [SanDisk Corporation (SNDK) Stock Analysis & Forecast - TradingKey](https://news.google.com/rss/articles/CBMiZkFVX3lxTE9XMjJrRXVpaHc5VnJuZzRiY0pCS2lFLWx2bmZWNWJ1cE9oT3ZsN3lScEtrY2JGaGtPNWFXN2QzVkMyVmNRR3ZBcGxDczM2RmtDUGxCTXRaeHBZUXdScGo4SnVKbTdIZw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 24 Sep 2026 12:25:56 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股中小基金 搶風頭 - 經濟日報；三大法人賣超台股438.73億元 - 經濟日報；台股擂台／「華冠北極星」劉彥良 看好景碩 | 台股擂台 | 證券 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | -0.32 | -0.20% | +2.06% | 2,475.00 | 2,500.00 | -1.00% | 未明確 | 86.28 | 28.69 | 514.81B TWD / 53.32% | 2026-09-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。

### 主要來源

- [台股中小基金 搶風頭 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5YUXpZNnlNVGtCOG1uQl95NmNpZlpoTUZpbXJaWkdja0k0cU1TcnVwY1FlS0pOUWRzbGFGMkRiSkNQX2tyN1NQNDlaWDRObUlObDVFRHB6bmtCUdIBX0FVX3lxTE5fQU5hNThwc3JKQWo5YTJPMi1Gd244eU15bE1IcllyTFd1dFpYTDEtWEJjNmpkMVlVaWRVdWJnaGVYT3NESHh1eVdpN1hjZzlUOG9lazR2OV9XaUdwUWEw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 24 Sep 2026 16:55:05 GMT
- [三大法人賣超台股438.73億元 - 經濟日報](https://news.google.com/rss/articles/CBMie0FVX3lxTFBmRGZIWkFUVHNnZVA1SVI4TWpDZzN5T3pXNVVyQlo3WFpKeU45cG5nT2U1OXpBMjZydXJ6Z0VpVUQ2QThCbV9kRjBnUDlRV0ZYdG9FYmJQaFQtb01helB0SVdNZFNGMl9aZkJ3Qm9sMlBONDRZSjk0U1kxQdIBX0FVX3lxTE9uNEMxSDNKZzFjY29PUFAzbGt6Mm9lRGRZMDFwODlxemcyNGowUVVfVW85dVpRem43MDJPam0yQlphY1NRRkJ2THNyVHlsZFJtRUxIaDFqU0gxMnpYMk9n?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 24 Sep 2026 07:13:00 GMT
- [台股擂台／「華冠北極星」劉彥良 看好景碩 | 台股擂台 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTE0wMVUwTnBDRmFIZ21sclpPeW9hR2Y4R2F0ckRmdFJxWTdYQXlIeHZWWFh4dnFXNUJfVS1MZVBPNFNBdTBRb05mMmxGYUZWdjBoa2J6STUzWEtzR25H?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 24 Sep 2026 13:21:12 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：AMD vs. Intel: Which Artificial Intelligence (AI) Chip Stock Has More Room to Run? - The Motley Fool；上櫃半導體廠鑫創不堪虧損 已提交大量解僱計畫書！11/23起分批資遣員工 - tw.stock.yahoo.com；華鉬跨足半導體材料應用 展現永續競爭力 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | +11.08% | N/A | 127.39 | 127.39 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | +21.93% | N/A | 629.26 | 629.26 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -0.20% | +2.06% | 2,475.00 | 2,500.00 | -1.00% | 不適用 | 86.28 | 28.69 | 514.81B TWD / 53.32% | 2026-09-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | -1.91% | +4.41% | 154.00 | 164.50 | -6.38% | 不適用 | 6.68 | 23.16 | 25.04B TWD / 30.71% | 2026-09-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +11.87% | +6.37% | 224.58 | 225.51 | -0.41% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | +11.28% | N/A | 1,080.53 | 1,080.53 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | +1.38% | +19.51% | 1,816.57 | 2,335.00 | -22.20% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -10.00% | -21.58% | 350.36 | 446.77 | -21.58% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 1 篇新聞出現相關標籤。

### 主要來源

- [AMD vs. Intel: Which Artificial Intelligence (AI) Chip Stock Has More Room to Run? - The Motley Fool](https://news.google.com/rss/articles/CBMivAFBVV95cUxQc1ctM2dtTkJYeUpMTC1jZjY1VkxMMFNuU1ZCcGtDeDFMTEVOR3kwdFlodmN1RGpDMzRjYXpENTZya2RJSVNLYlFTOXY1Nk85OEltd01Idmhsc0dLd0pkUnVaTlA2b1BkMFN4eU0weUJXT2NYZnE5R1A2VnZfRlhrcUNDVWpuUjMzU3gzY2s2bWhJT2hPa3FsSUZ1T2lPR1lDLXItUXRXU3JiTFAzNmlCMi1POUhNTmhPdGRlNg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 24 Sep 2026 12:02:00 GMT
- [上櫃半導體廠鑫創不堪虧損 已提交大量解僱計畫書！11/23起分批資遣員工 - tw.stock.yahoo.com](https://news.google.com/rss/articles/CBMiwANBVV95cUxNSjJ0Z19uZVptQXRocENGWFBCWDN5R2JxSEdxbmJNZHROXzZJR2Vzemt0VHFwNVh2eXpfZU5UVzJTbnJLeDJrRG5zd2dRWUM5S01BYnl2dzZ4MHA1NzVlVHlVUVFRd3hYTTFTZVNucFA5Q3A1ZG9xQmRtVDk1Qkt4WlE5LWxJMGNmVHFHWG5mUGliYVUzajdvRWQ4VjFzMElDZS1Kd000dk41R2xYM0NZU1lGMzdMbDVlUm9sSWp4TXdRY1hpeDFManMySG1pQlYwUnlKVXRSckdQVlpyRWd2Z1dsd1NRbDVBcVBPcm1WR0tyeGhpdEhiYTg4WGtId0tIYURzTVUwa0pTbFhrQkVnSnAtOXNJQk0zRFFXWXFoUzNhRnJWUWpEUENqcWE2TE15emhrMm9Sb1NUd0pkOFhFeHg1aEFMTlNya1JQSl9WdVRYZEo1SDNpdGVzRDR3bWFYVmlfamVtTlpVLXl4Nms0a0NQTTBJV25ha01rZm4tc1NpZXRtY0xmZTZrVjdrQlotNWc5NFhZWVBJa1pLT0IwMkR4VWR2ZDktTDVaT1plb3dRWkxpSFk5MlVpV1JCQ1Bl?oc=5) - Google News source discovery | Yahoo 奇摩股市 Wed, 23 Sep 2026 10:33:00 GMT
- [華鉬跨足半導體材料應用 展現永續競爭力 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFA2NC1kNks1R3BwUUlZeUt0aXRQaG15dGtXOF9qQWZDSUcyaUdsYVpUMjZuU1dqbVBYaC1DcnlzZjBUQzByX2NuT3hZdlhTYnlvSjFNYm5hbTZqQdIBX0FVX3lxTE90eDJfWlZfTE5FTXJzT1FUZWFoT3JPY3MyTlRqU2dzV1lsUXM3d3FMMmd0dXFnU2ZFMXkxaXo3NEp1YjZER3NEbnRLQXpnSEhyZ0szVEpDYjFaN2NxemtB?oc=5) - Google News source discovery | 經濟日報 money Wed, 23 Sep 2026 02:13:00 GMT

## 消費電子與手機

摘要：消費電子與手機 相關新聞集中在：32 核引擎如何定義 AI 手機新標準？ - TechNews 科技新報；穿戴裝置 AI 化如何改變智慧手機的核心地位？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +7.65% | +20.47% | 335.92 | 337.02 | -0.33% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | +0.20% | 0.00% | 250.50 | 289.00 | -13.32% | 不適用 | 15.21 | 16.51 | 921.77B TWD / 51.98% | 2026-09-01 |
| 2454 聯發科 | 產業/供應鏈推估 | 0.00 | +5.49% | +17.44% | 5,285.00 | 5,285.00 | 0.00% | 不適用 | 60.69 | 87.28 | 64.18B TWD / 44.08% | 2026-09-01 |

關聯理由（前 3）：
- AAPL：產業/供應鏈推估：公司標籤符合「消費電子與手機」關鍵字 hardware, consumer electronics, smartphone；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「消費電子與手機」關鍵字 hardware, consumer electronics；其中 0 篇新聞出現相關標籤。
- 2454：產業/供應鏈推估：公司標籤符合「消費電子與手機」關鍵字 smartphone；其中 0 篇新聞出現相關標籤。

### 主要來源

- [32 核引擎如何定義 AI 手機新標準？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMilgFBVV95cUxNWmkxZEhoZGtaVnhpanpIem9JTm9GRy0zbms5MHNfVkt6UDhvejU3MmhkRkxHb05pN2gza0ZtU21vT2hNSWJTMm00N3lnMGpDSndpdHFsN19qQmF1OUFQdzh3YWxBN2xRbDN3Q3VsMWM1UHNHZEJXNjhaWFFvbGNoMlhrSk5HWlBXQnNONXFJSE9McWdLVVE?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 24 Sep 2026 20:27:19 GMT
- [穿戴裝置 AI 化如何改變智慧手機的核心地位？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMifkFVX3lxTE9zNEtEN2JvSGpoUFVxQ2NsSDNHOFJsRGlPLWNCZGZpU2wwcUQ0a1BqX2RDNDJTUEN4S2puSXlscVdDNlFSczlYeHFaWVVHUHYwSi01dFZtZXg3U2xTZmltRFVFT0RFU1pQeEVFSzdidVdhWU5SN2J0WkxxbTBpdw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 24 Sep 2026 15:10:41 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：AMD vs. Intel: Which Artificial Intelligence (AI) Chip Stock Has More Room to Run? - The Motley Fool；Meta’s AI Agents Are Putting CPUs In Data Centers, But That’s Not Bullish For Intel (INTC) - Seeking Alpha；INTC Stock Rises Premarket: Chipmaker Reportedly Plans Data Center Layoffs, Could Unveil Details At Earnings This Week - Stocktwits

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.28 | +11.08% | N/A | 127.39 | 127.39 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.27 | +21.93% | N/A | 629.26 | 629.26 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 新聞直接提及 | -0.21 | +7.65% | +20.47% | 335.92 | 337.02 | -0.33% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | -0.03 | +11.87% | +6.37% | 224.58 | 225.51 | -0.41% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.04 | -0.20% | +2.06% | 2,475.00 | 2,500.00 | -1.00% | 未明確 | 86.28 | 28.69 | 514.81B TWD / 53.32% | 2026-09-01 |
| MSFT 微軟 | 產業/供應鏈推估 | -0.02 | +10.59% | +1.20% | 497.93 | 507.29 | -1.85% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -10.00% | -21.58% | 350.36 | 446.77 | -21.58% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.02 | +5.43% | +13.84% | 699.00 | 699.00 | 0.00% | 背離 | 13.92 | 50.58 | 82.25B TWD / 45.66% | 2026-09-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel、INTC」，共 4 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：衝擊, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。 方向判斷命中詞：衝擊, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AAPL：新聞直接提及「蘋果」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AMD vs. Intel: Which Artificial Intelligence (AI) Chip Stock Has More Room to Run? - The Motley Fool](https://news.google.com/rss/articles/CBMivAFBVV95cUxQc1ctM2dtTkJYeUpMTC1jZjY1VkxMMFNuU1ZCcGtDeDFMTEVOR3kwdFlodmN1RGpDMzRjYXpENTZya2RJSVNLYlFTOXY1Nk85OEltd01Idmhsc0dLd0pkUnVaTlA2b1BkMFN4eU0weUJXT2NYZnE5R1A2VnZfRlhrcUNDVWpuUjMzU3gzY2s2bWhJT2hPa3FsSUZ1T2lPR1lDLXItUXRXU3JiTFAzNmlCMi1POUhNTmhPdGRlNg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 24 Sep 2026 12:02:00 GMT
- [Meta’s AI Agents Are Putting CPUs In Data Centers, But That’s Not Bullish For Intel (INTC) - Seeking Alpha](https://news.google.com/rss/articles/CBMivAFBVV95cUxNN195ejRqWjFRMzZ4WFM4UG9YVGF3U2NwMWlFZzctZzNjX2dBOVFFSEFpS2w3OXFLcEREUTY1MHVlOWNhVnlFQ1pRTUFQclJLMVZ3UlF2U0o2Z0dNUnJ3SVpKQnpCTHRneUFYMFZqSjllRXR1NWE2S1VaZjdPSEdHZkpFZ0l5eFNjMzEzcFZKNkF3eElqYnJySmt6M3hKY1JPeVdGb2M3MS03UGtJS0d1VWE1OFkwTjA2ZDZVTQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 24 Sep 2026 16:41:46 GMT
- [INTC Stock Rises Premarket: Chipmaker Reportedly Plans Data Center Layoffs, Could Unveil Details At Earnings This Week - Stocktwits](https://news.google.com/rss/articles/CBMijAJBVV95cUxNUU1Kei1JS1pEcGlZdDE0MEx6ejhlSEdQeUpaWW1odTk4RGpScW1ES3JyRUlKOXJPMmxmRzVvS3dDNDlRbFFNckhjbjcxYlZrdnlSVXBmaFF4Q2lFdnZ3d01pVllNU3RyTGlpN29FYXowVFRiQTBkMEZjSDMwZGZWVGRkZGVwOFpVZC1qNlhWd1M1a3hWYS1jWExZcURiTi1xZWRFWFRfVFFJeEZiOTE4MjU1WUtqcWdOYW11Rk9EQlJDVC1IMDMxUGNGQi1GUTFtN2plLUVNUDhQd3VUY3d4cnM4MnN1WUFkTU5zblgzbThCd1Myeng5cm1kNHZicDFIbVZpSHNwLVVhU0NP?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 23 Sep 2026 20:25:14 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》收跌132點、險守48K；周K連二紅- 新聞 - MoneyDJ；台股開低走弱！失守48K 加權指數一度跌逾300多點、台積電跌20元 - MoneyDJ；【台股操盤人筆記】升息落地、AI獲利接棒，台股多頭蓄勢再起 - MoneyDJ

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | +0.32 | -0.20% | +2.06% | 2,475.00 | 2,500.00 | -1.00% | 未明確 | 86.28 | 28.69 | 514.81B TWD / 53.32% | 2026-09-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。

### 主要來源

- [《台股盤後》收跌132點、險守48K；周K連二紅- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNTnZ5OHlCUWd0R1lSZlRGRUJQN1dsMTdmM1RvT092T3dYQWpOVjdSMXdyNGNwakdMdHdKOWx6dElKWHdrTGJOSVVtRFpjT1NWamN5M3dNdzFXVnFLZ3Z5TFB4dHRYR1RKdFZiTUVxWnR3azU3VXFBSndLTzdjN0xxMEdVWkZpYmRMbjFxR1VXOWt1dw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 24 Sep 2026 07:38:00 GMT
- [台股開低走弱！失守48K 加權指數一度跌逾300多點、台積電跌20元 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxORjBHaTdQN2lRTnRCSVpmWTlEU0E5OE0tWU5EUXE3TEFZRnoxSUtKSWYtR3hoajZ6WHFTcmE2Nk1WS3lnTlliR3RWcVJ0UmNsZ2ZiNlpQNnNtMExrS0YxOEcwNENoZUVzdzZmRC1UZjBiM2VvRmNGVlFnYnZZSHk4bW9kczA0Mk1IMmFoQXhKcWNkQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 24 Sep 2026 02:51:00 GMT
- [【台股操盤人筆記】升息落地、AI獲利接棒，台股多頭蓄勢再起 - MoneyDJ](https://news.google.com/rss/articles/CBMilwFBVV95cUxQWWE2VFhYSWVSUm1HWWczMUtTdjE5QllLVm5hbmI4cHFJZUVLVmNUNDI3RG53ZmxSUnBpeGRjc3BNUnZRYnh3cmtNYmVjR282RzBzSEtyOS1FZjFPVlF1cHZBbU1GVmhVVWVyaEhzTDl0YnYyQnhFeFJHNzNNN2NINzBIVVlPcGNYSWV1eWtGRC0wMmxwQXJZ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 24 Sep 2026 01:31:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
