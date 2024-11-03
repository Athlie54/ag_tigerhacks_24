# main program
import sheepViews
import mainViews
import taskClass
import sheepClass

class mainController:
    def __init__(self,mainview,sheepview):
        self.mainview = mainview
        self.sheepview = sheepview
        self.currentTask = None
        self.currentSheep = None

    def openSheep(self):
        self.sheepview.TransWindow('SheepAnimations\\', 'SheepEatNew.gif', 5)
        #self.sheepview.TransWindow('SheepAnimations\\', 'Growth.gif', 3)

    def openMainMenu(self):
        self.mainview.MainMenu()

    def closeSheep(self):
        self.sheepview.window.quit

    def closeMainMenu(self):
        self.mainview.root.quit

    def setTaskAndSheep(self,sheep,task,workTimeHours,workTimeMinutes,breakTimeHours,breakTimeMinutes):
        self.currentTask = taskClass.Task(task,int(workTimeHours)*3600+int(workTimeMinutes)*60,int(breakTimeHours)*3600+int(breakTimeMinutes)*60)
        self.currentSheep = sheepClass.Sheep(sheep)
        #self.closeMainMenu() # fix this one
        #self.openSheep()