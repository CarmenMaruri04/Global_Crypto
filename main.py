import tkinter as tk
from config import COLOR_FONDO
from archivos_texto import crear_archivos_iniciales
from inicial import menu_principal

def main():
    root = tk.Tk()
    root.title("GlobalCrypto")
    crear_archivos_iniciales()
    root.geometry("800x600")
    root.configure(bg=COLOR_FONDO)
    menu_principal(root)
    root.mainloop()

if __name__ == "__main__":
    main()