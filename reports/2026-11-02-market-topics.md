# 每日股市熱門話題分析 - 2026-11-02

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **散熱與液冷供應鏈**｜正向｜熱度 2｜市場確認 36.23｜同向 1/2
2. **AI 伺服器與資料中心**｜正向｜熱度 12｜市場確認 10.12｜同向 3/8
3. **關稅與供應鏈轉移**｜正向｜熱度 3｜市場確認 0.00｜同向 1/3
4. **新興題材：鴻海AI伺服器機架產能**｜正向｜熱度 2｜市場確認 0.00｜同向 0/2
5. **新興題材：Q4營收**｜正向｜熱度 2｜市場確認 0.00｜同向 0/2

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.15（樣本 18）
- 5日相關係數：-0.06（樣本 17）
- 同向比例：5/18

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 散熱與液冷供應鏈 | 36.23 | 1/2 | 1 | +0.41% | -3.71% |
| AI 伺服器與資料中心 | 10.12 | 3/8 | 5 | -5.38% | +4.04% |
| 關稅與供應鏈轉移 | 0.00 | 1/3 | 2 | -13.99% | +18.99% |
| 新興題材：鴻海AI伺服器機架產能 | 0.00 | 0/2 | 1 | -0.97% | -3.62% |
| 新興題材：Q4營收 | 0.00 | 0/2 | 1 | -0.97% | -3.62% |
| 新興題材：OpenAI | 0.00 | 0/1 | 1 | -15.92% | -6.08% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價呈負相關；應檢查正負向詞庫，並降低新聞直接提及但股價背離的權重。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-10-20 | 0.09 | -0.81 | +69.23% | 13 |
| 2026-10-21 | -0.25 | 0.23 | +5.56% | 18 |
| 2026-10-22 | 0.02 | -0.21 | +38.89% | 18 |
| 2026-10-23 | 0.35 | 0.29 | +78.95% | 19 |
| 2026-10-24 | 0.09 | -0.31 | +70.00% | 20 |
| 2026-10-25 | 0.41 | 0.78 | +64.29% | 14 |
| 2026-10-26 | 0.27 | -0.25 | +36.36% | 11 |
| 2026-10-27 | 0.07 | 0.31 | +50.00% | 18 |
| 2026-10-28 | -0.30 | 0.47 | +20.00% | 15 |
| 2026-10-29 | -0.05 | 0.04 | +42.86% | 14 |
| 2026-10-30 | -0.00 | -0.05 | +47.62% | 21 |
| 2026-10-31 | 0.50 | -0.68 | +80.00% | 15 |
| 2026-11-01 | 0.47 | -0.40 | +85.71% | 14 |
| 2026-11-02 | -0.15 | -0.06 | +27.78% | 18 |

## 歷史回測摘要

- 回測日期：2026-11-02
- 近5日 3日相關：-0.10
- 近5日 5日相關：-0.07
- 同向比例：+40.00%
- 權重狀態：未調整

- 方向準確度：+40.00%
- 信心排序準確度：-0.10
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

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：輝達Rubin液冷商機升溫！奇鋐、雙鴻、健策、富世達等台廠受惠- 日報 - 工商時報；Google 測試在太空部屬 AI 伺服器，每 15 分鐘要關機散熱關鍵 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.26 | -1.12% | -4.33% | 3,095.00 | 3,435.00 | -9.90% | 背離 | 75.13 | 41.26 | 21.02B TWD / 44.92% | 2026-10-01 |
| NVDA 輝達 | 新聞直接提及 | +0.42 | +1.94% | -3.08% | 204.64 | 228.38 | -10.39% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐、散熱」，共 2 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：受惠。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [輝達Rubin液冷商機升溫！奇鋐、雙鴻、健策、富世達等台廠受惠- 日報 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5HT1p1WG5NdFJWdDgwSFp1ckFaMUNsTGdSTzZaVDhOTWtIQl90Rmh4SHZNTlIxUTdIcl9LTl9jR0s2cGpKR2xSdWpEUzRwZlFyQlNTblVuUTRGWFllcGsw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 01 Nov 2026 19:00:00 GMT
- [Google 測試在太空部屬 AI 伺服器，每 15 分鐘要關機散熱關鍵 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiigFBVV95cUxNekhPRDdTMk9DbGhhQlU3bll2V2pSazhEOWVodFdIX0lYdC0zWm5nUEV3MUZDcS1TaFVrdWpkOGJWWjFhMk9tVk1ZamFETHhxQnQ3NXBBSXcxLVNaTkJIM0pjOEJ0bllXQ0VtOG9LaGRCT0dPZTZ3eVBZTVBCSEc4ai1sVWpheWlJanc?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 02 Nov 2026 01:02:24 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：SpaceX太空資料中心攜手輝達上太空，伺服器規格五大變化，廣達、台達電等8檔成觀察焦點｜產業熱話 - 永豐金證券；AI 寫程式又快又多，漏洞風險與「責任歸屬」成企業開發新難題 - TechNews 科技新報；讓 AI 代理拿假金鑰辦事，機密管理新創 Infisical 完成 4 千萬美元 B 輪募資 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.55 | +1.94% | -3.08% | 204.64 | 228.38 | -10.39% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 產業/供應鏈推估 | +0.04 | -42.66% | +62.13% | 65.76 | 114.68 | -42.66% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.03 | -2.19% | N/A | 504.80 | 516.10 | -2.19% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.03 | -1.25% | -2.07% | 2,370.00 | 2,480.00 | -4.44% | 背離 | 86.28 | 27.47 | 511.86B TWD / 54.65% | 2026-10-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | +15.92% | +6.08% | 521.91 | 521.91 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -16.24% | -27.01% | 326.08 | 446.77 | -27.01% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.04 | +2.61% | -2.34% | 668.00 | 703.00 | -4.98% | 同向 | 13.92 | 48.34 | 88.13B TWD / 45.52% | 2026-10-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.02 | -1.14% | -5.43% | 3,915.00 | 4,920.00 | -20.43% | 背離 | 60.69 | 64.66 | 55.40B TWD / 1.97% | 2026-10-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。 方向判斷命中詞：受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 5 篇新聞出現相關標籤。 方向判斷命中詞：受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 5 篇新聞出現相關標籤。 方向判斷命中詞：受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [SpaceX太空資料中心攜手輝達上太空，伺服器規格五大變化，廣達、台達電等8檔成觀察焦點｜產業熱話 - 永豐金證券](https://news.google.com/rss/articles/CBMi0wRBVV95cUxOVEljZDEzaHlOWkl0LUhhQ2dnUF9XY1NjenNyeWRacnZvVXU0UnBNY1lWZ2RCR0dIZG1lbEQ1VDZ0UzA2MWp1TjlINVFlMHJTMTAydDYzMXAxZUpPYWNSU2RkYURWeVVtREs2THo5MjNua2VzSllLdEZaZU1iOFFNYnI2MkZqeWpQNlkxRHVLcEJhU3dXcEZEZHg4SVNoRjczaEc1dnFhUXdfSnBwMW5SaFhRUk15Zmw0MjByUl9ENVE3NFdQSHhXZzFLVWZJaUl0TjNyc0hKQ0FxNTZLNFVaQTkzZDc4LVZJekhJUXI4eUt0blV6Qno1c0ozNzZ2ZVVJZHBXWThhdkt0UHdzSkhiOFpicjV0bE9QTmlLSEw1dEVwRl94RUhMelFrMTlreEFJSVdrUk5MNVI1dHZ5Q3pfZ196bFUxNG1Mdzg2OWdSSTFnYXVHZ2NPVTV4UXl4b0YxZWFmNXRWQ2FVOVh5Qm9EN0Z5UzZzUnVlTjhobGlvanlmWkZKREhRRmFFM29YWDFsUHhhTWxfejlsSVlYbXc4ZHdEV0hvV0xGZVBQY25CWHBSZExoOVJra3IzbnU1VVRvVVQ5SnM4TFBzMWtFZ1o5YnYtMk1QVC1lSE1CSnRyMy1xa2lYRjE3YXQta2ZsMnpIS0ZFcFRLbXZNQmZlM1lZTU91SUJ0aElfYVlzRWlRbVRpOFNhQUlyNHlYRlEzMHdWbDRXZ2Z3ODNhOWdDVEFVN25RSnVINS15bS1kSE5RRjYyLVRSUWpQVXVtTnpPek5GNk5B?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 01 Nov 2026 08:36:35 GMT
- [AI 寫程式又快又多，漏洞風險與「責任歸屬」成企業開發新難題 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiqgFBVV95cUxNUDZJdkQ1MXZfWFFVdEZVTnY4OEcyeTlYRjNCZGpIeWpXR3A2ZmdoZHNRc1NBSXc0Z3FsNFAtUDh3RUdZeXFNTG55OWVndzN1S044YVVHdGJWaFJZaHJ2SXZ5UHR5Unl4RDhHbENqblc0V1UwdWdhYkl1QjA1dEE2Z0k5Z1Y3aF9KWVZldkhTZTEzaGE1aHVwQ1p6Vk5wYzlnVUlkU08wR0E5UQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 02 Nov 2026 00:20:33 GMT
- [讓 AI 代理拿假金鑰辦事，機密管理新創 Infisical 完成 4 千萬美元 B 輪募資 - TechNews 科技新報](https://news.google.com/rss/articles/CBMitwFBVV95cUxQeU9fYWQ5OGMwWThQM2JaZkVTTDljT1ZvcHF0WlY5ZThTb2FBSTU2NGxvcmgyaGFRc0VKcjFQa2t2UzBPTE9EaEJCUmxya2xUY3R5VTRTV29WODVvQVh5cW5fRFdIbGlzYUFmczlQT1BpbTJFSEEwUnR0c1lQVVhaQ0dsV29sMXVBVmFYSFN1QWpnRWdkUnhtS1NQZlhEZ2luTjVPN0dxZ045alFBTHkyYms5RXJOX1k?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 01 Nov 2026 23:50:07 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：美股激烈反應 CSP 與 Intel 財報 分析師看好台股 AI 供應鏈 - 經濟日報；整理包／黃仁勳概念股笑了！輝達季度財報超預期 完整台廠供應鏈名單、潛在受惠股一次看 - 經濟日報；Hot Chips 2026重點解析：AI競爭從晶片走向機櫃，台積電、世芯-KY等14檔台廠供應鏈｜產業熱話｜豐雲學堂2026 年 10 月 - 永豐金證券

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.42 | +1.94% | -3.08% | 204.64 | 228.38 | -10.39% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.21 | -42.66% | +62.13% | 65.76 | 114.68 | -42.66% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | +0.21 | -1.25% | -2.07% | 2,370.00 | 2,480.00 | -4.44% | 背離 | 86.28 | 27.47 | 511.86B TWD / 54.65% | 2026-10-01 |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +10.44% | +23.59% | 344.63 | 344.63 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | -0.81% | -1.80% | 245.50 | 289.00 | -15.05% | 不適用 | 15.21 | 16.18 | 1158.63B TWD / 38.42% | 2026-10-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。

### 主要來源

- [美股激烈反應 CSP 與 Intel 財報 分析師看好台股 AI 供應鏈 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9ITV96MDl5dnJ6RkJiOWtoZ0kwRDNxc2paWTJScDVRZUlRaTdWSXU4NXExdldHemNGSjdIWlc3QmQtYTVRWktpVG9yM1E1TzJwQWJhR0RFcGtjZ9IBX0FVX3lxTE03MlJXanhmd0pCQ2lMcWpnVEtZaHZkOE12bzlxY28yVW80ejNMX0dZb3Bqc2xmcjhmeUktRVR3VVRZRDBrcUU4dDQ4XzFkeXhPb21QOWxZWEczZXlfbk5v?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 01 Nov 2026 02:33:49 GMT
- [整理包／黃仁勳概念股笑了！輝達季度財報超預期 完整台廠供應鏈名單、潛在受惠股一次看 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBQUlViSHpPeDVlY29yaHFNNE5NcVlUQnE3ZThTcXRGNHgxYTVPOVVTRDlaTDV6Zml5WEwxVHNSeGFDcnVHUHhRSW15SzNpU0dYVDU3dThWNEVCbkZI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 31 Oct 2026 09:00:00 GMT
- [Hot Chips 2026重點解析：AI競爭從晶片走向機櫃，台積電、世芯-KY等14檔台廠供應鏈｜產業熱話｜豐雲學堂2026 年 10 月 - 永豐金證券](https://news.google.com/rss/articles/CBMi-gNBVV95cUxQUFV6TGVHbVd6aHlNN3lVZW1KX21mVkZEV0hHQlY4WlBhNVhhQWJJTGlmOHQwS2Nic1pySHp2ZVpaY0w5VHhRbHNMSjdzLWR1Y1NlTHN0b2FTdWlQMk5Pb3d2N01maU1HZGF1V3ZNMzNZR1ZlV056RnVBWnhpckpDeVpaaGUtX0tiZXZOUXdZak5vU1Q1RHM2TUxFUy1xTHRCandoNHBUMldrMkQ2LXFEd1lIUnR0WEhBSGtkbS1FNDh2ZjZ1cGVUSndTYjlMQk5GTFNwZ2x1b2VwTVFPbUxmelZYdlZERTd3R3lTeVpVQlpsNG1xdnlPN0ExVnJPS2JweWJEejFWZm9vb3dTb3d5SjNhSEFTMHJzM1dmUkJ3TjdOTTBhME5GdDFoRUJQTjVhWWdWb3prYUlkeDF3c0thaWU5eUFPUlh4bFl5Rk51cWVEUnNGSHI0NmJKdlZibWZmTEVVM0o0ZlZRcjd0bXZDY2VhanRZdHJJVmVOelE5MGpPNjRfc0JLd2hxdGVQOGpBQ19acFl2UW9MdWR6NDJIMjUyRUhnR0s2dHFGSk14TkJQdHFKRzlOT0luZlZra0I0a2tROGxKc3FCRUhuNkZ0VHVuc2R4NlMzM19yOGNfMndFcHVkcFEwdHp6eDZPc21YcWZGQmdTdHNWdw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 31 Oct 2026 07:00:00 GMT

## 新興題材：鴻海AI伺服器機架產能

摘要：新興題材：鴻海AI伺服器機架產能 相關新聞集中在：〈台股盤前要聞〉鴻海AI伺服器機架產能翻倍、聯發科ASIC Q4營收上修至25億美元 - Yahoo股市；〈台股盤前要聞〉鴻海AI伺服器機架產能翻倍、聯發科ASIC Q4營收上修至25億美元 - 鉅亨網

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2317 鴻海 | 新聞直接提及 | +0.38 | -0.81% | -1.80% | 245.50 | 289.00 | -15.05% | 未明確 | 15.21 | 16.18 | 1158.63B TWD / 38.42% | 2026-10-01 |
| 2454 聯發科 | 新聞直接提及 | +0.25 | -1.14% | -5.43% | 3,915.00 | 4,920.00 | -20.43% | 背離 | 60.69 | 64.66 | 55.40B TWD / 1.97% | 2026-10-01 |

關聯理由（前 3）：
- 2317：新聞直接提及「鴻海」，共 2 篇新聞命中。 方向判斷命中詞：上修。
- 2454：新聞直接提及「聯發科」，共 2 篇新聞命中。 方向判斷命中詞：上修。

### 主要來源

- [〈台股盤前要聞〉鴻海AI伺服器機架產能翻倍、聯發科ASIC Q4營收上修至25億美元 - Yahoo股市](https://news.google.com/rss/articles/CBMivANBVV95cUxPaEFXX0oyYVZwTmp4X25pQkROaFN1REpuMEh1VGZiOGxBbUprUGh4dDVsR1BVdGhKN2pXTXBudWNtT3RjaTFfNnBObEtqYTVpZ3hFT0F0eTM5WU5lTjE4dERQSXJyVlY3dkpEbGdLR0JvM0NOR3dNa2M0VjFheGhyOXJ1YjFrRXNiSER0NU0zU0p5UjZfXzdRU1JGZWFTaFpXMjg2bFZFWkl3MzN6MmdwRjZhV0M5bEJaTlRtQ09oLXpELWc5ZHhhQ1RMQXp6WUFkMkhfY2huZHlwU1U3Uy1YYkhrUC1vX3BzV3l4Y08xZ0RYYXExX1dabFNpdGljLUUtSVJfazB3Rk9iVFpGTERjeDlNMlhXRlBaVWVWdzBsVmpPUktyQ0VoUmFPbHhSaEQtRWFrd2Z0M0RQRkRYUU5ZMUtTcGFzRmJ4bUlJdEFONHZIN3M2RExQOHNCeWF0OGZ1OTlDakNxSmxBWi1XOEJuaHdoaEx4LVhIRWM5dzR5QzIzLXNQVEJDd2I4bWktak1fN3hPTnV2UTJPdXBFcHpMNFhnSTYtcGhnV3AxSmh5Z0xGem5jcTdDVHJxR1k?oc=5) - Google News source discovery | Yahoo 奇摩股市 Sun, 01 Nov 2026 21:10:03 GMT
- [〈台股盤前要聞〉鴻海AI伺服器機架產能翻倍、聯發科ASIC Q4營收上修至25億美元 - 鉅亨網](https://news.google.com/rss/articles/CBMiT0FVX3lxTE5jS1Rra3RlLVBiT1h6Ynl6TUhkMVhGTGNGNzJBekV2dmhWbGloazVsekVkOXFwb1ItRUtYbGNEc3BLSVllMmRYUDkzeTB1RkE?oc=5) - Google News source discovery | 鉅亨網 Sun, 01 Nov 2026 21:10:42 GMT

## 新興題材：Q4營收

摘要：新興題材：Q4營收 相關新聞集中在：〈台股盤前要聞〉鴻海AI伺服器機架產能翻倍、聯發科ASIC Q4營收上修至25億美元 - Yahoo股市；〈台股盤前要聞〉鴻海AI伺服器機架產能翻倍、聯發科ASIC Q4營收上修至25億美元 - 鉅亨網

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2317 鴻海 | 新聞直接提及 | +0.38 | -0.81% | -1.80% | 245.50 | 289.00 | -15.05% | 未明確 | 15.21 | 16.18 | 1158.63B TWD / 38.42% | 2026-10-01 |
| 2454 聯發科 | 新聞直接提及 | +0.25 | -1.14% | -5.43% | 3,915.00 | 4,920.00 | -20.43% | 背離 | 60.69 | 64.66 | 55.40B TWD / 1.97% | 2026-10-01 |

關聯理由（前 3）：
- 2317：新聞直接提及「鴻海」，共 2 篇新聞命中。 方向判斷命中詞：上修。
- 2454：新聞直接提及「聯發科」，共 2 篇新聞命中。 方向判斷命中詞：上修。

### 主要來源

- [〈台股盤前要聞〉鴻海AI伺服器機架產能翻倍、聯發科ASIC Q4營收上修至25億美元 - Yahoo股市](https://news.google.com/rss/articles/CBMivANBVV95cUxPaEFXX0oyYVZwTmp4X25pQkROaFN1REpuMEh1VGZiOGxBbUprUGh4dDVsR1BVdGhKN2pXTXBudWNtT3RjaTFfNnBObEtqYTVpZ3hFT0F0eTM5WU5lTjE4dERQSXJyVlY3dkpEbGdLR0JvM0NOR3dNa2M0VjFheGhyOXJ1YjFrRXNiSER0NU0zU0p5UjZfXzdRU1JGZWFTaFpXMjg2bFZFWkl3MzN6MmdwRjZhV0M5bEJaTlRtQ09oLXpELWc5ZHhhQ1RMQXp6WUFkMkhfY2huZHlwU1U3Uy1YYkhrUC1vX3BzV3l4Y08xZ0RYYXExX1dabFNpdGljLUUtSVJfazB3Rk9iVFpGTERjeDlNMlhXRlBaVWVWdzBsVmpPUktyQ0VoUmFPbHhSaEQtRWFrd2Z0M0RQRkRYUU5ZMUtTcGFzRmJ4bUlJdEFONHZIN3M2RExQOHNCeWF0OGZ1OTlDakNxSmxBWi1XOEJuaHdoaEx4LVhIRWM5dzR5QzIzLXNQVEJDd2I4bWktak1fN3hPTnV2UTJPdXBFcHpMNFhnSTYtcGhnV3AxSmh5Z0xGem5jcTdDVHJxR1k?oc=5) - Google News source discovery | Yahoo 奇摩股市 Sun, 01 Nov 2026 21:10:03 GMT
- [〈台股盤前要聞〉鴻海AI伺服器機架產能翻倍、聯發科ASIC Q4營收上修至25億美元 - 鉅亨網](https://news.google.com/rss/articles/CBMiT0FVX3lxTE5jS1Rra3RlLVBiT1h6Ynl6TUhkMVhGTGNGNzJBekV2dmhWbGloazVsekVkOXFwb1ItRUtYbGNEc3BLSVllMmRYUDkzeTB1RkE?oc=5) - Google News source discovery | 鉅亨網 Sun, 01 Nov 2026 21:10:42 GMT

## 新興題材：OpenAI

摘要：新興題材：OpenAI 相關新聞集中在：AI 回報疑慮衝擊 OpenAI 融資目標大縮水百億美元 - TechNews 科技新報；OpenAI slashes funding target by $10 billion amid tech rout, FT reports - Reuters

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 新聞直接提及 | -0.25 | +15.92% | +6.08% | 521.91 | 521.91 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：新聞直接提及「OpenAI」，共 2 篇新聞命中。 方向判斷命中詞：縮水, 衝擊。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AI 回報疑慮衝擊 OpenAI 融資目標大縮水百億美元 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiowFBVV95cUxNTHBicVZBZjVQWU9pbG16NVVkZmpTOGE5cDd4WEk3LURrN0lBMUstVnN0LWl1NEcySi1WWGU1elNxQzBQaThZcnBuWl8tMERIMVhRZ3kxVE9mVnp4dHhURXpjLTBWSERNX0w0QmpZdzlpa2tHXzVRNzNUMFhFQzhwckVESWp6cGJDRlRRUi1Nekg2SHIyNUF3NDdDVzBXaGYxeTBr?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 02 Nov 2026 00:28:43 GMT
- [OpenAI slashes funding target by $10 billion amid tech rout, FT reports - Reuters](https://news.google.com/rss/articles/CBMinAFBVV95cUxNTWw3N0l5dm5KUi1FQmllTEpEeUdkY1k5TVlFNTlnWWFlbTgtdUJfZE9RMjZiQlJEVXU2VFo2blVaWk1MZzNYMm9OYmdrSngtSk02YnhKNDdVMVZkS3hIMHpWZ2dnRjJZWjBzQ0lFRU4ySFFUQzdTdnUzN3JETGtCYlo3Y3kxeGJseG5veVJMSVVCRDVPYzB3TXQyaFE?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sat, 31 Oct 2026 00:17:00 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：美期中選舉逼近、美股上周五重挫 台股多空戰三情境推演 - 經濟日報；台股10月底開戶數1482.7萬人續創高 月增6.4萬人 | 產業熱點 | 產業 - 經濟日報；11月2日盤前／台股失半年線 惟技術面進入超跌區 靜待籌碼沉澱 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [美期中選舉逼近、美股上周五重挫 台股多空戰三情境推演 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1CUVg2X0dCd0lfTXdaNmF2ampJVkJpcF9rZTh1QUM3Z18zZ3JMNmVKcHFPeXNnVUJqaFFOa2VKaEQ1SUFCYWVMeGZiX2E0elV6YkhoTUpEcW1zUdIBX0FVX3lxTFBLalc4Y1IxQ2R1aVdUOUsxLV9id29vQ0JPSGZjX2UwdVFjaUhWMW1hc1VlcGZDVkdFTVBVM0hWMFpVbWpLTmVXOWtwNkhHOVY0TnQ3UFdqdzFlOElYOW00?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 01 Nov 2026 17:21:56 GMT
- [台股10月底開戶數1482.7萬人續創高 月增6.4萬人 | 產業熱點 | 產業 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxOSzJOVWxpN0t4YnRzd1VsOFRMSmRLeS1QYW9jYl9XZkVGbDJlS3BnTWc1MzFYQl83dnJzZnlUdTF1REstZU02bVpJdF9TM29OUjYtcDV2VjJzWFFiZWh0QnM1d2VnUGhlRUw1Qm1tTl9HWFVjNFQwSFc1b2pOdGVKdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 02 Nov 2026 01:00:32 GMT
- [11月2日盤前／台股失半年線 惟技術面進入超跌區 靜待籌碼沉澱 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxNZWYwTmZEYkt4SHpWVHhmUzlVTmhSQzVmakVVYnl6QmduakxFUGpmRFg4Z25hNkRMSXhaSjVQSUtHTkdyTEZSRXpfUnFJZm42dFFNd3hrTnplcTZxeGRLRXFIeUh6b3g2NnlUZHJGcHl2X2VkMFBqd3Q1THEyQTRSctIBX0FVX3lxTFBXQlBRQktJNjJNSTNHcm45V0ZrOXZMM2ZWUWNTa1FNS3ZRWGM2Nk5Tc1ZSODV4YnVBa1NxZndQTndqWUw4Sll4YnNCOXl6azRLc0E1bmxjcFphTE1SODFR?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 02 Nov 2026 00:18:24 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：10/30上市融資增加排行前20名 - 台股 - 新聞 - MoneyDJ；法人盤勢分析內容-台股 - MoneyDJ；美股指數期貨最新報價 8:37-台股 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [10/30上市融資增加排行前20名 - 台股 - 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMimwFBVV95cUxOT1BBMWl1ZXZpSGdMSUxnelFoeWNJMkJlZFJtQ3FxNTFCWm5KaU51U1F4U1hOdU9ENGYtRjV2SUN5YmkxTmhTQmFpNThhbzdGUHhWS1lRVk9jaDVsQUlodnN2a0xkR2Q5UjZwZ1VDV3UzNjVKdXRJc083TWNLYlplZ1lvc2tkR0V1Wlg3ZklRX284TU9iQ2lJRkpnNA?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 01 Nov 2026 23:31:00 GMT
- [法人盤勢分析內容-台股 - MoneyDJ](https://news.google.com/rss/articles/CBMijgFBVV95cUxNczRzVGZXdWozWTBmdkZZc25LZXQ2OHlzR1hzSEliMm9aVElVSEI1d081SzhwWjhLd0dENV9fRjR1cUxMcmg4Qk85RHNIQWNfNTJpRmY2YXlPQkxXU3JfLXNCTG1UcndMMHNTWmlhaUxWeVRyUVNaVVZITTJhNDVra28yclNlb2tGdEsxT2Rn?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 02 Nov 2026 00:41:02 GMT
- [美股指數期貨最新報價 8:37-台股 - MoneyDJ](https://news.google.com/rss/articles/CBMiigFBVV95cUxPU3U1OUc4bXh2N2FKb2hiUlE0dU9pWU9vSVBkOUthbklGc2E2UG1hbXpVc1dmd2ZiWjd1bWRHNWFiUVRlLTBUWjZoYm1tdU1rMzZiRk9aV0NBUHp2SFFXcHloMklEOGxiQ3hTSERTVFZ0aVFZeWxzcE5SXzB5RHlBVC1KTy1uVWprMHc?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 02 Nov 2026 00:50:50 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
