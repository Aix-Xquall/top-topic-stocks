# 每日股市熱門話題分析 - 2026-07-25

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **AI 伺服器與資料中心**｜正向｜熱度 15｜市場確認 0.25｜同向 1/6
2. **關稅與供應鏈轉移**｜正向｜熱度 4｜市場確認 22.95｜同向 1/4
3. **半導體與晶片供應鏈**｜中性｜熱度 4｜市場確認 0.00｜同向 0/5
4. **記憶體與 HBM 供應鏈**｜正向｜熱度 8｜市場確認 0.00｜同向 0/1
5. **綜合市場情緒**｜中性｜熱度 46｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.30（樣本 16）
- 5日相關係數：-0.06（樣本 16）
- 同向比例：2/16

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| AI 伺服器與資料中心 | 0.25 | 1/6 | 5 | -3.81% | +5.18% |
| 關稅與供應鏈轉移 | 22.95 | 1/4 | 3 | +1.81% | +5.14% |
| 半導體與晶片供應鏈 | 0.00 | 0/5 | 5 | -6.70% | +7.91% |
| 記憶體與 HBM 供應鏈 | 0.00 | 0/1 | 1 | -9.62% | +6.03% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：B104 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：B811 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-07-12 | 0.27 | 0.13 | +16.67% | 12 |
| 2026-07-13 | 0.39 | -0.09 | +15.38% | 13 |
| 2026-07-14 | 0.10 | -0.07 | +21.43% | 14 |
| 2026-07-15 | 0.20 | -0.16 | +28.57% | 7 |
| 2026-07-16 | 0.20 | 0.02 | +33.33% | 12 |
| 2026-07-17 | 0.36 | 0.02 | +60.00% | 15 |
| 2026-07-18 | 0.18 | 0.08 | +53.85% | 13 |
| 2026-07-19 | 0.37 | 0.09 | +12.50% | 16 |
| 2026-07-20 | -0.59 | 0.11 | +45.45% | 11 |
| 2026-07-21 | -0.12 | -0.03 | +12.50% | 8 |
| 2026-07-22 | -0.33 | -0.15 | +16.67% | 6 |
| 2026-07-23 | -0.01 | 0.01 | +41.67% | 12 |
| 2026-07-24 | -0.16 | 0.43 | +50.00% | 6 |
| 2026-07-25 | 0.30 | -0.06 | +12.50% | 16 |

## 歷史回測摘要

- 回測日期：2026-07-25
- 近5日 3日相關：0.04
- 近5日 5日相關：0.07
- 同向比例：+42.86%
- 權重狀態：未調整

- 方向準確度：+42.86%
- 信心排序準確度：0.04
- 診斷：低相關

調整原因：近 5 日有效樣本 7 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel rides AI boom to fastest revenue growth in almost 15 years, but shares sink - CNBC；Intel forecast crushes estimates as AI boom boosts chip demand; shares jump - Reuters；向台積電、三星招手建 2 奈米廠，以色列豪語打造「10 萬顆 GPU」巨型算力中心 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.59 | N/A | N/A | 92.32 | 114.68 | -19.50% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | +0.27 | -2.49% | +2.62% | 2,350.00 | 2,410.00 | -2.49% | 背離 | 74.39 | 31.59 | 442.68B TWD / 67.87% | 2026-07-01 |
| NVDA 輝達 | 產業/供應鏈推估 | +0.03 | -2.04% | +18.60% | 206.84 | 211.14 | -2.04% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.06 | N/A | N/A | 521.95 | 539.69 | -3.29% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 產業/供應鏈推估 | +0.02 | -2.81% | -24.67% | 381.70 | 506.69 | -24.67% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -14.52% | +23.40% | 381.92 | 446.77 | -14.52% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.02 | -3.16% | -0.16% | 613.00 | 680.00 | -9.85% | 背離 | 10.86 | 56.92 | 65.78B TWD / 32.86% | 2026-07-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.04 | +2.18% | +11.28% | 3,750.00 | 4,310.00 | -12.99% | 同向 | 62.91 | 59.76 | 58.01B TWD / 2.80% | 2026-07-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 2 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：growth, 成長。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 同時符合主題標籤：AI, advanced packaging, CoWoS, AI server。 方向判斷命中詞：growth, 成長。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：growth, 成長。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel rides AI boom to fastest revenue growth in almost 15 years, but shares sink - CNBC](https://news.google.com/rss/articles/CBMie0FVX3lxTE5OTVp5cW4xMmFTWkxNc1dUYkx0bFFYTGZhWURkWFNwT1NIcUxPUjVmb1dTU2hWcFBHd2dGVTA4alZFbDhDY0NScWJ4OVh0ZzVKRENFSW9CVkh4UTc0VGR3dEg4X1ZwSFhmZDhoLTNTRTdZY09XQWJuYlI4TdIBgAFBVV95cUxNUk9FT3hDOFlLV2xPYWFfMkx4M1JmT0wyYXVsMjhybnpNTUNqeURBS05CbGpqR1pmRlJJbElhM0R3SXJCOFd4SkRxdG5ZR0xCT1hteWVhTHh5dU9sSGNEdlgtalhIX1lVQ1VqZ1BTR0pnTTVmbXJMcUdHY2x0SDNhQw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 23 Jul 2026 20:03:07 GMT
- [Intel forecast crushes estimates as AI boom boosts chip demand; shares jump - Reuters](https://news.google.com/rss/articles/CBMivgFBVV95cUxNY1JRa3lMd0xIRC1RRGxjWWFMTmZqYmtPMnV1ZXlURS1KX0dQOFRRMXNhbDMwV0NieEhCYkc0QjNlVGlCSnE3OGYwZ1lUR1ZuTndhR2RBNVBxNnFnN043Z2NZM1BiemNBSUNvT3RRc1hSM0o5WjB0MTNkampodGcwSVFndUJwLWdaRXRHZHFKbzdNZFNNT245SHczYjdTX2NBVC0xNS1HcHc0Y1V6ZTFmQzMwcG1FR1NIUHVldlZn?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 23 Jul 2026 20:02:00 GMT
- [向台積電、三星招手建 2 奈米廠，以色列豪語打造「10 萬顆 GPU」巨型算力中心 - TechNews 科技新報](https://news.google.com/rss/articles/CBMilwFBVV95cUxNNXpjTUdOMVFNOS1MQzdQMS1McmdjNzNJdWtteEg1dEVaTHJLWHlSTlJqLU9GVGZkeGc2U2lGYWJoSjZwTE5RSDY1R0xFa09ZSnN5Z3NpWXhKTzhNSEVxXy1yMHA2SnZLQmxqNjNRS3poYmtTd2RDcEMyZXI2cE9yS0hjRmhnZ2hhMFZFbWhrNWc0QXRBdERz?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 24 Jul 2026 04:54:40 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：柏瑞投信：AI需求續強帶動供應鏈升溫，台股中長線動能仍可期 - MoneyDJ；AMD首款AI機櫃Helios下半年出貨、微軟宣布加入買家行列挑戰輝達霸權：從台積電先進製程到緯穎伺服器組裝，台美股受惠供應鏈與投資關鍵｜股市話題｜豐雲學堂2026 年 07 月 - sinotrade.com.tw；川普祭新關稅周五生效！60個經濟體遭課10%到12.5% 台灣適用稅率出爐 - news.cnyes.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.21 | -2.04% | +18.60% | 206.84 | 211.14 | -2.04% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 新聞直接提及 | +0.21 | -2.81% | -24.67% | 381.70 | 506.69 | -24.67% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | +0.21 | -2.49% | +2.62% | 2,350.00 | 2,410.00 | -2.49% | 背離 | 74.39 | 31.59 | 442.68B TWD / 67.87% | 2026-07-01 |
| 6669 緯穎 | 新聞直接提及 | +0.43 | +14.60% | +24.03% | 5,730.00 | 5,730.00 | 0.00% | 同向 | 298.31 | 19.21 | 111.37B TWD / 29.79% | 2026-07-01 |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +26.06% | +43.46% | 333.02 | 333.02 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | +2.64% | +7.91% | 252.50 | 289.00 | -12.63% | 不適用 | 14.13 | 17.93 | 821.76B TWD / 52.11% | 2026-07-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MSFT：新聞直接提及「微軟」，共 1 篇新聞命中。 方向判斷命中詞：受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 方向判斷命中詞：受惠。

### 主要來源

- [柏瑞投信：AI需求續強帶動供應鏈升溫，台股中長線動能仍可期 - MoneyDJ](https://news.google.com/rss/articles/CBMilwFBVV95cUxQREhHZEFYV1VLb3djcUViellUNXhQUzhvQzAzV2d0eTVBRkROZmxXX3g1ZElMdXdkTFV0bFJBRnJ3MDlyZHdBLXNLcFFYT1RDXzJ4LWtUcVNycmZWaUtvZ3l2Z1NFS2NXcE5RaEFGaHdRRjltNWE0SVcwOUNxelpQVFlvd3hkdFk0SkJ2T25RZ1ljaXVtSG5z?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 24 Jul 2026 06:00:00 GMT
- [AMD首款AI機櫃Helios下半年出貨、微軟宣布加入買家行列挑戰輝達霸權：從台積電先進製程到緯穎伺服器組裝，台美股受惠供應鏈與投資關鍵｜股市話題｜豐雲學堂2026 年 07 月 - sinotrade.com.tw](https://news.google.com/rss/articles/CBMiyAZBVV95cUxQMGZxaWxQSEJ2MUtZNTFRMjVIa09hSWJ4NDN4cDhrM3FlcE95bTdVNkxaeGpCZDEzaG1UOVVOSGZUNFFDOXZQQmhzamkwQlBnOXlDRDRlYnFqVkxnUzdqbTN4ZURNdkxqNHc2eUM5cGs4NnVFeUFndThHd0x1NlJ1ZkFReF9QTVpLRkN6YmM4ZVV5NjFmcUE4T3pzMGRXTjRvS1RyOFpLZS12dTM1dXNVMFZBNU8xOVU4YTNRQ1gxVHhYQy1oV3o3TllFSzBqU0EzcGx6TlFVYTg4Y0JSZ29PSURQZGFjTlhuY2dxeENPdGFHWjNqY2lxNjMzeDJHazN5OVdobTVIM1QxdGFncENURjM4NU8zdDNFMFVHOTc1RzNCWDk2WnkxemdaNERzSDRZeTJiV0doeGtIWDBLUjNpS01IUlVJdXBLQUFaQ2hwdUdRYzJoQzVQUnFkcDVrM2NaSjQ3SF9Uelk5WTFtV2dnOGNMMDcxVGFLUVVNNGg2bVhCd3NMajg5VDQzVU9GODBCT3J3Q19RSGg2M3VrVV9xbUlZaElWNHhmRlh6dkpYWmVJRnptSTlpcnF0enVad05KdlBsbXphMENlMmRKakw5N2d2VlJKdU9BcGFLaE5ENF9PSXlCdENwQTRkWUNZU3JLVVp4RzBnYkpkLUtldV84cFRDamNHN3VWVVFfRVQ5bUljTmttMnNFOWFabkhJQjgwaV84OHNiajliNmpmcjFhczRGb1BVV3pGZWwyNzRqMTBnb29LdW56VmFwSzR5N19kUjBrVGU5UjF4RGpIV3V5am5PWnBYaGgxTl9CajZYY0FtT2pqTWlyRHNRTV9LT19KTWV3dF85Y3NiY0pNUS1aTUI4bDFtemRxS3JibUhFUmN0SWFfZmsxZVBhWVF3NmttV0xuOVhJcVlIZmI2ck04MjZZWWEtem1SQVJkYjVxZXJiaWtWa3N4bUFndmh4QUFDSk5pY2I3RWExdHdsWWRQa3FMWVZWb2FQS09lWTlSQlk2NzhzWGJnOGpSaDZ3ekdXTW1VNThtOWdCSS1KcTA3b2tzNmNkY2ZqajJDUlVSLXVQSF81dFZBT0FHVzlySDJqZ1duSXBlaC0?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 24 Jul 2026 19:29:38 GMT
- [川普祭新關稅周五生效！60個經濟體遭課10%到12.5% 台灣適用稅率出爐 - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTE1pcFBxbklaaUU0NnJsV2xCYVdyZU91S21ldFNNMDJXZjFxTzBfdHdrYTk3NlREQmFRY1hnZkRvUUFiYnVLdHNWbGNCbWlxaHM?oc=5) - Google News source discovery | 鉅亨網 Fri, 24 Jul 2026 01:51:36 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel forecast crushes estimates as AI boom boosts chip demand; shares jump - Reuters；Intel Rises 3% on Q2 Earnings Beat, Upbeat Q3 Outlook as Chip Sector Stays Flat - 24/7 Wall St.；How the 'twin stars' of China, CXMT and YMTC, changed the chip game - Reuters

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.59 | N/A | N/A | 92.32 | 114.68 | -19.50% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.03 | -2.49% | +2.62% | 2,350.00 | 2,410.00 | -2.49% | 背離 | 74.39 | 31.59 | 442.68B TWD / 67.87% | 2026-07-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.03 | -4.83% | -11.11% | 128.00 | 164.50 | -22.19% | 背離 | 4.00 | 32.16 | 23.12B TWD / 22.85% | 2026-07-01 |
| NVDA 輝達 | 產業/供應鏈推估 | +0.02 | -2.04% | +18.60% | 206.84 | 211.14 | -2.04% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.04 | N/A | N/A | 521.95 | 539.69 | -3.29% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | +0.04 | N/A | N/A | 920.95 | 990.21 | -6.99% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.02 | -9.62% | +6.03% | 1,436.56 | 2,335.00 | -38.48% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -14.52% | +23.40% | 381.92 | 446.77 | -14.52% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：upbeat。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 3 篇新聞出現相關標籤。 方向判斷命中詞：upbeat。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 3 篇新聞出現相關標籤。 方向判斷命中詞：upbeat。

### 主要來源

- [Intel forecast crushes estimates as AI boom boosts chip demand; shares jump - Reuters](https://news.google.com/rss/articles/CBMivgFBVV95cUxNY1JRa3lMd0xIRC1RRGxjWWFMTmZqYmtPMnV1ZXlURS1KX0dQOFRRMXNhbDMwV0NieEhCYkc0QjNlVGlCSnE3OGYwZ1lUR1ZuTndhR2RBNVBxNnFnN043Z2NZM1BiemNBSUNvT3RRc1hSM0o5WjB0MTNkampodGcwSVFndUJwLWdaRXRHZHFKbzdNZFNNT245SHczYjdTX2NBVC0xNS1HcHc0Y1V6ZTFmQzMwcG1FR1NIUHVldlZn?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 23 Jul 2026 20:02:00 GMT
- [Intel Rises 3% on Q2 Earnings Beat, Upbeat Q3 Outlook as Chip Sector Stays Flat - 24/7 Wall St.](https://news.google.com/rss/articles/CBMivgFBVV95cUxQaUJQV2hra2c5UGd2OE9sMmpBX01KQVZVaFFoczllcFRKM2xyZ3ZtX1ZZclpxNlBiRnNGOVlzcEs4Q3pKclEzSG9VVmZOMWhnMzg4U0lGdWNFRkVVSzNkaVFYU0tqZHpWNGFMeGZkYXJFZjdnNzdDU1BuVThsWmZTNGlXUG5WUUp4TU1tRThGMkZ4VTFVMmh1NDhfVnpReGkzNEZTM2ZPRWdJZVJZZm4wajlTeVJHWUtLM0RSWjJn?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 24 Jul 2026 13:16:15 GMT
- [How the 'twin stars' of China, CXMT and YMTC, changed the chip game - Reuters](https://news.google.com/rss/articles/CBMirAFBVV95cUxPN3FtZ0tuZjBLVXBGemNjdHZlRFVaMUhXSHNuaWpfZnUxSk9PVVQtVldLNjNXSENkREV4UUZYdmN3dXE0RGk2d3poSzduX3UzM09JUURZMG5SQjZxeExscERSZ21SS1ptQUpWR3ROaXFGVlNnR3dWeDROc2Z4emx0NlU3dE5uMVp0aXM1SzJEdWJudVZoMFB6YnMwU2czOVBfaVBJTGhNcDBzUERo?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 24 Jul 2026 05:04:00 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Chip Stocks Slide Friday—Memory Favorites Micron, Sandisk Among the Big Decliners - Investopedia；INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits；Micron, SanDisk Stock Rout Looks Ugly — This New ETF Thinks That’s Perfect - Benzinga

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.50 | N/A | N/A | 920.95 | 990.21 | -6.99% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.25 | -9.62% | +6.03% | 1,436.56 | 2,335.00 | -38.48% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.37 | N/A | N/A | 521.95 | 539.69 | -3.29% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.37 | N/A | N/A | 92.32 | 114.68 | -19.50% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -2.04% | +18.60% | 206.84 | 211.14 | -2.04% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、MU」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 4 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Chip Stocks Slide Friday—Memory Favorites Micron, Sandisk Among the Big Decliners - Investopedia](https://news.google.com/rss/articles/CBMizgFBVV95cUxQMERJdk5WWmVGU2tpVHdoN0IzMHY1c0JPZGVySmp5ZWdoeTVvSlBUYnR0Vmx0WS03UlRDSUdtMUh4ejd0VVkzaWR1WXpXRE5EWlVhekROTXA3U2c0TEJvS0RVYWFPLTRNZ1ZhVGRCT1Z3LW5oVnpSeE1id180cTFIX1pRYzE4d3F6eDM2RHFlZGFjMlBrVmJrRW40MXRPd3Q0NTA4WkNLR3FVU2ljcmp5TTNLbjNsV3NKU2YxMHB3X2NfUk50eFpZY2pCaUd4dw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 24 Jul 2026 17:10:48 GMT
- [INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits](https://news.google.com/rss/articles/CBMi0AFBVV95cUxOWm5KdEIwSXpyY191UEhDa1V6NVpWa01UbmpJeWRIV0ttT080TmpDNEhISW5TWkQwUzBVYzBqSHJPWXRVNVJCampoWWRlYmhKVkhIeHBJLS0wLW5Ua09GQnRORXpFcW5qTEJkcnJGcW55aU5rOFVOLUFMbjRPZEpWT3A2ZllucnM0SU9JNEdrNUwyc3V2WHAtNFk3VHl4R1F6SkZRMFpleEE2Zl9MdW4tSEpMMnFGZ2hQZURWQ3B1WDlPR1BhRjJELVN5ODJWYVR3?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 24 Jul 2026 07:21:22 GMT
- [Micron, SanDisk Stock Rout Looks Ugly — This New ETF Thinks That’s Perfect - Benzinga](https://news.google.com/rss/articles/CBMiswFBVV95cUxQaXJYNm1oRllubk9wc0NmM2VHSG9jUVZyNlN6TDRYMmRWbHlDR2xrZThnLWdLRXZBazlZMzhwMW1EVVZMQ3MxUkR0OGxXeHdyTmZkYmhlVTZoZ1dEeE1CYm1KcGpRN0FkWHNzSnJfdXBSam4tMlJydVo3WG12YTNLMjJ0aXBlS3pFOTkyWXZ4X3N1bGlGbUhoMGVyT1pPdmpHeTBOYVV3VXZUUEQzbWlGWUlVbw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 24 Jul 2026 12:51:32 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股跌千點 法人喊一線「升」機 只要下周一站回季線 就有底氣挑戰45,171 - 經濟日報；10檔三強優勢股 法人卡位 | 市場焦點 | 證券 - 經濟日報；台股跌327點失守37000點 首見「雙萬金」紀錄 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股跌千點 法人喊一線「升」機 只要下周一站回季線 就有底氣挑戰45,171 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9lOWxzNTk2dVNvakxxbDdXYjJkSWdMUXdrLUpOdXRiZmFyTU5zSUdYQTlLbnVlbk1SLVJHaHlRZzB3ZF91N3VlSm1tam1HMV95dWhCM0JHRWNqQdIBX0FVX3lxTFBzemVpWmxwYUtiZ2w3MzItTzNleWZXZWYxblFJeGFLaXlKWGFvVWR4b0NaYUctTTRwclBhblpqQ3hkN3hmaGdHdWRPSlpoY3BsRWZQUDhELUxrSzQtWDNB?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 24 Jul 2026 16:34:49 GMT
- [10檔三強優勢股 法人卡位 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMidkFVX3lxTE9nU0V0dUt4VW9jTnY2RFRoYWlUbTFWTFhmZ0lUX2lFWGIwQTNlV0wwbUJfTWg0UndJOTJ1VDRJTjJtRGJBMmJEaDJidkUxZlE4aG5zTFBWMndCcHFjUjk4TDdhRHFvWjVvcXlkTVVXTDhXSXVWbWc?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 24 Jul 2026 15:36:32 GMT
- [台股跌327點失守37000點 首見「雙萬金」紀錄 - 經濟日報](https://news.google.com/rss/articles/CBMif0FVX3lxTE1KZEY0NFk2LWdBUVdUWnhJQklBZDJuSVdJSjNremp4OE53LXg0S2Z0TXZKcS1hMmpsRGJ2OXRMNFFOdmY1MEpRS3QzdDdzd1pZNUZ3bGVtcTNDR0hyZm9Ubm9fNHVFWnRjdm96YWNtRklJckp4LTVISm5veWtxMDjSAV9BVV95cUxQaWljRmNCbjJCTk5DaVBrUWdBSnpCZGk5MkIzalFNSU5sai1yYXozeHN5MDlrdnNHT3dubmFXZEVJaFRpeHFkbkNpUmZIdzBSeU12ZjNxYlJpRkM0b3hDdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 24 Jul 2026 13:00:04 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》大跌1195點、10日線又失守；週K翻紅-新聞內容-基金 - MoneyDJ；‧永豐期貨盤後分析 - MoneyDJ；個股動態報導內容-9607B820-B104-44F6-9A98-BC07985F3E0A - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》大跌1195點、10日線又失守；週K翻紅-新聞內容-基金 - MoneyDJ](https://news.google.com/rss/articles/CBMikwFBVV95cUxPOWsxX3JGYzVxUm1TZ1lnZnVjVGV6eGdRblFIRmdKRkNuMjVCemxBS01BWkpNT3RGaDdHTm9tNDB3ZGJoM1QyS1BTbW93ODI4QmU5MWd1Y2dRSV9Ddnl3RjdqT3RqZmQxdGI0bXI2VnNqLTNJSW1kZWhIWm53SDhjamV0a2tCT1RQVVZXNzV5alVMT28?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 24 Jul 2026 08:09:00 GMT
- [‧永豐期貨盤後分析 - MoneyDJ](https://news.google.com/rss/articles/CBMijgFBVV95cUxPQWZrZ1UwQ1JXQzVTZk9Qclg5UFBXX1BPMVRrZWZDOVQ3WkhTN3ZRLTNKYm5abVE3N1VwOVhRLVBrdVA2Mk0wekJsU0tydkJwdU9EcndmRjBmYzRid0Y0Z2x3Ri1EY3ZpdmJfMHZGRzFpeENoY2JSRE9iSGtZb0dSSTJKbkVmaXlXQi1hQWNB?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 24 Jul 2026 09:05:20 GMT
- [個股動態報導內容-9607B820-B104-44F6-9A98-BC07985F3E0A - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxOcWdNSl9jNGxsdTk0dHNIeHYtRml0blRBVnl4TGZGQ2x0bXJUczd1aWhCN0JyZDhDRUQ3N2dSay04alNtb1dPN0ZwVDBHOThRYmJKckJhVGQ3U3dpQ2NwMnBzNGkxMlZnS3gtWXlJbVZXTjVndkNlVG5VMTBmM3MwZEZWd1pCS0RoXzh1TmswNE5iS0E2?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 24 Jul 2026 11:10:09 GMT

## 新興題材：B104

摘要：新興題材：B104 相關新聞集中在：個股動態報導內容-9607B820-B104-44F6-9A98-BC07985F3E0A - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-9607B820-B104-44F6-9A98-BC07985F3E0A - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxOcWdNSl9jNGxsdTk0dHNIeHYtRml0blRBVnl4TGZGQ2x0bXJUczd1aWhCN0JyZDhDRUQ3N2dSay04alNtb1dPN0ZwVDBHOThRYmJKckJhVGQ3U3dpQ2NwMnBzNGkxMlZnS3gtWXlJbVZXTjVndkNlVG5VMTBmM3MwZEZWd1pCS0RoXzh1TmswNE5iS0E2?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 24 Jul 2026 11:10:09 GMT

## 新興題材：B811

摘要：新興題材：B811 相關新聞集中在：個股動態報導內容-3B25EB17-76F8-44E3-B811-077E0F4F69A2 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-3B25EB17-76F8-44E3-B811-077E0F4F69A2 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxQZ05WcUdubDh2YU0wVGx2UE9BYnBocU1heHg5b3p6Y0JoYzQwLWdLc2J3TUtGenRWcmNVS1NEbElNVlgzeFdEYlRNcVRTbS1GbmVWdmNOd0xaSlJ3T1RnR2hYeE9mSU9FVlFPMWEzb3BXdHZ1QjlaemwzanZTV3c2ci1JeS02VnRLcjF4TzZ6WXB2NVNB?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 24 Jul 2026 11:10:38 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
