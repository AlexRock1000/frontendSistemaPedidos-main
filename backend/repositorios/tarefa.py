from sqlalchemy import select

from banco import Sessao
from modelos.tarefa import Tarefa


def listar():
    sessao = Sessao()
    try:
        return sessao.scalars(select(Tarefa)).all()
    finally:
        sessao.close()


def buscar_por_id(tarefa_id: int):
    sessao = Sessao()
    try:
        return sessao.get(Tarefa, tarefa_id)
    finally:
        sessao.close()
