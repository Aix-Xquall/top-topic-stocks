# 每日股市熱門話題分析 - 2026-11-03

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **綜合市場情緒**｜負向｜熱度 41｜市場確認 81.76｜同向 1/1
2. **AI 伺服器與資料中心**｜中性｜熱度 14｜市場確認 90.98｜同向 7/8
3. **記憶體與 HBM 供應鏈**｜中性｜熱度 7｜市場確認 100.00｜同向 1/1
4. **新興題材：TradingKey**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
5. **半導體與晶片供應鏈**｜正向｜熱度 5｜市場確認 0.00｜同向 0/8

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.03（樣本 22）
- 5日相關係數：0.08（樣本 18）
- 同向比例：9/22

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 綜合市場情緒 | 81.76 | 1/1 | 0 | +3.92% | +2.31% |
| AI 伺服器與資料中心 | 90.98 | 7/8 | 1 | +9.91% | -5.28% |
| 記憶體與 HBM 供應鏈 | 100.00 | 1/1 | 0 | +14.15% | N/A |
| 新興題材：TradingKey | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | 0.00 | 0/8 | 8 | -15.54% | +3.81% |
| 散熱與液冷供應鏈 | 0.00 | 0/2 | 2 | -6.65% | -0.86% |
| 關稅與供應鏈轉移 | 0.00 | 0/2 | 2 | -28.09% | +24.42% |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 相關性偏弱；應提高同向價格確認權重，降低泛 AI、泛半導體等寬標籤推估權重。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
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
| 2026-11-01 | 0.47 | -0.40 | +85.71% | 14 |
| 2026-11-02 | -0.15 | -0.06 | +27.78% | 18 |
| 2026-11-03 | -0.03 | 0.08 | +40.91% | 22 |

## 歷史回測摘要

- 回測日期：2026-11-03
- 近5日 3日相關：0.06
- 近5日 5日相關：-0.03
- 同向比例：+61.54%
- 權重狀態：未調整

- 方向準確度：+61.54%
- 信心排序準確度：0.06
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

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：外資再砍735億元、投信大買361億元！台股失守 45K 三大法人賣超526億元 - 經濟日報；費半續挫拖累台股跌逾700點 力守44,000點大關 - 經濟日報；越跌越買 台股 ETF 受益人創高挑戰兩千萬人 00415A 等24檔受益人創高 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | -0.50 | -3.92% | -2.31% | 2,320.00 | 2,480.00 | -6.45% | 同向 | 86.28 | 27.01 | 511.86B TWD / 54.65% | 2026-10-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 2 篇新聞命中。

### 主要來源

- [外資再砍735億元、投信大買361億元！台股失守 45K 三大法人賣超526億元 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBtOW9ITEYwTzVaRXo3aC16QnFReHRVTnN1aC1wSmNlRi1Ea0lqZFlWN01jem1IVlBvUC1ucHJuZms5OXpOR2ZvdWw0dDFOQ0lwb0RJRkdnODhnZ9IBX0FVX3lxTFBVSFNpMmpJYlRmajRUVWFSR1ptWVFPU3RPT0lNLWQxdGEybG5KdkpUUXNjRlpJaVlkcnc4X19MV05QS3IwTzd6Vkh3S3lEWE9PTFRBb2l6dUVNdXVKYmow?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 02 Nov 2026 08:00:00 GMT
- [費半續挫拖累台股跌逾700點 力守44,000點大關 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE4wdzl1TUNmQTVWRkFxTW5Wd1hLLVJaemFNV2V3SHRMcjJJdTlGdFdodUJIQkZLU1N1MWRMRXpmMTE5eHFTM1c2d0xPNWxUSURTUzkzUElWSXEwUdIBX0FVX3lxTE5lVHRVLVZHLWYwSUJVNDMwX0hBYzlaR05Ldm83NkZwWGxfX2E3bEo0a2o0dzFFeUQ2ampTbG50aVFab2hGalpDU3lsWENwNWVVNTdFbGZIdlBPRVVGUXRF?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 02 Nov 2026 08:00:00 GMT
- [越跌越買 台股 ETF 受益人創高挑戰兩千萬人 00415A 等24檔受益人創高 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1ySWgyZTA5YU9yalE5SzlKR2ZMamhMc2s5WlZvbUZHaWM3c3JFZlE5M01fMWh2ZjExaHBSdDBkUEdrVHJUemZTS3hKX1NiRXViWko4UkhreUJ6UdIBX0FVX3lxTFB0RzhSU2VvUGUwSVE5c28xUF8xd0pNTmtGN3l5S0ZteEhXUFFKQmJDMDVOU0xfblVIbElEQm15ZlRSZWdFOWdZY1RLUUk5LWdDNzh4NmxVaWN6dGl6MkZB?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 02 Nov 2026 08:00:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Chip and AI stocks give up some gains ahead of AMD earnings (AMD:NASDAQ) - Seeking Alpha；Ed Yardeni Sees AI Chip Rebound, Year-End Stock Rally — Warns Of Midterm Election, Iran War Risks - TradingView；假日常工具、真色情換臉，數百款 AI App 暗藏「深偽」性剝削陷阱 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AMD 超微 | 新聞直接提及 | -0.53 | -9.54% | N/A | 466.84 | 516.10 | -9.54% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 產業/供應鏈推估 | -0.08 | -47.71% | +47.86% | 59.97 | 114.68 | -47.71% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | -0.06 | -8.48% | +0.98% | 202.06 | 228.38 | -11.52% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.06 | -3.92% | -2.31% | 2,320.00 | 2,480.00 | -6.45% | 同向 | 86.28 | 27.01 | 511.86B TWD / 54.65% | 2026-10-01 |
| MSFT 微軟 | 產業/供應鏈推估 | -0.02 | +12.63% | +3.07% | 507.12 | 521.91 | -2.83% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -12.99% | -14.70% | 322.23 | 446.77 | -27.88% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.04 | -3.02% | +3.06% | 642.00 | 703.00 | -8.68% | 同向 | 13.92 | 48.77 | 88.13B TWD / 45.52% | 2026-10-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.04 | -6.26% | -1.00% | 3,860.00 | 4,920.00 | -21.54% | 同向 | 60.69 | 65.57 | 55.40B TWD / 1.97% | 2026-10-01 |

關聯理由（前 3）：
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。 方向判斷命中詞：恐, 重挫, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：恐, 重挫, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：恐, 重挫, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Chip and AI stocks give up some gains ahead of AMD earnings (AMD:NASDAQ) - Seeking Alpha](https://news.google.com/rss/articles/CBMingFBVV95cUxOd2tWdkUzZldKRGVYT0FjMlRDZnJ6b2F6cWlQbTVxRWRjQjlMTDZFVERkYldQMnhqNmRwazN4X0pQQi1EYnlqbWNVTTRSOUNFUWtmUlVRa1FfcXdxdzh2TjlIdVlqUFl6WXlKNFFCVzFLRjBMWWRyaWVjOXQySTJsXy05RUZFcWU0NTZJTTRLeHlIdDh6QU5VRmdxclJQUQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 02 Nov 2026 18:41:59 GMT
- [Ed Yardeni Sees AI Chip Rebound, Year-End Stock Rally — Warns Of Midterm Election, Iran War Risks - TradingView](https://news.google.com/rss/articles/CBMi6gFBVV95cUxOcVNpLWNqVXBjN21SRnJRV3F1RkNybVNBbkwyN2dRLXdoejdSeUJUNm95ZDdLbXRwelh0amY0Tk1TcjhpY1FTMHAxXzhIaHNUbFJNNFlEd1FKSGhvSDFSSmZmVGdUTGpWa0lJRkVoMlh3T1F6ZF94Q1B1UjBfZWJlUXpkaTBfcjgxRGtCRVpSLUdvbTBpVkVzVGpmNThYM1ExNWhlNmNSaGtCNmRBVExtNUo4UVUxY3czbjFIQTVxS3B2WGc1ZjR2MHZLRXBQNElhYWY5dlI1eGNXWXVmX0tTRzNNWkhzZlI4Y1E?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 02 Nov 2026 11:08:29 GMT
- [假日常工具、真色情換臉，數百款 AI App 暗藏「深偽」性剝削陷阱 - TechNews 科技新報](https://news.google.com/rss/articles/CBMijwFBVV95cUxQTndUeWdnN3dqRVdDTHd4a09Gbk51dlpkNVM5QUN1bWU1V2t2UjFUN1BjSXZiYndueWhWYVpoS2RXRUo3bzVtNDljYXhYTjdCOTgzOHllcWV5c2dTVE9PZzZzYnc1dkdQSlVER3RFZ21wbnZZaHlrYnFDOVhHRTZBX25nZEpVbVdqV05XdEtMQQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 03 Nov 2026 02:00:41 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Micron Falls 4% as Kioxia's Cautious Outlook Hits Memory Stocks; Western Digital Drops 5%, SanDisk Slides 3% - 24/7 Wall St.；Micron vs. SanDisk: China's DRAM Scare Hit Both Stocks, but 1 Is the Better Buy - inkl；Kioxia Drops Over 15% to Six-Month Low Without Dragging Down US Memory Stocks: Micron, SanDisk Up Over 2% Pre-Market, SK Hynix Gains Nearly 5% - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| SNDK SanDisk | 新聞直接提及 | 0.00 | -23.47% | -14.38% | 1,075.08 | 2,335.00 | -53.96% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 新聞直接提及 | -0.57 | -14.15% | N/A | 833.59 | 971.00 | -14.15% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -8.48% | +0.98% | 202.06 | 228.38 | -11.52% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- SNDK：新聞直接提及「SanDisk、SNDK」，共 6 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：falls, upgrade。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- MU：新聞直接提及「Micron」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Micron Falls 4% as Kioxia's Cautious Outlook Hits Memory Stocks; Western Digital Drops 5%, SanDisk Slides 3% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi3wFBVV95cUxQd24xZ3lROHBoV1M2WWN3VmlMUjNjZ1ZfZnNNNGFmWnhZZ2d5Qnl4TjZMd3FPSm44N0VIRFhVM2s2RkNpVmdvMWJYeUZnRWR5YWhIdmtKdUpiQndZV19vaFlFRU1hZ1FfTk9GRzJ4M3lXLVJHclZ0cmpzYW9CbkJvb1BYNGNDYmpJTkJhWkRmMklmN3EtM2ZYc2V2bzEzdGZCVTJtZmVvVVk1SjhTQUQtNzZ2MDlQaXQ3T3NSaVBjQ0FCRm53Mkc3UEtzOGNWaUc2XzhVb0NNS3Ryc1JsZkVN?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 02 Nov 2026 18:53:00 GMT
- [Micron vs. SanDisk: China's DRAM Scare Hit Both Stocks, but 1 Is the Better Buy - inkl](https://news.google.com/rss/articles/CBMiowFBVV95cUxOZTkyZWhISU1jNWlma1RXOVM3djc2MXE1ZGlyY25sTGtuMHVnbVk2RWNCTGQxSWlnVWlmY2NxWnEyRGhVUXZxVzlrOEQ3dWQ2TTRDNWFSRDBjd2dscUE0WmJlVkxVZmdSQWNMRC1BQ0VMYjRmLW1nSGlfQTl2dUVxeEM5bUJYMWtPU0ZDaHZQeWtqZFVCd0xqNHczZThWVkI3LVQw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 02 Nov 2026 12:30:03 GMT
- [Kioxia Drops Over 15% to Six-Month Low Without Dragging Down US Memory Stocks: Micron, SanDisk Up Over 2% Pre-Market, SK Hynix Gains Nearly 5% - TradingKey](https://news.google.com/rss/articles/CBMi9gFBVV95cUxOR0hKX2llQ1NhcFNlbzhnTEwySGwxSEs3azIxMW9DOFBTMGp1MWdXQzg0VmtTT3gyS2pWR0s4TjdPWjhyZXgxNXQyVVNwdEIwbk9DdHNjNllvaTJiYWNBdlhEOTVvWkl6Zk9FTG0wbVlITHZFZV9pSjdpYmFSZi1PcDBBbkpkdUM4YWhWd2RXVWt1XzJOc1hFOW8zZFZqOS1oOGk1LWNidGEyRkxnNnpoeEVOOUI4c3VXaXcxY0xyeHVVMkYweGFxRHBtV19oaDlVcjMzYWdubENHN3NndUF2YmU4aUV2a3R2Y0dURHY4SGV0YzZRUlE?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 02 Nov 2026 09:40:53 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：AMD Q3 Earnings Preview: Can AI Chip Growth Reverse an 11% Decline? Wall Street's Highest Target Price at $1,250 - TradingKey；Kioxia Drops Over 15% to Six-Month Low Without Dragging Down US Memory Stocks: Micron, SanDisk Up Over 2% Pre-Market, SK Hynix Gains Nearly 5% - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AMD 超微 | 新聞直接提及 | 0.00 | -9.54% | N/A | 466.84 | 516.10 | -9.54% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 新聞直接提及 | 0.00 | -14.15% | N/A | 833.59 | 971.00 | -14.15% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | -23.47% | -14.38% | 1,075.08 | 2,335.00 | -53.96% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 方向判斷命中詞：decline, growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MU：新聞直接提及「Micron」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。

### 主要來源

- [AMD Q3 Earnings Preview: Can AI Chip Growth Reverse an 11% Decline? Wall Street's Highest Target Price at $1,250 - TradingKey](https://news.google.com/rss/articles/CBMivAFBVV95cUxOWlM2dGN1RU5oXzJfRlJ0VlJmMDFxWW01cmRXWkUwZU1PRncydV9HQ0MzUDhBOGNna0RnSFVjaEFTSmxINTNMZlhLRlBJS1daNllBVENKUkVVNmRSQlFqTFFnNUNPSFZabDk1emMwbkJscm03eTFlZlh1SHNkdDBTS0R4c19jM3hSNVVEUzZWOVpnejNQbGVtblFyMTJtYkllcjlQRV9pMURCQkN1QzNJZmMtNVhEOTlyRGVSSA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 02 Nov 2026 08:50:53 GMT
- [Kioxia Drops Over 15% to Six-Month Low Without Dragging Down US Memory Stocks: Micron, SanDisk Up Over 2% Pre-Market, SK Hynix Gains Nearly 5% - TradingKey](https://news.google.com/rss/articles/CBMi9gFBVV95cUxOR0hKX2llQ1NhcFNlbzhnTEwySGwxSEs3azIxMW9DOFBTMGp1MWdXQzg0VmtTT3gyS2pWR0s4TjdPWjhyZXgxNXQyVVNwdEIwbk9DdHNjNllvaTJiYWNBdlhEOTVvWkl6Zk9FTG0wbVlITHZFZV9pSjdpYmFSZi1PcDBBbkpkdUM4YWhWd2RXVWt1XzJOc1hFOW8zZFZqOS1oOGk1LWNidGEyRkxnNnpoeEVOOUI4c3VXaXcxY0xyeHVVMkYweGFxRHBtV19oaDlVcjMzYWdubENHN3NndUF2YmU4aUV2a3R2Y0dURHY4SGV0YzZRUlE?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 02 Nov 2026 09:40:53 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Chip and AI stocks give up some gains ahead of AMD earnings (AMD:NASDAQ) - Seeking Alpha；Ed Yardeni Sees AI Chip Rebound, Year-End Stock Rally — Warns Of Midterm Election, Iran War Risks - TradingView；台積電評估德州布局美半導體協會執行長：爭取延長投資稅務抵減| 產經 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | +0.28 | -3.92% | -2.31% | 2,325.00 | 2,480.00 | -6.25% | 背離 | 86.28 | 27.01 | 511.86B TWD / 54.65% | 2026-10-01 |
| 3711 日月光投控 | 新聞直接提及 | +0.28 | -3.02% | +3.06% | 641.00 | 703.00 | -8.82% | 背離 | 13.92 | 48.77 | 88.13B TWD / 45.52% | 2026-10-01 |
| AMD 超微 | 新聞直接提及 | +0.24 | -9.54% | N/A | 466.84 | 516.10 | -9.54% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 產業/供應鏈推估 | +0.04 | -47.71% | +47.86% | 59.97 | 114.68 | -47.71% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2303 聯電 | 產業/供應鏈推估 | +0.03 | -14.06% | -12.35% | 107.00 | 164.50 | -34.95% | 背離 | 6.80 | 16.25 | 25.35B TWD / 27.22% | 2026-10-01 |
| NVDA 輝達 | 產業/供應鏈推估 | +0.02 | -8.48% | +0.98% | 202.06 | 228.38 | -11.52% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | +0.02 | -14.15% | N/A | 833.59 | 971.00 | -14.15% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.02 | -23.47% | -14.38% | 1,075.08 | 2,335.00 | -53.96% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip, foundry。 方向判斷命中詞：rally。
- 3711：新聞直接提及「封測」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：rally。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Chip and AI stocks give up some gains ahead of AMD earnings (AMD:NASDAQ) - Seeking Alpha](https://news.google.com/rss/articles/CBMingFBVV95cUxOd2tWdkUzZldKRGVYT0FjMlRDZnJ6b2F6cWlQbTVxRWRjQjlMTDZFVERkYldQMnhqNmRwazN4X0pQQi1EYnlqbWNVTTRSOUNFUWtmUlVRa1FfcXdxdzh2TjlIdVlqUFl6WXlKNFFCVzFLRjBMWWRyaWVjOXQySTJsXy05RUZFcWU0NTZJTTRLeHlIdDh6QU5VRmdxclJQUQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 02 Nov 2026 18:41:59 GMT
- [Ed Yardeni Sees AI Chip Rebound, Year-End Stock Rally — Warns Of Midterm Election, Iran War Risks - TradingView](https://news.google.com/rss/articles/CBMi6gFBVV95cUxOcVNpLWNqVXBjN21SRnJRV3F1RkNybVNBbkwyN2dRLXdoejdSeUJUNm95ZDdLbXRwelh0amY0Tk1TcjhpY1FTMHAxXzhIaHNUbFJNNFlEd1FKSGhvSDFSSmZmVGdUTGpWa0lJRkVoMlh3T1F6ZF94Q1B1UjBfZWJlUXpkaTBfcjgxRGtCRVpSLUdvbTBpVkVzVGpmNThYM1ExNWhlNmNSaGtCNmRBVExtNUo4UVUxY3czbjFIQTVxS3B2WGc1ZjR2MHZLRXBQNElhYWY5dlI1eGNXWXVmX0tTRzNNWkhzZlI4Y1E?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 02 Nov 2026 11:08:29 GMT
- [台積電評估德州布局美半導體協會執行長：爭取延長投資稅務抵減| 產經 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1PSmY3YS1Gb2pUNnUxWjlCbkdoc1NieUVobWYzVWViR29KWWQ1Skl6Njg5OC1xZmpCM0tpakxwYWJoTjhuNTZYdUxROGNPRlZHYWpER0t5cXpNRXdYOEE?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 02 Nov 2026 23:52:00 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：輝達Rubin液冷商機升溫！奇鋐、雙鴻、健策、富世達等台廠受惠- 日報 - 工商時報；液冷技術升級台廠搶布局- 財經要聞- 工商時報 - 中時新聞網

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.22 | -4.82% | -2.70% | 3,085.00 | 3,435.00 | -10.19% | 背離 | 75.13 | 40.79 | 21.02B TWD / 44.92% | 2026-10-01 |
| NVDA 輝達 | 新聞直接提及 | +0.21 | -8.48% | +0.98% | 202.06 | 228.38 | -11.52% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐」，共 1 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：受惠。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [輝達Rubin液冷商機升溫！奇鋐、雙鴻、健策、富世達等台廠受惠- 日報 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5HT1p1WG5NdFJWdDgwSFp1ckFaMUNsTGdSTzZaVDhOTWtIQl90Rmh4SHZNTlIxUTdIcl9LTl9jR0s2cGpKR2xSdWpEUzRwZlFyQlNTblVuUTRGWFllcGsw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 01 Nov 2026 19:00:00 GMT
- [液冷技術升級台廠搶布局- 財經要聞- 工商時報 - 中時新聞網](https://news.google.com/rss/articles/CBMia0FVX3lxTE1pVFpYTk5mZ28zb3FOMWFtSW9YMENMMlphYVBqWVItNnVnZVU2VlFfZGFHVTYwZUFfTEQwdzJCV1d0c2h0NTFkUnFJZDRMRUdrem0wTXNKdWJBcHYzcDVORkpfd05HdGRQajdj?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 01 Nov 2026 20:10:00 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：美股激烈反應 CSP 與 Intel 財報 分析師看好台股 AI 供應鏈 - 經濟日報；整理包／黃仁勳概念股笑了！輝達季度財報超預期 完整台廠供應鏈名單、潛在受惠股一次看 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.21 | -8.48% | +0.98% | 202.06 | 228.38 | -11.52% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.21 | -47.71% | +47.86% | 59.97 | 114.68 | -47.71% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +8.42% | +21.33% | 338.32 | 344.63 | -1.83% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | -0.20% | +2.45% | 247.50 | 289.00 | -14.36% | 不適用 | 15.21 | 16.55 | 1158.63B TWD / 38.42% | 2026-10-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [美股激烈反應 CSP 與 Intel 財報 分析師看好台股 AI 供應鏈 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9ITV96MDl5dnJ6RkJiOWtoZ0kwRDNxc2paWTJScDVRZUlRaTdWSXU4NXExdldHemNGSjdIWlc3QmQtYTVRWktpVG9yM1E1TzJwQWJhR0RFcGtjZ9IBX0FVX3lxTE03MlJXanhmd0pCQ2lMcWpnVEtZaHZkOE12bzlxY28yVW80ejNMX0dZb3Bqc2xmcjhmeUktRVR3VVRZRDBrcUU4dDQ4XzFkeXhPb21QOWxZWEczZXlfbk5v?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 01 Nov 2026 02:33:49 GMT
- [整理包／黃仁勳概念股笑了！輝達季度財報超預期 完整台廠供應鏈名單、潛在受惠股一次看 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBQUlViSHpPeDVlY29yaHFNNE5NcVlUQnE3ZThTcXRGNHgxYTVPOVVTRDlaTDV6Zml5WEwxVHNSeGFDcnVHUHhRSW15SzNpU0dYVDU3dThWNEVCbkZI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 01 Nov 2026 08:00:00 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：統一證券：台股靜待籌碼沉澱後，醞釀築底反彈- 新聞 - MoneyDJ；國票證券：台股有望逐步築底- 新聞 - MoneyDJ；外資撤離加劇台股震盪，匯率與槓桿風險也同步升高- 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [統一證券：台股靜待籌碼沉澱後，醞釀築底反彈- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQOUJfNGRoUUN1bEFEUkVDbHFGb1hLMmxSdDhhd0dpSzQtV3Z1NjN2Tzl3ZzB3ekhJTjlKNG5OaXd5Z1BUOV9pWUp1Z3JGLVVzbDllZGV3cUV3QUlQMEZEYXpVeUZxUzRlMTM4S1JvWjdQWVYtSHFxNWllajM4QVdYZTdsdVEtd2NqM3RFNHJwSUIyUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 03 Nov 2026 00:34:00 GMT
- [國票證券：台股有望逐步築底- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQYXR1cDNDNmoycFVPOURzS2ZMTEV3Z2s5b1JXQkdoYVQ4c3pva1NKOXFPXzAyUWw0cUdUMTh3aDhYNUdUY2kxcnBmRFppVHp5LTNWdjduTFZQYS1hcFRNVzdZYjYtQ1k3U0hBTU5xNUpLQ1U2cDg2Vi1tUnprRERUSTdJUjVfY3ZHUkZaMWY0OXhjdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 03 Nov 2026 00:34:00 GMT
- [外資撤離加劇台股震盪，匯率與槓桿風險也同步升高- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNdlRicEJ6Z1VYeWFNUG5pVk9nMG9oSXJ2Y2RkWWFIM1Y0YjBjTXZhT0E3OHh3SHNmUHVsLXVNVkh0bjMtNEdXUUFqSEUzRlRfaGZYelFpSGFDckJPSFVOTXkta3QxVklQLXZhM1Y5SThvWmRFb0g5SWVSOVpGcGlvNkJ2WW9WcEZEcUZ4NVRvMGs2UQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 03 Nov 2026 00:20:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
