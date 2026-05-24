#!/usr/bin/env pwsh
# Commit and push DM notes to the private repo.

param([string]$Message)

$dm = Join-Path (Split-Path (Split-Path $PSScriptRoot)) "hoshisabi-dm"

Push-Location $dm
if (git status --porcelain) {
    if (-not $Message) { $Message = Read-Host "DM commit message" }
    git add .
    git commit -m $Message
    git push
    Write-Host "[dm] pushed" -ForegroundColor Green
} else {
    Write-Host "[dm] nothing to commit" -ForegroundColor DarkGray
}
Pop-Location
