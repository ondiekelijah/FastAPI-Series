from typing import Optional
from fastapi import FastAPI, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from . import schemas, models, database


app = FastAPI()

# Create the database tables

models.Base.metadata.create_all(bind=database.engine)


@app.get("/")
def get_posts(db: Session = Depends(database.get_db)):
    posts = db.query(models.Post).all()

    if not posts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No posts available yet",
        )

    return posts


@app.get("/{id}")
def get_post(id: int, db: Session = Depends(database.get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Posts from user with id:{id} not available",
        )

    return post


@app.post("/",status_code=status.HTTP_201_CREATED)
def create_post(post: schemas.Post, db: Session = Depends(database.get_db)):

    new_post = models.Post(**post.dict())

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


@app.put("/{id}")
def update_post(
    id: int, updated_post: schemas.Post, db: Session = Depends(database.get_db)
):

    post_query = db.query(models.Post).filter(models.Post.id == id)

    post = post_query.first()

    if post == None:
        raise HTTPException(
            status_code=404, detail=f"post with id:{id} is not available"
        )

    post_query.update(updated_post.dict())

    db.commit()

    return post_query.first()


@app.delete("/{id}")
def delete_post(id: int, db: Session = Depends(database.get_db)):

    post_query = db.query(models.Post).filter(models.Post.id == id)

    post = post_query.first()

    if post == None:
        raise HTTPException(
            status_code=404, detail=f"post with id:{id} is not available"
        )

    post_query.delete()
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
