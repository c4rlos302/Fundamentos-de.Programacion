personas = [["Juan","Peréz","Salazar",3,1],["María","García","Velasquez",8,2]]

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
        if entrada.replace(" ", "").replace(".","").isdigit():
            numero = float(entrada)
            return numero
        else:
            print("\n¡Error! Ingresa el número de años\n")

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
    print("*****************************")
    for persona in personas:
        print(f"Nombre: {persona[0]}")
        print(f"Apellido Paterno: {persona[1]}")
        print(f"Apellido Materno: {persona[2]}")
        print(f"Años trabajados: {persona[3]}")
        print(f"Clave de departamento: {persona[4]}\n")
    print("*****************************")

def mostrar_nombres(personas):
    i = 0
    for persona in personas:
        i += 1
        print(f"Persona {i}: {persona[0]}")
    print()

def buscar(personas):
    nombre = palabra_convertida("Ingresa el nombre de la persona a buscar: ")
    persona_encontrada = False
    for persona in personas:
        if persona[0] == nombre:
            persona_encontrada = True
            break
    if persona_encontrada == True:
            print(f"Nombre: {persona[0]}")
            print(f"Apellido Paterno: {persona[1]}")
            print(f"Apellido Materno: {persona[2]}")
            print(f"Años trabajados: {persona[3]}")
            print(f"Clave de departamento: {persona[4]}\n")
    else:print("Persona no encontrada")
    print()

def modificar(persona):
    while True:
        print()
        print(f"1. Nombre: {persona[0]}")
        print(f"2. Apellido Paterno: {persona[1]}")
        print(f"3. Apellido Materno: {persona[2]}")
        print(f"4. Años trabajados: {persona[3]}")
        print(f"5. Clave de departamento: {persona[4]}")
        print(f"6. Dejar de modificar\n")
        opcion = obtener_numero_int("¿Qué quieres modificar?: ")
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

def eliminar(persona, personas):
    personas.remove(persona)
    print(f"La persona {persona[0]} ha sido eliminada\n")

def mostrar_resultados(personas):
    print("\n___________________________________\n")
    for persona in personas:
        print(f"A {persona[0]} {persona[1]} {persona[2]}")
        if persona[4] == 1:
            if persona[3] > 0 and persona[3] <= 1:
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
            if persona[3] > 0 and persona[3] <= 1:
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
            if persona[3] > 0 and persona[3] <= 1:
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
    print("___________________________________\n")

def mostrar_con_indices(personas):
    for i, persona in enumerate(personas, start=1):
        print(f"{i}. Nombre: {persona[0]}")

def seleccionar_persona(personas):
    mostrar_con_indices(personas)
    while True:
        indice = obtener_numero_int("\nSelecciona el número de la persona: ")
        if 1 <= indice <= len(personas):
            return personas[indice - 1]
        else:
            print("\n¡Error! Ingresa un número válido.\n")

def menu():
    print("Que operación quiere hacer:\n")
    print("1. Agregar persona")
    print("2. Mostrar personas")
    print("3. Buscar persona")
    print("4. Modificar persona")
    print("5. Eliminar persona")
    print("6. Mostrar resultados")
    print("7. Regresar")
    opcion = obtener_numero_int("\nElige una opción: ")
    print()
    return opcion

def menu_principal():
    print("1. Agregar persona")
    print("2. Trabajar con una persona")
    print("3. Mostrar personas")
    print("4. Mostrar resultados")
    print("5. Salir")
    opcion = obtener_numero_int("\nElige una opción: ")
    print()
    return opcion

def submenu():
    print(f"\nQue quieres hacer con: {persona_seleccionada[0]} {persona_seleccionada[1]} {persona_seleccionada[2]}\n")
    print("1. Mostrar información")
    print("2. Modificar información")
    print("3. Eliminar persona")
    print("4. Regresar")
    opcion = obtener_numero_int("\nElige una operación: ")
    print()
    return opcion

print("*******************************")
print("Compañía multinacional de Rappi")  
print("*******************************\n")
while True:
    opcion_principal = menu_principal()
    if opcion_principal == 1:
        agregar(personas)
    elif opcion_principal == 2:
        persona_seleccionada = seleccionar_persona(personas)
        while True:
            opcion = submenu()
            if opcion == 1:
                mostrar([persona_seleccionada])
            elif opcion == 2:
                modificar(persona_seleccionada)
            elif opcion == 3:
                eliminar(persona_seleccionada, personas)
                break
            elif opcion == 4:
                break
            else:
                print("Opción Inválida")
    elif opcion_principal == 3:
        mostrar(personas)
    elif opcion_principal == 4:
        mostrar_resultados(personas)
    elif opcion_principal == 5:
        print("Saliste del programa")
        break
    else:
        print("Opción Inválida")
