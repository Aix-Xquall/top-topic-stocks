# 每日股市熱門話題分析 - 2026-09-01

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **AI 伺服器與資料中心**｜中性｜熱度 14｜市場確認 N/A｜同向 0/0
2. **關稅與供應鏈轉移**｜正向｜熱度 2｜市場確認 N/A｜同向 0/0
3. **利率與成長股估值**｜正向｜熱度 2｜市場確認 N/A｜同向 0/0
4. **散熱與液冷供應鏈**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
5. **半導體與晶片供應鏈**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：N/A（樣本 2）
- 5日相關係數：N/A（樣本 2）
- 同向比例：1/2

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| AI 伺服器與資料中心 | N/A | 0/0 | 0 | N/A | N/A |
| 關稅與供應鏈轉移 | N/A | 0/0 | 0 | N/A | N/A |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 記憶體與 HBM 供應鏈 | 20.91 | 1/2 | 1 | -4.70% | -1.07% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-08-18 | 0.29 | 0.36 | +80.00% | 10 |
| 2026-08-19 | -0.23 | -0.33 | +30.00% | 10 |
| 2026-08-20 | -0.72 | 0.06 | +50.00% | 8 |
| 2026-08-21 | -0.48 | -0.45 | +61.54% | 13 |
| 2026-08-22 | N/A | N/A | +50.00% | 2 |
| 2026-08-24 | -0.94 | -0.77 | +60.00% | 5 |
| 2026-08-25 | 0.01 | -0.58 | +35.71% | 14 |
| 2026-08-26 | 0.08 | 0.22 | +50.00% | 16 |
| 2026-08-27 | 0.38 | 0.11 | +54.55% | 11 |
| 2026-08-28 | 0.14 | 0.12 | +56.25% | 16 |
| 2026-08-29 | -0.10 | -0.01 | +40.00% | 10 |
| 2026-08-30 | -0.52 | -0.04 | +23.08% | 13 |
| 2026-08-31 | -0.41 | 0.29 | +40.00% | 10 |
| 2026-09-01 | N/A | N/A | +50.00% | 2 |

## 歷史回測摘要

- 回測日期：2026-09-01
- 近5日 3日相關：-0.06
- 近5日 5日相關：0.23
- 同向比例：+28.57%
- 權重狀態：未調整

- 方向準確度：+28.57%
- 信心排序準確度：-0.06
- 診斷：低相關

調整原因：近 5 日有效樣本 7 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：AI 伺服器與資料中心 相關新聞集中在：台股大跌他們逆勢紅！「這兩檔」擁 AI 護身符逆風暴衝 - 經濟日報；當 AI 開始替公司做決定，出了事究竟算誰的？ - TechNews 科技新報；別再盲目跟風，企業應以打造高回報、低風險的 AI 策略為目標 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +10.34% | +10.63% | 220.78 | 220.78 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2454 聯發科 | 新聞直接提及 | 0.00 | -0.51% | +4.25% | 3,985.00 | 4,310.00 | -7.54% | 不適用 | 60.69 | 64.82 | 48.47B TWD / 12.16% | 2026-08-01 |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 89.51 | 114.68 | -21.95% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 470.72 | 516.10 | -8.79% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -0.41% | +1.26% | 2,420.00 | 2,425.00 | -0.21% | 不適用 | 86.28 | 27.88 | 467.58B TWD / 44.69% | 2026-08-01 |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +29.17% | +0.12% | 507.29 | 513.53 | -1.22% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -1.96% | -11.28% | 370.34 | 446.77 | -17.11% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | -1.35% | -1.35% | 621.00 | 680.00 | -8.68% | 不適用 | 13.92 | 42.26 | 73.78B TWD / 43.15% | 2026-08-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2454：新聞直接提及「聯發科」，共 1 篇新聞命中。 同時符合主題標籤：AI。
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [台股大跌他們逆勢紅！「這兩檔」擁 AI 護身符逆風暴衝 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9Vak83OGpVNWVkQmFBQ0xWWTctNU9yaHNGeTN1QlZ3Ti1icnVjSG9xRGJXR3VZb2hTSWhSUDZrWVJyUVJVZVp0T2ZBbmhPUXlqTURUVEpxbUUyQdIBX0FVX3lxTFB1WmFFMnJGTExvbkYwYnFacWlDa2Z3TUdZdGs2SG9YRGhQam1QVG90VHl4ZUhtbTZ2Q2RualhFbHlsY1A2RzBxQ00zM0prSENKcURMeE4tc3h4RHYtVW9v?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 30 Aug 2026 09:00:00 GMT
- [當 AI 開始替公司做決定，出了事究竟算誰的？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMimgFBVV95cUxOU3FlbFVzU2hEd3VZd3dadFpjeVYtSExLVEQ2S3NXYjVMQ0JBZWRqbk9RdldzMnQ5UEY1Q193b0dIUnVZRTJ3dGlOWWxtc28yX1F1T2ZYaDVjMjhKemVlbGNaQXRodHZKeGh0aUJVbVpaU2d6ODYyem9ESzFQQWdCUEFGSFJmdjd3QmxEVEtnOFJheDdmNHFRdU93?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 01 Sep 2026 00:02:05 GMT
- [別再盲目跟風，企業應以打造高回報、低風險的 AI 策略為目標 - TechNews 科技新報](https://news.google.com/rss/articles/CBMihgFBVV95cUxOQU15UWphSkNWd0d1bmlMejNsRXM1OVI4ckhCVFJGakYxWHV6YU9QTWFCZlVPWHlFaWRPVXpvUlBPbVNJU0F1a1BFeVJTYUlfY3BDdndWRUk0UVRTclM4aHpHV0FjV0JMQ0ZUZ1hIMm5uUFk2ajV1bXBLT1JUWGY3bXpNQTN3dw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 31 Aug 2026 23:28:59 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：整理包／台股5萬點靠他們？ 黃仁勳概念股助漲東風 完整台廠供應鏈名單、潛在受惠股一次看 - 經濟日報；消費級 AI 晶片是否將納入出口管制清單？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +19.94% | +36.49% | 316.85 | 319.70 | -0.89% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | +1.42% | +2.67% | 253.00 | 289.00 | -12.46% | 不適用 | 15.21 | 16.48 | 946.51B TWD / 54.19% | 2026-08-01 |

關聯理由（前 3）：
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [整理包／台股5萬點靠他們？ 黃仁勳概念股助漲東風 完整台廠供應鏈名單、潛在受惠股一次看 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBQUlViSHpPeDVlY29yaHFNNE5NcVlUQnE3ZThTcXRGNHgxYTVPOVVTRDlaTDV6Zml5WEwxVHNSeGFDcnVHUHhRSW15SzNpU0dYVDU3dThWNEVCbkZI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 30 Aug 2026 09:00:00 GMT
- [消費級 AI 晶片是否將納入出口管制清單？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMipwFBVV95cUxQenpDMW00UzhnNGZCUkNMWk5hRmkxeDFNLTViS0czSTNIckFDSmdhX0N5UGN1cnBZYUlNd2VSOTN5b0RobUI4X0ZjaW1iWEZGQW9FTDliYk9BUEJMY1ZRVjlzOGdKYnBTTEhGVGFhWEVnR2ZhUXVERW9kQWYteGM1OE1PUEZTRXBaZ3ZhejZJZDNsVXZ6S3FpV1NWeExicG9xWGNndkRmUQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 31 Aug 2026 20:04:05 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：Why is Micron so cheap? AI rally leader has the third-lowest valuation in the S&P 500 - CNBC；美伊衝突再起！市場憂通膨美股多收跌、費半逆勢上揚 台指期夜盤微漲 - Yahoo股市

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.42 | N/A | N/A | 958.73 | 971.00 | -1.26% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +29.17% | +0.12% | 507.29 | 513.53 | -1.22% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron」，共 1 篇新聞命中。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Why is Micron so cheap? AI rally leader has the third-lowest valuation in the S&P 500 - CNBC](https://news.google.com/rss/articles/CBMivAFBVV95cUxQc09zYlhBaG13TG1zRVFCTW9wX3dnV3dObXJjZEFKM090MkpWY3ZHRThNcjFvTlE2NHAzU3NZcmxzeER5TEZoNTBLXzJkcW5zeW9vREJhajhKX19BNmFOVUd5Mm1hM2lLT2IxM214YjJCZkxncW44ekRJNHJaUF84R3Z1bU11cnoxN19kSjJtQXNYRWc3SGlNOGlZa0JDT0x6c2dMdE5EZEhOT1M1b01BZHFZbGpXZjd5VlVRaQ?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 31 Aug 2026 12:48:07 GMT
- [美伊衝突再起！市場憂通膨美股多收跌、費半逆勢上揚 台指期夜盤微漲 - Yahoo股市](https://news.google.com/rss/articles/CBMiuwNBVV95cUxOUnVpRDR2dkxqc2ZZYmdYMkFleXBPTFhkV1QwcWp3dUhzSlRYTWpQV2J0OTEyb3pqWjExVFBjdG8wQ052M2NUS0RqZFdUeTd6SzR4dTFFWmdRdzhKc3h6YnBaejZRXzRKcEx5bkJLQVlsZl9Jam5vTUg2SjZobURHU2ltSVdES0tpTFlNUmp4MlJGR1E3blBMeVBNcVZtMHA5aG1maU9xX0NBN1JJNHIxNWlXbnZKbzFxMW8yQmZBSjR6WFVSeUxoSHZpY0pMTVBubF9lVzNhNERxb2xvNDFZN3B6NHFYY2gtSkNQVzRqZ1Qza1FZZzl5WGU0b0trbE5wdnJLNGxzXzdCVmpGN2plUHdZeThaSWdEUTRBZ0s1dXJCRm5VY184LUE3UWlmQS1uXzhsMGdZZENMLTB3ZWZQVnhsSUFDTHNXc2NxaHZ4eE9YSVZ6eXc0YnQyZUx1UG1EMGFMZW5JT0FSdDNMRUNmQ0ZDNndSaExrenNGWWY1VVFZVjRrVk1iV2xVLUdJcWpkUTZrcWwtT2ZraUZuU3I3dk9JeGhxLUhpTEV1N05HWVV4X3JWS3RJY0xSRQ?oc=5) - Google News source discovery | Yahoo 奇摩股市 Mon, 31 Aug 2026 22:27:52 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：歐系競爭對手良率出包！「奇鋐小金雞」搶攻QD市占 目標價上探3280元 - FTNN 新聞網；AI data centers need massive amounts of cooling. Jenny Harrington is buying this HVAC stock - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | +8.56% | +19.96% | 3,360.00 | 3,360.00 | 0.00% | 不適用 | 75.13 | 45.65 | 18.59B TWD / 57.39% | 2026-08-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐」，共 1 篇新聞命中。 同時符合主題標籤：thermal。

### 主要來源

- [歐系競爭對手良率出包！「奇鋐小金雞」搶攻QD市占 目標價上探3280元 - FTNN 新聞網](https://news.google.com/rss/articles/CBMiS0FVX3lxTE9zZkx6X0RtNjc1elU5c19BRW5wLUdnOHJuVjdjWEF0Zkh3WEUwWWxlYXF3U1dhay1zRks0ek1YTlczdHVGeEd2Zmd2NA?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 31 Aug 2026 15:30:00 GMT
- [AI data centers need massive amounts of cooling. Jenny Harrington is buying this HVAC stock - CNBC](https://news.google.com/rss/articles/CBMiuwFBVV95cUxPLUxEUko1QmtqNkhzdmFaTzRybUN2Tm55VU81eDQ3THNyTjJBMktyME0wVlFCWlo0SWxNTkZNWEo4RUdPWjA5UVhxT0Z0TnlfOU5nRWgtTFBsZUlZeWRLc0E5Mm9RNzZIU2RkNDByMGwxOHhzX2lvLUl2QTJVQ0xhUElpR3JPNF96V0YzVzNUYnRPVThFZ3E0eFlrZ0ZIU2lCVE5LWFFiczQyTmo2X0lSanhHV2J1bHc0Rk1Z?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 31 Aug 2026 18:34:37 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：SEMICON半導體展友達秀玻璃核心基板技術| 產經 - cna.com.tw；台美簽署人才培育意向書 半導體產學合作 - cna.com.tw；證交所攜手台經院與資策會推出臺灣創新板(tib-創)半導體、汽車工業、通信網路及其他電子產業之洞察報告 - TWSE 臺灣證券交易所

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 89.51 | 114.68 | -21.95% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -0.41% | +1.26% | 2,420.00 | 2,425.00 | -0.21% | 不適用 | 86.28 | 27.88 | 467.58B TWD / 44.69% | 2026-08-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +4.45% | +4.45% | 130.00 | 164.50 | -20.97% | 不適用 | 6.68 | 19.40 | 23.84B TWD / 18.98% | 2026-08-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +10.34% | +10.63% | 220.78 | 220.78 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 470.72 | 516.10 | -8.79% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 958.73 | 971.00 | -1.26% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | +4.49% | +4.93% | 1,566.70 | 2,335.00 | -32.90% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -1.96% | -11.28% | 370.34 | 446.77 | -17.11% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 CPU, server CPU, x86, foundry；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 0 篇新聞出現相關標籤。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 0 篇新聞出現相關標籤。

### 主要來源

- [SEMICON半導體展友達秀玻璃核心基板技術| 產經 - cna.com.tw](https://news.google.com/rss/articles/CBMiXkFVX3lxTFA5YllYRkVVTnUyNTNCNFZaQjYwVnlGTE8zWlZOQm9OdzgwQ0t5eDVNVlpUeGVCMFRMeTZKYXlrdkVTMnJ3WlBNbkdnWWhzVXpBcHVnc0JKMUtRV0IwWmc?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 31 Aug 2026 14:04:00 GMT
- [台美簽署人才培育意向書 半導體產學合作 - cna.com.tw](https://news.google.com/rss/articles/CBMiU0FVX3lxTE1VR2w0aUxYYUp6YmNQaGphTTdBZHJFM1JBX0NkNEUtTGt0Uzhka2NpZFFoTk9KWDhaQjY4WHlUSVBvajRUb3pIalhrdXJBVEFFWUtN?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 31 Aug 2026 09:09:53 GMT
- [證交所攜手台經院與資策會推出臺灣創新板(tib-創)半導體、汽車工業、通信網路及其他電子產業之洞察報告 - TWSE 臺灣證券交易所](https://news.google.com/rss/articles/CBMinwFBVV95cUxPQ05nMmNmakRWM1lCV21PRWx3QXZUamNETHFsZnBacjRYVE9qVl9sTU5nN0hYVEo1eUczbU44blk5UEkyOEZxeFZOekVONDZLLTNNdkxTajh3aFBuVFg0Z1VQWE5PZ2JhOXp2MkZuRHl1NkQ0VzZ2a2JHUm56MXJXb3d6TFRSR1BKbEtSSmpPZkZqbWI5VktjN241UGdKSVU?oc=5) - Google News source discovery | TWSE Mon, 31 Aug 2026 12:56:17 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：MU, INTC, SNDK: Chip Stocks Rally After-Hours On AMD’s Blowout Report - Stocktwits；Why is Micron stock gaining today - Invezz；外資8月回補台股3,700億元 記憶體雙強、貨櫃三雄高掛 欣興榮登買超第二名 驚掀大事件！ - ctee.com.tw

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.48 | N/A | N/A | 958.73 | 971.00 | -1.26% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.41 | +4.49% | +4.93% | 1,566.70 | 2,335.00 | -32.90% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.36 | N/A | N/A | 470.72 | 516.10 | -8.79% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.36 | N/A | N/A | 89.51 | 114.68 | -21.95% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 3037 欣興 | 新聞直接提及 | +0.18 | -13.88% | -7.07% | 1,110.00 | 1,110.00 | 0.00% | 背離 | 15.49 | 66.51 | 16.25B TWD / 43.69% | 2026-08-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +10.34% | +10.63% | 220.78 | 220.78 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron」，共 3 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK」，共 1 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [MU, INTC, SNDK: Chip Stocks Rally After-Hours On AMD’s Blowout Report - Stocktwits](https://news.google.com/rss/articles/CBMiygFBVV95cUxPeVlYaXJjQjNtTkNRQUxQTHhaLUFMbE80Uy1MeDBpV0FPdkg2SHRLdkdfVUpXM1NrNWhZSVZQQ01sa0o4T1hKdzF1clBFRlRWUmMwWGxQTDNVVFBpOVhObUc2MXpBeXBOZ0p3R0w5NGRNOHB4X0ZIXzhlT0NMbmhzc1RtdmJRTWhlRUhKSHpyVnpaU0VGMlJyU2tDcmdkTG1hWVJJbmtTVDREbzFfWDB4bjhuTGswN3lmdkdHQzY1dzFOVU41VGlBNlZn?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 31 Aug 2026 11:39:43 GMT
- [Why is Micron stock gaining today - Invezz](https://news.google.com/rss/articles/CBMieEFVX3lxTE13Y2RlZGN3UFJLT0lyZ0hsSGh1NGp3c1dwd1VTUEdnVVl4Sms5ZVB6QVNlSkl5Z0d6dWExVURGWkJhd0FzMDFHSHJhM1VXZ3NqSFF1UWlubF9FdWUyaHV3SnNnTGRYbUNDRGpTRUY2WTN5ek5uMVZvUg?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 31 Aug 2026 18:44:02 GMT
- [外資8月回補台股3,700億元 記憶體雙強、貨櫃三雄高掛 欣興榮登買超第二名 驚掀大事件！ - ctee.com.tw](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBIdHNxTF9ZbXBZaVAtdDdnSDVyeVdEOUx6TGZHZFNqLXlHaUFRNjVxcm9STkdySERGZU9kTUJpcTV0dWtrR1BCYWVnZTdWZWxMYTRDN29iQy1IYlNxdmY0?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 30 Aug 2026 19:00:00 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股8月底開戶數近1470萬人續創高　月增9.1萬人 - 經濟日報；台指期夜盤幾近平盤　法人：台股可能維持震盪 - 經濟日報；最強亞股 台股8月漲3,008點 MSCI 季度調整效應拉抬指數守住46K - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股8月底開戶數近1470萬人續創高　月增9.1萬人 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxOU09RMk9RWV9ra1Nfa0h1OE9pVWpBWDJYbnpQWjRXZkFwblJaOVY2akF4UkxxeHpzZk5FbHBwR01iMUZDQ0xKV1JiT1p3RDhoVTJHdEtZbkFkTjR0ZGI2T09RQUlKMWt5S1o2SWNzOXBzZFBadVZwRlcxSlNVc0twStIBX0FVX3lxTE53aWVmMHY5cFgzakFqN1NLNU0zNVF2NUUydHBVN0FyRUJkYnBzUVFHM1ZQc29TRHlYY0N0VHdkSnRJYVBndXFvZnZiSVpkTmtLNVNsZWZ1aXM0QWRDMDNn?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 01 Sep 2026 00:45:32 GMT
- [台指期夜盤幾近平盤　法人：台股可能維持震盪 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBQUXVJUGxGZnM3bG9rQ2xrb29GTmhxVVJYX0szU3gwVTJyNTRkZndmUVJJMzFIYlhKRGVYOV9ydFRWZllPaGxkUzdpdGVMSnM5bzJmNkxLaWU1UdIBX0FVX3lxTE9qdkREVjJnREVKM3pnMVB2a3ZBc0NWaEhaQUdTelNVZ29ZeXVrYTlIYmg4Vm4zeFJzenVULU5QbGt5Wm5KcHYxRDIwMHZubGxuaHdVYzVSSFRtUXV6enFj?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 01 Sep 2026 00:30:41 GMT
- [最強亞股 台股8月漲3,008點 MSCI 季度調整效應拉抬指數守住46K - 經濟日報](https://news.google.com/rss/articles/CBMikAFBVV95cUxOYzVNZGFBT3dmZ0s3RGtGY2Iya0RfSTEwMTZMdGRLN0Vpa3RhZ1l4Z3lwb0J0MF9oMnBndS0ydnRBeHdwSlhfVjZVZXlyRWd4V3FvbFBUS2NSUmRnem1ubHByb3FmVGJuTzZlVnVJOWNGLVRyNmFHOGRybkVSX1RHWmk5YkN4T1R6QjdYdUVPTULSAV9BVV95cUxNeXduZE8tbzcyNWxYVTNUWWowejlHS1JvaThhc0poSllwazNGdTZUalZSOEZYSUZnQlhBNUNxZFZPVjAzTmcxS2RQQlJVOURsakx5OTZGd2ZzMGU0WnlKRQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 30 Aug 2026 09:00:00 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：統一證券：台股技術面仍屬正向- 新聞 - MoneyDJ；新聞內容-81F99C81-6630-4956-B005-E244020EEA67台股 - MoneyDJ；《台股盤後》收跌202點、5日線失而復得；本月漲近7% - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [統一證券：台股技術面仍屬正向- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNdmJPcU4tVlgzNjNOV0xvdURxNkRFcEtQTXdmOXkyLXpGcHpDRHVDMzAzV3ktano1LXpucHRfTThaam9OUmY2bmxRQW90SHdEdXN1LW5Tc1dyYWR3STJIaHhKTmdLM3BPNHBVXzl5SXhjSmRZaFBHeDgtdlR5cEdXVXBZSTl6QmktUERRMG94MW9CQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 01 Sep 2026 00:30:00 GMT
- [新聞內容-81F99C81-6630-4956-B005-E244020EEA67台股 - MoneyDJ](https://news.google.com/rss/articles/CBMiigFBVV95cUxNbHBtQ2FNUHdBLVQ5QzYxMGdqdklnV3h2TkoyOVQtaUFZSERIUThqbFRuQ0FpYnBiejhKbGZvTVpobHRreGE5VGRlNjltSzU2dElZMWtXa2NWM1JoMnFxUTBwRFVRZkw1aEhwU015cko5TEk1bUdiWnpKSkFhRzNsREVENm1qN3NRWkE?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 31 Aug 2026 23:50:12 GMT
- [《台股盤後》收跌202點、5日線失而復得；本月漲近7% - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNcG82Y2FOVFk0LVdTd1g3aUE5S3JjbW9DdnhXNWhGeC1HN2dwcHU1anJodGM5ZHdtZUlLRTVpTGZnTzA3eDFCakpsOTZ6YkZuUUtsOHVfWWdKSGduUTVpMTNMQjl2VERrYTcxQmpXXzY0ODE1eEZ3dFhhMXMyMGRDT240dGwzSjZtZ2Z0Z01iYlJ6dw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 31 Aug 2026 08:01:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
