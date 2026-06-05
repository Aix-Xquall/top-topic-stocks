# 每日股市熱門話題分析 - 2026-06-06

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜負向｜熱度 8｜市場確認 60.64｜同向 2/3
2. **新興題材：OpenAI**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
3. **散熱與液冷供應鏈**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0
4. **半導體與晶片供應鏈**｜中性｜熱度 7｜市場確認 N/A｜同向 0/0
5. **AI 伺服器與資料中心**｜正向｜熱度 18｜市場確認 20.07｜同向 2/6

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.12（樣本 11）
- 5日相關係數：0.06（樣本 11）
- 同向比例：5/11

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 60.64 | 2/3 | 1 | +4.66% | -9.49% |
| 新興題材：OpenAI | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 20.07 | 2/6 | 3 | -1.09% | +2.22% |
| 新興題材：TradingKey | 44.57 | 1/2 | 1 | +3.19% | -3.88% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-05-24 | -0.11 | 0.22 | +86.67% | 15 |
| 2026-05-25 | 0.40 | 0.33 | +50.00% | 10 |
| 2026-05-26 | -0.23 | -0.31 | +92.31% | 13 |
| 2026-05-27 | -0.07 | -0.07 | +87.50% | 8 |
| 2026-05-28 | 0.14 | -0.07 | +88.89% | 9 |
| 2026-05-29 | 0.14 | -0.04 | +71.43% | 7 |
| 2026-05-30 | 0.16 | -0.06 | +71.43% | 7 |
| 2026-05-31 | 0.96 | 0.09 | +100.00% | 3 |
| 2026-06-01 | -0.92 | -0.72 | +16.67% | 6 |
| 2026-06-02 | 0.08 | 0.05 | +72.73% | 11 |
| 2026-06-03 | 0.48 | 0.62 | +90.91% | 11 |
| 2026-06-04 | -0.38 | -0.30 | +85.71% | 7 |
| 2026-06-05 | 0.31 | 0.93 | +50.00% | 6 |
| 2026-06-06 | 0.12 | 0.06 | +45.45% | 11 |

## 歷史回測摘要

- 回測日期：2026-06-06
- 近5日 3日相關：0.14
- 近5日 5日相關：0.12
- 同向比例：+40.00%
- 權重狀態：已調整

- 方向準確度：+40.00%
- 信心排序準確度：0.14
- 診斷：弱正相關

調整原因：近 5 日方向與信心排序皆偏弱，降低方向詞與供應鏈推估權重，並加重背離扣分。；關鍵詞×公司後續樣本有效 4 筆，未達 30 筆，不調整樣本權重

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

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Intel and Micron Shares Plummet, What You Need To Know - StockStory；The Zacks Analyst Blog Highlights Micron, Sandisk, Seagate, Dell and Comfort Systems - The Globe and Mail；Market Rumors Nvidia Rubin Platform Plans to Reduce Memory Capacity, Storage Stocks Plunge Across the Board, SanDisk Falls Over 11%. - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | -0.72 | N/A | N/A | 864.01 | 996.00 | -13.25% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.72 | -9.15% | -8.00% | 1,559.32 | 1,831.50 | -14.86% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 新聞直接提及 | -0.62 | -7.59% | +20.71% | 385.73 | 446.77 | -13.66% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | -0.28 | +2.77% | +15.75% | 205.10 | 218.66 | -6.20% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | -0.53 | N/A | N/A | 99.17 | 114.68 | -13.52% | N/A | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、memory」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：falls, reduce。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：falls, reduce。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- AVGO：新聞直接提及「Broadcom」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel and Micron Shares Plummet, What You Need To Know - StockStory](https://news.google.com/rss/articles/CBMitgFBVV95cUxPYjhrdkN6RURRUGlRbDhQSGxyQndlVU5iWDdpdXo2bExIMk53U0ZicGM5OVB4bUJvd1NCZ0Z2ZGlGeHFxWXJZYWJBNkE3eUJZS0c1R016Tmh4eDRZRWI2alA5aDlMdV9GM25tamZqempfTmg1NUw1bG5EUURuNWxSd3R2LUgtcmM2LWdWbzRBQ2JwY1R2MExaZGRDMjZ1S0EtSHZ1WWltY1dGZjgxSzdkdjJBY0tLdw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 05 Jun 2026 16:30:31 GMT
- [The Zacks Analyst Blog Highlights Micron, Sandisk, Seagate, Dell and Comfort Systems - The Globe and Mail](https://news.google.com/rss/articles/CBMi-gFBVV95cUxQQjZRbFFvT3prZVZad2tiVmpsU1lBLXNsMGZhc0tVel9rc3JFZG5UbWV5Uld6a29HOXR5aGx1UnhPMURiV2M0ZGpLUU5TZHJGTjhrRmkzTjBFQnpocVkzRUpYUWJ0VUQtTkJjZ3h2Z0FwY1E5X2MxNUZpYU9uUlhzLXpzUEM1VFl6bG1lVmVnN3g3eVZvT29IOEVIcUNWZ29NcUhRX0ptYUE5dFUwMElaQkRQQ2YtZzFrUGwtM2NhX0FkdThpbXpSMVUxNXg4MDlHc0d0NDZncDdfLU5KajUxdWt3eTJ1WkhnOTJ1MGlxOUFldHU5VFJTNFR3?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 05 Jun 2026 09:42:51 GMT
- [Market Rumors Nvidia Rubin Platform Plans to Reduce Memory Capacity, Storage Stocks Plunge Across the Board, SanDisk Falls Over 11%. - TradingKey](https://news.google.com/rss/articles/CBMizAFBVV95cUxPMzkzNU02MkluY2lUUGtUc3QyaThEZjZ6QnJMb3QxOEFnNi1RN3lwNXZRWGdkVE1yTEt4Q0lnWThuQlB3U2tkVi1mQTFsWEVmUkhudEgwdk5OM1FfSmtHY0hVZWx1YjdKMWdHbE9sN2s3TXJsa1U3NV8taWNkOF9uNkJWY3paVjFoTXJyNGVENFV2UVh0ZjNnVU1hdk1DQVVjSWxCOXB0c1V0WWsyYU91SkwwRW9zQ2tTZlVmQjdtSm5JVzFaWW1pd2RNc0c?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 05 Jun 2026 19:46:22 GMT

## 新興題材：OpenAI

摘要：新興題材：OpenAI 相關新聞集中在：Trump administration, OpenAI discussing possible government stake in the AI startup - CNBC；Model routing is a fix for AI overspending. That's a problem for OpenAI and Anthropic - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 新聞直接提及 | 0.00 | +6.09% | -17.77% | 416.67 | 506.69 | -17.77% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：新聞直接提及「OpenAI」，共 2 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Trump administration, OpenAI discussing possible government stake in the AI startup - CNBC](https://news.google.com/rss/articles/CBMicEFVX3lxTE4ybHlVc085QUVIS2ZReHVWMVNPWTRhYmFuWVN1RXZVZUc0ZnZhbUlMT3Rpa1QxdEs3Q0Z6OG1qZ1VZN2N6TmlOMWlVYkVHc0dITjdkMnlTdnB2WmZZSkY4LW5HZHVRcjlKbDBoYVdva2_SAXZBVV95cUxObW91aGd3RmlfdHhHQVNLVUgyN3V6WDlFMkZ5UXdfbmZEQ0NfLW41REc4eTlMMkh1MlFiMW1BdFJmbm5sN1hOTVhwVl9VcXhlZzdVWFJyY1dkVFJQNFI2WXNTOXl1MllWa09KOHkxMkZsOXA4Qy1n?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 05 Jun 2026 17:58:46 GMT
- [Model routing is a fix for AI overspending. That's a problem for OpenAI and Anthropic - CNBC](https://news.google.com/rss/articles/CBMimgFBVV95cUxOM09LX2p4QkFZQ1FSTHc5c1hoQmlEcDQxVXpoTzhRQUVDMDNxMmc0cWo0bHZmeGtUM3ZFby1SZk5XWlBqZkRIdFotUDhHc0xhTmROM2Rrb1JTMnBqc3d1WG83LWxfVkYzUmZob0p3eUVCeFhoYWpkZ2FZYl80T3I0Y3gzM0FFaDFCYnhkUXJsU1c0WGRPOXlqcld30gGfAUFVX3lxTE5CRC1RQkRvRGlUc1VadzdQeHdKSFU5Ykl3MXZFel9yR0pBQ0lmWTl6VTFzaWZtOUlhNjk4RzhibnkwYjEtZnUyaURQSEFCLXZGUmxyX2J0WFVnMFhlalBMM3BiSVE1dnRXX1Z3QXQ5YmxhWExfaTRQNXgxcll5WXdpRHZ3WWxFMGIzLUNFOFFhUWJsTFJxMlhEQWZxX0xCUQ?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 05 Jun 2026 17:06:49 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：Computex 2026 散熱液冷商機爆發，奇鋐、雙鴻、台達電指標股全面迎戰AI 升級潮｜股市話題｜豐雲學堂2026 年 06 月 - sinotrade.com.tw；焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報；Cramer says 'cooling market' presents a chance to buy knocked-down AI stocks - CNBC

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | -3.70% | -2.44% | 2,600.00 | 2,835.00 | -8.29% | 不適用 | 61.06 | 42.72 | 15.63B TWD / 71.62% | 2026-05-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐、散熱」，共 2 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：跌停, 升級。

### 主要來源

- [Computex 2026 散熱液冷商機爆發，奇鋐、雙鴻、台達電指標股全面迎戰AI 升級潮｜股市話題｜豐雲學堂2026 年 06 月 - sinotrade.com.tw](https://news.google.com/rss/articles/CBMi9gNBVV95cUxOaE1JYWkyUGQ0QjBMdFRNX3JnektMSXp2UnFDbXlBY0Y5MHo5VWZfdW5Oc0xnWUJMdno3a3FIV2xTVkNWelpBNHItWWtuNGdvTXZFLUhaZy1FOTIyQVZQNHRzLWZqYUhqenBEOURzNHFiM2dIQ2xzVU5DZ1NiVTFJQVVaWXppMHdkUC1hSHRuS3dIdzZCdUl4eG5ZN0l2WDlSdXdQaE1SaTJUYTFsTk9KbTVFSGY3NkdsNkJLRzd0OC04eUNGWDVNVDBtUFVobVZXYlY1N0dhd2VQQXVDa3hvZFk3TXBSRGVVY1RwN2ZldFY2b19BcGRkbjV0WG9KVk9yLWozM1JnYVdhMnRSeG9lTVlkMnVPamhMVGF5RUxPUGZpMDFLWjR6NDQtVU8yTTRzQXQ1MGV5OHNyalZtTno1a2plWWp4WjhteEtCb2Z2Rm00S01UdThhaVk4S1ItbWFMTUx2Yy1vYmFhVy1UbHJlbEhmXzhUd09ra2N2ZHIzOGszVkJuYWg2b1FZMzFjZnVvNXBOeGY3MzU4UllCT3RXUE9fdEgzcDR5dHFxS2I4UjNrQUh0dzVqR2tGVnprLUVVZ25uZWx5Y25XMjBsU2E4djJ0RmU5UU11S1c3clE0QzdNM2ZHUEF1MGtkN3RnWVBFb3FvcFJR?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 05 Jun 2026 17:07:01 GMT
- [焦點股》健策：AI散熱賣壓沉重 再探跌停 - 自由時報](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBBdkF6TUhSZzVQMG9EeVZ5T1A1a0VHU0x5SDU3SEpyMkxINHBEZEQ1YmRKcGFESFA4TGhiY1BvUWV6VEVRcjZDWG8xZDRJckJ5eUt2NTNVemI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 05 Jun 2026 02:50:31 GMT
- [Cramer says 'cooling market' presents a chance to buy knocked-down AI stocks - CNBC](https://news.google.com/rss/articles/CBMipwFBVV95cUxQV1lyT3hnRFNCbEFyNU9CUnhKLXFOd3FfRnNFbDdQR3gxMGNWV3ZLcFNVb0NsaEVEZWNhSmZUdXZVcmlsUldLcVNubFg2d1JxLUMwNVpnTXlacmxOY091cWVVMWlOYjByWE1KTjUxNnVWd2lKcHJxY09IdTVZbzVreXFzakg3ZVlfLVY3S2xPTnZSN3NlN3RoNnFGc0tDajlOckNuUDZFNA?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 05 Jun 2026 16:44:30 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Broadcom Sinks 14% on Soft AI Chip Outlook Despite Earnings Beat, Dragging Down AMD and Intel - 24/7 Wall St.；Broadcom's Stock Sinks Despite Solid Earnings. Other Chip Stocks Are Sliding Too. - Investopedia；Broadcom Stock Tumbles After AI Chip Forecast Disappoints - Gotrade

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AVGO 博通 | 新聞直接提及 | 0.00 | -7.59% | +20.71% | 385.73 | 446.77 | -13.66% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | 0.00 | N/A | N/A | 99.17 | 114.68 | -13.52% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | N/A | N/A | 466.38 | 523.20 | -10.86% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -0.63% | +0.42% | 2,365.00 | 2,385.00 | -0.84% | 不適用 | 74.39 | 31.80 | 410.73B TWD / 17.50% | 2026-05-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | -7.07% | -9.00% | 131.50 | 144.50 | -9.00% | 不適用 | 4.00 | 33.04 | 22.94B TWD / 17.78% | 2026-06-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +2.77% | +15.75% | 205.10 | 218.66 | -6.20% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | N/A | N/A | 864.01 | 996.00 | -13.25% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -9.15% | -8.00% | 1,559.32 | 1,831.50 | -14.86% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- AVGO：新聞直接提及「Broadcom」，共 3 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Broadcom Sinks 14% on Soft AI Chip Outlook Despite Earnings Beat, Dragging Down AMD and Intel - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi0AFBVV95cUxPdmRfWUZwQWcxUXprS1BlRjFpUTJ0QVVpTF95d19SY1BpRWxCNXBwcEVJMVpaSHVqX0JtVmdIajN1SzZZd1FIdnNETWVQWUViX01oY1hicEhUd0VDZExVVzA2cDRqcm5yaWkwX2ZOTHhfUkNfaWtFZENHbDd5Zm5TRjltY0NzVUllcXItaG84MF83c2twaHVFbGE1a3R2NnpROXJnQWdGZ2dJZTBfRkxXNEdwb1EyNkxrM0pzZFBfa2JNcVBGckRzM01UVlJkTmpX?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 04 Jun 2026 13:24:25 GMT
- [Broadcom's Stock Sinks Despite Solid Earnings. Other Chip Stocks Are Sliding Too. - Investopedia](https://news.google.com/rss/articles/CBMisgFBVV95cUxOaEphSDRQOFVSdktVSjVmS1doUWt0TjRnVUg1WXBoR2l2ZUgwTXlVZGw5dzRVU2FXQm82VnY1ZHVCU09Da24xSDlvR3NTcF90cmtDZ1hrLVJGOXZCcWdsak1VV3Rwc2pBOGZKSGQyRXJ1a2kzYmZDbENDWFVYMUE1QWRqeFRjY0JQbm5LVlVDUkdDUnZpWGNxTGxKUEliT2tBRHdYLXpSVXI2UEVoNG5CcHdR?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 04 Jun 2026 14:57:38 GMT
- [Broadcom Stock Tumbles After AI Chip Forecast Disappoints - Gotrade](https://news.google.com/rss/articles/CBMikAFBVV95cUxNQ1otdFFpWTdlXzFkazZCSjZUdmhrRzR1ZXRDTTZ5Y1ZzRmRCUTd1cXlqR0FKZjg3Yk9GOFpjZ3owc3dxSkc3OHVZRzV2Q2lqODhuQlRtLXNlbU9ZdFJrdHRLTnhpX1JBVm9kTUk4X2JqYi1NWU1tNkZoc3dEYXg5Mm5tX2FXdXc1MDZfZDVwRTk?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 04 Jun 2026 03:15:43 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Broadcom Sinks 14% on Soft AI Chip Outlook Despite Earnings Beat, Dragging Down AMD and Intel - 24/7 Wall St.；Broadcom Stock Tumbles After AI Chip Forecast Disappoints - Gotrade；Buy These 5 Growth Stocks in June Amid Massive AI Infrastructure Boost - TradingView

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AVGO 博通 | 新聞直接提及 | +0.36 | -7.59% | +20.71% | 385.73 | 446.77 | -13.66% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | +0.69 | N/A | N/A | 99.17 | 114.68 | -13.52% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.67 | N/A | N/A | 466.38 | 523.20 | -10.86% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | +0.07 | +2.77% | +15.75% | 205.10 | 218.66 | -6.20% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.05 | -0.63% | +0.42% | 2,365.00 | 2,385.00 | -0.84% | 未明確 | 74.39 | 31.80 | 410.73B TWD / 17.50% | 2026-05-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.05 | +6.09% | -17.77% | 416.67 | 506.69 | -17.77% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | +0.03 | -2.20% | -5.56% | 577.00 | 611.00 | -5.56% | 背離 | 10.86 | 53.57 | 62.25B TWD / 19.22% | 2026-05-01 |
| 2454 聯發科 | 產業/供應鏈推估 | +0.03 | -4.97% | -0.23% | 4,300.00 | 4,430.00 | -2.93% | 背離 | 62.91 | 68.53 | 46.74B TWD / -4.14% | 2026-05-01 |

關聯理由（前 3）：
- AVGO：新聞直接提及「Broadcom」，共 2 篇新聞命中。 同時符合主題標籤：AI, datacenter。 方向判斷命中詞：boost, growth, 成長。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：boost, growth, 成長。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。 方向判斷命中詞：boost, growth, 成長。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Broadcom Sinks 14% on Soft AI Chip Outlook Despite Earnings Beat, Dragging Down AMD and Intel - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi0AFBVV95cUxPdmRfWUZwQWcxUXprS1BlRjFpUTJ0QVVpTF95d19SY1BpRWxCNXBwcEVJMVpaSHVqX0JtVmdIajN1SzZZd1FIdnNETWVQWUViX01oY1hicEhUd0VDZExVVzA2cDRqcm5yaWkwX2ZOTHhfUkNfaWtFZENHbDd5Zm5TRjltY0NzVUllcXItaG84MF83c2twaHVFbGE1a3R2NnpROXJnQWdGZ2dJZTBfRkxXNEdwb1EyNkxrM0pzZFBfa2JNcVBGckRzM01UVlJkTmpX?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 04 Jun 2026 13:24:25 GMT
- [Broadcom Stock Tumbles After AI Chip Forecast Disappoints - Gotrade](https://news.google.com/rss/articles/CBMikAFBVV95cUxNQ1otdFFpWTdlXzFkazZCSjZUdmhrRzR1ZXRDTTZ5Y1ZzRmRCUTd1cXlqR0FKZjg3Yk9GOFpjZ3owc3dxSkc3OHVZRzV2Q2lqODhuQlRtLXNlbU9ZdFJrdHRLTnhpX1JBVm9kTUk4X2JqYi1NWU1tNkZoc3dEYXg5Mm5tX2FXdXc1MDZfZDVwRTk?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 04 Jun 2026 03:15:43 GMT
- [Buy These 5 Growth Stocks in June Amid Massive AI Infrastructure Boost - TradingView](https://news.google.com/rss/articles/CBMixAFBVV95cUxOZ0pFVXhOYTJsVXdyekhDUXhVb1Rzd0hmamJVRWY1MXROYTVXVUZGMFVlTmZ2Tmc0Q2V4WHc1Y3dyb0dkNUVBbkVXZ3NYRVJoS0hfQzd5V1lvc3VBTThLbmFxdnR1ZXNZZ3lUSno3am5Fbjh4Y3lHc2lpeExXZzZWLXBKREd6dDJRTmRCVjRiOV9XRFViaDN4YlFLRWVfZ0dpa0F6S1NyMkZ0RzFhaER1ZmNva20xSWdXSnVsaklLRU81bEtp?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 04 Jun 2026 12:48:00 GMT

## 新興題材：TradingKey

摘要：新興題材：TradingKey 相關新聞集中在：Intel Corp Stock (INTC) Moved Down by 6.80% on Jun 5: What Investors Need To Know - TradingKey；Market Rumors Nvidia Rubin Platform Plans to Reduce Memory Capacity, Storage Stocks Plunge Across the Board, SanDisk Falls Over 11%. - TradingKey

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | -0.27 | +2.77% | +15.75% | 205.10 | 218.66 | -6.20% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 新聞直接提及 | -0.53 | N/A | N/A | 99.17 | 114.68 | -13.52% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 新聞直接提及 | -0.53 | N/A | N/A | 864.01 | 996.00 | -13.25% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.53 | -9.15% | -8.00% | 1,559.32 | 1,831.50 | -14.86% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 方向判斷命中詞：falls, reduce。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：新聞直接提及「INTC」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MU：新聞直接提及「memory」，共 1 篇新聞命中。 方向判斷命中詞：falls, reduce。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Intel Corp Stock (INTC) Moved Down by 6.80% on Jun 5: What Investors Need To Know - TradingKey](https://news.google.com/rss/articles/CBMiiwFBVV95cUxNM3lvb2NYZHZwdmg1M09iZW1tQm9ab2NGU0Y2bkwyREY1ZFdlSENXOHg4dzRkRGM4V0JyY3dMQXVKTEZMS1h3SEpvOXh3eDBHUDlic0t5amxvdFlaeDgyalZrRHJTblZWQmdlUXpJeHc5ZEVGcFZOcGlRdDZadFB3OVJ0Q2FnVG5XOGpv?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 05 Jun 2026 14:15:19 GMT
- [Market Rumors Nvidia Rubin Platform Plans to Reduce Memory Capacity, Storage Stocks Plunge Across the Board, SanDisk Falls Over 11%. - TradingKey](https://news.google.com/rss/articles/CBMizAFBVV95cUxPMzkzNU02MkluY2lUUGtUc3QyaThEZjZ6QnJMb3QxOEFnNi1RN3lwNXZRWGdkVE1yTEt4Q0lnWThuQlB3U2tkVi1mQTFsWEVmUkhudEgwdk5OM1FfSmtHY0hVZWx1YjdKMWdHbE9sN2s3TXJsa1U3NV8taWNkOF9uNkJWY3paVjFoTXJyNGVENFV2UVh0ZjNnVU1hdk1DQVVjSWxCOXB0c1V0WWsyYU91SkwwRW9zQ2tTZlVmQjdtSm5JVzFaWW1pd2RNc0c?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Fri, 05 Jun 2026 19:46:22 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：個股動態報導內容-579DC683-21EE-4EFF-8D05-C312A53FE1B1 - MoneyDJ理財網；個股動態報導內容-98637DE8-43BC-42C7-BFF4-F127B2FC6476 - MoneyDJ理財網；個股動態報導內容-190CA88F-AFE7-4F4E-BA8C-D8DF30ECE993 - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-579DC683-21EE-4EFF-8D05-C312A53FE1B1 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilAFBVV95cUxPbmlFdkk3YVlmdm5CVGRTak55bHg3aUJYNHQ0Wl9KVWx2STNuQ25YTkFnQXNXTXNmYnJPTC1jWGtoRzlhSFpvdTZBb05qYmI4VGtxSktEaW85UlE1LWVwcDlQMHhqN0h0Wmh0RXVBdjd4Q2s0YmxVZUdjS0JpbGtISHZEWjF6ejJaZmE4cVpyVVBQLWJj?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 05 Jun 2026 20:34:18 GMT
- [個股動態報導內容-98637DE8-43BC-42C7-BFF4-F127B2FC6476 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilAFBVV95cUxQdWs1Y2pxMGRjZjdoMWF0cGxmVEVPWVBxQmRSMlJoaVlOTno0NFlsMkp1Qm1jVVF1R1ptZzNDMkVRX1lwWkFPXzllSXhzWUFFTWhrb0VMNWoxWjB3ZFhLeE1OdFFFZ0ZBX1ZfMGpVX1lyaEdNNnl2cWRrR2xxMDhYeDNuWERaODhtNkZTUnVoZzJ3YXR0?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 05 Jun 2026 12:34:46 GMT
- [個股動態報導內容-190CA88F-AFE7-4F4E-BA8C-D8DF30ECE993 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMilAFBVV95cUxPNmJ3RjNXQVZkTE5oVWRMV1lqZ182Q2FZMFY5d0JCbjB6YW15RnUxMGx0S0xFNEFzemFOZTlGcHJ1M2pzR2lUaER5TDd0VS1yU2dTWDhiMjJIV0R3eUlmbkhkN0lDOFlvMGY2TXZ3OWgyVmhwSHdack1yN1Ywdy1XVWN0SWwwU1JSUlpGOHB3dlR4Zmtt?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 05 Jun 2026 03:46:12 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：《台股盤後》收跌606點、10日線失而復得；周K連三紅-新聞內容-基金 - MoneyDJ；美元指數反彈/台股重挫 台幣早盤貶值4分 - MoneyDJ；統一證券：台股短線估高檔震盪- 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》收跌606點、10日線失而復得；周K連三紅-新聞內容-基金 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxOd2RrT1RDNVJiOXQwYnFvOU9Tc1Jad21nQk5pN2V2M2RhbnNjNzFWTDZGYzZoQWhXX2Z3QkJqdHdJWGVFN0hLTkpZOFVBdktLRzhUbk84Wm94cUFuZVVRa1FEdTFXd1hNbk1IQWk3RE1vb3BsbEZncW1SRml0SWlNTEdxVzQ5UnpQa0VIa1VUeHQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 05 Jun 2026 08:09:00 GMT
- [美元指數反彈/台股重挫 台幣早盤貶值4分 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNY3I2RVBLSnYzalc4TGpkUXRzSWtjdXNiZDBnaHN3Rmtmc3cxOS1PaE81U2hDTlFtenhtb3N6M0U1cnFCN3NiSHBzMW5fMVFaeUU0MnZ4TkR2cTVOUzNKSkVJdzR6OUNzQVJfZ01sQWl5V3NNSHVkUFR1MVBTb3JyZ3FEcGxobXVxSUZpTDZJN3NJQQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 05 Jun 2026 04:56:00 GMT
- [統一證券：台股短線估高檔震盪- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPZWozTkd1THVuczdxWGFFdEZBcnR1dlJucHVRTnZic3pCaHZ1MFdYWVFWUnp0alc5ZWNSQTBfSzlIYUpiSGJ2ZHZpc28tbk5xMzFCSzBLTW5uQXNRbTFMWUJLZXB1V1B6dzZVamRfN0NCVXdMang2dnFCYUtGQzBMNEhoQ1hyWnA0UjVoWm81cVVWdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 05 Jun 2026 00:48:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
