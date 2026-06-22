# Pedir un numero N y genera las primeras N filas de este triangulo matematico

def ejecucion() :                                                                                 # Funcion que define la ejecucion del programa principal
    print('-'*50,'\n--> Desea ingresar un nuevo triangulo? \n--> 1 (SI)\n--> 2 (NO)')             # Instruccion para el usuario
    eleccion = input('==> ')                                                                      # Toma una entrada
    if eleccion == '1':                                                                           # Si la eleccion es igual a 1
        print('-'*50)                                                                             # Separador visual
        return True                                                                               # Retorna verdadero
    elif eleccion == '2':                                                                         # Si es la eleccion es igual a 2
        print('-'*50,'\n--> Fin del programa')                                                    # Mensaje de aviso fin del programa
        return False                                                                              # Devuelve falso
    else:                                                                                         # Si no es ninguna de las opciones
        print('-'*50,'\n--> Eleccion Invalida. Intente nuevamente')                               # Mensaje avisando el error al usuario
        return ejecucion()                                                                        # Retorna volviendo a ejecutar el programa

def try_filas():                                                                                  # Funcion que toma el numero de filas del usuario
    try:                                                                                          # Intenta 
        filas = int(input('==> ').strip())                                                        # Tomar un input, quitarle espacios y convertilo en int, almacenarlo en una variable
        print('-'*50)                                                                             # Separador visual
    except ValueError:                                                                            # Excepto cuando hay value error
        print('--> Valor Incorrecto. Intente nuevamente')                                         # Mensaje de error al usuario
        return try_filas()                                                                        # Vuelve a llamar a la funcion
    return filas                                                                                  # Si todo esta en orden devuelve la entrada normalizada como int 

def crear_triangulo(filas):                                                                       # Funcion que crea el triangulo tomando como argumento las filas deseadas
    triangulo_final = []                                                                          # Variable donde se almacenaran las filas del triangulo en listas anidadas

    for fila in range(filas):                                                                     # para cada fila en un rango de las filas deseadas
        nueva_fila = [1]                                                                          # La fila siempre empezara con un 1
        if fila > 0:                                                                              # Si la fila NO es la primera (un rango empieza en 0, asi que la primera iteracion es 0)
            fila_anterior = triangulo_final[fila-1]                                               # Tomaremos la fila anterior como la de un indice menos

            for sumas in  range(len(fila_anterior)-1):                                            # Para cada suma en un rango del tamaño de la fila anterior menos 1
                nuevo_num = fila_anterior[sumas] + fila_anterior[sumas+1]     
                # Se crea un nuevo numero, de tomar los 2 numeros de cada iteracion posible 
                # recorriendo la fila anterior
                nueva_fila.append(nuevo_num)                                                      # Se agrega a la fila de la iteracion este nuevo numero
            nueva_fila.append(1)                                                                  # Se agrega al final de la fila el numero 1
        triangulo_final.append(nueva_fila)                                                        # Se agrega al triangulo la nueva fila
    return triangulo_final                                                                        # Se devuelve el triangulo con sus filas anidadas como respuesta

def crear_filas(triangulo):                                                                       # Funcion que convierte las filas en texto para imprimir posteriormente
    filas_print = [' '.join(map(str,fila)) for fila in triangulo]                                 # Nueva lista donde se almacenan las filas transformadas una por una en cadenas de texto
    # Map = convierte en str cada fila
    # ' '.join Ingresa formatea el texto en cada linea haciendo espacio entre caracteres
    # [1, 3, 3, 1, ] --->>> '1 3 3 1'
    return filas_print                                                                            # Devuelve la lista con las filas normalizadas

def main():                                                                                       # Funcion que ejecuta el codigo principal
    print('--> Ingrese el numero de filas que desea visualizar: ')                                # Instruccion para el usuario
    filas = try_filas()                                                                           # Almacena las filas deseadas en una variable
    triangulo = crear_triangulo(filas)                                                            # Almacena el triangulo usando como argumento las filas deseadas
    filas_print = crear_filas(triangulo)                                                          # Almacena las filas del triangulo listas para imprimir
    ancho = len(filas_print[-1])                                                                  # Toma el ancho de la ultima fila del triangulo
    for fila in filas_print:                                                                      # Imprime cada fila lista para imprimir
        print(fila.center(ancho))                                                                 # La centra sobre el ancho tomado

run = True                                                                                        # Variable que define el arranque del programa
print("--> TRIANGULO DE PASCAL <--".center(50,"-"))                                               # Mensaje de bienvenida
while run == True:                                                                                # Mientras que la variable de ejecucion sea verdadera
    main()                                                                                        # Ejecutar el bloque principal
    run = ejecucion()  