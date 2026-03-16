impuesto_nacional: float = 0.19
def calcular_descuento(precio: float) -> float:
    descuento_local: float = precio * 0.10
    precio_con_impuesto: float = precio + (precio * impuesto_nacional)
    return precio_con_impuesto - descuento_local
resultado: float = calcular_descuento(1000)
print(f"Precio Final: {resultado}")