from fastapi import APIRouter

from managers.company import CompanyManager

router = APIRouter(tags=["company"])


@router.get("/company")
async def company():
    return await CompanyManager().get_company()
