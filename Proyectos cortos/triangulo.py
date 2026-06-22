# VALIDADOR DE TRIANGULO

# TOMAR LOS DATOS Y CONVERTIRLOS EN NUMEROS ENTEROS

lad1 = int(input('--> Ingrese un lado'))
lad2 = int(input('--> Ingrese un lado'))
lad3 = int(input('--> Ingrese un lado'))
ang1 = int(input('--> Ingrese un angulo'))
ang2 = int(input('--> Ingrese un angulo')) 
ang3 = int(input('--> Ingrese un angulo'))

# VERIFICA LOS ANGULOS

if ang1 + ang2 + ang3 == 180:
    print ('Triangulo valido')

# Funcion para verificar lados
def clasificacion_l(lad1,lad2,lad3,ang1,ang2,ang3):
    if lad1 == lad2 == lad3:
        print('Triangulo Equilatero')
    elif (lad1== lad2) or (lad1==lad3) or(lad2==lad3):
        print('Triangulo isoceles')
    else:
        print('Triangulo escaleno')

# Ejecutar la funcion         

clasificacion_l(lad1,lad2,lad3,ang1,ang2,ang3)