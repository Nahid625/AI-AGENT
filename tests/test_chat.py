def test_create_and_get_session(client, auth_headers):
    r = client.post("/chat/sessions", json={"title": "My chat"}, headers=auth_headers)
    assert r.status_code == 200
    session_id = r.json()["id"]
    assert r.json()["title"] == "My chat"

    r = client.get(f"/chat/sessions/{session_id}", headers=auth_headers)
    assert r.status_code == 200
    assert r.json()["id"] == session_id


def test_list_sessions(client, auth_headers):
    client.post("/chat/sessions", json={"title": "A"}, headers=auth_headers)
    client.post("/chat/sessions", json={"title": "B"}, headers=auth_headers)
    r = client.get("/chat/sessions", headers=auth_headers)
    assert r.status_code == 200
    assert len(r.json()) == 2


def test_delete_session(client, auth_headers):
    session_id = client.post("/chat/sessions", json={"title": "X"}, headers=auth_headers).json()[
        "id"
    ]
    assert client.delete(f"/chat/sessions/{session_id}", headers=auth_headers).status_code == 200
    assert client.get(f"/chat/sessions/{session_id}", headers=auth_headers).status_code == 404


def test_requires_auth(client):
    assert client.get("/chat/sessions").status_code in (401, 403)
