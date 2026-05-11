# 每日股市熱門話題分析 - 2026-05-12

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **AI 伺服器與資料中心**｜正向｜熱度 11｜市場確認 76.67｜同向 4/6
2. **記憶體與 HBM 供應鏈**｜正向｜熱度 8｜市場確認 92.08｜同向 2/2
3. **半導體與晶片供應鏈**｜正向｜熱度 4｜市場確認 86.00｜同向 4/5
4. **利率與成長股估值**｜正向｜熱度 2｜市場確認 84.88｜同向 1/1
5. **新興題材：OpenAI**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.00（樣本 14）
- 5日相關係數：0.42（樣本 14）
- 同向比例：11/14

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| AI 伺服器與資料中心 | 76.67 | 4/6 | 1 | +10.51% | +11.58% |
| 記憶體與 HBM 供應鏈 | 92.08 | 2/2 | 0 | +7.36% | +34.48% |
| 半導體與晶片供應鏈 | 86.00 | 4/5 | 0 | +15.46% | +16.52% |
| 利率與成長股估值 | 84.88 | 1/1 | 0 | +4.96% | +45.72% |
| 新興題材：OpenAI | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：TradingKey | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 相關性偏弱；應提高同向價格確認權重，降低泛 AI、泛半導體等寬標籤推估權重。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-05-08 | 0.03 | 0.48 | +76.92% | 13 |
| 2026-05-09 | 0.10 | 0.55 | +33.33% | 9 |
| 2026-05-10 | 0.45 | 0.55 | +75.00% | 8 |
| 2026-05-11 | -0.03 | 0.47 | +85.71% | 14 |
| 2026-05-12 | 0.00 | 0.42 | +78.57% | 14 |

## 歷史回測摘要

- 回測日期：2026-05-12
- 近5日 3日相關：0.17
- 近5日 5日相關：0.07
- 同向比例：+50.00%
- 權重狀態：未調整

- 方向準確度：+50.00%
- 信心排序準確度：0.17
- 診斷：弱正相關

主要錯誤來源（高信心但報酬不佳）：

- 記憶體與 HBM 供應鏈｜2330 台積電｜信心 0.87｜3日 -0.67%｜未明確
- 關稅與供應鏈轉移｜2317 鴻海｜信心 0.7｜3日 0.00%｜未明確

調整原因：近 5 日有效樣本 14 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：AI 伺服器與資料中心 相關新聞集中在：AI 購物工具如何優化創作者變現並提升廣告轉換率？ - TechNews 科技新報；AI 紅利分配爭議如何影響三星研發投資？ - TechNews 科技新報；Meta AI 串接外部服務對第三方 App 生態系的影響為何？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | +0.18 | N/A | N/A | 129.44 | 129.44 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.15 | +25.83% | +14.81% | 219.44 | 219.44 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.14 | N/A | N/A | 458.79 | 458.79 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.11 | -0.67% | -1.76% | 2,235.00 | 2,290.00 | -2.40% | 未明確 | 66.26 | 33.74 | 410.73B TWD / 17.50% | 2026-05-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.05 | -16.13% | -10.36% | 412.66 | 506.69 | -18.56% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.10 | +38.42% | +29.32% | 428.43 | 430.00 | -0.37% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.10 | +2.48% | +2.29% | 537.00 | 537.00 | 0.00% | 同向 | 9.37 | 57.80 | 62.25B TWD / 19.22% | 2026-05-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.10 | +13.12% | +35.19% | 3,880.00 | 3,880.00 | 0.00% | 同向 | 66.17 | 58.81 | 46.74B TWD / -4.14% | 2026-05-01 |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AI 購物工具如何優化創作者變現並提升廣告轉換率？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMixwFBVV95cUxOdVk2YlYwU3E3bTRYbTFXcUgtbzNlb0l5LVBWZUZmaTREZm5nRkZ1LVRVMUtJNHNESTZrcjMwVTczOXBZUXBKRUlhLWJNcnNwVXlTTHBvNXZUUVZoNG5tdzB0djBIWEtJQkxGOGJJTjZscHEyS3FZck5VQTN6eFpuWG91bXlXN1pnY0ItZ2g1UzJoLXlBMUVkcC1PZzBvdkl5b1JFWGVreXoxNHBaTm5pTXRTOURxQUJfUUdCZGx6Y2E1enhlMHdR?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 11 May 2026 17:49:07 GMT
- [AI 紅利分配爭議如何影響三星研發投資？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiqwFBVV95cUxQamlxLUQ0bVEtTTNlTHBLVFRDZDFxbUItRlpLNmUycnpsdElMcDRxMWtTb245T3lwek1vTEg4a1lnNWZTWWVHMkxqLTRQWnFxeHNvclBjQWFGUFRpdWZBX18zaFRBYW1yV2VKWnpkZXBXc21FSEFHYTZsa295ZjZiQ3hTbmg2akFwY1FncDYtYlNSNEpReC1XbnlsTUdfSHpUUjRCN1IwZWZ1RlU?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 11 May 2026 20:51:20 GMT
- [Meta AI 串接外部服務對第三方 App 生態系的影響為何？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiwgFBVV95cUxPdG45TWVtaDJkT1hUeVRPZFl4WjZiSXVEQmVGVlVyM0NDcXlvVTFMVUlOWkE1Y0RrdW14d2k3T3hWOXIydlJ2TFAtN2xRVnJzU1FaNmF1UkczS005aFZ4QmdyWmtWQ05vcUNVOXp4UWo3aFdVTHJZRUlGcHY0TFV1cGQzWC02YUJ2LXRma1lPcE9pdWJDbWdnQlBfc1VVb0Ixd1M5cGZHNnlCVmlIMXlXblZPSVJZRXdBdllodDl1ejU1Zw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 11 May 2026 17:24:23 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：台股ETF前十強單日全大彈逾3% 台新00947擁IC設計、記憶體唯一漲逾6%稱霸主被動ETF | 財富管理 | 商情 - 經濟日報；Intel (INTC) Stock Surges Over 14% on Apple Chip Deal and SK Hynix Talks - MEXC；Why Sandisk (Not Micron) Could Be the Biggest Winner Of the AI Memory Era - The Motley Fool

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.88 | N/A | N/A | 795.33 | 795.33 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.88 | +9.76% | +23.23% | 1,547.56 | 1,562.34 | -0.95% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.65 | N/A | N/A | 129.44 | 129.44 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 新聞直接提及 | +0.65 | +4.96% | +45.72% | 292.68 | 293.32 | -0.22% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +25.83% | +14.81% | 219.44 | 219.44 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、Micron Technology、memory」，共 4 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk、SNDK」，共 2 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。 方向判斷命中詞：surges。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [台股ETF前十強單日全大彈逾3% 台新00947擁IC設計、記憶體唯一漲逾6%稱霸主被動ETF | 財富管理 | 商情 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1fQkJpbktXZ2xKZTVFZDZMNFN3REtscjZJQnk2c0h1TldUcE9VSlFUSWVHSXZzaVRkdXhZZThNTk8yQnJmSWlXR0VEZXBMOFdUWXVhbmlpTTlnQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 10 May 2026 17:00:00 GMT
- [Intel (INTC) Stock Surges Over 14% on Apple Chip Deal and SK Hynix Talks - MEXC](https://news.google.com/rss/articles/CBMiSEFVX3lxTE1rZFpPUzN4cDF6WDhlZVpacVI1NXRwVGZrNm81ZXRROVF1Nk1OczdBTWZkcTRTQXRXRG9MMWcwNTc1dlFYa29MMw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 11 May 2026 17:59:16 GMT
- [Why Sandisk (Not Micron) Could Be the Biggest Winner Of the AI Memory Era - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxPZXNURzdrX1Q3SlJ4US0yRFpzZzMySE1iRVhuUk9DZWphT2ZNMHowM2xzUUExNVQyQXIwLUZVdExsZk5OT29Nc2s0YWZnb0RLZVJiTXh0Q3lTcjVQb2U5UDlCTEw1MF8tZFh3U1gybm40YWtKRGF1NTZXcjdaZDJZTUg5RDJ5ckdzQWl2cUZFTzJDaUVjbS1HQw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 11 May 2026 20:53:28 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：This Chip Stock Is Absolutely Skyrocketing. And No, I'm Not Talking About Intel or Nvidia. - The Motley Fool；科學園區審議會通過7案 新竹半導體聚落吸引SiC投資 - 中央社 CNA；Chip stocks continue to surge. Here's how to buy one for less - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.80 | N/A | N/A | 129.44 | 129.44 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.73 | +25.83% | +14.81% | 219.44 | 219.44 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.08 | -0.67% | -1.76% | 2,235.00 | 2,290.00 | -2.40% | 未明確 | 66.26 | 33.74 | 410.73B TWD / 17.50% | 2026-05-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.11 | +3.94% | +17.00% | 95.00 | 95.00 | 0.00% | 同向 | 4.00 | 23.87 | 22.66B TWD / 10.80% | 2026-05-01 |
| AMD 超微 | 產業/供應鏈推估 | +0.08 | N/A | N/A | 458.79 | 458.79 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | +0.08 | N/A | N/A | 795.33 | 795.33 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.08 | +9.76% | +23.23% | 1,547.56 | 1,562.34 | -0.95% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.08 | +38.42% | +29.32% | 428.43 | 430.00 | -0.37% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：surge。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：surge。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 2 篇新聞出現相關標籤。 方向判斷命中詞：surge。

### 主要來源

- [This Chip Stock Is Absolutely Skyrocketing. And No, I'm Not Talking About Intel or Nvidia. - The Motley Fool](https://news.google.com/rss/articles/CBMilwFBVV95cUxPdnBaZHBJdnlpVEJOdmJjMVBpeHJZbkdqUDlWeEozT0hUSmNLeVVyZElEQ3h0T3JTVXprdWtpUWl4NUJiOF8tMmIxR2dmaGp4UnRLZ0ZZbVA1eGpLLU9DMEN5QS1id0pWM3F6dVBUTm1Ub3c2ZDBIemlPTDFqOWE5RDc4MkE3YUdHR3paVGJ3ejF0RXRmUVNR?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 10 May 2026 09:41:00 GMT
- [科學園區審議會通過7案 新竹半導體聚落吸引SiC投資 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE5CRWg4b2FHcUR2VHBuUkxnWG5PNmo0N0lIckIxLWZodENjVzFQZGZuS3JEc0FxTEg2QUduamlKTTZpMW9zNTVUcGQzZ284d1dnSzlhWGlCRmM0LTNTTFE?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 11 May 2026 12:11:00 GMT
- [Chip stocks continue to surge. Here's how to buy one for less - CNBC](https://news.google.com/rss/articles/CBMinAFBVV95cUxNQ3VYbFJPZVBibUxWMXJhNHZ3R0VDNFBIc1drX1UyQjNBQXZyYVlUbjlLUTkxVmtOTFVLSEY5blpyQnNkZF9Fb0N0Y2hkY243dGI0SnlMbmxyR1lFSFlHVTZQYXl1Y3pXX241YVBFd3lELWttaXd1Z0tIX21nMHZpVUlSbXdUcjN5YXNVcGE0em5MRkgtV2N2UlV1WXnSAaIBQVVfeXFMT3JwdGtvVzBhNURlUkRIZW5qS0JfMk5VamlZQVkwc0pJY3pQMnVPUmVreHhmRFFNbllpSm5Kams1b1NBanNtVjJ2ZWxONFdsOGNhNXhTVXQ4UWVBem5fOFhYS1VQMzhVR0F2MnNPcmpHY3lSMzF0aklQUzR5WFRSb2pkQUo3cnFHV1huUTk5Y1Q5T2NuQUF6b1VZTlFkRzVVZ0VR?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 11 May 2026 15:58:54 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：Assessing Intel (INTC) Valuation After Apple Foundry Deal And AI Earnings Momentum - simplywall.st；美股創高還能追？摩根大通示警：別忽略「通膨未爆彈」 - news.cnyes.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.65 | N/A | N/A | 129.44 | 129.44 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 新聞直接提及 | +0.65 | +4.96% | +45.72% | 292.68 | 293.32 | -0.22% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | -16.13% | -10.36% | 412.66 | 506.69 | -18.56% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AAPL：新聞直接提及「Apple」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Assessing Intel (INTC) Valuation After Apple Foundry Deal And AI Earnings Momentum - simplywall.st](https://news.google.com/rss/articles/CBMiyAFBVV95cUxPYjRfUXlPS2Q4ZTR1bTB5MTlkR0xPT1poLTlyTnRtb0czQlAyT2t4NFBTd3g4VldtcVpjY3lxbjBka1RpTUszN19XTkV2enpGR3N4STN1UFRVTDNHcHFMZTI5VEZpQm5mU3FSZWRpRS1xZWs3eFU3SG5UQ2hwLXFYR1pmQ1pIdlRURkp4cmVXMjVpLTZvVVNoZEdvYUZZb0l2ZmN3MjhOSGMwbS01TUE1OHowamVkOE1aTGozZEVldG5DcFNEUE5LZNIBzgFBVV95cUxOTjd1eXhnclR6VVhlOFE4TmxLZzBBRHk4ckVEakhhRHB1RUZRQzFXSjV1cU5wZDYzMS14YndnSU9UajRnOEZVMlg3aVN2MFV1SW5zVFlBbWhEdl9BcWxTRC11Um5pNGpCY2FMcm1GblljZlZRSS1nb2RoUTJwRDc1MFM1anh6RGhqUm1pZE5aTDNXVUdJT09SUTJaN21wNWZwWmd6cGx1YTlGa20tRWgyUmRDeDdVRlZOR3JZN3BHaGRtaXhCMW9jZm5sdWd3Zw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 11 May 2026 16:54:21 GMT
- [美股創高還能追？摩根大通示警：別忽略「通膨未爆彈」 - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTE1nck9DaVMtWDJMaWlMb0V0V2pPWjlRRFp0SjRndkZsLXc3aGY0S1M3dHM4c21RNU03b0pGSGxySHNralFBMGVqS0lqVHlSM1E?oc=5) - Google News source discovery | 鉅亨網 Mon, 11 May 2026 12:30:06 GMT

## 新興題材：OpenAI

摘要：新興題材：OpenAI 相關新聞集中在：OpenAI creates new unit with $4 billion investment to aid corporate AI push - Reuters；Former OpenAI executive Sutskever discloses nearly $7 billion stake in AI firm - Reuters；OpenAI revenue chief Dresser says enterprise AI adoption is 'at a tipping point' - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 新聞直接提及 | 0.00 | -16.13% | -10.36% | 412.66 | 506.69 | -18.56% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：新聞直接提及「OpenAI」，共 3 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [OpenAI creates new unit with $4 billion investment to aid corporate AI push - Reuters](https://news.google.com/rss/articles/CBMitwFBVV95cUxONzBVZGx1c2JvQTRJeWZ2d1FPQU1GTnhSaEZONVV0YmpaRnI4WE50Q25udWxlNC1LbVR0ZkJnTzJYM0dRekdNZWVVempHSEZJT1ZTS1Q3bDI0NHJRdW5lOURaUmNPX0UtQVNnUXNyQUhXQnhvd1lYT1JZdXl5dWtiNk9CblcxV1FHQmdoSGpiekJjX3kwSlZSeHVOcE93ZHY1VU92bldWRTZqb2NKck1yUlRqWjkzRk0?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 11 May 2026 13:59:44 GMT
- [Former OpenAI executive Sutskever discloses nearly $7 billion stake in AI firm - Reuters](https://news.google.com/rss/articles/CBMiuwFBVV95cUxNejRjVEZaWTlmSWZJQkRSWDhNYkFqNm51UXNxTmNsVjFueEhEeTUwZUpvYkpPYjZLMGR5NGVYblpuZFo1cmJsLTNkVXk4OVFpdmwzS005N0hLWDRuNy1OcXhSVkFHT1FxcXBFa09GV2VqaGkxM3hPb2ltak1YU05jdVc3S2dUOGhMZGRiWHJFcnlGS2FCeEotQ0dPYWpPb2JneFpVSlhtZ181TmdZTEhEUEduU1BtWEs5X1B3?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 11 May 2026 19:56:22 GMT
- [OpenAI revenue chief Dresser says enterprise AI adoption is 'at a tipping point' - CNBC](https://news.google.com/rss/articles/CBMifEFVX3lxTE56YkNzZ0NCdElkekVKSncwNVY2WmlBQzd1S3pvSkYxOXNFdW52MWN6MHFQV21sa0FaLVJqbEl0Zm9OczQ2ZGI4cVM1SFowenMyYzNKb3RydjBWNE1NNV9NUi1sZk9BZFlra3FrNUo0RUU5VWhpNVpJX2RYamrSAYIBQVVfeXFMT2RQNWJ3OC1vbGFKLWVWekdWNl9pc1htREFvRXBKUFNjM1NTWHpMb0RPMlkxOXZEUW1kYWZ4MDVTeGhMbjdYbFBlVG9jdk8xNWplRnliMmtxUnktS25tTTZjOGhfXzk2djI4UEJXRHBuTkhleGIzUXVlN1BfRjVjNUN0QQ?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 11 May 2026 19:24:38 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Intel Corp Stock (INTC) Opened Up by 3.89% on May 11: A Full Analysis - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 129.44 | 129.44 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Corp Stock (INTC) Opened Up by 3.89% on May 11: A Full Analysis - TradingKey](https://news.google.com/rss/articles/CBMiiwFBVV95cUxPbE9rOS1iLWNzSGtmY01FQ1p3aUxBdWU1TmViRk5Ra2tUcy1keUZqTjZHbHZ2WmJndVVEQVNVRXZSNWQ0R1oxR2ZMdWg1ZTYwSkE4alNLZllGRWU2Nk1WX20zMDY3Y3pVX1pra3ZtMFRwdHZURWlqbjhhbW1jZm56MTRYX2dSN0xNWVE0?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 11 May 2026 13:48:29 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：散熱股大跌結束了嗎？健策亮燈、奇鋐守五日線 - 聯合新聞網

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | +4.93% | -11.44% | 2,555.00 | 2,835.00 | -9.88% | 不適用 | 49.17 | 52.23 | 15.63B TWD / 71.62% | 2026-05-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐」，共 1 篇新聞命中。 同時符合主題標籤：thermal。

### 主要來源

- [散熱股大跌結束了嗎？健策亮燈、奇鋐守五日線 - 聯合新聞網](https://news.google.com/rss/articles/CBMiUEFVX3lxTFBmNHdXUTNiMHpvZ3RLcnNzNjFhQmNFaThOdDM5Z1RVYVItWjdVWE9wUEpGMWx1SEtSbnRyeWJaaWxoTnZKVlYxaE1HVGhxem5G0gFWQVVfeXFMUGJiUUxEYjhhYlBqWDgwcHhYeTBic1dWUGEwMUFMV3IzUVV2NHEzRnJJOVpSS3dqSjlFTTEya0VXdHFHMVFNLUthcUM4aXVGY01JZFdoM0E?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 11 May 2026 04:06:05 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：《台股盤後》收漲186點、42K又得而復失，力守5日線- 新聞 - MoneyDJ理財網；【邱顯比、葉銀華】股市強彈 台股主動型基金報酬驚人 - MoneyDJ理財網；台股焦點：百一(6152.TW) - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》收漲186點、42K又得而復失，力守5日線- 新聞 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikgFBVV95cUxOSEZXLThOQWlqNWpIcngwLUpzaXFzNE9PNjhDTGZndTQwNkpKQVdNWUZKRG9Ob2lRSE9pZmdCRXd0QmROd1ROaUxfNWN1SndyX21fR2FDNVNzeURSWjMtbVZMN0RTbHRRY1BVY2lVRjU4WTIyeTA5b1hIeHlZSzFhSUg5c0NjRFU5b0xKWjFCTGxsQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 11 May 2026 07:55:00 GMT
- [【邱顯比、葉銀華】股市強彈 台股主動型基金報酬驚人 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilwFBVV95cUxNRVJkMTQwVkM4RVBOZjNYdHpIZWF5Z3BRTzUzaEdTLXd3cXJua0JIX19fVlJLXzdhbDJFTlVPanFJeld1emVJUDBsU1ZUVEhUOHoyUzV4SDZmeEFPSmJudnpCTTBXZF92WHNzeTY3TWJoZnZveHVTYWRJNTVhTkJMUlJqLUJkQ21YM0hucW5kNTgyUm5MZ0J3?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 11 May 2026 06:15:00 GMT
- [台股焦點：百一(6152.TW) - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikgFBVV95cUxNYy1rNnNKRFFYSWsycWZpcFNaQkgwVTZJblpsT2ZoMEYxMEFGb3VzeEl5S0l6TDh0TE1hdmltQ29SaENoNkhWOENOUDh6WTNUd25PbWpQcWtWNlNEVDUxMGJGUXB5SjlQdGQ1ZmM5S0FIUkg0eTIwb2FqQXZKWTRWWlI1VXNjczNxMkYzRjlWazd4Zw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 11 May 2026 01:11:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
