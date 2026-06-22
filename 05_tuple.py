# Tuplas

inventario = [
    ("PC",15),
    ("Mouse",100),
    ("Teclado Inalambrico",20),
    ("Monitor",35)
]

inventario_ordenado =  sorted(inventario, key=lambda item: item[1], reverse=True)

print(f"Inventario ordenado mayor a menor: ")

for dispositivos, cantidad in inventario_ordenado:
    print(f"Producto: {dispositivos:25} | Stock {cantidad}")


print('-'*50)

# Identifico el mayor y el menor
producto_top = inventario_ordenado[0]
producto_menos_vendido = inventario_ordenado[-1]

print(f"El producto con mas existencias: {producto_top[0]} {producto_top[1]} unidades")
print(f"EL producto con menos existencias: {producto_menos_vendido[0]} {producto_menos_vendido[1]} unidades")