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
        self.sheepview.TransWindow(0,0,0)
        self.sheepview.setup_menu()

    def openMainMenu(self):
        self.mainview.MainMenu()

    def closeSheep(self):
        sView = Tk(self.sheepview.window)
        sView.quit

    def closeMainMenu(self):
        mainRoot = self.mainview.getRoot()
        mainRoot.quit()

    def setTaskAndSheep(self,sheep,task,workTime,breakTime):
        cTask = taskClass.Task(task,workTime,breakTime)
        self.currentTask = cTask
        print("Going!")
        self.currentSheep = sheepClass.Sheep(sheep)
        self.closeMainMenu() # fix this one
        #self.openSheep()

    #def tempHideSheep(self):
        #self.sheepview. #something
    
    def completeTask(self):
        self.currentTask = None
        self.currentSheep = None
        self.closeSheep()
        self.openMainMenu()
    
    