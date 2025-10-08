@echo off
title MSFS 2020 Cache Cleaner - EXE Builder
echo.
echo ================================================
echo    Building .EXE for MSFS Cache Cleaner
echo ================================================
echo.

:: Check Python
python --version >nul 2>&1
if %errorLevel% neq 0 (
    echo [ERROR] Python is not installed!
    pause
    exit /b 1
)

:: Install PyInstaller
echo [INFO] Checking PyInstaller...
pip show pyinstaller >nul 2>&1
if %errorLevel% neq 0 (
    echo [INFO] Installing PyInstaller...
    pip install pyinstaller
    if %errorLevel% neq 0 (
        echo [ERROR] Cannot install PyInstaller
        pause
        exit /b 1
    )
)

:: Install dependencies
echo [INFO] Installing dependencies...
pip install psutil

:: Create .exe file
echo [INFO] Building .exe file...
echo This may take several minutes...
echo.

pyinstaller --onefile --windowed --name "MSFS2020_Cache_Cleaner" --add-data "README.md;." --icon=icon.ico MSFS2020_Cache_Cleaner.py

if %errorLevel% == 0 (
    echo.
    echo [SUCCESS] .exe file created in 'dist' folder
    echo.
    echo You can now share the file:
    echo dist\MSFS2020_Cache_Cleaner.exe
    echo.
    echo The .exe file does not require Python installation!
) else (
    echo.
    echo [ERROR] Error occurred while creating .exe
)

echo.
pause
