def leer_texto(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            return archivo.read()
    except:
        return "Texto no disponible"

def crear_archivos_iniciales():
    archivos = {
        "menu_principal.txt": """BIENVENIDO A GLOBALCRYPTO
        GlobalCrypto es tu puerta de entrada al mundo de la criptografia y la seguridad digital, presentado de una forma sencilla y divertida. 
        Desde el menu principal podras acceder a diferentes misiones y retos disenados para que aprendas paso a paso, poniendo en practica tus conocimientos mientras disfrutas de una experiencia interactiva.
        El programa esta organizado en niveles de dificultad (facil, intermedio y dificil), para que avances a tu ritmo y descubras nuevas opciones a medida que progresas.
        Cada mision te plantea situaciones reales y dinamicas, como la Mision en el hospital o el Archivo Fantasma, que te ayudaran a comprender como funciona la criptografia en la vida cotidiana.
        GlobalCrypto no es solo una herramienta de aprendizaje: es un espacio donde podras experimentar, equivocarte sin miedo y mejorar tus habilidades de forma entretenida. 
        El menu principal sera tu punto de partida para explorar todo lo que el programa tiene preparado para ti.""",
        "nivel_facil.txt": """NIVEL FACIL: PRIMER CONTACTO
        Has llegado al nivel disenado para iniciarte de manera sencilla y progresiva en el fascinante mundo de los codigos y los mensajes secretos. 
        En este nivel encontraras dos ejercicios fundamentales, creados para que comprendas los conceptos basicos de la criptografia de forma intuitiva y practica. 
        Cada ejercicio simula una situacion cotidiana donde el cifrado y el descifrado son la clave para resolver un pequeno misterio. 
        Aqui aprenderas a:
        Reconocer patrones simples en textos codificados.
        Aplicar tecnicas basicas de sustitucion y desplazamiento.
        Desarrollar tu pensamiento logico mientras descifras mensajes ocultos.
        No necesitas experiencia previa, solo curiosidad y atencion. 
        Cada reto incluye instrucciones claras y esta pensado para que avances paso a paso, afianzando lo aprendido sin presion.
        GlobalCrypto te acompana en este viaje: equivocarse es parte del aprendizaje, y cada intento te acerca mas a dominar las claves de la criptografia. 
        Listo para descifrar tu primer mensaje secreto?""",         
        "nivel_intermedio.txt": """NIVEL INTERMEDIO: PROFUNDIZANDO
        Para quienes buscan un desafio que vaya mas alla de lo basico.
        Este nivel esta pensado para quienes ya tienen cierta familiaridad con la criptografia o simplemente desean poner a prueba su ingenio con ejercicios mas elaborados. 
        Aqui los acertijos requieren una observacion mas aguda, donde las pistas son menos evidentes y la solucion exige conectar ideas de forma creativa.""",
        "nivel_dificil.txt": """NIVEL DIFICIL: OPERACIONES AVANZADAS
        Para mentes curiosas que no se conforman con lo evidente.
        Este es el espacio de los retos complejos. 
        Los ejercicios aqui simulan problemas donde la criptografia se convierte en un rompecabezas intelectual de alto nivel. 
        No es solo aplicar una tecnica, sino entender la estructura del secreto, perseverar ante la ambiguedad y disfrutar de la satisfaccion que viene con descifrar lo bien oculto."""
    }

    for nombre, contenido in archivos.items():
        try:
            with open(nombre, 'w', encoding='utf-8') as archivo:
                archivo.write(contenido)
        except:
            pass