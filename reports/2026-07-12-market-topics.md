# 每日股市熱門話題分析 - 2026-07-12

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜正向｜熱度 11｜市場確認 100.00｜同向 1/1
2. **新興題材：BofA**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0
3. **先進封裝與 CoPoS**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0
4. **半導體與晶片供應鏈**｜正向｜熱度 6｜市場確認 20.12｜同向 1/5
5. **AI 伺服器與資料中心**｜正向｜熱度 17｜市場確認 0.00｜同向 0/6

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.27（樣本 12）
- 5日相關係數：0.13（樣本 12）
- 同向比例：2/12

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 100.00 | 1/1 | 0 | +18.43% | +9.79% |
| 新興題材：BofA | N/A | 0/0 | 0 | N/A | N/A |
| 先進封裝與 CoPoS | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | 20.12 | 1/5 | 2 | +2.04% | +3.22% |
| AI 伺服器與資料中心 | 0.00 | 0/6 | 4 | -3.25% | +1.27% |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：B445 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-06-29 | 0.49 | -0.25 | +38.46% | 13 |
| 2026-06-30 | 0.44 | -0.27 | +62.50% | 8 |
| 2026-07-01 | -0.08 | 0.25 | +30.77% | 13 |
| 2026-07-02 | 0.30 | 0.03 | +55.56% | 9 |
| 2026-07-03 | 0.21 | 0.08 | +55.56% | 18 |
| 2026-07-04 | -0.22 | -0.36 | +22.22% | 18 |
| 2026-07-05 | -0.00 | 0.24 | +40.00% | 10 |
| 2026-07-06 | N/A | N/A | 0.00% | 2 |
| 2026-07-07 | N/A | N/A | 0.00% | 1 |
| 2026-07-08 | -0.05 | -0.05 | +71.43% | 14 |
| 2026-07-09 | -0.11 | -0.36 | +64.29% | 14 |
| 2026-07-10 | 0.55 | 0.05 | +77.78% | 9 |
| 2026-07-11 | 0.13 | -0.08 | +50.00% | 12 |
| 2026-07-12 | 0.27 | 0.13 | +16.67% | 12 |

## 歷史回測摘要

- 回測日期：2026-07-12
- 近5日 3日相關：-0.73
- 近5日 5日相關：-0.42
- 同向比例：+44.44%
- 權重狀態：未調整

- 方向準確度：+44.44%
- 信心排序準確度：-0.73
- 診斷：方向與信心皆需修正

調整原因：近 5 日有效樣本 9 筆，低於 15 筆門檻，暫不調整權重。

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

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：MU, INTC, SNDK: Chip Stocks Rally After-Hours On AMD’s Blowout Report - Stocktwits；SK Hynix Is Surging: 3 AI Chip Stocks Still Poised To Run - Seeking Alpha；SanDisk Vs. Micron: Why One of These Memory Stocks is Much More Dangerous Than the Other - 24/7 Wall St.

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.50 | N/A | N/A | 979.30 | 979.30 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.50 | +18.43% | +9.79% | 1,915.92 | 2,335.00 | -17.95% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.37 | N/A | N/A | 557.89 | 557.89 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.37 | N/A | N/A | 109.84 | 114.68 | -4.22% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -0.09% | +20.96% | 210.96 | 211.14 | -0.09% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK、SanDisk」，共 5 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [MU, INTC, SNDK: Chip Stocks Rally After-Hours On AMD’s Blowout Report - Stocktwits](https://news.google.com/rss/articles/CBMiygFBVV95cUxPeVlYaXJjQjNtTkNRQUxQTHhaLUFMbE80Uy1MeDBpV0FPdkg2SHRLdkdfVUpXM1NrNWhZSVZQQ01sa0o4T1hKdzF1clBFRlRWUmMwWGxQTDNVVFBpOVhObUc2MXpBeXBOZ0p3R0w5NGRNOHB4X0ZIXzhlT0NMbmhzc1RtdmJRTWhlRUhKSHpyVnpaU0VGMlJyU2tDcmdkTG1hWVJJbmtTVDREbzFfWDB4bjhuTGswN3lmdkdHQzY1dzFOVU41VGlBNlZn?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 11 Jul 2026 12:11:10 GMT
- [SK Hynix Is Surging: 3 AI Chip Stocks Still Poised To Run - Seeking Alpha](https://news.google.com/rss/articles/CBMingFBVV95cUxNLWZ5UjVLSHVobXNKQzJlYVFwYmpFeXdzS3NPUElWVDktN0hEX3pxazY2Y3lKd1N1TWxsRFJVYXg2TUo1bzcwbkVYeVJuajRiTVktWDNKMmxBTG5mYkJNcUJjRExhVkRIRF9VT1k3VHg1TXZEd1RKRW5HV0ZwSGdoY3I4dm81ZkM2MEo1WEZKS0l6VjBLRHRGQ0xJQm1DQQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 10 Jul 2026 19:30:04 GMT
- [SanDisk Vs. Micron: Why One of These Memory Stocks is Much More Dangerous Than the Other - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiygFBVV95cUxPanRqcm9nbXlaWUFJdlRSOVRreUh5NnViVmJIeXpJX0IyRm93N21nQ1hCTEo4cFY0ZVVUVk9DY2w0d2R0Z2NUSTVvZkNfVVFwZTFDXzJ4S2NWNW04YjdWTFVUY3BXQVBDVERRTkg3ZTRKWngwU2VYUUpFT0IzRFNLdnQtNFk1dmN1RnVKeEQ4cmtjSGFidGFCcTZsS2Q2UGc0Tnh4bUE4YUtVd01jRjNBZFk0bEZQaV80a003cGhGeUhUMzNVRFBWakdn?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 10 Jul 2026 15:32:33 GMT

## 新興題材：BofA

摘要：新興題材：BofA 相關新聞集中在：SanDisk Rebounds 5%, Western Digital Gains 5%, Micron Climbs 3% as UBS, Citi, BofA Turn Bullish on Memory - AOL.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 979.30 | 979.30 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | +18.43% | +9.79% | 1,915.92 | 2,335.00 | -17.95% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。

### 主要來源

- [SanDisk Rebounds 5%, Western Digital Gains 5%, Micron Climbs 3% as UBS, Citi, BofA Turn Bullish on Memory - AOL.com](https://news.google.com/rss/articles/CBMigwFBVV95cUxPMzRlcDNNdG1uZ3dYS0h5czFPUFJ2Tmw1cnI2c2FiczhtR0kxSUUxSEFNWWFMNVVTcHpIS1NOM2dNamNOZ1hvU2hRSTBJMXk5LWtyMlJyN1ZnMWtIcWxRTjBXVUJpMHlnbVdIdmhNOGxVa0lRT3hRSmtWUW9fZE5xdDlXYw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 11 Jul 2026 05:03:15 GMT

## 先進封裝與 CoPoS

摘要：先進封裝與 CoPoS 相關新聞集中在：英特爾大秀 EMIB-T 先進封裝技術，挑戰台積電 CoWoS 先進封裝技術 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | 0.00 | -1.83% | -2.03% | 2,415.00 | 2,415.00 | 0.00% | 不適用 | 74.39 | 32.47 | 416.98B TWD / 30.09% | 2026-06-01 |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 109.84 | 114.68 | -4.22% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | -0.29% | -6.88% | 677.00 | 680.00 | -0.44% | 不適用 | 10.86 | 62.86 | 65.78B TWD / 32.86% | 2026-07-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 同時符合主題標籤：advanced packaging, CoWoS, CoPoS, FOPLP。
- INTC：新聞直接提及「英特爾」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 3711：產業/供應鏈推估：公司標籤符合「先進封裝與 CoPoS」關鍵字 advanced packaging, CoPoS, FOPLP, panel-level packaging；其中 0 篇新聞出現相關標籤。

### 主要來源

- [英特爾大秀 EMIB-T 先進封裝技術，挑戰台積電 CoWoS 先進封裝技術 - TechNews 科技新報](https://news.google.com/rss/articles/CBMinAFBVV95cUxNUmZxdDluaml4UlpCaWhLY0t5Z3ZxN0l4R0FGdHVfTDZZX1JackZDZWVTVEVzZjd4djNKX1NFbWlORkhIcHUyc1ZzRmZGMGwwSnJQWjNTLW5RblNQU1FzSjYwUDNTVXVhWDlmb0dDSmE4RlUydF9SMExDVlhFQ2RsQnNSMFIzUlc1bHVxaDBPbExIdzI1RUlvcy1TRUo?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 11 Jul 2026 07:11:34 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel and Applied Materials Dive 10%, AMD Craters 8% as Samsung Earnings Trigger Chip Selloff - AOL.com；What Triggered the Recent Semiconductor Sell-Off - Kavout | AI；Intel Stock And Other AI Semiconductor Names Retail Investors Are Watching - simplywall.st

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.59 | N/A | N/A | 109.84 | 114.68 | -4.22% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | +0.26 | -1.83% | -2.03% | 2,415.00 | 2,415.00 | 0.00% | 背離 | 74.39 | 32.47 | 416.98B TWD / 30.09% | 2026-06-01 |
| NVDA 輝達 | 新聞直接提及 | +0.38 | -0.09% | +20.96% | 210.96 | 211.14 | -0.09% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.50 | N/A | N/A | 557.89 | 557.89 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 新聞直接提及 | +0.38 | -0.29% | -6.88% | 677.00 | 680.00 | -0.44% | 未明確 | 10.86 | 62.86 | 65.78B TWD / 32.86% | 2026-07-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.03 | -6.02% | -5.74% | 156.00 | 164.50 | -5.17% | 背離 | 4.00 | 39.20 | 23.12B TWD / 22.85% | 2026-07-01 |
| MU 美光 | 產業/供應鏈推估 | +0.04 | N/A | N/A | 979.30 | 979.30 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.04 | +18.43% | +9.79% | 1,915.92 | 2,335.00 | -17.95% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip, foundry。 方向判斷命中詞：創高。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：創高。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel and Applied Materials Dive 10%, AMD Craters 8% as Samsung Earnings Trigger Chip Selloff - AOL.com](https://news.google.com/rss/articles/CBMigAFBVV95cUxQTEZlSzlmUHNBNDU4ckRBX0FhenNQQ1dYQTU0RWVZeVcwblFWZkVycTN0VnJ6MC1VQlZweW9EUWh1bWpmM0taSkJwaXFCR2ZZa3NkamNxY0ZvVE1UZEdFSTM3N2hwRGxUZ1ZPdEdib1NSUmR1TmN0T21BZzYxZ3ZjZQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 11 Jul 2026 16:41:48 GMT
- [What Triggered the Recent Semiconductor Sell-Off - Kavout | AI](https://news.google.com/rss/articles/CBMiiwFBVV95cUxQeV9hbWl4LXg0eW5ZWFVERlpaZGRsZzBkOEQzb0VuSmptQ2RsR3RUcldSTzhJcW1URGZsbnBjVUxmYlNpMHlESnlJdEVvZ1RaSWloQ0ZfODJXV012UF9qYjFfYVNDaG15cXpBNXYxYWpjaGNIY2hRa3hOdGhUSjdOcDhabENFWmFvV1M0?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 11 Jul 2026 13:38:32 GMT
- [Intel Stock And Other AI Semiconductor Names Retail Investors Are Watching - simplywall.st](https://news.google.com/rss/articles/CBMi2wFBVV95cUxOR01WUG5oWGdDdkw2eFFQeUJYMkc2QUY4Z1J0RGFrM3UtSEY4aG1yd1oxdzZHT3pJNUFoaHEwa2pzRE9XbWZQblV4QzlrczNHRDc1MWFEYjVOQ2ZIY1hrY2lhMFJCcThtOUJEcFRQVDRFR3BGcDBVN1dva2Fyb1IxVE91VEdvYlpkaUhuOThvWXNXbkQwOTM0cXBLclh3MHI4N0VBSFIzTnh4aWRsZEVmamczY000SGJKMzhQbVNzaXhRZ3NGalhfVk9LZURUb05tS1JudTBDbkJLNU3SAeABQVVfeXFMTVN6am1OYWdJcVVvT1A0ZkV3OV9tLUdFTUxmcVZJSml2eVB6MDZPR2prU3luaUxvVDJUbkR2Y2I4ZG40OGthRDFWcnZvbTMtRjBCaHU4Tjd0VWItUlJBYlA1WndlTjk5Y1FpZklEblVROTI0QjJoTlAtVjBXVHZiaEUwdWZCRVk3WWJaalgtY1NzZkFPbDNVVTUzb0wtS2hscnFraFNaVndPWXdCWG1oaUk2T3JzbkNzSWU3UVNXUnNMei1fdWJJbzlDdHRMTmpsWFg0bTdzSU1xOHFpWHNydFI?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 11 Jul 2026 04:07:24 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：What Triggered the Recent Semiconductor Sell-Off - Kavout | AI；Intel Stock And Other AI Semiconductor Names Retail Investors Are Watching - simplywall.st；「Academic Humanizer」問世，抹除 AI 寫作痕跡引發學界爭議 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.56 | N/A | N/A | 109.84 | 114.68 | -4.22% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.04 | -0.09% | +20.96% | 210.96 | 211.14 | -0.09% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.06 | N/A | N/A | 557.89 | 557.89 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.03 | -1.83% | -2.03% | 2,415.00 | 2,415.00 | 0.00% | 背離 | 74.39 | 32.47 | 416.98B TWD / 30.09% | 2026-06-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.02 | -1.95% | -24.00% | 385.10 | 506.69 | -24.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -10.48% | +29.23% | 399.97 | 446.77 | -10.48% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.03 | -0.29% | -6.88% | 677.00 | 680.00 | -0.44% | 未明確 | 10.86 | 62.86 | 65.78B TWD / 32.86% | 2026-07-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.02 | -4.85% | -9.67% | 3,925.00 | 4,310.00 | -8.93% | 背離 | 62.91 | 62.55 | 58.01B TWD / 2.80% | 2026-07-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [What Triggered the Recent Semiconductor Sell-Off - Kavout | AI](https://news.google.com/rss/articles/CBMiiwFBVV95cUxQeV9hbWl4LXg0eW5ZWFVERlpaZGRsZzBkOEQzb0VuSmptQ2RsR3RUcldSTzhJcW1URGZsbnBjVUxmYlNpMHlESnlJdEVvZ1RaSWloQ0ZfODJXV012UF9qYjFfYVNDaG15cXpBNXYxYWpjaGNIY2hRa3hOdGhUSjdOcDhabENFWmFvV1M0?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 11 Jul 2026 13:38:32 GMT
- [Intel Stock And Other AI Semiconductor Names Retail Investors Are Watching - simplywall.st](https://news.google.com/rss/articles/CBMi2wFBVV95cUxOR01WUG5oWGdDdkw2eFFQeUJYMkc2QUY4Z1J0RGFrM3UtSEY4aG1yd1oxdzZHT3pJNUFoaHEwa2pzRE9XbWZQblV4QzlrczNHRDc1MWFEYjVOQ2ZIY1hrY2lhMFJCcThtOUJEcFRQVDRFR3BGcDBVN1dva2Fyb1IxVE91VEdvYlpkaUhuOThvWXNXbkQwOTM0cXBLclh3MHI4N0VBSFIzTnh4aWRsZEVmamczY000SGJKMzhQbVNzaXhRZ3NGalhfVk9LZURUb05tS1JudTBDbkJLNU3SAeABQVVfeXFMTVN6am1OYWdJcVVvT1A0ZkV3OV9tLUdFTUxmcVZJSml2eVB6MDZPR2prU3luaUxvVDJUbkR2Y2I4ZG40OGthRDFWcnZvbTMtRjBCaHU4Tjd0VWItUlJBYlA1WndlTjk5Y1FpZklEblVROTI0QjJoTlAtVjBXVHZiaEUwdWZCRVk3WWJaalgtY1NzZkFPbDNVVTUzb0wtS2hscnFraFNaVndPWXdCWG1oaUk2T3JzbkNzSWU3UVNXUnNMei1fdWJJbzlDdHRMTmpsWFg0bTdzSU1xOHFpWHNydFI?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 11 Jul 2026 04:07:24 GMT
- [「Academic Humanizer」問世，抹除 AI 寫作痕跡引發學界爭議 - TechNews 科技新報](https://news.google.com/rss/articles/CBMic0FVX3lxTE50elY3S29sQUg3WXNESTBmbkp2X2VlUmlIYTdxRjFaTnpHSUxSdlB6cHYwOTVWZWZqYWlsMEF0a1d2b1haUjRzcFNDa2FjV2VnM0o3Y1d2anl6WS1HZU0wbFU4YUNJUVdiS254VHFMNVJhMms?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 11 Jul 2026 06:41:34 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：同業股價表現-電子-電競筆電-台股 - MoneyDJ；最新專欄分析 - MoneyDJ；大昌-新竹 對 華泰(2329)個股 單一券商歷史明細 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [同業股價表現-電子-電競筆電-台股 - MoneyDJ](https://news.google.com/rss/articles/CBMiaEFVX3lxTE44QnY5c1lkZTRGNXhGZ012UmtmVXZPdnlyQ0JVVEZsOTA2VklQR1doNkgzSkRQNjRVMy13LS01MzZHUW4wbEpkN3pCTkVDZDJMNDRFWDRMX1EtNndvU3BJZDlsVVItdUZq?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 11 Jul 2026 09:08:26 GMT
- [最新專欄分析 - MoneyDJ](https://news.google.com/rss/articles/CBMib0FVX3lxTE5LOWxJSnlHUDlBNW1pUXNZdnBBeXJSR3UxOXZjWUsyYTFvaDBIbHNNRWNkME5mYVBYa2lZbHAzWjU4b19UMkl4NDNFaW9wUE9yNlZQUnk4cFQ1UGFXdzF2d2hnZlhBb1h0eFRfWTdJQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 10 Jul 2026 23:37:18 GMT
- [大昌-新竹 對 華泰(2329)個股 單一券商歷史明細 - MoneyDJ](https://news.google.com/rss/articles/CBMihwFBVV95cUxQNWpzZ3dhWEowY19hbkhmTDNkaW96NGxKVm1UMUZIbXNfdERNRkl3QnFFYXZsNDRRalNib1ZTam9MNnYzLWRORlZRbXUwZVU4RjZQUnJWczZIdnVWNTVFT1ZvV3lWSEtTdWVSck1Zd1QwUkpVc0JOX01mdERxUERXLThZaXlrZ00?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 11 Jul 2026 07:46:24 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股四大策略挑金雞 下半年焦點股 14強吸睛 | 市場焦點 | 證券 - 經濟日報；台股風險管理 要再加把勁 - 經濟日報；台股擂台／挑戰者「Q女王」劉良梅 本周挑環球晶、和大 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股四大策略挑金雞 下半年焦點股 14強吸睛 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxNUlJmOWVvdzJuUHA0TFE0RE1JSXIwMk9ZdGxjdC05U0VaanlmdXZEYjdGWWJ1R3NLeWlYZGdKWnNoU2JjQ001Nk9WcktobFpUcnJNbkcyQ0I3R2lvMjRPMjNFMDBHWEtVZ3Z1bFFqYzc2cVRoejNQb1lNdGdWUDVSeQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 10 Jul 2026 09:00:00 GMT
- [台股風險管理 要再加把勁 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE44Qnlmek5qYTMtTmFlcXhKWERNX0RRUEQxWWwwQlhBVFkxdkZaZko4YVlBQjdJbXhxOFJMRzlqNWF1R1g4UTVOMUpzYU5WTHM3dFotVXRvTWtMQdIBX0FVX3lxTE9fV21GSG5RZjhVcEgzLWhhZ0FMN3NnR2xQTHZ2MzlsMU1QaE1JcTJ5azh3S2Mwd3ByVWQyeXh6a0JrVDkzdHZ2RjREVUdoMDdac0JQSk1uMGdCMzAzZ1dz?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 11 Jul 2026 04:00:00 GMT
- [台股擂台／挑戰者「Q女王」劉良梅 本周挑環球晶、和大 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTE5oU09CWGRhOHBZMzh6TlE5SDd1T2s3VzBfOUxCN1V6SldjRGRxY3N6b21xR0hYaTFIc3RUOWdoNmUyZHltUnFzRzBfMlRKTDVCc2tCbU1GeGlINzZu?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 11 Jul 2026 17:25:58 GMT

## 新興題材：B445

摘要：新興題材：B445 相關新聞集中在：個股動態報導內容-F4D67FD3-6EDB-422A-B445-20BD81CAEDC4 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-F4D67FD3-6EDB-422A-B445-20BD81CAEDC4 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxQSWQwYmJ1dktsRkpxNTJ4MnRURjV1T0FNWGJ4dFFNYU1SZ2g5MGRIR2x4T2RaVXQzVm41Y2JiaXRYR0dsekQ0bjU5VmcydjhRLTJUVTNaZEFUZUxrcTlkNFp6VTE0bHVuRnJIOXBaY2gtU0N3WXMydHUxSU5OYzZteURQRXc2eERRV3BkNXlYczdIbU1V?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 10 Jul 2026 09:28:51 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
