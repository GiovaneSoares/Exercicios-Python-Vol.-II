"""Exercício 07.
Você está desenvolvendo um sistema para um hotel que permite aos clientes fazerem
reservas de quartos.
Crie uma classe chamada Quarto que represente um quarto do hotel.
Cada quarto deve ter um número, um tipo (por exemplo, simples, duplo, suíte), e um
status que indica se o quarto está disponível para reserva ou não.

    Adicione métodos à classe Quarto para reservar e liberar o quarto.
    Adicione um método para verificar se o quarto está disponível para reserva.

Crie alguns quartos diferentes e realize operações de reserva e liberação para testar a
funcionalidade.
"""

class Quarto:
    def __init__(self, numero: int, tipo: str) -> None:
        self.numero: int = numero
        self.tipo: str = tipo
        self.disponivel: bool = True

    def reservar_quarto(self) -> str:
        if self.disponivel:
            self.disponivel = False
            return f"Reserva do {self.numero} realizada com sucesso!"
        return f"O quarto de número {self.numero} não está disponivel para reserva."

    def liberar_quarto(self) -> str:
        if not self.disponivel:
            self.disponivel = True
            return f"Quarto de número {self.numero} liberado."
        return f"Quarto {self.numero} já está disponivel."

    def verificar_disponibilidade(self) -> str:
        if self.disponivel:
            return f"O quarto {self.numero} está a disposição!"
        return f"Quarto {self.numero} não está disponivel."


quarto_101 = Quarto(numero=101, tipo="Duplo")

print(quarto_101.reservar_quarto(), "\n")
print(quarto_101.verificar_disponibilidade(), "\n")
print(quarto_101.liberar_quarto(), "\n")
