def calcular_iva(precio_base: float) -> float :
    """calcula y retorna el precio total con un iva del 19%"""
    iva: float = precio_base * 0.19
    precio_final:float = precio_base + iva
    return precio_final
factura_1:float = calcular_iva(10000)    
factura_2:float = calcular_iva(5000)
print(f"Total a pagar factura 1: ${factura_1}")
print(f"Total a pagar factura 2: ${factura_2}")