import tkinter as tk

from tkinter import messagebox

import csv

import os

from models import Buku


def simpan_buku():
    judul = entry_judul.get()
    penulis = entry_penulis.get()
    isbn = entry_isbn.get()

    if not judul or not penulis or not isbn:
        messagebox.showwarning("Peringatan", "Semua kolom harus diisi!")
        return

    buku = Buku(judul, penulis, isbn)

    file_exists = os.path.exists("buku.csv")
    with open("buku.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Judul", "Penulis", "ISBN", "Status"])

        writer.writerow(buku.to_list())

    messagebox.showinfo("Berhasil", "Buku berhasil ditambahkan.")

    entry_judul.delete(0, tk.END)
    entry_penulis.delete(0, tk.END)
    entry_isbn.delete(0, tk.END)


# GUI
root = tk.Tk()
root.title("Formulir Tambah Buku")
root.geometry("800x500")
root.configure(bg="#f0f8ff")

tk.Label(
    root,
    text="Tambah Data Buku",
    font=("Arial", 16, "bold"),
    bg="#f0f8ff"
).pack(pady=10)

frame = tk.Frame(root, bg="#f0f8ff")
frame.pack(pady=5)

tk.Label(
    frame,
    text="Judul:",
    font=("Arial", 12),
    bg="#f0f8ff"
).grid(row=0, column=0, sticky="e", padx=5, pady=5)

entry_judul = tk.Entry(frame, width=30)
entry_judul.grid(row=0, column=1, pady=5)

tk.Label(
    frame,
    text="Penulis:",
    font=("Arial", 12),
    bg="#f0f8ff"
).grid(row=1, column=0, sticky="e", padx=5, pady=5)

entry_penulis = tk.Entry(frame, width=30)
entry_penulis.grid(row=1, column=1, pady=5)

tk.Label(
    frame,
    text="ISBN:",
    font=("Arial", 12),
    bg="#f0f8ff"
).grid(row=2, column=0, sticky="e", padx=5, pady=5)

entry_isbn = tk.Entry(frame, width=30)
entry_isbn.grid(row=2, column=1, pady=5)

tk.Button(
    root,
    text="Simpan Buku",
    command=simpan_buku,
    font=("Arial", 12),
    bg="#007acc",
    fg="white",
    width=20
).pack(pady=15)

root.mainloop()