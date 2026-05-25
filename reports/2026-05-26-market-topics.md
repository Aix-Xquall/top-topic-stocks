# 每日股市熱門話題分析 - 2026-05-26

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **AI 伺服器與資料中心**｜正向｜熱度 14｜市場確認 88.33｜同向 5/6
2. **半導體與晶片供應鏈**｜正向｜熱度 7｜市場確認 100.00｜同向 5/5
3. **記憶體與 HBM 供應鏈**｜正向｜熱度 6｜市場確認 93.47｜同向 2/2
4. **關稅與供應鏈轉移**｜中性｜熱度 5｜市場確認 N/A｜同向 0/0
5. **利率與成長股估值**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.23（樣本 13）
- 5日相關係數：-0.31（樣本 13）
- 同向比例：12/13

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| AI 伺服器與資料中心 | 88.33 | 5/6 | 1 | +18.18% | +12.92% |
| 半導體與晶片供應鏈 | 100.00 | 5/5 | 0 | +17.13% | +11.69% |
| 記憶體與 HBM 供應鏈 | 93.47 | 2/2 | 0 | +7.83% | +5.04% |
| 關稅與供應鏈轉移 | N/A | 0/0 | 0 | N/A | N/A |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：BofA | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價呈負相關；應檢查正負向詞庫，並降低新聞直接提及但股價背離的權重。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-05-13 | -0.08 | 0.07 | +58.33% | 12 |
| 2026-05-14 | -0.29 | -0.20 | +50.00% | 6 |
| 2026-05-15 | -0.17 | -0.08 | +58.33% | 12 |
| 2026-05-16 | -0.12 | -0.69 | +33.33% | 12 |
| 2026-05-17 | 0.09 | -0.34 | +40.00% | 15 |
| 2026-05-18 | -0.01 | -0.17 | +33.33% | 9 |
| 2026-05-19 | 0.04 | -0.01 | +62.50% | 8 |
| 2026-05-20 | 0.36 | 0.35 | +28.57% | 7 |
| 2026-05-21 | 0.28 | 0.52 | +45.45% | 11 |
| 2026-05-22 | 0.05 | -0.00 | +33.33% | 15 |
| 2026-05-23 | -0.00 | -0.05 | +84.62% | 13 |
| 2026-05-24 | -0.11 | 0.22 | +86.67% | 15 |
| 2026-05-25 | 0.40 | 0.33 | +50.00% | 10 |
| 2026-05-26 | -0.23 | -0.31 | +92.31% | 13 |

## 歷史回測摘要

- 回測日期：2026-05-26
- 近5日 3日相關：0.43
- 近5日 5日相關：0.52
- 同向比例：+44.44%
- 權重狀態：未調整

- 方向準確度：+44.44%
- 信心排序準確度：0.43
- 診斷：正相關

調整原因：近 5 日有效樣本 9 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：AI 伺服器與資料中心 相關新聞集中在：從百元衝上萬元不是夢？AI 帶動台股熱潮 盤點千金股、萬金股候選人 | 市場焦點 | 證券 - 經濟日報；Nvidia Is Buying Equity In Other AI Stocks, And It Can Be A Long-Term Catalyst - The Motley Fool；The AI chip rally is masking a dangerous truth. Half the S&P 500 is being left behind - MSN

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.72 | +23.47% | +12.66% | 215.33 | 215.33 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.72 | N/A | N/A | 119.84 | 119.84 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.07 | N/A | N/A | 467.51 | 467.51 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.07 | +5.72% | +3.12% | 2,310.00 | 2,310.00 | 0.00% | 同向 | 74.39 | 31.06 | 410.73B TWD / 17.50% | 2026-05-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.03 | -14.93% | -9.08% | 418.57 | 506.69 | -17.39% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.05 | +33.81% | +25.00% | 414.14 | 417.43 | -0.79% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.05 | +29.62% | +20.98% | 617.00 | 617.00 | 0.00% | 同向 | 10.86 | 57.29 | 62.25B TWD / 19.22% | 2026-05-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.05 | +31.42% | +24.85% | 4,245.00 | 4,245.00 | 0.00% | 同向 | 62.91 | 67.65 | 46.74B TWD / -4.14% | 2026-05-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [從百元衝上萬元不是夢？AI 帶動台股熱潮 盤點千金股、萬金股候選人 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxOUjRpbGd0TnFfek1NU0hjQmZmbDlIMVpZcndoYWFKbTRUZzdVNTZiUFktU05YcmRxVzZtSjdIWUNQT0VpRHgtUVFQZjRhTTBSYjlxZ2NfX3c1NXZOSUt3bko3QnRJcUc5U0dmZmt5MWtRcmFteDZfQXl0M0Z3dFYzMA?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 25 May 2026 09:01:51 GMT
- [Nvidia Is Buying Equity In Other AI Stocks, And It Can Be A Long-Term Catalyst - The Motley Fool](https://news.google.com/rss/articles/CBMilwFBVV95cUxQY3lxdTNwaWtsS3ZhV3hUOVlabV9IbjZzNHZkYVRLdHJhZDctbTJqRGd4WHYtT1BtODBzMkdMRV9ZMDF6Y1Y4NWFBOW9aNk1TaTE1cS00bWZ2MjU5YlpvT0haUVUzU2pkZVctZGNoLWZMU19MNzBocUVuSlhpWW1xa3FSZGxNQ3hmVHVjaTVxV1VtMklxMHY0?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 25 May 2026 13:50:00 GMT
- [The AI chip rally is masking a dangerous truth. Half the S&P 500 is being left behind - MSN](https://news.google.com/rss/articles/CBMi9AFBVV95cUxNdjh5dVBNcWlNdHVzMlRUaU4tUkNRcU1iR1VabGhSY3VEblE3MUFaNWtiUVB0Z0tIdE85RXU2cF9XVkxxRU81ZGpCMnpFclUydVBkQzFSNW54S3BKS2FNaFZfZ3pjc3VUTTEwUjJtY1RTZE1naUJoRjVyQ1czRnVhcDlCMGgyYUpzamhROW9Belg2TTJNaFlXdTRzekpnVUZsU0ZhdkkxLXllb3RXRXdIUnVpeW5VMFBIRmtLRGM4TEZjUmZJZVQyMlBpeE5DUUFDSi04MGd3UUlQRVowZnpDdDRZQVpRVXdfVWhRQ0RkTXNlYlJB?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 25 May 2026 00:12:44 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：The AI chip rally is masking a dangerous truth. Half the S&P 500 is being left behind - MSN；美伊協議前景與半導體類股助攻日股收漲| 證券 - 中央社 CNA；華為發表半導體韜定律，拚晶片效能 2031 年達 1.4 奈米 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | +0.65 | +5.72% | +3.12% | 2,310.00 | 2,310.00 | 0.00% | 同向 | 74.39 | 31.06 | 410.73B TWD / 17.50% | 2026-05-01 |
| INTC 英特爾 | 產業/供應鏈推估 | +0.10 | N/A | N/A | 119.84 | 119.84 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2303 聯電 | 產業/供應鏈推估 | +0.06 | +15.74% | +12.61% | 125.00 | 125.00 | 0.00% | 同向 | 4.00 | 31.41 | 22.66B TWD / 10.80% | 2026-05-01 |
| NVDA 輝達 | 產業/供應鏈推估 | +0.05 | +23.47% | +12.66% | 215.33 | 215.33 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.05 | N/A | N/A | 467.51 | 467.51 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | +0.05 | N/A | N/A | 751.00 | 751.00 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.05 | +6.90% | +5.05% | 1,478.69 | 1,562.34 | -5.35% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.05 | +33.81% | +25.00% | 414.14 | 417.43 | -0.79% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip, foundry。 方向判斷命中詞：rally。
- INTC：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 CPU, server CPU, x86, foundry；其中 2 篇新聞出現相關標籤。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 2 篇新聞出現相關標籤。 方向判斷命中詞：rally。

### 主要來源

- [The AI chip rally is masking a dangerous truth. Half the S&P 500 is being left behind - MSN](https://news.google.com/rss/articles/CBMi9AFBVV95cUxNdjh5dVBNcWlNdHVzMlRUaU4tUkNRcU1iR1VabGhSY3VEblE3MUFaNWtiUVB0Z0tIdE85RXU2cF9XVkxxRU81ZGpCMnpFclUydVBkQzFSNW54S3BKS2FNaFZfZ3pjc3VUTTEwUjJtY1RTZE1naUJoRjVyQ1czRnVhcDlCMGgyYUpzamhROW9Belg2TTJNaFlXdTRzekpnVUZsU0ZhdkkxLXllb3RXRXdIUnVpeW5VMFBIRmtLRGM4TEZjUmZJZVQyMlBpeE5DUUFDSi04MGd3UUlQRVowZnpDdDRZQVpRVXdfVWhRQ0RkTXNlYlJB?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 25 May 2026 00:12:44 GMT
- [美伊協議前景與半導體類股助攻日股收漲| 證券 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE5LaTdVOERJaTZ0eF9zRGVYX3Rzc1BkYnYtWExkTWU5MGFrWnFKb0xROTcwemQ0Ry0xLTlrRUZqd0Z6LVdBNGxDaHZUbU9QNzFUOGZveDBoODFZUS0xRGc?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 25 May 2026 07:05:00 GMT
- [華為發表半導體韜定律，拚晶片效能 2031 年達 1.4 奈米 - TechNews 科技新報](https://news.google.com/rss/articles/CBMidkFVX3lxTE1HNzVPTnoyQV9nYnBXTllrMC1tWGplcmJnWHU5TDRQZ01rSEZjX2ZSWjU2SVZIUnRGbGJsaUdhTkVSNVZBUl9kUDJDR1RSanJpX0hoZ3BfYTFYNkhERDdPUkZLdE1PT00tdUdqNVhadFlKWnJBa0E?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 25 May 2026 04:34:44 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Micron vs. SanDisk: Which AI Memory Stock Is the Better Buy? - The Globe and Mail；Micron vs. SanDisk: Which AI Memory Stock Is the Better Buy? - The Motley Fool；Micron vs. Sandisk: Which Memory Stock Wins From the AI Boom? - The Motley Fool

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.76 | N/A | N/A | 751.00 | 751.00 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.76 | +6.90% | +5.05% | 1,478.69 | 1,562.34 | -5.35% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 新聞直接提及 | +0.56 | +8.75% | +5.03% | 261.00 | 261.00 | 0.00% | 同向 | 14.13 | 18.54 | 832.10B TWD / 29.74% | 2026-05-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +23.47% | +12.66% | 215.33 | 215.33 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、memory、美光」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：漲停。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- 2317：新聞直接提及「鴻海」，共 1 篇新聞命中。

### 主要來源

- [Micron vs. SanDisk: Which AI Memory Stock Is the Better Buy? - The Globe and Mail](https://news.google.com/rss/articles/CBMi2gFBVV95cUxPMk9TQThZWVZxWUtUZ0pyazN2X3NMbFhSdS11TUVPUGdtUWVXOVBpREc2MFlCWmd0WkRUcGwyM3BHVDBrUEhrT3lHX3Z3RlkzblpueE83VFNRZzBLSWF5QUxQVml4UU00eGZCRjlKekhINjJ2dzRfMlF3SU9NOGZLSjhxeWtSTXRBcDU1TzFLWkpTeFFUNlFjMXlSTWZjaXRDd3VaS2VFazRYRy0xZmZNV3dsNDJzT0M1dzk3YVVIQk42YUM4Wi1qekpSeldjODBzc1ZuRHNjUDlFdw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 24 May 2026 07:00:00 GMT
- [Micron vs. SanDisk: Which AI Memory Stock Is the Better Buy? - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxNTFo0QXJPZUZ2SzhQLThlZ21HcjNfOTRfeUN2N1lGdTNUX0FqbTJXUHlvWDdwVFF3YmhrS2lHMkM4bzNHdWlqaVdCLVY1c3dnTFZaRWlpMzNLMkI1TGhENVRTbXQ3aGozRm5lY3NDemptaHZGVllBR0gzc2xqNEhaNHVKQ2x1WG1IVVBSTFhqM2phLXVSNURBZg?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 25 May 2026 14:45:00 GMT
- [Micron vs. Sandisk: Which Memory Stock Wins From the AI Boom? - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxObkVqdFVKR29XWlBOUjBHR3RaZlV2YWlKWmFySm1RWDllaGR2Qmw4U29ZUnVCQ0IwZmtiYVp6anRFTWJVQlBXcVI3Q09XazlSQkZjVUVmcjhmcWZIWmtJQXBzQ0FqaVJuYWJJbjVCZFh5Mzc1SXRscEpxb25IQmZ6Y3VydEdzMHpQbjZXTnZfaVZMTzd1NlVfQw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 24 May 2026 20:15:00 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：半導體人才戰！台灣學聯攜手南山中學與亞利桑那大學接軌全球人才供應鏈| 地方亮點 - 中央社 CNA；美國出口管制趨嚴，AI 供應鏈如何落實跨境合規？ - TechNews 科技新報；低軌衛星戰力接棒！「毫米波領航者」稜研科技申請創新板上市，證交所助攻台廠深耕全球國防太空供應鏈，實踐戰略新篇章 - TWSE 臺灣證券交易所

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +10.75% | +53.76% | 308.82 | 308.82 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | +8.75% | +5.03% | 261.00 | 261.00 | 0.00% | 不適用 | 14.13 | 18.54 | 832.10B TWD / 29.74% | 2026-05-01 |

關聯理由（前 3）：
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [半導體人才戰！台灣學聯攜手南山中學與亞利桑那大學接軌全球人才供應鏈| 地方亮點 - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTE85eWVOM1M0NjZPOEJXYlNVYVd3M1lRdzJPcDNEdDVJNlNqNVhLVy1mSk5mQTBTclVNd3g1aWFvc2Z2Y1ZHSE90WnVUNFRnd1BibndlSjVpbjFJV2hheEZv?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 25 May 2026 10:08:00 GMT
- [美國出口管制趨嚴，AI 供應鏈如何落實跨境合規？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiY0FVX3lxTE1aYkZiUWpRVFpqNHNKSVJMcnFiUUt4TGQ1Mm95Rk15bzZGVVBidnpqUFRHZWlxeXk3cjEydGU2b1FvaG5ud0ZWcndXYmkzNWxIb3h0S3lWMmJHSTFxdHNVUVFhWQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 25 May 2026 19:25:31 GMT
- [低軌衛星戰力接棒！「毫米波領航者」稜研科技申請創新板上市，證交所助攻台廠深耕全球國防太空供應鏈，實踐戰略新篇章 - TWSE 臺灣證券交易所](https://news.google.com/rss/articles/CBMinwFBVV95cUxPX2VJVEx4eXJnSDN5bjk3T2c0bEJNS0VESGRtWVNxNFprMTc0eXpESlliTERNZGVmSWdPSTU0YjJtRktzXzB1dmFZNTFhRkNxMDI4NlJ0NW9VaUt6SnlyVVJlUFd5aEdock1Oak1PSG5fZjVNS3hVMkNnd3cxeWxXV1FCSVdrZENPT3RhOXhPYTRXV1NfQzczdjA4My1WTVE?oc=5) - Google News source discovery | TWSE Mon, 25 May 2026 17:21:42 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：市值衝台股第九！國巨本益比飆54倍 明起攜手被動元件族群「關禁閉」 - 經濟日報；特朗普經濟“智囊團”核心成員哈塞特：和平協議達成後油價將大降美聯儲降息窗口將重開作者智通財經 - Investing.com 香港 - 股市報價& 財經新聞

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | -14.93% | -9.08% | 418.57 | 506.69 | -17.39% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [市值衝台股第九！國巨本益比飆54倍 明起攜手被動元件族群「關禁閉」 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE16cmdhazk4aWZLQThjX0pGNlczOGF3b203REg0UzVIT2dFVnJOZlp0ZDUtaHU4TjBPazdGcFloT1ltdmUxRVBfTGw0d0V6MmJMdmsxeFpMejZMd9IBX0FVX3lxTE5Hd0ZHMi1LVHpTbWdRWVdRTllQNlRGRm9jd0hCdXYwdXppNXRxdjlVeE9fWFNmOVNxMnNPal83Y3NOSmhMM01vVDBub0VuRTlRVi12bURReGVXQzJRTmRR?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 24 May 2026 09:00:00 GMT
- [特朗普經濟“智囊團”核心成員哈塞特：和平協議達成後油價將大降美聯儲降息窗口將重開作者智通財經 - Investing.com 香港 - 股市報價& 財經新聞](https://news.google.com/rss/articles/CBMicEFVX3lxTFB3c3EyTjJ0ektZR043Tm9CbVhmd0dDVDI4UnVOQjJjcmJtcnRzc295T1dKZl9zMjdEOFFvLXctQmpFSFJ0eml4dm9PazFPbUZheUJoVU5YZldLUm1iQ2MzRFhYQm1tdVdoZW9HWk1GZ2o?oc=5) - Google News source discovery | Investing.com Calendar Mon, 25 May 2026 02:20:05 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：輝達Vera Rubin點火！這「散熱大廠」液冷商機爆發 第二季EPS估達22.79元 - Yahoo股市

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | +10.04% | +6.85% | 2,575.00 | 2,835.00 | -9.17% | 不適用 | 61.06 | 42.31 | 15.63B TWD / 71.62% | 2026-05-01 |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +23.47% | +12.66% | 215.33 | 215.33 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 1 篇新聞命中。 同時符合主題標籤：thermal。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [輝達Vera Rubin點火！這「散熱大廠」液冷商機爆發 第二季EPS估達22.79元 - Yahoo股市](https://news.google.com/rss/articles/CBMioAJBVV95cUxOVTFFWUJsZVBsR1RQZVU5anZUNlBTVGpuNjV6MW91OGVHNnZ4cEZKdE9sZFc3VV9iby1UV01odmozVmQxaXBYdVR6bGJUTEtUdER1RjRwbHdHT3RVeGNvX05fcVJDLUNDR1UwUm1CRGZqdHllU3RBYU56SXMwSEwtb0NQTVZqb2xkbDR1TXBaaUgtc1lnbE5zYmNvQ3hJWHRMc3dOZ29RSHhBRmhJTC0tQnlkU0tyU01WcGZqSENYWlVlckFFU05zclNvNFk4RDY0NG9QakhiWmNzblVDV2tXLThvaTlWZXNlMFdTZzEyUk9jVS1FZVNZemxUUEhCY1d3MkEzdk5aaExBQ3ZuSzFTU1gwYU5WWWNSRFNadnc3VGo?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 24 May 2026 09:15:00 GMT

## 新興題材：BofA

摘要：新興題材：BofA 相關新聞集中在：BofA’s Vivek Arya Sees Nvidia at $350 as Agentic AI Drives an “Unprecedented” Chip Cycle - 24/7 Wall St.

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +23.47% | +12.66% | 215.33 | 215.33 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [BofA’s Vivek Arya Sees Nvidia at $350 as Agentic AI Drives an “Unprecedented” Chip Cycle - 24/7 Wall St.](https://news.google.com/rss/articles/CBMixwFBVV95cUxPbjYzaUl1NmpBMlI2SFN1aEN5S0FEMWdZNlZTbVBrM3A5MWFUZElyY3FrYTJkaUVtaFJXSmp0RUJ1bkotYkRsWFVwaHdsMC1sNHVxSGtnY0dtODYxZjdmVVNHTnAwMlhkWm1rX09JLVlIQ1FxNG9hM3dtdlFvSjI3Y3RIQXJaYWN2aDBnRHphRllrYnlhTDRVeXBWTnJQVTN0WUZrdUF5dGJIaTJ5eEctZnNoemM4M2twRTRpMXpBWG5HblpXWWdV?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 25 May 2026 11:30:34 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：《台股盤後》開高走高、飆漲1376點，首收43K - MoneyDJ理財網；台股再衝新高 台幣早盤爆量強升1.52角 - MoneyDJ理財網；《金屬》LME休市 COMEX黃金電子盤上漲0.9%-台股 - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》開高走高、飆漲1376點，首收43K - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikgFBVV95cUxPMHhhZXQzOVZmMnlCQ0NVcUp4ZkxORGVZdUFicnpXZkV1T0VXeUdiSTdVd3VhZThCeFRtVjY1d3Y2dnowM2pia3JiRWZGTDZmVzM5VlR5Y1JENmVTazYzakx2ZmtsYnZZd1c3LUk2My1Gck53QU9hcVBRY1BnajBMUXB2aDJIUEh4ejdSYk1IT21iUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 25 May 2026 08:02:00 GMT
- [台股再衝新高 台幣早盤爆量強升1.52角 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikgFBVV95cUxOTnFWUlVEamJ0RFZ4OENFLVJnQk5SaVdYcG9NLXR1dE0xeGI5aDZ5SzBEVmYxaG9RMVVQMXpQWEhxS3RSQVM2QXZoZVg1NnM5a01UQkI4MTlnME1XSGd1R2w4NlB6TkRDTGdfMkJaV1NIcXhWZHdEdEwxeFU4Mk9rSVlXNVlRR2p0VFA3MmFfc3IzZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 25 May 2026 04:23:00 GMT
- [《金屬》LME休市 COMEX黃金電子盤上漲0.9%-台股 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMiigFBVV95cUxNQlRPWEY3dzJ0dm5yOGFkVWw5Y3k3Z1cwakZqTmdFc1Q0WVdnQkxaVloxUnVLVjh4OG1CWXBUNFgxX1VTZF82cFRKTWJ5bG5FSUJ4OUNNU1A0eVpBdFVTRlRrUXRYTGROaWVSWkZrRU5oWDc1Q0dKaDJaV1A0NF9XeWRDTGxQNmMzc1E?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 25 May 2026 22:16:44 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
