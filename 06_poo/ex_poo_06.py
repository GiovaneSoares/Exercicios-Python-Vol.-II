"""Exercício 06.
Em uma escola, você precisa gerenciar informações sobre os alunos.
Crie uma classe chamada Aluno que represente um estudante.
Cada aluno deve ter um nome, uma idade e uma lista de disciplinas em que está
matriculado.

    Adicione métodos à classe Aluno para adicionar e remover disciplinas da lista.
    Adicione um método para verificar se um aluno está matriculado em uma determinada
    disciplina.

Crie alguns alunos e realize operações de matrícula e remoção de disciplinas para
testar a funcionalidade.
"""

class Aluno:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome: str = nome
        self.idade: int = idade
        self.disciplinas: list[str] = []

    def adicionar_disciplina(self, disciplina: str) -> str:
        if disciplina not in self.disciplinas:
            self.disciplinas.append(disciplina)
            return f"Disciplina {disciplina} adicionada para o aluno {self.nome}."
        msg_erro = f"O aluno {self.nome} já esta cadastrado na {disciplina}."
        raise ValueError(msg_erro)

    def remover_disciplina(self, disciplina: str) -> str:
        if disciplina in self.disciplinas:
            self.disciplinas.remove(disciplina)
            return f"Disciplina {disciplina} removida com sucesso."
        msg_erro: str = (
            f"O aluno {self.nome} não está metriculado na disciplina {disciplina}."
        )
        raise ValueError(msg_erro)

    def verificar_disciplina(self, disciplina: str) -> str:
        if disciplina in self.disciplinas:
            return f"O aluno {self.nome} está matriculado na disciplina {disciplina}."
        return f"O aluno {self.nome} não está matriculado na disciplina {disciplina}."


aluno_1 = Aluno(nome="Giovane", idade=24)

print(aluno_1.adicionar_disciplina(disciplina="Matemática"))
print(aluno_1.remover_disciplina(disciplina="Matemática"))

# try:
#     print(aluno_1.adicionar_disciplina(disciplina="Matemática"))
# except ValueError as e:
#     print(e)
