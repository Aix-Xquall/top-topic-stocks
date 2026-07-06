# 每日股市熱門話題分析 - 2026-07-07

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **AI 伺服器與資料中心**｜中性｜熱度 10｜市場確認 N/A｜同向 0/0
2. **半導體與晶片供應鏈**｜中性｜熱度 8｜市場確認 N/A｜同向 0/0
3. **消費電子與手機**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
4. **記憶體與 HBM 供應鏈**｜正向｜熱度 9｜市場確認 0.00｜同向 0/1
5. **綜合市場情緒**｜中性｜熱度 39｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：N/A（樣本 1）
- 5日相關係數：N/A（樣本 1）
- 同向比例：0/1

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| AI 伺服器與資料中心 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 消費電子與手機 | N/A | 0/0 | 0 | N/A | N/A |
| 記憶體與 HBM 供應鏈 | 0.00 | 0/1 | 1 | -23.28% | -16.56% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：B836 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：台股超級法說 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-06-24 | -0.38 | -0.11 | +25.00% | 12 |
| 2026-06-25 | 0.10 | -0.21 | +20.00% | 5 |
| 2026-06-26 | 0.08 | 0.04 | +25.00% | 16 |
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

## 歷史回測摘要

- 回測日期：2026-07-07
- 近5日 3日相關：N/A
- 近5日 5日相關：N/A
- 同向比例：N/A
- 權重狀態：未調整

- 方向準確度：N/A
- 信心排序準確度：N/A
- 診斷：樣本不足

調整原因：近 5 日有效樣本 0 筆，低於 15 筆門檻，暫不調整權重。

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

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：INTC Stock Rallies As Wall Street Leans Into AI And Foundry Story - timothysykes.com；人工幾十年只找到 20 種，AI 一出手就發現兩種室溫超導體新材料 - TechNews 科技新報；拒等七年電網擴建，投資大老指路：靠「線性發電機」破除 AI 能源瓶頸 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 122.20 | 122.20 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -7.38% | +12.13% | 195.55 | 211.14 | -7.38% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 552.05 | 552.05 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -1.80% | +3.80% | 2,460.00 | 2,460.00 | 0.00% | 不適用 | 74.39 | 33.07 | 416.98B TWD / 30.09% | 2026-06-01 |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | -1.53% | -23.67% | 386.74 | 506.69 | -23.67% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -16.31% | +20.80% | 373.90 | 446.77 | -16.31% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | -3.41% | +8.29% | 679.00 | 682.00 | -0.44% | 不適用 | 10.86 | 63.05 | 63.03B TWD / 28.57% | 2026-06-01 |
| 2454 聯發科 | 產業/供應鏈推估 | 0.00 | -4.84% | +5.50% | 4,125.00 | 4,310.00 | -4.29% | 不適用 | 62.91 | 65.74 | 47.43B TWD / 4.99% | 2026-06-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [INTC Stock Rallies As Wall Street Leans Into AI And Foundry Story - timothysykes.com](https://news.google.com/rss/articles/CBMifkFVX3lxTE9VWDh3Ui1tUVNpNGJVYTVVUkFUV1R4RGU0MnhpTkVzNXRsMVktM291MVJYWHVwcFNDM05lMnRLUzBnb0lmbVkxdTZDeUZQLV9ZVE9XYTV4Wmg1MExGQmlocmRlYm1sN1cwQndaQlk2c0F3NVFTdjZCS2V2VGlxUQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 06 Jul 2026 13:19:00 GMT
- [人工幾十年只找到 20 種，AI 一出手就發現兩種室溫超導體新材料 - TechNews 科技新報](https://news.google.com/rss/articles/CBMipwFBVV95cUxOZm1JZER6NEFZZDg3TUhycVVEM1hQZnpueGMxVm1nR2RLcmNCVHlWRk9uY0hkX3RGYXI3MXlzaTk3ZlN3andlTTg2VU1HVC1adWZwblUxclVXM0JHaTVYaEtYRm9oOXY3MUJ5MS02NDM5SkI4LUwzOHpFUXhZVFhZWE9sNjN6UWZ0Y0lZOTBJeEV0eHUwN3R6aWUyNk0xZWdESVk1ODB6MA?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 05 Jul 2026 23:51:55 GMT
- [拒等七年電網擴建，投資大老指路：靠「線性發電機」破除 AI 能源瓶頸 - TechNews 科技新報](https://news.google.com/rss/articles/CBMijAFBVV95cUxOdEl3eWk0YWY2eDBPbE1ldTVUcl9XTkw2dDFJRGlTVnRxWmZ2WkdzUkUzV09ZWEVxUWpweVFOcFVrUUhLcTZLTnlxZ2ZucVVoc085WlhmMWlBZ2VNcnBJazUxRmhXOUMtV0ZxMXZKOE9nNUpLQ1VBWXM4TDlmUTdBSlZFUVIyOHdnZjJpcA?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 06 Jul 2026 00:32:05 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：INTC Stock Rallies As Wall Street Leans Into AI And Foundry Story - timothysykes.com；1 Analyst Says This Chip Stock Could Soar 625% to Join Nvidia in the $5 Trillion Club - The Globe and Mail；韓搶攻AI半導體 李在明：速度決勝負 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 122.20 | 122.20 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | 0.00 | -7.38% | +12.13% | 195.55 | 211.14 | -7.38% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -1.80% | +3.80% | 2,460.00 | 2,460.00 | 0.00% | 不適用 | 74.39 | 33.07 | 416.98B TWD / 30.09% | 2026-06-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | -1.78% | +1.22% | 166.00 | 170.50 | -2.64% | 不適用 | 4.00 | 41.71 | 23.12B TWD / 22.85% | 2026-07-01 |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 552.05 | 552.05 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 984.75 | 984.75 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -23.28% | -16.56% | 1,744.43 | 2,335.00 | -25.29% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -16.31% | +20.80% | 373.90 | 446.77 | -16.31% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 3 篇新聞出現相關標籤。

### 主要來源

- [INTC Stock Rallies As Wall Street Leans Into AI And Foundry Story - timothysykes.com](https://news.google.com/rss/articles/CBMifkFVX3lxTE9VWDh3Ui1tUVNpNGJVYTVVUkFUV1R4RGU0MnhpTkVzNXRsMVktM291MVJYWHVwcFNDM05lMnRLUzBnb0lmbVkxdTZDeUZQLV9ZVE9XYTV4Wmg1MExGQmlocmRlYm1sN1cwQndaQlk2c0F3NVFTdjZCS2V2VGlxUQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 06 Jul 2026 13:19:00 GMT
- [1 Analyst Says This Chip Stock Could Soar 625% to Join Nvidia in the $5 Trillion Club - The Globe and Mail](https://news.google.com/rss/articles/CBMi_wFBVV95cUxQZmpnVGl2dkNVUHRtd192SHNuTHRaN2hZSFQxTHhINllTWXM0VWxsVmdHUjZ2T1ZNT1hZMkJIcXhRcFFpeWJFeEp6cWVNbS1sZ2pqMnRxUGRwTWpCRVNYQkF1UkJQVkVyZ1ZtTDVpYVB5TUxKamRSMVhQSjNxZzBIRVJFbEtZZ0MxUUs3b0Z2S3pOd0Z2ZFR0QXlnOXZ6RlF1NWVaemRKZUNUR25jS0dwNEVuZmZHY3ZTejdmSGZVejNramRydzZkbTFNdVRwOS10OTVwZ3d1SVMyTHQ0NkFFVXNvdlVfWG12QWpDUWJwRFVfXzN0UnBuTHBjSGQ0VXc?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 06 Jul 2026 18:56:59 GMT
- [韓搶攻AI半導體 李在明：速度決勝負 - 中央社 CNA](https://news.google.com/rss/articles/CBMiU0FVX3lxTE5Nby1pWkJUZVdPUXZtLVI2Ymk0QXYwR3dSMDlmUkN2bTlOQkpoYlYyUWtMVlU4VEF6YVlfV3VMY1A2ZHJ5Tzd4NEI4bjRoZ2RNU09R?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 06 Jul 2026 09:34:39 GMT

## 消費電子與手機

摘要：消費電子與手機 相關新聞集中在：Flash Crash or Cash? The AI Hardware Reset Investors Can’t Ignore - MarketBeat；蘋果拒交「王國鑰匙」，歐盟版 iPhone 全面封鎖全新 Siri AI - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AAPL 蘋果 | 新聞直接提及 | 0.00 | +18.35% | +34.69% | 312.66 | 312.66 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | -2.42% | -1.83% | 242.00 | 289.00 | -16.26% | 不適用 | 14.13 | 17.19 | 821.76B TWD / 52.11% | 2026-07-01 |
| 2454 聯發科 | 產業/供應鏈推估 | 0.00 | -4.84% | +5.50% | 4,125.00 | 4,310.00 | -4.29% | 不適用 | 62.91 | 65.74 | 47.43B TWD / 4.99% | 2026-06-01 |

關聯理由（前 3）：
- AAPL：新聞直接提及「蘋果」，共 1 篇新聞命中。 同時符合主題標籤：hardware, consumer electronics, smartphone。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「消費電子與手機」關鍵字 hardware, consumer electronics；其中 1 篇新聞出現相關標籤。
- 2454：產業/供應鏈推估：公司標籤符合「消費電子與手機」關鍵字 smartphone；其中 0 篇新聞出現相關標籤。

### 主要來源

- [Flash Crash or Cash? The AI Hardware Reset Investors Can’t Ignore - MarketBeat](https://news.google.com/rss/articles/CBMiogFBVV95cUxNb2ZMRGNIYWhPYkZoSklaZ0ZDRzhBdG9DbTB0RTdGa1REeGs2M2gxbVJNTzl5WXhtZ3FCS0pYak43WF8tMHpqc25wZURjYm9FTHd6SElKSVhwTW5FWGZqS1RjQTYtLUxzaWcyLWwxRTJON3A3Y1FhV09uZVNNN2RreDZnaHktSllzSXBabjExWGxOU1RVZHBBVWZFNUNfWHVSaGc?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 06 Jul 2026 20:52:07 GMT
- [蘋果拒交「王國鑰匙」，歐盟版 iPhone 全面封鎖全新 Siri AI - TechNews 科技新報](https://news.google.com/rss/articles/CBMi0gFBVV95cUxPRzRRMjRmYVJlV25FdG9pRHduaE9ZaGxpcnJrNzN0LW52RDZKZVBCR0pIWWVSSlRtekk2Tm40TDBJYTJ1UHphRnFCeU1zN2QzdXp6UTFBdnVZejVvWWE1MGJUc3NyNGt0Tzg0by1qamdGM3otN1F1cEdOS0ROdGZvSjJyS2paSVB4T3l1SG1fWUVvdFJVbU5MUkVyenctbTB3b0pKMDlwcHBGa3BGaEp3aW5ybTN5UC1weXE1R1U5S01PV1BMVXN4eVZuX05rS2Jib0E?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 06 Jul 2026 03:14:48 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：The AI Trade Is Off to a Hot Start This Week as Chip, Memory Stocks Surge - Investopedia；SanDisk Rebounds 5%, Western Digital Gains 5%, Micron Climbs 3% as UBS, Citi, BofA Turn Bullish on Memory - 24/7 Wall St.；NAND Shortage Fueled SanDisk’s 800% Run. Now Its Biggest Rival Is Coming to Nasdaq - Tech Times

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.62 | N/A | N/A | 984.75 | 984.75 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.31 | -23.28% | -16.56% | 1,744.43 | 2,335.00 | -25.29% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -7.38% | +12.13% | 195.55 | 211.14 | -7.38% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「memory、Micron、NAND」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：surge, shortage, fuels。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk、SNDK」，共 4 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：surge, shortage, fuels。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [The AI Trade Is Off to a Hot Start This Week as Chip, Memory Stocks Surge - Investopedia](https://news.google.com/rss/articles/CBMivgFBVV95cUxNeFJRSWNtNWJMT1NiMlA5R2tEc0VZUXpxdW1IdGdKVmdKOUZSOFI2X0N6RVRpNjJQRTFFQ3RwYkNUd0ZmYWQydTJOTkMzSzYxS0l3bWVwM0RjbERuR3o4X1A5Zmo3cFFub1BndF9BZklLekljSmw5OURoaXFHQ2pkNDJ2RFd2bUpjdW1nT0RVWWVQSUZ5dzg5SEdnbWQyUkdsSDM0QVY1elZBWjBmY3NPcDNRaURoa24zenRqOF93?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 06 Jul 2026 17:23:03 GMT
- [SanDisk Rebounds 5%, Western Digital Gains 5%, Micron Climbs 3% as UBS, Citi, BofA Turn Bullish on Memory - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi2gFBVV95cUxNR3ZWT2RJUjFndGRzYWxJQXltNmxQMTIwSVg1d3M0eEtyU0I2djJDVklfTFlaaUlSRGZielQ5N1A0LVJVQnMtWlZPSm02V0tJdnc0ZTZFaEM0M0czc0RQaHczQ0FzRmU5LUlmcVhHYndoVHcxV3IxSTNRMy1aaXpIUEZJdkxBbVpaVGxzVVh3Ny1IOTZOMTd3ekkzb3ZNQmd0ZXROVlZNOVZwRmpLdjNhdU5BeXZLNkdEdjdSNEdIQ0RBLXNIT3k5bEM1MkVqakZIRnZudXRTZ1JQdw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 06 Jul 2026 13:12:57 GMT
- [NAND Shortage Fueled SanDisk’s 800% Run. Now Its Biggest Rival Is Coming to Nasdaq - Tech Times](https://news.google.com/rss/articles/CBMixwFBVV95cUxQZktTWWEtcS02d3lfa0cwVVhEWWNuWVZOQy03ZGFPcVVPNEFCTURlMFVuQTRLeE54R2xEU3ZEQVB6VFlVb1g3YmpvTWE1dEFLV2k2ZHdYZzFpNWZDYnh4STBMNXh0a0VINWgyM1V6dWxBWERDOEZWdXBZbmZTV1RDNE95bFo2a2RZdDlINklXWDhQa2F1WWxoOTdKSmRaWXpUbnhuVnpZdUJQNldKcDJDUjItY0Q2YXpfUFVocHdwUW9DMjQtRzNF?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 06 Jul 2026 15:13:49 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股大震盪 公股進場護盤 法人：後市看台幣臉色 - 經濟日報；台股震出1.66兆元新天量　外資期貨淨空單逾5.8萬口 - 經濟日報；台股跌620.36點 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股大震盪 公股進場護盤 法人：後市看台幣臉色 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9UUGktWnBUSGhOd2p5TmY2TjVPbmY1XzJxb1RKMm9MeUFMSW13UldISGRtVGp5Xy1razdMb0FDTlhCQURnSW56N0w0OUI1X3lrNmM0QUJubGMxUdIBX0FVX3lxTE16a0RJQjBJRlVGZWo0SC1pY3AtclRlVkw4Um4zdGJKSDE1bnlXR2ppc09pc0M1VjJ0VVBWX21GbDQwZjZsdnJJSG1BSERhZlp4Z3BzdXR3Z2Y4Ym9vQUhB?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 06 Jul 2026 17:03:53 GMT
- [台股震出1.66兆元新天量　外資期貨淨空單逾5.8萬口 - 經濟日報](https://news.google.com/rss/articles/CBMif0FVX3lxTFBwaDNyZV9rSWVBdFBON2U3T1d1aFN6U3VERWVyZUpLUXB6VTFaNUlsUUNPQ1dVNS04OFdyaERGcTJ0OGFQMlNuY28wUWpuV2RTeHhVS2FXTzZPa0cwakoxa3BTTjczcTZwMUE4a2FlS3pYWVgyVGdveW1obzVJdknSAV9BVV95cUxPdUFGTFg1STVheFk5RFpMUl9hdnNCNUxoYzFhd0R4TW9ZM25IMVFhWG1hTGkydUNHTGw5QmNlU052TGF1Q0pzX0xkVUkxUWd5OU41cmt5azQ3Vms3OGxkNA?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 05 Jul 2026 09:00:00 GMT
- [台股跌620.36點 - 經濟日報](https://news.google.com/rss/articles/CBMif0FVX3lxTE13VVVrSzNaTFVkU2kzWTFKQzJNVGNRSHllc2Z0T01xcjZpck9ZblhSV2JJTWFucTJfekVJTmhPWXlLSEZvS1hicXowczdPVzFFNWxKQWFfaEQ2T0dseG9tbEdLQnZCNEZuSmZWdUlZTEpyVTNlS2ZoQmp6Y0pnQlHSAV9BVV95cUxQNEtxSjA0MF9pczM3SE5KdWRhUUlvNVpYdXRrSS1DTDVrc0Z1VF9CN0pJbWlidVVCV2I5VEhPc05LM2tGLTV4X2ozd2xyMDUtY1dVSEFkTkMzR0VTT293SQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 06 Jul 2026 17:08:30 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》下跌224點、守住10日線，47K得而復失- 新聞 - MoneyDJ；個股動態報導內容-ADDFDDB5-8ED4-4CA2-8AA1-E5C6E4354503 - MoneyDJ；個股動態報導內容-3D0A7221-3AFD-4969-8F65-7CD56128840B - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》下跌224點、守住10日線，47K得而復失- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPZXNCcFVZSVlZTEo4Y3pOTzlCNVJIQkw3RXl1MjdRQTB5RXdvM1N4cE1yTk8wM3Bicm1oN3hRcFhZQ1U2RzQ1RUJSaHBKdW5DVDNBaUtEQ2lnb0pWaGZ6MW45am50bjlBR2pkWXhfQl9HTU9YTnpxV3l6d29BcTZ0UjM1VC1JQ2hKWDRsZDZvV2hMZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 06 Jul 2026 07:33:00 GMT
- [個股動態報導內容-ADDFDDB5-8ED4-4CA2-8AA1-E5C6E4354503 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxQRlhVS3dOMjAxRWxYTFpsUEFwVjluSFpPTVYtMmo5YzJsSjlrZ0dkYl9iT1NibGNUX1dIQUxON1dCaG9nU2hYM0ZjNTVOejBiOGczMFdISE1Idk9CaU5uSEpFZzVpcXNMSW85T3QzdXVTc0JxMGJDR3VjekFqVHdQNFhxUDI2QlRtVHlqb214SkRYa28t?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 06 Jul 2026 12:03:47 GMT
- [個股動態報導內容-3D0A7221-3AFD-4969-8F65-7CD56128840B - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxPNU0zVFd6dlZpZl9yeXRabENSVUFPNzh4bXVJekE4MF95Ti1mdGUtUWR5WGZYR29sSGNRUGlHak1DSTZDTjNzTFJXU2ZnZW1VYzRKbTFlaGNyb1RpeGdqY0FmQmlzSXh6Ujdfelhvc2hqRGxpcGR1cVNHU0dLYkRYQ2RqWE1vSHpiSlY2U0ZPWXBIbGZ0?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 06 Jul 2026 10:21:19 GMT

## 新興題材：B836

摘要：新興題材：B836 相關新聞集中在：個股動態報導內容-B59D04F1-14FF-4F03-B836-4B3B421FED8A - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-B59D04F1-14FF-4F03-B836-4B3B421FED8A - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxPS3Z4VWNVYzdfLVBwQk5HUDlqWmR0R1BTWWZOdzhHNzJ6NlNxUDJzTE1CTW52TWNEWXRnNGNDRk5ETVlNU09VRXlsSENOdHRlR0Y1RjdkWEJFR25DWmh6dkl2SjZBY1FrQ3NTM2xPTEdWYjljS1JyTkQyanBOUnphbndKN1JCSUQwcDV2TU12RHVCSE1X?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 06 Jul 2026 02:35:44 GMT

## 新興題材：台股超級法說

摘要：新興題材：台股超級法說 相關新聞集中在：台股超級法說行情開跑 多頭人氣可用 指數蓄勢挑戰50K - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股超級法說行情開跑 多頭人氣可用 指數蓄勢挑戰50K - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE44VnpHWHAxLVlyRS16X1Y2cndXcDN3V3M2V053ZGx4R28tRElPVURhVlNqME9GTjFlQ0tpNFRNTUE5dTFMbVRwNHFjVE9EVExub211QU1VWFV4d9IBX0FVX3lxTE5BdWJENVlCSTF5NlBqWHZXdnRwbFhrbzRzMmk4NWhhcXV3VWstcTJrZnBLX2Jjc2xxakl3NG9GZkpJY1pMV3hjelNWdEJmak5ScDJYNDkxaXRDMkI3MXBz?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 05 Jul 2026 18:22:38 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
