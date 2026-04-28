from fastapi import FastAPI, HTTPException
from starlette.responses import FileResponse
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def caminho_imagem(foto): return os.path.join(BASE_DIR, "..", "imagem", foto)

@app.get("/")
def inicio():
    return {"mensagem": "Informe: http://127.0.0.1:8000/gatinho/cafe para ver a café dormindo, informe http://127.0.0.1:8000/gatinho/gatao para ver o gatão acordado :D ou  informe http://127.0.0.1:8000/fome/{nivel da fome} para verificar o nível de fome do gatinho."}

@app.get("/gatinho/{nome}")
def gatinho(nome: str):
    if nome == "cafe":
        caminho = caminho_imagem("cafe.jpeg")
    else:
        caminho = caminho_imagem("gatao.jpeg")

    if not os.path.exists(caminho):
        return {"erro": "gatinho não encontrado"}

    return FileResponse(caminho)

@app.get("/fome/{nivel}")
def verificar_fome(nivel: int):
    if nivel < 0 or nivel > 10:
        raise HTTPException(status_code=400, detail="O nivel de fome deve ser entre 0 e 10")
    if nivel >= 7:
        return {"status": "O gatinho está com muita fome, alimente o gatinho :("}
    elif nivel >= 4:
        return {"status": "O gatinho está ficando com fome :0"}
    else:
        return {"status": "O gatinho não está com fome :D"}
