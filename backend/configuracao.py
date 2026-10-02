import os

from dotenv import load_dotenv
from sqlalchemy import URL

load_dotenv()

CONFIGURACAO = {
    "url_do_banco": os.getenv("URL_DO_BANCO"),
}


def obter_configuracao():
    return CONFIGURACAO

ENDERECOS_FRONTEND = [
    endereco.strip()
    for endereco in os.getenv("ENDERECOS_FRONTEND", "").split(",")
    if endereco.strip()
]

url_do_banco = URL.create(
    "mysql+mysqlconnector",
    username=os.getenv("BANCO_USUARIO"),
    password=os.getenv("BANCO_SENHA"),
    host=os.getenv("BANCO_HOST"),
    port=os.getenv("BANCO_PORTA"),
    database=os.getenv("BANCO_NOME"),
)