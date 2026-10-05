from fastapi import APIRouter, status

from esquemas.tarefa import TarefaEntrada, TarefaSaida
from servicos import tarefa as servico_tarefa

router = APIRouter()


@router.get("/", response_model=list[TarefaSaida])
def listar(situacao: str | None = None):
    return servico_tarefa.listar(situacao)


@router.post("/", response_model=TarefaSaida, status_code=status.HTTP_201_CREATED)
def salvar(dados: TarefaEntrada):
    return servico_tarefa.salvar(dados.model_dump())


@router.get("/{tarefa_id}", response_model=TarefaSaida)
def buscar_por_id(tarefa_id: int):
    return servico_tarefa.buscar_por_id(tarefa_id)
