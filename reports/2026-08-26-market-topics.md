# 每日股市熱門話題分析 - 2026-08-26

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **綜合市場情緒**｜正向｜熱度 50｜市場確認 81.30｜同向 2/2
2. **記憶體與 HBM 供應鏈**｜正向｜熱度 6｜市場確認 62.97｜同向 2/3
3. **AI 伺服器與資料中心**｜正向｜熱度 13｜市場確認 49.15｜同向 3/6
4. **新興題材：StartupHub**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0
5. **散熱與液冷供應鏈**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.08（樣本 16）
- 5日相關係數：0.22（樣本 16）
- 同向比例：8/16

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 綜合市場情緒 | 81.30 | 2/2 | 0 | +3.77% | +3.79% |
| 記憶體與 HBM 供應鏈 | 62.97 | 2/3 | 1 | +5.43% | +10.44% |
| AI 伺服器與資料中心 | 49.15 | 3/6 | 1 | +4.71% | -2.52% |
| 新興題材：StartupHub | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：台股冷颼颼散熱 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | 8.47 | 1/5 | 3 | -1.84% | +0.03% |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 相關性偏弱；應提高同向價格確認權重，降低泛 AI、泛半導體等寬標籤推估權重。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-08-12 | 0.52 | -0.47 | +87.50% | 8 |
| 2026-08-13 | 0.72 | 0.24 | +100.00% | 7 |
| 2026-08-14 | 0.34 | 0.57 | +92.86% | 14 |
| 2026-08-15 | 0.24 | 0.30 | +68.75% | 16 |
| 2026-08-16 | 0.37 | 0.51 | +70.00% | 10 |
| 2026-08-17 | 0.49 | 0.60 | +66.67% | 12 |
| 2026-08-18 | 0.29 | 0.36 | +80.00% | 10 |
| 2026-08-19 | -0.23 | -0.33 | +30.00% | 10 |
| 2026-08-20 | -0.72 | 0.06 | +50.00% | 8 |
| 2026-08-21 | -0.48 | -0.45 | +61.54% | 13 |
| 2026-08-22 | N/A | N/A | +50.00% | 2 |
| 2026-08-24 | -0.94 | -0.77 | +60.00% | 5 |
| 2026-08-25 | 0.01 | -0.58 | +35.71% | 14 |
| 2026-08-26 | 0.08 | 0.22 | +50.00% | 16 |

## 歷史回測摘要

- 回測日期：2026-08-26
- 近5日 3日相關：0.41
- 近5日 5日相關：0.33
- 同向比例：+33.33%
- 權重狀態：未調整

- 方向準確度：+33.33%
- 信心排序準確度：0.41
- 診斷：正相關

調整原因：近 5 日有效樣本 6 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：綜合市場情緒 相關新聞集中在：第一金-華江 對 承啟(2425)個股 單一券商歷史明細 - justdata.moneydj.com；全村的希望來了 台股還能繼續漲？分析師曝輝達財報「這一數據」最重要 - 經濟日報；誰在買？台股由低點一路拉抬逾900點 三大法人卻賣超53億元 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.42 | +6.48% | +6.75% | 213.05 | 214.72 | -0.78% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | +0.42 | +1.05% | +0.84% | 2,400.00 | 2,425.00 | -1.03% | 同向 | 86.28 | 27.82 | 467.58B TWD / 44.69% | 2026-08-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。

### 主要來源

- [第一金-華江 對 承啟(2425)個股 單一券商歷史明細 - justdata.moneydj.com](https://news.google.com/rss/articles/CBMikgFBVV95cUxNMGU1cXFCQk9xbnZsQkRnZHJwZnJmZUwtd3NxSmR5WFc3U1UyYWliLW5qZDZpZ3duMXFZR2pUQVlKRTFEQ0dkUWZiVzZNUVp6YU5ZekRlZ2RQRUZsR0l5azlNd2dYVG1pQnJUSEw2N2ltRUF3eXA5RmxIWUNtaG11blV0RnFnSERDTnhDZkptRlNCZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 25 Aug 2026 10:22:03 GMT
- [全村的希望來了 台股還能繼續漲？分析師曝輝達財報「這一數據」最重要 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9qYWhDOGgyajFkRFI1cGF2WUNEaFQ3THdWZ1VDa2RfcDNhT3RCUzk5MHVGN2ZIUExlNVdCSlM4SGtYQ1pOa3QyazdkUnY1U0dEejVHOUFjZHBOQdIBX0FVX3lxTFBMZGJNeE13ZlE0YlJraTlkM1NTZlFkd0t4VjdMMnlnVUZVRWZER2dYSnZBWkp5WXZ3eTMxWFZzd3YtbDJES2cxbmpxT1NhNEthT3N5c1cwR2dkWmZvSHFz?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 25 Aug 2026 04:04:41 GMT
- [誰在買？台股由低點一路拉抬逾900點 三大法人卻賣超53億元 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5jQ1dxWDU0cF9jOFd5M01JdzdMZnpFVWs0b0pDWXVNbDVScDZ0TkJCMHp2Rm5oZ1l5dUI2aXgxNVF3VnpQYUhtOHRBT1lMUG40Ul82eGFqR1lzUdIBX0FVX3lxTE55bGc0dG9UNXducmNsanY5eHU4X3FDTjd3VHBWcDVXYUFMRDJqVGtRVkc5YzFtdHM5Qm9FZXpram9ULVNLUUl4aXp2MWpyM1lxXzQya2VnOEtfWWtOeGdF?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 24 Aug 2026 09:00:00 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：MU, INTC, SNDK: Chip Stocks Rally After-Hours On AMD’s Blowout Report - Stocktwits；Micron, Sandisk, and SK Hynix: History Says This About the Memory Trio's Rally - The Motley Fool；Micron, Sandisk, and SK Hynix: History Says This About the Memory Trio's Rally - AOL.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.48 | N/A | N/A | 932.97 | 971.00 | -3.92% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.24 | -7.49% | -8.92% | 1,480.77 | 2,335.00 | -36.58% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.37 | +6.48% | +6.75% | 213.05 | 214.72 | -0.78% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.36 | N/A | N/A | 479.18 | 516.10 | -7.15% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.36 | N/A | N/A | 87.48 | 114.68 | -23.72% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 新聞直接提及 | +0.36 | +17.31% | +33.50% | 309.90 | 312.06 | -0.69% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK、SanDisk」，共 5 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [MU, INTC, SNDK: Chip Stocks Rally After-Hours On AMD’s Blowout Report - Stocktwits](https://news.google.com/rss/articles/CBMiygFBVV95cUxPeVlYaXJjQjNtTkNRQUxQTHhaLUFMbE80Uy1MeDBpV0FPdkg2SHRLdkdfVUpXM1NrNWhZSVZQQ01sa0o4T1hKdzF1clBFRlRWUmMwWGxQTDNVVFBpOVhObUc2MXpBeXBOZ0p3R0w5NGRNOHB4X0ZIXzhlT0NMbmhzc1RtdmJRTWhlRUhKSHpyVnpaU0VGMlJyU2tDcmdkTG1hWVJJbmtTVDREbzFfWDB4bjhuTGswN3lmdkdHQzY1dzFOVU41VGlBNlZn?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 25 Aug 2026 01:15:44 GMT
- [Micron, Sandisk, and SK Hynix: History Says This About the Memory Trio's Rally - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxOeWQzZXZ1dVd2Z29RTXRfRUducGRqSDVyYjM4TzA0dDl5LWhUYnBwZUg2VVJOZEJ1VGFFQVBGYUlyd0Q5RTFSckhZeFhCRjk2cVJNUlkxWlQ4Mzl1QVlRZXBPeG16Ump3NE1IemptcFVXQ3BFV0xSSEVzTFFpQ2RPcGhUUG82ZWRBZEhhcGZfZV9ieEVwcnhyWA?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 24 Aug 2026 00:15:00 GMT
- [Micron, Sandisk, and SK Hynix: History Says This About the Memory Trio's Rally - AOL.com](https://news.google.com/rss/articles/CBMigAFBVV95cUxNRFZJaGdYdVhoeVFMRGVvNmN5UF9zQVVGWmhXV0RtRkdTY3hLN1Yyc1g3WDF1Nmx3MVRpQjl3bm9CYzZldGFGSVBkcXNJWFBBUnhnSS1TREU3X3Uyb0paMzF2MXFFSEVRREtQbjZGc3dvcGJ4bVU2bGtNenFyNUNvWg?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 24 Aug 2026 05:13:20 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Nvidia Q2 earnings on deck: Focus on Vera Rubin ramp-up, AI financing (NVDA:NASDAQ) - Seeking Alpha；120 通道自動化對位如何提升 AI 晶片量產良率？ - TechNews 科技新報；資本支出翻倍且現金流驟減，Meta 的 AI 投資回報期何時到來？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.54 | +6.48% | +6.75% | 213.05 | 214.72 | -0.78% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 產業/供應鏈推估 | +0.08 | N/A | N/A | 87.48 | 114.68 | -23.72% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.06 | N/A | N/A | 479.18 | 516.10 | -7.15% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.06 | +1.05% | +0.84% | 2,400.00 | 2,425.00 | -1.03% | 同向 | 86.28 | 27.82 | 467.58B TWD / 44.69% | 2026-08-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | +25.20% | -2.96% | 491.71 | 506.69 | -2.96% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -5.56% | -14.54% | 356.74 | 446.77 | -20.15% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.03 | +0.17% | -1.34% | 591.00 | 680.00 | -13.09% | 未明確 | 13.92 | 42.76 | 73.78B TWD / 43.15% | 2026-08-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.03 | +0.95% | -3.86% | 3,735.00 | 4,310.00 | -13.34% | 未明確 | 60.69 | 61.68 | 48.47B TWD / 12.16% | 2026-08-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVDA」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Nvidia Q2 earnings on deck: Focus on Vera Rubin ramp-up, AI financing (NVDA:NASDAQ) - Seeking Alpha](https://news.google.com/rss/articles/CBMiwgFBVV95cUxPOENpSTJQOWE2OWRaREMxZEI3SjRtR0hUWnIxdm42Nk9SWkpQdDdYT1pOUElYLTI5VkJJd2d3eEoyN0xhSVpVT0kwQ2xYc0dTclprVHhjUGZmc216LXpyTTFhdlRPbm5oa21nRWRoa3h4ZW9PVHZvWC1ONl9xT0JSZi1wdHFEN01IZ09rRFV3NWNydThRYmkwdVZ3aG1TVDdrZ3gzc18yQXlJdkdYWDBFeHo5STFoQWc5bHM5N3B0V1FLZw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 25 Aug 2026 17:21:35 GMT
- [120 通道自動化對位如何提升 AI 晶片量產良率？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMidEFVX3lxTE55azNCYU01REI1c2dmRk5wOTRlTlV1MVltblZ1Q3JkbUNiZTl3MGJLZThtYTg3V2FZZU10YU9JTGdUUXJ1YXJ2djVMc3JiZkxGdEdwT2RXWUhpVy1lNlY3OW5xeHVnU0dRUDgyQ21HUmtLMFlQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 25 Aug 2026 12:33:56 GMT
- [資本支出翻倍且現金流驟減，Meta 的 AI 投資回報期何時到來？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMie0FVX3lxTFBKT0JPbzBrNG5SbDN0c2JINjVJYWkyWnM1dVJ2akVRMUduelFoRUs5VDlkQkJ6MFNxdEUxbU5ySjgtSkZ0VkFGUHAyZTQzMjFoV055SlRmWU5ycjZ3LW9uRDhxVFo1SnRtakxZdVdzTVhpSFhrX0RTWmZUZw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 25 Aug 2026 15:04:09 GMT

## 新興題材：StartupHub

摘要：新興題材：StartupHub 相關新聞集中在：AI Stock Picks Today: MSFT, NVDA, INTC Trade Ideas Aug 25 - StartupHub.ai

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +6.48% | +6.75% | 213.05 | 214.72 | -0.78% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 87.48 | 114.68 | -23.72% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 新聞直接提及 | 0.00 | +25.20% | -2.96% | 491.71 | 506.69 | -2.96% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVDA」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MSFT：新聞直接提及「MSFT」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AI Stock Picks Today: MSFT, NVDA, INTC Trade Ideas Aug 25 - StartupHub.ai](https://news.google.com/rss/articles/CBMijgFBVV95cUxNRFdob1Q1djVlb1B6NlY3MXpULXhfY01NUWo1NUxfOTlYWE1kVlVFekFheTRTTWNmUVZqc3EwRjcyWFgwMEJPNmVjWjQ5YnBMd1luMzNGMGR2U3VkazJqQ3R5c3R1Zmg1QVVoT28zSXNuZ3dsUF9zWWdMX0ItYmdwZzNNa1ZCak1QaUNCenZ3?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 25 Aug 2026 06:00:00 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：台股冷颼颼散熱股卻發燙！奇鋐一日填息、健策飆逾5% 有何底氣？ - 經濟日報；奇鋐陳易成不只追營收、要追獲利！AI液冷讓半年EPS衝44.54元 明年產能再增五成 - 放言Fount Media

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | -1.17% | -2.80% | 2,950.00 | 2,950.00 | 0.00% | 不適用 | 75.13 | 39.32 | 18.59B TWD / 57.39% | 2026-08-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐」，共 2 篇新聞命中。 同時符合主題標籤：thermal。

### 主要來源

- [台股冷颼颼散熱股卻發燙！奇鋐一日填息、健策飆逾5% 有何底氣？ - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE45SDl5QmpUaFV5Mmc0Z1BvR1FBUWxSLXJTZGJwempaa1kyajZxXzhva29fYld3U09PQU12d1hoT0xTMkd6SllLajlDRERjcS14RU9wS3lEVVRGZ9IBX0FVX3lxTFBzLUFFNnpDR0Q0ZlZHa3RBNmhmdmFMZDZIVnNIR3k0akVDdXBMcWV5U29TSjRzR1E2SjF6amhPRzhvOHRwRUgxbnlzWjdiUzJ3VXpUU1VwUVllYkc0QUtV?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 24 Aug 2026 09:00:00 GMT
- [奇鋐陳易成不只追營收、要追獲利！AI液冷讓半年EPS衝44.54元 明年產能再增五成 - 放言Fount Media](https://news.google.com/rss/articles/CBMiUkFVX3lxTE44S3V0cGFHRkoySUpyRmtqV25Db2NPMjBYbnh2NlRmVWNGamI2TjliY3cxYnlPVWhGX1hqOUdZVkp1TUJ4bks0a0o0LVYyNS1SM1E?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 24 Aug 2026 09:42:22 GMT

## 新興題材：台股冷颼颼散熱

摘要：新興題材：台股冷颼颼散熱 相關新聞集中在：台股冷颼颼散熱股卻發燙！奇鋐一日填息、健策飆逾5% 有何底氣？ - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | -1.17% | -2.80% | 2,950.00 | 2,950.00 | 0.00% | 不適用 | 75.13 | 39.32 | 18.59B TWD / 57.39% | 2026-08-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐」，共 1 篇新聞命中。

### 主要來源

- [台股冷颼颼散熱股卻發燙！奇鋐一日填息、健策飆逾5% 有何底氣？ - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE45SDl5QmpUaFV5Mmc0Z1BvR1FBUWxSLXJTZGJwempaa1kyajZxXzhva29fYld3U09PQU12d1hoT0xTMkd6SllLajlDRERjcS14RU9wS3lEVVRGZ9IBX0FVX3lxTFBzLUFFNnpDR0Q0ZlZHa3RBNmhmdmFMZDZIVnNIR3k0akVDdXBMcWV5U29TSjRzR1E2SjF6amhPRzhvOHRwRUgxbnlzWjdiUzJ3VXpUU1VwUVllYkc0QUtV?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 24 Aug 2026 09:00:00 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Semiconductor Stocks Slide Ahead of NVIDIA Earnings: Intel Falls 5%, AMD Slides 4%, Taiwan Semiconductor Slips 3% - Yahoo Finance；國際半導體展9/2登場迎10萬訪客高鐵5站領證串聯科技聚落| 產經 - cna.com.tw；120 通道自動化對位如何提升 AI 晶片量產良率？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.57 | N/A | N/A | 87.48 | 114.68 | -23.72% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | -0.27 | +6.48% | +6.75% | 213.05 | 214.72 | -0.78% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | -0.24 | +1.05% | +0.84% | 2,400.00 | 2,425.00 | -1.03% | 背離 | 86.28 | 27.82 | 467.58B TWD / 44.69% | 2026-08-01 |
| AMD 超微 | 新聞直接提及 | -0.46 | N/A | N/A | 479.18 | 516.10 | -7.15% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2454 聯發科 | 新聞直接提及 | -0.35 | +0.95% | -3.86% | 3,735.00 | 4,310.00 | -13.34% | 未明確 | 60.69 | 61.68 | 48.47B TWD / 12.16% | 2026-08-01 |
| 2303 聯電 | 產業/供應鏈推估 | -0.03 | +8.23% | +5.04% | 125.00 | 164.50 | -24.01% | 背離 | 6.68 | 18.80 | 23.84B TWD / 18.98% | 2026-08-01 |
| MU 美光 | 產業/供應鏈推估 | -0.04 | N/A | N/A | 932.97 | 971.00 | -3.92% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | -0.04 | -7.49% | -8.92% | 1,480.77 | 2,335.00 | -36.58% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel、英特爾」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA、輝達」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「Taiwan Semiconductor」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip, foundry。 方向判斷命中詞：falls。

### 主要來源

- [Semiconductor Stocks Slide Ahead of NVIDIA Earnings: Intel Falls 5%, AMD Slides 4%, Taiwan Semiconductor Slips 3% - Yahoo Finance](https://news.google.com/rss/articles/CBMipwFBVV95cUxOaDBmM0FRUG1yQU9HbC1CQmkycUNUTkp2XzVpY0F6ZW01c2F2RTdxOC1LSHNsMW9weUtDLU9jZVY0aFlBMi1MLXBUV2p3TmFMa2JjMzYtUXhZVHFYVGFDUC1CSVRmRkRBeHRpc0p3ZnowV0xOU1Bqak1kNXdjZm5EZHNBSU90ekdadElkMEprbEJyTVJFVE94N2pMWXpGZ3N0QWNwM1lzVQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 24 Aug 2026 14:43:50 GMT
- [國際半導體展9/2登場迎10萬訪客高鐵5站領證串聯科技聚落| 產經 - cna.com.tw](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1aYnM3bDV4RV9DRndEcjJWOEVCU2poVWdqYzlyM1ZYVklwTHhPaTlwdXlCLTJQUm00V3ZsbG9yM25GdGFkTkc3cWdhMEtqQnNjZmFFN2luMmpxTEk0MGc?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 25 Aug 2026 08:59:00 GMT
- [120 通道自動化對位如何提升 AI 晶片量產良率？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMidEFVX3lxTE55azNCYU01REI1c2dmRk5wOTRlTlV1MVltblZ1Q3JkbUNiZTl3MGJLZThtYTg3V2FZZU10YU9JTGdUUXJ1YXJ2djVMc3JiZkxGdEdwT2RXWUhpVy1lNlY3OW5xeHVnU0dRUDgyQ21HUmtLMFlQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 25 Aug 2026 12:33:56 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》開低走高、收漲407點，月線失而復得- 新聞 - MoneyDJ；《台股盤後》開低走高、收漲407點，月線失而復得-新聞內容-基金 - MoneyDJ；法人專欄分析內容-台股 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》開低走高、收漲407點，月線失而復得- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxOMThHRWpkUXpHVXU2S0hFdzNWQWlZVDRCT0g2OGladFhuYXo2czBTUDVhSjQteE41dDBDYWtVZVRtRlRzVWZVdkJ1bWNPaDM3aWpfZFoyeFlLNDFYck5OQ1gxMURVallTTVg3SUMtS0ZYSkxEYXpndlo2bExEcG9XVWNKSm52ZVQzekpjQ2I3VXo3Zw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 25 Aug 2026 07:49:00 GMT
- [《台股盤後》開低走高、收漲407點，月線失而復得-新聞內容-基金 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxQN0F4SVB1VlBQQTNVMUQ5SE1RUHhtYTc1NzdYZzZ4SjhIVUhxVXhoU1hja0twR2s5VXZSbGNUd3BQdm9NdnU2Z0ppYUJUYVhPYmhwakdKZi0zSXNNWjREdTVpX2VZMjh3eXR3VWlFNjY3MmZZV2RLcjBaY0dUbEwzM042ZU9FblgzN25LMGk4RUU?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 25 Aug 2026 07:54:00 GMT
- [法人專欄分析內容-台股 - MoneyDJ](https://news.google.com/rss/articles/CBMilgFBVV95cUxQUGtWR3hyNzV1SDR1SVF6dlpXOFB6RG5sbXFSdmZ6WnpfZHY3TVc0djNQOHZZbDkyQmwwZXZoOGtDaGJkUUt1cXRseDFUYy1iVWdzbzgzc0FrMXFnd29LUHVmbFRnUGY3UXZ5UzVCRmsxNDF5MzdFaTFZa0VKdm1HRXpFazloSm1GZlpzcFgwNUtxdl82d0E?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 25 Aug 2026 16:07:40 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
