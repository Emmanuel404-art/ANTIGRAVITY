class Vehiculo:
    def __init__(self, marca:str, modelo:str, año:int):
        self.marca: str = marca
        self.modelo: str = modelo
        self.año: int = año

vehiculo_1 = Vehiculo("Toyota","supra mk4",2008)
vehiculo_2 = Vehiculo("Nissan","Silvia s14",2012)
print(f"vehiculo_1: Marca {vehiculo_1.marca}, Modelo {vehiculo_1.modelo}, Año {vehiculo_1.año}")
print(f"vehiculo_2: Marca {vehiculo_2.marca}, Modelo {vehiculo_2.modelo}, Año {vehiculo_2.año}")