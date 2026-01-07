import tkinter as tk
from tkinter import messagebox


def solo_letras_limitado(texto):
    if len(texto) > 50:
        return False
    return all(c.isalpha() or c.isspace() for c in texto)


def menu_principal():

    def nivel_facil():

        def borrar_texto():
            etiqueta_main.config(text="")

        def menu():
            etiqueta_main = tk.Label(root, text = "Bienvenido a GlobalCrypto \nGlobalCrypto es tu puerta de entrada al mundo de la criptografia y la seguridad digital, presentado de una forma sencilla y divertida. \nDesde el menu principal podras acceder a diferentes misiones y retos disenados para que aprendas paso a paso, poniendo en practica tus conocimientos mientras disfrutas de una experiencia interactiva.\nEl programa esta organizado en niveles de dificultad (facil, intermedio y dificil), para que avances a tu ritmo y descubras nuevas opciones a medida que progresas. \nCada mision te plantea situaciones reales y dinamicas, como la Mision en el hospital o el Archivo Fantasma, que te ayudaran a comprender como funciona la criptografia en la vida cotidiana.\nGlobalCrypto no es solo una herramienta de aprendizaje: es un espacio donde podras experimentar, equivocarte sin miedo y mejorar tus habilidades de forma entretenida. \nEl menu principal sera tu punto de partida para explorar todo lo que el programa tiene preparado para ti.")
            etiqueta_main.pack()

            boton_nivel_facil = tk.Button(root, text="Nivel Facil", command=nivel_facil)
            boton_nivel_facil.pack()
            boton_nivel_intermedio = tk.Button(root, text="Nivel Intermedio", command=nivel_intermedio)
            boton_nivel_intermedio.pack()
            boton_nivel_dificil = tk.Button(root, text="Nivel Dificil", command=nivel_dificil)
            boton_nivel_dificil.pack()
            boton_salir = tk.Button(root, text="Salir", command=root.destroy)
            boton_salir.pack()

            etiqueta_nivel_facil.config(text="")
            boton_misionhospital.destroy()
            boton_archivofantasma.destroy()
            boton_salir_menuprincipal.destroy()

        def mision_en_el_hospital():

            def menu_1():
                etiqueta_main = tk.Label(root, text = "Bienvenido a GlobalCrypto \nGlobalCrypto es tu puerta de entrada al mundo de la criptografia y la seguridad digital, presentado de una forma sencilla y divertida. \nDesde el menu principal podras acceder a diferentes misiones y retos disenados para que aprendas paso a paso, poniendo en practica tus conocimientos mientras disfrutas de una experiencia interactiva.\nEl programa esta organizado en niveles de dificultad (facil, intermedio y dificil), para que avances a tu ritmo y descubras nuevas opciones a medida que progresas. \nCada mision te plantea situaciones reales y dinamicas, como la Mision en el hospital o el Archivo Fantasma, que te ayudaran a comprender como funciona la criptografia en la vida cotidiana.\nGlobalCrypto no es solo una herramienta de aprendizaje: es un espacio donde podras experimentar, equivocarte sin miedo y mejorar tus habilidades de forma entretenida. \nEl menu principal sera tu punto de partida para explorar todo lo que el programa tiene preparado para ti.")
                etiqueta_main.pack()

                boton_nivel_facil = tk.Button(root, text="Nivel Facil", command=nivel_facil)
                boton_nivel_facil.pack()
                boton_nivel_intermedio = tk.Button(root, text="Nivel Intermedio", command=nivel_intermedio)
                boton_nivel_intermedio.pack()
                boton_nivel_dificil = tk.Button(root, text="Nivel Dificil", command=nivel_dificil)
                boton_nivel_dificil.pack()
                boton_salir = tk.Button(root, text="Salir", command=root.destroy)
                boton_salir.pack()

                etiqueta_mision_hospital.config(text="")
                entrada_mision_hospital.destroy()
                boton_misionhospital.destroy()
                boton_salir_menuprincipal_1.destroy()
                boton_enter.destroy()

            etiqueta_mision_hospital = tk.Label(root, text = "Eres un empleado de una empresa de ciberseguridad de un hospital y ha habido un incidente de phishing que insertaba un ransomware. \nEl ransomware pide un rescate porque ha encriptado los datos de los pacientes. \nTu jefe te pide que descubras quien ha hackeado el hospital, para luego el equipo poder usar \nla informacion disponible en internet para poder recuperar la informacion de los pacientes que han encriptado. \nCLAVE CIFRADA PARA CONCOCER AL GRUPO: \n NZSYKW IFWP NFHP AJNSYNXNJYJ \nPISTA: \n6 ")
            etiqueta_mision_hospital.pack() #Introduccion a mision en el hospital

            boton_misionhospital.destroy()
            boton_archivofantasma.destroy()
            boton_salir_menuprincipal.destroy()
            etiqueta_nivel_facil.config(text="")

            vcmd = root.register(solo_letras_limitado)
            entrada_mision_hospital = tk.Entry(
                root,
                validate="key",
                validatecommand=(vcmd, "%P")
            )
            entrada_mision_hospital.pack()

            def solucion_mision_hospital():
                input_user_mision_hospital = entrada_mision_hospital.get().strip().upper()

                nombre_hacker_hospital = ""
                pista1_1 = 5
                nombre_grupo_hackers_hospital = "MZSYJW IFWP MFHP AJNSYNXNJYJ"
                abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                try:
                    for ch in nombre_grupo_hackers_hospital:
                        if ch == " ":
                            nombre_hacker_hospital += " "
                        else:
                            idx = abecedario.find(ch)
                            nombre_hacker_hospital += abecedario[(idx - pista1_1) % len(abecedario)]
                except ValueError:
                    messagebox.showerror("Se ha producido un error al descifrar el mensaje.")

                nombre_hacker_hospital = nombre_hacker_hospital.strip().upper()

                if nombre_hacker_hospital in input_user_mision_hospital:
                    messagebox.showinfo(
                        message="Muy bien, lo has acertado.\nLa respuesta correcta es:\nHUNTER DARK HACK VEINTISIETE"
                    )
                else:
                    tk.Label(root, text="Lo siento, no es correcto.").pack()
                """
                Por cada letra en el codigo a descifrar se busca en el abecedario su posicion y se le resta el numero dado en la pista, 
                y una vez obtenemos ese nuevo numero que es la posicion en el abecedario de la letra real del mensaje, una vez hemos acabado con todas las letras 
                y se han ido anadiendo en la solucion se compara esta con la entrada del usuario.
                """
            boton_enter = tk.Button(root, text="Confirmar", command=solucion_mision_hospital)
            boton_enter.pack()
            boton_salir_menuprincipal_1 = tk.Button(root, text="Salir al menu principal", command=menu_1)
            boton_salir_menuprincipal_1.pack()

        def archivo_fantasma():

            def menu_2():
                etiqueta_main = tk.Label(root, text = "Bienvenido a GlobalCrypto \nGlobalCrypto es tu puerta de entrada al mundo de la criptografia y la seguridad digital, presentado de una forma sencilla y divertida. \nDesde el menu principal podras acceder a diferentes misiones y retos disenados para que aprendas paso a paso, poniendo en practica tus conocimientos mientras disfrutas de una experiencia interactiva.\nEl programa esta organizado en niveles de dificultad (facil, intermedio y dificil), para que avances a tu ritmo y descubras nuevas opciones a medida que progresas. \nCada mision te plantea situaciones reales y dinamicas, como la Mision en el hospital o el Archivo Fantasma, que te ayudaran a comprender como funciona la criptografia en la vida cotidiana.\nGlobalCrypto no es solo una herramienta de aprendizaje: es un espacio donde podras experimentar, equivocarte sin miedo y mejorar tus habilidades de forma entretenida. \nEl menu principal sera tu punto de partida para explorar todo lo que el programa tiene preparado para ti.")
                etiqueta_main.pack()

                boton_nivel_facil = tk.Button(root, text="Nivel Facil", command=nivel_facil)
                boton_nivel_facil.pack()
                boton_nivel_intermedio = tk.Button(root, text="Nivel Intermedio", command=nivel_intermedio)
                boton_nivel_intermedio.pack()
                boton_nivel_dificil = tk.Button(root, text="Nivel Dificil", command=nivel_dificil)
                boton_nivel_dificil.pack()
                boton_salir = tk.Button(root, text="Salir", command=root.destroy)
                boton_salir.pack()

                etiqueta_archivo_fantasma.config(text="")
                entrada_archivo_fantasma.destroy()
                boton_misionhospital.destroy()
                boton_salir_menuprincipal_2.destroy()
                boton_enter1.destroy()

            etiqueta_archivo_fantasma = tk.Label(root, text = "Una empresa de logistica internacional detecta que uno de sus servidores de gestion de envios ha dejado de funcionar. \nEn un primer momento, los empleados consideran que podria tratarse de un fallo tecnico o de un archivo extraviado. \nSin embargo, al realizar una revision detallada, descubren que el sistema ha sido objeto de un ataque informatico. \nLos atacantes han cifrado la base de datos de los clientes y han dejado un mensaje oculto en el sistema.\nTu mision consiste en identificar dicho mensaje oculto: \nXLMEVIGRWL VM ZIXSREL UZMGZHNZ")
            etiqueta_archivo_fantasma.pack() #Introduccion a archivo fantasma

            boton_misionhospital.destroy()
            boton_archivofantasma.destroy()
            boton_salir_menuprincipal.destroy()
            etiqueta_nivel_facil.config(text="")

            vcmd = root.register(solo_letras_limitado)
            entrada_archivo_fantasma = tk.Entry(
                root,
                validate="key",
                validatecommand=(vcmd, "%P")
            )
            entrada_archivo_fantasma.pack()

            def solucion_archivo_fantasma():
                input_user_archivo_fantasma = entrada_archivo_fantasma.get().strip().upper()
                mensaje_fantasma = ""
                mensaje_fantasma_encriptado = "XLMEVIGRWL VM ZIXSREL UZMGZHNZ"
                abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                oiradeceba = "ZYXWVUTSRQPONMLKJIHGFEDCBA"

                try:
                    for ch in mensaje_fantasma_encriptado:
                        if ch in oiradeceba:
                            mensaje_fantasma += abecedario[oiradeceba.find(ch)]
                        else:
                            mensaje_fantasma += " "
                except ValueError:
                    messagebox.showerror("Se ha producido un error al descifrar el mensaje.")
                """
                Por cada letra en el mensaje encriptado, se busca la posicion en el abecedario del reves y ese mismo numero sirve para encontrar 
                la letra real en el abecedario normal.
                """
                mensaje_fantasma = mensaje_fantasma.strip().upper()

                if mensaje_fantasma in input_user_archivo_fantasma:
                    messagebox.showinfo(
                        message="Muy bien, lo has acertado.\nLa respuesta correcta es:\nCONVERTIDO EN ARCHIVO FANTASMA"
                    )
                else:
                    tk.Label(root, text="Lo siento, no es correcto.").pack()

            boton_enter1 = tk.Button(root, text="Confirmar", command=solucion_archivo_fantasma)
            boton_enter1.pack()
            boton_salir_menuprincipal_2 = tk.Button(root, text="Salir al menu principal", command=menu_2)
            boton_salir_menuprincipal_2.pack()

        boton_nivel_facil.destroy()
        boton_nivel_intermedio.destroy()
        boton_nivel_dificil.destroy()
        boton_salir.destroy()

        borrar_texto()

        etiqueta_nivel_facil = tk.Label(root, text = "Excelente eleccion! \nHas llegado al nivel disenado para iniciarte de manera sencilla y progresiva en el fascinante mundo de los codigos y los mensajes secretos. \nEn este nivel encontraras dos ejercicios fundamentales, creados para que comprendas los conceptos basicos de la criptografia de forma intuitiva y practica. \nCada ejercicio simula una situacion cotidiana donde el cifrado y el descifrado son la clave para resolver un pequeno misterio. \nAquí aprenderas a:\nReconocer patrones simples en textos codificados.\nAplicar tecnicas basicas de sustitucion y desplazamiento.\nDesarrollar tu pensamiento logico mientras descifras mensajes ocultos.\nNo necesitas experiencia previa, solo curiosidad y atención. \nCada reto incluye instrucciones claras y esta pensado para que avances paso a paso, afianzando lo aprendido sin presion.\nGlobalCrypto te acompana en este viaje: equivocarse es parte del aprendizaje, y cada intento te acerca mas a dominar las claves de la criptografia. \nListo para descifrar tu primer mensaje secreto? \nEl desafio comienza ahora.")
        etiqueta_nivel_facil.pack() #Introduccion al nivel facil

        boton_misionhospital = tk.Button(root, text="Mision en el hospital", command=mision_en_el_hospital)
        boton_misionhospital.pack()
        boton_archivofantasma = tk.Button(root, text="Archivo fantasma", command=archivo_fantasma)
        boton_archivofantasma.pack()
        boton_salir_menuprincipal = tk.Button(root, text="Salir al menu principal", command=menu)
        boton_salir_menuprincipal.pack()


    def nivel_intermedio():
        def borrar_texto(): #Se borra el texto del menu principal
            etiqueta_main.config(text = "")
        def menu():#Se crea una copia del menu principal para al querer volver se vuelva a poder escoger otro nivel
            etiqueta_main = tk.Label(root, text = "Bienvenido a GlobalCrypto \nGlobalCrypto es tu puerta de entrada al mundo de la criptografia y la seguridad digital, presentado de una forma sencilla y divertida. \nDesde el menu principal podras acceder a diferentes misiones y retos disenados para que aprendas paso a paso, poniendo en practica tus conocimientos mientras disfrutas de una experiencia interactiva.\nEl programa esta organizado en niveles de dificultad (facil, intermedio y dificil), para que avances a tu ritmo y descubras nuevas opciones a medida que progresas. \nCada mision te plantea situaciones reales y dinamicas, como la Mision en el hospital o el Archivo Fantasma, que te ayudaran a comprender como funciona la criptografia en la vida cotidiana.\nGlobalCrypto no es solo una herramienta de aprendizaje: es un espacio donde podras experimentar, equivocarte sin miedo y mejorar tus habilidades de forma entretenida. \nEl menu principal sera tu punto de partida para explorar todo lo que el programa tiene preparado para ti.")
            etiqueta_main.pack()
            boton_nivel_facil = tk.Button(root, text = "Nivel Facil", command = nivel_facil) #Comando de nivel facil.
            boton_nivel_facil.pack()
            boton_nivel_intermedio = tk.Button(root, text = "Nivel Intermedio", command = nivel_intermedio) #Comando de nivel intermedio.
            boton_nivel_intermedio.pack()
            boton_nivel_dificil = tk.Button(root, text = "Nivel Dificil", command = nivel_dificil) #Comando de nivel dificil.
            boton_nivel_dificil.pack()

            boton_salir = tk.Button(root, text = "Salir", command = root.destroy) #Cerrar ventana
            boton_salir.pack()
            etiqueta_nivel_intermedio.config(text = "")
            boton_simbolitos.destroy()
            boton_intru.destroy()
            boton_salir_menuprincipal.destroy()
        
            
        def simbolitos():
          
            def menu_3():
                etiqueta_main = tk.Label(root, text = "Bienvenido a GlobalCrypto \nGlobalCrypto es tu puerta de entrada al mundo de la criptografia y la seguridad digital, presentado de una forma sencilla y divertida. \nDesde el menu principal podras acceder a diferentes misiones y retos disenados para que aprendas paso a paso, poniendo en practica tus conocimientos mientras disfrutas de una experiencia interactiva.\nEl programa esta organizado en niveles de dificultad (facil, intermedio y dificil), para que avances a tu ritmo y descubras nuevas opciones a medida que progresas. \nCada mision te plantea situaciones reales y dinamicas, como la Mision en el hospital o el Archivo Fantasma, que te ayudaran a comprender como funciona la criptografia en la vida cotidiana.\nGlobalCrypto no es solo una herramienta de aprendizaje: es un espacio donde podras experimentar, equivocarte sin miedo y mejorar tus habilidades de forma entretenida. \nEl menu principal sera tu punto de partida para explorar todo lo que el programa tiene preparado para ti.")
                etiqueta_main.pack()

                boton_nivel_facil = tk.Button(root, text="Nivel Facil", command=nivel_facil)
                boton_nivel_facil.pack()
                boton_nivel_intermedio = tk.Button(root, text="Nivel Intermedio", command=nivel_intermedio)
                boton_nivel_intermedio.pack()
                boton_nivel_dificil = tk.Button(root, text="Nivel Dificil", command=nivel_dificil)
                boton_nivel_dificil.pack()
                boton_salir = tk.Button(root, text="Salir", command=root.destroy)
                boton_salir.pack()

                etiqueta_simbolitos.config(text="")
                entrada_simbolitos.destroy()
                boton_intru.destroy()
                boton_salir_menuprincipal_3.destroy()
                boton_enter2.destroy()

            etiqueta_simbolitos = tk.Label(root, text = "Durante una revision rutinaria en el departamento de seguridad de tu organizacion, se ha detectado un mensaje interno que aparece codificado mediante un sistema de sustitucion por simbolos. \nAntes de poder determinar su origen o relevancia, es necesario descifrarlo. Tu tarea consiste en analizar el patron utilizado, identificar las equivalencias y reconstruir el contenido original.\n Mensaje a desencriptar:\n #?_’    #?    [! %#!?+*#    ()&=+-’    ]’=    ?)%{‘})_’? \n Pista: \n M = % \n E = # \n N = ! \n S = ? \n A = + \n J = * \n E = # \n \n C = ( \n I = ) \n F = & \n R = = \n A = + \n D = - \n O = ‘ \n ")
            etiqueta_simbolitos.pack() #Introduccion a simbolitos

            boton_simbolitos.destroy()
            boton_intru.destroy()
            boton_salir_menuprincipal.destroy()
            etiqueta_nivel_intermedio.config(text="")

            vcmd = root.register(solo_letras_limitado)
            entrada_simbolitos = tk.Entry(
                root,
                validate="key",
                validatecommand=(vcmd, "%P")
            )
            entrada_simbolitos.pack()

            def solucion_simbolitos():
                input_user_simbolitos = entrada_simbolitos.get().strip().upper()
                solucion_simbolitos = "ESTO ES UN MENSAJE CIFRADO POR SIMBOLITOS"
                


                if solucion_simbolitos in input_user_simbolitos:
                    messagebox.showinfo(
                        message="Muy bien, lo has acertado.\nLa respuesta correcta es:\nESTO ES UN MENSAJE CIFRADO POR SIMBOLITOS"
                    )
                else:
                    tk.Label(root, text="Lo siento, no es correcto.").pack()


            boton_enter2 = tk.Button(root, text="Confirmar", command=solucion_simbolitos)
            boton_enter2.pack()
            boton_salir_menuprincipal_3 = tk.Button(root, text="Salir al menu principal", command=menu_3)
            boton_salir_menuprincipal_3.pack()  

        def intrusion_en_la_red_electrica():
          
            def menu_4():
                etiqueta_main = tk.Label(root, text = "Bienvenido a GlobalCrypto \nGlobalCrypto es tu puerta de entrada al mundo de la criptografia y la seguridad digital, presentado de una forma sencilla y divertida. \nDesde el menu principal podras acceder a diferentes misiones y retos disenados para que aprendas paso a paso, poniendo en practica tus conocimientos mientras disfrutas de una experiencia interactiva.\nEl programa esta organizado en niveles de dificultad (facil, intermedio y dificil), para que avances a tu ritmo y descubras nuevas opciones a medida que progresas. \nCada mision te plantea situaciones reales y dinamicas, como la Mision en el hospital o el Archivo Fantasma, que te ayudaran a comprender como funciona la criptografia en la vida cotidiana.\nGlobalCrypto no es solo una herramienta de aprendizaje: es un espacio donde podras experimentar, equivocarte sin miedo y mejorar tus habilidades de forma entretenida. \nEl menu principal sera tu punto de partida para explorar todo lo que el programa tiene preparado para ti.")
                etiqueta_main.pack()

                boton_nivel_facil = tk.Button(root, text="Nivel Facil", command=nivel_facil)
                boton_nivel_facil.pack()
                boton_nivel_intermedio = tk.Button(root, text="Nivel Intermedio", command=nivel_intermedio)
                boton_nivel_intermedio.pack()
                boton_nivel_dificil = tk.Button(root, text="Nivel Dificil", command=nivel_dificil)
                boton_nivel_dificil.pack()
                boton_salir = tk.Button(root, text="Salir", command=root.destroy)
                boton_salir.pack()

                etiqueta_intru.config(text="")
                entrada_intru.destroy()
                boton_intru.destroy()
                boton_salir_menuprincipal_3.destroy()
                boton_enter2.destroy()

            etiqueta_intru = tk.Label(root, text = "Trabajas en el equipo de ciberseguridad de una empresa que gestiona la red electrica de varias ciudades. \nEn las ultimas horas, se han detectado apagones intermitentes que no coinciden con ninguna incidencia fisica en las subestaciones. \nTras una investigacion inicial, el equipo sospecha que un atacante ha conseguido acceso remoto a parte de la infraestructura critica y ha manipulado algunos sistemas de control. \nAl revisar los registros de uno de los servidores de supervision, encuentras un archivo de configuracion alterado que contiene un mensaje cifrado. \nCrees que en ese mensaje esta oculto el destino de exfiltracion de los datos robados. \nTu mision consiste en descifrar el mensaje usando el cifrado de Vigenere para averiguar adonde se estan enviando los datos: ")
            etiqueta_intru.pack() #Introduccion a intrusion en la red electrica
            clave_label = tk.Label(root, text="Clave: CLAVE")
            clave_label.pack() #Clave



            boton_simbolitos.destroy()
            boton_intru.destroy()
            boton_salir_menuprincipal.destroy()
            etiqueta_nivel_intermedio.config(text="")

            vcmd = root.register(solo_letras_limitado)
            entrada_intru = tk.Entry(
                root,
                validate="key",
                validatecommand=(vcmd, "%P")
            )
            entrada_intru.pack()
            
            def pista():
                try:
                    with open("pista.txt", "w", encoding = "utf-8") as f:
                        f.write("Fpsompz esjkwtmeetoi rqoo wivl")

                    etiqueta_pista = tk.Label(root, text = "Abra el pista.txt")
                    etiqueta_pista.pack()
                except FileNotFoundError:
                    messagebox.showerror("Se ha producido un error al buscar el archivo.")

            def solucion_intru(): 
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
                            decrypted += char # Normalizar 
                    user = entrada_intru.get().strip().lower() 
                    dec = decrypted.strip().lower() 
                    if user == dec: 
                        messagebox.showinfo( 
                            message="Muy bien, lo has acertado.\nLa respuesta correcta es:\ndestino exfiltracion nodo beta " 
                            )
                    else: 
                        tk.Label(root, text="Lo siento, no es correcto.").pack()
                except ValueError:
                    messagebox.showerror("Se ha producido un error al descirar el mensaje.")
                
                

            boton_pista = tk.Button(root, text= "Pista", command = pista )
            boton_pista.pack()
            boton_enter2 = tk.Button(root, text="Confirmar", command = solucion_intru)
            boton_enter2.pack()
            boton_salir_menuprincipal_3 = tk.Button(root, text="Salir al menu principal", command=menu_4)
            boton_salir_menuprincipal_3.pack()
            
        boton_nivel_facil.destroy()
        boton_nivel_intermedio.destroy()
        boton_nivel_dificil.destroy()
        boton_salir.destroy()
        
        
        borrar_texto()  

        etiqueta_nivel_intermedio = tk.Label(root, text = "Para quienes buscan un desafio que vaya mas alla de lo basico. \nEste nivel esta pensado para quienes ya tienen cierta familiaridad con la criptografia o simplemente desean poner a prueba su ingenio con ejercicios mas elaborados. \nAqui los acertijos requieren una observacion mas aguda, donde las pistas son menos evidentes y la solucion exige conectar ideas de forma creativa.")
        etiqueta_nivel_intermedio.pack()
        boton_simbolitos = tk.Button(root, text = "Simbolitos", command = simbolitos) 
        boton_simbolitos.pack() 
        boton_intru = tk.Button(root, text = "Intrusion en la red electrica", command = intrusion_en_la_red_electrica) 
        boton_intru.pack()
        boton_salir_menuprincipal = tk.Button(root, text = "Salir al menu principal", command = menu) #Se sale para escoger otro nivel o salir.
        boton_salir_menuprincipal.pack()  

    def nivel_dificil():
        def borrar_texto(): #Se borra el texto del menu principal
            etiqueta_main.config(text = "")
        def menu():#Se crea una copia del menu principal para al querer volver se vuelva a poder escoger otro nivel
            etiqueta_main = tk.Label(root, text = "Bienvenido a GlobalCrypto \nGlobalCrypto es tu puerta de entrada al mundo de la criptografia y la seguridad digital, presentado de una forma sencilla y divertida. \nDesde el menu principal podras acceder a diferentes misiones y retos disenados para que aprendas paso a paso, poniendo en practica tus conocimientos mientras disfrutas de una experiencia interactiva.\nEl programa esta organizado en niveles de dificultad (facil, intermedio y dificil), para que avances a tu ritmo y descubras nuevas opciones a medida que progresas. \nCada mision te plantea situaciones reales y dinamicas, como la Mision en el hospital o el Archivo Fantasma, que te ayudaran a comprender como funciona la criptografia en la vida cotidiana.\nGlobalCrypto no es solo una herramienta de aprendizaje: es un espacio donde podras experimentar, equivocarte sin miedo y mejorar tus habilidades de forma entretenida. \nEl menu principal sera tu punto de partida para explorar todo lo que el programa tiene preparado para ti.")
            etiqueta_main.pack()
            boton_nivel_facil = tk.Button(root, text = "Nivel Facil", command = nivel_facil) #Comando de nivel facil.
            boton_nivel_facil.pack()
            boton_nivel_intermedio = tk.Button(root, text = "Nivel Intermedio", command = nivel_intermedio) #Comando de nivel intermedio.
            boton_nivel_intermedio.pack()
            boton_nivel_dificil = tk.Button(root, text = "Nivel Dificil", command = nivel_dificil) #Comando de nivel dificil.
            boton_nivel_dificil.pack()

            boton_salir = tk.Button(root, text = "Salir", command = root.destroy) #Cerrar ventana
            boton_salir.pack()
            etiqueta_nivel_dificil.config(text = "")
            boton_limon.destroy()
            boton_zoo.destroy()
            boton_salir_menuprincipal.destroy()

        def Ataque_a_la_planta_de_limones():
          
            def menu_5():
                etiqueta_main = tk.Label(root, text = "Bienvenido a GlobalCrypto \nGlobalCrypto es tu puerta de entrada al mundo de la criptografia y la seguridad digital, presentado de una forma sencilla y divertida. \nDesde el menu principal podras acceder a diferentes misiones y retos disenados para que aprendas paso a paso, poniendo en practica tus conocimientos mientras disfrutas de una experiencia interactiva.\nEl programa esta organizado en niveles de dificultad (facil, intermedio y dificil), para que avances a tu ritmo y descubras nuevas opciones a medida que progresas. \nCada mision te plantea situaciones reales y dinamicas, como la Mision en el hospital o el Archivo Fantasma, que te ayudaran a comprender como funciona la criptografia en la vida cotidiana.\nGlobalCrypto no es solo una herramienta de aprendizaje: es un espacio donde podras experimentar, equivocarte sin miedo y mejorar tus habilidades de forma entretenida. \nEl menu principal sera tu punto de partida para explorar todo lo que el programa tiene preparado para ti.")
                etiqueta_main.pack()

                boton_nivel_facil = tk.Button(root, text="Nivel Facil", command=nivel_facil)
                boton_nivel_facil.pack()
                boton_nivel_intermedio = tk.Button(root, text="Nivel Intermedio", command=nivel_intermedio)
                boton_nivel_intermedio.pack()
                boton_nivel_dificil = tk.Button(root, text="Nivel Dificil", command=nivel_dificil)
                boton_nivel_dificil.pack()
                boton_salir = tk.Button(root, text="Salir", command=root.destroy)
                boton_salir.pack()

                etiqueta_limon.config(text="")
                entrada_limon.destroy()
                boton_limon.destroy()
                boton_salir_menuprincipal_4.destroy()
                boton_enter3.destroy()

            etiqueta_limon = tk.Label(root, text = "Trabajas en el equipo de ciberseguridad de una empresa agroalimentaria que gestiona varias plantas de procesado de frutas en todo el pais. \nEn las ultimas horas, la planta principal de procesado de limones ha sufrido una parada inesperada de la cinta de clasificacion automatica. \nAl principio, el equipo de mantenimiento sospecha de un fallo mecanico, pero pronto descubren que varios sistemas de control han sido modificados de forma remota. \nAl revisar los registros de uno de los controladores industriales, encuentras un archivo con un mensaje completamente en codigo binario. \nCrees que ese mensaje revela el objetivo del ataque y podria ayudar a reconfigurar los sistemas para volver a poner en marcha la planta. \nTu mision consiste en descifrar el mensaje binario para averiguar cual es el objetivo exacto del ataque. \nLa respuesta ha de ser en mayuculas ;)")
            etiqueta_limon.pack() #Introduccion ataque a la planta de limones


            boton_zoo.destroy()
            boton_limon.destroy()
            boton_salir_menuprincipal.destroy()
            etiqueta_nivel_dificil.config(text="")

            vcmd = root.register(solo_letras_limitado)
            entrada_limon = tk.Entry(
                root,
                validate="key",
                validatecommand=(vcmd, "%P")
            )
            entrada_limon.pack()
            
            def pista():
                try:
                    with open("Limon.txt", "w", encoding = "utf-8") as f:
                        f.write("01000001 01010100 01000001 01010001 01010101 01000101 00100000 01000001 00100000 01010000 01001100 01000001 01001110 01010100 01000001 00100000 01000100 01000101 00100000 01001100 01001001 01001101 01001111 01001110 01000101 01010011 \nCada grupo de 8 digitos binarios representa un caracter segun el codigo ASCII. \nEmpieza traduciendo 01000001 y sigue con cada grupo separado por espacios. ")
                    etiqueta_pista = tk.Label(root, text = "Abra el Limon.txt")
                    etiqueta_pista.pack()
                except FileNotFoundError:
                    messagebox.showerror("Se ha producido un error al buscar el archivo.")

            def solucion_limon(): 
                binario = """ 01000001 01010100 01000001 01010001 01010101 01000101 00100000 01000001 00100000 01010000 01001100 01000001 01001110 01010100 01000001 00100000 01000100 01000101 00100000 01001100 01001001 01001101 01001111 01001110 01000101 01010011 """
                binario = binario.replace("\n", " ").strip()
                bytes_binarios = binario.split(" ")
                mensaje = "" 
                try:
                    for byte in bytes_binarios: 
                        if byte:
                            numero = int(byte, 2)
                            caracter = chr(numero)
                            mensaje += caracter
                    mensaje_normalizado = mensaje.strip().upper() 
                    if mensaje_normalizado == entrada_limon.get():
                        messagebox.showinfo( 
                                message="Muy bien, lo has acertado.\nLa respuesta correcta es:\nATAQUE A PLANTA DE LIMONES " 
                                )
                    else: 
                        tk.Label(root, text="Lo siento, no es correcto.").pack()
                except ValueError:
                    messagebox.showerror("Se ha producido un error al descirar el mensaje.")

            boton_limon_pista = tk.Button(root, text= "Pista", command = pista )
            boton_limon_pista.pack()
            boton_enter3 = tk.Button(root, text="Confirmar", command = solucion_limon)
            boton_enter3.pack()
            boton_salir_menuprincipal_4 = tk.Button(root, text="Salir al menu principal", command=menu_5)
            boton_salir_menuprincipal_4.pack()
        
            
        def objetos_perdidos_zoo():
            def menu_6():
                etiqueta_main = tk.Label(root, text = "Bienvenido a GlobalCrypto \nGlobalCrypto es tu puerta de entrada al mundo de la criptografia y la seguridad digital, presentado de una forma sencilla y divertida. \nDesde el menu principal podras acceder a diferentes misiones y retos disenados para que aprendas paso a paso, poniendo en practica tus conocimientos mientras disfrutas de una experiencia interactiva.\nEl programa esta organizado en niveles de dificultad (facil, intermedio y dificil), para que avances a tu ritmo y descubras nuevas opciones a medida que progresas. \nCada mision te plantea situaciones reales y dinamicas, como la Mision en el hospital o el Archivo Fantasma, que te ayudaran a comprender como funciona la criptografia en la vida cotidiana.\nGlobalCrypto no es solo una herramienta de aprendizaje: es un espacio donde podras experimentar, equivocarte sin miedo y mejorar tus habilidades de forma entretenida. \nEl menu principal sera tu punto de partida para explorar todo lo que el programa tiene preparado para ti.")
                etiqueta_main.pack()

                boton_nivel_facil = tk.Button(root, text="Nivel Facil", command=nivel_facil)
                boton_nivel_facil.pack()
                boton_nivel_intermedio = tk.Button(root, text="Nivel Intermedio", command=nivel_intermedio)
                boton_nivel_intermedio.pack()
                boton_nivel_dificil = tk.Button(root, text="Nivel Dificil", command=nivel_dificil)
                boton_nivel_dificil.pack()
                boton_salir = tk.Button(root, text="Salir", command=root.destroy)
                boton_salir.pack()

                etiqueta_zoo.config(text="")
                entrada_zoo.destroy()
                boton_zoo.destroy()
                boton_salir_menuprincipal_4.destroy()
                boton_enter4.destroy()

            etiqueta_zoo = tk.Label(root, text = "En el zoologico se gestionan diariamente numerosos avisos relacionados con objetos extraviados por los visitantes. \nLa mayoria de estos casos son simples incidencias que se resuelven con rapidez, ya que suelen tratarse de pertenencias personales olvidadas en distintos rincones. \nNo obstante, en esta ocasion se ha registrado un informe que no encaja con las categorias habituales. \nEl objetivo de este ejercicio es analizar dicha incidencia y determinar cual ha sido el objeto extraviado. ")
            etiqueta_zoo.pack() #Introduccion a objetos perdidos


            boton_zoo.destroy()
            boton_limon.destroy()
            boton_salir_menuprincipal.destroy()
            etiqueta_nivel_dificil.config(text="")

            vcmd = root.register(solo_letras_limitado)
            entrada_zoo = tk.Entry(
                root,
                validate="key",
                validatecommand=(vcmd, "%P")
            )
            entrada_zoo.pack()
            
            def mensaje_zoo():
                try:
                    with open("MensajeZoo.txt", "w", encoding = "utf-8") as f:
                        f.write("Nos dan la siguiente información de tal objeto:\n ryhoet sx rs fwfj dsx vj nznp")
                    etiqueta_mensajezoo = tk.Label(root, text = "Abra el MensajeZoo.txt")
                    etiqueta_mensajezoo.pack()
                except FileNotFoundError:
                    messagebox.showerror("Se ha producido un error al buscar el archivo.")

            def ayuda_zoo():
                try:
                    with open("AyudaZoo.txt", "w", encoding = "utf-8") as f:
                        f.write("Se ha encriptado de tal manera: \n1. Invertir el mensaje. \n2. Asignar un numero a cada caracter (empezando por el 0). \n3. Si el caracter es par se le suman 3 posiciones en el alfabeto. \n4. Si el caracter es impar se le suman 5 posiciones. \n5. Si el caracter no es una letra, se deja tal cual.")
                    etiqueta_ayudazoo = tk.Label(root, text = "Abra el MensajeZoo.txt")
                    etiqueta_ayudazoo.pack()
                except FileNotFoundError:
                    messagebox.showerror("Se ha producido un error al buscar el archivo.")
            
            def solucion_zoo():
                mensaje_cifrado = "ryhoet sx rs fwfj dsx vj nznp"
                invertido = mensaje_cifrado[::-1] 
                resultado = [] 
                try:
                    for i, c in enumerate(invertido):
                        if 'a' <= c <= 'z': 
                            pos = ord(c) - ord('a') 
                            if i % 2 == 0: 
                                nueva_pos = (pos - 3) % 26 
                            else: 
                                nueva_pos = (pos - 5) % 26 
                            resultado.append(chr(nueva_pos + ord('a'))) 
                        else: 
                            resultado.append(c) 
                    solucion_objetos_perdidos = ''.join(resultado)                
                
                    if solucion_objetos_perdidos in entrada_zoo.get():
                        messagebox.showinfo( 
                                message="Muy bien, lo has acertado.\nLa respuesta correcta es:\nMiwi es una gata no un objeto" 
                                )
                    else: 
                        tk.Label(root, text="Lo siento, no es correcto.").pack()
                except ValueError:
                    messagebox.showerror("Se ha producido un error al descirar el mensaje.")

            boton_zoo_mensaje = tk.Button(root, text= "Mensaje", command = mensaje_zoo )
            boton_zoo_mensaje.pack()
            boton_zoo_ayuda = tk.Button(root, text= "Ayuda", command = ayuda_zoo )
            boton_zoo_ayuda.pack()
            boton_enter4 = tk.Button(root, text="Confirmar", command = solucion_zoo)
            boton_enter4.pack()
            boton_salir_menuprincipal_4 = tk.Button(root, text="Salir al menu principal", command=menu_6)
            boton_salir_menuprincipal_4.pack()



        boton_nivel_facil.destroy()
        boton_nivel_intermedio.destroy()
        boton_nivel_dificil.destroy()
        boton_salir.destroy()
        
        
        borrar_texto()  

        etiqueta_nivel_dificil = tk.Label(root, text = "Para mentes curiosas que no se conforman con lo evidente.\nEste es el espacio de los retos complejos. \nLos ejercicios aqui simulan problemas donde la criptografia se convierte en un rompecabezas intelectual de alto nivel. \nNo es solo aplicar una tecnica, sino entender la estructura del secreto, perseverar ante la ambiguedad y disfrutar de la satisfaccion que viene con descifrar lo bien oculto.")
        etiqueta_nivel_dificil.pack()
        boton_limon = tk.Button(root, text = "Ataque a la planta de limones", command = Ataque_a_la_planta_de_limones) 
        boton_limon.pack() 
        boton_zoo = tk.Button(root, text = "Objetos perdidos del zoologico", command = objetos_perdidos_zoo) 
        boton_zoo.pack()
        boton_salir_menuprincipal = tk.Button(root, text = "Salir al menu principal", command = menu) #Se sale para escoger otro nivel o salir.
        boton_salir_menuprincipal.pack()




    etiqueta_main = tk.Label(root, text = "Bienvenido a GlobalCrypto \nGlobalCrypto es tu puerta de entrada al mundo de la criptografia y la seguridad digital, presentado de una forma sencilla y divertida. \nDesde el menu principal podras acceder a diferentes misiones y retos disenados para que aprendas paso a paso, poniendo en practica tus conocimientos mientras disfrutas de una experiencia interactiva.\nEl programa esta organizado en niveles de dificultad (facil, intermedio y dificil), para que avances a tu ritmo y descubras nuevas opciones a medida que progresas. \nCada mision te plantea situaciones reales y dinamicas, como la Mision en el hospital o el Archivo Fantasma, que te ayudaran a comprender como funciona la criptografia en la vida cotidiana.\nGlobalCrypto no es solo una herramienta de aprendizaje: es un espacio donde podras experimentar, equivocarte sin miedo y mejorar tus habilidades de forma entretenida. \nEl menu principal sera tu punto de partida para explorar todo lo que el programa tiene preparado para ti.")
    etiqueta_main.pack()
    boton_nivel_facil = tk.Button(root, text = "Nivel Facil", command = nivel_facil) #Comando de nivel facil.
    boton_nivel_facil.pack()
    boton_nivel_intermedio = tk.Button(root, text = "Nivel Intermedio", command = nivel_intermedio) #Comando de nivel intermedio.
    boton_nivel_intermedio.pack()
    boton_nivel_dificil = tk.Button(root, text = "Nivel Dificil", command = nivel_dificil) #Comando de nivel dificil.
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
