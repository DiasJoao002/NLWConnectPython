import pytest
from .eventos_link_repository import EventosLinkRepository

@pytest.mark.skip("Insert in DB")
def test_insert_events_link():
    event_id = 12
    subs_id = 18
    event_link_repo = EventosLinkRepository()

    event_link_repo.insert(event_id, subs_id)