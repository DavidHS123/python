# En este programa, haremos una calculadora de salario que solicita al usuario el número de horas trabajadas y el salario por hora, y luego calcula el salario total.

# Solicitar al usuario el número de horas trabajadas
horas_trabajadas = float(input("Introduce el número de horas trabajadas: "))
# Solicitar al usuario el salario por hora
salario_por_hora = float(input("Introduce el salario por hora (EUR/h): "))
# Calcular el salario total
salario_total = horas_trabajadas * salario_por_hora
# Mostrar el resultado
print(f"El salario total por {horas_trabajadas} horas trabajadas a {salario_por_hora} por hora es: {salario_total} EUR")
# Este programa es un ejemplo simple de cómo calcular el salario semanal basado en las horas trabajadas y el salario por hora.

# Podemos ampliarlo para incluir más funcionalidades, como manejar horas extras o diferentes tarifas de pago.
# También podemos agregar validaciones para asegurarnos de que los datos ingresados sean válidos, como verificar que el número de horas trabajadas no sea negativo o que el salario por hora sea un valor positivo.