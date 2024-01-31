import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def main():
    print("Generador de Contraseñas Seguras")

    # Solicitar al usuario la longitud de la contraseña
    try:
        longitud = int(input("Ingrese la longitud de la contraseña deseada: "))
    except ValueError:
        print("Error: Ingrese un número entero válido.")
        return

    # Generar y mostrar la contraseña
    contrasena_generada = generar_contrasena(longitud)
    print("\nContraseña generada:", contrasena_generada)

if __name__ == "__main__":
    main()
