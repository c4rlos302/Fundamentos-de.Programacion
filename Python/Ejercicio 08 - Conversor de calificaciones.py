#Conversor de sistema de calificaciones numérico de a uno alfabético

'''A+ (97–100), A (93–96), A- (90–92), B+ (87–89), B (83–86), B- (80–82) ,
C+ (77–79), C (73–76), C- (70–72), D+ (67–69), D (65–66), D- (menos de 65)'''

calificacion_numero = float(input("Escribe tu calificacion: "))

if calificacion_numero >= 97 and calificacion_numero <=100:
    calificacion_letra = 'A+'

elif calificacion_numero >=93 and calificacion_numero <97:
    calificacion_letra = 'A'

elif calificacion_numero >=90 and calificacion_numero <93:
    calificacion_letra = 'A-'

elif calificacion_numero >=87 and calificacion_numero <90:
    calificacion_letra = 'B+'

elif calificacion_numero >=83 and calificacion_numero <87:
    calificacion_letra = 'B'

elif calificacion_numero >=80 and calificacion_numero <83:
    calificacion_letra = 'B-'

elif calificacion_numero >=77 and calificacion_numero <80:
    calificacion_letra = 'C+'

elif calificacion_numero >=73 and calificacion_numero <77:
    calificacion_letra = 'C'

elif calificacion_numero >=70 and calificacion_numero <73:
    calificacion_letra = 'C-'

elif calificacion_numero >=67 and calificacion_numero <70:
    calificacion_letra = 'D+'

elif calificacion_numero >=65 and calificacion_numero <67:
    calificacion_letra = 'D'

elif calificacion_numero >=0 and calificacion_numero <65:
    calificacion_letra = 'D-'

else: calificacion_letra = 'calificación no válida'


print("Tu calificación es:",calificacion_letra)
