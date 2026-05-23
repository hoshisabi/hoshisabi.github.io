#!/usr/bin/env pwsh
# Pull the latest public site changes and DM notes from their respective repos.

$root = Split-Path $PSScriptRoot

Push-Location $root
git pull
git submodule update --remote rpg/icewind-dale/dm
Write-Host "[done] site and dm notes up to date" -ForegroundColor Green
Pop-Location
