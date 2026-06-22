# Dibujo de diamante
# Pide un numero impar e imprime un diamante de asteriscos (*) perfectamente centrado

sep = f'{'-'*50}\n'                                                              # Separador visual

def try_filas():                                                                 # Funcion que toma la mitad del diamante
    print(f'{sep}--> Ingrese un numero impar (mitad del diamante)')              # Instruccion para el usuario
    try:                                                                         # Intenta
        entrada = int(input('==> '))                                             # Tomar una entrada y convertirlo en entero
        if entrada%2==1 and entrada>0:                                           # Si la entrada es impar y positiva
            return entrada                                                       # Devuelve la entrada
        else:                                                                    # Sino
            print(f'{sep}--> Ingrese un numero valido')                          # Mensaje de error para el usuario
            return try_filas()                                                   # Devuelve al inicio de la funcion
    except ValueError:                                                           # Excepto cuando hay value error
        print(f'{sep}--> Ingrese un valor valido')                               # Mensaje indicando el error al usuario
        return try_filas()                                                       # Devuelve al inicio de la funcion

def try_ancho(filas):                                                            # Funcion que calcula el ancho del diamante
    c = '*'                                                                      # Caracter de relleno
    ancho = len(c*(filas*2+1))                                                   # calcula el ancho de la fila de impresion mas ancha (la que da de la ultima fila de la mitad)
    return ancho                                                                 # Devuelve ese ancho


def print_diamante(filas,ancho):                                                 # Funcion que imprime el diamante
    c = '*'                                                                      # Caracter de relleno
    for i in range(filas):                                                       # Por cada iteracion en la cantidad de filas (primera mitad)
        print(f'{c*(i*2+1)}'.center(ancho))                                      # Imprime cada repeticion calculandola como el doble de caracteres mas 1 centrado segun el ancho
    for i in range(filas-2,-1,-1):                                               # Por cada iteracion en la cantidad de filas - 1 (segunda mitad) con paso negativo
        print(f'{c*(i*2+1)}'.center(ancho))                                      # Imprime cada repeticion calculadola como el doble de caracteres mas 1 centrado segun el ancho

def ejecucion():                                                                 # Funcion que define la opcion de run
    print(f'{sep}--> Desea ingresar un nuevo diamante?\n--> (1) SI\n--> (2) NO') # Mensaje de instruccion para le usuario
    try:                                                                         # Intenta
        eleccion = input('==> ').strip()                                         # Toma una entrada y quita los espacios
        if eleccion == '1':                                                      # Si la entrada es igual a 1
            return True                                                          # Devuelve verdadero (El programa se sigue ejecutando)
        elif eleccion == '2':                                                    # Si la entrada es igual a 2
            print(f'{sep}--> Fin del programa\n{sep}')                           # Mensaje indicando el fin del programa
            return False                                                         # Devuelve falso  (fin del programa)
        else:                                                                    # Sino ( se asume una entrada incorrecta )                   
            print(f'{sep}--> Eleccion Invalida. Intente nuevamente')             # Imprime mensaje de eleccion invalida
            return ejecucion()                                                   # Devuelve al inicio de la funcion 
    except ValueError:                                                           # Excepto cuando hay value error
        print(f'{sep}--> Ingrese una entrada valida')                            # Mensaje inidicando el error al usuario
        return ejecucion()                                                       # Devuelve al inicio de la funcion

run = True                                                                       # Variable que define la ejecucion del codigo
print('> DIBUJO DE DIAMANTE <'.center(50,'-'))                                   # Mensaje de bienvenida
while run == True:                                                               # Mientras que la variable de ejecucion sea verdadera
    filas = try_filas()                                                          # Toma una entrada de filas
    ancho = try_ancho(filas)                                                     # Calcula el ancho sobre las filas ingresadas
    print_diamante(filas,ancho)                                                  # Imprime el diamante usando la funcion
    run = ejecucion()                                                            # Reasigna la variable de ejecucion