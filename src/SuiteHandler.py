from AbstractHandler import *

class SuiteHandler(AbstractHandler):
    
    def __init__(self, rooms):
        super().__init__(rooms)
        
    def handleRequest(self, bid:float):
        pass