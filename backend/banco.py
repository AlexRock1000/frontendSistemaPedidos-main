from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from configuracao import obter_configuracao

configuracao = obter_configuracao()
engine = create_engine(configuracao["url_do_banco"])  # o motor
Sessao = sessionmaker(bind=engine)   # cada Sessao() abre uma conversa


class Base(DeclarativeBase):         # a classe mãe dos modelos
    pass                            # o corpo fica vazio de propósito
