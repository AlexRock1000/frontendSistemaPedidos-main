from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from rotas import itens, pedidos

app = FastAPI(title="Cardapio Digital")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(itens.router, prefix="/itens", tags=["Cardápio"])
app.include_router(pedidos.router, prefix="/pedidos", tags=["Pedidos"])

@app.get("/health")
def health():
    return {"status": "ok"}

