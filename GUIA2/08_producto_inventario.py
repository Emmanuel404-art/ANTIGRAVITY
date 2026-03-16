class Producto:

    def __init__(self, nombre: str, precio: float, stock: int):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad: int) -> None:
        try:
            if cantidad > self.stock:
                raise ValueError("Stock insuficiente")

            self.stock -= cantidad
            print(f" Venta realizada: {cantidad} unidades de {self.nombre}")
            print(f"Stock restante: {self.stock}")

        except ValueError as error:
            print(f" Error al vender {self.nombre}: {error}")

class ProductoPerecedero(Producto):

    def __init__(self, nombre: str, precio: float, stock: int, dias_vencimiento: int):
        super().__init__(nombre, precio, stock)
        self.dias_vencimiento = dias_vencimiento

producto1 = Producto("Arroz", 3500.0, 5)
producto2 = ProductoPerecedero("Leche", 2.5, 10, 7)

producto1.vender(2)
producto2.vender(3)

producto1.vender(10)