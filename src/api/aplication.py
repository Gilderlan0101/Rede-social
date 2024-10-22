from fastapi import FastAPI
from src.api.configuracao import configure_db, configure_rutes

''' Iniciando app '''
def creat_app():
    # iniciando app
    app = FastAPI()

    configure_db(app)
    configure_rutes(app)

    return app

# Executano a função que ligar nosso servido
app = creat_app()

