# Ejemplo 1
productos = [
    ("Laptop", 10),
    ("Tablet", 25),
    ("Celular", 50),
    ("Audifonos", 15)
]

productos_ordenados = sorted(productos, key=lambda item: item[1], reverse=True)

print("Productos ordenados por stock:")
for nombre, cantidad in productos_ordenados:
    print(f"{nombre:15} | Stock {cantidad}")


# Ejemplo 2
empleados = [
    ("Juan", 1200),
    ("Ana", 1500),
    ("Luis", 1000),
    ("Sofia", 1800)
]

empleados_ordenados = sorted(empleados, key=lambda item: item[1])

print("\nSalarios de menor a mayor:")
for nombre, salario in empleados_ordenados:
    print(f"{nombre:10} | Salario {salario}")


# Ejemplo 3
ciudades = [
    ("Bogota", 8000000),
    ("Medellin", 2500000),
    ("Cali", 2200000),
    ("Barranquilla", 1200000)
]

ciudades_ordenadas = sorted(ciudades, key=lambda item: item[1], reverse=True)

print("\nCiudades por población:")
for ciudad, poblacion in ciudades_ordenadas:
    print(f"{ciudad:15} | Habitantes {poblacion}")


# Ejemplo 4
cursos = [
    ("Python", 40),
    ("Java", 30),
    ("C#", 25),
    ("JavaScript", 50)
]

cursos_ordenados = sorted(cursos, key=lambda item: item[1])

print("\nCursos por duración:")
for curso, horas in cursos_ordenados:
    print(f"{curso:12} | Horas {horas}")


# Ejemplo 5
ventas = [
    ("Enero", 5000),
    ("Febrero", 7000),
    ("Marzo", 3000),
    ("Abril", 9000)
]

ventas_ordenadas = sorted(ventas, key=lambda item: item[1], reverse=True)

print("\nVentas por mes:")
for mes, total in ventas_ordenadas:
    print(f"{mes:10} | Ventas {total}")