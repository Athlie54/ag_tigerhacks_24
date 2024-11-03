import tkinter
from tkinter import *
import mainViews
import mainController
import sheepViews
import animationController
import time


if __name__ == '__main__':
    mainView = mainViews.mainViews()
    sheepView = sheepViews.sheepViews()
    maincontroller = mainController.mainController(mainView, sheepView)
    mainView.setController(maincontroller)
    sheepView.setController(maincontroller)
    maincontroller.openSheep()
    #here's the sheep doin a little dance using the animation controller
    animation = animationController.animationController(sheepView)
    time.sleep(2)
    animation.SheepGrowth(3)