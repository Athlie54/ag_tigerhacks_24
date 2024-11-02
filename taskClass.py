# task class, gets the task name, time to work, time to rest

import datetime

class Task:
    def __init__(self, taskName, timeToWork, timeToRest):
        self.taskName = taskName
        self.timeToWork = timeToWork
        self.timeToRest = timeToRest
        self.timeWorked = 0
        self.timeRested = 0
        self.timeStarted = datetime.datetime.now()
        self.timeEnded = None
        self.isWorking = True
        self.isResting = False

    def start(self):
        self.timeStarted = datetime.datetime.now()
        self.isWorking = True
        self.isResting = False

    def stop(self):
        self.timeEnded = datetime.datetime.now()
        self.isWorking = False
        self.isResting = False

    def rest(self):
        self.timeRested = self.timeRested + 1
        self.isResting = True
        self.isWorking = False

    def work(self):
        self.timeWorked = self.timeWorked + 1
        self.isWorking = True
        self.isResting = False

    def getTaskName(self):
        return self.taskName

    def getTimeToWork(self):
        return self.timeToWork

    def getTimeToRest(self):
        return self.timeToRest

    def getTimeWorked(self):
        return self.timeWorked

    def getTimeRested(self):
        return self.timeRested

    def getTimeStarted(self):
        return self.timeStarted

    def getTimeEnded(self):
        return self.timeEnded

    def getIsWorking(self):
        return self.isWorking

    def getIsResting(self):
        return self.isResting
