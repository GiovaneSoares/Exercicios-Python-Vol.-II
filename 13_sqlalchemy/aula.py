from sqlalchemy import Engine, create_engine, text

engine: Engine = create_engine(url="sqlite:///aula_13.db")

with engine.connect() as connection:
    connection.execute(statement=text(text="DROP TABLE IF EXISTS usuario"))

    connection.execute(
        statement=text(
            text="CREATE TABLE usuario (id_ INTEGER PRIMARY KEY,"
            "Nome TEXT NOT NULL,"
            "Sobrenome TEXT NOT NULL)",
        ),
    )
