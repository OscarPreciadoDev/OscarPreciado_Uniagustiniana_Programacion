# Conversor de tiempo total
# Pedir una cantidad de segundos entero y convertirla al formato exacto, Dias:Horas:Segundos:Minutos:Segundos



def try_segundos():                                                              # Funcion que toma una entrada de segundos                         
    print('--> Ingrese los segundos a normalizar')                               # Indicacion para el usuario
    try:                                                                         # Intenta
        entrada = int(input('==> '))                                             # Toma una entrada y la convierte a entero
        if entrada > 0:                                                          # Si la entrada es positiva
            print('--> Segundos ingresados exitosamente! ')                      # Mensaje de aceptacion
            return entrada                                                       # Devuelve esta entrada
        else:                                                                    # Si no
            print('--> Ingrese un numero valido')                                # Mensaje indicando el error al usuario
            return try_segundos()                                                # Devuelve al inicio de la funcion
    except ValueError:                                                           # Excepto cuando hay ValueError
        print('--> Error, ingrese un valor valido')                              # Imprime el error 
        return try_segundos()                                                    # Devuelve al inicio de la funcion
    
def tiempo_total(seg):                                                           # Funcion que normaliza el tiempo
    sobrante = seg                                                               # sobrante sera la variable que tiene los segundos sobrantes
    dias = sobrante // 86400                                                     # toma la parte entera de dividir los segundos entre los segundos de una dia
    sobrante =  sobrante % 86400                                                 # toma el restante de haber sacado los segundos del dia
    horas = sobrante // 3600                                                     # Toma la parte entera de dividir los segundos entre los segundos de una hora
    sobrante = sobrante % 3600                                                   # toma el restante de haber sacado los segundos de las horas
    minutos = sobrante // 60                                                     # Toma la parte entera de dividir los segundo sentre los segundos de un minuto
    sobrante = sobrante % 60                                                     # Toma el restante de haber sacado los segundos de los minutos
    segundos = sobrante                                                          # Los segundos sobrantes se asignan a esta variable
    print(sep,end="")                                                            # Separador visual
    impresion = (f'--> Dias: {dias:02}\n--> Horas: {horas:02}\n--> Minutos: {minutos:02}\n--> Segundos: {segundos:02}') # Mensaje normalizado con los calculos realizados
    return impresion

# 1 hora = 3600 segundos
# 1 minuto = 60 segundos
# 1 dia =  86400 segundos 

sep = f'{'-'*50}\n'                                                              # Separador visual

def ejecucion():                                                                 # Funcion que define la ejecucion del programa
    print(f'{sep}--> Desea ingresar un nuevo tiempo? \n--> (1) SI\n--> (2) NO')  # Mensaje de instruccion para el usuario
    try:                                                                         # Intenta
        eleccion = input('==> ').strip()                                         # Toma una entrada y quita los espacios
        if eleccion == '1':                                                      # Si la entrada es igual a 1
            return True                                                          # Devuelve verdadero (El programa se sigue ejecutando)
        elif eleccion == '2':                                                    # Si la entrada es igual a 2
            print(f'{sep}--> Fin del programa\n{sep}')                           # Mensaje indicando el fin del programa
            return False                                                         # Devuelve falso  (fin del programa)
        else:                                                                    # Sino ( se asume una entrada incorrecta )                   
            print(f'{sep}--> Eleccion Invalida. Intente nuevamente')             # Imprime mensaje de eleccion invalida
            return ejecucion()                                                   # Devuelve al inicio de la funcion 
    except ValueError:                                                           # Excepto cuando hay value error
        print(f'{sep}--> Ingrese una entrada valida')                            # Mensaje inidicando el error al usuario
        return ejecucion()                                                       # Devuelve al inicio de la funcion
    
run = True                                                                       # Variable que dfine la ejecucion del codigo
print('> CONVERSOR DE TIEMPO <'.center(50,'-'))                                  # Mensaje de bienvenida
while run == True:                                                               # Mientras que la variable de ejecucion sea verdadera
    segundos = try_segundos()                                                    # Toma una entrada para segundos
    print(tiempo_total(segundos))                                                # Imprime la normalizacion
    run = ejecucion()                                                            # Reasigna la variable de ejecucion