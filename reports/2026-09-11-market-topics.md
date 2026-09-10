# 每日股市熱門話題分析 - 2026-09-11

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **關稅與供應鏈轉移**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
2. **半導體與晶片供應鏈**｜中性｜熱度 6｜市場確認 N/A｜同向 0/0
3. **利率與成長股估值**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
4. **新興題材：MarketBeat**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0
5. **AI 伺服器與資料中心**｜正向｜熱度 14｜市場確認 25.99｜同向 3/8

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.01（樣本 12）
- 5日相關係數：-0.08（樣本 8）
- 同向比例：3/12

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 關稅與供應鏈轉移 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MarketBeat | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 25.99 | 3/8 | 3 | -0.09% | +0.98% |
| 記憶體與 HBM 供應鏈 | 0.00 | 0/4 | 3 | -5.47% | -5.14% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 相關性偏弱；應提高同向價格確認權重，降低泛 AI、泛半導體等寬標籤推估權重。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-08-29 | -0.10 | -0.01 | +40.00% | 10 |
| 2026-08-30 | -0.52 | -0.04 | +23.08% | 13 |
| 2026-08-31 | -0.41 | 0.29 | +40.00% | 10 |
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

## 歷史回測摘要

- 回測日期：2026-09-11
- 近5日 3日相關：0.06
- 近5日 5日相關：0.26
- 同向比例：+55.17%
- 權重狀態：已調整

- 方向準確度：+55.17%
- 信心排序準確度：0.06
- 診斷：低相關

調整原因：近 5 日信心分數與股價關係偏低，提高價格確認，降低寬題材推估。；關鍵詞×公司後續樣本有效 0 筆，未達 30 筆，不調整樣本權重

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

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：輝達Vera Rubin機櫃要價逾2億元！謝金河揭「台灣產業命運」：這台機櫃養大台灣供應鏈 - 財訊；攻半導體業聚賢研發－創擠進一線供應鏈- 日報 - ctee.com.tw

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +8.77% | +3.42% | 218.36 | 223.67 | -2.37% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +4.65% | +17.11% | 326.57 | 326.57 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | -1.95% | +1.41% | 251.00 | 289.00 | -13.15% | 不適用 | 15.21 | 16.55 | 921.77B TWD / 51.98% | 2026-09-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [輝達Vera Rubin機櫃要價逾2億元！謝金河揭「台灣產業命運」：這台機櫃養大台灣供應鏈 - 財訊](https://news.google.com/rss/articles/CBMie0FVX3lxTE5pbGdiUXNfcy1mY3Z0N1NpMkMxTG5XbDFELUdBOHpZc2wzZXdRaHUtQ0VUMXhhYnVFb3RpYlowd090WlF5UHA4SXFwNVJwVFkwZzBWMUp1LV9iUlBhZ3VOcmM1Qjl2YXpHUDEzaldHMHRQR3ZTSXNxNVgzbw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 09 Sep 2026 04:20:57 GMT
- [攻半導體業聚賢研發－創擠進一線供應鏈- 日報 - ctee.com.tw](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBUQXRkTEstUm15Y3V0Q3FHQWFrWHQ4VTZUWHNGU0pJZ24ycnR2UUptTzBQUmdLekpuWElmLUhaYkxKTy1GMDRPZUY2VGJ0ejdoU3llYzV1dzR0UVcyQ25R?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 10 Sep 2026 19:00:00 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel (INTC) Advances High NA EUV For High Volume Foundry Production - simplywall.st；Monolithic vs. Intel: Which Chip Stock Has a Better Upside? - tradingview.com；嘉縣府攜手中正大學首辦280小時半導體職訓基礎班 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | -12.52% | N/A | 100.32 | 114.68 | -12.52% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +8.77% | +3.42% | 218.36 | 223.67 | -2.37% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -0.41% | +2.51% | 2,450.00 | 2,465.00 | -0.61% | 不適用 | 86.28 | 28.40 | 514.81B TWD / 53.32% | 2026-09-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | -0.35% | +14.00% | 142.50 | 164.50 | -13.37% | 不適用 | 6.68 | 21.43 | 25.04B TWD / 30.71% | 2026-09-01 |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | -2.42% | N/A | 503.60 | 521.10 | -3.36% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | +0.66% | N/A | 977.41 | 1,027.77 | -4.90% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -2.72% | +8.96% | 1,692.59 | 2,335.00 | -27.51% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -7.31% | -19.24% | 360.83 | 446.77 | -19.24% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC、Intel」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 3 篇新聞出現相關標籤。

### 主要來源

- [Intel (INTC) Advances High NA EUV For High Volume Foundry Production - simplywall.st](https://news.google.com/rss/articles/CBMiygFBVV95cUxOaFp1MThlODdmZnFLQkRXckZZWUZiQTJkb1pWRHR3T1lTNVhBLVl4d1gzYzNDLTh3bEVrOVVhaU1TaTFJR1BiZUhYSEVUVnJJVUdqNVB2TUJIbTVLSFZsNXVlVUdYTHpLTDlDaEJkT3phMmNZNjBqeGVmMGE0cTRzamZ3ZDJhdlQwdmJ4NS1LMUdZOHhhb1ZnSFp4ekh5Qm1oUmY2UVJZYTdQdVA2S04wcEpGV0tqUEFqSFR0bmJQNlNVN2RsVkFNdXVR0gHPAUFVX3lxTE5FeGlRSlVqSG02QWRDejNVbkFLY1NmT0czSkZIRGVuRzlZeDFORHNlbmhGcnJrQlVVYWtHeUVWM2FGaTVzYzV3am1wU1Jnd0pKMVFwV2V6RUpwSzRKZDc4dXFZTjJSSXlDOFZPTzZleXpnUFR4RnBheTI5RG1jOVlWTU9BS0hvYjVKdE56ZHlWckpTVmlINmJ0SXZKVGtUV3NZNGlrR09peTZsVktCZ3pNRzQ2bU1wajA5a2pEblVXbDc2ZkJiNVU3ZktNanhrNA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 10 Sep 2026 19:20:50 GMT
- [Monolithic vs. Intel: Which Chip Stock Has a Better Upside? - tradingview.com](https://news.google.com/rss/articles/CBMisgFBVV95cUxPd01HNFM5WnROQW4wRDF3ZVc4QnVMWi01YlprTnhzMlF3OGYwZGFqekVFVzBPeS10c0xYZUdsZkNBQ0RCcUZUajJXMUFNeFYxbTZYR3VqUmRzSTdQMl9XMmdfR1g5MTRYd1pEaXFCN01kY1lmVlVGYUNFLVhGRGJYdzZHSURFdktyWTYxZHozR0FsM3hvSkQ3NHNfU3h1dzV3UEp4Qm1ScWgzYmY3dG5UZUR3?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 10 Sep 2026 12:14:00 GMT
- [嘉縣府攜手中正大學首辦280小時半導體職訓基礎班 - 中央社 CNA](https://news.google.com/rss/articles/CBMiVkFVX3lxTE8tazh3Q25mdUJGSnVzd2ZieWQybUMyWkY5UHRZQTFKSnk2dXp4UFAxcFkzV1RlSndJaXk0UDk5bm9NcjRHMnItdTJXTGI1azcxWmZvNzRn?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 10 Sep 2026 07:39:04 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：油價飆高、擔心通膨與 Fed 動向 台股開低跌破47K 法人：台股震盪洗盤 - 經濟日報；〈美股早盤〉能源與通膨壓力夾擊！Fed下周升息機率達70% 主要指數開低 - news.cnyes.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +9.37% | +0.09% | 492.44 | 507.29 | -2.93% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [油價飆高、擔心通膨與 Fed 動向 台股開低跌破47K 法人：台股震盪洗盤 - 經濟日報](https://news.google.com/rss/articles/CBMifEFVX3lxTE5ma0ZCOUZucE52aUpHcGlBSDJleVQwd1k4QjJtT0NFUDhUbWVWZ0Z1YUlzM1BHMllLSHlEc0VxWVIyeDZodk9KeVBBRTlxRlUwQzFJdW1SRFFGUUFvVzdrOFpOSGFxYzRwdkxERHo1Z0xyZlNvdWk3bFR6aWTSAV9BVV95cUxOQlhpSGhIYzl2TUpuQXdLeFNmbWZCek9Cc0ZVcDU5ckYzTlZYaDFKNTUzZVQ0TW9GQXVGMld6ZDZkbWw4eDFlRHNFbUVtcllFbTg2amVJUTNscVJPb3VsQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 10 Sep 2026 05:12:27 GMT
- [〈美股早盤〉能源與通膨壓力夾擊！Fed下周升息機率達70% 主要指數開低 - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTE9jX3V5YlUzZnBQclo2MFQ3S2lSdHlMTGpDSldyY2JtWGFzanRMaHBGeVF0bXNKNWYxOHU1a1dENVNvN3JtN2dxSGR4WDlBdGM?oc=5) - Google News source discovery | 鉅亨網 Thu, 10 Sep 2026 13:42:45 GMT

## 新興題材：MarketBeat

摘要：新興題材：MarketBeat 相關新聞集中在：Intel (NASDAQ:INTC) Shares Down 5.6% - Here's What Happened - MarketBeat

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | -12.52% | N/A | 100.32 | 114.68 | -12.52% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel (NASDAQ:INTC) Shares Down 5.6% - Here's What Happened - MarketBeat](https://news.google.com/rss/articles/CBMisgFBVV95cUxNZEx4Xy14Nm5FaXo4MzMtZzRabC1xblZRVGNGR2Y3UTJ1ZE5oWHVvNXZnZHhCQUFVdGtwQTVlTHlBNFBlVGtQdmRUVjZ6Z2NjcG10RjJ1dUkwTWItUUl0QXJKcy1BMFctMmpQQW95MmZZUnh1Yms1SEtkWFE1WFp4R3lEQkI1TXRTTmRVLVFrZElfTHBOUEpXbmtQQVJHc0NwQkhHd3pMU1gxNHM5cGFmb0Zn?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 10 Sep 2026 21:56:27 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：緯創 AI 伺服器出貨翻倍，美銀喊目標價 265 元 - TechNews 科技新報；又一人離職，Anthropic 科學家：AI 幾年後就會毀滅人類 - TechNews 科技新報；被 AI 暴增的工作量逼到極限，微軟 Edge 全面擴大自動化驗證機制突圍 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 新聞直接提及 | +0.50 | +9.37% | +0.09% | 492.44 | 507.29 | -2.93% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 產業/供應鏈推估 | +0.04 | -12.52% | N/A | 100.32 | 114.68 | -12.52% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.06 | +8.77% | +3.42% | 218.36 | 223.67 | -2.37% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.03 | -2.42% | N/A | 503.60 | 521.10 | -3.36% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.04 | -0.41% | +2.51% | 2,450.00 | 2,465.00 | -0.61% | 未明確 | 86.28 | 28.40 | 514.81B TWD / 53.32% | 2026-09-01 |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -7.31% | -19.24% | 360.83 | 446.77 | -19.24% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.04 | +4.67% | +10.36% | 650.00 | 680.00 | -4.41% | 同向 | 13.92 | 47.03 | 82.25B TWD / 45.66% | 2026-09-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.03 | -0.84% | +8.76% | 4,720.00 | 4,720.00 | 0.00% | 未明確 | 60.69 | 77.95 | 64.18B TWD / 44.08% | 2026-09-01 |

關聯理由（前 3）：
- MSFT：新聞直接提及「微軟」，共 1 篇新聞命中。 同時符合主題標籤：AI, datacenter。 方向判斷命中詞：擴大。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：擴大。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：擴大。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [緯創 AI 伺服器出貨翻倍，美銀喊目標價 265 元 - TechNews 科技新報](https://news.google.com/rss/articles/CBMia0FVX3lxTE9OOTB0c2dSc2lGSkNsNkFjQTVJdEdrT3hNNmVINHVSYnZVd3hsdFV5eFI2Z0hUczl0SkV6S1RRUEgxalBEX2hnbGd2bTd4RnhoMVhrTTN4Y2NlMUlvbFlCUjFTZVE4SHpVUlRV?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 10 Sep 2026 06:02:55 GMT
- [又一人離職，Anthropic 科學家：AI 幾年後就會毀滅人類 - TechNews 科技新報](https://news.google.com/rss/articles/CBMitAFBVV95cUxQdkZUUVZGV3daWkVSQzdkNzljQ1JvcUVIYXM4NW9oemdOZkk5amZiZDJoZVBlZjhVTkhGVGxJc3FIdDJuQ1ZJbmxDSHhBRkw5aXJkRHowTUNxVEQtZnpUVF9iTGkxdmxPQnJmMVFRTVdHdm5LZkxZbThfb25DMk4xendlX2NjdmtxdVFGcmdHZjlLRnloWkNtS1RTYmloUGtudHA3aVhYaWc0d2RRVlNkbjl1aEk?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 10 Sep 2026 05:09:06 GMT
- [被 AI 暴增的工作量逼到極限，微軟 Edge 全面擴大自動化驗證機制突圍 - TechNews 科技新報](https://news.google.com/rss/articles/CBMi3gFBVV95cUxORXYxb2IyNVNBTTlJRVFsdTBoSEU4UGxxblVlZ2xhUXA3Rk56NmwxZzJaM3ZLOWxLdjBrZF9lclczNmRqaE5FRnFUajRTNmFMOXdUb01kTVFEWVJsYTdkRHlxZUk2eFJ3aVl1NTFjcXZ2a29NNkZqLWp5R3ZLcTlXSlVKTzQ0RUxMbjBCTnZlcXo0bDNRZm8wRjVzbHI2cTVHNGFoU3drZFc1QVRUUm5fRVBuMUpsRnp3OHJwT1dxNVFibHBpQnZZSWZSMnJCWmZodmNDWmVoWlhBYW9DUXc?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 10 Sep 2026 23:26:15 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Billionaire Stanley Druckenmiller Has Sold Micron, Broadcom, and Intel. Here's the Biggest AI Chip Designer Left in His Portfolio. - The Motley Fool；Memory Stocks Rally as Goldman Says the Worst May Be Over: SK Hynix Climbs 5%, SanDisk Advances 3%, Micron Gains 2% - 24/7 Wall St.；Micron, Sandisk and the Next Leg Higher in Memory Stocks - The Globe and Mail

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.43 | +0.66% | N/A | 977.41 | 1,027.77 | -4.90% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.28 | -2.72% | +8.96% | 1,692.59 | 2,335.00 | -27.51% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.21 | -12.52% | N/A | 100.32 | 114.68 | -12.52% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | +0.21 | -7.31% | -19.24% | 360.83 | 446.77 | -19.24% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +8.77% | +3.42% | 218.36 | 223.67 | -2.37% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、MU」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk、SNDK」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Billionaire Stanley Druckenmiller Has Sold Micron, Broadcom, and Intel. Here's the Biggest AI Chip Designer Left in His Portfolio. - The Motley Fool](https://news.google.com/rss/articles/CBMilwFBVV95cUxOS2JQeWtOUG9IamcxVUpOQjc5OHBtTGxucEFuTTlEOUl6cjhvVXhZazJZSDhGOGVJeTd4UE9RMFMxQTBRQWtUU0VxWXV2WXBjSGxfTC1zVk1WbXRMbXU1aUY3RlhINHVOMXBoUzRrcnNCNG1YVWhTcDFPampnM3ByclJJNXI3NVhtRUxMd1JVajZRVXF1aGpJ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 10 Sep 2026 13:26:00 GMT
- [Memory Stocks Rally as Goldman Says the Worst May Be Over: SK Hynix Climbs 5%, SanDisk Advances 3%, Micron Gains 2% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi6AFBVV95cUxQdlpVZDZOQlJpRVJ3SkcyeE5xOHpUUDJURkNnTFhva2xVaVBGLXdlaFJwN3M4dVVvM3kwZWREYjVxQVBoY095WTdDbWdCNGtoOVV0Znhtd1VaRGI3X1ZzemRtdnJwSWN6THpJZVpkclpOV2pXLUhJRGhTbWxObzdBam1tYTNxS2llZG93RXY5WVl2cjNyNlBNTllzVGN0STJrbHlSMjJ3ZmdDNWhzMUtEUmwteUIzUEZvbEd5VC1ZTUtKYVZ1UTJiOUZSQkFoVWxoakhTU0RrM2xsbnR3aXF4czAwT2FwWF9C?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 09 Sep 2026 15:20:00 GMT
- [Micron, Sandisk and the Next Leg Higher in Memory Stocks - The Globe and Mail](https://news.google.com/rss/articles/CBMi1wFBVV95cUxQc01pUHdaSkdHaTQ4Qk5pU1UyMkhEX0ZCTjgzejVlUXFHWDBTWS1Tekd3WFlWay1NZ3VVNkRiY0kxbEVIY0c4bWRMVEtUZFRMMXBFMVNnUTZQeEhRM2JuaDlfVlZPbG1zb0YxNnMtZ1VXTmRBb3ZsSGVHNHNTLW00TTN2WmtVLVBXNDBsTEFKY0V5OExrZlJYZGJ6b3NPR0lGMldqZmwydjZHWnlEWVZzcGIxZzlydGpDMTNfcWJieUF5TEh2b2pHM3hiNEdxeWFtMEdhUnlFTQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 09 Sep 2026 20:52:26 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股市值型 ETF 帶勁 - 經濟日報；台股價跌量縮 外資落跑 | 市場焦點 | 證券 - 經濟日報；9月台股期指跌308點 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股市值型 ETF 帶勁 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBvbnZtWHZHMTlwQzZ6RG81X2hXNlp4bjgzWWZnSXJoRnJwRTNpNDdLSXR6a0JRS2poNXBhR1BzclJWVGNzdm5sVG5TVVFhZVdtNmFkM2VKVHZud9IBX0FVX3lxTE1UTFU2emZGRzBQUXBCRzJtb1V5VU1iTGhMelNKNFBvZmpBNGc1SVJpcktWekl6U0p5ZlJOY0RKa3ZORnh1ODlIa2JTWlVjd0xTUmRxNng3dktzdEFOY1Bv?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 10 Sep 2026 17:59:34 GMT
- [台股價跌量縮 外資落跑 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5lWFUzSEIzb0lLZUQzeUswLVE4ektUakstcmtZZUxRUUNYaTZTRnhOUm9mMl9YRDZaTW5pS1VXVFhtaUx0SzRkcHBQYnZZNmM3MXhlUnI1ZEpmQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 10 Sep 2026 17:11:39 GMT
- [9月台股期指跌308點 - 經濟日報](https://news.google.com/rss/articles/CBMie0FVX3lxTE1tRWNzajc2b2NLZzBFbHhjMDV5SHVyYk9GM1JmZkdMT1Vodjh5dTY1SlZpSW9hdV9yblI0Z2toS0RrRzZZbUUwaG1na2s2czZBN3lTUTJ4cDdEc2NxR3YzTGkySnd1TjdwenJjdmZtZFAyWXNVZDRnMmFKY9IBYEFVX3lxTFBtWWlhWkNzbmI5V3owT3I0dzJvR1VBQnVfZnlkVUxybXVzQWlIWW5iTGZ5TW5KekxDbFZHMkxxT2Q5Qk9pa180ZWYwRUN2RVhUNVNtbGRzUWUzZy0tM3dRRQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 10 Sep 2026 06:13:28 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》收跌242點、失守47K，10日線有守-新聞內容-基金 - MoneyDJ；16檔台股ETF規模創高 00919近月漲幅居冠 - MoneyDJ；【台股操盤人筆記】Fed利率會議後，Vera Rubin接棒基本面行情 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》收跌242點、失守47K，10日線有守-新聞內容-基金 - MoneyDJ](https://news.google.com/rss/articles/CBMikwFBVV95cUxPZGhfSWVNZ0o1TWI3UFZPb3J1OHdGYUpCLTBwOGxkbElPd0xmVEVSYWNpY29Qd2Y4QmNEQ200aXFqWEx2bDR6S3EtRjgxZ1l4UjkwQjBnSGV6aVZJaEhqOXppTmllLUVKQ24zSzlDclE2YkVITFlhVk5hVXNjS3RFSHJDUnZrNWVpMjlBYjJlbmhoWk0?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 10 Sep 2026 08:00:49 GMT
- [16檔台股ETF規模創高 00919近月漲幅居冠 - MoneyDJ](https://news.google.com/rss/articles/CBMiiwFBVV95cUxPSzMtM0VLYTFtZzR4NlF6RlV4VWdZbkROQUxxNkp2aW9hbzdxbU0tQTZmM0JFSVNJcVljc3RVYmd0MW5vUXRfMUpLVi1xVGZWaXpkTXB6U1lxaFFScjFHU1VRVE9qekl6S05TME9acGtvenl3SS1TYUl1b0d4TGxpOFFqa1lDN0lGZXBB?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 09 Sep 2026 03:28:00 GMT
- [【台股操盤人筆記】Fed利率會議後，Vera Rubin接棒基本面行情 - MoneyDJ](https://news.google.com/rss/articles/CBMilwFBVV95cUxOSmZXTERGWVk0d2hPV2RiV19BUGlhNUlnRTJLU2h2MEcxb19EdVY1NjhCbF9vMWp3NEJfR0pXbi1aeXJUMDY4MUNWU0J6MER3Y3BiNmNYVVV2endENUlNdmVRX0paTG9mZ0o0VUNEZmlpUVB5VFZMYzN3M3diOV9GSThVY2w2SjlGTnJwVllrc2JmbkNVNlVZ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 10 Sep 2026 02:08:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
