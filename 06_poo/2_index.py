class Pessoa:
    def __init__(self, nome, idade: int) -> None:
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        return f"Olá meu nome é {self.nome}! Tenho {self.idade} anos."
    
    def verificar_idade(self):
        if self.idade < 18:
            return f"Menor de idade."
        elif self.idade >= 18:
            return f"Maior de idade."
        
juninho = Pessoa("Junior", 25)
print(juninho.apresentar())
print(juninho.verificar_idade())