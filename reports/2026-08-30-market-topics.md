# 每日股市熱門話題分析 - 2026-08-30

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **散熱與液冷供應鏈**｜中性｜熱度 4｜市場確認 N/A｜同向 0/0
2. **記憶體與 HBM 供應鏈**｜中性｜熱度 4｜市場確認 N/A｜同向 0/0
3. **半導體與晶片供應鏈**｜正向｜熱度 11｜市場確認 34.88｜同向 2/5
4. **AI 伺服器與資料中心**｜負向｜熱度 13｜市場確認 0.00｜同向 1/6
5. **新興題材：SpaceX**｜負向｜熱度 2｜市場確認 0.00｜同向 0/1

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.52（樣本 13）
- 5日相關係數：-0.04（樣本 13）
- 同向比例：3/13

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 散熱與液冷供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 記憶體與 HBM 供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | 34.88 | 2/5 | 1 | +2.29% | +0.48% |
| AI 伺服器與資料中心 | 0.00 | 1/6 | 4 | -8.29% | -1.68% |
| 新興題材：SpaceX | 0.00 | 0/1 | 1 | -30.76% | -1.35% |
| 新興題材：OpenAI | 0.00 | 0/1 | 1 | -30.76% | -1.35% |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價呈負相關；應檢查正負向詞庫，並降低新聞直接提及但股價背離的權重。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-08-16 | 0.37 | 0.51 | +70.00% | 10 |
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

## 歷史回測摘要

- 回測日期：2026-08-30
- 近5日 3日相關：0.07
- 近5日 5日相關：0.25
- 同向比例：+48.28%
- 權重狀態：已調整

- 方向準確度：+48.28%
- 信心排序準確度：0.07
- 診斷：低相關

調整原因：近 5 日信心分數與股價關係偏低，提高價格確認，降低寬題材推估。；關鍵詞×公司後續樣本有效 5 筆，未達 30 筆，不調整樣本權重

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

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：統一-仁愛 對 健策(3653)個股 單一券商歷史明細 - MoneyDJ；本季營收續創新高可期 法人調高奇鋐獲利預估值及目標價 | 經濟日報 - LINE TODAY；液冷進入下半場！奇鋐(3017)、雙鴻(3324)、健策(3653)獲利驅動力，準備轉移到誰身上？ - 優分析UAnalyze

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | +13.90% | +17.28% | 3,360.00 | 3,360.00 | 0.00% | 不適用 | 75.13 | 44.79 | 18.59B TWD / 57.39% | 2026-08-01 |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +8.73% | +9.01% | 217.55 | 227.98 | -4.57% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐、3017、散熱」，共 3 篇新聞命中。 同時符合主題標籤：thermal。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [統一-仁愛 對 健策(3653)個股 單一券商歷史明細 - MoneyDJ](https://news.google.com/rss/articles/CBMikwFBVV95cUxPVXpCU3paRDhJdFdOdUNUMFd3VGxGT3Z0ZlpJcFpvaVlCNlhIYzk3MTZxUTR6azRuRldJNnVhVTVKa01vWjF5YkpjOUZlNWtSYXVWbFZhWW5sNVVwa2xGTGxhZklzUEdKR3gwVXE5Wk9Cb3ZNV1ZWZW1icE11b0dDaXNvczNjSjZPak0zdGExajRqeGM?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 29 Aug 2026 04:56:23 GMT
- [本季營收續創新高可期 法人調高奇鋐獲利預估值及目標價 | 經濟日報 - LINE TODAY](https://news.google.com/rss/articles/CBMiVkFVX3lxTFBNYXFYREV6S1FaeTh6V2V4OVllbHZ2T3RLcFhjeVNSSWUtRTh1VDZjRUVjb1BDazRTWTNHSjBRS2NqY1hSem1zQTVaNncyNjlLU05MUktR?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 28 Aug 2026 08:04:59 GMT
- [液冷進入下半場！奇鋐(3017)、雙鴻(3324)、健策(3653)獲利驅動力，準備轉移到誰身上？ - 優分析UAnalyze](https://news.google.com/rss/articles/CBMiVkFVX3lxTE8xUDE2YjJRMUJnanp0U3J6cFZ4THlySnNBMDUxelZYM3NZYVU1N2NvVk5hNWRFSFh6eTFTakMzeDFvM2hfOUZCaHozNnBFUVN1SThJSFpn?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 28 Aug 2026 07:55:00 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：MU, INTC, SNDK: Chip Stocks Rally After-Hours On AMD’s Blowout Report - Stocktwits；Palo Alto Networks CEO Nikesh Arora Warns Memory ‘Supercycle’ Will Eventually Turn Cyclical, Flagging Risk For Micron, SanDisk - TradingView；黃仁勳藉一場大缺貨改寫比賽規則，記憶體廠紅利沒預期那麼高了 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | N/A | N/A | 932.86 | 971.00 | -3.93% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | +0.28% | -6.96% | 1,484.98 | 2,335.00 | -36.40% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.37 | N/A | N/A | 465.58 | 516.10 | -9.79% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.37 | N/A | N/A | 89.47 | 114.68 | -21.98% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +8.73% | +9.01% | 217.55 | 227.98 | -4.57% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron」，共 2 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：risk, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK、SanDisk」，共 2 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：risk, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [MU, INTC, SNDK: Chip Stocks Rally After-Hours On AMD’s Blowout Report - Stocktwits](https://news.google.com/rss/articles/CBMiygFBVV95cUxPeVlYaXJjQjNtTkNRQUxQTHhaLUFMbE80Uy1MeDBpV0FPdkg2SHRLdkdfVUpXM1NrNWhZSVZQQ01sa0o4T1hKdzF1clBFRlRWUmMwWGxQTDNVVFBpOVhObUc2MXpBeXBOZ0p3R0w5NGRNOHB4X0ZIXzhlT0NMbmhzc1RtdmJRTWhlRUhKSHpyVnpaU0VGMlJyU2tDcmdkTG1hWVJJbmtTVDREbzFfWDB4bjhuTGswN3lmdkdHQzY1dzFOVU41VGlBNlZn?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 29 Aug 2026 00:26:37 GMT
- [Palo Alto Networks CEO Nikesh Arora Warns Memory ‘Supercycle’ Will Eventually Turn Cyclical, Flagging Risk For Micron, SanDisk - TradingView](https://news.google.com/rss/articles/CBMikAJBVV95cUxPaURLZDB5cFFjU2RVZDd2R1ZfdkJXcjZsU2JteUxYLTk2eUNIR2VicnlrOGl6dmw2Z0xHdXZ0dVB4bkg2RzJJVExFeXR2NGVIS3lQbklHUWlTVzgxYjdFRGlSVWlEa3h6Q0lKNDZZeDN6M0s4QlNlamdpcVJwMEIydWh6MEtENE95RTE4R0xFTkotYnVIQThEM3I5UU1udEdWUGVOeVZRRlVoV29mZWF4NThuWmZQUVZoTDV1TzMzVnZQclNMSlVFZDRnRGZFdWVPdkE3dm1fUlZFdTZYVkVmOV9wakxZUnlZWW1RNVdUZHZDcE9heTlSbVU0YWVyQV9majJxUTM2R1BLZkRrdEREWQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 28 Aug 2026 07:27:05 GMT
- [黃仁勳藉一場大缺貨改寫比賽規則，記憶體廠紅利沒預期那麼高了 - TechNews 科技新報](https://news.google.com/rss/articles/CBMirAFBVV95cUxOTEY0NzJCSHVtUW42ZHoyOHpTTjJvTmc5ZGJIR0l3LWhRRDVRSDJuRU9TM0xGNTB0amlUaE10RUlNbTJHTHN3OWxENFhIX3hLVzNwdHNnNjR4RjBpcWs2M3RJNHppWXJmbFRfNVFScHBJci1rR0h4T3VMc1BmX29aU2FocmZjTGd2MDBjY0FkUVR6QjhoQUZKRU9KdDEtQVZ6S2RDSE01Yk9ETjJG?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 29 Aug 2026 02:09:16 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel Stock Rises 4.4% as Nvidia Forecast Revives AI-Chip Demand - TechStock²；國際半導體展規模創新高資料中心CSP巨頭齊聚亮點一次看| 產經 - cna.com.tw；台法攜手布局半導體未來，法國以堅強陣容亮相 SEMICON - cna.com.tw

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.52 | N/A | N/A | 89.47 | 114.68 | -21.98% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.48 | +8.73% | +9.01% | 217.55 | 227.98 | -4.57% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.04 | +0.83% | +0.41% | 2,420.00 | 2,425.00 | -0.21% | 未明確 | 86.28 | 28.05 | 467.58B TWD / 44.69% | 2026-08-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.05 | +4.00% | +11.59% | 130.00 | 164.50 | -20.97% | 同向 | 6.68 | 19.55 | 23.84B TWD / 18.98% | 2026-08-01 |
| AMD 超微 | 產業/供應鏈推估 | +0.04 | N/A | N/A | 465.58 | 516.10 | -9.79% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | +0.04 | N/A | N/A | 932.86 | 971.00 | -3.93% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.03 | +0.28% | -6.96% | 1,484.98 | 2,335.00 | -36.40% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -2.37% | -11.65% | 368.79 | 446.77 | -17.45% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 1 篇新聞出現相關標籤。

### 主要來源

- [Intel Stock Rises 4.4% as Nvidia Forecast Revives AI-Chip Demand - TechStock²](https://news.google.com/rss/articles/CBMijAFBVV95cUxNSDZXWFlocl9hUUNzM3B5dkI4R19iWDZPMloxRnlmSVdiWEEzc25SaWpoOHlsYktTQzRXS2FGd01mNlR4ZGFZZTJ0VWhJZjZfSVhxbDZXZVlON2ZFU1Z4VElkZTBDbEczT0dQc2I2OHlfMjhxa0IzOXAwUldVRFdlUXRJYkRFOW9vcmhXMg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 28 Aug 2026 05:17:05 GMT
- [國際半導體展規模創新高資料中心CSP巨頭齊聚亮點一次看| 產經 - cna.com.tw](https://news.google.com/rss/articles/CBMiXkFVX3lxTFBCMldtd0RIWEpUczNKbGx3R2FQdEowNVJCZGwwX0pNeE1vOW5DYWZzaXlGYURCM3RJRGRSQ2JzRXFLTFFWR09wdFgzUXZ5QVEyVURKSFdiV0NTRTFoWUE?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 29 Aug 2026 02:16:00 GMT
- [台法攜手布局半導體未來，法國以堅強陣容亮相 SEMICON - cna.com.tw](https://news.google.com/rss/articles/CBMiVkFVX3lxTFAtQ0xKQjh4cHpwbGJtUHBMQlpoSzgybENzaFpNaU1QWVBvRXBPZTVuRkJCQXRyeUhoLUVqLWR6cnh6VHJKMGxhTHpBU0RNbVJjTXZDWnhR?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 29 Aug 2026 04:25:16 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：外資錢進來了！台股周漲1,107點 這周最愛的竟不是 AI 股 - 經濟日報；Marvell Leads AI Stocks Lower After Earnings That Narrowly Topped Estimates - Investopedia；Intel Stock Rises 4.4% as Nvidia Forecast Revives AI-Chip Demand - TechStock²

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | -0.28 | +8.73% | +9.01% | 217.55 | 227.98 | -4.57% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | -0.56 | N/A | N/A | 89.47 | 114.68 | -21.98% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | -0.06 | N/A | N/A | 465.58 | 516.10 | -9.79% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.04 | +0.83% | +0.41% | 2,420.00 | 2,425.00 | -0.21% | 未明確 | 86.28 | 28.05 | 467.58B TWD / 44.69% | 2026-08-01 |
| MSFT 微軟 | 產業/供應鏈推估 | -0.02 | +30.76% | +1.35% | 513.53 | 513.53 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -2.37% | -11.65% | 368.79 | 446.77 | -17.45% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.02 | +5.08% | +5.79% | 621.00 | 680.00 | -8.68% | 背離 | 13.92 | 44.93 | 73.78B TWD / 43.15% | 2026-08-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.02 | +6.69% | +5.15% | 3,985.00 | 4,310.00 | -7.54% | 背離 | 60.69 | 65.81 | 48.47B TWD / 12.16% | 2026-08-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。 方向判斷命中詞：lower。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：lower。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 5 篇新聞出現相關標籤。 方向判斷命中詞：lower。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [外資錢進來了！台股周漲1,107點 這周最愛的竟不是 AI 股 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5DWFhlckNUVEhYRzY1blVQV18yRHJ1V0ZIbDFKeTZsbVgxY2x5eXJ6Sm8wTF84VVlZZzRIMW45ZXJXQUFZZmFoaG45dHZwdmVZVHYyazJhb2dkZ9IBX0FVX3lxTFBmbTVkaWFLdTNZWTA5aHRJYldIZ1pPSmFxRU5SQ2U1NWdZRW1HQjhzMFZ4dmJDR3BaWmQtb2dEeXk4TGxxcWdtRXgtM3BKaENScV8zVDd3eE5hdU93clpJ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 28 Aug 2026 09:00:00 GMT
- [Marvell Leads AI Stocks Lower After Earnings That Narrowly Topped Estimates - Investopedia](https://news.google.com/rss/articles/CBMixgFBVV95cUxPUFlkN0tIUUo4RExHY3F0b2xBUzlBRlZ4Q3E3Z2x5RXV2UlM3XzRzNzJXZXpkbWhNOEFjSk5FWHJVN1FUS3plQmt1R1NQQ2pzNTVWUTFMMDQydEt0RF9CY1VlRVpoMm9POG5kWGdUdldQaEZvQ1oxNi1sLVRLNjF1Qkt4X1U2alNRM01RcnUwTE02X0phQjFIZnlxbG85SHZPOFE2LS1XVkRKZjRQSENyMHJWNHZYdlJkekY3akhMSXVYZ09kRUE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 28 Aug 2026 13:54:57 GMT
- [Intel Stock Rises 4.4% as Nvidia Forecast Revives AI-Chip Demand - TechStock²](https://news.google.com/rss/articles/CBMijAFBVV95cUxNSDZXWFlocl9hUUNzM3B5dkI4R19iWDZPMloxRnlmSVdiWEEzc25SaWpoOHlsYktTQzRXS2FGd01mNlR4ZGFZZTJ0VWhJZjZfSVhxbDZXZVlON2ZFU1Z4VElkZTBDbEczT0dQc2I2OHlfMjhxa0IzOXAwUldVRFdlUXRJYkRFOW9vcmhXMg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 28 Aug 2026 05:17:05 GMT

## 新興題材：SpaceX

摘要：新興題材：SpaceX 相關新聞集中在：OpenAI to cut off AI models for SpaceX-owned Cursor, escalating feud with Musk - Reuters；OpenAI to end model access to Cursor after acquisition by Elon Musk's SpaceX - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 新聞直接提及 | -0.26 | +30.76% | +1.35% | 513.53 | 513.53 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：新聞直接提及「OpenAI」，共 2 篇新聞命中。 方向判斷命中詞：cut。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [OpenAI to cut off AI models for SpaceX-owned Cursor, escalating feud with Musk - Reuters](https://news.google.com/rss/articles/CBMiowFBVV95cUxQRUdlVXhBU0dadjVHRG10TFFYU2wwWHdyenlGSGZkUVUtcHV2YVdrN25KS3c0cEdrWHhEY054X3c4SUszUjdDUVRXdzJwSkc2N2ZXeXFweHI5MjgtQmlZQjFiYU1TZ2p5cTB5SUE5MWttbHRJYlQ3eDlzUlFXR0JhOEFfYjd2QzF6MExhRnVnTzQ1TnA3a3FfR0tqYVVwVC1YcXZN?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 29 Aug 2026 07:05:19 GMT
- [OpenAI to end model access to Cursor after acquisition by Elon Musk's SpaceX - CNBC](https://news.google.com/rss/articles/CBMiekFVX3lxTE90bmQ0enBvenh2RFZzWDJtV2FWRnFMVzNRMEJrbG1RSmtWbnZ6MU1XcHV0TUJ1dll3YkJJM1RSMUgyRWVsV3NTeHpUV1JOeEZVb01TRkctT0c0NjZIc0haWFVTdzVkSmFLM1htanRGeVJZMmxNb2NaWnBn0gF_QVVfeXFMTnNMYVB6Q3hkc1l0NnRTSVhOeU5uT21nbUxOZDZjU2ota0tocTk2a3JjOWdxeUp0M2ttVUpHNk1ZTlB5MWp6QkR5c21aUlduUERGbzRZenhNZ1ZIQVVWTWt6RmJJdW8xcVAtRW05NnIxVGI5UE1uaVA4Q0V6NWd4cw?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 29 Aug 2026 19:05:55 GMT

## 新興題材：OpenAI

摘要：新興題材：OpenAI 相關新聞集中在：OpenAI to cut off AI models for SpaceX-owned Cursor, escalating feud with Musk - Reuters；OpenAI to end model access to Cursor after acquisition by Elon Musk's SpaceX - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 新聞直接提及 | -0.26 | +30.76% | +1.35% | 513.53 | 513.53 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：新聞直接提及「OpenAI」，共 2 篇新聞命中。 方向判斷命中詞：cut。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [OpenAI to cut off AI models for SpaceX-owned Cursor, escalating feud with Musk - Reuters](https://news.google.com/rss/articles/CBMiowFBVV95cUxQRUdlVXhBU0dadjVHRG10TFFYU2wwWHdyenlGSGZkUVUtcHV2YVdrN25KS3c0cEdrWHhEY054X3c4SUszUjdDUVRXdzJwSkc2N2ZXeXFweHI5MjgtQmlZQjFiYU1TZ2p5cTB5SUE5MWttbHRJYlQ3eDlzUlFXR0JhOEFfYjd2QzF6MExhRnVnTzQ1TnA3a3FfR0tqYVVwVC1YcXZN?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 29 Aug 2026 07:05:19 GMT
- [OpenAI to end model access to Cursor after acquisition by Elon Musk's SpaceX - CNBC](https://news.google.com/rss/articles/CBMiekFVX3lxTE90bmQ0enBvenh2RFZzWDJtV2FWRnFMVzNRMEJrbG1RSmtWbnZ6MU1XcHV0TUJ1dll3YkJJM1RSMUgyRWVsV3NTeHpUV1JOeEZVb01TRkctT0c0NjZIc0haWFVTdzVkSmFLM1htanRGeVJZMmxNb2NaWnBn0gF_QVVfeXFMTnNMYVB6Q3hkc1l0NnRTSVhOeU5uT21nbUxOZDZjU2ota0tocTk2a3JjOWdxeUp0M2ttVUpHNk1ZTlB5MWp6QkR5c21aUlduUERGbzRZenhNZ1ZIQVVWTWt6RmJJdW8xcVAtRW05NnIxVGI5UE1uaVA4Q0V6NWd4cw?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 29 Aug 2026 19:05:55 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：國泰-松江 對 聯強(2347)個股 單一券商歷史明細 - MoneyDJ；個股主力券商-4739 - MoneyDJ；宏遠-台中 對 友達(2409)個股 單一券商歷史明細 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [國泰-松江 對 聯強(2347)個股 單一券商歷史明細 - MoneyDJ](https://news.google.com/rss/articles/CBMigwFBVV95cUxQeGwxYW9rejFva2NCOU8wbm5NU3ktTHJnTTU5d1d2eVJORUlmcWFOVkdxNnFGOEJacWF3OWJkVDN3R3RfUndwakhFR3lIT1hzWTlRZ003RVV1TXN0TWd4empaY1lGblpoTjdRUjBPXzhwSm11dEtYdnRjLS1Qazdna281WQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 29 Aug 2026 15:27:39 GMT
- [個股主力券商-4739 - MoneyDJ](https://news.google.com/rss/articles/CBMikwFBVV95cUxONTR2U2QyOUM5aUhmVVZNX28yOEgyd2V1c2NacHdZM1ZnTWNGaUd3OHA1TXNVdGJNTVhkeFRQTDljenV0M0dRLUFSUXA0b3c5R3VPMnJSa3l4TlFramducFlxZldreTlvZ01HdlhpajFUaGRHNUtZWUlqMlBIUHd2aUZUZGQ3aVcwcDUzQlNlb1pGUzg?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 29 Aug 2026 17:57:23 GMT
- [宏遠-台中 對 友達(2409)個股 單一券商歷史明細 - MoneyDJ](https://news.google.com/rss/articles/CBMikwFBVV95cUxOTHBtd2dVQlZoY21JZlVzTm54UEd5b0ZLNEY4N2dwZURfeERxRGlPZkVaRVVjcVR0MG1Za2VWZEFsbDFLcjdxWURQSmlBYnM3UW9rYkpXclBFVzljRGcxVVlXMWFrbjZCRzREd3ZyVEl3R3FGaEhnUGRaNDJsOVNocHRIYlpsZzZHTXBMS0cwLTQ5Mk0?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 29 Aug 2026 05:22:33 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：群益金鼎-大甲 對 晶采(8049)個股 單一券商歷史明細 - kgieworld.moneydj.com；台股擂台／挑戰者「華冠北極星」劉彥良 本周選禾伸堂、國巨 | 台股擂台 | 證券 - 經濟日報；台股擂台／挑戰者「Q女王」劉良梅 本周挑環球晶、鉅陞 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [群益金鼎-大甲 對 晶采(8049)個股 單一券商歷史明細 - kgieworld.moneydj.com](https://news.google.com/rss/articles/CBMilAFBVV95cUxOZU9IeWR1TTVQd21jdkg0N2I4TlRmUEVHdklMdDYxQi1EX2NXNUU1cTEwbnlmWDVvMEh1RXFfQ29RdWVYbURXNEJweGVJc1FsQkRPWEZpLVNaTWRDMGU1U0FvTm5WZFZ3ZTNUdG5JZ1YteU04dGlJVzB3eTBUdHZLOTF0ZXpXcm54NGE5MkxOTnJqMDJs?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 29 Aug 2026 21:39:53 GMT
- [台股擂台／挑戰者「華冠北極星」劉彥良 本周選禾伸堂、國巨 | 台股擂台 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTE1fYU5VdEhleUNULXFDYnB4QUIwcTBVQTNaWXJmbTc2T0U4WVNFY2V1RlJ1a0V6bzk3WDRKdmh5OG5hX0lFTjEzdXZzVEJZVWstb3VqMmdlMXFlV0Zs?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 29 Aug 2026 15:43:48 GMT
- [台股擂台／挑戰者「Q女王」劉良梅 本周挑環球晶、鉅陞 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBpNi1od3pYNU1xRUxES2gyY2VERnNFT2ZvNlFENE9CVko0dW1CYl9MNC1FUFJsZF9mWjhXb0xLbmVBOHg5RllCYzRQQ3JHLURGQXBKVGRPaUhwN3pD?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 29 Aug 2026 15:45:01 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
