
from src.model.entities.eventos import Eventos
from abc import ABC, abstractmethod
 
class EventosRepositoryInterface(ABC):
    @abstractmethod
    def insert(self, event_name: str) -> None: pass
        
    # Busca no banco de dados
    @abstractmethod
    def select_event(self, event_name: str) -> Eventos: pass
        