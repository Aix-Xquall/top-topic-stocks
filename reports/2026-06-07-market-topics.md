# 每日股市熱門話題分析 - 2026-06-07

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **AI 伺服器與資料中心**｜中性｜熱度 12｜市場確認 N/A｜同向 0/0
2. **半導體與晶片供應鏈**｜負向｜熱度 4｜市場確認 55.00｜同向 3/5
3. **利率與成長股估值**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
4. **新興題材：5月營收**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
5. **記憶體與 HBM 供應鏈**｜負向｜熱度 9｜市場確認 13.37｜同向 1/3

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.32（樣本 11）
- 5日相關係數：-0.20（樣本 11）
- 同向比例：5/11

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| AI 伺服器與資料中心 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | 55.00 | 3/5 | 1 | +4.33% | -3.98% |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：5月營收 | N/A | 0/0 | 0 | N/A | N/A |
| 記憶體與 HBM 供應鏈 | 13.37 | 1/3 | 2 | -3.32% | -13.38% |
| 新興題材：TradingKey | 13.37 | 1/3 | 2 | -3.32% | -13.38% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價呈負相關；應檢查正負向詞庫，並降低新聞直接提及但股價背離的權重。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-05-25 | 0.40 | 0.33 | +50.00% | 10 |
| 2026-05-26 | -0.23 | -0.31 | +92.31% | 13 |
| 2026-05-27 | -0.07 | -0.07 | +87.50% | 8 |
| 2026-05-28 | 0.14 | -0.07 | +88.89% | 9 |
| 2026-05-29 | 0.14 | -0.04 | +71.43% | 7 |
| 2026-05-30 | 0.16 | -0.06 | +71.43% | 7 |
| 2026-05-31 | 0.96 | 0.09 | +100.00% | 3 |
| 2026-06-01 | -0.92 | -0.72 | +16.67% | 6 |
| 2026-06-02 | 0.08 | 0.05 | +72.73% | 11 |
| 2026-06-03 | 0.48 | 0.62 | +90.91% | 11 |
| 2026-06-04 | -0.38 | -0.30 | +85.71% | 7 |
| 2026-06-05 | 0.31 | 0.93 | +50.00% | 6 |
| 2026-06-06 | 0.12 | 0.06 | +45.45% | 11 |
| 2026-06-07 | -0.32 | -0.20 | +45.45% | 11 |

## 歷史回測摘要

- 回測日期：2026-06-07
- 近5日 3日相關：0.31
- 近5日 5日相關：-0.29
- 同向比例：+37.50%
- 權重狀態：未調整

- 方向準確度：+37.50%
- 信心排序準確度：0.31
- 診斷：正相關

調整原因：近 5 日有效樣本 8 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：AI 伺服器與資料中心 相關新聞集中在：股價回檔，市場如何評價其 AI 轉型？ - TechNews 科技新報；禁用 AI 面試如何重新定義數位時代人才價值？ - TechNews 科技新報；「知識獨立性」如何影響 AI 倫理與產品開發？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 99.17 | 114.68 | -13.52% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +2.77% | +15.75% | 205.10 | 211.14 | -2.86% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 466.38 | 516.10 | -9.63% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -0.63% | +0.42% | 2,365.00 | 2,365.00 | 0.00% | 不適用 | 74.39 | 31.80 | 410.73B TWD / 17.50% | 2026-05-01 |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +6.09% | -17.77% | 416.67 | 506.69 | -17.77% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -7.59% | +20.71% | 385.73 | 446.77 | -13.66% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | -2.20% | -5.56% | 577.00 | 611.00 | -5.56% | 不適用 | 10.86 | 53.57 | 62.25B TWD / 19.22% | 2026-05-01 |
| 2454 聯發科 | 產業/供應鏈推估 | 0.00 | -4.97% | -0.23% | 4,300.00 | 4,310.00 | -0.23% | 不適用 | 62.91 | 68.53 | 46.74B TWD / -4.14% | 2026-05-01 |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [股價回檔，市場如何評價其 AI 轉型？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMid0FVX3lxTE5nRDNjQkhDWVZBNGlJOC1GWTVTYjYtaGY1UWlNM1J5YmhDQm94Unp4NEI5eDhKX2QzWEQwMHA4QVdGelEwdnA4WHlQUkIta2tNbVNUdUtfeWlCX2dhcVQ5WHpfaDlobWNEaGFubi1lSnZlR2k0TnBV?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 06 Jun 2026 21:08:01 GMT
- [禁用 AI 面試如何重新定義數位時代人才價值？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMilwFBVV95cUxQOXRqSWYzR0E2bThwMFhJc3I4Z091TmdHSG1SRnpMMzhDdy16UC1tYTZVMHhja1o3ckRPNUdoaUtpMmVtbWQySVZya2JJOGIxX0ZsX1ItZVVMWkJXMG5sdHhiTnVjQXpoNFFCd2hkWUdpV1hYRTB1d1JodmV1X21PRjZ3elB4M2pDUlNIVWpzZXBORHg4M2VR?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 06 Jun 2026 18:06:00 GMT
- [「知識獨立性」如何影響 AI 倫理與產品開發？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMilwFBVV95cUxOQ25RQVlTM254eVl4X2ZTbWo4WTZzMEFSelhhUlI4eENSbUdEWkFtOXJoVmVDTDZfWXF4MThJQi00am1fc1ViLUdRdWpTVDIwamxnRUhkNWQtdUxyOHRSeXNKLVZXazdMdG5tXzcwVDREdWlrekpKOHJROFViV2dibmRsZ1F6NWwxa2g0TV9IUWhsOGZqRkJ3?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 06 Jun 2026 18:01:28 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：What Triggered the Recent Semiconductor Sell-Off - Kavout；經部：南部半導體崛起 資訊電子就業占製造業近3成 - 中央社 CNA；Wall Street's 'fear gauge' punches back as the 'crash up' in chip stocks finally reverses - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | -0.09 | N/A | N/A | 99.17 | 114.68 | -13.52% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.04 | -0.63% | +0.42% | 2,365.00 | 2,365.00 | 0.00% | 未明確 | 74.39 | 31.80 | 410.73B TWD / 17.50% | 2026-05-01 |
| 2303 聯電 | 產業/供應鏈推估 | -0.05 | -7.07% | -9.00% | 131.50 | 144.50 | -9.00% | 同向 | 4.00 | 33.04 | 22.94B TWD / 17.78% | 2026-06-01 |
| NVDA 輝達 | 產業/供應鏈推估 | -0.02 | +2.77% | +15.75% | 205.10 | 211.14 | -2.86% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | -0.04 | N/A | N/A | 466.38 | 516.10 | -9.63% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | -0.04 | N/A | N/A | 864.01 | 971.00 | -11.02% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | -0.04 | -9.15% | -8.00% | 1,559.32 | 1,831.50 | -14.86% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -7.59% | +20.71% | 385.73 | 446.77 | -13.66% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 CPU, server CPU, x86, foundry；其中 2 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 2 篇新聞出現相關標籤。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 2 篇新聞出現相關標籤。

### 主要來源

- [What Triggered the Recent Semiconductor Sell-Off - Kavout](https://news.google.com/rss/articles/CBMiiwFBVV95cUxQeV9hbWl4LXg0eW5ZWFVERlpaZGRsZzBkOEQzb0VuSmptQ2RsR3RUcldSTzhJcW1URGZsbnBjVUxmYlNpMHlESnlJdEVvZ1RaSWloQ0ZfODJXV012UF9qYjFfYVNDaG15cXpBNXYxYWpjaGNIY2hRa3hOdGhUSjdOcDhabENFWmFvV1M0?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 06 Jun 2026 05:47:53 GMT
- [經部：南部半導體崛起 資訊電子就業占製造業近3成 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE9qTkNxeUtMR0pnY3MwS1ZiY0FmdDNJaXFaVFhnenJjampjWnJHdUhSUzR3TDRleWY3Zl9CTXZSVkRQNG1GZXcybHd5NHI1NzBfM2NWRHQwbHhGTnlqS0E?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 05 Jun 2026 11:10:00 GMT
- [Wall Street's 'fear gauge' punches back as the 'crash up' in chip stocks finally reverses - CNBC](https://news.google.com/rss/articles/CBMivgFBVV95cUxQenFydEpMYUgwS3hiZTBTWjZuZ3dhS2YzNVAwa1RlM0lEbDFWYktubzBzN1BuM0lzZ0dhdXhIWUVZNE44cjNlVS05VHpFRVQxekI3WE84Z21kcG9jRDNvczl0bkFMNVFiQ2M3Tks1bXZhenNCM3JkaGo4R21sbHE5ZUF6c01oSzhQcmJWcGpJOEw1bkVFNW1oYmEyR0NjQUZwYTVaNlVqNXJHYWNvbXB2NUw2QTI2SWZpMnBkZFd30gHDAUFVX3lxTE42VTBsRDUyMnBoQWhkMWJRcERlQzFzeWY0aWhYUW1rVTQ2WmhVdjJ0WDlEWWtZSElfcU1iUTBOR1diVHhKRGlDd1B2MmVrWmtDREZWLUJvQ084anEtTUE5c0FqanJ0S1NUcFVPbDFLanlER2tDVU5Xel9iT01MQlVFTTZiUHNkRS1vbGZuaGQwNWVuX2xIYmpKcGhMYnRuMElQcWJCRS1lUzlaSnVjQUlYcGE5dWYzTUl5REF3N2hkR21uNA?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 06 Jun 2026 12:58:29 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：高達 80% 留任率對 AI 新創長期估值的意義？ - TechNews 科技新報；〈美股盤後〉非農爆表重創降息夢！費半狂瀉超10% 台積電ADR摔逾6% 標普9周連漲止步 - news.cnyes.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | 0.00 | -0.63% | +0.42% | 2,365.00 | 2,365.00 | 0.00% | 不適用 | 74.39 | 31.80 | 410.73B TWD / 17.50% | 2026-05-01 |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +6.09% | -17.77% | 416.67 | 506.69 | -17.77% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [高達 80% 留任率對 AI 新創長期估值的意義？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMilwFBVV95cUxPNlNQalhPT19nN2tQZEpPTnBjOUpPUEhaTkd3QnM4cXZCUElFOVVJQjB3NGN6eFgyWjlmTW5Bb2RDeXRvYnVRMXV1TENDdEZPSWRIVDVxemltNzcwUWE4WUc3a19xSURmd1hMWThOTkF0a1pnRDBXT0hwbHlCa3FSMXBVbHpmRHFzaXZMN1pwRXRKdk9GMk5j?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 06 Jun 2026 18:00:48 GMT
- [〈美股盤後〉非農爆表重創降息夢！費半狂瀉超10% 台積電ADR摔逾6% 標普9周連漲止步 - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTE1saldnSzVBWjRNYjZyNFpqd3F6QktleWJlS1BoTmRsbmNWbWhxRWpialNzMXBUeXZtcjJKMUI1VWJYTThHQTlrOW9iY3gycXM?oc=5) - Google News source discovery | 鉅亨網 Sat, 06 Jun 2026 00:12:47 GMT

## 新興題材：5月營收

摘要：新興題材：5月營收 相關新聞集中在：5月營收噴6倍！「記憶體IC設計廠」訂單看到明年中 DRAM逐月漲價20%首季EPS達1.88元 - Yahoo股市；5月營收狂增640%！「記憶體大廠」4月EPS暴賺3股本 切輝達邊緣AI供應鏈前景樂觀 - Yahoo股市

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +2.77% | +15.75% | 205.10 | 211.14 | -2.86% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [5月營收噴6倍！「記憶體IC設計廠」訂單看到明年中 DRAM逐月漲價20%首季EPS達1.88元 - Yahoo股市](https://news.google.com/rss/articles/CBMinwNBVV95cUxNRmpxckV6NGhjRHBwMmJvUGduU3hTbm94SGdJdHFPQk1xUnFZLUstSV94QmVUb2NOMUxSUWxoYVFEYUcwbzdEcDBNZk94enlDdnhiM2NsaVlzcGotb0FRckwyYkc4aFBGMDYwRGdrUDBKVUhPSWtFMXFHVGhuUDRidm9DWUVmb1ZZTWNNWHMtblpNTjQwTjEtck9HTVNWOUpvNmNhVjRnQ2FDQnBwWU5rUGhaTlBPQXNHR3FJakllOVpMQ0hCN0NwRzhpZ09oX3V2SG9HVC1tajFSX2U4WEtFdzF5MUJISUtDZnFfRzJibTJmaGFqYlIyQUxhcmdrQ3dTUXdhM1ZXTVhIcjVTcVhfNU8zamlNdnhuaVh5RkpkWVBfb19HT1Q0ci1LS0NCdldSeWNndkRlNW1Xc0pFdU1FaVVnMTEtZ19TTXJoVHZCckpOd2VnWUdIQjlFVzFaeGRBS25McVZIMHdud3V6aUszN3ZSTEx4Tm11VmE1SjhIekhjbjFidVBQQjlSSGF4M0hzRlo0ZEd1M3BNUE1CbGxj?oc=5) - Google News source discovery | Yahoo 奇摩股市 Sat, 06 Jun 2026 11:30:00 GMT
- [5月營收狂增640%！「記憶體大廠」4月EPS暴賺3股本 切輝達邊緣AI供應鏈前景樂觀 - Yahoo股市](https://news.google.com/rss/articles/CBMisgNBVV95cUxNNVkzSkYyU2RsbWYxZ2J0ejVPRjVrcWZTNkFpWDZMMlNWQm9uLXNwZnBCb1dlbWVuTUlLY1RUTEM4d3lDRW95WEZOeUFTUnpDT2ZZSlo5UXBualZWMGRENXUyTl9QcWNRb2daR1dlc0FlZXJHSU5URUdQLXMtbzd4Zkd0dzBBa1lIb0FKR1dhXzlvX2xCajgtR2tGR2lSUWRwdzNKcEh2YnU3VlNXd3JqNEEzc1I4cjJDZHprd1EyUmJfZE5pNDNQMzlPeFVUX19LRGJXN3lDaTZCS3BLdHpacmRac18wRm12TEhmdVBJcVBmeFZ2aUFKU0tlSDlJUml5ZTVaeVpjNlZDSGpERTB3cTNjcTUyay14THVGYTk1TGxpcVJjTWRhQVJKZWZ0QWpFVWsxUkFzbHRPcS1UbGVwSzlGemlmUFhkQkI2cVpxN1YxQmJFajhaVW9fVEd0THkxU2V0UldpWVNJNlQ5VnB6ZkJJY0dpVzZ1VmtVNVh1T0h3NG8tWnFPR20xc2VQMTg1UVRxLWw4Nm9MUnpKcVY3d2RKdTl5QUFwQmJBUWZGV0FwQQ?oc=5) - Google News source discovery | Yahoo 奇摩股市 Sat, 06 Jun 2026 08:45:00 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Intel and Micron Shares Plummet, What You Need To Know - StockStory；Intel Lands a Preliminary Apple Chip Deal and an SK Hynix Packaging Partnership — Is INTC Still a Buy at $124? - TradingKey；SanDisk (SNDK) Is Doing Something Unprecedented In The Al Sector! SNDK STOCK PODCAST ANALYSIS BUY Jobe Bellingham (gRMiCAoJ7a) - Mshale

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | -0.72 | N/A | N/A | 864.01 | 971.00 | -11.02% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.72 | -9.15% | -8.00% | 1,559.32 | 1,831.50 | -14.86% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | -0.62 | N/A | N/A | 99.17 | 114.68 | -13.52% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | -0.28 | +2.77% | +15.75% | 205.10 | 211.14 | -2.86% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 新聞直接提及 | -0.27 | +16.34% | +32.39% | 307.34 | 312.06 | -1.51% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、memory」，共 4 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：falls, reduce。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK、SanDisk」，共 4 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：falls, reduce。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel、INTC」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel and Micron Shares Plummet, What You Need To Know - StockStory](https://news.google.com/rss/articles/CBMitgFBVV95cUxPYjhrdkN6RURRUGlRbDhQSGxyQndlVU5iWDdpdXo2bExIMk53U0ZicGM5OVB4bUJvd1NCZ0Z2ZGlGeHFxWXJZYWJBNkE3eUJZS0c1R016Tmh4eDRZRWI2alA5aDlMdV9GM25tamZqempfTmg1NUw1bG5EUURuNWxSd3R2LUgtcmM2LWdWbzRBQ2JwY1R2MExaZGRDMjZ1S0EtSHZ1WWltY1dGZjgxSzdkdjJBY0tLdw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 05 Jun 2026 16:30:31 GMT
- [Intel Lands a Preliminary Apple Chip Deal and an SK Hynix Packaging Partnership — Is INTC Still a Buy at $124? - TradingKey](https://news.google.com/rss/articles/CBMi7gFBVV95cUxNTGpHN3o3WGJhaU1Nbld3bC03TnZpTlhfRXNCeU1Oc0QzRTlyelo3VjNvN0Nucjd5UWpkTDB5S1VPMVlRcHhfekg0U01ZbnoxNTRrbU1UdE11R3FQX3lIX3J3eFN0OUFjaENlM2ZlSjg0UkFIbGoxMGNPdXRrZFdVcEIxWTZfNlNRRG1fQXA5X1VoLUNMQklucVppVl9mVFc1cVBsNV95V1FqUWpLdEExZHZQTm5NM0RVQzRucC12MGthOVVXdEhsTUVWR1FNWjVhdDRXelNuTzNVbHpqSWJiamFFVmI0NTFGRjdwQTFR?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 06 Jun 2026 00:14:26 GMT
- [SanDisk (SNDK) Is Doing Something Unprecedented In The Al Sector! SNDK STOCK PODCAST ANALYSIS BUY Jobe Bellingham (gRMiCAoJ7a) - Mshale](https://news.google.com/rss/articles/CBMiW0FVX3lxTE82c25ZNkhMbnBFcHlYZktjT2gzRlFzREd4ZFlubTJYeG4zZFJ6NU1OdGxaX3BRYWM0bFdDWk5tMlNVS3BvWXRLZW1jUVp3SUdNYXlKam5zNEhNVm8?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 06 Jun 2026 17:27:45 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Intel Lands a Preliminary Apple Chip Deal and an SK Hynix Packaging Partnership — Is INTC Still a Buy at $124? - TradingKey；Market Rumors Nvidia Rubin Platform Plans to Reduce Memory Capacity, Storage Stocks Plunge Across the Board, SanDisk Falls Over 11%. - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | -0.27 | +2.77% | +15.75% | 205.10 | 211.14 | -2.86% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | -0.53 | N/A | N/A | 99.17 | 114.68 | -13.52% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 新聞直接提及 | -0.53 | N/A | N/A | 864.01 | 971.00 | -11.02% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.53 | -9.15% | -8.00% | 1,559.32 | 1,831.50 | -14.86% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 新聞直接提及 | -0.27 | +16.34% | +32.39% | 307.34 | 312.06 | -1.51% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 方向判斷命中詞：falls, reduce。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MU：新聞直接提及「memory」，共 1 篇新聞命中。 方向判斷命中詞：falls, reduce。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Lands a Preliminary Apple Chip Deal and an SK Hynix Packaging Partnership — Is INTC Still a Buy at $124? - TradingKey](https://news.google.com/rss/articles/CBMi7gFBVV95cUxNTGpHN3o3WGJhaU1Nbld3bC03TnZpTlhfRXNCeU1Oc0QzRTlyelo3VjNvN0Nucjd5UWpkTDB5S1VPMVlRcHhfekg0U01ZbnoxNTRrbU1UdE11R3FQX3lIX3J3eFN0OUFjaENlM2ZlSjg0UkFIbGoxMGNPdXRrZFdVcEIxWTZfNlNRRG1fQXA5X1VoLUNMQklucVppVl9mVFc1cVBsNV95V1FqUWpLdEExZHZQTm5NM0RVQzRucC12MGthOVVXdEhsTUVWR1FNWjVhdDRXelNuTzNVbHpqSWJiamFFVmI0NTFGRjdwQTFR?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 06 Jun 2026 00:14:26 GMT
- [Market Rumors Nvidia Rubin Platform Plans to Reduce Memory Capacity, Storage Stocks Plunge Across the Board, SanDisk Falls Over 11%. - TradingKey](https://news.google.com/rss/articles/CBMizAFBVV95cUxPMzkzNU02MkluY2lUUGtUc3QyaThEZjZ6QnJMb3QxOEFnNi1RN3lwNXZRWGdkVE1yTEt4Q0lnWThuQlB3U2tkVi1mQTFsWEVmUkhudEgwdk5OM1FfSmtHY0hVZWx1YjdKMWdHbE9sN2s3TXJsa1U3NV8taWNkOF9uNkJWY3paVjFoTXJyNGVENFV2UVh0ZjNnVU1hdk1DQVVjSWxCOXB0c1V0WWsyYU91SkwwRW9zQ2tTZlVmQjdtSm5JVzFaWW1pd2RNc0c?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 05 Jun 2026 19:46:22 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：個股動態報導內容-579DC683-21EE-4EFF-8D05-C312A53FE1B1 - MoneyDJ理財網；個股動態報導內容-20B02AEF-F5D0-49C8-9C00-99C5ABA0D41B - MoneyDJ理財網；個股動態報導內容-98637DE8-43BC-42C7-BFF4-F127B2FC6476 - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-579DC683-21EE-4EFF-8D05-C312A53FE1B1 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilAFBVV95cUxPbmlFdkk3YVlmdm5CVGRTak55bHg3aUJYNHQ0Wl9KVWx2STNuQ25YTkFnQXNXTXNmYnJPTC1jWGtoRzlhSFpvdTZBb05qYmI4VGtxSktEaW85UlE1LWVwcDlQMHhqN0h0Wmh0RXVBdjd4Q2s0YmxVZUdjS0JpbGtISHZEWjF6ejJaZmE4cVpyVVBQLWJj?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 05 Jun 2026 20:34:18 GMT
- [個股動態報導內容-20B02AEF-F5D0-49C8-9C00-99C5ABA0D41B - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilAFBVV95cUxQVHh3Y0Q0UllyNk5MRGlFUEc3Rlc0MW85Q3I5SERKUGRNeTFrQjdNYi1HQkt6eExJOXcxYmJIVmdvcmZYRWgzUGM5V0hybXQ0QV9aNGVoc3FleWFhakIwQXRsWHRaakJxM2RxcVpyd1lFWkx6d01RRklWU3hpXzB6WHA2ajZYREtSclJpdnoxOC1UT2pT?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 05 Jun 2026 13:51:31 GMT
- [個股動態報導內容-98637DE8-43BC-42C7-BFF4-F127B2FC6476 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilAFBVV95cUxQdWs1Y2pxMGRjZjdoMWF0cGxmVEVPWVBxQmRSMlJoaVlOTno0NFlsMkp1Qm1jVVF1R1ptZzNDMkVRX1lwWkFPXzllSXhzWUFFTWhrb0VMNWoxWjB3ZFhLeE1OdFFFZ0ZBX1ZfMGpVX1lyaEdNNnl2cWRrR2xxMDhYeDNuWERaODhtNkZTUnVoZzJ3YXR0?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 05 Jun 2026 12:34:46 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：為昇科 115年5月營收4574萬、年增3.82% - MoneyDJ；為升 115年5月營收2.18億、年減24.07% - MoneyDJ；全漢 115年5月營收11.15億、年減9.79% - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [為昇科 115年5月營收4574萬、年增3.82% - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQZGU2ZGhsS2tzSXlnZUtTMm0wU0tMLVpMU2NLV3hyVFQwaUdCQUxBeE1Da2phWTZfdnNoWHF4dUhqOTRlU3k2dUxfOUlaUGFDd2oyR1ZWYzRwbkVhNm9SQkZjdkxibEs5N1NRbFNpenBnckw2T2hGMU1veFFnVHdJRkVxSUhxLWVaMjA4SHJ1Z1dBZw?oc=5) - Google News source discovery | MoneyDJ Sat, 06 Jun 2026 11:43:00 GMT
- [為升 115年5月營收2.18億、年減24.07% - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNVTNsNVlCeUNmOV80ZFB6RlBVNVBqYnhZcEU4emo5NTc2TDV3SkVmQ08tN0dRcENvVk5Ob09zUkltbGdmdFlWTUdiVEExU1VseWFEMTJYX29kZFhld2Q4T1VLWlRvbVJIVEdNcjk4WTJRMHNfcExPaXhscG45OVFNWWpFdTliOHFidS0tNzFqMWF3dw?oc=5) - Google News source discovery | MoneyDJ Sat, 06 Jun 2026 13:03:00 GMT
- [全漢 115年5月營收11.15億、年減9.79% - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNRlp4S2s1RHRwdnJPVXkzWWtOVDlMaDdnY245UDlXb2pPcmY2NlFMMjl4YVJsbEVfVnhKMGhxeExoNjdYREZQM1BPaWJjUjVMdk9RSGYyTzVmTEszX2QzM21vQi1qSXVVc0FNNkpUYnlLaHcxRkI5cWZoTEhGa2lRVzF1YTNEcko0XzJSX1U1eXM3dw?oc=5) - Google News source discovery | MoneyDJ Sat, 06 Jun 2026 09:39:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
