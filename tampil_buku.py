import tkinter as tk

from tkinter import ttk

import csv

import os

def muat_data():
    for row in tree.get_children():
        tree.delete(row)

    if not os.path.exists("buku.csv"):
        return

    with open("buku.csv", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        headers = next(reader, None)  # Lewati header
        for row in reader:
            tree.insert("", tk.END, values=row)

# GUI
root = tk.Tk()
root.title("Daftar Buku")
root.geometry("800x500")
root.configure(bg="#f0f8ff")

label_judul = tk.Label(root, text="Daftar Buku di Perpustakaan",
                       font=("Arial", 16, "bold"), bg="#f0f8ff")
label_judul.pack(pady=10)

# Treeview
columns = ("Judul", "Penulis", "ISBN", "Status")
tree = ttk.Treeview(root, columns=columns, show="headings", height=15)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150 if col != "Status" else 100)

tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Tombol Refresh
btn_refresh = tk.Button(root, text="Muat Ulang Data", command=muat_data,
                        bg="#007acc", fg="white", font=("Arial", 12))
btn_refresh.pack(pady=10)

# Muat data saat formulir dibuka
muat_data()

root.mainloop()