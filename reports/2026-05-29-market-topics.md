# 每日股市熱門話題分析 - 2026-05-29

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **AI 伺服器與資料中心**｜正向｜熱度 10｜市場確認 76.67｜同向 4/6
2. **記憶體與 HBM 供應鏈**｜正向｜熱度 3｜市場確認 100.00｜同向 1/1
3. **關稅與供應鏈轉移**｜中性｜熱度 4｜市場確認 N/A｜同向 0/0
4. **半導體與晶片供應鏈**｜中性｜熱度 6｜市場確認 N/A｜同向 0/0
5. **散熱與液冷供應鏈**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.14（樣本 7）
- 5日相關係數：-0.04（樣本 7）
- 同向比例：5/7

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| AI 伺服器與資料中心 | 76.67 | 4/6 | 1 | +11.22% | +10.36% |
| 記憶體與 HBM 供應鏈 | 100.00 | 1/1 | 0 | +11.02% | +17.89% |
| 關稅與供應鏈轉移 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：TradingKey | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
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
| 2026-05-27 | -0.07 | -0.07 | +87.50% | 8 |
| 2026-05-28 | 0.14 | -0.07 | +88.89% | 9 |
| 2026-05-29 | 0.14 | -0.04 | +71.43% | 7 |

## 歷史回測摘要

- 回測日期：2026-05-29
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

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：台股市值全球第五，大摩估 2027 年 AI 半導體市場增 60% - TechNews 科技新報；硬體更新加速，Figure AI 最新系列作 Figure 04 定版邁向量產新紀元 - TechNews 科技新報；年輕人論壇靠 AI「轉大人」，Dcard 成立企業 AI Agent 事業 GNTC - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| TSLA 特斯拉 | 新聞直接提及 | +0.56 | +18.92% | +2.72% | 442.10 | 456.56 | -3.17% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 產業/供應鏈推估 | +0.10 | N/A | N/A | 120.89 | 121.77 | -0.72% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.08 | +22.85% | +12.10% | 214.25 | 214.25 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.07 | N/A | N/A | 518.09 | 518.09 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.05 | -0.65% | +2.91% | 2,295.00 | 2,300.00 | -0.22% | 未明確 | 74.39 | 30.86 | 410.73B TWD / 17.50% | 2026-05-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.03 | -13.22% | -7.25% | 426.99 | 506.69 | -15.73% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.05 | +37.82% | +28.76% | 426.58 | 426.58 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.05 | +1.62% | +22.94% | 627.00 | 642.00 | -2.34% | 同向 | 10.86 | 58.22 | 62.25B TWD / 19.22% | 2026-05-01 |

關聯理由（前 3）：
- TSLA：新聞直接提及「Tesla」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [台股市值全球第五，大摩估 2027 年 AI 半導體市場增 60% - TechNews 科技新報](https://news.google.com/rss/articles/CBMixAFBVV95cUxObjBlRmxSXzlNYzZOMnRhRG5PWE83ZnNZclNEWHlRZHI3djg1b0xNYkN3S2tzUktmODJEYWJFMEhpa2ZDVmRqOGRFNXNoVVNPVUMxVGRiOTgtQ0Vleks2cGY4M0YtRy1vRWk0Nlo5Tl9fcTNNUFA5aGllTy1RVXpCWGUtd3hqLWQ4dFlkTl9hVEc0RHRYYWJ5UVNZd1Zkd2E0N2czTjB6dHBzWUdvN185VHFEZjdQRkU2cWZTWWZ5eENkLTdl?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 27 May 2026 07:00:00 GMT
- [硬體更新加速，Figure AI 最新系列作 Figure 04 定版邁向量產新紀元 - TechNews 科技新報](https://news.google.com/rss/articles/CBMirAFBVV95cUxNcFNXMUp3RFB4VWlGcU4tZzJrTDFvbHhmNzl3dXpiUmVDWDZEVjhFdjRpaGdJQ2U4QU9NQUM0ZHRxcmt2ektlQTkzZG8wZ2p6bWFLM2pLNG1nUkdTMjhPTnJTbEFZMTVTcWxNOUJpT0ljLWxIOEstT0lobmtzZ1d0TGc5ay1UNzY5TXdFbFhPc0pZZEluUkZON09vWll5V2x5S3NycnRQeXo3ei1R?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 28 May 2026 23:03:58 GMT
- [年輕人論壇靠 AI「轉大人」，Dcard 成立企業 AI Agent 事業 GNTC - TechNews 科技新報](https://news.google.com/rss/articles/CBMia0FVX3lxTFBIcU5qUTYxYV96Z2JUNEJERjFkTFJxeWRqczFvenNpejU3cmNWc0Y1amJRT0ZUX21RVTNVbnpLNkVQd053eHA1R2NEeVFBSjNPdDhuZ2k0UEdfVTgzbHh4TVhDZ1h1VHlHa1kw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 28 May 2026 03:15:45 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Micron, Sandisk Get Mizuho Target Hikes on AI Memory Boom - Gotrade；Micron Technology Inc Stock (MU) Opened Up by 4.75% on May 27: Drivers Behind the Movement - TradingKey；台股創高後翻黑跌620點失守44K 汽零股吃補 這檔記憶體暴量連6揚 - 工商時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.76 | N/A | N/A | 923.52 | 928.41 | -0.53% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.65 | +11.02% | +17.89% | 1,641.64 | 1,641.64 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +22.85% | +12.10% | 214.25 | 214.25 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、MU」，共 2 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 1 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Micron, Sandisk Get Mizuho Target Hikes on AI Memory Boom - Gotrade](https://news.google.com/rss/articles/CBMijwFBVV95cUxNeV8tVnJ4WTQxLWs1ejlLMFJfS0h5NU1WenNRcDIwaWlSMElyUXFablJsTkJxTms2dzQySTluOFItUHI5ZTFpQ29sNVhfUjdzbVBlZEJOR0wzU0M1ZjFrLVR3ODRLVlRyX1JreWdKRjlyMDFYdVpCaGRod2FaM2ZkdzVGWE5qZ0VxMDIzbk5aZw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 28 May 2026 16:58:41 GMT
- [Micron Technology Inc Stock (MU) Opened Up by 4.75% on May 27: Drivers Behind the Movement - TradingKey](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPTkpaRHVlZEF0ekpkZFVlcHo1aU83RDViYVFZNWNLNmRXejJFaVlMS2xDZlRIaGN2clFNaGdKZ3VtVTVSZ2FPbkV5bmp0MjlCLXZGYTY1VnJGMkI0UjVpSUlMUEdnYkVlaXpaSjc5SUdCOHlYVVVEZWllZlhkWTZwQ1NuSTBVX0FW?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 27 May 2026 13:47:29 GMT
- [台股創高後翻黑跌620點失守44K 汽零股吃補 這檔記憶體暴量連6揚 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5nUEVILXZkcGxFN1NhUWZpWDA0WTZGZ1pBcmZWUGJnMDJUaHV2N2JLclhlSGZTNjNhVkdRQWZCeDA5N1kxRmp3WlNGa0JzZFpQdmNyWExfY1JCSklKUnVj?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 28 May 2026 06:00:00 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：美對台灣非半導體232關稅優惠上路 汽車零組件稅率15% - 中央社 CNA；232半導體關稅公布前鄭麗君：盼考量台美長期夥伴- 日報 - 工商時報；黃仁勳兆元宴大咖雲集，台 AI 供應鏈重量級掌門人齊聚 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +12.07% | +55.59% | 312.51 | 312.51 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | +0.77% | +6.26% | 263.00 | 264.00 | -0.38% | 不適用 | 14.13 | 18.68 | 832.10B TWD / 29.74% | 2026-05-01 |

關聯理由（前 3）：
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [美對台灣非半導體232關稅優惠上路 汽車零組件稅率15% - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBSelEwcXpNRVNvM0lHbDd0VlV5akZJZUFmSEpobl9XV0xwc3VJZjBZZkU2TnRsMjR2ZVY4WlluLWQ2NklhZEtOYWVxNFIzNkFjV203a2RIbVB1akU3amww?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 27 May 2026 15:30:00 GMT
- [232半導體關稅公布前鄭麗君：盼考量台美長期夥伴- 日報 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE43cTltNE1jZUxtZ2FZZHBGVk1EcTVHaVE2cU13M204aFhKMFNyZGwtb3BlTHEydEdoaDlNNFpkd3Z6cGpSRmJtT0NwS2tFRGJNY3VONHd0OW9FTWI3M0pJ?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 28 May 2026 19:00:00 GMT
- [黃仁勳兆元宴大咖雲集，台 AI 供應鏈重量級掌門人齊聚 - TechNews 科技新報](https://news.google.com/rss/articles/CBMib0FVX3lxTFBjRWpWX0FodzBEYW84dE0yVThlZ2RWY3dGVkVzdllsTkFCSTBXZ1dOTGNSWjNHZmM1VzZJbGlqeDZ4THMzMVliYUtpUmlWRzBEMFFuTURJcHpiQjZrUHRUbDhSa1FDZjRZTHYwODlONA?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 28 May 2026 10:50:00 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：談華為半導體新突破 黃仁勳：台積電和台灣領先10年 - 中央社 CNA；232半導體稅率尚未出爐鄭麗君：續爭取業者權益| 政治 - 中央社 CNA；南華大學半導體論壇匯聚國際產學能量 展現科技人才培育實力 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | 0.00 | -0.65% | +2.91% | 2,295.00 | 2,300.00 | -0.22% | 不適用 | 74.39 | 30.86 | 410.73B TWD / 17.50% | 2026-05-01 |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 120.89 | 121.77 | -0.72% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +13.60% | +22.41% | 142.00 | 143.50 | -1.05% | 不適用 | 4.00 | 35.68 | 22.66B TWD / 10.80% | 2026-05-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +22.85% | +12.10% | 214.25 | 214.25 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 518.09 | 518.09 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 923.52 | 928.41 | -0.53% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | +11.02% | +17.89% | 1,641.64 | 1,641.64 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | +37.82% | +28.76% | 426.58 | 426.58 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電、TSMC」，共 3 篇新聞命中。 同時符合主題標籤：semiconductor, chip, foundry。
- INTC：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 CPU, server CPU, x86, foundry；其中 1 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 1 篇新聞出現相關標籤。

### 主要來源

- [談華為半導體新突破 黃仁勳：台積電和台灣領先10年 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1MV2dMNFJNY21rdzZJcTI4V2hzUEcxRkJBRXNnMFExS1dpNFJ6aXFJVmtzZjFPSEZuVVdnNk9ZNGJTNmo2cEduQWhycFRNUHN3cnYxaEV3UnpFWi1Vd2c?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 28 May 2026 14:24:00 GMT
- [232半導體稅率尚未出爐鄭麗君：續爭取業者權益| 政治 - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9Ia3FUVk5fUU42NElhVjdxOE9LSmZaMFZwSWdrLWwzYm5WMDMtcVVvLWhvNVFhbi0tdGR5MjdiaHpjUkg0b0lyMlpwa0FxdWlhejVMTVdmazYxZE8wU2Nz?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 28 May 2026 07:45:00 GMT
- [南華大學半導體論壇匯聚國際產學能量 展現科技人才培育實力 - 中央社 CNA](https://news.google.com/rss/articles/CBMiVkFVX3lxTE9hN2R4V2lsN1RvNGotUmExMWs4V1NTampHREZYYzR0UU5ONjVMRm1fakJpRVIwVFkxX1J2MXg4RXVsVFpJVzNUOHVrejRILWFjQ0o5NmhB?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 28 May 2026 08:36:50 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：AI 散熱競爭進入下半場 奇鋐為何仍具成長空間？ | 行家心法 | 理財 - 經濟日報；焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | +0.19% | +3.41% | 2,580.00 | 2,835.00 | -8.99% | 不適用 | 61.06 | 42.39 | 15.63B TWD / 71.62% | 2026-05-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐、散熱」，共 2 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：跌停, 成長。

### 主要來源

- [AI 散熱競爭進入下半場 奇鋐為何仍具成長空間？ | 行家心法 | 理財 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTE0zZ3FCa3FiWjV3V3JBVFp4NF9fTWsyLWE2NEZ4WkE4UVBzTVlZVmVYZFpzVjQ1aEpjQWJxUzI0bVhxZ2duaXl5Q3RHaHZHR1JQMkxaUjl1NlpBZkEx?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 27 May 2026 07:49:30 GMT
- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 28 May 2026 10:13:21 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Micron Technology Inc Stock (MU) Opened Up by 4.75% on May 27: Drivers Behind the Movement - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 923.52 | 928.41 | -0.53% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Micron Technology Inc Stock (MU) Opened Up by 4.75% on May 27: Drivers Behind the Movement - TradingKey](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPTkpaRHVlZEF0ekpkZFVlcHo1aU83RDViYVFZNWNLNmRXejJFaVlMS2xDZlRIaGN2clFNaGdKZ3VtVTVSZ2FPbkV5bmp0MjlCLXZGYTY1VnJGMkI0UjVpSUlMUEdnYkVlaXpaSjc5SUdCOHlYVVVEZWllZlhkWTZwQ1NuSTBVX0FW?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 27 May 2026 13:47:29 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：個股動態報導內容-2A835736-C9EF-4148-8308-3C4488515194 - MoneyDJ理財網；台股「大怒神」 上演洗盤秀 國家隊進場救援 - 經濟日報；台股屢創新高但股民信心下滑？大型投顧法人這麼解讀 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-2A835736-C9EF-4148-8308-3C4488515194 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilAFBVV95cUxOUWhGZkhEalh6VmtIb2hnd0lVY1lGckx3Ty1TQ2Z5aFRxcGFwSHplWjBlTnF3YkpyZ0RRNWZmd081TjRvSWJ4VTd2YTlFVnNOenhQY1loREw0RzdLV1JBNFhmSlRkQzBveGxROGdsWDBsei1UUzVYSmxVakRJU0ZNSFlrNU1VUkU1aGFvVjdmV2JrVHNO?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 28 May 2026 07:18:43 GMT
- [台股「大怒神」 上演洗盤秀 國家隊進場救援 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5jYlUyRzA4Y0lWMDBGcU9JWE9jQ0ZrY1ZTbFFNZkFZeHFvLUFaVVNfVm1peXJWdnhka2JqOW9GVndrLTB5ZTFTUTJ1ZmxKZEdsSzJBVHEzVXY2d9IBX0FVX3lxTE1rZGZ3Mm5jWFFGeGtiTXYyVnNfc3oyWGt5NkZITUJFUHlYdFVwNXNvWUpJajNsTjdtR3VaZDVmOEF4NWpWbFBZMkxubjFabkRydGV3a0tKY1B4VmUtSEVJ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 28 May 2026 17:20:20 GMT
- [台股屢創新高但股民信心下滑？大型投顧法人這麼解讀 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxQM2F3SFlNREY4ZlROY3p0RE1fQ2RTRGthNEU5a1BLdW85dThaM1Q4TGhQZVZFd1ZCbHgyOWJxRW5OZHMwNkhidGRMY2l6em9JelRqby1sbDdtQXYzM2VDZmxEeTBWN1hzWm15VURlZGFRNmNqbFFqdFluNUc2TV8ydtIBX0FVX3lxTE1WZDhwTnU1XzJVYzBXRi1OanVlOTEza29NTUs4UFE0bFd1VTQ2ZTBha0JQRk13UWtrdFpDZGt1VHlzTXFiaUZwTmNuX0g0SEZlazlyZklOVzdraFZJV1hV?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 28 May 2026 14:17:02 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》收跌620點、日K翻黑，險守5日線-新聞內容-基金 - MoneyDJ；《台股盤後》收跌620點、日K翻黑，險守5日線- 新聞 - MoneyDJ；台股盤中創高後跳水終場大跌620點失守44K 單日震盪逾1700點創紀錄- 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》收跌620點、日K翻黑，險守5日線-新聞內容-基金 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxPY0t1cW9DYnlDWnRUU0VBNDh4LU5aMnhFRmh0WXh0M2ZjTE9WenQxYTFWcXYzM1NqS1RCS2dzc0ZiTjg4SlEwRUZYamdhbkpUY1ZuWXRPSncyc1NQeWN2MUtYSW51SzBHNEI3Y2VfUGNqR1FwUThNTE5hWk00SGJtTVE3d3dLT0l1QnhWSHUxOG8?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 28 May 2026 08:17:00 GMT
- [《台股盤後》收跌620點、日K翻黑，險守5日線- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMilgFBVV95cUxPWERuZzJSZk05QngzSjh0SXRlYUN4YjFZVWRGMjFmQWw3cW4xbnl2QWhSY2taX3dHRG8xM092dHJud2JVUkZlMUZCUDVBQVlDR2tTcGNZQ1BpOVA4OXRfZ1dRN1hxWDJPb0J5bF9wMjlvTDFFb1VhVzJuTndscGZ3NzRzMFpKNEstQ3hPdzFYTGlxSnNJM2c?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 28 May 2026 08:12:00 GMT
- [台股盤中創高後跳水終場大跌620點失守44K 單日震盪逾1700點創紀錄- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQQl9PbmhRRE45OHRiaUNBN3Rfb2xCU214VXB0WDdYQkpfcUVoVEkwSnRHdS1EQzBGRG5EZG1lUTR4WFVxLXpNR1NScEhTdU9ibE93OFBvc3JLMG9tYU9NVzlLd1d0QVI0ZWdSbC1hMXFfTDI3OHJRdE9RVm5jbUkzdTdVVjZkbm8tTHl1NmNmVE04dw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 28 May 2026 06:47:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
