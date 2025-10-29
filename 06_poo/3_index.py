class Conta_bancaria:
    def __init__(self, titular, saldo: float) -> None:
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor: int):
        if valor <= 0:
            print("Valor invalido.")
        else:
            self.saldo += valor
    