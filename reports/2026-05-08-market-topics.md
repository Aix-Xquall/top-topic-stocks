# 每日股市熱門話題分析 - 2026-05-08

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜正向｜熱度 8｜市場確認 83.47｜同向 1/1
2. **散熱與液冷供應鏈**｜負向｜熱度 10｜市場確認 14.49｜同向 1/2
3. **半導體與晶片供應鏈**｜正向｜熱度 1｜市場確認 100.00｜同向 5/5
4. **AI 伺服器與資料中心**｜正向｜熱度 2｜市場確認 68.84｜同向 3/5
5. **綜合市場情緒**｜正向｜熱度 23｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.03（樣本 13）
- 5日相關係數：0.48（樣本 13）
- 同向比例：10/13

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 83.47 | 1/1 | 0 | +4.49% | +23.79% |
| 散熱與液冷供應鏈 | 14.49 | 1/2 | 1 | -6.83% | +0.64% |
| 半導體與晶片供應鏈 | 100.00 | 5/5 | 0 | +15.10% | +17.76% |
| AI 伺服器與資料中心 | 68.84 | 3/5 | 1 | +8.95% | +9.00% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 相關性偏弱；應提高同向價格確認權重，降低泛 AI、泛半導體等寬標籤推估權重。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-05-08 | 0.03 | 0.48 | +76.92% | 13 |

## 歷史回測摘要

- 回測日期：2026-05-08
- 近5日 3日相關：0.04
- 近5日 5日相關：0.25
- 同向比例：+88.89%
- 權重狀態：已調整

- 方向準確度：+88.89%
- 信心排序準確度：0.04
- 診斷：低相關

主要錯誤來源（高信心但報酬不佳）：

- AI 伺服器與資料中心｜3711 日月光投控｜信心 0.73｜3日 -0.77%｜未明確

調整原因：近 5 日信心分數與股價關係偏低，提高價格確認，降低寬題材推估。

## 參考來源

| 類別 | 平台 | 用途 | 讀取方式 |
| --- | --- | --- | --- |
| 官方資料 | [公開資訊觀測站（MOPS）](https://mops.twse.com.tw/) | 財報、月營收、重大訊息、年報、法說資料 | 人工核對 / 後續可擴充自動抓取 |
| 官方資料 | [臺灣證券交易所（TWSE）](https://www.twse.com.tw/zh/trading/historical/stock-day.html) | 上市股價、成交資訊、本益比、殖利率、法人與交易統計 | 已部分自動抓取 |
| 官方資料 | [櫃買中心（TPEx）](https://www.tpex.org.tw/zh-tw/mainboard/trading/info/stock-pricing.html) | 上櫃、興櫃行情、歷史行情、注意股、券商買賣資料 | 人工核對 / 後續可擴充自動抓取 |
| 看盤＋新聞 | [Yahoo 奇摩股市](https://tw.stock.yahoo.com/) | 個股報價、個股新聞、自選股、行事曆、類股整理 | 已加入 RSS |
| 財經新聞 | [鉅亨網](https://news.cnyes.com/news/cat/tw_stock_news) | 台股即時新聞、個股新聞、盤後整理 | 已加入 RSS |
| 財經新聞 | [MoneyDJ 理財網](https://www.moneydj.com/kmdj/common/listnewarticles.aspx?a=X0200000&svc=NW) | 個股情報、台股即時新聞、產業新聞 | Google News RSS 備援 |
| 財經新聞 | [經濟日報 money](https://money.udn.com/money/cate/5590) | 證券新聞、即時財經、產業與法人觀點 | Google News RSS 備援 |
| 圖表分析 | [TradingView](https://tw.tradingview.com/markets/stocks-taiwan/market-movers-all-stocks/) | K 線圖、技術分析、財務欄位、股票篩選 | 人工核對 / 圖表參考 |

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：INTC, AMD, MU stocks hit 52-week highs today: What's triggering the rally? - MSN；MU vs. SNDK: Which AI Memory Stock Offers Better Value After the AI Rally? - TipRanks；Sandisk vs Micron: Which Stock Has a Better Chance of Continuing Its Magical Run? - TIKR.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.86 | N/A | N/A | 708.64 | 708.64 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.86 | +4.49% | +23.79% | 1,469.44 | 1,469.44 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.63 | N/A | N/A | 433.63 | 433.63 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.63 | N/A | N/A | 116.13 | 116.13 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +23.28% | +12.49% | 215.00 | 215.00 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK、SanDisk」，共 4 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [INTC, AMD, MU stocks hit 52-week highs today: What's triggering the rally? - MSN](https://news.google.com/rss/articles/CBMimANBVV95cUxNWnBwXy11U0pvUXdLcE5sSkpudVFPVVRVRVhCc1RBVEVHdFRFVG1KSWlnWGt0bFo3ZkJNSFlwR2JPNXFkcERmLTJLYXJsTlpGRUZIcjRpOWROVFN2YVU2d1AxY2U1ZldUUk9abDBzN0hyZ0RPZG1KaWh0Y1dmYTcwb3piNzZFWF9zMUdjSWFSVVVndlNPYVpJSjJtNlc4YmZLc3N3cjJtTXNsYU5jQjFGQjA2Z213aUUwRE1nc0J3ZVVNb1Z0TmlnUU9LamRrNjhWR28yM3Q2UjBpZEdQUlJfQTlZQlRycnExTGdiSEZBTmxmUHFPTjMwTFFRR1RqVkZWYmFFTVZUeHBycE9VdndfcWwtTW84YlF6UGVPbGcwdmpzSTVURGxOc21PZ2ZrOFJCQ2NEVG9IY2JZWnF6eng5MDFkemhiNWUwRWpfU243MjF1Vnpuc2FrcWJyMnBWNENhVnVjOHFGQTdEVlJsZ0tSRHYzdzFkel9lZXI1LWhhZlVtTFBYWURBOVdROFVzZzZTRWxBQXlVOVY?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 08 May 2026 09:40:07 GMT
- [MU vs. SNDK: Which AI Memory Stock Offers Better Value After the AI Rally? - TipRanks](https://news.google.com/rss/articles/CBMiowFBVV95cUxQcmVHSDlESW52SGpZT1JUbzhiWk1ESmNxVk1pYmpaU3ZzWTd6OUZEanFtcjZjU3VNZmpPZU1Hd2p0MXktdS04Sm1WYVg2ckhPWnFxOThHZ3A2SGhPb004VkdRejdtWWI5RWFkM1J1ZUdzVUFDSWY0NVVtTmF6TGc2UU84ZHNvT203OF9yY09xNWRRVFdJYVA3Y05XY2xxVC1jejlr?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 08 May 2026 13:15:29 GMT
- [Sandisk vs Micron: Which Stock Has a Better Chance of Continuing Its Magical Run? - TIKR.com](https://news.google.com/rss/articles/CBMiqAFBVV95cUxPOEpuY2xIYjFtU2dUcl9XWnlrNHdPLU1EQTMzVUFld01fQVBoMVJZQTFYU2xra05NRGNaeEFBZUZBbVFtQmZCeE9Yb21DOEt6NEI4cUJXb3NBT1o0V1dqSDRCQTEtVWtLLVcxMVkzd1J3OWJGYWwtMHpSZjBsTHhRRklaWjdMeThDLTZEVUtxeEFmNUlCbGxRRHZKc3F4MTRBd0VjM1dfazY?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 07 May 2026 16:08:20 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：輝達Rubin散熱遇瓶頸！奇鋐、健策同摜跌停 投信連砍「這檔」2刀收回近100億元 - Yahoo股市；輝達Rubin驚傳規格大閹割！散熱三雄慘遭血洗拆解奇鋐、健策背後致命一擊- 財經 - 中時新聞網；輝達Rubin傳改散熱設計！投信出貨奇鋐回收25億 「金融股這檔」遭清倉4.3萬張、連挨17刀 - Yahoo股市

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | -0.86 | -9.61% | -13.76% | 2,445.00 | 2,835.00 | -13.76% | 同向 | 49.17 | 49.37 | 15.63B TWD / 71.62% | 2026-05-01 |
| NVDA 輝達 | 新聞直接提及 | -0.43 | +23.28% | +12.49% | 215.00 | 215.00 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐、散熱」，共 6 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：改單片, 均熱片, 跌停, 暴跌, 衝擊。
- NVDA：新聞直接提及「輝達」，共 5 篇新聞命中。 方向判斷命中詞：改單片, 均熱片, 跌停, 暴跌。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [輝達Rubin散熱遇瓶頸！奇鋐、健策同摜跌停 投信連砍「這檔」2刀收回近100億元 - Yahoo股市](https://news.google.com/rss/articles/CBMi4wJBVV95cUxNbktLV0ZneVliZk5rS2xQNG9GSVlkZ2NyV0x5N3FDYWlyRlhJcjktak9XV2xLYy13RGIyWGdESDNqbmJhOVpGWEZmZDE0SUFOS1hKdWRrZy04Y2FIYkpKaGVXTkl4UWYtaGNtUEdudjBrVEVDUHgwNS1QNDZoV242bjB2MV85QmpkVVZQdFJPVWhjVzlVaURweGpHMGNDWXc4dzZ4VzZzUW5jcWNrdGh4R0tNVEJ0U2dOZ09wMklqcTNmYWphLUJERWQzdEpUcXRvOFRxY3lkR0Y1QTVXWVFrVGwwUFZpXzRhSmdtNkhFLXR0Q2FYT3pCcVZRM1YxTEpZZjV1b0dUeGNUeHozNHpwZnl5TjJCMkRPcnNEaEg0THRQOE9sNmlsc1A3UTA2QmxxNzUtb2dzc0RRQmhIYnhWMkRiVXhpWVBYaUxTUGFmZlBHYjVWdTdGME9senhpbzhlbTlN?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 06 May 2026 11:30:00 GMT
- [輝達Rubin驚傳規格大閹割！散熱三雄慘遭血洗拆解奇鋐、健策背後致命一擊- 財經 - 中時新聞網](https://news.google.com/rss/articles/CBMibkFVX3lxTE1Qejc0cFVHeTJ1QTZ5LVhFR1JibUdnZE9rMU96TnBWY2Vzenlqa2ZjWWJNTlJVZlM3eEtReXhxNmwyYWVJSnpmSERmVy1BXzdhamRhaGVMaUwzWlJKdDBvc05faUFxVVV5VHFsOC1B?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 06 May 2026 05:35:06 GMT
- [輝達Rubin傳改散熱設計！投信出貨奇鋐回收25億 「金融股這檔」遭清倉4.3萬張、連挨17刀 - Yahoo股市](https://news.google.com/rss/articles/CBMisANBVV95cUxQUVdpczJId3BfUnRFcjBKdXRJcWdUamdfMXo1a1U0aXBpelFKMWcwUHFGWDN6ZktaUWRkRkxJNk5Vek9HbEhSOGlPS21EY25wZkk4Slp1YkFYMDZGZ2Z6d1k2QXZxNjBxTE9YOGxDcGpGdTMyT1RtelVRWjE4Z2lqdjkzRC1XbG91MG5qNFBDSC02cGlRM21oM3NidG1kcXJicTFlTmxKZWY2SkhxVXBhcjVNVUVBWVN5YUx4azhjQmRBZFJ1YlhIRmtsXzVHQ1Bxc0c0eU45cTB2V2hhcWNyR213TENWUkVlblRtNWJ6X1lHNFB6ODg2WmVKT096eERrOXFjVDRLZnlLVFZuTzFEN3dNS0tJdUNkbllQTmNYQ200c25ROHI5dU1HRi1NQ3VTQUZLNlBYc3B1RWJaVXZ4RklNeFBKeGVDNlMzYXRKSTlNRmsyNDRlbmhWZk1NamowWHJ1ZkhIQk5KdGVzS1lIcTBIV2JHSXM2MzgzQnkzR1pnR3FhRzlabFJONGRzVFNxQXNWQ2F3ZDI3dmxYTmRUekMzLUJYejl3NFp5TTllcUo?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 07 May 2026 11:30:00 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：AMD stock soars on Q1 earnings beat, better-than-expected outlook amid strong AI chip demand - Yahoo Finance

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AMD 超微 | 新聞直接提及 | +0.69 | N/A | N/A | 433.63 | 433.63 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 產業/供應鏈推估 | +0.21 | N/A | N/A | 116.13 | 116.13 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.12 | +1.78% | +7.26% | 2,290.00 | 2,310.00 | -0.87% | 同向 | 66.26 | 34.87 | 410.73B TWD / 17.50% | 2026-05-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.12 | +9.87% | +18.11% | 91.30 | 96.50 | -5.39% | 同向 | 4.00 | 24.25 | 22.66B TWD / 10.80% | 2026-05-01 |
| NVDA 輝達 | 產業/供應鏈推估 | +0.09 | +23.28% | +12.49% | 215.00 | 215.00 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | +0.09 | N/A | N/A | 708.64 | 708.64 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.09 | +4.49% | +23.79% | 1,469.44 | 1,469.44 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.09 | +36.10% | +27.15% | 421.24 | 421.24 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：strong。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 CPU, server CPU, x86, foundry；其中 1 篇新聞出現相關標籤。 方向判斷命中詞：strong。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 1 篇新聞出現相關標籤。 方向判斷命中詞：strong。

### 主要來源

- [AMD stock soars on Q1 earnings beat, better-than-expected outlook amid strong AI chip demand - Yahoo Finance](https://news.google.com/rss/articles/CBMi8AFBVV95cUxOQ21TU0pxOWJ5c1NYbHY2R3RLYklyU2dxRU5LcjQ5VmRRQlptR1poSHAwSjdXRVprMC04OTg0N29HbEtpbk9RcjN0Y1V3ckFlLVpIeTFVLU4yMWdGTVc1eEZNUVFZV19WOVNnN2NOUlZEU21oaEdBN2hNM0ZKNG4xRWNiZWFUVzFNakotVDlFWHE0bEJ4aTZMMk5KTlFvVDFFWVJUNnMwWk9YZE9mamctRG9UNHpsbDFsakNweGhKODVIbWE5ajI5YlVwdFp1b29sYzBrcGlva1h1Nl9UaFZ1TkJaQy05cWFZVE8xdnZhVEE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 06 May 2026 20:21:30 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：AMD's Stock Soars to a Fresh Record as AI Demand Drives Up Sales - Investopedia；AMD stock soars on Q1 earnings beat, better-than-expected outlook amid strong AI chip demand - Yahoo Finance

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AMD 超微 | 新聞直接提及 | +0.86 | N/A | N/A | 433.63 | 433.63 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 產業/供應鏈推估 | +0.19 | N/A | N/A | 116.13 | 116.13 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.15 | +23.28% | +12.49% | 215.00 | 215.00 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.14 | +1.78% | +7.26% | 2,290.00 | 2,310.00 | -0.87% | 同向 | 66.26 | 34.87 | 410.73B TWD / 17.50% | 2026-05-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.05 | -15.66% | -9.86% | 414.98 | 506.69 | -18.10% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.10 | +36.10% | +27.15% | 421.24 | 421.24 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.08 | -0.77% | +7.95% | 516.00 | 540.00 | -4.44% | 未明確 | 9.37 | 58.13 | 61.58B TWD / 14.57% | 2026-04-01 |
| 3017 奇鋐 | 產業/供應鏈推估 | 0.00 | -9.61% | -13.76% | 2,445.00 | 2,835.00 | -13.76% | 不適用 | 49.17 | 49.37 | 15.63B TWD / 71.62% | 2026-05-01 |

關聯理由（前 3）：
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。 方向判斷命中詞：strong。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 2 篇新聞出現相關標籤。 方向判斷命中詞：strong。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 2 篇新聞出現相關標籤。 方向判斷命中詞：strong。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AMD's Stock Soars to a Fresh Record as AI Demand Drives Up Sales - Investopedia](https://news.google.com/rss/articles/CBMiogFBVV95cUxQRlU4VHdmV2FZWjh5S09ma1JDZHpFYWJ0b09tYW9kNkVfM0liOHhDNjB0dWdlOS1xVC1keElxdWJOWEdlWl9mQjNSb21uNklzNEdueFU1RlpBb2VsX0llSUR0VDBCUXNaWmZpRnZRYXdzNjVPbzA2dWNqdlZNbGFBbEd2S1F4aHhaMng1MTZUWUpYTWZTR3ZaM01RYjFnNlF1YkE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 06 May 2026 16:59:17 GMT
- [AMD stock soars on Q1 earnings beat, better-than-expected outlook amid strong AI chip demand - Yahoo Finance](https://news.google.com/rss/articles/CBMi8AFBVV95cUxOQ21TU0pxOWJ5c1NYbHY2R3RLYklyU2dxRU5LcjQ5VmRRQlptR1poSHAwSjdXRVprMC04OTg0N29HbEtpbk9RcjN0Y1V3ckFlLVpIeTFVLU4yMWdGTVc1eEZNUVFZV19WOVNnN2NOUlZEU21oaEdBN2hNM0ZKNG4xRWNiZWFUVzFNakotVDlFWHE0bEJ4aTZMMk5KTlFvVDFFWVJUNnMwWk9YZE9mamctRG9UNHpsbDFsakNweGhKODVIbWE5ajI5YlVwdFp1b29sYzBrcGlva1h1Nl9UaFZ1TkJaQy05cWFZVE8xdnZhVEE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 06 May 2026 20:21:30 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：《台股盤後》收跌329點、守5日線，週K翻紅- 新聞 - MoneyDJ理財網；國票證券：台股多方氣勢強盛 - 台股 - 新聞 - MoneyDJ理財網；統一證券：台股技術面為強勢多方格局- 新聞 - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》收跌329點、守5日線，週K翻紅- 新聞 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikgFBVV95cUxOZkE2bUJKemtyX1lrWVBUYVFISFA3ZXVSakRDOGh5LXdERVN2aEd6YkdHWXI1Ny1heHlaOXF3NkRMY3I3S21sZzBOTWEwV2puU2RQNDVnLWpyVlNsbzV5YlhxdkhJcmxpUmlDT0FnR3U0UXNYLUxyRmJfOHYtTVpMS19VTkZFWERJY0Y4bkVvN0lKdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 08 May 2026 07:53:00 GMT
- [國票證券：台股多方氣勢強盛 - 台股 - 新聞 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMimwFBVV95cUxNR19kRWFlZVNUYjEzN2dyMUxPRGJYOFduLTlBWFZCbHRTcFJHdk94MkJvMndwNU96SGpoTzh0RmhUcU9qeFdfQS1TMVFENXYydWswTHFkU1Azb3lfUVRocXE3REhObGM3QzM0Sk9Nam1UMDBzMVgtM2ZCRWQycUhBR0ZOMEVFcFFTeU9WekZreU9PM1JIckEzN3Jwbw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 08 May 2026 00:54:00 GMT
- [統一證券：台股技術面為強勢多方格局- 新聞 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikgFBVV95cUxOZWFwc0tkTF9MRHlMM0VCbUE4dkZsNzdhRFAyS3JRTTk4OHBFcVlhRXZCWERKeVNBNFl2b3BuTXFGcnJyakVBcjJ1eXJlaVVlMGlqUmticklRdWRhUXhTNS10U3I3bWN6WUJiMEstTTNGYjg2N2xuTWFHeGNtbmRFd21KSEZBSF9tTVN5d2hSMFVaUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 08 May 2026 00:54:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
