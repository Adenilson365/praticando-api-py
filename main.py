from fastapi import FastAPI
import uvicorn;

app = FastAPI()


@app.get("/")
async def root():
    return {"msg": "Hello World!!"}

@app.get("/pr")
async def pr():
    return {"msg":"Olá! Você está na minha aplicação de estudos Git e API"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")
    