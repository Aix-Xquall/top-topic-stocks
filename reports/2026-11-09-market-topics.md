# 每日股市熱門話題分析 - 2026-11-09

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **AI 伺服器與資料中心**｜負向｜熱度 12｜市場確認 82.50｜同向 6/8
2. **新興題材：10月營收**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
3. **半導體與晶片供應鏈**｜中性｜熱度 3｜市場確認 N/A｜同向 0/0
4. **散熱與液冷供應鏈**｜正向｜熱度 4｜市場確認 0.00｜同向 0/1
5. **新興題材：受惠AI伺服器**｜正向｜熱度 1｜市場確認 0.00｜同向 0/1

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.56（樣本 10）
- 5日相關係數：-0.62（樣本 9）
- 同向比例：6/10

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| AI 伺服器與資料中心 | 82.50 | 6/8 | 2 | +11.55% | -0.97% |
| 新興題材：10月營收 | N/A | 0/0 | 0 | N/A | N/A |
| 半導體與晶片供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 散熱與液冷供應鏈 | 0.00 | 0/1 | 1 | -21.29% | -25.36% |
| 新興題材：受惠AI伺服器 | 0.00 | 0/1 | 1 | -21.29% | -25.36% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：盯10月營收 | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價呈負相關；應檢查正負向詞庫，並降低新聞直接提及但股價背離的權重。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-10-26 | 0.27 | -0.25 | +36.36% | 11 |
| 2026-10-27 | 0.07 | 0.31 | +50.00% | 18 |
| 2026-10-28 | -0.30 | 0.47 | +20.00% | 15 |
| 2026-10-29 | -0.05 | 0.04 | +42.86% | 14 |
| 2026-10-30 | -0.00 | -0.05 | +47.62% | 21 |
| 2026-10-31 | 0.50 | -0.68 | +80.00% | 15 |
| 2026-11-01 | 0.47 | -0.40 | +85.71% | 14 |
| 2026-11-02 | -0.15 | -0.06 | +27.78% | 18 |
| 2026-11-03 | -0.03 | 0.08 | +40.91% | 22 |
| 2026-11-04 | -0.21 | 0.35 | +15.79% | 19 |
| 2026-11-05 | 0.13 | -0.53 | +66.67% | 12 |
| 2026-11-06 | -0.18 | 0.77 | +100.00% | 5 |
| 2026-11-08 | -0.21 | 0.03 | +23.08% | 13 |
| 2026-11-09 | -0.56 | -0.62 | +60.00% | 10 |

## 歷史回測摘要

- 回測日期：2026-11-09
- 近5日 3日相關：-0.03
- 近5日 5日相關：-0.53
- 同向比例：+75.00%
- 權重狀態：未調整

- 方向準確度：+75.00%
- 信心排序準確度：-0.03
- 診斷：信心校準問題

調整原因：近 5 日方向判斷多數同向，但信心分數與後續報酬呈負相關；判定為信心校準問題，優先降低高信心膨脹、寬題材推估與背離容忍。；關鍵詞×公司後續樣本有效 4 筆，未達 30 筆，不調整樣本權重

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

摘要：AI 伺服器與資料中心 相關新聞集中在：特納斯首份財報過關，蘋果「AI 避風港」光環卻開始褪色 - TechNews 科技新報；AI 駭客攻擊日韓企業：自動化網路入侵加劇企業資安與營運風險 - TechNews 科技新報；YC 執行長陳嘉興堪稱 AI 代理「重度發燒友」，每年 token 費高達 20 萬美元 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MSFT 微軟 | 新聞直接提及 | -0.25 | +17.85% | +7.85% | 530.61 | 530.61 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 新聞直接提及 | -0.21 | +9.71% | +22.78% | 342.37 | 342.37 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| INTC 英特爾 | 產業/供應鏈推估 | -0.08 | -50.92% | +38.76% | 56.28 | 114.68 | -50.92% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | -0.06 | -18.28% | -7.03% | 186.64 | 228.38 | -18.28% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | -0.06 | -12.99% | N/A | 449.04 | 516.10 | -12.99% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | -0.06 | -6.97% | -9.92% | 2,135.00 | 2,480.00 | -13.91% | 同向 | 86.28 | 24.75 | 511.86B TWD / 54.65% | 2026-10-01 |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -16.37% | -24.56% | 293.69 | 446.77 | -34.26% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.04 | -14.45% | -21.11% | 527.00 | 703.00 | -25.04% | 同向 | 13.92 | 38.13 | 88.13B TWD / 45.52% | 2026-10-01 |

關聯理由（前 3）：
- MSFT：新聞直接提及「微軟」，共 1 篇新聞命中。 同時符合主題標籤：AI, datacenter。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AAPL：新聞直接提及「蘋果」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [特納斯首份財報過關，蘋果「AI 避風港」光環卻開始褪色 - TechNews 科技新報](https://news.google.com/rss/articles/CBMifEFVX3lxTE1vTXBKbnNZN2c2RDR2VFpEeGlaLU9EMnNYZmdiUWFmMExjMUdJMFJUNnhrZkZVYkRKMWxxTWNtVHBQMFBvRHRSM1NIaWEtUVB1Y3MwS2toeElpNnZDYU03eG01blZQRGFnb21IcmFKc0lybVhsRks4OGx2SGw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 08 Nov 2026 23:32:58 GMT
- [AI 駭客攻擊日韓企業：自動化網路入侵加劇企業資安與營運風險 - TechNews 科技新報](https://news.google.com/rss/articles/CBMirwFBVV95cUxQYkFiaTRxV3htQzNyLWtzTGo1NHpHNHpWWkZGMnU5M2huWGMzSlZJQ3ZhS05oT0ZTaVZ1X0lkNFlSSDNMZExfYnAxMWV4TW5NeGc1Sk5TOXQ5U2hHYzZmQnRTeG9vdnN3d1pvTy1uZE1lZ3NybkxSM1dWX1pUTWFDd2h0S3cyQTFmZ0J2TUNMTTV5NzVKQWt5dDVWLXhpM0xpd3JrMXI2UThIMllta2Nr?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 09 Nov 2026 00:08:47 GMT
- [YC 執行長陳嘉興堪稱 AI 代理「重度發燒友」，每年 token 費高達 20 萬美元 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiwgFBVV95cUxQLV91bmpnakhkNTVfYXc0Njk4QWRlT1FiVERxUHJrWGFfT2ZuZkRRaFlkckpjZFJ0OHQ2cnpVZ0JWSVJ3Z1ZULUFTZkNOaFF2MGlZQkN0bF9IUmllQW8wT3JqbTB2cTVoWFNCU3V2UjdDUFZNdGdsN0Zsa0JyX3NsSktPdm10ZHc0enJDUzRaX3ctVmlldVRGRm92OF9LM3hGWndIWmN2ZTVlU3YyalNBcUZ1MWItQ0JNWDNEQTY1Wk5RZw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 09 Nov 2026 00:31:10 GMT

## 新興題材：10月營收

摘要：新興題材：10月營收 相關新聞集中在：奇鋐端出佳績！10月營收221.03億元連四個月刷單月新高紀錄- 產業 - 工商時報；台康生技雙引擎發威，10月營收創歷史次高，全球商業化布局加速 - Yahoo股市

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | -21.29% | -25.36% | 2,310.00 | 3,435.00 | -32.75% | 不適用 | 75.13 | 30.79 | 22.10B TWD / 34.35% | 2026-11-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐」，共 1 篇新聞命中。

### 主要來源

- [奇鋐端出佳績！10月營收221.03億元連四個月刷單月新高紀錄- 產業 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTFAzVzdCRnNSa3c3NUhrTWc3NWtCUmptdDU3N0taTzVGYzRjdDFaLV9uTHNkME9CZnpMTlZIcjg3QlhYdGV3SmNVOFlyVUlKZmxXc0kzQWFmaHUwZUdQaVlZ?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 08 Nov 2026 07:25:00 GMT
- [台康生技雙引擎發威，10月營收創歷史次高，全球商業化布局加速 - Yahoo股市](https://news.google.com/rss/articles/CBMimANBVV95cUxPUjcwdnNGczlHLXk5Z3EwX1JuTUtQYXJoMTdJZ0dkXzRzS1BoOVlJWFlZRFgwV0U4cXlMRVhCX3RKTVNpREVCMnJTOUkwcnpseWZuUWhGbUV4TjVRcXUzSmdaMzJ5T0F1bkR0WTU3ak5yeGpQeHI3cFZfTm1NVzJpQjVvQUtMMmhtX2ZaYi1wUWY5Mm0wcVF6dDBGczFlQV8tNkQtR2lwV3RnallGMFFETlZPejZaMTJJc1NsYTNoazFZdDg0WTBTUDk1TG5BZzZKeUJBQXktZno2RVVidENMVERaYlZFNVZWblpaendhejhZZURwOFotMTAwUlJjQ1V0VUg2WFl2cWJFQWY4QlEyU01YLTBqOFl4eTRlTXRoYmJBZkZ1VUlVWktxTDJNUV84UmdXWExlYmtkdHFJQWlaUWpsVWpkVGRiczhzbVhLZDY1NnRCLVRZQ2Yyb2w2RXpkZldETVd3SVRNQkJTcUxjNU94TG55WTQ0dm1LaVR6Y0pncExBUHNEMXB2eWxOWjN4OFE5LUJLbC0?oc=5) - Google News source discovery | Yahoo 奇摩股市 Mon, 09 Nov 2026 00:11:09 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：辛辛那提大學放映造山者蔡明介盼創造更多半導體黃金年代| 產經 - 中央社 CNA；印太對話聚焦台印合作 盼半導體搭橋 - 中央社 CNA；南科躍全球最大半導體聚落 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 產業/供應鏈推估 | 0.00 | -50.92% | +38.76% | 56.28 | 114.68 | -50.92% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -6.97% | -9.92% | 2,135.00 | 2,480.00 | -13.91% | 不適用 | 86.28 | 24.75 | 511.86B TWD / 54.65% | 2026-10-01 |
| 2303 聯電 | 產業/供應鏈推估 | 0.00 | -10.68% | -17.49% | 92.00 | 164.50 | -44.07% | 不適用 | 6.80 | 13.59 | 25.20B TWD / 18.33% | 2026-11-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -18.28% | -7.03% | 186.64 | 228.38 | -18.28% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | 0.00 | -12.99% | N/A | 449.04 | 516.10 | -12.99% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | 0.00 | -28.94% | N/A | 690.00 | 971.00 | -28.94% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | 0.00 | -25.87% | -27.44% | 835.06 | 2,335.00 | -64.24% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -16.37% | -24.56% | 293.69 | 446.77 | -34.26% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 CPU, server CPU, x86, foundry；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, chip, foundry；其中 0 篇新聞出現相關標籤。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 0 篇新聞出現相關標籤。

### 主要來源

- [辛辛那提大學放映造山者蔡明介盼創造更多半導體黃金年代| 產經 - 中央社 CNA](https://news.google.com/rss/articles/CBMiXkFVX3lxTE9jSGY2THR4NlJTX19EMEdJY0dIaFJiTG1jaS1zU3p4Ykg5ZkkxbEpSRDA2ZmNmUl9GREtkcU5NNFZHUE9tdWlNbVljNmpzQmV2N2FuaU1uLTFQcjdWb2c?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 08 Nov 2026 15:50:00 GMT
- [印太對話聚焦台印合作 盼半導體搭橋 - 中央社 CNA](https://news.google.com/rss/articles/CBMiV0FVX3lxTE9WbkRqNi1RWGh0MHZEcTkwZEoyQzJ6RU5hR3daSFdackFST1BLRnpzcnR4Vk9TanlKWGJOVDlPN1NWY2VUSmlIRzYwb2FwWFVDeGZocXNyMA?oc=5) - https://news.google.com/rss/search?q=site%3Acna.com.tw%20%E8%B2%A1%E7%B6%93%20OR%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20OR%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 07 Nov 2026 08:49:53 GMT
- [南科躍全球最大半導體聚落 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1zcEpBS2RWOFZGM0VyT09hWXVQc0JUV0xOSTAxZ3M5NDlsTFp5R3pRLUdjaXRKQnZMT3ptclJLbk1QUkV1NFpKMTVzM25IRXFleEVaNHJZWTNwQdIBX0FVX3lxTFAzR3VzTHNsSElCZElEbWJWT2hEMTM3Nl9JTHZvOEVpZ3MtZG43Q1hwZGFqem1ZQS1PX1VqbkV0MnJpOE13X3VhMU5wSzF2aS1jRmlzdE9RdDJKLWZ2TldZ?oc=5) - Google News source discovery | 經濟日報 money Sun, 08 Nov 2026 09:00:00 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：奇鋐端出佳績！10月營收221.03億元連四個月刷單月新高紀錄- 產業 - 工商時報；散熱股又有大消息？花旗喊買奇鋐、雙鴻 目標價齊升逾14% - 經濟日報；【即時新聞】奇鋐今日公告最新財報，受惠AI伺服器放量，第三季營收年增逾五成表現亮眼！ - CMoney投資網誌

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.28 | -21.29% | -25.36% | 2,310.00 | 3,435.00 | -32.75% | 背離 | 75.13 | 30.79 | 22.10B TWD / 34.35% | 2026-11-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐」，共 4 篇新聞命中。 同時符合主題標籤：thermal。 方向判斷命中詞：受惠, 放量, 創高。

### 主要來源

- [奇鋐端出佳績！10月營收221.03億元連四個月刷單月新高紀錄- 產業 - 工商時報](https://news.google.com/rss/articles/CBMiX0FVX3lxTFAzVzdCRnNSa3c3NUhrTWc3NWtCUmptdDU3N0taTzVGYzRjdDFaLV9uTHNkME9CZnpMTlZIcjg3QlhYdGV3SmNVOFlyVUlKZmxXc0kzQWFmaHUwZUdQaVlZ?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 08 Nov 2026 07:25:00 GMT
- [散熱股又有大消息？花旗喊買奇鋐、雙鴻 目標價齊升逾14% - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE04UXU3RGRUUnBBVElIbVBGZWozMUxfTzNsbE50ejYzRE1pUTJBQ0FNWS03VjRSYlZrUWkzSXhuNHhFQl9teWs5YTJ4QUU4ck1MZ0NneEk3XzF3UdIBX0FVX3lxTE5tclh3dXNNWDhDMnNiYmMyRW1DRFJwZUt6ZlZXMmdEYlhoQU9VR1pSeTVrVUpVT2FWOE1idEkxdXRhYTYyYVpMcnRwaWQ4NGpmRUNTREJUQ2UwNU01N0pF?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sat, 07 Nov 2026 08:00:00 GMT
- [【即時新聞】奇鋐今日公告最新財報，受惠AI伺服器放量，第三季營收年增逾五成表現亮眼！ - CMoney投資網誌](https://news.google.com/rss/articles/CBMikAFBVV95cUxQSndXY2F6U2tvOWFGcm5qVUdZcVNLckR2eml1cENlSlgtSE0yNmxtSk1lZWNEQ1c4YU9jN1Z1WUk0TnpuZkRHbEpyYWx3NmhXODBHd0RlZk9hNHE3UjNCZmRGOFdmQnNmUjRkV1RlYlhabV9ndzJaMEdydHdUSER5SmxkNVRmSkV6MVN2UWkwZkM?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 08 Nov 2026 22:20:43 GMT

## 新興題材：受惠AI伺服器

摘要：新興題材：受惠AI伺服器 相關新聞集中在：【即時新聞】奇鋐今日公告最新財報，受惠AI伺服器放量，第三季營收年增逾五成表現亮眼！ - CMoney投資網誌

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | +0.21 | -21.29% | -25.36% | 2,310.00 | 3,435.00 | -32.75% | 背離 | 75.13 | 30.79 | 22.10B TWD / 34.35% | 2026-11-01 |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐」，共 1 篇新聞命中。 方向判斷命中詞：受惠, 放量。

### 主要來源

- [【即時新聞】奇鋐今日公告最新財報，受惠AI伺服器放量，第三季營收年增逾五成表現亮眼！ - CMoney投資網誌](https://news.google.com/rss/articles/CBMikAFBVV95cUxQSndXY2F6U2tvOWFGcm5qVUdZcVNLckR2eml1cENlSlgtSE0yNmxtSk1lZWNEQ1c4YU9jN1Z1WUk0TnpuZkRHbEpyYWx3NmhXODBHd0RlZk9hNHE3UjNCZmRGOFdmQnNmUjRkV1RlYlhabV9ndzJaMEdydHdUSER5SmxkNVRmSkV6MVN2UWkwZkM?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 08 Nov 2026 22:20:43 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：國安基金護盤+美股反彈 台股今日拚首波解套行情 - 經濟日報；台股跌深可以搶反彈了？凱基：先過4萬點 還要等三訊號 - 經濟日報；台股1個月以來急跌萬點　法人：不宜貿然搶反彈 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [國安基金護盤+美股反彈 台股今日拚首波解套行情 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBiNTVHVVFVSnc2ek82OWh4a2Jrc1NTOE5WUG1XQXdPd0xfenlNOE5TdVQzQVVjMGRlaXBxNHRUdkNrV3JYUTlVZ2JMZDdqeUIyOUEwRWQ4eGhkd9IBX0FVX3lxTE5Sd1dZSUR6Q3VadWh6QVNPRUw2Q3JGbno0VDFDRFpTVUpwYUdIV3A5VTA0R0tMWUZvYl9DekRHaTZaNU5jZ0Jmdk1oNUI4OUJJdl9KcWxiR0pXaC1sT0pz?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 08 Nov 2026 17:26:29 GMT
- [台股跌深可以搶反彈了？凱基：先過4萬點 還要等三訊號 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9DcUF5TF81SU0zd1dXSjFhdkwwTVc1MkNKRGs4d19Ea0ljWVRPVFBBMWhVclYyZkt1WVFWUXg3d0JDcmVHMlphLUNHQ1JmeFlhZ3BBREZwZFQwQdIBX0FVX3lxTE1ua3d0ZFBUc0ptMUtkYVZjTjhJVTJZOHhXY0tJNUdoV0NrcUNSeHQ1c0RSRFZIOFY0eVFydFpSOWZZQWd2SVBQWlFuMHhoTEVuOXpnZ1ZYS3dGR1c4S0Qw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 08 Nov 2026 09:27:56 GMT
- [台股1個月以來急跌萬點　法人：不宜貿然搶反彈 - 經濟日報](https://news.google.com/rss/articles/CBMieEFVX3lxTE45WS1LMHdwUXhObEJHUFZLNUNpblpjMkdqRWxKVkdtNUdwTlVzRi1HcUJJNWdLZ1hCblhabHhSX19UcVUzMXdIcDF1MUpoQU54dzR2SWdVcGJYUVRYXzMzX2VJVkVtZFNEMEJIWlgtTW9PN3dHSUlfZNIBX0FVX3lxTE9mMnRhb09nVWVYekZXLU9Xd2JpLUR1VUJIQnpGejhnZGQwNXNxLU94ZS16M2hmNndxSmpvdWZnSndGRG5rc2FTOThZTmlSUEpLRjlQSGFiaUt0ZWlsUUF3?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 08 Nov 2026 02:45:32 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：台股回檔跌回4萬點區間！正二ETF績效亮眼，投資人如何看待槓桿風險？ - MoneyDJ；國票證券：台股若確認買盤延續性，有望迎接反彈行情 - 台股 - 新聞 - MoneyDJ；統一證券：台股力拚重返4萬點整數關卡- 新聞 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股回檔跌回4萬點區間！正二ETF績效亮眼，投資人如何看待槓桿風險？ - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxOOUdRS1NTTEVlX0dpS3NiRk81SjN1R00xVVo0SmxBWDM0YkZfTVFIOGdWb0R5MXZ0ZkNacjNCWjVvbVJXTmZCU1o1WUFmN3BZUzc0NjBNQWpWeXNEMU55OTQ4STBVZ00xMElqVlh0SG9hdE5DaGpHNmhsRnBTOXY1TVJ0c0FNUmNCdUprM1ZfQWR6UQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 09 Nov 2026 00:45:00 GMT
- [國票證券：台股若確認買盤延續性，有望迎接反彈行情 - 台股 - 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMimwFBVV95cUxPLVRsdWxQYWtxYnhHWFRyVkc1bFBON1o5eC1RSm9wV2w1djJjZHhSbTdGcFVCdF9SLTF6LWhnN3V4UmJOVmNZOEVHUkRWNVYyOGdhc2Q1cWVvaVREa045YUhQSmhnaDdKRUVITWRveEI2X0p5THV0S19lRkFjeXVSZDBJRm9oYlF0b1lVR1NaalBhUzhmLXYzQU94OA?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 09 Nov 2026 00:37:00 GMT
- [統一證券：台股力拚重返4萬點整數關卡- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPNXZudnFSTHhDX0FhVHVrdVZnTnZZSFNoc00za0JUMHdETUxrYTktdGRzNHBCZGkyV003SzNCX3lNcjJQaEJKX2UxU1lMSzNjQ2FJeXVtaFVEdVRWVVl6ZVlSakpZeTVnMUJuMUhzRXBrN0JVQTJNOTV5SEJTelprU2owNnJ0ems4X0xpcHlfSEFydw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Mon, 09 Nov 2026 00:37:00 GMT

## 新興題材：盯10月營收

摘要：新興題材：盯10月營收 相關新聞集中在：台股拚 V 型反轉 盯10月營收成績單 - 經濟日報

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [台股拚 V 型反轉 盯10月營收成績單 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9mWDFWQ0x3UFVHZmkxajhXSXFvNkhnQWFTUTFZY3lDZjRjN2g5U1Q5eUZ6SFpuWk1ETEZPQzJUUzhYeVctVVFlaFdMdlZKS0FPZUdKZU0yc1hpUdIBX0FVX3lxTE9ZWTI4ZHdreVVpR05yTTN3UE80TkJlQW1kamFlajZVbGVHVjRVNWZzdjNTbjEzdnZLVmtva3hGVmhQa182TXhHam1XbWd4elJkUVduUXZwSlR4aVVMREJJ?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Sun, 08 Nov 2026 07:00:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
