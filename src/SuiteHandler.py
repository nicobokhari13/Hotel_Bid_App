from AbstractHandler import *

class SuiteHandler(AbstractHandler):
    
    def __init__(self, rooms):
        super().__init__(rooms)
        
    def handleRequest(self, bid:float):
        if bid >= 280.0: #if the bid is within range
            if self.numRooms: # if there is a room, give one and return
                self.provideRoom()
                return "Success! You have booked a Suite Room"
            if self.successor: # if there are no rooms, the bid is still high enough to afford the successor rooms
                return self.successor.handleRequest(bid) #forward to successor if one exists
        else: # if the bid is not within range
            if self.successor: # bid must be lower, so forward to successor that has lower range
                return self.successor.handleRequest(bid)
        return None # return None for debugging purposes