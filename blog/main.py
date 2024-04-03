from fastapi import FastAPI
from . import schemas, models
from .database import engine

app = FastAPI()  # Create an instance of FastAPI

models.Base.metadata.create_all(engine)  # we are migrating tables by this


@app.post("/blog")
def create(request: schemas.Blog):
    return {"data": f"Blog is created with title as {request.title}"}
