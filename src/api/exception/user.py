from fastapi import  HTTPException


def login_wrong():
    raise HTTPException(status_code=404, detail='Erro: E-mail/senha invalidos')


def email_exist_func():
    raise HTTPException(status_code=400, detail='Email já cadastrado')
   