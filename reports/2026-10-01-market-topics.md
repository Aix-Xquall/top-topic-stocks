# 每日股市熱門話題分析 - 2026-10-01

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜正向｜熱度 11｜市場確認 47.49｜同向 1/2
2. **半導體與晶片供應鏈**｜負向｜熱度 6｜市場確認 61.13｜同向 5/8
3. **新興題材：輝達散熱**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
4. **新興題材：OpenAI**｜中性｜熱度 4｜市場確認 N/A｜同向 0/0
5. **AI 伺服器與資料中心**｜負向｜熱度 12｜市場確認 0.00｜同向 1/8

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.21（樣本 20）
- 5日相關係數：-0.27（樣本 14）
- 同向比例：8/20

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 47.49 | 1/2 | 1 | +4.17% | -8.33% |
| 半導體與晶片供應鏈 | 61.13 | 5/8 | 2 | +5.79% | +0.01% |
| 新興題材：輝達散熱 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：OpenAI | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 0.00 | 1/8 | 6 | -6.08% | -2.75% |
| 散熱與液冷供應鏈 | 15.88 | 1/2 | 1 | -6.38% | -4.38% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-09-18 | -0.15 | -0.07 | +35.71% | 14 |
| 2026-09-19 | 0.20 | 0.47 | +46.15% | 13 |
| 2026-09-20 | -0.04 | -0.25 | +30.77% | 13 |
| 2026-09-21 | -0.15 | -0.05 | +61.54% | 13 |
| 2026-09-22 | -0.00 | -0.01 | +88.24% | 17 |
| 2026-09-23 | 0.35 | 0.22 | +80.95% | 21 |
| 2026-09-24 | 0.05 | 0.42 | +90.00% | 10 |
| 2026-09-25 | -0.31 | 0.15 | +30.77% | 13 |
| 2026-09-26 | 0.22 | 0.14 | +63.64% | 11 |
| 2026-09-27 | 0.11 | -0.14 | +57.14% | 14 |
| 2026-09-28 | 0.05 | -0.53 | +63.64% | 11 |
| 2026-09-29 | 0.31 | -0.78 | +16.67% | 6 |
| 2026-09-30 | 0.05 | 0.04 | +33.33% | 18 |
| 2026-10-01 | 0.21 | -0.27 | +40.00% | 20 |

## 歷史回測摘要

- 回測日期：2026-10-01
- 近5日 3日相關：0.19
- 近5日 5日相關：-0.07
- 同向比例：+41.18%
- 權重狀態：未調整

- 方向準確度：+41.18%
- 信心排序準確度：0.19
- 診斷：弱正相關

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

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：What a $10,000 Investment Split Between Micron and Sandisk Could Be Worth by the End of 2027 - fool.com；The Zacks Analyst Blog Highlights Seagate, Western Digital, Micron and Sandisk - The Globe and Mail；Sandisk Bets on AI and Enterprise SSDs: Can It Outpace MU & STX? - TradingView

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.57 | +9.69% | N/A | 1,065.11 | 1,080.53 | -1.43% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.28 | -1.36% | -8.33% | 1,729.76 | 2,335.00 | -25.92% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +13.76% | +8.17% | 228.38 | 228.38 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、MU」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：strong。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [What a $10,000 Investment Split Between Micron and Sandisk Could Be Worth by the End of 2027 - fool.com](https://news.google.com/rss/articles/CBMimAFBVV95cUxNZXBybndmNzVRTzFNYVY2dnpJX2l2YTJFOHllZHBtTUs4NVVKOERkVTkwXzZoQjBac05FQkNMZ1lUMzBLaVNyQV9QWGpHX2FLeDU3cUxHVTlRRmpDMFBkaGV4U1p5bTc2cEx6RG9ReDc3UDBMeWdfLVg0b0Z1Q25rcGFXM3owR3M2djJJWGFmZG12STV3RnVNeg?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 30 Sep 2026 12:48:00 GMT
- [The Zacks Analyst Blog Highlights Seagate, Western Digital, Micron and Sandisk - The Globe and Mail](https://news.google.com/rss/articles/CBMi8gFBVV95cUxNYXg4WlpqX0xHMFlpY3MtRXBVaUx1N2gzVUFTZlg1M3dxN0ZKdHk5dExHOEEyUE5CdUNwZjkzWExHWTRvRUlHckV5WThWYmlKZFRrV2NiSmFhckJPMWFCbnZ0RjRMV1l6bUVFU2syUlZhRm5ZXzNxdXFJdzB0WkF3NlUzb2l0NjlsbTJDT01ibzVNUDFLNEJtY1VtczIwMjFaM0EtTWJycThzcmZkUGc1Ykw0OG9GeE13YWNmVjNPcmlUOEhwZzQyZEJyRWk5MHJPWTdELW0yQ0EwSnpGYl9JR2FtWmlpamQtQllJcFRhR29VQQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 29 Sep 2026 08:22:00 GMT
- [Sandisk Bets on AI and Enterprise SSDs: Can It Outpace MU & STX? - TradingView](https://news.google.com/rss/articles/CBMitwFBVV95cUxNSDY2VDU0Skp4LUtKVDJ2bGQ1dnVmZXUxMFRFYVFKX1dBZHBNV01kekRXcnJlV3l6eTdEeGt1MGtyNEFiRHlRZzN3MlRDd1p5ZVRrdU1Gd0Iyd0NkRWZKYXo5TWVZSU5wNGRoZ0lfUzdsaWpEUnE5N1RXY3BtNXB0NTI4U0EyeTlwcUdFbVRHRnJTUGFVT0JWSDRKczFmZzd0M2JnMDdmbXZlNkdEUVhRNm9NM2ZHTzA?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 30 Sep 2026 17:12:00 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel Rises 3% as Chip Contender Caps Off Surprisingly Strong September; NVIDIA Ticks Up, AMD Slips - Yahoo Finance；Intel Rises 3% as Chip Contender Caps Off Surprisingly Strong September; NVIDIA Ticks Up, AMD Slips - 24/7 Wall St.；台股節後重挫392點！聯發科暴跌7％成殺盤重心塑化、功率半導體逆勢爆發- 證券 - 工商時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.57 | +4.84% | N/A | 120.23 | 127.39 | -5.62% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.55 | +13.76% | +8.17% | 228.38 | 228.38 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.55 | +18.54% | N/A | 611.76 | 629.26 | -2.78% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2454 聯發科 | 新聞直接提及 | -0.47 | -5.11% | -1.80% | 5,285.00 | 5,285.00 | 0.00% | 同向 | 60.69 | 81.26 | 64.18B TWD / 44.08% | 2026-09-01 |
| 2330 台積電 | 產業/供應鏈推估 | +0.04 | -0.80% | 0.00% | 2,475.00 | 2,475.00 | 0.00% | 未明確 | 86.28 | 28.75 | 514.81B TWD / 53.32% | 2026-09-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.03 | -3.44% | -1.59% | 154.00 | 164.50 | -6.38% | 背離 | 6.68 | 23.23 | 25.04B TWD / 30.71% | 2026-09-01 |
| MU 美光 | 產業/供應鏈推估 | +0.04 | +9.69% | N/A | 1,065.11 | 1,080.53 | -1.43% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.02 | -1.36% | -8.33% | 1,729.76 | 2,335.00 | -25.92% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：strong。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：strong。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：strong。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Rises 3% as Chip Contender Caps Off Surprisingly Strong September; NVIDIA Ticks Up, AMD Slips - Yahoo Finance](https://news.google.com/rss/articles/CBMimAFBVV95cUxPcFJSR0RRQUNkdFpRNmtLSF9KNVFSWk5pTXhna1JheG5NbXA3Q0lXSmQ3OXgzVzJjVkRQQVhIRExObHlMcHdUaVU4VUltYTFrVy0xT3FsSjdTXzNlWk12b1lpd05TYWJvd21UVGVxV05Rc1l3T0UwRUxfZldzbUM4Q0JWb091UjZac3NuSF9JellQbDFoZFEyVw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 30 Sep 2026 16:29:13 GMT
- [Intel Rises 3% as Chip Contender Caps Off Surprisingly Strong September; NVIDIA Ticks Up, AMD Slips - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi1wFBVV95cUxPbE95RmdDZkVQNDM2REZ0bHd5V3RwdFB3X0M1Z2JVZXFNTVVuVGlrSzlHMkVXNDNteG9jLTVSaXNuSV8wamMybnVyaURocE1HT1dJQ25sZ1JSMEZuSkN5Tnk5eTREN2R6UUF4R3ZwbUc3Q1UzRy1sZnVueXJyQWNBTkYzN01SenI2aV9PeUY5UVNid01tUVN3TmtKVHhfUEkzNDREQUlNNWM2SVBsMDRJSGpxNGJMLTdweURkWEdvdlpEb2xFWTZSaXl5Z0k5eGFlWVBOZ3dVRQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 30 Sep 2026 16:29:00 GMT
- [台股節後重挫392點！聯發科暴跌7％成殺盤重心塑化、功率半導體逆勢爆發- 證券 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE8zd1N3YlNsaHgySEJuRDludy1iWWFjLVhXWllLVVRBYzZPVnlTSE1hdFA0bEx3TnllNXZFYzJKbHFoYzl6eG1TUnRtZmVSemY1d2xuSjFRRDA3RnFmR2U4?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 29 Sep 2026 06:20:00 GMT

## 新興題材：輝達散熱

摘要：新興題材：輝達散熱 相關新聞集中在：焦點股／輝達散熱認證台廠缺席！奇鋐、雙鴻雙雙跌逾5% 健策反創新高| 產經 - 非凡新聞台；奇鋐、雙鴻、健策...輝達散熱夥伴台廠缺席！這2檔跌半根、它反創新高，最新目標價「還有3成甜頭」 - 今周刊

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +13.76% | +8.17% | 228.38 | 228.38 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | -1.01% | +0.59% | 3,555.00 | 3,555.00 | 0.00% | 不適用 | 75.13 | 45.79 | 19.48B TWD / 54.34% | 2026-09-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 3017：新聞直接提及「奇鋐」，共 2 篇新聞命中。

### 主要來源

- [焦點股／輝達散熱認證台廠缺席！奇鋐、雙鴻雙雙跌逾5% 健策反創新高| 產經 - 非凡新聞台](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5ZMkFWNkNjZGNhRy1Ga0tLb3JXbHYxOUlTU2VyZ05Gel96MW5IOUpzRjNmWFBfN3BQY1lOQ1ZRa0tBclJwanB3dFQ0Y0JsNmlMU2RkNWNmQUlSYjRnQXJn?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 30 Sep 2026 12:10:15 GMT
- [奇鋐、雙鴻、健策...輝達散熱夥伴台廠缺席！這2檔跌半根、它反創新高，最新目標價「還有3成甜頭」 - 今周刊](https://news.google.com/rss/articles/CBMigAFBVV95cUxQZVV5eWdBR1ZBUUVtNi15WDc2aElJcVJvRWVCU29LTU1Yc25tLUxGT2FrWVFDRmpkNjdjTmUwSUEtWm1iRmN5Wnh6dFpPM3VURXNmYVNXZnFBU1NESTI3NXFrMERaRWpHNlQ3WVFMbHhkeHNyeF9aNHpRNnVuOE0tQw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 29 Sep 2026 08:04:00 GMT

## 新興題材：OpenAI

摘要：新興題材：OpenAI 相關新聞集中在：Synopsys, OpenAI strike deal to develop AI model for chip design work - Reuters；FTC opens probe into AI giants including Anthropic and OpenAI - Reuters；OpenAI links China’s Moonshot AI to attempt to extract its models’ reasoning - cnbc.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 新聞直接提及 | 0.00 | +13.92% | +4.25% | 512.90 | 512.90 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：新聞直接提及「OpenAI」，共 4 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Synopsys, OpenAI strike deal to develop AI model for chip design work - Reuters](https://news.google.com/rss/articles/CBMiqgFBVV95cUxNSUQ2UF9xa0tYb2VKRTFLNVpwb04xbnJCMld6TWx3Wm1IYTA0V2lXRmFEZC1hRm5zUXNOV3djUUo2SmRHbEFNbWRpMzQ0TFAzUzZGenQ1bEV4eGtkWXdWUnF4bGZmZXprb0lvOHdCcWhZU080QzU1aTl1WVBfR0V3NmNpNFVBM1Z6cWNEaDFFYkQ0eU5MLVdmNjJJTkFCSDg4eElUSUZqZ0Ntdw?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 30 Sep 2026 19:02:09 GMT
- [FTC opens probe into AI giants including Anthropic and OpenAI - Reuters](https://news.google.com/rss/articles/CBMiwgFBVV95cUxQdzYzcTVSY1JmRld3cFRBRlRaX0w0YVZHTjU3NWVvVG5BcXFIZGFwdXViLXBLNnhJQ3d0RS13T2VURWdNQ19ySkJuVXNlV2NWX0E3LUExYUZQaFBsTTVEaC1NMXJtR0RGYlllQVotQmM3VlRaVmd2em04YWdzTXFkMjhsUlQ0b1JlcVJBRENNRFFBT1NLcU00YUtqU0N5LUlJa0YxaEhzdU1mR1lkUTJ0MFhLMjA3a1FJVlQ5RXpMOEIxdw?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 30 Sep 2026 18:17:19 GMT
- [OpenAI links China’s Moonshot AI to attempt to extract its models’ reasoning - cnbc.com](https://news.google.com/rss/articles/CBMidkFVX3lxTE1kSmhrQ0lQOWwyV3JGWWpoclhLX1ZHYm9qX2tOTVRvcms5eUpOUjlrQ2RYdnhlVlJYTUNFelFRWjVkYXpJbVBPTU42amJ3QW5IMDdqYTZzcjVULWxuSjh0OUYyRTV6RG84ZlpLM2NlblNoWHJDdXfSAXtBVV95cUxQSTFoTHRwbXlLVFQtRXNCVlpLblVkRGNiMnN3RjgwVHE5anZvUW1aQlNzTGVGRXJISm9JUGdka1dWUnFEd0Nqc2s1N1d4UldwLUlTNWdCOWxJUFluSVZSTUJzZFhkM3VKNUNLd3cwNjJRa29QbWQ3d0hDN28?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 01 Oct 2026 00:04:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：AI 創造更多工作，卻拆掉職場新手村？新人為何更難入場 - TechNews 科技新報；實體店如何轉型，以對接 AI 導購後的入店體驗？ - TechNews 科技新報；蘋果導入 AI 助理時，如何維持核心的人本服務文化？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AAPL 蘋果 | 新聞直接提及 | -0.21 | +6.72% | +19.43% | 333.02 | 335.92 | -0.86% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 產業/供應鏈推估 | -0.04 | +4.84% | N/A | 120.23 | 127.39 | -5.62% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | -0.03 | +13.76% | +8.17% | 228.38 | 228.38 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | -0.03 | +18.54% | N/A | 611.76 | 629.26 | -2.78% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.04 | -0.80% | 0.00% | 2,475.00 | 2,475.00 | 0.00% | 未明確 | 86.28 | 28.75 | 514.81B TWD / 53.32% | 2026-09-01 |
| MSFT 微軟 | 產業/供應鏈推估 | -0.02 | +13.92% | +4.25% | 512.90 | 512.90 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -9.78% | -21.39% | 351.19 | 446.77 | -21.39% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.02 | +1.44% | +6.03% | 699.00 | 699.00 | 0.00% | 背離 | 13.92 | 50.87 | 82.25B TWD / 45.66% | 2026-09-01 |

關聯理由（前 3）：
- AAPL：新聞直接提及「蘋果」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：衝擊。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：衝擊。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AI 創造更多工作，卻拆掉職場新手村？新人為何更難入場 - TechNews 科技新報](https://news.google.com/rss/articles/CBMilAFBVV95cUxPZWt5cS1EclF3T0gtTUpNSGV1cHVrOU00Ylh5S1ZLLWo3OVdjeWpYSUN0Y2ZXSUswcHAzNUtmX2RXNnF4YjRJU3ZlbDF0UlpjbEozUzcxTGZCWllGZFlCZkVjOXdqZXJlcGFxbURmakFQM0xSdEhPQXBmNHRxdEdIVG9TOVJlUGlyYWZzMHFRMlVWTlg2?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 01 Oct 2026 00:04:51 GMT
- [實體店如何轉型，以對接 AI 導購後的入店體驗？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiswFBVV95cUxNYTlBQ0k3NWtId1hCLVNyLUhvZ2t1NFZtWjhzbF85UlAzeEZPcl95QThyTEtmQTUxWHEwS3FnbGZKeHNKYTVLaDZnajloY1kyeTJnR184dXdXb0R5a2YzV3NPT09MZGRJeUFwT2xONGtJSzdidGZWSE93Tk5oWm9Rbmgyd0pkZE9UcUJqa2tLckR6M3J3T05mOTRnbHE2cHFVN19HRW12UXYzUVBxNFhlbDZVOA?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 30 Sep 2026 21:58:01 GMT
- [蘋果導入 AI 助理時，如何維持核心的人本服務文化？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiswFBVV95cUxQd3hNNzRJTENUUHZyMWVkTTM0SUNRdV9IOEpOMXFDb2tNSHFibFN2VGVMdERQT1N2R19Bd0p2WTlPbndyX0tRaFlVQTlIV2hRWlU4Vm1xR3Q2QlNBa0txYS1WOUxOWS1vekpiS3lpZjRIZzg0V3RXOE1LdTU1YnE3OU9BbGh0N3VkVW5jOWFLdkJLMDhxZ2pUbHcyY2txcEV6dEdmR2swZ0YwLWV1ODZQb1pBVQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 30 Sep 2026 21:58:05 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：焦點股／輝達散熱認證台廠缺席！奇鋐、雙鴻雙雙跌逾5% 健策反創新高| 產經 - 非凡新聞台；奇鋐、雙鴻、健策...輝達散熱夥伴台廠缺席！這2檔跌半根、它反創新高，最新目標價「還有3成甜頭」 - 今周刊；焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | -0.57 | -1.01% | +0.59% | 3,555.00 | 3,555.00 | 0.00% | 同向 | 75.13 | 45.79 | 19.48B TWD / 54.34% | 2026-09-01 |
| NVDA 輝達 | 新聞直接提及 | -0.28 | +13.76% | +8.17% | 228.38 | 228.38 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐、散熱」，共 5 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：跌停。
- NVDA：新聞直接提及「輝達」，共 3 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [焦點股／輝達散熱認證台廠缺席！奇鋐、雙鴻雙雙跌逾5% 健策反創新高| 產經 - 非凡新聞台](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5ZMkFWNkNjZGNhRy1Ga0tLb3JXbHYxOUlTU2VyZ05Gel96MW5IOUpzRjNmWFBfN3BQY1lOQ1ZRa0tBclJwanB3dFQ0Y0JsNmlMU2RkNWNmQUlSYjRnQXJn?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 30 Sep 2026 12:10:15 GMT
- [奇鋐、雙鴻、健策...輝達散熱夥伴台廠缺席！這2檔跌半根、它反創新高，最新目標價「還有3成甜頭」 - 今周刊](https://news.google.com/rss/articles/CBMigAFBVV95cUxQZVV5eWdBR1ZBUUVtNi15WDc2aElJcVJvRWVCU29LTU1Yc25tLUxGT2FrWVFDRmpkNjdjTmUwSUEtWm1iRmN5Wnh6dFpPM3VURXNmYVNXZnFBU1NESTI3NXFrMERaRWpHNlQ3WVFMbHhkeHNyeF9aNHpRNnVuOE0tQw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 29 Sep 2026 08:04:00 GMT
- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 30 Sep 2026 01:23:51 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：法人盤勢分析內容-台股 - MoneyDJ理財網；美股指數期貨最新報價 8:37-台股 - MoneyDJ理財網；《台股盤後》收漲308點/48K未站穩；月K連二紅/季K連六紅-新聞內容-基金 - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [法人盤勢分析內容-台股 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMijgFBVV95cUxQcUYwbEdGeGdObzdsbzBVeWpGSmtfMnhfRTBWajI5czMtaXdKYjBmRzNfTDlXeEtsVDBjUjFUX1h4QVRnZmpuNk5qZkFRQ3ktMGh1MndZYUFTeHJLLVpXanpTTEZOaDJZWV9MMzNKc0l4MmRaclgtSlg4WTUwVDZHNHYzVE9qY2VFRE1TZ2lB?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 01 Oct 2026 00:33:58 GMT
- [美股指數期貨最新報價 8:37-台股 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMiigFBVV95cUxNSDRyQmdqZVpQdmFoYkNPUldQWlhLdjgwX3Jjb3E3NU83bFJIWFpXR3lSTGpJdG56VjAyYVJEdjVSbmFWNTlCaEFpWlBwNmROak9IYkdydXhDdkhabDBJYTNxYXQ3WUU2OXhmSXc5UlYtX2p3RXp3WlpvTGRLZ1FvamZNcllfUHoydnc?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 01 Oct 2026 00:48:17 GMT
- [《台股盤後》收漲308點/48K未站穩；月K連二紅/季K連六紅-新聞內容-基金 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikAFBVV95cUxPME9hTnF3d3VrcVIwbmV1U1ExZW5qbHk0MngxVDMtbzNkdThZaHlrYjRkUVp0S2lqYThXU2xIbDZib2NOQV9xQXJkV3JMMjhsaHVINk52WUtwMnVxMWVIY2lPQmxhYXFZcDFRS3ZPMzdPTnltYWQ5UDVwZVltWlVHR3o2bGlHUXpMRzd0NkxnaEg?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 30 Sep 2026 07:56:00 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：個股動態報導內容-FC48AAD4-B360-4417-B177-787A565F07C4 - MoneyDJ；個股動態報導內容-D0E06F37-5253-4700-A7F0-7D6F0B806D96 - MoneyDJ；個股動態報導內容-6CEB6F3A-5F0A-4C67-85A4-6BC225131C68 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-FC48AAD4-B360-4417-B177-787A565F07C4 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxQUTZFS2tzRnhObmhwNWEyTHpYdnU0RUg1cVNKSmZURkUyT3ZMaVFjMjdORDRZQWNJUlRtNTJDbEVGUVFrNE82X0pLRFV1YTFPWWFpSXo4ZVl5TGhYcFVrY19FVENWUEE4d05lM3ZqZzk4WklDWFBwd1hpNG1pYmRyNGkyTWlKS3lHMnFCQXdvWnV2cVpu?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 30 Sep 2026 10:40:12 GMT
- [個股動態報導內容-D0E06F37-5253-4700-A7F0-7D6F0B806D96 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxOcnVlenUyQlpmMFlZYnU1RTZUYXpZYUZqMUJzVFdQcXRueUxTXzdFSV9YbnJBc0k1QnpQeEpzem5XMThIQTJqODVmM3BON0R4TnJaVmdiVU8wWThlQnVGS19aMkpSb05TbTA3dFFQaGh1dWFOQ1dJQXduTnIyaFZKdDliUk1MSnE1d25SWFZNb0pva285?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 30 Sep 2026 04:54:22 GMT
- [個股動態報導內容-6CEB6F3A-5F0A-4C67-85A4-6BC225131C68 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxNSTdidTh1Z25EMGxoUUk3dzdlTHJxVFBmb1BHOHdyS25HeUNxYkhnakZUTFNWUm5WTjhaNUh3bG9rRVB0dzFUd0pSTHBuQ0o3RGxhdUF1am8yYXd6X0EzWVZuMlVqaHNfSDBraEw2NXFNYW8xSEhkeU1XZUFoUG1oTFRIenpoOGhhWnRYaWgtd0xQdHh2?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 30 Sep 2026 04:54:22 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
