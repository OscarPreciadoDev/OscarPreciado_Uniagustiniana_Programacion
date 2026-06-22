# Cajero Automático Eficiente:
# Pide un monto a retirar y calcula cuántos billetes de 
# 50000 
# 20000  
# 10000 
# debe entregar, minimizando la cantidad total de billetes.

def mejor_caso(ret, bill):                                                        # Funcion que crea la combinacion de billetes
    resultado = {}                                                                # Diccionario que guardara pares {billete:cantidad}
    for billete in bill:                                                          # Recorre la lista de billetes
        cantidad = ret // billete                                                 # Calcula la cantidad de ese billete al dividir la transaccion entre el billete y tomando su parte entera
        if cantidad > 0:                                                          # Si la cantidad es mayor a 0 (es decir que almenos un billete se puede usar)
            resultado[billete] = cantidad                                         # Agrega al diccionario el par {billete:cantidad}
            ret -= cantidad * billete                                             # Actualiza el retiro quitando el dinero ya calculado

        if ret == 0:                                                              # Si el retiro ya esta limpio (es decir ya se obtuvo la combinacion exacta)
            return resultado                                                      # Devuelve el diccionario de combinacion de billetes
    if ret != 0:                                                                  # Si aun queda dinero en el retiro (se asume que no es exacto el monto)
        print(f'{'-'*70}\n--> Monto Erroneo!!\n--> Fin de la transaccion')        # Mensaje indicando el error al usuario
        return None                                                               # No devuelve nada y sigue el programa (siguiente paso preguntar nueva transaccion)

def try_retiro():                                                                 # Funcion que toma una entrada 
    try:                                                                          # Intenta
        entrada = int(input('==> $ '))                                            # Tomar un input y convertilo en entero
        if entrada > 0 and entrada//10000 != 0:                                   # Si el numero ingresado es positivo y multiplo de 10.000
            return entrada                                                        # Lo devuelve
        else:                                                                     # Si no (Se asume que el numero no paso el primer filtro)
            print(f'{'-'*70}\n--> Ingrese un numero valido')                      # Mensaje de error para el usuario
            return try_retiro()                                                   # Devuelve al inicio de la funcion
    except ValueError:                                                            # Excepto cuando hay value error
        print(f'{'-'*70}\n--> El valor ingresado debe ser un numero entero !!!')  # Indica el error al usuario
        return try_retiro()                                                       # Devuelve al inicio de la funcion

def print_combinacion(combinacion):                                               # Funcion que muestra en consola el resultado de la combinacion de billetes
    print('-'*70)                                                                 #-----------
    for billete, cantidad in combinacion.items():                                 # Por cada par en los items del diccionario
        print(f'--> ${billete} : Cantidad {cantidad}')                            # Imprime formateado los billetes y las cantidades 

def ejecucion():                                                                  # Funcion que decide la continuacion del programa
    print(f'{'-'*70}\n--> Desea ingresar un nuevo monto?\n (1) SI\n (2) NO')      # Instrucciones para el usuario
    eleccion = input('==> ').strip()                                              # Toma un input y quita los espacios no deseados
    if eleccion == '1':                                                           # Si la opcion es 1
        return True                                                               # Devuelve verdadero
    elif eleccion == '2':                                                         # Si la opcion es 2
        print(f'{'-'*70}\n--> Fin de la transaccion\n{'-'*70}')                   # Mensaje indicando el fin del programa
        return False                                                              # Devuelve Falso (Se actualiza run a false y termina el programa)
    else:                                                                         # Si no (Se asume otra entrada que no es alguna de las opciones)
        print(f'{'-'*70}\n--> Ingrese una opcion valida !!')                      # Mensaje indicando el error al usuario
        return ejecucion()                                                        # Devuelve al inicio de la funcion

def main():                                                                       # Funcion que ejecuta el bloque principal del programa
    print(f'{'> CAJERO AUTOMATICO <'.center(70,'-')}\n Este cajero dispone unicamente de billetes de $50000, $20000 y $10000\n{'-'*70}\n Ingrese el monto que desea retirar: ')
    retiro = try_retiro()                                                         # Toma un input de la funcion y lo almacena como el monto a retirar
    combinacion = mejor_caso(retiro,billetes)                                     # Pasa el monto y los billetes por la funcion que calcula el mejor caso
    if combinacion:                                                               #  SI EXISTE UNA COMBINACION IMPRIMELA // Sino (se asume que el monto no es exacto, pasa a preguntar si cierra el programa o sigue)
        print_combinacion(combinacion)                                            # Llama a una funcion que imprime la combinacion formateada

billetes = [50000,20000,10000]                                                    # Billetes que se pueden retirar                                                  
run = True                                                                        # Variable que define la ejecucion de programa
while run == True:                                                                # Mientras que la variable de ejecucion sea verdadera
    main()                                                                        # Ejecuta el bloque principal
    run = ejecucion()                                                             # Actualiza la variable de ejecucion tomando un input de la funcion 