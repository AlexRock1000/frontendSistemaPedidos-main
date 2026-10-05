from repositorios import tarefa as repositorio_tarefa


def listar():
    return repositorio_tarefa.listar()


def buscar_por_id(tarefa_id: int):
    return repositorio_tarefa.buscar_por_id(tarefa_id)
