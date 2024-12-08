import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from converter import convert_schematic, save_schematic
import os

def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("Minecraft Schematics", "*.schem *.schematic")])
    if file_path:
        global loaded_file_path
        loaded_file_path = file_path
        convert_button.config(state=tk.NORMAL)
        convert_button.config(text="Converter Mapa")
        messagebox.showinfo("Arquivo Carregado", f"Arquivo {file_path} carregado com sucesso!")

def convert_schematic_file():
    if loaded_file_path:
        version_from = '1.20.4'
        version_to = version_var.get()
        progress_bar['value'] = 0
        root.update_idletasks()
        try:
            schematic = convert_schematic(loaded_file_path, version_from, version_to, progress_callback)
            output_path = f'converted_schematic_{version_to}.schematic'
            save_schematic(schematic, output_path)
            messagebox.showinfo("Sucesso", f"Conversão concluída! Arquivo salvo como '{output_path}'")
            download_button.config(state=tk.NORMAL)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao converter schematic: {e}")

def download_file():
    if loaded_file_path:
        version_to = version_var.get()
        output_path = f'converted_schematic_{version_to}.schematic'
        save_path = filedialog.asksaveasfilename(defaultextension=".schematic", filetypes=[("Minecraft Schematics", "*.schematic")])
        if save_path:
            os.rename(output_path, save_path)
            messagebox.showinfo("Sucesso", f"Arquivo salvo como '{save_path}'")

def progress_callback(progress):
    progress_bar['value'] = progress
    root.update_idletasks()

root = tk.Tk()
root.title("Minecraft Converter")
root.geometry("400x300")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(expand=True)

title_label = tk.Label(frame, text="Minecraft Converter", font=("Helvetica", 16))
title_label.pack(pady=10)

version_label = tk.Label(frame, text="Selecionar Versão de Destino:")
version_label.pack(pady=5)

version_var = tk.StringVar(value="1.8")
version_menu = ttk.Combobox(frame, textvariable=version_var, values=["1.8", "1.12", "1.16", "1.20"])
version_menu.pack(pady=5)

load_button = tk.Button(frame, text="Carregar Arquivo", command=load_file, width=20)
load_button.pack(pady=10)

convert_button = tk.Button(frame, text="Upar Schematic", command=convert_schematic_file, width=20, state=tk.DISABLED)
convert_button.pack(pady=10)

download_button = tk.Button(frame, text="Baixar Mapa", command=download_file, width=20, state=tk.DISABLED)
download_button.pack(pady=10)

progress_bar = ttk.Progressbar(frame, orient="horizontal", length=300, mode="determinate")
progress_bar.pack(pady=10)

root.mainloop()