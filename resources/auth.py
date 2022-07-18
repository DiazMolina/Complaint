from fastapi import APIRouter

from managers.user import UserManager
from schemas.request.user import UserRegisterIn, UserLoginIn

router = APIRouter(tags=["Auth"])


@router.post('/register', status_code=201)
async def register(user_data: UserRegisterIn):
    token = await UserManager.register(user_data.dict())
    return {'token': token}


@router.post('/login', status_code=200)
async def login(user_data: UserLoginIn):
    token = await UserManager.login(user_data.dict())
    return {'token': token}

# @router.post('/log')
# async def log(user_data: UserLoginIn):
#     user_do = await database.fetch_one(user.select().where(user.c.email == user_data.email))
#     if not user_do:
#         raise HTTPException(status_code=400, detail="Wrong email or password")
#     return AuthManager.encode_token(user_do)
