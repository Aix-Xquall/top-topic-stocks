# 每日股市熱門話題分析 - 2026-09-14

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **散熱與液冷供應鏈**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
2. **利率與成長股估值**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
3. **半導體與晶片供應鏈**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0
4. **AI 伺服器與資料中心**｜負向｜熱度 9｜市場確認 36.31｜同向 4/8
5. **記憶體與 HBM 供應鏈**｜正向｜熱度 4｜市場確認 1.91｜同向 1/6

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.31（樣本 15）
- 5日相關係數：-0.54（樣本 10）
- 同向比例：5/15

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 散熱與液冷供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 36.31 | 4/8 | 2 | +0.44% | +0.98% |
| 記憶體與 HBM 供應鏈 | 1.91 | 1/6 | 3 | -3.25% | -9.14% |
| 新興題材：OpenAI | 0.00 | 0/1 | 1 | -10.08% | -0.74% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價呈負相關；應檢查正負向詞庫，並降低新聞直接提及但股價背離的權重。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-09-01 | N/A | N/A | +50.00% | 2 |
| 2026-09-02 | -0.29 | 0.24 | +75.00% | 12 |
| 2026-09-03 | 0.10 | -0.10 | +54.55% | 11 |
| 2026-09-04 | -0.08 | -0.08 | +28.57% | 7 |
| 2026-09-05 | 0.13 | 0.34 | +54.17% | 24 |
| 2026-09-06 | 0.19 | 0.43 | +50.00% | 24 |
| 2026-09-07 | -0.15 | -0.09 | +53.33% | 15 |
| 2026-09-08 | -0.07 | 0.18 | +57.89% | 19 |
| 2026-09-09 | -0.28 | -0.12 | +54.17% | 24 |
| 2026-09-10 | 0.28 | 0.86 | +75.00% | 4 |
| 2026-09-11 | -0.01 | -0.08 | +25.00% | 12 |
| 2026-09-12 | -0.39 | 0.04 | +25.00% | 20 |
| 2026-09-13 | -0.42 | -0.14 | +17.65% | 17 |
| 2026-09-14 | -0.31 | -0.54 | +33.33% | 15 |

## 歷史回測摘要

- 回測日期：2026-09-14
- 近5日 3日相關：0.15
- 近5日 5日相關：-0.14
- 同向比例：+41.18%
- 權重狀態：未調整

- 方向準確度：+41.18%
- 信心排序準確度：0.15
- 診斷：弱正相關

調整原因：近 5 日方向與信心排序皆偏弱，降低方向詞與供應鏈推估權重，並加重背離扣分。；關鍵詞×公司後續樣本有效 0 筆，未達 30 筆，不調整樣本權重

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

摘要：散熱與液冷供應鏈 相關新聞集中在：散熱雙雄又要噴了？Rubin、ASIC第4季雙引擎點火奇鋐、雙鴻成長旺到明年- 產業 - 工商時報；焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | +2.59% | -5.60% | 3,370.00 | 3,425.00 | -1.61% | 不適用 | 75.13 | N/A | 19.48B TWD / 54.34% | 2026-09-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐、散熱」，共 2 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：跌停, 成長。

### 主要來源

- [散熱雙雄又要噴了？Rubin、ASIC第4季雙引擎點火奇鋐、雙鴻成長旺到明年- 產業 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1GSGVkS1BjdmdEazJZcE9fU2pyaG0xb3FEOUVSQ0Z3WXlTMXpvRnI1QnZVNWdaTXpRMkVDdlFqUmRBaFlhTWJZVU1DbElMdGQyMEJEMFppN01rS2hONC1N?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 12 Sep 2026 03:07:00 GMT
- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 13 Sep 2026 07:16:43 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：核心人才離職，對 AI 公司估值有何影響？ - TechNews 科技新報；美債殖利率攀升如何影響 AI 企業估值修整？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +10.08% | +0.74% | 495.63 | 507.29 | -2.30% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [核心人才離職，對 AI 公司估值有何影響？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiugFBVV95cUxQMFRFNzJxbEhfbVg3dUItZEQ3UXB4OTNXWjVDWldjNzROdkJBM3h2Ti1md2kxTGV0UlJXeW5RQUNhZjBBSC1NaHhuNkpZX0hRRVJCYUxlRzFZZk9LZ1VzbzVsanFLZ0dxam9mcWVaR3pKSW03eFFnQkM2VF9PMWpUUm83cGltaERXUE9pek9yZlIydkVmMFFySmVIWW9yVW5hNEpPM3RidEtuV0c0WC1jaXlYYmRhSkQ5QXc?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 13 Sep 2026 19:43:54 GMT
- [美債殖利率攀升如何影響 AI 企業估值修整？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMicEFVX3lxTE0zODlWVDFyUzFaNEx4YmlhdWRlOXR1Tl95cWwzWnphWjlzY2VYTDA3SFJGaVg3WWlEX0pLWVNxYjZfbmpiWGhyYVdFdml0VmhRbGMwdUhBbWE3ak1mZDkzc1d1eVEySWVDMkpVd0hMZWM?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 13 Sep 2026 19:15:51 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：賴總統頒褒揚令肯定黃崇仁為半導體產業開拓者| 政治 - 中央社 CNA；衝刺CPO、半導體！彭双浪喊砸錢友達集團齊衝「這檔」股價飆到三位數- 日報 - 工商時報；政府應開創半導體設備國產化之路- 日報 - 工商時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | -10.24% | N/A | 102.94 | 114.68 | -10.24% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -2.43% | 0.00% | 2,410.00 | 2,425.00 | -0.62% | 不適用 | 86.28 | N/A | 514.81B TWD / 53.32% | 2026-09-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +2.55% | +8.08% | 140.50 | 164.50 | -14.59% | 不適用 | 6.68 | N/A | 25.04B TWD / 30.71% | 2026-09-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +8.74% | +3.39% | 218.29 | 220.78 | -1.13% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | +0.01% | N/A | 516.13 | 516.13 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | +0.44% | N/A | 975.26 | 975.26 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -6.02% | +5.04% | 1,633.35 | 2,335.00 | -30.05% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -7.01% | -18.98% | 361.99 | 446.77 | -18.98% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 CPU, server CPU, x86, foundry；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 0 篇新聞出現相關標籤。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 0 篇新聞出現相關標籤。

### 主要來源

- [賴總統頒褒揚令肯定黃崇仁為半導體產業開拓者| 政治 - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9IM21aWWVSWUY0dE1aQTdfZEYwZkptdnJrelEyTEV4eWF6OFRNZzI3MjBOb19vay11UGY0bTRIQl9DS2Z4bnpxUTd3c1RFX1Y2VFZseWF3YWxnMmc5NHF3?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 12 Sep 2026 05:30:00 GMT
- [衝刺CPO、半導體！彭双浪喊砸錢友達集團齊衝「這檔」股價飆到三位數- 日報 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1mZnFaSkNvVUdacW1UMU5UZDFMbnRfYUdSNzZ3dU55OU9hUi0wSGVzOURVMjFKRkRlZTU1RENMcEFycU9TWFg4cGhxREdLbHZIeHZSNGFpVkdaZElwb0JB?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 12 Sep 2026 19:00:00 GMT
- [政府應開創半導體設備國產化之路- 日報 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1TTXdZTFhYQzhnMlBwSnlfS2FuR3FiZjQtNGJ6U1dUV05DRVpodHl3UWxpZ3Nqcms0WkZXYnQyQmx6WEV4cnUzLUJaS3FuUGRSWnJCYm45WUJzelhwTFVj?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 13 Sep 2026 19:00:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：養 AI 團隊比自己做還累？揭數位擴編潮背後的隱形工時與失控危機 - TechNews 科技新報；面對 AI 衝擊，教育體系應如何整合情緒教養以優化勞動力？ - TechNews 科技新報；Trump says 'very negative forces' raising exaggerated concerns over AI - Reuters

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | -0.08 | -10.24% | N/A | 102.94 | 114.68 | -10.24% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | -0.03 | +8.74% | +3.39% | 218.29 | 220.78 | -1.13% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | -0.04 | +0.01% | N/A | 516.13 | 516.13 | 0.00% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.06 | -2.43% | 0.00% | 2,410.00 | 2,425.00 | -0.62% | 同向 | 86.28 | N/A | 514.81B TWD / 53.32% | 2026-09-01 |
| MSFT 微軟 | 產業/供應鏈推估 | -0.02 | +10.08% | +0.74% | 495.63 | 507.29 | -2.30% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -7.01% | -18.98% | 361.99 | 446.77 | -18.98% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.03 | 0.00% | +5.10% | 618.00 | 680.00 | -9.12% | 未明確 | 13.92 | N/A | 82.25B TWD / 45.66% | 2026-09-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.04 | -2.65% | +3.85% | 4,585.00 | 4,585.00 | 0.00% | 同向 | 60.69 | N/A | 64.18B TWD / 44.08% | 2026-09-01 |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：slowdown, 衝擊。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：slowdown, 衝擊。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：slowdown, 衝擊。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [養 AI 團隊比自己做還累？揭數位擴編潮背後的隱形工時與失控危機 - TechNews 科技新報](https://news.google.com/rss/articles/CBMieEFVX3lxTE9ZenN5SzlwVE9DY000anRrOElnSnRLMFU0bmNGcnpNMXM5WXB4TlBUMV9HUnVpeGhKa29QMHQ5VHY1QkRRZktrQjhrVlpkbVg5djdsRkk1RFBlZnNCUW1mVmdmcU1PbE5DVGRhdDBvYVNrZjZtSmRYeA?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 13 Sep 2026 23:24:03 GMT
- [面對 AI 衝擊，教育體系應如何整合情緒教養以優化勞動力？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiYEFVX3lxTE40eW9qWWlFb2h3TTFwNzZjb05QQUpXQmZhZ0szUUNsTkV4VDlsQW5vNEl0em02WTVpVDFnaXN0OHQwcDlOM2NPMVhndVlOWU90RENPN0d5QlN4RzltUnBmbg?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 13 Sep 2026 20:47:51 GMT
- [Trump says 'very negative forces' raising exaggerated concerns over AI - Reuters](https://news.google.com/rss/articles/CBMiuAFBVV95cUxObThfSFpBRlQ0d1ZsVDV4SnZQdlJkYWZnRTlQRlpKWmRud283dWJQclhHQUUxM1dHSzVJakIxVnVBc2pYU0R2TmdUT01PSkJiY3I3WFRHUGNZNUh5RVdtRGk4QUppT1hVV0dHbDdwdGQzc0ZyZlRxeTUzNjg1UUY3RHpiR0JUOUpCdlV4b2xNd01FaEluMXhZZTA4eV9Gd0gxYW02eWprV05hRUREYWVGZUZLcHZWZWpa?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 13 Sep 2026 16:58:17 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits；Billionaire Stanley Druckenmiller Dumped Broadcom, Intel, and Micron for This Chip Stock. Here's Why. - The Globe and Mail；Prediction: This Artificial Intelligence (AI) Chip Stock Will Soar After Sept. 30 (Hint: It's Not Micron) - The Motley Fool

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.43 | +0.44% | N/A | 975.26 | 975.26 | 0.00% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.24 | -10.24% | N/A | 102.94 | 114.68 | -10.24% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.49 | -6.02% | +5.04% | 1,633.35 | 2,335.00 | -30.05% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.32 | +0.01% | N/A | 516.13 | 516.13 | 0.00% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | +0.21 | -7.01% | -18.98% | 361.99 | 446.77 | -18.98% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | -0.01 | +8.74% | +3.39% | 218.29 | 220.78 | -1.13% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron」，共 4 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：cut, rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「INTC、Intel」，共 2 篇新聞命中。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 1 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：cut。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。

### 主要來源

- [INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits](https://news.google.com/rss/articles/CBMi0AFBVV95cUxOWm5KdEIwSXpyY191UEhDa1V6NVpWa01UbmpJeWRIV0ttT080TmpDNEhISW5TWkQwUzBVYzBqSHJPWXRVNVJCampoWWRlYmhKVkhIeHBJLS0wLW5Ua09GQnRORXpFcW5qTEJkcnJGcW55aU5rOFVOLUFMbjRPZEpWT3A2ZllucnM0SU9JNEdrNUwyc3V2WHAtNFk3VHl4R1F6SkZRMFpleEE2Zl9MdW4tSEpMMnFGZ2hQZURWQ3B1WDlPR1BhRjJELVN5ODJWYVR3?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 12 Sep 2026 04:00:43 GMT
- [Billionaire Stanley Druckenmiller Dumped Broadcom, Intel, and Micron for This Chip Stock. Here's Why. - The Globe and Mail](https://news.google.com/rss/articles/CBMihwJBVV95cUxQVTRiZlJXR2JhMHdWU1pEaHBXOHlKcVFXNjFJOThTOWJqQjVHMUR4LWJJRDlkU2hVNjBuVXhXOHBJbkFCM2NyTGd4YUY1bzgzS0xTT3hBZC1RdWVmZFVMdTJmTFV0Y1NCcDdZZmlZNFZzTlE2U0xKQlRod0oxVDBiTW5KdkVURUhacmpfYVNGUUxTTGdYTjVZQmgyZ1NSS3Raay1UZzZyRmlXZnpQNXVUR0dkY09VbHpwZ29ZU05NTWRfNE5CUzFLNXZQT3FjaEZVUWJZaXVsdDlQN1VDOGRpNWhXMkp1TzY5NXVGajVST0xFcjNzZE15RDJBQUhraF8xV1JkZ2lGUQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 12 Sep 2026 08:43:06 GMT
- [Prediction: This Artificial Intelligence (AI) Chip Stock Will Soar After Sept. 30 (Hint: It's Not Micron) - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxQYmh5LXNaUGswaFF1T2w3UG8teTkxblRsS1prUlBaYUVlOTJSMWplZ0JSaDhyMUJjSGhhdXExT3hheGVKSVIwVXlLYkd4YnhJeURaeDkzWk11NDRhb255ZFVGOEM4eVRjNnVYNWhsNWxTQW1tX0ZTbjRMcTFxTkxPNEI2RE5DOUNiN0dRcmZXX1V6MU11TWNqaA?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 13 Sep 2026 13:35:00 GMT

## 新興題材：OpenAI

摘要：新興題材：OpenAI 相關新聞集中在：優先處理 AI 安全風險，OpenAI 執行長：2026 年內不會上市 - TechNews 科技新報；OpenAI's Altman won't do IPO this year, calls AI extinction risk 'unacceptable' - Reuters；OpenAI agents attacked RubyGems before Hugging Face incident, researchers say - Reuters

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 新聞直接提及 | -0.28 | +10.08% | +0.74% | 495.63 | 507.29 | -2.30% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：新聞直接提及「OpenAI」，共 3 篇新聞命中。 方向判斷命中詞：risk。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [優先處理 AI 安全風險，OpenAI 執行長：2026 年內不會上市 - TechNews 科技新報](https://news.google.com/rss/articles/CBMimwFBVV95cUxOel9ZNmtUTWlILURCNzJ4YXhkdlBEUVJmanBLcUViT0YyNTRtR0RiX2JZektYOVBxaHBac1o5SEtKTWxuZHlMSzh4TWFxOERNWXducVd4alp4OEw3TUViamM3OTMxaEcxcGZVX0tETnR6SjJSMzMyMDJpdTFHeU5jek5Cb1ZLMW1wZ3pqb2tQRjZxSkNvUnV1Vm1wdw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 13 Sep 2026 23:35:22 GMT
- [OpenAI's Altman won't do IPO this year, calls AI extinction risk 'unacceptable' - Reuters](https://news.google.com/rss/articles/CBMiuAFBVV95cUxNSkNHUFFrUlZCVWVKZ2dpVVkxSzBmcy16aFFHVTJDV25PZ0YzMjBLVlFQZ0pJcU5EVWJlUW13azNiV1BwOENLcTFVOFpZYVVlT0haaXI2ZkFaOUZxTGp2eE1kaGZCb2pXV1dBQy1XcjQ2NmNXMFA3Nnk5ZnA3MU5wWGZCV0ktTWZad2o0LVBmeW1BclBndWRfWEJScFduQklEZUFEX0NteFBhNDYxRG5keUdiUml3dVYz?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 12 Sep 2026 20:38:00 GMT
- [OpenAI agents attacked RubyGems before Hugging Face incident, researchers say - Reuters](https://news.google.com/rss/articles/CBMiygFBVV95cUxNV2F3RkRiVXZra3BTMExtX3lNVHBEV0xTbkxBMXNwaDVIOGtkeXJEWXRxeEd3dDlLbW5kOUdrQlFnXzVZTk9YRXMxdFRRVGpfR0puUjkyYXozVHJsVXVHTlhSNDVyZjlxMkVwNnU0a2pMMzdOSTdsaTJ4d2E2R1FLbU8wb0VVbW9GUzRsa0VTYUJhN24yRDNTTmtnYkpRUHVlN002SG54czB5UzRsTEtMLUxSSVgyN19xcnRwaGowODRJMXk3ZVNwRDNB?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 12 Sep 2026 08:26:39 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：群益金鼎-東門 對 寶成(9904)個股 單一券商歷史明細 - justdata.moneydj.com；富邦-台南 對 群光(2385)個股 單一券商歷史明細 - justdata.moneydj.com；富邦-八德 對 東友(5438)個股 單一券商歷史明細 - justdata.moneydj.com

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [群益金鼎-東門 對 寶成(9904)個股 單一券商歷史明細 - justdata.moneydj.com](https://news.google.com/rss/articles/CBMilgFBVV95cUxQQ2xhWEplNkpQRzM0S243ellsbnRxRE56XzU4WjIzZG9ScURDaXpYUFMzaWd5N0Nja2hrdHFUcjJXMjl5eFhfUjF1NzYyVEpoYXA5S200ZkJxa2tsd1RldzhlZ0hScXYzbHFTa3dGV1NWNzhCb01taUZhbkh1QWNmYUdDOWctRVRFOTQtWkxVSXpIVmFZanc?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 13 Sep 2026 15:05:16 GMT
- [富邦-台南 對 群光(2385)個股 單一券商歷史明細 - justdata.moneydj.com](https://news.google.com/rss/articles/CBMihgFBVV95cUxOc1RPUHJJOWU2Z0J3QkkxNGZqV1dWbEZyNEp6UWFlTTZ0YjZUZHQySVBDTl9FMV9MTFp0amlJeWotVHU0UjcwYmU2VmdTUEdEZTBaU29kZ1Rxa0RMYUVhejlGaU1sLTdmTnB3ZXIteFZWcExXWExjLWdVdkZVWWNDZTJVSUljZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 13 Sep 2026 12:53:52 GMT
- [富邦-八德 對 東友(5438)個股 單一券商歷史明細 - justdata.moneydj.com](https://news.google.com/rss/articles/CBMimwFBVV95cUxQZnA1alJvcGZWX0VKc0lJSlpYUEhOcy1VYnJNYU82NTRkZk9BYmVXdEpQVE9takgyQUoxOFhPNzZMaE1vN1JUMnpPVzYteDlHNFZPR1h4RWU4RE1jMW9uTXJkLWFuOXRtRG1McnpIUEdmQUdfQlBKQWZFN3hJUzBIV1hwbjBleWc5cDJLNUlwNHBnb2poaE15Q2VWTQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 13 Sep 2026 03:41:30 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：超級央行週登場！美日英台接力公布利率台股週一能否反彈受矚目- 新聞 - MoneyDJ；法人專欄分析內容-台股 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [超級央行週登場！美日英台接力公布利率台股週一能否反彈受矚目- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxORzRkQUI4ZlVrZER0SE9FRjBWSG1JVWFXNzFGS2JyWVViUF9KLWVOaTE5TUFNaUJkckt6cmc0N1JnS0pvQWZneVFsVGtOem9CcUJaSXVUd2lnYnoxazUzTUVORHJCSzFQVF83U1puVmlrbS1pR2w2bE5GQWx1eWdJNm1JNUVZNi1YUFRFR1lqQmNzQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 13 Sep 2026 05:49:00 GMT
- [法人專欄分析內容-台股 - MoneyDJ](https://news.google.com/rss/articles/CBMilgFBVV95cUxOOGxmMXhSX3gwZkc4cjZoR09YN1F5NjEzLV9EUmliUTJidlZaVmo5Z0F1Rk5MVEZralp3YTFDcmx0a2UzWVNmNmZTREpWMVp3YndCc19rc3o3NnI1WlJaTTgxMllrWi0tRXlPWk1xVjd2NXUyTmlTZGFwQ3Z2aTVEOVNZNFBNZ0txTUw3b1Z1SXJUOFBqTmc?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 13 Sep 2026 16:04:32 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
- TWSE PER/PBR 抓取失敗：Expecting value: line 1 column 1 (char 0)
