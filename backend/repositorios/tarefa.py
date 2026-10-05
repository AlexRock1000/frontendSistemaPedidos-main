from sqlalchemy import select

from banco import Sessao
from modelos.tarefa import Tarefa


def listar():
    sessao = Sessao()
    tarefas = sessao.scalars(select(Tarefa)).all()
    sessao.close()
    return tarefas


def buscar_por_id(tarefa_id: int):
    sessao = Sessao()
    try:
        return sessao.get(Tarefa, tarefa_id)
    finally:
        sessao.close()


def salvar(dados: dict):
    sessao = Sessao()
    try:
        tarefa = Tarefa(**dados)
        sessao.add(tarefa)
        sessao.commit()
        sessao.refresh(tarefa)
        return tarefa
    finally:
        sessao.close()
