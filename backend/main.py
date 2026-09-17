from fastapi import FastAPI
from rotas import itens, pedidos
from rotas import itens, pedidos

app = FastAPI(title="Cardapio Digital")

app.include_router(itens.router, prefix="/itens", tags=["Cardápio"])
app.include_router(pedidos.router, prefix="/pedidos", tags=["Pedidos"])

@app.get("/health")
def health():
    return {"status": "ok"}

