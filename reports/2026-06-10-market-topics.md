# 每日股市熱門話題分析 - 2026-06-10

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **散熱與液冷供應鏈**｜負向｜熱度 2｜市場確認 88.27｜同向 1/1
2. **利率與成長股估值**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
3. **半導體與晶片供應鏈**｜負向｜熱度 7｜市場確認 47.71｜同向 3/5
4. **AI 伺服器與資料中心**｜正向｜熱度 14｜市場確認 32.30｜同向 3/6
5. **新興題材：StocksToTrade**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.17（樣本 13）
- 5日相關係數：0.15（樣本 13）
- 同向比例：7/13

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 散熱與液冷供應鏈 | 88.27 | 1/1 | 0 | +6.09% | +5.74% |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | 47.71 | 3/5 | 2 | +1.90% | -4.62% |
| AI 伺服器與資料中心 | 32.30 | 3/6 | 3 | -0.90% | +2.00% |
| 新興題材：StocksToTrade | N/A | 0/0 | 0 | N/A | N/A |
| 記憶體與 HBM 供應鏈 | 0.00 | 0/1 | 1 | -6.43% | -4.07% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：SpaceX | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-05-28 | 0.14 | -0.07 | +88.89% | 9 |
| 2026-05-29 | 0.14 | -0.04 | +71.43% | 7 |
| 2026-05-30 | 0.16 | -0.06 | +71.43% | 7 |
| 2026-05-31 | 0.96 | 0.09 | +100.00% | 3 |
| 2026-06-01 | -0.92 | -0.72 | +16.67% | 6 |
| 2026-06-02 | 0.08 | 0.05 | +72.73% | 11 |
| 2026-06-03 | 0.48 | 0.62 | +90.91% | 11 |
| 2026-06-04 | -0.38 | -0.30 | +85.71% | 7 |
| 2026-06-05 | 0.31 | 0.93 | +50.00% | 6 |
| 2026-06-06 | 0.12 | 0.06 | +45.45% | 11 |
| 2026-06-07 | -0.32 | -0.20 | +45.45% | 11 |
| 2026-06-08 | 0.36 | -0.68 | +60.00% | 5 |
| 2026-06-09 | 0.07 | 0.19 | +25.00% | 8 |
| 2026-06-10 | 0.17 | 0.15 | +53.85% | 13 |

## 歷史回測摘要

- 回測日期：2026-06-10
- 近5日 3日相關：0.26
- 近5日 5日相關：0.15
- 同向比例：+50.00%
- 權重狀態：未調整

- 方向準確度：+50.00%
- 信心排序準確度：0.26
- 診斷：正相關

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

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：液冷向前衝散熱族群成績單亮眼奇鋐、雙鴻年增逾6成 富世達創同期新高- 日報 - 工商時報；3017 奇鋐- 黃仁勳曝「Rubin不用冷水機組」衝擊散熱股大摩建議逢低- 股市爆料同學會 - CMoney

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | -0.64 | -6.09% | -5.74% | 2,545.00 | 2,835.00 | -10.23% | 同向 | 61.06 | N/A | 15.87B TWD / 60.64% | 2026-06-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐、3017」，共 2 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：衝擊。

### 主要來源

- [液冷向前衝散熱族群成績單亮眼奇鋐、雙鴻年增逾6成 富世達創同期新高- 日報 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1rUUt1SC1MN19DNDVwbng1bk5PVDRsR2tEeEc5a01IMnFNLTdheVVUVl9MNWZodVlvak1pbXJGRFRVUllLTHNaUk9URDJkRXFnNy1ibWFyZ2FDNXV5TVU0?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 08 Jun 2026 19:00:00 GMT
- [3017 奇鋐- 黃仁勳曝「Rubin不用冷水機組」衝擊散熱股大摩建議逢低- 股市爆料同學會 - CMoney](https://news.google.com/rss/articles/CBMiXEFVX3lxTE5fMGxOX1loNC1oUlBxd0tFOFU2MEY2Y255amxRSWlWbFRad1ktQVBDRTVDUHJiTFZZZjM1LVJpUVpjUU9zT1VmeTJna1RNZFFSMDVqSEZCYnhpMGZv?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 08 Jun 2026 18:34:53 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：台股長線多頭未終結 法人點出這波回檔是「估值修正與擠泡沫」 - 經濟日報；美股收盤／美股劇烈震盪 科技股領跌 市場緊盯 SpaceX 上市與通膨數據 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +2.72% | -20.38% | 403.41 | 506.69 | -20.38% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [台股長線多頭未終結 法人點出這波回檔是「估值修正與擠泡沫」 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5fS0tMV2xEbVhBYVR1SHh4S0kyQUxwcXVWazZQUmdpSlZiZEc5SHVSTG1RVFJIVE5zUzl1eVdFTHg1cWxqUnBkNWRqNE9MUzFLS3Jud2FfUHdkZ9IBX0FVX3lxTFB2OTR5b2k2SkxRQ0FBdlp1TEFTdlhQVGxjVkJPQkx5M3RGRVlJOTVOQTVqc0lXaVJ1RW5oX0VTWGowYmQwUklhYnZHY01QaWd4S0tfdmc2TkJLc3B0bTNj?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 08 Jun 2026 17:40:14 GMT
- [美股收盤／美股劇烈震盪 科技股領跌 市場緊盯 SpaceX 上市與通膨數據 - 經濟日報](https://news.google.com/rss/articles/CBMiekFVX3lxTE1nQWNndlUzeFNCbTc2NGxWdExNbTM3QUtKeU1XVDhTc2FDbXZJWk0tUlNhemlmeWlPckFBaHZvWndIZzJYcm0zb3FWN2dpQjlKQTdsSWp1amdtRTVkY3V6cjU4d0FUTV8ydmEtTlNjS01ZTGNhZ2RYRWNR0gFiQVVfeXFMTkxMWDRiazVPX0JTZWJhX0hzNUZxY01JMnIwZ3BXR2QzcUhTUWlHSDJia0lNLXZRM1hJR1p5RkY4SHhRNE5vN0JUM2JDYk4ybWw2MWdOYmNRbjM5Zmp5dDc0cUE?oc=5) - Google News source discovery | 經濟日報 money Tue, 09 Jun 2026 22:54:19 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：AMD Sinks 9%, Intel Slides 8% as Chip Stocks Pull the NASDAQ 100 Down - 24/7 Wall St.；Broadcom Sinks 14% on Soft AI Chip Outlook Despite Earnings Beat, Dragging Down AMD and Intel - AOL.com；Semiconductor shorts pile on as winning trade reverses - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.72 | N/A | N/A | 107.92 | 114.68 | -5.89% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.72 | N/A | N/A | 475.51 | 516.10 | -7.87% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | -0.63 | -6.05% | +22.72% | 392.16 | 446.77 | -12.22% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.05 | -3.35% | -3.15% | 2,305.00 | 2,355.00 | -2.12% | 同向 | 74.39 | N/A | 410.73B TWD / 17.50% | 2026-05-01 |
| 2303 聯電 | 產業/供應鏈推估 | -0.03 | +2.00% | -9.89% | 127.50 | 144.50 | -11.76% | 背離 | 4.00 | N/A | 22.94B TWD / 17.78% | 2026-06-01 |
| NVDA 輝達 | 產業/供應鏈推估 | -0.02 | +4.32% | +17.50% | 208.19 | 211.14 | -1.40% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | -0.04 | N/A | N/A | 935.89 | 971.00 | -3.62% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | -0.04 | -6.43% | -4.07% | 1,646.54 | 1,831.50 | -10.10% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AVGO：新聞直接提及「Broadcom」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AMD Sinks 9%, Intel Slides 8% as Chip Stocks Pull the NASDAQ 100 Down - 24/7 Wall St.](https://news.google.com/rss/articles/CBMirwFBVV95cUxOWnprSDRab21rWGp4V0NkZjE5WXhIMzJSdUxKQmlTWVd3V0M1bXljeFRXdnh3TENqdzhucHU4V09nUHcyM2xlWWhWRE0wa2NFZFpmSWZZdVg1VWJxcWxVWXRnRTZhazNHT212Z0FaSExPb0RVOTVzY0kyLUc1Vm1FZ254dFVHLXNOM1dDZEo2U2lsZ1ZqS0NvNmFOVVNyNmc3bUZ0NHgyeTdSN2d5ZDY4?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 09 Jun 2026 16:28:24 GMT
- [Broadcom Sinks 14% on Soft AI Chip Outlook Despite Earnings Beat, Dragging Down AMD and Intel - AOL.com](https://news.google.com/rss/articles/CBMieEFVX3lxTE9kWlRUalB6cmJkd3ctZVQza1J5SXNTd1MtLVRWaEJYMUlvZE41TUtFbmd0ZXVyV0d3eTg3YmJtTHVxSENTRl9YZzRGY09Jc2pNczU1ZGRxZTNJYjd4d2IxdFgydWJwSzdQR2NQN2RmbE5pNUlYQUctbg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 09 Jun 2026 12:09:45 GMT
- [Semiconductor shorts pile on as winning trade reverses - CNBC](https://news.google.com/rss/articles/CBMilgFBVV95cUxQcndqdlAwamNHQUYtYnpsWmhBZ3dWeTd6WDRlNnpZWV83NjZHaVFvQTBaVEhZbEZjc0NDSmRXYVItUktaUFJJTFdrTjdHSnY4aDU1NlljNFlOMXVwTVZfT0lHTTliTi0wQzRleGxDMWw1cXprR0pTbWpvY0RnQ3VBVktqaW1vVXBKcmhQU045WFhPSk1RSGfSAZsBQVVfeXFMUEtjX3lXSXhPaG9NWkpMRlRrWXFHMmlRVEZrMmpUcmJWQzBXQXNqOVRmRUN0eXU5Zkk2OWdPOXBMM1o5LVcwLUo2ZWM3NUlJRmpBUkpVYVBRNWhiUTc2a3BJal8tcnBIbHdoblc0WmdPcW5DOHBLb1FrXzZ5c3BHYXVId3dPZThySUxfd3YtSUYxd2VxdVFDTkw3Q00?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 09 Jun 2026 18:26:25 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Broadcom Sinks 14% on Soft AI Chip Outlook Despite Earnings Beat, Dragging Down AMD and Intel - AOL.com；AI 推升 GDP，台灣經濟高速期多久？ - TechNews 科技新報；COMPUTEX 2026：研華攜手 NVIDIA 推 AI Factory Brain，從設備商上攻營運平台的戰略卡位 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.69 | +4.32% | +17.50% | 208.19 | 211.14 | -1.40% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.69 | N/A | N/A | 107.92 | 114.68 | -5.89% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.67 | N/A | N/A | 475.51 | 516.10 | -7.87% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | +0.32 | -6.05% | +22.72% | 392.16 | 446.77 | -12.22% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.03 | -3.35% | -3.15% | 2,305.00 | 2,355.00 | -2.12% | 背離 | 74.39 | N/A | 410.73B TWD / 17.50% | 2026-05-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | +2.72% | -20.38% | 403.41 | 506.69 | -20.38% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.02 | -4.05% | -3.56% | 569.00 | 611.00 | -6.87% | 背離 | 10.86 | N/A | 63.03B TWD / 28.57% | 2026-06-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.04 | +1.02% | -1.10% | 4,475.00 | 4,475.00 | 0.00% | 同向 | 62.91 | N/A | 46.74B TWD / -4.14% | 2026-05-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Broadcom Sinks 14% on Soft AI Chip Outlook Despite Earnings Beat, Dragging Down AMD and Intel - AOL.com](https://news.google.com/rss/articles/CBMieEFVX3lxTE9kWlRUalB6cmJkd3ctZVQza1J5SXNTd1MtLVRWaEJYMUlvZE41TUtFbmd0ZXVyV0d3eTg3YmJtTHVxSENTRl9YZzRGY09Jc2pNczU1ZGRxZTNJYjd4d2IxdFgydWJwSzdQR2NQN2RmbE5pNUlYQUctbg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 09 Jun 2026 12:09:45 GMT
- [AI 推升 GDP，台灣經濟高速期多久？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMigwFBVV95cUxNeTFFYm5XQ1VGa2o3VERGOU5KSDBoS0VYam9tOVlnbmJzTzNZdmFpV29LQVBzdDFXS1JtUTdUY1NxLV9IeHlFUko2c0JuTm9BUGhJdVFLSWcwcFZkblAxb0Mzb3BxVzNIcndXTE8zQzNBXzJLbUZFM2JvUi0zTU5uUV9ldw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 09 Jun 2026 17:24:35 GMT
- [COMPUTEX 2026：研華攜手 NVIDIA 推 AI Factory Brain，從設備商上攻營運平台的戰略卡位 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiuAFBVV95cUxNd19DX203MTB3dnNPNHM3QWN6RjM1cTRSc0pzWmg2Q3lhbkN3OW53RTViZjVZY1d3azVvVzRBUGpPOTF3ZFNPeWtoVWE5dWJCVTV6MklTM29RclZqaVIzWW1qM1lPaGROOXQ4cTRSdEJkTVFJZ3drTUd3NEdVTmVEM3lqRlhCQm10a2FENlFmQmtUNldHOXhra0FaMlBMdkwzN3M4cnBYSUNpbWVTc1V3X1IzcWdUc18x?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 09 Jun 2026 23:01:32 GMT

## 新興題材：StocksToTrade

摘要：新興題材：StocksToTrade 相關新聞集中在：Intel Stock Pops As AI Partnerships, Price Targets Climb - StocksToTrade

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 107.92 | 114.68 | -5.89% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Stock Pops As AI Partnerships, Price Targets Climb - StocksToTrade](https://news.google.com/rss/articles/CBMifEFVX3lxTFA5eHgyY0JnTW5jSWMwM2Z2dG91cTY5NE5BZGd1eDA1anBUVnNaSmlpdDVfY3JVS2NZa2hlR2xMcFVHd1ExdzJFRnZNMFZtelFHdThOS3dUX0tERlA1bEgtWUp4d3g2S3o5U0h3MEVHSUlrdFhIRGNnOWtWYTc?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 08 Jun 2026 16:33:00 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Prediction: This Artificial Intelligence (AI) Chip Stock Will Soar After Micron's Earnings - AOL.com；SanDisk (SNDK) Is Doing Something Unprecedented In The Al Sector! SNDK STOCK PODCAST ANALYSIS BUY Jobe Bellingham (gRMiCAoJ7a) - Mshale；Micron Rockets 8%, Western Digital Surges 7%, SanDisk Pops 6% in Memory-Stock Snap-Back - 24/7 Wall St.

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| SNDK SanDisk | 新聞直接提及 | +0.36 | -6.43% | -4.07% | 1,646.54 | 1,831.50 | -10.10% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 新聞直接提及 | +0.72 | N/A | N/A | 935.89 | 971.00 | -3.62% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +4.32% | +17.50% | 208.19 | 211.14 | -1.40% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- SNDK：新聞直接提及「SNDK、SanDisk」，共 5 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：surge, surges, rockets。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- MU：新聞直接提及「Micron、memory」，共 4 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：surge, surges, rockets。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Prediction: This Artificial Intelligence (AI) Chip Stock Will Soar After Micron's Earnings - AOL.com](https://news.google.com/rss/articles/CBMijwFBVV95cUxOSEhSXzJEMVRhX285dDczR0hQR0NtNXdQWVl5c3Q2SGNHSjk2azBCSjNUVGtSSXJyOVJ5ODlKYkNBRkVBTUdCUE5pTUkzWTA4dUp1Z2Y2TGt0cTFVYjlSOWRNZ0I0cFc3M3dsemlvSjJmOTM0bFBmZXBreEpsdUJ1MGtESnBhT3ZOaDE3SWp2RQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 09 Jun 2026 16:58:06 GMT
- [SanDisk (SNDK) Is Doing Something Unprecedented In The Al Sector! SNDK STOCK PODCAST ANALYSIS BUY Jobe Bellingham (gRMiCAoJ7a) - Mshale](https://news.google.com/rss/articles/CBMiW0FVX3lxTE82c25ZNkhMbnBFcHlYZktjT2gzRlFzREd4ZFlubTJYeG4zZFJ6NU1OdGxaX3BRYWM0bFdDWk5tMlNVS3BvWXRLZW1jUVp3SUdNYXlKam5zNEhNVm8?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 09 Jun 2026 10:56:00 GMT
- [Micron Rockets 8%, Western Digital Surges 7%, SanDisk Pops 6% in Memory-Stock Snap-Back - 24/7 Wall St.](https://news.google.com/rss/articles/CBMixAFBVV95cUxOTVlDSTFqRzVLYW91RjZOLUVOZnhQS0swOElKWGNKZEpiNTR0ZkhkRnNNaGgySVZ0ZC1faFdlZTBBVXJWLTJJWktZRjY1cXpsT0pycGZjWVJHcnJQanFzeXdlUk5yczExclI5SkN4M0t0d0xnUlJ3TmFFV1hHcmNLRjBpUm5sWWpnVW5CU0FORGRKSXk0ZTJZSWRpVEdQeTRmc0dDYWFXNkFpTnhSZTcxdFdiU3BNSXNjVlUzSUNuR014aFdH?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 08 Jun 2026 13:30:32 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：《台股盤後》10日線承壓、收漲1201點，重返44K - MoneyDJ理財網；個股動態報導內容-F60ADFE1-5EF0-4401-9F36-0426B77555BA - MoneyDJ理財網；統一證券：台股屬籌碼整理期，需由時間換取空間- 新聞 - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》10日線承壓、收漲1201點，重返44K - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikgFBVV95cUxQTlVZRC1oVks2Q1BGYTVzblR4MmJUZmtRTExPU180amZwbEhReUtzc0J1MUF5TmxKazBUa3M1akhVcXlYTEs2TjEzVHBpRnlmYVlRM3Z4R3hzU2V4SndOZmRKaHRsTS1iUjU5MGkwdmotanM1X2JNNmFhOGFFb2o5WmN0Z1huOGJ1V1ZXbFAzOW9Idw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 09 Jun 2026 08:09:00 GMT
- [個股動態報導內容-F60ADFE1-5EF0-4401-9F36-0426B77555BA - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilAFBVV95cUxQM1lKMmtLeG93Vy1NZXluVUJaNC14c094ZU1iNmtJUV9UOEcxSEZmaHA1UXh5aHpPM2tmZnVhVlRGUzZyQnlXM2t1OG1iYi1HdC1wWGpFcG9iQ21teUpNNWczMENQdTdmSzMyMkJMdGZsMm9WVkZvSWxIczJDSEM0NW9YWmptRzhqa0drVmJ0eXpEVXJK?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 09 Jun 2026 11:31:27 GMT
- [統一證券：台股屬籌碼整理期，需由時間換取空間- 新聞 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikgFBVV95cUxNdU51bEN5dzNVbGFPV25XNDNHeHQ1UmZOa1cwYTJuVUJqVUpVVmJiMDBoZUc5OERISVlSMEhJOXFyTklUS0tSTG81SjhfbjI1aEowUzRZRnk3RUVzVEwxRkpXQXBiUnNZY0VmTnVvM1dUc2R5T1BmajBDZ0Y5UzBnT0o4Tkl0QTNjWHFubkFvUFMxQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 09 Jun 2026 00:40:00 GMT

## 新興題材：SpaceX

摘要：新興題材：SpaceX 相關新聞集中在：AI coding startup Cursor, courted by SpaceX, picks London as European hub - Reuters；美股收盤／美股劇烈震盪 科技股領跌 市場緊盯 SpaceX 上市與通膨數據 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [AI coding startup Cursor, courted by SpaceX, picks London as European hub - Reuters](https://news.google.com/rss/articles/CBMiswFBVV95cUxNRGVPNnBjVDRKckFQa0pKZ0FEV1NNQUduWVR0c0RXQ2d2UV9COWotdXVOWDNuSUMybGdscTk0b1N4cVExQy1DWHhYZmo5SFZLSlFwc21qTzAzYVVTb1ZDTVFIWnRiLWk0MmxQbDRtZ2hCVHFfV0VwQ3dDYnNkaGowVnFTYnJ4dlBmMUowX3AybTlEUkFrZllSQ2FVdHUxYWNEbHJib0pGdjl3eDIwbzBMakNBNA?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 09 Jun 2026 05:01:00 GMT
- [美股收盤／美股劇烈震盪 科技股領跌 市場緊盯 SpaceX 上市與通膨數據 - 經濟日報](https://news.google.com/rss/articles/CBMiekFVX3lxTE1nQWNndlUzeFNCbTc2NGxWdExNbTM3QUtKeU1XVDhTc2FDbXZJWk0tUlNhemlmeWlPckFBaHZvWndIZzJYcm0zb3FWN2dpQjlKQTdsSWp1amdtRTVkY3V6cjU4d0FUTV8ydmEtTlNjS01ZTGNhZ2RYRWNR0gFiQVVfeXFMTkxMWDRiazVPX0JTZWJhX0hzNUZxY01JMnIwZ3BXR2QzcUhTUWlHSDJia0lNLXZRM1hJR1p5RkY4SHhRNE5vN0JUM2JDYk4ybWw2MWdOYmNRbjM5Zmp5dDc0cUE?oc=5) - Google News source discovery | 經濟日報 money Tue, 09 Jun 2026 22:54:19 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
- TWSE PER/PBR 抓取失敗：Expecting value: line 1 column 1 (char 0)
