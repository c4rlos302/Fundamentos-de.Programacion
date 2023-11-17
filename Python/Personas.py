personas = []

def obtener_numero_int(valor):
    while True:
        entrada = input(valor)
        if entrada.replace(" ", "").isdigit():
            numero = int(entrada)
            return numero
        else:
            print("\n¡Error! Ingresa una opción correcta.\n")

def agregar(personas):
    nombre = input("Escribe tu nombre: ")
    apellido_paterno = input("Escribe tu apellido paterno: ")
    apellido_materno = input("Escribe tu apellido materno: ")
    años = int(input("Escribe tus años trabajados: "))
    print("Clave 1")
    print("Clave 2")
    print("Clave 3")
    clave = int(input("Escribe tu clave de departamento: "))
    personas.append([nombre,apellido_paterno,apellido_materno,años,clave])
    print()

def mostrar(personas):
    for persona in personas:
        print(f"Nombre: {persona[0]}")
        print(f"Apellido Paterno: {persona[1]}")
        print(f"Apellido Materno: {persona[2]}")
        print(f"Años trabajados: {persona[3]}")
        print(f"Clave de departamento: {persona[4]}")
        print()
        
def buscar(personas):
    nombre = input("Nombre: ")
    for persona in personas:
        if persona[0] == nombre:
            print(f"Nombre: {persona[0]}")
            print(f"Apellido Paterno: {persona[1]}")
            print(f"Apellido Materno: {persona[2]}")
            print(f"Años trabajados: {persona[3]}")
            print(f"Clave de departamento: {persona[4]}")
            print()
            break
        else:print("Persona no encontrada")
    print()

def modificar(personas):
    nombre = input("Nombre: ")
    for persona in personas:
        if persona[0] == nombre:
            nombre = input(f"Nombre: ")
            apellido_paterno = input(f"Apellido Paterno: ")
            apellido_materno = input(f"Apellido Materno: ")
            años = input(f"Años trabajados: ")
            clave = input(f"Clave de departamento: ")
            persona[0] = nombre
            persona[1] = apellido_paterno
            persona[2] = apellido_materno
            persona[3] = años
            persona[4] = clave     
        else:print("Persona no encontrada")
    print()

def eliminar(personas):
    nombre = input("Nombre: ")
    for persona in personas:
        if persona[0] == nombre:
            personas.remove(persona)
        else:print("Persona no encontrada")
    print()

def menu():
    print("1. Agregar")
    print("2. Mostrar")
    print("3. Buscar")
    print("4. Modificar")
    print("5. Eliminar")
    print("6. Resultados")
    print("7. Salir")
    opcion = obtener_numero_int("\nOpción: ")
    print()
    return opcion

def mostrar_resultados(personas):
    for persona in personas:
        print(f"Nombre: {persona[0]}")
        print(f"Apellido Paterno: {persona[1]}")
        print(f"Apellido Materno: {persona[2]}")
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
        
