"""Exercício 03.
Desenvolva uma classe que represente uma conta bancária com os seguintes atributos:
titular e saldo.
Adicione métodos para realizar operações de depósito e saque na conta.
Certifique-se de tratar casos onde o saldo pode se tornar negativo após um saque.
Após definir a classe, crie uma instância dela e realize algumas operações de depósito
e saque para verificar o funcionamento dos métodos implementados.
"""


class ContaBancaria:
    def __init__(self, titular: str, saldo: float) -> None:
        self.titular: str = titular
        self.saldo: float = saldo

    def deposito(self, valor: float) -> str | None:
        if valor > 0:
            self.saldo += valor
            return f"Deposito de R${valor:.2f} na conta do titular: {self.titular} realizado!\nSeu novo saldo é R${self.saldo:.2f}"
        if valor == 0:
            return f"Deposito insuficiente! O valor deve ser superior a zero."
        return f"'{valor}' invalido! Digite um valor valido!"

    def saque(self, valor: float) -> str | None:
        if valor < 0:
            return "Valor invalido! Aponte um valor superior a 0."
        if valor > self.saldo:
            return f"Saldo insuficiente para saque.\nSaldo atual R${self.saldo:.2f}."
        if valor <= self.saldo:
            self.saldo -= valor
            return f"Saque no valor de R${valor} realizado!\nSeu novo saldo é de R${self.saldo:.2f}."


operacao1 = ContaBancaria(titular="Giovane", saldo=1000)

print(operacao1.saque(500.00))
print(operacao1.deposito(100.00))

