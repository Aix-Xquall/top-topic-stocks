# 每日股市熱門話題分析 - 2026-10-29

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **綜合市場情緒**｜正向｜熱度 49｜市場確認 38.75｜同向 1/2
2. **記憶體與 HBM 供應鏈**｜正向｜熱度 7｜市場確認 77.11｜同向 2/2
3. **新興題材：TradingKey**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0
4. **半導體與晶片供應鏈**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0
5. **AI 伺服器與資料中心**｜正向｜熱度 11｜市場確認 29.13｜同向 3/8

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.05（樣本 14）
- 5日相關係數：0.04（樣本 11）
- 同向比例：6/14

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 綜合市場情緒 | 38.75 | 1/2 | 0 | +1.25% | +0.46% |
| 記憶體與 HBM 供應鏈 | 77.11 | 2/2 | 0 | +2.37% | -4.43% |
| 新興題材：TradingKey | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 29.13 | 3/8 | 3 | +0.96% | +1.66% |
| 新興題材：完整台廠供應鏈 | 0.00 | 0/1 | 1 | -2.45% | +7.64% |
| 關稅與供應鏈轉移 | 0.00 | 0/1 | 1 | -2.45% | +7.64% |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 相關性偏弱；應提高同向價格確認權重，降低泛 AI、泛半導體等寬標籤推估權重。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-10-16 | -0.13 | -0.25 | +64.00% | 25 |
| 2026-10-17 | -0.10 | 0.49 | +26.32% | 19 |
| 2026-10-18 | -0.12 | 0.33 | +21.74% | 23 |
| 2026-10-19 | 0.44 | 0.36 | +50.00% | 12 |
| 2026-10-20 | 0.09 | -0.81 | +69.23% | 13 |
| 2026-10-21 | -0.25 | 0.23 | +5.56% | 18 |
| 2026-10-22 | 0.02 | -0.21 | +38.89% | 18 |
| 2026-10-23 | 0.35 | 0.29 | +78.95% | 19 |
| 2026-10-24 | 0.09 | -0.31 | +70.00% | 20 |
| 2026-10-25 | 0.41 | 0.78 | +64.29% | 14 |
| 2026-10-26 | 0.27 | -0.25 | +36.36% | 11 |
| 2026-10-27 | 0.07 | 0.31 | +50.00% | 18 |
| 2026-10-28 | -0.30 | 0.47 | +20.00% | 15 |
| 2026-10-29 | -0.05 | 0.04 | +42.86% | 14 |

## 歷史回測摘要

- 回測日期：2026-10-29
- 近5日 3日相關：0.45
- 近5日 5日相關：0.16
- 同向比例：+41.18%
- 權重狀態：已調整

- 方向準確度：+41.18%
- 信心排序準確度：0.45
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

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股開盤跌20.71點 - 經濟日報；台股年底作帳行情啟動 強勢反彈 重新站上 47K - 經濟日報；台股中小型基金 搶鏡 前十強近三個月報酬率都超過5% - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | +0.38 | +0.21% | +0.21% | 2,420.00 | 2,480.00 | -2.42% | 未明確 | 86.28 | 28.11 | 511.86B TWD / 54.65% | 2026-10-01 |
| 2454 聯發科 | 新聞直接提及 | +0.51 | +2.29% | +0.71% | 4,165.00 | 4,920.00 | -15.35% | 同向 | 60.69 | 69.94 | 55.40B TWD / 1.97% | 2026-10-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 2 篇新聞命中。
- 2454：新聞直接提及「聯發科」，共 2 篇新聞命中。

### 主要來源

- [台股開盤跌20.71點 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9TZTBzbDdOcktReFFGN0hicTlhbXJlb0pELVU2OVZQY2FPeDIzMDlvbWZCbzhaUF9ZblFjNm13QnFOOHh1RFJqdDlBaEI2TzMxYUprTzU3eW1CZ9IBX0FVX3lxTE81YUYyYjluaS0wS0VOX2trYmtSci1id2VTLThHUVhfRVhBZW1aUHg5eURPOWVoV2JYUkswUUJZN0pGSlhwS1ZGM2xxLXhnUkZtU2ZPNzg0Y3ItaEVWUER3?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 29 Oct 2026 01:18:53 GMT
- [台股年底作帳行情啟動 強勢反彈 重新站上 47K - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1Rc0NIR2l5VnBiT2dwcjdrOUN2bWhRaTJvbmdvSnAwUk8zSmVPQWJNNEcwRGctTUNSMERsMk02QkZGY0owM2lPODJ5di14aEI4OU9FQVZqZnVPZ9IBX0FVX3lxTE9YZ2ZjdEExNWFwT0FKRHF3QWhJZXFlbG5wQVVOYTZMYXItakVfZmtwZ0JtbVdpYVYtWm9HWVZEektnUWhCdDV1T3gxUmVfUnVHTzJmRW1yTGljaS1CalJz?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 28 Oct 2026 17:50:13 GMT
- [台股中小型基金 搶鏡 前十強近三個月報酬率都超過5% - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9mOUtoOWRyLXl6MHRxWlJVV0ZWSFNZX29CNzIyS1JsTXotX2FhRXlwOENMVkh6M2dHb2hBVHc0OHJsdXFfU19lZnZlM0p2cXJ4ZDUxQV9TTUhvd9IBX0FVX3lxTE9oT3NhQjJ1d2FONTdVQ2pod1RyOFJjM1RiQ3FiaW9YTHFYcGpHcXI5SHFIR1U3ZkZSVEhRSFJBN0hlcXBFWHhNaDFxRzJzNWhfNmtxaHNxS25acmVIRVRZ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 28 Oct 2026 16:32:10 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：SK Hynix Jumps 7%, Micron Rises 3% on Memory Shortage Call Through 2030 While Seagate Slips Despite Upbeat Guidance - 24/7 Wall St.；AI memory, chip stocks gain after SK Hynix posts record profit (MU:NASDAQ) - Seeking Alpha；SK Hynix Jumps 8% After a 632% Profit Surge and a $45 Billion Shareholder Pledge. Micron and SanDisk Are Riding Along. - 24/7 Wall St.

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.59 | +1.26% | N/A | 983.23 | 983.23 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.59 | +3.48% | -4.43% | 1,304.84 | 2,335.00 | -44.12% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -2.45% | +7.64% | 215.38 | 228.38 | -5.69% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、MU、memory」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：surge, shortage, upbeat。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 2 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：surge, shortage, upbeat。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [SK Hynix Jumps 7%, Micron Rises 3% on Memory Shortage Call Through 2030 While Seagate Slips Despite Upbeat Guidance - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi7AFBVV95cUxOeVNReGxhbnBQeHdLSG1kczcwcFRpdFMxaEdfYnZwNXZFR0NHeVd2SEc3aTQ1U1lsN1pUQ2t6bkhibDBEUHQ5LXVZUHpzVm1aSDNYX3hVV1Q0ZU1rd2RKc3pXVlJEajg2bVE0NENyRlNBeFJqbU1YTjhOaHhRX3BrRlFyeFVZN09xX29uUkJ0bkFMZGZsUHVoSXU2aFNQdlJrcXZFbWdyNFp6V191RmZ2RGNnM1BQbEJQSnhlLWhETlBoQk90NldEZno5NGw2clpJQXRzWndvMVYtcFlaRXZQUkFLaUQ3cXJuY2NvQg?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 28 Oct 2026 14:07:00 GMT
- [AI memory, chip stocks gain after SK Hynix posts record profit (MU:NASDAQ) - Seeking Alpha](https://news.google.com/rss/articles/CBMioAFBVV95cUxQRjMxTUN4S0NxcDNKT0ZXclUzV3VVTTRiclRZeU0wZngxblpEamx0dk0ybFVsNC1XNVpwa3oyZnhlLV92ZHh5SmdpN3VfbXNILUtLWmJTbWh1X0VobDdEaW5fWXhUZWJzdDE2aExVRDloWE1KUUdXTzZXNkFESnZ6ak9iZFRBSzZxVEYwRi0xejRMZXRoQ0RtU0xrSVI4N243?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 28 Oct 2026 09:35:27 GMT
- [SK Hynix Jumps 8% After a 632% Profit Surge and a $45 Billion Shareholder Pledge. Micron and SanDisk Are Riding Along. - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi7gFBVV95cUxPeUp5VnNGRUlqeWJxSGdyOWxxQWhYWGl6a1ZRa3RQMXFUTktNZkx2alVWWUZBTUV5QjBHTzZnTzVoSGZJUmhpVE1rX2VOS3NaNmFuX3BtLUFhV1c3MTYzZGY1Vi13dXFfMGQyMTVrQTJ0SlpYUGl6N0xVVnUtZHZac0YtNC00U25XLXhMa2RFc2ZJaGs0azR2bnJuZ2l6N1I3bERxbG4yRVVHMFJpTFpsczRLalprU0VpVG1HUC1jdkxuZ0JqUXpCZmFZc2lHOXFnRnIwZmsybTRtQ3VEdW1Hd1ZlUFJhbzF3dEtJaHB3?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 28 Oct 2026 12:04:00 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Micron Technology Inc Stock (MU) Opened Up by 4.81% on Oct 28: What Investors Need To Know - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | +1.26% | N/A | 983.23 | 983.23 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Micron Technology Inc Stock (MU) Opened Up by 4.81% on Oct 28: What Investors Need To Know - TradingKey](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPRHN4dlpxOS1ORFA5TlVZNmVDS1FMbXd2eEJfU1dDLVlFNW5HV2NXNmN5SWhrWDZVcjB1UWVzaEM1X08zUGE1eHF2Z2tLbWU0bE9sUEpWMXN4WEJNZE1UbEVQODVZWFB3aFVqTUlJNGI1M2tCS05qSk9Ud3c3UHNMVDdwRmhxb1NG?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 28 Oct 2026 13:47:22 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel to report Q3 earnings as chip stocks continue to rebound - Yahoo Finance；魏哲家：他的研究，改變了半導體產業- 書房 - 工商時報；劍橋研發 10 美元「微型光譜儀」晶片，智慧手錶無痛測血糖有望成真 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | -16.70% | N/A | 95.53 | 114.68 | -16.70% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +0.21% | +0.21% | 2,420.00 | 2,480.00 | -2.42% | 不適用 | 86.28 | 28.11 | 511.86B TWD / 54.65% | 2026-10-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | 0.00% | -2.66% | 120.50 | 164.50 | -26.75% | 不適用 | 6.80 | 19.25 | 25.35B TWD / 27.22% | 2026-10-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -2.45% | +7.64% | 215.38 | 228.38 | -5.69% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | +12.08% | N/A | 578.44 | 578.44 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | +1.26% | N/A | 983.23 | 983.23 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | +3.48% | -4.43% | 1,304.84 | 2,335.00 | -44.12% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -5.00% | -6.87% | 351.81 | 446.77 | -21.25% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 1 篇新聞出現相關標籤。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 1 篇新聞出現相關標籤。

### 主要來源

- [Intel to report Q3 earnings as chip stocks continue to rebound - Yahoo Finance](https://news.google.com/rss/articles/CBMivwFBVV95cUxPbkctcG9uQk10dUx1NUxmQXFvcTg4TkVzQTJBVWhMVmJjdVo5S0lGOWxXYWFmdnZyX3JGOVBmaWhYRFNmTHZ1Rkk2T2RKTXFxa3VrU3lRQ2ZBM3B3eDhzUGQ1NlpSbjlGMWpRajJXOXEzbDBob0xaRTlna2hxeE94X0JNdmdaLUU0UUR4eURaYlhmTmY0SERKNFk1R1dzTGZ6anBmQVZFLVgtQVh4OUFMYU96Mzk1NHBZVUJ1VWJqMA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 28 Oct 2026 22:17:13 GMT
- [魏哲家：他的研究，改變了半導體產業- 書房 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBHQ25nTGhYQmkwUUs1Z0ZXR3ZiSFU1Tk04LVlZLUdWV2V2ZWFvR2RwWkMxUDlMeDV6SnZwN3luZjdFeGpkWjA3dk81NXNVRXpsUUNWWnFNNDFrRDI2X3VF?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 28 Oct 2026 01:01:00 GMT
- [劍橋研發 10 美元「微型光譜儀」晶片，智慧手錶無痛測血糖有望成真 - TechNews 科技新報](https://news.google.com/rss/articles/CBMicEFVX3lxTE8zMWJqX3V5RTVUdjJRaTdoaEpCSlNxdko2d3MxVU56ZHpxXzdxXzZjeDFFeEswbjBfMldxSEdMalBtVVpETi1sNUFSXzhNakplcFRGcUpKWHdLT2NHd216WGtzT29hMzc5UmFTVVo3Yzk?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 28 Oct 2026 00:33:14 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Can Higher Data Center Revenues Propel Intel's Q3 Earnings? - TradingView；Meta 前 AI 主管創業 Ndoc，打造原生 AI 辦公軟體挑戰微軟 Office - TechNews 科技新報；科學家揪出 AI「痛感訊號」，放大後竟讓模型大失控 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.28 | -16.70% | N/A | 95.53 | 114.68 | -16.70% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 新聞直接提及 | +0.51 | +17.94% | +7.93% | 531.01 | 531.33 | -0.06% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2303 聯電 | 新聞直接提及 | +0.32 | 0.00% | -2.66% | 120.00 | 164.50 | -27.05% | 未明確 | 6.80 | 19.25 | 25.35B TWD / 27.22% | 2026-10-01 |
| NVDA 輝達 | 產業/供應鏈推估 | +0.03 | -2.45% | +7.64% | 215.38 | 228.38 | -5.69% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.06 | +12.08% | N/A | 578.44 | 578.44 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.04 | +0.21% | +0.21% | 2,420.00 | 2,480.00 | -2.42% | 未明確 | 86.28 | 28.11 | 511.86B TWD / 54.65% | 2026-10-01 |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -5.00% | -6.87% | 351.81 | 446.77 | -21.25% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.04 | +1.61% | +3.73% | 701.00 | 703.00 | -0.28% | 同向 | 13.92 | 50.29 | 88.13B TWD / 45.52% | 2026-10-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MSFT：新聞直接提及「微軟」，共 1 篇新聞命中。 同時符合主題標籤：AI, datacenter。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2303：新聞直接提及「聯電」，共 1 篇新聞命中。

### 主要來源

- [Can Higher Data Center Revenues Propel Intel's Q3 Earnings? - TradingView](https://news.google.com/rss/articles/CBMitAFBVV95cUxQQURNNUYtWE4zX0VXbDhMcmhBZnNQcVNwQjJlNWJoRy11VjlEY3UwUTFEdlhFVXM4ZjNSS2xKZjNEQV8xSjRLQXFyVXNLRDhYNTMzTW5ENkNFVnJ5Q1NJMzJoNjUyQU1HSjVtT08zcERlOHBGUWs2cGphRG1yY3JSUVBZOUcxT2dGdTl2b2M3N1prM0NNcVhNN2tBZHU4bG9ZMjdwWWktQ05hREV4RlZuc0UwYlc?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 27 Oct 2026 16:37:58 GMT
- [Meta 前 AI 主管創業 Ndoc，打造原生 AI 辦公軟體挑戰微軟 Office - TechNews 科技新報](https://news.google.com/rss/articles/CBMimAFBVV95cUxQT2VXUUs4enVXMlZKeHFZb1UwdVAyaHZwQ3lEY3ZzMFMyZnZuWW52SlpuS0ZQLW1aSE5CZ3JjRFpNaW5aVk0xdE4tNG11cUlnUkRBVXp6cjV5WnpEcjF3czQtVkFLeFRYeWJJUlZrYnFZZExCaGNNYk9oV3ZzcWJrVWZZY1pNd0NmRlpKdUxXcHlrZHI2cGsxRA?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 28 Oct 2026 23:42:21 GMT
- [科學家揪出 AI「痛感訊號」，放大後竟讓模型大失控 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiaEFVX3lxTE5lTUxzN2xQbk9mUnZjamV0cGpVbm1fdG8tMzZiVHBRVjItX2NLWmk0akt5ZkZIUFllZjg4bDlCcE51eTEzdzhDTW9FVEZEZ0FpZEJIZTVkX0dPWThaLUlqbEI4S0dlYmdY?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 28 Oct 2026 23:42:21 GMT

## 新興題材：完整台廠供應鏈

摘要：新興題材：完整台廠供應鏈 相關新聞集中在：整理包／黃仁勳概念股笑了！輝達季度財報超預期 完整台廠供應鏈名單、潛在受惠股一次看 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.21 | -2.45% | +7.64% | 215.38 | 228.38 | -5.69% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [整理包／黃仁勳概念股笑了！輝達季度財報超預期 完整台廠供應鏈名單、潛在受惠股一次看 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBQUlViSHpPeDVlY29yaHFNNE5NcVlUQnE3ZThTcXRGNHgxYTVPOVVTRDlaTDV6Zml5WEwxVHNSeGFDcnVHUHhRSW15SzNpU0dYVDU3dThWNEVCbkZI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 27 Oct 2026 09:00:00 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：整理包／黃仁勳概念股笑了！輝達季度財報超預期 完整台廠供應鏈名單、潛在受惠股一次看 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.21 | -2.45% | +7.64% | 215.38 | 228.38 | -5.69% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +10.18% | +23.30% | 343.83 | 347.10 | -0.94% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | +0.60% | +5.01% | 250.50 | 289.00 | -13.32% | 不適用 | 15.21 | 16.58 | 1158.63B TWD / 38.42% | 2026-10-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [整理包／黃仁勳概念股笑了！輝達季度財報超預期 完整台廠供應鏈名單、潛在受惠股一次看 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBQUlViSHpPeDVlY29yaHFNNE5NcVlUQnE3ZThTcXRGNHgxYTVPOVVTRDlaTDV6Zml5WEwxVHNSeGFDcnVHUHhRSW15SzNpU0dYVDU3dThWNEVCbkZI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 27 Oct 2026 09:00:00 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：國票證券：台股市場追價意願仍偏審慎- 新聞 - MoneyDJ；《台股盤後》電子股領軍攻高 收漲939點/重返47K - MoneyDJ；統一證券：台股估呈現高檔震盪格局- 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [國票證券：台股市場追價意願仍偏審慎- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPb3NmWkNsQlFhOGRVaEpySU1LRWUxd0NNcnhXNkZFUW51M2VRYWdDMk4zOUR1MS1ZcVhHTVV6eHZtYTkzTDg4X243RGExTkhQc3JFV2taemM3YnNSZWRNRUN6YXhmRkVLTDdEMHFLMDhFcjVpS2NJb00tQzJCOE41N1N2VUY5MVU4M3k2WHVOM19zQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 29 Oct 2026 00:38:00 GMT
- [《台股盤後》電子股領軍攻高 收漲939點/重返47K - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxOZXk5N09hbjhfRHVsTWF0eUZuaU9hUVNHbGVFSGpCbnByNGJlVktrZklxdEluYWZyMURpaWxnczN1aVBQekJoeGx5YjVlWWhmR29zSC1EejBIbE5kT21HSnhmMXNGT3E0OFJfZUkzS29pTUg5Xzh3S3p2ZVZmOEdMZ0Vpb3ctNGZrNmFxYXktbDNPUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 28 Oct 2026 08:00:00 GMT
- [統一證券：台股估呈現高檔震盪格局- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNbHBUZE9US3RBbDZLR243U0I2dUtac2dwd3FzWXpMa3BvWUtKOXhiTFI3TDRFN2Zud3FIa0lzOS1wS0I5NEFOUlU5OC04aXVnY2Z2NExoanhTaldiOG1lYUlfa09YYlF3dk9QbTVGQXBYbm1XUkdTaUt6REhhaU9JZmZtVlYwb0Fkeko3RjdUdjU5QQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 29 Oct 2026 00:38:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
