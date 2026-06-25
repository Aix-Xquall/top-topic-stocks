# 每日股市熱門話題分析 - 2026-06-26

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜正向｜熱度 24｜市場確認 36.16｜同向 1/2
2. **利率與成長股估值**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0
3. **新興題材：CoinDesk**｜正向｜熱度 1｜市場確認 N/A｜同向 0/0
4. **半導體與晶片供應鏈**｜正向｜熱度 7｜市場確認 26.99｜同向 2/5
5. **AI 伺服器與資料中心**｜正向｜熱度 9｜市場確認 0.00｜同向 0/6

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.08（樣本 16）
- 5日相關係數：0.04（樣本 16）
- 同向比例：4/16

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 36.16 | 1/2 | 1 | +0.39% | +14.84% |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：CoinDesk | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | 26.99 | 2/5 | 3 | -0.34% | +15.19% |
| AI 伺服器與資料中心 | 0.00 | 0/6 | 6 | -5.74% | +0.54% |
| 消費電子與手機 | 18.60 | 1/3 | 2 | -1.58% | +4.47% |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 相關性偏弱；應提高同向價格確認權重，降低泛 AI、泛半導體等寬標籤推估權重。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-06-13 | 0.87 | 0.98 | +100.00% | 4 |
| 2026-06-14 | 0.82 | 0.98 | +100.00% | 3 |
| 2026-06-15 | 0.87 | 0.56 | +42.86% | 7 |
| 2026-06-16 | 0.39 | 0.50 | +76.92% | 13 |
| 2026-06-17 | 0.17 | 0.47 | +62.50% | 8 |
| 2026-06-18 | -0.41 | -0.41 | +42.86% | 7 |
| 2026-06-19 | 0.06 | -0.04 | +57.14% | 7 |
| 2026-06-20 | 0.29 | 0.21 | +63.16% | 19 |
| 2026-06-21 | -0.01 | 0.32 | +55.56% | 18 |
| 2026-06-22 | -0.87 | -0.87 | +100.00% | 3 |
| 2026-06-23 | 0.38 | 0.01 | +62.50% | 8 |
| 2026-06-24 | -0.38 | -0.11 | +25.00% | 12 |
| 2026-06-25 | 0.10 | -0.21 | +20.00% | 5 |
| 2026-06-26 | 0.08 | 0.04 | +25.00% | 16 |

## 歷史回測摘要

- 回測日期：2026-06-26
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

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Micron Rockets On 346% Revenue Surge: 4 Top AI Chip Stocks (NASDAQ:MU) - Seeking Alpha；AI Chip Stocks Stage Rebound: Nvidia, AMD Lead Recovery Ahead of Micron Earnings Shock - TradingView；Micron Technology (MU) surged 16% after blowout earnings and strong guidance - CoinDesk

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.65 | N/A | N/A | 1,213.56 | 1,213.56 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.57 | +2.69% | +19.21% | 2,335.00 | 2,335.00 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.25 | -1.92% | +10.47% | 195.74 | 211.14 | -7.29% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.48 | N/A | N/A | 532.57 | 532.57 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU、Micron」，共 5 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：boost, strong, surge, surges, surged。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SNDK」，共 1 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：boost, surges, shortage。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Micron Rockets On 346% Revenue Surge: 4 Top AI Chip Stocks (NASDAQ:MU) - Seeking Alpha](https://news.google.com/rss/articles/CBMiqAFBVV95cUxNdERER2JOM2dGdE5HbGREc2wyaG5RV0RpS1JCem9VMElJX3ZYSDEwYzZzQmdHbUZtVjhMRWRWS0VfeXRrNTQ2N1VTbjQ3UzVpeEZtaU53bUNIWXhlZjMwUWZnVzlhNjV1dTJZckRfM01HUlJyR1pxTGx2S0UxalF5cHJ6ZXRZa01xTFloeDZ6YkFaWUN4cUNvdVRhV1ZyV0Q4RFdYeUlZUy0?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 25 Jun 2026 17:33:04 GMT
- [AI Chip Stocks Stage Rebound: Nvidia, AMD Lead Recovery Ahead of Micron Earnings Shock - TradingView](https://news.google.com/rss/articles/CBMi3AFBVV95cUxNX3R0SldMUHVoZE1DdFdXNE8xZnJyUVNVSnFIRWxFcUdCVDc4WUhlN2dhOVJRNlZpdGJWX1ROa2pacy13TUR4MjNBdDNEVDUzWUZiSTFJWE41b19CdzBMUGFwU3dvT19uNC1mZUVxM01oVGtGcENFUWNYRTIyc1Bxa2FVMVBUWVZFeFgwblN2Ty1aQkFBVVJZd1RwZXBmVGdmYTVYYjRlejRocERxS3BHa2FIUnVRT2pnVnUyelBiNjk1dkExX3ptc3pNc1d0TEhJNHhmOG1nYUNJcjBD?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 24 Jun 2026 19:34:27 GMT
- [Micron Technology (MU) surged 16% after blowout earnings and strong guidance - CoinDesk](https://news.google.com/rss/articles/CBMitwFBVV95cUxOT25Eb3gxMDAxbjQ5TjhLSlRhZ21lQWg2WU9MejJrb09iR0dYVk9Ha1RvTHBVYWg3Uzl0TGo1RDRhVFhYcWhmeW1QQ2R5SllsNTM4Rkp5VTB6R2RXeWY5UjJjZ19fWU5Jc2JvVTBFS1NXOXJsbGQ4djl6YmpDVVpHazRjUTF2aG0tOFhRNEZLTFd2d3plckZHRGstLXFMR2xqWnBZNG1odEdBVnFtcmx0aWtGenRIMkk?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 25 Jun 2026 13:38:06 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：台股陷「估值卸妝」陰霾 外資瘋狂提款 賣超1,774億元史上最大量 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | -10.16% | -30.37% | 352.83 | 506.69 | -30.37% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [台股陷「估值卸妝」陰霾 外資瘋狂提款 賣超1,774億元史上最大量 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE51eVhJVTVMZUROT1RCZ0ZNM1BmeHdJUnh0NU1lTEdKMHdRLS1xRVNIUW92TGp4QmRrTTFSYTh6ZmhwYzlnODAyTE5HZS1EZzJkUUpXekZBa1pxUdIBX0FVX3lxTE9KeU5Cb1ltX3ZSa3NhYkI4VE5WMFNwVW1wa3d2UUI1azU1djlpZ1ZfTjJEOER3RzVLWi13em1kZEgtT1FXelR6dk5fVzBzek5rR0x5dk1iSDIwLXRFck5V?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 24 Jun 2026 09:00:00 GMT

## 新興題材：CoinDesk

摘要：新興題材：CoinDesk 相關新聞集中在：Micron Technology (MU) surged 16% after blowout earnings and strong guidance - CoinDesk

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.48 | N/A | N/A | 1,213.56 | 1,213.56 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「MU」，共 1 篇新聞命中。 方向判斷命中詞：strong, surged。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Micron Technology (MU) surged 16% after blowout earnings and strong guidance - CoinDesk](https://news.google.com/rss/articles/CBMitwFBVV95cUxOT25Eb3gxMDAxbjQ5TjhLSlRhZ21lQWg2WU9MejJrb09iR0dYVk9Ha1RvTHBVYWg3Uzl0TGo1RDRhVFhYcWhmeW1QQ2R5SllsNTM4Rkp5VTB6R2RXeWY5UjJjZ19fWU5Jc2JvVTBFS1NXOXJsbGQ4djl6YmpDVVpHazRjUTF2aG0tOFhRNEZLTFd2d3plckZHRGstLXFMR2xqWnBZNG1odEdBVnFtcmx0aWtGenRIMkk?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 25 Jun 2026 13:38:06 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Intel vs TSM: Which Chip Giant is the Better Investment? - 24/7 Wall St.；國科會通過8件投資案CPO、半導體材料助攻競爭力| 產經 - 中央社 CNA；抓住功率半導體大趨勢！功率元件是什麼？功率半導體家族大解密 台鏈生態系、產業風險一次看 - 工商時報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.60 | N/A | N/A | 132.87 | 132.87 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.03 | -4.78% | +0.21% | 2,390.00 | 2,390.00 | 0.00% | 背離 | 74.39 | 32.13 | 416.98B TWD / 30.09% | 2026-06-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.05 | +11.56% | +27.50% | 178.50 | 178.50 | 0.00% | 同向 | 4.00 | 44.85 | 22.94B TWD / 17.78% | 2026-06-01 |
| NVDA 輝達 | 產業/供應鏈推估 | +0.02 | -1.92% | +10.47% | 195.74 | 211.14 | -7.29% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.04 | N/A | N/A | 532.57 | 532.57 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | +0.04 | N/A | N/A | 1,213.56 | 1,213.56 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.04 | +2.69% | +19.21% | 2,335.00 | 2,335.00 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -9.23% | +18.58% | 378.91 | 446.77 | -15.19% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 3 篇新聞出現相關標籤。 方向判斷命中詞：rally。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 3 篇新聞出現相關標籤。 方向判斷命中詞：rally。

### 主要來源

- [Intel vs TSM: Which Chip Giant is the Better Investment? - 24/7 Wall St.](https://news.google.com/rss/articles/CBMinwFBVV95cUxPTXk5b196aEREdnN4SVFUQW9TVUczSkdTU2s3RmtJYXBhV3ZEcXNfMjFGejdNeFpkTTBlZ3dTTG9fTkZDMlNraFB2bTgxOFFsaUp6c2RKRHpiNTY4OWJ4RjVabzcyUVVhWXIwV1k1RTZOMTZndkVUV3pXRE1mdlFIaW9OVTFWdXJKVXdSYnI5d2dnZnYtdDM4YVNCMnptNFk?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 25 Jun 2026 16:23:23 GMT
- [國科會通過8件投資案CPO、半導體材料助攻競爭力| 產經 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTFA5Y1RVVTRpbldSaC1XMlFINld4c3l0ZTJwWEI4R004OTBiVjQ0X3d6TmFQQmZsTTZuZXJCYkRDNGFTemxWSjljbUFxVktqSEhfcVoyUGRGSnJDbzhQN1E?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 25 Jun 2026 11:53:00 GMT
- [抓住功率半導體大趨勢！功率元件是什麼？功率半導體家族大解密 台鏈生態系、產業風險一次看 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5xNTR6bGVVMExPeVF5UWwyeFE0eWZtU2ItVG9CTEZnMWgtX2VCMGZrdkRUTmwzWHFUNkg1NHA0MkhGbUNSOHlBbXY3amsxREczVTV4eWNpVTBNbEI3Z05j?oc=5) - https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 24 Jun 2026 04:55:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Intel (INTC) Expands Into Edge AI With Kontron And Panther Lake Chips - simplywall.st；Nvidia Earnings Today Could Swing AI Trade: AMD, Intel, TSMC Among Stocks To Watch - Stocktwits；凱基證券「AI Agent智慧牧羊犬」榮獲2026 FCA創新商務獎 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.65 | N/A | N/A | 132.87 | 132.87 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.31 | -1.92% | +10.47% | 195.74 | 211.14 | -7.29% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.60 | N/A | N/A | 532.57 | 532.57 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | +0.30 | -4.78% | +0.21% | 2,390.00 | 2,390.00 | 0.00% | 背離 | 74.39 | 32.13 | 416.98B TWD / 30.09% | 2026-06-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.02 | -10.16% | -30.37% | 352.83 | 506.69 | -30.37% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -9.23% | +18.58% | 378.91 | 446.77 | -15.19% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.02 | -4.90% | +7.73% | 641.00 | 653.00 | -1.84% | 背離 | 10.86 | 59.52 | 63.03B TWD / 28.57% | 2026-06-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.02 | -3.47% | -3.36% | 4,310.00 | 4,310.00 | 0.00% | 背離 | 62.91 | 68.69 | 47.43B TWD / 4.99% | 2026-06-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC、Intel」，共 2 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel (INTC) Expands Into Edge AI With Kontron And Panther Lake Chips - simplywall.st](https://news.google.com/rss/articles/CBMiygFBVV95cUxOUkwycExmLVdRVjJPSUxzN3BoNTVycnF3NjdwcXZ6THNieERsb2N0NXZYM1J5R0tWeFI3SlhoNERMYmFGUjg5eXRpWWctYjZoN2VSLTVZOHF3cXVEbVg2aWRKY0daWHR2UzVfamtwNDkwd2xQUUJ4Tm90UE1WaXlaZmwzX2E5d0YtNTk2MHNtR1VSZkkzNE4yd3Y3MTZxMTJSRnFsd0t1TmtSTXRWZmdIMXNtdDZ3ZWNqekZHdlV3Z1hpeU5TaEc4ZWNB0gHPAUFVX3lxTE1GdDJuYXc1UjdvZXVaQUhYcWJhZ3Y1S2doU0VNbUN2REprek5YSUJTTE5IU2lGUjdxdDhZTUV2NUZndHRSS005RmhSaGNia2IteTQzMVBFenFtejJCWHhyZUtlTXZtRTlUVzhhR0cyRkJWLVFOUDJTVzFPUEsxSUM5VXdHOUh2RTJoUEJTSGRPTGluaDVOWDI2YUdTQUo4UU8zSnJrNXhuNk05UzlzVFNmTzlNWVYwblppdlVUZGN2MGpHZjhpUEx5NV8xLWNHSQ?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 25 Jun 2026 20:22:05 GMT
- [Nvidia Earnings Today Could Swing AI Trade: AMD, Intel, TSMC Among Stocks To Watch - Stocktwits](https://news.google.com/rss/articles/CBMi2wFBVV95cUxNd1FSRGJFazNSNkNzYlJONm1DZXVGWnBwMFBXdlRsUEpHYzZGY2h4d3Jqc2JGUjNwQ0MyUGFCLU9vNUo3UjBhQk56TzlDM1dQbTFVLVlHZlNycEV4Vk1mWnhMcWVyWFBrT3lMXzRBRDlrZlpDbm9KSFMyWHV3RGZEYWRjSEdrVGRPV3BHelc0ZU10Ym1QZmQzMkMzaTNPRDhyS2pDbUJqUzczV1JEZjhnOGN3UGNtdlI5VzBud1dPZXJ1UWVId2UxOENpLU9zcldlZURyZlg4bmJEd1k?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 24 Jun 2026 19:49:31 GMT
- [凱基證券「AI Agent智慧牧羊犬」榮獲2026 FCA創新商務獎 - 中央社 CNA](https://news.google.com/rss/articles/CBMiVkFVX3lxTE5HUWNDNDI0MV93dGhIalhYSnYzbkszLWJIOHA1U0kxOGtRMGZsck5VT3Z1SHhwTDVoN1RtcXFjNi15QWtYOXRZWFl3MXhDZDNlMV9tNjhn?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 25 Jun 2026 08:13:23 GMT

## 消費電子與手機

摘要：消費電子與手機 相關新聞集中在：Intel and TSMC report divergent Q1 earnings amid AI hardware growth, with Intel rebuilding and TSMC compounding. - Pluang

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.48 | N/A | N/A | 132.87 | 132.87 | 0.00% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | +0.24 | -4.78% | +0.21% | 2,390.00 | 2,390.00 | 0.00% | 背離 | 74.39 | 32.13 | 416.98B TWD / 30.09% | 2026-06-01 |
| AAPL 蘋果 | 產業/供應鏈推估 | +0.10 | +4.15% | +18.53% | 275.15 | 312.06 | -11.83% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | +0.04 | -4.10% | -5.33% | 257.50 | 289.00 | -10.90% | 背離 | 14.13 | 18.29 | 859.41B TWD / 39.57% | 2026-06-01 |
| 2454 聯發科 | 產業/供應鏈推估 | 0.00 | -3.47% | -3.36% | 4,310.00 | 4,310.00 | 0.00% | 不適用 | 62.91 | 68.69 | 47.43B TWD / 4.99% | 2026-06-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 方向判斷命中詞：growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「TSMC」，共 1 篇新聞命中。 方向判斷命中詞：growth。
- AAPL：產業/供應鏈推估：公司標籤符合「消費電子與手機」關鍵字 hardware, consumer electronics, smartphone；其中 1 篇新聞出現相關標籤。 方向判斷命中詞：growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel and TSMC report divergent Q1 earnings amid AI hardware growth, with Intel rebuilding and TSMC compounding. - Pluang](https://news.google.com/rss/articles/CBMihwFBVV95cUxONFMyWktuMTJTazBlVGZaTVZmd2tOS3dYb041MHhOSGJ4Y0ROX3pXUUw1c3J4bDU3YnNlTktFTnY5R3ZlUUpjeUZsTFZHNjAycmVfNnlyMDRxS2doYUc1RG5nS0taNWpsbUJjWERSWUZEU2d3dVYzcnROOWFjMVNrbDZhMWNiNXM?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 25 Jun 2026 17:29:38 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》收漲211點、續守10日線，日K連三黑- 新聞 - MoneyDJ；【台股操盤人筆記】在輪動與過熱中堅守優質AI部位 - MoneyDJ；個股動態報導內容-EF320823-B11B-4CF8-BDF5-6B67826F32DB - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》收漲211點、續守10日線，日K連三黑- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQUWNmTUcyczFDTEdiRXVnR3BEZUFVWTZiZWxVaTUxeWhCZnBjMm1JTnBpbUhlczFHOWxyMWVHZGh1RjlLMHNQX3hGQU9oTmJqMjNSTHJyOWoyWUhoSWp3Yk5heEE2aXh5VTZ6Y2FhSDVTQlY2cVhmMHN4Vi1mTDlFNFhVdTZDT0YzUm1YbnBpbnVyQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 25 Jun 2026 08:16:00 GMT
- [【台股操盤人筆記】在輪動與過熱中堅守優質AI部位 - MoneyDJ](https://news.google.com/rss/articles/CBMilwFBVV95cUxNaC1fVmI5cUQ0RlhsMzVnNl9Yel9FOG5ERkJ2MU9zY2hSSHFqbXRteFFQRFJ2eTZqNDVUOHhNeDI2RnRhWkhEYnc5Zk9nc1JXVmdiLUUycGg5MkY4cEhsbVZ0UGZOMHNWTDFnSEcxZ3hOOXUzNktXdXBLSjRxWHJKRjhydFFLUjJVbjlnQVVpNkdRa242WEtN?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 25 Jun 2026 02:49:00 GMT
- [個股動態報導內容-EF320823-B11B-4CF8-BDF5-6B67826F32DB - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxPTUlpbE9HODFKVXBBMW91TWg1WTBSNHlaOThQMUU0YVBfS3JDMXZKQ1VZYVR2WUF5cXNNcXByVWZsYjBJYlZDYTEtQmNrdnhXSV84X1o3Y3U2TnZXakdaOVh4TTVGOV9ZeEtCN2ZaZy1fdXlyS0t0QzJhZFoxaGoyOHVGVk5UMXRIZ2NLemRoSHRyV2FS?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 25 Jun 2026 11:29:59 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：外資三天賣超台股2,500億 法人預期季底部位平衡後再攻5萬點 - 經濟日報；台股高檔震盪 法人買超16檔「強恆強」個股 | 市場焦點 | 證券 - 經濟日報；台股 ETF 績效強強滾 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [外資三天賣超台股2,500億 法人預期季底部位平衡後再攻5萬點 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE51cmdFbjZDUWtfRGRaRkF0LUVXU1RjbGd5LVdJVE5HVTdGa0tyM0RndmRIN2phLWxBV1NLU0M4YnNlck1OeXA3cG0zUGF5Q3Z5aWxNQlJHNTRwd9IBX0FVX3lxTE4xS3JwUmdkY0hfTERjZHNOT3ZYMGZRMF9MU1FFeFVGLVh3OW9IS3NZa0xoMjhsaXRLbnJTRVJOZEJlSlh2THo3RGR2dGlESUZWaTNxWUM1YXhLRTNyZDdN?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 25 Jun 2026 17:15:36 GMT
- [台股高檔震盪 法人買超16檔「強恆強」個股 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMieEFVX3lxTFBpb3BVRGZBNVpYdTIwbjBQdUZfbWpRQVlfOWJvY0ROTXFzbi1rQVY3d0xIRjdwQlJnZUloQWZpVXNVc0paRVFrMGQxcnVGZ0pBU3hfRjVmY1o0dXdnemJTSVFVejdNUWM5OHBqYW1fTTJsSEZianpvQw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 25 Jun 2026 13:16:48 GMT
- [台股 ETF 績效強強滾 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxQdkJkZ2tpcS1DVmhRV2JpVnhEdGFMQVhBcjNIdG1JbFBJZmlYZ0habWVRMUdQd0NZMkRuQ2FWazFoY0h1bWxiaTJwT2RkWlFSMmt4bERoNlFnWnFLM1E2dXRsaFV5M01KLWxSXzI0VFpkUy10V1VPVW5OVU9kMExnTtIBX0FVX3lxTE81dm5zc29XODFBN2s0RGF6YUxScGVrc1piNjlRaUdlSHNXLXpXd0JwV2d5bzNqLWZlN2ZLLXdIX0VyU0xYa3AxR256WGdzTGxoT1NEeHRMT196SWNSc3Br?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 25 Jun 2026 17:54:22 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
