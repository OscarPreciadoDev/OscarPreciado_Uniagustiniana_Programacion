# Crear un ciclo while con un menú: 
# (1) Agregar, 
# (2) Ver lista, 
# (3) Salir. 
# Los datos deben persistir mientras el programa esté corriendo.

def try_opcion():                                                               # Funcion que toma una opcion del usuario
    print(f'{'-'*50}\n--> Eliga una de las siguientes opciones:\n--> (1) Agregar\n--> (2) Ver lista\n--> (3) Eliminar\n--> (4) Salir')
    try:                                                                        # Intenta
        opcion = int(input('==> ').strip())                                     # Tomar una entrada y convertirla en entero sin espacios
        if opcion not in range (1,5):                                           # Si la opcion no esta entre las opciones definidas [1,5]
            print(f'{'-'*50}\n--> Error de rango, Intente nuevamente')          # Imprime mensaje de error para el usuario
            return try_opcion()                                                 # Retorna a la funcion desde el inicio
        else:                                                                   # Si no (es decir que esta dentro del rango)
            return opcion                                                       # La funcion retorna la opcion elegida normalizada
    except ValueError:                                                          # Excepto cuando hay ValueError
        print(f'{'-'*50}\n--> Error de ingreso, intente nuevamente')            # Imprime mensaje de error para el usuario
        return try_opcion()                                                     # Devuelve a la funcion desde el inicio

def try_retiro(lista):                                                          # Funcion que define la opcion retiro
    rango = len(lista)                                                          # Crea un rango de opciones que es el tamaño de la lista 
    try:                                                                        # Intenta
        entrada = int(input('==> ').strip())                                    # Tomar un input, quitar espacios y convertilo a int
        if not entrada in range(1,rango+1):                                     # Si la entrada no esta en un rango de la lista(incluyendo el ultimo elemento)
            print(f'{'-'*50}\n--> Eleccion fuera de rango, intente nuevamente') # Mensaje indicando el error al usuario
            return try_retiro(lista)                                            # Devuelve al inicio de la funcion
        else:                                                                   # Si no (Confirmado que esta dentro de rango)
            return entrada                                                      # Retorna la entrada como respuesta de la funcion
    except ValueError:                                                          # Excepto cuando hay ValueError
        print(f'{'-'*50}\n--> Error de valor, intente nuevamente')              # Indica error al usuario
        return try_retiro(lista)                                                # Retorna la funcion desde el inicio

def try_ejecucion(opcion):                                                      # Funcion que decide si el programa termina o continua
    if opcion == 4:                                                             # Si la opcion elegida es la 4
        print(f'{'-'*50}\n--> Fin del programa\n{'-'*50}')                      # Mensaje indicando el fin del programa
        return False                                                            # Devuelve valor de falso (Termina el programa)
    else:                                                                       # Sino (se asume que tomo otra opcion)
        return True                                                             # Devuelve verdadero (Sigue corriendo el programa)
    
def try_tarea(opcion,lista):                                                    # Funcion que toma una opcion y la ejecuta teniendo en cuenta la lista
    if opcion == 1:                                                             # Si la opcion elegida fue 1 (Ingresar elemento)
        print(f'{'-'*50}\n--> Ingrese el nuevo elemento: ')                     # Mensaje indicando siguiente paso al usuario
        nuevo = input('==> ')                                                   # Toma un nuevo elemento
        lista.append(nuevo)                                                     # Agrega el nuevo elemento a la lista
        print(f'{'-'*50}\n--> Nuevo elemento agregado con exito!')              # Mensaje de verificacion
    if opcion == 2:                                                             # Si la opcion elegida fue 2 (Visualizar)
        print('-'*50)                                                           #--------------------
        if len(lista) == 0:                                                     # Si la lista no tiene elementos
            print(f'{'-'*50}\n--> La lista esta vacia actualmente')             # Mensaje inidicando que la lista esta vacia
        else:                                                                   # Sino (Se asume que hay elementos en la lista)
            for elemento in lista:                                              # por cada elemento de la lista
                print(f'* {elemento}')                                          # Imprimirlo
    if opcion == 3:                                                             # Si la opcion elegida fue 3 (eliminar)
        if len(lista) == 0:                                                     # Si la lista no tiene elementos
            print(f'{'-'*50}\n--> La lista esta vacia actualmente\n--> No hay elementos para retirar')  # Mensaje indicando al usuario que no hay nada para eliminar
        else:                                                                   # Sino (Se asume que la lista tiene algun elemento)
            print(f'{'-'*50}\n--> Ingrese la posicion del elemento que desea retirar') # Se indica la siguiente accion al usuario
            retiro = try_retiro(lista)                                          # Se toma un numero de index usando la funcion try_retiro=
            print(f'{'-'*50}\n--> El elemento "{lista[retiro-1]}" fue retirado con exito!!')   # Se confirma el retiro del elemento
            lista.pop(retiro-1)                                                 # Se elimina el elemento con el index indicado (Se quita 1 porque los index empiezan en 0)

run = True                                                                      # Variable que determina la ejecucion del programa
lista = []                                                                      # La lista de elementos inicialmente se declara vacia

while run == True:                                                              # Mientras que la variable de ejecucion sea verdadera
    print("--> MENU DE INVENTARIO <--".center(50,"-"))                          # Imprime mensaje principal
    opcion = try_opcion()                                                       # Toma una opcion usando la funcion opcion (detalles mencionados en la funcion)
    run = try_ejecucion(opcion)                                                 # Toma un valor para seguir/parar el programa
    tarea =  try_tarea(opcion,lista)                                            # (True) Realizar una tarea / (False) Fin del programa

