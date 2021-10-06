import os
import typing

from fastapi import FastAPI
from pydantic import BaseModel

from sqlalchemy import create_engine, Integer, Text, Table, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

Base = declarative_base()


engine = create_engine(f"postgresql+psycopg2://"
                       f"{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}"
                       f"@"
                       f"postgres:{os.getenv('POSTGRES_PORT')}"
                       f"/{os.getenv('POSTGRES_USER')}")


s = Session(bind=engine)


class CryptoCurrency(Table):
    __tablename__ = "CryptoCurrencies"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(Text, unique=True)

    def __str__(self):
        return f"CryptoCurrency id: {self.id}  name: {self.name}"


Base.metadata.create_all(bind=engine)


# some rest shit
class Request(BaseModel):
    currency_name: str


class Response(BaseModel):
    currencies: typing.List[typing.Union[int, str]]


app = FastAPI()


@app.get("/create/", response_model=Response)
async def create(request: Request):
    new_crypto = CryptoCurrency(name=request.currency_name)
    s.add(new_crypto)
    s.commit()
    return {"string": "successfully created"}


@app.get("/all/", response_model=Response)
async def all_items():
    result = [[item.id, item.name] for item in s.query(CryptoCurrency).all()]
    return {"currencies": "hello world !"}
