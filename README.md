# MSFS 2020 Professional Cache Cleaner

🛩️ **Professional cache cleaning tool for Microsoft Flight Simulator 2020**

[![Windows](https://img.shields.io/badge/Windows-11%20v24H2-blue?logo=windows)](https://www.microsoft.com/windows)
[![Python](https://img.shields.io/badge/Python-3.8+-green?logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![MSFS](https://img.shields.io/badge/MSFS-2020%2F2024-blue?logo=microsoft)](https://flightsimulator.com)

## 📖 Description

Advanced mod/tool for cleaning Microsoft Flight Simulator 2020 cache files, designed specifically for Windows 11 v24H2. This professional-grade utility helps maintain optimal performance by cleaning temporary files, NVIDIA cache, MSFS cache, and DirectX shader cache with a modern, user-friendly interface.

## ✨ Features

- 🗑️ **Windows Temporary Files Cleaning**
- 🎮 **NVIDIA Cache Cleaning** (DXCache, GLCache)
- ✈️ **MSFS 2020 Cache Cleaning** (all locations)
- 🎯 **DirectX Shader Cache Cleaning**
- 📊 **Cache Size Scanning** before cleaning
- 🔒 **Safe Deletion** with error handling
- 🎨 **Modern Dark Interface**
- 📝 **Detailed Operation Logs**
- ⚡ **Automatic MSFS Closing**

## 🚀 Installation

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

## 📁 Cleaned Locations

### 🗂️ Temporary Files:
- `%TEMP%` - user temporary folder
- `%TMP%` - alternative temporary folder
- `C:\Windows\Temp` - system temporary folder

### 🎮 NVIDIA Cache:
- `AppData\Local\NVIDIA\DXCache`
- `AppData\Local\NVIDIA\GLCache`
- `AppData\LocalLow\NVIDIA\PerDriverVersion\DXCache`

### ✈️ MSFS 2020 Cache:
- `AppData\Local\Packages\Microsoft.FlightSimulator_*\LocalCache`
- `AppData\Local\Packages\Microsoft.FlightSimulator_*\AC`
- `AppData\Roaming\Microsoft Flight Simulator\Cache`
- `Documents\My Games\Microsoft Flight Simulator\Cache`

### 🎯 DirectX:
- `AppData\Local\D3DSCache`

## 🎮 Usage

1. **Scanning** - Check how much space can be freed
2. **Option Selection** - Check categories to clean
3. **Close MSFS** - Automatically closes simulator
4. **Cleaning** - Start cleaning process
5. **Monitoring** - Watch progress in logs

## 🖥️ System Requirements

| Requirement | Minimum | Recommended |
|-------------|---------|-------------|
| **OS** | Windows 10 | Windows 11 v24H2 |
| **Python** | 3.8+ | 3.11+ |
| **RAM** | 2GB | 4GB+ |
| **Storage** | 100MB free | 500MB+ free |
| **Privileges** | User | Administrator |

## 📈 Performance Benefits

- **🚀 Increased Performance** - eliminates stutters
- **⚡ Faster Loading** - fresh cache loads more efficiently
- **💾 More Space** - removes gigabytes of unnecessary files
- **🛡️ Better Stability** - eliminates conflicts after updates
- **🔄 Automation** - one click instead of manual cleaning

## 🕐 When to Use

- After each MSFS 2020 update
- After NVIDIA driver updates
- When experiencing game performance issues
- Regularly every 1-2 weeks for performance maintenance
- When running low on disk space

## 🗺️ Roadmap & Future Versions

### Version 1.0 (Current)
**MSFS 2020 Professional Cache Cleaner v1.0** brings a modern, user-friendly dark interface and enhanced reliability for Windows 11, supporting efficient cleaning of MSFS 2020 cache, NVIDIA cache, temp files, and DirectX shader cache—with automatic MSFS closing and full log history.

### Version 2.0+ (Planned Features)
- **🕒 Automatic Scheduled Cleaning** - Set automatic cache cleaning at regular intervals
- **🎮 Full Steam Version Support** - Expand compatibility with both Microsoft Store and Steam editions
- **💾 One-Click Backup** - Safely back up cache folders before cleaning
- **🌍 Multi-language UI** - English, Polish, and more languages in settings
- **🔧 Advanced Cleaning Filters** - Select specific cache types to clean
- **📊 Performance Analytics** - Display game load times before and after cleaning
- **🔔 Notifications** - Get alerts when cleaning is completed or when errors are detected
- **⌨️ Command Line Mode** - Use in scripts/automation tasks
- **☁️ Cloud Sync** - Save and sync preferences across devices

## 🛠️ Troubleshooting

<details>
<summary><strong>"Python not found"</strong></summary>

**Solution:**
1. Download Python from [python.org](https://python.org)
2. During installation, check ✅ **"Add Python to PATH"**
3. Restart command prompt and try again
</details>

<details>
<summary><strong>"No permissions"</strong></summary>

**Solution:**
1. Right-click application/batch file
2. Select **"Run as administrator"**
3. Click "Yes" on UAC prompt
</details>

<details>
<summary><strong>"psutil module not found"</strong></summary>

**Solution:**
```bash
pip install psutil
# or
python -m pip install psutil
```
</details>

<details>
<summary><strong>"Cannot delete file"</strong></summary>

**Solution:**
1. Close Microsoft Flight Simulator completely
2. Use "Close MSFS" button in application
3. Restart application as administrator
</details>

## ⚠️ Important Information

- **Run as administrator** for full functionality
- **Close MSFS 2020** before cleaning
- **Backup important data** before use
- **First launch** after cleaning may take longer

---

**Version:** 1.0  
**Compatibility:** Windows 11 v24H2  
**Language:** English (Multi-language support planned)  
**License:** Professional Use

---

⭐ **If this tool helped improve your MSFS experience, please star the repository!**

**Made with ❤️ for the flight simulation community**
