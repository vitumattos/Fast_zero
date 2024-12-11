from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from fast_zero.app import app


@pytest.fixture
def client():
    return TestClient(app)


def test_read_root_deve_retornar_ok_e_olar_mundo(client):
    response = client.get('/')  # action

    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {'message': 'hello, world!'}


def test_create_user(client):
    response = client.post('/users/', json={
        'username': 'testeusernema',
        'password': 'password',
        'email': 'test@test.com'
    })  # action

    assert response.status_code == HTTPStatus.CREATED  # assert
    assert response.json() == {
        'username': 'testeusernema',
        'email': 'test@test.com',
        'id': 1
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'testeusernema',
                'email': 'test@test.com',
                'id': 1,
            }
        ]
    }


def test_update_users(client):
    response = client.put(
        '/users/1',
        json={
            'password': '123',
            'username': 'testeusernema',
            'email': 'test@test.com',
            'id': 1
        }
    )  # action

    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {
        'username': 'testeusernema',
        'email': 'test@test.com',
        'id': 1
    }


def test_delet_users(client):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted'}
