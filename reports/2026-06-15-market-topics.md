# 每日股市熱門話題分析 - 2026-06-15

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜正向｜熱度 3｜市場確認 100.00｜同向 1/1
2. **利率與成長股估值**｜負向｜熱度 4｜市場確認 N/A｜同向 0/0
3. **關稅與供應鏈轉移**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
4. **半導體與晶片供應鏈**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0
5. **AI 伺服器與資料中心**｜負向｜熱度 13｜市場確認 27.75｜同向 2/6

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.87（樣本 7）
- 5日相關係數：0.56（樣本 7）
- 同向比例：3/7

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 100.00 | 1/1 | 0 | +20.26% | +26.98% |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 關稅與供應鏈轉移 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 27.75 | 2/6 | 2 | +1.47% | -1.60% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：代工廠成本升高可能再漲價 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-06-01 | -0.92 | -0.72 | +16.67% | 6 |
| 2026-06-02 | 0.08 | 0.05 | +72.73% | 11 |
| 2026-06-03 | 0.48 | 0.62 | +90.91% | 11 |
| 2026-06-04 | -0.38 | -0.30 | +85.71% | 7 |
| 2026-06-05 | 0.31 | 0.93 | +50.00% | 6 |
| 2026-06-06 | 0.12 | 0.06 | +45.45% | 11 |
| 2026-06-07 | -0.32 | -0.20 | +45.45% | 11 |
| 2026-06-08 | 0.36 | -0.68 | +60.00% | 5 |
| 2026-06-09 | 0.07 | 0.19 | +25.00% | 8 |
| 2026-06-10 | 0.17 | 0.15 | +53.85% | 13 |
| 2026-06-11 | -0.05 | -0.08 | +14.29% | 7 |
| 2026-06-13 | 0.87 | 0.98 | +100.00% | 4 |
| 2026-06-14 | 0.82 | 0.98 | +100.00% | 3 |
| 2026-06-15 | 0.87 | 0.56 | +42.86% | 7 |

## 歷史回測摘要

- 回測日期：2026-06-15
- 近5日 3日相關：-0.38
- 近5日 5日相關：-0.27
- 同向比例：+28.57%
- 權重狀態：未調整

- 方向準確度：+28.57%
- 信心排序準確度：-0.38
- 診斷：方向與信心皆需修正

調整原因：近 5 日有效樣本 7 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits；Why I'm Still Holding Every Micron Share (NASDAQ:MU) - Seeking Alpha；Is Sandisk Corporation (SNDK) A Good Stock To Buy Now? - Insider Monkey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.68 | N/A | N/A | 981.61 | 981.61 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.58 | +20.26% | +26.98% | 1,980.10 | 1,980.10 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.50 | N/A | N/A | 511.57 | 516.10 | -0.88% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.50 | N/A | N/A | 124.57 | 124.57 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +2.82% | +15.80% | 205.19 | 211.14 | -2.82% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU」，共 2 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK」，共 1 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits](https://news.google.com/rss/articles/CBMi0AFBVV95cUxOWm5KdEIwSXpyY191UEhDa1V6NVpWa01UbmpJeWRIV0ttT080TmpDNEhISW5TWkQwUzBVYzBqSHJPWXRVNVJCampoWWRlYmhKVkhIeHBJLS0wLW5Ua09GQnRORXpFcW5qTEJkcnJGcW55aU5rOFVOLUFMbjRPZEpWT3A2ZllucnM0SU9JNEdrNUwyc3V2WHAtNFk3VHl4R1F6SkZRMFpleEE2Zl9MdW4tSEpMMnFGZ2hQZURWQ3B1WDlPR1BhRjJELVN5ODJWYVR3?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 14 Jun 2026 04:44:55 GMT
- [Why I'm Still Holding Every Micron Share (NASDAQ:MU) - Seeking Alpha](https://news.google.com/rss/articles/CBMihwFBVV95cUxOdzAwSXI4NllzenZjdWd2OWNIUEdrcmt4SHh4cUJ1X0hxUUMtS0FESEtJV290NkNJT2lSalRENERVOEQ4YUNhV0drd0llYmotdFE2cEdKSnlKalBDODQ0ckE5bTY5bmVFRnNVZzlQQlM0cXpFNmNlMGhnR2hmSEozNG5Hb3BXZW8?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 13 Jun 2026 13:00:21 GMT
- [Is Sandisk Corporation (SNDK) A Good Stock To Buy Now? - Insider Monkey](https://news.google.com/rss/articles/CBMingFBVV95cUxQSXYyNm4xbFYzUHYxQnkzbllCV01jbE53dGlMQk1Ib3lfanVJODFTQXJVbVJXMmVzeHpCZF9SMG84dllTblNadVRUTjkyWjNQWW5rd0pxTU1HM0lBS0Rlem5tZ1lROW5KVXk5MHd3T0hVWGpsalFEN1MxQ3lGTDBjSFZoRXZldG5hQ0tDeGRRMXpRQVF1SEl2NXpWZzYtUdIBpgFBVV95cUxQY2JyelJKRXVjMHRBTlpyVWhkTS1xRTF0bDFtakxaWTFzQW1VdGZRdVVQTXRPWkR0b2lJTVdnY1VuS1hCekh5NlRvZUVOd2ZUdE9WQWVQbzJJNDVFWjZlbzVNcXA2WlVlNUxRR3lYV2JLd19MS202NFdvak5ab0dmYzdiNVppMVlxdTBrbW50Sk8zamdGaElFRldmUDZ3TEhiQ3R1Uk53?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 13 Jun 2026 13:46:42 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：晶圓代工廠成本升高可能再漲價半導體通膨延燒| 產經 - 中央社 CNA；晶圓代工廠成本升高可能再漲價半導體通膨延燒- 產業 - 工商時報；高盛警告美股最大風險！10年期美債殖利率升破5% AI牛市恐面臨估值重擊 - news.cnyes.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | -0.51% | -22.88% | 390.74 | 506.69 | -22.88% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [晶圓代工廠成本升高可能再漲價半導體通膨延燒| 產經 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1DdHJCdDNoWGNBZGE4SERJZVNRaHlSQzYwci1FTkQzSC1PTWRCNUdRekJHeUI1YVhzNW81YUpkc2N0MjZIbDl4UVZkQV9vWm5QZVlYUEhuVWRYQXQ3T0E?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 14 Jun 2026 01:49:00 GMT
- [晶圓代工廠成本升高可能再漲價半導體通膨延燒- 產業 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1uOE9Hb0tiUlBoUm1jQzFBZ2RvNTdRZlRMRHdWNWw1ejFQOU5QRTVDX0hPeUVOaldMSGYzZ1ZaRjlseENJVm9RZnNESnM4Y3pTWDlKdE95eERCX21DZENv?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 14 Jun 2026 02:10:00 GMT
- [高盛警告美股最大風險！10年期美債殖利率升破5% AI牛市恐面臨估值重擊 - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTE5CamM0VUhraGdJa2Jxb1FmOTUtT0VIS2NNeUZMUGZudlR6Zy1vbVJrLVRVSGUzSVQtVENJMFVTOWxIVmhfOEZFTThCRzFCTzA?oc=5) - Google News source discovery | 鉅亨網 Sun, 14 Jun 2026 20:41:18 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：高美可科技擬投資近14億捷克建廠強化半導體供應鏈| 國際 - 中央社 CNA；半導體業可視化防線，對供應鏈有何啟示？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +10.20% | +25.41% | 291.13 | 312.06 | -6.71% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | -6.13% | -8.44% | 260.50 | 289.00 | -9.86% | 不適用 | 14.13 | 18.50 | 859.41B TWD / 39.57% | 2026-06-01 |

關聯理由（前 3）：
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [高美可科技擬投資近14億捷克建廠強化半導體供應鏈| 國際 - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5FZlhkNVpQbmxMSTRod2FXNTFVbjR2NmF2NUx4LXNfckxud0drZHFrdWtSMU0tLUhLaXJOd2JFYmpOV09abFhFM051ZUFma3YybUxiVm41Uy1OdHVqRjY4?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 14 Jun 2026 07:45:00 GMT
- [半導體業可視化防線，對供應鏈有何啟示？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiWEFVX3lxTE9LUmsxak1jUkRSQmZBSXdkLTdaamxURV9CaFUyaWt2RWt4UVBlOTBDc2wyWTZlcWVHckFMZUs4ZUpmSy1EZmcxZUpLSTNXYkt0TW1rQjdtT2k?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 14 Jun 2026 12:48:40 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel Shares Climb Again on AI Foundry Optimism, Pushing INTC Closer to Highs - TechStock²；代理AI引爆CPU斷貨潮！伺服器供不應求半導體下半年景氣看旺- 產業 - 工商時報；陸半導體併購 聚焦兩領域 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 124.57 | 124.57 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +0.22% | -2.33% | 2,310.00 | 2,355.00 | -1.91% | 不適用 | 74.39 | 31.06 | 416.98B TWD / 30.09% | 2026-06-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +4.71% | +1.52% | 133.50 | 144.50 | -7.61% | 不適用 | 4.00 | 33.54 | 22.94B TWD / 17.78% | 2026-06-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +2.82% | +15.80% | 205.19 | 211.14 | -2.82% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 511.57 | 516.10 | -0.88% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 981.61 | 981.61 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | +20.26% | +26.98% | 1,980.10 | 1,980.10 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -8.47% | +19.57% | 382.07 | 446.77 | -14.48% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 1 篇新聞出現相關標籤。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 1 篇新聞出現相關標籤。

### 主要來源

- [Intel Shares Climb Again on AI Foundry Optimism, Pushing INTC Closer to Highs - TechStock²](https://news.google.com/rss/articles/CBMingFBVV95cUxNWjUyaTRwT3MtcmhUUXp1cjFuSU95bmotOWJ5bjdFYm1VakoyeXNUbk5vT2pzUFY2cFRENk1CdC1iVFVRTUZvbUp3RkdJTmxudzJxUktRWUZZd19ROVFCelFGVHFUbUtHUi1qOFlwT21VR2l2R3FRT1o0WlFtUFZHSkZELUh1bm9LdzZHQklIZUFWdjVVSnkzZ19zOVVlUQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 14 Jun 2026 13:20:17 GMT
- [代理AI引爆CPU斷貨潮！伺服器供不應求半導體下半年景氣看旺- 產業 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBWOFRvdF95VHpOQXZjOWJnOXVzV2JmMXNnTXIxU1A1VnBiN3RSV2RrUlRNVnZsdjFCNm9MbjhMa3d1QnJRSk93MFZhMEJpbFlhdGJXMEF5bmpCd2lhdXlj?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 14 Jun 2026 01:57:00 GMT
- [陸半導體併購 聚焦兩領域 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE03bEZfdmdNZEU5dWVfZHM0WXhRZ1JMcThnNDA0NW5WTnh2Z1FxWDZ6bUVwN3FBQXAzUHctYlFNbW1Lb1JYWlpKNFZJMExTcjBid29UVEQyTTVfQdIBX0FVX3lxTE9EY081U3FnMndva1BOU2x1QzdqYi1aY2VZU1dfMlRxUFU0VXJLVTFiSzlPeVpOVXdHb20tZ1lOeWxOcWlESmpmMDdleUdzWVREUHp6MF9JREhneDNtcFNB?oc=5) - Google News source discovery | 經濟日報 money Sun, 14 Jun 2026 18:11:13 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Why Intel, AMD, Arm, and Other Artificial Intelligence (AI) Stocks Popped Today - AOL.com；Intel Shares Climb Again on AI Foundry Optimism, Pushing INTC Closer to Highs - TechStock²；企業應如何因應 AI 導致的員工批判性思考退化危機？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.68 | N/A | N/A | 124.57 | 124.57 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.63 | N/A | N/A | 511.57 | 516.10 | -0.88% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | -0.03 | +2.82% | +15.80% | 205.19 | 211.14 | -2.82% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.04 | +0.22% | -2.33% | 2,310.00 | 2,355.00 | -1.91% | 未明確 | 74.39 | 31.06 | 416.98B TWD / 30.09% | 2026-06-01 |
| MSFT 微軟 | 產業/供應鏈推估 | -0.03 | -0.51% | -22.88% | 390.74 | 506.69 | -22.88% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -8.47% | +19.57% | 382.07 | 446.77 | -14.48% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.02 | +3.69% | +2.25% | 590.00 | 611.00 | -3.44% | 背離 | 10.86 | 54.78 | 63.03B TWD / 28.57% | 2026-06-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.04 | -6.59% | -2.79% | 4,180.00 | 4,310.00 | -3.02% | 同向 | 62.91 | 66.61 | 47.43B TWD / 4.99% | 2026-06-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel、INTC」，共 2 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：暴跌。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。 方向判斷命中詞：暴跌。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：暴跌。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Why Intel, AMD, Arm, and Other Artificial Intelligence (AI) Stocks Popped Today - AOL.com](https://news.google.com/rss/articles/CBMidkFVX3lxTE5EX1pfT3Zkc1RMMU9NTVo1b2dpV1ZFS1Q1ODBrVjVuZ2RLTlJ2Z1pfWEpDeHcyVFVqdkJlczlZM19GSThNc2kyczljM1dGS0xHRWdsNkVqcExqaGRfTmlBSGgtSDZRSjBkcFhLX2xRRHdmSmJmQ1E?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 13 Jun 2026 01:24:17 GMT
- [Intel Shares Climb Again on AI Foundry Optimism, Pushing INTC Closer to Highs - TechStock²](https://news.google.com/rss/articles/CBMingFBVV95cUxNWjUyaTRwT3MtcmhUUXp1cjFuSU95bmotOWJ5bjdFYm1VakoyeXNUbk5vT2pzUFY2cFRENk1CdC1iVFVRTUZvbUp3RkdJTmxudzJxUktRWUZZd19ROVFCelFGVHFUbUtHUi1qOFlwT21VR2l2R3FRT1o0WlFtUFZHSkZELUh1bm9LdzZHQklIZUFWdjVVSnkzZ19zOVVlUQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 14 Jun 2026 13:20:17 GMT
- [企業應如何因應 AI 導致的員工批判性思考退化危機？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMikAFBVV95cUxOQUkwWXItbVRyZnpWRmd1cUwxUGs5cnFsQnJEZ2I5dlFIelVSUUptVkl3Q2dPanRaZzdESjMxdmVCUjJuNnpkOGlwa1BNVUgxZldVazFqbkl6aWNHYUV0azQxekRrbkpFZW9DWGNLRTlWTmpfMmlvU0ZiN1NNMjhoQTduVjcxWlZPMGFZUGN5RnY?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 14 Jun 2026 17:40:05 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股4月大漲22%　銀行業股市未實現利益飆新高 - 經濟日報；台股「大媽行情」有影 第四勢力崛起本周決戰44,933點 | 市場焦點 | 證券 - 經濟日報；台股本周面臨三變數 抗震看國家隊動向 加碼個股將成市場定海神針 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股4月大漲22%　銀行業股市未實現利益飆新高 - 經濟日報](https://news.google.com/rss/articles/CBMigwFBVV95cUxPNDVPUUVNbWhEOEhnN2JKcVpUQ2NEYS10YVMyOXpRa1NjQXJKRXF5d3M0ZnZSaDdvX2JOSlQ0S0pxYmNPWG5Dcm5HUzZWTU5RTzltc01ESEVueHhsQ2ZvWVM2NXFCLUZhT1RodkUwaGlpZHNRS3FqWTBKNkFSMjRKaGI5a9IBX0FVX3lxTFAzQkVQVUJpTnkzalI3NV9sTHByYmRuUXFBa2UxQnctRDJpTHoyRGRudC0tT3NpVURFbVRQVHNsQnRMeExEUS1qcnVqSFJ0QXBtZEFNbGtIb2FUdkpsY09r?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 14 Jun 2026 12:45:44 GMT
- [台股「大媽行情」有影 第四勢力崛起本周決戰44,933點 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9LZ0xYSVd0bk5uS2oxRjdTdUVxRWdiNE9XYjQ2RFNvcVFCQTlHT01BellNRjJESFNBeTJOekozWW8tcUdackhlOGdqSmMwUTQ2Z2d4ODFsOEhQdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 14 Jun 2026 17:23:40 GMT
- [台股本周面臨三變數 抗震看國家隊動向 加碼個股將成市場定海神針 - 經濟日報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE85M3NWSjRVcy1TUzUzd2lmLXpZc3V4TVp5cXZvR3EzaHVYM2lfTlRHcmNham9CeVdFMzBnWFJDaE00TzNxSFFSVzBUWUFyRHp5WUsybnFDa05BMzRFRDRF0gFfQVVfeXFMTzkzc1ZKNFVzLVNTNTN3aWYtellzdXhNWnlxdm9HcTNodVgzaV9OVEdyY2Fqb0J5V0UzMGdYUkNoTTRPM3FIUVJXMFRZQXJEenlZSzJucUNrTkEzNEVENEU?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 14 Jun 2026 18:56:24 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：法人專欄分析內容-台股 - MoneyDJ；同業股價表現-電子-AI伺服器-台股 - MoneyDJ；法人專欄分析內容-台股 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [法人專欄分析內容-台股 - MoneyDJ](https://news.google.com/rss/articles/CBMijgFBVV95cUxNdDZ0UkQyaXgwZlNvcEJlN3hseXlRUmlqd0pQSmRLZGk5Y2RCQzVxcWdRbHpsQV92TGV3N250ai1vaEFodjhHSmpMNFJuLVpWdjAzbG5LaTNHWFRCbUFfY3g5UVJTcmxUcHNNRjh4MzRRRU5ObXZUNDBGNEpLbmZYTUlMNnlmaE9VdTNHb1pB?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 14 Jun 2026 16:03:52 GMT
- [同業股價表現-電子-AI伺服器-台股 - MoneyDJ](https://news.google.com/rss/articles/CBMiaEFVX3lxTE1Sdms4eWdyalpVSHJEWTRySXlZRzJTLUxiNXlnMnRsRjQ4aFhMVlBPVVdXUE1rVUN0UU1xQTZLMVVWZGtFQ21NdmlEY3ZGMHQ3RGdCRXhpV0FLdkZkczI2UDdkQ19HaXBW?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 13 Jun 2026 21:52:52 GMT
- [法人專欄分析內容-台股 - MoneyDJ](https://news.google.com/rss/articles/CBMilgFBVV95cUxNRWVSZ1NuT0ZfdU9uTjR1d0NrVkcxTl9HTklNX3kwdjk1NjhqamNGM3llTnYydVFqV0p5c2Z1ZnhXckxhQUFFY01PcXYtUG1FZGthVkF2OUFGQnZuQ21RU1ZjSmVFdnJOMnFYX2ZidkczV1piYjVCRGFrRk5VVFlmdVZ4dXRuWHRWVXFBMEpQSUNEcjhYUEE?oc=5) - Google News source discovery | MoneyDJ Sun, 14 Jun 2026 16:03:52 GMT

## 新興題材：代工廠成本升高可能再漲價

摘要：新興題材：代工廠成本升高可能再漲價 相關新聞集中在：晶圓代工廠成本升高可能再漲價半導體通膨延燒| 產經 - 中央社 CNA；晶圓代工廠成本升高可能再漲價半導體通膨延燒- 產業 - 工商時報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [晶圓代工廠成本升高可能再漲價半導體通膨延燒| 產經 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1DdHJCdDNoWGNBZGE4SERJZVNRaHlSQzYwci1FTkQzSC1PTWRCNUdRekJHeUI1YVhzNW81YUpkc2N0MjZIbDl4UVZkQV9vWm5QZVlYUEhuVWRYQXQ3T0E?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 14 Jun 2026 01:49:00 GMT
- [晶圓代工廠成本升高可能再漲價半導體通膨延燒- 產業 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1uOE9Hb0tiUlBoUm1jQzFBZ2RvNTdRZlRMRHdWNWw1ejFQOU5QRTVDX0hPeUVOaldMSGYzZ1ZaRjlseENJVm9RZnNESnM4Y3pTWDlKdE95eERCX21DZENv?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 14 Jun 2026 02:10:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
