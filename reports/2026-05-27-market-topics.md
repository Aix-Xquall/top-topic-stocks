# 每日股市熱門話題分析 - 2026-05-27

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **半導體與晶片供應鏈**｜中性｜熱度 6｜市場確認 100.00｜同向 5/5
2. **記憶體與 HBM 供應鏈**｜中性｜熱度 8｜市場確認 N/A｜同向 0/0
3. **綜合市場情緒**｜負向｜熱度 37｜市場確認 0.00｜同向 0/1
4. **散熱與液冷供應鏈**｜正向｜熱度 1｜市場確認 100.00｜同向 2/2
5. **AI 伺服器與資料中心**｜中性｜熱度 10｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.07（樣本 8）
- 5日相關係數：-0.07（樣本 8）
- 同向比例：7/8

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 半導體與晶片供應鏈 | 100.00 | 5/5 | 0 | +17.60% | +15.50% |
| 記憶體與 HBM 供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | 0.00 | 0/1 | 1 | -23.20% | -12.42% |
| 散熱與液冷供應鏈 | 100.00 | 2/2 | 0 | +16.21% | +13.22% |
| AI 伺服器與資料中心 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：BofA | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：今年營收 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-05-14 | -0.29 | -0.20 | +50.00% | 6 |
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

## 歷史回測摘要

- 回測日期：2026-05-27
- 近5日 3日相關：1.00
- 近5日 5日相關：1.00
- 同向比例：+100.00%
- 權重狀態：未調整

- 方向準確度：+100.00%
- 信心排序準確度：1.00
- 診斷：正相關

調整原因：近 5 日有效樣本 3 筆，低於 15 筆門檻，暫不調整權重。

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

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：AMD Is Up 5% Today: Is It Outperforming Other Chip Stocks Like Intel and NVIDIA? - 24/7 Wall St.；Nvidia's Earnings Highlight Stronghold in AI Chip Market - Intellectia AI；機電四雄迎半導體、AI基建狂潮- 日報 - 工商時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.74 | +23.20% | +12.42% | 214.86 | 215.33 | -0.22% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.71 | N/A | N/A | 123.52 | 123.52 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.65 | N/A | N/A | 503.89 | 503.89 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.06 | +1.79% | +2.95% | 2,270.00 | 2,310.00 | -1.73% | 同向 | 74.39 | 30.52 | 410.73B TWD / 17.50% | 2026-05-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.06 | +12.50% | +15.49% | 130.50 | 130.50 | 0.00% | 同向 | 4.00 | 32.79 | 22.66B TWD / 10.80% | 2026-05-01 |
| MU 美光 | 產業/供應鏈推估 | +0.05 | N/A | N/A | 895.88 | 895.88 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.05 | +14.15% | +19.25% | 1,589.55 | 1,589.55 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.05 | +36.35% | +27.38% | 422.01 | 422.01 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：surge。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：surge。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：surge。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AMD Is Up 5% Today: Is It Outperforming Other Chip Stocks Like Intel and NVIDIA? - 24/7 Wall St.](https://news.google.com/rss/articles/CBMivgFBVV95cUxQZ2VTQlM4MmZNT3U3aG9tOUlnVjVNUVZNTjhkRHJOOURsXzdIYXFCWm9BLWlENVNmbXNzR093M0djalFwZDBKQWNmMGphcExTaF9pSnBuWmdaRzU2aHM1dTI1ajNiX0VGeHlRYURtVk5jcjVfM0lYbktEMEE3bTNtZkY5eTVIMmdZamlyYUlmUF9BdnMwTzlrd2Y1ajZhWlZZR2dtMjNwREpONWV3TEVUR2NjMDkyamJ1RXhBNlJR?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 26 May 2026 14:14:23 GMT
- [Nvidia's Earnings Highlight Stronghold in AI Chip Market - Intellectia AI](https://news.google.com/rss/articles/CBMikwFBVV95cUxOYllya3lCUElvV09zeG1GWkFlcnFNT0k3dWhDeVBjVlVObVVEZDROcTVUUkkzcEVZVDh5SkZrTmp0ai1xaS1FSmEtbnczXzV2ZWtVMzRaMm04ekJySVBITUNFVF9hMXQ3TjdwWFBGTVdPNndpaGx5TFhzbU8xbmdZb3ZhbHNJQ3E4eEF3QXlXMVBCeFU?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 26 May 2026 00:32:05 GMT
- [機電四雄迎半導體、AI基建狂潮- 日報 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1IYkYtWFpDb0ZoaHE2bHN4d1I2bXlRTERIM01udThnZHdmZGdUbTBRSVpFdEZ0VjY3ZnpiYXJXUkF4OGlTSFF3UkdPODFrdUh0SWFtTkxPbWxzZzZsNW5B?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 25 May 2026 19:00:00 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Not Just Micron: Memory Melt-Up Pulls SanDisk Up 8%, Western Digital Up 10% - 24/7 Wall St.；Why Sandisk Stock Just Popped - The Globe and Mail；MU vs. SNDK: Which AI Memory Winner Has More Upside Potential in 2026? - TipRanks

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 895.88 | 895.88 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | +14.15% | +19.25% | 1,589.55 | 1,589.55 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +23.20% | +12.42% | 214.86 | 215.33 | -0.22% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、MU」，共 4 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk、SNDK」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Not Just Micron: Memory Melt-Up Pulls SanDisk Up 8%, Western Digital Up 10% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMitgFBVV95cUxNLW5yRjF3eWkyN0NjTDdhM1FYTUstOURnXzJXVFhVUzU3TDFnRGdpcXd4djZaWUlCc0ExV0Y0OVltRlJUcjZvT2dTR3BpY0dnTDFfNkFxU3UwVndXR1Y4SEZpaEg1LUtSRmlvazhiZjQwYmZMSGV0eFV2aGJKSFAxLXBRYVJuUXhCaWNiYUZpckhnWG1QTWd2SndVNl9RTE1PY1lodWhGb2tiM1lvdld1U1U2TWpnZw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 26 May 2026 16:02:15 GMT
- [Why Sandisk Stock Just Popped - The Globe and Mail](https://news.google.com/rss/articles/CBMitwFBVV95cUxOcmFTbXFGWUU4R3JTd2tiaHUyVFRYYjM0a21CdUM0eFU5anVyX3NQdnJyNm9WMjFrVGxSMnRhNmRCcEtVNk1EVVRndzYwbmh6UVFwUjdXNThvSDJlOVAyYi1tcHl2N2h1bVVoUkNmdHRLaG13SXNFZWxFMTZRcXZtMVc0Y1Z1TkdJZFNwamlsd3VfTjhFd2NKQWRVS0NlaTNBTGZuUHdKaFlIRUxBVHRkX3pLVEIwcEU?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 26 May 2026 15:12:05 GMT
- [MU vs. SNDK: Which AI Memory Winner Has More Upside Potential in 2026? - TipRanks](https://news.google.com/rss/articles/CBMingFBVV95cUxPU19hbWNzYVN1MDBSWXRiSk9GMEhjYVVNWTRfYzROZGpxRm5FTm80by1iQm8xck9obFBsdkhDNzlfeWFPdHRIb1FCaEo2ZmNHQmtmZ3NoZEJ3cTZ3eUx4a1VKcnpfV01jNVdSWEJJalVUajJjMkJfSXBJbEJfd0xMR3BVSkZPUGR4ejE2SHBwOGphaWtJcTZkZUNBZUtHdw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 26 May 2026 17:44:56 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：Nvidia has a $200 Billion Warning for AMD and Intel Stock Investors - The Motley Fool；Did Nvidia Just Say "Checkmate" to Intel and AMD? - The Motley Fool；口袋證券申報超限證交所要查最重可罰200萬違約金| 產經 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | -0.33 | +23.20% | +12.42% | 214.86 | 215.33 | -0.22% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.65 | N/A | N/A | 503.89 | 503.89 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | -0.65 | N/A | N/A | 123.52 | 123.52 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |

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
- [口袋證券申報超限證交所要查最重可罰200萬違約金| 產經 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE9LMl85Qlg1TThfalA0YnRYM1FGX1E2SGxKeGJJSGNvcko1dklEdHQ0VXc2TDhQSnlmOXdkZ3lXNFNoV1p1SVBvakxodHFNQ2VyR2tlak1hVG93aVlYQUE?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 26 May 2026 11:04:00 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：輝達新一代 AI 平台 Vera Rubin 報到 電源、散熱鏈含金量大增 | 產業熱點 | 產業 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.58 | +9.22% | +14.02% | 2,725.00 | 2,835.00 | -3.88% | 同向 | 61.06 | 44.77 | 15.63B TWD / 71.62% | 2026-05-01 |
| NVDA 輝達 | 新聞直接提及 | +0.56 | +23.20% | +12.42% | 214.86 | 215.33 | -0.22% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 1 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：大增。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：大增。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [輝達新一代 AI 平台 Vera Rubin 報到 電源、散熱鏈含金量大增 | 產業熱點 | 產業 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE16LXJSNWVzS1hIQXlmd3lNWmVwXzdTQmhpcjhMTVpIenhHU3I2Tk5QaXVBc0hyZVo2em83VE95OUl1UVlwMUZUN0ZzM1hjbnNLb252WlFXREVYdw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 25 May 2026 09:00:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Nvidia's Earnings Highlight Stronghold in AI Chip Market - Intellectia AI；Intel Corporation stock (US4581401001): AI data center push meets fresh earnings scrutiny - AD HOC NEWS；科技巨頭隨行反映 AI 在外交中的何種地位？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +23.20% | +12.42% | 214.86 | 215.33 | -0.22% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 123.52 | 123.52 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 503.89 | 503.89 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +1.79% | +2.95% | 2,270.00 | 2,310.00 | -1.73% | 不適用 | 74.39 | 30.52 | 410.73B TWD / 17.50% | 2026-05-01 |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | -15.44% | -9.63% | 416.03 | 506.69 | -17.89% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | +36.35% | +27.38% | 422.01 | 422.01 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | +19.80% | +29.45% | 611.00 | 617.00 | -0.97% | 不適用 | 10.86 | 56.73 | 62.25B TWD / 19.22% | 2026-05-01 |
| 2454 聯發科 | 產業/供應鏈推估 | 0.00 | +20.14% | +35.18% | 4,265.00 | 4,265.00 | 0.00% | 不適用 | 62.91 | 67.97 | 46.74B TWD / -4.14% | 2026-05-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Nvidia's Earnings Highlight Stronghold in AI Chip Market - Intellectia AI](https://news.google.com/rss/articles/CBMikwFBVV95cUxOYllya3lCUElvV09zeG1GWkFlcnFNT0k3dWhDeVBjVlVObVVEZDROcTVUUkkzcEVZVDh5SkZrTmp0ai1xaS1FSmEtbnczXzV2ZWtVMzRaMm04ekJySVBITUNFVF9hMXQ3TjdwWFBGTVdPNndpaGx5TFhzbU8xbmdZb3ZhbHNJQ3E4eEF3QXlXMVBCeFU?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 26 May 2026 00:32:05 GMT
- [Intel Corporation stock (US4581401001): AI data center push meets fresh earnings scrutiny - AD HOC NEWS](https://news.google.com/rss/articles/CBMixgFBVV95cUxOajJxUVVlMEY4MlhGRmlJZlpycVVNNTFXNGF6ZHlIOTlITlhRaVFmUGVEYlVNaGdWSk12dmtQcWt0ZW1CWEc4WUg3ZDJheTM5MW9GbXdub1ZGbTBBZThhVzJVUFZpWG02d25hSXNjNGgyV0hxMmktOUdiNmFZeXBiaXV2RjMyXzRZeUlTN0RJcWFMZW42X0M2dlJZQktSUTVyWUJZRnZHazI4U1FBWm8zZllqRWVQaklFQ2h5MVBCSUhKZm00Unc?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 25 May 2026 04:36:13 GMT
- [科技巨頭隨行反映 AI 在外交中的何種地位？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMilwFBVV95cUxQMjZvcndFcVNtNlNJZ3VrQWZwaWJ6c1lmeE81ZFVwdkhfdk56VXlIckRpUlZSb2ZnR0VOSmEzMDFOYm95MkJqWVJnckhUSTVFcThzcHJ1Z2lMcXNNNFF1OFVXb0hhVm80cHlqT3JlVXhmSXBZRGV1Q0d5eEttaFR0X2QyRGVFaXBRSm11cElNSnl1ekdhZFpJ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 26 May 2026 20:56:09 GMT

## 新興題材：BofA

摘要：新興題材：BofA 相關新聞集中在：BofA’s Vivek Arya Sees Nvidia at $350 as Agentic AI Drives an “Unprecedented” Chip Cycle - 24/7 Wall St.

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +23.20% | +12.42% | 214.86 | 215.33 | -0.22% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [BofA’s Vivek Arya Sees Nvidia at $350 as Agentic AI Drives an “Unprecedented” Chip Cycle - 24/7 Wall St.](https://news.google.com/rss/articles/CBMixwFBVV95cUxPbjYzaUl1NmpBMlI2SFN1aEN5S0FEMWdZNlZTbVBrM3A5MWFUZElyY3FrYTJkaUVtaFJXSmp0RUJ1bkotYkRsWFVwaHdsMC1sNHVxSGtnY0dtODYxZjdmVVNHTnAwMlhkWm1rX09JLVlIQ1FxNG9hM3dtdlFvSjI3Y3RIQXJaYWN2aDBnRHphRllrYnlhTDRVeXBWTnJQVTN0WUZrdUF5dGJIaTJ5eEctZnNoemM4M2twRTRpMXpBWG5HblpXWWdV?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 25 May 2026 11:30:34 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》量增收跌119點，44K得而復失-新聞內容-基金 - MoneyDJ；《台股盤後》量增收跌119點，44K得而復失- 新聞 - MoneyDJ；法人專欄分析內容-台股 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》量增收跌119點，44K得而復失-新聞內容-基金 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxQdW96ZW1NVU5vRjdXVFdnVFlubWFRTGs3SldPVmNBMXAzckNYOGdSRVdDb3dDZHVadkNBbUlwbWpYSFc1VGw4OXVSbWVrWUxjZ2hKQU9ySC1WRWRBTmlSZ0ZTOUd1ZmxwMTBHeUU0dGwzalcxTHZmQVR6NTZ3MENiWUxNNVhhNEk0RGc1bExZUm4?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 26 May 2026 08:18:00 GMT
- [《台股盤後》量增收跌119點，44K得而復失- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxOVVdxNmhmdmJuckdXaFYzckVvSGQyeGNRSDZfLWExU3lNOTQ5eThlU1pWQlY0Y1BROHpPdXVZYUNrNzdvdGt1dlNZdC1JZHVlTl9KMUE3am5aS0ZkcEpPak1DZ0hCZWRMNHRKd0ZUV2paV0tHcGJmNVBEMHZHN2RSMGpkOU1tcmtCN3c4eTFfZlk1Zw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 26 May 2026 08:04:00 GMT
- [法人專欄分析內容-台股 - MoneyDJ](https://news.google.com/rss/articles/CBMijgFBVV95cUxOekpqWnl4T0JWbXdsV3NON3gtdTVoQ1pUSVFTRHlUZ3pxZmQ4ZUdpaGdmWnVjdEV5S3A1RUJYUWQ0ZUdqNW83VVN4eEpEbEVBT1F1M3VIYTdjdVViVkp4UmMtR3lwMHRIVkMxaDRkclZoZnlfVmpsOEExNjFGZmR4UmVyZ2V3ZTEzYjdKaDln?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 26 May 2026 16:19:31 GMT

## 新興題材：今年營收

摘要：新興題材：今年營收 相關新聞集中在：超豐通過配息3元；今年營收拚新高- 新聞 - MoneyDJ；朋程：卡位AI電源趨勢，今年營收雙位數增- 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [超豐通過配息3元；今年營收拚新高- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNaFYxQk5sU0YyQ2U4a0JjWDZuNXhMbG9UNllpQXJuNDk5WXhYTzBib000c3hHRFBnM18tbEhnendKWHJ3cE5WbXN1VkQ2SU9ONmlWUFNhVGhOb3Rxd3hyNmpwNWpxNk5qVDJ2ak1YRXA5SVF1RWhDWGN5MnQzVVFHVFU3NU9IUS1JVklzVkkzdzk4dw?oc=5) - Google News source discovery | MoneyDJ Tue, 26 May 2026 04:49:00 GMT
- [朋程：卡位AI電源趨勢，今年營收雙位數增- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxObENaWmpuX0RWODlPay1jSVR1RDZrMF9heWhHV2ZoRS15RmVncWk1YmlaVUx6VmJPTXBfM0xsMlFIZEJqUVNNbTZTTmV6dW5vMmp4a1NyN0ZVZFh5LTZmek5FOGxwV0otOXFwUVlUdmFCNkJOaFJORmgtR0EzcHlzUG83emVlSGdXOXp2X00xcWlEdw?oc=5) - Google News source discovery | MoneyDJ Tue, 26 May 2026 07:19:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
