import databases
from decouple import config
from sqlalchemy import MetaData

DATABASE_URL = f'postgresql://{config("DB_USER")}:{config("DB_PASSWORD")}@localhost:5432/complaint'
database = databases.Database(DATABASE_URL)
metadata = MetaData()
