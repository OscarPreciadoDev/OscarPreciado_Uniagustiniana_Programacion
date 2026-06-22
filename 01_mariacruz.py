# Ingresar una cadena alfanumerica
# Separar letras de numeros
# Mostrar suma de numeros
# Mostar letras en mayusculas

cadena = input('--> Ingrese una cadena: ')

letras = ''
suma = 0

for caracter in cadena:
    if caracter.isalpha():
        letras+= caracter.upper()
    elif caracter.isdigit():
        suma+= int(caracter)

print(f'Letras : {letras}')
print(f'Suma de numeros: {suma}')

