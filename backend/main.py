from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from configuracao import ENDERECOS_FRONTEND
from rotas import itens, pedidos, saude

app = FastAPI(title="Cardapio Digital")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ENDERECOS_FRONTEND,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(itens.router, prefix="/itens", tags=["Cardápio"])
app.include_router(pedidos.router, prefix="/pedidos", tags=["Pedidos"])
app.include_router(saude.router, prefix="", tags=["Saúde"])

