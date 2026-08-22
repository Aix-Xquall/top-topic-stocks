# 每日股市熱門話題分析 - 2026-08-23

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **AI 伺服器與資料中心**｜中性｜熱度 11｜市場確認 N/A｜同向 0/0
2. **記憶體與 HBM 供應鏈**｜中性｜熱度 5｜市場確認 N/A｜同向 0/0
3. **利率與成長股估值**｜負向｜熱度 2｜市場確認 N/A｜同向 0/0
4. **關稅與供應鏈轉移**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
5. **新興題材：NextG**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：N/A（樣本 0）
- 5日相關係數：N/A（樣本 0）
- 同向比例：0/0

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| AI 伺服器與資料中心 | N/A | 0/0 | 0 | N/A | N/A |
| 記憶體與 HBM 供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 關稅與供應鏈轉移 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：NextG | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：ic挖角Google晶片 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
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
| 2026-08-22 | N/A | N/A | +50.00% | 2 |

## 歷史回測摘要

- 回測日期：2026-08-23
- 近5日 3日相關：-0.02
- 近5日 5日相關：0.09
- 同向比例：+50.00%
- 權重狀態：未調整

- 方向準確度：+50.00%
- 信心排序準確度：-0.02
- 診斷：低相關

調整原因：近 5 日有效樣本 12 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：AI 伺服器與資料中心 相關新聞集中在：2030 年產值衝 1.6 兆，AI 系統整合是關鍵？ - TechNews 科技新報；AI 性別偏見如何影響兒童教育科技產品？ - TechNews 科技新報；擴散模型跨足晶體重建，預示 AI for Science 哪些新趨勢？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 新聞直接提及 | 0.00 | +23.04% | -4.63% | 483.24 | 506.69 | -4.63% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 90.07 | 114.68 | -21.46% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +7.31% | +7.59% | 214.72 | 214.72 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 473.25 | 516.10 | -8.30% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +1.26% | +0.63% | 2,410.00 | 2,425.00 | -0.62% | 不適用 | 86.28 | 27.94 | 467.58B TWD / 44.69% | 2026-08-01 |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -2.46% | -11.73% | 368.45 | 446.77 | -17.53% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | -2.00% | -4.71% | 587.00 | 680.00 | -13.68% | 不適用 | 13.92 | 42.47 | 73.78B TWD / 43.15% | 2026-08-01 |
| 2454 聯發科 | 產業/供應鏈推估 | 0.00 | -2.45% | -9.98% | 3,790.00 | 4,310.00 | -12.06% | 不適用 | 60.69 | 62.59 | 48.47B TWD / 12.16% | 2026-08-01 |

關聯理由（前 3）：
- MSFT：新聞直接提及「微軟」，共 1 篇新聞命中。 同時符合主題標籤：AI, datacenter。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [2030 年產值衝 1.6 兆，AI 系統整合是關鍵？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMickFVX3lxTE1ubkFseTQySG9xMFl3YmEzVEFSbE5IQkVuVW1XN0ZXcXB4S0UtVnpKUGRmd0dybmEtQVlOeUp1ZW5VSmNVRVVVbVZmZUhXd1lNaGFSNVM5Vi02TmtxLVMwMzVBQmxYUkRsbWkyMlg0bF9lUQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 22 Aug 2026 20:09:13 GMT
- [AI 性別偏見如何影響兒童教育科技產品？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiqAFBVV95cUxPZHZtbDVDYUJpal9BeS1rQXNodlFsSk9vOWZVZVppVko3aUxGaUdpOFVDV2lrRFd1dC1hTGUtZlB4T3FpcmJOZFc0aDN0YW5qeFlGYUpYeXUzejV4bDUtZEFZVzRKRkx1WlFsbGNjd0lKSURucGRHc2ktWTNxWC1obS1ac2xxNTd1RlJwWW1RZmtLdnJ5X1UtQTk1R29USm5TODFSM28wUFA?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 22 Aug 2026 18:40:51 GMT
- [擴散模型跨足晶體重建，預示 AI for Science 哪些新趨勢？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMingFBVV95cUxPV3hYYjZRWE5VLU5ZUVlmd2FNSEEydnJSUG1GVzd6Y2FSb2V5Zk5ZWTFrMnd6NmlBVC11aEpMczNtamdfck5UU2FwaHloZ3dUOEdzU2Y4TFFrWmttOTZmSjNYY2Y5ZEFVamdtOGRNdXBpYnA2S1NzNE81anQ4TnFVR2tGNDhXQktkVGo4MHNyTkVtOG5RUTVZcldScnJaQQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 22 Aug 2026 18:42:40 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：AI Money Moves Put These Five Stocks In Spotlight Last Week: NVDA, INTC, ORCL, AMD, SNDK - Stocktwits；These AI Stocks Could Crash But The Opportunity Is Huge (Micron Sandisk AMD Nvidia SK Hynix SMH ETF) Restaurant (4r1PXOJbkl) - Mshale；SanDisk Rallies 8%, Western Digital Rises 6%, Micron Gains 5% as Elon Musk Flags a Memory Bottleneck - AOL.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 966.78 | 971.00 | -0.43% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | -1.83% | -2.74% | 1,596.08 | 2,335.00 | -31.65% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +7.31% | +7.59% | 214.72 | 214.72 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | N/A | N/A | 473.25 | 516.10 | -8.30% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 90.07 | 114.68 | -21.46% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | 0.00 | +1.26% | +0.63% | 2,410.00 | 2,425.00 | -0.62% | 不適用 | 86.28 | 27.94 | 467.58B TWD / 44.69% | 2026-08-01 |
| 2454 聯發科 | 新聞直接提及 | 0.00 | -2.45% | -9.98% | 3,790.00 | 4,310.00 | -12.06% | 不適用 | 60.69 | 62.59 | 48.47B TWD / 12.16% | 2026-08-01 |

關聯理由（前 3）：
- MU：新聞直接提及「Micron」，共 3 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK、SanDisk」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVDA、NVIDIA」，共 2 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AI Money Moves Put These Five Stocks In Spotlight Last Week: NVDA, INTC, ORCL, AMD, SNDK - Stocktwits](https://news.google.com/rss/articles/CBMi4AFBVV95cUxNd2pVcHZnd2ZRY2JnQldxNE5YdUNFSzNEUGdoVzI3S0ZhcWZ5UVp1elNzV3ZvTnMyb1BNbmRrU1FlejdPcldpRngtbS1LSWx5b3VITWlfZU83eGdsbGNLWlRZaV9rR29KbjFQRE1ENFRnS1Z0Rm5GT1pBTzZ1VjJyckhVejNRZHNaSWU3NTI4eGFpbWw4RDdhaktXU1JMNmc3VUt0enBwSmotRGEwU00wcUpLVUhVaTNkcmZFUjBtLXdiR0IwSTNVdUw5MXpJS2xWeEJZYmZ5SU1uYVE0R3pzQg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 22 Aug 2026 12:23:31 GMT
- [These AI Stocks Could Crash But The Opportunity Is Huge (Micron Sandisk AMD Nvidia SK Hynix SMH ETF) Restaurant (4r1PXOJbkl) - Mshale](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBjRy11bHV3MlZQb25NMFU2MkcxN01BLTlyRlFLQ0FxUnkwZy1BRFlVZFdTUUF2aGRkeHpUMVZ6RGg4MDl5MklKLUhYTUJTVC1ZQkhSSndlVWU4ZkU?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 22 Aug 2026 06:29:13 GMT
- [SanDisk Rallies 8%, Western Digital Rises 6%, Micron Gains 5% as Elon Musk Flags a Memory Bottleneck - AOL.com](https://news.google.com/rss/articles/CBMigwFBVV95cUxNRHhHN3R0Wjg3ZHo2MnBhSTd5Zk1fNjhnLWRnbUdZY0JWd1hyNlhZNmtQUUVJYTBPWU9WMGhjU0VMal9BTHNMSHBvdkZlNEF5alI0bFQ0Q1hmdm51YzhNcXk3OHdaSUpGb3hETERlUFJXN2FBbGZDNWRLSVJiUXZsNTZvSQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 21 Aug 2026 20:22:27 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：Bessent's bond gambit aimed at calming markets is instead stirring inflation worries - CNBC；美債殖利率恐戳破美股泡沫？分析：高估值與AI循環融資風險升高 - news.cnyes.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +23.04% | -4.63% | 483.24 | 506.69 | -4.63% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Bessent's bond gambit aimed at calming markets is instead stirring inflation worries - CNBC](https://news.google.com/rss/articles/CBMivgFBVV95cUxPbFduci0wN2hKbnNSSWY4OVhUVnZSMU9TWFpCS2xtU1AyZlZudHJJTFJneW1weXNpelUwY0JlaUp4VC0xZFdLVERSYWRablV2LWRWaTU3cVVuOVB1N2ktOEdteno4eU8wRTRjQ2NPY3RVM1N6amxsSzA0TnIyeHZVZFU3MEx0QzB5VGJDRDNLZ0pVRTdtUHNkaFRWX0k5YnZMbkZ4bWpHeDA2bUFvNzJzR3ZKTlVTekEwRVFmZm9n0gHDAUFVX3lxTE8zSnhXOEp2SjVHTV9jRVNGQTd4ZTVzaVBVUzUtM3EyTjNMN1pfcG1peGVlZVBEeWtueVRDSHVpdkdjZ2x1dkF3UFdzT0VDaW5sakVmVkhrcUxNdVFKV21zSHBZWGRySDhIUEJvRkUtX3NVdGZxRXE0RTg3b2tsVEZpNmpZRndJNHNydHZZc2xrbHljQ1hEdjc1SWwxNTA5cDN1S2dQUldMSXhRaE1CLW1VNHZkeEpaa3YtOFhQRXpfLWJvSQ?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 21 Aug 2026 17:51:10 GMT
- [美債殖利率恐戳破美股泡沫？分析：高估值與AI循環融資風險升高 - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTE1wVnN1UmY2eGpvZk0tNEdtQ2NzYzZGOXY2NnFsYzRsY2xrMkZldloyaFYyS0QxYjBOZVZuaUt5eU81UmxrS2syYmd3dHhTd00?oc=5) - Google News source discovery | 鉅亨網 Sat, 22 Aug 2026 05:31:11 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：SEMI半導體材料聯盟成立促供應鏈完整及在地韌性| 產經 - cna.com.tw；SEMI半導體材料聯盟成立 串聯全球資源強化半導體材料供應鏈競爭力 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +17.10% | +33.26% | 309.35 | 312.06 | -0.87% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | -1.41% | -5.39% | 245.50 | 289.00 | -15.05% | 不適用 | 15.21 | 16.18 | 946.51B TWD / 54.19% | 2026-08-01 |

關聯理由（前 3）：
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [SEMI半導體材料聯盟成立促供應鏈完整及在地韌性| 產經 - cna.com.tw](https://news.google.com/rss/articles/CBMiXkFVX3lxTE5kaGc5dzFTYU1wTHNwMHVZNHZNak1wam5DNjFFTVJodk8xM1l4Tmt2SVlXbjNpaXFvZTFLNEtVX1Bja0NTeVFjMDAzaG1XRld0MVpJLWhQOEdqVHI2cUE?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 21 Aug 2026 07:10:00 GMT
- [SEMI半導體材料聯盟成立 串聯全球資源強化半導體材料供應鏈競爭力 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBOc3R0dkhNaENyY0lQRGhTSDc3S0xlc3BpQjNvcFc3aWlHTXo2bkhoSVRrMFI4VkRoR2tVZkFPUXpuemlQUkUtR3dIY1pwcE1MREhKRjV3T0czd9IBX0FVX3lxTE53eU52WFAzTWltbVllSzlBMDR0RVN5VGtBY0xBdW1LbTRqSURQWGVGOE1vUnpEQUkzbzNSZWJPLTk5bkVPSzRqckhvb1AxZ1BJTU9BSlZjVm9zMHUyNE9Z?oc=5) - Google News source discovery | 經濟日報 money Fri, 21 Aug 2026 14:44:37 GMT

## 新興題材：NextG

摘要：新興題材：NextG 相關新聞集中在：Intel (INTC) Pushes Into NextG Testing With Large Scale Open Source 5G Trials - simplywall.st

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 90.07 | 114.68 | -21.46% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel (INTC) Pushes Into NextG Testing With Large Scale Open Source 5G Trials - simplywall.st](https://news.google.com/rss/articles/CBMiygFBVV95cUxOako1M2NOc3VhUXVETG4tUG45X1phZFVsbVlOS1YySWgtZWVYVTMtUl9KU2ZVN0VxWUxJYXY5WG16bGp3Qlh6ZU9Qa3RZVG95N05Hd3ZYV2JsTG8zdnRVSmtqT1A4MU9TcTB1WlhFd1J3TklsaUxOdkRjb1IzUDVzaUcxa3U2cnAtQTFGUVk2bjhmZ1V2QzRoNEdlRDJUWkF5S3RMbmh4Z0dCdy1vWFZuaUFwLVdPb2JSd0UzODVRcUtCLTZ1MDJHMnpn0gHPAUFVX3lxTFBiWUhIY3NQMmt1RGVYUXV6U0xYX0U1RjZfVDBfMUhFMnE4TTVaMzAyNWc3d2RmLUZ3TDREWV9vR01QRTFNSGl2MWRaQmlWaExoSWZyZVB1V2VjaUVnSDVmUGQ1TEx2cE9keDl6ZXVNRTRtUUM1TlV4S0hoeS1lYXBpd2s4ZzNuY0tfLS1rMDR0VjFjU19mU2k1M1dWVlByMnN1bWRhUWNPelFLNmEzTDRISGRsQm53anI4aVFQZC02ZGNNSjVzb1hHdmRiS1NjQQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 22 Aug 2026 00:44:19 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：群益金鼎-中壢 對 金山電(8042)個股 單一券商歷史明細 - justdata.moneydj.com；兆豐-公益 對 材料*-KY(4763)個股 單一券商歷史明細 - justdata.moneydj.com；統一-城中 對 順藥(6535)個股 單一券商歷史明細 - justdata.moneydj.com

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [群益金鼎-中壢 對 金山電(8042)個股 單一券商歷史明細 - justdata.moneydj.com](https://news.google.com/rss/articles/CBMikgFBVV95cUxPaGpjemRHTS1wa2YzUHRSQ2tnNVVwXy1OY3h3ODFpbjVodDdXQnVjTF82R2c2YW56NHNlU1VsUDJSVVk1eXdrSHhzeURFZWptR2xoVlBFQTJFV2ZvWTd0bl9xZkRSQmxTZmptczB4OXRjOV9MQ2tXWUwyUm1ERlJydUJBMEUzVWQwV2FEa2tuc0cxQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 22 Aug 2026 13:50:35 GMT
- [兆豐-公益 對 材料*-KY(4763)個股 單一券商歷史明細 - justdata.moneydj.com](https://news.google.com/rss/articles/CBMikgFBVV95cUxPMDMyQjRvZDhadER4TGdZZklQYnNyQ1c5QkQyWk5iaFJCcnZKbWZPNnpkLUNoNGJJRjFYNXNobU5LU2M0N1RhZnJETXdIdU1rZTBhSjJvYmEyUnJzWktiMUUzWXdLSVRZa1BaYzNHLS1sS0ZoVFNFTkRfekx2M3pEU2tQVEU2OC1oX1IwXzlTT1g4dw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 22 Aug 2026 11:45:48 GMT
- [統一-城中 對 順藥(6535)個股 單一券商歷史明細 - justdata.moneydj.com](https://news.google.com/rss/articles/CBMiggFBVV95cUxQLWRRRDF6ekREYnNnak5qZ2t4alZTS25KY01jYlVEWFg2dHNLNGQ0X1RjREMtbEY5RmprWngzN2lWUEx0bzF5SnduejFQLWhha3pNNzNXeGJmdlBZRDFGdlVEUndYaTJjd3FBQzFtZkxzNmpseE1MOHhKTk91ZjF2NzB3?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 22 Aug 2026 09:52:50 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：個股動態報導內容-9B7633E0-F8F8-49D3-96E3-421DD539392D - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-9B7633E0-F8F8-49D3-96E3-421DD539392D - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxPNHRPYWRqRzMtdHh4aFBBZV9wUXBjeFo3d1I3eFA4TUgycGhlZDhZc1JJaTZtdUF4MXB3S3loMmlYVjM1Q1BMVUN5Q1JJb1pqRFpjN1hmOWMtY2d4cWFBb1RKSHJ3WERzV0J2clNBVGJZbGZ4Vmd2VWcxN2pSVy1QUHRtZG1CY0RLTGFaSEF4Z3VZVkdN?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 22 Aug 2026 15:25:29 GMT

## 新興題材：ic挖角Google晶片

摘要：新興題材：ic挖角Google晶片 相關新聞集中在：Anthropic挖角Google晶片大將布局自研半導體| 國際 - cna.com.tw

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [Anthropic挖角Google晶片大將布局自研半導體| 國際 - cna.com.tw](https://news.google.com/rss/articles/CBMiX0FVX3lxTE0wQ2JfOFNUYkpaaDNtR0JFd2hDRkRjajVabDVhMUo4X0o4aS1ZdkdqcWVoNXc3S0lqZzBnTDZsNERWanVBR3lOc2xBTjUyTURBdDZnVUlvcENXVTFRVDRB?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 22 Aug 2026 06:53:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
