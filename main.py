from fastapi import FastAPI
import uvicorn;

app = FastAPI()


@app.get("/")
async def root():
    return {"msg": "Hello World!!"}

@app.get("/welcome")
async def welcome():
    return {"msg":"Olá! Você está na minha aplicação de estudos Git e API"}

@app.get("/pr")
async def pr():
    return {"msg":"Olá! Você está na minha aplicação de estudos Git e API"}

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info", reload=True)