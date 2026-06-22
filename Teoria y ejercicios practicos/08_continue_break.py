# Break y continue

# Break para detener y salir
# Continue es para detener y continuar

numeros = [3,5,7,8,9,12]

buscar = 7

for numero in numeros:
    if numero == buscar:
        print(f">>> Encontrado el {numero} detengo la busqueda")
        break
    print(f">>> Encontrado {numero} ")

# Continue no detiene el codgio, se lo salta, hasta cuando haya una interaccion siguiente 


# Cree un programa que imprima los numeros impare y se salte los impares


numeros = [3,5,7,8,9,12]

for numero in range(1,21):
    if numero % 2 != 0 :
        continue    
    print(f">>> Encontrado el {numero}")