

concesionario = []  


for i in range(3):
    print("\nRegistro del vehículo", i + 1)

    marca = input("Ingrese la marca: ")
    modelo = input("Ingrese el modelo: ")
    precio = float(input("Ingrese el precio: "))


    vehiculo = {
        "marca": marca,
        "modelo": modelo,
        "precio": precio
    }


    concesionario.append(vehiculo)


print("\n--- Vehículos Registrados ---")

for auto in concesionario:
    print(f"Vehículo registrado: Marca {auto['marca']}, Modelo {auto['modelo']}, Precio: ${auto['precio']}")