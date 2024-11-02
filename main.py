import tkinter
from tkinter import *
import mainViews
import mainController
import sheepViews


if __name__ == '__main__':
    mainView = mainViews.mainViews()
    sheepBodyView = sheepViews.sheepViews('SheepAnimations\\','SheepEatBodyOnly.gif',1)
    sheepWoolView = sheepViews.sheepViews('SheepAnimations\\','growth.gif',3)
    sheepHeadView = sheepViews.sheepViews('SheepAnimations\\','SheepEatHeadOnly.gif',3)
    maincontroller = mainController.mainController(mainView,[sheepBodyView,sheepWoolView,sheepHeadView])
    mainView.setController(maincontroller)
    maincontroller.openMainMenu()