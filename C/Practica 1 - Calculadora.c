#include <stdio.h>

float sumar(float Numero1,float Numero2){
    printf("\n%.3f + %.3f = %.3f\n",Numero1, Numero2, Numero1+Numero2);}

float restar(float Numero1,float Numero2){
    printf("\n%.3f - %.3f = %.3f\n",Numero1, Numero2, Numero1-Numero2);}
    
float multiplicar(float Numero1,float Numero2){
    printf("\n%.3f x %.3f = %.3f\n",Numero1, Numero2, Numero1*Numero2);}
    
float dividir(float Dividendo,float Divisor){
    if (Divisor == 0){
        if (Dividendo == 0){
            printf("\n%.0f/%.0f = 0\n",Dividendo, Divisor);
        }
        else{
        printf("La división sobre 0 es inválida ya que el resultado de dividir\n");
        printf("cualquier número, excepto el 0, sobre 0 = ∞, en este caso %.3f/%.3f = infinito\n",Dividendo,Divisor);}}
    else {printf("\n%.3f/%.3f = %.3f\n",Dividendo, Divisor, Dividendo/Divisor);}}

double potencia(double NumeroBase,int Potencia){
    double NumeroMultiplicar, resultado, resultado_1;
    if (Potencia > 0){
        NumeroMultiplicar = NumeroBase;
        for (int i = 0; i < Potencia; i++){
            resultado = NumeroMultiplicar;
            NumeroMultiplicar*=NumeroBase;
        }
        printf("%lf elevado al número %d es: %lf",NumeroBase,Potencia,resultado);
    }
    else if (Potencia == 0){
        int resultado = 1;
        printf("\nTodo número elevado a la %d, da como resultado: %d\n",Potencia,resultado);
        printf("por lo tanto, %f elevado al número %d = %d\n",NumeroBase,Potencia,resultado);
    }
    else if (Potencia < 0){
        NumeroMultiplicar = NumeroBase;
        for (int i = 0; i < -Potencia-1; i++){
            resultado = NumeroMultiplicar;
            NumeroMultiplicar*=NumeroBase;
    }
    resultado = NumeroMultiplicar;
    resultado_1 = 1/NumeroMultiplicar;
    printf("\n%lf elevado al número %d da como resultado: 1/%lf que es igual a %.10lf\n",NumeroBase,Potencia,resultado,resultado_1);
}}

double raizCuadrada(double numero) {
    if (numero < 0) {
        printf("No se puede calcular la raíz cuadrada de un número negativo.\n");
        return -1.0; // Valor de error
    }

    double aproximacion = 1.0; // Valor inicial de aproximación

    while (1) {
        double siguiente = 0.5 * (aproximacion + numero / aproximacion);
        if (siguiente == aproximacion) {
            return siguiente;
        }
        aproximacion = siguiente;
    }
}

int main()
{
    char espacio;
    float Numero1, Numero2, Dividendo, Divisor;
    double NumeroBase;
    int Potencia, opcion;
    printf("*****************************"
           "\nEsta es una calculadora en C\n"
           "*****************************\n");
    do{
        printf("\n-------------------------------\n"
               "Seleciona la operación deseada:\n"
               "-------------------------------\n\n");
        puts("1. Suma\n"
             "2. Resta\n"
             "3. Multiplicación\n"
             "4. División\n"
             "5. Potencia\n"
             "6. Raíz Cuadrada\n"
             "7. Salir del programa\n");
        scanf("%d",&opcion);
        
        switch(opcion){
            
            case 1:
                printf("\n|Elegiste la suma|\n\n");
                printf("Ingresa el primer número: ");
                scanf("%f",&Numero1);
                printf("Ingresa el segundo número: ");
                scanf("%f",&Numero2);
                puts("");
                sumar(Numero1,Numero2);
                puts("");
                puts("Ingresa cualquier tecla para continuar\n");
                scanf("%s",&espacio);
            break;
            
            case 2:
                printf("\n|Elegiste la resta|\n\n");
                printf("Ingresa el primer número: ");
                scanf("%f",&Numero1);
                printf("Ingresa el segundo número: ");
                scanf("%f",&Numero2);
                puts("");
                restar(Numero1,Numero2);
                puts("");
                puts("Ingresa cualquier tecla para continuar\n");
                scanf("%s",&espacio);
            break;
            
            case 3:
                printf("\n|Elegiste la multiplicación|\n\n");
                printf("Ingresa el primer número: ");
                scanf("%f",&Numero1);
                printf("Ingresa el segundo número: ");
                scanf("%f",&Numero2);
                puts("");
                multiplicar(Numero1,Numero2);
                puts("");
                puts("Ingresa cualquier tecla para continuar\n");
                scanf("%s",&espacio);;
            break;
            
            case 4:
                printf("\n|Elegiste la división|\n\n");
                printf("Ingresa el dividendo: ");
                scanf("%f",&Dividendo);
                printf("Ingresa el divisor: ");
                scanf("%f",&Divisor);
                puts("");
                dividir(Dividendo,Divisor);
                puts("");
                puts("Ingresa cualquier tecla para continuar\n");
                scanf("%s",&espacio);
            break;
            
            case 5:
                printf("\n|Elegiste la potencia|\n\n");
                printf("Ingresa el número base: ");
                scanf("%lf",&NumeroBase);
                printf("Ingresa la potencia: ");
                scanf("%d",&Potencia);
                puts("");
                potencia(NumeroBase,Potencia);
                puts("");
                puts("Ingresa cualquier tecla para continuar\n");
                scanf("%s",&espacio);
            break;
            
            case 6:
                double resultado, numero;
                printf("\n|Elegiste la Raíz Cuadrada|\n\n");
                printf("Ingresa el número: ");
                scanf("%lf",&numero);
                puts("");
                if (numero == 0){
                    printf("√%.0lf es: 0",numero);
                }
                else {resultado = raizCuadrada(numero);
                if (resultado >= 0) {
                printf("La raíz cuadrada de %.2f es aproximadamente %.5f\n", numero, resultado);
                }}
                puts("");
                puts("Ingresa cualquier tecla para continuar\n");
                scanf("%s",&espacio);
            break;
            
            case 7:
                printf("¡¡Saliste del programa!!");
            break;
        }
    }while (opcion != 7);
    return 0;
}
