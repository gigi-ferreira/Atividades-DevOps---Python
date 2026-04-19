from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"giselinha"}
@app.get("/teste2")
async def funcaoteste():
    return {"do balacobaco":"dyva"}
print("Teste2")