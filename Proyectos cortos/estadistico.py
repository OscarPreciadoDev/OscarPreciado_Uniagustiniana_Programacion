# Pedir numeros hasta que se ingrese "fin". Al terminar, muestra el promedio y el numero mas alto


def try_num(numeros):                                                           # Funcion que toma entradas y tiene en cuenta la lista de numeros                  
    print(f'{sep}--> Ingrese un numero, o "fin" para terminar el programa: ')   # Instrucciones para el usuario
    entrada = input('==> ').strip()                                             # Toma una entrada y quita los espacios
    try:                                                                        # Intenta 
        new_num = float(entrada)                                                # Tomar una entrada y convertirla en float
        numeros.append(new_num)                                                 # Agregar el numero a la lista
        return numeros , True                                                   # Devuelve como resultado la lista nueva, y True (para que run siga ejecutando)
    except ValueError:                                                          # Excepto con ValueError (se asume entrada tipo str)
        if entrada.lower() == 'fin':                                            # Si la entrada normalizada es igual a "fin"
            print(f'{sep}--> Fin del ingreso de datos')                         # Mensaje inidicando el fin de entrada de datos
            return numeros, False                                               # Devuelve la lista sin modificaciones y false (para que run se detenga)
        else:                                                                   # Sino (se asume otro tipo de entrada)
            print(f'{sep}--> Ingrese una entrada valida')                       # Indica el error al usuario
            return numeros, True                                                # Devuelve la lista sin modifica y true (para que run siga ejecutando)

sep = f'{'-'*60}\n'                                                             # ---------
run = True                                                                      # Variable que define el bucle de entrada de datos
numeros = []                                                                    # Lista de numeros inicialmente vacia
print('> Estadisticas de usuario <'.center(60,'-'))                             # Mensaje de bienvenida

while run == True:                                                              # Mientras que la variable de ejecucion sea verdadera  
    numeros, run = try_num(numeros)                                             # Reasigna la lista y la variable de ejecucion con la funcion que toma entradas

try:                                                                            # Intenta 
    numeros.sort(reverse=True)                                                  # Organizar la lista de numeros de mayor a menor
    mayor = numeros[0]                                                          # Toma el primer numero de la lista organizada
    promedio = (sum(numeros)/len(numeros))                                      # Calcula el promedio de la suma de los numeros dividido entre la cantidad
    print(f'{sep}--> El promedio de los numeros ingresados es de: {promedio:.2f}\n--> El mayor numero ingresado fue {mayor}\n{sep}') # Respuesta principal de promedio y mayor
except (ZeroDivisionError,IndexError):                                          # Excepto con estos dos problemas causados cuando la lista esta vacia
    print(f'{sep}--> No ha ingresado numeros\n{sep}')                           # Indica la ausencia de datos en la lista al usuario

