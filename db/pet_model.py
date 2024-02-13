from datetime import datetime
import sqlalchemy as db
from pydantic import BaseModel
from typing import List

from db import Base


class PetCreate(BaseModel):
    name: str
    age: int
    type: str


class DeletePets(BaseModel):
    ids: List[int]


class Pet(Base):
    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    type = db.Column(db.Integer)
    created_at = db.Column(db.String, default=lambda: datetime.now().strftime('%Y-%m-%dT%H:%M:%S'))
