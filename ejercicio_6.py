import json
import hashlib
import os


def cargar_usuarios():
    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r") as f:
            return json.load(f)
    else:
        return []


def guardar_usuarios(usuarios):
    with open("usuarios.json", "w") as f:
        json.dump(usuarios, f, indent=4)


def registro():
    usuarios = cargar_usuarios()
    nombre_usuario = input("Introduce tu nombre de usuario: ")

    for usuario in usuarios:
        if usuario['nombre'] == nombre_usuario:
            print("El usuario ya existe.")
            return

    password = input("Introduce tu contraseña: ")
    hash_password = hashlib.sha256(password.encode()).hexdigest()
    usuarios.append({"nombre": nombre_usuario, "contraseña": hash_password})
    guardar_usuarios(usuarios)
    print("Usuario registrado correctamente.")


def login():
    usuarios = cargar_usuarios()
    nombre_usuario = input("Nombre de usuario: ")
    password = input("Contraseña: ")
    hash_password = hashlib.sha256(password.encode()).hexdigest()

    for usuario in usuarios:
        if usuario['nombre'] == nombre_usuario and usuario['contraseña'] == hash_password:
            print("Login exitoso.")
            return

    print("Nombre de usuario o contraseña incorrectos.")


def main():
    while True:
        opcion = input("(1)egistrarte o (2)ogin?: ").upper()

        if opcion == "1":
            registro()
        elif opcion == "2":
            login()
        else:
            print("Opción no válida.")

        continuar = input("¿Deseas continuar? (S/N): ").upper()
        if continuar != "S":
            break


if __name__ == "__main__":
    main()
