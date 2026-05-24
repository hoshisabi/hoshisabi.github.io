#!/usr/bin/env pwsh
# Pull the latest changes from both the public site and the private DM notes repo.

$site = Split-Path $PSScriptRoot
$dm   = Join-Path (Split-Path $site) "hoshisabi-dm"

Push-Location $site
git pull
Write-Host "[site] up to date" -ForegroundColor Green
Pop-Location

Push-Location $dm
git pull
Write-Host "[dm] up to date" -ForegroundColor Green
Pop-Location
