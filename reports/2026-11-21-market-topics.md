# 每日股市熱門話題分析 - 2026-11-21

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜負向｜熱度 9｜市場確認 100.00｜同向 2/2
2. **半導體與晶片供應鏈**｜負向｜熱度 4｜市場確認 100.00｜同向 8/8
3. **新興題材：TrendForce**｜負向｜熱度 1｜市場確認 100.00｜同向 2/2
4. **散熱與液冷供應鏈**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0
5. **先進封裝與 CoPoS**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.04（樣本 20）
- 5日相關係數：0.04（樣本 15）
- 同向比例：13/20

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 100.00 | 2/2 | 0 | +22.72% | +19.45% |
| 半導體與晶片供應鏈 | 100.00 | 8/8 | 0 | +24.72% | +14.68% |
| 新興題材：TrendForce | 100.00 | 2/2 | 0 | +22.72% | +19.45% |
| 散熱與液冷供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 先進封裝與 CoPoS | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 0.00 | 1/8 | 7 | -19.56% | -13.07% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 相關性偏弱；應提高同向價格確認權重，降低泛 AI、泛半導體等寬標籤推估權重。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-11-08 | -0.21 | 0.03 | +23.08% | 13 |
| 2026-11-09 | -0.56 | -0.62 | +60.00% | 10 |
| 2026-11-10 | -0.32 | 0.24 | +3.45% | 29 |
| 2026-11-11 | 0.34 | -0.26 | +46.67% | 15 |
| 2026-11-12 | -0.09 | 0.07 | +50.00% | 14 |
| 2026-11-13 | -0.56 | 0.42 | +54.17% | 24 |
| 2026-11-14 | -0.34 | 0.12 | +42.11% | 19 |
| 2026-11-15 | -0.02 | 0.62 | +50.00% | 20 |
| 2026-11-16 | -0.30 | -0.27 | +38.89% | 18 |
| 2026-11-17 | 0.44 | 0.39 | +80.00% | 15 |
| 2026-11-18 | 0.27 | -0.38 | +86.36% | 22 |
| 2026-11-19 | 0.20 | -0.23 | +69.57% | 23 |
| 2026-11-20 | -0.35 | -0.36 | +69.23% | 13 |
| 2026-11-21 | 0.04 | 0.04 | +65.00% | 20 |

## 歷史回測摘要

- 回測日期：2026-11-21
- 近5日 3日相關：0.38
- 近5日 5日相關：0.37
- 同向比例：+81.82%
- 權重狀態：已調整

- 方向準確度：+81.82%
- 信心排序準確度：0.38
- 診斷：正相關

調整原因：近 5 日信心分數與後續報酬呈正相關，提高市場確認、歷史題材與直接提及權重。；關鍵詞×公司後續樣本有效 0 筆，未達 30 筆，不調整樣本權重

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

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Micron and SanDisk Stocks Crash 12%-14% as AI Selloff Spreads to Memory Chipmakers - Coinpaper；SanDisk Tumbles 8% as TrendForce Turns Bearish on 2027 NAND Prices; Micron Falls 5%, SK Hynix Slides 4% - 24/7 Wall St.；SanDisk and Micron Rise 4% as Anthropic's Record IPO Revives the AI Trade; Western Digital Gains 5% - 24/7 Wall St.

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | -0.63 | -38.77% | N/A | 594.51 | 971.00 | -38.77% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.63 | -6.67% | -19.45% | 94.39 | 291.88 | -67.66% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -45.03% | -37.47% | 125.53 | 228.38 | -45.03% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：bearish, falls, growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 4 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：bearish, falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Micron and SanDisk Stocks Crash 12%-14% as AI Selloff Spreads to Memory Chipmakers - Coinpaper](https://news.google.com/rss/articles/CBMirgFBVV95cUxNYV83ZXhRN1MzSExhN3JhZi1xNEpVUlplSHcwZS1rOW1BR19QU0U3SDIzUXltZDZaQ25ETElCaVdFSnJDckhqUU5FYmRPMTdtU1pJV214X2RBb29qNDlNanhtczBQamVQMGlIWFBkU2pUVWxrdm56OU1IRHdBdXBrdWt5V1pRaVpFMmc2Rl8wT2l2N1YxSHhLLXRGUUNaU0tOaXFPOWI3V0hHazFEaXc?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 20 Nov 2026 22:31:44 GMT
- [SanDisk Tumbles 8% as TrendForce Turns Bearish on 2027 NAND Prices; Micron Falls 5%, SK Hynix Slides 4% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi2gFBVV95cUxOVEl4eHlVV1BGWUVwei1KdWRVeUxhZzZhQmRMZWRXemQ4MDhmTTNJTi1abThheG5TQ0xUczJLUmlySnEtS21aX3poNXlRMDRRM0hGaFllOGNoNHFjWjI4MTRUX2ZUWHFQWkczbHNLV19TOUhkd3lBdkhaX3F5NWpORHN3S3JhcHo3T0JvWXpLR1J4ZWpYYXpjODJERVNIVHNaRlJsSUkybEg4U3lSS2dqZDlDdDdlbDdFVi1YVjdsRXRzRlBsUzVkdjZEeXRmemlNR1N5ZktHY0VwZw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 20 Nov 2026 14:09:00 GMT
- [SanDisk and Micron Rise 4% as Anthropic's Record IPO Revives the AI Trade; Western Digital Gains 5% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi1gFBVV95cUxNLVFybjd3ZGJ4R2x2VVA0VjYtc3RFd3JCbFVWdC1QQWZRTUhyOUtTMnotbE1mTjJ0RGFMZlZvVzFySWd3T25yYnNmeFlGTWx2SGpHVW1YLXZONFhpMVAtOGYxSzktSTg4N0ZYNTduMkg0SFdMNFFCMGRrNU1FLWlJa1BMeExUc3RRaEs5bnVLallfSzhCaGdPaGxnUk9kcHpKVElINlAzQktWQUZ4Y2M0My11SGNBajc1NTU1VV9pTmpNTXphR3VMeTNWMUlXaTR4VkJDdnpn?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 19 Nov 2026 14:11:00 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel jumps 7% after landing first 18A chip cus... - Pluang；輝達案引發美關注先進 AI 晶片使用情形，新加坡稱願協助檢查 - TechNews 科技新報；美國批准近 88 萬顆高階 AI 晶片輸中，廠商名單曝光促國安爭議升溫 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.57 | -55.28% | +26.43% | 51.28 | 114.68 | -55.28% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | -0.52 | -45.03% | -37.47% | 125.53 | 228.38 | -45.03% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.05 | -7.83% | -14.89% | 2,000.00 | 2,480.00 | -19.35% | 同向 | 98.27 | 20.36 | 586.89B TWD / 59.71% | 2026-11-01 |
| 2303 聯電 | 產業/供應鏈推估 | -0.05 | -13.10% | -20.89% | 80.30 | 164.50 | -51.19% | 同向 | 6.80 | 11.86 | 25.20B TWD / 18.33% | 2026-11-01 |
| AMD 超微 | 產業/供應鏈推估 | -0.04 | -17.77% | N/A | 424.39 | 516.10 | -17.77% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | -0.04 | -38.77% | N/A | 594.51 | 971.00 | -38.77% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | -0.04 | -6.67% | -19.45% | 94.39 | 291.88 | -67.66% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -13.32% | -21.80% | 304.41 | 446.77 | -31.86% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：bearish。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：bearish。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 2 篇新聞出現相關標籤。 方向判斷命中詞：bearish。

### 主要來源

- [Intel jumps 7% after landing first 18A chip cus... - Pluang](https://news.google.com/rss/articles/CBMimAFBVV95cUxQb2RnYkczMVEzRlhIUDhraUh3T1hMcXpiamZxZnc2LWpkMnVVLU40LVdHRHM2ZENMbWRzbzJJWlRjSnNJN0lobktCNlpySDlJSmt0bjlOdWlhSGhjTDFNVWExd2NrVzVQM29JMGc3dS1DUVdSN3BEbWpIWVhqQ2ptY1NXYU14YzJNMDY0YVlFTGE0ZXU5bUFfeQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 19 Nov 2026 16:14:35 GMT
- [輝達案引發美關注先進 AI 晶片使用情形，新加坡稱願協助檢查 - TechNews 科技新報](https://news.google.com/rss/articles/CBMitAFBVV95cUxQTzVlNlYzSzk0NldxdkpSRjY1Z0hFWEVZWE1BN2Y3azROX0VCY2RDLXpfbElkbXBnS01TZHBSVTZWZkwxVWlIT2RQVmpLdWFfUkRCM1ZTOVNPOW5DdEE5SWZMaHpHMkd6MXg0WWRCX2g5eGxCWVR0YnBkWnYxeGs5bk9qWkhUd0p0YWh4UXk4Q0RQZW16SWN1MGg2VXNqOEhRZTVreno2NFFFTnU2WTFzaUFHWnU?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 19 Nov 2026 00:50:30 GMT
- [美國批准近 88 萬顆高階 AI 晶片輸中，廠商名單曝光促國安爭議升溫 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiwwFBVV95cUxPdEdTdXZ2UG9hUzBWQ2tUMWdHektfQ0RYQ2c1dnkzaXB0aXhtbFNJYUx4TnVDakU2ZGZyeW9paWtqeTFJOGpNTndGTk8weWVJUkVvVjZKd0F4cnhTTE43aWhwbkhrek1vMWRDUDZBNmFYOHdKblJ1Qkl4anVPUzRySW9tU2daLTRJUVhIeEVBR25lNFI4YklwcHZyVVhHc3Y3MzB2UGZDRW10SnZ4eHkzWEgwMzR2aUFzVmFoTEtnaUFIUEU?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 20 Nov 2026 05:41:31 GMT

## 新興題材：TrendForce

摘要：新興題材：TrendForce 相關新聞集中在：SanDisk Tumbles 8% as TrendForce Turns Bearish on 2027 NAND Prices; Micron Falls 5%, SK Hynix Slides 4% - 24/7 Wall St.

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | -0.46 | -38.77% | N/A | 594.51 | 971.00 | -38.77% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.46 | -6.67% | -19.45% | 94.39 | 291.88 | -67.66% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron」，共 1 篇新聞命中。 方向判斷命中詞：bearish, falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 1 篇新聞命中。 方向判斷命中詞：bearish, falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。

### 主要來源

- [SanDisk Tumbles 8% as TrendForce Turns Bearish on 2027 NAND Prices; Micron Falls 5%, SK Hynix Slides 4% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi2gFBVV95cUxOVEl4eHlVV1BGWUVwei1KdWRVeUxhZzZhQmRMZWRXemQ4MDhmTTNJTi1abThheG5TQ0xUczJLUmlySnEtS21aX3poNXlRMDRRM0hGaFllOGNoNHFjWjI4MTRUX2ZUWHFQWkczbHNLV19TOUhkd3lBdkhaX3F5NWpORHN3S3JhcHo3T0JvWXpLR1J4ZWpYYXpjODJERVNIVHNaRlJsSUkybEg4U3lSS2dqZDlDdDdlbDdFVi1YVjdsRXRzRlBsUzVkdjZEeXRmemlNR1N5ZktHY0VwZw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 20 Nov 2026 14:09:00 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：輝達財報佳散熱需求夯：奇鋐| 雜誌 - UDN；散熱雙雄戰1》奇鋐、雙鴻同喊明年ASIC超車 輝達獨大局面生變？ - 民報；《DJ在線》輝達換代若放緩，散熱廠布局受考驗 - 台視全球資訊網

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | -10.73% | -27.47% | 2,205.00 | 3,435.00 | -35.81% | 不適用 | 90.78 | 24.38 | 22.10B TWD / 34.35% | 2026-11-01 |
| NVDA 輝達 | 新聞直接提及 | 0.00 | -45.03% | -37.47% | 125.53 | 228.38 | -45.03% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐、散熱」，共 3 篇新聞命中。 同時符合主題標籤：thermal。
- NVDA：新聞直接提及「輝達」，共 3 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [輝達財報佳散熱需求夯：奇鋐| 雜誌 - UDN](https://news.google.com/rss/articles/CBMiUEFVX3lxTE9TSmFJTm5ZLTA1UUU3d3J6SmRHZG9ua1hVLXRFVFNfZFRBd3R3cU9oZkdCMkNLV3UxQVI1SlBYRXpjU3JTSW51djJvY3pPM3Iz?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 19 Nov 2026 06:23:29 GMT
- [散熱雙雄戰1》奇鋐、雙鴻同喊明年ASIC超車 輝達獨大局面生變？ - 民報](https://news.google.com/rss/articles/CBMiZEFVX3lxTFBkTG1nSTVFWUx3bHl4S213UVNVVUZRX2QzSVA0LVF6bmNWUEMxTi12Nm1yYVNuSDNFbGgyd3kwN0dJcExCM09wbC1ZZjd2QmxwUFM0Ul9FbWNCejg2dXhRcVQ0OEY?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 20 Nov 2026 21:23:01 GMT
- [《DJ在線》輝達換代若放緩，散熱廠布局受考驗 - 台視全球資訊網](https://news.google.com/rss/articles/CBMinAFBVV95cUxQcjhOczk0eFVzSVZsSlkxWWpodHZyM0JMMk56aGthZHh6RnNnNm96SG03Yllob01EakZRNzZ1SmZENGFDeGpVd21MSXl5alpxRHlLTXZTSk9MbENqSC1oY3FHQ0tvUXduVWFnV05DTm1uTmxMNjkwWkN4R3VFeFFWUy12SU9pbnFVcFdLdC0zaTVUeHQ2UVNWNm56Vng?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 19 Nov 2026 05:20:13 GMT

## 先進封裝與 CoPoS

摘要：先進封裝與 CoPoS 相關新聞集中在：美光新加坡 HBM 先進封裝廠首部機台進駐，預計 2027 年初進行產出 - TechNews 科技新報；南寶新設半導體產業發展部 布局先進封裝/CCL材料 - MoneyDJ

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | -38.77% | N/A | 594.51 | 971.00 | -38.77% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -7.83% | -14.89% | 2,000.00 | 2,480.00 | -19.35% | 不適用 | 98.27 | 20.36 | 586.89B TWD / 59.71% | 2026-11-01 |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | -12.12% | -23.58% | 457.00 | 703.00 | -34.99% | 不適用 | 17.55 | 26.23 | 88.62B TWD / 47.13% | 2026-11-01 |

關聯理由（前 3）：
- MU：新聞直接提及「美光」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「先進封裝與 CoPoS」關鍵字 advanced packaging, CoWoS, CoPoS, FOPLP；其中 0 篇新聞出現相關標籤。
- 3711：產業/供應鏈推估：公司標籤符合「先進封裝與 CoPoS」關鍵字 advanced packaging, CoPoS, FOPLP, panel-level packaging；其中 0 篇新聞出現相關標籤。

### 主要來源

- [美光新加坡 HBM 先進封裝廠首部機台進駐，預計 2027 年初進行產出 - TechNews 科技新報](https://news.google.com/rss/articles/CBMirAFBVV95cUxOYVZucWs4bGlaM0xsb1FfWVREQ194dGhCbVNuZHhNTXB4QTVETnZ0cDZYTHhQS0gtRHBzZFY0Rm51RFR5SzFtZGV4VjQ1UTdoQVA1cWNwVmlfQjJFeDM0OFhRbTl3Ty1Ub1R3Qk9uVnM4cHpNd3dQVDRlVXBwUkxONUFaQ1hSZk9TSWlfSURpdU9mMFJqQ1RibjFsdl90NU4zdjAzbGR2Wm5Kb2Yy?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 19 Nov 2026 10:02:40 GMT
- [南寶新設半導體產業發展部 布局先進封裝/CCL材料 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPeWUzUWM4YnhXMExKX2xvemZEU0NIb2trMjJ5SmtmZTQtdFVzdk9FS3VBOEpRVkZEakJ2SkJjcDR0UFdxcFNuZ3VZa1NBN0VIb0c3ZWlFY19ZbVJLQWRXWmsyVFl1T2hCOENsaTh5N0d4MEl1S042N2VpZ0hBdmc2WDQ3S3RVUHdsWmVpZnYtQ19rUQ?oc=5) - Google News source discovery | MoneyDJ Fri, 20 Nov 2026 07:55:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Nvidia vs. Intel: One AI Stock Is Worth the Drama, the Other Isn’t Worth the Wait, Says Investor - The Globe and Mail；Intel Stock And 2 AI Infrastructure Shares Backing Data Center Growth - Simply Wall St；AMD Is Down 8% After Short Seller Hunterbrook Ties AMD's Firmware to Blacklisted Chinese Server Maker; Resilient Intel Remains Up 5% - 24/7 Wall St.

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.32 | -55.28% | +26.43% | 51.28 | 114.68 | -55.28% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.32 | -45.03% | -37.47% | 125.53 | 228.38 | -45.03% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.29 | -17.77% | N/A | 424.39 | 516.10 | -17.77% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2454 聯發科 | 新聞直接提及 | +0.27 | -12.76% | -18.69% | 3,350.00 | 4,920.00 | -31.91% | 背離 | 62.35 | 53.88 | 55.03B TWD / 5.77% | 2026-11-01 |
| 2330 台積電 | 產業/供應鏈推估 | +0.03 | -7.83% | -14.89% | 2,000.00 | 2,480.00 | -19.35% | 背離 | 98.27 | 20.36 | 586.89B TWD / 59.71% | 2026-11-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | +7.61% | -1.52% | 484.52 | 507.29 | -4.49% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -13.32% | -21.80% | 304.41 | 446.77 | -31.86% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.02 | -12.12% | -23.58% | 457.00 | 703.00 | -34.99% | 背離 | 17.55 | 26.23 | 88.62B TWD / 47.13% | 2026-11-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 3 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：growth, 強勁。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA、輝達」，共 2 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。 方向判斷命中詞：growth, 強勁。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。 方向判斷命中詞：growth, 強勁。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Nvidia vs. Intel: One AI Stock Is Worth the Drama, the Other Isn’t Worth the Wait, Says Investor - The Globe and Mail](https://news.google.com/rss/articles/CBMiigJBVV95cUxNdUJxMFhWd2pVZTBYOUwwbXJNUjNETFBnNWFicVR0TzdrV0FKcV9LSXFDUWh0cjhUcFlKbVFEeVU4UmpUeDdxaGJQLU5LWnYxVXZ0QTVnLS1WUFhJTDlsS0JwWllrcjdlXzNVTUJ0VkVqbERYaEQ1dklOWDhOTV9iTDc3b2QxcFU0NkZ0N3BVWmRRUWE3eV8tWXIyaUdyd19PZUh4TmtROGtHOUtMQktlRW1scmdtYTNMU3RmOTJYOHNOTGFRV3F6ZU1rVVQxUXA2YVpEdnBMbDNneHZyUC1mbGRTUXlmeVQ4RG1NdUZpMzVsS1l0SjZnWjBnZ25VVnY2QmU2MDZpclF5UQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 20 Nov 2026 14:28:03 GMT
- [Intel Stock And 2 AI Infrastructure Shares Backing Data Center Growth - Simply Wall St](https://news.google.com/rss/articles/CBMiygFBVV95cUxQNTU2MldLVGdRQ3ExWW1WTzNwYTZyRnJYRzEwZHI0VmJTakJXNlZDa2NtSGw3eGNPUzgwNWlIejZhVVZRQTIwQm9UekQtQXFfVFFwQ0ZRTWlsa2NXUU5OMTFmODdXOUNYX3dhSHRjNXVjTVBTcm1VUldEcm52YjF6TVA2UXZYOTlPanNWZXNiVVZ2d2hUQ0diUUJjNVdhbXY1blZpMXhmMnUtVXhKRks3QzJsUkREV3REOThXemRrQlN3SnRUX2FGcHRR?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 20 Nov 2026 18:10:47 GMT
- [AMD Is Down 8% After Short Seller Hunterbrook Ties AMD's Firmware to Blacklisted Chinese Server Maker; Resilient Intel Remains Up 5% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMigAJBVV95cUxNdzd0czNoRHhWV3NBazdxMDZFQ0tLcWtObmF2UXRSLTBReGpORWJ4UkxpWDBZSUxqQ2YwNEFaNEEzSF9VRVZjQjU2UUE3dTlPUWhCRnBObm9IOXJrYjNhOHhXUnJSNTJzOE9ZZTNsNDBsdXc2ZkpmZ0J1NHF2MmdGaWlDdjBIZkMtRTRNQzZuWnY5YXNQZlI2MGJWOWNSemRHdzJEYXZyYkhaNWhBWEh5cHJTRkJCRzBXY191NVRFRGhlbTJaWS0yVldjaEd0LXNudnhPa2FGaExCdU5LUEl3ek5WdTBsMXRtMXluV1pYLUpIWmpuWHNOTGx2ZG81T3hT?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 19 Nov 2026 16:06:00 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股又跌！金管會加碼限空令 平盤下放空、借券賣出再收緊 - 經濟日報；台股大幅修正 證交所董事長林修銘信心喊話 - 經濟日報；今日最夯 ETF／台股周重挫、反向 ETF 買氣升溫 00686R 大漲8.7% - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股又跌！金管會加碼限空令 平盤下放空、借券賣出再收緊 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBpdng0NjBqN2dIdm1JVHVTbkRrbUpOeTdWRFpxVHcyaFpfN2lJRFBRZkdCbm8wX3JqcTV2RXF0ajZQQ0lSbk9yU21XcTcwWDdvMEY2anF6Z1lyd9IBX0FVX3lxTE9JMWtVRUlLZ2JlR0hSNm1mMElELWpqa0ttcDVFajFSZnRPMmc4MHJLc0RTbVNPOHlHblctOUxvczZ6YzhBVGxoeXBBSV8tRWNCQkhFLUtaUjdLU3V1ZjlN?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 19 Nov 2026 06:42:23 GMT
- [台股大幅修正 證交所董事長林修銘信心喊話 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE51TUR4VHAtUGtkSUMzWXFBbUhYVE1GUm83WERraDhyNERsT29SOGFUZVBjQ0M5VDEwNmJtVkFSSVU1OWI2NzI5WVBLLTdMb0RJZ1NTWkdnUXU1QdIBX0FVX3lxTFBHVGNiYXpLNFF1SmVncTBrRFFHck1feEwwcHRoR01sNm5ZZWxFMTVtZTE0TTQxamZpSy02MG8yckNDRVpyUUVvdWdJaTA3YjM5cnBXX0J1X01tZklSZVo4?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 20 Nov 2026 09:27:53 GMT
- [今日最夯 ETF／台股周重挫、反向 ETF 買氣升溫 00686R 大漲8.7% - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE00ZWEwSHRWTUhoQlJnNUYyRDhQMGR1S1dGbE9ETzdLYmR2MTVkSTNJemtFdjVMUW4yYjhtZ242SGM0MFJlTHg3Z1MwTWw3U3d5Vks0NUJVOG1jd9IBX0FVX3lxTE5Xai1uNFdTZ0RrcDNZSnFkWF9kZmZzNG8tTWVZaS1XNmc2WVpMdDRKZm9IdXc0Z05Rc1prcTNlaDBUbnN3VkFpMUo3ZWRCTy10S2JzYnpCa2FKc1J5eUFZ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 20 Nov 2026 12:43:18 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：主動式台股基金/ETF規模成長統一投信貢獻靚- 新聞 - MoneyDJ；《台股盤後》重摔2393點、險守36K；本週跌逾17% - MoneyDJ；統一證券：台股中長期技術面偏弱勢- 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [主動式台股基金/ETF規模成長統一投信貢獻靚- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPYmVKX3VWQ1dkdDVLYy1WWFpGYTUzUGRHckpwaG1mQTdMWmE2eEk5TmVzd1d3WGdYNXF6dnl4T1RTN1Nzdm5jem5ZcW1xdGNhZVI0YWtKa0Fpd0tXTWlRR3FDeVBQNlA1Vi1rY09nRDNVaXJKdW82bVB3cDhLUElMYlpYZkpwNFczaWRXUDYyZEZ1QQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 20 Nov 2026 07:05:00 GMT
- [《台股盤後》重摔2393點、險守36K；本週跌逾17% - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxQZjBGai1Vd3NWUWo3OVpZSmVXRDRRYUx4amhCT1VwRDZuaVo4WmlFLURNM2JDRlduRllfa2JGcVNJem9Jemcza0lSUWJUem9SRmc4aVBPYWdXOWRsZGlya0NfQkhBalgyVkZZNjZfZFc0WWtCbWdXZ0I1WkRkR1lfa0Q1cldSRlB6bFJVTzBsMms?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 20 Nov 2026 08:15:00 GMT
- [統一證券：台股中長期技術面偏弱勢- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQeWlveGstRUhLdllvQkt1Ri1QSm9iY3RUZ2Fja3NoWnFTUXJScDBUNzFVaHVCWDVRQy14bE02QlhFWGNmdlVndXBkRDdnZmEyZklPSEpYV3ZXbTlaMlc1Y1NDaEJMV182RnUxeFkxR1h3S05zV1lvdE5nX0cxNmJUeWtCQkhyY0hmc2NESjBKc19CUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 20 Nov 2026 00:46:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
