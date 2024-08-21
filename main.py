from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"msg": "Hello World!"}

@app.get("/welcome")
async def welcome():
    return {"msg":"Olá! Você está na minha aplicação de estudos Git e API"}

