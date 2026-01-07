import tkinter as tk
from tkinter import messagebox
from utils import *
from archivos_texto import leer_texto
from easter_egg import easter_egg1
from config import COLOR_FONDO

def nivel_facil(root):

    def volver_menu():
        from inicial import menu_principal
        menu_principal(root)

    def mision_en_el_hospital():
        limpiar_ventana(root)
        crear_boton(root, "← VOLVER", lambda: nivel_facil(root)).pack(anchor="nw", padx=10, pady=10)
        titulo = crear_etiqueta_titulo(root, "MISION EN EL HOSPITAL")
        titulo.pack(pady=10)
        texto = crear_etiqueta_normal(root, """Eres un empleado de una empresa de ciberseguridad de un hospital y ha habido un incidente de phishing que insertaba un ransomware. \nEl ransomware pide un rescate porque ha encriptado los datos de los pacientes. \nTu jefe te pide que descubras quien ha hackeado el hospital, para luego el equipo poder usar \nla informacion disponible en internet para poder recuperar la informacion de los pacientes que han encriptado. \nCLAVE CIFRADA PARA CONCOCER AL GRUPO: \n NZSYKW IFWP NFHP AJNSYNXNJYJ \nPISTA: \n6""")
        texto.pack(pady=10)
        frame = tk.Frame(root, bg=COLOR_FONDO)
        frame.pack(pady=10)
        tk.Label(frame, text="Ingresa tu respuesta:", bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(side="left", padx=5)
        entrada = crear_entrada(root)
        entrada.pack(in_=frame, side="left", padx=5)
        entrada.focus()

        def verificar():
            cifrado = "MZSYJW IFWP MFHP AJNSYNXNJYJ"
            abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            pista = 5
            descifrado = ""
            for ch in cifrado:
                if ch == " ":
                    descifrado += " "
                else:
                    idx = abecedario.find(ch)
                    descifrado += abecedario[(idx - pista) % 26]
            if descifrado.strip().upper() in entrada.get().strip().upper():
                messagebox.showinfo("Correcto", "HUNTER DARK HACK VEINTISIETE")
            else:
                tk.Label(root, text="Incorrecto", bg=COLOR_FONDO, fg="#ff4444").pack()
        frame_btn = tk.Frame(root, bg=COLOR_FONDO)
        frame_btn.pack(pady=20)
        crear_boton_accent(root, "VERIFICAR", verificar).pack(in_=frame_btn, side="left", padx=10)
        crear_boton(root, "MENU", lambda: nivel_facil(root)).pack(in_=frame_btn, side="left", padx=10)
        easter_egg1(root)

    def archivo_fantasma():
        limpiar_ventana(root)
        crear_boton(root, "← VOLVER", lambda: nivel_facil(root)).pack(anchor="nw", padx=10, pady=10)
        titulo = crear_etiqueta_titulo(root, "ARCHIVO FANTASMA")
        titulo.pack(pady=10)
        texto = crear_etiqueta_normal(root, """MENSAJE CIFRADO:\nXLMEVIGRWL VM ZIXSREL UZMGZHNZ""")
        texto.pack(pady=10)
        frame = tk.Frame(root, bg=COLOR_FONDO)
        frame.pack(pady=10)
        tk.Label(frame, text="Ingresa tu respuesta:", bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(side="left", padx=5)
        entrada = crear_entrada(root)
        entrada.pack(in_=frame, side="left", padx=5)
        entrada.focus()

        def verificar():
            cifrado = "XLMEVIGRWL VM ZIXSREL UZMGZHNZ"
            abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            rev = abc[::-1]
            desc = ""
            for ch in cifrado:
                if ch in rev:
                    desc += abc[rev.find(ch)]
                else:
                    desc += " "
            if desc.strip().upper() in entrada.get().strip().upper():
                messagebox.showinfo("Correcto", "CONVERTIDO EN ARCHIVO FANTASMA")
            else:
                tk.Label(root, text="Incorrecto", bg=COLOR_FONDO, fg="#ff4444").pack()
        frame_btn = tk.Frame(root, bg=COLOR_FONDO)
        frame_btn.pack(pady=20)
        crear_boton_accent(root, "VERIFICAR", verificar).pack(in_=frame_btn, side="left", padx=10)
        crear_boton(root, "MENU", lambda: nivel_facil(root)).pack(in_=frame_btn, side="left", padx=10)
        easter_egg1(root)

    # Pantalla principal del nivel
    limpiar_ventana(root)
    crear_boton(root, "← MENU", volver_menu).pack(anchor="nw", padx=10, pady=10)
    titulo = crear_etiqueta_titulo(root, "NIVEL FACIL")
    titulo.pack(pady=10)
    texto = leer_texto("nivel_facil.txt")
    crear_etiqueta_normal(root, texto).pack(pady=20)
    frame = tk.Frame(root, bg=COLOR_FONDO)
    frame.pack(pady=20)
    crear_boton_accent(root, "HOSPITAL", mision_en_el_hospital).pack(in_=frame, side="left", padx=10)
    crear_boton_accent(root, "ARCHIVO", archivo_fantasma).pack(in_=frame, side="left", padx=10)
    easter_egg1(root)