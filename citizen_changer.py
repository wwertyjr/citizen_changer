import os
import shutil
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def delete_and_copy(src, dest):
    # Eliminar destino si existe
    if os.path.exists(dest):
        if os.path.isdir(dest):
            shutil.rmtree(dest)
        else:
            os.remove(dest)
    # Copiar fuente al destino
    if os.path.isdir(src):
        shutil.copytree(src, dest)
    else:
        shutil.copy(src, dest)

def set_config_pvp():
    # Config PVP
    citizen_src = r"C:\Users\abuabaumiau\Desktop\citizen changer\pvp\citizen"
    citizen_dest = r"C:\Users\abuabaumiau\AppData\Local\FiveM\FiveM.app\citizen"
    config_src = r"C:\Users\abuabaumiau\Desktop\citizen changer\pvp\config\gta5_settings.xml"
    config_dest = r"C:\Users\abuabaumiau\AppData\Roaming\CitizenFX\gta5_settings.xml"
    
    lbl_status.config(text="Configurando para PVP...")
    root.update()
    delete_and_copy(citizen_src, citizen_dest)
    delete_and_copy(config_src, config_dest)
    lbl_status.config(text="Configuración PVP completada.")
    messagebox.showinfo("Info", "Se ha establecido la configuración PVP. Cerrando en 5 segundos...")
    root.after(5000, root.quit)

def set_config_default():
    # Default
    citizen_dest = r"C:\Users\abuabaumiau\AppData\Local\FiveM\FiveM.app\citizen"
    config_src = r"C:\Users\abuabaumiau\Desktop\citizen changer\default\gta5_settings.xml"
    config_dest = r"C:\Users\abuabaumiau\AppData\Roaming\CitizenFX\gta5_settings.xml"
    
    lbl_status.config(text="Configurando para Default...")
    root.update()
    if os.path.exists(citizen_dest):
        shutil.rmtree(citizen_dest)
    delete_and_copy(config_src, config_dest)
    lbl_status.config(text="Configuración Default completada.")
    messagebox.showinfo("Info", "Se ha establecido la configuración Default. Cerrando en 5 segundos...")
    root.after(5000, root.quit)

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Citizen Changer")
root.geometry("400x300")
root.configure(bg="black")

# Estilo para botones redondeados y cambio de color al pasar el ratón
style = ttk.Style()
style.configure("TButton",
                background="gray",
                foreground="black",  # Cambiar color de fuente a negro
                font=("Helvetica", 12),
                padding=10,
                borderwidth=0)
style.map("TButton",
          background=[("active", "lightblue")])

# Botones con bordes redondeados
style.layout("RoundedButton",
             [("Button.button", {"children": [("Button.focus", {"children": [("Button.padding", {"children": [("Button.label", {"sticky": "nswe"})]})]})],
                                 "sticky": "nswe"})])

style.configure("RoundedButton",
                relief="flat",
                borderwidth=0,
                focusthickness=3,
                focuscolor="none",
                background="#444",
                foreground="black",  # Cambiar color de fuente a negro
                font=("Helvetica", 12),
                padding=(10, 5),
                anchor="center")
style.map("RoundedButton",
          background=[("active", "#555")])

lbl_instructions = tk.Label(root, text="Elige una opción:", bg="black", fg="white", font=("Helvetica", 14))
lbl_instructions.pack(pady=10)

btn_pvp = ttk.Button(root, text="Config PVP", command=set_config_pvp, style="RoundedButton")
btn_pvp.pack(pady=10)

btn_default = ttk.Button(root, text="Default", command=set_config_default, style="RoundedButton")
btn_default.pack(pady=10)

lbl_status = tk.Label(root, text="", bg="black", fg="white", font=("Helvetica", 10))
lbl_status.pack(pady=20)

# Marca de agua
lbl_watermark = tk.Label(root, text="github.com/wwertyjr", fg="grey", bg="black", font=("Arial", 8))
lbl_watermark.pack(side="bottom", pady=10)

root.mainloop()
