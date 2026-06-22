# Pedir nombre y apellido. Si el usuario escribe con espacios extra o minúsculas, corrígelo a formato "Apellido, Nombre" (ej: " perez , JUAN" -> "Perez, Juan").


def ejecucion() :                                                                               # Funcion que define la ejecucion del programa principal
    print('-'*50,'\n--> Desea ajustar un nuevo nombre? \n--> 1 (SI)\n--> 2 (NO)')               # Instruccion para el usuario
    eleccion = input('==> ')                                                                    # Toma una entrada
    if eleccion == '1':                                                                         # Si la eleccion es igual a 1
        return True                                                                             # Retorna verdadero
    elif eleccion == '2':                                                                       # Si es la eleccion es igual a 2
        print('-'*50,'\n--> Fin del programa','\n','-'*50)                                      # Mensaje de aviso fin del programa
        return False                                                                            # Devuelve falso
    else:                                                                                       # Si no es ninguna de las opciones
        print('-'*50,'\n--> Eleccion Invalida. Intente nuevamente')                             # Mensaje avisando el error al usuario
        return ejecucion()                                                                      # Retorna al inicio de la funcion

def ajustar_nombre(nombre):                                                                     # Funcion que ajusta el nombre
    palabras = nombre.split()                                                                   # ALmacena una lista con las palabras 
    palabras_ajustadas = [palabra.capitalize() for palabra in palabras]                         # Almacena las palabras capitalizadas de la lista anterior0
    nombre_ajustado = ' '.join(palabras_ajustadas)                                              # string que tendra las palabras capitalizadas separadas por un espacio
    return nombre_ajustado                                                                      # Retorna el nombre ajustado

def try_nombre():                                                                               # Funcion que recibe un intento de nombre
    entrada = input('==> ')                                                                     # Almacena la entrada de un usuario
    caracteres = entrada.replace(" ","")                                                        # Variable que almacena el input sin espacios 
    if any(not caracter.isalpha() for caracter in caracteres):                                  # Si algun caracter no es una letra en la variable anterior
        print(f'{'-'*50}\n--> El nombre ingresado unicamente debe tener letras\n--> Intente nuevamente') # Mensaje indicando el erro al usuario
        return try_nombre()                                                                     # Devuelve al inicio de la funcion
    else:                                                                                       # Si no (nombre sin caracteres invalidos validado:) )
        palabras = entrada.split()                                                              # Crea una lista para almacenar las palabras separadas por espacio
        if len(palabras) != 2:                                                                  # Si la lista palabra no tiene 2 elementos
            print(f'{'-'*50}\n--> Debe ingresar un nombre y un apellido')                       # Mensaje indicando el error al usuario
            return(try_nombre())                                                                # Retorna la funcion desde el inicio
        else:                                                                                   # Sino (nombre validado con 2 elementos:) )
            return(entrada)                                                                     # Devuelve el nombre ingresado

def main():                                                                                     # Codigo de ejecucion del bloque principal 
    print(f'{'-'*50}\n--> Ingrese un nombre para ajustar: ')                                    # Instruccion para el usuario
    nombre = try_nombre()                                                                       # Crea una variable y almacena el resultado de la funcion try_nombre
    nombre_ajustado = ajustar_nombre(nombre)                                                    # Almacena el nombre ajustado en una variable
    print(f'{'-'*50}\n--> El nombre ajustado es: {nombre_ajustado}')                            # Imprime en terminal un string que contiene el nombre arreglado

run = True                                                                                      # Variable que define el arranque del programa
print("--> Formateador de nombres <--".center(50,"-"))                                          # Mensaje de bienvenida
while run == True:                                                                              # Mientras que la variable de ejecucion sea verdadera
    main()                                                                                      # Ejecutar el bloque principal
    run = ejecucion()                                                                           # Actualiza la variable de arranque