# 每日股市熱門話題分析 - 2026-10-06

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **散熱與液冷供應鏈**｜正向｜熱度 3｜市場確認 88.87｜同向 2/2
2. **半導體與晶片供應鏈**｜中性｜熱度 9｜市場確認 N/A｜同向 0/0
3. **AI 伺服器與資料中心**｜中性｜熱度 10｜市場確認 N/A｜同向 0/0
4. **利率與成長股估值**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0
5. **新興題材：DraftKings**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.72（樣本 8）
- 5日相關係數：-0.75（樣本 5）
- 同向比例：3/8

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 散熱與液冷供應鏈 | 88.87 | 2/2 | 0 | +6.29% | +10.12% |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | N/A | 0/0 | 0 | N/A | N/A |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：DraftKings | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：TradingKey | 4.76 | 1/4 | 3 | -4.25% | -9.95% |
| 記憶體與 HBM 供應鏈 | 0.00 | 0/2 | 2 | -8.12% | -19.38% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-09-23 | 0.35 | 0.22 | +80.95% | 21 |
| 2026-09-24 | 0.05 | 0.42 | +90.00% | 10 |
| 2026-09-25 | -0.31 | 0.15 | +30.77% | 13 |
| 2026-09-26 | 0.22 | 0.14 | +63.64% | 11 |
| 2026-09-27 | 0.11 | -0.14 | +57.14% | 14 |
| 2026-09-28 | 0.05 | -0.53 | +63.64% | 11 |
| 2026-09-29 | 0.31 | -0.78 | +16.67% | 6 |
| 2026-09-30 | 0.05 | 0.04 | +33.33% | 18 |
| 2026-10-01 | 0.21 | -0.27 | +40.00% | 20 |
| 2026-10-02 | 0.51 | 0.37 | +72.73% | 11 |
| 2026-10-03 | -0.35 | 0.13 | +16.67% | 6 |
| 2026-10-04 | -0.12 | 0.70 | +80.00% | 20 |
| 2026-10-05 | -0.16 | 0.29 | +73.33% | 15 |
| 2026-10-06 | -0.72 | -0.75 | +37.50% | 8 |

## 歷史回測摘要

- 回測日期：2026-10-06
- 近5日 3日相關：-0.08
- 近5日 5日相關：-0.01
- 同向比例：+62.50%
- 權重狀態：未調整

- 方向準確度：+62.50%
- 信心排序準確度：-0.08
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

摘要：散熱與液冷供應鏈 相關新聞集中在：CDU認證落榜、Rubin Ultra規格傳變？法人卻反手上修這家散熱廠業績及目標價- 證券 - 工商時報；〈財經週報-台股熱點〉從AI到外太空 散熱族群題材不斷 - 自由時報；輝達、Google、AWS齊助攻！這「散熱股」水冷板訂單滿手 今年估賺逾10個股本 - FTNN

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.57 | +4.37% | +0.84% | 3,550.00 | 3,550.00 | 0.00% | 同向 | 75.13 | 47.79 | 19.48B TWD / 54.34% | 2026-09-01 |
| NVDA 輝達 | 新聞直接提及 | +0.42 | +8.21% | +19.40% | 238.90 | 238.90 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 3 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：上修。
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [CDU認證落榜、Rubin Ultra規格傳變？法人卻反手上修這家散熱廠業績及目標價- 證券 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5jQ2hwTUdkTm9wU1JrQ0RiUEhMOGVjZXlyM1RxVGVqM2pRazBhLU1CLUNiTHZZYjZNeW9takZzTFVOZ3R4TC1LTkM2M3NfSG9UUWZneHNGcUZ4R09KUkFF?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 04 Oct 2026 01:25:00 GMT
- [〈財經週報-台股熱點〉從AI到外太空 散熱族群題材不斷 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTE9rc0xOT3JaSGZPbV9uNjZUNmJLdkctMThER29ldnFaMXp1YlBQajNxaVBBcHlrVEFOOUNLZkxISUt1ZVFOMHF4WXBSd1Jtc0plYWh5bDRrdVk?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 04 Oct 2026 12:32:32 GMT
- [輝達、Google、AWS齊助攻！這「散熱股」水冷板訂單滿手 今年估賺逾10個股本 - FTNN](https://news.google.com/rss/articles/CBMiS0FVX3lxTE00UmNaTUJTZGttSkcyY0lOYTJ5TlpQT1FQMDloUXZSaHZTZXpESU1Ua0s3ckVWOHk5LWFWU2stc3dUc19WUWszYVlpZw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 04 Oct 2026 15:50:00 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Advanced Micro Devices vs. Intel: Which Semiconductor Stock Is a Better Buy in 2026? - The Motley Fool；I’m Loading Up on Taiwan Semiconductor Ahead of Oct. 15 Earnings - 24/7 Wall St.；Intel Drops as Musk Signals TSMC Could Join Terafab, a “Setback” for Its Foundry Comeback - TIKR.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | +1.32% | N/A | 116.19 | 119.33 | -2.63% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | 0.00 | +3.83% | +4.04% | 2,575.00 | 2,575.00 | 0.00% | 不適用 | 86.28 | 29.85 | 514.81B TWD / 53.32% | 2026-09-01 |
| AMD 超微 | 新聞直接提及 | 0.00 | +22.41% | N/A | 631.75 | 633.91 | -0.34% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +8.21% | +19.40% | 238.90 | 238.90 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | -1.29% | -0.97% | 148.50 | 164.50 | -9.73% | 不適用 | 6.68 | 22.93 | 25.04B TWD / 30.71% | 2026-09-01 |
| MU 美光 | 產業/供應鏈推估 | 0.00 | +9.57% | N/A | 1,063.96 | 1,074.89 | -1.02% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -2.05% | -0.51% | 1,704.16 | 2,335.00 | -27.02% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -2.11% | -4.03% | 362.51 | 446.77 | -18.86% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 3 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「Taiwan Semiconductor、TSMC」，共 3 篇新聞命中。 同時符合主題標籤：semiconductor, chip, foundry。
- AMD：新聞直接提及「Advanced Micro Devices、AMD」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Advanced Micro Devices vs. Intel: Which Semiconductor Stock Is a Better Buy in 2026? - The Motley Fool](https://news.google.com/rss/articles/CBMizwFBVV95cUxOeGQ3dUc4cEFtNVIxeDV6WVkwUG9TNlBMOGUyUjJPSmktMXdPLXlqZXVfWWNRSGRjWXVHM0hRb0ZZYzlzUXFyZmhEUEFRZ05GcjVhSnVablIxMlM5WEVkeHpWeWw1bWtmb1JtX1V2Z3RERTZKTHRCbHNOc3JvdzRWMTJTNzNGLUZwUF84ZFJwLXEzYndhR0VmN3hacnp5QUhWdmp0b0M4UjZ6N1ZLV2x2ZUxyUDdsNVR3QzdrdGhwZnZoOHNBc1h1WmR4V25CbkE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 05 Oct 2026 20:27:30 GMT
- [I’m Loading Up on Taiwan Semiconductor Ahead of Oct. 15 Earnings - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiqgFBVV95cUxPbkNEWl85eWtEb2FPMUNHTFh4aTlOMVNUMGJ5b3NzaHEyY1BHZVluVjAxQXdhdlRMdkJ6ZzRfNXNfSXhTMnZrTXJsdkl4dW5FeHBaRDhKTjd2N2M4ZndIMTJ0cVFTNlphb0c4ZEJ3NGtRbUNfMGZYWkU2c2tPZ0xaUXR1YnVlR2dxaTdULVp0X3hLU3RaV2otTHlIVGIxZlBqQTdxLW8zUlBnZw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 05 Oct 2026 11:15:00 GMT
- [Intel Drops as Musk Signals TSMC Could Join Terafab, a “Setback” for Its Foundry Comeback - TIKR.com](https://news.google.com/rss/articles/CBMisgFBVV95cUxPMl9IUnBDTnI4SzA4ZDRvcHVMY1RKT3ZRZTZHZUFWMjhWekJ4WDBCNE1Bc043UzZoZ2ZIVFV2TnV6MktmaVhHM1NzSWxzUDdTOXdRRW8zc1c0V2dqbzBNSHVxOFAySVVoeWpHaGdnLUtpLVpVLWgwX2tNcENYZDl2NTMxQUFoRTczQ1paZnAwRlFIZGlzUFQ2NU9fR1hfeDhYVFdrLUlDNlhERmJrc3JSSHh3?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 05 Oct 2026 15:52:26 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：AI 推論成本每年便宜 13 倍，大廠訂閱制將面臨考驗 - TechNews 科技新報；營收成長飆贏同業 23% 的祕密，IBM 揭露 AI 時代財務長新使命 - TechNews 科技新報；Reflection 首款開放權重模型，恐對美中 AI 對手構威脅 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | +1.32% | N/A | 116.19 | 119.33 | -2.63% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +8.21% | +19.40% | 238.90 | 238.90 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | +22.41% | N/A | 631.75 | 633.91 | -0.34% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +3.83% | +4.04% | 2,575.00 | 2,575.00 | 0.00% | 不適用 | 86.28 | 29.85 | 514.81B TWD / 53.32% | 2026-09-01 |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +16.64% | +6.74% | 525.18 | 525.18 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -2.11% | -4.03% | 362.51 | 446.77 | -18.86% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | +5.55% | +6.15% | 739.00 | 739.00 | 0.00% | 不適用 | 13.92 | 53.69 | 82.25B TWD / 45.66% | 2026-09-01 |
| 2454 聯發科 | 產業/供應鏈推估 | 0.00 | +4.98% | -2.27% | 4,950.00 | 4,950.00 | 0.00% | 不適用 | 60.69 | 85.30 | 64.18B TWD / 44.08% | 2026-09-01 |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：恐, 成長。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：恐, 成長。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：恐, 成長。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AI 推論成本每年便宜 13 倍，大廠訂閱制將面臨考驗 - TechNews 科技新報](https://news.google.com/rss/articles/CBMidEFVX3lxTFBTSDNUUTJkc2hYVFROZDlocjF1a0wzV3AtclJQaFo4Wkd3NFItb0NNQ083TjhsU0NSeUtqb0tXakNBSXI4QjNoZGNJVU8xYUFZVzZ2X0RZc01lSEJZbHJsQ2lGYUJDSE9GUElmUnl6WU9UY3E5?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 05 Oct 2026 23:26:15 GMT
- [營收成長飆贏同業 23% 的祕密，IBM 揭露 AI 時代財務長新使命 - TechNews 科技新報](https://news.google.com/rss/articles/CBMibkFVX3lxTE1YVlR1eTFPTGlyTV9lOE5kUGlFWmZldHp4ZUdkWnU2d2RidHdUek42YWs5SDdIQmhLSWxvc2s3LTdpdm9PTkZpSjhXWjRBQTVpb1FDZzMyNk9oMGtxcGdPanY1ZkpvbUtSdUxnT1V3?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 06 Oct 2026 00:14:09 GMT
- [Reflection 首款開放權重模型，恐對美中 AI 對手構威脅 - TechNews 科技新報](https://news.google.com/rss/articles/CBMirwFBVV95cUxPNFpGTkVpaVRPdXJGQXFQLXVKSk13TEIteVBXZ1FCOVAwYks0eWxpMldyYlo3SmpQRTlwTlM1Z1JwaFFzR21EeFpaRURwbkd0c2xoRXJlTFYwZEYxdUZjZjFod3d6a0FzUzllWG5HdGtqU0FXVlNDOWx1TWpteWNQLTBLZFVla0dSMVFub0VncHMyUFppR1VtQXVvdFVBcnBzall0NHlGQ1pXWnI3dG9B?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 06 Oct 2026 01:07:30 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：台股進入「不敢賣」時代追友達、群創真的更有賺頭？低本益比證券股反而更吸睛| 個人理財| 理財 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +16.64% | +6.74% | 525.18 | 525.18 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [台股進入「不敢賣」時代追友達、群創真的更有賺頭？低本益比證券股反而更吸睛| 個人理財| 理財 - 經濟日報](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5idmQxQ2RPWFpuTS02VVdLZGtUQTFiWDRic19RNWk3X0k1czllZTc3MXY0bHMwR05NTG5nY3BiVE9JQ1VCNGtoWGxpWGpMbkVLeWFzZUFTbTNuZjg?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 04 Oct 2026 09:00:00 GMT

## 新興題材：DraftKings

摘要：新興題材：DraftKings 相關新聞集中在：Stocks making the biggest moves midday: Microsoft, SpaceX, Vaxcyte, Banco Bradesco, DraftKings & more - cnbc.com；Stocks making the biggest moves premarket: DraftKings, Itau Unibanco, PTC & more - cnbc.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 新聞直接提及 | 0.00 | +16.64% | +6.74% | 525.18 | 525.18 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：新聞直接提及「Microsoft」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Stocks making the biggest moves midday: Microsoft, SpaceX, Vaxcyte, Banco Bradesco, DraftKings & more - cnbc.com](https://news.google.com/rss/articles/CBMioAFBVV95cUxObW1JQVhXOHZ4WmVqNk1JeXdLOFZJOGtjVnVfYVhSRHIxN3dORGI4WGVjTDB3VHJHbnNBcGhvYTZ3bDNDM1hGUUNUbVd4U2VhdV96eWJYVmtvbGpkRGdIUUt5ZjY5OWR1Si0zdzRDT0hXeEo0LTA5cEN0MUtacWVrMWNGMm05bzZaTHNKSFdBem9EZThYd013TUdRVzBCRnhS?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 05 Oct 2026 17:13:38 GMT
- [Stocks making the biggest moves premarket: DraftKings, Itau Unibanco, PTC & more - cnbc.com](https://news.google.com/rss/articles/CBMilwFBVV95cUxQYmNvM0pfMnR0QmFNWnBFamlwT0ZEOC1qVWVMcTNGbUJ6S2xaSXhrdlhLYTVsaUhVUHo0OWtscnVYcDl3R05OODlsdU83RldtRHhrOE84cnRTbGlFU25fTjd2RUFtWEVwR0ZpR2w0ckw4MV9wbzNMQzByZDYwZDVtT0VtVXpxNThuODVZOW1pMHJHZ1RQTEZr?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 05 Oct 2026 11:45:09 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Why Is Intel (INTC) Stock Volatile After Earnings? Revenue Beat Overshadowed by $11 Billion Loss - TradingKey；Micron vs. SanDisk: As AI Data Center Boom Continues to Heat Up, Which Memory Stock Is a Better Buy? - TradingKey；Technology Equipment Sector: Companies, Performance and Stocks - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| SNDK SanDisk | 新聞直接提及 | +0.28 | -2.05% | -0.51% | 1,704.16 | 2,335.00 | -27.02% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 新聞直接提及 | -0.24 | +9.57% | N/A | 1,063.96 | 1,074.89 | -1.02% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.42 | +1.32% | N/A | 116.19 | 119.33 | -2.63% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 新聞直接提及 | -0.21 | +6.68% | +19.38% | 332.89 | 333.69 | -0.24% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- SNDK：新聞直接提及「SanDisk、SNDK」，共 3 篇新聞命中。 方向判斷命中詞：falls, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- MU：新聞直接提及「Micron、memory」，共 2 篇新聞命中。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Why Is Intel (INTC) Stock Volatile After Earnings? Revenue Beat Overshadowed by $11 Billion Loss - TradingKey](https://news.google.com/rss/articles/CBMiyAFBVV95cUxPdGVhdUdOWHYwd0I2OHRLRjlFVE9KTkNud09aOHhCOTZGY2NDZVM4VjFnTTZKdkpKdlBORHo1OG5RWENLVFg4VUZoYVdVWVRpaWFCSWtxY2dHX280ZFFsaDlvSldKQm9NdTdWTjlueks4V3V3RUVJQ2pqYVFtNi0xVU9zY2V3MGdONjRFaHJqU1RRaVZZMm9GZndlNVRSaWpveDlMWG41WG5qUk52T0tRcGl1bklGZ2twMmQyQnJxdkM0YzU1d1J2Wg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 04 Oct 2026 20:17:53 GMT
- [Micron vs. SanDisk: As AI Data Center Boom Continues to Heat Up, Which Memory Stock Is a Better Buy? - TradingKey](https://news.google.com/rss/articles/CBMiwgFBVV95cUxNb2l6VlJubm1teWI3RlFGWm9fZ0g0dDJFVWhtMUJaaHkySzF4NnQxMW5ScllzSGNlMFR2dUZPYUhFeUNVVndpNU82c2dRVTB2S1BoRTVwV1pIekRJWENUNFBYbDVQVjV5Yk9GYUhxdTNuVkNUVXNtREZ4ck5mN0laTlBUbDlUQkxhSjhNMTFNcE5TWjdVWkIwekZKTXI2d3ExUU1XZnFraF9ncWlnQnJfeDJxZzJnRGhUQXhrVFJzdzUwdw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 05 Oct 2026 00:05:52 GMT
- [Technology Equipment Sector: Companies, Performance and Stocks - TradingKey](https://news.google.com/rss/articles/CBMifEFVX3lxTE1rM1RZanBYR0E2ZzJJN1djdk05YjVMWGNjeEhWdHdEUklEMmRJaTI3UEg0ZGtsTUx5Rmtramx3R2dmRUs4UGx4UG9CRlZJMnNfZGFoSTAydk9DaGhERTAzR0pXUExacTNOZ1FoVTVsMjFpeGozMlJHMVlJU2c?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 05 Oct 2026 17:04:12 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Meet the Low-Cost Vanguard ETF With 32.4% Invested in Nvidia, Broadcom, Micron, AMD, Intel, and Lam Research, While VOO Has Just 14.8%. - The Globe and Mail；Micron or Sandisk: If I Could Only Own One for the Next 5 Years, It Would Be This One - The Motley Fool；Micron vs. SanDisk: As AI Data Center Boom Continues to Heat Up, Which Memory Stock Is a Better Buy? - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| SNDK SanDisk | 新聞直接提及 | 0.00 | -2.05% | -0.51% | 1,704.16 | 2,335.00 | -27.02% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 新聞直接提及 | -0.28 | +9.57% | N/A | 1,063.96 | 1,074.89 | -1.02% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +8.21% | +19.40% | 238.90 | 238.90 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | +22.41% | N/A | 631.75 | 633.91 | -0.34% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | 0.00 | +1.32% | N/A | 116.19 | 119.33 | -2.63% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 新聞直接提及 | -0.21 | +6.68% | +19.38% | 332.89 | 333.69 | -0.24% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | 0.00 | -2.11% | -4.03% | 362.51 | 446.77 | -18.86% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- SNDK：新聞直接提及「SanDisk、SNDK」，共 5 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：falls, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- MU：新聞直接提及「Micron、memory」，共 4 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：falls。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Meet the Low-Cost Vanguard ETF With 32.4% Invested in Nvidia, Broadcom, Micron, AMD, Intel, and Lam Research, While VOO Has Just 14.8%. - The Globe and Mail](https://news.google.com/rss/articles/CBMiuAJBVV95cUxOVDM2aW5CS0ZFajlmT19lRVQxbXNQbGx3NGdzWTdfdDZjR0swX00xWE9LSURpZHI4YTh5NVRESm14SllWUTVWX2RjY3lrWE1reUZoVFBNWWgwUDU2NzJtR2V3clNaZm9Na1NuMi1sNTIzNUh5Tm1wQmViQ21LdnhJeUhmQldfWTNGVVEtN2JqZVJZdkcyNDgwQXZ6SzZDUGx6SUxBd1V4UW04bDIyUmh0MFN5U04wc25hV3BId3FYU0cxTGFLNFhVWGh0UmoxQU1FTlREN3JIRV9yLXRmR1o3b2RORGRlSExEanNlUlRLWnlGVGc2UHBUdGhiajVJVkxKa0RKWTlVSWN1V3NUOUJJRnp6VGtrZWliNVV5S1Nud2E1Mm1zWnVzR1pmVkZ6ZHU2VFJKdE9OLUM?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 05 Oct 2026 10:54:55 GMT
- [Micron or Sandisk: If I Could Only Own One for the Next 5 Years, It Would Be This One - The Motley Fool](https://news.google.com/rss/articles/CBMilwFBVV95cUxPbmgzT0VqTE9aa1plT0RnRXpyclJjSEFCNGptcFlrcU41VTNadVp0SVlUeGZLSUVrZGozWEhxd2Q1bHZoN29IcE9sV25kd19MZTlUVEo1bHFfakpURmdmaG9KeXhKRXJVSDVYams0alpsdlJpMS13c3ItZ3NFUUkwQ3FFOEMwM2V3N1RSTFlrOEdFYmVDM0pF?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Sun, 04 Oct 2026 13:56:00 GMT
- [Micron vs. SanDisk: As AI Data Center Boom Continues to Heat Up, Which Memory Stock Is a Better Buy? - TradingKey](https://news.google.com/rss/articles/CBMiwgFBVV95cUxNb2l6VlJubm1teWI3RlFGWm9fZ0g0dDJFVWhtMUJaaHkySzF4NnQxMW5ScllzSGNlMFR2dUZPYUhFeUNVVndpNU82c2dRVTB2S1BoRTVwV1pIekRJWENUNFBYbDVQVjV5Yk9GYUhxdTNuVkNUVXNtREZ4ck5mN0laTlBUbDlUQkxhSjhNMTFNcE5TWjdVWkIwekZKTXI2d3ExUU1XZnFraF9ncWlnQnJfeDJxZzJnRGhUQXhrVFJzdzUwdw?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 05 Oct 2026 00:05:52 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：產業評析-第4季標的股 集團作帳+選舉行情 - MoneyDJ理財網；光模組轉單利多發酵、台股戰新高！投信重壓AI 缺貨鏈力抗空軍- 新聞 - MoneyDJ理財網；台股衝破四萬九 台幣早盤帶量升值5分 - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [產業評析-第4季標的股 集團作帳+選舉行情 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMijgFBVV95cUxNX2cta2pteWhvRTlfZDZqZEFwN0t3WXZpYjd1U1RQY3JDY005ejI4Ul83VEJnVERqcmNvb08tZExzVWdZbXJDc25TX2xaZm5jVHBJMTBka3lTZUVod0liV2R5cFpmRWpNOTVEb2JDUFRneGMxWUFXaF82TmVsQlZzMXRzb1VZa09lZ2xSNlR3?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 05 Oct 2026 22:18:45 GMT
- [光模組轉單利多發酵、台股戰新高！投信重壓AI 缺貨鏈力抗空軍- 新聞 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikgFBVV95cUxPOTRCcVE5RzFtN25TdklyckJCSkR1Q2tEU2V0dmswMGlsSHd0dld3eTU1c1pLQUl3d29mekJCT21GMG1XV2pwYmRXRnEwQXBkaDQwOEJKZlVRT09oTXFjQWFBeXBOSEJIMDlvYkZyQ3BjdGc1eUZ2V1p4enNDYVp6U29SNFZVWS1IQzdBakx3aURiZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 05 Oct 2026 04:11:00 GMT
- [台股衝破四萬九 台幣早盤帶量升值5分 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMioAFBVV95cUxONXgzQWhtMXNIcmp0NTZ2aGdyUHB0T29iY2Y2MGJpVEhKYnpMQk9pMVlOaHdwZ0o4X21PMDY0dURfR2RiLTJxdDhkMFh1c1d5UUExTVIzbEZrbWd4OUtrZEZxb0ZMUVlteHJhd3JlbVBvbzQ2WjBhSjNfZ3lRWVRPbzNqdHNpQkRIU2hOUW5qZ0ktMHRXUkQwRFBTaTlzay1w?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 05 Oct 2026 04:52:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
