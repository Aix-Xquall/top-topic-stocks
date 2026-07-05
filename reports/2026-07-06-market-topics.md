# 每日股市熱門話題分析 - 2026-07-06

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **新興題材：MoneyDJ**｜中性｜熱度 6｜市場確認 N/A｜同向 0/0
2. **AI 伺服器與資料中心**｜中性｜熱度 14｜市場確認 N/A｜同向 0/0
3. **半導體與晶片供應鏈**｜中性｜熱度 6｜市場確認 N/A｜同向 0/0
4. **綜合市場情緒**｜正向｜熱度 24｜市場確認 0.00｜同向 0/1
5. **記憶體與 HBM 供應鏈**｜正向｜熱度 3｜市場確認 0.00｜同向 0/1

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：N/A（樣本 2）
- 5日相關係數：N/A（樣本 2）
- 同向比例：0/2

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | 0.00 | 0/1 | 1 | -7.72% | +11.71% |
| 記憶體與 HBM 供應鏈 | 0.00 | 0/1 | 1 | -14.89% | -25.27% |
| 新興題材：台股新一季法說 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：台股超級法說 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：半導體法說 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
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
| 2026-07-06 | N/A | N/A | 0.00% | 2 |

## 歷史回測摘要

- 回測日期：2026-07-06
- 近5日 3日相關：0.19
- 近5日 5日相關：0.44
- 同向比例：+31.58%
- 權重狀態：已調整

- 方向準確度：+31.58%
- 信心排序準確度：0.19
- 診斷：弱正相關

調整原因：近 5 日方向與信心排序皆偏弱，降低方向詞與供應鏈推估權重，並加重背離扣分。；關鍵詞×公司後續樣本有效 0 筆，未達 30 筆，不調整樣本權重

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

摘要：新興題材：MoneyDJ 相關新聞集中在：法人專欄分析內容-台股 - MoneyDJ；理財行事曆 - MoneyDJ；愛普* 115年6月營收8.11億、年增59.48% - MoneyDJ

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2317 鴻海 | 新聞直接提及 | 0.00 | -4.18% | -3.22% | 240.50 | 289.00 | -16.78% | 不適用 | 14.13 | 17.08 | 821.76B TWD / 52.11% | 2026-07-01 |

關聯理由（前 3）：
- 2317：新聞直接提及「鴻海」，共 1 篇新聞命中。

### 主要來源

- [法人專欄分析內容-台股 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxPc09JVnhwZFdzTFE0ekZYLTEtSGRCX3g1S2swMHduaXJFTHY0bU4zN1hic1E2ZGRndW5DMjJVaURBS3BKbWhOYk5HbnhZby1pNzJiUUNOMUFDZ3V6UmROM1pydkhNUGZCYUpiYjlRbHhMb0s4UE5pWmt3Y2xyZnYwcUtEY3FweDZuNUFRN2dORkI?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 05 Jul 2026 16:16:04 GMT
- [理財行事曆 - MoneyDJ](https://news.google.com/rss/articles/CBMid0FVX3lxTE9JQzUzRkJYcnBRRzhqNjhkR1h3S1hjWnFhVlYxazZyN3lJcDJ5eU9wMjlLamJ0a21MRzAxMDlpcDR3YVBOdzlvcUNteURsOEhyTTUtTFVDa3RsTVptVHdYVXhxOTRZcG1MWnNuM21EVTgyVVZFT2pn?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 04 Jul 2026 07:04:39 GMT
- [愛普* 115年6月營收8.11億、年增59.48% - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNM25DX3g5QWJSQW55VnBtVmV0OXo2ZFNmWHdKRWZhTUZqOXZlVjJqX1hIc1VTcVpBQjFMYlhySklLckVDMHV4elYzcXhzaHgtckNjNXo4d3IyT1FVOXhNcldZVnZGMkhzeHJ5X1pLZmo5YlVCM0RTY1FBRnpOZlRkRjZVbmIxTlktV3R1OFBjdUlUQQ?oc=5) - Google News source discovery | MoneyDJ Sun, 05 Jul 2026 13:29:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：AI 狂潮太猛！台股電子業2026年盈餘預估暴增60% - 經濟日報；台股科技型 ETF 拉風 00892周漲6.9%稱冠 反映 AI 產業持續磁吸資金 - 經濟日報；AMD vs Palantir: Which AI Giant Is a Better Buy? - 24/7 Wall St.

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | 0.00 | -7.72% | +11.71% | 194.83 | 211.14 | -7.72% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 120.35 | 120.35 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | N/A | N/A | 517.82 | 517.82 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +1.45% | +4.49% | 2,445.00 | 2,445.00 | 0.00% | 不適用 | 74.39 | 32.87 | 416.98B TWD / 30.09% | 2026-06-01 |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | -0.57% | -22.93% | 390.49 | 506.69 | -22.93% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -19.32% | +16.46% | 360.45 | 446.77 | -19.32% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | +0.29% | +7.91% | 682.00 | 682.00 | 0.00% | 不適用 | 10.86 | 63.32 | 63.03B TWD / 28.57% | 2026-06-01 |
| 2454 聯發科 | 產業/供應鏈推估 | 0.00 | -1.18% | +8.12% | 4,195.00 | 4,310.00 | -2.67% | 不適用 | 62.91 | 66.85 | 47.43B TWD / 4.99% | 2026-06-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA、NVDA」，共 2 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel、INTC」，共 2 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AI 狂潮太猛！台股電子業2026年盈餘預估暴增60% - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFA3dFVoeXVXaV9CUHRVZmV5SnJpQmdZbHRGSC1jNWpXQmtUd3p2OXBjZXRZTHJwcFljSks0ZEpVVWdwVnlIakZBQ1pKYVRJQVFZLWs5LUF4d0E0Z9IBX0FVX3lxTE4tN1RMaVdQem0yekZyN2I0Mm1NOG1ZQ1ZpN1NhVWMyZm1pcHI5ZDJ3MFpQRnZ3N2dMV2cxWDg3MmdxWlQxbU02NUlrWmFJMC1OUkE2X19adHcwZ0Z3dGpB?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 04 Jul 2026 05:14:43 GMT
- [台股科技型 ETF 拉風 00892周漲6.9%稱冠 反映 AI 產業持續磁吸資金 - 經濟日報](https://news.google.com/rss/articles/CBMid0FVX3lxTE0xLV9WQlRlMUFUMG5MNUhTQXZpSExCSXRucVk1TF9IU3NFemQ5aFQ2bFlNMEF1QXNtZkdXbzhBblpaalRLb2pEdlhrYUVJZWp5MXcwd2dSUG9aNWtlRC04RkR4OUlDbTk3NGczNnAwNlFkVUxQRzdn0gFfQVVfeXFMTWhvXzBSaTd1b3NETXZqMVVZTG5ySHdxV29wczI1RWhoaFctTGR2VE95WFZ1MldCY1VSLXpCS3hkMS1uZzNLWUhRUXFmV045eEtQbHdiNW45VmY4SVZzakE?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 04 Jul 2026 09:00:00 GMT
- [AMD vs Palantir: Which AI Giant Is a Better Buy? - 24/7 Wall St.](https://news.google.com/rss/articles/CBMilAFBVV95cUxQTzNNSkJJUVZiWnNod1MwcnhucHV5REhnNHh3cEYxMjlLNlFMeWQ1dWVVcmRBZVV6MnRwWjFXV3R0V2RpQVRVbEtPbXlZWXNpNmxLaEFPWEpZV2c1MklSM2VhX0Rla2VEWjZkdE5XNjYxanFuSnRzYnNRcWJzd1hBNVJhZXRYYll2RzJIWWZLa3BkTHp0?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 05 Jul 2026 17:50:21 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：This AI Chip Stock Just Signed Massive Deals With 3 Hyperscalers, and It Still Looks Like a Great Buy Right Now (Hint: Not Nvidia or Intel) - The Globe and Mail；AI Semiconductor Stocks July 2026: NVDA, AMD, INTC Investment Analysis - Intellectia AI；104職缺7月達123萬個AI半導體綠領徵才同步升溫| 產經 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 120.35 | 120.35 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | 0.00 | -7.72% | +11.71% | 194.83 | 211.14 | -7.72% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | N/A | N/A | 517.82 | 517.82 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +1.45% | +4.49% | 2,445.00 | 2,445.00 | 0.00% | 不適用 | 74.39 | 32.87 | 416.98B TWD / 30.09% | 2026-06-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +3.65% | +3.96% | 170.50 | 170.50 | 0.00% | 不適用 | 4.00 | 42.84 | 22.94B TWD / 17.78% | 2026-06-01 |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 975.56 | 975.56 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -14.89% | -25.27% | 1,745.00 | 2,335.00 | -25.27% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -19.32% | +16.46% | 360.45 | 446.77 | -19.32% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel、INTC」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA、NVDA」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [This AI Chip Stock Just Signed Massive Deals With 3 Hyperscalers, and It Still Looks Like a Great Buy Right Now (Hint: Not Nvidia or Intel) - The Globe and Mail](https://news.google.com/rss/articles/CBMiwgJBVV95cUxQenpISGNBdWk3bXBfUHVabmpLTDJoUGlHR29CbFZjUWkyZlU2WFU0d18wdEpzQjNMTEg5cmtlWUw0VHppQlRoNUxKVmMxZ21XZUpwclE0T2EwanowWjFPMVFmX01abzRHeTFwQm42N1JwTnZzX2h0UHlnM0RkRVp4Z0l4N3ZLbWxKeEMyZVFOVUJ1R2pueGJsbTBscGI0Nk5nZU9OU040VTJfaDNSZlFfQlFCMDhtVWJxSU5lZGxhQjBldmtFYV9IblZQcUJsVjFDbDVlRFBLcDJHUVhVOGs4clVOM0NrNVR0ZXZXaXp3TWhZdHFHWnRFOG1na0hXaEV4RjdkY2NzUlJqVDBQY2JrZHpXWkdJX0JmVEhzTFpLdWR2SnpXU21GamJTTzBjY1FSVGI1bEdpaFdUZ2FTaHRhUEhR?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 05 Jul 2026 08:50:00 GMT
- [AI Semiconductor Stocks July 2026: NVDA, AMD, INTC Investment Analysis - Intellectia AI](https://news.google.com/rss/articles/CBMibkFVX3lxTE1rVzN0cnZWeF9vLVFmVWdQWktEV3J4SE9vZmdBYUs1eElSZjNrLUlJbGlmQ1ZHZzNDR3lCZzlfejBEa1FkeEZteTBxR2lsTld1dHNqVHczVElvMDUtNmhISlZXa2ExTWFrRDVoa2Jn?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 05 Jul 2026 00:16:16 GMT
- [104職缺7月達123萬個AI半導體綠領徵才同步升溫| 產經 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1mRFhtMjZWYTBmRnJnNzY1YnNnR0VaQlNOM2M5d3dlZG9lak1FUFdINU1iRFc2NlNrdkFIcmZ1VFVDOUI5OWJWUFljRGdpNXJyYWx5VW5DVndONGtycEE?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 04 Jul 2026 04:09:00 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股有望挑戰歷史高點 法人看好三大題材漲聲響起 | 市場焦點 | 證券 - 經濟日報；上周台股漲2,208點、周線翻紅 法人：費半若能止穩 台股更穩健 - 經濟日報；AMD Stock and Intel Crushed Nvidia in the First Half. Here's My Prediction for the Second Half. - The Motley Fool

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.27 | -7.72% | +11.71% | 194.83 | 211.14 | -7.72% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.45 | N/A | N/A | 517.82 | 517.82 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.45 | N/A | N/A | 120.35 | 120.35 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA、輝達」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [台股有望挑戰歷史高點 法人看好三大題材漲聲響起 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiekFVX3lxTE9mR2ZsT0hHOWZwUldjeW53bEItTlRoNDh1MGs4em1pQVJLNEdXRWJFQUFYbFJvQXgxZnFlRE1pcXJfQ3Nyc1dha1ptNlJ6eExiTU1IYk5oLU5WOUlYd1NWS2R4WkdUTHYtSEVGakJEMUxDUlNTZmw1Nkt3?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 05 Jul 2026 15:17:25 GMT
- [上周台股漲2,208點、周線翻紅 法人：費半若能止穩 台股更穩健 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9wd1pxY3p5NWItY24xSVpzeWdFVnVRREVtTkNISkxkQ0p3ampvOEl3RkNSc3pvVXNEVThSb2lBaW5CcWlBMHBGODZCcmNRc29qVTdQQXlDR1ZUUdIBX0FVX3lxTFAzcTgzQU91NUlIM2htNXZ5RmppbUdmX3Z1eEQ4eUQ1NElBaVo5WFFFTUVTNXJwZzg4X3hJMW85bTRZVl9tRkNqel80OXplaF92VjlMcHc5S1ZOTnJnNXgw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 05 Jul 2026 06:36:24 GMT
- [AMD Stock and Intel Crushed Nvidia in the First Half. Here's My Prediction for the Second Half. - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxOa3NzTTVhWW9xdU1Temp1YmIwSDVKSHlDM0dHOWJqYWtOSHg4TmI3SjNQRGlZSldqWGQyMW50NnZVUHNBMGlPNzl5TXQ3UGdnX2VvWlB2RnZOakl3TzNBX2xnWmZGMWE3REVMRTVCdi1SUjFNRmk3WVFjUGEyMjBUNlpZb1JPbkhJT3lmcDhZX1o5N1VZSzdBTA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 05 Jul 2026 22:33:26 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits；AI Memory Stocks Micron and Sandisk Are Up 200% in the Last 3 Months. History Says This Will Happen Next. - AOL.com；SanDisk Soars 858% to the Top. S&P 500's Top 10 Gainers for the First Half of 2026 Revealed, Why Wall Street Warns of a Deep Correction in the Second Half. - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.62 | N/A | N/A | 975.56 | 975.56 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.30 | -14.89% | -25.27% | 1,745.00 | 2,335.00 | -25.27% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.45 | N/A | N/A | 517.82 | 517.82 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.45 | N/A | N/A | 120.35 | 120.35 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -7.72% | +11.71% | 194.83 | 211.14 | -7.72% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron」，共 2 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 2 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits](https://news.google.com/rss/articles/CBMi0AFBVV95cUxOWm5KdEIwSXpyY191UEhDa1V6NVpWa01UbmpJeWRIV0ttT080TmpDNEhISW5TWkQwUzBVYzBqSHJPWXRVNVJCampoWWRlYmhKVkhIeHBJLS0wLW5Ua09GQnRORXpFcW5qTEJkcnJGcW55aU5rOFVOLUFMbjRPZEpWT3A2ZllucnM0SU9JNEdrNUwyc3V2WHAtNFk3VHl4R1F6SkZRMFpleEE2Zl9MdW4tSEpMMnFGZ2hQZURWQ3B1WDlPR1BhRjJELVN5ODJWYVR3?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 05 Jul 2026 01:33:23 GMT
- [AI Memory Stocks Micron and Sandisk Are Up 200% in the Last 3 Months. History Says This Will Happen Next. - AOL.com](https://news.google.com/rss/articles/CBMif0FVX3lxTE5yWVpaQ2gxRjNwTFNDUHlMeVRPNWFONjRhb3BOcnpCaHlBa0RPc3JUOWJYMi1Jb28yOFF1OU9HdVQwSnE3a3RxRHBlZ2tyWFNZdTFvcDBvb1B4QloyQVNwS0dxQnVLVE1WVWk2cG5hRU5uT01sWFdHZGJlc3RWUDg?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 05 Jul 2026 18:56:47 GMT
- [SanDisk Soars 858% to the Top. S&P 500's Top 10 Gainers for the First Half of 2026 Revealed, Why Wall Street Warns of a Deep Correction in the Second Half. - TradingKey](https://news.google.com/rss/articles/CBMixAFBVV95cUxNMmRoNU1MZW5vN3FUQ2xSMDV6RVJqSU5xX1ZzeTFFTTBzVTBSc0tMVDhfSDZtc3ozMEdwbFprRjhTcEY4c1AzTDM5VEVEWVp4ZVMyNjVvLTh2TUIybTF2MDVLSFBXTy1ZbEhSMnlITnd4TmlGUkxPM25ZYVBOZmoySXdSMWl6X183eC1PMEhmODI3amtJUXRjZFREc2pwZUZLcmZCMW5jN1ZobGhpa1ZmSEFHUk1JdDVUMTJ1Y2k5TTJ1eG9H?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 04 Jul 2026 19:09:05 GMT

## 新興題材：台股新一季法說

摘要：新興題材：台股新一季法說 相關新聞集中在：台股新一季法說會將自本周登場 AI 指標股領軍衝一波 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股新一季法說會將自本周登場 AI 指標股領軍衝一波 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1SbUZ2YXlad2dYcEszUUlRUExKcnhZbUg4dG82QnhidkV6Y1hYRmEyd3ByTV9WU3VDUmJiT1dpRU1VOUVaVDFyaTc2T0U0ajZrNzcwWl9Tc0o3Z9IBX0FVX3lxTE1hTXh0THJSSXhzMGhJaWFuaXFyT1hKZTRMRmFhWlRJaWRsOVViN2xJOVV2SUxSN2FXN004bm5sMGdXTzFXWTVJcjJndktEZXotckFzekQxMjBlT1FpTTVz?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 04 Jul 2026 09:00:00 GMT

## 新興題材：台股超級法說

摘要：新興題材：台股超級法說 相關新聞集中在：台股超級法說行情開跑 多頭人氣可用 指數蓄勢挑戰50K - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股超級法說行情開跑 多頭人氣可用 指數蓄勢挑戰50K - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE44VnpHWHAxLVlyRS16X1Y2cndXcDN3V3M2V053ZGx4R28tRElPVURhVlNqME9GTjFlQ0tpNFRNTUE5dTFMbVRwNHFjVE9EVExub211QU1VWFV4d9IBX0FVX3lxTE5BdWJENVlCSTF5NlBqWHZXdnRwbFhrbzRzMmk4NWhhcXV3VWstcTJrZnBLX2Jjc2xxakl3NG9GZkpJY1pMV3hjelNWdEJmak5ScDJYNDkxaXRDMkI3MXBz?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 05 Jul 2026 18:22:38 GMT

## 新興題材：半導體法說

摘要：新興題材：半導體法說 相關新聞集中在：半導體法說、營收將公布 法人：台股前景看好 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [半導體法說、營收將公布 法人：台股前景看好 - 經濟日報](https://news.google.com/rss/articles/CBMid0FVX3lxTE1SQ2FOMzkyZDZEZl9YMjlIOFROeVZkVVJiUjR2V0NsdjR6TXd5R2Q0MURDS2ZGN2lZZW5yQV9pOWNLNWxYS3NnbVFUTTZ2b0pmTk1wcFdVWUhLU1ZZZzd0ODdTUlNjOEk0Q2hydUlmak1ZbEUtT09F0gFfQVVfeXFMUEkyT183aUgxSS0zdWJLOTg5Tmc5Q2M1N3B6TWVYXzlHeVU5ZkVoQU9rMFdEa09SdkNUMVVndV9vNFI4ZHJTZ1ZqbUxULXRDWm1HWUdxWEJLRHc5eHhpRlk?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 05 Jul 2026 08:27:52 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
