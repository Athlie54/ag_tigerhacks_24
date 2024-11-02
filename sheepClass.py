# sheep class

class Sheep:
    def __init__(self,sheepName):
        self.stage = 0 # stage of wool growth
        self.eating = False # whether or not eating animation is going
        self.name = sheepName # user entered sheep name
    
    def GetStage(self):
        return self.stage 
    
    def GetEating(self):
        return self.eating
    
    def GetName(self):
        return self.name

    def Eat(self):
        self.eating = True
        # eating animation happens
        # for a few seconds
        self.eating = False