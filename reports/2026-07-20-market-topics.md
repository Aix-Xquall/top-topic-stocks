# 每日股市熱門話題分析 - 2026-07-20

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **AI 伺服器與資料中心**｜中性｜熱度 9｜市場確認 77.42｜同向 5/6
2. **半導體與晶片供應鏈**｜中性｜熱度 6｜市場確認 N/A｜同向 0/0
3. **記憶體與 HBM 供應鏈**｜正向｜熱度 7｜市場確認 0.00｜同向 0/2
4. **散熱與液冷供應鏈**｜中性｜熱度 4｜市場確認 0.00｜同向 0/1
5. **新興題材：AI散熱**｜負向｜熱度 1｜市場確認 0.00｜同向 0/1

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.59（樣本 11）
- 5日相關係數：0.11（樣本 11）
- 同向比例：5/11

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| AI 伺服器與資料中心 | 77.42 | 5/6 | 0 | +6.36% | +2.47% |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 記憶體與 HBM 供應鏈 | 0.00 | 0/2 | 2 | -13.44% | -6.50% |
| 散熱與液冷供應鏈 | 0.00 | 0/1 | 1 | -3.95% | +16.29% |
| 新興題材：AI散熱 | 0.00 | 0/1 | 1 | -3.77% | +6.38% |
| 新興題材：再探跌停 | 0.00 | 0/1 | 1 | -3.77% | +6.38% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價呈負相關；應檢查正負向詞庫，並降低新聞直接提及但股價背離的權重。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-07-07 | N/A | N/A | 0.00% | 1 |
| 2026-07-08 | -0.05 | -0.05 | +71.43% | 14 |
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

## 歷史回測摘要

- 回測日期：2026-07-20
- 近5日 3日相關：-0.01
- 近5日 5日相關：-0.03
- 同向比例：+53.33%
- 權重狀態：已調整

- 方向準確度：+53.33%
- 信心排序準確度：-0.01
- 診斷：低相關

調整原因：近 5 日信心分數與股價關係偏低，提高價格確認，降低寬題材推估。；關鍵詞×公司後續樣本有效 5 筆，未達 30 筆，不調整樣本權重

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

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel and Google deepen AI ties for chip design - Yahoo Finance Australia；Kimi K3 引熱議，開放權重模型恐推向「AI 共產主義」 - TechNews 科技新報；衛星結合 AI 算力，太空商機的下個關鍵為何？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.56 | N/A | N/A | 95.04 | 114.68 | -17.13% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | -0.06 | -3.95% | +16.29% | 202.81 | 211.14 | -3.95% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | -0.06 | N/A | N/A | 495.76 | 516.10 | -3.94% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.06 | -5.37% | -5.18% | 2,290.00 | 2,410.00 | -4.98% | 同向 | 74.39 | 30.79 | 442.68B TWD / 67.87% | 2026-07-01 |
| MSFT 微軟 | 產業/供應鏈推估 | -0.03 | +0.27% | -22.28% | 393.82 | 506.69 | -22.28% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -17.00% | +19.81% | 370.83 | 446.77 | -17.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.04 | -4.21% | -9.31% | 614.00 | 680.00 | -9.71% | 同向 | 10.86 | 57.01 | 65.78B TWD / 32.86% | 2026-07-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.04 | -7.92% | -14.14% | 3,370.00 | 4,310.00 | -21.81% | 同向 | 62.91 | 53.71 | 58.01B TWD / 2.80% | 2026-07-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：恐。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 5 篇新聞出現相關標籤。 方向判斷命中詞：恐。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 5 篇新聞出現相關標籤。 方向判斷命中詞：恐。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel and Google deepen AI ties for chip design - Yahoo Finance Australia](https://news.google.com/rss/articles/CBMiggFBVV95cUxPM0ZrUWsxVGc5T0Zod3pUNEpSYWp3WEVSX1RGYkxYQnVsTHZ3eHBGYnVnWGRlUHVnTU9hQ0NlT0J0VXBENlFfSzR0cVJSeTExMUxaUFVpbFZON0VfbXFsbHdrUXJwWHJveEZsQ25qUzdhY0g4NXZSRUVjTDcxdU9tSW13?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 18 Jul 2026 18:33:00 GMT
- [Kimi K3 引熱議，開放權重模型恐推向「AI 共產主義」 - TechNews 科技新報](https://news.google.com/rss/articles/CBMifEFVX3lxTE5wV1U1ZUNBZ3daNll2UzJjZEd2WFNvVzVCcEVaNTNRZHl4aWpvOFRUUFNOa0RVc0VhMEFyWUU4czJtVTNwZTFJTld0V1BfMmVkVmR3eUZIMkxmaFJXVFk5bE8wSGI0b2sxNFowNEsxQ2luLVpLN3dWb0tmdnY?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 19 Jul 2026 07:12:18 GMT
- [衛星結合 AI 算力，太空商機的下個關鍵為何？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiyAFBVV95cUxQM1FGaU1mVnphVXJSMjRwQTgxMlg0ZERZRkVfd1lWSGJjcDlKZHpzYkJ2RktEbFhkc29wSG44YjcyTWlacGNBcGlMNUVXSzNMcDhyQms0bXktYXMyczhFRFVvZGxJWkNRdjJCc0xGRDJfd0lNNmlfZUIybDB4Umg4N1NVZkhNYkVzTU5FcjFtSmVhRDhvMUhncVJkbUxobkprcEt2YUE4eWpxRksxSlRUdzVadmYyVlI3LVBYTHpyYzlNLUxIREFrNA?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 19 Jul 2026 20:03:17 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Why the SOXS Semiconductor Bear ETF Is Surging as Chip Stocks Sell Off - 24/7 Wall St.；Intel and Google deepen AI ties for chip design - Yahoo Finance Australia；半導體AI研發替代役8/3開放用人單位員額申請| 政治 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 95.04 | 114.68 | -17.13% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -5.37% | -5.18% | 2,290.00 | 2,410.00 | -4.98% | 不適用 | 74.39 | 30.79 | 442.68B TWD / 67.87% | 2026-07-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | -4.64% | -7.69% | 144.00 | 164.50 | -12.46% | 不適用 | 4.00 | 36.18 | 23.12B TWD / 22.85% | 2026-07-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -3.95% | +16.29% | 202.81 | 211.14 | -3.95% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 495.76 | 516.10 | -3.94% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 848.95 | 971.00 | -12.57% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -22.93% | -29.29% | 1,354.82 | 2,335.00 | -41.98% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -17.00% | +19.81% | 370.83 | 446.77 | -17.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 2 篇新聞出現相關標籤。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 2 篇新聞出現相關標籤。

### 主要來源

- [Why the SOXS Semiconductor Bear ETF Is Surging as Chip Stocks Sell Off - 24/7 Wall St.](https://news.google.com/rss/articles/CBMitAFBVV95cUxQQ2oxOXpDYWoxdnExdlNOQjVIbVNneUhWNllJUU5udW53VjRoeEc0THM4N01rTVRvclpkQzJvNnZuV3NzZEtWaTR1OHdGdkNuaXl1S1pfbGVVdWpNRk1RRDhSM09oQkhlaEhZV2VwZl9zdGpZblhlcXZPeEhvdVJ2NU5BNHJIQ3lvYTA5ekdVLUgyQnpaQUVReHpPUmwxc0VVdlRpanZqTEZ5RlRmZTJ6anZKblc?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 19 Jul 2026 16:31:05 GMT
- [Intel and Google deepen AI ties for chip design - Yahoo Finance Australia](https://news.google.com/rss/articles/CBMiggFBVV95cUxPM0ZrUWsxVGc5T0Zod3pUNEpSYWp3WEVSX1RGYkxYQnVsTHZ3eHBGYnVnWGRlUHVnTU9hQ0NlT0J0VXBENlFfSzR0cVJSeTExMUxaUFVpbFZON0VfbXFsbHdrUXJwWHJveEZsQ25qUzdhY0g4NXZSRUVjTDcxdU9tSW13?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 18 Jul 2026 18:33:00 GMT
- [半導體AI研發替代役8/3開放用人單位員額申請| 政治 - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5ZUHZGMU9NT0h4NmVaVVprMHAwUFBRNng5YzJadWJRWmlqdGJGTEJoaHBlZE5BNHFTUVBBaHFwaEpFNzUxT0hEc0llODNvWjBxY2dtdWVlaWVOaFhUbk04?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 18 Jul 2026 03:00:00 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits；Micron vs SanDisk: Which Memory Play Wins the AI Boom? - AOL.com；What Just Happened To AI Stocks? (Micron, AMD & Nvidia Explained) Tampa Bay Rays (1YP3IyRnVN) - Mshale

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.50 | N/A | N/A | 848.95 | 971.00 | -12.57% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.25 | -22.93% | -29.29% | 1,354.82 | 2,335.00 | -41.98% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.22 | -3.95% | +16.29% | 202.81 | 211.14 | -3.95% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.43 | N/A | N/A | 495.76 | 516.10 | -3.94% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.37 | N/A | N/A | 95.04 | 114.68 | -17.13% | N/A | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally, strong, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 2 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 2 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits](https://news.google.com/rss/articles/CBMi0AFBVV95cUxOWm5KdEIwSXpyY191UEhDa1V6NVpWa01UbmpJeWRIV0ttT080TmpDNEhISW5TWkQwUzBVYzBqSHJPWXRVNVJCampoWWRlYmhKVkhIeHBJLS0wLW5Ua09GQnRORXpFcW5qTEJkcnJGcW55aU5rOFVOLUFMbjRPZEpWT3A2ZllucnM0SU9JNEdrNUwyc3V2WHAtNFk3VHl4R1F6SkZRMFpleEE2Zl9MdW4tSEpMMnFGZ2hQZURWQ3B1WDlPR1BhRjJELVN5ODJWYVR3?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 18 Jul 2026 20:05:44 GMT
- [Micron vs SanDisk: Which Memory Play Wins the AI Boom? - AOL.com](https://news.google.com/rss/articles/CBMifkFVX3lxTE42Ym9lRnV1VFA1VjZuOHVZQ0IxcTF4eWs4ZFVGQmlJSEZYSHBldnY3bm5haDZ4MlFyMEFzT1QtZGpFU1ZKT1FwV2t3b0JuU2NNLS04UUJmNzRwZnpXbmVXVlZHRERBZEp3MThEZzN0TUY1UHVKYWFuWTJuSDFBdw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 19 Jul 2026 13:53:40 GMT
- [What Just Happened To AI Stocks? (Micron, AMD & Nvidia Explained) Tampa Bay Rays (1YP3IyRnVN) - Mshale](https://news.google.com/rss/articles/CBMiYEFVX3lxTE8wOFJoZHp0YmduNkMzXzVzNFhQbFhLa2swYkhlZURPc1BhRWs1empQZE1pck1EbFBUbmhwLThNbXJqdTR3UUdUbHRONlRhSWN1NDYzdHRWaG81bWRqc3JVbw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 19 Jul 2026 12:10:15 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報；訂單能見度達2029年！「散熱大廠」6月EPS衝8.03元 輝達Vera Rubin放量營運看旺 - Yahoo股市；無懼逆風 奇鋐、雙鴻權證搶鏡 - 中時新聞網

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | +3.77% | -6.38% | 2,200.00 | 2,835.00 | -22.40% | 不適用 | 61.06 | 36.15 | 17.62B TWD / 66.11% | 2026-07-01 |
| NVDA 輝達 | 新聞直接提及 | +0.21 | -3.95% | +16.29% | 202.81 | 211.14 | -3.95% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱、奇鋐」，共 4 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：利空, 跌停, 放量, 創高。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：放量。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 19 Jul 2026 08:36:46 GMT
- [訂單能見度達2029年！「散熱大廠」6月EPS衝8.03元 輝達Vera Rubin放量營運看旺 - Yahoo股市](https://news.google.com/rss/articles/CBMitAJBVV95cUxOWUJiNXpzMmhpVjlJQXY3Q0RsSk9rQndQNE94MGRXMk5rRGVTSU8zcHV3OWJ0OGZKcTZwcWdsXzZIdzBtZ2tkMFlPTjdKLWoxNWdLWjNmck10bzdSS29wWWNXRWRsUGt6TENpczVVLUNzTS1WZ3BONnBGYWZXMHpWal9tMjBweUdHY2xHNGt0RVVVX1M3bE5QdHBNeGhGRzNLMm5KM0hqd2p0eU9YOHFQS3lHYUVSUFcybWhadFlTYmlIODlUUUExcXo0bnYxSFVSVDRIUFE4UkpUUUNEREw1clJlMWJMWGRqX0hyRDVUZWtwaGN5OXFld2xRU0dLQklUbzFlTG5IU1ZVLUxWM0t2b1BNMU5Sb3lhMGpiZjZkTkthZXBsR0ZqWVNmRHA4eGNmam1HbQ?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 18 Jul 2026 06:48:56 GMT
- [無懼逆風 奇鋐、雙鴻權證搶鏡 - 中時新聞網](https://news.google.com/rss/articles/CBMia0FVX3lxTFAtNE5HWUdzS3lmc3puT05QWmdEaUIxZ1RvVmFQVTVLWkdEdk92UFJaUUIzV2VLd1RWX2UtY21ZMzVlNmdrUm1mX0tkci00Skp5NnRVc19wTktnelB5SlJuRFEzNHpwVElGTkpj?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 19 Jul 2026 20:10:00 GMT

## 新興題材：AI散熱

摘要：新興題材：AI散熱 相關新聞集中在：焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | -0.21 | +3.77% | -6.38% | 2,200.00 | 2,835.00 | -22.40% | 背離 | 61.06 | 36.15 | 17.62B TWD / 66.11% | 2026-07-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 1 篇新聞命中。 方向判斷命中詞：跌停。

### 主要來源

- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 19 Jul 2026 08:36:46 GMT

## 新興題材：再探跌停

摘要：新興題材：再探跌停 相關新聞集中在：焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | -0.21 | +3.77% | -6.38% | 2,200.00 | 2,835.00 | -22.40% | 背離 | 61.06 | 36.15 | 17.62B TWD / 66.11% | 2026-07-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 1 篇新聞命中。 方向判斷命中詞：跌停。

### 主要來源

- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 19 Jul 2026 08:36:46 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：外資狂砍1,890億元、三大法人爆賣2,617億元！台股殺出史上最大跌點 - 經濟日報；證交所攜手櫃買中心舉辦我國綠色證券認證制度宣導會 圓滿落幕 - 經濟日報；從除權息到股利再投資 凱基證券串聯生活場景打造安心投資生態圈 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [外資狂砍1,890億元、三大法人爆賣2,617億元！台股殺出史上最大跌點 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9TOGNsNGZna0dmeGhmNlNUN3FSaDUzZnJPVEdibTl5UC1tRkdzNDE1QXhJZ2pHQ09pU3FuOE5yS01NMUxKTF9iQXpsajJBZUY1eWdqOXZjTDZwZ9IBX0FVX3lxTE5Ia0VLSFdzRkFwcFlXWVRsLUt5dHRXTGVtenBpUzA4Z2JvZ3ZCT1dEdFNLMkpnQ0dZc0FScC02WjZnckIxNnZzV0JPdlNPR3BwV2dzR0RFdmJ3My12cUNz?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 18 Jul 2026 09:00:00 GMT
- [證交所攜手櫃買中心舉辦我國綠色證券認證制度宣導會 圓滿落幕 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxQcjdhVDd3clBwMWs1bG94YmlFdnJka2tiT1ZWLTdhSFh2WVhwUHdick5uR3pfeU1fQjg5V1pFc2JDYXJxenNYbG41T1RJZzB5RXhSQ2xiV2thbDJFRDdnaHc2TkQtQXZVLWE1WWlwZXFldHVuRTZ6LVRhZG9SNlRNdtIBX0FVX3lxTFB2RUlVMUkxZmZHNkRoNmI5RFdGcjQyVzlnU1ZvTlRBVDV5Q1BLNnd1STRxZHhabHlRRHVsc1p1aFJ4eEZPSVRvcnhDXzVTS2dpemFHZ0VvaTFza2tFNjNv?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 19 Jul 2026 04:43:06 GMT
- [從除權息到股利再投資 凱基證券串聯生活場景打造安心投資生態圈 - 經濟日報](https://news.google.com/rss/articles/CBMif0FVX3lxTFBBZFVTaTlxbHZ0LVJhc0pNaUxMWFNUWXpFTVpoWjlJTWpFejNFbEhmUWkyWVZIZWN0WHBFNjY4TnN1eDEtZmpEMU53TG91TWtzU0pDU1ZXN2dTc1hsdXUxeFl3Z2laVkVWdU5abjczNi1SSDZWTVZBSU5neXJ6Z3fSAV9BVV95cUxPNTBIRGZvM0NraXhtMmVJZUJxeGwzdEhfXzA0SjFDYThmNEtwZFF0Q3Z2YkdqaVFoT3UyVUdOQWZGUzZPVWJnTEp2MXBFT0owcjhXNUVRZTJQLUpySHl0NA?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 19 Jul 2026 20:45:36 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：產業評析-力抗灰犀牛危機－台股狂牛上沖下洗的震盪行情 - MoneyDJ；最新專欄分析 - MoneyDJ；基金-FundDJ基智網 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [產業評析-力抗灰犀牛危機－台股狂牛上沖下洗的震盪行情 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxPY044bXk0bjg5TERNbHN3UjB4ZHVqZ3ZfZEdCdU5sdnNYMW5LWHRMQVJ3WTVzaWxfU3BnUEhKQ1NXME1hakl6dGczbkhxOUM1dFRFYzJrSDZDWXZHdFNyV3dIREVrNUpCd3NRQkhUNXJtSFh3QlpQT3k4SGl6REJEQUdCUXRyWk42cEswck1Qdlo?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 19 Jul 2026 16:11:53 GMT
- [最新專欄分析 - MoneyDJ](https://news.google.com/rss/articles/CBMib0FVX3lxTFB4T3BtbC1TN2pBUWk2d0hTVmJGSFdFZEttSGdxOHV4bzVVYjVnN21MOXJsWWF1V0tCeDRGblQtS1FqMDFjUEJ5YzNiNDJ1VzJXem9yeDd3T2F2dW1HcnhpT2FBZWl2Y21GRzFwUkpZbw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 19 Jul 2026 13:47:12 GMT
- [基金-FundDJ基智網 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxNYjk2RDM3MlR1cWRaQkdnUVdBSjk0SEZYc004THZkLW1JY0VrVDR0aWlFR0pvR003Xy1QSUpkcGRHaXdnLUJnODVLd3lFY19vWUNoaTltbTBQekxXUE5NTjdxVkZFNUljejk1RkI2UlF4ZkkzNUJLUFpTVVAzN1IwWGhXVFZzLW9aWmJQQThoSlM?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 19 Jul 2026 17:41:26 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
