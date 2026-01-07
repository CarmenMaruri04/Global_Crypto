import tkinter as tk
from utils import (
    limpiar_ventana, crear_boton, crear_boton_accent,
    crear_etiqueta_titulo, crear_etiqueta_subtitulo,
    crear_etiqueta_normal
)
from archivos_texto import leer_texto
from easter_egg import easter_egg1
from config import COLOR_FONDO
from nivel_facil import nivel_facil
from nivel_intermedio import nivel_intermedio
from nivel_dificil import nivel_dificil

def menu_principal(root):
    limpiar_ventana(root)
    root.configure(bg=COLOR_FONDO)
    titulo = crear_etiqueta_titulo(root, "GLOBALCRYPTO")
    titulo.pack(pady=(30, 10))
    subtitulo = crear_etiqueta_subtitulo(root, "Sistema de Criptografia")
    subtitulo.pack(pady=(0, 20))
    texto_menu = leer_texto("menu_principal.txt")
    etiqueta_main = crear_etiqueta_normal(root, texto_menu)
    etiqueta_main.pack(pady=20)
    frame_botones = tk.Frame(root, bg=COLOR_FONDO)
    frame_botones.pack(pady=20)
    crear_boton_accent(root, "NIVEL FACIL", lambda: nivel_facil(root)).pack(in_=frame_botones, pady=5, padx=10)
    crear_boton_accent(root, "NIVEL INTERMEDIO", lambda: nivel_intermedio(root)).pack(in_=frame_botones, pady=5, padx=10)
    crear_boton_accent(root, "NIVEL DIFICIL", lambda: nivel_dificil(root)).pack(in_=frame_botones, pady=5, padx=10)
    crear_boton(root, "SALIR", root.destroy).pack(pady=10)
    easter_egg1(root)