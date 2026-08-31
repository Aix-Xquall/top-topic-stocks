# 每日股市熱門話題分析 - 2026-08-31

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **關稅與供應鏈轉移**｜正向｜熱度 4｜市場確認 100.00｜同向 2/2
2. **記憶體與 HBM 供應鏈**｜正向｜熱度 2｜市場確認 96.19｜同向 1/1
3. **半導體與晶片供應鏈**｜中性｜熱度 10｜市場確認 N/A｜同向 0/0
4. **散熱與液冷供應鏈**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
5. **AI 伺服器與資料中心**｜負向｜熱度 12｜市場確認 0.00｜同向 1/6

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.41（樣本 10）
- 5日相關係數：0.29（樣本 10）
- 同向比例：4/10

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 關稅與供應鏈轉移 | 100.00 | 2/2 | 0 | +12.57% | +20.39% |
| 記憶體與 HBM 供應鏈 | 96.19 | 1/1 | 0 | +8.73% | +9.01% |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 0.00 | 1/6 | 4 | -8.29% | -1.68% |
| 新興題材：OpenAI | 0.00 | 0/1 | 1 | -30.76% | -1.35% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價呈負相關；應檢查正負向詞庫，並降低新聞直接提及但股價背離的權重。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-08-17 | 0.49 | 0.60 | +66.67% | 12 |
| 2026-08-18 | 0.29 | 0.36 | +80.00% | 10 |
| 2026-08-19 | -0.23 | -0.33 | +30.00% | 10 |
| 2026-08-20 | -0.72 | 0.06 | +50.00% | 8 |
| 2026-08-21 | -0.48 | -0.45 | +61.54% | 13 |
| 2026-08-22 | N/A | N/A | +50.00% | 2 |
| 2026-08-24 | -0.94 | -0.77 | +60.00% | 5 |
| 2026-08-25 | 0.01 | -0.58 | +35.71% | 14 |
| 2026-08-26 | 0.08 | 0.22 | +50.00% | 16 |
| 2026-08-27 | 0.38 | 0.11 | +54.55% | 11 |
| 2026-08-28 | 0.14 | 0.12 | +56.25% | 16 |
| 2026-08-29 | -0.10 | -0.01 | +40.00% | 10 |
| 2026-08-30 | -0.52 | -0.04 | +23.08% | 13 |
| 2026-08-31 | -0.41 | 0.29 | +40.00% | 10 |

## 歷史回測摘要

- 回測日期：2026-08-31
- 近5日 3日相關：-0.15
- 近5日 5日相關：0.22
- 同向比例：+60.00%
- 權重狀態：已調整

- 方向準確度：+60.00%
- 信心排序準確度：-0.15
- 診斷：方向與信心皆需修正

調整原因：近 5 日方向與信心排序皆偏弱，降低方向詞與供應鏈推估權重，並加重背離扣分。；關鍵詞×公司後續樣本有效 5 筆，未達 30 筆，不調整樣本權重

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

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：就市論勢／AI 供應鏈 可留意 - 經濟日報；整理包／台股5萬點靠他們？ 黃仁勳概念股助漲東風 完整台廠供應鏈名單、潛在受惠股一次看 - 經濟日報；AI 需求排擠產能，對供應鏈影響為何？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AAPL 蘋果 | 產業/供應鏈推估 | +0.08 | +21.02% | +37.72% | 319.70 | 319.70 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | +0.08 | +4.12% | +3.05% | 253.00 | 289.00 | -12.46% | 同向 | 15.21 | 16.68 | 946.51B TWD / 54.19% | 2026-08-01 |

關聯理由（前 3）：
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 1 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 1 篇新聞出現相關標籤。

### 主要來源

- [就市論勢／AI 供應鏈 可留意 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9ZTVVDblpSd3A1OHFTcGJiWVAtNEt2MHBwa0pwZWRQZ09RTWM1ekxacHVoaUVhWWZZdjdJR285ZjM1bl9TZzVwLW96QVpsdlVsU1JfaVE4eHZXZ9IBX0FVX3lxTE9nRTIybXllRFl5Ykt6QXdYZms4SnUwU2VNTXJFUlM4WnplNGY4NGhTUmJSeU5VbmdOQXFPNktERkxtRUk4UTdoMmJ3Zk9oTTluTGRHamZuc1hsMzFjaGJV?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 30 Aug 2026 16:50:51 GMT
- [整理包／台股5萬點靠他們？ 黃仁勳概念股助漲東風 完整台廠供應鏈名單、潛在受惠股一次看 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBQUlViSHpPeDVlY29yaHFNNE5NcVlUQnE3ZThTcXRGNHgxYTVPOVVTRDlaTDV6Zml5WEwxVHNSeGFDcnVHUHhRSW15SzNpU0dYVDU3dThWNEVCbkZI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 29 Aug 2026 09:00:00 GMT
- [AI 需求排擠產能，對供應鏈影響為何？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMilwFBVV95cUxOMjVHOUhwVlhBZ3B0TDZla29ONDBQRkN6NGdZS3lMOUxxeVRuWUM1SEkxS2k2cDVTazRZa3kzbDdSREg4WS14MFJJQnF6OE9ESThQNlBKMGZQeWtLZEdWRUxkeUxuc1hoOV9OWHBVQnRJR2E3VTV5RXRVWHduRm4wRFlneXhyWlFoWlVKY2otaloxa3hlRW1N?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 30 Aug 2026 16:11:14 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：黃仁勳藉一場大缺貨改寫比賽規則，記憶體廠紅利沒預期那麼高了 - TechNews 科技新報；輝達70%成長帶旺記憶體！美銀喊2027年DRAM營收增幅上看80%、DDR4狂飆879% - news.cnyes.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.37 | +8.73% | +9.01% | 217.55 | 217.55 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 932.86 | 971.00 | -3.93% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | +0.28% | -6.96% | 1,484.98 | 2,335.00 | -36.40% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 同時符合主題標籤：HBM。 方向判斷命中詞：成長。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MU：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 AI memory, memory, HBM, HBM4；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 NAND, SSD, flash memory, memory；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。

### 主要來源

- [黃仁勳藉一場大缺貨改寫比賽規則，記憶體廠紅利沒預期那麼高了 - TechNews 科技新報](https://news.google.com/rss/articles/CBMirAFBVV95cUxOTEY0NzJCSHVtUW42ZHoyOHpTTjJvTmc5ZGJIR0l3LWhRRDVRSDJuRU9TM0xGNTB0amlUaE10RUlNbTJHTHN3OWxENFhIX3hLVzNwdHNnNjR4RjBpcWs2M3RJNHppWXJmbFRfNVFScHBJci1rR0h4T3VMc1BmX29aU2FocmZjTGd2MDBjY0FkUVR6QjhoQUZKRU9KdDEtQVZ6S2RDSE01Yk9ETjJG?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 29 Aug 2026 02:09:16 GMT
- [輝達70%成長帶旺記憶體！美銀喊2027年DRAM營收增幅上看80%、DDR4狂飆879% - news.cnyes.com](https://news.google.com/rss/articles/CBMiT0FVX3lxTFBRNE1TcjlvN0oxdzlLZ2szWFNDeUl2RmJlM01rSHdfWE9Qckl2b0lrSmRoa0RzXzJvalVVbEtqWkVwUTAxdUhMZXZ3YU1lSVE?oc=5) - Google News source discovery | 鉅亨網 Sun, 30 Aug 2026 07:10:06 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：國際半導體展聚焦矽光子及CPO 台積電COUPE量產受矚| 產經 - cna.com.tw；台法攜手布局半導體未來，法國以堅強陣容亮相 SEMICON - cna.com.tw；國際半導體展規模創新高資料中心CSP巨頭齊聚亮點一次看| 產經 - cna.com.tw

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | 0.00 | +0.83% | +0.41% | 2,420.00 | 2,425.00 | -0.21% | 不適用 | 86.28 | 28.05 | 467.58B TWD / 44.69% | 2026-08-01 |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 89.47 | 114.68 | -21.98% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +4.00% | +11.59% | 130.00 | 164.50 | -20.97% | 不適用 | 6.68 | 19.55 | 23.84B TWD / 18.98% | 2026-08-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +8.73% | +9.01% | 217.55 | 217.55 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 465.58 | 516.10 | -9.79% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 932.86 | 971.00 | -3.93% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | +0.28% | -6.96% | 1,484.98 | 2,335.00 | -36.40% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -2.37% | -11.65% | 368.79 | 446.77 | -17.45% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip, foundry。
- INTC：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 CPU, server CPU, x86, foundry；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 0 篇新聞出現相關標籤。

### 主要來源

- [國際半導體展聚焦矽光子及CPO 台積電COUPE量產受矚| 產經 - cna.com.tw](https://news.google.com/rss/articles/CBMiXkFVX3lxTFA4LWFsVUgtekV0TFR2UE5pNzhLa1JCLWhSQUJjeXJjcmNHWWI3MUlDZ1VwWGtZUXZyaVhhcTdKSUxZM0RBYVFVdzFxSnhvREVnMFNhcHphek9wc0libUE?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 30 Aug 2026 02:56:00 GMT
- [台法攜手布局半導體未來，法國以堅強陣容亮相 SEMICON - cna.com.tw](https://news.google.com/rss/articles/CBMiVkFVX3lxTFAtQ0xKQjh4cHpwbGJtUHBMQlpoSzgybENzaFpNaU1QWVBvRXBPZTVuRkJCQXRyeUhoLUVqLWR6cnh6VHJKMGxhTHpBU0RNbVJjTXZDWnhR?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 29 Aug 2026 04:25:16 GMT
- [國際半導體展規模創新高資料中心CSP巨頭齊聚亮點一次看| 產經 - cna.com.tw](https://news.google.com/rss/articles/CBMiXkFVX3lxTFBCMldtd0RIWEpUczNKbGx3R2FQdEowNVJCZGwwX0pNeE1vOW5DYWZzaXlGYURCM3RJRGRSQ2JzRXFLTFFWR09wdFgzUXZ5QVEyVURKSFdiV0NTRTFoWUE?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 29 Aug 2026 02:16:00 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：股價大漲7.55%！「液冷散熱大廠」上半年EPS狂賺23元 輝達GB追單加持營運 - FTNN 新聞網；AI 帶動散熱需求，全球產業鏈併購潮是否持續？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | +13.90% | +17.28% | 3,360.00 | 3,360.00 | 0.00% | 不適用 | 75.13 | 44.79 | 18.59B TWD / 57.39% | 2026-08-01 |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +8.73% | +9.01% | 217.55 | 217.55 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 2 篇新聞命中。 同時符合主題標籤：thermal。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [股價大漲7.55%！「液冷散熱大廠」上半年EPS狂賺23元 輝達GB追單加持營運 - FTNN 新聞網](https://news.google.com/rss/articles/CBMiS0FVX3lxTE11VF9ia19YbFRuZGEzczMwQ3ZYZXB1TjBjS2FFdXhEVmRGZHI5RHBCS21FNHFRQWUxOWVuWVNoUkQwMmxsZmVFWGpLaw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 29 Aug 2026 10:30:00 GMT
- [AI 帶動散熱需求，全球產業鏈併購潮是否持續？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiqwFBVV95cUxQSzRsRFhVZmp3cjJ1cHEyc2E2Z1pCazJpMWdjczAwZGlQYXlxTVhQVE80eW05aXQ1LW1FX2ZlNXl1R1kxd0FtSmVQYWZkbEN0b09WczVFUWh6N1ZsazYtWTM3bXE2dHVZeV8wSFlScFVSRGQ2YU9JUHBwdFdLdXdBd0RSbV80VHdWVGw1Rk40WkhnNFh3R3NXcFpPNjBDM0xGUi1WdkRrMUxodnc?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 30 Aug 2026 16:09:30 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：AI 財報點火台股！外資轉買、資金擴散中小型股「Risk-on」訊號浮現 | 基金天地 | 理財 - 經濟日報；Intel’s On‑Prem AI and TRACE Bet Could Be A Game Changer For Intel (INTC) - simplywall.st；國際半導體展規模創新高資料中心CSP巨頭齊聚亮點一次看| 產經 - cna.com.tw

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.54 | N/A | N/A | 89.47 | 114.68 | -21.98% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | -0.03 | +8.73% | +9.01% | 217.55 | 217.55 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | -0.06 | N/A | N/A | 465.58 | 516.10 | -9.79% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.04 | +0.83% | +0.41% | 2,420.00 | 2,425.00 | -0.21% | 未明確 | 86.28 | 28.05 | 467.58B TWD / 44.69% | 2026-08-01 |
| MSFT 微軟 | 產業/供應鏈推估 | -0.02 | +30.76% | +1.35% | 513.53 | 513.53 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -2.37% | -11.65% | 368.79 | 446.77 | -17.45% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.02 | +5.08% | +5.79% | 621.00 | 680.00 | -8.68% | 背離 | 13.92 | 44.93 | 73.78B TWD / 43.15% | 2026-08-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.02 | +6.69% | +5.15% | 3,985.00 | 4,310.00 | -7.54% | 背離 | 60.69 | 65.81 | 48.47B TWD / 12.16% | 2026-08-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：risk。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 5 篇新聞出現相關標籤。 方向判斷命中詞：risk。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 5 篇新聞出現相關標籤。 方向判斷命中詞：risk。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AI 財報點火台股！外資轉買、資金擴散中小型股「Risk-on」訊號浮現 | 基金天地 | 理財 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBGYW02cTJzb1JFTW9sejJONkRXLTNqYm93ZVNXQzdtaFN3VkFmZWZjeWo5VkwwbDl4RGdDM1htTzhWRXZmckVSSUt3SGNVVVpnRDg2UXZKbFJqZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 30 Aug 2026 10:39:43 GMT
- [Intel’s On‑Prem AI and TRACE Bet Could Be A Game Changer For Intel (INTC) - simplywall.st](https://news.google.com/rss/articles/CBMiygFBVV95cUxQTnREY1ltV290OElZb281WFRwUG0ydEROV3E1SGdGdTU0MEhBaXY2TnFvSFdfdHVlY1I5ejJfQUUxbTdnakVkNExZQTdzM3dLbzVPSlJCSC12Ty1KaVB6WUxwb2dPQWFXd1dGVUliUlRlZ2RibjlqYjI1U0lXUDZ6SEdpYmhHSXBjSkU1WXhRbVRZajVPT0ZZRDdLMW1oNzYwc3QxRUJSN0dGUzZ0LWRrcWlFVzNyMi0xb1dQbjBJbUQ2R1ZRdk5aM0lR0gHPAUFVX3lxTE9zTWpSWVJkaWFIcXp0dzZIcWNxZkJMaW1zREdRXzh3c1NiRnVSeFF4aVJTemZlMldxMGpDdjZENWQwQkhoY293SVI5QTFYRnBEXzl3eGNwV2dJVnVpczFjLTlQUzJON1J4WmpZS2kyVHJwRGJ4aU9WY3RtV3o2Z2J1eGdibXV4ckxlTnZqcmxWeHdwdmVJdnZuTWFsUUdXMWxoT3o5Vm1uSEhGYnQ0cU5SU0p2Zm1CLWpfZEFGTXRzVXF2bkdKdjgwcmprQjBLbw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 29 Aug 2026 04:43:05 GMT
- [國際半導體展規模創新高資料中心CSP巨頭齊聚亮點一次看| 產經 - cna.com.tw](https://news.google.com/rss/articles/CBMiXkFVX3lxTFBCMldtd0RIWEpUczNKbGx3R2FQdEowNVJCZGwwX0pNeE1vOW5DYWZzaXlGYURCM3RJRGRSQ2JzRXFLTFFWR09wdFgzUXZ5QVEyVURKSFdiV0NTRTFoWUE?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 29 Aug 2026 02:16:00 GMT

## 新興題材：OpenAI

摘要：新興題材：OpenAI 相關新聞集中在：OpenAI to cut off AI models for SpaceX-owned Cursor, escalating feud with Musk - Reuters；OpenAI to end model access to Cursor after acquisition by Elon Musk's SpaceX - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 新聞直接提及 | -0.24 | +30.76% | +1.35% | 513.53 | 513.53 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：新聞直接提及「OpenAI」，共 2 篇新聞命中。 方向判斷命中詞：cut。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [OpenAI to cut off AI models for SpaceX-owned Cursor, escalating feud with Musk - Reuters](https://news.google.com/rss/articles/CBMiowFBVV95cUxQRUdlVXhBU0dadjVHRG10TFFYU2wwWHdyenlGSGZkUVUtcHV2YVdrN25KS3c0cEdrWHhEY054X3c4SUszUjdDUVRXdzJwSkc2N2ZXeXFweHI5MjgtQmlZQjFiYU1TZ2p5cTB5SUE5MWttbHRJYlQ3eDlzUlFXR0JhOEFfYjd2QzF6MExhRnVnTzQ1TnA3a3FfR0tqYVVwVC1YcXZN?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 29 Aug 2026 10:20:17 GMT
- [OpenAI to end model access to Cursor after acquisition by Elon Musk's SpaceX - CNBC](https://news.google.com/rss/articles/CBMiekFVX3lxTE90bmQ0enBvenh2RFZzWDJtV2FWRnFMVzNRMEJrbG1RSmtWbnZ6MU1XcHV0TUJ1dll3YkJJM1RSMUgyRWVsV3NTeHpUV1JOeEZVb01TRkctT0c0NjZIc0haWFVTdzVkSmFLM1htanRGeVJZMmxNb2NaWnBn0gF_QVVfeXFMTnNMYVB6Q3hkc1l0NnRTSVhOeU5uT21nbUxOZDZjU2ota0tocTk2a3JjOWdxeUp0M2ttVUpHNk1ZTlB5MWp6QkR5c21aUlduUERGbzRZenhNZ1ZIQVVWTWt6RmJJdW8xcVAtRW05NnIxVGI5UE1uaVA4Q0V6NWd4cw?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 29 Aug 2026 19:05:55 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：個股動態報導內容-11019794-72EE-4044-808A-F9E55E653D1E - 5850web.moneydj.com；個股動態報導內容-459D711A-E1D3-4D32-9583-6E5E17400F06 - 5850web.moneydj.com；個股動態報導內容-3A3D0717-0D5D-43C7-833D-1D8748D19636 - 5850web.moneydj.com

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-11019794-72EE-4044-808A-F9E55E653D1E - 5850web.moneydj.com](https://news.google.com/rss/articles/CBMikgFBVV95cUxPaHdCcjRWWWlGdnVveTl5aXhEM2FPUGR2b1UtWXVMazdXMTV5OG9nVDhkaHhHTUJWSDA2S1JRZUJVN1l1Um54TVZNNy1yelozQ0RSZnJ5QlBUZTNVMUh2R2JoZDJfLUh3MGdVa3g2U3FJT2NvS2taNUgyWWNtNFFya2Q4VW8xNXdYQU4yNXZ0TXVxdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 30 Aug 2026 07:38:15 GMT
- [個股動態報導內容-459D711A-E1D3-4D32-9583-6E5E17400F06 - 5850web.moneydj.com](https://news.google.com/rss/articles/CBMikgFBVV95cUxPQW1tRTVERjQ1blNieGlIYmpFWGlfaDF4MGtXeHZyNXR4Wm91T2w4elpkOHgzY0dvc01udVdhSFVUWDJ4LUx2dDdyak1ERElOQ1JpY0ZZOTlLZEVBUVBwNy00MFdwaVVzWTFlaktTb3JXTVY1LUw4dkU2NFlMYkZTbER0OVVFMWtYeWo5RVcxdWhMZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 30 Aug 2026 08:25:26 GMT
- [個股動態報導內容-3A3D0717-0D5D-43C7-833D-1D8748D19636 - 5850web.moneydj.com](https://news.google.com/rss/articles/CBMikgFBVV95cUxPMFR3VVB5aV9ISzV6c1NVLVRXNklObFNSVVpvWDRxbUM1MTkwNHl6RUxGbldPQ2kxb0gzNkhDczZnWmV6clNKQU4yRl9kSk1xNExYcENTaDBBekFtYTZPRU1DQzRMUXYtZ1d0dDFxMUtDcnFuczViYjlWREdmalR1ZnZiTnFmU0pTNXRUa2xkdlBNUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 30 Aug 2026 07:16:11 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：法人專欄分析內容-台股 - MoneyDJ；個股動態報導內容-715F31AA-40CA-4CF8-9F14-C049031C750D - MoneyDJ；個股動態報導內容-92AB8B9E-4889-47B0-BB9A-E49599064C92 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [法人專欄分析內容-台股 - MoneyDJ](https://news.google.com/rss/articles/CBMilgFBVV95cUxQRGU4ajNBZXFSS1F5bDJjR2tscGUxdGRVbzlPd3lsYjgtMlJGbUNUa2wwYzNxSTZ4RDAzcDhkREczcDMwWWM4dUdsQldndVAzMGZDbXB1MlNDM0FkU2J4YS1RbnRyMHhrQ3kweHR1TzV6SExLUFlXZTNRS0otU1lFTHZ2bEZ1WHgxd2tFZnliaHpsZHFrblE?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 30 Aug 2026 16:02:22 GMT
- [個股動態報導內容-715F31AA-40CA-4CF8-9F14-C049031C750D - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxON1FHZ1dEX1NQMlVRbVI3NG9iX0tSU3lUckE2cnhEa3QxSG5NS0g5UWhEZTVQekF0ak5nUnFidVJtemRNRk5IeVB1Wms0VTlEdzlfS19XRDB3b0h3YWxobkstZmZGN3FNemVrS3Vpb2dHZXR3cWZzN0tta2RCUlFDZDZuRUF6cUotbDBUeVJYQXg5b0NN?oc=5) - Google News source discovery | MoneyDJ Sun, 30 Aug 2026 12:09:23 GMT
- [個股動態報導內容-92AB8B9E-4889-47B0-BB9A-E49599064C92 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxQZE4xQ21EeFBXb1JkVzgyVHYtNEtodXotZWNOZlVfLVRka0JoUjg4Nnc1amU1ajFzMkQxX05TelZmSmVzNktOSk1hM2R0WDF2RVYyVWxOSUpMbFNBREhFQU1CLXpuQkh1YXJ3aEk1NFN1ZDJrOGNPbkplOUFYUTg0TUJlelRQTTlSREJmTklyWnFWQl8w?oc=5) - Google News source discovery | MoneyDJ Sun, 30 Aug 2026 18:36:15 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
