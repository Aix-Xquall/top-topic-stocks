# 每日股市熱門話題分析 - 2026-07-27

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **新興題材：MoneyDJ**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0
2. **散熱與液冷供應鏈**｜正向｜熱度 1｜市場確認 77.77｜同向 1/1
3. **新興題材：AI伺服器液冷**｜正向｜熱度 1｜市場確認 77.77｜同向 1/1
4. **半導體與晶片供應鏈**｜正向｜熱度 13｜市場確認 N/A｜同向 0/0
5. **利率與成長股估值**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.54（樣本 8）
- 5日相關係數：0.11（樣本 8）
- 同向比例：3/8

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | 77.77 | 1/1 | 0 | +2.59% | +8.18% |
| 新興題材：AI伺服器液冷 | 77.77 | 1/1 | 0 | +2.59% | +8.18% |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 記憶體與 HBM 供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 0.25 | 1/6 | 5 | -3.81% | +5.18% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
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
| 2026-07-27 | 0.54 | 0.11 | +37.50% | 8 |

## 歷史回測摘要

- 回測日期：2026-07-27
- 近5日 3日相關：-0.13
- 近5日 5日相關：-0.11
- 同向比例：+25.00%
- 權重狀態：已調整

- 方向準確度：+25.00%
- 信心排序準確度：-0.13
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

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：法人專欄分析內容-台股 - MoneyDJ；台新-信義 對 台積電(2330)個股 單一券商歷史明細 - MoneyDJ；同業股價表現-生技醫療保健-基因定序-台股 - MoneyDJ

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | 0.00 | -2.49% | +2.62% | 2,350.00 | 2,410.00 | -2.49% | 不適用 | 74.39 | 31.59 | 442.68B TWD / 67.87% | 2026-07-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「2330」，共 1 篇新聞命中。

### 主要來源

- [法人專欄分析內容-台股 - MoneyDJ](https://news.google.com/rss/articles/CBMilgFBVV95cUxQUktTU2pPVDZvWGh3Ymc2R3UwOV92dUpuRnc4UW5NS2s3SnRrX1E2TWVwTXowZ0h0QjZGR0Z6LThIZW85aE5EN1lqQ0oyOW5NVkNPX28yUVN0dVFfRDlkMEthRXlNX3pNQWpIbFNoNEgzTUdlbnpQU0tTdVR4NHFmVzVCbkJnSWVpR181MEQwaUNLRnlWUnc?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 26 Jul 2026 16:11:02 GMT
- [台新-信義 對 台積電(2330)個股 單一券商歷史明細 - MoneyDJ](https://news.google.com/rss/articles/CBMilwFBVV95cUxNLVdJNzdnelltZHZteGRlVzhIak9Rdy1XQjc0T3Q0b0wyZ1paNmZubHhPd3Q0b2JxX1l0X2tmcDl0Y19iejRmZENsZThlTzRZdUQtcGZmcmR6X1BEajNjTHkzNkE2TkhxNkhvM25YZlpoM3EzcVhjQWVtUjU4dUZRckQxRWtGZXZlcTQtYXFYN0t5dTVXcjJ3?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 25 Jul 2026 14:30:50 GMT
- [同業股價表現-生技醫療保健-基因定序-台股 - MoneyDJ](https://news.google.com/rss/articles/CBMiYEFVX3lxTE11Q3pacFE1SktwTl9FeEpQMDBnVWtWbWQzMTN4NDM3UGwtaDZsaUR1Rm14cndWSlBqWW5aSnprOF85dWhpUkpfVUJqam1QcGhseE5iZTBxV0ZRYkpHRXVaVw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 25 Jul 2026 00:10:36 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：GB300升級VR200！AI伺服器液冷全面標配化 散熱產業規格升級全解析 - news.cnyes.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.43 | +2.59% | +8.18% | 2,380.00 | 2,835.00 | -16.05% | 同向 | 61.06 | 39.11 | 17.62B TWD / 66.11% | 2026-07-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 1 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：升級。

### 主要來源

- [GB300升級VR200！AI伺服器液冷全面標配化 散熱產業規格升級全解析 - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTE1qTlRBc09MS1RjaUpoTmxIZncyYklpMWpqcTctTnJOSGNzeUloOE11LXZwRHN0V1Nqa0hBTW8wMGNUeDhzTWoycXZtU2d0ZFU?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 25 Jul 2026 13:30:03 GMT

## 新興題材：AI伺服器液冷

摘要：新興題材：AI伺服器液冷 相關新聞集中在：GB300升級VR200！AI伺服器液冷全面標配化 散熱產業規格升級全解析 - news.cnyes.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.42 | +2.59% | +8.18% | 2,380.00 | 2,835.00 | -16.05% | 同向 | 61.06 | 39.11 | 17.62B TWD / 66.11% | 2026-07-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 1 篇新聞命中。 方向判斷命中詞：升級。

### 主要來源

- [GB300升級VR200！AI伺服器液冷全面標配化 散熱產業規格升級全解析 - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTE1qTlRBc09MS1RjaUpoTmxIZncyYklpMWpqcTctTnJOSGNzeUloOE11LXZwRHN0V1Nqa0hBTW8wMGNUeDhzTWoycXZtU2d0ZFU?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 25 Jul 2026 13:30:03 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：舊金山AI峰會韓國推動半導體總額9500億美元合作| 國際 - 中央社 CNA；台股半導體ETF 扮多頭主角- 日報 - 工商時報；外資：半導體遭超賣- 日報 - 工商時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 92.32 | 114.68 | -19.50% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -2.49% | +2.62% | 2,350.00 | 2,410.00 | -2.49% | 不適用 | 74.39 | 31.59 | 442.68B TWD / 67.87% | 2026-07-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | -4.83% | -11.11% | 128.00 | 164.50 | -22.19% | 不適用 | 4.00 | 32.16 | 23.12B TWD / 22.85% | 2026-07-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -2.04% | +18.60% | 206.84 | 211.14 | -2.04% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 521.95 | 521.95 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 920.95 | 971.00 | -5.15% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | +15.77% | +14.12% | 1,610.33 | 2,335.00 | -31.04% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -14.52% | +23.40% | 381.92 | 446.77 | -14.52% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 CPU, server CPU, x86, foundry；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 0 篇新聞出現相關標籤。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 0 篇新聞出現相關標籤。

### 主要來源

- [舊金山AI峰會韓國推動半導體總額9500億美元合作| 國際 - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTE10T3RQQzQ1c1BiWHpoUlJBLUtjekdoUFNlYm5YQ2dXREREVWx3OWEtVGJ0Ry1LbUVFWUtLQkNEVjJvQkRoRHlJb2VNOXk2bFF6WG8tb2RBRmJSSkRRWnNn?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 25 Jul 2026 09:33:00 GMT
- [台股半導體ETF 扮多頭主角- 日報 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1YMGJVeU0zOG9ITDQxTDIzdnBxWWpDWnNFbVVnRFZpWjdZTVNkN0RvSXJHa2hLRmJIc2tLbHd5eWJQckZYakpnaU1RYjBIWjhvRDJfbEVsYkNzZVEwUGM0?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 26 Jul 2026 19:00:00 GMT
- [外資：半導體遭超賣- 日報 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5Ua0x1UmhtdU56bnp5a21HN1JYQm41bWZmWnZIUGJOUjQ5YzF4ekk3azNUMV9SNWdZVWY4dmtGN0FwSWJwX21NanBmcHBQWkdzeXpWZUI3eXhCOXBTamtr?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 26 Jul 2026 19:00:00 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：Intel Stock: Grotesque Valuation (NASDAQ:INTC) - Seeking Alpha

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 92.32 | 114.68 | -19.50% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | -2.81% | -24.67% | 381.70 | 506.69 | -24.67% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Stock: Grotesque Valuation (NASDAQ:INTC) - Seeking Alpha](https://news.google.com/rss/articles/CBMidEFVX3lxTE5iWm5mQjItRTNsaHA2OGptQ0Y1YVVWbWVQWUR5VFhqMXg2emJGVnNteV9TOGpVNVF6dnpnekcyQnlORUpScXRyV2xkdFhSdVVHRWJqdGZhVFAwVzhoUV84WmJKUEFraEdGZVV1WXRkNjZkS3pK?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 26 Jul 2026 09:12:43 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Prediction: This Will Be Sandisk's Stock Price by Mid-2027 (Hint: It Implies a Big Move) - AOL.ca

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| SNDK SanDisk | 新聞直接提及 | 0.00 | +15.77% | +14.12% | 1,610.33 | 2,335.00 | -31.04% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 920.95 | 971.00 | -5.15% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -2.04% | +18.60% | 206.84 | 211.14 | -2.04% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- SNDK：新聞直接提及「SanDisk」，共 1 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- MU：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 AI memory, memory, HBM, HBM4；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Prediction: This Will Be Sandisk's Stock Price by Mid-2027 (Hint: It Implies a Big Move) - AOL.ca](https://news.google.com/rss/articles/CBMihAFBVV95cUxQdk5sNDEyNmp6TTl1XzFpaXZqSXN3clNWSUVIbk92SmtMTkZYLXUtMVJGQ1NaZmtkQXptck9oRVF6SFNqaTFuY29KdTAycXVRNmI4aTlRQnpWYVVHZm9XVlFib1JxU3pTcTRZMGxsSTl2Tk9pNTQtTFNjTGE1Qmp1Vl9Sek4?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 25 Jul 2026 01:02:17 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：AI 破解水的百年謎團：為什麼水結冰會膨脹？大阪大學找到觀察水分子的最佳「透視鏡」 - TechNews 科技新報；企業 AI 成本救星來了！Anthropic 以 Fable 一半價格推出 Opus 5 - TechNews 科技新報；企業應如何評估 AI 查核人力成本與自動化效益的平衡？ - TechNews 科技新報

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

- [AI 破解水的百年謎團：為什麼水結冰會膨脹？大阪大學找到觀察水分子的最佳「透視鏡」 - TechNews 科技新報](https://news.google.com/rss/articles/CBMilgFBVV95cUxNRFZmZEV6TzV4Rk41cl9XSW9ScHMwNWVtNFc1X0pIcmpodkQ0NjJMMVZSWldwTFFrdld1OUtIMUxReW9KTzZWSDBPNUJHWGRMTExLMEtBbmV3QnpmTEVkbk8yVFlKUGtOQWl6QjJpVkhaUllTWmV1WWRIZ3BBYWJmR0V0ak5nUi1LSDVNNDlPaER1RFFQd2c?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 25 Jul 2026 00:35:18 GMT
- [企業 AI 成本救星來了！Anthropic 以 Fable 一半價格推出 Opus 5 - TechNews 科技新報](https://news.google.com/rss/articles/CBMimgFBVV95cUxOaDRnQ1g0V0g4YnRvelpEZXVXejM5Tk5rcjdNUk9CemE1a0piRTIwbmljQm9GYXc0a3pYbFNld1RsQi04Z1BobzFPQ0JMd1RGUFlISXhrMVpGbjc2Q0h2X2hSTUFLTVJ6enBvSVNrTmIzS2lzdl9zSXFWTkx0TDdjMDFLQ21xd2JINXhXUHYwdWRPRlA0REJ3cmZn?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 26 Jul 2026 03:20:24 GMT
- [企業應如何評估 AI 查核人力成本與自動化效益的平衡？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiugFBVV95cUxOWlM5Z0JNa3lHdlkzdGJkV1lmUVV2TUFSRlRVblI4b1U5NVQtWFNQM3dFWk9NZWs3aFA3Q1JVbm9XOGlPTjl2Y3VrNVRJV0xMLXBXMTFmOExSZHQtX1lSa2x6TXEwaWg2aFNpeTNmRVlUbzVZMnBYc3NjamN3a3k3cEFMRFRGNHFLQlJyUVRBT0lnblByc0txbl8xNGhuRlJaU1FKX2R4SHpGYVE0V0tKTldwTm9vQmFQNHc?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 26 Jul 2026 07:49:00 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股高檔震盪加劇 本周多空行情決戰三關鍵聚焦 - 經濟日報；費半重挫逾4%　法人：台股短線仍處修正整理 - 經濟日報；台股再次跌破季線 整理期將拉長 法人點名三題材可逢低切入 | 市場焦點 | 證券 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股高檔震盪加劇 本周多空行情決戰三關鍵聚焦 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE0xQ2ItT1VBYWhYbElKVW9NRTRKM0FuVlJpcmNIYldKbWdWYnZYdzVmZXJUSkJrdmdGSlZxUjFQMExRcmhXb01GeS1EYmFGOEhaWW1kY0ZYLVBHZ9IBX0FVX3lxTE0tTTNJazZDNnRRTkxsWS1rbDg2WW1BTXpBTnVVcGlYRkNzc3pOa3JrLUVwcnNGYUR1QlIyOWJfQ2M0cnRWWmE2NmlhRXJvVkViOEU4YXB5YWhSaWtSeHFJ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 25 Jul 2026 09:00:00 GMT
- [費半重挫逾4%　法人：台股短線仍處修正整理 - 經濟日報](https://news.google.com/rss/articles/CBMif0FVX3lxTE45N1I0TGZxS0gwQy04X3BnTkdCSVhFNDg4ZEZQVTVjZ2lMNl9Sa0V1Nk5RTnNUUzdGQXd5Q0M1Skc4TThEczBUeHJHMUczNW5wVTBISUZvaWNLZ1ZscVpURWpBaGtsa2hGdmhVaENNUy02cHpzS2FnSzJ1YXBhVjDSAV9BVV95cUxPTmRNZmhzUWNuWW1pZkFCTFQzV1Vyc19VWU9CUzNza2ZISjZFNjM4aXg2SnAzbXN5MDFlZ0pqNVdRTTZrczBuT0t0ajVYVElMU2p2M0FQS3lWNndWN3FNTQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 26 Jul 2026 16:55:59 GMT
- [台股再次跌破季線 整理期將拉長 法人點名三題材可逢低切入 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMidkFVX3lxTE95X1ZzTTFRTndWamdCeXd6WkZNaDBvWWVMYzVERUJoOFZiMVRqSmZpNlpwTm5kSVNTT2otRnFhc2dhWGs4dUNtM04zOVY1bWt2Tmk3d0JSS2dOc3VDNnkyd3NkVjU5b1VsaGZ2Q2VZcFdmNV9sdGc?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 26 Jul 2026 14:36:18 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
