# 每日股市熱門話題分析 - 2026-08-13

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **AI 伺服器與資料中心**｜正向｜熱度 11｜市場確認 99.25｜同向 6/6
2. **記憶體與 HBM 供應鏈**｜正向｜熱度 8｜市場確認 100.00｜同向 1/1
3. **半導體與晶片供應鏈**｜中性｜熱度 8｜市場確認 N/A｜同向 0/0
4. **新興題材：StockStory**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0
5. **綜合市場情緒**｜正向｜熱度 42｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.72（樣本 7）
- 5日相關係數：0.24（樣本 7）
- 同向比例：7/7

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| AI 伺服器與資料中心 | 99.25 | 6/6 | 0 | +9.75% | +2.44% |
| 記憶體與 HBM 供應鏈 | 100.00 | 1/1 | 0 | +10.90% | -0.46% |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：StockStory | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：AI需求 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：CoreWeave | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-07-31 | 0.10 | -0.10 | +46.15% | 13 |
| 2026-08-01 | 0.38 | 0.25 | +54.55% | 11 |
| 2026-08-02 | 0.06 | -0.21 | +33.33% | 9 |
| 2026-08-03 | 0.35 | -0.49 | +60.00% | 5 |
| 2026-08-04 | 0.05 | -0.08 | +46.15% | 13 |
| 2026-08-05 | -0.39 | 0.44 | +64.29% | 14 |
| 2026-08-06 | 0.07 | 0.33 | +50.00% | 12 |
| 2026-08-07 | -0.22 | -0.17 | +50.00% | 8 |
| 2026-08-08 | 0.72 | 0.45 | +62.50% | 16 |
| 2026-08-09 | -0.39 | 0.46 | +71.43% | 7 |
| 2026-08-10 | -0.09 | 0.74 | +71.43% | 7 |
| 2026-08-11 | 0.57 | -0.18 | +54.55% | 11 |
| 2026-08-12 | 0.52 | -0.47 | +87.50% | 8 |
| 2026-08-13 | 0.72 | 0.24 | +100.00% | 7 |

## 歷史回測摘要

- 回測日期：2026-08-13
- 近5日 3日相關：0.10
- 近5日 5日相關：-0.08
- 同向比例：+66.67%
- 權重狀態：已調整

- 方向準確度：+66.67%
- 信心排序準確度：0.10
- 診斷：低相關

調整原因：近 5 日信心分數與股價關係偏低，提高價格確認，降低寬題材推估。；關鍵詞×公司後續樣本有效 5 筆，未達 30 筆，不調整樣本權重

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

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel AI Chip Stock Analysis 2026: INTC's $20B Bet on Artificial Intelligence - Intellectia AI；AMD, Intel, and NVIDIA All Rally Wednesday After Series of Blockbuster AI Earnings Reports - 24/7 Wall St.；中國每 36 秒新增一部 AI 短劇，生產加速但賺錢更難 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.57 | N/A | N/A | 100.95 | 114.68 | -11.97% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.54 | +11.99% | +12.29% | 224.09 | 224.09 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.53 | N/A | N/A | 482.93 | 516.10 | -6.43% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 新聞直接提及 | +0.50 | +25.38% | -2.81% | 492.43 | 506.69 | -2.81% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.06 | +1.90% | +0.42% | 2,415.00 | 2,425.00 | -0.41% | 同向 | 74.39 | 32.47 | 467.58B TWD / 44.69% | 2026-08-01 |
| AVGO 博通 | 產業/供應鏈推估 | +0.04 | +10.14% | -0.33% | 416.05 | 446.77 | -6.88% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.04 | +6.15% | +4.72% | 621.00 | 680.00 | -8.68% | 同向 | 13.92 | 44.93 | 73.78B TWD / 43.15% | 2026-08-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.04 | +2.95% | +0.37% | 4,015.00 | 4,310.00 | -6.84% | 同向 | 60.69 | 66.31 | 48.47B TWD / 12.16% | 2026-08-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC、Intel」，共 2 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel AI Chip Stock Analysis 2026: INTC's $20B Bet on Artificial Intelligence - Intellectia AI](https://news.google.com/rss/articles/CBMibkFVX3lxTE9ITWpmLTQ2dndFMWZlWXBtdEd1QTRWbVpwYnRRbUh0b2l4R21lSkdLd2pEdlFLeVFXdjBGRXBuamw1b05qRUJ0UGdfZEtDVWdycDlNQlZISmpjdXEtOGFTcVJSeXYwR0p2akJLUUtn?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 12 Aug 2026 17:55:48 GMT
- [AMD, Intel, and NVIDIA All Rally Wednesday After Series of Blockbuster AI Earnings Reports - 24/7 Wall St.](https://news.google.com/rss/articles/CBMizAFBVV95cUxNaFZPc1BKRnVYdEpmQ2NweDFpeDFKTU9aaVhYWW1uYzFBdXJLMTZEMmtEaHc0TGdYUTAydjZuZXI4VUJoRTMydGlhWHotU09wQkU1elZHSVJ2SnRPRHVpYkRyRExDQlhzUTJZdEVvTVphWXlSMkR5OU1jZ28wcFV3VGlRNlZ6elRXNGxoQUJheThWSlVmV19DZ0dDVy1pWGd3Slg0X3RtSHRKSG1MaFVubzhmMXdDNGZKMWxEV0J1MjdJVmtDM3IwYkhackw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 12 Aug 2026 22:21:27 GMT
- [中國每 36 秒新增一部 AI 短劇，生產加速但賺錢更難 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiowFBVV95cUxNbWVtMmZPQ05aRzRkWW9EZFc4RGtJWnlTbktoR3hZZFkteVhHNXYzVXBHd3V4bEZ4ejd3VFZuY0k4WHZZalpmLVZsTXVWS3o5Y0RyaGRXVjVmSWE5TFVOckFTTjJKbkM5ajV2bUNGZWNpUlZDaHVkRXNtRlNMdExFUkx6R0lyYWFYaFpPRjdaQTZyZE1aOUJRTDBhOFZPZElqLTYw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 11 Aug 2026 10:09:13 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：MU, INTC, SNDK: Chip Stocks Rally After-Hours On AMD’s Blowout Report - Stocktwits；Memory Stocks Rally Wednesday: SK Hynix, SanDisk, Micron All Jump. Here’s Why - 24/7 Wall St.；SK Hynix and SanDisk Climb 8%, Western Digital Gains 4% as Memory Shortage Deepens - AOL.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.48 | N/A | N/A | 911.29 | 971.00 | -6.15% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.48 | +10.90% | -0.46% | 1,344.29 | 2,335.00 | -42.43% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.36 | N/A | N/A | 482.93 | 516.10 | -6.43% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.36 | N/A | N/A | 100.95 | 114.68 | -11.97% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +11.99% | +12.29% | 224.09 | 224.09 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron、memory」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally, shortage。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK、SanDisk」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：rally, shortage。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [MU, INTC, SNDK: Chip Stocks Rally After-Hours On AMD’s Blowout Report - Stocktwits](https://news.google.com/rss/articles/CBMiygFBVV95cUxPeVlYaXJjQjNtTkNRQUxQTHhaLUFMbE80Uy1MeDBpV0FPdkg2SHRLdkdfVUpXM1NrNWhZSVZQQ01sa0o4T1hKdzF1clBFRlRWUmMwWGxQTDNVVFBpOVhObUc2MXpBeXBOZ0p3R0w5NGRNOHB4X0ZIXzhlT0NMbmhzc1RtdmJRTWhlRUhKSHpyVnpaU0VGMlJyU2tDcmdkTG1hWVJJbmtTVDREbzFfWDB4bjhuTGswN3lmdkdHQzY1dzFOVU41VGlBNlZn?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 11 Aug 2026 21:51:02 GMT
- [Memory Stocks Rally Wednesday: SK Hynix, SanDisk, Micron All Jump. Here’s Why - 24/7 Wall St.](https://news.google.com/rss/articles/CBMitwFBVV95cUxOMnJYc2tPUENlU3pTMmtBLVVuUVRLWFRjY2FKOHJjLTlDTWhqeGp0ZWFtcEtMTm5iZk5JUXVLMTl2SjRUNXlTRE1FTHRta09BNE9peDI3Vk5FeVg2b0FYY0NqWVdDMVN5azhKblVpSjlBbFMybVFaZmh4ZWRBenFueVg1OFo4b04xNmhDT3E5VksxX3NkdmNBV3JDVGJmYXFVbVhDc2xoVlRsdkx4TDhRN19CNFRpWWs?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 12 Aug 2026 22:06:38 GMT
- [SK Hynix and SanDisk Climb 8%, Western Digital Gains 4% as Memory Shortage Deepens - AOL.com](https://news.google.com/rss/articles/CBMid0FVX3lxTFBvLVltUGdlMW1YeUo3NjRfWWJkTU5lOVpMQndrVmJORDUtcjZDX25td1hNZWNmcFA1ZVloX1VYcDIyMnJsY3lzbkJ0WGFhdlA2T2htQzhORVNqUHRFY2F6alNWbV9VdklSS2MtSnRWSXJYeWdBc0lJ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 12 Aug 2026 17:17:31 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel AI Chip Stock Analysis 2026: INTC's $20B Bet on Artificial Intelligence - Intellectia AI；Intel vs. Qualcomm: Which Chip Stock is the Better Buy Now? - tradingview.com；台塑布局半導體化學品合資日商設廠拚2028年投產| 產經 - cna.com.tw

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 100.95 | 114.68 | -11.97% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +1.90% | +0.42% | 2,415.00 | 2,425.00 | -0.41% | 不適用 | 74.39 | 32.47 | 467.58B TWD / 44.69% | 2026-08-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +6.03% | +0.82% | 123.00 | 164.50 | -25.23% | 不適用 | 6.68 | 18.50 | 23.84B TWD / 18.98% | 2026-08-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +11.99% | +12.29% | 224.09 | 224.09 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 482.93 | 516.10 | -6.43% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 911.29 | 971.00 | -6.15% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | +10.90% | -0.46% | 1,344.29 | 2,335.00 | -42.43% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | +10.14% | -0.33% | 416.05 | 446.77 | -6.88% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC、Intel」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 2 篇新聞出現相關標籤。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 2 篇新聞出現相關標籤。

### 主要來源

- [Intel AI Chip Stock Analysis 2026: INTC's $20B Bet on Artificial Intelligence - Intellectia AI](https://news.google.com/rss/articles/CBMibkFVX3lxTE9ITWpmLTQ2dndFMWZlWXBtdEd1QTRWbVpwYnRRbUh0b2l4R21lSkdLd2pEdlFLeVFXdjBGRXBuamw1b05qRUJ0UGdfZEtDVWdycDlNQlZISmpjdXEtOGFTcVJSeXYwR0p2akJLUUtn?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 12 Aug 2026 17:55:48 GMT
- [Intel vs. Qualcomm: Which Chip Stock is the Better Buy Now? - tradingview.com](https://news.google.com/rss/articles/CBMisgFBVV95cUxPdDZfZzBEQzZnYk5xRHRXNEE0d2R0YXpNcVQ3YzhlX2VDRUoxdGZKSjRpanhrVkVIcHU0U3BodkRrWWZsNkQwY2FjYnJiX01QM3Azdm9rSXBBSU53QnhIZUNieEs4WXNpdkZ4MG1tbEd1LTQ5OEZyOTZUdldiOXpuSzNPd3RROF82dGtwSWQtWVYteUhQZEhiWHhvbWlieXJ3QlhLQVEzWGp5TzJMUlJZcVZB?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 12 Aug 2026 13:05:00 GMT
- [台塑布局半導體化學品合資日商設廠拚2028年投產| 產經 - cna.com.tw](https://news.google.com/rss/articles/CBMiXkFVX3lxTE9JT2hHUVliNFhPb3hiTDJzTmtFcFRsWng1VXVZSEM3NXE5Q0lRMUlDRGFFN191MHdsZDk3eGJvaWM0ZTRvTzJ1Q3VrUmhxOWxNOVd5aV84QnBybVVkemc?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 12 Aug 2026 09:07:00 GMT

## 新興題材：StockStory

摘要：新興題材：StockStory 相關新聞集中在：Kulicke and Soffa, AMD, Intel, and Nvidia Shares Are Soaring, What You Need To Know - StockStory

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +11.99% | +12.29% | 224.09 | 224.09 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | N/A | N/A | 482.93 | 516.10 | -6.43% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 100.95 | 114.68 | -11.97% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Kulicke and Soffa, AMD, Intel, and Nvidia Shares Are Soaring, What You Need To Know - StockStory](https://news.google.com/rss/articles/CBMi2AFBVV95cUxOVW5ZUmFRZzRaSGxUMUNuR2RLUVZRb21NWEVWalBLRzBPSGRjcEM2NGU4NGw5MTdzbGFLU0pNTFlnRzFuMU01TUF5a0ZoaHB0WjZMM09iZFJsd0dqdXpYSUVUQ2ljR05EZUlhZVM0Z2FWcVRPWlBqSnYzMGJLQjdVVk1mZjNLT2szazEyMjVmOG9iNmRud2pKS1daQlQ0T3lEQmRZWjhlanZZTE5EYzVJVWVjMjZrSGJYeWowS3BpYzZKQVhjaVlRV2FjRjN6RW1CbDJyVU9WRk8?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 12 Aug 2026 18:24:42 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股基金長線報酬 超車 ETF - 經濟日報；台股基金十強狂飆 近一年漲逾1.6倍 - 經濟日報；主動式台股基金 犀利 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股基金長線報酬 超車 ETF - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5ZYk4waURaRXBKZGVwOWc1SDh3MjB4eERfUFVkaUJmbWFmRnROb3NDN2lYdlctakIyM0dCNV9pNW51Vm95alJ1Rk1fWS1sUDZ1YjFBZFNXTnhQd9IBX0FVX3lxTE1tUThJWGVud2ppeWx4VnJ3NS02Y1NodFVvV1BwTjVyMTgtOW9IQ3ZJS2ExQm5YTnJuN3N4c0sweTdqcERnZFlqZzFaUkRJcm1HMmdDWDF3c3Z5VUt1bmt3?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 12 Aug 2026 18:22:37 GMT
- [台股基金十強狂飆 近一年漲逾1.6倍 - 經濟日報](https://news.google.com/rss/articles/CBMifkFVX3lxTFBCVFVxT2hkQ2VfVjFITWYzUElzRGdnUFFSN2t4UGJMWlhBZG16cGZ1enFxeHFpYUwyc0RwOTQ2M1FlRkl2TkY5NnlocXJOazRPcXE4bUwwSlRaRVdfNThuWHRRX2g3RXI5WEJpTkREenc3RlBqSmcxcnFnak9GUdIBX0FVX3lxTE5hYy1GTVpUcnNrTE5fYzRJSERpdnlzUUpHWFJGSU03MVZ1SVF1NDYxZU1tMmhkcTRxdEJNLVpJTEpWVUhJWmlCS2Fndl9laG9POS1yZW1IZmJZMy1UTjZV?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 12 Aug 2026 03:00:00 GMT
- [主動式台股基金 犀利 - 經濟日報](https://news.google.com/rss/articles/CBMid0FVX3lxTE8zZ210emNkb2J5NUtmYUZIeVZsY0txTnVxdUlvQ2N1TU9xRGxod3FQRE9HZE9nOWkzZm0ya1gwaF9lbEZYUzVNTjlYMmc3LUpWZDQtTDlPSUJ2QVhYdFVGWTQ3QS1xS2lOaUxqUEg3ZGlvUGJLM1B30gFfQVVfeXFMTkhiZzRQYnJabjAzZDVwUXNYcWd5VVNkRkhSUHRQSmlYNzV4ZE9CT2NzYm5rVDRCRlZLWVk4M25SU2tKdFM5dzRfby05ZkZSOG5Zb0hXWUxjMUR3eEJtek0?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 12 Aug 2026 17:45:35 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》開高走高、收漲397點，日K連三紅- 新聞 - MoneyDJ；統一證券：台股追價意願仍不足- 新聞 - MoneyDJ；《台股盤後》開高走高、收漲397點，日K連三紅-新聞內容-基金 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》開高走高、收漲397點，日K連三紅- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxOSkZfMWR6YU9HN2ZUSjc3UXhHR0lDZnNvaEE1eER0TF9OU0hzWkZ0TWs0VmJVR3lHYWx6WXd3N3k3STVvNUpacWlaWmkxeTBZdVRJR25TbXZLZDkzVDhsNy1FR3hVVEV6RldHSmcydUdWMFd6NXlKVnJMSHJnVEQ1emd3LXIyU3F2enFmYzNhWmlkZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 12 Aug 2026 07:36:00 GMT
- [統一證券：台股追價意願仍不足- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPdTNnR0Noa0ZpX1FDQmQ5RFdJaThOVDhPRjVERFR2LURPQnZLMFRVOVM5MzBJb0hPd20zSEk3RzVGRVlFeW1GWTA5MG1Bd3dhbzdLMGZZZ0xfWmgwQkJDRGVCLUZaV1Jma3prc3BzTEtFZ2RPU2FsZUVUMzlCV3hfQWJTaGRlZzdDYlM4Smh2Nld3UQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 12 Aug 2026 00:44:00 GMT
- [《台股盤後》開高走高、收漲397點，日K連三紅-新聞內容-基金 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxNRnVWY0wyREpReGxtRzBvWUNlUFJEQW9kODVYOG1KeUpxdVZsczQ5X0lRUDY0WG9SSkZuQmpFT2F4bmhkMHpzYVRaaUpEWl93MUdZRV9acXNnQjNMU19QVlRETF91X2tPenlMRUtTNURLX1hJZnBFUlhwa3B6dVJqUTQwM3JkNnlJNnFRZVJPSl8?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 12 Aug 2026 07:37:00 GMT

## 新興題材：AI需求

摘要：新興題材：AI需求 相關新聞集中在：研調：AI需求強勁，今年全球半導體收入估增94% - MoneyDJ；新加坡上調2026年GDP預測，第二季表現超預期，AI需求強勁 作者 Investing.com - Investing.com 香港 - 股市報價& 財經新聞

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [研調：AI需求強勁，今年全球半導體收入估增94% - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxORGhFblhrQWhYRzRJRFJTM293MnYwdjltNjVuNHZmTUYzSFBhZG9FNmVwOXBNUmZnS0RDZFFRdWxfZmJuVFpNZzNqMEU0UkxsUjFPX3lSeHhHUDZqYWc5Tjk3UEMxWUZOZjNsbk5xM0RvYjVlc2xKQUF3Q0pYaEZjVUNTTnBnSnVlMGlnaUZTVUtuUQ?oc=5) - Google News source discovery | MoneyDJ Wed, 12 Aug 2026 08:15:00 GMT
- [新加坡上調2026年GDP預測，第二季表現超預期，AI需求強勁 作者 Investing.com - Investing.com 香港 - 股市報價& 財經新聞](https://news.google.com/rss/articles/CBMic0FVX3lxTE5PSGd0ZzhoalVuMzNXZkJZUXVEOF9paU1SbFBCa1pnMDI2THRkWG02LU5QbkFsbE9zTHhRSlZNRU1IZFlROVhYOWdZd3JLN0dSN2RWazN5SVprWHB1NFhSNHhlV2VVeTBxMVVvSWdHaWxzQXM?oc=5) - Google News source discovery | Investing.com Calendar Tue, 11 Aug 2026 00:37:28 GMT

## 新興題材：CoreWeave

摘要：新興題材：CoreWeave 相關新聞集中在：S&P 500 ends higher as CoreWeave results fuel AI optimism - Reuters；CoreWeave counters a key bear case on the AI trade. What it means for our data center stocks - cnbc.com；Stocks making the biggest moves midday: Wendy's, H&R Block, Quantinuum, CoreWeave, Cava & more - cnbc.com

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [S&P 500 ends higher as CoreWeave results fuel AI optimism - Reuters](https://news.google.com/rss/articles/CBMiowFBVV95cUxPYklxZWxQWEI4bU5nVHpWUVJkQWo4YmQ5ZWpfTXNWWHBjNlE0d09NNEdtbWMtQldtbndIMzNBU1Z3TldjNEF5YUoxMHJSdHlXak50XzBMYlh4dHh2OWxVckViSjVxYUFCVlBvcnQ4Vk9vLVF0MWhGR3BidXQzOGItYUVjbnNYSk1pdS1XeTZqUGtaVTZzcDRkR1N1V0xkN0o5STBZ?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 12 Aug 2026 20:26:00 GMT
- [CoreWeave counters a key bear case on the AI trade. What it means for our data center stocks - cnbc.com](https://news.google.com/rss/articles/CBMixwFBVV95cUxPaldQSmF3QWRhaWFNSnJqZGtCZXZValFaSGxxcDRvWHFYZ2dCeGdPM2swNWlDVFF1MHl0c2wzMkJJaXp5RVBkNTRtYkhGOTZjaVBueVpSaU9CTGlCai1Dd2x1eUlrVTI2TGFYWVBmU01odVdjUjVQNGVFX0J1MFJHYzNXdGQ1b3hlSkhibHNDU3JINFBueXdhNnh2LUlXbXJINW1kQVRIRWRUcTBtSUpueERQVVpKdVA4UHY2cEpZNFNfbnpXRUhN?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 12 Aug 2026 20:16:05 GMT
- [Stocks making the biggest moves midday: Wendy's, H&R Block, Quantinuum, CoreWeave, Cava & more - cnbc.com](https://news.google.com/rss/articles/CBMingFBVV95cUxNYUptWUszbmpqUl93S1MxNzlUaEhOcklkbjRlT3I0MTc4dDNPR3Z2ZEFfT0V6SS0zOHlCcS1wU1J0MFdrRXdkbHhzYktLTGxlaHJyc3Q0SFU5dG9ZZjNVMXFCRzdob20yclBTd3BsemtSWlZaaHpNY2Y4WUFQcERlRE1kN29BdGVmZEl2Z0cwYmp2T1VacFN1Y2kyczJIdw?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 12 Aug 2026 16:06:12 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://m.cnyes.com/news/cat/tw_stock_news?type=rss，原因：The read operation timed out
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
