# arquivo: main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensagem": "Minha API "}

@app.get("/soma")
def somar(a: int, b: int):
    return {"resultado": a + b}
