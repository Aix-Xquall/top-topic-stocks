# 每日股市熱門話題分析 - 2026-11-23

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **AI 伺服器與資料中心**｜中性｜熱度 8｜市場確認 N/A｜同向 0/0
2. **半導體與晶片供應鏈**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
3. **綜合市場情緒**｜中性｜熱度 32｜市場確認 0.00｜同向 0/2
4. **新興題材：OpenAI**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
5. **關稅與供應鏈轉移**｜正向｜熱度 4｜市場確認 0.00｜同向 0/1

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.26（樣本 6）
- 5日相關係數：-0.36（樣本 6）
- 同向比例：0/6

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| AI 伺服器與資料中心 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | 0.00 | 0/2 | 2 | -10.46% | -17.89% |
| 新興題材：OpenAI | N/A | 0/0 | 0 | N/A | N/A |
| 關稅與供應鏈轉移 | 0.00 | 0/1 | 1 | -45.03% | -37.47% |
| 散熱與液冷供應鏈 | 0.00 | 0/2 | 2 | -27.88% | -32.47% |
| 新興題材：TradingKey | 0.00 | 0/1 | 1 | -55.28% | +26.43% |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-11-10 | -0.32 | 0.24 | +3.45% | 29 |
| 2026-11-11 | 0.34 | -0.26 | +46.67% | 15 |
| 2026-11-12 | -0.09 | 0.07 | +50.00% | 14 |
| 2026-11-13 | -0.56 | 0.42 | +54.17% | 24 |
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

## 歷史回測摘要

- 回測日期：2026-11-23
- 近5日 3日相關：0.08
- 近5日 5日相關：0.21
- 同向比例：+89.47%
- 權重狀態：未調整

- 方向準確度：+89.47%
- 信心排序準確度：0.08
- 診斷：低相關

調整原因：近 5 日信心分數與股價關係偏低，提高價格確認，降低寬題材推估。；關鍵詞×公司後續樣本有效 0 筆，未達 30 筆，不調整樣本權重

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

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel (INTC) Chip Breakthrough Opens A Fresh Angle On Its AI Push - Simply Wall St；AI 產出「做半套」，隱形補位工時正吞噬企業效能 - TechNews 科技新報；GTIC 報告：漏洞利用、AI Infra 與網路釣魚正在成為 AI 代理駭客三大獲利源 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | 0.00 | -45.03% | -37.47% | 125.53 | 228.38 | -45.03% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | 0.00 | -55.28% | +26.43% | 51.28 | 114.68 | -55.28% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | -17.77% | N/A | 424.39 | 516.10 | -17.77% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -7.83% | -14.89% | 2,020.00 | 2,480.00 | -18.55% | 不適用 | 98.27 | 20.36 | 586.89B TWD / 59.71% | 2026-11-01 |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +7.61% | -1.52% | 484.52 | 507.29 | -4.49% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -13.32% | -21.80% | 304.41 | 446.77 | -31.86% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | -12.12% | -23.58% | 474.50 | 703.00 | -32.50% | 不適用 | 17.55 | 26.23 | 88.62B TWD / 47.13% | 2026-11-01 |
| 2454 聯發科 | 產業/供應鏈推估 | 0.00 | -12.76% | -18.69% | 3,565.00 | 4,920.00 | -27.54% | 不適用 | 62.35 | 53.88 | 55.03B TWD / 5.77% | 2026-11-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel (INTC) Chip Breakthrough Opens A Fresh Angle On Its AI Push - Simply Wall St](https://news.google.com/rss/articles/CBMizwFBVV95cUxOMFVnTEhsQmRscnNQUEpoZnpyQWNHYWw4dldMLWVPR2dXMHdxTmltU2xlajZvZy1tdzZacE96VEphZEJPMWZ4X0lOT1VVVnlsQUhZMVZaWGoyeGVBeFN3aF9BY1dIQzFEcmg1czlyZGI5MXJhU3dOaThNMmtrc3AzT3VEbzVKTVk1OVhYaEtIdm5GRk5aN2dVYml0SXNnSjhTWTFVcWdod2F4QXp6VDJyb1o4NmtzR1hfdlVWak5naFRqM0V0cUlkR2t5eHdXVzjSAc8BQVVfeXFMTjBVZ0xIbEJkbHJzUFBKaGZ6ckFjR2FsOHZXTC1lT0dnVzB3cU5pbVNsZWo2b2ctbXc2WnBPelRKYWRCTzFmeF9JTk9VVVZ5bEFIWTFWWlhqMnhlQXhTd2hfQWNXSEMxRHJoNXM5cmRiOTFyYVN3Tmk4TTJra3NwM091RG81Sk1ZNTlYWGhLSHZuRkZOWjdnVWJpdElzZ0o4U1kxVXFnaHdheEF6elQycm9aODZrc0dYX3ZVVmpOZ2hUajNFdHFJZEdreXh3V1c4?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 22 Nov 2026 23:12:52 GMT
- [AI 產出「做半套」，隱形補位工時正吞噬企業效能 - TechNews 科技新報](https://news.google.com/rss/articles/CBMijwFBVV95cUxOa001MlFlUmZPZUNGNWhXeUJLMGdzZUdDOUIweml6clA5RmtPYnM5Y25mUmNuQ1BqZU10NlliWC1QemhkNkpnWm5nRmFKNHI3azN4YWNrOEZ5dDJVOXZFU3hpVy1JUDBCM2pFTk9EQ1R4NnVNUDhZUWZldHY0dTJmdmRkajFsM0tIUGxiWXUyZw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 22 Nov 2026 23:41:52 GMT
- [GTIC 報告：漏洞利用、AI Infra 與網路釣魚正在成為 AI 代理駭客三大獲利源 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiwwFBVV95cUxOOHRkNXk2Qlhab3hPajJkOWhQRTVEc3pfT2d3TVJfdVJvcmhTNTdKNXBxRWptYzVQYzl3dm1yalE5RUpXSzdYMkxEOWVmcFdQbTRsVXp6ZkhOOVVTbXNoaTBxcGllRzFGdEt3Q2tvSGpJT3FmTkRyaEx3X3JYc3RpQnByRE5qQTZFZWphMkFNbXFGY05aUHVFNlIxTmttcjYtN3JJOTN1Nl93elZ3cVBlZmxwWW5xaUFvNFAyX2NEc3I5bGc?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 22 Nov 2026 23:18:14 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel (INTC) Chip Breakthrough Opens A Fresh Angle On Its AI Push - Simply Wall St；紐時：輝達醜聞爆發數年前，中國國安部已盯上 AI 晶片 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | -55.28% | +26.43% | 51.28 | 114.68 | -55.28% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | 0.00 | -45.03% | -37.47% | 125.53 | 228.38 | -45.03% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -7.83% | -14.89% | 2,020.00 | 2,480.00 | -18.55% | 不適用 | 98.27 | 20.36 | 586.89B TWD / 59.71% | 2026-11-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | -13.10% | -20.89% | 88.30 | 164.50 | -46.32% | 不適用 | 6.80 | 11.86 | 25.20B TWD / 18.33% | 2026-11-01 |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | -17.77% | N/A | 424.39 | 516.10 | -17.77% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | -38.77% | N/A | 594.51 | 971.00 | -38.77% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -6.67% | -19.45% | 94.39 | 291.88 | -67.66% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -13.32% | -21.80% | 304.41 | 446.77 | -31.86% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 1 篇新聞出現相關標籤。

### 主要來源

- [Intel (INTC) Chip Breakthrough Opens A Fresh Angle On Its AI Push - Simply Wall St](https://news.google.com/rss/articles/CBMizwFBVV95cUxOMFVnTEhsQmRscnNQUEpoZnpyQWNHYWw4dldMLWVPR2dXMHdxTmltU2xlajZvZy1tdzZacE96VEphZEJPMWZ4X0lOT1VVVnlsQUhZMVZaWGoyeGVBeFN3aF9BY1dIQzFEcmg1czlyZGI5MXJhU3dOaThNMmtrc3AzT3VEbzVKTVk1OVhYaEtIdm5GRk5aN2dVYml0SXNnSjhTWTFVcWdod2F4QXp6VDJyb1o4NmtzR1hfdlVWak5naFRqM0V0cUlkR2t5eHdXVzjSAc8BQVVfeXFMTjBVZ0xIbEJkbHJzUFBKaGZ6ckFjR2FsOHZXTC1lT0dnVzB3cU5pbVNsZWo2b2ctbXc2WnBPelRKYWRCTzFmeF9JTk9VVVZ5bEFIWTFWWlhqMnhlQXhTd2hfQWNXSEMxRHJoNXM5cmRiOTFyYVN3Tmk4TTJra3NwM091RG81Sk1ZNTlYWGhLSHZuRkZOWjdnVWJpdElzZ0o4U1kxVXFnaHdheEF6elQycm9aODZrc0dYX3ZVVmpOZ2hUajNFdHFJZEdreXh3V1c4?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 22 Nov 2026 23:12:52 GMT
- [紐時：輝達醜聞爆發數年前，中國國安部已盯上 AI 晶片 - TechNews 科技新報](https://news.google.com/rss/articles/CBMipAFBVV95cUxNLXgtY3Q3ZWI4YnJ0RTdPdGlvREVwdmotaElpa0dSWkg4SWx3Y0hndnBTWk4weFVrZ181bTZaNURDVm9qZEZSV0FIOG95aTh5dDRwWjZOOFdUVG5DbWV6bGNmR3pCcHdSQWk3ZGFBTUFRWGl3TjBWQkt4eWpoU1lPWUFqT3RHU3B0eDJqcU03eEpaZTJrMUFEeEJVWlFBY2FGUl9MeQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 23 Nov 2026 01:03:15 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：費半崩跌逾10%拖累！台股36K前震盪 聯電漲停打開、台積電重返2千 - 經濟日報；政府救台股 別搞錯方向 - 經濟日報；台股平衡基金 穩穩賺 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | +0.24 | -7.83% | -14.89% | 2,010.00 | 2,480.00 | -18.95% | 背離 | 98.27 | 20.36 | 586.89B TWD / 59.71% | 2026-11-01 |
| 2303 聯電 | 新聞直接提及 | +0.24 | -13.10% | -20.89% | 87.40 | 164.50 | -46.87% | 背離 | 6.80 | 11.86 | 25.20B TWD / 18.33% | 2026-11-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 方向判斷命中詞：漲停。
- 2303：新聞直接提及「聯電」，共 1 篇新聞命中。 方向判斷命中詞：漲停。

### 主要來源

- [費半崩跌逾10%拖累！台股36K前震盪 聯電漲停打開、台積電重返2千 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1ZXzZUS0g2Zm5LUHFGenozcjExZFJHeW9nbk1LcEs3YV9GTS10cFl3TWJGQUpHYTBpWjNpWFQ5MVhiR2EzQ0x4bUx1SWxPeFd5SzZsSFF6Nm9PUdIBX0FVX3lxTFBGa2wtU3ZvTmI1anEwbFk5MC00TFdIZTVJR1dwUU5WU0ZaSmhvQVZTZFlPODFXSzFIc2gtWENhX2g2V2VJa18yTlN4MlhESmt0U3puNWhFNldBUDN0dVJF?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 22 Nov 2026 09:00:00 GMT
- [政府救台股 別搞錯方向 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9GWm1pa3R4TDJ3UUp1U2NONGRaSDJ1S1Jidm9WeGJNT0lVTlFkVWlPTXY3YWREMW4wTUFKTDlOaXROdS1ONEJZU2loLUJMM2pCeHQtWWFIMUhMd9IBX0FVX3lxTE5mQjZKLVloc21GWFlKUmZKNmtEUy1IRlI1bmh1NTVlUDc1ODN1cTZYV1I4NWd6VU9rY2oxbUFSWDRFdnhxcmpubWswSU1jcGNkV0xjeENVVm9GVnBxWEow?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 22 Nov 2026 18:49:04 GMT
- [台股平衡基金 穩穩賺 - 經濟日報](https://news.google.com/rss/articles/CBMieEFVX3lxTFBkeV80UU1wVmk4bWloVXFfMXhPck1VSGg5dHpvZUVnWW11NzFGaEhRSGJvV1hCekg0YXM2RkgtOHpvRU83bEVyelV6ZnBmck1SbjUzMUJHcW1vZUNYOVdfdHNUclJLQTJodmVmRkN4TmR0aDYtUEF5WdIBX0FVX3lxTE9VZHpYUERoTi1MQVRsMDlHMjUwWWNHME9STnN0RmdTeGVzamVsYXRTZk5pX3NJTVhmTFAzTVRkYmpkdm5iZ1lxQlU1aXVkNXVqdFU2WWtTVGZQa3hHdThR?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 22 Nov 2026 16:46:58 GMT

## 新興題材：OpenAI

摘要：新興題材：OpenAI 相關新聞集中在：養出 AI 駭客？OpenAI 被加州政府告上法院 - TechNews 科技新報；OpenAI scientist proposes industry AI limits tied to model intelligence metric - Reuters

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 新聞直接提及 | 0.00 | +7.61% | -1.52% | 484.52 | 507.29 | -4.49% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：新聞直接提及「OpenAI」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [養出 AI 駭客？OpenAI 被加州政府告上法院 - TechNews 科技新報](https://news.google.com/rss/articles/CBMicEFVX3lxTE5wRFFBVk1CZkx4RnZMY2oyYTZnZDMzX0xJT1p3eC10U0k4bU5VNng5NkN6VmJTa24tMmU0RjAzdE42aEkwbl84QV9talc1MFYzWkNSbk5CcXFUVWUyZVZMSHJLekxmdWN6QlUzVFhjMFQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 22 Nov 2026 23:53:05 GMT
- [OpenAI scientist proposes industry AI limits tied to model intelligence metric - Reuters](https://news.google.com/rss/articles/CBMivAFBVV95cUxPa0ZQb0xtalJ5djRmZmkwQnhmdDBlMEtncDUtUEJsUFBtWmptbkdVQ3c5QjY2TzhKN0NFT2ZzYnZmenQxY1lrUWFFYjJsdS1KazdRUkJINEJRemQ1alh6TGtnNW1nRE92bTF3RW9FMTIyODB3UmpBaW5oSzFDWDFVT3FXdjZDVzQ0TVNVd29nQzZvY3ByWVpBLUlhRVg0bFZiRHUxVjhqclptLUMycDJlYVBsQXQ4a28tRnFnbQ?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 22 Nov 2026 23:09:59 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：整理包／黃仁勳概念股笑了！輝達季度財報超預期 完整台廠供應鏈名單、潛在受惠股一次看 - 經濟日報；愛豐通運布局捷克打造歐洲半導體供應鏈樞紐| 全球中央 - 中央社 CNA；黃仁勳去職美嚴控 AI 產業，重大事件和供應鏈看法一次看 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.24 | -45.03% | -37.47% | 125.53 | 228.38 | -45.03% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +9.77% | +22.85% | 342.56 | 342.56 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | -4.11% | -12.86% | 210.50 | 289.00 | -27.16% | 不適用 | 16.57 | 12.70 | 1305.32B TWD / 45.73% | 2026-11-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [整理包／黃仁勳概念股笑了！輝達季度財報超預期 完整台廠供應鏈名單、潛在受惠股一次看 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBQUlViSHpPeDVlY29yaHFNNE5NcVlUQnE3ZThTcXRGNHgxYTVPOVVTRDlaTDV6Zml5WEwxVHNSeGFDcnVHUHhRSW15SzNpU0dYVDU3dThWNEVCbkZI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 21 Nov 2026 08:00:00 GMT
- [愛豐通運布局捷克打造歐洲半導體供應鏈樞紐| 全球中央 - 中央社 CNA](https://news.google.com/rss/articles/CBMiZkFVX3lxTE90QzFlaFNOSmdSN2dOclQ4ZHFoa1JwRERnZ3drZC1ZRjc4eGhVYzNIY0VxdTdGbTdlSlVQVjZoeEFLWXQ0Mi03SkxZcmVGTzcxSURya0Ztb0hCcHE4TGIzNWxQS2NtUQ?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 21 Nov 2026 09:07:00 GMT
- [黃仁勳去職美嚴控 AI 產業，重大事件和供應鏈看法一次看 - TechNews 科技新報](https://news.google.com/rss/articles/CBMi0gFBVV95cUxPRG02Vlh1aDEzd0tlR1k2RGhFVWNpYnE2UXB2cmpIWlRERmhpamQybWVidHAtclg2M09rbmhaMlZ6TGRoWVJ0RE1YQnRXaUZrVGY4aFB2YUt1TGMxS2lHcnBIQTJWRGZDT2h4SFVMOXFraUplNjctOHVNTkNYZ0NFMmgtRUhqVXd4a3ZBYThISlpwb3dxLU1aeHVYNEVjQUtLazJxTFBTY2ZUemFqVU9lWUNGZmhvYmU2WjRYeUczcFFpa2c5cHVuRjV3ZnNvdVpfbGc?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 23 Nov 2026 01:14:31 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：累計EPS大賺73元！「散熱大廠」第三季獲利翻倍成長 輝達Vera Rubin量產帶飛 - Yahoo股市；【即時新聞】最新財報報喜！奇鋐Q3獲利創佳績，單季EPS高達29.32元 - CMoney投資網誌；散熱雙雄戰1》奇鋐、雙鴻同喊明年ASIC超車 輝達獨大局面生變？ - Yahoo新聞

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.33 | -10.73% | -27.47% | 2,150.00 | 3,435.00 | -37.41% | 背離 | 90.78 | 24.38 | 22.10B TWD / 34.35% | 2026-11-01 |
| NVDA 輝達 | 新聞直接提及 | +0.28 | -45.03% | -37.47% | 125.53 | 228.38 | -45.03% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱、奇鋐」，共 3 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：成長。
- NVDA：新聞直接提及「輝達」，共 2 篇新聞命中。 方向判斷命中詞：成長。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [累計EPS大賺73元！「散熱大廠」第三季獲利翻倍成長 輝達Vera Rubin量產帶飛 - Yahoo股市](https://news.google.com/rss/articles/CBMikwNBVV95cUxQa0NTWENQd1d3UDNCYndMaTVlaVh0WFNnZk9GelVHWXVNSmdKWlhtYzU5dlZtVzVJOGs3NG40ZVZfQ2xQeDVKVU1FZDRmd0h6MWNTc3VTekRveEVaanZnZXM1d0tleXNGT3lTRmFHMXNHZmdpOThBekF3eUtWZHUtSHFIX2FLcWh2c0RsUW5QUGtWbVRlQ1FRaGFNbFZ6UzJnY0dlMDZMcWNJQUZMbGZYdXd4QmFMUkUxU3lYako0M0JSLXdTVVA3NzQzVE45ZmVvbHhFRFNrRzJqRW5ud0pHZTVTdmRIcWQwdDc2VXZ0LS1MZVRvODU1bjlFTjZuU09SWHg1MURnQXRrOHRac25nR1lXcVVfT0tJSFJYUVY2VTM2eU5wQXRCVXBVTk1IWVh6T1dOTVRKTlE3elJYaEx3MFFQQTVRWWd0aDRqODBfSEpTSnktZF9TN3Etbld5djR2UEdyMmtjWWNpeXRtMFBKX2Nlbl8xZjlYcWpfR0JRRnZfaERlUllZWWMzREdXWTNORjBJ?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 23 Nov 2026 01:14:05 GMT
- [【即時新聞】最新財報報喜！奇鋐Q3獲利創佳績，單季EPS高達29.32元 - CMoney投資網誌](https://news.google.com/rss/articles/CBMikAFBVV95cUxNQmt6Y3ZONkRBZDVUNy1jdTRtdE9tei0tT3BUYWViRXRhSFJ1QkYzVDRQMWhkNWRTdkg4SDFjVTRzQk1ucFF6U2VMOGtsbVdGcGlJajQ0NVhwQ2I5WjZUMFJnZXBvVEctc2NuT1R4Q2M0SDk5NHZUaU5NWUFHSENMUF9NMWM0RWtnbFhncTFCc3g?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 21 Nov 2026 15:38:13 GMT
- [散熱雙雄戰1》奇鋐、雙鴻同喊明年ASIC超車 輝達獨大局面生變？ - Yahoo新聞](https://news.google.com/rss/articles/CBMi8gJBVV95cUxNektmQm9BLVl0UTlIQ2M1bzNoM2dfX2pFNnVoa2xrOHFaZ0wtRVJoZDNjT0hMUi15b1d0NFVUb2Z0SXA0dE5OMFc5WnhiRk1mbkp6OXJFazJleVNRMWNWSzl0ZmpxUkM4VWdjV2FXZDVIRU9PZWZKZjR1V0V1R2hmT3QySjVua2U1R0w5S2NINVcyMG94dWdFN0lkV25NVXNWRjFHWlN3cGRDNEVpeDNpOXN2YjBPVkZCbzEzRXVoU285X01PeHo5V2Z5eW9paWVqRndfNkZVQUV5V1RIZTdUU1FTd29HRTBLVWY4SFpuSUFENVFVN1g5Sm0zTFY2R3l5NkpESFJYSURkQ2JmanktNUJDM21GcjBBRjZ2RlQ0VU9NSG1kNXFJOGVURkxMU3FuN01pWGFwamZNZGJVbzdtMHdPamtMZUVOTGlGTXhDc1BTVXl6SkVoZEVFZ0VyY3d5Z0h0bEVCUWc0ZGhidy1QRlFB?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 22 Nov 2026 00:14:39 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Intel Q2 2026: Revenue Up 25%, Data Center +59%, Stock Surges Then Retreats to $100 - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.24 | -55.28% | +26.43% | 51.28 | 114.68 | -55.28% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 方向判斷命中詞：surges。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Q2 2026: Revenue Up 25%, Data Center +59%, Stock Surges Then Retreats to $100 - TradingKey](https://news.google.com/rss/articles/CBMiyAFBVV95cUxPSTRQZEVBYzJNekhNS2NEYThtTnBoNEJCcWRZTS1SSFVXYnVfNjdpNndfd2xrWklfM2JvakdWTUdQNjdWaVFDaHl3bEo5WnpwUWZZQWlwdUpfUTZqbUR4R1hHdDhhLVowZU5IYnllc3ZkVTBHcDhGbzg0SERudlh6TVlNc3JPb2FjdkNjNFo1SmkzMFZHcmk0d1A5OERwMlFFeVhrQ1RuSVJVMmd1U3E1Z0toZWN6RWE2c1NkeU9ZejM5cGhJV0pxSg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 22 Nov 2026 14:18:46 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：統一證券：台股有望逐步築底- 新聞 - MoneyDJ；法人盤勢分析內容-台股 - MoneyDJ；美股指數期貨最新報價 8:38-台股 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [統一證券：台股有望逐步築底- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPN3VCQ1htUHhQTnpweXJ1MWpiX29aQW9WM1Z3T0o2aXhpdXVWVGlrSXNXaVZjamhZTUwtTkw1a2h3SWZaSE85ZDZBRVZaMlhwdEs3cnZCa3haTENVMFNwNUwzdllScEcyRWlXZFkzazVzYkpmdUppQVJMMjZJX3NCVVV5VXBfdkVPeU9SS1VCemhZQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 23 Nov 2026 00:40:00 GMT
- [法人盤勢分析內容-台股 - MoneyDJ](https://news.google.com/rss/articles/CBMijgFBVV95cUxPMk9oNjhuSDBaT1piTkoxNFFQWXV5bUViYjVrTFhseHNxdE9DcDdNX0JtV0xjOW1qQlZpeWdZSWJFV3N6OURxS3NpR1NpOXVuMzl0cG5LZHlRMllkU2ktc29FZ2NYWFZhTVpuR1Z1LVdHcWJqcGRIRFNvTTEtM2ZaX2dxNURsQ0h4eHhubTV3?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 23 Nov 2026 00:38:15 GMT
- [美股指數期貨最新報價 8:38-台股 - MoneyDJ](https://news.google.com/rss/articles/CBMiigFBVV95cUxONEFEdzBhWmtTMWt3Wi1PdGVLNW45NTkyZnFSYWV6TG1CUjJxa2JseHpvMV9zQTVVbTZDTXlScmNFQVJSNTF1NnVCd0VlU1liemVUTXdiY1RPTS1oejljWlhUOUpNZXZGWWpIMWMzRUZuS1VoY2I3YUVmSEZUbmk2a0JiX2QzZXlRU0E?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 23 Nov 2026 00:48:15 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
