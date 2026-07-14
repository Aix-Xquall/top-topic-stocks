# 每日股市熱門話題分析 - 2026-07-15

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜負向｜熱度 11｜市場確認 86.23｜同向 1/1
2. **關稅與供應鏈轉移**｜負向｜熱度 3｜市場確認 N/A｜同向 0/0
3. **利率與成長股估值**｜負向｜熱度 6｜市場確認 N/A｜同向 0/0
4. **半導體與晶片供應鏈**｜中性｜熱度 4｜市場確認 N/A｜同向 0/0
5. **散熱與液冷供應鏈**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.20（樣本 7）
- 5日相關係數：-0.16（樣本 7）
- 同向比例：2/7

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 86.23 | 1/1 | 0 | +5.41% | -8.66% |
| 關稅與供應鏈轉移 | N/A | 0/0 | 0 | N/A | N/A |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 0.54 | 1/6 | 4 | -3.71% | +0.77% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-07-02 | 0.30 | 0.03 | +55.56% | 9 |
| 2026-07-03 | 0.21 | 0.08 | +55.56% | 18 |
| 2026-07-04 | -0.22 | -0.36 | +22.22% | 18 |
| 2026-07-05 | -0.00 | 0.24 | +40.00% | 10 |
| 2026-07-06 | N/A | N/A | 0.00% | 2 |
| 2026-07-07 | N/A | N/A | 0.00% | 1 |
| 2026-07-08 | -0.05 | -0.05 | +71.43% | 14 |
| 2026-07-09 | -0.11 | -0.36 | +64.29% | 14 |
| 2026-07-10 | 0.55 | 0.05 | +77.78% | 9 |
| 2026-07-11 | 0.13 | -0.08 | +50.00% | 12 |
| 2026-07-12 | 0.27 | 0.13 | +16.67% | 12 |
| 2026-07-13 | 0.39 | -0.09 | +15.38% | 13 |
| 2026-07-14 | 0.10 | -0.07 | +21.43% | 14 |
| 2026-07-15 | 0.20 | -0.16 | +28.57% | 7 |

## 歷史回測摘要

- 回測日期：2026-07-15
- 近5日 3日相關：0.08
- 近5日 5日相關：0.10
- 同向比例：+27.27%
- 權重狀態：已調整

- 方向準確度：+27.27%
- 信心排序準確度：0.08
- 診斷：低相關

調整原因：近 5 日信心分數與股價關係偏低，提高價格確認，降低寬題材推估。；關鍵詞×公司後續樣本有效 5 筆，未達 30 筆，不調整樣本權重

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

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：台股創高後震盪翻黑收跌640點 記憶體股賣壓沉重 - 經濟日報；Intel, AMD, and Applied Materials Drop 4% as SK Hynix Rout and Oil Spike Hit Chip Stocks - 24/7 Wall St.；SK Hynix Soars 19% as Leveraged ETFs Launch, Lifting Micron, SanDisk, Western Digital - 24/7 Wall St.

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | -0.50 | N/A | N/A | 983.12 | 983.12 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.50 | -5.41% | +8.66% | 1,757.82 | 2,335.00 | -24.72% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.37 | N/A | N/A | 548.13 | 557.89 | -1.75% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | -0.37 | N/A | N/A | 107.76 | 114.68 | -6.03% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +0.31% | +21.44% | 211.80 | 211.80 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、memory」，共 4 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：fall, weak。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：fall, weak。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [台股創高後震盪翻黑收跌640點 記憶體股賣壓沉重 - 經濟日報](https://news.google.com/rss/articles/CBMiggFBVV95cUxOLUN4Z2ZNQldtWGNhc2NtWHZoYXFjM2tCVEpZZ2xlZXQyMEZkN3oyOVg2VU1hNHZMX3NTeGpCd3NXQnJyUjJ0dDhkdFBONmE2WGs3Rm8wV0YwUnhwYThIRFBtbXlrUTZKTDN5NnhCODljNzY2NVVkeWZnUm1RRThZU3B30gFfQVVfeXFMT05wWWF6T3NwVWpzcDYtWi01VDd3ZzgzXzJ1YUt1MDk1X3g3SmJJQjVLZEY0N1FJZzNWck9XaW5qWTR3RE1UdmpyeGVpUE5UM0c4N29BUjVEV1RMV2VqZzA?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 14 Jul 2026 13:14:28 GMT
- [Intel, AMD, and Applied Materials Drop 4% as SK Hynix Rout and Oil Spike Hit Chip Stocks - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiyAFBVV95cUxPVUNTQ043RnZkVTV6SnVvcEt3QkhMYWJONkRrWUVUQnBOV0dsVFRkRWtxR1U3Vk9lU1Q3aDI0R1RjMDhubEVtRTlUUmxfUXJZUi1mU1BWLUxKUnhsZWpkV3NtNGlGQkdKVzlYNGJjMFFYS2tmNEJEY210NkJMVlRhUklzN2NqaWMxWEdsYW1kT2J1OHdJRmNoLWR5Z3JPVEc1QThmbm95RWpNdThUeS1oVGxhZG1VeFhLTHhYb2FJOFBvWERxcVhmRQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 13 Jul 2026 14:22:17 GMT
- [SK Hynix Soars 19% as Leveraged ETFs Launch, Lifting Micron, SanDisk, Western Digital - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiyAFBVV95cUxPODY3M25aLW02T2dXb3FwYnJhVmVsX01udnJRVTdRM2NjUUd0LVRHTVFGTXN5SXZpWHNMZlBMSFBSWFlEdjVQX1pxZXU3LUhCampRdHJ3dWpicDQtdzY5ZExLcTRzakZzREhGRXdDTlYwRjlVb1RJcjhBTjdWTVQ1R0M3MExoc1FVMHZ0QkZYWTF5eFVNMjdqQmJRajFnWnJhOTlSUTRBNEFCUTlxdVVMVHVjWlJwaGgzYUFjRHc3RV9McmJ3d2ZGcg?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 14 Jul 2026 16:23:02 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：AI帶旺半導體供應鏈上市櫃公司6月營收齊揚| 證券 - 中央社 CNA；2027 年 記憶體大缺貨，對 AI 供應鏈有何衝擊？ - TechNews 科技新報；先進製程漲價，如何影響 AI 供應鏈？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +19.18% | +35.63% | 314.86 | 315.32 | -0.15% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | -0.84% | -2.69% | 235.50 | 289.00 | -18.51% | 不適用 | 14.13 | 16.73 | 821.76B TWD / 52.11% | 2026-07-01 |

關聯理由（前 3）：
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [AI帶旺半導體供應鏈上市櫃公司6月營收齊揚| 證券 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE9WSTY1bnBrM2FCZkxaVHV0bEMxQXFPQk1jSG40NFBRUzcwRXcwdnh5OXB5ZDFRY0FoSGN5YVdGTDd2ZUZxeDJXc3pGMHJXODQ1RVlFMEdtUjJSbEhqcnc?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 14 Jul 2026 11:14:00 GMT
- [2027 年 記憶體大缺貨，對 AI 供應鏈有何衝擊？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMitgFBVV95cUxOcnR4dkViMnJKNFlEc0dvS0FZb29xTVd0b2N1LTJmaEdoaWRFOUd3SHFGWTh2XzJRbGpBVi1kcjE3SENmem05UUROeTFLek91SmNNaVBnS2RCbmhEZFIyZTJiTVFPZ0QwZ1gzYjdhRWQ0WWRJYnFXb2hTMW9BZUo5MjN1X0Yyd3FBcXJKY3RYN3RhcnlXVHI3ek9WZGVFZ2doYWdNcDJ6aXZFdDd5aUVwT2wxX0M2QQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 14 Jul 2026 19:08:46 GMT
- [先進製程漲價，如何影響 AI 供應鏈？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMilwFBVV95cUxNMnYzVnlUTW5BNmhtWnpmb1hPby15dXlQU3BYZlU5SmxWbjhRWDJoSnl6RjJGaU5SYzVMWVhtVGVvQ1VWLU03ckJrV0NlN3A2Rmh0RDVDR2M2M2pEdF9LbkRESUtDM2RZb3R5MTVQYi01WmIzU0xjUzdRdGpETks5RnlWSVJZSWdoenJFM0hmOHNHQU1KRkpF?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 14 Jul 2026 13:26:04 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：AMD Rallies 5%, Intel Rises 4% as Cooling Inflation Sparks a Chip Rebound - 24/7 Wall St.；AMD Rallies 5%, Intel Rises 4% as Cooling Inflation Sparks a Chip Rebound - AOL.com；S&P 500 and Nasdaq end higher on cool inflation data, solid bank earnings - Reuters

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AMD 超微 | 新聞直接提及 | -0.51 | N/A | N/A | 548.13 | 557.89 | -1.75% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | -0.51 | N/A | N/A | 107.76 | 114.68 | -6.03% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | -1.99% | -24.03% | 384.93 | 506.69 | -24.03% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AMD Rallies 5%, Intel Rises 4% as Cooling Inflation Sparks a Chip Rebound - 24/7 Wall St.](https://news.google.com/rss/articles/CBMitAFBVV95cUxOQnhNeDh3Tko0WXVGWDNtZ3FyWXhPR1pJMGRjSWdkX1YxLUdXSklJb0RUM2R6YjJaMENWbThkVVBsREFVeFVsclNRRW5MVzJndWdBNVliU2hvMGRvNUdlZEV5bE14S0kzWDRoWlpJQmNyRm5jbDV6OXNFakQ3Wk9HZS1BN01fRzRTV1A2UExaUmxuZm5QcEpHcVFHWjNWMGhGcENOb3l1UUxLUlhlZ0FHcDdMYXc?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 14 Jul 2026 13:42:38 GMT
- [AMD Rallies 5%, Intel Rises 4% as Cooling Inflation Sparks a Chip Rebound - AOL.com](https://news.google.com/rss/articles/CBMieEFVX3lxTE1WdHQ4Y2hFWUpCbGhReF9leFhyV2M1NUpXTDBET29JSkdIUXFxQmtMaUwydmcyenFoUldhaTA1TGNYeFJxckJzWms5TjJRVk9ORXA1NmNGUDhPSjB5eXk2V2lucEppZHBJWGxyeFhmUE9pZTlnaFFIeg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 14 Jul 2026 13:43:45 GMT
- [S&P 500 and Nasdaq end higher on cool inflation data, solid bank earnings - Reuters](https://news.google.com/rss/articles/CBMivgFBVV95cUxPNUZzZmRoMHJILU51eUxkVEo5UmFGNUx3WjUwSU9qX0k5Zzk0Ulk0MUY3aGZQc0pTVUpQb0F4MUNiQ2RwY1F4ekptWjBJTkExaWhqRE9sLTRNTU84a09pS2lUV19wLTJ4LXgtU0VXY2RHQ3RHampMUE5MTVVQTjYzM1I4V1lfdVc2UFZGOHdPY1BOVEhWUDcxTVBkX3R4QzZON18xejctM09QU3VxbXprSDRWQXJhMVAzbjUxR3JR?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 14 Jul 2026 20:21:10 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel (INTC) Is Spending €5 Billion To Expand AI Chip Production In Ireland - simplywall.st；TSMC vs. Intel: Which AI Chip Manufacturing Stock Has More Upside Now? - TradingView；Intel Stock (NASDAQ:INTC) Lags Chip Rebound as $5.7 Billion Ireland Bet Raises Cash-Flow Bar - TechStock²

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 107.76 | 114.68 | -6.03% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | 0.00 | -1.83% | -1.63% | 2,420.00 | 2,420.00 | 0.00% | 不適用 | 74.39 | 32.54 | 442.68B TWD / 67.87% | 2026-07-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | -7.36% | -9.04% | 151.00 | 164.50 | -8.21% | 不適用 | 4.00 | 37.94 | 23.12B TWD / 22.85% | 2026-07-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +0.31% | +21.44% | 211.80 | 211.80 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 548.13 | 557.89 | -1.75% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 983.12 | 983.12 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -5.41% | +8.66% | 1,757.82 | 2,335.00 | -24.72% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -12.91% | +25.72% | 389.11 | 446.77 | -12.91% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC、Intel」，共 3 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「TSMC」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip, foundry。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 3 篇新聞出現相關標籤。

### 主要來源

- [Intel (INTC) Is Spending €5 Billion To Expand AI Chip Production In Ireland - simplywall.st](https://news.google.com/rss/articles/CBMiygFBVV95cUxNcEJYNVVPOTZQdTZCdWQybEdUV1hnSDBnTVlod3ZackRraTd1ZjZUVnZCdzF4WHUzVEZTbGtpNndIWVNfQmNXNTJkQ2lVY21PQnJ3LWtUN3pLVzZGMTJEejMwQ1FZOEVfU1pKTTFkemh0M0ptcHI4bTN1QlpkUUFjWXprbkhXRm5Zb1I1MzBXOVJXckNHaXBxVHpEVS1qVWlnVDU0d0FOcEhtM1dNMGhHRjZMV3NERVNldGd6R2lVOFluY3ozQlRZNDhn0gHPAUFVX3lxTE9nVGVDLUxnamZFcVRDSUNnRTh6amFLaWYzWGpZWnFaN0lXRTlZTDByMFl5dUZJdlZQQ0dUR3RReEdpOXlPV05hZ2FLbk1ONzBTdHdYUnNtWjA0SVBYekZRUzhYOVZ6eGZIY3hOY1ZtZ2MzOWxDQ0taT0JBQVpITERySFBQdTFXVmprZEFud3hsVms5RURncWV6VWFSRVQ3cEhGM25IVTNsNXkydkc3OEJsdHk5Qm9TT2YzMTJSMmgzaGVGQ1hVRnkyazRvbUx6aw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 14 Jul 2026 17:34:02 GMT
- [TSMC vs. Intel: Which AI Chip Manufacturing Stock Has More Upside Now? - TradingView](https://news.google.com/rss/articles/CBMiwAFBVV95cUxNdXRqQmNLUkI4VnAyR1B3QllsbVVRYVBGZ0c4eU5PNGhmaFhxZzRqUWJpNFJfZTQ4bWN2d000TE5xS3JNY21oZ3ZWSXFhVG10bGZsMlg0MnN5SW4yN3FaQnh1R2t0YkdUQzhjaENlSkwtQ0cxWlNHSnZxcU1ZUW82c2JaWXV5MTFobWlPN3F2c29oTnBCSmxKaVFRMXdsM1A4NG9FOGkyVWxNcmZkSktjRmwwN2RDdTVyMGxPbEJKYl8?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 13 Jul 2026 12:48:00 GMT
- [Intel Stock (NASDAQ:INTC) Lags Chip Rebound as $5.7 Billion Ireland Bet Raises Cash-Flow Bar - TechStock²](https://news.google.com/rss/articles/CBMirgFBVV95cUxOQ2NYUVpTaTZiN2o4Z09hODU3c3J4TEpLUzVCUkJCR0lDZDJrRkllaXVCNTNxdEZEY3NFVzVtRzRyVmVlY0VMRmpaUGNSVXRCNmg1M0IxNUE1WHhoSEl3OERPSG1qTWZOU2hHLVZtaHVSRVFXNUdEZTlDaHZiZjlhcUl5OXpOTGZpdUluNDJ3MHNOOG1zN0hoU2Y2MGhBQmpkNkIyNkVfLUNsTEtxd0E?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 14 Jul 2026 15:42:12 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：AMD Rallies 5%, Intel Rises 4% as Cooling Inflation Sparks a Chip Rebound - 24/7 Wall St.；AMD Rallies 5%, Intel Rises 4% as Cooling Inflation Sparks a Chip Rebound - AOL.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AMD 超微 | 新聞直接提及 | 0.00 | N/A | N/A | 548.13 | 557.89 | -1.75% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 107.76 | 114.68 | -6.03% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 3017 奇鋐 | 產業/供應鏈推估 | 0.00 | -8.82% | -20.60% | 2,120.00 | 2,835.00 | -25.22% | 不適用 | 61.06 | 34.83 | 17.62B TWD / 66.11% | 2026-07-01 |

關聯理由（前 3）：
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 3017：產業/供應鏈推估：公司標籤符合「散熱與液冷供應鏈」關鍵字 thermal；其中 0 篇新聞出現相關標籤。

### 主要來源

- [AMD Rallies 5%, Intel Rises 4% as Cooling Inflation Sparks a Chip Rebound - 24/7 Wall St.](https://news.google.com/rss/articles/CBMitAFBVV95cUxOQnhNeDh3Tko0WXVGWDNtZ3FyWXhPR1pJMGRjSWdkX1YxLUdXSklJb0RUM2R6YjJaMENWbThkVVBsREFVeFVsclNRRW5MVzJndWdBNVliU2hvMGRvNUdlZEV5bE14S0kzWDRoWlpJQmNyRm5jbDV6OXNFakQ3Wk9HZS1BN01fRzRTV1A2UExaUmxuZm5QcEpHcVFHWjNWMGhGcENOb3l1UUxLUlhlZ0FHcDdMYXc?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 14 Jul 2026 13:42:38 GMT
- [AMD Rallies 5%, Intel Rises 4% as Cooling Inflation Sparks a Chip Rebound - AOL.com](https://news.google.com/rss/articles/CBMieEFVX3lxTE1WdHQ4Y2hFWUpCbGhReF9leFhyV2M1NUpXTDBET29JSkdIUXFxQmtMaUwydmcyenFoUldhaTA1TGNYeFJxckJzWms5TjJRVk9ORXA1NmNGUDhPSjB5eXk2V2lucEppZHBJWGxyeFhmUE9pZTlnaFFIeg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 14 Jul 2026 13:43:45 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel (INTC) Is Spending €5 Billion To Expand AI Chip Production In Ireland - simplywall.st；TSMC vs. Intel: Which AI Chip Manufacturing Stock Has More Upside Now? - TradingView；未來 AI 圖像生成是否會成為個人品牌的標配？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.59 | N/A | N/A | 107.76 | 114.68 | -6.03% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | +0.27 | -1.83% | -1.63% | 2,420.00 | 2,420.00 | 0.00% | 背離 | 74.39 | 32.54 | 442.68B TWD / 67.87% | 2026-07-01 |
| NVDA 輝達 | 產業/供應鏈推估 | +0.04 | +0.31% | +21.44% | 211.80 | 211.80 | 0.00% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.06 | N/A | N/A | 548.13 | 557.89 | -1.75% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 產業/供應鏈推估 | +0.02 | -1.99% | -24.03% | 384.93 | 506.69 | -24.03% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -12.91% | +25.72% | 389.11 | 446.77 | -12.91% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.04 | +2.56% | -5.60% | 641.00 | 680.00 | -5.74% | 同向 | 10.86 | 59.52 | 65.78B TWD / 32.86% | 2026-07-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.02 | -8.39% | -11.27% | 3,660.00 | 4,310.00 | -15.08% | 背離 | 62.91 | 58.33 | 58.01B TWD / 2.80% | 2026-07-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC、Intel」，共 2 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：上修, 成長。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「TSMC」，共 1 篇新聞命中。 同時符合主題標籤：AI, advanced packaging, CoWoS, AI server。 方向判斷命中詞：上修, 成長。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：上修, 成長。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel (INTC) Is Spending €5 Billion To Expand AI Chip Production In Ireland - simplywall.st](https://news.google.com/rss/articles/CBMiygFBVV95cUxNcEJYNVVPOTZQdTZCdWQybEdUV1hnSDBnTVlod3ZackRraTd1ZjZUVnZCdzF4WHUzVEZTbGtpNndIWVNfQmNXNTJkQ2lVY21PQnJ3LWtUN3pLVzZGMTJEejMwQ1FZOEVfU1pKTTFkemh0M0ptcHI4bTN1QlpkUUFjWXprbkhXRm5Zb1I1MzBXOVJXckNHaXBxVHpEVS1qVWlnVDU0d0FOcEhtM1dNMGhHRjZMV3NERVNldGd6R2lVOFluY3ozQlRZNDhn0gHPAUFVX3lxTE9nVGVDLUxnamZFcVRDSUNnRTh6amFLaWYzWGpZWnFaN0lXRTlZTDByMFl5dUZJdlZQQ0dUR3RReEdpOXlPV05hZ2FLbk1ONzBTdHdYUnNtWjA0SVBYekZRUzhYOVZ6eGZIY3hOY1ZtZ2MzOWxDQ0taT0JBQVpITERySFBQdTFXVmprZEFud3hsVms5RURncWV6VWFSRVQ3cEhGM25IVTNsNXkydkc3OEJsdHk5Qm9TT2YzMTJSMmgzaGVGQ1hVRnkyazRvbUx6aw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 14 Jul 2026 17:34:02 GMT
- [TSMC vs. Intel: Which AI Chip Manufacturing Stock Has More Upside Now? - TradingView](https://news.google.com/rss/articles/CBMiwAFBVV95cUxNdXRqQmNLUkI4VnAyR1B3QllsbVVRYVBGZ0c4eU5PNGhmaFhxZzRqUWJpNFJfZTQ4bWN2d000TE5xS3JNY21oZ3ZWSXFhVG10bGZsMlg0MnN5SW4yN3FaQnh1R2t0YkdUQzhjaENlSkwtQ0cxWlNHSnZxcU1ZUW82c2JaWXV5MTFobWlPN3F2c29oTnBCSmxKaVFRMXdsM1A4NG9FOGkyVWxNcmZkSktjRmwwN2RDdTVyMGxPbEJKYl8?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 13 Jul 2026 12:48:00 GMT
- [未來 AI 圖像生成是否會成為個人品牌的標配？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMikAFBVV95cUxQd2dSdXlhUUczQzlQZGtWbE9Yc1BnWTg5ZTV2SGpiT050NU1jWE0tbU5KdTh1WUc4MDg3enY2cXE2ZmdKalJLYV9senRVYVpFcm4wb1FJZW1ROVp1QUVPUDJVZWNaaEpNT3ZqdEkzck5NVEtoTUl1eWVGZVQ2YTV6cmZxOTA2TlBCWll5aEdSVGM?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 14 Jul 2026 20:31:23 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股血洗1500點、連破45K、44K 兩大關卡！後市怎麼走、專家全說了 - 經濟日報；台股收跌1568點　金管會：跌幅介於亞股之間 - 經濟日報；台股行情V轉…主力、投信救市 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股血洗1500點、連破45K、44K 兩大關卡！後市怎麼走、專家全說了 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1tMlRNa3pCOTA1TE5FUnNMcjloRFdYTEtfbDBtVnpJcmxQa1J0YlJNWjBUUGg3QS16VHh1NlljdjR3ZEQ0R20tMFV0c2FhVUhlMjZMRFNpRWdkZ9IBX0FVX3lxTE5Ccl91S2RCVnhkM0NuNjl6NzBGNmhGZFZjZVNzV0Z3bjY4ZkVVRWJXRzZmMjlFd1hoM0ZmeklLeThNRk9WMy1XMmt1LS1zSmJxRUh1VGJOOXBveFAyX3ZZ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 14 Jul 2026 02:38:20 GMT
- [台股收跌1568點　金管會：跌幅介於亞股之間 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxNMjlTalJSaFZYR2VFV28wZlVFLW9ic25zR000TU8yTlp2VldNenI1MFQzbjlxblN2Z0V6b09NZnFEYlpsQU40OTBBdnBYMXZsNEpvdnJBZHBRWHhfZVlzWlhTbDdwRmxzQjYwSURGYVBaSm80WnMxVGlHVUYyQ3U3eNIBX0FVX3lxTFBkZWtqaVBUeXcwTnNlUGNaOXZ0eTNMUjF3SjZUOGw1THRXME95Y2p4VDg0R2EtMU5jSllKWW5OVjhnM2lMTVVBelZLUlNETFpIOU9XaUdqcXJHV3hzZ2Zr?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 14 Jul 2026 19:34:50 GMT
- [台股行情V轉…主力、投信救市 - 經濟日報](https://news.google.com/rss/articles/CBMifEFVX3lxTE1seXd5eW5hUmpRNmNUdlR3Z1FEZW1nQ0V6YmNKeEZKMjZCd3VkeEgtcVVBcDg2TTZEWnpRQ0hGa3N0UVpFTzRQeFBYSjMxUXJpcTFQaGVjdVZQNE1UTkQtWVNwWDRrTXdEUzNpeHRQSk9Zenh5TnJGeVhicjPSAV9BVV95cUxORHFvaXM3NkFPRlR4cjZYUHNLLXJGMl92ZkVOUFZlcVBKdG1YQ1h4aDBQclhzWGJvMk1MMFpkcjdDa2FOV2laQlV5cEVVWXRyT2hEVE1YQzFpMzkwUHI1RQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 14 Jul 2026 17:23:24 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：台股重挫 台幣早盤放量貶值2.2分 - MoneyDJ；《台股盤後》午盤拉逾千點 終場跌642點收44737點-新聞內容-基金 - MoneyDJ；第一金台股趨勢優選主動式ETF基金六月份經理人評論 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股重挫 台幣早盤放量貶值2.2分 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNQV9SN1lpbEpqVUlsTS1JbHhTcXJjNkxZbHVCMXhHV0JRYW9Eall5QUs3RkNOREpVLVJJbnVNc3F0VXRGRG50N19zdHlneDVKNXR5YTNVQVk3czZiZ29yUFhoaXJKNEI3d2FhQ3Z6Tm41aTh5SmVFVGpkS096Ni13bjR3UTBqbWpkWlVISDBidlBsdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 14 Jul 2026 04:20:00 GMT
- [《台股盤後》午盤拉逾千點 終場跌642點收44737點-新聞內容-基金 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxON1BVM2FnaVlOWUhodUxYSE93eEIxNVN1WG9PeHFHVzFHdHB0T2Rnd19MMWl6enlObk5ONExTRWZxRmQ1R01DeUJ3NE9sdHhZRG5WeVZ4MDFuYXM3MWJwMFI0NVRGYUVxbktZQ25KMmVpZEhWS0owSW9Ec3lUWVUyOUYyTHRRM05IcnpvQzJSS20?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 14 Jul 2026 08:08:00 GMT
- [第一金台股趨勢優選主動式ETF基金六月份經理人評論 - MoneyDJ](https://news.google.com/rss/articles/CBMilwFBVV95cUxPUUh2bmFTcVdfZ2N0SVZOMll0ekltcW4xaVFuMERqSEs2cTlVQTZnbVlHallNWm9PWGV6T3N2ZVpSS1VrLTBkZDRFX0hsc3U4Y1hIMGJkU0pXc2h6Z1dnaWVPRVUzQXRXdWpOMWN5Qmx0dkFnTTZYemEwLXJKVWNWN1p0UENxWVVwbjYwTVpiQ1c4RWhObmc4?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 14 Jul 2026 06:11:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
