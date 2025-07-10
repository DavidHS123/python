# En este programa, haremos una calculadora de salario, pero esta vez, la calculadora pedira al usuario, los dias trabajados, las horas trabajadas por día y el salario por hora, y luego calcula el salario total.
# Solicitar al usuario el número de días trabajados
dias_trabajados = int(input("Introduce el número de días trabajados: "))
# Solicitar al usuario el número de horas trabajadas por día
horas_por_dia = float(input("Introduce el número de horas trabajadas por día: "))
# Solicitar al usuario el salario por hora
salario_por_hora = float(input("Introduce el salario por hora: "))
# Calcular el salario total
salario_total = dias_trabajados * horas_por_dia * salario_por_hora
# Mostrar el resultado
print(f"El salario total por {dias_trabajados} días trabajados, {horas_por_dia} horas por día a {salario_por_hora} por hora es: {salario_total}")

# Este programa es un ejemplo simple de cómo calcular el salario total basado en los días trabajados, las horas trabajadas por día y el salario por hora.