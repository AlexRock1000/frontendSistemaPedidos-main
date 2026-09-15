from http.client import HTTPException
from fastapi import FastAPI

app = FastAPI(title="Cardapio Digital")

cardapio = [
    {"id": 1, "nome": "Pizza Marguerita", "preco": 39.90, "categoria": "prato"},
    {"id": 2, "nome": "Suco de Laranja",  "preco": 12.50, "categoria": "bebida"},
]

@app.get("/itens")
def listar_itens(categoria: str | None = None):  # texto ou nada; padrão None
    if categoria is None:                         # não veio ?categoria= na URL
        return cardapio
    filtrados = []
    for item in cardapio:
        if item["categoria"] == categoria:
            filtrados.append(item)
    return filtrados

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/itens/{item_id}")
def obter_item(item_id: int):
    for item in cardapio:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item não encontrado")