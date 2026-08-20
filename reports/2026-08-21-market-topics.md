# 每日股市熱門話題分析 - 2026-08-21

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜中性｜熱度 7｜市場確認 N/A｜同向 0/0
2. **半導體與晶片供應鏈**｜負向｜熱度 9｜市場確認 62.99｜同向 4/5
3. **AI 伺服器與資料中心**｜負向｜熱度 14｜市場確認 39.91｜同向 4/6
4. **新興題材：台股冷颼颼散熱**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0
5. **散熱與液冷供應鏈**｜正向｜熱度 4｜市場確認 0.00｜同向 0/1

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.48（樣本 13）
- 5日相關係數：-0.45（樣本 13）
- 同向比例：8/13

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | 62.99 | 4/5 | 1 | +2.33% | +1.81% |
| AI 伺服器與資料中心 | 39.91 | 4/6 | 2 | -2.25% | +4.97% |
| 新興題材：台股冷颼颼散熱 | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | 0.00 | 0/1 | 1 | -5.24% | -6.72% |
| 新興題材：TradingKey | 0.00 | 0/1 | 1 | -17.94% | -9.56% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價呈負相關；應檢查正負向詞庫，並降低新聞直接提及但股價背離的權重。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-08-08 | 0.72 | 0.45 | +62.50% | 16 |
| 2026-08-09 | -0.39 | 0.46 | +71.43% | 7 |
| 2026-08-10 | -0.09 | 0.74 | +71.43% | 7 |
| 2026-08-11 | 0.57 | -0.18 | +54.55% | 11 |
| 2026-08-12 | 0.52 | -0.47 | +87.50% | 8 |
| 2026-08-13 | 0.72 | 0.24 | +100.00% | 7 |
| 2026-08-14 | 0.34 | 0.57 | +92.86% | 14 |
| 2026-08-15 | 0.24 | 0.30 | +68.75% | 16 |
| 2026-08-16 | 0.37 | 0.51 | +70.00% | 10 |
| 2026-08-17 | 0.49 | 0.60 | +66.67% | 12 |
| 2026-08-18 | 0.29 | 0.36 | +80.00% | 10 |
| 2026-08-19 | -0.23 | -0.33 | +30.00% | 10 |
| 2026-08-20 | -0.72 | 0.06 | +50.00% | 8 |
| 2026-08-21 | -0.48 | -0.45 | +61.54% | 13 |

## 歷史回測摘要

- 回測日期：2026-08-21
- 近5日 3日相關：-0.62
- 近5日 5日相關：-0.37
- 同向比例：+83.33%
- 權重狀態：未調整

- 方向準確度：+83.33%
- 信心排序準確度：-0.62
- 診斷：信心校準問題

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

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Why Sandisk's 80% Margin Is More Than Just A Cycle Peak - Seeking Alpha；Why Are Semiconductor Stocks Falling? Micron, Sandisk and Nvidia Pull Back as Bond Yields Rise - MEXC；SK Hynix Climbs 4% on Record Buyback, Micron Ticks Up as Memory Defies the Tech Selloff - AOL.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 974.33 | 974.33 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | -10.42% | +4.75% | 1,600.62 | 2,335.00 | -31.45% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +8.38% | +8.66% | 216.85 | 217.56 | -0.33% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、memory」，共 4 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 2 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Why Sandisk's 80% Margin Is More Than Just A Cycle Peak - Seeking Alpha](https://news.google.com/rss/articles/CBMiowFBVV95cUxObWJpOEdZLWMtdExIRnNjZGFLRXF0bUtVMC1pZ253Y3JNQTJfcmR4eTJfaHJOVkQ4RUhNd2R1Ml9QakRHQ2k3TnM5Q1o3SWcwd0t2U2FPVEdlaU9sX051N2JOWG1rS2FqUmh4S3p3U05tZ194aWhCb0NNM0hmRTlhWl9LZnA3aWhjQUJ5T05sMDlTTlNGQlZ0ZjFYM1ZoUi1YODIw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 19 Aug 2026 12:00:00 GMT
- [Why Are Semiconductor Stocks Falling? Micron, Sandisk and Nvidia Pull Back as Bond Yields Rise - MEXC](https://news.google.com/rss/articles/CBMi2AFBVV95cUxNanRTeEx6RW8wdFpCaEliM09EMW1YaXE0Ny1wdEF1TTl4OW5ibmZieEUxd0RrZVJadTBxQUlibVNNZjZCYW50ckNlb1NTaTJHRDRBWDY2NmUxWjYyZ3BDVEx4N1ZiLThNa3VhMjluY2VzRTc2ZUY3Vjh5Z0U1OGFnaWhGVkk0ZWNQcmlFODZpNDl2b3dPNjBOOUJGeFdhSjlZTENDeFR2NmIzaDFnRGRObnAzSnRjVXZKSXREOXJVcFluM3B1N0daMEJENlVHSXBpQk1Lek9jdUw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 20 Aug 2026 04:18:43 GMT
- [SK Hynix Climbs 4% on Record Buyback, Micron Ticks Up as Memory Defies the Tech Selloff - AOL.com](https://news.google.com/rss/articles/CBMid0FVX3lxTFAtblM5NU9PVHY0YUY4Q2l1VWFIRXZkT3RVMWU1Sl9rRC14YUNtX1JCX0NNeWpiM1h6RlBFcUJzU01aOHNqOWp4aDVzSFEtWER3eVNfNWpmUFYtWXpxREczaWJpZlBjbVphdEkxMmUtS1Q1dndTU0Vj?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 20 Aug 2026 18:48:15 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Broadcom Holds Steady as ARK Buys the Dip, Intel Slips, AMD Eases After Google's Marvell Chip Deal - 24/7 Wall St.；Intel and AMD Fall 4%, NVIDIA Unchanged as Chip Selloff Defies Bond Yield Relief - AOL.com；Chip stocks fall despite bond yield relief; NVI... - Pluang

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.57 | N/A | N/A | 92.13 | 114.68 | -19.66% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.57 | N/A | N/A | 469.45 | 516.10 | -9.04% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | -0.28 | +8.38% | +8.66% | 216.85 | 217.56 | -0.33% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | -0.50 | -3.63% | -12.79% | 364.03 | 446.77 | -18.52% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.05 | -1.04% | -2.46% | 2,375.00 | 2,425.00 | -2.06% | 同向 | 86.28 | 27.53 | 467.58B TWD / 44.69% | 2026-08-01 |
| 2303 聯電 | 產業/供應鏈推估 | -0.05 | -4.94% | -7.23% | 115.50 | 164.50 | -29.79% | 同向 | 6.68 | 17.37 | 23.84B TWD / 18.98% | 2026-08-01 |
| MU 美光 | 產業/供應鏈推估 | -0.04 | N/A | N/A | 974.33 | 974.33 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | -0.04 | -10.42% | +4.75% | 1,600.62 | 2,335.00 | -31.45% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 3 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 3 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Broadcom Holds Steady as ARK Buys the Dip, Intel Slips, AMD Eases After Google's Marvell Chip Deal - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi1gFBVV95cUxOU2p6R1lpcW52OVZxbS1XT2hrcFI0Z29NMVRpcHZXanlUSzd2RjlXNzNKQXVOdXJ3ZGRNdUc3N1cwOUZiNzJTbXFydjF5MTRBdTg1Q213aXpiS0R6RGg1N0prLVVDdzFyQVlfMWU2cGJCaGRyWm5veFYxeXRTNGJWMnpUTnJnMWFZMXJwZ1B3WkpxTUVHdDVkeVpJTV9CeXJlM0FOU241a2NWUkx0NVJjNUdCRkpqdWlKN1Q4VmFVZlZLT2ZqWWJLVEVST1YwUkpLX1Q3SF9n?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 20 Aug 2026 13:32:32 GMT
- [Intel and AMD Fall 4%, NVIDIA Unchanged as Chip Selloff Defies Bond Yield Relief - AOL.com](https://news.google.com/rss/articles/CBMidkFVX3lxTE5WTENHR3kwSGFJTU5nRVFNeXZTcmFFVzhlU2EyYUgyNVZuaUgtVzAzNkhfZ1VsTzFwbFhYX3VQcklhU19jU1FMcndjeHdGN1FNcWQtaUcwVTRsSUltNk9vYjRiRWVpd3lkd05pdXk3X3d1blRBWVE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 19 Aug 2026 16:31:24 GMT
- [Chip stocks fall despite bond yield relief; NVI... - Pluang](https://news.google.com/rss/articles/CBMiqAFBVV95cUxObk9JMGQxT1I2OEpfSjMwMTdmMFRnTE55RWd3T09uQXJfbWFiQXpnanVGNDFncW4xNDgwN0xNcloyV3AzUnhRbzJYUWlxNzNWX05lcUpWVHBOdUpGc0FIbmZ5WUVSVkkyalphQ2hrTUt5WVZka3QweTVwSl80VFNyZW9pZkxvVXA5cEdYTExjTGRZbzFtY0JoSWRsbUY3SDV3c2g4T0RtcjI?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 19 Aug 2026 15:59:45 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：外資台股策略鎖定 AI 自動化、自行車復甦與紡織外銷 10檔焦點股一次看 - 經濟日報；破產企業資料是否會成為 AI 訓練的新藍海？ - TechNews 科技新報；內容平台將用戶數據納入 AI 訓練是否已成產業常態？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | -0.27 | +8.38% | +8.66% | 216.85 | 217.56 | -0.33% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 產業/供應鏈推估 | -0.08 | N/A | N/A | 92.13 | 114.68 | -19.66% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | -0.06 | N/A | N/A | 469.45 | 516.10 | -9.04% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.06 | -1.04% | -2.46% | 2,375.00 | 2,425.00 | -2.06% | 同向 | 86.28 | 27.53 | 467.58B TWD / 44.69% | 2026-08-01 |
| MSFT 微軟 | 產業/供應鏈推估 | -0.02 | +22.51% | -5.04% | 481.15 | 506.69 | -5.04% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -3.63% | -12.79% | 364.03 | 446.77 | -18.52% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.04 | -4.07% | -5.75% | 590.00 | 680.00 | -13.24% | 同向 | 13.92 | 42.69 | 73.78B TWD / 43.15% | 2026-08-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.04 | -8.64% | -12.43% | 3,700.00 | 4,310.00 | -14.15% | 同向 | 60.69 | 61.11 | 48.47B TWD / 12.16% | 2026-08-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [外資台股策略鎖定 AI 自動化、自行車復甦與紡織外銷 10檔焦點股一次看 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFA1THRBSWxTWFFqY2otWG9WZFNTSDNNNUxnOE5qUzlMZ3pETUNDYnk0ckprcEtxVHdSak5rZG9EMzFMUUNhX0pyUklYMGs1UVMwYlBNUWVwUlRLZ9IBX0FVX3lxTFB6QWpsWmpKMEV5aXNWS3RXQjg4TzJaWWNRbWRrZnFCTm8zcUNiUGdVOTZrTExtMTR6cl9sdDBKTkVDVENEZmtzNGdMZFBHNG81QkZEMTNDX2ZQanpLUlQ0?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 19 Aug 2026 09:00:00 GMT
- [破產企業資料是否會成為 AI 訓練的新藍海？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMingFBVV95cUxNNU1kc1VTNWdFeFJmbWFTTW9GRURTNXdYOFZ3WHJXOFd6UURnSEpRNERiSWFnVEJjU2o5UmQtdklkdU1wcExpbWw2QmdjUmUwQi03cm9VTlFMR3Y1eDBHb1YzdVRNVEZuaFRXb0FtRXBZN0cyY1lUMUVvc0pVcVJvWEVnc094NWFkVHpDcEp1akpNc0RCSXRJUndMV09Ydw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 20 Aug 2026 18:39:48 GMT
- [內容平台將用戶數據納入 AI 訓練是否已成產業常態？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMinAFBVV95cUxNbnhwTWh4bTZWMy1qUnZiWXp6ZFNqWmpWZnNWMzY4TXoxTUhNcGpGeVJmYWhKVlNKZ1FJU0NtU2U2RXRsSnJOMzl0aWd6QnZ6Rkx5MWVqWXhLa0hQOUp3dEhmRUtJYVdBRmFGMU1aRTBCYnkySHB1TUt5NTM3MzRmMkt2Q2dUdkhfR0lRRjloYVpUWk9xVzF6dmwxb0o?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 20 Aug 2026 13:44:38 GMT

## 新興題材：台股冷颼颼散熱

摘要：新興題材：台股冷颼颼散熱 相關新聞集中在：台股冷颼颼散熱股卻發燙！奇鋐一日填息、健策飆逾5% 有何底氣？ - UDN

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | -5.24% | -6.72% | 2,985.00 | 3,095.00 | -3.55% | 不適用 | 75.13 | 39.79 | 18.59B TWD / 57.39% | 2026-08-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐」，共 1 篇新聞命中。

### 主要來源

- [台股冷颼颼散熱股卻發燙！奇鋐一日填息、健策飆逾5% 有何底氣？ - UDN](https://news.google.com/rss/articles/CBMiUEFVX3lxTFBoT3ZhT0dCeGVQcHpPRUFWa202VXgza3d2THJEeGVreUlSaTdndWM3Ynd3UFFIc1k4STBSM040WmlXZmVaYl83eHl1MWVWSDl50gFWQVVfeXFMUFEwSkxFdWNvVFJraEVIV2tfNFJ0YU5wSnNMd2I5T2pBVC1LQVBYdWdOVml2RUFMMmNJRWw1eDN0azdwaEticC1zWmVGYTNFb1oyUzJ6Y2c?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 19 Aug 2026 03:00:32 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：〈財經週報-台股熱點〉從AI到外太空 散熱族群題材不斷 - 自由時報；台股冷颼颼散熱股卻發燙！奇鋐一日填息、健策飆逾5% 有何底氣？ - UDN；【即時新聞】奇鋐今日強勢完成一日填息，受惠液冷散熱需求爆發及強勁財報護體！ - CMoney投資網誌

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.28 | -5.24% | -6.72% | 2,985.00 | 3,095.00 | -3.55% | 背離 | 75.13 | 39.79 | 18.59B TWD / 57.39% | 2026-08-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱、奇鋐」，共 4 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：受惠, 強勁。

### 主要來源

- [〈財經週報-台股熱點〉從AI到外太空 散熱族群題材不斷 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTE9rc0xOT3JaSGZPbV9uNjZUNmJLdkctMThER29ldnFaMXp1YlBQajNxaVBBcHlrVEFOOUNLZkxISUt1ZVFOMHF4WXBSd1Jtc0plYWh5bDRrdVk?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 19 Aug 2026 19:40:39 GMT
- [台股冷颼颼散熱股卻發燙！奇鋐一日填息、健策飆逾5% 有何底氣？ - UDN](https://news.google.com/rss/articles/CBMiUEFVX3lxTFBoT3ZhT0dCeGVQcHpPRUFWa202VXgza3d2THJEeGVreUlSaTdndWM3Ynd3UFFIc1k4STBSM040WmlXZmVaYl83eHl1MWVWSDl50gFWQVVfeXFMUFEwSkxFdWNvVFJraEVIV2tfNFJ0YU5wSnNMd2I5T2pBVC1LQVBYdWdOVml2RUFMMmNJRWw1eDN0azdwaEticC1zWmVGYTNFb1oyUzJ6Y2c?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 19 Aug 2026 03:00:32 GMT
- [【即時新聞】奇鋐今日強勢完成一日填息，受惠液冷散熱需求爆發及強勁財報護體！ - CMoney投資網誌](https://news.google.com/rss/articles/CBMikAFBVV95cUxORDZrMzVOZEFBUGdCSzV0UW9rTjItQWZFUWJQUEZ4czJWbzFSbnhkdW5NOGJseEoyb0JGMERhQUFya0t0UmQxMzl2RGVBMHZoZDlqVDJoVkdLa1pCSlRFaXFnX3l3M3Q2TkRub1d5UHphSDRlYllFUVVXaWVEb3pDQ3JwcWkxYm01RDVZaGN5WjA?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 19 Aug 2026 10:25:05 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Intel Q2 $16.1B Beat: $20B Capital Raise, Foundry 14A Tesla Deal, Agentic AI CPU Demand - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.42 | N/A | N/A | 92.13 | 114.68 | -19.66% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| TSLA 特斯拉 | 新聞直接提及 | +0.21 | -17.94% | -9.56% | 345.13 | 456.56 | -24.41% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 方向判斷命中詞：raise。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- TSLA：新聞直接提及「Tesla」，共 1 篇新聞命中。 方向判斷命中詞：raise。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Q2 $16.1B Beat: $20B Capital Raise, Foundry 14A Tesla Deal, Agentic AI CPU Demand - TradingKey](https://news.google.com/rss/articles/CBMi-gFBVV95cUxPZTFRUWM4emwybjRpTEdrNWp0eHJRVHVTNTZSSWtIZVFoRWZqbTlkSWxaV3V0SzZqVVpGOFVKNnVVNlRtd19tWUVBMThHNWxlLWpWMU1xeE96WDNOMS03dDdEdW1BRTBYOG1iTm5Ec0xQdFZFa0FYMHktenVETXFxUHNseWVtamt2M1pheWdYUlRfRHQwSm8wM3gyOFFQdkh4cWpNWWEzSkhtV0ItczNsRlVrZnRabUlBc0dyVUFRNlVCc2hBbFJteE80M0xKdUE4Z1ZZMVdKYW85dWhOWTIwZ1MyUUcxbFdCQ2ZNX0VGWUQ0ajAzSnR3TEZ3?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 19 Aug 2026 06:43:46 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：凱基-竹北 對 根基(2546)個股 單一券商歷史明細 - justdata.moneydj.com；台股 ETF 主動式領跑 - 經濟日報；台股黑翻紅 量能探三周低點 外資轉買助攻 指數收復季線 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [凱基-竹北 對 根基(2546)個股 單一券商歷史明細 - justdata.moneydj.com](https://news.google.com/rss/articles/CBMiggFBVV95cUxPcnRiZ3luWVVCNlk5VW9jLWZSMzFIblU4bzFJRUlzS3lmVlNBcEQ1VmVOLW5LemQ0QzU0ajExN2dMa21pMnZmZjNFMFVfY1ZXdlZzOTFOVlNMVUtKejZLaVA4eTZHek5ZejRTdE5ZcHJZbFpTUmJ5S0duZXdFbGNXSDdB?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 20 Aug 2026 13:49:29 GMT
- [台股 ETF 主動式領跑 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE94UHpTcTlNelU1azNkX05BZlRRNDFLV0t2TGFuZEtRWEZPemh2eUY2VVpoQzYyOEZaWUN4NnpPQ05vay13amVjT040c1htZmxXdGNpZmpSdXlhd9IBX0FVX3lxTE1pVE82cjJTTi1vOTlpdkhjY2NTb29xd25OQ1Q2MS1ZV1NSNWplOTRybFRGbF9XZC1RR1dKTDZ3cm5LVTBEakl1dC1FZ0gzam5nbXU0SVU3cDhiVlBhdUJZ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 20 Aug 2026 16:56:28 GMT
- [台股黑翻紅 量能探三周低點 外資轉買助攻 指數收復季線 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9IMkIzWEM1dWh6TEtjcG9ydTJCOU9oS2RoaVRDOHg1Znl5UjBfTHQ2cGl6QlhHdkIzUXJ3SFVBNFdUSU1aWkl0N21MRF9zYnN6VWZRV2ZIWEVqUdIBX0FVX3lxTE5nemRGVmJCLVFWeXJJRnB5ZzFHYW52eElvRDZJY01YQ3I2NHVUTnVBSUVGeDR1bU44RXd3MldhdGFQNGRVLThZb21xVU5acUwxdE1PRzVFUVpkVXdaaGxJ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 20 Aug 2026 16:40:57 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》量縮收漲214點，收復季線- 新聞 - MoneyDJ；《台股盤後》量縮收漲214點，收復季線-新聞內容-基金 - MoneyDJ；台股震盪法人：反1、高息ETF成避險利器- 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》量縮收漲214點，收復季線- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxOWnlQQlB0MlhHSTFRTTZ3LU92anJ0NUdGYy1ydFo3MkgtZjF0eVhaNnZ1MEFkc2lUUjRNZmlqN1lURVVyWW84WWpZNDBhUzZCSkhyQnU5VG5sQXk2NFBYVHdZaWtZdFJ2NzdkSnluUjBjNGNUX3ZjZGVYY0JKUWMwNkw3Z2VrQzVTLWk2UGIxNkNDZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 20 Aug 2026 08:18:00 GMT
- [《台股盤後》量縮收漲214點，收復季線-新聞內容-基金 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxQS2ZwQVptYi1GLURGeFYzZC1vZHNJaFVteHh4Zy1QT2ZRNXYwSHFKWnRLSUI1U0NHbUR0Y2k2dktUejNLQWdaRzJvRkhlQm45d0xQQjlscV9KeDBWSjdwbEFjbkl2aW5zWXlwRXk3VTB5RXI2U041OGU1ZnJQcmpHaDJWQmg2RVg2YjJSTURHUjE?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 20 Aug 2026 08:23:00 GMT
- [台股震盪法人：反1、高息ETF成避險利器- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxONkxwSG1MYm5LdlFna2pRMTdobEVoUUVWUDM0NW1vMFFTRUlVLTg0a3I4MUF5X05kQlJ0c2pGbVBrV0dNTTFXNlVPdjlZbGNFM2xwdEFhZ0NFWGlXbW8zQml6Yl8xLW9xZE41dHN2LVhCdjlITERSOFdOcGpBQy1HUk1pWG83enR5UWR4SzR0UVJ2UQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 20 Aug 2026 02:42:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
