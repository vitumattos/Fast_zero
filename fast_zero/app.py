from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from fast_zero.schemas import (
    Message,
    UserBD,
    UserList,
    UserPublic,
    UserSchemas,
)

app = FastAPI()

database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'hello, world!'}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchemas):
    user_with_id = UserBD(
        id=len(database) + 1,
        **user.model_dump()
    )
    database.append(user_with_id)

    return user_with_id


@app.get('/users/', response_model=UserList)
def read_user():
    return {'users': database}


@app.get('/users/{user_id}', response_model=UserPublic)
def read_only_user(user_id: int):
    if user_id < 1 and user_id > (len(database)):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='User not found')
    return database[user_id - 1]


@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: UserSchemas):
    if user_id < 1 and user_id > (len(database)):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='User not found')
    user_with_id = UserBD(**user.model_dump(), id=user_id)
    database[user_id - 1] = user_id

    return user_with_id


@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int):
    if user_id < 1 and user_id > (len(database)):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='User not found')

    user_with_id = database[user_id - 1]
    del database[user_id - 1]
    return {'message': 'User deleted'}
