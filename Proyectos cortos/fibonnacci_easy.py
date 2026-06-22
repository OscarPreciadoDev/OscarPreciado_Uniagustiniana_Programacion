# Pedir un numero N y genera los primeros N terminos de la serie (0,1,1,2,3,5...)

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

# SECUENCIA DE FIBONACCI

limite = int(input('--> Ingrese el limite de la secuencia: '))

secuencia = []

for numero in range(0,2):
    secuencia.append(numero)

for numero in range(1,(limite-1)):
    nuevo_num = secuencia[-2] + secuencia[-1]
    secuencia.append(nuevo_num)

for numero in secuencia:
    print(numero,end=' ')