# 每日股市熱門話題分析 - 2026-06-18

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **AI 伺服器與資料中心**｜正向｜熱度 17｜市場確認 36.98｜同向 3/6
2. **新興題材：SpaceX**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0
3. **利率與成長股估值**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
4. **半導體與晶片供應鏈**｜正向｜熱度 4｜市場確認 N/A｜同向 0/0
5. **記憶體與 HBM 供應鏈**｜正向｜熱度 4｜市場確認 0.00｜同向 0/1

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.41（樣本 7）
- 5日相關係數：-0.41（樣本 7）
- 同向比例：3/7

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| AI 伺服器與資料中心 | 36.98 | 3/6 | 2 | +0.66% | +6.12% |
| 新興題材：SpaceX | N/A | 0/0 | 0 | N/A | N/A |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 記憶體與 HBM 供應鏈 | 0.00 | 0/1 | 1 | -1.08% | +19.20% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：B2B383C6A49F | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-06-04 | -0.38 | -0.30 | +85.71% | 7 |
| 2026-06-05 | 0.31 | 0.93 | +50.00% | 6 |
| 2026-06-06 | 0.12 | 0.06 | +45.45% | 11 |
| 2026-06-07 | -0.32 | -0.20 | +45.45% | 11 |
| 2026-06-08 | 0.36 | -0.68 | +60.00% | 5 |
| 2026-06-09 | 0.07 | 0.19 | +25.00% | 8 |
| 2026-06-10 | 0.17 | 0.15 | +53.85% | 13 |
| 2026-06-11 | -0.05 | -0.08 | +14.29% | 7 |
| 2026-06-13 | 0.87 | 0.98 | +100.00% | 4 |
| 2026-06-14 | 0.82 | 0.98 | +100.00% | 3 |
| 2026-06-15 | 0.87 | 0.56 | +42.86% | 7 |
| 2026-06-16 | 0.39 | 0.50 | +76.92% | 13 |
| 2026-06-17 | 0.17 | 0.47 | +62.50% | 8 |
| 2026-06-18 | -0.41 | -0.41 | +42.86% | 7 |

## 歷史回測摘要

- 回測日期：2026-06-18
- 近5日 3日相關：-0.18
- 近5日 5日相關：-0.23
- 同向比例：+68.42%
- 權重狀態：已調整

- 方向準確度：+68.42%
- 信心排序準確度：-0.18
- 診斷：方向與信心皆需修正

調整原因：近 5 日方向與信心排序皆偏弱，降低方向詞與供應鏈推估權重，並加重背離扣分。；關鍵詞×公司後續樣本有效 4 筆，未達 30 筆，不調整樣本權重

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

摘要：AI 伺服器與資料中心 相關新聞集中在：美好證券股東會／AI 浪潮再造新台灣奇蹟！七年布局 淨值成長133% - 經濟日報；AI 發展樂觀 群益投顧調升台股今年高點至53,000點 | 市場焦點 | 證券 - 經濟日報；Is Intel Stock's AI-Fueled Rally Outpacing Its Turnaround? - Trefis

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.62 | N/A | N/A | 121.10 | 121.10 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 新聞直接提及 | +0.28 | -3.52% | -25.22% | 378.91 | 506.69 | -25.22% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.06 | +2.55% | +15.50% | 204.65 | 211.14 | -3.07% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.06 | N/A | N/A | 512.48 | 516.10 | -0.70% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.06 | +3.25% | +5.76% | 2,385.00 | 2,400.00 | -0.62% | 同向 | 74.39 | 32.07 | 416.98B TWD / 30.09% | 2026-06-01 |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -5.88% | +22.95% | 392.90 | 446.77 | -12.06% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.03 | +0.85% | +10.39% | 595.00 | 611.00 | -2.62% | 未明確 | 10.86 | 55.25 | 63.03B TWD / 28.57% | 2026-06-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.04 | +6.70% | +7.34% | 4,460.00 | 4,560.00 | -2.19% | 同向 | 62.91 | 71.08 | 47.43B TWD / 4.99% | 2026-06-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：rally, 成長, 調升。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MSFT：新聞直接提及「微軟」，共 1 篇新聞命中。 同時符合主題標籤：AI, datacenter。 方向判斷命中詞：rally, 成長, 調升。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：rally, 成長, 調升。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [美好證券股東會／AI 浪潮再造新台灣奇蹟！七年布局 淨值成長133% - 經濟日報](https://news.google.com/rss/articles/CBMifEFVX3lxTE1GSWFUQ2lSWDdQSksyYW9hOFJ1bV85bUNQb1dJcUVPaFVraHhtTjJkamE1UUpsaTFkMU05Mk1vLWxyVEpLSWw3WS10OVp2ZzB2SmwzRlh4dmZuUmJzYk1SSHA3a1F5SVB5RnFpRmtKal9nOFpUUURWWDdjMmPSAV9BVV95cUxPZXFyVk1URXY5M3Z1YUNTeEp5dEFWQkdrYjdSS1BHc1d6Y0U3QnZYSGZOeTdEOGNEX19Xb25BR2s3ekdYdTBueTZQVDRpM0M3LUVCMGFQUUdWQmNnTXFIdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 16 Jun 2026 21:00:00 GMT
- [AI 發展樂觀 群益投顧調升台股今年高點至53,000點 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMigwFBVV95cUxNZi1qZkE4d0o0RUpmMzlvbGtHUGp5SEF0dzBOU1EwRkJrM012U3BWWVIyZ0hJUk00S2tDeENtUEpXcGpOVDc5X0VUbFlRdmNKMDhHX0lVYXpGeFczSFB5N09wbVNBZERMQm85b3REMEYzMkRIOU9ack9LaXp0TklBYnFpdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 17 Jun 2026 07:07:34 GMT
- [Is Intel Stock's AI-Fueled Rally Outpacing Its Turnaround? - Trefis](https://news.google.com/rss/articles/CBMixwFBVV95cUxQdklCZElMcTdjbjZXa1Vubmo3Tld1LXNmTXhaRjBZSlZabEphblg1ZEJYTkpKVnFTVnhoclp0Y1MxQWpmRmlzMjByLUdqdmFYQ1JRZHpqOGNvbWI1Q3NpMkNoQWVGQm9JOHBOTlgxaGFfU0IyWElsSmNucDI4TjRLVnQ5aGVsaU11Z3Ryb1VhMG5sV2s2d2x4bWR0UFpydFZiVi1Tc3B2eHM3Y3RweDdNaDhSYTNLV3FXcWlMUGQ2YzlJUEpZRFdz?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 16 Jun 2026 06:14:25 GMT

## 新興題材：SpaceX

摘要：新興題材：SpaceX 相關新聞集中在：SpaceX locks in $60 billion Cursor deal to close gap with rivals in AI coding race - Reuters；Stocks making the biggest moves midday: SpaceX, JPMorgan, UniQure, Intel, Figma, Nano Nuclear & more - CNBC；ProShares Ultra SpaceX (SPCF) Press Releases - Nasdaq

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 121.10 | 121.10 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [SpaceX locks in $60 billion Cursor deal to close gap with rivals in AI coding race - Reuters](https://news.google.com/rss/articles/CBMikAFBVV95cUxPRmxuTnhpZnhfWk9xMXRkVFVNeXBjXzZSRmZRakJpR0RzZnBxOWFfMk40NW1yaXBvTlBQY2FhbG1wY0w4d0wyRFhIOUhjSlF5VW5Fc3pwZ2xRaERESmhmWGp0UE4yT1l2d0M2N2R2UTlLRGFYSkczc2wxcWxCSU1TMzhleHJMR2pKSjcydDRGMHE?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 16 Jun 2026 14:52:06 GMT
- [Stocks making the biggest moves midday: SpaceX, JPMorgan, UniQure, Intel, Figma, Nano Nuclear & more - CNBC](https://news.google.com/rss/articles/CBMimAFBVV95cUxQQ0o4eXNsSHlKd0tlQ0VBakhiNE9hWE1UZDgzSjVXcHJsa0ZwNm4yZXdZY1BYUXJNT0tlaWVtb3QyRXY4Qk5lRnQ5V0VIQ01IeHBUdE1lb0lrZ3dPT3RHdnZVSUtvVlVPVm5xOGJtLXlRZ0RhUHdtVF9jUFBNWmJMYU83WTNOMm54R0VMMEkwNDRpeXA0SkphSg?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 17 Jun 2026 16:37:52 GMT
- [ProShares Ultra SpaceX (SPCF) Press Releases - Nasdaq](https://news.google.com/rss/articles/CBMic0FVX3lxTE4xN2d4Q01YanNfU182RFFkSmFwMGdfVWtXTUdNYkMtS3A5NzRqVVlsQ093aUw3OEdleFBkRmE0cDZaQW9Uem50WmRIT0J3WjZrU0tZTnNNMmpUVUhSZkhUX2l3aWVMdzIzZFhqd0JtbXNkOG8?oc=5) - Google News source discovery | Nasdaq Earnings Tue, 16 Jun 2026 18:16:46 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：Fed 4月、6月聲明比一比：華許掌舵後內容大瘦身 抗通膨立場更鮮明 - news.cnyes.com；瑞典央行維持利率1.75%不變，下調通膨預測 作者 Investing.com - Investing.com 香港 - 股市報價& 財經新聞

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | -3.52% | -25.22% | 378.91 | 506.69 | -25.22% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Fed 4月、6月聲明比一比：華許掌舵後內容大瘦身 抗通膨立場更鮮明 - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTFBpdkgxR1ozTGYtUThuX3h3NnFGOEJIeXdUclFjeFdERVZwSzJ6aXN3X0tNM3locE82Z1c1YThVM196Zko4MlYxNGhFejJseDQ?oc=5) - Google News source discovery | 鉅亨網 Wed, 17 Jun 2026 18:41:25 GMT
- [瑞典央行維持利率1.75%不變，下調通膨預測 作者 Investing.com - Investing.com 香港 - 股市報價& 財經新聞](https://news.google.com/rss/articles/CBMiekFVX3lxTE4yLWxyNFN6UzQ5c3dBWmZjYWpjUmM0UWhWOUFfSVJ2TFVhdFhIXzhENTdVUlBydldTV1laMThJTVBKRXZqT3lqbGs3d3VsTkRZUG1jOWUtZzBpUkxySUJVTFlLSW15SVV2Q2VDV01Zbl84N3JPVVRFX3NB?oc=5) - Google News source discovery | Investing.com Calendar Wed, 17 Jun 2026 07:53:39 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：韓國大舉研發功率半導體經濟部籲持續擴大科研預算| 產經 - 中央社 CNA；美國普渡大學來台交流促半導體學研合作| 生活 - 中央社 CNA；大立光爭取 CPO 訂單 將首度參加半導體展 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 121.10 | 121.10 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +3.25% | +5.76% | 2,385.00 | 2,400.00 | -0.62% | 不適用 | 74.39 | 32.07 | 416.98B TWD / 30.09% | 2026-06-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +4.87% | +18.14% | 140.00 | 144.50 | -3.11% | 不適用 | 4.00 | 35.18 | 22.94B TWD / 17.78% | 2026-06-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +2.55% | +15.50% | 204.65 | 211.14 | -3.07% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 512.48 | 516.10 | -0.70% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 1,043.19 | 1,043.19 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -1.08% | +19.20% | 1,958.80 | 2,107.86 | -7.07% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -5.88% | +22.95% | 392.90 | 446.77 | -12.06% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 CPU, server CPU, x86, foundry；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 0 篇新聞出現相關標籤。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 0 篇新聞出現相關標籤。

### 主要來源

- [韓國大舉研發功率半導體經濟部籲持續擴大科研預算| 產經 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE92NzNxSUY5bHpXcFpWR2hrMDVXeUNnTm5VWWhkd1hHYjBVLXZuamswUVkxSUlJY3pqWVZ1cjFWMlM4WEdZbEJvSzRuZXZiZEstQjR6MGZVNkkzeXZwaUE?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 17 Jun 2026 12:51:00 GMT
- [美國普渡大學來台交流促半導體學研合作| 生活 - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBJYlVDemhOXy10WWtESF9yRk5VNkc4cGNsNzNnbm92dUU5NzhfbmktaHVKai01X3BlN0pha0k0MGhyUVRkUUxsVFhKTi1zVEl1TjU5cGplTVNZRzVNa1hN?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 17 Jun 2026 07:31:00 GMT
- [大立光爭取 CPO 訂單 將首度參加半導體展 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE82QnJab1h2bmhUaEI0ZVJKeUlZS0dIZ1VQWW5Ob2JSeEFTVGxzZVBWZDlGVVBpMlgtSFBGd2l0VU5ablVJTzZBUG9iaVB1OWhVSXVXR3VlLVNYd9IBX0FVX3lxTE5VWGh2ODZtUm5leEtnX0s1RVNSaDY3YWkyUnAtSGJJbGNWaDFERllnVXNpQWVrVm4wOWhLdHFzZFdTMXg1blpLNVV2ZW9qZG9jZHhtVHV4WllHUTBnVmpJ?oc=5) - Google News source discovery | 經濟日報 money Tue, 16 Jun 2026 16:34:59 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits；Sandisk vs. Micron: Which AI Memory Stock Is the Better Buy After Their Monster Runs? - The Motley Fool；Sandisk vs. Micron: Which AI Memory Stock Is the Better Buy After Their Monster Runs? - Yahoo Finance

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.65 | N/A | N/A | 1,043.19 | 1,043.19 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.33 | -1.08% | +19.20% | 1,958.80 | 2,107.86 | -7.07% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.48 | N/A | N/A | 512.48 | 516.10 | -0.70% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.48 | N/A | N/A | 121.10 | 121.10 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +2.55% | +15.50% | 204.65 | 211.14 | -3.07% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron」，共 4 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits](https://news.google.com/rss/articles/CBMi0AFBVV95cUxOWm5KdEIwSXpyY191UEhDa1V6NVpWa01UbmpJeWRIV0ttT080TmpDNEhISW5TWkQwUzBVYzBqSHJPWXRVNVJCampoWWRlYmhKVkhIeHBJLS0wLW5Ua09GQnRORXpFcW5qTEJkcnJGcW55aU5rOFVOLUFMbjRPZEpWT3A2ZllucnM0SU9JNEdrNUwyc3V2WHAtNFk3VHl4R1F6SkZRMFpleEE2Zl9MdW4tSEpMMnFGZ2hQZURWQ3B1WDlPR1BhRjJELVN5ODJWYVR3?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 16 Jun 2026 11:50:36 GMT
- [Sandisk vs. Micron: Which AI Memory Stock Is the Better Buy After Their Monster Runs? - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxOelU0TGtoLVNkdXBiTHloOFYyOGJ4X1RQLVNhamtveXI1aTQ3WmwyRG5XWVNEQ3hMc1UzeURTTnF4TTN2Z1lOSjVUaGM1N3JNRE52cHJtQnNjRTdCSklpOWl6ZzVENHZsUmdhU09TVlBkaDlacjFSeV8zYkdnYU9vU1lBT1Q0ZnNsWWlHUUZPZ0c3em9PWGs5cg?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 17 Jun 2026 00:21:00 GMT
- [Sandisk vs. Micron: Which AI Memory Stock Is the Better Buy After Their Monster Runs? - Yahoo Finance](https://news.google.com/rss/articles/CBMilwFBVV95cUxQTGs4X09Pa1VweWZCdURQTzloc2hwTHg4SF9oTlh6T3pQSjNXdFBOVGNKVUdob1hEd3VNR2x0VU9tOVB0MWltM01Oa1lfeWlHUzlieTc5UzQ1cTlTanhQSG1Ob3lNRnYzZnE2dVlHUzZmbVMzUHVJbXhQN2xELURkNjlRVlNJRi1HeFdQZUQ1UnhJUWxBWGhV?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 16 Jun 2026 23:41:00 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：個股動態報導內容-7F5EED77-A7F5-47BB-A021-198A2B007162 - 5850web.moneydj.com；三大法人反手賣超256億元 台股最後一刻仍逆轉勝！急拉哪些個股？ - 經濟日報；台股擺尾翻紅 金、傳神救援 兩大族群接棒多頭大旗 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-7F5EED77-A7F5-47BB-A021-198A2B007162 - 5850web.moneydj.com](https://news.google.com/rss/articles/CBMikgFBVV95cUxQeEJtYUxscG9vNy00ZHJDT1IzamVGLXBtU1FkMGc4ajd3VGxnZ2UtYVh2SEtWUXNReEM4MmRTTG9Lek5OZUxNX09mcWxuVmlrVm94bklvaTZQNk1QWm1BZUdhVHIzbjhiT1lSb3JjWk5vcmRySG0tbjliR3ZEN2lJY0QzLWwyRHRFR01pdERtd1ZRdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 17 Jun 2026 11:53:15 GMT
- [三大法人反手賣超256億元 台股最後一刻仍逆轉勝！急拉哪些個股？ - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1vZXZWTUFBcUxNcWhiZ1cybUVBTktUSi1KN2VWTVo5SFdSQUlaTFBqa0tWd2wxTWpoV2ZWNjhpUHc4clJnOTR5ZWdVVHgxWDFhOUFRX3JobmtKQdIBX0FVX3lxTE5jeGI0WndORWlRd2dvVWs2ZWRqb283OV9takdWWHFhcnQ4d2NqQll2LVBkYVZFYS1nYm05djczZDR4Nl9HbWk2MzVtMUw2ZUdlVEpCMFBCYjNBbHRUdGI4?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 16 Jun 2026 09:00:00 GMT
- [台股擺尾翻紅 金、傳神救援 兩大族群接棒多頭大旗 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBnM255VTNrWENSREtOd1F0dE9RWEtjOTg0bUs3SnI0UFB6NGpWYmZqVGFZQkR6MGlLVWRwSjFDUmRRYm81cTFpUEt3elh0RmVRbnF5aWpWQ1JWQdIBX0FVX3lxTFA1T3NFb3lTc05VWk91STZYemVzYy1YUktSdEFCcHpTc3l4TEdIN1RRYjRHQmx1MU5BNnU1SkRULWVMOWVqZmVUd1IwNGU0SDNPWEh2dFd0M3NsaVJlbjlz?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 17 Jun 2026 17:05:36 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》開低拉高結算、收漲68點，日K連四紅- 新聞 - MoneyDJ；基金-FundDJ基智網 - MoneyDJ；統一證券：台股技術面有利於多方- 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》開低拉高結算、收漲68點，日K連四紅- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxOd3l3RjdlcFNFY095d2NBa015bE5iQ2F1Y3Y0QkNKYzQyenZxbE9IdnIwSDZ0OHhrWUprTjMwc2tmSWEyQXRSV1VHYjlTWW5aNjNlandWTW4zeFdSbUZlZWVHZGV2d3UwVnlpOTUxV0k4YWQwOGJOSmRfeWxXLXVEXy04cUg0bFB5M2RVVjVCU3EwUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 17 Jun 2026 07:48:00 GMT
- [基金-FundDJ基智網 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxQRS1FYTdpSGhOVXNXQVNVeWlleVJHYlJOdVAzZXN6ZGROc1hwNkdyWGd1M3FydFEwNHNFX0hQMFplUmxkZjNUZV9jS0c0aUxNbXpJWV9aeXNHUm5ZRm03UXBZV2tDbTVqRUFQY3lQUUFZWlpjUG5mZ0s3clNWZ01uNlBoQkdjalhNZUVFY2VhSmU?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 17 Jun 2026 16:34:05 GMT
- [統一證券：台股技術面有利於多方- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNdHZHdk5TODM0d2VlZnhnWUVTMXhaeHE3dDhEcFFlRWx0VHVJZnZnRGR3SjRaZHV4YVA4LVZvYmN1dXVLdGt6Nms3ZTF0ellHcG9HT3F5M3RTM19DLWJrN01NTWJIR3NYQVZ0cV9zazFndDUtVFdmbVJ0RWtBSVBURVFpX01paTc2Y21pb2wzZkQ5Zw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 17 Jun 2026 00:42:00 GMT

## 新興題材：B2B383C6A49F

摘要：新興題材：B2B383C6A49F 相關新聞集中在：個股動態報導內容-3701529C-4723-4B3D-8B16-B2B383C6A49F - 5850web.moneydj.com

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-3701529C-4723-4B3D-8B16-B2B383C6A49F - 5850web.moneydj.com](https://news.google.com/rss/articles/CBMikgFBVV95cUxORl9TdWNYa18xQlk2VDBHN0MyRzhDakM3cGpFUnh0aDJKSnRta3dzdXREM0k5dG56NmRFR0ZpODdWMHpXRUJieDVGbzQ2eVZzRExteWRHV3A2X0RvWkU4Q3dsT255QlB4Qmk5V1NqVm9GQ1c5TVpLTTByT2pUeExvUzFMLWpkdkxNN1VDWGpsQWlMUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 17 Jun 2026 11:53:15 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
