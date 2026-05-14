# 每日股市熱門話題分析 - 2026-05-15

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **半導體與晶片供應鏈**｜正向｜熱度 11｜市場確認 92.88｜同向 2/2
2. **AI 伺服器與資料中心**｜正向｜熱度 12｜市場確認 72.60｜同向 4/6
3. **散熱與液冷供應鏈**｜正向｜熱度 6｜市場確認 65.00｜同向 1/2
4. **新興題材：BofA**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0
5. **記憶體與 HBM 供應鏈**｜正向｜熱度 8｜市場確認 0.00｜同向 0/1

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.17（樣本 12）
- 5日相關係數：-0.08（樣本 12）
- 同向比例：7/12

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 半導體與晶片供應鏈 | 92.88 | 2/2 | 0 | +7.62% | +5.09% |
| AI 伺服器與資料中心 | 72.60 | 4/6 | 2 | +8.64% | +7.39% |
| 散熱與液冷供應鏈 | 65.00 | 1/2 | 0 | +17.59% | +14.57% |
| 新興題材：BofA | N/A | 0/0 | 0 | N/A | N/A |
| 記憶體與 HBM 供應鏈 | 0.00 | 0/1 | 1 | -10.65% | +3.19% |
| 新興題材：奇鋐看好今年營收 | 0.00 | 0/1 | 0 | 0.00% | +5.80% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：卻回殺跌停 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價呈負相關；應檢查正負向詞庫，並降低新聞直接提及但股價背離的權重。

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

## 歷史回測摘要

- 回測日期：2026-05-15
- 近5日 3日相關：-0.26
- 近5日 5日相關：-0.21
- 同向比例：+47.83%
- 權重狀態：已調整

- 方向準確度：+47.83%
- 信心排序準確度：-0.26
- 診斷：方向與信心皆需修正

主要錯誤來源（高信心但報酬不佳）：

- 散熱與液冷供應鏈｜3017 奇鋐｜信心 0.8｜3日 0.00%｜未明確

調整原因：近 5 日方向與信心排序皆偏弱，降低方向詞與供應鏈推估權重，並加重背離扣分。；關鍵詞×公司後續樣本有效 4 筆，未達 30 筆，不調整樣本權重

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

摘要：半導體與晶片供應鏈 相關新聞集中在：AMD vs Intel: One Triples Free Cash Flow While Another Burns Billions on Foundry Ambitions - 24/7 Wall St.；台積電估2030年半導體產值1.5兆美元COUPE成關鍵字| 產經 - 中央社 CNA；凱基證券輔導之IC設計新星 通寶半導體登興櫃掛牌 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | +0.73 | +1.57% | -1.73% | 2,270.00 | 2,270.00 | 0.00% | 同向 | 66.26 | 34.27 | 410.73B TWD / 17.50% | 2026-05-01 |
| INTC 英特爾 | 新聞直接提及 | +0.67 | N/A | N/A | 115.93 | 120.29 | -3.62% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.60 | N/A | N/A | 449.70 | 449.70 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2303 聯電 | 產業/供應鏈推估 | +0.07 | +13.68% | +11.92% | 108.00 | 108.00 | 0.00% | 同向 | 4.00 | 27.14 | 22.66B TWD / 10.80% | 2026-05-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +35.17% | +23.34% | 235.74 | 235.74 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 776.01 | 803.63 | -3.44% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -10.65% | +3.19% | 1,382.72 | 1,562.34 | -11.50% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | +42.09% | +32.75% | 439.79 | 439.79 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip, foundry。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AMD vs Intel: One Triples Free Cash Flow While Another Burns Billions on Foundry Ambitions - 24/7 Wall St.](https://news.google.com/rss/articles/CBMizgFBVV95cUxPUmhYbzNScEZyOWl4WlFxVi1mSnBQR0tvUzV3b0pFc3ZlTVBfR2tEeG96Z21Qd2FCcFBPcWZ4T3paZjNlUjZOQ2J2N2xJb3hjTFZMbDRuSmdBbldJNWZXdS04UDBHQkpXSnRqNkFrOWhKTDBGbFJvOWRySGFEQU9OX1A2TUNDS19KeDRYYWNzbXVRZ3JfT25HamF0QllNVTlqdGlwTzNna2tIbndVbnl0T2NLQ2ZPMmxuaTRiUkxvLWlzVWJsMWxNeWNqVDVNQQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 14 May 2026 18:58:29 GMT
- [台積電估2030年半導體產值1.5兆美元COUPE成關鍵字| 產經 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE44Wk13V2dSWl9yTGdoaDNJb1hTRlJ2UTlhZ3lIVkEwdjl4OVU5S2ZRLXZaWDRuLTQzX0R5U3FHOFZCQkNYb3o3eXRHME15enZwdHlVZjY5eWppTUptZ1E?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 14 May 2026 04:41:00 GMT
- [凱基證券輔導之IC設計新星 通寶半導體登興櫃掛牌 - 中央社 CNA](https://news.google.com/rss/articles/CBMiVkFVX3lxTE5ZZkdNcnFibi1qS1hGcXZtRDZ3Nl9tNGlsbVM4LVFyX0VEbzQxNDZtenI5NC1JdFNYRU1JQmFHRll4VVZDTWlta012SV9VNU9OdG1qdlF3?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 14 May 2026 10:21:54 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：當人工智慧成為老闆，AI 咖啡館實驗一窺人機共事盲點 - TechNews 科技新報；AI 需求帶動網通升級，哪些技術主導？ - TechNews 科技新報；AI 如何加劇 K 型經濟下的就業與所得分配？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | +0.12 | N/A | N/A | 115.93 | 120.29 | -3.62% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.10 | +35.17% | +23.34% | 235.74 | 235.74 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.09 | N/A | N/A | 449.70 | 449.70 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.09 | +1.57% | -1.73% | 2,270.00 | 2,270.00 | 0.00% | 同向 | 66.26 | 34.27 | 410.73B TWD / 17.50% | 2026-05-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | -16.78% | -11.06% | 409.43 | 506.69 | -19.20% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.07 | +42.09% | +32.75% | 439.79 | 439.79 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.07 | +2.05% | +1.48% | 548.00 | 548.00 | 0.00% | 同向 | 10.86 | 50.88 | 62.25B TWD / 19.22% | 2026-05-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.04 | -12.24% | -0.44% | 3,405.00 | 3,495.00 | -2.58% | 背離 | 62.91 | 54.26 | 46.74B TWD / -4.14% | 2026-05-01 |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：升級。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：升級。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：升級。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [當人工智慧成為老闆，AI 咖啡館實驗一窺人機共事盲點 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiiAFBVV95cUxObDUxSzZpWmViLXBSR2RDWlNWd1M1SzBHeHFpVnBCVGhhM3NCYW0zVTAzM2FZWGJxZ0ZRTU9qbk40bEZ1YjVnR3c5QmdjZUZKQjdENEk5Wmh3Z09wb0xYYUNyRnRKSWs2NlMzRWVpODdpTklSRzdYcXBCT2NzOERQeHEzMUg1Y0Ji?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 14 May 2026 10:48:10 GMT
- [AI 需求帶動網通升級，哪些技術主導？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiZEFVX3lxTE5aaEpZaU1hTjlzLXpDbGEwU3hIVmIxZkhjUk5YYTJyRlBmRGNfNEpsQmxDUUtRVGttQk5rUmxGZFdIWVZWS3FiYlk0UzlOaGlXWTNBcnhZeHlOX1A1QjBOUml0Yk0?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 14 May 2026 20:30:41 GMT
- [AI 如何加劇 K 型經濟下的就業與所得分配？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiaEFVX3lxTE1MaVp6YTEzYWFSbHh4VDF2WGw1dHBMaW9NRUZUNGZpTngwaTF6R2w3NVBEMnNqT0FDRkZGTE9OcDIzN0VfdldaS3IxaGdHQTJld2tjdlZrb2M5QUJnZmdGZENEZFJFa1F1?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 14 May 2026 20:30:00 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：新架構革命未停 健策扛非戰之罪、奇鋐遭錯殺 輝達降規趕出貨 散熱族群前景解析 - 今周刊；奇鋐看好今年營收及獲利逐季成長 針對散熱模組修改設計釋疑 - news.cnyes.com；傳NVIDIA Rubin取消鍍金設計 奇鋐：對營運無影響 - DIGITIMES

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.57 | 0.00% | +5.80% | 2,555.00 | 2,835.00 | -9.88% | 未明確 | 61.06 | 41.98 | 15.63B TWD / 71.62% | 2026-05-01 |
| NVDA 輝達 | 新聞直接提及 | +0.56 | +35.17% | +23.34% | 235.74 | 235.74 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐、3017」，共 6 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：成長, 創高。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [新架構革命未停 健策扛非戰之罪、奇鋐遭錯殺 輝達降規趕出貨 散熱族群前景解析 - 今周刊](https://news.google.com/rss/articles/CBMigAFBVV95cUxPM0JYUTV4R3hETXRncWdJbWYxQ2FtZlJxVVdKTVRNSk1wSXpkeExjbjVxWXBMWmxGdVl4dWlDWHU2OUduV3pkc0QzZmdIOThkSFVxenI3VldKU3d5ZlV1cmYyV2c5T1lqRERpU0hHZkMwTTlkQ2F6aXJpMWdCVXNKOQ?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 13 May 2026 06:01:00 GMT
- [奇鋐看好今年營收及獲利逐季成長 針對散熱模組修改設計釋疑 - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTE1rT2dIQUlJZEZtT0s3amhLcGNhS1phV2h1akJxMkVsNFhxNHF5c1p1dEVJMVE0aDFhT0JoTzllUkU2R3NVaktIejdiSkI0NEU?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 14 May 2026 11:19:40 GMT
- [傳NVIDIA Rubin取消鍍金設計 奇鋐：對營運無影響 - DIGITIMES](https://news.google.com/rss/articles/CBMijgFBVV95cUxOQUVMSFgxbWhnM285WnV4akdCQTA3YWNXQXBibG0wWndRMU43elRPUzZWYnRYdlZzOGgyOG5jVjJYSXVpN2VKWDV4bGV1ZUNhbGhPM2FZRmJXU3NRWXFRVmVlNGNtVWxtZFdSbkw1eTF2Wks0eG5kTkZPbzJvWjBzdXFQZEhwX2FJU2V2aHFR?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 14 May 2026 10:06:00 GMT

## 新興題材：BofA

摘要：新興題材：BofA 相關新聞集中在：BofA Just Nearly Doubled Micron Price Target to $950: Memory Supercycle Just Got Bigger - AOL.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 776.01 | 803.63 | -3.44% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [BofA Just Nearly Doubled Micron Price Target to $950: Memory Supercycle Just Got Bigger - AOL.com](https://news.google.com/rss/articles/CBMigAFBVV95cUxPa1RLclZZblQ4c25jRGsyS2ZiV2x6TC0zak1SQjNnZWlDX0EybWRpTS0yZDE5OE1aNExXaWZxWV9WbWp4ZVNFc1BidHNqUEpoSmt6QVRWdWozRmY1OWVRTEtlWGpjNnB1Vk5sYVYxQmpCZC1WZzAtbkpveVRxRGU3TA?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 13 May 2026 15:12:09 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：INTC, AMD, MU stocks hit 52-week highs today: What's triggering the rally? - MSN；How Far Can the Micron and Sandisk Rally Run? - TradingView；Why I'd Rather Own Micron Stock Than Sandisk - The Globe and Mail

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.76 | N/A | N/A | 776.01 | 803.63 | -3.44% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.38 | -10.65% | +3.19% | 1,382.72 | 1,562.34 | -11.50% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.56 | N/A | N/A | 449.70 | 449.70 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.56 | N/A | N/A | 115.93 | 120.29 | -3.62% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +35.17% | +23.34% | 235.74 | 235.74 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally, record high, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 2 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [INTC, AMD, MU stocks hit 52-week highs today: What's triggering the rally? - MSN](https://news.google.com/rss/articles/CBMimANBVV95cUxNWnBwXy11U0pvUXdLcE5sSkpudVFPVVRVRVhCc1RBVEVHdFRFVG1KSWlnWGt0bFo3ZkJNSFlwR2JPNXFkcERmLTJLYXJsTlpGRUZIcjRpOWROVFN2YVU2d1AxY2U1ZldUUk9abDBzN0hyZ0RPZG1KaWh0Y1dmYTcwb3piNzZFWF9zMUdjSWFSVVVndlNPYVpJSjJtNlc4YmZLc3N3cjJtTXNsYU5jQjFGQjA2Z213aUUwRE1nc0J3ZVVNb1Z0TmlnUU9LamRrNjhWR28yM3Q2UjBpZEdQUlJfQTlZQlRycnExTGdiSEZBTmxmUHFPTjMwTFFRR1RqVkZWYmFFTVZUeHBycE9VdndfcWwtTW84YlF6UGVPbGcwdmpzSTVURGxOc21PZ2ZrOFJCQ2NEVG9IY2JZWnF6eng5MDFkemhiNWUwRWpfU243MjF1Vnpuc2FrcWJyMnBWNENhVnVjOHFGQTdEVlJsZ0tSRHYzdzFkel9lZXI1LWhhZlVtTFBYWURBOVdROFVzZzZTRWxBQXlVOVY?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 14 May 2026 02:17:56 GMT
- [How Far Can the Micron and Sandisk Rally Run? - TradingView](https://news.google.com/rss/articles/CBMiogFBVV95cUxQUDJEOURraWNkd1BLeVV3dFhyUGdfQUZGNlBmZUtELVJjMHJXSzdkZWcwWWM1eHZoNW5UTHM3Y2F5X3N0aEI1WmhJb21zdXBRbVpnSE5wa01zTVhqQk5ST2djaVJCeU9jc0tzU2lTNkppWVhfdEx6Q0NIZGRQQU1ONEkxTnJ1Z1IyZEZLTzNoVjFFamNFMk9JREUzZlpGTVh0b3c?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 14 May 2026 19:03:00 GMT
- [Why I'd Rather Own Micron Stock Than Sandisk - The Globe and Mail](https://news.google.com/rss/articles/CBMixgFBVV95cUxPcllSNHJZR2QzNmdPWFhkX0NBVk5DYzdPdE9GSEdvWkN4Y1pSSGxmNlBhNzVBTVVZLXBoOV9KdWJTeVFIQWpXdG5zTXh4UjhCVm5qanlSdmE4Y1ctcUtzSUFHd0NVbGFrS01XN19ISFU2NUVHYTRkZUVvNWdPRkxPelV4eHJXVk1oUXNwY3o2V0tXV0hHUWZvVTU0VTVXcjY2NXhkRUJNMzV0UEF4aXFYTDRYeHBxaXY0OVdpbGRNUlM4Z2Yxb1E?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 14 May 2026 04:50:00 GMT

## 新興題材：奇鋐看好今年營收

摘要：新興題材：奇鋐看好今年營收 相關新聞集中在：奇鋐看好今年營收及獲利逐季成長 針對散熱模組修改設計釋疑 - news.cnyes.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.42 | 0.00% | +5.80% | 2,555.00 | 2,835.00 | -9.88% | 未明確 | 61.06 | 41.98 | 15.63B TWD / 71.62% | 2026-05-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐」，共 1 篇新聞命中。 方向判斷命中詞：成長。

### 主要來源

- [奇鋐看好今年營收及獲利逐季成長 針對散熱模組修改設計釋疑 - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTE1rT2dIQUlJZEZtT0s3amhLcGNhS1phV2h1akJxMkVsNFhxNHF5c1p1dEVJMVE0aDFhT0JoTzllUkU2R3NVaktIejdiSkI0NEU?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 14 May 2026 11:19:40 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：《台股盤後》收漲377點、42K未攻克，惟收復5日線- 新聞 - MoneyDJ理財網；台股ETF規模首破6兆，主動式、科技型增幅靚- 新聞 - MoneyDJ理財網；【台股操盤人筆記】市場過熱後的冷卻期，關鍵留意七月-報告內容-基金 - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》收漲377點、42K未攻克，惟收復5日線- 新聞 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikgFBVV95cUxPSGhxQ2VNR3VJS2k0TlBtZ1ItUlFWcEVPSTR6dWh4OEJud0VQaHBmODNiRUxkSjBWNGo0bFJpdVNvR2p1VmhCYzlzdHdEcHJlNlQ3bHNVaHVDZHB3d29ENkNON09LYUhMbFgwbmFhcHhpbE9Vc2VLeGotRE9JNVhmOFZwNTJsZkE3NTktNnotR0lQZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 14 May 2026 08:02:00 GMT
- [台股ETF規模首破6兆，主動式、科技型增幅靚- 新聞 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikgFBVV95cUxOU2o2ZDd2ZFRGMVNTMmtXeHRsWXVGaHdpa1R3X3d6VHdUOWJSZHdpQy1hTTRHSzUyaGt4bVh1WWhtV29lbHBHSlY5ZTFKTGJnSnk4SW1rTVQxYjlDSjZqazIxSE84SHdmYXNuaXFVdlFsZDhrU0tTNTdUUjJza1p3UERQUUZrYXBScmRSZVNtVXdzQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 14 May 2026 03:25:00 GMT
- [【台股操盤人筆記】市場過熱後的冷卻期，關鍵留意七月-報告內容-基金 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMimAFBVV95cUxObnlIQzR4bG80eThzVWwzbnRaREtXU0djVXMtTmlEa2RvQUlkTFQ0XzhHUGxEWnM3ZjNHeVlNV2Qxd3pjcEYxSGlyM3lQT09xS2JqMGNWbWMxSEtEYUFpYmJnRnBCbGhiQU43SDVXc0Z0M09YbXp3Y2JxZm9FQ0pyaTZ3aUZSYldmOEk2R09LQm80dUMyU1dZeA?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 14 May 2026 01:59:00 GMT

## 新興題材：卻回殺跌停

摘要：新興題材：卻回殺跌停 相關新聞集中在：台股51千金創紀錄！高價股重返最強主力 8檔飆天價、「它」卻回殺跌停 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股51千金創紀錄！高價股重返最強主力 8檔飆天價、「它」卻回殺跌停 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBkOG80WlRSaGVBbEw5eGNGRjhCN2FIOXVxRUJWbWQtMENiSDRyVmR6SkV2d0QwTW1aRTBhV2ZGdDF6Y1pCR2V4NUQ5SENzbE0wSDZrYlB2eTRCZ9IBX0FVX3lxTFBENlBxeHM0aGdqbE1MSDlrQ21HZmVxZVM1RDRDWWNkQXViTE9EcGMxcnFoYjVvNV9BemlRdUkzcnNzSzJBYUM4N0ZQbHRnbXlfTjM3TThTM2xkNk9vNGJR?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 13 May 2026 09:00:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
