from pydantic import BaseModel

'''Arquivo resoponsavel dos users '''
class UserRegistation(BaseModel):
    name: str
    email: str
    password: str


class Userlogin(BaseModel):
    email: str
    password: str 