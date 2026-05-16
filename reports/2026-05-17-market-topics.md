# 每日股市熱門話題分析 - 2026-05-17

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜正向｜熱度 9｜市場確認 65.00｜同向 1/2
2. **利率與成長股估值**｜負向｜熱度 2｜市場確認 N/A｜同向 0/0
3. **散熱與液冷供應鏈**｜正向｜熱度 2｜市場確認 65.00｜同向 1/2
4. **新興題材：散熱需求**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0
5. **半導體與晶片供應鏈**｜負向｜熱度 10｜市場確認 0.00｜同向 1/5

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.09（樣本 15）
- 5日相關係數：-0.34（樣本 15）
- 同向比例：6/15

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 65.00 | 1/2 | 1 | +13.07% | +4.00% |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | 65.00 | 1/2 | 1 | +13.31% | +9.15% |
| 新興題材：散熱需求 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | 0.00 | 1/5 | 3 | -7.90% | -15.37% |
| AI 伺服器與資料中心 | 15.28 | 3/6 | 2 | -6.57% | -5.43% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：引算力需求 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 相關性偏弱；應提高同向價格確認權重，降低泛 AI、泛半導體等寬標籤推估權重。
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

## 歷史回測摘要

- 回測日期：2026-05-17
- 近5日 3日相關：0.19
- 近5日 5日相關：0.07
- 同向比例：+50.00%
- 權重狀態：未調整

- 方向準確度：+50.00%
- 信心排序準確度：0.19
- 診斷：弱正相關

調整原因：近 5 日有效樣本 8 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：INTC, AMD, MU stocks hit 52-week highs today: What's triggering the rally? - MSN；Forward PE Explained: How to Value AI Stocks Like NVDA, AMD, INTC & MU - Bitget；How far can the Micron and SanDisk rally run? - MSN

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.76 | N/A | N/A | 724.66 | 724.66 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.38 | -3.06% | -9.90% | 1,407.61 | 1,562.34 | -9.90% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.65 | N/A | N/A | 424.10 | 424.10 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.65 | N/A | N/A | 108.77 | 108.77 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.58 | +29.20% | +17.89% | 225.32 | 225.32 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron、DRAM」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs, fuels。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk、SNDK」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [INTC, AMD, MU stocks hit 52-week highs today: What's triggering the rally? - MSN](https://news.google.com/rss/articles/CBMi5AFBVV95cUxQY3pZd0tYdUNGcG1tSnlLYzFoUGVhRkxycG1NV05QUEE1X1dxSF9GdG4zSU1DQ0k1T2EzZHZudXBXeUZmZ2lqWVB0MW0zaC1nSGUxOW83bHpUNmNFZTQyUTVnbGZOTENteEZoeEtnVjI4S1NIMm95aC12OW8ySmhLSzlZaGhrTHhiVVEzTW9pYXg4YUl3QjVsTUt5VV92WHBOOXRxN0t6X2p0bnI4REY3d1I0VWpwMC0ySzktNl9NWlotZ0ZUeWp3TTU4NFJoS1Nock5uemxfTWFGWld2R0JJNG5yNkM?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 16 May 2026 02:43:05 GMT
- [Forward PE Explained: How to Value AI Stocks Like NVDA, AMD, INTC & MU - Bitget](https://news.google.com/rss/articles/CBMiXkFVX3lxTE9MWEVQNWx2UVVsV1pNb19rNUUydVFfVXJiYU1EcG91OGFCZXZqSE5jQ25XWi0tVW9VWmd0eklaMzVRRkM4NHQ4aDd2dFZQV295cWxoc1Y2MTE0dXJEQVE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 15 May 2026 10:11:13 GMT
- [How far can the Micron and SanDisk rally run? - MSN](https://news.google.com/rss/articles/CBMimgFBVV95cUxOejBnM2dOaFVNSmZHSFhFUHRXNXJsRFlVZzI4ZWN1OWxIMEM4UlB2Q3phSGJ0OFBEZG9zcFBPUWdHeXVLRW5UZnphSlVRdmZVWEhVVlNaVi1ZMFU0RE5Wd2FZSWZ4MXlvelJYX1BMaW8wdXpkTE5KQWhXbGFxQmVuRmQ2Vm44UjRmS2pUZ0F5TlRqR3VCcWJJem1n?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 16 May 2026 10:40:30 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：Global shares stumble while bond yields climb on inflation worries - Reuters；Wall Street ends lower on mounting inflation worries - Reuters

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | -14.25% | -8.35% | 421.92 | 506.69 | -16.73% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Global shares stumble while bond yields climb on inflation worries - Reuters](https://news.google.com/rss/articles/CBMigwFBVV95cUxNdXdkc1k2VjFGcUx2RHhvb1BKVW9HNmp3ZnNyTmxQTElPSVY0OERvUThQNVRab0luYVdLbTFkREU1MkZfZVNld3BMNkdwV2RPcWgwTFVrQ0ZCZFRhY2pweVhGUmpOdlotOU96OUhndzdLQWpPdjNNVWdma2NZdzJNYVkwRQ?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 15 May 2026 02:12:00 GMT
- [Wall Street ends lower on mounting inflation worries - Reuters](https://news.google.com/rss/articles/CBMi1gFBVV95cUxQWjZBNTNiNzEwUUZ4SU40ZzNPX0FWWGhydkJtR3M2aEljYjVWZUN2NjRIRG5vQ2UtNUNlSGNlMUFacmlzQXZfaHN2MkJLTHY0ZXZMcVItZXo3Z3dubE9aenZXYjl6V0loS2lTZVVmUUtfeXpZcng5Tkw0bS03TmJ0d3RIOGV3ZnF3NmxTNU5SY0YwTlN2U2M5c3RmRFNtUkRZYTZxZjZURWFYWGVKNk9UZXdNdVNFOXp3MmQ2VjBCRThSaXZlNEtQc3hxN1NrSUZMRTBzc1NB?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 15 May 2026 22:24:13 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：單季就賺破2股本！「散熱大廠」Q1獲利強漲146.3%創高 輝達Rubin展開出貨業績續揚 - Yahoo股市；AI 散熱需求爆發，大摩升奇鋐目標價看 3,333 元 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.34 | -2.58% | +0.41% | 2,455.00 | 2,835.00 | -13.40% | 背離 | 61.06 | 40.34 | 15.63B TWD / 71.62% | 2026-05-01 |
| NVDA 輝達 | 新聞直接提及 | +0.56 | +29.20% | +17.89% | 225.32 | 225.32 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱、奇鋐」，共 2 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：創高。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：創高。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [單季就賺破2股本！「散熱大廠」Q1獲利強漲146.3%創高 輝達Rubin展開出貨業績續揚 - Yahoo股市](https://news.google.com/rss/articles/CBMitgJBVV95cUxPOV9JNHBtLTZFb1l0QmswcF9SYUY1QjNwV2J2Q2NiZjdRZmpTa2k4R05vZnIwcVk2SUF6OGNqQVpid3I2TjNrVE84OENZX0I5NVZtWjNnVm1rMTFUa1k2Z0JXVW00aVhUUFpVNnM3ZmpEcF9tUmJKSkdqc1NBY0VKbjAtZktOcnFFNW1Lcm1PQUZBNEg5cWFKY1YtRjdBVnRhSHh3VkpNRDFMXzRZdmVGVWwtVGF6RjNDQ0VPV25fd1Q5cEtYLWItVElMVThRTTdqeUNqOEJJX0s3WUU1NWxMOV90a3F5QjZlNk1XSnN5eUV1aUdnbXVtdDFqbkRoTVprMmJUYU5Hbkxhc3c1WUhWZ2tzdlhiUEtXNmxzcVM4SjVZNE5IYldxZkh1S1N4LUQwT3pWd3Z3?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 15 May 2026 00:35:25 GMT
- [AI 散熱需求爆發，大摩升奇鋐目標價看 3,333 元 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiXEFVX3lxTE4zdXlnbkJTczV2ZlFsWXJTZEVHSGQyZU1hVGZ0b2duSTR0Mm9uVnEzc084SVIwblM3OGZxRzFmbDJIdmF3eFB3bEItWkNOeWNHUFZQMFpfQU9ZREdr?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 15 May 2026 05:15:49 GMT

## 新興題材：散熱需求

摘要：新興題材：散熱需求 相關新聞集中在：AI 散熱需求爆發，大摩升奇鋐目標價看 3,333 元 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | -2.58% | +0.41% | 2,455.00 | 2,835.00 | -13.40% | 不適用 | 61.06 | 40.34 | 15.63B TWD / 71.62% | 2026-05-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐」，共 1 篇新聞命中。

### 主要來源

- [AI 散熱需求爆發，大摩升奇鋐目標價看 3,333 元 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiXEFVX3lxTE4zdXlnbkJTczV2ZlFsWXJTZEVHSGQyZU1hVGZ0b2duSTR0Mm9uVnEzc084SVIwblM3OGZxRzFmbDJIdmF3eFB3bEItWkNOeWNHUFZQMFpfQU9ZREdr?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 15 May 2026 05:15:49 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel (INTC) Stock Falls as UBS Warns of AI Chip Bubble - MEXC；Forget Intel. Its Own Executives Are Cashing Out and This Is the Chip Stock You Should Own Instead - 24/7 Wall St.；Intel Climbs 15% on Apple Chip Deal as Trader Warns on Upcoming Cisco Earnings - 24/7 Wall St.

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.76 | N/A | N/A | 108.77 | 108.77 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 新聞直接提及 | -0.28 | +7.67% | +49.48% | 300.23 | 300.23 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.06 | +0.44% | -1.09% | 2,265.00 | 2,265.00 | 0.00% | 未明確 | 74.39 | 30.45 | 410.73B TWD / 17.50% | 2026-05-01 |
| 2303 聯電 | 產業/供應鏈推估 | -0.04 | +5.26% | +20.48% | 110.00 | 110.00 | 0.00% | 背離 | 4.00 | 27.64 | 22.66B TWD / 10.80% | 2026-05-01 |
| NVDA 輝達 | 產業/供應鏈推估 | -0.03 | +29.20% | +17.89% | 225.32 | 225.32 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | -0.06 | N/A | N/A | 424.10 | 424.10 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | -0.06 | N/A | N/A | 724.66 | 724.66 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | -0.06 | -3.06% | -9.90% | 1,407.61 | 1,562.34 | -9.90% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC、Intel」，共 3 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AAPL：新聞直接提及「Apple」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 3 篇新聞出現相關標籤。 方向判斷命中詞：falls。

### 主要來源

- [Intel (INTC) Stock Falls as UBS Warns of AI Chip Bubble - MEXC](https://news.google.com/rss/articles/CBMiUEFVX3lxTE1VOVpGOGZaRnd0Nzl0WVV0UjdFRjlSSURXemN1bUhVVmIwRUxOaUNwWlJ0MEYwUm1tX2VSSFp0TXBwb2QzcnVjM3JtTDBzTmdm?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 15 May 2026 20:53:38 GMT
- [Forget Intel. Its Own Executives Are Cashing Out and This Is the Chip Stock You Should Own Instead - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi2AFBVV95cUxPUzUtMTQ2bGVYTXc4TzN1bGNpa3ZJem5mVl9YYjFNZGUwLTFoZFBkY1VyTk9jZGRoYW1YUFhBM0ZGRGJ4YWwzeElrVGlRV2lmMWpHN05sdkpCWlc0QzZoZjVDMUtnQU5JRWRaX2o2c0NlcFZpaDhpbVB0eEdIb2NLVkNVbGVZQkZwWVo4NTIyQTRiSXZuc2xHWEJobzF5TTBDaWFlc2gzV3NiZm40bzQwaG1QTFBkY2llZkdVeU5iN09Yb1lJWTl2bFZWMzU4anhxd3BUUTBOQk4?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 15 May 2026 12:51:33 GMT
- [Intel Climbs 15% on Apple Chip Deal as Trader Warns on Upcoming Cisco Earnings - 24/7 Wall St.](https://news.google.com/rss/articles/CBMivgFBVV95cUxOaTZPTHdDbWVDb2FLblZ1aWZIWV92eWROcERuUWRlZ2JrWTZIQWE0TXhaWHNPNFZzMEpmNk91NmNxVFczeF9JSllObUlpX2lLTkdrczJzN0ZMaWl5bmExbVY1OC1PMkF2WEhtcEZCc0dwSVpLNU1ZcUtVSW9HTGJubGdaY3QyNGV3UTRUTFZhMzRXVWQ2SWNYY20yRWhOUlpHbHhYRzhMUE1lQV9WTmNGNXo0djl2S19HOGxqSlZn?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 15 May 2026 16:41:10 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel (INTC) Stock Falls as UBS Warns of AI Chip Bubble - MEXC；比核電廠更惹人厭！美國逾七成民眾拒絕 AI 資料中心進駐後院 - TechNews 科技新報；中國轉向華為，本土 AI 晶片能否填補？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.72 | N/A | N/A | 108.77 | 108.77 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | -0.05 | +29.20% | +17.89% | 225.32 | 225.32 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | -0.09 | N/A | N/A | 424.10 | 424.10 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.07 | +0.44% | -1.09% | 2,265.00 | 2,265.00 | 0.00% | 未明確 | 74.39 | 30.45 | 410.73B TWD / 17.50% | 2026-05-01 |
| MSFT 微軟 | 產業/供應鏈推估 | -0.07 | -14.25% | -8.35% | 421.92 | 506.69 | -16.73% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | +37.38% | +28.34% | 425.19 | 425.19 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.07 | -1.44% | +6.01% | 547.00 | 547.00 | 0.00% | 同向 | 10.86 | 50.79 | 62.25B TWD / 19.22% | 2026-05-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.07 | -11.89% | -10.19% | 3,260.00 | 3,260.00 | 0.00% | 同向 | 62.91 | 51.95 | 46.74B TWD / -4.14% | 2026-05-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel (INTC) Stock Falls as UBS Warns of AI Chip Bubble - MEXC](https://news.google.com/rss/articles/CBMiUEFVX3lxTE1VOVpGOGZaRnd0Nzl0WVV0UjdFRjlSSURXemN1bUhVVmIwRUxOaUNwWlJ0MEYwUm1tX2VSSFp0TXBwb2QzcnVjM3JtTDBzTmdm?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 15 May 2026 20:53:38 GMT
- [比核電廠更惹人厭！美國逾七成民眾拒絕 AI 資料中心進駐後院 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9FTEJ4WWJDbGZNeXRUT052d0ZMQ2ZZUm84Vm1iWVNEUlk3YzRneTcxZUU1b1FfS2ZpQk1tbFpjMmNWcGtsWXk4MndTRUJrdUpXeHcxejBfMlQxQQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 15 May 2026 04:48:37 GMT
- [中國轉向華為，本土 AI 晶片能否填補？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiigFBVV95cUxPVnh0bklQT1dXVFhWcXJDc2RxVGRuOFIzeGI5R2FwN2FwTm51UEZVZlh3ajRHYW9YekhqeUJCcDR5dDI2V2ZwX290VmllbDl4MmFJQnF1RUJ6NC1RY0h5cDNJcEZMaDBPaGc3Y3pfcGVCaWtGeGx2blVaMWhpUUQyWEg2M0dscXl1cnc?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 16 May 2026 19:39:56 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股焦點：雷科(6207.TW) - MoneyDJ理財網；法人專欄分析-台股 - MoneyDJ理財網；法人專欄分析-台股 - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股焦點：雷科(6207.TW) - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikgFBVV95cUxNeGxwbHRueVd4a0pKMVh0VnpiOWpPQzE1Q0UtVnVpX0tTblFsNERiZk0zc25IZlVsNDZoNXlzRVZKV213clhLVkdpQk9oUHBfZHA5WGNORTFnUlVhLWZXVVZSV0R1ZWh5VWVKZ052U1VnZWh1c3dLMUhPUFczd09GYmI3RzZQcWs3VmlLNzFCS1BGdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 15 May 2026 01:12:00 GMT
- [法人專欄分析-台股 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMif0FVX3lxTE9DcnlCZ1duOFlzVHpyNzNfYUl1TU82V01pTkgxUWxaTEFnM2pJYW9Cb1dGbXpvUXNsNHptc0FHRXlSWk52dWlFajJVblVkOHh5aEhYSDRZYUNfWXZTZlNiSHpybGRvVGlpNTdFcDJObFFaUHctMmFBX1J5UmZyVGc?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 16 May 2026 09:52:04 GMT
- [法人專欄分析-台股 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMieEFVX3lxTFA4am9rejhMbmZEa1ptNTF2UkUtSl9mNDFEdWJCTjlrSGlRS29jX0E3WFlzOXQ0cnNsMUhWRmVNM19yQldaWEhGNC1qNVFNemdjQWl4cnN1aUlFU29rQ09vMUdja050NzVzZmZLOVl2ZENWLUpHOV91MA?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 16 May 2026 11:40:10 GMT

## 新興題材：引算力需求

摘要：新興題材：引算力需求 相關新聞集中在：台股創高回吐失守雙線！下半年 AI 引算力需求 台廠出貨潮可期 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股創高回吐失守雙線！下半年 AI 引算力需求 台廠出貨潮可期 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9ydV9tNFhjQjluNHBGTVlfZVkxbnZEZ0tGZlM0ckNiaElDWUM5S0ZjdVJ0N1dwcm8wb3hJNk9qYVJBLXBPck1aZ00yWWdOTFpEU0d3VVZyQVFJUdIBX0FVX3lxTE9ncVF2enhOU3JEU3RXQTBLMmRfTnlXSHRpcXB5WEpMaFdSQWlKamEzY08tZTVhbEtndUNfTXhpeUU4RUg5NndybEM0al9HNXp3RjdVelJqWXVlZ2pOOEM0?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 16 May 2026 07:47:45 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
