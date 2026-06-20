# 每日股市熱門話題分析 - 2026-06-21

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜正向｜熱度 12｜市場確認 80.95｜同向 1/1
2. **利率與成長股估值**｜中性｜熱度 3｜市場確認 86.71｜同向 1/1
3. **新興題材：TradingKey**｜正向｜熱度 2｜市場確認 80.95｜同向 1/1
4. **半導體與晶片供應鏈**｜正向｜熱度 6｜市場確認 63.39｜同向 4/5
5. **AI 伺服器與資料中心**｜正向｜熱度 9｜市場確認 37.15｜同向 3/6

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.01（樣本 18）
- 5日相關係數：0.32（樣本 18）
- 同向比例：10/18

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 80.95 | 1/1 | 0 | +3.65% | +16.12% |
| 利率與成長股估值 | 86.71 | 1/1 | 0 | +5.57% | +18.91% |
| 新興題材：TradingKey | 80.95 | 1/1 | 0 | +3.65% | +16.12% |
| 半導體與晶片供應鏈 | 63.39 | 4/5 | 1 | +2.46% | +16.77% |
| AI 伺服器與資料中心 | 37.15 | 3/6 | 3 | +0.71% | +8.30% |
| 散熱與液冷供應鏈 | 1.23 | 0/1 | 0 | +0.41% | -2.78% |
| 消費電子與手機 | 0.00 | 0/3 | 2 | -5.35% | -15.76% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 相關性偏弱；應提高同向價格確認權重，降低泛 AI、泛半導體等寬標籤推估權重。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-06-07 | -0.32 | -0.20 | +45.45% | 11 |
| 2026-06-08 | 0.36 | -0.68 | +60.00% | 5 |
| 2026-06-09 | 0.07 | 0.19 | +25.00% | 8 |
| 2026-06-10 | 0.17 | 0.15 | +53.85% | 13 |
| 2026-06-11 | -0.05 | -0.08 | +14.29% | 7 |
| 2026-06-13 | 0.87 | 0.98 | +100.00% | 4 |
| 2026-06-14 | 0.82 | 0.98 | +100.00% | 3 |
| 2026-06-15 | 0.87 | 0.56 | +42.86% | 7 |
| 2026-06-16 | 0.39 | 0.50 | +76.92% | 13 |
| 2026-06-17 | 0.17 | 0.47 | +62.50% | 8 |
| 2026-06-18 | -0.41 | -0.41 | +42.86% | 7 |
| 2026-06-19 | 0.06 | -0.04 | +57.14% | 7 |
| 2026-06-20 | 0.29 | 0.21 | +63.16% | 19 |
| 2026-06-21 | -0.01 | 0.32 | +55.56% | 18 |

## 歷史回測摘要

- 回測日期：2026-06-21
- 近5日 3日相關：N/A
- 近5日 5日相關：N/A
- 同向比例：N/A
- 權重狀態：未調整

- 方向準確度：N/A
- 信心排序準確度：N/A
- 診斷：樣本不足

調整原因：近 5 日有效樣本 0 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits；SanDisk (SNDK) Is Doing Something Unprecedented In The Al Sector! SNDK STOCK PODCAST ANALYSIS BUY Jobe Bellingham (gRMiCAoJ7a) - Mshale；AI Memory Bottleneck? These ETFs Let You Buy All the Winners - TradingView

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.65 | N/A | N/A | 1,133.99 | 1,133.99 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.65 | +3.65% | +16.12% | 2,184.75 | 2,184.75 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.48 | N/A | N/A | 537.37 | 537.37 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.48 | N/A | N/A | 133.99 | 133.99 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +5.57% | +18.91% | 210.69 | 211.14 | -0.21% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、memory、Micron」，共 4 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：growth, rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK、SanDisk」，共 4 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits](https://news.google.com/rss/articles/CBMi0AFBVV95cUxOWm5KdEIwSXpyY191UEhDa1V6NVpWa01UbmpJeWRIV0ttT080TmpDNEhISW5TWkQwUzBVYzBqSHJPWXRVNVJCampoWWRlYmhKVkhIeHBJLS0wLW5Ua09GQnRORXpFcW5qTEJkcnJGcW55aU5rOFVOLUFMbjRPZEpWT3A2ZllucnM0SU9JNEdrNUwyc3V2WHAtNFk3VHl4R1F6SkZRMFpleEE2Zl9MdW4tSEpMMnFGZ2hQZURWQ3B1WDlPR1BhRjJELVN5ODJWYVR3?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 19 Jun 2026 15:56:28 GMT
- [SanDisk (SNDK) Is Doing Something Unprecedented In The Al Sector! SNDK STOCK PODCAST ANALYSIS BUY Jobe Bellingham (gRMiCAoJ7a) - Mshale](https://news.google.com/rss/articles/CBMiW0FVX3lxTE82c25ZNkhMbnBFcHlYZktjT2gzRlFzREd4ZFlubTJYeG4zZFJ6NU1OdGxaX3BRYWM0bFdDWk5tMlNVS3BvWXRLZW1jUVp3SUdNYXlKam5zNEhNVm8?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 19 Jun 2026 20:28:11 GMT
- [AI Memory Bottleneck? These ETFs Let You Buy All the Winners - TradingView](https://news.google.com/rss/articles/CBMitgFBVV95cUxQTWh0N01GRE5vRWR3eWQzVGhDYmU3MHgwWUVvUXRtZnFRZDBpazI0N0JueUlyTnNxWEtmQ0tsZHpSTE1nU0VIOWJSNzZ1Wk1EMDNsZ0dDZGxVRUx4ZGUtMTQ0YUQzUWQ1OUs3cFNleTFXSzVCcmp3MktwR3VONHdvN0wzREU3WVo2VjRLNEVMajdqeTBGM3BJcWk2SW9hRmVQTnJ3X0V1QzZjSXRWWkxRLXdVdjhRdw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 19 Jun 2026 12:39:00 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：Intel Stock Rockets Overnight On Blowout Q1: Analyst Says ‘We’re Overthinking’ As Valuation Gap With NVDA, AMD Widens - Stocktwits；美股泡沫要破了？估值超越「1929經濟大恐慌」 - Yahoo股市；一檔賺40個股本的記憶體股，2027年缺貨較今年嚴重，本益比24倍逢低能布局嗎？ - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.48 | +5.57% | +18.91% | 210.69 | 211.14 | -0.21% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.48 | N/A | N/A | 537.37 | 537.37 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.48 | N/A | N/A | 133.99 | 133.99 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | -3.40% | -25.12% | 379.40 | 506.69 | -25.12% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVDA」，共 1 篇新聞命中。 方向判斷命中詞：rockets。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 方向判斷命中詞：rockets。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 方向判斷命中詞：rockets。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Stock Rockets Overnight On Blowout Q1: Analyst Says ‘We’re Overthinking’ As Valuation Gap With NVDA, AMD Widens - Stocktwits](https://news.google.com/rss/articles/CBMiiAJBVV95cUxOeXkzdzdWTjJEdE9PWlRvTGdqTnA2MklEYk5ZcE5ZYWVvT29nRVk2Z1p5czRsZGJzY0U3ZWNhTjFmbTdWaXpDa0R2OTh6RzNxZUxUWk9xOS1GbmNuRVdrdmpQdHBjUzFEejVOcFU2di16ak10T1FFVnFNNnZpVnVwU3RkejRveng1ZVF5T1pYdWkxdlB0VkZsQ21pZEJiZU9fVFM5SndpdUpnZVQ1UV9CUnV0RUlwcU9MNGtkbVR6Tng2OVlpY01HU0hXc2lEbzBxZFRER25yajZQcHhrVmdWRmNYUWxEVWVRUDFjcHZhZzVqbm9MVmZGX0ducGZzTmt0SjltejVNSlc?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 19 Jun 2026 16:47:45 GMT
- [美股泡沫要破了？估值超越「1929經濟大恐慌」 - Yahoo股市](https://news.google.com/rss/articles/CBMiowJBVV95cUxPVER3ckZxQjFDbmFFMXJnWEhXaG1SNVJjZHJVRDlqS0JNbVY0RmFrMUpOZTAzcm1wbW9ScW1qVk54NFhyMGJ3Ul9uYjJGajlDaGFlc1FTZ3RqbFFfR0VPdFUwNEpDN051bUJlNmVUaEFtNzAxYnBBLTh3M25ucjl4ZGtYNGEtZ2VIeUNTWG4zbUlQeEUyMmdrOEI1Z2Z6Z0xYSlgxUFdueTVxMGhvMVpwQW50QVJ1T2RvejhIUjkyUkNaRVUyREI4aF84SnEwQkVpbmctQXlfNDZIT0J3VXUzN0d1dG5GbElUTFFuQW5sOGV4VnNvWjlTZ0RocXF3bDFQc3A1SnZHdi1xWTI2T1lRdWpicW43enVSZ2VHWF9tXzctQUk?oc=5) - Google News source discovery | Yahoo 奇摩股市 Sat, 20 Jun 2026 01:51:11 GMT
- [一檔賺40個股本的記憶體股，2027年缺貨較今年嚴重，本益比24倍逢低能布局嗎？ - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9ZbWRhQ2dTYUFBNHdFX1ZkMTFxaVpoQXY3enBTRm9vQzV1b2c2TjZiTU5iLUoxOXZCeVF2bTk3dW13NGFZYVhBeno2Wk4wVnlFRE1jQTBIT3BUd9IBX0FVX3lxTE42Z2owcndGbzJXQ2tmQU1SUHZ1SEdkTGxGb0cwTmVaMGo2YmU3dGRzc2IzWkpuYnBubWN2SllSMGVSOEQ1OUJ4NTJZZmJJN3JCT2lzYlVDaHE5M0lhRm1j?oc=5) - Google News source discovery | 經濟日報 money Sat, 20 Jun 2026 02:00:00 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：SanDisk Corporation Stock (SNDK) Moved Up by 11.54% on Jun 19: Drivers Behind the Movement - TradingKey；2026 Global Top Seven Memory Giants Ranking: Kioxia, SanDisk Lead Growth, Who Is Strongest in the AI Memory Supercycle? - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| SNDK SanDisk | 新聞直接提及 | +0.56 | +3.65% | +16.12% | 2,184.75 | 2,184.75 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 新聞直接提及 | +0.48 | N/A | N/A | 1,133.99 | 1,133.99 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- SNDK：新聞直接提及「SNDK、SanDisk」，共 2 篇新聞命中。 方向判斷命中詞：growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- MU：新聞直接提及「memory」，共 1 篇新聞命中。 方向判斷命中詞：growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [SanDisk Corporation Stock (SNDK) Moved Up by 11.54% on Jun 19: Drivers Behind the Movement - TradingKey](https://news.google.com/rss/articles/CBMiiwFBVV95cUxNYUI4SlQ0VWlTUFpfV1hMalJyanVMVlgtbFQtUld3endXY2sxWDZIUEJTbkhwdGVKZ2tKb1lBSzhubXh5WVg5VUs5QWFldmlsLXllYndnZ1V4R2pNZWl3SjUyd1lOZ08xbEtqYUUzaERrbnFIWmJTVDhGdzJfSml1WXpXbHBlbmR3M29n?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 19 Jun 2026 16:15:23 GMT
- [2026 Global Top Seven Memory Giants Ranking: Kioxia, SanDisk Lead Growth, Who Is Strongest in the AI Memory Supercycle? - TradingKey](https://news.google.com/rss/articles/CBMirwFBVV95cUxPbElxTEtyRVJKeGtuQjFmb2p2V0c5TEo5XzVXbEcySExfb2dmeG4zRkpEUVpuMkhjcHh4azAxTlVSQUxYc1pMemlvcjhWMHhDeGRqajFUSUNLc3U5QlNYVVFCdnZPMWZzSV9XcHp5WnIwbDZDN3lpWkFMT1p6bGtvUGs2aTFEMHFyb3lPU1ZYQkZ1WjNJdGt6aTNxcFRrMzZHNGxydEdFY2VNQ2lHM1dr?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 20 Jun 2026 09:06:54 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Nasdaq gets boost from AI chip stocks; Fed rate question stays in focus - TechStock²；Nvidia and Intel Rallied Too Much, Broadcom Is the AI Chip Bargain Investors Need - NAI500；日月光投控24日股東會半導體封測景氣風向球- 日報 - 工商時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.59 | N/A | N/A | 133.99 | 133.99 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.54 | +5.57% | +18.91% | 210.69 | 211.14 | -0.21% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | +0.27 | -1.46% | +28.73% | 411.35 | 446.77 | -7.93% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 新聞直接提及 | +0.54 | +3.90% | +12.68% | 613.00 | 613.00 | 0.00% | 同向 | 10.86 | 56.92 | 63.03B TWD / 28.57% | 2026-06-01 |
| 2330 台積電 | 產業/供應鏈推估 | +0.05 | +1.47% | +7.11% | 2,410.00 | 2,410.00 | 0.00% | 同向 | 74.39 | 32.40 | 416.98B TWD / 30.09% | 2026-06-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.05 | +2.83% | +16.40% | 145.50 | 145.50 | 0.00% | 同向 | 4.00 | 36.56 | 22.94B TWD / 17.78% | 2026-06-01 |
| AMD 超微 | 產業/供應鏈推估 | +0.04 | N/A | N/A | 537.37 | 537.37 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | +0.04 | N/A | N/A | 1,133.99 | 1,133.99 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：boost。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：boost。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AVGO：新聞直接提及「Broadcom」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：boost。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Nasdaq gets boost from AI chip stocks; Fed rate question stays in focus - TechStock²](https://news.google.com/rss/articles/CBMilgFBVV95cUxPNkhxX19ZSGhGQUd5WlVEdGVjMnVkLTVMcTdiSk1WOHBNQWI5aDJmRTN1ZkNjQjRFY25Dd2phR21lTDJQSVdkNHlNeEdRUFduZ1VWd1QwMkE5R1V3VWU4Y0lGaTJydWo2dURvNlBDS0dIV0plbExkUElwOUNha3JFVFZpWGRhbjdia1Q3c2VtdGJaNUE2Z3c?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 20 Jun 2026 17:33:10 GMT
- [Nvidia and Intel Rallied Too Much, Broadcom Is the AI Chip Bargain Investors Need - NAI500](https://news.google.com/rss/articles/CBMiswFBVV95cUxQMGpvWWFXaEpyNHMwV3BGT2lKMDUyVmVSLWR6Q0NTN2dBNi01ZURlOGVNWVo4d0dTTFZ5eUZ4c0RmelM4eXRXVFNOcmc4elJwcDJ6b2pSZElpWVFXeWZmRVd4OWdiWUktRndLckNvUHVaLXphM24xOGdOSWVkbDFUb1hvOFJoV2c2WXVpVDJEZVdwTkxtc0tXU3ZfaTJZMGpOemJEOHpYTS11QTJNdDQyOTlBaw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 20 Jun 2026 01:27:47 GMT
- [日月光投控24日股東會半導體封測景氣風向球- 日報 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTFAzVkJaOFd2eGQ0RnlJWDBzbVF6YzQ3bzctSXJOWkNvSXByRXhFLUJDdjZKM1FFSVFpeHNsbmk2QU03ZVg4NmM0Wk03ZkFwZVBGazBBd3dJYy11SUJGS3hj?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 20 Jun 2026 19:00:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Nasdaq gets boost from AI chip stocks; Fed rate question stays in focus - TechStock²；Nvidia and Intel Rallied Too Much, Broadcom Is the AI Chip Bargain Investors Need - NAI500；千萬秒 AI 數據反映哪些用戶趨勢？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.62 | +5.57% | +18.91% | 210.69 | 211.14 | -0.21% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.62 | N/A | N/A | 133.99 | 133.99 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | +0.28 | -1.46% | +28.73% | 411.35 | 446.77 | -7.93% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.06 | N/A | N/A | 537.37 | 537.37 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.06 | +1.47% | +7.11% | 2,410.00 | 2,410.00 | 0.00% | 同向 | 74.39 | 32.40 | 416.98B TWD / 30.09% | 2026-06-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.02 | -3.40% | -25.12% | 379.40 | 506.69 | -25.12% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.04 | +3.90% | +12.68% | 613.00 | 613.00 | 0.00% | 同向 | 10.86 | 56.92 | 63.03B TWD / 28.57% | 2026-06-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.02 | -1.79% | +7.47% | 4,390.00 | 4,390.00 | 0.00% | 背離 | 62.91 | 69.96 | 47.43B TWD / 4.99% | 2026-06-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。 方向判斷命中詞：boost。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：boost。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AVGO：新聞直接提及「Broadcom」，共 1 篇新聞命中。 同時符合主題標籤：AI, datacenter。 方向判斷命中詞：boost。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Nasdaq gets boost from AI chip stocks; Fed rate question stays in focus - TechStock²](https://news.google.com/rss/articles/CBMilgFBVV95cUxPNkhxX19ZSGhGQUd5WlVEdGVjMnVkLTVMcTdiSk1WOHBNQWI5aDJmRTN1ZkNjQjRFY25Dd2phR21lTDJQSVdkNHlNeEdRUFduZ1VWd1QwMkE5R1V3VWU4Y0lGaTJydWo2dURvNlBDS0dIV0plbExkUElwOUNha3JFVFZpWGRhbjdia1Q3c2VtdGJaNUE2Z3c?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 20 Jun 2026 17:33:10 GMT
- [Nvidia and Intel Rallied Too Much, Broadcom Is the AI Chip Bargain Investors Need - NAI500](https://news.google.com/rss/articles/CBMiswFBVV95cUxQMGpvWWFXaEpyNHMwV3BGT2lKMDUyVmVSLWR6Q0NTN2dBNi01ZURlOGVNWVo4d0dTTFZ5eUZ4c0RmelM4eXRXVFNOcmc4elJwcDJ6b2pSZElpWVFXeWZmRVd4OWdiWUktRndLckNvUHVaLXphM24xOGdOSWVkbDFUb1hvOFJoV2c2WXVpVDJEZVdwTkxtc0tXU3ZfaTJZMGpOemJEOHpYTS11QTJNdDQyOTlBaw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 20 Jun 2026 01:27:47 GMT
- [千萬秒 AI 數據反映哪些用戶趨勢？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiYkFVX3lxTE1UT1pxdS10T09rWm83ZktzZkhjaThiUUEyMkw4RVg2ZFNGaFFBVXYzV2pFQnVhcDVFTExPSEZSRnpSa3RsR0JRcjRqZEFwa1VWS2NRZVp1MmdpdkJwb2lWTVlR?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 20 Jun 2026 18:50:27 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：GB300出貨爆量、Rubin正式量產！「這檔」5月營收暴增172％！奇鋐、台光電、廣達…法人點名AI供應鏈13強1次看- 上市櫃 - 旺得富理財網；焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報；1.4 奈米功耗優勢，能否解決 AI 手機的散熱與續航瓶頸？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | -0.49 | -0.41% | +2.78% | 2,400.00 | 2,835.00 | -15.34% | 未明確 | 61.06 | 39.43 | 15.87B TWD / 60.64% | 2026-06-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐、散熱」，共 3 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：跌停。

### 主要來源

- [GB300出貨爆量、Rubin正式量產！「這檔」5月營收暴增172％！奇鋐、台光電、廣達…法人點名AI供應鏈13強1次看- 上市櫃 - 旺得富理財網](https://news.google.com/rss/articles/CBMiakFVX3lxTE9pOUxhbU4ybWl5TWR3TjhGTVJkU1Qta2RLV202amhVMnVSVkVfTFk4TlQ2QklzZVE4Nm9oLUp3ckRtdkRMQnBBQkF0MU9VR3g3VXZaNXc1SXJnc3RGQnB3aV9ZUU5QZjQzMHc?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 19 Jun 2026 02:06:10 GMT
- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 19 Jun 2026 03:05:42 GMT
- [1.4 奈米功耗優勢，能否解決 AI 手機的散熱與續航瓶頸？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiakFVX3lxTE53MFVVRmR3YnJhRTlUV0VSNlFtNGw5dkJhMkdrMW1qU3d2VU9VYThreTBEOWxYV2NLbnNibFIwdEU4UUZITWVjeE45eWstdHpkOG9RYThheHZ3eXlDRXRzN3JwNzJtOTRDUkE?oc=5) - Google News source discovery | TechNews 科技新報 Sat, 20 Jun 2026 12:58:19 GMT

## 消費電子與手機

摘要：消費電子與手機 相關新聞集中在：The AI Memory Crunch Reached Your iPhone. Sandisk and Micron Cashed In. - techi.com；Gemini Intelligence 如何重塑 AI 手機競爭格局？ - TechNews 科技新報；榮耀新機如何衝擊台灣 AI 手機市場？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AAPL 蘋果 | 新聞直接提及 | -0.27 | +12.81% | +28.38% | 298.01 | 312.06 | -4.50% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 新聞直接提及 | -0.48 | N/A | N/A | 1,133.99 | 1,133.99 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.24 | +3.65% | +16.12% | 2,184.75 | 2,184.75 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3017 奇鋐 | 新聞直接提及 | -0.36 | -0.41% | +2.78% | 2,400.00 | 2,835.00 | -15.34% | 未明確 | 61.06 | 39.43 | 15.87B TWD / 60.64% | 2026-06-01 |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | +0.37% | +3.87% | 268.50 | 289.00 | -7.09% | 不適用 | 14.13 | 19.07 | 859.41B TWD / 39.57% | 2026-06-01 |
| 2454 聯發科 | 產業/供應鏈推估 | 0.00 | -1.79% | +7.47% | 4,390.00 | 4,390.00 | 0.00% | 不適用 | 62.91 | 69.96 | 47.43B TWD / 4.99% | 2026-06-01 |

關聯理由（前 3）：
- AAPL：新聞直接提及「iPhone」，共 1 篇新聞命中。 同時符合主題標籤：hardware, consumer electronics, smartphone。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MU：新聞直接提及「Micron」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。

### 主要來源

- [The AI Memory Crunch Reached Your iPhone. Sandisk and Micron Cashed In. - techi.com](https://news.google.com/rss/articles/CBMid0FVX3lxTFB3VE4yMGJYTmx0bXpCLUNVTmdJNVF4YkRpb2MyclJKOTd0WmhfeU9lb3o2VjloMFVpdDBlQXYxSG5vcVpNdzRzcmNrLWV6VTY4TFBiVmd4bnJVUWxNYldtVDRubDAzV3F3Q2prSVBkM1NWNmFneURV?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 19 Jun 2026 12:18:48 GMT
- [Gemini Intelligence 如何重塑 AI 手機競爭格局？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMibkFVX3lxTE1SVURja2RHNWNaTmZQR0FaR1B5RFBvYjVzVkZWSk9CN1EtWVJYbjJ5QVZLclhEc0JxNHZiMUZyekFSbEpFWjhSaHVydERGRUl6UEZnZml1cUE3dkIyNS1ha1hsWW85TkZkVEQ1UVZ3?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 20 Jun 2026 20:22:44 GMT
- [榮耀新機如何衝擊台灣 AI 手機市場？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiYkFVX3lxTE5zc0d0TlFOSHZ6TVNpcFNOaE54X1lteUd5TFFKTG1UNVBacDlEaUNIRFpMZnBScEhSRG01SHJLdUdRaEhPZ2RXNDU0QlBSWTIwOFEwNW9ZSml5dndHT2hfSEdn?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 20 Jun 2026 18:50:56 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：元大-鳳中 對 同亨(5490)個股 單一券商歷史明細 - justdata.moneydj.com；台股「四貸同堂」 金管會盯兩指標 - 經濟日報；台股「四貸同堂」 金管會盯兩指標 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [元大-鳳中 對 同亨(5490)個股 單一券商歷史明細 - justdata.moneydj.com](https://news.google.com/rss/articles/CBMilgFBVV95cUxQQTBMdVZJRHp2S1NfTmhaSUQtZmNVVFlhdXgwbTBVRFpaeEk4ZlM3eWVvaWRaVGVqbUJDRWQxV0d6NGdTejNlUU1yVHRiZFFKbmRMMjlicC1JZGRRME84T2NpSng5RjJveUpJc2Y5OFdzTV91dGZEcnZpbzhTXzRoM3lLSnBlY2Z4cGFHcjFDQnZMbXBQSVE?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 19 Jun 2026 18:25:25 GMT
- [台股「四貸同堂」 金管會盯兩指標 - 經濟日報](https://news.google.com/rss/articles/CBMihAFBVV95cUxNYjg3OXRYU2hBWjlOTFhTd0RBR2E0SHJ0VWdfYU5Nc01MZkNFZ1VaTHFUamN6WFlaQWxvR0RLQUFBU0dJUUUzX0ZFVGZiV09PN19YcEsyWkpIaWYxa3pYbTlTOTY1cmFMOTVMbWRWQVYtUVF5Ni1US2RBWmUyYlRiOExfV0rSAV9BVV95cUxNdlBEZUEwTlFERUpoMHBqeGt0TDN1VWdDUVhiTHlTOUxtdjVtS2dkbE9MRDVwMGJmcHRJYVFOVGtWSjVvcVVPbXdrc1RtaW5udnNmbEk2M2ZuV3h4d1FWSQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 20 Jun 2026 18:18:41 GMT
- [台股「四貸同堂」 金管會盯兩指標 - 經濟日報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE12UERlQTBOUURFSmgwcGp4a3RMM3VVZ0NRWGJMeVM5TG12NW1LZ2RsT0xENXAwYmZwdElhUU5Ua1ZKNW9xVU9td2tzVG1pbm52c2ZsSTYzZm5XeHh3UVZJ0gFfQVVfeXFMTXZQRGVBME5RREVKaDBwanhrdEwzdVVnQ1FYYkx5UzlMbXY1bUtnZGxPTEQ1cDBiZnB0SWFRTlRrVko1b3FVT213a3NUbWlubnZzZmxJNjNmbld4eHdRVkk?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 20 Jun 2026 18:18:41 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
