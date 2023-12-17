
# Se instala la LIBRERIA PYFIGLET



import random
from pyfiglet import Figlet

def mostrar_menu():
    print("¡Bienvenido al menú iterativo!")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")

def editar_titulo():
    figlet = Figlet()
    fuentes_disponibles = figlet.getFonts()
    fuente_seleccionada = random.choice(fuentes_disponibles)
    figlet.setFont(font=fuente_seleccionada)
    texto_imprimir = "¡Bienvenido!"
    titulo_editado = figlet.renderText(texto_imprimir)
    print(titulo_editado)

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            # SE agrega aquí el código para la opción 1
            pass
        elif opcion == "2":
            editar_titulo()
        elif opcion == "3":
            # se agrega aquí el código para la opción 3
            pass
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()