from abc import ABC,abstractmethod
from pygame.event import Event
class Tcomponent(ABC):
    @abstractmethod
    def handle_event(self,event:Event):
        pass
    @abstractmethod
    def draw(self):
        pass
