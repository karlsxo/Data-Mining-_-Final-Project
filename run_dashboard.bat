@echo off
REM Heart Disease Prediction Dashboard - Launcher Script
REM This script activates the Python environment and launches the Streamlit app

echo.
echo ========================================================
echo  Heart Disease Prediction Dashboard - Streamlit App
echo ========================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    pause
    exit /b 1
)

REM Create virtual environment if it doesn't exist
if not exist "streamlit_env" (
    echo Creating virtual environment...
    python -m venv streamlit_env
    echo Virtual environment created.
)

REM Activate virtual environment
echo Activating virtual environment...
call streamlit_env\Scripts\activate.bat

REM Install/upgrade dependencies
echo Installing required packages...
pip install -q -r requirements.txt

REM Launch Streamlit app
echo.
echo ========================================================
echo  Launching Heart Disease Prediction Dashboard...
echo ========================================================
echo.
echo The app will open at: http://localhost:8501
echo Press Ctrl+C to stop the server
echo.

streamlit run streamlit_app.py

pause
