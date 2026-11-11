# 每日股市熱門話題分析 - 2026-11-11

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **綜合市場情緒**｜負向｜熱度 40｜市場確認 100.00｜同向 1/1
2. **利率與成長股估值**｜負向｜熱度 4｜市場確認 100.00｜同向 1/1
3. **AI 伺服器與資料中心**｜中性｜熱度 11｜市場確認 N/A｜同向 0/0
4. **散熱與液冷供應鏈**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0
5. **關稅與供應鏈轉移**｜正向｜熱度 4｜市場確認 32.16｜同向 2/3

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.34（樣本 15）
- 5日相關係數：-0.26（樣本 11）
- 同向比例：7/15

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 綜合市場情緒 | 100.00 | 1/1 | 0 | +49.31% | -43.32% |
| 利率與成長股估值 | 100.00 | 1/1 | 0 | +25.32% | N/A |
| AI 伺服器與資料中心 | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 關稅與供應鏈轉移 | 32.16 | 2/3 | 1 | -4.84% | -7.48% |
| 半導體與晶片供應鏈 | 0.00 | 3/8 | 4 | -12.57% | +1.88% |
| 記憶體與 HBM 供應鏈 | 0.00 | 0/2 | 2 | -19.93% | -17.54% |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-10-28 | -0.30 | 0.47 | +20.00% | 15 |
| 2026-10-29 | -0.05 | 0.04 | +42.86% | 14 |
| 2026-10-30 | -0.00 | -0.05 | +47.62% | 21 |
| 2026-10-31 | 0.50 | -0.68 | +80.00% | 15 |
| 2026-11-01 | 0.47 | -0.40 | +85.71% | 14 |
| 2026-11-02 | -0.15 | -0.06 | +27.78% | 18 |
| 2026-11-03 | -0.03 | 0.08 | +40.91% | 22 |
| 2026-11-04 | -0.21 | 0.35 | +15.79% | 19 |
| 2026-11-05 | 0.13 | -0.53 | +66.67% | 12 |
| 2026-11-06 | -0.18 | 0.77 | +100.00% | 5 |
| 2026-11-08 | -0.21 | 0.03 | +23.08% | 13 |
| 2026-11-09 | -0.56 | -0.62 | +60.00% | 10 |
| 2026-11-10 | -0.32 | 0.24 | +3.45% | 29 |
| 2026-11-11 | 0.34 | -0.26 | +46.67% | 15 |

## 歷史回測摘要

- 回測日期：2026-11-11
- 近5日 3日相關：-0.03
- 近5日 5日相關：-0.30
- 同向比例：+58.82%
- 權重狀態：未調整

- 方向準確度：+58.82%
- 信心排序準確度：-0.03
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

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股開盤漲423.84點 - 經濟日報；Fed 利率不確定性降溫 國泰證券看好美股成長動能、日股改革紅利 | 市場焦點 | 證券 - 經濟日報；台股大漲兩天 外資不回頭 三大法人續賣超148億元 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.42 | -49.31% | +43.32% | 58.13 | 114.68 | -49.31% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [台股開盤漲423.84點 - 經濟日報](https://news.google.com/rss/articles/CBMie0FVX3lxTE1nUVhuZUNyZnhnQ0R5bk1YRFlQWFpQTElaWmlXWVFtb0pjQUVkVVNrQXMxcXF4S0JGZGREc2g3c3Q4V0RKLW9TN19KbElxZW1qQ29tU3JDckFiYWd2Vko5QkpJNU5RUWFzWTFYMVpwZUR2Z3NFQllLMmw1c9IBX0FVX3lxTE5vY0NITTc0TnppQTE2Z2JqMnhvZTl6SXEySW5ETU13azVlRWwxZE4zTlg0M2JDdVAzZGl6TVZIbXpxVHphOXV5RE9ta3dGYzA3V1gzMVl4TGVpWVNHdENB?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 11 Nov 2026 01:28:07 GMT
- [Fed 利率不確定性降溫 國泰證券看好美股成長動能、日股改革紅利 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxPYy0yTVN6Y0hHMmwyT2RyMEgtSURIOVJYMEtETm5ReGFrc2ZFeTFHV2ZsdERhalp5S0hTS3ZvWEM0VGtXa3V3Nm41bUN5eW9IbmJ2ZDhhTmFDQUNuTXRwcmFuVGZWVDlQMnRlb2JkNzVUQVVyMUh2WVpmbmY5ZkZFXw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 11 Nov 2026 01:29:29 GMT
- [台股大漲兩天 外資不回頭 三大法人續賣超148億元 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE16UzJXOFRDY2xaWHJibHlFUy1BQ3dLd3dlUHVSVnJkcEo4MGUwQ3dxUHNfUnIxWVZLMmh1T011ejQxVklKcXpXNnlHTnpTakJzX0F3QllWWG43QdIBX0FVX3lxTFBqT29TSThGQ2REUEM1a2RNOFhKbWJKa0RaWjdwX0JZVUllclRIT2QzaEJ4eUVGM2p5YjczT1ZZSy1uQVhRRGkwMTBKZnczd082aWtXYWFQU1gtTDUxcWNZ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 09 Nov 2026 08:00:00 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：Micron Rises 6% as Bulls Tout Its Bargain Valuation and Buyback Firepower; Seagate and Western Digital Jump 11% - 24/7 Wall St.；EXCLUSIVE: Anthropic eyes $1.4 trillion IPO valuation in test of Wall Street's AI fervor - Reuters；US yields climb, stocks fall as inflation data boosts chances for larger Fed rate hike - Reuters

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | -0.42 | -25.32% | N/A | 725.11 | 971.00 | -25.32% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +18.42% | +8.36% | 533.16 | 533.16 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Micron Rises 6% as Bulls Tout Its Bargain Valuation and Buyback Firepower; Seagate and Western Digital Jump 11% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi5wFBVV95cUxOaEkzTUtOalBCT2FfVlhBYnl3c0VjVDhMNDEwLVpqaktlNlF4V2pWeFlkVGhLT2FnTXFQTVNQaC1XMnBDbkpmQmxUMlVzUmI2QUpLUk5Ra1pBTzctWF8zcV8xWml2TEN1dUZDZzRqUW5XcVhDdldhaVdQNkJ4UFBheF8yeWJFY0MzeGJ5YTkzQXJJM2dCcFVZTTQyUDBRbzBzcXNNTTVkcS01MmdHcXJTcDI5WmtGUWx0eENHQ1d6Nzg1cW5UNnJZUVZHREE1NEt6MXVnT041RnVyU2Z3YnNYNmUyXzZoOUE?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 09 Nov 2026 17:52:00 GMT
- [EXCLUSIVE: Anthropic eyes $1.4 trillion IPO valuation in test of Wall Street's AI fervor - Reuters](https://news.google.com/rss/articles/CBMisAFBVV95cUxNaUtnS210c1pKNVpEZXJ1V1JpdUdyZ0h5OGh2SzVCXzJaVGRwaDZnb0NQZUxFS0ZFWmxwbU53ZlJtdlBkOWplZHdaNkloU0xwV3hvdlpjNnh0R1FISXdMOExfc09JckJqTWxjSWlZSjZpN0RWR1kyRUF6YUlXN0dqSm5XQU5TUmFmbWpFbGlzT3FZRllaMGU4cld0cDlsaFVYY0IzV2ZNYmwxYW0yd1FDaw?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 10 Nov 2026 19:55:19 GMT
- [US yields climb, stocks fall as inflation data boosts chances for larger Fed rate hike - Reuters](https://news.google.com/rss/articles/CBMie0FVX3lxTE9CVDNSVXJpWURQMkF1dUt1amw1WkxILXhVSjZyZkQxdGlBdWZvT0tqclhabXRKZC1xNlRIRmJSdkhINDVsYXlRdk9paVRCa085WWVKRTJFcm9CZWo2VzNaYU5lQ2RXbDdqb3QxdkY4SDFRb2JMVE8yemVJMA?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 10 Nov 2026 02:23:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：AMD vs. Intel: Which Is the Better Artificial Intelligence (AI) Chip Stock to Buy Right Now? - The Motley Fool；Not AMD. Not Intel. This Is the Artificial Intelligence (AI) Chip Stock Nvidia Should Fear Most. - The Motley Fool；別讓 AI 代理「自動化混亂」，企業應先重新檢視流程再導入 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | -49.31% | +43.32% | 58.13 | 114.68 | -49.31% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | -0.17% | N/A | 515.21 | 516.10 | -0.17% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | 0.00 | -26.05% | -15.87% | 168.89 | 228.38 | -26.05% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +2.01% | -0.44% | 2,305.00 | 2,480.00 | -7.06% | 不適用 | 86.28 | 26.49 | 586.89B TWD / 59.71% | 2026-11-01 |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +18.42% | +8.36% | 533.16 | 533.16 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -5.47% | -14.72% | 331.98 | 446.77 | -25.69% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | +5.77% | -1.79% | 604.00 | 703.00 | -14.08% | 不適用 | 17.55 | 34.73 | 88.62B TWD / 47.13% | 2026-11-01 |
| 2454 聯發科 | 產業/供應鏈推估 | 0.00 | +10.69% | +4.22% | 3,820.00 | 4,920.00 | -22.36% | 不適用 | 60.69 | 63.25 | 55.03B TWD / 5.77% | 2026-11-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 2 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AMD vs. Intel: Which Is the Better Artificial Intelligence (AI) Chip Stock to Buy Right Now? - The Motley Fool](https://news.google.com/rss/articles/CBMiygFBVV95cUxNal81S2Q0LVVWX3p5UkFSeTFmRjZCUUNjaVA4eTVqVmFDYUpJT3g1NHE1MDhqUWFRcjJXUzZDa0Vkd2pLUDJqVXRfYVNORWt6SS1rT2FxUmcxSzBYQW1pS2VyUGhPV0toYnNHbWdNME5mUWNJOUtlVzZNTFVsMzZYQmg0RmJucl9sWHBVRVdEVlV2Q3dtclBzX1ZuMTIxNzlkYlB6Qkg3eGxndEFBMDJsQnJNdFdtSG5RSGNQMDJwbld3UEhUU2RlM09R?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 10 Nov 2026 13:52:00 GMT
- [Not AMD. Not Intel. This Is the Artificial Intelligence (AI) Chip Stock Nvidia Should Fear Most. - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxQTl9nX2QzRVlCTVJEUF9iVXpva3ZYZU9Ial9aY3M3TkJvd3dUMnpMS2hMUW5ZZmVLZjlReTFGblJGTUYwRE9LMlc2MGZaZW5ySUdyQ2Z4aWRCR0JXaERqQ1FfY2NvdThjMlV3ekFoMktXTkNXY0RSVnd1cU9MZmhHYXVubFpkZ3JRNHhLb0R0ZmFSRE1xbmxrVA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 09 Nov 2026 12:00:00 GMT
- [別讓 AI 代理「自動化混亂」，企業應先重新檢視流程再導入 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiiAFBVV95cUxNTmRONHctYVJxS0FyOU9UT0JLTWgyS1BLNEZnaFlweFNzeVRQQWswTno2NnpXY19vT2syZWU5QzZqODY5U3VhTGRrdlltRzhsYmJJM1RjbFltc25uRm9leDJpTWFiQW5LNzNWWlZ1b09QTng3UzNfRlZUUXFWSkJoV0wyMmVQbmJr?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 11 Nov 2026 01:31:01 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：AI晶片SO HOT　進補台股散熱3強 - 鏡週刊Mirror Media；SpaceX 太空算力 2028 年上看 5GW！外資點名鴻海、奇鋐、台光電供應鏈 - 鏈新聞 ABMedia；奇鋐看明年ASIC營收超越GPU，水冷擴產逾五成- 新聞 - MoneyDJ

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | +8.77% | -4.94% | 2,860.00 | 3,435.00 | -16.74% | 不適用 | 90.78 | 30.84 | 22.10B TWD / 34.35% | 2026-11-01 |
| 2317 鴻海 | 新聞直接提及 | 0.00 | +2.77% | -1.63% | 236.50 | 289.00 | -18.17% | 不適用 | 15.21 | 15.92 | 1305.32B TWD / 45.73% | 2026-11-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱、奇鋐」，共 3 篇新聞命中。 同時符合主題標籤：thermal。
- 2317：新聞直接提及「鴻海」，共 1 篇新聞命中。

### 主要來源

- [AI晶片SO HOT　進補台股散熱3強 - 鏡週刊Mirror Media](https://news.google.com/rss/articles/CBMiXkFVX3lxTE44MExxRndBaHVGT3BjcUFtRXBLemRsUmtYcVBoSW5yNkRKRGk2YlB1eGtlY2xYaGJ3Qjg2ZHJuMHRFUmp1N0E1MkF6MWx3MGRaQnFLSmZqQUp5ODczS3fSAWJBVV95cUxNUEo5R3pQODRzdkhDQWI2WjU4dzVxOHZDczllV1NQSzR4MzdldTZCR0JvSmJBRms5VGZlTTVraW9hbHVZWnR1c1YzaW9NUmk5eVpSVnJrTlFDbUI1cWhIRTJ3Zw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 09 Nov 2026 19:00:00 GMT
- [SpaceX 太空算力 2028 年上看 5GW！外資點名鴻海、奇鋐、台光電供應鏈 - 鏈新聞 ABMedia](https://news.google.com/rss/articles/CBMiakFVX3lxTE9yUi1TMm0xWmlMZVR6VkE5cml3VzEzZGZzWEJvN1dKcWctQzRURFBmcGZWbkFTeFYzaEVqcHpzODY2MjJPSDhmYllSdjVjVVBHTXhVMVJLRlo1LU91YTEtN1dMcnc3NnhxMlE?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 10 Nov 2026 03:32:14 GMT
- [奇鋐看明年ASIC營收超越GPU，水冷擴產逾五成- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPWm5LY2pYbU9TV04tSm5aVXFXTWNJeFpzSVVZUnB2a0pfeHQ2NXhEbllVZHdEak1aaTBIVnJUYzM3NjF1bV96N081R0JTNW5QWXBFb3VxU1Q2V0MwRUJuTzNLQUJYdTdzVmFTYW54MWhWd1k3RlRNcU5yNHJXQTFQdHF0MWdvRHZzWm1pTHFHdV91QQ?oc=5) - Google News source discovery | MoneyDJ Tue, 10 Nov 2026 07:39:00 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：永豐金證券前10月熱門零股 AI 供應鏈躍交投重心 | 市場焦點 | 證券 - 經濟日報；整理包／黃仁勳概念股笑了！輝達季度財報超預期 完整台廠供應鏈名單、潛在受惠股一次看 - 經濟日報；SpaceX 太空算力 2028 年上看 5GW！外資點名鴻海、奇鋐、台光電供應鏈 - 鏈新聞 ABMedia

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2317 鴻海 | 新聞直接提及 | +0.45 | +2.77% | -1.63% | 237.00 | 289.00 | -17.99% | 同向 | 15.21 | 15.92 | 1305.32B TWD / 45.73% | 2026-11-01 |
| NVDA 輝達 | 新聞直接提及 | +0.21 | -26.05% | -15.87% | 168.89 | 228.38 | -26.05% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3017 奇鋐 | 新聞直接提及 | +0.42 | +8.77% | -4.94% | 2,860.00 | 3,435.00 | -16.74% | 同向 | 90.78 | 30.84 | 22.10B TWD / 34.35% | 2026-11-01 |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +11.68% | +24.98% | 348.51 | 348.51 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 2317：新聞直接提及「鴻海」，共 1 篇新聞命中。 同時符合主題標籤：supply chain, tariff。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 3017：新聞直接提及「奇鋐」，共 1 篇新聞命中。

### 主要來源

- [永豐金證券前10月熱門零股 AI 供應鏈躍交投重心 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMid0FVX3lxTFBQZGk0MjlTR2hZUHJuSGI3MzNLdEZBdF9nckt5eVlGeWdheEdQSTE3VTh3VWQ0QW4xU3B5Q1p4V1JaY3BEQmN6VjhtbVhtYjROc3hvS2RrOU9BRUhHVDRYUENCQ01rc1JBTkp4bDhEOWtEclNXYWQw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 11 Nov 2026 01:20:23 GMT
- [整理包／黃仁勳概念股笑了！輝達季度財報超預期 完整台廠供應鏈名單、潛在受惠股一次看 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBQUlViSHpPeDVlY29yaHFNNE5NcVlUQnE3ZThTcXRGNHgxYTVPOVVTRDlaTDV6Zml5WEwxVHNSeGFDcnVHUHhRSW15SzNpU0dYVDU3dThWNEVCbkZI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 09 Nov 2026 08:00:00 GMT
- [SpaceX 太空算力 2028 年上看 5GW！外資點名鴻海、奇鋐、台光電供應鏈 - 鏈新聞 ABMedia](https://news.google.com/rss/articles/CBMiakFVX3lxTE9yUi1TMm0xWmlMZVR6VkE5cml3VzEzZGZzWEJvN1dKcWctQzRURFBmcGZWbkFTeFYzaEVqcHpzODY2MjJPSDhmYllSdjVjVVBHTXhVMVJLRlo1LU91YTEtN1dMcnc3NnhxMlE?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 10 Nov 2026 03:32:14 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：AMD vs. Intel: Which Is the Better Artificial Intelligence (AI) Chip Stock to Buy Right Now? - The Motley Fool；Not AMD. Not Intel. This Is the Artificial Intelligence (AI) Chip Stock Nvidia Should Fear Most. - The Motley Fool；安世半導體執行長：仍可能與中國業務重新合併| 產經 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.28 | -49.31% | +43.32% | 58.13 | 114.68 | -49.31% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.28 | -26.05% | -15.87% | 168.89 | 228.38 | -26.05% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.42 | -0.17% | N/A | 515.21 | 516.10 | -0.17% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | +0.50 | +2.01% | -0.44% | 2,305.00 | 2,480.00 | -7.06% | 同向 | 86.28 | 26.49 | 586.89B TWD / 59.71% | 2026-11-01 |
| 2454 聯發科 | 新聞直接提及 | +0.49 | +10.69% | +4.22% | 3,820.00 | 4,920.00 | -22.36% | 同向 | 60.69 | 63.25 | 55.03B TWD / 5.77% | 2026-11-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.05 | +2.13% | -2.43% | 99.00 | 164.50 | -39.82% | 同向 | 6.80 | 14.84 | 25.20B TWD / 18.33% | 2026-11-01 |
| MU 美光 | 產業/供應鏈推估 | +0.02 | -25.32% | N/A | 725.11 | 971.00 | -25.32% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.02 | -14.55% | -17.54% | 886.51 | 2,335.00 | -62.03% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AMD vs. Intel: Which Is the Better Artificial Intelligence (AI) Chip Stock to Buy Right Now? - The Motley Fool](https://news.google.com/rss/articles/CBMiygFBVV95cUxNal81S2Q0LVVWX3p5UkFSeTFmRjZCUUNjaVA4eTVqVmFDYUpJT3g1NHE1MDhqUWFRcjJXUzZDa0Vkd2pLUDJqVXRfYVNORWt6SS1rT2FxUmcxSzBYQW1pS2VyUGhPV0toYnNHbWdNME5mUWNJOUtlVzZNTFVsMzZYQmg0RmJucl9sWHBVRVdEVlV2Q3dtclBzX1ZuMTIxNzlkYlB6Qkg3eGxndEFBMDJsQnJNdFdtSG5RSGNQMDJwbld3UEhUU2RlM09R?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 10 Nov 2026 13:52:00 GMT
- [Not AMD. Not Intel. This Is the Artificial Intelligence (AI) Chip Stock Nvidia Should Fear Most. - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxQTl9nX2QzRVlCTVJEUF9iVXpva3ZYZU9Ial9aY3M3TkJvd3dUMnpMS2hMUW5ZZmVLZjlReTFGblJGTUYwRE9LMlc2MGZaZW5ySUdyQ2Z4aWRCR0JXaERqQ1FfY2NvdThjMlV3ekFoMktXTkNXY0RSVnd1cU9MZmhHYXVubFpkZ3JRNHhLb0R0ZmFSRE1xbmxrVA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 09 Nov 2026 12:00:00 GMT
- [安世半導體執行長：仍可能與中國業務重新合併| 產經 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE02UnRGRW41Y3A5NF9XQlJnbVhwWThzRDhYOW1HbWdXVTBMT0JQMGV0RTZQaHNCaGFBa21Gbi1wRHNhYzRsRjBwbm4yUi1YTmlLNWZKcEJ4SzVPdlhzZUE?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 11 Nov 2026 00:24:00 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Micron Rises 6% as Bulls Tout Its Bargain Valuation and Buyback Firepower; Seagate and Western Digital Jump 11% - 24/7 Wall St.；Micron's 26 SCAs: Can Take-or-Pay Deals Boost Earnings Stability? - TradingView；Memory Stocks Show AI-Driven Divergence as Leaders Rally on Low Forward P/Es While Niche Players Lag - ChartMill

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.28 | -25.32% | N/A | 725.11 | 971.00 | -25.32% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.07 | -14.55% | -17.54% | 886.51 | 2,335.00 | -62.03% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -26.05% | -15.87% | 168.89 | 228.38 | -26.05% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、memory」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：boost, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 NAND, SSD, flash memory, memory；其中 2 篇新聞出現相關標籤。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Micron Rises 6% as Bulls Tout Its Bargain Valuation and Buyback Firepower; Seagate and Western Digital Jump 11% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi5wFBVV95cUxOaEkzTUtOalBCT2FfVlhBYnl3c0VjVDhMNDEwLVpqaktlNlF4V2pWeFlkVGhLT2FnTXFQTVNQaC1XMnBDbkpmQmxUMlVzUmI2QUpLUk5Ra1pBTzctWF8zcV8xWml2TEN1dUZDZzRqUW5XcVhDdldhaVdQNkJ4UFBheF8yeWJFY0MzeGJ5YTkzQXJJM2dCcFVZTTQyUDBRbzBzcXNNTTVkcS01MmdHcXJTcDI5WmtGUWx0eENHQ1d6Nzg1cW5UNnJZUVZHREE1NEt6MXVnT041RnVyU2Z3YnNYNmUyXzZoOUE?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 09 Nov 2026 17:52:00 GMT
- [Micron's 26 SCAs: Can Take-or-Pay Deals Boost Earnings Stability? - TradingView](https://news.google.com/rss/articles/CBMiuwFBVV95cUxQeDVHVmlYVG1TenZDQ1BGcUVweC1qSFdxZ25TMFBIR05UUENuZG15Skd0WDVubUZvd2hlTEVIZHN6b2k5MDltNzlhWVR3STdQUHVUYVJmdjhQN1VDSFBFYS1mNjJJN1JjdmhqbnQwRlZTbXg3QUplMmpjbzFia2o1NFlTUHAzMWJCNUNPVC00U1JuVlFXckUzMERjcmNmLXBsRnJ2aFFSODFIc1Nqd3BvTEFiZnltWmlTMzIw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 09 Nov 2026 17:21:32 GMT
- [Memory Stocks Show AI-Driven Divergence as Leaders Rally on Low Forward P/Es While Niche Players Lag - ChartMill](https://news.google.com/rss/articles/CBMi5AFBVV95cUxOTVVwNTlnT1hUOEFITS1iT1JfRDF3YlZBMUFfblRhSHdqTDhRZUgzOVVKZXBTeE5rNzJoQ3Q5b1ZGczVWSUJDay1Wdm1nUkJzMURnSlBmemFUWldPU2VNTE1zWjhDY2JKNEg4dV9TYUJlcjZUeGI1a0JsUkx1NG5mV0tQNmMxaGVRT2ZRWGVpOXhMcUhiU2VwV0pVdUpoWnJuWmNaWTBEbjEzS0lsbjFRR09NVzZoQWRmRXktOTZCbHdSUlVwaE5qNDA0U21sYXpmTVltVGppa19JNDdSSjFKblU3TFk?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 09 Nov 2026 23:06:04 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：國票證券：台股短線仍有震盪可能- 新聞 - MoneyDJ；統一證券：台股技術面仍有利於延續反彈- 新聞 - MoneyDJ；美股指數期貨最新報價 8:37-台股 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [國票證券：台股短線仍有震盪可能- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQdFBLRDA1MG1lYXZhcUFhSXM4SVY1RW9EZ1VPNjVTU0VCc2lHNXZfZEVybGVLWWRvV0ZrTUxDVWxvZ2VwYl9SaTFERWNWLUowZGs1aUJ2a2kwQU0zTDR2d3h2d3VLcmo3dFo5M1N0c21iNXNuR0ZqOHc5d2JJU0F0WmJCRVFWUHVrM1M3ZnRGTi03UQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 11 Nov 2026 00:37:00 GMT
- [統一證券：台股技術面仍有利於延續反彈- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNMFBkS0tGTjNEWkJCWDVVeVN1VWFtTlI4ek5QSi1sQlJ6RlRVSnJFMFNxTGVyOHlValdCcC1rVU1zc2JQQnpCeVg2NjFBZnhRaXU5TWxwQWdCT09VSjZ6clI4VjJTMWJKekIySzZLckhTSHY0UE8wVTV0ZmVNWmRjWVRVamFXNnA1cWhRWDFGcjhmUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 11 Nov 2026 00:37:00 GMT
- [美股指數期貨最新報價 8:37-台股 - MoneyDJ](https://news.google.com/rss/articles/CBMiigFBVV95cUxPa0RFMUdlNVRRM0dFMDdUVGZLdjdOWF9rVmtnVFVOZVZleEJ6ZWRsbU1Ob0o3N0VUdm5HRmg0NXhtNzR1bEdyR0E2WFlqcFh5MFl0bDJleV9DNmNvSUtYRmZqcGNRZ0M4bVJ3ZUZTT0Y3SHNmQlBySHNfRXJXSC1xRDhWbnFIR2pGaFE?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 11 Nov 2026 00:48:49 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
