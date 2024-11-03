# task class, gets the task name, time to work, time to rest

import time

class Task:
    def __init__(self, taskName, timeToWork, timeToRest):
        self.taskName = taskName
        self.timeToWork = timeToWork
        self.timeToRest = timeToRest
        self.workStart = 0
        # self.timeRemaining = 0
        self.restStart = 0
        self.isWorking = True
        #print(self.taskName,self.timeToWork,self.timeToRest)

    # if param given is 0, then user is working; if 1, user is resting
    def setState(self, state):
            if(state==0): # working
                self.workStart = time.time()
                self.work()
            elif(state==1): # resting
                self.restStart = time.time()
                self.rest()


    def rest(self):
        self.isWorking = False
        # self.timeRemaining = self.timeToRest
        time.sleep(self.getTimeToRest())


    def work(self):
        self.isWorking = True
        # self.timeRemaining = self.timeToWork
        time.sleep(self.getTimeToWork())

    def getTaskName(self):
        return self.taskName

    def getTimeToWork(self):
        return self.timeToWork

    def getTimeToRest(self):
        return self.timeToRest

    # def getTimeRemaining(self):
    #     return self.timeRemaining

    def getWorkStart (self):
        return self.workStart

    def getRestStart (self):
        return self.restStart

    def getIsWorking(self):
        return self.isWorking

