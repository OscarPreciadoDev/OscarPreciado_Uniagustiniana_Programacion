from curses.ascii import isdigit


def nombre_funcion(parametros):
    return "resultado"

def saludar():
    print ("Saludos para los estudiantes de programacion")

saludar()

def personalizado(nombre):
    print(f"Hola buen dia {nombre}")

personalizado('Jeronimo')


def calcular_propinas(total,porcentaje=15):

    propina = total * porcentaje/100

    return propina

cuenta_cliente = 55000
propina = calcular_propinas(cuenta_cliente)
print(propina)
propina_generosa = calcular_propinas(cuenta_cliente,20)

print(f"Cuenta del cliente: {cuenta_cliente}")
print(f"Propina: {propina}")
print(f"Propina generosa: {propina_generosa}")

argumento1 = 2
argumento2 = 3


def nombre_funcion(argumento1,argumento2):
    # Aqui va el codigo que se ejecuta al llamar a la funcion
    resultado = argumento1 + argumento2
    return resultado

# Aqui se invoca a la funcion aparte
variable = nombre_funcion(argumento1,argumento2) # 5

# Funcion de usuario
def sumar(num1,num2):
    suma = num1+num2
    return suma
a = 1
b = 2
a_mas_b = sumar(a,b)  # 3

# Funcion built-in
numeros = [1,2]
suma_de_numeros = sum(numeros) # 3


print("Hola",end='') # endwih= "\n"

# Funcion que verifica si un objeto es string

isinstance("Hola", str) # True 

# Los parametros son objeto , clase 


# Parametros por default
print("Hola",end="\n")  # Imprime Hola (salto de linea al final)

# Parametro modificado
print("Hola",end=":)") # Imprime Hola :) (sin salto de linea)



def elevar(base,exponente):
    potencia  = base ** exponente
    return potencia

a = 2
b = 3

a_elevado_b = elevar(a,b)  # 8

def funcion(num1,num2):
    sumar = num1+num2

    print(f"{num1} + {num2} = {sumar}")  # No termina la ejecucion del bloque
    return sumar                         # Si termina la ejecucion del bloque


# variable =  lambda parametro1, parametro2 : Expresion
suma = lambda a, b: a + b

print(suma(2, 3))  # 5



def ejemplo():
    interna = "Hola" # Variable local

externa = "Mundo"    # Variable global


def fun_entrada():
    entrada = input('(1) Si | (2) No') 
    if entrada == "1" or entrada == "2":  # Caso de salida
        return True
    else:                                 # Caso de retorno
        fun_entrada()



isdigit(32) # True