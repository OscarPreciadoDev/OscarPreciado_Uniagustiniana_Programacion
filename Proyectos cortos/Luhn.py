# ALgoritmo de Luht (Tarjeta): Pedir un numero de tarjeta y verificar si es valido sumando sus digitos (duplicando los de posicion par y restando 9 si exceden 10)

def try_cardnumber():                                                                              # Funcion que recibe el input de tarjeta
    entrada = input('==> ')                                                                        # Recibe una entrada del usuario 
    entrada_limpia = "".join(entrada.split())                                                      # Recibe la entrada separando por espacios la entrada y luego juntandola sin ningun espacio, normalizandola
    try:                                                                                           # Intenta 
        int(entrada_limpia)                                                                        # convertir esta entrada a un numero entero
    except ValueError:                                                                             # Excepto cuando hay ValueError
        print('-'*50)                                                                              # Separador visual
        print('--> Valor Invalido, intente nuevamente! ')                                          # Mensaje de error para el usuario 
        return try_cardnumber()                                                                    # Retorna al inicio de la funcion
    return entrada_limpia                                                                          # Si todo esta en orden retorna la tarjeta normalizada

def algoritmo_luhn(card):                                                                          # Funcion que ejecuta el algoritmo de verificacion luhn
    digits =  list(card)                                                                           # Genera una lista con los caracteres de la tarjeta
    digits.reverse()                                                                               # Invierte el orden de la lista
    digits = [int(x) for x in digits]                                                              # Convierte a Int cada elemento de la lista
    pares = digits[1::2]                                                                           # Crea una lista aparte unicamente con los elementos de posicion (1,3,5...)
    regular = digits[::2]                                                                          # Crea una lista aparte unicamente con los elementos de posicion (0,2,4...)
    pares_duplicados = []                                                                          # Se crea una lista vacia donde se hara el proceso a los numeros de 2da posicion
    for i in pares:                                                                                # para cada elemento de 2da posicion
        if (i*2) >=10:                                                                             # Si al multiplicar el elemento este da 10 o mas
            pares_duplicados.append((i*2)-9)                                                       # Agrega a la lista de duplicados la multiplicacion de este numero por 2, y restandole 9 segun la instruccion
        else:                                                                                      # Si no supera el 10
            pares_duplicados.append(i*2)                                                           # Lo agrega unicamente multiplicandolo
    sumatoria = sum(pares_duplicados+regular)                                                      # Se crea una variable sumatoria que suma los numeros regulares, y los 2dos modificados
    if sumatoria % 10 == 0:                                                                        # Si la sumatoria es divisible entre 10
        print('-'*50)                                                                              # Separador visual  
        return('--> Numero de tarjeta valido!')                                                    # Retorna mensaje de aprovacion al usuario
    else:                                                                                          # Si no
        print('-'*50)                                                                              # Separador visual  
        return('--> Numero de tarjeta invalido!')                                                  # Retorna mensaje de rechazo al usuario

def main():                                                                                       # Funcion que ejecuta el bloque principal
    print('-'*50,'\n--> Ingrese un numero de tarjeta para validar: ')                             # Instruccion para el usuario
    card = try_cardnumber()                                                                       # Toma la tarjeta ingresada
    print(algoritmo_luhn(card))                                                                   # Imprime el relsutado de la verificacion con el algoritmo

def ejecucion() :                                                                                 # Funcion que define la ejecucion del programa principal
    print('-'*50,'\n--> Desea ingresar una nueva tarjeta? \n--> 1 (SI)\n--> 2 (NO)')              # Instruccion para el usuario
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
print("--> VERIFICADOR TARJETA DE CREDITO <--".center(50,"-"))                                    # Mensaje de bienvenida
while run == True:                                                                                # Mientras que la variable de ejecucion sea verdadera
    main()                                                                                        # Ejecutar el bloque principal
    run = ejecucion()                                                                             # Actualiza la variable de arranque