# 每日股市熱門話題分析 - 2026-11-10

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **綜合市場情緒**｜負向｜熱度 52｜市場確認 0.00｜同向 0/2
2. **利率與成長股估值**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0
3. **AI 伺服器與資料中心**｜正向｜熱度 14｜市場確認 0.00｜同向 1/8
4. **半導體與晶片供應鏈**｜正向｜熱度 4｜市場確認 0.00｜同向 0/8
5. **新興題材：MoneyDJ**｜正向｜熱度 12｜市場確認 0.00｜同向 0/1

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.32（樣本 29）
- 5日相關係數：0.24（樣本 24）
- 同向比例：1/29

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 綜合市場情緒 | 0.00 | 0/2 | 1 | -0.69% | +1.04% |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 0.00 | 1/8 | 6 | -8.85% | +0.18% |
| 半導體與晶片供應鏈 | 0.00 | 0/8 | 7 | -14.96% | -0.75% |
| 新興題材：MoneyDJ | 0.00 | 0/1 | 1 | -1.11% | -4.08% |
| 關稅與供應鏈轉移 | 0.00 | 0/3 | 2 | -10.71% | -10.92% |
| 記憶體與 HBM 供應鏈 | 0.00 | 0/5 | 5 | -21.00% | +5.82% |
| 散熱與液冷供應鏈 | 0.00 | 0/2 | 1 | -5.17% | -10.88% |

### 方法調整建議

- 方向信心與股價呈負相關；應檢查正負向詞庫，並降低新聞直接提及但股價背離的權重。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-10-27 | 0.07 | 0.31 | +50.00% | 18 |
| 2026-10-28 | -0.30 | 0.47 | +20.00% | 15 |
| 2026-10-29 | -0.05 | 0.04 | +42.86% | 14 |
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

## 歷史回測摘要

- 回測日期：2026-11-10
- 近5日 3日相關：-0.06
- 近5日 5日相關：0.06
- 同向比例：+46.67%
- 權重狀態：未調整

- 方向準確度：+46.67%
- 信心排序準確度：-0.06
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

摘要：綜合市場情緒 相關新聞集中在：台股外資布局高度防禦 法人點出後市看一關鍵 - 經濟日報；台股開高續彈逾千點重返5日線！台積電領軍 台達電、世芯跳空漲停 - 經濟日報；台股盤中重登43000點　台積電聯發科領軍 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | +0.25 | -1.11% | -4.08% | 2,235.00 | 2,480.00 | -9.88% | 背離 | 86.28 | 25.91 | 511.86B TWD / 54.65% | 2026-10-01 |
| 2454 聯發科 | 新聞直接提及 | -0.32 | +0.27% | -6.17% | 3,790.00 | 4,920.00 | -22.97% | 未明確 | 60.69 | 61.52 | 55.40B TWD / 1.97% | 2026-10-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 2 篇新聞命中。 方向判斷命中詞：漲停。
- 2454：新聞直接提及「聯發科」，共 1 篇新聞命中。

### 主要來源

- [台股外資布局高度防禦 法人點出後市看一關鍵 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFB2X21VV29KQ0NBODRnX1ZaLUdESkhTTms2NDJXTkRxUHI2Z2dRNUZrSVM0dDJBLTNxTUpzaTJUV3ZOZU9NaGkzdElsQmVJYTh6c2dCRHk5YWxxUdIBX0FVX3lxTE5mMVBqWDJWUWNiWlg1bXZEc2ZWYTJOX0l5bGJ5blFibTNPeUU0eXhQMS11cEphLV9CWkFhaDl1QmpFNGc1R0FpeUgtQ2wyRlVZWk1QYXpzRFlSaDBqc25Z?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 09 Nov 2026 19:13:31 GMT
- [台股開高續彈逾千點重返5日線！台積電領軍 台達電、世芯跳空漲停 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5rYnB4TG1HQ0ZaTE1nVk5hbzU0Umxiem1iV3lyM0pjdUlISnVYMC02V1NtR0hEall5UlNLS05CcXFoNG9pRzVqNnp5ZXQtZzN0MDhmaVNDRUY3UdIBX0FVX3lxTFBWVDZKUHlNNEU1LTItUDYxckI5THJDQ3d4OTZwaGlpMDgtUG82QWpSUUxlS2lORGV5OGxFSEFVZEVKYmdvWnUwRHN3bzdIMm5RZEU2UEpHUy1sLVpJU2xF?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 09 Nov 2026 08:00:00 GMT
- [台股盤中重登43000點　台積電聯發科領軍 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxQRkxJZzJtbDN4c1l0QmhpUXZWSDJlMkx3TlZUanROc0FpdTEzSFNEa0E1NDlJWmE3U00wQzg2WmEwRGlRSVh0UlV1Zmxjdmt4bDVLbnFFY0tweEY1UDZlWGd4bVIxd2RyQkx1OVRmQW1GaFZiekFzbEJtV2RkTllqNtIBX0FVX3lxTE02NXBuRTZ6SEgwMmt3WVl6Qi1Fcjl1c3JIS2FVZGRDS2NlS3VzT0FtNW4zQnJiQnk2VUc5akFBR09DR2o3N1JwemhTZy1VR1lYUWFVVUl6VUpLeG14dEdB?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 10 Nov 2026 02:45:43 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：Micron Rises 6% as Bulls Tout Its Bargain Valuation and Buyback Firepower; Seagate and Western Digital Jump 11% - 24/7 Wall St.

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | -24.50% | N/A | 733.15 | 971.00 | -24.50% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +21.09% | +10.81% | 545.18 | 545.18 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Micron Rises 6% as Bulls Tout Its Bargain Valuation and Buyback Firepower; Seagate and Western Digital Jump 11% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi5wFBVV95cUxOaEkzTUtOalBCT2FfVlhBYnl3c0VjVDhMNDEwLVpqaktlNlF4V2pWeFlkVGhLT2FnTXFQTVNQaC1XMnBDbkpmQmxUMlVzUmI2QUpLUk5Ra1pBTzctWF8zcV8xWml2TEN1dUZDZzRqUW5XcVhDdldhaVdQNkJ4UFBheF8yeWJFY0MzeGJ5YTkzQXJJM2dCcFVZTTQyUDBRbzBzcXNNTTVkcS01MmdHcXJTcDI5WmtGUWx0eENHQ1d6Nzg1cW5UNnJZUVZHREE1NEt6MXVnT041RnVyU2Z3YnNYNmUyXzZoOUE?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 09 Nov 2026 17:52:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Not AMD. Not Intel. This Is the Artificial Intelligence (AI) Chip Stock Nvidia Should Fear Most. - The Motley Fool；3 AI Stocks To Own In November 2026 - Yahoo Finance Singapore；黃仁勳外遇掀國安疑雲，川普：某 AI 公司執行長遭警告準備坐牢 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.28 | -21.77% | -11.00% | 178.67 | 228.38 | -21.77% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.28 | -48.23% | +46.38% | 59.37 | 114.68 | -48.23% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.27 | -1.46% | N/A | 508.58 | 516.10 | -1.46% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.03 | -1.11% | -4.08% | 2,235.00 | 2,480.00 | -9.88% | 背離 | 86.28 | 25.91 | 511.86B TWD / 54.65% | 2026-10-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | +21.09% | +10.81% | 545.18 | 545.18 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -9.03% | -17.93% | 319.48 | 446.77 | -28.49% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.02 | -10.53% | -16.77% | 617.00 | 703.00 | -12.23% | 背離 | 17.55 | 40.59 | 88.13B TWD / 45.52% | 2026-10-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.03 | +0.27% | -6.17% | 3,790.00 | 4,920.00 | -22.97% | 未明確 | 60.69 | 61.52 | 55.40B TWD / 1.97% | 2026-10-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Not AMD. Not Intel. This Is the Artificial Intelligence (AI) Chip Stock Nvidia Should Fear Most. - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxQTl9nX2QzRVlCTVJEUF9iVXpva3ZYZU9Ial9aY3M3TkJvd3dUMnpMS2hMUW5ZZmVLZjlReTFGblJGTUYwRE9LMlc2MGZaZW5ySUdyQ2Z4aWRCR0JXaERqQ1FfY2NvdThjMlV3ekFoMktXTkNXY0RSVnd1cU9MZmhHYXVubFpkZ3JRNHhLb0R0ZmFSRE1xbmxrVA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 09 Nov 2026 12:00:00 GMT
- [3 AI Stocks To Own In November 2026 - Yahoo Finance Singapore](https://news.google.com/rss/articles/CBMifkFVX3lxTE5JNEVxVk5QY2FTdmRTMFFpeU1lT21EaUpBbWdvakFwTHc2SWYxdndvTzh0bFVaSlkwUFdHU2JncDNSYnpyZ1NBNzNLVHczb2pKaDdCYkI4Y09HRHE0Y3RfdkRzeFN5N1R0VnhfcFRTaTg0VTk2S0ZleFV4N2k5dw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 09 Nov 2026 13:13:13 GMT
- [黃仁勳外遇掀國安疑雲，川普：某 AI 公司執行長遭警告準備坐牢 - TechNews 科技新報](https://news.google.com/rss/articles/CBMisgFBVV95cUxPd3RzWkRGOG15cE1qZ3FkUzVXV1JFaHAxdER2SElndHFwNmFKODRNempFVllLSmhKU09BSG9uNWYzTDdIR1JETzFJamdkZlFtZDdxRXFobFJiai03bXV5ZmdhbW9KS2NwLXdTekdVa0w1bV8yVmstMHkwdHZoY2trRW1vTDZTVUFoUGt6R3lmNWdBM2tucTdiZXY2VnFzVUVza2k1aG42b2hkUkNzakluUFZ3?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 10 Nov 2026 01:38:13 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Not AMD. Not Intel. This Is the Artificial Intelligence (AI) Chip Stock Nvidia Should Fear Most. - The Motley Fool；國安基金進場發威！瑞銀看好21檔半導體股台積電、聯發科入列- 日報 - 工商時報；Google unveils new AI chip variants as cloud demand surges - Reuters

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.26 | -48.23% | +46.38% | 59.37 | 114.68 | -48.23% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | +0.24 | -1.11% | -4.08% | 2,235.00 | 2,480.00 | -9.88% | 背離 | 86.28 | 25.91 | 511.86B TWD / 54.65% | 2026-10-01 |
| NVDA 輝達 | 新聞直接提及 | +0.24 | -21.77% | -11.00% | 178.67 | 228.38 | -21.77% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.24 | -1.46% | N/A | 508.58 | 516.10 | -1.46% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2454 聯發科 | 新聞直接提及 | +0.36 | +0.27% | -6.17% | 3,790.00 | 4,920.00 | -22.97% | 未明確 | 60.69 | 61.52 | 55.40B TWD / 1.97% | 2026-10-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.03 | -8.34% | -12.09% | 98.70 | 164.50 | -40.00% | 背離 | 6.80 | 14.28 | 25.20B TWD / 18.33% | 2026-11-01 |
| MU 美光 | 產業/供應鏈推估 | +0.02 | -24.50% | N/A | 733.15 | 971.00 | -24.50% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.02 | -14.55% | -17.54% | 886.51 | 2,335.00 | -62.03% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：surges。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip, foundry。 方向判斷命中詞：surges。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：surges。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Not AMD. Not Intel. This Is the Artificial Intelligence (AI) Chip Stock Nvidia Should Fear Most. - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxQTl9nX2QzRVlCTVJEUF9iVXpva3ZYZU9Ial9aY3M3TkJvd3dUMnpMS2hMUW5ZZmVLZjlReTFGblJGTUYwRE9LMlc2MGZaZW5ySUdyQ2Z4aWRCR0JXaERqQ1FfY2NvdThjMlV3ekFoMktXTkNXY0RSVnd1cU9MZmhHYXVubFpkZ3JRNHhLb0R0ZmFSRE1xbmxrVA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 09 Nov 2026 12:00:00 GMT
- [國安基金進場發威！瑞銀看好21檔半導體股台積電、聯發科入列- 日報 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1YQWE2N2gySmNwYVJsemUxQ0pOZDNWcnJLR0RKWmRYLVdNVFAzU2VlZlM5RWptSEVDWThFNHVpNGlDb2xCYWhiQWN2OEp0LVhvY1Y2bkk4SEY5b1ZWTzVV?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 09 Nov 2026 19:00:00 GMT
- [Google unveils new AI chip variants as cloud demand surges - Reuters](https://news.google.com/rss/articles/CBMiuwFBVV95cUxOd1JDNDVNcnh0MU5wSzdrUVhVY3FpSklfazJZVWEtbGwyUkxydzhTcUVhV2F5aHdHV29OUE9Ea1JkZm93d2xVcU1VMEdEZE1xamt3RlktMVlqLUNGRVlIalpNd3ZRS2Z2LVN3b24yNUcyV1lkQm01MmJ3eHJLZVk3a3ZDSkhHcllvVHVxX1c1d3YtRHV3Q1g5d241UGNpLXJpSXRwTUYzcEdPcUhmN2FqdnBRNVZUYlM1WmJF?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 09 Nov 2026 15:24:44 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：統一證券：台股短期反彈壓力區在45000點 - MoneyDJ；國票證券：台股回檔整理後向上的可能性較大 - 報告 - 新聞 - MoneyDJ；美股指數期貨最新報價 10:37-台股 - MoneyDJ

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | +0.21 | -1.11% | -4.08% | 2,235.00 | 2,480.00 | -9.88% | 背離 | 86.28 | 25.91 | 511.86B TWD / 54.65% | 2026-10-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。

### 主要來源

- [統一證券：台股短期反彈壓力區在45000點 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPZmtNODY2bVJXRGd5dDFMak9zczFUNUFtLTc4WlNjdnZqeWp3clNOYllkdnBrN254U3RqczVmMmFZMW1qN3Q0VGhBeTZTQmVUdjFyY041UDVjSjIwT2JNUjl1dzRMU1Z3ZWVzd0tIODdxSXRHdVlEWTI4RUU2ZkZCRzJiRkFVQWwzcjFvRW93R3JsQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 10 Nov 2026 00:35:00 GMT
- [國票證券：台股回檔整理後向上的可能性較大 - 報告 - 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMihwFBVV95cUxPVFFXNmNEZVBEd2RsWHNfVl9PNU9WY3pJNndUWllWX01TMXNCcDBLRU04alJsMkVfZDNWMW5KazE5XzhQemVYb1kzZHZIWG5Pcl85djI1a0lLaDVhbWNGS2FrT1VLdDJ5Q09la09KckYtS3dCcmFLZlVDQzhVZ18yYUU0Y3BQQzA?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 10 Nov 2026 00:35:00 GMT
- [美股指數期貨最新報價 10:37-台股 - MoneyDJ](https://news.google.com/rss/articles/CBMiigFBVV95cUxOV0Z6VnRweDBuMVQwX1M4UFhyLTBDN3J6WFVRckhuWkRNY1BfZjMxcFU2VTlDZFhxVTgxalNWMlJpanJCaGFzLUh4bXVBU1oyYVZtSDJPei1xQzNsS3ZYUGJVdUZLbjlhdUhsZmx3Zl9lYktfU0daVWdYTjdYbzdSdXJJdmpZUTMwWGc?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 10 Nov 2026 02:48:10 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：整理包／黃仁勳概念股笑了！輝達季度財報超預期 完整台廠供應鏈名單、潛在受惠股一次看 - 經濟日報；SpaceX 太空算力 2028 年上看 5GW！外資點名鴻海、奇鋐、台光電供應鏈 - 鏈新聞 ABMedia

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2317 鴻海 | 新聞直接提及 | +0.34 | -0.42% | -4.78% | 239.50 | 289.00 | -17.13% | 未明確 | 15.21 | 15.75 | 1305.32B TWD / 45.73% | 2026-11-01 |
| NVDA 輝達 | 新聞直接提及 | +0.21 | -21.77% | -11.00% | 178.67 | 228.38 | -21.77% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3017 奇鋐 | 新聞直接提及 | +0.21 | -9.93% | -16.99% | 2,790.00 | 3,435.00 | -18.78% | 背離 | 75.13 | 33.86 | 22.10B TWD / 34.35% | 2026-11-01 |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +12.38% | +25.76% | 350.69 | 350.69 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 2317：新聞直接提及「鴻海」，共 1 篇新聞命中。 同時符合主題標籤：supply chain, tariff。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 3017：新聞直接提及「奇鋐」，共 1 篇新聞命中。

### 主要來源

- [整理包／黃仁勳概念股笑了！輝達季度財報超預期 完整台廠供應鏈名單、潛在受惠股一次看 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBQUlViSHpPeDVlY29yaHFNNE5NcVlUQnE3ZThTcXRGNHgxYTVPOVVTRDlaTDV6Zml5WEwxVHNSeGFDcnVHUHhRSW15SzNpU0dYVDU3dThWNEVCbkZI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 08 Nov 2026 08:00:00 GMT
- [SpaceX 太空算力 2028 年上看 5GW！外資點名鴻海、奇鋐、台光電供應鏈 - 鏈新聞 ABMedia](https://news.google.com/rss/articles/CBMiakFVX3lxTE9yUi1TMm0xWmlMZVR6VkE5cml3VzEzZGZzWEJvN1dKcWctQzRURFBmcGZWbkFTeFYzaEVqcHpzODY2MjJPSDhmYllSdjVjVVBHTXhVMVJLRlo1LU91YTEtN1dMcnc3NnhxMlE?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 10 Nov 2026 03:32:14 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：AMD, AVGO, INTC, MU: Chip Stocks Inch Higher As Investors Look Past Midterms-Led Selloff, Nvidia Controversy - TradingView；Micron Rises 6% as Bulls Tout Its Bargain Valuation and Buyback Firepower; Seagate and Western Digital Jump 11% - 24/7 Wall St.；Micron's 26 SCAs: Can Take-or-Pay Deals Boost Earnings Stability? - TradingView

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.28 | -24.50% | N/A | 733.15 | 971.00 | -24.50% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.22 | -21.77% | -11.00% | 178.67 | 228.38 | -21.77% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.21 | -1.46% | N/A | 508.58 | 516.10 | -1.46% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.21 | -48.23% | +46.38% | 59.37 | 114.68 | -48.23% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | +0.21 | -9.03% | -17.93% | 319.48 | 446.77 | -28.49% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -14.55% | -17.54% | 886.51 | 2,335.00 | -62.03% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron」，共 3 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：boost。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AMD, AVGO, INTC, MU: Chip Stocks Inch Higher As Investors Look Past Midterms-Led Selloff, Nvidia Controversy - TradingView](https://news.google.com/rss/articles/CBMi9wFBVV95cUxOeDNwbExuU3hfOWZiQzhWdjMtVTA0UzZDU0lvQW8yQnhNejhMNnhWbWtjeWtfUnJvb1dpeFptMElCYzZSVDZCQ0VlTWUyWGJWXy1WdTFYSGlzVTh4cUR0NldvYlBsSG9GdW0yNGp2TUZUODFYRlJBcDVQUGRsVW1RMjRUalhQRFBOWU00SE9KeWZsUXJLQ3NGMjNLM2lWNHFKQmloQy12SXp4VHMtemZlTXhrLTFITEktOWpfWkJlVDQ1dG5qMk0zNWpiaWdqOG9Oc1dVbUk4QXhCZXpDQTlOTHA5RGJUc0FRZXlzaWk2dVdWLXRGVDdr?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 09 Nov 2026 03:34:00 GMT
- [Micron Rises 6% as Bulls Tout Its Bargain Valuation and Buyback Firepower; Seagate and Western Digital Jump 11% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi5wFBVV95cUxOaEkzTUtOalBCT2FfVlhBYnl3c0VjVDhMNDEwLVpqaktlNlF4V2pWeFlkVGhLT2FnTXFQTVNQaC1XMnBDbkpmQmxUMlVzUmI2QUpLUk5Ra1pBTzctWF8zcV8xWml2TEN1dUZDZzRqUW5XcVhDdldhaVdQNkJ4UFBheF8yeWJFY0MzeGJ5YTkzQXJJM2dCcFVZTTQyUDBRbzBzcXNNTTVkcS01MmdHcXJTcDI5WmtGUWx0eENHQ1d6Nzg1cW5UNnJZUVZHREE1NEt6MXVnT041RnVyU2Z3YnNYNmUyXzZoOUE?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 09 Nov 2026 17:52:00 GMT
- [Micron's 26 SCAs: Can Take-or-Pay Deals Boost Earnings Stability? - TradingView](https://news.google.com/rss/articles/CBMiuwFBVV95cUxQeDVHVmlYVG1TenZDQ1BGcUVweC1qSFdxZ25TMFBIR05UUENuZG15Skd0WDVubUZvd2hlTEVIZHN6b2k5MDltNzlhWVR3STdQUHVUYVJmdjhQN1VDSFBFYS1mNjJJN1JjdmhqbnQwRlZTbXg3QUplMmpjbzFia2o1NFlTUHAzMWJCNUNPVC00U1JuVlFXckUzMERjcmNmLXBsRnJ2aFFSODFIc1Nqd3BvTEFiZnltWmlTMzIw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 09 Nov 2026 17:21:32 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：奇鋐端出佳績！10月營收221.03億元連四個月刷單月新高紀錄- 產業 - 工商時報；【即時新聞】奇鋐今日公告最新財報，受惠AI伺服器放量，第三季營收年增逾五成表現亮眼！ - CMoney投資網誌；SpaceX 太空算力 2028 年上看 5GW！外資點名鴻海、奇鋐、台光電供應鏈 - 鏈新聞 ABMedia

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.28 | -9.93% | -16.99% | 2,790.00 | 3,435.00 | -18.78% | 背離 | 75.13 | 33.86 | 22.10B TWD / 34.35% | 2026-11-01 |
| 2317 鴻海 | 新聞直接提及 | +0.32 | -0.42% | -4.78% | 239.50 | 289.00 | -17.13% | 未明確 | 15.21 | 15.75 | 1305.32B TWD / 45.73% | 2026-11-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐」，共 3 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：受惠, 放量。
- 2317：新聞直接提及「鴻海」，共 1 篇新聞命中。

### 主要來源

- [奇鋐端出佳績！10月營收221.03億元連四個月刷單月新高紀錄- 產業 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTFAzVzdCRnNSa3c3NUhrTWc3NWtCUmptdDU3N0taTzVGYzRjdDFaLV9uTHNkME9CZnpMTlZIcjg3QlhYdGV3SmNVOFlyVUlKZmxXc0kzQWFmaHUwZUdQaVlZ?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 08 Nov 2026 07:25:00 GMT
- [【即時新聞】奇鋐今日公告最新財報，受惠AI伺服器放量，第三季營收年增逾五成表現亮眼！ - CMoney投資網誌](https://news.google.com/rss/articles/CBMikAFBVV95cUxQSndXY2F6U2tvOWFGcm5qVUdZcVNLckR2eml1cENlSlgtSE0yNmxtSk1lZWNEQ1c4YU9jN1Z1WUk0TnpuZkRHbEpyYWx3NmhXODBHd0RlZk9hNHE3UjNCZmRGOFdmQnNmUjRkV1RlYlhabV9ndzJaMEdydHdUSER5SmxkNVRmSkV6MVN2UWkwZkM?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 08 Nov 2026 22:20:43 GMT
- [SpaceX 太空算力 2028 年上看 5GW！外資點名鴻海、奇鋐、台光電供應鏈 - 鏈新聞 ABMedia](https://news.google.com/rss/articles/CBMiakFVX3lxTE9yUi1TMm0xWmlMZVR6VkE5cml3VzEzZGZzWEJvN1dKcWctQzRURFBmcGZWbkFTeFYzaEVqcHpzODY2MjJPSDhmYllSdjVjVVBHTXhVMVJLRlo1LU91YTEtN1dMcnc3NnhxMlE?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 10 Nov 2026 03:32:14 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
