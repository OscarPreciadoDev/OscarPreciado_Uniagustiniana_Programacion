# match se utiliza para saber que camino tomar

'''
match variable:
    case valor1:
        # Si el codigo es una variable == valor1
    case valor2:
        # Si el codigo es una variable == valor2
    case _:
        # si el codigo es una variable vacia (default) 
'''

dia = int(input('==> Ingrese un numero del 1 al 7: '))

match dia:
    case 1:
        print(">>> Lunes aprendo ingles")
    case 2:
        print(">>> El martes aprendo calculo")
    case 3:\
        print(">>> El miercoles aprendo fisica")  
    case 4:
        print(">>> El jueves aprendo aprendo algebra")
    case 5:
        print(">>> El viernes aprendo musica")
    case 6:
        print(">>> El sabado aprendo aritmetica")
    case 7:
        print(">>> El domingo aprendo ciencias de la ebriedad")
    case _:
        print(">>> Dia no valido")