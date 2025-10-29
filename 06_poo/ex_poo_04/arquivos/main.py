from pathlib import Path

BASE_DIR = Path(__file__).parent / "arquivos"
ARQ_ENTRADA = "usuarios.txt"
ARQ_SAIDA = "relatorio.txt"

try:
    with Path(BASE_DIR / ARQ_ENTRADA).open(encoding="utf-8") as entrada:
        usuarios: list[usuario] = []
        total_bytes: int = 0
        linhas:list[str] = entrada.readlines()
        print(linhas)
        for linha in linhas:
            nome, tamanho_bytes = linha.split()
            print(nome, tamanho_bytes)

except Exception:
    pass