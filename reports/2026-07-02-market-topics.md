# 每日股市熱門話題分析 - 2026-07-02

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **綜合市場情緒**｜正向｜熱度 46｜市場確認 79.15｜同向 1/1
2. **散熱與液冷供應鏈**｜正向｜熱度 3｜市場確認 100.00｜同向 1/1
3. **新興題材：TradingKey**｜正向｜熱度 1｜市場確認 100.00｜同向 1/1
4. **AI 伺服器與資料中心**｜中性｜熱度 9｜市場確認 N/A｜同向 0/0
5. **半導體與晶片供應鏈**｜負向｜熱度 7｜市場確認 31.13｜同向 2/5

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.30（樣本 9）
- 5日相關係數：0.03（樣本 9）
- 同向比例：5/9

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 綜合市場情緒 | 79.15 | 1/1 | 0 | +3.05% | -5.06% |
| 散熱與液冷供應鏈 | 100.00 | 1/1 | 0 | +16.19% | +3.56% |
| 新興題材：TradingKey | 100.00 | 1/1 | 0 | +11.43% | +26.81% |
| AI 伺服器與資料中心 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | 31.13 | 2/5 | 2 | +1.04% | -6.60% |
| 記憶體與 HBM 供應鏈 | 0.00 | 0/1 | 1 | -2.80% | +6.15% |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：B226 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-06-19 | 0.06 | -0.04 | +57.14% | 7 |
| 2026-06-20 | 0.29 | 0.21 | +63.16% | 19 |
| 2026-06-21 | -0.01 | 0.32 | +55.56% | 18 |
| 2026-06-22 | -0.87 | -0.87 | +100.00% | 3 |
| 2026-06-23 | 0.38 | 0.01 | +62.50% | 8 |
| 2026-06-24 | -0.38 | -0.11 | +25.00% | 12 |
| 2026-06-25 | 0.10 | -0.21 | +20.00% | 5 |
| 2026-06-26 | 0.08 | 0.04 | +25.00% | 16 |
| 2026-06-27 | 0.12 | 0.29 | +57.89% | 19 |
| 2026-06-28 | 0.16 | 0.55 | +85.71% | 14 |
| 2026-06-29 | 0.49 | -0.25 | +38.46% | 13 |
| 2026-06-30 | 0.44 | -0.27 | +62.50% | 8 |
| 2026-07-01 | -0.08 | 0.25 | +30.77% | 13 |
| 2026-07-02 | 0.30 | 0.03 | +55.56% | 9 |

## 歷史回測摘要

- 回測日期：2026-07-02
- 近5日 3日相關：0.01
- 近5日 5日相關：0.03
- 同向比例：+52.38%
- 權重狀態：已調整

- 方向準確度：+52.38%
- 信心排序準確度：0.01
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

摘要：綜合市場情緒 相關新聞集中在：被動式台股 ETF 吸金 - 經濟日報；台股大漲846點 外資僅買超131億元、買賣超冠軍竟都是金融股 - 經濟日報；台股強彈熱度爆棚！聯電漲幅逼近190% 遭列處置股 明起「關禁閉」 | 集中市場 | 證券 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2303 聯電 | 新聞直接提及 | +0.56 | +3.05% | -5.06% | 169.00 | 169.00 | 0.00% | 同向 | 4.00 | N/A | 22.94B TWD / 17.78% | 2026-06-01 |

關聯理由（前 3）：
- 2303：新聞直接提及「聯電」，共 2 篇新聞命中。

### 主要來源

- [被動式台股 ETF 吸金 - 經濟日報](https://news.google.com/rss/articles/CBMifkFVX3lxTE41Mlp2akhSS1d2a3lSZ1I1cWp3NlM2d3lxYVdIQmUzcXJQcEJWMTVIRERGdmw1UlZmMGZoN2V2YXpwUk9EVnoyV0dxWlVLb0xWMjhsbzBwOHJ6VTBXc2xFeXVadm51Y2oxZ05SUkhWRWdpcUticHp4U0QwdTF3QdIBX0FVX3lxTE5WNTRYSHJoc0l2Z3ZXYkh5OGw5VURyTEdVRXBscnhsZ2g2dXdzNGljaldiT3B4ZUtfZ3g3eHlLczVQWUxRVWFXOEM5aXZaVnhsbkgtY2FjeEp5SjJjQVNJ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 01 Jul 2026 17:48:26 GMT
- [台股大漲846點 外資僅買超131億元、買賣超冠軍竟都是金融股 - 經濟日報](https://news.google.com/rss/articles/CBMif0FVX3lxTFBnZW95bFFUMllwazJUVF9NSWlYRVV1em9fMjdOVG91am00VW9iWS1qdU9YUS1DdFoycUhkRUxQVDR5ZXpXejBodVNZWGRfVDB0OXZJNzNaQjhXMVd6SHZKQ0VETVZqXzVnVlFiZmlxU0dHRTh4bWx4aWJfTUtEMU3SAV9BVV95cUxPbE0yMXNQUFNPYm00eXU1eWtxNnJJVllnWVR2OVdiMVd2ejM2N2FtckJuQzNCM0dkWjE3d1N1MDRsWHBsTmFQSFVnYTQya1NVczNpSS0wbDl6aGhkSTE2Zw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 30 Jun 2026 09:00:00 GMT
- [台股強彈熱度爆棚！聯電漲幅逼近190% 遭列處置股 明起「關禁閉」 | 集中市場 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9HQ1VOamd1ay1MSmRJVExtVUlLNHdaZ3lvUTE5dlFra0F4Qm1pZzFrN3NGU0h4MnBvRGJGTXNMR2RONXRvbmJuNlR4RjFzR3RDMHNLa240Z3dwQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 01 Jul 2026 14:39:10 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：ASIC/VeraRubin出貨升溫，奇鋐看旺下半年動能 - 台視全球資訊網；AI散熱廠奇鋐一度漲停！訂單直達2029年 看旺下半年動能 - 緯來新聞網；《電週邊》Vera Rubin出貨 奇鋐H2添柴火 - 富聯網

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.65 | +16.19% | +3.56% | 2,620.00 | 2,835.00 | -7.58% | 同向 | 61.06 | N/A | 15.87B TWD / 60.64% | 2026-06-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐」，共 3 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：漲停。

### 主要來源

- [ASIC/VeraRubin出貨升溫，奇鋐看旺下半年動能 - 台視全球資訊網](https://news.google.com/rss/articles/CBMikgFBVV95cUxNZ3A0cUdtMmx3LVJvbUZlRVNWTURxNENIYlFuX3NqQ1MxaWtCUjNBNWl3Q0NHMjhjZ3BIbXRKaWR0Nk1mSEZ0ZEVQcnZ5WF9QN2V0bWlIUGhZU1h1VGZoQW83MEJCTm92ZkljZ2ZSTTlFVjIyUUMwN1pQU0FpUmRnUFF0X2ZUQmhtelJpblFucjA3UQ?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 30 Jun 2026 06:20:18 GMT
- [AI散熱廠奇鋐一度漲停！訂單直達2029年 看旺下半年動能 - 緯來新聞網](https://news.google.com/rss/articles/CBMihgFBVV95cUxNb29xS092VmZKM0NYQ2FzQkhvTE9GMVlxRExmclA3bzhkUU13U3J0X1dpZlRqQ080OUlicFFhNnJkN2NuSnJ2TV9wbjJMb1YwT2dRdk1EOElrZ05TRnpmYnlrWGtNN0Y2T2tQdmVRZTQ5SU8wZTNUSmVUbDlFSGJHcnBkWHRodw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 30 Jun 2026 09:41:00 GMT
- [《電週邊》Vera Rubin出貨 奇鋐H2添柴火 - 富聯網](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPZng3NkEyalRuZHFXSkZ3Z1V6MThVbFlTaWs2QWIwZUdaVkRMMlBmWUFpMVp0a05MR2RDMWZ1ZHBoWEFfVVZPamV0SkpyVWtkTXkwV0RFSTVKTk9pX09UUXVLN2g3Uk5KUW9lc19ZWkFQUlpxcUo0U2pCNjgyY24zUnktalgwSUxP?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 01 Jul 2026 00:25:00 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Intel Stock Outlook: Can the Apple Foundry Deal Justify INTC’s 250% Rally? - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.48 | N/A | N/A | 127.02 | 139.63 | -9.03% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 新聞直接提及 | +0.48 | +11.43% | +26.81% | 294.38 | 312.06 | -5.67% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AAPL：新聞直接提及「Apple」，共 1 篇新聞命中。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Stock Outlook: Can the Apple Foundry Deal Justify INTC’s 250% Rally? - TradingKey](https://news.google.com/rss/articles/CBMiuAFBVV95cUxOUW1Cai1mU1FWR2h6WDBlMVpaQ3owUEpETXV6dGp5Y0FGdmJxQktrb1ZORUZmSWIyUVo2Q1g1cU1QX0dmZGw3cnFfT1FyVUhkVWtNUkx4dE9rcHFadC1tUXo4X19COVBXZmNkTVFJbm1JUGNERjN6cF9GWnlNREpSN1VTMXFzc01sSmpkNndONkp2MG5Kc3VjTzNZTlZGdk1DSUxvTGlQNUJXVGxpQ2l6SzljWm1VaE5a?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 01 Jul 2026 02:09:45 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：AWS 全自費推 FDE 新團隊，送整批專家到公司手把手建設 AI 系統並教到會 - TechNews 科技新報；「矽電光熱」成 AI 發展主要瓶頸！法人點名台積電、穎崴等 10 檔受惠股 - TechNews 科技新報；AI 化不如預期，福特聘用資深前員工回鍋省下數億美元 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | 0.00 | +7.05% | +4.81% | 2,505.00 | 2,505.00 | 0.00% | 不適用 | 74.39 | N/A | 416.98B TWD / 30.09% | 2026-06-01 |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 127.02 | 139.63 | -9.03% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -1.00% | +11.51% | 197.58 | 211.14 | -6.42% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 540.88 | 580.91 | -6.89% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | -2.15% | -24.16% | 384.28 | 506.69 | -24.16% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -11.52% | +15.58% | 369.34 | 446.77 | -17.33% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | +11.23% | +7.66% | 703.00 | 703.00 | 0.00% | 不適用 | 10.86 | N/A | 63.03B TWD / 28.57% | 2026-06-01 |
| 2454 聯發科 | 產業/供應鏈推估 | 0.00 | +11.73% | +1.17% | 4,335.00 | 4,335.00 | 0.00% | 不適用 | 62.91 | N/A | 47.43B TWD / 4.99% | 2026-06-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 同時符合主題標籤：AI, advanced packaging, CoWoS, AI server。 方向判斷命中詞：不如預期, 受惠。
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：不如預期, 受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：不如預期, 受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AWS 全自費推 FDE 新團隊，送整批專家到公司手把手建設 AI 系統並教到會 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiogFBVV95cUxNeTl2VUcySTRZa0VlSjJGU0FEcFhzRG9rZ0JncU9LeVU5SlVpVHhmNXBFd1hPejBhVGE3TzEzc3UzOE1sSnp6UmxiY3RPVHpsbDlkdk40dXVJejFJeWJBclpyVzlnSWVXdVgxbTctUGlRWU1kY0J0S3diR1dvaTF4RGhzcFczeXo3WTRXQzhOckhER1dqNEtPellPeFZhUjlVY2c?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 01 Jul 2026 03:43:46 GMT
- [「矽電光熱」成 AI 發展主要瓶頸！法人點名台積電、穎崴等 10 檔受惠股 - TechNews 科技新報](https://news.google.com/rss/articles/CBMidEFVX3lxTFBqMUNFaGhPOUtUZHhhaHF2SlBzWWdGdmU2QjJtTTR4VlVLbkZlaHlmMkFpQXRGc0FoekNqVjdTaTR6eXIwSEFoYXIyX243czhOSXdMeVJtQ0c5N08weWd6MjRpdjRmZGF1cmJIUVNpZGFWQ1d4?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 01 Jul 2026 10:27:42 GMT
- [AI 化不如預期，福特聘用資深前員工回鍋省下數億美元 - TechNews 科技新報](https://news.google.com/rss/articles/CBMijwFBVV95cUxPUS1ZU0dfZlVtY19idWNGVFZ4TXRGQXNKeUJuT3lOQTBCa0xtY1N4YWdzSkN0bXZCQ3BkaktrcnRwMGVyMmFYcDlacjNLa2JNRzF1RnVMVmh0N1NaMVhjME1sWWE2dTRfTlAyeXFDS3F3Q1F0dGg1d3BJbWR4NW9oS29DS3lieXYyc3JvVHJ0OA?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 30 Jun 2026 23:33:32 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel, AMD Jump 7% as Chip Stocks Catch a Risk-On Bid - 24/7 Wall St.；半導體股正在經歷最後的狂歡？大摩示警：走勢恐像白銀觸頂資金將轉向3大族群- 國際 - 工商時報；列台灣為競爭對手挑戰半導體產業鏈！邱銘乾：韓國吃大鍋飯缺創業精神學不來 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.59 | N/A | N/A | 127.02 | 139.63 | -9.03% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | -0.28 | +7.05% | +4.81% | 2,505.00 | 2,505.00 | 0.00% | 背離 | 74.39 | N/A | 416.98B TWD / 30.09% | 2026-06-01 |
| AMD 超微 | 新聞直接提及 | -0.54 | N/A | N/A | 540.88 | 580.91 | -6.89% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2303 聯電 | 產業/供應鏈推估 | -0.03 | +3.05% | -5.06% | 169.00 | 169.00 | 0.00% | 背離 | 4.00 | N/A | 22.94B TWD / 17.78% | 2026-06-01 |
| NVDA 輝達 | 產業/供應鏈推估 | -0.03 | -1.00% | +11.51% | 197.58 | 211.14 | -6.42% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | -0.04 | N/A | N/A | 1,032.28 | 1,154.29 | -10.57% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | -0.04 | -2.80% | +6.15% | 2,032.22 | 2,335.00 | -12.97% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -11.52% | +15.58% | 369.34 | 446.77 | -17.33% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：risk。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip, foundry。 方向判斷命中詞：risk, 重挫。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：risk。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel, AMD Jump 7% as Chip Stocks Catch a Risk-On Bid - 24/7 Wall St.](https://news.google.com/rss/articles/CBMimwFBVV95cUxPUTRGOGMwMUZfbkVVbXByR0FjbDc0MXZfeDV3WmdfbVFXbGtONWNEZHFIVzhVV0ZyQmRDcERTNHZOcUdfYjE5dGUzcDhuT2hyZDFOWXZ3YWlPM3FRd19ZWjlEYzJmSWJZd3BFR0lOQm14OThMOEZRV3lfQ1FJTWVFMlJvN01tQ3pNS2E0c2NOU0JIclhLSHNPdkgyMA?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 30 Jun 2026 16:18:10 GMT
- [半導體股正在經歷最後的狂歡？大摩示警：走勢恐像白銀觸頂資金將轉向3大族群- 國際 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5HdHh1X3RteG9WMmNWbHI4THFkSjFRbW9TUTVVak5hQ2xtalNyNk5qcFh3d0Q5Yi1pcnNrOTg3ck9ndHlZWVhzdTI2Y3hZbFVmRjdtaE1XcWdnNGxvOXJn?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 01 Jul 2026 06:43:00 GMT
- [列台灣為競爭對手挑戰半導體產業鏈！邱銘乾：韓國吃大鍋飯缺創業精神學不來 - TechNews 科技新報](https://news.google.com/rss/articles/CBMipwFBVV95cUxPeEZSMmlHT2pReC1PbHZjZnB1a3lZNlY1dlV5SkRYSHRFNnEySVJ1amRyX0huc3dMWlRBRkR6QnZlTktndkFnVTVtTi0tbWk2R2dua1BFdl9KS3lGZ3pUWFo1UEF2RUx6U0JUMEVqQUxtaUN6X0VaUzd5blVqMXJMQVhnUUM5YlZhZmJ2ZVRTUXZzSFYtQVR2MnBGb3diYUpCR29sNjRldw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 30 Jun 2026 05:46:48 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits；Semiconductor ETFs to Buy as Micron Leads $2T AI-Led Chip Market Rally - TradingView；Memory chip stocks hit the brakes at highs: SanDisk and Micron plunge sharply - 富途牛牛

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.65 | N/A | N/A | 1,032.28 | 1,154.29 | -10.57% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.33 | -2.80% | +6.15% | 2,032.22 | 2,335.00 | -12.97% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.48 | N/A | N/A | 540.88 | 580.91 | -6.89% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.48 | N/A | N/A | 127.02 | 139.63 | -9.03% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -1.00% | +11.51% | 197.58 | 211.14 | -6.42% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk、SNDK」，共 4 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 方向判斷命中詞：rally, 52-week highs, hit 52-week highs。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [INTC, AMD, MU Stocks Hit 52-Week Highs Today: What's Triggering The Rally? - Stocktwits](https://news.google.com/rss/articles/CBMi0AFBVV95cUxOWm5KdEIwSXpyY191UEhDa1V6NVpWa01UbmpJeWRIV0ttT080TmpDNEhISW5TWkQwUzBVYzBqSHJPWXRVNVJCampoWWRlYmhKVkhIeHBJLS0wLW5Ua09GQnRORXpFcW5qTEJkcnJGcW55aU5rOFVOLUFMbjRPZEpWT3A2ZllucnM0SU9JNEdrNUwyc3V2WHAtNFk3VHl4R1F6SkZRMFpleEE2Zl9MdW4tSEpMMnFGZ2hQZURWQ3B1WDlPR1BhRjJELVN5ODJWYVR3?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 01 Jul 2026 07:56:11 GMT
- [Semiconductor ETFs to Buy as Micron Leads $2T AI-Led Chip Market Rally - TradingView](https://news.google.com/rss/articles/CBMiwwFBVV95cUxPeW9UbHdiakdoUkJGblV3d0o2QVNRY09BQzUwa1FMMmFBM192blJwTF9LM0xpRlhwQXJRU3gzRGQ2a2o2VktHQ0JTYmFPb1RtcUFRNFB6clVYMTF1aUhjSVl0ZTNIekpueFV2MmpveFktMGdZVFZJOXY0NF80T2ZJRVVSdmNrNWo0eEdFLVNlWGp0NUdlUWlZc1BqbGJxQ2U3SkREbFFlbXVEdXNoOHpkbFh2MDFfSllWZUJQRHhwdENfNUU?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 01 Jul 2026 12:13:00 GMT
- [Memory chip stocks hit the brakes at highs: SanDisk and Micron plunge sharply - 富途牛牛](https://news.google.com/rss/articles/CBMimwFBVV95cUxPVFNpakNLMWViUlhoUmlpdjZqS2NwRkZYOHI0dWFyY2JKSEJ2N1N3VGlOVklSSWVhMU1uSUtGYTV1N1BSU3JSVkNEQjR5YVlSZjUzeEFRV1ItNkROaFJKdHV1c3ZWNXl0ZTBqZVVpOEVKRTVVQjY3N0pEWDY0MWRWM2hTOUc2MlY1andMQXEwUWphWEt2MktzTHJfRQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 01 Jul 2026 18:57:28 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：個股動態報導內容-01F2E20A-40C4-4615-9FAC-064DA228D46E - MoneyDJ；個股動態報導內容-AFA94DC4-B226-48C3-9BC1-99BD11E93ED7 - MoneyDJ；《台股盤後》收漲893點、日K連三紅，重返47K-新聞內容-基金 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-01F2E20A-40C4-4615-9FAC-064DA228D46E - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxOYmdwa2IxZk9vaFNLU0hsbFNqQTZJUlE3MDd5OGRlejgxZ3JzVzlkOGktZ0UzdGZUd0hUQzQ1dVpFOW5oTDhCczQ2Y0drLXEtLUE2ZVdZUE5nMDhxWGt2N1lvd3RZaW5DcjhwZlZLcFROek1iMGhFWFltanBpTUVhVkZEVDE1cWZKOUhibkxoN2dfdGN6?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 01 Jul 2026 12:18:55 GMT
- [個股動態報導內容-AFA94DC4-B226-48C3-9BC1-99BD11E93ED7 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxPUHV0ZUt1SVBqU1FKYkpKaUdWeHFxOG9KbndkeUZfY1NvcEVORlljV1o4VmlXUzQwd0tKQmtLcWtPbW9YUTBjQlNYeUh3RWg5S3hvUm9MUm41SmZVTHZ2TExQQU05dmFYMTZubngzbExBMU05bXJadGtJWE1weUlaNmtPRTlnZGQwQUthUW13cWRENTRX?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 01 Jul 2026 12:18:55 GMT
- [《台股盤後》收漲893點、日K連三紅，重返47K-新聞內容-基金 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxQOHpYUG5vUE5kMnEtOXZFLXdyUDFfclBrQ0EyTWtNUnVYUS1PaWpKWEI4UXhGdU9tVVo2X3I5dFF0MGoyTGg5OVZjUXlEVnpoWFhwNUpBTHRtYWM2Q21wS3ZXbDJJZWRiVlNqYzBXaGllRk82bHZHa01FalNnQnNNTndhRUJUTmJoQ2ZEblA1VVY?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 01 Jul 2026 07:45:00 GMT

## 新興題材：B226

摘要：新興題材：B226 相關新聞集中在：個股動態報導內容-AFA94DC4-B226-48C3-9BC1-99BD11E93ED7 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-AFA94DC4-B226-48C3-9BC1-99BD11E93ED7 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxPUHV0ZUt1SVBqU1FKYkpKaUdWeHFxOG9KbndkeUZfY1NvcEVORlljV1o4VmlXUzQwd0tKQmtLcWtPbW9YUTBjQlNYeUh3RWg5S3hvUm9MUm41SmZVTHZ2TExQQU05dmFYMTZubngzbExBMU05bXJadGtJWE1weUlaNmtPRTlnZGQwQUthUW13cWRENTRX?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 01 Jul 2026 12:18:55 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
- TWSE PER/PBR 抓取失敗：Expecting value: line 1 column 1 (char 0)
