# 每日股市熱門話題分析 - 2026-10-04

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **AI 伺服器與資料中心**｜正向｜熱度 17｜市場確認 70.99｜同向 6/8
2. **記憶體與 HBM 供應鏈**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
3. **半導體與晶片供應鏈**｜正向｜熱度 9｜市場確認 69.42｜同向 6/8
4. **新興題材：為什麼需要液冷**｜正向｜熱度 1｜市場確認 80.72｜同向 2/2
5. **散熱與液冷供應鏈**｜正向｜熱度 2｜市場確認 80.72｜同向 2/2

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.12（樣本 20）
- 5日相關係數：0.70（樣本 15）
- 同向比例：16/20

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| AI 伺服器與資料中心 | 70.99 | 6/8 | 1 | +6.16% | +2.41% |
| 記憶體與 HBM 供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | 69.42 | 6/8 | 1 | +5.64% | +1.72% |
| 新興題材：為什麼需要液冷 | 80.72 | 2/2 | 0 | +3.58% | +8.03% |
| 散熱與液冷供應鏈 | 80.72 | 2/2 | 0 | +3.58% | +8.03% |
| 新興題材：TradingKey | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價呈負相關；應檢查正負向詞庫，並降低新聞直接提及但股價背離的權重。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-09-21 | -0.15 | -0.05 | +61.54% | 13 |
| 2026-09-22 | -0.00 | -0.01 | +88.24% | 17 |
| 2026-09-23 | 0.35 | 0.22 | +80.95% | 21 |
| 2026-09-24 | 0.05 | 0.42 | +90.00% | 10 |
| 2026-09-25 | -0.31 | 0.15 | +30.77% | 13 |
| 2026-09-26 | 0.22 | 0.14 | +63.64% | 11 |
| 2026-09-27 | 0.11 | -0.14 | +57.14% | 14 |
| 2026-09-28 | 0.05 | -0.53 | +63.64% | 11 |
| 2026-09-29 | 0.31 | -0.78 | +16.67% | 6 |
| 2026-09-30 | 0.05 | 0.04 | +33.33% | 18 |
| 2026-10-01 | 0.21 | -0.27 | +40.00% | 20 |
| 2026-10-02 | 0.51 | 0.37 | +72.73% | 11 |
| 2026-10-03 | -0.35 | 0.13 | +16.67% | 6 |
| 2026-10-04 | -0.12 | 0.70 | +80.00% | 20 |

## 歷史回測摘要

- 回測日期：2026-10-04
- 近5日 3日相關：-0.07
- 近5日 5日相關：0.11
- 同向比例：+72.00%
- 權重狀態：已調整

- 方向準確度：+72.00%
- 信心排序準確度：-0.07
- 診斷：信心校準問題

調整原因：近 5 日方向判斷多數同向，但信心分數與後續報酬呈負相關；判定為信心校準問題，優先降低高信心膨脹、寬題材推估與背離容忍。；關鍵詞×公司後續樣本有效 4 筆，未達 30 筆，不調整樣本權重

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

摘要：AI 伺服器與資料中心 相關新聞集中在：AI 鏈、金融、台塑四寶 搶鏡 - 經濟日報；股海自由行／資安、 CPU 、設備股 動能強勁 | 證券達人 | 證券 - 經濟日報；Intel vs. Marvell Technology: Which AI Chip Stock Is a Better Buy in 2026? - The Motley Fool

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.57 | +4.05% | N/A | 119.33 | 119.33 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.54 | +5.97% | +16.92% | 233.95 | 233.95 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.06 | +22.83% | N/A | 633.91 | 633.91 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.06 | +1.01% | 0.00% | 2,500.00 | 2,500.00 | 0.00% | 同向 | 86.28 | 28.98 | 514.81B TWD / 53.32% | 2026-09-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | +14.95% | +5.19% | 517.53 | 517.53 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -4.10% | -5.99% | 355.14 | 446.77 | -20.51% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.04 | +3.78% | +2.89% | 713.00 | 713.00 | 0.00% | 同向 | 13.92 | 51.59 | 82.25B TWD / 45.66% | 2026-09-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.03 | +0.81% | -4.53% | 4,950.00 | 4,950.00 | 0.00% | 未明確 | 60.69 | 81.75 | 64.18B TWD / 44.08% | 2026-09-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel、INTC」，共 2 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：強勁。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 4 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AI 鏈、金融、台塑四寶 搶鏡 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxQM09QQWYxTTRXY2haMTNfQ05UdnhUal9PdGZwUG1SQWg1b0FTX2hIemhRRGktSzJ2ZGZvQ1E4R2xWQkQ2ZDd6SFpYMkQycHQ5Z09TdG1yV09KTGp1cEdqTWRHcS1kbU9ZSllYR3o4MHM0U1IwZFhZZWQyUWJSSERrcNIBX0FVX3lxTE5icWRlZUc5ZWc3S18zUkFsd19oWFh4NEpsWHNYRkxuVktBbzZnT18wMFlQT21XUl9aWFdtZnhvMDdUUm9xX3FrekNxNXRqdExyeC01LU1rS0N3ZEQ0VWNz?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 03 Oct 2026 18:24:45 GMT
- [股海自由行／資安、 CPU 、設備股 動能強勁 | 證券達人 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMifEFVX3lxTE9rNTdCSkpWSE80aHgtNG00QVc5eWpKMUllOXFEcU9tREluWTVIVFY2aW85SHMzeE9sNXhJbUlpaTJnUjg0TG12bUpQNkh4RU9ycXFMa2d3UzFSVFEtQ090a3lXekpDX0ZDdW9GdE5zY1R3M25id3JJWDFWOGI?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 03 Oct 2026 18:05:04 GMT
- [Intel vs. Marvell Technology: Which AI Chip Stock Is a Better Buy in 2026? - The Motley Fool](https://news.google.com/rss/articles/CBMitwFBVV95cUxOazlxeU5JVWlQLXdQRGdQUm5pYXFGaGpNWHNiX1VYbVhFR1RSVkY4Uk55WHdzMTRHbXQyNlRrVkE3UFJRYVA2ZjNQWDkyRGVhREltMndiMnhUeDVnQjRVbnhfQ3dPeklkSmhSUmRGeE9KZmhnb0xkWlJZS3d6ZkViYktVMmhMSEk2TUp0ckVnaU5jVy1LUWlXQnNhWm1jSWlMUC1oRkE5VUx4V05kRUlneS0yZGgtWTQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 03 Oct 2026 13:45:00 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Long-Term Agreements Don’t Protect the Memory Makers the Way You Think - inkl；美光等記憶體突遭血洗 背後兇手竟是它！南亞科、華邦電下周慘了？ - Yahoo股市

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | +10.70% | N/A | 1,074.89 | 1,074.89 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -0.56% | -3.25% | 1,719.99 | 2,335.00 | -26.34% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +5.97% | +16.92% | 233.95 | 233.95 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「memory、美光」，共 2 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 NAND, SSD, flash memory, memory；其中 1 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Long-Term Agreements Don’t Protect the Memory Makers the Way You Think - inkl](https://news.google.com/rss/articles/CBMimwFBVV95cUxPbjBtaFFCZ3lWUjkya01mR3M5T3pkY1EwbVRwZ2hFQ1djRnZ0UFFhVzZLbVRwazZrc2RlZXBSVGllT21WbHJCYWJId1FZcXhhREtJSl84UWFHSUt0VngwRlYzaVVpTUd5Tlhld0JLNmRySGZHbDBLUTNGUTZHRm81SVBnaWZ1Tmw4eG9XcUtGWnZPdHZLS052N1Nhbw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 02 Oct 2026 14:27:17 GMT
- [美光等記憶體突遭血洗 背後兇手竟是它！南亞科、華邦電下周慘了？ - Yahoo股市](https://news.google.com/rss/articles/CBMirwNBVV95cUxQWG12Tk9jWjZkdXcyRWYxMDhvYVFPTGJMU1Npd3g3dGRheV9SeXhoRlBNTHJZYVFVeEhKZU9VdWthMldHM3BXSDdmemJ6SlRXODloSUNyaFRkMlVtTEZ3SVFpQVFhMlVrUENEX0szNFZUdHYxTGNFYl9VejF2ZnFrZDNRalpfU0tMdWpTeXlDZS1ST1lCT0J1UmNSTW4zTWczNXBFV0hlcnp1V2N1SW9iSE9peWg1d2xmbWhFTDdCcDlUeE9jQzczVHd1MzZQaUw3RXhjVFpEaE1wOEx2c2hXb3BEVERXbGpHOFFFWkFJQi1PRmR0ZTJQVlUtbkxZd1lYb1BOd1owY3M3WmVHVkYwY2k4THVqRndacjVZTTl5clkxLVB0b2ZORjRBVXNwMHRnbTN2VVRUTm5hZFF2MDRlci1zcGlHNlhWUzNuekcxVEdBQ3pGcmVGZllJeEVYUFRKdkZNdnYtN1A2b29FMFVFWlViRFZqNW04YTBWaHNsV01jMFAxcE5FUHR2WVNQOTZvSnJVVlkycnVETnRJRUZ2dDlJeGZ4d0JheVI0dVI1dw?oc=5) - Google News source discovery | Yahoo 奇摩股市 Sat, 03 Oct 2026 04:49:07 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：股海自由行／資安、 CPU 、設備股 動能強勁 | 證券達人 | 證券 - 經濟日報；Intel vs. Marvell Technology: Which AI Chip Stock Is a Better Buy in 2026? - The Motley Fool；The AI Chip Revolution Wouldn’t Be Possible Without This Company - 24/7 Wall St.

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.54 | +4.05% | N/A | 119.33 | 119.33 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.49 | +5.97% | +16.92% | 233.95 | 233.95 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.05 | +1.01% | 0.00% | 2,500.00 | 2,500.00 | 0.00% | 同向 | 86.28 | 28.98 | 514.81B TWD / 53.32% | 2026-09-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.05 | +5.21% | +0.94% | 161.50 | 164.50 | -1.82% | 同向 | 6.68 | 24.29 | 25.04B TWD / 30.71% | 2026-09-01 |
| AMD 超微 | 產業/供應鏈推估 | +0.04 | +22.83% | N/A | 633.91 | 633.91 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | +0.04 | +10.70% | N/A | 1,074.89 | 1,074.89 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.03 | -0.56% | -3.25% | 1,719.99 | 2,335.00 | -26.34% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -4.10% | -5.99% | 355.14 | 446.77 | -20.51% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：強勁。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 3 篇新聞出現相關標籤。

### 主要來源

- [股海自由行／資安、 CPU 、設備股 動能強勁 | 證券達人 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMifEFVX3lxTE9rNTdCSkpWSE80aHgtNG00QVc5eWpKMUllOXFEcU9tREluWTVIVFY2aW85SHMzeE9sNXhJbUlpaTJnUjg0TG12bUpQNkh4RU9ycXFMa2d3UzFSVFEtQ090a3lXekpDX0ZDdW9GdE5zY1R3M25id3JJWDFWOGI?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 03 Oct 2026 18:05:04 GMT
- [Intel vs. Marvell Technology: Which AI Chip Stock Is a Better Buy in 2026? - The Motley Fool](https://news.google.com/rss/articles/CBMitwFBVV95cUxOazlxeU5JVWlQLXdQRGdQUm5pYXFGaGpNWHNiX1VYbVhFR1RSVkY4Uk55WHdzMTRHbXQyNlRrVkE3UFJRYVA2ZjNQWDkyRGVhREltMndiMnhUeDVnQjRVbnhfQ3dPeklkSmhSUmRGeE9KZmhnb0xkWlJZS3d6ZkViYktVMmhMSEk2TUp0ckVnaU5jVy1LUWlXQnNhWm1jSWlMUC1oRkE5VUx4V05kRUlneS0yZGgtWTQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 03 Oct 2026 13:45:00 GMT
- [The AI Chip Revolution Wouldn’t Be Possible Without This Company - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiqwFBVV95cUxQczRsRVU3dGhZN2JwdEJWOUtTMkZ4djRzVEh5cFVyeWk2OHN0X052RmRwYmJoUnAtVklaNTVJRkRJZzF2Rk9Zem5zbFV4aTdrREhWWnpNT05xN2VnZU1xenBjYlNNZjZFUWZZWmRtTTJmcGxPZUV3a0RzeW8xVkw3OUkxbnhUbTdHU1FSVHdHbmY5TjRYZ3B0SFNoU05yX3BhSGMyRWFRZW1HRUk?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 03 Oct 2026 15:30:00 GMT

## 新興題材：為什麼需要液冷

摘要：新興題材：為什麼需要液冷 相關新聞集中在：NVIDIA Vera Rubin 為什麼需要液冷？AI 散熱需求爆發，散熱股都會受惠嗎？-實習大人-林序安 - CMoney投資網誌

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.42 | +5.97% | +16.92% | 233.95 | 233.95 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3017 奇鋐 | 新聞直接提及 | +0.42 | +1.18% | -0.86% | 3,440.00 | 3,440.00 | 0.00% | 同向 | 75.13 | 45.85 | 19.48B TWD / 54.34% | 2026-09-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 方向判斷命中詞：受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 3017：新聞直接提及「散熱」，共 1 篇新聞命中。 方向判斷命中詞：受惠。

### 主要來源

- [NVIDIA Vera Rubin 為什麼需要液冷？AI 散熱需求爆發，散熱股都會受惠嗎？-實習大人-林序安 - CMoney投資網誌](https://news.google.com/rss/articles/CBMihwFBVV95cUxOUlVqWXU3REtfc2lQdDF6alJWZzZaQ0RnTm13ZGRDbkRvSG1Gdmg3b3Zna0JJcy1RTzhCZDNJVEVDSXVjRE1hSlRzZGt4WDh0bHROUTQxbDZoSm8zSzZ5bk1wSHVCeVNYNXh2WmZHY2FZS2RnbnliYnpUX1g1Tml1SjExWGV0U0U?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 02 Oct 2026 01:43:41 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：NVIDIA Vera Rubin 為什麼需要液冷？AI 散熱需求爆發，散熱股都會受惠嗎？-實習大人-林序安 - CMoney投資網誌；從安全氣囊做到 AI 散熱，時碩工業憑 20 年精密加工奪古河液冷大單 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.51 | +1.18% | -0.86% | 3,440.00 | 3,440.00 | 0.00% | 同向 | 75.13 | 45.85 | 19.48B TWD / 54.34% | 2026-09-01 |
| NVDA 輝達 | 新聞直接提及 | +0.42 | +5.97% | +16.92% | 233.95 | 233.95 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 2 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：受惠。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 方向判斷命中詞：受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [NVIDIA Vera Rubin 為什麼需要液冷？AI 散熱需求爆發，散熱股都會受惠嗎？-實習大人-林序安 - CMoney投資網誌](https://news.google.com/rss/articles/CBMihwFBVV95cUxOUlVqWXU3REtfc2lQdDF6alJWZzZaQ0RnTm13ZGRDbkRvSG1Gdmg3b3Zna0JJcy1RTzhCZDNJVEVDSXVjRE1hSlRzZGt4WDh0bHROUTQxbDZoSm8zSzZ5bk1wSHVCeVNYNXh2WmZHY2FZS2RnbnliYnpUX1g1Tml1SjExWGV0U0U?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 02 Oct 2026 01:43:41 GMT
- [從安全氣囊做到 AI 散熱，時碩工業憑 20 年精密加工奪古河液冷大單 - TechNews 科技新報](https://news.google.com/rss/articles/CBMioAFBVV95cUxQYlpYVTNmbDNNVXUyMnpJWE5BM0NyUjZ2ZmpVcGN2aEgwX2FqZlFEckpROV9Ebks1clpLSlA0UFJMd0gzVVBiZmw3aFJDS3JyV2lBc2tMRnBWN3cxZk4tQ3NVTFNQeEE1d3ZydmJzbXZDaldWUGxyYVAxR0V3OF9yUEZoZ3ctUFAzc2VUU1ZQNGJObWRyZUZKcS1nOVEyTHVy?oc=5) - Google News source discovery | TechNews 科技新報 Sun, 04 Oct 2026 00:00:59 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Why Is Intel (INTC) Stock Volatile After Earnings? Revenue Beat Overshadowed by $11 Billion Loss - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | +4.05% | N/A | 119.33 | 119.33 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Why Is Intel (INTC) Stock Volatile After Earnings? Revenue Beat Overshadowed by $11 Billion Loss - TradingKey](https://news.google.com/rss/articles/CBMiyAFBVV95cUxPdGVhdUdOWHYwd0I2OHRLRjlFVE9KTkNud09aOHhCOTZGY2NDZVM4VjFnTTZKdkpKdlBORHo1OG5RWENLVFg4VUZoYVdVWVRpaWFCSWtxY2dHX280ZFFsaDlvSldKQm9NdTdWTjlueks4V3V3RUVJQ2pqYVFtNi0xVU9zY2V3MGdONjRFaHJqU1RRaVZZMm9GZndlNVRSaWpveDlMWG41WG5qUk52T0tRcGl1bklGZ2twMmQyQnJxdkM0YzU1d1J2Wg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 03 Oct 2026 11:52:09 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台指期夜盤飆破4萬9！ 專家估：台股10月中可站上5萬 - MoneyDJ理財網；台股擂台 第3季「低調黑馬」陳奇琛賺26% - 經濟日報；台股擂台Q4賽前戰報 | 台股擂台 | 證券 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台指期夜盤飆破4萬9！ 專家估：台股10月中可站上5萬 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikgFBVV95cUxNTmtTRjJTTXJmenEwN0kzN3pkel9hdkxkdjE0UEJqeWh2dmlKSHBObmY4U2xPWDdhMnV6azBTRmxrUFJGN1drVWYwOEdvQUxCYm9BTzBmRFA5U2RGbFlFVk9tS3k1cnRLd2I5Y0FyRHZ1c2VfeEtBUElSSzNFX3l0MmxTcTNjbmowQW9tWnppc0FNdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 03 Oct 2026 06:12:00 GMT
- [台股擂台 第3季「低調黑馬」陳奇琛賺26% - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBrRnA1ZkpQOC1XSlBGUE9DaC1NU19Dc3Q5UURDeXdJRUd4cmNzcld6OUVRcVp3WENSMGpXeXhBdE4wZ0dyaGhMQTRJdjh2VEwxNmpMUExXU3N4Z9IBX0FVX3lxTFBtdkh2QUl0UGpMdzNoUDRHcURCQXRKb1dZOENHRkJsR0w2Q2FIZHZMclBsTEFFM1gxN0ZIR2ZoM3VDUTdMYVh6N2kwR1dEaUd6RGR2RTRKd2ZmY3pvYWZZ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 03 Oct 2026 17:56:32 GMT
- [台股擂台Q4賽前戰報 | 台股擂台 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTE9rSWRIZzFfeEFkdTRSVFZObHVESVlBS1ZUWm1qeTFpS3FjY25LZzdSemZncjh5a0laT0tKdmVsOGk4UjFYam5uWjZZcVJkdlo2RHhHX1FqVUpydXVF?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 03 Oct 2026 16:38:02 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：個股動態報導內容-33839053-108E-48E1-8983-C10C3C12E6B8 - MoneyDJ；個股動態報導內容-9E2D03CC-EA86-401C-B0D8-5CCBCC8B905B - MoneyDJ；個股動態報導內容-3C0416A1-6C2F-4013-BB5E-7200F6D94469 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-33839053-108E-48E1-8983-C10C3C12E6B8 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxQcjMwcUZqSWJhZDN6SFRKNnVOZlF5cjBmbmpiYVZlRVhsa2NzZE01bDRHUm94RXBGZ1dSWGo5blUzT0VMS0dkbEozbzFGX1Mzel9qLThPNFNGVy1zVjI3Y3hiYUh3QkVjbDFOeU9BNTdTdmNTSjYxaHQ4UW5LSi1zaW1aY0JOM3FHcHhCaUpmQTRiOW5J?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 03 Oct 2026 04:24:01 GMT
- [個股動態報導內容-9E2D03CC-EA86-401C-B0D8-5CCBCC8B905B - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxPRUdfLUVQVTI2MmVxR0lhcUhmWkVDZk5mckdXNERPdXlzR1FHeGtIY0MyMlJCblFaTDZ2b1JDZVF6MjM5QjhXS0pMbFloSERLak53bmNpeUw2bHJnZDJCRG83YUpxSkg5Zms5aGhhWEZzc0UxcThUSFNhWTBrV3ppRlJTVEtPLXlRcDNFbFlsMlNSRHdy?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 02 Oct 2026 20:51:57 GMT
- [個股動態報導內容-3C0416A1-6C2F-4013-BB5E-7200F6D94469 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxOT1NMMU54SUhEWTdrQjkzSzFhUGVSOGhCNjF6eHRuRTZGVWtGUVJYTnFkWG5kbnVsUWdFZGhmemtfaTJzQkZqVzJnV05HWG9GRU5ydUhzS1hoR1RxY1lxcm03RmZQREV5S2ZyOFVvTUh1blNBNWY2dlFqX3U1bm95bGgxWXdSdUtXSGhaam1MT25JYzJQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 02 Oct 2026 16:43:42 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
