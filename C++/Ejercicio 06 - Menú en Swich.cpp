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
    switch(conversion)
    {
        case 'A'://Cantidad en Centimetros
        case 'a':
        cout<<"Tu cantidad es "<<char(34)<<num<<"cm"<<char(34)<<", elige a que lo quieres convertir:"<<endl;
        cout<<endl;
        cout<<"A)Milimetros"<<endl;
        cout<<"B)Decimetros"<<endl;
        cout<<"C)Metros"<<endl;
        cout<<endl;
        cin>>valor;
        cout<<endl;
        switch(valor)
        {
            case 'A'://Convertir a Milimetros
            case 'a':
            cout<<"Tu resultado es: "<<num*10<<"mm"<<endl;
            break;
        
            case 'B'://Convertir a Decimetros
            case 'b':
            cout<<"Tu resultado es: "<<num/10<<"dm"<<endl;
            break;
        
            case 'C'://Convertir a Metros
            case 'c':
            cout<<"Tu resultado es: "<<num/100<<"m"<<endl;
            break;
        
            default:cout<<"Error"<<endl;
        }
        break;
        
        case 'B'://Cantidad en Metros
        case 'b':
        cout<<"Tu cantidad es "<<char(34)<<num<<"m"<<char(34)<<", elige a que lo quieres convertir:"<<endl;
        cout<<endl;
        cout<<"A)Decametros"<<endl;
        cout<<"B)Kilometros"<<endl;
        cout<<endl;
        cin>>valor;
        cout<<endl;
        switch(valor)
        {
            case 'A'://Convertir a Decametros
            case 'a':
            cout<<"Tu resultado es: "<<num/10<<"dam"<<endl;
            break;
        
            case 'B'://Convertir a Kilometros
            case 'b':
            cout<<"Tu resultado es: "<<num/1000<<"km"<<endl;
            break;
        
            default:cout<<"Error"<<endl;
        }
        break;
        
        default:cout<<"Error"<<endl;
    }

    return 0;
}
