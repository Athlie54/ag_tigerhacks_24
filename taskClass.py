# task class, gets the task name, time to work, time to rest

import time

class Task:
    def __init__(self, taskName, timeToWork, timeToRest):
        self.taskName = taskName
        self.timeToWork = timeToWork
        self.timeToRest = timeToRest
        self.timeStarted = 0
        self.timeRemaining = 0
        self.timeEnded = ""
        self.isWorking = True
        #print(self.taskName,self.timeToWork,self.timeToRest)

    # def start(self):
    #     self.timeStarted = datetime.datetime.now()
    #     self.timeRemaining = self.timeToWork
    #     self.isWorking = True

    # def stop(self):
    #     self.timeEnded = datetime.datetime.now()
    #     self.timeRemaining = None
    #     self.isWorking = False

    # if param given is 0, then user is working; if 1, user is resting
    def setState(self, state):
            if(state==0):
                self.timeStarted = time.time()
                self.timeRemaining = self.timeToWork
                self.isWorking = True
            elif(state==1):
                self.timeEnded = time.time()
                self.timeRemaining = 0


    def rest(self):
        self.isWorking = False
        self.timeRemaining = self.timeToRest

    def work(self):
        self.isWorking = True
        self.timeRemaining = self.timeToWork

    def getTaskName(self):
        return self.taskName

    def getTimeToWork(self):
        return self.timeToWork

    def getTimeToRest(self):
        return self.timeToRest

    def getTimeRemaining(self):
        return self.timeRemaining

    def getTimeStarted(self):
        return self.timeStarted

    def getTimeEnded(self):
        return self.timeEnded

    def getIsWorking(self):
        return self.isWorking

