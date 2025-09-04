from typing import TYPE_CHECKING

import requests

if TYPE_CHECKING:
    from requests import Response


def consultar_cep(cep: str) -> None:
    url: str = f"https://viacep.com.br/ws/{cep}/json/"

    resposta: Response = requests.get(url=url, timeout=3)
    resposta.raise_for_status()

    if resposta.status_code == 400:
        print("Erro: CEP invalido. verifique o formato do CEP fornecido.")
        return

    data: dict[str, str] = resposta.json()

    if "erro" in data:
        print("CEP não encontrado.")
    else:
        print("\nCEP encontrado!")
        print(f"CEP: {data['uf']}")
        print(f"Logradouro: {data['logradouro']}")
        print(f"Complemento: {data['complemento']}")
        print(f"Bairro: {data['bairro']}")
        print(f"Cidade: {data['localidade']}")
        print(f"Estado: {data['estado']}")


cep: str = input("Digite o CEP para consulta: ")
try:
    consultar_cep(cep=cep)
except requests.exceptions.HTTPError as e:
    print(f"Erro HTTP: {e}")
except requests.exceptions.ConnectTimeout:
    print("Erro: Tempo esgotado.")
except requests.exceptions.RequestException as e:
    print(f"Erro: {e}")

