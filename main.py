from fastapi import FastAPI
from chatgpt import router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
    'https://chatgpt-experience-fe-949479c40e6b.herokuapp.com',
    'http://localhost:3000',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"chatgpt-experience": "ready"}

app.include_router(router)
