import tkinter as tk
from tkinter import messagebox
from config import COLOR_FONDO, COLOR_ACCENT

def easter_egg1(root):
    def mensaje():
        messagebox.showinfo(message='GRACIAS POR USAR GLOBALCRYPTO')
    emoji = tk.Button(
        root, text="😀", command=mensaje,
        bg=COLOR_FONDO, fg=COLOR_ACCENT,
        font=("Arial", 12), relief="flat", bd=0
    )
    emoji.pack(side="bottom", anchor="se", padx=10, pady=10)