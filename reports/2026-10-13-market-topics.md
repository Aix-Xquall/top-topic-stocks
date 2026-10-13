# 每日股市熱門話題分析 - 2026-10-13

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **散熱與液冷供應鏈**｜負向｜熱度 2｜市場確認 94.42｜同向 1/1
2. **半導體與晶片供應鏈**｜中性｜熱度 5｜市場確認 N/A｜同向 0/0
3. **新興題材：MarketBeat**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0
4. **記憶體與 HBM 供應鏈**｜負向｜熱度 12｜市場確認 30.54｜同向 2/5
5. **AI 伺服器與資料中心**｜負向｜熱度 12｜市場確認 28.75｜同向 4/8

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.05（樣本 15）
- 5日相關係數：-0.03（樣本 9）
- 同向比例：7/15

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 散熱與液冷供應鏈 | 94.42 | 1/1 | 0 | +8.14% | +1.60% |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MarketBeat | N/A | 0/0 | 0 | N/A | N/A |
| 記憶體與 HBM 供應鏈 | 30.54 | 2/5 | 3 | +0.85% | -0.20% |
| AI 伺服器與資料中心 | 28.75 | 4/8 | 4 | -2.08% | -3.15% |
| 新興題材：TradingKey | 0.00 | 0/1 | 1 | -1.86% | N/A |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 相關性偏弱；應提高同向價格確認權重，降低泛 AI、泛半導體等寬標籤推估權重。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-09-30 | 0.05 | 0.04 | +33.33% | 18 |
| 2026-10-01 | 0.21 | -0.27 | +40.00% | 20 |
| 2026-10-02 | 0.51 | 0.37 | +72.73% | 11 |
| 2026-10-03 | -0.35 | 0.13 | +16.67% | 6 |
| 2026-10-04 | -0.12 | 0.70 | +80.00% | 20 |
| 2026-10-05 | -0.16 | 0.29 | +73.33% | 15 |
| 2026-10-06 | -0.72 | -0.75 | +37.50% | 8 |
| 2026-10-07 | 0.48 | 0.61 | +73.33% | 15 |
| 2026-10-08 | 0.13 | 0.40 | +58.33% | 12 |
| 2026-10-09 | -0.03 | 0.37 | +38.89% | 18 |
| 2026-10-10 | -0.28 | -0.96 | +57.14% | 7 |
| 2026-10-11 | 0.66 | -0.74 | +40.00% | 5 |
| 2026-10-12 | -0.08 | -0.07 | +41.67% | 12 |
| 2026-10-13 | -0.05 | -0.03 | +46.67% | 15 |

## 歷史回測摘要

- 回測日期：2026-10-13
- 近5日 3日相關：0.22
- 近5日 5日相關：0.21
- 同向比例：+45.45%
- 權重狀態：已調整

- 方向準確度：+45.45%
- 信心排序準確度：0.22
- 診斷：正相關

調整原因：近 5 日信心分數與後續報酬呈正相關，提高市場確認、歷史題材與直接提及權重。；關鍵詞×公司後續樣本有效 4 筆，未達 30 筆，不調整樣本權重

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

摘要：散熱與液冷供應鏈 相關新聞集中在：Rubin、Trainium、TPU接力助攻！「散熱大廠」9月營收首破200億元 多外資力挺喊買 - FTNN 新聞網；焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | -0.52 | -8.14% | -1.60% | 3,315.00 | 3,440.00 | -3.63% | 同向 | 75.13 | 45.12 | 21.02B TWD / 44.92% | 2026-10-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 2 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：跌停。

### 主要來源

- [Rubin、Trainium、TPU接力助攻！「散熱大廠」9月營收首破200億元 多外資力挺喊買 - FTNN 新聞網](https://news.google.com/rss/articles/CBMiS0FVX3lxTE0tQWxMdV8wRlRmcTMyaGpjeGdIeUNyd2tEekRUbHpkRVY1MjY2MEJYUjI0OXp3b0FZc0dMQmRodVNDR09lZlY2aE5uSQ?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 11 Oct 2026 01:53:00 GMT
- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 11 Oct 2026 21:05:15 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：INTC, AMD, AVGO: Chip Stocks Jump Premarket After Nvidia's Blowout Report - Stocktwits；Why Are Nvidia, AMD and Intel Stocks Falling Today? AI Chip Selloff Deepens - Stocks Down Under；泰國補半導體人才缺口官員：安排工程學生赴台培訓| 產經 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | -11.62% | N/A | 101.35 | 114.68 | -11.62% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +2.51% | +13.11% | 226.32 | 229.28 | -1.29% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | +15.14% | N/A | 594.24 | 608.10 | -2.28% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | 0.00 | -1.74% | +1.60% | 2,500.00 | 2,550.00 | -1.96% | 不適用 | 86.28 | 29.44 | 511.86B TWD / 54.65% | 2026-10-01 |
| AVGO 博通 | 新聞直接提及 | 0.00 | -4.22% | -6.09% | 354.73 | 446.77 | -20.60% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 新聞直接提及 | 0.00 | +20.19% | +9.99% | 541.15 | 541.15 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | -1.36% | -9.91% | 140.00 | 164.50 | -14.89% | 不適用 | 6.68 | 21.88 | 25.35B TWD / 27.22% | 2026-10-01 |
| MU 美光 | 產業/供應鏈推估 | 0.00 | +1.86% | N/A | 989.04 | 1,029.00 | -3.88% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC、Intel」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [INTC, AMD, AVGO: Chip Stocks Jump Premarket After Nvidia's Blowout Report - Stocktwits](https://news.google.com/rss/articles/CBMizwFBVV95cUxPQUU4dTZXYndUX2YwZlZ6VmR6d3JoV2dDbE1XR1FKS0p2YTZScmlIclZkTUxxb0paRW00TEgwVlE1Qk5hT3BnM3J4eVZqVDBpZ3o1blFiYTQ5M2t3OTlJU3pud01kVlJYQzFVaF82a2xfWXRfM2R2MzBVRDczX0pnRkpPZ3dpam03QlhibkliRnQ3NWhJU25VM0d1bVlvSm02bjJaV2pjZlJwTUpVVnZCMHRxYjFFd2Q2RXRNOFl3ZkItc0llS0JKR2dVN1VORDg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 12 Oct 2026 15:44:18 GMT
- [Why Are Nvidia, AMD and Intel Stocks Falling Today? AI Chip Selloff Deepens - Stocks Down Under](https://news.google.com/rss/articles/CBMiekFVX3lxTFBwQjkyMXh0YndVRlJhS3FBSll4dVB4akV2TWoyclpKWEE3RXEzODUwYWxtczdwdV9PUFFLUnVfenNtSWpZWnlGRUMzbGJiVHpaOVA0WEVmQ3RzSHFOalAzWENZWFVJeW1QMWtPRDh2YnRKNkdGYzFfN2hR?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 12 Oct 2026 17:41:20 GMT
- [泰國補半導體人才缺口官員：安排工程學生赴台培訓| 產經 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE96Z3RSbXB0b1R3QThwV0owTlNwUzc4Y2RsOUVxVkY4T0Zac0FDVHB2aEJka2RIbG1ydDhyMkVPM1c0dFU0RWR0QWR2Mi0zQmNZcGVwYXB2anhsSVU1c1E?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 12 Oct 2026 13:25:00 GMT

## 新興題材：MarketBeat

摘要：新興題材：MarketBeat 相關新聞集中在：Intel (NASDAQ:INTC) Stock Price Down 3.2% - What's Next? - MarketBeat

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | -11.62% | N/A | 101.35 | 114.68 | -11.62% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel (NASDAQ:INTC) Stock Price Down 3.2% - What's Next? - MarketBeat](https://news.google.com/rss/articles/CBMirAFBVV95cUxNek9NdUVIZldzbTdmd0JuanBsaW5JRE11YUhpLWpXUW1aaEJaM3hjVWplU2VWWFI1aXN6WUtnZGNlNlYwTE5JdW1zM3VoRFhiMHdOMHY0ZUEteW43OHdfc2NHV3A3UXAxOU96T05ZNmp2LWxSWDdpcnZ4WXNqX2QwNlNkUHFyVUF0OVdEbFFtTVk5TDRhS1kxbWdmczRCa1RfWU1LTUVBRTBBTkVN?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 12 Oct 2026 21:37:11 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：SNDK, MU, INTC, AMD, SKHY: Chip Stocks Extend Slide As AI Funding Concerns, China Competition Weigh On Sector - Yahoo Finance；INTC, AMD, NVDA, MU: Chip Stocks Open Mixed Premarket After Worst Week In A Month - TradingView；Micron May Become a Safe Haven Investment Prospect in 2027 and Beyond - TradingView

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | -0.29 | +1.86% | N/A | 989.04 | 1,029.00 | -3.88% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.59 | -12.12% | -12.72% | 1,487.33 | 2,335.00 | -36.30% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.26 | +15.14% | N/A | 594.24 | 608.10 | -2.28% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | -0.51 | -11.62% | N/A | 101.35 | 114.68 | -11.62% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | -0.23 | +2.51% | +13.11% | 226.32 | 229.28 | -1.29% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK、SanDisk」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [SNDK, MU, INTC, AMD, SKHY: Chip Stocks Extend Slide As AI Funding Concerns, China Competition Weigh On Sector - Yahoo Finance](https://news.google.com/rss/articles/CBMijwFBVV95cUxNSGpkbjZBYzUtM1ZpSzdHSGtQa0ozaGpQeUVJVDFWV3VsdDZQbU9nYXlXNHhaTXRpN0lmc0lZT3g4QWhHNEtNckpTV2g0d1JNZmlBT0twYWxRVzA4bFFLY2R6QVZHcU5UcGFNeXlWWjVRQ0pONHNrSHJWdHp1UUYyaDN3VkIzR0tncjZMSFZfOA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 13 Oct 2026 01:42:00 GMT
- [INTC, AMD, NVDA, MU: Chip Stocks Open Mixed Premarket After Worst Week In A Month - TradingView](https://news.google.com/rss/articles/CBMi0wFBVV95cUxNVEJkZE5wbzh3ejh4cTg2UVNuaEFQNUpqa042WmVEMUM2ZTJ2ZHJ3bS1IRUJOM29pWHp2NEJ1M2o1dEpHZUEyaEtvYXZBSGtpWkJCWllmcS1Pb3JtOUpVZUlualdLYmFDWjNXMHZVV1U0WVF1OEVkM3FBMHRVU1AzOXM0ZjdQcDVuWV9LM0dtelE0bmh6SnBUMlRFdDBZMl9ZS3JSZ0Vvall2RTNiTUhyYkxhMGRkN1hScEJhTFZOOVRDTGhhOGZBbXhvdnMtWHp1Ums0?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 12 Oct 2026 08:55:35 GMT
- [Micron May Become a Safe Haven Investment Prospect in 2027 and Beyond - TradingView](https://news.google.com/rss/articles/CBMiwwFBVV95cUxNS3BJV2FUQmxVSnpzYlZ1N1hBN3lHdUstR1YtRlVxRFdHQnlXTWk0SGpZVE1wdUlXak1ULU1jbVhrSnN3OWd5MENwbTQzeDBhOVJ5MXpJVlhGSEItZTVUbXNXV0NycTlrRkdWazRQb05oV2wxZTRtcHlMazdqZUZtVThSajlsQ3c5Zk5sTE5hUjJVcjBudDVKR3N0VjBjMGgzTFhtYjhheHJzOTBVUkhJUHI0T1J6Ry15ZThNaklEd3BYbms?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 12 Oct 2026 13:21:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Why Are Nvidia, AMD and Intel Stocks Falling Today? AI Chip Selloff Deepens - Stocks Down Under；英特爾與博通執行長示警，融資恐成 AI 發展最大瓶頸 - TechNews 科技新報；7,500 億美元的 AI 軍備賽，四大巨頭資本支出竟超車單一國家 GDP - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.59 | -11.62% | N/A | 101.35 | 114.68 | -11.62% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | -0.28 | +2.51% | +13.11% | 226.32 | 229.28 | -1.29% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.27 | +15.14% | N/A | 594.24 | 608.10 | -2.28% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 新聞直接提及 | -0.26 | +20.19% | +9.99% | 541.15 | 541.15 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | -0.51 | -4.22% | -6.09% | 354.73 | 446.77 | -20.60% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.06 | -1.74% | +1.60% | 2,500.00 | 2,550.00 | -1.96% | 同向 | 86.28 | 29.44 | 511.86B TWD / 54.65% | 2026-10-01 |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.02 | +2.42% | +6.87% | 738.00 | 744.00 | -0.81% | 背離 | 13.92 | 55.14 | 88.13B TWD / 45.52% | 2026-10-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.04 | -6.00% | -6.57% | 4,495.00 | 4,920.00 | -8.64% | 同向 | 60.69 | 76.38 | 55.40B TWD / 1.97% | 2026-10-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel、英特爾」，共 2 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：reduce, 恐。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。 方向判斷命中詞：reduce, 恐。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。 方向判斷命中詞：reduce, 恐。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Why Are Nvidia, AMD and Intel Stocks Falling Today? AI Chip Selloff Deepens - Stocks Down Under](https://news.google.com/rss/articles/CBMiekFVX3lxTFBwQjkyMXh0YndVRlJhS3FBSll4dVB4akV2TWoyclpKWEE3RXEzODUwYWxtczdwdV9PUFFLUnVfenNtSWpZWnlGRUMzbGJiVHpaOVA0WEVmQ3RzSHFOalAzWENZWFVJeW1QMWtPRDh2YnRKNkdGYzFfN2hR?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 12 Oct 2026 17:41:20 GMT
- [英特爾與博通執行長示警，融資恐成 AI 發展最大瓶頸 - TechNews 科技新報](https://news.google.com/rss/articles/CBMitgFBVV95cUxPaFFhRzhXakxzZkR5X0FLX2lYcFFWNXJNd2pJa1VXUUN3d0RGd3dMUFNqTTloVC13cEc3eS1iMi15bkV6QV9zWEtIdVhjUjk0Z3MtbGwzc0F3bDZXY1JoOW5OamJ2dnhfalRFWWFicFBEUGZNV1ZCUEc3a3VXd0ZxZ2RMbWM3cHZMUjVFZ0dORmxJamJnMzl4Vm9BMWE4bXZfMzljNFd5ZldLdExyX1oteVFCaEU3UQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 13 Oct 2026 02:16:02 GMT
- [7,500 億美元的 AI 軍備賽，四大巨頭資本支出竟超車單一國家 GDP - TechNews 科技新報](https://news.google.com/rss/articles/CBMieEFVX3lxTE1TaUhUdnFSanN1d0pjaVZsWGd2aFNtYVNNSmJBTnhKN0hHNEg1ejZramcwQWE4SVNINHUzdzMwZ3JDbVllanktNUZ2Z0tZb1VzcS1CZkJORk8yZHp0YnZqUmxRTzk1YWt5NXVFRjVyU3Nyb0dwamhfXw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 13 Oct 2026 01:50:13 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Micron Stock Price Forecast: MU Falls Below $1,000 as ChangXin Memory Tech Progress Sparks Concerns - TradingKey；Micron Technology Inc Stock (MU) Opened Down by 3.56% on Oct 12: Drivers Behind the Movement - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | -0.26 | +1.86% | N/A | 989.04 | 1,029.00 | -3.88% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU」，共 2 篇新聞命中。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Micron Stock Price Forecast: MU Falls Below $1,000 as ChangXin Memory Tech Progress Sparks Concerns - TradingKey](https://news.google.com/rss/articles/CBMi1wFBVV95cUxPX0hRVUtQSEZaMkVQdFNra21GdDVUcXFHSlpXN0NYZzlMQW1DZmhPLW51emZVRVBDNWtrSmFibUpVZ3lvaDk0a2E5WmpsOWs2SkVDZnFFQUZGSFY2c2ZnQVFOTHAweVE2Zm5OcXF6cTNBVjJGc2RDWlo4dUIzaFFMTmhNdHk4RmlPYURoa2E3cnI0d04tVDZWdUtaVlQ3QnRRQU1XTGg5VU5FOVYwelBGdFZsZU90VVlBSHRHa191THRYOVlVSTdtNlZsSXBVZDZfNlBOODRuVQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 13 Oct 2026 02:00:05 GMT
- [Micron Technology Inc Stock (MU) Opened Down by 3.56% on Oct 12: Drivers Behind the Movement - TradingKey](https://news.google.com/rss/articles/CBMiiAFBVV95cUxOSVZlaUtLb3JUMWx3NDVuVTlvZnFRNTJsNlU1Z2RoT1RUMERyVUloeWllcHE5WWxsUy1Pb2lTYUJTTmY2SWczNzJvNHo5bkNYWGxuSlUwLThlNHBaMXNoa2ttN2JqQ1ByS0MyMFc2RURhRWdabmRQaTM0ZXA3c0Jmd1VVckxXRGVm?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 12 Oct 2026 13:47:15 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：個股動態報導內容-2F9E8442-0C18-4F4A-AA05-100B03A5414E - MoneyDJ理財網；個股動態報導內容-E1D1BE83-2041-4EFC-A467-9D73937C9BA9 - MoneyDJ理財網；台股早盤大跌最深近千點 法人提醒恐再跌到這個區間 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-2F9E8442-0C18-4F4A-AA05-100B03A5414E - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilAFBVV95cUxQVWE1VTYzMjlIeV9pRnpkSEtKajIzYmN2dk0wT2haNkxkRTMzVlpXWjNsWnlTNEE5M1p0UXAwaHliUXJ3UHpZVC1rR2U0cGx5TkhqajY3YzBxRDRXSkM3WC1PMnhSQU50Njc5dEx4ZU1WQmFETjgyanZXeDF1NnV6c0ZzUHJ0NER0SmljY2RBNlZfazhi?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 12 Oct 2026 14:02:27 GMT
- [個股動態報導內容-E1D1BE83-2041-4EFC-A467-9D73937C9BA9 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilAFBVV95cUxOZkdQOEZYZGxlMUpGb0pNV2ZxSGNiUl8xX1htc3JnYUpybTBoSlViWW5OR19xQWdDTFFBUDgwVlIxYUFRY2RhQnRXOEpJMjIwc1FkYVdiOUJXTkFOVFE0RGwtRVd2YXNuSVltMTZXNWMxeFNQTkg0YWlCdC1qcTM1WEdnUHppYlA2LUk5YzVySVZjNDho?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 12 Oct 2026 11:26:20 GMT
- [台股早盤大跌最深近千點 法人提醒恐再跌到這個區間 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1udUYza3hfY2s2REZDYXpic0VqbEMzRFhsVENieG1od3VqSGV4ZzhYZHNqeGFmSnRMZDVOTnBmbGVITEF2UFBfZFZXZHItYVZ4N3FvNkQ5NHJDZ9IBX0FVX3lxTFA3b3oxMm85Nkx2ZWhPMjMycng5cGtZTHBfZzBwVEFRTmZVWEtrMGhfTTBHM1VrUUcwSS1kOEk0Zkp5ejNiSUNmRWhGS1FySlZTM3lVb3pLUEkxNWlmUXo0?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 13 Oct 2026 01:57:54 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：統一證券：台股技術面呈現漲多震檔整理格局- 新聞 - MoneyDJ；國票證券：台股多方信心並未鬆動- 新聞 - MoneyDJ；《台股盤後》開低走高/量縮收跌11點 10日線失而復得- 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [統一證券：台股技術面呈現漲多震檔整理格局- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPYkJ6aFdDYWFXbEZWN2htYWtMQy1MdHlIcUI4bFJjTXlGXzZuQ3dIWXlhdlFXa2lwM3dFWjZzTF9GZHA5cVR1ZlpTblhyRnpvSVZxZmhiS0RmSXFEbXNObmU1QjFDRU1zdGRrRDRlVzZmc0pZcnlTX1pXeHYzUW1HaHgxSXhTb05RbVRpbGlNNFJfdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 13 Oct 2026 00:38:00 GMT
- [國票證券：台股多方信心並未鬆動- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxOT1RrMWw1WERQS3BGOXQ1YmlyVGtPSnVpdExKa2JPUk5SS2FkU3N1ZDFTNVdteGdNYjlPNU56T2lpQ1hHa3VkeDFUd3NMcGlQZHpkaGZnYzN6dXFkQnQ4Tm5yTEpFVFZoQmJTME5vUUxKOXQ0SXVoYkstVldwblM1NTZDNVEwUmhJRl9ESElRMFQyUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 13 Oct 2026 00:38:00 GMT
- [《台股盤後》開低走高/量縮收跌11點 10日線失而復得- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQS190ckYzU1J6R3pLWVJYd1Ezd0NIVjJmeHJ1TVg1X0pWeVc1MDVRVVBHdWV1WGstUUtQMDVRd21UOUVHMGJ6S01zVHpSNUkyRFFYZWJlcFhQdmE5a09RRUk0Vy0wYl9lMElGUjhEWWg2MmpmMzdZdl9HMktmdnJsR1RtZk9hS3dERF9fd19LeGVBUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 12 Oct 2026 08:08:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
