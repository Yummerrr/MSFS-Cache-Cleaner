@echo off
title MSFS 2020 Cache Cleaner - Automatic Launcher
echo.
echo ================================================
echo    MSFS 2020 Professional Cache Cleaner v2.0
echo ================================================
echo.

:: Check administrator privileges
net session >nul 2>&1
if %errorLevel% == 0 (
    echo [INFO] Running with administrator privileges - Perfect!
) else (
    echo [WARNING] No administrator privileges!
    echo Some files may not be accessible for cleaning.
    echo.
    pause
)

:: Check if Python is installed
echo [INFO] Checking Python installation...
python --version >nul 2>&1
if %errorLevel% neq 0 (
    echo [ERROR] Python is not installed!
    echo.
    echo Download Python from: https://www.python.org/downloads/
    echo Check "Add Python to PATH" option during installation
    echo.
    pause
    exit /b 1
)

:: Check required modules
echo [INFO] Checking required modules...
python -c "import tkinter, psutil" >nul 2>&1
if %errorLevel% neq 0 (
    echo [INFO] Installing required modules...
    pip install psutil
    if %errorLevel% neq 0 (
        echo [ERROR] Cannot install psutil module
        echo Try running: pip install psutil
        pause
        exit /b 1
    )
)

:: Launch application
echo [INFO] Starting MSFS 2020 Cache Cleaner...
echo.
python "%~dp0MSFS2020_Cache_Cleaner.py"

if %errorLevel% neq 0 (
    echo.
    echo [ERROR] Error occurred while starting application
    pause
)
