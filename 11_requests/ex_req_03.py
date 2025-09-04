"""Exercício 03.

Crie uma função chamada consultar_ultimos_artigos que realiza uma consulta à API v4
do Spaceflight News (spaceflightnewsapi.net) para obter os últimos artigos publicados.
A função deve imprimir os títulos dos 5 primeiros artigos retornados pela API.
Se ocorrer algum erro na consulta, a função deve imprimir uma mensagem informando a
falha na solicitação.
"""

from pathlib import Path

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag


def scrape_countries(url: str, headers: dict[str, str]):
    try:
        response = requests.get(url=url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"Erro HTTP ao acessar {url}: {e}")
        return []
    except requests.exceptions.Timeout:
        print("Tempo esgotado.")
        return []
    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro ao acessar {url}: {e}")
        return []
    soup = BeautifulSoup(markup=response.content, features="html.parser")
    return soup.find_all(name="div", class_="col-md-4 country")


def extract_country_data(country: Tag):
    try:
        name_tag = country.find(name="h3", class_="country-name")
        capital_tag = country.find(name="span", class_="country-capital")
        population_tag = country.find(name="span", class_="country-population")
        area_tag = country.find(name="span", class_="country-area")

        if (
            name_tag is None
            or capital_tag is None
            or population_tag is None
            or area_tag is None
        ):
            print(f"Elemento faltando no país: {country}")
            return None

        name = name_tag.get_text(strip=True)
        capital = capital_tag.get_text(strip=True)
        population = population_tag.get_text(strip=True)
        area = area_tag.get_text(strip=True)
    except AttributeError as e:
        print(f"Erro ao extrair os dados do país: {country}")
        return None
    return {"Nome": name, "Capital": capital, "População": population, "Área": area}


def save_to_file(data_list, file_path: Path):
    try:
        with file_path.open("w", encoding="utf8") as file:
            for data in data_list:
                file.write(f"Nome: {data["Nome"]}\n")
                file.write(f"Capital: {data["Capital"]}\n")
                file.write(f"População: {data["População"]}\n")
                file.write(f"Área: {data["Área"]}\n\n")
    except OSError as e:
        print(f"Ocorreu um erro ao salvar o arquivo: {e}")


url = "https://www.scrapethissite.com/pages/simple/"
headers = {"User-Agent": "Mozilla/5.0"}
output_file = Path("countries_data.txt")
all_country_data = []

countries = scrape_countries(url, headers)

for country in countries:
    data = extract_country_data(country)
    if data:
        print(data)
        all_country_data.append(data)
    if all_country_data:
        save_to_file(all_country_data, output_file)
    else:
        print("Nenhum dado foi extraído.")
