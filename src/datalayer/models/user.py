import secrets
from tortoise.models import Model
from tortoise import fields

# gerado de token do usuario
def generete_token():
    return secrets.token_urlsafe(20)

class UserModel(Model):
    # quais dados queremos pegar do user, e qauntidade de caractere
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=120)
    email = fields.CharField(max_length=120, unique=True)
    password = fields.TextField() # user pode coloca a senha que quise
    token = fields.TextField(default=generete_token) 

