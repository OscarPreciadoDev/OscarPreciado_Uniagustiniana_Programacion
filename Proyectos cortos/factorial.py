# Factorial Acumulado: 
# Calcular el factorial de un número, pero muestra el proceso de la operación 
# ej: para 5, mostrar 5x4x3x2x1 = 120).

def ejecucion() :                                                                               # Funcion que define la ejecucion del programa principal
    print('-'*50,'\n--> Desea ingresar un nuevo numero? \n--> 1 (SI)\n--> 2 (NO)')              # Instruccion para el usuario
    eleccion = input('==> ')                                                                    # Toma una entrada
    if eleccion == '1':                                                                         # Si la eleccion es igual a 1
        return True                                                                             # Retorna verdadero
    elif eleccion == '2':                                                                       # Si es la eleccion es igual a 2
        print('-'*50,'\n--> Fin del programa','\n','-'*50)                                      # Mensaje de aviso fin del programa
        return False                                                                            # Devuelve falso
    else:                                                                                       # Si no es ninguna de las opciones
        print('-'*50,'\n--> Eleccion Invalida. Intente nuevamente')                             # Mensaje avisando el error al usuario
        return ejecucion()                                                                      # Retorna volviendo a ejecutar el programa
    
def try_num():                                                                                  # Funcion para tomar un numero
    try:                                                                                        # Intenta
        entrada = int((input('==> ')).strip())                                                  # Tomar una entrada, quitarle los espacios y convertirla en numero
        if entrada >= 0:                                                                        # Si la entrada es mayor o igual a 0
            return entrada                                                                      # La devuelve como respuesta de la funcion
        else:                                                                                   # Sino
            print('--> Rango invalido, el numero debe ser 0 o positivo')                        # Mensaje de error para el usuario
            return try_num()                                                                    # Vuelve a llamar a la funciondesde el inicio
    except ValueError:                                                                          # Excepto cuando hay ValueError
        print('--> Valor invalido, intentelo nuevamente')                                       # Mensaje indicando el error al usuario
        return try_num()                                                                        # Devuelve al inicio de l a funcion

def imprimir_factoriales(num):                                                                  # Funcion utilizada para calcular los numeros factoriales
    if num == 0:                                                                                # Si el numero ingresado es 0
        return(f'{'-'*50}\n--> !0 = 1')                                                         # El factorial es de caso especial da 1
    else:                                                                                       # Sino
        multiplicandos = []                                                                     # Lista vacia para los multiplicandos
        factorial = 1                                                                           # El factorial de todo numero tiene en sus multiplicandos el 1
        for numero in range(1,num +1):                                                          # Para cada numero en un rango de 1 hasta el numero inidicado (incluyendolo)
            multiplicandos.append(numero)                                                       # Agrega este numero a la lista
        for factor in range(1,num+1):                                                           # Para cada numero en un rango de 1 hasta el numero indicado (incluyendolo)
            factorial *= factor                                                                 # Multiplica al factorial (1) por todos estos numeros
        string_factorial = str(factorial)                                                       # Convierte el resultado factorial en str
        string_multiplicandos = (' x '.join(map(str,multiplicandos)))                           # Guarda en un str los multiplicandos formateados con ' x '
        string_final = f'{string_multiplicandos[::-1]} = {string_factorial}'                    # Crea un string final uniendo los multiplicandos y el factorial
        return(string_final)                                                                    # Retorna el string final
    
def main():                                                                                     # Funcion principal
    print(f'{'-'*50}\n--> Ingrese un numero para calcular su factorial: ')                      # Instruccion para el usuario
    numero = try_num()                                                                          # Guarda un numero llamando a la funcion de try_num
    print(imprimir_factoriales(numero))                                                         # Imprime el resultado de la funcion factorial

run = True                                                                                      # Variable que define el arranque del programa
print("--> NUMERO FACTORIAL <--".center(50,"-"))                                                # Mensaje de bienvenida
while run == True:                                                                              # Mientras que la variable de ejecucion sea verdadera
    main()                                                                                      # Ejecutar el bloque principal
    run = ejecucion()                                                                           # Actualiza la variable de arranque
