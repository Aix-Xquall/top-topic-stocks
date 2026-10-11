# 每日股市熱門話題分析 - 2026-10-11

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **新興題材：台積電法說**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0
2. **記憶體與 HBM 供應鏈**｜中性｜熱度 4｜市場確認 N/A｜同向 0/0
3. **新興題材：TradingKey**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
4. **半導體與晶片供應鏈**｜中性｜熱度 5｜市場確認 N/A｜同向 0/0
5. **AI 伺服器與資料中心**｜負向｜熱度 18｜市場確認 10.34｜同向 2/5

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.66（樣本 5）
- 5日相關係數：-0.74（樣本 3）
- 同向比例：2/5

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 新興題材：台積電法說 | N/A | 0/0 | 0 | N/A | N/A |
| 記憶體與 HBM 供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：TradingKey | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 10.34 | 2/5 | 3 | -5.89% | -6.35% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MarketVector | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
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
| 2026-10-11 | 0.66 | -0.74 | +40.00% | 5 |

## 歷史回測摘要

- 回測日期：2026-10-11
- 近5日 3日相關：0.42
- 近5日 5日相關：-0.74
- 同向比例：+40.00%
- 權重狀態：未調整

- 方向準確度：+40.00%
- 信心排序準確度：0.42
- 診斷：正相關

調整原因：近 5 日有效樣本 10 筆，低於 15 筆門檻，暫不調整權重。

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

## 新興題材：台積電法說

摘要：新興題材：台積電法說 相關新聞集中在：南亞科、台積電法說接力登場 誰是台股衝上5萬點推手？ - 經濟日報；法人：台積電法說會15日登場有助支撐台股高檔整理| 證券 - 中央社 CNA；南亞科、台積電法說接力登場 誰是台股衝上5萬點推手？ - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | 0.00 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | 29.56 | N/A TWD / N/A | N/A |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 3 篇新聞命中。

### 主要來源

- [南亞科、台積電法說接力登場 誰是台股衝上5萬點推手？ - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1pcE1nRkIxQkNMOEF5MTZNMldiUTYtc1VPUFVaU2JhS29yRWpTSWRSRnhOa1ZBTjBUTno5R1h2V1hUNEpaenRXdUw0WTdGMzNKZE5iczJndmxVQdIBX0FVX3lxTE8yRXQ3V1dlVWVHZWd1em9Yd0k0N2FJd0RiaHJZcnpwMld3eTRTa0xQNEZ5Zjh5MWl1ZjFOWGFBVU45RHY4T0JubExBejEzUjdCcFhSOUQ5NWh3SlFKVi13?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 10 Oct 2026 17:35:09 GMT
- [法人：台積電法說會15日登場有助支撐台股高檔整理| 證券 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE4wdm4zWkh6Y1piZG05bXJ2VTVFcGxoc3JDam84dWQzOGQzc3JGTWVGR2pTcWtUZUN1alZxcFJQQXBVLVIwaTBRUHJwRlFheV84dXRJR3R1UEZPbm1qVmc?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 09 Oct 2026 06:40:00 GMT
- [南亞科、台積電法說接力登場 誰是台股衝上5萬點推手？ - 經濟日報](https://news.google.com/rss/articles/CBMigwFBVV95cUxNeHRhcVJZd0g1cmhwVHE5MEtNdzUxbW43ZXdKSl9KV1pMb2QwTFBPSlBGeFlaaW9LN1A1b0F4UzBqVk41elJxc1pOMHliN2tHTHl5Ykd0SkFSUDBNRlRRbHcycnFSdEFvZV9rbzBuRHRvUlRnR2hIMEZSRUJfQmhKV2NkMNIBX0FVX3lxTE8yRXQ3V1dlVWVHZWd1em9Yd0k0N2FJd0RiaHJZcnpwMld3eTRTa0xQNEZ5Zjh5MWl1ZjFOWGFBVU45RHY4T0JubExBejEzUjdCcFhSOUQ5NWh3SlFKVi13?oc=5) - Google News source discovery | 經濟日報 money Sat, 10 Oct 2026 17:35:09 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Not Micron. Not Sandisk. This Memory Stock Is Quietly Gaining Share. - Yahoo Finance；Not Micron. Not Sandisk. This Memory Stock Is Quietly Gaining Share. - The Motley Fool；Micron Technology Inc (MU) Stock Analysis & Forecast - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | +5.97% | N/A | 1,029.00 | 1,029.00 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | -4.74% | -8.03% | 1,581.82 | 2,335.00 | -32.26% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +3.85% | +14.59% | 229.28 | 229.28 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、MU」，共 4 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Not Micron. Not Sandisk. This Memory Stock Is Quietly Gaining Share. - Yahoo Finance](https://news.google.com/rss/articles/CBMimgFBVV95cUxQX1dlbFdXRmIyM0xuXzlkWGROM0VXb3NDSEJpcm4xVTJLazlMYnpqb3Ytdlh5THY5NXA1Uy1JcEVfaHpBQjZONlozSW1WOGVRMXlUdzR3TDBna25wWFN3LW1mS3UtUXhOQjZWMkh6LTFRcVdUaEF1Tmc5SUdiNThSbnVpWmxDZ2VhX050em9MYWpRR2lmdl9hLWV3?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 09 Oct 2026 16:00:00 GMT
- [Not Micron. Not Sandisk. This Memory Stock Is Quietly Gaining Share. - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxPSFlZeUJQU0hxYXhwUC1jdWtaRU5id19uWDFxbzdKRzdRQ3h4bmdEekIzblVncS1FYU1CUW5jUE9vVEZpcDFzU2JnaUJVcndJaFh1XzUtbWo0MFhjN1diSEkxY1lxQkVRQjFwb05NZ0tCaWk4RF9DV015QVpNZV8tNGxremd5ZW8wZ3lIMjc5RWNJR25zMGRGSg?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 09 Oct 2026 16:40:00 GMT
- [Micron Technology Inc (MU) Stock Analysis & Forecast - TradingKey](https://news.google.com/rss/articles/CBMiY0FVX3lxTFB2cjlJNEFoZnN6al9fVWlOSktTV2tWRzJ1c0c2SklreGhaeHF5VlZlSjNNRE1SaXlnaUVsQ1FaMXFtZUlvM19kUzhHdURNU1VkNmNhLTNPSDNtXzBpSHNZS0xkNA?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 10 Oct 2026 02:56:02 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Micron Technology Inc (MU) Stock Analysis & Forecast - TradingKey；Memory Stocks Rebound Across the Board as Micron, SanDisk and SK Hynix Gain Over 2% - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | +5.97% | N/A | 1,029.00 | 1,029.00 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | -4.74% | -8.03% | 1,581.82 | 2,335.00 | -32.26% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。

### 主要來源

- [Micron Technology Inc (MU) Stock Analysis & Forecast - TradingKey](https://news.google.com/rss/articles/CBMiY0FVX3lxTFB2cjlJNEFoZnN6al9fVWlOSktTV2tWRzJ1c0c2SklreGhaeHF5VlZlSjNNRE1SaXlnaUVsQ1FaMXFtZUlvM19kUzhHdURNU1VkNmNhLTNPSDNtXzBpSHNZS0xkNA?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 10 Oct 2026 02:56:02 GMT
- [Memory Stocks Rebound Across the Board as Micron, SanDisk and SK Hynix Gain Over 2% - TradingKey](https://news.google.com/rss/articles/CBMi2AFBVV95cUxOMUJZMnd4M1FIOUU3NU5fQmQxOGFnVlk1VDFNaWQyVHVhNFQySmhVN281NXRFcE4zSjBsY2puTkFUOGZjNUNRWDIzYXMtWkp4dTVzbUVOQm1sVWRLOG91WU5sSjFacDV5SURHSnhpbnV3aURGUGo5MU1hWmcxbVJuX0JuNUh2bkVkNnFDN1BKNEdxMTJNVHZ4d1pPajlna3AxYnhhUkR6cWxlakIxZlNLWG54eUlzakVCRTlxMkdWT1dfUlRGR2x4LXZVNkV0N3lPUG9sMldZSFo?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 09 Oct 2026 09:04:49 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：INTC, AMD, AVGO: Chip Stocks Jump Premarket After Nvidia's Blowout Report - Stocktwits；駐匈代表：台匈合作潛力升溫看好AI與半導體業布局| 國際 - 中央社 CNA；外交部：歐洲議會報告籲歐盟與台灣強化半導體等領域合作| 政治 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | -8.70% | N/A | 104.70 | 114.68 | -8.70% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +3.85% | +14.59% | 229.28 | 229.28 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | +17.83% | N/A | 608.10 | 608.10 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | 0.00 | -2.38% | -4.29% | 361.54 | 446.77 | -19.08% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | 29.56 | N/A TWD / N/A | N/A |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | 22.18 | N/A TWD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | +5.97% | N/A | 1,029.00 | 1,029.00 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -4.74% | -8.03% | 1,581.82 | 2,335.00 | -32.26% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [INTC, AMD, AVGO: Chip Stocks Jump Premarket After Nvidia's Blowout Report - Stocktwits](https://news.google.com/rss/articles/CBMizwFBVV95cUxPQUU4dTZXYndUX2YwZlZ6VmR6d3JoV2dDbE1XR1FKS0p2YTZScmlIclZkTUxxb0paRW00TEgwVlE1Qk5hT3BnM3J4eVZqVDBpZ3o1blFiYTQ5M2t3OTlJU3pud01kVlJYQzFVaF82a2xfWXRfM2R2MzBVRDczX0pnRkpPZ3dpam03QlhibkliRnQ3NWhJU25VM0d1bVlvSm02bjJaV2pjZlJwTUpVVnZCMHRxYjFFd2Q2RXRNOFl3ZkItc0llS0JKR2dVN1VORDg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 10 Oct 2026 07:54:55 GMT
- [駐匈代表：台匈合作潛力升溫看好AI與半導體業布局| 國際 - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBCdHpIS09SUzc3NFZRa2Z1dTlRMVFaMWs5V0xRQU1HY0ozV0p5S0lhSW1sb1pvNXlkd1NTY0RVVlBSVVAwckx4Q25ZcEJQQjZVSjVqdmt6ZHg4YUthbjJj?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 10 Oct 2026 13:37:00 GMT
- [外交部：歐洲議會報告籲歐盟與台灣強化半導體等領域合作| 政治 - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9rTjlWQU5zN1VHTEMxbFdQaklDNHdIYmxfMEkweHdUeVo1dmwzcElYU0MzY0NmdmtTX2R3cU12NHZVR3VHZVdRenVab3BjVU52OWlaNm95TXByREpvSk93?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 09 Oct 2026 05:19:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Is Terafab AI Role Altering The Investment Case For Intel (INTC)? - Simply Wall Street；可調整推理程度的功能，將如何改變企業開發 AI 代理的邏輯？ - TechNews 科技新報；Anthropic 大幅降價對 AI 模型市場價格戰有何長期影響？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.54 | -8.70% | N/A | 104.70 | 114.68 | -8.70% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | -0.03 | +3.85% | +14.59% | 229.28 | 229.28 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | -0.03 | +17.83% | N/A | 608.10 | 608.10 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.06 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | 29.56 | N/A TWD / N/A | N/A |
| MSFT 微軟 | 產業/供應鏈推估 | -0.02 | +18.84% | +8.75% | 535.07 | 535.07 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -2.38% | -4.29% | 361.54 | 446.77 | -19.08% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.04 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | 53.84 | N/A TWD / N/A | N/A |
| 2454 聯發科 | 產業/供應鏈推估 | -0.04 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | 77.46 | N/A TWD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：恐。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：恐。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：恐。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Is Terafab AI Role Altering The Investment Case For Intel (INTC)? - Simply Wall Street](https://news.google.com/rss/articles/CBMiygFBVV95cUxOcGtldWVQWjNZUWJ6c0NFU3hVay1iOThiWUZxckhMeFlUVW1CeTdNalVvMTE1bVMzVGp5QWpORGprMmZPWG5PTGtZNnpwSnFBemx2SzJqY0NVLWEySV9lR2Via2RNV2pHT1dSS0liTkxlT2Zma2ZCclFBSTkzNlZYdWgwelYwWGVQVU9OOVpHV2k5LUhTMlBkRHNaSXBXbFlWbWRnaUlLUUtxRDE4WjlVSTFDVHRUai1ZMEptcHViZUdiWE1kdklQbXdR0gHPAUFVX3lxTE1UdnBWNW5aQU5pQjhaamF5UkgwOE5LRFI4V2JTc3ZrN2tiZjVBeXBiMkkwQUUwMU5iZW9VTHY3b2xveDBqWWlLYUNuZmw0M1FWd1ZNN3N5WE1pUFIwOVBIZVNldnU0bVQ2MzYtNHIxN2puWHVaUHUwRFZNQXRRLVdObzgxOGdXZWhVWXc2TzlYRFRaQk9UTkxjZnlFbzhtem9qTmtEdzExVEpmMktlbTNiYWlQd1ptNFNFYkVnUXVYTm1PS1BxcHpadnFLZ1dDOA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 10 Oct 2026 08:40:44 GMT
- [可調整推理程度的功能，將如何改變企業開發 AI 代理的邏輯？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMib0FVX3lxTE9wN0JVOVJFbncwM1RqXzIyMVpEQ3BQT0p2OU9HZnR1dkZXenJ3MWJQbXJKSl9TSHdYQjg4WHFmcmhfOFZtSWhxZWdESnRIdjBqb2p3ZG9Hdi1rZWxFUlJHVXlSbWI2QUUyUHFDVXZKcw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 10 Oct 2026 16:32:59 GMT
- [Anthropic 大幅降價對 AI 模型市場價格戰有何長期影響？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMib0FVX3lxTE9HVVhEelF1T2k4WUlWbXA2SUFCUjRkU3AybGhMeExXT3B1cEdjV3N0d0o5ZUJvS053ZFBHSUMyZG8zU0dfOHQ3Ukg2Z1RCOVRLZHAyUmk3b1NROFJISUhqWHV1bktNVTFram5rYUlWMA?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 10 Oct 2026 16:25:30 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：個股動態報導內容-13BFA797-BD5C-4F4C-B41C-2F575E2353A3 - MoneyDJ理財網；個股動態報導內容-9E94BE75-F504-4FEC-9C2D-8704A8E703C2 - MoneyDJ理財網；台新-大裕 對 彰銀(2801)個股 單一券商歷史明細 - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-13BFA797-BD5C-4F4C-B41C-2F575E2353A3 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilAFBVV95cUxPYTdvTW9JUWdJeVppMTdKQ05HNkF6V1J2WVVQejRpWE5mOFo4Q0xYOE8tTlBTNHF2MW9pQWdNekp2TVhsQVd5amdHaEt2cjBwNVpsY21ZQkRJdkdjanozVFpNaFJWblVVM294TTdWTVBXckVuYUgzdXI2aWpJdXV1SjFjQk5pYWdPMEpsWmh0MXkzZ2Jt?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 09 Oct 2026 10:43:37 GMT
- [個股動態報導內容-9E94BE75-F504-4FEC-9C2D-8704A8E703C2 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilAFBVV95cUxNVWFMdC1qSXlzcFVMcmJMZlNsZnlBMHpCdjZxdGw3VFc0SmJ5aElDbElFSVRaVURDTDZvSW15cVNHNDI5WEl5UldudkdISFhSVnIzRDN1Zy02S3VRbGpkMnRjaHVNUldnQno0bDMyS0NIcHZiZ2hQdXlFbE9oX21IYWFUQm1zMW1qMjJYMWd4YnpLNURj?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 09 Oct 2026 10:28:33 GMT
- [台新-大裕 對 彰銀(2801)個股 單一券商歷史明細 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikwFBVV95cUxPSXlpeHl1QlZPYzktOFpJcHNvdml1ZVBXVHNGSzdWZDUyWk02RmpBcG5lS0dCZTFHV2VFR0gtRU50cHg5YzVSamRBaG9rdTlhRUNCczRwTWxTOTBRYkJTV1FWR2ZMU0RaSUJpQnBReUFBVHhUWlJOc0xnRm45c2w4QllKUjBCUU9QX2JVbFJYZEdueG8?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 09 Oct 2026 13:36:51 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：最新專欄分析 - MoneyDJ；泰金寶-DR自結9月合併營收6.45億美元，年增16.6% - MoneyDJ；鎰勝 115年9月營收7.41億、年增14.53% - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [最新專欄分析 - MoneyDJ](https://news.google.com/rss/articles/CBMieEFVX3lxTE5McmhrLUd0Ymo0TmVhaWRYVURuTFVJWW1WZFVibkp5OG4yVWV5bUV0ZHlKZHAxdEdVQ25EbXpvQTFyckhCVHBnZDlHWXJ5c05HTjhVVnpTRHlDS3ZaQmhYQ3E4akVodTRaM3Fsbk9pcWdJdG1HcGJXdQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 09 Oct 2026 07:00:00 GMT
- [泰金寶-DR自結9月合併營收6.45億美元，年增16.6% - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQcFFDc3Q3dHpUTlF4Q3BPMk12b1c4dkJVb05rVW95d0xybU1mb1VoYmNYVUxOdlRvZW1kUGdJd3I1ckZFVUdRNmd3VTgyTHhiNEFOTGJZTU5wWFpmRDVPcXJvUWJSUWZ1LVFYclRBYnBjVDV4QUIzeTh4SWNCTGRXWjh2cnVJYzByQnhncDRGQlNhUQ?oc=5) - Google News source discovery | MoneyDJ Sat, 10 Oct 2026 23:38:00 GMT
- [鎰勝 115年9月營收7.41億、年增14.53% - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNemFNazE1ZkpkTGp6RF9fc2Rqdm9ZR3BSVkNjSjlXbjR2Qm9DSUFmVjJVekJRalVtS09ESmxfekowd3N6VDNNZDVLSGhxS1VjWEgtSGxTcFBVMkFVLU5Dek45cGxkUlhQbXlvTWZKRDFseWM2dUJaYjEwYWZaMzlrUXExbVJDQ2N4enZ0ZFFxdFJSUQ?oc=5) - Google News source discovery | MoneyDJ Sat, 10 Oct 2026 17:49:00 GMT

## 新興題材：MarketVector

摘要：新興題材：MarketVector 相關新聞集中在：MarketVector 攜手 Paragon 將旗艦半導體基準指數引入鏈上 - 中央社 CNA

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [MarketVector 攜手 Paragon 將旗艦半導體基準指數引入鏈上 - 中央社 CNA](https://news.google.com/rss/articles/CBMiVkFVX3lxTE8tUU5JU3E5S0lRd1FLVUNVLXVPT3cyWVdNVU92WkpPN0RQalBYdHp0dDlNVFZhSHVRSTBqRkpTLTRURlB0Zng1RDV1SWo4c18zQVo1TnBn?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 10 Oct 2026 09:35:36 GMT

## 資料缺口與需人工確認

- FinMind 月營收抓取失敗：2303，原因：HTTP Error 402: Payment Required
- FinMind 月營收抓取失敗：2330，原因：HTTP Error 402: Payment Required
- FinMind 月營收抓取失敗：2454，原因：HTTP Error 402: Payment Required
- FinMind 月營收抓取失敗：3711，原因：HTTP Error 402: Payment Required
- FinMind 綜合損益表抓取失敗：2303，原因：HTTP Error 402: Payment Required
- FinMind 綜合損益表抓取失敗：2330，原因：HTTP Error 402: Payment Required
- FinMind 綜合損益表抓取失敗：2454，原因：HTTP Error 402: Payment Required
- FinMind 綜合損益表抓取失敗：3711，原因：HTTP Error 402: Payment Required
- FinMind 股價抓取失敗：2303，原因：HTTP Error 402: Payment Required
- FinMind 股價抓取失敗：2330，原因：HTTP Error 402: Payment Required
- FinMind 股價抓取失敗：2454，原因：HTTP Error 402: Payment Required
- FinMind 股價抓取失敗：3711，原因：HTTP Error 402: Payment Required
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
