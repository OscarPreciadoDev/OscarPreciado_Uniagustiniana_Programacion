# Crear un cronometro que cuente HH:MM:SS usando bucles anidados y una pausa de un segundo entre cada incremento

import time                                                     # Importa la libreria time de la cual se usara la funcion time.sleep()

h = 00                                                          # Se define el tiempo acumulado en 00 para todo
m = 00
s = 00

print("--> RELOJ DE CONSOLA <--".center(50,"-"))                # Mensaje de bienvenida                                                  
while True:                                                     # Bucle infinito
    while h<24:                                                 # Mientras que las horas sean menores a 24
        while m<60:                                             # Mientras que los minutos sean menores a 60
            while s<60:                                         # Mientras que los segundos sean menores a 60
                print(f'{h:02}:{m:02}:{s:02}'.center(50))       # Imprime el reloj, dandole :00 de tamaño a los numeros
                s +=1                                           # En cada iteracion aumenta un segundo
                time.sleep(1)                                   # Espera un segundo para la siguiente iteracion
            m +=1                                               # Cuando llegue a 60 segundos aumenta un minuto
            s = 0                                               # Se actualiza a 0 los segundos
        h += 1                                                  # Cuando llege a 60 minutos aumenta una hora
        m = 0                                                   # Se actualiza a 0 los minutos



