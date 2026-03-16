class CuentaBancaria:
    def __init__(self, titular:str, saldo_inicial:float):
        self.titular:str = titular
        self.saldo:float = saldo_inicial
    def depositar(self, cantidad:float) -> None:
        self.saldo += cantidad
        print(f"Deposito Exitoso. Nuevo saldo de {self.titular}: ${self.saldo}")    
    def retirar(self, cantidad: float) -> None:
        if cantidad > self.saldo:
            print(f"Error: {self.titular} no tiene fondos suficientes.")
        else:
            self.saldo -= cantidad
            print(f"Retiro exitoso. Saldo restante: ${self.saldo}")    

cuenta_ana = CuentaBancaria("ana lopez", 50000)

cuenta_ana.depositar(20000)
cuenta_ana.retirar(100000)
cuenta_ana.retirar(15000)