# 每日股市熱門話題分析 - 2026-05-24

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **AI 伺服器與資料中心**｜正向｜熱度 13｜市場確認 88.33｜同向 5/6
2. **半導體與晶片供應鏈**｜正向｜熱度 9｜市場確認 86.00｜同向 4/5
3. **記憶體與 HBM 供應鏈**｜正向｜熱度 6｜市場確認 96.47｜同向 2/2
4. **散熱與液冷供應鏈**｜正向｜熱度 2｜市場確認 100.00｜同向 2/2
5. **先進封裝與 CoPoS**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.11（樣本 15）
- 5日相關係數：0.22（樣本 15）
- 同向比例：13/15

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| AI 伺服器與資料中心 | 88.33 | 5/6 | 1 | +14.30% | +8.18% |
| 半導體與晶片供應鏈 | 86.00 | 4/5 | 0 | +13.47% | +9.18% |
| 記憶體與 HBM 供應鏈 | 96.47 | 2/2 | 0 | +8.82% | +29.41% |
| 散熱與液冷供應鏈 | 100.00 | 2/2 | 0 | +14.98% | +8.16% |
| 先進封裝與 CoPoS | N/A | 0/0 | 0 | N/A | N/A |
| 關稅與供應鏈轉移 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：TradingKey | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價呈負相關；應檢查正負向詞庫，並降低新聞直接提及但股價背離的權重。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-05-11 | -0.03 | 0.47 | +85.71% | 14 |
| 2026-05-12 | 0.00 | 0.42 | +78.57% | 14 |
| 2026-05-13 | -0.08 | 0.07 | +58.33% | 12 |
| 2026-05-14 | -0.29 | -0.20 | +50.00% | 6 |
| 2026-05-15 | -0.17 | -0.08 | +58.33% | 12 |
| 2026-05-16 | -0.12 | -0.69 | +33.33% | 12 |
| 2026-05-17 | 0.09 | -0.34 | +40.00% | 15 |
| 2026-05-18 | -0.01 | -0.17 | +33.33% | 9 |
| 2026-05-19 | 0.04 | -0.01 | +62.50% | 8 |
| 2026-05-20 | 0.36 | 0.35 | +28.57% | 7 |
| 2026-05-21 | 0.28 | 0.52 | +45.45% | 11 |
| 2026-05-22 | 0.05 | -0.00 | +33.33% | 15 |
| 2026-05-23 | -0.00 | -0.05 | +84.62% | 13 |
| 2026-05-24 | -0.11 | 0.22 | +86.67% | 15 |

## 歷史回測摘要

- 回測日期：2026-05-24
- 近5日 3日相關：-0.01
- 近5日 5日相關：0.63
- 同向比例：+60.00%
- 權重狀態：已調整

- 方向準確度：+60.00%
- 信心排序準確度：-0.01
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

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel Has Soared 225% in 2026. Here's Where the AI Stock Could Be By the End of 2028 - The Globe and Mail；Is Intel’s (INTC) Confidential AI Push Quietly Rewriting Its Core Investment Narrative? - Yahoo Finance UK；How Intel’s AI Chip Pivot and Foundry Deals Could Reshape the Outlook for Intel (INTC) Investors - simplywall.st

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.76 | N/A | N/A | 119.84 | 119.84 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.09 | +23.47% | +12.66% | 215.33 | 215.33 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.08 | N/A | N/A | 467.51 | 467.51 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.08 | +2.27% | -0.44% | 2,255.00 | 2,255.00 | 0.00% | 同向 | 74.39 | 30.32 | 410.73B TWD / 17.50% | 2026-05-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.03 | -14.93% | -9.08% | 418.57 | 506.69 | -17.39% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.06 | +33.81% | +25.00% | 414.14 | 417.43 | -0.79% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.06 | +18.86% | +2.56% | 561.00 | 561.00 | 0.00% | 同向 | 10.86 | 52.09 | 62.25B TWD / 19.22% | 2026-05-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.06 | +22.35% | +18.40% | 3,860.00 | 3,860.00 | 0.00% | 同向 | 62.91 | 61.51 | 46.74B TWD / -4.14% | 2026-05-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel、INTC」，共 3 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：升級。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：升級。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：升級。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Has Soared 225% in 2026. Here's Where the AI Stock Could Be By the End of 2028 - The Globe and Mail](https://news.google.com/rss/articles/CBMi_gFBVV95cUxOZUFwS0JmVFd6SnhyZFFBNTFXR1cwV1hGcW1mekhPMnpHak9raWd1MkRzY1U3NFhoS1l0NjFTTnRwbDFzeHdSMWJSeXFNcUhVek1FcVo0dXhXMUxjWE0wdjlSUnR2d3R1d3ZXQlRDM1Z1NUhwNlZxNU9GbThxaVpsMHVZaEpoX2NFWno0Vk5zb0F5eWpHdXBmcmprTk92RzFPcFREcF9PbkI2S1VTZ25vTDdueEdtT1RCVU5iZ0FUY0U4UFI2WVVIMXR6VkhweVJLYzBLWVMycTZPckR0R0l3dHRBMnN1U1l3ZU1UYkgzTVdlM0RYcldma3cxajluZw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 23 May 2026 20:09:56 GMT
- [Is Intel’s (INTC) Confidential AI Push Quietly Rewriting Its Core Investment Narrative? - Yahoo Finance UK](https://news.google.com/rss/articles/CBMihwFBVV95cUxQUWViU3lKZVVmTU9Cb0tiOXBudWJUQVpkQXZnb0FBRmNpSWRnOWhNaDFfM29nQjd3cXRUdlEyZUpveW15c0tyWkZHQ0xWa2FiUVVRdkhidTdaTmNwd0dFeXdNTWV2ZUsydGxWNVJfTzV3aFlWNXhrS0ozb3dua1VsMXJMM3NQY0U?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 23 May 2026 15:11:55 GMT
- [How Intel’s AI Chip Pivot and Foundry Deals Could Reshape the Outlook for Intel (INTC) Investors - simplywall.st](https://news.google.com/rss/articles/CBMiygFBVV95cUxQOXMwd0dJck9QVFNIV3I2ZHVnWHRqTExGMHRXREdNZ3dyRHA5ZlBYYjRhWjRpalF0Y3NYWDlnTUtNZi1GOUplaGZ6aGVBVUQxNld2UEdvVVN3UGdDSEQyX0w5R2lBYzBqYlB0SXJxcktWQkF5bWtSUnRERkZBNlpzNlIyZjRYeGp0bTZxT0FrOHZacXJNaVJ1c0NnYi12YlB4X0dLOUowdTdMcHB2Z1dsVUEyeTdzVVhjX2ZLUmtubldQU2c1YlJpcXh30gHPAUFVX3lxTE93MXF3eE9QczdVQ1pZQnJydnJ0ZWhDR2JLUjlXMlVaeURnZXNvcFY4bUpONi1jaE5NUHV2UHVNc2tESnpTYjN6WngzY3FZc3BXUzBtekQxZ3BQOHh1VHctQnM0cE56ekV3R2V1UFRhVlhHZ0dGRHFWY1g1S0YzdkpIWkZxek1VMk9qV1NwenNGQzNucDFEOWFkbGN5VWp2eWdrSXYtNHFkQUhKY2xzNURrTnFkNmF4UThlX3BfNkUxdUdkeFRyQzd2UWVMWmx2TQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 22 May 2026 10:45:18 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：How Intel’s AI Chip Pivot and Foundry Deals Could Reshape the Outlook for Intel (INTC) Investors - simplywall.st；中國聞泰提告安世半導體求償370億元| 兩岸 - 中央社 CNA；陸股劇烈震盪後反彈分析：AI半導體獲利了結陷整理| 兩岸 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.69 | N/A | N/A | 119.84 | 119.84 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.07 | +2.27% | -0.44% | 2,255.00 | 2,255.00 | 0.00% | 同向 | 74.39 | 30.32 | 410.73B TWD / 17.50% | 2026-05-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.05 | +0.88% | +3.64% | 114.00 | 114.00 | 0.00% | 未明確 | 4.00 | 28.64 | 22.66B TWD / 10.80% | 2026-05-01 |
| NVDA 輝達 | 產業/供應鏈推估 | +0.05 | +23.47% | +12.66% | 215.33 | 215.33 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.05 | N/A | N/A | 467.51 | 467.51 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | +0.05 | N/A | N/A | 751.00 | 751.00 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.05 | +6.90% | +5.05% | 1,478.69 | 1,562.34 | -5.35% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.05 | +33.81% | +25.00% | 414.14 | 417.43 | -0.79% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 2 篇新聞出現相關標籤。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 2 篇新聞出現相關標籤。

### 主要來源

- [How Intel’s AI Chip Pivot and Foundry Deals Could Reshape the Outlook for Intel (INTC) Investors - simplywall.st](https://news.google.com/rss/articles/CBMiygFBVV95cUxQOXMwd0dJck9QVFNIV3I2ZHVnWHRqTExGMHRXREdNZ3dyRHA5ZlBYYjRhWjRpalF0Y3NYWDlnTUtNZi1GOUplaGZ6aGVBVUQxNld2UEdvVVN3UGdDSEQyX0w5R2lBYzBqYlB0SXJxcktWQkF5bWtSUnRERkZBNlpzNlIyZjRYeGp0bTZxT0FrOHZacXJNaVJ1c0NnYi12YlB4X0dLOUowdTdMcHB2Z1dsVUEyeTdzVVhjX2ZLUmtubldQU2c1YlJpcXh30gHPAUFVX3lxTE93MXF3eE9QczdVQ1pZQnJydnJ0ZWhDR2JLUjlXMlVaeURnZXNvcFY4bUpONi1jaE5NUHV2UHVNc2tESnpTYjN6WngzY3FZc3BXUzBtekQxZ3BQOHh1VHctQnM0cE56ekV3R2V1UFRhVlhHZ0dGRHFWY1g1S0YzdkpIWkZxek1VMk9qV1NwenNGQzNucDFEOWFkbGN5VWp2eWdrSXYtNHFkQUhKY2xzNURrTnFkNmF4UThlX3BfNkUxdUdkeFRyQzd2UWVMWmx2TQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 22 May 2026 10:45:18 GMT
- [中國聞泰提告安世半導體求償370億元| 兩岸 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE9IU0ZWbVVLdm9pYUdvNXNZbDUteVBzYkVMNTVvSUFHel9ZaWtmcHZOa0NCX05idXlnQjMzM3h6b0VRRHJERWVCUnhESndLQUc1U2I3enQtN1l0dmcwVVE?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 23 May 2026 05:00:00 GMT
- [陸股劇烈震盪後反彈分析：AI半導體獲利了結陷整理| 兩岸 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTFBpVHJTMmRMQU1qNDJBeC0xYWhNQ3JldkpnN3d6VEN2cmpFRTBuRU5lSkdrWFl5TklVdkhMQmt0em9RSGhsY0xocUNnZFNvWWNuMzdVZU1FVmJSYTZ3QUE?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 22 May 2026 09:21:00 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Intel Lands a Preliminary Apple Chip Deal and an SK Hynix Packaging Partnership — Is INTC Still a Buy at $124? - TradingKey；A Billionaire Investor Just Increased His Exposure to Memory Makers Sandisk and Micron. Should Investors Buy the Stocks? - The Motley Fool；SA Asks: What's the best memory chip stock right now? (MU:NASDAQ) - Seeking Alpha

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.76 | N/A | N/A | 751.00 | 751.00 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.76 | +6.90% | +5.05% | 1,478.69 | 1,562.34 | -5.35% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.56 | N/A | N/A | 119.84 | 119.84 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 新聞直接提及 | +0.56 | +10.75% | +53.76% | 308.82 | 308.82 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +23.47% | +12.66% | 215.33 | 215.33 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、MU」，共 4 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 2 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Lands a Preliminary Apple Chip Deal and an SK Hynix Packaging Partnership — Is INTC Still a Buy at $124? - TradingKey](https://news.google.com/rss/articles/CBMi7gFBVV95cUxNTGpHN3o3WGJhaU1Nbld3bC03TnZpTlhfRXNCeU1Oc0QzRTlyelo3VjNvN0Nucjd5UWpkTDB5S1VPMVlRcHhfekg0U01ZbnoxNTRrbU1UdE11R3FQX3lIX3J3eFN0OUFjaENlM2ZlSjg0UkFIbGoxMGNPdXRrZFdVcEIxWTZfNlNRRG1fQXA5X1VoLUNMQklucVppVl9mVFc1cVBsNV95V1FqUWpLdEExZHZQTm5NM0RVQzRucC12MGthOVVXdEhsTUVWR1FNWjVhdDRXelNuTzNVbHpqSWJiamFFVmI0NTFGRjdwQTFR?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 23 May 2026 04:17:03 GMT
- [A Billionaire Investor Just Increased His Exposure to Memory Makers Sandisk and Micron. Should Investors Buy the Stocks? - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxPUVBOYTlGSEl0VWFGX2hjU0I0ejFnMWJ6Q3c0N2I4NmZpYjQyZFN5RlpObGtXVjhqR2t5dllaTzlOR3Rya005dnIwN0tXYzhPZUFEQ1FDQkpDZUhENVVhaDM1TW5ybEZqaHdDTEptWFo2bEluSkFUdF9xb25rTkpFYXdZeGF4TjRST285SWxxNjJCcGd5QThzcQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 23 May 2026 12:45:00 GMT
- [SA Asks: What's the best memory chip stock right now? (MU:NASDAQ) - Seeking Alpha](https://news.google.com/rss/articles/CBMikgFBVV95cUxNX21SMDFpcS1mRE1wUENtQnAteEtiaTk2Z0VsVHFGOWhPSlNMdE9kVEtyTHR2TkVPWDkyNi1ic3BkbmpHZS1EdUIybkRtSnJjcHdOUVhFWjh2dmFJcmc2b0otZnZBcE1YaHRDd08tMjdWZWZld0ljdmI2TWlXVzhuNG9BU0dtdVVFcEp3U1pvMTIzZw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 23 May 2026 15:00:42 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：輝達新一代 AI 平台 Vera Rubin 報到 電源、散熱鏈含金量大增 - 經濟日報；崇越在先進封裝與散熱材料佈局具備哪些優勢？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.67 | +6.49% | +3.67% | 2,545.00 | 2,835.00 | -10.23% | 同向 | 61.06 | 41.82 | 15.63B TWD / 71.62% | 2026-05-01 |
| NVDA 輝達 | 新聞直接提及 | +0.56 | +23.47% | +12.66% | 215.33 | 215.33 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 2 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：大增。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：大增。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [輝達新一代 AI 平台 Vera Rubin 報到 電源、散熱鏈含金量大增 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE16LXJSNWVzS1hIQXlmd3lNWmVwXzdTQmhpcjhMTVpIenhHU3I2Tk5QaXVBc0hyZVo2em83VE95OUl1UVlwMUZUN0ZzM1hjbnNLb252WlFXREVYd9IBX0FVX3lxTFBuaVRLMy1fQno0VWxmS2I4bmlxdWVsWXJPN3Z0YXZ6OE94R2hYMjVuT0FWaTktVWF4eVFsY2t6bjdQbzF0R0tOdkxESXFLNTVGQmROZXRGRHppdEh5S2xj?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 22 May 2026 09:00:00 GMT
- [崇越在先進封裝與散熱材料佈局具備哪些優勢？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMingFBVV95cUxPRFdobWx1eWctdkd1U2hoakJFWThHNDB6QUFOaVlDOFFmS0FHX2Z3Zm5NVjVsb2hnVHNTU00zVU5GS3djUFBoei1NbkZ1ZDJ6MkZmTzdHVTJfM0t2Y3U1Zk4tVHk2Z2o1MGJmZ3lWX05nRTc4RFAzTDlibWQtczdHdkQ0UkZTV1R5VG5SMW45dkhqRHI5Zm9sZFNFRVVaUQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 23 May 2026 18:39:45 GMT

## 先進封裝與 CoPoS

摘要：先進封裝與 CoPoS 相關新聞集中在：崇越在先進封裝與散熱材料佈局具備哪些優勢？ - TechNews 科技新報；AI 重塑半導體結構3／先進封裝抬頭 需求年增20% - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | +6.49% | +3.67% | 2,545.00 | 2,835.00 | -10.23% | 不適用 | 61.06 | 41.82 | 15.63B TWD / 71.62% | 2026-05-01 |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +2.27% | -0.44% | 2,255.00 | 2,255.00 | 0.00% | 不適用 | 74.39 | 30.32 | 410.73B TWD / 17.50% | 2026-05-01 |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | +18.86% | +2.56% | 561.00 | 561.00 | 0.00% | 不適用 | 10.86 | 52.09 | 62.25B TWD / 19.22% | 2026-05-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 1 篇新聞命中。
- 2330：產業/供應鏈推估：公司標籤符合「先進封裝與 CoPoS」關鍵字 advanced packaging, CoWoS, CoPoS, FOPLP；其中 0 篇新聞出現相關標籤。
- 3711：產業/供應鏈推估：公司標籤符合「先進封裝與 CoPoS」關鍵字 advanced packaging, CoPoS, FOPLP, panel-level packaging；其中 0 篇新聞出現相關標籤。

### 主要來源

- [崇越在先進封裝與散熱材料佈局具備哪些優勢？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMingFBVV95cUxPRFdobWx1eWctdkd1U2hoakJFWThHNDB6QUFOaVlDOFFmS0FHX2Z3Zm5NVjVsb2hnVHNTU00zVU5GS3djUFBoei1NbkZ1ZDJ6MkZmTzdHVTJfM0t2Y3U1Zk4tVHk2Z2o1MGJmZ3lWX05nRTc4RFAzTDlibWQtczdHdkQ0UkZTV1R5VG5SMW45dkhqRHI5Zm9sZFNFRVVaUQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 23 May 2026 18:39:45 GMT
- [AI 重塑半導體結構3／先進封裝抬頭 需求年增20% - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE0tU2RpWTZablFIRTR1VHI0eU9sZUxxekJFaXczR0RVZ0FINzVLUEsxQmp1TWtES3duT2lBZkcxUGNXSTJzTTY0N3RGelczUEZKaGRoUjZJTUo4d9IBX0FVX3lxTE1pMlRNYzNBNVJVSWFQWDBFUlB2RUttZEpQMUkzV2s0bHBEaXctUEhfY2lOVUx6Mzg3cE5CU3BWOWp1VFAyaGMycEF0elBFVUZ1djZVdWdBUHlIcE4xdnhB?oc=5) - Google News source discovery | 經濟日報 money Sat, 23 May 2026 02:00:00 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：美貿易代表：半導體關稅重要但近期不會加徵| 國際 - 中央社 CNA；崇越轉型整合平台，對半導體供應鏈有何意義？ - TechNews 科技新報；AI繼續帶台股衝？黃仁勳抵台洩口風：台灣供應鏈「下半年會很忙」 - Yahoo股市

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +10.75% | +53.76% | 308.82 | 308.82 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | +2.04% | +0.60% | 250.00 | 257.50 | -2.91% | 不適用 | 14.13 | 17.76 | 832.10B TWD / 29.74% | 2026-05-01 |

關聯理由（前 3）：
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [美貿易代表：半導體關稅重要但近期不會加徵| 國際 - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5CMVJjNWxnemNEVHFVWTJJdjZyRDdlU05SVFBYb3o4UEZWZUpVTnVVdldfaFlVVzFSbl85dHp2WEY2YmtDcEhBRUxmVEUwZF9WU1N3X0gwR2RoN210Zi1Z?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 23 May 2026 04:23:00 GMT
- [崇越轉型整合平台，對半導體供應鏈有何意義？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMingFBVV95cUxPMC0tajZzR3VWaVNxUV91R1d2dHl3MWZydFlHWjVFdk1qQy1rLUZTTjJHY3VnZFN3TzhSTHYtbDhtb1hLRWhvTzFFZGxFNVRnYmNIcUViMTdDbGNxQWNJVXozNXFMb1R3TklKSmprd1d2YW9Tc1VYN0FCTVREQUEwZGZsMkdNbTVzUkJSUnpFbnVsMzRvX0VmUmY5d2ZsUQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 23 May 2026 19:06:40 GMT
- [AI繼續帶台股衝？黃仁勳抵台洩口風：台灣供應鏈「下半年會很忙」 - Yahoo股市](https://news.google.com/rss/articles/CBMijgNBVV95cUxOTmVrOEthSm9aVVNBVVRTVkphRVlzellBWFlRRGFKYmJucEN2ZWNOT21RT2ViZkVfZ192eWkwM21NTk9ITVJuS3d3YzBoUnpxd1E1QzlVSXVJUEZJUGxaMUxFQ3pISllyYnBFc2pmckttX1o2WUxYT1M5bnFjcGdmUmd1ek0yeDA1blJYY3lzb0hfalk4dXhsM1lQVTNVUUFGUllOSE9uZFRHbGhJdlp6dTdCRXV0UDNvaVlCUncwOFlKaHM1OHVUTFB3WkJlQmtSTXlXcUxMVFc5ekU3d3FuazROaUIzbk1DODRvb2NyYkRuaTlaSVN3dkIyM3k3RXFWc004a1hSX0RSMzNnM1RDVE1WVF9vdTdPTzlTcDdDbFIzbHIzSTFjbXFRQ1hwQlVneEpCMGI3emY2aFhZNEtpamF4Q2hnajlUYi1Jc0V6cjBXd0ZmODNDb2h5NFRqa09jNGlSUXdVZnVQd0FJYi1zb1o3VU1URlJoOERJeWFNbkhnY1o3TGhaaGFLNlB0UQ?oc=5) - Google News source discovery | Yahoo 奇摩股市 Sat, 23 May 2026 12:42:31 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Intel Lands a Preliminary Apple Chip Deal and an SK Hynix Packaging Partnership — Is INTC Still a Buy at $124? - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 119.84 | 119.84 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 新聞直接提及 | 0.00 | +10.75% | +53.76% | 308.82 | 308.82 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AAPL：新聞直接提及「Apple」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Lands a Preliminary Apple Chip Deal and an SK Hynix Packaging Partnership — Is INTC Still a Buy at $124? - TradingKey](https://news.google.com/rss/articles/CBMi7gFBVV95cUxNTGpHN3o3WGJhaU1Nbld3bC03TnZpTlhfRXNCeU1Oc0QzRTlyelo3VjNvN0Nucjd5UWpkTDB5S1VPMVlRcHhfekg0U01ZbnoxNTRrbU1UdE11R3FQX3lIX3J3eFN0OUFjaENlM2ZlSjg0UkFIbGoxMGNPdXRrZFdVcEIxWTZfNlNRRG1fQXA5X1VoLUNMQklucVppVl9mVFc1cVBsNV95V1FqUWpLdEExZHZQTm5NM0RVQzRucC12MGthOVVXdEhsTUVWR1FNWjVhdDRXelNuTzNVbHpqSWJiamFFVmI0NTFGRjdwQTFR?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 23 May 2026 04:17:03 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：法人專欄分析-台股 - MoneyDJ理財網；‧永豐期貨盤後分析 - MoneyDJ理財網；《台股盤後》大漲899點、首收42K；週K翻紅-新聞內容-基金 - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [法人專欄分析-台股 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMiiAFBVV95cUxQdWR6NUs2MGl2RkdzMU91NlYtOUtNR3hnNHQxZ0hRVVFLNVp1dmd0ZmZnWm5FRTdramd6SW45dlRsWEtzSWVTVkhEaHNFeHZEYmFVUDV0YWprUnlqZnAtOEoybUNfbWRsQlR4Y1RoWTk5eTFQS0lTZ2pKN1o5cnpMSXVXeWtjTTdN?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 23 May 2026 02:48:04 GMT
- [‧永豐期貨盤後分析 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikAFBVV95cUxOY0luQ0tTdF9GdTJLMkNUdlF2bWlBQUZZZlJSMWFfamtXU19nQXdqZ04wN1hVUVJYb0pya1hELUhqa2JkTWhvdG9VeTF3UGY3aFNFNlNwVm9uYjJOZmRvQ0gtRnpISzI5ZUxGSVNsUk1rNGI1T09ORnd6YjZ6UW9LMk16NnQ2Rzl2STFwZHhjX3g?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 22 May 2026 15:33:45 GMT
- [《台股盤後》大漲899點、首收42K；週K翻紅-新聞內容-基金 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMimAFBVV95cUxQcXh4WmJhNVJsQlVsT2NQT2E4NkZFY3VDRkl4N3hHLXdfbUswTmxXbERUNnRBaFllSS1qczhJY3NUSFMzbDNhcWFFMG12NXExeW83X19SVnpWcHh1U3ZmcVFzNFpydFVkemltYWE5dmc2MXRESWRVeFFrOWt4ZjZIbmxlOTZvMUE3R2kzUGRYX0g0T1ZjNkZIQg?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 22 May 2026 08:07:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
