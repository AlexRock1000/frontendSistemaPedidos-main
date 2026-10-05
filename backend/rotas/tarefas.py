from fastapi import APIRouter, HTTPException, status

from esquemas.tarefa import TarefaEntrada, TarefaSaida
from servicos import tarefa as servico_tarefa

router = APIRouter()


@router.get("/", response_model=list[TarefaSaida])
def listar():
    return servico_tarefa.listar()


@router.post("/", response_model=TarefaSaida, status_code=status.HTTP_201_CREATED)
def salvar(dados: TarefaEntrada):
    return servico_tarefa.salvar(dados.model_dump())


@router.get("/{tarefa_id}", response_model=TarefaSaida)
def buscar_por_id(tarefa_id: int):
    tarefa = servico_tarefa.buscar_por_id(tarefa_id)
    if tarefa is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tarefa
