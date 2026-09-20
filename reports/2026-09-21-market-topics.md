# 每日股市熱門話題分析 - 2026-09-21

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **半導體與晶片供應鏈**｜正向｜熱度 6｜市場確認 93.31｜同向 1/1
2. **綜合市場情緒**｜正向｜熱度 30｜市場確認 39.76｜同向 1/2
3. **AI 伺服器與資料中心**｜正向｜熱度 17｜市場確認 64.74｜同向 6/8
4. **關稅與供應鏈轉移**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
5. **新興題材：TradingKey**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.15（樣本 13）
- 5日相關係數：-0.05（樣本 8）
- 同向比例：8/13

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 半導體與晶片供應鏈 | 93.31 | 1/1 | 0 | +7.77% | +3.24% |
| 綜合市場情緒 | 39.76 | 1/2 | 1 | +1.58% | N/A |
| AI 伺服器與資料中心 | 64.74 | 6/8 | 2 | +4.08% | -1.05% |
| 關稅與供應鏈轉移 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：TradingKey | N/A | 0/0 | 0 | N/A | N/A |
| 記憶體與 HBM 供應鏈 | 0.00 | 0/2 | 2 | -10.82% | -9.70% |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：台積9月營收 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價呈負相關；應檢查正負向詞庫，並降低新聞直接提及但股價背離的權重。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-09-08 | -0.07 | 0.18 | +57.89% | 19 |
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

## 歷史回測摘要

- 回測日期：2026-09-21
- 近5日 3日相關：-0.10
- 近5日 5日相關：-0.17
- 同向比例：+37.50%
- 權重狀態：未調整

- 方向準確度：+37.50%
- 信心排序準確度：-0.10
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

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：印度發展半導體尋跨國合作龍頭大廠肯定台灣領先地位| 國際 - cna.com.tw；不當縮小版日月光，台灣「封測小巨人」狂吃 AI 外溢訂單的突圍之道 - TechNews 科技新報；美債殖利率破 5%，半導體股為何展現抗跌韌性？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3711 日月光投控 | 新聞直接提及 | +0.45 | +7.77% | +3.24% | 632.00 | 680.00 | -7.06% | 同向 | 13.92 | 46.16 | 82.25B TWD / 45.66% | 2026-09-01 |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | -5.30% | N/A | 108.60 | 114.68 | -5.30% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +3.14% | +2.07% | 2,460.00 | 2,460.00 | 0.00% | 不適用 | 86.28 | 28.52 | 514.81B TWD / 53.32% | 2026-09-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +12.64% | +11.03% | 156.00 | 164.50 | -5.17% | 不適用 | 6.68 | 23.46 | 25.04B TWD / 30.71% | 2026-09-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +10.72% | +5.27% | 222.27 | 222.27 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | +8.47% | N/A | 559.82 | 559.82 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | +4.61% | N/A | 1,015.80 | 1,015.80 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | +17.04% | +9.70% | 1,791.82 | 2,335.00 | -23.26% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3711：新聞直接提及「日月光」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
- INTC：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 CPU, server CPU, x86, foundry；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 0 篇新聞出現相關標籤。

### 主要來源

- [印度發展半導體尋跨國合作龍頭大廠肯定台灣領先地位| 國際 - cna.com.tw](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5vZUpZWlI1U25XQzEzSjk2RW5lY3l6TmFOZndGdUw1WmFGRDQ1aWJPMnp0Y1N5UExwbDJMVnhrXzhXeHlHYmtmWG1oQ2dTeXJ0dENSeFdHdTlRTkxlbzFz?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 19 Sep 2026 13:06:00 GMT
- [不當縮小版日月光，台灣「封測小巨人」狂吃 AI 外溢訂單的突圍之道 - TechNews 科技新報](https://news.google.com/rss/articles/CBMi3AFBVV95cUxQYlBNaEZMT2prTEFnYkZyZm1EWDF1c3R1QU5Ta2g3Y2p3b2htcFhvSzY4M3RiZFl0MXNjOGVuTWFrMmN5RXJNd1laQjEzODlKVTZfTTVJaUVCaUVMbGt6LXdnMHB0QUJSem1GNVE1a1IyN3I1NkV4WXNsYzlMY1R3MzJCYUdjNmdkVjlzSV9XWXRJQVFnVDJKcW51TUs3djFKWmFNdzEyVUhmUjQ3STlnOFVZOEJ6SE1nU2ZvRGtWdjhaNzlwS1B2SnQ2MFFRelF3YXQ4X3VaNmdSS3VG?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 20 Sep 2026 23:14:36 GMT
- [美債殖利率破 5%，半導體股為何展現抗跌韌性？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMipgFBVV95cUxPY3hrcFQ0LWhSY3B3TGtjVW9WemNHaWlRS1pHTjBpMlVxLWpmcUF1OUhmWGlxZEprRm9mRmRMeXpPM1JNS2hZMHNfaGlDbzVyZ1doQUJ2Z1h2WDc0dlhSZTAtVWw3RFdGLU94Y3RoQkpsWktNLWNMRVRVLVBKUjNiRldsa201ZVNSSWVmUzRESm5NZGhna1J3aVRHSkxBb0s4UFlES0xn?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 20 Sep 2026 06:32:55 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：華南永昌-忠孝 對 健椿(4561)個股 單一券商歷史明細 - justdata.moneydj.com；不確定因素消除 台股量能回溫 法人：後市可積極布局 - 經濟日報；台股7月震盪八千點 熟齡族抄底 | 市場焦點 | 證券 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AMD 超微 | 新聞直接提及 | +0.42 | +8.47% | N/A | 559.82 | 559.82 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.21 | -5.30% | N/A | 108.60 | 114.68 | -5.30% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 方向判斷命中詞：surge, 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。 方向判斷命中詞：surge, 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [華南永昌-忠孝 對 健椿(4561)個股 單一券商歷史明細 - justdata.moneydj.com](https://news.google.com/rss/articles/CBMiggFBVV95cUxPa05TUjAxM1RlNnFEdDY3OVp2c0M5LS14eTR6ellJT3VtT05lWUFiLVFlUENYNFpaQ3Q2QlZQeGRhM1pSVFZwM3FWejN2Y2gxd3BSTFVoTlVVaDBrYU5sdDhKMEJDZzk3RVNmSUtLdi1BUDJmVFVLNEIxYjBveVBvMmFB?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 20 Sep 2026 06:57:21 GMT
- [不確定因素消除 台股量能回溫 法人：後市可積極布局 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBsV0lQM05Xcm1CRENkT0xDd0lObUxYelBJSC1yU0h1WlFEaUdnM1ZiUC1WWDBlR2duZUxzQVJvN3F4TTJoenZBeXdqZl9hc2I4YXhDZ1BWR3dFQdIBX0FVX3lxTE9oaEwyZGFOcENVUXRFbEhNOW9iWk5KVnJtQk15R05PRWtrQmNNYnVsVzVyMUpZVzg4UWxsWWU1RVozYk1kcDVwWDNFT1ZSSVM0RzVmSmRITXhpY2dfT1ZJ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 20 Sep 2026 06:50:32 GMT
- [台股7月震盪八千點 熟齡族抄底 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMie0FVX3lxTE5BRTBlbUwyUUt0ankyeXpBOUVyamFLWDNwQnpuUWRUcUZsY1hORFAySk1NSkhvalcyOVJGTlAtUjAwSTVoTjF3eE5TN1JJS0IzUDhvQklKeS1vWFlsVDI1clpWWHY4dF96Sk11RXVIWVVGcDVkVVJMX1NjZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 20 Sep 2026 02:37:01 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：台股行情先蹲後跳 法人買盤回頭靠攏 AI 股 - 經濟日報；3 AI Infrastructure Stocks Investors Are Watching After Nvidia Policy Signals - simplywall.st；AI 創作版權歸誰？專家警告：平台允許商用不等於免除侵權風險 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.54 | +10.72% | +5.27% | 222.27 | 222.27 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 新聞直接提及 | +0.50 | +7.77% | +3.24% | 632.00 | 680.00 | -7.06% | 同向 | 13.92 | 46.16 | 82.25B TWD / 45.66% | 2026-09-01 |
| INTC 英特爾 | 產業/供應鏈推估 | +0.04 | -5.30% | N/A | 108.60 | 114.68 | -5.30% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.06 | +8.47% | N/A | 559.82 | 559.82 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.06 | +3.14% | +2.07% | 2,460.00 | 2,460.00 | 0.00% | 同向 | 86.28 | 28.52 | 514.81B TWD / 53.32% | 2026-09-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | +9.67% | +0.36% | 493.78 | 507.29 | -2.66% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -8.14% | -19.96% | 357.61 | 446.77 | -19.96% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2454 聯發科 | 產業/供應鏈推估 | +0.04 | +6.32% | +2.73% | 4,710.00 | 4,710.00 | 0.00% | 同向 | 60.69 | 77.79 | 64.18B TWD / 44.08% | 2026-09-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 3711：新聞直接提及「日月光」，共 1 篇新聞命中。 同時符合主題標籤：advanced packaging, AI。
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [台股行情先蹲後跳 法人買盤回頭靠攏 AI 股 - 經濟日報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1qR1ZJSTdGRkVMdmZGUDNBalNoYU5Ld0dkNE9udWxmOTFEeU1FSlRCQWl0Q3hWcm9ETEpTMEF3eWJzWTl6NGdmVnluQ0VuQmlWaE5GVUFTQUVCMGxPNXdZ0gFfQVVfeXFMTWpHVklJN0ZGRUx2ZkZQM0FqU2hhTkt3R2Q0T251bGY5MUR5TUVKVEJBaXRDeFZyb0RMSlMwQXd5YnNZOXo0Z2ZWeW5DRW5CaVZoTkZVQVNBRUIwbE81d1k?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 20 Sep 2026 17:10:40 GMT
- [3 AI Infrastructure Stocks Investors Are Watching After Nvidia Policy Signals - simplywall.st](https://news.google.com/rss/articles/CBMi1AFBVV95cUxQdWZHclZPdmFUTVZScWpxamJxT3Y0TVM1dzAwXzE3WEhPbG9TT3RlMXUwZHpNbFNmYS1ZRVp5YXVfeUxGZlVueDJwaU41eFdtVDRzeGZvMnVpSVpuQTBvS2N0SGw5d0FFQmt3S0dPNVRWTnVxQ2lnLWx3MkpEaWNoWkpQNzh6SGpEclMyVDJnaDlJOC1LNWRBTkthWmQ1UlBtNzlMV0R5WmxyZUsycUhyLUdQdjdzclRkdmRoRUFVVFA3NzZVYy1DbEpLS2JfZ1R6SDZnStIB2gFBVV95cUxNUXN2Uy1tRDA4U1dTUXd5eHBBYi1pY01WMGZTTk5rQ091WXM2S3ZJem5DZktGTWhPN0pKRW5xc3hHNG4tdjJQZEhYUW0tRC02RWRvMGlVMVY2Zl81T2xOZVM4UWlkUWRnd1N0QzRsX0htM0Q1a2VJeS16UXVIdEhCRFJmdk1FV2FlXzhqbTZPeno5QjVDSG9XVlRhSDJ1ODZPYU1zamhiV3dwTTZTaUEzLTlTanVkalg3S3dJSE9WZVRYeG1SUXlFelhPVWlZcjhJbzVvVk5oRDE4dw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 20 Sep 2026 15:43:10 GMT
- [AI 創作版權歸誰？專家警告：平台允許商用不等於免除侵權風險 - TechNews 科技新報](https://news.google.com/rss/articles/CBMicEFVX3lxTFBwZG0zb1RFMFNtRnk2elBLTjB1MDhFSGNJWlQxeF9VNVJrdHBnMjdXcVBVQnFYci1BMWxFNG5wSUtOOEV1LUEteFdQU2JlcmhidnRwdV9TZ1dvd2pPU3ZrQ1dUOUZuNWJvNWxLc2x0dWw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 20 Sep 2026 23:26:15 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：AI 投資需求向供應鏈擴散 柏瑞投信：台股中長線多頭格局未變 - 經濟日報；高雄白埔產業園21日開工打造半導體在地供應鏈| 地方 - cna.com.tw

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +7.71% | +20.54% | 336.13 | 336.13 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | +1.62% | +1.01% | 250.50 | 289.00 | -13.32% | 不適用 | 15.21 | 16.51 | 921.77B TWD / 51.98% | 2026-09-01 |

關聯理由（前 3）：
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [AI 投資需求向供應鏈擴散 柏瑞投信：台股中長線多頭格局未變 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9QRjc3ZW1yQkZHczBJTDNsNW0xcmlBSDNWWTJMdkJweEFmRnY2RkttLUpXcmU1d1VjelpRZHMtV3JLSlgtdThuVWpWeDh0eEg1Y1pYWE8za1dCQdIBX0FVX3lxTE5mMlZnS2RfX1JzRm5KaVBjbENnWDBISHRZQ09pRVQ1TFpQM3FKejB6UFFWUk50eFhtdWZMUEFSSUE5YXdIZ2s1a3lnXzhOZW5TdDB2d2pYTW00c3lLVXdB?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 20 Sep 2026 02:37:19 GMT
- [高雄白埔產業園21日開工打造半導體在地供應鏈| 地方 - cna.com.tw](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBPdmpPWG83cVAtTDJZQ0N2THZLNjBkWUxpanJlMnRxVHpTMG9DS0FKSWRQcV9UemlQNHRkRnZNWTdFcWt5bGg1d01jeHl5TXQ0WEZkTGRleWljVkp5bzhJ?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 20 Sep 2026 06:16:00 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Micron vs. SanDisk: Which Memory Stock Is Better Suited for Long-Term Holding, MU or SNDK? - TradingKey；Micron Technology Inc (MU) Stock Analysis & Forecast - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | +4.61% | N/A | 1,015.80 | 1,015.80 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | +17.04% | +9.70% | 1,791.82 | 2,335.00 | -23.26% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。

### 主要來源

- [Micron vs. SanDisk: Which Memory Stock Is Better Suited for Long-Term Holding, MU or SNDK? - TradingKey](https://news.google.com/rss/articles/CBMi0wFBVV95cUxNVnhOMUFzTkdHc0pxM0w3eUNZdDgwejhRUjVNdVpKYXF1T0xMSHd3c2dYNDBGQkVULXhpTjYtbTBxUnJCX0E0MUhLUlBEUkZxcTVKOGtYZHFSdVlZdWVFNzFta05NeE5oZHNHVEc3RHNpRlZ0aXhRNFJRbkp5TGMwRWEtNEpWMnZ0UFJjNjhIV1ZjXzZ4MEQzYXRYSVBHNVlWRV92WVFUUS0ya29mc1NXT0tIYnBsX2JuWUE4TURLUnI2Tk5vNkV2eHZoZDZ2ZnpGVEdF?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 20 Sep 2026 09:26:01 GMT
- [Micron Technology Inc (MU) Stock Analysis & Forecast - TradingKey](https://news.google.com/rss/articles/CBMiY0FVX3lxTFB2cjlJNEFoZnN6al9fVWlOSktTV2tWRzJ1c0c2SklreGhaeHF5VlZlSjNNRE1SaXlnaUVsQ1FaMXFtZUlvM19kUzhHdURNU1VkNmNhLTNPSDNtXzBpSHNZS0xkNA?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 20 Sep 2026 17:31:27 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Micron vs. SanDisk: Which Memory Stock Is Better Suited for Long-Term Holding, MU or SNDK? - TradingKey；Citi Forecasts Widening Memory Chip Shortages Through 2031 as AI Demand Expands - Yahoo Finance；Citi Projects DRAM and NAND Supply Deficits as AI Memory Demand Accelerates - Yahoo Finance UK

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | -0.28 | +4.61% | N/A | 1,015.80 | 1,015.80 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.28 | +17.04% | +9.70% | 1,791.82 | 2,335.00 | -23.26% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +10.72% | +5.27% | 222.27 | 222.27 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、memory、DRAM」，共 4 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK、NAND」，共 2 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Micron vs. SanDisk: Which Memory Stock Is Better Suited for Long-Term Holding, MU or SNDK? - TradingKey](https://news.google.com/rss/articles/CBMi0wFBVV95cUxNVnhOMUFzTkdHc0pxM0w3eUNZdDgwejhRUjVNdVpKYXF1T0xMSHd3c2dYNDBGQkVULXhpTjYtbTBxUnJCX0E0MUhLUlBEUkZxcTVKOGtYZHFSdVlZdWVFNzFta05NeE5oZHNHVEc3RHNpRlZ0aXhRNFJRbkp5TGMwRWEtNEpWMnZ0UFJjNjhIV1ZjXzZ4MEQzYXRYSVBHNVlWRV92WVFUUS0ya29mc1NXT0tIYnBsX2JuWUE4TURLUnI2Tk5vNkV2eHZoZDZ2ZnpGVEdF?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 20 Sep 2026 09:26:01 GMT
- [Citi Forecasts Widening Memory Chip Shortages Through 2031 as AI Demand Expands - Yahoo Finance](https://news.google.com/rss/articles/CBMioAFBVV95cUxQVC1sTElMZ3liZGNHNUJnNUhhUEZ2di16cUZvVDNDY2E1ZXFkd1FFMFlvX1NiQ3RkbmJJSkd3aVkwRlZOZE1ibjF4QWlST3BSQ3F1VVpacE1KQUhIZGVKTnFfekpYazZOclFnVU5jTXBtTkwzNDV6azlwR2kyQmlDSnk4c3l2VU95dFM5QnBTTmtVRlNCTTB1ZTB2amdoWUVP?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 19 Sep 2026 14:54:45 GMT
- [Citi Projects DRAM and NAND Supply Deficits as AI Memory Demand Accelerates - Yahoo Finance UK](https://news.google.com/rss/articles/CBMihgFBVV95cUxQWDJNOEIzRERkdXhiVWhnVmR0UTZ4RFVnZEZERWVkQVZRNDd4WDhjU3k0YWlCNS1CR0hma2VDWnFZWTBkdmxZajRIZjVmLW9nQ3otLU0wc1cyNzZOWkFhTGFkeE5WR2E2T1pQbGcyXzBuZE1VRUpPX29rZ09FQW5BS0I4Mk8xUQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 19 Sep 2026 14:54:18 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：個股動態報導內容-7BA8C88D-7431-42A0-90DA-A3765471FB2B - MoneyDJ；個股動態報導內容-744AECD4-A915-4D6C-8611-DE2703911708 - MoneyDJ；個股動態報導內容-22198E30-71FB-4E2E-B5C9-625DE2A5A746 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-7BA8C88D-7431-42A0-90DA-A3765471FB2B - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxNVVZCN3pQbDlscFZMcy1ZOWNjdlBQRUo2Ty1wUlRkZHJUajV6WjFoeGdmeU5TSl9YSGIzRUtiWXdfNmFuXzlyZlB3R1NyNGJwM1ZXUmZ5Wl9ORnNEOWlfRlBCckd2ZnlKZzVSU1JFZExIemN3SEtNdWNnRExjRG42b25pSXZVcWt0UUdlcHkxYS0ySlJr?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 20 Sep 2026 15:42:39 GMT
- [個股動態報導內容-744AECD4-A915-4D6C-8611-DE2703911708 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxNRVEyc0N2MWZZcEdNdDZyQXNoSzFSazNYYXJrNGFkUTVwaWRRN24xMlExdUpnaTZ3WVdiRkx2M3dvMDFsREUzelc4ZkQ0bzF0TENvbEJGd3IzZzJzSTBiMUFmcFp4T2ZBSmJpYUNUN0ZJdUU2WHBVZ21qemhJdWxZT0ZfODM1OEQxN2hCcUZCTUpJZzNI?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 20 Sep 2026 15:22:26 GMT
- [個股動態報導內容-22198E30-71FB-4E2E-B5C9-625DE2A5A746 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxNRHdaVWRjR0lmUTdwdXZFWFhQZlZPX0x5MDM4dFBuV2dXVFlQS0NCWlVOQmtGN2pPakNKbWRhcGhOSVR4VWJQS1A1Ry0xSEdHdlQyT0pxS0J0Yk5sSTQ1U2ttYjY4VjBpYkkwLXhsam1jUHc5d0JtRkRtS2s1aVpiYWtqekFINko3TVRROEt0Z0paWjho?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 20 Sep 2026 12:16:43 GMT

## 新興題材：台積9月營收

摘要：新興題材：台積9月營收 相關新聞集中在：台股基本面行情將接棒、台積9月營收上看5,200億 大盤節後挑戰48K - 經濟日報；台股基本面行情將接棒、台積9月營收上看5,200億 大盤節後挑戰48K - Yahoo股市

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股基本面行情將接棒、台積9月營收上看5,200億 大盤節後挑戰48K - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFA3MVVTS2Z0c21kbVY4MzFiT0NSVWViVFlaSm54Wk54ZS0tQnQ2eHUtQzlnS0Z0V0NqVzU5WlJ0U1RUbEdxckktUURLWU5ObnFGZkhUMUFFTWxWd9IBX0FVX3lxTE5CNHRPQmRIZGpRZW5OTm5VZjdHeXFQWGJwVlhhMFhmdURqVTNwd2VGNHFFQ185VWVmWWlVbnp4Zk5uVG1vQ1N1NFFDMFFCclp2VkQ0SGFFcnpxdUxFaEpn?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 20 Sep 2026 17:21:41 GMT
- [台股基本面行情將接棒、台積9月營收上看5,200億 大盤節後挑戰48K - Yahoo股市](https://news.google.com/rss/articles/CBMiigNBVV95cUxNZW1xMTNlSk1GWC1DNVI0MWpnb2k4UHQzMWIyZndNX1pNeVh2UVNndmdkQy1QR3JMUDJ3SmVLY1VoeEdNbW1PRzFLdWs3LWh6XzJ1UEI1MnNQVElrTkVCLW1raU42eGo1d2ZzOU1uZXdwMzV2NzNwYzNwMFljUVc5Ny1MY2Vlc1lGeFAxNWtrWEhzbmxDQlJQaDcyd0dNd0tVdzV0Z1J2VkpualZ2Nmx1TjhBODQ1VEZqLUZfYlo1TEdocGNmV0U3dmZCTG1acHd4MGdELXJEcjIzOVpJRkZFLS1EUnE1WFVYZkpVYnloLVJJMmpPZkk0Qk1vc0lqUGVRVmJqOE9fU2U0VGhCVnhnVHZqVXRfNFJMQTBreDRIcFJFUXdxMzVWVEl3OWZyNkRoNk8yRDktYlo0WmZqQ2h4cU93U2p3QTNWTU5MVFJWS0Z1eXJOc2NXZWhyVTRpTjhyWVNHQ3QtVEpLNUl0V1pVcDk5eGZnN1dENlJrd2xzRDM2ZnBjcllIUENR?oc=5) - Google News source discovery | Yahoo 奇摩股市 Sun, 20 Sep 2026 22:48:58 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
