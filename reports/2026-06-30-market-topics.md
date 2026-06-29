# 每日股市熱門話題分析 - 2026-06-30

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **綜合市場情緒**｜中性｜熱度 34｜市場確認 N/A｜同向 0/0
2. **記憶體與 HBM 供應鏈**｜正向｜熱度 12｜市場確認 54.27｜同向 2/3
3. **AI 伺服器與資料中心**｜中性｜熱度 11｜市場確認 N/A｜同向 0/0
4. **半導體與晶片供應鏈**｜負向｜熱度 6｜市場確認 50.81｜同向 3/5
5. **新興題材：TradingKey**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.44（樣本 8）
- 5日相關係數：-0.27（樣本 8）
- 同向比例：5/8

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 記憶體與 HBM 供應鏈 | 54.27 | 2/3 | 1 | +2.53% | -5.24% |
| AI 伺服器與資料中心 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | 50.81 | 3/5 | 1 | +2.94% | -2.74% |
| 新興題材：TradingKey | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：台積法說 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：B0729B41 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-06-17 | 0.17 | 0.47 | +62.50% | 8 |
| 2026-06-18 | -0.41 | -0.41 | +42.86% | 7 |
| 2026-06-19 | 0.06 | -0.04 | +57.14% | 7 |
| 2026-06-20 | 0.29 | 0.21 | +63.16% | 19 |
| 2026-06-21 | -0.01 | 0.32 | +55.56% | 18 |
| 2026-06-22 | -0.87 | -0.87 | +100.00% | 3 |
| 2026-06-23 | 0.38 | 0.01 | +62.50% | 8 |
| 2026-06-24 | -0.38 | -0.11 | +25.00% | 12 |
| 2026-06-25 | 0.10 | -0.21 | +20.00% | 5 |
| 2026-06-26 | 0.08 | 0.04 | +25.00% | 16 |
| 2026-06-27 | 0.12 | 0.29 | +57.89% | 19 |
| 2026-06-28 | 0.16 | 0.55 | +85.71% | 14 |
| 2026-06-29 | 0.49 | -0.25 | +38.46% | 13 |
| 2026-06-30 | 0.44 | -0.27 | +62.50% | 8 |

## 歷史回測摘要

- 回測日期：2026-06-30
- 近5日 3日相關：-0.19
- 近5日 5日相關：-0.58
- 同向比例：+50.00%
- 權重狀態：未調整

- 方向準確度：+50.00%
- 信心排序準確度：-0.19
- 診斷：方向與信心皆需修正

調整原因：近 5 日有效樣本 8 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：綜合市場情緒 相關新聞集中在：急跌就是大利多！台股力拚大 V 轉 法人圈期待本周行情 - 經濟日報；璞玉收益指數 優於大盤 - 經濟日報；聯發科評價 麥格理證券喊上萬元 給予「優於大盤」評級 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 131.72 | 131.72 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2454 聯發科 | 新聞直接提及 | 0.00 | -8.75% | -12.43% | 3,910.00 | 4,310.00 | -9.28% | 不適用 | 62.91 | N/A | 47.43B TWD / 4.99% | 2026-06-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2454：新聞直接提及「聯發科」，共 1 篇新聞命中。

### 主要來源

- [急跌就是大利多！台股力拚大 V 轉 法人圈期待本周行情 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFA3ZjEybWJVVFM3V0hINUJYWG9nY25Fak5NcWJld0RPZDlySTVSM0h0NWFtUzNoWDNRTWdfWlZud3NPZmwyTmc4RTV2QlJ3cmxyYnFLWDhhQnFLUdIBX0FVX3lxTE9mYnVGLTNvb2tNWjZfYXFvR3pNQ3hINVVoOGxBWW5keE9CejZmaVlsQ0JaaEMtb0YycTVvTDFONjdnTGFPQVU5TXFlN2pXZ2FtV2kxUXR0N3NKM0laZzRn?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 28 Jun 2026 17:29:39 GMT
- [璞玉收益指數 優於大盤 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxNV2xQcUpVbTdmUGh0aWhSWGxnSmRBbW5ZS04xbW9pWEMya1hvSjRrdmRGa3puN0NMN0kxWGdDTzlnMEtkMnZNY0RIQ3ZDZFhXa0Z4RzY2d3dqM09oREpqZmRqYUI2dXljQmwtbWpDX2FLbm1wdGd0MmZ1X1RSeVhZdtIBX0FVX3lxTFBPT1NEblcyU2hXTmNhTDR6cXd2bjZEa0tzUkFhbG1GTEFmM1NURGkybzd5bkdzeHVUOElxbUhuNFJXb1F5by1qS0NyUTRrbE1jLVYtOGRnZ2tCd0gwaUNV?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 29 Jun 2026 16:58:58 GMT
- [聯發科評價 麥格理證券喊上萬元 給予「優於大盤」評級 - 經濟日報](https://news.google.com/rss/articles/CBMidEFVX3lxTE1aUW1vaW8tTkM2ZVJLcFlqSW5SbDc2aFE1VU1tOHhqeFJ2Q21yYUhFMHhHOGplUER5OEZ0amZhbW9zTVV3RDZDdG1OcXIyXy02LXc5U1hEelJJTUhCT0ktcXJxQ3F3QS1DbEo0Vjg1V2EwVXFn0gFfQVVfeXFMT0dVSkd0Z1BMNkxhbUVxOE4tT2ZQSXJIQTFHV05XZFpxQTFQd3RibndNS1BBRW0yS0ZjMVZoUFFSNV9ZcGxlenFtM1pNSEZXX2VmN1FJcWQ1YUVlcGdjUXc?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 29 Jun 2026 17:19:59 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Micron vs SanDisk: Which Memory Stock Has More Upside as AI Demand Surges? - TIKR.com；The Zacks Analyst Blog Highlights Micron Technology and Sandisk - The Globe and Mail；Sandisk: Avoid Becoming Exit Liquidity When The AI Trade Kabooms (NASDAQ:SNDK) - Seeking Alpha

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| SNDK SanDisk | 新聞直接提及 | +0.65 | +7.10% | -9.82% | 2,050.39 | 2,335.00 | -12.19% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 新聞直接提及 | +0.65 | N/A | N/A | 1,145.28 | 1,145.28 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.48 | N/A | N/A | 539.49 | 539.49 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 新聞直接提及 | +0.24 | -6.15% | -27.26% | 368.57 | 506.69 | -27.26% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 新聞直接提及 | +0.48 | +6.65% | +21.37% | 281.74 | 312.06 | -9.72% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -2.30% | +10.03% | 194.97 | 211.14 | -7.66% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- SNDK：新聞直接提及「SanDisk、SNDK」，共 6 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：surges。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- MU：新聞直接提及「Micron、Micron Technology」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：surges。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Micron vs SanDisk: Which Memory Stock Has More Upside as AI Demand Surges? - TIKR.com](https://news.google.com/rss/articles/CBMiqgFBVV95cUxNZWxiWDQ5anN2OVVNdlk4RnBNQ3lHNnQ0SWcwSEZCU3BLNGdhS3lYYWsydmJJdnp4THkzSGRmR1JYRERsb2oyYlJDX21sVEVQQWw3VnhPTVNwTEdUVE8zMjVZOUkxTXd6NmVrMmNBR1BLdlZzOEI4bTcxbEMwaTFWM09PNFRRcElwNURhbFVXYmVTNmdWTHI5R19CZmNnTVFMMDRwNl9aV2JVUQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 29 Jun 2026 11:05:22 GMT
- [The Zacks Analyst Blog Highlights Micron Technology and Sandisk - The Globe and Mail](https://news.google.com/rss/articles/CBMi3wFBVV95cUxPVFE1NDExU25VWC1laFVaYzFUVWw2Y3hidnBONXh4N24wWUs3YlFNalFPMWdlSGQ1cDZRSEo4SllHMjNFOVUwZWQ0VlNOZ3NGOFVBc2ZIRVVhRFdxQWg2UU9GVDl3YmJ4VHdYbU1UR3NmZEJMVV80Si00UGpOQkRRZjNwSGc2ZDVMenBndEtFYTRJeHhBUmNXQzVGbmJMY0xxNG9UQ2M5RUpPVEctNHNlU2dBNFY3WjMzZHhhWjBfMXFlejU1eENadGNaNHNxbFlPSUxmX2NGZkgwOHlNTGtv?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 29 Jun 2026 16:01:03 GMT
- [Sandisk: Avoid Becoming Exit Liquidity When The AI Trade Kabooms (NASDAQ:SNDK) - Seeking Alpha](https://news.google.com/rss/articles/CBMipwFBVV95cUxONWw3MEY3dlpUMVBIbzhxZTRhREdFbFlub08yQjRoLWR4aTJGcUFPdDVUZ2tMb25pdmlHcW9RU2tkQlpsTldYbzRLT012anBaUnFUM2lqYXkxWUw1Y0tXSExqX0UxTHZkdmJIQnR3UVFGV3NaNmh0cDFLTlhKNXR0anJWY3JJdkItRk4yUGo5ajc1NWJDWWt4REpBZUc2dGRVdkVBNVVPaw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 29 Jun 2026 17:42:10 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：韓國將投入逾37兆打造新半導體聚落與AI資料中心| 國際 - 中央社 CNA；Apple says it is releasing updates early in response to AI cybersecurity concerns - Reuters；Banks get creative and look further afield as AI-fueled debt soars - Reuters

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AAPL 蘋果 | 新聞直接提及 | 0.00 | +6.65% | +21.37% | 281.74 | 312.06 | -9.72% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 131.72 | 131.72 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -2.30% | +10.03% | 194.97 | 211.14 | -7.66% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 539.49 | 539.49 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -0.84% | -5.58% | 2,370.00 | 2,370.00 | 0.00% | 不適用 | 74.39 | N/A | 416.98B TWD / 30.09% | 2026-06-01 |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | -6.15% | -27.26% | 368.57 | 506.69 | -27.26% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -10.78% | +16.55% | 372.45 | 446.77 | -16.63% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | -3.98% | -6.97% | 627.00 | 632.00 | -0.79% | 不適用 | 10.86 | N/A | 63.03B TWD / 28.57% | 2026-06-01 |

關聯理由（前 3）：
- AAPL：新聞直接提及「Apple」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 5 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 5 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [韓國將投入逾37兆打造新半導體聚落與AI資料中心| 國際 - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTFAwaXZfUzRBNW1jY2ZIRGNaNmhITlNKakVpTEE3VUJ1dW0tYkc0T2hsYWd0elE1Rlk4b3NYWjB0MnluVFBLbWQ1M1JCN1dGei1tZ19CVG5qakhPNG9Wc2dN?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 29 Jun 2026 09:38:00 GMT
- [Apple says it is releasing updates early in response to AI cybersecurity concerns - Reuters](https://news.google.com/rss/articles/CBMivAFBVV95cUxQS1dqel8tXzhpYzZWUlBPSVFZUUs4SXBZaFhSa3BYSEduQUlUdHpnWUthMXEtOV9zNzFnSElUUXY3OUxTci0yS0RKVzZWNzZPbm5ZV0RaS3FSUllGWmp0Q05HNTRCSEthY0Mwa1ZhNUNOa09LUURBVnlGSi15cG9kQlBzUmhfRG0wdnFxVlpsb21DVlkzbElsdmpNWUFqaksyVFZFdVhTdE1kUVlQUzMzM1Z3ZmpTWWhMSUFkeQ?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 29 Jun 2026 21:31:04 GMT
- [Banks get creative and look further afield as AI-fueled debt soars - Reuters](https://news.google.com/rss/articles/CBMisgFBVV95cUxOdDBiVE50bXZsYUc3enlSS2I5WjlqVkJtRHF0S0Mtbms4cmR6bnRSNGpDRHczSDQ0VkpyY3JLSXpka2NBYU11amM2akJROFVaZzFOMmppaHJpd0ZjVjFqWnRrRmplV2hFaHZ3N0otLWtpUm1MTkVTMDJSNFBwMnRad1k3ekN5UmVNOGI0Y05fSGNCemhUaUhkbVhCcFhNaWdxbklhRVJ5RkE5eHV0b2FJVkxn?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 29 Jun 2026 11:33:41 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：韓國將投入逾37兆打造新半導體聚落與AI資料中心| 國際 - 中央社 CNA；台股功率半導體恐遭波及！安森美狂瀉23％ 專家點名這5檔下周小心- 證券 - 工商時報；Key facts on South Korea's three chip and AI 'mega projects' - Reuters

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | -0.08 | N/A | N/A | 131.72 | 131.72 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.04 | -0.84% | -5.58% | 2,370.00 | 2,370.00 | 0.00% | 未明確 | 74.39 | N/A | 416.98B TWD / 30.09% | 2026-06-01 |
| 2303 聯電 | 產業/供應鏈推估 | -0.05 | -7.87% | +2.50% | 164.00 | 164.00 | 0.00% | 同向 | 4.00 | N/A | 22.94B TWD / 17.78% | 2026-06-01 |
| NVDA 輝達 | 產業/供應鏈推估 | -0.04 | -2.30% | +10.03% | 194.97 | 211.14 | -7.66% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | -0.04 | N/A | N/A | 539.49 | 539.49 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | -0.04 | N/A | N/A | 1,145.28 | 1,145.28 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | -0.02 | +7.10% | -9.82% | 2,050.39 | 2,335.00 | -12.19% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -10.78% | +16.55% | 372.45 | 446.77 | -16.63% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 CPU, server CPU, x86, foundry；其中 2 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 2 篇新聞出現相關標籤。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 2 篇新聞出現相關標籤。

### 主要來源

- [韓國將投入逾37兆打造新半導體聚落與AI資料中心| 國際 - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTFAwaXZfUzRBNW1jY2ZIRGNaNmhITlNKakVpTEE3VUJ1dW0tYkc0T2hsYWd0elE1Rlk4b3NYWjB0MnluVFBLbWQ1M1JCN1dGei1tZ19CVG5qakhPNG9Wc2dN?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 29 Jun 2026 09:38:00 GMT
- [台股功率半導體恐遭波及！安森美狂瀉23％ 專家點名這5檔下周小心- 證券 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5aRDdzUFdaU2pYOGVNTUhDb1cwUjFoUjV3UTdYV0xtLVlPOXJmZm54eTU5dXdDTmg4ekc0SGlrR0IxQkN2LW02NkN4RjlEWlZNRmRsM0pzeXB1LTB6RURJ?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 28 Jun 2026 03:37:00 GMT
- [Key facts on South Korea's three chip and AI 'mega projects' - Reuters](https://news.google.com/rss/articles/CBMirgFBVV95cUxQNnRKRHFyQlZFbnRGMEJPclZSWHJOU1NObHFnSUR2QUlZZmJsMXhUZlFaS21TVUZ5bFZVdTZKa1R2XzJYcDdpT01vYzR1V2k4OVhnNUlEbnBJc1FhSTVZY29zaDJqTnNEanRvckU2NXdnTXFjelN0aGxncnRSZG44dVg5RFNFeGc0dmMtNGEtcE55RnhQWm85dkRDMFVXazdNVTRZNzk3Z041YTk1S3c?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 29 Jun 2026 11:32:54 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Micron, SanDisk Both Plunge Over 6%; Apple, Microsoft Price Hikes Backfire on Market, Memory Stocks Face Loosening Earnings Logic - TradingKey；SanDisk Corporation Stock (SNDK) Moved Down by 4.65% on Jun 29: A Full Analysis - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| SNDK SanDisk | 新聞直接提及 | 0.00 | +7.10% | -9.82% | 2,050.39 | 2,335.00 | -12.19% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 1,145.28 | 1,145.28 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 新聞直接提及 | 0.00 | -6.15% | -27.26% | 368.57 | 506.69 | -27.26% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 新聞直接提及 | 0.00 | +6.65% | +21.37% | 281.74 | 312.06 | -9.72% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- SNDK：新聞直接提及「SanDisk、SNDK」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- MU：新聞直接提及「Micron」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MSFT：新聞直接提及「Microsoft」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Micron, SanDisk Both Plunge Over 6%; Apple, Microsoft Price Hikes Backfire on Market, Memory Stocks Face Loosening Earnings Logic - TradingKey](https://news.google.com/rss/articles/CBMiyAFBVV95cUxNLURtVkFWdE43ZTQwQk5ZMDhPdG12bmFnLTNVMkcwcFAtaDdYLWxDTER0TWJ5VmpkdnI4d3ZNQXNXUUhTY2pZcTF6UERHWl9VM1VLWEZRV000Y0VCQlU2cGhyd2ZQanJKRnpNb0JUN0todFpQNzVBS2V1Z2xTMXlwdm1tQ01Ob0lMSUdQbGpHbHllRTNlQ3hZMlZXTkJsZExWYW1XaHktX21kY2RsU3lDekltUFlVZlJfSjB2Tm5LVHdyVEJ6T0ktUg?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 29 Jun 2026 15:02:12 GMT
- [SanDisk Corporation Stock (SNDK) Moved Down by 4.65% on Jun 29: A Full Analysis - TradingKey](https://news.google.com/rss/articles/CBMiiwFBVV95cUxQbjlIVHJMbklZVEY4WGI3YnlSZWJBQ0U4d0RzbXk2NktJN1U1Ym8tQ3NJY0Y5UUNWQ1ZDRkNmcWxiRmZYd2ljYzBjX3ZraGk5ZTRsb0l6WmVyVWlyR0lpNHFzYlByOE9SdmJTclRqaGlvMWVpc29QQWNwUmJUT0FkNlFWMmpUdDB5d0xN?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 29 Jun 2026 16:15:28 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》量縮收漲428點，月線得而復失- 新聞 - MoneyDJ；個股動態報導內容-68304238-1E97-4B5A-A07E-865DB928C3AD - MoneyDJ；個股動態報導內容-76F46F44-79D7-4201-84B8-1AE2B53B3480 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》量縮收漲428點，月線得而復失- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPQzZFeWt3eEVsMDI4cWJJOVEyUUE0cWZOb0piRkxLLUVKMjJoRHMxR1JObFBsZE4yLTBYRU15TnB4VjFhLU9yUzA3UVNWUkVTMVFPa3p6aTBkclJ2ZE1ndU1fTVlTV1dsR3dpOGptMXZQNGdBZnZRcDBvNE5FNnhrSFYyamExSFA3TTJ0OXRQSFBTZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 29 Jun 2026 07:50:00 GMT
- [個股動態報導內容-68304238-1E97-4B5A-A07E-865DB928C3AD - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxOVHNuLUN5MDFiV0NfbElzVVNGd19IZGJuOVNfMi1WZFpmTE9QQnFWQTJOTmhtc2Ezc3dHM2RWWlU2aUE1YWYzWUpyN2NKR0tmUFc1c0FFa1lZRzgySnRIZDdXQWJod2liX28yV3ZDaVBWRHJsbjZGZnBDdzZqdTVsaGJtb0ZzaFU2aU9JSzI3eDBDWXFV?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 29 Jun 2026 12:24:10 GMT
- [個股動態報導內容-76F46F44-79D7-4201-84B8-1AE2B53B3480 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxQSU02VW1hTDNKV2FfQmo3cExibDRyMnR2TGRSV3AyakhneUJMUDNDNjB0OVJvMC11VVd5c0NJWW5OWUFMaWFFZWFxWUZzN2tiXy1rN2VZSWtuc2F3NF9BZ00tWjVqLUlXdjV0M2tIWDZxMVhTekZQeGljZ2dxcThsOG9lREZCa0lDdzk4VlM2Sk1WN1NT?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 29 Jun 2026 12:24:10 GMT

## 新興題材：台積法說

摘要：新興題材：台積法說 相關新聞集中在：台股 7月不看淡 台積法說看多 不排除上攻5萬點 - 經濟日報；台股 7月不看淡 台積法說看多 不排除上攻5萬點 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股 7月不看淡 台積法說看多 不排除上攻5萬點 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9pbnJwS1BtRE9xQUFUYTRVNXFtd3loc1duNXFnd1p6QzhlRVNJekJlMlh1X2Y2aE1IZ1ZXTkRnNUpaM1JPMEJWRE5TcTlvRWZNWHo4dWFJRDZmd9IBX0FVX3lxTE5NaURJSk53U1RQUnlHQ3RtYVpGOWF3WlVzNlVMNnZ1QUJVanlQU1NWS1JWWDNQc3AyZXZZOU05VjJLWWJnRnl3cFdXekNTVXpxRVh5YllOUFB6bG5wSy13?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 29 Jun 2026 03:00:00 GMT
- [台股 7月不看淡 台積法說看多 不排除上攻5萬點 - 經濟日報](https://news.google.com/rss/articles/CBMikAFBVV95cUxOZE51R040c1hUNkdrelJsNlV1SVotMXdUc0NwT1JNaGZOZ21YbFlhU1NpQjFBTkRLczVZNEVyWGI5eERGT3BRSFBvNkJTem5xSzFPM2RxTDFhbHFXYUJzOG45SE41QU54c1dncndjTVFYR29CM0t6SktZVEVUcWpSSjR1ejZfSzU3R1hVX194eVXSAV9BVV95cUxOTWlESUpOd1NUUFJ5R0N0bWFaRjlhd1pVczZVTDZ2dUFCVWp5UFNTVktSVlgzUHNwMmV2WTlNOVYyS1liZ0Z5d3BXV3pDU1V6cUVYeWJZTlBQemxucEstdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 28 Jun 2026 09:00:00 GMT

## 新興題材：B0729B41

摘要：新興題材：B0729B41 相關新聞集中在：個股動態報導內容-B0729B41-93EF-4775-A2E0-3DE7459E8819 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-B0729B41-93EF-4775-A2E0-3DE7459E8819 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxQeVBacUYtV0lKd0FDMHNPRENiUnFONmdRRzhOTmtPb3lMZWJZTEwxSEpoNFRlVDdoWGpZZk9hY3plQ054MkltSVN4ZE9tSHVudnZycEV1akZ2Y0pSUVpWRi1EaGZZemw1TlkzZG9fSVFBRkpoWVlvYzVXdUVhQWtxU1RkdjBicElZWlVSVlQzMzVGdUVV?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 29 Jun 2026 12:24:10 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
- TWSE PER/PBR 抓取失敗：Expecting value: line 1 column 1 (char 0)
