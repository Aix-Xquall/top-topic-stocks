# 每日股市熱門話題分析 - 2026-05-09

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜正向｜熱度 9｜市場確認 100.00｜同向 1/1
2. **散熱與液冷供應鏈**｜負向｜熱度 5｜市場確認 14.33｜同向 1/2
3. **綜合市場情緒**｜正向｜熱度 23｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.21（樣本 3）
- 5日相關係數：0.85（樣本 3）
- 同向比例：2/3

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 100.00 | 1/1 | 0 | +11.09% | +31.62% |
| 散熱與液冷供應鏈 | 14.33 | 1/2 | 1 | -6.89% | +0.58% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-05-08 | 0.03 | 0.48 | +76.92% | 13 |
| 2026-05-09 | 0.21 | 0.85 | +66.67% | 3 |

## 歷史回測摘要

- 回測日期：2026-05-09
- 近5日 3日相關：0.21
- 近5日 5日相關：0.26
- 同向比例：+83.33%
- 權重狀態：已調整

- 方向準確度：+83.33%
- 信心排序準確度：0.21
- 診斷：正相關

調整原因：近 5 日信心分數與後續報酬呈正相關，提高市場確認、歷史題材與直接提及權重。

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

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：INTC, AMD, MU stocks hit 52-week highs today: What's triggering the rally? - MSN；Micron Rockets 11%, SanDisk Rallies 11%, Western Digital Up 3% on AI Memory Supercycle Bull Case - 24/7 Wall St.；Micron Stock vs. Sandisk Stock: One Is a Much Better Buy, According to a Wall Street Analyst - AOL.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.88 | N/A | N/A | 746.81 | 746.81 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.88 | +11.09% | +31.62% | 1,562.34 | 1,562.34 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.65 | N/A | N/A | 455.19 | 455.19 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.65 | N/A | N/A | 124.92 | 124.92 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +23.39% | +12.59% | 215.20 | 215.20 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs, rockets。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk、SNDK」，共 4 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：rally, rockets。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [INTC, AMD, MU stocks hit 52-week highs today: What's triggering the rally? - MSN](https://news.google.com/rss/articles/CBMimANBVV95cUxNWnBwXy11U0pvUXdLcE5sSkpudVFPVVRVRVhCc1RBVEVHdFRFVG1KSWlnWGt0bFo3ZkJNSFlwR2JPNXFkcERmLTJLYXJsTlpGRUZIcjRpOWROVFN2YVU2d1AxY2U1ZldUUk9abDBzN0hyZ0RPZG1KaWh0Y1dmYTcwb3piNzZFWF9zMUdjSWFSVVVndlNPYVpJSjJtNlc4YmZLc3N3cjJtTXNsYU5jQjFGQjA2Z213aUUwRE1nc0J3ZVVNb1Z0TmlnUU9LamRrNjhWR28yM3Q2UjBpZEdQUlJfQTlZQlRycnExTGdiSEZBTmxmUHFPTjMwTFFRR1RqVkZWYmFFTVZUeHBycE9VdndfcWwtTW84YlF6UGVPbGcwdmpzSTVURGxOc21PZ2ZrOFJCQ2NEVG9IY2JZWnF6eng5MDFkemhiNWUwRWpfU243MjF1Vnpuc2FrcWJyMnBWNENhVnVjOHFGQTdEVlJsZ0tSRHYzdzFkel9lZXI1LWhhZlVtTFBYWURBOVdROFVzZzZTRWxBQXlVOVY?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 08 May 2026 09:40:07 GMT
- [Micron Rockets 11%, SanDisk Rallies 11%, Western Digital Up 3% on AI Memory Supercycle Bull Case - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi0AFBVV95cUxNdVdEUVVPNy1QXzdMaF9veS1EWk54NC1FM2VPR2hicTJ1T1pabS1CMTJaN3hMcEJabnFZVVFleHNBNERIQXFtVHZfTnBNbDE1djdNbWlTSXJjb3VmTmU0b0RwdUVjYkwtZ2kzeFUyS0pTQUxYdTJndVRVQ1hLYzg0cmJDUU8wUXBGekxncW9ma3JieG16Nlp6R1luUFJGUm5CVUF2SEQ0VkVkejZGak5zcGd0RkdkdVZHZEVRSHBkU2NRU2szdmV6UlRORFJBeXNZ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 08 May 2026 15:49:24 GMT
- [Micron Stock vs. Sandisk Stock: One Is a Much Better Buy, According to a Wall Street Analyst - AOL.com](https://news.google.com/rss/articles/CBMifkFVX3lxTE5QRzZySzBiVmxvaEZtRXdPa3l0OU9oYzZIWjBHZndTRkhfVk8yRnVxQUpSb3J2eEhid0Z0OVpmQW82S2VGWkFUT0JfTWxIM0RfQWliS3lRcjZsRElGLW80SHo2a0NobkJ2ejNTNlhWSHhyeG1wenpMM0FsdzZpUQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 08 May 2026 17:58:17 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：輝達Rubin傳改散熱設計！投信出貨奇鋐回收25億 「金融股這檔」遭清倉4.3萬張、連挨17刀 - Yahoo股市；散熱三雄遭血洗！Rubin設計變更傳言衝擊，市場不需要散熱了嗎? - CMoney投資網誌；〈焦點股〉市場傳輝達Rubin修改散熱設計 健策再吞跌停 - news.cnyes.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | -0.88 | -9.61% | -13.76% | 2,445.00 | 2,835.00 | -13.76% | 同向 | 49.17 | 49.98 | 15.63B TWD / 71.62% | 2026-05-01 |
| NVDA 輝達 | 新聞直接提及 | -0.38 | +23.39% | +12.59% | 215.20 | 215.20 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐、散熱、3017」，共 5 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：利空, 跌停, 衝擊。
- NVDA：新聞直接提及「輝達」，共 2 篇新聞命中。 方向判斷命中詞：跌停。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [輝達Rubin傳改散熱設計！投信出貨奇鋐回收25億 「金融股這檔」遭清倉4.3萬張、連挨17刀 - Yahoo股市](https://news.google.com/rss/articles/CBMisANBVV95cUxQUVdpczJId3BfUnRFcjBKdXRJcWdUamdfMXo1a1U0aXBpelFKMWcwUHFGWDN6ZktaUWRkRkxJNk5Vek9HbEhSOGlPS21EY25wZkk4Slp1YkFYMDZGZ2Z6d1k2QXZxNjBxTE9YOGxDcGpGdTMyT1RtelVRWjE4Z2lqdjkzRC1XbG91MG5qNFBDSC02cGlRM21oM3NidG1kcXJicTFlTmxKZWY2SkhxVXBhcjVNVUVBWVN5YUx4azhjQmRBZFJ1YlhIRmtsXzVHQ1Bxc0c0eU45cTB2V2hhcWNyR213TENWUkVlblRtNWJ6X1lHNFB6ODg2WmVKT096eERrOXFjVDRLZnlLVFZuTzFEN3dNS0tJdUNkbllQTmNYQ200c25ROHI5dU1HRi1NQ3VTQUZLNlBYc3B1RWJaVXZ4RklNeFBKeGVDNlMzYXRKSTlNRmsyNDRlbmhWZk1NamowWHJ1ZkhIQk5KdGVzS1lIcTBIV2JHSXM2MzgzQnkzR1pnR3FhRzlabFJONGRzVFNxQXNWQ2F3ZDI3dmxYTmRUekMzLUJYejl3NFp5TTllcUo?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 07 May 2026 11:30:00 GMT
- [散熱三雄遭血洗！Rubin設計變更傳言衝擊，市場不需要散熱了嗎? - CMoney投資網誌](https://news.google.com/rss/articles/CBMifkFVX3lxTE9RalFwM2o4STVKZU5iV2wwdlRfMmxwTjF1OXJCd1RGa2pEeDRQcFg1SjIzVUdwWEptUHlrZEs4RlU1MVpPR2wtWUZRVkdXaEZGMVNibl8tUW9CZEV0WnJqamtLODNVazZLSUU5WkJXelNHb2wxMllvT2YwRHZGUQ?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 08 May 2026 08:26:50 GMT
- [〈焦點股〉市場傳輝達Rubin修改散熱設計 健策再吞跌停 - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTFBqMnEwOWsycmg4NUpSbHJmSzJXOWsyaWZOLTRVaDNQNnRZUkxPSEdqX0I5NFA5UVdxSFYzTjZWb0ZuYzVQc3QycjRFTzZjYVU?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 07 May 2026 03:37:34 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：《台股盤後》收跌329點、守5日線，週K翻紅- 新聞 - MoneyDJ理財網；國票證券：台股多方氣勢強盛 - 台股 - 新聞 - MoneyDJ理財網；個股動態報導內容-FD533747-C852-4D42-935F-1F7C3E1C03CC - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》收跌329點、守5日線，週K翻紅- 新聞 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikgFBVV95cUxOZkE2bUJKemtyX1lrWVBUYVFISFA3ZXVSakRDOGh5LXdERVN2aEd6YkdHWXI1Ny1heHlaOXF3NkRMY3I3S21sZzBOTWEwV2puU2RQNDVnLWpyVlNsbzV5YlhxdkhJcmxpUmlDT0FnR3U0UXNYLUxyRmJfOHYtTVpMS19VTkZFWERJY0Y4bkVvN0lKdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 08 May 2026 07:53:00 GMT
- [國票證券：台股多方氣勢強盛 - 台股 - 新聞 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMimwFBVV95cUxNR19kRWFlZVNUYjEzN2dyMUxPRGJYOFduLTlBWFZCbHRTcFJHdk94MkJvMndwNU96SGpoTzh0RmhUcU9qeFdfQS1TMVFENXYydWswTHFkU1Azb3lfUVRocXE3REhObGM3QzM0Sk9Nam1UMDBzMVgtM2ZCRWQycUhBR0ZOMEVFcFFTeU9WekZreU9PM1JIckEzN3Jwbw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 08 May 2026 00:54:00 GMT
- [個股動態報導內容-FD533747-C852-4D42-935F-1F7C3E1C03CC - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilAFBVV95cUxOUXlLWkliRGZlSVFKMkxtUTNBaGl4akVCNWhRTHVqbHlHczQ4VV91MHl1Sms1MDVienBWNmNiZmhsRUsyLXVlMkdnX3pIQmg3QkdGaUt5aGJNaGFLaHR0YnVYZGFMWklWcmgyeEs0Z2NEckk5eHA1WG1YRzRWT2dqTVJGWkZEdDBNZWhSWGFGUVFnMlBk?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 08 May 2026 10:36:36 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
