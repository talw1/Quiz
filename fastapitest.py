from fastapi import FastAPI
import sys
import os

import test

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "name": "Sample Item"}

@app.get("/hello")
def get_hello():
    print("************** Start  **************")
    print(sys.path)
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # Add current dir


    test.test1()
    return {"hellow Tal"}