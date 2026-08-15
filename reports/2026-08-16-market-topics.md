# 每日股市熱門話題分析 - 2026-08-16

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜正向｜熱度 8｜市場確認 100.00｜同向 2/2
2. **新興題材：TradingKey**｜正向｜熱度 2｜市場確認 100.00｜同向 1/1
3. **AI 伺服器與資料中心**｜正向｜熱度 13｜市場確認 69.35｜同向 4/6
4. **半導體與晶片供應鏈**｜中性｜熱度 7｜市場確認 N/A｜同向 0/0
5. **新興題材：OpenAI**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.37（樣本 10）
- 5日相關係數：0.51（樣本 10）
- 同向比例：7/10

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 100.00 | 2/2 | 0 | +20.82% | +24.10% |
| 新興題材：TradingKey | 100.00 | 1/1 | 0 | +29.11% | +35.38% |
| AI 伺服器與資料中心 | 69.35 | 4/6 | 1 | +7.56% | +3.17% |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：OpenAI | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | 0.00 | 0/1 | 1 | -17.21% | -16.16% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-08-03 | 0.35 | -0.49 | +60.00% | 5 |
| 2026-08-04 | 0.05 | -0.08 | +46.15% | 13 |
| 2026-08-05 | -0.39 | 0.44 | +64.29% | 14 |
| 2026-08-06 | 0.07 | 0.33 | +50.00% | 12 |
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

## 歷史回測摘要

- 回測日期：2026-08-16
- 近5日 3日相關：-0.14
- 近5日 5日相關：0.02
- 同向比例：+44.44%
- 權重狀態：未調整

- 方向準確度：+44.44%
- 信心排序準確度：-0.14
- 診斷：方向與信心皆需修正

調整原因：近 5 日方向與信心排序皆偏弱，降低方向詞與供應鏈推估權重，並加重背離扣分。；關鍵詞×公司後續樣本有效 5 筆，未達 30 筆，不調整樣本權重

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

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Social Media Went Negative on Memory Stocks like SanDisk & Micron Last Weekend. Then They Rallied. - 24/7 Wall St.；Not Micron, Not Sandisk. This Artificial Intelligence (AI) Memory Stock Could Be the Next Nvidia. - The Motley Fool；Micron Stock Keeps Surging Toward $1,000 Mark as SanDisk Boost Ignites Memory Sector - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.48 | N/A | N/A | 971.66 | 971.66 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.48 | +29.11% | +35.38% | 1,641.11 | 2,335.00 | -29.72% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.43 | +12.53% | +12.82% | 225.16 | 225.16 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：boost。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 6 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：boost。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 2 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Social Media Went Negative on Memory Stocks like SanDisk & Micron Last Weekend. Then They Rallied. - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi1AFBVV95cUxNb0NXR3BnT2g0TjRzZnJNeW9lVjFVZFRBVXNPaTFSTmJQMURZRFdSX1BKMHBXNFBYNEtVZ0F3Vl9nN1p4VWpOZmFiRkEybFdub1V1V3MyX2VBMUJoczNOb1Y3aXAyM2pCQ2pqZU5OaEFQTmJ0VnloWjJHeUk4WXNlRjNhb2tIUGZ1ODhXZnFoMW5SRHYxZ3g2MHo0Nm95cm1lZWpzM0VWSmJpUS1Nd3cyZzVBeHA1azRheG1sQ0s3TmVjeW1vaFpVcWlRa09CWVR5dlB1Vg?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 15 Aug 2026 14:43:38 GMT
- [Not Micron, Not Sandisk. This Artificial Intelligence (AI) Memory Stock Could Be the Next Nvidia. - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxNT1lqZTE3dmJEaW1sd0hsdGs2NWMzR2tycU1JLTlYVW9XUk1SM2ZoY0lGendPdmVTanNvNWpvRnIwTkxIdTVNRzg5TzZtMzA5ZUw0a25jZ1RYY1N6MFcxMUZ0UXVvYmM5M3ZZejNaYXJ0MVFuNDNib05FQVRXTkdpR3RjdVlWeWVTdjhUTURfdTFseXNLZTBTYg?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 14 Aug 2026 12:00:00 GMT
- [Micron Stock Keeps Surging Toward $1,000 Mark as SanDisk Boost Ignites Memory Sector - TradingKey](https://news.google.com/rss/articles/CBMirAFBVV95cUxQQUMweERrRmdmWUhEMXJmNTdnNG1KQ3pGUmNXdUZyb3gyV0JFeDJKRE0yZWJZTnlsUW85QjBmay1sVUx5T0ZjWFJBM2JqNHdPbk5JQ2FXOGZIV05wU2J2LUd2cWJOTjlJMDE5QUY5dDJTdU40R2pHenp2M2RyVEdIa3B1Rm5od0RKQ095M29FVHlqNEs4SW1rMGl5ZnlmSVF4alY3OWNYbXl1a2Jz?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 14 Aug 2026 11:10:52 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Intel Stock Forecast: $20 Billion Offering, AI Growth and Foundry Risks - TradingKey；Micron Stock Keeps Surging Toward $1,000 Mark as SanDisk Boost Ignites Memory Sector - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.42 | N/A | N/A | 102.50 | 114.68 | -10.62% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 新聞直接提及 | +0.42 | N/A | N/A | 971.66 | 971.66 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.42 | +29.11% | +35.38% | 1,641.11 | 2,335.00 | -29.72% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 方向判斷命中詞：growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MU：新聞直接提及「Micron」，共 1 篇新聞命中。 方向判斷命中詞：boost。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 1 篇新聞命中。 方向判斷命中詞：boost。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。

### 主要來源

- [Intel Stock Forecast: $20 Billion Offering, AI Growth and Foundry Risks - TradingKey](https://news.google.com/rss/articles/CBMiqAFBVV95cUxOUmhMdmthODlUYVdDY0FsamxBS2N6MlVxR3MyZjIxX0Z1QWxLUnY3dFU3OEVuT1FZV3l6ZUlCdlllUVUwaHRmQ19laUFIeUhISnJ2d1VkWEZLenQzYlBlWWY4aVd0R19sbG5xWUhvVlJ3bTF6WFZZVGQzQUIyZ1FtNVN1ZnctNTZwa1ktM0tfZThaVWhpcERva19SMUFUUjZ1WGYtLVVWbHo?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 14 Aug 2026 02:05:37 GMT
- [Micron Stock Keeps Surging Toward $1,000 Mark as SanDisk Boost Ignites Memory Sector - TradingKey](https://news.google.com/rss/articles/CBMirAFBVV95cUxQQUMweERrRmdmWUhEMXJmNTdnNG1KQ3pGUmNXdUZyb3gyV0JFeDJKRE0yZWJZTnlsUW85QjBmay1sVUx5T0ZjWFJBM2JqNHdPbk5JQ2FXOGZIV05wU2J2LUd2cWJOTjlJMDE5QUY5dDJTdU40R2pHenp2M2RyVEdIa3B1Rm5od0RKQ095M29FVHlqNEs4SW1rMGl5ZnlmSVF4alY3OWNYbXl1a2Jz?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 14 Aug 2026 11:10:52 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：股海自由行／獲利強勁 AI 鏈 長線主打星 | 證券達人 | 證券 - 經濟日報；Is Intel’s US$20 Billion AI-Focused Equity Raise Reshaping The Investment Case For Intel (INTC)? - simplywall.st；綠能落地受限，AI 能否突破併網與審批瓶頸？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.54 | N/A | N/A | 102.50 | 114.68 | -10.62% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.06 | +12.53% | +12.82% | 225.16 | 225.16 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.06 | N/A | N/A | 514.39 | 516.10 | -0.33% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.04 | 0.00% | +1.05% | 2,395.00 | 2,425.00 | -1.24% | 未明確 | 86.28 | N/A | 467.58B TWD / 44.69% | 2026-08-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | +26.14% | -2.23% | 495.40 | 506.69 | -2.23% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.04 | +4.03% | -5.85% | 392.99 | 446.77 | -12.04% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.02 | -2.07% | +5.30% | 616.00 | 680.00 | -9.41% | 背離 | 13.92 | N/A | 73.78B TWD / 43.15% | 2026-08-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.04 | +4.73% | +7.95% | 4,210.00 | 4,310.00 | -2.32% | 同向 | 60.69 | N/A | 48.47B TWD / 12.16% | 2026-08-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：raise, 強勁。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：raise, 強勁。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：raise, 強勁。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [股海自由行／獲利強勁 AI 鏈 長線主打星 | 證券達人 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE11dmw0RDAtQUo4Q3M0LVFZWkpFS3NtX0tuRmZhYjluRUVzaUstV0lPS1U2T2dlemFuRF9GZ3UycUFYMHVxOVVHZ1dIZURkWGNvWlA1MURPUmJZQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 15 Aug 2026 18:01:26 GMT
- [Is Intel’s US$20 Billion AI-Focused Equity Raise Reshaping The Investment Case For Intel (INTC)? - simplywall.st](https://news.google.com/rss/articles/CBMiygFBVV95cUxQS0I4U3kwOF9nek4zS1JsSGtleE05UmlUdklRMG5WX0h2Y2xuUE8yRVZZX0dpUXd2Z0l6dkpEUFgzX0l3TWU4UEVuNDZuRktRcVRMOFAwMHNXdXROeVozNDFvaDlCZmNVQWN6c0Nld3Q0ckR1NXNmd1A3SGlwbUdTZkVibnZROFp6TW1xakJwNklQMFJCY1Nod2lTbGFVdVdYSzNQMWFOWHV4VHkwTS1NdWl5ME1RN1NkV19GQ3dmMHVwaF9CNFpiNjBn0gHPAUFVX3lxTE1pS2Utc0tTbTRwSnoyajFrTHp4dXdoMzFfVWVZNXdxVHRNOFNLclQ3WHZaR1MtZ3F1cVpwUktxSHg5MG5GWmxfd2xrT3Y1WDdrQXRYd0tFTjB3U2Y3Mk1GcGVaVjZTMERqRTVSLVhrSDBxdmUzdkhWb0tlTEJIcjBPOThLWDdFYlg5N3lMSld4OTdDZ0ZEUXdqamlGWTZtWEtVQm5VTTEtV3o0aVVoTmVtanRhRks2eXFfLWstb3dLYkp0RlYzeFBPQmljQ09ZNA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 15 Aug 2026 18:30:35 GMT
- [綠能落地受限，AI 能否突破併網與審批瓶頸？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMid0FVX3lxTE5hRElENFZ4b0NGMHZmV0VMTi0ydWtEUGRLTHVNWGRoVDE4Y21lelpyZ2xObFdtYXVmVFZkcmhWQ0lxTDh0ZEpBYmtCeWJOME83d0hkSUJSMDFZbWJSY0IwX2JKVG1ELVhHRUkwZHVtSlFiSDV4b3o0?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 15 Aug 2026 17:27:38 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：美來台修讀STEM學位達百人續推半導體人才合作| 生活 - cna.com.tw；廣運攻AI、半導體布局新事業- 日報 - 工商時報；電信、半導體跨界搶進資服- 日報 - 工商時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | 0.00 | 0.00% | +1.05% | 2,395.00 | 2,425.00 | -1.24% | 不適用 | 86.28 | N/A | 467.58B TWD / 44.69% | 2026-08-01 |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 102.50 | 114.68 | -10.62% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | -1.63% | +4.31% | 121.00 | 164.50 | -26.44% | 不適用 | 6.68 | N/A | 23.84B TWD / 18.98% | 2026-08-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +12.53% | +12.82% | 225.16 | 225.16 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 514.39 | 516.10 | -0.33% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 971.66 | 971.66 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | +29.11% | +35.38% | 1,641.11 | 2,335.00 | -29.72% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | +4.03% | -5.85% | 392.99 | 446.77 | -12.04% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip, foundry。
- INTC：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 CPU, server CPU, x86, foundry；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 0 篇新聞出現相關標籤。

### 主要來源

- [美來台修讀STEM學位達百人續推半導體人才合作| 生活 - cna.com.tw](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBOT3NPWlhyU2dxZzhfbHE0d2tkRDh3YVdCakM4UkZ5blNzUWJfVzlycWlJS2pxVEs0d2FFM3k3aGMtVzJjaHFvazFxd3RFOHhQeklaNVhDQ1VYcUpURVNz?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 15 Aug 2026 05:31:00 GMT
- [廣運攻AI、半導體布局新事業- 日報 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5YaFBWbVdDMDh0bFpBOWZqeFpCaVhHNWIxbExzVEQtcV9sYW8wMDFlangwTDYyWkpDTUQ2NHBhaF9SaV9tU1c5MmZSZm93bzVYZG5LdkZXZzZvWFYxOVNz?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 15 Aug 2026 19:00:00 GMT
- [電信、半導體跨界搶進資服- 日報 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE53anVRdld2RW52dmNxRHBuVjRpQjNHcmFPUXFaVlA4eHZmVVJTalEtZlkzOHlERF8tcUVTUTNTNFdsdjZpQjU5b0JJZFFQeHNvWmJwZ3ZzczFUZXdrelAw?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 15 Aug 2026 19:00:00 GMT

## 新興題材：OpenAI

摘要：新興題材：OpenAI 相關新聞集中在：OpenAI talent exodus raises 'huge red flag' ahead of IPO - CNBC；OpenAI CFO Friar tells investors that enterprise business now bigger than consumer by revenue - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 新聞直接提及 | 0.00 | +26.14% | -2.23% | 495.40 | 506.69 | -2.23% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：新聞直接提及「OpenAI」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [OpenAI talent exodus raises 'huge red flag' ahead of IPO - CNBC](https://news.google.com/rss/articles/CBMiaEFVX3lxTE44OUJZSWt3dkU4Vmh6T1lEbkFhMi1SNnc0aEF2d1RNNzZ2Q0ViLWM2UGFYS0VSLVUzYW1PNjRPYm04ajJlV2JSdXlGS1BnYU1wcDhyT2pxMzNvNHRWQkoyZGY5bmdaZ2ZI0gFuQVVfeXFMT0hVcEpCdG9PRElhcFVtc211cnNmX0twcF9DeVU2aXNRYXdZaExmNFlDdGluaWtmQ0pjXzY0bVNKWVNRMHY1a0FkSlRTelZaLXBkaW9FNm01TFU0MGY0dVVIQXY2M2ZfekYxd3FiNnc?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 14 Aug 2026 15:45:15 GMT
- [OpenAI CFO Friar tells investors that enterprise business now bigger than consumer by revenue - CNBC](https://news.google.com/rss/articles/CBMiqgFBVV95cUxQRHBnZWdHT2ZNTFBza3ZncERqUnFNTFJPcGUyY3ljd3hYUUFTMEF5ZHpWVGxrY0l2a0Ftd3ZWcTc3bjA2aHBVSUcyZ0xwVTFRUEJRdEhSSV95cVd3S01NcDBiQ19RbVFkbUlUSWNqVE4zUkM4bVJCMVNRb2xRdWVyT2p3RTFkWnluVnllUk4yYm84YXQ2T09NSzVEUnY2c2Vub0VxZ3VxSXl4d9IBrwFBVV95cUxPOGVvSTlpbkI0eWNxcVZEbk4zbFdJdUF1ZEJ0QmxKelEzbG1NQW82TFNIeUEyXzlVdm1hb1pUZkh4MnU1bFZaMTdzdFBpZmk3TmM3VFh6SXFBV0pCUHRURFBkLVhtZEN0X2tSVVVkR0E3WEFyRzNablVSTjRucC1DZE1fRUNMLXVRZUVUS3F5cmptNkF6WkRxS1JQVl9TaUtQX1owTnVnY09SVkJIZHpN?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 14 Aug 2026 19:00:31 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | -0.21 | +17.21% | +16.16% | 3,235.00 | 3,235.00 | 0.00% | 背離 | 75.13 | N/A | 18.59B TWD / 57.39% | 2026-08-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 1 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：跌停。

### 主要來源

- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 14 Aug 2026 22:00:58 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：凱基-中山 對 志信(2611)個股 單一券商歷史明細 - justdata.moneydj.com；《台股盤後》收跌210點、5日線有守；周K連二紅- 新聞 - MoneyDJ理財網；查詢民國 (yy/mm/dd) 以前的相關新聞輸入日期 - 6480.moneydj.com

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [凱基-中山 對 志信(2611)個股 單一券商歷史明細 - justdata.moneydj.com](https://news.google.com/rss/articles/CBMihgFBVV95cUxPdTdCY05xR09KcV9qbnVNUlpwbVRxbEczdGlnV1RaTVRyaEVNRXhxUndOeG41d21HTUoxbl94eTBmSGFKdUxJQ0hYYVlCbzBPOHNZZXl0YWE0NkprQk5ncXRiVkJFZEhyVThWWGdVV2tYWkEtdEgxakdiQXZRYUlGZHJtZVgyZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 14 Aug 2026 21:10:45 GMT
- [《台股盤後》收跌210點、5日線有守；周K連二紅- 新聞 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikgFBVV95cUxNLWVtUXdHV3JlczBLRWtXYmZCTjZEQ3JHaDN3YnFONEJIRFRmbFlBVEVHM2ZwVUQxWDNJX3pWWW5Ja2Jrc0twZENfQUxjMV8zdUk0NXlSa2RIenlQUXFjNmFubjlyUHlsa1ZrZHplR3Q1LXFrVjBNV3ZxOEF3cDBIYjhJckFfSjdVU3ZBSDlELUVKZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 14 Aug 2026 07:45:00 GMT
- [查詢民國 (yy/mm/dd) 以前的相關新聞輸入日期 - 6480.moneydj.com](https://news.google.com/rss/articles/CBMiZkFVX3lxTE5pbTdIZ3JfVy1reVJMbmpqa21MNE9MN05pejNiVXZiNS04eEI4dkpzY2ZoUk9IWlNJZ0RCZzltc1h4SmR0NG5idTFxbnlBdUNBSDFSWW53OG9Gak8yYW8yMk5HLU9KUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 15 Aug 2026 08:12:37 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：富邦-南員林 對 久裕(4173)個股 單一券商歷史明細 - MoneyDJ；宏遠-台中 對 華邦電(2344)個股 單一券商歷史明細 - MoneyDJ；永豐金-中正 對 尖點(8021)個股 單一券商歷史明細 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [富邦-南員林 對 久裕(4173)個股 單一券商歷史明細 - MoneyDJ](https://news.google.com/rss/articles/CBMikwFBVV95cUxPOERjSTNrdU1nUG8zbTJPdW5UbnJKYzBKTVVHTG9VYmVZWE9pUjBJMDh2bEM2QVgxMmlfRjh5Z2l6WjduaVEzeEtqbWZkWnZXSXNZNmZmVDdSMjQ0R09saEEwRDlKUzdLam5TNzlvUnJObTFNclhtOWFPNnpSZjlLTmRwZmtXTWhpd0VtT1dNbmtKWTQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 15 Aug 2026 09:13:44 GMT
- [宏遠-台中 對 華邦電(2344)個股 單一券商歷史明細 - MoneyDJ](https://news.google.com/rss/articles/CBMikwFBVV95cUxOb2xac2FoRkZvd3VsMDZuSUNNUE1Za3p0YjE1TkszMlY3Z3JWYlE5MU1PMHhPWnNQMlozZnNWUUZfX0tRci1kZlRLVUJ0RXdwbkZYM0tIYnF0akM5aTZMLUhwVS04b1VnOTJZeTVmSDVvQ0liR1FRbE14Zkp2aWttVV95dElKcTg4bTM4cG5na05YQlU?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 14 Aug 2026 21:30:35 GMT
- [永豐金-中正 對 尖點(8021)個股 單一券商歷史明細 - MoneyDJ](https://news.google.com/rss/articles/CBMikwFBVV95cUxOMjNCWlZaRnFpQTBRMi1OZlZ3cTg3OTdoRTVhYmVmUWxjR2dCTURGTkRNeDJCQlJPdmg4dWpzZnRQdXd6UkVXVGFXY2ZMT1pjeFVHYjNmUWNoZkMzLXVkRmhkN3dVX2JZeU51TnNkclNBZU1oa2hteFNuaVlYdjJSTHJ1UVQ0LUpFLXc5YkNORXVzcnc?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 14 Aug 2026 18:46:26 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
- TWSE PER/PBR 抓取失敗：Expecting value: line 1 column 1 (char 0)
