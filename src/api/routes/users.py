from fastapi import APIRouter
from src.api.dtos.users import UserRegistation, Userlogin
from src.datalayer.models.user import UserModel
from src.api.exception.user import login_wrong, email_exist_func


''' Router: receber uma rota padrão antes de mostra a proxima rota, ex
    /user/ <-- rota inicial
    /user/teste <-- rota teste '''
router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not fold"}} #<-- MSG que aparecera caso não emcomtre a pagina
)




# Criando rotas de registro
@router.post("/register")
async def register(body: UserRegistation):

    # verificando se email ja esta cadastrado
    email_exist = await UserModel.filter(email = body.email)
    if email_exist:
        raise email_exist_func()
    # caso não
    else:

        user = await UserModel.create(
            name = body.name,
            email = body.email,
            password = body.password
        )

        return {'Created': user}



@router.post("/login")
async def login(body: Userlogin):
    user = None
    try:
        # Buscando infor no banco de dados
        user = await UserModel.get(email = body.email)
        print('date', user)
    except Exception as e:
        print(e)
        return login_wrong() # mensagem dee erro
    
    if user.password != body.password:
        return login_wrong()  # mensagem dee erro

    return user


# Rota par visualiza os usuarios
@router.get("/users")
async def view_user():
    users = await UserModel.all()

    return {'users': users}