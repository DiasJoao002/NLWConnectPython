import pytest
from .eventos_repository import EventosRepository

# Testes de integração -> Integra o projeto com o Banco de Dados
@pytest.mark.skip("Insert in DB")
def test_insert_eventos():
    event_name = "eventoTeste"
    event_repo = EventosRepository()

    event_repo.insert(event_name)

@pytest.mark.skip("Select in DB")
def test_select_event():
    event_name = "eventoTeste"
    evet_repo = EventosRepository()

    event = evet_repo.select_event(event_name)