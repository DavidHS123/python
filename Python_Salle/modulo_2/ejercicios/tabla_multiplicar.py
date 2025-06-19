# En este programa, imprimiremos tablas de multiplicar utilizando un bucle while.

tabla = 0 # Puedes cambiar este valor para imprimir la tabla de multiplicar de otro número

while tabla <= 10:
    print(f"Tabla del {tabla}:")
    multiplo = 1

    while multiplo <= 10: 
        print(f"{tabla} x {multiplo} = {tabla * multiplo}")
        multiplo += 1

    print()  # Imprime una línea en blanco para separar las tablas
    tabla += 1

print("Fin de las tablas de multiplicar.")
# Este programa imprimirá las tablas de multiplicar del 0 al 10. 