from sqlalchemy import Column, Date, ForeignKey, Integer, String

from banco import Base


class Tarefa(Base):
    __tablename__ = "tarefas"

    id = Column(Integer, primary_key=True)
    titulo = Column(String(100), nullable=False)
    descricao = Column(String(500), nullable=False)
    prazo = Column(Date, nullable=False)
    situacao = Column(String(20), nullable=False)
    itens_feitos = Column(Integer, nullable=False)
    solicitante_id = Column(
        Integer,
        ForeignKey("solicitantes.id", name="fk_tarefas_solicitantes"),
        nullable=False,
    )
