# 每日股市熱門話題分析 - 2026-05-20

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **利率與成長股估值**｜負向｜熱度 3｜市場確認 N/A｜同向 0/0
2. **半導體與晶片供應鏈**｜中性｜熱度 7｜市場確認 N/A｜同向 0/0
3. **新興題材：OpenAI**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0
4. **AI 伺服器與資料中心**｜中性｜熱度 11｜市場確認 33.37｜同向 2/6
5. **新興題材：CoinCentral**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.36（樣本 7）
- 5日相關係數：0.35（樣本 7）
- 同向比例：2/7

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：OpenAI | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 33.37 | 2/6 | 4 | +3.35% | -0.29% |
| 新興題材：CoinCentral | N/A | 0/0 | 0 | N/A | N/A |
| 記憶體與 HBM 供應鏈 | 0.00 | 0/1 | 0 | -0.04% | +4.73% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：千金股驚現跌停 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-05-08 | 0.03 | 0.48 | +76.92% | 13 |
| 2026-05-09 | 0.10 | 0.55 | +33.33% | 9 |
| 2026-05-10 | 0.45 | 0.55 | +75.00% | 8 |
| 2026-05-11 | -0.03 | 0.47 | +85.71% | 14 |
| 2026-05-12 | 0.00 | 0.42 | +78.57% | 14 |
| 2026-05-13 | -0.08 | 0.07 | +58.33% | 12 |
| 2026-05-14 | -0.29 | -0.20 | +50.00% | 6 |
| 2026-05-15 | -0.17 | -0.08 | +58.33% | 12 |
| 2026-05-16 | -0.12 | -0.69 | +33.33% | 12 |
| 2026-05-17 | 0.09 | -0.34 | +40.00% | 15 |
| 2026-05-18 | -0.01 | -0.17 | +33.33% | 9 |
| 2026-05-19 | 0.04 | -0.01 | +62.50% | 8 |
| 2026-05-20 | 0.36 | 0.35 | +28.57% | 7 |

## 歷史回測摘要

- 回測日期：2026-05-20
- 近5日 3日相關：0.03
- 近5日 5日相關：0.02
- 同向比例：+37.50%
- 權重狀態：未調整

- 方向準確度：+37.50%
- 信心排序準確度：0.03
- 診斷：低相關

調整原因：近 5 日有效樣本 8 筆，低於 15 筆門檻，暫不調整權重。

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

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：Wall St ends lower as inflation worries push up yields - Reuters；市場憂中東戰事恐使通膨維持高檔　美股多收黑 - 經濟日報；Gradiant宣布完成E輪募資，公司估值達20億美元，協助加快AI、半導體以及工業水處理基建領域布局 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | -15.16% | -9.33% | 417.42 | 506.69 | -17.62% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Wall St ends lower as inflation worries push up yields - Reuters](https://news.google.com/rss/articles/CBMisAFBVV95cUxPTExrQVdLWjM3N1B1VnNNMFc4MFNXMXU2RVRtNVVuNUlJcGJDenVoc0E3RWV4UDhMQkhIVmRZemxvQnVyQXJiQktfRV9XUzRkRW9vUjhQT0stU2RNM2w0ZHQzTGQ2Zi1Db1lVdEdwUzFpZTNHUFhOTmd3RE4zbW5sQkpkZzh1M1gxSk1rRmd4R3pUaVN6cFVZeWluNE1IQWZ2eHh6VTd6Z1JjNFZ4dUZERA?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 19 May 2026 20:32:08 GMT
- [市場憂中東戰事恐使通膨維持高檔　美股多收黑 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTFAzU3BZYm9UUFNjcnRPVXVpOVNTVTJRQzdSZTFzVHJMZ2JvWFc0alJQWkt4WWNDM1g1al82Nk9YTVFsZTEweFZjQTY2cHd3eG9raHB4UzBKRnBjME0t0gFiQVVfeXFMTVJfMU56YTZhRHMxM1hrRVUycWZIMUYzNFc1WE5WbWdnWk8yRnhyWVRFbThCcGRtZEdCUmM4ZFJsdDZranF2dEFuNTVOem80MUw4X0RXMEh4QWZGSGNzcy1PNlE?oc=5) - Google News source discovery | 經濟日報 money Tue, 19 May 2026 22:12:14 GMT
- [Gradiant宣布完成E輪募資，公司估值達20億美元，協助加快AI、半導體以及工業水處理基建領域布局 - 中央社 CNA](https://news.google.com/rss/articles/CBMiVkFVX3lxTFA2S2pfNjdTQVhVUldIVTFlVDhmUjFXWDBmTVFpYnRzSnF1SVNkTkRGcm5KSzl2d25EMVl1MVFYMGJaMVBaSDktZkpUMWFFZ0tNNkl5ZWJn?oc=5) - Google News source discovery | 中央社財經 Tue, 19 May 2026 10:21:24 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：AI chip stocks slip ahead of Nvidia's earnings - Seeking Alpha；AMD, Broadcom and Qualcomm Lead Chip Stock Sell-Off Ahead of Nvidia Earnings - TradingView；三星罷工談判仍未解 擔憂對半導體產業不利 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +26.50% | +15.42% | 220.61 | 222.32 | -0.77% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | N/A | N/A | 414.05 | 420.99 | -1.65% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | 0.00 | +32.81% | +24.08% | 411.07 | 420.71 | -2.29% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 110.80 | 110.80 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -2.86% | -2.22% | 2,205.00 | 2,240.00 | -1.56% | 不適用 | 74.39 | 29.65 | 410.73B TWD / 17.50% | 2026-05-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +4.63% | +8.13% | 113.00 | 113.00 | 0.00% | 不適用 | 4.00 | 28.39 | 22.66B TWD / 10.80% | 2026-05-01 |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 698.74 | 698.74 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | +0.04% | -4.73% | 1,383.29 | 1,562.34 | -11.46% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AVGO：新聞直接提及「Broadcom」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AI chip stocks slip ahead of Nvidia's earnings - Seeking Alpha](https://news.google.com/rss/articles/CBMiiwFBVV95cUxPc2tRY0FlOENHczNna3BoNXdDbnhoc1dfdVBrSm1tRUpEN1REU09VVEVsdldwVmNsalpaeUwxVnFJazRyTjktdjduejBObE83a1BSTWoyOEpUcUZLMDBwaVVNY1AxR1JuX3NqYmxtd3BPWWotQmVJVFQ5Y19Zd1F5bFFJdjV1N0hQYVVr?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 19 May 2026 15:31:22 GMT
- [AMD, Broadcom and Qualcomm Lead Chip Stock Sell-Off Ahead of Nvidia Earnings - TradingView](https://news.google.com/rss/articles/CBMi0AFBVV95cUxPTWZjc2ZsNWRCMmpOaUtHRThWNXpFR3VKc053R0pENU54XzlxUnJBMFdmMWZrN0NGbVUxdHJZekl6MWRxd0FmTU5LYlhXNldNaGdkOHZGN3I0V2N1ZGRneGhwdFFzOE1aQXZLS25iR3FNT2liOU1tbXBSMEEwQ1hlczVBeC1xRk1kNTVUMWFNejNJOTBMZXVHY3Iyc0lMV042cXRxWHZGTnFESF9MeFNzNVAtcFA4Z0ZqcUY5V1Z1b09FZ2d2Q1FSaVRkZGFpQ05y?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 19 May 2026 17:50:47 GMT
- [三星罷工談判仍未解 擔憂對半導體產業不利 - 中央社 CNA](https://news.google.com/rss/articles/CBMiU0FVX3lxTFBhRG5uWjFTcTdkQUdZMXFDY2ljNjYwNUhreXQ1VXBvUkdtc0VOUU1BOWJyN2dPT2lVQXU2UHBCZGc0RzhFYnRCclNFWTdmVi1IcVpV?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 18 May 2026 21:45:00 GMT

## 新興題材：OpenAI

摘要：新興題材：OpenAI 相關新聞集中在：OpenAI co-founder and former Tesla AI executive Karpathy joins Anthropic - Reuters；Google debuts new AI models, personal AI agents in effort to keep pace with OpenAI and Anthropic - CNBC；Anthropic hires OpenAI co-founder Andrej Karpathy, former Tesla AI leader - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 新聞直接提及 | 0.00 | -15.16% | -9.33% | 417.42 | 506.69 | -17.62% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| TSLA 特斯拉 | 新聞直接提及 | 0.00 | +8.70% | -6.11% | 404.11 | 456.56 | -11.49% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：新聞直接提及「OpenAI」，共 3 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- TSLA：新聞直接提及「Tesla」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [OpenAI co-founder and former Tesla AI executive Karpathy joins Anthropic - Reuters](https://news.google.com/rss/articles/CBMi3wFBVV95cUxOVGY5aXh3VWF5NnFfXzE0ZGlXUlFWMjZZd2Fma0NncENURmhIbWF3SHcwTjhON0E1dGNYS2NBZTJwaTNQUEllSnNDWTk5RmR1dXl4XzlEbkNTRm1PM3h4RklFYnZlYS1yTGdlaW4tSndtN1BXQnJ0TFF5YUJpRnR0dFJfbm1uSjM3VG1kUXpjOHBNUk82WVEwUjFwVHhtWngtQUxtQldJakpUSWFueFRkdzVBX0NsV1ZSSUprcDhFOVRiNjR3OXRvODIzbWpfWFNVQzBlejV1SWtiRjlpMXlF?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 19 May 2026 16:15:59 GMT
- [Google debuts new AI models, personal AI agents in effort to keep pace with OpenAI and Anthropic - CNBC](https://news.google.com/rss/articles/CBMiekFVX3lxTE1oM0xhc3gzR1phR242UDVKSjFyN2pIQXZ2VHRobVNVVElHVWVFbG5hVGF3Q0VUWGliZDhLemdWa1ltRmZ2TlBuTVFOX2hyZ0JaRzhZSXFlRWtZcHZuZ043c1JIUWdlOHRtVmxrVGZCdlBzTUpwMnlUdk9B0gF_QVVfeXFMT09kbmg3TlRTbllJdGJVbF8xRzd3T2lUYV9ycmxBYnN4azJjOThzWXFvU2NBV1JNMktOOEtDUm9xb3V4d2pVVTRCNTVNcVc3UlhHNUk3bWhBVTl6YkxVeU91U25lVmJuWEVCRzBwcGFITkNmYi1UdVBlbVo5dUVmZw?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 19 May 2026 17:47:26 GMT
- [Anthropic hires OpenAI co-founder Andrej Karpathy, former Tesla AI leader - CNBC](https://news.google.com/rss/articles/CBMiqgFBVV95cUxNX3BaX2VoOXUxLXdIWm4tNWVHTmdob2NKeFpXeUR4dV9WNlZSc0pYeFZ4RlpyZHpOSnlheTV0WlVzRjUtYWVsU3VJNzdrdnUzdEI2NGhwT1gwaEZsRXpxQ1gyRVNvQ0JNUDlvNjdudHoxcmdIa0w4U1VkeHZrUWNMbUNteUZqV0xJZVZfeHNWdVhoOGxmSmI5aDU5VUxaOERFUTdibW1SS0RJd9IBrwFBVV95cUxOaUFIT1FQWlBnMXBYRHZZR1puZ0xGVUFUMzJWbU85dGdueDIzZU5rSGd5ZkRtbnNSRUVfZXM4ak9NcVZLclA5U2UwVFRQQUNNVnhwOEpYUmhsYl81NWpIX0QtdlRNVzdjQloxckRmNFhPNG1EMFhwUk9BeTF6c0t1VkhydFNIZVFrX2hrWjBtbmxWeFdpdklqX1JBUjc0b1laQkg1WDNfQzJLVzN5TjBv?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 19 May 2026 16:31:08 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：AI chip stocks slip ahead of Nvidia's earnings - Seeking Alpha；Intel Stock Bounces as Wall Street Rethinks AI Narrative - TechStock²；AI 需求爆衝，Google 執行長：每月處理 3,200 兆 token，年成長七倍 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.72 | +26.50% | +15.42% | 220.61 | 222.32 | -0.77% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.72 | N/A | N/A | 110.80 | 110.80 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.09 | N/A | N/A | 414.05 | 420.99 | -1.65% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.04 | -2.86% | -2.22% | 2,205.00 | 2,240.00 | -1.56% | 背離 | 74.39 | 29.65 | 410.73B TWD / 17.50% | 2026-05-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | -15.16% | -9.33% | 417.42 | 506.69 | -17.62% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.07 | +32.81% | +24.08% | 411.07 | 420.71 | -2.29% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.04 | -13.87% | -14.95% | 472.00 | 510.00 | -7.45% | 背離 | 10.86 | 43.83 | 62.25B TWD / 19.22% | 2026-05-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.04 | -7.34% | -14.73% | 3,155.00 | 3,400.00 | -7.21% | 背離 | 62.91 | 50.28 | 46.74B TWD / -4.14% | 2026-05-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。 方向判斷命中詞：成長。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：成長。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：成長。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AI chip stocks slip ahead of Nvidia's earnings - Seeking Alpha](https://news.google.com/rss/articles/CBMiiwFBVV95cUxPc2tRY0FlOENHczNna3BoNXdDbnhoc1dfdVBrSm1tRUpEN1REU09VVEVsdldwVmNsalpaeUwxVnFJazRyTjktdjduejBObE83a1BSTWoyOEpUcUZLMDBwaVVNY1AxR1JuX3NqYmxtd3BPWWotQmVJVFQ5Y19Zd1F5bFFJdjV1N0hQYVVr?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 19 May 2026 15:31:22 GMT
- [Intel Stock Bounces as Wall Street Rethinks AI Narrative - TechStock²](https://news.google.com/rss/articles/CBMimwFBVV95cUxNMGpLUWVVcW9GYUxfYkxMcldvVzZJOWdPcVg2RFlzQi1FU1Rzd0lxQ2ZMWFg3dFZkZUxuUU95RGdvTURmc0ZZVWg4Y1RLeEYwSlFabTRsU05MSk9ieW8wRlpTRi05aUlBMmoxNjZHYWxNdnd4d1ItOWh0NHA2aW02QlF1ZXJZcnBIdzVxUklhRXhJTGJfWkFES1J1NA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 19 May 2026 19:49:49 GMT
- [AI 需求爆衝，Google 執行長：每月處理 3,200 兆 token，年成長七倍 - TechNews 科技新報](https://news.google.com/rss/articles/CBMirAFBVV95cUxNdHZYeHZSdjY0SGpWVmJmSUZFQW5OcnFrNmxxUHpnblk4OTFNZ0t0UGx1dXBIcUMzQ2RiZ2psZm9sSHNxcTVwM0hONWMtckhkdi1kMmtHN3U2WjN2TDBMYVZjUjJGZVN1QjJTSi02eFJLU1hLSmN5RTVzcEJwVGFhU2p5X3MxdXNPWElyQXdnd1hZNEdpcEwwQk1aYnJqblMtNnpsTWpDc0VvT2gy?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 19 May 2026 22:06:36 GMT

## 新興題材：CoinCentral

摘要：新興題材：CoinCentral 相關新聞集中在：Intel (INTC) Stock Hits Near All-Time Highs After Earnings Shock the Street - CoinCentral

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 110.80 | 110.80 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel (INTC) Stock Hits Near All-Time Highs After Earnings Shock the Street - CoinCentral](https://news.google.com/rss/articles/CBMinwFBVV95cUxPRjYzcFZBVld4Q0RCWWp1bkRNVW9Jenhpano0QXhaUDB2d2ItUUhaNi05ZkFTaE8wbmcwYl81RU1LemR2YzVpNlZQZy1wc3ZQeTRLZENOc09TLTlGMlVVb3owWm9BZVNHOE1PbHNHNDk0a1NLNnQ1MzY0X0FQYmxDRVZlSG1OeXR0RTUzeTZLZVFKbGZLMU14ellvZmE1V1k?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 19 May 2026 14:25:03 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Micron and Intel shares push highs again: What is fueling the rally? - MSN；Micron Is Up 6% Today: Is It Outperforming Other Memory Stocks Like SanDisk and Western Digital? - 24/7 Wall St.；Micron (MU) and SanDisk (SNDK) – Why a Top Analyst Boosted Price Targets on These AI Stocks - TipRanks

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | -0.76 | N/A | N/A | 698.74 | 698.74 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.57 | +0.04% | -4.73% | 1,383.29 | 1,562.34 | -11.46% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.56 | N/A | N/A | 110.80 | 110.80 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +26.50% | +15.42% | 220.61 | 222.32 | -0.77% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、MU、memory」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：fall, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk、SNDK」，共 4 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Micron and Intel shares push highs again: What is fueling the rally? - MSN](https://news.google.com/rss/articles/CBMijwNBVV95cUxOcUNfZ2xVR0VaQVBiek1PWEZWcDFLV0VTYk14YU5xZ2htOFJpbS1vRlBpM01hOXY0M1BseHNPQmpuTW5SVFo0QjB0WmhSSmlkaUdnOVJZSUE4LWZtbmdFSzlZdTduODd1U2MxUXRmR0hLWGNFWEFQMFU3aHJTZU5rSGNZbFJod2ZNNFZybUlFUnpVWFoxd0hBRjBRYnZmYm11RlR4ZHBzRGZCMGduUDQxcVBsZzVWM3JZZGktVlpCcDBvV0NNc0k3ZG1YNjRiNUg3eVFTUDB5dDV1aWxialBvNFVQRExCYzQ3eGprSUVaTWhPOXhEMEJVM3hKOVRIYVl0MDdqc25YUVdpa0hIYVd0LWEtWkYxamF0YXAxV01JQnVJMDV6NG4tVGNsdTRPLWlrTjBvZklKR0VhWUNQTnVabmlOYXIxZUZWV25MNFBwMW9aaDhKQXN4OVN2bnVWLXNZZ0RHeE9VWS1MME93c1hNdW40TDBIYWMtVjVGWjJtdm00cUhTZVBiNUJxbUpuU1U?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 19 May 2026 07:34:07 GMT
- [Micron Is Up 6% Today: Is It Outperforming Other Memory Stocks Like SanDisk and Western Digital? - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi0wFBVV95cUxNUlZhQy05U3k1YmxlSVJDNmNaemFpdDAtSE8xOF91U1oxUFMxRHNDZU9Leks4blNuM3ZTSmxPTkktbGdJaXBSNlVkWkdZN3VGaDJtcXA5TUVQYUUwMjJqeXJjTnptVmRuSmNVOFpQaHF3bU9EMldCVTJkLWhnMTZwUUw4TzJXRTJNeEllTjhxRFVfOFM5bDZIcEVrQVhUUzFab0MxNWVVeGF3NGFfc0NfQTlOWXd2bG01bUdsR05ZSDl2ejNRNnZPMkNpSXdlWjFyS3Vv?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 19 May 2026 18:17:14 GMT
- [Micron (MU) and SanDisk (SNDK) – Why a Top Analyst Boosted Price Targets on These AI Stocks - TipRanks](https://news.google.com/rss/articles/CBMitgFBVV95cUxPemJ3SDk4amFybllYNU9pckVlWnRRekFSNm9yTlQtZ21icEhQZGV4Ny05M3FMWEhpeHBESVN3cFZVaHpzd2lVY1ZMX3hKcFhfV1NFZ2lSemNhc0RJcTdneENWY0hHWk5PQWhSclgzQWY4LU8xa3U0aDg2WllmdnYxWVRsMHlTeFVrbDRWM2N1TUlpRlJRTlZGRzc2bGM4aWFQUWNfUGZ3V1hUQWp0OUhmdzBRZnJTdw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 19 May 2026 20:35:19 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：《台股盤後》收跌716點、失守月線，日K連三黑- 新聞 - MoneyDJ理財網；統一證券：台股估短期維持區間震盪- 新聞 - MoneyDJ理財網；台股焦點：朋程(8255.TW) - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》收跌716點、失守月線，日K連三黑- 新聞 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikgFBVV95cUxPbWRrYkxaVkpMVUVNdEstSGxYLUU5bzF4QklYU254bnRYM0VQLWhEb1B5aVE4OUpudkNIQTYwalpjTm43QTJBdUlBd1ppVjVUWFpyZzhUN29STU5aRnRnTDB4Y3prbnhHYlR3TDh6Z25vLTlOYWxSU0pLWE9lak5zaXRSdE4wdVpsT1hrN3FEV0podw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 19 May 2026 07:45:00 GMT
- [統一證券：台股估短期維持區間震盪- 新聞 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikgFBVV95cUxNaW5NTGpqVF9jNnZMQUN0Q0M2RFA1bDVkeEJpc2diR2FteUo1aGtiWkMwb0xRc2tpbjVpUGFJajVoVndVaVNPNHFxb1otVlRyZTd5VGwyM0lSa3ZwVXV3ZHY3ZHVSQ3dvNjZaLUNETkdrUFpjajcwQWlmcXdBY3E0cE9ObUx6RHRlM0xQT0RQa2VIdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 19 May 2026 00:43:00 GMT
- [台股焦點：朋程(8255.TW) - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikgFBVV95cUxOSDJpN05MQl8xZG9DOWVveHE4SlRYVGxYamZYSUcxNDNkWmhYRm9pZTNTT3RPREZvdW14M0FHOG1DckZrc2FSU0J6WDZETXNiZnUxMk1RVWNCQlhRTVJ4bGI2YnNCQWRBZ2ZoZF93Yld0NGVMcC1KX3A0MlZ1bnJ2NWRKYVY1SUxaT1lBSTVjNW8tQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 19 May 2026 01:22:00 GMT

## 新興題材：千金股驚現跌停

摘要：新興題材：千金股驚現跌停 相關新聞集中在：台股雙萬元破局 千金股驚現跌停潮是怎麼回事？ - 經濟日報；台股雙萬元破局 千金股驚現跌停潮是怎麼回事？ - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股雙萬元破局 千金股驚現跌停潮是怎麼回事？ - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxOUjJOVThMQlliclpXZHcxZGNrVU9hNTdud25jSFoyMkpaTnpQLW95cF9ZY0tIUW9fWkpvM0Vub29WUzUxNml2dWhtd2t5YVVKWElhRzhBZTFMaEtWRDNwYzBJNDVEQnV3WXZaR2VHdS1Dc1QtX0IzbEUwZml0T2U4a9IBX0FVX3lxTE1KYWpIWmxxUGYzYnE2NU5pUUR3eXVkTjZOUk4xQmNPZ2puTENNbzBvRmt1Nndjb19hQ29FZUt2Z2c4ODJCUEw1eG5nZGVmSnl2RTU1MnYzdE9KbGhLaWhR?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 19 May 2026 13:17:50 GMT
- [台股雙萬元破局 千金股驚現跌停潮是怎麼回事？ - 經濟日報](https://news.google.com/rss/articles/CBMid0FVX3lxTFBoNG9GYVU0WWFmMFE1OG5EWjV2dDFldTlRVGw0UEJjcnJVOU45Q0ZfbWVuc3hVZ1RyMlM4NzYwYVJQNDJ6dzRqR195SXpkbDJHNklTbV9vWVozMkppanJmQ0lza21Wam0xNC1PN3NhbVdINmJqTTQw0gFfQVVfeXFMTUphakhabHFQZjNicTY1TmlRRHd5dWRONk5STjFCY09nam5MQ01vMG9Ga3U2d2NvX2FDb0VlS3ZnZzg4MkJQTDV4bmdkZWZKeXZFNTUydjN0T0psaEtpaFE?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 18 May 2026 22:00:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
