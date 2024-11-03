import sheepViews
import time

class animationController:
    
    waitTime = 0.1
    
    # INIT, BLASTER AND SETTERS
    def __init__(self, sheepview):
        self.sheepview = sheepview
        #self.layer1 = ["TransSheep\\", "SheepEatBodyTrans.gif", 0]
        #self.layer2 = ["TransSheep\\", "GrowthTrans.gif", 0]
        #self.layer3 = ["TransSheep\\", "SheepEatHeadTrans.gif", 0]
        self.layer1Frame = 0
        self.layer2Frame = 0
        self.layer3Frame = 0
        
    def blastLayersToSheep(self):
        self.sheepview.TransWindow(self.layer1Frame,self.layer2Frame,self.layer3Frame)#self.layer1[0], self.layer1[1], self.layer1[2], self.layer2[0], self.layer2[1], self.layer2[2], self.layer3[0], self.layer3[1], self.layer3[2]
        
    def setLayer1(self, index):#gif_path, gif_file_name, current_frame
        self.layer1Frame = index
        #self.layer1[0] = gif_path
        #self.layer1[1] = gif_file_name
        #self.layer1[2] = current_frame
        
    def setLayer2(self, index):
        self.layer2Frame = index
        # self.layer2[0] = gif_path
        # self.layer2[1] = gif_file_name
        # self.layer2[2] = current_frame
        
    def setLayer3(self, index):
        self.layer3Frame = index
        # self.layer3[0] = gif_path
        # self.layer3[1] = gif_file_name
        # self.layer3[2] = current_frame
        
    #STATIC POSES AND SUCH
    
    def SheepGrowth(self, level):
        self.setLayer2(level)#"TransSheep\\", "GrowthTrans.gif"
    
    def SheepIdle(self):
        self.setLayer1(0)#"TransSheep\\", "SheepEatBodyTrans.gif", 0
        self.setLayer3(0)#"TransSheep\\", "SheepEatHeadTrans.gif", 0
    
    #ANIMATIONS (TIMED)
    
    def SheepEat(self):
        self.setLayer1(0)#"TransSheep\\", "SheepEatBodyTrans.gif"
        self.setLayer3(0)#"TransSheep\\", "SheepEatHeadTrans.gif", 
        for i in range(15):
            self.setLayer3(i)#"TransSheep\\", "SheepEatHeadTrans.gif", 
            self.blastLayersToSheep()
            time.sleep(self.waitTime)
            
        self.SheepIdle()
        
    def SheepShocked(self):
        self.setLayer1(0+1)#"TransSheep\\", "SheepEatTrans.gif", 
        self.blastLayersToSheep()
        for i in range(10):
            self.setLayer3(i+15)#"TransSheep\\", "LightningTrans.gif", 
            self.blastLayersToSheep()
            time.wait(self.waitTime)
        for i in range(9):
            self.setLayer1(i+2)#"TransSheep\\", "ShockedSheep.gif", 
            self.setLayer3(10+i+15)#"TransSheep\\", "LightningTrans.gif", 
            self.blastLayersToSheep()
            time.wait(self.waitTime)
        for i in range(15):
            self.setLayer1(9+i+2)#"TransSheep\\", "ShockedSheep.gif", 
            self.setLayer3(16-i+15)#"TransSheep\\", "LightningTrans.gif", 
            self.blastLayersToSheep()
            time.wait(self.waitTime)
        self.SheepIdle()