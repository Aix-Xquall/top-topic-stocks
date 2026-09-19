# 每日股市熱門話題分析 - 2026-09-20

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **散熱與液冷供應鏈**｜正向｜熱度 2｜市場確認 100.00｜同向 1/1
2. **利率與成長股估值**｜正向｜熱度 1｜市場確認 100.00｜同向 1/1
3. **半導體與晶片供應鏈**｜正向｜熱度 6｜市場確認 N/A｜同向 0/0
4. **綜合市場情緒**｜負向｜熱度 36｜市場確認 0.00｜同向 0/2
5. **AI 伺服器與資料中心**｜正向｜熱度 20｜市場確認 5.26｜同向 2/8

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.04（樣本 13）
- 5日相關係數：-0.25（樣本 10）
- 同向比例：4/13

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 散熱與液冷供應鏈 | 100.00 | 1/1 | 0 | +10.11% | +1.78% |
| 利率與成長股估值 | 100.00 | 1/1 | 0 | +10.11% | +1.78% |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | 0.00 | 0/2 | 2 | -9.48% | -6.88% |
| AI 伺服器與資料中心 | 5.26 | 2/8 | 6 | -4.08% | +1.05% |
| 記憶體與 HBM 供應鏈 | 0.00 | 0/1 | 1 | -5.30% | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：哪些硬體廠營收 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 相關性偏弱；應提高同向價格確認權重，降低泛 AI、泛半導體等寬標籤推估權重。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-09-07 | -0.15 | -0.09 | +53.33% | 15 |
| 2026-09-08 | -0.07 | 0.18 | +57.89% | 19 |
| 2026-09-09 | -0.28 | -0.12 | +54.17% | 24 |
| 2026-09-10 | 0.28 | 0.86 | +75.00% | 4 |
| 2026-09-11 | -0.01 | -0.08 | +25.00% | 12 |
| 2026-09-12 | -0.39 | 0.04 | +25.00% | 20 |
| 2026-09-13 | -0.42 | -0.14 | +17.65% | 17 |
| 2026-09-14 | -0.31 | -0.54 | +33.33% | 15 |
| 2026-09-15 | -0.04 | -0.42 | +68.75% | 16 |
| 2026-09-16 | -0.19 | -0.46 | +55.56% | 9 |
| 2026-09-17 | 0.43 | -0.13 | +66.67% | 9 |
| 2026-09-18 | -0.15 | -0.07 | +35.71% | 14 |
| 2026-09-19 | 0.20 | 0.47 | +46.15% | 13 |
| 2026-09-20 | -0.04 | -0.25 | +30.77% | 13 |

## 歷史回測摘要

- 回測日期：2026-09-20
- 近5日 3日相關：0.01
- 近5日 5日相關：-0.12
- 同向比例：+40.74%
- 權重狀態：已調整

- 方向準確度：+40.74%
- 信心排序準確度：0.01
- 診斷：低相關

調整原因：近 5 日信心分數與股價關係偏低，提高價格確認，降低寬題材推估。；關鍵詞×公司後續樣本有效 4 筆，未達 30 筆，不調整樣本權重

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

摘要：散熱與液冷供應鏈 相關新聞集中在：ASIC水冷產品助威 法人調升奇鋐獲利預估值及目標價 - 經濟日報；台股Q4有新主角？兩檔主動ETF押健策、金融股也入列換股方向曝光- 證券 - 工商時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.43 | +10.11% | +1.78% | 3,430.00 | 3,430.00 | 0.00% | 同向 | 75.13 | 45.72 | 19.48B TWD / 54.34% | 2026-09-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐」，共 1 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：調升。

### 主要來源

- [ASIC水冷產品助威 法人調升奇鋐獲利預估值及目標價 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBLZl9MTWhEM1JpdjN3WTY2VlpoeDB0bWkzSXdVSWdYcjFobkgtRFhpMmVwNVo1WTRfeFIxMWdmZXM4ZGVpeFgzS243eWVlNThYZ3lyRXdUYmk5Z9IBX0FVX3lxTE1uZE9WWEhQSU5MTmZPYnFmSC15ZFEtbEVlSjcxOUFyQlFnRm1CRC04ZWZtYnFmY0gwX083R1l6bVZKZVJyd3ZRVDJnbDVzNEpkR05vbTE5YUZPeVpidWlN?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 18 Sep 2026 05:03:01 GMT
- [台股Q4有新主角？兩檔主動ETF押健策、金融股也入列換股方向曝光- 證券 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE10eUlJSkI0ZjRoc2NhQ3ZqUVJONTN4YWxvV19zelFMRmJoWFUtWjExNFg2SWY5OV9CYThfZ21PMW01akxjck9LT2t1VXdVaGRIYXE2TTVDRURua0V5UE5B?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 18 Sep 2026 23:08:00 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：ASIC水冷產品助威 法人調升奇鋐獲利預估值及目標價 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.42 | +10.11% | +1.78% | 3,430.00 | 3,430.00 | 0.00% | 同向 | 75.13 | 45.72 | 19.48B TWD / 54.34% | 2026-09-01 |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +9.67% | +0.36% | 493.78 | 507.29 | -2.66% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐」，共 1 篇新聞命中。 方向判斷命中詞：調升。
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [ASIC水冷產品助威 法人調升奇鋐獲利預估值及目標價 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBLZl9MTWhEM1JpdjN3WTY2VlpoeDB0bWkzSXdVSWdYcjFobkgtRFhpMmVwNVo1WTRfeFIxMWdmZXM4ZGVpeFgzS243eWVlNThYZ3lyRXdUYmk5Z9IBX0FVX3lxTE1uZE9WWEhQSU5MTmZPYnFmSC15ZFEtbEVlSjcxOUFyQlFnRm1CRC04ZWZtYnFmY0gwX083R1l6bVZKZVJyd3ZRVDJnbDVzNEpkR05vbTE5YUZPeVpidWlN?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 18 Sep 2026 05:03:01 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：印度發展半導體尋跨國合作龍頭大廠肯定台灣領先地位| 國際 - 中央社 CNA；《DJ在線》軍工/半導體接力，兩大稀有金屬商前景亮 - Yahoo股市；9天狂漲逾5成！這「半導體設備耗材廠」第二季EPS暴增1566% 新產能最快10月認證 - Yahoo股市

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | -5.30% | N/A | 108.60 | 114.68 | -5.30% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +3.14% | +2.07% | 2,460.00 | 2,460.00 | 0.00% | 不適用 | 86.28 | 28.52 | 514.81B TWD / 53.32% | 2026-09-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +12.64% | +11.03% | 156.00 | 164.50 | -5.17% | 不適用 | 6.68 | 23.46 | 25.04B TWD / 30.71% | 2026-09-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +10.72% | +5.27% | 222.27 | 222.27 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | +8.47% | N/A | 559.82 | 559.82 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | +4.61% | N/A | 1,015.80 | 1,015.80 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | +17.04% | +9.70% | 1,791.82 | 2,335.00 | -23.26% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -8.14% | -19.96% | 357.61 | 446.77 | -19.96% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 CPU, server CPU, x86, foundry；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 0 篇新聞出現相關標籤。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 0 篇新聞出現相關標籤。

### 主要來源

- [印度發展半導體尋跨國合作龍頭大廠肯定台灣領先地位| 國際 - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5vZUpZWlI1U25XQzEzSjk2RW5lY3l6TmFOZndGdUw1WmFGRDQ1aWJPMnp0Y1N5UExwbDJMVnhrXzhXeHlHYmtmWG1oQ2dTeXJ0dENSeFdHdTlRTkxlbzFz?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 19 Sep 2026 13:06:00 GMT
- [《DJ在線》軍工/半導體接力，兩大稀有金屬商前景亮 - Yahoo股市](https://news.google.com/rss/articles/CBMixgJBVV95cUxQdVZESWRERHVucFJpR0lEZzdlUFFUNXlRYjRWUGd2cEpyazhnQkNZbWh4NTladnF4MzBiUFIxS1ktcF9Objd3bHMtcENzOG5KS3dIMWNReUliUVBfeVQzSHR6eTBaOWJnUk1faEJsbzBDU043WDhqZ1p5aVo4WGZCb1VoTFpZeFkyVmFVVUdseTR0WnZDUEdLOTJXWjRDMm0zSElpTlM1bTBEV0F0MjZKSllHUkZORnJERHJFMzVGaHJjT3BfeldoeVRQZDFTWHJ2QXJZLVRHWTVBcFI2RkdqdmJGQWJtWXhfX1ctaVh3OXp6ME1heEJjTE1mUkp1NXpTMlNDaFBFZFJ3dFl6NFNnVS0zNWN1aWxUUlNnTndjZWwyYmh1RHp2NEVLbXZfZnFIY3RZcmZETXYybk5wdFF5Y1R1Q2JHdw?oc=5) - Google News source discovery | Yahoo 奇摩股市 Fri, 18 Sep 2026 05:39:15 GMT
- [9天狂漲逾5成！這「半導體設備耗材廠」第二季EPS暴增1566% 新產能最快10月認證 - Yahoo股市](https://news.google.com/rss/articles/CBMiswNBVV95cUxPdU9RRzdndmk3NVVTM2JFUjlRWW9Eb0NXR29aNzRkbk56S2Fxd0szMDlja3UyN0pDbXN5Rm5SaHR6SE1BZTdVdmhWZkNHVFZYSXhRYVdmSkh5Mk00UDJhOE1HdWR6d0d2M21veThoUGtQZGdfNTRHWWVDMGxoVkEyRlpESXNsVGNManREOExMNy1mNWlQY1pNSUY5VVZwaEFKZ1B4S0R6VEs5ZU11Q1RUbm5fZndXVjEzakFUSEpWYmdWNkxvYzNvel9kOUh5ZVlyamg2dzdLc2ItUmN2ekRhTE9vVVBsVVpUM1lxYm5YS1A3aGVNbVZyYVlZT01LaWZweEZaYUZHa2tPYUlYaXRBNUtjbklvV3F5NlZHTHl6N2NqY0dEQUdZMkk3Z0p5OFh0TnZKTUkxUGhKNkttQnJrNWRyakJSdTFmVjJKODBXMEVWbzk2em1xZWJtVUFHaFJoMlJROWlfNklJZTR5eEN3aC1TTTl0eHpqNVhnWXJVWl9MdXZfVDhxNG5VRktRN1l3RVMwNFJ6SzI2YTE5Q0xkNE9qelNMeXh5eW0yR2RpaGRJMFE?oc=5) - Google News source discovery | Yahoo 奇摩股市 Sat, 19 Sep 2026 14:45:00 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：兆豐-天母 對 至上(8112)個股 單一券商歷史明細 - justdata.moneydj.com；永興-台中 對 京晨科(6419)個股 單一券商歷史明細 - justdata.moneydj.com；台股擂台／周冠軍「低調黑馬」陳奇琛 本周看好聯亞、聯電 | 台股擂台 | 證券 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2454 聯發科 | 新聞直接提及 | -0.21 | +6.32% | +2.73% | 4,710.00 | 4,710.00 | 0.00% | 背離 | 60.69 | 77.79 | 64.18B TWD / 44.08% | 2026-09-01 |
| 2303 聯電 | 新聞直接提及 | -0.21 | +12.64% | +11.03% | 156.00 | 164.50 | -5.17% | 背離 | 6.68 | 23.46 | 25.04B TWD / 30.71% | 2026-09-01 |

關聯理由（前 3）：
- 2454：新聞直接提及「聯發科」，共 1 篇新聞命中。
- 2303：新聞直接提及「聯電」，共 1 篇新聞命中。

### 主要來源

- [兆豐-天母 對 至上(8112)個股 單一券商歷史明細 - justdata.moneydj.com](https://news.google.com/rss/articles/CBMimwFBVV95cUxOVzZ6RlpDT2ZDellBMk5DRE1sZHljZmRNUmRjdU9tbHRPYmQxMm55N1BIU2FEV3p4bmpNM0ZnVHBEZ1pRRTVaZVQxd3laUGxZdDdhd3Z0enA2M1kyRHZvY0pVbEhtY3ZERXpSV1ZOamJDMmZ6R240RmFEa3BQUkRTNVBVYUhsc2VIMmMwcU5nWmF6dXJsN2JYamxvbw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 19 Sep 2026 13:46:01 GMT
- [永興-台中 對 京晨科(6419)個股 單一券商歷史明細 - justdata.moneydj.com](https://news.google.com/rss/articles/CBMiggFBVV95cUxOUjF4UktBTkI1OGF3WmRTTHh1YXBWdFVkcTdLWFY3OFI4RVk1TC1vRVpnYWZSMkJSRnlYSUlEY3BuYno1MWVOMF9ISmJnekN6Z0tFUjl2a21ZZm1Xb0JfN3c5YlJod3RXb3FlaGdXdWdIQjZ5cUpYc0JKd2RDb0hsZXNB?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 19 Sep 2026 07:42:45 GMT
- [台股擂台／周冠軍「低調黑馬」陳奇琛 本周看好聯亞、聯電 | 台股擂台 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTFB3T3UtYk56SmVYZHB1d3dkTmhzUFhXMTNuUkNZQjVBVEFMMDFvQ3lOSXRMWWxoOWFqdFNGRXZuQnBvSmY5TGozeE80TEJwbjhkUzBISDFhZWxXdm9C?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 19 Sep 2026 16:16:57 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：升息不確定性消退 台股焦點重回 AI 與基本面 | 市場焦點 | 證券 - 經濟日報；Did AI Slowdown Calls Just Shift Intel's (INTC) Investment Narrative? - webull.com；AI 需求如何影響輝達產品策略？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | -0.27 | +10.72% | +5.27% | 222.27 | 222.27 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | -0.54 | -5.30% | N/A | 108.60 | 114.68 | -5.30% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | -0.03 | +8.47% | N/A | 559.82 | 559.82 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.03 | +3.14% | +2.07% | 2,460.00 | 2,460.00 | 0.00% | 背離 | 86.28 | 28.52 | 514.81B TWD / 53.32% | 2026-09-01 |
| MSFT 微軟 | 產業/供應鏈推估 | -0.02 | +9.67% | +0.36% | 493.78 | 507.29 | -2.66% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -8.14% | -19.96% | 357.61 | 446.77 | -19.96% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.02 | +7.77% | +3.24% | 638.00 | 680.00 | -6.18% | 背離 | 13.92 | 46.16 | 82.25B TWD / 45.66% | 2026-09-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.02 | +6.32% | +2.73% | 4,710.00 | 4,710.00 | 0.00% | 背離 | 60.69 | 77.79 | 64.18B TWD / 44.08% | 2026-09-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。 方向判斷命中詞：slowdown。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：slowdown。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：slowdown。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [升息不確定性消退 台股焦點重回 AI 與基本面 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxOT0FnRHdLcjdJOGh0eE9xMmp4a01YQnhoc3FHcHdBTy1QcHQyYWNwakMxWFZCOHRNbDBZcjk5cmd6LWxRQ1JNZVM0MkwyZFFHdHRpVnE0a0N6b1NTZklKbEI5S191aG50NTYxWU5GeHBYcVdrV1dfNE1reHZWbXJ1Yg?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 19 Sep 2026 03:09:58 GMT
- [Did AI Slowdown Calls Just Shift Intel's (INTC) Investment Narrative? - webull.com](https://news.google.com/rss/articles/CBMiWEFVX3lxTE9TU0xQVWpVQnkzX0VWWVFZUi1ud3ZrS1RBTjJBMTNVWFp6clViN0Rrd2hJVHp3VEhSMlJsQ0NSTDFpMUplTlFEZlR5cjNYdzNodkpYRENZMm8?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 18 Sep 2026 02:30:56 GMT
- [AI 需求如何影響輝達產品策略？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMib0FVX3lxTE1JOE43YnJSMW9SY09URkZBekh2VHRCZERmdnZVNXA4N0Q5aUNRMnRadnVMeV9NQlhXMExtSl9kT0Nfb3NIZjMyQThFWWJjUHJQVkJZbkJCUXdtbjJ2UUhyS29YSXFkaFJOU2ZWVmlmcw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 19 Sep 2026 20:37:14 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Intel vs. SK Hynix: Which Chip Stock Is Worth Chasing After This Week's Surge? - Zacks Investment Research；夜盤狂洗400點！台股下周續噴 「記憶體」恐成最強火種 - Yahoo股市；美光財報倒數 輝達、SK海力士釋記憶體市場強烈訊號 - news.cnyes.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | +4.61% | N/A | 1,015.80 | 1,015.80 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +10.72% | +5.27% | 222.27 | 222.27 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.21 | -5.30% | N/A | 108.60 | 114.68 | -5.30% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | +17.04% | +9.70% | 1,791.82 | 2,335.00 | -23.26% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「美光」，共 1 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 方向判斷命中詞：surge。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel vs. SK Hynix: Which Chip Stock Is Worth Chasing After This Week's Surge? - Zacks Investment Research](https://news.google.com/rss/articles/CBMitgFBVV95cUxOMEFXQ29yMHczbUs4TVo5OGFnSlRYNk1JY0VRR3lzSmdaUmJXaEFvRHlTa3VSOWxkVmpvNmlISnF0UF9DSC1uS1F6aHJ5aFVSU2tob01FRmR4MFpjVkcwdEZ6NE5HckhpeG16ZmRCdzJ3bVUwby1pVE9Bd3hLTkdpSDBhUXJ3UG5YZDRZbUhPRXFWQ2FNd210Q2szcFBMai1vR2hkWk10d054TjAtSlFyYVZ3blBNZw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 18 Sep 2026 18:31:59 GMT
- [夜盤狂洗400點！台股下周續噴 「記憶體」恐成最強火種 - Yahoo股市](https://news.google.com/rss/articles/CBMihANBVV95cUxONFhodVY1TGxjVmhzckItOUlIOHduaVhETFlhMU1qYnluLS1TRTRuNGstQjV2UkNEVF9fS0pIcVhoTXphQWViUER3ZmlWeXhCODVLN016cWo2dnFBQTB1aVU0dWJpUmJkOTBjYlZkVnlQaG0wbkR1TGRUUGNweVM1YjFKblJRQUlodW93TWF5UHpsa0dfS1Rad1A0UXI2LTZoYmdSWUxzY3QwMHBMYVNPdU1idWp5eW5GbTFCRmhwcXJtOUVjTFA2M2Rxck11Ym1KNzBCYjJRbHR0WTNmM3k4eEM0RjNVcEpqS1pLOTI1RVFHR0pKaFVmNDBEYWVvZVhEeDlLR05CTW1xSFE5d1R0Y2hxd0ZrM2x5TUJURklsa09HSlRWdTBDM3o5RUdxZkhNUkNVTlhlWGFqbllfVTZ4eTFzbkpjN0NxZFVKVFJUdFZRbEdhTi1lNTdVYXA5OGVLOXZndzBaRzNpUVFNQkVibVloWkFPZjFEblFYMGUxNDZrQ2RY?oc=5) - Google News source discovery | Yahoo 奇摩股市 Sat, 19 Sep 2026 02:41:31 GMT
- [美光財報倒數 輝達、SK海力士釋記憶體市場強烈訊號 - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTE9WaEJmS0lyUTVPUE9TeHFQWHVnTF9iQzJHTTg5aGMtMXp4bmZzSHRhOWhGQlNpZGNfN3FiUkREUEtFSGlSZnBxY0tMTmJmWmM?oc=5) - Google News source discovery | 鉅亨網 Sat, 19 Sep 2026 05:00:05 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：個股動態報導內容-6E73B8E4-63BD-4374-984D-7772D070EB99 - MoneyDJ；個股動態報導內容-A9215FDA-158C-4C15-9578-1225FC644816 - MoneyDJ；兆豐-桃鶯 對 欣巴巴(9906)個股 單一券商歷史明細 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-6E73B8E4-63BD-4374-984D-7772D070EB99 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxPUW40QzlNaExxcUV1aDFNaXF6MUxObDV6bHhZWldmbGFpM09nZ1VEQm5NQ1VoMFZTQUlmaDJNSEI2UTRHRHgwdEdtMktKNVdHZmtGTFdXTlp2NEdIeFl4d2VaMTVISHhuZGtzMk1mcEV1NWpxTEJjajgzdVpVaWNoanctcG1Ma3pMWmlWeERrc2lEbndK?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 19 Sep 2026 17:27:34 GMT
- [個股動態報導內容-A9215FDA-158C-4C15-9578-1225FC644816 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxPUWhOejcyYWxpZHI5ZTVoeDlYUnhOS3J3dWw2N1ZSNXdZbFZ5SFRMZ2lkSWNzWFBySzJDdzF0WS13ZEtPSzhPN3BISUZiZldBaWV6WXVfVHZ4QnNFSU1mV3RIcU42dWxqX05DN1JkRWdaZnNnSDdvb0VOWU81R0tkZXdJeERZUjFxTVIybE54bXpCeW9N?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 18 Sep 2026 13:25:47 GMT
- [兆豐-桃鶯 對 欣巴巴(9906)個股 單一券商歷史明細 - MoneyDJ](https://news.google.com/rss/articles/CBMinAFBVV95cUxORlNuc3VjVVhaMlRJdFpRMU5NU1poWUxUdjNEQXo4bTdYbWxWLUVmbGdycEhhM2ZWTTY4SzNkejhCdzNYR3lWc0hPQmFja0stbHdyTzlNdUpjbi1TWHU5VWE3SldOOEc4Z3JZWkxENEx3aVVwNDNRYmkzZ1NpVDNYT1J5akJTSXN3aXFNWTIzcUF4WkRkSzFtQktTb0g?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 19 Sep 2026 08:18:06 GMT

## 新興題材：哪些硬體廠營收

摘要：新興題材：哪些硬體廠營收 相關新聞集中在：AI 進入驗證期，哪些硬體廠營收最穩？ - TechNews 科技新報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [AI 進入驗證期，哪些硬體廠營收最穩？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiU0FVX3lxTE1DR1l5eW9FQ1dCVHBxTGlqTTJRZm5xcE9mdy1xSTJsemVoRmxoNzl6U28zTFZrWWdzWDRjLXplanlTTzAzWTNEOGdLREVlNUFnYU84?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 19 Sep 2026 15:03:54 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
