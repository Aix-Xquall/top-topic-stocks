# 每日股市熱門話題分析 - 2026-07-05

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **新興題材：TradingKey**｜正向｜熱度 1｜市場確認 100.00｜同向 1/1
2. **AI 伺服器與資料中心**｜負向｜熱度 11｜市場確認 48.52｜同向 3/6
3. **半導體與晶片供應鏈**｜中性｜熱度 5｜市場確認 N/A｜同向 0/0
4. **新興題材：CoinDesk**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0
5. **記憶體與 HBM 供應鏈**｜正向｜熱度 7｜市場確認 0.00｜同向 0/2

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.00（樣本 10）
- 5日相關係數：0.24（樣本 10）
- 同向比例：4/10

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 新興題材：TradingKey | 100.00 | 1/1 | 0 | +16.83% | +32.95% |
| AI 伺服器與資料中心 | 48.52 | 3/6 | 1 | +4.51% | -4.29% |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：CoinDesk | N/A | 0/0 | 0 | N/A | N/A |
| 記憶體與 HBM 供應鏈 | 0.00 | 0/2 | 2 | -11.30% | -6.78% |
| 利率與成長股估值 | 0.00 | 0/1 | 1 | -7.72% | +11.71% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 相關性偏弱；應提高同向價格確認權重，降低泛 AI、泛半導體等寬標籤推估權重。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-06-22 | -0.87 | -0.87 | +100.00% | 3 |
| 2026-06-23 | 0.38 | 0.01 | +62.50% | 8 |
| 2026-06-24 | -0.38 | -0.11 | +25.00% | 12 |
| 2026-06-25 | 0.10 | -0.21 | +20.00% | 5 |
| 2026-06-26 | 0.08 | 0.04 | +25.00% | 16 |
| 2026-06-27 | 0.12 | 0.29 | +57.89% | 19 |
| 2026-06-28 | 0.16 | 0.55 | +85.71% | 14 |
| 2026-06-29 | 0.49 | -0.25 | +38.46% | 13 |
| 2026-06-30 | 0.44 | -0.27 | +62.50% | 8 |
| 2026-07-01 | -0.08 | 0.25 | +30.77% | 13 |
| 2026-07-02 | 0.30 | 0.03 | +55.56% | 9 |
| 2026-07-03 | 0.21 | 0.08 | +55.56% | 18 |
| 2026-07-04 | -0.22 | -0.36 | +22.22% | 18 |
| 2026-07-05 | -0.00 | 0.24 | +40.00% | 10 |

## 歷史回測摘要

- 回測日期：2026-07-05
- 近5日 3日相關：0.04
- 近5日 5日相關：0.37
- 同向比例：+27.78%
- 權重狀態：已調整

- 方向準確度：+27.78%
- 信心排序準確度：0.04
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

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Intel Stock Outlook: Can the Apple Foundry Deal Justify INTC’s 250% Rally? - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.48 | N/A | N/A | 120.35 | 120.35 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 新聞直接提及 | +0.48 | +16.83% | +32.95% | 308.63 | 312.06 | -1.10% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AAPL：新聞直接提及「Apple」，共 1 篇新聞命中。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Stock Outlook: Can the Apple Foundry Deal Justify INTC’s 250% Rally? - TradingKey](https://news.google.com/rss/articles/CBMiuAFBVV95cUxOUW1Cai1mU1FWR2h6WDBlMVpaQ3owUEpETXV6dGp5Y0FGdmJxQktrb1ZORUZmSWIyUVo2Q1g1cU1QX0dmZGw3cnFfT1FyVUhkVWtNUkx4dE9rcHFadC1tUXo4X19COVBXZmNkTVFJbm1JUGNERjN6cF9GWnlNREpSN1VTMXFzc01sSmpkNndONkp2MG5Kc3VjTzNZTlZGdk1DSUxvTGlQNUJXVGxpQ2l6SzljWm1VaE5a?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 04 Jul 2026 13:03:52 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：AI 狂潮太猛！台股電子業2026年盈餘預估暴增60% - 經濟日報；AI Chip Stocks Are Beating Big Tech Right Now - Memeburn；拒絕 AI 壟斷，中等強國組「開源聯盟」奪回全球科技主權 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 新聞直接提及 | -0.43 | -0.57% | -22.93% | 390.49 | 506.69 | -22.93% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 產業/供應鏈推估 | -0.08 | N/A | N/A | 120.35 | 120.35 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | -0.06 | -7.72% | +11.71% | 194.83 | 211.14 | -7.72% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | -0.06 | N/A | N/A | 517.82 | 517.82 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.03 | +1.45% | +4.49% | 2,445.00 | 2,445.00 | 0.00% | 背離 | 74.39 | 32.87 | 416.98B TWD / 30.09% | 2026-06-01 |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -19.32% | +16.46% | 360.45 | 446.77 | -19.32% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.03 | +0.29% | +7.91% | 682.00 | 682.00 | 0.00% | 未明確 | 10.86 | 63.32 | 63.03B TWD / 28.57% | 2026-06-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.04 | -1.18% | +8.12% | 4,195.00 | 4,310.00 | -2.67% | 同向 | 62.91 | 66.85 | 47.43B TWD / 4.99% | 2026-06-01 |

關聯理由（前 3）：
- MSFT：新聞直接提及「微軟」，共 1 篇新聞命中。 同時符合主題標籤：AI, datacenter。 方向判斷命中詞：衝擊。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：衝擊。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：衝擊。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AI 狂潮太猛！台股電子業2026年盈餘預估暴增60% - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFA3dFVoeXVXaV9CUHRVZmV5SnJpQmdZbHRGSC1jNWpXQmtUd3p2OXBjZXRZTHJwcFljSks0ZEpVVWdwVnlIakZBQ1pKYVRJQVFZLWs5LUF4d0E0Z9IBX0FVX3lxTE4tN1RMaVdQem0yekZyN2I0Mm1NOG1ZQ1ZpN1NhVWMyZm1pcHI5ZDJ3MFpQRnZ3N2dMV2cxWDg3MmdxWlQxbU02NUlrWmFJMC1OUkE2X19adHcwZ0Z3dGpB?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 04 Jul 2026 05:14:43 GMT
- [AI Chip Stocks Are Beating Big Tech Right Now - Memeburn](https://news.google.com/rss/articles/CBMiakFVX3lxTE85NVkzalR5d1VLYTZpdDFMTVRTR0NHN0J2MlZNRDRReHRUS0FhV3ctVy1hQXB4by1nUFV1a0dqRl93WG8yczVad3BxWTFUR0dpRHV4LUY1Wm80RjAxM09jQTBfRGpNSnp6S2c?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 04 Jul 2026 10:38:56 GMT
- [拒絕 AI 壟斷，中等強國組「開源聯盟」奪回全球科技主權 - TechNews 科技新報](https://news.google.com/rss/articles/CBMirgFBVV95cUxQTUFWYlNRWG90QUJFaEdMNmxHcF9WajI1QkEyanZNTEg3TmJ4TVFoTUVZSFJhNUJLTjNpNVhpdzQ0NU5td2J6VTNad2pLekhJWWxOMmRWYkcyYjkzbDhlN3VTcG1UVHdBb1F5eDZUQmpkdUhUUlZSRHFPRU13WUc0Vzl6YmhvUTFVRHk2VjhMVXNrSVNNZHBoS2tqV1k2dUNLNW5hNUhEM1ZaenFPZmc?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 04 Jul 2026 01:45:43 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：AI Chip Stocks Are Beating Big Tech Right Now - Memeburn；金屬中心半導體檢測實驗室揭牌 攜手SEMI與日立先端強化S廊帶量能 - 中央社 CNA；美國半導體投資熱 德州科學園區吸引台灣企業布局 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 120.35 | 120.35 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +1.45% | +4.49% | 2,445.00 | 2,445.00 | 0.00% | 不適用 | 74.39 | 32.87 | 416.98B TWD / 30.09% | 2026-06-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +3.65% | +3.96% | 170.50 | 170.50 | 0.00% | 不適用 | 4.00 | 42.84 | 22.94B TWD / 17.78% | 2026-06-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -7.72% | +11.71% | 194.83 | 211.14 | -7.72% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 517.82 | 517.82 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 975.56 | 975.56 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -14.89% | -25.27% | 1,745.00 | 2,335.00 | -25.27% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -19.32% | +16.46% | 360.45 | 446.77 | -19.32% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 CPU, server CPU, x86, foundry；其中 1 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 1 篇新聞出現相關標籤。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 1 篇新聞出現相關標籤。

### 主要來源

- [AI Chip Stocks Are Beating Big Tech Right Now - Memeburn](https://news.google.com/rss/articles/CBMiakFVX3lxTE85NVkzalR5d1VLYTZpdDFMTVRTR0NHN0J2MlZNRDRReHRUS0FhV3ctVy1hQXB4by1nUFV1a0dqRl93WG8yczVad3BxWTFUR0dpRHV4LUY1Wm80RjAxM09jQTBfRGpNSnp6S2c?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 04 Jul 2026 10:38:56 GMT
- [金屬中心半導體檢測實驗室揭牌 攜手SEMI與日立先端強化S廊帶量能 - 中央社 CNA](https://news.google.com/rss/articles/CBMiVkFVX3lxTE1IMDFKV0xaLTJ5V0YzTEljTUxRTXFFWTNTWFhubHdEbzZ1Y2RsMTFoVF9EMTN4emVoTTZmZkxVbFdValN2Wk84cE1UcXo4SGo2UXlrbDhR?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 03 Jul 2026 08:11:36 GMT
- [美國半導體投資熱 德州科學園區吸引台灣企業布局 - 中央社 CNA](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1GbmItcXptOHV0NjJFS2RoRjh1U0dVYnRPRlNUd3gyYko3clAwbTU3NU5WZXc4b2VFN3ZWVXJoUWJlLVI1Z1hlbTBSZUw5VUtmUmVKSjFYc3ZQQQ?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 03 Jul 2026 08:28:37 GMT

## 新興題材：CoinDesk

摘要：新興題材：CoinDesk 相關新聞集中在：Bitcoin (BTC) price bounces as memory, semiconductor stock trade starts to cool - CoinDesk

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 975.56 | 975.56 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「memory」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Bitcoin (BTC) price bounces as memory, semiconductor stock trade starts to cool - CoinDesk](https://news.google.com/rss/articles/CBMi2AFBVV95cUxNcnZabWhFQUtYQnhIN2VmS0ZLNTZoRjRZMjZhX0ZTMFhpSGFjNnRpc05Ba0dTbWgyRDh6S05wZlRpM1VDWnIxdmUxbnl6SmdrN1ZFY0RUNUoyVXVXd2hyd01Hc2Z6ZUVrME93VkNMNVNja21HVFhJR3dLRkZaUGZjZjhZMXp0LVNHSG1vZGFxM2ZBNW0ySFYweDc1MkRpWlI5RG9QZ0xqY21OaWRYbDA2OUF0LTQ1eGRFU0xUN3VBVzhaOG10YTNieDVpVXJZUjRlOWVod056N28?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 03 Jul 2026 10:42:05 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Micron vs. Intel: Which AI Stock Is the Better Buy? - The Globe and Mail；Bitcoin (BTC) price bounces as memory, semiconductor stock trade starts to cool - CoinDesk；US Memory Chip Giants Shed $340 Billion in Two Days as 'Big Short' Investor Targets Micron - finance.biggo.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.65 | N/A | N/A | 975.56 | 975.56 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.29 | -14.89% | -25.27% | 1,745.00 | 2,335.00 | -25.27% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.48 | N/A | N/A | 120.35 | 120.35 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.01 | -7.72% | +11.71% | 194.83 | 211.14 | -7.72% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、memory、DRAM」，共 4 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「NAND」，共 1 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Micron vs. Intel: Which AI Stock Is the Better Buy? - The Globe and Mail](https://news.google.com/rss/articles/CBMixgFBVV95cUxQcUVDN1hKRXNCWHdEQTlINE0tN2hCTXRLUE83Y2pKdTFPMnhTSTVVLW8wWTFRZXRLMGVFTmhmMkFWNXh5SzJ6OTlEOVV1d3VseHNkbmcwaUxoelJfYzNzRzlzRUUzVFc0Y0Q2aE9TY29rQllNZDNwdkY1M3dMVGZaSHdGVmJRdnQzei1lOFNhTVB3TnhFaVhjenMyMzFZS3FzLU10blFlMmsxTEM1QWtVM05FWkRkNGk3ZEhKODdoMy0zdkw0NXc?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 04 Jul 2026 01:02:07 GMT
- [Bitcoin (BTC) price bounces as memory, semiconductor stock trade starts to cool - CoinDesk](https://news.google.com/rss/articles/CBMi2AFBVV95cUxNcnZabWhFQUtYQnhIN2VmS0ZLNTZoRjRZMjZhX0ZTMFhpSGFjNnRpc05Ba0dTbWgyRDh6S05wZlRpM1VDWnIxdmUxbnl6SmdrN1ZFY0RUNUoyVXVXd2hyd01Hc2Z6ZUVrME93VkNMNVNja21HVFhJR3dLRkZaUGZjZjhZMXp0LVNHSG1vZGFxM2ZBNW0ySFYweDc1MkRpWlI5RG9QZ0xqY21OaWRYbDA2OUF0LTQ1eGRFU0xUN3VBVzhaOG10YTNieDVpVXJZUjRlOWVod056N28?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 03 Jul 2026 10:42:05 GMT
- [US Memory Chip Giants Shed $340 Billion in Two Days as 'Big Short' Investor Targets Micron - finance.biggo.com](https://news.google.com/rss/articles/CBMidkFVX3lxTE93UE4yU21pTmxaYjhiU2d3S21YdEhwUk80SERKNmFZYUpmX0NaOEN4ZWUwYmkzLXhiTFMwZFRZTV93OUw0ZTlmdm9RMEpCdHlNb01GbU9Nb2xUX1BxRFhMWWxIUUdaVGpxalhJMGRJNy1jSG1yWHc?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 03 Jul 2026 06:15:00 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：野村投信：2026年下半年台股展望 AI驅動基本面續強 留意通膨與地緣政治變數-報告內容-基金 - MoneyDJ；Intel Stock Rockets Overnight On Blowout Q1: Analyst Says ‘We’re Overthinking’ As Valuation Gap With NVDA, AMD Widens - Stocktwits；AMD's Valuation is Stretched at 54.08X P/E: Buy, Sell or Hold the Stock? - TradingView

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AMD 超微 | 新聞直接提及 | +0.56 | N/A | N/A | 517.82 | 517.82 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.24 | -7.72% | +11.71% | 194.83 | 211.14 | -7.72% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.48 | N/A | N/A | 120.35 | 120.35 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | -0.57% | -22.93% | 390.49 | 506.69 | -22.93% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 方向判斷命中詞：rockets。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVDA」，共 1 篇新聞命中。 方向判斷命中詞：rockets。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 方向判斷命中詞：rockets。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [野村投信：2026年下半年台股展望 AI驅動基本面續強 留意通膨與地緣政治變數-報告內容-基金 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxPUnV5dFlBaTVrVUh5ei1odGhlNUE2alJRTUplX3hpS09vYWpQRUo0UjRUVTlyZk9SMjc4NmNlOXpSY2hQNzJNQ2IxbVpyenpwczdJQzFYSnhpMC1jbXZRbmF6eHotamhnckdEZ1FmTjhubW9QWlNpWTJvdTV5emowdjltVnhGMmVtbWgtV1hEckc?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 03 Jul 2026 08:36:00 GMT
- [Intel Stock Rockets Overnight On Blowout Q1: Analyst Says ‘We’re Overthinking’ As Valuation Gap With NVDA, AMD Widens - Stocktwits](https://news.google.com/rss/articles/CBMiiAJBVV95cUxOeXkzdzdWTjJEdE9PWlRvTGdqTnA2MklEYk5ZcE5ZYWVvT29nRVk2Z1p5czRsZGJzY0U3ZWNhTjFmbTdWaXpDa0R2OTh6RzNxZUxUWk9xOS1GbmNuRVdrdmpQdHBjUzFEejVOcFU2di16ak10T1FFVnFNNnZpVnVwU3RkejRveng1ZVF5T1pYdWkxdlB0VkZsQ21pZEJiZU9fVFM5SndpdUpnZVQ1UV9CUnV0RUlwcU9MNGtkbVR6Tng2OVlpY01HU0hXc2lEbzBxZFRER25yajZQcHhrVmdWRmNYUWxEVWVRUDFjcHZhZzVqbm9MVmZGX0ducGZzTmt0SjltejVNSlc?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 03 Jul 2026 04:45:54 GMT
- [AMD's Valuation is Stretched at 54.08X P/E: Buy, Sell or Hold the Stock? - TradingView](https://news.google.com/rss/articles/CBMiwwFBVV95cUxQZ0c4RV9wSng4RG01elFjb1BaNzFUTENxUC1ObUdiWkhwZFIyUjlTSmhRc3hNX0NjSzE3Xzc4a1g1Q1hEdTZUdDdfeEtRZWZEcm5vbFowd0cxRi0yaG1zV1k5OTdBeWVTNUJrYThWRGxOT1dkeG5xM29nWndVVXV3NDdZQ2hjLV92MXRKV3lzdzJNeWpMN3pPcFM4R28yZnN2cWlzRFNhZVZWNXJZd0NuQzdtc3p3X0RmbEo4eVc4S1VhTTA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 03 Jul 2026 16:50:00 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股開盤漲90.6點 - 經濟日報；費半指數下挫　法人：台股面臨46000點保衛戰 - 經濟日報；台股上漲731點創新高　爆新天量1.55兆元 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股開盤漲90.6點 - 經濟日報](https://news.google.com/rss/articles/CBMif0FVX3lxTFA4VFVHZVRXT3ZfcWtrMUFmSDdFNWdNTkpWakY2b0dRUTlPY01Pd21QSUxRd29MUGVtRzlDU04xclV6bk00N0NLS0k2WlVkQXZuSjVhRFJXLUdRdUkxXy1hQ3UwWTVwWG14MWR1ZFFTb1ZHRngwVGtBLVZ3VlhxYWvSAV9BVV95cUxNSmJXa1BKMi1CbEdYbWthbnpTZ1h0Y0VzU0NhdTRSckxNXy1yaE4xZVU2ZGlabi1IcWg4VDBYbW45UGxOTkZPc2ZXU1hZTFdXdFVyVXNTVkZ5cEtOelMxVQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 04 Jul 2026 19:49:15 GMT
- [費半指數下挫　法人：台股面臨46000點保衛戰 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBHYmRQak1lMndHMDN2RUN3Yk9sNks5UDdWV3RiclVGaEdZckRoMG13aXRfTllYdVBVVWllSndzZmotT180NHJWSHNMR3BsVkhYaUFXbVBEeVZTd9IBX0FVX3lxTFBINE1UMXFRX1Brd3hFR0pIaVdMYktqbElvdUxiRmRNdnZFdHRReGNBU2VWMXhwSFlYSjU3R0t2OHNWNmp2ZTVtaFNyWVhoRlJhaVN4TUtkcXFDTE1RbHVN?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 03 Jul 2026 00:30:33 GMT
- [台股上漲731點創新高　爆新天量1.55兆元 - 經濟日報](https://news.google.com/rss/articles/CBMif0FVX3lxTFA4Q3hCWmdfR3BqWV8waFNIbXdka3V2bmROcS1xVGtDWjBXVkMtT21JbWR2ck5jeDFNMEV4V1Y1TjZwNjdCWDhPR1FnYnJubERlWFRPazNCNDcyWGdfMnNSWXlPYThkZ09CZUMzMTV0OVA4SFUwMWZCQVFGSE9sTmPSAV9BVV95cUxNQ2hJMHRxWlNKRks5Ni1kR2NiZ2gyRk5hV1k4c3k2NjJQaEl4SlJNelczeHp5bENQRmZZMVgxV0hsbzN6ZmNDM0lHOEU4Y3pIaGtPMGVnSkxCRVAzem1Gbw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 04 Jul 2026 16:40:15 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：個股動態報導內容-5BFC87A9-0100-44FA-989E-1D077D56C21F - MoneyDJ；個股動態報導內容-0ABA5E24-C285-41E9-A181-3764B51884D8 - MoneyDJ；十檔台股科技ETF七月除息 00927年化配息率最靚 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-5BFC87A9-0100-44FA-989E-1D077D56C21F - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxQbDdfbXgzWHVZNVItOGhVV3NpTzY2ZnZuRHU4OFQtRWlBNThSVVNLNXZGNWY2MldVNUhDbVpFQ1hIeU9ZOGxuS3Y3RjhKeGVrbHN4N2hlR2Vnd0lWQnlERURHZnNfbW94ZXBuQ1dIMzh1eFM3QWM3MEhYdWpkZXRZSS14aXF3QTB6RmVvcE4xTE1yYWti?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 03 Jul 2026 19:06:44 GMT
- [個股動態報導內容-0ABA5E24-C285-41E9-A181-3764B51884D8 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxNdVVLWTJTOW4xQ1N1X3RKVHExNVBvcTFMSmdxSFVMSjMxNW1rYUZZSFluck9CaTdqRUd1WklGbG5UUS1IeDNuRXpHdkM1bXpYTHVTUmo1WFBqcjc1b2VCajI0MkVtWGVfTVdGRDFUSUJDRXFNcEl0UmJGeGc5WWVsTVdDVXUzYTRRNXlERnhHY2loUzVp?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 03 Jul 2026 12:12:08 GMT
- [十檔台股科技ETF七月除息 00927年化配息率最靚 - MoneyDJ](https://news.google.com/rss/articles/CBMiiwFBVV95cUxNdDJLdmhTdkVRX3ZJODcwak1jQjRhNEROWXBQUXY3TTE4Wm81ZS05RmZ0LXZPd2MyVEdveU83bzFyV0FvYndKMUxzejZBYko0eUl6bXhlTVIyVmsxSlNHSFFQNTY5aFR1QkwzQmkzRVQycnY3T3c5WWJhYTRXNlFtZ2UxUU1oVFFQTlRv?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 03 Jul 2026 02:59:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
