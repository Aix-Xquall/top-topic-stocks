# 每日股市熱門話題分析 - 2026-11-08

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **新興題材：MoneyDJ**｜負向｜熱度 11｜市場確認 90.91｜同向 1/1
2. **利率與成長股估值**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
3. **半導體與晶片供應鏈**｜中性｜熱度 4｜市場確認 N/A｜同向 0/0
4. **AI 伺服器與資料中心**｜正向｜熱度 14｜市場確認 0.00｜同向 1/8
5. **關稅與供應鏈轉移**｜正向｜熱度 2｜市場確認 0.00｜同向 0/1

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.21（樣本 13）
- 5日相關係數：0.03（樣本 11）
- 同向比例：3/13

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 新興題材：MoneyDJ | 90.91 | 1/1 | 0 | +6.97% | +9.92% |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 0.00 | 1/8 | 7 | -13.74% | -4.20% |
| 關稅與供應鏈轉移 | 0.00 | 0/1 | 1 | -18.28% | -7.03% |
| 記憶體與 HBM 供應鏈 | 0.00 | 1/3 | 2 | -15.03% | -2.33% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：CoreWeave | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價呈負相關；應檢查正負向詞庫，並降低新聞直接提及但股價背離的權重。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-10-25 | 0.41 | 0.78 | +64.29% | 14 |
| 2026-10-26 | 0.27 | -0.25 | +36.36% | 11 |
| 2026-10-27 | 0.07 | 0.31 | +50.00% | 18 |
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

## 歷史回測摘要

- 回測日期：2026-11-08
- 近5日 3日相關：-0.24
- 近5日 5日相關：0.12
- 同向比例：+64.71%
- 權重狀態：已調整

- 方向準確度：+64.71%
- 信心排序準確度：-0.24
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

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：費半崩逾12%血洗全球！ 台積電跌停、台股早盤暴瀉逾3700點「破4萬大關」 - MoneyDJ；《台股盤後》重挫1873點、年線失而復得；週K連四黑-新聞內容-基金 - MoneyDJ；國安基金第10次進場！ 啟動安定市場任務維護台股穩定- 新聞 - MoneyDJ

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | -0.50 | -6.97% | -9.92% | 2,135.00 | 2,480.00 | -13.91% | 同向 | 86.28 | 24.75 | 511.86B TWD / 54.65% | 2026-10-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 2 篇新聞命中。 方向判斷命中詞：跌停。

### 主要來源

- [費半崩逾12%血洗全球！ 台積電跌停、台股早盤暴瀉逾3700點「破4萬大關」 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPUVFFbkszaVdWbnE4ZUdDZkhfaWtMQjBhWnBjUTY4c1JiV1BoUllMV21yUUhfbzNnWENfamJhMWtsQVp2NGlsQ19Ncm01WEVZNWtRWkVWbjFweU53VnF5ZVRYbndJTVJuSUctSFVPZEltOEdSYVhuS1c4QmlHeFRvZHE2Z3VyV1FfcTAyNFhXZkkxZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 06 Nov 2026 04:10:00 GMT
- [《台股盤後》重挫1873點、年線失而復得；週K連四黑-新聞內容-基金 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxNYjVRb0RTY0xScFM4U3BiUzZHYmZXalFlTGV3X3QxcnRSSGJGUTVSWllwencyU1VyRjlSMnRmcjFGWko3ZXkwUjc1UmNFVlR3emprclE3OHJmRHF4Z0VCSkNIZExVWFZZN01YeEt0YlVZWmNCbWxrVHFTYk4zX2NULTkwUmkwRWZ0X1Q2ZTVtRGU?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 06 Nov 2026 08:22:00 GMT
- [國安基金第10次進場！ 啟動安定市場任務維護台股穩定- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNaE9fV1J2T1haXzNrMk5VRkZqbTNTRS03S29HdW9oeUQ2aEpHQXFXdUF2b2J6LWdoMTUtd1g4QXRHTnpkTWZwQVJteV9vd05reWRicGNnTWFfXzB0Y2VFVXFVQjUyTG9QWnpPYzlJZGdGYzl2TVpDa09QX1FyMElpUDJ3eFFzeFppN0pxTGJWVTFRUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 06 Nov 2026 10:37:00 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：OpenAI gets $11 billion funding at $1.25 trillion valuation, source says - Reuters；美股一周展望／晶片股急彈能追嗎？通膨、CoreWeave 財報考驗反彈成色 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 新聞直接提及 | 0.00 | +17.85% | +7.85% | 530.61 | 530.61 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：新聞直接提及「OpenAI」，共 1 篇新聞命中。 同時符合主題標籤：rate cut。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [OpenAI gets $11 billion funding at $1.25 trillion valuation, source says - Reuters](https://news.google.com/rss/articles/CBMiwgFBVV95cUxNdlpNRm5XVy11c3hLY0NRdjh2T3VmOE1LOWQ2LXlvcFhmZlFJYkQya3N3QWxud2UteUZpWVlCTXVHUXZZTjIwRlVQaUhqOGhyM2lDaDJTSGcxMnE5MzhOZ1NHYlJIc1p5bHRxaVZjZDd4MFY2RWMtRkNlYkhSVkdpMlRBWi1PYUNmZGNydXZnOTZFMTFoOHR0azBpUlU1aHpVdFA4dlhCV0dDNm91VE0xSVg0bXZhcF9jaVAzcXYzaldOdw?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 06 Nov 2026 23:19:47 GMT
- [美股一周展望／晶片股急彈能追嗎？通膨、CoreWeave 財報考驗反彈成色 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTE1hdFF2Ynd2NTY4NjJpeEpUbEl2UHpFcEFObi1SY1dSMlE5TUY1ekV6YzIwdkRzRVIwaW5WdjVxX2pvOEd4TVFHX0lMb1BabVVtZENSdkVBd3hHY0Nl0gFiQVVfeXFMT1ZZYXdZd0lpV1JGdE5VdU5XMWpESlFlQURyaWtGWVZ2dzQ5UTFqTGo5VUZLd1hiaFlGeS1kQlVJanRIbzJJcFRYZ0NxTlhMRVFoWXp1d0tKajJIZ1YzNDJEd2c?oc=5) - Google News source discovery | 經濟日報 money Sat, 07 Nov 2026 05:09:09 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：AMD Jumps 8%, Intel and NVIDIA Climb 5% as Chip Stocks Rebound From Worst Sell-Off Since 2020 - 24/7 Wall St.；印太對話聚焦台印合作 盼半導體搭橋 - 中央社 CNA；Democrat shaping AI policy bought chip stocks despite backing congressional trading ban - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | -50.92% | +38.76% | 56.28 | 114.68 | -50.92% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | 0.00 | -6.97% | -9.92% | 2,135.00 | 2,480.00 | -13.91% | 不適用 | 86.28 | 24.75 | 511.86B TWD / 54.65% | 2026-10-01 |
| NVDA 輝達 | 新聞直接提及 | 0.00 | -18.28% | -7.03% | 186.64 | 228.38 | -18.28% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | -12.99% | N/A | 449.04 | 516.10 | -12.99% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | -10.68% | -17.49% | 92.00 | 164.50 | -44.07% | 不適用 | 6.80 | 13.59 | 25.20B TWD / 18.33% | 2026-11-01 |
| MU 美光 | 產業/供應鏈推估 | 0.00 | -28.94% | N/A | 690.00 | 971.00 | -28.94% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -25.87% | -27.44% | 835.06 | 2,335.00 | -64.24% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -16.37% | -24.56% | 293.69 | 446.77 | -34.26% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip, foundry。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AMD Jumps 8%, Intel and NVIDIA Climb 5% as Chip Stocks Rebound From Worst Sell-Off Since 2020 - 24/7 Wall St.](https://news.google.com/rss/articles/CBMizwFBVV95cUxPa01iWmYtRkh1S3plOXhjRGlOVGg1RzZfUS1yRzA3REs1MTFmb0NYQWJRYmNWSlRVYjlnV1hnMm5IT0d6YXFrUDRhWG94UG81TEJ0OVAwSzJ3TzRha3hESW5hSS1hXzA0cm9VV0ZVV1NoZFdSTGdDc3lTaG1wOEV2YkdUYjFkclpkbk1sQmkzYXBHNHBIUkdXb2NEMkkwcWNya2t5WkdXZWtFN2ZBWDFiZlkwd3VXd0ozcExtZ29kZGQzOWl3YWg1YmM0dkVZSTQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 06 Nov 2026 14:05:00 GMT
- [印太對話聚焦台印合作 盼半導體搭橋 - 中央社 CNA](https://news.google.com/rss/articles/CBMiV0FVX3lxTE9WbkRqNi1RWGh0MHZEcTkwZEoyQzJ6RU5hR3daSFdackFST1BLRnpzcnR4Vk9TanlKWGJOVDlPN1NWY2VUSmlIRzYwb2FwWFVDeGZocXNyMA?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 07 Nov 2026 08:49:53 GMT
- [Democrat shaping AI policy bought chip stocks despite backing congressional trading ban - CNBC](https://news.google.com/rss/articles/CBMiiwFBVV95cUxPTWpGNEh5dXFLVVRVSGk3c3A2LW1NNUV5WEtIMDdwUHNGODVZVXZCWktHNjFMWXpVVS1JZTl4SnVrTHNXMlVJRjdrTkJ2a19MQUNzSEVGWjJTbDQzbVR6bnhQUWk2cGEtT0xNVkcxRlpBWmRtWWVydzU5Z3JMUlZJUnBsdmRxWXJFMzBr?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 07 Nov 2026 13:30:01 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：強攻 AI 與企業級市場，潘健成：群聯擺脫依賴低價庫存邁入 AI 營運收割期 - TechNews 科技新報；AI 聊天機器人也能當學者？實測揭露學術出版防線的新危機 - TechNews 科技新報；工業 AI 邁向規模化導入，AVEVA 以資料基礎串聯工程與營運 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | +0.04 | -50.92% | +38.76% | 56.28 | 114.68 | -50.92% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.03 | -18.28% | -7.03% | 186.64 | 228.38 | -18.28% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.03 | -12.99% | N/A | 449.04 | 516.10 | -12.99% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.03 | -6.97% | -9.92% | 2,135.00 | 2,480.00 | -13.91% | 背離 | 86.28 | 24.75 | 511.86B TWD / 54.65% | 2026-10-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | +17.85% | +7.85% | 530.61 | 530.61 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -16.37% | -24.56% | 293.69 | 446.77 | -34.26% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.02 | -14.45% | -21.11% | 527.00 | 703.00 | -25.04% | 背離 | 13.92 | 38.13 | 88.13B TWD / 45.52% | 2026-10-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.02 | -7.76% | -13.41% | 3,390.00 | 4,920.00 | -31.10% | 背離 | 60.69 | 55.99 | 55.40B TWD / 1.97% | 2026-10-01 |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [強攻 AI 與企業級市場，潘健成：群聯擺脫依賴低價庫存邁入 AI 營運收割期 - TechNews 科技新報](https://news.google.com/rss/articles/CBMi9wFBVV95cUxPWnl1UVVNUV9KSUd0b0VsRDhDdGhrY3BrYlk3ZEQ5T2lwY0ZKMTZwVTRQamVhX1V0VndnUWM2UmtSTzBNMVlJYzhfOV93enA1WTc2Q2h2M1dscU5qc3NzWTd4SHh5TXkxSnpWcDRjNXJnUHRZUVlMbjZ4Z1FyS3BCZkZmd2hmaHlZcElkY09MdEZCNm84anN5WTI0NjhmVl94THl2SFg2ZV8zXzVSOEhhY3U1RDdzQTRUbW4yaFQ0TFRYRkZYWF9DeTBfam96amY4c0ZkUDFSS2U0ZTFFX3JHeXNIb3dFZDBJYzNVR2diSTBjc1lNVk4w?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 06 Nov 2026 12:53:10 GMT
- [AI 聊天機器人也能當學者？實測揭露學術出版防線的新危機 - TechNews 科技新報](https://news.google.com/rss/articles/CBMijAFBVV95cUxOaWtsSmw0dkp0RXlxNUxFanFCRlU2by1TVzBlWUh5X1Noc3ZwSUdCYTE5MHFPYzFPXy15MUZkb25oYjZneFRrM1FUeks3Zlh1WDlQQkV1MDRrTFVzd0tWQms0OUY1QXFUYlV1d2ozV0VCVkRLUGtMMWNNaE1BbW9MZnB5ZXgyTHVod1VxMA?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 08 Nov 2026 00:34:25 GMT
- [工業 AI 邁向規模化導入，AVEVA 以資料基礎串聯工程與營運 - TechNews 科技新報](https://news.google.com/rss/articles/CBMimgFBVV95cUxOeHhqOWx2WXBIOFZPdnRueHdYeDgwSnpKOFV1aXVOZU1nMlVxc0xvX2UzWmxfSlI2Zm1zZkhkdkswUUl2UGY2RlJwemtCLW9RNVhZRERHaEpvOEtUMGtNa19mb1RGMVI1WmFUTEpGcnVSMm5vaFhyNFcwWlBSU09FaDJnRXRqSmFELXViUDF0TGVJbUJRQzV5UnlB?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 07 Nov 2026 07:05:01 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：整理包／黃仁勳概念股笑了！輝達季度財報超預期 完整台廠供應鏈名單、潛在受惠股一次看 - 經濟日報；美資料中心建置添變數 台股伺服器供應鏈耐震度受考驗 | 產經 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.21 | -18.28% | -7.03% | 186.64 | 228.38 | -18.28% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +9.71% | +22.78% | 342.37 | 342.37 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | -8.55% | -8.55% | 224.50 | 289.00 | -22.32% | 不適用 | 15.21 | 14.80 | 1305.32B TWD / 45.73% | 2026-11-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [整理包／黃仁勳概念股笑了！輝達季度財報超預期 完整台廠供應鏈名單、潛在受惠股一次看 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBQUlViSHpPeDVlY29yaHFNNE5NcVlUQnE3ZThTcXRGNHgxYTVPOVVTRDlaTDV6Zml5WEwxVHNSeGFDcnVHUHhRSW15SzNpU0dYVDU3dThWNEVCbkZI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 06 Nov 2026 08:00:00 GMT
- [美資料中心建置添變數 台股伺服器供應鏈耐震度受考驗 | 產經 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE9oTjVSblBlbVVSc0dlQTBPaUQzVGN3a1BIa1JHSlJaMjc5bDdpaXU4WC1Wb3AzLVd2end6N3RhLWNJQTl1bmdxRXQzUjFsOGVjdkpRRWtuSDBSQ0FoRmc?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 07 Nov 2026 04:03:00 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：SanDisk Surges 10%, Micron and Western Digital Jump 8% as Memory and Storage Stocks Rebound From AI Sell-Off - 24/7 Wall St.；Stock-Split Watch: Is Micron (MU) Next? - Yahoo Finance；Stock-Split Watch: Is Micron (MU) Next? - The Motley Fool

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.28 | -28.94% | N/A | 690.00 | 971.00 | -28.94% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.28 | -25.87% | -27.44% | 835.06 | 2,335.00 | -64.24% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 新聞直接提及 | +0.42 | +9.71% | +22.78% | 342.37 | 342.37 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -18.28% | -7.03% | 186.64 | 228.38 | -18.28% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、MU」，共 4 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：surges。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：surges。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- AAPL：新聞直接提及「Apple」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [SanDisk Surges 10%, Micron and Western Digital Jump 8% as Memory and Storage Stocks Rebound From AI Sell-Off - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi4wFBVV95cUxPZS1YbHc4X3E2bTJFVVlNa2MxelRtN28wVVNqR0wzRXBUMXJaQTJTN3E5WTh2M3BHZllVb01pc18tOWhjbGowQlpwVmZCMWtNV3dxdDJrZE41akxCdkpNY1c4aGtpdE5MekswV21LRjV6UjNockY3Qk5hVUQ0NWVFTlB5WVUyOEplZjlCdVlQTUdZTWdJTVhZQ3VmQl92YmtzeGkwQ1JJYks0UzNUdXI4R2ZVNE1aTXV1Mm5jWTMtdjJmVmNwYkp6RGFQbUdTM1UyZW5wbzRaRmc0WEN5eW1vRXpacw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 06 Nov 2026 14:08:00 GMT
- [Stock-Split Watch: Is Micron (MU) Next? - Yahoo Finance](https://news.google.com/rss/articles/CBMilwFBVV95cUxOOGZscl80VGN3X3Uyc0hwU2I4ekROZ1M2NWpnTkhmWURvMk5Ua3BtQ0FtN0RzVmFnUlFjTG84ZW1MbkdxM0pCaXNmUTRYNmg0dmV5YnljWUtkRU1iLXBfdWZ1X3R1TUdBVWxHMXREM3VxLTNkaVczZDBoLXB2VUxxdXg0X3RaZTRRdUlyaTd6T1lyX3g5U2pv?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 06 Nov 2026 15:20:00 GMT
- [Stock-Split Watch: Is Micron (MU) Next? - The Motley Fool](https://news.google.com/rss/articles/CBMihAFBVV95cUxNZEtzX2U2NE9kV2RKT2tybFU1MUpvTDZ6d0dqakExR2dUY0VMMTBvbWxnVlp6WEtZN1Z2ZzJzQmpLRk1ZUzJlT0dpVldNcW5WMTNUNDhKZURCc09uWWVDclIyWktJbmN4NUJ6Rk9ZVU8wdjc5S294NWdxME5UdHRqLXJKM0Y?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 06 Nov 2026 15:00:00 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股 ETF 反向商品漲勢犀利 富邦臺灣加權反1單周勁揚14.2% - 經濟日報；台股跌深！大盤可能已出現波段低點 注意五大落底關鍵訊號 - 經濟日報；台股擂台／挑戰者「統一 e 起發」陳立委 本周青睞保瑞、同亨 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股 ETF 反向商品漲勢犀利 富邦臺灣加權反1單周勁揚14.2% - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9iQnkyelpVaFQ0dnNZV1czcmpONWlDREJYVVlHQmNBcEhlMXctY2I3TFlBQ1V2aEFWUVBBVnVSRktaTXhUX3R3RkR2b09zdE5rWkhFWGRKRVZWUdIBX0FVX3lxTE81TGEwc25sVEhINV9aaGE3SnJ2bUlKUDRaZzB2dnBFYVlYZkNvTGtWZkUwTjhpaFB0N0ZjRWdrS0ktWEFGdnZ0Z0pxZThVMGU1SDJoNHQ2cFVScFBoX1BN?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 07 Nov 2026 17:02:27 GMT
- [台股跌深！大盤可能已出現波段低點 注意五大落底關鍵訊號 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBlbUZIVmxSeGhfUEFoU1BERHY0eTVBVWV1WTJ4bVdGTHhRRUN4ekh2TWoyNlpibVNQUFFLWGE4LVdVWTc5eEV0N21GZG9IR0xkdUJQdlNBTENjUdIBX0FVX3lxTFBmVnJpMmktdDN6dzM0M0hCNlNpWnFPOFROZkk4YXFGNzVET0FsX0tIdklfbGV1dFdLQjdkdHNRblhaM3k4ZFZmTXBXZVRnMXk0RFZDUzh0U3BWbmY1YzJn?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 07 Nov 2026 09:06:48 GMT
- [台股擂台／挑戰者「統一 e 起發」陳立委 本周青睞保瑞、同亨 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBKWngwSUZucVJOWWZ3bVVsR2ktS2h1SlUzV1lYcGRNd2tnX1BldldUUVd0Y3BabFZwbElJWmJnbXVuRjhmV3hBUksxLU1jbE53bFJfMWtOT3VHX2VX?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 07 Nov 2026 17:16:08 GMT

## 新興題材：CoreWeave

摘要：新興題材：CoreWeave 相關新聞集中在：反彈恐是死貓跳？財經名嘴示警AI融資疑慮未除 CoreWeave、Nebius下周財報是關鍵考驗 - 鉅亨網；美股一周展望／晶片股急彈能追嗎？通膨、CoreWeave 財報考驗反彈成色 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [反彈恐是死貓跳？財經名嘴示警AI融資疑慮未除 CoreWeave、Nebius下周財報是關鍵考驗 - 鉅亨網](https://news.google.com/rss/articles/CBMiT0FVX3lxTE10U3BrUWRUTlNOc09yWFJiUm9rZ1V1Tmsycm9kcWhIMWt5eHRBQ3RNcXFKVnR0LV9RSHRkVFYzOTVscXhxRGJKSVhfYktzUGM?oc=5) - Google News source discovery | 鉅亨網 Sat, 07 Nov 2026 11:40:03 GMT
- [美股一周展望／晶片股急彈能追嗎？通膨、CoreWeave 財報考驗反彈成色 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTE1hdFF2Ynd2NTY4NjJpeEpUbEl2UHpFcEFObi1SY1dSMlE5TUY1ekV6YzIwdkRzRVIwaW5WdjVxX2pvOEd4TVFHX0lMb1BabVVtZENSdkVBd3hHY0Nl0gFiQVVfeXFMT1ZZYXdZd0lpV1JGdE5VdU5XMWpESlFlQURyaWtGWVZ2dzQ5UTFqTGo5VUZLd1hiaFlGeS1kQlVJanRIbzJJcFRYZ0NxTlhMRVFoWXp1d0tKajJIZ1YzNDJEd2c?oc=5) - Google News source discovery | 經濟日報 money Sat, 07 Nov 2026 05:09:09 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
