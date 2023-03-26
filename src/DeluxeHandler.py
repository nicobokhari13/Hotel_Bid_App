from AbstractHandler import *

class DeluxeHandler(AbstractHandler):
    
    def __init__(self, rooms):
        super().__init__(rooms)
        
    def handleRequest(self, bid:float):
        if bid < 80.0:
            return "Sorry, that bid is not enough for any room"
        if bid < 150.0: 
            if self.numRooms:
                self.provideRoom()
                return "Success! You have booked a Standard Room"
            return "Sorry, your bid can only afford a Standard Room, and we are all sold out"
        if bid == 150.0:
            if self.numRooms:
                self.provideRoom()
                return "Success! You have booked a Standard Room"
            if(self.successor):
                self.successor.handleRequest(bid)
        if bid > 150.0:
            if(self.successor):
                self.successor.handleRequest(bid)
        return None