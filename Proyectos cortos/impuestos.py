# Calcula el impuesto: los primeros $10.000 son excentos, de $10.000 a #20.000 pagan 10%, y el escedente de $20.000 paga 20%


sep = f'{'-'*50}\n'

numero = 30000

def cal_impuesto(num):                                                           # Funcion que calcula el impuesto
    if num < 10000:                                                              # Si el ingreso es menor a 10.000 es excento
        return 0                                                                 # Se devuelve 0
    elif 10000 < num < 20000:                                                    # Si el ingreso esta entre 10K y 20K
        cant = num - 10000                                                       # Se calcula el dinero en el rango (quitando 10K excentos)
        imp = cant*0.1                                                           # Calcula el 10% del impuesto del dinero que aplica
        return imp                                                               # Devuelve ese impuesto
    else:                                                                        # Si no (se asume un ingreso mayor a 20K)
        imp = 1000                                                               # El impuesto ya tendra 1K del impuesto del 10% de los primeros 20K
        add = num - 20000                                                        # Se calcula el restante de dinero quitando los 20K ya calculados 
        imp += add*0.2                                                           # Se calcula el 20% de ese restante y se suma al impuesto
        return imp                                                               # Devuelve el impuesto

def try_ingreso():                                                               # Funcion para tomar una entrada
    print(f'{sep}--> Ingrese un monto para calcular su impuesto ')               # Instruccion para el usuario 
    try:                                                                         # Intenta
        entrada = int(input('==> $'))                                            # Tomar una entrada y convertirla en entero
        if entrada > 0:                                                          # Si la entrada es positiva
            return entrada                                                       # Devuelve la entrada
        else:                                                                    # Si no
            print(f'{sep}--> Ingrese un ingreso valido!!')                       # Mensaje indicando el error al usuario
            return try_ingreso()                                                 # Devuelve al inicio de la funcion
    except ValueError:                                                           # Excepto cuando hay value error
        print('--> Error, Ingrese un numero ')                                   # Muestra el error al usuario
        return try_ingreso()                                                     # Devuelve al inicio de la funcion

def ejecucion():                                                                 # Funcion que define la ejecucion del programa
    print(f'{sep}--> Desea ingresar un nuevo ingreso? \n--> (1) SI\n--> (2) NO') # Mensaje de instruccion para el usuario
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
    

run = True                                                                       # Variable que define la ejecucion del programa
print('> CALCULADORA DE IMPUESTOS <'.center(50,'-'))                             # Mensaje de bienvenida para el usuario
while run == True:                                                               # Mientras que la variable de ejecucion sea verdadero
    ingreso = try_ingreso()                                                      # Toma una entrada
    impuesto = cal_impuesto(ingreso)                                             # Calcula el impuesto de la entrada
    print(f'{sep}--> El impuesto de ${ingreso} es de ${impuesto} ')              # Imprime un mensaje indicando el resultado
    run = ejecucion()                                                            # Reasigna la variable de ejecucion