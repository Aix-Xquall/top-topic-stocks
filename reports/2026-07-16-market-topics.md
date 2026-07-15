# 每日股市熱門話題分析 - 2026-07-16

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **半導體與晶片供應鏈**｜正向｜熱度 11｜市場確認 51.81｜同向 3/5
2. **利率與成長股估值**｜正向｜熱度 5｜市場確認 N/A｜同向 0/0
3. **關稅與供應鏈轉移**｜正向｜熱度 2｜市場確認 N/A｜同向 0/0
4. **AI 伺服器與資料中心**｜正向｜熱度 14｜市場確認 5.09｜同向 1/6
5. **記憶體與 HBM 供應鏈**｜正向｜熱度 10｜市場確認 0.00｜同向 0/1

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.20（樣本 12）
- 5日相關係數：0.02（樣本 12）
- 同向比例：4/12

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 半導體與晶片供應鏈 | 51.81 | 3/5 | 1 | +3.27% | +12.71% |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 關稅與供應鏈轉移 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 5.09 | 1/6 | 2 | -2.19% | +4.17% |
| 記憶體與 HBM 供應鏈 | 0.00 | 0/1 | 1 | -15.71% | -6.49% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：投入逾4千億元推國產晶片 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-07-03 | 0.21 | 0.08 | +55.56% | 18 |
| 2026-07-04 | -0.22 | -0.36 | +22.22% | 18 |
| 2026-07-05 | -0.00 | 0.24 | +40.00% | 10 |
| 2026-07-06 | N/A | N/A | 0.00% | 2 |
| 2026-07-07 | N/A | N/A | 0.00% | 1 |
| 2026-07-08 | -0.05 | -0.05 | +71.43% | 14 |
| 2026-07-09 | -0.11 | -0.36 | +64.29% | 14 |
| 2026-07-10 | 0.55 | 0.05 | +77.78% | 9 |
| 2026-07-11 | 0.13 | -0.08 | +50.00% | 12 |
| 2026-07-12 | 0.27 | 0.13 | +16.67% | 12 |
| 2026-07-13 | 0.39 | -0.09 | +15.38% | 13 |
| 2026-07-14 | 0.10 | -0.07 | +21.43% | 14 |
| 2026-07-15 | 0.20 | -0.16 | +28.57% | 7 |
| 2026-07-16 | 0.20 | 0.02 | +33.33% | 12 |

## 歷史回測摘要

- 回測日期：2026-07-16
- 近5日 3日相關：-0.09
- 近5日 5日相關：-0.08
- 同向比例：+33.33%
- 權重狀態：未調整

- 方向準確度：+33.33%
- 信心排序準確度：-0.09
- 診斷：低相關

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

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel (INTC) Is Spending €5 Billion To Expand AI Chip Production In Ireland - simplywall.st；TSMC to post Q2 earnings as AI chip demand stays strong (TSM:NYSE) - Seeking Alpha；半導體股漲勢帶動日股收高| 證券 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.55 | N/A | N/A | 102.99 | 114.68 | -10.19% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | +0.51 | +1.04% | 0.00% | 2,440.00 | 2,440.00 | 0.00% | 同向 | 74.39 | 32.80 | 442.68B TWD / 67.87% | 2026-07-01 |
| AAPL 蘋果 | 新聞直接提及 | +0.43 | +23.97% | +41.08% | 327.50 | 327.50 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2303 聯電 | 產業/供應鏈推估 | +0.05 | +6.41% | +7.10% | 166.00 | 166.00 | 0.00% | 同向 | 4.00 | 41.71 | 23.12B TWD / 22.85% | 2026-07-01 |
| NVDA 輝達 | 產業/供應鏈推估 | +0.03 | +0.64% | +21.85% | 212.50 | 212.50 | 0.00% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.04 | N/A | N/A | 529.14 | 548.13 | -3.46% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | +0.04 | N/A | N/A | 904.28 | 983.12 | -8.02% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.02 | -15.71% | -6.49% | 1,615.00 | 2,335.00 | -30.84% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：strong, demand stays strong。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「TSMC」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip, foundry。 方向判斷命中詞：strong, demand stays strong。
- AAPL：新聞直接提及「Apple」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel (INTC) Is Spending €5 Billion To Expand AI Chip Production In Ireland - simplywall.st](https://news.google.com/rss/articles/CBMiygFBVV95cUxNcEJYNVVPOTZQdTZCdWQybEdUV1hnSDBnTVlod3ZackRraTd1ZjZUVnZCdzF4WHUzVEZTbGtpNndIWVNfQmNXNTJkQ2lVY21PQnJ3LWtUN3pLVzZGMTJEejMwQ1FZOEVfU1pKTTFkemh0M0ptcHI4bTN1QlpkUUFjWXprbkhXRm5Zb1I1MzBXOVJXckNHaXBxVHpEVS1qVWlnVDU0d0FOcEhtM1dNMGhHRjZMV3NERVNldGd6R2lVOFluY3ozQlRZNDhn0gHPAUFVX3lxTE9nVGVDLUxnamZFcVRDSUNnRTh6amFLaWYzWGpZWnFaN0lXRTlZTDByMFl5dUZJdlZQQ0dUR3RReEdpOXlPV05hZ2FLbk1ONzBTdHdYUnNtWjA0SVBYekZRUzhYOVZ6eGZIY3hOY1ZtZ2MzOWxDQ0taT0JBQVpITERySFBQdTFXVmprZEFud3hsVms5RURncWV6VWFSRVQ3cEhGM25IVTNsNXkydkc3OEJsdHk5Qm9TT2YzMTJSMmgzaGVGQ1hVRnkyazRvbUx6aw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 14 Jul 2026 17:34:02 GMT
- [TSMC to post Q2 earnings as AI chip demand stays strong (TSM:NYSE) - Seeking Alpha](https://news.google.com/rss/articles/CBMimAFBVV95cUxPbkpDdVZEbkI0TmpjSGVTd25lVTBYTHZXRnd5Vm9HX1VVU2VFR2VDTE85TjRJdnRKelVYQjFSbjVJVEZHMERrZmpTekpWMVk0b2Y4enJ1MkJaQ0E3ODdBSUthakNDMzVJbkFkZUJuNkRzOWVsRlAzQ3BHM3RtTG1HcEswR3R5VW1QLTMwcUM0eWUweTBEZzBRZQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 15 Jul 2026 16:31:51 GMT
- [半導體股漲勢帶動日股收高| 證券 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE9DeGNQQ2RJR2JWaHg4ekZNMDFKX21lZWprazR4Z0VfUTJxMEJVVWFZREJYNVkwMHJYX1NtVGNYRGx5YWt0alRNOUo3aHl2SmlTSXdGTzhPUFk1clJ3M1E?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 15 Jul 2026 06:52:00 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：Wall St ends higher on cool inflation data, strong earnings - Reuters；〈美股盤後〉通膨降溫標普連二紅 費半跌逾2% 美光、SK海力士ADR崩超8% - Yahoo股市；〈美股盤後〉通膨降溫標普連二紅 費半跌逾2% 美光、SK海力士ADR崩超8% - news.cnyes.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.51 | N/A | N/A | 904.28 | 983.12 | -8.02% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +0.74% | -21.92% | 395.63 | 506.69 | -21.92% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「美光」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Wall St ends higher on cool inflation data, strong earnings - Reuters](https://news.google.com/rss/articles/CBMiowFBVV95cUxOWUtNV3dNS0otQllnaU9ZVG83WlpzSDB0MlB4OVJFQ0V3QjRCT1BhbjRjMkdXeTFwbUwwczE2cVFkREhxSkpwZTJvZmZLUGtPYlk5Vk53cnlxSmdXZjgwb1JEZ284QmJ2SGlUSkgzRlZSQ1k4bzhaM0wzajRMbVV4bGZEaUtSOUFZVGxtRHlNYW5ucEtuRVA1Q3NpOWRXdExXYWNr?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 15 Jul 2026 21:09:18 GMT
- [〈美股盤後〉通膨降溫標普連二紅 費半跌逾2% 美光、SK海力士ADR崩超8% - Yahoo股市](https://news.google.com/rss/articles/CBMiigNBVV95cUxPZ1RDNWdBQnhjWGxPMUd0aHFqdjIySWZUUVEwQU0xODQ4YjNvbkJmNDE0WURIUnBKZnFqTnhuazc0OVlQMFEzN0hBblNXTndEU0tNbWZpQklReEpndlZlYVp6VFktb01TZHE5ZnExLUQwMjRqOFJiMi1FbHhxT19uU0NRQnRYMUFVR1ZMTE9TNU5sOUFWWXA2Ml9nRGpoZG1DQVpvOWJzX1AyQlRibml0U28tdHpwX1hFVDlUWmZiZVVlUHpRZnBhMWFNbkR2SnBNdHZoS09pWGxvSmpCZFZSR0FMM3ZVMm1BZmFwM0Z5bUo0QVNWWXBhMTBDd1k2Q3hwYTNTNXg3bmxzX0t0dEdBUG5GRVhUWDdyUm5Ba2hORzF5dF9TbzRVZFQtZjlvU2NkQjJyRmhNQjh4clVRQnpoaTItZ25RWWhsczdibzRWaV8yV1dLSXoyTGNId3NhMUpIV0lVMXFSeXNCc2tYbEZFcmxOMkNsQXBHUExTWjJfT2RoclU2VHhYUXFB?oc=5) - Google News source discovery | Yahoo 奇摩股市 Wed, 15 Jul 2026 21:32:11 GMT
- [〈美股盤後〉通膨降溫標普連二紅 費半跌逾2% 美光、SK海力士ADR崩超8% - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTE1IY3dCb1pYY0YwWlBzQzlnb1QxV2YyYWZPVF9RN1hxN1JQSnNLYVJBNXFkSUpOajlHdGs4VjFmS3N0bUNwcE13RW1RSjUyNEE?oc=5) - Google News source discovery | 鉅亨網 Wed, 15 Jul 2026 21:32:12 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：功率半導體迎新成長循環環球晶、合晶等台廠供應鏈布局一次看- 日報 - 工商時報；7／15盤前｜功率半導體上下游台廠供應鏈一條龍各家布局解析- 證券 - 工商時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +23.97% | +41.08% | 327.50 | 327.50 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | +0.63% | +0.84% | 239.00 | 289.00 | -17.30% | 不適用 | 14.13 | 16.97 | 821.76B TWD / 52.11% | 2026-07-01 |

關聯理由（前 3）：
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [功率半導體迎新成長循環環球晶、合晶等台廠供應鏈布局一次看- 日報 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBvZXhKc1ppNkR5bTNxcjVEWHIyTDQ0eTFYZXlSRFN1UnMyMW1FVnJBS25HMGx1S1haU3FGTTZnYnFlRnU0bzJ3ZFA1V0Q3NmpWeEF2b2FXSjU4eWxxRUZJ?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 14 Jul 2026 19:00:00 GMT
- [7／15盤前｜功率半導體上下游台廠供應鏈一條龍各家布局解析- 證券 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5yZkpRSU5MX0pRMERuWmhQM21vQVhfYUp2XzZVNllkRnhlYmhoTHM4Tm1fQXkwcE9XVURnTWQ0YTgzTFBUcUNqdXlxcWhrc09JbFQ0d1BlNVlBa05UNXJj?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 14 Jul 2026 23:26:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel (INTC) Is Spending €5 Billion To Expand AI Chip Production In Ireland - simplywall.st；TSMC to post Q2 earnings as AI chip demand stays strong (TSM:NYSE) - Seeking Alpha；AI 帶旺第三類半導體，台灣上游材料廠迎新商機 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.56 | N/A | N/A | 102.99 | 114.68 | -10.19% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | +0.54 | +1.04% | 0.00% | 2,440.00 | 2,440.00 | 0.00% | 同向 | 74.39 | 32.80 | 442.68B TWD / 67.87% | 2026-07-01 |
| NVDA 輝達 | 產業/供應鏈推估 | +0.04 | +0.64% | +21.85% | 212.50 | 212.50 | 0.00% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.06 | N/A | N/A | 529.14 | 548.13 | -3.46% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 產業/供應鏈推估 | +0.03 | +0.74% | -21.92% | 395.63 | 506.69 | -21.92% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -11.75% | +27.39% | 394.28 | 446.77 | -11.75% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.03 | +0.89% | +4.92% | 683.00 | 683.00 | 0.00% | 未明確 | 10.86 | 63.42 | 65.78B TWD / 32.86% | 2026-07-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.02 | -4.71% | -7.20% | 3,740.00 | 4,310.00 | -13.23% | 背離 | 62.91 | 59.60 | 58.01B TWD / 2.80% | 2026-07-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：strong, demand stays strong, 成長。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「TSMC」，共 1 篇新聞命中。 同時符合主題標籤：AI, advanced packaging, CoWoS, AI server。 方向判斷命中詞：strong, demand stays strong, 成長。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：strong, demand stays strong, 成長。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel (INTC) Is Spending €5 Billion To Expand AI Chip Production In Ireland - simplywall.st](https://news.google.com/rss/articles/CBMiygFBVV95cUxNcEJYNVVPOTZQdTZCdWQybEdUV1hnSDBnTVlod3ZackRraTd1ZjZUVnZCdzF4WHUzVEZTbGtpNndIWVNfQmNXNTJkQ2lVY21PQnJ3LWtUN3pLVzZGMTJEejMwQ1FZOEVfU1pKTTFkemh0M0ptcHI4bTN1QlpkUUFjWXprbkhXRm5Zb1I1MzBXOVJXckNHaXBxVHpEVS1qVWlnVDU0d0FOcEhtM1dNMGhHRjZMV3NERVNldGd6R2lVOFluY3ozQlRZNDhn0gHPAUFVX3lxTE9nVGVDLUxnamZFcVRDSUNnRTh6amFLaWYzWGpZWnFaN0lXRTlZTDByMFl5dUZJdlZQQ0dUR3RReEdpOXlPV05hZ2FLbk1ONzBTdHdYUnNtWjA0SVBYekZRUzhYOVZ6eGZIY3hOY1ZtZ2MzOWxDQ0taT0JBQVpITERySFBQdTFXVmprZEFud3hsVms5RURncWV6VWFSRVQ3cEhGM25IVTNsNXkydkc3OEJsdHk5Qm9TT2YzMTJSMmgzaGVGQ1hVRnkyazRvbUx6aw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 14 Jul 2026 17:34:02 GMT
- [TSMC to post Q2 earnings as AI chip demand stays strong (TSM:NYSE) - Seeking Alpha](https://news.google.com/rss/articles/CBMimAFBVV95cUxPbkpDdVZEbkI0TmpjSGVTd25lVTBYTHZXRnd5Vm9HX1VVU2VFR2VDTE85TjRJdnRKelVYQjFSbjVJVEZHMERrZmpTekpWMVk0b2Y4enJ1MkJaQ0E3ODdBSUthakNDMzVJbkFkZUJuNkRzOWVsRlAzQ3BHM3RtTG1HcEswR3R5VW1QLTMwcUM0eWUweTBEZzBRZQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 15 Jul 2026 16:31:51 GMT
- [AI 帶旺第三類半導體，台灣上游材料廠迎新商機 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiuAFBVV95cUxOMVhMX1o0OExGaW1fdlhvYmN0REw2ODJMRTNraUY5QXdaX0RqU3JLUmRkdGpuWlQwclZJdXloOUtXbkhtZldhVkthNzQ1d3hCWENOdUJaVU8wb3dsNlZxM0c1bHdScXFKUGxxN2x0Nlp4LVU0V3R6U0FSVGx6TVJFVEFxLXdOU2dYQ1VyRGEzSjhUMGJqQU02YVN3UHlrMV9yUTdDU3lpY3BpS0xNdmVMNEpyRHF1YWZD?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 15 Jul 2026 09:50:35 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：AI memory, chip stocks fall again after brief recovery despite strong ASML results - Seeking Alpha；Micron vs SanDisk: Which Memory Play Wins the AI Boom? - 24/7 Wall St.；Micron vs SanDisk: Which Memory Play Wins the AI Boom? - AOL.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.50 | N/A | N/A | 904.28 | 983.12 | -8.02% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.25 | -15.71% | -6.49% | 1,615.00 | 2,335.00 | -30.84% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +0.64% | +21.85% | 212.50 | 212.50 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「memory、Micron」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：fall, rally, strong, surges。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 4 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：fall, rally, strong, surges。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AI memory, chip stocks fall again after brief recovery despite strong ASML results - Seeking Alpha](https://news.google.com/rss/articles/CBMiuwFBVV95cUxPR3lHUGNsWmpmTWNFM2FieFNGVUl6ZW9yUF9FZWtHZ2tNZl9COHJaT2hFOHVFMklnUkk3dmVGVFB2dWdXdEZVNHc4S2xFOHdhQTRyVTk1NWJTZWtGeENicEtFSENKNEk4YXB2YUFDTXpSbHEwWjFTaGNScXBBMW9EQ3E0UTFPMU5MM1NmTzRpQTUwLVk1cEpoV2JwR2JmRmZkUDI5VUZBdVpUT2E2amlYRm12Vlg2RkEtNEZ3?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 15 Jul 2026 15:38:01 GMT
- [Micron vs SanDisk: Which Memory Play Wins the AI Boom? - 24/7 Wall St.](https://news.google.com/rss/articles/CBMinAFBVV95cUxNT1JxOGlOMHV0Mkg3cUFFMUxVSVBVRUpVcmdwallSZWFYOU85YXo2ZG5qTTgzOXVuYXJ2YU5sbldYRm1wQW5mSzVQOHJNZmV0eHVFYm4ycXdPQnpxUURGRGpEZlJKT2dDMnpwMnpzeDhFY0VVcVYwRXozWEQwYzVseTJjUUlDbVdIaEF1bndRWWw0UG51NmdPNERPZ2U?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 15 Jul 2026 16:30:33 GMT
- [Micron vs SanDisk: Which Memory Play Wins the AI Boom? - AOL.com](https://news.google.com/rss/articles/CBMifkFVX3lxTE9QTzlzYnRpWXlOWjVQNkhmb0xOZVg0TWN1eGZZbFFJLUtVU2kzVm5NWW1QbUd4bEwzYVlTdGhLRGRCZ3laMXhodEpnR21RZzI1M1dNX3hTUUtOcmJOUzZsY1A0UEwyaFhfS2phdXplRzRfeUR6S2szc3NKbEdOUQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 15 Jul 2026 16:56:20 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股強彈玩真的還是死貓跳？分析師曝後市：布局重點「挑這些」 - 經濟日報；台股強揚 千金俱樂部增至51檔 - 經濟日報；台股高檔震盪加劇 法人連買強勢股具領漲抗跌優勢 | 市場焦點 | 證券 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股強彈玩真的還是死貓跳？分析師曝後市：布局重點「挑這些」 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBhOC1NR1JiMDdwVGxvQWlMeENSVzBCSkMzZzVJaTRCTm1OQkw2YzNMTk9nWV8tN2ZWUnZmOXAxV184QnNyNTBsZ1AybExwSHA3LVpzSW9uLUxSQdIBX0FVX3lxTFBwcFF0Z2xTN1l3UDN6bE1IZnBBSDN2aE44UTRkRDFUQ2xKai1qa0VSVWdHck16MVZLdjR4ZFQ3UUlsMVY2Wm1sY1VGNEJ5YkZabkF3NlNDVFMzNzhMS0Fv?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 14 Jul 2026 09:00:00 GMT
- [台股強揚 千金俱樂部增至51檔 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxPZEZpcUpHSHNLT05NYXBrMTBfakdFV1ZabjhBdDEtY09LY19fZ1hfTXNzNGdhb1ZvZngtTFJkYlBOZUNqWEUxTTJQRjZjSmVQdVY2bFhPR1JQbDdFMTJHRVF5ZTZaNE5NMmo2bGJ4M181S1RuSlJTTGhwcjVYX0FEM9IBX0FVX3lxTE94YmVmUGYyUVVhSW5qUVlVLUxYNWVXeDRkNnlROVppYy1hTVpEenFPRDVGSERuYkhVYWZIYUhwTkl4dWgxQ2ZtelFhWmhzak9LVnlBWV90R1ZYSVp3b3I0?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 14 Jul 2026 09:00:00 GMT
- [台股高檔震盪加劇 法人連買強勢股具領漲抗跌優勢 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFB6VnpVc1AxTnowMTFGdGRUM3gyUWR0bm82S0JpQnJqT21EaGFvei1GaXBfcEw2cXV6VjQ2Z3pJVmVxd0ViM0dWSEp5VzZfMHVkaFBkNG1jUlByUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 15 Jul 2026 13:45:24 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》開高走高、收漲893點，收復5日線- 新聞 - MoneyDJ；《台股盤後》開高走高、收漲893點，收復5日線-新聞內容-基金 - MoneyDJ；息收有助抗震17檔台股ETF明日除息- 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》開高走高、收漲893點，收復5日線- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPY2h6WnNRNU1VN2tMa0pvRGpSWkRFeHhOckRGSlhGTjFDM0JnZWhVYjNyckJRMEs5RDI2aEpMNzJlekpod2xmd2U0ZExLYjUyb29oZjNVMlJzMXpiNktSV0dxQXJNWmY5ZkZmQ1hFNlNiNDF1VVZCZVpCNTVOU3VRNkRJQVJkUy1ibzRHYWN2eGRrZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 15 Jul 2026 07:55:00 GMT
- [《台股盤後》開高走高、收漲893點，收復5日線-新聞內容-基金 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxPeWQzazFCSm15YnE4ZjhKLURrb3RseFZvRG03Nm9LTUlVRm1Qc2hxaEx6dXF5cFcwTExKUTl1M0VJVDQ4V2luTEZPdXJGV2xwaVZod3A5dEdiQUg0VXN1NXpSbkN3eXpjUUQ0N0Y5b1FYZWctaUQ4QTFPcjAxQk91VHZpU2MzOG5iQ0pMdUxlUXU?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 15 Jul 2026 07:57:00 GMT
- [息收有助抗震17檔台股ETF明日除息- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxOZkphSFZRNGNhU1phV1Q5ZS10ZHNzeTRSNzRBbnRLYXBkekM2ejJRbXdBV0EtMzNPX19Rb3RuTUFab0M3OXZMYkNJT2RGWDhZOFpCeUMzUkVLazJrSUxPTUtMNWdZdkdhN1ZnQjd5T2ZaRi03TER6QmR3MG9oQzVKTmpGbzltV3FRNFJUS09ZSzRZdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 15 Jul 2026 02:34:00 GMT

## 新興題材：投入逾4千億元推國產晶片

摘要：新興題材：投入逾4千億元推國產晶片 相關新聞集中在：印度核准半導體2.0計畫投入逾4千億元推國產晶片| 國際 - 中央社 CNA

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [印度核准半導體2.0計畫投入逾4千億元推國產晶片| 國際 - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBpT0xhTUhWcDZIc2lScHA5OEV1SmIza1ItaG1kRmtNcGFPWVpwN2hPWTkxRTBibUdRa0RuZ0dJdE1YOXc4ak1oakpDNjNaWTlMeWlzYnJVcXZqYjNORjhN?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 15 Jul 2026 13:49:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
