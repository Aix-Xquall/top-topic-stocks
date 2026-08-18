# 每日股市熱門話題分析 - 2026-08-19

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **利率與成長股估值**｜正向｜熱度 3｜市場確認 99.46｜同向 1/1
2. **半導體與晶片供應鏈**｜中性｜熱度 12｜市場確認 N/A｜同向 0/0
3. **關稅與供應鏈轉移**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
4. **AI 伺服器與資料中心**｜中性｜熱度 12｜市場確認 32.55｜同向 2/6
5. **記憶體與 HBM 供應鏈**｜負向｜熱度 10｜市場確認 0.00｜同向 0/2

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.23（樣本 10）
- 5日相關係數：-0.33（樣本 10）
- 同向比例：3/10

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 利率與成長股估值 | 99.46 | 1/1 | 0 | +9.82% | +10.11% |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 關稅與供應鏈轉移 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 32.55 | 2/6 | 3 | +3.07% | -2.10% |
| 記憶體與 HBM 供應鏈 | 0.00 | 0/2 | 2 | -8.11% | -19.01% |
| 散熱與液冷供應鏈 | 0.00 | 0/1 | 1 | -5.16% | +9.96% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價呈負相關；應檢查正負向詞庫，並降低新聞直接提及但股價背離的權重。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-08-06 | 0.07 | 0.33 | +50.00% | 12 |
| 2026-08-07 | -0.22 | -0.17 | +50.00% | 8 |
| 2026-08-08 | 0.72 | 0.45 | +62.50% | 16 |
| 2026-08-09 | -0.39 | 0.46 | +71.43% | 7 |
| 2026-08-10 | -0.09 | 0.74 | +71.43% | 7 |
| 2026-08-11 | 0.57 | -0.18 | +54.55% | 11 |
| 2026-08-12 | 0.52 | -0.47 | +87.50% | 8 |
| 2026-08-13 | 0.72 | 0.24 | +100.00% | 7 |
| 2026-08-14 | 0.34 | 0.57 | +92.86% | 14 |
| 2026-08-15 | 0.24 | 0.30 | +68.75% | 16 |
| 2026-08-16 | 0.37 | 0.51 | +70.00% | 10 |
| 2026-08-17 | 0.49 | 0.60 | +66.67% | 12 |
| 2026-08-18 | 0.29 | 0.36 | +80.00% | 10 |
| 2026-08-19 | -0.23 | -0.33 | +30.00% | 10 |

## 歷史回測摘要

- 回測日期：2026-08-19
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

摘要：利率與成長股估值 相關新聞集中在：Intel Stock Rockets Overnight On Blowout Q1: Analyst Says ‘We’re Overthinking’ As Valuation Gap With NVDA, AMD Widens - Stocktwits；AI chip startup Etched doubles valuation to $21 billion in under a month - reuters.com；Global bond markets put governments on notice over fiscal, inflation risks - reuters.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.42 | +9.82% | +10.11% | 219.74 | 225.16 | -2.41% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.42 | N/A | N/A | 484.39 | 516.10 | -6.14% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.42 | N/A | N/A | 96.68 | 114.68 | -15.69% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +22.63% | -4.95% | 481.63 | 506.69 | -4.95% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVDA」，共 1 篇新聞命中。 方向判斷命中詞：rockets。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 方向判斷命中詞：rockets。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 方向判斷命中詞：rockets。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Stock Rockets Overnight On Blowout Q1: Analyst Says ‘We’re Overthinking’ As Valuation Gap With NVDA, AMD Widens - Stocktwits](https://news.google.com/rss/articles/CBMiiAJBVV95cUxOeXkzdzdWTjJEdE9PWlRvTGdqTnA2MklEYk5ZcE5ZYWVvT29nRVk2Z1p5czRsZGJzY0U3ZWNhTjFmbTdWaXpDa0R2OTh6RzNxZUxUWk9xOS1GbmNuRVdrdmpQdHBjUzFEejVOcFU2di16ak10T1FFVnFNNnZpVnVwU3RkejRveng1ZVF5T1pYdWkxdlB0VkZsQ21pZEJiZU9fVFM5SndpdUpnZVQ1UV9CUnV0RUlwcU9MNGtkbVR6Tng2OVlpY01HU0hXc2lEbzBxZFRER25yajZQcHhrVmdWRmNYUWxEVWVRUDFjcHZhZzVqbm9MVmZGX0ducGZzTmt0SjltejVNSlc?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 18 Aug 2026 00:50:40 GMT
- [AI chip startup Etched doubles valuation to $21 billion in under a month - reuters.com](https://news.google.com/rss/articles/CBMirAFBVV95cUxPZ3NNZlBGNU1FVmtQWnVzMlc1SjFEVmtwYWJLNVJTYUpJS0NEb29iT0NhR1R5bUdKMlhqUWsyMjRJekVtcWFWb3dCX1lHMWlFNHJVLTZCeEoycW1ZdE03VThfZDEzellONHd4ZnJ3RlNEYlA4cGJReEFvaG13bTR0MHItbHlWN3pMWDNMN3JMVkJQNFo2aHFTQUw1QTlrWUt0V0FKamtGSm5rWUVT?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 18 Aug 2026 18:41:39 GMT
- [Global bond markets put governments on notice over fiscal, inflation risks - reuters.com](https://news.google.com/rss/articles/CBMiugFBVV95cUxQeWxrV2hFeTRkQjZmS2pjcmpEM1VJd2tTc2lkT1NxVjJ3c0Jpa2ZNQzJ3eFlSa1BoV3pQN3VLNzZEUHM0SHZHMURHLUthd21TV0R6TkY5N0lfR1pKRnRGZGpFc1FzamJfT1l2Q1pYQXloZ25LYWdxOHhQcndkZ21xU1lXZFJwc0ZOcnVqWUkyejNUdVcyWWlORW9rdzZORlJCZjZHMWZNX0tKYU44bDJReUpMcVNlOFBNd0E?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 18 Aug 2026 19:01:49 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Applied Materials Rockets 98% in 2026: How Does AMAT Compare to Lam Research and KLA as AI Capex Powers Chip Gear Stocks? - 24/7 Wall St.；Intel and AMD Fall 4% as 13F Filings Reveal Concentrated Chip Bets - 24/7 Wall St.；Best Semiconductor Stocks for 2026 and How to Invest - The Motley Fool

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 96.68 | 114.68 | -15.69% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | N/A | N/A | 484.39 | 516.10 | -6.14% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -2.26% | -0.63% | 2,380.00 | 2,425.00 | -1.86% | 不適用 | 86.28 | 27.59 | 467.58B TWD / 44.69% | 2026-08-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | -4.42% | -3.25% | 119.00 | 164.50 | -27.66% | 不適用 | 6.68 | 17.89 | 23.84B TWD / 18.98% | 2026-08-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +9.82% | +10.11% | 219.74 | 225.16 | -2.41% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 940.76 | 971.66 | -3.18% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | +6.39% | +27.91% | 1,625.78 | 2,335.00 | -30.37% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | +0.60% | -8.97% | 380.00 | 446.77 | -14.95% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：fall, rockets。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：fall, rockets。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 3 篇新聞出現相關標籤。 方向判斷命中詞：fall, rockets。

### 主要來源

- [Applied Materials Rockets 98% in 2026: How Does AMAT Compare to Lam Research and KLA as AI Capex Powers Chip Gear Stocks? - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi9AFBVV95cUxNSnNrcVN4SmZkNS00cmlLeUlwOXIzb18tLWpkWE04d0FMbTNCUjZfOGU3ZFRpQkhoZXRnb1ZWMHJ1Q2dQSTZMUVlTdmJwaGpZbEZUVmowczNQbHlTZFJUQldTVkZaa0NhdXRyY3ZXS1c4VUhYVDhkOFJsbUdJODhBWEdBdC1tSlZkWXFZR3BYS2w5eGtYM0FZZkNGMVBnLWdpdk9YQmUyOHk5NmVOSVdNdklCVTNrODR0cHl1d0M0OXVVNlNRdE5LS082RGdRUUFpZHZBS0NLX2Z6Nm1qdHhXU2RrQ01RbnhpQm5MaENTal9GTjk1?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 18 Aug 2026 19:22:38 GMT
- [Intel and AMD Fall 4% as 13F Filings Reveal Concentrated Chip Bets - 24/7 Wall St.](https://news.google.com/rss/articles/CBMirgFBVV95cUxQRWF0ODlabmdJbGY4b2RxRF9ScEh3bWhGZ3dWMFM0N0FTNGd5alVoWEx0czl0VEE5ZU9DM1B1dXVKTEZyS0dMM09yZmJFWlQtYzFXX3N4ZTBGVXkwY2ZFYWkySDZLS2xtSUJUbFFOTVF1eUlXSVIxMWtNR1hxSFZrYlNHM0pvQ2FOWEVYOXJHX0FyOUdkZDh2dFNobC0zcV9ncUI2X0ZHaDFaRGh6TEE?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 18 Aug 2026 13:34:44 GMT
- [Best Semiconductor Stocks for 2026 and How to Invest - The Motley Fool](https://news.google.com/rss/articles/CBMipgFBVV95cUxOT1dYNXFONXk3TGdVWUstTHRMeGNyX1RDMmVLWUNsOFBvSGplTndkeHA1YU54QXhKOHV2RXFmOS1kY2lmMjNJVFBodDQ0ajVCZm8zMUlqM0NBV1R5MzEwTk9TUUZuWUFTQ1BpV1otQW9DTnhiMGJLRS1sd0x1VUR6U1dQU2pWM3kwWmx2UHhtRDZxZmJIT1dPa2NtYVZQd3FEU1hld2xn?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 17 Aug 2026 05:04:00 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：液冷成高階 AI 機架基礎設施標配，台灣散熱供應鏈一次看 - 鏈新聞 ABMedia；揚發實業迎戰半導體供應鏈減碳浪潮- 日報 - 工商時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | -5.16% | +9.96% | 3,035.00 | 3,235.00 | -6.18% | 不適用 | 75.13 | 40.46 | 18.59B TWD / 57.39% | 2026-08-01 |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +17.36% | +33.55% | 310.03 | 312.06 | -0.65% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | -4.96% | -5.32% | 249.00 | 289.00 | -13.84% | 不適用 | 15.21 | 16.41 | 946.51B TWD / 54.19% | 2026-08-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 1 篇新聞命中。
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [液冷成高階 AI 機架基礎設施標配，台灣散熱供應鏈一次看 - 鏈新聞 ABMedia](https://news.google.com/rss/articles/CBMiiAFBVV95cUxQMWVZczl6cUxBLUhVcUxsTi1FXzN0SHZ2bzUzUWZLSV9yYUlnM19JUk5SeHRVam5IdHVJcERRNjYyT1kxZ3YwVnFpRW1VRldVekh0YU1fZF83WVZuMVBEaVRLelNtM04zbXJjRGhlUEFicER5VnFoOEY3dFJTaUI3OWRvQURWLXpI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 18 Aug 2026 08:41:13 GMT
- [揚發實業迎戰半導體供應鏈減碳浪潮- 日報 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9LZzFNbG1mMFljV2ljOVBQM1FPWXRiUjQybnJJMjhmZmhWYzhUR1VYWXNzSzJOaFExSm5Sd05ObjhIa1UwYjEyaERkdGQ5MnVWSjl5VXdoSjRQZi1vSHl3?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 18 Aug 2026 19:00:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel (INTC) Pushes Deeper Into AI Data Centers With Co Packaged Optics - simplywall.st；Applied Materials Rockets 98% in 2026: How Does AMAT Compare to Lam Research and KLA as AI Capex Powers Chip Gear Stocks? - 24/7 Wall St.；當 AI 取代初階人力，未來青年進入科技業的門檻為何？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.54 | N/A | N/A | 96.68 | 114.68 | -15.69% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.06 | +9.82% | +10.11% | 219.74 | 225.16 | -2.41% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.06 | N/A | N/A | 484.39 | 516.10 | -6.14% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.03 | -2.26% | -0.63% | 2,380.00 | 2,425.00 | -1.86% | 背離 | 86.28 | 27.59 | 467.58B TWD / 44.69% | 2026-08-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | +22.63% | -4.95% | 481.63 | 506.69 | -4.95% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.03 | +0.60% | -8.97% | 380.00 | 446.77 | -14.95% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.02 | -4.31% | -4.77% | 599.00 | 680.00 | -11.91% | 背離 | 13.92 | 43.34 | 73.78B TWD / 43.15% | 2026-08-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.02 | -8.05% | -3.36% | 3,885.00 | 4,310.00 | -9.86% | 背離 | 60.69 | 64.16 | 48.47B TWD / 12.16% | 2026-08-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：rockets。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：rockets。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, GPU, datacenter, AI server；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：rockets。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel (INTC) Pushes Deeper Into AI Data Centers With Co Packaged Optics - simplywall.st](https://news.google.com/rss/articles/CBMiygFBVV95cUxPOENIaEZQcjJmWnBrU2tZenlJQ0FmeU1ralIyNkhHb2l2VUdiU3k3U2R2RWxJdFhGWXpxSTB6eFkxaXZpaklEU2NWWkpITDBKdWZlMnNhWG5IRWtNdWtmQUJGbGxqODNvY0I1ellNOXVqU05ldFROVFh0UFBzTXl4Q0RBclhIaFFsOTlCN20yRW9DajZVZzNoaS00ZXR5Y251RHlKVkN6QnlsN09KZTRhUW1RZGNjRmh4NURRamJQSkVQSGRWSWFpNjVn0gHPAUFVX3lxTE0tZkpBcEJUUFIxeXlfRGpZdF9EUm8yR0hvTEppclhMV3R6LW15eG0yYTRSeUkwYkpmU2RJdXhhc3RFS1l3TkpjUHRsclJreVJRbXc5UTYwM012ZFVPbWV6LXRLV2JPT0pNbm9maXZJSUNTNGlEVWlhVm9yaGc2a2h6SS1GcUVkQ2RCb1hTVzNneGpxM1pzaVlyMm9WNDdTWkZVU2p5TzdnM3Q5VVRtU25MQTFUaUhSOG1YSklDcDRRV0hIZGs2c3hLV0NUVVNoUQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 18 Aug 2026 07:39:44 GMT
- [Applied Materials Rockets 98% in 2026: How Does AMAT Compare to Lam Research and KLA as AI Capex Powers Chip Gear Stocks? - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi9AFBVV95cUxNSnNrcVN4SmZkNS00cmlLeUlwOXIzb18tLWpkWE04d0FMbTNCUjZfOGU3ZFRpQkhoZXRnb1ZWMHJ1Q2dQSTZMUVlTdmJwaGpZbEZUVmowczNQbHlTZFJUQldTVkZaa0NhdXRyY3ZXS1c4VUhYVDhkOFJsbUdJODhBWEdBdC1tSlZkWXFZR3BYS2w5eGtYM0FZZkNGMVBnLWdpdk9YQmUyOHk5NmVOSVdNdklCVTNrODR0cHl1d0M0OXVVNlNRdE5LS082RGdRUUFpZHZBS0NLX2Z6Nm1qdHhXU2RrQ01RbnhpQm5MaENTal9GTjk1?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 18 Aug 2026 19:22:38 GMT
- [當 AI 取代初階人力，未來青年進入科技業的門檻為何？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMitAFBVV95cUxPZXVWQ2tWRm9fQnZuNUIzcWQ4eldIaXg2eXFyVFhpM2lKM2djbkg2VW9QeWZtYnpWTEVyejZIc2l1NUVTQ1B4OExqZzlHTnlZQ0dzcmNzZkFNeU1MdkVoUEpaLUVJbWltVTJIT1hBZVBjX2JVN2NqZVVoR0VPNkNhdkswYkpJcXFfbm1OTlVTcmowN1pVUmFVNnZmbFk0NDlxSlc1NmdseG1xRWxVblZkSkViRWU?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 18 Aug 2026 20:06:42 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：AI Money Moves Put These Five Stocks In Spotlight Last Week: NVDA, INTC, ORCL, AMD, SNDK - tradingview.com；Micron down 6%, SK Hynix and SanDisk 5%: why is memory trade crashing? - tradingview.com；Is Micron or Sandisk Better Poised For Upside Through The End of September? - AOL.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | -0.48 | N/A | N/A | 940.76 | 971.66 | -3.18% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.24 | +6.39% | +27.91% | 1,625.78 | 2,335.00 | -30.37% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | -0.18 | +9.82% | +10.11% | 219.74 | 225.16 | -2.41% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.36 | N/A | N/A | 484.39 | 516.10 | -6.14% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | -0.36 | N/A | N/A | 96.68 | 114.68 | -15.69% | N/A | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、memory」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK、SanDisk」，共 5 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVDA」，共 1 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AI Money Moves Put These Five Stocks In Spotlight Last Week: NVDA, INTC, ORCL, AMD, SNDK - tradingview.com](https://news.google.com/rss/articles/CBMi3AFBVV95cUxPTVVVMU5ZcWxVWk1HRnNleEcxQ2pxZ3hXanVDQXQ2MENTR0k5dlVyWDA2OEZaaG13R2MxUm5SY182MXdWR3ZaYXZQbzVvUGlFdE1yRVhzTjhLNzQ5RkZDSkZ1aG1sQ2Q1M0RrRk00cnI3RlBCejZDMmhVTXFHTnpkdjBaU3pTM0pfU0NDejhjNld2SHh4V1A0NE1DUnVKT3hybzVyalVqbjJEZ3N6ZF9HQmY3SHV5anRsalpkV0o5TVF5NU1KQ2JnaXhlMkxfNW4wSVk4RElxT1BWZXBL?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 17 Aug 2026 01:48:00 GMT
- [Micron down 6%, SK Hynix and SanDisk 5%: why is memory trade crashing? - tradingview.com](https://news.google.com/rss/articles/CBMivwFBVV95cUxPYTEyVm5odUtKcllPM1BxWWNwZHdQMlNEOFM4YnJ0Y29iNDdCWUh5b1gxTmo5QWttb19sSm9ISWFtOTU1NlJCaXBMX1VOWG0zM0JtWjlabEtsNlRTc20tZUlLaGVzNzZOTHBNU3RXcGt0eTQ2eUM0MzBqRV9jLVY5R2RYR3FDRzFrN2xwbkVvcXBCWHhRN1BNRzE5WVJIbDdGdWNmTHFOUkZDN1lMTUc0WDBmUUEtRHp3U05vUGRLVQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 18 Aug 2026 09:59:22 GMT
- [Is Micron or Sandisk Better Poised For Upside Through The End of September? - AOL.com](https://news.google.com/rss/articles/CBMihgFBVV95cUxOdS1KR0lnaGRRYnU3dFRPMXk3dlEzeHFWMjVKbzlkQUs1V3AyQUFNUHdyQ2FTM3d4N2k4RVNwRnpFeGFhU002SC1BYzgyZ1k1Njl4SDQ0UEViZmJFMzd0ZElCZXNnbmkySTZuMmtFemtVeng0YmMzS2FQQ1RBa2ZiNHFoOUhyUQ?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Mon, 17 Aug 2026 23:42:15 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：液冷散熱 2026 滲透率飆破五成！台廠受惠 奇鋐、雙鴻、健策卡位 - 緯來新聞網；液冷成高階 AI 機架基礎設施標配，台灣散熱供應鏈一次看 - 鏈新聞 ABMedia

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.26 | -5.16% | +9.96% | 3,035.00 | 3,235.00 | -6.18% | 背離 | 75.13 | 40.46 | 18.59B TWD / 57.39% | 2026-08-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐、散熱」，共 2 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：受惠。

### 主要來源

- [液冷散熱 2026 滲透率飆破五成！台廠受惠 奇鋐、雙鴻、健策卡位 - 緯來新聞網](https://news.google.com/rss/articles/CBMihgFBVV95cUxOOWNBNzFxYnhMSllXRUQxWFNJMEF4SUQxWHU2czBxcTNWQ1VoSUpFcXhQejdNd1FhOHBHd3FhOG5WM1V3NDluT2lpTVJXLUhabXFpczdRbWlDRnFMUDIzeHR0VGpQX0JIemxRQVgzZFE4ZlJTV3duX1ZoNVpvcnktMVBjV0lCQQ?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 17 Aug 2026 10:55:00 GMT
- [液冷成高階 AI 機架基礎設施標配，台灣散熱供應鏈一次看 - 鏈新聞 ABMedia](https://news.google.com/rss/articles/CBMiiAFBVV95cUxQMWVZczl6cUxBLUhVcUxsTi1FXzN0SHZ2bzUzUWZLSV9yYUlnM19JUk5SeHRVam5IdHVJcERRNjYyT1kxZ3YwVnFpRW1VRldVekh0YU1fZF83WVZuMVBEaVRLelNtM04zbXJjRGhlUEFicER5VnFoOEY3dFJTaUI3OWRvQURWLXpI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 18 Aug 2026 08:41:13 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股拚止跌要看三指標 法人：不再惡化多頭仍有反攻的機會 | 市場焦點 | 證券 - 經濟日報；台股平衡型 完勝大盤 - 經濟日報；台股平衡型 完勝大盤 | 基金天地 | 理財 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股拚止跌要看三指標 法人：不再惡化多頭仍有反攻的機會 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5RamhvdE1LZDBhSXdIWjJLcXJCLW5RY1M3U0tzT2dIQVhkOGpIWXk5MVptb3o1bUpKWDh2aGVKU3F2eU1OY0xwMEozSzZzU1NoelB5b3I5RERDUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 18 Aug 2026 18:16:59 GMT
- [台股平衡型 完勝大盤 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9wcGRjaGJBeUdNTERJLTNEdjhVRzk1dDlHeUY4b2tlcUNyaEYyM2ttSlVET1hQbXdlMnVIdHNNT2xrYUtSVUI0TTlMWWt3ZVhlUGxwYTc2LXhfZ9IBX0FVX3lxTE9sT2syQ0lqTlR2YzhWYUlLZ1FNYlFLejlPOUt5dExnblhVU29DVFhxeGxfdWVkTkJDdk83MjZPRFJxYXQ5V2djbFd6bmduYkE3LWZjNUI2VmVteG01d1BR?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 18 Aug 2026 15:33:27 GMT
- [台股平衡型 完勝大盤 | 基金天地 | 理財 - 經濟日報](https://news.google.com/rss/articles/CBMid0FVX3lxTE9wZ09odlJjUGx2U1N0YTB0X0x1d0F0T3d2eUFRS3lvNzZqSDZuel8zRHNFYndjS0lNbmdDdks4SF93OEt0MG1DaDBTR3dZRDVBQ25Objg0NUpMYVdTamVsdzdEMzhYTElRQmpTR1JkX2phTm1kWHdn?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 18 Aug 2026 15:33:27 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》電子股熄火 指數翻黑收跌548點 - MoneyDJ；《台股盤後》電子股熄火 指數翻黑收跌548點-新聞內容-基金 - MoneyDJ；統一證券：台股有待補量上漲，化解上方賣壓- 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》電子股熄火 指數翻黑收跌548點 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQbjl4ZjFfUklJeXFuRDNrQTF3WXZkcERsOHFBbkRBLVdVUjZ1MEx4eG05LWttQ3JyazNNcy1KbjY2aVNUV0ZhM0xTcDRZM3phNzRZMzBnX1NwbXh6ZXliZnd2bVhZZnYtdmd4aHFkdi00UjdRVFNLWHdFMHQ0VU1vdTdPT3JRa2RLcjd5LXJBQnR5UQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 18 Aug 2026 07:14:00 GMT
- [《台股盤後》電子股熄火 指數翻黑收跌548點-新聞內容-基金 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxQZ3UxQzNlejlPekZpOGtteGhMSlJUUXo5N2FGX1UwVHNBdFF2SzVTQmhMOG03d3NIVG1YdjdPM0V4dy1zaC1zR21mWmtoWEFtUVdpWklCNkNVRVpQb0x1bVVZWG02NUpSR3FTWEUzMlpkMmFwRUZBZXRQSU5wYW44MDJZNTc0eGRXcEtVTzNFd2s?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 18 Aug 2026 07:16:00 GMT
- [統一證券：台股有待補量上漲，化解上方賣壓- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxOd1lySzBBVWhlR2tWa2c1Z091VlNEYjJDOWZYR2pnU3hsZmwzcjh6X3djMkhpVnU2RGpMTkNuSld3ZWREZHYtamxxTnB1X0plWGRYMlUyYWNtbE03MmFBVzZQcmo4NXFUUDloMlFrMHdhcE8wSF9Oaml1Wk9tcm9tRkFFRTJSZTgweXphUXR2MjY0UQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 18 Aug 2026 00:43:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
