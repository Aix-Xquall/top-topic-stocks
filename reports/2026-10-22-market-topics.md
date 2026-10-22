# 每日股市熱門話題分析 - 2026-10-22

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **新興題材：SpaceX**｜正向｜熱度 4｜市場確認 88.19｜同向 2/2
2. **關稅與供應鏈轉移**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
3. **記憶體與 HBM 供應鏈**｜中性｜熱度 2｜市場確認 N/A｜同向 0/0
4. **新興題材：AI競爭從晶片**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0
5. **AI 伺服器與資料中心**｜負向｜熱度 14｜市場確認 27.14｜同向 3/8

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：0.02（樣本 18）
- 5日相關係數：-0.21（樣本 12）
- 同向比例：7/18

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 新興題材：SpaceX | 88.19 | 2/2 | 0 | +6.07% | -8.11% |
| 關稅與供應鏈轉移 | N/A | 0/0 | 0 | N/A | N/A |
| 記憶體與 HBM 供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：AI競爭從晶片 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | 27.14 | 3/8 | 3 | +0.30% | +1.68% |
| 半導體與晶片供應鏈 | 9.58 | 2/8 | 4 | -2.64% | -3.61% |
| 綜合市場情緒 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 相關性偏弱；應提高同向價格確認權重，降低泛 AI、泛半導體等寬標籤推估權重。
- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-10-09 | -0.03 | 0.37 | +38.89% | 18 |
| 2026-10-10 | -0.28 | -0.96 | +57.14% | 7 |
| 2026-10-11 | 0.66 | -0.74 | +40.00% | 5 |
| 2026-10-12 | -0.08 | -0.07 | +41.67% | 12 |
| 2026-10-13 | -0.05 | -0.03 | +46.67% | 15 |
| 2026-10-14 | 0.08 | -0.29 | +57.14% | 14 |
| 2026-10-15 | -0.08 | 0.08 | +33.33% | 12 |
| 2026-10-16 | -0.13 | -0.25 | +64.00% | 25 |
| 2026-10-17 | -0.10 | 0.49 | +26.32% | 19 |
| 2026-10-18 | -0.12 | 0.33 | +21.74% | 23 |
| 2026-10-19 | 0.44 | 0.36 | +50.00% | 12 |
| 2026-10-20 | 0.09 | -0.81 | +69.23% | 13 |
| 2026-10-21 | -0.25 | 0.23 | +5.56% | 18 |
| 2026-10-22 | 0.02 | -0.21 | +38.89% | 18 |

## 歷史回測摘要

- 回測日期：2026-10-22
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

## 新興題材：SpaceX

摘要：新興題材：SpaceX 相關新聞集中在：Nasdaq leads Wall Street gains as SpaceX, Super Micro boost AI sentiment - Reuters；SpaceX gives the AI trade a shot in the arm. What it means for our stocks - CNBC；SpaceX 財報／營收大增161% AI 業務狂飆九倍 馬斯克喊支持與特斯拉合併 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AMD 超微 | 新聞直接提及 | +0.42 | +7.10% | N/A | 552.72 | 552.72 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| TSLA 特斯拉 | 新聞直接提及 | +0.42 | +5.03% | -8.11% | 386.47 | 456.56 | -15.35% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- AMD：新聞直接提及「超微」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- TSLA：新聞直接提及「特斯拉」，共 1 篇新聞命中。 方向判斷命中詞：大增。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Nasdaq leads Wall Street gains as SpaceX, Super Micro boost AI sentiment - Reuters](https://news.google.com/rss/articles/CBMivwFBVV95cUxQZUJTOXdaa0JmVzZubm12MGt4VnNSemsyOW1fQXpCMnhEc25HSVJRZk93d2NYUXQ3eHBuQklaNE1FT1QyQ1NqdTFkdExDbmoxY2JtOWhLQkVtYXczMHh3a3VsZmhub1JFc0FIZHN1eEcwc3FRZVZWQnBoSjFjekFYTUN6X2d5WHJUWGpDU2paekhhU24zenhNbWpXUmtfdmo5cTFIZVZwTXdiRzZoeUtiazhHWkJEWEVZLTVmQmRMcw?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 21 Oct 2026 23:11:13 GMT
- [SpaceX gives the AI trade a shot in the arm. What it means for our stocks - CNBC](https://news.google.com/rss/articles/CBMiwgFBVV95cUxPa3RKeUk2aUowdVFZSGl2akgzVlVSa0laaVJUZTczNVI2QmZraTBfX2RFU01JVkp3QmxzRVBfTFN2ZFgzbVVTUkxXQ0phT090QXFRR1pLUXpZQmFWZkpOblFGd0d3Z1VLY1ZORGJPOFpDRnNCdzRCWlNDREVXYnFvWUw5dnR1WjMwenB1OWlNTW04Y09Ld3AteUFnc2RfVS1uWDFza1puM29odXZFdGtzN09Dd1V0T2pjS1hQY0JhZWtFZw?oc=5) - https://news.google.com/rss/search?q=site%3Acnbc.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 21 Oct 2026 19:01:23 GMT
- [SpaceX 財報／營收大增161% AI 業務狂飆九倍 馬斯克喊支持與特斯拉合併 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBNczZ5aUdiVnZuZXI5Mm9LaF96czIyaXBDX29pdmNVYU5NakFROThGaTdhXzhHUEZ3Y0h6N2lLdkRBYkxjaHhtRGRacWdPOTVDc093ZmFBelZyUDdk0gFiQVVfeXFMTjM3TkJzR3ZqQ250aU5jY2FYQm9leVU5VnhnZGZaZmFjQkEzN1hLblpzSGo5OXZiTDhkaXNmdGZDXzhQQi13ckJ4RVpiWDVwWDJCUUMtbW9XUlFIejFya2hTUlE?oc=5) - Google News source discovery | 經濟日報 money Wed, 21 Oct 2026 00:00:01 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：Hot Chips 2026重點解析：AI競爭從晶片走向機櫃，台積電、世芯-KY等14檔台廠供應鏈｜產業熱話｜豐雲學堂2026 年 10 月 - 永豐金證券；AI 需求排擠傳統產能，消費性電子供應鏈該如何因應？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | 0.00 | 0.00% | -2.81% | 2,420.00 | 2,480.00 | -2.42% | 不適用 | 86.28 | 28.05 | 511.86B TWD / 54.65% | 2026-10-01 |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +10.23% | +23.36% | 343.99 | 343.99 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | +2.46% | +2.88% | 250.00 | 289.00 | -13.49% | 不適用 | 15.21 | 16.48 | 1158.63B TWD / 38.42% | 2026-10-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [Hot Chips 2026重點解析：AI競爭從晶片走向機櫃，台積電、世芯-KY等14檔台廠供應鏈｜產業熱話｜豐雲學堂2026 年 10 月 - 永豐金證券](https://news.google.com/rss/articles/CBMi-gNBVV95cUxQUFV6TGVHbVd6aHlNN3lVZW1KX21mVkZEV0hHQlY4WlBhNVhhQWJJTGlmOHQwS2Nic1pySHp2ZVpaY0w5VHhRbHNMSjdzLWR1Y1NlTHN0b2FTdWlQMk5Pb3d2N01maU1HZGF1V3ZNMzNZR1ZlV056RnVBWnhpckpDeVpaaGUtX0tiZXZOUXdZak5vU1Q1RHM2TUxFUy1xTHRCandoNHBUMldrMkQ2LXFEd1lIUnR0WEhBSGtkbS1FNDh2ZjZ1cGVUSndTYjlMQk5GTFNwZ2x1b2VwTVFPbUxmelZYdlZERTd3R3lTeVpVQlpsNG1xdnlPN0ExVnJPS2JweWJEejFWZm9vb3dTb3d5SjNhSEFTMHJzM1dmUkJ3TjdOTTBhME5GdDFoRUJQTjVhWWdWb3prYUlkeDF3c0thaWU5eUFPUlh4bFl5Rk51cWVEUnNGSHI0NmJKdlZibWZmTEVVM0o0ZlZRcjd0bXZDY2VhanRZdHJJVmVOelE5MGpPNjRfc0JLd2hxdGVQOGpBQ19acFl2UW9MdWR6NDJIMjUyRUhnR0s2dHFGSk14TkJQdHFKRzlOT0luZlZra0I0a2tROGxKc3FCRUhuNkZ0VHVuc2R4NlMzM19yOGNfMndFcHVkcFEwdHp6eDZPc21YcWZGQmdTdHNWdw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 21 Oct 2026 16:47:02 GMT
- [AI 需求排擠傳統產能，消費性電子供應鏈該如何因應？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMi4wFBVV95cUxOMF9LZnlSSE1IS1BKZ0x4OVgwdmpBNUsyQjNfTEQyUV9TelJ0eWRkTWlPSi1TUVNnTEVwQnk1S3dmZldZdnpiZTkySzBQWHAtZU1QaFRGTTkzTjhqM0NiSEpyRHI2THRuZWxfaWN4MDUwU0NzeXdOM3ZTMHU3Z3hNMjJtaEdFMFByWWlVVTZmdUxVUHlibkhnUUpzdzhqQnRoVjZGV1lybC1mb2V5MkZDbEV6dXdCOVQwajV1NFNfV09TekxUSzI3TF9vcElTelA5dHFSSVZTY3o0dFF1QWI2cGYwZw?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 21 Oct 2026 17:08:21 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：SK Hynix Sinks 4% as Seoul Selloff Revives AI Spending Fears; SanDisk Drops 3%, Micron Eases - 24/7 Wall St.；戴爾示警目前積壓訂單高達 950 億美元，記憶體短缺 2027 年將加劇 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | 0.00 | -5.90% | N/A | 913.67 | 971.00 | -5.90% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | -2.11% | -7.89% | 1,365.38 | 2,335.00 | -41.53% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | +0.54% | +10.94% | 221.97 | 228.38 | -2.81% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron」，共 1 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 1 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「記憶體與 HBM 供應鏈」關鍵字 HBM；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [SK Hynix Sinks 4% as Seoul Selloff Revives AI Spending Fears; SanDisk Drops 3%, Micron Eases - 24/7 Wall St.](https://news.google.com/rss/articles/CBMizAFBVV95cUxNcHlHZGJCNmRRWjVDbl9RM2p1RDU5eDNIVU1CenZyVndKMFl5RDdhb0tGTUV5bVc4Wm11cXNZdVUtNkUwcDQ1VHp6bzJzZ0dUbVVKcXR4T2huWVdxTUpMb0xhLU90SXV1V3F6WFl0Z3JmWFpTSlZsZEctZWxXckVtNFEwTVUzTXZqeHpnem9SRVg4alZXRFFTWE15ZURvT2FPTVVUQ295QXRqWVNCQWs3SEhZQ3ZRSWhibWthVGN2MEN5QkRSRlp4YkV4bDM?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Tue, 20 Oct 2026 13:30:00 GMT
- [戴爾示警目前積壓訂單高達 950 億美元，記憶體短缺 2027 年將加劇 - TechNews 科技新報](https://news.google.com/rss/articles/CBMixwFBVV95cUxNc1Vvbzk1TlV5WTBjVWFEbXEwZl95Nkd1b3lQcmUxQ0pkbjlXUWxTM2kzV1g0cVRQYi1QSHZFc3llTjZ1cGdqdHlvbWMtblBzSmhDUXJVUGE3WEhIc0FNeHlmeENNZHBJSEkzd3FRY3pWakVvY0h5aFJFZG9VYWZmMXpjY2J6TjNJekdRZjhkV3NUbTdNcEFBLXpZMnpxM2piQmVhdGpTRy0wUWFiS1RHRzZZc0w5TjNEeGM0NnRrSDk4M0VzUWJj?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 21 Oct 2026 02:56:40 GMT

## 新興題材：AI競爭從晶片

摘要：新興題材：AI競爭從晶片 相關新聞集中在：Hot Chips 2026重點解析：AI競爭從晶片走向機櫃，台積電、世芯-KY等14檔台廠供應鏈｜產業熱話｜豐雲學堂2026 年 10 月 - 永豐金證券

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | 0.00 | 0.00% | -2.81% | 2,420.00 | 2,480.00 | -2.42% | 不適用 | 86.28 | 28.05 | 511.86B TWD / 54.65% | 2026-10-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。

### 主要來源

- [Hot Chips 2026重點解析：AI競爭從晶片走向機櫃，台積電、世芯-KY等14檔台廠供應鏈｜產業熱話｜豐雲學堂2026 年 10 月 - 永豐金證券](https://news.google.com/rss/articles/CBMi-gNBVV95cUxQUFV6TGVHbVd6aHlNN3lVZW1KX21mVkZEV0hHQlY4WlBhNVhhQWJJTGlmOHQwS2Nic1pySHp2ZVpaY0w5VHhRbHNMSjdzLWR1Y1NlTHN0b2FTdWlQMk5Pb3d2N01maU1HZGF1V3ZNMzNZR1ZlV056RnVBWnhpckpDeVpaaGUtX0tiZXZOUXdZak5vU1Q1RHM2TUxFUy1xTHRCandoNHBUMldrMkQ2LXFEd1lIUnR0WEhBSGtkbS1FNDh2ZjZ1cGVUSndTYjlMQk5GTFNwZ2x1b2VwTVFPbUxmelZYdlZERTd3R3lTeVpVQlpsNG1xdnlPN0ExVnJPS2JweWJEejFWZm9vb3dTb3d5SjNhSEFTMHJzM1dmUkJ3TjdOTTBhME5GdDFoRUJQTjVhWWdWb3prYUlkeDF3c0thaWU5eUFPUlh4bFl5Rk51cWVEUnNGSHI0NmJKdlZibWZmTEVVM0o0ZlZRcjd0bXZDY2VhanRZdHJJVmVOelE5MGpPNjRfc0JLd2hxdGVQOGpBQ19acFl2UW9MdWR6NDJIMjUyRUhnR0s2dHFGSk14TkJQdHFKRzlOT0luZlZra0I0a2tROGxKc3FCRUhuNkZ0VHVuc2R4NlMzM19yOGNfMndFcHVkcFEwdHp6eDZPc21YcWZGQmdTdHNWdw?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 21 Oct 2026 16:47:02 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：Taiwan Semiconductor Owns The Tollbooth and Helps Me Ignore The AI Financing Noise - 24/7 Wall St.；防堵 AI 代理管帳暴走，新創 Fragment 獲 1,200 萬美元打造專屬防線 - TechNews 科技新報；AI 代理誤刪資料，企業資安如何轉型？ - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | -0.40 | 0.00% | -2.81% | 2,420.00 | 2,480.00 | -2.42% | 未明確 | 86.28 | 28.05 | 511.86B TWD / 54.65% | 2026-10-01 |
| INTC 英特爾 | 產業/供應鏈推估 | -0.08 | -18.94% | N/A | 92.96 | 114.68 | -18.94% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 產業/供應鏈推估 | -0.04 | +0.54% | +10.94% | 221.97 | 228.38 | -2.81% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | -0.03 | +7.10% | N/A | 552.72 | 552.72 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| MSFT 微軟 | 產業/供應鏈推估 | -0.02 | +18.37% | +8.32% | 532.95 | 532.95 | 0.00% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.04 | -8.79% | -10.58% | 337.80 | 446.77 | -24.39% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | -0.02 | +1.94% | -8.43% | 684.00 | 703.00 | -2.70% | 背離 | 13.92 | 49.49 | 88.13B TWD / 45.52% | 2026-10-01 |
| 2454 聯發科 | 產業/供應鏈推估 | -0.04 | -2.59% | -7.49% | 4,140.00 | 4,920.00 | -15.85% | 同向 | 60.69 | 68.37 | 55.40B TWD / 1.97% | 2026-10-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「Taiwan Semiconductor」，共 1 篇新聞命中。 同時符合主題標籤：AI, advanced packaging, CoWoS, AI server。
- INTC：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, CPU, server CPU, x86；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- NVDA：產業/供應鏈推估：公司標籤符合「AI 伺服器與資料中心」關鍵字 AI, artificial intelligence, GPU, datacenter；其中 6 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [Taiwan Semiconductor Owns The Tollbooth and Helps Me Ignore The AI Financing Noise - 24/7 Wall St.](https://news.google.com/rss/articles/CBMixAFBVV95cUxNR1BFREdRMEdMNHpHQmltSWg0RTJUQjFaakZkZ1JxdGFXa05yVmVxVmVIdjJVc2dUZTFJVWRZUGxrell0enk4Q1R6ck5sVFlNOXN3OTdsU0kxRzVXOUJTQWZHZGFaVF9CTUVwNTdaTjlfZ0JwdEpvRzM4Y2NEeVlDZzZpbm5tU3RUbVNmYlZvZTdBNWdiMWlhdjNRdXA5bWdWZ2doZUFnVzFpM2RtVWlKZXpMempabUE4X1ZTd0xucHhhNUdv?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 21 Oct 2026 12:45:00 GMT
- [防堵 AI 代理管帳暴走，新創 Fragment 獲 1,200 萬美元打造專屬防線 - TechNews 科技新報](https://news.google.com/rss/articles/CBMimwFBVV95cUxNYkQwTk84dS1fVzhjMkdTZVJId2FXdi1JdDBEMC1GNEpWSTY0X2xQRFlqeFZiV2VBWjc1THRxQkNFVTV0OGFlc3NEbDZsRGNZOFBRdXY0MG8zZndHTjgxUlBDYVlld29VVGJwT3hHUzVlMm1KRkZlUjRtTUY2bjBKV2JFeWF0NkxFczAwNnQyVUtOa1g0c2pKLXdXOA?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 21 Oct 2026 23:21:53 GMT
- [AI 代理誤刪資料，企業資安如何轉型？ - TechNews 科技新報](https://news.google.com/rss/articles/CBMigAFBVV95cUxQNV83QzZsU3p5dEtsX1FCOW1Bc3ZCdkg0TGtDd2tya2lwTjhKbHl4VXhsWEsxWWJpOWNVQVZpaGlwZDlHYU1CMEVxRGdTOFlnVE02MEpuX1J3RXBZZ0JFQnh2aFdxVldjNTZxZk9HYW54elhHNXJvanJIMGJ0dXpZdA?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 21 Oct 2026 15:45:54 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：AMD, QCOM Targets Raised While INTC, COHR Face Cuts — Susquehanna Sees ‘Modest Upside’ For Chip Earnings - Yahoo Finance；AMD, QCOM Targets Raised While INTC, COHR Face Cuts — Susquehanna Sees ‘Modest Upside’ For Chip Earnings - TradingView；Taiwan Semiconductor Owns The Tollbooth and Helps Me Ignore The AI Financing Noise - 24/7 Wall St.

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | +0.28 | -18.94% | N/A | 92.96 | 114.68 | -18.94% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | +0.56 | +7.10% | N/A | 552.72 | 552.72 | 0.00% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 新聞直接提及 | +0.38 | 0.00% | -2.81% | 2,420.00 | 2,480.00 | -2.42% | 未明確 | 86.28 | 28.05 | 511.86B TWD / 54.65% | 2026-10-01 |
| 3711 日月光投控 | 新聞直接提及 | +0.49 | +1.94% | -8.43% | 684.00 | 703.00 | -2.70% | 同向 | 13.92 | 49.49 | 88.13B TWD / 45.52% | 2026-10-01 |
| 2303 聯電 | 產業/供應鏈推估 | +0.03 | -3.76% | -9.86% | 128.00 | 164.50 | -22.19% | 背離 | 6.68 | 19.25 | 25.35B TWD / 27.22% | 2026-10-01 |
| NVDA 輝達 | 產業/供應鏈推估 | +0.03 | +0.54% | +10.94% | 221.97 | 228.38 | -2.81% | 未明確 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | +0.02 | -5.90% | N/A | 913.67 | 971.00 | -5.90% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | +0.02 | -2.11% | -7.89% | 1,365.38 | 2,335.00 | -41.53% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- INTC：新聞直接提及「INTC」，共 2 篇新聞命中。 同時符合主題標籤：CPU, server CPU, x86, foundry。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 2 篇新聞命中。 同時符合主題標籤：semiconductor, chip。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2330：新聞直接提及「Taiwan Semiconductor」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip, foundry。

### 主要來源

- [AMD, QCOM Targets Raised While INTC, COHR Face Cuts — Susquehanna Sees ‘Modest Upside’ For Chip Earnings - Yahoo Finance](https://news.google.com/rss/articles/CBMimgFBVV95cUxPMVlhVmwtMzY3VXU0T0Y4c0M1MUNpeE9pZE1GaWhBd0pSTTBoWEdJOXJSNVlOMDZRQk9aQ0N5R05VMFlHbUsyUUJfM003Z3d3R0JtTXYtM3ZPZGgwWTVjcTRYQ2QyMDNnZExhNWlHTTlkVV9rQWpnUTgyQ2tCZS0yTEtHbVlHRlE3QTZfM3N3a2V4enZIMlY3NHVn?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 21 Oct 2026 14:30:29 GMT
- [AMD, QCOM Targets Raised While INTC, COHR Face Cuts — Susquehanna Sees ‘Modest Upside’ For Chip Earnings - TradingView](https://news.google.com/rss/articles/CBMi7wFBVV95cUxQMWR4T3Y5ZkV5SWpwRGlmS2p2MkFDZkhwbzBUM3AwZzZRbEVqcVVDYXRHMW40dkdCcllnU1QzUXdBTU9MUWFlUDExN2MwS0h6MXJvLW10Wjk4QUZnZmVpT0hUMkUxcTRZeDJtXzI5Z0R0TXpCcEMya1lKNEkxN2d6MmJ6UWFfdGJCMnU5ekhpaloyLXBkcGtCN25DY2Y0UVM5a0otWk1Kb0FfM3BCRUNRdW4xeUg5RFp3ZjVlcGVRdTgzUm1WckJSenRfSWNIekdseE1KSE9yaUlQT0N2ZllvRWVNOWozSThOd0ktVHphbw?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 21 Oct 2026 14:30:29 GMT
- [Taiwan Semiconductor Owns The Tollbooth and Helps Me Ignore The AI Financing Noise - 24/7 Wall St.](https://news.google.com/rss/articles/CBMixAFBVV95cUxNR1BFREdRMEdMNHpHQmltSWg0RTJUQjFaakZkZ1JxdGFXa05yVmVxVmVIdjJVc2dUZTFJVWRZUGxrell0enk4Q1R6ck5sVFlNOXN3OTdsU0kxRzVXOUJTQWZHZGFaVF9CTUVwNTdaTjlfZ0JwdEpvRzM4Y2NEeVlDZzZpbm5tU3RUbVNmYlZvZTdBNWdiMWlhdjNRdXA5bWdWZ2doZUFnVzFpM2RtVWlKZXpMempabUE4X1ZTd0xucHhhNUdv?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 21 Oct 2026 12:45:00 GMT

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：《台股盤後》收漲594點、47K未站穩，重返5日線- 新聞 - MoneyDJ理財網；台股ETF受益人數破1900萬創高22檔同寫新猷- 新聞 - MoneyDJ理財網；台股ETF受益人數破1900萬創高22檔同寫新猷 - MoneyDJ理財網

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [《台股盤後》收漲594點、47K未站穩，重返5日線- 新聞 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikgFBVV95cUxPNGlRUkJpUERzbnJPN1RBM0toZVZTX0VWX2QxeVNuWFFaZ1cydUpRR3hVU2JsNTJZUkdxalk5VTFqVXI0REJHZU5wdG9iQUx6QjNCUDItcU5JTU5WaW1lNmlZb1ZDTndaY2laUUtUU3dCbG9FNTNFUEs0N2gxeXlaMlA5X3FQVXZQWVpsT0hYWDZNZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 21 Oct 2026 07:55:00 GMT
- [台股ETF受益人數破1900萬創高22檔同寫新猷- 新聞 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMikgFBVV95cUxPekx0QU11RE5jTXo4bW9yb2pYQjRkVDRXTXdpZXVmMFdoTTNKQkdRR0hTVDNwelBkTU12ZkZobk1nWUJKUHFtTjRSVFZZcW9wSmduU3JKeEhyTEVCYTFZUHo0SGNlbnctVEQtdUdDUndhOUtwNzVWTndvbzBldUFVRU1uNWxYLTl3NDJkZGxqeWN4QQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 21 Oct 2026 04:32:00 GMT
- [台股ETF受益人數破1900萬創高22檔同寫新猷 - MoneyDJ理財網](https://news.google.com/rss/articles/CBMiiwFBVV95cUxQSkkyNENQOGJURF9WcGdxYmhWQXUwTjRQWS1TQ2pvM0VNMk1WUWNlUnZMM3puQmJzblplOVVjOEk4cXZXR0xpTHJIS3JJeEdSMVk2S2s2TGEwZ05ETXN0cTdodlcyang3cDQyLWxIOHVnUFZtem9SU2NYRDgzU3RHc0N4VjV1Yk4zd3Zv?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 21 Oct 2026 04:32:00 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：個股動態報導內容-A87BAFE9-F216-47B4-98F2-CDC1735B0E2A - MoneyDJ；個股動態報導內容-90A26515-6C3E-4CCB-95BB-4424ECD811B3 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [個股動態報導內容-A87BAFE9-F216-47B4-98F2-CDC1735B0E2A - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxPck5aSHp4dFdJcWo2elRzdHNZWUNRNUtCQ2dHc3VuN2dnQUxhVFd3M05PMkUzQkhJQlRwRllpSmdUeFJldFlldnRycHVvYlVHMTV4X0t3TEtyb0pzRm9BZks5cWROVXlBa2ZldnVpLVZFZnUtZVR2MXJCelA5MlpRemp3Wi01RF9IWjBHb0tXLTJNdVoy?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 21 Oct 2026 06:32:01 GMT
- [個股動態報導內容-90A26515-6C3E-4CCB-95BB-4424ECD811B3 - MoneyDJ](https://news.google.com/rss/articles/CBMilAFBVV95cUxQR1RIU1pEWm1jb3FjTkN1Qlc2aUNScEZGODFBWTlfWU1BdTFLNDBDYTYxWFowT1RadmlIb1ZTMUZZZU9QR3lqV2w4OXVjMmNSQzFNbFVtYWhIeXB5SkkyWnhDV3hDdnVIZ1NmUnRsNk11eWYyeXhlem94bk5TT0FSVVhKbU5BTy01d1JWTW1BUnBGcnha?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 21 Oct 2026 00:54:33 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
