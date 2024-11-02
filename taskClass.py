# task class, gets the task name, time to work, time to rest

import datetime

class Task:
    def __init__(self, taskName, timeToWork, timeToRest):
        self.taskName = taskName
        self.timeToWork = timeToWork
        self.timeToRest = timeToRest
        self.timeStarted = datetime.datetime.now()
        self.timeRemaining = None
        self.timeEnded = None
        self.isWorking = True

    def start(self):
        self.timeStarted = datetime.datetime.now()
        self.timeRemaining = self.timeToWork
        self.isWorking = True

    def stop(self):
        self.timeEnded = datetime.datetime.now()
        self.timeRemaining = None
        self.isWorking = False

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
