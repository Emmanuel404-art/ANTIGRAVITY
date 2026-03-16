print("---diagnostico de red---")
hay_internet = input("¿el modem tiene luces encendidas? (si/no):")
if hay_internet == "si":
    print("paso 1 : el equipo recibe energia.")
    luz_roja = input("¿alguna de las luces es color rojo? (si/no):")
    if luz_roja =="si":
      print("fallo detectado: problema en la fibra optica. llame a soporte.")
    else:
      print("todo normal: su conexion esta operando al 100%.")
else:
    print("Fallo critico: verifique que el equipo este conecado a la corriente.")