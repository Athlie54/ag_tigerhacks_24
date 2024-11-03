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
    #maincontroller.openSheep()
    #here's the sheep doin a little dance using the animation controller
    animation = animationController.animationController(sheepView)

    
    while True:
        sheepView.TransWindow("TransSheep\\", "SheepEatBodyTrans.gif", 0, "TransSheep\\", "GrowthTrans.gif", 2, "TransSheep\\", "SheepEatHeadTrans.gif", 0)
        time.sleep(1)
        for i in range(15):
            sheepView.TransWindow("TransSheep\\", "SheepEatBodyTrans.gif", 0, "TransSheep\\", "GrowthTrans.gif", i/5, "TransSheep\\", "SheepEatHeadTrans.gif", i)
            time.sleep(1)