# 每日股市熱門話題分析 - 2026-07-19

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **電動車與電池**｜負向｜熱度 1｜市場確認 100.00｜同向 1/1
2. **利率與成長股估值**｜正向｜熱度 1｜市場確認 N/A｜同向 0/0
3. **消費電子與手機**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0
4. **關稅與供應鏈轉移**｜正向｜熱度 2｜市場確認 29.58｜同向 1/4
5. **先進封裝與 CoPoS**｜正向｜熱度 2｜市場確認 0.00｜同向 0/3

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.37（樣本 16）
- 5日相關係數：0.09（樣本 16）
- 同向比例：2/16

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 電動車與電池 | 100.00 | 1/1 | 0 | +12.61% | -2.45% |
| 利率與成長股估值 | N/A | 0/0 | 0 | N/A | N/A |
| 消費電子與手機 | N/A | 0/0 | 0 | N/A | N/A |
| 關稅與供應鏈轉移 | 29.58 | 1/4 | 2 | +4.03% | +6.95% |
| 先進封裝與 CoPoS | 0.00 | 0/3 | 3 | -4.51% | +0.60% |
| 記憶體與 HBM 供應鏈 | 0.00 | 0/4 | 4 | -9.12% | -6.87% |
| 新興題材：股半導體族群受惠先進封裝 | 0.00 | 0/2 | 2 | -4.79% | -7.25% |
| 新興題材：晶片需求 | 0.00 | 0/2 | 2 | -4.79% | -7.25% |

### 方法調整建議

- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-07-06 | N/A | N/A | 0.00% | 2 |
| 2026-07-07 | N/A | N/A | 0.00% | 1 |
| 2026-07-08 | -0.05 | -0.05 | +71.43% | 14 |
| 2026-07-09 | -0.11 | -0.36 | +64.29% | 14 |
| 2026-07-10 | 0.55 | 0.05 | +77.78% | 9 |
| 2026-07-11 | 0.13 | -0.08 | +50.00% | 12 |
| 2026-07-12 | 0.27 | 0.13 | +16.67% | 12 |
| 2026-07-13 | 0.39 | -0.09 | +15.38% | 13 |
| 2026-07-14 | 0.10 | -0.07 | +21.43% | 14 |
| 2026-07-15 | 0.20 | -0.16 | +28.57% | 7 |
| 2026-07-16 | 0.20 | 0.02 | +33.33% | 12 |
| 2026-07-17 | 0.36 | 0.02 | +60.00% | 15 |
| 2026-07-18 | 0.18 | 0.08 | +53.85% | 13 |
| 2026-07-19 | 0.37 | 0.09 | +12.50% | 16 |

## 歷史回測摘要

- 回測日期：2026-07-19
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
| TSLA 特斯拉 | 新聞直接提及 | -0.51 | -12.61% | +2.45% | 380.84 | 456.56 | -16.58% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- TSLA：新聞直接提及「Tesla」，共 1 篇新聞命中。 同時符合主題標籤：EV, electric vehicle, battery, autonomous driving。 方向判斷命中詞：pressure。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [EV competition and battery pricing put Tesla and power semiconductor suppliers in focus](https://example.com/sample/ev-battery) - sample 2026-05-07T04:00:00Z

## 利率與成長股估值

摘要：利率與成長股估值 相關新聞集中在：降息預期升溫，美股科技股與高本益比成長股估值重新受到討論

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +0.27% | -22.28% | 393.82 | 506.69 | -22.28% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MSFT：產業/供應鏈推估：公司標籤符合「利率與成長股估值」關鍵字 rate cut；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [降息預期升溫，美股科技股與高本益比成長股估值重新受到討論](https://example.com/sample/rate-cut-tech) - sample 2026-05-07T08:00:00+08:00

## 消費電子與手機

摘要：消費電子與手機 相關新聞集中在：Tariff uncertainty pressures Apple hardware supply chain while investors watch Taiwan exporters

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AAPL 蘋果 | 新聞直接提及 | 0.00 | +26.33% | +43.77% | 333.74 | 333.74 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | -0.64% | -1.47% | 234.00 | 289.00 | -19.03% | 不適用 | 14.13 | 16.62 | 821.76B TWD / 52.11% | 2026-07-01 |
| 2454 聯發科 | 產業/供應鏈推估 | 0.00 | -7.92% | -14.14% | 3,370.00 | 4,310.00 | -21.81% | 不適用 | 62.91 | 53.71 | 58.01B TWD / 2.80% | 2026-07-01 |

關聯理由（前 3）：
- AAPL：新聞直接提及「Apple」，共 1 篇新聞命中。 同時符合主題標籤：hardware, consumer electronics, smartphone。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「消費電子與手機」關鍵字 hardware, consumer electronics；其中 1 篇新聞出現相關標籤。
- 2454：產業/供應鏈推估：公司標籤符合「消費電子與手機」關鍵字 smartphone；其中 0 篇新聞出現相關標籤。

### 主要來源

- [Tariff uncertainty pressures Apple hardware supply chain while investors watch Taiwan exporters](https://example.com/sample/tariff-apple) - sample 2026-05-07T05:30:00Z

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：台股半導體族群受惠先進封裝與 AI 晶片需求，台積電、日月光與記憶體相關個股受關注；Tariff uncertainty pressures Apple hardware supply chain while investors watch Taiwan exporters

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AAPL 蘋果 | 新聞直接提及 | +0.47 | +26.33% | +43.77% | 333.74 | 333.74 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | +0.21 | -5.37% | -5.18% | 2,290.00 | 2,410.00 | -4.98% | 背離 | 74.39 | 30.79 | 442.68B TWD / 67.87% | 2026-07-01 |
| 3711 日月光投控 | 新聞直接提及 | +0.21 | -4.21% | -9.31% | 614.00 | 680.00 | -9.71% | 背離 | 10.86 | 57.01 | 65.78B TWD / 32.86% | 2026-07-01 |
| 2317 鴻海 | 產業/供應鏈推估 | +0.06 | -0.64% | -1.47% | 234.00 | 289.00 | -19.03% | 未明確 | 14.13 | 16.62 | 821.76B TWD / 52.11% | 2026-07-01 |

關聯理由（前 3）：
- AAPL：新聞直接提及「Apple」，共 1 篇新聞命中。 同時符合主題標籤：tariff, supply chain。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 方向判斷命中詞：受惠。
- 3711：新聞直接提及「日月光」，共 1 篇新聞命中。 方向判斷命中詞：受惠。

### 主要來源

- [台股半導體族群受惠先進封裝與 AI 晶片需求，台積電、日月光與記憶體相關個股受關注](https://example.com/sample/tw-semiconductor) - sample 2026-05-07T07:00:00+08:00
- [Tariff uncertainty pressures Apple hardware supply chain while investors watch Taiwan exporters](https://example.com/sample/tariff-apple) - sample 2026-05-07T05:30:00Z

## 先進封裝與 CoPoS

摘要：先進封裝與 CoPoS 相關新聞集中在：AI server demand lifts Nvidia, TSMC and memory chip suppliers as datacenter spending rises；台股半導體族群受惠先進封裝與 AI 晶片需求，台積電、日月光與記憶體相關個股受關注

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | +0.29 | -5.37% | -5.18% | 2,290.00 | 2,410.00 | -4.98% | 背離 | 74.39 | 30.79 | 442.68B TWD / 67.87% | 2026-07-01 |
| 3711 日月光投控 | 新聞直接提及 | +0.24 | -4.21% | -9.31% | 614.00 | 680.00 | -9.71% | 背離 | 10.86 | 57.01 | 65.78B TWD / 32.86% | 2026-07-01 |
| NVDA 輝達 | 新聞直接提及 | +0.21 | -3.95% | +16.29% | 202.81 | 211.14 | -3.95% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 新聞直接提及 | +0.43 | N/A | N/A | 848.95 | 971.00 | -12.57% | N/A | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 2330：新聞直接提及「TSMC、台積電」，共 2 篇新聞命中。 同時符合主題標籤：advanced packaging, CoWoS, CoPoS, FOPLP。 方向判斷命中詞：受惠。
- 3711：新聞直接提及「日月光」，共 1 篇新聞命中。 同時符合主題標籤：advanced packaging, CoPoS, FOPLP, panel-level packaging。 方向判斷命中詞：受惠。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [AI server demand lifts Nvidia, TSMC and memory chip suppliers as datacenter spending rises](https://example.com/sample/ai-server-demand) - sample 2026-05-07T06:00:00Z
- [台股半導體族群受惠先進封裝與 AI 晶片需求，台積電、日月光與記憶體相關個股受關注](https://example.com/sample/tw-semiconductor) - sample 2026-05-07T07:00:00+08:00

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：AI server demand lifts Nvidia, TSMC and memory chip suppliers as datacenter spending rises；台股半導體族群受惠先進封裝與 AI 晶片需求，台積電、日月光與記憶體相關個股受關注

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.45 | N/A | N/A | 848.95 | 971.00 | -12.57% | N/A | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | +0.21 | -5.37% | -5.18% | 2,290.00 | 2,410.00 | -4.98% | 背離 | 74.39 | 30.79 | 442.68B TWD / 67.87% | 2026-07-01 |
| NVDA 輝達 | 新聞直接提及 | +0.20 | -3.95% | +16.29% | 202.81 | 211.14 | -3.95% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 新聞直接提及 | +0.18 | -4.21% | -9.31% | 614.00 | 680.00 | -9.71% | 背離 | 10.86 | 57.01 | 65.78B TWD / 32.86% | 2026-07-01 |
| SNDK SanDisk | 產業/供應鏈推估 | +0.06 | -22.93% | -29.29% | 1,354.82 | 2,335.00 | -41.98% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

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
| 2330 台積電 | 新聞直接提及 | +0.21 | -5.37% | -5.18% | 2,290.00 | 2,410.00 | -4.98% | 背離 | 74.39 | 30.79 | 442.68B TWD / 67.87% | 2026-07-01 |
| 3711 日月光投控 | 新聞直接提及 | +0.21 | -4.21% | -9.31% | 614.00 | 680.00 | -9.71% | 背離 | 10.86 | 57.01 | 65.78B TWD / 32.86% | 2026-07-01 |

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
| 2330 台積電 | 新聞直接提及 | +0.21 | -5.37% | -5.18% | 2,290.00 | 2,410.00 | -4.98% | 背離 | 74.39 | 30.79 | 442.68B TWD / 67.87% | 2026-07-01 |
| 3711 日月光投控 | 新聞直接提及 | +0.21 | -4.21% | -9.31% | 614.00 | 680.00 | -9.71% | 背離 | 10.86 | 57.01 | 65.78B TWD / 32.86% | 2026-07-01 |

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
