# Crear una lista de 10 celdas (0 o 1). En cada turno, una celda cambia a 1 si tiene un vecino vivo, o a 0 si está aislada.


import random

def new_lista(lista):
    nueva_list = []
    for posicion, casilla in enumerate(lista):
        if posicion == 0:
            derecho = lista[posicion+1]
            if derecho == 1:
                nueva_list.append(1)
            else:
                nueva_list.append(0)
        elif posicion in range(1,9):
            derecho = lista[posicion+1]
            izquierdo = lista[posicion-1]
            if (izquierdo==1 or derecho==1):
                nueva_list.append(1)
            else:
                nueva_list.append(0)
        else:
            izquierdo = lista[posicion-1]
            if izquierdo == 1:
                nueva_list.append(1)
            else:
                nueva_list.append(0)
    return nueva_list

def juego(lista_inicial,turnos):
    print('-'*50)
    lista_recorrido = lista_inicial
    for turno in range(turnos+1):
        print(f'Turno {turno} ==> {lista_recorrido}')
        lista_recorrido = new_lista(lista_recorrido)

def try_turnos():                                                                                  # Funcion que toma los turnos solicitados por el usuario
    try:                                                                                           # Intenta 
        entrada = int(input('==> '))                                                               # tomar una entrada y convertirlo en entero
        if entrada <= 1 or entrada >10 :                                                           # Si el numero ingresado no esta entre 2 y 10
            print(f'{'-'*50}--\n--> El rango de los turnos debe estar entre (2 - 10)\n--> Intente nuevamente') # Mensaje de error para el usuario
            return try_turnos()                                                                    # Devuelve la funcion desde el inicio
        else:                                                                                      # Si no (Se asume que la entrada esta en el rango) 
            return entrada                                                                         # Retorna la entrada
    except ValueError:                                                                             # Excepto cuando hay ValueError
        print(f'{'-'*50}--\n--> Valor invalido, intente nuevamente')                               # Imprime mensaje de error
        return try_turnos()                                                                        # Devuelve al inicio de la funcion

def try_list():                                                                                   # Funcion que crea una lista nueva
    lista = []                                                                                    # La lista empieza vacia
    for i in range(10):                                                                           # 10 veces
        element = random.randrange(0,2)                                                           # Crea un elemento al azar sea 1 o  0
        lista.append(element)                                                                     # Agrega este elemento a la lista
    return lista                                                                                  # Devuelve la lista nueva completada

def main():                                                                                       # Bloque de ejecucion principal del programa
    print(f'{'-'*50}--\n--> Ingrese el numero de turnos a jugar: ')                               # Indicacion para el usuario
    turnos = try_turnos()                                                                         # Toma un input de la funcion try_turnos y la guarda
    new_list = try_list()                                                                         # Crea una nueva lista aleatoria creada en la funcion try_list
    juego(new_list,turnos)                                                                        # Ejecuta el codigo de juego con los argmentos (lista,turnos)

def ejecucion() :                                                                                 # Funcion que define la ejecucion del programa principal
    print('-'*50,'\n--> Desea ingresar un nuevo Intento? \n--> 1 (SI)\n--> 2 (NO)')               # Instruccion para el usuario
    eleccion = input('==> ')                                                                      # Toma una entrada
    if eleccion == '1':                                                                           # Si la eleccion es igual a 1
        return True                                                                               # Retorna verdadero
    elif eleccion == '2':                                                                         # Si es la eleccion es igual a 2
        print('-'*50,'\n--> Fin del programa')                                                    # Mensaje de aviso fin del programa
        return False                                                                              # Devuelve falso
    else:                                                                                         # Si no es ninguna de las opciones
        print('-'*50,'\n--> Eleccion Invalida. Intente nuevamente')                               # Mensaje avisando el error al usuario
        return ejecucion()                                                                        # Retorna volviendo a ejecutar el programa

run = True                                                                                        # Variable que define el arranque del programa
print("--> PROPAGACION <--".center(50,"-"))                                                       # Mensaje de bienvenida
while run == True:                                                                                # Mientras que la variable de ejecucion sea verdadera
    main()                                                                                        # Ejecutar el bloque principal
    run = ejecucion() 