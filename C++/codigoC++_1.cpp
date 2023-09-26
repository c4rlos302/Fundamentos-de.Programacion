#include <iostream>

using namespace std;

int main()
{
    int ope;
    int sum;
    int num1;
    int num2;
    num1=2;
    num2=3;

    cout<<num1+num2<<"\n\n";
    cout<<(34*num2)-(num1*53)<<"\n\n";
    sum=num1+num2;
    ope=(34*num2)-(num1*53);
    
if(sum<ope){
    cout<<"El segundo resultado es mayor que el primero\n\n";
}
else{
    cout<<"El primer resultado es el mayor de los dos\n\n";
}
    return 0;
}
