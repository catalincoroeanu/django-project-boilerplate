from django.test import Client


def test_home():
    client = Client()
    response = client.get('/')
    assert response.status_code == 200
