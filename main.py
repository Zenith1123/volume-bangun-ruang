import tkinter as tk
from tkinter import messagebox
import math

def hitung_kubus():
    try:
        s = float(entry_sisi.get())
        volume = s ** 3
        label_hasil.config(text=f"Volume Kubus = {volume:.2f}")
    except:
        messagebox.showerror("Error", "Masukkan angka yang valid!")

def hitung_tabung():
    try:
        r = float(entry_jari.get())
        t = float(entry_tinggi.get())
        volume = math.pi * r**2 * t
        label_hasil.config(text=f"Volume Tabung = {volume:.2f}")
    except:
        messagebox.showerror("Error", "Masukkan angka yang valid!")

def hitung_bola():
    try:
        r = float(entry_jari_bola.get())
        volume = (4/3) * math.pi * r**3
        label_hasil.config(text=f"Volume Bola = {volume:.2f}")
    except:
        messagebox.showerror("Error", "Masukkan angka yang valid!")

root = tk.Tk()
root.title("Aplikasi Hitung Volume Bangun Ruang")
root.geometry("450x400")

judul = tk.Label(root, text="HITUNG VOLUME BANGUN RUANG", 
                 font=("Arial", 14))
judul.grid(row=0, column=0, columnspan=3, pady=15)

tk.Label(root, text="=== KUBUS ===", font=("Arial", 11, "bold"))\
    .grid(row=1, column=0, columnspan=3, pady=10)

tk.Label(root, text="Sisi Kubus").grid(row=2, column=0, sticky="w", padx=10)
entry_sisi = tk.Entry(root)
entry_sisi.grid(row=2, column=1)
tk.Button(root, text="Hitung Kubus", command=hitung_kubus)\
    .grid(row=2, column=2, padx=10)

tk.Label(root, text="=== TABUNG ===", font=("Arial", 11, "bold"))\
    .grid(row=3, column=0, columnspan=3, pady=20)

tk.Label(root, text="Jari-jari Tabung").grid(row=4, column=0, sticky="w", padx=10)
entry_jari = tk.Entry(root)
entry_jari.grid(row=4, column=1)

tk.Label(root, text="Tinggi Tabung").grid(row=5, column=0, sticky="w", padx=10)
entry_tinggi = tk.Entry(root)
entry_tinggi.grid(row=5, column=1)

tk.Button(root, text="Hitung Tabung", command=hitung_tabung)\
    .grid(row=4, column=2, rowspan=2, padx=10)

tk.Label(root, text="=== BOLA ===", font=("Arial", 11, "bold"))\
    .grid(row=6, column=0, columnspan=3, pady=20)

tk.Label(root, text="Jari-jari Bola").grid(row=7, column=0, sticky="w", padx=10)
entry_jari_bola = tk.Entry(root)
entry_jari_bola.grid(row=7, column=1)

tk.Button(root, text="Hitung Bola", command=hitung_bola)\
    .grid(row=7, column=2, padx=10)

label_hasil = tk.Label(root, text="Hasil akan muncul di sini",
                       font=("Arial", 12), fg="blue")
label_hasil.grid(row=8, column=0, columnspan=3, pady=30)

root.mainloop()