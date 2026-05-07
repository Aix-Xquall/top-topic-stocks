# 每日股市熱門話題中文分析系統

這是一個免費資料源優先的 Python MVP，用來每日產生繁體中文 Markdown/HTML 報告：

- 分析美股與台股熱門市場話題
- 推估可能相關公司
- 補上 EPS、本益比、營收、營收 YoY 與資料來源
- 明確標示「新聞直接提及」或「產業/供應鏈推估」

> 本工具只做研究輔助，不提供買賣建議。

## 快速開始

```powershell
python -m market_topics run --date 2026-05-07
```

輸出檔案：

- `reports/2026-05-07-market-topics.md`
- `reports/2026-05-07-market-topics.html`

若想完全離線測試：

```powershell
python -m market_topics run --date 2026-05-07 --offline-sample
```

## 可選環境變數

```powershell
$env:ALPHAVANTAGE_API_KEY="你的 Alpha Vantage key"
$env:FINMIND_TOKEN="你的 FinMind token"
$env:SEC_USER_AGENT="你的名稱 your-email@example.com"
```

沒有 API key 時，系統會跳過對應資料源並在報告「資料缺口」列出原因。

## 專案結構

```text
market_topics/
  collectors/     新聞、美股、台股資料抓取
  analysis/       話題聚類與公司關聯評分
  reporting/      中文 Markdown/HTML 報告
config/
  company_universe.csv
  topic_keywords.json
  rss_feeds.txt
reports/
tests/
```

## 測試

```powershell
python -m unittest discover -s tests
```

## GitHub Actions 每日自動執行

建議建立 public GitHub repository：

- Repository name: `top-topic-stocks`
- Description: `Top topic (Stocks)`
- GitHub Pages source: `GitHub Actions`

本專案已包含 `.github/workflows/daily-market-topics.yml`，排程為台北時間每日 06:00：

```yaml
cron: "0 22 * * *"
```

Workflow 會執行：

1. 跑單元測試。
2. 產生當日 Markdown、HTML 與 JSON 摘要。
3. Commit `reports/`。
4. 部署 GitHub Pages。
5. 透過 LINE Messaging API push 今日摘要。

HTML 報告網址格式：

```text
https://<github-user>.github.io/top-topic-stocks/reports/YYYY-MM-DD-market-topics.html
```

## LINE Messaging API Secrets

請在 GitHub repo 的 `Settings > Secrets and variables > Actions` 設定：

```text
LINE_CHANNEL_ACCESS_TOKEN
LINE_TO
```

可選 secrets：

```text
SEC_USER_AGENT
ALPHAVANTAGE_API_KEY
FINMIND_TOKEN
```

`LINE_CHANNEL_ACCESS_TOKEN` 請使用 LINE Developers 後台重新發行後的 token。不要把 token 或 userId 寫進 repo。

若要本機測試通知，可先產生報告，再執行：

```powershell
python -m market_topics notify-line --date 2026-05-07 --report-url "https://<github-user>.github.io/top-topic-stocks/reports/2026-05-07-market-topics.html"
```

如果缺少 LINE secrets，指令會略過通知，不會影響報告產生。
