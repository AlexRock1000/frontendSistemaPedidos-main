from repositorios import tarefa as repositorio_tarefa


def listar(situacao: str | None = None):
    tarefas = repositorio_tarefa.listar()
    if situacao is None:
        return tarefas
    return [t for t in tarefas if t.situacao == situacao]


def buscar_por_id(tarefa_id: int):
    return repositorio_tarefa.buscar_por_id(tarefa_id)


def salvar(dados: dict):
    return repositorio_tarefa.salvar(dados)
