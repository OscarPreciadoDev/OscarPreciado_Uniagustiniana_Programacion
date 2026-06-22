# Pedir una cadena alfanumerica. Separa las letras de los numeros, suma los numeros y muestra las letras en mayuscula

def filtro(cadena):                                                              # Funcion que filtra la cadena ingresada
    letras = []                                                                  # Lista para las letras inicialmente vacia
    numeros = []                                                                 # Lista para los numeros inicialmente vacia
    for char in cadena:                                                          # Por cada elemento en la cadena
        try:                                                                     # Intenta
            numeros.append(int(char))                                            # Agregar a la lista de numeros el caracter convertido en entero
        except ValueError:                                                       # Excepto value error (se asume que el caracter no es numero, entonces es letra)
            letras.append(char)                                                  # Agrega el caracter a la lista de letras
    suma = sum(numeros)                                                          # Se suman los numeros de la lista de numeros
    letras_minus = " ".join(letras)                                              # Se crea un string con todas las letras de la lista
    letras_mayus = letras_minus.upper()                                          # Se normalizan todas a mayuscula
    return suma, letras_mayus                                                    # Devuelve como respuesta la suma y el str con las letras en mayuscula

def try_cadena():                                                                # Funcion que toma una cadena de entrada
    print(f'{sep}--> Ingrese una cadena para filtrar')                           # Instrucciones para el usuario
    try:                                                                         # Intenta
        entrada = input('==> ').strip()                                          # Toma una entrada y quita los espacios 
        if any(not char.isalnum() for char in entrada ):                         # Si algun caracter en la cadena no es alfanumerico
            print(f'{sep}--> Ingrese una palabra valida')                        # Mensaje indicando el error al usuario
            return try_cadena()                                                  # Devuelve al inicio de la funcion
        else:                                                                    # Si no (todo en orden)
            print(f'{sep}--> Cadena ingresada con exito')                        # Mensaje inidicando el ingreso de la cadena
            return entrada                                                       # Devuelve la entrada
    except ValueError:                                                           # Excepto con value error (entrada erronea)
        print(f'{sep}--> Ingrese una cadena valida')                             # Mensaje indicando el error al usuario
        return try_cadena()                                                      # Devuelve al inicio de la funcion
    
def ejecucion():                                                                 # Funcion que define la ejecucion del programa
    print(f"{sep}--> Desea ingresar una nueva cadena?\n--> (1) SI\n--> (2) NO")  # Mensaje de instruccion para el usuario
    try:                                                                         # Intenta
        entrada = input('==> ').strip()                                          # Toma una entrada y quita los espacios
        if entrada == "1":                                                       # Si la entrada es igual a '1'
            return True                                                          # Devuelve verdadero (se sigue ejecutando el programa)
        elif entrada == "2":                                                     # Sino si la entrada es igual a '2'
            print(f'{sep}--> Fin del programa\n{sep}')                           # Imprime mensaje inidicando el fin del programa
            return False                                                         # Devuelve verdadero (fin del programa)
        else:                                                                    # Sino (se asume una entrada distinta a las opciones)
            print(f'\n{sep}--> Ingrese una entrada valida')                      # Indica el error al usuario
            return ejecucion()                                                   # Devuelve al inicio de la funcion
    except ValueError:                                                           # Excepto con value error (entrada incorrecta)
        print(f'{sep}--> Ingrese una entrada valida')                            # Indica el error al usuario
        return ejecucion()                                                       # Devuelve al inicio de la funcion

sep = f'{'-'*50}\n'                                                              # ----
run = True                                                                       # variable que define la ejecucion del programa
print('> FILTRO DE CARACTERES <'.center(50,'-'))                                 # Mensaje de bienvenida
while run == True:                                                               # Mientras que la variable de ejecucion sea verdadera
    cadena = try_cadena()                                                        # asigna una cadena desde la funcion
    suma, mayusculas = filtro(cadena)                                            # Calcula la suma y dicta las mayusculas usando el filtro sobre la cadena
    print(f'--> Sumatoria : {suma}')                                             # Mensaje que imprime la sumatoria
    print(f'--> Letras : {mayusculas}')                                          # Mensaje que imprime las mayusculas
    run = ejecucion()                                                            # Se reasigna la variable de ejecucion