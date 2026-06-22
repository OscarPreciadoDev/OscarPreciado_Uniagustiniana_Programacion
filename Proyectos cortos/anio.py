# Solicita un año y determina si es bisiesto 
# divisible por 4, pero no por 100, 
# a menos que sea divisible por 400

def try_anio():                                                                     # Funcion que toma un anio de entrada
    print(f'{'-'*50}\n--> Ingrese un anio para verificar: ')                        # Mensaje de indicacion para el usuario
    try:                                                                            # Intenta
        entrada = int(input('==> '))                                                # Toma una entrada del usuario y la convierte en entero
        if (0 < len(str(entrada))) and entrada > 0:                                 # Si el anio tiene almenos un digito y es positivo
            return entrada                                                          # Devuelve la entrada (pasa la verificacion)
        else:                                                                       # Si no (es decir que no )
            print(f'{'-'*50}\n--> Ingrese un anio valido')                          # Mensaje indicando el error al usuario
            return try_anio()                                                       # Devuelve al inicio de la funcion
    except ValueError:                                                              # Excepto (Ingreso algo que no es numero)
        print(f'{'-'*50}\n--> Ingrese un valor valido')                             # Muestra el error al usuario
        return try_anio()                                                           # Devuelve al inicio de la funcion

def ver_anio(anio):                                                                 # Funcion para verificar el anio ingresado
    bisciestio = False                                                              # Inicialmente se declara como no bisciesto
    if anio % 4 == 0:                                                               # Si el anio es divisible 
        bisciestio = True                                                           # Es bisciesto
        if anio % 100 == 0:                                                         # Si el anio tambien es divisible entre 100
            bisciestio = False                                                      # No es bisciesto
            if anio % 400 == 0:                                                     # Pero si el anio es divisible entre 400 
                bisciestio = True                                                   # Si es bisciesto
            else:                                                                   # Si no es divisible entre 400 
                bisciestio = False                                                  # No es bisciesto
        else:                                                                       # Si no es divisible entre 100
            bisciestio = True                                                       # Es bisciesto
    else:                                                                           # Si no es divisible entre 4
        bisciestio = False                                                          # No es bisciesto
    if bisciestio == True:                                                          # Si bisciesto es igual a verdadero
        return (' es bisciesto')                                                    # Devolver mensaje para verdadero
    else:                                                                           # Si no (no es bisciesto)
        return (' no es bisciesto ')                                                # Devolver mensaje para no bisciesto

def ejecucion():                                                                    # Funcion que define la ejecucion del programa
    print(f'{'-'*50}\n--> Desea ingresar un nuevo anio?\n--> (1) SI\n--> (2) NO')   # Mensaje inidicando las opciones al usuario
    entrada = input('==> ').strip()                                                 # Toma una entrada y elimina los espacios
    if entrada == '1':                                                              # Si la entrada es igual a '1'
        return True                                                                 # Devuelve verdaderio (sigue ejecutando el programa)
    elif entrada == '2':                                                            # Si no si la entrada es igual a '2'
        print(f'{'-'*50}\n--> Fin del programa\n{'-'*50}')                          # Mensaje indicando el fin del programa
        return False                                                                # Devuelve falso (fin del while)
    else:                                                                           # Sino (se asume entrada incorrecta)
        print(f'{'-'*50}\n--> Ingrese una opcion valida')                           # Mensaje inidicando el error al usuario
        return ejecucion()                                                          # Devuelve al inicio de la funcion

run = True                                                                          # Variable que define la ejecucion del codigo

print('> VALIDADOR DE ANIO BISIESTO <'.center(50,'-'))                              # Mensaje de bienvenida
while run == True:                                                                  # Mientras que la variable de ejecucion sea verdadera
    anio = try_anio()                                                               # Solicitar un anio
    print(f'{'-'*50}\n--> El anio {anio}{ver_anio(anio)}')                          # Imprimir mensaje de verificacion usando la funcion 
    run = ejecucion()                                   