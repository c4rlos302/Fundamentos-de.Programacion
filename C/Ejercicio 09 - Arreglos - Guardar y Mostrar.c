#include <stdio.h>

void ARREGLO_ENTEROS() {
    int a;
    printf("Elige el tamaño de tu arreglo de números: ");
    scanf("%d", &a);
    int Arreglo_Numeros_Enteros[a];
    
    for (int i = 0; i < a; i++) {
        printf("Ingresa el valor de la posición %d de tu arreglo de números: ", i + 1);
        scanf("%d", &Arreglo_Numeros_Enteros[i]);
    }
    printf("\n");
    for (int j = 0; j < a; j++) {
        printf("El valor de tu arreglo en la posición %d es: %d\n", j + 1, Arreglo_Numeros_Enteros[j]);
    }

    printf("\n");
}

void ARREGLO_FLOTANTES() {
    int b;
    printf("Elige el tamaño de tu arreglo de flotantes: ");
    scanf("%d", &b);
    float Arreglo_Numeros_Flotantes[b];

    for (int k = 0; k < b; k++) {
        printf("Ingresa el valor de la posición %d de tu arreglo de números: ", k + 1);
        scanf("%f", &Arreglo_Numeros_Flotantes[k]);
    }
    printf("\n");
    for (int l = 0; l < b; l++) {
        printf("El valor de tu arreglo en la posición %d es: %f\n", l + 1, Arreglo_Numeros_Flotantes[l]);
    }

    printf("\n");
}

void ARREGLO_STRING() {
    int c;
    printf("Elige el tamaño de tu arreglo de strings: ");
    scanf("%d", &c);
    char Arreglo_Strings[c][100];

    for (int m = 0; m < c; m++) {
        printf("Ingresa el valor de la posición %d de tu arreglo de números: ", m + 1);
        scanf("%s", Arreglo_Strings[m]);
    }
    printf("\n");
    for (int n = 0; n < c; n++) {
        printf("El valor de tu arreglo en la posición %d es: %s\n", n + 1, Arreglo_Strings[n]);
    }

    printf("\n");
}

int main() {
    int opcion;
    do {
        printf("\n------------------------------------------------\n"
               "Selecciona el tipo de arreglo que quieres hacer:\n"
               "------------------------------------------------\n\n");
        printf("1. Arreglo de enteros\n"
               "2. Arreglo de flotantes\n"
               "3. Arreglo de strings\n"
               "4. Salir\n\n");
        scanf("%d", &opcion);
        printf("\n");

        switch (opcion) {
            case 1:
                printf("Elegiste arreglo de enteros\n\n");
                ARREGLO_ENTEROS();
                break;

            case 2:
                printf("Elegiste arreglo de flotantes\n\n");
                ARREGLO_FLOTANTES();
                break;

            case 3:
                printf("Elegiste arreglo de strings\n\n");
                ARREGLO_STRING();
                break;

            case 4:
                printf("Saliste del programa\n");
                break;

            default:
                printf("Elige una opción válida\n\n");
        }

        if (opcion == 4) {
            break;
        } else {
            char b[10];
            printf("Presiona cualquier tecla y Enter para continuar: ");
            scanf("%s", b);
        }

    } while (opcion != 4);

    return 0;
}
