estudiantes = [
    {"nombre": "ana", "nota": 90},
    {"nombre": "luis", "nota": 50}
]

for persona in estudiantes:
    if int(persona["nota"]) >= 60:
        print(f"{persona['nombre']} ha aprobado")
