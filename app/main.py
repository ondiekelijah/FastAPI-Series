from typing import Optional
from fastapi import FastAPI, Depends, status, HTTPException
from sqlalchemy.orm import Session
from . import schemas, models, database

app = FastAPI()

# Create the database tables
models.Base.metadata.create_all(bind=database.engine)

# Root
@app.get("/")
def read_root():
    return {"Hello": "World"}


# Create a post
@app.post("/", status_code=201)
def create_post(post: schemas.PostCreate, db: Session = Depends(database.get_db)):

    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


# Fetch all
@app.get("/posts", status_code=200)
def get_posts(db: Session = Depends(database.get_db)):

    print(db.query(models.Post)) 

    return db.query(models.Post).all()


# Fetch post by ID
@app.get("/posts/{id}")
def get_post(id: int, db: Session = Depends(database.get_db)):

    post = db.query(models.Post).filter(models.Post.id == id).first()

    if not post:
        raise HTTPException(
            status_code=500,
            detail=f"Posts with id:{id} not available",
        )

    return post


# Update post
@app.put("/posts/update/{id}", status_code=200)
def update_post(
    id: int,
    updated_post: schemas.PostCreate, db: Session = Depends(database.get_db)
):
    # AttributeError: 'Post' object has no attribute 'update' -> incase we used first() here
    post_query = db.query(models.Post).filter(models.Post.id == id)
    # So instead we do it independently

    post = post_query.first()

    if post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id:{id} was not found",
        )

    post_query.update(
        updated_post.dict(),
        # synchronize_session is used for query synchronization policy 
        # for the session when the delete or update operation is performed.
        synchronize_session=False,
    )
    db.commit()

    return post_query.first()
