def test_root_health(client):
    r = client.get("/AI/")
    assert r.status_code == 200
    assert r.json() == {"message": "API is working"}
