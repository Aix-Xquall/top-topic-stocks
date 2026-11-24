# 每日股市熱門話題分析 - 2026-11-24

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **利率與成長股估值**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0
2. **綜合市場情緒**｜中性｜熱度 41｜市場確認 0.00｜同向 0/3
3. **AI 伺服器與資料中心**｜正向｜熱度 21｜市場確認 0.00｜同向 1/8
4. **半導體與晶片供應鏈**｜正向｜熱度 5｜市場確認 0.00｜同向 0/8
5. **新興題材：MoneyDJ**｜正向｜熱度 12｜市場確認 0.00｜同向 0/2

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.41（樣本 27）
- 5日相關係數：0.30（樣本 23）
- 同向比例：1/27

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | 0.00 | 0/3 | 3 | -6.06% | -6.17% |
| AI 伺服器與資料中心 | 0.00 | 1/8 | 7 | -14.29% | -1.95% |
| 半導體與晶片供應鏈 | 0.00 | 0/8 | 8 | -18.01% | -4.20% |
| 新興題材：MoneyDJ | 0.00 | 0/2 | 2 | -17.20% | -13.06% |
| 散熱與液冷供應鏈 | 0.00 | 0/2 | 2 | -20.31% | -15.73% |
| 新興題材：TradingKey | 0.00 | 0/1 | 1 | -47.98% | +47.09% |
| 記憶體與 HBM 供應鏈 | 0.00 | 0/3 | 3 | -20.51% | -18.61% |

### 方法調整建議

- 方向信心與股價呈負相關；應檢查正負向詞庫，並降低新聞直接提及但股價背離的權重。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
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
| 2026-11-24 | -0.41 | 0.30 | +3.70% | 27 |

## 歷史回測摘要

- 回測日期：2026-11-24
- 近5日 3日相關：0.05
- 近5日 5日相關：0.13
- 同向比例：+48.00%
- 權重狀態：未調整

- 方向準確度：+48.00%
- 信心排序準確度：0.05
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

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：永豐金：台股估值落歷史低檔，明年起迎回升行情- 新聞 - MoneyDJ

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +9.39% | +0.10% | 492.50 | 507.29 | -2.92% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [永豐金：台股估值落歷史低檔，明年起迎回升行情- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxOTDl2RVBoakdOWVV5YVBpS1JFeVRKcnMtUVdSbUc4bENLTUFka2lwZXE3eW5HZUtGVXgzSlExN1BJaTNSLVZpb1QtbnpuZS1pNmt4Sm8wQjlqUVFtV1BRdm5oOERrZzBodEtMc0dXdUt0eFFPNVBSUGVXbHJ2MkZzandIcHFHVXRnUzB4ZkNVcFBFdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 23 Nov 2026 06:50:00 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：搶救台股大作戰 全員動起來 卓揆今邀金融、科技、工商界代表座談 - 經濟日報；政府護盤見效？台股盤中狂飆千點 聯發科、台達電等權值攻漲停 - 經濟日報；台股反彈外資還是賣超289億元 賣最多的竟是這檔市值 ETF - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | +0.24 | -6.67% | -8.35% | 2,230.00 | 2,480.00 | -10.08% | 背離 | 98.27 | 20.66 | 586.89B TWD / 59.71% | 2026-11-01 |
| 2454 聯發科 | 新聞直接提及 | +0.24 | -6.47% | -2.90% | 4,050.00 | 4,920.00 | -17.68% | 背離 | 62.35 | 59.27 | 55.03B TWD / 5.77% | 2026-11-01 |
| 2303 聯電 | 新聞直接提及 | +0.24 | -5.05% | -7.25% | 97.10 | 164.50 | -40.97% | 背離 | 6.80 | 13.04 | 25.20B TWD / 18.33% | 2026-11-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 方向判斷命中詞：漲停。
- 2454：新聞直接提及「聯發科」，共 1 篇新聞命中。 方向判斷命中詞：漲停。
- 2303：新聞直接提及「聯電」，共 1 篇新聞命中。 方向判斷命中詞：漲停。

### 主要來源

- [搶救台股大作戰 全員動起來 卓揆今邀金融、科技、工商界代表座談 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBqUGtocWpmQVBHRzhuX09NR19vRzNNWUdKZFJlV281QkxLbGlKUkxuUVNEa3B0X1RrTEJ6T1NDbWY3Rks3bEhrZHBFQzlFUVJnR0R1VjlmMjlxd9IBX0FVX3lxTE1PVEo1SUxjemdjVDdvdFlxY0xSUFFvMnV5SlFrdG1LWm9hU2FNTS1wRVcwYVdXMUF5Z2JZd0trNnhwMVktVjRhQjhWNjQwT2FaOU1TMVhTR01xVG5JSEZF?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 22 Nov 2026 17:38:58 GMT
- [政府護盤見效？台股盤中狂飆千點 聯發科、台達電等權值攻漲停 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1aYU1vcmRYSHRpem5ROTMwWDlMenlmTWVKVExTWHFOQTk2aFV0WVFzQmxJX3BpWFdmV0NyMkpkQTRkTEJyOGhRdXpuai05VG1pS2R5THVwUEQzUdIBX0FVX3lxTE5NYVQ4bl9UV0duQXB0dUZ0c1V1YzJBMUh1WFJYTm4zbHVuZ05SQ3BVNU5lcDZQUjdub2xFV1JsTi1sMVlNM2IwODR5UjFaY1ZaQ2Q2OXQ4SmJJLXdNS0JZ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 22 Nov 2026 08:00:00 GMT
- [台股反彈外資還是賣超289億元 賣最多的竟是這檔市值 ETF - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBkWkRtMnZFemFkMmtvdHRwcV80R3NISlZoNXlTd3RzSWc0OTVwLUd2aXJPai1uU3lTZG5PVTk3S0ZFMGQtYTJLTktWNWtiM0N5NTlpSzFabXRNQdIBX0FVX3lxTE1YQUxTaTE4amxFTGNPZDJkdUpwSWY1WmR5QV95RzFMN1c4SmlCaXRFZGhwU1pUNDdRTlJTTEVpNW1LTV93aTI3cjk3VEh1YnAtMTYxQ29IbWh3NHMzTXd3?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 23 Nov 2026 08:00:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel (INTC) Chip Breakthrough Opens A Fresh Angle On Its AI Push - Simply Wall St；Wall Street Is Focused on AI Software. But the Real Money Could Be Made Somewhere Else - 24/7 Wall St.；資料中心開不了！馬斯克：AI產業明年「瘋狂缺錢」數千億美元從哪來？ - 工商時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.31 | -47.98% | +47.09% | 59.66 | 114.68 | -47.98% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.03 | -27.73% | -17.78% | 165.05 | 228.38 | -27.73% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.03 | -12.14% | N/A | 453.46 | 516.10 | -12.14% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.03 | -6.67% | -8.35% | 2,230.00 | 2,480.00 | -10.08% | 背離 | 98.27 | 20.66 | 586.89B TWD / 59.71% | 2026-11-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | +9.39% | +0.10% | 492.50 | 507.29 | -2.92% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -10.72% | -19.45% | 313.55 | 446.77 | -29.82% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.02 | -12.04% | -12.36% | 530.00 | 703.00 | -24.61% | 背離 | 17.55 | 27.67 | 88.62B TWD / 47.13% | 2026-11-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.02 | -6.47% | -2.90% | 4,050.00 | 4,920.00 | -17.68% | 背離 | 62.35 | 59.27 | 55.03B TWD / 5.77% | 2026-11-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：續強。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 5 篇新聞出現相關標籤。 方向判斷命中詞：續強。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 5 篇新聞出現相關標籤。 方向判斷命中詞：續強。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel (INTC) Chip Breakthrough Opens A Fresh Angle On Its AI Push - Simply Wall St](https://news.google.com/rss/articles/CBMizwFBVV95cUxOMFVnTEhsQmRscnNQUEpoZnpyQWNHYWw4dldMLWVPR2dXMHdxTmltU2xlajZvZy1tdzZacE96VEphZEJPMWZ4X0lOT1VVVnlsQUhZMVZaWGoyeGVBeFN3aF9BY1dIQzFEcmg1czlyZGI5MXJhU3dOaThNMmtrc3AzT3VEbzVKTVk1OVhYaEtIdm5GRk5aN2dVYml0SXNnSjhTWTFVcWdod2F4QXp6VDJyb1o4NmtzR1hfdlVWak5naFRqM0V0cUlkR2t5eHdXVzjSAc8BQVVfeXFMTjBVZ0xIbEJkbHJzUFBKaGZ6ckFjR2FsOHZXTC1lT0dnVzB3cU5pbVNsZWo2b2ctbXc2WnBPelRKYWRCTzFmeF9JTk9VVVZ5bEFIWTFWWlhqMnhlQXhTd2hfQWNXSEMxRHJoNXM5cmRiOTFyYVN3Tmk4TTJra3NwM091RG81Sk1ZNTlYWGhLSHZuRkZOWjdnVWJpdElzZ0o4U1kxVXFnaHdheEF6elQycm9aODZrc0dYX3ZVVmpOZ2hUajNFdHFJZEdreXh3V1c4?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 22 Nov 2026 23:12:52 GMT
- [Wall Street Is Focused on AI Software. But the Real Money Could Be Made Somewhere Else - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiyAFBVV95cUxPdGViSHAxSk1qRC13Qk5fSkZCVEJoeTNabnBta2ZUcWg0dHNuYUhhTEVlcjRkbU8wY2lqZi1IaGd2OVFJeVJCQVJNWVIzUlhld1BOQ081dDhDNXNYNVMwS29jUi1ZM0xnbndPTzA0MkFHQ2MxbXNQWlBvZmk3TkIyMUM2UWNNQlBDQk44WTkzTHNLajhBalNZVm9SUV9HM25uamRGa1oxaHRPVFdoUmxHTWUxUEs3X25DLU5OVlZkWTBTMlJiTzJTTw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 23 Nov 2026 16:03:00 GMT
- [資料中心開不了！馬斯克：AI產業明年「瘋狂缺錢」數千億美元從哪來？ - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE01MVE1OHViZDZENW9BalhlYzBVZkUyMzByT2tHUGhKVVFjbVNYVzlyRHlFVHJiNllzMlVSMzRnZDFnSHlsQUZoanRNbDhuNHFzdmdqUkYwaEJYdnJiWVhZ?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 23 Nov 2026 01:44:00 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Taiwan Semiconductor Rallies 17% as Jensen Huang's Return to NVIDIA Lifts Chip Stocks; Intel Surges 15%, AMD Jumps 8% - 24/7 Wall St.；Intel (INTC) Chip Breakthrough Opens A Fresh Angle On Its AI Push - Simply Wall St；通吃半導體、人形機器人與 CPO！東佑達「全自製」攻高階設備商機 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.33 | -47.98% | +47.09% | 59.66 | 114.68 | -47.98% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | +0.29 | -6.67% | -8.35% | 2,230.00 | 2,480.00 | -10.08% | 背離 | 98.27 | 20.66 | 586.89B TWD / 59.71% | 2026-11-01 |
| NVDA 輝達 | 新聞直接提及 | +0.28 | -27.73% | -17.78% | 165.05 | 228.38 | -27.73% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.28 | -12.14% | N/A | 453.46 | 516.10 | -12.14% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2303 聯電 | 產業/供應鏈推估 | +0.03 | -5.05% | -7.25% | 97.10 | 164.50 | -40.97% | 背離 | 6.80 | 13.04 | 25.20B TWD / 18.33% | 2026-11-01 |
| MU 美光 | 產業/供應鏈推估 | +0.02 | -27.12% | N/A | 707.70 | 971.00 | -27.12% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.02 | -6.67% | -19.45% | 94.39 | 291.88 | -67.66% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -10.72% | -19.45% | 313.55 | 446.77 | -29.82% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel、INTC」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：surges。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「Taiwan Semiconductor」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip, foundry。 方向判斷命中詞：surges。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：surges。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Taiwan Semiconductor Rallies 17% as Jensen Huang's Return to NVIDIA Lifts Chip Stocks; Intel Surges 15%, AMD Jumps 8% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi6wFBVV95cUxPY3NBa1ZIRXJyUHFCWERaWWxiTGFoRW53aGY2Q1pqUzZQNmpiVGpQdG00T2hzVWpQNEN4Q0JBYlRja3FvdWhKaHpxVjVxQjRfQnlwRmc1Tm0tMFVVQjVNTzUzM29rbTlwWE5DZDNRYWM3aHQ0NkNzbGhIUExDa1F3MnhibXEwWEc3RzhUUzNIUkYtV1haWGtfYWdzNnlpaHFLU3dQS1R1dDZKVUx1SC1GczJ5UnMyTVF6alEyblVtdmIwdldnQjhIc01OaDgycmpQQ0pNQlBGaVRmWHJMS1ExemxsdFFVNkpLVEZn?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 23 Nov 2026 15:55:00 GMT
- [Intel (INTC) Chip Breakthrough Opens A Fresh Angle On Its AI Push - Simply Wall St](https://news.google.com/rss/articles/CBMizwFBVV95cUxOMFVnTEhsQmRscnNQUEpoZnpyQWNHYWw4dldMLWVPR2dXMHdxTmltU2xlajZvZy1tdzZacE96VEphZEJPMWZ4X0lOT1VVVnlsQUhZMVZaWGoyeGVBeFN3aF9BY1dIQzFEcmg1czlyZGI5MXJhU3dOaThNMmtrc3AzT3VEbzVKTVk1OVhYaEtIdm5GRk5aN2dVYml0SXNnSjhTWTFVcWdod2F4QXp6VDJyb1o4NmtzR1hfdlVWak5naFRqM0V0cUlkR2t5eHdXVzjSAc8BQVVfeXFMTjBVZ0xIbEJkbHJzUFBKaGZ6ckFjR2FsOHZXTC1lT0dnVzB3cU5pbVNsZWo2b2ctbXc2WnBPelRKYWRCTzFmeF9JTk9VVVZ5bEFIWTFWWlhqMnhlQXhTd2hfQWNXSEMxRHJoNXM5cmRiOTFyYVN3Tmk4TTJra3NwM091RG81Sk1ZNTlYWGhLSHZuRkZOWjdnVWJpdElzZ0o4U1kxVXFnaHdheEF6elQycm9aODZrc0dYX3ZVVmpOZ2hUajNFdHFJZEdreXh3V1c4?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 22 Nov 2026 23:12:52 GMT
- [通吃半導體、人形機器人與 CPO！東佑達「全自製」攻高階設備商機 - TechNews 科技新報](https://news.google.com/rss/articles/CBMicEFVX3lxTE5CNmRxOC00MkUzb2ZXQzBXUng2SENwZGNmQjF4WEJVaDktR0JUeEROTGJnWVpZZzg0WFNaLUZfcXFJNkd5bVZxRm9UWjVIX1FmcFZvbTdqM1AwSHU5RjN0di1HNDFCMUk1QUkxNHVrM00?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 24 Nov 2026 05:05:43 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：國票證券：台股將迎強勁反攻行情- 新聞 - MoneyDJ；統一證券：台股短線浮現跌深反彈契機- 新聞 - MoneyDJ；美股指數期貨最新報價 12:37-台股 - MoneyDJ

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.28 | -27.73% | -17.78% | 165.05 | 228.38 | -27.73% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | +0.24 | -6.67% | -8.35% | 2,230.00 | 2,480.00 | -10.08% | 背離 | 98.27 | 20.66 | 586.89B TWD / 59.71% | 2026-11-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 2 篇新聞命中。 方向判斷命中詞：漲停。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 方向判斷命中詞：漲停。

### 主要來源

- [國票證券：台股將迎強勁反攻行情- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPVFFpUXJUOUQ2d3BQSTI1SkFLTVNKYzVDblNpdUlNWFZhTTNudFZpTW50aXpXUXRwOWdmaHFkbHVlSl80XzN1UDJ3NlA4VlhCWXBUa2s0VDBrTFhhV0h5Yk0xOVdLSW5TT3RacXFGMTVxME5ZSWtnbmhfM2VRbF92bHM1ZVV3dGZHS0MyTlhrV1BtZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 24 Nov 2026 00:47:00 GMT
- [統一證券：台股短線浮現跌深反彈契機- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxOWEZGNGxhaHU5V1B1a2U0TU5EMHV6Qkc3em9JLXpwOTg4Rm94c2piRjFQdWliLU5pYWJrTE03bTJpUnZTb29sTFVJUHdZbzd6bHZsd29Ka2daVTFJSWJoNHlFTFNkRUhGeHdCdkRDN0Z1Q05EdHFhSGhUOTRwTnA5ektybUtrWERPS0FELWxFSlU5QQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 24 Nov 2026 00:47:00 GMT
- [美股指數期貨最新報價 12:37-台股 - MoneyDJ](https://news.google.com/rss/articles/CBMiigFBVV95cUxOZFF0SGdWWmR0X0ltMHR3bGNsemZCUExBVW45WW5CSUJwaE5BRlBqd2d0R3VoM1dpby0wZExFdlpsQUU2UEMwWGxYZkVQOUVQY0p6LTM0T0xhbnZJV0R2ZXlPY3BnZ2k5MlRadDZYb29pMF9BRkZQV1VtNi00OWhGdEpkTmJWRGhMYnc?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 24 Nov 2026 04:48:06 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：散熱雙雄戰1》奇鋐、雙鴻同喊明年ASIC超車 輝達獨大局面生變？ - 民報；累計EPS大賺73元！「散熱大廠」第三季獲利翻倍成長 輝達Vera Rubin量產帶飛 - Yahoo股市；【即時新聞】今日法人看好奇鋐液冷散熱出貨放量，第三季毛利率衝33.9%創新高！ - CMoney投資網誌

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.33 | -12.89% | -13.69% | 2,600.00 | 3,435.00 | -24.31% | 背離 | 90.78 | 26.14 | 22.10B TWD / 34.35% | 2026-11-01 |
| NVDA 輝達 | 新聞直接提及 | +0.28 | -27.73% | -17.78% | 165.05 | 228.38 | -27.73% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐、散熱」，共 4 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：成長, 放量。
- NVDA：新聞直接提及「輝達」，共 2 篇新聞命中。 方向判斷命中詞：成長。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [散熱雙雄戰1》奇鋐、雙鴻同喊明年ASIC超車 輝達獨大局面生變？ - 民報](https://news.google.com/rss/articles/CBMiZEFVX3lxTFBkTG1nSTVFWUx3bHl4S213UVNVVUZRX2QzSVA0LVF6bmNWUEMxTi12Nm1yYVNuSDNFbGgyd3kwN0dJcExCM09wbC1ZZjd2QmxwUFM0Ul9FbWNCejg2dXhRcVQ0OEY?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 22 Nov 2026 00:00:00 GMT
- [累計EPS大賺73元！「散熱大廠」第三季獲利翻倍成長 輝達Vera Rubin量產帶飛 - Yahoo股市](https://news.google.com/rss/articles/CBMikwNBVV95cUxQa0NTWENQd1d3UDNCYndMaTVlaVh0WFNnZk9GelVHWXVNSmdKWlhtYzU5dlZtVzVJOGs3NG40ZVZfQ2xQeDVKVU1FZDRmd0h6MWNTc3VTekRveEVaanZnZXM1d0tleXNGT3lTRmFHMXNHZmdpOThBekF3eUtWZHUtSHFIX2FLcWh2c0RsUW5QUGtWbVRlQ1FRaGFNbFZ6UzJnY0dlMDZMcWNJQUZMbGZYdXd4QmFMUkUxU3lYako0M0JSLXdTVVA3NzQzVE45ZmVvbHhFRFNrRzJqRW5ud0pHZTVTdmRIcWQwdDc2VXZ0LS1MZVRvODU1bjlFTjZuU09SWHg1MURnQXRrOHRac25nR1lXcVVfT0tJSFJYUVY2VTM2eU5wQXRCVXBVTk1IWVh6T1dOTVRKTlE3elJYaEx3MFFQQTVRWWd0aDRqODBfSEpTSnktZF9TN3Etbld5djR2UEdyMmtjWWNpeXRtMFBKX2Nlbl8xZjlYcWpfR0JRRnZfaERlUllZWWMzREdXWTNORjBJ?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 23 Nov 2026 01:14:05 GMT
- [【即時新聞】今日法人看好奇鋐液冷散熱出貨放量，第三季毛利率衝33.9%創新高！ - CMoney投資網誌](https://news.google.com/rss/articles/CBMikAFBVV95cUxPTjBpR19sU1BvM2RpUTJQN1NPS250eldvZ3VDVUpsdjdmT1FScmtqa2xpaXJqYk5BR2dvd3BMWUlFbWQtS1RwTDIwdzUxS01Ua2pWOEVES1JIWDhCNmJWTXNNN2s0V1RERmVXWXo0b2V3SHAzRW9JWTV5ODRBeHNhcElyUkZCV21NaENlMjNPb1U?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 23 Nov 2026 22:08:15 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Intel Q2 2026: Revenue Up 25%, Data Center +59%, Stock Surges Then Retreats to $100 - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.24 | -47.98% | +47.09% | 59.66 | 114.68 | -47.98% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 方向判斷命中詞：surges。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Q2 2026: Revenue Up 25%, Data Center +59%, Stock Surges Then Retreats to $100 - TradingKey](https://news.google.com/rss/articles/CBMiyAFBVV95cUxPSTRQZEVBYzJNekhNS2NEYThtTnBoNEJCcWRZTS1SSFVXYnVfNjdpNndfd2xrWklfM2JvakdWTUdQNjdWaVFDaHl3bEo5WnpwUWZZQWlwdUpfUTZqbUR4R1hHdDhhLVowZU5IYnllc3ZkVTBHcDhGbzg0SERudlh6TVlNc3JPb2FjdkNjNFo1SmkzMFZHcmk0d1A5OERwMlFFeVhrQ1RuSVJVMmd1U3E1Z0toZWN6RWE2c1NkeU9ZejM5cGhJV0pxSg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 22 Nov 2026 14:18:46 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：SanDisk and Micron’s Early-2027 Worst Cases: A NAND Inflection After a Split vs. Peak-Cycle Fear Amid Heavy CapEx - 24/7 Wall St.；Citi Says Memory-Stock Rout Is Overdone, Sees Micron Doubling and SanDisk Tripling - BigGo Finance；SanDisk Surges 22% as Jensen Huang's Return to NVIDIA Sparks AI Chip Rebound; Seagate Jumps 18%, Micron Rallies 16% - 24/7 Wall St.

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.33 | -27.12% | N/A | 707.70 | 971.00 | -27.12% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.33 | -6.67% | -19.45% | 94.39 | 291.88 | -67.66% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.24 | -27.73% | -17.78% | 165.05 | 228.38 | -27.73% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron」，共 3 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：surges。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：surges。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：HBM。 方向判斷命中詞：surges。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [SanDisk and Micron’s Early-2027 Worst Cases: A NAND Inflection After a Split vs. Peak-Cycle Fear Amid Heavy CapEx - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi6gFBVV95cUxQWHhZOVVuRFlrM0V1bUJkY194VXpteG9uR2ZtVk95bVNhbHRTSTkxNDhnZTJaU2FMNVRhYW1DNnV0VWNCWGp1ZjZRaFFoQ3k3ZmJYMHUyQ2xwN0ZWamFsUnRyUS1lWUY2Qk96OUhUX3Y4cXRmTVZEM1NnSW44aXhXOGlWRThOV2hhYno3dTFreXhGWE0zcjFkbmh3aXVwNHpqRnVIeTk3LTNYT0pqUm9PY3ZWOXJVZEp0V214bHpxY3djWXFhU3c0TVZrcE9BV0NZOEdjZWwzbVNJTHZvNktsQno1Rk5FZlNrekE?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 23 Nov 2026 13:45:00 GMT
- [Citi Says Memory-Stock Rout Is Overdone, Sees Micron Doubling and SanDisk Tripling - BigGo Finance](https://news.google.com/rss/articles/CBMidkFVX3lxTE8yazg4UElia25TOFNPRURwTWxyYmNRU0RwMlQwVVZhWjJYWUxJczFJc090MG9qYXY3czZsdlN4SURqRnllQnVkd1d6TFF4WVY5ZlBlNW1kMVBqMl9ENVMzcWlxbW1UcHRieXlzaVN0MnItdXVQRFE?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 23 Nov 2026 10:35:00 GMT
- [SanDisk Surges 22% as Jensen Huang's Return to NVIDIA Sparks AI Chip Rebound; Seagate Jumps 18%, Micron Rallies 16% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi6AFBVV95cUxNUEJsWmVwcjVqZEVVSDlZVi15SjI2SHFHSE9ublVINEpBWGlNRlBET3FWUFE5bGxvbEhKWHMzMjlBTnpobEVtMXhId1Z1cnVuRVpNcnlsS0E3TlZmREs5aXhXMV9hdlg0OHRHMDhUeHA2UFNKLUZwc1o5SDk5NWFVekZLUUZoazZwWHFabG9iZHQ2OW14dzh3TjVtT2tSS2xqQlVqd1VNcFRja3RTS3pMTERYT3F3cVJPUXFOTno4c3d5NjJVZmladk8tQW05aVFQeFVQem1PcWlrNEM2T1JTNFBzaXJicmpH?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 23 Nov 2026 15:04:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
