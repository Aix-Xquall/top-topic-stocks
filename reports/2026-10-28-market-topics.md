# 每日股市熱門話題分析 - 2026-10-28

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **利率與成長股估值**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
2. **AI 伺服器與資料中心**｜正向｜熱度 18｜市場確認 14.99｜同向 2/8
3. **半導體與晶片供應鏈**｜正向｜熱度 6｜市場確認 12.34｜同向 1/3
4. **記憶體與 HBM 供應鏈**｜正向｜熱度 8｜市場確認 0.00｜同向 0/3
5. **關稅與供應鏈轉移**｜正向｜熱度 1｜市場確認 0.00｜同向 0/1

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.30（樣本 15）
- 5日相關係數：0.47（樣本 10）
- 同向比例：3/15

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 14.99 | 2/8 | 5 | -0.84% | -0.52% |
| 半導體與晶片供應鏈 | 12.34 | 1/3 | 2 | -3.66% | +8.92% |
| 記憶體與 HBM 供應鏈 | 0.00 | 0/3 | 3 | -4.85% | +0.24% |
| 關稅與供應鏈轉移 | 0.00 | 0/1 | 1 | -1.29% | +8.92% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：中國需求 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價呈負相關；應檢查正負向詞庫，並降低新聞直接提及但股價背離的權重。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-10-15 | -0.08 | 0.08 | +33.33% | 12 |
| 2026-10-16 | -0.13 | -0.25 | +64.00% | 25 |
| 2026-10-17 | -0.10 | 0.49 | +26.32% | 19 |
| 2026-10-18 | -0.12 | 0.33 | +21.74% | 23 |
| 2026-10-19 | 0.44 | 0.36 | +50.00% | 12 |
| 2026-10-20 | 0.09 | -0.81 | +69.23% | 13 |
| 2026-10-21 | -0.25 | 0.23 | +5.56% | 18 |
| 2026-10-22 | 0.02 | -0.21 | +38.89% | 18 |
| 2026-10-23 | 0.35 | 0.29 | +78.95% | 19 |
| 2026-10-24 | 0.09 | -0.31 | +70.00% | 20 |
| 2026-10-25 | 0.41 | 0.78 | +64.29% | 14 |
| 2026-10-26 | 0.27 | -0.25 | +36.36% | 11 |
| 2026-10-27 | 0.07 | 0.31 | +50.00% | 18 |
| 2026-10-28 | -0.30 | 0.47 | +20.00% | 15 |

## 歷史回測摘要

- 回測日期：2026-10-28
- 近5日 3日相關：0.09
- 近5日 5日相關：-0.14
- 同向比例：+54.55%
- 權重狀態：未調整

- 方向準確度：+54.55%
- 信心排序準確度：0.09
- 診斷：低相關

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

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：《貴金屬》通膨憂慮緩解 COMEX黃金上漲0.9%-台股 - MoneyDJ；台股5萬點不遠了？童子賢看好台積電全年EPS衝百元：本益比不算高 - Yahoo股市

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | 0.00 | -0.21% | -0.83% | 2,400.00 | 2,480.00 | -3.23% | 不適用 | 86.28 | 27.82 | 511.86B TWD / 54.65% | 2026-10-01 |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +18.01% | +7.99% | 531.33 | 531.33 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [《貴金屬》通膨憂慮緩解 COMEX黃金上漲0.9%-台股 - MoneyDJ](https://news.google.com/rss/articles/CBMiigFBVV95cUxOSDBvTVVuUGJBSlBKcUxXV0N1MVBiUXF5bUcwZWo1Skk0MHN0X3YwMTFKZXhfaE44RDRQTmxTcGctbDdwN3Q0Y0FURVlSaGo3ODdyRFQ5bl9pX1A4UUFvMjFPdUg5ODZITmNLVzI2QlRSWWJCcVZ1VXNfTXR2SE4zaTBXRklMTXVzNnc?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 27 Oct 2026 22:16:33 GMT
- [台股5萬點不遠了？童子賢看好台積電全年EPS衝百元：本益比不算高 - Yahoo股市](https://news.google.com/rss/articles/CBMisANBVV95cUxQeFgwTzhab2w5aFYzaXh5MFNnLWU5VHZuc3RPUGREMjVYa1dvQkRkNExyczlkTFRRNHdnVXFtVWYxLU5OZzNKdU0yRThUUUZXcHVEYlpseFRNNnpjUURkOXlNS3NzUFpFNUpwcDNnWUxTV2RUdEJfclI3NFk5Z0NIZlhYUWtpRlpRek9UYmJSR0JEend1dnBiWGJlX2FPNzFCR0hldU9RU1drOGZkeHFGcmVvT1FERVBmbm1kN2lweUR2VEZYN3kxcnlncGFUcVZZV0NkeTlfakFIRFFKS0kxU1B3SjZndUs5WE1XaXJremhadVRWVXBxNTM2YzdqOXRzZDNqV3ZoZnRxUmlJV2hoT01uc0s0VnBZdXliZm5KYUphdU5tZ213eVlQOC1UamJla1prS2FDbGtBM3lqdHlFdnZzS2RyRnVjU0lVRGVZcHdxdWx0Q3FSYm9maXEzMHBmQW50Y09pODlTOXdyZWxuejgzSW5JY1pmTk5HcWFWWU5JR0ZHMk5XSVhqQ3BFY1poc1RRTzZBVUdlYWxKYURiNVYyX2VMdUJHYTVhZHdrOE0?oc=5) - Google News source discovery | Yahoo 奇摩股市 Tue, 27 Oct 2026 03:20:47 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Can Higher Data Center Revenues Propel Intel's Q3 Earnings? - TradingView；Intel Rises 5% as New Street Upgrade Cites Server CPU Shortage; AMD and NVIDIA Gain 3% - 24/7 Wall St.；Intel: Agentic AI Is Making CPUs A New Bottleneck (NASDAQ:INTC) - Seeking Alpha

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.28 | -18.26% | N/A | 93.74 | 114.68 | -18.26% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.28 | -1.29% | +8.92% | 217.94 | 228.38 | -4.57% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.53 | +8.56% | N/A | 560.26 | 560.26 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.04 | -0.21% | -0.83% | 2,400.00 | 2,480.00 | -3.23% | 未明確 | 86.28 | 27.82 | 511.86B TWD / 54.65% | 2026-10-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | +18.01% | +7.99% | 531.33 | 531.33 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -7.56% | -9.38% | 342.33 | 446.77 | -23.38% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.02 | -1.36% | -2.98% | 651.00 | 703.00 | -7.40% | 背離 | 13.92 | 47.11 | 88.13B TWD / 45.52% | 2026-10-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.02 | -4.58% | -6.82% | 3,960.00 | 4,920.00 | -19.51% | 背離 | 60.69 | 65.40 | 55.40B TWD / 1.97% | 2026-10-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel、INTC」，共 3 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：shortage, upgrade。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA、輝達」，共 2 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。 方向判斷命中詞：shortage, upgrade。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。 方向判斷命中詞：shortage, upgrade。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Can Higher Data Center Revenues Propel Intel's Q3 Earnings? - TradingView](https://news.google.com/rss/articles/CBMitAFBVV95cUxQQURNNUYtWE4zX0VXbDhMcmhBZnNQcVNwQjJlNWJoRy11VjlEY3UwUTFEdlhFVXM4ZjNSS2xKZjNEQV8xSjRLQXFyVXNLRDhYNTMzTW5ENkNFVnJ5Q1NJMzJoNjUyQU1HSjVtT08zcERlOHBGUWs2cGphRG1yY3JSUVBZOUcxT2dGdTl2b2M3N1prM0NNcVhNN2tBZHU4bG9ZMjdwWWktQ05hREV4RlZuc0UwYlc?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 27 Oct 2026 16:37:58 GMT
- [Intel Rises 5% as New Street Upgrade Cites Server CPU Shortage; AMD and NVIDIA Gain 3% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMixgFBVV95cUxNTWpBX0ZyOWZISEViUlRGWExyVWc0WXFYNFNaMm1YTGg1dnZzYlhLaGs1Zm9Ob01TZlhWOVQxVm11NVh3RmltV2hab040ODlWTWthc01oVnp6YTVqM2Y2TEx4SllpcVNVVjNpd1FUYlBlYmhMZ2E3THdYeWpzOFctYXNBY2Flamw0STlONXBrajNHM1huMjRkQ1ZBNDY1dkd5VXRjT0FzbWdQcXN2MnJrVnVDdzdsaEpySXREZWQ5MVZUSmFteEE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 26 Oct 2026 18:50:00 GMT
- [Intel: Agentic AI Is Making CPUs A New Bottleneck (NASDAQ:INTC) - Seeking Alpha](https://news.google.com/rss/articles/CBMijwFBVV95cUxPckJrNDZtMnl3ZmFVTnp2UUEwSG5YNGVkWFhRQncxazBYWlF2S0ZLQmVqQ0lvZC1sNHktTTk2SldMT2xqZ3hITFUxa0x0b01hblN1WWc0XzlJOUkwRHItelozdGNDbm1ReXJhX3dCMDZBdGpmMkdrck0zT0tHS1RLRXdGY1pFalR1V2FuM1BTVQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 26 Oct 2026 18:05:42 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel Rises 5% as New Street Upgrade Cites Server CPU Shortage; AMD and NVIDIA Gain 3% - 24/7 Wall St.；要開天窗？越南首座半導體廠明年試產難未敲定ASML設備採購- 國際 - 工商時報；外資今年賣超台股破2.2兆創高！上周賣超前三名全是晶圓代工股- 證券 - 工商時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.26 | -18.26% | N/A | 93.74 | 114.68 | -18.26% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.23 | -1.29% | +8.92% | 217.94 | 228.38 | -4.57% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.45 | +8.56% | N/A | 560.26 | 560.26 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -0.21% | -0.83% | 2,400.00 | 2,480.00 | -3.23% | 不適用 | 86.28 | 27.82 | 511.86B TWD / 54.65% | 2026-10-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | -3.54% | -7.89% | 122.50 | 164.50 | -25.53% | 不適用 | 6.68 | 18.42 | 25.35B TWD / 27.22% | 2026-10-01 |
| MU 美光 | 產業/供應鏈推估 | 0.00 | -4.35% | N/A | 928.76 | 971.00 | -4.35% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -8.90% | -8.43% | 1,255.58 | 2,335.00 | -46.23% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -7.56% | -9.38% | 342.33 | 446.77 | -23.38% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：shortage, upgrade。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：shortage, upgrade。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：shortage, upgrade。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Rises 5% as New Street Upgrade Cites Server CPU Shortage; AMD and NVIDIA Gain 3% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMixgFBVV95cUxNTWpBX0ZyOWZISEViUlRGWExyVWc0WXFYNFNaMm1YTGg1dnZzYlhLaGs1Zm9Ob01TZlhWOVQxVm11NVh3RmltV2hab040ODlWTWthc01oVnp6YTVqM2Y2TEx4SllpcVNVVjNpd1FUYlBlYmhMZ2E3THdYeWpzOFctYXNBY2Flamw0STlONXBrajNHM1huMjRkQ1ZBNDY1dkd5VXRjT0FzbWdQcXN2MnJrVnVDdzdsaEpySXREZWQ5MVZUSmFteEE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 26 Oct 2026 18:50:00 GMT
- [要開天窗？越南首座半導體廠明年試產難未敲定ASML設備採購- 國際 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1PN3M4TGJxV1lXQWlMUERWSUJlemxzcmVjYnR4VWszMWNITHctSjdwRXZINVVmcE9zSktVWTJOS3N5LTh3YjFpSWlkdFdESGZ0V3JwRTBRdXBVRVhaNjlV?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 26 Oct 2026 10:59:00 GMT
- [外資今年賣超台股破2.2兆創高！上周賣超前三名全是晶圓代工股- 證券 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5RZnBkeHlMN0RnTFBlaUJZUzhKM0tOTGYybVU4cnNsYXNtMVRRV3ItSEtJSVJ5WDZVRmNsQzc2XzlwZkR4Q2QybEo2OEtxTFQ1eG8tRVVVVURSWWdxUVRR?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 27 Oct 2026 07:48:00 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Here's What $1,000 Spread Across These 4 Memory and Storage Stocks Could Be Worth by 2030 - AOL.co.uk；Here's What $1,000 Spread Across These 4 Memory and Storage Stocks Could Be Worth by 2030 - The Motley Fool；Is SK Hynix Stock a Buy Before Q3 Earnings? Key Tips to Note - TradingView

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.28 | -4.35% | N/A | 928.76 | 971.00 | -4.35% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.26 | -8.90% | -8.43% | 1,255.58 | 2,335.00 | -46.23% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.21 | -1.29% | +8.92% | 217.94 | 228.38 | -4.57% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「memory、Micron」，共 3 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 1 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Here's What $1,000 Spread Across These 4 Memory and Storage Stocks Could Be Worth by 2030 - AOL.co.uk](https://news.google.com/rss/articles/CBMie0FVX3lxTFBrajFCWmtjLUR4bjM1Y1g5d0ZhanZYb1d4aUtJbHRBNFdjWmhaTTNheHAtY3NjXy1aakVrakJqRlRQQ09oWUtwRmt1TExoVHdaSHRiTzFzd1Z5SGl2bWhNblRKNjVtMzhZUVJkUGZUQldjZW9ON1BzRWctUQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 26 Oct 2026 10:20:00 GMT
- [Here's What $1,000 Spread Across These 4 Memory and Storage Stocks Could Be Worth by 2030 - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxOMlV1b2lRZFZMdVlkWkpBTk96YkxQTy1nc3czclQ3RnBYb1ZVbUdMa1p2MXRZNDNxb19hcXo4OEN1WUNnaXVJQk5hQWNHb2k3NTJRSzNNMWx2MDBmSXNwbUZONlRLYTdrUDZwM3JCZGlBejVsZ3NKdXlUYTlWY1BoczA2Wm1oQXN6T194M0xPWjhxMkg0dVJFVA?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 26 Oct 2026 11:00:00 GMT
- [Is SK Hynix Stock a Buy Before Q3 Earnings? Key Tips to Note - TradingView](https://news.google.com/rss/articles/CBMitAFBVV95cUxOc05UaWJBWkVSVnpMUGV3enZzRXF3bTloTGFRODVSQWYwUnU1S2pmN0haUU9nd2RkQXB3RWhYMktPRURFQmxTYl80MnFxbzJBb1FBWWx1WFF5NDRIR3hsemJ0SFQ3ZmdCNXNBdGt4SjNXY3hwVnFMblBRVzRoaWpEQ1FMZ2hmVldNUHNMRDlpdVkyN1BkeGlzUjRkYU5IbHlpUHB4TTNaa01lSk1CTGpFYlk3aHg?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 27 Oct 2026 12:24:00 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：整理包／黃仁勳概念股笑了！輝達季度財報超預期 完整台廠供應鏈名單、潛在受惠股一次看 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.21 | -1.29% | +8.92% | 217.94 | 228.38 | -4.57% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +11.23% | +24.48% | 347.10 | 347.73 | -0.18% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | +2.48% | +1.43% | 247.50 | 289.00 | -14.36% | 不適用 | 15.21 | 16.32 | 1158.63B TWD / 38.42% | 2026-10-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [整理包／黃仁勳概念股笑了！輝達季度財報超預期 完整台廠供應鏈名單、潛在受惠股一次看 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBQUlViSHpPeDVlY29yaHFNNE5NcVlUQnE3ZThTcXRGNHgxYTVPOVVTRDlaTDV6Zml5WEwxVHNSeGFDcnVHUHhRSW15SzNpU0dYVDU3dThWNEVCbkZI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 26 Oct 2026 09:00:00 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：PCB/CCL 受惠於供需吃緊 大摩及高盛一致看好這三檔台股 - 經濟日報；外資退居配角？投信大買236億元、自營商賣超124億元 台股震盪908點收高 - 經濟日報；00415A新兵加持 台股 ETF 受益人檔數雙創高 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [PCB/CCL 受惠於供需吃緊 大摩及高盛一致看好這三檔台股 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBZR1doUmZ6Wk9pdlRzNGQwcVYzXzB1TmxHZmdZNERjR2RsdEhwMVR6aUNHc0ZqRmZKOHNxNXpTTWwxU3c4NlotbTJhQzd1T01VU0pBZ1AxdENXUdIBX0FVX3lxTFBkRG1tU2N0STJHSmpHUmpYemFFWDNFSGNTNmJBWW5hQ2VpQ3lOUkRWLWNKY01iUzZ4VmlWaWR2ZlVPSDlXTGhXcmgzanN4WGNjMnRiVzdodUwteUdwRGVv?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 27 Oct 2026 09:00:00 GMT
- [外資退居配角？投信大買236億元、自營商賣超124億元 台股震盪908點收高 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1kM0NJeUNxNi1XQWdEQmZtX2d0V3J5YVFDN0pYUkwyTVhoVVh0b0ZFSFFUcWZ6ZXdLNldQOUZFWWg0Q0IwWnRWcTh3T2trSWlQM0Z2NkZKUjg3Z9IBX0FVX3lxTE9nMnM1SUZ5Y3hpTnRMa29PZy1uaVpwVTY4RmFhQ2RiLXZ6S1NDVjIwUjczSXdXRENzNE0zUms2RWNiUVBmcGxvdlBYVHAyRVRXX3dJSWZ1SElaWkoya1BZ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 26 Oct 2026 09:00:00 GMT
- [00415A新兵加持 台股 ETF 受益人檔數雙創高 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE54M0pJbVVzaDR2NURyXzIyN0hWZXp2amJ2am5hWWFYR3RhOVlqbDZGZFk3RU9BdlJYeU1TbXFLV1dwOUdMLURvVEJFZFRvUHVKR2UxMjhWVHJGZ9IBX0FVX3lxTE5Jcnhfd042LVprWXh6Qk1lMGJLZ0VfR2JyM2k2Qlo5TnhHdkdLSEp5NEo2VjhwOFh1MHdlOHFBbGYzMDNjS3lrcGNnaDBmV0E2THFwaXdxQ2JwNlNZSkZN?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 27 Oct 2026 09:00:00 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：法人專欄分析內容-台股 - MoneyDJ；《台股盤後》收漲54點、日K連二黑，季線得而復失- 新聞 - MoneyDJ；臺指期、電子期近月盤後收盤價-台股 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [法人專欄分析內容-台股 - MoneyDJ](https://news.google.com/rss/articles/CBMijgFBVV95cUxOVTN4OHNSTXpqbnczQXBqS2hEY0ZUUjdaN2RtRTV3LXM1RXhZZHg3SzZHUEs3V0JucExkQWlBeUEyMFZNRE5nbzgyOXA0ZjR5WkpsdUlPY2F2eGREWjdLa1RQcWQ4VUhNRmM3alRRdy04cEVZd0FwSS1HOVM0aVN3WlRNejZSNEp3bXJRejB3?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 27 Oct 2026 16:17:11 GMT
- [《台股盤後》收漲54點、日K連二黑，季線得而復失- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxObVBlVFdLUjhzckI0OWtqbGJ3aE5WczBZLWdjWkRyOENMRjhSVWRNNWpJQlRNZlNPb21aRkUwMTRrTjhuQXdqMmFsU1FJbzBmbVV0YkVseU1hUGtTcHN4dlNtUGVCZXlNY29Fb2VqbG5PX25GdThfSGJQOGZRZUdTekpmbFpWdXlUTWo0ZGt5aHhyUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 27 Oct 2026 08:00:00 GMT
- [臺指期、電子期近月盤後收盤價-台股 - MoneyDJ](https://news.google.com/rss/articles/CBMiigFBVV95cUxPNVRfTVNPelRENHdUQ3FzaEd0amotYmp4T3hYMFg2YUNzcE4tUzA5WXBKeVJRRUVYeEt5OFgxM2hCUHFyNFhrSVdjMHJ1RlJ6Zmw5YTBhYnlnVnUxNzVSZGJkS2tUWVp0aXlkd3NEYks1dXcxSGxxX3Q3cFZWczZqcXFTYzZJa1RYbUE?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 27 Oct 2026 23:51:32 GMT

## 新興題材：中國需求

摘要：新興題材：中國需求 相關新聞集中在：《金屬》中國需求帶動 LME基本金屬多數上漲-台股 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《金屬》中國需求帶動 LME基本金屬多數上漲-台股 - MoneyDJ](https://news.google.com/rss/articles/CBMiigFBVV95cUxNeDhaXzQ3MktPTk9GeFlpMkFtYThGQkJycExsQnl6RkhwNnZ1WmJDcEFYZFctTEtHZ210TVdsRjl1LWJQbDJtVUducHhIRTZkdzZ4aUE4ZXZrVDdpano4NDVudzRLVzlTT3o3N1UtTTRCY18tejZWY2pEN3pITmhJYzgyUVhHOWx4RXc?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 27 Oct 2026 22:16:26 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
