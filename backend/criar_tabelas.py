from banco import Base, engine
from modelos.tarefa import Tarefa

Base.metadata.create_all(engine)
print("Tabelas:", list(Base.metadata.tables))
