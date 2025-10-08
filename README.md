# MSFS 2020 Professional Cache Cleaner v1.0

## Description
Advanced mod/tool for cleaning Microsoft Flight Simulator 2020 cache files, designed specifically for Windows 11 v24H2.

## Features
- **Windows Temporary Files Cleaning**
- **NVIDIA Cache Cleaning** (DXCache, GLCache)
- **MSFS 2020 Cache Cleaning** (all locations)
- **DirectX Shader Cache Cleaning**
- **Cache Size Scanning** before cleaning
- **Safe Deletion** with error handling
- **Modern Dark Interface**
- **Detailed Operation Logs**
- **Automatic MSFS Closing**

## Installation

### Method 1: Automatic (recommended)
1. Download all files to one folder
2. Right-click on `Run_MSFS_Cleaner.bat`
3. Select "Run as administrator"
4. Script will automatically check and install requirements

### Method 2: Manual
1. Install Python 3.8+ from python.org
2. Open command prompt as administrator
3. Run: `pip install psutil`
4. Run: `python MSFS2020_Cache_Cleaner.py`

### Method 3: .exe file
1. Run `Build_EXE.bat` as administrator
2. .exe file will be created in `dist` folder
3. Run `MSFS2020_Cache_Cleaner.exe` (no Python required)

## Cleaned Locations

### Temporary Files:
- `%TEMP%` - user temporary folder
- `%TMP%` - alternative temporary folder
- `C:\Windows\Temp` - system temporary folder

### NVIDIA Cache:
- `AppData\Local\NVIDIA\DXCache`
- `AppData\Local\NVIDIA\GLCache`
- `AppData\LocalLow\NVIDIA\PerDriverVersion\DXCache`

### MSFS 2020 Cache:
- `AppData\Local\Packages\Microsoft.FlightSimulator_*\LocalCache`
- `AppData\Local\Packages\Microsoft.FlightSimulator_*\AC`
- `AppData\Roaming\Microsoft Flight Simulator\Cache`
- `Documents\My Games\Microsoft Flight Simulator\Cache`

### DirectX:
- `AppData\Local\D3DSCache`

## Usage

1. **Scanning** - Check how much space can be freed
2. **Option Selection** - Check categories to clean
3. **Close MSFS** - Automatically closes simulator
4. **Cleaning** - Start cleaning process
5. **Monitoring** - Watch progress in logs

## Important Information

- **Run as administrator** for full functionality
- **Close MSFS 2020** before cleaning
- **Backup important data** before use
- **First launch** after cleaning may take longer

## System Requirements

- Windows 11 v24H2 (recommended)
- Python 3.8+ (for .py version)
- Administrator privileges
- 100MB free disk space

## Benefits

- **Increased Performance** - eliminates stutters
- **Faster Loading** - fresh cache loads more efficiently
- **More Space** - removes gigabytes of unnecessary files
- **Better Stability** - eliminates conflicts after updates
- **Automation** - one click instead of manual cleaning

## When to Use

- After each MSFS 2020 update
- After NVIDIA driver updates
- When experiencing game performance issues
- Regularly every 1-2 weeks for performance maintenance
- When running low on disk space

## Troubleshooting

**"Python not found"**
- Download from python.org and check "Add to PATH"

**"No permissions"**
- Run as administrator

**"psutil module not found"**
- Run: `pip install psutil`

**"Cannot delete file"**
- Close all programs using the files
- Restart as administrator

---
**Version:** 1.0  
**Compatibility:** Windows 11 v24H2  
**Language:** English  
**License:** Professional Use
About v2.0
MSFS 2020 Professional Cache Cleaner v2.0 brings a modern, user-friendly dark interface and enhanced reliability for Windows 11, supporting efficient cleaning of MSFS 2020 cache, NVIDIA cache, temp files, and DirectX shader cache—with automatic MSFS closing and full log history.

Planned for Future Versions
Automatic Scheduled Cleaning: Set automatic cache cleaning at regular intervals

Full Steam Version Support: Expand compatibility with both Microsoft Store and Steam editions

One-Click Backup: Safely back up cache folders before cleaning

Multi-language UI: English, Polish, and more languages in settings

Advanced Cleaning Filters: Select specific cache/types to clean

Performance Analytics: Display game load times before and after cleaning

Notifications: Get alerts when cleaning is completed or when errors are detected

Command Line Mode: Use in scripts/automation tasks

Cloud Sync: Save and sync preferences

