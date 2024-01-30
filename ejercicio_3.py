def crear_archivo(ruta_archivo, contenido=''):
    try:
        with open(ruta_archivo, 'w') as archivo:
            archivo.write(contenido)
        return f'Se ha creado el archivo {ruta_archivo} correctamente.'
    except PermissionError:
        return f'No se tienen permisos para crear el archivo {ruta_archivo}.'
    except Exception as e:
        return f'Ocurrió un error al crear el archivo {ruta_archivo}: {str(e)}'


ruta_nuevo_archivo = 'c:/carpeta_3/archivo.json'
contenido = 'hola Mundo'

resultado = crear_archivo(ruta_nuevo_archivo, contenido)
print(resultado)
