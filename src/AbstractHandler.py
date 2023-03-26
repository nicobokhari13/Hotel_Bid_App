from __future__ import annotations
from abc import ABC, abstractmethod

class AbstractHandler(ABC):
    
    successor: AbstractHandler = None
    
    def __init__(self, numRooms):
        self.numRooms = numRooms
    
    def setSuccessor(self, handler: AbstractHandler):
        self.successor = handler
        
    def provideRoom(self):
        self.numRooms -= 1
    
    @abstractmethod
    def handleRequest(self, bid:float):
        pass