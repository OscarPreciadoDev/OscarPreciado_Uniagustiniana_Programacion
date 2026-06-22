# Pedir una palabra y un numero de desplazamiento, muestra la palabra resultante desplazando cada letra en el alfabeto

def cesar (word, desplazamiento):                                                               
    new_word = ''                                                                # Funcion que crea una palabra nueva usando la base y el desplazamiento deseado
    for i in word:                                                               # Por cada caracter en la palabra
        if i in alfabeto:                                                        # Si el caracter esta en el alfabeto (minuscula)
            posicion = alfabeto.index(i)                                         # Se calcula la posicion dentro del alfabeto del caracter
            new_posicion = posicion + desplazamiento                             # Se crea una nueva posicion como la inicial + el desplazamiento
            new_letra = alfabeto[new_posicion]                                   # La nueva letra se toma en la nueva ubicacion
            new_word += new_letra                                                # Se agrega esa nueva letra a la nueva palabra
        elif i in alfabeto_mayus:                                                # Si no si la letra esta en el alfabeto mayus (mayuscula)
            posicion = alfabeto_mayus.index(i)                                   # Se calcula la posicion dentrl del alfabeto del caracter
            new_posicion =  posicion + desplazamiento                            # La nueva posicion sera la posicion inicial + desplazamiento
            new_letra =  alfabeto_mayus[new_posicion]                            # Se toma la nueva letra de la nueva posicion
            new_word += new_letra                                                # Se agrega la nueva letra a la palabra
        else:                                                                    # Si no (no es un caracter) 
            new_word += i                                                        # se agrega igual sin modificaciones a la nueva palabra
    return new_word                                                              # Se devuelve la nueva palabra

def try_word():                                                                  # Funcion que toma una palabra
    print(f'{sep}--> Ingrese una palabra para cifrar')                           # Instruccion para el usuario
    entrada = input('==> ').strip()                                              # Toma una entrada y quita los espacios   
    return entrada                                                               # Devuelve el ingreso

def try_desplazamiento():                                                        # Funcion que toma un desplazamiento
    print(f'{sep}--> Ingrese la cantidad de desplazamiento que desea')           # Instruccion para el usuario
    try:                                                                         # Intenta
        entrada = int(input('==> '))                                             # Tomar una entrada y convertirla en entero
        if -26 <= entrada <= 26 :                                                # Si la entrada esta en el rango (mas se sale del tamanio del alfabeto)
            return entrada                                                       # Devuelve la entrada de desplazamiento
        else:                                                                    # Sino (se asume un numero fuera de rango)
            print(f'{sep}--> Debe ingresar un numero entre -26 y 26')            # Se indica al usuario el error   
            return try_desplazamiento()                                          # Devuelve al inicio de la funcion
    except ValueError:                                                           # Excepto value error (entrada como str, float o otros)
        print(f'{sep}--> Ingrese un valor valido')                               # Mensaje indicando el error al usuario
        return try_desplazamiento()                                              # Devuelve al inicio de la funcion

def ejecucion():                                                                 # Funcion que determina la ejecucion del programa 
    print(f'{sep}--> Desea ingresar una nueva palabra?\n--> (1) SI\n--> (2) NO') # Instrucciones para el usuario    
    try:                                                                         # Intenta 
        entrada = input('==> ')                                                  # Tomar una entrada
        if entrada == '1':                                                       # Si la entrada es igual a '1'
            return True                                                          # Devuelve verdadero (sigue ejecutando)
        elif entrada == '2':                                                     # Sino si la entrada es igual a '2'
            print(f'{sep}--> Fin del programa\n{sep}')                           # Imprime fin del programa
            return False                                                         # Devuelve falso (no se ejecuta mas)
        else:                                                                    # Sino (se asume otra entrada fuera de las opciones)
            print(f'{sep}--> Ingrese una opcion valida')                         # Mensaje inidicando el error al usuario
            return ejecucion()                                                   # Devuelve al inicio de la funcion
    except ValueError:                                                           # Excepto con value error ( entrada invalida)
        print(f'{sep}--> Ingrese una entrada valida')                            # Muestra el error al usuario
        return ejecucion()                                                       # Devuelve al inicio de la funcion
    
alfabeto = 'abcdefghijklmnopqrstuvwxyz'                                          # Declara la variable que contiene la guia de alfabeto
alfabeto_mayus = alfabeto.upper()                                                # Alfabeto pero en mayuscula
sep = f'{'-'*50}\n'                                                              # ------
run = True                                                                       # Variable que define la ejecucion del programa
print('> CIFRADO CESAR <'.center(50,'-'))                                        # Mensaje de bienvenida
while run == True:                                                               # Mientras que la variable de ejecucion sea verdadero
    palabra = try_word()                                                         # Toma una palabra usando la funcion
    desplazamiento = try_desplazamiento()                                        # Toma un desplazamiento usando la funcion
    palabra_cifrada = cesar(palabra,desplazamiento)                              # Crea una palabra cifrada usando los datos brindados por el usuario
    print(f"{sep}--> La palabra '{palabra}' cifrada {desplazamiento} unidades es '{palabra_cifrada}'")   # Imprime una respuesta principal
    run = ejecucion()                                                            # Se reasigna la variable de ejecucion del codigo