import tkinter
from tkinter import *
import mainViews
import mainController
import sheepViews
import animationController

if __name__ == '__main__':
    window = tkinter.Tk()
    mainView = mainViews.mainViews()
    sheepView = sheepViews.sheepViews(window)
    maincontroller = mainController.mainController(mainView, sheepView)
    mainView.setController(maincontroller)
    sheepView.setController(maincontroller)
    animation = animationController.animationController(sheepView)
    
    def update_sheep():
        sheepView.TransWindow("TransSheep\\", "SheepEatBodyTrans.gif", 0,
                              "TransSheep\\", "GrowthTrans.gif", 2,
                              "TransSheep\\", "SheepEatHeadTrans.gif", 0)
        window.after(1000, update_sheep_sequence, 0)

    def update_sheep_sequence(i):
        if i < 15:
            sheepView.TransWindow("TransSheep\\", "SheepEatBodyTrans.gif", 0,
                                  "TransSheep\\", "GrowthTrans.gif", 1,
                                  "TransSheep\\", "SheepEatHeadTrans.gif", i)
            window.after(1000, update_sheep_sequence, i + 1)
        else:
            window.after(1000, update_sheep)

    update_sheep()
    window.mainloop()