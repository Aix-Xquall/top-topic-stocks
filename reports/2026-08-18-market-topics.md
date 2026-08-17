# 每日股市熱門話題分析 - 2026-08-18

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜正向｜熱度 9｜市場確認 100.00｜同向 3/3
2. **新興題材：MoneyDJ**｜中性｜熱度 11｜市場確認 N/A｜同向 0/0
3. **半導體與晶片供應鏈**｜正向｜熱度 9｜市場確認 70.45｜同向 3/5
4. **散熱與液冷供應鏈**｜正向｜熱度 3｜市場確認 97.19｜同向 2/2
5. **新興題材：TradingKey**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.29（樣本 10）
- 5日相關係數：0.36（樣本 10）
- 同向比例：8/10

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 100.00 | 3/3 | 0 | +20.35% | +29.58% |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | 70.45 | 3/5 | 1 | +9.48% | +10.14% |
| 散熱與液冷供應鏈 | 97.19 | 2/2 | 0 | +9.06% | +12.04% |
| 新興題材：TradingKey | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：UlmltETmgV | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
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
| 2026-08-17 | 0.49 | 0.60 | +66.67% | 12 |
| 2026-08-18 | 0.29 | 0.36 | +80.00% | 10 |

## 歷史回測摘要

- 回測日期：2026-08-18
- 近5日 3日相關：0.50
- 近5日 5日相關：0.24
- 同向比例：+16.67%
- 權重狀態：未調整

- 方向準確度：+16.67%
- 信心排序準確度：0.50
- 診斷：正相關

調整原因：近 5 日有效樣本 12 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：AI Money Moves Put These Five Stocks In Spotlight Last Week: NVDA, INTC, ORCL, AMD, SNDK - TradingView；Memory Stocks Rally Wednesday: SK Hynix, SanDisk, Micron All Jump. Here’s Why - AOL.com；Bank of America Says the AI Memory Boom Isn't Over: Why It Sees Micron's Earnings Exploding 34% a Year - 247wallst.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.48 | N/A | N/A | 1,011.75 | 1,011.75 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.48 | +32.92% | +44.34% | 1,786.85 | 2,335.00 | -23.48% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.37 | +12.45% | +12.75% | 225.01 | 225.16 | -0.07% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.36 | N/A | N/A | 506.00 | 516.10 | -1.96% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.36 | N/A | N/A | 103.49 | 114.68 | -9.76% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 新聞直接提及 | +0.36 | +15.67% | +31.64% | 305.59 | 312.06 | -2.07% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、memory」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK、SanDisk」，共 4 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVDA」，共 1 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AI Money Moves Put These Five Stocks In Spotlight Last Week: NVDA, INTC, ORCL, AMD, SNDK - TradingView](https://news.google.com/rss/articles/CBMi3AFBVV95cUxPTVVVMU5ZcWxVWk1HRnNleEcxQ2pxZ3hXanVDQXQ2MENTR0k5dlVyWDA2OEZaaG13R2MxUm5SY182MXdWR3ZaYXZQbzVvUGlFdE1yRVhzTjhLNzQ5RkZDSkZ1aG1sQ2Q1M0RrRk00cnI3RlBCejZDMmhVTXFHTnpkdjBaU3pTM0pfU0NDejhjNld2SHh4V1A0NE1DUnVKT3hybzVyalVqbjJEZ3N6ZF9HQmY3SHV5anRsalpkV0o5TVF5NU1KQ2JnaXhlMkxfNW4wSVk4RElxT1BWZXBL?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 17 Aug 2026 01:48:00 GMT
- [Memory Stocks Rally Wednesday: SK Hynix, SanDisk, Micron All Jump. Here’s Why - AOL.com](https://news.google.com/rss/articles/CBMiggFBVV95cUxNYjRZcVE1OXphX2lEbzd4VkFVc0lmUDRSOGtsRnhJMVd4VkMzUHhEdXJwb21HOWdLUHVhclJzNGdzT2wxZnBHQV9CSFFKZ3FWSHc4Zk5POXVFN0pVZGowYlpGYUVEVmtLY01xamZBZGszVVl4OEZxdFZleExZdDJUejdn?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 17 Aug 2026 14:46:33 GMT
- [Bank of America Says the AI Memory Boom Isn't Over: Why It Sees Micron's Earnings Exploding 34% a Year - 247wallst.com](https://news.google.com/rss/articles/CBMi2gFBVV95cUxOZ2s4Qy1ZSlJUQ1dCbWVxQktYd2RPVkZ1UlpEcjBpU1BRRzNuUTJNNDVWMGJoRmw4SUpyUVY2NjNOZXRFVi1KeTlOTHUxMXhHd2dMT3ZNNmwyOGF1d1BTR0VEdkp6T20yc3l0amJvWWltS0Y4TzRFcjZPY1ZrSjhEZVNWN0VyMnRXNVM4UmlzeHg0LUxkZDRSOVV4cElrYmJ4bmV1bmJUc1g4MUFCQjJYelFDeWgzY1lJQzlSZE9ld2tCRWVtTzluRUtDaF9MZFJ6RkM3SC1kX3BHdw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 17 Aug 2026 09:56:30 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》量縮收漲46點，46K得而復失- 新聞 - MoneyDJ；《台股盤後》量縮收漲46點，46K得而復失-新聞內容-基金 - MoneyDJ；國票證券：台股多方架構尚未遭到破壞- 新聞 - MoneyDJ

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3037 欣興 | 新聞直接提及 | 0.00 | +12.00% | +12.90% | 1,120.00 | 1,120.00 | 0.00% | 不適用 | 15.49 | 74.57 | 16.25B TWD / 43.69% | 2026-08-01 |

關聯理由（前 3）：
- 3037：新聞直接提及「欣興」，共 1 篇新聞命中。

### 主要來源

- [《台股盤後》量縮收漲46點，46K得而復失- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxOSlpIQ0pCeC0xSlBHcHNrMmZ0THl5MVNqckwtY0xEMkJheDRSRFQ2WEwtdm9HYUp6bEg0RGlOUldDWmdhTF8yX3lkMUdfTXkySTdkZFowSjNBTmlOOXRvUlNxVk1meWdYVzJKSzI4a05PNWlzaHNRV1oxQWQ5RkVIU3RCY2tJR3ZKeFZkT095N0hmZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 17 Aug 2026 08:10:00 GMT
- [《台股盤後》量縮收漲46點，46K得而復失-新聞內容-基金 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxQcG92VktYdEFuVUluVXJydnh5cTVnSXI0TnlTZkZHY19yNTNYSkRSYjJWSUFWSDVFRk5JaVJvNTlTVEFHbDVvaURKaFV4VzFXOTJuQzVqUVgwOGNPVEhpakQzTEU5MUpPam5RcXRJTFRmRVFWTElDLWlhR1kweHU4MW1jdngtVnpkVi15TDhhTC0?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 17 Aug 2026 08:11:00 GMT
- [國票證券：台股多方架構尚未遭到破壞- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxOU1FJN040blZDa1ZrS1pUS3V4SVZibmJvQ2JBYk9UTXgxdHM2MmhvbGtIdk1Odk42d05sLVphMWdkejF0RkFKa21WSVBTbTc2ZzNQZFZFWVExb2J1M2tQakI1LWZEU0NJNzlBZWZOOEtTUHpiUTFPTlNDSHFYSnJUTm1zNDRnQWJjZXlmYTBCOXQ0dw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 17 Aug 2026 00:35:00 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Best Semiconductor Stocks for 2026 and How to Invest - The Motley Fool；曾海華：半導體擴產趨勢明確崇越下半年營運續成長| 產經 - cna.com.tw；台科大暑期材料營攜國際大廠引進AI、半導體實作模擬| 生活 - cna.com.tw

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | +0.08 | N/A | N/A | 103.49 | 114.68 | -9.76% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.04 | -0.62% | +0.84% | 2,400.00 | 2,425.00 | -1.03% | 未明確 | 86.28 | 27.82 | 467.58B TWD / 44.69% | 2026-08-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.03 | -1.22% | -1.22% | 121.50 | 164.50 | -26.14% | 背離 | 6.68 | 18.27 | 23.84B TWD / 18.98% | 2026-08-01 |
| NVDA 輝達 | 產業/供應鏈推估 | +0.04 | +12.45% | +12.75% | 225.01 | 225.16 | -0.07% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.04 | N/A | N/A | 506.00 | 516.10 | -1.96% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | +0.04 | N/A | N/A | 1,011.75 | 1,011.75 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.04 | +32.92% | +44.34% | 1,786.85 | 2,335.00 | -23.48% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.04 | +3.89% | -5.99% | 392.43 | 446.77 | -12.16% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 CPU, server CPU, x86, foundry；其中 1 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 1 篇新聞出現相關標籤。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 1 篇新聞出現相關標籤。

### 主要來源

- [Best Semiconductor Stocks for 2026 and How to Invest - The Motley Fool](https://news.google.com/rss/articles/CBMipgFBVV95cUxOT1dYNXFONXk3TGdVWUstTHRMeGNyX1RDMmVLWUNsOFBvSGplTndkeHA1YU54QXhKOHV2RXFmOS1kY2lmMjNJVFBodDQ0ajVCZm8zMUlqM0NBV1R5MzEwTk9TUUZuWUFTQ1BpV1otQW9DTnhiMGJLRS1sd0x1VUR6U1dQU2pWM3kwWmx2UHhtRDZxZmJIT1dPa2NtYVZQd3FEU1hld2xn?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 17 Aug 2026 05:04:00 GMT
- [曾海華：半導體擴產趨勢明確崇越下半年營運續成長| 產經 - cna.com.tw](https://news.google.com/rss/articles/CBMiXkFVX3lxTE4xZjJKQnExYkVDOXlya2tlb2wwNEZNZEx6Z21rT1hodHl5ekgyNGJxWm9yNkcxT2RUR0xnQ3JUdVlVWFp2TkVrMElrV0g2VzEtQ01GS3ExenJ4VEs3ZHc?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 17 Aug 2026 08:46:00 GMT
- [台科大暑期材料營攜國際大廠引進AI、半導體實作模擬| 生活 - cna.com.tw](https://news.google.com/rss/articles/CBMiX0FVX3lxTFB6UE1RYTZvclRONXdmdTdzdUlhbU53b1NCRkxHek5URGs3S3I4ZU5yYmtFSXFSYUVxanY5ejBBNkFzY0tDVDA3bDBPNGRTME9mN2lLcmk3MzZ2OU85VFdR?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 17 Aug 2026 05:49:00 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：緯穎、富世達 認購火 | 權證特區 | 證券 - 經濟日報；液冷散熱 2026 滲透率飆破五成！台廠受惠 奇鋐、雙鴻、健策卡位 - 緯來新聞網；這散熱大廠吃AI四大平台　目標價至4005元 - 鏡週刊Mirror Media

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.51 | +8.25% | +13.92% | 3,150.00 | 3,235.00 | -2.63% | 同向 | 75.13 | 41.99 | 18.59B TWD / 57.39% | 2026-08-01 |
| 6669 緯穎 | 新聞直接提及 | +0.42 | +9.88% | +10.15% | 6,620.00 | 6,620.00 | 0.00% | 同向 | 313.51 | 21.22 | 117.69B TWD / 39.23% | 2026-08-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐、散熱」，共 2 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：受惠。
- 6669：新聞直接提及「緯穎」，共 1 篇新聞命中。

### 主要來源

- [緯穎、富世達 認購火 | 權證特區 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBCdHR0WWh0Njh6X3FUd3dESWQ1Zm9yZENCb1I3cE1PcE1fZmgxamdKcTNwS2JsZE5TZTM0M1lKZjYxYVNyQWxIb3lkc2tsTjNseUthaXlFeUwyZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 17 Aug 2026 16:16:37 GMT
- [液冷散熱 2026 滲透率飆破五成！台廠受惠 奇鋐、雙鴻、健策卡位 - 緯來新聞網](https://news.google.com/rss/articles/CBMihgFBVV95cUxOOWNBNzFxYnhMSllXRUQxWFNJMEF4SUQxWHU2czBxcTNWQ1VoSUpFcXhQejdNd1FhOHBHd3FhOG5WM1V3NDluT2lpTVJXLUhabXFpczdRbWlDRnFMUDIzeHR0VGpQX0JIemxRQVgzZFE4ZlJTV3duX1ZoNVpvcnktMVBjV0lCQQ?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 17 Aug 2026 10:55:00 GMT
- [這散熱大廠吃AI四大平台　目標價至4005元 - 鏡週刊Mirror Media](https://news.google.com/rss/articles/CBMiYkFVX3lxTE1GRVJ6VlVQMjRWQWROT3FTSmZJOUlCWmtXRGp5MHRXTURfbHNUUUpQNHo3cWlHY09LSUh0VEdKSVdKbmZxcUpqYnctSmdwSGRGQUh3TXoyblB3Ykp3TnYxWWVR0gFiQVVfeXFMTUZFUnpWVVAyNFZBZE5PcVNKZkk5SUJaa1dEankwdFdNRF9sc1RRSlA0ejdxaUdjT0tJSHRUR0pJV0puZnFxSmpidy1KZ3BIZEZBSHdNejJuUHdiSndOdjFZZVE?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 16 Aug 2026 17:00:00 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Veteran Tech Investor Dan Niles: Agentic AI Wave to Last at Least Another Year, Intel Is Top Chip Pick - TradingKey；SanDisk Stock Price Forecast: Surging Past $1,700 Mark, Will Memory Frenzy Push SNDK to New Record? - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 103.49 | 114.68 | -9.76% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 1,011.75 | 1,011.75 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | +32.92% | +44.34% | 1,786.85 | 2,335.00 | -23.48% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MU：新聞直接提及「memory」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。

### 主要來源

- [Veteran Tech Investor Dan Niles: Agentic AI Wave to Last at Least Another Year, Intel Is Top Chip Pick - TradingKey](https://news.google.com/rss/articles/CBMizAFBVV95cUxPYUpMdFBOWElJbW5uTzV2VXl6bFJ6ckR6ZzI4MVA2VmJCeUM1QlZNYlYtV2hSazJJRTg0MEVFSG80NTdUaFVEZlhoamV3RER4NkxOSWhPSml6SGROSEg2Y19QSVY4d2hIT2VWZEFURGdhRFZIN2lFbXV6Qnd4YlJ5em40RFNITzYtV0lvQ0tDTzlNaUFFRjVHUzZ5S1FEb3FOM2hBdGEwc0k1TUZ0ZVVFVHVsdEplX3JPZTBsSmdpRHpmNkY2T0VBM3lZYmg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 17 Aug 2026 08:12:53 GMT
- [SanDisk Stock Price Forecast: Surging Past $1,700 Mark, Will Memory Frenzy Push SNDK to New Record? - TradingKey](https://news.google.com/rss/articles/CBMisgFBVV95cUxOVm4zTXpIM2wtanVVcnd5bThlcjk3MXRLYjM5Mi1wQzNVc3NfTUxEMlViNGVhT0ZieGJlVDUxTmwzZFQtZElUajFwaDdnWkVfZU9pNVRkWFVDSjA1bU16UXA3RkJFcERtMFZKbVhmNUp2QldWQk9vMUU3V29iUHVGWncwOEFfaWJxYUlTbmlaWXRCNFgzd2dwUkdDS2xZTGlzeG9DZk95OVdZZDQ4YXNWMUpn?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 17 Aug 2026 07:12:51 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：AI Wave Show 觀後感：地端 AI 萌芽中 - TechNews 科技新報；Anthropic 執行長剖析 AI 反彈，關鍵在美國大眾失去信任 - TechNews 科技新報；Google 傳聯手 AMD 打造第十代 TPU，整合 CPU 核心攻強化學習 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AMD 超微 | 新聞直接提及 | 0.00 | N/A | N/A | 506.00 | 516.10 | -1.96% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 103.49 | 114.68 | -9.76% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +12.45% | +12.75% | 225.01 | 225.16 | -0.07% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -0.62% | +0.84% | 2,400.00 | 2,425.00 | -1.03% | 不適用 | 86.28 | 27.82 | 467.58B TWD / 44.69% | 2026-08-01 |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +22.31% | -5.20% | 480.35 | 506.69 | -5.20% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | +3.89% | -5.99% | 392.43 | 446.77 | -12.16% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | -0.97% | -2.38% | 615.00 | 680.00 | -9.56% | 不適用 | 13.92 | 44.50 | 73.78B TWD / 43.15% | 2026-08-01 |
| 2454 聯發科 | 產業/供應鏈推估 | 0.00 | +0.87% | +2.27% | 4,050.00 | 4,310.00 | -6.03% | 不適用 | 60.69 | 66.89 | 48.47B TWD / 12.16% | 2026-08-01 |

關聯理由（前 3）：
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 5 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AI Wave Show 觀後感：地端 AI 萌芽中 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiXkFVX3lxTE4yR09kN1Z3WGQ0VW9nYlJwcVdYdXZaZERGWnRlbm9vbDhiZHRrVzB2MUw3UkxVMGxwYV90YkdhOHh3emZrQVhta1FxUC1jbEVKVXMtR3drdzR5bEd4UEE?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 17 Aug 2026 00:00:58 GMT
- [Anthropic 執行長剖析 AI 反彈，關鍵在美國大眾失去信任 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiogFBVV95cUxPQnFpaEVXaWxKTHJGSG5kVkR2Umh1Z2l0bFB3MWdabkY5QUNWZERCS3BMdVRfQzA5OXZ1Uzh6c2c3Y3pwdzZxVTM0RnNwc1p5LWRfT2Q2UFl2S2ZBbzd0RnJWVDdFa1I1YjlvaEI5UnJKMENEWFpwNWlGU1piODZTajdwb2NtZmNwMjF5TkVuM2x2bjNqMDNNS3RTbTVURHNNM0E?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 17 Aug 2026 07:04:47 GMT
- [Google 傳聯手 AMD 打造第十代 TPU，整合 CPU 核心攻強化學習 - TechNews 科技新報](https://news.google.com/rss/articles/CBMikgFBVV95cUxORW5pajg2Vmlvb3d4VjM5dHl5LTFPNDBQc3Jha0JiSkxIN2E2NGJGa0lFd0ItRHpBZzMtMFhIOWVnal9zcEJtQWxNYmVZTFhHUXF3NXBMamtfTUdiUzFGTVowVy16ODM2Z0dHazZPSWhEU3d4UnpYLUkyRFZFbExXTmxFMUU4WmM2SXdLX2dvVVZzdw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 17 Aug 2026 00:33:22 GMT

## 新興題材：UlmltETmgV

摘要：新興題材：UlmltETmgV 相關新聞集中在：The Memory Selloff - An Institutional Audit Electric Bicycle (UlmltETmgV) - Mshale

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 1,011.75 | 1,011.75 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「memory」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [The Memory Selloff - An Institutional Audit Electric Bicycle (UlmltETmgV) - Mshale](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9jSmc0Q0pDQVFLeXdHb3NJM0lOLS1JTFYtZXpSaTY4dWZNbFlYQllHa1YteHQ2WGVmSGNQc1I0NWtWd0RLdmg0c29BeVR0TVdoX2c0X3QxRm9IQmc?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 17 Aug 2026 14:04:04 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股將上演股王爭霸戰 川湖與信驊股價拉近成話題 - 經濟日報；台股基本面穩健 但評價面已反映樂觀預期 - 經濟日報；8月台股期指漲76點 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股將上演股王爭霸戰 川湖與信驊股價拉近成話題 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9DZnFaR2dEM3JSWHpvakZFb0xPY2RBbkpDXzJqYnNOa25YMEM0VXRVRENSdTlvYnhOWmxqd21CTGJYdHIxNndiZkFfRVM3OFkxMWlRZ1FCVkxqUdIBX0FVX3lxTE9mX0lzNXJSTVZ0UlZocU44eXJJMVdMMFJ4ZnR2LVJiWl9uVThEdm1HczkwUmEtTTlyZXNOR01qVEZrNG5leUJzWEdnc1RqX1JyNUhhMjlZV2V5NmhZcnFJ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 16 Aug 2026 09:00:00 GMT
- [台股基本面穩健 但評價面已反映樂觀預期 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9jeTlqTXpkY1Nab3F2WGk4LWxFcFc2Ylk3bHR3TUlCMjUyWXFKVnA2blNhSE0yX0NiSWhSZ3VXNmRNckR6UWpJdkZRZGhGX19NcXh5SFpSYy1mZ9IBX0FVX3lxTE1BOTRRd2V4SWN2M0RKcjJpNXBJVWtHc2tuRmpPdHNicnl1S3ByZy1DWlhvR3pzT3NBcU56dU9fZ3RpNVRSTVRYNTlKSXJlWXo3Ml9NWGtmaGk0TzRveFJv?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 17 Aug 2026 11:20:58 GMT
- [8月台股期指漲76點 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxNRnpQR3VSdnpZelF2X0tJZjhRSG95bmVPM0dCQUFSZDNGblp6T2c5eS1yckJJTGsyR09EdmtFUnAyODJoU3E4MVBEM21Ba2NkMFg4MEl5RGdXaTJZRC1iNDNLMmN5RjVZbV9LS21KQk9TbW02QmlldzRtcjlLVU9uQ9IBX0FVX3lxTE92YXhTbnpkNmQ2OEhmUlJaMEhXZVcydUlkT184VWx3akpjS0FfUjF5bW5jSzcxZHpULWJ1RXo5ZE9pcEVNLV9VcjFoZFBHa01mdUFBb203ZjFVbkhlUXJV?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 17 Aug 2026 06:21:25 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
