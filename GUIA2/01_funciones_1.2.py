def crear_perfil(nombre: str, rol:str)-> None:
    """registra un nuevo perfil en el sistema."""
    print(f"Registrando en base de datos: {nombre} | permisos: {rol}")
crear_perfil("carlos", "admin")
crear_perfil("ana", "ventas")