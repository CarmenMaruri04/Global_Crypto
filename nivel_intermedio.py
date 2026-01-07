import tkinter as tk
from tkinter import messagebox
from utils import *
from archivos_texto import leer_texto
from easter_egg import easter_egg1
from config import COLOR_FONDO

def nivel_intermedio(root):
    def volver_menu():
        from inicial import menu_principal
        menu_principal(root)

    # OPCION 1: SIMBOLITOS
    def simbolitos():
        limpiar_ventana(root)
        crear_boton(root, "← VOLVER", lambda: nivel_intermedio(root)).pack(anchor="nw", padx=10, pady=10)
        titulo = crear_etiqueta_titulo(root, "SIMBOLITOS")
        titulo.pack(pady=10)
        texto = crear_etiqueta_normal(root, """Durante una revision rutinaria se ha detectado un mensaje interno codificado mediante un sistema de sustitucion por simbolos.\nMensaje a desencriptar:\n#?_'    #?    [! %#!?+*#    ()&=+-'    ]'=    ?)%{'})_'?\n\nPista:\nM = %\nE = #\nN = !\nS = ?\nA = +\nJ = *\nC = (\nI = )\nF = &\nR = =\nD = -\nO = '""")
        texto.pack(pady=10)
        frame = tk.Frame(root, bg=COLOR_FONDO)
        frame.pack(pady=10)
        tk.Label(frame, text="Ingresa tu respuesta:", bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(side="left", padx=5)
        entrada = crear_entrada(root)
        entrada.pack(in_=frame, side="left", padx=5)
        entrada.focus()

        def verificar():
            solucion = "ESTO ES UN MENSAJE CIFRADO POR SIMBOLITOS"
            if solucion in entrada.get().strip().upper():
                messagebox.showinfo("Correcto", solucion)
            else:
                tk.Label(root, text="Incorrecto", bg=COLOR_FONDO, fg="#ff4444").pack()
        frame_btn = tk.Frame(root, bg=COLOR_FONDO)
        frame_btn.pack(pady=20)
        crear_boton_accent(root, "VERIFICAR", verificar).pack(in_=frame_btn, side="left", padx=10)
        crear_boton(root, "MENU", lambda: nivel_intermedio(root)).pack(in_=frame_btn, side="left", padx=10)
        easter_egg1(root)

    # OPCION 2: INTRUSION RED ELECTRICA
    def intrusion_red():
        limpiar_ventana(root)
        crear_boton(root, "← VOLVER", lambda: nivel_intermedio(root)).pack(anchor="nw", padx=10, pady=10)
        titulo = crear_etiqueta_titulo(root, "INTRUSION RED ELECTRICA")
        titulo.pack(pady=10)
        texto = crear_etiqueta_normal(root, """Trabajas en el equipo de ciberseguridad de una empresa que gestiona la red electrica.\nSe han detectado apagones intermitentes sospechosos.\nTu mision consiste en descifrar el mensaje usando el cifrado de Vigenere para averiguar adonde se estan enviando los datos.""")
        texto.pack(pady=10)
        clave_label = tk.Label(root, text="Clave: CLAVE", bg=COLOR_FONDO, fg=COLOR_ACCENT, font=("Arial", 10, "bold"))
        clave_label.pack()
        frame = tk.Frame(root, bg=COLOR_FONDO)
        frame.pack(pady=10)
        tk.Label(frame, text="Ingresa tu respuesta:", bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(side="left", padx=5)
        entrada = crear_entrada(root)
        entrada.pack(in_=frame, side="left", padx=5)
        entrada.focus()

        def pista():
            try:
                with open("pista.txt", "w", encoding="utf-8") as f:
                    f.write("Fpsompz esjkwtmeetoi rqoo wivl")

                tk.Label(root, text="Archivo 'pista.txt' creado", bg=COLOR_FONDO, fg=COLOR_SECUNDARIO).pack()
            except:
                messagebox.showerror("Error", "No se pudo crear el archivo.")

        def verificar():
            key = "clave"
            text = "Fpsompz esjkwtmeetoi rqoo wivl"
            decrypted = ""
            key_index = 0
            try:
                for char in text:
                    if char.isalpha():
                        shift = ord(key[key_index % len(key)]) - ord('a')
                        base = ord('A') if char.isupper() else ord('a')
                        decrypted_char = chr((ord(char) - base - shift) % 26 + base)
                        decrypted += decrypted_char
                        key_index += 1
                    else:
                        decrypted += char
                if entrada.get().strip().lower() == decrypted.strip().lower():
                    messagebox.showinfo("Correcto", "destino exfiltracion nodo beta")
                else:
                    tk.Label(root, text="Incorrecto", bg=COLOR_FONDO, fg="#ff4444").pack()
            except:
                messagebox.showerror("Error", "Error al descifrar.")
        frame_btn = tk.Frame(root, bg=COLOR_FONDO)
        frame_btn.pack(pady=20)
        crear_boton(root, "PISTA", pista).pack(in_=frame_btn, side="left", padx=5)
        crear_boton_accent(root, "VERIFICAR", verificar).pack(in_=frame_btn, side="left", padx=5)
        crear_boton(root, "MENU", lambda: nivel_intermedio(root)).pack(in_=frame_btn, side="left", padx=5)
        easter_egg1(root)

    # PANTALLA PRINCIPAL DEL NIVEL
    limpiar_ventana(root)
    crear_boton(root, "← MENU", volver_menu).pack(anchor="nw", padx=10, pady=10)
    titulo = crear_etiqueta_titulo(root, "NIVEL INTERMEDIO")
    titulo.pack(pady=10)
    texto = leer_texto("nivel_intermedio.txt")
    crear_etiqueta_normal(root, texto).pack(pady=20)
    frame = tk.Frame(root, bg=COLOR_FONDO)
    frame.pack(pady=20)
    crear_boton_accent(root, "SIMBOLITOS", simbolitos).pack(in_=frame, side="left", padx=10)
    crear_boton_accent(root, "RED ELECTRICA", intrusion_red).pack(in_=frame, side="left", padx=10)
    easter_egg1(root)