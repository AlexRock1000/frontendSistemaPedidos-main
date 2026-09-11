from fastapi import FastAPI

app = FastAPI(title="Cardapio Digital")

@app.get("/health")
def health():
    return {"status": "ok"}