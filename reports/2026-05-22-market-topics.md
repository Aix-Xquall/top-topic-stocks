# 每日股市熱門話題分析 - 2026-05-22

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜正向｜熱度 3｜市場確認 100.00｜同向 1/1
2. **散熱與液冷供應鏈**｜正向｜熱度 2｜市場確認 100.00｜同向 2/2
3. **新興題材：StartupHub**｜正向｜熱度 1｜市場確認 100.00｜同向 1/1
4. **半導體與晶片供應鏈**｜負向｜熱度 11｜市場確認 0.00｜同向 0/5
5. **AI 伺服器與資料中心**｜負向｜熱度 14｜市場確認 0.00｜同向 1/6

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.05（樣本 15）
- 5日相關係數：-0.00（樣本 15）
- 同向比例：5/15

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 100.00 | 1/1 | 0 | +15.70% | +11.54% |
| 散熱與液冷供應鏈 | 100.00 | 2/2 | 0 | +14.70% | +6.25% |
| 新興題材：StartupHub | 100.00 | 1/1 | 0 | +25.87% | +14.85% |
| 半導體與晶片供應鏈 | 0.00 | 0/5 | 4 | -15.91% | -11.43% |
| AI 伺服器與資料中心 | 0.00 | 1/6 | 3 | -8.16% | -4.43% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：SpaceX | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 相關性偏弱；應提高同向價格確認權重，降低泛 AI、泛半導體等寬標籤推估權重。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-05-09 | 0.10 | 0.55 | +33.33% | 9 |
| 2026-05-10 | 0.45 | 0.55 | +75.00% | 8 |
| 2026-05-11 | -0.03 | 0.47 | +85.71% | 14 |
| 2026-05-12 | 0.00 | 0.42 | +78.57% | 14 |
| 2026-05-13 | -0.08 | 0.07 | +58.33% | 12 |
| 2026-05-14 | -0.29 | -0.20 | +50.00% | 6 |
| 2026-05-15 | -0.17 | -0.08 | +58.33% | 12 |
| 2026-05-16 | -0.12 | -0.69 | +33.33% | 12 |
| 2026-05-17 | 0.09 | -0.34 | +40.00% | 15 |
| 2026-05-18 | -0.01 | -0.17 | +33.33% | 9 |
| 2026-05-19 | 0.04 | -0.01 | +62.50% | 8 |
| 2026-05-20 | 0.36 | 0.35 | +28.57% | 7 |
| 2026-05-21 | 0.28 | 0.52 | +45.45% | 11 |
| 2026-05-22 | 0.05 | -0.00 | +33.33% | 15 |

## 歷史回測摘要

- 回測日期：2026-05-22
- 近5日 3日相關：-0.20
- 近5日 5日相關：-0.11
- 同向比例：+16.67%
- 權重狀態：未調整

- 方向準確度：+16.67%
- 信心排序準確度：-0.20
- 診斷：方向與信心皆需修正

調整原因：近 5 日有效樣本 6 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：SanDisk Soars 9%, Western Digital Rallies 5%, Micron Rises 3% as Memory Trade Reawakens - 24/7 Wall St.；How far can the Micron and SanDisk rally run? - MSN；Micron Technology Inc Stock (MU) Moved Up by 3.60% on May 21: What Investors Need To Know - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.76 | N/A | N/A | 762.10 | 762.10 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.75 | +15.70% | +11.54% | 1,542.24 | 1,562.34 | -1.29% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +25.87% | +14.85% | 219.51 | 223.47 | -1.77% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、MU」，共 3 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 2 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [SanDisk Soars 9%, Western Digital Rallies 5%, Micron Rises 3% as Memory Trade Reawakens - 24/7 Wall St.](https://news.google.com/rss/articles/CBMixAFBVV95cUxNZkhrZUMzSXFPODFuVFhtbUNjdGlNM0ZzdFZyYmtTY2JPQ1FENk9xZUhRSHpaNWpkOUdCazNzNDBoc1gyU0NXYk4xdEkxaE5FYVczSnZ4bkkxeUl1Y3dnOHpXcGdjOFpFYjdfVXo3dFhLa0gycURrUjBDMnFzN1dqZ0kxdjd0elVISk9WRXNUY2F6azNZbEI4VFRyV2ZRY2NWM1d1amx2UEtadFNZcWMzbGhqVk9IdlJZNTFVd0hwVWp4bWFO?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 21 May 2026 17:49:35 GMT
- [How far can the Micron and SanDisk rally run? - MSN](https://news.google.com/rss/articles/CBMimgFBVV95cUxOejBnM2dOaFVNSmZHSFhFUHRXNXJsRFlVZzI4ZWN1OWxIMEM4UlB2Q3phSGJ0OFBEZG9zcFBPUWdHeXVLRW5UZnphSlVRdmZVWEhVVlNaVi1ZMFU0RE5Wd2FZSWZ4MXlvelJYX1BMaW8wdXpkTE5KQWhXbGFxQmVuRmQ2Vm44UjRmS2pUZ0F5TlRqR3VCcWJJem1n?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 21 May 2026 15:14:43 GMT
- [Micron Technology Inc Stock (MU) Moved Up by 3.60% on May 21: What Investors Need To Know - TradingKey](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPZnVyQXplRmd6MlBoSkItX2dsRWJhX016bUVqX1FBRDRwTUtmanp6TEVYanNpZmFQS1hQemRhWnZqWlhYWktGLTlGQ3YxVUkxQTQtaTllTUZzUE5xZ1BrLWFjTlBqdHlFZExua1d3R0hXd1ZFemtHYm94TDFtOUxkOXBDNC1qTHpM?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 21 May 2026 14:15:31 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：輝達新一代 AI 平台 Vera Rubin 報到 電源、散熱鏈含金量大增 - 經濟日報；【最新消息】奇鋐Q1 EPS 20元亮眼題材延燒，「10檔散熱概念股」強勢上攻！ - CMoney投資網誌

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.67 | +3.53% | -2.35% | 2,495.00 | 2,835.00 | -11.99% | 同向 | 61.06 | 41.00 | 15.63B TWD / 71.62% | 2026-05-01 |
| NVDA 輝達 | 新聞直接提及 | +0.56 | +25.87% | +14.85% | 219.51 | 223.47 | -1.77% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱、奇鋐」，共 2 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：大增。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：大增。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [輝達新一代 AI 平台 Vera Rubin 報到 電源、散熱鏈含金量大增 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE16LXJSNWVzS1hIQXlmd3lNWmVwXzdTQmhpcjhMTVpIenhHU3I2Tk5QaXVBc0hyZVo2em83VE95OUl1UVlwMUZUN0ZzM1hjbnNLb252WlFXREVYd9IBX0FVX3lxTFBuaVRLMy1fQno0VWxmS2I4bmlxdWVsWXJPN3Z0YXZ6OE94R2hYMjVuT0FWaTktVWF4eVFsY2t6bjdQbzF0R0tOdkxESXFLNTVGQmROZXRGRHppdEh5S2xj?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 21 May 2026 03:00:00 GMT
- [【最新消息】奇鋐Q1 EPS 20元亮眼題材延燒，「10檔散熱概念股」強勢上攻！ - CMoney投資網誌](https://news.google.com/rss/articles/CBMifkFVX3lxTE5leWRlX3BVMWE0Z3dlLWJfX0VMamhrQ0cyeUxCeWVnTTZJZkU5WUQzYk55WEg5QTBGOVZhaXBnWVF3RlJOczJQTmljNjliOXk4R25XdFh1NGNIZnVzN2RJZUUtUmU0bW1mZHBqemNVQkZQWmFjVEViVGdZTUUyUQ?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 21 May 2026 07:08:41 GMT

## 新興題材：StartupHub

摘要：新興題材：StartupHub 相關新聞集中在：Arm Holdings surges 15% on AGI CPU upgrade; Intel and AMD lead chip sector recovery ahead of Nvidia earnings, SOXX +4.7% - StartupHub.ai

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.56 | +25.87% | +14.85% | 219.51 | 223.47 | -1.77% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.56 | N/A | N/A | 449.59 | 449.59 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.56 | N/A | N/A | 118.50 | 118.96 | -0.39% | N/A | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 方向判斷命中詞：surges, upgrade。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 方向判斷命中詞：surges, upgrade。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 方向判斷命中詞：surges, upgrade。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Arm Holdings surges 15% on AGI CPU upgrade; Intel and AMD lead chip sector recovery ahead of Nvidia earnings, SOXX +4.7% - StartupHub.ai](https://news.google.com/rss/articles/CBMigAFBVV95cUxQdk9OSFc1LXdjUE93LVJmNzhiSXliRGVRLWhTWnJ6Z0tkTEkzVUtxYWdwUE9YVHUtcEhLeEJzUDV0aG9xS3BCd2h6bDdzYXVnT0ZfVzlya3pHT0o1dU9IYjVON2JVS1dLZkFSX3JIM0RQUWctWHJNaG9ReklHUnl5VA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 20 May 2026 22:47:06 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：AMD Is Up 8% Today: Is It Outperforming Other Chip Stocks Like Intel and NVIDIA? - Yahoo Finance；Intel Tenstorrent Interest Puts AI Chip Ambitions And Risks In Focus - simplywall.st；德國外資降溫仍優於歐盟國家台灣為半導體關鍵夥伴| 國際 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.76 | N/A | N/A | 118.50 | 118.96 | -0.39% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | -0.32 | +25.87% | +14.85% | 219.51 | 223.47 | -1.77% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.63 | N/A | N/A | 449.59 | 449.59 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.06 | -0.45% | -1.76% | 2,230.00 | 2,230.00 | 0.00% | 未明確 | 74.39 | 29.98 | 410.73B TWD / 17.50% | 2026-05-01 |
| 2303 聯電 | 產業/供應鏈推估 | -0.04 | +4.50% | +7.41% | 116.00 | 116.00 | 0.00% | 背離 | 4.00 | 29.15 | 22.66B TWD / 10.80% | 2026-05-01 |
| MU 美光 | 產業/供應鏈推估 | -0.06 | N/A | N/A | 762.10 | 762.10 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | -0.03 | +15.70% | +11.54% | 1,542.24 | 1,562.34 | -1.29% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.03 | +33.94% | +25.13% | 414.57 | 417.76 | -0.76% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AMD Is Up 8% Today: Is It Outperforming Other Chip Stocks Like Intel and NVIDIA? - Yahoo Finance](https://news.google.com/rss/articles/CBMinAFBVV95cUxPWEpRREtYMk9EbkJlR05sNFBDT1ZnaEhDeHVUOXF5eTRNOHhiZFEtZlBiaDZtem4zazFzd05pelVKQXBoZ1VhOVlYd0JxUTZEVTFYVjJSSnktYXkzWVFqR1Jia08xT05YZnE5Y1lhaTVPbXVpZmhUV2syaXE1OFFRa3JPY3U0UllsYm11QzhhVXk0anNEdVJic1RWdlU?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 20 May 2026 16:08:26 GMT
- [Intel Tenstorrent Interest Puts AI Chip Ambitions And Risks In Focus - simplywall.st](https://news.google.com/rss/articles/CBMiyAFBVV95cUxQdE9EVmhLc3VKejNsRllIZnhJMWNVOERnUkxnOUtSWFM1WkxDQUtVckg1TDl4YjhVRXNCR25JUTV3UGhsbUZhRnBKZnNqY0lGbmQ3NUZpeElNb2RNM2xqU1ZMTFROOUE1cEJzMUlxZ3AxU0hQX3lJTFpIZzBhUE5fM3dFSDk3ak9aUTI2U1lBQ2hRcE9YWFlaYWM1NVZsdU16YzdVaXI3Y1JaOEU2WkIySXI4S3J1NE5tVEVtMVd4c0gtTDkxM3NXU9IBzgFBVV95cUxPcGpXWTB4MlZsaUxoLVdtWFJoYTM1VUN3TmRTNE9zVWR3TkloeGZxRWI3aE5Wcy0ycG9xZXUzOXhhRjRWMnhRVHRwWlMwRGhrQ01TR29BVHRNUEtPcWkzTWJJYkphbnF5QzhYMDhWQlNVTmYxeVBZalAyN3VCYlB0WXVOZGhEYVJyZ3BjVE4yX0dxeVpBUldGSzhsOE12R2tiSVlWWEstZV80bFBaZ280Z3RJdk4tQnEyQnhWODBpb21lVnZjUWM3R0JVNkR2UQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 20 May 2026 08:39:44 GMT
- [德國外資降溫仍優於歐盟國家台灣為半導體關鍵夥伴| 國際 - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1VbXB6aWV4R2lzbWZlRDVoMGd0TUNhQkxVQlBrZXIzVDJOQ3ppa2tPWGR4a3hVOWw5N2xsVGo3UDYtWnRYQ0ROUmxQMkhLME0zSjdfZldva21xSVVlSnpR?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 21 May 2026 14:42:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel Tenstorrent Interest Puts AI Chip Ambitions And Risks In Focus - simplywall.st；千億預算加持！賴清德政策牛肉解密 台股4大紅利股最吃香 AI、機器人、半導體、軍工起飛？ - 工商時報；民眾寧選核電廠，核能是否成為 AI 供電解方？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.72 | N/A | N/A | 118.50 | 118.96 | -0.39% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | -0.05 | +25.87% | +14.85% | 219.51 | 223.47 | -1.77% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | -0.09 | N/A | N/A | 449.59 | 449.59 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.07 | -0.45% | -1.76% | 2,230.00 | 2,230.00 | 0.00% | 未明確 | 74.39 | 29.98 | 410.73B TWD / 17.50% | 2026-05-01 |
| MSFT 微軟 | 產業/供應鏈推估 | -0.07 | -14.82% | -8.96% | 419.09 | 506.69 | -17.29% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | +33.94% | +25.13% | 414.57 | 417.76 | -0.76% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.05 | 0.00% | -6.93% | 510.00 | 510.00 | 0.00% | 未明確 | 10.86 | 47.35 | 62.25B TWD / 19.22% | 2026-05-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.04 | +4.41% | +4.26% | 3,550.00 | 3,550.00 | 0.00% | 背離 | 62.91 | 56.57 | 46.74B TWD / -4.14% | 2026-05-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：衝擊。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：衝擊。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：衝擊。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Tenstorrent Interest Puts AI Chip Ambitions And Risks In Focus - simplywall.st](https://news.google.com/rss/articles/CBMiyAFBVV95cUxQdE9EVmhLc3VKejNsRllIZnhJMWNVOERnUkxnOUtSWFM1WkxDQUtVckg1TDl4YjhVRXNCR25JUTV3UGhsbUZhRnBKZnNqY0lGbmQ3NUZpeElNb2RNM2xqU1ZMTFROOUE1cEJzMUlxZ3AxU0hQX3lJTFpIZzBhUE5fM3dFSDk3ak9aUTI2U1lBQ2hRcE9YWFlaYWM1NVZsdU16YzdVaXI3Y1JaOEU2WkIySXI4S3J1NE5tVEVtMVd4c0gtTDkxM3NXU9IBzgFBVV95cUxPcGpXWTB4MlZsaUxoLVdtWFJoYTM1VUN3TmRTNE9zVWR3TkloeGZxRWI3aE5Wcy0ycG9xZXUzOXhhRjRWMnhRVHRwWlMwRGhrQ01TR29BVHRNUEtPcWkzTWJJYkphbnF5QzhYMDhWQlNVTmYxeVBZalAyN3VCYlB0WXVOZGhEYVJyZ3BjVE4yX0dxeVpBUldGSzhsOE12R2tiSVlWWEstZV80bFBaZ280Z3RJdk4tQnEyQnhWODBpb21lVnZjUWM3R0JVNkR2UQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 20 May 2026 08:39:44 GMT
- [千億預算加持！賴清德政策牛肉解密 台股4大紅利股最吃香 AI、機器人、半導體、軍工起飛？ - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5kcDRNcVFnVkh4ay15a2Q1Umk1VEp1Zjh2R1dCVjk2TGxkREdwVFB5WS1sazMzaUZaNkFpd3VkOVZsZGdLeWJleXRaUWF2aVpTT2pzODhBbjZHbVN5QWIw?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 20 May 2026 19:00:00 GMT
- [民眾寧選核電廠，核能是否成為 AI 供電解方？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiXkFVX3lxTFBCRmFEWWlnQVdJZDhvS01QM01SYjJrUjdsX0I0eVNEcDZVUDRxT1hXTlBzWUZBUEZZUVQ5NnNXelRINDA4STNuLTJBWWppa1JjYmR5VXJTaUtMREYtUEE?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 21 May 2026 21:58:02 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台新證 APP 上午傳當機「重複扣款之亂」恐再現 - 經濟日報；台股基金 吸金力強 - 經濟日報；台股報復性反彈 外資轉買 AI族群狂飆 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台新證 APP 上午傳當機「重複扣款之亂」恐再現 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBVQjg3aVMzM3NmWmdmQVlWUDhJdGZVSERON21jMUxfNzlGLWwxMFFUd1VwV1dCa3U4dC0tRy1wUmlteVkwWHNETjVxbXprWE5YcHRDM3Qxejk5UdIBX0FVX3lxTE94RU5UV0lfaUhzNFczYkZGSkFBX01MWjBtMW91UjNQYlVCUFpUb0hXQkh6ek5nLW5Kd2RhYTk1ZldKQ25TLUlNRWF4aHZVVjNidUJYVmxPbE95T2tRRDRB?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 21 May 2026 02:57:44 GMT
- [台股基金 吸金力強 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5KMGUzNVJqUEhOMGp5bjlCd3o5X3J1aFFXYkxPeE9rdUFIaUY4ZkRkWjMxSDZzcnhacUpfRnNoT2dnak5UYmpaZ0YwWEZCa1ZfMzdyakNWWTcwd9IBX0FVX3lxTFBWRVZtdldLWUtJUHJ6b2x4X1RTcWFFX2syMk9iZ3F4UGNfUVAzbEhRNENnc202alF2N0kwT0tqMjdhSndYSEpLNk1oZnl6VTE1QXVKdUZiNE5YQzFJUzAw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 21 May 2026 16:54:26 GMT
- [台股報復性反彈 外資轉買 AI族群狂飆 - 經濟日報](https://news.google.com/rss/articles/CBMidkFVX3lxTFAyR09PbGJUYmo0OUptT21GTGszMmFmOS1HQ0NxVzFpMzB2b3pDUVpib0JtTTZLT2xBOEpzN2lSVm5UZlZXSDdEaTBkSThHQl9ES2t5T3psYkhocXFoNm0xYW1SOXFTT01iYmJsdklBUlRnblp2c0HSAV9BVV95cUxQQ185cnpmSmZwT2JMOGxjMUhuMVUzV2Rzb0xXZGo3SDJYb0dQd0ltSzVweXEzMGpOTkR5Yk85Z2RSeVVSaE0xUV9JTUt2MTB0N1BJRS1oa2FUVGJOOGhLMA?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 21 May 2026 17:12:09 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：美股指數期貨最新報價 16:38-台股 - MoneyDJ；法人專欄分析內容-台股 - MoneyDJ；統一證券：台股基本面成為上攻底氣- 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [美股指數期貨最新報價 16:38-台股 - MoneyDJ](https://news.google.com/rss/articles/CBMilgFBVV95cUxNNXRZUEVkcGd1VVRaN3hPNVhhLWZiOTU5aFN3eGJjSG1hU3lXaHFERE4xcHBhRU9qOW4xSVVfcTkzcktlUGptZjNiRzBqRW1hcU0xSXB4ODBlVlN6V29MWWFYZy0wbHRFY253ajRqWUgzRnlRTVZMeWZxOUNCR3VVdFZ6TnJlcE5RU21NMndMY1FqV215cWc?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 21 May 2026 08:48:09 GMT
- [法人專欄分析內容-台股 - MoneyDJ](https://news.google.com/rss/articles/CBMijgFBVV95cUxPSjVJdGNjdFFKU0dsOXRUTFFqSW8xX0V6VjhUWTd3eHlQek1GeGlvd2xrdGlTOXJHWGVRSjRVMXJ4Z2dlMm5mZGhQV2RRdndVSHJQVWlCZjR1V3AyOXF3MFROaDlnZ0x3REh1UDVpQmpVX3gtSDBXby1IeldWbTdjREU1WmNBNWN3cVVMUXFB?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 21 May 2026 16:02:35 GMT
- [統一證券：台股基本面成為上攻底氣- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQbU55VU9ZdkRaV0ZJcDZiYWNWYlJIOU15ejIwSVdNbmppaGZQMEdWMUg4ZF9DMFB6RkU1aUxUNUhiTGpFVC1qUnEzci1BOG9RRVZnTDFnVnUyOHAwMElSdk9ETGswbklzTTM0dC1BWkNSYzRmcEExQUd5QkZDMDRDdGVMRVMzSURuQTRUcm9tTG84dw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 21 May 2026 00:32:00 GMT

## 新興題材：SpaceX

摘要：新興題材：SpaceX 相關新聞集中在：Exclusive: Grok falls flat in Washington, undercutting SpaceX's AI growth story - Reuters；SpaceX IPO bets $2 trillion on Musk's ambitious rockets-to-AI vision - Reuters

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [Exclusive: Grok falls flat in Washington, undercutting SpaceX's AI growth story - Reuters](https://news.google.com/rss/articles/CBMiqAFBVV95cUxNYkVBeG83TF9qcjAxRjBDQ3FLR25nNUxtLUFFMmI3S01nSm5obzhLS2FMTDA3MDZTeEpRdGg0TWlCOERydWI4RWlaZVJYRVM4YmN3TVEzRkFBbmtxa2NwWm9OT0xJVjJPQnl3NEZFZzRsOUdGUU13MGNLVFRqTXJZcW93dGk5SGZORExyNjJiX2s3V0tab3Zra21XbGdkaGFiUU9ydFZfaGg?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 21 May 2026 12:39:15 GMT
- [SpaceX IPO bets $2 trillion on Musk's ambitious rockets-to-AI vision - Reuters](https://news.google.com/rss/articles/CBMiuwFBVV95cUxOQWFQNlFYaW5rYmNvNi1JS3VublRZR3JER1VTWEN2aXhPQWNEREl5QnI1QzhoandKMHJDMFpHdWE4SlFWcndBcEo1c1Jfd3hKOTNxc2hMcWpGcnZmUzVmSWlhNnJyRXpPbHl0V0VPbTljM0pxOHpqdnpzejMyTHhRQmc1cTdmczEtRjVyTFFlVTM4b2tZeU9oNHgzZUFMZlN1UC1IcTI4NlZKTlg2RVAxR2lQUGlyaVMtR0NF?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 21 May 2026 21:02:54 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
