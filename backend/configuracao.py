import os

from dotenv import load_dotenv

load_dotenv()

ENDERECOS_FRONTEND = [
    endereco.strip()
    for endereco in os.getenv("ENDERECOS_FRONTEND", "").split(",")
    if endereco.strip()
]