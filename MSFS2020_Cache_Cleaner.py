import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import os
import shutil
import subprocess
import threading
import time
from datetime import datetime
import psutil

class MSFS2020CacheCleaner:
    def __init__(self, root):
        self.root = root
        self.root.title("MSFS 2020 Professional Cache Cleaner v2.0")
        self.root.geometry("800x600")
        self.root.configure(bg='#1e1e1e')
        
        # Control variables
        self.clean_temp = tk.BooleanVar(value=True)
        self.clean_nvidia = tk.BooleanVar(value=True)
        self.clean_msfs = tk.BooleanVar(value=True)
        self.clean_dx = tk.BooleanVar(value=True)
        
        self.setup_styles()
        self.create_widgets()
        self.log("MSFS 2020 Cache Cleaner started successfully")
        
    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        # Dark theme
        style.configure('Dark.TLabel', background='#1e1e1e', foreground='#ffffff', font=('Segoe UI', 10))
        style.configure('Title.TLabel', background='#1e1e1e', foreground='#00ff88', font=('Segoe UI', 16, 'bold'))
        style.configure('Dark.TFrame', background='#1e1e1e')
        style.configure('Dark.TCheckbutton', background='#1e1e1e', foreground='#ffffff', font=('Segoe UI', 10))
        style.configure('Green.TButton', background='#00aa44', foreground='white', font=('Segoe UI', 11, 'bold'))
        style.configure('Red.TButton', background='#cc3333', foreground='white', font=('Segoe UI', 11, 'bold'))
        style.configure('Blue.TButton', background='#0066cc', foreground='white', font=('Segoe UI', 11, 'bold'))
        
    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, style='Dark.TFrame')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title_label = ttk.Label(main_frame, text="MSFS 2020 Professional Cache Cleaner", style='Title.TLabel')
        title_label.pack(pady=(0, 20))
        
        # Options frame
        options_frame = ttk.LabelFrame(main_frame, text="Cleaning Options", style='Dark.TFrame')
        options_frame.pack(fill=tk.X, pady=(0, 20))
        
        ttk.Checkbutton(options_frame, text="Windows Temporary Files", variable=self.clean_temp, style='Dark.TCheckbutton').pack(anchor=tk.W, padx=10, pady=5)
        ttk.Checkbutton(options_frame, text="NVIDIA Cache (DXCache, GLCache)", variable=self.clean_nvidia, style='Dark.TCheckbutton').pack(anchor=tk.W, padx=10, pady=5)
        ttk.Checkbutton(options_frame, text="MSFS 2020 Cache (all locations)", variable=self.clean_msfs, style='Dark.TCheckbutton').pack(anchor=tk.W, padx=10, pady=5)
        ttk.Checkbutton(options_frame, text="DirectX Shader Cache", variable=self.clean_dx, style='Dark.TCheckbutton').pack(anchor=tk.W, padx=10, pady=5)
        
        # Buttons frame
        buttons_frame = ttk.Frame(main_frame, style='Dark.TFrame')
        buttons_frame.pack(fill=tk.X, pady=(0, 20))
        
        ttk.Button(buttons_frame, text="Scan Cache Size", command=self.scan_cache_size, style='Blue.TButton').pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(buttons_frame, text="Clean Cache", command=self.start_cleaning, style='Green.TButton').pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(buttons_frame, text="Close MSFS", command=self.close_msfs, style='Red.TButton').pack(side=tk.LEFT)
        
        # Progress bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(main_frame, variable=self.progress_var, maximum=100)
        self.progress_bar.pack(fill=tk.X, pady=(0, 10))
        
        # Status label
        self.status_label = ttk.Label(main_frame, text="Ready to work", style='Dark.TLabel')
        self.status_label.pack(pady=(0, 10))
        
        # Logs
        log_frame = ttk.LabelFrame(main_frame, text="Operation Logs", style='Dark.TFrame')
        log_frame.pack(fill=tk.BOTH, expand=True)
        
        self.log_text = scrolledtext.ScrolledText(log_frame, bg='#2d2d2d', fg='#ffffff', font=('Consolas', 9))
        self.log_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
    def log(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        self.log_text.insert(tk.END, log_entry)
        self.log_text.see(tk.END)
        self.root.update_idletasks()
        
    def close_msfs(self):
        self.log("Checking MSFS 2020 processes...")
        processes_closed = 0
        
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                if 'flightsimulator' in proc.info['name'].lower() or 'msfs' in proc.info['name'].lower():
                    proc.terminate()
                    processes_closed += 1
                    self.log(f"Closed process: {proc.info['name']}")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
                
        if processes_closed == 0:
            self.log("No active MSFS 2020 processes found")
        else:
            self.log(f"Closed {processes_closed} MSFS 2020 processes")
            time.sleep(2)
            
    def get_cache_locations(self):
        username = os.getenv('USERNAME')
        locations = {}
        
        if self.clean_temp.get():
            locations['temp'] = [
                os.path.expandvars(r'%TEMP%'),
                os.path.expandvars(r'%TMP%'),
                r'C:\Windows\Temp'
            ]
            
        if self.clean_nvidia.get():
            locations['nvidia'] = [
                f'C:\\Users\\{username}\\AppData\\Local\\NVIDIA\\DXCache',
                f'C:\\Users\\{username}\\AppData\\Local\\NVIDIA\\GLCache',
                f'C:\\Users\\{username}\\AppData\\LocalLow\\NVIDIA\\PerDriverVersion\\DXCache'
            ]
            
        if self.clean_msfs.get():
            locations['msfs'] = [
                f'C:\\Users\\{username}\\AppData\\Local\\Packages\\Microsoft.FlightSimulator_8wekyb3d8bbwe\\LocalCache',
                f'C:\\Users\\{username}\\AppData\\Local\\Packages\\Microsoft.FlightSimulator_8wekyb3d8bbwe\\AC',
                f'C:\\Users\\{username}\\AppData\\Roaming\\Microsoft Flight Simulator\\Cache',
                f'C:\\Users\\{username}\\Documents\\My Games\\Microsoft Flight Simulator\\Cache'
            ]
            
        if self.clean_dx.get():
            locations['directx'] = [
                f'C:\\Users\\{username}\\AppData\\Local\\D3DSCache'
            ]
            
        return locations
        
    def calculate_folder_size(self, folder_path):
        total_size = 0
        if os.path.exists(folder_path):
            for dirpath, dirnames, filenames in os.walk(folder_path):
                for filename in filenames:
                    try:
                        filepath = os.path.join(dirpath, filename)
                        total_size += os.path.getsize(filepath)
                    except (OSError, FileNotFoundError):
                        pass
        return total_size
        
    def format_size(self, size_bytes):
        if size_bytes == 0:
            return "0 B"
        size_names = ["B", "KB", "MB", "GB", "TB"]
        import math
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return f"{s} {size_names[i]}"
        
    def scan_cache_size(self):
        def scan_thread():
            self.status_label.config(text="Scanning cache sizes...")
            locations = self.get_cache_locations()
            total_size = 0
            
            for category, paths in locations.items():
                category_size = 0
                for path in paths:
                    size = self.calculate_folder_size(path)
                    category_size += size
                    
                total_size += category_size
                self.log(f"Category {category}: {self.format_size(category_size)}")
                
            self.log(f"TOTAL SIZE TO CLEAN: {self.format_size(total_size)}")
            self.status_label.config(text=f"Scan completed: {self.format_size(total_size)}")
            
        threading.Thread(target=scan_thread, daemon=True).start()
        
    def clean_folder(self, folder_path):
        deleted_size = 0
        deleted_files = 0
        
        if not os.path.exists(folder_path):
            return deleted_size, deleted_files
            
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            try:
                if os.path.isfile(item_path):
                    size = os.path.getsize(item_path)
                    os.remove(item_path)
                    deleted_size += size
                    deleted_files += 1
                elif os.path.isdir(item_path):
                    folder_size = self.calculate_folder_size(item_path)
                    shutil.rmtree(item_path)
                    deleted_size += folder_size
                    deleted_files += 1
            except (PermissionError, FileNotFoundError, OSError) as e:
                self.log(f"Cannot delete {item_path}: {str(e)}")
                
        return deleted_size, deleted_files
        
    def start_cleaning(self):
        def cleaning_thread():
            if not any([self.clean_temp.get(), self.clean_nvidia.get(), self.clean_msfs.get(), self.clean_dx.get()]):
                messagebox.showwarning("Warning", "Select at least one cleaning option!")
                return
                
            result = messagebox.askyesno("Confirmation", 
                                       "Are you sure you want to clean the selected cache?\n\n"
                                       "This operation is irreversible!")
            if not result:
                return
                
            self.status_label.config(text="Cleaning in progress...")
            self.progress_var.set(0)
            
            locations = self.get_cache_locations()
            total_categories = len(locations)
            current_category = 0
            
            total_deleted_size = 0
            total_deleted_files = 0
            
            for category, paths in locations.items():
                self.log(f"Cleaning category: {category.upper()}")
                
                for path in paths:
                    if os.path.exists(path):
                        self.log(f"   Cleaning: {path}")
                        deleted_size, deleted_files = self.clean_folder(path)
                        total_deleted_size += deleted_size
                        total_deleted_files += deleted_files
                        
                        if deleted_files > 0:
                            self.log(f"   Deleted {deleted_files} items ({self.format_size(deleted_size)})")
                        else:
                            self.log(f"   Folder already clean")
                    else:
                        self.log(f"   Folder does not exist: {path}")
                        
                current_category += 1
                progress = (current_category / total_categories) * 100
                self.progress_var.set(progress)
                
            self.progress_var.set(100)
            self.log(f"CLEANING COMPLETED!")
            self.log(f"Total result: {total_deleted_files} items, {self.format_size(total_deleted_size)} freed space")
            self.status_label.config(text=f"Completed: {self.format_size(total_deleted_size)} freed")
            
            messagebox.showinfo("Success!", 
                              f"Cleaning completed!\n\n"
                              f"Deleted: {total_deleted_files} items\n"
                              f"Freed: {self.format_size(total_deleted_size)}")
            
        threading.Thread(target=cleaning_thread, daemon=True).start()

def main():
    # Check administrator privileges
    try:
        import ctypes
        is_admin = ctypes.windll.shell32.IsUserAnAdmin()
        if not is_admin:
            messagebox.showwarning("Warning", 
                                 "Application works better with administrator privileges.\n"
                                 "Some files may not be accessible for cleaning.")
    except:
        pass
    
    root = tk.Tk()
    app = MSFS2020CacheCleaner(root)
    
    # Application icon (optional)
    try:
        root.iconbitmap('icon.ico')
    except:
        pass
    
    root.mainloop()

if __name__ == "__main__":
    main()
