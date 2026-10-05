from fastapi import APIRouter, HTTPException

from esquemas.tarefa import TarefaSaida
from servicos import tarefa as servico_tarefa

router = APIRouter()


@router.get("/", response_model=list[TarefaSaida])
def listar():
    return servico_tarefa.listar()


@router.get("/{tarefa_id}", response_model=TarefaSaida)
def buscar_por_id(tarefa_id: int):
    tarefa = servico_tarefa.buscar_por_id(tarefa_id)
    if tarefa is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tarefa
