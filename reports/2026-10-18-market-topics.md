# 每日股市熱門話題分析 - 2026-10-18

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **新興題材：MoneyDJ**｜中性｜熱度 5｜市場確認 N/A｜同向 0/0
2. **先進封裝與 CoPoS**｜正向｜熱度 2｜市場確認 N/A｜同向 0/0
3. **半導體與晶片供應鏈**｜正向｜熱度 7｜市場確認 0.00｜同向 1/8
4. **AI 伺服器與資料中心**｜正向｜熱度 9｜市場確認 4.69｜同向 2/8
5. **關稅與供應鏈轉移**｜正向｜熱度 2｜市場確認 18.39｜同向 1/3

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.12（樣本 23）
- 5日相關係數：0.33（樣本 15）
- 同向比例：5/23

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 先進封裝與 CoPoS | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | 0.00 | 1/8 | 7 | -8.01% | -7.75% |
| AI 伺服器與資料中心 | 4.69 | 2/8 | 6 | -4.27% | -3.79% |
| 關稅與供應鏈轉移 | 18.39 | 1/3 | 2 | -1.65% | -3.55% |
| 記憶體與 HBM 供應鏈 | 0.00 | 1/4 | 3 | -10.26% | -17.86% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：CoreWeave | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價呈負相關；應檢查正負向詞庫，並降低新聞直接提及但股價背離的權重。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-10-05 | -0.16 | 0.29 | +73.33% | 15 |
| 2026-10-06 | -0.72 | -0.75 | +37.50% | 8 |
| 2026-10-07 | 0.48 | 0.61 | +73.33% | 15 |
| 2026-10-08 | 0.13 | 0.40 | +58.33% | 12 |
| 2026-10-09 | -0.03 | 0.37 | +38.89% | 18 |
| 2026-10-10 | -0.28 | -0.96 | +57.14% | 7 |
| 2026-10-11 | 0.66 | -0.74 | +40.00% | 5 |
| 2026-10-12 | -0.08 | -0.07 | +41.67% | 12 |
| 2026-10-13 | -0.05 | -0.03 | +46.67% | 15 |
| 2026-10-14 | 0.08 | -0.29 | +57.14% | 14 |
| 2026-10-15 | -0.08 | 0.08 | +33.33% | 12 |
| 2026-10-16 | -0.13 | -0.25 | +64.00% | 25 |
| 2026-10-17 | -0.10 | 0.49 | +26.32% | 19 |
| 2026-10-18 | -0.12 | 0.33 | +21.74% | 23 |

## 歷史回測摘要

- 回測日期：2026-10-18
- 近5日 3日相關：0.33
- 近5日 5日相關：0.44
- 同向比例：+44.44%
- 權重狀態：未調整

- 方向準確度：+44.44%
- 信心排序準確度：0.33
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

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：第一金台股趨勢優選主動式ETF基金九月份經理人評論 - MoneyDJ；錢進你家1／台股大跳水台積電攻3,000元再等等 資深分析師曝關鍵時間點 - MoneyDJ；獲利支撐台股中長線多頭行情- 新聞 - MoneyDJ

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | 0.00 | -2.81% | -5.10% | 2,420.00 | 2,480.00 | -2.42% | 不適用 | 86.28 | 28.05 | 511.86B TWD / 54.65% | 2026-10-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。

### 主要來源

- [第一金台股趨勢優選主動式ETF基金九月份經理人評論 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxQWlprZGpjaUJHSEtUZUtUUFJ4SWlZelhaMVV5cC1NM3RYWFp2Qno0dVVzT2RyaHNEekN0LTYxS1BUVU1USnlzV0swVGlLZlhOWUpTT1FLQ2UtcnZoWnROVWVOWWhoVXBVYnpqeHB4V2JSZE1HWHREOW03MktVeHhoZjl4Vnl2OUxwVlFaVGN2RTk?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 16 Oct 2026 07:58:00 GMT
- [錢進你家1／台股大跳水台積電攻3,000元再等等 資深分析師曝關鍵時間點 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQRlRuS1ZXSWxFUm1WdnZWbDRILTdYV3BnMnYxTWRXYlpFZ21TYWNmZTlZcV9zanl4X3RvTnF0UDlvWUZxd05WNU9iOFA5NzJOLTlCVENOSHM3RXRGck5ieVkwanJRcGVjR1dnb0Q5Ti1uQ2xzSmlIaDJQQ05fNVQtOXpJV1d1UkU3dXprTzA3VkNVUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 16 Oct 2026 00:40:00 GMT
- [獲利支撐台股中長線多頭行情- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMieEFVX3lxTE5zb1ByZ054cjZhRndOSTFMS2FudzFFX1Ywd0ljS2ZhUG5Xc0d2cGNWN3ZNUnFZZHZoTm1uSlVxdzdiT3huZmlKYkxsY3IxTUJBN3lUS0NIcE91UmZqOE52RTdWV2xhbWRHSF8zN2l6U1lJTTJwRlRiRg?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 17 Oct 2026 02:10:00 GMT

## 先進封裝與 CoPoS

摘要：先進封裝與 CoPoS 相關新聞集中在：布局先進封裝對友達毛利提升有何實質助益？ - TechNews 科技新報；先進封裝躍升，哪些設備商受惠？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -2.81% | -5.10% | 2,420.00 | 2,480.00 | -2.42% | 不適用 | 86.28 | 28.05 | 511.86B TWD / 54.65% | 2026-10-01 |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | -9.32% | -9.81% | 671.00 | 703.00 | -4.55% | 不適用 | 13.92 | 48.55 | 88.13B TWD / 45.52% | 2026-10-01 |

關聯理由（前 3）：
- 2330：產業/供應鏈推估：公司標籤符合「先進封裝與 CoPoS」關鍵字 advanced packaging, CoWoS, CoPoS, FOPLP；其中 0 篇新聞出現相關標籤。
- 3711：產業/供應鏈推估：公司標籤符合「先進封裝與 CoPoS」關鍵字 advanced packaging, CoPoS, FOPLP, panel-level packaging；其中 0 篇新聞出現相關標籤。

### 主要來源

- [布局先進封裝對友達毛利提升有何實質助益？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiXkFVX3lxTFAyUG11WEtDSmE3M2llZUpOakNXcTdwQWlTTUlPV2haRXVsX0ZtZE1uY1ZVZE1JODg5YlotTzJ3Mm5oUkdtOXpkQ2g1TjdoVFFDR1pPU1ZSWmVBMTJFM1E?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 17 Oct 2026 13:34:46 GMT
- [先進封裝躍升，哪些設備商受惠？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMihgFBVV95cUxOYUV5bTZ3MGNNeUZETXNCdXZUOU1PWVF4Tng3cExQdUplOGhzYjg3eEZWYjktTjQxa3RrbkR6WE5aWU1Fb0toTzFIS0duTk0xOGFYOW1CdG5pV0pnaTRhVnYzb2FnNjh1NThHdjAzdFlBbEJndUpCOEE0Y2FMVXdYeVEyZDFHUQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 17 Oct 2026 11:19:03 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel and AMD Drop 3% as Rotation Out of AI Chip Stocks Continues; NVIDIA Holds Steady - Yahoo Finance；Intel and AMD Drop 3% as Rotation Out of AI Chip Stocks Continues; NVIDIA Holds Steady - 24/7 Wall St.；寬能隙半導體結合矽光子 國際論壇聚焦AI時代產業新契機 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.29 | -21.65% | N/A | 89.85 | 114.68 | -21.65% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.28 | -3.01% | +7.02% | 214.13 | 228.38 | -6.24% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.57 | +2.45% | N/A | 528.75 | 528.75 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.03 | -2.81% | -5.10% | 2,420.00 | 2,480.00 | -2.42% | 背離 | 86.28 | 28.05 | 511.86B TWD / 54.65% | 2026-10-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.03 | -6.01% | -9.83% | 133.00 | 164.50 | -19.15% | 背離 | 6.68 | 20.00 | 25.35B TWD / 27.22% | 2026-10-01 |
| MU 美光 | 產業/供應鏈推估 | +0.02 | -9.49% | N/A | 878.84 | 971.00 | -9.49% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.02 | -12.35% | -17.86% | 1,299.30 | 2,335.00 | -44.36% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -11.23% | -12.97% | 328.75 | 446.77 | -26.42% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel and AMD Drop 3% as Rotation Out of AI Chip Stocks Continues; NVIDIA Holds Steady - Yahoo Finance](https://news.google.com/rss/articles/CBMilAFBVV95cUxNN0N5M25IMWs2NDBOYkgxTURwWjYxZDlzb191dENkZ0I2cUpFWFZCd1RueW5oaWlnZW95NXlkaDZWcXMzYTJXRjZyNDVJWkJNeGpYb1h0b1AyUncxblp2Ul9ocFlFSElZZTBiLXJtSlJDYkVLYWxRcmdZMDAtVjlweHJJQ2tJbXBVckxvQ3ZjMl84aHND?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 16 Oct 2026 14:54:02 GMT
- [Intel and AMD Drop 3% as Rotation Out of AI Chip Stocks Continues; NVIDIA Holds Steady - 24/7 Wall St.](https://news.google.com/rss/articles/CBMixwFBVV95cUxOYkx0cUlYODFLcFU1VmZRLThzT01WVVlib1hPV0NvTmJYTnhzbFZjZTNpelZjdDd0ZEZmWGNLVE5xYTVHWWhYS2JaNklfQ3hnMGVPRVJCVTlBOFJSQ1hFTXBjWmZMdDdzZ1dWS2ZtOE14SWxFMmJTeU82YmhWVjlMQ1BxN3B6MGNjTkxVa21tTnViRmxXSDZMZEhtZWVpbVRCOFVTM2VDUS0tS05vT1o1d1NPYW41VV9YMjhJellwSjh3dGQ5Mk5j?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 16 Oct 2026 14:54:00 GMT
- [寬能隙半導體結合矽光子 國際論壇聚焦AI時代產業新契機 - 中央社 CNA](https://news.google.com/rss/articles/CBMiVkFVX3lxTE92am1HalVjaml5Y0FjeFMycjNhMkJxeDNOdC1XNmlMYmpTcG00eTgzMGltZHMzUUd4QVNDdFV6SUFnNndQXzRueElqbWdoMjc3RlJ6RVV3?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 16 Oct 2026 07:47:58 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel and AMD Drop 3% as Rotation Out of AI Chip Stocks Continues; NVIDIA Holds Steady - Yahoo Finance；Intel and AMD Drop 3% as Rotation Out of AI Chip Stocks Continues; NVIDIA Holds Steady - 24/7 Wall St.；Agentic AI 轉型面臨哪些挑戰？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.29 | -3.01% | +7.02% | 214.13 | 228.38 | -6.24% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.29 | -21.65% | N/A | 89.85 | 114.68 | -21.65% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.59 | +2.45% | N/A | 528.75 | 528.75 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.03 | -2.81% | -5.10% | 2,420.00 | 2,480.00 | -2.42% | 背離 | 86.28 | 28.05 | 511.86B TWD / 54.65% | 2026-10-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | +17.50% | +7.53% | 529.05 | 529.05 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -11.23% | -12.97% | 328.75 | 446.77 | -26.42% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.02 | -9.32% | -9.81% | 671.00 | 703.00 | -4.55% | 背離 | 13.92 | 48.55 | 88.13B TWD / 45.52% | 2026-10-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.02 | -6.08% | -9.38% | 4,250.00 | 4,920.00 | -13.62% | 背離 | 60.69 | 70.19 | 55.40B TWD / 1.97% | 2026-10-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 2 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。 方向判斷命中詞：boost, fuels。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 2 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：boost, fuels。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。 方向判斷命中詞：boost, fuels。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel and AMD Drop 3% as Rotation Out of AI Chip Stocks Continues; NVIDIA Holds Steady - Yahoo Finance](https://news.google.com/rss/articles/CBMilAFBVV95cUxNN0N5M25IMWs2NDBOYkgxTURwWjYxZDlzb191dENkZ0I2cUpFWFZCd1RueW5oaWlnZW95NXlkaDZWcXMzYTJXRjZyNDVJWkJNeGpYb1h0b1AyUncxblp2Ul9ocFlFSElZZTBiLXJtSlJDYkVLYWxRcmdZMDAtVjlweHJJQ2tJbXBVckxvQ3ZjMl84aHND?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 16 Oct 2026 14:54:02 GMT
- [Intel and AMD Drop 3% as Rotation Out of AI Chip Stocks Continues; NVIDIA Holds Steady - 24/7 Wall St.](https://news.google.com/rss/articles/CBMixwFBVV95cUxOYkx0cUlYODFLcFU1VmZRLThzT01WVVlib1hPV0NvTmJYTnhzbFZjZTNpelZjdDd0ZEZmWGNLVE5xYTVHWWhYS2JaNklfQ3hnMGVPRVJCVTlBOFJSQ1hFTXBjWmZMdDdzZ1dWS2ZtOE14SWxFMmJTeU82YmhWVjlMQ1BxN3B6MGNjTkxVa21tTnViRmxXSDZMZEhtZWVpbVRCOFVTM2VDUS0tS05vT1o1d1NPYW41VV9YMjhJellwSjh3dGQ5Mk5j?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 16 Oct 2026 14:54:00 GMT
- [Agentic AI 轉型面臨哪些挑戰？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMi1gFBVV95cUxQUWthVy14R00xTEpJZm5uVmZxNHNnRlpoUlk1Sk1FRFRWN1NVSzNXVHAwTUU2blRoMG10VW00alRQazJvTndKRlVNU0VoMVpYTFlCS1UzT3lYdjRfTWppakI1SXpwSDloU2RRbWtVRWxJRlM4UVhPbGhVa2t2NUU3SmZFWmFsNjltTXlTVUd4dTlJdm5pelFwN09pRWR3bDZZbVVRbERyZmpvaFhoaVp0UXJZTmFTaDB4ZGxQM0VZQVByc3BFRzQ3MEpqcDVpb3p5Y2NOVXhB?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 17 Oct 2026 18:20:35 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：整理包／黃仁勳概念股笑了！輝達季度財報超預期 完整台廠供應鏈名單、潛在受惠股一次看 - 經濟日報；0056最後買進日別錯過鴻海法說先行AI供應鏈最關注這件事特斯拉、Meta Q3財報雙重出爐台灣AI供應鏈跟著動中油凍漲護車主｜投資早知道 - Yahoo股市

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2317 鴻海 | 新聞直接提及 | +0.46 | +1.67% | -2.01% | 244.00 | 289.00 | -15.57% | 同向 | 15.21 | 16.08 | 1158.63B TWD / 38.42% | 2026-10-01 |
| NVDA 輝達 | 新聞直接提及 | +0.21 | -3.01% | +7.02% | 214.13 | 228.38 | -6.24% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| TSLA 特斯拉 | 新聞直接提及 | +0.21 | -3.60% | -15.66% | 354.72 | 456.56 | -22.31% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +10.06% | +23.17% | 343.46 | 343.46 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 2317：新聞直接提及「鴻海」，共 1 篇新聞命中。 同時符合主題標籤：supply chain, tariff。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- TSLA：新聞直接提及「特斯拉」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [整理包／黃仁勳概念股笑了！輝達季度財報超預期 完整台廠供應鏈名單、潛在受惠股一次看 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBQUlViSHpPeDVlY29yaHFNNE5NcVlUQnE3ZThTcXRGNHgxYTVPOVVTRDlaTDV6Zml5WEwxVHNSeGFDcnVHUHhRSW15SzNpU0dYVDU3dThWNEVCbkZI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 16 Oct 2026 09:00:00 GMT
- [0056最後買進日別錯過鴻海法說先行AI供應鏈最關注這件事特斯拉、Meta Q3財報雙重出爐台灣AI供應鏈跟著動中油凍漲護車主｜投資早知道 - Yahoo股市](https://news.google.com/rss/articles/CBMi_AVBVV95cUxNckdQWTVuTmF2Mnk3dXpEOThpNnM1ODNtc3NSNWFPeExkdDNaQ3pGZjJVNGJiT3NwREMtbnhUREg5d2g5dEtKYXdXZnZBRWJqTXcwa2YtbFZ2Z0pqcEI0Z2JOamJnVHNVUEFBdkxvWWgwY2FpZlJ3dXhQLWVXaElhZUpYWG1SZ2llVV92MzdXY0xMOTdldzg2ZW5POTJueVdlcGVOUDhLTXhfTThIMjZmT2dzdWx5cmpjNHhNbGx5dDUzYkJ2VmtxUk9CbmZwclh2Ym0waGQxOTJPandPS0p2V3A4R3ZfQVRpTE1RdzBIOHc0NWE2OE9NWmtkSVZWc1VlWlROQ3Z0MHQtMHJqZkZhS3J0MEJEVlpFeHR0WTR2by1BbUdKUzU3MUpOcVZOcHA4WEZFRnN6eDlwNW51SmZzcXl5ZWpqRUhzN3dxbmFrTFRqTXV2RDJLTFN4SlBXYzFuVl9RYmNTTnR4elVQYy1fUFpDZURJSFZRQ2tzSUxDTmRlWGxrSi0xVmpvY1N5VGRRUEF5c00xdW9WdjVJRUhUcjhKdEw3OWNfMlNON09JRm1rSlVrd1I2aWE0ekJoMUdOWWJ6VHBkNWN6eWhWc1JjRzFVbGxzamw5dElrXzVpc1BuUVBrV3dhUE0tYnh0a0hsU3UxemZqRWU2NVY5eE9jQnlJNXM4ZElyVkJFVFhpY3h1Yl8zUEp2N1FtdUwzNmdBZzk5eHUwaHdWNEk3RFhaRlVyTGx5WWEteWpVcTZoOVpTZjBPMG51VkllUmNlLWVLQ2pNOXBlTnlwUFM0WDBONThFY2RiVjF2cmotejFkUTFQLUljSk8yOVdzSklSc2RvQ2dqSmsyS24zdnN2QWJTazJNT2dDMHpISTdFV2phTkxzR29ReFpDYVA2UUFQNHE2UWw3bi00NVMzQnNsNnVyb3NibjE2UFZtV2RqUkN5ajBQWW95X1ZqRXRzSnBKeEtnaHF4Yi1IZy1OekxFVjRvQ3duSklVU3MtRURhaA?oc=5) - Google News source discovery | Yahoo 奇摩股市 Sat, 17 Oct 2026 15:07:13 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits；SK Hynix, SanDisk, and Micron Drop 3% Despite Goldman Sachs Calling China Chip Fears Overdone - 24/7 Wall St.；Micron and Sandisk Have a History of Cyclicality. Is This Time Different? - The Globe and Mail

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.29 | -9.49% | N/A | 878.84 | 971.00 | -9.49% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.29 | -12.35% | -17.86% | 1,299.30 | 2,335.00 | -44.36% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.43 | +2.45% | N/A | 528.75 | 528.75 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.21 | -21.65% | N/A | 89.85 | 114.68 | -21.65% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -3.01% | +7.02% | 214.13 | 228.38 | -6.24% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk、SSD」，共 4 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits](https://news.google.com/rss/articles/CBMi0AFBVV95cUxOWm5KdEIwSXpyY191UEhDa1V6NVpWa01UbmpJeWRIV0ttT080TmpDNEhISW5TWkQwUzBVYzBqSHJPWXRVNVJCampoWWRlYmhKVkhIeHBJLS0wLW5Ua09GQnRORXpFcW5qTEJkcnJGcW55aU5rOFVOLUFMbjRPZEpWT3A2ZllucnM0SU9JNEdrNUwyc3V2WHAtNFk3VHl4R1F6SkZRMFpleEE2Zl9MdW4tSEpMMnFGZ2hQZURWQ3B1WDlPR1BhRjJELVN5ODJWYVR3?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 16 Oct 2026 17:48:56 GMT
- [SK Hynix, SanDisk, and Micron Drop 3% Despite Goldman Sachs Calling China Chip Fears Overdone - 24/7 Wall St.](https://news.google.com/rss/articles/CBMizwFBVV95cUxQQ1ZZZTY4bmhPSzZ1cjV0WllQWGZOVTRMN2t3emE5blRHUHNTekFGelpNZ2ZZU2lHUmRDTE4tYzZPeVZiVWxpTVVUaURYeE5XQWNyM2pQNlg2LTFGMkpnVmVNM19IcDR1VUdvQ0IzWnU1bFk4aFp0ZGYxVjFWR2hiTkxmUndGUzl1MEZmSm52TE5jTE9pNU1JZEYyMnJSaUIxTXJlb2RSUnZXMzZwM2NkcUNBSkJoQWhYaXcyNnpFcDhveTlVTGVIb25rR3h6WnM?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 16 Oct 2026 13:30:00 GMT
- [Micron and Sandisk Have a History of Cyclicality. Is This Time Different? - The Globe and Mail](https://news.google.com/rss/articles/CBMi7AFBVV95cUxQTHlPZElPTHJpRU84dWVxb1hocG1pcDhWaldXeUdZbi1QUXNkSUh5U2N4ZG1ydEdZMWMtZDE5Zk1SQTZTUFlrWW9ndTIyQXpmallqQmxjY18yOVJCb0g3clNCbmdWbUJ5ZGxRWjF0aTZJeG1oVVI2ZnFQME5aUEpTckdjMFVOOUY1c2tIZUZfV3J4VDNlZU5jN1puZTBDYk14N3B3cmNWcTdmcWxxTUd4aUpkVG5UeFZiYnlBcWMwUHVNTFNHZEZQVWxnMkEtenRyeE5TVmRkbEsySGx6bW5iQVI3SlN6RXMtdTJBSg?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 16 Oct 2026 22:31:12 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：個股動態報導內容-41075C53-B2FE-4C21-AFA3-8C48D48DDD63 - MoneyDJ理財網；個股動態報導內容-D471358E-8DED-46A7-8DFD-48F718BCA389 - MoneyDJ理財網；個股動態報導內容-553FD7D7-AFE8-403E-BF9D-2501C68EC366 - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-41075C53-B2FE-4C21-AFA3-8C48D48DDD63 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilAFBVV95cUxNcUxKcnVyVW5jd0daNTFjbEJBZkV6WHJ5dXQyRGU4RmlqanNrc05RTkhDS1BadlV4bWVZbGlvWi1hWWlVeTB4MXkzYkdobUk2aWcwa2RYWXhjWjQ2c3dXS2N0bWticmRveWNlcnpwWUF4NVZnMHAxZUUybV9vd1YwRXJQbDlhaHB5QnU5UUNXU1R2Wkw3?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 17 Oct 2026 05:55:55 GMT
- [個股動態報導內容-D471358E-8DED-46A7-8DFD-48F718BCA389 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilAFBVV95cUxNMUNBUmF6TlNhTFhYMHZLeDZKOE12RmliOUNjZWhQRjdNckQ4VEpUdnAtaGJ5NDZ0dkRsUm9TSHRVeWtvQndwaS1TbFdLUm9zcHJpRVdsSG04b3J1YzlGc0M0SHpVVFZpUzZEWU5wQnJsZDhHNEhpUHJVeGdob2c1ZVJ6Mnc0UTlVbHFMdGJWWm9BOXJs?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 16 Oct 2026 15:48:46 GMT
- [個股動態報導內容-553FD7D7-AFE8-403E-BF9D-2501C68EC366 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilAFBVV95cUxORVkzTHBlb3YyaHNZelpHR3ZhSTNfZ3MzMnd3MGt2WWNfWW93eWxZR3RLNVdHcmVQOFJVT0RFYkNyS09XV0ZBbG9OLW5lMzVjQzh2NGVQWUpCT1k0Y3B6N1R2bG9laDNzeDR2d0JSbkZOM0lOSWU0VTNoRS12bXprMXN6MnJuZkFYZjZjX1N0R3J3SDlN?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 16 Oct 2026 15:23:44 GMT

## 新興題材：CoreWeave

摘要：新興題材：CoreWeave 相關新聞集中在：Why CoreWeave is in the crosshairs of the AI scare - Reuters；CoreWeave bond rout tests market's math on AI buildout - Reuters

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [Why CoreWeave is in the crosshairs of the AI scare - Reuters](https://news.google.com/rss/articles/CBMilwFBVV95cUxOWDBmSEI4THQ5MFFtQXA5a1YweUdtQ2RIYXJXU0t0SFpiQ2kzbENpUWpVbW9hRU5KY1FiMkZPdDVOcmY3OW5WTVRqTFo1SnZKQmxweEFXeVhkY0ZySUdjQWVoV2p3TEVlbXVSSVBZTnNVbXdNc2Q1bmpzSVFrYXFtTmVhUloyaDRqeHp0NllQZWxDTHFENXhv?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 16 Oct 2026 17:51:43 GMT
- [CoreWeave bond rout tests market's math on AI buildout - Reuters](https://news.google.com/rss/articles/CBMiqgFBVV95cUxOdm5VTll1VmRrVEdWNm9HMmh4dUtxaDN2alV3YnJxUmtZdVJjZV9obW5Kc2tOYTNEQVdQNE1XMnFNbk1PaFBTTHZqcWxFZklDOVRtYm9IOWhnMjRuZTYyM2U0NVA1WmY0a3ZGQTFJbFp5cU1ha3h2WXBwLVFBSmtjRnVmZm8xdUtCMWlaX1YyUkpCSDhZamRzRG9UV3paVU9MalVpa0FFbzRBZw?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 16 Oct 2026 16:48:32 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
