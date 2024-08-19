from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

 
@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/posts")
def getPosts():
    return {"data": "These are your posts"}


@app.post("/createposts")
def createPost(payload: dict = Body(...)):
    print(payload)
    return {"new_post": f"title: {payload['title']} | content: {payload['content']}"}