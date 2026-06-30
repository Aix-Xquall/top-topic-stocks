# 每日股市熱門話題分析 - 2026-07-01

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **半導體與晶片供應鏈**｜負向｜熱度 9｜市場確認 53.32｜同向 3/5
2. **綜合市場情緒**｜負向｜熱度 37｜市場確認 0.00｜同向 0/1
3. **散熱與液冷供應鏈**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0
4. **關稅與供應鏈轉移**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
5. **新興題材：AI散熱**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.08（樣本 13）
- 5日相關係數：0.25（樣本 13）
- 同向比例：4/13

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 半導體與晶片供應鏈 | 53.32 | 3/5 | 0 | +3.77% | -8.09% |
| 綜合市場情緒 | 0.00 | 0/1 | 0 | -0.84% | +3.21% |
| 散熱與液冷供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 關稅與供應鏈轉移 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：AI散熱 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 7.24 | 1/6 | 3 | -1.48% | -0.35% |
| 記憶體與 HBM 供應鏈 | 0.00 | 0/1 | 1 | -2.62% | +15.79% |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 相關性偏弱；應提高同向價格確認權重，降低泛 AI、泛半導體等寬標籤推估權重。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-06-18 | -0.41 | -0.41 | +42.86% | 7 |
| 2026-06-19 | 0.06 | -0.04 | +57.14% | 7 |
| 2026-06-20 | 0.29 | 0.21 | +63.16% | 19 |
| 2026-06-21 | -0.01 | 0.32 | +55.56% | 18 |
| 2026-06-22 | -0.87 | -0.87 | +100.00% | 3 |
| 2026-06-23 | 0.38 | 0.01 | +62.50% | 8 |
| 2026-06-24 | -0.38 | -0.11 | +25.00% | 12 |
| 2026-06-25 | 0.10 | -0.21 | +20.00% | 5 |
| 2026-06-26 | 0.08 | 0.04 | +25.00% | 16 |
| 2026-06-27 | 0.12 | 0.29 | +57.89% | 19 |
| 2026-06-28 | 0.16 | 0.55 | +85.71% | 14 |
| 2026-06-29 | 0.49 | -0.25 | +38.46% | 13 |
| 2026-06-30 | 0.44 | -0.27 | +62.50% | 8 |
| 2026-07-01 | -0.08 | 0.25 | +30.77% | 13 |

## 歷史回測摘要

- 回測日期：2026-07-01
- 近5日 3日相關：-0.28
- 近5日 5日相關：-0.15
- 同向比例：+33.33%
- 權重狀態：未調整

- 方向準確度：+33.33%
- 信心排序準確度：-0.28
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

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel, AMD Jump 7% as Chip Stocks Catch a Risk-On Bid - 24/7 Wall St.；亞大外文系把半導體變成新語言 - 中央社 CNA；韓國砸重金挑戰台灣半導體邱銘乾：中小企業活力難複製| 產經 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.58 | N/A | N/A | 139.63 | 139.63 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.53 | N/A | N/A | 580.91 | 580.91 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.04 | +0.84% | -3.21% | 2,370.00 | 2,370.00 | 0.00% | 未明確 | 74.39 | 32.40 | 416.98B TWD / 30.09% | 2026-06-01 |
| 2303 聯電 | 產業/供應鏈推估 | -0.05 | -7.84% | -3.24% | 164.00 | 164.00 | 0.00% | 同向 | 4.00 | 41.33 | 22.94B TWD / 17.78% | 2026-06-01 |
| NVDA 輝達 | 產業/供應鏈推估 | -0.03 | +0.26% | +12.92% | 200.09 | 211.14 | -5.23% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | -0.04 | N/A | N/A | 1,154.29 | 1,154.29 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | -0.04 | -2.62% | +15.79% | 2,273.73 | 2,335.00 | -2.62% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -9.51% | +18.21% | 377.75 | 446.77 | -15.45% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：risk。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：risk。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 1 篇新聞出現相關標籤。 方向判斷命中詞：risk。

### 主要來源

- [Intel, AMD Jump 7% as Chip Stocks Catch a Risk-On Bid - 24/7 Wall St.](https://news.google.com/rss/articles/CBMimwFBVV95cUxPUTRGOGMwMUZfbkVVbXByR0FjbDc0MXZfeDV3WmdfbVFXbGtONWNEZHFIVzhVV0ZyQmRDcERTNHZOcUdfYjE5dGUzcDhuT2hyZDFOWXZ3YWlPM3FRd19ZWjlEYzJmSWJZd3BFR0lOQm14OThMOEZRV3lfQ1FJTWVFMlJvN01tQ3pNS2E0c2NOU0JIclhLSHNPdkgyMA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 30 Jun 2026 16:18:10 GMT
- [亞大外文系把半導體變成新語言 - 中央社 CNA](https://news.google.com/rss/articles/CBMiVkFVX3lxTE9pSzZXWGh2V0M5TkphZFZ4bThxSWFjMXB5RUJLaG81ZWZMUjFzU2czV0NtTnRWRkVQWm43Zk5RWnlnZnB3djJxNl85QU51andQMkNSd1JB?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 30 Jun 2026 07:35:01 GMT
- [韓國砸重金挑戰台灣半導體邱銘乾：中小企業活力難複製| 產經 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE9ldE9JTHEzUmRuemlfR1F0MlhmWldaRWNZalNSREdKNlBDcG9ZM184SEFjNE9DQ01BdS1TTHctbnFKdVVDcDVITzNJQ2FzTXMzdmQ0b3E4Y3N0ejhtS2c?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 30 Jun 2026 08:03:00 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：鉅額交易仙人指路！台積電爆2,585元新天價 助攻台股劍指 48K 大關 - 經濟日報；34檔台股 ETF 熱 - 經濟日報；台股基金 犀利 | 基金天地 | 理財 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | -0.36 | +0.84% | -3.21% | 2,370.00 | 2,370.00 | 0.00% | 未明確 | 74.39 | 32.40 | 416.98B TWD / 30.09% | 2026-06-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。

### 主要來源

- [鉅額交易仙人指路！台積電爆2,585元新天價 助攻台股劍指 48K 大關 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9ycnUyYUd3eDlmQkw5ZmJOWERUQmx0cUVPdDdlY29qM3I5eHk2UkppTklsdWRPNTF0dUdaMXNVWjNMbmtYX0dkb2VZUGt0bGVPZjVMaVRyY2prZ9IBX0FVX3lxTE4wS0tYVFlDX1NYdUl3RnQ0RDlEejd6eGdoQmg1TEhZQUVDVEpFdmYtbGRPS3JVVEpqdG1QLWROQXhYT1Y3Y2VXYXRtMER1c0lMaDY1XzRaN2hmV0ZPZWdJ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 30 Jun 2026 11:44:40 GMT
- [34檔台股 ETF 熱 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5JTGlERGhEdWw2YW5YWWVMLS00c285UEtQMXNHdHd1dVpFNzJqb01hUTJjYmtuOVlrNmlHQUlYWUFUOWM3R0ZES0I5akRJeEgwNU5fVmw5Y1lHd9IBX0FVX3lxTE5TMTd1aDZiQmhCUFlPdk5nMFhYYmR1cVRxZnJBbjhieUJ2SlpkLTY1dDlfM29xR3g3bk5FdlV6bDdsV2V1RFVjVjRib2xOV1lmT3hCbGVXM3c5eHlKTS1z?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 30 Jun 2026 16:38:08 GMT
- [台股基金 犀利 | 基金天地 | 理財 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxQbi1NZmpxSl9XU0NXOGYtSTZtZ21iOHJMcnoyRGRtaEhPb05YSXBZOEl0RnBhVzFnVHJFdzFTdmtGTlVhTFNCQmlZZHVma3J3QlgwQTlpX0lwVHBQY0wtckR4TEtiUjRKR3hSVExfQTZQUU10WFlTMWM4OUVLVTVYUg?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 30 Jun 2026 17:43:51 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報；ASIC/VeraRubin出貨升溫，奇鋐看旺下半年動能 - 台視全球資訊網；AI散熱廠奇鋐一度漲停！訂單直達2029年 看旺下半年動能 - 緯來新聞網

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | +0.80% | +4.12% | 2,300.00 | 2,835.00 | -18.87% | 不適用 | 61.06 | 41.49 | 15.87B TWD / 60.64% | 2026-06-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱、奇鋐」，共 3 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：跌停, 漲停。

### 主要來源

- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 29 Jun 2026 20:42:39 GMT
- [ASIC/VeraRubin出貨升溫，奇鋐看旺下半年動能 - 台視全球資訊網](https://news.google.com/rss/articles/CBMikgFBVV95cUxNZ3A0cUdtMmx3LVJvbUZlRVNWTURxNENIYlFuX3NqQ1MxaWtCUjNBNWl3Q0NHMjhjZ3BIbXRKaWR0Nk1mSEZ0ZEVQcnZ5WF9QN2V0bWlIUGhZU1h1VGZoQW83MEJCTm92ZkljZ2ZSTTlFVjIyUUMwN1pQU0FpUmRnUFF0X2ZUQmhtelJpblFucjA3UQ?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 30 Jun 2026 06:20:18 GMT
- [AI散熱廠奇鋐一度漲停！訂單直達2029年 看旺下半年動能 - 緯來新聞網](https://news.google.com/rss/articles/CBMihgFBVV95cUxNb29xS092VmZKM0NYQ2FzQkhvTE9GMVlxRExmclA3bzhkUU13U3J0X1dpZlRqQ080OUlicFFhNnJkN2NuSnJ2TV9wbjJMb1YwT2dRdk1EOElrZ05TRnpmYnlrWGtNN0Y2T2tQdmVRZTQ5SU8wZTNUSmVUbDlFSGJHcnBkWHRodw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 30 Jun 2026 09:41:00 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：傳台積電結盟華邦電，專家：強化 AI 供應鏈自主能力 - TechNews 科技新報；Nike results top estimates even as China sales drop 12%; retailer expects $986 million tariff refund - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | 0.00 | +0.84% | -3.21% | 2,370.00 | 2,370.00 | 0.00% | 不適用 | 74.39 | 32.40 | 416.98B TWD / 30.09% | 2026-06-01 |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +9.53% | +24.65% | 289.36 | 312.06 | -7.27% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | -2.52% | -3.28% | 246.50 | 289.00 | -14.71% | 不適用 | 14.13 | 17.83 | 859.41B TWD / 39.57% | 2026-06-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 1 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 1 篇新聞出現相關標籤。

### 主要來源

- [傳台積電結盟華邦電，專家：強化 AI 供應鏈自主能力 - TechNews 科技新報](https://news.google.com/rss/articles/CBMilgFBVV95cUxQT3JEb0ktSXhOdjlMRXVRX0twVWhsaGRxdkt6eXZJd1hka1RMUEVIaTE0MWp4M3I4UVBhemhYR1pzSm92aEs2MUpWci1vY3FoQ1pYRHFONU8tQXJwRXp4X0RBaXQyX1NRX2dYcVFGbWxVTUEtWFk2U1llSnhRRThKMjZydC0zSjJYRENFNi16cHI4THZYbHc?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 30 Jun 2026 06:47:32 GMT
- [Nike results top estimates even as China sales drop 12%; retailer expects $986 million tariff refund - CNBC](https://news.google.com/rss/articles/CBMib0FVX3lxTE1xQWRJOWN6aWhPdk9WYklzclNNYWhqQXlraUJocHdEbEEyTkw5Rm51RGhobjZHNmlBWE51ZDI0Yl9waWNfT29kTDZNbTZkcWhfY0tObFZSTU0yUFNjWk5QUDB5XzhEVllkS1U1Qzl1d9IBdEFVX3lxTE5KanlrN3ptZ2g3UV9XT3BHMGxDOXIwNy13ZDczMjhNOVJsdXhVMEt6LWh6bTRHN3ZPb0FTVlVRQ1EzbUh2dkdkQlZwVWJFcTZuUmtIZFlOd1hvN3oxaE93YU0wVng1d1Bqa29GOWZvYnlCWEpG?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 30 Jun 2026 16:00:01 GMT

## 新興題材：AI散熱

摘要：新興題材：AI散熱 相關新聞集中在：焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報；AI散熱廠奇鋐一度漲停！訂單直達2029年 看旺下半年動能 - 緯來新聞網

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | +0.80% | +4.12% | 2,300.00 | 2,835.00 | -18.87% | 不適用 | 61.06 | 41.49 | 15.87B TWD / 60.64% | 2026-06-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱、奇鋐」，共 2 篇新聞命中。 方向判斷命中詞：跌停, 漲停。

### 主要來源

- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 29 Jun 2026 20:42:39 GMT
- [AI散熱廠奇鋐一度漲停！訂單直達2029年 看旺下半年動能 - 緯來新聞網](https://news.google.com/rss/articles/CBMihgFBVV95cUxNb29xS092VmZKM0NYQ2FzQkhvTE9GMVlxRExmclA3bzhkUU13U3J0X1dpZlRqQ080OUlicFFhNnJkN2NuSnJ2TV9wbjJMb1YwT2dRdk1EOElrZ05TRnpmYnlrWGtNN0Y2T2tQdmVRZTQ5SU8wZTNUSmVUbDlFSGJHcnBkWHRodw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 30 Jun 2026 09:41:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：是方捲 AI 伺服器走私案澄清：僅提供機房服務，無涉客戶設備買賣 - TechNews 科技新報；AWS 執行長：以 AI 取代初階員工是「最愚蠢想法」，這種公司有天終會自爆 - TechNews 科技新報；Amazon’s AWS commits $1 billion toward new unit for embedded AI engineers - Reuters

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | +0.08 | N/A | N/A | 139.63 | 139.63 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.04 | +0.26% | +12.92% | 200.09 | 211.14 | -5.23% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.06 | N/A | N/A | 580.91 | 580.91 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.04 | +0.84% | -3.21% | 2,370.00 | 2,370.00 | 0.00% | 未明確 | 74.39 | 32.40 | 416.98B TWD / 30.09% | 2026-06-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.02 | -5.02% | -26.38% | 373.02 | 506.69 | -26.38% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -9.51% | +18.21% | 377.75 | 446.77 | -15.45% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.04 | +6.08% | +2.72% | 627.00 | 627.00 | 0.00% | 同向 | 10.86 | 63.14 | 63.03B TWD / 28.57% | 2026-06-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.02 | -1.51% | -6.39% | 3,910.00 | 4,310.00 | -9.28% | 背離 | 62.91 | 67.65 | 47.43B TWD / 4.99% | 2026-06-01 |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [是方捲 AI 伺服器走私案澄清：僅提供機房服務，無涉客戶設備買賣 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiYEFVX3lxTE9EdUtfNVdtdHRaNHFNaHdLT0pIMllkZDhqTVpPQ1ZhSTVhMzRVUXlrTWN0MjZuZ0Z4YnUyY01FeXdLV2Q5NkhwVUxxSVVDOTZUUUhpYmtFck4yX09JcTRiQw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 30 Jun 2026 01:56:45 GMT
- [AWS 執行長：以 AI 取代初階員工是「最愚蠢想法」，這種公司有天終會自爆 - TechNews 科技新報](https://news.google.com/rss/articles/CBMitgFBVV95cUxPWHMzWDlyQ0xjUlpHbnVUZHhiMnhpeWRqY0NYVnd5aF9nemVjU3ZuSU5WLWZuN1pqZWlDdzd6SWFHQnREZ0NUUmpudEQwcXRTZHhEQmFLaEx4WHhEV3ZkWVIzcGpMVDc3YURiczFNNVVOVWtQOW9VSEFVQzE4eW5YQmlDdVBydzFyN3owR2FCU3JVazYxYWVnOEFXaUtXWDFuUVJOcXZqTmRXRzBmcjlfU1NWVGotZw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 29 Jun 2026 03:34:24 GMT
- [Amazon’s AWS commits $1 billion toward new unit for embedded AI engineers - Reuters](https://news.google.com/rss/articles/CBMixwFBVV95cUxNUnN2ZVVJdDBidHNmQklYVW9kTC1ORjFFNVA5UTlRelBoRFRLWWM0ODllUzN0UkJBX2ZpNmRtRl9Gd2FFZ2R0aV94M1FpOVNIaE9PS1pEbm1aZk9xMFVxR00wdUpsLVczVXRhMDc5S1hfdUhBUzNVT1htTTZvTm9EOXNTd2NlNFNzdlZoXzU4ZFpMMzNYWm8wU3VqWXVMMml1Z0pPYzV2eUpPNlBpcURIQjhuYi1Xc2lCRkh1bmxWWXhUQkNuWjBV?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 30 Jun 2026 15:15:56 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits；AI Memory Stocks Micron and Sandisk Are Up 200% in the Last 3 Months. History Says This Will Happen Next. - Yahoo Finance；Sandisk: Micron Confirmed The Memory Supercycle (NASDAQ:SNDK) - Seeking Alpha

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.65 | N/A | N/A | 1,154.29 | 1,154.29 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.33 | -2.62% | +15.79% | 2,273.73 | 2,335.00 | -2.62% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.48 | N/A | N/A | 580.91 | 580.91 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.48 | N/A | N/A | 139.63 | 139.63 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +0.26% | +12.92% | 200.09 | 211.14 | -5.23% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron、Micron Technology」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally, surges, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk、SNDK」，共 5 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：surges。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits](https://news.google.com/rss/articles/CBMi0AFBVV95cUxOWm5KdEIwSXpyY191UEhDa1V6NVpWa01UbmpJeWRIV0ttT080TmpDNEhISW5TWkQwUzBVYzBqSHJPWXRVNVJCampoWWRlYmhKVkhIeHBJLS0wLW5Ua09GQnRORXpFcW5qTEJkcnJGcW55aU5rOFVOLUFMbjRPZEpWT3A2ZllucnM0SU9JNEdrNUwyc3V2WHAtNFk3VHl4R1F6SkZRMFpleEE2Zl9MdW4tSEpMMnFGZ2hQZURWQ3B1WDlPR1BhRjJELVN5ODJWYVR3?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 29 Jun 2026 13:21:22 GMT
- [AI Memory Stocks Micron and Sandisk Are Up 200% in the Last 3 Months. History Says This Will Happen Next. - Yahoo Finance](https://news.google.com/rss/articles/CBMinAFBVV95cUxQenR4YzFrTnM2V0lNNzRqaWU2NjlCd1pQd0Uta3RFdzVUX29oTWIyam8wbHFzWnFjcmVldHNTYWI2YUQwVTk2MnJqaENvYUFoSmg3TEM0ay13NnVZc1JOOW9JdWphU0MxeFgyR2EtQ2Q4NTRScjB0MFRGSm9zOWtqMG9nY240aFdKWGhDT05zRXBTMkNfLUNITnFhNnk?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 30 Jun 2026 08:32:00 GMT
- [Sandisk: Micron Confirmed The Memory Supercycle (NASDAQ:SNDK) - Seeking Alpha](https://news.google.com/rss/articles/CBMikAFBVV95cUxNcDUzM1JHTWhEWjRtQmtTRTFnNDJRenJTU1o0eDM5NThCZng3VlhQUVk2Y2pKU1Vhd0szOG44dDVsZmZ0aEdyWWdlT3FqbEpoZ0VadWVmeHdKLXZ4dVVtNnp0aDhMcHMzNm80QlNvZDBCMHU5MHZsSlFIcFJwVU5HSkphU0lXZmVFdy1ndldQTUg?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 30 Jun 2026 12:27:47 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》收漲1126點/重返10日線 月K連三紅/Q2漲45% - MoneyDJ；統一證券：台股應避免過度槓桿，提防高波動- 新聞 - MoneyDJ；00685L今年來漲幅居台股ETF之冠，將1拆24 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》收漲1126點/重返10日線 月K連三紅/Q2漲45% - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQSmdGTG1pQzZnaWRkZlRPOHg5d1ltQXRITFpnaTJhaG9WWEl5V211RDE3dk8tblJjRUF5dkpfLUZHWktHODNmS0ZUNFJEV1IyNjYzSnBncm5ldV9yZUlWN0pGdjNNSFduTXZmaXdKbDRUTGZhUmhhQUluWVZxM0hlQTNxTUI2VDVicWVVUzIxOUFDdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 30 Jun 2026 07:37:00 GMT
- [統一證券：台股應避免過度槓桿，提防高波動- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNTWFDTDA0T09US3F4dUpRcEQwbUEtNWZ5b2dmd1d3emVRUGZIaUEzV2xINEFYc1l6bUY4ZW5kWGt1M0NKZ2U2bWh2OXUyMlNUSzgyUU1BYWxZczBoQVFqSFNHMGxHWXl5b2lsalp0V2pSdEhMQlFiUUFZME54d2wyU1V6Und3STlfSDY3Sk5yMVN0UQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 30 Jun 2026 00:32:00 GMT
- [00685L今年來漲幅居台股ETF之冠，將1拆24 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQOU54UnpKNTZ2Z1hucVRhd0tvVWFRaWFEX2QwVEZuTmN5RjljTVMyclpISy1qbzQwRTRrNWNwT2h3aDNibnZ6Y2ZMaUVXUlA1MGZZWGxVUlhLd2t5VVN6eWRRd3d0OG5nZmRxZ09mTWNFbDhMcWRtTV9DSUlXV2Y5cjk4REVTd3R0RUlCQm9LZFJjZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 30 Jun 2026 02:34:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
