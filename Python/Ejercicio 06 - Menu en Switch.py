print("\nCompañia multinacional de Rappi") #Debe de solicitar "Nombre", "Clave de departamento", "Antiguedad del trabajador".
print("*******************************\n") #Debe imprimir "Nombre", "Dias que le tocan de vacaciones".
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

Nombre = input("Escribe tu nombre: ")
print("\n",Nombre, "a que departamento perteneces:\n"
      "\nDepartamento de Atención a Clientes (Clave 1)\n"
      "Departamento de Logistica (Clave 2)\n"
      "Gerencia (Clave 3)\n")
Clave = int(input("Ingresa el número de clave: "))

if Clave == 1:
    Años = int(input("Cuantos años tienes trabajando: "))
    if Años == 1:
        Vacaciones = 6
    elif Años >= 2 and Años <= 6:
        Vacaciones = 14
    elif Años >= 7:
        Vacaciones = 20
    else: print("\nNúmero de Años no Válidos")

elif Clave == 2:
    Años = int(input("Cuantos años tienes trabajando: "))
    if Años == 1:
        Vacaciones = 7
    elif Años >= 2 and Años <= 6:
        Vacaciones = 15
    elif Años >= 7:
        Vacaciones = 22
    else: print("\nNúmero de Años no Válidos")

elif Clave == 3:
    Años = int(input("Cuantos años tienes trabajando: "))
    if Años == 1:
        Vacaciones = 10
    elif Años >= 2 and Años <= 6:
        Vacaciones = 20
    elif Años >= 7:
        Vacaciones = 30
    else: print("\nNúmero de Años no Válidos")

else: print("\nClave no Válida")

print("\n---------------------------------------")
print(Nombre + " te pertenecen", Vacaciones, "días de vacaciones")
print("---------------------------------------\n")
