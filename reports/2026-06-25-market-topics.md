# 每日股市熱門話題分析 - 2026-06-25

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜負向｜熱度 17｜市場確認 53.99｜同向 1/2
2. **利率與成長股估值**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
3. **AI 伺服器與資料中心**｜中性｜熱度 7｜市場確認 N/A｜同向 0/0
4. **先進封裝與 CoPoS**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
5. **半導體與晶片供應鏈**｜中性｜熱度 5｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.10（樣本 5）
- 5日相關係數：-0.21（樣本 5）
- 同向比例：1/5

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 53.99 | 1/2 | 0 | +6.33% | -4.22% |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | N/A | 0/0 | 0 | N/A | N/A |
| 先進封裝與 CoPoS | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：OpenAI | 0.00 | 0/3 | 2 | -5.42% | -2.91% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-06-11 | -0.05 | -0.08 | +14.29% | 7 |
| 2026-06-13 | 0.87 | 0.98 | +100.00% | 4 |
| 2026-06-14 | 0.82 | 0.98 | +100.00% | 3 |
| 2026-06-15 | 0.87 | 0.56 | +42.86% | 7 |
| 2026-06-16 | 0.39 | 0.50 | +76.92% | 13 |
| 2026-06-17 | 0.17 | 0.47 | +62.50% | 8 |
| 2026-06-18 | -0.41 | -0.41 | +42.86% | 7 |
| 2026-06-19 | 0.06 | -0.04 | +57.14% | 7 |
| 2026-06-20 | 0.29 | 0.21 | +63.16% | 19 |
| 2026-06-21 | -0.01 | 0.32 | +55.56% | 18 |
| 2026-06-22 | -0.87 | -0.87 | +100.00% | 3 |
| 2026-06-23 | 0.38 | 0.01 | +62.50% | 8 |
| 2026-06-24 | -0.38 | -0.11 | +25.00% | 12 |
| 2026-06-25 | 0.10 | -0.21 | +20.00% | 5 |

## 歷史回測摘要

- 回測日期：2026-06-25
- 近5日 3日相關：0.01
- 近5日 5日相關：0.00
- 同向比例：+42.86%
- 權重狀態：未調整

- 方向準確度：+42.86%
- 信心排序準確度：0.01
- 診斷：低相關

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

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：AI Chip Stocks Stage Rebound: Nvidia, AMD Lead Recovery Ahead of Micron Earnings Shock - TradingView；The NASDAQ Dropped 3% as Micron, Intel, and AMD Tumble, but One Tech Name Is Bucking the Trend - 24/7 Wall St.；AI, chip stocks slowly recover after Tuesday's onslaught ahead of Micron's results - Seeking Alpha

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | -0.65 | N/A | N/A | 1,048.51 | 1,051.77 | -0.31% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.56 | N/A | N/A | 519.74 | 519.85 | -0.02% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.56 | -12.37% | -3.87% | 1,914.46 | 2,273.73 | -15.80% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | -0.38 | -0.29% | +12.31% | 199.00 | 211.14 | -5.75% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | -0.48 | N/A | N/A | 131.65 | 132.28 | -0.48% | N/A | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、memory」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 1 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。

### 主要來源

- [AI Chip Stocks Stage Rebound: Nvidia, AMD Lead Recovery Ahead of Micron Earnings Shock - TradingView](https://news.google.com/rss/articles/CBMi3AFBVV95cUxNX3R0SldMUHVoZE1DdFdXNE8xZnJyUVNVSnFIRWxFcUdCVDc4WUhlN2dhOVJRNlZpdGJWX1ROa2pacy13TUR4MjNBdDNEVDUzWUZiSTFJWE41b19CdzBMUGFwU3dvT19uNC1mZUVxM01oVGtGcENFUWNYRTIyc1Bxa2FVMVBUWVZFeFgwblN2Ty1aQkFBVVJZd1RwZXBmVGdmYTVYYjRlejRocERxS3BHa2FIUnVRT2pnVnUyelBiNjk1dkExX3ptc3pNc1d0TEhJNHhmOG1nYUNJcjBD?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 24 Jun 2026 19:34:27 GMT
- [The NASDAQ Dropped 3% as Micron, Intel, and AMD Tumble, but One Tech Name Is Bucking the Trend - 24/7 Wall St.](https://news.google.com/rss/articles/CBMizwFBVV95cUxOWEdDU2VZemJDS2VqbXJPd2ZZTDE0d2IwQmRvRGRRN2RiWlU2LVgteFYwSkhndTNBWlZoRFJlWVlDblA0TG5BbUgyUklfQ0xMeW8yVE1vU2tTdkl2WVcxMEd5TjBJaVVUOF9NdXNYRUpyN2dRNlhaSmtEVGRiRnN5cGhadXhnNkhNWWxHTU9Ham8zQmFTWlBYLWM4LUh5TWtSVDhZZFpjZENxeHMzXzNiUDJZWlRlQ0pOa2V4c2VTOWRPY3FiTjBVc3dhV21aY2c?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 24 Jun 2026 16:54:48 GMT
- [AI, chip stocks slowly recover after Tuesday's onslaught ahead of Micron's results - Seeking Alpha](https://news.google.com/rss/articles/CBMiuAFBVV95cUxQUXN1dF9UU1lMZzJxSHQ0OFZuTU4zNnAySzZqUzdubWZUalllWXhDYno4N1gyeW1qS3BqdE9wSTM0RndFYi1Udi1yY1NsSnU0eHF0RWZEaC1nSVRyZFFFckp1c0FZbkRCc3F6c1lSTVNYcU1sOUI3akZnblpYQ3l5UndwYWlUVUN2cFgtSm41dm1UeHo2RzhDXzZtZG1CY3lnRURGbFp3NzBkWHJvaFRndVNDbTQ0MFM1?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 24 Jun 2026 15:52:54 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：台股陷「估值卸妝」陰霾 外資瘋狂提款 賣超1,774億元史上最大量 - 經濟日報；台股陷「估值卸妝」陰霾 外資瘋狂提款 賣超1,774億元史上最大量 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | -6.95% | -27.87% | 365.46 | 506.69 | -27.87% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [台股陷「估值卸妝」陰霾 外資瘋狂提款 賣超1,774億元史上最大量 - 經濟日報](https://news.google.com/rss/articles/CBMikAFBVV95cUxONC1veHNFSDN2Z0p2UWtlbVR5WHpvaUluQWQ1WjQxcF9PaXZ2RTFzRHMtOFFJRWNwaFI0OG1aNC16SmoyeHNPdUR0eGZub3JfY2hFczZTQW5fT28wMENIOHVaMHJGY3Z6UmtBVGw4aTBJd1R3NDdMUDU1czdNbm90LWliLWpGb2N0eTZIUkswYk_SAV9BVV95cUxPSnlOQm9ZbV92UmtzYWJCOFROVjBTcFVtcGt3dlFCNWs1NXY5aWdWX04yRDhEd0c1S1otd3ptZGRILU9RV3pUenZOX1cwc3pOa0dMeXZNYkgyMC10RXJOVQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 23 Jun 2026 09:00:00 GMT
- [台股陷「估值卸妝」陰霾 外資瘋狂提款 賣超1,774億元史上最大量 - 經濟日報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9KeU5Cb1ltX3ZSa3NhYkI4VE5WMFNwVW1wa3d2UUI1azU1djlpZ1ZfTjJEOER3RzVLWi13em1kZEgtT1FXelR6dk5fVzBzek5rR0x5dk1iSDIwLXRFck5V0gFfQVVfeXFMT0p5TkJvWW1fdlJrc2FiQjhUTlYwU3BVbXBrd3ZRQjVrNTV2OWlnVl9OMkQ4RHdHNUtaLXd6bWRkSC1PUVd6VHp2Tl9XMHN6TmtHTHl2TWJIMjAtdEVyTlU?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 24 Jun 2026 17:48:30 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel (NASDAQ:INTC) keeps foundry premium even after AI chip selloff, trading data shows - TechStock²；美風投家 2030 年五大 AI 預言：台積電與 ASML 不再能壟斷晶圓代工市場 - TechNews 科技新報；AI 算力狂飆下的隱形危機，中國 80% 綠電資料中心為何難以實現？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 131.65 | 132.28 | -0.48% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | 0.00 | -0.83% | -0.42% | 2,390.00 | 2,490.00 | -4.02% | 不適用 | 74.39 | N/A | 416.98B TWD / 30.09% | 2026-06-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -0.29% | +12.31% | 199.00 | 211.14 | -5.75% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 519.74 | 519.85 | -0.02% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | -6.95% | -27.87% | 365.46 | 506.69 | -27.87% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -8.47% | +19.57% | 382.07 | 446.77 | -14.48% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | +6.53% | +10.30% | 653.00 | 662.00 | -1.36% | 不適用 | 10.86 | N/A | 63.03B TWD / 28.57% | 2026-06-01 |
| 2454 聯發科 | 產業/供應鏈推估 | 0.00 | -2.39% | -6.03% | 4,285.00 | 4,535.00 | -5.51% | 不適用 | 62.91 | N/A | 47.43B TWD / 4.99% | 2026-06-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 同時符合主題標籤：AI, advanced packaging, CoWoS, AI server。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel (NASDAQ:INTC) keeps foundry premium even after AI chip selloff, trading data shows - TechStock²](https://news.google.com/rss/articles/CBMiqAFBVV95cUxOaDlLSzJiY2V4TWlEVVFQQUppQzV2aXYzZVBNMUlTVktHdjY0NXR1ZFdkUXpudWJyeXlfZi0zUld0eHlDd08xNkRjMDVOS2FRR0Z2OFl4NExZaGZUVlh3LXdwTUdtdkFPbXhoeHA5Tkg3VS1tRXBERDBWYVJyVGNpaUFZS183aXVfNFhFNGthbWF1RkJIZ0lPU0pwQTRZbFAyODlyY3RHUWo?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 24 Jun 2026 08:27:00 GMT
- [美風投家 2030 年五大 AI 預言：台積電與 ASML 不再能壟斷晶圓代工市場 - TechNews 科技新報](https://news.google.com/rss/articles/CBMie0FVX3lxTE1DaF9hRWJ5Zy03enkzOVh3bHV2b01vYnZ4QW43SjdFY0RkZS1YWDlWT0xseFBRd29HRzhUMV9DaDFJdkkxVUI3ZktlYTRuQjZkamMyblJmejRFdVptbm56SUhuUmI0NUpQSVhYa3VFWlpCLWxjUWI3TmU2OA?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 23 Jun 2026 23:31:23 GMT
- [AI 算力狂飆下的隱形危機，中國 80% 綠電資料中心為何難以實現？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMitwFBVV95cUxNOWJjM05pZDVFWjluTXZFcmE4dG1zc29CdXoxdVRDVWw3QnkwZTVzajh2LU1FaHdXNEY2UjJQTVgyeC1qeDA2ZHlQdkNTOGRjSUw3YTdHSUV5TjBDMVRSNk5pNUZPNUZXY1A0NXlkVFRkWHMycEo3azFXOE5iRnhZTDdST21NSmo3V1l6YjRtRW9oVGRxV21jczY5MEYtS2Z3cjNCdWhGQ05jeDkyYV94OVVyLXhjTGc?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 24 Jun 2026 00:21:32 GMT

## 先進封裝與 CoPoS

摘要：先進封裝與 CoPoS 相關新聞集中在：AI 加持 30 年 FOPLP／玻璃基板市場規模估飆增逾 11 倍 - TechNews 科技新報；台積電先進封裝廠五地開花，傳評估中科二林設廠未獲證實 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | 0.00 | -0.83% | -0.42% | 2,390.00 | 2,490.00 | -4.02% | 不適用 | 74.39 | N/A | 416.98B TWD / 30.09% | 2026-06-01 |
| 3711 日月光投控 | 新聞直接提及 | 0.00 | +6.53% | +10.30% | 653.00 | 662.00 | -1.36% | 不適用 | 10.86 | N/A | 63.03B TWD / 28.57% | 2026-06-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 同時符合主題標籤：advanced packaging, CoWoS, CoPoS, FOPLP。
- 3711：新聞直接提及「FOPLP」，共 1 篇新聞命中。 同時符合主題標籤：advanced packaging, CoPoS, FOPLP, panel-level packaging。

### 主要來源

- [AI 加持 30 年 FOPLP／玻璃基板市場規模估飆增逾 11 倍 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiowFBVV95cUxPSHVtZHF3YUwyVko5emp3LUxaMFRaay16QTdtNzUwNmhMRzFHVE00WWw1MUJUenp5bnM1bGVRQm9BSGYxbnE4bVJNcER3YmItQUZKSUJuRlJtOVktTy15T3BnVWZZTHphMGJiR1NmMUpmRldWVkFreTdTTHZYMWVSQ05vSzl1eTI0NWwta3piZWhTMU5MWkhWanByaEdkczNHYUdR?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 24 Jun 2026 03:32:20 GMT
- [台積電先進封裝廠五地開花，傳評估中科二林設廠未獲證實 - TechNews 科技新報](https://news.google.com/rss/articles/CBMirwFBVV95cUxQX0UxTEpEWGdMbkdpMDNCX0NxV1BLWnJ5RDR5LW4wUURCMHBFQ1JqZjF2UVIxdVJxNG5hRkNvUWJmdlE5aTduVllYMk13bVc5Tks1ZGw5TVpYWHBfdGExX0dNSmppd0g2NWFFNG9MYzhmMTZuckZrdlZkLWlRVTc0MlhtbC1HQ19xcmEtZ2xNQmRnTTZPT3FDRm5PNnNuODN2MHVZdXkxZkNVWXBtS3hv?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 23 Jun 2026 06:04:03 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel (NASDAQ:INTC) keeps foundry premium even after AI chip selloff, trading data shows - TechStock²；Intel (INTC) And UMC Team Up On 12nm And 3nm Chip Development - simplywall.st；晶片股拋售及技術面修正台股面臨高槓桿與空單考驗| 證券 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 131.65 | 132.28 | -0.48% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | 0.00 | -0.83% | -0.42% | 2,390.00 | 2,490.00 | -4.02% | 不適用 | 74.39 | N/A | 416.98B TWD / 30.09% | 2026-06-01 |
| 2303 聯電 | 新聞直接提及 | 0.00 | +22.34% | +26.24% | 178.00 | 178.00 | 0.00% | 不適用 | 4.00 | N/A | 22.94B TWD / 17.78% | 2026-06-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -0.29% | +12.31% | 199.00 | 211.14 | -5.75% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 519.74 | 519.85 | -0.02% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 1,048.51 | 1,051.77 | -0.31% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -12.37% | -3.87% | 1,914.46 | 2,273.73 | -15.80% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -8.47% | +19.57% | 382.07 | 446.77 | -14.48% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip, foundry。
- 2303：新聞直接提及「UMC」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, foundry, chip。

### 主要來源

- [Intel (NASDAQ:INTC) keeps foundry premium even after AI chip selloff, trading data shows - TechStock²](https://news.google.com/rss/articles/CBMiqAFBVV95cUxOaDlLSzJiY2V4TWlEVVFQQUppQzV2aXYzZVBNMUlTVktHdjY0NXR1ZFdkUXpudWJyeXlfZi0zUld0eHlDd08xNkRjMDVOS2FRR0Z2OFl4NExZaGZUVlh3LXdwTUdtdkFPbXhoeHA5Tkg3VS1tRXBERDBWYVJyVGNpaUFZS183aXVfNFhFNGthbWF1RkJIZ0lPU0pwQTRZbFAyODlyY3RHUWo?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 24 Jun 2026 08:27:00 GMT
- [Intel (INTC) And UMC Team Up On 12nm And 3nm Chip Development - simplywall.st](https://news.google.com/rss/articles/CBMiyAFBVV95cUxQOUJmRXNuVjF6OEIyNDlneTlqa1R5QUxmZGhSV0xRbVlkRG40RE53VzBIcVFzcV9vMk1oZllhTFdmY3RsWWFUZm9RSXdZMGlPTVh5ek9BS3JFWGNtVEhOZ3JnSXdZYzkyYUY2MDRQU0RTWFlmazY2cFItMl9BbjYtckpDcnotRUxnZm9sa2w1V2s2OS1UdnVObm45M0pfLXp4azZ6QjBEa2hmYW1ZUjZlOGtsYncxZnQyVDFzNk9FdVJnVk9nVUpBQdIBzgFBVV95cUxObEtFbTVrSm4ycFI5a3NpYk5JeVl1Z3hSRUFCOUh3V3RUUzRGbzhPMndhM0xoOTR4cTBwUEJCazE4VUdWWXdkLS1rdjBZMEZETEJhSG1oMzdvcDFycVB3NkU3d2tXbFlLbmkzYUwxZnBUSGwySjRaN1dDLTRqUTFBLU04WEg2Uk9JM2lxYXNSbkl1YmptX21KamZkY3h1SzlGeWoyZXNWTzl5MXRPbjJiVklBSzlhMHhERHhiTGxxbmRIQWIzRFZRVGJPb1Fpdw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 23 Jun 2026 13:44:18 GMT
- [晶片股拋售及技術面修正台股面臨高槓桿與空單考驗| 證券 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE4ydVI3SUdTR3BJRS0tZGFKdkFiTGxHVy1reUNMdWdlNkQ3VnFHa1lZYkhLQVNnS2FyRWpNdzI2MlNDclV0ZmVkX01Gd3BoeHpnbGxJM3FJdGFHbWp1TGc?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 24 Jun 2026 10:47:00 GMT

## 新興題材：OpenAI

摘要：新興題材：OpenAI 相關新聞集中在：OpenAI 首款 AI 推理晶片「Jalapeño」亮相，攜手博通設計、台積電生產 - TechNews 科技新報；OpenAI unveils custom chip it designed with Broadcom to boost its AI infrastructure - Reuters

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 新聞直接提及 | +0.28 | -6.95% | -27.87% | 365.46 | 506.69 | -27.87% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | +0.28 | -8.47% | +19.57% | 382.07 | 446.77 | -14.48% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | +0.36 | -0.83% | -0.42% | 2,390.00 | 2,490.00 | -4.02% | 未明確 | 74.39 | N/A | 416.98B TWD / 30.09% | 2026-06-01 |

關聯理由（前 3）：
- MSFT：新聞直接提及「OpenAI」，共 2 篇新聞命中。 方向判斷命中詞：boost。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AVGO：新聞直接提及「博通、Broadcom」，共 2 篇新聞命中。 方向判斷命中詞：boost。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。

### 主要來源

- [OpenAI 首款 AI 推理晶片「Jalapeño」亮相，攜手博通設計、台積電生產 - TechNews 科技新報](https://news.google.com/rss/articles/CBMikAFBVV95cUxPdTdvM1BCUXZtcEhiMzd6dnZqY1pYV2pRMzl0cmlzV09sR0RLZTk0Nk02WGFLY0NYNFJzb1ZqS05PZjRIM0hxeHdwdzJKUGhQTnFIQWw2UjVDWWpIVWNQRzRkR01HRTBjX3JNQnhvZW9MNmFld21KSE14QThGOEZuSEVGeGNiV3pJaENvVmdEU08?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 24 Jun 2026 16:32:40 GMT
- [OpenAI unveils custom chip it designed with Broadcom to boost its AI infrastructure - Reuters](https://news.google.com/rss/articles/CBMi0AFBVV95cUxQdThteGtwZVZweXpUZTNQR0djS0ViNGhlZjNacUlpaG5KZ2M2SGdLckxXcEV5T3Z5UDhhRjJ5OUh5LTAxQThQVjNGUG1xWGIwM1VLeUNxNjY2N0RfbnFySTY1d0txYjdlNUVWY1lFbFZhRHcyTV9XRWFkRWZjdzM1Mk1QUWVhTmRRYi1IVklHdlJJeThoMUloTlNFTm4yQ29YTUFXRDUtZjZOeVh2cThIazdhUWd1bjdKcXJsamNqN01VR3RMZUtvLXI3SXpvNGV6?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 24 Jun 2026 13:22:09 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：個股動態報導內容-BDC854D7-6E03-4E79-92FD-06E194DB3D63 - 5850web.moneydj.com；台股賣壓出籠 多頭士氣受挫 千金股淪重災區降至51檔 - 經濟日報；台股賣壓出籠 多頭士氣受挫 千金股淪重災區降至51檔 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-BDC854D7-6E03-4E79-92FD-06E194DB3D63 - 5850web.moneydj.com](https://news.google.com/rss/articles/CBMikgFBVV95cUxQSTlNcHVaTEp2SVRHbEMwdEpZNDNRQzItSGtiR0ZoU1Z3ZFFoQzFOakFmWWJUTWJwbHhoeElDa1ppeDlvbTZRV3FGSUl5UzFzTDBGLXdQYi1IVU50QWxOa0l4NG5UVXZjUlhybDhrZGZST2p5djhEUkJ1WUljY3ZDMEd5eGxQMGdUV2RZb05tSVYxQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 24 Jun 2026 11:28:48 GMT
- [台股賣壓出籠 多頭士氣受挫 千金股淪重災區降至51檔 - 經濟日報](https://news.google.com/rss/articles/CBMidEFVX3lxTE1EYVlUUnJ0VmVsZFRKQXhkX1E5QlR2MWJMdUtYUmF5Nl90QkN6dVEwNnNRWlJkSWJtZUl0RVVnSzUwa0VYSFFVLVVDRS04WGNJZ3F5bm9BWEJqVXFCd1ZHcjFROExpd19YTWQxNzhXamQ1d0Ns0gFfQVVfeXFMT1czczdPSVNKX3ZGTmJJY1M1X0lFWDd3enFSVUUzSUlmT3hXc01ZR1FnN1NXMS0wbWEwS1JveDk2TThUdGN4eXdLRy1ZYXRfVFBWS1l0ZTluSXNMVl9TbFk?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 23 Jun 2026 09:00:00 GMT
- [台股賣壓出籠 多頭士氣受挫 千金股淪重災區降至51檔 - 經濟日報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9XM3M3T0lTSl92Rk5iSWNTNV9JRVg3d3pxUlVFM0lJZk94V3NNWUdRZzdTVzEtMG1hMEtSb3g5Nk04VHRjeHl3S0ctWWF0X1RQVktZdGU5bklzTFZfU2xZ0gFfQVVfeXFMT1czczdPSVNKX3ZGTmJJY1M1X0lFWDd3enFSVUUzSUlmT3hXc01ZR1FnN1NXMS0wbWEwS1JveDk2TThUdGN4eXdLRy1ZYXRfVFBWS1l0ZTluSXNMVl9TbFk?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 24 Jun 2026 17:16:19 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》外資天量賣超！重摔1057點、險守46K-新聞內容-基金 - MoneyDJ；個股動態報導內容-F443159C-A70E-4B38-A658-10F8EC07EC46 - MoneyDJ；個股動態報導內容-418C8C78-0A29-4566-B81C-FAE360CFFD76 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》外資天量賣超！重摔1057點、險守46K-新聞內容-基金 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxPYTlIQjlvMmptTWQzMlNxNWxlMjBhVUZULWdobldfZnBQSGlQRzRadDc4VnhYMnI3Y2RYV1BmT2VHV2tOR1hfQXlJNS1lckNJaFAwSUk3R0FuYmVBZ0h6a1lnYzlDZXduQXZfS1B0Q1ZBOEEzNHNUeEdrc29IdVJjUGU3dDFMVk1kRlloMHpuZXI?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 24 Jun 2026 08:03:00 GMT
- [個股動態報導內容-F443159C-A70E-4B38-A658-10F8EC07EC46 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxPREpNZVhTX0FkV0dRR0VVS21mS1U4UHM5bWFlT3RqdTB2UjVRd3Q1ZEN1ckh5d3lzbXJkNVFRUV82QmxNOGxOVW84X0doaTREZWJSWUoxVVlyTkFsUlpYVktuNm90ZFJhS0lieEJyVnFtNzhZWHVhQmhqQW9wZmlVWTlKTVBQVkRlVTdjV1Vxb202MmZ4?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 24 Jun 2026 10:11:23 GMT
- [個股動態報導內容-418C8C78-0A29-4566-B81C-FAE360CFFD76 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxQT25mblF3Wk40R2V2Y2pzMUlNMlhkREppb3N3dnB0bFNpVVBMWVdZVFpfaVE3aHN4LXctTG9ETGdxUGlKQUFBQ21aejBEMWpzb19aZ0hPZUdIaTk3Z0t3VU9nbWhqRktQV0Y3aFdwQlJ0SzVMbWNDTXNMUENhSXdLb0hmTXhFT2NwdVdRTXkwVUdhUnRO?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 24 Jun 2026 11:34:05 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
- TWSE PER/PBR 抓取失敗：Expecting value: line 1 column 1 (char 0)
