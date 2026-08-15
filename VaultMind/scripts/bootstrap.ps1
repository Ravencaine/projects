# Bootstrap script for VaultMind on Windows 11.
# Idempotent: safe to run multiple times.
#
# What it does:
#   1. Verifies prerequisites (Python 3.12, ffmpeg, Tesseract, Ollama, Rust).
#   2. Creates .venv and installs requirements-dev.txt.
#   3. Creates vault/ subdirectories.
#   4. Pulls Ollama models.
#   5. Downloads the OpenVINO Whisper IR model.
#   6. (Optional) Installs the cargo tauri CLI.
#
# Usage:
#   pwsh -ExecutionPolicy Bypass -File scripts\bootstrap.ps1
#   pwsh -ExecutionPolicy Bypass -File scripts\bootstrap.ps1 -SkipOllama
#   pwsh -ExecutionPolicy Bypass -File scripts\bootstrap.ps1 -Force

[CmdletBinding()]
param(
    [switch]$SkipOllama,
    [switch]$SkipWhisper,
    [switch]$Force,
    [switch]$SkipRust
)

$ErrorActionPreference = "Stop"
$ProgressPreference    = "SilentlyContinue"

# --------------------------------------------------------------------- #
# Paths
# --------------------------------------------------------------------- #

$ScriptDir   = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoRoot    = Resolve-Path (Join-Path $ScriptDir "..")
$VenvDir     = Join-Path $RepoRoot ".venv"
$ModelsDir   = Join-Path $RepoRoot "models"
$WhisperDir  = Join-Path $ModelsDir "whisper"
$VaultDir    = Join-Path $RepoRoot "vault"
$WhisperRepo = "OpenVINO/distil-whisper-large-v3-int4-ov"
$WhisperPath = Join-Path $WhisperDir "distil-whisper-large-v3-int4-ov"

function Log($msg) { Write-Host "[bootstrap] $msg" -ForegroundColor Cyan }
function Warn($msg) { Write-Host "[bootstrap] WARN: $msg" -ForegroundColor Yellow }
function Err($msg)  { Write-Host "[bootstrap] ERROR: $msg" -ForegroundColor Red; exit 1 }

# --------------------------------------------------------------------- #
# 1. Prerequisite checks
# --------------------------------------------------------------------- #

Log "Checking prerequisites..."

# Python 3.12
$python = (Get-Command py -ErrorAction SilentlyContinue) ?? (Get-Command python -ErrorAction SilentlyContinue) ?? (Get-Command python3 -ErrorAction SilentlyContinue)
if (-not $python) {
    Err "Python not found in PATH. Install Python 3.12: winget install Python.Python.3.12"
}
$pyVer = & $python.Source -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')"
if ($pyVer -ne "3.12") {
    Warn "Found Python $pyVer. VaultMind targets 3.12 exactly. Continuing — install 3.12 if you hit issues."
}

# ffmpeg
if (-not (Get-Command ffmpeg -ErrorAction SilentlyContinue)) {
    Warn "ffmpeg not found. Install: winget install Gyan.FFmpeg"
}

# Tesseract (only required if you ingest images / scanned PDFs)
if (-not (Get-Command tesseract -ErrorAction SilentlyContinue)) {
    Warn "Tesseract not found. Optional unless you ingest images / scanned PDFs. Install: winget install UB-Mannheim.TesseractOCR"
}

# Ollama
$ollama = Get-Command ollama -ErrorAction SilentlyContinue
if (-not $ollama) {
    Warn "Ollama not found. Install from https://ollama.com/download (or winget install Ollama.Ollama)."
}

# Rust toolchain
if (-not $SkipRust) {
    if (-not (Get-Command cargo -ErrorAction SilentlyContinue)) {
        Warn "Rust toolchain not found. Install: winget install Rustlang.Rustup"
    }
}

Log "Prerequisite check complete."

# --------------------------------------------------------------------- #
# 2. .venv + requirements
# --------------------------------------------------------------------- #

if ((Test-Path $VenvDir) -and -not $Force) {
    Log "Virtual environment already exists at $VenvDir (use -Force to recreate)."
} else {
    if ($Force -and (Test-Path $VenvDir)) {
        Log "Removing existing .venv..."
        Remove-Item -Recurse -Force $VenvDir
    }
    Log "Creating virtual environment at $VenvDir..."
    & $python.Source -m venv $VenvDir
}

Log "Installing requirements-dev.txt..."
& (Join-Path $VenvDir "Scripts\python.exe") -m pip install --upgrade pip | Out-Null
& (Join-Path $VenvDir "Scripts\python.exe") -m pip install -r (Join-Path $RepoRoot "requirements-dev.txt")

# --------------------------------------------------------------------- #
# 3. Vault directories
# --------------------------------------------------------------------- #

Log "Creating vault/ subdirectories..."
New-Item -ItemType Directory -Force -Path (Join-Path $VaultDir "downloads") | Out-Null
New-Item -ItemType Directory -Force -Path (Join-Path $VaultDir "audio")     | Out-Null
New-Item -ItemType Directory -Force -Path (Join-Path $VaultDir ".cache")    | Out-Null
New-Item -ItemType Directory -Force -Path (Join-Path $ModelsDir "whisper")  | Out-Null

# --------------------------------------------------------------------- #
# 4. Ollama models
# --------------------------------------------------------------------- #

if ($SkipOllama) {
    Log "Skipping Ollama model pull (-SkipOllama)."
} elseif ($ollama) {
    Log "Pulling Ollama models (qwen2.5:7b-instruct-q4_K_M, nomic-embed-text)..."
    & ollama pull qwen2.5:7b-instruct-q4_K_M
    & ollama pull nomic-embed-text
} else {
    Warn "Ollama not installed; skipping model pull. Run 'ollama pull qwen2.5:7b-instruct-q4_K_M' manually after install."
}

# --------------------------------------------------------------------- #
# 5. OpenVINO Whisper model
# --------------------------------------------------------------------- #

if ($SkipWhisper) {
    Log "Skipping OpenVINO Whisper download (-SkipWhisper)."
} else {
    if ((Test-Path $WhisperPath) -and -not $Force) {
        Log "OpenVINO Whisper model already present at $WhisperPath."
    } else {
        Log "Downloading OpenVINO Whisper IR ($WhisperRepo)..."
        Log "This is ~750 MB; will take a few minutes."
        & (Join-Path $VenvDir "Scripts\python.exe") -m pip install --quiet "huggingface-hub>=0.24"
        & (Join-Path $VenvDir "Scripts\python.exe") -c @"
from huggingface_hub import snapshot_download
import os
path = snapshot_download(
    repo_id="$WhisperRepo",
    local_dir=r"$WhisperPath",
    local_dir_use_symlinks=False,
)
print("Downloaded to:", path)
"@
    }
}

# --------------------------------------------------------------------- #
# 6. cargo tauri CLI
# --------------------------------------------------------------------- #

if (-not $SkipRust) {
    if (Get-Command cargo -ErrorAction SilentlyContinue) {
        $tauriInstalled = cargo install --list 2>$null | Select-String "tauri-cli"
        if (-not $tauriInstalled) {
            Log "Installing cargo tauri-cli (Tauri 2.x)..."
            cargo install tauri-cli --version "^2.0" --locked
        } else {
            Log "cargo tauri-cli already installed."
        }
    }
}

# --------------------------------------------------------------------- #
# Summary
# --------------------------------------------------------------------- #

Log "Bootstrap complete."
Log ""
Log "Next steps:"
Log "  Terminal 1: uvicorn backend.main:app --port 8765 --reload"
Log "  Terminal 2: cargo tauri dev"
Log ""
Log "Verify with: python scripts/verify_phase0.py"