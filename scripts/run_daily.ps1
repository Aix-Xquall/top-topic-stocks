param(
    [string]$ReportDate = (Get-Date -Format "yyyy-MM-dd"),
    [string]$PythonExe = "python"
)

$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $ProjectRoot

& $PythonExe -m market_topics run --date $ReportDate

