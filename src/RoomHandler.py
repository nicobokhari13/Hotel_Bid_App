from abc import ABC

class RoomHandler(ABC):
    _successor:RoomHandler
    numRooms:int
    
    @abstractmethod
    def handleRequest(self, bid: float):
        ...
    
    
    
