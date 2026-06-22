# Piedra, Papel, Tijera, Lagarto, Spock:
# Implementa este juego contra la computadora usando condicionales anidados para todas las reglas de victoria. 
# Reglas
# Piedra aplasta Tijera **********
# Piedra aplasta Lagarto **********
# Papel cubre Piedra ***********
# Papel refuta Spock ***********
# Tijera corta Papel ***********
# Tijera decapita Lagarto *********
# Lagarto envenena Spock ***********
# Lagarto come Papel *******
# Spock rompe Tijera ***********    
# Spock vaporiza Piedra **********

import random                                                   # Importa la libreria random
# Se define en un diccionario los roles enlazados con un numero de opcion
roles = {                
    1:'Piedra',
    2:'Tijera',
    3:'Papel',
    4:'Lagarto',
    5:'Spock'}

def main():                                                                                     # Declaracion del bloque de codigo principal
    print('-'*50)                                                                               # ---------------------------
    # Indica al usuario las posibles opciones
    print('--> Eliga una de las siguientes opciones: \n--> (1) Piedra\n--> (2) Papel\n--> (3) Tijeras\n--> (4) Lagarto\n--> (5) Spock')
    rol = try_rol(roles)                                                                        # Toma un numero de opcion mediante la funcion try_rol       
    rol_maquina = random.randint(1,5)                                                           # Da a la maquina un rol random usando funcion de la libreria importada
    print(ganador(rol,rol_maquina,roles))                                                       # Imprime el mensaje que retorna la funcion del juego

def ganador(j, m, roles):                                                                       # Funcion que ejecuta la comparacion entre las 2 opciones
    j = int(j)                                                                                  # Convierte en entero la opcion del jugador
    m = int(m)                                                                                  # Convierte en entero la opcion de la maquina
    rol_jugador = roles[j]                                                                      # Usando el diccionario asigna el nombre de la opcion
    rol_maquina = roles[m]                                                                      # Usando el diccionario asigna el nombre de la opcion

    print(f"{'-'*50}\n--> Rol del jugador: {rol_jugador}\n--> Rol del enemigo: {rol_maquina}")  # Mensaje al usuario confirmando los roles de la iteracion

    if j == m:                                                                                  # Si los roles son iguales
        return '--> Empate!!'                                                                   # Devuelve empate

    # Comparacion entre las opciones, se describen todos los casos donde el jugador puede ganar

    if  (j==1 and m==2) or (j==1 and m==4) or \
        (j==3 and m==1) or (j==3 and m==5) or \
        (j==2 and m==3) or (j==2 and m==4) or \
        (j==4 and m==5) or (j==4 and m==3) or \
        (j==5 and m==2) or (j==5 and m==1):
        return f'--> Has Ganado!!! {rol_jugador} gana a {rol_maquina}.'                         # Si algun caso se cumple se devuelve mensaje de Juego ganado
    else:                                                                                       # Si no
        return f'--> Has Perdido!!! {rol_maquina} gana a {rol_jugador}'                         # Se asume que no empato ni gano, asi que la maquina lleva la ronda

def try_rol(roles):                                                                             # Funcion que recibe la entrada de opcion del usuario
    entrada = input('==> ').strip()                                                             # Toma una entrada y le quita los espacios de tenerlos
    try:                                                                                        # Intenta
        opcion =int(entrada)                                                                    # Guardar la entrada en una variable convirtiendola en int
    except ValueError:                                                                          # Excepto cuando ocurre ValueError
        print('--> Valor invalido, intente nuevamente')                                         # Mensaje indicando el error al usuario
        return try_rol(roles)                                                                   # Lo devuelve al inicio de la funcion
    if not opcion in roles.keys():                                                              # Si la opcion elegida no esta en las llaves del diccionario
        print('--> Eleccion fuera de rango, intente nuevamente ')                               # Mensaje indicando el error al usuario
        return try_rol(roles)                                                                   # Devuelve al usuario al inicio de la funcion
    return entrada                                                                              # Si todo esta en orden devuelve la entrada registrada

def ejecucion() :                                                                               # Funcion que define la ejecucion del programa principal
    print('-'*50,'\n--> Desea jugar de nuevo? \n--> 1 (SI)\n--> 2 (NO)')                        # Instruccion para el usuario
    eleccion = input('==> ')                                                                    # Toma una entrada
    if eleccion == '1':                                                                         # Si la eleccion es igual a 1
        return True                                                                             # Retorna verdadero
    elif eleccion == '2':                                                                       # Si es la eleccion es igual a 2
        print('-'*50,'\n--> Fin del programa','\n','-'*50)                                      # Mensaje de aviso fin del programa
        return False                                                                            # Devuelve falso
    else:                                                                                       # Si no es ninguna de las opciones
        print('-'*50,'\n--> Eleccion Invalida. Intente nuevamente')                             # Mensaje avisando el error al usuario
        return ejecucion()                                                                      # Retorna volviendo a ejecutar el programa
    
run = True                                                                                      # Variable que define el arranque del programa
print("--> PIEDRA PAPEL TIJERA LAGARTO SPCOK <--".center(50,"-"))                               # Mensaje de bienvenida
while run == True:                                                                              # Mientras que la variable de ejecucion sea verdadera
    main()                                                                                      # Ejecutar el bloque principal
    run = ejecucion()                                                                           # Actualiza la variable de arranque
