from fastapi import FastAPI
import uvicorn;

app = FastAPI()


@app.get("/")
async def root():
    return {"msg": "Hello World!!"}

@app.get("/pr")
async def pr():
    return {"msg":"Olá! Você está na minha aplicação de estudos Git e API"}

@app.get("/actions")
async def pr():
    return {"msg":"Testando o Actions"}

@app.get("/health")
async def health_check():
    if True: #apenas para fins de estudo health docker
        return {"status": "ok"}
    else:
        raise HTTPException(status_code=500, detail="Internal Server Error")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")
    