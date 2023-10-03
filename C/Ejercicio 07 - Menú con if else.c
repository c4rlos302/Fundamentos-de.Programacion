#include <stdio.h>
//Pide un numero e imprime un dia de la semana
int main()
{
    int dia;
    puts("Elige un dia de la semana del 1 al 7");
    scanf("%d",&dia);
    if (dia==1)
    {
        puts("Elegiste el Lunes");
    }
    else if (dia==2)
    {
        puts("Elegiste el Martes");
    }
    else if (dia==3)
    {
        puts("Elegiste el Miercoles");
    }
    else if (dia==4)
    {
        puts("Elegiste el Jueves");
    }
    else if (dia==5)
    {
        puts("Elegiste el Viernes");
    }
    else if (dia==6)
    {
        puts("Elegiste el Sabado");
    }
    else if (dia==7)
    {
        puts("Elegiste el Domingo");
    }
    else {puts("¡Error!");}
    return 0;
}
