# 每日股市熱門話題分析 - 2026-08-29

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **散熱與液冷供應鏈**｜中性｜熱度 4｜市場確認 96.19｜同向 1/1
2. **關稅與供應鏈轉移**｜正向｜熱度 2｜市場確認 96.19｜同向 1/1
3. **利率與成長股估值**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
4. **記憶體與 HBM 供應鏈**｜正向｜熱度 3｜市場確認 48.52｜同向 1/2
5. **半導體與晶片供應鏈**｜中性｜熱度 7｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.10（樣本 10）
- 5日相關係數：-0.01（樣本 10）
- 同向比例：4/10

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 散熱與液冷供應鏈 | 96.19 | 1/1 | 0 | +8.73% | +9.01% |
| 關稅與供應鏈轉移 | 96.19 | 1/1 | 0 | +8.73% | +9.01% |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 記憶體與 HBM 供應鏈 | 48.52 | 1/2 | 0 | +4.50% | +1.02% |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 0.00 | 1/6 | 4 | -8.29% | -1.68% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價呈負相關；應檢查正負向詞庫，並降低新聞直接提及但股價背離的權重。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-08-15 | 0.24 | 0.30 | +68.75% | 16 |
| 2026-08-16 | 0.37 | 0.51 | +70.00% | 10 |
| 2026-08-17 | 0.49 | 0.60 | +66.67% | 12 |
| 2026-08-18 | 0.29 | 0.36 | +80.00% | 10 |
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

## 歷史回測摘要

- 回測日期：2026-08-29
- 近5日 3日相關：0.23
- 近5日 5日相關：0.46
- 同向比例：+37.50%
- 權重狀態：已調整

- 方向準確度：+37.50%
- 信心排序準確度：0.23
- 診斷：正相關

調整原因：近 5 日信心分數與後續報酬呈正相關，提高市場確認、歷史題材與直接提及權重。；關鍵詞×公司後續樣本有效 5 筆，未達 30 筆，不調整樣本權重

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

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報；【即時新聞】最新！奇鋐受惠輝達水冷加單，Q3營收估季增15% - CMoney投資網誌；本季營收續創新高可期 法人調高奇鋐獲利預估值及目標價 | 經濟日報 - LINE TODAY

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | +13.90% | +17.28% | 3,360.00 | 3,360.00 | 0.00% | 不適用 | 75.13 | 44.79 | 18.59B TWD / 57.39% | 2026-08-01 |
| NVDA 輝達 | 新聞直接提及 | +0.43 | +8.73% | +9.01% | 217.55 | 227.98 | -4.57% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱、奇鋐、3017」，共 4 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：跌停, 受惠。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 27 Aug 2026 01:04:04 GMT
- [【即時新聞】最新！奇鋐受惠輝達水冷加單，Q3營收估季增15% - CMoney投資網誌](https://news.google.com/rss/articles/CBMikAFBVV95cUxNenhIWFhSb2ZPX1hYMVZ1UDVlSlIxRW9CSlFPR3FOeTViSjFwLXFHc3ZIUzRNaFdlaW1ISjk1WGFOX3c2TWItZzBuU2J2WE0xSklXVVZnY3IybzM3SklrTzZ1am04bnd0Yzd2Wi1tYklTLWc4M29iWE5NZHhvZm5pemdOVDUtYlRQMndnSnh6X0U?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 27 Aug 2026 22:46:39 GMT
- [本季營收續創新高可期 法人調高奇鋐獲利預估值及目標價 | 經濟日報 - LINE TODAY](https://news.google.com/rss/articles/CBMiVkFVX3lxTFBNYXFYREV6S1FaeTh6V2V4OVllbHZ2T3RLcFhjeVNSSWUtRTh1VDZjRUVjb1BDazRTWTNHSjBRS2NqY1hSem1zQTVaNncyNjlLU05MUktR?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 28 Aug 2026 06:41:23 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：整理包／黃仁勳概念股笑了！輝達季度財報超預期 完整台廠供應鏈名單、潛在受惠股一次看 - 經濟日報；美國擬擴大半導體關稅！伺服器、筆電恐全中 科技業警告：恐成AI發展絆腳石 - Yahoo股市

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.43 | +8.73% | +9.01% | 217.55 | 227.98 | -4.57% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +21.02% | +37.72% | 319.70 | 319.70 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | +4.12% | +3.05% | 253.00 | 289.00 | -12.46% | 不適用 | 15.21 | 16.68 | 946.51B TWD / 54.19% | 2026-08-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [整理包／黃仁勳概念股笑了！輝達季度財報超預期 完整台廠供應鏈名單、潛在受惠股一次看 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBQUlViSHpPeDVlY29yaHFNNE5NcVlUQnE3ZThTcXRGNHgxYTVPOVVTRDlaTDV6Zml5WEwxVHNSeGFDcnVHUHhRSW15SzNpU0dYVDU3dThWNEVCbkZI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 28 Aug 2026 11:00:00 GMT
- [美國擬擴大半導體關稅！伺服器、筆電恐全中 科技業警告：恐成AI發展絆腳石 - Yahoo股市](https://news.google.com/rss/articles/CBMiywNBVV95cUxPT1JhM2dRR2Y0TEtOZXFSaU54eGtxV0p2ZnJkZ01ydWNVcHRCRkRQS2pQN19yZU1YRE16RTdQN2k1SDhjMTRRX3VTZ1JCNzRJOGtUOFFsQ1pheWt3Tm5wcFZGVlA3aDlHckt0QjVFa3F6bEZYVExoMDdldjNDanR2eXJIMFJRbmlJVDl2dUFxaV9OYjF2Um9kYUNiT1Z3RTc1SEZWNEFaZ3doTVYwNVJ3MWpSSl9wRzNsQWlmcTFuRkVUNGlRNlItMXVSVnhtWW1hRjhOSkY3U3kydUctUTh4X2MyVDdnR0MtQ240aDJ6Ung3XzB3TkRQTU0xN01RTlpHT0owRGdTSGxaazNpbEpmVXVYSjdvUGE5Wko1QjZTM09GQTlMX3JDRmN4NWtiU2JJTVFfRXl1M042enpvdDdhSHZxYzA1Y1RDYkJjWDJ5RmIybThwZlFmei1iZ0NQb21yM3VXeHI3TkpmY2ZEX2IzTXFjRXhzU3hzWmVYa0lROHJMQUFvR3lXeWhRREFiYlA3WTdfVkRNYUlMTHVqZmdWMlhHWkJsZEwzZEs1OUd4VmlvOEZqVzd4ZTVOUHFSM0UzZmppaS1EVHVIVWc?oc=5) - Google News source discovery | Yahoo 奇摩股市 Fri, 28 Aug 2026 15:15:00 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：本季營收續創新高可期 法人調高奇鋐獲利預估值及目標價 | 經濟日報 - LINE TODAY；華許放鷹了！通膨不乖乖降 Fed就得繼續出手 - news.cnyes.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | +13.90% | +17.28% | 3,360.00 | 3,360.00 | 0.00% | 不適用 | 75.13 | 44.79 | 18.59B TWD / 57.39% | 2026-08-01 |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +30.76% | +1.35% | 513.53 | 513.53 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐」，共 1 篇新聞命中。
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [本季營收續創新高可期 法人調高奇鋐獲利預估值及目標價 | 經濟日報 - LINE TODAY](https://news.google.com/rss/articles/CBMiVkFVX3lxTFBNYXFYREV6S1FaeTh6V2V4OVllbHZ2T3RLcFhjeVNSSWUtRTh1VDZjRUVjb1BDazRTWTNHSjBRS2NqY1hSem1zQTVaNncyNjlLU05MUktR?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 28 Aug 2026 06:41:23 GMT
- [華許放鷹了！通膨不乖乖降 Fed就得繼續出手 - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTE01U2VpUXpCUzJRb3VlZldTZmUxQ193c0p2LTN5aW5HdWVJWnVsVGpzemdFWmVKaUVULTlrNFFIOG53VjVpdlJLWmxUUnZzMGM?oc=5) - Google News source discovery | 鉅亨網 Fri, 28 Aug 2026 14:18:13 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：NVIDIA Surges 6% as a 70% Growth Forecast Overrides a Memory Margin Warning, AMD and Intel Tick Up - 24/7 Wall St.；Palo Alto Networks CEO Nikesh Arora Warns Memory ‘Supercycle’ Will Eventually Turn Cyclical, Flagging Risk For Micron, SanDisk - TradingView；Why are memory stocks MU, SNDK, and WDC falling despite Nvidia’s results - TradingView

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.50 | N/A | N/A | 932.86 | 971.00 | -3.93% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.38 | +0.28% | -6.96% | 1,484.98 | 2,335.00 | -36.40% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.44 | +8.73% | +9.01% | 217.55 | 227.98 | -4.57% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.37 | N/A | N/A | 465.58 | 516.10 | -9.79% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.37 | N/A | N/A | 89.47 | 114.68 | -21.98% | N/A | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「memory、Micron、MU」，共 3 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：risk, growth, surges。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk、SNDK」，共 2 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：risk, growth, surges。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 2 篇新聞命中。 同時符合主題標籤：HBM。 方向判斷命中詞：growth, surges。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [NVIDIA Surges 6% as a 70% Growth Forecast Overrides a Memory Margin Warning, AMD and Intel Tick Up - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi1gFBVV95cUxQRUhUUDNGdzI3WWVWRWtvM2VVeTZXTDNxU1RhVEZ2N1F0TzNSNTN0b3E0dlAxNXR2NURYaDFTLUtmUlJfUHBrOFVKTG1RUHJZcFBpSEk4ZDlXOFBtU21IdDhMS29PLXBEREo4ZEVpbXlyVVhiLWlXTFVHd1Q0N1JJZHFPYVZ1RkdtTjZkLS1NVGtsN1lsaThtWDhSZ0FUUzRNV1V3c0EyWGVYMjViUnQ3VEtzMHZ0MGo0NUhTQlB1enZYeHRRMnBHVXZhRUpOSDFxN1IwcUlR?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 27 Aug 2026 13:30:00 GMT
- [Palo Alto Networks CEO Nikesh Arora Warns Memory ‘Supercycle’ Will Eventually Turn Cyclical, Flagging Risk For Micron, SanDisk - TradingView](https://news.google.com/rss/articles/CBMijwJBVV95cUxOZ3JOZG5Famt0S0VvRHZiNHhRTDFMMmVFZEtBTHhvcVp1WFJQclJtaWh2ZWUzZTVzY1JOend5a2lrbGFWTzNhdXFwanFEX051ekUxbTZGQTgyU1FmVFJuMkljX0Vlby1IX1lHbGZKUnE3c3NCQVFUQzRycml3V3Bodkd6N1F6dmFXMHVrRUhHelFCZ0RJX2RFRTBBMzY5eWRaMWRSVDJ0N3FIMWE4OTMzVFNpQ3h0eVMzdHRPcUdUalBHZ0hMTnFhUjdKcW5ua1FsOFNJNnJDQS1ydndhamZkUW5oUE5Ha05pclFMazFaV0NaQzVWT2R6UzV4M0tEVFNuVjhoVkdvXzUtZXZvOFRV?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 28 Aug 2026 07:27:05 GMT
- [Why are memory stocks MU, SNDK, and WDC falling despite Nvidia’s results - TradingView](https://news.google.com/rss/articles/CBMixAFBVV95cUxQdjNQcDgxMjZUdWlZaTNFbzl6UXI5aGZBTjU0LWltZXFaU1JqbmY4SHpxUURIakhBX3FFMWo2S2VDX1h5dkhyc2Q2MFhkNllESHNqTUZXWURUR2RRVlVZM0dsRmxKWWpwemZhcEpINHZtUU5NcnJYZzRVZkdKc3poQmN4VG44WGtpaVdiV0tNdkIyaXk1M1VUZ3ZHbWVHOWxiMmZsdjI4c1NYMFU4UXRwNVBzQlMzZXI2c0pRcTBjdTAwcll3?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 27 Aug 2026 15:33:09 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel Stock Rises 4.4% as Nvidia Forecast Revives AI-Chip Demand - TechStock²；INTC, AMD, AVGO: Chip Stocks Jump Premarket After Nvidia's Blowout Report - TradingView；AMD and INTC Are 2 AI Semiconductor Behemoths Ahead of NVDA in 2026 - The Globe and Mail

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +8.73% | +9.01% | 217.55 | 227.98 | -4.57% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 89.47 | 114.68 | -21.98% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | N/A | N/A | 465.58 | 516.10 | -9.79% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | 0.00 | -2.37% | -11.65% | 368.79 | 446.77 | -17.45% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +0.83% | +0.41% | 2,420.00 | 2,425.00 | -0.21% | 不適用 | 86.28 | 28.05 | 467.58B TWD / 44.69% | 2026-08-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +4.00% | +11.59% | 130.00 | 164.50 | -20.97% | 不適用 | 6.68 | 19.55 | 23.84B TWD / 18.98% | 2026-08-01 |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 932.86 | 971.00 | -3.93% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | +0.28% | -6.96% | 1,484.98 | 2,335.00 | -36.40% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA、NVDA、輝達」，共 4 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel、INTC」，共 3 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Stock Rises 4.4% as Nvidia Forecast Revives AI-Chip Demand - TechStock²](https://news.google.com/rss/articles/CBMijAFBVV95cUxNSDZXWFlocl9hUUNzM3B5dkI4R19iWDZPMloxRnlmSVdiWEEzc25SaWpoOHlsYktTQzRXS2FGd01mNlR4ZGFZZTJ0VWhJZjZfSVhxbDZXZVlON2ZFU1Z4VElkZTBDbEczT0dQc2I2OHlfMjhxa0IzOXAwUldVRFdlUXRJYkRFOW9vcmhXMg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 28 Aug 2026 05:17:05 GMT
- [INTC, AMD, AVGO: Chip Stocks Jump Premarket After Nvidia's Blowout Report - TradingView](https://news.google.com/rss/articles/CBMiywFBVV95cUxQSHlsWWM3MEJWQnpMeGtNZDQtVFRjblZPNHVMZzZtX1VNX3o4cXpMRjQ3QjZRRVpHUXVLVWNkRFlpWFBsb2M1aU9sTmcxZlVHWWhocEY0WWZILV9tWl9xNzRfTmZWU3hwZUJWSEtBaHNzTEtvdjljYnNpNU1ncUpHenlYNWgxTVVGUEZ1UzYzcWF5TGI2V1JTTDNZZUdoWHRWS1V5YkJ0ZTAtLWdIYjhDNFZFYW1OQjAwZWlMczVjUlNWN2ZJbVpnWnEtYw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 27 Aug 2026 09:43:17 GMT
- [AMD and INTC Are 2 AI Semiconductor Behemoths Ahead of NVDA in 2026 - The Globe and Mail](https://news.google.com/rss/articles/CBMi5wFBVV95cUxNWUtadkxRWGFmYU5IVjU2dldyQm9IdmVWYWNVZlUxN3RlN2RkR1RwaFI1bXBmMHBvOWVpVU50QXlseVpfVG1XNkJVVTN4Zjh1NVlLN1RaZm5GYU1iN0pwQTRRTkFFTTdoanljUFhzZXYtN2E3OElaamhQMWtfR2ROOFBxQWtpZTNEX0EwN05sVVBqVERmNzBnclhEMkFJSXZISDk1TXBiVDl5LVlUUGVQRlpKSmZtZzIyaS1vLU50UmZPMzc2RkZMcmZJZmozdkhEbmRxY2FqSXJpdklIVl9SRnppdkswRG8?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 27 Aug 2026 12:51:02 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：外資錢進來了！台股周漲1,107點 這周最愛的竟不是 AI 股 - 經濟日報；Intel Stock Rises 4.4% as Nvidia Forecast Revives AI-Chip Demand - TechStock²；Marvell Leads AI Stocks Lower After Earnings That Narrowly Topped Estimates - Investopedia

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | -0.29 | +8.73% | +9.01% | 217.55 | 227.98 | -4.57% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | -0.59 | N/A | N/A | 89.47 | 114.68 | -21.98% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.54 | N/A | N/A | 465.58 | 516.10 | -9.79% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.04 | +0.83% | +0.41% | 2,420.00 | 2,425.00 | -0.21% | 未明確 | 86.28 | 28.05 | 467.58B TWD / 44.69% | 2026-08-01 |
| MSFT 微軟 | 產業/供應鏈推估 | -0.02 | +30.76% | +1.35% | 513.53 | 513.53 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -2.37% | -11.65% | 368.79 | 446.77 | -17.45% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.02 | +5.08% | +5.79% | 621.00 | 680.00 | -8.68% | 背離 | 13.92 | 44.93 | 73.78B TWD / 43.15% | 2026-08-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.02 | +6.69% | +5.15% | 3,985.00 | 4,310.00 | -7.54% | 背離 | 60.69 | 65.81 | 48.47B TWD / 12.16% | 2026-08-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA、NVDA」，共 2 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。 方向判斷命中詞：lower。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel、INTC」，共 2 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：lower。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。 方向判斷命中詞：lower。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [外資錢進來了！台股周漲1,107點 這周最愛的竟不是 AI 股 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5DWFhlckNUVEhYRzY1blVQV18yRHJ1V0ZIbDFKeTZsbVgxY2x5eXJ6Sm8wTF84VVlZZzRIMW45ZXJXQUFZZmFoaG45dHZwdmVZVHYyazJhb2dkZ9IBX0FVX3lxTFBmbTVkaWFLdTNZWTA5aHRJYldIZ1pPSmFxRU5SQ2U1NWdZRW1HQjhzMFZ4dmJDR3BaWmQtb2dEeXk4TGxxcWdtRXgtM3BKaENScV8zVDd3eE5hdU93clpJ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 28 Aug 2026 12:00:00 GMT
- [Intel Stock Rises 4.4% as Nvidia Forecast Revives AI-Chip Demand - TechStock²](https://news.google.com/rss/articles/CBMijAFBVV95cUxNSDZXWFlocl9hUUNzM3B5dkI4R19iWDZPMloxRnlmSVdiWEEzc25SaWpoOHlsYktTQzRXS2FGd01mNlR4ZGFZZTJ0VWhJZjZfSVhxbDZXZVlON2ZFU1Z4VElkZTBDbEczT0dQc2I2OHlfMjhxa0IzOXAwUldVRFdlUXRJYkRFOW9vcmhXMg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 28 Aug 2026 05:17:05 GMT
- [Marvell Leads AI Stocks Lower After Earnings That Narrowly Topped Estimates - Investopedia](https://news.google.com/rss/articles/CBMixgFBVV95cUxPUFlkN0tIUUo4RExHY3F0b2xBUzlBRlZ4Q3E3Z2x5RXV2UlM3XzRzNzJXZXpkbWhNOEFjSk5FWHJVN1FUS3plQmt1R1NQQ2pzNTVWUTFMMDQydEt0RF9CY1VlRVpoMm9POG5kWGdUdldQaEZvQ1oxNi1sLVRLNjF1Qkt4X1U2alNRM01RcnUwTE02X0phQjFIZnlxbG85SHZPOFE2LS1XVkRKZjRQSENyMHJWNHZYdlJkekY3akhMSXVYZ09kRUE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 28 Aug 2026 13:54:57 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：外資錢進來了！台股周漲1,107點 這周最愛的竟不是AI股 - 經濟日報；台股六大利多 將挑戰47K 法人：只要量能放大 將攻向前高 - 經濟日報；台股漲356.23點 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [外資錢進來了！台股周漲1,107點 這周最愛的竟不是AI股 - 經濟日報](https://news.google.com/rss/articles/CBMieEFVX3lxTE1WRDdsQ2NvbzdfRXdlZDZOTDRIOUs4bl82U1RPb1FvaGkyU0hreDF5LURrdEZmZWxzUVI4UTZiV20zcE9lN0Y3NnZBV2YtUVNpdlg3MlFrYmhEQ3hiSDl2dmZYb1RCYkRVZFFMb3pXNXh3cVRSMHFTbtIBX0FVX3lxTFBmbTVkaWFLdTNZWTA5aHRJYldIZ1pPSmFxRU5SQ2U1NWdZRW1HQjhzMFZ4dmJDR3BaWmQtb2dEeXk4TGxxcWdtRXgtM3BKaENScV8zVDd3eE5hdU93clpJ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 28 Aug 2026 19:51:29 GMT
- [台股六大利多 將挑戰47K 法人：只要量能放大 將攻向前高 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1wOFFTWHBhenNfSGFtSnhUa1IyVHNvRFI5QnFaWmJmQjRNamJfaGJuejJDaXFJNzk5d0V1XzV2ZTE2Z2o3Z2RjNENjUjFZandvdUVnYTQ1M1Rud9IBX0FVX3lxTE1pZGZLWEtmNkQyWXNuUWRmekZpNEV6RGVtNEF6X1NmejFBc19tbXliTWlLeU5wM0F2M1FXZC1obnltUmhlT1NEdlhHZmtZNzl1eFdLb1R3NGUwUDd3bUdn?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 28 Aug 2026 16:29:11 GMT
- [台股漲356.23點 - 經濟日報](https://news.google.com/rss/articles/CBMidEFVX3lxTFB3V3dVcUhuQWV1S0JqUnhZZms2WWx2REdaS0toc0N4cWNQenZ2bktNbkhRTlQzcUM2eEg4ZXpEUl85Mnc0cnl5d0Z0cnVWeTY2eTRJVXlzMGNVRXV1U1JOUG5aMXZUeWpSVUxSNi1aa2h5Smtz0gFfQVVfeXFMTXdyczFMZ0hyN0JhVVpLRlN5UG94eGprZXBiYzNqTWhZYk1xMVV4RWhjX2U1aGRQTDYta0hnWmExN0pDSFJTWmQ1dHZwVkZCRlVUTW5TOERGbGVBcmt1cHM?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 28 Aug 2026 05:55:01 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》收漲356點、重返46K；週K翻紅- 新聞 - MoneyDJ；《台股盤後》收漲356點、重返46K；週K翻紅-新聞內容-基金 - MoneyDJ；統一證券：台股震盪盤堅，仍有利於多方- 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》收漲356點、重返46K；週K翻紅- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQRVVwbEIwU01selpIVks2Wk9mcG05TDFFVjFWMGx1d2ZraDY0cmd1Z0JuUTVvVmc2emFaYWZaVk96QmdFbFpUNVh3amVMNk5zeVROSllqZVNrbnFKNjZGS3FqNTB1NWc2aURNRXprcWdHay1HbWM4Q0dneVBqbko2SnBWVmVIdUY4bDI5ZGN0RnRmQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 28 Aug 2026 07:47:00 GMT
- [《台股盤後》收漲356點、重返46K；週K翻紅-新聞內容-基金 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxPaHEzQ1BPMWgxbDRwb2NWajM4cjJYTWlrQ0poQ0g4MTdNeVlmUGYybHZYeGFVNG9yVlpiMTlkbWlUYUZHdWVmaml2a2dvM2pTRnZwVm4zNlR5TmM1MkRidmwxVzNLSnlONzVBUjdYb01EWnQ4bElQemRMSWtmZjVtVVIzSG5uM1JNZDViVnRwMTk?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 28 Aug 2026 07:49:00 GMT
- [統一證券：台股震盪盤堅，仍有利於多方- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxOTTEzTFJjcEpnTHVIWkRGZl9tcVk3Wm9FbmhJZl92MWcxZl95VHFyZnRhRm5mdmZaQVBvYkt6SzltajZUMVZHOXBtQU1sdF9SdjV6SkZxaHF6UmVCclhKdGg2Z0dhRVlfdzBXbFRLN0ZtR2VUUVd1XzRsTlhWdlhPWVdUajJQdFN0ZUVLSllEVnNhZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 28 Aug 2026 00:41:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
