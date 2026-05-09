# 每日股市熱門話題分析 - 2026-05-09

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜正向｜熱度 13｜市場確認 100.00｜同向 1/1
2. **半導體與晶片供應鏈**｜中性｜熱度 4｜市場確認 N/A｜同向 0/0
3. **關稅與供應鏈轉移**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
4. **先進封裝與 CoPoS**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
5. **AI 伺服器與資料中心**｜負向｜熱度 10｜市場確認 0.00｜同向 1/6

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.03（樣本 9）
- 5日相關係數：0.51（樣本 9）
- 同向比例：3/9

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 100.00 | 1/1 | 0 | +11.09% | +31.62% |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 關稅與供應鏈轉移 | N/A | 0/0 | 0 | N/A | N/A |
| 先進封裝與 CoPoS | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 0.00 | 1/6 | 4 | -10.46% | -14.47% |
| 新興題材：輝達Rubin傳改散熱 | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | 14.33 | 1/2 | 1 | -6.89% | +0.58% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-05-08 | 0.03 | 0.48 | +76.92% | 13 |
| 2026-05-09 | -0.03 | 0.51 | +33.33% | 9 |

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

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：INTC, AMD, MU stocks hit 52-week highs today: What's triggering the rally? - MSN；Micron Has The Better Scarcity, Sandisk Has The Hotter Trade (NASDAQ:SNDK) - Seeking Alpha；Micron Rockets 11%, SanDisk Rallies 11%, Western Digital Up 3% on AI Memory Supercycle Bull Case - 24/7 Wall St.

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
- SNDK：新聞直接提及「SNDK、SanDisk」，共 5 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：rally, rockets。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [INTC, AMD, MU stocks hit 52-week highs today: What's triggering the rally? - MSN](https://news.google.com/rss/articles/CBMi5AFBVV95cUxQY3pZd0tYdUNGcG1tSnlLYzFoUGVhRkxycG1NV05QUEE1X1dxSF9GdG4zSU1DQ0k1T2EzZHZudXBXeUZmZ2lqWVB0MW0zaC1nSGUxOW83bHpUNmNFZTQyUTVnbGZOTENteEZoeEtnVjI4S1NIMm95aC12OW8ySmhLSzlZaGhrTHhiVVEzTW9pYXg4YUl3QjVsTUt5VV92WHBOOXRxN0t6X2p0bnI4REY3d1I0VWpwMC0ySzktNl9NWlotZ0ZUeWp3TTU4NFJoS1Nock5uemxfTWFGWld2R0JJNG5yNkM?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 07 May 2026 04:32:29 GMT
- [Micron Has The Better Scarcity, Sandisk Has The Hotter Trade (NASDAQ:SNDK) - Seeking Alpha](https://news.google.com/rss/articles/CBMiogFBVV95cUxPd0ZFd1h0S2xPWDdWWFBOcnR1cmFWU3JqTllFQ1h2aGVQajA3dG9MeTJ4WU1xZHhqVWtXNi1wZlVWOUhGRm1LUURfUGV3dXZWX0RHbEZzWXBpMmowMWpVd1RyeXQxR0VkSjlZaUpYcUx4NVBCUkh1bDN4dFdUdlJjem9sTlRYcGpiOFpQSnNKMGZoUjVQY1IwdnlZbnozM1ItRXc?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 09 May 2026 10:51:53 GMT
- [Micron Rockets 11%, SanDisk Rallies 11%, Western Digital Up 3% on AI Memory Supercycle Bull Case - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi0AFBVV95cUxNdVdEUVVPNy1QXzdMaF9veS1EWk54NC1FM2VPR2hicTJ1T1pabS1CMTJaN3hMcEJabnFZVVFleHNBNERIQXFtVHZfTnBNbDE1djdNbWlTSXJjb3VmTmU0b0RwdUVjYkwtZ2kzeFUyS0pTQUxYdTJndVRVQ1hLYzg0cmJDUU8wUXBGekxncW9ma3JieG16Nlp6R1luUFJGUm5CVUF2SEQ0VkVkejZGak5zcGd0RkdkdVZHZEVRSHBkU2NRU2szdmV6UlRORFJBeXNZ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 08 May 2026 15:49:24 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：How High Is Donald Trump’s 10% INTC Stake After the Apple-Intel Chip-Making Deal? - Coinpaper；Intel (INTC) Stock Hits All-Time Highs After Apple Chip Deal Breaks Through - MEXC Exchange；半導體擺脫「週期」束縛？高盛看多南韓股市 KOSPI目標上看9000點 - news.cnyes.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 124.92 | 124.92 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 新聞直接提及 | 0.00 | +5.19% | +46.04% | 293.32 | 293.32 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +1.78% | +7.26% | 2,290.00 | 2,290.00 | 0.00% | 不適用 | 66.26 | N/A | 410.73B TWD / 17.50% | 2026-05-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +9.87% | +18.11% | 91.30 | 91.30 | 0.00% | 不適用 | 4.00 | N/A | 22.66B TWD / 10.80% | 2026-05-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +23.39% | +12.59% | 215.20 | 215.20 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 455.19 | 455.19 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 746.81 | 746.81 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | +11.09% | +31.62% | 1,562.34 | 1,562.34 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AAPL：新聞直接提及「Apple」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 2 篇新聞出現相關標籤。

### 主要來源

- [How High Is Donald Trump’s 10% INTC Stake After the Apple-Intel Chip-Making Deal? - Coinpaper](https://news.google.com/rss/articles/CBMiqwFBVV95cUxPZkszQjl5OEtwZ1BfUXgyb2VVZEo5UGYxU3VGa0tmTTl5S0l2Rzd4S3BBQlJ2Rk9sQXVIZGMzOVZWY3RwSDU2QWlGZWg4ajVxMk9mRGJGR25vUF9BZ1k1OFVOV3lkUmlaNk9PdnRjbWFqRnhFVXdEY1FGVWFyNGZIdG5rY2tYUTFzdEU2TE1KUExXWjJnaGI5emJ4NEx4MWpfaVBmTzRmU1NBcDQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 09 May 2026 12:12:39 GMT
- [Intel (INTC) Stock Hits All-Time Highs After Apple Chip Deal Breaks Through - MEXC Exchange](https://news.google.com/rss/articles/CBMiR0FVX3lxTE1JaGFRNl9nQWRoSjZBeFJhZmNSdnZsbHUyMWd6eXd2eFpvdDJYQU9pc0djN1lrVkZhR0RjY0Z4NlZWMmNNNVow?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 08 May 2026 20:24:09 GMT
- [半導體擺脫「週期」束縛？高盛看多南韓股市 KOSPI目標上看9000點 - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTE5LV01UNW5LT0tUNFd3dXkyOG5hQUpIZnZNeG1XTElSZVAxOUM2YVoxbnoxdEU0a090eEJHQWIyZXJ2YjZOei1WUlB0WmlrT3M?oc=5) - Google News source discovery | 鉅亨網 Sat, 09 May 2026 06:00:05 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：駐馬代表：台馬半導體供應鏈互補拓展區域市場| 產經 - 中央社 CNA；AI晶片引爆N3應用占比衝40% 法人看好3利多點火台股供應鏈 - news.cnyes.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +5.19% | +46.04% | 293.32 | 293.32 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | +4.38% | +13.90% | 250.00 | 257.50 | -2.91% | 不適用 | 13.60 | N/A | 832.10B TWD / 29.74% | 2026-05-01 |

關聯理由（前 3）：
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [駐馬代表：台馬半導體供應鏈互補拓展區域市場| 產經 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE5Ta2I0emx3Z0M3UkRfcm9RaE51NTBFQlR1V1FKR2ZBY1R3N0lFTjhMYXlyWEZhLUMyaEE4anJmdnltWDlwUGY4QUg0UWc3bldIMXMtcmdnV3ZES2lGM0E?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 08 May 2026 07:01:00 GMT
- [AI晶片引爆N3應用占比衝40% 法人看好3利多點火台股供應鏈 - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTFBFQ0pwY3NKOXFCc010ajZpci1SSGdsU3Q3NXJtTl9NTFRNaVRQTzVjbHU2NTY4YUJEeFZlaUZDcWRPeFNoV3Bma3hQcm5iYnc?oc=5) - Google News source discovery | 鉅亨網 Sat, 09 May 2026 03:51:13 GMT

## 先進封裝與 CoPoS

摘要：先進封裝與 CoPoS 相關新聞集中在：日月光攜手楠梓電擴廠打造先進封裝產能新據點- 產業 - 工商時報；產品線都漲價，這檔半導體今年營收季季高，擁FCBGA+FOPLP，從280元拉回到222被低估了嗎？ - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3711 日月光投控 | 新聞直接提及 | 0.00 | -0.77% | +7.95% | 516.00 | 516.00 | 0.00% | 不適用 | 9.37 | N/A | 62.25B TWD / 19.22% | 2026-05-01 |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +1.78% | +7.26% | 2,290.00 | 2,290.00 | 0.00% | 不適用 | 66.26 | N/A | 410.73B TWD / 17.50% | 2026-05-01 |

關聯理由（前 3）：
- 3711：新聞直接提及「日月光、FOPLP」，共 2 篇新聞命中。 同時符合主題標籤：advanced packaging, CoPoS, FOPLP, panel-level packaging。
- 2330：產業/供應鏈推估：公司標籤符合「先進封裝與 CoPoS」關鍵字 advanced packaging, CoWoS, CoPoS, FOPLP；其中 1 篇新聞出現相關標籤。

### 主要來源

- [日月光攜手楠梓電擴廠打造先進封裝產能新據點- 產業 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9MMWxVY0Fyek5VdlFVSXF3QUMydm5nU1NpeDd3aHdxV1RFc240WlpMRFJiLXJ6Yi10bUNHcEF6ZWJZaGVYOWZURFJkcWUyMlp2Q3JFUjZwTjYydWNkY1Q4?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 08 May 2026 06:59:00 GMT
- [產品線都漲價，這檔半導體今年營收季季高，擁FCBGA+FOPLP，從280元拉回到222被低估了嗎？ - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9rN0JOZUZmSE9iUk80VVlUYktiMkZOOXNuQmlzb21HVVptUEdJYnk4NWdXSlE5M0FxUGt0Z3RMdHRWWlFoT2xkbW9UTjd0UHJKSGtDSHhFZndmd9IBX0FVX3lxTE1iWWJ3MWdBZHROQkEtekhkc0hydEluMS1fU0hYN0VTc2hJX2E5VG1oNFBWM0FIN1RucEpYbk5mT09hVGNNOEVOODJqWWMzOGlMQ3hvbDFfRFpDMW1oMW5n?oc=5) - Google News source discovery | 經濟日報 money Fri, 08 May 2026 15:35:33 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：賓大數學創新如何挑戰現有 AI 算力擴張趨勢？ - TechNews 科技新報；Replit 靠「非工程師」市場大賺 90% 毛利，揭開 AI 獲利的生存密碼 - TechNews 科技新報；S&P 500 and Nasdaq notch records, boosted by AI and earnings optimism - Reuters

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | -0.42 | +23.39% | +12.59% | 215.20 | 215.20 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 產業/供應鏈推估 | -0.22 | N/A | N/A | 124.92 | 124.92 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | -0.17 | N/A | N/A | 455.19 | 455.19 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.09 | +1.78% | +7.26% | 2,290.00 | 2,290.00 | 0.00% | 背離 | 66.26 | N/A | 410.73B TWD / 17.50% | 2026-05-01 |
| MSFT 微軟 | 產業/供應鏈推估 | -0.12 | -15.63% | -9.83% | 415.12 | 506.69 | -18.07% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.06 | +38.93% | +29.79% | 430.00 | 430.00 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.09 | -0.77% | +7.95% | 516.00 | 516.00 | 0.00% | 未明確 | 9.37 | N/A | 62.25B TWD / 19.22% | 2026-05-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.06 | +15.06% | +39.08% | 3,630.00 | 3,630.00 | 0.00% | 背離 | 66.17 | N/A | 46.74B TWD / -4.14% | 2026-05-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。 方向判斷命中詞：cut。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：cut。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：cut。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [賓大數學創新如何挑戰現有 AI 算力擴張趨勢？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMimgFBVV95cUxPMzJUTUN3MXJDS1RaOVR6bmdNWEREaEQ0SWJWS0R2THdiMnNBTk1vV2xDRXB2NDVJN2pndWhTRG80clVqQnBFUWhXLS03ekZ5U2plXy1qQ2tOc0dTNC0zQ2ZidWJxNFQ3TWNPd1VUQ2dZSG4xanM4S1R2amlRb0w4SGZ6M0hwRjZNQ3hCcGhXZmRuN0NxZTE5Mk9B?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 09 May 2026 10:54:36 GMT
- [Replit 靠「非工程師」市場大賺 90% 毛利，揭開 AI 獲利的生存密碼 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiqgFBVV95cUxQWV9kUzhMSVFrNFdvaWgwQ3dTZzVOYWwwQ0pLQTV4RTNUR1VCZlYweGRtbldDcjB4bVpNbEMtZElIOUdQSnVUVkJaZTV5eHNYQmk4ejJwdHhVLUp6TEJOQXJLZ0g1SUFvZE12RkpTakYwaXhmZTR4cDR0R0FQQnEtaG5iT1kzOFZvdHFtdXJBazcxRWc2TE1SUTZZazkxeG41LTdFZS1mZThOQQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 09 May 2026 03:07:10 GMT
- [S&P 500 and Nasdaq notch records, boosted by AI and earnings optimism - Reuters](https://news.google.com/rss/articles/CBMinAFBVV95cUxOOGVILXcwU3hObHYzalJvRDNUTDVJS0pXNnR6QjVtNXhtTTNSclRlejJYRjRiX2pJcmlOMGVBdzZvOUdzNWg1aV9GQVdWdzBOUUVEX3NaaGhTcHlyNEJEcFlVOHJGWnJWVlZNZHNnMC0wQ0ZPZmRxMTZYdGF4T1MwcDdLcUM4Q0xyNzJJRHVyUlJUT0lKM21leFU5dVc?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 08 May 2026 23:26:47 GMT

## 新興題材：輝達Rubin傳改散熱

摘要：新興題材：輝達Rubin傳改散熱 相關新聞集中在：輝達Rubin傳改散熱設計！投信出貨奇鋐回收25億 「金融股這檔」遭清倉4.3萬張、連挨17刀 - Yahoo股市

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +23.39% | +12.59% | 215.20 | 215.20 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | -9.61% | -13.76% | 2,445.00 | 2,835.00 | -13.76% | 不適用 | 49.17 | N/A | 15.63B TWD / 71.62% | 2026-05-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 3017：新聞直接提及「奇鋐」，共 1 篇新聞命中。

### 主要來源

- [輝達Rubin傳改散熱設計！投信出貨奇鋐回收25億 「金融股這檔」遭清倉4.3萬張、連挨17刀 - Yahoo股市](https://news.google.com/rss/articles/CBMisANBVV95cUxQUVdpczJId3BfUnRFcjBKdXRJcWdUamdfMXo1a1U0aXBpelFKMWcwUHFGWDN6ZktaUWRkRkxJNk5Vek9HbEhSOGlPS21EY25wZkk4Slp1YkFYMDZGZ2Z6d1k2QXZxNjBxTE9YOGxDcGpGdTMyT1RtelVRWjE4Z2lqdjkzRC1XbG91MG5qNFBDSC02cGlRM21oM3NidG1kcXJicTFlTmxKZWY2SkhxVXBhcjVNVUVBWVN5YUx4azhjQmRBZFJ1YlhIRmtsXzVHQ1Bxc0c0eU45cTB2V2hhcWNyR213TENWUkVlblRtNWJ6X1lHNFB6ODg2WmVKT096eERrOXFjVDRLZnlLVFZuTzFEN3dNS0tJdUNkbllQTmNYQ200c25ROHI5dU1HRi1NQ3VTQUZLNlBYc3B1RWJaVXZ4RklNeFBKeGVDNlMzYXRKSTlNRmsyNDRlbmhWZk1NamowWHJ1ZkhIQk5KdGVzS1lIcTBIV2JHSXM2MzgzQnkzR1pnR3FhRzlabFJONGRzVFNxQXNWQ2F3ZDI3dmxYTmRUekMzLUJYejl3NFp5TTllcUo?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 07 May 2026 11:30:00 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：輝達Rubin傳改散熱設計！投信出貨奇鋐回收25億 「金融股這檔」遭清倉4.3萬張、連挨17刀 - Yahoo股市；散熱三雄遭血洗！Rubin設計變更傳言衝擊，市場不需要散熱了嗎? - CMoney投資網誌；〈焦點股〉市場傳輝達Rubin修改散熱設計 健策再吞跌停 - news.cnyes.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | -0.88 | -9.61% | -13.76% | 2,445.00 | 2,835.00 | -13.76% | 同向 | 49.17 | N/A | 15.63B TWD / 71.62% | 2026-05-01 |
| NVDA 輝達 | 新聞直接提及 | -0.38 | +23.39% | +12.59% | 215.20 | 215.20 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐、散熱、3017」，共 4 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：跌停, 衝擊。
- NVDA：新聞直接提及「輝達」，共 2 篇新聞命中。 方向判斷命中詞：跌停。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [輝達Rubin傳改散熱設計！投信出貨奇鋐回收25億 「金融股這檔」遭清倉4.3萬張、連挨17刀 - Yahoo股市](https://news.google.com/rss/articles/CBMisANBVV95cUxQUVdpczJId3BfUnRFcjBKdXRJcWdUamdfMXo1a1U0aXBpelFKMWcwUHFGWDN6ZktaUWRkRkxJNk5Vek9HbEhSOGlPS21EY25wZkk4Slp1YkFYMDZGZ2Z6d1k2QXZxNjBxTE9YOGxDcGpGdTMyT1RtelVRWjE4Z2lqdjkzRC1XbG91MG5qNFBDSC02cGlRM21oM3NidG1kcXJicTFlTmxKZWY2SkhxVXBhcjVNVUVBWVN5YUx4azhjQmRBZFJ1YlhIRmtsXzVHQ1Bxc0c0eU45cTB2V2hhcWNyR213TENWUkVlblRtNWJ6X1lHNFB6ODg2WmVKT096eERrOXFjVDRLZnlLVFZuTzFEN3dNS0tJdUNkbllQTmNYQ200c25ROHI5dU1HRi1NQ3VTQUZLNlBYc3B1RWJaVXZ4RklNeFBKeGVDNlMzYXRKSTlNRmsyNDRlbmhWZk1NamowWHJ1ZkhIQk5KdGVzS1lIcTBIV2JHSXM2MzgzQnkzR1pnR3FhRzlabFJONGRzVFNxQXNWQ2F3ZDI3dmxYTmRUekMzLUJYejl3NFp5TTllcUo?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 07 May 2026 11:30:00 GMT
- [散熱三雄遭血洗！Rubin設計變更傳言衝擊，市場不需要散熱了嗎? - CMoney投資網誌](https://news.google.com/rss/articles/CBMifkFVX3lxTE9RalFwM2o4STVKZU5iV2wwdlRfMmxwTjF1OXJCd1RGa2pEeDRQcFg1SjIzVUdwWEptUHlrZEs4RlU1MVpPR2wtWUZRVkdXaEZGMVNibl8tUW9CZEV0WnJqamtLODNVazZLSUU5WkJXelNHb2wxMllvT2YwRHZGUQ?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 08 May 2026 08:26:50 GMT
- [〈焦點股〉市場傳輝達Rubin修改散熱設計 健策再吞跌停 - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTFBqMnEwOWsycmg4NUpSbHJmSzJXOWsyaWZOLTRVaDNQNnRZUkxPSEdqX0I5NFA5UVdxSFYzTjZWb0ZuYzVQc3QycjRFTzZjYVU?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 07 May 2026 03:37:34 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：IPO行事曆台股 - MoneyDJ理財網；《台股盤後》收跌329點、守5日線，週K翻紅-新聞內容-基金 - MoneyDJ理財網；美股指數期貨最新報價 16:38-台股 - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [IPO行事曆台股 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMibEFVX3lxTFBiR2JJT2ZfZnJvY2VXNWpVT3N3VU1xbHhCUkhrbFlKT2RwVEhyWm9aRzJtbENfcHBxWFBTUU1OWGJxb091R0RmMHZzckg5Z1ZqTnpMRW9POXRsXzhPZnZKWC1fMzZVN1RNY25OcA?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 08 May 2026 19:07:53 GMT
- [《台股盤後》收跌329點、守5日線，週K翻紅-新聞內容-基金 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMimAFBVV95cUxPaDAxeXpPbGxEdWJCQUkxZmQxNVQ4VkpUeUxjb18tbmEwTTVqaGNWVnI0X2JvYjVmYzVSZGZxNWxMUTRlZmpsNzM1ZDN3cERMNkRJS0dXUU5Nc3JQaURGWU9XdnFiYk82ZG9DenB6QzEwVXg4Z2NZN1FsSk9ybkJfbXU3YkFPVVg3dHFHbUotNjZMSTJXdW1hTA?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 08 May 2026 07:54:00 GMT
- [美股指數期貨最新報價 16:38-台股 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilgFBVV95cUxNeDdaeHhNWjdYcnZJWXpfNV9MeDBDbHpablQ1elBqaDd1cFJfRGpuLWZ1aHBUSVk5QkFZWHVvbEtPRFJabl9TekJYb08zeENXMlFxam04aW5hZlh1S2QwNXBTcHVrSUd4WjhzaUFWbVBZUGhJMEVtYkoyRkZTbzVRSWVvNmFQLU1yLWxYbWp5R2xPdWhMRmc?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 08 May 2026 08:52:57 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
- TWSE PER/PBR 抓取失敗：<urlopen error [WinError 10054] 遠端主機已強制關閉一個現存的連線。>
