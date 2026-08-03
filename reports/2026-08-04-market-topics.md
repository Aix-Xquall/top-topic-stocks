# 每日股市熱門話題分析 - 2026-08-04

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜正向｜熱度 9｜市場確認 100.00｜同向 1/1
2. **半導體與晶片供應鏈**｜正向｜熱度 9｜市場確認 63.18｜同向 3/5
3. **關稅與供應鏈轉移**｜中性｜熱度 5｜市場確認 N/A｜同向 0/0
4. **新興題材：OpenAI**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
5. **AI 伺服器與資料中心**｜正向｜熱度 9｜市場確認 0.00｜同向 2/6

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.05（樣本 13）
- 5日相關係數：-0.08（樣本 13）
- 同向比例：6/13

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 100.00 | 1/1 | 0 | +26.79% | +0.77% |
| 半導體與晶片供應鏈 | 63.18 | 3/5 | 2 | +7.06% | +8.10% |
| 關稅與供應鏈轉移 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：OpenAI | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 0.00 | 2/6 | 4 | -10.65% | -8.15% |
| 散熱與液冷供應鏈 | 0.00 | 0/1 | 1 | -21.72% | -6.25% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 相關性偏弱；應提高同向價格確認權重，降低泛 AI、泛半導體等寬標籤推估權重。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-07-22 | -0.33 | -0.15 | +16.67% | 6 |
| 2026-07-23 | -0.01 | 0.01 | +41.67% | 12 |
| 2026-07-24 | -0.16 | 0.43 | +50.00% | 6 |
| 2026-07-25 | 0.30 | -0.06 | +12.50% | 16 |
| 2026-07-26 | 0.38 | 0.06 | +23.53% | 17 |
| 2026-07-27 | 0.54 | 0.11 | +37.50% | 8 |
| 2026-07-28 | 0.32 | 0.13 | +36.36% | 11 |
| 2026-07-29 | 0.16 | -0.03 | +92.31% | 13 |
| 2026-07-30 | 0.25 | 0.92 | +66.67% | 6 |
| 2026-07-31 | 0.10 | -0.10 | +46.15% | 13 |
| 2026-08-01 | 0.38 | 0.25 | +54.55% | 11 |
| 2026-08-02 | 0.06 | -0.21 | +33.33% | 9 |
| 2026-08-03 | 0.35 | -0.49 | +60.00% | 5 |
| 2026-08-04 | 0.05 | -0.08 | +46.15% | 13 |

## 歷史回測摘要

- 回測日期：2026-08-04
- 近5日 3日相關：0.12
- 近5日 5日相關：-0.05
- 同向比例：+46.15%
- 權重狀態：未調整

- 方向準確度：+46.15%
- 信心排序準確度：0.12
- 診斷：弱正相關

調整原因：近 5 日有效樣本 13 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：台股開低翻紅漲逾600點　CPO、記憶體與被動元件強攻 - 經濟日報；MU, INTC, SNDK: Chip Stocks Rally After-Hours On AMD’s Blowout Report - Stocktwits；Seagate and Western Digital Dive 6%, SK Hynix and Micron Slide 5% as Memory Stocks Cool - 24/7 Wall St.

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.48 | N/A | N/A | 829.50 | 971.00 | -14.57% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.48 | +26.79% | +0.77% | 1,288.03 | 2,335.00 | -44.84% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.36 | N/A | N/A | 484.64 | 516.10 | -6.10% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.36 | N/A | N/A | 91.00 | 114.68 | -20.65% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -2.13% | +18.49% | 206.64 | 211.14 | -2.13% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron、memory」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK、SanDisk」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [台股開低翻紅漲逾600點　CPO、記憶體與被動元件強攻 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9IS1hkeEFUMjMyYzItdzkwMkNRX2VPb21BWmFLbk1IUkZkNWpCcGt2RzZoRnFvdnlFclZXaGJBcHNZMC1mWEdKSUlaZWR6cS1fMGVfSzNwYWduUdIBX0FVX3lxTFBONjZjdlBKWkI3Qm9GczJGTE5nZkpRRHl3X2NZVmd5QVN6UDN4SUgwSG9wUXVGR3E5VHVDNHdMU0w2WFZodW9OQjVfNjNVbEtwRmJMVUhGR3RKMG1vblNv?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 03 Aug 2026 03:12:30 GMT
- [MU, INTC, SNDK: Chip Stocks Rally After-Hours On AMD’s Blowout Report - Stocktwits](https://news.google.com/rss/articles/CBMiygFBVV95cUxPeVlYaXJjQjNtTkNRQUxQTHhaLUFMbE80Uy1MeDBpV0FPdkg2SHRLdkdfVUpXM1NrNWhZSVZQQ01sa0o4T1hKdzF1clBFRlRWUmMwWGxQTDNVVFBpOVhObUc2MXpBeXBOZ0p3R0w5NGRNOHB4X0ZIXzhlT0NMbmhzc1RtdmJRTWhlRUhKSHpyVnpaU0VGMlJyU2tDcmdkTG1hWVJJbmtTVDREbzFfWDB4bjhuTGswN3lmdkdHQzY1dzFOVU41VGlBNlZn?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 03 Aug 2026 08:18:52 GMT
- [Seagate and Western Digital Dive 6%, SK Hynix and Micron Slide 5% as Memory Stocks Cool - 24/7 Wall St.](https://news.google.com/rss/articles/CBMixwFBVV95cUxPTVBHRDdxSllBN0lHQXdBSVhoa0g0cWpyalBpN3FWR0gyQ1ItSjE3VnVwcEVPTm1MS3JQNC1uRHhEdG5IVV9VSHRXWHRCWHY4d2VrZktnaG9PUnJKWkMydmI2dldhQnJsMnllbWZDQWg0bkRjTnU5QTVHdEZpTUpjeEhRa1VHdk5OU2lPNWVuNUJzYmIwaE9ydzllLTBXaU4tOFI2WWJxSWhKZDNKZFlObjc1X1RjcGd6aWR5MTQzNnNFZlNON05r?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 03 Aug 2026 14:00:19 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：AMD to report Q2 earnings as chip stocks continue to waver - Yahoo Finance；Are Chip Stocks Poised to Stage a Recovery? Here’s What Wall Street Analysts Are Saying - Investopedia；Intel and AMD Soar 13%, Taiwan Semiconductor Rallies 7% as AI-Chip Stocks Bounce Hard - AOL.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AMD 超微 | 新聞直接提及 | +0.56 | N/A | N/A | 484.64 | 516.10 | -6.10% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.53 | N/A | N/A | 91.00 | 114.68 | -20.65% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | +0.50 | +7.73% | +0.85% | 2,370.00 | 2,425.00 | -2.27% | 同向 | 74.39 | 31.86 | 442.68B TWD / 67.87% | 2026-07-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.05 | +15.12% | -6.35% | 118.00 | 164.50 | -28.27% | 同向 | 6.68 | 17.74 | 23.12B TWD / 22.85% | 2026-07-01 |
| NVDA 輝達 | 產業/供應鏈推估 | +0.02 | -2.13% | +18.49% | 206.64 | 211.14 | -2.13% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | +0.04 | N/A | N/A | 829.50 | 971.00 | -14.57% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.04 | +26.79% | +0.77% | 1,288.03 | 2,335.00 | -44.84% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -12.21% | +26.73% | 392.23 | 446.77 | -12.21% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「Taiwan Semiconductor」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip, foundry。

### 主要來源

- [AMD to report Q2 earnings as chip stocks continue to waver - Yahoo Finance](https://news.google.com/rss/articles/CBMiugFBVV95cUxQWXBhRk5HYUtYR2NZamZqZVZiU1BBd0tVeUpWTW81eXdndkdKdV9mMTYyVjdQc1FKNmhURm9NdXJwOGtqMmZRYTZpTmdTazlLbkhQNHV0bDFxWkx5azhfamxhck55UVllbUl3VjBzNkNoc2FaOHdWZ0Vwel83N0dfV0hSZFdWUkFoQ3NKUzFWN3RqeUlJSVkxNEhVdWRVenkzbGxHdlk4MTlOVUhjSEUyN2lhQWxPemZsdmc?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 03 Aug 2026 11:00:00 GMT
- [Are Chip Stocks Poised to Stage a Recovery? Here’s What Wall Street Analysts Are Saying - Investopedia](https://news.google.com/rss/articles/CBMijgFBVV95cUxPekxqc1VRZjhXQ0dEUTVIX1RsTk9WRm5tbmJlUDlKbS05Qm9VZjcwMlV3aFRCcEVMajhqbVNlTWkzcmQ3dWZ4dHQyNGh4ZHdzLTBPNFZPZ01CRVV3empPSWpwbVVlOE5Ra3I3S1JjRk03UllyMHcxSDFvVUN3Vl94MjFtdjA0d0FIaTE2WEZn?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 03 Aug 2026 20:06:55 GMT
- [Intel and AMD Soar 13%, Taiwan Semiconductor Rallies 7% as AI-Chip Stocks Bounce Hard - AOL.com](https://news.google.com/rss/articles/CBMid0FVX3lxTE41by1UUVByc3A0NEtzcGdBNFFHUnZqVWcwVjdqRjN2SzFQSzlMYW1sYVhqSUJEMGw1TWd5NkdGeEZoUWhsZkw3YXRHUElLa3d3MTduMHYtRE50WE55WmxvTXNKMTFFYjhHX2Q2blVFd2VsNmd2RUpZ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 03 Aug 2026 17:31:01 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：INTC Stock Slides As Sector Weakness And Tariff Risks Mount - StocksToTrade；Intel Stock Slides As Sector Fears And Tariff Risks Mount - timothysykes.com；切入四大CSP水冷供應鏈！法人看「這檔」全年EPS上看94.8元 GB平台、ASIC訂單齊發 - FTNN 新聞網

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 91.00 | 114.68 | -20.65% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +14.85% | +30.71% | 303.42 | 312.06 | -2.77% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | +6.75% | 0.00% | 253.00 | 289.00 | -12.46% | 不適用 | 14.13 | 17.97 | 821.76B TWD / 52.11% | 2026-07-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC、Intel」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 2 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 2 篇新聞出現相關標籤。

### 主要來源

- [INTC Stock Slides As Sector Weakness And Tariff Risks Mount - StocksToTrade](https://news.google.com/rss/articles/CBMifEFVX3lxTFBka2FwX3owSnhOMlcyc3h1bmMwX3FDOHNZV2VQQV9GM250SHdBajVReXg2WTlFQ3FfMXJNSlIwcXFhWFBVM1FYaWxoelA4YmxGTU1sMU5NWC1qaDBRdTQ3bmJ2S0pXVzMwbWhpdEZreEhqZjhhdlBNOXNGUl8?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 03 Aug 2026 12:33:00 GMT
- [Intel Stock Slides As Sector Fears And Tariff Risks Mount - timothysykes.com](https://news.google.com/rss/articles/CBMieEFVX3lxTE8zWXdhLUItNEw3eDJ5RFFEZTA1c29uc0EyTDgtU3VCc0M3eGhSY2ZxamhkMEdYNV8xNlBmcUNRMDZvV3Bka0F4M3J3aV91MGNxX19KbUJYQ1hmYl9XMWxCbXU1LWdEMl9aYXFHQW5MM3hDLWtMMlREcw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 03 Aug 2026 11:47:00 GMT
- [切入四大CSP水冷供應鏈！法人看「這檔」全年EPS上看94.8元 GB平台、ASIC訂單齊發 - FTNN 新聞網](https://news.google.com/rss/articles/CBMiS0FVX3lxTE5fa2U5clpzcXJJdnJpWWpLNk44WU1felhZNmdIRG41UDkwdlZ0RkNrWDF4OGxpM0NmZFdPUDlULTZmRC1nUlBLSWNmYw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 03 Aug 2026 13:45:00 GMT

## 新興題材：OpenAI

摘要：新興題材：OpenAI 相關新聞集中在：Meta, Anthropic, Google, OpenAI to meet Trump officials about AI safety testing - Reuters；Big Tech's Anthropic and OpenAI stakes are distorting the corporate earnings picture - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 新聞直接提及 | 0.00 | +24.17% | -3.76% | 487.65 | 506.69 | -3.76% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：新聞直接提及「OpenAI」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Meta, Anthropic, Google, OpenAI to meet Trump officials about AI safety testing - Reuters](https://news.google.com/rss/articles/CBMiqgFBVV95cUxObWVNalU0cV9OY2Q0RHFkdFJtakZJRTdzV1BiUDVvamY3RlVRX3ZydGl5YnAzU2dxQldBTVVMMW1wMWl0ekI1eXZJdm84bjBtUFBZc2JBeVJfblJEMVhDZGs4UWpaZXZTTUQtYy1QVFVsYmxsUG1jVHZTd2VFWEJXV2FlNXg4ZVZmRUI5SWpxMWo2cGFTT0hWRUJmNUpyaXZFRnRISnhvNy1YUQ?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 03 Aug 2026 21:57:58 GMT
- [Big Tech's Anthropic and OpenAI stakes are distorting the corporate earnings picture - CNBC](https://news.google.com/rss/articles/CBMiowFBVV95cUxQLVZ0SlZoODJGekFDdGRyVkJwNll5b09xSGtra3lBRHJuQWtoc0hOZlJxdjk2YUZUZDJXZFJSdFJTcVNfQnhHUFZBMUg0ZTVmTU5qMk1TMkw0am92T2FjZlotdnd2X3RReUNWcHJyRDJxRDZ2MjczUWZ3c0pQeWYxN1d3MUV5LVA4SE5UUXlqRjR3QTM1c3NVOTNpUlh6YTllOE9j0gGoAUFVX3lxTE9jQlpJY3Q1UDdiSHVzWEJhcFdnSHdNbFNyeDQ2cUsxLUhwQ2Vnd0pnTnM4YUlnUkptOFVhUUZpaUw4anZ3R2huVkoxWmt0WkRlQUhNamF2ZE1BZHdlV2ZwMXd0YktDT1VZTmZqVXBfZmVwdVhoaGxkRWc0U2hMOWpmcWtTMlVjdzR5R2dkMFgzYVl6b1V0ZnpnejNEa21NaXctd3lsdThqQw?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 03 Aug 2026 21:53:42 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel and AMD Soar 13%, Taiwan Semiconductor Rallies 7% as AI-Chip Stocks Bounce Hard - AOL.com；美國擬禁用中國開源 AI 模型，估美企年成本恐增高達 120 億美元 - TechNews 科技新報；.牧德 7 月營收續創新高，AI 高階製程接單動能延續 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.54 | N/A | N/A | 91.00 | 114.68 | -20.65% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.53 | N/A | N/A | 484.64 | 516.10 | -6.10% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | -0.27 | +7.73% | +0.85% | 2,370.00 | 2,425.00 | -2.27% | 背離 | 74.39 | 31.86 | 442.68B TWD / 67.87% | 2026-07-01 |
| NVDA 輝達 | 產業/供應鏈推估 | -0.06 | -2.13% | +18.49% | 206.64 | 211.14 | -2.13% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 產業/供應鏈推估 | -0.02 | +24.17% | -3.76% | 487.65 | 506.69 | -3.76% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -12.21% | +26.73% | 392.23 | 446.77 | -12.21% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.02 | +22.24% | +0.33% | 610.00 | 680.00 | -10.29% | 背離 | 10.86 | 56.64 | 65.78B TWD / 32.86% | 2026-07-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.02 | +24.13% | +6.25% | 3,910.00 | 4,310.00 | -9.28% | 背離 | 60.69 | 64.57 | 58.01B TWD / 2.80% | 2026-07-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：恐。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。 方向判斷命中詞：恐。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「Taiwan Semiconductor」，共 1 篇新聞命中。 同時符合主題標籤：AI, advanced packaging, CoWoS, AI server。 方向判斷命中詞：恐。

### 主要來源

- [Intel and AMD Soar 13%, Taiwan Semiconductor Rallies 7% as AI-Chip Stocks Bounce Hard - AOL.com](https://news.google.com/rss/articles/CBMid0FVX3lxTE41by1UUVByc3A0NEtzcGdBNFFHUnZqVWcwVjdqRjN2SzFQSzlMYW1sYVhqSUJEMGw1TWd5NkdGeEZoUWhsZkw3YXRHUElLa3d3MTduMHYtRE50WE55WmxvTXNKMTFFYjhHX2Q2blVFd2VsNmd2RUpZ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 03 Aug 2026 17:31:01 GMT
- [美國擬禁用中國開源 AI 模型，估美企年成本恐增高達 120 億美元 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiswFBVV95cUxPVzlEb1BVSTNXdmV2dG9CcUNXNzA4RHgyWTZTODV0czcwMG91RXBvVUo3cFp5bWthWmlCX1pCQ29IaVJnZXlxdVMyYk9DNnJKSVNUS05UVThqV3BqM0xFU2owa1lVNURGaF9qMTFvdm0xYnktTUZDNWhjY3JzOHc0NFNEZzNKNElpQ0NQOEFTUVBndkZlaGNRb3BNOHkxWDJBalJkZkRhZWstb1FzVDNvQ0JyUQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 03 Aug 2026 07:11:15 GMT
- [.牧德 7 月營收續創新高，AI 高階製程接單動能延續 - TechNews 科技新報](https://news.google.com/rss/articles/CBMirAFBVV95cUxNNEhsQjIyZ2VUXzJaX0NKUHlHZTZVZW5BTWNOX1NrU29DWU9mMkNhdlZsZndPSEJtOW5RbzFGVUJtem4xSzVzamtBU1hQakpMcDJYLWJYZlRWSngwakswVVlwcW5zaEl3Znl5TTlPQ2ZRT0tnR296dS1KLUZGWWF5YXJQcDhLU20xVGJXU2Z5YzMwbkF4MDA3TXZNQllVY3o0cWlpMHdjRl9vZ1Mw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 03 Aug 2026 21:01:47 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報；切入四大CSP水冷供應鏈！法人看「這檔」全年EPS上看94.8元 GB平台、ASIC訂單齊發 - FTNN 新聞網

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | -0.21 | +21.72% | +6.25% | 2,550.00 | 2,835.00 | -10.05% | 背離 | 61.06 | 41.90 | 17.62B TWD / 66.11% | 2026-07-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 1 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：跌停。

### 主要來源

- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 03 Aug 2026 19:56:20 GMT
- [切入四大CSP水冷供應鏈！法人看「這檔」全年EPS上看94.8元 GB平台、ASIC訂單齊發 - FTNN 新聞網](https://news.google.com/rss/articles/CBMiS0FVX3lxTE5fa2U5clpzcXJJdnJpWWpLNk44WU1felhZNmdIRG41UDkwdlZ0RkNrWDF4OGxpM0NmZFdPUDlULTZmRC1nUlBLSWNmYw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 03 Aug 2026 13:45:00 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：股市向下扎根！台股7月開戶數突破1,460萬大關 未成年族群成增加主力 - 經濟日報；散戶有多猛？上半年1.08兆元狂買台股 力抗外資賣超 | 市場焦點 | 證券 - 經濟日報；台股內資挺 挑戰兩關卡 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [股市向下扎根！台股7月開戶數突破1,460萬大關 未成年族群成增加主力 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE13RFhoVHVyN2VWZ0ZteVZtb0ozNUdkUnZlRVJ3cEhuY3ZmVWJ3QzFDZy1nTUdyZE1DeHp6ajNYdFY5bGpVSzdtSUQ1MlpMTHkzek5LcXRJcUExQdIBX0FVX3lxTE1Pa29KeE0tczVTajlIOWd2R0ZFRHNrbjhiSW9IempDbVBOTnEzQS1wOXJmSUZRZ1QzN0ViNHdSdktreV9FNWJfTzBiOFl0dENzSERwb0wxVnJtTzRjNUgw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 03 Aug 2026 06:34:16 GMT
- [散戶有多猛？上半年1.08兆元狂買台股 力抗外資賣超 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9KZmkxb1l6SnFKcGxOOWVuVDRSMThXR0lpcExLMkNYOUlaSnlGN1EyNUtiQXRVd01PMmpycjNSaWprRFpRaXBrNDdQQ3BwQXhOemIyX25Qc1dDdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 03 Aug 2026 14:40:03 GMT
- [台股內資挺 挑戰兩關卡 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5uVnBjRDJWT01MY29uOVEyZGlPaWVkRHFBQUJtY1JDUkZRX0NSc3FYR0VaX1pkeFhnVkh6NVVXY2xJcm4yYjJ5Z1cxX1VrVk1NR3BhUllTUXdLZ9IBX0FVX3lxTE43X2hJQ1BZOWhLZ0hmY3BrbnkyWlZWcm5uLVl1SHZwelE5YmV1eVZpVjJDelc2bUxLX0NCTGJPU1loZ29qNFdHQ2k0aWJCMHh3MHZ2WndGTm1NcG1QcHI0?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 03 Aug 2026 17:59:18 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：統一證券：台股估短線持續在月線與半年線間震盪- 新聞 - MoneyDJ；國票證券：台股短線仍以震盪整理看待- 新聞 - MoneyDJ；《台股盤後》收漲266點、日K連二紅，10日線失而復得- 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [統一證券：台股估短線持續在月線與半年線間震盪- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMieEFVX3lxTE5yYlM2VUdBR1ZNVmN0Rk5KTWYtTU5DRmswZnJJU2x3cHJYSndTUURrZVZpZ3RrVGM3a1FXcVRZQk5Hd3Y4Sl9FZjNITHozN3N0TzBoR1JLbnR5aVRaTUl2MGRQaDN2VzZCbS1pQ0xLUzlMU1ZGb3NKZA?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 03 Aug 2026 00:48:00 GMT
- [國票證券：台股短線仍以震盪整理看待- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMieEFVX3lxTE9WNFNvMVFQd1FmdzVZampvSlFEelh6dDNCamdjY2NrUGNCMTZaWElYaU1pSU90eGVNcnZFWTVOaG9oNEtlV3FhNDRwXzl1MUJUdGR6Uk1vbU13TGY0eVg4aUtGMkRodWxhMzdWZ0EzOENwaUozTWZRMg?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 03 Aug 2026 00:48:00 GMT
- [《台股盤後》收漲266點、日K連二紅，10日線失而復得- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPbGo0bGZCRktWVDU3SURGa2tocndQeU4xN3U0dHhhWms1ZFVnZVkxMEx2b3c1ZUluY0w2ZkxGclhPWlQ2bG51QTlBNzBCMmp2NmJFOXNHVGN4bmVwcnBMZnlOYS1lT1kyMXhRVTZYNkljUk94UmdHcno3dlYxQzMwZkx5TkQyYWt4RHJSWjEwaE5JZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 03 Aug 2026 07:51:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
