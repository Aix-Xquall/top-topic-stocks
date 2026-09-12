# 每日股市熱門話題分析 - 2026-09-13

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **利率與成長股估值**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0
2. **新興題材：MoneyDJ**｜負向｜熱度 7｜市場確認 38.63｜同向 1/2
3. **新興題材：DeepSeek**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
4. **AI 伺服器與資料中心**｜正向｜熱度 13｜市場確認 16.19｜同向 2/8
5. **半導體與晶片供應鏈**｜正向｜熱度 8｜市場確認 0.00｜同向 0/1

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.42（樣本 17）
- 5日相關係數：-0.14（樣本 11）
- 同向比例：3/17

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | 38.63 | 1/2 | 0 | +1.21% | 0.00% |
| 新興題材：DeepSeek | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 16.19 | 2/8 | 4 | -0.44% | -0.98% |
| 半導體與晶片供應鏈 | 0.00 | 0/1 | 1 | -2.43% | 0.00% |
| 記憶體與 HBM 供應鏈 | 0.00 | 0/5 | 3 | -4.56% | -6.97% |
| 新興題材：OpenAI | 0.00 | 0/1 | 1 | -10.08% | -0.74% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價呈負相關；應檢查正負向詞庫，並降低新聞直接提及但股價背離的權重。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-08-31 | -0.41 | 0.29 | +40.00% | 10 |
| 2026-09-01 | N/A | N/A | +50.00% | 2 |
| 2026-09-02 | -0.29 | 0.24 | +75.00% | 12 |
| 2026-09-03 | 0.10 | -0.10 | +54.55% | 11 |
| 2026-09-04 | -0.08 | -0.08 | +28.57% | 7 |
| 2026-09-05 | 0.13 | 0.34 | +54.17% | 24 |
| 2026-09-06 | 0.19 | 0.43 | +50.00% | 24 |
| 2026-09-07 | -0.15 | -0.09 | +53.33% | 15 |
| 2026-09-08 | -0.07 | 0.18 | +57.89% | 19 |
| 2026-09-09 | -0.28 | -0.12 | +54.17% | 24 |
| 2026-09-10 | 0.28 | 0.86 | +75.00% | 4 |
| 2026-09-11 | -0.01 | -0.08 | +25.00% | 12 |
| 2026-09-12 | -0.39 | 0.04 | +25.00% | 20 |
| 2026-09-13 | -0.42 | -0.14 | +17.65% | 17 |

## 歷史回測摘要

- 回測日期：2026-09-13
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

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：Stocks stumble on inflation fears, but 2 of our names give us reasons to stay bullish - CNBC；通膨疑慮升溫 美股跌多漲少 - money.udn.com；通膨疑慮升溫 美股跌多漲少 - money.udn.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +10.08% | +0.74% | 495.63 | 507.29 | -2.30% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Stocks stumble on inflation fears, but 2 of our names give us reasons to stay bullish - CNBC](https://news.google.com/rss/articles/CBMitAFBVV95cUxPVmFDU1BhckZ0MXVVUElqZVF6Q1lJemx3VWZlSXd6cmRpcmFYNUJOZmI1Q3o0RjlLSExfX3N6R0xTSEtIemJaRE10VEZkZV80cDhaVXFjWHhfSUZPektiNlJwRmJsckRpci1hc3lXRER3aE83NDJTUTRKT2tXc05yVE9KZE45MVJiVXdKUW9mRDcxblh1NTB1b0lPTEFsaFpCMHJlc21pZ3hrRlJTVTN3SGRlMEY?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 12 Sep 2026 14:37:07 GMT
- [通膨疑慮升溫 美股跌多漲少 - money.udn.com](https://news.google.com/rss/articles/CBMidEFVX3lxTFBzWTh3c0NzUDNXSW54RVNaZUdndEZzR0J2b044S0YzVS1JMWN4am5rZEFsRVpleTd6MVdObFQ3U3Fqb21MWVRfbmVMWnp6VkpEamdDVEZTRTVaNU5YT1Y1cWNvWEhWQmZjNEpvZU1mNVIzRW850gFfQVVfeXFMTWlqV0w5bFNCaVVtaTZvMEh3UjlHZC1VTEpXR1diUHpOWEJvSVZ1NWV4YldYWk1mcjFnSVFfc3ptMDZEOUVsRlBFSWpZUHhGUnhFNjVPQ1hfdHNONUZ6T1U?oc=5) - Google News source discovery | 經濟日報 money Sat, 12 Sep 2026 14:43:30 GMT
- [通膨疑慮升溫 美股跌多漲少 - money.udn.com](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1paldMOWxTQmlVbWk2bzBId1I5R2QtVUxKV0dXYlB6TlhCb0lWdTVleGJXWFpNZnIxZ0lRX3N6bTA2RDlFbEZQRUlqWVB4RlJ4RTY1T0NYX3RzTjVGek9V0gFfQVVfeXFMTWlqV0w5bFNCaVVtaTZvMEh3UjlHZC1VTEpXR1diUHpOWEJvSVZ1NWV4YldYWk1mcjFnSVFfc3ptMDZEOUVsRlBFSWpZUHhGUnhFNjVPQ1hfdHNONUZ6T1U?oc=5) - Google News source discovery | 經濟日報 money Sat, 12 Sep 2026 14:43:30 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：費半跳水衝擊台股力守 4 萬 7 關卡，台積電創高營收力抗空軍 - 新聞 - MoneyDJ；《台股盤後》收跌755點、險守46K，周K翻黑- 新聞 - MoneyDJ；台積電氣弱下殺35元台股早盤重挫逾800點回測46K壓力大- 新聞 - MoneyDJ

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | -0.49 | -2.43% | 0.00% | 2,410.00 | 2,425.00 | -0.62% | 同向 | 86.28 | 27.94 | 514.81B TWD / 53.32% | 2026-09-01 |
| AMD 超微 | 新聞直接提及 | -0.32 | +0.01% | N/A | 516.13 | 516.13 | 0.00% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 2 篇新聞命中。 方向判斷命中詞：重挫, 衝擊, 創高。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [費半跳水衝擊台股力守 4 萬 7 關卡，台積電創高營收力抗空軍 - 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMieEFVX3lxTFBZWXY4WUpzMDJpZmgzWGRxSE5FYXZFa1FHbG94c2lMVlg5amVOaTRURlBUdGRaT1A0STZ0ZUdWTTJOVnFEOE9KWmV3Z09pb0FkQkhQc0FIeGI5b1pqQnZPN3M0MWJiRGotY1kzVF9CRHE3SS1rVHRxNw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 11 Sep 2026 03:41:00 GMT
- [《台股盤後》收跌755點、險守46K，周K翻黑- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPQ0pSOWgyWXUwWVhNdmZPZDZMcEFJdXEyQWt2Z0tFRWJxZWV0VjdKa3pseXlZaExjWHRWLTlWYzgwaXB6ZzJ6cE5hSktWb3Z2Szc5Uk4yalFWQTByNzQ4c2MyNWJjWVFBUmZrWHhvcFFNWk1DOXhLQ2p1SGFrUmVnbVBfVktVQmctMGRIa250bnRWdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 11 Sep 2026 08:08:00 GMT
- [台積電氣弱下殺35元台股早盤重挫逾800點回測46K壓力大- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMieEFVX3lxTE02T2MtR2IwUUcwUmZsenlPcElVbUFMcTV5RkNhVmtOcGl5WFFqczQ4d2F4ejZvTW1PWm1tZEhicGRVdVRENVJENlV4Z0UyLWFYd05GREQxWUh3Y3huTW9IcE5lQ1lxdkt6MXM3a3BlWTN3ZXNLMkhYVA?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 11 Sep 2026 02:11:00 GMT

## 新興題材：DeepSeek

摘要：新興題材：DeepSeek 相關新聞集中在：SK Hynix, Samsung Shares Dip In Korea After DeepSeek Debuts AI Tech That Uses Less Memory – Micron, SanDisk Hold Up - TradingView；DeepSeek's Leaner AI Model Slams Korean Chip Stocks as Memory Demand Fears Resurface - finance.biggo.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | +0.44% | N/A | 975.26 | 975.26 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | -6.02% | +5.04% | 1,633.35 | 2,335.00 | -30.05% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、memory」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。

### 主要來源

- [SK Hynix, Samsung Shares Dip In Korea After DeepSeek Debuts AI Tech That Uses Less Memory – Micron, SanDisk Hold Up - TradingView](https://news.google.com/rss/articles/CBMiggJBVV95cUxQYzk4MzNIdGNsSUFGRnlaZU5JRlpFXzc5OWc0T3BLOXR2SUhkLUxRZlU3b214U25FbmlzXzBXS084RExNZnM4UGhqaEdISkZHTVFHUFhVdmpwTDdFeUpXNXRNeXUyRVFFZEptT2puaTNtczRmQzczZ3lSSDk0LUpFcXRQbFFjVkdJakpxUC16M001NHprbWFVV2NCbHlremhab0V6aTFtb2UweUYyczJ0Rzg3RUlVQnpsb3duc2NPMC1relgyOFlNckRtYktYRlFTTGFoMzNkdkZ1ZFkwN1Z6OGNhSXVWVG1mVFRUZ2dYd3FOa0hZV1BjX1U4TERNdnc2T1E?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 11 Sep 2026 07:18:11 GMT
- [DeepSeek's Leaner AI Model Slams Korean Chip Stocks as Memory Demand Fears Resurface - finance.biggo.com](https://news.google.com/rss/articles/CBMidkFVX3lxTE9JeUNEOWNXNTFOaUp3d2hfUkw3N1VDQmluaUFuZ2RhVnVQa1ZPNDByaWk4X1RnalpwYTBqUzVYejUzdFdpMEZDOGc3MnhwQXVVVklVREF3Z1hmdjEwZS1DSWtuZkg3elMtNVpjc1RfdVAtUjFVRkE?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 11 Sep 2026 18:44:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：企業如何利用 AI 評估人才的「盡責性」以提升長期績效？ - TechNews 科技新報；員工如何在導入 AI 工具時，避免批判性思考能力被科技削弱？ - TechNews 科技新報；生物節能機制，如何啟發 AI 機器人？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | +0.04 | -10.24% | N/A | 102.94 | 114.68 | -10.24% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.06 | +8.74% | +3.39% | 218.29 | 220.78 | -1.13% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.04 | +0.01% | N/A | 516.13 | 516.13 | 0.00% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.03 | -2.43% | 0.00% | 2,410.00 | 2,425.00 | -0.62% | 背離 | 86.28 | 27.94 | 514.81B TWD / 53.32% | 2026-09-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | +10.08% | +0.74% | 495.63 | 507.29 | -2.30% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -7.01% | -18.98% | 361.99 | 446.77 | -18.98% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.03 | 0.00% | +5.10% | 618.00 | 680.00 | -9.12% | 未明確 | 13.92 | 44.72 | 82.25B TWD / 45.66% | 2026-09-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.02 | -2.65% | +3.85% | 4,585.00 | 4,585.00 | 0.00% | 背離 | 60.69 | 75.72 | 64.18B TWD / 44.08% | 2026-09-01 |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [企業如何利用 AI 評估人才的「盡責性」以提升長期績效？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMigwFBVV95cUxQV0x2OEFIVjJaN3d4R2Ewd0RKOGdRZTJCR2xiOG9XSC1veVM1NmtZb1IxWktuYmI0N2U4ZzNwM3dHUjVYem54c0h5Q1l4a2FQMUhhY2JqTXZHSHB2TE1jc1d4SWh3XzA3TnV3cUxSZFpuV0t4WU00QzdPbkNiOVN2cllCNA?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 12 Sep 2026 17:36:56 GMT
- [員工如何在導入 AI 工具時，避免批判性思考能力被科技削弱？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMid0FVX3lxTE5CeVNfbEpnVTNEclN5elRoZXFpRFM0YWRwb1BkNUtWZmoxeTI5cHhhWjNHU0xMZ2FyTEE1QXFZOWwxZkhkbkVEb3BWS1NWTWd2T2J2SGhVYjZTQXcxUjVtN0duZ2o4TFk3d1VhVHIxVUw5RFE1NWVr?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 12 Sep 2026 12:43:08 GMT
- [生物節能機制，如何啟發 AI 機器人？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMipgFBVV95cUxOek5YVmpQZGJ5dWFXN3FSNVh3MnRvVmVoWG9NNERuUXlCX2p3bzhYRjFHZThoYWpwSGc2cGE4QkdvaUlHQ0xfdUFibHVPNTVVejFuX1YwTHBJZ2tzeThveDFTSUo1SnNiOTU5VGNvRFk2ZFpGaUhvRkgxY2taTFFjb1BfYmxyaVVOMFF3OTlob1BhRi1ta1M1c0lhS0hxejIwXzlqdGtn?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 12 Sep 2026 12:33:29 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：台股外資狂砍 打46K 保衛戰 國家隊即刻救援 低接台積電、世芯等半導體股 - money.udn.com；賴總統頒褒揚令肯定黃崇仁為半導體產業開拓者| 政治 - 中央社 CNA；中石化：下半年調整產銷另布局新能源、半導體材料| 證券 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | +0.27 | -2.43% | 0.00% | 2,410.00 | 2,425.00 | -0.62% | 背離 | 86.28 | 27.94 | 514.81B TWD / 53.32% | 2026-09-01 |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | -10.24% | N/A | 102.94 | 114.68 | -10.24% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +2.55% | +8.08% | 140.50 | 164.50 | -14.59% | 不適用 | 6.68 | 21.13 | 25.04B TWD / 30.71% | 2026-09-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +8.74% | +3.39% | 218.29 | 220.78 | -1.13% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | +0.01% | N/A | 516.13 | 516.13 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | +0.44% | N/A | 975.26 | 975.26 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -6.02% | +5.04% | 1,633.35 | 2,335.00 | -30.05% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -7.01% | -18.98% | 361.99 | 446.77 | -18.98% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip, foundry。
- INTC：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 CPU, server CPU, x86, foundry；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 0 篇新聞出現相關標籤。

### 主要來源

- [台股外資狂砍 打46K 保衛戰 國家隊即刻救援 低接台積電、世芯等半導體股 - money.udn.com](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBteEtoRm9iZzNIYWt5akVtOGxHWTRxdEJFb0RRempldjJjakR0V2NvOUhPS28wby1zdEJhM0VpeFdtNlZ6Tnk2aWRjUnhnX2djTVBmaEJkakZJQdIBX0FVX3lxTE53dzR1NDlPc3NQR1QzOUR0VXBQT2VlVGZYYzBHYzFFeVowQi1Va2JNaWp4ODNmRWhCS1dGYWFiMzlVTEh6TTIzakFnRkxUX1VwRE9wejZZSGZ1Zjg2YkpB?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 11 Sep 2026 17:02:33 GMT
- [賴總統頒褒揚令肯定黃崇仁為半導體產業開拓者| 政治 - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9IM21aWWVSWUY0dE1aQTdfZEYwZkptdnJrelEyTEV4eWF6OFRNZzI3MjBOb19vay11UGY0bTRIQl9DS2Z4bnpxUTd3c1RFX1Y2VFZseWF3YWxnMmc5NHF3?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 12 Sep 2026 05:30:00 GMT
- [中石化：下半年調整產銷另布局新能源、半導體材料| 證券 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE5yR0IxRXNhZFZhNHBWeG9BVXN1Rjc4Z1M3RzBLM19EQmdWemZWallXMHFQR3RTZUw3b2tkeHBnVmJOdVdZQUJTSlE0NzRONVZpdlpzMVVSZExTZkFNVGc?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 11 Sep 2026 10:57:00 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits；Billionaire Stanley Druckenmiller Dumped Broadcom, Intel, and Micron for This Chip Stock. Here's Why. - The Globe and Mail；SK Hynix, Samsung Shares Dip In Korea After DeepSeek Debuts AI Tech That Uses Less Memory – Micron, SanDisk Hold Up - TradingView

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.43 | +0.44% | N/A | 975.26 | 975.26 | 0.00% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.28 | -6.02% | +5.04% | 1,633.35 | 2,335.00 | -30.05% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.24 | -10.24% | N/A | 102.94 | 114.68 | -10.24% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.32 | +0.01% | N/A | 516.13 | 516.13 | 0.00% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | +0.21 | -7.01% | -18.98% | 361.99 | 446.77 | -18.98% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +8.74% | +3.39% | 218.29 | 220.78 | -1.13% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron、memory」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk、SNDK」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- INTC：新聞直接提及「INTC、Intel」，共 2 篇新聞命中。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits](https://news.google.com/rss/articles/CBMi0AFBVV95cUxOWm5KdEIwSXpyY191UEhDa1V6NVpWa01UbmpJeWRIV0ttT080TmpDNEhISW5TWkQwUzBVYzBqSHJPWXRVNVJCampoWWRlYmhKVkhIeHBJLS0wLW5Ua09GQnRORXpFcW5qTEJkcnJGcW55aU5rOFVOLUFMbjRPZEpWT3A2ZllucnM0SU9JNEdrNUwyc3V2WHAtNFk3VHl4R1F6SkZRMFpleEE2Zl9MdW4tSEpMMnFGZ2hQZURWQ3B1WDlPR1BhRjJELVN5ODJWYVR3?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 12 Sep 2026 04:00:43 GMT
- [Billionaire Stanley Druckenmiller Dumped Broadcom, Intel, and Micron for This Chip Stock. Here's Why. - The Globe and Mail](https://news.google.com/rss/articles/CBMihwJBVV95cUxQVTRiZlJXR2JhMHdWU1pEaHBXOHlKcVFXNjFJOThTOWJqQjVHMUR4LWJJRDlkU2hVNjBuVXhXOHBJbkFCM2NyTGd4YUY1bzgzS0xTT3hBZC1RdWVmZFVMdTJmTFV0Y1NCcDdZZmlZNFZzTlE2U0xKQlRod0oxVDBiTW5KdkVURUhacmpfYVNGUUxTTGdYTjVZQmgyZ1NSS3Raay1UZzZyRmlXZnpQNXVUR0dkY09VbHpwZ29ZU05NTWRfNE5CUzFLNXZQT3FjaEZVUWJZaXVsdDlQN1VDOGRpNWhXMkp1TzY5NXVGajVST0xFcjNzZE15RDJBQUhraF8xV1JkZ2lGUQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 12 Sep 2026 08:43:06 GMT
- [SK Hynix, Samsung Shares Dip In Korea After DeepSeek Debuts AI Tech That Uses Less Memory – Micron, SanDisk Hold Up - TradingView](https://news.google.com/rss/articles/CBMiggJBVV95cUxQYzk4MzNIdGNsSUFGRnlaZU5JRlpFXzc5OWc0T3BLOXR2SUhkLUxRZlU3b214U25FbmlzXzBXS084RExNZnM4UGhqaEdISkZHTVFHUFhVdmpwTDdFeUpXNXRNeXUyRVFFZEptT2puaTNtczRmQzczZ3lSSDk0LUpFcXRQbFFjVkdJakpxUC16M001NHprbWFVV2NCbHlremhab0V6aTFtb2UweUYyczJ0Rzg3RUlVQnpsb3duc2NPMC1relgyOFlNckRtYktYRlFTTGFoMzNkdkZ1ZFkwN1Z6OGNhSXVWVG1mVFRUZ2dYd3FOa0hZV1BjX1U4TERNdnc2T1E?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 11 Sep 2026 07:18:11 GMT

## 新興題材：OpenAI

摘要：新興題材：OpenAI 相關新聞集中在：OpenAI IPO will not happen in 2026 amid AI safety fears, Altman says - Reuters；OpenAI agents attacked RubyGems before Hugging Face incident, researchers say - Reuters；OpenAI rules out IPO this year as Altman, Musk & Amodei warn AI is moving too fast - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 新聞直接提及 | -0.28 | +10.08% | +0.74% | 495.63 | 507.29 | -2.30% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：新聞直接提及「OpenAI」，共 5 篇新聞命中。 方向判斷命中詞：slowdown。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [OpenAI IPO will not happen in 2026 amid AI safety fears, Altman says - Reuters](https://news.google.com/rss/articles/CBMiuAFBVV95cUxNSkNHUFFrUlZCVWVKZ2dpVVkxSzBmcy16aFFHVTJDV25PZ0YzMjBLVlFQZ0pJcU5EVWJlUW13azNiV1BwOENLcTFVOFpZYVVlT0haaXI2ZkFaOUZxTGp2eE1kaGZCb2pXV1dBQy1XcjQ2NmNXMFA3Nnk5ZnA3MU5wWGZCV0ktTWZad2o0LVBmeW1BclBndWRfWEJScFduQklEZUFEX0NteFBhNDYxRG5keUdiUml3dVYz?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 12 Sep 2026 20:46:43 GMT
- [OpenAI agents attacked RubyGems before Hugging Face incident, researchers say - Reuters](https://news.google.com/rss/articles/CBMiygFBVV95cUxNV2F3RkRiVXZra3BTMExtX3lNVHBEV0xTbkxBMXNwaDVIOGtkeXJEWXRxeEd3dDlLbW5kOUdrQlFnXzVZTk9YRXMxdFRRVGpfR0puUjkyYXozVHJsVXVHTlhSNDVyZjlxMkVwNnU0a2pMMzdOSTdsaTJ4d2E2R1FLbU8wb0VVbW9GUzRsa0VTYUJhN24yRDNTTmtnYkpRUHVlN002SG54czB5UzRsTEtMLUxSSVgyN19xcnRwaGowODRJMXk3ZVNwRDNB?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 11 Sep 2026 22:41:00 GMT
- [OpenAI rules out IPO this year as Altman, Musk & Amodei warn AI is moving too fast - CNBC](https://news.google.com/rss/articles/CBMitAFBVV95cUxQbWdEQ1p3VzJkd2E3ZmYwWmRkRWlwWEhFSm1PTjQ3Y1N1bGNPd1lXcjZncEhPVVNrd3dFT3oxd1FVbzVMZmZTVEJVZGJ6MHNxTUd0eVI5MkpuY191WG9CaUozc3AzWkhPQUlzUDh0dXFqQzlNd09CR0NrQ01NaVBERHhCUE9vcmR1UmlfMFVXdmFlcDNocnJkMkJOa0pWQ0p0SVhia1QwS3A4LVZjYXdfLWhiRTHSAboBQVVfeXFMUE44bkREVTl5S1B2R2RMNUlMSlZlT1N0RU5yeTJLaDhFd0dWZ2wwRmdaVUpWRGpYbTBtVVlITnRNLTJRcW43RlhKQzZFVTluc2E2dVhuSzNOWWtoVzFwRDFDX0wxVWszTDk5NkcxQjNaN3JCWGlpUnhTdGM4dzliVHFQam1IV2x6dW1jMkh4SkFNWjVRbzlSQVpaZEFvbE9QZHNiSWJMS3l4aDVMLVFRdk9FbGYxLXBZdjNB?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 12 Sep 2026 16:22:17 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：凱基-雙和 對 正淩(8147)個股 單一券商歷史明細 - justdata.moneydj.com；個股動態報導內容-17D84AC7-B1B6-4273-9F17-E2986C244F83 - concords.moneydj.com；個股動態報導內容-6A412172-6430-462C-A799-344F9D2989B0 - concords.moneydj.com

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [凱基-雙和 對 正淩(8147)個股 單一券商歷史明細 - justdata.moneydj.com](https://news.google.com/rss/articles/CBMilgFBVV95cUxPc0hiWXZNOVNBbkJRVnVEYXNLMUpjRkNmSFN6T0M5dFYyeXBNUnZvY1FVTHFFMkk4cVhiRGdOT2tvelB4SWhKcHAtSHJrbW9tQlJGMDdmbHVLWkxwRXFnWkd6bEt4RGRwM2I4Z3lmclRmVURxb2FVbDZhRS1oNjFXTHNURy10OFVYWC1mLWtKVFhZQjhiQUE?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 12 Sep 2026 13:56:49 GMT
- [個股動態報導內容-17D84AC7-B1B6-4273-9F17-E2986C244F83 - concords.moneydj.com](https://news.google.com/rss/articles/CBMilAFBVV95cUxPMl9JemhJUHZWRXVlQ1h6ZVZacWN6dlJnaDR3Qm56azM2RXhNUnlibE54NVRlU21RU2wtcWVQTzNGa2loZTRyWFpZWEZvZXg3VVVVSXV4bm1MaEhOOVFnRUtOUjhzVy1TN2JaNTFtcWZ4bFZ1X0xPMENRY3NreHh0V1BSU0drcTVjQ2toSHFiS3ppU1h0?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 11 Sep 2026 16:51:23 GMT
- [個股動態報導內容-6A412172-6430-462C-A799-344F9D2989B0 - concords.moneydj.com](https://news.google.com/rss/articles/CBMilAFBVV95cUxNVzhZR3FLS0VJOE5ZRUZoczdleTVKU1BQMENtQUdYQmxFZnA2VDlQTHFZU0xQU1pXUmd6dnFITGViM0VJamRMTjJIYmo2c21fMlpuc0JrNVBiS2MtR28weXRvS1JRT2lRNWdvT3N0SXZkdWZQc1hrbFU1ZTdObGYyZ1NNTXlqclNyWlhFNzJVN29CYlN2?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 11 Sep 2026 16:14:54 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
