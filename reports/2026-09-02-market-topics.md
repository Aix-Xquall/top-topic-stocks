# 每日股市熱門話題分析 - 2026-09-02

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **AI 伺服器與資料中心**｜正向｜熱度 16｜市場確認 70.57｜同向 4/6
2. **綜合市場情緒**｜正向｜熱度 38｜市場確認 41.84｜同向 2/3
3. **記憶體與 HBM 供應鏈**｜中性｜熱度 6｜市場確認 96.01｜同向 1/1
4. **散熱與液冷供應鏈**｜正向｜熱度 3｜市場確認 86.16｜同向 2/2
5. **半導體與晶片供應鏈**｜中性｜熱度 9｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.29（樣本 12）
- 5日相關係數：0.24（樣本 12）
- 同向比例：9/12

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| AI 伺服器與資料中心 | 70.57 | 4/6 | 1 | +7.97% | +2.80% |
| 綜合市場情緒 | 41.84 | 2/3 | 1 | -1.61% | +1.96% |
| 記憶體與 HBM 供應鏈 | 96.01 | 1/1 | 0 | +8.67% | +8.95% |
| 散熱與液冷供應鏈 | 86.16 | 2/2 | 0 | +5.38% | +12.27% |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 關稅與供應鏈轉移 | N/A | 0/0 | 0 | N/A | N/A |
| 先進封裝與 CoPoS | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價呈負相關；應檢查正負向詞庫，並降低新聞直接提及但股價背離的權重。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-08-19 | -0.23 | -0.33 | +30.00% | 10 |
| 2026-08-20 | -0.72 | 0.06 | +50.00% | 8 |
| 2026-08-21 | -0.48 | -0.45 | +61.54% | 13 |
| 2026-08-22 | N/A | N/A | +50.00% | 2 |
| 2026-08-24 | -0.94 | -0.77 | +60.00% | 5 |
| 2026-08-25 | 0.01 | -0.58 | +35.71% | 14 |
| 2026-08-26 | 0.08 | 0.22 | +50.00% | 16 |
| 2026-08-27 | 0.38 | 0.11 | +54.55% | 11 |
| 2026-08-28 | 0.14 | 0.12 | +56.25% | 16 |
| 2026-08-29 | -0.10 | -0.01 | +40.00% | 10 |
| 2026-08-30 | -0.52 | -0.04 | +23.08% | 13 |
| 2026-08-31 | -0.41 | 0.29 | +40.00% | 10 |
| 2026-09-01 | N/A | N/A | +50.00% | 2 |
| 2026-09-02 | -0.29 | 0.24 | +75.00% | 12 |

## 歷史回測摘要

- 回測日期：2026-09-02
- 近5日 3日相關：-0.07
- 近5日 5日相關：0.20
- 同向比例：+52.63%
- 權重狀態：已調整

- 方向準確度：+52.63%
- 信心排序準確度：-0.07
- 診斷：低相關

調整原因：近 5 日信心分數與股價關係偏低，提高價格確認，降低寬題材推估。；關鍵詞×公司後續樣本有效 5 筆，未達 30 筆，不調整樣本權重

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

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel (INTC) Stock May Be 5% Overvalued As New AI Chips Debut - simplywall.st；Semiconductor stocks fall as global bond yields hit 1-year highs, pressuring AI growth valuations. - Pluang；AI 工具氾濫致品牌同質化，行銷大賽勝負已不在技術而是原創力 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.54 | N/A | N/A | 88.97 | 114.68 | -22.42% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.06 | +8.67% | +8.95% | 217.44 | 217.55 | -0.05% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.06 | N/A | N/A | 459.61 | 516.10 | -10.95% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.06 | +1.24% | +1.67% | 2,440.00 | 2,440.00 | 0.00% | 同向 | 86.28 | 28.28 | 467.58B TWD / 44.69% | 2026-08-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | +27.57% | -1.12% | 501.02 | 513.53 | -2.44% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -2.14% | -11.44% | 369.68 | 446.77 | -17.25% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.03 | +0.83% | +3.21% | 610.00 | 680.00 | -10.29% | 未明確 | 13.92 | 44.14 | 73.78B TWD / 43.15% | 2026-08-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.04 | +11.64% | +15.53% | 4,315.00 | 4,315.00 | 0.00% | 同向 | 60.69 | 71.26 | 48.47B TWD / 12.16% | 2026-08-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：fall, growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：fall, growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：fall, growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel (INTC) Stock May Be 5% Overvalued As New AI Chips Debut - simplywall.st](https://news.google.com/rss/articles/CBMixwFBVV95cUxOVkFkeTlCZE12N2FKMnZ1YlpOdkp1ZEVFZTRsc0h2bHFsY3k1VE80NkVMS0RLQVB2V0puOU1xRHVSZHJzWjk4OVFWb2swTUZzWnI5Wnh3NDNTbF9UWGduMTFxN0dvcVhSaXlvekE3TU1jNjJfSWNEdGpiN2ItRldtdzJMQlMxejQ3T3J5OERDS0hQU09aYXQyRUhKOERpck1QdWI3X0R2WG9wQ1JqQUhvQ181SkdWOHZxY0hCaTd1QWc4OXFWcFpB0gHMAUFVX3lxTE55SHVWbVJrM2MzNlVzbEI3dnJLaUs0VERtdGU4ZEc1NkZMZ1A5OU5IN2MtVmtvMlh2aThCcGVfTHlpUzlGVkIxT2NETHBzWWxtOGZ4dU9OYllRd01rNDFOZ0Z2NGIyaEYwNjBDTVNaVkZseTBBQ08zdEdnUDZiTE1uSlBDNTE2LXpGYjZId0ZpbXlOREc3bFRhR2QzeTRTeXQza2FldkFrdnZGMGhFMUlZM1VBUkRYaGloVl9rQlU0Snl3TXJXdV9XTVY4bg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 01 Sep 2026 16:17:31 GMT
- [Semiconductor stocks fall as global bond yields hit 1-year highs, pressuring AI growth valuations. - Pluang](https://news.google.com/rss/articles/CBMirwFBVV95cUxQVHo1aHZwaDliYkhsZGNpbzlwRUh0dHUwV1hNUFd5VndsdlI1MW1oZlVPTTIzZ1hlTVpXYkZaSGRzLUcwZzRoSFNEbjZVdThGWTRsc2hxNmZJOXhsMWkzVDlJdUsyRUpzVFNJbzczYTg1X2tRUHBTNU5ZZjY3RUk4V0QxcC1ZZXVxcWk4OURwWVVQRTVGTWgweFpEbmhrSi1jcl9ORTBtem9CYm9WalVr?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 01 Sep 2026 13:38:55 GMT
- [AI 工具氾濫致品牌同質化，行銷大賽勝負已不在技術而是原創力 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiigFBVV95cUxOdDRDTXZsSC1kemlVT04yd1plZXVFb1VDZzJtY25salM2cndWN3JPdUk4Q1hESzY3Mi1IeEo3M3FRbmdaOG1jQlFleWV2N1V6cVNkWUV0SUpUaGZWeEFjV1NHaG5LbHU4cElPNFN4eEZiRUluT1lrZjlVNm9rQkhWMjhRbEZaR2twaGc?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 01 Sep 2026 23:26:15 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股往新高挑戰 分析師看好這五族群可以買、欣興也被點名 - 經濟日報；台股大滿貫9月開門紅 台積電、聯發科領漲 將蓄勢挑戰48,218點新高 - 經濟日報；台股8月開戶數再創新高 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | +0.42 | +1.24% | +1.67% | 2,440.00 | 2,440.00 | 0.00% | 同向 | 86.28 | 28.28 | 467.58B TWD / 44.69% | 2026-08-01 |
| 2454 聯發科 | 新聞直接提及 | +0.42 | +11.64% | +15.53% | 4,315.00 | 4,315.00 | 0.00% | 同向 | 60.69 | 71.26 | 48.47B TWD / 12.16% | 2026-08-01 |
| 3037 欣興 | 新聞直接提及 | +0.21 | -17.71% | -11.32% | 971.00 | 1,110.00 | -12.52% | 背離 | 15.49 | 64.65 | 16.25B TWD / 43.69% | 2026-08-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。
- 2454：新聞直接提及「聯發科」，共 1 篇新聞命中。
- 3037：新聞直接提及「欣興」，共 1 篇新聞命中。

### 主要來源

- [台股往新高挑戰 分析師看好這五族群可以買、欣興也被點名 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE93Mm5QUy12TlVCc2wyamZtLXI2MkJOMmlEV2JIWHVCWUNUWVBjTEZtdklJd3FpMGJBSnVsVFM2RERmZXVLakhyR0FORjVNX3FvWmdHOXQzbllmd9IBX0FVX3lxTE9IcWIxU1dMMENMaFFONEctbWxVSllyWG9pR2RLbk5EWHRhcS1RTjdNeWpjT2FiemE2R1BLbFliV2VlakkydUM0T1lfWmhjbG1fdWVFQms0b0VDa1Z1cDRF?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 31 Aug 2026 09:00:00 GMT
- [台股大滿貫9月開門紅 台積電、聯發科領漲 將蓄勢挑戰48,218點新高 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1RbVR2cXZQRjI2TUxlNHdLTmpqT1F4ZlpWZmJyVklZWHV4YllUWWVyVzBEN0p6SjlJMV9xSjJWMnNzWUtXd056UmxhbkVab3ZzdnV2Slp6TG05UdIBX0FVX3lxTFBqdlpEXzE5X2w2R1gwZGJwd1IteF8tLUlCeThQWTZXODEwWlR2Tk1MeVdMOHltRmUtRjRXRGxULWYtLUsyd3FWZFdKUDRiQmZYN2NEYm5UWmd1LVlFN240?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 01 Sep 2026 03:00:00 GMT
- [台股8月開戶數再創新高 - 經濟日報](https://news.google.com/rss/articles/CBMid0FVX3lxTFBrNWxkQmVKTVMyMEpzeGtsZHJIN2VCY0VvUllvblpLaXdxRnhyVE1xdV9MS0dWTnBnTWJRVjB0a3k1aTZpZnlmUkxSVjJFTmlrZGMzdFRSSWN2emVnOFgxWERiWEdGMVlXVlNBZGNHSExMYmktVFJn0gFfQVVfeXFMTWpYNTBHZFRIMDItRnlPdDdENTVyMGJMNEJMa3FUQUQ2bUNoaVI0bG1UZGZRWmxndkl4SHJsZjhuelJ0RFhrVkE1WnFMeVdOeXRraWkxUTNpdG5fOGlzUlk?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 01 Sep 2026 17:03:15 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：MU, INTC, SNDK: Chip Stocks Rally After-Hours On AMD’s Blowout Report - Stocktwits；AI Memory Stocks Rally After Nvidia Earnings: SanDisk, Micron and SK Hynix Rise — Which Stock Is Best to Buy? - Mitrade；China's CXMT makes breakthrough in advanced memory chips: report (MU:NASDAQ) - Seeking Alpha

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 933.44 | 971.00 | -3.87% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | +3.50% | +3.79% | 1,536.87 | 2,335.00 | -34.18% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.37 | +8.67% | +8.95% | 217.44 | 217.55 | -0.05% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.36 | N/A | N/A | 459.61 | 516.10 | -10.95% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.36 | N/A | N/A | 88.97 | 114.68 | -22.42% | N/A | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：risk, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK、SanDisk」，共 4 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：risk, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：HBM。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [MU, INTC, SNDK: Chip Stocks Rally After-Hours On AMD’s Blowout Report - Stocktwits](https://news.google.com/rss/articles/CBMiygFBVV95cUxPeVlYaXJjQjNtTkNRQUxQTHhaLUFMbE80Uy1MeDBpV0FPdkg2SHRLdkdfVUpXM1NrNWhZSVZQQ01sa0o4T1hKdzF1clBFRlRWUmMwWGxQTDNVVFBpOVhObUc2MXpBeXBOZ0p3R0w5NGRNOHB4X0ZIXzhlT0NMbmhzc1RtdmJRTWhlRUhKSHpyVnpaU0VGMlJyU2tDcmdkTG1hWVJJbmtTVDREbzFfWDB4bjhuTGswN3lmdkdHQzY1dzFOVU41VGlBNlZn?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 01 Sep 2026 07:23:05 GMT
- [AI Memory Stocks Rally After Nvidia Earnings: SanDisk, Micron and SK Hynix Rise — Which Stock Is Best to Buy? - Mitrade](https://news.google.com/rss/articles/CBMifEFVX3lxTE9vM3huOXl5dmFRYXlSSDU0QkVBZnlybzJsTlBKTUMzclRQelFkTnRmNG5HcERRMERxYXp6UE91dXJCeXV3THhodllvaXBzSFktVmtXenpDNm1KQ25DWUdIOE5LQ0l0V3lEMTgwTmd1WnJEbVZYZl9OdzBBZ00?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 01 Sep 2026 06:31:12 GMT
- [China's CXMT makes breakthrough in advanced memory chips: report (MU:NASDAQ) - Seeking Alpha](https://news.google.com/rss/articles/CBMiogFBVV95cUxPWVZibXZYS2JsV1duVmdVbUFlUC1YSHhMRDRPaHo0bWVoUjVROGhmVUZDLXY3cWloWXQyZkp3MHFSekdYQ0l0Mmp6Si14S1dYZEdybzY1T0UyZlI0aXNBZV9fVjFqRGhXSE41MWlaUlhlYjdIbDZUZ3A5X2xKUTJYOUlNTkctUmN1dEpzcTZyTUZFUlBXcmV3MXc4MUNVLUdxZnc?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 01 Sep 2026 07:45:38 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：奇鋐小金雞受惠輝達　目標價至3280元 - 鏡週刊Mirror Media；歐系競爭對手良率出包！「奇鋐小金雞」搶攻QD市占 目標價上探3280元 - FTNN 新聞網；雙鴻展望看更樂觀；明年營收增幅優今年- 新聞 - MoneyDJ

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.51 | +2.10% | +15.59% | 3,410.00 | 3,410.00 | 0.00% | 同向 | 75.13 | 45.45 | 18.59B TWD / 57.39% | 2026-08-01 |
| NVDA 輝達 | 新聞直接提及 | +0.42 | +8.67% | +8.95% | 217.44 | 217.55 | -0.05% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐」，共 2 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：受惠。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [奇鋐小金雞受惠輝達　目標價至3280元 - 鏡週刊Mirror Media](https://news.google.com/rss/articles/CBMiYkFVX3lxTE9HMUNULU5BcC1zd3h6RzhHaHJQVnp2T2xtX0NVNV9hQzJ6aDVZTTBUaFRSMERCYnhWSnVPSHRqTmlSRG1UeFM2ODltRzJQblJ5dUxxdDlBS3c1LWtDSVRwc2RB0gFiQVVfeXFMT0cxQ1QtTkFwLXN3eHpHOEdoclBWenZPbG1fQ1U1X2FDMnpoNVlNMFRoVFIwREJieFZKdU9IdGpOaVJEbVR4UzY4OW1HMlBuUnl1THF0OUFLdzUta0NJVHBzZEE?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 01 Sep 2026 17:00:00 GMT
- [歐系競爭對手良率出包！「奇鋐小金雞」搶攻QD市占 目標價上探3280元 - FTNN 新聞網](https://news.google.com/rss/articles/CBMiS0FVX3lxTE9zZkx6X0RtNjc1elU5c19BRW5wLUdnOHJuVjdjWEF0Zkh3WEUwWWxlYXF3U1dhay1zRks0ek1YTlczdHVGeEd2Zmd2NA?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 31 Aug 2026 15:30:00 GMT
- [雙鴻展望看更樂觀；明年營收增幅優今年- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQRHBRbGNIdmpoZFNwTlVRcTluRTlRWmltdzJkSFJVT1FqSUVQdFlnNDB3dnAyZW95RWk3WTRIRkFubzhjbExJdkNiSi1VRGRha3lLQlhtWXYzdE9ydFhuOElwM3hrc2ZlVXVwY3YtdTg3M2RwYTNYbEhibEZhYmhMS2NRM25qVWRDeVZUeFZHOXgzdw?oc=5) - Google News source discovery | MoneyDJ Tue, 01 Sep 2026 09:11:00 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Semiconductor Stocks Slide as Global Bond Selloff Lifts Yields: Intel Drops 3%, NVIDIA and AMD Slip - 24/7 Wall St.；Semiconductor stocks fall as global bond yields hit 1-year highs, pressuring AI growth valuations. - Pluang；SEMICON半導體展友達秀玻璃核心基板技術| 產經 - cna.com.tw

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 88.97 | 114.68 | -22.42% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +8.67% | +8.95% | 217.44 | 217.55 | -0.05% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | N/A | N/A | 459.61 | 516.10 | -10.95% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +1.24% | +1.67% | 2,440.00 | 2,440.00 | 0.00% | 不適用 | 86.28 | 28.28 | 467.58B TWD / 44.69% | 2026-08-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +11.81% | +6.00% | 132.50 | 164.50 | -19.45% | 不適用 | 6.68 | 19.92 | 23.84B TWD / 18.98% | 2026-08-01 |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 933.44 | 971.00 | -3.87% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | +3.50% | +3.79% | 1,536.87 | 2,335.00 | -34.18% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -2.14% | -11.44% | 369.68 | 446.77 | -17.25% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：fall, growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：fall, growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：fall, growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Semiconductor Stocks Slide as Global Bond Selloff Lifts Yields: Intel Drops 3%, NVIDIA and AMD Slip - 24/7 Wall St.](https://news.google.com/rss/articles/CBMihgJBVV95cUxNTEUtZVdRb2w2ZGY3SXJBZmpaM3VmMzVxbk9CNV9OX3B4RmFpNzlGWWN4eXBjU1JsRHd1OGplT2dGVlg5VVdUc0x0OThJOW12ZS16TFhQV2s4UXVRX2hRcjNrdlB3RlR0ZnNPQ1F6bTVDUW1BeHRYSnJ0bHQ5RFY3SEtkam1FdE9SNFVSMmhIb0tJMk1yWTdhRnM2N05BX1VZZ3NnYWx2MHZyLVdwZFZnRzhpa1dJcmZ3LXFxTXBYT2U2bEl0aGF4VFczZmpxSlAwc2x3RVJpcTh3cnJTVWpUblRPa25pWjAya0lnQVB6TDM4Wm85cjhFZFlXOEZ6Q2ZWUVZFTFZR?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 01 Sep 2026 13:15:00 GMT
- [Semiconductor stocks fall as global bond yields hit 1-year highs, pressuring AI growth valuations. - Pluang](https://news.google.com/rss/articles/CBMirwFBVV95cUxQVHo1aHZwaDliYkhsZGNpbzlwRUh0dHUwV1hNUFd5VndsdlI1MW1oZlVPTTIzZ1hlTVpXYkZaSGRzLUcwZzRoSFNEbjZVdThGWTRsc2hxNmZJOXhsMWkzVDlJdUsyRUpzVFNJbzczYTg1X2tRUHBTNU5ZZjY3RUk4V0QxcC1ZZXVxcWk4OURwWVVQRTVGTWgweFpEbmhrSi1jcl9ORTBtem9CYm9WalVr?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 01 Sep 2026 13:38:55 GMT
- [SEMICON半導體展友達秀玻璃核心基板技術| 產經 - cna.com.tw](https://news.google.com/rss/articles/CBMiXkFVX3lxTFA5YllYRkVVTnUyNTNCNFZaQjYwVnlGTE8zWlZOQm9OdzgwQ0t5eDVNVlpUeGVCMFRMeTZKYXlrdkVTMnJ3WlBNbkdnWWhzVXpBcHVnc0JKMUtRV0IwWmc?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 31 Aug 2026 14:04:00 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：整理包／台股5萬點靠他們？ 黃仁勳概念股助漲東風 完整台廠供應鏈名單、潛在受惠股一次看 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +23.07% | +40.06% | 325.13 | 325.13 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | +1.59% | +5.35% | 256.00 | 289.00 | -11.42% | 不適用 | 15.21 | 16.88 | 946.51B TWD / 54.19% | 2026-08-01 |

關聯理由（前 3）：
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [整理包／台股5萬點靠他們？ 黃仁勳概念股助漲東風 完整台廠供應鏈名單、潛在受惠股一次看 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBQUlViSHpPeDVlY29yaHFNNE5NcVlUQnE3ZThTcXRGNHgxYTVPOVVTRDlaTDV6Zml5WEwxVHNSeGFDcnVHUHhRSW15SzNpU0dYVDU3dThWNEVCbkZI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 31 Aug 2026 09:00:00 GMT

## 先進封裝與 CoPoS

摘要：先進封裝與 CoPoS 相關新聞集中在：經部打造半導體先進封裝材料設備聚落白埔園區擬第3季招商| 產經 - cna.com.tw；德律跨足先進封裝，搶半導體檢測商機- 新聞 - MoneyDJ

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +1.24% | +1.67% | 2,440.00 | 2,440.00 | 0.00% | 不適用 | 86.28 | 28.28 | 467.58B TWD / 44.69% | 2026-08-01 |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | +0.83% | +3.21% | 610.00 | 680.00 | -10.29% | 不適用 | 13.92 | 44.14 | 73.78B TWD / 43.15% | 2026-08-01 |

關聯理由（前 3）：
- 2330：產業/供應鏈推估：公司標籤符合「先進封裝與 CoPoS」關鍵字 advanced packaging, CoWoS, CoPoS, FOPLP；其中 0 篇新聞出現相關標籤。
- 3711：產業/供應鏈推估：公司標籤符合「先進封裝與 CoPoS」關鍵字 advanced packaging, CoPoS, FOPLP, panel-level packaging；其中 0 篇新聞出現相關標籤。

### 主要來源

- [經部打造半導體先進封裝材料設備聚落白埔園區擬第3季招商| 產經 - cna.com.tw](https://news.google.com/rss/articles/CBMiXkFVX3lxTE0za24yUEJFVVNwaE9lWl9ZMkloTmtKei1Kano4Y283aGtYVUUzOEUtdjh0N1JrUldYMm42a2JQZkZPb2xlOGhmT2FPMWJxSGFoN1R6ZF9VR2swc0VSN1E?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 01 Sep 2026 12:50:00 GMT
- [德律跨足先進封裝，搶半導體檢測商機- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQdU9JMGl5NVdLWEJYQ2hiSXYzTDMzb1R0Q0gxa0RKb1ZDTmFtZ0VFZV9VSkduR1k3cmFiSGU1dTJFb0IzUndXZm9rZE5mX3JGQXpIZnBXd29PRVRTc29PdkZfeXNqUlFiS3EyRklwXzk4QXdUcnNVZHlZWkNia3ZhS2d2cEZURmJXbUVfdXFpUjViUQ?oc=5) - Google News source discovery | MoneyDJ Tue, 01 Sep 2026 03:04:00 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》大漲820點，創近2個月收盤新高- 新聞 - MoneyDJ；台股強漲 台幣早盤放量升值3.5分 - MoneyDJ；美股指數期貨最新報價 9:37-台股 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》大漲820點，創近2個月收盤新高- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNNDFveTlWM2hxdkJwTEVJdTRNckNHLUtVSWFDdnFIc0s3Um1YNmd6YS1zNGpXRXh5YlhvV3lDSmVIcnQyaGNlbUVXRWZuQk1ENy1iX1R6UnlFVkpjcDJXZlNiZ3JrMXBMMDFiZ1RkWnRZelhZVFVONkdJLVFSZVhFb2pHS1VDYzB5RWlYM0dSREMydw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 01 Sep 2026 08:29:00 GMT
- [台股強漲 台幣早盤放量升值3.5分 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxOUHNSWFZIWUFmTmNVSzFDR3Byck95VUxLWGNNNXk2Q0tLWGxKSkFIbHpXdmN4eG44eXRzcmNFX0lMVjlqNzN1bFhUT0p6akdoOFJ1NUkzREVkLVV0WUJyUldubDctQ0dTUWdGbjFRdkhSVTlaamdxZnFVUWpUeEpBdzg3NUxzWUZIaUFxLWtiaE9ydw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 01 Sep 2026 04:56:00 GMT
- [美股指數期貨最新報價 9:37-台股 - MoneyDJ](https://news.google.com/rss/articles/CBMiigFBVV95cUxPYzBhX0hBQjdjX3IzOXNqYTY1ZElBLVBiYkljSTZPcXZpRG1MSnZ4XzVlZElBSXk4NW9Pc0xHYkJ2M2RyM1BGWV9tNFR0anV1dXQ2WmJ4LVBmM21FWEItREc2TENMcDl6dTd3cFRCOTJIWS1jaThSV3RGcUR2d3dPYmk3SEN0YkpaSlE?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 01 Sep 2026 01:48:59 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
