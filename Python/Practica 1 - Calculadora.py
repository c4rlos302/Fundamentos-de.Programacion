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

def sumar(Numero1=float,Numero2=float):
    print(f"{Numero1} + {Numero2} = {Numero1+Numero2}")

def restar(Numero1=float,Numero2=float):
    print(f"{Numero1} - {Numero2} = {Numero1-Numero2}")
    
def multiplicar(Numero1=float,Numero2=float):
    print(f"{Numero1} x {Numero2} = {Numero1*Numero2}")
    
def dividir(Dividendo=float,Divisor=float):
    if Divisor == 0:
        print("La división sobre 0 es inválida ya que el resultado de dividir")
        print(f"cualquier número sobre 0 = ∞, en este caso {Dividendo}/{Divisor} = ∞")
    else:
        print(f"{Dividendo}/{Divisor} = {Dividendo/Divisor}")
    
def potencia(NumeroBase=float,Potencia=int):
    if Potencia > 0:
        NumeroMultiplicar = NumeroBase
        for i in range(1,Potencia+1):
            resultado = NumeroMultiplicar
            NumeroMultiplicar*=NumeroBase
        print(f"{NumeroBase} elevado al número {Potencia} es: {resultado}")
    elif Potencia == 0:
        resultado = 1
        print(f"Todo número elevado a la {Potencia}, da como resultado: {resultado}")
        print(f"por lo tanto, {NumeroBase} elevado al número {Potencia} = {resultado}")
    elif Potencia < 0:
        NumeroMultiplicar = NumeroBase
        for i in range(1,-Potencia):
            resultado = NumeroMultiplicar
            NumeroMultiplicar*=NumeroBase
        resultado = NumeroMultiplicar
        resultado_1 = 1/NumeroMultiplicar
        print(f"{NumeroBase} elevado al número {Potencia} da como resultado: 1/{resultado} que es igual a {resultado_1}")

def RaizCuadrada(numero=float):
    if numero < 0:
        numero*=-1
        precision = 0.0000000001
        inicio = 0
        fin = (numero)
        medio = (fin + inicio)/2
        while fin - inicio > precision:
            if medio * medio > numero:
                fin = medio
            else:
                inicio = medio
            medio = (inicio + fin) / 2;
        resultado = medio
        print(f"No existen las raices cuadradas negativas, pero √-{numero} es: {resultado:.5f}i")
    elif numero == 0:
         print(f"√{numero:.0f} es: 0")
    else:
        precision = 0.0000000001
        inicio = 0
        fin = numero
        medio = (fin + inicio)/2
        while fin - inicio > precision:
            if medio * medio > numero:
                fin = medio
            else:
                inicio = medio
            medio = (inicio + fin) / 2;
        resultado = medio
        print(f"√{numero} es: {resultado:.10f}")

print("*********************************"
      "\nEsta es una calculadora en python\n"
      "*********************************\n")
opcion = 0
while opcion != 7:
    print("---------------------------------\n"
          '"Seleciona la operación deseada": \n'
          "---------------------------------\n")
    opcion = obtener_numero_int("1. Suma\n"
                       "2. Resta\n"
                       "3. Multiplicación\n"
                       "4. División\n"
                       "5. Potencia\n"
                       "6. Raíz Cuadrada\n"
                       "7. Salir del programa\n\n")
    if opcion == 1:
        print('\n"Elegiste la suma"\n')
        Numero1 = obtener_numero_float("Ingresa el primer número: ")
        Numero2 = obtener_numero_float("Ingresa el segundo número: ")
        print()
        sumar(Numero1,Numero2)
        print()
        espacio = input('"Presiona enter para continuar"\n')
        
    elif opcion == 2:
        print('\n"Elegiste la resta"\n')
        Numero1 = obtener_numero_float("Ingresa el primer número: ")
        Numero2 = obtener_numero_float("Ingresa el segundo número: ")
        print()
        restar(Numero1,Numero2)
        print()
        espacio = input('"Presiona enter para continuar"\n')
        
    elif opcion == 3:
        print('\n"Elegiste la multiplicación"\n')
        Numero1 = obtener_numero_float("Ingresa el primer número: ")
        Numero2 = obtener_numero_float("Ingresa el segundo número: ")
        print()
        multiplicar(Numero1,Numero2)
        print()
        espacio = input('"Presiona enter para continuar"\n')
        
    elif opcion == 4:
        print('\n"Elegiste la división"\n')
        Numero1 = obtener_numero_float("Ingresa el dividendo: ")
        Numero2 = obtener_numero_float("Ingresa el divisor: ")
        print()
        dividir(Numero1,Numero2)
        print()
        espacio = input('"Presiona enter para continuar"\n')
        
    elif opcion == 5:
        print('\n"Elegiste la potencia"\n')
        Numero1 = obtener_numero_float("Ingresa el número base: ")
        Numero2 = obtener_numero_int("Ingresa la potencia: ")
        print()
        potencia(Numero1,Numero2)
        print()
        espacio = input('"Presiona enter para continuar"\n')
        
    elif opcion == 6:
        print('\n"Elegiste la raíz cuadrada"\n')
        Numero1 = obtener_numero_float("Ingresa el número base: ")
        print()
        RaizCuadrada(Numero1)
        print()
        espacio = input('"Presiona enter para continuar"\n')
        
    elif opcion == 7:
        print('\n"Saliste del programa"\n')
        
    else:
        print()
        print("****************\n"
              "Opción no Válida\n"
              "****************\n")
        print()
        espacio = input("Presiona enter e intenta otra opción\n")
