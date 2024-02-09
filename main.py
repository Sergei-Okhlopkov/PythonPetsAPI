import sqlite3

from fastapi import FastAPI

from db import create_db
from db.models import Pet, PetCreate

create_db()

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
    return {**pet.dict()}


@app.get("/pets/{limit}")
def get_pets_with_limit(limit):
    conn = sqlite3.connect('pets.db')
    c = conn.cursor()
    c.execute(f"SELECT * FROM pets LIMIT {limit}")
    pets = [{"id": row[0], "name": row[1], "age": row[2], "type": row[3]} for row in c.fetchall()]
    conn.close()
    return pets


@app.get("/pets")
def get_pets():
    conn = sqlite3.connect('pets.db')
    c = conn.cursor()
    c.execute("SELECT * FROM pets LIMIT 20")
    pets = [{"id": row[0], "name": row[1], "age": row[2], "breed": row[3]} for row in c.fetchall()]
    conn.close()
    return pets


@app.delete("/pets")
def delete_pets():
    return "Удалили питомцев"
