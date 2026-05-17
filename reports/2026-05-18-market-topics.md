# 每日股市熱門話題分析 - 2026-05-18

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **半導體與晶片供應鏈**｜中性｜熱度 8｜市場確認 N/A｜同向 0/0
2. **AI 伺服器與資料中心**｜正向｜熱度 11｜市場確認 43.05｜同向 2/6
3. **散熱與液冷供應鏈**｜正向｜熱度 1｜市場確認 65.00｜同向 1/2
4. **新興題材：TradingKey**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0
5. **記憶體與 HBM 供應鏈**｜正向｜熱度 4｜市場確認 0.00｜同向 0/1

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.01（樣本 9）
- 5日相關係數：-0.17（樣本 9）
- 同向比例：3/9

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 43.05 | 2/6 | 3 | +6.57% | +5.43% |
| 散熱與液冷供應鏈 | 65.00 | 1/2 | 1 | +13.31% | +9.15% |
| 新興題材：TradingKey | N/A | 0/0 | 0 | N/A | N/A |
| 記憶體與 HBM 供應鏈 | 0.00 | 0/1 | 1 | -3.06% | -9.90% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：EagleRock | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：首季營收 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-05-08 | 0.03 | 0.48 | +76.92% | 13 |
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

## 歷史回測摘要

- 回測日期：2026-05-18
- 近5日 3日相關：-0.03
- 近5日 5日相關：-0.09
- 同向比例：+45.45%
- 權重狀態：未調整

- 方向準確度：+45.45%
- 信心排序準確度：-0.03
- 診斷：低相關

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

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：台塑四寶股東會發超額股利朝半導體、低碳全力轉型| 證券 - 中央社 CNA；印度 2032 晶片自主，人才缺口何解？ - TechNews 科技新報；ASIC 與 CPU 並進，晶片商產品策略如何調整？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 108.77 | 108.77 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +0.44% | -1.09% | 2,265.00 | 2,265.00 | 0.00% | 不適用 | 74.39 | 30.45 | 410.73B TWD / 17.50% | 2026-05-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +5.26% | +20.48% | 110.00 | 110.00 | 0.00% | 不適用 | 4.00 | 27.64 | 22.66B TWD / 10.80% | 2026-05-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +29.20% | +17.89% | 225.32 | 225.32 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 424.10 | 424.10 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 724.66 | 724.66 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -3.06% | -9.90% | 1,407.61 | 1,562.34 | -9.90% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | +37.38% | +28.34% | 425.19 | 425.19 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 CPU, server CPU, x86, foundry；其中 3 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 1 篇新聞出現相關標籤。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 1 篇新聞出現相關標籤。

### 主要來源

- [台塑四寶股東會發超額股利朝半導體、低碳全力轉型| 證券 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTFBReTJhSkRlckZEdU5yRy1UUUQ2VnBTb01FRnlJMzZYMTJXOEx6cG41VjhLN3NYX3cyUXV6Wk1td2pTeHBUS1JqdEZieEtFdGRJT0JvclVKUTNKcXo5MVE?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 16 May 2026 02:11:00 GMT
- [印度 2032 晶片自主，人才缺口何解？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiakFVX3lxTE1jc2tkNmM0MDlIcUpETTEzSHpVYUd0Yy1WdHlLUzFDelBfb0FTeko3Wi1SdTJTTUIwXzZSUkQ3S0RnTUtVZlpMU1QtaC0zOVpCMXBwSFNIOW80X1VINXRXZ0kyd0piRFJyeVE?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 17 May 2026 19:31:47 GMT
- [ASIC 與 CPU 並進，晶片商產品策略如何調整？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE9vdldKZWZHNEk5dGtPRHVGNDJBODhpdlNXOWN2aW9CbHY4c05nTDE3cERfanhjNkRzMHBuOC0xNVJuYjU1ZENHbFpJVFBLUjF0aWhsUmdHM3VrZnpxcGdQbnBpV21Pc2M?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 17 May 2026 18:30:31 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：資金持續流入 AI 指數高檔震盪 台股商品資金輪動 - 經濟日報；重電、線纜族群業績強強滾，兩大關鍵推進器使「老產業」變 AI 時代新寵 - TechNews 科技新報；ASIC 與 CPU 並進，晶片商產品策略如何調整？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | +0.12 | N/A | N/A | 108.77 | 108.77 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.10 | +29.20% | +17.89% | 225.32 | 225.32 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.09 | N/A | N/A | 424.10 | 424.10 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.07 | +0.44% | -1.09% | 2,265.00 | 2,265.00 | 0.00% | 未明確 | 74.39 | 30.45 | 410.73B TWD / 17.50% | 2026-05-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | -14.25% | -8.35% | 421.92 | 506.69 | -16.73% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.07 | +37.38% | +28.34% | 425.19 | 425.19 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.04 | -1.44% | +6.01% | 547.00 | 547.00 | 0.00% | 背離 | 10.86 | 50.79 | 62.25B TWD / 19.22% | 2026-05-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.04 | -11.89% | -10.19% | 3,260.00 | 3,260.00 | 0.00% | 背離 | 62.91 | 51.95 | 46.74B TWD / -4.14% | 2026-05-01 |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 5 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 5 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [資金持續流入 AI 指數高檔震盪 台股商品資金輪動 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxQNC1jU1RHd1RwUWhpdmFkekljUHdkWmY5M1o4N3pZVVhaRkx3U1BzeTQ5NjFvTFZ2OFRiWmNRT0ZKanhxMWVfa2h2Rjl3OWctb1JKMGFlZ2VkY0lyMkxBM0xsSGR4MjRCcjZFam4yR0JrVjlEajBQUWQ2WlgxdG9YV9IBX0FVX3lxTE1aTnh1TWRBMUhzaDBEbi1kbERGN1JXQVRVNDJWV05WUkN2TllHeGh6YWQyaDlFSUtNanpRTWFOV25nV01iX2VKeFJfSEs4VjgxclBoT0EtNDVyMk9PcGt3?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 17 May 2026 16:23:06 GMT
- [重電、線纜族群業績強強滾，兩大關鍵推進器使「老產業」變 AI 時代新寵 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiogFBVV95cUxON3BKYUM0NVllZW1jZWl6MGdveEtfZjlaVVAtTGN3TVQ4TUtpTlVuSXNwUC1UTGJRc1BvczN6M0NFQ1NVUkNwMzBVOE1DYjFJcnJRSEJibUljdTd1Vl8xWG1KT1RkTGtHQTVaLWx4TkRjdDBrUE9senJTMVp2cmtpamZzZHZRWGZxaEFPZG9WTXUwdVpOMlBBQ1p1UU1EZ1ZOVnc?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 17 May 2026 03:01:41 GMT
- [ASIC 與 CPU 並進，晶片商產品策略如何調整？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE9vdldKZWZHNEk5dGtPRHVGNDJBODhpdlNXOWN2aW9CbHY4c05nTDE3cERfanhjNkRzMHBuOC0xNVJuYjU1ZENHbFpJVFBLUjF0aWhsUmdHM3VrZnpxcGdQbnBpV21Pc2M?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 17 May 2026 18:30:31 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：輝達拉貨太猛！台股「散熱一哥」EPS上看95元 最新目標價曝光 - Yahoo股市

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.29 | -2.58% | +0.41% | 2,455.00 | 2,835.00 | -13.40% | 背離 | 61.06 | 40.34 | 15.63B TWD / 71.62% | 2026-05-01 |
| NVDA 輝達 | 新聞直接提及 | +0.56 | +29.20% | +17.89% | 225.32 | 225.32 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 1 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：拉貨。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：拉貨。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [輝達拉貨太猛！台股「散熱一哥」EPS上看95元 最新目標價曝光 - Yahoo股市](https://news.google.com/rss/articles/CBMijwJBVV95cUxQSEhGQUNRbDhkZGVsT1Q4Xzl4RklFQ1RoeWxMM21SQl80TFdTRndiVWJKT3pKelZoRmpHTnNwQjlLX2lTbWJUdkxZZ1Q5akxzNjJoNUN2Sms1dFhvRXRROWNxc1NROW5OWUwxX3BvYWFQeDNKbWFPYWZ4MFlLNmJJbExlNW53b1ZiNlJZMm52VmVRMjBsM29vQjJ2UXdiRDhyWm1yck9GbUVDS1I3dWNKSENiMDdMaEEyX2JodW0zMEdpZzU0dGhoX3paNzBuSU5lQW9DaTdBblh2b2xjMmUyTDVDZlVmYk9qdURFOUx2UUEwSEIzWC05cU9vVkc4andHM3Q1c1B4REtJVF94LTgw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 17 May 2026 13:15:00 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：SanDisk Soars 411% This Year Yet Wall Street Forecasts 9x PE. Why Are Memory Stocks Getting Cheaper as They Rise? When Will the Memory Cycle Peak? - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 724.66 | 724.66 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | -3.06% | -9.90% | 1,407.61 | 1,562.34 | -9.90% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「memory」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。

### 主要來源

- [SanDisk Soars 411% This Year Yet Wall Street Forecasts 9x PE. Why Are Memory Stocks Getting Cheaper as They Rise? When Will the Memory Cycle Peak? - TradingKey](https://news.google.com/rss/articles/CBMisgFBVV95cUxObzJfc3d4cmhVcWFHbmc4Q3ZCQkJ3RkpWZ2ZJUXlOeDRRb09HNVpTX1Vwbks5d1poQ3VwV09ORlRGVmZGQTNYQWZ5LW9Vc1FtZEVZSkxLRmhkQkRrdlNHMUZGNm96eDNid0FhRjVfc0FqbF9aYnhYNHUyVVFaREtqbk9YajVBbGRyc01ndzVzMm9UZDVFMFBtdXItU2l1TTYxd3N0eGpPZEY2U3BIVmdQNUNn?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 17 May 2026 09:32:10 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：INTC, AMD, MU stocks hit 52-week highs today: What's triggering the rally? - MSN；Are SanDisk and Micron Too Expensive? Here's How You Can Invest in the Artificial Intelligence (AI) Memory Supercycle for Just $50. - AOL.com；SanDisk Soars 411% This Year Yet Wall Street Forecasts 9x PE. Why Are Memory Stocks Getting Cheaper as They Rise? When Will the Memory Cycle Peak? - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.76 | N/A | N/A | 724.66 | 724.66 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.38 | -3.06% | -9.90% | 1,407.61 | 1,562.34 | -9.90% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.56 | N/A | N/A | 424.10 | 424.10 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.56 | N/A | N/A | 108.77 | 108.77 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +29.20% | +17.89% | 225.32 | 225.32 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron、memory」，共 4 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [INTC, AMD, MU stocks hit 52-week highs today: What's triggering the rally? - MSN](https://news.google.com/rss/articles/CBMiwgFBVV95cUxNNzAzNzNjWEVSMUxtSHNzTGJnUVgzU183d0dnMnNOdEF0UXhkQ1pkRHd1UWtkRmVvSFlIbzZ5OWtRVDRrVFZxaG1HMWNPb2xqbVFJRHhCcVVmWUN1ZEVmekRmUFNoejJhRVBkM2doUktXOFdxZUh5NGV5X3NjWFNaTmRuWnN0R0xKTVo0dHd2bEFJTDFGM3c2OTg3ay1VZXJ0dkF2Z09XUnNYQzlETWZ4Vk5NVUJWT2MtbldyOVp6SGVuUQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 16 May 2026 21:55:28 GMT
- [Are SanDisk and Micron Too Expensive? Here's How You Can Invest in the Artificial Intelligence (AI) Memory Supercycle for Just $50. - AOL.com](https://news.google.com/rss/articles/CBMihAFBVV95cUxQcHd6enA5Wngwa1dtZU1wVWRpUHl5Q1Z1dkc0SGlrcE1EcmEtd0ZSM3d3YTlLUTVOSFVmOHJ6MC02dThfYnVETU5FcS1VSzBOOU9FVnA0QjBOdTdMMUNfdGJkWTlzWW9EU2NoTUdER0JWUFVVbW5ud2ttclhQVlVpa2lzcnA?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 17 May 2026 18:43:56 GMT
- [SanDisk Soars 411% This Year Yet Wall Street Forecasts 9x PE. Why Are Memory Stocks Getting Cheaper as They Rise? When Will the Memory Cycle Peak? - TradingKey](https://news.google.com/rss/articles/CBMisgFBVV95cUxObzJfc3d4cmhVcWFHbmc4Q3ZCQkJ3RkpWZ2ZJUXlOeDRRb09HNVpTX1Vwbks5d1poQ3VwV09ORlRGVmZGQTNYQWZ5LW9Vc1FtZEVZSkxLRmhkQkRrdlNHMUZGNm96eDNid0FhRjVfc0FqbF9aYnhYNHUyVVFaREtqbk9YajVBbGRyc01ndzVzMm9UZDVFMFBtdXItU2l1TTYxd3N0eGpPZEY2U3BIVmdQNUNn?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 17 May 2026 09:32:10 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：投資觀點-謝金河：台股關鍵的下一步 五窮六絕的新機會 - MoneyDJ理財網；同業股價表現-電子-電競週邊-台股 - MoneyDJ理財網；理財行事曆-台股 - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [投資觀點-謝金河：台股關鍵的下一步 五窮六絕的新機會 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMijgFBVV95cUxNNUhxOGNrU1poX0Q5eDB3UTdNZ25zelczbzJPWm5oNUVEbnRnTERQQkFKc2hLY1BGYW8zZkR2eFhGZTVRYmRFYlhpSW8yZTNZWjJ4Q2dmcndULVowT3JOZTAtcEg0bU1GejE0WnozbDVEME53YVFHaGEzd2pBdFZMbXVqdnZjeTg1c3p2TTZ3?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 17 May 2026 16:01:35 GMT
- [同業股價表現-電子-電競週邊-台股 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMiYEFVX3lxTFAwNXVPNnlQbC1POGZXcF9TXzBZaF9POXQxY0ZOa3lHY0RNbWFlejQtTDR5S2s0Mm9SLTJHSXo4NEVSYkdWOWIyQmhidmlOUmNZMm5XSVl6SklwRUt0YTd3QQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 17 May 2026 18:41:40 GMT
- [理財行事曆-台股 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMieEFVX3lxTFBkeVItVlNwTEdqN0V5R29ZMk5NSjRqNlZLNWVqZzlaRmpjVTZEZnY1MEE4bEdPb0RERnAxTG1aMlRIWXZNNER5dkoyTUljY2JxUllJeUdDVENkN0Nac1E1RFlkcXJCcmw5VXptMVd5MDlfQ3E3RlVNRg?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 17 May 2026 07:01:24 GMT

## 新興題材：EagleRock

摘要：新興題材：EagleRock 相關新聞集中在：EROK-EagleRock Land, LLC-細產業-美股 - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [EROK-EagleRock Land, LLC-細產業-美股 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMiW0FVX3lxTE92ZFB3TDZ3dUJBSnQxZW1wX2xNbHVNMjRVWE5PTFR1ZDdPUjljUVFaUG9pR3lyQVJ2dXRtRFFMZ3FhWWdDalZ5bk5VSGtBRUNoUGlpMkVYYXp3LUE?oc=5) - Google News source discovery | MoneyDJ Sat, 16 May 2026 10:27:03 GMT

## 新興題材：首季營收

摘要：新興題材：首季營收 相關新聞集中在：信義房屋公司治理滿貫、遠見ESG獲雙獎 首季營收年增3成 - 中央社 CNA

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [信義房屋公司治理滿貫、遠見ESG獲雙獎 首季營收年增3成 - 中央社 CNA](https://news.google.com/rss/articles/CBMiVEFVX3lxTE9LVFh1MzhFSkFLUWUwRV9pcV9YbmJ6LUg5VllnRDUtM2ZwRGhJSThMZTBaTDE1RmlrYWs0YzlXRHBNbFcxODM2REYxdkYxQ3lDenplYw?oc=5) - Google News source discovery | 中央社財經 Sat, 16 May 2026 01:30:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
