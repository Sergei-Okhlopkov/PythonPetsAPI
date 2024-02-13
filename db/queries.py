from sqlalchemy import delete
from db import SessionLocal
from db.pet_model import Pet, PetCreate
from enums.pet_type import str_to_enum, PetType


def create_pet_query(pet_create: PetCreate):
    try:
        pet_type = str_to_enum(pet_create.type)
        session = SessionLocal()
        pet = Pet(name=pet_create.name, age=pet_create.age, type=pet_type.value)
        session.add(pet)
        session.flush()

        result = {
            "id": pet.id,
            "name": pet.name,
            "age": pet.age,
            "type": pet_type.name,
            "created_at": pet.created_at
        }

        session.commit()
        session.close()

        return result
    except Exception as ex:
        return {"error": str(ex)}


def get_pets_query(limit: int = 20):
    session = SessionLocal()
    pets = session.query(Pet).limit(limit).all()
    session.close()
    items = [{"id": pet.id,
              "name": pet.name,
              "age": pet.age,
              "type": PetType(pet.type).name,
              "created_at": pet.created_at} for pet in pets]

    result = {
        "count": len(items),
        "items": items
    }

    return result


def delete_pets_query(ids):
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
