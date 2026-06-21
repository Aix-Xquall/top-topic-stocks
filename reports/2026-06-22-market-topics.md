# 每日股市熱門話題分析 - 2026-06-22

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜正向｜熱度 8｜市場確認 94.69｜同向 2/2
2. **綜合市場情緒**｜中性｜熱度 23｜市場確認 N/A｜同向 0/0
3. **新興題材：TradingKey**｜正向｜熱度 2｜市場確認 80.95｜同向 1/1
4. **半導體與晶片供應鏈**｜中性｜熱度 10｜市場確認 N/A｜同向 0/0
5. **利率與成長股估值**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.87（樣本 3）
- 5日相關係數：-0.87（樣本 3）
- 同向比例：3/3

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 94.69 | 2/2 | 0 | +8.23% | +22.25% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：TradingKey | 80.95 | 1/1 | 0 | +3.65% | +16.12% |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：公司於德國地區營收 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
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
| 2026-06-20 | 0.29 | 0.21 | +63.16% | 19 |
| 2026-06-21 | -0.01 | 0.32 | +55.56% | 18 |
| 2026-06-22 | -0.87 | -0.87 | +100.00% | 3 |

## 歷史回測摘要

- 回測日期：2026-06-22
- 近5日 3日相關：0.01
- 近5日 5日相關：0.39
- 同向比例：+57.14%
- 權重狀態：未調整

- 方向準確度：+57.14%
- 信心排序準確度：0.01
- 診斷：低相關

調整原因：近 5 日有效樣本 7 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：台股股東會行情還有戲 AI 景氣展望受關注 美光法說將添助力 | 市場焦點 | 證券 - 經濟日報；Intel stock enters week at record high after Apple chip report, Micron test ahead - TechStock²；SanDisk Corporation Stock (SNDK) Moved Up by 11.54% on Jun 20: Facts Behind the Movement - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.65 | N/A | N/A | 1,133.99 | 1,133.99 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.64 | +3.65% | +16.12% | 2,184.75 | 2,184.75 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.48 | N/A | N/A | 133.99 | 133.99 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 新聞直接提及 | +0.48 | +12.81% | +28.38% | 298.01 | 312.06 | -4.50% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +5.57% | +18.91% | 210.69 | 211.14 | -0.21% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「美光、Micron、memory」，共 3 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：growth, record high。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK、SanDisk」，共 2 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 方向判斷命中詞：record high。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [台股股東會行情還有戲 AI 景氣展望受關注 美光法說將添助力 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxQb2dySWljMU1FN0hQSC11TDlkUUxsdUR5N09qRmwySlk5YURuM0JaRkc0NUt5TGdWTUF2NU9iNjRFSzJpaUUtY013Wl8xWjNkMU15UEVnZWNKeldENTBQd25DVnNzTjVOSm85RkEwNGlHdmVjQzVLRkZOa01uM2dpYg?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 20 Jun 2026 09:00:00 GMT
- [Intel stock enters week at record high after Apple chip report, Micron test ahead - TechStock²](https://news.google.com/rss/articles/CBMiowFBVV95cUxPcjRBeFRnZXJPcWxRUGl1V2YtVkxaQU8tbmlqei02QU0wcG1ZdHozWTBtc3hVdC01ZDR4Z01PT1d5T1ZQaEZKdG5YQkY4d1JwSjU1RVJuRHc1YlNMRXcwZURLWGRkcnYyOUZ5ZlBXb2FudVNrcEJqLUlwNkdNQTNiYjVCcDRPMk5UbE5NbGwwS3dUY0dlbXpJeG5Od3RYYktvQm1N?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 21 Jun 2026 15:36:19 GMT
- [SanDisk Corporation Stock (SNDK) Moved Up by 11.54% on Jun 20: Facts Behind the Movement - TradingKey](https://news.google.com/rss/articles/CBMiiwFBVV95cUxQdUg0ZDZDOE5aUnhrN1BvQWNWN0tUVHlORmNhampRM2J1clNuS0RaQVdSdWZUYmZYNkFQRGd4OEdPLVVUMnU4SzFKcjBBb3NKY0tRbmJZMnB2MFJqUVNpNmIzaFF2bzJaaWhEeDY2QVR0RUYwbm8tU19lYXgwZ1B3ajFiLWl5SGpYQVBR?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 20 Jun 2026 15:15:29 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股行情持續走揚 融資餘額挑戰新高 - 經濟日報；台股多頭氣盛、投信季底作帳 大盤蓄勢衝47K - 經濟日報；櫃買教戰綠色證券認證 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 133.99 | 133.99 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [台股行情持續走揚 融資餘額挑戰新高 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxPQm1VT0diRWVsVC1Md1plOVRyTmRQY0pSMklyekQtWmNWeVNPU2FCNk1sMlZjdExqQUNTVmdaUnltUGFnQ29Da1NXTXd2cmpBMTBUcmQyaHFKSjZSLVVCemJtTDY4LVRuXzdTcEIzR0h3SUwycl9Oa0xvWXlyaDByMNIBX0FVX3lxTE1oMV9kYTlHbm1iUXJBZHZIazVVcWQ4Z2VxeUZYdnNJMnlMb3M2bGw5QnhpRUhXRmhxM2I4XzU0a2U1RFpZamRhSFI0aFZ3MG5XRjF4VEVKRFlvazF6cW9j?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 20 Jun 2026 09:00:00 GMT
- [台股多頭氣盛、投信季底作帳 大盤蓄勢衝47K - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5qNEFfOFdnNkd2MXdHbkY1V0J0VUp5bnJ3bmZvVU8wSVZtZjJxRVhxNUcyLVl5QUxnM2xDY2J5c3NkVHpWZTNQZzlvNFNvMGRQNlBTZHV6alJKUdIBX0FVX3lxTE5YV2lQMHdfdlN5MS1ReDRhVExTMUJyVnFuSUh2Ym93dk1fSjhYTzJEVTBzMWNkZUN3Q0g4U292NldWM3RyUG1ITF9NZXk1V21IM2hlcVZkamlDMGFRcU1r?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 21 Jun 2026 17:31:40 GMT
- [櫃買教戰綠色證券認證 - 經濟日報](https://news.google.com/rss/articles/CBMiggFBVV95cUxQQ21UelFtRURzaXljdWhDRHhOa0hYLWtHQUNQMTNFaWFLU2YzUTZWVWZtaTFiT3JpMHlqNEx2c2VUVF84SVpDYU1YV0hBc0xYMWZXQ3VxejkwQmtNZlNDSDhtamNPR0wzaXVXOGZKTGdBbURGTk1OVjgydjg1Z1ZqSF9B0gFgQVVfeXFMT0k2VXlud0lGanJaNjVrSHBURi1qdmtUbmUwZV93dkFLMVFtYS1SYXlLOExfSjlkVG5qaXRqSzlid0lDQUtXMjhrRkNZMlRNb3NhOFBtLWRUQ3VZRm5WcHdf?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 21 Jun 2026 15:47:08 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：SanDisk Corporation Stock (SNDK) Moved Up by 11.54% on Jun 20: Facts Behind the Movement - TradingKey；2026 Global Top Seven Memory Giants Ranking: Kioxia, SanDisk Lead Growth, Who Is Strongest in the AI Memory Supercycle? - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| SNDK SanDisk | 新聞直接提及 | +0.56 | +3.65% | +16.12% | 2,184.75 | 2,184.75 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 新聞直接提及 | +0.48 | N/A | N/A | 1,133.99 | 1,133.99 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- SNDK：新聞直接提及「SNDK、SanDisk」，共 2 篇新聞命中。 方向判斷命中詞：growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- MU：新聞直接提及「memory」，共 1 篇新聞命中。 方向判斷命中詞：growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [SanDisk Corporation Stock (SNDK) Moved Up by 11.54% on Jun 20: Facts Behind the Movement - TradingKey](https://news.google.com/rss/articles/CBMiiwFBVV95cUxQdUg0ZDZDOE5aUnhrN1BvQWNWN0tUVHlORmNhampRM2J1clNuS0RaQVdSdWZUYmZYNkFQRGd4OEdPLVVUMnU4SzFKcjBBb3NKY0tRbmJZMnB2MFJqUVNpNmIzaFF2bzJaaWhEeDY2QVR0RUYwbm8tU19lYXgwZ1B3ajFiLWl5SGpYQVBR?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 20 Jun 2026 15:15:29 GMT
- [2026 Global Top Seven Memory Giants Ranking: Kioxia, SanDisk Lead Growth, Who Is Strongest in the AI Memory Supercycle? - TradingKey](https://news.google.com/rss/articles/CBMirwFBVV95cUxPbElxTEtyRVJKeGtuQjFmb2p2V0c5TEo5XzVXbEcySExfb2dmeG4zRkpEUVpuMkhjcHh4azAxTlVSQUxYc1pMemlvcjhWMHhDeGRqajFUSUNLc3U5QlNYVVFCdnZPMWZzSV9XcHp5WnIwbDZDN3lpWkFMT1p6bGtvUGs2aTFEMHFyb3lPU1ZYQkZ1WjNJdGt6aTNxcFRrMzZHNGxydEdFY2VNQ2lHM1dr?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 20 Jun 2026 09:06:54 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Nvidia and Intel Rallied Too Much, Broadcom Is the AI Chip Bargain Investors Need - NAI500；台積電全額資助熊本大學設新獎學金培育半導體人才| 國際 - 中央社 CNA；日衛浴大廠TOTO砸157億搶攻1奈米半導體零組件市場| 產經 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 133.99 | 133.99 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | 0.00 | +1.47% | +7.11% | 2,410.00 | 2,410.00 | 0.00% | 不適用 | 74.39 | N/A | 416.98B TWD / 30.09% | 2026-06-01 |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +5.57% | +18.91% | 210.69 | 211.14 | -0.21% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | 0.00 | -1.46% | +28.73% | 411.35 | 446.77 | -7.93% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +2.83% | +16.40% | 145.50 | 145.50 | 0.00% | 不適用 | 4.00 | N/A | 22.94B TWD / 17.78% | 2026-06-01 |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 537.37 | 537.37 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 1,133.99 | 1,133.99 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | +3.65% | +16.12% | 2,184.75 | 2,184.75 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip, foundry。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Nvidia and Intel Rallied Too Much, Broadcom Is the AI Chip Bargain Investors Need - NAI500](https://news.google.com/rss/articles/CBMiswFBVV95cUxQMGpvWWFXaEpyNHMwV3BGT2lKMDUyVmVSLWR6Q0NTN2dBNi01ZURlOGVNWVo4d0dTTFZ5eUZ4c0RmelM4eXRXVFNOcmc4elJwcDJ6b2pSZElpWVFXeWZmRVd4OWdiWUktRndLckNvUHVaLXphM24xOGdOSWVkbDFUb1hvOFJoV2c2WXVpVDJEZVdwTkxtc0tXU3ZfaTJZMGpOemJEOHpYTS11QTJNdDQyOTlBaw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 20 Jun 2026 01:27:47 GMT
- [台積電全額資助熊本大學設新獎學金培育半導體人才| 國際 - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1TdEpGVi1XSW43MWhSVUhoUldKdGhWdmZiOTJocjdxM3czaEJnSE1xdTdya0hVSS1QZFFqMWVFTmNYajZhWEhteTROckdmT3BOMVRUeERtenp4NG56Ujc4?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 21 Jun 2026 08:28:00 GMT
- [日衛浴大廠TOTO砸157億搶攻1奈米半導體零組件市場| 產經 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1QQkV1NDgxMTg2X3NsNUF3c2ZmRTMtQUZmcXp5ak9BTldKMHRKdEcxLTR6T1NFbVdCcGVuUnlyamd6QWF4eC0tTW9sVkQzYS15dE5XNkNORUlMVTFMZGc?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 21 Jun 2026 09:59:00 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：台股周線翻紅 法人：華許放鷹只是煙霧彈 通膨回落有機會開啟鷹式降息 - 經濟日報；3 US AI Stocks With Valuation Risks And Earnings Growth - simplywall.st；美股泡沫要破了？估值超越「1929經濟大恐慌」 - Yahoo股市

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | -3.40% | -25.12% | 379.40 | 506.69 | -25.12% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [台股周線翻紅 法人：華許放鷹只是煙霧彈 通膨回落有機會開啟鷹式降息 - 經濟日報](https://news.google.com/rss/articles/CBMid0FVX3lxTE1xbjZCa0ZIRFpvVTI2dEI4aFFsNkwzNUNnTkhnVnZfSFhlV2huV2tIMk1JTFhtR0E2YmR6eUVCQks1dlZQRXE2T1FDSkRQZk1xLXplRTRzUGFiYS12VFo0TmRKU0xyR2RFdENMQlptX2xpUGdrRDk40gFfQVVfeXFMTlFEeElrSW96Rk1qMzZOc05RNlhXR2k2dmVLQVd1amhmYWR3ZXAtZUkwU3pOZnV6Q2czaFNYRk1Fa1FQX1FDaDZRS2pEWm5abXpRUVJjWjJ2UDBoeUs2cEk?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 21 Jun 2026 04:22:58 GMT
- [3 US AI Stocks With Valuation Risks And Earnings Growth - simplywall.st](https://news.google.com/rss/articles/CBMiywFBVV95cUxObVEwTHo0bjlIMW5USmE2MDIzQWZWT2FtbThOZXQ4aWF2bmZYbDVJNERmM1g0NVpGRm1uc1dPR2FJWlVVZm9iSEhSUzJRU0pIVklvc0drZEZIYy1lNWt4Y1dXS2h0Tms1NHRfb2lfcmZJUjhnUjM0TVpQV2lKa2hBVlRIQ09YWnRScTdSZ1J4Y3Q3bEpaeUl4TzdneHZVU1FDaks0eUNtelFWSWVwSUpaMGZpUVp0ejd0X0lUYlUzdWpfdGZYWUJPeGw4UdIB0AFBVV95cUxPLWJkOUNFRW1vbHhDQ3lQZEYyanpJYU1ZbWlvdlFoX0pfcUZWRGdxVzVxYWJuMC1OelZ0dE5DclNCZHFVanFFSy01UjNmek1NZno4Nmd4Qzl5S2p6b1Q5eVVhNWpEM3Joa2xyS3ZUdUJrRXBWakxOT0p4b1RIYWtIQ1I0X29GenQ2RXFtMl9jSHJjSUNibFVRS013dlBQX0hrUU1mZWI2cWxOM2FTUk5hQTh1OGNHZXdYTThkb0Rod2xiSnAxS082MzFfSWtuUkZI?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 21 Jun 2026 11:38:03 GMT
- [美股泡沫要破了？估值超越「1929經濟大恐慌」 - Yahoo股市](https://news.google.com/rss/articles/CBMiowJBVV95cUxPVER3ckZxQjFDbmFFMXJnWEhXaG1SNVJjZHJVRDlqS0JNbVY0RmFrMUpOZTAzcm1wbW9ScW1qVk54NFhyMGJ3Ul9uYjJGajlDaGFlc1FTZ3RqbFFfR0VPdFUwNEpDN051bUJlNmVUaEFtNzAxYnBBLTh3M25ucjl4ZGtYNGEtZ2VIeUNTWG4zbUlQeEUyMmdrOEI1Z2Z6Z0xYSlgxUFdueTVxMGhvMVpwQW50QVJ1T2RvejhIUjkyUkNaRVUyREI4aF84SnEwQkVpbmctQXlfNDZIT0J3VXUzN0d1dG5GbElUTFFuQW5sOGV4VnNvWjlTZ0RocXF3bDFQc3A1SnZHdi1xWTI2T1lRdWpicW43enVSZ2VHWF9tXzctQUk?oc=5) - Google News source discovery | Yahoo 奇摩股市 Sat, 20 Jun 2026 01:51:11 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Nvidia and Intel Rallied Too Much, Broadcom Is the AI Chip Bargain Investors Need - NAI500；42 奈米閘極間距對 AI 晶片效能提升有何具體貢獻？ - TechNews 科技新報；AI 誤判年齡，Meta 審核機制如何兼顧精準度？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +5.57% | +18.91% | 210.69 | 211.14 | -0.21% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 133.99 | 133.99 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | 0.00 | -1.46% | +28.73% | 411.35 | 446.77 | -7.93% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 537.37 | 537.37 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +1.47% | +7.11% | 2,410.00 | 2,410.00 | 0.00% | 不適用 | 74.39 | N/A | 416.98B TWD / 30.09% | 2026-06-01 |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | -3.40% | -25.12% | 379.40 | 506.69 | -25.12% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | +3.90% | +12.68% | 613.00 | 613.00 | 0.00% | 不適用 | 10.86 | N/A | 63.03B TWD / 28.57% | 2026-06-01 |
| 2454 聯發科 | 產業/供應鏈推估 | 0.00 | -1.79% | +7.47% | 4,390.00 | 4,390.00 | 0.00% | 不適用 | 62.91 | N/A | 47.43B TWD / 4.99% | 2026-06-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AVGO：新聞直接提及「Broadcom」，共 1 篇新聞命中。 同時符合主題標籤：AI, datacenter。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Nvidia and Intel Rallied Too Much, Broadcom Is the AI Chip Bargain Investors Need - NAI500](https://news.google.com/rss/articles/CBMiswFBVV95cUxQMGpvWWFXaEpyNHMwV3BGT2lKMDUyVmVSLWR6Q0NTN2dBNi01ZURlOGVNWVo4d0dTTFZ5eUZ4c0RmelM4eXRXVFNOcmc4elJwcDJ6b2pSZElpWVFXeWZmRVd4OWdiWUktRndLckNvUHVaLXphM24xOGdOSWVkbDFUb1hvOFJoV2c2WXVpVDJEZVdwTkxtc0tXU3ZfaTJZMGpOemJEOHpYTS11QTJNdDQyOTlBaw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 20 Jun 2026 01:27:47 GMT
- [42 奈米閘極間距對 AI 晶片效能提升有何具體貢獻？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMib0FVX3lxTE91V2FWenFqQTU4ci03amwycXVZbUVkcWlDeGJqQ0M5NG1QbUozcElRUXpBcEUtWXM5LVBLaFdiaEctNkR6UDJQai11RzJmb2Iwa05CTmNxTU1UZjBZXzNVcFdWVUhXYkt1V3ZjMFpaWQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 21 Jun 2026 20:01:42 GMT
- [AI 誤判年齡，Meta 審核機制如何兼顧精準度？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMivgFBVV95cUxQMkZ3M0ZPSk1xYUVSMTc3dzd1azVjOFg5N1pTZ08wVkVKT1JCaHhHbEFxTk5aVlRRb240aDlhWjM4TUNNWm9nUXcwZGhDcFkwcU9vSF9IRlhfZnJ5YzlRRjVsRkx0T2lWSkdDdVNSWWsweHZxTE1nN1dNb2Q4Um5UYWQ5VEFubGs2a0FCNnRlLXdaSVJRMFRxV3RFcDJFeHR3d1RzWFBVeENLVDNPeXhuY09hOHFTcWJaOWhGU1lR?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 21 Jun 2026 13:08:24 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：法人專欄分析內容-台股 - MoneyDJ；華南永昌-斗六 對 歐格(3002)個股 單一券商歷史明細 - MoneyDJ；力新 公告本公司財務主管發生異動 - 台股 - 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [法人專欄分析內容-台股 - MoneyDJ](https://news.google.com/rss/articles/CBMilgFBVV95cUxPSnlqYW9KUTg3TU1jOThzQm5vdHVZTWJJdjY2d0NPM1VRVWtDVFpNUmkzOTBhQWI0MHBoS1ZXaFI4UldrQWtMZmNZSDI3bnR1UlM1d0tIMzJla0h6cjhFUkV1NmdBR0xVdkJiVVBPckRtUy1JNzdiYkhpVzVEbnFYelYyamJtMzMyWGFVVGRoOElmcE5aX2c?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 21 Jun 2026 16:16:19 GMT
- [華南永昌-斗六 對 歐格(3002)個股 單一券商歷史明細 - MoneyDJ](https://news.google.com/rss/articles/CBMigwFBVV95cUxNalNaTTdpVDBhOV90TmNTYm1OXzNMTTNoUUE2TXd0a1Y4aE9HcEl6TTlvaWNuMUtod3pCUnlsWWs1a3VQOHVwbXltNkpEMHlRdDVOSWpsLWJIbHRXeXFHd2w5aEpDT1JpcWhGaXJSSmhIOXhQYl9LdTQxWDZLVWtTYWVPYw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 20 Jun 2026 08:21:36 GMT
- [力新 公告本公司財務主管發生異動 - 台股 - 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMiggFBVV95cUxNalpuanlHb0QyczQ2MmN5eU1idGVFMm1MRVZDaXI4bkNIOVJ3STBCUndoeEJrNlh6QWxuMEJoclIwNFNkaXczb2F1ZGZ0TUZlTWwwLXgwTXFwdEUzLWtqTEFudmt1eGpjcXk1ckNCNjJYQ0F6aS13NGdTVHlBLThiTExB?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 21 Jun 2026 02:11:00 GMT

## 新興題材：公司於德國地區營收

摘要：新興題材：公司於德國地區營收 相關新聞集中在：中磊：公司於德國地區營收比重甚低，華為技術提訟案估影響極為有限 - Yahoo股市；中磊：公司於德國地區營收比重甚低，華為技術提訟案估影響極為有限- 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [中磊：公司於德國地區營收比重甚低，華為技術提訟案估影響極為有限 - Yahoo股市](https://news.google.com/rss/articles/CBMiugNBVV95cUxQOXdLTjdBRGtSUjhBTDI2MTkwZmZYOFhJbnJhRmFTNzY5Si1ocU9uWmFfQno4WmxwRjlnUTNWdlNIYWsxWkN4cmVkUEN0dzV2b1ZJbG9mZk01YUp2R0VaMEFuOGp5V1FTSVk5emdpU2lpbHExRWVRa0lnX09FUGVwbm5UMWhxSmxTaXkzU2dzTUExNXJERFBtVFVQOVhzbFNBV1R4YlVpODBhbUJKTlY4b18tejVLb0Y2ZTZYRjRwNVNQTnZmbS1oaUJSNWFXZ21qYk8zdnhNaV8weUdaU0xmWVVRZV9qRTNfSkRsOXhWRnFReFNNeVJnMjg5OFdJbjAzZ3hudjBsMk5ueV93WXB3MGhlakM3ZEVHZGRHZnVXSWVZWHBpMFhIcU1FUjhsWWtBNk5BZVR5NVJNUkphQVJBOUlHU1NVQVQxVnIzNFhiMjJKdEFMZU1PVWc5YVItT0ZtcnZqdkJpOUlhRFdHTDU0SXhQa0RyajBEUWlVcW1nUFREYU9oVU9GaHhMcXlScVFQNkpjaFJRcjhPbnZhRUw4cU83Zk5CdkpXYUxBX2ZoZHZjRFkxb2FsWnl3?oc=5) - Google News source discovery | Yahoo 奇摩股市 Sun, 21 Jun 2026 21:30:00 GMT
- [中磊：公司於德國地區營收比重甚低，華為技術提訟案估影響極為有限- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxOUFFrMzRORWh6YWI2b1dSaVpwd2hIN2VNQ05KemxPR0dwTjE0UXBjWl9nVXRmMkx3Q0dlNXF4RjhrR0Y0SXFEMFBCTHpoelhiSUJGTFBiU09BQS0tbW5PS0dia3RTNVA1REsyM21IVWRuT1dlUWRvMG8wZnFKeEhBTFhMQkxFbXlCeDJfM0xOaVA3QQ?oc=5) - Google News source discovery | MoneyDJ Sun, 21 Jun 2026 21:30:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
- TWSE PER/PBR 抓取失敗：Expecting value: line 1 column 1 (char 0)
