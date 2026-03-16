edad_usuario = int(input("por favor, ingresa tu edad en numeros: "))
print("evaluando permisos de acceso...")
if edad_usuario >= 18:
    print("acceso concedido: eres mayor de edad.")
elif edad_usuario >= 13 :
    print("acceso restringido: eres adolecente, necesitas permiso de un tutor.")
else:
    print("acceso denegado: eres menor de edad")
print("Gracias por usar el sistema")    