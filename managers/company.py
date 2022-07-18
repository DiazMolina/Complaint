from db import database
from models.company import company


class CompanyManager:
    @staticmethod
    async def get_company():
        return await database.fetch_all(company.select())
