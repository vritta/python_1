from random import randint
from typing import Optional
from fastapi import FastAPI, HTTPException, Response, status
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

my_data = [{"title": "abc", "content": "cont1", "rating": 1, "id": 0}]

def find_post(id):
    for p in my_data:
        if p["id"]==id:
            return p

class Post(BaseModel):
    id: int
    title: str
    content: str
    rating: Optional[int] = None

my_post = [{}]
@app.get("/")
async def root():
    return {"message":"Hi cutie !"}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(new_post: Post):
    new_post = new_post.model_dump()
    new_post["id"] = randint(0,100)
    print(new_post)
    my_data.append(new_post)
    # my_data.model_dump()
    return {"data":my_data}

@app.get("/posts/{id}", status_code=status.HTTP_201_CREATED)
def get_post(id: int):
    post = find_post(id)
    if not post:
        # response.status_code = status.HTTP_404_NOT_FOUND
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"post with id: {id} not found")
    # return post
    return {"post_detail":post}