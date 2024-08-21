from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
async def root():
    return {"msg": "Hello World!"}

