from fastapi import FastAPI
from chatgpt import router
app = FastAPI()

@app.get("/")
async def read_root():
    return {"chatgpt-experience": "ready"}

app.include_router(router)
