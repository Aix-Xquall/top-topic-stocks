# 每日股市熱門話題分析 - 2026-11-28

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **利率與成長股估值**｜中性｜熱度 3｜市場確認 100.00｜同向 1/1
2. **關稅與供應鏈轉移**｜正向｜熱度 3｜市場確認 N/A｜同向 0/0
3. **半導體與晶片供應鏈**｜中性｜熱度 4｜市場確認 N/A｜同向 0/0
4. **新興題材：BigGo**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0
5. **綜合市場情緒**｜正向｜熱度 37｜市場確認 0.00｜同向 0/1

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.24（樣本 13）
- 5日相關係數：-0.67（樣本 11）
- 同向比例：2/13

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 利率與成長股估值 | 100.00 | 1/1 | 0 | +49.95% | -41.52% |
| 關稅與供應鏈轉移 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：BigGo | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | 0.00 | 0/1 | 1 | -2.24% | +9.00% |
| AI 伺服器與資料中心 | 0.00 | 1/8 | 7 | -14.72% | +4.03% |
| 記憶體與 HBM 供應鏈 | 0.00 | 0/3 | 3 | -24.72% | -22.25% |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-11-15 | -0.02 | 0.62 | +50.00% | 20 |
| 2026-11-16 | -0.30 | -0.27 | +38.89% | 18 |
| 2026-11-17 | 0.44 | 0.39 | +80.00% | 15 |
| 2026-11-18 | 0.27 | -0.38 | +86.36% | 22 |
| 2026-11-19 | 0.20 | -0.23 | +69.57% | 23 |
| 2026-11-20 | -0.35 | -0.36 | +69.23% | 13 |
| 2026-11-21 | 0.04 | 0.04 | +65.00% | 20 |
| 2026-11-22 | -0.11 | 0.38 | +70.83% | 24 |
| 2026-11-23 | 0.26 | -0.36 | 0.00% | 6 |
| 2026-11-24 | -0.41 | 0.30 | +3.70% | 27 |
| 2026-11-25 | 0.25 | 0.11 | +50.00% | 26 |
| 2026-11-26 | -0.31 | 0.08 | +36.36% | 22 |
| 2026-11-27 | 0.15 | 0.36 | +43.75% | 16 |
| 2026-11-28 | 0.24 | -0.67 | +15.38% | 13 |

## 歷史回測摘要

- 回測日期：2026-11-28
- 近5日 3日相關：-0.03
- 近5日 5日相關：0.12
- 同向比例：+33.33%
- 權重狀態：未調整

- 方向準確度：+33.33%
- 信心排序準確度：-0.03
- 診斷：低相關

調整原因：近 5 日有效樣本 12 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：利率與成長股估值 相關新聞集中在：AMD Shares Rebound 2% as Chip Stocks Rally, But Valuation Worries Linger After Erste Downgrade - BigGo Finance；AMD Rises 4% Despite Erste Group Downgrade on Valuation; Marvell Climbs 6%, Intel Gains 5% - 24/7 Wall St.；台股現在是「甜甜價」？多頭總司令張錫開示：台積電2年拚5,000元、聯發科估值曝光- 證券 - 工商時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AMD 超微 | 新聞直接提及 | 0.00 | -17.74% | N/A | 424.54 | 516.10 | -17.74% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | -0.45 | -49.95% | +41.52% | 57.40 | 114.68 | -49.95% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | 0.00 | -2.24% | +9.00% | 2,180.00 | 2,480.00 | -12.10% | 不適用 | 98.27 | 22.19 | 586.89B TWD / 59.71% | 2026-11-01 |
| 2454 聯發科 | 新聞直接提及 | 0.00 | -9.14% | +9.85% | 3,680.00 | 4,920.00 | -25.20% | 不適用 | 62.35 | 59.19 | 55.03B TWD / 5.77% | 2026-11-01 |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +9.46% | +0.17% | 492.85 | 507.29 | -2.85% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 方向判斷命中詞：downgrade, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 方向判斷命中詞：downgrade。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。

### 主要來源

- [AMD Shares Rebound 2% as Chip Stocks Rally, But Valuation Worries Linger After Erste Downgrade - BigGo Finance](https://news.google.com/rss/articles/CBMidkFVX3lxTFBFY2lwdUxPbWU2THNDNlh6enpGdlFVLVMxX2gwSWtyLUJxOWpzRlA1OERWMUtCU2VGVVJ1YXFheERIVnVsYi1JWVBIQVFfZmJyRkhhMHVpZElyc3NlVjA5emZZMThyRXFLSFhJcWFGR0FYdGV0bkE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 27 Nov 2026 17:55:00 GMT
- [AMD Rises 4% Despite Erste Group Downgrade on Valuation; Marvell Climbs 6%, Intel Gains 5% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiyAFBVV95cUxQUTZqbXgxYXAtN1NPM3AyaGV2Z01KeWxfSkVxdU0tdUhlOWNjU04ydzM3c1FpLW1xZEdFbGhGU2VvckFPcjhUbGV0WTBuRFBnY1Vldm5rWF9XOFp0WnAtYlExYW5MWEtOWnhVUGpTM05yWTVHN01fczNYbnZEak9xVkJ4cmI3eEM1TndVSlNERjhpZ0NsWlh2QWJ1azVNWmd5cnZYemR0ZWYxZmVBbFJyaXJGUkhmTFdlelVtRlk2SUo1RGFlc3lnWA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 27 Nov 2026 14:02:00 GMT
- [台股現在是「甜甜價」？多頭總司令張錫開示：台積電2年拚5,000元、聯發科估值曝光- 證券 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTFA5U3ZicFJ1WUlhUU14YmlzcmctbFNkNXNEWk54b05MNWM0UjFmMmlJNm1jeFY1dFI0eU1PLWY3bTliNnlXUE01NGZmX1pFOF9FcmtjRnIyUmtvdGg2R0lN?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 28 Nov 2026 00:35:00 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：美擬對馬來西亞課最高18%關稅 學者估半導體投資影響有限 - 中央社 CNA；荷蘭抵制美國新規！反對擴大半導體曝光設備對中出口管制 - 鉅亨網；美擬對馬來西亞課最高18%關稅學者估半導體投資影響有限| 國際 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +14.89% | +28.58% | 358.54 | 358.54 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | -3.31% | +4.29% | 219.00 | 289.00 | -24.22% | 不適用 | 16.57 | 13.25 | 1305.32B TWD / 45.73% | 2026-11-01 |

關聯理由（前 3）：
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [美擬對馬來西亞課最高18%關稅 學者估半導體投資影響有限 - 中央社 CNA](https://news.google.com/rss/articles/CBMiV0FVX3lxTE10MmtNWVl5Zm1YS1ZKU3ppenpDMVFyS2Y1X2wzZlVDc3ZtUVhfZTRBUGxNNWx0SVJZSVlFeVZ0RVJmbzJ1OVkxVXJabHh6QlZmekhtRVBuMA?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 27 Nov 2026 09:25:18 GMT
- [荷蘭抵制美國新規！反對擴大半導體曝光設備對中出口管制 - 鉅亨網](https://news.google.com/rss/articles/CBMiT0FVX3lxTFAwMDE1X2lwMVZFbkdVMUY1eFdHOU14VGwzcHFhMDVVeGJVM3VMbTQ1RGRBbDlXc0ZVV2NrR1FNeEtQd3RhU0pzWEdCbjI2NTQ?oc=5) - Google News source discovery | 鉅亨網 Sat, 28 Nov 2026 00:43:13 GMT
- [美擬對馬來西亞課最高18%關稅學者估半導體投資影響有限| 國際 - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5vcDdGR2RWTVRsbjg4ckYzQ3BnUERSbVIwYzVoVEx1dG9JSFdPZmthY0xHNDJYdTl5MzhZSUZkZUQxc0pIenVZOUE5WnphWkttVVNqLUJqTmpFUWsyX21v?oc=5) - Google News source discovery | 中央社財經 Thu, 26 Nov 2026 12:51:00 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：通吃 AI 晶片測試與日系航太專案！英柏得科技預計 12 月中掛牌上市 - TechNews 科技新報；美半導體股遭血洗 韓國散戶急撈底、狂買 SOXL - TechNews 科技新報；美出口限令加速轉變！瑞銀：中國產 AI 晶片 2028 年市占率將突破 88% - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | -49.95% | +41.52% | 57.40 | 114.68 | -49.95% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -2.24% | +9.00% | 2,180.00 | 2,480.00 | -12.10% | 不適用 | 98.27 | 22.19 | 586.89B TWD / 59.71% | 2026-11-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | -9.89% | +8.97% | 87.50 | 164.50 | -46.81% | 不適用 | 6.80 | 12.92 | 25.20B TWD / 18.33% | 2026-11-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -34.11% | -25.04% | 150.49 | 228.38 | -34.11% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | -17.74% | N/A | 424.54 | 516.10 | -17.74% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | -33.37% | N/A | 646.95 | 971.00 | -33.37% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -6.67% | -19.45% | 94.39 | 291.88 | -67.66% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -11.06% | -19.76% | 312.34 | 446.77 | -30.09% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 CPU, server CPU, x86, foundry；其中 1 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 1 篇新聞出現相關標籤。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 1 篇新聞出現相關標籤。

### 主要來源

- [通吃 AI 晶片測試與日系航太專案！英柏得科技預計 12 月中掛牌上市 - TechNews 科技新報](https://news.google.com/rss/articles/CBMieEFVX3lxTFBnZkNDSUpBV09tYVF0TzFJZ2RPWTg2TG84NHJrXy12QW1CUnl6azlFLW9GRTYwRFJjeHdJTjB5S2h2R2h3OUJ5NlpnWWtyYVZZUjAyMExxV0hDc1otd1BIVHNsVXBBOXoyS3o1c3ZzTm5XbDdaZjgwbw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 27 Nov 2026 07:09:51 GMT
- [美半導體股遭血洗 韓國散戶急撈底、狂買 SOXL - TechNews 科技新報](https://news.google.com/rss/articles/CBMirwFBVV95cUxNZDU1RVk5NlNGcnJFV0pXSGlFa3FYZC00TkstLVlNZXlRa1RJZjlqeDNzREVoQjBGRWE0ZHJnUWFfZWVsd1ZTM0tLcUZ5djNxN0xNbDQ2QzU1aG9wWjBJVWZDTFJaMzY0aUZ6ZFN3dHUtRTJOWllWUGNObXpRamUzM2Vhc2xJV0pHdDFWd0pYX3VrM0tYZnZhd3hvY1AwZHdEX2FIZVpXTV82eWo1SG80?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 27 Nov 2026 05:55:32 GMT
- [美出口限令加速轉變！瑞銀：中國產 AI 晶片 2028 年市占率將突破 88% - TechNews 科技新報](https://news.google.com/rss/articles/CBMiekFVX3lxTE8wRDFSZHBFV3o5VE9PMjdvNC1ocmpWdlNoaXduM3VxcGRkb1h6S1pfZ2otdTZTQmdRaFN6M0dlZ29LNlN1TEI3cnFOWEdTNVR6QnJNbFFzUVR1Y2VoTTAySWlzbUY1eGpwbnAxd01hVW0yREVzaUZRdEhB?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 27 Nov 2026 09:12:44 GMT

## 新興題材：BigGo

摘要：新興題材：BigGo 相關新聞集中在：AMD Shares Rebound 2% as Chip Stocks Rally, But Valuation Worries Linger After Erste Downgrade - BigGo Finance

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AMD 超微 | 新聞直接提及 | 0.00 | -17.74% | N/A | 424.54 | 516.10 | -17.74% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 方向判斷命中詞：downgrade, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AMD Shares Rebound 2% as Chip Stocks Rally, But Valuation Worries Linger After Erste Downgrade - BigGo Finance](https://news.google.com/rss/articles/CBMidkFVX3lxTFBFY2lwdUxPbWU2THNDNlh6enpGdlFVLVMxX2gwSWtyLUJxOWpzRlA1OERWMUtCU2VGVVJ1YXFheERIVnVsYi1JWVBIQVFfZmJyRkhhMHVpZElyc3NlVjA5emZZMThyRXFLSFhJcWFGR0FYdGV0bkE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 27 Nov 2026 17:55:00 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股可以買了嗎？分析師點名必買這8檔 - 經濟日報；法人喊台股跌深是王道 16檔買盤力捧二低一高股 將帶頭突圍 | 市場焦點 | 證券 - 經濟日報；台積電硬撐台股翻紅！三大法人仍賣超213億元 本周提款2,916億元 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | +0.27 | -2.24% | +9.00% | 2,180.00 | 2,480.00 | -12.10% | 背離 | 98.27 | 22.19 | 586.89B TWD / 59.71% | 2026-11-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 2 篇新聞命中。

### 主要來源

- [台股可以買了嗎？分析師點名必買這8檔 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1JX3h1RDctSHcxc1hNNUtHTUE5OUpJTGFsdDhVZ01QVjlfUTFDUGVnUC1raEE0OGRvOGdQZmdYdGdPcTEtVlhIVXM3UW5ZWUZmSW5JRnJRNk4yZ9IBX0FVX3lxTFBHNmxGZEdHSnFUcUw2TkJyVVY1LVZTaXhxUFFzbk45R3ZJQ2dPM2M4Tm03MmI2NVJTOXhWeHVwTWp6Tlpoa2dCdXZsVGhRbGVIYVNZQXBCTkN1NjRMNTdJ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 27 Nov 2026 08:00:00 GMT
- [法人喊台股跌深是王道 16檔買盤力捧二低一高股 將帶頭突圍 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1qa08xQV9pVTNRa3diVUlLSEtSaVlFZDdzU3dQMEJIWlFmVDhKYnYxb01paDlrQ2tVYW5VNER4am1aSm1ObVRIamQ3MlZ4Q1ZhUnRmNmxtWkN5UQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 27 Nov 2026 19:21:41 GMT
- [台積電硬撐台股翻紅！三大法人仍賣超213億元 本周提款2,916億元 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE0wWE5zWVA3V1VaNXBrSmFfeXp3TjZBOW9mVk9FcG82akpYRTRfR0NfOHNRS2FvV3U0bXZBb19nX0ZjQ0ROeUR6cFFxS1BuVnNvQnE5SDA2c092Z9IBX0FVX3lxTE5DNTB0eUhVRHFJeFU0XzNRbnV1WkRwLW5EekhodDZucFR3cHhzeVVWWGZ4MmJfNHQxbkRyWVpUTDBPRzJXbGZZWmIyYnFVRXdkMU4zVFBPeWUzOFFyRV9R?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 26 Nov 2026 08:00:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：台股周線翻紅飆3,274點！碩禾奪漲幅王 AI 股誰出頭？ - 經濟日報；觀望氣氛濃厚 台股短線有壓 法人：待 AI 重整進攻節奏 - 經濟日報；Broadcom Makes More AI Money Than AMD—So Why Is AMD’s Stock Crushing It? - 24/7 Wall St.

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AMD 超微 | 新聞直接提及 | +0.28 | -17.74% | N/A | 424.54 | 516.10 | -17.74% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | +0.27 | -11.06% | -19.76% | 312.34 | 446.77 | -30.09% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 產業/供應鏈推估 | +0.04 | -49.95% | +41.52% | 57.40 | 114.68 | -49.95% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.03 | -34.11% | -25.04% | 150.49 | 228.38 | -34.11% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.03 | -2.24% | +9.00% | 2,180.00 | 2,480.00 | -12.10% | 背離 | 98.27 | 22.19 | 586.89B TWD / 59.71% | 2026-11-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | +9.46% | +0.17% | 492.85 | 507.29 | -2.85% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.02 | -3.02% | +12.47% | 514.00 | 703.00 | -26.88% | 背離 | 17.55 | 29.51 | 88.62B TWD / 47.13% | 2026-11-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.02 | -9.14% | +9.85% | 3,680.00 | 4,920.00 | -25.20% | 背離 | 62.35 | 59.19 | 55.03B TWD / 5.77% | 2026-11-01 |

關聯理由（前 3）：
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AVGO：新聞直接提及「Broadcom」，共 1 篇新聞命中。 同時符合主題標籤：AI, datacenter。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [台股周線翻紅飆3,274點！碩禾奪漲幅王 AI 股誰出頭？ - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1ETFh4ZUFJeUhpaXUteXRVVkVHazgyaEZ4TXZQOXlwNWRtbXowSjVzYnBPRExtOUMzTTBVZWJnNmZZajYyVUZscDJqN3dKY2ZnZ1U2cWlTU1I3Z9IBX0FVX3lxTFBRMjhUN0hPaUhXRHZlN3VZVjlHLXYteWtiZWp5NWNHZE5BTlB5QzNFOElCamYtUHRQQndWak8tTWRaUWJ3bHVBMFg4azI0SUpFU1dFQ3ZXVExvV0w2Yl9F?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 26 Nov 2026 08:00:00 GMT
- [觀望氣氛濃厚 台股短線有壓 法人：待 AI 重整進攻節奏 - 經濟日報](https://news.google.com/rss/articles/CBMid0FVX3lxTE5qa0JsZUwyQlVWVVNJWjZ3OWN6dkNZeXRuTE14dTdDX01mWFUyMkZ0VnpFS21kTl9NcW01dkUxLWg2b1NkeDduY3NGRXRPMjBvZXd6bUNaaWNpXzRyQm9wZ2tGWlVKbnpBQWVvTkpTZWpfS0taUU9F0gFfQVVfeXFMUEp3eTdhVUJ2RTkzRnFtZTZuRV90eDFacHVWVTlRQlJHZXhMNGZkOF9ueC1DM0p3ZUVMQTJSekRwTnNiMEZvV2NGb1Brb1lBQmpSSGxaaURlYVIzdXZjQkk?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 27 Nov 2026 08:30:35 GMT
- [Broadcom Makes More AI Money Than AMD—So Why Is AMD’s Stock Crushing It? - 24/7 Wall St.](https://news.google.com/rss/articles/CBMitAFBVV95cUxOSVlVaEZQaUJpeFNkUWc0MEEyQ1dWUG5vSDdYY0NQSkVPeVJBS2o2X0NFM0JXcFg1NWlTRkQxZVdFb2tzN0wtZ09QWDVrWm40eEJTaVVmaUNPMFY2cXRhOFR1Ml93eE9oVWtJY2sxMkhQc3FJamJqX0ZQMGpCUkJsWlFsam5EZTR0VUNmeW1YWGNzNy1sWVZ2dzZoeUU3SWZ0X2kzbTNoRnpPeklIeTlidS01dnI?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 27 Nov 2026 12:15:00 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Chip Stocks Surge, SanDisk Jumps Over 10% as JPMorgan Says AI Stock Selloff May Be Nearing End of First Phase - TradingKey；SanDisk Jumps 10% as Investors Return to Beaten-Down Memory Stocks; Micron and SK Hynix Rise 6% Despite TrendForce DRAM Warning - 24/7 Wall St.；Micron vs. SanDisk: Which Is the Better AI Stock to Buy for 2027? - TradingView

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.30 | -33.37% | N/A | 646.95 | 971.00 | -33.37% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.30 | -6.67% | -19.45% | 94.39 | 291.88 | -67.66% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.23 | -34.11% | -25.04% | 150.49 | 228.38 | -34.11% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、MU、memory」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：boost, growth, surges。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk、SNDK」，共 5 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：surge, surges。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Chip Stocks Surge, SanDisk Jumps Over 10% as JPMorgan Says AI Stock Selloff May Be Nearing End of First Phase - TradingKey](https://news.google.com/rss/articles/CBMi-AFBVV95cUxPbGJhWVk5RU9jVGw2Y2dPaHNHM2JQYXl2d1NBeDdxQ0ZBU3BvSWdOOTRmTHUyN2tobjBTS3NsOUhhWU10WXBWQzE2N0ZZQ1E3NUQ3SmxwTlc3LVE3d0FuWDU0ckVWTWs3YjNlWnNSVjJUcnZLcjVMV2xYRUZMM2NMTlJCN0Vja1djQmt6Q1luNEpENnE5WTYwX0ZHd0E5UUtrdGRwQ1YteU15dXpyZFN4YnVWd2RyN3luenBhUFNfOU9RaHJSRk5RUjRobWZ0amVfRm1JZ0h6MGxkSEg1ZnVUdTRETWN3dmduMmZNQmZyU1RQNzhNQ2R4aQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 27 Nov 2026 15:49:58 GMT
- [SanDisk Jumps 10% as Investors Return to Beaten-Down Memory Stocks; Micron and SK Hynix Rise 6% Despite TrendForce DRAM Warning - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi_AFBVV95cUxPYXc1djBnUlNucXVkS1RSVHM3bngxaVo4MXFTMHNKZVdsbzNyZlJULVphMlZRZlFwUngwd3Y1aVRNcDRoNzRTU1NyR2JfVk9jWHA2Qk9iTFBtNkdWQlRLaGpxTmV0WFJNczgxT2xSMTc5aGl1Tzhvdi1laHJRdGM3RVNReEE1aFVTQVVFWDRaaW5DYkpjZHoxRWFBMTktZU5BV3NmSVVaSlI3X284X01jWkg1bjB2WEFpTEo4TzdHOVJLbUNfVkM2UmJyeEhxMm0xRVhjaE9tdUdSWHhrVDRlbWlIZXJuZ0dLYWViaWhzNkRXRFRnT1c3UzZqOHQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 27 Nov 2026 13:58:00 GMT
- [Micron vs. SanDisk: Which Is the Better AI Stock to Buy for 2027? - TradingView](https://news.google.com/rss/articles/CBMivwFBVV95cUxObXNUNmhjMWtnTndOSUpVMmZibFpzZ1hYUFpraHBFU0xYWkpUcUxBWHdEYU96ZDE0TDZHdGVFWnBwUGVIWHN6ZXd0c2ZROGE4MjVhbVJFTDZLbUFqaEZwblVIYUlDLWRseWY1Z1JzSk9vcW1hRmdMblFLRnBtMmRrb2dUc3EyM2c1Qm5XZTFiclBXbkpielZBYk90bVRBQW1CcHh0aXNrZkNWWFItN0FjOU1ZQ3lGMVJ0WGJYTnhLaw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 27 Nov 2026 11:18:15 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》選前觀望量縮小漲156點；本週飆漲9% - MoneyDJ；統一證券：台股技術面已現築底反彈契機- 新聞 - MoneyDJ；國票證券：台股築底條件更成熟- 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》選前觀望量縮小漲156點；本週飆漲9% - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxOdWVrUzZzREV5d2FHanFzYmEzaDY2QXp5QXFsRjVxSXhfbzdZcTRudXI4TTN2TzRmdkhrUFUtUWlEbGRmNnZUdEtOMU5kVVRkWFo0Y0dYdUFpODJZcFdIQWFGaHphNElVUGREWnRSbDUxWVZLY3kyMW53OFB3bEpLR2JwQ3VpSlZET1RnNFYzSWVKUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 27 Nov 2026 07:53:00 GMT
- [統一證券：台股技術面已現築底反彈契機- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNQ202Zkd5RGZuTm5kSWlQRHZia1I3elBQWVlmQjJTbU9lQkZPVWdzVGhyMWk1QzJQbWlZZEpKS1VHQlFWbXpicUh6cDBEc2V3b1BFQW1mQWxCay0zejdvVEJ6ZkJWbldETFVlM2M0YndrQUM4c3dHREd0Nm53OHQ5cVV1UElGT09PSmI5bEFEZ0xpZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 27 Nov 2026 00:43:00 GMT
- [國票證券：台股築底條件更成熟- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxOWUF4Q2FudjRxUWRMdHlZZmJlSlJzZWxaT3hCVUU5OWNQS0xRQ2xTTEl1ajM5dndmcHNxRUtVVVFTMklfM2c0NHdEMWN5a1hRRzlHODNPS2w2a3JmY3R1YVlSdVd2dzc3N0ZBTGxZbWVPNjAzeHhUM21FM205SlV1dDFGajNRZlM5WDhnZUpVeW52UQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 27 Nov 2026 00:43:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
