# 每日股市熱門話題分析 - 2026-11-27

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜負向｜熱度 3｜市場確認 100.00｜同向 3/3
2. **半導體與晶片供應鏈**｜中性｜熱度 6｜市場確認 N/A｜同向 0/0
3. **新興題材：B300**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
4. **綜合市場情緒**｜負向｜熱度 38｜市場確認 0.00｜同向 0/2
5. **關稅與供應鏈轉移**｜負向｜熱度 4｜市場確認 38.91｜同向 1/3

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.15（樣本 16）
- 5日相關係數：0.36（樣本 14）
- 同向比例：7/16

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 100.00 | 3/3 | 0 | +26.46% | +22.54% |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：B300 | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | 0.00 | 0/2 | 1 | -3.10% | -0.87% |
| 關稅與供應鏈轉移 | 38.91 | 1/3 | 2 | +5.19% | -0.03% |
| AI 伺服器與資料中心 | 0.00 | 3/8 | 4 | -12.72% | -1.62% |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：排除漲價 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-11-14 | -0.34 | 0.12 | +42.11% | 19 |
| 2026-11-15 | -0.02 | 0.62 | +50.00% | 20 |
| 2026-11-16 | -0.30 | -0.27 | +38.89% | 18 |
| 2026-11-17 | 0.44 | 0.39 | +80.00% | 15 |
| 2026-11-18 | 0.27 | -0.38 | +86.36% | 22 |
| 2026-11-19 | 0.20 | -0.23 | +69.57% | 23 |
| 2026-11-20 | -0.35 | -0.36 | +69.23% | 13 |
| 2026-11-21 | 0.04 | 0.04 | +65.00% | 20 |
| 2026-11-22 | -0.11 | 0.38 | +70.83% | 24 |
| 2026-11-23 | 0.26 | -0.36 | 0.00% | 6 |
| 2026-11-24 | -0.41 | 0.30 | +3.70% | 27 |
| 2026-11-25 | 0.25 | 0.11 | +50.00% | 26 |
| 2026-11-26 | -0.31 | 0.08 | +36.36% | 22 |
| 2026-11-27 | 0.15 | 0.36 | +43.75% | 16 |

## 歷史回測摘要

- 回測日期：2026-11-27
- 近5日 3日相關：0.13
- 近5日 5日相關：0.26
- 同向比例：+50.00%
- 權重狀態：已調整

- 方向準確度：+50.00%
- 信心排序準確度：0.13
- 診斷：弱正相關

調整原因：近 5 日方向與信心排序皆偏弱，降低方向詞與供應鏈推估權重，並加重背離扣分。；關鍵詞×公司後續樣本有效 0 筆，未達 30 筆，不調整樣本權重

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

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Micron Falls 7% as a Weaker DRAM Outlook and New Tariffs Hit Memory Stocks; SanDisk Drops 7%: Are Micron and Memory Stocks Now a Value Play? - 24/7 Wall St.；MU, SNDK, SKHY Jump As Nvidia Tests Kioxia Memory Fix — Analyst Presses Memory Giants For ‘Massive’ Buybacks - TradingView；美光勞資衝突恐釀雙輸？謝金河曝「美光考慮關廠撤資、資遣3千人」 恐牽動半導體產業 對台灣茲事體大 - 工商時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | -0.61 | -38.08% | N/A | 601.25 | 971.00 | -38.08% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.61 | -6.67% | -19.45% | 94.39 | 291.88 | -67.66% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | -0.47 | -34.63% | -25.63% | 149.30 | 228.38 | -34.63% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、MU、美光」，共 3 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：falls, 恐。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk、SNDK」，共 2 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Micron Falls 7% as a Weaker DRAM Outlook and New Tariffs Hit Memory Stocks; SanDisk Drops 7%: Are Micron and Memory Stocks Now a Value Play? - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiiwJBVV95cUxPMHo3cGJWUUhPeEoxeTRsSTRvWldWNF9yUG9tbTlpR0Q4QW80S1g2cnJyUHMtZm1pM3h6QUxtLV9JMktCYXRicFltVUxfWFRXNWJxOGh0b283S1FlSkNBOWV0eDJpQUdxZWRfX0hXeHIwR3JROWt2N3ZFaUdJcGRDQ2QwLVBuMGlvVzVlWGtjUlJmRnA4b1JhTUNRMGRZRG16a01EUG9ZV0ROWkF0MFpoYldLWEZMeTl6TlJSMDVfZjV3dG9ndGFsb1Z0eEV0dm9QWFN6bVRiS2hlbzVhYndvbk5SeVluWnIySGxIeFdocDFqTDNYLWFRdXZXX1RXZmNONUFDSFljOFFnVW8?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 25 Nov 2026 14:13:00 GMT
- [MU, SNDK, SKHY Jump As Nvidia Tests Kioxia Memory Fix — Analyst Presses Memory Giants For ‘Massive’ Buybacks - TradingView](https://news.google.com/rss/articles/CBMi9gFBVV95cUxOTGlsbjI2elVWYkZiSGpjdjdZc083S2lsWVNzT0MyS2l2X1RJdzRfa1BXTnVRanlaWXZ6aGpMaEpqSEtsNGNYMFlzS0hEbi1oWjY1VFRPS29WcjJyMkpGUm9qSEx6T1BOdnl4OFhhVGFaX0FTbFRoQTRyMENISXFsWlFCbEtZM1hDcXhvWDNneHNuTDhIeG85LUpMRE8wV2R2UloyZkdqRWJEUlZNQzZnX2xZXzQwOGtIUGxLckNWbVRjZlVSZEpTME9BME53Y1ViWFZQYU5KM3poV0NPWTRPTXZwV3V6aVZRZlNXMWpCWDU2YWhGc2c?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 26 Nov 2026 06:30:00 GMT
- [美光勞資衝突恐釀雙輸？謝金河曝「美光考慮關廠撤資、資遣3千人」 恐牽動半導體產業 對台灣茲事體大 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE0xOExsVVBvR0t1bGhxTnpldXVoYUFaQ1ppZnNSNEpYVzBEaXZ1bWp5U2t4X2tPaUJiNjdDLURQV3dTTzU0S2ZfbzdZOVVHSEhNbG5zcFpER29nUGpmaXVn?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 26 Nov 2026 02:47:00 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：台股選前39,000點拉鋸！川普曬半導體投資、台積電美廠活動倒數 | 市場焦點 | 證券 - 經濟日報；2026年臺灣IPO創新動能升溫 半導體籌資居冠 - 中央社 CNA；半導體ETF成市場震盪布局焦點這檔績效最強原因曝光- 理財 - 工商時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | 0.00 | +5.67% | +2.14% | 2,170.00 | 2,480.00 | -12.50% | 不適用 | 98.27 | 21.83 | 586.89B TWD / 59.71% | 2026-11-01 |
| NVDA 輝達 | 新聞直接提及 | 0.00 | -34.63% | -25.63% | 149.30 | 228.38 | -34.63% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | -52.50% | +34.29% | 54.47 | 114.68 | -52.50% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +0.57% | +0.68% | 88.60 | 164.50 | -46.14% | 不適用 | 6.80 | 13.12 | 25.20B TWD / 18.33% | 2026-11-01 |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | -21.33% | N/A | 406.03 | 516.10 | -21.33% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | -38.08% | N/A | 601.25 | 971.00 | -38.08% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -6.67% | -19.45% | 94.39 | 291.88 | -67.66% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -14.33% | -22.71% | 300.86 | 446.77 | -32.66% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip, foundry。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 CPU, server CPU, x86, foundry；其中 3 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [台股選前39,000點拉鋸！川普曬半導體投資、台積電美廠活動倒數 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBtNVRxU3ZraE1zSG11WmdONUtneGxvOVB3R0l5OWltc3hfS3NWX05iaURndzVFdGxlT3p5Zmg5MlRNbzFvWTJyb0gyX1pjM29mTnhIYngxZU1qUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 26 Nov 2026 08:00:00 GMT
- [2026年臺灣IPO創新動能升溫 半導體籌資居冠 - 中央社 CNA](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBXSER3SXZWRWI3aUtvcF9lcDB6cXVDTU9tQjlxNm1QT3dWaEdTTjVjeDN4UEZ1bEpvQ2Y0R1ZpbmE0U0pwamZmY04zMXdxX1NFUUFJZDhOenI4UQ?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 26 Nov 2026 09:40:02 GMT
- [半導體ETF成市場震盪布局焦點這檔績效最強原因曝光- 理財 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTFB6QkZaaHBQSVIwbTFlOUxhaEVROVZVWTVEY3RKVld3QVlsb3NGeEJhYUdZODNSeThKM1FyeWFULW9pOWtvNDY0MjZJVkJmUEdITVczbjZiWDFDamZ1N1pr?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 27 Nov 2026 02:35:00 GMT

## 新興題材：B300

摘要：新興題材：B300 相關新聞集中在：中國 AI 算力需求有多強？美國新規掀輝達 B300 求售潮 - TechNews 科技新報；禁令擋不住！輝達 B300 伺服器現身深圳華強北，一台開價 300 萬美元 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | 0.00 | -34.63% | -25.63% | 149.30 | 228.38 | -34.63% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [中國 AI 算力需求有多強？美國新規掀輝達 B300 求售潮 - TechNews 科技新報](https://news.google.com/rss/articles/CBMirgFBVV95cUxNeDE4TUFmNktvOGVNdW5PQ2FJdkJqUWJOcVlkTlAxRjFSTGVnZTVwd1dLQ1FoZTlpTTZzXzFjU1BkclZHTUtPQ24zeE95aVVHbnVBZVlQOVVpRE01XzBWU3lOX3Y2UHJGeTFFa3BrdnFQcTdvNXNfYzBtTG9INlVmNXRxcEFaYWVTX0xYYXg3NFhvMERETDBUYlRWamRTTThfS0N0SHREUnJ3OFVnV1E?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 27 Nov 2026 00:11:44 GMT
- [禁令擋不住！輝達 B300 伺服器現身深圳華強北，一台開價 300 萬美元 - TechNews 科技新報](https://news.google.com/rss/articles/CBMitAFBVV95cUxOeXFsLTBXMXBtaVJ6alFHMExBdXk5aWswZi1YS0VYOERwOG5HQnRqVk1xVWtKQlh0aGZaTWdpMFA5eWpCMUdTNnVGOVQ0ZWdRRk9xdGpwLUhwZkNiVWE5UG9HcE9INEw2dmhhN2FoMUtEUDZNLVI5UWVicTlSNVZoal9DbkpkbU1CQlZBQTFjY2libHZGaHVDTkFuS2NsaFFZSUFNcEx3RVU0UkpKcG9YajJLTFI?oc=5) - Google News source discovery | TechNews 科技新報 Fri, 27 Nov 2026 01:56:57 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股出現感恩節行情？法人研判 最壞情況已過 - 經濟日報；台股多空激戰3萬9！聯發科、台達電翻黑 台積電能扛住？ - 經濟日報；台股早盤漲逾200點後震盪　權值股穩盤衛星題材股勁揚 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | -0.27 | +5.67% | +2.14% | 2,170.00 | 2,480.00 | -12.50% | 背離 | 98.27 | 21.83 | 586.89B TWD / 59.71% | 2026-11-01 |
| 2454 聯發科 | 新聞直接提及 | -0.34 | +0.54% | -0.40% | 3,685.00 | 4,920.00 | -25.10% | 未明確 | 62.35 | 59.59 | 55.03B TWD / 5.77% | 2026-11-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 2 篇新聞命中。
- 2454：新聞直接提及「聯發科」，共 1 篇新聞命中。

### 主要來源

- [台股出現感恩節行情？法人研判 最壞情況已過 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1fOVJQX0t2QWR5UnVYcnR6RVRIV1A2V0NKVDRxc2JEa3lUSWVuZHlXbTRvalpXczI5MUd2a3ZRcWJhWjhRcWoyQm9qb3RqbmtLUlAtVUFldS14UdIBX0FVX3lxTE1qSUZOaDN6UGRDYXI1MWhtQmJDUFUxRFM4NFR0V2I3c0pFSDVxUzYtcm03bV93cjJSbmhYbFhLdkVSZ3pFLXRIdTk2LW9NSVRZWGFFTzFqQUVEd0pTb2lr?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 26 Nov 2026 19:32:26 GMT
- [台股多空激戰3萬9！聯發科、台達電翻黑 台積電能扛住？ - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1QQlNEWmRBVHN6OWs4THVIeF9NZzBZbUtDUG9XU0lQb0w1Tlh3VDR4OXQxdlBiVVBuN1MzTWtjWGdKLUZieS1CMmFLWUlvbC1xQ09vZTFJaEszd9IBX0FVX3lxTFBTSU43MDhDbDRnYnU0RzVqa2plMVpXSlBoby15dUlRWTFfSVRQUWlnR1B0bm96YmdOb3FXemtBQThzbWdCUnhYUEJDcDR2QlB6cm43aUR6MGNvbEk2ZGJN?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 26 Nov 2026 08:00:00 GMT
- [台股早盤漲逾200點後震盪　權值股穩盤衛星題材股勁揚 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBySzUxT3FROGZHMHVPMVBvV3ZsVzVINERJMzJCTUFwZVN4VDdNUTZ3TkVUcTJQa2dlYlJGemNEa2hIVm9OZklsWk4tZFI1aG5iUXNhWlhrUlpsUdIBX0FVX3lxTFBGUXVXWWN4eDRHd3FTOFJTaVJCaFFfSWhlQjhNRUJ4QjRURmdTOERQd0R4NmthUng4ajlHNDI0WXBqbHpYNjhxY2ZUYWFpbVNtT3pqWW50NVZEVTJQcDY4?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 27 Nov 2026 01:21:52 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：黃仁勳回歸行情 3 天洗一輪，輝達概念股還能追？五大 AI 供應鏈盤點【黃仁勳11天回鍋懶人包】｜美股觀察 - 永豐金證券；美擬對馬來西亞課最高18%關稅學者估半導體投資影響有限| 國際 - 中央社 CNA；European stocks end higher on easing tariff fears, ECB leadership continuity - Reuters

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | -0.45 | -34.63% | -25.63% | 149.30 | 228.38 | -34.63% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 產業/供應鏈推估 | -0.04 | +13.95% | +27.52% | 355.58 | 355.58 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | -0.04 | +5.10% | -1.81% | 220.50 | 289.00 | -23.70% | 背離 | 16.57 | 13.10 | 1305.32B TWD / 45.73% | 2026-11-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 1 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 1 篇新聞出現相關標籤。

### 主要來源

- [黃仁勳回歸行情 3 天洗一輪，輝達概念股還能追？五大 AI 供應鏈盤點【黃仁勳11天回鍋懶人包】｜美股觀察 - 永豐金證券](https://news.google.com/rss/articles/CBMi4wRBVV95cUxNc0hVTlMycGE2T0h5RWRDcDJvSTZ2S1VXMjBZa3prV3hNTndubnhoS2VPakkzRHZOanV5M2kzbG1hazNwVkExVEJ0NmhFOXRjRzFKczVNR2hUbnBtaWtYNjRuQTBWV0ZRSmxPRXZlYTJZcE1VVkNNaWZiOVo2dkRkRzc4MjBOY29XN0l6eEIwbTlVd0lLU0gzSWZBb3FlZzhacHpXQXlwM0xDSDdJNFRacEdaTFhBTDhrd2JnNWstNExZTjBubHc5eG5FVEZhcEdYVW1idVVrS1dRcXpxQzhPai1fckJlc0VmdDJaQjI3RXJiNnZTNUhueEo1bmRqWmR0UmtiRUFaRUJLVWw2Z01FcTlMenk4LUhLY2FmLVNFTndlRnVKZWpJNEpGeXdnSmlnZVB3RmxvNHVEdGFvaEJIVVhEdGs0VWUwUllpaVNuSmNLVXhCMlJXazNYcnRseFZSSFRDZkU5aGVhNjV3NTJnN1lEN2JZb29jYmhDSnlPZk5lSW8tb2UxM01yVG5MOW5CQldTb1JfbkxaRnJram5Na1M4Sm92b3p2eWppUmlwdEZMV3dkZDEzZnktWGZnNU4wVXBOZS11MTJiXzhZWFRwQXBKZW9ZS1piOWFjdUNOTzlma0J6RWlzMlk1NFhHLXYwcVppTkpFblRlMzBQYTIyenJUeGUwVWpEdjZFRWpsRWJ0bnlaa3JOVzdVQXRXaEZyREszYXh5VlRleHVEbkFOUjZLa2U0OHdVMkZwUzBXOE1hOVZTcUEwWWZzT0RLMTl6WW93WXpPQzZQRXFYMlBQdE5jTQ?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 26 Nov 2026 03:55:01 GMT
- [美擬對馬來西亞課最高18%關稅學者估半導體投資影響有限| 國際 - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5vcDdGR2RWTVRsbjg4ckYzQ3BnUERSbVIwYzVoVEx1dG9JSFdPZmthY0xHNDJYdTl5MzhZSUZkZUQxc0pIenVZOUE5WnphWkttVVNqLUJqTmpFUWsyX21v?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 26 Nov 2026 12:51:00 GMT
- [European stocks end higher on easing tariff fears, ECB leadership continuity - Reuters](https://news.google.com/rss/articles/CBMisAFBVV95cUxOWDAyOS03ZTA0ZzRTRmR6d2diZDJ5X0V0ejhjSlg1MzhMaTlCNU1LNTBCYVlJS2VhVV9USmNxYnNGYk9CaTdYckN1NVBZLWNKQm9BYXB5SEpNYVMyN3hzbFRjaExPY3piakNDakM1Qm1NSDJ1MFJLZzF3NGN5TFVCYThrYmNzZFhyVzN1bVBhaXh6a2t4cUxNQzBGUnpWVVFxb1l2cFR5WE1UZ0tvUEpDcw?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 26 Nov 2026 17:43:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：AI 駭客逼銀行加速修補漏洞，系統更新反而成了當機風險 - TechNews 科技新報；Meta 大裁人工審核力推 AI，員工憂演算法成政治黑箱直言：真的是一團亂 - TechNews 科技新報；Anthropic 揭露 AI 時代工程師升遷關鍵：看重「協調力」與實際成果 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | +0.04 | -52.50% | +34.29% | 54.47 | 114.68 | -52.50% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.03 | -34.63% | -25.63% | 149.30 | 228.38 | -34.63% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.03 | -21.33% | N/A | 406.03 | 516.10 | -21.33% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.06 | +5.67% | +2.14% | 2,170.00 | 2,480.00 | -12.50% | 同向 | 98.27 | 21.83 | 586.89B TWD / 59.71% | 2026-11-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | +8.82% | -0.42% | 489.93 | 507.29 | -3.42% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -14.33% | -22.71% | 300.86 | 446.77 | -32.66% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.04 | +6.02% | +1.39% | 521.00 | 703.00 | -25.89% | 同向 | 17.55 | 29.33 | 88.62B TWD / 47.13% | 2026-11-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.03 | +0.54% | -0.40% | 3,685.00 | 4,920.00 | -25.10% | 未明確 | 62.35 | 59.59 | 55.03B TWD / 5.77% | 2026-11-01 |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AI 駭客逼銀行加速修補漏洞，系統更新反而成了當機風險 - TechNews 科技新報](https://news.google.com/rss/articles/CBMitAFBVV95cUxQcmo5WmRkRDVhMUVkQXdReDFfN3J1NFg5RkUzWS15V0FXamU5UVVRYklEeVJyNGJqb2t3NnlVZzJtSFROWmtHa2M2U0NJVUdWYzJOQ09nSkEyQzhxUVJWOFRWbmdEZ3otcldQOGcxZzUzVk9fZnFqc1Z0aC0weWlTbnZmb0dWRjk0dndaSWY4YnJzNkVoZFlzUnUtWEU0cFNOcjg2YmJCcF8xNl80SzdUZ21UWXQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 27 Nov 2026 02:37:01 GMT
- [Meta 大裁人工審核力推 AI，員工憂演算法成政治黑箱直言：真的是一團亂 - TechNews 科技新報](https://news.google.com/rss/articles/CBMid0FVX3lxTE5tTElSWWJZTm11QWZYcXUzdktuVm84ZXpMTEhUUmd0X2g1eml6ckFKb0w3cnRVN2I1dHpFZzZsMV9ESHRxY0IyX1BlMEZYU0ctSUxyNEFoRFhCWlF4TUdFSlFyZGhMQ0ZQZkpjSVBfN3lkOXN5VkNz?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 27 Nov 2026 02:01:57 GMT
- [Anthropic 揭露 AI 時代工程師升遷關鍵：看重「協調力」與實際成果 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiogFBVV95cUxNQzVvU2JRWVNXX0RFZUtzRFlxclM3Q2tqdDZmZEZ1cFRSc3EwVWpWSVRsUTh4aE1NTC1IOWJlUnFvNWtKeDRpdVppNURuMlRvNzAyTmNSMkRXMVhQeFI2VVNEV3A1ZFBQVEZvaEdRak0zc25hNW9nMC1CNnJfNGJwdklRUHlKTmhDcnZ4bUlBTnlXa0wtU1JlVklxTmViajBlanc?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 27 Nov 2026 03:12:03 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：統一證券：台股技術面已現築底反彈契機- 新聞 - MoneyDJ；國票證券：台股築底條件更成熟- 新聞 - MoneyDJ；基金-FundDJ基智網 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [統一證券：台股技術面已現築底反彈契機- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNQ202Zkd5RGZuTm5kSWlQRHZia1I3elBQWVlmQjJTbU9lQkZPVWdzVGhyMWk1QzJQbWlZZEpKS1VHQlFWbXpicUh6cDBEc2V3b1BFQW1mQWxCay0zejdvVEJ6ZkJWbldETFVlM2M0YndrQUM4c3dHREd0Nm53OHQ5cVV1UElGT09PSmI5bEFEZ0xpZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 27 Nov 2026 00:43:00 GMT
- [國票證券：台股築底條件更成熟- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxOWUF4Q2FudjRxUWRMdHlZZmJlSlJzZWxaT3hCVUU5OWNQS0xRQ2xTTEl1ajM5dndmcHNxRUtVVVFTMklfM2c0NHdEMWN5a1hRRzlHODNPS2w2a3JmY3R1YVlSdVd2dzc3N0ZBTGxZbWVPNjAzeHhUM21FM205SlV1dDFGajNRZlM5WDhnZUpVeW52UQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 27 Nov 2026 00:43:00 GMT
- [基金-FundDJ基智網 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxOODdzQVpfZ3FFVmd2Q1VTcWlNa3QxSnFib3oxNzl4VlUtZ0lwb3JiYzZCNnFKWlNzZ2M3cEg2a2s2V0tia0N1T2E1ZzRqVTJFWXJGZjRlRGxzalppbW9EZWhHcG1SaXFIak9hMVdsNzBIZjdhWlVpSGpDUUhSbHN2SmVRRE42MzZyUDZ5YWZYdHg?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 26 Nov 2026 20:00:40 GMT

## 新興題材：排除漲價

摘要：新興題材：排除漲價 相關新聞集中在：排除漲價因素，研華明年營收仍看增逾兩成 - Yahoo股市；排除漲價因素，研華明年營收仍看增逾兩成- 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [排除漲價因素，研華明年營收仍看增逾兩成 - Yahoo股市](https://news.google.com/rss/articles/CBMitAJBVV95cUxOQXg4UV9vOVVMTWQ3SXdMeGRUSV9sUFFPRi1OT1puektBdEdDc2VaVGZzSWFiSm1ZVzZoNFJMQkVTVzZlN0QweEhMOWVXY2dkNEZXWVpLWkpCeUw0S0labnY3VDJoMWFHUk1rc1g0dGxEMzJ0YmZLVG5vTEk5WjJfNFJyVEsxVi1nVXFBZW1ON3Nha2I5LVRQQllvZThUWXpJaWJRcXE2TXV3R2s1MVZVR1RVVFJUZmRWd0hzWERtS0tKYlQxV3BuMHpUNHJBV1haM3VnOGI4YktMTTBVOWNIN1UzM2lkMVpJZHd3Qjlnek96akJhc25FdjhzVC1KSXJRY1ZHNzlkQVJPa0dNNWRrQzRLMG5KSFQ5RWhnazdhd3NiYVdoMjREOUFzd3JtLUZMUHQ0Sg?oc=5) - Google News source discovery | Yahoo 奇摩股市 Fri, 27 Nov 2026 02:34:12 GMT
- [排除漲價因素，研華明年營收仍看增逾兩成- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQWDlkWF80TUJkd0pMb0lmYVVLOGZKc2xlOWxGbkVOeWFnc2JYVDdfd3ZOdHVkZUNnRkNkQUNCTXBNWV9aMXNaVm1GRkhyZXVMbG45SE9pS3dyVDdueVVObTRwWnR6MkVyRGJKblZNbUFLYmkxUFhmc0I2aUFkbFVqSlJHb1A5c0p6OGNONzJ0SmNpZw?oc=5) - Google News source discovery | MoneyDJ Fri, 27 Nov 2026 01:21:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
