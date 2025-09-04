class Carro:
    def __init__(self, modelo: str, cor: str, ano: int) -> None:
        self.modelo: str = modelo
        self.cor: str = cor
        self.ano: int = ano
        self.ligado: bool = False

    def ligar(self) -> None:
        if not self.ligado:
            print(f"O modelo {self.modelo} de cor {self.cor}, foi ligado.")
            self.ligado = True
        else:
            print(f"O modelo {self.modelo} já esta ligado!")

    def desligar(self) -> None:
        if self.ligado:
            print(f"O {self.modelo}, foi desligado!")
            self.ligado = False
        else:
            print(f"{self.modelo} já está desligado.")


fiat_uno = Carro(modelo="fiat uno", cor="Verde", ano=2011)

fiat_uno.ligar()
fiat_uno.desligar()
