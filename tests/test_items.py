from fastapi.testclient import TestClient

from api.main import app
from api.routers.items import fake_items_db

client = TestClient(app)






def test_get_items():
    response = client.get("/items/", headers={"x-token": "fake-super-secret-token"})
    assert response.status_code == 200, response.text
    assert response.json() == fake_items_db
