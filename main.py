from fastapi import FastAPI
from pydantic import BaseModel


class Response(BaseModel):
    string: str


app = FastAPI()


@app.get("/", response_model=Response)
async def hello_world():
    return {"string": "hello world !"}
