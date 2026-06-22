capital = int(input('--> Ingrese el capital: '))
rentabilidad = int(input('--> Ingrese una retabilidad anual % '))
anios = int(input('--> Ingrese los anios: '))

porcentaje = rentabilidad/100

for anio in range(1,anios+1):
    capital = capital * (1+porcentaje)
    print(f'Año : {anio} Capital: {capital}')