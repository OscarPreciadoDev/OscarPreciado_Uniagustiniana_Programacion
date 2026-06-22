# Buscar el numero. Crea un bucle que pida numeros al usuario constantemente. Si el usuario ingresa un numero negativo, el programa debe decir error critico y cerrarse usando break. Si ingresa el numero 0 debe decir "numero nulo, saltando"... Usando continue


while True:
    num = int(input('>>> Ingrese un numero: '))
    
    if num > 0:
        print('>> Pass')
    elif num == 0:
        print(">> Numero nulo, saltando...")
        continue
    elif num < 0:
        print("!! Error Critico !!")
        break
