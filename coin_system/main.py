from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"hello": "coin_system"}