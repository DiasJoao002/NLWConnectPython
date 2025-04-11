from abc import ABC, abstractmethod
from src.model.entities.eventos_link import EventosLink

class EventosLinkRepositoryInterface(ABC):

    @abstractmethod
    def insert(self, event_id: int, subscriber_id: int) -> str: pass
        
    # Busca no banco de dados
    @abstractmethod
    def select_events_link(self, event_id: int, subscriber_id: int) -> EventosLink: pass
        