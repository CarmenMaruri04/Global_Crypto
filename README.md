# Global_Crypto

GlobalCrypto es una aplicación educativa desarrollada en Python con Tkinter cuyo objetivo es introducir de forma interactiva y progresiva los conceptos básicos de la criptografía y la seguridad digital.
El programa presenta diferentes misiones organizadas por niveles de dificultad, donde el usuario debe descifrar mensajes cifrados aplicando técnicas clásicas de criptografía.


Los objetivos principales de GlobalCrypto son:
- Aprender los fundamentos de la criptografía clásica.
- Desarrollar el pensamiento lógico mediante la resolución de acertijos.
- Comprender la importancia de la seguridad de la información en situaciones reales.
- Practicar el desarrollo de interfaces gráficas con Tkinter.
- Aplicar buenas prácticas de programación como la validación de entradas y el manejo de errores.

## Estructura del programa
La aplicación se inicia desde un menú principal, desde el cual se puede acceder a tres niveles de dificultad:
### Nivel Fácil – Primer contacto
Pensado para introducir los conceptos básicos de la criptografía.

Incluye dos misiones:
### Misión en el hospital
Descifrado mediante el cifrado César, aplicando un desplazamiento sobre el alfabeto.
### Archivo fantasma
Descifrado mediante el cifrado Atbash, basado en la inversión del alfabeto.

### Nivel Intermedio – Profundizando
Dirigido a usuarios que ya dominan lo básico y buscan un reto mayor.

Incluye dos misiones:
### Simbolitos
Sistema de sustitución por símbolos, donde se deben interpretar las pistas dadas para reconstruir el mensaje original.
### Intrusión en la red eléctrica
Descifrado mediante el cifrado de Vigenère, utilizando una clave proporcionada y gestionando pistas externas mediante archivos de texto.

### Nivel Difícil – Operaciones avanzadas
El nivel más complejo, enfocado a retos más elaborados y menos directos.

Incluye dos misiones:
### Ataque a la planta de limones
Descifrado de un mensaje en binario, interpretando caracteres ASCII.
### Objetos perdidos en el zoo
Cifrado personalizado que combina inversión del mensaje, desplazamientos variables y lógica condicional según la posición del carácter.

## Técnicas de criptografía utilizadas
A lo largo del proyecto se trabajan distintas técnicas y métodos de cifrado:
-Cifrado César.
-Cifrado Atbash.
-Cifrado de Vigenère.
-Sustitución por símbolos.
-Codificación binaria (ASCII).
-Algoritmos de cifrado personalizados diseñados específicamente para el proyecto.

## Organización del código

-El proyecto está dividido en varios archivos para mejorar la legibilidad y el mantenimiento:
-main.py: punto de entrada de la aplicación.
-inicial.py: menú principal y navegación entre niveles.
-nivel_facil.py, nivel_intermedio.py, nivel_dificil.py: lógica de cada nivel y sus misiones.
-utils.py: funciones reutilizables para la interfaz gráfica y validación de entradas.
-config.py: configuración de colores y estilos visuales.
-archivos_texto.py: gestión de textos externos y creación de archivos necesarios.
-easter_egg.py: pequeño detalle interactivo como elemento extra del programa.

## Tecnologías utilizadas

-Python 3
-Tkinter (interfaz gráfica)
-tkinter.messagebox (mensajes emergentes)
-Archivos de texto para pistas y contenido dinámico

## Autoras:
Proyecto desarrollado por las autoras (Gemma y Carmen) como trabajo educativo, aplicando buenas prácticas de programación y poniendo en práctica los conocimientos adquiridos sobre criptografía y desarrollo de software.

Estado del proyecto: COMPLETADO.
