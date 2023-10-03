num = float(input("Dame un número: \n"))
print("\n")
print('Tu cantidad es "'+str(num)+'", elige centimetros o metros:')
print("A)Centimetros")
print("B)Metros")
conversion = str(input("\n"))

if conversion == 'A' or conversion == 'a':
    print('Tu cantidad es "'+str(num)+'cm", elige a que lo quieres convertir:')
    print("A)Milimetros")
    print("B)Decimetros")
    print("C)Metros")
    valor = str(input("\n"))
    
    if valor == 'A' or valor == 'a':
        print("Tu resultado es: ",num*10,"mm\n")
        
    elif valor == 'B' or valor == 'b':
        print("Tu resultado es: ",num/10,"dm\n")
        
    elif valor == 'C' or valor == 'c':
        print("Tu resultado es: ",num/100,"m\n")
    else: print("Error!!")
    
    
elif conversion == 'B' or conversion == 'b':
    print('Tu cantidad es "'+str(num)+'m", elige a que lo quieres convertir:')
    print("A)Decametros")
    print("B)Kilometros")
    valor = str(input("\n"))
    
    if valor == 'A' or valor == 'a':
        print("Tu resultado es: ",num/10,"dam\n")
        
    elif valor == 'B' or valor == 'b':
        print("Tu resultado es: ",num/1000,"km\n")
        
    else: print("Error!!")
    

else:print("Error!!")
