import os
import shutil
import json
import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk

# Function to handle folder and file selection dialogs
def select_folder(var):
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        var.set(folder_selected)

def select_file(var):
    file_selected = filedialog.askopenfilename()
    if file_selected:
        var.set(file_selected)

# Function to save paths to a JSON file
def save_paths():
    paths = {
        "citizen_src_pvp": citizen_src_pvp.get(),
        "citizen_dest": citizen_dest.get(),
        "config_src_pvp": config_src_pvp.get(),
        "config_dest": config_dest.get(),
        "config_src_default": config_src_default.get()
    }
    with open('paths.json', 'w') as f:
        json.dump(paths, f)
    messagebox.showinfo("Info", "Paths saved successfully.")

# Function to load paths from a JSON file
def load_paths():
    if os.path.exists('paths.json'):
        with open('paths.json', 'r') as f:
            paths = json.load(f)
            citizen_src_pvp.set(paths.get("citizen_src_pvp", ""))
            citizen_dest.set(paths.get("citizen_dest", ""))
            config_src_pvp.set(paths.get("config_src_pvp", ""))
            config_dest.set(paths.get("config_dest", ""))
            config_src_default.set(paths.get("config_src_default", ""))
            lbl_status.config(text="Paths loaded.")
    else:
        messagebox.showwarning("Warning", "paths.json file not found.")

# Function to delete and copy files/folders
def delete_and_copy(src, dest):
    if os.path.exists(dest):
        if os.path.isdir(dest):
            shutil.rmtree(dest)
        else:
            os.remove(dest)
    if os.path.isdir(src):
        shutil.copytree(src, dest)
    else:
        shutil.copy(src, dest)

# Function to set PVP configuration
def set_config_pvp():
    delete_and_copy(citizen_src_pvp.get(), citizen_dest.get())
    delete_and_copy(config_src_pvp.get(), config_dest.get())
    lbl_status.config(text="PVP Configuration set.")
    messagebox.showinfo("Info", "PVP Configuration applied. Closing in 5 seconds...")
    root.after(5000, root.quit)

# Function to set Default configuration
def set_config_default():
    if os.path.exists(citizen_dest.get()):
        shutil.rmtree(citizen_dest.get())
    delete_and_copy(config_src_default.get(), config_dest.get())
    lbl_status.config(text="Default Configuration set.")
    messagebox.showinfo("Info", "Default Configuration applied. Closing in 5 seconds...")
    root.after(5000, root.quit)

# Function to automatically detect paths
def detect_paths():
    user_profile = os.environ['USERPROFILE']
    citizen_dest.set(os.path.join(user_profile, r"AppData\Local\FiveM\FiveM.app\citizen"))
    config_dest.set(os.path.join(user_profile, r"AppData\Roaming\CitizenFX\gta5_settings.xml"))
    lbl_status.config(text="Paths detected automatically.")
    root.update()

# GUI Configuration
root = tk.Tk()
root.title("Citizen Changer")
root.geometry("1280x720")
root.configure(bg="black")

# Variables for paths
citizen_src_pvp = tk.StringVar()
citizen_dest = tk.StringVar()
config_src_pvp = tk.StringVar()
config_dest = tk.StringVar()
config_src_default = tk.StringVar()

# Custom Button Style
style = ttk.Style()

style.configure("Custom.TButton",
                background="#555",
                foreground="black",  # Set font color to black
                font=("Helvetica", 12),
                relief="flat")
style.map("Custom.TButton",
          background=[("active", "#777")])

# Main Frame
frame_main = tk.Frame(root, bg="black")
frame_main.pack(expand=True, fill="both")

# Instructions Label
lbl_instructions = tk.Label(frame_main, text="Choose an option:", bg="black", fg="white", font=("Helvetica", 18, "bold"))
lbl_instructions.pack(pady=20)

# Buttons
btn_pvp = ttk.Button(frame_main, text="Config PVP", command=set_config_pvp, style="Custom.TButton")
btn_pvp.pack(pady=10)

btn_default = ttk.Button(frame_main, text="Default", command=set_config_default, style="Custom.TButton")
btn_default.pack(pady=10)

# Status Label
lbl_status = tk.Label(frame_main, text="", bg="black", fg="white", font=("Helvetica", 12))
lbl_status.pack(pady=20)

# Watermark Label
lbl_watermark = tk.Label(root, text="github.com/wwertyjr", fg="grey", bg="black", font=("Arial", 8))
lbl_watermark.pack(side="bottom", pady=10)

# Setup Frame
frame_setup = tk.Frame(root, bg="black")
frame_setup.pack(pady=20)

# Buttons and Labels for path configuration
btn_detect_paths = ttk.Button(frame_setup, text="Detect Paths", command=detect_paths, style="Custom.TButton")
btn_detect_paths.grid(row=0, column=0, columnspan=3, pady=10)

tk.Label(frame_setup, text="Citizen PVP Path:", bg="black", fg="white", font=("Helvetica", 12)).grid(row=1, column=0, sticky="e", padx=10, pady=5)
tk.Entry(frame_setup, textvariable=citizen_src_pvp, width=50).grid(row=1, column=1, padx=10, pady=5)
ttk.Button(frame_setup, text="Select", command=lambda: select_folder(citizen_src_pvp), style="Custom.TButton").grid(row=1, column=2, padx=10, pady=5)

tk.Label(frame_setup, text="Citizen Dest Path:", bg="black", fg="white", font=("Helvetica", 12)).grid(row=2, column=0, sticky="e", padx=10, pady=5)
tk.Entry(frame_setup, textvariable=citizen_dest, width=50).grid(row=2, column=1, padx=10, pady=5)
ttk.Button(frame_setup, text="Select", command=lambda: select_folder(citizen_dest), style="Custom.TButton").grid(row=2, column=2, padx=10, pady=5)

tk.Label(frame_setup, text="Config PVP Path:", bg="black", fg="white", font=("Helvetica", 12)).grid(row=3, column=0, sticky="e", padx=10, pady=5)
tk.Entry(frame_setup, textvariable=config_src_pvp, width=50).grid(row=3, column=1, padx=10, pady=5)
ttk.Button(frame_setup, text="Select", command=lambda: select_file(config_src_pvp), style="Custom.TButton").grid(row=3, column=2, padx=10, pady=5)

tk.Label(frame_setup, text="Config Dest Path:", bg="black", fg="white", font=("Helvetica", 12)).grid(row=4, column=0, sticky="e", padx=10, pady=5)
tk.Entry(frame_setup, textvariable=config_dest, width=50).grid(row=4, column=1, padx=10, pady=5)
ttk.Button(frame_setup, text="Select", command=lambda: select_file(config_dest), style="Custom.TButton").grid(row=4, column=2, padx=10, pady=5)

tk.Label(frame_setup, text="Config Default Path:", bg="black", fg="white", font=("Helvetica", 12)).grid(row=5, column=0, sticky="e", padx=10, pady=5)
tk.Entry(frame_setup, textvariable=config_src_default, width=50).grid(row=5, column=1, padx=10, pady=5)
ttk.Button(frame_setup, text="Select", command=lambda: select_file(config_src_default), style="Custom.TButton").grid(row=5, column=2, padx=10, pady=5)

ttk.Button(frame_setup, text="Save Paths", command=save_paths, style="Custom.TButton").grid(row=6, column=0, columnspan=3, pady=10)

# Load paths at startup
load_paths()

root.mainloop()
