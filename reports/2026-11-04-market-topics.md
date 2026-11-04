# 每日股市熱門話題分析 - 2026-11-04

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **綜合市場情緒**｜負向｜熱度 39｜市場確認 84.91｜同向 1/1
2. **散熱與液冷供應鏈**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
3. **新興題材：TradingKey**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
4. **AI 伺服器與資料中心**｜正向｜熱度 16｜市場確認 0.00｜同向 1/8
5. **半導體與晶片供應鏈**｜正向｜熱度 5｜市場確認 0.00｜同向 1/8

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.21（樣本 19）
- 5日相關係數：0.35（樣本 15）
- 同向比例：3/19

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 綜合市場情緒 | 84.91 | 1/1 | 0 | +4.97% | +4.37% |
| 散熱與液冷供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：TradingKey | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 0.00 | 1/8 | 7 | -9.79% | +4.21% |
| 半導體與晶片供應鏈 | 0.00 | 1/8 | 7 | -13.08% | +6.16% |
| 記憶體與 HBM 供應鏈 | 0.00 | 0/2 | 2 | -17.70% | -14.38% |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：CrowdStrike | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價呈負相關；應檢查正負向詞庫，並降低新聞直接提及但股價背離的權重。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-10-22 | 0.02 | -0.21 | +38.89% | 18 |
| 2026-10-23 | 0.35 | 0.29 | +78.95% | 19 |
| 2026-10-24 | 0.09 | -0.31 | +70.00% | 20 |
| 2026-10-25 | 0.41 | 0.78 | +64.29% | 14 |
| 2026-10-26 | 0.27 | -0.25 | +36.36% | 11 |
| 2026-10-27 | 0.07 | 0.31 | +50.00% | 18 |
| 2026-10-28 | -0.30 | 0.47 | +20.00% | 15 |
| 2026-10-29 | -0.05 | 0.04 | +42.86% | 14 |
| 2026-10-30 | -0.00 | -0.05 | +47.62% | 21 |
| 2026-10-31 | 0.50 | -0.68 | +80.00% | 15 |
| 2026-11-01 | 0.47 | -0.40 | +85.71% | 14 |
| 2026-11-02 | -0.15 | -0.06 | +27.78% | 18 |
| 2026-11-03 | -0.03 | 0.08 | +40.91% | 22 |
| 2026-11-04 | -0.21 | 0.35 | +15.79% | 19 |

## 歷史回測摘要

- 回測日期：2026-11-04
- 近5日 3日相關：-0.38
- 近5日 5日相關：-0.07
- 同向比例：+47.83%
- 權重狀態：已調整

- 方向準確度：+47.83%
- 信心排序準確度：-0.38
- 診斷：方向與信心皆需修正

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

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：個股動態報導內容-D6F11A4B-73C5-417C-91FD-BAABEEF4BEB6 - MoneyDJ理財網；台股暴跌連連破底！現在是接刀還是撿鑽石？分析師說三個字... - 經濟日報；台積電上漲25元　台股早盤揚升逾400點 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | -0.42 | -4.97% | -4.37% | 2,300.00 | 2,480.00 | -7.26% | 同向 | 86.28 | 26.60 | 511.86B TWD / 54.65% | 2026-10-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。

### 主要來源

- [個股動態報導內容-D6F11A4B-73C5-417C-91FD-BAABEEF4BEB6 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilAFBVV95cUxQLWNhT2NFTVljVV9BVGZleHY0c0hJT1o5cTdYancyeTYxMHpxME5qZHRGcGMwcWFsWXhuSHdtMnpVVkw0a3hVRmc0U3RoTzBlM2RoYzNUZWFrSnZ3MU5MWXVxTWc0Nk5Ybm1ILWdWVmxBa0xOMFhoMjlQZTJoVmdZdGQ3ZHlCU3NUbGxqZDNYWDF5OVVa?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 03 Nov 2026 15:41:10 GMT
- [台股暴跌連連破底！現在是接刀還是撿鑽石？分析師說三個字... - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5TZHhUcmtDTHFiM2FINTV3ZzhCZ2NQN3BXT0U1eUJLWHZra252dHh4RWZsNDFzNDVCRW9nUTV4NElyZngybHlVLUxPRTJRdjRlazFpZUU4X0VmQdIBX0FVX3lxTE5UMm9hTnB5eFQ1cV9lUVZkQUNtUTRuS0ZJSGtTMWNYQUVoc01aU0VhWWd1bXoyRWc1MUNud0RRZVdSVzhKUjBzeUFnT3hpdVJLMnpDYVE3cmpsZ3g3aG9r?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 03 Nov 2026 08:00:00 GMT
- [台積電上漲25元　台股早盤揚升逾400點 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9BZ1dQMTFXX3BuMEZwTm5Scm90aGoxRDVkOWhnN0dFWFJKZVRPVFo5eThrRGVQSzVJSDhUMlJKdllTbmUtcUVMaUFPNnNPVU8teS1rNWticGNYd9IBX0FVX3lxTE5vSHpfYUZ3dk5kX1VTVTlaOTk4UnhzUENtQnEyQ3l0STRkWFgtR0k2ZHIweFhrOWhneGkzcnA5OGdBcXIyd1hMNlF2ekF2dVFVbXdxTmtta2NhSWVPYWpz?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 04 Nov 2026 01:22:13 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：目標價直奔4005大關！「這散熱大廠」吃爆AI四大平台　明年EPS估衝160元 - 三立新聞；散熱股又有大消息？花旗喊買奇鋐、雙鴻 目標價齊升逾14% - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | -5.48% | -6.23% | 2,910.00 | 3,435.00 | -15.28% | 不適用 | 75.13 | 39.12 | 21.02B TWD / 44.92% | 2026-10-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱、奇鋐」，共 2 篇新聞命中。 同時符合主題標籤：thermal。

### 主要來源

- [目標價直奔4005大關！「這散熱大廠」吃爆AI四大平台　明年EPS估衝160元 - 三立新聞](https://news.google.com/rss/articles/CBMiSEFVX3lxTE1YNGltVnpUeUVGeXZfMHhqYTZvamNrQV9XZUI1OEtTTjYtNWxuLXZIZG1iNTRXVGhPZGt2bFVjdXVxZmNMLW1FcdIBTEFVX3lxTE9QNm02TXVKNXAzRTBpWjBydnNSTzM1RG84T2I1R0I2SGhoS09VNzdrbGdQNllBR0l5LXdtWERBeHlLNV9sQmJwOWdhNzI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 02 Nov 2026 05:31:38 GMT
- [散熱股又有大消息？花旗喊買奇鋐、雙鴻 目標價齊升逾14% - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE04UXU3RGRUUnBBVElIbVBGZWozMUxfTzNsbE50ejYzRE1pUTJBQ0FNWS03VjRSYlZrUWkzSXhuNHhFQl9teWs5YTJ4QUU4ck1MZ0NneEk3XzF3UdIBX0FVX3lxTE5tclh3dXNNWDhDMnNiYmMyRW1DRFJwZUt6ZlZXMmdEYlhoQU9VR1pSeTVrVUpVT2FWOE1idEkxdXRhYTYyYVpMcnRwaWQ4NGpmRUNTREJUQ2UwNU01N0pF?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 02 Nov 2026 08:00:00 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：AMD Q3 Earnings Preview: Can AI Chip Growth Reverse an 11% Decline? Wall Street's Highest Target Price at $1,250 - TradingKey；Kioxia Drops Over 15% to Six-Month Low Without Dragging Down US Memory Stocks: Micron, SanDisk Up Over 2% Pre-Market, SK Hynix Gains Nearly 5% - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AMD 超微 | 新聞直接提及 | 0.00 | -6.24% | N/A | 483.90 | 516.10 | -6.24% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 新聞直接提及 | 0.00 | -11.94% | N/A | 855.10 | 971.00 | -11.94% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | -23.47% | -14.38% | 1,075.08 | 2,335.00 | -53.96% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 方向判斷命中詞：decline, growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MU：新聞直接提及「Micron」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。

### 主要來源

- [AMD Q3 Earnings Preview: Can AI Chip Growth Reverse an 11% Decline? Wall Street's Highest Target Price at $1,250 - TradingKey](https://news.google.com/rss/articles/CBMivAFBVV95cUxOWlM2dGN1RU5oXzJfRlJ0VlJmMDFxWW01cmRXWkUwZU1PRncydV9HQ0MzUDhBOGNna0RnSFVjaEFTSmxINTNMZlhLRlBJS1daNllBVENKUkVVNmRSQlFqTFFnNUNPSFZabDk1emMwbkJscm03eTFlZlh1SHNkdDBTS0R4c19jM3hSNVVEUzZWOVpnejNQbGVtblFyMTJtYkllcjlQRV9pMURCQkN1QzNJZmMtNVhEOTlyRGVSSA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 02 Nov 2026 08:50:53 GMT
- [Kioxia Drops Over 15% to Six-Month Low Without Dragging Down US Memory Stocks: Micron, SanDisk Up Over 2% Pre-Market, SK Hynix Gains Nearly 5% - TradingKey](https://news.google.com/rss/articles/CBMi9gFBVV95cUxOR0hKX2llQ1NhcFNlbzhnTEwySGwxSEs3azIxMW9DOFBTMGp1MWdXQzg0VmtTT3gyS2pWR0s4TjdPWjhyZXgxNXQyVVNwdEIwbk9DdHNjNllvaTJiYWNBdlhEOTVvWkl6Zk9FTG0wbVlITHZFZV9pSjdpYmFSZi1PcDBBbkpkdUM4YWhWd2RXVWt1XzJOc1hFOW8zZFZqOS1oOGk1LWNidGEyRkxnNnpoeEVOOUI4c3VXaXcxY0xyeHVVMkYweGFxRHBtV19oaDlVcjMzYWdubENHN3NndUF2YmU4aUV2a3R2Y0dURHY4SGV0YzZRUlE?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 02 Nov 2026 09:40:53 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Chip and AI stocks give up some gains ahead of AMD earnings (AMD:NASDAQ) - Seeking Alpha；Ed Yardeni Sees AI Chip Rebound, Year-End Stock Rally — Warns Of Midterm Election, Iran War Risks - TradingView；網銀密碼交給 AI 幫管帳，Meta 前資安長嚴厲警告：簡直瘋了 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AMD 超微 | 新聞直接提及 | +0.27 | -6.24% | N/A | 483.90 | 516.10 | -6.24% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 產業/供應鏈推估 | +0.04 | -47.20% | +49.29% | 60.55 | 114.68 | -47.20% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.03 | -6.38% | +3.30% | 206.69 | 228.38 | -9.50% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.03 | -4.97% | -4.37% | 2,300.00 | 2,480.00 | -7.26% | 背離 | 86.28 | 26.60 | 511.86B TWD / 54.65% | 2026-10-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | +15.71% | +5.89% | 520.99 | 521.91 | -0.18% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -10.32% | -12.08% | 332.13 | 446.77 | -25.66% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.02 | -9.81% | -5.38% | 627.00 | 703.00 | -10.81% | 背離 | 13.92 | 44.57 | 88.13B TWD / 45.52% | 2026-10-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.02 | -9.15% | -7.20% | 3,720.00 | 4,920.00 | -24.39% | 背離 | 60.69 | 60.69 | 55.40B TWD / 1.97% | 2026-10-01 |

關聯理由（前 3）：
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Chip and AI stocks give up some gains ahead of AMD earnings (AMD:NASDAQ) - Seeking Alpha](https://news.google.com/rss/articles/CBMingFBVV95cUxOd2tWdkUzZldKRGVYT0FjMlRDZnJ6b2F6cWlQbTVxRWRjQjlMTDZFVERkYldQMnhqNmRwazN4X0pQQi1EYnlqbWNVTTRSOUNFUWtmUlVRa1FfcXdxdzh2TjlIdVlqUFl6WXlKNFFCVzFLRjBMWWRyaWVjOXQySTJsXy05RUZFcWU0NTZJTTRLeHlIdDh6QU5VRmdxclJQUQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 02 Nov 2026 18:41:59 GMT
- [Ed Yardeni Sees AI Chip Rebound, Year-End Stock Rally — Warns Of Midterm Election, Iran War Risks - TradingView](https://news.google.com/rss/articles/CBMi6AFBVV95cUxNQ180YVUtbkU0SWtCX3hyOHFxdHBTWjBfZHFyZnVzLVktYVpZS2lmd1BaU21qZ05Md1BEclRiLU1CbEc1QVo1a0VIUUNWZEVfWlZJTDd6T2F0bmlxUkxmVVQxVDdLQTVwalVCM3ZiaFZOMmpWWEItX1ZoUkw2cFNyakg4dHdFTjZIN3J4UUhkT1oyNzhzTDRucnNDSllkZmZSTThyVUZ1M04zNGNxVFVSWnpqTHA5NWRKSUpjYlhuSm1lRFVKb0ZiblFoOUk1bk5Fb2FYcU5uOWx5RXpheldLY1JZRWNZWW1k?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 02 Nov 2026 11:08:29 GMT
- [網銀密碼交給 AI 幫管帳，Meta 前資安長嚴厲警告：簡直瘋了 - TechNews 科技新報](https://news.google.com/rss/articles/CBMigAFBVV95cUxNMXdxWmtKU0NyNGlUd0xIczFRTk9oZUwzU2pfTHlqcDRENk5SMDZrNnJVaGJrUXFHTU8wWGh3dTB0ejN5VzhTN3ZPM180ZVJIRmxvX0Z1RnFLbW51c1ppVnl4ak82M0cxcUxleGZCaHZtSmhsTC1ZUGZmVUw2N2c0dQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 04 Nov 2026 00:11:26 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：AMD Advances 5%, Intel Rises 4%, Marvell Gains 2% as Chip Stocks Bounce Ahead of AMD Earnings - 24/7 Wall St.；AMD to report Q3 results as chip stocks rebound following last week's steep selloff - Yahoo Finance；Chip and AI stocks give up some gains ahead of AMD earnings (AMD:NASDAQ) - Seeking Alpha

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AMD 超微 | 新聞直接提及 | +0.28 | -6.24% | N/A | 483.90 | 516.10 | -6.24% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.27 | -47.20% | +49.29% | 60.55 | 114.68 | -47.20% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 新聞直接提及 | +0.42 | +6.36% | +19.02% | 331.90 | 344.63 | -3.69% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.03 | -4.97% | -4.37% | 2,300.00 | 2,480.00 | -7.26% | 背離 | 86.28 | 26.60 | 511.86B TWD / 54.65% | 2026-10-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.03 | -10.82% | -15.92% | 104.50 | 164.50 | -36.47% | 背離 | 6.80 | 15.21 | 25.35B TWD / 27.22% | 2026-10-01 |
| NVDA 輝達 | 產業/供應鏈推估 | +0.02 | -6.38% | +3.30% | 206.69 | 228.38 | -9.50% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | +0.02 | -11.94% | N/A | 855.10 | 971.00 | -11.94% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.02 | -23.47% | -14.38% | 1,075.08 | 2,335.00 | -53.96% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- AMD：新聞直接提及「AMD」，共 3 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AAPL：新聞直接提及「蘋果」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AMD Advances 5%, Intel Rises 4%, Marvell Gains 2% as Chip Stocks Bounce Ahead of AMD Earnings - 24/7 Wall St.](https://news.google.com/rss/articles/CBMizAFBVV95cUxNZGt2UGdvbUNTNWlLYnZUTDM0NEI2X01iZVNTbXg4Yk5ib3NSN2VNTFEtR0JDMkVFNlgteFkzRU5Rc21VSlo4VnFkRU1FQnlYeU16Z2FIeUY4a1ZuN1o2cS1LaHlGR0ZNR3VwYnBKTUNuZjd0ZFNYLTZFN3pWajdzRDByN2MzV3pyYzRhVEdyLWlLWVJMUFNUeU91ZWxkS2ZZYzRlN0p0MXhQUjNsazR1cGdQWG1UZW1rRTZ2TEJ2MzRIT0R4SVZxeU9tTmw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 03 Nov 2026 14:44:00 GMT
- [AMD to report Q3 results as chip stocks rebound following last week's steep selloff - Yahoo Finance](https://news.google.com/rss/articles/CBMi2gFBVV95cUxQczVqLW1wb1JxQkVGUFRiUnlZMGZncjVUWkNtR2hOb1JKTkF0eVRMLWduLVZYVWNId0VfY0JVWHFVQkpDRzZGTGM5d21DcnhXRmlueXA3amMxb1Bobzkxb0ZDdkkwYVBQem1LcHN0MVJLbWNiWWowQWJYYlRtOTEwcDJzR201MlhwU1F1V0VCbVl5VE9fTGllRml2anhLa1cwQzlHMjM2TmtaR3ZEVHVkN285NWFYRjZWYmRqcHVER2tSMllCTXRCXzVuam9HUG9YcTluZ2g2SVk5UQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 03 Nov 2026 15:03:56 GMT
- [Chip and AI stocks give up some gains ahead of AMD earnings (AMD:NASDAQ) - Seeking Alpha](https://news.google.com/rss/articles/CBMingFBVV95cUxOd2tWdkUzZldKRGVYT0FjMlRDZnJ6b2F6cWlQbTVxRWRjQjlMTDZFVERkYldQMnhqNmRwazN4X0pQQi1EYnlqbWNVTTRSOUNFUWtmUlVRa1FfcXdxdzh2TjlIdVlqUFl6WXlKNFFCVzFLRjBMWWRyaWVjOXQySTJsXy05RUZFcWU0NTZJTTRLeHlIdDh6QU5VRmdxclJQUQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 02 Nov 2026 18:41:59 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Micron Falls 4% as Kioxia's Cautious Outlook Hits Memory Stocks; Western Digital Drops 5%, SanDisk Slides 3% - 24/7 Wall St.；Micron vs. SanDisk: China's DRAM Scare Hit Both Stocks, but 1 Is the Better Buy - Barchart.com；US Pre-Market: Memory Chip Stocks Rally Broadly, SanDisk and Micron Each Up More Than 3% - BigGo Finance

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| SNDK SanDisk | 新聞直接提及 | +0.28 | -23.47% | -14.38% | 1,075.08 | 2,335.00 | -53.96% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 新聞直接提及 | +0.28 | -11.94% | N/A | 855.10 | 971.00 | -11.94% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -6.38% | +3.30% | 206.69 | 228.38 | -9.50% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- SNDK：新聞直接提及「SanDisk、SNDK」，共 6 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：falls, rally, surges, upgrade。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- MU：新聞直接提及「Micron」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：falls, rally, surges。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Micron Falls 4% as Kioxia's Cautious Outlook Hits Memory Stocks; Western Digital Drops 5%, SanDisk Slides 3% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi3wFBVV95cUxQd24xZ3lROHBoV1M2WWN3VmlMUjNjZ1ZfZnNNNGFmWnhZZ2d5Qnl4TjZMd3FPSm44N0VIRFhVM2s2RkNpVmdvMWJYeUZnRWR5YWhIdmtKdUpiQndZV19vaFlFRU1hZ1FfTk9GRzJ4M3lXLVJHclZ0cmpzYW9CbkJvb1BYNGNDYmpJTkJhWkRmMklmN3EtM2ZYc2V2bzEzdGZCVTJtZmVvVVk1SjhTQUQtNzZ2MDlQaXQ3T3NSaVBjQ0FCRm53Mkc3UEtzOGNWaUc2XzhVb0NNS3Ryc1JsZkVN?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 02 Nov 2026 18:53:00 GMT
- [Micron vs. SanDisk: China's DRAM Scare Hit Both Stocks, but 1 Is the Better Buy - Barchart.com](https://news.google.com/rss/articles/CBMivAFBVV95cUxOdEFZQXlVNFZTZjFXRTBSdEFXZ0FWeGdHczdqVFV5dXNYNXppOUlhR0t6T3ZRX1lVcU1PQjVveFhYVFdLOEtIc0NSdXp4MWVuZkROaF9pbEpGNVJjZ25XUkVSYmtERlY4MUJyT1d6Q3c4U2NiSTRNYnBma1Y0WUdYN252eFAxTkFUNXh0QnE5UWplNDFzeHI0X1NlZFpmWVZxb2lfa1FRNy10cE56ZjhWTnMyQzVSVmY5bWtDaw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 02 Nov 2026 12:30:03 GMT
- [US Pre-Market: Memory Chip Stocks Rally Broadly, SanDisk and Micron Each Up More Than 3% - BigGo Finance](https://news.google.com/rss/articles/CBMidkFVX3lxTFBKU0ZYTXNYWDFJNmZaOWlhREVZRHVwdE1fM2UtVl9tWjNrWWhwVDdjRFVMczRZWkg2VWVKVTdaMjlwZjRqZm55eVh0VEZHaDhjYVhraXlXdFRnbGNKaU9jSW1UWVU0b0l1ODhlVlNUNXUyVVduZlE?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 03 Nov 2026 12:06:00 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：統一證券：台股整體技術面弱勢整理- 新聞 - MoneyDJ；國票證券：台股超跌反彈條件可望逐漸醞釀- 新聞 - MoneyDJ；20261103台股融資維持率 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [統一證券：台股整體技術面弱勢整理- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMilgFBVV95cUxQNGJZMnpncE1zVEhBdG5PMGM2b0F4czhzZFBnUlR4WS1nQmpQVFozcy1pb2Z4TDNBOWU5bEpOVU55OGVlWUd4T2tHemZXeUtWcGU1dFFYaDR0TlRLYXcycC1TNElvcTg5X2ZYWkF3NU8tY1ZTWnluQ1lvb1dOak5CQ1FpVV9vRUZvVXpNdlgtRnRtOHVCWmc?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 04 Nov 2026 01:00:00 GMT
- [國票證券：台股超跌反彈條件可望逐漸醞釀- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxOS1MyeE54RmtYUV9BbmJLOVVZVFBZZUFKeDhjLXo1SVZfRlZBZjRqQlh3dTJZU01icXk3RHNtZlZaY21lUkNJVnFCTGRtTldrd3FQNnBfVm5qaGo4RVQ3R1FQYktwLVRRV3UwQzBOT3hGSU1LekRzajhmeG5lU0k2QWloVXN3VzFQd2IyOVd1UmtOZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 04 Nov 2026 01:00:00 GMT
- [20261103台股融資維持率 - MoneyDJ](https://news.google.com/rss/articles/CBMisgFBVV95cUxPTGctVzkweldaYm1lU0VtQU5ONkU4MDl1WVN5aG1aOUdqREdQbHZCSDE0cFF2MXFnekcxV1FDWjZrUFlKbEF0OElIRnNGSl9xc0pvV25NR0hGbFVMZVRONjBjNVAtdEJOX3RZMnEyS1FWV3JVYk9mbHJlVmI4SlJrQkZETkZVcGZsNGQxT04taXNTM1NmUjJRdTJBbmVFemo5eWlSQkpzMnpydG9CVG1hVkJn0gG3AUFVX3lxTE5MNXZGbkhpWG1Hc0tCb3pkNWNrNWhRMTNTSWxleU1XbkY4VkhLc2VPXzNkc1ZVZVZTUjAyTEZIaGJYWjQxb2VSMjBCY2QtR1o5YzVWdWI5bEdEZkZ1bEZCeDRwZDN5WjlEVVZSdFZ2bjFxTnJqRjY1Nk5hdEVMbURrNU4yQkZBMnFTV1pEZzBoR3ZDbmVvdzI4OXU5OFduNno1SW5seXplaXlJMnFTdXdDZzhyRXFuQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 03 Nov 2026 15:31:01 GMT

## 新興題材：CrowdStrike

摘要：新興題材：CrowdStrike 相關新聞集中在：CrowdStrike's new kill switch can stop rogue AI agents in their tracks, CEO says - CNBC；CrowdStrike launches AI kill switch that it says can stop internal agents that go rogue - CNBC

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [CrowdStrike's new kill switch can stop rogue AI agents in their tracks, CEO says - CNBC](https://news.google.com/rss/articles/CBMitgFBVV95cUxPTGk5Z3RYZDNLZmJIN2FraWVkTm9paXBOd0w0c0lTQ2p1Z2lXZjhzR0VnTjJCVk5UU1pGRG5sTElvY3hhYW5Ta19pN1dHNzcwZW9PSDFoLXlBcTBQVFlSbFZYQWxPaXE1WHFVOFZUTHZ0ZTlWLTBpNjE3cnRPWllZYlVDUjRmaVY0QXgzODRxLW1nSmw3VXBLV0EyZENMeDVkU24tR2VwTmZoYmJnOFI3QVp6am9md9IBuwFBVV95cUxNTmsxR1FYWlNubkpfbXhSNmZDcmlhWjBWb3ZETDRnOVd2VWp4bU11Rmg0Rnc4b2hnLUF5WEJtWE0tT0EwdGswZE54ODhRWl9EYWYzLW93S2ZhVDFOTWRXSFg5WWN4TS1IdGJ3YnNMb2JEdDU2cnlkb2JPVl9HcnNJdUNkLU9BaXdFWkxDMkRYNXBqSnBQNGlDd1gwQW5uZzhvLWJsTnZaR3otbEZSVUxjamNUdlhKN0poblR3?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 03 Nov 2026 23:37:07 GMT
- [CrowdStrike launches AI kill switch that it says can stop internal agents that go rogue - CNBC](https://news.google.com/rss/articles/CBMiggFBVV95cUxQY2hvQXJrTkR2WVQzQ3lkTUNrczVfcXc2VEVSbW5tQ2hhb0pQSk5MZ0xsNjBCcW5FdlJxeTZSeF80MUw3b2hhcWk3NG5LR0RxX0pkY1ZDUWdFaWdSekJnX0Npemh1ME1TbEl3WVBtUlNmVjNyNFlpWFhHcXlvWC05U3NR0gGHAUFVX3lxTE1kb2tRX0VwdjZndEhueklPNmxSOEFMdzI4d21MajNrVlh3QW02c0hGaWxiWWRnREQ3cl9fMnU4WXVpYXZkVEk2QmlQR2RldHlQUXNtVHdMdEUtUndhUjBEYTBjNkZELTVXclUtMWpIZGhfYTJnU0FpN3JObC1Wb0s0RG45UXM5SQ?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 03 Nov 2026 19:35:24 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
