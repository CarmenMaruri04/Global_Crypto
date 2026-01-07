import tkinter as tk
from tkinter import messagebox
from utils import *
from archivos_texto import leer_texto
from easter_egg import easter_egg1
from config import COLOR_FONDO

def nivel_dificil(root):
    def volver_menu():
        from inicial import menu_principal
        menu_principal(root)

    # OPCION 1: ATAQUE A LA PLANTA DE LIMONES
    def ataque_limon():
        limpiar_ventana(root)
        crear_boton(root, "← VOLVER", lambda: nivel_dificil(root)).pack(anchor="nw", padx=10, pady=10)
        titulo = crear_etiqueta_titulo(root, "ATAQUE PLANTA LIMONES")
        titulo.pack(pady=10)
        texto = crear_etiqueta_normal(root, """La planta principal de procesado de limones ha sufrido una parada inesperada. \nSe ha encontrado un archivo con un mensaje completamente en codigo binario.\nTu mision consiste en descifrar el mensaje binario para averiguar el objetivo del ataque.""")
        texto.pack(pady=10)
        frame = tk.Frame(root, bg=COLOR_FONDO)
        frame.pack(pady=10)
        tk.Label(frame, text="Ingresa tu respuesta:", bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(side="left", padx=5)
        entrada = crear_entrada(root)
        entrada.pack(in_=frame, side="left", padx=5)
        entrada.focus()

        def pista():
            try:
                with open("Limon.txt", "w", encoding="utf-8") as f:
                    f.write("""01000001 01010100 01000001 01010001 01010101 01000101 00100000 01000001 00100000 01010000 01001100 01000001 01001110 01010100 01000001 00100000 01000100 01000101 00100000 01001100 01001001 01001101 01001111 01001110 01000101 01010011 \nCada grupo de 8 digitos binarios representa un caracter ASCII.""")
                tk.Label(root, text="Archivo 'Limon.txt' creado", bg=COLOR_FONDO, fg=COLOR_SECUNDARIO).pack()
            except:
                messagebox.showerror("Error", "No se pudo crear el archivo.")

        def verificar():
            binario = """01000001 01010100 01000001 01010001 01010101 01000101 00100000 01000001 00100000 01010000 01001100 01000001 01001110 01010100 01000001 00100000 01000100 01000101 00100000 01001100 01001001 01001101 01001111 01001110 01000101 01010011"""
            bytes_binarios = binario.split(" ")
            mensaje = ""
            try:
                for byte in bytes_binarios:
                    if byte:
                        mensaje += chr(int(byte, 2))
                if mensaje.strip().upper() == entrada.get().strip().upper():
                    messagebox.showinfo("Correcto", "ATAQUE A PLANTA DE LIMONES")
                else:
                    tk.Label(root, text="Incorrecto", bg=COLOR_FONDO, fg="#ff4444").pack()
            except:
                messagebox.showerror("Error", "Error al descifrar el mensaje.")
        frame_btn = tk.Frame(root, bg=COLOR_FONDO)
        frame_btn.pack(pady=20)
        crear_boton(root, "PISTA", pista).pack(in_=frame_btn, side="left", padx=5)
        crear_boton_accent(root, "VERIFICAR", verificar).pack(in_=frame_btn, side="left", padx=5)
        crear_boton(root, "MENU", lambda: nivel_dificil(root)).pack(in_=frame_btn, side="left", padx=5)
        easter_egg1(root)

    # OPCION 2: OBJETOS PERDIDOS EN EL ZOO
    def objetos_zoo():
        limpiar_ventana(root)
        crear_boton(root, "← VOLVER", lambda: nivel_dificil(root)).pack(anchor="nw", padx=10, pady=10)
        titulo = crear_etiqueta_titulo(root, "OBJETOS PERDIDOS ZOO")
        titulo.pack(pady=10)
        texto = crear_etiqueta_normal(root, """En el zoologico se ha registrado un informe extrano. \nTu mision es analizar el mensaje cifrado y descubrir que objeto ha sido extraviado.""")
        texto.pack(pady=10)
        frame = tk.Frame(root, bg=COLOR_FONDO)
        frame.pack(pady=10)
        tk.Label(frame, text="Ingresa tu respuesta:", bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(side="left", padx=5)
        entrada = crear_entrada(root)
        entrada.pack(in_=frame, side="left", padx=5)
        entrada.focus()

        def mensaje():
            try:
                with open("MensajeZoo.txt", "w", encoding="utf-8") as f:
                    f.write("Nos dan la siguiente informacion:\nryhoet sx rs fwfj dsx vj nznp")
                tk.Label(root, text="Archivo 'MensajeZoo.txt' creado", bg=COLOR_FONDO, fg=COLOR_SECUNDARIO).pack()
            except:
                messagebox.showerror("Error", "No se pudo crear el archivo.")

        def ayuda():
            try:
                with open("AyudaZoo.txt", "w", encoding="utf-8") as f:
                    f.write("""Metodo de cifrado:
1. Invertir el mensaje.
2. Asignar un numero a cada caracter.
3. Si el indice es par, restar 3 posiciones.
4. Si el indice es impar, restar 5 posiciones.
5. Si no es letra, dejar igual.""")
                tk.Label(root, text="Archivo 'AyudaZoo.txt' creado", bg=COLOR_FONDO, fg=COLOR_SECUNDARIO).pack()
            except:
                messagebox.showerror("Error", "No se pudo crear el archivo.")

        def verificar():
            mensaje_cifrado = "ryhoet sx rs fwfj dsx vj nznp"
            invertido = mensaje_cifrado[::-1]
            resultado = []
            try:
                for i, c in enumerate(invertido):
                    if 'a' <= c <= 'z':
                        pos = ord(c) - ord('a')
                        nueva_pos = (pos - 3) % 26 if i % 2 == 0 else (pos - 5) % 26
                        resultado.append(chr(nueva_pos + ord('a')))
                    else:
                        resultado.append(c)
                solucion = ''.join(resultado)
                if solucion in entrada.get().lower():
                    messagebox.showinfo("Correcto", "Miwi es una gata no un objeto")
                else:
                    tk.Label(root, text="Incorrecto", bg=COLOR_FONDO, fg="#ff4444").pack()
            except:
                messagebox.showerror("Error", "Error al descifrar el mensaje.")
        frame_btn = tk.Frame(root, bg=COLOR_FONDO)
        frame_btn.pack(pady=20)
        crear_boton(root, "MENSAJE", mensaje).pack(in_=frame_btn, side="left", padx=5)
        crear_boton(root, "AYUDA", ayuda).pack(in_=frame_btn, side="left", padx=5)
        crear_boton_accent(root, "VERIFICAR", verificar).pack(in_=frame_btn, side="left", padx=5)
        crear_boton(root, "MENU", lambda: nivel_dificil(root)).pack(in_=frame_btn, side="left", padx=5)
        easter_egg1(root)

    # PANTALLA PRINCIPAL DEL NIVEL
    limpiar_ventana(root)
    crear_boton(root, "← MENU", volver_menu).pack(anchor="nw", padx=10, pady=10)
    titulo = crear_etiqueta_titulo(root, "NIVEL DIFICIL")
    titulo.pack(pady=10)
    texto = leer_texto("nivel_dificil.txt")
    crear_etiqueta_normal(root, texto).pack(pady=20)
    frame = tk.Frame(root, bg=COLOR_FONDO)
    frame.pack(pady=20)
    crear_boton_accent(root, "PLANTA LIMONES", ataque_limon).pack(in_=frame, side="left", padx=10)
    crear_boton_accent(root, "ZOO", objetos_zoo).pack(in_=frame, side="left", padx=10)
    easter_egg1(root)