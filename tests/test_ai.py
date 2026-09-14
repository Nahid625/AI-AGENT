import src.routes.ai_router as ai_router


def test_ask_creates_session(client, auth_headers, monkeypatch):
    monkeypatch.setattr(ai_router, "ask_question", lambda *a, **k: "stub answer")
    r = client.post("/AI/ask", data={"content": "hello world"}, headers=auth_headers)
    assert r.status_code == 200
    body = r.json()
    assert body["answer"] == "stub answer"
    assert body["session_id"]
    assert body["title"].startswith("hello world")
