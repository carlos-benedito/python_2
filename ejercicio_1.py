import os


def listar_contenido_carpeta(ruta):
    if os.path.isdir(ruta):
        elementos = os.listdir(ruta)

        for elemento in elementos:
            ruta_completa = os.path.join(ruta, elemento)
            if os.path.isfile(ruta_completa):
                print(f'Archivo: {elemento}')
            elif os.path.isdir(ruta_completa):
                print(f'Directorio: {elemento}')
            else:
                print(f'Otro tipo de elemento: {elemento}')
    else:
        print(f'La ruta {ruta} no es un directorio válido.')


ruta_carpeta = ('D:/')
listar_contenido_carpeta(ruta_carpeta)
