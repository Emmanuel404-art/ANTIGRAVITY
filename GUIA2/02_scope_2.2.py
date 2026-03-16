def convertir_moneda(cantidad: float, moneda: str = "COP") -> None:
    print(f"Procesando Transaccion: {cantidad} en moneda {moneda}")
convertir_moneda(5000, "USD")
convertir_moneda(150000)