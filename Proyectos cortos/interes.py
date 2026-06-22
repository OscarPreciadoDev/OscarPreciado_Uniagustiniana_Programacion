# Pedir un monto de capital, tasa y anios mostrar el saldo acumulado anio tras anio en una tabla

# nuevo saldo anual se calcula de la siguiente manera
# Formula del calculo del rendimiento anual:
        # nuevo saldo = saldo anterior * (1 + tasa)

def tabla(capital,tasa_a,anios):                                                         # Funcion que crea la tabla con los datos
    saldo = capital                                                                      # El capital de guardara en la variable saldo
    print('='*50)                                                                        # =========
    for anio in range(1,anios+1):                                                        # Por cada anio en el rango de anios indicado (desde el 1 hasta el anio final)
        saldo *=  (1 + tasa_a)                                                           # El saldo se actualiza multiplicandolo por la formula de calculo del rendimiento anual
        print(f'|| Año : {anio}',end="")                                                 # Se imprime el anio de la iteracion y se termina sin salto de linea
        print(f'|| Capital : {saldo:.2f}  '.rjust(38),end="||\n")                        # Se imprime el valor del saldo de la iteracion formateado y completando el lado derecho de la tabla
    print('='*50)                                                                        # =================

def try_inputs():                                                                        # Funcion que toma los inputs necesarios
    print(f'{sep}--> Ingrese los siguientes datos solicitado a continuacion: ')          # Instrucciones para el usuario
    print(f'{sep}--> Ingrese el capital inicial:')                                       # Primera instruccion de entrada
    try:                                                                                 # Intenta
        saldo = float(input("==> $ "))                                                   # Tomar una entrada y convertirla a float
        if saldo > 0:                                                                    # Si esta es mayor a 0 (positiva)
            pass                                                                         # Ok
        else:                                                                            # Sino (negativa)
            print(f'{sep}--> Ingrese un monto valido! ')                                 # Indica el error al usuario
            return try_inputs()                                                          # Devuelve al inicio de la funcion
    except ValueError:                                                                   # Excepto con value error (entrada str o otros)
        print(f'{sep}--> Ingrese una entrada valida')                                    # Indica el error al usuario
        return try_inputs()                                                              # Devuelve al inicio de la funcion
    print(f'{sep}--> Ingrese la tasa de rendimiento anual: ')                            # Segunda instruccion de entrada
    try:                                                                                 # Intenta
        try_tasa = int(input("==> % "))                                                  # Tomar una entrada y convertirla a entero
        if 0 <= try_tasa <= 1000:                                                        # Si la entrada esta en el rango
            tasa = try_tasa/100                                                          # La convierte en porcentaje
        else:                                                                            # Sino (fuera de rango)
            print(f'{sep}--> Ingrese un numero valido! ')                                # Mensaje de error para el usuario
            return try_inputs()                                                          # Retorna al inicio de la funcion
    except ValueError:                                                                   # Excepto con value error (entrada str o otros)
        print(f'{sep}--> Ingrese una entrada valida')                                    # Indica el error al usuario
        return try_inputs()                                                              # Devuelve al inicio de la funcion
    print(f'{sep}--> Ingrese los años de rendimiento a calcular: ')                      # Tercera instruccion de entrada
    try:                                                                                 # Intenta
        anios = int(input("==> "))                                                       # Tomar una entrada y convertirla en entero
        if anios > 0:                                                                    # Si el anio entrado es positivo
            pass                                                                         # OK
        else:                                                                            # Sino (se asume anio negativos)
            print(f'{sep}--> Ingrese un numero valido! ')                                # Mensaje indicando el error al usuario
            return try_inputs()                                                          # Devuelve al inicio de la funcion
    except ValueError:                                                                   # Excepto con value error (entrada str o otros)
        print(f'{sep}--> Ingrese una entrada valida')                                    # Mensaje indicando el error al usuario
        return try_inputs()                                                              # Devuelve al inicio de la funcion
    return saldo, tasa, anios                                                            # Al final si todo esta en orden devuelve los 3 datos ingresados


def ejecucion():                                                                         # Funcion que determina la ejecucion del codigo
    print(f'{sep}--> Desea ingresar una nueva tabla?\n--> (1) SI\n--> (2) NO')           # Indicaciones para el usuario
    try:                                                                                 # Intenta
        entrada = input('==> ').strip()                                                  # Toma una entrada y quita los espacios
        if entrada == '1':                                                               # Si la entrada es igual a '1'
            return True                                                                  # Devuelve verdadero (se sigue ejecutando el programa)
        elif entrada == '2':                                                             # Si no si la entrada es igual a '2'
            print(f'{sep}--> Fin del programa\n{sep}')                                   # Mensaje indicando el final del programa
            return False                                                                 # Devuelve falso (se termina el bucle de ejecucion)
        else:                                                                            # Sino (se asume entrada incorrecta)
            print(f'{sep}--> Ingrese una entrada valida')                                # Indica el error al usuario
            return ejecucion()                                                           # Llama al inicio de la funcion
    except ValueError:                                                                   # Excepto con valueError (error de entrada)
        print(f'{sep}--> Ingrese una entrada valida')                                    # Indica el error al usuario
        return ejecucion()                                                               # Retorna al inicio de la funcion


sep = f'{'-'*50}\n'                                                                      # ---------
run = True                                                                               # Variable de ejecucion
print('> INTERES COMPUESTO <'.center(50,'-'))                                            # Mensaje de bienvenida
while run == True:                                                                       # Mientras que la variable de ejecucion sea verdadera
    capital,tasa,anios = try_inputs()                                                    # Asigna estos 3 datos usando la funcion de inputs
    tabla(capital,tasa,anios)                                                            # Crea una tabla usando los 3 datos recolectados usando la funcion tabla()
    run = ejecucion()                                                                    # Reasigna la variable de ejecucion