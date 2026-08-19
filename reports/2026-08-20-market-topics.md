# 每日股市熱門話題分析 - 2026-08-20

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **半導體與晶片供應鏈**｜負向｜熱度 14｜市場確認 59.68｜同向 4/5
2. **AI 伺服器與資料中心**｜中性｜熱度 11｜市場確認 N/A｜同向 0/0
3. **新興題材：台股冷颼颼散熱**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0
4. **新興題材：OpenAI**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
5. **散熱與液冷供應鏈**｜正向｜熱度 5｜市場確認 0.00｜同向 0/1

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.72（樣本 8）
- 5日相關係數：0.06（樣本 8）
- 同向比例：4/8

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 半導體與晶片供應鏈 | 59.68 | 4/5 | 1 | +1.23% | -0.75% |
| AI 伺服器與資料中心 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：台股冷颼颼散熱 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：OpenAI | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | 0.00 | 0/1 | 1 | -4.33% | +6.36% |
| 記憶體與 HBM 供應鏈 | 0.00 | 0/1 | 1 | -4.40% | +16.71% |
| 新興題材：TradingKey | 0.00 | 0/1 | 1 | -16.52% | -7.99% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-08-07 | -0.22 | -0.17 | +50.00% | 8 |
| 2026-08-08 | 0.72 | 0.45 | +62.50% | 16 |
| 2026-08-09 | -0.39 | 0.46 | +71.43% | 7 |
| 2026-08-10 | -0.09 | 0.74 | +71.43% | 7 |
| 2026-08-11 | 0.57 | -0.18 | +54.55% | 11 |
| 2026-08-12 | 0.52 | -0.47 | +87.50% | 8 |
| 2026-08-13 | 0.72 | 0.24 | +100.00% | 7 |
| 2026-08-14 | 0.34 | 0.57 | +92.86% | 14 |
| 2026-08-15 | 0.24 | 0.30 | +68.75% | 16 |
| 2026-08-16 | 0.37 | 0.51 | +70.00% | 10 |
| 2026-08-17 | 0.49 | 0.60 | +66.67% | 12 |
| 2026-08-18 | 0.29 | 0.36 | +80.00% | 10 |
| 2026-08-19 | -0.23 | -0.33 | +30.00% | 10 |
| 2026-08-20 | -0.72 | 0.06 | +50.00% | 8 |

## 歷史回測摘要

- 回測日期：2026-08-20
- 近5日 3日相關：-0.25
- 近5日 5日相關：-0.09
- 同向比例：+50.00%
- 權重狀態：未調整

- 方向準確度：+50.00%
- 信心排序準確度：-0.25
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

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel and AMD Fall 4%, NVIDIA Unchanged as Chip Selloff Defies Bond Yield Relief - 24/7 Wall St.；Intel and AMD Fall 4%, NVIDIA Unchanged as Chip Selloff Defies Bond Yield Relief - AOL.com；Chip stocks fall despite bond yield relief; NVI... - Pluang

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.57 | N/A | N/A | 92.80 | 114.68 | -19.08% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | -0.28 | +8.73% | +9.01% | 217.56 | 219.74 | -0.99% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.56 | N/A | N/A | 466.42 | 516.10 | -9.63% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.05 | -1.88% | -2.69% | 2,350.00 | 2,425.00 | -3.09% | 同向 | 86.28 | 27.24 | 467.58B TWD / 44.69% | 2026-08-01 |
| 2303 聯電 | 產業/供應鏈推估 | -0.05 | -4.55% | -6.10% | 115.50 | 164.50 | -29.79% | 同向 | 6.68 | 17.37 | 23.84B TWD / 18.98% | 2026-08-01 |
| MU 美光 | 產業/供應鏈推估 | -0.04 | N/A | N/A | 937.10 | 971.00 | -3.49% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | -0.04 | -4.40% | +16.71% | 1,568.87 | 2,335.00 | -32.81% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -4.04% | -13.16% | 362.48 | 446.77 | -18.87% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel and AMD Fall 4%, NVIDIA Unchanged as Chip Selloff Defies Bond Yield Relief - 24/7 Wall St.](https://news.google.com/rss/articles/CBMivwFBVV95cUxQY3lCZ2VYblNHNWRSdlBKTERDZ0JQVDFVT2x5WGpwdUNqclVrbEt6cThVQ2ltVmR0YnZZV1NiQWlGbzVCaDVKQ1BVOGJPSFhKajhwR2ZEREh6dFBGX2FMS0xUb3czZ1FfS1JCR3kxbEZ4bXZwVHdIa3FtQVZNd3YtRkNJdGN4X25EMmN5Q3hXbW1hSjZmMUhyeFpJSzloNnFIaDVMeXpvY19DbV9KRE9icFpIeDI3YTNldDVkUEdDUQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 19 Aug 2026 15:34:32 GMT
- [Intel and AMD Fall 4%, NVIDIA Unchanged as Chip Selloff Defies Bond Yield Relief - AOL.com](https://news.google.com/rss/articles/CBMidkFVX3lxTE5WTENHR3kwSGFJTU5nRVFNeXZTcmFFVzhlU2EyYUgyNVZuaUgtVzAzNkhfZ1VsTzFwbFhYX3VQcklhU19jU1FMcndjeHdGN1FNcWQtaUcwVTRsSUltNk9vYjRiRWVpd3lkd05pdXk3X3d1blRBWVE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 19 Aug 2026 15:36:40 GMT
- [Chip stocks fall despite bond yield relief; NVI... - Pluang](https://news.google.com/rss/articles/CBMiqAFBVV95cUxObk9JMGQxT1I2OEpfSjMwMTdmMFRnTE55RWd3T09uQXJfbWFiQXpnanVGNDFncW4xNDgwN0xNcloyV3AzUnhRbzJYUWlxNzNWX05lcUpWVHBOdUpGc0FIbmZ5WUVSVkkyalphQ2hrTUt5WVZka3QweTVwSl80VFNyZW9pZkxvVXA5cEdYTExjTGRZbzFtY0JoSWRsbUY3SDV3c2g4T0RtcjI?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 19 Aug 2026 15:59:45 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel (INTC) Pushes Deeper Into AI Data Centers With Co Packaged Optics - simplywall.st；不再紙上談兵！偲倢科技以 SPAK 營運代理讓 AI 真正接管工廠營運流程 - TechNews 科技新報；隱私保護 AI 對機器人進入長照有何作用？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 92.80 | 114.68 | -19.08% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +8.73% | +9.01% | 217.56 | 219.74 | -0.99% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 466.42 | 516.10 | -9.63% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -1.88% | -2.69% | 2,350.00 | 2,425.00 | -3.09% | 不適用 | 86.28 | 27.24 | 467.58B TWD / 44.69% | 2026-08-01 |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +23.32% | -4.42% | 484.31 | 506.69 | -4.42% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -4.04% | -13.16% | 362.48 | 446.77 | -18.87% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | -4.55% | -5.31% | 588.00 | 680.00 | -13.53% | 不適用 | 13.92 | 42.55 | 73.78B TWD / 43.15% | 2026-08-01 |
| 2454 聯發科 | 產業/供應鏈推估 | 0.00 | -8.67% | -4.23% | 3,845.00 | 4,310.00 | -10.79% | 不適用 | 60.69 | 63.50 | 48.47B TWD / 12.16% | 2026-08-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel (INTC) Pushes Deeper Into AI Data Centers With Co Packaged Optics - simplywall.st](https://news.google.com/rss/articles/CBMiygFBVV95cUxPOENIaEZQcjJmWnBrU2tZenlJQ0FmeU1ralIyNkhHb2l2VUdiU3k3U2R2RWxJdFhGWXpxSTB6eFkxaXZpaklEU2NWWkpITDBKdWZlMnNhWG5IRWtNdWtmQUJGbGxqODNvY0I1ellNOXVqU05ldFROVFh0UFBzTXl4Q0RBclhIaFFsOTlCN20yRW9DajZVZzNoaS00ZXR5Y251RHlKVkN6QnlsN09KZTRhUW1RZGNjRmh4NURRamJQSkVQSGRWSWFpNjVn0gHPAUFVX3lxTE0tZkpBcEJUUFIxeXlfRGpZdF9EUm8yR0hvTEppclhMV3R6LW15eG0yYTRSeUkwYkpmU2RJdXhhc3RFS1l3TkpjUHRsclJreVJRbXc5UTYwM012ZFVPbWV6LXRLV2JPT0pNbm9maXZJSUNTNGlEVWlhVm9yaGc2a2h6SS1GcUVkQ2RCb1hTVzNneGpxM1pzaVlyMm9WNDdTWkZVU2p5TzdnM3Q5VVRtU25MQTFUaUhSOG1YSklDcDRRV0hIZGs2c3hLV0NUVVNoUQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 18 Aug 2026 07:39:44 GMT
- [不再紙上談兵！偲倢科技以 SPAK 營運代理讓 AI 真正接管工廠營運流程 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiV0FVX3lxTE9vbkhpWHNkb19oZzlWbGdQOEkxSkdHbnNEeWdUYkNZUHhpOVZWS25QQWxXYldXQUJPUkxnZHFZVE9JRFFYMjVBMVZhekZrdWtXNFp4RlFQaw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 19 Aug 2026 08:03:34 GMT
- [隱私保護 AI 對機器人進入長照有何作用？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE81Ym40NjVUTThCUERZeElNeGRRYkRFTWk3ZGhobHdydmhaSTY2UnNja3NVSE1NaXFGeWYtaDMtTjU5LUdhOVdoa2hlbmxWUG1DRjZNTEtHbVg1ejc5Tm1tQTg4NER4TlE?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 19 Aug 2026 08:20:31 GMT

## 新興題材：台股冷颼颼散熱

摘要：新興題材：台股冷颼颼散熱 相關新聞集中在：台股冷颼颼散熱股卻發燙！奇鋐一日填息、健策飆逾5% 有何底氣？ - UDN

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | -4.33% | +6.36% | 3,095.00 | 3,095.00 | 0.00% | 不適用 | 75.13 | 41.26 | 18.59B TWD / 57.39% | 2026-08-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐」，共 1 篇新聞命中。

### 主要來源

- [台股冷颼颼散熱股卻發燙！奇鋐一日填息、健策飆逾5% 有何底氣？ - UDN](https://news.google.com/rss/articles/CBMiVkFVX3lxTE5lSzhPNFFIV1J3YmZEZFByc0FGVGsxM3V2Zm0wSE1xbmYwZHI2STRHRlBRY0wxc1VKZEx5TzFwdnU1VGN5NEpvSXNZTGIxRWhfQzFnRk1n?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 19 Aug 2026 03:00:32 GMT

## 新興題材：OpenAI

摘要：新興題材：OpenAI 相關新聞集中在：Stock winners and losers as Anthropic passes OpenAI as hottest AI upstart - CNBC；AI雙雄季報逆轉！WSJ：OpenAI Q2營收僅季增18% 遠低於Anthropic逾140%增速 - news.cnyes.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 新聞直接提及 | 0.00 | +23.32% | -4.42% | 484.31 | 506.69 | -4.42% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：新聞直接提及「OpenAI」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Stock winners and losers as Anthropic passes OpenAI as hottest AI upstart - CNBC](https://news.google.com/rss/articles/CBMirwFBVV95cUxPWmFhYU5mVjhXb0FnQ0NHTk1CMXE1azlabnZiN1pnZVN6aXhqUkdNLTVsMU9DTDJVVWVxVGxVMHFtaGx5QmRNWlc4ODljVnJYOXgxZEpUV1ZrYXBJUFplSXhHeDJKN293TXRUUHh4c1ZkVDFvdFBzSXJ0WXg0OVZVWUJFdVJmUmdlTFB5NjFJV0xQTWloM1lGZEQ4aFFWMDlYRkVFTGxiVDdLYmZCVVYw?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 19 Aug 2026 16:00:07 GMT
- [AI雙雄季報逆轉！WSJ：OpenAI Q2營收僅季增18% 遠低於Anthropic逾140%增速 - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTE5ya2JpM3MtdFhZaFYxaG9iQTRFeTV5V00zekJpWFU4LWJ4WmpPVjJ5Vk8wWmRDbkVaWVRNd044T1NaNkpJeFA5U1l2MUxVQlU?oc=5) - Google News source discovery | 鉅亨網 Wed, 19 Aug 2026 06:30:07 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：健策、巨大 認購突圍 | 權證特區 | 證券 - 經濟日報；台股冷颼颼散熱股卻發燙！奇鋐一日填息、健策飆逾5% 有何底氣？ - UDN；焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.28 | -4.33% | +6.36% | 3,095.00 | 3,095.00 | 0.00% | 背離 | 75.13 | 41.26 | 18.59B TWD / 57.39% | 2026-08-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐、散熱」，共 4 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：跌停, 受惠, 強勁。

### 主要來源

- [健策、巨大 認購突圍 | 權證特區 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5wSXExU3VWOFV0V0l6cXhGSXAxZ2RhNk9vXzlUOHRrcG9kNmw3RmFidTl6V0ZqNEZFSW53ZXBUb1J1cnJQc20wVU5hdDVVMG14eW9yVmRXWWRtQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 19 Aug 2026 16:01:03 GMT
- [台股冷颼颼散熱股卻發燙！奇鋐一日填息、健策飆逾5% 有何底氣？ - UDN](https://news.google.com/rss/articles/CBMiVkFVX3lxTE5lSzhPNFFIV1J3YmZEZFByc0FGVGsxM3V2Zm0wSE1xbmYwZHI2STRHRlBRY0wxc1VKZEx5TzFwdnU1VGN5NEpvSXNZTGIxRWhfQzFnRk1n?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 19 Aug 2026 03:00:32 GMT
- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 19 Aug 2026 02:52:39 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Why Sandisk's 80% Margin Is More Than Just A Cycle Peak - Seeking Alpha；WSJ Report Sends Memory Stocks Down. SanDisk Down 9%, Micron Down 7%, Western Digital Down 5% - AOL.com；Micron down 6%, SK Hynix and SanDisk 5%: why is memory trade crashing? - TradingView

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| SNDK SanDisk | 新聞直接提及 | +0.24 | -4.40% | +16.71% | 1,568.87 | 2,335.00 | -32.81% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 新聞直接提及 | +0.48 | N/A | N/A | 937.10 | 971.00 | -3.49% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +8.73% | +9.01% | 217.56 | 219.74 | -0.99% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- SNDK：新聞直接提及「SanDisk、SNDK」，共 4 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：rally, surges。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- MU：新聞直接提及「Micron、DRAM」，共 3 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Why Sandisk's 80% Margin Is More Than Just A Cycle Peak - Seeking Alpha](https://news.google.com/rss/articles/CBMiowFBVV95cUxObWJpOEdZLWMtdExIRnNjZGFLRXF0bUtVMC1pZ253Y3JNQTJfcmR4eTJfaHJOVkQ4RUhNd2R1Ml9QakRHQ2k3TnM5Q1o3SWcwd0t2U2FPVEdlaU9sX051N2JOWG1rS2FqUmh4S3p3U05tZ194aWhCb0NNM0hmRTlhWl9LZnA3aWhjQUJ5T05sMDlTTlNGQlZ0ZjFYM1ZoUi1YODIw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 19 Aug 2026 12:00:00 GMT
- [WSJ Report Sends Memory Stocks Down. SanDisk Down 9%, Micron Down 7%, Western Digital Down 5% - AOL.com](https://news.google.com/rss/articles/CBMif0FVX3lxTFB5NDdMby01OWUyWFhOYXI2WkV0eW9ZTFFybVQxb0dkZ0FzcU5WWDlHcnhjY2xpMDVSUWRJNVRBcEhHemV1TXlyVGY4ZURYSnpNMzV5czJhLW9xOHlUTkFrdmNFb29IWnc0WC1SczNCMU1PRlhVdkI3ZW92aWdmaFU?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 18 Aug 2026 17:08:28 GMT
- [Micron down 6%, SK Hynix and SanDisk 5%: why is memory trade crashing? - TradingView](https://news.google.com/rss/articles/CBMivwFBVV95cUxPYTEyVm5odUtKcllPM1BxWWNwZHdQMlNEOFM4YnJ0Y29iNDdCWUh5b1gxTmo5QWttb19sSm9ISWFtOTU1NlJCaXBMX1VOWG0zM0JtWjlabEtsNlRTc20tZUlLaGVzNzZOTHBNU3RXcGt0eTQ2eUM0MzBqRV9jLVY5R2RYR3FDRzFrN2xwbkVvcXBCWHhRN1BNRzE5WVJIbDdGdWNmTHFOUkZDN1lMTUc0WDBmUUEtRHp3U05vUGRLVQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 18 Aug 2026 09:59:22 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Intel Q2 $16.1B Beat: $20B Capital Raise, Foundry 14A Tesla Deal, Agentic AI CPU Demand - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.42 | N/A | N/A | 92.80 | 114.68 | -19.08% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| TSLA 特斯拉 | 新聞直接提及 | +0.21 | -16.52% | -7.99% | 351.12 | 456.56 | -23.09% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 方向判斷命中詞：raise。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- TSLA：新聞直接提及「Tesla」，共 1 篇新聞命中。 方向判斷命中詞：raise。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Q2 $16.1B Beat: $20B Capital Raise, Foundry 14A Tesla Deal, Agentic AI CPU Demand - TradingKey](https://news.google.com/rss/articles/CBMi-gFBVV95cUxPZTFRUWM4emwybjRpTEdrNWp0eHJRVHVTNTZSSWtIZVFoRWZqbTlkSWxaV3V0SzZqVVpGOFVKNnVVNlRtd19tWUVBMThHNWxlLWpWMU1xeE96WDNOMS03dDdEdW1BRTBYOG1iTm5Ec0xQdFZFa0FYMHktenVETXFxUHNseWVtamt2M1pheWdYUlRfRHQwSm8wM3gyOFFQdkh4cWpNWWEzSkhtV0ItczNsRlVrZnRabUlBc0dyVUFRNlVCc2hBbFJteE80M0xKdUE4Z1ZZMVdKYW85dWhOWTIwZ1MyUUcxbFdCQ2ZNX0VGWUQ0ajAzSnR3TEZ3?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 19 Aug 2026 06:43:46 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：《台股盤後》收跌589點、日K連二黑，失守季線- 新聞 - moneydj.com；台股ETF受益人數連兩周降溫 4檔反1逆勢增 - 新聞 - moneydj.com；《台股盤後》收跌589點、日K連二黑，失守季線-新聞內容-基金 - moneydj.com

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》收跌589點、日K連二黑，失守季線- 新聞 - moneydj.com](https://news.google.com/rss/articles/CBMikgFBVV95cUxQckE1WkdXOVMzcWVqSXh3QTRSY0UwN0hiTnFZTkhrUlFyOWswaEdjMVNxYW5oZGdfbFo5Y0dGSDFHRDdwcENRNjRTV3BwWUtUdDJUaWlsT1V4UGtaSXMxSW5QQWt4dGxLa3RHWlVTeVNSdGY0ZHBMUUFBNmhIYllrYU9Ya0FNUkVfazhRMEdQbU8wQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 19 Aug 2026 08:09:00 GMT
- [台股ETF受益人數連兩周降溫 4檔反1逆勢增 - 新聞 - moneydj.com](https://news.google.com/rss/articles/CBMikgFBVV95cUxQSjI2cE5VV01BWmtMTkRmNnlqajV0bU80WFBMZEE4VTFQNER6X1hnZ2xnWHdBSnN4ME54VkQ1X2JiM1ZyUEFTR1l4eENlZWhKSGJ0YUlMb0R3b3duc2JRNkFDcVhkNEJUTTB5TW5jb0F1S3pvdXJCdDczTEl1X0ZWak1HS1VLREIzRkNNbjQzUmZidw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 19 Aug 2026 03:31:00 GMT
- [《台股盤後》收跌589點、日K連二黑，失守季線-新聞內容-基金 - moneydj.com](https://news.google.com/rss/articles/CBMikAFBVV95cUxPV2tsNDV5WkpGQzFhdWdSeDNZM185YlE4VmFLWmVkVjhWZ05RRGpVb3o4ZS1jS25EdFgzUnZ4QndDUU1wYnM3ZWFHYVhHNTRGc0I4V3pMYng2ZVBRMzNLTmo4RE5LTkN4VTZ5Nk96UThEUXEwSnRuMFFVV0hkV1lOZTlqRThSalhTcWdmX01tZ0o?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 19 Aug 2026 08:13:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
