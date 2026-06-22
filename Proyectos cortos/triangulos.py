# Validador de triangulos pro
# Pedir 3 lados y 3 angulos
# Verificar si son validos (suma de angulos == 180)
# ------------------------------------------------------
# Clasificacion segun lados: 
# Clasificaciones
# Equilatero                || 3 lados iguales y 3 angulos iguales (60)
# Isoceles                  || 2 lados iguales y 2 angulos iguales
# Escaleno                  || 3 lados diferentes y 3 angulos diferentes
# -------------------------------------------------------
# Clasificacion segun angulos:
# Acutangulo                || 3 angulos menores a 90
# Rectangulo                || 1 angulo igual a 90
# Obtusangulo               || 1 angulo mayor a 90


def tomar_lados():                                                                     # Funcion para tomar los lados del triangulo
    entradas_l = input('--> ')                                                         # Toma los 3 lados del triangulo desde un input
    try:                                                                               # Intenta
        lados = [float(x) for x in entradas_l.split()]                                 # Guarda en una lista los valores separados por espacios como float
    except ValueError:                                                                 # Excepto cuando hay ValueError
        print('--> Los valores ingresados deben ser numeros, intente nuevamente!!')    # Mensaje indicando el error al usuario
        tomar_lados()                                                                  # Vuelve a llamar a la funcion desde el inicio
    if len(lados) != 3:                                                                # Si el tamaño de la lista es diferente de 3
        print('--> Numero de lados invalido, deben ser 3. Intente nuevamente !! ')     # Mensaje indicando el error al usuario
        tomar_lados()                                                                  # Vuelve a llamar a la funcion desde el inicio
    else:                                                                              # Si no encaja en la condicion anterior
        for i in lados:                                                                # Por cada elemento de la lista
            if i<=0:                                                                   # Si el elemento es 0 o negativo
                print('--> El lado del triangulo debe ser un numero positivo')         # Mensaje indicando el error al usuario
                tomar_lados()                                                          # Vuelve a llamar a la funcion
    return lados                                                                       # Si todo esta en orden devuelve como valor la lista de los lados validada

def tomar_angulos():                                                                   # Funcion para tomar los angulos del triangulo
    entradas_a = input('--> ')                                                         # Toma 3 angulos del triangulo desde un input
    try:                                                                               # Intenta
        angulos = [float(x) for x in entradas_a.split()]                               # Guarda en una lista los valores separados por espacios como float
    except ValueError:                                                                 # Excepto cuando hay ValueError
        print('--> Los valores ingresados debe ser numeros, intente nuevamente')       # Mensaje indicando el error al usuario
        tomar_angulos()                                                                # Vuelve a llamar a la funcion desde el inicio
    if len(angulos) != 3:                                                              # Si el tamaño de la lista es diferente de 3 
        print('--> Numero de lados invalidado, debe ser 3. Intente nuevamente!!')      # Mensaje indicando el error al usuario
        tomar_angulos()                                                                # Vuelve a llamar a la funcion desde el inicio
    else:                                                                              # Sino
        for i in angulos:                                                              # Por cada elemento en la lista verifica
            if i<=0:                                                                   # Si el elemento es menor o igual a 0
                print('--> El angulo del triangulo debe ser un numero positivo')       # Mensaje indicando el error al usuario
                tomar_angulos()                                                        # Vuelve a llamar a la funcion desde el inicio
    if sum(angulos) != 180:                                                            # Si la suma de los angulos es diferente de 180
        print('--> La suma de sus angulos debe ser de 180, intente nuevamente!!')      # Mensaje inidicando el error al usuario
        tomar_angulos()                                                                # Vuelve a llamar a la funcion desde el inicio
    return angulos                                                                     # Si todo es verificado exitosamente entrega la lista con los angulos

def clasificacion_l(l,a):                                                              # Funcion que clasifica el triangulo segun sus lados, usa como argumentos los lados y angulos del triangulo
    if len(set(l))==1 and len(set(a))==1:                                              # Si tiene 3 angulos iguales y 3 lados iguales
        return('Equilaterio')                                                          # Categoriza como Equilatero
    elif len(set(l))==2 and len(set(a))==2:                                            # Si tiene 2 angulos diferentes y 2 lados diferentes en su set 
        return('Isoceles')                                                             # Categoriza como Isoceles
    else:                                                                              # Sino significa que tiene 3 angulos diferentes y 3 lados diferentes
        return('Escaleno')                                                             # Categoriza como escaleno

def clasificacion_a(a):                                                                # Funcion que clasifica el triangulo segun sus angulos
    if any(x>90 for x in a):                                                           # Si algun angulo es mayor a 90
        return('Obtusangulo')                                                          # Devuelve obtusangulo
    elif any(x == 90 for x in a):                                                      # Si algun angulo es igual a 90
        return('Rectangulo')                                                           # Devuelve obtusangulo
    else:                                                                              # Sino siginifica que todos sus angulos son menores a 90 
        return('Acutangulo')

def main():                                                                                                        # Define el programa principal de ejecucion
    print('-'*75,'\n--> Ingrese el tamano de los 3 lados del triangulo separado por espacios:')                    # Instruccion para el usuario
    lados = tomar_lados()                                                                                          # Almacena los datos tomados por la funcion de lados en una variable
    print('-'*75,'\n--> Lados recibidos exitosamente!!')                                                           # Mensaje de confirmacion al usuario
    print('-'*75,'\n--> Ingrese los 3 angulos de su triangulo separados por espacios')                             # Instruccion para el usuario
    angulos = tomar_angulos()                                                                                      # Almacena los datos tomados por la funcion de angulos en una variable
    print('-'*75,'\n--> Angulos tomados exitosamente!!')                                                           # Mensaje de confirmacion al usuario
    print('-'*75,f'\n--> La clasificacion del triangulo segun sus lados es: {clasificacion_l(lados,angulos)}')     # Mensaje de clasificacion por lados y llama a la funcion de clasificacion lados
    print(f'--> La clasificacion del triangulo segun sus angulos es: {clasificacion_a(angulos)}')                  # Mensaje de clasificacion por angulos y llama a la funcion de clasificacion angulo

def ejecucion() :                                                                                                  # Funcion que define la ejecucion del programa principal
    print('-'*75,'\n--> Desea ingresar un nuevo triangulo? \n--> 1 (SI)\n--> 2 (NO)')                              # Instruccion para el usuario
    eleccion = input('--> ')                                                                                       # Toma una entrada
    if eleccion == '1':                                                                                            # Si la eleccion es igual a 1
        return True                                                                                                # Retorna verdadero
    elif eleccion == '2':                                                                                          # Si es la eleccion es igual a 2
        print('-'*75,'\n--> Fin del programa')                                                                     # Mensaje de aviso fin del programa
        return False                                                                                               # Devuelve falso
    else:                                                                                                          # Si no es ninguna de las opciones
        print('-'*75,'\n--> Eleccion Invalida. Intente nuevamente')                                                # Mensaje avisando el error al usuario
        return ejecucion()                                                                                         # Retorna volviendo a ejecutar el programa

run = True                                                                                                         # Variable que define el arranque del programa
print("\n\n","--> VALIDADOR DE TRIANGULOS PRO <--".center(73,"-"))                                                 # Mensaje de bienvennida
while run == True:                                                                                                 # Mientras que la variable de ejecucion sea verdadera
    main()                                                                                                         # Ejecuta el bloque principal
    run = ejecucion()                                                                                              # Actualiza la variable de arranque