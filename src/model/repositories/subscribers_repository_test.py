import pytest
from .subscribers_repository import SubscribersRepository

@pytest.mark.skip("Insert in DB")
def test_insert():
    subscriber_info = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "evento_id": 3
    }

    subs_repo = SubscribersRepository()
    subs_repo.insert(subscriber_info)

@pytest.mark.skip("Select in DB")
def test_select_subscriber():
    email = "john.doe@example.com"
    event_id = 3

    subs_repo = SubscribersRepository()
    respota = subs_repo.select_subscriber(email, event_id)
    print(respota.nome)
