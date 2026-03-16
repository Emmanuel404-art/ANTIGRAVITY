tiene_licencia = input("¿tienes licencia para conducir? (si/no):")
esta_sobrio = input("¿has bebido alcohol hoy? (si/no):")
if tiene_licencia == "si" and esta_sobrio == "no":
    print("puede conducir el vehiculo.")
else:
    print("entregue las llaves. No puede conducir.")