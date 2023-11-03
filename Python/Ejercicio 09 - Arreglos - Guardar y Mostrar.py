def obtener_numero_float(valor):
    while True:
        entrada = input(valor)
        if entrada.replace(".", "", 1).replace("-", "", 1).replace(" ", "").isdigit():
            numero = float(entrada)
            return numero
        else:
            print("\n¡Error! Debes ingresar un número válido.\n")

def obtener_numero_int(valor):
    while True:
        entrada = input(valor)
        if entrada.replace("-", "", 1).replace(" ", "").isdigit():
            numero = int(entrada)
            return numero
        else:
            print("\n¡Error! Debes ingresar un número entero.\n")

def ArreglosEnteros():
    a = int(obtener_numero_int("Ingresa el tamaño de tu arreglo: "))
    print()
    arreglo = [0] * a
    for i in range(a):
        arreglo[i] = int(obtener_numero_int(f"Ingresa el valor en la posición {i+1}: "))
        i+=1
    print()
    for j in range(a):
        print(f"El valor de tu arreglo en la posición {j+1} es: {arreglo[j]}")
        j+=1
        
def ArreglosFlotantes():
    a = int(obtener_numero_int("Ingresa el tamaño de tu arreglo: "))
    print()
    arreglo = [0] * a
    for i in range(a):
        arreglo[i] = float(obtener_numero_float(f"Ingresa el valor en la posición {i+1}: "))
        i+=1
    print()
    for j in range(a):
        print(f"El valor de tu arreglo en la posición {j+1} es: {arreglo[j]}")
        j+=1

def ArreglosStrings():
    a = int(obtener_numero_int("Ingresa el tamaño de tu arreglo: "))
    print()
    arreglo = [0] * a
    for i in range(a):
        arreglo[i] = input(f"Ingresa el valor en la posición {i+1}: ")
        i+=1
    print()
    for j in range(a):
        print(f"El valor de tu arreglo en la posición {j+1} es: {arreglo[j]}")
        j+=1

opcion = 0
while opcion != 4:
    print("\n---------------------------------\n"
          '"Seleciona la operación deseada": \n'
          "---------------------------------\n")
    opcion = obtener_numero_int("1. Arreglo Entero\n"
                       "2. Arreglo Flotante\n"
                       "3. Arreglo String\n"
                       "4. Salir del programa\n\n")
    if opcion == 1:
        ArreglosEnteros()
    elif opcion == 2:
        ArreglosFlotantes()
    elif opcion == 3:
        ArreglosStrings()
    elif opcion == 4:
        print("Saliste del programa\n")
    else: print("Error, ingresa una opción válida\n")
    espacio = input("Presiona enter e intenta otra opción\n")
