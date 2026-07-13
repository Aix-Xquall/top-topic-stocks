# 每日股市熱門話題分析 - 2026-07-14

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜負向｜熱度 14｜市場確認 53.35｜同向 2/3
2. **新興題材：台積電6月營收**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
3. **半導體與晶片供應鏈**｜正向｜熱度 11｜市場確認 0.00｜同向 0/5
4. **AI 伺服器與資料中心**｜中性｜熱度 10｜市場確認 1.54｜同向 1/6
5. **綜合市場情緒**｜負向｜熱度 42｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.10（樣本 14）
- 5日相關係數：-0.07（樣本 14）
- 同向比例：3/14

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 53.35 | 2/3 | 0 | +2.23% | -4.15% |
| 新興題材：台積電6月營收 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | 0.00 | 0/5 | 3 | -4.34% | +5.31% |
| AI 伺服器與資料中心 | 1.54 | 1/6 | 3 | -3.38% | +1.20% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：SpaceX | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：還有就看營收 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 相關性偏弱；應提高同向價格確認權重，降低泛 AI、泛半導體等寬標籤推估權重。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
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
| 2026-07-11 | 0.13 | -0.08 | +50.00% | 12 |
| 2026-07-12 | 0.27 | 0.13 | +16.67% | 12 |
| 2026-07-13 | 0.39 | -0.09 | +15.38% | 13 |
| 2026-07-14 | 0.10 | -0.07 | +21.43% | 14 |

## 歷史回測摘要

- 回測日期：2026-07-14
- 近5日 3日相關：0.52
- 近5日 5日相關：0.32
- 同向比例：+33.33%
- 權重狀態：未調整

- 方向準確度：+33.33%
- 信心排序準確度：0.52
- 診斷：正相關

調整原因：近 5 日有效樣本 6 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：產業評析-複製記憶體超級大循環 矽晶圓股漲聲起 - MoneyDJ；Intel, AMD, and Applied Materials Drop 4% as SK Hynix Rout and Oil Spike Hit Chip Stocks - 24/7 Wall St.；MU, INTC, SNDK: Chip Stocks Rally After-Hours On AMD’s Blowout Report - Stocktwits

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | -0.50 | N/A | N/A | 937.00 | 979.30 | -4.32% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.50 | -3.08% | -4.04% | 1,673.97 | 2,335.00 | -28.31% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.49 | N/A | N/A | 534.39 | 557.89 | -4.21% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.43 | N/A | N/A | 103.12 | 114.68 | -10.08% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | -0.38 | -3.60% | +16.70% | 203.53 | 211.14 | -3.60% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | -0.28 | 0.00% | -0.20% | 2,440.00 | 2,440.00 | 0.00% | 未明確 | 74.39 | 32.80 | 442.68B TWD / 67.87% | 2026-07-01 |

關聯理由（前 3）：
- MU：新聞直接提及「MU、memory、Micron」，共 4 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：fall, weak, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK、SanDisk」，共 2 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：fall, weak, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 3 篇新聞命中。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [產業評析-複製記憶體超級大循環 矽晶圓股漲聲起 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxOWV8xbWVMWTZuSTVmb3VnYmtDdndUSzlyRUJhVlFoNWtpMm9QX3lrZlRGNVRZTzhSRUtkbUJaSEZRWWthYjdSZjVZZXpycDUtYWJxWGJvLWtVTWRaV3R6ZFRpMGtuTkxhMmhOdWlYczFodVZCZDlyZ0RKSi0tX1cwTE03NVJibnBsdjVwS1F2Qlc?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 13 Jul 2026 16:03:06 GMT
- [Intel, AMD, and Applied Materials Drop 4% as SK Hynix Rout and Oil Spike Hit Chip Stocks - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiyAFBVV95cUxPVUNTQ043RnZkVTV6SnVvcEt3QkhMYWJONkRrWUVUQnBOV0dsVFRkRWtxR1U3Vk9lU1Q3aDI0R1RjMDhubEVtRTlUUmxfUXJZUi1mU1BWLUxKUnhsZWpkV3NtNGlGQkdKVzlYNGJjMFFYS2tmNEJEY210NkJMVlRhUklzN2NqaWMxWEdsYW1kT2J1OHdJRmNoLWR5Z3JPVEc1QThmbm95RWpNdThUeS1oVGxhZG1VeFhLTHhYb2FJOFBvWERxcVhmRQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 13 Jul 2026 14:22:17 GMT
- [MU, INTC, SNDK: Chip Stocks Rally After-Hours On AMD’s Blowout Report - Stocktwits](https://news.google.com/rss/articles/CBMiygFBVV95cUxPeVlYaXJjQjNtTkNRQUxQTHhaLUFMbE80Uy1MeDBpV0FPdkg2SHRLdkdfVUpXM1NrNWhZSVZQQ01sa0o4T1hKdzF1clBFRlRWUmMwWGxQTDNVVFBpOVhObUc2MXpBeXBOZ0p3R0w5NGRNOHB4X0ZIXzhlT0NMbmhzc1RtdmJRTWhlRUhKSHpyVnpaU0VGMlJyU2tDcmdkTG1hWVJJbmtTVDREbzFfWDB4bjhuTGswN3lmdkdHQzY1dzFOVU41VGlBNlZn?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 13 Jul 2026 13:38:01 GMT

## 新興題材：台積電6月營收

摘要：新興題材：台積電6月營收 相關新聞集中在：台積電6月營收出爐！ 「年月雙增」創歷史新高 - Yahoo股市；台積電6月營收4426億元創新高 Q2逼近財測高標 - news.cnyes.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | 0.00 | 0.00% | -0.20% | 2,440.00 | 2,440.00 | 0.00% | 不適用 | 74.39 | 32.80 | 442.68B TWD / 67.87% | 2026-07-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 2 篇新聞命中。

### 主要來源

- [台積電6月營收出爐！ 「年月雙增」創歷史新高 - Yahoo股市](https://news.google.com/rss/articles/CBMiqwJBVV95cUxNRC14S0gwYlg5ZHBCSDFMSmU2QmF1QU9GZzZXUENSOVFvVnNoekZjVl82TjlvZ0VJNUxvbDhVMUZOSmgtb1plMHJLUDE2b01fRGlTYnZzcV9fZTRYcEJoX3dwQ1J3UF9ETHA1OFFmME5aczgzNjlWeFdtbzYza2NKRUxlN0xZLTZ5WWJPVmhpY1RHOWdSUmkyYndzTG0tSUhJNFlqeUhlMnl3YUI4ZC1CaGppUkZ5MlJhTnIzZkFxVUZXUjQ1b1RCWGZRMkZlNEktcTFxODFPdVZxbE96TWFLMkVWV0FwOW84Yy15bk1MTVZHcGdzdUZsQkQ2dEZRdlctc2FnaXAzbTFuNVpWMHJlSjh4Wm5jN3ZTaGRoeng5bjNoRGV2anV0QkNLZw?oc=5) - Google News source discovery | Yahoo 奇摩股市 Mon, 13 Jul 2026 06:30:50 GMT
- [台積電6月營收4426億元創新高 Q2逼近財測高標 - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTE9CbEo5Tld3MGRWd3E2SUhnaTZueUU0WF80NG9sR3dqand6NElid3R5R3ExQl9DSjJaNEdRekRsdmstOG9jM1pkRVUzLVhSRzQ?oc=5) - Google News source discovery | 鉅亨網 Mon, 13 Jul 2026 05:48:16 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：TSMC vs. Intel: Which AI Chip Manufacturing Stock Has More Upside Now? - The Globe and Mail；Intel (INTC) Raises Server Chip Prices As AI Demand Pushes Supply Limits - Yahoo Finance；Intel, AMD tumble as chip sell-off deepens: what if US-Iran conflict drags on? - Invezz

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.59 | N/A | N/A | 103.12 | 114.68 | -10.08% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | +0.38 | 0.00% | -0.20% | 2,440.00 | 2,440.00 | 0.00% | 未明確 | 74.39 | 32.80 | 442.68B TWD / 67.87% | 2026-07-01 |
| AMD 超微 | 新聞直接提及 | +0.50 | N/A | N/A | 534.39 | 557.89 | -4.21% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2303 聯電 | 產業/供應鏈推估 | +0.04 | -0.97% | -9.97% | 153.50 | 164.50 | -6.69% | 未明確 | 4.00 | 38.57 | 23.12B TWD / 22.85% | 2026-07-01 |
| NVDA 輝達 | 產業/供應鏈推估 | +0.02 | -3.60% | +16.70% | 203.53 | 211.14 | -3.60% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | +0.04 | N/A | N/A | 937.00 | 979.30 | -4.32% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.02 | -3.08% | -4.04% | 1,673.97 | 2,335.00 | -28.31% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -14.04% | +24.08% | 384.05 | 446.77 | -14.04% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel、INTC」，共 3 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「TSMC」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip, foundry。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [TSMC vs. Intel: Which AI Chip Manufacturing Stock Has More Upside Now? - The Globe and Mail](https://news.google.com/rss/articles/CBMi5gFBVV95cUxNMFJlbzl5WDNwYU82dy1UdE1IU2U4RTN3YXJDZmx6OUZZbWpVMDhNMFpJWU5aYVEtdHpZQWdXX09oY2RDU3JZNkctSmhKVVgza0RTVXBWV0R4cXRXUGt6SndKQTZhQUJrelRwSVhkZFB5YlF6X3NucEZIblNYM2JicEdiX2IxNDdwQ2hseTRjdHpzUGVUbVdtTVJKYUZhem5pUk9BNlJ5bmp1aHNHRzU5bGVaLVRvSDl0NklEampSaXk3YUFTRnI5d0tQVHk4Q3JacEpGYXp4R2JWaUI0OGlqbmdrMWRBQQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 13 Jul 2026 13:52:56 GMT
- [Intel (INTC) Raises Server Chip Prices As AI Demand Pushes Supply Limits - Yahoo Finance](https://news.google.com/rss/articles/CBMimAFBVV95cUxNWUhrbV9RZWlYZy14V1hNbk53bjNYZ3lNYk8wWnVJUmNHZUdCUnoybFlLSzZNMTVXTEFKeDlReGJqYm54QUY1VWQxSlZLeFRpdUs5dEJfZVRka2E1SllZcXRZVDY0aEtBMllmR1BDY1Jaa1g3UWQxeC0yRGh0R0xRWDZQcUtBdi04TXZEN3BaV0Q3dUZiQm8xRg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 12 Jul 2026 04:15:00 GMT
- [Intel, AMD tumble as chip sell-off deepens: what if US-Iran conflict drags on? - Invezz](https://news.google.com/rss/articles/CBMipwFBVV95cUxPZE8zSDhQMlJ2eHdSSnIzdEJ4dnAtcW1STkZCY3dScHo3eHQ2WVBpSFFLd20zQ0FSWFhCdkt1ckwzSFh0WFBTdzhEeXdCLXdYUkczT0lhNzFIbjNQTXR5SkNCNzVoc1Z5VjRZMWExUm1ZX0FkYjRhTUNZT3UtMk56ZldzNDA0NVNOckxRZjNUeEYzbmkwS21Zd25RYzU0RUJUaXBPQTBycw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 13 Jul 2026 15:25:12 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：TSMC vs. Intel: Which AI Chip Manufacturing Stock Has More Upside Now? - The Globe and Mail；Intel (INTC) Raises Server Chip Prices As AI Demand Pushes Supply Limits - Yahoo Finance；AI 代理如何優化諾基亞電信工作流程？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.59 | N/A | N/A | 103.12 | 114.68 | -10.08% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | +0.41 | 0.00% | -0.20% | 2,440.00 | 2,440.00 | 0.00% | 未明確 | 74.39 | 32.80 | 442.68B TWD / 67.87% | 2026-07-01 |
| NVDA 輝達 | 產業/供應鏈推估 | +0.03 | -3.60% | +16.70% | 203.53 | 211.14 | -3.60% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.06 | N/A | N/A | 534.39 | 557.89 | -4.21% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 產業/供應鏈推估 | +0.03 | -0.45% | -22.83% | 390.99 | 506.69 | -22.83% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -14.04% | +24.08% | 384.05 | 446.77 | -14.04% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.04 | +2.92% | -1.76% | 670.00 | 680.00 | -1.47% | 同向 | 10.86 | 62.21 | 65.78B TWD / 32.86% | 2026-07-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.02 | -5.09% | -8.82% | 3,825.00 | 4,310.00 | -11.25% | 背離 | 62.91 | 60.96 | 58.01B TWD / 2.80% | 2026-07-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel、INTC」，共 2 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「TSMC」，共 1 篇新聞命中。 同時符合主題標籤：AI, advanced packaging, CoWoS, AI server。 方向判斷命中詞：rally。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [TSMC vs. Intel: Which AI Chip Manufacturing Stock Has More Upside Now? - The Globe and Mail](https://news.google.com/rss/articles/CBMi5gFBVV95cUxNMFJlbzl5WDNwYU82dy1UdE1IU2U4RTN3YXJDZmx6OUZZbWpVMDhNMFpJWU5aYVEtdHpZQWdXX09oY2RDU3JZNkctSmhKVVgza0RTVXBWV0R4cXRXUGt6SndKQTZhQUJrelRwSVhkZFB5YlF6X3NucEZIblNYM2JicEdiX2IxNDdwQ2hseTRjdHpzUGVUbVdtTVJKYUZhem5pUk9BNlJ5bmp1aHNHRzU5bGVaLVRvSDl0NklEampSaXk3YUFTRnI5d0tQVHk4Q3JacEpGYXp4R2JWaUI0OGlqbmdrMWRBQQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 13 Jul 2026 13:52:56 GMT
- [Intel (INTC) Raises Server Chip Prices As AI Demand Pushes Supply Limits - Yahoo Finance](https://news.google.com/rss/articles/CBMimAFBVV95cUxNWUhrbV9RZWlYZy14V1hNbk53bjNYZ3lNYk8wWnVJUmNHZUdCUnoybFlLSzZNMTVXTEFKeDlReGJqYm54QUY1VWQxSlZLeFRpdUs5dEJfZVRka2E1SllZcXRZVDY0aEtBMllmR1BDY1Jaa1g3UWQxeC0yRGh0R0xRWDZQcUtBdi04TXZEN3BaV0Q3dUZiQm8xRg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 12 Jul 2026 04:15:00 GMT
- [AI 代理如何優化諾基亞電信工作流程？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMikgFBVV95cUxPSTQ2NENVekk2dU5WblRWX2ZiaUZvN3NUQ0xZQUhZeEEwMUI4UFVfX1IyV2RHVGppSUllZFFDRlRvSWFyT3pmNGJhdXlLNkxHTEhmN0lUUlRkZ3BZakNKMmRobzMzck0wOFUzM25SdGZPQkw1WjVkbUtuS1RpcS1HSHd4MlF0MVZMYl9FdUZTb2QtUQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 13 Jul 2026 19:58:57 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股火熱助燃成長動能 法人看好元大金全年獲利飛越700億 - 經濟日報；台股 ETF 受益人 連三周創高 | 基金天地 | 理財 - 經濟日報；台股上週跌1426點 上市股票總市值減少4.62兆元 | 市場焦點 | 證券 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股火熱助燃成長動能 法人看好元大金全年獲利飛越700億 - 經濟日報](https://news.google.com/rss/articles/CBMie0FVX3lxTFBlMUoydzZ5QUZtdk5vMGhIZDBEZXF6amZsZjdRd2VfeVhGSzk3ZGlfd1hkdHJGZ2JrVS00UzhHdjVtOHRxTmVtejlOMmsyc3BVZkFWcy1kTXk5QzVaUlFOZ0VRajN2X2ZTR3pHVFBuQkdiNWFaQUR2aktrc9IBX0FVX3lxTFA4RVZTclVySFRmQjljMDhXdXVSNHhTaW5sT2JrWFdoOEF5MlJQWXk4ZUF5Y1lCR1ZYZ1Q4LVV0ajB4TzZScXJFc0drbHBQM0lUN3VTWFdqc0w2VGJiN0Jn?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 13 Jul 2026 13:03:13 GMT
- [台股 ETF 受益人 連三周創高 | 基金天地 | 理財 - 經濟日報](https://news.google.com/rss/articles/CBMifkFVX3lxTFBRUVdRc212UXpyV3o2THVzZDRiZ0Q1ckN3WEpPOEtWMGpwbEliUkdnei1DRW9KclIydVlhZER6OXQtTHVxemplWTZEWEV2M0tDclo3NkJqcGpBV2MxN1BYaXNIc0hhXzJHRUIxNGZTQUc3VDJjbVdlSVFlZmxKUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 13 Jul 2026 15:22:49 GMT
- [台股上週跌1426點 上市股票總市值減少4.62兆元 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMie0FVX3lxTE1raTQwQ3Q3WGJ4WGJmRFo4dFNyMVhDOU52VXpXNURJT1JUU0hCMkhRb1RtWFFaWGhUa0ZURFUyMVl3b0hKcEs5S0NTMWU4S2I4UmZjNUpzMkZrdVBoZTBERlZaejN1c01rbFB5SFk1YllDQjhVS2dWRXRHZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 13 Jul 2026 10:45:40 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》震盪逾千點、收漲25點，日K連二黑-新聞內容-基金 - MoneyDJ；統一證券：台股技術面仍趨於震盪- 新聞 - MoneyDJ；國票證券：台股短線應會採防守優先的格局- 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》震盪逾千點、收漲25點，日K連二黑-新聞內容-基金 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxNbW5lR3hMNWtCZGZqZ0xYN1RkY0JGZ2pCdUp5TGZMbXlhT0dwWTFkalNEb1JSbXJmOVUzanZJMjdqZURISk5XbE1CaWFzdkM5d1kxdnZrVGpZYW1jdVpnY2RwTC13eTJjYW1zMEU1U0lBOUFrYzR5UkxEWGNVMEZRN0xlWmVKSjJxOFp6VEhBTHM?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 13 Jul 2026 08:05:00 GMT
- [統一證券：台股技術面仍趨於震盪- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNUEU4LWp5UlZDbTRrUnF1Q3VCY2hrSG1wcGxGSXBMVG13QmZYQkgxUEI1N2kxSEtBRFlfOGl1SVNHZFkyb05rVmVldm9JQ0czVTRHLVpEblBjRU9CNFRsY3dzeHlIbGdNTlBuSWpaalEzR25oMFJ6VVI2MW5xOGpabjdJZDJqOXBVdXBOd3ZVM2hpUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 13 Jul 2026 00:43:00 GMT
- [國票證券：台股短線應會採防守優先的格局- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPZDVCYjEwT1dvd1l1XzQ3bUd6RnpDWGZ5SHhOSXdheTQwVkYyNTg4cmJVdWdxM2ZyNHlTOEgxY1pjcTRHb2p5aVk2a29LSjg3dUs0ZnlRdjNYUWFPUGN3VFZJMTVuRkRGcDk2OTVYQVlBTXBGZGY1U1BoM1lVUnNnSzlSZlJ3VlE3bHpORGk1bExJQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 13 Jul 2026 00:43:00 GMT

## 新興題材：SpaceX

摘要：新興題材：SpaceX 相關新聞集中在：Big banks poised to report booming revenue propelled by SpaceX IPO, Iran war volatility - CNBC；Stocks making the biggest moves midday: Nio, Braiin, AppLovin, SpaceX, SK Hynix & more - CNBC

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [Big banks poised to report booming revenue propelled by SpaceX IPO, Iran war volatility - CNBC](https://news.google.com/rss/articles/CBMimwFBVV95cUxOODgyV1JDSDU5WS1UOVM0WVItaGRva0FmQWZUOGRKdENDdXBDUm84UmtQV013RUUwbGl5ZEJaZWxjalpIOWxYR0h1NGlYZ2liUnA3aUF5VG9mOGNRZS1LOUxOTGhCRHBKNUVaQUdSRE1VYUxpTU9oME9OSktvMzROc3hLN1kwclNoeGxjQ0k4ZllNb1R3c2cxbG1ISdIBoAFBVV95cUxQM1QyVU5DRUpDQzMxUXpoanE4RzA5VC02bmlxSWhmNGt3Z3N6NnJlbm5UQ2UwWnFmZ1piQnQ5Zmlsei1EV0dwUmN3MFNLbmVqN09PV0N0dTJXSTNBN1l4bWRyWDRkSXBYTzFGQWpraDJBakl5OVpXTHQxdW5OajZ2TUNxRlJsUVNvdnJCb2RLUlk1bEJjQUQwMk03S2tNcmJm?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 13 Jul 2026 12:00:40 GMT
- [Stocks making the biggest moves midday: Nio, Braiin, AppLovin, SpaceX, SK Hynix & more - CNBC](https://news.google.com/rss/articles/CBMinwFBVV95cUxOZDQ0NERIMGhETWplNDF3by1zTWozc0NwSFRrRzljaVQ2WjJWdG5lalVYVWFPLW1KMWtaWWItdkVwSFhEWF9kNkNNUzkzeU14clluNnJMck9pRThlVFk2SWJwWVJycUtmelNZZXEwRTluNzJrVGxxaEdpbUFZLTRXUTlyd0Ita19XZGttQzdtQ0x0dU52TmtURmp2SWFRTk0?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 13 Jul 2026 16:21:26 GMT

## 新興題材：還有就看營收

摘要：新興題材：還有就看營收 相關新聞集中在：產業評析-下半年行情3大特色－資減股落底、巨額資本支出 還有就看營收了 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [產業評析-下半年行情3大特色－資減股落底、巨額資本支出 還有就看營收了 - MoneyDJ](https://news.google.com/rss/articles/CBMilgFBVV95cUxOdkN0ZTU1Q0pUODJxQzBwbldCMkxfZmdXWURaRzZZZ0tteVVZTzl3dDlfU1JnNXk3RThvNnBQQmxDVjVZYk5tWWt0Z3BIQjU5T2lLZUhvU2cxLWNOZm92N05vWVJWQmJfNFJSTmI1NGhEZGYwdXFXMk1fMFZSRnVMRVU5NkJSaE5acU1hNzBwMHZJbzV1d0E?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 13 Jul 2026 16:03:06 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
