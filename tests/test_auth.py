def test_signup_success(client, signup_payload):
    r = client.post("/user/signup", json=signup_payload())
    assert r.status_code == 200
    assert r.json()["user"]["email"] == "test@example.com"


def test_signup_duplicate(client, signup_payload):
    client.post("/user/signup", json=signup_payload())
    r = client.post("/user/signup", json=signup_payload())
    assert r.status_code == 400


def test_signup_short_password(client, signup_payload):
    r = client.post("/user/signup", json=signup_payload(hashed_password="short"))
    assert r.status_code == 400


def test_login_success(client, signup_payload):
    client.post("/user/signup", json=signup_payload())
    r = client.post("/user/login", json={"email": "test@example.com", "password": "password123"})
    assert r.status_code == 200
    assert r.json()["user"]["token"]


def test_login_wrong_password(client, signup_payload):
    client.post("/user/signup", json=signup_payload())
    r = client.post("/user/login", json={"email": "test@example.com", "password": "wrongpass"})
    assert r.status_code == 401


def test_login_unknown_user(client):
    r = client.post("/user/login", json={"email": "nobody@example.com", "password": "password123"})
    assert r.status_code == 404
