<<<<<<< HEAD
﻿import tkinter as tk #Importamos la interficie grafica que vamos a usar
from tkinter import ARC, messagebox #Importamos messagebox para el easteregg
=======
import tkinter as tk #Importamos la interficie grafica que vamos a usar
from tkinter import messagebox #Importamos messagebox para el easteregg
>>>>>>> origin/Develop


def menu_principal(): #Menu principal con todas sus opciones
    def nivel_facil(): #Al haber escogido nivel facil se desarrolla lo siguiente:

        def borrar_texto(): #Se borra el texto del menu principal
            etiqueta_main.config(text = "")
        def menu():#Se crea una copia del menu principal para al querer volver se vuelva a poder escoger otro nivel
            etiqueta_main = tk.Label(root, text = "Bienvenido a GlobalCrypto \nGlobalCrypto es tu puerta de entrada al mundo de la criptografia y la seguridad digital, presentado de una forma sencilla y divertida. \nDesde el menu principal podras acceder a diferentes misiones y retos disenados para que aprendas paso a paso, poniendo en practica tus conocimientos mientras disfrutas de una experiencia interactiva.\nEl programa esta organizado en niveles de dificultad (facil, intermedio y dificil), para que avances a tu ritmo y descubras nuevas opciones a medida que progresas. \nCada mision te plantea situaciones reales y dinamicas, como la Mision en el hospital o el Archivo Fantasma, que te ayudaran a comprender como funciona la criptografia en la vida cotidiana.\nGlobalCrypto no es solo una herramienta de aprendizaje: es un espacio donde podras experimentar, equivocarte sin miedo y mejorar tus habilidades de forma entretenida. \nEl menu principal sera tu punto de partida para explorar todo lo que el programa tiene preparado para ti.")
            etiqueta_main.pack()
            boton_nivel_facil = tk.Button(root, text = "Nivel Facil", command = nivel_facil) #Comando de nivel facil falta las dos opciones de dentro.
            boton_nivel_facil.pack()
            boton_nivel_intermedio = tk.Button(root, text = "Nivel Intermedio", command = nivel_intermedio) #Comando de nivel intermedio falta las dos opciones de dentro.
            boton_nivel_intermedio.pack()
            boton_nivel_dificil = tk.Button(root, text = "Nivel Dificil", command = nivel_dificil) #Comando de nivel intermedio falta las dos opciones de dentro.
            boton_nivel_dificil.pack()

            boton_salir = tk.Button(root, text = "Salir", command = root.destroy) #Cerrar ventana
            boton_salir.pack()
            etiqueta_nivel_facil.config(text = "")
            boton_misionhospital.destroy()
            boton_archivofantasma.destroy()
            boton_salir_menuprincipal.destroy()
<<<<<<< HEAD

=======
>>>>>>> origin/Develop
        def mision_en_el_hospital():
            def menu_1():#Se crea una copia del menu principal para al querer volver se vuelva a poder escoger otro nivel
                etiqueta_main = tk.Label(root, text = "Bienvenido a GlobalCrypto \nGlobalCrypto es tu puerta de entrada al mundo de la criptografia y la seguridad digital, presentado de una forma sencilla y divertida. \nDesde el menu principal podras acceder a diferentes misiones y retos disenados para que aprendas paso a paso, poniendo en practica tus conocimientos mientras disfrutas de una experiencia interactiva.\nEl programa esta organizado en niveles de dificultad (facil, intermedio y dificil), para que avances a tu ritmo y descubras nuevas opciones a medida que progresas. \nCada mision te plantea situaciones reales y dinamicas, como la Mision en el hospital o el Archivo Fantasma, que te ayudaran a comprender como funciona la criptografia en la vida cotidiana.\nGlobalCrypto no es solo una herramienta de aprendizaje: es un espacio donde podras experimentar, equivocarte sin miedo y mejorar tus habilidades de forma entretenida. \nEl menu principal sera tu punto de partida para explorar todo lo que el programa tiene preparado para ti.")
                etiqueta_main.pack()
                boton_nivel_facil = tk.Button(root, text = "Nivel Facil", command = nivel_facil) #Comando de nivel facil falta las dos opciones de dentro.
                boton_nivel_facil.pack()
                boton_nivel_intermedio = tk.Button(root, text = "Nivel Intermedio", command = nivel_intermedio) #Comando de nivel intermedio falta las dos opciones de dentro.
                boton_nivel_intermedio.pack()
                boton_nivel_dificil = tk.Button(root, text = "Nivel Dificil", command = nivel_dificil) #Comando de nivel intermedio falta las dos opciones de dentro.
                boton_nivel_dificil.pack()

                boton_salir = tk.Button(root, text = "Salir", command = root.destroy) #Cerrar ventana
                boton_salir.pack()
                etiqueta_mision_hospital.config(text = "")
                entrada_mision_hospital.delete(0, tk.END)
                entrada_mision_hospital.config(state = "disabled")
                entrada_mision_hospital.destroy()
                boton_misionhospital.destroy()
                boton_salir_menuprincipal_1.destroy()
                boton_enter.destroy()

            etiqueta_mision_hospital = tk.Label(root, text = "Eres un empleado de una empresa de ciberseguridad de un hospital y ha habido un incidente de phishing que insertaba un ransomware. \nEl ransomware pide un rescate porque ha encriptado los datos de los pacientes. \nTu jefe te pide que descubras quien ha hackeado el hospital, para luego el equipo poder usar \nla informacion disponible en internet para poder recuperar la informacion de los pacientes que han encriptado. \nCLAVE CIFRADA PARA CONCOCER AL GRUPO: \n NZSYKW IFWP NFHP AJNSYNXNJYJ \nPISTA: \n6 ")
            etiqueta_mision_hospital.pack()
            boton_misionhospital.destroy()
            boton_archivofantasma.destroy()
            boton_salir_menuprincipal.destroy()
            etiqueta_nivel_facil.config(text = "")
            entrada_mision_hospital = tk.Entry(root) 
            entrada_mision_hospital.pack()

            def solucion_mision_hospital():
                input_user_mision_hospital = entrada_mision_hospital.get().strip().upper()

                nombre_hacker_hospital = ""
                pista1_1 = 5
                nombre_grupo_hackers_hospital = "MZSYJW IFWP MFHP AJNSYNXNJYJ"
                abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

                for ch in nombre_grupo_hackers_hospital:
                    if ch == " ":
                        nombre_hacker_hospital += " "
                    else:
                        idx = abecedario.find(ch)
                        numero_idx = (idx - pista1_1) % len(abecedario)
                        nombre_hacker_hospital += abecedario[numero_idx]
                        
                nombre_hacker_hospital = nombre_hacker_hospital.strip().upper()
<<<<<<< HEAD
=======
                print(nombre_hacker_hospital)
>>>>>>> origin/Develop
                if nombre_hacker_hospital in input_user_mision_hospital:
                    messagebox.showinfo(
                        message="Muy bien, lo has acertado.\nLa respuesta correcta es:\nHUNTER DARK HACK VEINTISIETE"
                    )
                else:
                    etiqueta_equivocado = tk.Label(root, text="Lo siento, no es correcto.")
                    etiqueta_equivocado.pack()
    
            boton_enter = tk.Button(root, text = "Confirmar", command = solucion_mision_hospital)
            boton_enter.pack()
            boton_salir_menuprincipal_1 = tk.Button(root, text = "Salir al menu principal", command = menu_1) #Se sale para escoger otro nivel o salir.
            boton_salir_menuprincipal_1.pack()
<<<<<<< HEAD
        
        def archivo_fantasma():
            def menu_2():#Se crea una copia del menu principal para al querer volver se vuelva a poder escoger otro nivel
                etiqueta_main = tk.Label(root, text = "Bienvenido a GlobalCrypto \nGlobalCrypto es tu puerta de entrada al mundo de la criptografia y la seguridad digital, presentado de una forma sencilla y divertida. \nDesde el menu principal podras acceder a diferentes misiones y retos disenados para que aprendas paso a paso, poniendo en practica tus conocimientos mientras disfrutas de una experiencia interactiva.\nEl programa esta organizado en niveles de dificultad (facil, intermedio y dificil), para que avances a tu ritmo y descubras nuevas opciones a medida que progresas. \nCada mision te plantea situaciones reales y dinamicas, como la Mision en el hospital o el Archivo Fantasma, que te ayudaran a comprender como funciona la criptografia en la vida cotidiana.\nGlobalCrypto no es solo una herramienta de aprendizaje: es un espacio donde podras experimentar, equivocarte sin miedo y mejorar tus habilidades de forma entretenida. \nEl menu principal sera tu punto de partida para explorar todo lo que el programa tiene preparado para ti.")
                etiqueta_main.pack()
                boton_nivel_facil = tk.Button(root, text = "Nivel Facil", command = nivel_facil) #Comando de nivel facil falta las dos opciones de dentro.
                boton_nivel_facil.pack()
                boton_nivel_intermedio = tk.Button(root, text = "Nivel Intermedio", command = nivel_intermedio) #Comando de nivel intermedio falta las dos opciones de dentro.
                boton_nivel_intermedio.pack()
                boton_nivel_dificil = tk.Button(root, text = "Nivel Dificil", command = nivel_dificil) #Comando de nivel intermedio falta las dos opciones de dentro.
                boton_nivel_dificil.pack()

                boton_salir = tk.Button(root, text = "Salir", command = root.destroy) #Cerrar ventana
                boton_salir.pack()
                etiqueta_archivo_fantasma.config(text = "")
                entrada_archivo_fantasma.delete(0, tk.END)
                entrada_archivo_fantasma.config(state = "disabled")
                entrada_archivo_fantasma.destroy()
                boton_misionhospital.destroy()
                boton_salir_menuprincipal_2.destroy()
                boton_enter1.destroy()

            etiqueta_archivo_fantasma = tk.Label(root, text = "Una empresa de logistica internacional detecta que uno de sus servidores de gestion de envios ha dejado de funcionar. \nEn un primer momento, los empleados consideran que podria tratarse de un fallo tecnico o de un archivo extraviado. \nSin embargo, al realizar una revision detallada, descubren que el sistema ha sido objeto de un ataque informatico. \nLos atacantes han cifrado la base de datos de los clientes y han dejado un mensaje oculto en el sistema.\nTu mision consiste en identificar dicho mensaje oculto: \nXLMEVIGRWL VM ZIXSREL UZMGZHNZ")
            etiqueta_archivo_fantasma.pack()
            boton_misionhospital.destroy()
            boton_archivofantasma.destroy()
            boton_salir_menuprincipal.destroy()
            etiqueta_nivel_facil.config(text = "")
            entrada_archivo_fantasma = tk.Entry(root) 
            entrada_archivo_fantasma.pack()

            def solucion_archivo_fantasma():
                input_user_archivo_fantasma = entrada_archivo_fantasma.get().strip().upper()
                a=1
                mensaje_fantasma = ""
                mensaje_fantasma_encriptado = "XLMEVIGRWL VM ZIXSREL UZMGZHNZ"
                abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                oiradeceba = "ZYXWVUTSRQPONMLKJIHGFEDCBA"

                for ch in mensaje_fantasma_encriptado:
                    if ch in oiradeceba:
                        idx = oiradeceba.find(ch)
                        pues_no_in = abecedario[idx]
                        mensaje_fantasma += pues_no_in

                    else:
                        mensaje_fantasma += " "
                        
                        
                mensaje_fantasma = mensaje_fantasma.strip().upper()
                if mensaje_fantasma in input_user_archivo_fantasma:
                    messagebox.showinfo(
                        message="Muy bien, lo has acertado.\nLa respuesta correcta es:\nCONVERTIDO EN ARCHIVO FANTASMA"
                    )
                else:
                    etiqueta_equivocado = tk.Label(root, text="Lo siento, no es correcto.")
                    etiqueta_equivocado.pack()
    
    
            boton_enter1 = tk.Button(root, text = "Confirmar", command = solucion_archivo_fantasma)
            boton_enter1.pack()
            boton_salir_menuprincipal_2 = tk.Button(root, text = "Salir al menu principal", command = menu_2) #Se sale para escoger otro nivel o salir.
            boton_salir_menuprincipal_2.pack()
=======


>>>>>>> origin/Develop

        boton_nivel_facil.destroy()
        boton_nivel_intermedio.destroy()
        boton_nivel_dificil.destroy()
        boton_salir.destroy()
        
        
        borrar_texto()  
        etiqueta_nivel_facil = tk.Label(root, text = "Excelente eleccion! \nHas llegado al nivel disenado para iniciarte de manera sencilla y progresiva en el fascinante mundo de los codigos y los mensajes secretos. \nEn este nivel encontraras dos ejercicios fundamentales, creados para que comprendas los conceptos basicos de la criptografia de forma intuitiva y practica. \nCada ejercicio simula una situacion cotidiana donde el cifrado y el descifrado son la clave para resolver un pequeno misterio. \nAquí aprenderas a:\nReconocer patrones simples en textos codificados.\nAplicar tecnicas basicas de sustitucion y desplazamiento.\nDesarrollar tu pensamiento logico mientras descifras mensajes ocultos.\nNo necesitas experiencia previa, solo curiosidad y atención. \nCada reto incluye instrucciones claras y esta pensado para que avances paso a paso, afianzando lo aprendido sin presion.\nGlobalCrypto te acompana en este viaje: equivocarse es parte del aprendizaje, y cada intento te acerca mas a dominar las claves de la criptografia. \nListo para descifrar tu primer mensaje secreto? \nEl desafio comienza ahora.")
        etiqueta_nivel_facil.pack() #Introduccion al nivel facil
        boton_misionhospital = tk.Button(root, text = "Mision en el hospital", command = mision_en_el_hospital) #Falta comando para clickar esta opcion.
        boton_misionhospital.pack() 
        boton_archivofantasma = tk.Button(root, text = "Archivo fantasma", command = archivo_fantasma) #Falta comando para clickar esta opcion.
        boton_archivofantasma.pack()
        boton_salir_menuprincipal = tk.Button(root, text = "Salir al menu principal", command = menu) #Se sale para escoger otro nivel o salir.
        boton_salir_menuprincipal.pack()
    def nivel_intermedio():
        def borrar_texto(): #Se borra el texto del menu principal
            etiqueta_main.config(text = "")
        def menu():#Se crea una copia del menu principal para al querer volver se vuelva a poder escoger otro nivel
            etiqueta_main = tk.Label(root, text = "Bienvenido a GlobalCrypto \nGlobalCrypto es tu puerta de entrada al mundo de la criptografia y la seguridad digital, presentado de una forma sencilla y divertida. \nDesde el menu principal podras acceder a diferentes misiones y retos disenados para que aprendas paso a paso, poniendo en practica tus conocimientos mientras disfrutas de una experiencia interactiva.\nEl programa esta organizado en niveles de dificultad (facil, intermedio y dificil), para que avances a tu ritmo y descubras nuevas opciones a medida que progresas. \nCada mision te plantea situaciones reales y dinamicas, como la Mision en el hospital o el Archivo Fantasma, que te ayudaran a comprender como funciona la criptografia en la vida cotidiana.\nGlobalCrypto no es solo una herramienta de aprendizaje: es un espacio donde podras experimentar, equivocarte sin miedo y mejorar tus habilidades de forma entretenida. \nEl menu principal sera tu punto de partida para explorar todo lo que el programa tiene preparado para ti.")
            etiqueta_main.pack()
            boton_nivel_facil = tk.Button(root, text = "Nivel Facil", command = nivel_facil) #Comando de nivel facil falta las dos opciones de dentro.
            boton_nivel_facil.pack()
            boton_nivel_intermedio = tk.Button(root, text = "Nivel Intermedio", command = nivel_intermedio) #Comando de nivel intermedio falta las dos opciones de dentro.
            boton_nivel_intermedio.pack()
            boton_nivel_dificil = tk.Button(root, text = "Nivel Dificil", command = nivel_dificil) #Comando de nivel intermedio falta las dos opciones de dentro.
            boton_nivel_dificil.pack()

            boton_salir = tk.Button(root, text = "Salir", command = root.destroy) #Cerrar ventana
            boton_salir.pack()
            etiqueta_nivel_intermedio.config(text = "")
            boton_opcion2_1.destroy()
            boton_opcion2_2.destroy()
            boton_salir_menuprincipal.destroy()
        boton_nivel_facil.destroy()
        boton_nivel_intermedio.destroy()
        boton_nivel_dificil.destroy()
        boton_salir.destroy()
        
        
        borrar_texto()  

        etiqueta_nivel_intermedio = tk.Label(root, text = "Para quienes buscan un desafio que vaya mas alla de lo basico. \nEste nivel esta pensado para quienes ya tienen cierta familiaridad con la criptografia o simplemente desean poner a prueba su ingenio con ejercicios mas elaborados. \nAqui los acertijos requieren una observacion mas aguda, donde las pistas son menos evidentes y la solucion exige conectar ideas de forma creativa.")
        etiqueta_nivel_intermedio.pack()
        boton_opcion2_1 = tk.Button(root, text = "Opcion 1") #Falta comando para clickar esta opcion.
        boton_opcion2_1.pack() 
        boton_opcion2_2 = tk.Button(root, text = "Opcion 2") #Falta comando para clickar esta opcion.
        boton_opcion2_2.pack()
        boton_salir_menuprincipal = tk.Button(root, text = "Salir al menu principal", command = menu) #Se sale para escoger otro nivel o salir.
        boton_salir_menuprincipal.pack()  

    def nivel_dificil():
        def borrar_texto(): #Se borra el texto del menu principal
            etiqueta_main.config(text = "")
        def menu():#Se crea una copia del menu principal para al querer volver se vuelva a poder escoger otro nivel
            etiqueta_main = tk.Label(root, text = "Bienvenido a GlobalCrypto \nGlobalCrypto es tu puerta de entrada al mundo de la criptografia y la seguridad digital, presentado de una forma sencilla y divertida. \nDesde el menu principal podras acceder a diferentes misiones y retos disenados para que aprendas paso a paso, poniendo en practica tus conocimientos mientras disfrutas de una experiencia interactiva.\nEl programa esta organizado en niveles de dificultad (facil, intermedio y dificil), para que avances a tu ritmo y descubras nuevas opciones a medida que progresas. \nCada mision te plantea situaciones reales y dinamicas, como la Mision en el hospital o el Archivo Fantasma, que te ayudaran a comprender como funciona la criptografia en la vida cotidiana.\nGlobalCrypto no es solo una herramienta de aprendizaje: es un espacio donde podras experimentar, equivocarte sin miedo y mejorar tus habilidades de forma entretenida. \nEl menu principal sera tu punto de partida para explorar todo lo que el programa tiene preparado para ti.")
            etiqueta_main.pack()
            boton_nivel_facil = tk.Button(root, text = "Nivel Facil", command = nivel_facil) #Comando de nivel facil falta las dos opciones de dentro.
            boton_nivel_facil.pack()
            boton_nivel_intermedio = tk.Button(root, text = "Nivel Intermedio", command = nivel_intermedio) #Comando de nivel intermedio falta las dos opciones de dentro.
            boton_nivel_intermedio.pack()
            boton_nivel_dificil = tk.Button(root, text = "Nivel Dificil", command = nivel_dificil) #Comando de nivel intermedio falta las dos opciones de dentro.
            boton_nivel_dificil.pack()

            boton_salir = tk.Button(root, text = "Salir", command = root.destroy) #Cerrar ventana
            boton_salir.pack()
            etiqueta_nivel_dificil.config(text = "")
            boton_opcion3_1.destroy()
            boton_opcion3_2.destroy()
            boton_salir_menuprincipal.destroy()
        boton_nivel_facil.destroy()
        boton_nivel_intermedio.destroy()
        boton_nivel_dificil.destroy()
        boton_salir.destroy()
        
        
        borrar_texto()  

        etiqueta_nivel_dificil = tk.Label(root, text = "Para mentes curiosas que no se conforman con lo evidente.\nEste es el espacio de los retos complejos. \nLos ejercicios aqui simulan problemas donde la criptografia se convierte en un rompecabezas intelectual de alto nivel. \nNo es solo aplicar una tecnica, sino entender la estructura del secreto, perseverar ante la ambiguedad y disfrutar de la satisfaccion que viene con descifrar lo bien oculto.")
        etiqueta_nivel_dificil.pack()
        boton_opcion3_1 = tk.Button(root, text = "Opcion 1") #Falta comando para clickar esta opcion.
        boton_opcion3_1.pack() 
        boton_opcion3_2 = tk.Button(root, text = "Opcion 2") #Falta comando para clickar esta opcion.
        boton_opcion3_2.pack()
        boton_salir_menuprincipal = tk.Button(root, text = "Salir al menu principal", command = menu) #Se sale para escoger otro nivel o salir.
        boton_salir_menuprincipal.pack()




    etiqueta_main = tk.Label(root, text = "Bienvenido a GlobalCrypto \nGlobalCrypto es tu puerta de entrada al mundo de la criptografia y la seguridad digital, presentado de una forma sencilla y divertida. \nDesde el menu principal podras acceder a diferentes misiones y retos disenados para que aprendas paso a paso, poniendo en practica tus conocimientos mientras disfrutas de una experiencia interactiva.\nEl programa esta organizado en niveles de dificultad (facil, intermedio y dificil), para que avances a tu ritmo y descubras nuevas opciones a medida que progresas. \nCada mision te plantea situaciones reales y dinamicas, como la Mision en el hospital o el Archivo Fantasma, que te ayudaran a comprender como funciona la criptografia en la vida cotidiana.\nGlobalCrypto no es solo una herramienta de aprendizaje: es un espacio donde podras experimentar, equivocarte sin miedo y mejorar tus habilidades de forma entretenida. \nEl menu principal sera tu punto de partida para explorar todo lo que el programa tiene preparado para ti.")
    etiqueta_main.pack()
    boton_nivel_facil = tk.Button(root, text = "Nivel Facil", command = nivel_facil) #Comando de nivel facil falta las dos opciones de dentro.
    boton_nivel_facil.pack()
    boton_nivel_intermedio = tk.Button(root, text = "Nivel Intermedio", command = nivel_intermedio) #Comando de nivel intermedio falta las dos opciones de dentro.
    boton_nivel_intermedio.pack()
    boton_nivel_dificil = tk.Button(root, text = "Nivel Dificil", command = nivel_dificil) #Comando de nivel intermedio falta las dos opciones de dentro.
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
