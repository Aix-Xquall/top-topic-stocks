# 每日股市熱門話題分析 - 2026-05-14

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜中性｜熱度 7｜市場確認 N/A｜同向 0/0
2. **AI 伺服器與資料中心**｜負向｜熱度 17｜市場確認 12.04｜同向 3/6
3. **利率與成長股估值**｜負向｜熱度 2｜市場確認 N/A｜同向 0/0
4. **半導體與晶片供應鏈**｜中性｜熱度 5｜市場確認 N/A｜同向 0/0
5. **新興題材：TradingKey**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.29（樣本 6）
- 5日相關係數：-0.20（樣本 6）
- 同向比例：3/6

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 12.04 | 3/6 | 3 | -7.66% | -6.19% |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：TradingKey | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：正本公司115年3月營收 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-05-08 | 0.03 | 0.48 | +76.92% | 13 |
| 2026-05-09 | 0.10 | 0.55 | +33.33% | 9 |
| 2026-05-10 | 0.45 | 0.55 | +75.00% | 8 |
| 2026-05-11 | -0.03 | 0.47 | +85.71% | 14 |
| 2026-05-12 | 0.00 | 0.42 | +78.57% | 14 |
| 2026-05-13 | -0.08 | 0.07 | +58.33% | 12 |
| 2026-05-14 | -0.29 | -0.20 | +50.00% | 6 |

## 歷史回測摘要

- 回測日期：2026-05-14
- 近5日 3日相關：-0.12
- 近5日 5日相關：-0.08
- 同向比例：+50.00%
- 權重狀態：已調整

- 方向準確度：+50.00%
- 信心排序準確度：-0.12
- 診斷：方向與信心皆需修正

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

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Intel Lands a Preliminary Apple Chip Deal and an SK Hynix Packaging Partnership — Is INTC Still a Buy at $124? - TradingKey；Why Sandisk (Not Micron) Could Be the Biggest Winner Of the AI Memory Era - AOL.com；Buy, Sell, or Hold: SanDisk at $1,562 and Micron at $746 - 24/7 Wall St.

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 803.63 | 803.63 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | -7.37% | +2.64% | 1,447.23 | 1,562.34 | -7.37% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 120.29 | 120.61 | -0.27% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 新聞直接提及 | 0.00 | +7.18% | +48.80% | 298.87 | 298.87 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +29.49% | +18.16% | 225.83 | 225.83 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron」，共 4 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Lands a Preliminary Apple Chip Deal and an SK Hynix Packaging Partnership — Is INTC Still a Buy at $124? - TradingKey](https://news.google.com/rss/articles/CBMi7gFBVV95cUxNTGpHN3o3WGJhaU1Nbld3bC03TnZpTlhfRXNCeU1Oc0QzRTlyelo3VjNvN0Nucjd5UWpkTDB5S1VPMVlRcHhfekg0U01ZbnoxNTRrbU1UdE11R3FQX3lIX3J3eFN0OUFjaENlM2ZlSjg0UkFIbGoxMGNPdXRrZFdVcEIxWTZfNlNRRG1fQXA5X1VoLUNMQklucVppVl9mVFc1cVBsNV95V1FqUWpLdEExZHZQTm5NM0RVQzRucC12MGthOVVXdEhsTUVWR1FNWjVhdDRXelNuTzNVbHpqSWJiamFFVmI0NTFGRjdwQTFR?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 13 May 2026 13:02:11 GMT
- [Why Sandisk (Not Micron) Could Be the Biggest Winner Of the AI Memory Era - AOL.com](https://news.google.com/rss/articles/CBMifEFVX3lxTE9BckZjd2l3VzdjRjllREliSGtVUWtQV3BfaXpubkxkT0Ria1lRU1ZYRUdzU2FyWG9vby1Tbjg2d2NQTWhGSWZ3Q21wOWdvWTBHUmhHNkhZLVJ0SjA0c0hmZGFHM0s4Snc4MzZBZ1lla2FrTC1ERXFNSjRuMzI?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 13 May 2026 10:03:25 GMT
- [Buy, Sell, or Hold: SanDisk at $1,562 and Micron at $746 - 24/7 Wall St.](https://news.google.com/rss/articles/CBMimgFBVV95cUxQaFd2ODJsSVZWQVpBb09wYmpRN2FJU1JwdUloSDl3ZW96SlBGZ2s4eDFxQ01MRWZ6bkZhdWZqakZhaHBJQ1RXbWE1MU11OFNzSEcyZ3ZEUVNwRVh3V0RjdGl3YVZBbDlLbjcxMzJqOUxNdTh4MGViYWxsdFJaZ2tCcnZaVHByaVFTdnNzdGlQdTNkay10eHZDSlVB?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 12 May 2026 13:31:14 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：AI Gold Rush or Earnings Trap: Buy Applied Materials Stock as its Q2 Results Approach? - TradingView；國科會ICTGC新創 強化資料中心、半導體設計及無人機實力 - 中央社 CNA；AI 版 ELD 如何轉型為車隊管理核心？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | -0.13 | N/A | N/A | 120.29 | 120.61 | -0.27% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | -0.06 | +29.49% | +18.16% | 225.83 | 225.83 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | -0.10 | N/A | N/A | 445.50 | 448.29 | -0.62% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.10 | -3.06% | -1.33% | 2,220.00 | 2,255.00 | -1.55% | 同向 | 66.26 | 33.51 | 410.73B TWD / 17.50% | 2026-05-01 |
| MSFT 微軟 | 產業/供應鏈推估 | -0.07 | -17.64% | -11.98% | 405.21 | 506.69 | -20.03% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | +34.66% | +25.80% | 416.79 | 419.30 | -0.60% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.04 | +6.20% | +4.58% | 548.00 | 555.00 | -1.26% | 背離 | 10.86 | 50.88 | 62.25B TWD / 19.22% | 2026-05-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.07 | -3.72% | +1.90% | 3,495.00 | 3,700.00 | -5.54% | 同向 | 66.17 | 52.97 | 46.74B TWD / -4.14% | 2026-05-01 |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 5 篇新聞出現相關標籤。 方向判斷命中詞：衝擊。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 5 篇新聞出現相關標籤。 方向判斷命中詞：衝擊。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 5 篇新聞出現相關標籤。 方向判斷命中詞：衝擊。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AI Gold Rush or Earnings Trap: Buy Applied Materials Stock as its Q2 Results Approach? - TradingView](https://news.google.com/rss/articles/CBMi1wFBVV95cUxPYk5ES2tndkF3THRfcEpMMnJPTVpmSmhvdTFLVHJxbDFhbDhsRzhXUTI1eUZ1XzY3SnRTZUxTa3VyUVgtTnpjTTFyNWVPcDFCaHR1ajRHZWZUbU82ZFBFbE1HTFNTTDJWMEZHQXRmNDhnVGJkYWRDSlpVYnJHMElwNF85cVZ4U3ROZ3BzQU43UWpDNm5zUW9IUDJQMktHSDE0OEx3U3Zpdkp1NElDc25NekxUbmZaQ0dNYk02b0ExdldoTE43MkZwR181M1p2aUV0U3kxWlZENA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 13 May 2026 18:41:00 GMT
- [國科會ICTGC新創 強化資料中心、半導體設計及無人機實力 - 中央社 CNA](https://news.google.com/rss/articles/CBMiVkFVX3lxTE9XQnZTSm9MRXZ4SmVRR2tNUHpjWmVJOGp5MHI1X2tPeGJPVUlOTk8xZEdZSURBbHJIREtwd2JmalFDTE4zOG9LRjVPTjFpZUFkb05xYkdR?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 13 May 2026 03:11:38 GMT
- [AI 版 ELD 如何轉型為車隊管理核心？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9RQVpjWWhJdVN4MTdnOHNDVEpkZ1IxcTVTZ2JqVllpRjlZNFk3WkpLUUZyaTJtRXFteWVhR1ZocGZwOVZGLVpYM2FrcjJWdnpTZ3RQd3Voamd6Rnc?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 13 May 2026 17:56:00 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：Fed降息夢碎！美國4月PPI爆表年升6.0% 今年升息機率衝上50% - news.cnyes.com；AI樂觀情緒蓋過通膨利空　美股標普那指收盤創新高 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | -17.64% | -11.98% | 405.21 | 506.69 | -20.03% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Fed降息夢碎！美國4月PPI爆表年升6.0% 今年升息機率衝上50% - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTE4wd3FYQUxwRlFWMXRTSDVKakJaOVBnTmd0WnRRN1FLdWlTUG1hc3dpdUluNGpqb21OOHU3em0xZXdPOW9yWDBXZVpoaWRLSjg?oc=5) - Google News source discovery | 鉅亨網 Wed, 13 May 2026 12:40:10 GMT
- [AI樂觀情緒蓋過通膨利空　美股標普那指收盤創新高 - 經濟日報](https://news.google.com/rss/articles/CBMid0FVX3lxTE5DMEExSTFNbi1UR3UxOUtJbmhYaFBRekVLYTFvZnNWMF9hNGdTb01ndkluRzF1OG1EbXhDeUgzRHZwMWtUaTZsbzlsR28xbG1LbTJaRWZnWURJLTl4UzJPb0FfUjJCeWN4MmlJRGpmOVc0S0J2RFd30gFfQVVfeXFMUGZBSkg1NG1nWF9fQ2tXWDVzVm9HYlNVZmlWSk1VM0VDZXpYM0lqVE5BazVCcTNRYUZIcFFFeWZTdjRuakJHOFZjM0VNeXd0dzZFbm1oelZqbzVpUUhiajg?oc=5) - Google News source discovery | 經濟日報 money Wed, 13 May 2026 21:24:02 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Forget Intel: Here Is the Chip Stock Wall Street Is Sleeping On - 24/7 Wall St.；國科會主委吳誠文訪視成大晶體研究中心 產官學聚焦次世代半導體關鍵布局 - 中央社 CNA；國科會ICTGC新創 強化資料中心、半導體設計及無人機實力 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 120.29 | 120.61 | -0.27% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -3.06% | -1.33% | 2,220.00 | 2,255.00 | -1.55% | 不適用 | 66.26 | 33.51 | 410.73B TWD / 17.50% | 2026-05-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +7.78% | +7.66% | 98.40 | 104.50 | -5.84% | 不適用 | 4.00 | 24.72 | 22.66B TWD / 10.80% | 2026-05-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +29.49% | +18.16% | 225.83 | 225.83 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 445.50 | 448.29 | -0.62% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 803.63 | 803.63 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -7.37% | +2.64% | 1,447.23 | 1,562.34 | -7.37% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | +34.66% | +25.80% | 416.79 | 419.30 | -0.60% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 1 篇新聞出現相關標籤。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 1 篇新聞出現相關標籤。

### 主要來源

- [Forget Intel: Here Is the Chip Stock Wall Street Is Sleeping On - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiqgFBVV95cUxPOFFwRnFyU2VxTTR3SjBtdUhlZU1rRHpFM0NZcTVEMklNdWRNT09CdUZmMWZHZ3JuSWpQZlVxLXFjYjc2UlB2Q2lLRVRoamZlSGpsM0xMU3BMTjdQOVFkcXZ5VjVCdE5MM1hiY1Vxb0JibWlkcXU1S1VuYkw2TktfZUtLcm8wMnNpbUMtSjJ6SERvd29XWFRMSDJsSUJGeHRoZjJMVzdZZ1lYZw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 13 May 2026 13:34:44 GMT
- [國科會主委吳誠文訪視成大晶體研究中心 產官學聚焦次世代半導體關鍵布局 - 中央社 CNA](https://news.google.com/rss/articles/CBMiVkFVX3lxTE1nLUE2b1VKa2lVTE5WMnpvdkFiRUhQZENQNDBoTUs0RFhsU1Z3MzlJSzUyS25CLUZ6YlNVMWdWeDF3TFlkZ3VkM1hLazZXUjc0c012VGd3?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 13 May 2026 09:05:10 GMT
- [國科會ICTGC新創 強化資料中心、半導體設計及無人機實力 - 中央社 CNA](https://news.google.com/rss/articles/CBMiVkFVX3lxTE9XQnZTSm9MRXZ4SmVRR2tNUHpjWmVJOGp5MHI1X2tPeGJPVUlOTk8xZEdZSURBbHJIREtwd2JmalFDTE4zOG9LRjVPTjFpZUFkb05xYkdR?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 13 May 2026 03:11:38 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Intel Lands a Preliminary Apple Chip Deal and an SK Hynix Packaging Partnership — Is INTC Still a Buy at $124? - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 120.29 | 120.61 | -0.27% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 新聞直接提及 | 0.00 | +7.18% | +48.80% | 298.87 | 298.87 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AAPL：新聞直接提及「Apple」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Lands a Preliminary Apple Chip Deal and an SK Hynix Packaging Partnership — Is INTC Still a Buy at $124? - TradingKey](https://news.google.com/rss/articles/CBMi7gFBVV95cUxNTGpHN3o3WGJhaU1Nbld3bC03TnZpTlhfRXNCeU1Oc0QzRTlyelo3VjNvN0Nucjd5UWpkTDB5S1VPMVlRcHhfekg0U01ZbnoxNTRrbU1UdE11R3FQX3lIX3J3eFN0OUFjaENlM2ZlSjg0UkFIbGoxMGNPdXRrZFdVcEIxWTZfNlNRRG1fQXA5X1VoLUNMQklucVppVl9mVFc1cVBsNV95V1FqUWpLdEExZHZQTm5NM0RVQzRucC12MGthOVVXdEhsTUVWR1FNWjVhdDRXelNuTzNVbHpqSWJiamFFVmI0NTFGRjdwQTFR?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 13 May 2026 13:02:11 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：Sizzling semiconductor trade at risk of cooling - and stalling US stocks rally - Reuters

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 產業/供應鏈推估 | 0.00 | +5.73% | +6.16% | 2,585.00 | 2,835.00 | -8.82% | 不適用 | 49.17 | 52.84 | 15.63B TWD / 71.62% | 2026-05-01 |

關聯理由（前 3）：
- 3017：產業/供應鏈推估：公司標籤符合「散熱與液冷供應鏈」關鍵字 thermal；其中 0 篇新聞出現相關標籤。

### 主要來源

- [Sizzling semiconductor trade at risk of cooling - and stalling US stocks rally - Reuters](https://news.google.com/rss/articles/CBMisAFBVV95cUxPcDlEX0swclZvbE1tWTVxa3o1bV91dkhsaFVVVHVSeFI2d0s1a0hjcGdZdnVzZ2c2RnFkbFhVd0dtaTdpV3M2MS11R0Frd1hqZzBfampZMzdPWnJTVndCa0J3ZW5BZElYZy1UcVR2OWdDTURMQjZuOXRIT01odHMxdWt4VWcyWnBlMnNGZ3VjMXlyTUVILWtHWHIzLTVtS1JRd3lveEFzUnRNckZvSFdvVg?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 13 May 2026 14:32:54 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：《台股盤後》收跌523點、日K翻黑，10日線有守-新聞內容-基金 - MoneyDJ理財網；台股回檔 台幣早盤放量貶值4.2分 - MoneyDJ理財網；面對520行情 主動式台股ETF多空操作具靈活度 - 基金 - 新聞 - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》收跌523點、日K翻黑，10日線有守-新聞內容-基金 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMimAFBVV95cUxObGtUMGN4RzNvZGJvWUQzM2lTY3RoQ3FXWDhnTVktWHpSbDFaUmpOemV2b1l4WmFjaG12RTNZQzJ4OWJnVWVsTnlLcTR1SWs5cDNTOXNSUkpXT2VMQjJobGdoelZqQV84OVRyQjExRGNqSm1adzMwcTBQTV9uMWdoLWdiUU13SC1hbm1BRk1uUllvRUFDOV9JUA?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 13 May 2026 09:10:00 GMT
- [台股回檔 台幣早盤放量貶值4.2分 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikgFBVV95cUxOTnZtQTlUeHZGLXdyQkZ2LUdQV3Q0WjNtV2VVZkZvcXAtazE0MHhzZmVJQTVYMFdzUGZ3SjhNTHpEUU5QMXdBSjVYRUxVOUhoVHJqaTM1UUdxXy03V1g0VlhTcmhyaExWdHR0WmRzNWhld2VxbmFITmt3Q1NoeGFtM0l5c3p2RUp1V2lMRHpkS2tIUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 13 May 2026 04:52:00 GMT
- [面對520行情 主動式台股ETF多空操作具靈活度 - 基金 - 新聞 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMihwFBVV95cUxOdnlRZWVYYjZwbkdSMUVlbGdDanhtcnJlbGhVV3dNNHY2dDRlLUJTT0lEcG5VdTFBRWsxNVBIU3FKdk1sNXdNNUREeDhqbEgtQ01zcmliXzRMbjFKMDBGNGZPUzBmcEZMdlZFVmJidXFGcVpoR09kenZYcUwzdmRiZm01bXlmTFU?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 13 May 2026 05:00:00 GMT

## 新興題材：正本公司115年3月營收

摘要：新興題材：正本公司115年3月營收 相關新聞集中在：耀勝更正本公司115年3月營收公告- 新聞 - MoneyDJ理財網；三商壽更正本公司115年3月營收公告及各項產品業務營收統計資料及4月14日重訊內容- 新聞 - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [耀勝更正本公司115年3月營收公告- 新聞 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikgFBVV95cUxNeHlhd2I2RjZpNXl1ekNZQmJWREswcnVkT2JLVTBxcU9sVWNCUFVIN1h3M1MydmxzYnVPRmZsMkhaNGdDQjQzTzdhaS1wWlpncEVVeUJsNlA1MlpqbUo2Qy02bENEdDJIcUxlZW1HTnlEUzRpM0ozbGJkclhkM1RsV2xXekppRVFnN0t3S3NRN1NKdw?oc=5) - Google News source discovery | MoneyDJ Wed, 13 May 2026 11:53:00 GMT
- [三商壽更正本公司115年3月營收公告及各項產品業務營收統計資料及4月14日重訊內容- 新聞 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikgFBVV95cUxNbXBfcTVIcjZWcEkwMk1QRlZhQ1ZMNlFHcEhuMzg4TlZOVWNjNG5hUTRaUTYycW1hMTcxcE5tcm55a0NHa3RlVHliVzBRckxueW9YQ3RtYlRrMkR5VVZES2RVQ3I3REdGUnpyanFUQUNxcnFsN0VUY0VtQnhUUnBaeW1GWll4eGMzSFNQVEhOcEUydw?oc=5) - Google News source discovery | MoneyDJ Wed, 13 May 2026 09:23:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
