from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from src.api.routes import users

'''Todas as função recebem app para poderem se incluidas ao app'''


def configure_rutes(app: FastAPI):
    '''def onde sera criada as rotas'''
    app.include_router(users.router)


def configure_db(app: FastAPI):
    '''Inicie seus modelos e banco de dados como:'''
    register_tortoise(
        app=app,
        config={
            'connections': {
                # 'default': 'postgres://postgres:qwerty123@localhost:5432/test'
                'default': 'sqlite://db.sqlite3'  # Usando SQLite como banco de dados
            },
            'apps': {
                'models': {
                    # Substitua pelo caminho dos seus modelos isso vai inica o tortoise
                    'models': [
                        'src.datalayer.models.user'
                    ],  
                    'default_connection': 'default',
                },
            },
            'use_tz': False,  # Configura se vai usar timezone ou não
            'timezone': 'UTC',  # Defina o timezone se `use_tz=True`
        },
        generate_schemas=True,  # Isso cria as tabelas automaticamente, se necessário, sempre que inicia
        add_exception_handlers=True,  # Adiciona manipuladores de exceção
    )



