from app import app

def test_inicio():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert "funcionando" in resp.get_data(as_text=True).lower()
