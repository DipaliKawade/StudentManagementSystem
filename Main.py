from fastapi import FastAPI
from Routes.stdroutes import router

app  = FastAPI()

app.include_router(router)

@app.get("/")
def greet():
    return {"message":"hello"}