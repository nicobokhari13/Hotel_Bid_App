from AbstractHandler import *

class StandardHandler(AbstractHandler):
    
    def __init__(self, rooms):
        super().__init__(rooms)
    
    def handleRequest(self, bid:float):
        if bid < 80.0: # if the bid is not within range, return with rejection
            return "Bid rejected: bid is not enough for any room. Please enter a new bid price"
        if bid >= 80.0: #if the bid is within range, 
            if self.numRooms: #if there is a room, give one and return
                self.provideRoom()
                return "Success! You have booked a Standard Room"
            #if there are no Standard Rooms left, return that all Standard rooms are booked
            return "Sorry, all Standard rooms have been booked"
        return None