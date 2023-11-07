#include <stdio.h>
void convertir_a_Minuscula(char *cadena)
{
    while (*cadena)
    {
        if (*cadena >= 65 && *cadena <= 90)
        {
            *cadena = *cadena + 32;
        }
        else if(*cadena == 165)//Ñ
        {
            *cadena = *cadena - 1;
        }
        else if(*cadena == 181)//Á
        {
            *cadena = *cadena - 21;
        }
        else if(*cadena == 144)//É
        {
            *cadena = *cadena - 14;
        }
        else if(*cadena == 214)//Í
        {
            *cadena = *cadena - 53;
        }
        else if(*cadena == 224)//Ó
        {
            *cadena = *cadena - 62;
        }
        else if(*cadena == 233)//Ú
        {
            *cadena = *cadena - 70;
        }
        else if(*cadena == 142)//Ä
        {
            *cadena = *cadena - 10;
        }
        else if(*cadena == 211)//Ë
        {
            *cadena = *cadena - 74;
        }
        else if(*cadena == 216)//Ï
        {
            *cadena = *cadena - 77;
        }
        else if(*cadena == 153)//Ö
        {
            *cadena = *cadena - 5;
        }
        else if(*cadena == 154)//Ü
        {
            *cadena = *cadena - 25;
        }
        *cadena++;
    }
}
void convertir_a_Mayuscula(char *cadena)
{
    while (*cadena)
    {
        if (*cadena >= 97 && *cadena <= 122)
        {
            *cadena = *cadena - 32;
        }
        else if(*cadena == 164)//ñ
        {
            *cadena = *cadena + 1;
        }
        else if(*cadena == 160)//á
        {
            *cadena = *cadena + 21;
        }
        else if(*cadena == 130)//é
        {
            *cadena = *cadena + 14;
        }
        else if(*cadena == 161)//í
        {
            *cadena = *cadena + 53;
        }
        else if(*cadena == 162)//ó
        {
            *cadena = *cadena + 62;
        }
        else if(*cadena == 163)//ú
        {
            *cadena = *cadena + 70;
        }
        else if(*cadena == 132)//ä
        {
            *cadena = *cadena + 10;
        }
        else if(*cadena == 137)//ë
        {
            *cadena = *cadena + 74;
        }
        else if(*cadena == 139)//ï
        {
            *cadena = *cadena + 77;
        }
        else if(*cadena == 148)//ö
        {
            *cadena = *cadena + 5;
        }
        else if(*cadena == 129)//ü
        {
            *cadena = *cadena + 25;
        }
        *cadena++;
    }
}
int main()
{
    int opcion = 0;
    char texto[60];
    do
    {
        printf("Ingresa tu cadena: ");
        scanf("%s", texto);
