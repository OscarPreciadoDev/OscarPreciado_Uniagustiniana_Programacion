# 2.	Validador de PIN Robusto: Crea un sistema que pida un PIN de 4 dígitos. El usuario tiene solo 3 intentos antes de que el programa imprima "SISTEMA BLOQUEADO" y termine.




def main(acceso, intentos, contrasenia):                                                               # Funcion que ejecuta el bloque principal del programa usando las variables principales                          
    pin_correcto = contrasenia                                                                         # Tomamos la contrasenia y se asigna a una variable
    print(f'{"-"*50}\n--> Ingrese su contrasenia')                                                     # Mensaje de instruccion para el usuario
    if intentos > 0:                                                                                   # Si los intentos no son el primero
        print(f'{"-"*50}\n--> LLeva {intentos} intentos')                                              # Indica cuantos intentos lleva al usuario
    if acceso == False and intentos < 3:                                                               # Si el acceso aun esta denegado y lleva menos de 3 intentos
        try:                                                                                           # Intenta         
            entrada = int(input('==> '))                                                               # Tomar una contrasenia y convertirla en entero
            if len(str(entrada))== 4:                                                                  # Si el tamanio de la entrada es de 4 caracteres
                if entrada == pin_correcto:                                                            # Si la entrada es igual al pin correcto
                    print(f'{"-"*50}\n--> Acceso concedido !! Bienvenido')                             # Mensaje indicando el acceso al usuario
                    return True, 4                                                                     # Retorna True (acceso) y 4 (intentos) (se saca del rango para asegurar fin del programa)
                else:                                                                                  # Si no
                    print(f'{"-"*50}\n--> PIN incorrecto')                                             # Mensaje indicando negacion al usuario
                    intentos += 1                                                                      # Aumenta un intento
                    return False, intentos                                                             # Devuelve False (acceso) y los intentos de la iteracion
            else:                                                                                      # Sino (pin de tamanio incorrecto)
                print(f'{"-"*50}\n--> Su PIN debe tener 4 digitos')                                    # Mensaje indicando el error de ingreso
                intentos += 1                                                                          # aumenta un intento
                return False, intentos                                                                 # Devuelve False (acceso) y los intentos de la iteracion            
        except ValueError:                                                                             # Excepto cuando hay ValueError (Ingreso de caracteres especiales)
            print(f'{"-"*50}\n--> Incorrecto (Su PIN debe ser un numero de 4 Digitos (XXXX))')         # Mensaje indicando la denegacion al usuario
            intentos +=1                                                                               # Aumenta un intento
            return False, intentos                                                                     # Devuelve False (acceso) y los intentos de la iteracion


def ejecucion(intentos,acceso):                                                                        # Funcion para la ejecucion del codigo
    if intentos < 3 and acceso == False:                                                               # Si los intentos son menores a 2 (3 es el limite) y el acceso aun no esta dado
        return True                                                                                    # Devuelve verdadero (Seguir intentando el programa)
    else:                                                                                              # Sino (o ya llego al limite o ya ingreso)
        return False                                                                                   # Devuelve verdadero

contrasenia = 1234                                                                                     # Contrasenia definida como correcta
intentos = 0                                                                                           # Intentos inicialmente empiezan en 0
acceso = False                                                                                         # El acceso comienza denegado
run = True                                                                                             # Variable que decide la ejecucion del programa

print('> VALIDADOR DE PIN <'.center(50,'-'))                                                           # Mensaje de bienvenida
while run == True:                                                                                     # Mientras que la ejecucion sea verdadera
    acceso, intentos = main(acceso, intentos, contrasenia)                                             # Reasignar estos valores usando la funcion principal
    run = ejecucion(intentos,acceso)                                                                   # Verifica si el programa aun esta en condiciones de continuar, sino se termina
print(f'{"-"*50}\n--> Fin del programa\n{'-'*50}')                                                     # Mensaje de cierre del programa