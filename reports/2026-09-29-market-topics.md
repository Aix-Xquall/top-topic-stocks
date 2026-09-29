# 每日股市熱門話題分析 - 2026-09-29

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **AI 伺服器與資料中心**｜中性｜熱度 19｜市場確認 N/A｜同向 0/0
2. **記憶體與 HBM 供應鏈**｜中性｜熱度 8｜市場確認 N/A｜同向 0/0
3. **利率與成長股估值**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0
4. **新興題材：OpenAI**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
5. **半導體與晶片供應鏈**｜中性｜熱度 5｜市場確認 0.00｜同向 1/5

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.31（樣本 6）
- 5日相關係數：-0.78（樣本 4）
- 同向比例：1/6

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| AI 伺服器與資料中心 | N/A | 0/0 | 0 | N/A | N/A |
| 記憶體與 HBM 供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：OpenAI | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | 0.00 | 1/5 | 3 | -6.17% | -4.95% |
| 散熱與液冷供應鏈 | 0.00 | 0/1 | 1 | -4.10% | -11.62% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-09-16 | -0.19 | -0.46 | +55.56% | 9 |
| 2026-09-17 | 0.43 | -0.13 | +66.67% | 9 |
| 2026-09-18 | -0.15 | -0.07 | +35.71% | 14 |
| 2026-09-19 | 0.20 | 0.47 | +46.15% | 13 |
| 2026-09-20 | -0.04 | -0.25 | +30.77% | 13 |
| 2026-09-21 | -0.15 | -0.05 | +61.54% | 13 |
| 2026-09-22 | -0.00 | -0.01 | +88.24% | 17 |
| 2026-09-23 | 0.35 | 0.22 | +80.95% | 21 |
| 2026-09-24 | 0.05 | 0.42 | +90.00% | 10 |
| 2026-09-25 | -0.31 | 0.15 | +30.77% | 13 |
| 2026-09-26 | 0.22 | 0.14 | +63.64% | 11 |
| 2026-09-27 | 0.11 | -0.14 | +57.14% | 14 |
| 2026-09-28 | 0.05 | -0.53 | +63.64% | 11 |
| 2026-09-29 | 0.31 | -0.78 | +16.67% | 6 |

## 歷史回測摘要

- 回測日期：2026-09-29
- 近5日 3日相關：0.11
- 近5日 5日相關：-0.00
- 同向比例：+60.00%
- 權重狀態：未調整

- 方向準確度：+60.00%
- 信心排序準確度：0.11
- 診斷：弱正相關

調整原因：近 5 日有效樣本 5 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：AI 伺服器與資料中心 相關新聞集中在：3 AI Infrastructure Stocks Facing Higher Rates And Rising Data Center Demand - simplywall.st；Intel Shares Ride AI Server Boom to Best Year Since 1981, but History Flashes Caution - finance.biggo.com；AI 寫錯判例還不夠，這次直接捏造證人：法律專業還能相信生成式 AI 嗎？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +14.00% | +8.39% | 228.86 | 228.86 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | 0.00 | +1.18% | N/A | 116.03 | 127.39 | -8.92% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | +17.78% | N/A | 607.87 | 629.26 | -3.40% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -0.20% | +2.06% | 2,485.00 | 2,485.00 | 0.00% | 不適用 | 86.28 | 28.69 | 514.81B TWD / 53.32% | 2026-09-01 |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +13.10% | +3.50% | 509.22 | 509.22 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -10.20% | -21.76% | 349.57 | 446.77 | -21.76% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | +5.43% | +13.84% | 690.00 | 699.00 | -1.29% | 不適用 | 13.92 | 50.58 | 82.25B TWD / 45.66% | 2026-09-01 |
| 2454 聯發科 | 產業/供應鏈推估 | 0.00 | +5.49% | +17.44% | 5,175.00 | 5,285.00 | -2.08% | 不適用 | 60.69 | 87.28 | 64.18B TWD / 44.08% | 2026-09-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [3 AI Infrastructure Stocks Facing Higher Rates And Rising Data Center Demand - simplywall.st](https://news.google.com/rss/articles/CBMi3wFBVV95cUxOXzF1ZmU0cWJzandwaVJiZTZ5Y2VOaWJBQnZ0NnZwR0JacEZ3M0lNWDFlbVhFbS0wM2RDUzJmUmwySWtsZjZHTlhDb042cWRBN2RnaUlBTW1Db2NOdmxpWC1EOXlUSy1MWWJmc0xXeDh4blMyQllwQ1ViOEYxamFyYmkwd3d5NjZnM3pkZ0QtMmZsblZ4emVfSkMzSkYwR2xwdUwzQVFoNC1hZXpySTZEdDhvd091UU5BNGxyeTRMQm1ISFZ0ZGNPbTFYNnFfem00aFJCUTFrb20yNjFqZ2Rz0gHkAUFVX3lxTFBkQ1VfeFlVNVd0dklfc29ROFRYUUU4eXdUY0lXOV92OHg5LUJGS1h2cjN0U0NfNUZRVkp3SUNXY056WE54ZlhxQTJFUUtsVXFXeUFwZXBlSzhuSG9pNmhYUEd0ZGplVVRxWHN3YW1DcXFweTNuR181cVk5M2x6RnZmZXlJcWpyNGdCbERidjhiLXdvUnIwZ2Vrb1oxWUgtbkZZSnpWMWsxdnUzRGtQN2d4SllDMTFmdm92M0pSUmFTd1JWN3gyeWJXdGRiSTVYUzFOQng0LWExeVY4VWZLNUdFcWphbg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 28 Sep 2026 23:56:47 GMT
- [Intel Shares Ride AI Server Boom to Best Year Since 1981, but History Flashes Caution - finance.biggo.com](https://news.google.com/rss/articles/CBMidkFVX3lxTE8xNmVkckx3SmxHNUh4bTdncU4wMlIwNFJvUGZQaFZSME1wdE14M3k2cUFIRjJ4RWZTaXBnTUZDdzZRQmlFNjVVTWQzWUNhemxlUzZpS1BGMnAwbVF1Q1ZMZGs5MlQ1QVNJMGVZcEtKTzRYR0ZyTlE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 28 Sep 2026 18:06:00 GMT
- [AI 寫錯判例還不夠，這次直接捏造證人：法律專業還能相信生成式 AI 嗎？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiowFBVV95cUxNSXRKTGgzYVRrWEhjbWtmQXBQeDV4N2N4V0Rjd0FJc291N1h6MmR3R0VRcjZrTXAzYTF4R0xheXpPem9MNXRicTBjdUFQOG9iNklDOHpqRnZ2S0dEdXlhVHpVSTRuTjA2cDZnd2lmV1ZVOE1QRFhyUm45WUgzcFp2d2UwTTIyQUlBR29Sd0M5NE9YVW5jbVU2azBnYmtGUnNsNm44?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 29 Sep 2026 00:02:27 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：SKHY or MU: Which Memory Stock Is Worth Betting on at Present? - TradingView；Micron Technology Inc (MU) Stock Analysis & Forecast - TradingKey；4 Memory Semiconductor Stocks to Watch in October 2026 - Yahoo Finance

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | +8.55% | N/A | 1,053.98 | 1,080.53 | -2.46% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | -5.71% | -3.04% | 1,712.89 | 2,335.00 | -26.64% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +14.00% | +8.39% | 228.86 | 228.86 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、memory、Micron」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 2 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [SKHY or MU: Which Memory Stock Is Worth Betting on at Present? - TradingView](https://news.google.com/rss/articles/CBMitwFBVV95cUxPTVhnQ05CdUI0RjFFUzJ1bkxfSWNuckNlY0x0b3pVUzROckU4cVl3TFIwRmRnVHFwaV9PMmNTRl82bUQ4Q1dxZUVyS0o2QThqMjBBYnhnS0dLQmJsRjA4dTZkR2Jtd3VWYmQtbTEwRGZEYlRGdnhQQ25EOEJFWmdZaGQzNHRfX1l1bFh4RnA5M25hN2MyS2I0YkRxMDZIbG52VUJiSjIwbE1IOWZTcmQtY01aQXBzWnc?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 28 Sep 2026 15:44:00 GMT
- [Micron Technology Inc (MU) Stock Analysis & Forecast - TradingKey](https://news.google.com/rss/articles/CBMiY0FVX3lxTFB2cjlJNEFoZnN6al9fVWlOSktTV2tWRzJ1c0c2SklreGhaeHF5VlZlSjNNRE1SaXlnaUVsQ1FaMXFtZUlvM19kUzhHdURNU1VkNmNhLTNPSDNtXzBpSHNZS0xkNA?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 28 Sep 2026 01:49:25 GMT
- [4 Memory Semiconductor Stocks to Watch in October 2026 - Yahoo Finance](https://news.google.com/rss/articles/CBMiogFBVV95cUxOZFM5YmtsblI5Vm5PeHZjZnVmMTRhbEFXaGEzcXR5NE5OaWdjcGZjRXJvdXhsRzlZLTgxcUowMVdnb2F2dGFyR0hEUFF4Q0Y0QnhhbFhub2VfM3laX3FhREZMSHVDNEtMYnBsS2J4dkxWb2plZWFBaDB4Z21PRXAwV1FldGpaajQ0WWpvdTVCSDJxOUtyRUZVeGZrY0l3dGRDa1E?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 28 Sep 2026 13:18:00 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：2000！超級周期「護體」+本益比7倍 超級多頭在美光財報前重申最狂目標價 - news.cnyes.com；科技七雄估值降至10年低點 小摩看好止血回升、但難再主導美股 - news.cnyes.com；美股收盤／四大指數收黑 費半跌1.6% 美伊僵局推升通膨疑慮 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | +8.55% | N/A | 1,053.98 | 1,080.53 | -2.46% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +13.10% | +3.50% | 509.22 | 509.22 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「美光」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [2000！超級周期「護體」+本益比7倍 超級多頭在美光財報前重申最狂目標價 - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTE9ITnpDT3VFdkNtYU1lM2ViSmp2VUwwMGpNYlBybklEaF9ZNWMwcTZIdDllX0hpend5VXZKWXRFckFoZ2RLOVJUQUJqSmp4VkE?oc=5) - Google News source discovery | 鉅亨網 Mon, 28 Sep 2026 23:50:56 GMT
- [科技七雄估值降至10年低點 小摩看好止血回升、但難再主導美股 - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTE9fOWdSWDdkMGpDTmx4T2dVSWtUSGFrcUZVOTY0TG1LRmtHbUlLMUxsTnV1ZV9HMEJQekQ0WnlDXzJ4bHVIeXZEQ3lIZG5PbTA?oc=5) - Google News source discovery | 鉅亨網 Mon, 28 Sep 2026 23:20:25 GMT
- [美股收盤／四大指數收黑 費半跌1.6% 美伊僵局推升通膨疑慮 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTE9vOXBDNks1OE1XVnpDOFlMaW5WUF9CSTJfT29HM3VKSnFselIxLXkzNVFhQVgtTlFyUmd0YXY2S3k2NXNIVHhFOTZZUlphUWVBdzJ6OUNQRG8tU3pv0gFiQVVfeXFMTU5SSTBiV3o0b0Z2NEVDWVBlU1FkZ3NZRkt3enVPUmFRc3RVSWNyUmpCQ3gzMWxRaU5jRkRCUWhaSDYwYzR6Qkd4Z0NHal80bnZlX2lXRGpNLW5xcWN0b2I5Tmc?oc=5) - Google News source discovery | 經濟日報 money Mon, 28 Sep 2026 23:14:18 GMT

## 新興題材：OpenAI

摘要：新興題材：OpenAI 相關新聞集中在：OpenAI shelves new AI model release over safety concerns - Reuters；OpenAI abandons plan to release upcoming model as safety concerns escalate - cnbc.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 新聞直接提及 | 0.00 | +13.10% | +3.50% | 509.22 | 509.22 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：新聞直接提及「OpenAI」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [OpenAI shelves new AI model release over safety concerns - Reuters](https://news.google.com/rss/articles/CBMisgFBVV95cUxNMXc5dDQ0V0FSdEZfMWN3YjNGcG1jZmdHaG1mTDRwMExSZ2pLcjFzRzN1aU0tZFNJa0ZBZXVDdzJJQWxqN01WTmxUbXcyOFEyU1hIUjVpLXlJMW5SVUpiTWRkOHFQd1lyYmVCRHM1UzRtc3lPQXdoRHVvQmQ2ZGp2dGFjLXA1YWNhRjhDc0Z0MmVfejhYdk1IOFEzdUVTYl9Rc0hOWWVKY0RzeENVaks0eFZR?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 28 Sep 2026 22:34:00 GMT
- [OpenAI abandons plan to release upcoming model as safety concerns escalate - cnbc.com](https://news.google.com/rss/articles/CBMisAFBVV95cUxON3J6Rk5EcVdTM1V5QmZWRVhSQW1DaDBmYU5YQ0JnM1hLMUxXbWVSVy1vdmZYWjA1T1N2WnRMNnB2N0NkVUwySjFlU05ISE5uRUFOdnIxYVVxVTkwaTlNcm5LdlduajAwZHFGcUExZ3Z5Rm5zZmNFcldST2pfN2pvWU5JRkY2US1TUVRZZ09jYjFLQUh3cnBsVHNCQmh4SHdKcC1mM0ZLRFNmV0o4R2tfUtIBtgFBVV95cUxQakpZOVlkQTEzOHdkWEI5ZmxXVUc1MFJCWkFLNkVxNld2NjA4WkRwUFV0TlM4ejJhWnZzc1JfcERhMFIwdUEtWU5pLU9tSzN6VnBLbFpKYkd3SEZqMnBJcFVJY3VLdjlqS2NWUDVKTVNXZ0otXy1RZE9XaGg4YVYydjJEM3BjSHlDXzZla2dleU9lOTZjem1oWDBqRWp1LXlyckFZcTNDd3lmazBVcGZJc0dUc0xGUQ?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 28 Sep 2026 22:27:58 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel stock falls as chip-sector sentiment weakens and investors lock in gains - Quiver Quantitative；摩根大通估全球AI題材回檔後有望復甦看多半導體股| 證券 - 中央社 CNA；半導體迎百年一遇擴產潮！法人喊買這家特化廠在手訂單暴增近倍- 證券 - 工商時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.26 | +1.18% | N/A | 116.03 | 127.39 | -8.92% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | 0.00 | -10.20% | -21.76% | 349.57 | 446.77 | -21.76% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2454 聯發科 | 新聞直接提及 | 0.00 | +5.49% | +17.44% | 5,175.00 | 5,285.00 | -2.08% | 不適用 | 60.69 | 87.28 | 64.18B TWD / 44.08% | 2026-09-01 |
| 3711 日月光投控 | 新聞直接提及 | 0.00 | +5.43% | +13.84% | 690.00 | 699.00 | -1.29% | 不適用 | 13.92 | 50.58 | 82.25B TWD / 45.66% | 2026-09-01 |
| 2330 台積電 | 產業/供應鏈推估 | -0.03 | -0.20% | +2.06% | 2,480.00 | 2,480.00 | 0.00% | 未明確 | 86.28 | 28.69 | 514.81B TWD / 53.32% | 2026-09-01 |
| 2303 聯電 | 產業/供應鏈推估 | -0.04 | -1.91% | +4.41% | 154.00 | 164.50 | -6.38% | 同向 | 6.68 | 23.16 | 25.04B TWD / 30.71% | 2026-09-01 |
| NVDA 輝達 | 產業/供應鏈推估 | -0.01 | +14.00% | +8.39% | 228.86 | 228.86 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | -0.01 | +17.78% | N/A | 607.87 | 629.26 | -3.40% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AVGO：新聞直接提及「博通」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：falls, 放量。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2454：新聞直接提及「聯發科」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：falls, 放量。

### 主要來源

- [Intel stock falls as chip-sector sentiment weakens and investors lock in gains - Quiver Quantitative](https://news.google.com/rss/articles/CBMisAFBVV95cUxOSERteld6MGRfUHBZdkhtS1lSZHgxWGRNQ28wUlUzcm5iTHRQYW5WTWIzM29HZ0xSd2ZmOWNOZW01MG9RZVBXQ2hBLVlqOTA1Z2JKcGNyRnNxeE5SUzl4UkpBblNrVmkxamNOX09NZHZxUXRLX1hHZ1pMZFh2UHdsZ25mR1NqTEdCekYyUVpMUWplbzZycHNnbjhMbngzS1U1eGpxdlh4Q1NPamxzMkpEOA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 28 Sep 2026 14:50:00 GMT
- [摩根大通估全球AI題材回檔後有望復甦看多半導體股| 證券 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE4yNllQd2JGY3cweWV4NExGT1F0dlVMU1lackJXMjc2M3NJT0YwblJibUFDYjFGOG5kWlNhbU9wZGI2QjlTb0dPdTZ2a0o4b1VMeXdMN2RaYkhLRmsxOHc?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 28 Sep 2026 15:08:00 GMT
- [半導體迎百年一遇擴產潮！法人喊買這家特化廠在手訂單暴增近倍- 證券 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1QbmhRM3JIakpBTUdxdXdBMHBJRVpEWWs3Y0trTWpkb0FJTkljdjZ0d3V2YjVBSG9vb3JYVFNZVFEyWXZFZ280RXYtZGljYWZ3S0JkQldiV0RZR3hZLVcw?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 28 Sep 2026 06:30:00 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：目標價4340元！「散熱大廠」EPS直衝10股本 Vera Rubin水冷板市占優於預期、液冷散熱占比衝5成 - FTNN；焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報；散熱股又有大消息？花旗喊買奇鋐、雙鴻 目標價齊升逾14% - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | -0.28 | +4.10% | +11.62% | 3,450.00 | 3,555.00 | -2.95% | 背離 | 75.13 | 47.39 | 19.48B TWD / 54.34% | 2026-09-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱、奇鋐」，共 3 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：跌停。

### 主要來源

- [目標價4340元！「散熱大廠」EPS直衝10股本 Vera Rubin水冷板市占優於預期、液冷散熱占比衝5成 - FTNN](https://news.google.com/rss/articles/CBMiS0FVX3lxTE9QNnV5TFFwZWktZlV6QTVFTVhNMW9HVjFvanAwM05OUHh3UXlYbzg5UGFMYVZQclFoWE4yVmlkRF9jdE5qbGU5eWVXOA?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 28 Sep 2026 14:50:00 GMT
- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 27 Sep 2026 06:21:19 GMT
- [散熱股又有大消息？花旗喊買奇鋐、雙鴻 目標價齊升逾14% - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE04UXU3RGRUUnBBVElIbVBGZWozMUxfTzNsbE50ejYzRE1pUTJBQ0FNWS03VjRSYlZrUWkzSXhuNHhFQl9teWs5YTJ4QUU4ck1MZ0NneEk3XzF3UdIBX0FVX3lxTE5tclh3dXNNWDhDMnNiYmMyRW1DRFJwZUt6ZlZXMmdEYlhoQU9VR1pSeTVrVUpVT2FWOE1idEkxdXRhYTYyYVpMcnRwaWQ4NGpmRUNTREJUQ2UwNU01N0pF?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 27 Sep 2026 09:00:00 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股開盤跌150.71點 - 經濟日報；台股10月行情「四多」加持 法人看好大盤挑戰50K | 市場焦點 | 證券 - 經濟日報；台股有望「秋後變盤向上」 法人押寶四大類股 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股開盤跌150.71點 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxNb3ZUUXBvUmFvRmR6VHZWV0xpWDU1WS1ENjRiT2Y1a3ZPODBqd1JDSEVNY09Rd1M3YTlMSjhBY3hoMVIyWnRsWU5SbWs4OFVVT2NrQzRrNmJlVDlDeW9FMUg4RFp5N3hHaHBaSEdYdWdrOGZvQkRMVUIzZzBKMmpHN9IBX0FVX3lxTE9adi1DN1FDYXhYUFF2X0tLUFR0VUlYZkZIRGwtUXB6TGRtMlhQQ09LNXllYWNyZkNhUk9iWXBrRzR4a3lSS3pVOFl0WktlWGdrYS1uMnJtSzRXXzR0N1VN?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 29 Sep 2026 01:14:58 GMT
- [台股10月行情「四多」加持 法人看好大盤挑戰50K | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1vN1JGR0VKaGkwb2s4STdvMkJNclFna0ROTk5ldndCOVZKbHlBRFFQRG1CY0toLXJmdDA4QTVhMk1vNUpWU2NxckNBQzBNeDNKSTNIdG4ySjdBZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 28 Sep 2026 18:39:27 GMT
- [台股有望「秋後變盤向上」 法人押寶四大類股 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE90VzRrcUc5MmloZ2J1WEtmSFp5ZkJpeEZmNlJsVWQ4MXBUSG9TWXN4dkFiWHRqOWJmTHVZY2dMVXMtbng2QXVSUDdGd2h0WElqTlA2OEdZY3BmQdIBX0FVX3lxTFBFT2F2ZjBRc3dzV1U3ZkJ1ZmhOVEgzOTBKS3U0MWZKdTU4LWdTWVJucU45RDN4NHZoUWdMTjdvMGgyUVBjbGl6anhkVEIyd1RENmQwa1NIdVY0SVlXN3g4?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 28 Sep 2026 03:00:00 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：統一證券：台股技術面維持穩健強勢- 新聞 - MoneyDJ；國票證券：台股資金有望重回權益市場- 新聞 - MoneyDJ；美股指數期貨最新報價 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [統一證券：台股技術面維持穩健強勢- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPOVVJXzUzcmFmcUxxczZqdE5UdTY5OUhRcFdTeHVpT3dVYjM5V2tXRTF5aUh4am1hbkJNRzlvX2d5OEhIdExBVlpkTVFTblBBOWlTeVBxZDFvSGJlcW5sV2pNbGZaVFp2NjNCRGE1dTRKVmtsbDJQX3FoMUF0SGF5OTMzczhCU3pySm1ZN1FKalBJdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 29 Sep 2026 00:41:00 GMT
- [國票證券：台股資金有望重回權益市場- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxOSXB2Y3pxZHVQUTBFaUU1dUk0b05TcmlRc1JhMThQel9uazVRQ1VMRkJ6U0YzSjdhaUdNZElDdk1aYTRaeENJdTFWOFh2MlFxSm1XUzI5ZjdRR0Z1RXhwYV91dlZDNDdscTRIcmhOYnVrSGEwSmFqTEV2LWtHNmlkOUdNNkxnWUxnakEteWg5U3NqUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 29 Sep 2026 00:41:00 GMT
- [美股指數期貨最新報價 - MoneyDJ](https://news.google.com/rss/articles/CBMiigFBVV95cUxOSVpqRUJ4UnlkYnoxSlF6TXVJZG5rdWNNNThrREtNeEF0bUVtN0ZVVFI1NERZQW95bmlEOGQ5LVp1X3d0Y3N1RE5BNTZDRzV2dHVXSGdMWldXU2pzVlJIR2VKQ1lRaFdYRjV4ejE5QzZGSE1aLV9ibmR0TDQwVVYtOHd6b3lvYU9BQ1E?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 29 Sep 2026 00:48:19 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
