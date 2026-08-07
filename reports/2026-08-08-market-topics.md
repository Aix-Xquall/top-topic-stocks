# 每日股市熱門話題分析 - 2026-08-08

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **電動車與電池**｜負向｜熱度 1｜市場確認 100.00｜同向 1/1
2. **關稅與供應鏈轉移**｜正向｜熱度 2｜市場確認 71.07｜同向 3/4
3. **利率與成長股估值**｜正向｜熱度 1｜市場確認 N/A｜同向 0/0
4. **先進封裝與 CoPoS**｜正向｜熱度 2｜市場確認 60.76｜同向 2/3
5. **消費電子與手機**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.72（樣本 16）
- 5日相關係數：0.45（樣本 16）
- 同向比例：10/16

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 電動車與電池 | 100.00 | 1/1 | 0 | +21.88% | +13.90% |
| 關稅與供應鏈轉移 | 71.07 | 3/4 | 0 | +6.19% | +10.47% |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 先進封裝與 CoPoS | 60.76 | 2/3 | 0 | +4.70% | +5.12% |
| 消費電子與手機 | N/A | 0/0 | 0 | N/A | N/A |
| 記憶體與 HBM 供應鏈 | 34.25 | 2/4 | 1 | -0.25% | +3.79% |
| 新興題材：股半導體族群受惠先進封裝 | 38.24 | 1/2 | 0 | +1.08% | +1.57% |
| 新興題材：晶片需求 | 38.24 | 1/2 | 0 | +1.08% | +1.57% |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-07-26 | 0.38 | 0.06 | +23.53% | 17 |
| 2026-07-27 | 0.54 | 0.11 | +37.50% | 8 |
| 2026-07-28 | 0.32 | 0.13 | +36.36% | 11 |
| 2026-07-29 | 0.16 | -0.03 | +92.31% | 13 |
| 2026-07-30 | 0.25 | 0.92 | +66.67% | 6 |
| 2026-07-31 | 0.10 | -0.10 | +46.15% | 13 |
| 2026-08-01 | 0.38 | 0.25 | +54.55% | 11 |
| 2026-08-02 | 0.06 | -0.21 | +33.33% | 9 |
| 2026-08-03 | 0.35 | -0.49 | +60.00% | 5 |
| 2026-08-04 | 0.05 | -0.08 | +46.15% | 13 |
| 2026-08-05 | -0.39 | 0.44 | +64.29% | 14 |
| 2026-08-06 | 0.07 | 0.33 | +50.00% | 12 |
| 2026-08-07 | -0.22 | -0.17 | +50.00% | 8 |
| 2026-08-08 | 0.72 | 0.45 | +62.50% | 16 |

## 歷史回測摘要

- 回測日期：2026-08-08
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

## 電動車與電池

摘要：電動車與電池 相關新聞集中在：EV competition and battery pricing put Tesla and power semiconductor suppliers in focus

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| TSLA 特斯拉 | 新聞直接提及 | -0.49 | -21.88% | -13.90% | 328.58 | 456.56 | -28.03% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- TSLA：新聞直接提及「Tesla」，共 1 篇新聞命中。 同時符合主題標籤：EV, electric vehicle, battery, autonomous driving。 方向判斷命中詞：pressure。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [EV competition and battery pricing put Tesla and power semiconductor suppliers in focus](https://example.com/sample/ev-battery) - sample 2026-05-07T04:00:00Z

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：台股半導體族群受惠先進封裝與 AI 晶片需求，台積電、日月光與記憶體相關個股受關注；Tariff uncertainty pressures Apple hardware supply chain while investors watch Taiwan exporters

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AAPL 蘋果 | 新聞直接提及 | +0.46 | +18.60% | +34.97% | 313.33 | 313.33 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | +0.42 | +2.16% | -2.27% | 2,370.00 | 2,425.00 | -2.27% | 同向 | 74.39 | 31.86 | 442.68B TWD / 67.87% | 2026-07-01 |
| 3711 日月光投控 | 新聞直接提及 | +0.32 | 0.00% | +5.41% | 585.00 | 680.00 | -13.97% | 未明確 | 10.86 | 54.32 | 65.78B TWD / 32.86% | 2026-07-01 |
| 2317 鴻海 | 產業/供應鏈推估 | +0.08 | +4.00% | +3.79% | 260.00 | 289.00 | -10.03% | 同向 | 14.13 | 18.47 | 946.51B TWD / 54.19% | 2026-08-01 |

關聯理由（前 3）：
- AAPL：新聞直接提及「Apple」，共 1 篇新聞命中。 同時符合主題標籤：tariff, supply chain。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 方向判斷命中詞：受惠。
- 3711：新聞直接提及「日月光」，共 1 篇新聞命中。 方向判斷命中詞：受惠。

### 主要來源

- [台股半導體族群受惠先進封裝與 AI 晶片需求，台積電、日月光與記憶體相關個股受關注](https://example.com/sample/tw-semiconductor) - sample 2026-05-07T07:00:00+08:00
- [Tariff uncertainty pressures Apple hardware supply chain while investors watch Taiwan exporters](https://example.com/sample/tariff-apple) - sample 2026-05-07T05:30:00Z

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：降息預期升溫，美股科技股與高本益比成長股估值重新受到討論

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +27.31% | -1.32% | 499.99 | 506.69 | -1.32% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [降息預期升溫，美股科技股與高本益比成長股估值重新受到討論](https://example.com/sample/rate-cut-tech) - sample 2026-05-07T08:00:00+08:00

## 先進封裝與 CoPoS

摘要：先進封裝與 CoPoS 相關新聞集中在：AI server demand lifts Nvidia, TSMC and memory chip suppliers as datacenter spending rises；台股半導體族群受惠先進封裝與 AI 晶片需求，台積電、日月光與記憶體相關個股受關注

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | +0.57 | +2.16% | -2.27% | 2,370.00 | 2,425.00 | -2.27% | 同向 | 74.39 | 31.86 | 442.68B TWD / 67.87% | 2026-07-01 |
| 3711 日月光投控 | 新聞直接提及 | +0.36 | 0.00% | +5.41% | 585.00 | 680.00 | -13.97% | 未明確 | 10.86 | 54.32 | 65.78B TWD / 32.86% | 2026-07-01 |
| NVDA 輝達 | 新聞直接提及 | +0.42 | +11.93% | +12.22% | 223.96 | 223.96 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 新聞直接提及 | +0.42 | N/A | N/A | 877.57 | 971.00 | -9.62% | N/A | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 2330：新聞直接提及「TSMC、台積電」，共 2 篇新聞命中。 同時符合主題標籤：advanced packaging, CoWoS, CoPoS, FOPLP。 方向判斷命中詞：受惠。
- 3711：新聞直接提及「日月光」，共 1 篇新聞命中。 同時符合主題標籤：advanced packaging, CoPoS, FOPLP, panel-level packaging。 方向判斷命中詞：受惠。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AI server demand lifts Nvidia, TSMC and memory chip suppliers as datacenter spending rises](https://example.com/sample/ai-server-demand) - sample 2026-05-07T06:00:00Z
- [台股半導體族群受惠先進封裝與 AI 晶片需求，台積電、日月光與記憶體相關個股受關注](https://example.com/sample/tw-semiconductor) - sample 2026-05-07T07:00:00+08:00

## 消費電子與手機

摘要：消費電子與手機 相關新聞集中在：Tariff uncertainty pressures Apple hardware supply chain while investors watch Taiwan exporters

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AAPL 蘋果 | 新聞直接提及 | 0.00 | +18.60% | +34.97% | 313.33 | 313.33 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | +4.00% | +3.79% | 260.00 | 289.00 | -10.03% | 不適用 | 14.13 | 18.47 | 946.51B TWD / 54.19% | 2026-08-01 |
| 2454 聯發科 | 產業/供應鏈推估 | 0.00 | +0.91% | +9.70% | 3,900.00 | 4,310.00 | -9.51% | 不適用 | 60.69 | 64.41 | 58.01B TWD / 2.80% | 2026-07-01 |

關聯理由（前 3）：
- AAPL：新聞直接提及「Apple」，共 1 篇新聞命中。 同時符合主題標籤：hardware, consumer electronics, smartphone。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「消費電子與手機」關鍵字 hardware, consumer electronics；其中 1 篇新聞出現相關標籤。
- 2454：產業/供應鏈推估：公司標籤符合「消費電子與手機」關鍵字 smartphone；其中 0 篇新聞出現相關標籤。

### 主要來源

- [Tariff uncertainty pressures Apple hardware supply chain while investors watch Taiwan exporters](https://example.com/sample/tariff-apple) - sample 2026-05-07T05:30:00Z

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：AI server demand lifts Nvidia, TSMC and memory chip suppliers as datacenter spending rises；台股半導體族群受惠先進封裝與 AI 晶片需求，台積電、日月光與記憶體相關個股受關注

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.44 | N/A | N/A | 877.57 | 971.00 | -9.62% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | +0.42 | +2.16% | -2.27% | 2,370.00 | 2,425.00 | -2.27% | 同向 | 74.39 | 31.86 | 442.68B TWD / 67.87% | 2026-07-01 |
| NVDA 輝達 | 新聞直接提及 | +0.39 | +11.93% | +12.22% | 223.96 | 223.96 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 新聞直接提及 | +0.27 | 0.00% | +5.41% | 585.00 | 680.00 | -13.97% | 未明確 | 10.86 | 54.32 | 65.78B TWD / 32.86% | 2026-07-01 |
| SNDK SanDisk | 產業/供應鏈推估 | +0.06 | -15.09% | -0.22% | 1,212.21 | 2,335.00 | -48.09% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「memory」，共 1 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「TSMC、台積電」，共 2 篇新聞命中。 方向判斷命中詞：受惠。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：HBM。 方向判斷命中詞：受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AI server demand lifts Nvidia, TSMC and memory chip suppliers as datacenter spending rises](https://example.com/sample/ai-server-demand) - sample 2026-05-07T06:00:00Z
- [台股半導體族群受惠先進封裝與 AI 晶片需求，台積電、日月光與記憶體相關個股受關注](https://example.com/sample/tw-semiconductor) - sample 2026-05-07T07:00:00+08:00

## 新興題材：股半導體族群受惠先進封裝

摘要：新興題材：股半導體族群受惠先進封裝 相關新聞集中在：台股半導體族群受惠先進封裝與 AI 晶片需求，台積電、日月光與記憶體相關個股受關注

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | +0.42 | +2.16% | -2.27% | 2,370.00 | 2,425.00 | -2.27% | 同向 | 74.39 | 31.86 | 442.68B TWD / 67.87% | 2026-07-01 |
| 3711 日月光投控 | 新聞直接提及 | +0.32 | 0.00% | +5.41% | 585.00 | 680.00 | -13.97% | 未明確 | 10.86 | 54.32 | 65.78B TWD / 32.86% | 2026-07-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 方向判斷命中詞：受惠。
- 3711：新聞直接提及「日月光」，共 1 篇新聞命中。 方向判斷命中詞：受惠。

### 主要來源

- [台股半導體族群受惠先進封裝與 AI 晶片需求，台積電、日月光與記憶體相關個股受關注](https://example.com/sample/tw-semiconductor) - sample 2026-05-07T07:00:00+08:00

## 新興題材：晶片需求

摘要：新興題材：晶片需求 相關新聞集中在：台股半導體族群受惠先進封裝與 AI 晶片需求，台積電、日月光與記憶體相關個股受關注

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | +0.42 | +2.16% | -2.27% | 2,370.00 | 2,425.00 | -2.27% | 同向 | 74.39 | 31.86 | 442.68B TWD / 67.87% | 2026-07-01 |
| 3711 日月光投控 | 新聞直接提及 | +0.32 | 0.00% | +5.41% | 585.00 | 680.00 | -13.97% | 未明確 | 10.86 | 54.32 | 65.78B TWD / 32.86% | 2026-07-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 方向判斷命中詞：受惠。
- 3711：新聞直接提及「日月光」，共 1 篇新聞命中。 方向判斷命中詞：受惠。

### 主要來源

- [台股半導體族群受惠先進封裝與 AI 晶片需求，台積電、日月光與記憶體相關個股受關注](https://example.com/sample/tw-semiconductor) - sample 2026-05-07T07:00:00+08:00

## 資料缺口與需人工確認

- Google News 財經來源抓取失敗：site:cna.com.tw 財經 OR 證券 OR 台股 OR 半導體 OR 公司，原因：HTTP Error 503: Service Unavailable
- Google News 財經來源抓取失敗：site:cnbc.com markets OR stocks OR earnings OR semiconductor OR AI，原因：HTTP Error 503: Service Unavailable
- Google News 財經來源抓取失敗：site:ctee.com.tw 台股 OR 個股 OR 產業 OR 半導體 OR 法人，原因：HTTP Error 503: Service Unavailable
- Google News 財經來源抓取失敗：site:investing.com economic calendar OR CPI OR rate decision OR PMI OR GDP，原因：HTTP Error 503: Service Unavailable
- Google News 財經來源抓取失敗：site:money.udn.com 證券 OR 台股 OR 個股 OR 美股 OR 半導體 OR 財報，原因：HTTP Error 503: Service Unavailable
- Google News 財經來源抓取失敗：site:moneydj.com 台股 OR 個股 OR 產業 OR 半導體 OR 財報 OR 營收，原因：HTTP Error 503: Service Unavailable
- Google News 財經來源抓取失敗：site:mops.twse.com.tw 重大訊息 OR 月營收 OR 財報 OR 法說會，原因：HTTP Error 503: Service Unavailable
- Google News 財經來源抓取失敗：site:nasdaq.com earnings OR dividend OR IPO OR split，原因：HTTP Error 503: Service Unavailable
- Google News 財經來源抓取失敗：site:news.cnyes.com 台股 OR 個股 OR 美股 OR 半導體 OR 財報 OR 營收，原因：HTTP Error 503: Service Unavailable
- Google News 財經來源抓取失敗：site:reuters.com markets OR stocks OR earnings OR revenue OR semiconductor OR AI，原因：HTTP Error 503: Service Unavailable
- Google News 財經來源抓取失敗：site:technews.tw 半導體 OR AI OR 晶片 OR 先進封裝 OR 伺服器，原因：HTTP Error 503: Service Unavailable
- Google News 財經來源抓取失敗：site:tpex.org.tw 上櫃 OR 興櫃 OR 注意股票 OR 公告，原因：HTTP Error 503: Service Unavailable
- Google News 財經來源抓取失敗：site:tw.stock.yahoo.com 台股 OR 個股 OR 美股 OR 半導體 OR 財報 OR 營收，原因：HTTP Error 503: Service Unavailable
- Google News 財經來源抓取失敗：site:twse.com.tw 上市公司 OR 注意股票 OR 法人 OR 成交資訊，原因：HTTP Error 503: Service Unavailable
- RSS 抓取失敗：https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant，原因：HTTP Error 503: Service Unavailable
- RSS 抓取失敗：https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en，原因：HTTP Error 503: Service Unavailable
- RSS 抓取失敗：https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en，原因：HTTP Error 503: Service Unavailable
- RSS 抓取失敗：https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant，原因：HTTP Error 503: Service Unavailable
- RSS 抓取失敗：https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en，原因：HTTP Error 503: Service Unavailable
- RSS 抓取失敗：https://news.google.com/rss/search?q=site%3Actee.com.tw%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20OR%20%E7%94%A2%E6%A5%AD%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant，原因：HTTP Error 503: Service Unavailable
- RSS 抓取失敗：https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant，原因：HTTP Error 503: Service Unavailable
- RSS 抓取失敗：https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant，原因：HTTP Error 503: Service Unavailable
- RSS 抓取失敗：https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en，原因：HTTP Error 503: Service Unavailable
- RSS 抓取失敗：https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant，原因：HTTP Error 503: Service Unavailable
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
- 未取得符合報告日期的即時新聞，改用內建樣本新聞產生報告。
