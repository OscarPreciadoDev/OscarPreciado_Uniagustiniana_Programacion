# Ejemplo 1
def ordenar_lista(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

valores = [8, 3, 5, 1, 9]
print(f"Lista ordenada: {ordenar_lista(valores)}")


# Ejemplo 2
precios = [500, 200, 1000, 300, 700]
print(f"Precios ordenados: {ordenar_lista(precios)}")


# Ejemplo 3
calorias = [250, 100, 400, 150, 300]
print(f"Calorías ordenadas: {ordenar_lista(calorias)}")


# Ejemplo 4
distancias = [10, 5, 20, 15, 2]
print(f"Distancias ordenadas: {ordenar_lista(distancias)}")


# Ejemplo 5
tiempos = [60, 45, 30, 90, 15]
print(f"Tiempos ordenados: {ordenar_lista(tiempos)}")