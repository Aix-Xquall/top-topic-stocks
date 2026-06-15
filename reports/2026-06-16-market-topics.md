# 每日股市熱門話題分析 - 2026-06-16

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜正向｜熱度 10｜市場確認 100.00｜同向 1/1
2. **AI 伺服器與資料中心**｜正向｜熱度 14｜市場確認 70.82｜同向 5/6
3. **半導體與晶片供應鏈**｜正向｜熱度 5｜市場確認 86.00｜同向 4/5
4. **新興題材：TradingKey**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0
5. **散熱與液冷供應鏈**｜負向｜熱度 3｜市場確認 0.00｜同向 0/1

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.39（樣本 13）
- 5日相關係數：0.50（樣本 13）
- 同向比例：10/13

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 100.00 | 1/1 | 0 | +28.28% | +28.37% |
| AI 伺服器與資料中心 | 70.82 | 5/6 | 1 | +4.16% | +7.44% |
| 半導體與晶片供應鏈 | 86.00 | 4/5 | 1 | +10.77% | +18.40% |
| 新興題材：TradingKey | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | 0.00 | 0/1 | 1 | -2.12% | +6.23% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：SpaceX | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-06-02 | 0.08 | 0.05 | +72.73% | 11 |
| 2026-06-03 | 0.48 | 0.62 | +90.91% | 11 |
| 2026-06-04 | -0.38 | -0.30 | +85.71% | 7 |
| 2026-06-05 | 0.31 | 0.93 | +50.00% | 6 |
| 2026-06-06 | 0.12 | 0.06 | +45.45% | 11 |
| 2026-06-07 | -0.32 | -0.20 | +45.45% | 11 |
| 2026-06-08 | 0.36 | -0.68 | +60.00% | 5 |
| 2026-06-09 | 0.07 | 0.19 | +25.00% | 8 |
| 2026-06-10 | 0.17 | 0.15 | +53.85% | 13 |
| 2026-06-11 | -0.05 | -0.08 | +14.29% | 7 |
| 2026-06-13 | 0.87 | 0.98 | +100.00% | 4 |
| 2026-06-14 | 0.82 | 0.98 | +100.00% | 3 |
| 2026-06-15 | 0.87 | 0.56 | +42.86% | 7 |
| 2026-06-16 | 0.39 | 0.50 | +76.92% | 13 |

## 歷史回測摘要

- 回測日期：2026-06-16
- 近5日 3日相關：-0.51
- 近5日 5日相關：-0.56
- 同向比例：+46.15%
- 權重狀態：未調整

- 方向準確度：+46.15%
- 信心排序準確度：-0.51
- 診斷：方向與信心皆需修正

調整原因：近 5 日有效樣本 13 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits；4 AI Memory Stocks to Buy Now Before Prices Spike Even Higher - The Globe and Mail；Micron Technology Inc Stock (MU) Moved Up by 8.00% on Jun 15: What Investors Need To Know - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.68 | N/A | N/A | 1,087.99 | 1,087.99 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.63 | +28.28% | +28.37% | 2,107.86 | 2,107.86 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.50 | N/A | N/A | 547.26 | 547.26 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.50 | N/A | N/A | 127.86 | 127.86 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +6.45% | +19.90% | 212.45 | 212.45 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、memory、DRAM」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 1 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits](https://news.google.com/rss/articles/CBMi0AFBVV95cUxOWm5KdEIwSXpyY191UEhDa1V6NVpWa01UbmpJeWRIV0ttT080TmpDNEhISW5TWkQwUzBVYzBqSHJPWXRVNVJCampoWWRlYmhKVkhIeHBJLS0wLW5Ua09GQnRORXpFcW5qTEJkcnJGcW55aU5rOFVOLUFMbjRPZEpWT3A2ZllucnM0SU9JNEdrNUwyc3V2WHAtNFk3VHl4R1F6SkZRMFpleEE2Zl9MdW4tSEpMMnFGZ2hQZURWQ3B1WDlPR1BhRjJELVN5ODJWYVR3?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 14 Jun 2026 17:06:03 GMT
- [4 AI Memory Stocks to Buy Now Before Prices Spike Even Higher - The Globe and Mail](https://news.google.com/rss/articles/CBMi3AFBVV95cUxPWVJDdTdDMFNxM0tDYWZVSU9kV3N2R0t6ZTNsWkMxVVBKSE42X3VsdVlMWjAxeGZQN2NHa0ZwSDM1SDIzZlBHYzZJQVFZR2ZVdmpBT1F5SElGN3ZlRTlLN3hWVlNwalJGWXgyZk1jRlREOXNzZmY4WVlpTTNuRjRxOGd1eGt3YW5XcndxSVlFQ3pMdzhVSE1KamxQSlk3c3B1RHdZSnJKTXNXb3FGNl8xeVZzRTByOUdkaXRIN1N0Um5kX3pGa3gwQm53d2Z0VE9ZTUY5dlhBQzVVNjgy?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 15 Jun 2026 15:28:42 GMT
- [Micron Technology Inc Stock (MU) Moved Up by 8.00% on Jun 15: What Investors Need To Know - TradingKey](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPMk5JMklrcXVXeFdYSUVkSFFzbzQ1Z1J4T0UyZGJiclBCTGtDX0NsYnJHaUNlbjhBMkdqRjlXYTJkbkQxTVZabGdTSVJuTWNISEpkZ0FLTElsMVpQVl94dTJobGJyV2V5aWxQT0tnenBpc1JRT0YwdmRObWFKZWszSlFWU0dSN3BC?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 15 Jun 2026 14:15:31 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：AMD vs Intel: Both Are Positioned for AI Data Center Growth But There Will Be Only One Winner - 24/7 Wall St.；Better Artificial Intelligence (AI) Inference Stock: AMD vs. Intel - The Motley Fool；Why Intel, AMD, Arm, and Other Artificial Intelligence (AI) Stocks Popped Today - AOL.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.68 | N/A | N/A | 127.86 | 127.86 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.68 | N/A | N/A | 547.26 | 547.26 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.06 | +6.45% | +19.90% | 212.45 | 212.45 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.06 | +5.32% | +3.49% | 2,375.00 | 2,375.00 | 0.00% | 同向 | 74.39 | 31.93 | 416.98B TWD / 30.09% | 2026-06-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | +1.79% | -21.10% | 399.76 | 506.69 | -21.10% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -5.63% | +23.28% | 393.94 | 446.77 | -11.82% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.04 | +9.46% | +9.26% | 590.00 | 611.00 | -3.44% | 同向 | 10.86 | 54.78 | 63.03B TWD / 28.57% | 2026-06-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.04 | +7.58% | +9.83% | 4,470.00 | 4,470.00 | 0.00% | 同向 | 62.91 | 71.24 | 47.43B TWD / 4.99% | 2026-06-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 3 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 3 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。 方向判斷命中詞：growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AMD vs Intel: Both Are Positioned for AI Data Center Growth But There Will Be Only One Winner - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi0gFBVV95cUxNUGVWenQxaG9tUXctUEhEVm84c001ZU5qb2tGSEt0RWk5YVBZaHlRcmhjUlZLQ05OZkNOeHU5YThTODJRRDg4SUt3VEgyaUMwcllPa2Jvb0ZUOGxuMG1fMndGcDlJTFpjTnVpb0l5Z1VZc2U1YzVfTHJXNW9vNHFNeGI2RHZMdlVQb0d0X0xBUGx5QXZqdFRzM3hzNVozWkkxTkRBOFV3TnFnc0RpT0h3cVdPWUtDRXNpZHJUOU9PX2ZSUEFCSTRLUVRvU21Meml4MGc?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 15 Jun 2026 19:39:32 GMT
- [Better Artificial Intelligence (AI) Inference Stock: AMD vs. Intel - The Motley Fool](https://news.google.com/rss/articles/CBMilwFBVV95cUxQRlRmZWx5Y2l2SEc0clU4NnRERUV1QlVBRWh3eUF3Y3RaRUREQ05aNEdaMjdESmVWSGg1VmlHSVZLcFFHd1lhanNMalk3M3Z1OGRCczhlRkJQMEhPcFI4UmJZTl83QzRIZVBBUEkyQnNWVURvVS10aTVyam1raW8xVXlaUGVlSjBWUEhvM1hyUlhyeDZCdzE4?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 15 Jun 2026 18:45:00 GMT
- [Why Intel, AMD, Arm, and Other Artificial Intelligence (AI) Stocks Popped Today - AOL.com](https://news.google.com/rss/articles/CBMidkFVX3lxTE0tZ3JDNjVEc0ppWWNCVkppUUQ2X1B5ZXJiTEVQanpEOFJnbTdVWFA3eWxRczlocG9xMDhoem52N0ZSUVF5QVRkQ2Q4ajFOZjJSV05peE1IR044RS0zZVEzX0h5SmpWaGtQZWswY1ViTFZhS2Q5YUE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 15 Jun 2026 20:41:15 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：AMD Jumps 8% to a Record High, NVIDIA Climbs 4%, Intel Rises 3% in a Risk-On Chip Surge - 24/7 Wall St.；攜手新北科學日培育人才 淡江大學教材將半導體製程科普化 - 中央社 CNA；台股波動完看基本面南亞科等15檔績優股出列AI、半導體最吃香- 日報 - 工商時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.61 | N/A | N/A | 127.86 | 127.86 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.55 | +6.45% | +19.90% | 212.45 | 212.45 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.55 | N/A | N/A | 547.26 | 547.26 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.04 | +5.32% | +3.49% | 2,375.00 | 2,375.00 | 0.00% | 同向 | 74.39 | 31.93 | 416.98B TWD / 30.09% | 2026-06-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.04 | +19.41% | +16.94% | 141.50 | 144.50 | -2.08% | 同向 | 4.00 | 35.55 | 22.94B TWD / 17.78% | 2026-06-01 |
| MU 美光 | 產業/供應鏈推估 | +0.03 | N/A | N/A | 1,087.99 | 1,087.99 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.03 | +28.28% | +28.37% | 2,107.86 | 2,107.86 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.01 | -5.63% | +23.28% | 393.94 | 446.77 | -11.82% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：risk, surge, record high。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：risk, surge, record high。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：risk, surge, record high。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AMD Jumps 8% to a Record High, NVIDIA Climbs 4%, Intel Rises 3% in a Risk-On Chip Surge - 24/7 Wall St.](https://news.google.com/rss/articles/CBMixAFBVV95cUxPRGZfT0xRY2dJSjdwWEFpY3dXanBNWEFmUWhjWUNjUDJlQ3lMTE82TXk3WFpSUmwyRlBKZFN3R0NpNjRldm1pNDRvT3ZhbFR1bHdYWDk1Ymd5bjNRYVdwNWlDcVB4VGhuNDJFSmNfRTNvWUg1TXBuVnJEYm5DRnl0WGF0RXhFeHAwZ0RuWTBlODFvT25haFpuY081QVlCX20yNTdDUU5mRnFKVGh3dXIyb3lvWjdOOUVZWUtBOWFsUzYtaEtN?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 15 Jun 2026 16:22:42 GMT
- [攜手新北科學日培育人才 淡江大學教材將半導體製程科普化 - 中央社 CNA](https://news.google.com/rss/articles/CBMiVkFVX3lxTE90amkwRkJCbXkzcTZidFN2OW40UlhNUEtQNnRhMWFaRGxrZy1YTkh6LUVMTktKbVVPNVF3NVlxTWF5eGtXLWRTdzZZSk5ZQ2NqMDFXZHBn?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 15 Jun 2026 06:28:43 GMT
- [台股波動完看基本面南亞科等15檔績優股出列AI、半導體最吃香- 日報 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9NeHFNS1BQYmN1dWVTRHhZbXRPdERVVk90b1NBaF8wOHNoeVA0M3lqQ0NVb0toWmNTdTFqX25IVHBCeGR4Y282ZzJvRDlGWEw0SEZNUmJzc3l0aWRsYkpn?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 14 Jun 2026 19:00:00 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Micron Technology Inc Stock (MU) Moved Up by 8.00% on Jun 15: What Investors Need To Know - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 1,087.99 | 1,087.99 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Micron Technology Inc Stock (MU) Moved Up by 8.00% on Jun 15: What Investors Need To Know - TradingKey](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPMk5JMklrcXVXeFdYSUVkSFFzbzQ1Z1J4T0UyZGJiclBCTGtDX0NsYnJHaUNlbjhBMkdqRjlXYTJkbkQxTVZabGdTSVJuTWNISEpkZ0FLTElsMVpQVl94dTJobGJyV2V5aWxQT0tnenBpc1JRT0YwdmRObWFKZWszSlFWU0dSN3BC?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 15 Jun 2026 14:15:31 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：基本面佳散熱雙雄權證夯- 日報 - 工商時報；焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報；告別低毛利！匯鑽科以獨家「鍍鎳金銦」搶攻 AI 液冷與 CPO 光通訊領域 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | -0.30 | +2.12% | -6.23% | 2,410.00 | 2,835.00 | -14.99% | 背離 | 61.06 | 39.60 | 15.87B TWD / 60.64% | 2026-06-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 2 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：跌停。

### 主要來源

- [基本面佳散熱雙雄權證夯- 日報 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE40YUpfRjZKcHlaV3ZmUDRLNUpLTmpjVEhMY2psWjJNcFZFbXRPM3RkcVFxdGtEWElxM0hSUExqR2RIYUZOUm4yMEhwSlc1am9oUTFHaUJSRFQ5MTRMM1pF?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 14 Jun 2026 19:00:00 GMT
- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 15 Jun 2026 06:05:19 GMT
- [告別低毛利！匯鑽科以獨家「鍍鎳金銦」搶攻 AI 液冷與 CPO 光通訊領域 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiYEFVX3lxTE9HWnYwd3VKRUtTblMzWk82RzVMSWU3Mm5nUTMtVVAxejZieFE4bXpsWXFmZjRwVmtab3RIOGhqTk5vcWF0c1BUeW16N1J2ODk3ZGZqZ1dQUmRfYjE1RnI5Vg?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 15 Jun 2026 07:47:57 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：個股動態報導內容-E85B5DB2-B3C9-4981-8E54-4ACACE61D6C4 - 5850web.moneydj.com；盟立打入CoPoS鏈 - 經濟日報；台股多頭氣勢如虹 七檔拚進台股千金俱樂部 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-E85B5DB2-B3C9-4981-8E54-4ACACE61D6C4 - 5850web.moneydj.com](https://news.google.com/rss/articles/CBMikgFBVV95cUxOc1NiLU9saUNtTl9RN29WakxkWTFNSlNsSHM2OExfcG5yUDBLeVpfc185OTlJNkRrcXdDcUN2SlJ1MXhmQmJqYUlla2hMNGxVOFRxWFNaeW1YaUtISk1KMW1Dekk5OHgwTk9UMWxTazRtUmpDTkxNTkhkMFprYWhIODQyTHdGZHlkdGJRN01vanEzZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 15 Jun 2026 11:57:49 GMT
- [盟立打入CoPoS鏈 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFA3dkFfU0FfN09RQXdCOHZFRE0tRXNxVW1WSy14czJlQVdOMkRCczh1dF8xZkttcjFVaC1XRkNTOHpvT3h1eTZ1Zno2cnJ6eDhhLW50bDZGbUktZ9IBX0FVX3lxTFBSdWc0ZG5HVGhfWEJiRzc0dk05QWgyNDZITE5kN0tLNW1JYkw3dkZhci1JdGp5WHNyRWVCYWJIQWIyQmtzYU9oR190WG9ITHk3QjI4NXVUS0JMajJUOE0w?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 14 Jun 2026 17:21:00 GMT
- [台股多頭氣勢如虹 七檔拚進台股千金俱樂部 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5uMnFTdXlPcGlWdFNCWmh5U05zakJNSkxRd1ZIT0dmc0VEN0xid2NFeFVqWjBZeVlPUmE1bXJMbTBNLTBXRHVRd00xVzRmaU56VG1acGNVUnU4Z9IBX0FVX3lxTE9ubEtfZXdmYzMwMGZSWk03dUswdUlSX3FYaDIzclJzUmUyNW5tZ05hOC1vblctLUkwMC1QUnY2Z3dEci1FVzlZNmprSWNwUFc1clBiSmRWSmh4dmFXSVVB?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 15 Jun 2026 02:00:00 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》大漲1227點，站回45K及各均線-新聞內容-基金 - MoneyDJ；本周台股ETF除息高峰351萬人期待搶息- 新聞 - MoneyDJ；國票證券：台股盤勢震盪幅度估加大- 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》大漲1227點，站回45K及各均線-新聞內容-基金 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxQQVlkZE1SaS02MURDcHpkbEw4UnNjN2J4SlZILUhRdGxzTmtfX01rcmV6b1lZelBreW9tc3gzRHFkRUp3UGxlZURNU0h6MU82MzU1MXdISDIwYzdfVmtfV0hHTHQwakNHX3l4c29pQjE0emRzRTZjMW9DV2IzT2dkWUQweGVBbEZKMkFHb2tkRW4?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 15 Jun 2026 07:43:00 GMT
- [本周台股ETF除息高峰351萬人期待搶息- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQMFJmT1kzSGN5dGhnWlZmRkJ1R2hrOWR2WHVUNDQ5X2YzOHN5OU5nOXJpQ1JPVDdtMlRkYUxJb2ZVMTVXUmo3SU1ldlVvTDFUa2Y5cWs2RFZ3Z3hZeElJTGpudzA4THpqQmNubWRUekpSbTNObWYteFhQdzVBVWlCT0xRNkJPQjNtTHNPWlZmU19CQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 15 Jun 2026 03:01:00 GMT
- [國票證券：台股盤勢震盪幅度估加大- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNTHJGUU9wOUo4VnVJMjN2cXNScXc1SHJQNVlMOWlJVGppSW1JaHl1UGhCSzBIZEszcTZZcHBGZTYxRC0wSTJoZUpvQTBobjVkS29hbmx6UHc0QTJfU2FQTnNOaGhpWjY0WkZBSFhzdFBtUkxsQjZXdzVVNTI5R1ZxanVPNXZvcTB3ODV5UWJJQ2JpUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 15 Jun 2026 00:45:00 GMT

## 新興題材：SpaceX

摘要：新興題材：SpaceX 相關新聞集中在：Stocks making the biggest moves midday: SpaceX, Roku, Tripadvisor, Ferrari & more - CNBC；Stocks making the biggest moves premarket: SpaceX, United Airlines, Roku & more - CNBC；These rocket stocks sold off on the SpaceX IPO. KeyBanc says it's time to buy the dip - CNBC

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [Stocks making the biggest moves midday: SpaceX, Roku, Tripadvisor, Ferrari & more - CNBC](https://news.google.com/rss/articles/CBMiogFBVV95cUxQWXRBOGx5SWxXQWdWY1lPb0dzbktra0FQOER0U3dYY0lmOVNsa1NGcmgzbXROQjZIc3lWRTY4OV9zbXdaakxDNmJXZ2VfcENLUF9CQUdsSjB4UWNXV1lhRmx0azlKVWNZVnlvM0s0ZXVuYXZnTW1Wem54SjN0bFJ3M0lUdDhiMkV3RW51cktTcExnc0JUUVZYSVNzWmwtM2YwTVE?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 15 Jun 2026 15:59:57 GMT
- [Stocks making the biggest moves premarket: SpaceX, United Airlines, Roku & more - CNBC](https://news.google.com/rss/articles/CBMilwFBVV95cUxQRWdtdzhPaG50amwzbWp4NGdWc2tDNzhOZ0MyOEh1bEZjcDRfZVFyYzM3M2FCejVJMVd2eWJOS1NiR1dYYktPcW5UYl9BdS1kb253TUlTQXRleDB0Y0p0UjBfWEJWcGRYQVpMeDlJMVdRMzAzXzR2dlJVWERHeEJ5NDhRZTluaU5oUzdpMTg2UWhwVGJSRy1J?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 15 Jun 2026 11:28:56 GMT
- [These rocket stocks sold off on the SpaceX IPO. KeyBanc says it's time to buy the dip - CNBC](https://news.google.com/rss/articles/CBMipgFBVV95cUxOZmkyWEdpVDJwUWFrV1FPV3N0N1k0ZTZEVWtLUDJtcEJPdFU4cVBldVk5RE5URllSVkEyY2NHSURzRUdSQWd4X1l3UU4tT1Axc0Z5UlRfanJROUZhNzlsQUZWdTcwMzVIcE5KU19mTjN4dEhHVzVfNG1RdUlQalBqNjVBd0l2dUx5a3hwQm5PY1ZLOEczaDhfZVRIQlBtZ3NTTXp5MUJB?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 15 Jun 2026 13:07:15 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
