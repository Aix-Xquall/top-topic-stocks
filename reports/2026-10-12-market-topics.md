# 每日股市熱門話題分析 - 2026-10-12

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **散熱與液冷供應鏈**｜負向｜熱度 2｜市場確認 82.12｜同向 1/1
2. **關稅與供應鏈轉移**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
3. **半導體與晶片供應鏈**｜中性｜熱度 5｜市場確認 N/A｜同向 0/0
4. **記憶體與 HBM 供應鏈**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
5. **AI 伺服器與資料中心**｜負向｜熱度 15｜市場確認 18.92｜同向 3/8

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.08（樣本 12）
- 5日相關係數：-0.07（樣本 8）
- 同向比例：5/12

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 散熱與液冷供應鏈 | 82.12 | 1/1 | 0 | +4.04% | +1.99% |
| 關稅與供應鏈轉移 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 記憶體與 HBM 供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 18.92 | 3/8 | 3 | -2.44% | -3.27% |
| 綜合市場情緒 | 2.91 | 0/1 | 0 | +0.97% | -1.59% |
| 新興題材：TradingKey | 30.91 | 1/2 | 1 | -1.36% | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 相關性偏弱；應提高同向價格確認權重，降低泛 AI、泛半導體等寬標籤推估權重。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-09-29 | 0.31 | -0.78 | +16.67% | 6 |
| 2026-09-30 | 0.05 | 0.04 | +33.33% | 18 |
| 2026-10-01 | 0.21 | -0.27 | +40.00% | 20 |
| 2026-10-02 | 0.51 | 0.37 | +72.73% | 11 |
| 2026-10-03 | -0.35 | 0.13 | +16.67% | 6 |
| 2026-10-04 | -0.12 | 0.70 | +80.00% | 20 |
| 2026-10-05 | -0.16 | 0.29 | +73.33% | 15 |
| 2026-10-06 | -0.72 | -0.75 | +37.50% | 8 |
| 2026-10-07 | 0.48 | 0.61 | +73.33% | 15 |
| 2026-10-08 | 0.13 | 0.40 | +58.33% | 12 |
| 2026-10-09 | -0.03 | 0.37 | +38.89% | 18 |
| 2026-10-10 | -0.28 | -0.96 | +57.14% | 7 |
| 2026-10-11 | 0.66 | -0.74 | +40.00% | 5 |
| 2026-10-12 | -0.08 | -0.07 | +41.67% | 12 |

## 歷史回測摘要

- 回測日期：2026-10-12
- 近5日 3日相關：0.15
- 近5日 5日相關：-0.37
- 同向比例：+45.45%
- 權重狀態：未調整

- 方向準確度：+45.45%
- 信心排序準確度：0.15
- 診斷：弱正相關

調整原因：近 5 日有效樣本 11 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：散熱與液冷供應鏈 相關新聞集中在：Rubin、Trainium、TPU接力助攻！「散熱大廠」9月營收首破200億元 多外資力挺喊買 - Yahoo股市；焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | -0.51 | -4.04% | -1.99% | 3,440.00 | 3,440.00 | 0.00% | 同向 | 75.13 | 45.85 | 21.02B TWD / 44.92% | 2026-10-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 2 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：跌停。

### 主要來源

- [Rubin、Trainium、TPU接力助攻！「散熱大廠」9月營收首破200億元 多外資力挺喊買 - Yahoo股市](https://news.google.com/rss/articles/CBMirwJBVV95cUxQak1YQ1Z2Q3ZqM3JLbWpuSHZTTEhCcEZYb1o5YnpVbFZDV29wSFpGUjIwczhFWlZfcjE2M0Fla2JKUm9GTGNJVHliLTgtQTJtMkhjcGd5SjRuVEtfYUNWUy12OVJTaDR5Qzd2d0FDQWlyVExoeEt3VFlWcTA1aFQtdmZFaEEzWlF0Y180cV9sQkN0NnY2TFJyWFU4Vk9TUTBqOTlwbVJ6NThEeGI1UTZUT2JNVWs1YW44YkRwQmoxWURGRHlZODhfR2RCWVhjcnBTNmVzR0lwYjkzb1NGUTgxS291cGhCX2JkdXFrV0NXNVVIMG1JUGVTaC1GWWdhbm1jaDdTdUpGSkpyOTFlWkY0ZzVXSGZ0Z2lnM01FUnBrVk0xZmFqalJPWnVmZ3p6d2s?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 11 Oct 2026 02:01:35 GMT
- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 11 Oct 2026 21:05:15 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：台灣斯洛伐克簽半導體合作協議助強化供應鏈角色| 國際 - 中央社 CNA；生技重塑香水產業供應鏈，但 AI 仍難完全複製自然 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +7.88% | +20.72% | 336.64 | 336.64 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | -1.97% | -1.97% | 249.00 | 289.00 | -13.84% | 不適用 | 15.21 | 16.41 | 1158.63B TWD / 38.42% | 2026-10-01 |

關聯理由（前 3）：
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [台灣斯洛伐克簽半導體合作協議助強化供應鏈角色| 國際 - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTE91bGwyQjFTejByRlhYTjFlcGE4dXdMeDZrUlYwTU14bDA1N1Vpa0ZCeHAtS05KTW5fTnZ2Z2ZhUnFvdTF1a0ttUHllYzVPbnJMVkhRTTdTZDZMc081bkVr?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 10 Oct 2026 10:15:00 GMT
- [生技重塑香水產業供應鏈，但 AI 仍難完全複製自然 - TechNews 科技新報](https://news.google.com/rss/articles/CBMilgFBVV95cUxNOFhlbnRQUkdZRDZGUWpjMDFVYmZTVHo0WVVYNXViTkl5MjFoQ1lINlQ3dFRhLWlqXzI4OXdNcG5CcWh0Vm1zbFJXVkxSeVFCeEtrMk5XWU5ENjhvaWF3ZFpjeHZSUkN3ekY5ZUN1MllsUHBRMkUxdHZuQjhJSjVMdW8zZEJ2Z0VjY0FFNU0zcHZWRENHY1E?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 12 Oct 2026 00:25:09 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：AI Revenue Questions Pull Semiconductor Stocks Off October Highs - Yahoo Finance；Broadcom vs. Intel: Which Chip Stock Is a Better Buy in 2026? - The Globe and Mail；岩田清文：台日半導體脣齒相依防衛合作應聚焦軍民兩用| 政治 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | -8.70% | N/A | 104.70 | 114.68 | -8.70% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | 0.00 | -2.38% | -4.29% | 361.54 | 446.77 | -19.08% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -0.97% | +1.59% | 2,550.00 | 2,550.00 | 0.00% | 不適用 | 86.28 | 29.56 | 511.86B TWD / 54.65% | 2026-10-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | -3.28% | -8.67% | 147.50 | 164.50 | -10.33% | 不適用 | 6.68 | 22.18 | 25.35B TWD / 27.22% | 2026-10-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +3.85% | +14.59% | 229.28 | 229.28 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | +17.83% | N/A | 608.10 | 608.10 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | +5.97% | N/A | 1,029.00 | 1,029.00 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -4.74% | -8.03% | 1,581.82 | 2,335.00 | -32.26% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AVGO：新聞直接提及「Broadcom」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 2 篇新聞出現相關標籤。

### 主要來源

- [AI Revenue Questions Pull Semiconductor Stocks Off October Highs - Yahoo Finance](https://news.google.com/rss/articles/CBMipwFBVV95cUxNbnZpNHVtZUNtSDNTZ3g1Nl9oVXg4alBDTU91bE9rZWl6VEs5VU9KeHpDUjVEUWFBUWUwN3JPR2FPZDhuS19XOENSaVVvWVA5bExTV3lLZFc5elNWNGVqeEZpUk1rU2xQa29zNE9zc3MxZERHRFl2dVh1MWtka0Z3OXdnYmMwRkVHd2xpcUFlQjZOWWFYOHlYa09uNFIzNFBRLVNSTkxGMA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 10 Oct 2026 16:38:00 GMT
- [Broadcom vs. Intel: Which Chip Stock Is a Better Buy in 2026? - The Globe and Mail](https://news.google.com/rss/articles/CBMi2wFBVV95cUxOdVBSRGZlVWwtWHF6RU5xR2VDcTh0eWxLb2pLRnlrRFBBZmtsbFpzU0cxbkY4WHVvU2hrSUtLT2EwMWRRejRyU2RaQXFVb2VUNEdjbGlGNlQ4Rl9GeDlPV3hBUlZCdmNMSXFHV3NkTm9tWm9QVGxCWTk5N2Z2d2d6QVhsUjREN1VYRWRaR2RRdE9GdnNScEJZd2JpMTlwUmtTSnhBN0V0eEowY29telAwOWMtTS1xYVRtUXBEdjdPWkpwRTREazNKMGV3bWFPNWdITnlTTFBaMVNQUWM?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 10 Oct 2026 15:35:00 GMT
- [岩田清文：台日半導體脣齒相依防衛合作應聚焦軍民兩用| 政治 - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTFAxQUg0a3NwMTFfRnhURXBPM19fQWhPYWRwM01HYkliN3hwTnoybnc0ZlhoYnpHUk9Bd3hkY1hrU0RpSHVSdHFLZGhHT01rS2xrRlFfQ3REdldXbS1HbDNj?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 11 Oct 2026 06:18:00 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：INTC, AMD, MU, NVDA: Chip Stocks Tumble Again, Stalling A Nascent Rebound - Stocktwits；Micron Technology Inc (MU) Stock Analysis & Forecast - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | +5.97% | N/A | 1,029.00 | 1,029.00 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +3.85% | +14.59% | 229.28 | 229.28 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | +17.83% | N/A | 608.10 | 608.10 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | 0.00 | -8.70% | N/A | 104.70 | 114.68 | -8.70% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -4.74% | -8.03% | 1,581.82 | 2,335.00 | -32.26% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU」，共 2 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVDA」，共 1 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [INTC, AMD, MU, NVDA: Chip Stocks Tumble Again, Stalling A Nascent Rebound - Stocktwits](https://news.google.com/rss/articles/CBMizAFBVV95cUxORHdiV3k3V2RtSVBoRTJaaW5PcTZhQzBTNlRUM2VqcjBpcTViNkREdS1uVGtnb1FYckxkREh4Z00zN2NBSnlNRGZ0SWhpNERydkZKTlJCejRLQ2xqejNxREhfS1ZzSm5CdjhrZzlZTnRiN1Z6M3VtSDU1d2trMG9jVFUwT3hadk93R2l0TlBBZkttekkyTDBHTW1Zc01YTmNzRVJ3Tm11dGcwNktNX04yU0pLUENBQl9sOUI4dVMydW02UUhxZDVXX2pZT0M?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 10 Oct 2026 17:07:24 GMT
- [Micron Technology Inc (MU) Stock Analysis & Forecast - TradingKey](https://news.google.com/rss/articles/CBMiY0FVX3lxTFB2cjlJNEFoZnN6al9fVWlOSktTV2tWRzJ1c0c2SklreGhaeHF5VlZlSjNNRE1SaXlnaUVsQ1FaMXFtZUlvM19kUzhHdURNU1VkNmNhLTNPSDNtXzBpSHNZS0xkNA?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 10 Oct 2026 02:56:02 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：AI Revenue Questions Pull Semiconductor Stocks Off October Highs - Yahoo Finance；Is Terafab AI Role Altering The Investment Case For Intel (INTC)? - Simply Wall Street；「AI 美元」時代來臨，科技巨頭獲利能力將成霸權新考驗 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.54 | -8.70% | N/A | 104.70 | 114.68 | -8.70% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 新聞直接提及 | -0.25 | +18.84% | +8.75% | 535.07 | 535.07 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | -0.03 | +3.85% | +14.59% | 229.28 | 229.28 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | -0.03 | +17.83% | N/A | 608.10 | 608.10 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.04 | -0.97% | +1.59% | 2,550.00 | 2,550.00 | 0.00% | 未明確 | 86.28 | 29.56 | 511.86B TWD / 54.65% | 2026-10-01 |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -2.38% | -4.29% | 361.54 | 446.77 | -19.08% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.03 | +0.27% | +4.79% | 744.00 | 744.00 | 0.00% | 未明確 | 13.92 | 53.84 | 82.25B TWD / 45.66% | 2026-09-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.04 | -9.20% | -5.82% | 4,690.00 | 4,920.00 | -4.67% | 同向 | 60.69 | 77.46 | 55.40B TWD / 1.97% | 2026-10-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MSFT：新聞直接提及「微軟」，共 1 篇新聞命中。 同時符合主題標籤：AI, datacenter。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AI Revenue Questions Pull Semiconductor Stocks Off October Highs - Yahoo Finance](https://news.google.com/rss/articles/CBMipwFBVV95cUxNbnZpNHVtZUNtSDNTZ3g1Nl9oVXg4alBDTU91bE9rZWl6VEs5VU9KeHpDUjVEUWFBUWUwN3JPR2FPZDhuS19XOENSaVVvWVA5bExTV3lLZFc5elNWNGVqeEZpUk1rU2xQa29zNE9zc3MxZERHRFl2dVh1MWtka0Z3OXdnYmMwRkVHd2xpcUFlQjZOWWFYOHlYa09uNFIzNFBRLVNSTkxGMA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 10 Oct 2026 16:38:00 GMT
- [Is Terafab AI Role Altering The Investment Case For Intel (INTC)? - Simply Wall Street](https://news.google.com/rss/articles/CBMiygFBVV95cUxOcGtldWVQWjNZUWJ6c0NFU3hVay1iOThiWUZxckhMeFlUVW1CeTdNalVvMTE1bVMzVGp5QWpORGprMmZPWG5PTGtZNnpwSnFBemx2SzJqY0NVLWEySV9lR2Via2RNV2pHT1dSS0liTkxlT2Zma2ZCclFBSTkzNlZYdWgwelYwWGVQVU9OOVpHV2k5LUhTMlBkRHNaSXBXbFlWbWRnaUlLUUtxRDE4WjlVSTFDVHRUai1ZMEptcHViZUdiWE1kdklQbXdR0gHPAUFVX3lxTE1UdnBWNW5aQU5pQjhaamF5UkgwOE5LRFI4V2JTc3ZrN2tiZjVBeXBiMkkwQUUwMU5iZW9VTHY3b2xveDBqWWlLYUNuZmw0M1FWd1ZNN3N5WE1pUFIwOVBIZVNldnU0bVQ2MzYtNHIxN2puWHVaUHUwRFZNQXRRLVdObzgxOGdXZWhVWXc2TzlYRFRaQk9UTkxjZnlFbzhtem9qTmtEdzExVEpmMktlbTNiYWlQd1ptNFNFYkVnUXVYTm1PS1BxcHpadnFLZ1dDOA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 10 Oct 2026 08:40:44 GMT
- [「AI 美元」時代來臨，科技巨頭獲利能力將成霸權新考驗 - TechNews 科技新報](https://news.google.com/rss/articles/CBMie0FVX3lxTE1Yb1pMSGljLXN1TzdFM3VxRnVDcmV1ZERWTngtU1FuQjZWOV9SOGR0d0ZpUWJpRGRCMHdMUHRVdFZKSnYxa0VmNDJldU9BeXhCTV9XWEJVV05Gb3drdlJ2Yk5wNUZXbWZxU1pfVFF3NFlIdDNLZThxTnFqbw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 11 Oct 2026 23:41:29 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股散戶追價 融資水位急升 | 市場焦點 | 證券 - 經濟日報；台股高檔震盪加劇 16檔站穩所有均線強勢股 多頭人氣匯聚 | 市場焦點 | 證券 - 經濟日報；台股 ETF 人氣大噴發 近一周多檔受益人數紛紛創高 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | -0.32 | -0.97% | +1.59% | 2,550.00 | 2,550.00 | 0.00% | 未明確 | 86.28 | 29.56 | 511.86B TWD / 54.65% | 2026-10-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。

### 主要來源

- [台股散戶追價 融資水位急升 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxQS28xOXdQMkVXZEY3UHptSzJIeXFqWTBPemwyaEhQVkFTV3BYMS15V0IxRm9XUjE2Y09tbW5UNVdudWU5RDRic0w3bXBvY0VPX3VPQVpmMG1qeFNGR1JSVHYzSmc4eGRvbVhLdjU4UVRwT0sxdUVTX2pmYk40eVhmZQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 10 Oct 2026 09:00:00 GMT
- [台股高檔震盪加劇 16檔站穩所有均線強勢股 多頭人氣匯聚 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBQcjRWc1l4UUhKRmdHTm9DTjZZVGFoVGxXc1VTX0FPdmtpMGo1OFZJVmtfSlZRejF5WG8tT0JPVTFnNUVlRGhISDN5U3pnRmFxSngwOVN4WG42dw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 11 Oct 2026 15:30:16 GMT
- [台股 ETF 人氣大噴發 近一周多檔受益人數紛紛創高 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1oQXotanlIYTlNWjZNcmswZlFYb252XzN3NlVzV09zX2RzcTBiRVYtVV81OHhXSHB3eXlfSW5wT0RPYXBmbV9INjhHLUpYNnNPOTAxdk1UM1MtZ9IBX0FVX3lxTE8xTkVTbk1ROUpQNzhob0VPcFBlVUdSZ1QtR0Q4T2xjeEhCRmpwR3Z5ZU9odHBZNmJZNDR2UEE4TFAtU0x5akFaZ2JrcDgwWEhOenBXT2JFNEI3NFlLMG04?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 11 Oct 2026 16:37:47 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Intel Q2 2026: Revenue Up 25%, Data Center +59%, Stock Surges Then Retreats to $100 - TradingKey；Micron Technology Inc (MU) Stock Analysis & Forecast - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.21 | -8.70% | N/A | 104.70 | 114.68 | -8.70% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 新聞直接提及 | +0.42 | +5.97% | N/A | 1,029.00 | 1,029.00 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 方向判斷命中詞：surges。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MU：新聞直接提及「MU」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Q2 2026: Revenue Up 25%, Data Center +59%, Stock Surges Then Retreats to $100 - TradingKey](https://news.google.com/rss/articles/CBMiyAFBVV95cUxPSTRQZEVBYzJNekhNS2NEYThtTnBoNEJCcWRZTS1SSFVXYnVfNjdpNndfd2xrWklfM2JvakdWTUdQNjdWaVFDaHl3bEo5WnpwUWZZQWlwdUpfUTZqbUR4R1hHdDhhLVowZU5IYnllc3ZkVTBHcDhGbzg0SERudlh6TVlNc3JPb2FjdkNjNFo1SmkzMFZHcmk0d1A5OERwMlFFeVhrQ1RuSVJVMmd1U3E1Z0toZWN6RWE2c1NkeU9ZejM5cGhJV0pxSg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 11 Oct 2026 12:45:06 GMT
- [Micron Technology Inc (MU) Stock Analysis & Forecast - TradingKey](https://news.google.com/rss/articles/CBMiY0FVX3lxTFB2cjlJNEFoZnN6al9fVWlOSktTV2tWRzJ1c0c2SklreGhaeHF5VlZlSjNNRE1SaXlnaUVsQ1FaMXFtZUlvM19kUzhHdURNU1VkNmNhLTNPSDNtXzBpSHNZS0xkNA?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 10 Oct 2026 02:56:02 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：法人盤勢分析內容-台股-MoneyDJ理財網 - MoneyDJ；法人專欄分析內容-台股-MoneyDJ理財網 - MoneyDJ；個股主力券商-6122 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [法人盤勢分析內容-台股-MoneyDJ理財網 - MoneyDJ](https://news.google.com/rss/articles/CBMijgFBVV95cUxPSHgxOUZ5TThZMGtrMlpvQ2k4blZzQUlSVFplczNVODVIZmpnRklMZWhILUwtdTNKbUtnd3F0LVdhWC0teU1jS1YtaHFuU3RVMTI5eFh5a1pHWkhtU2FLOWZtZU5zczFIOU16RXNJX1lwd241TTJja0lnaVdVa1VOSmJZWmt5U0FCYU10Q25B?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 12 Oct 2026 00:21:04 GMT
- [法人專欄分析內容-台股-MoneyDJ理財網 - MoneyDJ](https://news.google.com/rss/articles/CBMilgFBVV95cUxPXzRTX1FmeU5iYTlrRk1BeDd3ODNfTld2aEUtUHd6M0tPdDFEMHhndTl5T3d1WEJFY1Z3SUJKRWNTSzNQZExsTlU2X0wxVF9HWU1CWThocklWMmhtSk55OXhrVC1EV0VOcUV1VFFCdl9nQXZpT1RFeEItUnF3ZUpyb1dZQnExVGdGcE5vTUc0Zy1vOGJxM3c?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 11 Oct 2026 16:02:32 GMT
- [個股主力券商-6122 - MoneyDJ](https://news.google.com/rss/articles/CBMimwFBVV95cUxQa2xsU3ZfcVBYRzNpV1V5aW5jOGNBb3BmUURQcmd0VFh6Snp3c0d0bWNmQXhaMXo1QUV4Rnl6aEw4N2UwN3J1SnM2SVFfZ1BsOHlxMDNBVEFJWWx2djVCZHB3Tm5XOEx2NFR0S2tKd3dDVU9HajVrck52MnZoalNldXVSTDJTSm5jckd0bUdZVmhQS2FPXzkxQzNucw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 10 Oct 2026 10:38:18 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
