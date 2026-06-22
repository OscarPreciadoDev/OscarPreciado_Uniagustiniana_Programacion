# Analisis de constraseñas
# Pide una clave y valida :+8 caracteres, debe tener almenos un numero, una mayuscula, y un caracter especial

def validador(contrasenia):                                                                # Funcion que valida la contrasenia
    if any(caracter.isdigit() for caracter in contrasenia):                                # Si algun caracter es digito en la contrasenia
        if any(caracter.isalpha() for caracter in contrasenia):                            # Si algun caracter es del alfabeto
            if any(caracter.isupper() for caracter in contrasenia):                        # Si algun caracter es mayuscula
                if any(not  caracter.isalnum() for caracter in contrasenia):               # si algun caracter NO es alfanumerico (caracter especial)
                    validacion = True                                                      # Actualiza la variable validacion a True
                else:                                                                      # Si no hay caracteres especiales
                    validacion = False                                                     # Actualiza la variable de validacion a False
            else:                                                                          # Si no hay caracteres en mayuscula
                validacion = False                                                         # Actualiza la variable de validacion a False
        else:                                                                              # Si no hay caracteres alfabeticos 
            validacion == False                                                            # Actualiza la variable a False
    else:                                                                                  # Si no hay numeros
        validacion = False                                                                 # Actualiza la variable a false

    if validacion == True:                                                                 # Si al terminar los anteriores la variable termina en True
        print('-'*50)                                                                      # Separador visual
        return('Valida')                                                                   # Retorna 'Valida'
    else:                                                                                  # Si no ( False )
        print('-'*50)                                                                      # Separador visual
        return('Invalida')                                                                 # Retorna 'Invalida
    
def main():                                                                                # Funcion del programa principal
    print('-'*50)                                                                          # Separador visual
    print('--> Ingrese una contraseña para validacion: ')                                  # Instruccion para el usuario
    try_contraseña = input('==> ')                                                         # Toma una entrada y la guarda como contrasenia
    print(f'Contraseña {validador(try_contraseña)}')                                       # Imprime un string que llama a la funcion de validacion y imprime el resultado

def ejecucion() :                                                                          # Funcion que define la ejecucion del programa principal
    print('-'*50,'\n--> Desea ingresar una nueva contraseña? \n--> 1 (SI)\n--> 2 (NO)')    # Instruccion para el usuario
    eleccion = input('==> ')                                                               # Toma una entrada
    if eleccion == '1':                                                                    # Si la eleccion es igual a 1
        return True                                                                        # Retorna verdadero
    elif eleccion == '2':                                                                  # Si es la eleccion es igual a 2
        print('-'*50,'\n--> Fin del programa','\n','-'*50)                                 # Mensaje de aviso fin del programa
        return False                                                                       # Devuelve falso
    else:                                                                                  # Si no es ninguna de las opciones
        print('-'*50,'\n--> Eleccion Invalida. Intente nuevamente')                        # Mensaje avisando el error al usuario
        return ejecucion()                                                                 # Retorna volviendo a ejecutar el programa

run = True                                                                                 # Variable que define el arranque del programa
print("--> VALIDADOR DE CONTRASEÑA <--".center(50,"-"))                                    # Mensaje de bienvenida
while run == True:                                                                         # Mientras que la variable de ejecucion sea verdadera
    main()                                                                                 # Ejecutar el bloque principal
    run = ejecucion()                                                                      # Actualiza la variable de arranque