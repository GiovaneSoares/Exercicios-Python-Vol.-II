"""Exercício 05.
Você é responsável por desenvolver um sistema de gestão de estoque para uma loja.
Crie uma classe chamada Produto que represente um item em estoque.
Cada produto deve ter um nome, um preço e uma quantidade disponível em estoque.

    Adicione métodos à classe Produto para aumentar e diminuir a quantidade em estoque.
    Adicione um método para calcular o valor total do estoque de um produto
    (preço * quantidade).

Crie dois produtos diferentes e realize algumas operações para demonstrar o
funcionamento do sistema.
"""
# from decimal import Decimal


class Produto:
    def __init__(self, nome: str, preco: float, estoque: int) -> None:
        self.nome: str = nome
        self.preco: float = preco
        self.estoque: int = estoque

    def aumentar_estoque(self, quantidade: int) -> None:
        if self.estoque > 0:
            self.estoque += quantidade

    def diminuir_estoque(self, quantidade: int) -> None:
        if quantidade > 0:
            if quantidade > self.estoque:
                print("Quantidade indisponivel em estoque!")
            else:
                self.estoque -= quantidade

    def calcular_valor_total(self) -> float:
        return self.preco * self.estoque

    def descricao(self) -> str:
        return f"Nome: {self.nome}\nPreço: R$ {self.preco:.2f}\nQuantidade em estoque: {self.estoque}\nValor total em estoque R$ {self.calcular_valor_total():.2f}."


produto_1 = Produto(nome="Camiseta", preco=29.99, estoque=50)
produto_2 = Produto(nome="Boné", preco=50.50, estoque=5)

produto_1.aumentar_estoque(20)
produto_1.diminuir_estoque(5)
print(produto_1.descricao())
