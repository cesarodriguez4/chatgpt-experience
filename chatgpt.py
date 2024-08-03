from fastapi import APIRouter
from openai import OpenAI

router = APIRouter(
    prefix="/chatgpt",
    tags=["chatgpt"],
)

client = OpenAI()

@router.post("/query")
async def chatgpt_query(query: dict):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": query.get("query")},
        ],
    )
    return {"response": completion.choices[0].message.content}