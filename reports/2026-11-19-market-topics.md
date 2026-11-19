# 每日股市熱門話題分析 - 2026-11-19

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **AI 伺服器與資料中心**｜負向｜熱度 12｜市場確認 73.75｜同向 5/8
2. **散熱與液冷供應鏈**｜負向｜熱度 4｜市場確認 100.00｜同向 2/2
3. **記憶體與 HBM 供應鏈**｜負向｜熱度 3｜市場確認 100.00｜同向 3/3
4. **半導體與晶片供應鏈**｜負向｜熱度 6｜市場確認 82.50｜同向 6/8
5. **綜合市場情緒**｜正向｜熱度 42｜市場確認 0.00｜同向 0/1

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.20（樣本 23）
- 5日相關係數：-0.23（樣本 19）
- 同向比例：16/23

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| AI 伺服器與資料中心 | 73.75 | 5/8 | 2 | +11.25% | +2.48% |
| 散熱與液冷供應鏈 | 100.00 | 2/2 | 0 | +22.30% | +17.75% |
| 記憶體與 HBM 供應鏈 | 100.00 | 3/3 | 0 | +24.52% | +22.70% |
| 半導體與晶片供應鏈 | 82.50 | 6/8 | 1 | +17.27% | +6.57% |
| 綜合市場情緒 | 0.00 | 0/1 | 1 | -7.45% | -9.19% |
| 新興題材：BigGo | N/A | 0/0 | 0 | N/A | N/A |
| 關稅與供應鏈轉移 | 0.00 | 0/1 | 1 | -33.90% | -24.80% |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-11-05 | 0.13 | -0.53 | +66.67% | 12 |
| 2026-11-06 | -0.18 | 0.77 | +100.00% | 5 |
| 2026-11-08 | -0.21 | 0.03 | +23.08% | 13 |
| 2026-11-09 | -0.56 | -0.62 | +60.00% | 10 |
| 2026-11-10 | -0.32 | 0.24 | +3.45% | 29 |
| 2026-11-11 | 0.34 | -0.26 | +46.67% | 15 |
| 2026-11-12 | -0.09 | 0.07 | +50.00% | 14 |
| 2026-11-13 | -0.56 | 0.42 | +54.17% | 24 |
| 2026-11-14 | -0.34 | 0.12 | +42.11% | 19 |
| 2026-11-15 | -0.02 | 0.62 | +50.00% | 20 |
| 2026-11-16 | -0.30 | -0.27 | +38.89% | 18 |
| 2026-11-17 | 0.44 | 0.39 | +80.00% | 15 |
| 2026-11-18 | 0.27 | -0.38 | +86.36% | 22 |
| 2026-11-19 | 0.20 | -0.23 | +69.57% | 23 |

## 歷史回測摘要

- 回測日期：2026-11-19
- 近5日 3日相關：-0.08
- 近5日 5日相關：-0.04
- 同向比例：+51.35%
- 權重狀態：未調整

- 方向準確度：+51.35%
- 信心排序準確度：-0.08
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

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Taiwan Semiconductor Falls 4% as U.S. Tightens AI Chip Curbs on China; Intel Drops 3%, AMD Slides 2% - 24/7 Wall St.；大摩看好台積電先進製程與 AI 結構性領先優勢，力挺目標價 3,088 元 - TechNews 科技新報；銅價暴跌反成 AI 隱憂，資料中心恐面臨缺銅危機 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | -0.59 | -7.45% | -9.19% | 2,130.00 | 2,480.00 | -14.11% | 同向 | 98.27 | 22.14 | 586.89B TWD / 59.71% | 2026-11-01 |
| INTC 英特爾 | 新聞直接提及 | -0.56 | -52.33% | +34.79% | 54.67 | 114.68 | -52.33% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.28 | +2.72% | N/A | 530.14 | 530.14 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | -0.06 | -33.90% | -24.80% | 150.96 | 228.38 | -33.90% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 產業/供應鏈推估 | -0.02 | +12.89% | +3.31% | 508.29 | 508.29 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.03 | +0.81% | -9.05% | 354.05 | 446.77 | -20.75% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.04 | -8.36% | -11.18% | 509.00 | 703.00 | -27.60% | 同向 | 17.55 | 31.46 | 88.62B TWD / 47.13% | 2026-11-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.04 | -4.37% | -1.25% | 3,755.00 | 4,920.00 | -23.68% | 同向 | 62.35 | 63.37 | 55.03B TWD / 5.77% | 2026-11-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「Taiwan Semiconductor、台積電」，共 2 篇新聞命中。 同時符合主題標籤：AI, advanced packaging, CoWoS, AI server。 方向判斷命中詞：falls, 恐, 暴跌。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：falls, 恐, 暴跌。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。 方向判斷命中詞：falls, 恐, 暴跌。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Taiwan Semiconductor Falls 4% as U.S. Tightens AI Chip Curbs on China; Intel Drops 3%, AMD Slides 2% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi1AFBVV95cUxQbTYxU1FmUU5YaC1IY0pVU2FNWHVqZkpud3MybzRhZW9MR3RYNDdwUGFzSkJWTEJELWVWcFNIWU1GcU94QnRJRDl0OUYtTXVyeFlacWxLQnVWRTh0ZmVKaEwyNHd1MUtNdWZ6X1diRW5IZVJOeHVWQS1pRndMQTdUbGw0ODNZTmdYUjRCRUx0VHFtZDdvT3k0clRGdTRDYS1tek1hcEFGLVVjaUZ2bzdRdDJfOXh3RGdVMTg5S0ZFS0txdm8xWmJJaWQ3RFItZ2hNRkw2ZA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 17 Nov 2026 17:02:00 GMT
- [大摩看好台積電先進製程與 AI 結構性領先優勢，力挺目標價 3,088 元 - TechNews 科技新報](https://news.google.com/rss/articles/CBMizwFBVV95cUxNZDRiNmlJR3pWUWR6LXgwbkhla2lpMVhjaU11SnRpWEJmd1Y5LUtRZDVoSDlCSnp2dTRfTUc0cFlScE1OOUZfU1dNdXQ3ZWs2cnBlSDU4VHA1RVo4ZmJvS3pLd3Rqb2xvajFmZkUyYWxYSENBNVRYSndxcFlrUF9lb3U2aEZNWTZXazdUYlZmbm5XSjJiemVrZU5yYUpJRkhXZnZTYUt0VGhSZG0yMzBsMURIUTF6cFhuOFVNSWVQZDBNTzlYUnZUM202LVNVSDQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 19 Nov 2026 01:32:14 GMT
- [銅價暴跌反成 AI 隱憂，資料中心恐面臨缺銅危機 - TechNews 科技新報](https://news.google.com/rss/articles/CBMi0AFBVV95cUxQVXJybXo1ODhWb2pyZ2xKbFJ0N1g2U0VzaGl3YUt5Tk96cWp3OW1CTDdfM3VxTGdyX3FUVUVrblFoeDRRVnhpNDZoMExaS2lZYmh4QkZNQXhqWHRXUWVQWGxVUHlFWmVROGM0dS1KRGhneHVoN0Z6Qkc4OERmMDNvU0ZmYkk5eHlBQnJ5VEhiRVBWQzFyVUZCM3dBZzNlaThaajBzTEhpaThFa0daMnNJUUJMNm9fVjVzNEVjdlRqZDl6MDRJbDFERUpELUF0RXdW?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 19 Nov 2026 01:52:16 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：奇鋐新舊平台並行，明年首季續爬坡 - 新聞 - MoneyDJ；〈焦點股〉輝達財報優於預期 散熱三雄高掛三顆紅燈 - 鉅亨網；NVIDIA管理層無論誰掌舵 AI晶片散熱需求估只增不減 - DIGITIMES

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | -0.59 | -10.69% | -10.69% | 2,450.00 | 3,435.00 | -28.68% | 同向 | 90.78 | 30.01 | 22.10B TWD / 34.35% | 2026-11-01 |
| NVDA 輝達 | 新聞直接提及 | -0.44 | -33.90% | -24.80% | 150.96 | 228.38 | -33.90% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐、散熱」，共 3 篇新聞命中。 同時符合主題標籤：thermal。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [奇鋐新舊平台並行，明年首季續爬坡 - 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNaHJtVVBkbmNHOUhSS0s0MUx5UUwya1UzZk1EUjY1Y2dMVlM5emVpNkdlTmdGR3NlTUpDc1M5dHpnQUJoNTVUNUxWRjA0d1BtdzBMenppeHJMa0JTTWlubHVqTC1QWldkMXpCeVpkVWJLTkRjRkRrY1NTQ3doQUhEc2VMSTB3aUlZWEVJeE5hVFdWUQ?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 18 Nov 2026 04:03:00 GMT
- [〈焦點股〉輝達財報優於預期 散熱三雄高掛三顆紅燈 - 鉅亨網](https://news.google.com/rss/articles/CBMiT0FVX3lxTE9JMEhHVHlFVE5PSjZTTnZ2cDJCYWpBRWN6WGlDM2p0UFFZSnlGcHQxU2Yxc1h4bjVMWnRRUUFVQkdveEpwUzJ3X01wY0ZhVkE?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 18 Nov 2026 04:46:08 GMT
- [NVIDIA管理層無論誰掌舵 AI晶片散熱需求估只增不減 - DIGITIMES](https://news.google.com/rss/articles/CBMia0FVX3lxTE55X2pwMHJIeTJibHA0WGhUSExOUXVYcXF1T2JhOUpfZ05CMWxyTnFhX3lscnNyTEx3TDFLNktaSVZXZnVDY0FrWFJSeEFOVmJTQmJGb1Z2TXZiWjFaQ25oaF9aZmNrLWFyUWQ0?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 18 Nov 2026 16:20:38 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Not Micron, Not Sandisk. This Is My Top Memory Stock for 2027. - Yahoo Finance；SanDisk and Micron Fall 4% as GF Securities Cuts NAND Price Forecast and Warns of a Glut; SK Hynix Dips - 24/7 Wall St.；Micron and Sandisk Gain as Nvidia Results Lift Memory Demand Outlook; Applied Optoelectronics Slides on $550 Million Equity Program - BigGo Finance

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | -0.59 | -27.37% | N/A | 705.27 | 971.00 | -27.37% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.59 | -12.29% | -20.61% | 776.22 | 2,335.00 | -66.76% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | -0.45 | -33.90% | -24.80% | 150.96 | 228.38 | -33.90% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron」，共 3 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Not Micron, Not Sandisk. This Is My Top Memory Stock for 2027. - Yahoo Finance](https://news.google.com/rss/articles/CBMilgFBVV95cUxQNUtEWE45Si14U3NjVmpheXdPT3dpaXNvMDlDU09pTXJRd2NFZGg3T0hRblVyMnFoR2Y2WjVCM3JDSFh2OGVjTG1lYjFkblNJVk91SGZaNVBHdnN3TVhmekJsSnBDbXY0WkRtM1JHUW1YRnVYMVJENEEwcXdwOUFrSHJWbEpHLXk0MmhENGg1NzVmdzJJX0E?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 18 Nov 2026 19:21:02 GMT
- [SanDisk and Micron Fall 4% as GF Securities Cuts NAND Price Forecast and Warns of a Glut; SK Hynix Dips - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi3gFBVV95cUxNTjhxMWdCdlBPVzZFcllkOUFvaWtIeWpQSE4wQjdfOHhpMkN2bW5hUmZYcmc4SzhaNVdpQ2tmcEZ1eGp6SlcxZ29uVzRwaFlJNVZDTlVuMHp3dF9SSC15SldENkZLZmZnZnJkUks5Qk5oaGZLN21TSVlZX1B0WExiVlVEcEdVekljakpWUXBhMVhXVFBCQnRrVHRrYnk0QzVUZ3lNa1kzRUpzbGV3MkgzYktQOXliVWZSM05qQ2JIM2xKQV9oQXA4clJzTVBoRk56OTRvNWg4b2pRbkVudlE?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 17 Nov 2026 16:06:00 GMT
- [Micron and Sandisk Gain as Nvidia Results Lift Memory Demand Outlook; Applied Optoelectronics Slides on $550 Million Equity Program - BigGo Finance](https://news.google.com/rss/articles/CBMidkFVX3lxTE1oMVZLZk5Mb3ZtSi1zZUEwYnR4aXZoR1ZWMUdsWHQ0Qjlwa1liMGpMdEJLSExocUNVQVRKZThxdlFVMDFxTl9TbGpNUVlsRm1OTjlkbmZESlhld3pfRWhfejkwMFdZbzUzWVRrOUY3Sm1VVTZGU3c?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 18 Nov 2026 14:25:00 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：台股4萬點多空交戰後失守 半導體賣壓擴散、櫃買重挫近5% - 經濟日報；Taiwan Semiconductor Falls 4% as U.S. Tightens AI Chip Curbs on China; Intel Drops 3%, AMD Slides 2% - 24/7 Wall St.；科林研發全新台灣技術中心動土 加速AI時代半導體製造技術研發 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.53 | -52.33% | +34.79% | 54.67 | 114.68 | -52.33% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | -0.50 | -7.45% | -9.19% | 2,130.00 | 2,480.00 | -14.11% | 同向 | 98.27 | 22.14 | 586.89B TWD / 59.71% | 2026-11-01 |
| NVDA 輝達 | 新聞直接提及 | -0.48 | -33.90% | -24.80% | 150.96 | 228.38 | -33.90% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.24 | +2.72% | N/A | 530.14 | 530.14 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2303 聯電 | 產業/供應鏈推估 | -0.04 | -8.37% | -10.58% | 89.20 | 164.50 | -45.78% | 同向 | 6.80 | 13.74 | 25.20B TWD / 18.33% | 2026-11-01 |
| MU 美光 | 產業/供應鏈推估 | -0.03 | -27.37% | N/A | 705.27 | 971.00 | -27.37% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | -0.03 | -12.29% | -20.61% | 776.22 | 2,335.00 | -66.76% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.02 | +0.81% | -9.05% | 354.05 | 446.77 | -20.75% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「Taiwan Semiconductor」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip, foundry。 方向判斷命中詞：falls。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [台股4萬點多空交戰後失守 半導體賣壓擴散、櫃買重挫近5% - 經濟日報](https://news.google.com/rss/articles/CBMifkFVX3lxTFAtbnREMEJLMi1tQWg5cFV3YjVadDFadHgwaXl4ZlRGTHBKT0NrNFFGcGRGbHdQRUdTU3JvZDdha2hOWmMxaG10WHdKaGRKeGpRajBndTdoZTZsajROZWoxT2NzZmtCdWtyM1dwOXVwaVdqQkFQWUViQWdiMHg4UdIBX0FVX3lxTE9VM3RUZXVSVDZpTHRkdVlCeTdCd3lZVkdkNkJBUnZsY19PZTJtYmRpb3hnRDVfbjVYeDJkd3FNWEpjM1hFYnh2X0x1ZkdKV0FBSThMNG9VV19FTmdaS2dV?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 18 Nov 2026 09:00:00 GMT
- [Taiwan Semiconductor Falls 4% as U.S. Tightens AI Chip Curbs on China; Intel Drops 3%, AMD Slides 2% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi1AFBVV95cUxQbTYxU1FmUU5YaC1IY0pVU2FNWHVqZkpud3MybzRhZW9MR3RYNDdwUGFzSkJWTEJELWVWcFNIWU1GcU94QnRJRDl0OUYtTXVyeFlacWxLQnVWRTh0ZmVKaEwyNHd1MUtNdWZ6X1diRW5IZVJOeHVWQS1pRndMQTdUbGw0ODNZTmdYUjRCRUx0VHFtZDdvT3k0clRGdTRDYS1tek1hcEFGLVVjaUZ2bzdRdDJfOXh3RGdVMTg5S0ZFS0txdm8xWmJJaWQ3RFItZ2hNRkw2ZA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 17 Nov 2026 17:02:00 GMT
- [科林研發全新台灣技術中心動土 加速AI時代半導體製造技術研發 - 中央社 CNA](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBZSXFOUEVmZHhTMDBCWmZjM3FjSXkyRWV5TjVSclI3VGVyOHhueElfenFQZEdwLXNUU1hZcWtDSnJRQlIxSnhJYmVoa2VDREo0V0NvQ1pQcWJrZw?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 18 Nov 2026 09:45:14 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股4萬點誰在撐？國安基金連三天護盤都在買什麼？個股、張數一次看 | 金融脈動 | 金融 - 經濟日報；台股4萬點保衛戰未歇！開低翻紅漲120點又急殺逾500點 權值股多空激戰 - 經濟日報；台股早盤賣壓重　跌逾800點失守4萬點 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | +0.22 | -7.45% | -9.19% | 2,130.00 | 2,480.00 | -14.11% | 背離 | 98.27 | 22.14 | 586.89B TWD / 59.71% | 2026-11-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。

### 主要來源

- [台股4萬點誰在撐？國安基金連三天護盤都在買什麼？個股、張數一次看 | 金融脈動 | 金融 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE04eXJZUlZzQWxBbGV0MTlOcEpTaG1Lb0NTWkdJRFRlZTVIY1Q1T0JYeHRoS0xSWjlwSktSZ21IV3VNUkxiNVB3emJsRzVlT3FZbThnQUdnLUgydw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 18 Nov 2026 20:46:42 GMT
- [台股4萬點保衛戰未歇！開低翻紅漲120點又急殺逾500點 權值股多空激戰 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5hSDdPM2tGempxYVRfdlRDVlJZaF9qcWZEb21VbjZUYW4wNFVVTDFleEdlT3c2eU9uSXNid1VDbmdHOFZoMmd5b2dweDU4c21rejVlTm8tc1djUdIBX0FVX3lxTE9ZTEl6RFdUWV9vUm5aV3ZVdzZqWXNtQzFDVUZwRTRyMzJLVmd4U1hpbmdpU01rcVNfNXQ5Nkl0cWM5dXhMWFFnN0NOZzdpOGxlamsxR2E1QUlZRmUwTTNN?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 18 Nov 2026 09:00:00 GMT
- [台股早盤賣壓重　跌逾800點失守4萬點 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1JVElNcXFtRjRyMXhEZmQwSzdqdGdmRVdaeklsMHAxSlZQZzlrYkpSdXg0b1A4MjVjX2lvSXMwdmo0MW5TbWgxcFVPY2VQUVpmWkN4Y2dPODZ2d9IBX0FVX3lxTE0zV19OYTFjWC1ibUxzSzZ6RS1FekxSRWxodWsxQXFPSTJUZUhQZGxWdy1vbk5Ma01FdjU3ODltc1o4dE1yTkdMbTlDWXZieUhhRHZLWjVWeko1YXJtRVRj?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 19 Nov 2026 01:36:32 GMT

## 新興題材：BigGo

摘要：新興題材：BigGo 相關新聞集中在：Micron and Sandisk Gain as Nvidia Results Lift Memory Demand Outlook; Applied Optoelectronics Slides on $550 Million Equity Program - BigGo Finance

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | 0.00 | -33.90% | -24.80% | 150.96 | 228.38 | -33.90% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 新聞直接提及 | 0.00 | -27.37% | N/A | 705.27 | 971.00 | -27.37% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | -12.29% | -20.61% | 776.22 | 2,335.00 | -66.76% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MU：新聞直接提及「Micron」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。

### 主要來源

- [Micron and Sandisk Gain as Nvidia Results Lift Memory Demand Outlook; Applied Optoelectronics Slides on $550 Million Equity Program - BigGo Finance](https://news.google.com/rss/articles/CBMidkFVX3lxTE1oMVZLZk5Mb3ZtSi1zZUEwYnR4aXZoR1ZWMUdsWHQ0Qjlwa1liMGpMdEJLSExocUNVQVRKZThxdlFVMDFxTl9TbGpNUVlsRm1OTjlkbmZESlhld3pfRWhfejkwMFdZbzUzWVRrOUY3Sm1VVTZGU3c?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 18 Nov 2026 14:25:00 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：整理包／黃仁勳概念股笑了！輝達季度財報超預期 完整台廠供應鏈名單、潛在受惠股一次看 - 經濟日報；經長會晤歐盟成長總署及出席波蘭TEEMA產業日深化民主供應鏈夥伴關係- 新聞 - MoneyDJ

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.22 | -33.90% | -24.80% | 150.96 | 228.38 | -33.90% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +12.94% | +26.39% | 352.45 | 352.45 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | -8.30% | -8.68% | 218.00 | 289.00 | -24.57% | 不適用 | 16.57 | 13.37 | 1305.32B TWD / 45.73% | 2026-11-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [整理包／黃仁勳概念股笑了！輝達季度財報超預期 完整台廠供應鏈名單、潛在受惠股一次看 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBQUlViSHpPeDVlY29yaHFNNE5NcVlUQnE3ZThTcXRGNHgxYTVPOVVTRDlaTDV6Zml5WEwxVHNSeGFDcnVHUHhRSW15SzNpU0dYVDU3dThWNEVCbkZI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 17 Nov 2026 08:00:00 GMT
- [經長會晤歐盟成長總署及出席波蘭TEEMA產業日深化民主供應鏈夥伴關係- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNajlLcnVkTUZ1Y1JaUHhjZUpiM0t6QXZobFpNNVJJaTI1RHlzMmhMZ3VFb185Qmp4YlF6V2lUZklDTVA5cDFhVDVNeXFIQlUtN3VlLUs5amJ2cHRUVEJLWDZLSVhpbEhpTFZqRWJOWGh2aWRHZkdOTWphV2JQUVNZYWREUWsyXzJSaGZpVWFIMEg0Zw?oc=5) - Google News source discovery | MoneyDJ Thu, 19 Nov 2026 01:10:00 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：國票證券：台股短線籌碼壓力仍在- 新聞 - MoneyDJ；統一證券：台股短期盤勢仍偏向大區間震盪- 新聞 - MoneyDJ；美股指數期貨最新報價 9:37-台股 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [國票證券：台股短線籌碼壓力仍在- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPTjRYWkptb0NFWWdLU05jcHdhSTJwQXZJV0VvajQ5bUcwamtQdUtrRDNkbk13TWl4UVVwcndxUkZfODAzQzNrcDVGbVpfMktZbGJBc0tLMHFZS2NGN2ZCUmtWTFRTZGY5Nk1CT1ExLV96VW9KUzZNSnZQTW5xYXJuZmp5NlRmN045eE9JR2Q1TGp2QQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 19 Nov 2026 00:42:00 GMT
- [統一證券：台股短期盤勢仍偏向大區間震盪- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPMHpHVlJvY0xhbk1kYXItY3VjTjl1TGxhMzJWcllYNnYtVHE5VzJMaHBfSVl1TlAzWXdlZzg4YmptVzRTSEdJUkVkaEF6QVVmM2xUcWlBYXF5MXQzQ1BDOHlQOHk3ZjdKM3NESGhRZ3N1bXNrWDhSUTlSS1hsNUpVOFJHN3ZDZDFHUWNCR0dMd2RsQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 19 Nov 2026 00:42:00 GMT
- [美股指數期貨最新報價 9:37-台股 - MoneyDJ](https://news.google.com/rss/articles/CBMiigFBVV95cUxOVUhfZXNHR2hUTGdmSnFxajdLeGdjM25Fc0VvSFNkVXZNdnk4d3BfZlNWOGhYUGxCQmJEVnBWVXAtQjUyS2lVNFJja01LdjIteFpkckNwcHpKbHN0cUdZYUd6T1RZZ3VKUWtudzF6eUdDN2xvR20yRm1PS1JMbVU0T2prV0I3Ni1DN3c?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 19 Nov 2026 01:49:43 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
