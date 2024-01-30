import json

nombre_archivo = 'datos.json'


try:
    with open(nombre_archivo, 'r') as archivo:
        lista_personas = json.load(archivo)
except FileNotFoundError:
    lista_personas = []

while True:
    print("1. Modificar")
    print("2. Crear nuevo")
    print("3. Salir")

    opcion = input("opción: ")

    if opcion == '1':
        if lista_personas:
            print("\nNombres existentes:")
            for i, persona in enumerate(lista_personas):
                print(f"{i + 1}. {persona['nombre']} {persona['apellido']}")

            indice_str = input("menu de modificar: ")
            if indice_str.isdigit():
                indice = int(indice_str) - 1
                if 0 <= indice < len(lista_personas):
                    nuevo_nombre = input("Introduce el nuevo nombre: ")
                    nuevo_apellido = input("Introduce el nuevo apellido: ")
                    lista_personas[indice]['nombre'] = nuevo_nombre
                    lista_personas[indice]['apellido'] = nuevo_apellido
                    print("Nombre modificado con éxito.")
                else:
                    print("Índice fuera de rango. Por favor, seleccione un índice válido.")
            else:
                print("Entrada inválida. Por favor, ingrese un número entero.")
        else:
            print("No hay nombres para modificar.")
    elif opcion == '2':
        nombre = input("Introduce el nombre: ")
        apellido = input("Introduce el apellido: ")
        nueva_persona = {"nombre": nombre, "apellido": apellido}
        lista_personas.append(nueva_persona)
        print("Nombre creado con éxito.")
    elif opcion == '3':
        break
    else:
        print("Opción no válida")


with open(nombre_archivo, 'w') as archivo:
    json.dump(lista_personas, archivo, indent=4)

print(f"Los datos se han guardado en el archivo {nombre_archivo}.")


