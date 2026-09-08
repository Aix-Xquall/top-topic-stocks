# 每日股市熱門話題分析 - 2026-09-09

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **綜合市場情緒**｜中性｜熱度 35｜市場確認 80.05｜同向 1/1
2. **記憶體與 HBM 供應鏈**｜正向｜熱度 8｜市場確認 51.85｜同向 3/5
3. **半導體與晶片供應鏈**｜中性｜熱度 13｜市場確認 52.77｜同向 5/8
4. **散熱與液冷供應鏈**｜正向｜熱度 2｜市場確認 52.98｜同向 1/2
5. **利率與成長股估值**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.28（樣本 24）
- 5日相關係數：-0.12（樣本 16）
- 同向比例：13/24

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 綜合市場情緒 | 80.05 | 1/1 | 0 | +3.35% | +1.23% |
| 記憶體與 HBM 供應鏈 | 51.85 | 3/5 | 2 | +3.28% | +8.92% |
| 半導體與晶片供應鏈 | 52.77 | 5/8 | 3 | +3.01% | +0.99% |
| 散熱與液冷供應鏈 | 52.98 | 1/2 | 0 | +6.00% | +1.62% |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：OpenAI | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 17.73 | 3/8 | 5 | -2.84% | -0.25% |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價呈負相關；應檢查正負向詞庫，並降低新聞直接提及但股價背離的權重。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-08-27 | 0.38 | 0.11 | +54.55% | 11 |
| 2026-08-28 | 0.14 | 0.12 | +56.25% | 16 |
| 2026-08-29 | -0.10 | -0.01 | +40.00% | 10 |
| 2026-08-30 | -0.52 | -0.04 | +23.08% | 13 |
| 2026-08-31 | -0.41 | 0.29 | +40.00% | 10 |
| 2026-09-01 | N/A | N/A | +50.00% | 2 |
| 2026-09-02 | -0.29 | 0.24 | +75.00% | 12 |
| 2026-09-03 | 0.10 | -0.10 | +54.55% | 11 |
| 2026-09-04 | -0.08 | -0.08 | +28.57% | 7 |
| 2026-09-05 | 0.13 | 0.34 | +54.17% | 24 |
| 2026-09-06 | 0.19 | 0.43 | +50.00% | 24 |
| 2026-09-07 | -0.15 | -0.09 | +53.33% | 15 |
| 2026-09-08 | -0.07 | 0.18 | +57.89% | 19 |
| 2026-09-09 | -0.28 | -0.12 | +54.17% | 24 |

## 歷史回測摘要

- 回測日期：2026-09-09
- 近5日 3日相關：-0.06
- 近5日 5日相關：-0.10
- 同向比例：+60.00%
- 權重狀態：已調整

- 方向準確度：+60.00%
- 信心排序準確度：-0.06
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

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股離新高僅咫尺之遙 分析師曝賣壓竟是來自這些人 - 經濟日報；台股走勢 緊盯三大指標 - 經濟日報；台股 ETF 夯規模躍進 整體達7.8兆元 領先大盤衝高 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | +0.56 | +3.35% | +1.23% | 2,470.00 | 2,470.00 | 0.00% | 同向 | 86.28 | 28.63 | 467.58B TWD / 44.69% | 2026-08-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 3 篇新聞命中。 方向判斷命中詞：漲停。

### 主要來源

- [台股離新高僅咫尺之遙 分析師曝賣壓竟是來自這些人 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9DSk04OWh3MmtfbktBZTJ6RS1KTEV6YUNJTUIydnQ3QTFUb1dZSkktcG1CLTdSaGJLYTdnUXFYMVMxQk9Mbk1Ta0FkWHhHV3Y3UUhaYkRvR1F6d9IBX0FVX3lxTE85RjhvTTNKVEdTQVRRTVRpZHlkcEdwdHVUU3RIZGFrVzNyUC02Z2t5QkgxYnNEUTFYVmdtZWF4dzkxM21kRVJJYWZuMjhRSll4RFdTMVgzZVZPOS01RDdj?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 07 Sep 2026 09:00:00 GMT
- [台股走勢 緊盯三大指標 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxNOFZ6TXpoRzRKeTBXMUdKa19IWUI0OUlnaXJhS2NHZ0RSV1lBM1duaGk4Zy1hTmJnWDFpWWlvMGJWdm5LZEtmTC1EUWlzckU1NHgtaVZBUkJlS0ZnVWw3bDJiN3JDZ2w2N0NiZ2R1MHVELTJuOHliWGdqZk5YTGIyUdIBX0FVX3lxTE1qM1BUcTdtQWQtS2FfQXVCem1XOEFvaHBhbjJTcFU5OWd6S2FKalowTVgwVHBFLTd3eUZ2UjVMYS1CQWJ5TmRUaEZIWTQtcFpmUFBxUG9mczRDUkVXLTNB?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 08 Sep 2026 17:36:21 GMT
- [台股 ETF 夯規模躍進 整體達7.8兆元 領先大盤衝高 - 經濟日報](https://news.google.com/rss/articles/CBMidEFVX3lxTE9YWFlsU0RsYnI3cDF4VTZJdk9VSUp0SjZMOWxrcE9ud0JUSHVKdVJsNHVSRk5MRm54amxKTHNKUXJjR0lCa2lYckc5cTNRdGl6dHdTcGJ4MWtacl9wOVlxNm43TGtPbWd5ZjNxWVB4VmlIZ0xK0gFfQVVfeXFMTTQxT2NITmRHRVpzd2Zyc3lidVhleDdJdW1Nbm5MMUpTTDhoWC1VUjBSd3Rlb0FpU2tiaXVpVGE2WEt5azlVY2VIVGRIN1FzOThkVmd1c2w4dzE5NmxoWmc?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 08 Sep 2026 15:33:49 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：US Stocks Fall as Dow Drops 600 Points, Philadelphia Semiconductor Index Bucks Trend Up 1.3%; Semiconductor Stocks Strengthen, Intel Rises 9%, SK Hynix Gains Nearly 5% - tradingkey.com；INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits；Micron and Sandisk Face a New China Threat -- 1 Has a Much Bigger Problem - Yahoo Finance

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.57 | +3.01% | N/A | 1,000.26 | 1,016.59 | -1.61% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.57 | +11.88% | +10.93% | 1,737.99 | 2,335.00 | -25.57% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.24 | -8.90% | N/A | 104.47 | 114.68 | -8.90% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.21 | -2.01% | N/A | 505.74 | 516.10 | -2.01% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.03 | +12.44% | +6.91% | 225.73 | 230.36 | -2.01% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron」，共 4 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs, 升級。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk、SNDK」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel、INTC」，共 2 篇新聞命中。 方向判斷命中詞：fall, rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [US Stocks Fall as Dow Drops 600 Points, Philadelphia Semiconductor Index Bucks Trend Up 1.3%; Semiconductor Stocks Strengthen, Intel Rises 9%, SK Hynix Gains Nearly 5% - tradingkey.com](https://news.google.com/rss/articles/CBMi2AFBVV95cUxNLW13YmdESnNacDhCVWtpeGk3UXM4d2cwSTZwVExEbTRyZGJBYjczVnJqRU1VSGtBemROMGZlSTBoSzYxYU8ySjhjeVVoSEFFcVdGTGZkLXotcW9pVnVfVUJXRWVhX1Q1cGZuNzJlbTNPN2RUWEJYOGY1TWpNSWtScWt0OFF3WWxwbTVYQzVNYmR5ZWJhTnZjWGVkVDNYUmVvaWVqZ3JiVDVWMzd0a1pGNFlEMVFCZExlZmhxRWpveERMV09PY0tPMHlnX1BuWlF5blM3UkQ5MjQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 08 Sep 2026 20:19:38 GMT
- [INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits](https://news.google.com/rss/articles/CBMi0AFBVV95cUxOWm5KdEIwSXpyY191UEhDa1V6NVpWa01UbmpJeWRIV0ttT080TmpDNEhISW5TWkQwUzBVYzBqSHJPWXRVNVJCampoWWRlYmhKVkhIeHBJLS0wLW5Ua09GQnRORXpFcW5qTEJkcnJGcW55aU5rOFVOLUFMbjRPZEpWT3A2ZllucnM0SU9JNEdrNUwyc3V2WHAtNFk3VHl4R1F6SkZRMFpleEE2Zl9MdW4tSEpMMnFGZ2hQZURWQ3B1WDlPR1BhRjJELVN5ODJWYVR3?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 07 Sep 2026 06:13:53 GMT
- [Micron and Sandisk Face a New China Threat -- 1 Has a Much Bigger Problem - Yahoo Finance](https://news.google.com/rss/articles/CBMingFBVV95cUxONTZqY1h1QlIxR3dvaUpBbV80UllhZkk3Qk92YUtnc281X0pBWmJnTXVzNEJkMVozOVR5R3dsMkpSM2JzOThoQTJtM251UVIxc0Q5ZDBqbHpJakZ3Slo0ZFhIUV96czI4eFh5eDFRRDZmUVdmeldQbEhyQ1BtV2ZBdWk3SlVnNmM4OVNWSnpNazRkcWhkNk0xLVFmMjBtQQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 08 Sep 2026 16:00:07 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel Leads Chip Stocks Rally as Qualcomm, AMD and Broadcom Stocks Jump - Yahoo Finance；Intel Climbs 5% on High-NA EUV Production Lead, ASML and Taiwan Semiconductor Advance 3% - 24/7 Wall St.；人力銀行報告：半導體操作技術維修職缺今年6成不限科系| 產經 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.28 | -8.90% | N/A | 104.47 | 114.68 | -8.90% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | +0.49 | +3.35% | +1.23% | 2,470.00 | 2,470.00 | 0.00% | 同向 | 86.28 | 28.63 | 467.58B TWD / 44.69% | 2026-08-01 |
| AMD 超微 | 新聞直接提及 | +0.23 | -2.01% | N/A | 505.74 | 516.10 | -2.01% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | +0.23 | -5.32% | -17.51% | 368.56 | 446.77 | -17.51% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2303 聯電 | 產業/供應鏈推估 | +0.05 | +9.60% | +3.40% | 137.00 | 164.50 | -16.72% | 同向 | 6.68 | 20.60 | 25.04B TWD / 30.71% | 2026-09-01 |
| NVDA 輝達 | 產業/供應鏈推估 | +0.04 | +12.44% | +6.91% | 225.73 | 230.36 | -2.01% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | +0.04 | +3.01% | N/A | 1,000.26 | 1,016.59 | -1.61% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.04 | +11.88% | +10.93% | 1,737.99 | 2,335.00 | -25.57% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「Taiwan Semiconductor」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip, foundry。 方向判斷命中詞：rally。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Leads Chip Stocks Rally as Qualcomm, AMD and Broadcom Stocks Jump - Yahoo Finance](https://news.google.com/rss/articles/CBMimgFBVV95cUxPQTFyNVlvZ1o1eUw5YVFLTTVrR1FyR1czclRiV3dPR3FONmxCZlc2UFUtS3dFUTIzNlRLa3lxeHdKOXpvZGdJMUxWMXp4VjJBWWZnNXltOU54czR3LWlJd19zaHFQQkN4ZWg0dkpRS2Z2QkpBQjdWbFFCV0U1QjZyWXMzclVDWmJ4NWhxdWtwdU9QUUNwMkM2WnV3?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 08 Sep 2026 20:49:45 GMT
- [Intel Climbs 5% on High-NA EUV Production Lead, ASML and Taiwan Semiconductor Advance 3% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiyAFBVV95cUxQeVdjXzlsZ2hoZGNKMWdYM04xbEVRTDNkOEotUHU3SHdYN2RuSHBxVWUyVDl2S01zNnJQd0psRGttX0toSU5lQlZ5Y3cxYmVZOFRhc0REUTdIYkx3bXdSZ1cwOVNWZEg4azE0cUpBNFFqZkp2bE5Gcnc3c3VBeVp2NDJqVEV3Q0RVTDBka1ZmRVBmV2VkRHpiY3lyb1A2UUlrUWhVTUJUMFRvMXF2dWJ4R3RlZFpkcjVKU29mdTFkcFgwYUtpUlYtMQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 08 Sep 2026 13:32:00 GMT
- [人力銀行報告：半導體操作技術維修職缺今年6成不限科系| 產經 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTFBmSkdoNWhtOTVndkFHSlpTRkF4aC1jMzVMdzVlN01VSERjdE5ibWNCbzl3Wk1zMUdPaG5aM043aVlBbk04SVNuVGVXQXRwTVlqdEdyT2swcXIxNVRLd1E?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 08 Sep 2026 04:10:00 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：輝達放量在即！「這散熱大廠」吃同業良率低紅利 目標價上看4500元 - 三立新聞；從精密沖壓做到AI高階散熱！它切入Rubin、Trainium3　法人一路上修EPS - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.38 | -0.45% | -3.67% | 3,285.00 | 3,570.00 | -7.98% | 未明確 | 75.13 | 43.79 | 19.48B TWD / 54.34% | 2026-09-01 |
| NVDA 輝達 | 新聞直接提及 | +0.42 | +12.44% | +6.91% | 225.73 | 230.36 | -2.01% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 2 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：上修, 放量。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：放量。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [輝達放量在即！「這散熱大廠」吃同業良率低紅利 目標價上看4500元 - 三立新聞](https://news.google.com/rss/articles/CBMiS0FVX3lxTFBSeGhzZkREcTZTWjFOVEZuSWRUY1Fwc2hZWlZKRFFMT09JWUo5RTNRdnYxNUFlbDBXMzdoTVJsSnZvQnFLQkZTZVVWcw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 07 Sep 2026 17:37:52 GMT
- [從精密沖壓做到AI高階散熱！它切入Rubin、Trainium3　法人一路上修EPS - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9zREF2QXpCNXB4SWxlR3NaTklRem8zT09HMUxTRjRUcl9ocjU0ZG9tTVh3aTBOd01fTHZlSkd4Z1NqY25hQUtDQ1ZDanpvWlJEYmg0RTIyR1R0UdIBX0FVX3lxTE8tWXAtRHRTVno3b0c5aHpoalRJWmZhOWR6R1hHVHM1RmZDSjV6MDlkNE56M2p2RlR1SGttZTVHUl9rN1Ata2dqLXFDVjBKQUtnVHp5dGpXRk9ZdXFKNkFN?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 07 Sep 2026 15:00:00 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：French AI company Mistral hits $24 billion valuation in funding round - Reuters；連21周上調！不甩高通膨+升息預期 美股獲利動能5年來最強 - Yahoo股市

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +9.71% | +0.39% | 493.95 | 507.29 | -2.63% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [French AI company Mistral hits $24 billion valuation in funding round - Reuters](https://news.google.com/rss/articles/CBMitAFBVV95cUxNSzZndFBZYk1SQ19xOVJYSXR1ZHdKa2p2a0RSYTVfeWVicHRLZ2JOdG5zc3hibHhJYWh1V3pIVEhDaV9Wc2xQV2RlYkNkTEZJSDV2V1V6aGloYXVPcFNtMHlCU1ZsTnR5UEZTNTI5WTExa1A4Vy0xZjN4ZFE3TVUzN2tUWFNnc3V2aXNBRldFWXlGYnFwcGtGVkFtRE9HTDktVUhJR09HVUwtdHZmNHdjWGZCTkw?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 08 Sep 2026 05:02:00 GMT
- [連21周上調！不甩高通膨+升息預期 美股獲利動能5年來最強 - Yahoo股市](https://news.google.com/rss/articles/CBMi9wJBVV95cUxQczB3VUZWWVQyVkVnMGViTTRkWk5NdUJoaHNyQUZObFZfdGdOWmJsTzJtRjdweHJvbkFtS2c2U0hpblRHQ3JDSGVJbWJtUGlUWWphTElqYVd6YUNVSkZlcVAzdmdwWF85cnEtdFlFT09TY0xkeG85NGxvQkJidS1ZeWRYWFloU211czVJTkFzMnFtUEFLWkFla3dzaVc0S1ozcGJ2RDlZaUs1TVh4SUhzRUtEcXN3MXBWaHVTQ0U1XzRiMEN4YXhaODJiSE1NMG5KV21lU2RIQ2d4Tl9JbTUyUVRjLUNVYWRGdVBkOUJYZ1NrSk1CaUVVcEhvTlF3b3NWZzhhWWFNMG1oWXJJVk9xTW95NTBvd3NDVWJ1VVVVb3JyczRzak5sdjVwSVJiQ1JDQlJEMzRjRWNPYWl0ZmctaUZSNjNQalB6ZC16akYwcUMyRXJpc01JVmpHY3V0bmxBVkt6QWtna181SE9VbmNBckhVSFFOMlk?oc=5) - Google News source discovery | Yahoo 奇摩股市 Tue, 08 Sep 2026 19:30:04 GMT

## 新興題材：OpenAI

摘要：新興題材：OpenAI 相關新聞集中在：OpenAI, New York Times case tees up key test of AI training under copyright law - Reuters；Cramer says these 2 stocks are big winners from OpenAI's new model release - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 新聞直接提及 | 0.00 | +9.71% | +0.39% | 493.95 | 507.29 | -2.63% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：新聞直接提及「OpenAI」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [OpenAI, New York Times case tees up key test of AI training under copyright law - Reuters](https://news.google.com/rss/articles/CBMixwFBVV95cUxPNm9Dck5iY3gydVpGQlBFVU5mcF9oa0Qzd0Y5OWN4ZjRVb2huWDBWeFVUeXhQejZZTkdUd3JfZDhZN095X21HODJSdnJ4MVhyMjZQWjVuSXJrM1dMN3dZdkcwMG1NMnB0V05ENDhoN2hKakZLZDExczNYNUlEXzNFcXVQTUdNMDI0THVKYWxuc3dheVBMNUpqdGNHcENOMlpyLUhPVnFTM1JYZURNOWM2dnktUGo1Q3JtdlBpb29uUF9jNVRlVnlR?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 08 Sep 2026 16:05:09 GMT
- [Cramer says these 2 stocks are big winners from OpenAI's new model release - CNBC](https://news.google.com/rss/articles/CBMisAFBVV95cUxNLTR6TnVtVFNLRDBzY0tNTEhUZnF3aS01NkdMcF9tYWFQTDdIaF9qZmp5dHZHem5fMjdhUFN1ZmRfYUtqS2VJR3Q3WkNRcWFLM3kxejNMMXc4Vmx3UlVhd3RVT0N6bEtZQ3JGNjBYTXI4R1JuQ01XZzF4S1JndWp4ZW5PSWs4NV9SS0FaMmU4bS1hdWFxSHZWQ3ZKWkgxQzZpc0xodFJxZnVzTlJwY0tUTg?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 08 Sep 2026 16:41:42 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：AI 淪恐怖份子利器？美情報界與專家齊示警：生物安全防線已全面落後 - TechNews 科技新報；法國新創 Phagos 用 AI 煉「噬菌體」抗生素，2 個月完成傳統 10 年研發 - TechNews 科技新報；Meta launches AI agent that can access other apps to send emails, make payments - Reuters

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | -0.08 | -8.90% | N/A | 104.47 | 114.68 | -8.90% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | -0.03 | +12.44% | +6.91% | 225.73 | 230.36 | -2.01% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | -0.06 | -2.01% | N/A | 505.74 | 516.10 | -2.01% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.03 | +3.35% | +1.23% | 2,470.00 | 2,470.00 | 0.00% | 背離 | 86.28 | 28.63 | 467.58B TWD / 44.69% | 2026-08-01 |
| MSFT 微軟 | 產業/供應鏈推估 | -0.02 | +9.71% | +0.39% | 493.95 | 507.29 | -2.63% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -5.32% | -17.51% | 368.56 | 446.77 | -17.51% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.02 | +4.92% | +1.31% | 618.00 | 680.00 | -9.12% | 背離 | 13.92 | 44.72 | 73.78B TWD / 43.15% | 2026-08-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.02 | +8.53% | +9.15% | 4,710.00 | 4,710.00 | 0.00% | 背離 | 60.69 | 77.79 | 48.47B TWD / 12.16% | 2026-08-01 |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：falls, 恐。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：falls, 恐。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：falls, 恐。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AI 淪恐怖份子利器？美情報界與專家齊示警：生物安全防線已全面落後 - TechNews 科技新報](https://news.google.com/rss/articles/CBMigwFBVV95cUxPWDNUTnFhSThMeUNmUTN2YlZUV3AxOFZqdU94Y0dyMkFGRlJ5Zl9lODBQM0FIMS1UV1kyeTJsRjJQRHAtUzBtNUVfWnB2dzQxWDV4Z3BfUkpUQk1CZHU2Z01aZnhSMDZmeGVmVFp2YWJ5bkdjdjJwZjFTTkFLVTFXVGdYQQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 08 Sep 2026 23:43:22 GMT
- [法國新創 Phagos 用 AI 煉「噬菌體」抗生素，2 個月完成傳統 10 年研發 - TechNews 科技新報](https://news.google.com/rss/articles/CBMimAFBVV95cUxNQnlsbVgwVm1xRXJZZUpERlVtbzNmczJmaEpObDVTMGhobXNaV211cFlwUzZhcHItQ09CVzVGWTA5clNORGxMdklicVc4T0ExWFRQTlZZTWphVHYweUhSRDlHTGhUSjlldVZmY1lwSXFCSXgxTmJocDdiZEp4V2xncUc2VmNMSDhiSXVxQVRZYTRIMGw4OE1zNw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 08 Sep 2026 23:22:32 GMT
- [Meta launches AI agent that can access other apps to send emails, make payments - Reuters](https://news.google.com/rss/articles/CBMivAFBVV95cUxQS195TVZPeEJJbzNYTEZ0dnI4WGxOWXF2ZlRmbDEyU1VtWnFsd012VXVDd01mRHY3Y3lDOW9pRXRYSXR6R2NqYVM3R0xwMURjZElSZHVkckZidjNoWTh5OWlNWkZGUGJpWnpDSUhUOUxBUEZDTVpwZjFXemxIdTlvanpSMXF2MXo1UkNtN2UtZVdfX3J2ZTdCekREbUxkaFo1MVpLakxOT0ZaeUVoMlhlb2E0Y0dfV2g0bXRNbw?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 08 Sep 2026 21:29:41 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：台股今年來漲幅反超韓國！ 居亞股之首- 新聞 - MoneyDJ；《台股盤後》台積難撐盤、量縮收跌220點，險守47K-新聞內容-基金 - MoneyDJ；國票證券：台股短線偏多看待- 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股今年來漲幅反超韓國！ 居亞股之首- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNaGlzaFlRR3Byci00cnNuSHZ1Tm5TVDlsNW1HaXJEVW1zOTZNV3hzcEJhMlBYV2pfOG1iMmFYRnEwaGViWms3RzkyM05YRUhMdF92LWlkZVBLdnFJamROd3p3cFlTRXpZcDRuMTJlZUJYMjBvRTBGS3Z2cGRWZDVGdlljd1JJS2p3TkRzRkUzWmc4dw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 08 Sep 2026 04:09:00 GMT
- [《台股盤後》台積難撐盤、量縮收跌220點，險守47K-新聞內容-基金 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxNMkFEZm5YaTBVV2M5cm1JeHZnTWo2SjItclhCdGlIUVRDNlk3M2daN1VKZnpacVdWeC1yc1MzUVNqMmstTjlRVTllYWhKRk81T0VnV01kMHU5d0N1dlN3NTZJUXJYeUVsN2hsZE13dzd0R1JWZ2JLRG1NOVFjTTZDdWFyYXhyV2VaTGZwYzd0OUc?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 08 Sep 2026 08:04:00 GMT
- [國票證券：台股短線偏多看待- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPeldTNjdyX21jOTlTZGMxZk1OTFlJa3QtSXUyV1dtZFc4Z2ZRS3ZxTG9uWlhXampBYlpWZnhYRC10Vm9yU1N4djI5M0NJR2NNbWRaUzdheGN0WWhfYkNVYUNXZ3RMOUR5b284YXh0cUViblp6X29WbjJjNnYxQkd5VEMxY05GcFBlS0l1X3BvZHEtUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 08 Sep 2026 00:39:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
