# 4. Inversión Matemática: Pide un número entero (ej: 12345) y devuélvelo invertido (54321) usando solo operaciones matemáticas (// y %), sin convertir a string.

from ast import While, withitem
from multiprocessing import Value


def try_entrada():                                                                       # Funcion que toma un numero de entrada
    print(f'\n{'-'*50}\n--> Ingrese un numero: ')                                        # Instruccion para el usuario
    try:                                                                                 # Intente
        entrada = int(input('==> '))                                                     # Tomar una entrada, convertirla en entero
        return entrada                                                                   # Devolver la entrada
    except ValueError:                                                                   # Excepto (entrada que no es numero)
        print(f'{'-'*50}\n--> Ingrese un numero valido!! ')                              # Mensaje inidicando el error al usuario
        return try_entrada()                                                             # Devuelve al inicio de la funcion
    
def calcular_dig(entrada):                                                               # Calcula los digitos del numero ingresado
    numero = entrada                                                                     # Toma el numero
    digitos = 0                                                                          # Variable que almacenara la cantidad de digitos
    while numero > 0:                                                                    # Mientras que el numero a descomponer sea mayor a 0
        numero //= 10                                                                    # Se saca el ultimo numero y nos quedamos con lo demas
        digitos += 1                                                                     # Se aumenta la cantidad de digitos
    return(digitos)                                                                      # Devuelve la cantidad de digitos calculados

def ejecucion():                                                                         # Funcion que define la ejecucion del programa
    print(f'\n{'-'*50}\n--> Desea ingresar un nuevo numero?\n--> (1) SI\n--> (2) NO')    # Mensaje indicando la operacion al usuario
    try:                                                                                 # Intenta
        entrada = input('==> ').strip()                                                  # Tomar una entrada y quitarle los espacios
        if entrada == '1':                                                               # Si la entrada es igual a 1
            return True                                                                  # Devuelve verdadero (se sigue ejecutando el programa)
        elif entrada == '2':                                                             # Si la entrada es igual a 2 
            print(f'{'-'*50}\n--> Fin de programa\n{'-'*50}')                            # Mensaje indicando el fin del programa
            return False                                                                 # Devuelve falso (fin del programa)
        else:                                                                            # Si no ( se asume una entrada distinta a las opciones )
            print(f'{'-'*50}\n--> Ingrese una opcion valida')                            # Mensaje indicando el error al usuario
            return ejecucion()                                                           # Devuelve al inicio de la funcion 
    except ValueError:                                                                   # Excepto cuando hay value error (alguna entrada que bloquee el programa)
        print(f'{'-'*50}\n--> Error de entrada, ingrese una opcion valida')              # Mensaje inidicando el error al usuario
        return ejecucion()                                                               # Devuelve al inicio de la funcion

def invert(numero, digitos):                                                             # Funcion que invierte el numero

    impresion = numero                                                                   # Variable donde se almacena el numero a transformar
    print('-'*50)                                                                        # ----------------
    print('==> El numero invertido es: ',end=" ")                                        # Impresion en consola
    for digito in range(digitos):                                                        # Para cada digito en un rango de la variable digitos (tamanio)
        residuo = impresion%10                                                           # Guarda el residuo de dividir en 10
        impresion //= 10                                                                 # Quita un digito al numero a tranformar
        print(residuo,end="")                                                            # Imprime ese numero retirado y no da salto de linea

run = True                                                                               # Variable que define la ejecucion del programa  
print('> INVERSOR DE NUMEROS <'.center(50,'-'))                                          # Mensaje de bienvenida
while run == True:                                                                       # Mientras que la variable de ejecucion sea verdadera
    numero = try_entrada()                                                               # Intenta tomar un numero de entrada
    digitos = calcular_dig(numero)                                                       # Cantidad de digitos del numero
    invertido = invert(numero,digitos)                                                   # Funcion que invierte el numero y de paso lo imprime
    run = ejecucion()                                                                    # Reasigna la variable de ejecucion