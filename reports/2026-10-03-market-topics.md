# 每日股市熱門話題分析 - 2026-10-03

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **散熱與液冷供應鏈**｜中性｜熱度 2｜市場確認 87.91｜同向 1/1
2. **AI 伺服器與資料中心**｜中性｜熱度 11｜市場確認 N/A｜同向 0/0
3. **新興題材：TradingKey**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
4. **半導體與晶片供應鏈**｜中性｜熱度 5｜市場確認 N/A｜同向 0/0
5. **關稅與供應鏈轉移**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.35（樣本 6）
- 5日相關係數：0.13（樣本 3）
- 同向比例：1/6

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 散熱與液冷供應鏈 | 87.91 | 1/1 | 0 | +5.97% | +16.92% |
| AI 伺服器與資料中心 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：TradingKey | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 關稅與供應鏈轉移 | N/A | 0/0 | 0 | N/A | N/A |
| 記憶體與 HBM 供應鏈 | 0.00 | 0/5 | 5 | -9.58% | -9.43% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-09-20 | -0.04 | -0.25 | +30.77% | 13 |
| 2026-09-21 | -0.15 | -0.05 | +61.54% | 13 |
| 2026-09-22 | -0.00 | -0.01 | +88.24% | 17 |
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

## 歷史回測摘要

- 回測日期：2026-10-03
- 近5日 3日相關：-0.02
- 近5日 5日相關：0.30
- 同向比例：+69.23%
- 權重狀態：未調整

- 方向準確度：+69.23%
- 信心排序準確度：-0.02
- 診斷：低相關

調整原因：近 5 日有效樣本 13 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：散熱與液冷供應鏈 相關新聞集中在：NVIDIA Vera Rubin 為什麼需要液冷？AI 散熱需求爆發，散熱股都會受惠嗎？-實習大人-林序安 - cmnews.com.tw；焦點股》健策：AI散熱賣壓沉重 再探跌停 - stock.ltn.com.tw

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | +1.18% | -0.86% | 3,440.00 | 3,510.00 | -1.99% | 不適用 | 75.13 | 45.85 | 19.48B TWD / 54.34% | 2026-09-01 |
| NVDA 輝達 | 新聞直接提及 | +0.42 | +5.97% | +16.92% | 233.95 | 233.95 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「散熱」，共 2 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：跌停, 受惠。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 方向判斷命中詞：受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [NVIDIA Vera Rubin 為什麼需要液冷？AI 散熱需求爆發，散熱股都會受惠嗎？-實習大人-林序安 - cmnews.com.tw](https://news.google.com/rss/articles/CBMihwFBVV95cUxOUlVqWXU3REtfc2lQdDF6alJWZzZaQ0RnTm13ZGRDbkRvSG1Gdmg3b3Zna0JJcy1RTzhCZDNJVEVDSXVjRE1hSlRzZGt4WDh0bHROUTQxbDZoSm8zSzZ5bk1wSHVCeVNYNXh2WmZHY2FZS2RnbnliYnpUX1g1Tml1SjExWGV0U0U?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 02 Oct 2026 01:43:41 GMT
- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - stock.ltn.com.tw](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 02 Oct 2026 19:06:07 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：從移民少女到 AI 教母，李飛飛走進 AMD 技術核心 - TechNews 科技新報；「AI 寫程式已超越我巔峰時期」，Google 前執行長施密特：下代工程師將成為 AI 架構師 - TechNews 科技新報；AI 代理入侵風險是否延緩企業導入？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AMD 超微 | 新聞直接提及 | 0.00 | +22.83% | N/A | 633.91 | 633.91 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | +4.05% | N/A | 119.33 | 120.00 | -0.56% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +5.97% | +16.92% | 233.95 | 233.95 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +1.01% | 0.00% | 2,500.00 | 2,510.00 | -0.40% | 不適用 | 86.28 | 28.98 | 514.81B TWD / 53.32% | 2026-09-01 |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +14.95% | +5.19% | 517.53 | 517.53 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -4.10% | -5.99% | 355.14 | 446.77 | -20.51% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | +3.78% | +2.89% | 713.00 | 713.00 | 0.00% | 不適用 | 13.92 | 51.59 | 82.25B TWD / 45.66% | 2026-09-01 |
| 2454 聯發科 | 產業/供應鏈推估 | 0.00 | +0.81% | -4.53% | 4,950.00 | 4,980.00 | -0.60% | 不適用 | 60.69 | 81.75 | 64.18B TWD / 44.08% | 2026-09-01 |

關聯理由（前 3）：
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [從移民少女到 AI 教母，李飛飛走進 AMD 技術核心 - TechNews 科技新報](https://news.google.com/rss/articles/CBMijAFBVV95cUxNcERVS0hqSXZhaWpXRDcwTVZ1ZWdKRkZ4VFhKSzMyUDRsWEtQOFhfaTRVWmxOeGFhTE9pTWJGLXZIa3RDQ3AyS2s3UW9tZFRqbE9jYVlrbVdsRlJ5SzJiV0lGUWFVY2I0LVdPenItb1JIOVEyU3FqNDBHc1MtbTNwbm5VRGRlQ2pZYVZVNA?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 02 Oct 2026 06:22:22 GMT
- [「AI 寫程式已超越我巔峰時期」，Google 前執行長施密特：下代工程師將成為 AI 架構師 - TechNews 科技新報](https://news.google.com/rss/articles/CBMigwFBVV95cUxNMW5FS0VqZ0hkS2J4U2JzUWxjUjg1NEMwSXQ4RHUxY1dIR3I4MnFaNDRoOFpLc3FlWHBrVUNoMkQ1VVBTT2tqdGd2Rmk1ZFEtdFNYZE1kbExwd0l6dldpZlI4NzhDa1RuNG5ybzViMW5uRFhKTTdOSHEzSkliNzNUWlhLVQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 02 Oct 2026 06:42:22 GMT
- [AI 代理入侵風險是否延緩企業導入？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMitwFBVV95cUxNV1FxMXdPbng4S3NtTm9zYWlSNEZ0QnJXelNjOGpjV1BidTBBT0dxY2gtNm9XRk9fRzZJR0xlNV80MVM1dk1oR09lRmR5X3Zjd1BnYUMza3I5UUFKMmxrcGVhc3NEcmo4Tno5NXptaVhlOTFZUW1Ed2RqQlB4NFI0cGlvZE95ejI1Ry03dHFaQ0g2OHFsT0NzQUd3UnVLcGlVek02OEdjZ2tBRDc1U0h1SWhILW9nM1E?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 02 Oct 2026 18:23:19 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Memory Giant SK Hynix Nears US Listing: Some Key Information You Need to Know - TradingKey；Micron Technology Inc (MU) Stock Analysis & Forecast - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | +10.70% | N/A | 1,074.89 | 1,097.39 | -2.05% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「memory、MU」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Memory Giant SK Hynix Nears US Listing: Some Key Information You Need to Know - TradingKey](https://news.google.com/rss/articles/CBMisgFBVV95cUxNY3h5Smd3UUktRzdfMXRISlplRm1CNG52TkJPSjRNSG43RGsxZHJENXlnaXFscVJNeXRORDFyenkyQ3pXZmM0SDU5VzEtX1gycFpwMHZ2d0RWeldvSzRUZGE4VUZfMGNzUDJkTkZUb0hHSkUtV2ZXeHdJTW56ZnJUUXJkMlZPYndOQ3piNlQ5RVY2UnpUWEZyM1l6NTFVODB5VURSbnFIYlU1bmdTTmJ5QVB3?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 01 Oct 2026 10:42:15 GMT
- [Micron Technology Inc (MU) Stock Analysis & Forecast - TradingKey](https://news.google.com/rss/articles/CBMiY0FVX3lxTFB2cjlJNEFoZnN6al9fVWlOSktTV2tWRzJ1c0c2SklreGhaeHF5VlZlSjNNRE1SaXlnaUVsQ1FaMXFtZUlvM19kUzhHdURNU1VkNmNhLTNPSDNtXzBpSHNZS0xkNA?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 02 Oct 2026 11:12:06 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：AMD Climbs 3% as Chip Stocks Extend Their Run; Arm Jumps 8%, NVIDIA Rises 2% - 24/7 Wall St.；AI 需求爆發如何重塑晶圓代工競爭格局？ - TechNews 科技新報；Stocks making the biggest moves midday: Tesla, Broadcom, Nike, ON Semiconductor & more - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | 0.00 | +5.97% | +16.92% | 233.95 | 233.95 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | +22.83% | N/A | 633.91 | 633.91 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | 0.00 | -4.10% | -5.99% | 355.14 | 446.77 | -20.51% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| TSLA 特斯拉 | 新聞直接提及 | 0.00 | +0.72% | -11.89% | 370.59 | 456.56 | -18.83% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | +4.05% | N/A | 119.33 | 120.00 | -0.56% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | +1.01% | 0.00% | 2,500.00 | 2,510.00 | -0.40% | 不適用 | 86.28 | 28.98 | 514.81B TWD / 53.32% | 2026-09-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | +5.21% | +0.94% | 161.50 | 164.50 | -1.82% | 不適用 | 6.68 | 24.29 | 25.04B TWD / 30.71% | 2026-09-01 |
| MU 美光 | 產業/供應鏈推估 | 0.00 | +10.70% | N/A | 1,074.89 | 1,097.39 | -2.05% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AVGO：新聞直接提及「Broadcom」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AMD Climbs 3% as Chip Stocks Extend Their Run; Arm Jumps 8%, NVIDIA Rises 2% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMitgFBVV95cUxQOUVMNnlzM3F6SjRudU9qR25WZnl1bklOSVozNWJJVVhZSTE4dUZDTDdxc3RyaDd1djVwYmdnV1dyS2hITnJ4REtGMmVJeC0xN1REMXVGOGp5dTU0RHNacERQYW1wMzZ0M0ZzZTNJWmZKeDl5b19PQmNzRjBCSS1wWVkwRFFNOFJJNlFfVUFBYlNJVnd1NndsZG5jcmFHYTJHVVl1QWcyTS1ueVo2bEJCZ1hKd2F2Zw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 02 Oct 2026 15:47:00 GMT
- [AI 需求爆發如何重塑晶圓代工競爭格局？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMigAFBVV95cUxPb3hOeG5BMDRBYVBxSUw4bTVybktmYURKMFhOdjE0WHAwNUZVa2tiSDNyV2hrS3RxZWFOUDRUb1g4R1RVLXRBNzF0SW0wUUVNQUFtUmZYbXBCZTdDRkl2clhMSFBsU2EyVmp4NkRpMkdld09GQ1dyU1V1eUhxRXFBeQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 02 Oct 2026 14:56:46 GMT
- [Stocks making the biggest moves midday: Tesla, Broadcom, Nike, ON Semiconductor & more - CNBC](https://news.google.com/rss/articles/CBMinwFBVV95cUxQc2dHVDZOU0dKSXRCYmNEY3pWQ193T1U5SkRPRmpzS0ZnSThZNk5Kd2toYXN2clJ6UHdrNlpHQ24yUjFrTlpxbk1UZm5ja2RQTUEzMTVaU1FUUDVxOXdVOVhlQng4c1Fua1Y3N2c5UDdoZ2UybUFTc0cyV0JQMmJLanlWSk9ubVJ3Q3JzRGQ3bkp4MEhCZWF5ZjRzWC1qZ28?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 02 Oct 2026 16:56:21 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：台股5萬點進入射程 高價股強者恆強 AI供應鏈續撐多頭 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +6.93% | +19.67% | 333.69 | 333.69 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | +0.20% | -1.95% | 251.00 | 289.00 | -13.15% | 不適用 | 15.21 | 16.55 | 921.77B TWD / 51.98% | 2026-09-01 |

關聯理由（前 3）：
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [台股5萬點進入射程 高價股強者恆強 AI供應鏈續撐多頭 - 經濟日報](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBNMm5pYWtDQ2Nvc2lKdXpESFdTX2NHZmJ2cTBKOThEMWV3dEw2dU9DdkNsbUxYQVA0RW9HSGZVLWpQaUJxX0J1YzdGbWRUOGNPeFlTNHpqbWJudFHSAV9BVV95cUxQSnZjX1dLTWhSU0tpSGNWcE5VYTNiNm1OUl9nREJDalFQQXFhcHFtUFRFSTFQaHF6MGgwRFhVYmJ2cUdjR0Zqb0dQaUxYb1RFV1JkR0JDajB6YU9zWVlSTQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 02 Oct 2026 16:13:31 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：INTC, AMD, MU, NVDA: Chip Stocks Tumble Again, Stalling A Nascent Rebound - Stocktwits；AI Chip Rally Broadens as Micron's Outlook, Lower Yields Lift Nvidia, AMD and Peers - finance.biggo.com；Micron Revenue Surges 379%: 4 Top AI Chip Stocks (NASDAQ:MU) - Seeking Alpha

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | -0.28 | +10.70% | N/A | 1,074.89 | 1,097.39 | -2.05% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | -0.26 | +5.97% | +16.92% | 233.95 | 233.95 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | -0.24 | +22.83% | N/A | 633.91 | 633.91 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | -0.21 | +4.05% | N/A | 119.33 | 120.00 | -0.56% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | -0.07 | +4.37% | +1.94% | 1,787.69 | 2,335.00 | -23.44% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron、memory」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：lower, risk, rally, surges。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVDA、NVIDIA」，共 2 篇新聞命中。 同時符合主題標籤：HBM。 方向判斷命中詞：lower, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 方向判斷命中詞：lower, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [INTC, AMD, MU, NVDA: Chip Stocks Tumble Again, Stalling A Nascent Rebound - Stocktwits](https://news.google.com/rss/articles/CBMizAFBVV95cUxORHdiV3k3V2RtSVBoRTJaaW5PcTZhQzBTNlRUM2VqcjBpcTViNkREdS1uVGtnb1FYckxkREh4Z00zN2NBSnlNRGZ0SWhpNERydkZKTlJCejRLQ2xqejNxREhfS1ZzSm5CdjhrZzlZTnRiN1Z6M3VtSDU1d2trMG9jVFUwT3hadk93R2l0TlBBZkttekkyTDBHTW1Zc01YTmNzRVJ3Tm11dGcwNktNX04yU0pLUENBQl9sOUI4dVMydW02UUhxZDVXX2pZT0M?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 02 Oct 2026 11:11:43 GMT
- [AI Chip Rally Broadens as Micron's Outlook, Lower Yields Lift Nvidia, AMD and Peers - finance.biggo.com](https://news.google.com/rss/articles/CBMidkFVX3lxTE96bS1WbUVMM3VreHA2ZE53UUQtV0JFaGViakdDUk50YURXOGVONUVndW4tY3FvYmZrUWpicHZoNWVscVZ1dG1VdU1xeEM2akctQXBCV3hEb0RXLXhaZkpWRHZmLUpiU3dfQTdUY1pfUTdWZEE5TWc?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 02 Oct 2026 18:34:00 GMT
- [Micron Revenue Surges 379%: 4 Top AI Chip Stocks (NASDAQ:MU) - Seeking Alpha](https://news.google.com/rss/articles/CBMimwFBVV95cUxNeklWZ1dfNTRJMHJYdENCY1l2eHBhX1pFOUYteDRlNXhIbEIzS21EekRnT3RscnVMTGFCbHBkeTZFMDNMLTFoQXdfbVp1M0hQTm9wdkZyQlpWZC1JeGhyYnpjcGEtRzF4U25lQW9uXzQyNFlDRnhqanRuTlJ1RmVOSVJtX1JULTBYMnlubXhuRHZlUmZOLVNyTG1SVQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 01 Oct 2026 16:31:53 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：《台股盤後》收漲122點、再寫新高；週K連三紅- 新聞 - MoneyDJ理財網；台股ETF規模逾8兆！ 0050就占2.5兆穩居第一- 新聞 - MoneyDJ理財網；國票證券：台股多方架構並未出現敗筆- 新聞 - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》收漲122點、再寫新高；週K連三紅- 新聞 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikgFBVV95cUxOVHNBdlcyV2ZrREZZNjR0VGtCNGVJQ3NCX2gtQjU3eWp2UWRZTWxUZXhLRDlPaDhaOEwyaDBKMDlPRGY5aEdqT2tSTEtvWGxpWHdWZ2txeEZfN0Z5RGRBT005TGllb3hhZXFYZS1xaFFhakxxc1FMazRMVjh3TlB1OF9oNjB3M29fYnVUNXZrOXNIZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 02 Oct 2026 07:57:00 GMT
- [台股ETF規模逾8兆！ 0050就占2.5兆穩居第一- 新聞 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikgFBVV95cUxNb3ZUa1RkZTVCUzJyT0ZIS1NXdVk3RW1tdGN5aG40VS1WY1lYT1NiUEtWZ1RTbGE2SGZRNkRQOW5xNF90clZJSENTOWtFVWY3RmExZU5QZW10OTU3M0xBMjlJLWJnd0FmR1BnTlRlcXdBSzBJUTVONXFyLU5sMzhHQWlxci1ZYlVwU3p1UjhYUTlEdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 02 Oct 2026 08:52:00 GMT
- [國票證券：台股多方架構並未出現敗筆- 新聞 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikgFBVV95cUxOSFFwTUpJQi1nQ2l0N01IM3hPS1hTcDU3YWNiOERMS09MenA2clVuZllEZTM2VExTYTFYbU9pSklVVHNXSVFuU2VTb0xleXhxNkUxRmh5enpoNkptalZBc25MSkp2M0xZNy1hU1JMRU5Fd3g0MUJWTGk4VmI3djM2ZEc2RUQ0TWQ5ZEU4c21QVWtmdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 02 Oct 2026 00:37:00 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：個股動態報導內容-9E2D03CC-EA86-401C-B0D8-5CCBCC8B905B - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-9E2D03CC-EA86-401C-B0D8-5CCBCC8B905B - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxPRUdfLUVQVTI2MmVxR0lhcUhmWkVDZk5mckdXNERPdXlzR1FHeGtIY0MyMlJCblFaTDZ2b1JDZVF6MjM5QjhXS0pMbFloSERLak53bmNpeUw2bHJnZDJCRG83YUpxSkg5Zms5aGhhWEZzc0UxcThUSFNhWTBrV3ppRlJTVEtPLXlRcDNFbFlsMlNSRHdy?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 02 Oct 2026 20:51:57 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
