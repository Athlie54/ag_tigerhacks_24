import sheepViews
import time

class animationController:
    
    waitTime = 0.1
    
    # INIT, BLASTER AND SETTERS
    def __init__(self, sheepview):
        self.sheepview = sheepview
        self.layer1 = ["TransSheep\\", "SheepEatBodyTrans.gif", 0]
        self.layer2 = ["TransSheep\\", "GrowthTrans.gif", 0]
        self.layer3 = ["TransSheep\\", "SheepEatHeadTrans.gif", 0]
        
    def blastLayersToSheep(self):
        self.sheepview.TransWindow(self.layer1[0], self.layer1[1], self.layer1[2], self.layer2[0], self.layer2[1], self.layer2[2], self.layer3[0], self.layer3[1], self.layer3[2])
        
    def setLayer1(self, gif_path, gif_file_name, current_frame):
        self.layer1[0] = gif_path
        self.layer1[1] = gif_file_name
        self.layer1[2] = current_frame
        
    def setLayer2(self, gif_path, gif_file_name, current_frame):
        self.layer2[0] = gif_path
        self.layer2[1] = gif_file_name
        self.layer2[2] = current_frame
        
    def setLayer3(self, gif_path, gif_file_name, current_frame):
        self.layer3[0] = gif_path
        self.layer3[1] = gif_file_name
        self.layer3[2] = current_frame
        
    #STATIC POSES AND SUCH
    
    def SheepGrowth(self, level):
        self.setLayer2("TransSheep\\", "GrowthTrans.gif", level)
    
    def SheepIdle(self):
        self.setLayer1("TransSheep\\", "SheepEatBodyTrans.gif", 0)
        self.setLayer3("TransSheep\\", "SheepEatHeadTrans.gif", 0)
    
    #ANIMATIONS (TIMED)
    
    def SheepEat(self):
        self.setLayer1("TransSheep\\", "SheepEatBodyTrans.gif", 0)
        self.setLayer3("TransSheep\\", "SheepEatHeadTrans.gif", 0)
        for i in range(15):
            self.setLayer3("TransSheep\\", "SheepEatHeadTrans.gif", i)
            self.blastLayersToSheep()
            time.sleep(self.waitTime)
            
        self.SheepIdle()
        
    def SheepShocked(self):
        self.setLayer1("TransSheep\\", "SheepEatTrans.gif", 0)
        self.blastLayersToSheep()
        for i in range(10):
            self.setLayer3("TransSheep\\", "LightningTrans.gif", i)
            self.blastLayersToSheep()
            time.wait(self.waitTime)
        for i in range(9):
            self.setLayer1("TransSheep\\", "ShockedSheep.gif", i)
            self.setLayer3("TransSheep\\", "LightningTrans.gif", 10+i)
            self.blastLayersToSheep()
            time.wait(self.waitTime)
        for i in range(15):
            self.setLayer1("TransSheep\\", "ShockedSheep.gif", 9+i)
            self.setLayer3("TransSheep\\", "LightningTrans.gif", 16-i)
            self.blastLayersToSheep()
            time.wait(self.waitTime)
        self.SheepIdle()