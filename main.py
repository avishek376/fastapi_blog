from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()  # Create an instance of FastAPI


@app.get("/")  # Define a route
def index():
    return {"message": "Hello, World!"}


@app.get("/blog")
def blog(limit: int = 10, published_status: bool = False, sort: Optional[str] = None):
    if published_status:
        return {"data": f"Blog list of {limit} items, publish status is {published_status}"}
    else:
        return {"data": "Not published yet..."}


@app.get("/blog")
def blog():
    return {"data": "Blog list"}


@app.get("/blog/{id}")
def get_blog(id: int):
    return {"data": id}


class Blog(BaseModel):
    title: str
    body: str
    is_published: Optional[bool]


@app.post("/blog")
def create_blog(blog: Blog):
    return {"data": f"blog is created successfully with title {blog.title}"}
