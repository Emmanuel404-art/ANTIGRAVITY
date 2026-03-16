carrito_compras = ["leche", "huevos", "pan"]
print(f"carrito inicial: {carrito_compras}")
carrito_compras.append("cafe")
print(f"agrego cafe: {carrito_compras}")
carrito_compras.remove("leche")
print(f"quito la leche: {carrito_compras}")
carrito_compras[0] = "huevos campesinos"
print(f"cambie los huevos normales: {carrito_compras}")