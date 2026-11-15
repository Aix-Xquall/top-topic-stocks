# 每日股市熱門話題分析 - 2026-11-15

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **新興題材：MoneyDJ**｜中性｜熱度 11｜市場確認 100.00｜同向 1/1
2. **關稅與供應鏈轉移**｜負向｜熱度 2｜市場確認 100.00｜同向 1/1
3. **散熱與液冷供應鏈**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0
4. **AI 伺服器與資料中心**｜正向｜熱度 18｜市場確認 16.71｜同向 4/8
5. **半導體與晶片供應鏈**｜正向｜熱度 6｜市場確認 0.00｜同向 3/8

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.02（樣本 20）
- 5日相關係數：0.62（樣本 16）
- 同向比例：10/20

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 新興題材：MoneyDJ | 100.00 | 1/1 | 0 | +28.69% | +18.88% |
| 關稅與供應鏈轉移 | 100.00 | 1/1 | 0 | +28.69% | +18.88% |
| 散熱與液冷供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 16.71 | 4/8 | 4 | -6.10% | +9.84% |
| 半導體與晶片供應鏈 | 0.00 | 3/8 | 4 | -10.93% | +7.29% |
| 記憶體與 HBM 供應鏈 | 9.61 | 1/2 | 1 | -8.46% | +5.98% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：AI三雄營收 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 相關性偏弱；應提高同向價格確認權重，降低泛 AI、泛半導體等寬標籤推估權重。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-11-01 | 0.47 | -0.40 | +85.71% | 14 |
| 2026-11-02 | -0.15 | -0.06 | +27.78% | 18 |
| 2026-11-03 | -0.03 | 0.08 | +40.91% | 22 |
| 2026-11-04 | -0.21 | 0.35 | +15.79% | 19 |
| 2026-11-05 | 0.13 | -0.53 | +66.67% | 12 |
| 2026-11-06 | -0.18 | 0.77 | +100.00% | 5 |
| 2026-11-08 | -0.21 | 0.03 | +23.08% | 13 |
| 2026-11-09 | -0.56 | -0.62 | +60.00% | 10 |
| 2026-11-10 | -0.32 | 0.24 | +3.45% | 29 |
| 2026-11-11 | 0.34 | -0.26 | +46.67% | 15 |
| 2026-11-12 | -0.09 | 0.07 | +50.00% | 14 |
| 2026-11-13 | -0.56 | 0.42 | +54.17% | 24 |
| 2026-11-14 | -0.34 | 0.12 | +42.11% | 19 |
| 2026-11-15 | -0.02 | 0.62 | +50.00% | 20 |

## 歷史回測摘要

- 回測日期：2026-11-15
- 近5日 3日相關：N/A
- 近5日 5日相關：N/A
- 同向比例：+50.00%
- 權重狀態：未調整

- 方向準確度：+50.00%
- 信心排序準確度：N/A
- 診斷：樣本不足

調整原因：近 5 日有效樣本 4 筆，低於 15 筆門檻，暫不調整權重。

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

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：最新專欄分析 - MoneyDJ；《台股盤後》收漲583點、44K得而復失；週K翻紅- 新聞 - MoneyDJ；台股震盪、企業獲利卻創高！AI三雄營收飆破紀錄 00961掌握科技金融雙引擎 - 市場短波 - 新聞 - MoneyDJ

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | -0.42 | -28.69% | -18.88% | 162.85 | 228.38 | -28.69% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：衝擊。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [最新專欄分析 - MoneyDJ](https://news.google.com/rss/articles/CBMicEFVX3lxTE1VRTMzejJyYnBUSW1LRGhEY1NtRzQwSWdZdjd3blpXdlJ2NDV4bmJRMjY3WFlRcHJRTWpjcFo4YXFLVG54bEgwdzZ3aW0wRGNmRlllX2tBZFlKd295Q19LeHZVZ01hdlo0M09OQk54d1o?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 14 Nov 2026 16:06:20 GMT
- [《台股盤後》收漲583點、44K得而復失；週K翻紅- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPZDVLNnRPbnJoTEhWU0x2cEVkQ0JPT0JaeTlQV2ltWmo0UjRBVlo2Z0NZLVZHZGlxbWxmWXVUa281NHZyMnN4RTdFbkhEU0dQdFRSSVlmY0puVHc5STh1U1BwMzBnRHItQ0RqY1k4X2FGT3hQbENWdlFYYkM0SU5HaGlmLS1wLVlEeFNDNDY4dzFsUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 13 Nov 2026 08:05:00 GMT
- [台股震盪、企業獲利卻創高！AI三雄營收飆破紀錄 00961掌握科技金融雙引擎 - 市場短波 - 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMihwFBVV95cUxQUmNvMHg5b080SU1SYTItaGxCa2I0c0w3QmxQWmNfQm52R2ZrR3BmcVZINkZBekVLc3ZvTGJMc1FMUm1PWDRSY1FnbGFmUnhwM1FPTnp6dFUyNWZQVnVTd0hjQmI0Zjd4dmtDLTYtb01iTE0yVWJwOVhtOUtrc1N6Sm5XenZzb3M?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 13 Nov 2026 02:53:00 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：黃仁勳閃辭衝擊台廠佈局　8大供應鏈影響一次看 - ETtoday財經雲；黃仁勳風波台股一度逆勢漲近1400點！亞洲供應鏈緊盯輝達17日財報 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | -0.42 | -28.69% | -18.88% | 162.85 | 228.38 | -28.69% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +14.17% | +27.76% | 356.27 | 356.27 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | -0.21% | +7.35% | 241.00 | 289.00 | -16.61% | 不適用 | 16.57 | 15.89 | 1305.32B TWD / 45.73% | 2026-11-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [黃仁勳閃辭衝擊台廠佈局　8大供應鏈影響一次看 - ETtoday財經雲](https://news.google.com/rss/articles/CBMiUkFVX3lxTFBjRFU3NW04VWo4ZDNzTFJHa05nc3NHS2R2WF9TWEl2UkctSXU3V2lKRFQzTjVyUi11UTRkZFR6OWtCLXduZjd4TDhES3dGandvd2fSAVBBVV95cUxPSkRHV29KWWhRSjZvTlAzeEliQmhwNjVpWVlnd0MwOFp5M0RrYUtzMkdsZk0tSXJrZ3pwLWZ3TkdELW1QM09IOVZyYjBET0NnSw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 13 Nov 2026 06:19:00 GMT
- [黃仁勳風波台股一度逆勢漲近1400點！亞洲供應鏈緊盯輝達17日財報 - 中央社 CNA](https://news.google.com/rss/articles/CBMiU0FVX3lxTFBoa3JzU3A2QlVHWENNdWtGYVZMMDI1cTl1Z25QR3A2NG5iVV8wYzZYQTlnMzBfSjdSRFcxb1JCRGM5N3lzNmp4MElPdGpGZ000RU9r?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 13 Nov 2026 09:25:00 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：散熱股又有大消息？花旗喊買奇鋐、雙鴻 目標價齊升逾14% - 經濟日報；台積電法說遇輝達財報AI行情的關鍵48小時 MSCI半年度調整出爐AI伺服器供電散熱誰最強？緯穎台達電奇鋐雙鴻11月17至18日法說見真章中油油價連8凍漲｜投資早知道 - Yahoo股市；股價殺成這樣仍看好！「AI散熱雙雄」連摔 外資目標價竟飆上2,000元 - FTNN

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | +8.96% | +31.60% | 3,040.00 | 3,435.00 | -11.50% | 不適用 | 90.78 | 33.61 | 22.10B TWD / 34.35% | 2026-11-01 |
| NVDA 輝達 | 新聞直接提及 | 0.00 | -28.69% | -18.88% | 162.85 | 228.38 | -28.69% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | 0.00 | +2.84% | +10.07% | 2,350.00 | 2,480.00 | -5.24% | 不適用 | 98.27 | 23.92 | 586.89B TWD / 59.71% | 2026-11-01 |
| 6669 緯穎 | 新聞直接提及 | 0.00 | -2.68% | +5.14% | 1,635.00 | 2,565.00 | -36.26% | 不適用 | 272.05 | 14.42 | 165.13B TWD / 80.94% | 2026-11-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐、散熱」，共 3 篇新聞命中。 同時符合主題標籤：thermal。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。

### 主要來源

- [散熱股又有大消息？花旗喊買奇鋐、雙鴻 目標價齊升逾14% - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE04UXU3RGRUUnBBVElIbVBGZWozMUxfTzNsbE50ejYzRE1pUTJBQ0FNWS03VjRSYlZrUWkzSXhuNHhFQl9teWs5YTJ4QUU4ck1MZ0NneEk3XzF3UdIBX0FVX3lxTE5tclh3dXNNWDhDMnNiYmMyRW1DRFJwZUt6ZlZXMmdEYlhoQU9VR1pSeTVrVUpVT2FWOE1idEkxdXRhYTYyYVpMcnRwaWQ4NGpmRUNTREJUQ2UwNU01N0pF?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 13 Nov 2026 08:00:00 GMT
- [台積電法說遇輝達財報AI行情的關鍵48小時 MSCI半年度調整出爐AI伺服器供電散熱誰最強？緯穎台達電奇鋐雙鴻11月17至18日法說見真章中油油價連8凍漲｜投資早知道 - Yahoo股市](https://news.google.com/rss/articles/CBMigwdBVV95cUxQOXN2QXlmOEJLa2VBcEQ1SGtxRU0yOUNkUDRpQzZCMVRCWTdEVzZpVGNqTDJROFo5eC11Zy0tdGhnUFBvV1llZEwtbi1PQUdXZEdBOGJuTjhreGQxcVhwbjRHb2hOXzlFNVBtNkZVaC1YZmJGUmsxZ0xuUVhNS0JKT0tQaGlVRDlsNm5LdHdpR2lSeGpOWDI2S01hU1VMblBIR2JvX05vcWVucFotd1hBVHNRWlROZUhsTjZPdzdNMTI5M1BpYWFoSlV1dzRKNjZPQUNCY2FnS0VRSGtDYXhINFlmU1BMQ0dINklkckFRc28tVF9xT0xIOHZvUW1hV0NHWHFRX051UmpUQVhaVEp1OUN0Wk1teEpjVndCU19ZS2lDU2F2Qkcwdl80V0lSd1lpS3FHVzVZM1VqdFJzYWd4bjM4T2p0YkNDMW9ZZEJyVkhDQk5CY1dEdGRtRHpSWU1QVFcyTGV0eUhKS0F0dXVRNjUwY3RDOW9sUHJ4ZzNZOVBuVWUxUFotYXNBdmhjUVZicHFZZWJwVXRjOG1fYmpWS0ltN0lSb1VvM0NnNXNaODJFYndiZXFJTHpiRW0yT1NzdnpENTZpSnNON0R1SnhkUEhMcUV1UjNHclhvODVHNHFnSTdwU2pXaTFRQjB0WWxzaWJBblN6TjZZRVA2cGR5QUEwSmFJX3hlY1JyMFFhM2xTc0lpb0ppeHh1ZzE2Ty01SDczeC1YdWdLRmlYR3BuczFfVm5Ob1djMy1aN1gxWXk5UGFBZVVGM1g4bHA5Rzd5WHFQMS1FWFpnTFk1VWc4NkJQS3Bmb3V0X0sxSkVuTHhtTE1xU1U4NUFQX1QwckFFek5jU3B0bzh4ZmwxS3ZwTXE2WFBnOHZIdFYwUmFIRTdGTGdkMTlVM21qaHBzWGNvd3JIVmlFWmJEYm5sV2x6T3RCbDVBalozblQzckpLQ01NVEVNcDNiejYtaHd5NFpQTEx3RU1vQnlZSHRmTUxNMWVNSkFrdHptYTJsZ1ZfVGtNdmNoU0llNUdzbU9qbDVaNzVtcDBPY2k4YUh3OFlqYlliYV96SGJKdnlENVRMTnU4RU12Wms2UkFUTWlZaXUxQ21GVE5XS0NiZFF6eF9CZDI1XzFnQ0hlVjBQZUpQekRwNWtKeVduUXVHczh2R3I2TmlHRzhla2FYZWlYSmwxOWRZZw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 14 Nov 2026 13:18:33 GMT
- [股價殺成這樣仍看好！「AI散熱雙雄」連摔 外資目標價竟飆上2,000元 - FTNN](https://news.google.com/rss/articles/CBMiS0FVX3lxTFByY1Z0cFh4SjA3THhaaDd0NEplVG5rb3U5Z3djejRoejFLX2lkbHVFeEwxTVhsdWZSd2RCYWkzRmV6SU5BWTNtSnItSQ?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 14 Nov 2026 04:05:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：股海自由行／遭錯殺 AI 績優股 伺機布局 | 證券達人 | 證券 - 經濟日報；Intel vs AMD: which chip stock wins the AI rotation trade - Yahoo Finance Singapore；Intel’s CEO Says AI Is Now Buying Almost as Many CPUs as GPUs - 24/7 Wall St.

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.28 | -47.98% | +47.09% | 59.66 | 114.68 | -47.98% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.53 | +3.48% | N/A | 534.06 | 534.06 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.03 | -28.69% | -18.88% | 162.85 | 228.38 | -28.69% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.06 | +2.84% | +10.07% | 2,350.00 | 2,480.00 | -5.24% | 同向 | 98.27 | 23.92 | 586.89B TWD / 59.71% | 2026-11-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | +16.36% | +6.48% | 523.88 | 523.88 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -1.19% | -10.86% | 347.01 | 446.77 | -22.33% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.02 | -1.16% | +13.47% | 598.00 | 703.00 | -14.94% | 背離 | 17.55 | 34.33 | 88.62B TWD / 47.13% | 2026-11-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.04 | +7.57% | +21.53% | 4,120.00 | 4,920.00 | -16.26% | 同向 | 62.35 | 66.27 | 55.03B TWD / 5.77% | 2026-11-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 2 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [股海自由行／遭錯殺 AI 績優股 伺機布局 | 證券達人 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE50T0NDOGFzamcwaUtoaEdmU014ZlpzdVZKN3phNGgwVm52cTV5STV4NWxaYllSQmtFVUtiaDBxQXpncWdHVTV2Q1NJTjdmV0NxbGJMVkQ4YU52Zw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 13 Nov 2026 18:39:57 GMT
- [Intel vs AMD: which chip stock wins the AI rotation trade - Yahoo Finance Singapore](https://news.google.com/rss/articles/CBMifEFVX3lxTE1vNWdvTXNxTWF4SHRqMEpUbU9PR05wNnEya2EtS2hhVXgyblFIWDEyMGlSWlBJdmdOdGk5UHRKVFBUcXFlV1JfN2N1Q1Fmb3ZqazZNWkdCTVdFRnlwZEs0ZTBTcmlGMERIV3o3YWsyc3NRWXF3ZzRFTVdfWmY?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 13 Nov 2026 16:03:45 GMT
- [Intel’s CEO Says AI Is Now Buying Almost as Many CPUs as GPUs - 24/7 Wall St.](https://news.google.com/rss/articles/CBMipwFBVV95cUxOelZLNkl1VW1Fdm9wYW5HNW43b1lKYVdkdTB0dEtfTWVJYlBubk8zdFhEZjVBNnVlaDlpY0k2T1NNblE3ZWlJeElzbEhPdDREZ2lLNVgtM3VTdzA0YWV2X3REVUhwZDV1RUVPcFByb3lyMVhvdklMRkxMOTNjQlJpd0ptTzNWNHlIOVd4d0F6R29LOGtJX0I0SDhUZkV0NUc3NERyU05GVQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 13 Nov 2026 14:09:00 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：AMD or Intel: 1 Chip Stock Is the Clear Winner - Yahoo Finance；AMD Tumbles 11%, Broadcom and Intel Slide 6% as Chip Rally Reverses - 24/7 Wall St.；Intel vs AMD: which chip stock wins the AI rotation trade - Yahoo Finance Singapore

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.28 | -47.98% | +47.09% | 59.66 | 114.68 | -47.98% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.57 | +3.48% | N/A | 534.06 | 534.06 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | +0.24 | -1.19% | -10.86% | 347.01 | 446.77 | -22.33% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.05 | +2.84% | +10.07% | 2,350.00 | 2,480.00 | -5.24% | 同向 | 98.27 | 23.92 | 586.89B TWD / 59.71% | 2026-11-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.04 | +1.00% | +10.33% | 101.50 | 164.50 | -38.30% | 未明確 | 6.80 | 14.99 | 25.20B TWD / 18.33% | 2026-11-01 |
| NVDA 輝達 | 產業/供應鏈推估 | +0.02 | -28.69% | -18.88% | 162.85 | 228.38 | -28.69% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | +0.02 | -19.84% | N/A | 778.31 | 971.00 | -19.84% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.04 | +2.91% | +5.98% | 885.01 | 2,335.00 | -62.10% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 3 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 3 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AVGO：新聞直接提及「Broadcom」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AMD or Intel: 1 Chip Stock Is the Clear Winner - Yahoo Finance](https://news.google.com/rss/articles/CBMikAFBVV95cUxPdHBQQld4eGVlRXdIRDFvUUpkTWhEd0Q0WVUwUnNnbGNNWmQ5NHplc1Z2azhyWTR6elpkUG5rX1pSQ0s0a3IySWd5VE9WOHowY285eWhlVjFoVzlsNUtydVN1dHpIanA2UldHdXFjdFYwWXpnRTdJZGJaUDlCdHkwVGhqbkRaTFE5bHdxTDYzUmI?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 13 Nov 2026 18:50:00 GMT
- [AMD Tumbles 11%, Broadcom and Intel Slide 6% as Chip Rally Reverses - 24/7 Wall St.](https://news.google.com/rss/articles/CBMirAFBVV95cUxORGF0bHBHVFVLQllub3poU29ZYjB0eGhLMGdOUWVwSWk5UHNOVTNwbE5oSGlEbHpQazdwUklLRHhxYS1nU2pIVzNMNElWMVBYOEJkX18taldPMDZKdTlZc3duSllBYkN6clJKZWw2MVhsc1ZqQkFGajM2NHJ2LWpUM0FxZUJOOElBdWE4ZXc5Zy1MbnFWdlBYdHRqSnZyYnhHcUcyTjlEU2JzSlFr?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 13 Nov 2026 16:56:00 GMT
- [Intel vs AMD: which chip stock wins the AI rotation trade - Yahoo Finance Singapore](https://news.google.com/rss/articles/CBMifEFVX3lxTE1vNWdvTXNxTWF4SHRqMEpUbU9PR05wNnEya2EtS2hhVXgyblFIWDEyMGlSWlBJdmdOdGk5UHRKVFBUcXFlV1JfN2N1Q1Fmb3ZqazZNWkdCTVdFRnlwZEs0ZTBTcmlGMERIV3o3YWsyc3NRWXF3ZzRFTVdfWmY?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 13 Nov 2026 16:03:45 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Micron Is Down 20% in a Month. What Will It Take to Get MU Stock Back to $1,000? - 24/7 Wall St.；Why are Micron, SK Hynix, and SanDisk stocks falling on Friday? - Invezz；Micron vs. Sandisk: Both AI Stocks Look Dirt Cheap, but This Top Investor Says One Has More Staying Power - TipRanks

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.28 | -19.84% | N/A | 778.31 | 971.00 | -19.84% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.57 | +2.91% | +5.98% | 885.01 | 2,335.00 | -62.10% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -28.69% | -18.88% | 162.85 | 228.38 | -28.69% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron」，共 4 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Micron Is Down 20% in a Month. What Will It Take to Get MU Stock Back to $1,000? - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiuwFBVV95cUxNelVwdm5oMDVMRW1lazFacTZYZXpVTHNKQXNQbjBoREsyUkpBVHVDbnJWM2dHTXdYQTZmVG9hUDR5NjV0c2FoWVFsaExLRXRBUWlGTUhBV0taQkRMbTQtZmpNbzR1TGxaUFNfWHgyM3NyMnU2VWxPTTRpRW0zczEwUm9vMm1Kc2ViMTZBM2MxeVZDQmxTQWR0T0ZRa3pFSmVVS29NczJHQTAzaVZSMUhITTZibjhNamFlQ2pr?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 13 Nov 2026 17:52:00 GMT
- [Why are Micron, SK Hynix, and SanDisk stocks falling on Friday? - Invezz](https://news.google.com/rss/articles/CBMinAFBVV95cUxOT1AtR2lzLXRZdkUwZkxnbVV4Y1RRQ1ZmRkZSTTUwWTBNc0ZRaDU5dUctQnFoOWxXQ00wbmJUMnRhcHo2eWNUVlZHS3FOVTJkcUlTdU1HVE5CdWw5WnBNWE0ydVlsbjRFYkdRUDBiT2VIYUQzWU1KenhUbkJQOTB4Ty1sRC1HMTRYQUtDYXVobUZYNjJtdFFrTWVETnc?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 13 Nov 2026 16:42:45 GMT
- [Micron vs. Sandisk: Both AI Stocks Look Dirt Cheap, but This Top Investor Says One Has More Staying Power - TipRanks](https://news.google.com/rss/articles/CBMi1wFBVV95cUxNV3Uwbnc2RUVKSkVEaU9UbjlhTWNsSzRnb2hPNkJHaWpDVlRyVXZYRUt0S1R2cENXaGJXdXRYNVBpVUg1bExCaG50OGFUbDd4ODRaVGNSMTFYQ2NTbXF2STdjUUJMM0pBTXJLaFMtMHVzd2E4Ynh5U0xKSjFYejdBUHQyeVRZN21fc3NPbmd1WGJvckRkUFBuaVR3MExSeEczRFZ0cjBJaThsUUd6Nnc4UlI1RzEzdExncU5uRURaZHN3TUwyTTVET21pYjdzWjE0bzg4aWw2WQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 13 Nov 2026 16:23:23 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：股海自由行／跟著國安基金 逢低分批布局 | 證券達人 | 證券 - 經濟日報；台股擂台／挑戰者「股市御錢術」楊育華 本周看好南亞、光頡 - 經濟日報；台股 ETF 正向槓桿商品犀利 四檔單周漲幅超過兩成 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [股海自由行／跟著國安基金 逢低分批布局 | 證券達人 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFAxNWhpbGZIM01EeTA4bnVfNHdXdDIxVDhrX3h3aEdzQkdLQzl1SnpaN2VwbnZ2Y0FqX1dsak9rQWtuWkx6cHBDNE80Tzc2M2ttSWR5MTNjZ2I3Zw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 14 Nov 2026 17:51:41 GMT
- [台股擂台／挑戰者「股市御錢術」楊育華 本周看好南亞、光頡 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTE1HYUJ2Y1BVanRRcXdkUzRzRDM2THhnNU1LX0VBanBWQlpQdE1PRWc4aUllSEoyZ2tGeERraUJHWDJDSlMyMUp4d2d2S18zQUpqM3BwQ3pPQWdRdEVK?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 14 Nov 2026 16:25:09 GMT
- [台股 ETF 正向槓桿商品犀利 四檔單周漲幅超過兩成 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxQV0tVMDl2RW5JdTZ3YThwcmFBVDJCQ2lDWS1mZllWaV9EdExWcWgwSUQxdmdQMWt4Njd6bHhoOE1DanNzV0hiVm16TVZvQVJWTDRrbGZ6TUxabWRNMWtPYm01M2Vib2o1RUVmeEpaeFM5VkU0ZTE2UWQwQXg5UnRGMdIBX0FVX3lxTFA2bVhaWFk4dTVxTlg3SFctM2lrS1lJeHNNZ2V1X0tPTWdzZUk3RVZCNFdhN1BGaWZhWWZpd3Q1bmREaXRDalZhdmw4RWpHOXFqczZxbG1lTm1ZQkZQc3VB?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 14 Nov 2026 15:17:36 GMT

## 新興題材：AI三雄營收

摘要：新興題材：AI三雄營收 相關新聞集中在：台股震盪、企業獲利卻創高！AI三雄營收飆破紀錄 00961掌握科技金融雙引擎 - 市場短波 - 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股震盪、企業獲利卻創高！AI三雄營收飆破紀錄 00961掌握科技金融雙引擎 - 市場短波 - 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMihwFBVV95cUxQUmNvMHg5b080SU1SYTItaGxCa2I0c0w3QmxQWmNfQm52R2ZrR3BmcVZINkZBekVLc3ZvTGJMc1FMUm1PWDRSY1FnbGFmUnhwM1FPTnp6dFUyNWZQVnVTd0hjQmI0Zjd4dmtDLTYtb01iTE0yVWJwOVhtOUtrc1N6Sm5XenZzb3M?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 13 Nov 2026 02:53:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
