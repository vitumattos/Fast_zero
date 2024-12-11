import pytest
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from fast_zero.models import User, table_register


@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')
    table_register.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    table_register.metadata.drop_all(engine)


def test_create_user(session):
    user = User(username='vitor',
                email='vitor@email.com',
                password='123')

    session.add(user)
    session.commit()

    result = session.scalar(
        select(User).where(User.email == 'vitor@email.com')
    )

    assert result.username == 'vitor'
