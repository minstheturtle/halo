import tkinter as tk
import subprocess
import os

# Fungsi membuka file lain
def buka_tambah_buku():
    subprocess.Popen(["python", "tambah_buku.py"], shell=True)

def buka_tampil_buku():
    subprocess.Popen(["python", "tampil_buku.py"], shell=True)

# GUI Main Menu
root = tk.Tk()
root.title("Menu Utama Sistem Perpustakaan")
root.geometry("600x450")
root.configure(bg="#e6f2ff")

# Judul
label = tk.Label(root, text="Menu Utama", font=("Arial", 18, "bold"),
                 bg="#e6f2ff")
label.pack(pady=20)


# Tombol Tambah Buku
btn_tambah = tk.Button(root, text="Tambah Buku", command=buka_tambah_buku,
                       font=("Arial", 14), bg="#4CAF50", fg="white",
                       width=20)
btn_tambah.pack(pady=10)


# Tombol Tampilkan Buku
btn_tampil = tk.Button(root, text="Tampilkan Buku", command=buka_tampil_buku,
                       font=("Arial", 14), bg="#2196F3", fg="white",
                       width=20)
btn_tampil.pack(pady=10)


# Jalankan menu
root.mainloop()