from fastapi import FastAPI
from db.pet_model import PetCreate, DeletePets
from db.queries import get_pets_query, delete_pets_query, create_pet_query

app = FastAPI(title="PetsAPI")


@app.post("/pets")
def create_pet(pet_create: PetCreate):
    return create_pet_query(pet_create)


@app.get("/pets/{limit}")
def get_pets_limit(limit):
    return get_pets_query(limit)


@app.get("/pets")
def get_pets():
    return get_pets_query()


@app.delete("/pets")
def delete_pets(pets: DeletePets):
    return delete_pets_query(pets.ids)
