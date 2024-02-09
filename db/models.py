from pydantic import BaseModel


class PetCreate(BaseModel):
    name: str
    age: int
    type: str

class Pet(PetCreate):
    id: int
    created_at: str