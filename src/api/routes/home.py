from fastapi import APIRouter, Depends
from typing_extensions import Annotated
from src.api.authentication.auth import verify_token
from src.datalayer.models.user import UserModel

# Definição da rota padrão
router = APIRouter(
    prefix="/me",
    tags=["me"],
    responses={404: {"description": "Not found"}}
)

@router.post("/")
async def my_informations(corrent_user: Annotated[UserModel, Depends(verify_token)]):
    print("corrent_user", corrent_user)
    return corrent_user
