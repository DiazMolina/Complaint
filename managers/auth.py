from datetime import datetime, timedelta
from typing import Optional

import jwt
from decouple import config
from fastapi import HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from starlette.requests import Request

from db import database
from models import RoleType, user


class AuthManager:
    @staticmethod
    def encode_token(user):
        try:
            payload = {
                "sub": user["id"],
                "exp": datetime.utcnow() + timedelta(minutes=129)
            }
            return jwt.encode(payload, config('SECRET_KEY'), algorithm='HS256')
        except Exception:
            raise HTTPException(status_code=500, detail="Can't generate a token.")


class CustomBearer(HTTPBearer):
    async def __call__(self, request: Request) -> Optional[HTTPAuthorizationCredentials]:
        res = await super().__call__(request)
        try:
            payload = jwt.decode(res.credentials, config('SECRET_KEY'), algorithms=['HS256'])
            user_data = await database.fetch_one(user.select().where(user.c.id == payload['sub']))
            request.state.user = user_data
            print(user_data)
            return payload
        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=401, detail="Signature expired. Please log in again."
            )
        except jwt.InvalidTokenError:
            raise HTTPException(
                status_code=401, detail="Invalid token. Please log in again."
            )


oauth2_scheme = CustomBearer()


def is_complainer(request: Request):
    print(request.state)
    if request.state.user["role"] != RoleType.complainer:
        raise HTTPException(status_code=403, detail="You are not a complainer")


def is_approver(request: Request):
    if request.state.user["role"] != RoleType.approver:
        raise HTTPException(status_code=403, detail="You are not an approver")


def is_admin(request: Request):
    if request.state.user["role"] != RoleType.admin:
        raise HTTPException(status_code=403, detail="You are not an admin")
