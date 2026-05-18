# Heart Disease Prediction Dashboard - PowerShell Launcher
# This script activates the Python environment and launches the Streamlit app

Write-Host "========================================================" -ForegroundColor Cyan
Write-Host " Heart Disease Prediction Dashboard - Streamlit App" -ForegroundColor Cyan
Write-Host "========================================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed
try {
    python --version | Out-Null
} catch {
    Write-Host "Error: Python is not installed or not in PATH" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Create virtual environment if it doesn't exist
if (-not (Test-Path "streamlit_env")) {
    Write-Host "Creating virtual environment..." -ForegroundColor Yellow
    python -m venv streamlit_env
    Write-Host "Virtual environment created." -ForegroundColor Green
}

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& "streamlit_env\Scripts\Activate.ps1"

# Install/upgrade dependencies
Write-Host "Installing required packages..." -ForegroundColor Yellow
pip install -q -r requirements.txt

# Launch Streamlit app
Write-Host ""
Write-Host "========================================================" -ForegroundColor Cyan
Write-Host " Launching Heart Disease Prediction Dashboard..." -ForegroundColor Cyan
Write-Host "========================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "The app will open at: http://localhost:8501" -ForegroundColor Green
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host ""

streamlit run streamlit_app.py

Read-Host "Press Enter to exit"
