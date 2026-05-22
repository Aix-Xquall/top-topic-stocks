# 每日股市熱門話題分析 - 2026-05-23

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **AI 伺服器與資料中心**｜正向｜熱度 10｜市場確認 88.33｜同向 5/6
2. **半導體與晶片供應鏈**｜正向｜熱度 7｜市場確認 86.00｜同向 4/5
3. **散熱與液冷供應鏈**｜正向｜熱度 3｜市場確認 100.00｜同向 2/2
4. **記憶體與 HBM 供應鏈**｜中性｜熱度 4｜市場確認 N/A｜同向 0/0
5. **先進封裝與 CoPoS**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.00（樣本 13）
- 5日相關係數：-0.05（樣本 13）
- 同向比例：11/13

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| AI 伺服器與資料中心 | 88.33 | 5/6 | 1 | +14.30% | +8.18% |
| 半導體與晶片供應鏈 | 86.00 | 4/5 | 0 | +13.47% | +9.18% |
| 散熱與液冷供應鏈 | 100.00 | 2/2 | 0 | +14.98% | +8.16% |
| 記憶體與 HBM 供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 先進封裝與 CoPoS | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：TradingKey | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 相關性偏弱；應提高同向價格確認權重，降低泛 AI、泛半導體等寬標籤推估權重。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-05-10 | 0.45 | 0.55 | +75.00% | 8 |
| 2026-05-11 | -0.03 | 0.47 | +85.71% | 14 |
| 2026-05-12 | 0.00 | 0.42 | +78.57% | 14 |
| 2026-05-13 | -0.08 | 0.07 | +58.33% | 12 |
| 2026-05-14 | -0.29 | -0.20 | +50.00% | 6 |
| 2026-05-15 | -0.17 | -0.08 | +58.33% | 12 |
| 2026-05-16 | -0.12 | -0.69 | +33.33% | 12 |
| 2026-05-17 | 0.09 | -0.34 | +40.00% | 15 |
| 2026-05-18 | -0.01 | -0.17 | +33.33% | 9 |
| 2026-05-19 | 0.04 | -0.01 | +62.50% | 8 |
| 2026-05-20 | 0.36 | 0.35 | +28.57% | 7 |
| 2026-05-21 | 0.28 | 0.52 | +45.45% | 11 |
| 2026-05-22 | 0.05 | -0.00 | +33.33% | 15 |
| 2026-05-23 | -0.00 | -0.05 | +84.62% | 13 |

## 歷史回測摘要

- 回測日期：2026-05-23
- 近5日 3日相關：0.00
- 近5日 5日相關：0.00
- 同向比例：+100.00%
- 權重狀態：未調整

- 方向準確度：+100.00%
- 信心排序準確度：0.00
- 診斷：低相關

調整原因：近 5 日有效樣本 3 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：AI 伺服器與資料中心 相關新聞集中在：How Intel’s AI Chip Pivot and Foundry Deals Could Reshape the Outlook for Intel (INTC) Investors - simplywall.st；2 AI Stocks Hugely Benefit From 'RAMpocalypse' (NYSEARCA:SPY) - Seeking Alpha；蘇姿丰：AI 是 50 年來最重要科技，AI 無所不在時代正式來臨 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.72 | N/A | N/A | 119.84 | 119.84 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.10 | +23.47% | +12.66% | 215.33 | 219.51 | -1.90% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.09 | N/A | N/A | 467.51 | 467.51 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.09 | +2.27% | -0.44% | 2,255.00 | 2,255.00 | 0.00% | 同向 | 74.39 | 30.32 | 410.73B TWD / 17.50% | 2026-05-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | -14.93% | -9.08% | 418.57 | 506.69 | -17.39% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.07 | +33.81% | +25.00% | 414.14 | 417.43 | -0.79% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.07 | +18.86% | +2.56% | 561.00 | 561.00 | 0.00% | 同向 | 10.86 | 52.09 | 62.25B TWD / 19.22% | 2026-05-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.07 | +22.35% | +18.40% | 3,860.00 | 3,860.00 | 0.00% | 同向 | 62.91 | 61.51 | 46.74B TWD / -4.14% | 2026-05-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：benefit。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：benefit。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：benefit。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [How Intel’s AI Chip Pivot and Foundry Deals Could Reshape the Outlook for Intel (INTC) Investors - simplywall.st](https://news.google.com/rss/articles/CBMiygFBVV95cUxQOXMwd0dJck9QVFNIV3I2ZHVnWHRqTExGMHRXREdNZ3dyRHA5ZlBYYjRhWjRpalF0Y3NYWDlnTUtNZi1GOUplaGZ6aGVBVUQxNld2UEdvVVN3UGdDSEQyX0w5R2lBYzBqYlB0SXJxcktWQkF5bWtSUnRERkZBNlpzNlIyZjRYeGp0bTZxT0FrOHZacXJNaVJ1c0NnYi12YlB4X0dLOUowdTdMcHB2Z1dsVUEyeTdzVVhjX2ZLUmtubldQU2c1YlJpcXh30gHPAUFVX3lxTE93MXF3eE9QczdVQ1pZQnJydnJ0ZWhDR2JLUjlXMlVaeURnZXNvcFY4bUpONi1jaE5NUHV2UHVNc2tESnpTYjN6WngzY3FZc3BXUzBtekQxZ3BQOHh1VHctQnM0cE56ekV3R2V1UFRhVlhHZ0dGRHFWY1g1S0YzdkpIWkZxek1VMk9qV1NwenNGQzNucDFEOWFkbGN5VWp2eWdrSXYtNHFkQUhKY2xzNURrTnFkNmF4UThlX3BfNkUxdUdkeFRyQzd2UWVMWmx2TQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 22 May 2026 10:45:18 GMT
- [2 AI Stocks Hugely Benefit From 'RAMpocalypse' (NYSEARCA:SPY) - Seeking Alpha](https://news.google.com/rss/articles/CBMijgFBVV95cUxPX2RJSTkzeE1xYkw0bThMSGk0UFhfQnBYbDVNeUlmR0dEcnYtU0tkZnhjY0tiYkJkWEFuQjJCbjMwRGNVcHpSWEExZkJyVzV3RUlqeXJnSXd4X0FhdTVRREMycHFoaUw0MzlNYWxvZnJ5UWUwdXlnbG1WdTJwN3RranFEUXduMVpNWE9GRjVn?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 22 May 2026 13:00:00 GMT
- [蘇姿丰：AI 是 50 年來最重要科技，AI 無所不在時代正式來臨 - TechNews 科技新報](https://news.google.com/rss/articles/CBMinAFBVV95cUxOaUE1T1VTZ1A0OS1DZUtjR24xd0RDc01WVHZId25BRm5RemRFZEUzWTh5YzFfNFNaeDMyZ01zaXhTa0VfejdaM1JnMHQ4THhXVHFmM0Jya08yaENaaWJ3blkzd21CV05sRWJJbkE3Mk1oX1ZSbUh1MmxETG9LdjVoUmM2T21zRUotUGM2bUo1Zmp6TlhxNFUtTnRsdGw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 22 May 2026 03:18:50 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：How Intel’s AI Chip Pivot and Foundry Deals Could Reshape the Outlook for Intel (INTC) Investors - simplywall.st；Forget Intel. Its Own Executives Are Cashing Out and This Is the Chip Stock You Should Own Instead - AOL.com；陸股劇烈震盪後反彈分析：AI半導體獲利了結陷整理| 兩岸 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.76 | N/A | N/A | 119.84 | 119.84 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.07 | +2.27% | -0.44% | 2,255.00 | 2,255.00 | 0.00% | 同向 | 74.39 | 30.32 | 410.73B TWD / 17.50% | 2026-05-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.05 | +0.88% | +3.64% | 114.00 | 116.00 | -1.72% | 未明確 | 4.00 | 28.64 | 22.66B TWD / 10.80% | 2026-05-01 |
| NVDA 輝達 | 產業/供應鏈推估 | +0.06 | +23.47% | +12.66% | 215.33 | 219.51 | -1.90% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.06 | N/A | N/A | 467.51 | 467.51 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | +0.06 | N/A | N/A | 751.00 | 762.10 | -1.46% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.06 | +6.90% | +5.05% | 1,478.69 | 1,562.34 | -5.35% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.06 | +33.81% | +25.00% | 414.14 | 417.43 | -0.79% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC、Intel」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 2 篇新聞出現相關標籤。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 2 篇新聞出現相關標籤。

### 主要來源

- [How Intel’s AI Chip Pivot and Foundry Deals Could Reshape the Outlook for Intel (INTC) Investors - simplywall.st](https://news.google.com/rss/articles/CBMiygFBVV95cUxQOXMwd0dJck9QVFNIV3I2ZHVnWHRqTExGMHRXREdNZ3dyRHA5ZlBYYjRhWjRpalF0Y3NYWDlnTUtNZi1GOUplaGZ6aGVBVUQxNld2UEdvVVN3UGdDSEQyX0w5R2lBYzBqYlB0SXJxcktWQkF5bWtSUnRERkZBNlpzNlIyZjRYeGp0bTZxT0FrOHZacXJNaVJ1c0NnYi12YlB4X0dLOUowdTdMcHB2Z1dsVUEyeTdzVVhjX2ZLUmtubldQU2c1YlJpcXh30gHPAUFVX3lxTE93MXF3eE9QczdVQ1pZQnJydnJ0ZWhDR2JLUjlXMlVaeURnZXNvcFY4bUpONi1jaE5NUHV2UHVNc2tESnpTYjN6WngzY3FZc3BXUzBtekQxZ3BQOHh1VHctQnM0cE56ekV3R2V1UFRhVlhHZ0dGRHFWY1g1S0YzdkpIWkZxek1VMk9qV1NwenNGQzNucDFEOWFkbGN5VWp2eWdrSXYtNHFkQUhKY2xzNURrTnFkNmF4UThlX3BfNkUxdUdkeFRyQzd2UWVMWmx2TQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 22 May 2026 10:45:18 GMT
- [Forget Intel. Its Own Executives Are Cashing Out and This Is the Chip Stock You Should Own Instead - AOL.com](https://news.google.com/rss/articles/CBMihgFBVV95cUxNaWdkSUVySmJGWWtvZXk5V0FLNW40OUNZRXNFRTFpSVhFd1ZILWhpZEpOc1dSejA3Q1dMR1NvX2otQlpRSzJJQmNyVVJhRUs0QUtLVU8yTmlJV2xuT2FXaDVWNVZzYjc4UnFXV01WNkpleURwd1ByWW9aTWEyZm9HSS1ZS2E2dw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 22 May 2026 13:22:33 GMT
- [陸股劇烈震盪後反彈分析：AI半導體獲利了結陷整理| 兩岸 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTFBpVHJTMmRMQU1qNDJBeC0xYWhNQ3JldkpnN3d6VEN2cmpFRTBuRU5lSkdrWFl5TklVdkhMQmt0em9RSGhsY0xocUNnZFNvWWNuMzdVZU1FVmJSYTZ3QUE?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 22 May 2026 09:21:00 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：輝達新一代 AI 平台 Vera Rubin 報到 電源、散熱鏈含金量大增 - 經濟日報；【最新消息】奇鋐Q1 EPS 20元亮眼題材延燒，「10檔散熱概念股」強勢上攻！ - CMoney投資網誌；雙鴻董事長林育申：「AI旺到2028年沒問題」ASIC勢頭很猛展望樂觀 - news.cnyes.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.67 | +6.49% | +3.67% | 2,545.00 | 2,835.00 | -10.23% | 同向 | 61.06 | 41.82 | 15.63B TWD / 71.62% | 2026-05-01 |
| NVDA 輝達 | 新聞直接提及 | +0.56 | +23.47% | +12.66% | 215.33 | 219.51 | -1.90% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱、奇鋐」，共 2 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：大增。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：大增。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [輝達新一代 AI 平台 Vera Rubin 報到 電源、散熱鏈含金量大增 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE16LXJSNWVzS1hIQXlmd3lNWmVwXzdTQmhpcjhMTVpIenhHU3I2Tk5QaXVBc0hyZVo2em83VE95OUl1UVlwMUZUN0ZzM1hjbnNLb252WlFXREVYd9IBX0FVX3lxTFBuaVRLMy1fQno0VWxmS2I4bmlxdWVsWXJPN3Z0YXZ6OE94R2hYMjVuT0FWaTktVWF4eVFsY2t6bjdQbzF0R0tOdkxESXFLNTVGQmROZXRGRHppdEh5S2xj?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 22 May 2026 05:00:00 GMT
- [【最新消息】奇鋐Q1 EPS 20元亮眼題材延燒，「10檔散熱概念股」強勢上攻！ - CMoney投資網誌](https://news.google.com/rss/articles/CBMifkFVX3lxTE5leWRlX3BVMWE0Z3dlLWJfX0VMamhrQ0cyeUxCeWVnTTZJZkU5WUQzYk55WEg5QTBGOVZhaXBnWVF3RlJOczJQTmljNjliOXk4R25XdFh1NGNIZnVzN2RJZUUtUmU0bW1mZHBqemNVQkZQWmFjVEViVGdZTUUyUQ?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 21 May 2026 07:08:41 GMT
- [雙鴻董事長林育申：「AI旺到2028年沒問題」ASIC勢頭很猛展望樂觀 - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTE9sSVZ5cG52T0habmdNUXdlZXEzOUEwV1hWelFNV2pqSmkycXRvVlpPZDJqRzRWTGJzc1ozcmJZMmpGWE5wTTZja1FtY1Z3bVk?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 21 May 2026 04:55:05 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：SanDisk Soars 9%, Western Digital Rallies 5%, Micron Rises 3% as Memory Trade Reawakens - 24/7 Wall St.；SanDisk Soars 9%, Western Digital Rallies 5%, Micron Rises 3% as Memory Trade Reawakens - Yahoo Finance；Micron Technology Inc Stock (MU) Moved Up by 3.60% on May 21: What Investors Need To Know - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 751.00 | 762.10 | -1.46% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | +6.90% | +5.05% | 1,478.69 | 1,562.34 | -5.35% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +23.47% | +12.66% | 215.33 | 219.51 | -1.90% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、MU」，共 3 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 2 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 1 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [SanDisk Soars 9%, Western Digital Rallies 5%, Micron Rises 3% as Memory Trade Reawakens - 24/7 Wall St.](https://news.google.com/rss/articles/CBMixAFBVV95cUxNZkhrZUMzSXFPODFuVFhtbUNjdGlNM0ZzdFZyYmtTY2JPQ1FENk9xZUhRSHpaNWpkOUdCazNzNDBoc1gyU0NXYk4xdEkxaE5FYVczSnZ4bkkxeUl1Y3dnOHpXcGdjOFpFYjdfVXo3dFhLa0gycURrUjBDMnFzN1dqZ0kxdjd0elVISk9WRXNUY2F6azNZbEI4VFRyV2ZRY2NWM1d1amx2UEtadFNZcWMzbGhqVk9IdlJZNTFVd0hwVWp4bWFO?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 21 May 2026 17:49:35 GMT
- [SanDisk Soars 9%, Western Digital Rallies 5%, Micron Rises 3% as Memory Trade Reawakens - Yahoo Finance](https://news.google.com/rss/articles/CBMinAFBVV95cUxNTVdJVFVsUWh0eHBwVDd2X3VVNDc1TGh5bEFpTWNDOVltblVFd09sZWF0YXlzTHU5MFZhcHROVUw2U1hXdDN2cXgzd3Vha3pGUmVhRUJwQ0ZjTmJwaS1OLVlkVHhGeWVRS2VFNVhILXVsUF9qMG04ZG5WaXY0U2hORndrT1ZJQnRlcHVOZmxlMGpGQzhjZHhYaDFQeGg?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 21 May 2026 17:49:35 GMT
- [Micron Technology Inc Stock (MU) Moved Up by 3.60% on May 21: What Investors Need To Know - TradingKey](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPZnVyQXplRmd6MlBoSkItX2dsRWJhX016bUVqX1FBRDRwTUtmanp6TEVYanNpZmFQS1hQemRhWnZqWlhYWktGLTlGQ3YxVUkxQTQtaTllTUZzUE5xZ1BrLWFjTlBqdHlFZExua1d3R0hXd1ZFemtHYm94TDFtOUxkOXBDNC1qTHpM?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 21 May 2026 14:15:31 GMT

## 先進封裝與 CoPoS

摘要：先進封裝與 CoPoS 相關新聞集中在：台玻攻玻璃基板新應用 - 經濟日報；AMD 點名台封測廠，扇出型先進封裝搶 AI 商機 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3711 日月光投控 | 新聞直接提及 | 0.00 | +18.86% | +2.56% | 561.00 | 561.00 | 0.00% | 不適用 | 10.86 | 52.09 | 62.25B TWD / 19.22% | 2026-05-01 |
| AMD 超微 | 新聞直接提及 | 0.00 | N/A | N/A | 467.51 | 467.51 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +2.27% | -0.44% | 2,255.00 | 2,255.00 | 0.00% | 不適用 | 74.39 | 30.32 | 410.73B TWD / 17.50% | 2026-05-01 |

關聯理由（前 3）：
- 3711：新聞直接提及「封測」，共 1 篇新聞命中。 同時符合主題標籤：advanced packaging, CoPoS, FOPLP, panel-level packaging。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「先進封裝與 CoPoS」關鍵字 advanced packaging, CoWoS, CoPoS, FOPLP；其中 0 篇新聞出現相關標籤。

### 主要來源

- [台玻攻玻璃基板新應用 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5KRmhaUS1Rc2E1V2lINXpFZ09LTTgxcDZETG1oZ1d1aXVNYmRZRkl5dmE4N2xvTXBmUktFaGN1dmQta3B3dExWYzZWa0ppSzdTbVduRUdUMlUwQdIBX0FVX3lxTE9mX2ZMbTBJZ3ZnY0hKSFM5eERDRXZqUlFMaEl2UGFrY09oUFlUYVhqdnM3ZzZZd1V0WnlYRm5XMWlYUDFxZ1dGMFg5OUtPM2xzTjBZQzJtMU1QVldXNS1B?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 21 May 2026 14:58:12 GMT
- [AMD 點名台封測廠，扇出型先進封裝搶 AI 商機 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiY0FVX3lxTE9rZk45dmZob1FrVG5pdVJlSUF4eUtvRWpEVWM4RXhQdDUyRV9wX3ozVlpCN2JkZF91d182QlB1eFEwbjlIdUFUdUp2S0gtS2dqZVNUUXE0bmt1NzhLd2FCOWhsTQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 21 May 2026 15:51:35 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Micron Technology Inc Stock (MU) Moved Up by 3.60% on May 21: What Investors Need To Know - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 751.00 | 762.10 | -1.46% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Micron Technology Inc Stock (MU) Moved Up by 3.60% on May 21: What Investors Need To Know - TradingKey](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPZnVyQXplRmd6MlBoSkItX2dsRWJhX016bUVqX1FBRDRwTUtmanp6TEVYanNpZmFQS1hQemRhWnZqWlhYWktGLTlGQ3YxVUkxQTQtaTllTUZzUE5xZ1BrLWFjTlBqdHlFZExua1d3R0hXd1ZFemtHYm94TDFtOUxkOXBDNC1qTHpM?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 21 May 2026 14:15:31 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：上班族都買什麼股？逾四成在台股賺到錢 人力銀行揭密：買「這個」最夯 - 經濟日報；台股雙王領軍 寫四驚奇 外資強補761.3億元 - 經濟日報；台股漲426.02點 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [上班族都買什麼股？逾四成在台股賺到錢 人力銀行揭密：買「這個」最夯 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTE54R3JfXzViMl9LQlpDQWpfMzF5QlVQeXpFVF82eUxsc0pVQ0FUM2hwazZKRG0wYmFobmNvV3l0VHM2bVFnVFZBRTdHX1lCVFpRdDYxMGRBOGNSQnFh0gFiQVVfeXFMUE85R1ltUTBldUJTbnJyYmtrQk5UMzl3eTZ6S2syd0M3Sk8ta2VoVU9NdHNZTjlKc05CZ3RIN1BnMWdxbHI0UWRNalROR0ViWnY1UG52V3FIWURzX0JTbFlfZmc?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 22 May 2026 04:22:44 GMT
- [台股雙王領軍 寫四驚奇 外資強補761.3億元 - 經濟日報](https://news.google.com/rss/articles/CBMidkFVX3lxTE9hOUdsSV9aeDVaOE5ySGJlVlV1cVZScFI3Umw4Z0lsOHIzeTVybUVDbHpCNC14NUlyZmJJUDVqcG5tWEVjZDFyU3FvTk55djdZU1paWFJXOWExRmVRNW5PQzF1THdDT2xqRzNpZGhSNjVVTkh0VUHSAV9BVV95cUxPSXdOal9RVEE4Z25vWFJPa3N4T29KRk5aS09CeHBYWWdfNmxHWWNrODVhc19JbDUwMG5ud3JYdUZtS1ZCN3F3QzNFMXNCMHdrQ0x5SjNvUkhDM2o0ekNSdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 22 May 2026 17:21:36 GMT
- [台股漲426.02點 - 經濟日報](https://news.google.com/rss/articles/CBMikAFBVV95cUxNZjB4SWpjU3RpRXdacHFEM0dKcFQ0VF9odzd1RFBNdlhGUFZoTGVnUHQ1RWhPZ0NQR1lUYmRsdzEtS2VNbDE0UkdkdzdHLXVyQ3Z5T3AxUnIwNnhkRXhRRG1HaHRES1hhWWRGMHZObEFFdnpLWXBfNzhMN2Y1V3RxRy16aGZEVEFFTDBwZzBtTlLSAV9BVV95cUxQODd5b1gtcmRYWjJTMEdRNWN3VElYZG1ZaG5USW9CYUJPZU96QndOa2o0ZkR4MnhDeFQ2eTBYdkk1OHMzVDFhRUFjRW94MWMtMjk0b2JWZG5aREM5Q29naw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 22 May 2026 14:14:12 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》大漲899點、首收42K；週K翻紅- 新聞 - MoneyDJ；國票證券：台股指數估挑戰42000點大關- 新聞 - MoneyDJ；統一證券：台股有望持續震盪盤堅 - 台股 - 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》大漲899點、首收42K；週K翻紅- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQdWRUZzlfQmQweXZjTXF0dl9MLUMxVEppYmlLeFVmVDZQLUpZZUZ3QTZWTWZGTUJuY0hYLVZxcXptS2IxZ3ctSXZhV0lJYmNQVUM3OUlXX2RJQWNJdXF3M1lxdjhUci1lM0ltUXh2ZE4xV0xINDRYdWVGcjRra2FoZGhWMDB2MWppUTZZakpEcEpVZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 22 May 2026 08:06:00 GMT
- [國票證券：台股指數估挑戰42000點大關- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxOU3M3bjRjY0NCcjV1RXFZaDZBcTZFVlkzcGw0NmRzVlY1M0hIaEh2c1NrLUVsMGFIamRyYkpMdW5yb21hLXhWRVNuVkl3RS16Vi1rVE5wd3RlaUNxSk5KZ2N2dGRGd2VHRVNHTjFjZWpZRUFtYms3M2FWRWhWVW1jRnBHUU81cjVmN2Nxc212Nmp3dw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 22 May 2026 00:44:00 GMT
- [統一證券：台股有望持續震盪盤堅 - 台股 - 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMimwFBVV95cUxQU0RpXzlWMmJaYW1MMUttYWZoaEQyQlAxaFBvbWJoWUZTRVpuLXR2dTBGb2hPdlJaNktCT3BFaGtIRkpsdlROT2FiLTJaOUhsZzFQQXNpU1QtQXJMLVFpbDRjNGw4RGJOVkZaX0YtekRsWnQ3WkVXWkNlYXFLMWx4UFdxMlF2U0oyMjk2SFZfbDlYUUxmX21XT1Itcw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 22 May 2026 00:44:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
