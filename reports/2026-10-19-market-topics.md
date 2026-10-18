# 每日股市熱門話題分析 - 2026-10-19

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜負向｜熱度 6｜市場確認 90.75｜同向 4/4
2. **利率與成長股估值**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
3. **半導體與晶片供應鏈**｜中性｜熱度 4｜市場確認 N/A｜同向 0/0
4. **新興題材：MarketBeat**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
5. **AI 伺服器與資料中心**｜正向｜熱度 8｜市場確認 4.69｜同向 2/8

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.44（樣本 12）
- 5日相關係數：0.36（樣本 9）
- 同向比例：6/12

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 90.75 | 4/4 | 0 | +6.92% | +5.31% |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MarketBeat | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 4.69 | 2/8 | 6 | -4.27% | -3.79% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：B072 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-10-06 | -0.72 | -0.75 | +37.50% | 8 |
| 2026-10-07 | 0.48 | 0.61 | +73.33% | 15 |
| 2026-10-08 | 0.13 | 0.40 | +58.33% | 12 |
| 2026-10-09 | -0.03 | 0.37 | +38.89% | 18 |
| 2026-10-10 | -0.28 | -0.96 | +57.14% | 7 |
| 2026-10-11 | 0.66 | -0.74 | +40.00% | 5 |
| 2026-10-12 | -0.08 | -0.07 | +41.67% | 12 |
| 2026-10-13 | -0.05 | -0.03 | +46.67% | 15 |
| 2026-10-14 | 0.08 | -0.29 | +57.14% | 14 |
| 2026-10-15 | -0.08 | 0.08 | +33.33% | 12 |
| 2026-10-16 | -0.13 | -0.25 | +64.00% | 25 |
| 2026-10-17 | -0.10 | 0.49 | +26.32% | 19 |
| 2026-10-18 | -0.12 | 0.33 | +21.74% | 23 |
| 2026-10-19 | 0.44 | 0.36 | +50.00% | 12 |

## 歷史回測摘要

- 回測日期：2026-10-19
- 近5日 3日相關：-0.14
- 近5日 5日相關：0.14
- 同向比例：+52.94%
- 權重狀態：已調整

- 方向準確度：+52.94%
- 信心排序準確度：-0.14
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

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：記憶體、證券股 高息可期 - 經濟日報；Micron vs. SanDisk: As Storage Sector Drops Broadly, Which Is the Better Long-Term Investment? - TradingKey；Can Micron and Sandisk Break the Memory Cycle? - NAI500

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | -0.57 | -9.49% | N/A | 878.84 | 971.00 | -9.49% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.57 | -12.35% | -17.86% | 1,299.30 | 2,335.00 | -44.36% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | -0.43 | -3.01% | +7.02% | 214.13 | 228.38 | -6.24% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | -0.42 | -2.81% | -5.10% | 2,420.00 | 2,480.00 | -2.42% | 同向 | 86.28 | 28.05 | 511.86B TWD / 54.65% | 2026-10-01 |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、memory」，共 3 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 2 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [記憶體、證券股 高息可期 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE81U0cwY3JsUmJRbU1CV1FmMF9aRVJqSXluNXJDM2xLZUlWeEtDaUM4R0VUNjlHRHAtRW5oelgtWXZPUS1aTmhmbWU3WURmQ3BmOXprNk95aVYwZ9IBX0FVX3lxTFBYVGljcy1QeEtWWlk2WGF2dTNsRFZpelFXUWlKYm92aV9yb0lFeFphemdTcGFIRHRFZWxFUVpNRUhQX3o5SEw2ckx5eWlIWlJmazlkWG0yeGpBVHNkYnNz?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 18 Oct 2026 17:03:29 GMT
- [Micron vs. SanDisk: As Storage Sector Drops Broadly, Which Is the Better Long-Term Investment? - TradingKey](https://news.google.com/rss/articles/CBMirwFBVV95cUxPRExCekw1bi01clVWX000RDFNOGpNOEVTVm13SDE3NDdBTUFUOURwS09tYkhtcE9fQTNiTUk4bDd2WmtWRnhlZkQ0NlJWWnV3UklmSGcwVnhSTjNOTmV6ci1FTW42Y1hjMVhoZXFfVUpGWHVOYU1tVGVlUFk2ZUR1SXhNRVV4a3Nia3JrbjFBWUZxdlptVUR3VjN5V2x5ZGFiVi1lTTJJQUFuX2l1LWsw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 18 Oct 2026 02:08:15 GMT
- [Can Micron and Sandisk Break the Memory Cycle? - NAI500](https://news.google.com/rss/articles/CBMihAFBVV95cUxPRzJqODlXeGhqbXlvWHlkRC13dXRvYUY1UkRadDF4SlpXTkpEM3ZHSS1wdDM3NzZtN1UtdExoQUwxcVZ3aGJKODZkZl9IMTBCenp3RFpObWJWVFRKcVRZYkw4bGMzN1JYMmZiajVDUlJzeWFsWkthWGFibDI5YW44eHJFVmY?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 17 Oct 2026 01:36:10 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：China AI supply-chain IPOs hold firm despite valuation pullback, Citi says - Reuters；AI stocks plunge. Inflation heats up. Where we're still finding opportunities - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +17.50% | +7.53% | 529.05 | 529.05 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [China AI supply-chain IPOs hold firm despite valuation pullback, Citi says - Reuters](https://news.google.com/rss/articles/CBMixAFBVV95cUxNcnFDdU1MSGd4Ylh4aktUWnlOM2V2RklNLXAxVm5QNThadUkzS2k1cWhoNnJpQkF3Nzk2U1c5ZlJlbUhGVFVpZTIxZEJYak8yVmtjVVhBdGs5NnVjVlowQnhRaWw1enZTVjBIVS1Wd2wwMkQtV2lYelR3MTFfVVlRRTBfMlBOUTlDYlI4UXdBZEFfcUFQcVNNNHVzOTR4bnUyanUtRE9nVkdnbTk4VHJvRWVxM2xjcXhjVUI4WVh2Y3Q2Q0Fw?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 17 Oct 2026 08:19:38 GMT
- [AI stocks plunge. Inflation heats up. Where we're still finding opportunities - CNBC](https://news.google.com/rss/articles/CBMiwwFBVV95cUxQSWIyUlNyQi13dVB2VVh3WTZjbWR1cV9OdlFZblJWVGdNeHhlQ2kzb2lfZHU2dzRjMGZLZWhnU2NFRmw3OWZFT2VSQktMQU9hc0VScWs1SGxfeURwTEtLbzVJMTVfbU9rVzFyY0FqZ3EwU0V2U2VkZjdlQjZ6X1ZDNFdyZjgxWnljY0RSZVVWY0F4a3BwaDFhamYzT0JCazJ4THpLSHN1Xy03SUQ3aVB0U21UYi1tVEdyLWVuX2gtNExRQlk?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 17 Oct 2026 15:42:34 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel (INTC) Lands A Major Customer For Its 14A Foundry Process - Yahoo Finance UK；Intel (INTC) Lands Major Foundry Customer As 18A Output Tops Targets - Simply Wall Street；Semiconductor market to remain solid ‘at least through next year,’ South Korea finance minister says - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | -21.65% | N/A | 89.85 | 114.68 | -21.65% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -2.81% | -5.10% | 2,420.00 | 2,480.00 | -2.42% | 不適用 | 86.28 | 28.05 | 511.86B TWD / 54.65% | 2026-10-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | -6.01% | -9.83% | 133.00 | 164.50 | -19.15% | 不適用 | 6.68 | 20.00 | 25.35B TWD / 27.22% | 2026-10-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -3.01% | +7.02% | 214.13 | 228.38 | -6.24% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | +2.45% | N/A | 528.75 | 528.75 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | -9.49% | N/A | 878.84 | 971.00 | -9.49% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -12.35% | -17.86% | 1,299.30 | 2,335.00 | -44.36% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -11.23% | -12.97% | 328.75 | 446.77 | -26.42% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 3 篇新聞出現相關標籤。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 3 篇新聞出現相關標籤。

### 主要來源

- [Intel (INTC) Lands A Major Customer For Its 14A Foundry Process - Yahoo Finance UK](https://news.google.com/rss/articles/CBMihwFBVV95cUxPU1BQVWdlWUoxYURMU2VZS2QzNzF2MjU5X2Q2V3VsM183eWh1RGhZTWczejEyWHNJaHRieWlGQl8zX0lLaUs3ejkwTExYbUdWaEdvd0FNYkNocDJfdS1Ca2FzMGpIck92anJKcHpjUHRubkswZVFwS2dCSjJ2eERuSU1qS01WSEU?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 18 Oct 2026 15:12:09 GMT
- [Intel (INTC) Lands Major Foundry Customer As 18A Output Tops Targets - Simply Wall Street](https://news.google.com/rss/articles/CBMiygFBVV95cUxOYld4UmM0U1VqUEl4TnVsMGtJZURnVmlqYkxXcXY5Q0FlWjBNcEljVjdhVVhseVpLMTkxX1laa0ZtWVpvMmxyd1lUdllsajE5SkMxem02d0dpZUh0MEFMNFZZZHNsN3diSXk1OWxtMFp4ejlkX2lEV2dzX1QyVzB6N2dqakU1c19qWTJ4Ni1hdWlBa1FVei1XNmR2ck1wNlBac0pvMVBwQUxBOTVaaDdoNm5DNFQ4ZWw2Q0tKRHozVUotcnluYVAtUkN30gHPAUFVX3lxTE5jNl9HdE5yUTRza3BVcXRHLVhfMEJibGszelpxal9zaU1IVEd3eEZ0MTlzbDJ6V1Vwcjl4d3M1MGNndEpfMnRsUHJoVnFYY3FMblpwVGMtUUlJYUljZFFYT0RDZl81U0pVMFlzZ29udU1KUWc2OGpTVVM5WndJbC1HeE5lVjJFdFp3SVAxcEhyZGphNG4xTm5VZExTT204bW5vaVVKdGR3N3JnMC0yWG05bmJRX1loV1RDUlJRdE83WWVWV3lNMDctaGFyQ1diYw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 18 Oct 2026 01:37:36 GMT
- [Semiconductor market to remain solid ‘at least through next year,’ South Korea finance minister says - CNBC](https://news.google.com/rss/articles/CBMijAFBVV95cUxPZXhtaE1RUk5kMDU2aUdhQThmY1M1bzNaRmNYbDhMZGZsZ005eHVZWU1zM19WVHR5djJKcVIzVTFIZWpMMkZ0THljQXdmZTA4dU9nZms3OFhpd2IwdlVndGZzM3RkVlk5MXJLdmtNVDNZOHRKejNIbzVfaWJoUThhSTZyQm1WRng2blVuR9IBkgFBVV95cUxNazg5ZWV5amlrcnpLZkZnaDd5SjZsSmdXbVBEQVFfYUdZdUIzX20wbHJMNk9JRWtjZkhqRk8xZlpvenVvNGtoRWVHU3ZhMk1PZE1lOXBjZDFoNjY5cDFaOFpOd2Q3SkdxWXFLVHhUSUNqdDhJeGxWRkhwRXpoTnNiZVU3eGZiSzRFb1BZWEJiSVU5Zw?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 17 Oct 2026 16:31:29 GMT

## 新興題材：MarketBeat

摘要：新興題材：MarketBeat 相關新聞集中在：Intel Corporation $INTC Shares Acquired by Robertson Stephens Wealth Management LLC - MarketBeat；Intel Corporation $INTC Shares Bought by Counterpoint Mutual Funds LLC - MarketBeat

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | -21.65% | N/A | 89.85 | 114.68 | -21.65% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Corporation $INTC Shares Acquired by Robertson Stephens Wealth Management LLC - MarketBeat](https://news.google.com/rss/articles/CBMi2wFBVV95cUxQUGh4amVKQ3VyTEhMRDE2Ny03VERJb0p3Z1EtRWx1X2xkSlBDUmlwbmxYVkxIR3lJcVF1bVY0QXVfM2M2c3pPLXlISzZkd1lkdDRTNWl0MDRPRnFTM042d2l5cDdjR3MzdWJEMnBRU3U1MDNsY09JWWxMaFJpZFRjaW5lOWVZekhSd0ZsZ0hrcHVKNFcyU2ZlVXFIdGltcW9iaUdSZGhvUkNXbXpBOWQ4UERsTFViOTFVazlBc2VuWHcyS3dzYjZFR2N1QmhfUnZoaktnNUJmdTAxLUE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 18 Oct 2026 10:01:54 GMT
- [Intel Corporation $INTC Shares Bought by Counterpoint Mutual Funds LLC - MarketBeat](https://news.google.com/rss/articles/CBMiygFBVV95cUxOV29SZ0dDUE9KSEdrMXZWVUl4SWlTZzAtWkRtQTNid21lNWNNNlJmNXUyVTlPQ3p3aERhdFAxeFRrdEhlX05YaVR2Ujg3cjVISnJHTmRpdm9BR0hXSkRUaUx1YmM5T0dxdEhxWGpxWFRxZXRaUnNfNXhpejhWWjVUQV80Rk9IeFhFTHl1QzdTazZEZUdJZnZzYm8zZmNWd0pPTjRkOXNBTWJkdllGYzdFTjVIZUlCc21Tdy1jN0JveWxTX0x6NFpDNnJB?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 18 Oct 2026 08:20:05 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：AI 破解理論科學問題比例兩年從 2% 升至 35%，MIT 研究指多領域將迎巨變 - TechNews 科技新報；從 24 天縮短到 3 天！AI 模型「除護欄」速度狂飆，原廠安全設定恐淪為裝飾 - TechNews 科技新報；25 歲工程師捨微軟 640 萬高薪，靠 AI 零資金創辦理財工具 Treasury - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 新聞直接提及 | +0.50 | +17.50% | +7.53% | 529.05 | 529.05 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 產業/供應鏈推估 | +0.04 | -21.65% | N/A | 89.85 | 114.68 | -21.65% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.03 | -3.01% | +7.02% | 214.13 | 228.38 | -6.24% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.06 | +2.45% | N/A | 528.75 | 528.75 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.03 | -2.81% | -5.10% | 2,420.00 | 2,480.00 | -2.42% | 背離 | 86.28 | 28.05 | 511.86B TWD / 54.65% | 2026-10-01 |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -11.23% | -12.97% | 328.75 | 446.77 | -26.42% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.02 | -9.32% | -9.81% | 671.00 | 703.00 | -4.55% | 背離 | 13.92 | 48.55 | 88.13B TWD / 45.52% | 2026-10-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.02 | -6.08% | -9.38% | 4,250.00 | 4,920.00 | -13.62% | 背離 | 60.69 | 70.19 | 55.40B TWD / 1.97% | 2026-10-01 |

關聯理由（前 3）：
- MSFT：新聞直接提及「微軟」，共 1 篇新聞命中。 同時符合主題標籤：AI, datacenter。 方向判斷命中詞：恐, benefit, boost。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：恐, benefit, boost。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：恐, benefit, boost。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AI 破解理論科學問題比例兩年從 2% 升至 35%，MIT 研究指多領域將迎巨變 - TechNews 科技新報](https://news.google.com/rss/articles/CBMijAFBVV95cUxQdEJFUWRXSy1MdUVWdEZibHI5alg3Sjk3Y1FNdV93ZVNBUW1oOG9zU0tTclRCbV80TDZxRTlWVGw5VFN6V1dkWGhRazhWTDVKRlJTXzZUZEJ6MUEyR0RTYU1wb3p1TDI1emFjSUdXRkxVY0JNT2wxOHJUb3hHQUJ5cW5mMFhXUDFNOTRuNA?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 18 Oct 2026 23:24:24 GMT
- [從 24 天縮短到 3 天！AI 模型「除護欄」速度狂飆，原廠安全設定恐淪為裝飾 - TechNews 科技新報](https://news.google.com/rss/articles/CBMirwFBVV95cUxPZjRteXZ1c2kxeWpHblhtWE5hVlUxVXFWOVpfT0ZzWGwtblNwWFlCb0RtSngwNDYyZEcwUWI4eW9IVFRQTlBfLUwwbWVab1FCZUZNaVVPcGNiU0N0S0JSb3V6MEhmZlRUVVpTc3MtbFpaZ3RMLTBFOXZ5azhRRi1GcmJwSlc1bHJnMGFSNjJwVVJIS0JRdENQbTcwQ1ZLX2VOZ2doSWNCTmtMdXNMazNJ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 18 Oct 2026 23:19:24 GMT
- [25 歲工程師捨微軟 640 萬高薪，靠 AI 零資金創辦理財工具 Treasury - TechNews 科技新報](https://news.google.com/rss/articles/CBMinAFBVV95cUxNQU1wWVBmLWhQdjFhZkRTTzJEMlROTER5d0VkckkzMXA3VUxyRnhOTDlTS242OWhtTXRfVk00UzZSaHpnVmRnT2pvNktFRWlzX1ZYSVAtMllFRGRmamM1bXVQMFRFTF8zZFA0MV9ZTjFaT3VPRTNOY0RkOGJlbUx3Q25fZXRBeDUxbXRuOGVHOVA5dHRkQW1VRVJHaHg?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 18 Oct 2026 07:34:46 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：個股動態報導內容-425DAEAF-2F6A-4943-84B8-412DF449A1DC - MoneyDJ理財網；空軍壓境！台股警鈴大響 後市三情境推演 預期大盤46,500點附近有支撐 - 經濟日報；四大本土投顧：台股震盪後開新局 多頭有望主導新一波走勢 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-425DAEAF-2F6A-4943-84B8-412DF449A1DC - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilAFBVV95cUxQUEVNcmNHYVNXV1F6emxUdXdPVENKQ2YwVUZmeTJRRTI1RldkVE5YMC15Mmpxb1M1ZXVVMS1yelNBNzhhdEROWFI2WWljNnpWNElScHRLbnZYU05HNkxlV29RV3ZzTE1pNG12a002Tk5va19IZzNQUDgyQm5MdFRXNjdHRGotYmJDb0xIU3ZYaE5KeWN6?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 17 Oct 2026 19:15:26 GMT
- [空軍壓境！台股警鈴大響 後市三情境推演 預期大盤46,500點附近有支撐 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBLU0FESTRmNDUzNEhrZ2J6eTlXTDRqV291WDVCU1FoYmM0SjBLa055V0tHVWJsZTlMNDU4OTZCMjRnTldaaHNic3c5QkQtOEFZcFJvVVJlVHk1QdIBX0FVX3lxTE53Y0VHQ1AyWjFseDBnTnB0bjJPOXFkYkhGY2RmWkpuakY1bjFDbEJkdEs5XzJvSWtJYlpYc1drRzZxU1U1ajY3MFp2ZTh3d3RnbVRsLWM2S0hxTWdGSWtV?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 17 Oct 2026 09:00:00 GMT
- [四大本土投顧：台股震盪後開新局 多頭有望主導新一波走勢 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBzMmdidUQ4OHRjbGprVGwxczg4ZkljMmN4aE93d21ZVWdTM0wtcmJ2T1VpVktKOGpMMXdIMTdGN2JQb3dCbmlkQ2VwZU01Yk1RYmFEVWpyeWtLQdIBX0FVX3lxTE5OZUhfekJ5ckdrdFlBbmFuWDYzSkI3SUxPOVdCekprN0YtNmR6WDFyWlZ3ZGF6OExRbnBJSUl6aHIweWkwRUFMRmJFOXZadU5iX0xmOXRhejNCVGI4bC1R?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 18 Oct 2026 17:29:02 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：法人專欄分析內容-台股-MoneyDJ理財網 - MoneyDJ；法人專欄分析內容-台股-MoneyDJ理財網 - MoneyDJ；華南永昌-桃園 對 尚茂(8291)個股 單一券商歷史明細 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [法人專欄分析內容-台股-MoneyDJ理財網 - MoneyDJ](https://news.google.com/rss/articles/CBMilgFBVV95cUxNRWVwajBXUmhZem5mRG9HbWRnZWVwYWdUQ0FxRzVUU2lsblR1Y1N6dThjQzhmSm9fODk3SzFxZmVXN1RSZmtzRWZPM2RhS2hXRkdYRkM5d3J0dExfV052SUtDand6MWd1Nkl6NDVIUVR0WE1lZVZKMUk5MU1iZF9SNXJ5VDlLQ3ZIeWpySmtkWjZJX0o3bUE?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 18 Oct 2026 16:30:28 GMT
- [法人專欄分析內容-台股-MoneyDJ理財網 - MoneyDJ](https://news.google.com/rss/articles/CBMilgFBVV95cUxNcE5ITnE3aGM4VE5ueUY2bV9jVWY1ZUxJVkxuVGhRYmtIeHMzcWRMRXUxODd0TW5mMmRCWUdYSnFQRXdnRXYzWEtVUW5lTzNCSGZGMGQzSWtlYUlXbkc3VUQxYW1yX2dfSnFiWHBuOTlaOVcyQjVsVVVlYWczbHQwZmRKS0NKSjV4TWk0bF9KbGtRMDNXcnc?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 18 Oct 2026 16:30:28 GMT
- [華南永昌-桃園 對 尚茂(8291)個股 單一券商歷史明細 - MoneyDJ](https://news.google.com/rss/articles/CBMigwFBVV95cUxPTjd5RTdXaVpYbjdIdVh2MkVieXRGSTJ4UW5LcFhFelF2NG1DU1ZIZVRVX3psRnp5UndPaExid1NseDlOc21yLVJ0WnczTThCcUpJc1dGQXh3LWh4bDI2c3M0QnNxTjFHM09xVmZBSGF5TmRUUDZuM1M2Z3FrODJFMEd2NA?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 18 Oct 2026 11:59:59 GMT

## 新興題材：B072

摘要：新興題材：B072 相關新聞集中在：個股動態報導內容-312C252C-4EBB-4709-B072-9A69E0A9EB03 - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-312C252C-4EBB-4709-B072-9A69E0A9EB03 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilAFBVV95cUxNSF96Wk9oSDlybzZjanpOQklsbmlEazR0MUVfRHg2bGhuVlp2bFcwV2I0bWJiakc5X1dWMVJva082OGVFcC00Y0MxX1cxOTh4ci1jTDMwMW5zOTZsU0NSMTVqekVxV0hMSXlPeGdDcXZWOVJaTFZrNi13NDU1Wk5sMno3ZC12N0VWNWZSc0YwY3ZSZUlQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 17 Oct 2026 18:47:25 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
