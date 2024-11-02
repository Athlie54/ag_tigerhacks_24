import tkinter
from tkinter import *
import mainViews
import mainController
import sheepViews


if __name__ == '__main__':
    mainView = mainViews.mainViews()
    sheepView = sheepViews.sheepViews()
    maincontroller = mainController.mainController(mainView,sheepView)
    mainView.setController(maincontroller)
    maincontroller.openMainMenu()