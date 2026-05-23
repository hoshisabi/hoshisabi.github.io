#!/usr/bin/env pwsh
# Commit and push DM notes to the private repo, then update the public pointer.

param([string]$Message)

$root = Split-Path $PSScriptRoot
$dm   = Join-Path $root "rpg\icewind-dale\dm"

# 1. Push DM notes to private repo
Push-Location $dm
if (git status --porcelain) {
    if (-not $Message) { $Message = Read-Host "DM commit message" }
    git add .
    git commit -m $Message
    git push
    Write-Host "[dm] pushed to private repo" -ForegroundColor Green
} else {
    Write-Host "[dm] nothing to commit" -ForegroundColor DarkGray
}
Pop-Location

# 2. Update the public repo's submodule pointer if it changed
Push-Location $root
git add rpg/icewind-dale/dm
git diff --cached --quiet -- rpg/icewind-dale/dm
if ($LASTEXITCODE -ne 0) {
    git commit -m "chore: update dm submodule"
    git push
    Write-Host "[site] pointer updated" -ForegroundColor Green
}
Pop-Location
