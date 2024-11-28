from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_deve_retornar_ok_e_olar_mundo():
    client = TestClient(app)  # arrenger (organização)

    response = client.get('/')  # action

    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {'message': 'hello, world!'}
