# 每日股市熱門話題分析 - 2026-05-11

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **綜合市場情緒**｜正向｜熱度 36｜市場確認 75.34｜同向 1/1
2. **AI 伺服器與資料中心**｜正向｜熱度 15｜市場確認 73.10｜同向 4/6
3. **記憶體與 HBM 供應鏈**｜正向｜熱度 8｜市場確認 100.00｜同向 2/2
4. **半導體與晶片供應鏈**｜正向｜熱度 4｜市場確認 100.00｜同向 5/5
5. **新興題材：B729**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.03（樣本 14）
- 5日相關係數：0.47（樣本 14）
- 同向比例：12/14

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 綜合市場情緒 | 75.34 | 1/1 | 0 | +1.78% | +7.26% |
| AI 伺服器與資料中心 | 73.10 | 4/6 | 1 | +8.81% | +15.63% |
| 記憶體與 HBM 供應鏈 | 100.00 | 2/2 | 0 | +17.25% | +22.11% |
| 半導體與晶片供應鏈 | 100.00 | 5/5 | 0 | +10.26% | +23.12% |
| 新興題材：B729 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：AI伺服器 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：三大晶片 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：4月營收 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 相關性偏弱；應提高同向價格確認權重，降低泛 AI、泛半導體等寬標籤推估權重。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-05-08 | 0.03 | 0.48 | +76.92% | 13 |
| 2026-05-09 | 0.10 | 0.55 | +33.33% | 9 |
| 2026-05-10 | 0.45 | 0.55 | +75.00% | 8 |
| 2026-05-11 | -0.03 | 0.47 | +85.71% | 14 |

## 歷史回測摘要

- 回測日期：2026-05-11
- 近5日 3日相關：0.00
- 近5日 5日相關：0.05
- 同向比例：+46.67%
- 權重狀態：已調整

- 方向準確度：+46.67%
- 信心排序準確度：0.00
- 診斷：低相關

調整原因：近 5 日信心分數與股價關係偏低，提高價格確認，降低寬題材推估。；關鍵詞×公司後續樣本有效 0 筆，未達 30 筆，不調整樣本權重

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

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：產業評析-兩千億買盤湧向神山？中小股慘了？4問解讀「台積電條款」資金洗牌 - MoneyDJ理財網；法人專欄分析-台股 - MoneyDJ理財網；法人專欄分析-台股 - MoneyDJ理財網

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | +0.65 | +1.78% | +7.26% | 2,290.00 | 2,290.00 | 0.00% | 同向 | 66.26 | 34.57 | 410.73B TWD / 17.50% | 2026-05-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。

### 主要來源

- [產業評析-兩千億買盤湧向神山？中小股慘了？4問解讀「台積電條款」資金洗牌 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilgFBVV95cUxNSFdvWExZeU5PLVN0UVdfdkhfYTh4MFhjd21ZVDNwMlczZDdLOHFCRlNIbzJCX1ZSNm54aVhrS3d5SmRnSU1FaldhMmRoaFhLQTdhaG8wU2pMdTBtbUUxQUdWSnlBT2dIeGNEUFFKVktmeG1KcHdLVk1QekRISWEzWGZlTDl4YWc2YmpEZUlsNnlIR1VteWc?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 10 May 2026 16:03:30 GMT
- [法人專欄分析-台股 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMif0FVX3lxTE1tVGplb0kzQXRQa1NWMmVZZkl1VC0tSVZyd3U4aHN1ZEUzYnhsanJreHAwX0U0Z2VObE1zLUhJTm94S2xNZDRBSUxRampqT2xIb3lhbWVWdmZmMmVZb21NdTR0TjNRSU5ialgtVUVXeGtydjZTeE5ZRnlLNTdPNUU?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 10 May 2026 17:04:42 GMT
- [法人專欄分析-台股 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMib0FVX3lxTE42ZDA2T0pFSlpCT1IzZjVoeE5yeWRfRjlkZmtTSjVNZXB0ZFdvUG80cFYyNEdEZmZ6SVNmaTAyUmpQelo3UUwyX2JHZDRLSWVkRVkxbFc2a2ZZWDRPa18zX1YxY2JUOENxQkN0azdpaw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 10 May 2026 16:51:46 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：台股受惠 AI 加持及資金行情再創新高 法人點名三大題材人氣聚焦 | 市場焦點 | 證券 - 經濟日報；小摩：台股 AI 硬體鏈看漲 專家點名吸睛族群 - 經濟日報；AI 需求正旺及大廠擴產腳步持續 台股科技基金逢回布局 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.88 | N/A | N/A | 124.89 | 124.92 | -0.02% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 新聞直接提及 | +0.65 | +5.17% | +46.01% | 293.26 | 293.32 | -0.02% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.15 | +23.40% | +12.60% | 215.22 | 215.22 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.14 | N/A | N/A | 455.19 | 455.19 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.14 | +1.78% | +7.26% | 2,290.00 | 2,290.00 | 0.00% | 同向 | 66.26 | 34.57 | 410.73B TWD / 17.50% | 2026-05-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.05 | -15.64% | -9.84% | 415.06 | 506.69 | -18.08% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.10 | +38.93% | +29.79% | 430.00 | 430.00 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.08 | -0.77% | +7.95% | 516.00 | 516.00 | 0.00% | 未明確 | 9.37 | 55.54 | 62.25B TWD / 19.22% | 2026-05-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC、Intel」，共 2 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：rally, 受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AAPL：新聞直接提及「AAPL」，共 1 篇新聞命中。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：rally, 受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [台股受惠 AI 加持及資金行情再創新高 法人點名三大題材人氣聚焦 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMieEFVX3lxTFA2SGQ3d3pFamg1S3IzWXdCMmVlRVJINjlOVlpEalZLV29UdTBHMGFsQXJlUFdwZFlza0E5ZVF3OVA3SWNlTXp0Nkx0MXkxM3c4NFpERE1wRnVJLU82VGV4c0FfSDA4d0xkcGdqTW0zeUlCOXVkQnh0MA?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 10 May 2026 14:55:45 GMT
- [小摩：台股 AI 硬體鏈看漲 專家點名吸睛族群 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxNbmYxXzFmQ0J6R1c2cTg2TF83dXJrWlBSQ3BmNi01MDViWlRpbDFmVl9yM09aVUVhV2hSbnVHSVNTVEpra1dnc1hwVDk5Z3pfZFNYbW90dnNIWlpkazlOc3c4ZU0ySTVNdnhaeHo5RE5idVZCdHg1TW40VzQ0UUFQUNIBX0FVX3lxTE9ycWdoS2Z4WFNnS2xibmlRQzc1U2lxWDZTNDB2RFIzTkZZQVdkYkVyT2tNQUg2N081bmlTTENmRlNIemVOeXY3TlgzUmZiVjg4ZTRpZEV0aXdQREl2bEZR?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 10 May 2026 18:13:31 GMT
- [AI 需求正旺及大廠擴產腳步持續 台股科技基金逢回布局 - 經濟日報](https://news.google.com/rss/articles/CBMihAFBVV95cUxNQXpKcDZOMmJTRU1Uc2l0ekxNN0lpME81a3h2SjJtNTJ5blU0a3NaeEhRTl9JdnBFWjRxbHQzN3RxdVR5RXdvaV82dXI1eVRjWVk3ODVpVm1OdXg5VzY4ZlZReFBYcmFuTFpNaW9OUml5Q2FJX3RIYTBKZDdLRjJnMWVWYV_SAV9BVV95cUxOOG1TT0lSMUxWNGNNc1E0VVhjTTk2TmlsM1NGbHdOVUZ0N1plWFZkaUdoMFpDTFBtQnFFWm45Uzc0a3RYbVBXSHRRa3g5Um53UUdjcTlnU3o5UGJxWk9Jdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 10 May 2026 16:50:57 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：INTC, AMD, MU stocks hit 52-week highs today: What's triggering the rally? - MSN；Are SanDisk and Micron Too Expensive? Here's How You Can Invest in the Artificial Intelligence (AI) Memory Supercycle for Just $50. - The Motley Fool；Micron vs. Sandisk: One AI Stock Is a Buy, One Is a Sell, Says Investor - TipRanks

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.88 | N/A | N/A | 746.79 | 746.81 | -0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.88 | +11.09% | +31.62% | 1,562.34 | 1,562.34 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.67 | +23.40% | +12.60% | 215.22 | 215.22 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.65 | N/A | N/A | 455.19 | 455.19 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.65 | N/A | N/A | 124.89 | 124.92 | -0.02% | N/A | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk、SNDK」，共 4 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [INTC, AMD, MU stocks hit 52-week highs today: What's triggering the rally? - MSN](https://news.google.com/rss/articles/CBMimANBVV95cUxNWnBwXy11U0pvUXdLcE5sSkpudVFPVVRVRVhCc1RBVEVHdFRFVG1KSWlnWGt0bFo3ZkJNSFlwR2JPNXFkcERmLTJLYXJsTlpGRUZIcjRpOWROVFN2YVU2d1AxY2U1ZldUUk9abDBzN0hyZ0RPZG1KaWh0Y1dmYTcwb3piNzZFWF9zMUdjSWFSVVVndlNPYVpJSjJtNlc4YmZLc3N3cjJtTXNsYU5jQjFGQjA2Z213aUUwRE1nc0J3ZVVNb1Z0TmlnUU9LamRrNjhWR28yM3Q2UjBpZEdQUlJfQTlZQlRycnExTGdiSEZBTmxmUHFPTjMwTFFRR1RqVkZWYmFFTVZUeHBycE9VdndfcWwtTW84YlF6UGVPbGcwdmpzSTVURGxOc21PZ2ZrOFJCQ2NEVG9IY2JZWnF6eng5MDFkemhiNWUwRWpfU243MjF1Vnpuc2FrcWJyMnBWNENhVnVjOHFGQTdEVlJsZ0tSRHYzdzFkel9lZXI1LWhhZlVtTFBYWURBOVdROFVzZzZTRWxBQXlVOVY?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 09 May 2026 21:55:23 GMT
- [Are SanDisk and Micron Too Expensive? Here's How You Can Invest in the Artificial Intelligence (AI) Memory Supercycle for Just $50. - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxOMjZxU0hyNU1WLXVVSS1PMHhIZUpXVFhGaGFza2NpTXdMaE80NkFDVC1RdkJjdFV2Y0JaMi1ubkRCX0lqM1NJb2UwSGZqQVZxOExRRzI5ZWR5TzQ1UlBFNHE3RmtYemtCSlRjbmJham03OVJwR29xLTZZM05RdjdZQlFaNU9GSEZqQkZSTmRteDBwYzB5NHNyUg?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 10 May 2026 15:45:00 GMT
- [Micron vs. Sandisk: One AI Stock Is a Buy, One Is a Sell, Says Investor - TipRanks](https://news.google.com/rss/articles/CBMipwFBVV95cUxQNS1TclpvZE9FTVg4eXlGVHYtYnFHemI3elM3VUFiWmU4ckJiRmRlMmpfci1HYm9maEp4WXh1eUV5ODhRVHluNm9zSFZwYjJfRkdKaldEdms2dG1OblE3d0FyOFZZV3l5MERZcGthMU5uWXEzREpoTEI1SGRra3F0d2FVZFVlOGpBX3QzOWtVMmRMWk1vb1BRWWpLWVBnb1JSTmpMc0Fibw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 10 May 2026 16:51:31 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：ARM vs. INTC: Which AI-Era Semiconductor Stock Will Reward Patient Investors? - 24/7 Wall St.；Apple Stock Week Ahead: AAPL Rally Faces CPI, AI and Intel Chip Deal Test - TechStock²；鉬在現代半導體與綠能產業的戰略地位為何？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.88 | N/A | N/A | 124.89 | 124.92 | -0.02% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 新聞直接提及 | +0.65 | +5.17% | +46.01% | 293.26 | 293.32 | -0.02% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.11 | +1.78% | +7.26% | 2,290.00 | 2,290.00 | 0.00% | 同向 | 66.26 | 34.57 | 410.73B TWD / 17.50% | 2026-05-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.11 | +9.87% | +18.11% | 91.30 | 91.30 | 0.00% | 同向 | 4.00 | 22.94 | 22.66B TWD / 10.80% | 2026-05-01 |
| NVDA 輝達 | 產業/供應鏈推估 | +0.08 | +23.40% | +12.60% | 215.22 | 215.22 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.08 | N/A | N/A | 455.19 | 455.19 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | +0.08 | N/A | N/A | 746.79 | 746.81 | -0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.08 | +11.09% | +31.62% | 1,562.34 | 1,562.34 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC、Intel」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AAPL：新聞直接提及「AAPL」，共 1 篇新聞命中。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 2 篇新聞出現相關標籤。 方向判斷命中詞：rally。

### 主要來源

- [ARM vs. INTC: Which AI-Era Semiconductor Stock Will Reward Patient Investors? - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiugFBVV95cUxOUFp0eFZTZFhYcUlrSmoxSVp1V284VXVhdjhuOFhWdmN6YUVHdFBqVnNHOG4xS0tUcVAzN2ZzZ0Vjd2tZdDV2RFF3bUlxR2F2NjlnWHp5eWFyMG03S0ptSjFmZ2pua0JWMjhYLXJiRldxZTcwNzIxYms5Ql9fd1pFOVZCSkNLeHZweElIOEFvWm9DbjBrY0EtX2RPblQ4azJUN0EyNnNkLVdsZm5SNGloa1BSQ0NKOGFoZlE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 09 May 2026 21:11:10 GMT
- [Apple Stock Week Ahead: AAPL Rally Faces CPI, AI and Intel Chip Deal Test - TechStock²](https://news.google.com/rss/articles/CBMilwFBVV95cUxOMW1aTUJSUFk5SzVmN001NXFRSG9ZSUI1M0hjR1ByWVAyaDg1aFJYV1N4RHV0cGVNSDl4UUVLYnFONnNKNS1xaFhIV1V0ZF9sZnBEcWVYcDJuenNEMUpmYWVWekVKWF9hMXBuT0NVbFVLWW5sV2k4NzBnVnlqMHhDVjFhTmUyWEd3dnlST3VfZS1FUlFXaFlZ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 10 May 2026 12:23:39 GMT
- [鉬在現代半導體與綠能產業的戰略地位為何？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMihwFBVV95cUxQRFNYRm5wS3JxdDBLQzdfUzVCbHRKSGxmZElYS3dSLUFZR0VJYzFSX0lOWm9xaE9KRlhZcFZpYUFfWV9BaXpzak5ieVh0T0l4aDk1VDVZaDRCMFlhSnd6U3RObUtoMU5sN2Z2RGxpLTRmVWNxMGVvYTJFM0NjVVV1S2pYY1NWZjg?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 10 May 2026 09:10:44 GMT

## 新興題材：B729

摘要：新興題材：B729 相關新聞集中在：個股動態報導內容-A5484CA0-4338-4C8D-B729-3A6C27904444 - pscnetsecrwd.moneydj.com

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-A5484CA0-4338-4C8D-B729-3A6C27904444 - pscnetsecrwd.moneydj.com](https://news.google.com/rss/articles/CBMimgFBVV95cUxOTUlUeTRkU0xtU3lQLUt1M3JWTWxVdDNkU0F6S2liNTZuT1dNOG4xNVg5bVlwQWxXcWVTNUtydGhWSUxLWFp0WU0zVDcwdHhqV0liMGhWUVphaHhKUVc2LVloOGRuRGVOTE1tMWlRMWhPZHBGUS0xMW0wRm9pYUlRTU9FbHpubENhTzM1VDdUd2VPcm80WFZmdUpR?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 09 May 2026 20:18:18 GMT

## 新興題材：AI伺服器

摘要：新興題材：AI伺服器 相關新聞集中在：同業股價表現-電子-AI伺服器-台股 - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [同業股價表現-電子-AI伺服器-台股 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMiaEFVX3lxTE5kXzVkeWE2S3ZyWnFmaGFUcy1TUHoybTE4eWd4S2JxTDJ2OWxmc24wUUd3SWhqSXFVUDVYT0QzSzVMVjVpd3Q0U0E3UHdUUWxKX3haYkxFTjhMUnpvRDhHaGpTWmlqUDBZ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 09 May 2026 10:30:36 GMT

## 新興題材：三大晶片

摘要：新興題材：三大晶片 相關新聞集中在：三大晶片巨頭搶先佈局 PCIe 8.0 對產業競爭有何意義？ - TechNews 科技新報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [三大晶片巨頭搶先佈局 PCIe 8.0 對產業競爭有何意義？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMib0FVX3lxTE5IaFN5LS1Udm9jUWMzR3Ffb29SN2hGR2xwUmxFRk5qMF9rUHdGckN4UHNnRURadWpOckFGaThaZHNNa1NCSjBYQkJQZ1J2R043cGFTM0QzMXZsTW1QVFlJQTVocDJQWEtsbW1FeFFiMA?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 10 May 2026 11:14:57 GMT

## 新興題材：4月營收

摘要：新興題材：4月營收 相關新聞集中在：4月營收飆歷史新高！國家隊單週加碼「航運股這檔」2.2萬張 旺宏、台化、京元電全打包帶走 - Yahoo股市

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [4月營收飆歷史新高！國家隊單週加碼「航運股這檔」2.2萬張 旺宏、台化、京元電全打包帶走 - Yahoo股市](https://news.google.com/rss/articles/CBMi7AJBVV95cUxOWXF6TWJVS0NzM3Q3MVkzN2E0dnJKZ3hPZ0RlbS1FbmVWdUF0SzRJVVpzblFVajJteWxQMGNaN2tfZTQyXzlVTTZ0NGNGdlpSU1JGQkhBdVhJNVQ3YzAtaFU1Ul9NNW1oenU3QzBic0hSd09kczVvcHgwWnRrdG92UkhoWklzY0xSOC16dmRwLVExMUxlWnZWNGpyWnVpX2NRWWpDVmgzNFdBNWJQRkxlNHFtdHoxUFRydUNhdXUtX2xpdWQ3UHpHWk9aOXFHVktfUHR0b3JYZGRGNVRrcVk3a1M0NWlCTzFPdkJYVFFMLTB4QVdrTjJSX2Nlc2ROZUQwWjBHTUJ1Y3NiRjZ4YjM5THNISExDWXlMTnR3bk9aTEdaRElJQ09DTHVYdEMxVld1dEpZNmp0STIxNW1RX0VfU3A4RXRtUUlmbXQtbDdNNkJoc2dNZWxmMDhCU01ibC04VVRTSHJNVGNYREk3?oc=5) - Google News source discovery | Yahoo 奇摩股市 Sun, 10 May 2026 12:30:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
