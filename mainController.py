# main program
import sheepViews
import mainViews

class mainController:
    def __init__(self,mainview,sheepview):
        self.mainview = mainview
        self.sheepview = sheepview

    def openSheep(self):
        self.sheepview.TransWindow('SheepAnimations\\', 'SheepEat.gif', 0, 3)
        #self.sheepview.TransWindow('SheepAnimations\\', 'growth.gif', 3, 3)

    def openMainMenu(self):
        self.mainview.MainMenu()

    def closeSheep(self):
        self.sheepview.window.quit

    def closeMainMenu(self):
        self.mainview.root.quit