def calcular_salario_neto(salario_base: float, bonificacion: float = 0.0) -> float:
    """calcular el salario neto: Resta 8% de salud y pension, Suma la bonificacion(opcional) """

    descuento_salud_pension: float = salario_base * 0.08
    salario_despues_descuento: float = salario_base - descuento_salud_pension
    salario_final: float = salario_despues_descuento + bonificacion

    return salario_final



nomina_1: float = calcular_salario_neto(2000000)
nomina_2: float = calcular_salario_neto(2000000, 300000)

print(f"Salario sin bonificación: ${nomina_1}")
print(f"Salario con bonificación: ${nomina_2}")