# Solicita un rango (inicio y fin y muestra todos los numeros primos que se encuentran en ese intervalo)

def try_range():                                                                            # Funcion que toma el rango donde se hara la busqueda de primos
    entrada = input('--> Ingrese el intervalo separado por espacio:  ').split()             # Input que tomara dos valores separados por espacios almacenando en una lista
    try:                                                                                    # Intenta
        entrada = [int(x) for x in entrada]                                                 # Convertir los elementos de la lista en enteros
    except ValueError:                                                                      # Excepto cuando hay ValueError
        print('--> Valor invalido! Intente nuevamente')                                     # Mensaje de error para el usuario
        return try_range()                                                                  # Retorna la funcion desde el inicio
    if not len(entrada)==2:                                                                 # Si la lista no tiene 2 elementos exactamente
        print('--> Debe ingresar 2 valores. Intente nuevamente')                            # Mensaje de error para el usuario
        return try_range()                                                                  # Retorna la funcion desde el incio
    elif not entrada[0] < entrada[1]:                                                       # Si el intervalo no es logico (inicio menor / Final mayor)
        print('El inicio debe ser menor que el final del rango. Intente nuevamente')        # Mensaje de error para el usuario
        return try_range()                                                                  # Retorna la funcion desde el inicio
    elif any(x<0 for x in entrada):                                                         # Si algun numero en la entrada es negativo
        print('--> El intervalo debe ser positivo')                                         # Indica que el intervalo debe ser positivo
        return try_range()                                                                  # Retorna la funcion desde el inicio
    return(entrada)                                                                         # Si todo esta en orden retorna la lista "entrada"

def main():                                                                                 # Funcion del bloque principal
    print('-'*75)                                                                           # Separador visual
    intervalo = try_range()                                                                 # Almacena "entrada" en una variable
    print('-'*75)                                                                           # Separador visual
    inicio, fin = intervalo                                                                 # Toma los valores de entrada y los guarda en 2 variables de inicio y fin
    for numero in range(inicio,fin+1):                                                      # Para cada numero en el intervalo dado (incluyendo el fin)
        if numero <=1:                                                                      # Si el numero es menor o igual a uno
            primo = False                                                                   # No es primo
        else:                                                                               # Sino
            primo = True                                                                    # Inicialmente se asume que el numero es hipoteticamente primo
            for i in range(2,numero):                                                       # Para cada numero entre 2 y ese numero
                if numero%i== 0:                                                            # Si al dividir el numero entre esos intentos da 0
                    primo = False                                                           # Significa que hay mas divisiores, por lo que no es primo
                    break                                                                   # Sale del for
        if primo == True:                                                                   # Si el numero termina el bucle con la variable primo como verdadera
            print(numero)                                                                   # Se imprime

def ejecucion() :                                                                           # Funcion que define la ejecucion del programa principal
    print('-'*75,'\n--> Desea ingresar una nuevo intervalo? \n--> 1 (SI)\n--> 2 (NO)')      # Instruccion para el usuario
    eleccion = input('--> ')                                                                # Toma una entrada
    if eleccion == '1':                                                                     # Si la eleccion es igual a 1
        return True                                                                         # Retorna verdadero
    elif eleccion == '2':                                                                   # Si es la eleccion es igual a 2
        print('-'*75,'\n--> Fin del programa')                                              # Mensaje de aviso fin del programa
        return False                                                                        # Devuelve falso
    else:                                                                                   # Si no es ninguna de las opciones
        print('-'*75,'\n--> Eleccion Invalida. Intente nuevamente')                         # Mensaje avisando el error al usuario
        return ejecucion()                                                                  # Retorna volviendo a ejecutar el programa

run = True                                                                                  # Variable que define el arranque del programa
print("\n\n","--> NUMEROS PRIMOS <--".center(73,"-"))                                       # Mensaje de bienvenida
while run == True:                                                                          # Mientras que la variable de ejecucion sea verdadera
    main()                                                                                  # Ejecutar el bloque principal
    run = ejecucion()                                                                       # Actualiza la variable de arranque