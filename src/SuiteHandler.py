from AbstractHandler import *

class SuiteHandler(AbstractHandler):
    
    def __init__(self, rooms):
        super().__init__(rooms)
        
    def handleRequest(self, bid:float):
        if bid >= 280.0:
            if self.numRooms:
                self.provideRoom()
                return "Success! You have booked a Suite Room"
            if self.successor:
                return self.successor.handleRequest(bid)
        else:
            if self.successor:
                return self.successor.handleRequest(bid)
        return None