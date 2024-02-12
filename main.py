import sqlite3

from fastapi import FastAPI
from db.pet_model import Pet, PetCreate, DeletePets

app = FastAPI(title="PetsAPI")


@app.post("/pets")
def create_pet(pet_create: PetCreate):
    conn = sqlite3.connect('pets.db')
    c = conn.cursor()
    c.execute("INSERT INTO pets (name, age, type) VALUES (?, ?, ?)",
              (pet_create.name, pet_create.age, pet_create.type))
    conn.commit()
    row = c.execute(f"SELECT * FROM pets WHERE id={c.lastrowid}").fetchone()
    pet = Pet(id=row[0],
              name=row[1],
              age=row[2],
              type=row[3],
              created_at=row[4])

    conn.close()
    result = {
        "id": pet.id,
        "name": pet.name,
        "age": pet.age,
        "type": pet.type,
        "created_at": pet.created_at
    }
    return result


@app.get("/pets/{limit}")
def get_pets_with_limit(limit):
    conn = sqlite3.connect('pets.db')
    c = conn.cursor()
    c.execute(f"SELECT * FROM pets LIMIT {limit}")
    query_data = c.fetchall()
    items = [{"id": row[0], "name": row[1], "age": row[2], "type": row[3], "created_at": row[4]} for row in query_data]
    conn.close()

    result = {
        "count": len(query_data),
        "items": items
    }

    return result


@app.get("/pets")
def get_pets():
    conn = sqlite3.connect('pets.db')
    c = conn.cursor()
    c.execute("SELECT * FROM pets LIMIT 20")
    query_data = c.fetchall()
    items = [{"id": row[0], "name": row[1], "age": row[2], "type": row[3], "created_at": row[4]} for row in query_data]
    conn.close()
    result = {
        "count": len(query_data),
        "items": items
    }
    return result


@app.delete("/pets")
def delete_pets(pets: DeletePets):
    success_count = 0
    errors = []

    conn = sqlite3.connect('pets.db')
    c = conn.cursor()
    for pet_id in pets.ids:
        try:
            query = f"DELETE FROM pets WHERE id={pet_id}"
            c.execute(query)
            if c.rowcount > 0:
                success_count += 1
            else:
                errors.append({"id": pet_id, "error": "Pet with the matching ID was not found."})
        except Exception as ex:
            errors.append({"id": pet_id, "error": str(ex)})

    conn.commit()
    conn.close()

    result = {
        "deleted": success_count,
        "errors": errors
    }
    return result

