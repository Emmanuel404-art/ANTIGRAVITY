class SistemaSeguridad:
    def __init__(self, pin_acceso: int):
        self.usuario: str = "admin"
        self.__pin_secreto: int = pin_acceso
        self.__alarma_activada: bool = True

    def desactivar_alarma(self, intento_pin:int) -> None:
        if intento_pin == self.__pin_secreto:
            self.__alarma_activada = False
            print("Alarma Desactivada")
        else:
            print("Intruso Detectado, Llamando a la policia.")    

casa_central = SistemaSeguridad(1234)
print(casa_central.__pin_secreto)
casa_central.desactivar_alarma(9999)
casa_central.desactivar_alarma(1234)            
