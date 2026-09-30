# 每日股市熱門話題分析 - 2026-09-30

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **利率與成長股估值**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0
2. **散熱與液冷供應鏈**｜中性｜熱度 4｜市場確認 N/A｜同向 0/0
3. **新興題材：輝達散熱**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
4. **記憶體與 HBM 供應鏈**｜負向｜熱度 6｜市場確認 29.03｜同向 1/2
5. **半導體與晶片供應鏈**｜中性｜熱度 8｜市場確認 17.35｜同向 3/8

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.05（樣本 18）
- 5日相關係數：0.04（樣本 12）
- 同向比例：6/18

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：輝達散熱 | N/A | 0/0 | 0 | N/A | N/A |
| 記憶體與 HBM 供應鏈 | 29.03 | 1/2 | 1 | -1.99% | +3.04% |
| 半導體與晶片供應鏈 | 17.35 | 3/8 | 4 | -2.97% | +3.39% |
| AI 伺服器與資料中心 | 5.96 | 2/8 | 4 | -3.85% | -0.51% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：油價及記憶體 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 相關性偏弱；應提高同向價格確認權重，降低泛 AI、泛半導體等寬標籤推估權重。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-09-17 | 0.43 | -0.13 | +66.67% | 9 |
| 2026-09-18 | -0.15 | -0.07 | +35.71% | 14 |
| 2026-09-19 | 0.20 | 0.47 | +46.15% | 13 |
| 2026-09-20 | -0.04 | -0.25 | +30.77% | 13 |
| 2026-09-21 | -0.15 | -0.05 | +61.54% | 13 |
| 2026-09-22 | -0.00 | -0.01 | +88.24% | 17 |
| 2026-09-23 | 0.35 | 0.22 | +80.95% | 21 |
| 2026-09-24 | 0.05 | 0.42 | +90.00% | 10 |
| 2026-09-25 | -0.31 | 0.15 | +30.77% | 13 |
| 2026-09-26 | 0.22 | 0.14 | +63.64% | 11 |
| 2026-09-27 | 0.11 | -0.14 | +57.14% | 14 |
| 2026-09-28 | 0.05 | -0.53 | +63.64% | 11 |
| 2026-09-29 | 0.31 | -0.78 | +16.67% | 6 |
| 2026-09-30 | 0.05 | 0.04 | +33.33% | 18 |

## 歷史回測摘要

- 回測日期：2026-09-30
- 近5日 3日相關：0.04
- 近5日 5日相關：-0.06
- 同向比例：+35.71%
- 權重狀態：未調整

- 方向準確度：+35.71%
- 信心排序準確度：0.04
- 診斷：低相關

調整原因：近 5 日有效樣本 14 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：利率與成長股估值 相關新聞集中在：高本益比族群領跌 台股下挫392點收47631點 - 中央社 CNA；美國通膨數據與美光財報將揭曉 期貨市場震盪晶片股受矚目 - Yahoo股市；美股收盤／三大指數小幅收低 費半反彈逾1% 市場靜待通膨和就業數據 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | +9.69% | N/A | 1,065.08 | 1,080.53 | -1.43% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +13.04% | +3.45% | 508.96 | 508.96 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「美光」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [高本益比族群領跌 台股下挫392點收47631點 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE91WW8xMWkzbTEySUU4cmJDTGlnQzZZNXV5cTZMNVM2WThCWElJZlB2cHB0eHhNZnJlUzNsczFoREJJS1I1UEZ3YnpqN0VNYUFLSEpnZjh2NVk5OHBYWHc?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 29 Sep 2026 06:16:00 GMT
- [美國通膨數據與美光財報將揭曉 期貨市場震盪晶片股受矚目 - Yahoo股市](https://news.google.com/rss/articles/CBMilANBVV95cUxPOHNUcTJUMFIxUTJRSloyLVBuZG8yelpUS0dzN2wtVTJDS3FYYWo4STNSVk5fMXAwM0VYTnFGdGwzWmpncXZfOWxxMUpJdjlIQ0pDSlFqUDlZMkhhazdGMk4ybjNDYXByZTlaR0xvbHk0YmM5aXV3M2NnT1FmS3pzTzhpRFhfbmxQSTRyRlljS0N1Sy1ucDl6N3B1ck9QdFJUeG11aUNMNENDcEVIQXE0ckwtT2dqbmh1azFvRkMzZk1KeDlZN0l4NHdfVGZKRG5STWJKaDBkcmg2V1dJb3dxc21nVFVSekl2dDZWbm5SYlZvNGRvZy1NWUxHMUtGZkE5T2VlZXozeHBfUm5aVnFsMWR2bkRNTnZyLVhCN1NpeFlSUlJOMXc2cnN4eVFvckMyLWY2WktHOG5CbnNmbWE0UDdWLUdSNXE4UWlSRmpFcTJhcGtMV2lOam1veldhMG0tTGZhOWNhUXhaZ1RwTDZteTRkcm5makx0Q2tUb2F5bHlXU2V4X01ucW9hckZVYlNmaFVlRQ?oc=5) - Google News source discovery | Yahoo 奇摩股市 Tue, 29 Sep 2026 23:01:12 GMT
- [美股收盤／三大指數小幅收低 費半反彈逾1% 市場靜待通膨和就業數據 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTE83YkUxLUNPTXJERUJPUTBPU0VWenUzSTJlNWMxT0VCWVY4Q3k5UG15dEtoYWdvVzFMc0l5RTBsY1VOYUppNlpjT19XWExDaXlSX0hpSmZJQXFOMzRm0gFiQVVfeXFMUGEyOE1rcno5T1dOcjY5R0IxakRzWlBoYjFOTmpreDVuVHhleng3M1Mzc0VrSG01QWpBZXhSUWx4dXByVE9BMTlldExNbW9FMEttYXg1eUJ0YTB4VXplWlNQRmc?oc=5) - Google News source discovery | 經濟日報 money Tue, 29 Sep 2026 23:11:27 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：焦點股／輝達散熱認證台廠缺席！奇鋐、雙鴻雙雙跌逾5% 健策反創新高| 產經 - 非凡新聞台；奇鋐、雙鴻、健策...輝達散熱夥伴台廠缺席！這2檔跌半根、它反創新高，最新目標價「還有3成甜頭」 - 今周刊；散熱股真的涼了？最新百頁研究報告流出！「這檔復活重返輝達水冷名單」法人喊上2,000元逼哭空頭、三雄驚天目標價也曝光 - 旺得富理財網

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | +0.29% | -0.87% | 3,400.00 | 3,555.00 | -4.36% | 不適用 | 75.13 | 45.32 | 19.48B TWD / 54.34% | 2026-09-01 |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +13.18% | +7.61% | 227.21 | 227.21 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐、散熱」，共 4 篇新聞命中。 同時符合主題標籤：thermal。
- NVDA：新聞直接提及「輝達」，共 3 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [焦點股／輝達散熱認證台廠缺席！奇鋐、雙鴻雙雙跌逾5% 健策反創新高| 產經 - 非凡新聞台](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5ZMkFWNkNjZGNhRy1Ga0tLb3JXbHYxOUlTU2VyZ05Gel96MW5IOUpzRjNmWFBfN3BQY1lOQ1ZRa0tBclJwanB3dFQ0Y0JsNmlMU2RkNWNmQUlSYjRnQXJn?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 29 Sep 2026 21:37:35 GMT
- [奇鋐、雙鴻、健策...輝達散熱夥伴台廠缺席！這2檔跌半根、它反創新高，最新目標價「還有3成甜頭」 - 今周刊](https://news.google.com/rss/articles/CBMigAFBVV95cUxQZVV5eWdBR1ZBUUVtNi15WDc2aElJcVJvRWVCU29LTU1Yc25tLUxGT2FrWVFDRmpkNjdjTmUwSUEtWm1iRmN5Wnh6dFpPM3VURXNmYVNXZnFBU1NESTI3NXFrMERaRWpHNlQ3WVFMbHhkeHNyeF9aNHpRNnVuOE0tQw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 29 Sep 2026 08:04:00 GMT
- [散熱股真的涼了？最新百頁研究報告流出！「這檔復活重返輝達水冷名單」法人喊上2,000元逼哭空頭、三雄驚天目標價也曝光 - 旺得富理財網](https://news.google.com/rss/articles/CBMiakFVX3lxTE5iaGdreEtvOTMzNE9qOWpKSkIyZnQ5VXcyNXZJamlQUTNLZl9OLVBnWHBzMUFkT0p4cXF2TWExNEc3MXpUYUJfNlFnb050U2xMQk9TdGtLMW13WkRObC1STHl1ZDVnNWJMQWc?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 29 Sep 2026 05:56:36 GMT

## 新興題材：輝達散熱

摘要：新興題材：輝達散熱 相關新聞集中在：焦點股／輝達散熱認證台廠缺席！奇鋐、雙鴻雙雙跌逾5% 健策反創新高| 產經 - 非凡新聞台；奇鋐、雙鴻、健策...輝達散熱夥伴台廠缺席！這2檔跌半根、它反創新高，最新目標價「還有3成甜頭」 - 今周刊

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +13.18% | +7.61% | 227.21 | 227.21 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | +0.29% | -0.87% | 3,400.00 | 3,555.00 | -4.36% | 不適用 | 75.13 | 45.32 | 19.48B TWD / 54.34% | 2026-09-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 3017：新聞直接提及「奇鋐」，共 2 篇新聞命中。

### 主要來源

- [焦點股／輝達散熱認證台廠缺席！奇鋐、雙鴻雙雙跌逾5% 健策反創新高| 產經 - 非凡新聞台](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5ZMkFWNkNjZGNhRy1Ga0tLb3JXbHYxOUlTU2VyZ05Gel96MW5IOUpzRjNmWFBfN3BQY1lOQ1ZRa0tBclJwanB3dFQ0Y0JsNmlMU2RkNWNmQUlSYjRnQXJn?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 29 Sep 2026 21:37:35 GMT
- [奇鋐、雙鴻、健策...輝達散熱夥伴台廠缺席！這2檔跌半根、它反創新高，最新目標價「還有3成甜頭」 - 今周刊](https://news.google.com/rss/articles/CBMigAFBVV95cUxQZVV5eWdBR1ZBUUVtNi15WDc2aElJcVJvRWVCU29LTU1Yc25tLUxGT2FrWVFDRmpkNjdjTmUwSUEtWm1iRmN5Wnh6dFpPM3VURXNmYVNXZnFBU1NESTI3NXFrMERaRWpHNlQ3WVFMbHhkeHNyeF9aNHpRNnVuOE0tQw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 29 Sep 2026 08:04:00 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：台股收跌392點失守48K 觀望地緣政治、油價及記憶體大廠股價 - 經濟日報；4 Memory Semiconductor Stocks to Watch in October 2026 - Yahoo Finance；Micron and SanDisk Stocks Continue to Decline - intellectia.ai

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | -0.28 | +9.69% | N/A | 1,065.08 | 1,080.53 | -1.43% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.49 | -5.71% | -3.04% | 1,712.89 | 2,335.00 | -26.64% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +13.18% | +7.61% | 227.21 | 227.21 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「memory、Micron、MU」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：decline。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 1 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：decline。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [台股收跌392點失守48K 觀望地緣政治、油價及記憶體大廠股價 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE4zM3drVDhtcDZCaXJHb1A2cVlSdU1sMUNWeG54ZkNsUk5XSW9ORVpfQmpFalhoXzFsVVJza05RQnhiMWZLN3haSjFBbHpEX2RWcTYtTjU0a0V2d9IBX0FVX3lxTE1WdGlCd3pnYzlqZVFsZ2tsdDVSVTlhSktjQmROdFFuUHdKanRFVFpGQUE1RHJGSTNZdjBxcDktNEppX3VnVkhsdG5CMVdUZ2h5WVRhbzBURWxScEtQZkkw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 28 Sep 2026 09:00:00 GMT
- [4 Memory Semiconductor Stocks to Watch in October 2026 - Yahoo Finance](https://news.google.com/rss/articles/CBMiogFBVV95cUxOZFM5YmtsblI5Vm5PeHZjZnVmMTRhbEFXaGEzcXR5NE5OaWdjcGZjRXJvdXhsRzlZLTgxcUowMVdnb2F2dGFyR0hEUFF4Q0Y0QnhhbFhub2VfM3laX3FhREZMSHVDNEtMYnBsS2J4dkxWb2plZWFBaDB4Z21PRXAwV1FldGpaajQ0WWpvdTVCSDJxOUtyRUZVeGZrY0l3dGRDa1E?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 28 Sep 2026 13:18:00 GMT
- [Micron and SanDisk Stocks Continue to Decline - intellectia.ai](https://news.google.com/rss/articles/CBMihgFBVV95cUxPdmxMM3k5TVBVdXMwN3lJbkZuencxQ0tMZEJjNHJkWkx6LUJWY2o1aDRaRkNSM0lZR2I1cXJOMGNYcktHSlZnVlZ4MUxYR1RtMGZDOEkwVHBOZmpJSVZKUXZQX1lCUEE4dUs1X2k1RWFSdEpRVVhOQkVHbUZEUV83ZXUyT3NmZw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 29 Sep 2026 08:32:00 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel stock falls as chip-sector sentiment weakens and investors lock in gains - Quiver Quantitative；台灣引領全球半導體專家建議善用印度人才保優勢| 生活 - 中央社 CNA；半導體迎百年一遇擴產潮！法人喊買這家特化廠在手訂單暴增近倍- 證券 - 工商時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.26 | +1.09% | N/A | 115.93 | 127.39 | -9.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.04 | +0.61% | +0.61% | 2,475.00 | 2,475.00 | 0.00% | 未明確 | 86.28 | 28.69 | 514.81B TWD / 53.32% | 2026-09-01 |
| 2303 聯電 | 產業/供應鏈推估 | -0.05 | -4.06% | -1.60% | 153.50 | 164.50 | -6.69% | 同向 | 6.68 | 23.08 | 25.04B TWD / 30.71% | 2026-09-01 |
| NVDA 輝達 | 產業/供應鏈推估 | -0.02 | +13.18% | +7.61% | 227.21 | 227.21 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | -0.02 | +17.72% | N/A | 607.57 | 629.26 | -3.45% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | -0.02 | +9.69% | N/A | 1,065.08 | 1,080.53 | -1.43% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | -0.04 | -5.71% | -3.04% | 1,712.89 | 2,335.00 | -26.64% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -8.78% | -20.52% | 355.10 | 446.77 | -20.52% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 1 篇新聞出現相關標籤。 方向判斷命中詞：falls。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 1 篇新聞出現相關標籤。 方向判斷命中詞：falls。

### 主要來源

- [Intel stock falls as chip-sector sentiment weakens and investors lock in gains - Quiver Quantitative](https://news.google.com/rss/articles/CBMisAFBVV95cUxOSERteld6MGRfUHBZdkhtS1lSZHgxWGRNQ28wUlUzcm5iTHRQYW5WTWIzM29HZ0xSd2ZmOWNOZW01MG9RZVBXQ2hBLVlqOTA1Z2JKcGNyRnNxeE5SUzl4UkpBblNrVmkxamNOX09NZHZxUXRLX1hHZ1pMZFh2UHdsZ25mR1NqTEdCekYyUVpMUWplbzZycHNnbjhMbngzS1U1eGpxdlh4Q1NPamxzMkpEOA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 28 Sep 2026 14:50:00 GMT
- [台灣引領全球半導體專家建議善用印度人才保優勢| 生活 - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9wbDhfdWRLZGZUTWo3X1JlampDbFRWQ1F4RnVhVVFPdzhieHNQU3oyMWExVWJoTHl1a0FlY3VRTllWOUFkRnI5b1dXeFRzOHlYZl9YTENaTThXUGZ5Z1Z3?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 29 Sep 2026 09:51:00 GMT
- [半導體迎百年一遇擴產潮！法人喊買這家特化廠在手訂單暴增近倍- 證券 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1QbmhRM3JIakpBTUdxdXdBMHBJRVpEWWs3Y0trTWpkb0FJTkljdjZ0d3V2YjVBSG9vb3JYVFNZVFEyWXZFZ280RXYtZGljYWZ3S0JkQldiV0RZR3hZLVcw?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 28 Sep 2026 06:30:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：下指令要求 AI「不要產生幻覺」也無效，研究：系統設計就是「非答不可」 - TechNews 科技新報；美中 AI 競賽換跑道，從比拚最強模型轉向產業應用與基礎設施 - TechNews 科技新報；四大主流模型全中招，最新研究：AI 判定女性化用語較不專業且充滿誇張情緒 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | -0.04 | +1.09% | N/A | 115.93 | 127.39 | -9.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | -0.03 | +13.18% | +7.61% | 227.21 | 227.21 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | -0.03 | +17.72% | N/A | 607.57 | 629.26 | -3.45% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.04 | +0.61% | +0.61% | 2,475.00 | 2,475.00 | 0.00% | 未明確 | 86.28 | 28.69 | 514.81B TWD / 53.32% | 2026-09-01 |
| MSFT 微軟 | 產業/供應鏈推估 | -0.02 | +13.04% | +3.45% | 508.96 | 508.96 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -8.78% | -20.52% | 355.10 | 446.77 | -20.52% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.03 | -0.87% | +7.68% | 687.00 | 699.00 | -1.72% | 未明確 | 13.92 | 49.71 | 82.25B TWD / 45.66% | 2026-09-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.04 | -5.21% | +4.25% | 4,910.00 | 5,285.00 | -7.10% | 同向 | 60.69 | 81.09 | 64.18B TWD / 44.08% | 2026-09-01 |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：衝擊。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：衝擊。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：衝擊。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [下指令要求 AI「不要產生幻覺」也無效，研究：系統設計就是「非答不可」 - TechNews 科技新報](https://news.google.com/rss/articles/CBMixAFBVV95cUxOM2hwbS1kMEZjeFFxV2dYOGpDYXA3V0swbldiN044V0g1NnJibnc4TklVV05BNHJ2NWF4RHhjOGMxZnBGeVZFTlJnRVFlQnpJZVNGQWVNMDJOR2o1c2dhenl6eWlITDNYQjV5REdHbml4RWluMWdlUVVQcTBGY09tVG9yeDBxeXJ4TTFBOTN5UG5JMVoySkgzUFFtRmpLTTlGd2MwQkdqanN1amtOTFh3SnNUTDJ5UVY1QnVhaWZpR19yR3hO?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 30 Sep 2026 00:16:27 GMT
- [美中 AI 競賽換跑道，從比拚最強模型轉向產業應用與基礎設施 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiywFBVV95cUxQd3FuSXpsV0RoekxzdmV6UWhyR1BRZnVuWWwyYzg4QWNKMWVPdDg3bDk0TkE0bk02eFNsM2xFREhoZ3laTjZYM0lWMUx1bzh1ZWU3dDVYNFdOX3A3cjk3OHN2R0RSdHhUYlBGM1RPOWNqcWtITGhWNlJTaTAxc1NiaVJnYVVxVzlwMThPSnFTYTZQWlhfWnF5c3dDUUpTbmI3dWcyWnNSTTd1bzBIdmxnanZXYVl6RlM0X3VBUnBIUldfdENaMEtqc01NNA?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 29 Sep 2026 23:41:25 GMT
- [四大主流模型全中招，最新研究：AI 判定女性化用語較不專業且充滿誇張情緒 - TechNews 科技新報](https://news.google.com/rss/articles/CBMilAFBVV95cUxNS0I0bVJGOGdQc3NzMkZ6Y1JLRUc5QXRCalFubjVpRF9HcWtPQmtCYnI5ZjlNQ1hEV0pJVWU3V0pSRS1tQUgwamFyQU80Y0VNTWdlak9jS2ZWSHVTa3cwTERNaTNEU1FjZllscUZTeUJPOHRuMkxRSktHa2hmRWkzSVQ2RUw2U3V5V3ZKNVFHdnFQOENn?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 29 Sep 2026 23:21:23 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：《台股盤後》震盪收跌392點失守48K及5日線- 新聞 - moneydj.com；法人盤勢分析內容-台股-MoneyDJ理財網 - moneydj.com；台股中秋連假後首日開盤走弱 終場重挫392點失守48K - moneydj.com

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》震盪收跌392點失守48K及5日線- 新聞 - moneydj.com](https://news.google.com/rss/articles/CBMikgFBVV95cUxOTmhVNmhWd0VoNUx5VDYtd0xTRElOZy0yWU51dllsVTllMmNjamllaWJSeEFIRFhUOGtuWERObGxIbVBqZnQxVDBmSkhwRnRaZXNIbXlMM2NULTdURUZXR2ZvaUZrTTEzX1RpSnViNE5jamoxSFFVWkJIYW5UeTBQVDdZYW5lcVh0YkktSDd6SGlZUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 29 Sep 2026 08:06:00 GMT
- [法人盤勢分析內容-台股-MoneyDJ理財網 - moneydj.com](https://news.google.com/rss/articles/CBMijgFBVV95cUxOeHBsWHAwbVVnTkJBMVczTG1oU2tHTDc1UlBlM25hX0tLQWNCX05Ma2FGRkJMSkdfclVBVENkS25WT0hqUVFQZUxuNW12RlhmN0NBSkMtVDhlWUF0dXRmR3JmWGRtV0c0c3dCSHdDbGFDdWlMcEsyNk1RR3p5VFZRYVRkcG9XNnpGM0c0eklR?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 30 Sep 2026 00:33:51 GMT
- [台股中秋連假後首日開盤走弱 終場重挫392點失守48K - moneydj.com](https://news.google.com/rss/articles/CBMikgFBVV95cUxNeGdZcmwtd2tfbHlVZ1BjRzBlUkctbmhqZzdMalRLb2tPZ2VWMVlBZWVLNEdGblF1S1d5MXp3bEUyb0ltaVB6T1hUR3pTWDVrLXNOWi1iUzd2WWJfY0FyWEZYZXBIUE1jOUZIX3NpekQzcVhtMTZKOFRLQVJVT3Y0V05rYzZld3ZRVVp0d0doRU1ZUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 29 Sep 2026 06:32:00 GMT

## 新興題材：油價及記憶體

摘要：新興題材：油價及記憶體 相關新聞集中在：台股收跌392點失守48K 觀望地緣政治、油價及記憶體大廠股價 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股收跌392點失守48K 觀望地緣政治、油價及記憶體大廠股價 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE4zM3drVDhtcDZCaXJHb1A2cVlSdU1sMUNWeG54ZkNsUk5XSW9ORVpfQmpFalhoXzFsVVJza05RQnhiMWZLN3haSjFBbHpEX2RWcTYtTjU0a0V2d9IBX0FVX3lxTE1WdGlCd3pnYzlqZVFsZ2tsdDVSVTlhSktjQmROdFFuUHdKanRFVFpGQUE1RHJGSTNZdjBxcDktNEppX3VnVkhsdG5CMVdUZ2h5WVRhbzBURWxScEtQZkkw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 28 Sep 2026 09:00:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
