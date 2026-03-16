class MascotaVirtual:
    
    def __init__(self, nombre: str):
        self.nombre: str = nombre
        self.energia: int = 10
        print(f"🐾 Mascota {self.nombre} creada con energía inicial de {self.energia}")

    def jugar(self) -> None:
        self.energia -= 3
        print(f"{self.nombre} jugó. Energía actual: {self.energia}")

    def dormir(self) -> None:
        self.energia += 5
        print(f"{self.nombre} durmió. Energía actual: {self.energia}")


mi_mascota = MascotaVirtual("Firulais")


mi_mascota.jugar()
mi_mascota.dormir()