# filtro. Escribe un bucle for que recorra una lista de nombres, si encuentra el nombre "Admin", debe usar continue para no imprimirlo (por privacidad), pero debe imprimir todos los demas nombres


usuarios = [
    "Oscar",
    "Andres",
    "Camila",
    "Pancho",
    "Juan"
]

admin = "Pancho"

for user in usuarios:
    if user == admin:
        continue
    print(f">>> Welcome {user} ")