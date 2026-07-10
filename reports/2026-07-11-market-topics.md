# 每日股市熱門話題分析 - 2026-07-11

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **綜合市場情緒**｜正向｜熱度 34｜市場確認 81.16｜同向 1/1
2. **記憶體與 HBM 供應鏈**｜中性｜熱度 8｜市場確認 N/A｜同向 0/0
3. **新興題材：SpaceX**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
4. **AI 伺服器與資料中心**｜中性｜熱度 12｜市場確認 40.74｜同向 3/6
5. **新興題材：6月營收**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.13（樣本 12）
- 5日相關係數：-0.08（樣本 12）
- 同向比例：6/12

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 綜合市場情緒 | 81.16 | 1/1 | 0 | +3.72% | +5.02% |
| 記憶體與 HBM 供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：SpaceX | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 40.74 | 3/6 | 1 | +1.92% | -2.53% |
| 新興題材：6月營收 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | 25.04 | 2/5 | 1 | -0.99% | -11.43% |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：台積將法說 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-06-28 | 0.16 | 0.55 | +85.71% | 14 |
| 2026-06-29 | 0.49 | -0.25 | +38.46% | 13 |
| 2026-06-30 | 0.44 | -0.27 | +62.50% | 8 |
| 2026-07-01 | -0.08 | 0.25 | +30.77% | 13 |
| 2026-07-02 | 0.30 | 0.03 | +55.56% | 9 |
| 2026-07-03 | 0.21 | 0.08 | +55.56% | 18 |
| 2026-07-04 | -0.22 | -0.36 | +22.22% | 18 |
| 2026-07-05 | -0.00 | 0.24 | +40.00% | 10 |
| 2026-07-06 | N/A | N/A | 0.00% | 2 |
| 2026-07-07 | N/A | N/A | 0.00% | 1 |
| 2026-07-08 | -0.05 | -0.05 | +71.43% | 14 |
| 2026-07-09 | -0.11 | -0.36 | +64.29% | 14 |
| 2026-07-10 | 0.55 | 0.05 | +77.78% | 9 |
| 2026-07-11 | 0.13 | -0.08 | +50.00% | 12 |

## 歷史回測摘要

- 回測日期：2026-07-11
- 近5日 3日相關：-0.16
- 近5日 5日相關：-0.13
- 同向比例：+44.44%
- 權重狀態：已調整

- 方向準確度：+44.44%
- 信心排序準確度：-0.16
- 診斷：方向與信心皆需修正

調整原因：近 5 日方向與信心排序皆偏弱，降低方向詞與供應鏈推估權重，並加重背離扣分。；關鍵詞×公司後續樣本有效 5 筆，未達 30 筆，不調整樣本權重

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

摘要：綜合市場情緒 相關新聞集中在：台股波動放大 逢回可布局 - 經濟日報；群益證攜集保推動「開放證券2.0」 跨券商一鍵授權財力證明更便利 - 經濟日報；群益證攜集保推動「開放證券2.0」 跨券商一鍵授權財力證明更便利 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2317 鴻海 | 新聞直接提及 | +0.43 | +3.72% | +5.02% | 237.50 | 289.00 | -17.82% | 同向 | 14.13 | 16.87 | 821.76B TWD / 52.11% | 2026-07-01 |

關聯理由（前 3）：
- 2317：新聞直接提及「鴻海」，共 1 篇新聞命中。

### 主要來源

- [台股波動放大 逢回可布局 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBUcm5nV0dPemlQbU5IOXNjbTF6Z0V0UmJiUnIyRDMwaWhjZ3FQZkxCSkxLZXlBczhSRmE5Q0R0M3dQc3NBakUzMFRoSE9kaHloSHlCaFVvblhmQdIBX0FVX3lxTE90OXl1Njk0aFBmVzFhSnJWcWtzZzdnYWYxVEtnNVNmTDZjcUw0eUpqRkJTLWJMLXdDUGxwcUhqWFBYODNKajlsMHhxeTlqbG1CczllTG5HVFB3RjJuRUx3?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 10 Jul 2026 16:10:19 GMT
- [群益證攜集保推動「開放證券2.0」 跨券商一鍵授權財力證明更便利 - 經濟日報](https://news.google.com/rss/articles/CBMieEFVX3lxTE91RzE3cmVoT1YtaXJOSi1GMDVMV2pvd0NBWW95aGFqaUhpOEwtWUM2VHVUTk5QNmlyemFGb2FPM25NOGZSODducUp6a2JvUjJtc3hCNkNvLTNDbF9WLTZOUzFqV3RFc2cyQUhBakxMRzBpRXNzOG8xMNIBX0FVX3lxTE0yMGdWekdUdFpWWnBfakEwdW5xaGFCMjA2TEtGUGVSSzY0d3JQS2cxQ1ZXM01qWDZNenhtUEtGcjBhZ2UzSWJ1LUtSWEJNaFlnMHg2MjVXNGkzZkxaWlFz?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 10 Jul 2026 12:40:56 GMT
- [群益證攜集保推動「開放證券2.0」 跨券商一鍵授權財力證明更便利 - 經濟日報](https://news.google.com/rss/articles/CBMieEFVX3lxTFBkZ2ZYOHJBRjRjaHpfRnhINWd2S0wxOF9aaFhhWmZ5T0xUT3pSSU1OUnhqdzFOSWp4RmdyTnhSVHd3NnNJQlhWLW5TcGtndllaaVMzUWNiMWNEb3RVS0dld3l1WEdtMFZ0bldBYlpHV0cyZHNPQU9tatIBX0FVX3lxTE1HZEpUaW9ENDFyd05IQzktWGltblE5bjB1Vl9QbzJVdXdWR0pMZWNxU1FJX3VDZE5GbXVlY2ZsREMya09Bb0FDLW5EeXFrWkVvelBGMGxaSnFMZmlEOWtv?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 10 Jul 2026 12:40:56 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：MU, WDC, INTC: Why Are Chip Stocks Rebounding In Premarket Trading Today? - Yahoo Finance；SanDisk Vs. Micron: Why One of These Memory Stocks is Much More Dangerous Than the Other - 24/7 Wall St.；SanDisk Vs. Micron: Why One of These Memory Stocks is Much More Dangerous Than the Other - AOL.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 979.30 | 991.64 | -1.24% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | +18.43% | +9.79% | 1,915.92 | 2,335.00 | -17.95% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 109.84 | 114.68 | -4.22% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -0.09% | +20.96% | 210.96 | 211.14 | -0.09% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron、memory」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk、SNDK」，共 4 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [MU, WDC, INTC: Why Are Chip Stocks Rebounding In Premarket Trading Today? - Yahoo Finance](https://news.google.com/rss/articles/CBMijgFBVV95cUxPUGlvNlc0cG0xRDlFRjFaMjk4dDR0UjVWUThaWjJEdHNHaTBPaDZJUGZwVHNaSEhkZDExbEtwd2JuMi0tVWx0QVBhMXhJaEpfaUtqMTlBbzkteXlCbmFqRURuR0QyQW1XSnZTWmNCVDFUckQ2NFM5Q1NiS1ZfNlh3cmJsdnJhLWVqaXpoeEJn?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 09 Jul 2026 09:05:20 GMT
- [SanDisk Vs. Micron: Why One of These Memory Stocks is Much More Dangerous Than the Other - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiygFBVV95cUxPanRqcm9nbXlaWUFJdlRSOVRreUh5NnViVmJIeXpJX0IyRm93N21nQ1hCTEo4cFY0ZVVUVk9DY2w0d2R0Z2NUSTVvZkNfVVFwZTFDXzJ4S2NWNW04YjdWTFVUY3BXQVBDVERRTkg3ZTRKWngwU2VYUUpFT0IzRFNLdnQtNFk1dmN1RnVKeEQ4cmtjSGFidGFCcTZsS2Q2UGc0Tnh4bUE4YUtVd01jRjNBZFk0bEZQaV80a003cGhGeUhUMzNVRFBWakdn?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 10 Jul 2026 15:32:33 GMT
- [SanDisk Vs. Micron: Why One of These Memory Stocks is Much More Dangerous Than the Other - AOL.com](https://news.google.com/rss/articles/CBMieEFVX3lxTFBxMnRHQnBKaGNyQjdaX1Nsc1VUczhucmVUc0hLSGlneXN6NDNDSkUwSktuOU5hNjl0VUxSUEhLUXpEN215WXB5U0RVNnQ2eDM0SFNUVEE5Nzcya0RmRXhTS1FHQUV0bEdFd0JwaDFXUU82eVljQUhQTA?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 10 Jul 2026 15:54:33 GMT

## 新興題材：SpaceX

摘要：新興題材：SpaceX 相關新聞集中在：Crypto Brokerage CEO: “We’re Going Live Today With 24/7 Trading of Real U.S. Equities” Starting With Micron, SanDisk and SpaceX - AOL.com；SpaceX's near-term AI payoff seen tethered to Earth, not outer space - Reuters

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 979.30 | 991.64 | -1.24% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | +18.43% | +9.79% | 1,915.92 | 2,335.00 | -17.95% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。

### 主要來源

- [Crypto Brokerage CEO: “We’re Going Live Today With 24/7 Trading of Real U.S. Equities” Starting With Micron, SanDisk and SpaceX - AOL.com](https://news.google.com/rss/articles/CBMigAFBVV95cUxNRDNZTUpqc0NkX3FWeDBnb1ZNTDhOclE4aUxUZk83YldTV0xiZ1RLM2tka2pwWmNmSnVOclJidHRHMUpCR29SOVVSN0lQOFpGUUhFV1hSb3JCTTc4ZjRxeUV1UmxadW5xSmpGQ2J0bkVOTHZMeDNkMkUwSklDSjBBOQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 10 Jul 2026 16:25:08 GMT
- [SpaceX's near-term AI payoff seen tethered to Earth, not outer space - Reuters](https://news.google.com/rss/articles/CBMiqwFBVV95cUxQUWpsRnIya2JuUDVDWlg1eFN4Zk5ZVUE5UWtMY3ZTTlRzTGtVellDRVZZWXNEeldhQW9UOEg2Mlo3bGVOQWlaeEV2QVhOUlBfMmJkdTlvdUxRdVl1Vks4WFdaTXRMaVJ5Y3d5TDNFeFgxWU0xZTRTMXlwS1hUME1zT3lWWE5mLWVsTk1mUzc3VHEyU2NOSUZTLVBEVWNhV3oxV3Vpdkx4cUFxbjA?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 10 Jul 2026 13:26:56 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel Stock And Other AI Semiconductor Names Retail Investors Are Watching - simplywall.st；少子化掩蓋真相，AI 取代低階白領釀台灣人才斷層危機 - TechNews 科技新報；硬體作為 AI 服務入口，未來的獲利模式趨勢？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | -0.42 | -0.09% | +20.96% | 210.96 | 211.14 | -0.09% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | -0.56 | N/A | N/A | 109.84 | 114.68 | -4.22% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | -0.06 | N/A | N/A | 557.89 | 557.89 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.06 | -2.03% | -2.23% | 2,415.00 | 2,415.00 | 0.00% | 同向 | 74.39 | 32.47 | 416.98B TWD / 30.09% | 2026-06-01 |
| MSFT 微軟 | 產業/供應鏈推估 | -0.04 | -1.95% | -24.00% | 385.10 | 506.69 | -24.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -10.48% | +29.23% | 399.97 | 446.77 | -10.48% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.03 | +0.15% | -6.46% | 677.00 | 680.00 | -0.44% | 未明確 | 10.86 | 62.86 | 65.78B TWD / 32.86% | 2026-07-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.02 | +2.91% | -2.30% | 3,925.00 | 4,310.00 | -8.93% | 背離 | 62.91 | 62.55 | 58.01B TWD / 2.80% | 2026-07-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。 方向判斷命中詞：衝擊。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：衝擊。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：衝擊。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Stock And Other AI Semiconductor Names Retail Investors Are Watching - simplywall.st](https://news.google.com/rss/articles/CBMi2wFBVV95cUxOR01WUG5oWGdDdkw2eFFQeUJYMkc2QUY4Z1J0RGFrM3UtSEY4aG1yd1oxdzZHT3pJNUFoaHEwa2pzRE9XbWZQblV4QzlrczNHRDc1MWFEYjVOQ2ZIY1hrY2lhMFJCcThtOUJEcFRQVDRFR3BGcDBVN1dva2Fyb1IxVE91VEdvYlpkaUhuOThvWXNXbkQwOTM0cXBLclh3MHI4N0VBSFIzTnh4aWRsZEVmamczY000SGJKMzhQbVNzaXhRZ3NGalhfVk9LZURUb05tS1JudTBDbkJLNU3SAeABQVVfeXFMTVN6am1OYWdJcVVvT1A0ZkV3OV9tLUdFTUxmcVZJSml2eVB6MDZPR2prU3luaUxvVDJUbkR2Y2I4ZG40OGthRDFWcnZvbTMtRjBCaHU4Tjd0VWItUlJBYlA1WndlTjk5Y1FpZklEblVROTI0QjJoTlAtVjBXVHZiaEUwdWZCRVk3WWJaalgtY1NzZkFPbDNVVTUzb0wtS2hscnFraFNaVndPWXdCWG1oaUk2T3JzbkNzSWU3UVNXUnNMei1fdWJJbzlDdHRMTmpsWFg0bTdzSU1xOHFpWHNydFI?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 10 Jul 2026 06:35:37 GMT
- [少子化掩蓋真相，AI 取代低階白領釀台灣人才斷層危機 - TechNews 科技新報](https://news.google.com/rss/articles/CBMimAFBVV95cUxPN3RYTzdacW9FUThYakVNRm1fNG5lVW02d0stSExmaXEyTFVUOHloUW1nZVRocE0wNTFYcUY3UFp5OEd0Vm5fTVpvb19RTXFqTnFXaGZKaFhDNDNaazloWlh0ZkU4aXdheVhfSXJsQ19odHNCQWtyQTdGUHdlVUd3VFFxZTBPRXNoVnhNWEZaUWQ5OHFMQXhPZw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 10 Jul 2026 09:49:39 GMT
- [硬體作為 AI 服務入口，未來的獲利模式趨勢？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiZEFVX3lxTE1DaDlpUm1rWjlFZHJVR1M5LXBGZ1RZVkN6V09Zb1NHRnFlN1Z1UF85VGFITTdfMnlKTllLSTlNcWJwaUxLY1lBbF9IX1lPczNLenFaNGRKb1dOV1g0eEhLMlJvMC0?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 10 Jul 2026 21:08:45 GMT

## 新興題材：6月營收

摘要：新興題材：6月營收 相關新聞集中在：說好的開獎呢？颱風打亂台積電 6月營收延至下周一揭曉 - Yahoo股市；6月營收下滑22%後，1—6月累計營收為何也同步年減40.88%？ | 鉅亨網 - AIGC - news.cnyes.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | 0.00 | -2.03% | -2.23% | 2,415.00 | 2,415.00 | 0.00% | 不適用 | 74.39 | 32.47 | 416.98B TWD / 30.09% | 2026-06-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。

### 主要來源

- [說好的開獎呢？颱風打亂台積電 6月營收延至下周一揭曉 - Yahoo股市](https://news.google.com/rss/articles/CBMi_gJBVV95cUxQMlc2R0xUeVlJSERkaFlSemdvTmFOZGp0ZzdOZ2o2QjJNbENmTmpTVUtWbkNDR3JmVlJTQU9aWXpRenl1T1Z2QWtCR3JiTzJUdmZnb19JUXJac2JoNUpUUUFhNG16WEQ2aVdHcl9kTXZCa2k3N3hveWxGWHNCMGN4U2dLMmNJRWJpUjdBT1ZwVnZtSEd1OTJ2LXF1ZlJlUUhoOG9RUS1JY0JfMHFBbk9MdUFuR1ZyQm9GQjRCYmVRNzR4bDJ4VGJ3RThsZlpZaE45MnQ4N3Nvc3pOZUs3cWNDWnhkQUVVM000YzBfSmc0S1hleGVsTmwzT1lYR3poWDNTS2FCQTdtTXZwSEhURnFhTjhLQjZROVRCSEdXZlpvRVRQcEU0bFcxeG5LUmxGa0ROT0tOa0xhR3NDR3dOaE1kWHBqWXdOOU9FMXozWWRsSWJBd2x4TnZFbnhtVDlLQXQ2dXZGVEU1SmpXblNEc2I3QlNaZlBsdV9Bc0ZCVnBn?oc=5) - Google News source discovery | Yahoo 奇摩股市 Fri, 10 Jul 2026 05:59:37 GMT
- [6月營收下滑22%後，1—6月累計營收為何也同步年減40.88%？ | 鉅亨網 - AIGC - news.cnyes.com](https://news.google.com/rss/articles/CBMimwFBVV95cUxPbUFrTUQtX1J0cF9odUVxUFJ4RzZpTW9GZkpLSDAtNTFveE5hSDdJb1QtaVI3VS1oWG9XYjI2VDlTVmdJbW5mM0JsS1lfdjZtazV6Zmc2S0NOd1Y1ck4yRjE1bkdjU3VQX1NhNVVyNkhLcUhJMG9OT1FqZlVmanBYUGtaOGpHRFM2RXl5U3E4ckdIX3hUR0FUV2xXdw?oc=5) - Google News source discovery | 鉅亨網 Fri, 10 Jul 2026 09:48:20 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel and Applied Materials Dive 10%, AMD Craters 8% as Samsung Earnings Trigger Chip Selloff - AOL.com；Taiwan Semiconductor Is a No-Brainer Buy Before July 16 Earnings. Here’s Why - 24/7 Wall St.；Intel Stock And Other AI Semiconductor Names Retail Investors Are Watching - simplywall.st

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.59 | N/A | N/A | 109.84 | 114.68 | -4.22% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | -0.53 | -2.03% | -2.23% | 2,415.00 | 2,415.00 | 0.00% | 同向 | 74.39 | 32.47 | 416.98B TWD / 30.09% | 2026-06-01 |
| AMD 超微 | 新聞直接提及 | -0.50 | N/A | N/A | 557.89 | 557.89 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2303 聯電 | 產業/供應鏈推估 | -0.04 | -0.90% | -0.60% | 156.00 | 164.50 | -5.17% | 未明確 | 4.00 | 39.20 | 23.12B TWD / 22.85% | 2026-07-01 |
| NVDA 輝達 | 產業/供應鏈推估 | -0.03 | -0.09% | +20.96% | 210.96 | 211.14 | -0.09% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | -0.04 | N/A | N/A | 979.30 | 991.64 | -1.24% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | -0.02 | +18.43% | +9.79% | 1,915.92 | 2,335.00 | -17.95% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -10.48% | +29.23% | 399.97 | 446.77 | -10.48% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel、INTC」，共 3 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「Taiwan Semiconductor」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip, foundry。 方向判斷命中詞：falls。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel and Applied Materials Dive 10%, AMD Craters 8% as Samsung Earnings Trigger Chip Selloff - AOL.com](https://news.google.com/rss/articles/CBMigAFBVV95cUxQTEZlSzlmUHNBNDU4ckRBX0FhenNQQ1dYQTU0RWVZeVcwblFWZkVycTN0VnJ6MC1VQlZweW9EUWh1bWpmM0taSkJwaXFCR2ZZa3NkamNxY0ZvVE1UZEdFSTM3N2hwRGxUZ1ZPdEdib1NSUmR1TmN0T21BZzYxZ3ZjZQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 10 Jul 2026 09:45:35 GMT
- [Taiwan Semiconductor Is a No-Brainer Buy Before July 16 Earnings. Here’s Why - 24/7 Wall St.](https://news.google.com/rss/articles/CBMixwFBVV95cUxNeVB1dWlwS3hhSmtPTHFyZnJnLTlpbm5pTEw5cHhfTW5kcEdsa0ExeXNKLUhIb0ZndUNVXzl6eWlLQ3RxNFJSLXFnc0hkUGJTU01Yb09kR1VxOXNhRkdlUmFUTEdEWjFKTU1SLUF6U2Z3RE56WjkyRG1pVHMzS0ZPbmNFbUs3TUR4cGY1OVI5Wk9YM2lQVjdTU3dUZ1hscVE5YndjV2ViM2t0ZUZFMzNzWE16WFJaNEZjVEdraTZNWU5XRmh5WGZV?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 10 Jul 2026 12:30:30 GMT
- [Intel Stock And Other AI Semiconductor Names Retail Investors Are Watching - simplywall.st](https://news.google.com/rss/articles/CBMi2wFBVV95cUxOR01WUG5oWGdDdkw2eFFQeUJYMkc2QUY4Z1J0RGFrM3UtSEY4aG1yd1oxdzZHT3pJNUFoaHEwa2pzRE9XbWZQblV4QzlrczNHRDc1MWFEYjVOQ2ZIY1hrY2lhMFJCcThtOUJEcFRQVDRFR3BGcDBVN1dva2Fyb1IxVE91VEdvYlpkaUhuOThvWXNXbkQwOTM0cXBLclh3MHI4N0VBSFIzTnh4aWRsZEVmamczY000SGJKMzhQbVNzaXhRZ3NGalhfVk9LZURUb05tS1JudTBDbkJLNU3SAeABQVVfeXFMTVN6am1OYWdJcVVvT1A0ZkV3OV9tLUdFTUxmcVZJSml2eVB6MDZPR2prU3luaUxvVDJUbkR2Y2I4ZG40OGthRDFWcnZvbTMtRjBCaHU4Tjd0VWItUlJBYlA1WndlTjk5Y1FpZklEblVROTI0QjJoTlAtVjBXVHZiaEUwdWZCRVk3WWJaalgtY1NzZkFPbDNVVTUzb0wtS2hscnFraFNaVndPWXdCWG1oaUk2T3JzbkNzSWU3UVNXUnNMei1fdWJJbzlDdHRMTmpsWFg0bTdzSU1xOHFpWHNydFI?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 10 Jul 2026 06:35:37 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：台股交易制度迎變革金管會促券商三面向強化系統- 新聞 - MoneyDJ；‧永豐期貨盤後分析 - MoneyDJ；產業評析-謝金河：台股高檔遇亂流－重新檢視基本面，調整持股 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股交易制度迎變革金管會促券商三面向強化系統- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNMmE4cDVqWFN0dFNUVlhyZXN0UVdOVFJydnBnbERBY2d5bTlreTFGOGtYVVozUVNmbzROV0FBdlBxYTlYYkFfNUNrRjhEdFhlVWlxMkdkM255M3BVTFFnMndCR3RhUmowSXpjWC1MSGwxdW80TTBMcVowQVVITW1naW1QSnhyeDZ5QzZWWnJ1dEVJdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 09 Jul 2026 20:39:00 GMT
- [‧永豐期貨盤後分析 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxNekk5QjZoODRaOUhreElOckpBYVlvcXFKWjJLbFFWQWY4bkJFdFdtU1VXbi1JOFRfcE1GOTNSWTYtbXZ6WlpCLWNmWm1WMEhIQ0k2RHJqdmFYMzE4blk5eldXcENqcXZoX3Q3RjdNWElUV3hNa01NWjZFUEp2bXh5YWZ1WHlmWGJac2tOSG5VZnM?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 09 Jul 2026 18:59:19 GMT
- [產業評析-謝金河：台股高檔遇亂流－重新檢視基本面，調整持股 - MoneyDJ](https://news.google.com/rss/articles/CBMijgFBVV95cUxPd3JEUGx1c3NMRzJWNDNIaWV2VnhxYkZwRFd2ZFNyQVNUekhmdlBCRnNKWGJheUtVS1FUTTluSlB1SThzLUtMOHppUi1PZHpvSk9jelktNV8teVJ1VVdjelROREUtd29xTzlQOWc3ZFhfTU9CN0tmRHdyNW5mN2VuOFhBV2RIcGRycVA1QzZB?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 09 Jul 2026 16:12:36 GMT

## 新興題材：台積將法說

摘要：新興題材：台積將法說 相關新聞集中在：台積將法說 牽動台股三劇本 樂觀情境下可望帶動大盤挑戰50K - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台積將法說 牽動台股三劇本 樂觀情境下可望帶動大盤挑戰50K - 經濟日報](https://news.google.com/rss/articles/CBMieEFVX3lxTE1aclIza1U4SlRuTzJqWGtXRHU4eTBEcmtqaHNMZnJoMmN0LVY3X1VXUEptM08xSXRobWFUalpHdUtUQ1dwcmhIc2pydkVNaTBFaDZobmlDZjZIZmVPeGY2eTU0UkNNTVEwdkNfX0U2a1pRME1seWpsbtIBX0FVX3lxTE1NaWJpaGVELTk3eGhKTnRfWGtyOHg4TllLYndHTzd5cjJmN3poVEtBNDBYTkFtZWJka3ZQdWEyOHpodzZSSmZkVTNRWWtNTWdCcGtXRVdjamlFZlV4eDRN?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 10 Jul 2026 18:15:25 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
