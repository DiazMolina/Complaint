from fastapi import APIRouter

from resources import auth, complaint, company, user

api_router = APIRouter()
api_router.include_router(auth.router)
api_router.include_router(complaint.router)
api_router.include_router(company.router)
api_router.include_router(user.router)
