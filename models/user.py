from sqlalchemy import Table, Column, Integer, String, Enum

from db import metadata
from models.enums import RoleType

user = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String(125), unique=True),
    Column("password", String(255)),
    Column("first_name", String(125)),
    Column("last_name", String(125)),
    Column("phone", String(20)),
    Column(
        "role", Enum(RoleType), nullable=False, server_default=RoleType.complainer.name
    ),
    Column("iban", String(125)),
)
