# Matriz identidad
# Solicita un numero N y genera una matriz identidad de N/tiempo N usando bucles anidados

def try_tamanio():                                                                       # Funcion que toma una entrada para tamanio de la matriz
    print('--> Ingrese el tamanio de filas-columnas de la matriz identidad:')            # Instrucciones para el usuario
    try:                                                                                 # Intenta
        entrada = int(input('==> '))                                                     # Toma una entrada y convierte en entero
        if entrada > 0:                                                                  # Si la entrada es mayor a 0 (positiva)
            return entrada                                                               # La retorna como respuesta de la funcion
        else:                                                                            # Sino (se asume numero negativo, invalido)
            print('--> Ingrese un numero positivo')                                      # Indica el error al usuario
            return try_tamanio()                                                         # Devuelve al inicio de la funcion
    except  ValueError:                                                                  # Excepto con valueError (entrada incorrecta)
        print('--> Ingrese un valor valido.')                                            # Indica el error al usuario
        return try_tamanio()                                                             # Devuelve al inicio de la funcion

def crear_matriz(tamanio):                                                               # Funcion que crea la matriz en funcion del tamanio
    matriz = []                                                                          # Variable donde se guardaran las listas de filas de la matriz
    for fila in range(tamanio):                                                          # Por cada fila en el tamanio definido
        new_fila = []                                                                    # Se crea una fila vacia                              
        for columna in range(tamanio):                                                   # Por cada columna (elemento) en el rango
            if fila == columna:                                                          # Si el elemento esta en la misma posicion de fila y columna
                new_fila.append(1)                                                       # Agrega un 1 a la fila
            else:                                                                        # Si no (se asume que esta en otra posicion)
                new_fila.append(0)                                                       # Agrega un 0
        matriz.append(new_fila)                                                          # Finalmente se agrega esa fila a la matriz
    return matriz                                                                        # Devuelve la matriz como resultado de la funcion

def print_matriz(matriz):                                                                # Funcion que imprime la matriz
    print('\n')                                                                          # "     "
    for fila in matriz:                                                                  # Por cada fila de la matriz
        string = " ".join(map(str,fila))                                                 # Crea un string donde ingresara los elementos de la fila convertidos en str uno por uno (map)
        print(f"({string})".center(50))                                                  # Imprime ese string formateado con "( )" y centrado
    print('\n')                                                                          # "     "

def ejecucion():                                                                         # Funcion que determina la ejecucion del codigo
    print('--> Desea ingresar una nueva matriz?\n--> (1) SI\n--> (2) NO')                # Indicaciones para el usuario
    try:                                                                                 # Intenta
        entrada = input('==> ').strip()                                                  # Toma una entrada y quita los espacios
        if entrada == '1':                                                               # Si la entrada es igual a '1'
            return True                                                                  # Devuelve verdadero (se sigue ejecutando el programa)
        elif entrada == '2':                                                             # Si no si la entrada es igual a '2'
            print('--> Fin del programa')                                                # Mensaje indicando el final del programa
            return False                                                                 # Devuelve falso (se termina el bucle de ejecucion)
        else:                                                                            # Sino (se asume entrada incorrecta)
            print('--> Ingrese una entrada valida')                                      # Indica el error al usuario
            return ejecucion()                                                           # Llama al inicio de la funcion
    except ValueError:                                                                   # Excepto con valueError (error de entrada)
        print('--> Ingrese una entrada valida')                                          # Indica el error al usuario
        return ejecucion()                                                               # Retorna al inicio de la funcion

run = True                                                                               # Variable que determina la ejecucion del programa
print('> GENERADOR DE MATRIZ IDENTIDAD <'.center(50,'-'))                                # Mensaje de bienvenida
while run == True:                                                                       # Mientas que la variable de ejecucion sea verdadera
    tamanio =  try_tamanio()                                                             # Toma un tamanio con la funcion que toma un input y lo verifica
    matriz = crear_matriz(tamanio)                                                       # Crea una matriz identidad usando el tamanio ingresado
    print(f'--> La matriz identidad con ({tamanio}) filas y columnas es la siguiente: ') # Mensaje para el usuario 
    print_matriz(matriz)                                                                 # Se imprime la matriz formateada
    run = ejecucion()                                                                    # Se reasigna la variable de ejecucion del codigo