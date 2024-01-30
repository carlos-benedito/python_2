import json

nombre_archivo = 'datos.json'


try:
    with open(nombre_archivo, 'r') as archivo:
        lista_personas = json.load(archivo)
except FileNotFoundError:
    lista_personas = []


def nombre_existe(nombre_buscado):
    for persona in lista_personas:
        if persona['nombre'] == nombre_buscado:
            return True
    return False


nombre_buscado = input("Introduce un nombre para buscar: ")

if nombre_existe(nombre_buscado):
    print(f"El nombre '{nombre_buscado}' existe en el archivo {nombre_archivo}.")
else:
    print(f"El nombre '{nombre_buscado}' no existe en el archivo {nombre_archivo}.")

