# main program
import sheepViews
import mainViews
import taskClass
import sheepClass
from tkinter import *

class mainController:
    def __init__(self,mainview,sheepview):
        self.mainview = mainview
        self.sheepview = sheepview
        self.currentTask = None
        self.currentSheep = None

    def openSheep(self):
        self.sheepview.TransWindow('TransSheep\\', 'SheepEatBodyTrans.gif', 0, 'TransSheep\\', 'GrowthTrans.gif', 0, 'TransSheep\\', 'SheepEatHeadTrans.gif', 0)

    def openMainMenu(self):
        self.mainview.MainMenu()

    def closeSheep(self):
        sView = Tk(self.sheepview.window)
        sView.quit

    def closeMainMenu(self):
        self.mainview.root.quit

    def setTaskAndSheep(self,sheep,task,workTimeHours,workTimeMinutes,breakTimeHours,breakTimeMinutes):
        self.currentTask = taskClass.Task(task,int(workTimeHours)*3600+int(workTimeMinutes)*60,int(breakTimeHours)*3600+int(breakTimeMinutes)*60)
        self.currentSheep = sheepClass.Sheep(sheep)
        #self.closeMainMenu() # fix this one
        #self.openSheep()

    #def tempHideSheep(self):
        #self.sheepview. #something
    
    def completeTask(self):
        self.currentTask = None
        self.currentSheep = None
        self.closeSheep()
        self.openMainMenu()
    
    