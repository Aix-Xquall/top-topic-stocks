# 每日股市熱門話題分析 - 2026-11-13

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜中性｜熱度 8｜市場確認 50.23｜同向 1/2
2. **綜合市場情緒**｜負向｜熱度 47｜市場確認 0.00｜同向 0/2
3. **AI 伺服器與資料中心**｜正向｜熱度 17｜市場確認 41.99｜同向 6/8
4. **新興題材：TradingKey**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0
5. **半導體與晶片供應鏈**｜正向｜熱度 3｜市場確認 25.66｜同向 5/8

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.56（樣本 24）
- 5日相關係數：0.42（樣本 20）
- 同向比例：13/24

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 50.23 | 1/2 | 1 | +5.08% | +11.49% |
| 綜合市場情緒 | 0.00 | 0/2 | 2 | -4.03% | -7.87% |
| AI 伺服器與資料中心 | 41.99 | 6/8 | 2 | -3.50% | +7.39% |
| 新興題材：TradingKey | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | 25.66 | 5/8 | 3 | -6.03% | +4.77% |
| 關稅與供應鏈轉移 | 0.00 | 0/1 | 1 | -27.23% | -17.22% |
| 新興題材：CoreWeave | 0.00 | 1/3 | 2 | -19.90% | +27.68% |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價呈負相關；應檢查正負向詞庫，並降低新聞直接提及但股價背離的權重。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-10-30 | -0.00 | -0.05 | +47.62% | 21 |
| 2026-10-31 | 0.50 | -0.68 | +80.00% | 15 |
| 2026-11-01 | 0.47 | -0.40 | +85.71% | 14 |
| 2026-11-02 | -0.15 | -0.06 | +27.78% | 18 |
| 2026-11-03 | -0.03 | 0.08 | +40.91% | 22 |
| 2026-11-04 | -0.21 | 0.35 | +15.79% | 19 |
| 2026-11-05 | 0.13 | -0.53 | +66.67% | 12 |
| 2026-11-06 | -0.18 | 0.77 | +100.00% | 5 |
| 2026-11-08 | -0.21 | 0.03 | +23.08% | 13 |
| 2026-11-09 | -0.56 | -0.62 | +60.00% | 10 |
| 2026-11-10 | -0.32 | 0.24 | +3.45% | 29 |
| 2026-11-11 | 0.34 | -0.26 | +46.67% | 15 |
| 2026-11-12 | -0.09 | 0.07 | +50.00% | 14 |
| 2026-11-13 | -0.56 | 0.42 | +54.17% | 24 |

## 歷史回測摘要

- 回測日期：2026-11-13
- 近5日 3日相關：0.09
- 近5日 5日相關：0.14
- 同向比例：+37.93%
- 權重狀態：未調整

- 方向準確度：+37.93%
- 信心排序準確度：0.09
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

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Sandisk, Micron, and SK Hynix Slide 3% as NVIDIA Shake-Up Hits Memory Stocks - 24/7 Wall St.；Micron vs. Sandisk: The AI Memory Supercycle Is Big Enough for Both, but Here's the Better Buy. - The Motley Fool；Micron Stock Surges After CoreWeave's AI Earnings Surprise - TradingView

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | -17.77% | N/A | 798.44 | 971.00 | -17.77% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.28 | +17.08% | -5.76% | 977.69 | 2,335.00 | -58.13% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | -0.51 | -27.23% | -17.22% | 166.19 | 228.38 | -27.23% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：fall, surges。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 5 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 2 篇新聞命中。 同時符合主題標籤：HBM。 方向判斷命中詞：fall。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Sandisk, Micron, and SK Hynix Slide 3% as NVIDIA Shake-Up Hits Memory Stocks - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiuAFBVV95cUxNZElZUF9heWhMaUlVdXpsYTV0S0RkQ1ZjMHVncGRYZXo1TG4tYzBSMjY3VkN0eld5cGdtcHpBeWJaWU16d3ZReU13MzY1QkgzT2MzWS02UzB1RTBseURHeFJuMGdyR093NzlGUFJCejRMY0lOSktOc2hWM2pDS1ZTR3JxM1RpNEVLQnI3VGIwby1vSHN1elRFRkZUTThjNms1SmgyRDc5QkxJYklvT0VQN25vNWtvc0FZ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 12 Nov 2026 16:56:00 GMT
- [Micron vs. Sandisk: The AI Memory Supercycle Is Big Enough for Both, but Here's the Better Buy. - The Motley Fool](https://news.google.com/rss/articles/CBMilwFBVV95cUxNSUJ2cmkyUE9WVjNZcUxXZ195TnFya2g4cnBvRFpfMkxqd0NhMGNpczA3bmI2Y3VZb3p5ZHJTWlNxTlUxSjJnSWNjNjR3ejVrODdMRkhVX25zTnktNUkybzY1MUxjT3BXdVN3NFVSVUdqNGpVVU5DN1FRcjRkcmJjaEFKbUthV1JQUTNBN1ZIY3BLSktTdjgw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 12 Nov 2026 05:00:00 GMT
- [Micron Stock Surges After CoreWeave's AI Earnings Surprise - TradingView](https://news.google.com/rss/articles/CBMiugFBVV95cUxPMzdGTnBhbUJrTm94czdjbEx6TmF6M01KYklPeWpkRmtUbGxUaTZaZWg4bFBBYklUTnhqenRPbldTd1ZxNmlzazVoWHRySGFVaHlWc2N1MEY2LUxDaUEzUUxYQVktdEc2dHdWd2FZaHd4NW03UTU1ZnhMLTg1dTdodlVRcHVCdkJlbmViQXFqSlF6aXBMdHRzSExQN0ZNZjAxVUROZDF2SVB6dHl0MjBPR1dMRkNObVJNdGc?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 11 Nov 2026 16:01:54 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：黃仁勳辭職衝擊美股、台股卻強彈逾千點！聯發科漲停 ASIC 刷一排紅燈 - 經濟日報；黃仁勳去職利空出盡　台股勁揚逾1200點突破44300點 - 經濟日報；台股開盤漲627.88點 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | -0.21 | +4.70% | +4.46% | 2,385.00 | 2,480.00 | -3.83% | 背離 | 86.28 | 27.12 | 586.89B TWD / 59.71% | 2026-11-01 |
| 2454 聯發科 | 新聞直接提及 | -0.21 | +3.36% | +11.27% | 4,235.00 | 4,920.00 | -13.92% | 背離 | 60.69 | 63.58 | 55.03B TWD / 5.77% | 2026-11-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。
- 2454：新聞直接提及「聯發科」，共 1 篇新聞命中。 方向判斷命中詞：衝擊, 漲停。

### 主要來源

- [黃仁勳辭職衝擊美股、台股卻強彈逾千點！聯發科漲停 ASIC 刷一排紅燈 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5tRVVUMER0WWlRU1VvRmFLcVQ0WG9lTFlxUVJlSXBjMzRQX1J3YzR1eDRoSkpkaVpua3BmMlc5QVIxY2h5ZDczNnNkOEZfUjEtSmhHd3ZTdDFDUdIBX0FVX3lxTE1qQTdKTDhjYkU5dDZSbDYwV2pOQVI1RHdwTjg2RjlXdnh6NERXYXV6TTlpLUhaaWVaazAtNDZTandaTG9GdzU1VURKeEdtS0ZkLTk4U1RrUW13eFZkaVI0?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 12 Nov 2026 09:00:00 GMT
- [黃仁勳去職利空出盡　台股勁揚逾1200點突破44300點 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1qQldQRmEyaUpjeFpxZ3dlaFNybTZoWW0tZFBEMFJXR2RWNzVXdmc0OWYxeXBYRndwWkFMbkZadHdRTDlVX1VudkFxdWljemQ1RUtnZEtidDhpZ9IBX0FVX3lxTE5nam5LLWRGVmZwZUgxRlp1S1dZcDF5NVU0aGY5YUFfZW1lNzVIR2F3NldqX3JNVVpoYUVIeUFCaTE2UzFpaEFodmhPRkkzTnpwSkZkVHJnajNiYXUydTVJ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 13 Nov 2026 01:21:22 GMT
- [台股開盤漲627.88點 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBIbzAySlRvWWx5NFZnQzA0YUNTblI2S0ZjX1ZGVDBINVNLTE9SWDZKS0JKbVZVR0pFYmR3S3NIU2l6TVJwbHNISW9TcWN5SkJGSGpmcWxLREt3d9IBX0FVX3lxTE9fTDQ3WmZPaU5fVlNlWVRPeEw0eDBDOUc1SGVuOVN4YTJvczg0Tmh5N041VVEzYW11cUR5TEFnZ0R6bmdkdVdwTEZpY2pVUnJ5U3FWRE1kekNMMk4yUWp3?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 13 Nov 2026 01:12:21 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：外資僅賣超個位數、台股卻殺1,165點！黃仁勳風波衝擊 AI 股 - 經濟日報；Stock Market Today, Nov. 11: Intel Climbs on Broader Chip Rally as AI Infrastructure Demand Lifts Semiconductor Stocks - Yahoo Finance；華碩打造「代理人電腦」生態系，PC 變身全天候 AI 助理 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.28 | -46.63% | +50.89% | 61.20 | 114.68 | -46.63% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.03 | -27.23% | -17.22% | 166.19 | 228.38 | -27.23% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.06 | +13.41% | N/A | 585.30 | 585.30 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.06 | +4.70% | +4.46% | 2,385.00 | 2,480.00 | -3.83% | 同向 | 86.28 | 27.12 | 586.89B TWD / 59.71% | 2026-11-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | +16.16% | +6.30% | 523.00 | 523.00 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.04 | +3.75% | -6.40% | 364.36 | 446.77 | -18.45% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.04 | +4.46% | +2.45% | 618.00 | 703.00 | -12.09% | 同向 | 17.55 | 33.64 | 88.62B TWD / 47.13% | 2026-11-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.04 | +3.36% | +11.27% | 4,235.00 | 4,920.00 | -13.92% | 同向 | 60.69 | 63.58 | 55.03B TWD / 5.77% | 2026-11-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：衝擊, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：衝擊, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：衝擊, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [外資僅賣超個位數、台股卻殺1,165點！黃仁勳風波衝擊 AI 股 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5sUEY4SHBLVjhvTnh3VDVCOExPdHNnRlhiamstLWNDWGkxcEZrdDloVjI5bVFELW9lRG05WnpLTVdDYk04TV9HR2x3aTU5NnBQVGg1SUpoR2lOd9IBX0FVX3lxTE9KT3NUdGFzay1GSFE5ODhyQUlfOGhKR0NLYngzSGZzQXl2enVmbkZ4NUJobTZsSktWQ2tVZkh2b2ZXdV9zUTlqTkNGRkM1WVo0c0JLdW9NWGpEekJWeW5r?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 12 Nov 2026 08:00:00 GMT
- [Stock Market Today, Nov. 11: Intel Climbs on Broader Chip Rally as AI Infrastructure Demand Lifts Semiconductor Stocks - Yahoo Finance](https://news.google.com/rss/articles/CBMilAFBVV95cUxPTkhodDFrb2Rsa1d5c0x0U25GVTJqRS1xRndhSjh5UkxsNnc5WnZuZElydWpRYWpIWlZteXFlUmlGS2ttR0I4YlE0UW1lVkhUZjYwSzBTaTVpRmxtMlg5LWhqLTVTaGh5SnFIRjFZcXAzWnFYdFZzNDFjQXBFTUI0V3NkNktrRUZIU05BVGtTdVFJYzZt?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 11 Nov 2026 23:04:34 GMT
- [華碩打造「代理人電腦」生態系，PC 變身全天候 AI 助理 - TechNews 科技新報](https://news.google.com/rss/articles/CBMieEFVX3lxTFAxNndxWEUtMWt3NXJjeUY1eTlXQXYyYzRFZnZDSVJFUHJxRDQ0RTB4N2FHQ2ZVbmlwRnpQdVdpbk5LSkZRZW9jaDhBeVpyU21jTy1GaUpGbnFJWF8yc2lfU0Q3amh2ZFlzNE95b0tIYU50b2NNRjRtQg?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 13 Nov 2026 01:46:46 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：US Memory Stocks Rebound Overnight as Western Digital, Micron Rise Over 5%, SanDisk Gains Over 6% - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | -17.77% | N/A | 798.44 | 971.00 | -17.77% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | +17.08% | -5.76% | 977.69 | 2,335.00 | -58.13% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。

### 主要來源

- [US Memory Stocks Rebound Overnight as Western Digital, Micron Rise Over 5%, SanDisk Gains Over 6% - TradingKey](https://news.google.com/rss/articles/CBMiuAFBVV95cUxNRnhzanJpc2ZzN09NTDV0TldjQkdvQ010STcxUGpIU0s5VGFxXzdPaFgxQ3VZSlhXbHJlNVBheGhZQUJTVl96RHMwT0xJRzJRakpyUVNwTzVBUHVvWnpvc0FGTkxSeHBOR04xT0xObXd2dS1iMm5BMmI3X3VrNFZnTDNUd0NzTlVIQTVPVUtyNFFSSHFlV0ZBZm9mTlhqYWlUVG5fZEY3STBJcHQxZGxyOXBEZjl6TV8z?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 11 Nov 2026 09:00:25 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Stock Market Today, Nov. 11: Intel Climbs on Broader Chip Rally as AI Infrastructure Demand Lifts Semiconductor Stocks - Yahoo Finance；Applied Materials forecasts quarterly revenue above estimates on strong AI chip demand - Reuters；Explainer: Tougher curbs on AI chip sales to China likely after Nvidia CEO resigns - Reuters

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.27 | -46.63% | +50.89% | 61.20 | 114.68 | -46.63% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.24 | -27.23% | -17.22% | 166.19 | 228.38 | -27.23% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.05 | +4.70% | +4.46% | 2,385.00 | 2,480.00 | -3.83% | 同向 | 86.28 | 27.12 | 586.89B TWD / 59.71% | 2026-11-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.05 | +4.45% | +2.64% | 104.50 | 164.50 | -36.47% | 同向 | 6.80 | 14.92 | 25.20B TWD / 18.33% | 2026-11-01 |
| AMD 超微 | 產業/供應鏈推估 | +0.04 | +13.41% | N/A | 585.30 | 585.30 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | +0.02 | -17.77% | N/A | 798.44 | 971.00 | -17.77% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.04 | +17.08% | -5.76% | 977.69 | 2,335.00 | -58.13% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.04 | +3.75% | -6.40% | 364.36 | 446.77 | -18.45% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：rally, strong。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：rally, strong。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 3 篇新聞出現相關標籤。 方向判斷命中詞：rally, strong。

### 主要來源

- [Stock Market Today, Nov. 11: Intel Climbs on Broader Chip Rally as AI Infrastructure Demand Lifts Semiconductor Stocks - Yahoo Finance](https://news.google.com/rss/articles/CBMilAFBVV95cUxPTkhodDFrb2Rsa1d5c0x0U25GVTJqRS1xRndhSjh5UkxsNnc5WnZuZElydWpRYWpIWlZteXFlUmlGS2ttR0I4YlE0UW1lVkhUZjYwSzBTaTVpRmxtMlg5LWhqLTVTaGh5SnFIRjFZcXAzWnFYdFZzNDFjQXBFTUI0V3NkNktrRUZIU05BVGtTdVFJYzZt?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 11 Nov 2026 23:04:34 GMT
- [Applied Materials forecasts quarterly revenue above estimates on strong AI chip demand - Reuters](https://news.google.com/rss/articles/CBMivgFBVV95cUxNeVJYSC1hal9odmptblkwc25YV0pZQXBaaTd0SGFyMW5tT1ZtNzZaTlN0OGFnY2I0dnI3ZmZRaXpwUThvZW5kay1tMElieklOVVZLTDFBTmtQbkpiSWpUZzlLNnZPRmlJSkxoWVZhZGlveTdzNjVsN0ZtZUVMMnk2REQtYmRHRzQwMDhNMVBYQXVQbjBpcHNNYnFWWldTbUItYV9pT1hMYkwwZi1jS0pvZXp4eHJhbHE4OEp6RW13?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 12 Nov 2026 21:14:13 GMT
- [Explainer: Tougher curbs on AI chip sales to China likely after Nvidia CEO resigns - Reuters](https://news.google.com/rss/articles/CBMiswFBVV95cUxQRERObVhKZklNOEliOFhfQmhqMmZaQWktbkVWTXlxZU8zbUtxQ1cwZnZpaGJwZ1djUHFFVVlydTFsQUd3UUJEV0NOdUliUGY1ZGNKN1ZPWG1zYkpxcEgtNGJlSFVrTi1EVm84MnFFbWxmeXR1YmotNUdzVFBtUVU1VmhPR3ZGTHFUcHlSUnRQQmU0WUYyRi1fdnNHOHc3QUh2OWVsQURUb3BwVTVaMm9NRUdnbw?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 12 Nov 2026 19:08:21 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：整理包／黃仁勳概念股笑了！輝達季度財報超預期 完整台廠供應鏈名單、潛在受惠股一次看 - 經濟日報；輝達供應鏈雜音頻傳！「7檔」保證不出軌 - 鏡週刊Mirror Media；黃仁勳事件台灣 AI 供應鏈非訂單消失，是規格升級放緩導致獲利增量縮水與遞延 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.28 | -27.23% | -17.22% | 166.19 | 228.38 | -27.23% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +13.72% | +27.27% | 354.88 | 355.63 | -0.21% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | +0.42% | +2.13% | 241.50 | 289.00 | -16.44% | 不適用 | 15.21 | 15.82 | 1305.32B TWD / 45.73% | 2026-11-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 3 篇新聞命中。 方向判斷命中詞：受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [整理包／黃仁勳概念股笑了！輝達季度財報超預期 完整台廠供應鏈名單、潛在受惠股一次看 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBQUlViSHpPeDVlY29yaHFNNE5NcVlUQnE3ZThTcXRGNHgxYTVPOVVTRDlaTDV6Zml5WEwxVHNSeGFDcnVHUHhRSW15SzNpU0dYVDU3dThWNEVCbkZI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 11 Nov 2026 08:00:00 GMT
- [輝達供應鏈雜音頻傳！「7檔」保證不出軌 - 鏡週刊Mirror Media](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBBTGR1UWhzUW9NMGhuZ2w2R3VldTJ1REsxcEtZdjRJaGhsOUl5VHp3WmtEeFM4Rzd0RGdhMkduVkk2QlNyMElPZVQzbTJZZk02SDBJNUxZY1ZDRzUt0gFiQVVfeXFMTnRmNzJaYU9TanlhN21KWmc0ZGpZSXRNMk5uOG1NYk9wc214eDVXcTJMcS16VnktZ2tkNUt4MkJTNW55SXd0V1NGQ2l0MWxCN0xSM0ZPb1FYNGFtR1V3OEdkM0E?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 12 Nov 2026 21:00:00 GMT
- [黃仁勳事件台灣 AI 供應鏈非訂單消失，是規格升級放緩導致獲利增量縮水與遞延 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiygFBVV95cUxOc2lQcm44UW0xTWxPQ1lpMkRqZHRnNmZRTHdyS3JyNWlkVC0wQ2pzTWxwdWlkZXJtNlQwa0lXNVJYekZob09LR1dGaFJWZU5VN0VuNEpSVkhOQjBqY0JfTUc3Z3ROdGtVT2lyYURWZURTcFdsNzhFeF8xY2ZIUFZUM1I0NkJOTFAyZnpBSC13TWswNzNWNndxejRkcUpGMkZxVmpBN1pQejgxZjFEcTR2Njd4cldHSDd1bms1OFQzcl9CTTY5VnBHUkJR?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 13 Nov 2026 02:03:45 GMT

## 新興題材：CoreWeave

摘要：新興題材：CoreWeave 相關新聞集中在：Marvell and Intel Rally 7% as CoreWeave’s Results Reignite the AI Chip Trade; Taiwan Semiconductor Climbs 4% - Yahoo Finance；Marvell and Intel Rally 7% as CoreWeave's Results Reignite the AI Chip Trade; Taiwan Semiconductor Climbs 4% - 24/7 Wall St.；Intel INTC Stock Recovers 25% as CoreWeave Earnings Boost Chip Shares - FXLeaders

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.28 | -46.63% | +50.89% | 61.20 | 114.68 | -46.63% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | +0.50 | +4.70% | +4.46% | 2,385.00 | 2,480.00 | -3.83% | 同向 | 86.28 | 27.12 | 586.89B TWD / 59.71% | 2026-11-01 |
| MU 美光 | 新聞直接提及 | +0.21 | -17.77% | N/A | 798.44 | 971.00 | -17.77% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel、INTC」，共 3 篇新聞命中。 方向判斷命中詞：boost, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「Taiwan Semiconductor」，共 2 篇新聞命中。 方向判斷命中詞：rally。
- MU：新聞直接提及「Micron」，共 1 篇新聞命中。 方向判斷命中詞：surges。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Marvell and Intel Rally 7% as CoreWeave’s Results Reignite the AI Chip Trade; Taiwan Semiconductor Climbs 4% - Yahoo Finance](https://news.google.com/rss/articles/CBMimwFBVV95cUxQYkgxNWZhV21wSTd3Y1JhcENLT2NoNEROWmd0cHdtbTAxSlVSNC1tNE5LbzN2MWxZX1o4dDFMZkNnWDFmNmw3VVdMTk9EZS1NZ1ByMkhCYjN0c19LTFdwdjUwWDIzQm9HV3h5b2hKRmFSOEtKRlB2MTVmNHo3bWxxcUFMYTFiMDZWTXBWT05GeXpQT3RSXy1yQlVDZw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 11 Nov 2026 14:48:18 GMT
- [Marvell and Intel Rally 7% as CoreWeave's Results Reignite the AI Chip Trade; Taiwan Semiconductor Climbs 4% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi4gFBVV95cUxOams4aFViZ0MzZnZKUXdOUEUtcVJ0QzNQTXpLSjExRjctOVdOZnhGZDU2WVlQWFJxMUZYNjFabC0tU1NMekFxT21VdjktUkNFZDZ4WmRFMi11MHY3MllzWXRPV3FhbjZ6dkxDV2RFMEY4XzVfZzdUTVlFcy01WU5PelljOElGb0dmekt0ZmZsbzU1NWJnTVczU0loYVpfNkJYQWUyZ1Y0MnBXaXlqTDN2MFZBME5xZFdVcE1iMGxWbVo3bnY4TkxTVnBMYUNON2FBT1J4YlVQQmg2NnRyZ2pmbU1R?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 11 Nov 2026 14:48:00 GMT
- [Intel INTC Stock Recovers 25% as CoreWeave Earnings Boost Chip Shares - FXLeaders](https://news.google.com/rss/articles/CBMisAFBVV95cUxOTXpSdWVYaGJoc3o4YlR1bVFuZ29GemZJSG82ZlFoY21DM3hPdzNlN1NWTjczLVhrZnh6dFRraFY4NW1mZHRGWXplN2VBaTVRWVFZVkRVZ2JUUXNHemppOFppMHdqVzNDTUx3UTE4UXRiSFdYVG1fYmdLSDlTYXJJVzc1cDFTeVhlNXhla19qWmRiXzB2eUp2RDRTVDVzZHNVSXlOZWdSVy1paThHeGdVQw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 11 Nov 2026 21:16:03 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：MSCI季度調整：臺股於全球ACWI/新興/日本除外亞洲權重分別升0.03、0.15、0.11個百分點- 新聞 - MoneyDJ；法人盤勢分析內容-台股 - MoneyDJ；統一證券：台股5日線未跌破前，仍有機會延續反彈格局- 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [MSCI季度調整：臺股於全球ACWI/新興/日本除外亞洲權重分別升0.03、0.15、0.11個百分點- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMieEFVX3lxTE15RFR4LUdmUXR6STNTaXNCVGlaUkVSaFhDNi1qRXpTRU1tcWpha1paWEItWHAtYXpfYlhUa0g0ZlFXTkpfVUh6YXN5ZVMwSnZtT3ZaSE53S05sYmVBRVRGZ1MwdWVWaURxSm92a0hTSnpyWjhjWnk3NQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 13 Nov 2026 00:33:00 GMT
- [法人盤勢分析內容-台股 - MoneyDJ](https://news.google.com/rss/articles/CBMijgFBVV95cUxObkhKOEN0UFc1QU5lS015Ny05WnF0aXpXUksxQU9pWUtMSXBWOFMzVDdqNHFDOXF2RUpiRlJOWWFjYWYxTUV5clgzOFlNUjNiRUZGemczYWxLUEl3Tml0SWhhNW82VmxpanlVTW5NNFpaQk1QSkxXYzRBZ2Y3RURpTXA2RHVJQTNrdURSVU53?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 13 Nov 2026 00:59:25 GMT
- [統一證券：台股5日線未跌破前，仍有機會延續反彈格局- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPWGdJeXZHb0lWRTduTDdsQ2NRUldEZGJ5OW5zVkczMkIxYm5Ub3NkNXVOUldFSm1lYW9hNlhxTkNkUGtXMlJjSnk2LXRhWDVycVcxS0lnS2MtRnk2MmNUdXVxTElmR0VGYkdhSXVOa0RqdUZQOFA5dVpVRHNKRnRNNGtBUTVjM0d0UDNIbUpCb0JRdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 13 Nov 2026 00:59:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
