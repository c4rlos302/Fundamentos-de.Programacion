#include <stdio.h>
//Pide un numero y arroja un dia de la semana
int main()
{
    int dia;
    puts("Elige un dia de la semana del 1 al 7");
    scanf("%d",&dia);
    switch(dia)
    {
        case 1:puts("Elegiste el Lunes");
            break;
        
        case 2:puts("Elegiste el Martes");
            break;
            
        case 3:puts("Elegiste el Miercoles");
            break;
        
        case 4:puts("Elegiste el Jueves");
            break;
            
        case 5:puts("Elegiste el Viernes");
            break;
        
        case 6:puts("Elegiste el Sabado");
            break;
        
        case 7:puts("Elegiste el Domingo");
            break;
        
        default:puts("¡Error!");
    }
    return 0;
}
