total_ahorrado = 0
for mes in range(1,4):
    consignacion = int(input(f"¿cuanto dinero vas a ahorrar en el mes {mes}?:"))
    total_ahorrado = total_ahorrado + consignacion
print(f"¡ahorro completado! tienes un total de: ${total_ahorrado}")