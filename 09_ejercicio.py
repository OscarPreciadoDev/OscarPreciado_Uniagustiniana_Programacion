# Cajero automatico

saldo =  150000

while True:
    print("""
>>> CAJERO AUTOMATICO
>>> (1) RETIRAR
>>> (2) CONSULTAR SALDO
>>> (3) SALIR
""")
    eleccion =  int(input("==> "))

    match eleccion:
        case 1:
            print('>>> Ingrese el monto a retirar :')
            retiro = int(input("==> "))
            saldo -= retiro
            print(f'>>> Retiro realizado, su saldo actual es de ${saldo}')
        case 2:
            print(f">>> Su saldo actual es ${saldo}")
        case 3:
            print(">>> Fin del programa")
            break
        case _:
            print(">>> Eleccion no valida, intente nuevamente!!")