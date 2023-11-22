personas = []

def palabra_convertida(valor):
    while True:
        entrada = input(valor)
        palabra = entrada.capitalize().replace(" ", "")
        return palabra

def obtener_numero_int(valor):
    while True:
        entrada = input(valor)
        if entrada.replace(" ", "").isdigit():
            numero = int(entrada)
            return numero
        else:
            print("\n¡Error! Ingresa una opción correcta.\n")

def obtener_numero_años(valor):
    while True:
        entrada = input(valor)
        if entrada.replace(" ", "").isdigit():
            numero = int(entrada)
            return numero
        else:
            print("\n¡Error! Ingresa un número de años.\n")

def obtener_numero_1_3(valor):
    while True:
        entrada = input(valor)
        if entrada.replace(" ", "").isdigit():
            entrada = int(entrada)
            if entrada >= 1 and entrada <= 3:
                numero = int(entrada)
                return numero
            else:print("\n¡Clave Inválida! Ingresa un número del 1 al 3\n")
        else:
            print("\n¡Error! Ingresa un número entero\n")

def agregar(personas):
    nombre = palabra_convertida("Escribe tu nombre: ")
    apellido_paterno = palabra_convertida("Escribe tu apellido paterno: ")
    apellido_materno = palabra_convertida("Escribe tu apellido materno: ")
    años = obtener_numero_años("Escribe tus años trabajados: ")
    print("Departamento de Atención a Clientes (Clave 1)")
    print("Departamento de Logistica (Clave 2)")
    print("Gerencia (Clave 3)")
    clave = obtener_numero_1_3("Escribe tu clave de departamento: ")
    personas.append([nombre,apellido_paterno,apellido_materno,años,clave])
    print()

def mostrar(personas):
    for persona in personas:
        print(f"Nombre: {persona[0]}")
        print(f"Apellido Paterno: {persona[1]}")
        print(f"Apellido Materno: {persona[2]}")
        print(f"Años trabajados: {persona[3]}")
        print(f"Clave de departamento: {persona[4]}\n")

def buscar(personas):
    nombre = palabra_convertida("Nombre: ")
    for persona in personas:
        if persona[0] == nombre:
            print(f"Nombre: {persona[0]}")
            print(f"Apellido Paterno: {persona[1]}")
            print(f"Apellido Materno: {persona[2]}")
            print(f"Años trabajados: {persona[3]}")
            print(f"Clave de departamento: {persona[4]}\n")
            break
        else:print("Persona no encontrada")
    print()

def modificar(personas):
    nombre = palabra_convertida("Nombre: ")
    for persona in personas:
        if persona[0] == nombre:
            while True:
                print()
                print(f"1. Nombre: {persona[0]}")
                print(f"2. Apellido Paterno: {persona[1]}")
                print(f"3. Apellido Materno: {persona[2]}")
                print(f"4. Años trabajados: {persona[3]}")
                print(f"5. Clave de departamento: {persona[4]}")
                print(f"6. Dejar de modificar\n")
                opcion = obtener_numero_int("Que quieres modificar: ")
                if opcion == 1:
                    nombre = palabra_convertida("Nombre: ")
                    persona[0] = nombre
                elif opcion == 2:
                    apellido_paterno = palabra_convertida("Apellido Paterno: ")
                    persona[1] = apellido_paterno
                elif opcion == 3:
                    apellido_materno = palabra_convertida("Apellido Materno: ")
                    persona[2] = apellido_materno
                elif opcion == 4:
                    años = obtener_numero_años("Años trabajados: ")
                    persona[3] = años
                elif opcion == 5:
                    clave = obtener_numero_1_3("Clave de departamento: ")
                    persona[4] = clave
                elif opcion == 6:
                    break
        else:print("Persona no encontrada")
    print()

def eliminar(personas):
    nombre = palabra_convertida("Nombre: ")
    personas_a_eliminar = []
    for persona in personas:
        if persona[0] == nombre:
            personas_a_eliminar.append(persona)
    if personas_a_eliminar:
        for persona in personas_a_eliminar:
            personas.remove(persona)
        print("Persona eliminada\n")
    else:
        print("Persona no encontrada\n")
    print()

def menu():
    print("1. Agregar persona")
    print("2. Mostrar personas")
    print("3. Buscar persona")
    print("4. Modificar persona")
    print("5. Eliminar persona")
    print("6. Mostrar resultados")
    print("7. Salir")
    opcion = obtener_numero_int("\nOpción: ")
    print()
    return opcion

def mostrar_resultados(personas):
    for persona in personas:
        print(f"A {persona[0]} {persona[1]} {persona[2]}")
        if persona[4] == 1:
            if persona[3] == 1:
                Vacaciones = 6
                print(f"Le pertenecen {Vacaciones} dias de vacaciones")
            elif persona[3] >= 2 and persona[3] <= 6:
                Vacaciones = 14
                print(f"Le pertenecen {Vacaciones} dias de vacaciones")
            elif persona[3] >= 7:
                Vacaciones = 20
                print(f"Le pertenecen {Vacaciones} dias de vacaciones")
            else: print("\nNúmero de Años no Válidos")
        
        elif persona[4] == 2:
            if persona[3] == 1:
                Vacaciones = 7
                print(f"Le pertenecen {Vacaciones} dias de vacaciones")
            elif persona[3] >= 2 and persona[3] <= 6:
                Vacaciones = 15
                print(f"Le pertenecen {Vacaciones} dias de vacaciones")
            elif persona[3] >= 7:
                Vacaciones = 22
                print(f"Le pertenecen {Vacaciones} dias de vacaciones")
            else: print("\nNúmero de Años no Válidos")
        
        elif persona[4] == 3:
            if persona[3] == 1:
                Vacaciones = 10
                print(f"Le pertenecen {Vacaciones} dias de vacaciones")
            elif persona[3] >= 2 and persona[3] <= 6:
                Vacaciones = 20
                print(f"Le pertenecen {Vacaciones} dias de vacaciones")
            elif persona[3] >= 7:
                Vacaciones = 30
                print(f"Le pertenecen {Vacaciones} dias de vacaciones")
            else: print("\nNúmero de Años no Válidos")
        else: print("\nClave no Válida")
        
        print()

print("\nCompañia multinacional de Rappi") #Este programa calcula los dias de vacaciones de las personas 
print("*******************************\n") #segun al departamento que pertenecen y los años trabajados 
#Tres departamentos:

    #Departamento de Atención a Clientes (Clave 1)

        #Con 1 año de servicio, reciben 6 dias de vacaciones.
        #Con 2 a 6 años de servicio, reciben 14 dias de vacaciones.
        #A partir de 7 años de servicio, reciben 20 dias de vacaciones.

    #Departamento de Logistica (Clave 2)

        #Con 1 año de servicio, reciben 7 dias de vacaciones.
        #Con 2 a 6 años de servicio, reciben 15 dias de vacaciones.
        #A partir de 7 años de servicio, reciben 22 dias de vacaciones.

    #Gerencia (Clave 3)
    
        #Con 1 año de servicio, reciben 10 dias de vacaciones.
        #Con 2 a 6 años de servicio, reciben 20 dias de vacaciones.
        #A partir de 7 años de servicio, reciben 30 dias de vacaciones.

agregar(personas)

while(True):
    opcion = menu()
    if opcion == 1:
        agregar(personas)
    elif opcion == 2:
        mostrar(personas)
    elif opcion == 3:
        buscar(personas)
    elif opcion == 4:
        modificar(personas)
    elif opcion == 5:
        eliminar(personas)
    elif opcion == 6:
        mostrar_resultados(personas)
    elif opcion == 7:
        print("Saliste del programa")
        break
    else: print("Opción Inválida")
