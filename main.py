from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hi cutie !"}

@app.post("/createpost")
def create_post(payload: dict = Body(...)):
    return {"title":f"{payload["post_title"]}", "content": f"{payload["post_content"]}"}