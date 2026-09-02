# 每日股市熱門話題分析 - 2026-09-03

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **AI 伺服器與資料中心**｜正向｜熱度 14｜市場確認 49.66｜同向 5/8
2. **半導體與晶片供應鏈**｜中性｜熱度 12｜市場確認 N/A｜同向 0/0
3. **關稅與供應鏈轉移**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0
4. **綜合市場情緒**｜正向｜熱度 34｜市場確認 0.00｜同向 0/1
5. **記憶體與 HBM 供應鏈**｜負向｜熱度 3｜市場確認 30.39｜同向 1/2

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.10（樣本 11）
- 5日相關係數：-0.10（樣本 8）
- 同向比例：6/11

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| AI 伺服器與資料中心 | 49.66 | 5/8 | 3 | +1.97% | +0.65% |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 關稅與供應鏈轉移 | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | 0.00 | 0/1 | 1 | -12.34% | -16.12% |
| 記憶體與 HBM 供應鏈 | 30.39 | 1/2 | 1 | -1.53% | -3.60% |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：2030半導體營收 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：擬加徵半導體關稅 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
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
| 2026-09-01 | N/A | N/A | +50.00% | 2 |
| 2026-09-02 | -0.29 | 0.24 | +75.00% | 12 |
| 2026-09-03 | 0.10 | -0.10 | +54.55% | 11 |

## 歷史回測摘要

- 回測日期：2026-09-03
- 近5日 3日相關：0.10
- 近5日 5日相關：-0.34
- 同向比例：+56.25%
- 權重狀態：已調整

- 方向準確度：+56.25%
- 信心排序準確度：0.10
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

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel (INTC) Stock May Be 5% Overvalued As New AI Chips Debut - simplywall.st；AI 同時衝擊人類四大驅動力，專家：轉型成敗關鍵還是「人」 - TechNews 科技新報；蔡力行談台灣 AI 時代獨特價值，彈性、速度、規模並攜手夥伴共創多贏 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | -0.54 | -21.48% | N/A | 90.05 | 114.68 | -21.48% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | -0.50 | -5.66% | -17.80% | 367.24 | 446.77 | -17.80% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | -0.03 | +11.79% | +6.28% | 224.41 | 224.41 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | -0.06 | -11.44% | N/A | 457.06 | 516.10 | -11.44% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.06 | -1.45% | -1.24% | 2,385.00 | 2,440.00 | -2.25% | 同向 | 86.28 | 27.65 | 467.58B TWD / 44.69% | 2026-08-01 |
| MSFT 微軟 | 產業/供應鏈推估 | -0.02 | +10.35% | +0.98% | 496.82 | 507.29 | -2.06% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.04 | -5.15% | -0.51% | 589.00 | 680.00 | -13.38% | 同向 | 13.92 | 42.62 | 73.78B TWD / 43.15% | 2026-08-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.02 | +7.28% | +8.37% | 4,275.00 | 4,315.00 | -0.93% | 背離 | 60.69 | 70.60 | 48.47B TWD / 12.16% | 2026-08-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：衝擊。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AVGO：新聞直接提及「Broadcom」，共 1 篇新聞命中。 同時符合主題標籤：AI, datacenter。 方向判斷命中詞：衝擊。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。 方向判斷命中詞：衝擊。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel (INTC) Stock May Be 5% Overvalued As New AI Chips Debut - simplywall.st](https://news.google.com/rss/articles/CBMizAFBVV95cUxOeUh1Vm1SazNjMzZVc2xCN3ZyS2lLNFREbXRlOGRHNTZGTGdQOTlOSDdjLVZrbzJYdmk4QnBlX0x5aVM5RlZCMU9jRExwc1lsbThmeHVPTmJZUXdNazQxTmdGdjRiMmhGMDYwQ01TWlZGbHkwQUNPM3RHZ1A2YkxNbkpQQzUxNi16RmI2SHdGaW15TkRHN2xUYUdkM3k0U3l0M2thZXZBa3Z2RjBoRTFJWTNVQVJEWGhpaFZfa0JVNEp5d01yV3VfV01WOG7SAcwBQVVfeXFMTnlIdVZtUmszYzM2VXNsQjd2cktpSzRURG10ZThkRzU2RkxnUDk5Tkg3Yy1Wa28yWHZpOEJwZV9MeWlTOUZWQjFPY0RMcHNZbG04Znh1T05iWVF3TWs0MU5nRnY0YjJoRjA2MENNU1pWRmx5MEFDTzN0R2dQNmJMTW5KUEM1MTYtekZiNkh3RmlteU5ERzdsVGFHZDN5NFN5dDNrYWV2QWt2dkYwaEUxSVkzVUFSRFhoaWhWX2tCVTRKeXdNcld1X1dNVjhu?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 01 Sep 2026 15:51:20 GMT
- [AI 同時衝擊人類四大驅動力，專家：轉型成敗關鍵還是「人」 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiyAFBVV95cUxNb1RlVS1KMkxndTVra09lMVdTWng1VE1mYkowLW1JTEw1Z3VzUUZ4QnBHYWs5ZU5kSEtGdmk4MU5HQk8yTHRxZHJvTVdLZ3MzZXBMcjI5ZVZrRnh3UVduV3Z4bEM0dXVlazhWLWZUSTRmeTM3OEZaNDJXRXl2WkhZNXNhWjlCbktiV3Fsak9JRE80RzE3aE1CaDZvbFhBTkNDOTFZMEZXZEh5OWtsekV4Rnl2RHFRRkhyN2pUdDFnOXhVQ3NYNWZKSw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 02 Sep 2026 23:32:18 GMT
- [蔡力行談台灣 AI 時代獨特價值，彈性、速度、規模並攜手夥伴共創多贏 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiuAFBVV95cUxOcDlXUjBOeDlvRElCSnVmS1czNGxkSjlKUzFPRzBrcGRyT0hFT3R4TmpLTFgtMjk5NnhFal9WWlRpaHEwS1lCYVJQQ3oyQ2JjckZ0b3JwclV2aXcwVE1ULUVzczVVeE9aX3NrLVYtU2dYeFlXVkJtLXo5R2RxUGl5NG5kX3BXMDVTaW1aZ0F1RHdWVV9KS3RwUnhGWGs2RlVtaldoUGdra1ZWNHZQbjNQYll4Yk5qZFdi?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 02 Sep 2026 10:32:41 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：INTC, AMD, AVGO: Chip Stocks Jump Premarket After Nvidia's Blowout Report - Stocktwits；Semiconductor Stocks Slide as Global Bond Selloff Lifts Yields: Intel Drops 3%, NVIDIA and AMD Slip - 24/7 Wall St.；SEMICON半導體展開幕 世界肯定台灣實力 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | -21.48% | N/A | 90.05 | 114.68 | -21.48% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +11.79% | +6.28% | 224.41 | 224.41 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | -11.44% | N/A | 457.06 | 516.10 | -11.44% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | 0.00 | -5.66% | -17.80% | 367.24 | 446.77 | -17.80% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -1.45% | -1.24% | 2,385.00 | 2,440.00 | -2.25% | 不適用 | 86.28 | 27.65 | 467.58B TWD / 44.69% | 2026-08-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | -3.08% | +2.02% | 126.00 | 164.50 | -23.40% | 不適用 | 6.68 | 18.95 | 23.84B TWD / 18.98% | 2026-08-01 |
| MU 美光 | 產業/供應鏈推估 | 0.00 | -1.54% | N/A | 956.08 | 971.00 | -1.54% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | +4.61% | +3.60% | 1,553.40 | 2,335.00 | -33.47% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC、Intel」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [INTC, AMD, AVGO: Chip Stocks Jump Premarket After Nvidia's Blowout Report - Stocktwits](https://news.google.com/rss/articles/CBMizwFBVV95cUxPQUU4dTZXYndUX2YwZlZ6VmR6d3JoV2dDbE1XR1FKS0p2YTZScmlIclZkTUxxb0paRW00TEgwVlE1Qk5hT3BnM3J4eVZqVDBpZ3o1blFiYTQ5M2t3OTlJU3pud01kVlJYQzFVaF82a2xfWXRfM2R2MzBVRDczX0pnRkpPZ3dpam03QlhibkliRnQ3NWhJU25VM0d1bVlvSm02bjJaV2pjZlJwTUpVVnZCMHRxYjFFd2Q2RXRNOFl3ZkItc0llS0JKR2dVN1VORDg?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 02 Sep 2026 15:58:59 GMT
- [Semiconductor Stocks Slide as Global Bond Selloff Lifts Yields: Intel Drops 3%, NVIDIA and AMD Slip - 24/7 Wall St.](https://news.google.com/rss/articles/CBMihgJBVV95cUxNTEUtZVdRb2w2ZGY3SXJBZmpaM3VmMzVxbk9CNV9OX3B4RmFpNzlGWWN4eXBjU1JsRHd1OGplT2dGVlg5VVdUc0x0OThJOW12ZS16TFhQV2s4UXVRX2hRcjNrdlB3RlR0ZnNPQ1F6bTVDUW1BeHRYSnJ0bHQ5RFY3SEtkam1FdE9SNFVSMmhIb0tJMk1yWTdhRnM2N05BX1VZZ3NnYWx2MHZyLVdwZFZnRzhpa1dJcmZ3LXFxTXBYT2U2bEl0aGF4VFczZmpxSlAwc2x3RVJpcTh3cnJTVWpUblRPa25pWjAya0lnQVB6TDM4Wm85cjhFZFlXOEZ6Q2ZWUVZFTFZR?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 01 Sep 2026 13:15:00 GMT
- [SEMICON半導體展開幕 世界肯定台灣實力 - 中央社 CNA](https://news.google.com/rss/articles/CBMiU0FVX3lxTE5NVjdlVXRHaHhORDFRUHRhVHRVendLUmU5eUJWNk5TWm50djhiQ3BUbDRnUGxwbGpWbkl4NjNfWnRUM2JjSGluREJtZkFDTU9kUE1v?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 02 Sep 2026 09:29:52 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：美商務部長：擬加徵半導體關稅在美生產可豁免| 國際 - 中央社 CNA；AI 時代全球布局戰略，劉揚偉提倡與台灣攜手製造新供應鏈視野 - TechNews 科技新報；2030 年兆級 AI 商機下，台灣材料供應鏈如何轉型？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +4.13% | +16.54% | 324.96 | 325.13 | -0.05% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | -0.79% | +1.83% | 251.00 | 289.00 | -13.15% | 不適用 | 15.21 | 16.55 | 946.51B TWD / 54.19% | 2026-08-01 |

關聯理由（前 3）：
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [美商務部長：擬加徵半導體關稅在美生產可豁免| 國際 - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9uRW1LYWp4YWN6aDlzSHFBdm0xbGFjb1hMcEVlcWlhNTU0VFg2ZkpsYlVSaE84LVB5TUFjcnpTVGdOdGQ4bVRQVFlfenozaTliQ2VXaGpITVlxRmpHVHQ0?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 02 Sep 2026 16:55:00 GMT
- [AI 時代全球布局戰略，劉揚偉提倡與台灣攜手製造新供應鏈視野 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiwAFBVV95cUxPb1RFX0V0cmRIWGNCQ0MxZVI3bnlrTko0ejFPOC1hZm82WEdBbUl6MTE1SGpPclN1SFFQeF85MFJrYnJySTJWV0FLNjVjc2Z5QXE4VkEzWnVfZzhPWVhUb2YzTFRRRlNxRmxGWlFEV2NORHljQUVMTi1NUmlnYVZRdU5yeE11OEl3dkJabElqSmxzRTlzNVBmcXU2TGFGQUUzcERsNnVZTExQc3hOWFZ1UzhObElrQXNJY1RGcjRFX3Q?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 02 Sep 2026 11:03:06 GMT
- [2030 年兆級 AI 商機下，台灣材料供應鏈如何轉型？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMiuAFBVV95cUxQbC0xRkFRVVFqczFXMGU2WXpWa0lLU2YweEV3NjN5NFU0cnFFdk1lTWpLZ3FsRlIyUjl6eEFNdFhhLVFlcVp0X0Fwb2NfdTZfenRmeHNDeVNtY21QdEw2eFNBRnBsamgtR1lITHpqbk44UVZvVVZneUY0S0hfaDVEZm9FWm9SYk1RLUJHUWRpcndCakh4OVpJWXA2QVJUWi03cTVpbXJFNm1RRGxHNGNiTmFPbnhJRTVh?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 02 Sep 2026 10:31:23 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股往新高挑戰 分析師看好這五族群可以買、欣興也被點名 - money.udn.com；台股外資殺盤砍近千億 後市留意美國股債及大盤技術面等三風險 - money.udn.com；台股基金強勢 22檔績效翻倍 中小型五檔今年來最高漲逾150% - money.udn.com

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3037 欣興 | 新聞直接提及 | +0.21 | -12.34% | -16.12% | 973.00 | 1,070.00 | -9.07% | 背離 | 15.49 | 64.78 | 16.25B TWD / 43.69% | 2026-08-01 |

關聯理由（前 3）：
- 3037：新聞直接提及「欣興」，共 1 篇新聞命中。

### 主要來源

- [台股往新高挑戰 分析師看好這五族群可以買、欣興也被點名 - money.udn.com](https://news.google.com/rss/articles/CBMiWkFVX3lxTE93Mm5QUy12TlVCc2wyamZtLXI2MkJOMmlEV2JIWHVCWUNUWVBjTEZtdklJd3FpMGJBSnVsVFM2RERmZXVLakhyR0FORjVNX3FvWmdHOXQzbllmd9IBX0FVX3lxTE9IcWIxU1dMMENMaFFONEctbWxVSllyWG9pR2RLbk5EWHRhcS1RTjdNeWpjT2FiemE2R1BLbFliV2VlakkydUM0T1lfWmhjbG1fdWVFQms0b0VDa1Z1cDRF?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 01 Sep 2026 09:00:00 GMT
- [台股外資殺盤砍近千億 後市留意美國股債及大盤技術面等三風險 - money.udn.com](https://news.google.com/rss/articles/CBMiWkFVX3lxTE0zVVNBXzJiVFJBTUt3T0NRVnNZb3hwWksxTWtZOXVHQ2QzOFdmcWMzRDNlLUhWWEVyT1lTNVUzVlhZRVh6TVQ1cGVsa1JIMnhOQmM5LXdtcDBtd9IBX0FVX3lxTFB0OVFHZjlBS0Y5VXRPNE5USllESEtNX3FTVzdzVXFOMzRiUHV5TkpJZzJhbTVtUC1LdjN3MWJrSDR3VG1vZVRnSTk4N2xNM3lJak9RZ3BsZ2lUdVZzQ0RZ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 02 Sep 2026 04:00:00 GMT
- [台股基金強勢 22檔績效翻倍 中小型五檔今年來最高漲逾150% - money.udn.com](https://news.google.com/rss/articles/CBMiWkFVX3lxTE85cVk1UEJGV2lhQXZtRVgxX0lxeFF0Y09VeTdHNld2VUNGcDBmM3dMc3VFQks2c3JQcXpIT1NWZ1FwVE5ETEwyd3ktWkVXWVVFaDBpVVVmYndvUdIBX0FVX3lxTFBmVE03cWpqTkRZMVU3RWoxakFQYnB2S2VZVUhEeU0tVC1EYloxQTN5WGo2djRENlFMc0lCRC1IaUFGOGYxYkQ3aXM4WGFUb0k1X21xa0VKR21EMlBzZHc0?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 02 Sep 2026 16:14:52 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：MU And SNDK's Nascent Rebound Faces A New Test — China's CXMT Reportedly Makes Major Breakthrough With New AI Memory Chip - TradingView；Micron, SanDisk stocks slip premarket as a new China risk emerges - Invezz；大摩：AI 時代記憶體進占主導地位，看好兩家台系供應商優於大盤評等 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | -0.48 | -1.54% | N/A | 956.08 | 971.00 | -1.54% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.24 | +4.61% | +3.60% | 1,553.40 | 2,335.00 | -33.47% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +11.79% | +6.28% | 224.41 | 224.41 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron」，共 2 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：risk。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK、SanDisk」，共 2 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：risk。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [MU And SNDK's Nascent Rebound Faces A New Test — China's CXMT Reportedly Makes Major Breakthrough With New AI Memory Chip - TradingView](https://news.google.com/rss/articles/CBMiiwJBVV95cUxPazJPY0tBOWJOQkp0ekcyUXQtbTlRWWFaLTBUOFZOMDBIQzNQQ0lzeU5XbGw5ZHBzTWdXZWpodktmanpxTzNkaDVLNEhaR3lqc21zUFludjYtYTY4czZKM0dQU0hrTW1wQ3RoaEhlNWFLWEpvVVZhYXNMb3ZlcEZLOU1vb1MwZEQ0NWpaOGhEX0E2U3lQZ2FLQXNNdU9XVEtWc3pzbjVMZ2hzd2hXdTBIYWRqQmp6dHE1akgyWjRJUWdyTDZVWHc1Y0tUZzFjbWJfbHJOblJpb3JMLWYxX1ZtS0pCOGFCcDVDMmZMSXNEcWVqVlRjam83UU5va0RDMzFnajRMVUVTMHQ2Z3M?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 01 Sep 2026 04:14:16 GMT
- [Micron, SanDisk stocks slip premarket as a new China risk emerges - Invezz](https://news.google.com/rss/articles/CBMiogFBVV95cUxQSlJOUnYwWUh1STZUb3hOem52cFBIaFhFWERxdEZfcGlBc282M3A3b2xPcGk5Q2t0UTQ2ekFNYXk5cFhaZjBHRTg5NDNIS3hyUktvUEp5SnVoMmdjWGZISnBmRmJiZGd4S214Ri1JSDVqY040RUEtVkIwOFRmYXhmUnZXSHBNc0dhX0p1a2hOQTM4dEVvVEk3UzFaRmVrYUkzQkE?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 01 Sep 2026 11:15:38 GMT
- [大摩：AI 時代記憶體進占主導地位，看好兩家台系供應商優於大盤評等 - TechNews 科技新報](https://news.google.com/rss/articles/CBMic0FVX3lxTE9sNFcwRGxyUnB6VjE3REFKTGpXRk9ZdmNvWFhsWWlUSFJxcnY5dU5OOThIekZNWXdTWkhicGcwbnVIbGh4RDRBWTZ6eVdvaWNKLVVpZVJpMm1yQVdkQnVyUXFWU3AwcDRmYXNHT1oyYk9OWGc?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 02 Sep 2026 04:11:59 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：投資觀點-台股還值得買進？ - MoneyDJ；《台股盤後》重摔784點、日K翻黑，跌破5日線- 新聞 - MoneyDJ；國票證券：台股量能將是攻高關鍵 - 台股 - 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [投資觀點-台股還值得買進？ - MoneyDJ](https://news.google.com/rss/articles/CBMilgFBVV95cUxPT2RpUGI0WlA3UmpMeUp3blFpTXNheHRKSzc3Q0tkOWl1cXpKZjBiajR0b3dQSmNwMVRKUmNhYzk5NXJuSzZsdzc3N3FNbGVlbmh6bHlIbUl6cHlnS2lscHhEczhuQTdDX2c2ZllzbEc3R3VWMWFNTEdUOHh4QklhVVhyTDI5M1d1MzR4ekpUNzZXd3czX1E?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 02 Sep 2026 16:11:03 GMT
- [《台股盤後》重摔784點、日K翻黑，跌破5日線- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPWGVZYzhJUmkwUXN0US03bmNhcWhOT2RPbjRRc2wtS2Y1SERzUm5nSHZqeXJBVVYxalhfUThtVVpFUmV3QVJJUjJCd0lWSHZyRWVhZFloYzVTTXVaNmtFS1pEUUJJZktXRmt3WWo4bktDNlB4eFJaNlZMZjZOcVlJS1NCM1VaS1Bid1VId3ptTzhpdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 02 Sep 2026 08:10:00 GMT
- [國票證券：台股量能將是攻高關鍵 - 台股 - 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMiggFBVV95cUxQcG0yWWNlZkNpQU5DOTNsVWlIaWVQMjNwcnUzZW9nWlZNYUROWnVUYzcySnNrcFhOcHc4d2hlaDROaXZ5MXV3aTlnYUtfRTZROGJGaHJKN21EeUtwUENUNWkyc1RBYUhEVVJBel9iR2NUWUFGQjhFOXhqQThiU1lhbXVn?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 02 Sep 2026 00:30:00 GMT

## 新興題材：2030半導體營收

摘要：新興題材：2030半導體營收 相關新聞集中在：SEMI總裁：台灣是AI重鎮 2030半導體營收衝2兆美元| 產經 - 中央社 CNA

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [SEMI總裁：台灣是AI重鎮 2030半導體營收衝2兆美元| 產經 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1uR3d0Q01PT2ZlZk5Sa0lNLXM4T0JSSmlSUTFQOTB1QzlKLXBCVUVZR000Q0VMbjJKZTlXOU8yZjJ2UC1SdWRPQW9oZ2dGb1dTVTZMTW9ZSWNPREhaV3c?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 02 Sep 2026 04:40:00 GMT

## 新興題材：擬加徵半導體關稅

摘要：新興題材：擬加徵半導體關稅 相關新聞集中在：美商務部長：擬加徵半導體關稅在美生產可豁免| 國際 - 中央社 CNA

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [美商務部長：擬加徵半導體關稅在美生產可豁免| 國際 - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9uRW1LYWp4YWN6aDlzSHFBdm0xbGFjb1hMcEVlcWlhNTU0VFg2ZkpsYlVSaE84LVB5TUFjcnpTVGdOdGQ4bVRQVFlfenozaTliQ2VXaGpITVlxRmpHVHQ0?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 02 Sep 2026 16:55:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
