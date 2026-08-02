# 每日股市熱門話題分析 - 2026-08-03

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜正向｜熱度 4｜市場確認 100.00｜同向 1/1
2. **AI 伺服器與資料中心**｜中性｜熱度 9｜市場確認 N/A｜同向 0/0
3. **半導體與晶片供應鏈**｜中性｜熱度 5｜市場確認 N/A｜同向 0/0
4. **關稅與供應鏈轉移**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
5. **散熱與液冷供應鏈**｜正向｜熱度 3｜市場確認 41.24｜同向 1/2

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.35（樣本 5）
- 5日相關係數：-0.49（樣本 5）
- 同向比例：3/5

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 100.00 | 1/1 | 0 | +10.83% | -15.43% |
| AI 伺服器與資料中心 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 關稅與供應鏈轉移 | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | 41.24 | 1/2 | 0 | +2.08% | +5.39% |
| 新興題材：液冷散熱 | 41.24 | 1/2 | 0 | +2.08% | +5.39% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-07-21 | -0.12 | -0.03 | +12.50% | 8 |
| 2026-07-22 | -0.33 | -0.15 | +16.67% | 6 |
| 2026-07-23 | -0.01 | 0.01 | +41.67% | 12 |
| 2026-07-24 | -0.16 | 0.43 | +50.00% | 6 |
| 2026-07-25 | 0.30 | -0.06 | +12.50% | 16 |
| 2026-07-26 | 0.38 | 0.06 | +23.53% | 17 |
| 2026-07-27 | 0.54 | 0.11 | +37.50% | 8 |
| 2026-07-28 | 0.32 | 0.13 | +36.36% | 11 |
| 2026-07-29 | 0.16 | -0.03 | +92.31% | 13 |
| 2026-07-30 | 0.25 | 0.92 | +66.67% | 6 |
| 2026-07-31 | 0.10 | -0.10 | +46.15% | 13 |
| 2026-08-01 | 0.38 | 0.25 | +54.55% | 11 |
| 2026-08-02 | 0.06 | -0.21 | +33.33% | 9 |
| 2026-08-03 | 0.35 | -0.49 | +60.00% | 5 |

## 歷史回測摘要

- 回測日期：2026-08-03
- 近5日 3日相關：0.21
- 近5日 5日相關：-0.42
- 同向比例：+16.67%
- 權重狀態：未調整

- 方向準確度：+16.67%
- 信心排序準確度：0.21
- 診斷：正相關

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

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：AI Memory Boom Goes Bust. Micron, SK Hynix, Sandisk Plunge 30% — and Are Still Falling - AOL.com；Memory Stocks Blast Off: Micron, SK Hynix, SanDisk, Western Digital, and Seagate All Rally Double-Digits - AOL.com；AMD and Sandisk are two of the big chip stocks with earnings momentum in the new week - cnbc.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| SNDK SanDisk | 新聞直接提及 | +0.48 | +10.83% | -15.43% | 1,214.83 | 2,335.00 | -47.97% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 新聞直接提及 | +0.48 | N/A | N/A | 823.03 | 971.00 | -15.24% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.36 | N/A | N/A | 476.15 | 516.10 | -7.74% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +0.59% | +13.30% | 200.75 | 211.14 | -4.92% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- SNDK：新聞直接提及「SanDisk」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- MU：新聞直接提及「Micron」，共 2 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AI Memory Boom Goes Bust. Micron, SK Hynix, Sandisk Plunge 30% — and Are Still Falling - AOL.com](https://news.google.com/rss/articles/CBMid0FVX3lxTE1RNmVHcFBiMGttYTMxY1RhY1hLT0g4ZEN3blRldmM0TUdVTkx5V0FiQm1IVGVWWDl6VUhMU3M0U1pRekJtbHpJSnUzbFdpeEJ4elhGLWt3MVNxSmRiRHotZG1zNFU0YjB4ZHdtbXFxYW9CZVB1d3hJ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 02 Aug 2026 06:36:22 GMT
- [Memory Stocks Blast Off: Micron, SK Hynix, SanDisk, Western Digital, and Seagate All Rally Double-Digits - AOL.com](https://news.google.com/rss/articles/CBMif0FVX3lxTE5DRWo2R1YwaUdINm5jTXM4ZU1zNUNpS2VTcmFuWnRQV2xOYXhHc1NGeXJwdGFkM1RVMC1aM3VHSkpycDN5SGxOeFhQdVZvYTEtMmR0Yl9QcWdGU1NQakEtRUJoTFkxNHpVeHhNdXZ5WXFCNWdrWlhSblBsWlhGZ3M?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 01 Aug 2026 18:44:07 GMT
- [AMD and Sandisk are two of the big chip stocks with earnings momentum in the new week - cnbc.com](https://news.google.com/rss/articles/CBMipAFBVV95cUxNUV9SQmIweFU0ZWxCLXJJQUVBRUo3OXhvRGl6dGh1cWozSXRQTjBmdlBoSzlHTEV2SG9Yb3piNXlIZk1maUdycmwxbFBZblZCejI5VHFzaEE4QmpUdlRDS1czTi1QNGdCbGl6N0xCLUJHTlZZcE5DVHh1a1Fzc2Z2MURKLWJQRWtkT2ptTXZWUlNfNEtNVDk0VGgzQmFOeXBoUjZXMA?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 02 Aug 2026 11:56:25 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：台股指數商品 擁 AI 題材 - 經濟日報；One AI Stock Everyone Wishes They Bought Earlier - AOL.com；AI 典範轉移下，封裝技術在價值鏈地位如何提升？ - cdn.technews.tw

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 90.20 | 114.68 | -21.35% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +0.59% | +13.30% | 200.75 | 211.14 | -4.92% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 476.15 | 516.10 | -7.74% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +6.36% | +3.19% | 2,425.00 | 2,425.00 | 0.00% | 不適用 | 74.39 | 32.60 | 442.68B TWD / 67.87% | 2026-07-01 |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +18.33% | -8.28% | 464.72 | 506.69 | -8.28% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -6.74% | +21.82% | 389.28 | 446.77 | -12.87% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | +0.18% | -9.46% | 555.00 | 680.00 | -18.38% | 不適用 | 10.86 | 51.53 | 65.78B TWD / 32.86% | 2026-07-01 |
| 2454 聯發科 | 產業/供應鏈推估 | 0.00 | +7.24% | -5.20% | 3,555.00 | 4,310.00 | -17.52% | 不適用 | 60.69 | 58.71 | 58.01B TWD / 2.80% | 2026-07-01 |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [台股指數商品 擁 AI 題材 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5NUHdHQ2J6UDkwTUlCSENqUDJyMkdpV3QyS2JJcE1EeVZGTldsYllCUGhvVXFaZjh2aTJMX1NrY2dQVVl5SFZUbzM0MzVSSVNBSnBzVEdqMVNtUdIBX0FVX3lxTE9MSVFmYzhYR084VlYteXZQN3RRNDdaZ1J4RUx4UXUyb1Z3SEZSRXpFMkYxOHJZWWRBUzhycXJLZm9CamZoQjNFYVhMT1BfdW5fcjVZLXFNVkxRaFFweDlF?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 02 Aug 2026 16:05:45 GMT
- [One AI Stock Everyone Wishes They Bought Earlier - AOL.com](https://news.google.com/rss/articles/CBMifEFVX3lxTE5LczBRZFF2R0huWUI4MlhCbjhwTlF5NXFFYUItdERWSi1FdzJvSDd4RWJWWnY4TERYcGlpaUlTajNoRi1nT2VuZ0ZnMThlTmlTM1lLcG42bnBNQXpIMlpsbUY5WkFfcm5jRXk2dDBBMVQ0WS1lX3RZcFRPb2o?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 02 Aug 2026 02:20:06 GMT
- [AI 典範轉移下，封裝技術在價值鏈地位如何提升？ - cdn.technews.tw](https://news.google.com/rss/articles/CBMitAFBVV95cUxNXzc3bkJ3d3RBTm91dkltSEcyZm9sOS03OEtDN0tXWTVKYUVtQkRpSDhtZk1MTWdUVHQ1eUZuT2NCVjdaN0JNNlljQlB1dXhqOEhOWHlqNS0tSVpqVUppVVk5WVRiWC1xQ1pWeW52bTJlR1J1aWs0ekNJWWxlU2lEVzlaSjU1QnRFRkhmeVMzcFNXS2xVVnpDcWZkR3NUTDF5T01BX1YxWWtxbzVlcjVMNjIyMGs?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 02 Aug 2026 17:06:01 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：汲取2016年地震經驗熊本半導體業將逐步復工| 國際 - 中央社 CNA；SEMICON West長期移師鳳凰城延續半導體生態動能| 產經 - 中央社 CNA；主動式 ETF 佈局亞洲半導體的優勢？ - cdn.technews.tw

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 90.20 | 114.68 | -21.35% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +6.36% | +3.19% | 2,425.00 | 2,425.00 | 0.00% | 不適用 | 74.39 | 32.60 | 442.68B TWD / 67.87% | 2026-07-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +6.61% | -5.47% | 121.00 | 164.50 | -26.44% | 不適用 | 6.68 | 18.20 | 23.12B TWD / 22.85% | 2026-07-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +0.59% | +13.30% | 200.75 | 211.14 | -4.92% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 476.15 | 516.10 | -7.74% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 823.03 | 971.00 | -15.24% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | +10.83% | -15.43% | 1,214.83 | 2,335.00 | -47.97% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -6.74% | +21.82% | 389.28 | 446.77 | -12.87% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 CPU, server CPU, x86, foundry；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 0 篇新聞出現相關標籤。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 0 篇新聞出現相關標籤。

### 主要來源

- [汲取2016年地震經驗熊本半導體業將逐步復工| 國際 - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5TbW1VN3JLY3UyNnBteG9YbHl6WDM3ZGxZTWdTS1NTeWY5ZU9SdGNIWmVibGNQbVB6NkExbFVUNkowb0NBODJrN3pZY2xYbFJCWmJucEVJN2xqT0Y0bUZV?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 02 Aug 2026 04:31:00 GMT
- [SEMICON West長期移師鳳凰城延續半導體生態動能| 產經 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1iVGZUZnlWUWx0dWdlSXBxb1E4c2ZELXg1UGphMlZKNUd0QW95WnR6eVVkbHFTQlZSUm9qbkwxTDVGTC1sTW5NdVFNaW9MdG1oc3BqRlp5OG93MEE5MVE?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 01 Aug 2026 03:51:00 GMT
- [主動式 ETF 佈局亞洲半導體的優勢？ - cdn.technews.tw](https://news.google.com/rss/articles/CBMicEFVX3lxTE1fdEZFdUpEci1GTW5TOUFIbzNCVVRVVmlUOE5kNjR4QWtXY1RFV1JzWXJHa1hObFhQVTFta254UjZaVjJFaEtDWEFwemVyeHVrUHFlUXRvU0FGc3N1T1VldkZ2VkNnTlV4b1ZjLUxEUUE?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 02 Aug 2026 17:06:52 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：高槓桿投資對半導體供應鏈穩定性有何影響？ - cdn.technews.tw；半導體供應鏈 短打優選 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +16.93% | +33.07% | 308.91 | 312.06 | -1.01% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | +5.25% | -0.79% | 250.50 | 289.00 | -13.32% | 不適用 | 14.13 | 17.79 | 821.76B TWD / 52.11% | 2026-07-01 |

關聯理由（前 3）：
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [高槓桿投資對半導體供應鏈穩定性有何影響？ - cdn.technews.tw](https://news.google.com/rss/articles/CBMibkFVX3lxTE9vLWZsVmJHeDNaNV91TFJDNjlacW1NUGxZM25qcGt4RVlFT0ZKOEV2NnJVUzlacXdwMkRVcGlYcHEwWmFJWUstRUlQMGxWSktDeV94UXppQXlCYkp0Z29IdHR5NDJzdW9rVXpFWkhn?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 02 Aug 2026 17:05:12 GMT
- [半導體供應鏈 短打優選 - 經濟日報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1qb1AzdkdXWXVHMlg1OVllUjM2MXFEYnNHMlBDZG80WWcyWlZicDJmMkluQ1pNb3pjNjJBQVBKcnVTWWRjRXFRVEJYLTdlTFBUU1lXaUstZVBmRmdyZnlF0gFfQVVfeXFMTWpvUDN2R1dZdUcyWDU5WWVSMzYxcURic0cyUENkbzRZZzJaVmJwMmYySW5DWk1vemM2MkFBUEpydVNZZGNFcVFUQlgtN2VMUFRTWVdpSy1lUGZGZ3JmeUU?oc=5) - Google News source discovery | 經濟日報 money Sun, 02 Aug 2026 16:52:05 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：5月EPS攻8.03元！「液冷散熱大廠」股價漲停鎖死 輝達Rubin、Google TPU放量業績走強 - Yahoo股市；奇鋐、貿聯 押逾三個月 - 經濟日報；20 歲輟學生吸金 3,100 萬美元！Omen AI 專攻液冷監控，成 AI 散熱市場新星 - technews.tw

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.57 | +3.57% | -2.52% | 2,320.00 | 2,835.00 | -18.17% | 同向 | 61.06 | 38.12 | 17.62B TWD / 66.11% | 2026-07-01 |
| NVDA 輝達 | 新聞直接提及 | +0.32 | +0.59% | +13.30% | 200.75 | 211.14 | -4.92% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱、奇鋐」，共 3 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：放量, 漲停。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：放量, 漲停。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [5月EPS攻8.03元！「液冷散熱大廠」股價漲停鎖死 輝達Rubin、Google TPU放量業績走強 - Yahoo股市](https://news.google.com/rss/articles/CBMivAJBVV95cUxPUC0zRGZSdUIxZnN6WGRrU0JXc3B1ODdIaDhwaF91T3AwZUp6SG9adVBHbFRpaHRfQk43ZE1MM192bFctV3pydGZxOFYzcGxucm5CMGVXRE52YmU5Sm5lVGlkS1hrOWpMMVc1M3NkcHlmRVNtYTFRckl4WUdneXNtNXRKTjlWcHRGZ2dvMVFvZzZpc2FvcllSQU9hVE9RbGpoTXhNcGloR2xmY0NINWlXS1Z4aXB3SmJVMGlLdzF4MV8ydUNoeHVxS3NweFN6OE42b2syNjRDY25HemNGek9ISTVoVlJMeGItdVVzQ3VsbU50UnRLQlF5RHR6N0FGNUdCbjA3MDVRcXRlUi1Qb0p1M1pYc2M1SEJVU21VLXZTS3ZNQ3VyNDJucHV3eElJZnBMbUJVdjNxd3hhdzhW?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 01 Aug 2026 09:30:00 GMT
- [奇鋐、貿聯 押逾三個月 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5KSEJnMUh0cUpTTEhJb1ItNTZpbUd1VUdVWHczUDV1NWNEQklmbHpuSU9VNnE5TTZmX0FFY1VySFB2SEVYdmFjODFTUldCSXlpWWpoYUloR2xiQdIBX0FVX3lxTFBRMlR4WFd3b29CSnJwMXVjOTkwd0pFb2ZCZGhIZ0FZaWwzeXBiQlBWMF9FYTZzZkVOUzJ2YThCX1FmbDRHZk4yVVNVU09GdDV5Wk8zT0g3eDlNdmotTWI4?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 01 Aug 2026 09:00:00 GMT
- [20 歲輟學生吸金 3,100 萬美元！Omen AI 專攻液冷監控，成 AI 散熱市場新星 - technews.tw](https://news.google.com/rss/articles/CBMiZEFVX3lxTE44NXFiUnA2OEVtVHE3ZjhPTkdFRDdFYzU0bE9IN3hWSHg2emstWHhtR3huRUZxU0hrb202RG1pQnZsSnJwR3lhZG5EdmI1VmlpVkQ3RzhrdjgxbzlxYkJtQWhvUmU?oc=5) - Google News source discovery | TechNews 科技新報 Sun, 02 Aug 2026 07:34:33 GMT

## 新興題材：液冷散熱

摘要：新興題材：液冷散熱 相關新聞集中在：5月EPS攻8.03元！「液冷散熱大廠」股價漲停鎖死 輝達Rubin、Google TPU放量業績走強 - Yahoo股市

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.32 | +0.59% | +13.30% | 200.75 | 211.14 | -4.92% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| 3017 奇鋐 | 新聞直接提及 | +0.42 | +3.57% | -2.52% | 2,320.00 | 2,835.00 | -18.17% | 同向 | 61.06 | 38.12 | 17.62B TWD / 66.11% | 2026-07-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：放量, 漲停。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 3017：新聞直接提及「散熱」，共 1 篇新聞命中。 方向判斷命中詞：放量, 漲停。

### 主要來源

- [5月EPS攻8.03元！「液冷散熱大廠」股價漲停鎖死 輝達Rubin、Google TPU放量業績走強 - Yahoo股市](https://news.google.com/rss/articles/CBMivAJBVV95cUxPUC0zRGZSdUIxZnN6WGRrU0JXc3B1ODdIaDhwaF91T3AwZUp6SG9adVBHbFRpaHRfQk43ZE1MM192bFctV3pydGZxOFYzcGxucm5CMGVXRE52YmU5Sm5lVGlkS1hrOWpMMVc1M3NkcHlmRVNtYTFRckl4WUdneXNtNXRKTjlWcHRGZ2dvMVFvZzZpc2FvcllSQU9hVE9RbGpoTXhNcGloR2xmY0NINWlXS1Z4aXB3SmJVMGlLdzF4MV8ydUNoeHVxS3NweFN6OE42b2syNjRDY25HemNGek9ISTVoVlJMeGItdVVzQ3VsbU50UnRLQlF5RHR6N0FGNUdCbjA3MDVRcXRlUi1Qb0p1M1pYc2M1SEJVU21VLXZTS3ZNQ3VyNDJucHV3eElJZnBMbUJVdjNxd3hhdzhW?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 01 Aug 2026 09:30:00 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：個股動態報導內容-407A84C8-87F8-418C-B9ED-3465C334A919 - justdata.moneydj.com；富邦-虎尾 對 健喬(4114)個股 單一券商歷史明細 - justdata.moneydj.com；台股8月天 三利多撐腰 盤勢整理後將有望上攻45K大關 | 市場焦點 | 證券 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-407A84C8-87F8-418C-B9ED-3465C334A919 - justdata.moneydj.com](https://news.google.com/rss/articles/CBMikwFBVV95cUxPbVVudnJNSWc1SlA0RmJYRXNvQ1FVTEhzdHAtTVBNRE1nMDVROWxpcDVlbjBlOENzc3dWQ3NfWEpqT3dVLXdfTGZWMFI1dks0eDNfWTlpdFJIMTdpNkNEem5yc1pmdHJWUm9oNTdVclR6YjJDTHMzOHVIWFpWV3Jab2Qtb0k2cGp1S0lfMXlSOG42d3M?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 02 Aug 2026 11:19:18 GMT
- [富邦-虎尾 對 健喬(4114)個股 單一券商歷史明細 - justdata.moneydj.com](https://news.google.com/rss/articles/CBMiggFBVV95cUxQSFVLZjZRclZMSm05TTB0Y1hLZlZvT01DcTFwdTVfNnJiM1d1WVRhRUx4QXBiX1VQdHZCVDNiNUJKX1JQOXo3VUEtS0FfU0ZLNTdTVXZFN2VYM0hOUVpzcU04MWxfSUFmYVdXalE1LVNuclNnQmFxUklVZFpmcFdFT0pB?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 01 Aug 2026 07:56:56 GMT
- [台股8月天 三利多撐腰 盤勢整理後將有望上攻45K大關 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1WSXlWYjNjXzVJbDlsa0VXQWN3VnhxdWo5OW9pOWNmUHhHWlhOODJiOWZQd1pBYjRpMjh5RFE3ekdzaG9XQ2Q4VnJFVGg2eDJENXVkRXZTUVNtZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 02 Aug 2026 17:26:19 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：產業評析-台股三大去槓桿尋寶指南 - MoneyDJ；基金-FundDJ基智網 - MoneyDJ；華南永昌-林口 對 凌群(2453)個股 單一券商歷史明細 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [產業評析-台股三大去槓桿尋寶指南 - MoneyDJ](https://news.google.com/rss/articles/CBMijgFBVV95cUxNUk0tanNZalo0UENiaTVYTHhlb1labUVDUEc5czhFdWIwLXdCakpFb2VoUUtod3lFZV8wYkRqS1luZnlpMUZoYkhuUFFPSWxTR0cycml0Y2pqRUhONEtWU1FKVGhpN21BYTV5QkpydXZKVEVBTFB0ODFJTjVzczAybG5UZFcyT0VOMWJKUWh3?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 02 Aug 2026 16:15:49 GMT
- [基金-FundDJ基智網 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxQQmZ4UC14WXN4N253czVFcnpDYXQwRGR4aWxXbWFoZWNlSU9LQUMxTmhNa3RnbURzYXVuV1BBQnMyU0Z6SkNZeEJuQnJJUmRtZG05OEo2WW9Bb1BGcjJHVVZRT3YwcU9HOGwwT08yeVBJcW0wOEF2elNCdktCTFltWnZ3Z2FHdVFBcG9OeHl4czk?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 02 Aug 2026 20:15:06 GMT
- [華南永昌-林口 對 凌群(2453)個股 單一券商歷史明細 - MoneyDJ](https://news.google.com/rss/articles/CBMigwFBVV95cUxPc0t3Qk0zVDlMSnFJTUVvMV9jZlhvWHEyYldtYmlFNUZ2OVNhNWxYVWlFaG1OM3hVNnZpUk9hS2VhZ0c2U20tR0xtbU40b0lVaGxEd1NZdE9salhfcXF3X010T0pUd3YxWjlKMXlSSHdzN3JmM2tyYmk3a1o1QWlHSjA5RQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 02 Aug 2026 01:15:18 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
