# 每日股市熱門話題分析 - 2026-05-28

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **綜合市場情緒**｜正向｜熱度 31｜市場確認 100.00｜同向 2/2
2. **記憶體與 HBM 供應鏈**｜正向｜熱度 11｜市場確認 79.27｜同向 1/1
3. **AI 伺服器與資料中心**｜正向｜熱度 12｜市場確認 88.33｜同向 5/6
4. **半導體與晶片供應鏈**｜中性｜熱度 9｜市場確認 N/A｜同向 0/0
5. **新興題材：PwHjtCzc4w**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.14（樣本 9）
- 5日相關係數：-0.07（樣本 9）
- 同向比例：8/9

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 綜合市場情緒 | 100.00 | 2/2 | 0 | +21.05% | +27.44% |
| 記憶體與 HBM 供應鏈 | 79.27 | 1/1 | 0 | +3.09% | +14.94% |
| AI 伺服器與資料中心 | 88.33 | 5/6 | 1 | +13.12% | +18.66% |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：PwHjtCzc4w | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：TradingKey | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：無人機飛控晶片 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-05-15 | -0.17 | -0.08 | +58.33% | 12 |
| 2026-05-16 | -0.12 | -0.69 | +33.33% | 12 |
| 2026-05-17 | 0.09 | -0.34 | +40.00% | 15 |
| 2026-05-18 | -0.01 | -0.17 | +33.33% | 9 |
| 2026-05-19 | 0.04 | -0.01 | +62.50% | 8 |
| 2026-05-20 | 0.36 | 0.35 | +28.57% | 7 |
| 2026-05-21 | 0.28 | 0.52 | +45.45% | 11 |
| 2026-05-22 | 0.05 | -0.00 | +33.33% | 15 |
| 2026-05-23 | -0.00 | -0.05 | +84.62% | 13 |
| 2026-05-24 | -0.11 | 0.22 | +86.67% | 15 |
| 2026-05-25 | 0.40 | 0.33 | +50.00% | 10 |
| 2026-05-26 | -0.23 | -0.31 | +92.31% | 13 |
| 2026-05-27 | -0.07 | -0.07 | +87.50% | 8 |
| 2026-05-28 | 0.14 | -0.07 | +88.89% | 9 |

## 歷史回測摘要

- 回測日期：2026-05-28
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

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：Nvidia has a $200 Billion Warning for AMD and Intel Stock Investors - The Motley Fool；Did Nvidia Just Say "Checkmate" to Intel and AMD? - The Motley Fool；Rubin機櫃售價飆漲95%！零組件大升級，誰是大贏家！？ - news.cnyes.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.65 | +21.90% | +11.23% | 212.60 | 214.86 | -1.05% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.65 | N/A | N/A | 495.54 | 503.89 | -1.66% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.65 | N/A | N/A | 121.77 | 123.52 | -1.42% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2454 聯發科 | 新聞直接提及 | +0.56 | +20.21% | +43.65% | 4,640.00 | 4,640.00 | 0.00% | 同向 | 62.91 | 73.94 | 46.74B TWD / -4.14% | 2026-05-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Nvidia has a $200 Billion Warning for AMD and Intel Stock Investors - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxPaHNTUDhIVXJyLU9OdXdxQWQtdVo3M0psdEs3YVFjYkRVbzBQS3BlM0IzX2ZiQjd6VjgxMnlxY01tTE9EcS1Yd085cEVJVjA3SkhaZHZFaGpnbUFSSTNKbGQ3eTE4bEpuUzYzRjJWREtpbDZNbHNmUUhZZ1NDQ3VYOXYzVmdYOU41eEhNSEN4UUJLQlBLYkZoaQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 26 May 2026 19:23:00 GMT
- [Did Nvidia Just Say "Checkmate" to Intel and AMD? - The Motley Fool](https://news.google.com/rss/articles/CBMikwFBVV95cUxNZDVHMFNEblJNcXhaVUFHSU5OWUo1V0ZqYnNBX01CUThmYnFXcGJKY21sN09pQXVwV3BIZFN2SmZMenM3ckV4R2V6Q1lxUk03QXdKMG1TV2RLM0EtaWNNUVBSWmZ4OXNqYTBZOWhvUXI1VXYwNWxNTXl5SGtiNndCck45RC1qU19HVlBMZWxDaUFqN0U?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 26 May 2026 11:30:00 GMT
- [Rubin機櫃售價飆漲95%！零組件大升級，誰是大贏家！？ - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTE1FNjl0SVlISzBtUmpVRzJnc1I4Q2VET3c1ZGU2ZTdHY1ZHUTBDOFl2NGZkX3JIZEktMGVpbkFUV1hMWGhteWF6eDhfMUJqNmc?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 26 May 2026 06:17:04 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：MICRON (MU) Just Had Its Best Week Since 2008 🚀🔥 Dorit Kemsley (PwHjtCzc4w) - Mshale；Not Just Micron: Memory Melt-Up Pulls SanDisk Up 8%, Western Digital Up 10% - 24/7 Wall St.；Micron Technology Inc Stock (MU) Opened Up by 4.75% on May 27: Drivers Behind the Movement - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.76 | N/A | N/A | 928.41 | 928.41 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.76 | +3.09% | +14.94% | 1,589.94 | 1,589.94 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +21.90% | +11.23% | 212.60 | 214.86 | -1.05% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron」，共 4 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 4 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [MICRON (MU) Just Had Its Best Week Since 2008 🚀🔥 Dorit Kemsley (PwHjtCzc4w) - Mshale](https://news.google.com/rss/articles/CBMiW0FVX3lxTE93NDhKakdBRDhhUWZYQzQ1QVllVTZJdVV4QjhabUxwRGMxOGxqV0V2RTdNcnF2ODBSOGZ3VHJURW5pRFY1MlUtdFNLdU5OdzFEU21oVldZbTBXanM?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 27 May 2026 18:01:47 GMT
- [Not Just Micron: Memory Melt-Up Pulls SanDisk Up 8%, Western Digital Up 10% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMitgFBVV95cUxNLW5yRjF3eWkyN0NjTDdhM1FYTUstOURnXzJXVFhVUzU3TDFnRGdpcXd4djZaWUlCc0ExV0Y0OVltRlJUcjZvT2dTR3BpY0dnTDFfNkFxU3UwVndXR1Y4SEZpaEg1LUtSRmlvazhiZjQwYmZMSGV0eFV2aGJKSFAxLXBRYVJuUXhCaWNiYUZpckhnWG1QTWd2SndVNl9RTE1PY1lodWhGb2tiM1lvdld1U1U2TWpnZw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 26 May 2026 16:02:15 GMT
- [Micron Technology Inc Stock (MU) Opened Up by 4.75% on May 27: Drivers Behind the Movement - TradingKey](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPTkpaRHVlZEF0ekpkZFVlcHo1aU83RDViYVFZNWNLNmRXejJFaVlMS2xDZlRIaGN2clFNaGdKZ3VtVTVSZ2FPbkV5bmp0MjlCLXZGYTY1VnJGMkI0UjVpSUlMUEdnYkVlaXpaSjc5SUdCOHlYVVVEZWllZlhkWTZwQ1NuSTBVX0FW?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 27 May 2026 13:47:29 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Nvidia's Earnings Highlight Stronghold in AI Chip Market - Intellectia AI；高通 AI 晶片打入中國市場？傳已獲字節跳動 AI ASIC 大單 - TechNews 科技新報；力積電 COMPUTEX 攜手愛普、晶豪科等，大秀 3D AI Foundry 布局 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.72 | +21.90% | +11.23% | 212.60 | 214.86 | -1.05% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.72 | N/A | N/A | 121.77 | 123.52 | -1.42% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.07 | N/A | N/A | 495.54 | 503.89 | -1.66% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.07 | +2.00% | +5.26% | 2,300.00 | 2,300.00 | 0.00% | 同向 | 74.39 | 30.92 | 410.73B TWD / 17.50% | 2026-05-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.03 | -16.13% | -10.36% | 412.67 | 506.69 | -18.56% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.05 | +36.30% | +27.33% | 421.86 | 422.01 | -0.04% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.05 | +14.44% | +34.87% | 642.00 | 642.00 | 0.00% | 同向 | 10.86 | 59.61 | 62.25B TWD / 19.22% | 2026-05-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.05 | +20.21% | +43.65% | 4,640.00 | 4,640.00 | 0.00% | 同向 | 62.91 | 73.94 | 46.74B TWD / -4.14% | 2026-05-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「foundry」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Nvidia's Earnings Highlight Stronghold in AI Chip Market - Intellectia AI](https://news.google.com/rss/articles/CBMikwFBVV95cUxOYllya3lCUElvV09zeG1GWkFlcnFNT0k3dWhDeVBjVlVObVVEZDROcTVUUkkzcEVZVDh5SkZrTmp0ai1xaS1FSmEtbnczXzV2ZWtVMzRaMm04ekJySVBITUNFVF9hMXQ3TjdwWFBGTVdPNndpaGx5TFhzbU8xbmdZb3ZhbHNJQ3E4eEF3QXlXMVBCeFU?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 26 May 2026 20:54:48 GMT
- [高通 AI 晶片打入中國市場？傳已獲字節跳動 AI ASIC 大單 - TechNews 科技新報](https://news.google.com/rss/articles/CBMicEFVX3lxTE1LRXRRdkRVTXVMRk5DSWN3cVZkVzNqX0RaSjE5YjF3WWZsQ3AxVWJtTzVlWWQxMS1uQ2tqUjVPaFF6M2hXSjZKZC1ObjJrTUhlMk5vcURheWVKR2ZHcTFxRlh4RmFjQ25zLWg5bnFOaTc?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 27 May 2026 03:55:22 GMT
- [力積電 COMPUTEX 攜手愛普、晶豪科等，大秀 3D AI Foundry 布局 - TechNews 科技新報](https://news.google.com/rss/articles/CBMia0FVX3lxTE1DQ2J0bWtOWG8yMXgwa1Z5dlMwWXFMR2dtU0Z5ZDRXQzRBLVRFYWo4YUtKZDZXdmVUczluQlp0RnowcDNRcWhkYVljTTdpTlFqdDNPXzduZV9HQW5GQnVrWEVpVUZPR0NSUVcw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 26 May 2026 04:58:01 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：AMD Is Up 8% Today: Is It Outperforming Other Chip Stocks Like Intel and NVIDIA? - AOL.com；AMD Is Up 5% Today: Is It Outperforming Other Chip Stocks Like Intel and NVIDIA? - 24/7 Wall St.；Nvidia's Earnings Highlight Stronghold in AI Chip Market - Intellectia AI

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +21.90% | +11.23% | 212.60 | 214.86 | -1.05% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 121.77 | 123.52 | -1.42% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | N/A | N/A | 495.54 | 503.89 | -1.66% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +2.00% | +5.26% | 2,300.00 | 2,300.00 | 0.00% | 不適用 | 74.39 | 30.92 | 410.73B TWD / 17.50% | 2026-05-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +25.88% | +32.87% | 143.50 | 143.50 | 0.00% | 不適用 | 4.00 | 36.06 | 22.66B TWD / 10.80% | 2026-05-01 |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 928.41 | 928.41 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | +3.09% | +14.94% | 1,589.94 | 1,589.94 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | +36.30% | +27.33% | 421.86 | 422.01 | -0.04% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 3 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AMD Is Up 8% Today: Is It Outperforming Other Chip Stocks Like Intel and NVIDIA? - AOL.com](https://news.google.com/rss/articles/CBMigAFBVV95cUxQcTA3M2lWZDdtY0VZOVpVN25MQUo0WGRER0xJVjNmaURCc0c5UFBxSDNaZ0g0aE9uRTRoTE5DYVJwOHVpaHdUaHhfV0hjRVVPV1RzckF5VHNvNUlRelR2NkJvRXAxLTlyQXd6SURmMkFiRmdhbWZoNTQzWGpabXc4Wg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 27 May 2026 16:45:09 GMT
- [AMD Is Up 5% Today: Is It Outperforming Other Chip Stocks Like Intel and NVIDIA? - 24/7 Wall St.](https://news.google.com/rss/articles/CBMivgFBVV95cUxQZ2VTQlM4MmZNT3U3aG9tOUlnVjVNUVZNTjhkRHJOOURsXzdIYXFCWm9BLWlENVNmbXNzR093M0djalFwZDBKQWNmMGphcExTaF9pSnBuWmdaRzU2aHM1dTI1ajNiX0VGeHlRYURtVk5jcjVfM0lYbktEMEE3bTNtZkY5eTVIMmdZamlyYUlmUF9BdnMwTzlrd2Y1ajZhWlZZR2dtMjNwREpONWV3TEVUR2NjMDkyamJ1RXhBNlJR?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 26 May 2026 14:14:23 GMT
- [Nvidia's Earnings Highlight Stronghold in AI Chip Market - Intellectia AI](https://news.google.com/rss/articles/CBMikwFBVV95cUxOYllya3lCUElvV09zeG1GWkFlcnFNT0k3dWhDeVBjVlVObVVEZDROcTVUUkkzcEVZVDh5SkZrTmp0ai1xaS1FSmEtbnczXzV2ZWtVMzRaMm04ekJySVBITUNFVF9hMXQ3TjdwWFBGTVdPNndpaGx5TFhzbU8xbmdZb3ZhbHNJQ3E4eEF3QXlXMVBCeFU?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 26 May 2026 20:54:48 GMT

## 新興題材：PwHjtCzc4w

摘要：新興題材：PwHjtCzc4w 相關新聞集中在：MICRON (MU) Just Had Its Best Week Since 2008 🚀🔥 Dorit Kemsley (PwHjtCzc4w) - Mshale

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 928.41 | 928.41 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [MICRON (MU) Just Had Its Best Week Since 2008 🚀🔥 Dorit Kemsley (PwHjtCzc4w) - Mshale](https://news.google.com/rss/articles/CBMiW0FVX3lxTE93NDhKakdBRDhhUWZYQzQ1QVllVTZJdVV4QjhabUxwRGMxOGxqV0V2RTdNcnF2ODBSOGZ3VHJURW5pRFY1MlUtdFNLdU5OdzFEU21oVldZbTBXanM?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 27 May 2026 18:01:47 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Micron Technology Inc Stock (MU) Opened Up by 4.75% on May 27: Drivers Behind the Movement - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 928.41 | 928.41 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Micron Technology Inc Stock (MU) Opened Up by 4.75% on May 27: Drivers Behind the Movement - TradingKey](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPTkpaRHVlZEF0ekpkZFVlcHo1aU83RDViYVFZNWNLNmRXejJFaVlMS2xDZlRIaGN2clFNaGdKZ3VtVTVSZ2FPbkV5bmp0MjlCLXZGYTY1VnJGMkI0UjVpSUlMUEdnYkVlaXpaSjc5SUdCOHlYVVVEZWllZlhkWTZwQ1NuSTBVX0FW?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 27 May 2026 13:47:29 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》開高震盪收漲731點、寫新天量，首收44K - MoneyDJ；台股狂飆 5月投資股票信心逆勢創逾三年低-新聞內容-基金 - MoneyDJ；台股狂飆5月投資股票信心逆勢創逾三年低- 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》開高震盪收漲731點、寫新天量，首收44K - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQRUdvYkp1Rk1EenpXb0thOFAwVWlicjJ3Ykw1cGdjZHo3WTVfRHlsYlhQaUxSd0tWTHhGbHlFZE9Eb1B2MmMwcFdtckVwMDV0Z3k1cmd4eU1UY1hVOFBzYlJnenZXUGs4U29Qc2QyZ01KWlpFNXh4WVA4VXFmcjZabi1DaFBZaDB2Uk5zUXJReVJqQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 27 May 2026 08:22:00 GMT
- [台股狂飆 5月投資股票信心逆勢創逾三年低-新聞內容-基金 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxOTm5TbXd0Vmg0a3AzSEEyekpLc25JRHNZQmp2ZHJSYUczaGZuYU1EdDd2V2tMRmhoaXFQNk4wUThGbDhpQTZtRW9YUDdNbVo4Sm12S3h2Z0NybkJvRG9MeEtwSEpHUFlSc0hjOEJjdHdnMlFabkxZOFJLemFsOTBRajFFQnktN2tTZHNJUlh0T2Y?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 27 May 2026 07:14:00 GMT
- [台股狂飆5月投資股票信心逆勢創逾三年低- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMilgFBVV95cUxNWks4RjAyQl9CVlNocW9BU0s5N3NaZmVvLTBCZmhaWVg5ZFBQaTNSU21JVHE0b0k2VUpnbExNN2tqZzdGTTVQRXJHdHpyWHZwNEM1el9iTm14Zll3a24xNFNLMjZOVFMyOFNBUGdWVlZ1TUpObkY1WUwzblZJTUdEMzhnZ29Qb2xzTm8tdUM5ZGJKQ2VEM0E?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 27 May 2026 07:13:00 GMT

## 新興題材：無人機飛控晶片

摘要：新興題材：無人機飛控晶片 相關新聞集中在：無人機飛控晶片中國製？雷虎：意法半導體生產| 產經 - 中央社 CNA

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [無人機飛控晶片中國製？雷虎：意法半導體生產| 產經 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE11d04xNzRfMGJRcC0xNjRwM19GZllaRmhJZDVROTBhSEhrSkVCUEw1QTBvZEhCRUg4UG1BVnhQajZLWUw0SzhjeFo5dXRWRGl2eFlnU3U4UzFBVmJYUWc?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 27 May 2026 05:54:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
