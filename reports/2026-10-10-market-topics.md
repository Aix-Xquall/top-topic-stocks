# 每日股市熱門話題分析 - 2026-10-10

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **關稅與供應鏈轉移**｜正向｜熱度 2｜市場確認 81.55｜同向 1/1
2. **記憶體與 HBM 供應鏈**｜正向｜熱度 7｜市場確認 50.03｜同向 3/5
3. **新興題材：台積電法說**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
4. **AI 伺服器與資料中心**｜中性｜熱度 11｜市場確認 N/A｜同向 0/0
5. **半導體與晶片供應鏈**｜中性｜熱度 9｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.28（樣本 7）
- 5日相關係數：-0.96（樣本 4）
- 同向比例：4/7

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 關稅與供應鏈轉移 | 81.55 | 1/1 | 0 | +3.85% | +14.59% |
| 記憶體與 HBM 供應鏈 | 50.03 | 3/5 | 2 | +2.68% | +2.31% |
| 新興題材：台積電法說 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | 0.00 | 0/1 | 1 | -4.04% | -1.99% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：2場法說 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-09-27 | 0.11 | -0.14 | +57.14% | 14 |
| 2026-09-28 | 0.05 | -0.53 | +63.64% | 11 |
| 2026-09-29 | 0.31 | -0.78 | +16.67% | 6 |
| 2026-09-30 | 0.05 | 0.04 | +33.33% | 18 |
| 2026-10-01 | 0.21 | -0.27 | +40.00% | 20 |
| 2026-10-02 | 0.51 | 0.37 | +72.73% | 11 |
| 2026-10-03 | -0.35 | 0.13 | +16.67% | 6 |
| 2026-10-04 | -0.12 | 0.70 | +80.00% | 20 |
| 2026-10-05 | -0.16 | 0.29 | +73.33% | 15 |
| 2026-10-06 | -0.72 | -0.75 | +37.50% | 8 |
| 2026-10-07 | 0.48 | 0.61 | +73.33% | 15 |
| 2026-10-08 | 0.13 | 0.40 | +58.33% | 12 |
| 2026-10-09 | -0.03 | 0.37 | +38.89% | 18 |
| 2026-10-10 | -0.28 | -0.96 | +57.14% | 7 |

## 歷史回測摘要

- 回測日期：2026-10-10
- 近5日 3日相關：0.01
- 近5日 5日相關：0.01
- 同向比例：+25.00%
- 權重狀態：未調整

- 方向準確度：+25.00%
- 信心排序準確度：0.01
- 診斷：低相關

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

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：整理包／台股5萬點靠他們？ 台廠第4季爆發潮來了！完整輝達供應鏈名單、潛在受惠股一次看 - 經濟日報；台股高檔震盪免驚！法人估企業獲利年增84%、AI 供應鏈續旺 | 市場焦點 | 證券 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.42 | +3.85% | +14.59% | 229.28 | 230.48 | -0.52% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +7.88% | +20.72% | 336.64 | 340.42 | -1.11% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | -1.97% | -1.97% | 249.00 | 289.00 | -13.84% | 不適用 | 15.21 | 16.41 | 1158.63B TWD / 38.42% | 2026-10-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [整理包／台股5萬點靠他們？ 台廠第4季爆發潮來了！完整輝達供應鏈名單、潛在受惠股一次看 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTE1fUEppNWpZZlc3bVF4Sy1zaUJjQWE5NjAwTGZSaFFNU21ZSWo0Und6RG1BY0QxTm93R2RHV3diX0RaX2k2SHRka3FCam1VeS1aTjduTlg5akJyOEJw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 08 Oct 2026 06:47:15 GMT
- [台股高檔震盪免驚！法人估企業獲利年增84%、AI 供應鏈續旺 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxOZnp6RHg1SVZHQVNGM3RDczN2ekNGb1pHTWhrbjliRzZoaTU5YUxxTFIxX3hEbm84SUNZYUI0OVhyS2kzRFIwZzBoM0tLU1lEWE9SSWlzZzFPMHBzeVIzMXMtRnNxM3ppVUh6WFU3SHIzSjRiaFh1WUl2R1huZGxiNg?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 09 Oct 2026 05:18:26 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits；INTC, AMD, MU, NVDA: Chip Stocks Tumble Again, Stalling A Nascent Rebound - Stocktwits；Not Micron. Not Sandisk. This Memory Stock Is Quietly Gaining Share. - The Motley Fool

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.57 | +5.97% | N/A | 1,029.00 | 1,035.84 | -0.66% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.28 | -5.56% | -9.97% | 1,609.46 | 2,335.00 | -31.07% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.49 | +17.83% | N/A | 608.10 | 620.68 | -2.03% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.24 | -8.70% | N/A | 104.70 | 114.68 | -8.70% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.43 | +3.85% | +14.59% | 229.28 | 230.48 | -0.52% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron、memory」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：growth, rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 2 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits](https://news.google.com/rss/articles/CBMi0AFBVV95cUxOWm5KdEIwSXpyY191UEhDa1V6NVpWa01UbmpJeWRIV0ttT080TmpDNEhISW5TWkQwUzBVYzBqSHJPWXRVNVJCampoWWRlYmhKVkhIeHBJLS0wLW5Ua09GQnRORXpFcW5qTEJkcnJGcW55aU5rOFVOLUFMbjRPZEpWT3A2ZllucnM0SU9JNEdrNUwyc3V2WHAtNFk3VHl4R1F6SkZRMFpleEE2Zl9MdW4tSEpMMnFGZ2hQZURWQ3B1WDlPR1BhRjJELVN5ODJWYVR3?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 09 Oct 2026 07:20:23 GMT
- [INTC, AMD, MU, NVDA: Chip Stocks Tumble Again, Stalling A Nascent Rebound - Stocktwits](https://news.google.com/rss/articles/CBMizAFBVV95cUxORHdiV3k3V2RtSVBoRTJaaW5PcTZhQzBTNlRUM2VqcjBpcTViNkREdS1uVGtnb1FYckxkREh4Z00zN2NBSnlNRGZ0SWhpNERydkZKTlJCejRLQ2xqejNxREhfS1ZzSm5CdjhrZzlZTnRiN1Z6M3VtSDU1d2trMG9jVFUwT3hadk93R2l0TlBBZkttekkyTDBHTW1Zc01YTmNzRVJ3Tm11dGcwNktNX04yU0pLUENBQl9sOUI4dVMydW02UUhxZDVXX2pZT0M?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 09 Oct 2026 02:20:41 GMT
- [Not Micron. Not Sandisk. This Memory Stock Is Quietly Gaining Share. - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxPSFlZeUJQU0hxYXhwUC1jdWtaRU5id19uWDFxbzdKRzdRQ3h4bmdEekIzblVncS1FYU1CUW5jUE9vVEZpcDFzU2JnaUJVcndJaFh1XzUtbWo0MFhjN1diSEkxY1lxQkVRQjFwb05NZ0tCaWk4RF9DV015QVpNZV8tNGxremd5ZW8wZ3lIMjc5RWNJR25zMGRGSg?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 09 Oct 2026 16:40:00 GMT

## 新興題材：台積電法說

摘要：新興題材：台積電法說 相關新聞集中在：法人：台積電法說會15日登場　有助支撐台股高檔整理 - 經濟日報；法人：台積電法說會15日登場有助支撐台股高檔整理| 證券 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | 0.00 | -0.97% | +1.59% | 2,550.00 | 2,550.00 | 0.00% | 不適用 | 86.28 | 29.56 | 511.86B TWD / 54.65% | 2026-10-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 2 篇新聞命中。

### 主要來源

- [法人：台積電法說會15日登場　有助支撐台股高檔整理 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1XODJFM2RLZlI4ay0weXl1c3NUSzNNTUYyLUwxb2xpeW1pZ0Naa1NvY1Jxbm9xRTVibk8zOGhFTFYxWlJhRFh5MTFiOWM4QllwNl9RZHRpVi13d9IBX0FVX3lxTE41YmpTZFVnNU95QWhrVDMtbk5JNXRDUVdpTlZZSkhuZG5weUQ5aWtJSEw1ZFhPOERHb0ZENDF4cGtTWWZSSUVOcGpXZkJseXNUYXlobFlUSXhkWWt4bzVr?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 09 Oct 2026 06:54:30 GMT
- [法人：台積電法說會15日登場有助支撐台股高檔整理| 證券 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE4wdm4zWkh6Y1piZG05bXJ2VTVFcGxoc3JDam84dWQzOGQzc3JGTWVGR2pTcWtUZUN1alZxcFJQQXBVLVIwaTBRUHJwRlFheV84dXRJR3R1UEZPbm1qVmc?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 09 Oct 2026 06:40:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel (INTC) Deepens AI Chip R And D Partnership - Simply Wall Street；Record Profits at Samsung and TSMC Say the AI Trade is Intact - TradingView；大陸全面推動「AI＋」！布局六大未來產業盲目投資將究責- 兩岸 - 工商時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | -8.70% | N/A | 104.70 | 114.68 | -8.70% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | 0.00 | -0.97% | +1.59% | 2,550.00 | 2,550.00 | 0.00% | 不適用 | 86.28 | 29.56 | 511.86B TWD / 54.65% | 2026-10-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +3.85% | +14.59% | 229.28 | 230.48 | -0.52% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | +17.83% | N/A | 608.10 | 620.68 | -2.03% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +18.84% | +8.75% | 535.07 | 535.07 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -2.38% | -4.29% | 361.54 | 446.77 | -19.08% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | +0.27% | +4.79% | 744.00 | 744.00 | 0.00% | 不適用 | 13.92 | 53.84 | 82.25B TWD / 45.66% | 2026-09-01 |
| 2454 聯發科 | 產業/供應鏈推估 | 0.00 | -9.20% | -5.82% | 4,690.00 | 4,920.00 | -4.67% | 不適用 | 60.69 | 77.46 | 55.40B TWD / 1.97% | 2026-10-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「TSMC」，共 1 篇新聞命中。 同時符合主題標籤：AI, advanced packaging, CoWoS, AI server。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel (INTC) Deepens AI Chip R And D Partnership - Simply Wall Street](https://news.google.com/rss/articles/CBMitwFBVV95cUxPMnFDbUxweFl2WmprMlB0ck1jbFo0OVJvaEQtWklMRl81ZGNtN0FJTGRTVzQwNmo2aGZPWDloU280dHlOVmFhdWo4MzFHNXc0S3hIbXh2VzB3Nzc3TnlwNjliekdDdXNycVhJb2JiVVBBUWZfQWlCRG92bkx4ZnluWW9ROWhyZ0NSdmFycU1hbHRBVGU0dnl4V3htQ3ZDZmhoR1BXMEhzbmtkeTdNUVZWaDlCYnc3LTTSAbwBQVVfeXFMTkVIbXRkblg2N3ZTNDdjQTFsR25hUENvOFRFWmkweFhzQWx0UV9KYlF1X3l0cWhnRldvWko3bG9tdUlFdFhCTnZFbXhKb044eW5obXVoaEZnaUxvUmlPRFhkX1lmclVuU1UzZkk0TnNMZGRsYUFnMUZHWU5Pb0VONnBJMnBIRTdGRndncTRmblhhbktJU25XTDNsRUFaV0VQZ2NaYk1LdjN6eFpjZF9UNC1FSlBtcnp1VzJKUlE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 09 Oct 2026 06:03:02 GMT
- [Record Profits at Samsung and TSMC Say the AI Trade is Intact - TradingView](https://news.google.com/rss/articles/CBMiuAFBVV95cUxONnZvTi1uaDNKSkZNVzVwMVBYRkYxTDNrQmRxZFFDaVZRMmczUzBVQUpWY0o3Y0M4eEpJZVBKNmgwT2lBZGQ5YTRMakgxYk9HU2NpbVFCQkZJSzhTRkxvNi1yUVJJQUg4WEt5WWlrUnhlR1VJSjZzN2I0ZEZXUjlyWUhTM2MtOEd4NzdHTk1DdngyQUk0Q2stTEU3MVNUSHNUb1RpRkVHOVBTZW5na0ZQWmNTODFCMHF5?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 09 Oct 2026 12:23:00 GMT
- [大陸全面推動「AI＋」！布局六大未來產業盲目投資將究責- 兩岸 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE41LWhURndFMUJPellfSmpNTkczMGVBSktWUDVvakFXYm9uX0RUWTFEQXRzR0VVNHE1bzN5dEo0dE1MLTFTZ3VsX0tBX1Jyc09JUXJSMUh3a1BudjlKeXBB?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 09 Oct 2026 10:54:00 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel (INTC) Deepens AI Chip R And D Partnership - Simply Wall Street；Intel Slides 3% as Chip Stocks Sell Off With Yields and Oil Higher; NVIDIA and AMD Slip - Yahoo Finance；AMD vs. Intel: Which Chip Stock Has More Upside From Here? - The Motley Fool

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | -8.70% | N/A | 104.70 | 114.68 | -8.70% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | +17.83% | N/A | 608.10 | 620.68 | -2.03% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +3.85% | +14.59% | 229.28 | 230.48 | -0.52% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -0.97% | +1.59% | 2,550.00 | 2,550.00 | 0.00% | 不適用 | 86.28 | 29.56 | 511.86B TWD / 54.65% | 2026-10-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | -3.28% | -8.67% | 147.50 | 164.50 | -10.33% | 不適用 | 6.68 | 22.18 | 25.35B TWD / 27.22% | 2026-10-01 |
| MU 美光 | 產業/供應鏈推估 | 0.00 | +5.97% | N/A | 1,029.00 | 1,035.84 | -0.66% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -5.56% | -9.97% | 1,609.46 | 2,335.00 | -31.07% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -2.38% | -4.29% | 361.54 | 446.77 | -19.08% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC、Intel」，共 4 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 3 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel (INTC) Deepens AI Chip R And D Partnership - Simply Wall Street](https://news.google.com/rss/articles/CBMitwFBVV95cUxPMnFDbUxweFl2WmprMlB0ck1jbFo0OVJvaEQtWklMRl81ZGNtN0FJTGRTVzQwNmo2aGZPWDloU280dHlOVmFhdWo4MzFHNXc0S3hIbXh2VzB3Nzc3TnlwNjliekdDdXNycVhJb2JiVVBBUWZfQWlCRG92bkx4ZnluWW9ROWhyZ0NSdmFycU1hbHRBVGU0dnl4V3htQ3ZDZmhoR1BXMEhzbmtkeTdNUVZWaDlCYnc3LTTSAbwBQVVfeXFMTkVIbXRkblg2N3ZTNDdjQTFsR25hUENvOFRFWmkweFhzQWx0UV9KYlF1X3l0cWhnRldvWko3bG9tdUlFdFhCTnZFbXhKb044eW5obXVoaEZnaUxvUmlPRFhkX1lmclVuU1UzZkk0TnNMZGRsYUFnMUZHWU5Pb0VONnBJMnBIRTdGRndncTRmblhhbktJU25XTDNsRUFaV0VQZ2NaYk1LdjN6eFpjZF9UNC1FSlBtcnp1VzJKUlE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 09 Oct 2026 06:03:02 GMT
- [Intel Slides 3% as Chip Stocks Sell Off With Yields and Oil Higher; NVIDIA and AMD Slip - Yahoo Finance](https://news.google.com/rss/articles/CBMilgFBVV95cUxPTDU2WU80ZHFCVUhacU5IWTlHYWVTR3RYeVQwMkN4Z0VKTnUwV0xUcC1SS1M2YkdTRV93eVlsNk1hRWZBcjAyOWZKNzdReG9BekprbHluV0hNLWplS08wQXJsUGFRbVN6dE1IWkRCR1RQMmpxSE01cnFvLXR6ZGRnMXFjTzR3TTRZY09WeGNoUWNPem4zMEE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 08 Oct 2026 14:05:43 GMT
- [AMD vs. Intel: Which Chip Stock Has More Upside From Here? - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxNTW90STZZbFdiQlVsRkJCN0hCNXJTMEl0UHd6QlJMNWotcy10MDJkUWlUYWZtWE9JZ3l1R1dzMm0tOE9fSFRLYkU0VFlFeFF3WS1DamlLWkVVZWlJbVphOTQxVFVUb3lqc3k1UUo0cjM2Mks3dTFoVmM2bTBLSWtaTnFoaUVCa0wwTnpIbjRHbDhZclZDcWFnMw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 08 Oct 2026 17:30:00 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：散熱廠Q3營收皆創高，Q4盼續成長 - 台視全球資訊網；奇鋐 Q3 營收創高，外資看好液冷動能延續至 2027 年 - TechNews 科技新報；焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.28 | -4.04% | -1.99% | 3,440.00 | 3,440.00 | 0.00% | 背離 | 75.13 | 45.85 | 21.02B TWD / 44.92% | 2026-10-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱、奇鋐」，共 4 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：跌停, 成長, 創高。

### 主要來源

- [散熱廠Q3營收皆創高，Q4盼續成長 - 台視全球資訊網](https://news.google.com/rss/articles/CBMiqwFBVV95cUxPOGFiQlctcjF4Qi1KQ25ZNjk2RXpudHljWG9IekhkQ09zQ2k3SGhCeWxvRXBJRnZXQm0ydXlBZVc5Q0FZbWR2Rl9DYjN5YXpDbjlabkxJQ3VWVzduTVU0WllpMlFPbXVMQUlIbUdERFBJQWljYWpsUjByUnNieXM0NmFpTlNyYUh5MjJhRjBvX2tGMmxfTUxwcjlhRnZfbU5rU0ttZ01iRzExVlU?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 08 Oct 2026 03:50:53 GMT
- [奇鋐 Q3 營收創高，外資看好液冷動能延續至 2027 年 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiXEFVX3lxTE5wTkNlcmlzTGd5cURrSWxidEZVY2ZmMXlmQXN5dEJnbGd0cndMWG1OOWM1cU96QXJZUXQxc0kzc1IxOFpRdVZKd3F3M3lBUVJteG9LZEJ1eXluamho?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 08 Oct 2026 02:09:35 GMT
- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 09 Oct 2026 02:49:04 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：個股動態報導內容-9E94BE75-F504-4FEC-9C2D-8704A8E703C2 - MoneyDJ理財網；個股動態報導內容-13BFA797-BD5C-4F4C-B41C-2F575E2353A3 - MoneyDJ理財網；個股動態報導內容-E2B6ACA2-228B-484B-B7EB-86835838D08A - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-9E94BE75-F504-4FEC-9C2D-8704A8E703C2 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilAFBVV95cUxNVWFMdC1qSXlzcFVMcmJMZlNsZnlBMHpCdjZxdGw3VFc0SmJ5aElDbElFSVRaVURDTDZvSW15cVNHNDI5WEl5UldudkdISFhSVnIzRDN1Zy02S3VRbGpkMnRjaHVNUldnQno0bDMyS0NIcHZiZ2hQdXlFbE9oX21IYWFUQm1zMW1qMjJYMWd4YnpLNURj?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 09 Oct 2026 10:28:33 GMT
- [個股動態報導內容-13BFA797-BD5C-4F4C-B41C-2F575E2353A3 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilAFBVV95cUxPYTdvTW9JUWdJeVppMTdKQ05HNkF6V1J2WVVQejRpWE5mOFo4Q0xYOE8tTlBTNHF2MW9pQWdNekp2TVhsQVd5amdHaEt2cjBwNVpsY21ZQkRJdkdjanozVFpNaFJWblVVM294TTdWTVBXckVuYUgzdXI2aWpJdXV1SjFjQk5pYWdPMEpsWmh0MXkzZ2Jt?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 09 Oct 2026 10:43:37 GMT
- [個股動態報導內容-E2B6ACA2-228B-484B-B7EB-86835838D08A - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilAFBVV95cUxNd2tIdVdVb2NmNjBhUGlpNW9NeTQ0M3BLVEZrNHdtMUk0ZlRlRVdBV1FkZ1NxUW1CTnFZdzZUd0JfLVNNUHhkckZodEhuZGFxSkh5dXUtYXB2dkNUUkZQaFZDVnI3RnZoSTlPZUE1VFJZYjNKV3B0YWs1am9wUlNaMnZFNXVDd2xpSXR1T0lCU0VwZVhh?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 09 Oct 2026 05:06:20 GMT

## 新興題材：2場法說

摘要：新興題材：2場法說 相關新聞集中在：台股5萬點只是開始還是末升段尾聲？朱成志：2場法說會判多空 - 經濟日報；台股5萬點只是開始還是末升段尾聲？朱成志：2場法說會判多空 | 市場焦點 | 證券 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股5萬點只是開始還是末升段尾聲？朱成志：2場法說會判多空 - 經濟日報](https://news.google.com/rss/articles/CBMiggFBVV95cUxOdDVmMklXUlVnWmhOOHY5b0pWN01aZHZ2bndBSlVUdmVkRXNMb1BjZFNzREF0RmxyVmhiX1hrWE9ZcXUzVzRoajhIOXBfdlNiZEpmdFN5U0lGclQ5WkVvdHlJY2d6TUdkYmhZVmtDSUY3Yzh0bnppVlR2RU1oRW5qVUFn0gFfQVVfeXFMTVJ5S2p1RzhNZUNleHRhZ3F3cVB1Y3JHMi1hZzhib2VjYm5JTVN3ZzMtR1VMOW5HLUNFY3JsTS1MS3BJbmRFTW1JM0JQck9YU0xJUkJrS3ZfZ3lFSmQ5N3c?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 08 Oct 2026 23:00:00 GMT
- [台股5萬點只是開始還是末升段尾聲？朱成志：2場法說會判多空 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9iaUxWazFTRlJGdElKMlN1TlN4Yy0tbWNrNkFqaDhlVXgzM1dHcHdLdXVybF9fdV8tLUk0eDZIaHJQbFJDcWlJblpScS1XQmJIWkRTakY4eGtmUQ?oc=5) - Google News source discovery | 經濟日報 money Thu, 08 Oct 2026 23:00:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
