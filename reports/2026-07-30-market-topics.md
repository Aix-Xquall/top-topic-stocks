# 每日股市熱門話題分析 - 2026-07-30

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **綜合市場情緒**｜負向｜熱度 46｜市場確認 98.52｜同向 3/3
2. **AI 伺服器與資料中心**｜中性｜熱度 8｜市場確認 N/A｜同向 0/0
3. **關稅與供應鏈轉移**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0
4. **利率與成長股估值**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
5. **半導體與晶片供應鏈**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.25（樣本 6）
- 5日相關係數：0.92（樣本 4）
- 同向比例：4/6

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 綜合市場情緒 | 98.52 | 3/3 | 0 | +9.51% | +10.76% |
| AI 伺服器與資料中心 | N/A | 0/0 | 0 | N/A | N/A |
| 關稅與供應鏈轉移 | N/A | 0/0 | 0 | N/A | N/A |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 記憶體與 HBM 供應鏈 | 0.00 | 1/3 | 2 | -43.15% | +36.48% |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：全球晶片 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
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
| 2026-07-28 | 0.32 | 0.13 | +36.36% | 11 |
| 2026-07-29 | 0.16 | -0.03 | +92.31% | 13 |
| 2026-07-30 | 0.25 | 0.92 | +66.67% | 6 |

## 歷史回測摘要

- 回測日期：2026-07-30
- 近5日 3日相關：0.71
- 近5日 5日相關：0.73
- 同向比例：+60.00%
- 權重狀態：未調整

- 方向準確度：+60.00%
- 信心排序準確度：0.71
- 診斷：正相關

調整原因：近 5 日有效樣本 5 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：綜合市場情緒 相關新聞集中在：台股大回檔 此時是國安基金護盤時機？財政部回應了 - 經濟日報；台股回檔爆槓桿危機！929檔「融資告急名單」熱門族群個股曝光 - 經濟日報；台股一度再崩逾千點失守4.1K！台積電、聯發科領跌 鴻海領金控股抗空 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | -0.42 | -6.38% | -8.33% | 2,200.00 | 2,410.00 | -8.71% | 同向 | 74.39 | 29.58 | 442.68B TWD / 67.87% | 2026-07-01 |
| 2317 鴻海 | 新聞直接提及 | -0.42 | -6.14% | -5.77% | 237.00 | 289.00 | -17.99% | 同向 | 14.13 | 16.83 | 821.76B TWD / 52.11% | 2026-07-01 |
| 2454 聯發科 | 新聞直接提及 | -0.42 | -16.00% | -18.18% | 3,150.00 | 4,310.00 | -26.91% | 同向 | 62.91 | 50.20 | 58.01B TWD / 2.80% | 2026-07-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。
- 2317：新聞直接提及「鴻海」，共 1 篇新聞命中。
- 2454：新聞直接提及「聯發科」，共 1 篇新聞命中。

### 主要來源

- [台股大回檔 此時是國安基金護盤時機？財政部回應了 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBQTHFoUHNLUWRYOFh0Y3dxby1vMjY3a3dFZHNNMzBlekdiNHV4NzdGQWVVbjMySHYwSmVjQVhrbm9pRGhwMFc5UURXVWo4VFo4NXhXa2xWMG1IZ9IBX0FVX3lxTE9PTDFqYUJyNzVMeDlfSWVCcmZMaEpXYzBHZzI2LUdKMWVWYmdTUklMaFdUT0h6YTE3TkhBTVBCUEt1eWE3Tkd4TEZnRkpmNkgwZ1RWeldMMkRkY3A3QlFZ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 29 Jul 2026 02:11:38 GMT
- [台股回檔爆槓桿危機！929檔「融資告急名單」熱門族群個股曝光 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1pRXdBUkNhamxfaU5ianlPS2RfdklXYTZaTm1IZEc0NFRDaF93RE9BUnNJQzNVdjFDd0Z3ZmpHSnYzQ3ZPUlpJTThrTWdwYXV2bEtkOXZiUW01QdIBX0FVX3lxTE0wWE9rYzBmWlNETXVFYlMyNVZkeWZHYU81Rll5RlptbWVpTDdiaG40eG95ZUx2N2UwYVpxeHgyUkt5bXlpeGNpZ3FaWTRtc0tZd2taN3RuY1V2T2RLSURn?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 28 Jul 2026 09:00:00 GMT
- [台股一度再崩逾千點失守4.1K！台積電、聯發科領跌 鴻海領金控股抗空 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5TWW00anJjWGJQXzdCeEJUb3pLYkxTTGgxcUhRQ2lwbGtEc19xMGEzZFVFZHp4Y3lyYzE3WHpqY0pEcHI4UGQ2MVRYQU9IaHNPV1V1SnhiRkt1d9IBX0FVX3lxTE1zVVVSZUlNODZyQ1o1amtVQjFfNFROUURLc1N4c1FKT0JnNHhWXzFUZ0p5am9nT0RBQXMxTklYUjVPVUhVU3RIN0lHUEQ3ODBFUDlZaTBVZTRVelh6OE8w?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 28 Jul 2026 09:00:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：AMD vs. Intel: Which Is the Better Artificial Intelligence Chip Stock to Own Until the End of 2027? - The Motley Fool；科技業如何運用 AI 創新應對全球第四次珊瑚白化危機？ - TechNews 科技新報；台股第七大跌點守住 ４ 萬點大關！AI 融資疑慮十大抗震 ETF 出列 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | +79.52% | N/A | 81.88 | 114.68 | -28.60% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | N/A | N/A | 429.56 | 516.10 | -16.77% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -10.01% | +8.95% | 190.01 | 211.14 | -10.01% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -6.38% | -8.33% | 2,200.00 | 2,410.00 | -8.71% | 不適用 | 74.39 | 29.58 | 442.68B TWD / 67.87% | 2026-07-01 |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | -0.56% | -22.92% | 390.54 | 506.69 | -22.92% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -17.11% | +19.65% | 370.32 | 446.77 | -17.11% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | -18.60% | -23.93% | 499.00 | 680.00 | -26.62% | 不適用 | 10.86 | 46.33 | 65.78B TWD / 32.86% | 2026-07-01 |
| 2454 聯發科 | 產業/供應鏈推估 | 0.00 | -16.00% | -18.18% | 3,150.00 | 4,310.00 | -26.91% | 不適用 | 62.91 | 50.20 | 58.01B TWD / 2.80% | 2026-07-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AMD vs. Intel: Which Is the Better Artificial Intelligence Chip Stock to Own Until the End of 2027? - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxOZmlRRXNPT0RKTDhibkh2X0o3ejZGY2FQak8tNzVNclhuQllGRzNzTUNxUnV4TFRkR1ZtVHBBcjVpaVZvQ1pLQlN0VFg4VTRkT2tPc1VydTBrR0tUZmN0STFJckhxa3dCRnU1ZmtOejJaYjVUVnBtZXptUTVRdmpRazI3U1NTZEpEcENSTGlRWGNjNGlGVGJ1WQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 28 Jul 2026 14:49:00 GMT
- [科技業如何運用 AI 創新應對全球第四次珊瑚白化危機？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiwgFBVV95cUxNR0w3ZmJHeXRGM1NWbi0zVTNuSHUzOWlqLTN6a0ZMc2JSSHBzWDhyazEwankzMWhYVWZHY0pOTTlGRUFydUVZRkV5T3NwaGtibEgzRFRVWEZ3a19YOWtSMk0xTi15MGpXSGhYMDFyMmRJYXJ4OFdjRFBJTlByRVFqNVctbFJ1bVp2NmJGdVdISi1rQy1SeDZhUHFXNWhnXzM2cENpRHRST3J6WEZHc1NCa0V3YW5xS2RjT05Kbmd0MnpCQQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 29 Jul 2026 18:15:29 GMT
- [台股第七大跌點守住 ４ 萬點大關！AI 融資疑慮十大抗震 ETF 出列 - TechNews 科技新報](https://news.google.com/rss/articles/CBMia0FVX3lxTE9PcEo5UEJDQTZJYXRmckpFcWNOMFAtZ1E0alpiVFdBZXg0TkF0Wmt5UTJkdGFJdFB6bWNxS0o1UC1vZlhlcGk1TkYtdFZ4dzRNeWFwYzk3TjFPY1ZTR0xLeGFRZjBjTDlmRXh3?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 29 Jul 2026 06:48:24 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：熊本強震考驗半導體供應鏈韌性，崇越科技異地備援供貨無虞 - TechNews 科技新報；強震對全球半導體供應鏈韌性有何影響？ - TechNews 科技新報；《DJ Insight》台積電CPO今年量產，半導體供應鏈新一波震盪- 新聞 - MoneyDJ

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | 0.00 | -6.38% | -8.33% | 2,200.00 | 2,410.00 | -8.71% | 不適用 | 74.39 | 29.58 | 442.68B TWD / 67.87% | 2026-07-01 |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +28.01% | +45.68% | 338.19 | 340.08 | -0.56% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | -6.14% | -5.77% | 237.00 | 289.00 | -17.99% | 不適用 | 14.13 | 16.83 | 821.76B TWD / 52.11% | 2026-07-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [熊本強震考驗半導體供應鏈韌性，崇越科技異地備援供貨無虞 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiiAFBVV95cUxOM0VoRjFKdTRaT0h4MW9RVEEtdmNLeGxxVFFtTXpBMlhQbkp5QzRFQ3hDWUVPT0x6RmlNcFBNTC0zQklhamlMVTdXX1pUbS1HaTgxS1NWMGw3MVktQnhXZGxDMlM1QXRGMkdkanBwOGJSbkFVbXRmOWhHUnVDR2xiZDZXSmNGQjQw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 29 Jul 2026 07:47:48 GMT
- [強震對全球半導體供應鏈韌性有何影響？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMikgFBVV95cUxOUW44Rm53QjdUcTVFVlllM0ZNZUdxaGY4NENVMUljajBsUHQwZjB0WWZiUFRVT2RrbU5yYkpHSHh6YTZZVXlMSldoTVRNNHQxaU1oa21VWk92Wk1rQlpHNkdzMHZtWTdLYzJ5MzlmcjBHdzBmR2ZoV2xnZVJXbk40dWw4bndJeGtiaFlQbkppaUdsZw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 29 Jul 2026 05:22:31 GMT
- [《DJ Insight》台積電CPO今年量產，半導體供應鏈新一波震盪- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPdTd3X2NQdlN2blNEWDZZXzhYYXJZMldjMHFLZXR3VjBETXhmMWczS0NYeUZ3MEtuby1SeFJFU2dOMkVvU041UUFVV0t0WDNtS0Y0U0dETzJIUk9mWW9RQUN5empwdXlNZkRpQThQdHJqUVc5cHVYRDJadUJQYU9fSmVXTWFQVThVLTVtQWNVZ0d0dw?oc=5) - Google News source discovery | MoneyDJ Tue, 28 Jul 2026 00:33:00 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：AI 熱潮才剛開始，市場：晶片如石油將推高通膨 - TechNews 科技新報；Eliyan raises $145 million at $1 billion valuation to ease AI chip data bottlenecks - reuters.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | -0.56% | -22.92% | 390.54 | 506.69 | -22.92% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AI 熱潮才剛開始，市場：晶片如石油將推高通膨 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiekFVX3lxTE1pOE11em90ZmxMZjV0dS1TWmlkTVdwUmp6Ukx5Z2dQSEVZZE5LTHc0aFpXWTJRNi03blJ2MUtVX2FTMjlGRFFmWm5rOW9UZk1MS2MxVmZRNnBnbW9JRjYwOHhPWlNPdXZEU2MwaHo4bzBoMHZlU0JtTlB3?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 29 Jul 2026 04:36:06 GMT
- [Eliyan raises $145 million at $1 billion valuation to ease AI chip data bottlenecks - reuters.com](https://news.google.com/rss/articles/CBMivAFBVV95cUxOUzJETVlDYmVHWnk4Q1lPTmlXNXJ2YWFrMzA2N3dRSWhYYTI1TnNtUkppWG54WW8zRmpQenlTNXhqYVBKUUJILUNUSzRfZHVoaTh1LWxhSFl0ZlN6NE5Lb3o5ZkhyOXNFT3FubnJsOGp5dmNWTWlqeTdpUFpPTDRhWnNrMnE4NXMyTGdHU3FpZVBmcXd5NFE1RXdNdjN2Q0MzRUdOdVFDcXZudEJ5RkZabDFodDl4Unkwc3Nzaw?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 29 Jul 2026 13:08:52 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：AMD vs. Intel: Which Is the Better Artificial Intelligence Chip Stock to Own Until the End of 2027? - The Motley Fool；半導體股遭拋售 資金轉進軟體股、防禦類股？ - TechNews 科技新報；US to award GlobalFoundries $300 million to develop faster AI chip links - reuters.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | +79.52% | N/A | 81.88 | 114.68 | -28.60% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | N/A | N/A | 429.56 | 516.10 | -16.77% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -6.38% | -8.33% | 2,200.00 | 2,410.00 | -8.71% | 不適用 | 74.39 | 29.58 | 442.68B TWD / 67.87% | 2026-07-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | -19.92% | -26.26% | 102.50 | 164.50 | -37.69% | 不適用 | 6.68 | 25.75 | 23.12B TWD / 22.85% | 2026-07-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -10.01% | +8.95% | 190.01 | 211.14 | -10.01% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | +79.21% | N/A | 739.00 | 971.00 | -23.89% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -29.28% | -36.48% | 1,015.89 | 2,335.00 | -56.49% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -17.11% | +19.65% | 370.32 | 446.77 | -17.11% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 2 篇新聞出現相關標籤。

### 主要來源

- [AMD vs. Intel: Which Is the Better Artificial Intelligence Chip Stock to Own Until the End of 2027? - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxOZmlRRXNPT0RKTDhibkh2X0o3ejZGY2FQak8tNzVNclhuQllGRzNzTUNxUnV4TFRkR1ZtVHBBcjVpaVZvQ1pLQlN0VFg4VTRkT2tPc1VydTBrR0tUZmN0STFJckhxa3dCRnU1ZmtOejJaYjVUVnBtZXptUTVRdmpRazI3U1NTZEpEcENSTGlRWGNjNGlGVGJ1WQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 28 Jul 2026 14:49:00 GMT
- [半導體股遭拋售 資金轉進軟體股、防禦類股？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMirwFBVV95cUxPcG9Nc0NuQWpMUVNsaXFiSFVUSzBNTFYtTi1sc3lCQUpwcVFnOUlSdDRBXzhmY2psMzMxck9nYUdqZkZqQ3FfQlBZMWtZX25SUUlDR2VTcjY0NG5RZXpCVXlxblVzS09wZk5CM2l3ZEF2bFVIUUZ1U1VMQVZWdFRNTkhIYjhQUXdpMnJhNkpIemktV3lBb0NoQzFsLUZhTUlkOVQyNW9zSGg3THZ0dEdN?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 29 Jul 2026 06:13:23 GMT
- [US to award GlobalFoundries $300 million to develop faster AI chip links - reuters.com](https://news.google.com/rss/articles/CBMiswFBVV95cUxNOW0tVXFBZ2FXNkREcFU0S3dXaExacjNVemJWU3RsbnhiTTJWdkZram9nb0s2ZFdRVHJLZmM0VHdRTEMzRFpMcV9Ea0hZNEpoeDhlb0Nyc2RzUzBJSHBXckJ3aTIwQ1F6b2lqeEFkbUFNdXIwbEpLV191OTdoS2ZocUFsdXlIaGl1dFNaMDN2STN4ZXRyLThUemlSeVdoUXJMQ3hmUjdQaTR4cURDQ0JRcUpBNA?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 29 Jul 2026 18:53:56 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：US Chip Stocks Slump Pre-Market: Micron Falls Over 5%, AMD and Intel Drop More Than 4% - TradingKey；Prediction: Micron and Sandisk Stocks Will Both Plummet After July 30 - AOL.com；Sandisk vs. Micron: Which Memory Stock Is the Better Buy for the Second Half of 2026? - Yahoo Finance

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | -0.24 | +79.21% | N/A | 739.00 | 971.00 | -23.89% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.48 | -29.28% | -36.48% | 1,015.89 | 2,335.00 | -56.49% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.36 | N/A | N/A | 429.56 | 516.10 | -16.77% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | -0.18 | +79.52% | N/A | 81.88 | 114.68 | -28.60% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -10.01% | +8.95% | 190.01 | 211.14 | -10.01% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、memory」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 4 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [US Chip Stocks Slump Pre-Market: Micron Falls Over 5%, AMD and Intel Drop More Than 4% - TradingKey](https://news.google.com/rss/articles/CBMi3wFBVV95cUxNTG51Z2N1OGIyZllqMXpBYzAtVVJTci1xMzM5UGlDcjR5YXR5NFFGckI5bGU1MmVpbmZ4cXl2SFJadzEweHNvOUN1eUFwaEYzcTVZT21UbFVhNV83NDVsSVlTQnN0ZmQ5aDlvdUJpMUxnVnlNLXhJa1lwMlh2eGxPUkJGY2RNMzFTNUJvcWFnUlZ4cEE5QkJRb2VvQnY3YXlKM2JxSXh3WjVEVjdfb0s1bFNMRGVWV1NzbHczQUticEZXNEd6cC1TbG9pdUR4dTYtclkyWENHV1FhTmxKNUhz?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 28 Jul 2026 08:56:51 GMT
- [Prediction: Micron and Sandisk Stocks Will Both Plummet After July 30 - AOL.com](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPd3FPNU9EQ0NyQW5nSmVVTDQtbnhHNjd5MmhXaDk3eE5LRUFYR0tNRkNUNDBGZ3A0NnFlRHdXSFF0TnJoa3VxbUVxM3hEMDZyaVpRZl95ek1sYW93QmktdGFiWHloODVTY1Q5ZnpSZEswUVpiMXA0S2ROSmtMaDdGRkExY2xqWXE5?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 29 Jul 2026 18:15:57 GMT
- [Sandisk vs. Micron: Which Memory Stock Is the Better Buy for the Second Half of 2026? - Yahoo Finance](https://news.google.com/rss/articles/CBMimwFBVV95cUxPanlPb0wtcWpJNWFaLWJCbnFkT2tiQzdjaVhmbDk4c0xUcjVwTXNSR3VtQ0lvZjBSemttZTJLb1VYR3I1c3RIaDk4MXlNRVhzcjRsaUhfU1lyclNjbkhfWTBnbVk3VXhzTmR0VW50Qm1GaHJCTmN0X1pUVlpTSWtQV05uYkhtQW9PSzF6LWRqNmU2OVpDMUQtVXZqdw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 28 Jul 2026 18:05:00 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：個股動態報導內容-960937A0-2BB4-4486-A34C-67B87D4099BA - MoneyDJ；個股動態報導內容-B9EDFDBD-654E-4E57-89B0-1699626707FE - MoneyDJ；《台股盤後》收跌1564點/史上第7大跌點4萬點失而復得- 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-960937A0-2BB4-4486-A34C-67B87D4099BA - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxQaFBZS3RXZ2tJQTFoOU84aGRBYVhONGtndTJHWlVpTFgxekxwdWs2QWQyMFN2bjBTd2w2aGEyVDFGb095U1FUYkk4b3M4WjNHZ0dpWjVES2p3UktqMEJfTG5sTHZ6V0dDakRPQXdpYjZnQzNQTHBQM2RLTUEtTVBzQ2ZnaFVyR2pTRmhFUUJEMUVrSU9L?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 29 Jul 2026 21:42:49 GMT
- [個股動態報導內容-B9EDFDBD-654E-4E57-89B0-1699626707FE - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxNZDRudlZRUG1LZ1d1d1hfWkRCWE9HZHBTcGpER2R1YWVrMGJNNVd4SE91Vm1uVEV3b2lERTBoNFZsSTh2YU5nUXVEMFRELS1CaDM5V2hzSXNlV2FiVnhDa2xTOWo0N3ZlSXcySUllYTZhUThHeWR1Wkh0clFUYk9CWk9CRURvalpuaHR6cFZUSGdQR1JQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 29 Jul 2026 20:44:41 GMT
- [《台股盤後》收跌1564點/史上第7大跌點4萬點失而復得- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQMHhRNVBYTUxnVnBKQmdCV0ZURm9mUnBMVUp2bUc3VGd4X0NzVDhYamFzV3BGNTNEUFpCZk5TYXBwWFFfQU4zN0hpUjBHanRfeFdnR1dYM1pLLU93R3ZfTkJXMTJGVmc0SkJtdzdrY19jSWx3VmdabXZFZV9UTVNuRUFmZzFEMUJ3SXZOOVR5YWRpdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 29 Jul 2026 07:48:00 GMT

## 新興題材：全球晶片

摘要：新興題材：全球晶片 相關新聞集中在：全球晶片股跳水 台股重挫2,030點 止跌緊盯三個訊號 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [全球晶片股跳水 台股重挫2,030點 止跌緊盯三個訊號 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5KVFF3a0dmT0swSEZEYTRrLVQza3BoclJXem1TVkJma3Fhd3NHUTBtZmh4QzlrVkluenQwTWMtUXhWZ29QdzNLOGlLTFQ4dEJxQncwdWdqTTgzd9IBX0FVX3lxTE5mMkhWNlE3M2NBbDdYeVVCQVRzVlFwRFhfNlFYZDJxMVFjMDEzU2pDa0hXQ25mbk15SlZGUzg1ekJnZlVXVzdySk1iSkJtNkxBRG0wZ2VQTHZpaVgtM0xV?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 28 Jul 2026 17:39:47 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
