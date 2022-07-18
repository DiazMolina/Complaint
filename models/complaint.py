from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    Enum,
    Text,
    Float,
    DateTime,
    func,
    ForeignKey,
)

from db import metadata
from models.enums import State

complaint = Table(
    "complaints",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(125), nullable=False),
    Column("description", Text, nullable=False),
    Column("photo_url", String(200), nullable=False),
    Column("amount", Float, nullable=False),
    Column("created_at", DateTime, server_default=func.now()),
    Column("status", Enum(State), nullable=False, server_default=State.pending.name),
    Column("complainer_id", ForeignKey("users.id"), nullable=False),
)
