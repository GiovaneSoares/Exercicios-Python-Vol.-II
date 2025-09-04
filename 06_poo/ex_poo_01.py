"""Exercício 01.
Crie uma classe chamada Carro que represente um veículo.
Esta classe deve ter dois atributos: marca e modelo.
Além disso, adicione um método chamado descricao() que retorna uma string formatada
contendo a marca e o modelo do carro.
Após definir a classe, crie uma instância dessa classe e chame o método descricao()
para exibir as informações do carro.
    Exemplo de saída esperada:
        Carro: Toyota Corolla
"""


class Carro:
    def __init__(self, marca: str, modelo: str) -> None:
        self.marca: str = marca
        self.modelo: str = modelo

    def descricao(self) -> str:
        return f"Carro: {self.marca} {self.modelo}"


carro = Carro(marca="Toytota", modelo="Corolla")

print(carro.descricao())
