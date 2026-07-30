# 每日股市熱門話題分析 - 2026-07-31

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **AI 伺服器與資料中心**｜負向｜熱度 14｜市場確認 78.91｜同向 5/6
2. **新興題材：這檔連收3根跌停**｜負向｜熱度 1｜市場確認 88.51｜同向 1/1
3. **新興題材：StocksToTrade**｜正向｜熱度 1｜市場確認 N/A｜同向 0/0
4. **新興題材：OpenAI**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
5. **半導體與晶片供應鏈**｜正向｜熱度 4｜市場確認 0.00｜同向 0/5

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.10（樣本 13）
- 5日相關係數：-0.10（樣本 13）
- 同向比例：6/13

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| AI 伺服器與資料中心 | 78.91 | 5/6 | 1 | +6.86% | +3.48% |
| 新興題材：這檔連收3根跌停 | 88.51 | 1/1 | 0 | +6.17% | +8.32% |
| 新興題材：StocksToTrade | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：OpenAI | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | 0.00 | 0/5 | 4 | -7.91% | -2.46% |
| 記憶體與 HBM 供應鏈 | 0.42 | 0/1 | 0 | +0.14% | -20.52% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 相關性偏弱；應提高同向價格確認權重，降低泛 AI、泛半導體等寬標籤推估權重。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-07-18 | 0.18 | 0.08 | +53.85% | 13 |
| 2026-07-19 | 0.37 | 0.09 | +12.50% | 16 |
| 2026-07-20 | -0.59 | 0.11 | +45.45% | 11 |
| 2026-07-21 | -0.12 | -0.03 | +12.50% | 8 |
| 2026-07-22 | -0.33 | -0.15 | +16.67% | 6 |
| 2026-07-23 | -0.01 | 0.01 | +41.67% | 12 |
| 2026-07-24 | -0.16 | 0.43 | +50.00% | 6 |
| 2026-07-25 | 0.30 | -0.06 | +12.50% | 16 |
| 2026-07-26 | 0.38 | 0.06 | +23.53% | 17 |
| 2026-07-27 | 0.54 | 0.11 | +37.50% | 8 |
| 2026-07-28 | 0.32 | 0.13 | +36.36% | 11 |
| 2026-07-29 | 0.16 | -0.03 | +92.31% | 13 |
| 2026-07-30 | 0.25 | 0.92 | +66.67% | 6 |
| 2026-07-31 | 0.10 | -0.10 | +46.15% | 13 |

## 歷史回測摘要

- 回測日期：2026-07-31
- 近5日 3日相關：-0.16
- 近5日 5日相關：-0.03
- 同向比例：+80.00%
- 權重狀態：未調整

- 方向準確度：+80.00%
- 信心排序準確度：-0.16
- 診斷：信心校準問題

調整原因：近 5 日有效樣本 10 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel and AMD Soar 13%, Taiwan Semiconductor Rallies 7% as AI-Chip Stocks Bounce Hard - 24/7 Wall St.；Intel and AMD Soar 13%, Taiwan Semiconductor Rallies 7% as AI-Chip Stocks Bounce Hard - AOL.com；Intel Stock Crashes 40% After Earnings Miss: What Investors Need to Know - Intellectia AI

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.57 | N/A | N/A | 91.13 | 114.68 | -20.54% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.57 | N/A | N/A | 485.39 | 516.10 | -5.95% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | -0.57 | -6.17% | -8.32% | 2,205.00 | 2,410.00 | -8.51% | 同向 | 74.39 | 29.65 | 442.68B TWD / 67.87% | 2026-07-01 |
| NVDA 輝達 | 產業/供應鏈推估 | -0.06 | -7.63% | +11.83% | 195.04 | 211.14 | -7.63% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 產業/供應鏈推估 | -0.02 | +14.86% | -10.97% | 451.10 | 506.69 | -10.97% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -13.19% | +25.31% | 387.84 | 446.77 | -13.19% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.04 | -16.94% | -22.19% | 505.00 | 680.00 | -25.74% | 同向 | 10.86 | 46.89 | 65.78B TWD / 32.86% | 2026-07-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.04 | -12.09% | -16.52% | 3,235.00 | 4,310.00 | -24.94% | 同向 | 62.91 | 51.55 | 58.01B TWD / 2.80% | 2026-07-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 3 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：miss, 衝擊。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。 方向判斷命中詞：miss, 衝擊。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「Taiwan Semiconductor」，共 2 篇新聞命中。 同時符合主題標籤：AI, advanced packaging, CoWoS, AI server。 方向判斷命中詞：miss, 衝擊。

### 主要來源

- [Intel and AMD Soar 13%, Taiwan Semiconductor Rallies 7% as AI-Chip Stocks Bounce Hard - 24/7 Wall St.](https://news.google.com/rss/articles/CBMixAFBVV95cUxPWjNkUlFwLW5GRm5rekkxNDVwNWRqbWdWMkMxbldhRTBGSnNfczRSUHNPNTU2aHdXdEE5OWJqeHNFM09tU1NQRzB6aV9jWVVfYzJCM1pkLUVVZWtzaEhWMXBMckl1eHJDeVNBbTFzZXIwbjNUR0JFaXBRTGl5S0hMa1F4QmpMWmNVTlBDdC0yYjRQMW43cWtKNzFBZ0xyRmhvX21ER0ZFdGpDakt5Rkw2VEp5R24xSDZCVGtWZURMOGxxSWZ5?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 30 Jul 2026 15:51:09 GMT
- [Intel and AMD Soar 13%, Taiwan Semiconductor Rallies 7% as AI-Chip Stocks Bounce Hard - AOL.com](https://news.google.com/rss/articles/CBMid0FVX3lxTE41by1UUVByc3A0NEtzcGdBNFFHUnZqVWcwVjdqRjN2SzFQSzlMYW1sYVhqSUJEMGw1TWd5NkdGeEZoUWhsZkw3YXRHUElLa3d3MTduMHYtRE50WE55WmxvTXNKMTFFYjhHX2Q2blVFd2VsNmd2RUpZ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 30 Jul 2026 16:06:56 GMT
- [Intel Stock Crashes 40% After Earnings Miss: What Investors Need to Know - Intellectia AI](https://news.google.com/rss/articles/CBMia0FVX3lxTE1ZRG8zUGZZb1RHeWxvWi0tU2k4cHo5NGJ3YWNIRHIwQmtEa1VoXy1xbTJYZjFXTUFfV0VrdnA3SG9uSS1zOExzSnlDN05LdU9yY25lakxNRlRnT08xWkNJR19aYVl4TlIwdHJJ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 30 Jul 2026 04:16:27 GMT

## 新興題材：這檔連收3根跌停

摘要：新興題材：這檔連收3根跌停 相關新聞集中在：台積電殺尾盤台股跌105點失守40K 這檔連收3根跌停板- 證券 - 工商時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | -0.42 | -6.17% | -8.32% | 2,205.00 | 2,410.00 | -8.51% | 同向 | 74.39 | 29.65 | 442.68B TWD / 67.87% | 2026-07-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 方向判斷命中詞：跌停。

### 主要來源

- [台積電殺尾盤台股跌105點失守40K 這檔連收3根跌停板- 證券 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBTVjUwN1VmS0lJbTExNGk0bkZqMU8zZUxYaGtTNldsVVYycVNWSW92NVQtNmdxc1JPRk9HQ0VsTEdGVE4wdFhJOVpUbS1HTlVmQUU5b1llcktWTy1OaGY0?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 30 Jul 2026 06:07:00 GMT

## 新興題材：StocksToTrade

摘要：新興題材：StocksToTrade 相關新聞集中在：Intel Stock Jumps As Blowout Q2 Fuels AI Momentum - StocksToTrade

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.42 | N/A | N/A | 91.13 | 114.68 | -20.54% | N/A | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 方向判斷命中詞：fuels。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Stock Jumps As Blowout Q2 Fuels AI Momentum - StocksToTrade](https://news.google.com/rss/articles/CBMiekFVX3lxTE5uTDdTR25UeGZidkpISkgxQ2VEdGdnS0J3cnhPUG9YdExtSklvVEtCZDZNY3NuWFljNHZ1U2ZXd3pCRTlPRHkxcGtXQjhGclBUODRuX0VYa3FCeC02ZjNEcEJIb3c3Nk55Q19ua2R1RmJ3eGJ1c011QXR3?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 30 Jul 2026 11:51:00 GMT

## 新興題材：OpenAI

摘要：新興題材：OpenAI 相關新聞集中在：OpenAI cuts prices on smaller models as businesses scrutinize AI spend - Reuters；OpenAI cuts prices for two of its GPT-5.6 AI models as companies grow sensitive to costs - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 新聞直接提及 | 0.00 | +14.86% | -10.97% | 451.10 | 506.69 | -10.97% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：新聞直接提及「OpenAI」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [OpenAI cuts prices on smaller models as businesses scrutinize AI spend - Reuters](https://news.google.com/rss/articles/CBMiwwFBVV95cUxNRlV6ZXZOeE5EZHRqQ0V6RUZXdVpiNnoxRUNHbDZVdnhocXNJTW1SMDVGZnI0d0hzdnhXLVZCcGIxb1lWdFVmV1V3VjVuWVlULWhHQmI4WWI5ZTJ1TWYxLVV0Q0pScTR6S0Jkd1RJYzRTaTc3bGN6QVJXcXdKa3NNMGxINmEzQnE0WHp5TGV2YXhldFhXeUs5Vzc5Qmc4ZkVqTms1YWZmSWltcVJhajBta0RIdHRfaDhrSGM1OXlhblFHRzQ?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 30 Jul 2026 17:01:43 GMT
- [OpenAI cuts prices for two of its GPT-5.6 AI models as companies grow sensitive to costs - CNBC](https://news.google.com/rss/articles/CBMiakFVX3lxTFBOSUpBdTdrSGxnV01VOWpVSkF3cVZtdVdsMk9rR21Eb0FhVHhFWHRPbk1nbmItUWVRWmljTV9qUDNwblBQdkozVmkxVTJIWjNnUjR1bzV5a3RnZDZ5ZXota2o4N05rZ0FHSEHSAW9BVV95cUxQaTRNRG5HMU15cTEtUlhWNnpfWFJRLTdQbVVhOXlXSzJ4aU5UUm9IUTBHR0dVS01ydG5qN3FjVjRVcVZWRTNBMUtSMkdweEEyNFprbHg3RmtJQ1RSV0k0NWVlcXZPajBBRmFoZUcxRzA?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 30 Jul 2026 17:01:09 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel and AMD Soar 13%, Taiwan Semiconductor Rallies 7% as AI-Chip Stocks Bounce Hard - 24/7 Wall St.；Intel and AMD Soar 13%, Taiwan Semiconductor Rallies 7% as AI-Chip Stocks Bounce Hard - AOL.com；Taiwan Semiconductor Is Copying One of Intel's Best Ideas - Here's Why Investors Should Pay Attention - 24/7 Wall St.

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.57 | N/A | N/A | 91.13 | 114.68 | -20.54% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | +0.28 | -6.17% | -8.32% | 2,205.00 | 2,410.00 | -8.51% | 背離 | 74.39 | 29.65 | 442.68B TWD / 67.87% | 2026-07-01 |
| AMD 超微 | 新聞直接提及 | +0.57 | N/A | N/A | 485.39 | 516.10 | -5.95% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2303 聯電 | 產業/供應鏈推估 | +0.03 | -12.70% | -20.58% | 110.00 | 164.50 | -33.13% | 背離 | 6.68 | 16.54 | 23.12B TWD / 22.85% | 2026-07-01 |
| NVDA 輝達 | 產業/供應鏈推估 | +0.02 | -7.63% | +11.83% | 195.04 | 211.14 | -7.63% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | +0.04 | N/A | N/A | 874.66 | 971.00 | -9.92% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.03 | +0.14% | -20.52% | 1,279.96 | 2,335.00 | -45.18% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -13.19% | +25.31% | 387.84 | 446.77 | -13.19% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 3 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「Taiwan Semiconductor」，共 3 篇新聞命中。 同時符合主題標籤：semiconductor, chip, foundry。 方向判斷命中詞：growth。
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel and AMD Soar 13%, Taiwan Semiconductor Rallies 7% as AI-Chip Stocks Bounce Hard - 24/7 Wall St.](https://news.google.com/rss/articles/CBMixAFBVV95cUxPWjNkUlFwLW5GRm5rekkxNDVwNWRqbWdWMkMxbldhRTBGSnNfczRSUHNPNTU2aHdXdEE5OWJqeHNFM09tU1NQRzB6aV9jWVVfYzJCM1pkLUVVZWtzaEhWMXBMckl1eHJDeVNBbTFzZXIwbjNUR0JFaXBRTGl5S0hMa1F4QmpMWmNVTlBDdC0yYjRQMW43cWtKNzFBZ0xyRmhvX21ER0ZFdGpDakt5Rkw2VEp5R24xSDZCVGtWZURMOGxxSWZ5?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 30 Jul 2026 15:51:09 GMT
- [Intel and AMD Soar 13%, Taiwan Semiconductor Rallies 7% as AI-Chip Stocks Bounce Hard - AOL.com](https://news.google.com/rss/articles/CBMid0FVX3lxTE41by1UUVByc3A0NEtzcGdBNFFHUnZqVWcwVjdqRjN2SzFQSzlMYW1sYVhqSUJEMGw1TWd5NkdGeEZoUWhsZkw3YXRHUElLa3d3MTduMHYtRE50WE55WmxvTXNKMTFFYjhHX2Q2blVFd2VsNmd2RUpZ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 30 Jul 2026 16:06:56 GMT
- [Taiwan Semiconductor Is Copying One of Intel's Best Ideas - Here's Why Investors Should Pay Attention - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi2AFBVV95cUxQVzFJTktWRzJ1N29FeG5tOFJtOGc4RllPQ1B6ODdBSTFiWW5kUDc5a01aUEhxVEk1a3ByTHVsamw5LWJKWFo1bjItYlc3QUZJVWZVSW5NOF9CZktZcW1VNkhDbmZkUVQ0OEdhbjJSWk5hb0R0UUtENlMwWUxId3JsRXlwRGtnVUdKS1Q3U3ZDM3ItUmJIOGw2UExJendSVkFTY2JjS0wzTnRLYUVPcUt0S0dOUmpUX1lQZkNOSmVNOWdXc3NZT19GS3JCYXZWX3AzcUVrdTdYTmg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 30 Jul 2026 15:13:34 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Micron vs SanDisk: Which Chipmaker Stands Out After the Pullback - Yahoo Finance；Memory Stocks Blast Off: Micron, SK Hynix, SanDisk, Western Digital, and Seagate All Rally Double-Digits - 24/7 Wall St.；Prediction: Micron and Sandisk Stocks Will Both Plummet After July 30 - AOL.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.48 | N/A | N/A | 874.66 | 971.00 | -9.92% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.36 | +0.14% | -20.52% | 1,279.96 | 2,335.00 | -45.18% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -7.63% | +11.83% | 195.04 | 211.14 | -7.63% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、memory」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 4 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Micron vs SanDisk: Which Chipmaker Stands Out After the Pullback - Yahoo Finance](https://news.google.com/rss/articles/CBMioAFBVV95cUxQWDg3MnNXR21xVzNDeGs0STk0Vks1SElxVnRaT2NvSm9UVWtROGRXU3pnYkZQbFZpVG50elQ3RmxrQkNpRng0eGJOUEdESWlScFJCaE9lemlpS0FkRFZfN1dyN3BnRjVvemxrWHctMV9jbjkwak9VVHdUMnQ1bWc2OThMNVY5bUF0SlI2Qk91YVd4bkRtNmM3VjIySFNFQWxK?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 30 Jul 2026 15:41:14 GMT
- [Memory Stocks Blast Off: Micron, SK Hynix, SanDisk, Western Digital, and Seagate All Rally Double-Digits - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi2wFBVV95cUxQYThlb3NydmtXZkVkeS1VSFJ1UzlBNk16aFZUbDIzLWk3LWJNUmh5S25PT1lyQTJTa2JNa0VIbkdzcDhkTTFORk1jdjlHYjZoeHppUmxNNzBnT1BGTWNKMUVROEdDbTVJUHZmbFMzX3Q0SWZwaU53TVl3cUNsMHZ1eXBRNHFmM0VmRFpTbTFPb0lQNU1WNWRzUWtHU1ZiaHg4UXhQeHlrdV9LRFBwNEYtM0NuTHNLMjdSdzBOa3ozb2dHZjR6cTVDeTQyLVpNb05VZXVEb3B6eGxxeVU?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 30 Jul 2026 14:44:36 GMT
- [Prediction: Micron and Sandisk Stocks Will Both Plummet After July 30 - AOL.com](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPd3FPNU9EQ0NyQW5nSmVVTDQtbnhHNjd5MmhXaDk3eE5LRUFYR0tNRkNUNDBGZ3A0NnFlRHdXSFF0TnJoa3VxbUVxM3hEMDZyaVpRZl95ek1sYW93QmktdGFiWHloODVTY1Q5ZnpSZEswUVpiMXA0S2ROSmtMaDdGRkExY2xqWXE5?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 29 Jul 2026 18:15:57 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：多殺多賣壓湧現 台股國家隊急救援 - 經濟日報；台股大回檔 此時是國安基金護盤時機？財政部回應了 - 經濟日報；台股回檔爆槓桿危機！929檔「融資告急名單」熱門族群個股曝光 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [多殺多賣壓湧現 台股國家隊急救援 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9HRTdma1NSRFc2N3hjeF9SVGgzdXFxcm5uMDlVUVY1SWVJUjA3RGlMMWc4TkFoeGJfb0s0QnBnNUxwS3NRRlpaTzVyZC1JZHFXSmE3THlNOWZoUdIBX0FVX3lxTE5YSU9HSlNBNHpjbUJpQ1EzeThuX3dVWTdNV0pZTGstS3JFT3BGTk9kQmlFSzZuTUZhbVdqXzRudXl6LUJ0a1N0YUZuMkZhVF9Md0VEUjBYY1FSUXdYeW9N?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 29 Jul 2026 17:53:59 GMT
- [台股大回檔 此時是國安基金護盤時機？財政部回應了 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBQTHFoUHNLUWRYOFh0Y3dxby1vMjY3a3dFZHNNMzBlekdiNHV4NzdGQWVVbjMySHYwSmVjQVhrbm9pRGhwMFc5UURXVWo4VFo4NXhXa2xWMG1IZ9IBX0FVX3lxTE9PTDFqYUJyNzVMeDlfSWVCcmZMaEpXYzBHZzI2LUdKMWVWYmdTUklMaFdUT0h6YTE3TkhBTVBCUEt1eWE3Tkd4TEZnRkpmNkgwZ1RWeldMMkRkY3A3QlFZ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 29 Jul 2026 02:11:38 GMT
- [台股回檔爆槓桿危機！929檔「融資告急名單」熱門族群個股曝光 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1pRXdBUkNhamxfaU5ianlPS2RfdklXYTZaTm1IZEc0NFRDaF93RE9BUnNJQzNVdjFDd0Z3ZmpHSnYzQ3ZPUlpJTThrTWdwYXV2bEtkOXZiUW01QdIBX0FVX3lxTE0wWE9rYzBmWlNETXVFYlMyNVZkeWZHYU81Rll5RlptbWVpTDdiaG40eG95ZUx2N2UwYVpxeHgyUkt5bXlpeGNpZ3FaWTRtc0tZd2taN3RuY1V2T2RLSURn?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 29 Jul 2026 09:00:00 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：基金-FundDJ基智網 - MoneyDJ；台股失守4萬點關卡...國安基金出動救火？ 財政部：市場失序才會進場- 新聞 - MoneyDJ；《台股盤後》衝高千點後壓回、收跌105點，失守40K - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [基金-FundDJ基智網 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxQMGJQT2Foak8xMlRSWlh4aE9aanFZY0NBMFFwMnVoQV8zeVpnM0x4WTRyVUMwZHV2WkFDWG1CLTNCU3B4OTBKRUZOWkJPSGZud2xZek92R3Z5U2JDbWwtYmFYNnh3ak1aazVtbVM5SDctSEZtRFMwNkNKa19VQmZXdlNJNnBEZmktWVNjRGNmVkY?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 30 Jul 2026 18:24:50 GMT
- [台股失守4萬點關卡...國安基金出動救火？ 財政部：市場失序才會進場- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPV1cyUmdfX2g3Vk9iYjc4U1owTmFDR2ZpRkVzNzdpNEp4V1dKcFVrdjNtaUpHM0ZsU1FaX1RhVm5iN0k0WC1BMXhxZFlNZjZIM1lfanZyZzROcGVuT1dibVJFM1YxYlhkSTYyRkJtd0Q5bXBjVE9PeHhOSUZ3NldZQ2d5V0xzX2FibnRHLVAyUUtCdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 30 Jul 2026 13:04:00 GMT
- [《台股盤後》衝高千點後壓回、收跌105點，失守40K - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNVElrYVFVczhXalNoMFo3R0ppdVpDcHJtSHF5cmFZWFFrTkxnRDJjWEw1VXFoQUdPTHFhajJfZy15Qk5DblFFbmw1NG1EdXJocFNuMWdhQVNDNkhsVUlzNEoxNjNoaGFkaEVzMmJMZUl2UXdHeC0tODFYb05CdjhuYzZGTzVsLU94eVNGWU5tZzRrdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 30 Jul 2026 07:49:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
