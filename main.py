import random

def cifrar_texto(texto):
    texto_cifrado = ""
    for palabra in texto.split(", "):
        palabra_al_reves = palabra[::-1]  # Invertir la palabra
        for letra in palabra_al_reves:
            if random.choice([True, False]):  # Aleatoriamente decide si convertir la letra a ASCII
                valor_ascii = str(ord(letra))  # Obtener el código ASCII de la letra
                texto_cifrado += valor_ascii 
            else:
                if random.choice([True, False]): # Aleatoriamente decide si convertir la letra a mayúscula o no
                    texto_cifrado += letra.upper()
                else:
                    texto_cifrado += letra.lower()
    return texto_cifrado

def ingresar_texto():
    texto = input("Ingrese el texto a cifrar: ")
    return texto

def ingresar_clave():
    while True:
        clave = input("Ingrese la clave de 8 digitos para poder cifrar el texto: ")
        if len(clave) == 8:
            return clave
        else:
            print("Clave No Aceptada. La clave debe tener exactamente 8 caracteres.")

if __name__ == "__main__":
    print("Hector Aramboles. 2019-0821\n")
    print("Programa de Cifrado y Descifrado de Texto\n")
    
    texto_original = ingresar_texto()
    print("\n")
    clave = ingresar_clave()

    print("\nTexto original:")
    print(texto_original)
    
    texto_cifrado = cifrar_texto(texto_original)
    print("\nTexto cifrado:")
    print(texto_cifrado)
    
    clave_ingresada = ""
    while clave_ingresada != clave:
        clave_ingresada = input("\nVuelva a ingresar la clave para descifrar el texto: ")
        if clave_ingresada == clave:
            texto_descifrado = texto_original
            print("\nTexto descifrado:")
            print(texto_descifrado)
        else:
            print("Clave incorrecta. Ingrese la clave nuevamente.")
    
    input("\nPresiona Enter para salir del programa")