#include <stdio.h>

int main()

{
    int mod;
    int num1;
    int num2;
    int resultado;
    
    printf("Ingrese la modalidad (suma=1, resta=2, multiplicación=3, división=4\n");
    scanf("%d",&mod);
    if(mod==1){
        printf("Ingrese el primer número de la suma:\n");
        scanf("%d",&num1);
        printf("Ingrese el segundo número:\n");
        scanf("%d",&num2);
        resultado = num1+num2;
        printf("El resultado es : %d\n",resultado);
    }
    if(mod==2){
        printf("Ingrese el primer número de la resta:\n");
        scanf("%d",&num1);
        printf("Ingrese el segundo número:\n");
        scanf("%d",&num2);
        resultado = num1-num2;
        printf("El resultado es : %d\n",resultado);
    }
    if(mod==3){
        printf("Ingrese el primer número de la multiplicacion:\n");
        scanf("%d",&num1);
        printf("Ingrese el segundo número:\n");
        scanf("%d",&num2);
        resultado = num1*num2;
        printf("El resultado es : %d\n",resultado);
    }
    if(mod==4){
        printf("Ingrese el primer número de la division:\n");
        scanf("%d",&num1);
        printf("Ingrese el segundo número:\n");
        scanf("%d",&num2);
        resultado = num1/num2;
        printf("El resultado es :%d\n",resultado);
    }
    if(mod>4,mod<1){
        printf("¡¡Error!!\n");
    }

    return 0;
}
