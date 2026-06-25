from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_create_order():
    # 1. Obtener el token de acceso
    login_response = client.post(
        "/token", data={"username": "admin", "password": "password123"}
    )
    token = login_response.json()["access_token"]

    # 2. Realizar la petición al endpoint protegido usando el token
    response = client.post(
        "/orders",
        json={"customer_name": "Angie", "total": 100},
        headers={"Authorization": f"Bearer {token}"},
    )

    # 3. Validar que ahora sí responda 200 OK
    assert response.status_code == 200
    assert response.json()["customer_name"] == "Angie"
