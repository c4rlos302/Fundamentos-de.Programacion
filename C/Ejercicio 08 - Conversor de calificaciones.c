//Conversor de sistema de calificaciones numérico de a uno alfabético
    
    /*A+ (97–100), A (93–96), A- (90–92), B+ (87–89), B (83–86), B- (80–82) ,
    C+ (77–79), C (73–76), C- (70–72), D+ (67–69), D (65–66), D- (menos de 65)*/
    
    #include <stdio.h>
    
    int main()
    {
        float calificacion_numero;
        char* calificacion_letra;
        printf("Escribe tu calificación: ");
        scanf("%f",&calificacion_numero);
        
        if (calificacion_numero >= 97 && calificacion_numero <=100)
        {
            calificacion_letra = "A+";
        }
        else if (calificacion_numero >=93 && calificacion_numero <97)
        {
            calificacion_letra = "A";
        }
        else if (calificacion_numero >=90 && calificacion_numero <93)
        {
            calificacion_letra = "A-";
        }
        else if (calificacion_numero >=87 && calificacion_numero <90)
        {
            calificacion_letra = "B+";
        }
        else if (calificacion_numero >=83 && calificacion_numero <87)
        {
            calificacion_letra = "B";
        }
        else if (calificacion_numero >=80 && calificacion_numero <83)
        {
            calificacion_letra = "B-";
        }
        else if (calificacion_numero >=77 && calificacion_numero <80)
        {
            calificacion_letra = "C+";
        }
        else if (calificacion_numero >=73 && calificacion_numero <77)
        {
            calificacion_letra = "C";
        }
        else if (calificacion_numero >=70 && calificacion_numero <73)
        {
            calificacion_letra = "C-";
        }
        else if (calificacion_numero >=67 && calificacion_numero <70)
        {
            calificacion_letra = "D+";
        }
        else if (calificacion_numero >=65 && calificacion_numero <67)
        {
            calificacion_letra = "D";
        }
        else if (calificacion_numero >=0  &&calificacion_numero <65)
        {
            calificacion_letra = "D-";
        }
    else{ calificacion_letra = "calificación no válida";}
    
    
    printf("Tu calificación es: %s",calificacion_letra);
    
        return 0;
    }
