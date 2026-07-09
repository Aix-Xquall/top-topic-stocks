# 每日股市熱門話題分析 - 2026-07-10

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **散熱與液冷供應鏈**｜負向｜熱度 3｜市場確認 100.00｜同向 1/1
2. **AI 伺服器與資料中心**｜負向｜熱度 9｜市場確認 69.97｜同向 5/6
3. **半導體與晶片供應鏈**｜中性｜熱度 8｜市場確認 N/A｜同向 0/0
4. **新興題材：TradingKey**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
5. **記憶體與 HBM 供應鏈**｜正向｜熱度 11｜市場確認 38.85｜同向 1/2

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.55（樣本 9）
- 5日相關係數：0.05（樣本 9）
- 同向比例：7/9

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 散熱與液冷供應鏈 | 100.00 | 1/1 | 0 | +11.99% | +14.23% |
| AI 伺服器與資料中心 | 69.97 | 5/6 | 0 | +3.88% | -0.53% |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：TradingKey | N/A | 0/0 | 0 | N/A | N/A |
| 記憶體與 HBM 供應鏈 | 38.85 | 1/2 | 1 | +1.28% | +3.85% |
| 新興題材：OpenAI | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-06-27 | 0.12 | 0.29 | +57.89% | 19 |
| 2026-06-28 | 0.16 | 0.55 | +85.71% | 14 |
| 2026-06-29 | 0.49 | -0.25 | +38.46% | 13 |
| 2026-06-30 | 0.44 | -0.27 | +62.50% | 8 |
| 2026-07-01 | -0.08 | 0.25 | +30.77% | 13 |
| 2026-07-02 | 0.30 | 0.03 | +55.56% | 9 |
| 2026-07-03 | 0.21 | 0.08 | +55.56% | 18 |
| 2026-07-04 | -0.22 | -0.36 | +22.22% | 18 |
| 2026-07-05 | -0.00 | 0.24 | +40.00% | 10 |
| 2026-07-06 | N/A | N/A | 0.00% | 2 |
| 2026-07-07 | N/A | N/A | 0.00% | 1 |
| 2026-07-08 | -0.05 | -0.05 | +71.43% | 14 |
| 2026-07-09 | -0.11 | -0.36 | +64.29% | 14 |
| 2026-07-10 | 0.55 | 0.05 | +77.78% | 9 |

## 歷史回測摘要

- 回測日期：2026-07-10
- 近5日 3日相關：-0.23
- 近5日 5日相關：0.21
- 同向比例：+14.29%
- 權重狀態：未調整

- 方向準確度：+14.29%
- 信心排序準確度：-0.23
- 診斷：方向與信心皆需修正

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

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：散熱三雄6月營收僅雙鴻月減；上半年皆同期高 - 台視全球資訊網；美系外資重申正向看法，奇鋐下半年營運可望優於上半年 - TechNews 科技新報；焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | -0.62 | -11.99% | -14.23% | 2,350.00 | 2,835.00 | -17.11% | 同向 | 61.06 | 38.61 | 17.62B TWD / 66.11% | 2026-07-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱、奇鋐」，共 3 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：跌停。

### 主要來源

- [散熱三雄6月營收僅雙鴻月減；上半年皆同期高 - 台視全球資訊網](https://news.google.com/rss/articles/CBMikgFBVV95cUxPRmxvNEpjZFpLMm5pZXh2TTN4VTA4eWJmanNXNDRPR094Nk9ZUUdLY3Y3VmNSeUtVdkJpc09TM0Y1UDM0ZkhiU05QYVJhMWtmdjIyT0ZBMDBsNi03NWZmRGJTSUlrckxLSGZNdll0eXdHdWYwcFdNTm5kcVIxTGl3U1N2Y3l0b1ZzVUZiRjVzWEJWUQ?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 08 Jul 2026 02:32:06 GMT
- [美系外資重申正向看法，奇鋐下半年營運可望優於上半年 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiXEFVX3lxTE9tQkN3UDY5eV9KLWVjSG5BYXBOU19SUl9QUGpzaHo1dVB4d1BpRHdmZ0d6cTBXUGNfSEo4YlBMWllfQk9TZGdzRV9XS1pkZWQ0Nm5IVEhjT09IeEkt?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 08 Jul 2026 02:08:57 GMT
- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 09 Jul 2026 04:46:29 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：傳統 ERP 導入如何藉由 AI 加值服務，轉化為企業決策的關鍵動能？ - TechNews 科技新報；面對 AI 幻覺，如何確保教育內容正確性？ - TechNews 科技新報；排除爭議議題，AI 教育是否削弱獨立思考？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | -0.59 | -3.96% | +16.27% | 202.78 | 211.14 | -3.96% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | -0.57 | -1.83% | -2.03% | 2,415.00 | 2,465.00 | -2.03% | 同向 | 74.39 | 32.47 | 416.98B TWD / 30.09% | 2026-06-01 |
| INTC 英特爾 | 產業/供應鏈推估 | -0.08 | N/A | N/A | 112.54 | 114.68 | -1.87% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | -0.06 | N/A | N/A | 546.72 | 546.72 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 產業/供應鏈推估 | -0.04 | -2.13% | -24.14% | 384.36 | 506.69 | -24.14% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -10.22% | +29.60% | 401.11 | 446.77 | -10.22% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.03 | -0.29% | -6.88% | 677.00 | 680.00 | -0.44% | 未明確 | 10.86 | 62.86 | 65.78B TWD / 32.86% | 2026-07-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.04 | -4.85% | -9.67% | 3,925.00 | 4,310.00 | -8.93% | 同向 | 62.91 | 62.55 | 47.43B TWD / 4.99% | 2026-06-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 同時符合主題標籤：AI, advanced packaging, CoWoS, AI server。
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [傳統 ERP 導入如何藉由 AI 加值服務，轉化為企業決策的關鍵動能？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBxNHNELVdfUGFZdUhMVlEwekFoUDhoRVJILU5Tb3M5T3VpWmtPczdWU1hUR2hTN25iSnRhS0hFbVpkZ0wxLUhVTUhmSHJpSHVOYTZGMFloNG9CanM?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 09 Jul 2026 20:40:42 GMT
- [面對 AI 幻覺，如何確保教育內容正確性？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMisAFBVV95cUxQeUFuYlpqeWE1MWhLazZjTE95c25GQVVobmJDVkFmOWJfdFFfUERpT1c0RXJaVXRBZ24waUQ1OWpLeWRRWFBnZ0xXUzBVLUNHS3FpZ3kzVU1idTNtekZhZ2Z5YWZ1bHpkSDFWWldRS3MtOUZkRVdEc2d0bFc4bllsN1pfQ3gxb1F1NWFxMk1FUTJ6eFA5ak5FY2xvSVZfcHRDQnVmNUhCNE5YSTd1MFVzQQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 09 Jul 2026 20:07:47 GMT
- [排除爭議議題，AI 教育是否削弱獨立思考？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMisAFBVV95cUxOY1p2S1RlOVd3bjhOU3Z1Nkxic0xVeEtMZmdUU0g2U3lES01yWHpSdWFud0RLMTF1eVM0b2cwSDJLUDlDQ0RBaUFOQUlzLW9sRFRGWlBCdFljZ2gtcGFHSERYODN5Zmh6OWhfR1dNV3BlNzNlejJOdHk1akEzTFZlQ19MMEk2dzJkeEY0dTNxT0tLbndWM3NmeXltUksyTVVTT241aHpERDFJNUtpbGtIUQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 09 Jul 2026 20:11:19 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：AMD Jumps 7%, Intel Climbs 5%, Broadcom Rises 2% as Tom Lee Calls the Chip Selloff a Buying Opportunity - 24/7 Wall St.；科技半導體業南遷UPS設高雄服務中心- 日報 - 工商時報；晶片 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 112.54 | 114.68 | -1.87% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | 0.00 | -1.83% | -2.03% | 2,415.00 | 2,465.00 | -2.03% | 不適用 | 74.39 | 32.47 | 416.98B TWD / 30.09% | 2026-06-01 |
| NVDA 輝達 | 新聞直接提及 | 0.00 | -3.96% | +16.27% | 202.78 | 211.14 | -3.96% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | N/A | N/A | 546.72 | 546.72 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | 0.00 | -10.22% | +29.60% | 401.11 | 446.77 | -10.22% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | -6.02% | -5.74% | 156.00 | 164.50 | -5.17% | 不適用 | 4.00 | 39.20 | 23.12B TWD / 22.85% | 2026-07-01 |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 991.64 | 991.64 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | +6.53% | -8.56% | 1,858.27 | 2,335.00 | -20.42% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip, foundry。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AMD Jumps 7%, Intel Climbs 5%, Broadcom Rises 2% as Tom Lee Calls the Chip Selloff a Buying Opportunity - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi2gFBVV95cUxOcnZhekZUem9ORFhNVWZSaFJ3SmEyOG0tai00d211T25hTkxVejVJT3Rxa0pwVWk3NmM3bGZvbUdVb2d4QTZtdWZhdjFNY0xIQ3c2ME5BdVA4M19aV3hwbFlPd3h2bXVCcjNWcWpVOFhaT3E4QXBqQWUyVmFpTjZrQWlYTU81RTdnak93Nk9PdnBLeWFFbXFvelJwZ1VKN0NiNG1YdTlSV1JEcnR1QmI0MVctWWRCQXRUci15N1FiS19pUUQ1dkxYdWEwVnp5WE1pbjlibE1TYkNfdw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 09 Jul 2026 14:04:48 GMT
- [科技半導體業南遷UPS設高雄服務中心- 日報 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE85ODRXVlhQSjVrdkFSTEVLZWxrdndSQkNKWV9VN2diYnZyNk90VXF2cEhXUzNhbEZ1VTZyX3Q2S2ZZR09aenB5dmRDZl9aY1pMVFhUNzRvcFlCNXluYkdv?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 09 Jul 2026 19:00:00 GMT
- [晶片 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiZEFVX3lxTFBJM3dlNnhlb04xRDhjejNuM1pDT1kzdTJkcWFieFg3SkFLTVRwY0huSmhFRmpadzVUVUY1QkJoUE83M1hmSFJDZkx4V21oWERJS3FwZmNYRlNjMkF5anpud0kwRWE?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 09 Jul 2026 22:06:03 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Intel (INTC) Stock Price Prediction: Perplexity Chose Nvidia Over Intel — Can $113 Hold Into July 23 Earnings? - TradingKey；Micron Technology Inc Stock (MU) Moved Up by 8.87% on Jul 9: Facts Behind the Movement - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | 0.00 | -3.96% | +16.27% | 202.78 | 211.14 | -3.96% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 112.54 | 114.68 | -1.87% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 991.64 | 991.64 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MU：新聞直接提及「MU」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel (INTC) Stock Price Prediction: Perplexity Chose Nvidia Over Intel — Can $113 Hold Into July 23 Earnings? - TradingKey](https://news.google.com/rss/articles/CBMi1AFBVV95cUxObnUxRzhfQlUySTZiSDlySTFtdVRoQlo1Wkc5MG5sWEw1MG5fTHltSF9oYmRidzk2VjBuY3lvV1lwTDN0eEd6eDE2MkpqM0plZXpkSHJZbWlRemwzN2dVc2hoMHZKTkZGaG5DUTFDRktFck1rODlsTjRSWk5kX3dVN1FrSklWSjlCd2sxNHNzRDVfLTRzYlVTNEFTWlN0NlYxeGdfSE84SVFmMVltZ3FodlpodldUc0Nfa3plZkdHbUE3Q09aNnFYdXZYajV5R2o2VVZ6dA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 09 Jul 2026 14:04:58 GMT
- [Micron Technology Inc Stock (MU) Moved Up by 8.87% on Jul 9: Facts Behind the Movement - TradingKey](https://news.google.com/rss/articles/CBMiiAFBVV95cUxQZEVOdkpQQzl6QjNadHBPVUFac2stTnUyRG1rTGdzWmkxYk9QQ0Z1d0FTZEp1ZHpDY1lkSFVPSU1SNzlxZjZvNWxkUk9NLUxmZ2ptZ19DYzdHWjR4aHFta1FscGEwWHpOQlhPX3U3Q3NXcTJuZmFLSnhKc19OeWIxTWJwVEt5WDhU?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 09 Jul 2026 14:15:11 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：MU, WDC, INTC: Why Are Chip Stocks Rebounding In Premarket Trading Today? - Yahoo Finance；Micron Is Up 700%. It's Still Cheaper Than Nvidia, AMD And Even Intel - Benzinga；Micron Vs. Intel: Which Volatile Memory Giant Should Investors Buy Now? - 24/7 Wall St.

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.62 | N/A | N/A | 991.64 | 991.64 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.62 | +6.53% | -8.56% | 1,858.27 | 2,335.00 | -20.42% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.61 | N/A | N/A | 112.54 | 114.68 | -1.87% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.23 | -3.96% | +16.27% | 202.78 | 211.14 | -3.96% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.45 | N/A | N/A | 546.72 | 546.72 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron、Micron Technology」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：surge。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：surge。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- INTC：新聞直接提及「INTC、Intel」，共 3 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [MU, WDC, INTC: Why Are Chip Stocks Rebounding In Premarket Trading Today? - Yahoo Finance](https://news.google.com/rss/articles/CBMijgFBVV95cUxPUGlvNlc0cG0xRDlFRjFaMjk4dDR0UjVWUThaWjJEdHNHaTBPaDZJUGZwVHNaSEhkZDExbEtwd2JuMi0tVWx0QVBhMXhJaEpfaUtqMTlBbzkteXlCbmFqRURuR0QyQW1XSnZTWmNCVDFUckQ2NFM5Q1NiS1ZfNlh3cmJsdnJhLWVqaXpoeEJn?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 09 Jul 2026 09:05:20 GMT
- [Micron Is Up 700%. It's Still Cheaper Than Nvidia, AMD And Even Intel - Benzinga](https://news.google.com/rss/articles/CBMiswFBVV95cUxNcGE3Nm1oYjYyQ3htcmVzMGpuOXA2dU1iYllTeFBPT0EyandLekZBTDFTSGx5T2VQVUpqQTZVY3VHYkdaOTFOQTNCLVpscm1Ca2pCTWtqcTBKaFZvZzQ2TmlNY3VSdnJLQkFGdjdOeDA3OXJ2WGNONXVYcVFxQXliaXU3dGllT3A3dW5hSnRXbzM0T1VzVXNzOFNYeWR3LVhPVGxFaDZLNlVkUHpwdlQtd0hoOA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 09 Jul 2026 12:35:46 GMT
- [Micron Vs. Intel: Which Volatile Memory Giant Should Investors Buy Now? - 24/7 Wall St.](https://news.google.com/rss/articles/CBMisgFBVV95cUxNdy1qODN4RTI2TzdiajU2VzB6QkNUbkpvRmlGUVhqcS12UUhydWFtZHdFelk5aEkyT3ZmaFJfaTdaM0JiWU1uaGNoQUM3MEJVLWJkTGY5enF4cGlpMVVGUk4tejRwX1BUX1V6WDVDUGJPMGlxcjRwcXRDeUoxVXIzQXBxR1dSdm5zMThXcHBpOFJaVnhiQ2JWbldKenpkTk5PRWc2czN2NVNxWk9VUjFaTGVB?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 09 Jul 2026 18:23:10 GMT

## 新興題材：OpenAI

摘要：新興題材：OpenAI 相關新聞集中在：OpenAI launches ChatGPT Work, deepening race for workplace AI tools - Reuters；Meta jumps into AI coding market in effort to chase Anthropic and OpenAI - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 新聞直接提及 | 0.00 | -2.13% | -24.14% | 384.36 | 506.69 | -24.14% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：新聞直接提及「OpenAI」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [OpenAI launches ChatGPT Work, deepening race for workplace AI tools - Reuters](https://news.google.com/rss/articles/CBMifkFVX3lxTE1wemJKWTFORXd6YmVORDljMUFEUGZmMlllRmlfX0lSRGpicmFuRmQ2NFNwV0hNWnhrZmZsamZGMXYyM1JGemZ0ODBnaXo0anRwZk81RzA3ZmY2VkZMYnVld2dHQV9FUFNEYjd3Sy1HNmUtdnRIbkx6Mnc0ZDVfQQ?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 09 Jul 2026 18:51:55 GMT
- [Meta jumps into AI coding market in effort to chase Anthropic and OpenAI - CNBC](https://news.google.com/rss/articles/CBMioAFBVV95cUxOa1dxU1JNM2gybUFmVWR1STVhX2VWVGVGWGhxMEdXX0RBR243dGIzaDBqR1NCS2VSX2Z6ZVFXa181QUZSeHB0SDNhM25wYzNzYk1iY1NObWs3bE5iNlZKdC1jMmFhaklWNHpLQlN6UU5UT01HalhfY0hRRWFzbVk1ZDVSR1V1X1VuMTBsMFlMb0c0eTdVcnU0bDQ1aFE3NTFw0gGmAUFVX3lxTE1nWm5QWUJiRDFLYkZVcEdjUjZJcHlyRXItanp5YUhRSkRIMjVIRFd4YW5uYmlkWjNaLW4yY3FjanBOV2ZlUDY0TjFBZkVaeXh2NzFSdzVoYUZGQlpGaGUzMWVYNHktMkVrRVJWakdxbExxUjRyMVd2VDh0bF9SeG11VTNHRXIwdWFzdmlaNGZ4TzB1RXYteTI0aWFVcmJRQkRMNFpSNEE?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 09 Jul 2026 14:00:01 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股開盤漲11.59點 - 經濟日報；台股 ETF 雙族群 犀利 - 經濟日報；台股掀交易變革　金管會3面向促券商強化系統穩定性 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股開盤漲11.59點 - 經濟日報](https://news.google.com/rss/articles/CBMif0FVX3lxTE9QaUN5Q05vb2UtbnRfUzdqWHBVT3ZhVTh4MW03QmxHYlYyZDJyd25ybDVmUTQxdlRrTUJFT29MYktYeHJSeUoxdm5vUlBfRzNwT3hXRldYb2c5UmVLVTdWbC10RTE3T2lDZzFRMzJfa3dOME5HRVFsVm4tZ1F2V2PSAV9BVV95cUxOd21JM08xanhnSU4yU0ZVR1duRm9pZWpsSl9XS2NVMzhXQ0JQdnNmaklRTThRZ0JhQjJoWklxR2kzdWZuLVFJOWNJWXFLUG1qbU9vX3FQT2lyc29pUnVVbw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 09 Jul 2026 20:41:21 GMT
- [台股 ETF 雙族群 犀利 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxPZ3lqWFF1UnBGdEtPM1VmakkwVmRYUFNZRGZFSC1vQWZvLUVTUFpiN2dzRUJHcjhZTXhSRHZVeGc4SEpDcXYzWXRjaXFSRmxhYTdPY0owQUgwYkdiSDlpTHR3c1FPQW40VERwazVCYmM3SE9xdi1sbDF3aFQySFVnMNIBX0FVX3lxTE1CQ3hyd0xqM2lLdlJpUUN0V2FPN3RNZjcxdVEyX1F0anpxN19SNlNwa1NQZnp3eVN4LXlsUDlnMUh6Ymd6cmF1ZllGcG9neEVEejZSUGsxd01ESTN4MlR3?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 09 Jul 2026 18:26:24 GMT
- [台股掀交易變革　金管會3面向促券商強化系統穩定性 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBZNTlFMWJBbmtaMUZZS3FDRUxuejlBVWVXeW55ZFM0S1Z5RXE5NFpkMmlmV1lvMVhFOWtvUDAwVDg2LXE2enpydmMzZFp1eUNYV2oycU9zOEJ0QdIBX0FVX3lxTE1WNmZTSS1UdW4yYXNhdGN2QzVyb20tWGNTTGsyVUNld2ZhRGFrV19YMVpBa0FfRE10dnAxaGp2d3lFeE8xUGhtZzc3clRoRmNpMjlSbFlEOGNEYUZDbVJz?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 09 Jul 2026 11:38:16 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：台股交易制度迎變革金管會促券商三面向強化系統- 新聞 - MoneyDJ；中茂 115年6月營收284萬、年增29.87% - MoneyDJ；能率 115年6月營收7.79億、年增9.16% - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股交易制度迎變革金管會促券商三面向強化系統- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNMmE4cDVqWFN0dFNUVlhyZXN0UVdOVFJydnBnbERBY2d5bTlreTFGOGtYVVozUVNmbzROV0FBdlBxYTlYYkFfNUNrRjhEdFhlVWlxMkdkM255M3BVTFFnMndCR3RhUmowSXpjWC1MSGwxdW80TTBMcVowQVVITW1naW1QSnhyeDZ5QzZWWnJ1dEVJdw?oc=5) - Google News source discovery | MoneyDJ Thu, 09 Jul 2026 20:39:00 GMT
- [中茂 115年6月營收284萬、年增29.87% - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNbmw0bnc0eGJxVTZsNERhajZRbVdsdGZzcExuSGU5My12YjdTWC1QV3BnZkNKXy1VV1Y0UEp2clRqX2VSdkxPVXRSLW9naGxEUjFRMk9wTEFfTWEzT3h5VVU2RW9lRDRTc1lreFJnTjJhY0U0d1NKbUdDTm5kRUtxMUtEZVU0b0hjdzFBNHNpSUllZw?oc=5) - Google News source discovery | MoneyDJ Thu, 09 Jul 2026 16:14:00 GMT
- [能率 115年6月營收7.79億、年增9.16% - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNc3M4NVAzUExfYU1KRXFHeW5vd0FLYUpHUnNFaWhyTmxJZnNRMEVEZ1RTclB6MXF2Z1piTUtiWTBlMjdGdDFRalI3OXB5WHZDQ21iN3I3ZmNaT2xHVjAxUURSdzFPcThGWVlROHpuTnNBOXY3elQ2NHRKOXZwRVlZSWxXMmNoR2dUN0VnVE42X2Nxdw?oc=5) - Google News source discovery | MoneyDJ Thu, 09 Jul 2026 15:54:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
