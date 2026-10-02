# 每日股市熱門話題分析 - 2026-10-02

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜正向｜熱度 11｜市場確認 62.20｜同向 2/3
2. **電動車與電池**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0
3. **AI 伺服器與資料中心**｜正向｜熱度 10｜市場確認 68.31｜同向 6/8
4. **半導體與晶片供應鏈**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0
5. **關稅與供應鏈轉移**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.51（樣本 11）
- 5日相關係數：0.37（樣本 7）
- 同向比例：8/11

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 62.20 | 2/3 | 1 | +5.18% | -4.22% |
| 電動車與電池 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 68.31 | 6/8 | 2 | +5.27% | +0.57% |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 關稅與供應鏈轉移 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：OpenAI | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：9月營收 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-09-19 | 0.20 | 0.47 | +46.15% | 13 |
| 2026-09-20 | -0.04 | -0.25 | +30.77% | 13 |
| 2026-09-21 | -0.15 | -0.05 | +61.54% | 13 |
| 2026-09-22 | -0.00 | -0.01 | +88.24% | 17 |
| 2026-09-23 | 0.35 | 0.22 | +80.95% | 21 |
| 2026-09-24 | 0.05 | 0.42 | +90.00% | 10 |
| 2026-09-25 | -0.31 | 0.15 | +30.77% | 13 |
| 2026-09-26 | 0.22 | 0.14 | +63.64% | 11 |
| 2026-09-27 | 0.11 | -0.14 | +57.14% | 14 |
| 2026-09-28 | 0.05 | -0.53 | +63.64% | 11 |
| 2026-09-29 | 0.31 | -0.78 | +16.67% | 6 |
| 2026-09-30 | 0.05 | 0.04 | +33.33% | 18 |
| 2026-10-01 | 0.21 | -0.27 | +40.00% | 20 |
| 2026-10-02 | 0.51 | 0.37 | +72.73% | 11 |

## 歷史回測摘要

- 回測日期：2026-10-02
- 近5日 3日相關：0.09
- 近5日 5日相關：0.27
- 同向比例：+60.87%
- 權重狀態：已調整

- 方向準確度：+60.87%
- 信心排序準確度：0.09
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

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Micron Revenue Surges 379%: 4 Top AI Chip Stocks (NASDAQ:MU) - Seeking Alpha；Intel Stock Rises 4% as Micron Results Boost AI Chip and Memory Sector Sentiment - FXLeaders；Micron's Blowout Q4 Pushes Memory Peak Further Out – But Investors Still See A Cycle Risk - TradingView

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.57 | +13.02% | N/A | 1,097.39 | 1,097.39 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.28 | -2.13% | -4.22% | 1,739.89 | 2,335.00 | -25.49% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.42 | +4.64% | N/A | 120.00 | 120.23 | -0.19% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +14.14% | +14.44% | 228.38 | 228.38 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：risk, boost, surges。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 2 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：risk, boost。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 方向判斷命中詞：boost。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Micron Revenue Surges 379%: 4 Top AI Chip Stocks (NASDAQ:MU) - Seeking Alpha](https://news.google.com/rss/articles/CBMimwFBVV95cUxNeklWZ1dfNTRJMHJYdENCY1l2eHBhX1pFOUYteDRlNXhIbEIzS21EekRnT3RscnVMTGFCbHBkeTZFMDNMLTFoQXdfbVp1M0hQTm9wdkZyQlpWZC1JeGhyYnpjcGEtRzF4U25lQW9uXzQyNFlDRnhqanRuTlJ1RmVOSVJtX1JULTBYMnlubXhuRHZlUmZOLVNyTG1SVQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 01 Oct 2026 16:31:53 GMT
- [Intel Stock Rises 4% as Micron Results Boost AI Chip and Memory Sector Sentiment - FXLeaders](https://news.google.com/rss/articles/CBMikgFBVV95cUxNX19wM0NhUjhXek1hWS1LdDlST1k0dzZncHB3cmQzcjMxNDJuWnViRnpHQW1Ib3gwRWxoWmxObjFhWkJNWUt5VExxV2xOZ053OTBCYlZEOTlJem1VQjl6N1VudUxyTGNNM01kLWdMaV83Z0hYWlJPYmFyZ0piU1ItSHVfaXlwTjR1RVl6SmFUNHk5QQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 01 Oct 2026 12:00:01 GMT
- [Micron's Blowout Q4 Pushes Memory Peak Further Out – But Investors Still See A Cycle Risk - TradingView](https://news.google.com/rss/articles/CBMi4gFBVV95cUxQQjFwN0JLNTducUY1dTR4YWF6bTk0bmxVemwxZUJHTU9qVGZ4YnpaWU9mYWgycFdhUHBRNURja1lFNGlraXIwTC1jZTFJS21ERDZGZGthUUxoSXU0RzVBSUZtSVg0MEhpaFNoS2Nfd0xvZEJIZFdZUGxRYzRjcU1CUTM5b3p0VjR0UkJaN3FkYWp3MXpvbGI1b3IwaXB0VnUwaFdJYzZoMWFjZTVzcm1ycHdHRzdFd1BRc181WWZDSnlDZFZkOWc5OFN3d2FWeThVR18zYk01NVpZb1JZNkowNjRR?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 01 Oct 2026 09:07:42 GMT

## 電動車與電池

摘要：電動車與電池 相關新聞集中在：半導體微加工技術導入電池，韓國團隊成功打造高穩定「無負極電池」新架構 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| TSLA 特斯拉 | 產業/供應鏈推估 | 0.00 | -15.64% | -7.03% | 354.81 | 456.56 | -22.29% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- TSLA：產業/供應鏈推估：公司標籤符合「電動車與電池」關鍵字 EV, electric vehicle, battery, autonomous driving；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [半導體微加工技術導入電池，韓國團隊成功打造高穩定「無負極電池」新架構 - TechNews 科技新報](https://news.google.com/rss/articles/CBMihwFBVV95cUxOdzJpRmU1clgzNHhlbmg2S08zNTNSaUtOOWxDZ21rYkxQWXIzYS1DNWU2cVdPSzZGMHdYU3N3VE1Bd2VwWVdUcnlpZmJlSkxWT2FLOUVRdDk1b2JfYzJma1BtZ25KdjlwaHhaRzRIQ1ZZRWtueVYwVm1OWmJlYkhoazYzVGI4M3c?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 02 Oct 2026 00:37:21 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：AMD Doesn’t Need to Beat Nvidia to Be a Big AI Winner - 24/7 Wall St.；+35%, +33%: AI chip and infrastructure stocks cap a blockbuster Sep, here’s why - Investing.com；AI 聊天機器人答案太單一，研究指多樣性仍不及 Google 搜尋 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.54 | +14.14% | +14.44% | 228.38 | 228.38 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.53 | +19.30% | N/A | 615.73 | 615.73 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 產業/供應鏈推估 | +0.08 | +4.64% | N/A | 120.00 | 120.23 | -0.19% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.06 | +1.41% | +2.03% | 2,510.00 | 2,510.00 | 0.00% | 同向 | 86.28 | 29.09 | 514.81B TWD / 53.32% | 2026-09-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | +13.89% | +4.23% | 512.80 | 512.90 | -0.02% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -7.03% | -15.87% | 351.19 | 446.77 | -21.39% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.04 | +1.57% | +2.45% | 710.00 | 710.00 | 0.00% | 同向 | 13.92 | 51.37 | 82.25B TWD / 45.66% | 2026-09-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.02 | -5.77% | -3.86% | 4,980.00 | 4,980.00 | 0.00% | 背離 | 60.69 | 82.25 | 64.18B TWD / 44.08% | 2026-09-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AMD Doesn’t Need to Beat Nvidia to Be a Big AI Winner - 24/7 Wall St.](https://news.google.com/rss/articles/CBMinAFBVV95cUxONlZEdU4tNW40NVNla1NnbTlYeFRDNXdOcllzNndZOENsNDctSTNFR0FVTUZ3M2pNVmRXWVBjOXJtcUdXY0p4Tk9GMjJUSHZ5dGMtU2lhYkJjMjBTRVBhSG9Xd0JZWTJJNWxmYVRzUlVUUlpLaTk3eENGcnNGS2taNVgxSDQ2Q050dWxVYmVaVGVCYXBMZlpHRXFKano?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 01 Oct 2026 16:00:00 GMT
- [+35%, +33%: AI chip and infrastructure stocks cap a blockbuster Sep, here’s why - Investing.com](https://news.google.com/rss/articles/CBMixgFBVV95cUxQY2hSUWVTTlc4MFFRSER5djA1dENpWGdwSG91cThIckJUVUFhWUxSTnNndzFnVHgxVjA1dDBFRXdMUkpINGg4TFRtX0tHX05oQWZSSDRjNko0TzR6MUpfOEhfaE1aRmR3VW9uaUp5dk9oM2J5WFBqUFZQdkFla2M5WWZpbVJCWDVHQkRLUzRtWEJXQzdmRHFLU1ZuNlE4YUhKQVU0dWRUREo4eE53dmlHWGRZTWhWR2pORW9sUFRBaHBtUFJ3alE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 01 Oct 2026 01:56:34 GMT
- [AI 聊天機器人答案太單一，研究指多樣性仍不及 Google 搜尋 - TechNews 科技新報](https://news.google.com/rss/articles/CBMixAFBVV95cUxNT1JoTE4tRm96T2RTSDU3Z0k3aTFtTDJzaVZvTzFlSGtOQTZqWTZ3NjMtSGQ4SWYzYUhWRXpZaFRoTE5sQkZnYWhvXzFSV3VrYnVnMExaSFhtUWU3LVJoNFNqSS1Cc1ZOTl9fWkpXMmE4SzBfWG5sWGdkQ1ctN2M4TWlfZmNTNmVCemFXVllDN1o1TFVEZWstdkF0ODRVM2RNTV9JUUdMaVdzV0MxbWxKVGxmb0J6WkV0RFU4T1gyQ3VSeVpu?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 02 Oct 2026 00:58:16 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：+35%, +33%: AI chip and infrastructure stocks cap a blockbuster Sep, here’s why - Investing.com；Chip Stocks Roar Back: AMD, Intel Power SOXX Toward Best Month Since June - TradingView；Top 5 Semiconductor Stocks to Own Into Year End: Bank of America - Benzinga

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | +4.64% | N/A | 120.00 | 120.23 | -0.19% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | +19.30% | N/A | 615.73 | 615.73 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +1.41% | +2.03% | 2,510.00 | 2,510.00 | 0.00% | 不適用 | 86.28 | 29.09 | 514.81B TWD / 53.32% | 2026-09-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +4.87% | +0.94% | 161.50 | 164.50 | -1.82% | 不適用 | 6.68 | 24.29 | 25.04B TWD / 30.71% | 2026-09-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +14.14% | +14.44% | 228.38 | 228.38 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | +13.02% | N/A | 1,097.39 | 1,097.39 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -2.13% | -4.22% | 1,739.89 | 2,335.00 | -25.49% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -7.03% | -15.87% | 351.19 | 446.77 | -21.39% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 3 篇新聞出現相關標籤。

### 主要來源

- [+35%, +33%: AI chip and infrastructure stocks cap a blockbuster Sep, here’s why - Investing.com](https://news.google.com/rss/articles/CBMixgFBVV95cUxQY2hSUWVTTlc4MFFRSER5djA1dENpWGdwSG91cThIckJUVUFhWUxSTnNndzFnVHgxVjA1dDBFRXdMUkpINGg4TFRtX0tHX05oQWZSSDRjNko0TzR6MUpfOEhfaE1aRmR3VW9uaUp5dk9oM2J5WFBqUFZQdkFla2M5WWZpbVJCWDVHQkRLUzRtWEJXQzdmRHFLU1ZuNlE4YUhKQVU0dWRUREo4eE53dmlHWGRZTWhWR2pORW9sUFRBaHBtUFJ3alE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 01 Oct 2026 01:56:34 GMT
- [Chip Stocks Roar Back: AMD, Intel Power SOXX Toward Best Month Since June - TradingView](https://news.google.com/rss/articles/CBMiywFBVV95cUxNT0RMdUJDbkdpdXFQaVRrUmd0VnJQbHJVdlZNZHB0ZVU0MlNKYkZPU0hLVXRMRG9nVHRrWnoxc1dRTDJrWGpVYzRBLUlMUkdFQjJmakZNWkdGeHZoTExMbk5pM3dEek56cjR4Wk5SWDJmaEZaNlRPLUZGNmU5SHQtWmhBVTZDLXoyVFQyYkhyQjY3ZTJGRTFYbWVvTE43djJXYUYzN0o0a09fSnlNNkprbk80eUlfUHJVMDJ1ZldCQTlXQUd3MERJRnkxQQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 30 Sep 2026 07:48:55 GMT
- [Top 5 Semiconductor Stocks to Own Into Year End: Bank of America - Benzinga](https://news.google.com/rss/articles/CBMiqgFBVV95cUxNRnRTRXpObEZtdHBHNEhEellsRzRsLWNLazloaEI2QkhMamJCTkZDUEVsMnhDOWNHbDBPZk5rdVgyXzBBRkFabzNZc1VRUUkwbmNTMTlIeVpJc3lWS1FQUllpdVhiZnRLaUtpYmpFV0tQRnFTS2JlMWhheG9ESkdpaXB4b3czWExidVRVVmhPc0JBV1h3SmJqUm1CU0s1eHpROUdIcmxiWWdhQQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 30 Sep 2026 20:01:40 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：美債殖利率飆24 年新高，台股挑戰48K 大關卡位AI 供應鏈- 新聞 - moneydj.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +5.85% | +18.46% | 330.32 | 333.02 | -0.81% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | +1.40% | +0.40% | 254.00 | 289.00 | -12.11% | 不適用 | 15.21 | 16.74 | 921.77B TWD / 51.98% | 2026-09-01 |

關聯理由（前 3）：
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [美債殖利率飆24 年新高，台股挑戰48K 大關卡位AI 供應鏈- 新聞 - moneydj.com](https://news.google.com/rss/articles/CBMikgFBVV95cUxPazY4QkVNWDBLNEdrUGZFV3Z4NFRpQUZVT0p3aWh6VVp2cHBPWFFHMzd3bDJUeFNWc2REZ2V6cTF6ckt5QWZETmtOTmlKajNwbEtFQWRoS0xqMldnOHhhekxaenJ1QnJjeFFCM2w1VkMzZ2hSTnp4NFJpbUticnFHNlY3V3dLSEdzaHVQTDlaVERDZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 01 Oct 2026 03:10:00 GMT

## 新興題材：OpenAI

摘要：新興題材：OpenAI 相關新聞集中在：OpenAI 破解數學難題震撼學界，AI 時代的數學核心：是「找答案」還是「真理解」 - TechNews 科技新報；OpenAI alerts more than 100 groups about rogue AI agent activity - Reuters

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 新聞直接提及 | 0.00 | +13.89% | +4.23% | 512.80 | 512.90 | -0.02% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：新聞直接提及「OpenAI」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [OpenAI 破解數學難題震撼學界，AI 時代的數學核心：是「找答案」還是「真理解」 - TechNews 科技新報](https://news.google.com/rss/articles/CBMihgFBVV95cUxPZnM4bkJDT0psOG9XNEtsMW1ucnRPQi1XSE15THkyazJ4a3c1c0NOalk5YnVVbzBqQ2JLMzE4RFhpOXg3dUkxSmRNM3BISnNrTkNPSHA4VFJaYWh5ZHZRRVMwYmpPaUtDa3Y1YzFFYjJCMGVBeVBwTllac2VUNS1KLUtJV3JFUQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 01 Oct 2026 23:42:57 GMT
- [OpenAI alerts more than 100 groups about rogue AI agent activity - Reuters](https://news.google.com/rss/articles/CBMiuAFBVV95cUxQby1YSlo5dUJYU0ExbVRnbnR6U0JJaHc5MXdacGFBTUtSVFZUMFFrLWZYNmc3SENiYmdKY0I1bEM1azNwUWJ0RDY2YVUyNzF4a0ZFNENEMF9yaXFLTHVxeUxOMWVyTE1ubWFVTVFEYUZic3NvVkVEa3JjS3llaHpxNHoxMmZiNXZfX192cUhlM2hoYUxiTy1MTFRiMGJSRkt4SlhxZy1UYXpwLXYtdEh0N1c5UXBfMC1j?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 01 Oct 2026 22:26:30 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：國票證券：台股多方架構並未出現敗筆- 新聞 - moneydj.com；基金-FundDJ基智網 - moneydj.com；《台股盤後》收漲413點重返48K/寫收盤新高- 新聞 - moneydj.com

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [國票證券：台股多方架構並未出現敗筆- 新聞 - moneydj.com](https://news.google.com/rss/articles/CBMikgFBVV95cUxOSFFwTUpJQi1nQ2l0N01IM3hPS1hTcDU3YWNiOERMS09MenA2clVuZllEZTM2VExTYTFYbU9pSklVVHNXSVFuU2VTb0xleXhxNkUxRmh5enpoNkptalZBc25MSkp2M0xZNy1hU1JMRU5Fd3g0MUJWTGk4VmI3djM2ZEc2RUQ0TWQ5ZEU4c21QVWtmdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 02 Oct 2026 00:37:00 GMT
- [基金-FundDJ基智網 - moneydj.com](https://news.google.com/rss/articles/CBMikAFBVV95cUxPNTFCQkVXNmM5a3ZMZ0hPVVVkZ3F0Ml9xcGZSdFBTZkV0NjhVTjBlY05DRFJyODl4QnJrYThGX0ZSTmlOMHRKVmtkZFI0bWNmQnllVEczdDEzOVFpSkNpOFJFME84VkZZUl9wT080UV9uVUwtNm1kM1Z6dTJmYkNfUkYweFdVZ08zTFJUX1Y3Ync?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 01 Oct 2026 17:17:20 GMT
- [《台股盤後》收漲413點重返48K/寫收盤新高- 新聞 - moneydj.com](https://news.google.com/rss/articles/CBMikgFBVV95cUxPellWV1BWN1NPSC03cWp2T1VDX19MYVlwQ2VCWklCcWd4UVhDRDFzbUlWanFSTnE2X0dnOXp1aHplUXRweDg1aDRKVEt6SWNHRjZTVk11UWdpcTZVdWczWHhKc2p0OFhmRjdyQVJJeFk4dWhOWWxXaTlLenNFMGdMaG5hQ1JQczdrVVM2bW9sUXFmUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 01 Oct 2026 08:00:00 GMT

## 新興題材：9月營收

摘要：新興題材：9月營收 相關新聞集中在：智邦揮別投信賣壓強彈！AI雙引擎發威，9月營收、Q4營收續創高 - Yahoo股市

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [智邦揮別投信賣壓強彈！AI雙引擎發威，9月營收、Q4營收續創高 - Yahoo股市](https://news.google.com/rss/articles/CBMi-gJBVV95cUxNNFJyNEJ5aHhwNDhDZ1RsOEJUcnhtXzl6V0RUZzVfM1VOSEdRYnAwbi1ULU9sQjFvaEl1WEFkODdNdzBJZFJlbmxKWDdiSFhDb0VtQnItLTl2eERrQ0E4RHYwcFNqREswSUJwcWU0VUJGSEczSXB6VVhldDgyTFRCcXQ0QW53dmVYTEs5YTZlT1pLMHZPY3FzdVJRM3VMU1lMVlhGeG5OVHlPLVhGQjlzVy1TODcxek95WVR6SkdudmN4ZElqd0F5UW5Pa0V4X2ZQbGdIbmo3dkF5NnAyNEpLdHIyRFp1SGROWEtXVkFZNWhhRk5XV0dNNlk4ZXJPbnV3emFNd0wtbXpQQmFQcEd4MXl1cDBZTDAwQ1ZUSU5qQ2NleF92MTdSQm8xdUw4OWxpQmplMVcyS2VWZDh3UnJyNEhEc0I4cXJnYzgzcmxUTHpKYkM0aXRVYllQc2c4RXVvaGYxRFp5VGpXMVliNVM0bTFEcXJWMW1tT3c?oc=5) - Google News source discovery | Yahoo 奇摩股市 Thu, 01 Oct 2026 02:52:19 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
