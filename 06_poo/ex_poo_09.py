"""Exercício 09.

Desenvolva um sistema bancário simplificado com Python.
Crie uma classe ContaBancaria que represente uma conta bancária genérica, incluindo
funcionalidades básicas como depósito, saque, consulta de saldo e troca de titular.
Em seguida, implemente uma classe derivada chamada ContaCorrente que herda da classe
base ContaBancaria.
Na classe ContaCorrente, substitua o método sacar para considerar um limite de saque
além do saldo disponível na conta.
Isso permite que os clientes tenham acesso a um valor adicional para saques, além do
saldo atual em suas contas correntes.
"""
class ContaBancaria:
        def __init__(self, nome: str = "Giovane", saldo: float = 100) -> None:
                self.nome = nome
                self.saldo = saldo
        
        def deposito(self, valor: float):
                if valor > 0:
                        self.saldo += valor
                        print(f"Deposito R${valor} realizado.\nNovo saldo R${self.saldo}. ")
                elif valor <= 0:
                        print("O valor do deposito deve ser superior a zero!")
        
        def saque(self, valor: float):
                if valor > 0:
                    if valor <= self.saldo:
                           self.saldo -= valor
                           print(f"Saque R${valor:.2f} realizado.")
                           print(f"Seu novo saldo é R${self.saldo:.2f}.")
                    else:
                        print("Operação falhou! Saldo insuficiente.")
                else:
                        print("O valor do saque deve ser superior a zero!")

        def consultarSaldo(self):
                print(f"Seu saldo é R${self.saldo:.2f}.")
        
        def trocarTitular(self, novo_titular: str):
                if novo_titular != self.nome:
                       self.nome = novo_titular
                       print(f"Troca de titular realizada.")
                       print(f"Seja bem vindo! {self.nome}!")
                
                else:
                       print("Esse titular já esta cadastrado.")

class ContaCorrente(ContaBancaria):
       def __init__(self, nome: str = "Giovane", saldo: float = 0, limite_extra: float = 0) -> None:
              ContaBancaria.__init__(self)
              self.limite_extra: float = limite_extra
        
        def sacar(self, valor: float):
              pass
       
        def consultarsaldo(self) -> str:
              return f"\nTitular: {self.nome}\nSaldo: {self.saldo:.2f}\nLimite extra: R${self.limite_extra}"
              
giovane = ContaBancaria("Giovane", 200)
giovane.trocarTitular("Giovane")