# 每日股市熱門話題分析 - 2026-11-18

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **綜合市場情緒**｜負向｜熱度 49｜市場確認 73.89｜同向 2/3
2. **AI 伺服器與資料中心**｜負向｜熱度 16｜市場確認 82.50｜同向 6/8
3. **半導體與晶片供應鏈**｜中性｜熱度 10｜市場確認 100.00｜同向 8/8
4. **記憶體與 HBM 供應鏈**｜負向｜熱度 7｜市場確認 100.00｜同向 3/3
5. **關稅與供應鏈轉移**｜負向｜熱度 3｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.27（樣本 22）
- 5日相關係數：-0.38（樣本 18）
- 同向比例：19/22

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 綜合市場情緒 | 73.89 | 2/3 | 1 | +9.07% | -17.85% |
| AI 伺服器與資料中心 | 82.50 | 6/8 | 1 | +11.92% | +2.10% |
| 半導體與晶片供應鏈 | 100.00 | 8/8 | 0 | +18.30% | +3.20% |
| 記憶體與 HBM 供應鏈 | 100.00 | 3/3 | 0 | +24.51% | +14.93% |
| 關稅與供應鏈轉移 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：變現需求 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：AI供應鏈 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-11-04 | -0.21 | 0.35 | +15.79% | 19 |
| 2026-11-05 | 0.13 | -0.53 | +66.67% | 12 |
| 2026-11-06 | -0.18 | 0.77 | +100.00% | 5 |
| 2026-11-08 | -0.21 | 0.03 | +23.08% | 13 |
| 2026-11-09 | -0.56 | -0.62 | +60.00% | 10 |
| 2026-11-10 | -0.32 | 0.24 | +3.45% | 29 |
| 2026-11-11 | 0.34 | -0.26 | +46.67% | 15 |
| 2026-11-12 | -0.09 | 0.07 | +50.00% | 14 |
| 2026-11-13 | -0.56 | 0.42 | +54.17% | 24 |
| 2026-11-14 | -0.34 | 0.12 | +42.11% | 19 |
| 2026-11-15 | -0.02 | 0.62 | +50.00% | 20 |
| 2026-11-16 | -0.30 | -0.27 | +38.89% | 18 |
| 2026-11-17 | 0.44 | 0.39 | +80.00% | 15 |
| 2026-11-18 | 0.27 | -0.38 | +86.36% | 22 |

## 歷史回測摘要

- 回測日期：2026-11-18
- 近5日 3日相關：0.06
- 近5日 5日相關：0.08
- 同向比例：+56.00%
- 權重狀態：未調整

- 方向準確度：+56.00%
- 信心排序準確度：0.06
- 診斷：低相關

調整原因：近 5 日信心分數與股價關係偏低，提高價格確認，降低寬題材推估。；關鍵詞×公司後續樣本有效 0 筆，未達 30 筆，不調整樣本權重

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

摘要：綜合市場情緒 相關新聞集中在：台股暴跌 這些外資攜手投信逆勢敲進股可留意 - 經濟日報；輝達財報前夕賣壓罩頂！台積電領台股開低跌逾千點 失守5日線、43K - 經濟日報；台股開盤漲627.98點 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.26 | -31.93% | -22.56% | 155.46 | 228.38 | -31.93% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | -0.51 | -51.89% | +36.02% | 55.17 | 114.68 | -51.89% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | -0.44 | -7.26% | -5.03% | 2,175.00 | 2,480.00 | -12.30% | 同向 | 98.27 | 22.09 | 586.89B TWD / 59.71% | 2026-11-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 2 篇新聞命中。 方向判斷命中詞：放量。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel、INTC」，共 2 篇新聞命中。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。

### 主要來源

- [台股暴跌 這些外資攜手投信逆勢敲進股可留意 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE4xS0tUSENVbEdyMVlZM1JSXy1qQzB2ckFOUml5eW9mSU1zOW5JWGxJdk40bmJPX0lGNklmMXFUejgxWExGMVpaSE9ubjdYUldRdUE2czBhT0xTQdIBX0FVX3lxTFBMRmVUMXFmcWRNdjRvUi1qd1ZZeC1vckY1d2NQMjFjRFo3RmFna2JUbEh6SFgxcWRkd2h6Wk1lVkl5U0FLMnJYOHpmLUVHZFRMemxyUWRvazk4eWZaUV9B?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 16 Nov 2026 08:00:00 GMT
- [輝達財報前夕賣壓罩頂！台積電領台股開低跌逾千點 失守5日線、43K - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5heDdtUEVTNkJEUFA2WjQzRlFfbDlmWnZibjl4LUVqemhIN1JzZ1dhOVlYUzZGZFVyTnJheDg4RUNldV9zVWRyOWFHdjdLYThodk1PTGptaE12Z9IBX0FVX3lxTE9lZlVhQU1QVnlfZm5CamhGRElxU0xIeU9kY19jckFMSW1SYTZtYnRMVFVia21JNDdiOVpqekdDd1lVT05hb1lTUmdraXlGcVBYMjd4REtFODlMTkptOE1J?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 16 Nov 2026 08:00:00 GMT
- [台股開盤漲627.98點 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1HRmpJR011SFZQMVlDaXpqTUQ2STAtYUZEZ21HR1BzcEdaeWE3VEhDcXo2ODRKaTFqZWhxSy02TXR5dXFUQTB2bUdNMzRtcHVOaDhHd0pEWkhyUdIBX0FVX3lxTE82RUtfbmtBS25VNkhQanhkZVhIblN5eGhWT0xyOXVKMUt0N1plYi1MSy1RS28xS2EzTi1qUlJDVVBWTG00Q1JJc1lfVnA5QUNTZGtfbVFzb0JZS3dBdFdj?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 18 Nov 2026 01:12:20 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：台股收盤／跌947.97點收40,092.11點 台積電收2,170元跌2.03% | AI 人機協作 | 證券 - 經濟日報；台股強震近1,750點！AI 高價股淪重災區 34千金僅「這4檔」逆勢走揚 - 經濟日報；INTW 2X Intel ETF Tumbles 13% as Intel Drops Amid Shareholder Lawsuit and AI Chip Selloff; Taiwan Semiconductor Falls 5% - Yahoo Finance

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | -0.59 | -7.26% | -5.03% | 2,175.00 | 2,480.00 | -12.30% | 同向 | 98.27 | 22.09 | 586.89B TWD / 59.71% | 2026-11-01 |
| INTC 英特爾 | 新聞直接提及 | -0.59 | -51.89% | +36.02% | 55.17 | 114.68 | -51.89% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.59 | -2.46% | N/A | 503.41 | 516.10 | -2.46% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | -0.56 | -31.93% | -22.56% | 155.46 | 228.38 | -31.93% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 產業/供應鏈推估 | -0.02 | +12.44% | +2.89% | 506.24 | 517.99 | -2.27% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -2.73% | -12.25% | 341.60 | 446.77 | -23.54% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.04 | -11.26% | -14.05% | 529.00 | 703.00 | -24.75% | 同向 | 17.55 | 29.85 | 88.62B TWD / 47.13% | 2026-11-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.03 | -0.26% | +0.26% | 3,860.00 | 4,920.00 | -21.54% | 未明確 | 62.35 | 61.77 | 55.03B TWD / 5.77% | 2026-11-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電、Taiwan Semiconductor」，共 3 篇新聞命中。 同時符合主題標籤：AI, advanced packaging, CoWoS, AI server。 方向判斷命中詞：falls。
- INTC：新聞直接提及「Intel」，共 2 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [台股收盤／跌947.97點收40,092.11點 台積電收2,170元跌2.03% | AI 人機協作 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBoNDZmRXZLeVhudWtPNldxb3paWkEtXzNoOEN3RWlUVnNtMm4ySkt1Ynp0bUFfdzRYcUJEWXZLQW9Rdlh5SnBWQWRGOFU2T1BmV0lyeVRkVi16YkU?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 16 Nov 2026 08:00:00 GMT
- [台股強震近1,750點！AI 高價股淪重災區 34千金僅「這4檔」逆勢走揚 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5SbFV2QjlUeHY5OUhONVdyelp4QmoyYjA4U3BsU2RILVNfWHV2MGNQUDNEaWRuaDZ1NmdsMDlnUmowamN5Q203TGc2dWJjbGdSbF9SX0ZXWTVZQdIBX0FVX3lxTE81SXFWSXdRUXhKNUJRUDlmd2hfejM3TDZRaDBRS1BnR2hSNHVJSGhOV1ZKMHV0bDlhTHZUMTY2bDY5X0VEbFNpQ091cGN3dlE4c2VQYUlIZnpLcEhkMFdJ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 16 Nov 2026 08:00:00 GMT
- [INTW 2X Intel ETF Tumbles 13% as Intel Drops Amid Shareholder Lawsuit and AI Chip Selloff; Taiwan Semiconductor Falls 5% - Yahoo Finance](https://news.google.com/rss/articles/CBMilAFBVV95cUxQdmtzY3otMWptM0k1dXpYalRVUm03VUxJZUhVYWpTc0hnT1IxTjVVd1ZCS3dhRmxUc0xiUXo0YTA2bjFheVVNM1dVLTZoV0xrdUpPZzlZNUlYekpHNWR5ZE44aU1MZHBVUzhhUERHODI2R2VlV1haTk1qQThkTUVKaFZIb05VRDFBUjZUZ2xmb3hqTWJ4?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 16 Nov 2026 20:03:12 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：INTW 2X Intel ETF Tumbles 13% as Intel Drops Amid Shareholder Lawsuit and AI Chip Selloff; Taiwan Semiconductor Falls 5% - Yahoo Finance；Taiwan Semiconductor Falls 4% as U.S. Tightens AI Chip Curbs on China; Intel Drops 3%, AMD Slides 2% - 24/7 Wall St.；AMD Expects Its CPU Revenue to Double in 2027. Is NVIDIA’s Turmoil AMD’s Opening? - 24/7 Wall St.

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.59 | -51.89% | +36.02% | 55.17 | 114.68 | -51.89% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | -0.58 | -7.26% | -5.03% | 2,175.00 | 2,480.00 | -12.30% | 同向 | 98.27 | 22.09 | 586.89B TWD / 59.71% | 2026-11-01 |
| AMD 超微 | 新聞直接提及 | -0.57 | -2.46% | N/A | 503.41 | 516.10 | -2.46% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | -0.49 | -31.93% | -22.56% | 155.46 | 228.38 | -31.93% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2303 聯電 | 產業/供應鏈推估 | -0.05 | -8.51% | -8.06% | 90.90 | 164.50 | -44.74% | 同向 | 6.80 | 13.65 | 25.20B TWD / 18.33% | 2026-11-01 |
| MU 美光 | 產業/供應鏈推估 | -0.04 | -26.63% | N/A | 712.42 | 971.00 | -26.63% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | -0.04 | -14.96% | -7.30% | 797.24 | 2,335.00 | -65.86% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -2.73% | -12.25% | 341.60 | 446.77 | -23.54% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「Taiwan Semiconductor」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip, foundry。 方向判斷命中詞：falls。
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [INTW 2X Intel ETF Tumbles 13% as Intel Drops Amid Shareholder Lawsuit and AI Chip Selloff; Taiwan Semiconductor Falls 5% - Yahoo Finance](https://news.google.com/rss/articles/CBMilAFBVV95cUxQdmtzY3otMWptM0k1dXpYalRVUm03VUxJZUhVYWpTc0hnT1IxTjVVd1ZCS3dhRmxUc0xiUXo0YTA2bjFheVVNM1dVLTZoV0xrdUpPZzlZNUlYekpHNWR5ZE44aU1MZHBVUzhhUERHODI2R2VlV1haTk1qQThkTUVKaFZIb05VRDFBUjZUZ2xmb3hqTWJ4?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 16 Nov 2026 20:03:12 GMT
- [Taiwan Semiconductor Falls 4% as U.S. Tightens AI Chip Curbs on China; Intel Drops 3%, AMD Slides 2% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi1AFBVV95cUxQbTYxU1FmUU5YaC1IY0pVU2FNWHVqZkpud3MybzRhZW9MR3RYNDdwUGFzSkJWTEJELWVWcFNIWU1GcU94QnRJRDl0OUYtTXVyeFlacWxLQnVWRTh0ZmVKaEwyNHd1MUtNdWZ6X1diRW5IZVJOeHVWQS1pRndMQTdUbGw0ODNZTmdYUjRCRUx0VHFtZDdvT3k0clRGdTRDYS1tek1hcEFGLVVjaUZ2bzdRdDJfOXh3RGdVMTg5S0ZFS0txdm8xWmJJaWQ3RFItZ2hNRkw2ZA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 17 Nov 2026 17:02:00 GMT
- [AMD Expects Its CPU Revenue to Double in 2027. Is NVIDIA’s Turmoil AMD’s Opening? - 24/7 Wall St.](https://news.google.com/rss/articles/CBMivgFBVV95cUxOODM3R2FIcVBUYnR5ZWZGWmNCSDNjaUpybFY3WUdwdDJBNklCQUhiNGRmMWU3QjZCTlRBNjM5LVFtX3hzck9qekVKQVZsMGc4V0RvbGFuRE9tN3NZU21BYUM4cDZjclg3NkRQSG9SS0VES1VTbmktYWRXYnQ5YU1MTWRidURYT0pnSEdmaVRCeXUtU3JqOG9hbXR0NFNQZWpPMFMxZUFXZzViSlNKUjB0NEdNUnByeFh5VTNTaXNB?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 17 Nov 2026 16:04:00 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：‘I’m Not a SanDisk Fan. I’m a Micron Fan’: Jim Cramer Picks Sides. Why MU Stock Looks Safer Than SNDK Stock. - Barchart.com；SK Hynix Is Down 16% in a Month. What Will It Take to Get SKHY Stock Back to $150? - 24/7 Wall St.；Why Micron and Sandisk stocks are falling on Monday? - TradingView

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | -0.59 | -26.63% | N/A | 712.42 | 971.00 | -26.63% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.59 | -14.96% | -7.30% | 797.24 | 2,335.00 | -65.86% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | -0.45 | -31.93% | -22.56% | 155.46 | 228.38 | -31.93% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK、SanDisk」，共 5 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [‘I’m Not a SanDisk Fan. I’m a Micron Fan’: Jim Cramer Picks Sides. Why MU Stock Looks Safer Than SNDK Stock. - Barchart.com](https://news.google.com/rss/articles/CBMi3AFBVV95cUxPemdiUWFhaEd2eHIwVlAwUWYwcUVpR1hibl9kVGJFMFhhX2lES0pJMnpnWlQxU0JsRUZ5Q1hMYzNvamotdTZ5aHVYZ0lFTThrbWlUNEV1dV9vWDZKQ2xLM1lYN0NGTVJkMXlPUXFJT0xVNHhEYXZ5RHhyT2VZSjJGbE1ocXFSek5VMEVEQzlhN25KNFJrY0pyZGZZX2ZtQV9NWURrcEM2UERLdVFGdVUwd2RfUllXeDVDU2hreE96RlVkV2lGc2c5VTVPaV92SWgyVm9WN0lkcjd6dEhI?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 16 Nov 2026 22:25:27 GMT
- [SK Hynix Is Down 16% in a Month. What Will It Take to Get SKHY Stock Back to $150? - 24/7 Wall St.](https://news.google.com/rss/articles/CBMivwFBVV95cUxOSl83eG1sQ3h1TzdRREptcHhkdmY5aXhnY3l1M1NkdXFtNlVTRmJ2Tjk5ZjB3TXBjb3phMl9lbmtPUGsyWTJlaFJBSDdvLS1GemhaMVRUU2x0OERJVkt2Vlh3STFLUXNObzRGVTFuczdvM0VCR2NzY01qYUZDUkNzQW92SG5nUl9KYzBxRlBXbk4zNU12c25iWmd2UDdqcWh4azZ2OGphd3VOVDNsMTJSdENEampNdmlXcWZqS1ZJZw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 16 Nov 2026 19:03:00 GMT
- [Why Micron and Sandisk stocks are falling on Monday? - TradingView](https://news.google.com/rss/articles/CBMixgFBVV95cUxNMjgyTzBfNkZOU0todTlhLTRnNWtjaXFTWW13MjVyaTlLWVhsQVJKdFowOUFyYkd4N1NpVjhYWUltY2VFZ3ozcjFmYTI1cVJQTFFXU3JMRzQ2aWFCU2hKYW04Y0IxNnduY1RIakVHSEFDa3I2eno3TENDdkVzTy1wMmw0NTlZejR2T2hRZWFHdFd2MmV0dmU0WWZnQTFJM0tyU0FCNFVYTl9SZ0RhdXBwWGJ0SlhlYloyVVhQZ3R2M1JoUXV0UUE?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 16 Nov 2026 15:19:24 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：台股重挫2635點史上第2大 AI供應鏈全面下殺 - 經濟日報；黃仁勳請辭後再傳利空！Vera Rubin 延後放量，台灣20家AI供應鏈分成2大陣營 - CMoney投資網誌；美國 BIS 祭出 AI 新規 法人評估對台半導體供應鏈影響有限 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +12.77% | +26.20% | 351.91 | 352.78 | -0.25% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | -8.75% | -9.32% | 218.00 | 289.00 | -24.57% | 不適用 | 16.57 | 13.25 | 1305.32B TWD / 45.73% | 2026-11-01 |

關聯理由（前 3）：
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [台股重挫2635點史上第2大 AI供應鏈全面下殺 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBrbjkwejJFSENUNkM1LXlKZDVsTmFFNXdVZG5IVklOOEYtVkNlUExhbk43dmEya05hRkxZLXcyUVFkM0V0THdKMzVjVXZsOWFoUUpNNEtXUkdWQdIBX0FVX3lxTFAyOHN5SExOXzdHSWhPeDQxZC1TN0FYQzkteHkzQ2JxUGxySDlYVU1NYWV5MWkwamUzUTZwQ3VLcEVuaGZ2alI2a2FUWjNGRE5IYjVpbURXWE5pUTJPdTJB?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 16 Nov 2026 07:01:16 GMT
- [黃仁勳請辭後再傳利空！Vera Rubin 延後放量，台灣20家AI供應鏈分成2大陣營 - CMoney投資網誌](https://news.google.com/rss/articles/CBMifkFVX3lxTE8zTHhaZzFYcGVyb010OXRrYjhUQ1N6RUtsbzVILVgwbG5kN2ZfODBMZmFBUkdGNkVVdWp2eS0tZjNjZTNFOUtNR2k2V0xkVHR3MExWVzRoR05zR0NoR0VyOUR2QjBZX3VQRFl1c3Nsdi0xUVJ5SmZVUUJwYzRWZw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 16 Nov 2026 08:27:49 GMT
- [美國 BIS 祭出 AI 新規 法人評估對台半導體供應鏈影響有限 - 經濟日報](https://news.google.com/rss/articles/CBMiekFVX3lxTE5XY2kxa1dHWkpGSVRYT3dqTGRpMGN1TW1pMTNORDN6T2taaUdmSkdsVTVtRjZyYURBVnRoTDU4NUo2R05MODcxaGxRZlgzeHZ0UWxUTGFaR3A1dDBJZ0t2Qkl6WHBmM0FZUnhHSGVyTDZzMVE3U004d2Z30gFfQVVfeXFMTUw4QVBNa3Z4YkVSU0NNWDZJVWtmLXJvWFJ3RDdLX21hdEZ1TWNnY193bkVMbE56YUNBWVRvZVBYRXlJb1NNb05jT253ZUMxY210ekstSHZQdnJvdEtwOUU?oc=5) - Google News source discovery | 經濟日報 money Wed, 18 Nov 2026 01:51:12 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：統一證券：台股技術面弱勢整理，反覆利空測試- 新聞 - MoneyDJ；國票證券：台股低檔仍有承接力道- 新聞 - MoneyDJ；AI創世紀+去槓桿並存，群益投顧估明年台股區間35-50K - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [統一證券：台股技術面弱勢整理，反覆利空測試- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxOblJBSkR3SFQyV0dIUEt0OVBfdXRGWG12WlNleFJ6NTZ5c2pFNUhCVWREM2dHMllRbnhTUWJMeW9OZ3otQjQwcHhsSnBpb2hJSzM3R2dZR2RjOFhray1mV1QxRGI5Y1Z3aDhTaHRBZHZsdWlMSkl5MUJycTRGbVlLNmNZcGlTUGF3M3YyZmthX2Fsdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 18 Nov 2026 00:51:00 GMT
- [國票證券：台股低檔仍有承接力道- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQc2Nlek5mRjlfQ3JMN2s0Y2taMWNDaTB0dHhJVjVkcUVaTDlGY3hac0IxeWxXUXlvV1QzOUhSU0lvVlljal9iTUp6SEd1bElEVUFxcFQwdXF0bjMxakItMzA3Sm92anpUbHRiNF9qSzZ6bTZxUU5odEd6OGxLTHljcnVReFhKZVNHaFc4bjhfWDRqQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 18 Nov 2026 00:51:00 GMT
- [AI創世紀+去槓桿並存，群益投顧估明年台股區間35-50K - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxORmE4cEdFTVNGSUlub2VkT3RnSEFTSVlKaFR5VzY1YW1na25CbnFNeDl6eUhaNGYzNUNOMkFrSW90elFFMUlHcjUwWDNpT3lDUTlzZ3FERV9qWUF1VC1UUWN6MFNmT2xPMjFKanpDSXg2cXFRYkMyTURWLTRjb2ZxbGQ2SGZNbjZEbFJmaXEtWWlLUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 17 Nov 2026 09:07:00 GMT

## 新興題材：變現需求

摘要：新興題材：變現需求 相關新聞集中在：《貴金屬/金屬》美元殖利率漲+變現需求壓抑金價-台股 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《貴金屬/金屬》美元殖利率漲+變現需求壓抑金價-台股 - MoneyDJ](https://news.google.com/rss/articles/CBMiigFBVV95cUxQdF9rek42N1lFejVpdkhoWFpwbi14ejRYN2JqcmVna0dpSkwyX0R0U0JXVzFzR3VubXpsWHBzbE9Cc3dJUTZZWGJobXFSX2drMTFGamhxUUs0SmpZbHFjV1NFazBGOFNxX204UDJxRFkwZGlPMUQtTzFCSFlaT3RmLThfT1pDY1hxMEE?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 17 Nov 2026 23:17:59 GMT

## 新興題材：AI供應鏈

摘要：新興題材：AI供應鏈 相關新聞集中在：台股重挫2635點史上第2大 AI供應鏈全面下殺 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股重挫2635點史上第2大 AI供應鏈全面下殺 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBrbjkwejJFSENUNkM1LXlKZDVsTmFFNXdVZG5IVklOOEYtVkNlUExhbk43dmEya05hRkxZLXcyUVFkM0V0THdKMzVjVXZsOWFoUUpNNEtXUkdWQdIBX0FVX3lxTFAyOHN5SExOXzdHSWhPeDQxZC1TN0FYQzkteHkzQ2JxUGxySDlYVU1NYWV5MWkwamUzUTZwQ3VLcEVuaGZ2alI2a2FUWjNGRE5IYjVpbURXWE5pUTJPdTJB?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 16 Nov 2026 07:01:16 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
