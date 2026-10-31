# 每日股市熱門話題分析 - 2026-10-31

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **綜合市場情緒**｜負向｜熱度 51｜市場確認 73.75｜同向 1/1
2. **AI 伺服器與資料中心**｜負向｜熱度 17｜市場確認 70.49｜同向 6/8
3. **新興題材：全球晶片**｜負向｜熱度 3｜市場確認 100.00｜同向 1/1
4. **半導體與晶片供應鏈**｜中性｜熱度 3｜市場確認 100.00｜同向 2/2
5. **記憶體與 HBM 供應鏈**｜負向｜熱度 4｜市場確認 76.67｜同向 2/3

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.50（樣本 15）
- 5日相關係數：-0.68（樣本 13）
- 同向比例：12/15

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 綜合市場情緒 | 73.75 | 1/1 | 0 | +1.25% | +2.07% |
| AI 伺服器與資料中心 | 70.49 | 6/8 | 2 | +6.00% | -6.71% |
| 新興題材：全球晶片 | 100.00 | 1/1 | 0 | +42.66% | -62.13% |
| 半導體與晶片供應鏈 | 100.00 | 2/2 | 0 | +24.98% | -32.20% |
| 記憶體與 HBM 供應鏈 | 76.67 | 2/3 | 1 | +15.20% | -33.80% |
| 新興題材：TradingKey | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MarketWatch | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-10-18 | -0.12 | 0.33 | +21.74% | 23 |
| 2026-10-19 | 0.44 | 0.36 | +50.00% | 12 |
| 2026-10-20 | 0.09 | -0.81 | +69.23% | 13 |
| 2026-10-21 | -0.25 | 0.23 | +5.56% | 18 |
| 2026-10-22 | 0.02 | -0.21 | +38.89% | 18 |
| 2026-10-23 | 0.35 | 0.29 | +78.95% | 19 |
| 2026-10-24 | 0.09 | -0.31 | +70.00% | 20 |
| 2026-10-25 | 0.41 | 0.78 | +64.29% | 14 |
| 2026-10-26 | 0.27 | -0.25 | +36.36% | 11 |
| 2026-10-27 | 0.07 | 0.31 | +50.00% | 18 |
| 2026-10-28 | -0.30 | 0.47 | +20.00% | 15 |
| 2026-10-29 | -0.05 | 0.04 | +42.86% | 14 |
| 2026-10-30 | -0.00 | -0.05 | +47.62% | 21 |
| 2026-10-31 | 0.50 | -0.68 | +80.00% | 15 |

## 歷史回測摘要

- 回測日期：2026-10-31
- 近5日 3日相關：0.28
- 近5日 5日相關：-0.13
- 同向比例：+64.71%
- 權重狀態：已調整

- 方向準確度：+64.71%
- 信心排序準確度：0.28
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

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：個股動態報導內容-02D16A59-9517-445F-82C9-7E2668667D1A - MoneyDJ理財網；股匯遭重擊！台股收跌1,156點創波段低點 台積電收低45元 - 經濟日報；歷來最慘…外資本月大砍台股近兆元 公股低接2,409億創新高 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | -0.45 | -1.25% | -2.07% | 2,370.00 | 2,480.00 | -4.44% | 同向 | 86.28 | 27.47 | 511.86B TWD / 54.65% | 2026-10-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。

### 主要來源

- [個股動態報導內容-02D16A59-9517-445F-82C9-7E2668667D1A - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilAFBVV95cUxNNkNuTmY2MDM0V0hjWnZyeU16OWVOSkNwZzBZSkwxa3FiY3htYVZOQ0ZNQ3JVZVVpb3c4cUtFQWNDNUxHdUlUNUJmSmNiMDduNVRjSmFaa3ZqOTFtTkZlVjhuRXV4SUlLNDVra1pyUjZWd0VtRDIxQUwtUTFCazR2NEZiRjBySTZsUk1SLVgtVm4tdi1C?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 30 Oct 2026 11:44:48 GMT
- [股匯遭重擊！台股收跌1,156點創波段低點 台積電收低45元 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFAtQm1fdS1TVVNhaVQxSUExRGthMWc5QUQ2bm10dU1ab0FyNEQyM0FoLVdaaXlKeDRkU1l5T3dIajVOc2FHck9FSUUtTGZOdVEwVS1mRDkwek9tQdIBX0FVX3lxTE1sOTdhNHZTWmY4d1g2ZnZsUWhEWEdWYS1ZYzFqX2RMMmZ2d0RoMDR5dEp1RllLUUhGVGRrOE1iamhvVUsxU2YtWHRRTGRSdWxBd1FLYU5lOUplNE5TNjl3?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 29 Oct 2026 09:00:00 GMT
- [歷來最慘…外資本月大砍台股近兆元 公股低接2,409億創新高 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1WRklLUmJhbFlfTWwtYmVwNy1LamxkZnJZRzljN3BrUHV5dmlXTUhDd0k0aFFaZ09BTmJ3azd0d2pSbDhmQkp2UWM5UHZMMUpQS3VCc0ZCamVRQdIBX0FVX3lxTE51RmhUNmcwUlNxaVVfd2xfQjRxTGR2R1laNW1kSU5ITy05N205c0lLUElFa08ydjh6TkhNMUZZZ3MwU1pCcGR4TzN6TnIxd254ZnBZUDJvMXAycXN3RmZ3?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 30 Oct 2026 18:21:46 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：AMD stock falls as Intel's earnings flag PC slump and server supply squeeze - Quartz；個案用 AI 打造心理諮商師「分身」，專家提醒恐混淆療程並延誤治療 - TechNews 科技新報；LHC 數據將增長十倍，這對 AI 算力基礎設施有何影響？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.58 | -42.66% | +62.13% | 65.76 | 114.68 | -42.66% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.56 | -2.19% | N/A | 504.80 | 566.42 | -10.88% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | -0.06 | -7.31% | +2.27% | 204.64 | 228.38 | -10.39% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.06 | -1.25% | -2.07% | 2,370.00 | 2,480.00 | -4.44% | 同向 | 86.28 | 27.47 | 511.86B TWD / 54.65% | 2026-10-01 |
| MSFT 微軟 | 產業/供應鏈推估 | -0.02 | +15.92% | +6.08% | 521.91 | 530.14 | -1.55% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -11.95% | -13.68% | 326.08 | 446.77 | -27.01% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.02 | +2.61% | -2.34% | 668.00 | 703.00 | -4.98% | 背離 | 13.92 | 48.34 | 88.13B TWD / 45.52% | 2026-10-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.04 | -1.14% | -5.43% | 3,915.00 | 4,920.00 | -20.43% | 同向 | 60.69 | 64.66 | 55.40B TWD / 1.97% | 2026-10-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：falls, 恐。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。 方向判斷命中詞：falls, 恐。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 5 篇新聞出現相關標籤。 方向判斷命中詞：恐。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AMD stock falls as Intel's earnings flag PC slump and server supply squeeze - Quartz](https://news.google.com/rss/articles/CBMieEFVX3lxTE03WGhQN1lFOU5lR1ZLNWFYdmRmZjNKTjBrNW9DX1FZbkpaVDczTXYwUG91VDBVYkwxNVJROXhmNFk2UG9ST1UxRFo3b1VfbUNpcUF2NVJ0WXJnbFo3eUQzUE85QVdqMEZwY1NBZ0xVWTkwRzhhb3I0TA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 30 Oct 2026 13:36:23 GMT
- [個案用 AI 打造心理諮商師「分身」，專家提醒恐混淆療程並延誤治療 - TechNews 科技新報](https://news.google.com/rss/articles/CBMitAFBVV95cUxQd3EtYmVKX2wzbXZaUVFLTVc5SnY2N2FwZFJRTEFrc0U4UHBiV2FwQXczNTREYXQ5YlVVb0RlZzdmRmhVY0xGVWRxV0ZsVEZJTE9lUEJNbDBTZTJmTUlUS0NRLUdLZGxYV1VVOWZZeWtpU0FOUmlZT01ScjRSc2tJbGRORm1CMkNXOHp6ZDF1Wnl3YnBJS2p2V0dQNTRGMFAyRmRSemVoalAyZTVzQm1YUWM5eVA?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 31 Oct 2026 00:34:35 GMT
- [LHC 數據將增長十倍，這對 AI 算力基礎設施有何影響？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMieEFVX3lxTE9KT2hwYmhQTnpadDhBOVhUYlNiUTNlMnBGeWlTLWtRNklBT1VESmJzNTVid3gxMlEtT01HYllHVlZNNXJMamYyQmpoUDJGSU9kamxnelBiZE1nd2NDY1ZtaG1vSWtiNGlLQXM1OUIyenctbmswYjBlaA?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 30 Oct 2026 17:35:19 GMT

## 新興題材：全球晶片

摘要：新興題材：全球晶片 相關新聞集中在：英特爾股價大崩 30%！恐創史上最大單日跌幅，全球晶片股跟著下殺 - TechNews 科技新報；英特爾盤中崩跌30%！恐寫史上最慘一天 全球晶片股跟著殺 - Yahoo股市；英特爾盤中崩跌30%！恐寫史上最慘一天 全球晶片股跟著殺 - 鉅亨網

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.60 | -42.66% | +62.13% | 65.76 | 114.68 | -42.66% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「英特爾」，共 3 篇新聞命中。 方向判斷命中詞：恐。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [英特爾股價大崩 30%！恐創史上最大單日跌幅，全球晶片股跟著下殺 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiZ0FVX3lxTFBFUC1UWDU2UmRfVGFuT0lfdU5LY25hMlYxd040dVpGYXBxYWhOS0FuYWRRcTI4bzRTOEZOaWdfMlU3UlgtTHNSVjJIRy16aEpSbTRuZXlrTnowaTAtYmVjT3VVbHl1M28?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 31 Oct 2026 00:54:39 GMT
- [英特爾盤中崩跌30%！恐寫史上最慘一天 全球晶片股跟著殺 - Yahoo股市](https://news.google.com/rss/articles/CBMi6gJBVV95cUxPbGFaWjN0NEJlSzUwR3FPSVIwQ2FRckNXWVlacW9FbER4TXIyZ2lGaTdfbnJXSnNrX2RUSUk2OGljem85T3hFR1ZRRlYtUlV5d3JlNW1YUkV6SmNrNm1KanZicnNOTUQ5NGRoXzFWYU5fNG5RLUZ1anR5RkNVR3NaQnNET25VeFV4bDBPajlnZEYxQ3hfYWc2WWhSWnB2UjJ1VmxJc0RBRzg1Z3NDRnphN2FxS2k5YUk5ZXFaTFhvdzFkRHowNEdBaTVEdUhJREFXcERSdDhVaDBJdVNoVDdMWDBwbW4ta3NBdnl2Uy1nd1FBdmpUU0RMWGx1aUdIMFJKNzlaSW1ybzQ1VVVoWlZ3TWxPcVlIMmlqUy1vZzJGam1HUi16bUpwdDg3YktyTU1QME9ZWmZfLTJEYTBMVkU1OVJMNURoQ1lfc0Z2WGd1N2JDUHRrZ3M0bmwtaHVQaEtQNW8tNnN6a0NnZw?oc=5) - Google News source discovery | Yahoo 奇摩股市 Fri, 30 Oct 2026 17:30:03 GMT
- [英特爾盤中崩跌30%！恐寫史上最慘一天 全球晶片股跟著殺 - 鉅亨網](https://news.google.com/rss/articles/CBMiT0FVX3lxTFBQLUtaT0lUZGZYcmpJSzVRQlFfQXk2d1lDeEkxVkdYS1oxaGRQeHdmT00wYmJUak52VjhTMExRQXpERUU0Rm15dmo4WEh5UFE?oc=5) - Google News source discovery | 鉅亨網 Fri, 30 Oct 2026 17:30:24 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：台股崩跌近千點這家砷化鎵晶圓代工廠卻漲停！法人看好衛星、AI光通訊雙引擎點火- 證券 - 工商時報；英特爾盤前暴跌近25% 拖累半導體族群 輝達盤前挫2.8% - 鉅亨網；AI 與半導體雙引擎爆發！盧超群：2026 年台灣將成美國第一大貿易夥伴 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.53 | -42.66% | +62.13% | 65.76 | 114.68 | -42.66% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | -0.48 | -7.31% | +2.27% | 204.64 | 228.38 | -10.39% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -1.25% | -2.07% | 2,370.00 | 2,480.00 | -4.44% | 不適用 | 86.28 | 27.47 | 511.86B TWD / 54.65% | 2026-10-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | -8.98% | -12.89% | 111.50 | 164.50 | -32.22% | 不適用 | 6.80 | 16.47 | 25.35B TWD / 27.22% | 2026-10-01 |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | -2.19% | N/A | 504.80 | 566.42 | -10.88% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | -8.88% | N/A | 884.74 | 971.00 | -8.88% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | +5.93% | +5.48% | 1,330.05 | 2,335.00 | -43.04% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -11.95% | -13.68% | 326.08 | 446.77 | -27.01% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「英特爾」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：暴跌。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：暴跌。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 0 篇新聞出現相關標籤。

### 主要來源

- [台股崩跌近千點這家砷化鎵晶圓代工廠卻漲停！法人看好衛星、AI光通訊雙引擎點火- 證券 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBpb215RGxTcmFfUzVVNlJ3UDR0cHJETWhBcnliVzR2dFRwOTRmWmtYWkx0YlZKLWZ4WS03Y1pSU3dIbUQ5V1hCZGN5OElwWnk0RFZRQWxKQzNCZnFZVkRV?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 29 Oct 2026 04:13:00 GMT
- [英特爾盤前暴跌近25% 拖累半導體族群 輝達盤前挫2.8% - 鉅亨網](https://news.google.com/rss/articles/CBMiT0FVX3lxTE42TEFlZ2VLNW1sUzlkTVYzWTMwVVhsOTFBVzQwWVV2aDVuV3BOYXdhUXc0VV9SaUpKYnZ4TURCSXdkaGJPWFp6Mlg4UURLMDg?oc=5) - Google News source discovery | 鉅亨網 Fri, 30 Oct 2026 11:19:22 GMT
- [AI 與半導體雙引擎爆發！盧超群：2026 年台灣將成美國第一大貿易夥伴 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiogFBVV95cUxNeTQ3U25aRS1XVlZqZUtFRUY3U3hKbDFPRlZoNjhIYjFWX25vdWRmX2RFM3JraGNjVlRUb1pWZm80aVpMN1cyUmNYdGk2SC1QVjE1WE5qQjZOdVhnQ3ZUb1Vvb3VmYUV4Q1o2Q2tkTmFxUFpuZlRscGEzMVBEdEl0ak9yYjZGWnpsRWVubGVVVEpCaV84ZnlWZ2ZueTluNXhvd3c?oc=5) - Google News source discovery | TechNews 科技新報 Fri, 30 Oct 2026 03:53:55 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Sandisk Sinks 9% Despite Earnings Beat, Raised Guidance and 8-for-1 Split; Western Digital Tumbles 8%, Seagate Slides 7%, Micron Falls 6% - 24/7 Wall St.；Sandisk and Micron Slide 5% as Samsung Miss Cools Memory Rally Ahead of Sandisk Earnings; SK Hynix Falls 3%, Western Digital Dips - 24/7 Wall St.；Samsung Stock Plunges After Earnings, Dragging Micron, SanDisk, and Western Digital Down Over 3% Pre-Market as Market Focuses on SanDisk Earnings - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | -0.60 | -8.88% | N/A | 884.74 | 971.00 | -8.88% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.30 | +5.93% | +5.48% | 1,330.05 | 2,335.00 | -43.04% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | -0.45 | -42.66% | +62.13% | 65.76 | 114.68 | -42.66% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -7.31% | +2.27% | 204.64 | 228.38 | -10.39% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron」，共 3 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：falls, miss, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：falls, miss, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- INTC：新聞直接提及「英特爾」，共 1 篇新聞命中。 方向判斷命中詞：暴跌。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Sandisk Sinks 9% Despite Earnings Beat, Raised Guidance and 8-for-1 Split; Western Digital Tumbles 8%, Seagate Slides 7%, Micron Falls 6% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMigwJBVV95cUxPRHRncUhXeEE4ajg0RnF2WVhka1ZpVFdYM1BhOGFjRlRaMndMQmh6VGVCekx0TTJzQmZKUVJ4d0JsSm02RjM4MjF3b2p2blY0ZlZ6R0dVbE5NWTVuOHBqTTctY0czUVdYbnZHanNTYXR2ODlwNkd2S1RKaENyejg5REpWQUdzOHRaTFcwUVYxLV8tUlRmcHVCNTlWNk5ld0Q1R1lHV1RpZ0xDLTRNQ2x3S3VkdEVZVXpieEc4TEg4UkFsdG1IZnVTeFMxV1c5Sk00U3ljeWN3aG56N1J4Y25ZUHRUQnUxS0dzZnc0NnVINlowNDcyMzhuNmFjaUM2ZDlDQzdR?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 30 Oct 2026 14:17:00 GMT
- [Sandisk and Micron Slide 5% as Samsung Miss Cools Memory Rally Ahead of Sandisk Earnings; SK Hynix Falls 3%, Western Digital Dips - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi_gFBVV95cUxPUTVoOHM3cGRfOTVDVENWV3cza09ETURab0FjUEhxVm0zMUVjU0txVWJodFktb2czT21aS29KUThnMHRzN1d5YUE3VFV0NDU5LXYxclVGTEtydzhGZEhZdVhQZ2hPYUsxM3p4ZE83SU56VTM4N1BaQzUzRG9HbGZnRzVURThXVUJsYUpoWmdhdlctVmNUZkRjQThyNTY3aS1lVTVJdm1QMTVfQ0xTY1Jrd3ZleW10c1AwYndnYjVkNm5qRHRCZDM1SThnbEx4YVcyNUY4RzBfNTg5QjZVcXJ1VmxXcUw0TWYtbG0zTUxTZlZvM1dabnMyN2NoYnd3QQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 29 Oct 2026 20:09:00 GMT
- [Samsung Stock Plunges After Earnings, Dragging Micron, SanDisk, and Western Digital Down Over 3% Pre-Market as Market Focuses on SanDisk Earnings - TradingKey](https://news.google.com/rss/articles/CBMizAFBVV95cUxNakRJaWlSeUc3b3V6MTVnYTFNdEw3VTAwQko1UHI2RXBoUW94MGFhYkRaY19lMzl6WjZ6MC02ZW82Uk56UUxSWFZkX0xkdl9oV3p0Wk1BbmptRFNPMEszMW10Y25YMi1YMEJTNEVRbmFaV2lqdzlaVGtWWnJVQjBEX0diaVRJN3dZX0tBdVBZTTZmWU9YMS1rSHFHdlNXbzJXbk5RWTJZaUs3SFFuaGRIQjUwZFNjV05lYkppUHJkUXI2T2NMOW1Ka1I3bjU?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 29 Oct 2026 08:44:33 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Samsung Stock Plunges After Earnings, Dragging Micron, SanDisk, and Western Digital Down Over 3% Pre-Market as Market Focuses on SanDisk Earnings - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | -8.88% | N/A | 884.74 | 971.00 | -8.88% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | +5.93% | +5.48% | 1,330.05 | 2,335.00 | -43.04% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。

### 主要來源

- [Samsung Stock Plunges After Earnings, Dragging Micron, SanDisk, and Western Digital Down Over 3% Pre-Market as Market Focuses on SanDisk Earnings - TradingKey](https://news.google.com/rss/articles/CBMizAFBVV95cUxNakRJaWlSeUc3b3V6MTVnYTFNdEw3VTAwQko1UHI2RXBoUW94MGFhYkRaY19lMzl6WjZ6MC02ZW82Uk56UUxSWFZkX0xkdl9oV3p0Wk1BbmptRFNPMEszMW10Y25YMi1YMEJTNEVRbmFaV2lqdzlaVGtWWnJVQjBEX0diaVRJN3dZX0tBdVBZTTZmWU9YMS1rSHFHdlNXbzJXbk5RWTJZaUs3SFFuaGRIQjUwZFNjV05lYkppUHJkUXI2T2NMOW1Ka1I3bjU?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 29 Oct 2026 08:44:33 GMT

## 新興題材：MarketWatch

摘要：新興題材：MarketWatch 相關新聞集中在：AMD’s stock slides after Intel earnings reveal two big issues - MarketWatch

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AMD 超微 | 新聞直接提及 | 0.00 | -2.19% | N/A | 504.80 | 566.42 | -10.88% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | 0.00 | -42.66% | +62.13% | 65.76 | 114.68 | -42.66% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AMD’s stock slides after Intel earnings reveal two big issues - MarketWatch](https://news.google.com/rss/articles/CBMipgFBVV95cUxQSG1ER3NBSmVWMHJlelZ0akVNa1FTVDFlM1J3b2ZMOWZXanV1cVdDblB6dDlHRmJYZDRVZ2JKWTRfRDIyTkZaNENTZVQ2MGFJUjk2X0ZfU2ZTVjZEcm02VlJZXzQyYmlVdHY2Mm5BaEVvUmN0Tm1rQUF2NWlIQTdLMFpWNVl3QUNvX05MRlg0cmw5d1JQWjAxeUtDeHpVandzY2tDZGxn?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 30 Oct 2026 20:28:00 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：20261030台股融資維持率 - MoneyDJ；《台股盤後》收跌1156點、險守45K；周K連三黑/本月跌5.7% - MoneyDJ；國票證券：台股需留意大量低點45676點有守與否- 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [20261030台股融資維持率 - MoneyDJ](https://news.google.com/rss/articles/CBMisgFBVV95cUxOMnRaN19teXVpY2RWVUZhTmc5VC1DeHdlbXBRUzNFZ3p6dzctcWNKQ2tRRVBFdkNRREc0OWpFUWFxUWV0aGFzMzJzeVhwTVBIamxGSzdXQnE5NUxqWmVGWkF2UzZScERGNE8zNFU4eE5rNTVMX203bEcwWS1oZWdjSTNjaGE0enJ0SzRYMVBmNTNqUUhVUEQ3SUJac2Iwb0pFTTNRbU9fVWhyTXhoX0J3ckVB0gG3AUFVX3lxTE02dnFHNGtmNVNWWG9FWURMZGN5bEMyU0E1QnMwbUxJQWpoam54LUhlUzhnRjJiMDJmdndTaUMyT2NyU3ZOWGtVbGMwNko4TTlIRTd5T3hKZVM5aFhNMEFKZlpsMElFOEtzLXFWaG5KWGlhTjZaZ3pORGNJNmp3TW92ZWpiNVRXRExPV011Y1QtZmcyNkRId2NyTUtzQzVSeU1HUXNoNjRtVkFQNDVCbGZyYUlwTTgxSQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 30 Oct 2026 15:03:35 GMT
- [《台股盤後》收跌1156點、險守45K；周K連三黑/本月跌5.7% - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQTlc0Y2wtX09WZFBjXzhVUXVMakI5cGNRZDNGSHVIN1M0d0NVZ3IydFFPTnpnSGR3NTltWmhtdEJZdDNtUV8yZExtUVNud3lKVW9MRVF3Mm8xQ3dja2FtdGFHWFRWX0RXMTV1RkdUZkdyM3NYbnlkWDd2LXRMNWNHNUVZZklLeVRETS01S2RPS0tadw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 30 Oct 2026 07:56:00 GMT
- [國票證券：台股需留意大量低點45676點有守與否- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQd3dqaXFNZHExWXctR0xEei0wcDFhU1JQbFFxS001STcxM09sU3pWR3Z0MEFVNTExMVZwV0ZfVmJLM1BnYk00RHFTY3Z3YVpheXBnMWlJZllBVl9QMHNreVVLUzQ4ZlhNX09Ma0ZDMW1CT3E0VWZrQnU5N3QwcDVLQ3dicGZTSUttbHZadWg3bXI0dw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 30 Oct 2026 00:49:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
