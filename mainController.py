# main program
import sheepViews
import mainViews

class mainController:
    def __init__(self,view):
        self.view = view

    def openSheep():
        sheepViews.SheepWindow

    def openMainMenu():
        mainViews.MainMenu

    def closeSheep():
        sheepViews.window.quit

    def closeMainMenu():
        mainViews.root.quit