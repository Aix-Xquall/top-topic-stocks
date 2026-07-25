# 每日股市熱門話題分析 - 2026-07-26

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜正向｜熱度 7｜市場確認 55.59｜同向 1/2
2. **散熱與液冷供應鏈**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
3. **半導體與晶片供應鏈**｜正向｜熱度 11｜市場確認 9.13｜同向 1/5
4. **AI 伺服器與資料中心**｜正向｜熱度 17｜市場確認 0.25｜同向 1/6
5. **關稅與供應鏈轉移**｜中性｜熱度 3｜市場確認 22.95｜同向 1/4

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.38（樣本 17）
- 5日相關係數：0.06（樣本 17）
- 同向比例：4/17

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 55.59 | 1/2 | 1 | +6.87% | +16.36% |
| 散熱與液冷供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | 9.13 | 1/5 | 4 | -1.62% | +9.53% |
| AI 伺服器與資料中心 | 0.25 | 1/6 | 5 | -3.81% | +5.18% |
| 關稅與供應鏈轉移 | 22.95 | 1/4 | 3 | +1.81% | +5.14% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：B104 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-07-13 | 0.39 | -0.09 | +15.38% | 13 |
| 2026-07-14 | 0.10 | -0.07 | +21.43% | 14 |
| 2026-07-15 | 0.20 | -0.16 | +28.57% | 7 |
| 2026-07-16 | 0.20 | 0.02 | +33.33% | 12 |
| 2026-07-17 | 0.36 | 0.02 | +60.00% | 15 |
| 2026-07-18 | 0.18 | 0.08 | +53.85% | 13 |
| 2026-07-19 | 0.37 | 0.09 | +12.50% | 16 |
| 2026-07-20 | -0.59 | 0.11 | +45.45% | 11 |
| 2026-07-21 | -0.12 | -0.03 | +12.50% | 8 |
| 2026-07-22 | -0.33 | -0.15 | +16.67% | 6 |
| 2026-07-23 | -0.01 | 0.01 | +41.67% | 12 |
| 2026-07-24 | -0.16 | 0.43 | +50.00% | 6 |
| 2026-07-25 | 0.30 | -0.06 | +12.50% | 16 |
| 2026-07-26 | 0.38 | 0.06 | +23.53% | 17 |

## 歷史回測摘要

- 回測日期：2026-07-26
- 近5日 3日相關：0.25
- 近5日 5日相關：0.20
- 同向比例：+27.27%
- 權重狀態：未調整

- 方向準確度：+27.27%
- 信心排序準確度：0.25
- 診斷：正相關

調整原因：近 5 日有效樣本 11 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：台股開高 記憶體族群強勢 - 經濟日報；Micron Boosts HBM4 Ramp-Up: Will It Help MU Lead the AI Memory Race? - Yahoo Finance；Micron and Sandisk Are Surging: Can the Rally Last Through 2027? - AOL.ca

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.50 | N/A | N/A | 920.95 | 971.00 | -5.15% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.50 | +15.77% | +14.12% | 1,610.33 | 2,335.00 | -31.04% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.22 | -2.04% | +18.60% | 206.84 | 211.14 | -2.04% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron、memory」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 2 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 2 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [台股開高 記憶體族群強勢 - 經濟日報](https://news.google.com/rss/articles/CBMieEFVX3lxTFBlLWIwOXFvWUIzSzRScHFOYkNlNlFSSE9VR1hoWmpNblljM3FSQjN5eFBLZGM4a2JZZVY4Q3VhSTQ3a1ppNXlxUHpkWWRwcDF6T1ZzazItQjc0OERmQ0xNNlBBUnM0QjVtdVpNNG1HRE9WTjJvS3ZZLdIBX0FVX3lxTE83WDIybmhZTEJ0bXZ5N3RqMzkxV3Jub1JmQnFGYnRvY2M1ZTZ2REl0OHRldGhFMzUwaFg0cjlfeV81bTQwZGw2Vm1qYXh4SThMRGZTWmRRVUE3Q2hUR3BF?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 24 Jul 2026 09:00:00 GMT
- [Micron Boosts HBM4 Ramp-Up: Will It Help MU Lead the AI Memory Race? - Yahoo Finance](https://news.google.com/rss/articles/CBMilwFBVV95cUxOODdfeExDRWc2VlloS0ZPU2RrcDA1UEpzbWZnOV9lTVpiLUZVR2lYWXlaMEc2ZzljRnRiTkxJTHpIbWYtYTI4OXlDdUtRU1dVTVlHSlhOajZrN3praGFrWVBfS2ZobHJiaVpiZzlERlptY0RJamhXZ3p6S3N5SzZ5dTJ6cDRrMS01SThFNmVuQnNRb0ExREk4?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 24 Jul 2026 12:47:00 GMT
- [Micron and Sandisk Are Surging: Can the Rally Last Through 2027? - AOL.ca](https://news.google.com/rss/articles/CBMiggFBVV95cUxQY1l0SVlObTFldHhaVkxhMUdSSEd1Mk9uNWpzMTJvVnlmcS1XZTY2ejhTM19Ma0lyekZuY1YzMTEyV1ZwcHhVOGxBclh5STViR2ZtbFZzaGhIWXdQcGVNbFFiV09WS2hzOWYtVTFFSkVYLUY2enp1TGplT2MxbFRmLWF3?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 24 Jul 2026 17:24:53 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：GB300升級VR200！AI伺服器液冷全面標配化 散熱產業規格升級全解析 - news.cnyes.com；焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | +2.59% | +8.18% | 2,380.00 | 2,835.00 | -16.05% | 不適用 | 61.06 | 39.11 | 17.62B TWD / 66.11% | 2026-07-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 2 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：跌停, 升級。

### 主要來源

- [GB300升級VR200！AI伺服器液冷全面標配化 散熱產業規格升級全解析 - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTE1qTlRBc09MS1RjaUpoTmxIZncyYklpMWpqcTctTnJOSGNzeUloOE11LXZwRHN0V1Nqa0hBTW8wMGNUeDhzTWoycXZtU2d0ZFU?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 25 Jul 2026 13:30:03 GMT
- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 24 Jul 2026 17:19:02 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：What Triggered the Recent Semiconductor Sell-Off - Kavout | AI；Intel Rises 3% on Q2 Earnings Beat, Upbeat Q3 Outlook as Chip Sector Stays Flat - 24/7 Wall St.；舊金山AI峰會韓國推動半導體總額9500億美元合作| 國際 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.53 | N/A | N/A | 92.32 | 114.68 | -19.50% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.03 | -2.49% | +2.62% | 2,350.00 | 2,410.00 | -2.49% | 背離 | 74.39 | 31.59 | 442.68B TWD / 67.87% | 2026-07-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.03 | -4.83% | -11.11% | 128.00 | 164.50 | -22.19% | 背離 | 4.00 | 32.16 | 23.12B TWD / 22.85% | 2026-07-01 |
| NVDA 輝達 | 產業/供應鏈推估 | +0.02 | -2.04% | +18.60% | 206.84 | 211.14 | -2.04% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.04 | N/A | N/A | 521.95 | 521.95 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | +0.04 | N/A | N/A | 920.95 | 971.00 | -5.15% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.04 | +15.77% | +14.12% | 1,610.33 | 2,335.00 | -31.04% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -14.52% | +23.40% | 381.92 | 446.77 | -14.52% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：upbeat。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 2 篇新聞出現相關標籤。 方向判斷命中詞：upbeat。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 2 篇新聞出現相關標籤。 方向判斷命中詞：upbeat。

### 主要來源

- [What Triggered the Recent Semiconductor Sell-Off - Kavout | AI](https://news.google.com/rss/articles/CBMiiwFBVV95cUxQeV9hbWl4LXg0eW5ZWFVERlpaZGRsZzBkOEQzb0VuSmptQ2RsR3RUcldSTzhJcW1URGZsbnBjVUxmYlNpMHlESnlJdEVvZ1RaSWloQ0ZfODJXV012UF9qYjFfYVNDaG15cXpBNXYxYWpjaGNIY2hRa3hOdGhUSjdOcDhabENFWmFvV1M0?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 25 Jul 2026 16:21:35 GMT
- [Intel Rises 3% on Q2 Earnings Beat, Upbeat Q3 Outlook as Chip Sector Stays Flat - 24/7 Wall St.](https://news.google.com/rss/articles/CBMivgFBVV95cUxQaUJQV2hra2c5UGd2OE9sMmpBX01KQVZVaFFoczllcFRKM2xyZ3ZtX1ZZclpxNlBiRnNGOVlzcEs4Q3pKclEzSG9VVmZOMWhnMzg4U0lGdWNFRkVVSzNkaVFYU0tqZHpWNGFMeGZkYXJFZjdnNzdDU1BuVThsWmZTNGlXUG5WUUp4TU1tRThGMkZ4VTFVMmh1NDhfVnpReGkzNEZTM2ZPRWdJZVJZZm4wajlTeVJHWUtLM0RSWjJn?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 24 Jul 2026 13:16:15 GMT
- [舊金山AI峰會韓國推動半導體總額9500億美元合作| 國際 - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTE10T3RQQzQ1c1BiWHpoUlJBLUtjekdoUFNlYm5YQ2dXREREVWx3OWEtVGJ0Ry1LbUVFWUtLQkNEVjJvQkRoRHlJb2VNOXk2bFF6WG8tb2RBRmJSSkRRWnNn?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 25 Jul 2026 09:33:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：What Triggered the Recent Semiconductor Sell-Off - Kavout | AI；AI 破解水的百年謎團：為什麼水結冰會膨脹？大阪大學找到觀察水分子的最佳「透視鏡」 - TechNews 科技新報；自建電網是否成為 AI 產業新常態？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | +0.08 | N/A | N/A | 92.32 | 114.68 | -19.50% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.03 | -2.04% | +18.60% | 206.84 | 211.14 | -2.04% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.06 | N/A | N/A | 521.95 | 521.95 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.03 | -2.49% | +2.62% | 2,350.00 | 2,410.00 | -2.49% | 背離 | 74.39 | 31.59 | 442.68B TWD / 67.87% | 2026-07-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.02 | -2.81% | -24.67% | 381.70 | 506.69 | -24.67% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -14.52% | +23.40% | 381.92 | 446.77 | -14.52% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.02 | -3.16% | -0.16% | 613.00 | 680.00 | -9.85% | 背離 | 10.86 | 56.92 | 65.78B TWD / 32.86% | 2026-07-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.04 | +2.18% | +11.28% | 3,750.00 | 4,310.00 | -12.99% | 同向 | 62.91 | 59.76 | 58.01B TWD / 2.80% | 2026-07-01 |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [What Triggered the Recent Semiconductor Sell-Off - Kavout | AI](https://news.google.com/rss/articles/CBMiiwFBVV95cUxQeV9hbWl4LXg0eW5ZWFVERlpaZGRsZzBkOEQzb0VuSmptQ2RsR3RUcldSTzhJcW1URGZsbnBjVUxmYlNpMHlESnlJdEVvZ1RaSWloQ0ZfODJXV012UF9qYjFfYVNDaG15cXpBNXYxYWpjaGNIY2hRa3hOdGhUSjdOcDhabENFWmFvV1M0?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 25 Jul 2026 16:21:35 GMT
- [AI 破解水的百年謎團：為什麼水結冰會膨脹？大阪大學找到觀察水分子的最佳「透視鏡」 - TechNews 科技新報](https://news.google.com/rss/articles/CBMilgFBVV95cUxNRFZmZEV6TzV4Rk41cl9XSW9ScHMwNWVtNFc1X0pIcmpodkQ0NjJMMVZSWldwTFFrdld1OUtIMUxReW9KTzZWSDBPNUJHWGRMTExLMEtBbmV3QnpmTEVkbk8yVFlKUGtOQWl6QjJpVkhaUllTWmV1WWRIZ3BBYWJmR0V0ak5nUi1LSDVNNDlPaER1RFFQd2c?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 25 Jul 2026 00:35:18 GMT
- [自建電網是否成為 AI 產業新常態？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMirgFBVV95cUxNbnVEbkhKODhONmh3S3M3R2huZWxtQlgzR192TmRpeDg0dDBfSG95aGMxS1dKYnBtN0JkdF92YjhsRThmVWdfYTQ1a3lhQWtaUnlvRl9SOW55MUVRUmhrR25fZUFiUWp3WGpEVjZObU85QV8zVEtWUm5aQTEyZnktbGNUZENOVjRManRxc01nMFh4YVJ0eHFibmJudGluclNZQm4xczRBXzRLSHZxY2c?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 25 Jul 2026 15:30:53 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：AMD首款AI機櫃Helios下半年出貨、微軟宣布加入買家行列挑戰輝達霸權：從台積電先進製程到緯穎伺服器組裝，台美股受惠供應鏈與投資關鍵｜股市話題｜豐雲學堂2026 年 07 月 - sinotrade.com.tw；〈台股開盤〉美國新關稅24日生效 衝擊台股跌逾800點回測4萬4與季線 - news.cnyes.com；〈ETF成分股調整〉00891換股納中美晶、台勝科、大聯大 完整涵蓋AI供應鏈 - news.cnyes.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.21 | -2.04% | +18.60% | 206.84 | 211.14 | -2.04% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 新聞直接提及 | +0.21 | -2.81% | -24.67% | 381.70 | 506.69 | -24.67% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | +0.21 | -2.49% | +2.62% | 2,350.00 | 2,410.00 | -2.49% | 背離 | 74.39 | 31.59 | 442.68B TWD / 67.87% | 2026-07-01 |
| 6669 緯穎 | 新聞直接提及 | +0.43 | +14.60% | +24.03% | 5,730.00 | 5,730.00 | 0.00% | 同向 | 298.31 | 19.21 | 111.37B TWD / 29.79% | 2026-07-01 |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +26.06% | +43.46% | 333.02 | 333.02 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | +2.64% | +7.91% | 252.50 | 289.00 | -12.63% | 不適用 | 14.13 | 17.93 | 821.76B TWD / 52.11% | 2026-07-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MSFT：新聞直接提及「微軟」，共 1 篇新聞命中。 方向判斷命中詞：受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 方向判斷命中詞：受惠。

### 主要來源

- [AMD首款AI機櫃Helios下半年出貨、微軟宣布加入買家行列挑戰輝達霸權：從台積電先進製程到緯穎伺服器組裝，台美股受惠供應鏈與投資關鍵｜股市話題｜豐雲學堂2026 年 07 月 - sinotrade.com.tw](https://news.google.com/rss/articles/CBMiyAZBVV95cUxQMGZxaWxQSEJ2MUtZNTFRMjVIa09hSWJ4NDN4cDhrM3FlcE95bTdVNkxaeGpCZDEzaG1UOVVOSGZUNFFDOXZQQmhzamkwQlBnOXlDRDRlYnFqVkxnUzdqbTN4ZURNdkxqNHc2eUM5cGs4NnVFeUFndThHd0x1NlJ1ZkFReF9QTVpLRkN6YmM4ZVV5NjFmcUE4T3pzMGRXTjRvS1RyOFpLZS12dTM1dXNVMFZBNU8xOVU4YTNRQ1gxVHhYQy1oV3o3TllFSzBqU0EzcGx6TlFVYTg4Y0JSZ29PSURQZGFjTlhuY2dxeENPdGFHWjNqY2lxNjMzeDJHazN5OVdobTVIM1QxdGFncENURjM4NU8zdDNFMFVHOTc1RzNCWDk2WnkxemdaNERzSDRZeTJiV0doeGtIWDBLUjNpS01IUlVJdXBLQUFaQ2hwdUdRYzJoQzVQUnFkcDVrM2NaSjQ3SF9Uelk5WTFtV2dnOGNMMDcxVGFLUVVNNGg2bVhCd3NMajg5VDQzVU9GODBCT3J3Q19RSGg2M3VrVV9xbUlZaElWNHhmRlh6dkpYWmVJRnptSTlpcnF0enVad05KdlBsbXphMENlMmRKakw5N2d2VlJKdU9BcGFLaE5ENF9PSXlCdENwQTRkWUNZU3JLVVp4RzBnYkpkLUtldV84cFRDamNHN3VWVVFfRVQ5bUljTmttMnNFOWFabkhJQjgwaV84OHNiajliNmpmcjFhczRGb1BVV3pGZWwyNzRqMTBnb29LdW56VmFwSzR5N19kUjBrVGU5UjF4RGpIV3V5am5PWnBYaGgxTl9CajZYY0FtT2pqTWlyRHNRTV9LT19KTWV3dF85Y3NiY0pNUS1aTUI4bDFtemRxS3JibUhFUmN0SWFfZmsxZVBhWVF3NmttV0xuOVhJcVlIZmI2ck04MjZZWWEtem1SQVJkYjVxZXJiaWtWa3N4bUFndmh4QUFDSk5pY2I3RWExdHdsWWRQa3FMWVZWb2FQS09lWTlSQlk2NzhzWGJnOGpSaDZ3ekdXTW1VNThtOWdCSS1KcTA3b2tzNmNkY2ZqajJDUlVSLXVQSF81dFZBT0FHVzlySDJqZ1duSXBlaC0?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 24 Jul 2026 19:29:38 GMT
- [〈台股開盤〉美國新關稅24日生效 衝擊台股跌逾800點回測4萬4與季線 - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTE5PTzVDVEFOWW5lZVBOdUFEaFVKMy0tTDV1b3NmU3d3M2JmODdfZDRPYVJnWGgyT2gwbmlmUGQyajhVVXFaMVNPekhrOUowWlU?oc=5) - Google News source discovery | 鉅亨網 Fri, 24 Jul 2026 01:47:06 GMT
- [〈ETF成分股調整〉00891換股納中美晶、台勝科、大聯大 完整涵蓋AI供應鏈 - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTE15bDljOXN6VXhidDBxeTk4dC1tbGFocmVnWE5EYnRneUZMTENvVl9xNGE1YmVMemdDMFNzcEJOUjk3YXZvV1YwdEI4MTNldkU?oc=5) - Google News source discovery | 鉅亨網 Fri, 24 Jul 2026 06:32:36 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：國泰證券 對 神隆(1789)個股 單一券商歷史明細 - justdata.moneydj.com；個股動態報導內容-8BB25D0A-EC3B-447A-9725-EDBC2AE73EAA - justdata.moneydj.com；台股量縮下挫1195點歷史第9大跌點　週線翻紅 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [國泰證券 對 神隆(1789)個股 單一券商歷史明細 - justdata.moneydj.com](https://news.google.com/rss/articles/CBMihgFBVV95cUxNTHhKVFNxeVItZ3RJQ1ZMaVcyaW1ZMEx4c25KVm0yTFFvZ2JYWld6d19NUXd5Q1FTdzhKRjE0RXUwek0tZlFZaWh4R0VNLU5kaDg2cFdRSU4yOHJIdTdBMEtFdnpNRU9zWDlZamJSTGpjSnRJMm12d3NmcmZCZ3dGRWlMM2cxUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 24 Jul 2026 18:12:30 GMT
- [個股動態報導內容-8BB25D0A-EC3B-447A-9725-EDBC2AE73EAA - justdata.moneydj.com](https://news.google.com/rss/articles/CBMikwFBVV95cUxNc3l2YjlQaXhFemYwRXM0LVY0N254WVUyQ3lDQldERmNONjRGZ1Nxd081clpMeE41ZFFxZFlkV1k4SUgxbzlyQ0NfLVhHaXNpWF9BRmlsdjBDa3VuaU44Y21WY0k2QUM3WjFIUElLUDhoOS1WYUVhZ1pVXzR1QVU0MUhqVXZHcmg0QUtsMzg4WDlnZkE?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 24 Jul 2026 23:05:26 GMT
- [台股量縮下挫1195點歷史第9大跌點　週線翻紅 - 經濟日報](https://news.google.com/rss/articles/CBMie0FVX3lxTE1vaWplckJobzJCeGZZUUhabkgwd0R1TlB4bDFtVGFJT0h0dmxWZE1IYl8wVlN5SlpxY2taenhCdTBiQ3lMaXF1UXEzVTlyMUxZSXB1M2tyeF9Lb3lQcGd6cjFoRC11YlJWbFAtbk02OUlWR2t1MUR5cnNVVdIBX0FVX3lxTFA5QXVTdG1qNU5hZUtkdXJ1aTZXRzJ6aEtfcld0QURzNG9CWXhtQnlabVVUNWgwU1A5cG1NOUZtczlsQjN1OW1tTEgxdzNzSDRzTmM1Y1NiNUxYZjRYLU9V?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 24 Jul 2026 07:00:53 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》大跌1195點、10日線又失守；週K翻紅-新聞內容-基金 - MoneyDJ；個股動態報導內容-9607B820-B104-44F6-9A98-BC07985F3E0A - MoneyDJ；個股動態報導內容-6803D646-B1E6-47C4-8BA6-86B58C003E18 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》大跌1195點、10日線又失守；週K翻紅-新聞內容-基金 - MoneyDJ](https://news.google.com/rss/articles/CBMimAFBVV95cUxORE5wd3htMlNMTXJHNG5McDFHS2FFUDM4UWlkZkJINno3U1lnMXV3M3MxUTd1cGd0VzN0Skp6T2Nvbi1rUEJ2eFFLOGQwWWJmQzR6ak9ZTWppbFZKazFNcEtwMVN1RjFWSkRXMjN4MDVPdlFHRlVHVzFFMXJsNGNPM05wQS00M1N1cWp3OXFUcFpGaDd2WUpPLQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 24 Jul 2026 08:09:00 GMT
- [個股動態報導內容-9607B820-B104-44F6-9A98-BC07985F3E0A - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxOcWdNSl9jNGxsdTk0dHNIeHYtRml0blRBVnl4TGZGQ2x0bXJUczd1aWhCN0JyZDhDRUQ3N2dSay04alNtb1dPN0ZwVDBHOThRYmJKckJhVGQ3U3dpQ2NwMnBzNGkxMlZnS3gtWXlJbVZXTjVndkNlVG5VMTBmM3MwZEZWd1pCS0RoXzh1TmswNE5iS0E2?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 24 Jul 2026 11:10:09 GMT
- [個股動態報導內容-6803D646-B1E6-47C4-8BA6-86B58C003E18 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxNcXdRVkZseXZ2dVIzWkZYc1BXNVIxdDF6aXFOU2JVeVY4ZDFUZktVT21IcDhoSlRoRGFOaUlobW9oS0R0T21QWWRlSm5fV0pRV1NEcFFnYXlQckhUWXVPa1BmTGo1Mkk3cXNSc2VTV0MzeE5fdzhuNW1SMG42cmNYZjVndGRXb1hjNXVELTdrU0w0cmdr?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 24 Jul 2026 11:10:38 GMT

## 新興題材：B104

摘要：新興題材：B104 相關新聞集中在：個股動態報導內容-9607B820-B104-44F6-9A98-BC07985F3E0A - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-9607B820-B104-44F6-9A98-BC07985F3E0A - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxOcWdNSl9jNGxsdTk0dHNIeHYtRml0blRBVnl4TGZGQ2x0bXJUczd1aWhCN0JyZDhDRUQ3N2dSay04alNtb1dPN0ZwVDBHOThRYmJKckJhVGQ3U3dpQ2NwMnBzNGkxMlZnS3gtWXlJbVZXTjVndkNlVG5VMTBmM3MwZEZWd1pCS0RoXzh1TmswNE5iS0E2?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 24 Jul 2026 11:10:09 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
