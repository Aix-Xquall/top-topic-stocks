# 每日股市熱門話題分析 - 2026-09-22

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **新興題材：MoneyDJ**｜正向｜熱度 11｜市場確認 100.00｜同向 1/1
2. **AI 伺服器與資料中心**｜正向｜熱度 16｜市場確認 86.63｜同向 7/8
3. **半導體與晶片供應鏈**｜正向｜熱度 5｜市場確認 86.31｜同向 7/8
4. **記憶體與 HBM 供應鏈**｜中性｜熱度 7｜市場確認 N/A｜同向 0/0
5. **新興題材：TradingKey**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.00（樣本 17）
- 5日相關係數：-0.01（樣本 13）
- 同向比例：15/17

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 新興題材：MoneyDJ | 100.00 | 1/1 | 0 | +10.60% | +9.87% |
| AI 伺服器與資料中心 | 86.63 | 7/8 | 1 | +8.46% | +2.20% |
| 半導體與晶片供應鏈 | 86.31 | 7/8 | 1 | +8.35% | +3.57% |
| 記憶體與 HBM 供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：TradingKey | N/A | 0/0 | 0 | N/A | N/A |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：竟摜跌停 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 相關性偏弱；應提高同向價格確認權重，降低泛 AI、泛半導體等寬標籤推估權重。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-09-09 | -0.28 | -0.12 | +54.17% | 24 |
| 2026-09-10 | 0.28 | 0.86 | +75.00% | 4 |
| 2026-09-11 | -0.01 | -0.08 | +25.00% | 12 |
| 2026-09-12 | -0.39 | 0.04 | +25.00% | 20 |
| 2026-09-13 | -0.42 | -0.14 | +17.65% | 17 |
| 2026-09-14 | -0.31 | -0.54 | +33.33% | 15 |
| 2026-09-15 | -0.04 | -0.42 | +68.75% | 16 |
| 2026-09-16 | -0.19 | -0.46 | +55.56% | 9 |
| 2026-09-17 | 0.43 | -0.13 | +66.67% | 9 |
| 2026-09-18 | -0.15 | -0.07 | +35.71% | 14 |
| 2026-09-19 | 0.20 | 0.47 | +46.15% | 13 |
| 2026-09-20 | -0.04 | -0.25 | +30.77% | 13 |
| 2026-09-21 | -0.15 | -0.05 | +61.54% | 13 |
| 2026-09-22 | -0.00 | -0.01 | +88.24% | 17 |

## 歷史回測摘要

- 回測日期：2026-09-22
- 近5日 3日相關：-0.06
- 近5日 5日相關：-0.17
- 同向比例：+47.62%
- 權重狀態：已調整

- 方向準確度：+47.62%
- 信心排序準確度：-0.06
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

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》聯發科天價助攻、收漲538點，日K連四紅- 新聞 - MoneyDJ；抱股賞月台股8利多護航- 新聞 - MoneyDJ；新聞內容-B93F0943-87B0-47E7-9110-F8F980B63FE5台股 - MoneyDJ

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2454 聯發科 | 新聞直接提及 | +0.42 | +10.60% | +9.87% | 5,010.00 | 5,010.00 | 0.00% | 同向 | 60.69 | 82.74 | 64.18B TWD / 44.08% | 2026-09-01 |

關聯理由（前 3）：
- 2454：新聞直接提及「聯發科」，共 1 篇新聞命中。

### 主要來源

- [《台股盤後》聯發科天價助攻、收漲538點，日K連四紅- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNOWlqUVI2NG0xYWFjQmtVS2w2WUw2T1ZvZWZSb2FlMThhdUdBZ3ZTWG9JdDRFblB0eWRsVlBQNUR5cVEyREcyQjJTR0I5R3NibTRTREEyREp3bVp4R0RRV25OOWNEU2RnV3RGOE9FM3MwTUg0MEJiUmZUejA4WW1mNDdCV0xieHdlWkdmV1lJMW8xQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 21 Sep 2026 07:57:00 GMT
- [抱股賞月台股8利多護航- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQcHM1dnFWUG9kdF9EeVU1QTdPQU54S3BjV241WnpqX1Y4VWpycTBuVTFHck02MjdfNVgyWHItNmZJOXNrakxvWjNwYlN1TzJ4b1V4S2pTb2RBaF92bGhWVFYxb3YzcVlicUpKZDE1NER1UGRnSHM4SGthdkhQRXNucmFBcm41SHRiMkJuajJDV1ZSUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 20 Sep 2026 22:40:00 GMT
- [新聞內容-B93F0943-87B0-47E7-9110-F8F980B63FE5台股 - MoneyDJ](https://news.google.com/rss/articles/CBMiigFBVV95cUxOUW1fVE1KbGxUQlVHV0pFbUhvQVZkNDl6Q09CRDhDZHZqdzFDT3hmaGFraWtHdUJYOXNIT2t0aGEwUllENkR3TC1KcVNMZ3ZQb3JQSWlHVHpFUWtlZjNkeC1jamVyeEZIVXdCbnRGRk5aLWxvdmJ0ZlZpSm5UNTBQZDBKeGprR05Ra1E?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 21 Sep 2026 23:50:14 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel Stock And 2 AI Infrastructure Leaders Tied To Chip Policy - Yahoo Finance；企業小心落入「決策債務」停滯陷阱，AI 資訊過量只會讓待辦清單越來越長 - TechNews 科技新報；免費 AI 進校園後，學校還能自由退出嗎？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.54 | +6.19% | N/A | 121.78 | 121.78 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.06 | +13.27% | +7.69% | 227.38 | 227.38 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.06 | +19.26% | N/A | 615.52 | 615.52 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.06 | +4.20% | +4.20% | 2,480.00 | 2,480.00 | 0.00% | 同向 | 86.28 | 28.75 | 514.81B TWD / 53.32% | 2026-09-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | +11.41% | +1.95% | 501.61 | 507.29 | -1.12% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -6.84% | -18.83% | 362.66 | 446.77 | -18.83% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.04 | +9.59% | +8.33% | 663.00 | 680.00 | -2.50% | 同向 | 13.92 | 47.97 | 82.25B TWD / 45.66% | 2026-09-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.04 | +10.60% | +9.87% | 5,010.00 | 5,010.00 | 0.00% | 同向 | 60.69 | 82.74 | 64.18B TWD / 44.08% | 2026-09-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Stock And 2 AI Infrastructure Leaders Tied To Chip Policy - Yahoo Finance](https://news.google.com/rss/articles/CBMimwFBVV95cUxQaWMyWjNsTGo0cnFWRl9CcWt0VWRJRHdydTAweEctclQxYzlPbmQ4a1BvRTBwLTk2U00xWHVGQTc0VjgyQ2ZjQTBfNWhEcUViSGN4T2w0S3Q2ZkZSY1JFZTdkSFNOMFpyN1JJeldfWWtnYW5USnZlWkpHR2IwUVdnU1g0SDBKdC01cXp1WkJSVkhYZ2ZpOW12STBkRQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 21 Sep 2026 07:13:18 GMT
- [企業小心落入「決策債務」停滯陷阱，AI 資訊過量只會讓待辦清單越來越長 - TechNews 科技新報](https://news.google.com/rss/articles/CBMilAFBVV95cUxNRlYxcVhEU3lqWTd6ODJqUXdJQVQwMEF5R3RpbFEwX1l3QWk4Q2M4NzlQbFBFVGtmM2NOdGRRQklSNjRJRXJyNERBX3BWYmU4YUZ1bV9YamJKZm1fdXRyZGMtQ2F4QlV0TG9nd2t6TFo0bXQ5Z2JkcllzMkV6TnE0cHFFbl9TVThZZVc2U0FrYXlFT1hP?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 21 Sep 2026 23:27:51 GMT
- [免費 AI 進校園後，學校還能自由退出嗎？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMi6AFBVV95cUxOU1UtZDJxNFJ5aXljY2YyNl9sVWU1Z3E0OFZGelVOaWthQTVhQ3l6aDJQRDZjM05VVGJDRHZPYWN0UFJlMm85OTRJWWFlY2RsRGN5OTEycFdKS2lXbk5kQmhDSHlSRVlkbDk2WUdHanh1TGpHUVY0N190Mnp2d1BOMjNmM01oNjlCeE8xS2RlVnlBLWNEaHJaTzlpRVF3blNNTk8ya0lWTHJiMkNBNjUtdHZIdTlrMDVZTVpLMGpEM1h2SXhoWXBuMldLTnJHbjZrdHI1Vkt3ajNvX2l6SDNINWVtUzFxbXlk?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 22 Sep 2026 00:11:15 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel Stock And 2 AI Infrastructure Leaders Tied To Chip Policy - Yahoo Finance；INTC, AMD, AVGO: Chip Stocks Jump Premarket After Nvidia's Blowout Report - Stocktwits；GSA校園人才講堂登場 產學攜手培育半導體本地與國際人才 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.57 | +6.19% | N/A | 121.78 | 121.78 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.47 | +13.27% | +7.69% | 227.38 | 227.38 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.47 | +19.26% | N/A | 615.52 | 615.52 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | +0.23 | -6.84% | -18.83% | 362.66 | 446.77 | -18.83% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2454 聯發科 | 新聞直接提及 | +0.47 | +10.60% | +9.87% | 5,010.00 | 5,010.00 | 0.00% | 同向 | 60.69 | 82.74 | 64.18B TWD / 44.08% | 2026-09-01 |
| 3711 日月光投控 | 新聞直接提及 | +0.47 | +9.59% | +8.33% | 663.00 | 680.00 | -2.50% | 同向 | 13.92 | 47.97 | 82.25B TWD / 45.66% | 2026-09-01 |
| 2330 台積電 | 產業/供應鏈推估 | +0.05 | +4.20% | +4.20% | 2,480.00 | 2,480.00 | 0.00% | 同向 | 86.28 | 28.75 | 514.81B TWD / 53.32% | 2026-09-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.05 | +10.56% | +10.18% | 157.00 | 164.50 | -4.56% | 同向 | 6.68 | 23.61 | 25.04B TWD / 30.71% | 2026-09-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel、INTC」，共 3 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：rally, surges。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Stock And 2 AI Infrastructure Leaders Tied To Chip Policy - Yahoo Finance](https://news.google.com/rss/articles/CBMimwFBVV95cUxQaWMyWjNsTGo0cnFWRl9CcWt0VWRJRHdydTAweEctclQxYzlPbmQ4a1BvRTBwLTk2U00xWHVGQTc0VjgyQ2ZjQTBfNWhEcUViSGN4T2w0S3Q2ZkZSY1JFZTdkSFNOMFpyN1JJeldfWWtnYW5USnZlWkpHR2IwUVdnU1g0SDBKdC01cXp1WkJSVkhYZ2ZpOW12STBkRQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 21 Sep 2026 07:13:18 GMT
- [INTC, AMD, AVGO: Chip Stocks Jump Premarket After Nvidia's Blowout Report - Stocktwits](https://news.google.com/rss/articles/CBMizwFBVV95cUxPQUU4dTZXYndUX2YwZlZ6VmR6d3JoV2dDbE1XR1FKS0p2YTZScmlIclZkTUxxb0paRW00TEgwVlE1Qk5hT3BnM3J4eVZqVDBpZ3o1blFiYTQ5M2t3OTlJU3pud01kVlJYQzFVaF82a2xfWXRfM2R2MzBVRDczX0pnRkpPZ3dpam03QlhibkliRnQ3NWhJU25VM0d1bVlvSm02bjJaV2pjZlJwTUpVVnZCMHRxYjFFd2Q2RXRNOFl3ZkItc0llS0JKR2dVN1VORDg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 20 Sep 2026 00:57:55 GMT
- [GSA校園人才講堂登場 產學攜手培育半導體本地與國際人才 - 中央社 CNA](https://news.google.com/rss/articles/CBMiVkFVX3lxTFBPQXRKRWRCMUdEellvRFROblNJRlVVRVlCdm55OWd2cUw3emF1aFBSOWs5eGRlV3RnVElRX1dzc0c4STRDS3pFZFc0MWhYX1JpWkxYUlhn?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 21 Sep 2026 06:05:29 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Zacks Investment Ideas feature highlights: Intel, SK Hynix, Nvidia, Microsoft and Apple - The Globe and Mail；Micron: Old Valuation Metrics No Longer Matter (NASDAQ:MU) - Seeking Alpha；Micron vs. SanDisk: Which Memory Stock Is Better Suited for Long-Term Holding, MU or SNDK? - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | +7.51% | N/A | 1,043.96 | 1,043.96 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | +17.04% | +9.70% | 1,791.82 | 2,335.00 | -23.26% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +13.27% | +7.69% | 227.38 | 227.38 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | 0.00 | +6.19% | N/A | 121.78 | 121.78 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 新聞直接提及 | 0.00 | +11.41% | +1.95% | 501.61 | 507.29 | -1.12% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 新聞直接提及 | 0.00 | +8.63% | +21.56% | 338.98 | 338.98 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU」，共 4 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Zacks Investment Ideas feature highlights: Intel, SK Hynix, Nvidia, Microsoft and Apple - The Globe and Mail](https://news.google.com/rss/articles/CBMi_AFBVV95cUxNRzJQSUV1bUhKczQ3SUc5eWVZbWoyQVJycGlLdkVERVFFa2w0WWNvbE9MUEhSWFIyZmJDNEdmUVM2QjE3elpzYldYVnd0cmYzRUNobWtmNVg1THR5SG54LVRNMmRsdHJ6NVZPTDlFSUZDVEpFV3B6d01PbVZHQU5WQTF5ZjNqbGdTa3VWWG56YXFEOEt4bFliNWZzaTlfSmlIMmoxVDVPWm0xVkxZZGdSWk91VC1EaUE2QkhPUXBleWtydVVYbUQxa0U2TnJrQ2ZpWHliZFVPekdhQWdzRE9JbENRSk9MQnZmWFFpZzFjRFFqckhteTgyMnU1UmU?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 21 Sep 2026 14:12:00 GMT
- [Micron: Old Valuation Metrics No Longer Matter (NASDAQ:MU) - Seeking Alpha](https://news.google.com/rss/articles/CBMijwFBVV95cUxNSVhGZUdSc0U1Q21jdjlyMHMyMU42TnBWOGRMUnNmWXdWa1ZWcDZlVU9mZ3J0Yi1ma012a0ROblpaTmRWTzdvUms4em9TR3pja2ktY3JwTFhvUUdzMk9ydUptT3R6bDlUTkszOWpfV2VjSXNweExUcnpFZnQxQWhWYllkaTBtdVZGNEZGSFRSTQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 21 Sep 2026 16:19:16 GMT
- [Micron vs. SanDisk: Which Memory Stock Is Better Suited for Long-Term Holding, MU or SNDK? - TradingKey](https://news.google.com/rss/articles/CBMi0wFBVV95cUxNVnhOMUFzTkdHc0pxM0w3eUNZdDgwejhRUjVNdVpKYXF1T0xMSHd3c2dYNDBGQkVULXhpTjYtbTBxUnJCX0E0MUhLUlBEUkZxcTVKOGtYZHFSdVlZdWVFNzFta05NeE5oZHNHVEc3RHNpRlZ0aXhRNFJRbkp5TGMwRWEtNEpWMnZ0UFJjNjhIV1ZjXzZ4MEQzYXRYSVBHNVlWRV92WVFUUS0ya29mc1NXT0tIYnBsX2JuWUE4TURLUnI2Tk5vNkV2eHZoZDZ2ZnpGVEdF?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 20 Sep 2026 09:26:01 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Why Is Intel (INTC) Stock Volatile After Earnings? Revenue Beat Overshadowed by $11 Billion Loss - TradingKey；Micron vs. SanDisk: Which Memory Stock Is Better Suited for Long-Term Holding, MU or SNDK? - TradingKey；Micron Technology Inc (MU) Stock Analysis & Forecast - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | +7.51% | N/A | 1,043.96 | 1,043.96 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | 0.00 | +6.19% | N/A | 121.78 | 121.78 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | +17.04% | +9.70% | 1,791.82 | 2,335.00 | -23.26% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。

### 主要來源

- [Why Is Intel (INTC) Stock Volatile After Earnings? Revenue Beat Overshadowed by $11 Billion Loss - TradingKey](https://news.google.com/rss/articles/CBMiyAFBVV95cUxPdGVhdUdOWHYwd0I2OHRLRjlFVE9KTkNud09aOHhCOTZGY2NDZVM4VjFnTTZKdkpKdlBORHo1OG5RWENLVFg4VUZoYVdVWVRpaWFCSWtxY2dHX280ZFFsaDlvSldKQm9NdTdWTjlueks4V3V3RUVJQ2pqYVFtNi0xVU9zY2V3MGdONjRFaHJqU1RRaVZZMm9GZndlNVRSaWpveDlMWG41WG5qUk52T0tRcGl1bklGZ2twMmQyQnJxdkM0YzU1d1J2Wg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 20 Sep 2026 15:06:47 GMT
- [Micron vs. SanDisk: Which Memory Stock Is Better Suited for Long-Term Holding, MU or SNDK? - TradingKey](https://news.google.com/rss/articles/CBMi0wFBVV95cUxNVnhOMUFzTkdHc0pxM0w3eUNZdDgwejhRUjVNdVpKYXF1T0xMSHd3c2dYNDBGQkVULXhpTjYtbTBxUnJCX0E0MUhLUlBEUkZxcTVKOGtYZHFSdVlZdWVFNzFta05NeE5oZHNHVEc3RHNpRlZ0aXhRNFJRbkp5TGMwRWEtNEpWMnZ0UFJjNjhIV1ZjXzZ4MEQzYXRYSVBHNVlWRV92WVFUUS0ya29mc1NXT0tIYnBsX2JuWUE4TURLUnI2Tk5vNkV2eHZoZDZ2ZnpGVEdF?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 20 Sep 2026 09:26:01 GMT
- [Micron Technology Inc (MU) Stock Analysis & Forecast - TradingKey](https://news.google.com/rss/articles/CBMiY0FVX3lxTFB2cjlJNEFoZnN6al9fVWlOSktTV2tWRzJ1c0c2SklreGhaeHF5VlZlSjNNRE1SaXlnaUVsQ1FaMXFtZUlvM19kUzhHdURNU1VkNmNhLTNPSDNtXzBpSHNZS0xkNA?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 21 Sep 2026 07:10:52 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：Micron: Old Valuation Metrics No Longer Matter (NASDAQ:MU) - Seeking Alpha

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | +7.51% | N/A | 1,043.96 | 1,043.96 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +11.41% | +1.95% | 501.61 | 507.29 | -1.12% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Micron: Old Valuation Metrics No Longer Matter (NASDAQ:MU) - Seeking Alpha](https://news.google.com/rss/articles/CBMijwFBVV95cUxNSVhGZUdSc0U1Q21jdjlyMHMyMU42TnBWOGRMUnNmWXdWa1ZWcDZlVU9mZ3J0Yi1ma012a0ROblpaTmRWTzdvUms4em9TR3pja2ktY3JwTFhvUUdzMk9ydUptT3R6bDlUTkszOWpfV2VjSXNweExUcnpFZnQxQWhWYllkaTBtdVZGNEZGSFRSTQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 21 Sep 2026 16:19:16 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股登歷史次高驚見震盪！聯茂爆3.19億元鉅額違約交割 金額創今年新高 - 經濟日報；台股短線攻擊訊號亮了 法人看好秋節前後挑戰新高 - 經濟日報；台股市值兆元股 增至24檔 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股登歷史次高驚見震盪！聯茂爆3.19億元鉅額違約交割 金額創今年新高 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE8tdXVhOWRnVnZJaGhHWklmRDQya0ZvUV9sYkNoWVJDakNzZUhHdjVZdWxiWDNSOWl2TnZveUhFaVFYSHl4MWlLalo2WnI0QVgzVFZSOTFUclp6UdIBX0FVX3lxTFB6Umd5bllsWFNsX2ljMjlVVENOdEFBM3hZLXZYV3VpVmdJZ05WZE83d3Y2ejhfbUNNblY1Z09FN0lCeC1EVVZkQmoyMGVJM0wwVlo1MUt2WlVJYzc4djhn?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 20 Sep 2026 09:00:00 GMT
- [台股短線攻擊訊號亮了 法人看好秋節前後挑戰新高 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9ONGdXNEJBN3FFSGdPeGpUNHpoOTUySUd1VE5DUHllSkhpTXBKY09sQTFNUDRaWUU2ckNjVWtUR2o2Sk5IaDh3X1lPb1VScEpFVnVQZUt3cHdqUdIBX0FVX3lxTFBIUG9MOGtJRVNTZDlxcEg2WWVIMmRmVmFFcmJOUWU5UkRkMDdNLWpVRk9iNkdlSVFrOXBBb0dJa05GZmNJS2VkdVpvdE5CazBTMzRKSE5lMDZPTThYTDZV?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 21 Sep 2026 18:33:58 GMT
- [台股市值兆元股 增至24檔 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9DNWt3dUYzUEhsdGhCNHFkNDJ2TXpPWVNkZ2puQkg0REw4MENqZXFDQ0cyVlBsT0NjYUtmZkRsQlBLNExKeFZqaHRZUVk0akVnVy1rdmlIQ2RBZ9IBX0FVX3lxTE9QUlpmSjlYLTFNTnZXcUhWeWxZOFotX29nTE5aYm5qTFQ2WE9WMFVmdF9aV19NSDVhdUpGNm9sUWRCYlFUc19YT1Jyc1hMUXh6bzh0TFFOQVZOa0U1cjdN?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 21 Sep 2026 03:00:00 GMT

## 新興題材：竟摜跌停

摘要：新興題材：竟摜跌停 相關新聞集中在：三大法人買超470億元！台股差不到23點再攀顛峰 「這檔千金股」竟摜跌停 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [三大法人買超470億元！台股差不到23點再攀顛峰 「這檔千金股」竟摜跌停 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFB2a3AtMnkyaGhoNWllai1RcmIwd1FGcjRTZlg1bHFLS1lCWkZ4MGczdTQ4WVBRMlBJME91SlZJeW5naXBrbG0yV2FuUVpmdUZhOEk4aS1nMmdrQdIBX0FVX3lxTFBGRjV2MU41WW5iVHd4REw5SWhTcVJYTjBqSG5xdmt6OW1nMWxrQkJmUldydEI2eEdsc2p4Wlp5bThtcmFGRjFnVjBUem1rRllRazM3aHVqNi1RNGlkNnYw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 20 Sep 2026 09:00:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
