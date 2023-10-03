#include <iostream>

using namespace std;

int main()
{
    char conversion, valor;
    double num;
    cout<<"Dame un valor"<<endl;
    cout<<endl;
    cin>>num;
    cout<<endl;
    
    cout<<"Tu cantidad es "<<char(34)<<num<<char(34)<<", elige centimetros o metros:"<<endl;
    cout<<endl;
    cout<<"A)Centimetros"<<endl;
    cout<<"B)Metros"<<endl;
    cout<<endl;
    cin>>conversion;
    cout<<endl;
    
    if (conversion=='A' ||conversion=='a') //Cantidad en Centimetros
        {
        cout<<"Tu cantidad es "<<char(34)<<num<<"cm"<<char(34)<<", elige a que lo quieres convertir:"<<endl;
        cout<<endl;
        cout<<"A)Milimetros"<<endl;
        cout<<"B)Decimetros"<<endl;
        cout<<"C)Metros"<<endl;
        cout<<endl;
        cin>>valor;
        cout<<endl;
            
        if (valor=='A'||valor=='a')//Convertir a Milimetros
            {
            cout<<"Tu resultado es: "<<num*10<<"mm"<<endl;
            }
        
        else if(valor =='B'||valor=='b') //Convertir a Decimetros
            {
            cout<<"Tu resultado es: "<<num/10<<"dm"<<endl;
            }
        
        else if(valor=='C'||valor=='c') //Convertir a Metros
            {
            cout<<"Tu resultado es: "<<num/100<<"m"<<endl;
            }
        else {cout<<"Error"<<endl;}
        }
        
    else if (conversion=='B' ||conversion=='b')//Cantidad en Metros
        {
        cout<<"Tu cantidad es "<<char(34)<<num<<"m"<<char(34)<<", elige a que lo quieres convertir:"<<endl;
        cout<<endl;
        cout<<"A)Decametros"<<endl;
        cout<<"B)Kilometros"<<endl;
        cout<<endl;
        cin>>valor;
        cout<<endl;
        if (valor=='A'||valor=='a')//Convertir a Milimetros
            {
            cout<<"Tu resultado es: "<<num/10<<"dam"<<endl;
            }
        
        else if(valor =='B'||valor=='b') //Convertir a Decimetros
            {
            cout<<"Tu resultado es: "<<num/1000<<"km"<<endl;
            }
        
        else {cout<<"Error"<<endl;}
        }
 
    else {cout<<"Error"<<endl;}

    return 0;
}
