if (-Not (Test-Path ".venv")) {
    Write-Host ">>> No .venv folder found. Run: python -m venv .venv"
    exit 1
}

Write-Host ">>> Activating virtual environment (.venv)"
.\.venv\Scripts\Activate.ps1
