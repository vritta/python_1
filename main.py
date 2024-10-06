from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    rating: Optional[int] = None

@app.get("/")
async def root():
    return {"message":"Hi cutie !"}

@app.post("/createpost")
def create_post(new_post: Post):
    print(new_post)
    return new_post.model_dump()
    # return {"title":f"{new_post["title"]}", "content": f"{new_post["content"]}"}