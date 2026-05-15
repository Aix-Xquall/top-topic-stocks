# 每日股市熱門話題分析 - 2026-05-16

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜正向｜熱度 9｜市場確認 65.00｜同向 1/2
2. **利率與成長股估值**｜負向｜熱度 5｜市場確認 N/A｜同向 0/0
3. **半導體與晶片供應鏈**｜中性｜熱度 9｜市場確認 N/A｜同向 0/0
4. **散熱與液冷供應鏈**｜正向｜熱度 4｜市場確認 65.00｜同向 1/2
5. **AI 伺服器與資料中心**｜正向｜熱度 12｜市場確認 45.16｜同向 2/6

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.12（樣本 12）
- 5日相關係數：-0.69（樣本 12）
- 同向比例：4/12

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 65.00 | 1/2 | 1 | +13.07% | +4.00% |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | 65.00 | 1/2 | 1 | +13.31% | +9.15% |
| AI 伺服器與資料中心 | 45.16 | 2/6 | 3 | +7.28% | -1.11% |
| 新興題材：針對散熱 | 0.00 | 0/1 | 1 | -2.58% | +0.41% |
| 新興題材：奇鋐看好今年營收 | 0.00 | 0/1 | 1 | -2.58% | +0.41% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價呈負相關；應檢查正負向詞庫，並降低新聞直接提及但股價背離的權重。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

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
| 2026-05-15 | -0.17 | -0.08 | +58.33% | 12 |
| 2026-05-16 | -0.12 | -0.69 | +33.33% | 12 |

## 歷史回測摘要

- 回測日期：2026-05-16
- 近5日 3日相關：0.04
- 近5日 5日相關：-0.11
- 同向比例：+42.86%
- 權重狀態：未調整

- 方向準確度：+42.86%
- 信心排序準確度：0.04
- 診斷：低相關

調整原因：近 5 日有效樣本 14 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Forward PE Explained: How to Value AI Stocks Like NVDA, AMD, INTC & MU - Bitget；Micron (MU) & Sandisk (SNDK) Stocks May Still Be Cheap as ‘High-Bandwidth Memory Can Be Priced Ridiculously High’ - TipRanks；Why I'd Rather Own Micron Stock Than Sandisk - The Motley Fool

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.76 | N/A | N/A | 724.66 | 776.01 | -6.62% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.38 | -3.06% | -9.90% | 1,407.61 | 1,562.34 | -9.90% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.67 | +29.20% | +17.89% | 225.32 | 235.74 | -4.42% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.56 | N/A | N/A | 424.10 | 449.70 | -5.69% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.56 | N/A | N/A | 108.77 | 115.93 | -6.18% | N/A | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK、SanDisk」，共 5 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVDA、NVIDIA」，共 2 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Forward PE Explained: How to Value AI Stocks Like NVDA, AMD, INTC & MU - Bitget](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBINHZlcG9JcmdnVVlsTklBZlROVGItVmtRX2VDX1FYSXYwT0RYME5zNWtGbDZvMzgzWGhkQmlXZ2hrUXFqWXh4dTJQOEx4TDRHY3NCZXg3MGxnT0U4?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 15 May 2026 10:11:13 GMT
- [Micron (MU) & Sandisk (SNDK) Stocks May Still Be Cheap as ‘High-Bandwidth Memory Can Be Priced Ridiculously High’ - TipRanks](https://news.google.com/rss/articles/CBMi0AFBVV95cUxQTHFkLVVTQVJjQ3ZhMzV3Z1lHbXVrT2VsYlhwYUhVbFUwaHF4eXczbklHc2MtXzNnOEFlWFVvTEtHTHk2Y3ZFMngzbmk1RFlkY2lJU3duMDRHaWxPSW1zVlJhNFlMYmM0MFpHdE9vWmRHV0MxZ1kwR082QUxzdTFDWEtOeXJ2dzZGbWZpanZWQ3FyMXFnQmhPN19MOHZZMXNNNllFMlF5V0tZR2xsUEJQRE5IRWRBOFhRQkZGYVZ1VjJvaTdxUVgyb0EwMHlicXVN?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 15 May 2026 11:30:22 GMT
- [Why I'd Rather Own Micron Stock Than Sandisk - The Motley Fool](https://news.google.com/rss/articles/CBMihwFBVV95cUxNel8xVUxEczE0OW94SGplUk5vVWdLcWQ5ckVscnFGSDRWWTlZNUpKS1IwMmJTUjd0bTlZbEx5LXp6LTh5WE1WNl9GVUtoYkV3QlpzODBMTVNyRk0tRFA0bDh1NllkaWJrdElVcFc5STI4cVFPNV95R1BnbTlzeUZOVzByZmZTbDg?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 14 May 2026 05:30:00 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：Chip Stocks Fall As Inflation Fears Trigger Profit-Taking - Benzinga；AI 技術能否在五年後有效緩解通膨壓力？ - TechNews 科技新報；Global shares drop, bond yields climb on inflation worries - Reuters

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | -14.25% | -8.35% | 421.92 | 506.69 | -16.73% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Chip Stocks Fall As Inflation Fears Trigger Profit-Taking - Benzinga](https://news.google.com/rss/articles/CBMirwFBVV95cUxOMTY0UnlCOFgteFlXMGlWdHpDLW5PbkhLQ1J0M0o2Wi01ZGozS2RRdWd5dHRIUmhCVHJwYVdaUjQxSUwzd0ZNdENubFp5c2F5QXpoTERDUk9xMi12VDRjcGJvWVRsdE9yMGZVZ180c3R2ZHE1V25YSE1sUnEzWlFrM1MxWUlQaVRrNk01YndnSVFjcEl5OXgxbndGYzRoLWZZbXptZHVhR3oxbVlIQVl3?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 15 May 2026 10:59:23 GMT
- [AI 技術能否在五年後有效緩解通膨壓力？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiZEFVX3lxTE14QnBvTWlfQms5LXduNGhLSWZWRHRDQXF5QVZ5TzZtaVJaUkVVS3dLZ0ViYmxDQVQ2V1RSR1VUSG5laElnSlh1Qm0tR0pHOWVCZHdxeDAxQ1J1VW5uazM4T0QydWY?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 15 May 2026 11:32:26 GMT
- [Global shares drop, bond yields climb on inflation worries - Reuters](https://news.google.com/rss/articles/CBMigwFBVV95cUxNdXdkc1k2VjFGcUx2RHhvb1BKVW9HNmp3ZnNyTmxQTElPSVY0OERvUThQNVRab0luYVdLbTFkREU1MkZfZVNld3BMNkdwV2RPcWgwTFVrQ0ZCZFRhY2pweVhGUmpOdlotOU96OUhndzdLQWpPdjNNVWdma2NZdzJNYVkwRQ?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 15 May 2026 02:12:00 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel Climbs 15% on Apple Chip Deal as Trader Warns on Upcoming Cisco Earnings - 24/7 Wall St.；Forget Intel. Its Own Executives Are Cashing Out and This Is the Chip Stock You Should Own Instead - AOL.com；Intel (INTC) Stock Falls as UBS Warns of AI Chip Bubble - MEXC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 108.77 | 115.93 | -6.18% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | 0.00 | +0.44% | -1.09% | 2,265.00 | 2,270.00 | -0.22% | 不適用 | 74.39 | 30.45 | 410.73B TWD / 17.50% | 2026-05-01 |
| AAPL 蘋果 | 新聞直接提及 | 0.00 | +7.67% | +49.48% | 300.23 | 300.23 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +5.26% | +20.48% | 110.00 | 110.00 | 0.00% | 不適用 | 4.00 | 27.64 | 22.66B TWD / 10.80% | 2026-05-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +29.20% | +17.89% | 225.32 | 235.74 | -4.42% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 424.10 | 449.70 | -5.69% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 724.66 | 776.01 | -6.62% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -3.06% | -9.90% | 1,407.61 | 1,562.34 | -9.90% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel、INTC」，共 4 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：falls, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「Taiwan Semiconductor、台積電」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip, foundry。 方向判斷命中詞：falls, rally。
- AAPL：新聞直接提及「Apple」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Climbs 15% on Apple Chip Deal as Trader Warns on Upcoming Cisco Earnings - 24/7 Wall St.](https://news.google.com/rss/articles/CBMivgFBVV95cUxOaTZPTHdDbWVDb2FLblZ1aWZIWV92eWROcERuUWRlZ2JrWTZIQWE0TXhaWHNPNFZzMEpmNk91NmNxVFczeF9JSllObUlpX2lLTkdrczJzN0ZMaWl5bmExbVY1OC1PMkF2WEhtcEZCc0dwSVpLNU1ZcUtVSW9HTGJubGdaY3QyNGV3UTRUTFZhMzRXVWQ2SWNYY20yRWhOUlpHbHhYRzhMUE1lQV9WTmNGNXo0djl2S19HOGxqSlZn?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 15 May 2026 16:41:10 GMT
- [Forget Intel. Its Own Executives Are Cashing Out and This Is the Chip Stock You Should Own Instead - AOL.com](https://news.google.com/rss/articles/CBMihgFBVV95cUxNaWdkSUVySmJGWWtvZXk5V0FLNW40OUNZRXNFRTFpSVhFd1ZILWhpZEpOc1dSejA3Q1dMR1NvX2otQlpRSzJJQmNyVVJhRUs0QUtLVU8yTmlJV2xuT2FXaDVWNVZzYjc4UnFXV01WNkpleURwd1ByWW9aTWEyZm9HSS1ZS2E2dw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 15 May 2026 13:06:34 GMT
- [Intel (INTC) Stock Falls as UBS Warns of AI Chip Bubble - MEXC](https://news.google.com/rss/articles/CBMiSEFVX3lxTE5TUWp1MVpiNkRCYXZibV83aHZWU1BTR19TOUtQZkdBSTdqUlFXajdESHQtcnVCSmttNFBqU2J4dFZESTZmUGF4Xw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 15 May 2026 16:06:15 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：奇鋐看好今年營收及獲利逐季成長 針對散熱模組修改設計釋疑 - news.cnyes.com；傳NVIDIA Rubin取消鍍金設計 奇鋐：對營運無影響 - DIGITIMES；單季就賺破2股本！「散熱大廠」Q1獲利強漲146.3%創高 輝達Rubin展開出貨業績續揚 - Yahoo股市

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.38 | -2.58% | +0.41% | 2,455.00 | 2,835.00 | -13.40% | 背離 | 61.06 | 40.34 | 15.63B TWD / 71.62% | 2026-05-01 |
| NVDA 輝達 | 新聞直接提及 | +0.56 | +29.20% | +17.89% | 225.32 | 235.74 | -4.42% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐、散熱、3017」，共 4 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：成長, 創高。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：創高。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [奇鋐看好今年營收及獲利逐季成長 針對散熱模組修改設計釋疑 - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTE1rT2dIQUlJZEZtT0s3amhLcGNhS1phV2h1akJxMkVsNFhxNHF5c1p1dEVJMVE0aDFhT0JoTzllUkU2R3NVaktIejdiSkI0NEU?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 14 May 2026 11:19:40 GMT
- [傳NVIDIA Rubin取消鍍金設計 奇鋐：對營運無影響 - DIGITIMES](https://news.google.com/rss/articles/CBMijgFBVV95cUxOQUVMSFgxbWhnM285WnV4akdCQTA3YWNXQXBibG0wWndRMU43elRPUzZWYnRYdlZzOGgyOG5jVjJYSXVpN2VKWDV4bGV1ZUNhbGhPM2FZRmJXU3NRWXFRVmVlNGNtVWxtZFdSbkw1eTF2Wks0eG5kTkZPbzJvWjBzdXFQZEhwX2FJU2V2aHFR?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 14 May 2026 10:06:00 GMT
- [單季就賺破2股本！「散熱大廠」Q1獲利強漲146.3%創高 輝達Rubin展開出貨業績續揚 - Yahoo股市](https://news.google.com/rss/articles/CBMitgJBVV95cUxPOV9JNHBtLTZFb1l0QmswcF9SYUY1QjNwV2J2Q2NiZjdRZmpTa2k4R05vZnIwcVk2SUF6OGNqQVpid3I2TjNrVE84OENZX0I5NVZtWjNnVm1rMTFUa1k2Z0JXVW00aVhUUFpVNnM3ZmpEcF9tUmJKSkdqc1NBY0VKbjAtZktOcnFFNW1Lcm1PQUZBNEg5cWFKY1YtRjdBVnRhSHh3VkpNRDFMXzRZdmVGVWwtVGF6RjNDQ0VPV25fd1Q5cEtYLWItVElMVThRTTdqeUNqOEJJX0s3WUU1NWxMOV90a3F5QjZlNk1XSnN5eUV1aUdnbXVtdDFqbkRoTVprMmJUYU5Hbkxhc3c1WUhWZ2tzdlhiUEtXNmxzcVM4SjVZNE5IYldxZkh1S1N4LUQwT3pWd3Z3?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 15 May 2026 00:35:25 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel (INTC) Stock Falls as UBS Warns of AI Chip Bubble - MEXC；Intel's Explosive Rally Vs Taiwan Semiconductor's Steady Dominance: Which AI Chip Giant Wins? - Benzinga；GAI 與 Edge AI 整合對沉浸式內容創作有何影響？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.76 | N/A | N/A | 108.77 | 115.93 | -6.18% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | +0.52 | +0.44% | -1.09% | 2,265.00 | 2,270.00 | -0.22% | 未明確 | 74.39 | 30.45 | 410.73B TWD / 17.50% | 2026-05-01 |
| AAPL 蘋果 | 新聞直接提及 | -0.28 | +7.67% | +49.48% | 300.23 | 300.23 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.10 | +29.20% | +17.89% | 225.32 | 235.74 | -4.42% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.09 | N/A | N/A | 424.10 | 449.70 | -5.69% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | -14.25% | -8.35% | 421.92 | 506.69 | -16.73% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.07 | +37.38% | +28.34% | 425.19 | 439.79 | -3.32% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.04 | -1.44% | +6.01% | 547.00 | 548.00 | -0.18% | 背離 | 10.86 | 50.79 | 62.25B TWD / 19.22% | 2026-05-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC、Intel」，共 2 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：falls, 不如預期, rally, 創高。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「Taiwan Semiconductor」，共 1 篇新聞命中。 同時符合主題標籤：AI, advanced packaging, CoWoS, AI server。 方向判斷命中詞：falls, 不如預期, rally, 創高。
- AAPL：新聞直接提及「蘋果」，共 1 篇新聞命中。 方向判斷命中詞：不如預期。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel (INTC) Stock Falls as UBS Warns of AI Chip Bubble - MEXC](https://news.google.com/rss/articles/CBMiSEFVX3lxTE5TUWp1MVpiNkRCYXZibV83aHZWU1BTR19TOUtQZkdBSTdqUlFXajdESHQtcnVCSmttNFBqU2J4dFZESTZmUGF4Xw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 15 May 2026 16:06:15 GMT
- [Intel's Explosive Rally Vs Taiwan Semiconductor's Steady Dominance: Which AI Chip Giant Wins? - Benzinga](https://news.google.com/rss/articles/CBMi3wFBVV95cUxPQ19SMUFrdEtLcjF3VWJQd01rRWNmeGZyZUtQUTBhZF9wR3UwclI0VTRhaG4zVEVaU2NFLTFpc1RkaGp1SzVtMi1kWWpBNGdPQU5tdVo4clVsVldtS041QmpPLXQzdTQ2MG5lZlRjWk92akQ1X1dyNHdudkI2VHJUbTlQOVJjeGpDcjBQd3hYSUhYSnc3clRoRXMtb2ZwenNtWks1SjZ2ZmFYeWJNZXh1WHBUU0x4V0pYdEVndDZoWVdYeEhxZzR6YXh5NG1uUWpIakFBN29TaVdyZ0pwb1BV?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 15 May 2026 12:30:28 GMT
- [GAI 與 Edge AI 整合對沉浸式內容創作有何影響？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiXkFVX3lxTE9QWXNrT2FybXdfTEg2NloyQlJFSTlQbngzSnRwbFp2aDI1MlhwanVqYm9aTzFrYW1qUlV0MVVxNGhtY2VhUW43aGwtTnUxVjFBcVNwMzJxTklfTGFfYkE?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 15 May 2026 18:00:12 GMT

## 新興題材：針對散熱

摘要：新興題材：針對散熱 相關新聞集中在：奇鋐看好今年營收及獲利逐季成長 針對散熱模組修改設計釋疑 - news.cnyes.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.28 | -2.58% | +0.41% | 2,455.00 | 2,835.00 | -13.40% | 背離 | 61.06 | 40.34 | 15.63B TWD / 71.62% | 2026-05-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐」，共 1 篇新聞命中。 方向判斷命中詞：成長。

### 主要來源

- [奇鋐看好今年營收及獲利逐季成長 針對散熱模組修改設計釋疑 - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTE1rT2dIQUlJZEZtT0s3amhLcGNhS1phV2h1akJxMkVsNFhxNHF5c1p1dEVJMVE0aDFhT0JoTzllUkU2R3NVaktIejdiSkI0NEU?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 14 May 2026 11:19:40 GMT

## 新興題材：奇鋐看好今年營收

摘要：新興題材：奇鋐看好今年營收 相關新聞集中在：奇鋐看好今年營收及獲利逐季成長 針對散熱模組修改設計釋疑 - news.cnyes.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.28 | -2.58% | +0.41% | 2,455.00 | 2,835.00 | -13.40% | 背離 | 61.06 | 40.34 | 15.63B TWD / 71.62% | 2026-05-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐」，共 1 篇新聞命中。 方向判斷命中詞：成長。

### 主要來源

- [奇鋐看好今年營收及獲利逐季成長 針對散熱模組修改設計釋疑 - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTE1rT2dIQUlJZEZtT0s3amhLcGNhS1phV2h1akJxMkVsNFhxNHF5c1p1dEVJMVE0aDFhT0JoTzllUkU2R3NVaktIejdiSkI0NEU?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 14 May 2026 11:19:40 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：《台股盤後》震盪逾千點、收跌579點；週K翻黑- 新聞 - MoneyDJ理財網；台股焦點：益登(3048.TW) - MoneyDJ理財網；台股焦點：瑞耘(6532.TW) - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》震盪逾千點、收跌579點；週K翻黑- 新聞 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikgFBVV95cUxOUlhpTEo3M1B1LVBxaTVxZkJfeHNZd1UyQlF6enZHb3RwTjdrZEV1eHJNc1k2SWlhbm1oSmhheVhJUjc5QmJDbUVHdUo3ZV9wQkxsVVRoRnVDS1FiSkExVGZLeW5hUUdZUUVSbXQ4eVFCQy1mT2tmVmpKaE1oOTR0TFlmZEtfVFFKdjdMS0FiM0NxZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 15 May 2026 08:25:00 GMT
- [台股焦點：益登(3048.TW) - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikgFBVV95cUxOUTlqdzl3UE5MbGlXOG9lckZTeW5fajRORWZtRWlzaTcyZ1QwQUFaVTlFSXB5T1cwamViTXJBRHQybTd4Q3l2N3FlNW9BbkliWXZyWUxSOG5hYUNFcXU4S2xUcm1BTVBRb05oNVhMbHEtdzlJTWg1QS1pQUdZV1pVZk1FNlRfVjJaOURaTkxZRHBnZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 15 May 2026 01:10:00 GMT
- [台股焦點：瑞耘(6532.TW) - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikgFBVV95cUxOS0xKcFpweExhSGxpcHdUQmFnbV9EeTRhbHlFNFhod1FEa2NWNjNGdURsWlhPTG5YeDJ2eUJMNnpRNkxfcUFMWGtpLUJOY0ZET1Uzb2cyZDVfY2hZUGgzZTVBVjVRdFNXVU1vLWRVSTN6UElTTWp4TE1LSVZIbkJTOFpHOVBjdmNQZUV4MkhTVThUZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 15 May 2026 01:23:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
