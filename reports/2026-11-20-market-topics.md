# 每日股市熱門話題分析 - 2026-11-20

本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。

## 重點摘要

1. **綜合市場情緒**｜負向｜熱度 41｜市場確認 85.57｜同向 1/1
2. **半導體與晶片供應鏈**｜負向｜熱度 3｜市場確認 100.00｜同向 8/8
3. **散熱與液冷供應鏈**｜中性｜熱度 7｜市場確認 N/A｜同向 0/0
4. **AI 伺服器與資料中心**｜中性｜熱度 16｜市場確認 N/A｜同向 0/0
5. **新興題材：BigGo**｜中性｜熱度 1｜市場確認 N/A｜同向 0/0

## 市場驗證

為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。

- 3日相關係數：-0.35（樣本 13）
- 5日相關係數：-0.36（樣本 10）
- 同向比例：9/13

| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 綜合市場情緒 | 85.57 | 1/1 | 0 | +5.19% | +10.26% |
| 半導體與晶片供應鏈 | 100.00 | 8/8 | 0 | +17.76% | +7.21% |
| 散熱與液冷供應鏈 | N/A | 0/0 | 0 | N/A | N/A |
| AI 伺服器與資料中心 | N/A | 0/0 | 0 | N/A | N/A |
| 新興題材：BigGo | N/A | 0/0 | 0 | N/A | N/A |
| 關稅與供應鏈轉移 | 0.00 | 0/1 | 1 | -36.08% | -27.28% |
| 記憶體與 HBM 供應鏈 | 0.00 | 0/3 | 3 | -23.88% | -23.36% |
| 新興題材：MoneyDJ | N/A | 0/0 | 0 | N/A | N/A |

### 方法調整建議

- 方向信心與股價呈負相關；應檢查正負向詞庫，並降低新聞直接提及但股價背離的權重。

## 每日迭代追蹤

此表用來觀察每日模型分數是否逐步貼近市場表現。

| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |
| --- | ---: | ---: | ---: | ---: |
| 2026-11-06 | -0.18 | 0.77 | +100.00% | 5 |
| 2026-11-08 | -0.21 | 0.03 | +23.08% | 13 |
| 2026-11-09 | -0.56 | -0.62 | +60.00% | 10 |
| 2026-11-10 | -0.32 | 0.24 | +3.45% | 29 |
| 2026-11-11 | 0.34 | -0.26 | +46.67% | 15 |
| 2026-11-12 | -0.09 | 0.07 | +50.00% | 14 |
| 2026-11-13 | -0.56 | 0.42 | +54.17% | 24 |
| 2026-11-14 | -0.34 | 0.12 | +42.11% | 19 |
| 2026-11-15 | -0.02 | 0.62 | +50.00% | 20 |
| 2026-11-16 | -0.30 | -0.27 | +38.89% | 18 |
| 2026-11-17 | 0.44 | 0.39 | +80.00% | 15 |
| 2026-11-18 | 0.27 | -0.38 | +86.36% | 22 |
| 2026-11-19 | 0.20 | -0.23 | +69.57% | 23 |
| 2026-11-20 | -0.35 | -0.36 | +69.23% | 13 |

## 歷史回測摘要

- 回測日期：2026-11-20
- 近5日 3日相關：0.28
- 近5日 5日相關：0.30
- 同向比例：+68.97%
- 權重狀態：已調整

- 方向準確度：+68.97%
- 信心排序準確度：0.28
- 診斷：正相關

調整原因：近 5 日信心分數與後續報酬呈正相關，提高市場確認、歷史題材與直接提及權重。；關鍵詞×公司後續樣本有效 0 筆，未達 30 筆，不調整樣本權重

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

## 綜合市場情緒

摘要：綜合市場情緒 相關新聞集中在：台股又跌！金管會加碼限空令 平盤下放空、借券賣出再收緊 - 經濟日報；台股4萬點誰在撐？國安基金連三天護盤都在買什麼？個股、張數一次看 | 金融脈動 | 金融 - 經濟日報；美亞股市殺聲四起！台股一度跌逾1,600點失守37K 台達電、信驊重挫 | 市場焦點 | 證券 - 經濟日報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | -0.45 | -5.19% | -10.26% | 2,010.00 | 2,480.00 | -18.95% | 同向 | 98.27 | 21.37 | 586.89B TWD / 59.71% | 2026-11-01 |

關聯理由（前 3）：
- 2330：新聞直接提及「台積電」，共 1 篇新聞命中。 方向判斷命中詞：重挫。

### 主要來源

- [台股又跌！金管會加碼限空令 平盤下放空、借券賣出再收緊 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBpdng0NjBqN2dIdm1JVHVTbkRrbUpOeTdWRFpxVHcyaFpfN2lJRFBRZkdCbm8wX3JqcTV2RXF0ajZQQ0lSbk9yU21XcTcwWDdvMEY2anF6Z1lyd9IBX0FVX3lxTE9JMWtVRUlLZ2JlR0hSNm1mMElELWpqa0ttcDVFajFSZnRPMmc4MHJLc0RTbVNPOHlHblctOUxvczZ6YzhBVGxoeXBBSV8tRWNCQkhFLUtaUjdLU3V1ZjlN?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 19 Nov 2026 06:42:23 GMT
- [台股4萬點誰在撐？國安基金連三天護盤都在買什麼？個股、張數一次看 | 金融脈動 | 金融 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE04eXJZUlZzQWxBbGV0MTlOcEpTaG1Lb0NTWkdJRFRlZTVIY1Q1T0JYeHRoS0xSWjlwSktSZ21IV3VNUkxiNVB3emJsRzVlT3FZbThnQUdnLUgydw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 18 Nov 2026 20:46:42 GMT
- [美亞股市殺聲四起！台股一度跌逾1,600點失守37K 台達電、信驊重挫 | 市場焦點 | 證券 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9iczYzS055dE42eTBacGVoV0VkM09FdjFFb2FWZThjdWNPalpTNFljclNZYm1peDVmNjZ6Z0RaSURJU091R19vS2tNZlRPdmJMSk1HaHowMThpZw?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 19 Nov 2026 08:00:00 GMT

## 半導體與晶片供應鏈

摘要：半導體與晶片供應鏈 相關新聞集中在：台股崩跌逾2,000點探七個月低檔 半導體三雄全面重挫 - 經濟日報；TSMC tightens China AI chip curbs as new US rules close manufacturing loophole, sources say - Reuters；AI半導體股遭大舉拋售！日經早盤崩逾2700點失守57000點 韓股跌逾4%摔落5000點之下 - 鉅亨網

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 2330 台積電 | 新聞直接提及 | -0.51 | -5.19% | -10.26% | 2,010.00 | 2,480.00 | -18.95% | 同向 | 98.27 | 21.37 | 586.89B TWD / 59.71% | 2026-11-01 |
| INTC 英特爾 | 產業/供應鏈推估 | -0.07 | -51.41% | +37.38% | 55.72 | 114.68 | -51.41% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| 2303 聯電 | 產業/供應鏈推估 | -0.04 | -7.35% | -12.67% | 80.10 | 164.50 | -51.31% | 同向 | 6.80 | 13.03 | 25.20B TWD / 18.33% | 2026-11-01 |
| NVDA 輝達 | 產業/供應鏈推估 | -0.03 | -36.08% | -27.28% | 145.98 | 228.38 | -36.08% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 產業/供應鏈推估 | -0.03 | -5.21% | N/A | 489.19 | 516.10 | -5.21% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 產業/供應鏈推估 | -0.03 | -28.89% | N/A | 690.44 | 971.00 | -28.89% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 產業/供應鏈推估 | -0.03 | -6.67% | -19.45% | 94.39 | 291.88 | -67.66% | 同向 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | -0.03 | -1.29% | -10.95% | 346.65 | 446.77 | -22.41% | 同向 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 2330：新聞直接提及「TSMC」，共 1 篇新聞命中。 同時符合主題標籤：semiconductor, chip, foundry。
- INTC：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 CPU, server CPU, x86, foundry；其中 1 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2303：產業/供應鏈推估：公司標籤符合「半導體與晶片供應鏈」關鍵字 semiconductor, foundry, chip；其中 1 篇新聞出現相關標籤。

### 主要來源

- [台股崩跌逾2,000點探七個月低檔 半導體三雄全面重挫 - 經濟日報](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9OUjhiaFNfc0dwZjB0M1hRLVB5ME9kUkgzMVdjOE8wOERPUmVsSUNVd0tCSkh2VkJqLWJLT1FqMGJXaDRkNi1JbWhBUkZBWXNmMWR1dndNUFd5UdIBX0FVX3lxTE12bDFqUHdycTRLaDlDTFFWSEg2bm5BdDJXUW44ZFdZUkl0V3Q2ZXYzSHJyT0pYZEJUVzhzTko4SHh0MUtGTk5aSUJLV0QzZlhuZlFrTlBvZzZSSzlMVkpV?oc=5) - https://news.google.com/rss/search?q=site%3Amoney.udn.com%20%E8%AD%89%E5%88%B8%20OR%20%E5%8F%B0%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 19 Nov 2026 08:00:00 GMT
- [TSMC tightens China AI chip curbs as new US rules close manufacturing loophole, sources say - Reuters](https://news.google.com/rss/articles/CBMiwAFBVV95cUxNc1pDUGRULVJNeGdkT21ERVNzMEl6RHJKTEtLRWFFQjFpYjdxWU5NMmM3Zl8zUzlHQUd3UzJlNE1UV2tlZnZFTEZrNnRKSWU1Y1lkSU1ISmF6U1JGNWNEeUJETVpHNDI5QTEwMWJTTmRraUgyaDR2RUJ1UlRadVJZMW9MUTZCeXdpZHRZRWl1X1VIZ0xBbllSWEUxMGxmdmllVFgxbmxuTmljOFFBTUkyUGR2NDRfTmM0Rm5xcXFxaHk?oc=5) - https://news.google.com/rss/search?q=site%3Areuters.com%20markets%20OR%20stocks%20OR%20earnings%20OR%20semiconductor%20OR%20AI%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 19 Nov 2026 12:48:00 GMT
- [AI半導體股遭大舉拋售！日經早盤崩逾2700點失守57000點 韓股跌逾4%摔落5000點之下 - 鉅亨網](https://news.google.com/rss/articles/CBMiT0FVX3lxTE9nZExzdmo0ME9XbnlnekU0X2RIbDA3SEtBUEVXX0k4elhmTFdqRmNCa05fU1k3b2JtbW5HU3U2WDhYbW05WGVUbFMtZnl6M2M?oc=5) - Google News source discovery | 鉅亨網 Fri, 20 Nov 2026 01:07:17 GMT

## 散熱與液冷供應鏈

摘要：散熱與液冷供應鏈 相關新聞集中在：輝達財報佳散熱需求夯：奇鋐| 雜誌 - UDN；《DJ在線》輝達換代若放緩，散熱廠布局受考驗 - 台視全球資訊網；奇鋐新舊平台並行，明年首季續爬坡 - 新聞 - MoneyDJ

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 3017 奇鋐 | 新聞直接提及 | 0.00 | -10.77% | -11.89% | 2,205.00 | 3,435.00 | -35.81% | 不適用 | 90.78 | 27.03 | 22.10B TWD / 34.35% | 2026-11-01 |
| NVDA 輝達 | 新聞直接提及 | 0.00 | -36.08% | -27.28% | 145.98 | 228.38 | -36.08% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- 3017：新聞直接提及「奇鋐、散熱」，共 5 篇新聞命中。 同時符合主題標籤：thermal。
- NVDA：新聞直接提及「輝達」，共 4 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [輝達財報佳散熱需求夯：奇鋐| 雜誌 - UDN](https://news.google.com/rss/articles/CBMiUEFVX3lxTE9TSmFJTm5ZLTA1UUU3d3J6SmRHZG9ua1hVLXRFVFNfZFRBd3R3cU9oZkdCMkNLV3UxQVI1SlBYRXpjU3JTSW51djJvY3pPM3Iz?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 19 Nov 2026 06:23:29 GMT
- [《DJ在線》輝達換代若放緩，散熱廠布局受考驗 - 台視全球資訊網](https://news.google.com/rss/articles/CBMinAFBVV95cUxQcjhOczk0eFVzSVZsSlkxWWpodHZyM0JMMk56aGthZHh6RnNnNm96SG03Yllob01EakZRNzZ1SmZENGFDeGpVd21MSXl5alpxRHlLTXZTSk9MbENqSC1oY3FHQ0tvUXduVWFnV05DTm1uTmxMNjkwWkN4R3VFeFFWUy12SU9pbnFVcFdLdC0zaTVUeHQ2UVNWNm56Vng?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 19 Nov 2026 05:20:13 GMT
- [奇鋐新舊平台並行，明年首季續爬坡 - 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxNaHJtVVBkbmNHOUhSS0s0MUx5UUwya1UzZk1EUjY1Y2dMVlM5emVpNkdlTmdGR3NlTUpDc1M5dHpnQUJoNTVUNUxWRjA0d1BtdzBMenppeHJMa0JTTWlubHVqTC1QWldkMXpCeVpkVWJLTkRjRkRrY1NTQ3doQUhEc2VMSTB3aUlZWEVJeE5hVFdWUQ?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 18 Nov 2026 04:03:00 GMT

## AI 伺服器與資料中心

摘要：AI 伺服器與資料中心 相關新聞集中在：AMD Is Down 8% After Short Seller Hunterbrook Ties AMD's Firmware to Blacklisted Chinese Server Maker; Resilient Intel Remains Up 5% - 24/7 Wall St.；AI ASIC 與 TPU 動能強勁，大摩喊聯發科目標價 6,188 元 - TechNews 科技新報；將算力轉化成應用力！叡揚攜手企業迎接 AI 代理創造商業價值 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| INTC 英特爾 | 新聞直接提及 | 0.00 | -51.41% | +37.38% | 55.72 | 114.68 | -51.41% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AMD 超微 | 新聞直接提及 | 0.00 | -5.21% | N/A | 489.19 | 516.10 | -5.21% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2454 聯發科 | 新聞直接提及 | 0.00 | -1.98% | -3.38% | 3,390.00 | 4,920.00 | -31.10% | 不適用 | 62.35 | 59.84 | 55.03B TWD / 5.77% | 2026-11-01 |
| NVDA 輝達 | 產業/供應鏈推估 | 0.00 | -36.08% | -27.28% | 145.98 | 228.38 | -36.08% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2330 台積電 | 產業/供應鏈推估 | 0.00 | -5.19% | -10.26% | 2,015.00 | 2,480.00 | -18.75% | 不適用 | 98.27 | 21.37 | 586.89B TWD / 59.71% | 2026-11-01 |
| MSFT 微軟 | 產業/供應鏈推估 | 0.00 | +10.67% | +1.28% | 498.30 | 507.29 | -1.77% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| AVGO 博通 | 產業/供應鏈推估 | 0.00 | -1.29% | -10.95% | 346.65 | 446.77 | -22.41% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 3711 日月光投控 | 產業/供應鏈推估 | 0.00 | -8.36% | -13.99% | 463.50 | 703.00 | -34.07% | 不適用 | 17.55 | 28.93 | 88.62B TWD / 47.13% | 2026-11-01 |

關聯理由（前 3）：
- INTC：新聞直接提及「Intel」，共 1 篇新聞命中。 同時符合主題標籤：AI, CPU, server CPU, x86。 方向判斷命中詞：恐, 強勁。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AMD：新聞直接提及「AMD」，共 1 篇新聞命中。 同時符合主題標籤：AI, GPU, datacenter, AI server。 方向判斷命中詞：恐, 強勁。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2454：新聞直接提及「聯發科」，共 1 篇新聞命中。 同時符合主題標籤：AI。 方向判斷命中詞：恐, 強勁。

### 主要來源

- [AMD Is Down 8% After Short Seller Hunterbrook Ties AMD's Firmware to Blacklisted Chinese Server Maker; Resilient Intel Remains Up 5% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMigAJBVV95cUxNdzd0czNoRHhWV3NBazdxMDZFQ0tLcWtObmF2UXRSLTBReGpORWJ4UkxpWDBZSUxqQ2YwNEFaNEEzSF9VRVZjQjU2UUE3dTlPUWhCRnBObm9IOXJrYjNhOHhXUnJSNTJzOE9ZZTNsNDBsdXc2ZkpmZ0J1NHF2MmdGaWlDdjBIZkMtRTRNQzZuWnY5YXNQZlI2MGJWOWNSemRHdzJEYXZyYkhaNWhBWEh5cHJTRkJCRzBXY191NVRFRGhlbTJaWS0yVldjaEd0LXNudnhPa2FGaExCdU5LUEl3ek5WdTBsMXRtMXluV1pYLUpIWmpuWHNOTGx2ZG81T3hT?oc=5) - https://news.google.com/rss/search?q=AMD%20Intel%20INTC%20stock%20AI%20chip%20earnings%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 19 Nov 2026 16:06:00 GMT
- [AI ASIC 與 TPU 動能強勁，大摩喊聯發科目標價 6,188 元 - TechNews 科技新報](https://news.google.com/rss/articles/CBMilgFBVV95cUxPb3V5Nm9PVHJ3X2RHLW5McnBxRmtHN0xkUUI1OHJ4bjRyWVhsYlVHaXY4VFJIaDBaSmRDTFBQRzFiWmhoakc0d3FpRjdDa0xxU3ZHYzlEdElLaVVkUEtrdXRmLVlNV2VVOVlHbE0wWUplcXh1MzhQbXduTm9JSmc5UlNuSVpHaThNS2IyV0E1bU56QzlMSWc?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 20 Nov 2026 01:15:06 GMT
- [將算力轉化成應用力！叡揚攜手企業迎接 AI 代理創造商業價值 - TechNews 科技新報](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE1Rc3lNekFRVElHVmNGV3pxUzNzLW9tNmh1OEZ4VmptOFdBeGRCTUF4V0JqdUVZSDhfdjhEU3M0RUN0dEEzdDJJMER1UWVKX1NGbE1SZVFZNnhfTG5vWTNMV2gzajhlWDg?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 20 Nov 2026 01:20:06 GMT

## 新興題材：BigGo

摘要：新興題材：BigGo 相關新聞集中在：Micron and Sandisk Gain as Nvidia Results Lift Memory Demand Outlook; Applied Optoelectronics Slides on $550 Million Equity Program - BigGo Finance

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | 0.00 | -36.08% | -27.28% | 145.98 | 228.38 | -36.08% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| MU 美光 | 新聞直接提及 | 0.00 | -28.89% | N/A | 690.44 | 971.00 | -28.89% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | 0.00 | -6.67% | -19.45% | 94.39 | 291.88 | -67.66% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- MU：新聞直接提及「Micron」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 1 篇新聞命中。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。

### 主要來源

- [Micron and Sandisk Gain as Nvidia Results Lift Memory Demand Outlook; Applied Optoelectronics Slides on $550 Million Equity Program - BigGo Finance](https://news.google.com/rss/articles/CBMidkFVX3lxTE1oMVZLZk5Mb3ZtSi1zZUEwYnR4aXZoR1ZWMUdsWHQ0Qjlwa1liMGpMdEJLSExocUNVQVRKZThxdlFVMDFxTl9TbGpNUVlsRm1OTjlkbmZESlhld3pfRWhfejkwMFdZbzUzWVRrOUY3Sm1VVTZGU3c?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 18 Nov 2026 14:25:00 GMT

## 關稅與供應鏈轉移

摘要：關稅與供應鏈轉移 相關新聞集中在：整理包／黃仁勳概念股笑了！輝達季度財報超預期 完整台廠供應鏈名單、潛在受惠股一次看 - 經濟日報；美國擴大東南亞 AI 晶片出口管制，AI 伺服器出貨結構將依終端客戶重新調整 - TechNews 科技新報

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| NVDA 輝達 | 新聞直接提及 | +0.23 | -36.08% | -27.28% | 145.98 | 228.38 | -36.08% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| AAPL 蘋果 | 產業/供應鏈推估 | 0.00 | +11.90% | +25.23% | 349.21 | 349.21 | 0.00% | 不適用 | N/A | N/A | N/A USD / N/A | N/A |
| 2317 鴻海 | 產業/供應鏈推估 | 0.00 | +0.92% | -8.13% | 211.50 | 289.00 | -26.82% | 不適用 | 16.57 | 13.34 | 1305.32B TWD / 45.73% | 2026-11-01 |

關聯理由（前 3）：
- NVDA：新聞直接提及「輝達」，共 1 篇新聞命中。 方向判斷命中詞：受惠。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- AAPL：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 tariff, supply chain；其中 0 篇新聞出現相關標籤。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- 2317：產業/供應鏈推估：公司標籤符合「關稅與供應鏈轉移」關鍵字 supply chain, tariff；其中 0 篇新聞出現相關標籤。

### 主要來源

- [整理包／黃仁勳概念股笑了！輝達季度財報超預期 完整台廠供應鏈名單、潛在受惠股一次看 - 經濟日報](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBQUlViSHpPeDVlY29yaHFNNE5NcVlUQnE3ZThTcXRGNHgxYTVPOVVTRDlaTDV6Zml5WEwxVHNSeGFDcnVHUHhRSW15SzNpU0dYVDU3dThWNEVCbkZI?oc=5) - https://news.google.com/rss/search?q=%E5%A5%87%E9%8B%90%20%E8%BC%9D%E9%81%94%20%E6%95%A3%E7%86%B1%20Rubin%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Wed, 18 Nov 2026 08:00:00 GMT
- [美國擴大東南亞 AI 晶片出口管制，AI 伺服器出貨結構將依終端客戶重新調整 - TechNews 科技新報](https://news.google.com/rss/articles/CBMi2gFBVV95cUxORzctUXU4YlFtWldBMkp5M1drQVVyVnJSR3dJMEZjalRQQkpDaWhKUzRtNkw1THpPZ3REN1VicUJPMVdzQzhlX29ocDF6X1BaYWo1bFdZeTQ5ZXF4cDlQR1NKTnY0eWZWLTNuSGY4YmFWdUNKSW5ULWQzSVVjMGZWOEU1S2NQdUlUSV9lZ013cWQway1aMmxFNFdma1Z0Z1ZsTlBGTkU2ZHYwTUtyV01BOHYzaW9SRC01NmFYOWlrMXdtLTVmQTk1QXpaYWd3SzZfUEJ2RUV5QUhXUQ?oc=5) - https://news.google.com/rss/search?q=site%3Atechnews.tw%20%E5%8D%8A%E5%B0%8E%E9%AB%94%20OR%20AI%20OR%20%E6%99%B6%E7%89%87%20OR%20%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D%20when%3A3d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 19 Nov 2026 23:04:34 GMT

## 記憶體與 HBM 供應鏈

摘要：記憶體與 HBM 供應鏈 相關新聞集中在：SanDisk and Micron Rise 4% as Anthropic's Record IPO Revives the AI Trade; Western Digital Gains 5% - 24/7 Wall St.；Not Micron, Not Sandisk. This Is My Top Memory Stock for 2027. - Yahoo Finance；Micron’s Next $100 Billion Growth Opportunity Could Surprise Wall Street - 24/7 Wall St.

### 相關公司

| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| MU 美光 | 新聞直接提及 | +0.30 | -28.89% | N/A | 690.44 | 971.00 | -28.89% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| SNDK SanDisk | 新聞直接提及 | +0.30 | -6.67% | -19.45% | 94.39 | 291.88 | -67.66% | 背離 | N/A | N/A | N/A USD / N/A | N/A |
| NVDA 輝達 | 新聞直接提及 | +0.23 | -36.08% | -27.28% | 145.98 | 228.38 | -36.08% | 背離 | N/A | N/A | N/A USD / N/A | N/A |

關聯理由（前 3）：
- MU：新聞直接提及「Micron」，共 6 篇新聞命中。 同時符合主題標籤：AI memory, memory, HBM, HBM4。 方向判斷命中詞：growth。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。
- SNDK：新聞直接提及「SanDisk」，共 4 篇新聞命中。 同時符合主題標籤：NAND, SSD, flash memory, memory。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。
- NVDA：新聞直接提及「NVIDIA」，共 1 篇新聞命中。 同時符合主題標籤：HBM。
  - 資料備註：未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。；未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。

### 主要來源

- [SanDisk and Micron Rise 4% as Anthropic's Record IPO Revives the AI Trade; Western Digital Gains 5% - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi1gFBVV95cUxNLVFybjd3ZGJ4R2x2VVA0VjYtc3RFd3JCbFVWdC1QQWZRTUhyOUtTMnotbE1mTjJ0RGFMZlZvVzFySWd3T25yYnNmeFlGTWx2SGpHVW1YLXZONFhpMVAtOGYxSzktSTg4N0ZYNTduMkg0SFdMNFFCMGRrNU1FLWlJa1BMeExUc3RRaEs5bnVLallfSzhCaGdPaGxnUk9kcHpKVElINlAzQktWQUZ4Y2M0My11SGNBajc1NTU1VV9pTmpNTXphR3VMeTNWMUlXaTR4VkJDdnpn?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 19 Nov 2026 14:11:00 GMT
- [Not Micron, Not Sandisk. This Is My Top Memory Stock for 2027. - Yahoo Finance](https://news.google.com/rss/articles/CBMilgFBVV95cUxQNUtEWE45Si14U3NjVmpheXdPT3dpaXNvMDlDU09pTXJRd2NFZGg3T0hRblVyMnFoR2Y2WjVCM3JDSFh2OGVjTG1lYjFkblNJVk91SGZaNVBHdnN3TVhmekJsSnBDbXY0WkRtM1JHUW1YRnVYMVJENEEwcXdwOUFrSHJWbEpHLXk0MmhENGg1NzVmdzJJX0E?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Wed, 18 Nov 2026 19:21:02 GMT
- [Micron’s Next $100 Billion Growth Opportunity Could Surprise Wall Street - 24/7 Wall St.](https://news.google.com/rss/articles/CBMitAFBVV95cUxQQ09zV1JoYWdDdXJpZ0xHZE1wMWJ5R3N6LU5yQ21uZkJMTXcyemVWV1dEVTVfY255VDdOYnZkY3lkLTNhY0JQMzk2bGUtdWlxV3FlN21LMmYyaE12ZHVIUl9BR01GMEZQSlJJaHlNcjFEQ21qdVVTOU1vUnBYdTZtdnBEclp4RUZZUE1CUERNSG9ZNWpheHI4Vm91ZkpIWDFtckVEMXRQaE1PQ0czZERGVVlVSXc?oc=5) - https://news.google.com/rss/search?q=Micron%20MU%20SanDisk%20SNDK%20HBM%20memory%20AI%20stock%20when%3A3d&hl=en-US&gl=US&ceid=US:en Thu, 19 Nov 2026 17:04:00 GMT

## 新興題材：MoneyDJ

摘要：新興題材：MoneyDJ 相關新聞集中在：統一證券：台股中長期技術面偏弱勢- 新聞 - MoneyDJ；美股指數期貨最新報價 - MoneyDJ；《台股盤後》量縮重挫1768點，失守年線-新聞內容-基金 - MoneyDJ

### 相關公司

目前沒有足夠依據推估相關公司。

### 主要來源

- [統一證券：台股中長期技術面偏弱勢- 新聞 - MoneyDJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxQeWlveGstRUhLdllvQkt1Ri1QSm9iY3RUZ2Fja3NoWnFTUXJScDBUNzFVaHVCWDVRQy14bE02QlhFWGNmdlVndXBkRDdnZmEyZklPSEpYV3ZXbTlaMlc1Y1NDaEJMV182RnUxeFkxR1h3S05zV1lvdE5nX0cxNmJUeWtCQkhyY0hmc2NESjBKc19CUQ?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 20 Nov 2026 00:46:00 GMT
- [美股指數期貨最新報價 - MoneyDJ](https://news.google.com/rss/articles/CBMiigFBVV95cUxNcnRSZHoyemYwWU51R2JBRm5HaEtyN05OUWdieWY2RmgtUVdsQlNFYUNWVGVTZVNiOFVRS1BXTzlvMVdxOXcwQWZFU2FndWR2TkwyYlVvX0lyR2F3cjY0QUlBTFduMTBJblFwYVZmbXlMdXU5UTJFWC1wNDRxNTJ1Z19OaHU3RXhyT1E?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Fri, 20 Nov 2026 01:49:39 GMT
- [《台股盤後》量縮重挫1768點，失守年線-新聞內容-基金 - MoneyDJ](https://news.google.com/rss/articles/CBMikAFBVV95cUxNamlFYy1XWEtFcVJIdkpjQkZQUUdDN1RiY3V1M2NISHFMaGtwMkVsc21QN0p0MUJmbU5lT0ZpZEMzMVF3ZjFIX3pWTmIxeWdDdUQ5VGFUdFVKQXlFMWJ6U2psVXIyQzE3WFBvUERteGY2eHJWYWtIZTc1WHBGMEFsMFhUaHVRU0RXRDJEX2w4Mzg?oc=5) - https://news.google.com/rss/search?q=site%3Amoneydj.com%20%E5%8F%B0%E8%82%A1%20OR%20%E5%80%8B%E8%82%A1%20when%3A7d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant Thu, 19 Nov 2026 08:11:00 GMT

## 資料缺口與需人工確認

- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=intl-markets，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=news，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=research，原因：HTTP Error 404: Not Found
- RSS 抓取失敗：https://tw.stock.yahoo.com/rss?category=tw-market，原因：HTTP Error 404: Not Found
