from fastapi import FastAPI
import pandas as pd
from typing import Union

# uvicorn main:app --reload

# http://127.0.0.1:8000
# http://127.0.0.1:8000/docs -  AREA Swagger UI - documentação


app = FastAPI()

@app.get("/home")
def hello_root():
    return {"message": "Hello World"}

# http://127.0.0.1:8000/items/27?nome=Bruno

@app.get("/items/{item_id}")
def read_item(item_id: int, nome: Union[str, None] = None):
    return {"item_id": item_id, "nome": nome}

