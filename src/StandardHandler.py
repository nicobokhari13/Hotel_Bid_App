from AbstractHandler import *

class StandardHandler(AbstractHandler):
    
    def __init__(self, rooms):
        super().__init__(rooms)
    
    def handleRequest(self, bid:float):
        if bid < 80.0:
            return "Bid rejected: bid is not enough for any room. Please enter a new bid price"
        if bid >= 80.0: 
            if self.numRooms:
                self.provideRoom()
                return "Success! You have booked a Standard Room"
            return "Sorry, all room have been booked"
        return None