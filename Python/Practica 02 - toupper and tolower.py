def obtener_numero_int(valor):
    while True:
        entrada = input(valor)
        if entrada.replace(" ", "").isdigit():
            numero = int(entrada)
            return numero
        else:
            print("\n¡Error! Ingresa una opción correcta.\n")

def convertir_a_minuscula(cadena):
    resultado = ""
    for caracter in cadena:
        if 'A' <= caracter <= 'Z':
            resultado += chr(ord(caracter) + 32)
        elif caracter == 'Ñ':
            resultado += 'ñ'
        elif caracter == 'Á':
            resultado += 'á'
        elif caracter == 'É':
            resultado += 'é'
        elif caracter == 'Í':
            resultado += 'í'
        elif caracter == 'Ó':
            resultado += 'ó'
        elif caracter == 'Ú':
            resultado += 'ú'
        elif caracter == 'Ä':
            resultado += 'ä'
        elif caracter == 'Ë':
            resultado += 'ë'
        elif caracter == 'Ï':
            resultado += 'ï'
        elif caracter == 'Ö':
            resultado += 'ö'
        elif caracter == 'Ü':
            resultado += 'ü'
        else:
            resultado += caracter
    return resultado

def convertir_a_mayuscula(cadena):
    resultado = ""
    for caracter in cadena:
        if 'a' <= caracter <= 'z':
            resultado += chr(ord(caracter) - 32)
        elif caracter == 'ñ':
            resultado += 'Ñ'
        elif caracter == 'á':
            resultado += 'Á'
        elif caracter == 'é':
            resultado += 'É'
        elif caracter == 'í':
            resultado += 'Í'
        elif caracter == 'ó':
            resultado += 'Ó'
        elif caracter == 'ú':
            resultado += 'Ú'
        elif caracter == 'ä':
            resultado += 'Ä'
        elif caracter == 'ë':
            resultado += 'Ë'
        elif caracter == 'ï':
            resultado += 'Ï'
        elif caracter == 'ö':
            resultado += 'Ö'
        elif caracter == 'ü':
            resultado += 'Ü'
        else:
            resultado += caracter
    return resultado

opcion = 0

while opcion != 3:

    cadena = input("Ingresa tu cadena: ")
    print()
    print("1. Convertir a mayúsculas")
    print("2. Convertir a minúsculas")
    print("3. Salir")
    print()
    opcion = obtener_numero_int("Elija una opción: ")

    if opcion == 1:
        
        resultado = convertir_a_mayuscula(cadena)
        print(f"Tu cadena {cadena} se convirtió en: {resultado}")
        print()

    elif opcion == 2:

        resultado = convertir_a_minuscula(cadena)
        print(f"Tu cadena {cadena} se convirtió en: {resultado}")
        print()

    elif opcion == 3:

        print("Saliste del programa")
