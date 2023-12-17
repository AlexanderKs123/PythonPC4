# como 1er paso guardamos el texto en un archivo q se va a crear. 
texto = """En el ámbito del desarrollo de software, la colaboración es fundamental. La 
colaboración eficiente impulsa la eficacia y mejora la calidad del código. La calidad del 
código, a su vez, es esencial para la mantenibilidad del sistema. Mantener un sistema 
sin problemas es esencial para la satisfacción del cliente. La satisfacción del cliente, por 
supuesto, es un objetivo clave para cualquier equipo de desarrollo. Desarrollar 
estrategias para fomentar la colaboración continua y mejorar la calidad del código es 
una práctica que beneficia a todos los miembros del equipo y contribuye al éxito 
general del proyecto"""

# se guarda de la sig. forma "texto.txt"
with open("texto.txt", "w", encoding="utf-8") as archivo:
    archivo.write(texto)

# aqui se lee el archivo y cuenta la frecuencia de la palabra "la"
with open("texto.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    frecuencia_la = contenido.lower().count("la")

print(f"La palabra 'la' aparece {frecuencia_la} veces en el texto.")

# para agregar texto nuevo ingresado por el usuario tood al final de texto anterior
texto_usuario = input("Ingrese texto para agregar al final del archivo: ")

with open("texto.txt", "a", encoding="utf-8") as archivo:
    archivo.write("\n" + texto_usuario)

print("Texto ingresado por el usuario agregado al final del archivo.")
