from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"giselinha"}
@app.get("/teste1")
async def funcaoteste():
    return {"teste":"dyva"}