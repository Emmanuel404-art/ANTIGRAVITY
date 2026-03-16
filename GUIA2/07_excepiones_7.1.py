class CajeroAutomatico:
    def __init__(self):
        self.efectivo_disponible: float = 10000.0

    def solicitar_retiro(self) -> None:
        print("--- Bienvenido al Cajero ---")

        try:
            monto_str: str = input("Ingrese la cantidad a retirar (solo números): ")

            monto: float = float(monto_str)

            if monto == 0:
                raise ValueError("No puede retirar cero pesos.")

            self.efectivo_disponible -= monto
            print(f"Retiro exitoso. Quedan ${self.efectivo_disponible} en el cajero.")

        except ValueError as e:
            print(f" ERROR DE FORMATO: Usted ingresó caracteres inválidos. ({e})")

        except Exception as e:
            print(f" ERROR CRÍTICO DESCONOCIDO: Contacte soporte. Detalles: {e}")

        finally:
            print("Expulsando tarjeta... Gracias por utilizar nuestra red.\n")


mi_cajero = CajeroAutomatico()

mi_cajero.solicitar_retiro()