from sqlalchemy import Column, Integer, String, Date
from banco import Base

class Tarefa(Base):                             # herda da Base: vira tabela
    __tablename__ = "tarefas"                    # o nome da tabela no MySQL
    id = Column(Integer, primary_key=True)       # INT PRIMARY KEY AUTO_INCREMENT
    titulo = Column(String(100), nullable=False) # VARCHAR(100) NOT NULL
    descricao = Column(String(500), nullable=False)
    prazo = Column(Date, nullable=False)         # DATE NOT NULL
    situacao = Column(String(20), nullable=False)
    itens_feitos = Column(Integer, nullable=False)
    solicitante_id = Column(Integer, nullable=False)