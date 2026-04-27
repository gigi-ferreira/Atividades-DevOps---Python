from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "Olá mundo"}

@app.get("/soma/{a}/{b}")
def soma(a: int, b: int):
    return {"resultado": a + b}
