colores = ["Rojo", "Azul", "Verde"]
print(f"Lista de colores: {colores}")
color_eliminar = input("Escribe un color que no te guste (Rojo, Azul o Verde): ")
colores.remove(color_eliminar)
print(f"Lista final de colores: {colores}")