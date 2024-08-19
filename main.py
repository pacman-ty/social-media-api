from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

# schema for posts 
class Post(BaseModel):
    title: str
    content: str 
    published: bool = True
    rating: Optional[int] = None

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/posts")
def getPosts():
    return {"data": "These are your posts"}

@app.get("/posts/{id}")
def getPosts():
    return {"data": "These are your posts"}

@app.put("/posts/{id}")
def updatePosts():
    return

@app.delete("/posts/{id}")
def deletePosts():
    return


@app.post("/posts")
def createPost(post: Post):
    print(post)
    print(post.model_dump())

    return {"post": f"title: {post.title} | content: {post.content}"}

