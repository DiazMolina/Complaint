from sqlalchemy import Table, Integer, Column, String

from db import metadata

company = Table(
    "company",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(255)),
)
