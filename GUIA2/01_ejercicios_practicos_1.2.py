def es_mayor_de_edad(edad: int) -> bool:
    """Retorna True si es mayor de edad, de lo contrario False"""
    if edad >= 18:
        return True
    else:
        return False

edad_usuario = 20

if es_mayor_de_edad(edad_usuario):
    print("Es mayor de edad")
else:
    print("Es menor de edad")