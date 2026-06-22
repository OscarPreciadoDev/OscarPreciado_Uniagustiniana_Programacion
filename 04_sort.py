# Orden de los datos 

# Visualizacion: Es mas facil para un humano leer una lista de nombres de la A a la Z

# Priorizacion: ordenar tareas por fecha de vencimiento o importancia

# Metodo Sort (metodo para un vector)
calificaciones = [
    30,
    45,
    20,
    35,
    10
]

# Ordenar de menor a mayor
calificaciones.sort()
print(f"Ordenar las calificaciones de forma ascendente: {calificaciones}")

# Ordenar de mayor a menor
calificaciones.sort(reverse=True)
print(f"Ordenar las calificaciones de forma descendente: {calificaciones}")

# Metodo burbuja (Metodo para dos vectores)

def lista_manual(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0,n-i-1):
            if lista[j]>lista[j+1]:
                lista[j],lista[j+1] = lista[j+1],lista[j]

    return lista

precios = [50, 1000, 1, 2000, 200]
print(f"Imprima los precios ordenados: {lista_manual(precios)}")


# Tupla

