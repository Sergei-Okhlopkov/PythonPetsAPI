import sqlalchemy as db
from pydantic import BaseModel
from typing import List
from __init__ import Base


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
    type = db.Column(db.String)
    created_at = db.Column(db.String, default="strftime('%Y-%m-%dT%H:%M:%S',  datetime('now', '3 hours'))")
