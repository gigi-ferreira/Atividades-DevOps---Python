from fastapi import FastAPI
from starlette.responses import FileResponse
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def caminho_imagem(foto): return os.path.join(BASE_DIR, "..", "imagem", foto)

@app.get("/")
def inicio():
    return {"mensagem": "Informe: http://127.0.0.1:8000/gatinho/soninho para ver a café dormindo, ou informe http://127.0.0.1:8000/gatinho/gatao para ver o gatão acordado :D"}

@app.get("/gatinho/{humor}")
def gatinho(humor: str):
    if humor == "soninho":
        caminho = caminho_imagem("cafe.jpeg")
    else:
        caminho = caminho_imagem("gatao.jpeg")

    if not os.path.exists(caminho):
        return {"erro": "gatinho não encontrado"}

    return FileResponse(caminho)