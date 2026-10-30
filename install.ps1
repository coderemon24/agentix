# Agentix (agx) — One-Line Windows Installer
# Usage: irm https://raw.githubusercontent.com/coderemon24/agentix/main/install.ps1 | iex

Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host "  Installing Agentix (agx) in: $PWD" -ForegroundColor Cyan
Write-Host "======================================================================" -ForegroundColor Cyan

$zipUrl = "https://github.com/coderemon24/agentix/archive/refs/heads/main.zip"
$tempZip = "$env:TEMP\agentix-main.zip"
$tempExtract = "$env:TEMP\agentix-extract"

try {
    Write-Host "--> Downloading Agentix bundle from GitHub..." -ForegroundColor Yellow
    Invoke-WebRequest -Uri $zipUrl -OutFile $tempZip -UseBasicParsing

    if (Test-Path $tempExtract) { Remove-Item -Recurse -Force $tempExtract }
    Write-Host "--> Extracting Agentix files..." -ForegroundColor Yellow
    Expand-Archive -Path $tempZip -DestinationPath $tempExtract -Force

    $sourceDir = "$tempExtract\agentix-main"

    # Folders to copy
    $folders = @(".agents", "scripts", "tests\visual-qa", ".cursor", ".github")
    foreach ($f in $folders) {
        $src = "$sourceDir\$f"
        if (Test-Path $src) {
            $dest = "$PWD\$f"
            New-Item -ItemType Directory -Force -Path $dest | Out-Null
            Copy-Item -Path "$src\*" -Destination $dest -Recurse -Force
        }
    }

    # Root files to copy
    $files = @(
        "agx.cmd", "agentix.cmd", "agx", "agentix",
        "AGENTS.md", "USER_MANUAL.md", "CLAUDE.md",
        ".cursorrules", ".windsurfrules", "CONVENTIONS.md",
        "ui-refactor.md", "UI-Mandatory.md", "gitcommit.md"
    )
    foreach ($f in $files) {
        $src = "$sourceDir\$f"
        if (Test-Path $src) {
            Copy-Item -Path $src -Destination "$PWD\$f" -Force
        }
    }

    # Clean up temp
    Remove-Item -Force $tempZip -ErrorAction SilentlyContinue
    Remove-Item -Recurse -Force $tempExtract -ErrorAction SilentlyContinue

    # Register Global CLI in npm bin if available
    $npmDir = "$env:APPDATA\npm"
    if (Test-Path $npmDir) {
        Copy-Item -Path "$PWD\agx.cmd" -Destination "$npmDir\agx.cmd" -Force -ErrorAction SilentlyContinue
        Copy-Item -Path "$PWD\agentix.cmd" -Destination "$npmDir\agentix.cmd" -Force -ErrorAction SilentlyContinue
        Write-Host "--> Registered global CLI command 'agx' in: $npmDir" -ForegroundColor Cyan
    }

    Write-Host "--> Initializing Git branches and worktrees..." -ForegroundColor Yellow
    python scripts\agx.py init

    Write-Host "======================================================================" -ForegroundColor Green
    Write-Host "  [SUCCESS] Agentix (agx) installed successfully!" -ForegroundColor Green
    Write-Host "  Run 'agx st' to check team status." -ForegroundColor Green
    Write-Host "======================================================================" -ForegroundColor Green
}
catch {
    Write-Host "[ERROR] Installation failed: $_" -ForegroundColor Red
    exit 1
}

