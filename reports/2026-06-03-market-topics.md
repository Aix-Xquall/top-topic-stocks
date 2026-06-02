# 每日股市熱門話題分析 - 2026-06-03

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **AI 伺服器與資料中心**｜正向｜熱度 18｜市場確認 78.23｜同向 5/6
2. **記憶體與 HBM 供應鏈**｜正向｜熱度 10｜市場確認 94.30｜同向 2/2
3. **關稅與供應鏈轉移**｜正向｜熱度 6｜市場確認 90.00｜同向 3/3
4. **半導體與晶片供應鏈**｜中性｜熱度 8｜市場確認 N/A｜同向 0/0
5. **散熱與液冷供應鏈**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.48（樣本 11）
- 5日相關係數：0.62（樣本 11）
- 同向比例：10/11

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| AI 伺服器與資料中心 | 78.23 | 5/6 | 1 | +6.63% | +11.84% |
| 記憶體與 HBM 供應鏈 | 94.30 | 2/2 | 0 | +8.10% | +16.86% |
| 關稅與供應鏈轉移 | 90.00 | 3/3 | 0 | +6.67% | +9.89% |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：TradingKey | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-05-21 | 0.28 | 0.52 | +45.45% | 11 |
| 2026-05-22 | 0.05 | -0.00 | +33.33% | 15 |
| 2026-05-23 | -0.00 | -0.05 | +84.62% | 13 |
| 2026-05-24 | -0.11 | 0.22 | +86.67% | 15 |
| 2026-05-25 | 0.40 | 0.33 | +50.00% | 10 |
| 2026-05-26 | -0.23 | -0.31 | +92.31% | 13 |
| 2026-05-27 | -0.07 | -0.07 | +87.50% | 8 |
| 2026-05-28 | 0.14 | -0.07 | +88.89% | 9 |
| 2026-05-29 | 0.14 | -0.04 | +71.43% | 7 |
| 2026-05-30 | 0.16 | -0.06 | +71.43% | 7 |
| 2026-05-31 | 0.96 | 0.09 | +100.00% | 3 |
| 2026-06-01 | -0.92 | -0.72 | +16.67% | 6 |
| 2026-06-02 | 0.08 | 0.05 | +72.73% | 11 |
| 2026-06-03 | 0.48 | 0.62 | +90.91% | 11 |

## 歷史回測摘要

- 回測日期：2026-06-03
- 近5日 3日相關：0.23
- 近5日 5日相關：0.08
- 同向比例：+66.67%
- 權重狀態：未調整

- 方向準確度：+66.67%
- 信心排序準確度：0.23
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

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：NVIDIA vs. Intel: Which AI Chip Stock Should Retirement Investors Own? - 24/7 Wall St.；AI Bubble or Not, the Stock Prices of These Dotcom Darlings Are Soaring Like It's 1999 - Investopedia；Intel Up 250% in 2026: Is the AI Comeback Real or a Short Squeeze? - Gotrade

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.76 | +11.65% | +25.75% | 222.82 | 224.36 | -0.69% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.76 | N/A | N/A | 107.93 | 114.68 | -5.89% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.70 | N/A | N/A | 521.54 | 521.54 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | +0.66 | +15.37% | +50.70% | 481.57 | 481.57 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.07 | +3.70% | +4.85% | 2,380.00 | 2,380.00 | 0.00% | 同向 | 74.39 | 32.00 | 410.73B TWD / 17.50% | 2026-05-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.05 | +12.37% | -12.90% | 441.31 | 506.69 | -12.90% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.03 | -5.90% | -3.44% | 590.00 | 611.00 | -3.44% | 背離 | 10.86 | 54.78 | 62.25B TWD / 19.22% | 2026-05-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.05 | +2.61% | +6.10% | 4,525.00 | 4,555.00 | -0.66% | 同向 | 62.91 | 72.11 | 46.74B TWD / -4.14% | 2026-05-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 2 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 2 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「超微」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [NVIDIA vs. Intel: Which AI Chip Stock Should Retirement Investors Own? - 24/7 Wall St.](https://news.google.com/rss/articles/CBMisAFBVV95cUxNV2xGcmtmdThoNlg1ZGFuZFdEcUk1OUthU1FwcmV1T0RVdFB6XzNuLXpXNUQ5c1E3cW42bUxXZ2xjdnBrUUxXVVlVcVdJbk9DbUJQbGhYZjVEZWtQVWR4YkgzX3VVckdTLWJ3MXkzTVNiMUhabmstWnpDRzhtdVE3bTBuU3dFeTFZMGI1VHc5V1BzYllMQXlVYmFDaENRamxMemxqOWItdUppdlJPQms2UA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 02 Jun 2026 21:15:01 GMT
- [AI Bubble or Not, the Stock Prices of These Dotcom Darlings Are Soaring Like It's 1999 - Investopedia](https://news.google.com/rss/articles/CBMi0wFBVV95cUxPbm5waTRSdTJzV1hldE05RF96bERyY2lEdTBkbmtoM2JQRVltdHMxU3ZteGpaTmlZelhmenZZX1g0ZW1MZERPR3FQbVJiMm81VzdhOU5odXhyaDlUZlZzeDFWajk4ZDlHSWZqaEZQZlJaRWtpT1ZJZUVqb05jUnRic0lIc3hjN1BrNjlQTEl5SVNfY0ctR1ZWMFpXY0FlYmE5R21MSVJvcmFiYUdKQU9OQVYxYmJ2TmtTOVdaMWVUYURBbnl0d3dVNXhtTjhOMTV4NDRV?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 02 Jun 2026 19:43:43 GMT
- [Intel Up 250% in 2026: Is the AI Comeback Real or a Short Squeeze? - Gotrade](https://news.google.com/rss/articles/CBMickFVX3lxTE9FV0EyYTFDS1V2WXo0RE5leTQzbGJFYTV6ZzFacGQtZjRxanpTckhmRFRDUndTd3ViYVVGc3JfdnRuNllQZDVrU1E4Y0ljSzdDVTVObWswN2xQdlJOdV9BQjNkcXVxdmlLZGVfUFJkVzI3Zw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 02 Jun 2026 04:00:16 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Wall Street Can't Get Enough of Semiconductor Stocks. Should You Buy Micron or Intel Right Now? - The Globe and Mail；The Zacks Analyst Blog Highlights NVIDIA, Sandisk and Micron - Yahoo Finance Singapore；Micron Rises 7%, Western Digital Climbs and SanDisk Climb 4% as Memory Stocks Extend Parabolic Run - 24/7 Wall St.

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.76 | N/A | N/A | 1,064.10 | 1,064.10 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.76 | +4.55% | +7.98% | 1,716.36 | 1,761.43 | -2.56% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.59 | +11.65% | +25.75% | 222.82 | 224.36 | -0.69% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.56 | N/A | N/A | 107.93 | 114.68 | -5.89% | N/A | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、memory、Micron Technology」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：increase, shortage。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 4 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：shortage。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：HBM。 方向判斷命中詞：increase, shortage。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Wall Street Can't Get Enough of Semiconductor Stocks. Should You Buy Micron or Intel Right Now? - The Globe and Mail](https://news.google.com/rss/articles/CBMiggJBVV95cUxOM0dja1dhV0oxbWhiaWhIcGJNX1cxbFZlbWF3RUc3Wkh0WWtfaTJGbjNiOS1Eem1XWTYwTG5EOXIyeGpEVW5kNlE5SEdUR3BTNko4UnNLQnhqYkd2NXFnZ1FRUDIwRm1mN2xnUnhMMXRzSVRFZmFjbDBFbEJfSEJfY2FRdTUybGt6Z3ktZ0R0c2ZPbkFZdjg0eTZOSHF6WWZVeExPUnFQTzZlOHJaUlVNelR1akZNY094RGRPNVFhd01uX2FLT1BHTDNtdWtOblVILWtEeWtkbXdhcEtUOUJhNHlGWEhiZk1HZ0lZanFkaEQ0cG5LbFJpMEdOVkZORWExVVE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 02 Jun 2026 12:15:57 GMT
- [The Zacks Analyst Blog Highlights NVIDIA, Sandisk and Micron - Yahoo Finance Singapore](https://news.google.com/rss/articles/CBMijgFBVV95cUxPUzVRWS1tSThobklZazRtT3V4QmVVYWVpR25yeFZpeVRXQ2RLcDVVVWNteWU3US02VmVYeno4NjZFYUlldnBWcUFCQV96SHVfZWllTmY1MmNQRmdNQ1dJdE1uMHBOaFBibVNqeC05SmZtZERBOTBmVkVEbl9TVHlOQ0RaQ1o3dHdrRE5aSnNB?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 02 Jun 2026 13:02:00 GMT
- [Micron Rises 7%, Western Digital Climbs and SanDisk Climb 4% as Memory Stocks Extend Parabolic Run - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi1gFBVV95cUxQWGk4MzVNdHRfU1JvRTc2Q2phVmRCd2Q3c0h6cVlzZ3dsczdkdzlHcGRGdXE5ZjVsY3AxMFMzUVFRMF9weG16OExPaHN2cVZHRFJiRlhaTUxLVGdvRy1Sb3VkNVF4SkxIMExoSEQ1My16Q25jZ2Jwa3o1X1BhWlNSMnppNF9nclQ0QjNRbVNTNW1rS016VDFjTXh6cVlIaUZkUXM0dThsNmE4OG13M3RjUjJ5cWhGVGo4NnI5LS1rQTg1VWxycDc0NW1PLUpfcjFmY0dyWWdR?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 01 Jun 2026 18:38:38 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：熱／黃仁勳的Vera Rubin放量　供應鏈14強 - 鏡週刊Mirror Media；奔向5萬點1／VR200激勵台股萬花齊放　「第二梯隊」供應鏈類股成焦點 | 財經 | CTWANT - CTWANT；輝達GTC效應發威，散熱與背板供應鏈齊揚-財經焦點情報站 - CMoney投資網誌

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.56 | +11.65% | +25.75% | 222.82 | 224.36 | -0.69% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | +0.56 | +3.70% | +4.85% | 2,380.00 | 2,380.00 | 0.00% | 同向 | 74.39 | 32.00 | 410.73B TWD / 17.50% | 2026-05-01 |
| 3017 奇鋐 | 新聞直接提及 | +0.56 | +4.65% | -0.92% | 2,700.00 | 2,835.00 | -4.76% | 同向 | 61.06 | 44.36 | 15.63B TWD / 71.62% | 2026-05-01 |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +19.31% | +35.78% | 315.20 | 315.20 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | +14.64% | +16.41% | 301.50 | 301.50 | 0.00% | 不適用 | 14.13 | 21.41 | 832.10B TWD / 29.74% | 2026-05-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。
- 3017：新聞直接提及「散熱」，共 1 篇新聞命中。

### 主要來源

- [熱／黃仁勳的Vera Rubin放量　供應鏈14強 - 鏡週刊Mirror Media](https://news.google.com/rss/articles/CBMiYkFVX3lxTE1iM01PTnRPWF83QXJ6MEJqckxMWUJDOUtvR1N4bWFkdlo0S2N6RG83YkUydHd1UE04ZVFjOF90aW1scTJFUmdPQ0RMdnV5NU43QjFxV25zOWN0cHFydVlhdWpR0gFiQVVfeXFMTWIzTU9OdE9YXzdBcnowQmpyTExZQkM5S29HU3htYWR2WjRLY3pEbzdiRTJ0d3VQTThlUWM4X3RpbWxxMkVSZ09DREx2dXk1TjdCMXFXbnM5Y3RwcXJ1WWF1alE?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 01 Jun 2026 18:00:00 GMT
- [奔向5萬點1／VR200激勵台股萬花齊放　「第二梯隊」供應鏈類股成焦點 | 財經 | CTWANT - CTWANT](https://news.google.com/rss/articles/CBMiVEFVX3lxTFBfMEluNU9uYXgyODZiV2w5MDZaY2x5eFF2REVDNjFhdFN2Vk1LRDgzRFBoVTNfU2didS1oVmM2emR0ZkpyYmhFcEJ0UVFNYXJmT0RwRtIBVEFVX3lxTFBfMEluNU9uYXgyODZiV2w5MDZaY2x5eFF2REVDNjFhdFN2Vk1LRDgzRFBoVTNfU2didS1oVmM2emR0ZkpyYmhFcEJ0UVFNYXJmT0RwRg?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 01 Jun 2026 22:00:00 GMT
- [輝達GTC效應發威，散熱與背板供應鏈齊揚-財經焦點情報站 - CMoney投資網誌](https://news.google.com/rss/articles/CBMiggFBVV95cUxQZktUTUYzLWdLUnJPVF9UODRobVdLSE5nMWhoRDdmQ1hmTFBQdENpNHRCNU1yS3BnYkROVU5FbmR1ODBxNHZQTkZGY3B3dXZ6eUhaZERNZWg4elk2eHlPLTdKWjVuWGlrTlQzSVlaTWRJQUdEbTFleWdEMDQ4Z0g5b3Vn?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 01 Jun 2026 04:45:07 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：NVIDIA vs. Intel: Which AI Chip Stock Should Retirement Investors Own? - 24/7 Wall St.；NVIDIA vs. Broadcom: Which Is the Better Long-Term AI Chip Bet? - 24/7 Wall St.；COMPUTEX 6月2號開展，全面引爆 AI概念股強漲，輝達Rubin800V架構將帶動導線架與功率半導體?【研究觀點】 - sinotrade.com.tw

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +11.65% | +25.75% | 222.82 | 224.36 | -0.69% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 107.93 | 114.68 | -5.89% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | 0.00 | +15.37% | +50.70% | 481.57 | 481.57 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 新聞直接提及 | 0.00 | +12.37% | -12.90% | 441.31 | 506.69 | -12.90% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +3.70% | +4.85% | 2,380.00 | 2,380.00 | 0.00% | 不適用 | 74.39 | 32.00 | 410.73B TWD / 17.50% | 2026-05-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | -0.35% | +8.43% | 141.50 | 146.00 | -3.08% | 不適用 | 4.00 | 35.55 | 22.66B TWD / 10.80% | 2026-05-01 |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 521.54 | 521.54 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 1,064.10 | 1,064.10 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA、輝達」，共 3 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AVGO：新聞直接提及「Broadcom」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [NVIDIA vs. Intel: Which AI Chip Stock Should Retirement Investors Own? - 24/7 Wall St.](https://news.google.com/rss/articles/CBMisAFBVV95cUxNV2xGcmtmdThoNlg1ZGFuZFdEcUk1OUthU1FwcmV1T0RVdFB6XzNuLXpXNUQ5c1E3cW42bUxXZ2xjdnBrUUxXVVlVcVdJbk9DbUJQbGhYZjVEZWtQVWR4YkgzX3VVckdTLWJ3MXkzTVNiMUhabmstWnpDRzhtdVE3bTBuU3dFeTFZMGI1VHc5V1BzYllMQXlVYmFDaENRamxMemxqOWItdUppdlJPQms2UA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 02 Jun 2026 21:15:01 GMT
- [NVIDIA vs. Broadcom: Which Is the Better Long-Term AI Chip Bet? - 24/7 Wall St.](https://news.google.com/rss/articles/CBMipwFBVV95cUxPbmtYdmQwSWdPNnhQalkxQWlJbjNsN3VXNlowaWtQYVFvTjFDTUctQnRIT2tiLW1naS1VYjZTZktaVWhleHp4Q3QyUUhYbVhIS1MwVDAwWEJxTmlselBKSFZNVU11bzlEYnNpRmlWaWJsWHpDNVNDcTBkU2FUZUgxeTZ0dko0VlAwRG5ObGJNc0xpNkZjMjQ1Slhlanp3ckJ5Q2NvdnQ3aw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 02 Jun 2026 18:27:28 GMT
- [COMPUTEX 6月2號開展，全面引爆 AI概念股強漲，輝達Rubin800V架構將帶動導線架與功率半導體?【研究觀點】 - sinotrade.com.tw](https://news.google.com/rss/articles/CBMirARBVV95cUxQYVNIbkZONWdtVDF6eGV5YjlqemtTajhNVjBYdDlqT213WmV0MkJ2QkdWWXJGSU1sbHZYSVR2WW1fOVZvV0E1ck1yMHZRYWo5Ym5ubFFQalV4RkVnb2J1RmRXRW8zeThyQjBxbktweUtSUklYSklLckticUNEcnZwWi1kdm5OV3hkbk84aGtrUTNWVE5XNnUzUmJyaVNUT3JnR0h5TFZySGYxSERkZHNRUE4yOU1tSXFBOWtfWFVRajVGU1hXWExNYnJNWjY4aVAtWXBJWWJJdXNaS1h6UDV0dUZmZWFjc1NxR2tqbmgtVk1CcGtSaS0tM19VVmk5LW5xU0F3TUlwRnY0M0xqTWxlVXFHb2Y0dVNvQXgzNDJ5MFVzMDM5WU1MMEp6MVd0Tk9RTHJQMHRJVkV2bDZZZ0QwQ0tsenJveGJuRG5VTzRad2VlWVNhRm9JTTd3VElFcmJrU05RdDZqeDlmS3Bzd2hnTUQ3a3lYRV9ScThTT3hIZUwzOHcxUlRpQkRPVFUxYkdjYnhGZjFudXdPTFJzWGZRb0hLU0dHMnZQdnhVUnpLa0xOWlZsX3Q5S0lnRXd6R0loR0NtREpxVmVCNTdqRjZQaTRGSndFSl9QVDNWUGEtc01INlo5d0NKa25uejR1SFByR0FReVphcUhDYzhubGliQXVGSWh3aDFVVmtiTmhyUG82WW10ejNUVnVhc3J3NjgxdUROMFVFSGZLejc4?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 02 Jun 2026 19:19:54 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：奇鋐：2026年下半年將大爆發 訂單看到2029年 - 經濟日報；輝達GTC效應發威，散熱與背板供應鏈齊揚-財經焦點情報站 - CMoney投資網誌

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | +4.65% | -0.92% | 2,700.00 | 2,835.00 | -4.76% | 不適用 | 61.06 | 44.36 | 15.63B TWD / 71.62% | 2026-05-01 |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +11.65% | +25.75% | 222.82 | 224.36 | -0.69% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐、散熱」，共 2 篇新聞命中。 同時符合主題標籤：thermal。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [奇鋐：2026年下半年將大爆發 訂單看到2029年 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1rQVZJMTVHbVJ1c2Q0MnFVVUY0TGZ3akVQVkp1SnBfZ3hsekFwU0VEajEzTnJBTUtTT2Z0bmc1OUFWdTBCSk5UbWlxWHpLS0ZaTWs1WnFmcElZZ9IBX0FVX3lxTE1lWHktNVZnUTRHODFlSWVBTkp5Wm1VeUtBMnljWnF2RUw3YW5hUDVKOXo1anhSNlpfN043RHIxSXBBMWFwRFpEbnlQOWF3d1Q5Yk1SV0JOaXNuY1d6UUQw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 02 Jun 2026 17:04:08 GMT
- [輝達GTC效應發威，散熱與背板供應鏈齊揚-財經焦點情報站 - CMoney投資網誌](https://news.google.com/rss/articles/CBMiggFBVV95cUxQZktUTUYzLWdLUnJPVF9UODRobVdLSE5nMWhoRDdmQ1hmTFBQdENpNHRCNU1yS3BnYkROVU5FbmR1ODBxNHZQTkZGY3B3dXZ6eUhaZERNZWg4elk2eHlPLTdKWjVuWGlrTlQzSVlaTWRJQUdEbTFleWdEMDQ4Z0g5b3Vn?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 01 Jun 2026 04:45:07 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Intel Corp Stock (INTC) Opened Down by 3.36% on Jun 2: Drivers Behind the Movement - TradingKey；SK Hynix 1,000% Annual Gain Not Enough? Top Wall Street Funds Increase Stakes, Will HBM Chip Supply Shortage Escalate Further? - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.56 | N/A | N/A | 107.93 | 114.68 | -5.89% | N/A | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Corp Stock (INTC) Opened Down by 3.36% on Jun 2: Drivers Behind the Movement - TradingKey](https://news.google.com/rss/articles/CBMiiwFBVV95cUxNckUyelFKcXZhNk8tbURxRWl5U1lQZE9aa2VWbGdpZUR2NDY4TEt0ZnJBVGRjcVlBMVpOQm1ZTlJycG1jWUNnWncwYWkwbXlMZ0tfSFY1RWFnS19JaXhyblNZOHZUcWhOczN1N0IwbXpsanN0ZFVHekNNMGdpdDMtM25rc2NkTTlZaHUw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 02 Jun 2026 13:47:22 GMT
- [SK Hynix 1,000% Annual Gain Not Enough? Top Wall Street Funds Increase Stakes, Will HBM Chip Supply Shortage Escalate Further? - TradingKey](https://news.google.com/rss/articles/CBMiswFBVV95cUxNeVFoMlVkLVZfWERVemV6Qm1Ga1hGazNMb19RNk5YODdKdWZLZlVhTnE2alVMcjlDekJCdnZCcTVVUnVCQUJDU1lpUndibS13RGs0U1ZmSDhWTXp5REU1WkhkdHBMaVI3bWVDRmU0TEV3aVdzM0dBRTJRUnpaYlJwVTNhYlJTY2JCeUJuR182LVhSYnJ6c3pzU1hiMTFjZW11X0piZ1ZSRnEyYW42X1Bac2RHTQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 01 Jun 2026 13:05:45 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股大洗盤46K近關情怯 巨震1,046點 匯市成交量衝上35億美元 - 經濟日報；台股大洗盤46K近關情怯 巨震1,046點 匯市成交量衝上35億美元 - 經濟日報；台股基金 97%漲贏大盤 | 基金天地 | 理財 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股大洗盤46K近關情怯 巨震1,046點 匯市成交量衝上35億美元 - 經濟日報](https://news.google.com/rss/articles/CBMidEFVX3lxTFBIeEMzWWRPaEJoamFzZlRTX2ptS0U3Ym5ZSnJzNTFMTmxsakdldkpMMDBHaGg2MWVSV3VtcFV5MGY1d18tdHk5QlliT2ctSGViN0ZsaUpkbjB3YzRvcjdTYjRlbUxXR2owMjlmX1Bta3dac1Bq0gFfQVVfeXFMTVhKNEVKMGVVZk1LTE8yYjZZcXNONGwzaGtwb21vS3Q4LV9jNmlDWVVxYi1KS1hPY1VoZmowbTlzeFFUVFJ2XzhlMmdVTkhDYmYzQ0FfV19HcGFQcEFQR00?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 02 Jun 2026 17:24:09 GMT
- [台股大洗盤46K近關情怯 巨震1,046點 匯市成交量衝上35億美元 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1DRUtjMmtySU9TUWtrQ2ozREJOSHlNOGw5VzZzdWhnQVNacjBpeXpMeHdmVUY0NUViNGF0QURBNFFnZEM4dVlPYlF3Um41YS05SlRnMkx4Q1JZZ9IBX0FVX3lxTE1YSjRFSjBlVWZNS0xPMmI2WXFzTjRsM2hrcG9tb0t0OC1fYzZpQ1lVcWItSktYT2NVaGZqMG05c3hRVFRSdl84ZTJnVU5IQ2JmM0NBX1dfR3BhUHBBUEdN?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 02 Jun 2026 17:24:09 GMT
- [台股基金 97%漲贏大盤 | 基金天地 | 理財 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5mOGFYaEQ2d25RUE9DN2J5djk4Z1ZZZVFjY3l2elZ3dmlTYlBTWl9UVDk0azFiTDhBQmUtZ0xjRktRSGpCblZTQzJvNmkyLTRGc0JzV0N4dHZWQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 02 Jun 2026 17:01:06 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》震盪逾千點、收漲219點續創新高- 新聞 - MoneyDJ；柏瑞聚焦「GIANT」五面向，冀掌握台股結構性機會- 新聞 - MoneyDJ；統一證券：台股盤勢仍由多方掌握發球權- 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》震盪逾千點、收漲219點續創新高- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxOWG9hUG96ejRrdVoxdUVmeXlkS2tHc2x6WmJpWlV0bjBrNkljWU5IMzFPZWU2eW1LSVNPV214bVhxNWx2VlRwNjl0THZnLXVEWVNnc3hYRG90d0xvMlY5VmpTX3NIZTN0Z2tBRHZwaFlwTjdmcWV5LWxlNW9wNk9Od0F3UUlXdVR0TG5IdXZvdEgwdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 02 Jun 2026 07:46:00 GMT
- [柏瑞聚焦「GIANT」五面向，冀掌握台股結構性機會- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNb0tIX0JOWVBiM0FxS1dlNFczZ0dpZFVzbzN1S1J4SWdDZkY1T0xUenRGdlB6WHl1dXZyTWlUMEkwbWlNZnZpQnRzaW9saUhQenYtdEhNSlhMWkZKOTNZVDJPQmdJZ3RzdHNmaTVDTlR2bnFlVGdodTBJdkJQVEtvSG50THFxd0JBekVEbjRaaWJMZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 02 Jun 2026 03:52:00 GMT
- [統一證券：台股盤勢仍由多方掌握發球權- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQZzEtODZYdTJWSjlHLXptMU1aeXRXMlRubjN4TVFISUxXODlUTzhMbjdCOVBLY3J4aUd3Rkp3UlE0WTdNZW5Xb3dpbFBXM2xSVUE4OFNYWThmcFNNOXhwSmN3bEFNZHl0b1BzZ2kwcHFUQm5YUGFna1o5RkVMRmZEMmJydGFZeHVIVUdOc255dFdsdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 02 Jun 2026 00:35:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
