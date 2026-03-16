def calcular_area_rectangulo(base: float, altura: float) -> float:
    """Retorna el área de un rectángulo"""
    area: float = base * altura
    return area



resultado = calcular_area_rectangulo(5.0, 3.0)
print(f"El área del rectángulo es: {resultado}")