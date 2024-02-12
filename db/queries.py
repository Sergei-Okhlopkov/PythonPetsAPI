from sqlalchemy import delete
from db import SessionLocal
from db.pet_model import Pet, PetCreate


def create_pet(pet_create: PetCreate):
    session = SessionLocal()
    pet = Pet(name=pet_create.name, age=pet_create.age, type=pet_create.type)
    session.add(pet)
    session.commit()
    session.close()

    return pet


def get_pets(limit: int = 20):
    session = SessionLocal()
    pets = session.query(Pet).limit(limit)
    session.close()

    return pets

def delete_pets(ids):
    success_count = 0
    errors = []

    session = SessionLocal()

    for pet_id in ids:
        try:
            delete_stmt = delete(Pet).where(Pet.id == pet_id)
            query = session.execute(delete_stmt)
            if query.rowcount > 0:
                success_count += 1
            else:
                errors.append({"id": pet_id, "error": "Pet with the matching ID was not found."})
        except Exception as ex:
            errors.append({"id": pet_id, "error": str(ex)})

    session.commit()
    session.close()

    result = {
        "deleted": success_count,
        "errors": errors
    }
    return result




