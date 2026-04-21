from fastapi import FastAPI
from starlette.responses import FileResponse

app = FastAPI()

@app.get("/foto")
def get_foto():
    return FileResponse("imagem/cafe.jpeg")

