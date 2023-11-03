#include <iostream>

using namespace std;
void ARREGLO_ENTEROS(){
    int a;
    cout<<"Elige el tamaño de tu arreglo de números: ";
    cin>>a;
    int Arreglo_Numeros_Enteros[a];
    for (int i = 0; i < a; i++){
        cout<<"Ingresa el valor de la posición "<<i+1<<" de tu arreglo de números: ";
        cin>>Arreglo_Numeros_Enteros[i];
    }
    for (int j = 0; j < a; j++){
        cout<<"El valor de tu arreglo en la posición "<<j+1<<" es: "<<Arreglo_Numeros_Enteros[j]<<endl;
    }
    cout<<endl;
}

void ARREGLO_FLOTANTES(){
    int b;
    cout<<"Elige el tamaño de tu arreglo de flotantes: ";
    cin>>b;
    float Arreglo_Numeros_Flotantes[b];
    for (int k = 0; k < b; k++){
        cout<<"Ingresa el valor de la posición "<<k+1<<" de tu arreglo de números: ";
        cin>>Arreglo_Numeros_Flotantes[k];
    }
    for (int l = 0; l < b; l++){
        cout<<"El valor de tu arreglo en la posición "<<l+1<<" es: "<<Arreglo_Numeros_Flotantes[l]<<endl;
    }
    cout<<endl;
}

void ARREGLO_STRING(){
    int c;
    cout<<"Elige el tamaño de tu arreglo de strings: ";
    cin>>c;
    string Arreglo_Strings[c];
    for (int m = 0; m < c; m++){
        cout<<"Ingresa el valor de la posición "<<m+1<<" de tu arreglo de números: ";
        cin>>Arreglo_Strings[m];
    }
    for (int n = 0; n < c; n++){
        cout<<"El valor de tu arreglo en la posición "<<n+1<<" es: "<<Arreglo_Strings[n]<<endl;
    }
    cout<<endl;
}

int main()
{
    int opcion;
    do{
    cout<<"\n------------------------------------------------\n"
            "Seleciona el tipo de arreglo que quieres hacer:\n"
            "------------------------------------------------\n"<<endl;
    cout<<"1. Arreglo de enteros\n"
          "2. Arreglo de flotantes\n"
          "3. Arreglo de strings\n"
          "4. Salir\n"<<endl;
    cin>>opcion;
    cout<<endl;
    switch(opcion){
        case 1:
        cout<<"Elegiste arreglo de enteros\n"<<endl;
            ARREGLO_ENTEROS();
        break;
        
        case 2:
        cout<<"Elegiste arreglo de flotantes\n"<<endl;
            ARREGLO_FLOTANTES();
        break;
        
        case 3:
        cout<<"Elegiste arreglo de strings\n"<<endl;
            ARREGLO_STRING();
        break;
        
        case 4:
            cout<<"Saliste de el programa"<<endl;
        break;
        
        default:
        cout<<"Elige una opción válida"<<endl;
    }
    
    if (opcion == 4){
        break;
    }
    else{string b;
    cout<<"Presiona cualquier tecla para continuar"<<endl;
    cin>>b;}
    
    }while(opcion != 4);
    return 0;
}
