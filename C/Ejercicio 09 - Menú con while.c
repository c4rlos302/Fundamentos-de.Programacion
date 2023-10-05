#include <stdio.h>
//Pide un numero y arroja un dia de la semana
int main()
{
    int dia;
    while(dia != 8){
    printf("Elige un dia de la semana del 1 al 7\t");
    puts("8) Salir");
    scanf("%d",&dia);
    switch(dia)
    {
        case 1:puts("Elegiste el Lunes");
        printf("\n");
            break;
        
        case 2:puts("Elegiste el Martes");
        printf("\n");
            break;
            
        case 3:puts("Elegiste el Miercoles");
        printf("\n");
            break;
        
        case 4:puts("Elegiste el Jueves");
        printf("\n");
            break;
            
        case 5:puts("Elegiste el Viernes");
        printf("\n");
            break;
        
        case 6:puts("Elegiste el Sabado");
        printf("\n");
            break;
        
        case 7:puts("Elegiste el Domingo");
        printf("\n");
            break;
        
        case 8:puts("Saliste del programa");
        printf("\n");
            break;
        
        default:puts("¡Error!");
        printf("\n");
    }
    }
    return 0;
}
