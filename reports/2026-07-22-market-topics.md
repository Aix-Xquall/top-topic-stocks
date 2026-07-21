# 每日股市熱門話題分析 - 2026-07-22

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **AI 伺服器與資料中心**｜中性｜熱度 12｜市場確認 N/A｜同向 0/0
2. **記憶體與 HBM 供應鏈**｜中性｜熱度 6｜市場確認 N/A｜同向 0/0
3. **關稅與供應鏈轉移**｜負向｜熱度 2｜市場確認 N/A｜同向 0/0
4. **半導體與晶片供應鏈**｜正向｜熱度 10｜市場確認 1.38｜同向 1/5
5. **散熱與液冷供應鏈**｜負向｜熱度 2｜市場確認 0.00｜同向 0/1

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.33（樣本 6）
- 5日相關係數：-0.15（樣本 6）
- 同向比例：1/6

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| AI 伺服器與資料中心 | N/A | 0/0 | 0 | N/A | N/A |
| 記憶體與 HBM 供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 關稅與供應鏈轉移 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | 1.38 | 1/5 | 4 | -4.21% | +4.56% |
| 散熱與液冷供應鏈 | 0.00 | 0/1 | 1 | -4.27% | -9.43% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：SpaceX | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-07-09 | -0.11 | -0.36 | +64.29% | 14 |
| 2026-07-10 | 0.55 | 0.05 | +77.78% | 9 |
| 2026-07-11 | 0.13 | -0.08 | +50.00% | 12 |
| 2026-07-12 | 0.27 | 0.13 | +16.67% | 12 |
| 2026-07-13 | 0.39 | -0.09 | +15.38% | 13 |
| 2026-07-14 | 0.10 | -0.07 | +21.43% | 14 |
| 2026-07-15 | 0.20 | -0.16 | +28.57% | 7 |
| 2026-07-16 | 0.20 | 0.02 | +33.33% | 12 |
| 2026-07-17 | 0.36 | 0.02 | +60.00% | 15 |
| 2026-07-18 | 0.18 | 0.08 | +53.85% | 13 |
| 2026-07-19 | 0.37 | 0.09 | +12.50% | 16 |
| 2026-07-20 | -0.59 | 0.11 | +45.45% | 11 |
| 2026-07-21 | -0.12 | -0.03 | +12.50% | 8 |
| 2026-07-22 | -0.33 | -0.15 | +16.67% | 6 |

## 歷史回測摘要

- 回測日期：2026-07-22
- 近5日 3日相關：N/A
- 近5日 5日相關：N/A
- 同向比例：+100.00%
- 權重狀態：未調整

- 方向準確度：+100.00%
- 信心排序準確度：N/A
- 診斷：樣本不足

調整原因：近 5 日有效樣本 4 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：AI 伺服器與資料中心 相關新聞集中在：Is Intel (INTC) Still Cheap Following AI Partnerships And Earnings Optimism? - Yahoo Finance；Intel Launches Fresh Layoffs in Data Center and AI Unit Ahead of Earnings as Lip-Bu Tan Pushes Turnaround Strategy - Benzinga；越錯越自信？研究揭 AI 讓人失去說「不知道」的能力，正確率狂跌仍深信不疑 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 105.45 | 114.68 | -8.05% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -1.82% | +18.86% | 207.29 | 211.14 | -1.82% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 544.43 | 544.43 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -2.43% | -0.41% | 2,410.00 | 2,410.00 | 0.00% | 不適用 | 74.39 | 32.40 | 442.68B TWD / 67.87% | 2026-07-01 |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +1.28% | -21.50% | 397.75 | 506.69 | -21.50% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -13.49% | +24.87% | 386.50 | 446.77 | -13.49% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | -7.18% | -1.25% | 633.00 | 680.00 | -6.91% | 不適用 | 10.86 | 58.77 | 65.78B TWD / 32.86% | 2026-07-01 |
| 2454 聯發科 | 產業/供應鏈推估 | 0.00 | -0.81% | +0.27% | 3,670.00 | 4,310.00 | -14.85% | 不適用 | 62.91 | 58.49 | 58.01B TWD / 2.80% | 2026-07-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC、Intel」，共 2 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Is Intel (INTC) Still Cheap Following AI Partnerships And Earnings Optimism? - Yahoo Finance](https://news.google.com/rss/articles/CBMingFBVV95cUxPZEdHMkZGX05CeTFEeDY5Ukludl9qbDVPUFlrbUxtSUt6X2d3cnJpZnJHR2NsUVJlRGZIX3lsZ0VScVVHX0g2aTM0Qk5hclNSQ3BfWkllYUFTalBlSEdncGNFQTRqNjE2Y21JQkkxXzZFSndCa2c0WmFkV1oyVmFCaWlWZERNdTh3NDY4dHNkOFVBczF1WllmTDQzT1JXdw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 21 Jul 2026 14:08:11 GMT
- [Intel Launches Fresh Layoffs in Data Center and AI Unit Ahead of Earnings as Lip-Bu Tan Pushes Turnaround Strategy - Benzinga](https://news.google.com/rss/articles/CBMimwFBVV95cUxQVUNLYWFWSUpFY3NkOVRadzZIeUFjUWhKRjZxbXFCOHJUc1p4TWw1ZnYwb1gzWmJJdG5vTU1raVBUOE1UTTgzcV8xbk9zY2M4bUdkU2hFUUV0cGlzc3F5aGpVdkZJUm5YcENZYW5raTJuREJUOWtUZHFLRVgzUDFDQ3YyV2RrTHl2Mmo5WFNNSXI3LUJsbmVLcnpzVQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 21 Jul 2026 03:33:06 GMT
- [越錯越自信？研究揭 AI 讓人失去說「不知道」的能力，正確率狂跌仍深信不疑 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiigFBVV95cUxQdnpQMWRnZVZQNnl0dHk1MjFmVVl5UUE1bTZub01YRXBRMnF2ZGVHZHl5V2pIT1g0bGtUYU5tS0x5X05falozNWQ1SDdKa29Td2VRUDBtVmxvY0tzeFdPZldXS3JpcnZSbzdYaGNFZFh0cWc4Qk9YVDJseG9RY2FFTXMyVFp4OU9OZHc?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 20 Jul 2026 23:42:59 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：SanDisk Rises 8%, Western Digital Jumps 9%, Micron Adds 7% as Memory Rebound Accelerates - 24/7 Wall St.；What Just Happened To AI Stocks? (Micron, AMD & Nvidia Explained) Tampa Bay Rays (R1YP3IyRnV) - Mshale；Micron stock up 3%, SanDisk gains 2.5%: what woke the memory trade? - Invezz

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 970.82 | 971.00 | -0.02% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | +12.64% | -9.58% | 1,589.40 | 2,335.00 | -31.93% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | 0.00 | -1.82% | +18.86% | 207.29 | 211.14 | -1.82% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | N/A | N/A | 544.43 | 544.43 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、美光」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 4 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [SanDisk Rises 8%, Western Digital Jumps 9%, Micron Adds 7% as Memory Rebound Accelerates - 24/7 Wall St.](https://news.google.com/rss/articles/CBMixgFBVV95cUxQalNRdnRUTGwycDNhTnJqWHFqUWhsbFd4VzFiZ01wRDgtc2F4bWRablRXQURQQXNzQkNKMGRKZ3RNWVp3RWY5SHY5c19JbWVRWTN2dTY3ak1FZXdtdVV2M1BydnR0SHJCSVpuclFDdVRzRXM3c2dBY2F0RjcyY3UtLTFMcm02YjROV0dTQ1IzdEVJVUI5RmZyeTlXV2JkRU9UQTFYZjJGQXpWb2sxN1h6SEVFemdtUHNQNFV0ekszb2pVTU1ZZ3c?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 21 Jul 2026 14:20:32 GMT
- [What Just Happened To AI Stocks? (Micron, AMD & Nvidia Explained) Tampa Bay Rays (R1YP3IyRnV) - Mshale](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9EbHNjRlRhMTc5ejJqQTNtdlRRM1ZwV0JaR25fLW1uTWtONVR6N3pqM0NDcWJwZHdUVUpEdmpWN3VfRFRHcGF0QnhSTXk4NUVCSmE0ZkRQaEdNc1E?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 20 Jul 2026 20:26:07 GMT
- [Micron stock up 3%, SanDisk gains 2.5%: what woke the memory trade? - Invezz](https://news.google.com/rss/articles/CBMinwFBVV95cUxOV3otdFpxVllCV3h6WW9QdU95X3U2Smx5WUYzNXVia01uUzZ5NUMycFE1akxHdG5PSzZxX3p5ZXZGZVhjeElNOWlNMkJlZHBIVTdGaUJfVWUxX3JORkRQNW9VRWVOUjVYZVVHbnE4UGVmVFhHZkRVTHVaQ3VuTWF1MzY3UlhOaHlVN1pJMzVDLXRRTEJFQ1V6QmNhcUNnV1U?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 20 Jul 2026 10:12:29 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：凱基投顧：台股高檔震盪留意評價修正後的AI供應鏈- 新聞 - MoneyDJ；AI 帶來的電力消耗挑戰，對半導體供應鏈有何衝擊？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +24.06% | +41.18% | 327.74 | 333.74 | -1.80% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | +1.44% | +4.46% | 246.00 | 289.00 | -14.88% | 不適用 | 14.13 | 17.47 | 821.76B TWD / 52.11% | 2026-07-01 |

關聯理由（前 3）：
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [凱基投顧：台股高檔震盪留意評價修正後的AI供應鏈- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNbEVIZHd6YWhUWXBWbzRWNGxDWndCNEM4X0MxanVmR2NBMnQwNENVdndkVFhTV3dDMnJYNGh4TWktWlVOZ0RmVFYyNjBvNjU1UmVpcmx0NlphYXpNQmlaVG5fRkNvWktwSnhTQ25ZUU9KdmxCVVlSbmhvMkVZZWZvX1VqUV9SVnppVkZ4S1M2UG1oZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 21 Jul 2026 08:31:00 GMT
- [AI 帶來的電力消耗挑戰，對半導體供應鏈有何衝擊？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiakFVX3lxTE1wSHFncWg0QnhTREN3R1JXbTFkakg0VVpZWnQ0X1VnXzh2a19FSzQ2RDcyVUd2bmFuS0FXSENNdzdNRWluNXE0U29jaE1RcVIza0gyYkUtNEhCTkNvOVhOcDQ5clJGdmdjNFE?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 21 Jul 2026 19:58:07 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Chip Stocks Are Rebounding - Should Investors Buy Intel (INTC) Before Q2 Earnings? - Yahoo Finance；Intel Earnings Could Decide the Next Big Move for the Chip Stock - TradingView；台衝刺半導體AI 工研院推綠色算力 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.59 | N/A | N/A | 105.45 | 114.68 | -8.05% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.03 | -2.43% | -0.41% | 2,410.00 | 2,410.00 | 0.00% | 背離 | 74.39 | 32.40 | 442.68B TWD / 67.87% | 2026-07-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.03 | -15.94% | -10.93% | 134.50 | 164.50 | -18.24% | 背離 | 4.00 | 33.79 | 23.12B TWD / 22.85% | 2026-07-01 |
| NVDA 輝達 | 產業/供應鏈推估 | +0.02 | -1.82% | +18.86% | 207.29 | 211.14 | -1.82% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.04 | N/A | N/A | 544.43 | 544.43 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | +0.04 | N/A | N/A | 970.82 | 971.00 | -0.02% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.04 | +12.64% | -9.58% | 1,589.40 | 2,335.00 | -31.93% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -13.49% | +24.87% | 386.50 | 446.77 | -13.49% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC、Intel」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 3 篇新聞出現相關標籤。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 3 篇新聞出現相關標籤。

### 主要來源

- [Chip Stocks Are Rebounding - Should Investors Buy Intel (INTC) Before Q2 Earnings? - Yahoo Finance](https://news.google.com/rss/articles/CBMiowFBVV95cUxOS1FQT29sSFp6N1NDcGdkbXBPNG9TcUhzWnViX25KXzhxVEw3ZW9ZZlJLdEEwaGYydTNiaEpGcXc4RVlMQ2NyLUZTSDZhYmFEdmJCM3FHUFJuS295a1VqdHMyUkw4eDJfRlgtYWRLS0VxcUoybmQyV21ZZS1ra1RsTmpkeFNKcUpDRHJLU2dYd0YwMU1lLWZNRktDVEZUZDRsUUdr?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 21 Jul 2026 19:12:00 GMT
- [Intel Earnings Could Decide the Next Big Move for the Chip Stock - TradingView](https://news.google.com/rss/articles/CBMiwgFBVV95cUxQTnhUXzBkb3RSMDJmb3YwcW84eU5fLVdld2djQ21KeUllLXN4by01bzhLQWo2ak5JMmdzQy10aWI1V2s5dkFVLXlqVkM5RUEyeVhYaFNOSW5CZXNDWXA3VFAyeGNVV0Y1Wi1VZkkxTDRiVm85cTBlZjRZRndzYUZjZjl1TmJPeldZYmRhVnZJOXhOS0wwVkpHXzltc25FRVppd0ljR21FUTNDdU0wLXBZcTdRZW9pcDF3UmZjS3pwSll1UQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 21 Jul 2026 15:44:51 GMT
- [台衝刺半導體AI 工研院推綠色算力 - 中央社 CNA](https://news.google.com/rss/articles/CBMiU0FVX3lxTE5RMktvV08zeVNxT0Ytc1d0cXRlRldVUEJRd0w3c1pXMW1WUVNfQ3lhVlh5V29OZnNJV01Vc1RHd0lBQVpmX2t5V19TbEhmTnRSZWlN?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 21 Jul 2026 09:19:54 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：〈財經週報-台股熱點〉從AI到外太空 散熱族群題材不斷 - 自由時報；台股創高「散熱三雄」卻殺到跌停?阮慕驊揭市場利空鬼故事： 老套路又上演 - MSN

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | -0.26 | +4.27% | +9.43% | 2,320.00 | 2,835.00 | -18.17% | 背離 | 61.06 | 38.12 | 17.62B TWD / 66.11% | 2026-07-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 2 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：利空, 跌停, 創高。

### 主要來源

- [〈財經週報-台股熱點〉從AI到外太空 散熱族群題材不斷 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTE9rc0xOT3JaSGZPbV9uNjZUNmJLdkctMThER29ldnFaMXp1YlBQajNxaVBBcHlrVEFOOUNLZkxISUt1ZVFOMHF4WXBSd1Jtc0plYWh5bDRrdVk?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 21 Jul 2026 16:32:34 GMT
- [台股創高「散熱三雄」卻殺到跌停?阮慕驊揭市場利空鬼故事： 老套路又上演 - MSN](https://news.google.com/rss/articles/CBMiywNBVV95cUxOVWQ2cl9CQWdVTEtlWWZYRlVaMXYxSWRqRy0zU3VPcVhHZmxCVWEtUGRxNnk1aGhYcGtxcmo2ZUR2RlVzaEN0ak1XU1pkNUNJcS0tR0V5QmZNZlljaUpNeUVhdE1OSUZwYWU2bjEybGNwYnU3bHoycWlLcDlKMVdxZXNwaTZuaExTVENhdGRYdVFNanpmZ2QwUWlOTGw1R04wSkludG1XbnVZa1B0aWVKd2JRTGdTUE1OMTg0NmE2eHNZY3U3V1lIWmU5UVk0dEdrZ05ma3lHWjhUUktoX2lmcFhZNDJidUZTTWZHOVlqa1VvQXctMl83dkpsS0RHREtPYmNkd3AxNl96dHFRaGJwNWVYcHVrX3E2aXdwZmRMcGJaZjNjZmhYS1hNNi1mNkZVTFJBaGRZVEsySkZ6LTFTTi1jUFEyNHRLVE4yaFYwV3NNTG9ZT25HZDhldm9fSzJpYnlra3NwX1BUSnNxQjN4b3VrMC1icXRBWl9vTG9WZDc2dW5HMG9wX2hfVVFxN2VuWEVPbDN1dW9tS09tSUh3VEx3Vk1jN1dBclc2NVNvZEEzb1FpNUJFYVZqemsyV0gxLW92dF85Uk9zNms?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 21 Jul 2026 02:19:10 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：電金雙箭頭發威 台股強勢連三漲收45,809點 蓄勢挑戰歷史新高 - 經濟日報；權值股領軍台股勁揚逾1200點　被動元件、PCB走強 - 經濟日報；台股報復性 V 轉 創1,783最大漲點 大盤將再戰45K - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [電金雙箭頭發威 台股強勢連三漲收45,809點 蓄勢挑戰歷史新高 - 經濟日報](https://news.google.com/rss/articles/CBMigwFBVV95cUxOLS1fb2dCc1JQc2RPLTJPU0drOGZ3Mm1scXhUUlNpMG9LdTFhMTBSaFAta3RuaEZXeXZPSEZXU3VlRDczcEFvajlKWU82ek1sRXhmOUpGekh3WmZyVXpFb0JzQzZ3ZnJkeXZBZy1UX3M4ZnZ5ald3dFpZX3hDS0JIMU1nMNIBX0FVX3lxTFAxQ3liUW5uXzVSY3J2RXhQMEZBWEYwQURLVEMxaHNvWnFNY0o3RlJoU21zMWoyU3BZTjlfeUttRTRDV1VhRlhaQzhiRTlPclFORUI0bzF3ajc1QzRXdV80?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 20 Jul 2026 09:00:00 GMT
- [權值股領軍台股勁揚逾1200點　被動元件、PCB走強 - 經濟日報](https://news.google.com/rss/articles/CBMie0FVX3lxTE1Ja2pvUWRtekdVTElUOV93NjkyNnpsdGtmWmdJSmpoRURGejJWSGszUEU3UzBNdzgteVF2UlNiSWctcmRWVzVkdzdPSm42eFNFNDcxcXo0WmpzeXllYklQaGpxSl9BdkhaMDhmN2pLS0ZoWVJpQnZxdWtQVdIBX0FVX3lxTE9WVW9rRHhzSGYxT21MX1NsS0xFd3ZjT0l3Z3EtakJyMm9JMVYyODdLWHFxQzBJZHhIMWZVMHNYNk9VeHhGdlEwcVFfQzVrbnE0QVhsLUY4bWJsSk5KUG5Z?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 21 Jul 2026 02:55:40 GMT
- [台股報復性 V 轉 創1,783最大漲點 大盤將再戰45K - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFB5Z3NnZkpqZG1pdkRVbEhDR0U1elUzVk5yeFVxZzZIc29jNmNUdmtNR2hiUW1wYTExQmtBS0FKSVlHdEk5bEEwcWtTTjZkY25fbGVHZFJyT0w0UdIBX0FVX3lxTE5ydFNCY1B4bXYxMTMxYnlkWWtaMjd2VGx5dnNHaEl6TkFnMXhLRzB1SHpsS0VRTUdfcFp0SEN0N2RGSzMyQnBvNTlhV056SkduQmFxWWF2YUJ1ZmNhNjBr?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 21 Jul 2026 17:16:49 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：台股ETF受益人突破1800萬，00685L奪人氣王 - MoneyDJ；‧永豐期貨盤後分析 - MoneyDJ；台股ETF受益人突破1800萬，00685L奪人氣王- 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股ETF受益人突破1800萬，00685L奪人氣王 - MoneyDJ](https://news.google.com/rss/articles/CBMiiwFBVV95cUxNcnh2NEsxSDlMeEQ1emhNOWxVREd2UjZja2dKMFhZLTRESXRkOExyRnN1OUZxZjFVRGl2SVR6WGNGMGI2SnlIaUR3cUhzV0lUa293TEdEWkpIQVdjelZ2Q201YkE2QjNzSXZiaklXS1VrS0hCS053V1BHRDVKbWdCM2dOS09vTHRzVUdR?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 21 Jul 2026 04:48:00 GMT
- [‧永豐期貨盤後分析 - MoneyDJ](https://news.google.com/rss/articles/CBMijgFBVV95cUxNbEpMRm5BVVlJVDljODBKcVdkUzJ6Y1pSQTVfUENnblRQME5RRGZGWE5feFIzNDZQU1pybmV4eTJjeVZIaXpaWG1QMmN3cmdyYTd5bEtXNThZTE95YVNlZmFOZklZNWFwSERTaE44MW1lcE1OcVpUbVZKVVc5RS1NN1RRZy1iSEUyRlphZXBB?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 21 Jul 2026 08:06:14 GMT
- [台股ETF受益人突破1800萬，00685L奪人氣王- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPZy0zblBtdktYYXpHTVRseWR4SWlJd0owSlU1bk9uOEZGcWFjNTdZdGNROHBXZmdLbGRnQXpsUlFTVm5xMXFqYTM2a2N1cGM5YjhGNkZqb1U1eW9hV2JfNnFaQ0oza3NhNXFFa2VUbUNLNjdacURNQ0k2ZnNUcl9JazlVU2d6b0hkSHZ4WWJBOWRndw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 21 Jul 2026 04:48:00 GMT

## 新興題材：SpaceX

摘要：新興題材：SpaceX 相關新聞集中在：Goldman Sachs creates private markets platform as rich investors seek the next SpaceX and Stripe - CNBC；SpaceX snaps 7-day losing streak, sets earnings date that triggers first big share unlock - CNBC

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [Goldman Sachs creates private markets platform as rich investors seek the next SpaceX and Stripe - CNBC](https://news.google.com/rss/articles/CBMigAFBVV95cUxPaEVmSnZkRGlDVkdQOE5CUm02WkUzQkNlaE9zN2xRN1RvNFZIQ0wxZnlGaE5nQWxWQklSd292OUZZUUV3UkdXSHh1eDRTajluSWMwQUVjZWllc1VXZkIyZnNORXB4NzJtbUpvNWFhZzB2M0dWdXlycHVFdGl2d3IxZ9IBhgFBVV95cUxPM1FBTHVWVGZmWC1KUTJCRDhneHFsOFAtWnIweS13dW05WnFZc0pjTVlhc2hXbzZVYVc0TUtwTTBnN2FRWWp0MmxCeUlIVEpxWmQxbUpvdEd3YWw0SGlaOE1qSU5XZmY0SG8tLUQ4UGM4T0V5WDZVa0dIRzNpWkhXRWJ5YXNaQQ?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 21 Jul 2026 18:22:18 GMT
- [SpaceX snaps 7-day losing streak, sets earnings date that triggers first big share unlock - CNBC](https://news.google.com/rss/articles/CBMiggFBVV95cUxPRkdmZWRDY3lEamR3d0hxUlF6LXNROVQ0VU85REJ3X3B3TWIxZTl4YURrbEdpMjRoVUNrWXJab1VkWnZJVzhnWnVZSkdJWHltUUxYWkdaQmpmSUJKQ1dmNzduOXhfaTc0V3hqUENCTEEtdFUtUzRGMXhVYXNTZExLcTJ30gGHAUFVX3lxTE5mUTBLOXc3R21iUUFTbkFiYzloMFJGRWZFanJTNEdDaTl3NnpWc0hFOWl3YXUwRUljY3pVMmhNeWgxRGduLUM3eGxJWWlpUm1NVjdLMk80d0NfdnFHOGhTQnliTFctSVJIQ050UVJ2S2hEamc5SVlrQnFpaDRCdE9IbF9aS1pZYw?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 21 Jul 2026 14:10:49 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
