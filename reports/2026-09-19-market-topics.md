# 每日股市熱門話題分析 - 2026-09-19

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜正向｜熱度 10｜市場確認 72.80｜同向 3/4
2. **散熱與液冷供應鏈**｜中性｜熱度 4｜市場確認 100.00｜同向 1/1
3. **半導體與晶片供應鏈**｜中性｜熱度 6｜市場確認 N/A｜同向 0/0
4. **關稅與供應鏈轉移**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
5. **利率與成長股估值**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.20（樣本 13）
- 5日相關係數：0.47（樣本 9）
- 同向比例：6/13

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 72.80 | 3/4 | 1 | +6.77% | +7.49% |
| 散熱與液冷供應鏈 | 100.00 | 1/1 | 0 | +10.72% | +5.27% |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 關稅與供應鏈轉移 | N/A | 0/0 | 0 | N/A | N/A |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 5.26 | 2/8 | 6 | -4.08% | +1.05% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-09-06 | 0.19 | 0.43 | +50.00% | 24 |
| 2026-09-07 | -0.15 | -0.09 | +53.33% | 15 |
| 2026-09-08 | -0.07 | 0.18 | +57.89% | 19 |
| 2026-09-09 | -0.28 | -0.12 | +54.17% | 24 |
| 2026-09-10 | 0.28 | 0.86 | +75.00% | 4 |
| 2026-09-11 | -0.01 | -0.08 | +25.00% | 12 |
| 2026-09-12 | -0.39 | 0.04 | +25.00% | 20 |
| 2026-09-13 | -0.42 | -0.14 | +17.65% | 17 |
| 2026-09-14 | -0.31 | -0.54 | +33.33% | 15 |
| 2026-09-15 | -0.04 | -0.42 | +68.75% | 16 |
| 2026-09-16 | -0.19 | -0.46 | +55.56% | 9 |
| 2026-09-17 | 0.43 | -0.13 | +66.67% | 9 |
| 2026-09-18 | -0.15 | -0.07 | +35.71% | 14 |
| 2026-09-19 | 0.20 | 0.47 | +46.15% | 13 |

## 歷史回測摘要

- 回測日期：2026-09-19
- 近5日 3日相關：0.19
- 近5日 5日相關：0.23
- 同向比例：+42.86%
- 權重狀態：未調整

- 方向準確度：+42.86%
- 信心排序準確度：0.19
- 診斷：弱正相關

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

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Intel vs. SK Hynix: Which Chip Stock Is Worth Chasing After This Week's Surge? - Zacks Investment Research；What Could Intel (INTC) Gain From a US Memory Chip Push? - simplywall.st；Intel Stock Jumps 4% on SK Hynix Rumor, But Here’s Why the Real Win Is Years Away - 24/7 Wall St.

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.57 | +4.61% | N/A | 1,015.80 | 1,015.80 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.28 | -5.30% | N/A | 108.60 | 114.68 | -5.30% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.57 | +17.04% | +9.70% | 1,791.82 | 2,335.00 | -23.26% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.43 | +10.72% | +5.27% | 222.27 | 222.27 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「memory、Micron」，共 4 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：shortage。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel、INTC」，共 4 篇新聞命中。 方向判斷命中詞：surge。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 2 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：shortage。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。

### 主要來源

- [Intel vs. SK Hynix: Which Chip Stock Is Worth Chasing After This Week's Surge? - Zacks Investment Research](https://news.google.com/rss/articles/CBMitgFBVV95cUxOMEFXQ29yMHczbUs4TVo5OGFnSlRYNk1JY0VRR3lzSmdaUmJXaEFvRHlTa3VSOWxkVmpvNmlISnF0UF9DSC1uS1F6aHJ5aFVSU2tob01FRmR4MFpjVkcwdEZ6NE5HckhpeG16ZmRCdzJ3bVUwby1pVE9Bd3hLTkdpSDBhUXJ3UG5YZDRZbUhPRXFWQ2FNd210Q2szcFBMai1vR2hkWk10d054TjAtSlFyYVZ3blBNZw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 18 Sep 2026 18:31:59 GMT
- [What Could Intel (INTC) Gain From a US Memory Chip Push? - simplywall.st](https://news.google.com/rss/articles/CBMiwAFBVV95cUxPcnVoYjNOdUduSXVUMnEwXzRELVM3bV9VY1UzcUZSMGdRMWVGc2k2OUFJWnozM3d6cmRleDVXQmhBN1lTaDBKMEJ2b0JCQzlLUlRkWllMdVRhcG1KTUFFY2gzdWl0SlpGNmVCdmNicWJVNDN6V2pFWmR1TE5saEJUend3Zkl4cVI3Q2JNUDZBeWctRm9YdEN5VmE0WjBfNEJyYUNJcVdDYTF3NWVvZ0NRelA2NkxwdG1nTDAwQktCVW_SAcYBQVVfeXFMUEYwNlV2cmt3cklJNkNoYk9NbzdBT2F6RlllNTBXaEJwUmp4MDlLOEpNLVBWOVFtcE5sVURRbTRYNkh3YzZaYjFUMW1zTE4yUTNBOGpQdEZJZEw2T3J3QWhuRUNJUFg2QlBGNDVyTVgwVEVsaGpnQ1lNaHBXZDdGcWxrU2VLUUhRc2YyT2EwV0Q3WXVOdFdYQ3hPb1JWVlowb2JqZHpKcXdhYl9GQTJha1IyaGpnY3JtR0M3UTd3Rkd6M1o4SDRB?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 17 Sep 2026 02:33:57 GMT
- [Intel Stock Jumps 4% on SK Hynix Rumor, But Here’s Why the Real Win Is Years Away - 24/7 Wall St.](https://news.google.com/rss/articles/CBMivwFBVV95cUxOZ2duanBTWEwtaEJVM0M2TG1OYV9zS2laNjYtekxwSDRPUGNnajVQOHR2Sk9ydEZ1M3dkcHZWTDNPcDhqS3h6ejFKdUVPem43a3A1NVc3WktLRy1CeVhiT0hxTllhSzV5U3ZSQmpDWUlmRUEyYXBQT21uS1NVY0NnMzg1bkowVW9Mb21ZOUxKb3FfM3J3ZlQwSjJZbTkwNGtCN3ZfdUxmRjhjU09TdlRWdUJZX1daQVNYYVBsOWlJdw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 17 Sep 2026 16:03:00 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：輝達、Google、AWS訂單齊發！這「 散熱廠」今年EPS上修至106.51元 法人目標價喊上4500元 - FTNN 新聞；焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報；台股Q4有新主角？兩檔主動ETF押健策、金融股也入列換股方向曝光- 證券 - ctee.com.tw

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | +10.11% | +1.78% | 3,430.00 | 3,430.00 | 0.00% | 不適用 | 75.13 | 45.72 | 19.48B TWD / 54.34% | 2026-09-01 |
| NVDA 輝達 | 新聞直接提及 | +0.42 | +10.72% | +5.27% | 222.27 | 222.27 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 2 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：跌停, 上修。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：上修。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [輝達、Google、AWS訂單齊發！這「 散熱廠」今年EPS上修至106.51元 法人目標價喊上4500元 - FTNN 新聞](https://news.google.com/rss/articles/CBMiS0FVX3lxTE9yd20yMnNacGQzOFcxZDRtSzZic29PRzJ4bUd5S2k0UlhYeU9fWE5tSjZrZVVDR1BnU0FNRWZlT0l1Rlh4d2VHZFNsSQ?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 17 Sep 2026 15:45:00 GMT
- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 17 Sep 2026 18:42:33 GMT
- [台股Q4有新主角？兩檔主動ETF押健策、金融股也入列換股方向曝光- 證券 - ctee.com.tw](https://news.google.com/rss/articles/CBMiX0FVX3lxTE10eUlJSkI0ZjRoc2NhQ3ZqUVJONTN4YWxvV19zelFMRmJoWFUtWjExNFg2SWY5OV9CYThfZ21PMW01akxjck9LT2t1VXdVaGRIYXE2TTVDRURua0V5UE5B?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 18 Sep 2026 23:08:00 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：72名越南FPT大學生赴亞大 半導體育才跨足東南亞 - 中央社 CNA；AI 時代下，敢做決定對半導體研發有何關鍵影響？ - TechNews 科技新報；This semiconductor stock is in the dumps. BMO says it can bounce back - cnbc.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | -5.30% | N/A | 108.60 | 114.68 | -5.30% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +3.14% | +2.07% | 2,460.00 | 2,460.00 | 0.00% | 不適用 | 86.28 | 28.52 | 514.81B TWD / 53.32% | 2026-09-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +12.64% | +11.03% | 156.00 | 164.50 | -5.17% | 不適用 | 6.68 | 23.46 | 25.04B TWD / 30.71% | 2026-09-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +10.72% | +5.27% | 222.27 | 222.27 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | +8.47% | N/A | 559.82 | 559.82 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | +4.61% | N/A | 1,015.80 | 1,015.80 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | +17.04% | +9.70% | 1,791.82 | 2,335.00 | -23.26% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -8.14% | -19.96% | 357.61 | 446.77 | -19.96% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 CPU, server CPU, x86, foundry；其中 1 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 1 篇新聞出現相關標籤。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 1 篇新聞出現相關標籤。

### 主要來源

- [72名越南FPT大學生赴亞大 半導體育才跨足東南亞 - 中央社 CNA](https://news.google.com/rss/articles/CBMiVkFVX3lxTE96d3lqQXBHTFFDYWt1NjJpOW4tdU9jOWZUemJ0MHQwcmZmSnF0bDJTWW4ySVJVRllQZzNZVFlPRmJ6RWZiNTliaEtzY2JBa0RjLWhKSUhB?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 18 Sep 2026 03:09:21 GMT
- [AI 時代下，敢做決定對半導體研發有何關鍵影響？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1EQkQ3ZXcxZThvMUZoVll6UzNDbjZrZDRNSE82Z3haaDUyYU45QjB1TVh0ZUN1QWY1Mmc5ZUxGS2k2SmxURUJwXzA1dVdoZmZCYnc3ZEFzeXNJOFk?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 18 Sep 2026 11:34:37 GMT
- [This semiconductor stock is in the dumps. BMO says it can bounce back - cnbc.com](https://news.google.com/rss/articles/CBMiqAFBVV95cUxOQ2ZGSzlpR1VnMV92MG1EZndUUkpWejBkSThPS3N0dWhSNi13V05JcUVaOGUzU05JTURlQ2pIdHc5WUdPUUc5cm9pa1BPU0Q5OTlSc3Z6eW4tTk1LdnVaX1I5SlFBYjRiYk9ReDZiTW9DZTFnQUo5Sm5qdEhoV21sSmtmZE9RLUU5LUp2Rm9ieHh4dEhwMGNlZDJOaEVadjc3bDZnZW9Cb04?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 18 Sep 2026 14:29:37 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：泰國進軍前端晶片製造，如何衝擊全球供應鏈？ - TechNews 科技新報；光傳輸升級再升級！明年1.6T光收發模組大出貨法人聚焦聯亞、全新等InP供應鏈- 日報 - ctee.com.tw

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +7.71% | +20.54% | 336.13 | 337.00 | -0.26% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | +1.62% | +1.01% | 250.50 | 289.00 | -13.32% | 不適用 | 15.21 | 16.51 | 921.77B TWD / 51.98% | 2026-09-01 |

關聯理由（前 3）：
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [泰國進軍前端晶片製造，如何衝擊全球供應鏈？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMijgFBVV95cUxQcjVQMm1DM3I1QmdpLVhEOHNzY2cxYnN2SmIwVHBTZ0xqLUd3Tzl5emxBaGVZQ0ZlZDJhTEx0a2JCSVU5YnpUYXRmUlh3TnZqSGlUTUlxbWZLMlV5UWVSX1pzQmtxbGgzb0Eyb2lUQVpVdUpDSG5PalVrM2NwUHJIc0s5eXFSRU1JNDRPaDJB?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 18 Sep 2026 14:06:35 GMT
- [光傳輸升級再升級！明年1.6T光收發模組大出貨法人聚焦聯亞、全新等InP供應鏈- 日報 - ctee.com.tw](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5DUVRlMkNTcUJ0YzUyWFlaOWZjZ1l0cU1oUVNvdktOZ2VfMXZjRENmRHBrUThheGd4OXV1R3lORUt6TS16Mk9RdVdfUkxNOVl3UDdDTTR3OW8wOC1GbXRr?oc=5) - Google News source discovery | 工商時報 Thu, 17 Sep 2026 19:00:00 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：AI 通膨來襲？央行：短期可控、長期生產力提升將降壓 - TechNews 科技新報；全球央行調控通膨 美股漲跌互見 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +9.67% | +0.36% | 493.78 | 507.29 | -2.66% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AI 通膨來襲？央行：短期可控、長期生產力提升將降壓 - TechNews 科技新報](https://news.google.com/rss/articles/CBMi3gFBVV95cUxQYlNycFBnMW1Fa1F3VGxsTmtidEFWdmRtVFAtcFdDelF6M0lveEtRWkRuQ0ZuM2s3eG1NZjJsc05WMWxYaFZPRmNrQVAyZXBjNXczZW44Y29tVDBEMVp5eE5MaWVZdDUtcWRDcWxGdjhFV25fLTR5VU1lcjBNbFZoQlIyemZwbllUazV3X0RBRTkyV2JYLUlTRFZqRklDSk54NmhpeVhObjNlTjZ6Q3lwcmRCUWZfUHEzemQ2Ylc2d3lKREFtNHdJQ2dEUE1PT0lrVlNFdk5WM3VNOExraVE?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 18 Sep 2026 08:40:07 GMT
- [全球央行調控通膨 美股漲跌互見 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTE5DOXdvaG02SzBGRzRHaXI3V2pOUy1YMzEwaFNOQnE3ZnJQVmt4dndaSUFiQjlKRFZJNDdaUV9Hank2NjVtYUhzc1Rpa2E2VWJvWFI3bGhVX3ptVnFM0gFiQVVfeXFMT0hNcTZiVWJjUmJEcWUzRUVtMkRiSjcwUXRraDFhWFFxRHh1NXVia2JRdko4eXVySFFjRWVBOV9kcnkwaDNPS01oem5uemdxNDR0TENzdHBBQURCV3JjUTY0MlE?oc=5) - Google News source discovery | 經濟日報 money Fri, 18 Sep 2026 21:21:25 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Agent 隱瞞錯誤，企業導入 AI 應如何評估風險？ - TechNews 科技新報；AI 時代下，敢做決定對半導體研發有何關鍵影響？ - TechNews 科技新報；深度競合策略，對 AI 投資有何啟示？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | -0.08 | -5.30% | N/A | 108.60 | 114.68 | -5.30% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | -0.03 | +10.72% | +5.27% | 222.27 | 222.27 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | -0.03 | +8.47% | N/A | 559.82 | 559.82 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.03 | +3.14% | +2.07% | 2,460.00 | 2,460.00 | 0.00% | 背離 | 86.28 | 28.52 | 514.81B TWD / 53.32% | 2026-09-01 |
| MSFT 微軟 | 產業/供應鏈推估 | -0.02 | +9.67% | +0.36% | 493.78 | 507.29 | -2.66% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -8.14% | -19.96% | 357.61 | 446.77 | -19.96% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.02 | +7.77% | +3.24% | 638.00 | 680.00 | -6.18% | 背離 | 13.92 | 46.16 | 82.25B TWD / 45.66% | 2026-09-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.02 | +6.32% | +2.73% | 4,710.00 | 4,710.00 | 0.00% | 背離 | 60.69 | 77.79 | 64.18B TWD / 44.08% | 2026-09-01 |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Agent 隱瞞錯誤，企業導入 AI 應如何評估風險？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiogFBVV95cUxNZ29NQ2xMdG5Od3prZkhmQ1hwdExpRmRFTUhIeFc5aDltYTJteVg1cnU1NjM3NVBqZkI0alZCM0lVcDJnUmJEcVFNNkVWQjA1eWdQWjhhZ05MaU1tMlVHQzNDMFRKVmxKc3lraVFUTGFNdjhUNW00MnNSb2JIczZlTGxEQWdQZ1pTQWZncDc2OTNOa2xXU3lXT3hyb1BRTkEtX3c?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 18 Sep 2026 14:34:58 GMT
- [AI 時代下，敢做決定對半導體研發有何關鍵影響？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1EQkQ3ZXcxZThvMUZoVll6UzNDbjZrZDRNSE82Z3haaDUyYU45QjB1TVh0ZUN1QWY1Mmc5ZUxGS2k2SmxURUJwXzA1dVdoZmZCYnc3ZEFzeXNJOFk?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 18 Sep 2026 11:34:37 GMT
- [深度競合策略，對 AI 投資有何啟示？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMicEFVX3lxTE11dlEtejB4SG1BNVk5TVRmZ05kb3BxcS1kd2FjdmpEVFI1c2FVVFBRYk45bmV4cUJibGZyR2RBdzJjRlpxSVBJY25xRUdoZDM3U1BDSXBzQTA0ZnRVaE8zZmtsOW5NVFJsYi1zMUdLeFY?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 18 Sep 2026 11:04:54 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：三大法人都回來台股了！台股大漲近900點、共買超1,165億元 - 經濟日報；升息不確定引信拆除 雙王領漲 台股外資回補869億 - 經濟日報；台股週線收紅995點　上市公司總市值升破154兆元 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [三大法人都回來台股了！台股大漲近900點、共買超1,165億元 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFB4eklXTWVfWWpaNUZBTjdpNXlUZUlLTTZ6ZTVJNFVuLTlzenNtb0JJTlB4VzJsQ0lWbl9ZcGtmUmRRSmZyS2k3YzNJUkozOEZjZEFsM3NPUjJfd9IBX0FVX3lxTE5MVTFqamFYZUtEbTk0QUhoQm8zeHozNDRGcHVtc0JaMm1VcURkbUFYQWh3MERiVHNnYUdhcUNxMFZzc1pYalh1eVpicmhvNlhLR0tDclhCTTdKM0ZhZllZ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 17 Sep 2026 09:00:00 GMT
- [升息不確定引信拆除 雙王領漲 台股外資回補869億 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE4zNWNOcWpQM0JrQzgwakstdW15MXdZc0N0ZWxYdE9Sb2ZDNmtrZFRuRllMR3VZVy1Id3Fod2pjN0MydVJpaUVqaldiQmpWdjFXUkVSRXRqZTlzd9IBX0FVX3lxTFA1bU1lTGhyckREUjhDWF9nbVBtS01PVnZrQzlNV0dROVByc2RBaUlma2VFYmJGeXhOdnE5VGJrUGZZa29FSTIwWGs4WkZSWS1Sa1Z1X2JHSWRFb2tfTUln?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 18 Sep 2026 16:48:31 GMT
- [台股週線收紅995點　上市公司總市值升破154兆元 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxOcHZEb1NzMUhRLTNLY1NnTHQ1SC1jSFpOUnlFejRoY3dUalZJd09Fb0hocEhuaG1QeUJQWFZCM0Y5MHFyT0Vtd01Zd3ZpZHFzMG1kdHBfY29QTnVJekRJNGU5MEt6WEJqUHdlWDdaa283OTZ1aGVBUkp3UmhfYVQ1cdIBX0FVX3lxTE12d19iT1FaMG9YaHliekw5N1kwcTRpeWRfc2NwZDRKRksxUGlsenJfQkt2c3kxZ1A3aTZYZVNXVGxJVTdycEdzLXFTLXNQZGF4SGxBSWJodkFNQ0ZOUnJv?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 18 Sep 2026 10:21:47 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》量增大漲892點、重返47K；週K翻紅- 新聞 - MoneyDJ；個股動態報導內容-A9215FDA-158C-4C15-9578-1225FC644816 - MoneyDJ；個股動態報導內容-D0266336-3C69-4DAD-A624-36ECFB1F8FD2 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》量增大漲892點、重返47K；週K翻紅- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxOUVdycFg2VGZiODRnbUIyUHhGck5YaEVnM19zVW54V2ZBdGtRRUFyZUVOckI3b2pjOTJpeXZiRFVTbm13LXlQa2J2RW1fLWI0eE8xYUVBd2ZJX3lOVWdPWTdDekVBZDFPamhMN29GaWpqY09vVGNJdGRucGp2NzRUWERXQlEwRkpTWW1abmNFWllPdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 18 Sep 2026 08:06:00 GMT
- [個股動態報導內容-A9215FDA-158C-4C15-9578-1225FC644816 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxPUWhOejcyYWxpZHI5ZTVoeDlYUnhOS3J3dWw2N1ZSNXdZbFZ5SFRMZ2lkSWNzWFBySzJDdzF0WS13ZEtPSzhPN3BISUZiZldBaWV6WXVfVHZ4QnNFSU1mV3RIcU42dWxqX05DN1JkRWdaZnNnSDdvb0VOWU81R0tkZXdJeERZUjFxTVIybE54bXpCeW9N?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 18 Sep 2026 13:25:47 GMT
- [個股動態報導內容-D0266336-3C69-4DAD-A624-36ECFB1F8FD2 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxQNlltNXNYV0syTURtUVJPNWlJUXZpU0lRZWM4YzY1OGJiRG01ZUgwTDBJQkN0NXRhMDVoQ1d6MWFGY1lhcXVGaVNzYXhsQkdvLVdBYkhTRHdfamlnY0FVY0txdl9hUnZ2VGtReGpyeDNuRFloRE9QbVVuVHZGMnVuNGF1ZTZBekJmci1RYmsyc1MwT3hE?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 18 Sep 2026 11:38:58 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
