class Servidor:
    def __init__(self, nombre:str, ip:str, ram_gb:int):
        self.nombre:str = nombre
        self.ip:str = ip
        self.ram_gb:int = ram_gb
        self.estado:str = "Apagado"
server_ventas = Servidor ("ventas-01", "192.168.1.10", 16)
server_bd = Servidor("Database-Main", "210.0.0.5", 65)
print(f"El servidor {server_ventas.nombre} tiene {server_ventas.ram_gb}GB de RAM.")
print(f"El servidor {server_bd.nombre} actualmente esta: {server_bd.estado}")