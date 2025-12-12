import tkinter as tk #Importamos la interficie grafica que vamos a usar
from tkinter import messagebox #Importamos messagebox para el easteregg


def menu_principal(): #Menu principal con todas sus opciones
    def nivel_facil(): #Al haber escogido nivel facil se desarrolla lo siguiente:
        def borrar_texto(): #Se borra el texto del menu principal
            etiqueta_main.config(text = "")
        def menu():#Se crea una copia del menu principal para al querer volver se vuelva a poder escoger otro nivel
            etiqueta_main = tk.Label(root, text = "Bienvenido a GlobalCrypto \nGlobalCrypto es tu puerta de entrada al mundo de la criptografia y la seguridad digital, presentado de una forma sencilla y divertida. \nDesde el menu principal podras acceder a diferentes misiones y retos disenados para que aprendas paso a paso, poniendo en practica tus conocimientos mientras disfrutas de una experiencia interactiva.\nEl programa esta organizado en niveles de dificultad (facil, intermedio y dificil), para que avances a tu ritmo y descubras nuevas opciones a medida que progresas. \nCada mision te plantea situaciones reales y dinamicas, como la Mision en el hospital o el Archivo Fantasma, que te ayudaran a comprender como funciona la criptografia en la vida cotidiana.\nGlobalCrypto no es solo una herramienta de aprendizaje: es un espacio donde podras experimentar, equivocarte sin miedo y mejorar tus habilidades de forma entretenida. \nEl menu principal sera tu punto de partida para explorar todo lo que el programa tiene preparado para ti.")
            etiqueta_main.pack()
            boton_nivel_facil = tk.Button(root, text = "Nivel Facil", command = nivel_facil) #Falta comando de clicar opcion
            boton_nivel_facil.pack()
            boton_nivel_intermedio = tk.Button(root, text = "Nivel Intermedio") #Falta comando de clicar opcion
            boton_nivel_intermedio.pack()
            boton_nivel_dificil = tk.Button(root, text = "Nivel Dificil") #Falta comando de clicar opcion
            boton_nivel_dificil.pack()

            boton_salir = tk.Button(root, text = "Salir", command = root.destroy) #Cerrar ventana
            boton_salir.pack()
            etiqueta_nivel_facil.config(text = "")
            boton_misionhospital.destroy()
            boton_archivofantasma.destroy()
            boton_salir_menuprincipla.destroy()
        boton_nivel_facil.destroy()
        boton_nivel_intermedio.destroy()
        boton_nivel_dificil.destroy()
        boton_salir.destroy()
        
        
        borrar_texto()  
        etiqueta_nivel_facil = tk.Label(root, text = "Excelente eleccion! \nHas llegado al nivel disenado para iniciarte de manera sencilla y progresiva en el fascinante mundo de los codigos y los mensajes secretos. \nEn este nivel encontraras dos ejercicios fundamentales, creados para que comprendas los conceptos basicos de la criptografia de forma intuitiva y practica. \nCada ejercicio simula una situacion cotidiana donde el cifrado y el descifrado son la clave para resolver un pequeno misterio. \nAquí aprenderas a:\nReconocer patrones simples en textos codificados.\nAplicar tecnicas basicas de sustitucion y desplazamiento.\nDesarrollar tu pensamiento logico mientras descifras mensajes ocultos.\nNo necesitas experiencia previa, solo curiosidad y atención. \nCada reto incluye instrucciones claras y esta pensado para que avances paso a paso, afianzando lo aprendido sin presion.\nGlobalCrypto te acompana en este viaje: equivocarse es parte del aprendizaje, y cada intento te acerca mas a dominar las claves de la criptografia. \nListo para descifrar tu primer mensaje secreto? \nEl desafio comienza ahora.")
        etiqueta_nivel_facil.pack() #Introduccion al nivel facil
        boton_misionhospital = tk.Button(root, text = "Mision en el hospital") #Falta comando para clickar esta opcion.
        boton_misionhospital.pack() 
        boton_archivofantasma = tk.Button(root, text = "Archivo fantasma") #Falta comando para clickar esta opcion.
        boton_archivofantasma.pack()
        boton_salir_menuprincipla = tk.Button(root, text = "Salir al menu principal", command = menu) #Se sale para escoger otro nivel o salir.
        boton_salir_menuprincipla.pack()
    
    etiqueta_main = tk.Label(root, text = "Bienvenido a GlobalCrypto \nGlobalCrypto es tu puerta de entrada al mundo de la criptografia y la seguridad digital, presentado de una forma sencilla y divertida. \nDesde el menu principal podras acceder a diferentes misiones y retos disenados para que aprendas paso a paso, poniendo en practica tus conocimientos mientras disfrutas de una experiencia interactiva.\nEl programa esta organizado en niveles de dificultad (facil, intermedio y dificil), para que avances a tu ritmo y descubras nuevas opciones a medida que progresas. \nCada mision te plantea situaciones reales y dinamicas, como la Mision en el hospital o el Archivo Fantasma, que te ayudaran a comprender como funciona la criptografia en la vida cotidiana.\nGlobalCrypto no es solo una herramienta de aprendizaje: es un espacio donde podras experimentar, equivocarte sin miedo y mejorar tus habilidades de forma entretenida. \nEl menu principal sera tu punto de partida para explorar todo lo que el programa tiene preparado para ti.")
    etiqueta_main.pack()
    boton_nivel_facil = tk.Button(root, text = "Nivel Facil", command = nivel_facil) #Comando de nivel facil falta las dos opciones de dentro.
    boton_nivel_facil.pack()
    boton_nivel_intermedio = tk.Button(root, text = "Nivel Intermedio") #Falta comando de clicar opcion
    boton_nivel_intermedio.pack()
    boton_nivel_dificil = tk.Button(root, text = "Nivel Dificil") #Falta comando de clicar opcion
    boton_nivel_dificil.pack()

    boton_salir = tk.Button(root, text = "Salir", command = root.destroy) #Cerrar ventana
    boton_salir.pack()

def easter_egg1():
    def mensaje():
        messagebox.showinfo(message = 'GRACIAS POR USAR GLOBALCRYPTO')

    emoji = tk.Button(root, text = "😀", command = mensaje)
    emoji.pack()

root = tk.Tk() #Crear ventana
root.title("GlobalCrypto")

menu_principal() #Llamando a menu principal con todas sus opciones
easter_egg1()



root.mainloop() #Para que se realice
