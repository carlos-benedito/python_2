def leer_contenido_archivo(ruta_archivo):
    try:
        with open(ruta_archivo, 'r') as archivo:
            contenido = archivo.read()
            return contenido
    except FileNotFoundError:
        return f'El archivo {ruta_archivo} no se encontró.'
    except PermissionError:
        return f'No se tienen permisos para acceder al archivo {ruta_archivo}.'
    except Exception as e:
        return f'Ocurrió un error al leer el archivo {ruta_archivo}: {str(e)}'


ruta_archivo = 'c:/carpeta_3/archivo.json'
contenido = leer_contenido_archivo(ruta_archivo)
print(contenido)
