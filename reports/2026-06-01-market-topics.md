# 每日股市熱門話題分析 - 2026-06-01

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜中性｜熱度 7｜市場確認 N/A｜同向 0/0
2. **利率與成長股估值**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0
3. **半導體與晶片供應鏈**｜中性｜熱度 7｜市場確認 N/A｜同向 0/0
4. **散熱與液冷供應鏈**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0
5. **新興題材：在台AI超級電腦產能**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.92（樣本 6）
- 5日相關係數：-0.72（樣本 6）
- 同向比例：1/6

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：在台AI超級電腦產能 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 0.00 | 1/6 | 4 | -10.29% | -11.35% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：SoftBank | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-05-19 | 0.04 | -0.01 | +62.50% | 8 |
| 2026-05-20 | 0.36 | 0.35 | +28.57% | 7 |
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

## 歷史回測摘要

- 回測日期：2026-06-01
- 近5日 3日相關：-0.52
- 近5日 5日相關：-0.36
- 同向比例：+16.67%
- 權重狀態：未調整

- 方向準確度：+16.67%
- 信心排序準確度：-0.52
- 診斷：方向與信心皆需修正

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

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Are Micron and Sandisk Stocks in a Bubble? - The Motley Fool；Not Just Micron: Memory Melt-Up Pulls SanDisk Up 8%, Western Digital Up 10% - AOL.com；A Billionaire Investor Just Increased His Exposure to Memory Makers Sandisk and Micron. Should Investors Buy the Stocks? - AOL.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 971.00 | 971.00 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | +6.63% | +9.90% | 1,694.98 | 1,694.98 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +21.07% | +10.47% | 211.14 | 211.14 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 4 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Are Micron and Sandisk Stocks in a Bubble? - The Motley Fool](https://news.google.com/rss/articles/CBMijAFBVV95cUxNN0FnT1JEbU5Xa3BGRVJJWUdLa0xReEpzam1YdWVuZTNzNXFraU91OXNPdDJNRWRxRFpnal9QeVJoSWkzZ1g2blVxUE5YSTRoTUFqT3o3T3dsS0VPSlA0Si1TUmZkcE83ODZBUjRkbHREZ0tXVmxLU1pLd1RTLXN2eWRXajFSbzhQMFNGQg?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 31 May 2026 13:08:00 GMT
- [Not Just Micron: Memory Melt-Up Pulls SanDisk Up 8%, Western Digital Up 10% - AOL.com](https://news.google.com/rss/articles/CBMie0FVX3lxTE5FeHdrVTdzRy1BdXYyS3ltaHFPWGotNzlPaG9hOTBNZTdDUkZtS0ZTem16cjhhcHZ1N1Z0V1lNR0VkRlU5RmEzYXJEZjFhaGJDdlNSbHhRNlIybWFCYjJwQUU5MG9oNm00R2lTaFJ4WVNNM29QYXg3bThJNA?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 30 May 2026 21:22:26 GMT
- [A Billionaire Investor Just Increased His Exposure to Memory Makers Sandisk and Micron. Should Investors Buy the Stocks? - AOL.com](https://news.google.com/rss/articles/CBMikgFBVV95cUxNZVdtTWhPRTB5UU9IdFdmQ2FUSFBQVTRjakVzVUJxUnZuMmpSeENoNnFlcGFhaG0zMWxwS3RqVHl6SlJTLVpoT2lsUUZoejVrM0R2eU1QV011bmZyTFZRS0VxWm42NG9WYWZJeGNvTUJncHhSdWtjN2x1U0dYZHBkN3dQVjVOZ3hES2VnRTYyYThJUQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 30 May 2026 19:42:47 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：台股周線連二紅 直逼45K 法人：通膨未降溫 市場已經沒人在意風險 - 經濟日報；Intel’s Role In Edgecore Open Fabric Raises AI Promise And Valuation Questions - simplywall.st；童子賢：股市過熱要看本益比台股還沒有過熱| 產經 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 114.68 | 114.68 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | -8.49% | -2.20% | 450.24 | 506.69 | -11.14% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [台股周線連二紅 直逼45K 法人：通膨未降溫 市場已經沒人在意風險 - 經濟日報](https://news.google.com/rss/articles/CBMie0FVX3lxTFA3YTUwQzVrZ1Fta1R1cDJFQnFaTEgybmZ6WUpFcmhOXzY3ZmQ0eGFHZnZXaVEzMkxYX3ZKNUl4NWlWWkZXQWRlVmdqRzhHajhjMzNLT244R1BWMUpzUi1oRHYwZW0xTW9NbUFWMGlLOUh5SF9ZelBBdm1Xd9IBX0FVX3lxTE4tTUlhZjc5c1JLRG9BNHVuRjdTZnBQZlRkRGJHVmdXc1pNYjB5cVBvcXFwWjBtSm1WM1ZhZmVUUDhFUWJxZFRScnhILVhSTGVKT3R0YUtmN2NPeWlBS0pj?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 31 May 2026 05:08:55 GMT
- [Intel’s Role In Edgecore Open Fabric Raises AI Promise And Valuation Questions - simplywall.st](https://news.google.com/rss/articles/CBMiygFBVV95cUxOUjFpMlJPcmVILURjTUFaTy1yY1drR2ZGd0pjdjFvRzRKZVpodWZQT0ItcFg3YnhaZ3FhSlhFd3pKQVBwYVdEM19GeGF3dzhnMlptdnJOLTZyNHlzZmhuai1WLTJsRlVSNGUwUzY1NFFWdnJOamdiZnhpVzE2WUxpWTVSTWtmTUl1U3hMTjJ2emNFMThvM2NsY3JLVS1USGFaY2VwRnBsUG1kcHdWNWlycW5QWk5qSmZfa3p5YkltazhYcUtrS0tsQ3BR0gHPAUFVX3lxTE9ZVjhVUW0xS3lfWDlUd3p6dldYU3VtT2h4bTJLeDh5ME8taXJrZUFtd1ZJWXM5VFF0R2V6LTBGcmF5NkVLVFcyVUtGb2J0ZFMtVnN5Ql8zWDJ1Rnc5QzlOQnNOV1dNM28tUjNrR184NV9jRmNVVGZfcHA4TTg5U25LZldBMUJRZlBOWm5oVnZqLXN3NHhrWlFBdnl5YkZHRTN0bXQ4MFR1ZmpJT2tVLWxGc0p4eFVQVC0tV3ZCM0p1ZFdtckFZYzhsSUdwOUg4cw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 31 May 2026 18:10:56 GMT
- [童子賢：股市過熱要看本益比台股還沒有過熱| 產經 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE5GaVctQXJBYjFNdmx1dXo5RVNDb2hoaDA3ZW1ZUE1XeHlpVXBqcWdiZVI5ZjRUbjE0ZlNvRE1aUVlVQ1NZRjgwM2kzN2tpY1lSQklGMnNSdXEyRDZUemc?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 30 May 2026 02:14:00 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：德國新創發展石墨烯半導體 預計量產需約3年 - 中央社 CNA；不只半導體吃紅利！輝達帶旺代工二哥和碩、廣達等組裝廠大翻身- 日報 - 工商時報；加速擺脫對美依賴，傳字節跳動擬自研 CPU 晶片 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +21.07% | +10.47% | 211.14 | 211.14 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 114.68 | 114.68 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +3.74% | +4.43% | 2,355.00 | 2,355.00 | 0.00% | 不適用 | 74.39 | 31.66 | 410.73B TWD / 17.50% | 2026-05-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +10.73% | +26.75% | 144.50 | 144.50 | 0.00% | 不適用 | 4.00 | 36.31 | 22.66B TWD / 10.80% | 2026-05-01 |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 516.10 | 516.10 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 971.00 | 971.00 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | +6.63% | +9.90% | 1,694.98 | 1,694.98 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | +44.35% | +34.85% | 446.77 | 446.77 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達、NVIDIA」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 CPU, server CPU, x86, foundry；其中 2 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 1 篇新聞出現相關標籤。

### 主要來源

- [德國新創發展石墨烯半導體 預計量產需約3年 - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9FaF9vOGhHMzdRQXpGUm9rbzhySGJSUXp1TGdWakJiZUZhQU5WNkhsUTNncy1iN1RSZG9UQkNsT2JhZnI3aVBieHVzX09SMWdjQXBYaDFzNFBRRldPenlF?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 31 May 2026 12:42:00 GMT
- [不只半導體吃紅利！輝達帶旺代工二哥和碩、廣達等組裝廠大翻身- 日報 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9sbW1BSWJwOFNpZTluTUZZXzBQNlo0cmZ2QW1EaV9aNDVneXZhVzU5V3VEeE00V2VjQWJwdlFvbVowWWZaVjBvWDhuaVRkMUh5cHF0ellqTUdOSDM4ZFdN?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 30 May 2026 19:00:00 GMT
- [加速擺脫對美依賴，傳字節跳動擬自研 CPU 晶片 - TechNews 科技新報](https://news.google.com/rss/articles/CBMickFVX3lxTE5veGNrVDFCamlGbmFQV0c2QnoyUUZxS2VDeHZJR1BPaGpNTEJTd3FrLWdlQWVkWkRCV2lvckJiSnhKeENYWUJ3TFJyTVNWTXBIakl5cmNSZmxkT3EwX2xTc0hlNlh5N2J3Znd2eGNWOXk5UQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 31 May 2026 06:32:00 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：Micron Joins '$1 Trillion Club'. AI Chip Trade Has No Signs of Cooling Down. What's Next? - Moomoo

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 971.00 | 971.00 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 3017 奇鋐 | 產業/供應鏈推估 | 0.00 | -2.20% | +4.72% | 2,665.00 | 2,835.00 | -6.00% | 不適用 | 61.06 | 43.79 | 15.63B TWD / 71.62% | 2026-05-01 |

關聯理由（前 3）：
- MU：新聞直接提及「Micron」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 3017：產業/供應鏈推估：公司標籤符合「散熱與液冷供應鏈」關鍵字 thermal；其中 0 篇新聞出現相關標籤。

### 主要來源

- [Micron Joins '$1 Trillion Club'. AI Chip Trade Has No Signs of Cooling Down. What's Next? - Moomoo](https://news.google.com/rss/articles/CBMi3wJBVV95cUxPaFNzbV9ZWFk3STJJZWpibkZ6alIyVzJWeXV5Y1RXLWQyNUUweUZLb3FSTmdLZUNBZWcxcjFRQngtdjBsU0EyUFhCbm9GV0RXNkFrQ2RiR0JiRDloUDdIMkMza0g1UlBQWGNPUEVvVEY2cWUyR3B3LTVqQ3pNOW1Vd1RqZVN2Vms0Ti1fbnczWUY2Z0QzeUd2OGhGdkVDc05hYW1CNFRNQmIyYlBlY2pObDVXb3o1U2JsaWQtSWFtOFdzeG1YeThpQ3ZjTVdiLXFtek9OSWI4VXVYS0cxa3AyZENRRjB1ZXJrN2ZYdjNJU1JzVlA0WXZJejJMb3JBX3RUaFhGWTJqS1VtMWtRYmxIMGNTcWQzQkVSTjlVOXV5UUZ0clo4ZXR2eGZmRXZuNy1hN0VCVS1XLWctbWlDNmpLYnVXQU5DeHBhYWg1UkY1OWJSRjdPQ21xV2dNaGd0aFE?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 31 May 2026 10:40:59 GMT

## 新興題材：在台AI超級電腦產能

摘要：新興題材：在台AI超級電腦產能 相關新聞集中在：「輝達背板股」誰新上榜？黃仁勳：在台AI超級電腦產能倍增 - 遠見雜誌

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +21.07% | +10.47% | 211.14 | 211.14 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [「輝達背板股」誰新上榜？黃仁勳：在台AI超級電腦產能倍增 - 遠見雜誌](https://news.google.com/rss/articles/CBMiTkFVX3lxTFA4bXN1d3ZSMlFLaGdORTk2UTlpTWk4UTRnQnZrYWlGc3dmOUNDdUhoYUhpTkZIYnRhZVdnZTRTYmhBQjdFMExTbVUxbnJxZw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 31 May 2026 04:05:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Week Ahead | Focus on COMPUTEX: AI giants NVIDIA, Intel, and AMD take the stage in succession; U.S. May ADP and non-farm payroll data arrive; Meituan and Broadcom to report earnings - 富途牛牛；加速擺脫對美依賴，傳字節跳動擬自研 CPU 晶片 - TechNews 科技新報；博通端多款 Wi-Fi 8 新品，推業界首款端到端 50G PON 邊緣 AI 產品組合 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AVGO 博通 | 新聞直接提及 | -0.38 | +44.35% | +34.85% | 446.77 | 446.77 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | -0.36 | +21.07% | +10.47% | 211.14 | 211.14 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | -0.72 | N/A | N/A | 114.68 | 114.68 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.70 | N/A | N/A | 516.10 | 516.10 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.04 | +3.74% | +4.43% | 2,355.00 | 2,355.00 | 0.00% | 背離 | 74.39 | 31.66 | 410.73B TWD / 17.50% | 2026-05-01 |
| MSFT 微軟 | 產業/供應鏈推估 | -0.05 | -8.49% | -2.20% | 450.24 | 506.69 | -11.14% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.04 | 0.00% | +8.91% | 611.00 | 611.00 | 0.00% | 未明確 | 10.86 | 56.73 | 62.25B TWD / 19.22% | 2026-05-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.03 | +1.06% | +11.66% | 4,310.00 | 4,310.00 | 0.00% | 背離 | 62.91 | 68.69 | 46.74B TWD / -4.14% | 2026-05-01 |

關聯理由（前 3）：
- AVGO：新聞直接提及「Broadcom、博通」，共 2 篇新聞命中。 同時符合主題標籤：AI, datacenter。 方向判斷命中詞：衝擊。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。 方向判斷命中詞：衝擊。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：衝擊。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Week Ahead | Focus on COMPUTEX: AI giants NVIDIA, Intel, and AMD take the stage in succession; U.S. May ADP and non-farm payroll data arrive; Meituan and Broadcom to report earnings - 富途牛牛](https://news.google.com/rss/articles/CBMinAFBVV95cUxNcGtwRFlnbTdjQmFUYjlvWkkyQ1JBT1NOcXBIbWs2UWpWMjFzcHhWMDF6UDJrcXhHX2xtQUt4Uk1KS1lsem1EcEYwZFpfRG91dmE5bGpma2g2NlMyOXlhQ2pUWS1PbU51SG5GdmxITzZfSkNIbmlsTTcyNHZpUlZjTHpuZWZEelZmc180aWZqZnpjRFJ5TVhaX1F1em8?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 31 May 2026 08:24:00 GMT
- [加速擺脫對美依賴，傳字節跳動擬自研 CPU 晶片 - TechNews 科技新報](https://news.google.com/rss/articles/CBMickFVX3lxTE5veGNrVDFCamlGbmFQV0c2QnoyUUZxS2VDeHZJR1BPaGpNTEJTd3FrLWdlQWVkWkRCV2lvckJiSnhKeENYWUJ3TFJyTVNWTXBIakl5cmNSZmxkT3EwX2xTc0hlNlh5N2J3Znd2eGNWOXk5UQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 31 May 2026 06:32:00 GMT
- [博通端多款 Wi-Fi 8 新品，推業界首款端到端 50G PON 邊緣 AI 產品組合 - TechNews 科技新報](https://news.google.com/rss/articles/CBMikwFBVV95cUxOamVZcUtiQ0NNc1NQd0VWYV9RUUJRc1dIWHRya3luTmVfSk5QRDU2ZlZwbHBXaXYxa3l3WG5rWGQ0VFYzRWZGT0RMU1A0NWhkazE5dnZJQkZiaDJBVVRjaV9qVi1oMWNiWXhQMnhoUnNsQzJwNkhtYjFCeUkxSF9Ta0NOSEUtTEwya3h6azZzUF9YNW8?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 31 May 2026 06:57:35 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：法人專欄分析內容-台股 - MoneyDJ理財網；同業股價表現-電子-USB IC-台股 - MoneyDJ理財網；最新專欄分析 - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [法人專欄分析內容-台股 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilgFBVV95cUxNSkFzeVh1blVsZC1HMlVnc3FlSV9rcHl4eDZRQlFJbmpVSVhlMVh3YUE4bUE0NUVoTkZuNXlMQjd6dV9VN3R5WFNaQlhQWXB6Q2FFVXUtYVJpeDBiazcyNFJoYlVmRGVrbXZiMElHLVNYVm9udHlnV195empNcWVScENjdjdROC1TekpqR2hzMmM5b2YxTlE?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 31 May 2026 16:14:56 GMT
- [同業股價表現-電子-USB IC-台股 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMiaEFVX3lxTFBmYndsNVhDRDRmWGVsY3NTSFF3dldCNFY5THRMSjNCeDZJT1JQUWRyaU93eVZTSl90Qi1EVU56dEpOd1VQeVlrMWNMa3gyZEphN3hVbXZZX2h0TmVZQTBsQk5Eal96cWNZ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 31 May 2026 17:43:42 GMT
- [最新專欄分析 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMieEFVX3lxTFBDek9xZlRqNDFzUGpoSm5CM3dnZnIydkh2UEpnR01zbkJ6VlQ3UkQ3LVh2dXBwV3lNa0pDdF9idkJVeXkxdExGZEVWaG9YZngzeWdTRVJMMnpESG9LV0c3dmpyNFZIczBqT2R4c2E4aTlnYmZHV0VhaA?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 31 May 2026 11:21:09 GMT

## 新興題材：SoftBank

摘要：新興題材：SoftBank 相關新聞集中在：SoftBank to build up AI data centres in France with major investment - Reuters；SoftBank plans 75 billion euros of AI investments in France, as Europe struggles to catch up with U.S. and China - CNBC

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [SoftBank to build up AI data centres in France with major investment - Reuters](https://news.google.com/rss/articles/CBMivgFBVV95cUxNSGpvaWFPVFk5eDM4Y1RPY29QVXVhYXN4UHQyVlJ5NzJzUWMxRk90S2EwNVRjeE82MlJWeWhCMjNHN1NPSVQ2UjY5UlBBWHdQSmdKRURxZFF1YkRYVEFFbW03V3pFZ1dKSGxQdEsxVUdkNkxZalIybVhYRjlkSmlfTkZDd1RfaWFLdXFVMTF2VXZBOHlxcTVwQkRQbVNqbXRLYzN1Z1NEZVhhaUZWeXdraUZMVG1wVFVIeDZMRzB3?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 30 May 2026 20:06:26 GMT
- [SoftBank plans 75 billion euros of AI investments in France, as Europe struggles to catch up with U.S. and China - CNBC](https://news.google.com/rss/articles/CBMiqAFBVV95cUxQeGdvazJVU0FLWWxqTjhBWS1CM2IyZThDc29uckwwc0h1US1Cd0NRcWpnLXpUNmpkck5Dc29MQmpxLXk4TDFNWlhUUHQ5YlAzTjk2Q2d0eW5GMVI4V29ZYWdXMjRnWC0zb3Z6NVp2Vll6TDlNV2gtb2tmTXBkQWE3RWFzaGQzczBuTlhhU1I3Z19WcG1hQ2hhYWVIYlFoQm9UWXVxRVVBRErSAa4BQVVfeXFMTTRzWVdjYzFEdTJZME5BSUxDaXBsd2pfLVdVMS12NFljOTFNN2MxS2hJNk95WTFlSnpvTm0tOGY4LTBmSTJXbXNLQk5uNXBidjJLWjZFYklLUW9ldGUwOXROTlM2M01GS2xNU2pHVS15UWs2aWY0b1YzUzdBaU9oelVNTlZYYUNOU2JDR2tFR2gyM3l6YlRVblVoOHhRamRDQnV3R3liVlA2UnQ3Y1l3?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 31 May 2026 07:26:59 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
