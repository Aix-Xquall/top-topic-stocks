# 每日股市熱門話題分析 - 2026-06-19

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **關稅與供應鏈轉移**｜正向｜熱度 2｜市場確認 74.41｜同向 1/1
2. **新興題材：SpaceX**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
3. **記憶體與 HBM 供應鏈**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0
4. **AI 伺服器與資料中心**｜負向｜熱度 16｜市場確認 32.85｜同向 3/6
5. **半導體與晶片供應鏈**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.06（樣本 7）
- 5日相關係數：-0.04（樣本 7）
- 同向比例：4/7

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 關稅與供應鏈轉移 | 74.41 | 1/1 | 0 | +1.47% | +7.11% |
| 新興題材：SpaceX | N/A | 0/0 | 0 | N/A | N/A |
| 記憶體與 HBM 供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 32.85 | 3/6 | 3 | -0.71% | -8.30% |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：B600 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
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
| 2026-06-17 | 0.17 | 0.47 | +62.50% | 8 |
| 2026-06-18 | -0.41 | -0.41 | +42.86% | 7 |
| 2026-06-19 | 0.06 | -0.04 | +57.14% | 7 |

## 歷史回測摘要

- 回測日期：2026-06-19
- 近5日 3日相關：0.02
- 近5日 5日相關：-0.15
- 同向比例：+57.89%
- 權重狀態：已調整

- 方向準確度：+57.89%
- 信心排序準確度：0.02
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

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：連噴5根仍未達目標價！「液冷關鍵廠」雙題材股價衝史高、EPS上修12.2元 打入AI巨頭供應鏈 - FTNN 新聞；台積電結合台日供應鏈發表玻璃基板封裝成果，給韓國對手強大威脅 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | +0.48 | +1.47% | +7.11% | 2,410.00 | 2,410.00 | 0.00% | 同向 | 74.39 | N/A | 416.98B TWD / 30.09% | 2026-06-01 |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +12.81% | +28.38% | 298.01 | 312.06 | -4.50% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | +0.37% | +3.87% | 268.50 | 289.00 | -7.09% | 不適用 | 14.13 | N/A | 859.41B TWD / 39.57% | 2026-06-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [連噴5根仍未達目標價！「液冷關鍵廠」雙題材股價衝史高、EPS上修12.2元 打入AI巨頭供應鏈 - FTNN 新聞](https://news.google.com/rss/articles/CBMiS0FVX3lxTE1haHk4NXN0eVJ2MFRONzR3bWZMNXBTdTBDTC10cVlabFZVUkFFUndSdnhRXzQxLXVWVFdQRlM2ZjNwRXFDZWdhV2JoUQ?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 18 Jun 2026 03:35:00 GMT
- [台積電結合台日供應鏈發表玻璃基板封裝成果，給韓國對手強大威脅 - TechNews 科技新報](https://news.google.com/rss/articles/CBMi8gFBVV95cUxPVTZDVGxpOWJURVYweU5WS2lScjJIZURmdWxKYzQ2TjV1SGxPR0Fya0ZBdlVCa2RNRVdCcC1ZZ2JzeVVsSXFXUHlhUjJlcm1GWXFwWnQwWXMweEhWS3RyZndibm8waFBTajAtcnpWSms3UUlqdENSZS1jRGFRTkdMb1BuSGlRbUZnMGlXTGVPelV6cHMzVndkNUcyZWtoQl9uSFZEejRaV05oTENOcU10NUdPa1dFR1RRdlZOa2hHeFlSWjRJQUg4X2dwbkc1VWdBcGVuU2lnZngxUjhhSE1samFKUXNZaXk2a2NkVS11UUhvQQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 18 Jun 2026 10:46:04 GMT

## 新興題材：SpaceX

摘要：新興題材：SpaceX 相關新聞集中在：Stocks making the biggest moves premarket: Intel, SpaceX, Micron, Carnival & more - CNBC；SpaceX has even more room to run after AI coding deal, Oppenheimer says - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 133.99 | 133.99 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 1,133.99 | 1,133.99 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MU：新聞直接提及「Micron」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Stocks making the biggest moves premarket: Intel, SpaceX, Micron, Carnival & more - CNBC](https://news.google.com/rss/articles/CBMihgFBVV95cUxPNHBLeVJzRWRieW4zTzhTbE1zTXdVbTRUbjh3bHhwTWFtZEt0bmRoZ0NXaTlUTDFxbmdwV0stQi1pNFlFRXVidVc4dkZNZjk5M1EzZnF5MWpzZ25BTGxEbnRjbXBpcmdzLWNmU25YRkRocC1fSldzUnE1OFVmc0NvT01LNjU4QQ?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 18 Jun 2026 11:43:15 GMT
- [SpaceX has even more room to run after AI coding deal, Oppenheimer says - CNBC](https://news.google.com/rss/articles/CBMiqwFBVV95cUxOaUo3RHA5eVRDcjRQV3E4dVpkbWxsUUQwRTFLdU1UVkZ6SnU3dWJMX2xWWWFDZDNmY1BocmJNS3ItMDJySEZmdEx0czdtRVUwdVQzOGpFVUJoSTFZSFlOM2RlNEstbnR1Q0lBeDhxOUlrTEZCN1lZWFA5S3B2THgtQVdGb1VQU19hYXNwcXN3OHpKWk5INVJuLWZDN0RDQ1NtTThScy1tTDNILXc?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 18 Jun 2026 14:25:07 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Sandisk vs. Micron: Which AI Memory Stock Is the Better Buy After Their Monster Runs? - The Motley Fool；SanDisk (SNDK) Is Doing Something Unprecedented In The Al Sector! SNDK STOCK PODCAST ANALYSIS BUY Jobe Bellingham (gRMiCAoJ7a) - Mshale；Stocks making the biggest moves premarket: Intel, SpaceX, Micron, Carnival & more - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 1,133.99 | 1,133.99 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | +3.65% | +16.12% | 2,184.75 | 2,184.75 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 133.99 | 133.99 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +5.57% | +18.91% | 210.69 | 211.14 | -0.21% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron」，共 2 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk、SNDK」，共 2 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Sandisk vs. Micron: Which AI Memory Stock Is the Better Buy After Their Monster Runs? - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxOelU0TGtoLVNkdXBiTHloOFYyOGJ4X1RQLVNhamtveXI1aTQ3WmwyRG5XWVNEQ3hMc1UzeURTTnF4TTN2Z1lOSjVUaGM1N3JNRE52cHJtQnNjRTdCSklpOWl6ZzVENHZsUmdhU09TVlBkaDlacjFSeV8zYkdnYU9vU1lBT1Q0ZnNsWWlHUUZPZ0c3em9PWGs5cg?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 17 Jun 2026 00:21:00 GMT
- [SanDisk (SNDK) Is Doing Something Unprecedented In The Al Sector! SNDK STOCK PODCAST ANALYSIS BUY Jobe Bellingham (gRMiCAoJ7a) - Mshale](https://news.google.com/rss/articles/CBMiW0FVX3lxTE82c25ZNkhMbnBFcHlYZktjT2gzRlFzREd4ZFlubTJYeG4zZFJ6NU1OdGxaX3BRYWM0bFdDWk5tMlNVS3BvWXRLZW1jUVp3SUdNYXlKam5zNEhNVm8?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 17 Jun 2026 12:04:02 GMT
- [Stocks making the biggest moves premarket: Intel, SpaceX, Micron, Carnival & more - CNBC](https://news.google.com/rss/articles/CBMihgFBVV95cUxPNHBLeVJzRWRieW4zTzhTbE1zTXdVbTRUbjh3bHhwTWFtZEt0bmRoZ0NXaTlUTDFxbmdwV0stQi1pNFlFRXVidVc4dkZNZjk5M1EzZnF5MWpzZ25BTGxEbnRjbXBpcmdzLWNmU25YRkRocC1fSldzUnE1OFVmc0NvT01LNjU4QQ?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 18 Jun 2026 11:43:15 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：AMD, Arm, Intel Get Price-Target Hikes On 'CPU Renaissance' - Investor's Business Daily；美中若鬆綁，韓國 AI 紅利如何延續？ - TechNews 科技新報；威盛股東會陳文琦釋展望，佈局 AI 與光通訊搶攻先進製程與矽光子商機 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.62 | N/A | N/A | 133.99 | 133.99 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.60 | N/A | N/A | 537.37 | 537.37 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | -0.03 | +5.57% | +18.91% | 210.69 | 211.14 | -0.21% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.03 | +1.47% | +7.11% | 2,410.00 | 2,410.00 | 0.00% | 背離 | 74.39 | N/A | 416.98B TWD / 30.09% | 2026-06-01 |
| MSFT 微軟 | 產業/供應鏈推估 | -0.04 | -3.40% | -25.12% | 379.40 | 506.69 | -25.12% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -1.46% | +28.73% | 411.35 | 446.77 | -7.93% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.02 | +3.90% | +12.68% | 613.00 | 613.00 | 0.00% | 背離 | 10.86 | N/A | 63.03B TWD / 28.57% | 2026-06-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.04 | -1.79% | +7.47% | 4,390.00 | 4,460.00 | -1.57% | 同向 | 62.91 | N/A | 47.43B TWD / 4.99% | 2026-06-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 5 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AMD, Arm, Intel Get Price-Target Hikes On 'CPU Renaissance' - Investor's Business Daily](https://news.google.com/rss/articles/CBMikAFBVV95cUxNQUtOLUo0YWtpcFhqaXZQcm00UllGOTM4X0VoUTNneEJRQnktSXkxNENJSXM0c3ozZDNGRFRKQi1rckFLNUtXMXo5bm9IMEt4TDhiTkdvNFB2TVFVM1JIOEVnVzNFLVlqbzhVMDliVUhrVUhqOC1WSzNIcy1pOVBfWDl4blNuZm11RFYxU25rNXU?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 17 Jun 2026 20:40:00 GMT
- [美中若鬆綁，韓國 AI 紅利如何延續？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMikgFBVV95cUxNVXpka1FqdDJOTzRBaGJOS3FtaUtOWlpfc1BDYTNVRC1IbnM4RzlkMFpPa05yWEQ1Zk81LXJ5ZUJGMG81SnhqZnVwci1EX0ppR1lVeWxrMGdiUmt2amptOU5QQkhtRVBpNXpDdkVxakZtYkktdmpEYlY3eEFSMkdtUjlLZFZoRFhtT0xsTmtxT2d6Zw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 18 Jun 2026 13:22:45 GMT
- [威盛股東會陳文琦釋展望，佈局 AI 與光通訊搶攻先進製程與矽光子商機 - TechNews 科技新報](https://news.google.com/rss/articles/CBMisgFBVV95cUxObjhDN1pRcGpFcklhNHBhdmhZRFV3LXZlY3BLUjkzX05LNnZhWlpLbFdjOWxCTmNFZjVBMjMzZmNyaWlmb3U3T0FTWm5RTTZERGhyZnQyYmRVbEZsdUxrS2NpOGU2NFNEeUwtcUJNTmJGZXpVV3N3dThNYjdYaTJmcjBoNGx6d1kzMFF5dzBuUFYwbmg0MWdaY1VZNTRjVmhCSjcxQVRzSGVzckNvbTdaR2ZR?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 18 Jun 2026 10:01:14 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel Soars 10% After Trump Says Apple Will Partner With Intel on U.S. Chip Production - 24/7 Wall St.；AMD, Arm, Intel Get Price-Target Hikes On 'CPU Renaissance' - Investor's Business Daily；晶片股領漲美股收紅 SpaceX連2跌 | 美股動態 | 國際 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 133.99 | 133.99 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | N/A | N/A | 537.37 | 537.37 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 新聞直接提及 | 0.00 | +12.81% | +28.38% | 298.01 | 312.06 | -4.50% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +1.47% | +7.11% | 2,410.00 | 2,410.00 | 0.00% | 不適用 | 74.39 | N/A | 416.98B TWD / 30.09% | 2026-06-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +2.83% | +16.40% | 145.50 | 145.50 | 0.00% | 不適用 | 4.00 | N/A | 22.94B TWD / 17.78% | 2026-06-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +5.57% | +18.91% | 210.69 | 211.14 | -0.21% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 1,133.99 | 1,133.99 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | +3.65% | +16.12% | 2,184.75 | 2,184.75 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AAPL：新聞直接提及「Apple」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Soars 10% After Trump Says Apple Will Partner With Intel on U.S. Chip Production - 24/7 Wall St.](https://news.google.com/rss/articles/CBMixgFBVV95cUxNVzhoeWlXcXhFaFFMNlJUTjNLemQzVnM4WmVXWFBkRnc1YlFWbjQ0OFViUkhvYy1iMWszQW5ZbnA4RTFXd2wtejlJaEhSSkx4c2UxZkRuZWZFb2JoNzdJQjR2UkRjQktqVVp1TlFSZFV4dGE3c2p2MWJSM3h4OGhKbmsxam1fZTF5MTVBZE9zRW92cXMxMmhyR3Y4OXJ4YnNSZ2V6SlJhSkExeHRCZS1oQjJLNE9MRC1POFlWR0k4ckl1dm0ydVE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 18 Jun 2026 13:24:32 GMT
- [AMD, Arm, Intel Get Price-Target Hikes On 'CPU Renaissance' - Investor's Business Daily](https://news.google.com/rss/articles/CBMikAFBVV95cUxNQUtOLUo0YWtpcFhqaXZQcm00UllGOTM4X0VoUTNneEJRQnktSXkxNENJSXM0c3ozZDNGRFRKQi1rckFLNUtXMXo5bm9IMEt4TDhiTkdvNFB2TVFVM1JIOEVnVzNFLVlqbzhVMDliVUhrVUhqOC1WSzNIcy1pOVBfWDl4blNuZm11RFYxU25rNXU?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 17 Jun 2026 20:40:00 GMT
- [晶片股領漲美股收紅 SpaceX連2跌 | 美股動態 | 國際 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBKLThndjN2WUdoVUZPZVRnNGc0SG40UW0zV2oyY1JaalU0QXF4X3pqY2VsWDZncUFMSWxtbWppVDZvTVlUNjNwRzgwRG1fZnhpRVRQZ2RwRXg1VWZ6?oc=5) - Google News source discovery | 經濟日報 money Thu, 18 Jun 2026 21:30:25 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：不怕Fed放鷹 台股50K拚超前達陣 法人喊基本面毫無利空 | 市場焦點 | 證券 - 經濟日報；台股上演瘋牛行情！法人：下周插旗48,000點 | 市場焦點 | 證券 - 經濟日報；台股主動式 ETF 大吸金 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [不怕Fed放鷹 台股50K拚超前達陣 法人喊基本面毫無利空 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMidkFVX3lxTE5Ybk1OTVVXeWVRR3BFcDg2NmFnaThtUXZmVXJSSlZwb2RQY1BwTm1XVXRNUVFMR3dHbzMwa1VvRDBmMmU4dF84b3hWVEFGWHExeEt4UkI5bG14ZWQzWnMtdnJMSjZmRmJ1S1JiUXBORzhfTlE3dnc?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 17 Jun 2026 09:00:00 GMT
- [台股上演瘋牛行情！法人：下周插旗48,000點 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxQb0YxRTRVWUZjYnVwUkQ3U3VnQ1E1dzlHLVdxVWp0ODFVU043X2hjUFg2bFVOckJIREZIcnF3b1hQMUFqQnB5MXlhclkzeE5lMlExcEdncnJLQVZLWHJteVdOeWprSHFydGpBdnduNDdscGhRdXNMSDFUZmtIbjJWNg?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 18 Jun 2026 11:21:25 GMT
- [台股主動式 ETF 大吸金 - 經濟日報](https://news.google.com/rss/articles/CBMieEFVX3lxTE00dVRJM2lXLVQtb1BkX0gzdHd1VlRWUXR5Tkd5OG5SQ1RKT3BvdmJSblpiRVlGVjRFZVczTUxZOWlqU2UtNTVna2JjQi1Cb0JuUEVZWlBqT3ZZZURMTjhTdTRuelJOY3pJOE10RHh3RW5DMWxSTm5GctIBX0FVX3lxTFBfcW1fd2t1MUdrMzFtWDFlVEVwczR1UjE4d3ZyYXEyM2VraGU0ejdCZWNucEYyd21sdUNWU3hUMGJPLWw2MVg4ZkxZVlZYajZxdzlidHB2a2txZC1CZVVz?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 18 Jun 2026 17:03:51 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》電金權值領軍、收漲587點/創高；週K翻紅- 新聞 - MoneyDJ；個股動態報導內容-387C0FB7-2F2C-4B46-B600-B6CBA7D78DAE - MoneyDJ；第一金：不排除併購；台股短投市值創高- 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》電金權值領軍、收漲587點/創高；週K翻紅- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNakk5Smd5QVhaRGNNTXFvTzlKQzh6V3BaaHVSX1FReC1jUEFRd0NENGFXMTJBUFItYXV2ZkRHMGtmX2R2TXVRd0duNDF3dlc4cTVvRkdNWVRkclRJOFJXOUhEWmxvQlBMTEJtZTZaemlkVkQwYnk3aDF4RDFWRVdVSS1BMkxEZklFVmYzazRpN2tlZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 18 Jun 2026 07:57:00 GMT
- [個股動態報導內容-387C0FB7-2F2C-4B46-B600-B6CBA7D78DAE - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxNaTdBUm1USGFkNUJrX25uU3FBTmRrMGdObzA1M3VHQW85bU1pMGV2X09EQmVOdk5hRnhTMGlIaDI2dXZ1UzF6ODJQV2xReFZhYmFfRzBfRUxPQWVLTG5rMDRCSklZZWhCY0xJXzlVVDZOcHVjdXQzeXJDMmlWQnhtaHJlMFphcndkMVhERGJ5RXdQd2xV?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 18 Jun 2026 09:26:56 GMT
- [第一金：不排除併購；台股短投市值創高- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxORUJkeXVxUnhQWmNHenNXcFVyY3VGeHNfTEJocWxGQUlTcTVGYlA0ZDZGdWJiNGRWdmJvenh6LUFieDIydlI1MFIxWWY4T2ZJbTV1TzV3ZC1yZG0zSHpra1E1UHBhMUlpdHIxcWQ2LVE1NVFTcUh2M2h5N1NTeGdMdGd6NEthdU9DRm11Q0Y1Z09iUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 18 Jun 2026 05:16:00 GMT

## 新興題材：B600

摘要：新興題材：B600 相關新聞集中在：個股動態報導內容-387C0FB7-2F2C-4B46-B600-B6CBA7D78DAE - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-387C0FB7-2F2C-4B46-B600-B6CBA7D78DAE - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxNaTdBUm1USGFkNUJrX25uU3FBTmRrMGdObzA1M3VHQW85bU1pMGV2X09EQmVOdk5hRnhTMGlIaDI2dXZ1UzF6ODJQV2xReFZhYmFfRzBfRUxPQWVLTG5rMDRCSklZZWhCY0xJXzlVVDZOcHVjdXQzeXJDMmlWQnhtaHJlMFphcndkMVhERGJ5RXdQd2xV?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 18 Jun 2026 09:26:56 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
- TWSE PER/PBR 抓取失敗：Expecting value: line 1 column 1 (char 0)
