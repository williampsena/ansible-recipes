from api import app


def test_coin_flip_route():
    response = app.test_client().get('/')

    assert response.status_code == 200