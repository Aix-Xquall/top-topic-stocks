# 每日股市熱門話題分析 - 2026-11-26

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **記憶體與 HBM 供應鏈**｜負向｜熱度 4｜市場確認 100.00｜同向 3/3
2. **綜合市場情緒**｜負向｜熱度 41｜市場確認 0.00｜同向 0/2
3. **AI 伺服器與資料中心**｜中性｜熱度 15｜市場確認 0.00｜同向 3/7
4. **半導體與晶片供應鏈**｜正向｜熱度 5｜市場確認 0.00｜同向 2/8
5. **利率與成長股估值**｜負向｜熱度 2｜市場確認 0.00｜同向 0/1

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.31（樣本 22）
- 5日相關係數：0.08（樣本 18）
- 同向比例：8/22

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 記憶體與 HBM 供應鏈 | 100.00 | 3/3 | 0 | +26.46% | +22.54% |
| 綜合市場情緒 | 0.00 | 0/2 | 2 | -8.15% | +4.32% |
| AI 伺服器與資料中心 | 0.00 | 3/7 | 4 | -13.95% | -3.85% |
| 半導體與晶片供應鏈 | 0.00 | 2/8 | 6 | -18.90% | -6.78% |
| 利率與成長股估值 | 0.00 | 0/1 | 1 | -7.50% | +1.15% |
| 關稅與供應鏈轉移 | 0.00 | 0/1 | 1 | -34.63% | -25.63% |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：SpaceX | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價呈負相關；應檢查正負向詞庫，並降低新聞直接提及但股價背離的權重。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-11-13 | -0.56 | 0.42 | +54.17% | 24 |
| 2026-11-14 | -0.34 | 0.12 | +42.11% | 19 |
| 2026-11-15 | -0.02 | 0.62 | +50.00% | 20 |
| 2026-11-16 | -0.30 | -0.27 | +38.89% | 18 |
| 2026-11-17 | 0.44 | 0.39 | +80.00% | 15 |
| 2026-11-18 | 0.27 | -0.38 | +86.36% | 22 |
| 2026-11-19 | 0.20 | -0.23 | +69.57% | 23 |
| 2026-11-20 | -0.35 | -0.36 | +69.23% | 13 |
| 2026-11-21 | 0.04 | 0.04 | +65.00% | 20 |
| 2026-11-22 | -0.11 | 0.38 | +70.83% | 24 |
| 2026-11-23 | 0.26 | -0.36 | 0.00% | 6 |
| 2026-11-24 | -0.41 | 0.30 | +3.70% | 27 |
| 2026-11-25 | 0.25 | 0.11 | +50.00% | 26 |
| 2026-11-26 | -0.31 | 0.08 | +36.36% | 22 |

## 歷史回測摘要

- 回測日期：2026-11-26
- 近5日 3日相關：-0.07
- 近5日 5日相關：-0.05
- 同向比例：+44.44%
- 權重狀態：未調整

- 方向準確度：+44.44%
- 信心排序準確度：-0.07
- 診斷：低相關

調整原因：近 5 日有效樣本 9 筆，低於 15 筆門檻，暫不調整權重。

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

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：Micron Falls 7% as a Weaker DRAM Outlook and New Tariffs Hit Memory Stocks; SanDisk Drops 7%: Are Micron and Memory Stocks Now a Value Play? - 24/7 Wall St.；Micron vs. Sandisk: Which AI Memory Stock Is the Better Buy? - Yahoo Finance；Micron Falls 7% as NVIDIA Pullback Partially Reverses Monday's AI Chip Rally; SanDisk and SK Hynix Drop 6% - 24/7 Wall St.

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | -0.65 | -38.08% | N/A | 601.25 | 971.00 | -38.08% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | -0.65 | -6.67% | -19.45% | 94.39 | 291.88 | -67.66% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | -0.49 | -34.63% | -25.63% | 149.30 | 228.38 | -34.63% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron、MU」，共 4 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：downgrade, falls, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 3 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。 方向判斷命中詞：falls, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：HBM。 方向判斷命中詞：falls, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Micron Falls 7% as a Weaker DRAM Outlook and New Tariffs Hit Memory Stocks; SanDisk Drops 7%: Are Micron and Memory Stocks Now a Value Play? - 24/7 Wall St.](https://news.google.com/rss/articles/CBMiiwJBVV95cUxPMHo3cGJWUUhPeEoxeTRsSTRvWldWNF9yUG9tbTlpR0Q4QW80S1g2cnJyUHMtZm1pM3h6QUxtLV9JMktCYXRicFltVUxfWFRXNWJxOGh0b283S1FlSkNBOWV0eDJpQUdxZWRfX0hXeHIwR3JROWt2N3ZFaUdJcGRDQ2QwLVBuMGlvVzVlWGtjUlJmRnA4b1JhTUNRMGRZRG16a01EUG9ZV0ROWkF0MFpoYldLWEZMeTl6TlJSMDVfZjV3dG9ndGFsb1Z0eEV0dm9QWFN6bVRiS2hlbzVhYndvbk5SeVluWnIySGxIeFdocDFqTDNYLWFRdXZXX1RXZmNONUFDSFljOFFnVW8?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 25 Nov 2026 14:13:00 GMT
- [Micron vs. Sandisk: Which AI Memory Stock Is the Better Buy? - Yahoo Finance](https://news.google.com/rss/articles/CBMilwFBVV95cUxQb3FMcEw4VGdDR2wxVTZlOXJuVU53MWlvQkw1Z3hqSnpqNWFINnBvaUhYQ1pUY3J3ellQSm9leF96SHFjaTBXYUZFLVJSTHAxdzR2VmRyM1hCUjR6SE1zZmQxc0U1dndyQTBCSmpWYTh6eXlDaDFnSkxqZllFRm5odHJIa1FGand5NEpHQzV2MDlSb2MzbVlz?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 24 Nov 2026 20:25:02 GMT
- [Micron Falls 7% as NVIDIA Pullback Partially Reverses Monday's AI Chip Rally; SanDisk and SK Hynix Drop 6% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi3wFBVV95cUxNMEhYd2YzdW9RLU5fRm1YYllkNjlZVlU0d3BKcXM1UzNXZkduWmZWMWlsTTR5WFVKX2RxdnNFSXd6RElyenpGYVBuanUza240SU9KM1lYQlo1dmdsNkNQeU1PVTNCbkhtRzF4XzFyc2xlcjh0OUd6aGNFelAyU3Y4a0FnRHl4S19nMGRYRklRSUtGeklHWXVkOEFITUhFUy13Q1ZzdnBCSXpMb19Vdmx1RFVPRjcxdDE4T2xaOGVlMjdaaW1tRDh4ODRHLVpxNzFxTG1IR09PZWhvakptRXlv?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 24 Nov 2026 14:07:00 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股開高強彈逾950點！聯發科扛多頭大旗、台積電卻陷震盪 - 經濟日報；台股近期劇烈震盪 增加流動性注意股標準擬放寬 最快年底前上路 - 經濟日報；美股逆轉收紅 台股衝過39000點 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | -0.24 | +7.50% | -1.15% | 2,145.00 | 2,480.00 | -13.51% | 背離 | 98.27 | 21.88 | 586.89B TWD / 59.71% | 2026-11-01 |
| 2454 聯發科 | 新聞直接提及 | -0.24 | +8.81% | -7.49% | 3,700.00 | 4,920.00 | -24.80% | 背離 | 62.35 | 58.63 | 55.03B TWD / 5.77% | 2026-11-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。
- 2454：新聞直接提及「聯發科」，共 1 篇新聞命中。

### 主要來源

- [台股開高強彈逾950點！聯發科扛多頭大旗、台積電卻陷震盪 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5TMlpDSGxmNm05N2k5cm1BUFBMVEZkWW41T3E4SmdWNDd1NTVTSmpFM25oY1VDeTZFR2N4VWxCNjRRV0RGaGhWNGJuZkJkM21SSDh4N0lLbGdWUdIBX0FVX3lxTE56cHVKT29OSjk5SFZjY0JpeWl4cEZxTE1udTdvRGttTFE5STFGVThnNklJX1liLXRhSnZKOEpHWUMyaDJjQ3BiVkpaY3MweFBxdVNwM1AtOXAxUEl6MGpR?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 25 Nov 2026 08:00:00 GMT
- [台股近期劇烈震盪 增加流動性注意股標準擬放寬 最快年底前上路 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE13NS1FdHp4N0M4V0UxalJyYmhGaVlRQm9WWTRXanF5OTJXYnJnYzdwa2ZoYVd6c2NLQzIzbmdDZ2NqTkRDNHBWeFNmRjR4X21kTXZPcGM3N0EwUdIBX0FVX3lxTE1paVRDSU91ZVFtSUFXZjNGTFdpSk9Hc2JVY1VDampMTVFGUGFqbmk1RGVkSjkxalVndXZnM3FRVmNkUW9uajlEWVgxQU1adjYySHc5T3R2aG5JcW1hZ1E4?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 25 Nov 2026 19:40:06 GMT
- [美股逆轉收紅 台股衝過39000點 - 經濟日報](https://news.google.com/rss/articles/CBMigAFBVV95cUxPS0JlTXJBb0RnTEUxLU9SYk1sWXprN19ZbTluZTBjcXRFNFM2WTUwV2FCSlpqMk94MUhCcmkxaXJlUl9UcHdDNUxrSFg2eGxMZ21FdTkxWV92QS0xdFdXT21Wc3FreExPMm5EX1JZTmdzMEJtNUZRZ0xpa0g4c1BmatIBX0FVX3lxTE4xaGFPQkVpQWk4WVd5dFltbUpVM3c1M3MzOGxIXzhuZHdpZ29XMkQ5bXRQMThNbXlvajM3QzI5ZTA5V21lbnVrZlE1MUhYczVtMjJLRWhJdzBCUEpQc0I4?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 26 Nov 2026 01:21:56 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：AI ASIC 動能強勁，花旗維持聯發科買進評等目標價 6,800 元 - TechNews 科技新報；路透：黃仁勳重掌輝達對 AI 信用市場減壓有限 - TechNews 科技新報；代理式 AI 需求攀升，對蘋果資料中心電力配置有何衝擊？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.31 | -34.63% | -25.63% | 149.30 | 228.38 | -34.63% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 新聞直接提及 | 0.00 | +13.95% | +27.52% | 355.58 | 355.58 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2454 聯發科 | 新聞直接提及 | +0.55 | +8.81% | -7.49% | 3,700.00 | 4,920.00 | -24.80% | 同向 | 62.35 | 58.63 | 55.03B TWD / 5.77% | 2026-11-01 |
| INTC 英特爾 | 產業/供應鏈推估 | +0.04 | -52.50% | +34.29% | 54.47 | 114.68 | -52.50% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | +0.03 | -21.33% | N/A | 406.03 | 516.10 | -21.33% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.06 | +7.50% | -1.15% | 2,150.00 | 2,480.00 | -13.31% | 同向 | 98.27 | 21.88 | 586.89B TWD / 59.71% | 2026-11-01 |
| MSFT 微軟 | 產業/供應鏈推估 | +0.04 | +8.82% | -0.42% | 489.93 | 507.29 | -3.42% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -14.33% | -22.71% | 300.86 | 446.77 | -32.66% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 同時符合主題標籤：AI, artificial intelligence, GPU, datacenter。 方向判斷命中詞：衝擊, 成長, 強勁。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AAPL：新聞直接提及「蘋果」，共 2 篇新聞命中。 方向判斷命中詞：衝擊, 成長。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2454：新聞直接提及「聯發科」，共 1 篇新聞命中。 同時符合主題標籤：AI。 方向判斷命中詞：衝擊, 成長, 強勁。

### 主要來源

- [AI ASIC 動能強勁，花旗維持聯發科買進評等目標價 6,800 元 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiqwFBVV95cUxNQ0l2dG9QNW9keGJybG1OclYtVDdUUURYRTFxUm5oMG9oOGtBQUJNT19xNjJlbUs4NWFQWlkyMjc4NWh1dThfTVNUTm8xU0pQMkxqbmkxTkM4eDNkeUp3c29xZ3YyT0hHZmtaTTlmOFNDZnF2Wm4yak5MbTRELUFRMVhHZzE3dmNrYWRVNDJhRU1wSHRUZU5oUjBTdF9CRHhreC1WRXFrcDhmTnM?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 26 Nov 2026 02:32:18 GMT
- [路透：黃仁勳重掌輝達對 AI 信用市場減壓有限 - TechNews 科技新報](https://news.google.com/rss/articles/CBMipAFBVV95cUxNNExUZnJKbnlPRWszLTFEc3RUbkxWdE1vc2haTU9QMW13dmhzVDlqbFR4ejFuVmQzSmZUMnFhOVhiQmZ4YndxMzVjbDlRaXlQZWwzLVRyTVBKWmJjbG5nY2dkTjgzUUdGQjZ0ejBTZDU0R0dpOHA4OUJBQTJ0LU84VEUxRnd2RW5pZlMxQzhyVnNzTWdwZER5UDAwbXI5QnU5VlQzdg?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 26 Nov 2026 00:21:29 GMT
- [代理式 AI 需求攀升，對蘋果資料中心電力配置有何衝擊？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMikwFBVV95cUxPWG8yX1lNNUhSS0ZQenhwNWpUTXNqbF9KRXdSeDVLWWdsVDlZQmlOZWllSVpjZm1XdXFtYVNhTURqY2xzVks0blNLcDdRVEx5dW9EbXlsM2lZT2U5b1RtZl92WkF3d3k0dkN6VWhQVFR5R3RsY2toaEhkWmNEdkhZQUFyeUt6NTBWbS0tSC03bmhCV0U?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 25 Nov 2026 23:50:58 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：Why Is Intel Stock Down Today? Shares Fall 8.1% to $54.83 as Chip Rally Cools After 16.3% Jump - Around Prague；Intel: Geopolitics And Foundry Improvements Offer Potent One-Two Punch (Rating Upgrade) - Seeking Alpha；美232調查中鄭麗君：半導體配額內已免稅、無人機全球最低| 政治 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.33 | -52.50% | +34.29% | 54.47 | 114.68 | -52.50% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.27 | -34.63% | -25.63% | 149.30 | 228.38 | -34.63% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | +0.05 | +7.50% | -1.15% | 2,150.00 | 2,480.00 | -13.31% | 同向 | 98.27 | 21.88 | 586.89B TWD / 59.71% | 2026-11-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.05 | +8.84% | -6.02% | 88.70 | 164.50 | -46.08% | 同向 | 6.80 | 12.91 | 25.20B TWD / 18.33% | 2026-11-01 |
| AMD 超微 | 產業/供應鏈推估 | +0.02 | -21.33% | N/A | 406.03 | 516.10 | -21.33% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | +0.02 | -38.08% | N/A | 601.25 | 971.00 | -38.08% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.02 | -6.67% | -19.45% | 94.39 | 291.88 | -67.66% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | +0.02 | -14.33% | -22.71% | 300.86 | 446.77 | -32.66% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。 方向判斷命中詞：fall, rally, upgrade。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip。 方向判斷命中詞：fall, rally。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 3 篇新聞出現相關標籤。 方向判斷命中詞：fall, rally, upgrade。

### 主要來源

- [Why Is Intel Stock Down Today? Shares Fall 8.1% to $54.83 as Chip Rally Cools After 16.3% Jump - Around Prague](https://news.google.com/rss/articles/CBMirgFBVV95cUxNQ1hzRkw4OWJpcE9GMHBjSFp0WV9KdlFKWC1ZY01nSmgxbkRrM2N2eGRBTVFBM21BNTRQNVdmcUljT0Y0dDNNc20zcDJjYTFPUExuQkItZ251ZENpQ3JIVDl4YmxYLS1INUREY2JFLTZVMnBEQlptYU5JWjJFTjd5S1lMbmFaWHQxeUF3UDFRSkE4QnQzbWxWMjh2X21fQ2lkOVg5WmpURDdzMmdWWHc?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 24 Nov 2026 17:11:07 GMT
- [Intel: Geopolitics And Foundry Improvements Offer Potent One-Two Punch (Rating Upgrade) - Seeking Alpha](https://news.google.com/rss/articles/CBMirwFBVV95cUxQNlJlVmxWYllZX3lZS1dZTTRnZFVWanVWWkhNWXlLb0Vrajg2S2ZIZEo1emVTTWpjc3BwTVd0c3RGeDRLU3BLcVFfVFBKZWliLTZlMHc4ZGxJQjVqTVBhUV9IdVhXellLU0NhTXRMSVFLSUZ6WVJ1V09oSzN1bXpCOGs4bWZRVUVZM2x1Nmp2YVhVSnE3Qmx4V1plcTNhdmoyS2Y1VjZsV1dDMXdqcFNF?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 24 Nov 2026 15:05:21 GMT
- [美232調查中鄭麗君：半導體配額內已免稅、無人機全球最低| 政治 - 中央社 CNA](https://news.google.com/rss/articles/CBMiX0FVX3lxTE8wbVNNNnlESEJIaU5FTENkSFotdnkxR0xWV2N1N2Z5UG5qTHRDSWZGZUhmZEgwTjFBZmNydXF5VTdLNGpab3V3YjExQm5uLVNZZkRaMDRwUGROQzgwcmdr?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 26 Nov 2026 03:07:00 GMT

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：〈美股早盤〉AI賣壓、通膨與關稅夾擊！那指跌逾4% 台積電ADR挫逾7% - 鉅亨網；德國2026年第三季GDP增長0.1%，較初估值小幅下修 作者 Investing.com - Investing.com 香港 - 股市報價& 財經新聞

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | -0.24 | +7.50% | -1.15% | 2,145.00 | 2,480.00 | -13.51% | 背離 | 98.27 | 21.88 | 586.89B TWD / 59.71% | 2026-11-01 |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +8.82% | -0.42% | 489.93 | 507.29 | -3.42% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [〈美股早盤〉AI賣壓、通膨與關稅夾擊！那指跌逾4% 台積電ADR挫逾7% - 鉅亨網](https://news.google.com/rss/articles/CBMiT0FVX3lxTE1CMzBWWF82cUZyN2NZLWh4dFVGd29LMzUxUFlROUdCcWhJSlIycTBUeWtZbVZvcVQ4UGxNdDdUTnV3bkxOUlg4SzZJR1BPVDg?oc=5) - Google News source discovery | 鉅亨網 Wed, 25 Nov 2026 14:44:38 GMT
- [德國2026年第三季GDP增長0.1%，較初估值小幅下修 作者 Investing.com - Investing.com 香港 - 股市報價& 財經新聞](https://news.google.com/rss/articles/CBMiekFVX3lxTE5Od2loQ2JyamtBTmNGWnI4REtZTktJQ2kyZ2FKbjc5YmV5dUstWF90MzdwYWRJQWxDT2NmRFZ1NHJVN2d6S3hhSk0yUkhkdGlJdDg4Ml9SMzBDelM2ZjA1cUlETkQzS2FHbjJERFFvREMtSHBPOEoyckl3?oc=5) - Google News source discovery | Investing.com Calendar Wed, 25 Nov 2026 09:35:51 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：《農產品》CBOT玉米、黃豆收高 關稅政策受矚-台股 - MoneyDJ；整理包／黃仁勳概念股笑了！輝達季度財報超預期 完整台廠供應鏈名單、潛在受惠股一次看 - 經濟日報；美國301關稅利空淡化 台股盤中勁揚逾1200點 - 中央社 CNA

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.24 | -34.63% | -25.63% | 149.30 | 228.38 | -34.63% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +13.95% | +27.52% | 355.58 | 355.58 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | -1.67% | -6.56% | 214.50 | 289.00 | -25.78% | 不適用 | 16.57 | 12.49 | 1305.32B TWD / 45.73% | 2026-11-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [《農產品》CBOT玉米、黃豆收高 關稅政策受矚-台股 - MoneyDJ](https://news.google.com/rss/articles/CBMiigFBVV95cUxPX1AzdGg5R1RHSV9FN083MzF0dFdVNzV3VG93M2dYbUh5REpKd0MxU0RHSnlKWExWcHp0OGVUdWdaZFdlQUVVSTdjam9DOEV4RDUzZVVodnlqVUtrS09TY1Z4TWNVVWpuWkZ4dkNxb0xsYlFuWU9NdXZLUzlpek52SFFVUVFfOW1SU2c?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 25 Nov 2026 23:26:23 GMT
- [整理包／黃仁勳概念股笑了！輝達季度財報超預期 完整台廠供應鏈名單、潛在受惠股一次看 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBQUlViSHpPeDVlY29yaHFNNE5NcVlUQnE3ZThTcXRGNHgxYTVPOVVTRDlaTDV6Zml5WEwxVHNSeGFDcnVHUHhRSW15SzNpU0dYVDU3dThWNEVCbkZI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Tue, 24 Nov 2026 08:00:00 GMT
- [美國301關稅利空淡化 台股盤中勁揚逾1200點 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE11dW11aFBFZGZMWUd4S0FpV21QZnh3cmFtSDl1enA3eHFNVjZoVEFKRGgwMm56NXRWaGE5RS1RcHBLNkp3bjNOZk12M1hHaXRuZXRYZVhmNkVfeEdTM3c?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 26 Nov 2026 03:14:00 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：台股ETF受益人連6周創高高息/市值型人氣相對旺- 新聞 - MoneyDJ；國票證券：台股短線仍需時間消化賣壓- 新聞 - MoneyDJ；惠譽:台股波動不致影響銀行/壽險穩定性券商恐受衝擊- 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股ETF受益人連6周創高高息/市值型人氣相對旺- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPRldpWE96VHhrcUlaT0FuRGdOZ2NmZHRON3d1UG1VMDVpaDZyTWFNX1pJbnVNV0lvQ0RSVDVQNnBGNXBtYThSUjdlTVd2V3ZSTVBYR1UybDNpMFJPV0xZNUJlZTZmVmVTUGJtWG01VXJpRnU5eER5V2QwZ0hJMWNmbHM2dW1Vb0s3U25HdzI5cGtyUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 25 Nov 2026 04:46:00 GMT
- [國票證券：台股短線仍需時間消化賣壓- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxOY0VrcnlJd0dnVWF2bGU0Qm1OZmt3cDJlVEZJcXpjME1jQUp0cGtieFFQc3B2YS1Wd3d0Q280dWJwWDk3RlBKS3JHLXVhT2ZuWmt1bzRaZHFSQXRadkhtZ0NmMHB0Zm1tZ1dvNWZBamVPUzM0UTBxZnd6VHhEbzVjRG1nZW56VVE1NGJWTFhwak9hdw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 26 Nov 2026 00:38:00 GMT
- [惠譽:台股波動不致影響銀行/壽險穩定性券商恐受衝擊- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxOcnJTTlpzQnU3R1ZLM21iYlZmck1ueERsVG9QSnVNb21reUlCSFEweXJMbkU4WHh4UkRwV1B0dnJPTGlHMzQ4bk5CdXp1QWM2NkY3Y0hTaDFwZl9SUXRkbFc1UG94NFN6UGVEck5wQWFLU2pGcndCVVdoeWJ0LXhsd2J0eV9QYW5LZ2tDYmxnajdIUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 26 Nov 2026 02:38:00 GMT

## 新興題材：SpaceX

摘要：新興題材：SpaceX 相關新聞集中在：SpaceX 百萬衛星獲放行！台股低軌衛星掀漲停潮「決勝點」是什麼？ - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [SpaceX 百萬衛星獲放行！台股低軌衛星掀漲停潮「決勝點」是什麼？ - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1XajVkYTlnVUVDT3pCaVVneU5xUmdJLVR4VWxGSkM3TkxjcmdYTngybW96NGhNZEJyejVlMnhtQ0hQdVdxOU1XREstUlVRelJWS29VQ3dyWVZPZ9IBX0FVX3lxTE9rVEN6SlhZRndLTDNzTGpqaDROenZXbXBFMjlxQWNHZkI1d2c2cHgxc2pWZ0Qtak5VcktpTENxUG5yNnFwZkNTN2wxQzhJRGl4a0huVW5XVTRyTkkwYVlz?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 25 Nov 2026 08:00:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
