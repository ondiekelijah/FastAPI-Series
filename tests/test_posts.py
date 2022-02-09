from app import schemas


def test_get_all_posts(client, init_posts):
    res = client.get("/")
    assert res.status_code == 200



def test_get_one_post(client, init_posts):

    res = client.get(f"/{init_posts[0].id}")

    post = res.json()

    assert res.status_code == 200
    assert post["id"] == init_posts[0].id
    assert post["title"] == init_posts[0].title
    assert post["content"] == init_posts[0].content


def test_create_post(client, init_posts):

    data = {"title": "new title", "content": "new content"}

    res = client.post("/", json =data )

    new_post = schemas.Post(**res.json())

    assert new_post.title == data["title"]
    assert new_post.content == data["content"]
    assert res.status_code == 201



def test_update_post(client, init_posts):

    data = {"title": "Updated title", "content": "updated content"}

    res = client.put(f"/{init_posts[0].id}", json =data)


    updated_post = schemas.Post(**res.json())

    assert updated_post.title == data["title"]
    assert updated_post.content == data["content"]
    assert res.status_code == 200




def test_delete_post(client, init_posts):

    res = client.delete(f"/{init_posts[0].id}")

    assert res.status_code == 204

