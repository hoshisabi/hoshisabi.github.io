#!/usr/bin/env pwsh
# Commit and push public site changes.

param([string]$Message)

$root = Split-Path $PSScriptRoot

Push-Location $root
git status --short
if (git status --porcelain) {
    if (-not $Message) { $Message = Read-Host "Commit message" }
    git add .
    git commit -m $Message
    git push
    Write-Host "[site] pushed" -ForegroundColor Green
} else {
    Write-Host "[site] nothing to commit" -ForegroundColor DarkGray
}
Pop-Location
