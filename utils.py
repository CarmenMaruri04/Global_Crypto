import tkinter as tk
from config import *

def solo_letras_limitado(texto):
    if len(texto) > 50:
        return False
    return all(c.isalpha() or c.isspace() for c in texto)

def limpiar_ventana(root):
    for widget in root.winfo_children():
        widget.destroy()

def crear_boton(root, texto, comando):
    return tk.Button(
        root, text=texto, command=comando,
        bg=COLOR_BOTON, fg=COLOR_TEXTO,
        font=("Arial", 10, "bold"),
        padx=15, pady=5, relief="flat", bd=0
    )

def crear_boton_accent(root, texto, comando):
    return tk.Button(
        root, text=texto, command=comando,
        bg=COLOR_ACCENT, fg="#000000",
        font=("Arial", 10, "bold"),
        padx=15, pady=5, relief="flat", bd=0
    )

def crear_etiqueta_titulo(root, texto):
    return tk.Label(
        root, text=texto, bg=COLOR_FONDO,
        fg=COLOR_ACCENT, font=("Arial", 14, "bold"), pady=10
    )

def crear_etiqueta_subtitulo(root, texto):
    return tk.Label(
        root, text=texto, bg=COLOR_FONDO,
        fg=COLOR_SECUNDARIO, font=("Arial", 11, "bold"), pady=5
    )

def crear_etiqueta_normal(root, texto, wraplength=700):
    return tk.Label(
        root, text=texto, bg=COLOR_FONDO,
        fg=COLOR_TEXTO, font=("Arial", 10),
        wraplength=wraplength, justify="left",
        padx=20, pady=10
    )

def crear_entrada(root):
    vcmd = root.register(solo_letras_limitado)
    return tk.Entry(
        root, validate="key",
        validatecommand=(vcmd, "%P"),
        bg=COLOR_ENTRADA, fg=COLOR_TEXTO,
        font=("Arial", 10), width=50
    )