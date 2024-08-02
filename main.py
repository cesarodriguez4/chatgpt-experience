from typing import Union
from openai import OpenAI

from fastapi import FastAPI

app = FastAPI()
client = OpenAI()

@app.get("/")
async def read_root():
    return {"chatgpt-experience": "ready"}

@app.post("/chatgpt-query")
async def chatgpt_query(query: dict):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": query.get("query")},
        ],
    )
    return {"response": completion.choices[0].message.content}
