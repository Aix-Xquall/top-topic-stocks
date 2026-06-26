# 每日股市熱門話題分析 - 2026-06-27

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **綜合市場情緒**｜負向｜熱度 32｜市場確認 93.99｜同向 3/3
2. **新興題材：聯發科跌停**｜負向｜熱度 4｜市場確認 100.00｜同向 2/2
3. **新興題材：聯發科慘跌停**｜負向｜熱度 1｜市場確認 100.00｜同向 2/2
4. **半導體與晶片供應鏈**｜負向｜熱度 10｜市場確認 67.50｜同向 4/5
5. **新興題材：OpenAI**｜中性｜熱度 4｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.12（樣本 19）
- 5日相關係數：0.29（樣本 19）
- 同向比例：11/19

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 綜合市場情緒 | 93.99 | 3/3 | 0 | +8.00% | +0.60% |
| 新興題材：聯發科跌停 | 100.00 | 2/2 | 0 | +10.23% | +7.26% |
| 新興題材：聯發科慘跌停 | 100.00 | 2/2 | 0 | +10.23% | +7.26% |
| 半導體與晶片供應鏈 | 67.50 | 4/5 | 1 | +3.83% | -5.68% |
| 新興題材：OpenAI | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 0.00 | 0/6 | 6 | -7.68% | -2.49% |
| 記憶體與 HBM 供應鏈 | 0.00 | 0/1 | 1 | -6.47% | +4.30% |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
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
| 2026-06-26 | 0.08 | 0.04 | +25.00% | 16 |
| 2026-06-27 | 0.12 | 0.29 | +57.89% | 19 |

## 歷史回測摘要

- 回測日期：2026-06-27
- 近5日 3日相關：-0.05
- 近5日 5日相關：0.33
- 同向比例：+84.62%
- 權重狀態：未調整

- 方向準確度：+84.62%
- 信心排序準確度：-0.05
- 診斷：信心校準問題

調整原因：近 5 日有效樣本 13 筆，低於 15 筆門檻，暫不調整權重。

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

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：00929等三檔台股 ETF 換股出爐 刪台積電、聯發科、聯電等 - 經濟日報；亞股大震撼 黑色星期五／「台股」遭外資血洗 | 市場焦點 | 證券 - 經濟日報；三大法人砍2,055億元！台股跌點第三慘 外資本周包辦史上前二大賣超 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.48 | N/A | N/A | 128.32 | 132.87 | -3.42% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | -0.48 | -6.02% | -2.90% | 2,340.00 | 2,390.00 | -2.09% | 同向 | 74.39 | 31.46 | 416.98B TWD / 30.09% | 2026-06-01 |
| 2454 聯發科 | 新聞直接提及 | -0.48 | -14.44% | -11.62% | 3,880.00 | 4,310.00 | -9.98% | 同向 | 62.91 | 61.83 | 47.43B TWD / 4.99% | 2026-06-01 |
| 2303 聯電 | 新聞直接提及 | -0.48 | -3.53% | +12.71% | 164.00 | 178.50 | -8.12% | 同向 | 4.00 | 41.21 | 22.94B TWD / 17.78% | 2026-06-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。
- 2454：新聞直接提及「聯發科」，共 1 篇新聞命中。

### 主要來源

- [00929等三檔台股 ETF 換股出爐 刪台積電、聯發科、聯電等 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9VeG1meEl3OW9kYzFNaG9Td21ycmotaXVhVVlsYmlmVDhwRHJRMFY5MFlNSEZpbHZLSEVSZ3NYM21VMTZ4TW9xYmhTNFc1c1NCQlRQekRPTE1FQdIBX0FVX3lxTE9GZHpRWnl3dExKRnhMd21LWXRQcWZGdXF4REdRdk5ET043SFVIalo5MzNZcjdsYk5mLVpabnNVOWFEU0hETzdFcGwwN0xmU1JOejdUaFZneWZwRmJTY2Y0?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 25 Jun 2026 09:00:00 GMT
- [亞股大震撼 黑色星期五／「台股」遭外資血洗 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxQVHJ3OWt0dGlDUUxKMWJTcWxSMXBackxyRzEwcE1JaWdvSlI5VWhUbkRyenNGTi1Vb2VWRFpyTFotUTdRQ3Zza0MwVXJZR2RxYTg3Nk5wYnl5TGx4R2M4RUFuS0l4cEp4djZRRVRmOGNuZVVfQVlJM1dQOHR4TFNUNg?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 26 Jun 2026 17:34:30 GMT
- [三大法人砍2,055億元！台股跌點第三慘 外資本周包辦史上前二大賣超 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1rWEVDU0l2TmtzTy1nd0xEWHZKbHVzVVNjS2dTemJvalFlYUNyanFCNDRnYkpEZEtpU2U0Y3VLVXRJZGZ5T3dlRDlZMEdYSjFwZkdHQ29aWktBQdIBX0FVX3lxTE1ZVnVHcFJRSTZ5LUJ2MURtZWx2ZkNWcmRkM1BYT08zREVGZGxGcDN5X2xGbGRnZzBvVnFIdUpPV243OXpzU1NSNkpFRlZhT1JleGZoVE0xRTQxY3poVDVF?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 25 Jun 2026 09:00:00 GMT

## 新興題材：聯發科跌停

摘要：新興題材：聯發科跌停 相關新聞集中在：台股收跌1,683點連四黑 聯發科跌停、台積電下跌50元 - 經濟日報；台股大跌1683點摜破45000點 聯發科跌停剩49千金 - 中央社 CNA；台股崩跌1,683點失守4萬5 聯發科跌停、39檔躺平- 證券 - 工商時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2454 聯發科 | 新聞直接提及 | -0.65 | -14.44% | -11.62% | 3,880.00 | 4,310.00 | -9.98% | 同向 | 62.91 | 61.83 | 47.43B TWD / 4.99% | 2026-06-01 |
| 2330 台積電 | 新聞直接提及 | -0.48 | -6.02% | -2.90% | 2,340.00 | 2,390.00 | -2.09% | 同向 | 74.39 | 31.46 | 416.98B TWD / 30.09% | 2026-06-01 |

關聯理由（前 3）：
- 2454：新聞直接提及「聯發科」，共 4 篇新聞命中。 方向判斷命中詞：跌停, 重挫。
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 方向判斷命中詞：跌停。

### 主要來源

- [台股收跌1,683點連四黑 聯發科跌停、台積電下跌50元 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE40QjFlQ0F2dFFrMXJKQ2lVeDZmMkR6cUxBTWtIY1luT2VUbTFNejZWMUpyeE9FRHFINVdKSTIzWTFVN2hyaXRQSm1sWmVOdko2RU40VDFfVUFkQdIBX0FVX3lxTFBVYlllMjJEWUFGTE1mRHh4bDZ0dHQ0OEgxbHFueV9tWUg0RThjWGFmWkx5U21KckM3UU5sWXlLc2tvREIxMGd0Q0xJSG5kSS10Si1XR19OME1xV0hZMF9j?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 25 Jun 2026 09:00:00 GMT
- [台股大跌1683點摜破45000點 聯發科跌停剩49千金 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE5xbFpvNlhaN083YzQ3Q3F5UzhhaWxaaVQwbkt3UjJQS3A5RFF1RXZickNqdlVSWklqOVE0bU5uS1Q1ZjQwRUtDeUVuLWtLWjFiWDBWQ1VCc0tGSnRPOUE?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 26 Jun 2026 06:37:00 GMT
- [台股崩跌1,683點失守4萬5 聯發科跌停、39檔躺平- 證券 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5tZHZSNXRIamhtUWdiSjFmOFplMmEwME9oWVB1dV9acXFsODZ6WFNscTJmMkYyTE5aTm9iM3psczlUN1cyNWxKX0FHeWdHNEwzdzBkUU1ieDQ5YVpXRUNr?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 26 Jun 2026 06:11:00 GMT

## 新興題材：聯發科慘跌停

摘要：新興題材：聯發科慘跌停 相關新聞集中在：台股暴跌1683點「史上第3大跌點」 台積電跌50元、聯發科慘跌停- 新聞 - MoneyDJ

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | -0.48 | -6.02% | -2.90% | 2,340.00 | 2,390.00 | -2.09% | 同向 | 74.39 | 31.46 | 416.98B TWD / 30.09% | 2026-06-01 |
| 2454 聯發科 | 新聞直接提及 | -0.48 | -14.44% | -11.62% | 3,880.00 | 4,310.00 | -9.98% | 同向 | 62.91 | 61.83 | 47.43B TWD / 4.99% | 2026-06-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 方向判斷命中詞：跌停, 暴跌。
- 2454：新聞直接提及「聯發科」，共 1 篇新聞命中。 方向判斷命中詞：跌停, 暴跌。

### 主要來源

- [台股暴跌1683點「史上第3大跌點」 台積電跌50元、聯發科慘跌停- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPM254c3c4VURJSmdSTG1iZTBkVzJPV3lVNkZCN1VlZFJmYS1HdVBkMmxnQS1FR1Z1d2NMTndoR2ZUQnRRU2lWQWlFaFFkZU54VFdDQl82RWdxV0xtQXQ1N3JLR0JESV9uYU5ZbEdrQU5LRm1HUm80d3Fnem4xQ3VBS1VRYnN5Ry1tRXZRd3lPWUl5UQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 26 Jun 2026 06:19:00 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：What Triggered the Recent Semiconductor Sell-Off - Kavout | AI；ON Semiconductor Tumbles 20%: Is It Dragging Down Semiconductor Names Like AMD and Intel? - 24/7 Wall St.；INTC Stock Has More Than Tripled This Year — But Goldman Sachs Names 3 Better Chip Bets - TradingView

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.65 | N/A | N/A | 128.32 | 132.87 | -3.42% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.57 | N/A | N/A | 521.58 | 532.57 | -2.06% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.05 | -6.02% | -2.90% | 2,340.00 | 2,390.00 | -2.09% | 同向 | 74.39 | 31.46 | 416.98B TWD / 30.09% | 2026-06-01 |
| 2303 聯電 | 產業/供應鏈推估 | -0.05 | -3.53% | +12.71% | 164.00 | 178.50 | -8.12% | 同向 | 4.00 | 41.21 | 22.94B TWD / 17.78% | 2026-06-01 |
| NVDA 輝達 | 產業/供應鏈推估 | -0.04 | -3.53% | +8.66% | 192.53 | 211.14 | -8.81% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | -0.04 | N/A | N/A | 1,132.33 | 1,213.56 | -6.69% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | -0.02 | +6.47% | -4.30% | 2,090.71 | 2,335.00 | -10.46% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -12.56% | +14.23% | 365.02 | 446.77 | -18.30% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel、INTC」，共 3 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：pressure。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：pressure。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 4 篇新聞出現相關標籤。 方向判斷命中詞：pressure。

### 主要來源

- [What Triggered the Recent Semiconductor Sell-Off - Kavout | AI](https://news.google.com/rss/articles/CBMiiwFBVV95cUxQeV9hbWl4LXg0eW5ZWFVERlpaZGRsZzBkOEQzb0VuSmptQ2RsR3RUcldSTzhJcW1URGZsbnBjVUxmYlNpMHlESnlJdEVvZ1RaSWloQ0ZfODJXV012UF9qYjFfYVNDaG15cXpBNXYxYWpjaGNIY2hRa3hOdGhUSjdOcDhabENFWmFvV1M0?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 26 Jun 2026 14:48:26 GMT
- [ON Semiconductor Tumbles 20%: Is It Dragging Down Semiconductor Names Like AMD and Intel? - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiygFBVV95cUxOS00zZTJBdlhvTWVDRjNfWHFScGptT21Ia01wSFpKT25SWXcxY3N2WTNZQjc4YUlTVThQak5KTElLUUFNN0pYelZqRWZnb3lzLXdYUnlCSnVEVlJXeEROblIweGYyTnl2Z0dVbjgwMGs3MDFwYUVXd1lUb25QY0pvLTU5UU1yVTczdG04Vzg5Y29SU3RFdlJ2V2kyMEI3U09JVzNUZTBDUFI2dlBKMVJkdDVKdWJCWTlmbkxBTWpHLXJUNUxLQmluSzdn?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 26 Jun 2026 14:16:26 GMT
- [INTC Stock Has More Than Tripled This Year — But Goldman Sachs Names 3 Better Chip Bets - TradingView](https://news.google.com/rss/articles/CBMi3wFBVV95cUxQeG5OczZERXJtX3ktdUlHZmJVSTlyZWxMZE5KaV9EUWNwaTVnLUo3VGxuNGZmUERFUEdKMlY0NVJGemFWSXFBd2dISzlzOEZKNVo1eDJKYWZCMzNFWkI5MXZnY0tKS2o4NE1XQmMtYlhuUk44bVZhZTFGTUExUWp5dzFrV2Q5ZThoX0lLSUFYdERCVXJuRG1YazN1d29la3ZwaFZZb1NvSFhqMUZ2UkxRcUo2QmhPckZXUkVhTFNpcC1GVXBvS0g2c0xfdXFnTm11aTQwT2FUbldSMDM0ejA4?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 26 Jun 2026 08:04:11 GMT

## 新興題材：OpenAI

摘要：新興題材：OpenAI 相關新聞集中在：分析：白宮出重手介入 OpenAI、Anthropic，AI 監管警鐘響起 - TechNews 科技新報；OpenAI defers public rollout of GPT‑5.6 as US seeks early access to frontier AI models - Reuters；OpenAI limits new AI models to 'trusted partners' at request of U.S. government - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 新聞直接提及 | 0.00 | -5.03% | -26.39% | 372.97 | 506.69 | -26.39% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：新聞直接提及「OpenAI」，共 4 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [分析：白宮出重手介入 OpenAI、Anthropic，AI 監管警鐘響起 - TechNews 科技新報](https://news.google.com/rss/articles/CBMioAFBVV95cUxPNkh2U01zVGU2U01mNnJzMEpXWS1lX3RScExfLXU2ZEF6cHZiXzY0R2pQbUViN0VtRUtsTmVNelhMeVVKcXVSR21ZM3BaMXBZOXZER2xNXzRIbktmMWc0Q3RlZDVYNk03Y0twSGZjeXZybzRZWEhHVVAtVTl2dFQ5Uk9QcVJ5cnBrRzJKc1VmMDFLa2lDSEVZQ2dBVDVhY1Ro?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 26 Jun 2026 10:46:35 GMT
- [OpenAI defers public rollout of GPT‑5.6 as US seeks early access to frontier AI models - Reuters](https://news.google.com/rss/articles/CBMixwFBVV95cUxQUnFfdzFOMEtRZ2xQYThDMDl3OFlWUDVFQ3VFelowLVVHUGt0TktoUHMzamJDekMzS09jaGR5RU9EaVNsNmdKR1JYSzVwbGNneUVaWWlnQzM4YnUxZGp3ZkthVlYyUGhXMUtDSjNZVC1YSGlpeDYxVjBOTkdSeGltaC15TjRqYVJiQnlxVlhjY01ZODRVQURFMjZEbVdaUHRJV2JlNklyRXRpNzAxbnVDS1dETk82WjJxLXZFdFRrSk8tTDJJZTJF?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 26 Jun 2026 20:09:22 GMT
- [OpenAI limits new AI models to 'trusted partners' at request of U.S. government - CNBC](https://news.google.com/rss/articles/CBMiqgFBVV95cUxPbXc3S3VNWkFPMXVnZmZSRWhFYmpaQTV5X0NuMFJsUlZiRHZPY2lfNlJ0U0VNUTFlLUpNNFFCRC01akpSX3hET0IzM21IRVBaYmVYOHRlLWN0LXhmajhzZDQyd2pSSUVSUnFKek5oQ0xjUDhIRi05ZFZCcVIzUndQQjZGQUJ3V0piMGNjMF9WQ0NDYUdCb3V6a095emJpSlV5eFJYZEx2ck5sd9IBrwFBVV95cUxNQ2tyUVkzakNiV1hERTNhVXNKdXAwWmVmZU5MeEg5QUhMYzB4dVBPYzBMZWxPRUhBTm9MYlZfbWRzaUllS19PMjU1MkNWRGtCNVNGQWhYemttSWtyTGhnTU9CLWVhQUd1MXFIb1VjNXVDSE9hX0tubVpuSTB6MTBDMlFzejk5Z2MyNEdVY0xsQTdrdjBlS2pVWUo3eTgwc0hFWlI1emNVMDZ1c3NaT3pZ?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 26 Jun 2026 17:02:44 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：AI 鏈17台廠 高盛喊買 - 經濟日報；What Triggered the Recent Semiconductor Sell-Off - Kavout | AI；黃仁勳幫AI資料中心重定位 輝達股東會釋新訊 法人點名這票台鏈受惠 - 財訊

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.31 | -3.53% | +8.66% | 192.53 | 211.14 | -8.81% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 產業/供應鏈推估 | +0.08 | N/A | N/A | 128.32 | 132.87 | -3.42% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.06 | N/A | N/A | 521.58 | 532.57 | -2.06% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.03 | -6.02% | -2.90% | 2,340.00 | 2,390.00 | -2.09% | 背離 | 74.39 | 31.46 | 416.98B TWD / 30.09% | 2026-06-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.02 | -5.03% | -26.39% | 372.97 | 506.69 | -26.39% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -12.56% | +14.23% | 365.02 | 446.77 | -18.30% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.02 | -4.53% | +3.10% | 632.00 | 641.00 | -1.40% | 背離 | 10.86 | 58.68 | 63.03B TWD / 28.57% | 2026-06-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.02 | -14.44% | -11.62% | 3,880.00 | 4,310.00 | -9.98% | 背離 | 62.91 | 61.83 | 47.43B TWD / 4.99% | 2026-06-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。 方向判斷命中詞：受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 5 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 5 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AI 鏈17台廠 高盛喊買 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1TOXJ4QmYyYV8xUG5jeWI0UVRhemtDR2RuNFZCTVFDX0t5WjNaRW5KSXNnTUI4NUl3SFpQZ0lTS2tYNnAxemlQbWFPSVZZa0NlSW5qMjg3TlJCQdIBX0FVX3lxTE10RFdVUE1sWUhrdFEwM0pXbGJLWUw2LXlpSy1kUlR3SURxY0RYQWRlUjMyaUJSR0loNmFjemYtQmh0OWN0aFRPLWhJM2h6TUFUM3k1UmJKX0ZEV2x6R2k4?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 25 Jun 2026 16:42:39 GMT
- [What Triggered the Recent Semiconductor Sell-Off - Kavout | AI](https://news.google.com/rss/articles/CBMiiwFBVV95cUxQeV9hbWl4LXg0eW5ZWFVERlpaZGRsZzBkOEQzb0VuSmptQ2RsR3RUcldSTzhJcW1URGZsbnBjVUxmYlNpMHlESnlJdEVvZ1RaSWloQ0ZfODJXV012UF9qYjFfYVNDaG15cXpBNXYxYWpjaGNIY2hRa3hOdGhUSjdOcDhabENFWmFvV1M0?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 26 Jun 2026 14:48:26 GMT
- [黃仁勳幫AI資料中心重定位 輝達股東會釋新訊 法人點名這票台鏈受惠 - 財訊](https://news.google.com/rss/articles/CBMie0FVX3lxTE1TcUE0VHVLSks3QUlEblBMNGtMU1BESlhvamFjdlFqc0Vic08yWlF2QWRYUTFCbFNKcDRCUFd0WTd2bWZpb2xGTnU3cFhFVmxETGppaFpuYkNkN0M5Q2JLSV9BV3Z6dTdkTUZXcmpTZHVmdnZFNE9lamUzZw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 26 Jun 2026 07:38:33 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Micron Just Delivered Great News for Intel, AMD, Arm, and Qualcomm Stock Investors - The Motley Fool；Micron Rockets On 346% Revenue Surge: 4 Top AI Chip Stocks (NASDAQ:MU) - Seeking Alpha；Sandisk: Unlike Micron, There's Much Higher Risk (NASDAQ:SNDK) - Seeking Alpha

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.65 | N/A | N/A | 1,132.33 | 1,213.56 | -6.69% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.56 | N/A | N/A | 521.58 | 532.57 | -2.06% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.28 | +6.47% | -4.30% | 2,090.71 | 2,335.00 | -10.46% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.48 | N/A | N/A | 128.32 | 132.87 | -3.42% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -3.53% | +8.66% | 192.53 | 211.14 | -8.81% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、MU」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：risk, strong, surge, surged, rockets。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 方向判斷命中詞：risk。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK」，共 1 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：risk。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。

### 主要來源

- [Micron Just Delivered Great News for Intel, AMD, Arm, and Qualcomm Stock Investors - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxQSXR2ZktPYm9lYV9JN0l2TFhkZURiZmVSQm15THlxSGFtR1Bhb3Vtd041bWtGS2ZlSkFpS1oxRUgwNHlGZ3NvS2hkTmtWeXB1WE9hcENjMUx2QkpHRk5PSXFyZjJCN1cxZ3pJOEpiZFZjXzNJTEVxWUtFRWpocXJZdUdqQS1acm9IdzJEelhDbUV5Q1hUTlNiVw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 26 Jun 2026 16:45:00 GMT
- [Micron Rockets On 346% Revenue Surge: 4 Top AI Chip Stocks (NASDAQ:MU) - Seeking Alpha](https://news.google.com/rss/articles/CBMiqAFBVV95cUxNdERER2JOM2dGdE5HbGREc2wyaG5RV0RpS1JCem9VMElJX3ZYSDEwYzZzQmdHbUZtVjhMRWRWS0VfeXRrNTQ2N1VTbjQ3UzVpeEZtaU53bUNIWXhlZjMwUWZnVzlhNjV1dTJZckRfM01HUlJyR1pxTGx2S0UxalF5cHJ6ZXRZa01xTFloeDZ6YkFaWUN4cUNvdVRhV1ZyV0Q4RFdYeUlZUy0?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 25 Jun 2026 17:33:04 GMT
- [Sandisk: Unlike Micron, There's Much Higher Risk (NASDAQ:SNDK) - Seeking Alpha](https://news.google.com/rss/articles/CBMijwFBVV95cUxQRXpXTDhCV0lPR1NsdEJJWjZhcmVFdGV4YllDYnZzb3k5d3htTFhzZ3pJQm1Za3JUUTBURlF0ZExqVGlSWG1jNnpBM0RlZmM1SmtYa3MwaUFGS2R4ZUdhLXRzd0QwU0JVVW1SQU15ZFdkM2YxN2VEWUtwcEsyQ1dlU2xTOWFfN1lXc19kSWFNcw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 26 Jun 2026 17:30:21 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：個股動態報導內容-DEA027E2-69CF-4B23-982C-FBAF59E127F3 - MoneyDJ；《台股盤後》暴跌1683點、失守月線；全週下跌逾4%-新聞內容-基金 - MoneyDJ；個股動態報導內容-497A3C04-8737-4F18-A2A0-EDBF7CA535CF - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-DEA027E2-69CF-4B23-982C-FBAF59E127F3 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxNN1psNlNNa0VzQ3FxWWtDNjA2dzd5c1hrTHFQODJ6OXpKaVFHUVRjMjFrX2xRYUlDc2JHM09WYWh6WTBPMEpJVzZlVEhDdE1ydUtpWGxERHl6MlBVdFJ4aUxwd0VXNXpudjkwOFdiSU9CcC1oc3FmT05kMlBQMGZNTnFBbUJtdjhxaG4zSXpiWFNlZVlj?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 26 Jun 2026 17:15:18 GMT
- [《台股盤後》暴跌1683點、失守月線；全週下跌逾4%-新聞內容-基金 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxPNzdMNXJEU3gxcTdfM3Z6dF9zSUpaeFo5ZW9rLURGWjdUd0VYN1hZRXRHQVprTW5iLUxMSEN4YUdTSXY5b0Y1ZGd3eWJLVElJMjhxbmthM25tZjJtSEVNYm5RbTV3MGRZc3d2QkpRbFRXWEFsOV9sT3FjNElGdmt5RFAtQ3hKTGQtUDg2RnNHVTk?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 26 Jun 2026 08:00:00 GMT
- [個股動態報導內容-497A3C04-8737-4F18-A2A0-EDBF7CA535CF - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxQVDUwMDVJZDVuWHVZblBCbjI2QS16YXNlUEVOenIyaTNROVZVa2dZaUlQcXZibHItckVpSWlGVzJ1UDdQd0dUcS1TZVBBUGtMdXliV01MVjQxN2lfQUt4M3lVaGdfbkY0aERReDhzRTJ4Z2x5NTJEc2JfbWF3Y0ZrZ0RsY1p1WmIybzlYVmNtMDBmcGpn?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 26 Jun 2026 09:15:03 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
