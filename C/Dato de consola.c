#include <stdio.h>

int main()
{
    char palabra[80];
    int entero;
    float flotante;
    
    printf("Dame una palabra\n");
    scanf("%s",&palabra);
    
    printf("Dame un numero entero\n");
    scanf("%d",&entero);
    
    printf("Dame un numero flotante\n");
    scanf("%f",&flotante);
    
    printf("Tu palabra es: %s\n",palabra);
    printf("Tu entero es: %d\n",entero);
    printf("Tu flotante es: %.2f\n\a",flotante);
  
    return 0;
}
