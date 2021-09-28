from fastapi import FastAPI
from pydantic import BaseModel

from typing import List, Dict


class Response(BaseModel):
    string: str


app = FastAPI()


@app.get("/", response_model=Response)
async def hello_world():
    return {"string": "hello world !"}
