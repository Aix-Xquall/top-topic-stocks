# 每日股市熱門話題分析 - 2026-10-30

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **散熱與液冷供應鏈**｜負向｜熱度 2｜市場確認 100.00｜同向 2/2
2. **利率與成長股估值**｜中性｜熱度 4｜市場確認 N/A｜同向 0/0
3. **記憶體與 HBM 供應鏈**｜負向｜熱度 11｜市場確認 29.68｜同向 3/6
4. **AI 伺服器與資料中心**｜正向｜熱度 14｜市場確認 24.64｜同向 3/8
5. **半導體與晶片供應鏈**｜正向｜熱度 7｜市場確認 30.72｜同向 2/5

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.00（樣本 21）
- 5日相關係數：-0.05（樣本 14）
- 同向比例：10/21

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 散熱與液冷供應鏈 | 100.00 | 2/2 | 0 | +10.49% | +6.62% |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 記憶體與 HBM 供應鏈 | 29.68 | 3/6 | 3 | -1.77% | -0.34% |
| AI 伺服器與資料中心 | 24.64 | 3/8 | 4 | -0.54% | -1.21% |
| 半導體與晶片供應鏈 | 30.72 | 2/5 | 3 | +0.91% | -0.13% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：台達電預期Q4營收 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 相關性偏弱；應提高同向價格確認權重，降低泛 AI、泛半導體等寬標籤推估權重。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-10-17 | -0.10 | 0.49 | +26.32% | 19 |
| 2026-10-18 | -0.12 | 0.33 | +21.74% | 23 |
| 2026-10-19 | 0.44 | 0.36 | +50.00% | 12 |
| 2026-10-20 | 0.09 | -0.81 | +69.23% | 13 |
| 2026-10-21 | -0.25 | 0.23 | +5.56% | 18 |
| 2026-10-22 | 0.02 | -0.21 | +38.89% | 18 |
| 2026-10-23 | 0.35 | 0.29 | +78.95% | 19 |
| 2026-10-24 | 0.09 | -0.31 | +70.00% | 20 |
| 2026-10-25 | 0.41 | 0.78 | +64.29% | 14 |
| 2026-10-26 | 0.27 | -0.25 | +36.36% | 11 |
| 2026-10-27 | 0.07 | 0.31 | +50.00% | 18 |
| 2026-10-28 | -0.30 | 0.47 | +20.00% | 15 |
| 2026-10-29 | -0.05 | 0.04 | +42.86% | 14 |
| 2026-10-30 | -0.00 | -0.05 | +47.62% | 21 |

## 歷史回測摘要

- 回測日期：2026-10-30
- 近5日 3日相關：-0.02
- 近5日 5日相關：-0.01
- 同向比例：+38.46%
- 權重狀態：未調整

- 方向準確度：+38.46%
- 信心排序準確度：-0.02
- 診斷：低相關

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

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：散熱股又有大消息？花旗喊買奇鋐、雙鴻 目標價齊升逾14% - 經濟日報；Weak quarter for Intel sends shivers through cooling chip stocks - Reuters

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | -0.45 | -1.27% | -6.62% | 2,910.00 | 3,435.00 | -15.28% | 同向 | 75.13 | 41.39 | 21.02B TWD / 44.92% | 2026-10-01 |
| INTC 英特爾 | 新聞直接提及 | -0.43 | -19.72% | N/A | 92.07 | 114.68 | -19.72% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐」，共 1 篇新聞命中。 同時符合主題標籤：thermal。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 方向判斷命中詞：weak。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [散熱股又有大消息？花旗喊買奇鋐、雙鴻 目標價齊升逾14% - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE04UXU3RGRUUnBBVElIbVBGZWozMUxfTzNsbE50ejYzRE1pUTJBQ0FNWS03VjRSYlZrUWkzSXhuNHhFQl9teWs5YTJ4QUU4ck1MZ0NneEk3XzF3UdIBX0FVX3lxTE5tclh3dXNNWDhDMnNiYmMyRW1DRFJwZUt6ZlZXMmdEYlhoQU9VR1pSeTVrVUpVT2FWOE1idEkxdXRhYTYyYVpMcnRwaWQ4NGpmRUNTREJUQ2UwNU01N0pF?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 28 Oct 2026 09:00:00 GMT
- [Weak quarter for Intel sends shivers through cooling chip stocks - Reuters](https://news.google.com/rss/articles/CBMiqAFBVV95cUxNcXEzUmpkSHEwZWtxM2cwVjMwQkJXMVZqVUJrWk8xejY0TzkyZmtvN0E2Z3Q3MDJfNkRLOXRKUW5xR2QzLVM5WjQzSVp2OVBhQldOMVJKZkJ2ZC1qMm04dWFSVjExd1h2bXV2emx1dmkwTVFzT29DamloeVhPZUdwZEhuUmhvem92VG9MQzFIZU1ibDR1MWNaZ0o2ZVBOYzhodHdyQVY4T1U?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 29 Oct 2026 21:10:54 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：Serval triples valuation to $3 billion as businesses adopt AI workflow automation - Reuters；〈美股早盤〉AI砸錢何時回本？Alphabet財報失色、通膨又施壓 主要指數開低 - Yahoo股市；美國第三季GDP增長3.4%，通膨震倉壓力持續 作者 Investing.com - Investing.com 香港 - 股市報價& 財經新聞

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +17.75% | +7.75% | 530.14 | 531.01 | -0.16% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Serval triples valuation to $3 billion as businesses adopt AI workflow automation - Reuters](https://news.google.com/rss/articles/CBMiuwFBVV95cUxQWGsxVlVwdm94YVFRbXJ6eWNIXzRuWkZqVkZwNm5QUnkyc0EyUHFyY21WTE9LRFNRSVpEbHg5b0UxaGJsbEYtdVRuTWxHN0xFVnkwa1kya1I4S0ZadXhGQmZmZWtQdGJvbDVrQXI1UVhjLU1zWTdPQWlpLW5ubEdEMWhrczRhbGNHUVRxVTJBZVZtVmpiT0UtWlYwZEZMRjN3NW1LSFhYR1pfc1lLS0lBaGdnc1pLazVyT0dJ?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 29 Oct 2026 12:02:45 GMT
- [〈美股早盤〉AI砸錢何時回本？Alphabet財報失色、通膨又施壓 主要指數開低 - Yahoo股市](https://news.google.com/rss/articles/CBMimgNBVV95cUxNdzZEUEpFUkVOaEplb29jYmROTE8yODdCaEFFYTA4YzJiZ1FCbm96dzVGejZDeE9tcThEZHRfbnBEakwwM25WN2lmNVh6andMVmkxTHVwRWFFbEJVQ2dEbXRuRFRkX1BxLW1pbVlnMEhLdW5qYlJhY3NZOXJKUlhUelJDSE12WUx1Sm5QaGJhTU03bmFld3ZpOXVZa2t6RVo1TDZNUVpRUHhkdzlVSllQcVBSTXpmRUJERGRKakVKREFZdnd5SDh3WXA0RTk1ZDdsaUgxYVEtbzRvanFWSU1ybWdmdVBRMXAwLVZ4M2RWT0VGQ3lRd0c4SFdySU1mVkJNMVg1Zkg3SGlUVmE2QjlKUDZONF90dEJZLUhiTDhKX0xHZHFaZTlHQnFlNHVmSWR4c2VSSnh0SGJyRjhUeklhYjhOZmpVTzU4and0OVhNemxEbEpmZnJtTldwbmN6Q1VHRjZuMnJ1NGt0bzRmWmZYM1FpN0F0UjZtUktISmN1RDlwWmtRcWJPQV9TOEEwSFE2RHRZZUJmbmtJQQ?oc=5) - Google News source discovery | Yahoo 奇摩股市 Thu, 29 Oct 2026 13:40:18 GMT
- [美國第三季GDP增長3.4%，通膨震倉壓力持續 作者 Investing.com - Investing.com 香港 - 股市報價& 財經新聞](https://news.google.com/rss/articles/CBMic0FVX3lxTE9zUWFKQWZpQU9MWEgzU3RnZWdOYVZzM1RUUEdIM05TdWlaTWo4VjgyS3Y0MlRjX2hkRHB0dXdPUUwxamtBdERmWGJNRjl1dG83RnZWS2k3VWNUMDQ5MmFRLUZjS1dQYTdlLUthX2t3SzMyVkE?oc=5) - Google News source discovery | Investing.com Calendar Thu, 29 Oct 2026 16:49:12 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：INTC, AMD, AVGO, MU Decline On Samsung’s Profit Miss, Lighter Capex From Microsoft, Alphabet - Yahoo Finance；AMD, Broadcom, and Micron stocks lead chip sector higher for third day in a row - Yahoo Finance；Sandisk and Micron Slide 5% as Samsung Miss Cools Memory Rally Ahead of Sandisk Earnings; SK Hynix Falls 3%, Western Digital Dips - 24/7 Wall St.

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | -0.59 | -3.78% | N/A | 934.27 | 983.23 | -4.98% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.29 | +13.47% | +1.93% | 1,404.77 | 2,335.00 | -39.84% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.26 | +9.75% | N/A | 566.42 | 578.44 | -2.08% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | -0.51 | -6.84% | -8.67% | 345.00 | 446.77 | -22.78% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | -0.43 | -19.72% | N/A | 92.07 | 114.68 | -19.72% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 新聞直接提及 | -0.21 | +17.75% | +7.75% | 530.14 | 531.01 | -0.16% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -3.22% | +6.78% | 213.66 | 228.38 | -6.45% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：decline, falls, miss, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：falls, miss, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 方向判斷命中詞：decline, miss。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [INTC, AMD, AVGO, MU Decline On Samsung’s Profit Miss, Lighter Capex From Microsoft, Alphabet - Yahoo Finance](https://news.google.com/rss/articles/CBMikwFBVV95cUxPc2ZMRUR5SGxXOExveVpWbURvMjlSc3lCcmIyN3EydF9CSjRkTVpTR1N1YkowTTlJVnE1RnBTSk1DNzBVV0hjRkFGNE9KbGFHSTBaN1o2MmNDaDlZbk1HRDh6Ui15WngzWjloUmJ4U3BWcllmNF9GYWc2WXk5c0d1c293bXZkNWptcXl4eVFrY0NGU0k?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 29 Oct 2026 07:02:37 GMT
- [AMD, Broadcom, and Micron stocks lead chip sector higher for third day in a row - Yahoo Finance](https://news.google.com/rss/articles/CBMizwFBVV95cUxNLUNESjNKQm9WM29KdEpZZlN1dGpYam5zbUhBUDE0X1lnLW1xZ3BGaFpsUld2cTJzVDJaeV80UTdyNWcyUW5xVkZEZ2Z5a0VNYlROSTZGUGRPQ0JSUFVINXNhWUcyQVo5MTRULWs2SVVLUXI5ZVd1SzBWbm1jdzNORkt0SkM5WHV4aUhGTlRiQ29TNzluVTlGTERRdmNiNklmVV9kMUQwbktWWHJVZHo0SndTYWVQeTdYM3h2dzF5WmJrWXZGLXk2Q3QxLTgxV3M?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 28 Oct 2026 13:57:56 GMT
- [Sandisk and Micron Slide 5% as Samsung Miss Cools Memory Rally Ahead of Sandisk Earnings; SK Hynix Falls 3%, Western Digital Dips - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi_gFBVV95cUxPUTVoOHM3cGRfOTVDVENWV3cza09ETURab0FjUEhxVm0zMUVjU0txVWJodFktb2czT21aS29KUThnMHRzN1d5YUE3VFV0NDU5LXYxclVGTEtydzhGZEhZdVhQZ2hPYUsxM3p4ZE83SU56VTM4N1BaQzUzRG9HbGZnRzVURThXVUJsYUpoWmdhdlctVmNUZkRjQThyNTY3aS1lVTVJdm1QMTVfQ0xTY1Jrd3ZleW10c1AwYndnYjVkNm5qRHRCZDM1SThnbEx4YVcyNUY4RzBfNTg5QjZVcXJ1VmxXcUw0TWYtbG0zTUxTZlZvM1dabnMyN2NoYnd3QQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 29 Oct 2026 20:09:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：美國防科技公司高層示警：AI 競賽恐促使習近平奪台 - TechNews 科技新報；AI 說錯話誰買單？當聊天機器人成為法院被告 - TechNews 科技新報；法官怒了！律師費照收，訴狀卻像 AI 交作業 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | -0.08 | -19.72% | N/A | 92.07 | 114.68 | -19.72% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | -0.06 | -3.22% | +6.78% | 213.66 | 228.38 | -6.45% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | -0.03 | +9.75% | N/A | 566.42 | 578.44 | -2.08% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.03 | +1.26% | +0.42% | 2,370.00 | 2,480.00 | -4.44% | 背離 | 86.28 | 27.99 | 511.86B TWD / 54.65% | 2026-10-01 |
| MSFT 微軟 | 產業/供應鏈推估 | -0.02 | +17.75% | +7.75% | 530.14 | 531.01 | -0.16% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -6.84% | -8.67% | 345.00 | 446.77 | -22.78% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.02 | +4.43% | +3.48% | 631.00 | 703.00 | -10.24% | 背離 | 13.92 | 49.42 | 88.13B TWD / 45.52% | 2026-10-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.03 | +0.87% | -2.53% | 3,810.00 | 4,920.00 | -22.56% | 未明確 | 60.69 | 66.80 | 55.40B TWD / 1.97% | 2026-10-01 |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：恐。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：恐。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：恐。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [美國防科技公司高層示警：AI 競賽恐促使習近平奪台 - TechNews 科技新報](https://news.google.com/rss/articles/CBMilgFBVV95cUxPZzhqQmxudGxMMWp4SnBNVXh3QzJ1VHFsQlFrMDZDZXVYTi1YSU1yOXd5d1V1U2dpRjhYazh0ZVZEZHhyNDlGUnpRZXN3TWV4VmdsS3ZpOURHbGxjdFpGWThURWh6X01xazFZalVpTDdWMWNKVlJFRmhzVTlDeWJNNERiLWhiaGhqdzlFbFdiVllIMTZwQUE?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 29 Oct 2026 01:33:29 GMT
- [AI 說錯話誰買單？當聊天機器人成為法院被告 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiwAFBVV95cUxOSUI3MlZpUGdIa2ROcHNjRDRUR0haY0FBU3NvYXB6RTJNR3RqUVhSVnItZHg5QlYxQ2ViTE1lSldwbjZYNm92aFBUakR4ejVHS1lWSEhYaFlGTWJBRTNLcm5aUW5OZldwa2hXOHB3anRJdkFsWVJpZXA1eU5qUzhLSU82YnJLVDJPMmQ5a1pXWF91eWwxSVMtSE1ta2VIQ2I1U09ZZms0M0tZcmtEYlluc0lpWXJnMVlnaHM2VHNNNjA?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 30 Oct 2026 00:03:51 GMT
- [法官怒了！律師費照收，訴狀卻像 AI 交作業 - TechNews 科技新報](https://news.google.com/rss/articles/CBMixAFBVV95cUxQc1AwOTgwVmFqam1BcGxqU2xMV2gyMEg0M08tLTd4OE92ZjRIY2lGd3FfUTRHdjZocWZ1S0h0QkNteUxYNmhBMDhZNjJYc01MUm5LSm42NFVWNERPT2ZlUkMyQU90TjZTVTNzOF9MVVcwZjBWX01GS29SY0dMZWVidXJ4MVlMN3dYYk5WOEhsNFdWUmVPTGRkY0trRFo5VVd0X0Y2TEhyc2JLS29uXzVuajA5QVFaTkFYYmZRdkprSzlPWDhG?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 29 Oct 2026 23:53:49 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel Drops 4% Ahead of Earnings as Foundry Hopes Fade; Alphabet Tumbles 12%, Microsoft Edges Lower - 24/7 Wall St.；早安世界》TSIA：今年台灣半導體產值估逾9.1兆元 成長40.9% - 中央社 CNA；TSIA：今年台灣半導體產值估逾9.1兆元 成長40.9% - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.52 | -19.72% | N/A | 92.07 | 114.68 | -19.72% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3037 欣興 | 新聞直接提及 | +0.23 | -4.15% | -1.42% | 963.00 | 1,175.00 | -18.04% | 背離 | 20.41 | 53.83 | 18.65B TWD / 64.67% | 2026-10-01 |
| MSFT 微軟 | 新聞直接提及 | -0.21 | +17.75% | +7.75% | 530.14 | 531.01 | -0.16% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.03 | +1.26% | +0.42% | 2,370.00 | 2,480.00 | -4.44% | 背離 | 86.28 | 27.99 | 511.86B TWD / 54.65% | 2026-10-01 |
| 2303 聯電 | 產業/供應鏈推估 | -0.05 | -7.97% | -9.06% | 110.00 | 164.50 | -33.13% | 同向 | 6.80 | 17.06 | 25.35B TWD / 27.22% | 2026-10-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -3.22% | +6.78% | 213.66 | 228.38 | -6.45% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | +9.75% | N/A | 566.42 | 578.44 | -2.08% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | -3.78% | N/A | 934.27 | 983.23 | -4.98% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：lower。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 3037：新聞直接提及「載板」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor。
- MSFT：新聞直接提及「Microsoft」，共 1 篇新聞命中。 方向判斷命中詞：lower。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Drops 4% Ahead of Earnings as Foundry Hopes Fade; Alphabet Tumbles 12%, Microsoft Edges Lower - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi1gFBVV95cUxQR0ZDMHBOanVZeUtaMDlfLWhTMzJwMzRNRHlSNDBmV2VyQWpSWkxzekJjdHdlYlVyaFMyRVF0RFJJVjFETG5mYmJQaTVzY01rV2lqQ3hLOXIwd3FWdm5ONVpjR0I2aEdrcE81SU12RnliWEoxOTdvbDRtMk1ScGpIb2ZjdUE3MUNkSVFpelRGUmtTMVZSMXM1WWd4RDZwc0lwRGJZYk05VVd6NXBscGtLNFhJZlNMcmt1dXhsOW5EdTgyVzNhQnljcjV2ZHhkMEx0MHN6T01B?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 29 Oct 2026 18:04:00 GMT
- [早安世界》TSIA：今年台灣半導體產值估逾9.1兆元 成長40.9% - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTE12V0JSdm55RWVBUVpvMmJfSUprZFBGcFpJTW41MWRqSWtLXzhuWDk4LXV4ak1xLVNiQXI4S1J5WnFteGZnSDFXOTRiTC1UTG5lVzJXYkFYWEZmVWV4b184?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 29 Oct 2026 23:27:00 GMT
- [TSIA：今年台灣半導體產值估逾9.1兆元 成長40.9% - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1MX0tFT1FFRTEtUFFwR2dQV0luVnk0NzN4WDRrY2NNSXJFUmFEdXFXTjN3RFh1NW9mQzhKZFZZNHplVWZBdkV5NnhTZ0FfckdfOS1teF9TeGNiMXBoRWc?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 29 Oct 2026 07:28:00 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：8檔台股高息ETF今年來含息績效勝大盤 00927漲幅居冠 - MoneyDJ理財網；台股重挫近千點到底怎麼了？分析師曝三大利空衝擊下只能這麼做 - 經濟日報；台股開盤跌228.54點 | 市場焦點 | 證券 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [8檔台股高息ETF今年來含息績效勝大盤 00927漲幅居冠 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMiiwFBVV95cUxNX1AzUlozdEJDSXJhUzROUjYxNlZwS1Z1ZzZkdWRqSlpnVlhWZE82SlJ2NVdDVEhMbzF5bnBQWm5RckxDMG9TYU55YkVpZDZWVkpfSUlmYXA4Q2U1eUs3bE5FTTFRMFpZWFJKSkFxbE9pb0lBMFBKRkxvUnZqaUN1NDl5UVRDdDQxY1gw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 29 Oct 2026 03:55:00 GMT
- [台股重挫近千點到底怎麼了？分析師曝三大利空衝擊下只能這麼做 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1yZ3lyWmxCQWszcFlMZUExeVVoRDV1N2Rjd2ZjZXlKdS1JdTBzeEQ4ZjFNWXgtMmNwNk1iS1FCenVyWjZodm1SVUc1WlBMREgwcDd4ZDlzTFR1Z9IBX0FVX3lxTE9yUEFEeU5LUzQ3TE9QY2RXTU9rQ1AwaENRR3diV1FRQ3Q2OEkxeS1TNHVXYl82eDlDaWloUkVLSUlPTDJSODNrMERELUR5WGIxc2ZLYmc1aFlyVU5yRXdv?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 29 Oct 2026 04:58:19 GMT
- [台股開盤跌228.54點 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxPR1NGTXVKWWdTUGV2ZWlJRFZmTk94Q2JpbTBSYzEtbkl5cVVCeFNac1NhV2pXOTQ4VGtEb3VIVW16VzYwakZ3YzJ1N2pURGEtd1JaYmlzbWkwUjlfVlhxNE9VbGgtRXNzZjBxejlKWE1lM1FPbS1reXNOa1hCQU15Uw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 30 Oct 2026 01:20:30 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：統一證券：台股籌碼面仍有待沉澱- 新聞 - MoneyDJ；《台股盤後》電子權值股領跌收跌667點/失守季線- 新聞 - MoneyDJ；外資匯出再起：AI財報疑慮拖累台股與新台幣同步承壓- 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [統一證券：台股籌碼面仍有待沉澱- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPYmVqcDlVSXFrODJVTS02MmlDTm1JQmtjemVaS05lNG1vRHlwMi1zT1VSaFBkb29Nd1VxUFNyQnlkck1CeEsyeFRDNVVlRV9ldnJxTFBpcGo0a0hiOGgzZENuaU5IRm5XZVVzeTNLbUVIOVd5b0Zwd1ZlY2ZhV0lZZXdicDdjZy1jelpESnFjUjdrdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 30 Oct 2026 00:49:00 GMT
- [《台股盤後》電子權值股領跌收跌667點/失守季線- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQTzNvQ1hiMWd2S1lsY1FWY3RlNmlLZ3FBVFNVMU5nWm9qUDI5VmNBelFUTE9qSlRRM2J0dVMxbnctZURpYnlyVTNHMEQ4Y0puTHdIUHlwa2NYWmQzZXZXcGdXYUlGTmswckhMODJmdmJHNzJVTFNNRmQ3eF8tamtXem1KZG8yZFZzeVl2cDloTmE0Zw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 29 Oct 2026 08:04:00 GMT
- [外資匯出再起：AI財報疑慮拖累台股與新台幣同步承壓- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQbGMyVnRRNVJrdHdzbHVZaDRPN01oWnFkZGllQ21Udm9EQU5IRjV2aTNheEhNYkVUZ2JvczQzWlBNYzc2M0h1ZzNaSGd5ZzlzTU1tRThLOHNCcFNaQzg1b1A2c2E1T28yNG1CdDlfaDVlaVlmeVc1RkRMb2FPSTNQbldDWTFkRFBFLUdaOVZHbWtVZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 30 Oct 2026 00:36:00 GMT

## 新興題材：台達電預期Q4營收

摘要：新興題材：台達電預期Q4營收 相關新聞集中在：〈台股盤前要聞〉台達電預期Q4營收優於Q3、國巨Q4可望淡季不淡 - Yahoo股市；〈台股盤前要聞〉台達電預期Q4營收優於Q3、國巨Q4可望淡季不淡 - 鉅亨網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [〈台股盤前要聞〉台達電預期Q4營收優於Q3、國巨Q4可望淡季不淡 - Yahoo股市](https://news.google.com/rss/articles/CBMi-gJBVV95cUxNTGMydnplQ2RxX2IzUFRzeUZaR3NqUnA4OFdRZTYzVGZZNkRSOEcwb05HVFpQZktVQ040UFE2ajhFemwycjVuSFhXMzlUTVJWNl9TMHpPTmJrTHl6LVVFeHIyd2pCUjZ5NjhkekR3U29VMmZqRGZVTFJSLXlmX2FSU2dLOUZjS3Eta3ZaYUg2NWJsQ3BETGdBdWQ3YS1Tb2RWLVc0b1dZbExXR1h0ZE1IazVuQ0J4Z2oydnQ1cGhCT1V0VEx1UDg1NHNXT1FVQk1hNmQwNUtiVDUtYnoyYlJhQjBvbFM4RlRBNTB4azJzN1dHcjVKdlByNmEwOHNZSUFRdU4yZi1XSTgwSWJWbi0zOEF1dk9aeVNVdlJPNXdmbnlvcm8wUV93WWFiOVFiZG9SaHpLV1lrVXd6c2lYdUxJOXlsaHJOcTNGdk5DLUVVemxPejRhalZRLUg4X05mdnlSTG1aZUsxNHFXQW04MjNQRnQ0SF80THBHMmc?oc=5) - Google News source discovery | Yahoo 奇摩股市 Thu, 29 Oct 2026 21:10:02 GMT
- [〈台股盤前要聞〉台達電預期Q4營收優於Q3、國巨Q4可望淡季不淡 - 鉅亨網](https://news.google.com/rss/articles/CBMiT0FVX3lxTFBHWW16Yk1iV2xET0ZqSnNKMGxhRThOZGc0ZFlhYVZPNlJ4XzkzNDlDRmk2Q0ZCT1ZnSnlEaDJHdEFrOS1veGdFZG50SHc1eGM?oc=5) - Google News source discovery | 鉅亨網 Thu, 29 Oct 2026 21:09:10 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
