from banco import Base, engine
from modelos.tarefa import Tarefa # o import apresenta o modelo para a Base


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print(f"Tabelas: {list(Base.metadata.tables.keys())}")

Base.metadata.create_all(engine)    # cria só a tabela que ainda não existe
print("Tabelas:", list(Base.metadata.tables))
