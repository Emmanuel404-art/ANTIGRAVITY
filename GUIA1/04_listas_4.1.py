inventario_frutas = ["manzana","pera","mango","banano"]
print(f"la primera fruta es: {inventario_frutas[0]}")
print(f"la tercera fruta es: {inventario_frutas[2]}")
print("---imprimiendo viñetas automaticas---")
for fruta in inventario_frutas:
    print(f"- {fruta} disponible en bodega")