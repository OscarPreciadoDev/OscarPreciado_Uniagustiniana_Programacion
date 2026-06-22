# Pedir un numero N y genera los primeros N terminos de la serie (0,1,1,2,3,5...)



def rango():
    print('-'*65)                                                                                 # Funcion que toma el rango
    print('--> Ingrese la cantidad de numeros (ENTERO) que desea ver de la serie: ')                       # Instrucciones para el usuario
    try:                                                                                          # Intenta
        try_rango = int(input("--> "))                                                                  # Guardar en una variable un input convertido a entero que es el rango "N"
    except ValueError:                                                                            # Excepto cuando hay ValueError
        print('--> Valor Invalido!! Ingrese un numero valido')                                    # Mensaje de error al usuario
        return rango()                                                                            # Devuelve la funcion desde el inicio
    if try_rango<= 0:                                                                             # Si el numero dado es 0 o es negativo
        print('--> Rango Invalido, el numero tiene que ser positivo')                             # Mensaje de error al usuario
        return rango()                                                                            # Devuelve la funcion desde el inicio
    return try_rango                                                                              # Si todo esta bien devuelve el numero de rango "N"

lista = []                                                                                        # Define la lista de numeros inicialmente vacia
for i in range(0,2):                                                                              # Toma los numeros [0,1]
    lista.append(i)                                                                               # Los agrega a la lista

def main():                                                                                       # Funcion de bloque prinicipal
    limite =  rango()                                                                             # Almacena el rango en una variable
    for i in range(1,limite-1):                                                                   # Por cada paso en un rango entre [1 y un numero antes del limite]
        nuevo_num = lista[-2] + lista[-1]                                                         # Crea un nuevo numero sumando los 2 ultimos de la lista    
        lista.append(nuevo_num)                                                                   # Adjunta este nuevo numero al final de la lista
    print('-'*65)                                                                                 # Separador visual
    for i in lista:                                                                               # Para cada elemento de la lista
        print(i)                                                                                  # Imprimir el elemento

def ejecucion() :                                                                                 # Funcion que define la ejecucion del programa principal
    print('-'*75,'\n--> Desea ingresar una nueva serie? \n--> 1 (SI)\n--> 2 (NO)')                # Instruccion para el usuario
    eleccion = input('--> ')                                                                      # Toma una entrada
    if eleccion == '1':                                                                           # Si la eleccion es igual a 1
        return True                                                                               # Retorna verdadero
    elif eleccion == '2':                                                                         # Si es la eleccion es igual a 2
        print('-'*75,'\n--> Fin del programa')                                                    # Mensaje de aviso fin del programa
        return False                                                                              # Devuelve falso
    else:                                                                                         # Si no es ninguna de las opciones
        print('-'*75,'\n--> Eleccion Invalida. Intente nuevamente')                               # Mensaje avisando el error al usuario
        return ejecucion()                                                                        # Retorna volviendo a ejecutar el programa

run = True                                                                                        # Variable que define el arranque del programa
print("\n\n","--> SECUENCIA DE FIBONACCI <--".center(63,"-"))                                     # Mensaje de bienvenida
while run == True:                                                                                # Mientras que la variable de ejecucion sea verdadera
    main()                                                                                        # Ejecutar el bloque principal
    run = ejecucion()                                                                             # Actualiza la variable de arranque