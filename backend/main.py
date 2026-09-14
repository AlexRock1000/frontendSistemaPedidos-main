from fastapi import FastAPI

app = FastAPI(title="Cardapio Digital")

cardapio = [
    {"id": 1, "nome": "Pizza Marguerita", "preco": 39.90, "categoria": "prato"},
    {"id": 2, "nome": "Suco de Laranja",  "preco": 12.50, "categoria": "bebida"},
]

@app.get("/itens")
def listar_itens():
    return cardapio

@app.get("/health")
def health():
    return {"status": "ok"}