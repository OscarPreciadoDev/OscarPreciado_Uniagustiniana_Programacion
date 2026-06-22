n = int(input('--> Ingrese un numero: '))
factorial = 1 
proceso = ''

i = n
while i > 0:
    factorial *= i
    proceso += str(i) + (' x ' if i > 1 else "")
    i -= 1

print(f" {n}! -> {proceso} = {factorial}")