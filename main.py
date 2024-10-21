from random import randint
from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

my_data = [{"title": "abc", "content": "cont1", "rating": 1, "id": 0}]
class Post(BaseModel):
    id: int
    title: str
    content: str
    rating: Optional[int] = None

my_post = [{}]
@app.get("/")
async def root():
    return {"message":"Hi cutie !"}

@app.post("/posts")
def create_post(new_post: Post):
    new_post = new_post.model_dump()
    new_post["id"] = randint(0,100)
    print(new_post)
    my_data.append(new_post)
    # my_data.model_dump()
    return {"data":my_data}