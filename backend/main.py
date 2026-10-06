from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from configuracao import ENDERECOS_FRONTEND
from rotas import itens, pedidos, saude, tarefas
from servicos.excecoes import ErroDeRegra

app = FastAPI(title="Cardapio Digital")


@app.exception_handler(ErroDeRegra)
def tratar_erro_de_regra(_request: Request, exc: ErroDeRegra):
    _ = _request
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": str(exc)},
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=ENDERECOS_FRONTEND,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(itens.router, prefix="/itens", tags=["Cardápio"])
app.include_router(pedidos.router, prefix="/pedidos", tags=["Pedidos"])
app.include_router(tarefas.router, prefix="/tarefas", tags=["Tarefas"])
app.include_router(saude.router, prefix="", tags=["Saúde"])

