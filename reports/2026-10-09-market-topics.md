# 每日股市熱門話題分析 - 2026-10-09

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **利率與成長股估值**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
2. **AI 伺服器與資料中心**｜中性｜熱度 15｜市場確認 43.13｜同向 3/7
3. **半導體與晶片供應鏈**｜正向｜熱度 8｜市場確認 30.80｜同向 3/8
4. **記憶體與 HBM 供應鏈**｜負向｜熱度 7｜市場確認 33.32｜同向 1/2
5. **散熱與液冷供應鏈**｜正向｜熱度 2｜市場確認 0.00｜同向 0/1

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.03（樣本 18）
- 5日相關係數：0.37（樣本 12）
- 同向比例：7/18

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 43.13 | 3/7 | 2 | +4.38% | +4.63% |
| 半導體與晶片供應鏈 | 30.80 | 3/8 | 4 | +1.52% | -1.30% |
| 記憶體與 HBM 供應鏈 | 33.32 | 1/2 | 1 | -0.56% | +9.97% |
| 散熱與液冷供應鏈 | 0.00 | 0/1 | 1 | -4.04% | -1.99% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：群聯9月營收 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：B7201AFA | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 相關性偏弱；應提高同向價格確認權重，降低泛 AI、泛半導體等寬標籤推估權重。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-09-26 | 0.22 | 0.14 | +63.64% | 11 |
| 2026-09-27 | 0.11 | -0.14 | +57.14% | 14 |
| 2026-09-28 | 0.05 | -0.53 | +63.64% | 11 |
| 2026-09-29 | 0.31 | -0.78 | +16.67% | 6 |
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

## 歷史回測摘要

- 回測日期：2026-10-09
- 近5日 3日相關：0.05
- 近5日 5日相關：0.11
- 同向比例：+42.86%
- 權重狀態：未調整

- 方向準確度：+42.86%
- 信心排序準確度：0.05
- 診斷：低相關

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

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：美債殖利率衝高，如何影響 AI 股估值修正？ - TechNews 科技新報；〈美股早盤〉通膨陰影又來了！主要指數開低 晶片股也吃悶棍 - 鉅亨網

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +16.07% | +6.22% | 522.61 | 529.76 | -1.35% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [美債殖利率衝高，如何影響 AI 股估值修正？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMisgFBVV95cUxPNkVlWHBrQ1RhRFFjdTN5S1JzRHVyRllJUkRoSUJCZk0wbWlRdVgwRnIyZ3I3UDNvcDNKbXk0ci1Ebl9DMTNSOExLTWFlUkhQRktqSmJxNUV5dTZMelBZVWZvMnZwM0Jkd0tRVWFfQi1Ib3FqM1RGc1ZUOVZtR1V3aTIyMHZydHNvX0huLURabjkxTnNTSVZuYW50aXRYS3c4a0FhV2JLYzkwcmpGdWRzdUZn?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 08 Oct 2026 13:24:34 GMT
- [〈美股早盤〉通膨陰影又來了！主要指數開低 晶片股也吃悶棍 - 鉅亨網](https://news.google.com/rss/articles/CBMiT0FVX3lxTE8ybXg1Q3pFcEgxV05IZl9ITzFmbVJUQjh4RFJDVk9LQU4wZXpmSkZJWXMxQWdlXzZNbzBMLTdOYk1NRXpQQURSenhwZEM2eVE?oc=5) - Google News source discovery | 鉅亨網 Thu, 08 Oct 2026 13:39:04 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：10月台股主角 第一金投顧：AI 需求強勁 半導體擔綱 - 經濟日報；Elon Musk Reaffirms Control Over Terafab AI Chip Complex As Intel Remains Involved - Yahoo Finance；三檔 AI 流量股誰值得買？名嘴 Jim Cramer 獨推 Akamai - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.27 | -6.63% | N/A | 107.08 | 114.68 | -6.63% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 新聞直接提及 | 0.00 | +9.09% | +22.08% | 340.42 | 340.42 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.06 | +4.39% | +15.19% | 230.48 | 237.47 | -2.94% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.06 | +20.26% | N/A | 620.68 | 645.86 | -3.90% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.04 | -0.97% | +1.59% | 2,550.00 | 2,585.00 | -1.35% | 未明確 | 86.28 | 29.56 | 511.86B TWD / 54.65% | 2026-10-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | +16.07% | +6.22% | 522.61 | 529.76 | -1.35% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -2.75% | -4.66% | 360.14 | 446.77 | -19.39% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.03 | +0.27% | +4.79% | 744.00 | 744.00 | 0.00% | 未明確 | 13.92 | 53.84 | 82.25B TWD / 45.66% | 2026-09-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：強勁。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AAPL：新聞直接提及「Apple」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：強勁。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [10月台股主角 第一金投顧：AI 需求強勁 半導體擔綱 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1UM2tMdW5wcVZPV3pDeGRSRlNRajlsb01zZ2VMcHM0RlFkQlF0ZXNUTnFyc05ubFFuQlJ0SkRhclZ3STM4dGxvYmlMdHhLZnF2M0FsWmNTQWtXZ9IBX0FVX3lxTE5GMnpLRE03dTFvYlk4WG0tYlBZSV9BWkUwcDY5ZDEtMFltODFQTHBmSU92QjA1bldVSG9TanJneWpnWUNuVndXM1R5WFd5cHJRdE9BTnQ4NTBqODNwRi1J?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 09 Oct 2026 00:44:00 GMT
- [Elon Musk Reaffirms Control Over Terafab AI Chip Complex As Intel Remains Involved - Yahoo Finance](https://news.google.com/rss/articles/CBMinAFBVV95cUxNN1RGRHZZNWo2UWpwTndHWUNZam5WMlhYRFVoYzJKQ2Z5ZnRCTFE1aDVaUUhGeU9hYkxndUF1VGlHY3hYcXFGNi1lTkRxaXFURTUyOXZNcWlQVDRXbUR1QkdwT3pURE5WQV94NnE2TC1jdzZPREZ5dzdxSnVUZ0JjeWhrbjVmSmxFNTFhbWhkSjdXSXZuajMwWFFiMlM?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 08 Oct 2026 12:43:20 GMT
- [三檔 AI 流量股誰值得買？名嘴 Jim Cramer 獨推 Akamai - TechNews 科技新報](https://news.google.com/rss/articles/CBMijwFBVV95cUxNcmZtUWhCREMxZjRRNG1OSUFTOVhHb3dweEZLQkZ5MmFXVnk2bVEyQVo0aHBXNmQ3VDhoMVJyUEEwdDhjZm9SaHB2SlZKVDZyaU1PSXZKT3l1TW9YZmhfT0xVMnd1aEpfb3FRREg0RVZPVGNEZTdWQ3pFbVh5ZldmcXVnbGs4REhRdmd4cDExTQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 09 Oct 2026 01:30:28 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：10月台股主角 第一金投顧：AI 需求強勁 半導體擔綱 - 經濟日報；AMD vs. Intel: Which Chip Stock Has More Upside From Here? - The Motley Fool；AMD vs. Intel: Which Chip Stock Has More Upside From Here? - The Globe and Mail

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.28 | -6.63% | N/A | 107.08 | 114.68 | -6.63% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.57 | +20.26% | N/A | 620.68 | 645.86 | -3.90% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.57 | +4.39% | +15.19% | 230.48 | 237.47 | -2.94% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | +0.25 | -2.75% | -4.66% | 360.14 | 446.77 | -19.39% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.04 | -0.97% | +1.59% | 2,550.00 | 2,585.00 | -1.35% | 未明確 | 86.28 | 29.56 | 511.86B TWD / 54.65% | 2026-10-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.03 | -3.28% | -8.67% | 147.50 | 164.50 | -10.33% | 背離 | 6.68 | 22.18 | 25.35B TWD / 27.22% | 2026-10-01 |
| MU 美光 | 產業/供應鏈推估 | +0.04 | +6.68% | N/A | 1,035.84 | 1,088.00 | -4.79% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.02 | -5.56% | -9.97% | 1,609.46 | 2,335.00 | -31.07% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel、INTC」，共 5 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 4 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [10月台股主角 第一金投顧：AI 需求強勁 半導體擔綱 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1UM2tMdW5wcVZPV3pDeGRSRlNRajlsb01zZ2VMcHM0RlFkQlF0ZXNUTnFyc05ubFFuQlJ0SkRhclZ3STM4dGxvYmlMdHhLZnF2M0FsWmNTQWtXZ9IBX0FVX3lxTE5GMnpLRE03dTFvYlk4WG0tYlBZSV9BWkUwcDY5ZDEtMFltODFQTHBmSU92QjA1bldVSG9TanJneWpnWUNuVndXM1R5WFd5cHJRdE9BTnQ4NTBqODNwRi1J?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 09 Oct 2026 00:44:00 GMT
- [AMD vs. Intel: Which Chip Stock Has More Upside From Here? - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxNTW90STZZbFdiQlVsRkJCN0hCNXJTMEl0UHd6QlJMNWotcy10MDJkUWlUYWZtWE9JZ3l1R1dzMm0tOE9fSFRLYkU0VFlFeFF3WS1DamlLWkVVZWlJbVphOTQxVFVUb3lqc3k1UUo0cjM2Mks3dTFoVmM2bTBLSWtaTnFoaUVCa0wwTnpIbjRHbDhZclZDcWFnMw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 08 Oct 2026 17:30:00 GMT
- [AMD vs. Intel: Which Chip Stock Has More Upside From Here? - The Globe and Mail](https://news.google.com/rss/articles/CBMi1wFBVV95cUxQel9IUUJJNm9lTGN6RXU5cFFJTTVPMFdWa3dhMzhlZG00d1BOTXlEaUJXNEdCWllrU2RFS21SLTZFMU1Pc0oxOHpLd0RiZXkyTnF3aXVuRTdLSHY1QzBGalZoWmhQbUxqZUpqLUV6VXUtTWJneE9CNnhqSU9ZWVRORFNnYnNrR0JadXY2RGUtVE9jSjg1QVp2TkZZXzE4MXFYQzFXRVFxOGdoMGYzVG9fVzJ1akdVTDJEN1ZaRUw1Uk9QVmEtR3o2T2p4cWx4OVhISXpTRWllYw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 08 Oct 2026 17:36:50 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Sandisk Is Up 613% in 2026 and Micron Isn't Far Behind. Which AI Memory Stock Has More Room to Run? - The Motley Fool；Micron's DRAM Sales Reach $40B: Can AI Demand Drive Growth? - TradingView；AI Stocks Micron and Sandisk Are Up 460% and 1,190% in the Past Year. History Says This Will Happen Next. - The Motley Fool

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | -0.28 | +6.68% | N/A | 1,035.84 | 1,088.00 | -4.79% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.57 | -5.56% | -9.97% | 1,609.46 | 2,335.00 | -31.07% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +4.39% | +15.19% | 230.48 | 237.47 | -2.94% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、memory」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：risk, growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk、NAND」，共 4 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：risk, growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Sandisk Is Up 613% in 2026 and Micron Isn't Far Behind. Which AI Memory Stock Has More Room to Run? - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxPbktRQm9WOXZlQmN1d3dITVNQYk5FbUh6RERNdlNaUzRNUmVpbTlpMHltM3FHNU04WVo4dlJ5NmJqTnVnYzNVVFlvdVZFeUZSUmE0ODNpMW5vSnptdUUxbWg1eDgzSklFblBYbDdTRzdsVzR5X0tmbWk1bnpHZTNkNDBfWlpHZWQzbjhrVmF6djR5dnBjbGd3VA?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 07 Oct 2026 10:15:00 GMT
- [Micron's DRAM Sales Reach $40B: Can AI Demand Drive Growth? - TradingView](https://news.google.com/rss/articles/CBMisgFBVV95cUxNUlA0VWplanZfaF9oazVsbTQybFBMVFdDeHQ4aGMtVkVpTlhxb2lkb2ZfV2N2c3N1dEdHWWlTNllRVkM0MFYwV0dhdWRnRUJIOERGMGdjcm9iblRnR0FGQW10eklTOFVPWUpuZUY2QWFLb3BkUW1XWER3Qk11WVotRFF6bTJBSHc4VWVTbnhWOHI3QUNBWXhnZzJqTGt3VWl1Z2JyX2RrQ2dfOHhoNThtUWdn?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 08 Oct 2026 12:58:00 GMT
- [AI Stocks Micron and Sandisk Are Up 460% and 1,190% in the Past Year. History Says This Will Happen Next. - The Motley Fool](https://news.google.com/rss/articles/CBMilwFBVV95cUxNazU1Y05uLUpNU3ZkelQ2VkNyUktJdm0xV0dlRGxqaXJKWmlldGotcFEyN0pkV2xQbVY0NkY3akdPM25TOGpVenoxY215cTNfbGJaMTNpLXBsclNCQU5MQ3VyR18tdnF2dFY3ZkF1OXdCbHg3LURvZGZsMDRBMXdSRERvVWxDTVFnZmdUa2Fzbk1MWlVKNWNB?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 07 Oct 2026 09:48:00 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：散熱廠Q3營收皆創高，Q4盼續成長 - 台視全球資訊網；焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.26 | -4.04% | -1.99% | 3,440.00 | 3,545.00 | -2.96% | 背離 | 75.13 | 45.85 | 21.02B TWD / 44.92% | 2026-10-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 2 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：跌停, 成長, 創高。

### 主要來源

- [散熱廠Q3營收皆創高，Q4盼續成長 - 台視全球資訊網](https://news.google.com/rss/articles/CBMiqwFBVV95cUxPOGFiQlctcjF4Qi1KQ25ZNjk2RXpudHljWG9IekhkQ09zQ2k3SGhCeWxvRXBJRnZXQm0ydXlBZVc5Q0FZbWR2Rl9DYjN5YXpDbjlabkxJQ3VWVzduTVU0WllpMlFPbXVMQUlIbUdERFBJQWljYWpsUjByUnNieXM0NmFpTlNyYUh5MjJhRjBvX2tGMmxfTUxwcjlhRnZfbU5rU0ttZ01iRzExVlU?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 08 Oct 2026 03:50:53 GMT
- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 08 Oct 2026 03:35:00 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：個股動態報導內容-F7704B07-D7DE-488E-B38C-0C1A418F6245 - MoneyDJ理財網；《台股盤後》量縮收跌492點、失守5日線；週K連四紅-新聞內容-基金 - MoneyDJ理財網；個股動態報導內容-51395381-C25B-4899-92BE-7E33DD223C2A - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-F7704B07-D7DE-488E-B38C-0C1A418F6245 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilAFBVV95cUxNdDBnZk1IMWx5ck1URjgxQWR0Z3AxbHZvbWdZSzJPZ0pFMi1TUmY0TmtubWxvSXdmSHREcXNxTFh1X3lYRnFOSFlOZnRoNTJkWnItc2dTWDFKNHpwQV83YzFTM28yMVk0MnM4U3E1Mk9fSzdiNTYxYl9yRGVyZkpWVTM4N0FqWUFoOGxHYlp0WkpjU1NB?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 08 Oct 2026 22:06:07 GMT
- [《台股盤後》量縮收跌492點、失守5日線；週K連四紅-新聞內容-基金 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikAFBVV95cUxOS3RuckcydUZqRlRpMlVwU29neVY3eGRaYm82ZGpFSUhMenpFdHJnX21DYXhmd2lhM3RHZDJKaEsyWHppUkk5TjBBTnNXTkRaM1EwbDhDNjF5aEtrd1ZjOHJzTGtRcWw1cnN4dmhqeWtQM1RvUG5jSnBnU1VZT0Y5a3MwcUhBVWtfUm5ZV2Z5blc?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 08 Oct 2026 07:56:00 GMT
- [個股動態報導內容-51395381-C25B-4899-92BE-7E33DD223C2A - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilAFBVV95cUxQSlVrYzRuYUpwQzZObjMxS1RzOUx5Y0dPbEptOE9HbzZ3M1VPRjZTaTNubUc4WkZtOXh3R0ZUQm5lS0o2VDF1bjRFTDRjVlFSdlVRSzExTXlNa3l4UTNaOExRRk16cFNkR2lSMko1ZDg4NzlMLVNCSEVybmc1eTZiR3BGTnRCZU01XzktdFVzUTMtQUNm?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 08 Oct 2026 17:17:32 GMT

## 新興題材：群聯9月營收

摘要：新興題材：群聯9月營收 相關新聞集中在：群聯9月營收狂飆370％大炸裂！董座潘健成曝幕後「最強神助攻」 - Yahoo股市；群聯9月營收連十月創高；AI應用占比已逾半- 新聞 - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [群聯9月營收狂飆370％大炸裂！董座潘健成曝幕後「最強神助攻」 - Yahoo股市](https://news.google.com/rss/articles/CBMi-AJBVV95cUxOME9OaklBX202dlk2ckNDMWZMbTRuWnA0bU5RYVBPZ3hKU0pqQzBKUUk0aHB4LU50NGJHbVU0enktay1neFpwdUN4cEhIZUo3MDh4NlYyQ2xLV0NwYXZxRXJCc1k5VFM5RGJmR2pKSkNxdUFPbzJHaFNrbEZ5QzFQdzBHT0VWMFJvaXgza29fOS1WZzRkRTdLQmJKMm1SQVdteHB4LTYwRTZ5b3EyNFNQbmRrZGVmSGVKRmNDZzZkWWpEdW1BenJwSmxGU3ZqaXQzbjQ3STI4SlpfUktvYnJiRmhkMUJUS0w5MWNlaFQwaGxvZ29RaXg4YldQcG9MUjdFanhWRFhhSVE2NmRVUjdKN1RaM3RHbnhGZkVvS0QyclVNNjJ0LVVQd0RVaEo3UzlBeXFnaEc0emQxZ1BIeks0Tkdkc2NFYmRURnV2S0YxanB0dE9aZHJBUVBUbnluYXpSTTVPLXpFZk9NYnNneGVMc1FScjl4dkgw?oc=5) - Google News source discovery | Yahoo 奇摩股市 Thu, 08 Oct 2026 07:32:43 GMT
- [群聯9月營收連十月創高；AI應用占比已逾半- 新聞 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikgFBVV95cUxNZElPZEd2RVp3V0VFdldjcjVScXdTYkFoYV81a3M3LW1uWnJSTll0Ni01M3J3VUNGRTNhLXpSSkJvSHM1MUlLNHdtM18yZWRVMy1XTnZaV3FEQmZLVi0ybm5tU2M4clRaS0o4UG5GM2VtOVJOeHZCY245dDU1Uk93bkNWQU03Z3M0RWVZaW5tWHpwQQ?oc=5) - Google News source discovery | MoneyDJ Thu, 08 Oct 2026 07:54:00 GMT

## 新興題材：B7201AFA

摘要：新興題材：B7201AFA 相關新聞集中在：個股動態報導內容-B7201AFA-69F9-482E-A03D-6611F0356F66 - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-B7201AFA-69F9-482E-A03D-6611F0356F66 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilAFBVV95cUxPSXRXSHl1djB1MGp3NkFaNDR2a1BWNHRpQ0RCUEJ1ZFhnbkwzYl9YSHA0WE5RX1p5OFlDdmpxLTNYQlczSTJfS1JZWWkzODNzVldQTUgtb3pIZGZCMUk4UFN6VTFIWnZiR21JRVBkaERUMnRfamhoRWxIcHVKN3NOSERnNDdGdHpIbE1tcU9nRXUzcVVx?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 08 Oct 2026 12:21:10 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
