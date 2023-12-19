from fastapi import FastAPI, Request

from models import Pessoa

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/pessoas")
async def create_person(pessoa: Pessoa):
    return pessoa
